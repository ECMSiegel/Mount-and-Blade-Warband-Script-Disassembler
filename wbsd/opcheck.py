"""Validate the opcode reference table against compiled corpora.

For every opcode seen in any loaded module:
  * arity  -- every observed operand count must lie in [min_arity, max_arity]
  * tags   -- operands in a typed position (troop, party, faction, item, ...)
              must not carry a DIFFERENT resource tag (variables/registers/
              locals and bare constants are fine: those are computed ids)
  * unknown -- opcodes absent from the reference table: engine-extension
              (WSE / later engine) dependencies, or corruption.
"""
from collections import Counter, defaultdict

from . import headers
from .analyze import decode
from .opref import OPS, CALL_SCRIPT

TYPED = {"troop", "party", "faction", "item", "scene", "quest", "pt", "menu",
         "prsnt", "mt", "spr", "sound", "psys", "mesh", "icon", "skill",
         "tableau", "anim", "track", "script"}
NEUTRAL_TAGS = {0, 1, 2, 17}


def check(mods):
    arity = defaultdict(Counter)          # code -> Counter(n_operands)
    tagbad = defaultdict(Counter)         # (code, pos) -> Counter(tag kind)
    tagok = Counter()
    unknown = defaultdict(Counter)        # code -> Counter(module slug)
    where = {}
    for m in mods:
        for b in m.blocks:
            for code, flags, ops in b.stmts:
                arity[code][len(ops)] += 1
                op = OPS.get(code)
                if op is None:
                    unknown[code][m.slug] += 1
                    where.setdefault((code, m.slug), b.id)
                    continue
                if code == CALL_SCRIPT:
                    continue
                for i, o in enumerate(ops[:len(op.roles)]):
                    role = op.roles[i]
                    if role not in TYPED:
                        continue
                    tag, _ = decode(o)
                    if tag in NEUTRAL_TAGS:
                        continue
                    kind = headers.TAGS.get(tag)
                    if kind == role or (role == "string" and kind in ("string", "qstr")):
                        tagok[(code, i)] += 1
                    else:
                        tagbad[(code, i)][kind] += 1
                        where.setdefault((code, i, kind), (m.slug, b.id))
    report = {"arity_mismatch": [], "tag_mismatch": [], "unknown": [], "clean": 0}
    for code, cnt in sorted(arity.items()):
        op = OPS.get(code)
        if op is None:
            continue
        bad = {n: c for n, c in cnt.items() if not (op.min_arity <= n <= op.max_arity)}
        if bad:
            report["arity_mismatch"].append((code, op.name, op.min_arity, op.max_arity, dict(cnt)))
        else:
            report["clean"] += 1
    for (code, i), cnt in sorted(tagbad.items()):
        op = OPS[code]
        report["tag_mismatch"].append((code, op.name, i, op.roles[i], dict(cnt), tagok[(code, i)],
                                       [where.get((code, i, k)) for k in cnt]))
    for code, cnt in sorted(unknown.items()):
        report["unknown"].append((code, dict(cnt), dict(arity[code]),
                                  {s: where[(code, s)] for s in cnt}))
    return report


def render(report):
    out = ["opcode reference check: %d opcodes clean on arity" % report["clean"]]
    out.append("")
    out.append("ARITY MISMATCHES (reference arity vs observed operand counts):")
    for code, name, lo, hi, cnt in report["arity_mismatch"]:
        out.append("  %5d %-40s ref %d..%s observed %s" % (code, name, lo, hi if hi < 99 else "*", cnt))
    out.append("")
    out.append("TAG MISMATCHES (typed position carrying another resource tag):")
    for code, name, i, role, cnt, ok, ex in report["tag_mismatch"]:
        out.append("  %5d %-36s arg%d(%s) bad=%s ok=%d e.g. %s" % (code, name, i, role, cnt, ok, ex[:2]))
    out.append("")
    out.append("UNKNOWN OPCODES (not in vanilla Warband reference -> engine extension / WSE):")
    for code, mods, ar, ex in report["unknown"]:
        out.append("  %5d in %s arity %s e.g. %s" % (code, mods, ar, list(ex.items())[:2]))
    return "\n".join(out)
