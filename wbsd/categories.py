"""Behaviour categories: what KIND of work a block does, read from its opcodes.

Used to infer the purpose of anonymous/poorly-named scripts and to cluster
blocks into systems. Each category is a set of opcode ranges/ids, chosen from
the reference table's names; they describe effects, never intent.
"""
from collections import Counter

from .opref import OPS


def _ids(*specs):
    out = set()
    for s in specs:
        if isinstance(s, tuple):
            out.update(range(s[0], s[1] + 1))
        else:
            out.add(s)
    return out


CATEGORIES = {
    # campaign map
    "party_ai": _ids((1638, 1649), (2290, 2294), 1604, 1606, 1607, 1644, 1645),
    "party_spawn": _ids(1100, 1103, 1675, 1232, 1230, 1231, 1623, 2300, 2301, 2302, 2310, 2311, 1080),
    "party_members": _ids(1610, 1612, 1613, 1615, 1617, 1618, 1619, 1630, 1631, 1633, 1650, 1652, 1653, 1654, 2156, 2157, 2160),
    "prisoners": _ids(1611, 1614, 1616, 1632, 1634, 1651, 1656, 1657, 1658, 2159, 2161, 1211, 1216, 1202, 1204),
    "map_movement": _ids(1625, 1626, 1627, 1628, 1629, 1608, 2281, 1660, 1661, 1662, 1694, 1695, 1696, 1665),
    "battle_sim": _ids(1697, 1698, 1663, 1666, 1667, 1690, 1691, 108),
    "diplomacy": _ids(1270, 2190, 2201),
    "economy": _ids(1528, 1529, 2149, 1070, 1490, 1491, 1492, 1493, 1512, 1513, 1170, 1171, 1172, 2230, 2231, 2701),
    "troop_progression": _ids(1062, 1063, 1064, (1520, 1525), 1670, 1673, 1674, 1561, 2170, 2171, 2172, 2176),
    "inventory": _ids((1530, 1544), 1509, 1510, 1511, 2165, 2167, 150, 151),
    "quests": _ids((200, 204), (1280, 1291), 2240, 2250, (2261, 2263), 1098, 1111, 1112, 1113),
    "notes_ui": _ids((1090, 1098), (1108, 1119), 2053),
    "messages": _ids(1104, 1105, 1106, 1120, 1121, 1122),
    "strings": _ids((2318, 2346)),
    "menus": _ids(2060, 2061, (2040, 2058), 1304),
    "presentation_ui": _ids((900, 991)),
    "dialog": _ids(1025, 2197, 2198, 2199, 2200, 2020, 2021, 2022, 1920, 1935, 1936),
    "encounter": _ids(1300, 1301, 1302, 1303, 1307, 2202, 2203, 2205, 39, 1019, 1020, 1201, 1203, 101, 102, 103, 104, 105, 106, 107),
    "scene_setup": _ids(1910, 1911, 1912, 1250, 1251, (1261, 1266), 1930, (1940, 1943), 2211),
    "agents": _ids((1700, 1783), 1689, 1692, 1693, 1699, (1802, 1809), 1825, 1826, 1827, 1829, (2065, 2099), 2076, 2077),
    "team_orders": _ids((1784, 1796), 1775, 1828, 1837, 1789),
    "mission_flow": _ids(1003, 1004, 1005, 1006, 1906, 1907, (2365, 2385), 2002, 2003, 2004),
    "scene_props": _ids((1800, 1891), 1974, 16, 2610, 2611, 2612, 2615, 2616, 2617),
    "positions": _ids((700, 793)),
    "effects_sound": _ids((599, 616), (1960, 1978), 1886, 1887, 1881, 1882, 1797, 1798),
    "camera": _ids((2001, 2019), 61, 62),
    "input": _ids(70, 71, 72, 73, 75, 77, 78),
    "multiplayer": _ids((380, 499), 17),
    "time": _ids(2270, 2271, 2272, 2273, 1030, 1031),
    "item_stats": _ids((2700, 2726), 1570),
    "faces": _ids((2747, 2767), 1503, 1555),
    "tableau": _ids((1980, 2000)),
}

OP_CATEGORY = {}
for _cat, _ops in CATEGORIES.items():
    for _o in _ops:
        OP_CATEGORY.setdefault(_o, _cat)


def profile(block):
    c = Counter()
    for code, _f, _ops in block.stmts:
        cat = OP_CATEGORY.get(code)
        if cat:
            c[cat] += 1
    return c


def summary(counter, top=5):
    total = sum(counter.values()) or 1
    return ", ".join("%s %d%%" % (k, round(100.0 * v / total)) for k, v in counter.most_common(top))
