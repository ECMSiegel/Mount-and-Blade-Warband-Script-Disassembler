"""The author's own corrections, applied on top of what the generator parses
from the user's headers (see build_tables.py). This file holds no header text.

OP_SIGNATURES  opcode -> argument list (comma separated), replacing the parsed
               one. Two kinds of entry live here:
               - corpus corrections: places where the official header comment is
                 wrong or omits optional arguments (an optional arg that every
                 corpus use passes, wrong arity, copy-pasted comments), checked
                 with `wbsd opcheck`; and
               - the author's own argument-name vocabulary (value_2, position_no
                 ...), which decides how opref.py reads each argument's role.
EVENT_FIXES    trigger codes the TLD headers lack but the engine uses.
"""

# Header argument spelling -> the role vocabulary opref.py understands.
ARG_ALIASES = {
    "dest_position_no": "position_no", "source_position_no": "position_no",
    "position_register_no": "position_no", "hit_position_register": "position_no",
    "ray_position_register": "position_no", "position": "position_no",
    "team_id": "team_no", "item_kind_no": "item_id", "agent_no": "agent_id",
    "agent_id_deliverer": "agent_id", "faction_no": "faction_id",
    "troop_no": "troop_id", "troop_id_hero": "troop_id", "party_no": "party_id",
    "par_sys_id": "particle_system_id", "string_no": "string_register",
    "string": "string_id", "scene_prop_instance_id": "prop_instance_id",
    "prop_instance_no": "prop_instance_id", "rain_type": "rain_type",
}
OP_SIGNATURES = {
    1: '<script_id>,[params...]',
    16: '<destination>,[scene_prop_id],[object_type]',
    30: '<value>,<value>',
    31: '<value>,<value>',
    32: '<value>,<value>',
    50: '<destination>',
    390: '<message_type>,<value>,<value>',
    391: '<message_type>,<value>,<value>,<value>',
    392: '<message_type>,<value>,<value>,<value>,<value>',
    396: '<player_id>,<message_type>,<value>,<value>',
    397: '<player_id>,<message_type>,<value>,<value>,<value>',
    398: '<player_id>,<message_type>,<value>,<value>,<value>,<value>',
    403: '<player_id>,<value>',
    405: '<player_id>,<troop_id>',
    413: '<troop_id>',
    425: '<destination>,<team_no>,<examine_all_spawn_points>,[is_horseman]',
    426: '<team_no>,<scene_prop_kind_no>',
    427: '<team_no>,<prop_instance_id>',
    451: '<team_no>,<value>',
    453: '<team_no>,<value>',
    460: '<destination>,<player_id>',
    466: '<player_id>,<value>,<player_id>',
    529: '<destination>,<team_no>,<slot_no>',
    716: '<position_no>,<position_no_2>,<position_no_3>',
    717: '<position_no>,<position_no_2>,<position_no_3>',
    910: '<destination>,<string_id>,[flags]',
    912: '<destination>,<string_id>,[flags]',
    918: '<destination>,[mesh_id],[mesh_id_2]',
    940: '<destination>,<string_id>,[flags]',
    941: '<destination>,<string_id>,[flags]',
    943: '<destination>,[string_id],[value]',
    946: '<position_no>,<overlay_id>',
    956: '<overlay_id>,<string_no>',
    980: '<string_id>,<value>',
    1003: '[team_no]',
    1025: '<troop_id>,[troop_dna]',
    1120: '<string_id>,[string_id_2]',
    1121: '<string_id>,[string_id_2],[string_id_3]',
    1122: '<string_id>,[color],[auto_close_time]',
    1125: '<value>',
    1170: '[value]',
    1262: '[value]',
    1265: '<entry_no>,<troop_id>,<number_of_troops>,[team_no],[group_no]',
    1277: '<destination>,<faction_id>',
    1280: '<quest_id>,[giver_troop_id]',
    1492: '[value]',
    1493: '<item_id>,<value>',
    1501: '<troop_id>,<string_no>',
    1502: '<troop_id>,<string_no>',
    1539: '<troop_id>,<troop_id_2>,<probability>',
    1616: '<party_id>,<troop_id>,<number>',
    1623: '<party_id>,<party_id_2>,<value_spawn_radius>',
    1645: '<party_id>,<attraction>',
    1649: '<destination>,<party_id>',
    1660: '<party_id>,<party_id_2>',
    1662: '<party_id>,<party_id_2>',
    1667: '<party_id>,<hours>',
    1669: '<party_id>,<string_no>',
    1682: '<party_id>,<map_icon_id>,<up_down_distance>,<up_down_frequency>,<rotate_frequency>,<fade_frequency>',
    1685: '<destination>,<party_id>,<skill_id>',
    1697: '<party_id>,<attack_rounds>,<party_id_2>',
    1698: '<party_id>,<party_id_2>',
    1722: '<agent_id>,<agent_id_2>,[value],[item_id]',
    1725: '<agent_id>,[value]',
    1726: '<destination>,<agent_id>,[hand_no]',
    1727: '<destination>,<agent_id>,[value]',
    1730: '<agent_id>,<position_no>,[auto_set_z_to_ground_level],[no_rethink]',
    1748: '<agent_id>,<position_no>,[auto_set_z_to_ground_level]',
    1757: '<agent_id>,<prop_instance_id>',
    1768: '<destination>,<agent_id>,[body_part]',
    1793: '<team_no>,<agent_id>',
    1795: '<team_no>,<sub_class>,[value]',
    1799: '<position_no>,<position_no_2>',
    1810: '<destination>,<scene_prop_id>',
    1811: '<destination>,<scene_prop_id>,<instance_no>',
    1817: '<destination>,<prop_instance_id>',
    1829: '<agent_id>,<position_no>,<starting_speed>,<item_id>,<item_modifier>,<item_id_2>,<item_modifier_2>',
    1863: '<position_no>,<prop_instance_id>',
    1871: '<prop_instance_id>,<position_no>',
    1872: '<prop_instance_id>,<position_no>',
    1873: '<prop_instance_id>,<position_no>',
    1874: '<prop_instance_id>,<position_no>',
    1889: '<prop_instance_id>,<scene_prop_id>',
    1890: '<scene_prop_id>,<scene_prop_id_2>',
    1891: '<item_id>,<scene_prop_id>',
    1907: '[delay_in_seconds]',
    1910: '<scene_id>,[entry_no]',
    1942: '<mission_template_id>,<entry_no>,<item_id>',
    1964: '<string_no>,[lod_begin],[lod_end]',
    1968: '<particle_system_id>,<value_num_particles>,[value_period]',
    1971: '<item_id>,[item_modifier],[seconds_before_pruning]',
    1973: '<item_id>,[item_modifier]',
    1974: '<scene_prop_id>,[variation]',
    1976: '<item_id>,<item_modifier>,[seconds_before_pruning]',
    1978: '<string_no>,<sub_mesh_no>,[lod_begin],[lod_end]',
    1980: '<tableau_material_id>,<value>,<position_no>,<value_fixed_point>,<value_fixed_point_2>',
    1986: '<tableau_material_id>,[value]',
    1990: '<position_no>,<red_fixed_point>,<green_fixed_point>,<blue_fixed_point>',
    1991: '<position_no>,<red_fixed_point>,<green_fixed_point>,<blue_fixed_point>',
    1996: '<item_id>,<position_no>,<animation_id>,[value]',
    1999: '<item_id>',
    2001: '<mission_cam_mode>,[duration],[value]',
    2012: '<position_no>,<duration>,[value]',
    2016: '<position_no>,<value>,<duration>,[value_2]',
    2022: '<line_no>,<string_no>',
    2042: '[troop_id]',
    2043: '[exchange_leader],[party_id]',
    2051: '[troop_id]',
    2135: '<destination>,<range_high>',
    2158: '<destination>,<troop_id>',
    2159: '<destination>,[party_id]',
    2205: '<party_id>',
    2327: '<string_register>,<item_id>,[number]',
    2340: '<string_register>,<hours_to_add>',
    2346: '<string_register>,<class_id>',
    2386: '<value>',
    2387: '[value]',
    2403: '<parameter_name>,[matrix...]',
}

# Used when a header copy lacks the list (the TLD one has all three).
LIST_DEFAULTS = {
    "DEPTH": ["try_begin", "try_for_range", "try_for_range_backwards", "try_for_parties",
              "try_for_agents", "try_for_prop_instances", "try_for_players"],
    "GLOBAL_LHS": ["val_lshift", "val_rshift", "val_add", "val_sub", "val_mul",
                   "val_div", "val_max", "val_min", "val_mod"],
}
TRIGGER_SKIP = set()    # ti_* names that are not trigger codes of their own
TAG_FIXES = {}
EVENT_FIXES = {-75.0: "ti_on_switch_to_map"}
KEY_FIXES = {}


def apply_ops(ops):
    for code, args in OP_SIGNATURES.items():
        if code in ops:     # a header without this opcode just skips the fix
            ops[code] = (ops[code][0], [a for a in args.split(",") if a])


def apply_tables(tags, events, keys):
    tags.update(TAG_FIXES)
    events.update(EVENT_FIXES)
    keys.update(KEY_FIXES)
