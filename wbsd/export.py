"""Export the cross-reference index of every registered module to SQLite.

    out/wbsd.sqlite   (git-ignored; regenerate any time)

Tables (all keyed by `module` slug):
  blocks(module, bid, kind, owner, part, n_stmts, named_hash, shape_hash, meta)
  calls(module, src, dst, stmt, bare)            script call graph (dst = block id)
  refs(module, bid, kind, name, role, stmt)      resource references by NAME
  slots(module, bid, obj, slot, access, obj_repr, value_repr, value_kind, stmt)
  globals(module, bid, name, access, stmt)
  texts(module, kind, id, text)                  strings, quick strings, menu/dialog text
  names(module, kind, idx, name)

Example:  sqlite3 out/wbsd.sqlite \
  "select module, bid from slots where obj='party' and slot=44 and access='set'"
"""
import json
import os
import sqlite3

from . import analyze, config, queries, registry

SCHEMA = """
create table blocks(module, bid, kind, owner, part, n_stmts, named_hash, shape_hash, meta);
create table calls(module, src, dst, stmt, bare);
create table refs(module, bid, kind, name, role, stmt);
create table slots(module, bid, obj, slot, access, obj_repr, value_repr, value_kind, stmt);
create table globals(module, bid, name, access, stmt);
create table texts(module, kind, id, text);
create table names(module, kind, idx, name);
"""
INDEXES = """
create index i_calls on calls(module, dst);
create index i_refs on refs(module, kind, name);
create index i_slots on slots(module, obj, slot);
create index i_globals on globals(module, name);
create index i_blocks on blocks(module, bid);
create index i_bnh on blocks(named_hash);
"""


def write(slugs=None):
    os.makedirs(config.OUT_DIR, exist_ok=True)
    path = os.path.join(config.OUT_DIR, "wbsd.sqlite")
    if os.path.exists(path):
        os.remove(path)
    db = sqlite3.connect(path)
    db.executescript(SCHEMA)
    for slug in (slugs or registry.slugs()):
        ix = queries.get(slug)
        m = ix.mod
        rows_b, rows_c, rows_r, rows_s, rows_g = [], [], [], [], []
        for b in m.blocks:
            _e, nh, sh = analyze.fingerprints(m, b)
            meta = {k: v for k, v in b.meta.items() if isinstance(v, (int, float, str)) or v is None}
            rows_b.append((slug, b.id, b.kind, b.owner, b.part, len(b.stmts), nh, sh, json.dumps(meta)))
            x = ix.x[b.id]
            for idx, bare, n in x.calls:
                rows_c.append((slug, b.id, ix.script_bid(idx), n, int(bare)))
            for kind, idx, role, n in x.refs:
                rows_r.append((slug, b.id, kind, m.name(kind, idx) or "%s#%d" % (kind, idx), role, n))
            for objkind, access, slot, orep, vrep, vkind, n in x.slots:
                rows_s.append((slug, b.id, objkind, slot, access, orep, vrep, vkind, n))
            for g, rw, n in x.globals:
                rows_g.append((slug, b.id, m.name("global", g) or "g%d" % g, rw, n))
        db.executemany("insert into blocks values (?,?,?,?,?,?,?,?,?)", rows_b)
        db.executemany("insert into calls values (?,?,?,?,?)", rows_c)
        db.executemany("insert into refs values (?,?,?,?,?,?)", rows_r)
        db.executemany("insert into slots values (?,?,?,?,?,?,?,?,?)", rows_s)
        db.executemany("insert into globals values (?,?,?,?,?)", rows_g)
        tx = []
        for kind in ("string", "qstr"):
            tx += [(slug, kind, n, t) for n, t in m.texts.get(kind, {}).items()]
        tx += [(slug, b.kind, b.id, b.meta.get("text", "")) for b in m.blocks
               if b.kind in ("menu", "mopt", "dlg") and b.part in ("body", "cond") or (b.kind == "mopt" and b.part.endswith(":cond"))]
        db.executemany("insert into texts values (?,?,?,?)", tx)
        nm = []
        for kind, lst in m.names.items():
            nm += [(slug, kind, i, n) for i, n in enumerate(lst)]
        db.executemany("insert into names values (?,?,?,?)", nm)
        db.commit()
    db.executescript(INDEXES)
    db.commit()
    db.close()
    return "wrote %s (%.1f MB)" % (path, os.path.getsize(path) / 1e6)
