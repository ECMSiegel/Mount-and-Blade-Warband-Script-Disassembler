# Example atlas

A worked example of the feature atlas (see [docs/ATLAS.md](../../docs/ATLAS.md)): 311 records describing gameplay
systems found in 15 Mount & Blade: Warband mods, with the overlaps between them.

- `features/<slug>.json` - one file per mod, one record per system (what it does, how it works, the scripts, slots and globals involved, evidence, confidence).
- `overlaps.json` - groups of records from different mods that implement the same mechanic.
- `FEATURE_INVENTORY.md` - generated from the above: `WB_ATLAS_DIR=examples/atlas python3 wbsd/wbsd.py inventory`.
- `modules.json` - the mods the records come from and their folder names, so you can reproduce the atlas. Copy it to the repo root as `modules.json` (git-ignored there), or point `WB_REGISTRY` at it.

Check it: `WB_ATLAS_DIR=examples/atlas python3 wbsd/wbsd.py features-check`.

## How it was made

Each module was disassembled and compared with `wbsd` (the `report`, `grep`, `text` and related commands),
and the findings were written up following the `atlas-audit` procedure in `skills/`. Every record lists the
evidence behind it (commands run, block ids, script names) and a confidence level. Records state facts about the
mod only (what a system does, how it works, what it touches, how sure we are). They carry no advice or verdict about
any other project, no platform verdicts, and no free-text notes beyond a few factual oddities, so the optional
judgement fields (value, difficulty, risk and so on) are left out.

## Credits

All the mods below belong to their authors. Native is the base game by TaleWorlds. Authors are as named on
each mod's own page (ModDB profile or Steam Workshop listing) or in the mod's own files.

| Slug | Mod | Author | Link | Records |
|---|---|---|---|---|
| `vc` | Viking Conquest | TaleWorlds Entertainment (publisher); developed by the Brytenwalda team | [Steam](https://store.steampowered.com/app/321300) / [ModDB](https://www.moddb.com/games/mount-blade-warband-viking-conquest) | 28 |
| `awoiaf` | A World of Ice and Fire | produno and the A World of Ice and Fire Dev Team | [ModDB](https://www.moddb.com/mods/a-world-of-ice-and-fire) | 23 |
| `pop` | Prophesy of Pendor 3.9.5 | Saxondragon (original author); 3.9 team led by K0nr@d | [Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=875202420) | 24 |
| `tld` | The Last Days of the Third Age | The Last Days Development Team | [Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=299974223) / [ModDB](https://www.moddb.com/mods/the-last-days) | 22 |
| `be` | Between Empires 1.0 | Sailor_Moon0 | [ModDB](https://www.moddb.com/mods/between-empires) | 25 |
| `laigle` | L'Aigle | Docm30 | [ModDB](https://www.moddb.com/mods/laigle) | 18 |
| `nw` | Napoleonic Wars | Flying Squirrel Entertainment; published by TaleWorlds Entertainment | [ModDB](https://www.moddb.com/games/mountblade-warband-napoleonic-wars) | 15 |
| `oa1860` | 1860s Old America 1.5 | GABRILDURO | [ModDB](https://www.moddb.com/mods/1860s-old-america) | 8 |
| `sw` | Star Wars Conquest | SWC Dev Team | [ModDB](https://www.moddb.com/mods/swconquest) | 18 |
| `bi` | Bellum Imperii 1.6 | gokiller | [ModDB](https://www.moddb.com/mods/bellum-imperii) | 20 |
| `acw` | The American Civil War Mod: Revived | King85 | [ModDB](https://www.moddb.com/mods/the-american-civil-war-mod-revived) | 34 |
| `acan` | Aut Caesar Aut Nihil | [BG]Maxi | [Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=1612746028) | 27 |
| `ad457` | 457 AD: Last Years of the Western Empire | 457AD team | [ModDB](https://www.moddb.com/mods/457ad) | 19 |
| `cbl` | Extended Native: Calradia's Borderlands | DouwFR | [ModDB](https://www.moddb.com/mods/extended-native-calradias-borderlands) | 11 |
| `perisno` | Perisno 1.5.0 | Perisno Development Team | [ModDB](https://www.moddb.com/mods/perisno) | 19 |

Calradia Borderlands also has a later V3.52 build (tables only); its differences are written into the `cbl` records.
`features/perisno.json` and `modules/perisno.md` were produced fresh with the shipped `skills/atlas-add` and `skills/atlas-audit`, as a worked example of those skills. One further mod was examined but produced no records, so it is not listed.

Not affiliated with or endorsed by these mods' authors; descriptions are this project's own analysis; no mod files are included.
