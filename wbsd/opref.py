"""Opcode reference model built from opref_data.RAW (read-only naming layer)."""
import re

try:
    from . import opref_data
except ImportError as _e:
    if "opref_data" not in str(_e):
        raise
    raise SystemExit(
        "wbsd: the opcode/operand tables have not been built yet -- "
        "run `python3 wbsd/build_tables.py --download` (or `wb-build-tables --download`) first, "
        "or pass a Module System folder instead of --download") from None

# argument name -> semantic role
_ROLE_PATTERNS = [
    (r"^destination", "dest"),
    (r"^troop_id|^troop_dna", None),            # resolved below
    (r"^party_template_id", "pt"),
    (r"^party_id|^joiner_party_id|^host_party_id", "party"),
    (r"^faction_id", "faction"),
    (r"^item_id", "item"),
    (r"^item_type_id", "itemtype"),
    (r"^scene_id", "scene"),
    (r"^quest_id", "quest"),
    (r"^script_id", "script"),
    (r"^menu_id", "menu"),
    (r"^presentation_id", "prsnt"),
    (r"^mission_template_id", "mt"),
    (r"^scene_prop_id", "spr"),
    (r"^prop_instance_id", "propinst"),
    (r"^sound_id", "sound"),
    (r"^particle_system_id", "psys"),
    (r"^mesh_id", "mesh"),
    (r"^map_icon_id", "icon"),
    (r"^skill_id|^skill_no", "skill"),
    (r"^string_id", "string"),
    (r"^string_register|^string_no", "sreg"),
    (r"^position_no", "pos"),
    (r"^agent_id", "agent"),
    (r"^team_no", "team"),
    (r"^player_id", "player"),
    (r"^slot_no", "slot"),
    (r"^info_page_id", "infopage"),
    (r"^tableau_material_id", "tableau"),
    (r"^anim_id|^animation_id", "anim"),
    (r"^track_id", "track"),
    (r"^entry_no", "entry"),
    (r"^overlay_id|^container_overlay_id", "overlay"),
    (r"^key_id", "key"),
]

SLOT_OBJECTS = ["troop", "party", "faction", "scene", "party_template", "agent",
                "quest", "item", "player", "team", "scene_prop"]
SLOT_ACCESS = {500: "set", 520: "get", 540: "eq", 560: "ge"}


def _role(argname):
    a = argname.strip("[]<>")
    if a.startswith("troop_id") or a.startswith("troop_id_2"):
        return "troop"
    for pat, role in _ROLE_PATTERNS:
        if role and re.match(pat, a):
            return role
    return "value"


class Op(object):
    __slots__ = ("code", "name", "args", "roles", "optional", "can_fail",
                 "depth", "writes_first", "slot")

    def __init__(self, code, name, args):
        self.code = code
        self.name = name
        self.args = args
        self.roles = [_role(a) for a in args]
        self.optional = [a.startswith("[") for a in args]
        self.can_fail = False
        self.depth = False
        self.writes_first = bool(args) and self.roles[0] == "dest"
        self.slot = None  # (object_kind, access)

    @property
    def min_arity(self):
        return sum(1 for o in self.optional if not o)

    @property
    def max_arity(self):
        if any("..." in a for a in self.args):
            return 99
        return len(self.args)


def _build():
    ops = {}
    for line in opref_data.RAW.strip().splitlines():
        parts = line.split(None, 2)
        code, name = int(parts[0]), parts[1]
        args = [a.strip() for a in parts[2].split(",")] if len(parts) > 2 else []
        ops[code] = Op(code, name, args)
    by_name = {o.name: o for o in ops.values()}
    for n in opref_data.CAN_FAIL:
        if n in by_name:
            by_name[n].can_fail = True
    for n in opref_data.DEPTH:
        if n in by_name:
            by_name[n].depth = True
    for n in opref_data.GLOBAL_LHS:
        if n in by_name:
            by_name[n].writes_first = True
    for base, access in SLOT_ACCESS.items():
        for i, obj in enumerate(SLOT_OBJECTS):
            op = ops.get(base + i)
            if op is not None:
                op.slot = (obj, access)
    return ops, by_name


OPS, BY_NAME = _build()

CALL_SCRIPT = 1
TRY_END, TRY_BEGIN, ELSE_TRY = 3, 4, 5
BLOCK_OPENERS = frozenset(o.code for o in OPS.values() if o.depth)
NEG = 0x80000000
THIS_OR_NEXT = 0x40000000

# Negated comparisons render as their module-system aliases.
NEG_ALIASES = {30: "lt", 31: "neq", 32: "le"}

