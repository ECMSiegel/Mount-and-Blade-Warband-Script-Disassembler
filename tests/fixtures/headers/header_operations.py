# Synthetic header for the wbtools test suite. Invented text, not a Module System
# header: it declares only the opcodes the demo fixture module uses, in the
# "name = code  # (name, args)" syntax that wbsd/build_tables.py reads.

call_script = 1  # (call_script, <script_id>, [<param>...]),
try_end = 3  # (try_end),
try_begin = 4  # (try_begin),
else_try = 5  # (else_try),
store_script_param = 23  # (store_script_param, <destination>, <script_param_no>),
eq = 31  # (eq, <value>, <value>),
gt = 33  # (gt, <value>, <value>),
troop_set_slot = 500  # (troop_set_slot, <troop_id>, <slot_no>, <value>),
troop_get_slot = 520  # (troop_get_slot, <destination>, <troop_id>, <slot_no>),
display_message = 1000  # (display_message, <string_id>, [<color>]),
assign = 2133  # (assign, <destination>, <value>),

can_fail_operations = [
  eq, gt, troop_get_slot,
]

depth_operations = [
  try_begin,
]

global_lhs_operations = [
  assign,
]
