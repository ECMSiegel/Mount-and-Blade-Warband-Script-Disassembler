#!/usr/bin/env python3
"""Find tests that can never fail.

    python3 tools/hollow_check.py PATH...

PATH is a test file or a folder (searched for test*.py). Exit 1 and list every problem test
(a function named test*), else exit 0. Exit 2 for a bad path or a file that does not parse.
Stdlib only; reads the files, never imports or runs them.

A test is HOLLOW unless its code that can run (nested functions included, if the test uses them)
has one of:
  * an `assert` statement whose condition is not a constant or a comparison of a thing with itself;
  * a call to self.assert*/assert_* (assertEqual, assertRaises, ...), unless every argument is a
    constant or the first two are the same expression (assertTrue(True), assertEqual(x, x));
    and a call to fail* (self.fail), which always counts;
  * a call to check*, expect*, verify* or ensure* (check(cond, label), check_x(...)) only if that
    name is imported from _support, or is a helper that can itself fail (an assert, a raise, or a
    call to such a helper) defined in the same file or in a sibling module it imports it from. subprocess.check_call / check_output count;
  * FAIL.append(...) / FAILURES.append(...) (also extend), only if the same file also asserts on
    that list or imports _support: the repo's script-style tests collect failures in a list that a
    wrapper test then requires to be empty;
  * a call with keyword check=True (subprocess.run(..., check=True));
  * `raise` of anything except a SkipTest;
  * sys.exit / exit / quit;
  * a call to a helper defined in the same file that has one of the above (helpers whose name
    starts with require or skip do not count: they only decide whether to run).

Code that can never run does not count, and a test whose only assertions are in such code is
reported as "its assertions can never run": the body of `if False` / `if 0` (or the else of
`if True`), statements after return / raise / continue / break in the same block, and a nested
def or class the test never refers to.

A test containing `assert (x, "msg")` (an assert of a tuple, always true) is reported on its own,
whatever else it asserts.

Not detected: an assertion inside a try/except that swallows it.
"""
import ast
import os
import re
import sys

ASSERT_CALL = re.compile(r"^assert([A-Z_]|$)")
PREFIX_CALL = re.compile(r"^(check|expect|verify|ensure)([A-Z_]|$)")
FAIL_CALL = re.compile(r"^fail([A-Z_]|$)")
FAIL_LIST = re.compile(r"^fail(ure)?s?$", re.I)
SKIPPERS = re.compile(r"^_*(require|skip)", re.I)


def _call_name(node):
    f = node.func
    if isinstance(f, ast.Name):
        return f.id
    if isinstance(f, ast.Attribute):
        return f.attr
    return None


def _const(test):
    """True / False for a constant condition, None when it depends on something."""
    if isinstance(test, ast.Constant):
        return bool(test.value)
    return None


def _trivial(node):
    """True for an expression that cannot be false (or whose truth no data can change)."""
    if isinstance(node, ast.Constant):
        return True
    if isinstance(node, ast.Compare) and len(node.ops) == 1 and isinstance(node.ops[0], (ast.Eq, ast.Is, ast.GtE, ast.LtE)):
        return ast.dump(node.left) == ast.dump(node.comparators[0])
    return False


def _args_trivial(call):
    """assertTrue(True), assertEqual(x, x): nothing the code under test can change."""
    pos = call.args
    if not pos:
        return False
    if all(isinstance(a, ast.Constant) for a in pos):
        return True
    return len(pos) >= 2 and ast.dump(pos[0]) == ast.dump(pos[1])


class _State(object):
    def __init__(self, list_ok):
        self.list_ok = list_ok        # FAILURES.append counts in this file
        self.found = False
        self.dead_found = False
        self.tuple_assert = False
        self.called = set()           # names of calls that can run
        self.loads = set()            # names read by code that can run
        self.nested = {}              # name -> def/class node, not yet scanned
        self.scanned = set()

    def mark(self, live):
        if live:
            self.found = True
        else:
            self.dead_found = True


def _on_call(n, st, live):
    name = _call_name(n)
    if name is None:
        return
    if live:
        st.called.add(name)
    if any(k.arg == "check" and isinstance(k.value, ast.Constant) and k.value.value is True for k in n.keywords):
        st.mark(live)
    if name in ("exit", "quit"):
        st.mark(live)
    elif FAIL_CALL.match(name):
        st.mark(live)
    elif ASSERT_CALL.match(name):
        if not _args_trivial(n):
            st.mark(live)
    elif name in ("check_call", "check_output") and isinstance(n.func, ast.Attribute) \
            and isinstance(n.func.value, ast.Name) and n.func.value.id == "subprocess":
        st.mark(live)
    elif PREFIX_CALL.match(name) and isinstance(n.func, ast.Attribute) \
            and isinstance(n.func.value, ast.Name) and n.func.value.id == "_support":
        st.mark(live)
    elif name in ("append", "extend") and isinstance(n.func, ast.Attribute) \
            and isinstance(n.func.value, ast.Name) and FAIL_LIST.match(n.func.value.id) and st.list_ok:
        st.mark(live)


def _expr(node, st, live):
    for n in ast.walk(node):
        if isinstance(n, ast.Call):
            _on_call(n, st, live)
        elif isinstance(n, ast.Name) and live and isinstance(n.ctx, ast.Load):
            st.loads.add(n.id)


def _scan(stmts, st, live):
    for s in stmts:
        if isinstance(s, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            st.nested.setdefault(s.name, s)
            continue
        if isinstance(s, ast.Assert):
            if isinstance(s.test, ast.Tuple) and s.test.elts:
                st.tuple_assert = True
            elif not _trivial(s.test):
                st.mark(live)
        elif isinstance(s, ast.Raise):
            if "SkipTest" not in (ast.dump(s.exc) if s.exc is not None else ""):
                st.mark(live)
        body_live = body_dead = live
        if isinstance(s, (ast.If, ast.While)):
            c = _const(s.test)
            body_live = live and c is not False
            body_dead = live and c is not True
        for field, val in ast.iter_fields(s):
            items = val if isinstance(val, list) else [val]
            if field in ("body", "orelse", "finalbody") and items and isinstance(items[0], ast.stmt):
                _scan(items, st, body_dead if field == "orelse" else body_live)
                continue
            for item in items:
                if isinstance(item, ast.ExceptHandler):
                    if item.type is not None:
                        _expr(item.type, st, live)
                    _scan(item.body, st, live)
                elif getattr(ast, "match_case", None) and isinstance(item, ast.match_case):
                    _scan(item.body, st, live)
                elif isinstance(item, ast.AST) and not isinstance(item, ast.stmt):
                    _expr(item, st, live)
        if isinstance(s, (ast.Return, ast.Raise, ast.Continue, ast.Break)):
            live = False


def _inspect(func, list_ok):
    """_State for one function: everything its runnable code can do."""
    st = _State(list_ok)
    _scan(func.body, st, True)
    again = True
    while again:                     # a nested def or class the test refers to is part of the test
        again = False
        for name, node in list(st.nested.items()):
            if name in st.loads and name not in st.scanned:
                st.scanned.add(name)
                body = node.body if not isinstance(node, ast.ClassDef) else \
                    [m for m in node.body if isinstance(m, (ast.FunctionDef, ast.AsyncFunctionDef))]
                if isinstance(node, ast.ClassDef):
                    for m in body:
                        _scan(m.body, st, True)
                else:
                    _scan(node.body, st, True)
                again = True
    for name, node in st.nested.items():
        if name not in st.scanned:           # never used: whatever it asserts can never run
            probe = _State(list_ok)
            _scan(node.body, probe, True)
            if probe.found:
                st.dead_found = True
    return st


def _imports_support(tree):
    ok, names = False, set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            if any(a.name.split(".")[-1] == "_support" for a in n.names):
                ok = True
        elif isinstance(n, ast.ImportFrom):
            mod = (n.module or "").split(".")[-1]
            if mod == "_support":
                ok = True
                names.update(a.asname or a.name for a in n.names)
            elif any(a.name == "_support" for a in n.names):
                ok = True
    return ok, names


def _asserts_on_list(tree):
    for n in ast.walk(tree):
        if isinstance(n, ast.Assert):
            parts = [n.test]
        elif isinstance(n, ast.Call) and _call_name(n) and ASSERT_CALL.match(_call_name(n)):
            parts = list(n.args)
        else:
            continue
        for p in parts:
            for m in ast.walk(p):
                if isinstance(m, ast.Name) and FAIL_LIST.match(m.id):
                    return True
    return False


def _sibling_able(tree, filename, seen):
    """Names this file imports from a sibling module (`from test_wbasm import check`) that can fail there."""
    names = set()
    folder = os.path.dirname(os.path.abspath(filename)) if os.path.isfile(filename) else None
    if folder is None:
        return names
    for n in ast.walk(tree):
        if isinstance(n, ast.ImportFrom) and n.module and n.module.split(".")[-1] != "_support":
            path = os.path.join(folder, n.module.split(".")[-1] + ".py")
            if os.path.isfile(path) and path not in seen:
                with open(path, "rb") as fh:
                    _o, _t, able = _analyse(fh.read(), path, seen | {path})
                names.update((a.asname or a.name) for a in n.names if able.get(a.name))
    return names


def analyse(source, filename="<src>"):
    """([(line, qualified name, reason)], number of tests) for the problem tests in `source`."""
    out, total, _able = _analyse(source, filename, {filename})
    return out, total


def _analyse(source, filename, seen):
    tree = ast.parse(source, filename)
    imported, imported_names = _imports_support(tree)
    imported_names = imported_names | _sibling_able(tree, filename, seen)
    list_ok = imported or _asserts_on_list(tree)
    funcs = []          # (qualified name, node)

    def visit(node, prefix):
        for child in ast.iter_child_nodes(node):
            if isinstance(child, ast.ClassDef):
                visit(child, prefix + child.name + ".")
            elif isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                funcs.append((prefix + child.name, child))
                visit(child, prefix + child.name + ".")
            else:
                visit(child, prefix)
    visit(tree, "")
    info = {q: _inspect(f, list_ok) for q, f in funcs}
    able = {}           # bare name -> True when a function or import of that name can fail
    for name in imported_names:
        if PREFIX_CALL.match(name) or ASSERT_CALL.match(name):
            able[name] = True
    for q, st in info.items():
        bare = q.rsplit(".", 1)[-1]
        if st.found and not SKIPPERS.match(bare):
            able[bare] = True
    changed = True
    while changed:
        changed = False
        for q, st in info.items():
            bare = q.rsplit(".", 1)[-1]
            if SKIPPERS.match(bare) or able.get(bare):
                continue
            if any(able.get(c) for c in st.called):
                able[bare] = True
                changed = True
    out, total = [], 0
    for q, f in funcs:
        bare = q.rsplit(".", 1)[-1]
        if not bare.startswith("test"):
            continue
        total += 1
        st = info[q]
        if st.tuple_assert:
            out.append((f.lineno, q, "asserts a tuple, which is always true (assert (x, msg))"))
        elif st.found or any(able.get(c) for c in st.called if c != bare):
            continue
        elif st.dead_found:
            out.append((f.lineno, q, "its assertions can never run (dead code, or a nested def it never uses)"))
        else:
            out.append((f.lineno, q, "has no assert, check, fail or raise path"))
    return out, total, able


def _files(paths):
    for p in paths:
        if os.path.isdir(p):
            for d, dirs, names in sorted(os.walk(p)):
                dirs[:] = sorted(x for x in dirs if x not in ("__pycache__", ".git"))
                for n in sorted(names):
                    if n.startswith("test") and n.endswith(".py"):
                        yield os.path.join(d, n)
        elif os.path.isfile(p):
            yield p
        else:
            raise FileNotFoundError(p)


def main(argv):
    paths = argv[1:]
    if not paths or paths[0] in ("-h", "--help"):
        print(__doc__)
        return 0 if paths else 2
    hollow, total, nfiles = [], 0, 0
    try:
        for path in _files(paths):
            with open(path, "rb") as fh:
                src = fh.read()
            try:
                found, n = analyse(src, path)
            except SyntaxError as e:
                print("%s: cannot parse: %s" % (path, e))
                return 2
            nfiles += 1
            total += n
            hollow += [(path, line, q, why) for line, q, why in found]
    except FileNotFoundError as e:
        print("no such file or folder: %s" % e)
        return 2
    for path, line, q, why in hollow:
        print("%s:%d: %s %s" % (path, line, q, why))
    print("hollow_check: %d tests in %d files, %d hollow" % (total, nfiles, len(hollow)))
    return 1 if hollow else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
