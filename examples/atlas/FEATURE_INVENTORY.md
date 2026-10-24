# Feature inventory

Generated from `features/*.json` by `wbsd.py inventory` — edit the JSON, not this file. 311 features across 15 modules.

## Index by category

### campaign-ai

| feature | module | confidence |
|---|---|---|
| [Kings without a town take one; lords of fortress-less kingdoms defect or disband](#ad457landless-faction-cleanup) | ad457 | confirmed |
| [Land-border graph between centres and factions](#beland-border-graph) | be | confirmed |
| [Faction strategic AI (target choice and assailability score)](#perisnofaction-ai-dk2) | perisno | confirmed |
| [SWC faction-hero campaign AI and politics (M&B 1.011 lineage)](#swold-faction-hero-campaign-ai) | sw | strongly-inferred |
| [Faction Strength economy driving the war (and gating sieges)](#tldfaction-strength-war-progression) | tld | confirmed |

### kingdom-management

| feature | module | confidence |
|---|---|---|
| [Civil wars, usurping the throne, annexing the losing side, and defeated kingdoms reborn](#acancivil-war-usurpation-restoration) | acan | strongly-inferred |
| [Ranks, offices and honorary titles (legate, auxiliary prefect, governor, Quaestor..Censor) with triumphs](#acanranks-offices-titles) | acan | strongly-inferred |
| [Start the campaign as an existing faction's commander-in-chief](#acwplay-as-ruler-start) | acw | confirmed |
| [Large fief building system with two build queues and a management screen](#ad457center-buildings-management) | ad457 | confirmed |
| [Court offices for vassals and a title ladder for the player](#ad457court-offices-and-titles) | ad457 | confirmed |
| [National military technology tree with dated inventions](#befaction-technology-tree) | be | confirmed |
| [National manpower pool, conscription policy and population-scaled lord count](#bemanpower-conscription-dynamic-lords) | be | confirmed |
| [Twelve borderland kingdoms with ten new cultures](#cbltwelve-borderland-kingdoms) | cbl | confirmed |
| [Fief stewards with real skills that the player can train](#popfief-stewards-with-skills) | pop | confirmed |
| [Choose the culture (troop tree) of the player's own faction](#swplayer-faction-culture-switch) | sw | confirmed |
| [Marshal elections with candidates and lord votes](#vcmarshal-election) | vc | strongly-inferred |

### diplomacy-politics

| feature | module | confidence |
|---|---|---|
| [Conspiracies against the ruler (palace assassination fights) and treason or embezzlement trials](#acanconspiracy-treason-trials) | acan | strongly-inferred |
| [Influence points, Senate support and kingdom-wide edicts voted in the Senate](#acansenate-influence-edicts) | acan | confirmed |
| [Permanent two-bloc war (Union armies vs Confederate armies)](#acwalliance-blocs) | acw | confirmed |
| [Weak kingdoms become tributaries; provocations lead to reparation demands](#ad457ai-tributary-states-casus-belli) | ad457 | confirmed |
| [Independent tribes with capitals, patrols, migration, conquest and tribute](#ad457minor-tribes-and-tributaries) | ad457 | strongly-inferred |
| [Separate Essos war/peace driver](#awoiafessos-war-peace-driver) | awoiaf | confirmed |
| [Personal letters to lords (insult, duel challenge, demands, bribes) carried by a messenger party](#awoiafletters-to-lords) | awoiaf | confirmed |
| [Spy network: plant spies in towns, read reports, order sabotage](#awoiafspy-network-sabotage) | awoiaf | confirmed |
| [Static Wars: canon-locked diplomacy with scripted war declarations](#awoiafstatic-wars-scripted-diplomacy) | awoiaf | confirmed |
| [Infamy, casus belli and alliance call-to-arms diplomacy](#beinfamy-casus-belli-alliances) | be | confirmed |
| [Peace conference with victory points, territory and reparations](#bepeace-negotiations-victory-points) | be | strongly-inferred |
| [Diplomacy mod (treaties, ministers, patrols, policies, gifts)](#bidiplomacy-suite) | bi | confirmed |
| [Send gifts or bribes to another faction's ruler (RP courier quest)](#tldgift-bribe-courier-quest) | tld | confirmed |
| [Defeated kingdoms can be reborn; their landless lords roam as 'adventurers'](#vcfaction-restoration-and-adventurers) | vc | strongly-inferred |

### lord-behavior

| feature | module | confidence |
|---|---|---|
| [AI lords spend their wealth: build in fiefs, hire mercenaries, upgrade their own gear](#ad457lord-business-build-hire-upgrade) | ad457 | confirmed |
| [Named retainers riding in lords' armies](#awoiaflord-retinue-heroes) | awoiaf | confirmed |
| [AI lords build improvements in their fiefs](#biai-lords-build) | bi | confirmed |
| [Per-lord army doctrine for reinforcements](#laiglelord-army-doctrine) | laigle | confirmed |
| [Friendly lords periodically offer troops or equipment](#tldlord-friendship-gifts) | tld | strongly-inferred |
| [Lords alternate between small patrols and full Hosts, with the number of Hosts set by faction strength](#tldstrength-scaled-hosts-and-patrols) | tld | strongly-inferred |

### party-ai

| feature | module | confidence |
|---|---|---|
| [Lord army size from leadership, renown, rank and fiefs; per-faction level-bracket wages](#acwlord-army-size-and-wages) | acw | confirmed |

### economy-trade

| feature | module | confidence |
|---|---|---|
| [Faction treasuries with a weekly budget: income/spending categories, corruption, tax fraud, embezzlement trials](#acanimperial-treasury-budget) | acan | confirmed |
| [Private estates (latifundia) on the map with production buildings, slave labour and weekly rents](#acanlatifundium-estates) | acan | strongly-inferred |
| [Camp hunting: deer, boar and buffalo herds](#acwhunting) | acw | confirmed |
| [Diplomacy 4.x extras: tax inefficiency, disguises, taverngoer locations](#ad457dplmc4-tax-inefficiency-and-extras) | ad457 | confirmed |
| [Iron Bank of Braavos: central deposits, loans with deadlines and war tax](#awoiafiron-bank) | awoiaf | confirmed |
| [Odd jobs and camp activities (mines, village labour, music, gambling, fishing, smoking food)](#awoiafside-jobs-and-camp-activities) | awoiaf | strongly-inferred |
| [Regional economy: population, resources, factories and supply](#bepes-regional-economy) | be | strongly-inferred |
| [Trade routes, production and arenas for the new centres](#cblnew-centre-economy-and-arena-wiring) | cbl | confirmed |
| [Pre-1.15x Native baseline (shared with CAE and 1860s)](#laigleold-native-baseline) | laigle | confirmed |
| [National regimental depots with rank-gated uniform shops](#laigleregimental-depots) | laigle | confirmed |
| [Town bank screen and a gambling game](#perisnobank-and-gambling) | perisno | strongly-inferred |
| [Hourly budget processing, patrol wages and budget report](#perisnobudget-and-patrol-wages) | perisno | confirmed |
| [Merchant ledger (what a trade good would earn elsewhere)](#perisnotrade-ledger) | perisno | confirmed |
| [Bank account with interest, 30-day loans, weekly pay-day from cash or account](#swbank-interest-loans-payday) | sw | confirmed |
| [Per-faction Resource Points purse with faction-paid troop upkeep](#tldfaction-resource-points-upkeep) | tld | confirmed |
| [Plundering captured towns, loot choices, recovery time and slave-taking](#vctown-plunder-and-slaves) | vc | strongly-inferred |
| [Weekly trade ledger in the budget report and anti-exploit price formulas](#vcweekly-trade-ledger) | vc | confirmed |

### settlements-villages

| feature | module | confidence |
|---|---|---|
| [Conquest aftermath: keep or plunder, exterminate/enslave the population, raze the settlement, repopulate and shift its culture](#acanconquest-aftermath-culture-change) | acan | strongly-inferred |
| [Culture-specific fief buildings with culture drift (inherits ad457.center_buildings_management; acan adds culture shift and piety effects)](#acanculture-specific-fief-buildings) | acan | strongly-inferred |
| [Tavern ambience: seated musicians playing banjo/fiddle, patrons sitting and drinking](#acwtavern-musicians-ambience) | acw | confirmed |
| [Enslaving villages and 'repopulating' hostile settlements](#ad457village-enslavement-and-repopulation) | ad457 | strongly-inferred |
| [Roman public buildings in fiefs (18 improvement types, upkeep, effects)](#biroman-public-buildings) | bi | confirmed |
| [Enterable inn with fights and a hired assassin](#perisnoperisno-inn) | perisno | confirmed |
| [Fief 'heartbeat' problems (steward summons to solve local crises)](#popfief-heartbeat-problems) | pop | confirmed |
| [Expanded fief buildings with damage, auto-repair and AI lord construction](#popfief-improvements-expanded) | pop | confirmed |
| [Buildings that unlock special recruits (clone chamber, droid foundry, force temple, rancor pit)](#swrecruit-unlock-buildings) | sw | confirmed |
| [Expanded fief buildings (church/temple, mead hall, brewery, scriptorium, guild hall, slave market, blacksmith)](#vcextended-center-improvements) | vc | confirmed |
| [Player-built refuge (hideout) that grows into a fortified base](#vcplayer-refuge) | vc | confirmed |

### recruitment-troops

| feature | module | confidence |
|---|---|---|
| [Unit-based army organisation: standing legions with HQs, cohort-limited party size, unit recruitment and province manpower](#acanlegions-cohorts-army-organisation) | acan | strongly-inferred |
| [Colour-guard troops: limit per party and battle spawning](#acwcolor-guard-flagbearers) | acw | confirmed |
| [Conscription after volunteers run out](#acwconscription) | acw | confirmed |
| [Regional named-regiment recruitment ('area of recruitment')](#acwregional-regiment-recruitment) | acw | confirmed |
| [Barracks screen: pick exactly which troops to recruit](#ad457barracks-recruitment-screen) | ad457 | strongly-inferred |
| [Garrison reinforcements march in from the fief's villages](#ad457village-reinforcement-marches) | ad457 | confirmed |
| [Paid elite-troop training at great houses](#awoiafhold-elite-trainers) | awoiaf | confirmed |
| [Custom kingdom troop designer](#becustom-kingdom-troop-editor) | be | strongly-inferred |
| [Enlistment office and rank promotion service](#beenlistment-service-ranks) | be | confirmed |
| [Modified-Native campaign rules (recruitment, autocalc, lords, bandits)](#benative-campaign-rule-changes) | be | confirmed |
| [Freelancer: request reassignment to another troop line](#bifreelancer-reassignment) | bi | strongly-inferred |
| [Military academy: pay to upgrade troops in a town](#bimilitary-academy-upgrades) | bi | confirmed |
| [Buy and maintain an artillery park (player and AI lords)](#laigleartillery-park) | laigle | confirmed |
| [Regimental standard bearers and captured enemy colours](#laiglestandard-bearers-and-captured-colours) | laigle | strongly-inferred |
| [Recruit village volunteers as a chosen troop type](#laigletyped-volunteer-recruitment) | laigle | confirmed |
| [Chamberlain, constable recruiters and retainer training](#perisnoconstable-recruiters-and-training) | perisno | confirmed |
| [Re-equip a soldier from a template and see its quality score](#perisnocustom-troop-reequip) | perisno | confirmed |
| [Passive training of lord parties and garrisons (with garrison sorting)](#popgarrison-and-lord-training) | pop | confirmed |
| [Noble recruit pool for the player's kingdom](#popnoble-recruit-pool) | pop | confirmed |
| [Player-founded knighthood order with customizable, trainable troops](#popplayer-founded-order) | pop | confirmed |
| [Growing town volunteer pools, troop hand-over to towns, and stationed reserves](#tldtown-volunteers-and-reserves) | tld | strongly-inferred |
| [Recruiting requires the local lord's permission, which can be revoked](#vcrecruitment-permissions) | vc | confirmed |

### companions-heroes

| feature | module | confidence |
|---|---|---|
| [Household staff: captured prisoners made cooks and household slaves, with quality affecting feasts, budget and estates](#acanhousehold-staff) | acan | confirmed |
| [Companion bodyguards in towns, villages and castles (with armed disguise when sneaking in)](#acwcompanion-bodyguards-and-disguise) | acw | confirmed |
| [Companions follow you as bodyguards in towns](#bitown-bodyguards) | bi | confirmed |
| [Ask companions or friendly lords to find special troops](#popcompanion-unique-troop-requests) | pop | strongly-inferred |
| [Companion catch-up XP and promotion of companions to lords](#tldcompanion-catchup-and-promotion) | tld | confirmed |
| [Persistent battle injuries, healing and optional hero permadeath](#tldpersistent-injuries-permadeath) | tld | confirmed |

### character-progression

| feature | module | confidence |
|---|---|---|
| [Player health and mortality: sickness accumulates, can be treated, and can kill the character](#acanplayer-health-mortality) | acan | confirmed |
| [Three-year junior-officer contract, reenlistment bounty and senior-officer promotion thresholds](#acwenlistment-contract-career) | acw | confirmed |
| [Freelancer (enlist as a soldier) with ACW extensions](#acwfreelancer-extensions) | acw | confirmed |
| [Westerosi background character creation (nationality x job x reason x religion x trait)](#awoiafbackground-character-creation) | awoiaf | confirmed |
| [Foraging party skill reduces food consumption](#biforaging-skill) | bi | confirmed |
| [Tavern mentors: pay to train attributes](#cbltavern-mentors) | cbl | confirmed |
| [Military rank ladder, purchasable commissions and rank salary](#laiglemilitary-rank-career) | laigle | confirmed |
| [Special items grant skill bonuses while equipped, with tooltip text](#perisnoitem-equip-bonuses) | perisno | confirmed |
| [Earned character traits (Oathkeeper, Berserker, Battle-scarred, ...)](#tldplayer-traits) | tld | confirmed |
| [Player ambitions ('Set goal') with tracked metrics and rewards](#vcplayer-goals) | vc | confirmed |
| [Lasting battle wounds on the player (head/face/body), healing and permanent scars](#vcplayer-persistent-injuries) | vc | confirmed |

### prisoners

| feature | module | confidence |
|---|---|---|
| [Slave economy: prisoners and conquered populations become culture-specific slaves, sold by town slave traders, slavers and special dealers](#acanslave-economy) | acan | strongly-inferred |
| [Executing captured lords, with honour/relation fallout and royal succession](#awoiaflord-execution-succession) | awoiaf | confirmed |
| [Prisoner revolts in over-stretched AI parties](#vcprisoner-revolts) | vc | confirmed |

### bandits-outlaws

| feature | module | confidence |
|---|---|---|
| [Named partisan leaders and faction-aligned irregular bands that raid villages](#acwpartisan-bands) | acw | confirmed |
| [Bandit spawn points for the new regions](#cblregional-bandit-spawn-points) | cbl | confirmed |
| [Deserter bands splitting off from lords' armies](#poplord-party-deserters) | pop | confirmed |
| [Invader-faction strength meter driven by the player's kills](#popminor-faction-repression-meter) | pop | confirmed |
| [Level-scaled renegade knight and wandering mercenary warbands](#poprenegade-and-merc-warbands) | pop | confirmed |

### mercenaries

| feature | module | confidence |
|---|---|---|
| [Enlisting as a common soldier: career progress gated by about 30 random service events](#acanenlistment-career-events) | acan | strongly-inferred |
| [Freelancer (enlist as a soldier) - 457 AD variant](#ad457freelancer-variant) | ad457 | strongly-inferred |
| [Legion and foreign mercenary camps on the map](#bilegion-mercenary-camps) | bi | confirmed |
| [Freelancer Guild contracts and deserter bands](#perisnofreelancer-guild-contracts) | perisno | strongly-inferred |
| [Kings hire named mercenary companies that shadow their armies](#popking-hired-mercenary-companies) | pop | confirmed |

### caravans-patrols

| feature | module | confidence |
|---|---|---|
| [Knight patrols sent out from knighthood chapterhouses](#poporder-chapter-knight-patrols) | pop | confirmed |
| [Sheriff improvement spawns village militia patrols](#popsheriff-militia-patrols) | pop | confirmed |
| [Automatic faction patrols based at towns (levels 1-3)](#swfaction-town-patrols) | sw | confirmed |

### armies-campaigns

| feature | module | confidence |
|---|---|---|
| [PAS lord and marshal AI (direct campaign control)](#bepas-marshal-campaign-ai) | be | confirmed |
| [Enlist as a freelancer soldier under a lord](#perisnofreelancer-service) | perisno | confirmed |
| [War theatres with moving advance camps](#tldwar-theaters-advance-camps) | tld | confirmed |

### sieges

| feature | module | confidence |
|---|---|---|
| [Siege planning (blockade, sanitation, traitors, infiltration, ambushes, starvation, fortified siege camp): inherited Brytenwalda/VC system](#acansiege-planning-inherited) | acan | confirmed |
| [Smoke over besieged towns on the world map; caravans leave a town at most every 2 hours](#acwbesieged-map-smoke-and-caravan-spacing) | acw | confirmed |
| [Wave-by-wave auto-resolved siege assault, plus surrender when besieged](#acwsiege-assault-waves-and-surrender) | acw | confirmed |
| [Siege planning and siege-camp events (inherited from VC/Brytenwalda, extended)](#ad457vc-siege-planning-and-camp-events-inherited) | ad457 | strongly-inferred |
| [Battering-ram assaults, and using a captured lord to force a surrender](#awoiafsiege-ram-assault-and-hostage-surrender) | awoiaf | confirmed |
| [Townsfolk take up arms when a town is besieged](#bisiege-town-militia) | bi | confirmed |
| [Explosive powder barrels and destructible field cover](#oa1860explosive-and-destructible-props) | oa1860 | confirmed |
| [Siege planning: blockade, sanitation, treachery, sabotage, burning fields, starvation and siege equipment](#vcsiege-planning) | vc | confirmed |

### battle-ai-formations

| feature | module | confidence |
|---|---|---|
| [Thrust-only ('noswing') weapon swap for infantry in tight formation (spear and pike wall)](#acanthrust-only-formation-weapons) | acan | confirmed |
| [Inherited VC battle stack: battlegroup formations AI, war cries/horns/shield taunts, courage spreading, shield bash; plus a ratio-based rout rule](#acanvc-battle-stack-inherited) | acan | confirmed |
| [Player commands every allied soldier in battle](#acwcommand-all-allies) | acw | confirmed |
| [Timed AI battle plan, faction default formations and mounted-pistol auto-switch](#acwscripted-ai-battle-plan) | acw | confirmed |
| [VC battle layer: formations, local courage, war cries/berserk, ship battles (inherited)](#ad457vc-battle-naval-layer-inherited) | ad457 | confirmed |
| [AI battle plans: attack groups, leapfrog advance, counter-attack swap, defensive lines](#beai-battle-tactics-presets) | be | strongly-inferred |
| [Infantry square, prone/crouch fire and dig-in trenches](#beinfantry-square-and-field-works) | be | strongly-inferred |
| [PBOD battle orders + Motomataru formations AI](#bipbod-formations-ai) | bi | confirmed |
| [PBOD orders/camera/deployment + Motomataru formations AI (older build)](#laiglepbod-motomataru-stack) | laigle | confirmed |
| [Division-level line-battle AI (advance to range, halt and fire, charge when close)](#nwdivision-gunpowder-ai) | nw | confirmed |
| [Musket-line formations via invisible locator props (line/column/square/skirmish, wheel)](#nwlocator-line-formations) | nw | confirmed |
| [Synchronised division volley fire](#nwvolley-fire) | nw | confirmed |
| [Formation and battle-group AI for field battles](#perisnobattle-formations-and-tactics) | perisno | confirmed |
| [Starting-orders presentation before joining a battle](#perisnostarting-orders-screen) | perisno | speculative |
| [Only disciplined armies use formation AI; rabble fights as a mob](#popdisciplined-faction-ai-gate) | pop | confirmed |
| [Formations and field-tactics battle AI (Motomataru-style kit, PoP variant)](#popformations-battle-ai-kit) | pop | confirmed |
| [Ranged troops step back from melee](#swranged-backstep-ai) | sw | confirmed |
| [Formations and battle AI (PoP-lineage set plus Motomataru '_moto' set, weapon-type orders)](#tldformations-motomataru-pop-lineage) | tld | confirmed |
| [Formations v2 with on/off toggle and native-rank fallback](#vcformations-order-translation) | vc | confirmed |

### combat-mechanics

| feature | module | confidence |
|---|---|---|
| [Drivable chariots and chariot races (requires WSE2)](#acanchariots-wse2) | acan | confirmed |
| [Spawn-time equipment variety and item-quality steps, plus blacksmith item improvement](#acanspawn-equipment-variety-and-item-quality) | acan | strongly-inferred |
| [Thrown hand grenades with area damage](#acwexplosive-grenades) | acw | confirmed |
| [Recruitable field artillery batteries (player + AI lords)](#acwfield-artillery) | acw | confirmed |
| [Buck-and-ball / shotgun multi-pellet fire, distance-tiered gunshot sound, pan smoke and shell ejection](#acwmulti-projectile-firearms) | acw | confirmed |
| [Iron-sight aiming / zoom camera for long arms](#acwrifle-iron-sight-zoom) | acw | confirmed |
| [Fire arrows and burnable/destructible siege props](#awoiaffire-arrows-destructible-props) | awoiaf | confirmed |
| [Crewed field-gun and howitzer batteries (Yuri cannon system)](#befield-artillery-batteries) | be | confirmed |
| [Firearm range falloff, headshots and cover in one hit trigger](#befirearm-hit-damage-model) | be | confirmed |
| [Central per-weapon firing effects via engine hook game_missile_launch](#bemissile-launch-firing-effects) | be | strongly-inferred |
| [Shotgun / scatter-gun pellet spread](#beshotgun-pellet-spread) | be | confirmed |
| [Machine-gun teams, gas attacks, gas masks and grenades](#beww1-weapons-mg-gas-grenades) | be | strongly-inferred |
| [Per-faction troop combat modifiers (unfinished)](#bifaction-agent-modifiers) | bi | strongly-inferred |
| [Garrison combat bonuses from fief buildings](#bigarrison-building-battle-bonuses) | bi | confirmed |
| [Flintlock pistols and muskets with firing triggers](#cblflintlock-item-triggers) | cbl | strongly-inferred |
| [Crewed field artillery in campaign battles](#laiglefield-artillery) | laigle | confirmed |
| [Firearm muzzle, pan-flash, distance-sound, scatter-shot and bullet-impact effects](#laiglemusket-item-effects) | laigle | confirmed |
| [Player-crewed artillery (12pdr, howitzer, mortar, fort, naval, carronade, swivel, rocket)](#nwcrewed-artillery) | nw | confirmed |
| [Grenades, explosive shot and destructible props](#nwexplosives-destructible-props) | nw | confirmed |
| [Central muzzle flash, smoke and report on every gunshot (engine hook)](#nwmissile-launch-effects) | nw | strongly-inferred |
| [Exploding grenades, dynamite and shells](#oa1860explosive-thrown-weapons) | oa1860 | confirmed |
| [Per-gun muzzle smoke and fire effects](#oa1860firearm-muzzle-effects) | oa1860 | confirmed |
| [Hand cannon with scripted cannonball arc](#oa1860scripted-ballistic-hand-cannon) | oa1860 | confirmed |
| [Fire arrows and fire bolts explode on impact](#perisnofire-ammo-explosions) | perisno | confirmed |
| [Field healing consumable (bacta injector + capsules) and other hotkey abilities](#swfield-heal-consumable) | sw | confirmed |
| [Thrown grenades simulated by script (arc, gravity, bounce, fuse, blast)](#swscripted-grenade-ballistics) | sw | strongly-inferred |
| [Support units that resupply ammo and heal nearby allies in battle](#swsupport-unit-auras) | sw | confirmed |
| [Hotkey weapon mode switch (swap a weapon for its alternate form in place)](#swweapon-mode-toggle) | sw | confirmed |
| [Per-agent battle modifiers from terrain, night, race and faction weather auras](#tldbattle-condition-modifiers) | tld | confirmed |
| [Day/night combat proficiency shift by race](#tldday-night-proficiency-shift) | tld | strongly-inferred |
| [Armour encumbrance penalties and fall damage when a horse dies](#tldencumbrance-and-fall-damage) | tld | strongly-inferred |
| [Dehorsing, horse blunt damage, falling, AI shield bash and weapon-dependent casualties](#vccombat-extras-dehorse-bash) | vc | strongly-inferred |

### morale

| feature | module | confidence |
|---|---|---|
| [Rally-cry key (B): enemies near the player briefly flee](#acwbattle-cry-rout) | acw | confirmed |
| [Bury the dead after a victory (honor/morale trade-off)](#acwbury-the-dead) | acw | confirmed |
| [Company discipline, suppression and rout](#becompany-discipline-rout) | be | confirmed |
| [Courage, rout and rally per soldier (with retreat order and difficulty scale)](#nwmorale-rout-rally) | nw | confirmed |
| [Side-wide battle morale (coherence), routs and player rallies](#tldbattle-coherence-rout-rally) | tld | confirmed |
| [Battle immersion: war cries, horns, shield taunts, berserker rage and morale spreading from nearby events](#vcbattle-immersion-courage) | vc | confirmed |

### deployment

| feature | module | confidence |
|---|---|---|
| [Skirmisher detachment screen (unreachable)](#biskirmisher-detachment) | bi | speculative |
| [Hand-made battlefields chosen by battle size](#laiglesize-aware-battlefields) | laigle | confirmed |
| [Remembered per-division formations and placements across battles](#vcpersistent-division-formations) | vc | confirmed |

### tournaments

| feature | module | confidence |
|---|---|---|
| [Tournament invitations and noble reactions (Floris/TPE tournament layer)](#awoiaftournament-invitations-tpe) | awoiaf | confirmed |
| [Bare-knuckle boxing ladder in town arenas](#laigleboxing-ladder) | laigle | confirmed |
| [Showdowns, Shootouts and colonial army menus (renamed Native)](#oa1860renamed-native-menus) | oa1860 | confirmed |

### quests

| feature | module | confidence |
|---|---|---|
| [Tavern bounty-hunting quests](#acwbounty-hunting-quests) | acw | confirmed |
| [President's espionage chain: rescue a spy, meet a spy, incite a riot in an enemy town](#acwespionage-riot-quests) | acw | confirmed |
| [Lord quest: destroy an enemy scout camp](#acwscout-camp-quest) | acw | strongly-inferred |
| [Senator's 'lost eagle' quest](#bilost-eagle-quest) | bi | confirmed |
| [Playable story start: inn brawl, pistol duel, smugglers raid](#laiglestory-start-missions) | laigle | confirmed |
| [Scripted historical-battle campaign (briefing, camp, companion picker, cutscene camera)](#nwhistorical-campaign-framework) | nw | strongly-inferred |

### reputation-relations

| feature | module | confidence |
|---|---|---|
| [Commoner trust: a kingdom-wide peasant reputation](#awoiafcommoner-trust) | awoiaf | confirmed |
| [Triumphus after taking a city](#bitriumphus) | bi | confirmed |
| [Joinable knighthood orders with rank points, order quests and expulsion](#popknighthood-order-membership) | pop | confirmed |
| [Automatic relation gain with lords who fought beside you](#poppost-battle-lord-relation-gain) | pop | confirmed |
| [Rank and Influence per faction](#tldfaction-rank-influence) | tld | confirmed |

### law-governance

| feature | module | confidence |
|---|---|---|
| [Town decrees (curfew, entry controls, garbage collection, social housing, strict law, begging ban)](#acantown-decrees) | acan | confirmed |
| [Political simulation: classes, parties, parliament, laws, unrest and civil war](#bepps-political-simulation) | be | strongly-inferred |

### religion-culture

| feature | module | confidence |
|---|---|---|
| [Patron deity, piety and sacrifices, with divine boons and in-battle miracles](#acanpatron-gods-piety-miracles) | acan | confirmed |
| [Faiths for lords and kingdoms, player conversion, piety and battle blessings](#ad457religion-faiths-and-piety) | ad457 | confirmed |
| [Four-faith religion (Seven, Old Gods, R'hllor, Drowned God) - extends VC's religion](#awoiaffour-faiths-religion) | awoiaf | strongly-inferred |
| [Night's Watch as a neutral sworn order: take the black, send prisoners to the Wall, rangers and free-folk raiders](#awoiafnights-watch-rules) | awoiaf | confirmed |
| [Romanitas (how Roman a settlement is)](#biromanitas) | bi | confirmed |
| [Monasteries and pagan hofs as visitable map sites (donate, learn to read, convert, recruit, pillage)](#vcmonasteries-and-hofs) | vc | confirmed |
| [Christian/pagan religion of settlements, slow conversion and player faith](#vcreligion-center-conversion) | vc | confirmed |

### dynamic-world-events

| feature | module | confidence |
|---|---|---|
| [Settlement events and epidemics (inherits ad457.settlement_disasters_epidemics; acan adds harvests, winters, sanitation and wider effects)](#acansettlement-events-epidemics) | acan | confirmed |
| [Day-counted historical event calendar (incl. leader assassination)](#acwhistorical-event-calendar) | acw | confirmed |
| [Prisoner break-outs from overloaded parties and refugee columns](#acwprisoner-breakouts-and-refugees) | acw | confirmed |
| [Seasonal disasters and epidemics in settlements](#ad457settlement-disasters-epidemics) | ad457 | confirmed |
| [Town revolts that spawn rebel kingdoms, plus rebel reconciliation and riots in ownerless towns](#ad457town-rebellions-secession) | ad457 | confirmed |
| [Random travel events with moral choices](#ad457travel-random-events) | ad457 | confirmed |
| [Canon story-event timeline (Red Wedding, Battle of the Bastards, Craster's Keep, Ned's death, Varys/Daenerys invasion...)](#awoiafcanon-story-event-timeline) | awoiaf | confirmed |
| [Random travel events (renown-gated choice events + weekly minor incidents)](#awoiafrandom-travel-events) | awoiaf | confirmed |
| [White Walker invasion waves and the War for the Dawn](#awoiafwhite-walker-invasion) | awoiaf | confirmed |
| [Dark Knights invasion: 100/250/500-day options](#cblinvasion-date-options) | cbl | confirmed |
| [Persistent seasonal weather and rain greatcoats](#laigleweather-seasons) | laigle | confirmed |
| [Random battle weather and time of day](#nwbattle-weather-generator) | nw | strongly-inferred |
| [Scheduled rebel armies and unemployed-mercenary warbands](#perisnorebels-and-mercenary-bands) | perisno | confirmed |
| [Procedurally generated minor knighthood orders that settle in AI fiefs](#popai-minor-order-generation) | pop | confirmed |
| [Refugees and looters spawned by raids and conquests](#popraid-refugees) | pop | strongly-inferred |
| [Named 'signature' warlords with patrols, repeatable until defeated and dealt with](#popunique-signature-heroes) | pop | confirmed |
| [Configurable random ambushes and assassins on landing in towns](#swrandom-town-ambushes) | sw | confirmed |
| [Faction defeat, territory redistribution, lord defection and last stand](#tldfaction-defeat-redistribution-last-stand) | tld | confirmed |
| [Random camp/siege events and lord's-court judgment cases](#vcrandom-events-and-judgments) | vc | confirmed |

### map-travel

| feature | module | confidence |
|---|---|---|
| [Paid fast travel by ship, train or stagecoach between linked towns](#acwfast-travel-network) | acw | confirmed |
| [Lord parties use their faction's own map icon](#biculture-lord-map-icons) | bi | confirmed |
| [Enlarged Calradia map (Native kept, borderlands added)](#cblexpanded-calradia-map) | cbl | confirmed |
| [Map icons by party type, ship icon on sea lanes](#cblmap-icons-by-party-type-and-ships) | cbl | confirmed |
| [Calradia Borderlands V3.52: what the later version adds](#cblv352-later-version-changes) | cbl | confirmed |
| [Terrain-dependent party speed on the map](#laigleterrain-party-speed) | laigle | strongly-inferred |
| [Buy a ship in port towns](#oa1860purchasable-ship) | oa1860 | confirmed |
| [Owned starship with buyable component upgrades that grant party bonuses](#swstarship-upgrades) | sw | confirmed |
| [Named map regions: entry messages, region-picked battle scenes and landmarks](#tldregion-tracking-and-battle-scenes) | tld | confirmed |
| [Hide from enemies and wilderness animal ambushes](#tldwilderness-encounters-hide-animal-ambush) | tld | confirmed |
| [Paid passage between ports](#vcport-passage-travel) | vc | strongly-inferred |

### naval

| feature | module | confidence |
|---|---|---|
| [Ports, landings and ferries as map parties, sea trade routes, embarking armies and an overseas merchant fleet](#acanports-ferries-sea-trade) | acan | strongly-inferred |
| [Sea encounters fought as boarding actions](#laiglenaval-boarding-battle) | laigle | confirmed |
| [Ship-to-ship deck battles with boarding](#vcdeck-sea-battles) | vc | confirmed |
| [AI sea traffic: traders, fishers, slavers, travellers and sea kings sailing between ports](#vcsea-ai-traffic) | vc | strongly-inferred |
| [Sailing on the campaign map (land/sea switching, wind-and-navigation speed)](#vcsea-travel-map) | vc | confirmed |
| [Owning a fleet: ship types, crew capacity, hull damage, buying/building/capturing ships](#vcship-fleet-ownership) | vc | confirmed |

### qol-ui

| feature | module | confidence |
|---|---|---|
| [Troop detail screen and per-culture upgrade-tree presentations](#acantroop-detail-and-upgrade-trees) | acan | confirmed |
| [Lord map icons that grow into an 'army' icon above 150 men](#acwarmy-size-map-icons) | acw | confirmed |
| [Custom battles: 35 historical battlefields, 38 playable generals, per-battle time of day and fog](#acwcustom-battle-historical-scenarios) | acw | confirmed |
| [Death camera with automatic hold orders when the player falls (MadVader deathcam)](#acwdeath-camera) | acw | confirmed |
| [Spoken / bugled order and group-selection callouts (with engine-native volley/rank orders)](#acworder-voice-callouts) | acw | confirmed |
| [Walk around your own camp (and the enlisted army's camp)](#acwwalkable-party-camp) | acw | confirmed |
| [Start the game as ruler or vassal of an existing kingdom](#ad457royal-and-lord-sandbox-start) | ad457 | strongly-inferred |
| [New-game setup choices (naming canon, static vs sandbox wars, commoner trust, wounds, start continent, White Walker date)](#awoiafcampaign-setup-options) | awoiaf | confirmed |
| [Main-menu web link buttons (Steam/Epic/YouTube/Twitter/Discord)](#awoiafmain-menu-web-links) | awoiaf | confirmed |
| [Party/loot exchange screen hotkeys (take all, drop all prisoners, move stacks)](#awoiafparty-screen-hotkeys) | awoiaf | strongly-inferred |
| [Aerial command camera with mouse-placed company positions (PBS)](#beaerial-command-view) | be | strongly-inferred |
| [Firearm descriptions in item tooltips](#befirearm-item-info-text) | be | strongly-inferred |
| [First-person iron-sight camera when aiming firearms](#beironsight-aiming) | be | strongly-inferred |
| [Battle announcements: first blood, fallen heroes, kill milestones](#bibattle-event-messages) | bi | confirmed |
| [Faro gambling minigame](#laiglefaro-card-game) | laigle | strongly-inferred |
| [Keep weapons and horse picked up in battle](#laiglekeep-battlefield-pickups) | laigle | confirmed |
| [Custom battle designer by division](#nwcustom-battle-division-designer) | nw | strongly-inferred |
| [F-key order tree with 'hold where I look' arrow](#nwfkey-order-tree) | nw | confirmed |
| [On-screen objective markers and mission timer/progress counter](#nwobjective-markers-hud) | nw | confirmed |
| [Shouted voice commands and order call-outs](#nwvoice-commands) | nw | confirmed |
| [Camp-menu cheat-mode toggle (broken)](#oa1860cheat-mode-camp-toggle) | oa1860 | strongly-inferred |
| [Party-exchange screen extensions (hover hotkeys on the troop screens)](#perisnoexchange-screen-extensions) | perisno | strongly-inferred |
| [Walk among and drill your army from the camp menu](#popcamp-troop-review-drill) | pop | strongly-inferred |
| [Party/garrison exchange-screen hotkeys (take all, move stacks)](#popparty-screen-hotkeys) | pop | strongly-inferred |
| [Upgrade-all with preview of who can be promoted](#swmass-upgrade-preview) | sw | confirmed |
| [In-game key assignment for mod abilities](#swrebindable-ability-keys) | sw | confirmed |
| [Scope zoom overlay and first-person helmet visor](#swscope-and-visor-overlays) | sw | confirmed |
| [Camp menu: walk the camp, review troops in a scene, timed consumables, dynamic party icon](#tldcamp-menu-actions) | tld | strongly-inferred |
| [Party-exchange screen hotkeys (take/give all, reorder stacks)](#tldexchange-screen-hotkeys) | tld | confirmed |
| [In-game strategy, difficulty and AI tweak options](#tldin-game-strategy-options) | tld | strongly-inferred |
| [Gamepad (Xbox d-pad) battle command menus](#vcgamepad-order-menus) | vc | confirmed |
| [Civilian second outfit worn automatically in towns and halls](#vcsecond-outfit) | vc | strongly-inferred |

### reports-info

| feature | module | confidence |
|---|---|---|
| [In-game faction troop-tree viewer](#befaction-troop-tree-viewer) | be | strongly-inferred |
| [Reports: zoomable political world map screen](#biworld-map-presentation) | bi | confirmed |
| [Post-battle results screen with kill-based pay and casualty tally](#nwbattle-results-payout) | nw | confirmed |
| [Per-fief base income with income and construction reports](#popfief-base-income-and-reports) | pop | confirmed |
| [Procedural rumours and gossip with per-NPC cooldowns](#poprumor-system) | pop | strongly-inferred |
| [Camp, character, faction and troop-tree report screens](#vccamp-and-report-screens) | vc | strongly-inferred |

### automation

| feature | module | confidence |
|---|---|---|
| [Permanent field camps commanded by a companion, which store troops and loot, ransom your prisoners and attract bandits](#acanplayer-permanent-camps) | acan | strongly-inferred |
| [Companions auto-upgrade their gear from the loot pool](#perisnoautoloot-equipment-upgrade) | perisno | confirmed |

### performance-bugfix

| feature | module | confidence |
|---|---|---|
| [WSE break_loop (opcode 8) in the imprisoned-companion traveller dialog](#acwwse-break-loop-opcode8) | acw | confirmed |
| [Targeted per-kingdom AI recalculation instead of world-wide rethinks](#ad457per-faction-ai-recalculation) | ad457 | confirmed |
| [Round-robin ('async') campaign processing instead of hourly bulk loops](#beasync-round-robin-campaign-ai) | be | confirmed |
| [Battle morale recalculation spread over three ticks (performance)](#bicourage-update-staggering) | bi | confirmed |
| [On-load savegame repair and content-update migration](#vcsavegame-content-update) | vc | confirmed |

### other

| feature | module | confidence |
|---|---|---|
| [Inherited 457 AD base: lord business AI, sandbox ruler/vassal start, character creation (with acan's changes)](#acanad457-base-inherited) | acan | confirmed |
| [Month-based scene light, regional fog and snow in battle and town scenes](#acanseasonal-light-fog-weather) | acan | strongly-inferred |
| [Skin-tone-matched bare arms and legs on clothing items (uses WSE op 2749)](#acanskin-matched-clothing-wse) | acan | confirmed |
| [Wild animal herds on the map and hunting battles](#awoiafhunting-herds) | awoiaf | strongly-inferred |
| [Regional weather report and battle sky, rain, fog and ambience](#becampaign-weather-battle-atmosphere) | be | strongly-inferred |
| [Campaign balance retune (party size, food, morale, rewards)](#cblcampaign-balance-retune) | cbl | confirmed |
| [93 hand-made field battle scenes by terrain](#cblcustom-field-battle-scenes) | cbl | confirmed |
| [Multiplayer-only systems (catalogue)](#nwmp-only-systems) | nw | confirmed |
| [Older-Native base shared with L'Aigle and CAE](#oa1860cae-native-baseline) | oa1860 | confirmed |
| [Script-level array library on hidden temp parties](#perisnoarray-library) | perisno | confirmed |
| [Start-of-game hard mode and fog of war toggles](#perisnohard-mode-and-fog-of-war) | perisno | confirmed |
| [Hunting animal herds on the map](#perisnohunting-missions) | perisno | strongly-inferred |
| [Faction battle-start speech and shouts](#swbattle-start-speeches) | sw | confirmed |
| [Cantina blackjack and tavern brawls](#swcantina-blackjack-and-brawls) | sw | confirmed |
| [Space dogfight minigame (training ground only)](#swspace-battle-minigame) | sw | strongly-inferred |
| [Seasons that change scene lighting/shaders and map time](#vcseasons-scene-lighting) | vc | strongly-inferred |

## Details

<a id="ad457landless-faction-cleanup"></a>
### Kings without a town take one; lords of fortress-less kingdoms defect or disband — ad457 (`ad457.landless_faction_cleanup`)

**What it does:** Every frame one kingdom is checked. If its king owns no town but the kingdom has a town with no lord, the king is given it. If the kingdom has lost every town and castle, its lords look for a new kingdom and defect (announced in the log); those who cannot leave have their war parties disbanded when idle, and the rest lose 50 relation with their king.

**How it works:** strig:41 (interval 0, round-robin $checked_faction over fac_player_supporters_faction..fac_manhunters) calls check_king_has_town, check_lords_but_no_centers, recalculate_ais_for_faction. check_king_has_town: if an active non-player kingdom's leader (faction slot 11) owns no town (loop p_town_1..p_castle_1 on party 7), find one of the kingdom's towns with party 7 == -1 and give_center_to_lord(center, king); castles are not considered. check_lords_but_no_centers: if the kingdom holds no towns/castles (villages ignored), for each lord: lord_find_alternative_faction -> change_troop_faction with log '{s1} has joined the {s2}'; else if his party (troop 10) is idle and not in battle and not the player's enlisted party -> remove_party, troop 10 = -1, '{s1} has disbanded.'; else -50 relation with the king.

- **Hooks:** `strig:41`
- **Scripts:** `check_king_has_town`, `check_lords_but_no_centers`, `recalculate_ais_for_faction`, `lord_find_alternative_faction`, `change_troop_faction`, `give_center_to_lord`, `remove_hero_prisoners`, `troop_change_relation_with_troop`
- **Slots:** `faction:11`, `faction:21`, `faction:64`, `party:7`, `troop:2`, `troop:10`
- **Globals:** `checked_faction`, `players_kingdom`, `enlisted_party`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis ad457 strig:41: round-robin $checked_faction, three calls`, `dis ad457 check_king_has_town: give_center_to_lord to a landless king`, `dis ad457 check_lords_but_no_centers: defection log '{s1} has joined the', disband '{s1} has disbanded.', -50 relation`
- **Overlaps:** `acan.civil_war_usurpation_restoration`, `ad457.town_rebellions_secession`, `tld.faction_defeat_redistribution_last_stand`, `vc.faction_restoration_and_adventurers`

<a id="beland-border-graph"></a>
### Land-border graph between centres and factions — be (`be.land_border_graph`)

**What it does:** At game start every town/castle records its three nearest neighbouring centres (with hand-fixed exceptions across water) and whether it is coastal; the game then knows which nations actually share a land border. Provocations, war declarations, notifications and AI targets use it so nations only fight neighbours, and overseas nations need sea access.

**How it works:** walled_centers_assign_closest_centers (173 stmts, from game_start): for each centre p_town_1..p_village_1 store the three closest other centres in party slots 140/141/142 (excluding already chosen), manual overrides for strait pairs (p_castle_44<->p_town_20, ...), party slot 143 = 1 for listed coastal towns. cf_if_center_borders_a_faction_by_land(center, faction): true if any centre of that faction lists this one or is listed by it. cf_if_faction_borders_a_faction_by_land, cf_if_center_borders_any_enemy_faction_by_land, cf_if_center_borders_any_faction_by_land, cf_if_faction_has_access_to_sea (slot 143). Used by create_random_provocation, diplomacy_start_war_between_kingdoms (war notification only for neighbours), pas_get_random_border_center_for_faction, PES trade.

- **Hooks:** `script:game_start (walled_centers_assign_closest_centers)`
- **Scripts:** `walled_centers_assign_closest_centers`, `cf_if_center_borders_a_faction_by_land`, `cf_if_faction_borders_a_faction_by_land`, `cf_if_center_borders_any_enemy_faction_by_land`, `cf_if_center_borders_any_faction_by_land`, `cf_if_center_borders_a_faction`, `cf_if_faction_borders_a_faction`, `cf_if_faction_has_access_to_sea`, `pas_get_random_border_center_for_faction`, `pas_get_random_war_border_center_for_faction`
- **Slots:** `party:140`, `party:141`, `party:142`, `party:143`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis be walled_centers_assign_closest_centers`, `dis be cf_if_center_borders_a_faction_by_land`, `callers: create_random_provocation, diplomacy_start_war_between_kingdoms, pas_* use it`

<a id="perisnofaction-ai-dk2"></a>
### Faction strategic AI (target choice and assailability score) — perisno (`perisno.faction_ai_dk2`)

**What it does:** Each kingdom periodically rethinks its strategy: which enemy centres to attack, who to grant fiefs, how to answer political issues, using a numeric assailability score per centre.

**How it works:** strig:33 (every 3h) calls recalculate_ais, which runs decide_faction_ai_dk2 (527 stmts, 89-block closure) per faction; the force-rethink menu option does the same. It calls npc_decision_checklist_* helpers and calculate_center_assailability_score_dk2 (323 stmts) which weighs prosperity, strength and distance and prints 'attack of {s8} is {reg0}' debug text. It also raises notifications (war declared, feast, marshal relief) and touches qst_organize_feast, qst_wed_betrothed.

- **Hooks:** `strig:33`, `menu:faction_orders/opt:faction_orders_rethink_all:conseq`
- **Scripts:** `recalculate_ais`, `decide_faction_ai_dk2`, `calculate_center_assailability_score_dk2`, `npc_decision_checklist_evaluate_enemy_center_for_attack_dk2`, `find_total_prosperity_score`, `npc_decision_checklist_troop_follow_or_not`
- **Slots:** `faction:4`, `faction:5`, `faction:8`, `faction:11`, `faction:21`
- **Globals:** `g_do_not_skip_other_than_current_ai_object`
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `explain perisno decide_faction_ai_dk2: caller recalculate_ais; entry strig:33 (every 3h) and menu faction_orders_rethink_all; NEW script`, `explain perisno calculate_center_assailability_score_dk2: caller npc_decision_checklist_evaluate_enemy_center_for_attack_dk2; debug text 'attack of {s8} is {reg0}'`, `hooks perisno strig:33 calls recalculate_ais`, `slots faction[4], [5], [8], [11], [21] read in closure`

<a id="swold-faction-hero-campaign-ai"></a>
### SWC faction-hero campaign AI and politics (M&B 1.011 lineage) — sw (`sw.old_faction_hero_campaign_ai`)

**What it does:** SW's campaign runs on the older Mount&Blade 1.011-style faction model: faction heroes decide whether to follow the marshal or act alone, factions start war and peace on timers, captured centers are handed out by assign_lords_to_empty_centers, and the player's faction army is managed by an 'automated attack system'.

**How it works:** strig:24 (7 h) -> decide_faction_party_ais -> calculate_troop_ai -> faction_hero_decide_next_ai_state (470 stmts) / _follow_or_not (250); strig:39 randomly_start_war_peace; strig:54 assign_lords_to_empty_centers; strig:93 process_automated_attack_system; party_decide_next_ai_state_under_command for heroes following the player; diplomacy_start_war/peace_between_factions.

- **Hooks:** `strig:24`, `strig:39`, `strig:54`, `strig:93`
- **Scripts:** `decide_faction_party_ais`, `faction_hero_decide_next_ai_state`, `faction_hero_decide_next_ai_state_follow_or_not`, `randomly_start_war_peace`, `diplomacy_start_war_between_factions`, `diplomacy_start_peace_between_factions`, `process_automated_attack_system`, `party_decide_next_ai_state_under_command`, `calculate_troop_ai_under_command`
- **Slots:** `party:4-63, 123, 800`
- **Relation to Native:** replaces-native
- **Confidence:** strongly-inferred
- **Evidence:** `explain sw faction_hero_decide_next_ai_state: caller calculate_troop_ai, entry strig/menu/dialog`, `sw hooks: strig:24, strig:39, strig:54, strig:93`

<a id="tldfaction-strength-war-progression"></a>
### Faction Strength economy driving the war (and gating sieges) — tld (`tld.faction_strength_war_progression`)

**What it does:** Each faction has a single Strength number that rises daily from its towns and falls whenever one of its parties is destroyed; the winner (or the player's allied theatre factions, if the player won) gains what the loser lost. Strength is announced in words ('The forces of Rohan are now ...'), and a faction's towns can only be besieged once its Strength drops below a threshold that relaxes as the player levels up.

**How it works:** Faction slot 153 = live strength (capped 8000), slot 150 = displayed strength synced every 5 h by strig:56 with a colour-coded message when the thousands-band changes (faction_strength_string_to_s23 maps /1000 to 'crushed'..'unrivalled' strings). Slot 148/149 = cumulative gains/losses. strig:20 (daily) adds each center's party slot 256 income (halved under options, before the war, or when the faction is below $tld_option_regen_limit; ally multiplier $tld_ally_str_income_multi) and raises $g_fac_str_siegable = 3000 + (player level - war level) * relax-rate ('The war expands'). clear_party_group (called when a party is wiped) subtracts the party's value (party slot 1, scaled by $tld_victory_str_multi if the player won) from its faction and adds it to the victor, or splits it among player-allied factions in the player's theatre. decide_faction_ai, kingdom_hero_decide_next_ai_state, the marshal dialog and the player's own 'Attack the town' menu option all compare enemy strength against $g_fac_str_siegable (capital needs siegable-2000).

- **Hooks:** `strig:20`, `strig:56`, `script:clear_party_group`, `menu:town/opt:player_initiate_siege:cond`, `menu:castle_outside/opt:player_castle_initiate_siege:cond`, `menu:faction_strengths_report`
- **Scripts:** `faction_recalculate_strength`, `faction_strength_string_to_s23`, `clear_party_group`, `decide_faction_ai`, `kingdom_hero_decide_next_ai_state`, `store_average_center_value_per_faction`
- **Menus:** `menu:faction_strengths_report`, `menu:camp_strat_tweaks`
- **Dialogs:** `dlg:565:dlga_marshall_suggest:marshall_answer:cond`, `dlg:627:dlga_lord_talk_ask_about_war_details:lord_talk_ask_about_war_2:conseq`
- **Slots:** `faction:148`, `faction:149`, `faction:150`, `faction:153`, `party:1`, `party:256`, `party:260`
- **Globals:** `g_fac_str_siegable`, `tld_war_began`, `tld_option_regen_rate`, `tld_option_regen_limit`, `tld_option_siege_relax_rate`, `tld_victory_str_multi`, `tld_ally_str_income_multi`, `tld_player_level_to_begin_war`, `player_won_last_battle`
- **Module-specific resources:** string: str_faction_strength_crushed .. str_faction_strength_last
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `dis tld strig:20 (center income loop, $g_fac_str_siegable update)`, `dis tld strig:56 (150<-153 sync, messages)`, `dis tld clear_party_group (153 -= party slot 1; winner/theatre allies +)`, `global tld g_fac_str_siegable: readers decide_faction_ai, marshall dialog, town/castle siege conds`, `slot tld faction 153: 123 accesses / 37 blocks incl. quest reward dialogs`
- **Overlaps:** `be.pas_marshal_campaign_ai`, `tld.war_theaters_advance_camps`, `vc.marshal_election`

<a id="acancivil-war-usurpation-restoration"></a>
### Civil wars, usurping the throne, annexing the losing side, and defeated kingdoms reborn — acan (`acan.civil_war_usurpation_restoration`)

**What it does:** A realm can split into civil war, after which the winner annexes the losers' lords and fiefs. A strong player or lord can usurp the throne, which reshuffles factions, ranks, titles, fiefs and marriages. Every two days the game checks whether a destroyed kingdom can be restored with a new lord.

**How it works:** activate_main_story_civil_war / start_year_of_four set $g_civil_war and split factions (story-driven in acan). usurp_faction (177 stmts) moves lords between factions (change_troop_faction), adjusts relations, kills or divorces where needed (kill_lord_lady, troop_divorce_troop), re-ranks (troop_set_rank), regrants fiefs (give_center_to_lord2), resets titles, banners and party sizes, and assigns honorary titles. cf_annex_faction (from dlg:6222 end_civil_war_captured_enemies or menu notification_civil_war_faction_defeated) folds the defeated side's lords and centres into the victor and changes right to rule. strig:87 (every 48 h) checks for defeated factions and calls reactivate_kingdom, which can spawn a new lord (give_birth_to_lord), return exiles (dplmc_lord_return_from_exile) and hand back a centre, then sends menu_notification_kingdom_restored / _liberated. become_emperor finalises a usurpation for the player.

- **Hooks:** `strig:87`, `menu:goy_purge/opt:Continue.:conseq`, `menu:meeting_with_centurio_3`, `menu:notification_civil_war_faction_defeated/opt:continue:conseq`, `dlg:6222:dlga_end_civil_war_captured_enemies`, `prsnt:select_kingdom/t1`
- **Scripts:** `usurp_faction`, `cf_annex_faction`, `reactivate_kingdom`, `give_birth_to_lord`, `become_emperor`, `activate_main_story_civil_war`, `end_civil_war`, `kill_lord_lady`, `troop_divorce_troop`, `give_center_to_lord2`, `change_faction_banner`
- **Menus:** `menu_notification_kingdom_restored`, `menu_notification_kingdom_liberated`, `menu_end_civil_war`, `menu_notification_civil_war_faction_defeated`, `menu_goy_purge`
- **Slots:** `faction:10`, `faction:12`, `faction:223`, `troop:178`, `troop:183`
- **Globals:** `g_civil_war`, `g_is_emperor`, `g_unrest`, `g_has_senat_sup`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `explain acan usurp_faction: 13 callees incl. change_troop_faction/kill_lord_lady/troop_set_rank/give_center_to_lord2/ai_assign_title`, `explain acan cf_annex_faction: callers end_civil_war dialog + civil-war-defeated menu`, `explain acan strig:87 (every 48h): calls reactivate_kingdom, menus notification_kingdom_restored/_liberated`
- **Overlaps:** `ad457.landless_faction_cleanup`, `ad457.town_rebellions_secession`, `tld.faction_defeat_redistribution_last_stand`, `vc.faction_restoration_and_adventurers`

<a id="acanranks-offices-titles"></a>
### Ranks, offices and honorary titles (legate, auxiliary prefect, governor, Quaestor..Censor) with triumphs — acan (`acan.ranks_offices_titles`)

**What it does:** Lords and the player hold formal offices: command of a standing legion, command of an auxiliary unit, a provincial governorship, and honorary titles (Quaestor, Aedile, Consul, Censor) handed out by the ruler. Office decides party size, banner and title. Losing a trial, resigning or angering the ruler strips it. Victories earn triumph points and a public triumph.

**How it works:** troop_set_rank (103 callers) writes the rank slot: troop slot 178 = legion commanded (also mirrored in trp_province_array slot 215+n), slot 179 = auxiliary unit template commanded (mirrored at 250+n). It then updates $g_rank for the player, re-forms the lord's party (party_update_cohorts), and resets the title, the banner and every owned fief's banner icon. remove_office_from_troop (trial verdicts, resignation, leaving the faction) clears offices and calls find_new_commander_for_legion / _for_aux / faction_dismisses_marshall. Honorary titles are handed out by ai_assign_title (relation/renown driven; give_honorary_titles at game start; menu_honorary_title_granted) and can be usurped (usurp_honor_title_with_help) or lost when the holder angers others (destroy_center text). Provinces are imperial or senatorial (prsnt:make_province_imperial / make_province_senatorial, governor_selection, governor_change). get_province_relation_modifier rates provinces as unruly or easy to rule. troop_change_triumph_points accumulates triumph points, and troop_holds_triumph / triumph_marsh_start stage the triumph mission (mst_triumph). change_lord_party_to_fit_rank sizes the party to the office.

- **Hooks:** `strig:192`, `strig:69`, `menu:notification_player_faction_province_appointed`, `menu:notification_player_senatorial_province_appointed`, `menu:honorary_title_granted`, `prsnt:governor_change/t0`, `prsnt:governor_selection/t0`, `prsnt:make_province_imperial/t0`, `dlg:5622:dlga_trial_guilty`, `dlg:4817:dlga_imperial_give_up_province_resign`, `menu:triumph`
- **Scripts:** `troop_set_rank`, `remove_office_from_troop`, `ai_assign_title`, `give_honorary_titles`, `usurp_honor_title_with_help`, `find_new_commander_for_legion`, `find_new_commander_for_aux`, `change_lord_party_to_fit_rank`, `get_province_relation_modifier`, `troop_change_triumph_points`, `troop_holds_triumph`, `triumph_marsh_start`, `assign_center_to_lord`, `get_current_rank_to_s21`, `get_player_rank_string_s43`
- **Menus:** `menu_honorary_title_granted`, `menu_triumph`, `menu_triumph_awared_ai`, `menu_trial_guilty`
- **Presentations:** `prsnt_governor_change`, `prsnt_governor_selection`, `prsnt_make_province_imperial`, `prsnt_make_province_senatorial`, `prsnt_province_notifiction_player`, `prsnt_legion_selection`, `prsnt_aux_selection`
- **Mission templates:** `mst_triumph`
- **Slots:** `troop:178`, `troop:179`, `troop:183`, `troop:189`, `troop:52`, `troop:10`, `troop:13`
- **Globals:** `g_rank`, `g_is_emperor`, `g_civil_war`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `dis acan troop_set_rank: slot 178 -> province_array 215+n, slot 179 -> 250+(pt - pt_cohors_aux), $g_rank, party_update_cohorts, banner reset loop over fiefs`, `explain acan ai_assign_title / give_honorary_titles: menu_honorary_title_granted; weekly_imperial_balance text 'awarded the title of Censor/Consul/Aedile/Quaestor'`, `explain acan remove_office_from_troop: callers trial_guilty, resign, caught_embezzle_punished`, `explain acan get_province_relation_modifier: 14 presentation callers, 'considered to be unruly / easy to rule'`
- **Overlaps:** `acan.enlistment_career_events`, `acw.enlistment_contract_career`, `acw.freelancer_extensions`, `ad457.court_offices_and_titles`, `ad457.freelancer_variant`, `be.enlistment_service_ranks`, `bi.freelancer_reassignment`, `laigle.military_rank_career`, `pop.knighthood_order_membership`, `tld.faction_rank_influence`

<a id="acwplay-as-ruler-start"></a>
### Start the campaign as an existing faction's commander-in-chief — acw (`acw.play_as_ruler_start`)

**What it does:** A new-game option lets the player take over one of the seven factions: the player assumes the leader's name, face, banner and fiefs, all that faction's lords transfer to the player's realm, and the original leader is removed from play.

**How it works:** menu:start_phase -> menu:king_start (7 options) -> script player_is_king(faction): sets $king_start/$king_faction, banner from faction slot 15, activate_player_faction, copies the leader's type/face keys/name to trp_player, give_center_to_lord for every center owned by the leader (court = first town, player relocated there), temporary minister, removes the leader's party and sets him outlaw/inactive, copies faction slots 0-399 into fac_player_supporters_faction, transfers every lord of that faction with change_troop_faction, then adds starting XP/gear (200 stmts). Many systems later check $king_start (bloc alliance membership, cannons' crew faction, rally cry, order voices).

- **Hooks:** `menu:king_start/opt:kingdom_1:conseq`, `menu:king_start/opt:kingdom_7:conseq`
- **Scripts:** `player_is_king`, `activate_player_faction`, `give_center_to_lord`, `change_troop_faction`
- **Menus:** `menu_king_start`, `menu_adventurer_start`
- **Slots:** `faction:15`, `faction:11`, `faction:8`, `faction:21`, `troop:10`
- **Globals:** `king_start`, `king_faction`, `g_player_court`, `g_starting_town`, `g_player_minister`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis acw player_is_king (200 stmts)`, `roots acw player_is_king -> 7 king_start options`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_game_menus.py 20222 king_start; module_scripts.py 53853 player_is_king`
- **Overlaps:** `ad457.royal_and_lord_sandbox_start`, `awoiaf.campaign_setup_options`, `cbl.invasion_date_options`, `laigle.story_start_missions`, `tld.in_game_strategy_options`

<a id="ad457center-buildings-management"></a>
### Large fief building system with two build queues and a management screen — ad457 (`ad457.center_buildings_management`)

**What it does:** Every town, castle and village can hold about 33 building types (mills, mines, quarries, fisheries, guard posts, watchtowers, messenger posts, prison tower, training ground, slave market, sewers, baths, a temple of the holder's faith, and very expensive prestige monuments up to 300,000 silver). Names and descriptions change with the settlement's culture. Two buildings can be under construction at once; finished buildings give prosperity, renown, relation and troop experience over time. The holder manages it all from a graphical management screen that also offers garrison exchange and a brutal 'repopulate' option.

**How it works:** Building ids are party slots 128-160 (value >=1 = built). get_improvement_details (1009 stmts, Native 32) maps id -> culture-specific name/description in s0/s1 and cost in reg0 (e.g. 141 guard posts 15000, 133 iron mine 80000, 156 150000, 160 300000; 142 = temple whose name follows the holder's religion, 8000). improve_center(center, builder, days) puts $g_improvement_type into the first free queue (slot 162 with finish-hour 163, else 164/165) and records the builder in 272/273; gives the builder +3 renown or the player 200 xp. strig:74 (every ~1.6 min game time) walks one centre per tick ($g_set_center_upgrades) and calls cf_check_building_finished for both queues: when the finish hour passes it sets the building slot, messages the holder and applies one-off effects (prosperity, honour, piety, relation, walker types). strig:141 (every 2.1h, random town/castle) applies recurring effects: 157/158/160 add prosperity and +5 owner renown and +1/+2 player relation, 149 (training ground) upgrades the garrison with 30-50k xp, 159 adds renown. The UI is prsnt_center_management started by mst:center_management (t0 every frame), reached from menu:center_manage_2 (town 'Manage this town/fortress', village 'Manage this village'); its event handler (prsnt:center_management/t2) sets $g_improvement_type and links to menu_garrison_management (swap troops with the garrison) and menu_repopulate (needs >=200 men and negative relation). Fire disasters (see ad457.settlement_disasters_epidemics) can destroy buildings.

- **Hooks:** `strig:74`, `strig:141`, `mst:center_management/t0:conseq`, `prsnt:center_management/t2`, `prsnt:center_management/t4`, `menu:town/opt:walled_center_manage:conseq`, `menu:village/opt:village_manage:conseq`
- **Scripts:** `get_improvement_details`, `improve_center`, `cf_check_building_finished`, `get_improvement_picture`, `center_get_capital`, `change_center_prosperity`
- **Menus:** `menu_center_manage_2`, `menu_garrison_management`, `menu_repopulate`, `menu_repopulate_complete`
- **Presentations:** `prsnt_center_management`
- **Mission templates:** `mst_center_management`
- **Slots:** `party:128-160 (building flags)`, `party:161`, `party:162`, `party:163`, `party:164`, `party:165`, `party:272`, `party:273`, `party:327`
- **Globals:** `g_improvement_type`, `g_set_center_upgrades`, `piety`
- **Module-specific resources:** string: *_name_rome / *_description_rome culture variants (e.g. str_guard_posts_name_rome, str_silvermine_name_rome); mesh: building pictures chosen by get_improvement_picture (625 stmts); scene: mst_center_management scene
- **Relation to Native:** replaces-native
- **Confidence:** confirmed
- **Evidence:** `dis ad457 improve_center: queue slots 162/163 and 164/165, builder 272/273, finish hour = now + days*24`, `dis ad457 strig:74: rotating centre index $g_set_center_upgrades, calls cf_check_building_finished(162,163) and (164,165)`, `dis ad457 strig:141: building slots 149/157/158/159/160 -> prosperity, renown, relation, party_upgrade_with_xp 30000-50000`, `dis ad457 get_improvement_details: 33 ids 128-160 with costs 10000-300000; 142 = religion-specific temple (Chalcedonian/Arian/Miaphysite/Nestorian/Donatist basilica, pagan shrine, Zoroastrian temple, synagogue)`, `refs ad457 prsnt prsnt_center_management: mst:center_management/t0 + its own event handlers; refs menu_garrison_management / menu_repopulate only from prsnt:center_management/t2`, `explain prsnt:center_management/t2 text: 'You need to be either the governor of the town or increase faction cen...', 'You need at least 200 men and a negative relation with the settlement'`
- **Overlaps:** `acan.culture_specific_fief_buildings`, `acan.latifundium_estates`, `ad457.lord_business_build_hire_upgrade`, `bi.ai_lords_build`, `bi.garrison_building_battle_bonuses`, `bi.roman_public_buildings`, `pop.fief_base_income_and_reports`, `pop.fief_heartbeat_problems`, `pop.fief_improvements_expanded`, `pop.fief_stewards_with_skills`, `sw.recruit_unlock_buildings`, `vc.extended_center_improvements`

<a id="ad457court-offices-and-titles"></a>
### Court offices for vassals and a title ladder for the player — ad457 (`ad457.court_offices_and_titles`)

**What it does:** Kingdoms hand out named offices (e.g. Magister Militum per Gallia, Magister Officiorum, Comes Africae, Eran-Spahbed) to their most respected lords, and a ruling player can appoint vassals to offices through the minister. A player serving Rome rises through honorary ranks - Vir Clarissimus, then Spectabilis, then Illustris - as his relation with the emperor reaches 15, 30 and 50, each announced by a promotion screen. Titles show in lord names and notes.

**How it works:** assign_rank(office, faction): among the faction's lords without an office (troop 155 == 0) and with rank >= 1 (troop 156), pick the one with the best relation-to-ruler + renown/2 (min 300), set troop 155 = office, then troop_set_title_according_to_faction (modified, 165 stmts) rebuilds his displayed name; called from change_troop_faction and indict_lord_for_treason so offices are refilled when holders leave. Player: trig:21-24 (24h, one-shot) require homage to fac_kingdom_1/2 and relation with either emperor >= 15/30/50 and the previous rank in troop 156, then jump to menu_promotion_clarissimus/spectabilis/illustris whose 'Accept the title' option sets troop 156. dlg:1364-1373 (minister_grant_rank_choose_office) let a ruling player assign the office list. game_get_troop_note shows the rank.

- **Hooks:** `trig:21:conseq`, `trig:22:conseq`, `trig:23:conseq`, `trig:24:conseq`, `dlg:701:dlga_minister_talk:minister_grant_rank:cond`, `script:change_troop_faction`
- **Scripts:** `assign_rank`, `troop_set_title_according_to_faction`, `change_troop_faction`, `indict_lord_for_treason`, `game_get_troop_note`
- **Menus:** `menu_promotion_clarissimus`, `menu_promotion_spectabilis`, `menu_promotion_illustris`, `menu_promotion_officorum`
- **Dialogs:** `dlg:701`, `dlg:1364`, `dlg:1365`, `dlg:1366`, `dlg:1367`, `dlg:1368`, `dlg:1369`, `dlg:1370`, `dlg:1371`, `dlg:1372`, `dlg:1373`
- **Slots:** `troop:155`, `troop:156`, `troop:7`, `faction:11`
- **Globals:** `g_king_start`, `g_player_culture`, `player_honor`, `player_has_homage`, `players_kingdom`
- **Module-specific resources:** string: office names: Comes Domesticus, Magister Officiorum, Magister Militum per Gallia, Magister Utriusque Militiae, Comes Illyricum, Comes Hispenias, Comes Africae, Eran-Spahbed ...
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis ad457 assign_rank: troop 155/156 selection by relation + renown, troop_set_title_according_to_faction`, `dis ad457 trig:21/22/24:cond: homage + relation >=15/30/50 + troop 156 rank steps`, `slot ad457 troop 156: written by promotion menus' accept options, read by assign_rank and trig:22-24`, `global ad457 g_king_start readers include dlg:1364-1373 'minister_grant_rank_choose_office'`, `explain ad457 assign_rank: text 'Comes_Domesticus | Magister_Officiorum | Magister_Militum_per_Gallia ...'`
- **Overlaps:** `acan.enlistment_career_events`, `acan.ranks_offices_titles`, `acw.enlistment_contract_career`, `acw.freelancer_extensions`, `ad457.freelancer_variant`, `be.enlistment_service_ranks`, `bi.freelancer_reassignment`, `laigle.military_rank_career`, `pop.knighthood_order_membership`, `tld.faction_rank_influence`

<a id="befaction-technology-tree"></a>
### National military technology tree with dated inventions — be (`be.faction_technology_tree`)

**What it does:** Each nation researches about 19 military technologies (rifled muskets, breech-loaders, smokeless powder, modern artillery, skirmish-line and modern attack tactics, machine guns, gas...). Each has an historical year; once that year is reached a nation may invent it at random (faster at higher game speed or for rich nations), and the player can fund research from the budget. Technologies switch what the battle systems allow: gun models, formations, abilities, rifle issued to troops, uniforms.

**How it works:** faction slots 406-424 hold state (10000 = invented); 425-443 the year each becomes available (slot+19); 768 national budget. strig:113 (24 h): for each live kingdom and tech not invented with year <= $g_current_year, chance 1000/$g_game_speed (halved if budget <= 1000) out of 3000 -> invented, message 'The {s1} has finished researching technology {s2}'. prsnt_faction_technologies shows the tree (pts_create_tech_button, pts_create_selected_tech_name/description, cf_pts_check_tech_availability) with a Research button ('Country does not have enough budget to start research'). Gate predicates cf_if_party_/team_/agent_faction_invented_technology are called from ~250 sites (formation changes: '{s1} cannot change formation - you need to research Skirmish Line Tactics'). strig:123 swaps uniforms when uniform techs land.

- **Hooks:** `strig:113`, `prsnt:faction_technologies/t0`, `prsnt:faction_technologies/t1`, `menu:tech_invented`, `strig:123`
- **Scripts:** `cf_if_party_faction_invented_technology`, `cf_if_team_faction_invented_technology`, `cf_if_agent_faction_invented_technology`, `cf_pts_check_tech_availability`, `pts_create_tech_button`, `pts_create_selected_tech_name`, `pts_create_selected_tech_description`, `initialize_factions_technology_and_presets`, `get_strength_modifier_for_faction_by_technologies`, `uniform_progression_change_officer_clothes`
- **Menus:** `menu_tech_invented`, `menu_start_game_choose_date`
- **Presentations:** `prsnt_faction_technologies`
- **Slots:** `faction:406-424`, `faction:425-443`, `faction:768`
- **Globals:** `g_current_year`, `g_game_speed`, `g_faction_technologies_*`
- **Module-specific resources:** mesh: mesh_faction_technologies_*; string: str_faction_technology_*_name, str_faction_technology_*_description
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis be strig:113 (dated random invention)`, `dis be cf_if_party_faction_invented_technology (slot == 10000)`, `explain be prsnt:faction_technologies/t0 (tech names, Research button)`, `text be: research messages and formation-gate messages`

<a id="bemanpower-conscription-dynamic-lords"></a>
### National manpower pool, conscription policy and population-scaled lord count — be (`be.manpower_conscription_dynamic_lords`)

**What it does:** Each nation has a manpower pool that refills from its population according to its conscription policy (volunteer 3 %, limited 10 %, extended 20 %, wide 25 %). Lords and garrisons refill only by drawing from that pool, so long wars exhaust a country. The number of lords a nation fields and their party size scale with population and army-size policy; lords are drawn from (or returned to) a shared pool of lord troops as nations grow, shrink or are annexed.

**How it works:** faction slots: 769 population, 876 manpower, 877 manpower cap, 878 policy, 879 reinforcement chance %, 825 army-size %, 828 military spending counter. pas_faction_set_conscription_policy(f, 1..4): cap = population/11000 (min 50) x 30/100/200/250 %, re-bases pool, chance = pool x100/800 clamped 5..100. pas_faction_calculate_manpower (per PPS iteration): pool += sqrt(population)/2500 (12..500) x policy factor, clamp -2000..cap. cf_pas_faction_reinforcement_required(f, cost): roll chance (slot 879) then subtract cost from pool. pas_reinforce_party(party): if below party_get_ideal_size and the roll passes (cost 3 for centres, 7 for lords) adds 3+3+1 (or 2+3+1+1 for lords) of the faction's four troop types (faction 809-812), adds 20 to 828, trims excess; adds artillery officers if tech 424 and few guns. pas_get_faction_ideal_lord_number = population/2,000,000 x 825/100 + 3 (3..50). party_get_ideal_size (modified Native) = $preferred_ai_party_size (+25 for the faction leader) or for lords preferred-30 + 4 x ideal lords, clamp 50..200. pas_faction_manage_lord_number (per iteration, max 2 changes): too few -> pas_init_lord takes a factionless lord from trp_knight_1_1..trp_kingdom_1_pretender; too many -> remove_lord_from_game. strig:50 (24 h) respawns defeated lords only if cf_pas_faction_reinforcement_required(f, 0) succeeds. prsnt_pas_menu shows army size, policy slider and penalties to satisfaction/workers.

- **Hooks:** `strig:124 (pps_faction_iteration -> pas_*)`, `strig:50`, `prsnt:pas_menu/t0`, `prsnt:pas_menu/t1`
- **Scripts:** `pas_faction_set_conscription_policy`, `pas_faction_calculate_manpower`, `pas_faction_get_manpower_growth_rate`, `cf_pas_faction_reinforcement_required`, `pas_reinforce_party`, `pas_get_faction_ideal_lord_number`, `pas_faction_manage_lord_number`, `pas_init_lord`, `remove_lord_from_game`, `party_get_ideal_size`, `pas_get_conscription_policy_name`, `pas_faction_buy_military_resources`
- **Presentations:** `prsnt_pas_menu`
- **Slots:** `faction:769`, `faction:825`, `faction:828`, `faction:809-812`, `faction:876`, `faction:877`, `faction:878`, `faction:879`, `party:580`
- **Globals:** `preferred_ai_party_size`
- **Relation to Native:** replaces-native
- **Confidence:** confirmed
- **Evidence:** `dis be pas_faction_set_conscription_policy / pas_faction_calculate_manpower / cf_pas_faction_reinforcement_required / pas_reinforce_party`, `explain be prsnt:pas_menu/t0 texts 'Volunteer army (3% of the population)' ... 'Wide conscription (25%)'`, `dis be pas_get_faction_ideal_lord_number, party_get_ideal_size`, `BUG: pas_faction_manage_lord_number stmt 24 '(eq, :l5, :l5, :l0)' - three operands, compares l5 with itself, so the 'too many lords' branch removes lords of ANY faction`
- **Overlaps:** `acan.legions_cohorts_army_organisation`, `acw.conscription`, `acw.regional_regiment_recruitment`, `ad457.barracks_recruitment_screen`, `ad457.village_reinforcement_marches`, `awoiaf.hold_elite_trainers`, `bi.military_academy_upgrades`, `laigle.typed_volunteer_recruitment`, `pop.garrison_and_lord_training`, `pop.noble_recruit_pool`, `tld.town_volunteers_and_reserves`

<a id="cbltwelve-borderland-kingdoms"></a>
### Twelve borderland kingdoms with ten new cultures — cbl (`cbl.twelve_borderland_kingdoms`)

**What it does:** Twelve new factions hold the new lands: Braetynia, Sudestria, Xothay, Jumne, Phoessanid Empire (4-5 towns each), the city-states of Wunden, Blackstone and Su'undi, two knightly orders (White Knights, Golden Crusaders) and two clans (Hisu, Suju). Each has a king, 3-20 lords, its own five-tier troop line, banner block, tournament gear and encounter picture; six have pretenders.

**How it works:** factions.txt INSERTS culture_9..20 after culture_6 and kingdom_9..20 after kingdom_6 (kingdom_1 moves from idx 16 in the base module to 28; fac_kingdoms_end 23 -> 47), so the Native kingdom range loops cover them. game_start: culture slots 41-45 (recruit..elite) and 53-58 (walkers), kingdom slot 10 (culture) / 11 (leader) / 15 (banner mesh) / 22 (adjective string), leader renown troop slot 7, 23 town and 54 castle grants, 23 town lords, claim slots party:62 on 21 centres (incl. Native ones such as p_town_2 for kingdom 9), pretender home slot troop:60 for kingdoms 9-13 and 15; lord banners via spr_banner_a + per-kingdom offsets 126..268. Hardcoded faction numbers elsewhere are bumped (encounter_init_variables/add_routed_party ranges 16..23 -> 28..47, get_default_formation, field_tactics). Per-kingdom tournament gear (menu:town_tournament/opt:tournament_join_next_fight) and encounter backgrounds (menu:simple_encounter, mesh_pic_kingdomN_encounter). The Dark Knights invasion (strig:134/135) sets -40 relations with kingdoms 9-13/17/18 and names the Dark lords; strig:139 gives kingdom-specific armour for kingdoms 9-13. Lords: kingdoms 9-13 one king + 20 knights + pretender; 14-16 king + 8; 17-18 king + 5; 19-20 king + 3.

- **Hooks:** `script:game_start`, `strig:134`, `strig:135`, `strig:139`, `menu:simple_encounter`, `menu:town_tournament/opt:tournament_join_next_fight:conseq`
- **Scripts:** `game_start`, `initialize_faction_troop_types`, `initialize_banner_info`, `initialize_aristocracy`, `initialize_npcs`, `get_culture_with_faction_for_music`, `encounter_init_variables`, `add_routed_party`, `get_default_formation`, `field_tactics`, `create_kingdom_hero_party_dk`, `dplmc_start_alliance_between_kingdoms`, `dplmc_start_defensive_between_kingdoms`, `dplmc_start_nonaggression_between_kingdoms`, `dplmc_start_trade_between_kingdoms`
- **Menus:** `menu_simple_encounter`, `menu_town_tournament`
- **Presentations:** `prsnt_banner_selection`, `prsnt_game_profile_banner_selection`, `prsnt_culture_troop_tree`
- **Slots:** `faction:10`, `faction:11`, `faction:15`, `faction:22`, `faction:41`, `faction:42`, `faction:43`, `faction:44`, `faction:45`, `faction:53`, `faction:54`, `faction:55`, `faction:56`, `faction:57`, `faction:58`, `party:62`, `troop:7`, `troop:13`, `troop:60`
- **Globals:** `$players_kingdom`
- **Module-specific resources:** faction: fac_culture_9..fac_culture_20, fac_kingdom_9..fac_kingdom_20; troop: trp_kingdom_9_lord..trp_kingdom_20_lord, trp_knight_9_1.., trp_brettonian_*, trp_sudestrian_*, trp_eastern_*, trp_jumne_*, trp_phoessanid_*, trp_wunden_*, trp_blackstone_*, trp_suundi_*, trp_paladin_*, trp_ninja_*; mesh: mesh_banner_kingdom_h..l, mesh_banner_kingdom_14..20, mesh_pic_kingdom9_encounter..; spr: ~180 extra banner props
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `troop name scan: kingdoms 9-13 20 knights, 14-16 8, 17-18 5, 19-20 3`
- **Overlaps:** `cbl.expanded_calradia_map`, `cbl.new_centre_economy_and_arena_wiring`, `cbl.v352_later_version_changes`

<a id="popfief-stewards-with-skills"></a>
### Fief stewards with real skills that the player can train — pop (`pop.fief_stewards_with_skills`)

**What it does:** Every town/castle seneschal and village elder is a skilled steward (random skills at game start). Their engineering, trade, trainer and other skills drive building repair and AI construction, garrison training, heartbeat-crisis outcomes and income. The lord can hold a paid 'training session' (a few hours of waiting, 150 denars per hour) that raises the steward's skills up to the best in the player's party. The steward is also the hub for feasts, tournaments, gossip, mine closing and the war room.

**How it works:** initialize_steward_skills (from game_start) gives each seneschal (trp_town_1_seneschal..) 69 random skill points and each village elder 39. game_start / pop2_location_improvements store the steward troop in party slot 293. pop_check_steward_skills(steward) totals the gap between the steward's skills and get_max_skill_of_player_party; menu:steward_training (reached from dlg:2293 steward_menu3 / dlg:3393 village_elder_menu3) prices it at hours = gap (3..18) and 150 denars/hour; confirm (opt:steward_training_confirm) pays, calls pop_train_steward (raises each of ~14 skills, e.g. 27, 0, 7, 22, 9 ..., to the party max with troop_raise_skill) and rests in the town for the duration. Consumers: auto_repair_buildings / random_build_buildings (skill 8 engineering), strig:31 garrison XP (skill 17 trainer), pop3_heartbeat_resolve (skills 7/8/15/22), menu:center_improve text ('Your steward, with an engineering skill of ...').

- **Hooks:** `dlg:2282:dlga_start:steward_menu:cond`, `dlg:2293:dlga_steward_menu:steward_menu3:cond`, `dlg:3393:dlga_village_elder_talk:village_elder_menu3:cond`, `menu:steward_training/opt:steward_training_confirm:conseq`, `script:game_start`
- **Scripts:** `initialize_steward_skills`, `pop_check_steward_skills`, `pop_train_steward`, `get_max_skill_of_player_party`, `pop2_location_improvements`
- **Menus:** `menu_steward_training`, `menu_steward_training_complete`
- **Dialogs:** `dlg:2282-2431 steward_menu*`, `dlg:3393 village_elder_menu3`
- **Slots:** `party:293`, `party:295`
- **Globals:** `pop_train_steward_hours`, `auto_enter_town`, `g_town_visit_after_rest`, `g_last_rest_center`
- **Module-specific resources:** mesh: mesh_pic_pendor_village_training
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis menu:steward_training + confirm option (full)`, `dis initialize_steward_skills (full)`, `dis pop_train_steward head: skill-by-skill raise to party max`, `slot pop party 293: 57 accesses across improvements, training, heartbeat`
- **Overlaps:** `acan.culture_specific_fief_buildings`, `acan.latifundium_estates`, `ad457.center_buildings_management`, `ad457.lord_business_build_hire_upgrade`, `bi.ai_lords_build`, `bi.garrison_building_battle_bonuses`, `bi.roman_public_buildings`, `pop.fief_base_income_and_reports`, `pop.fief_heartbeat_problems`, `pop.fief_improvements_expanded`, `sw.recruit_unlock_buildings`, `vc.extended_center_improvements`

<a id="swplayer-faction-culture-switch"></a>
### Choose the culture (troop tree) of the player's own faction — sw (`sw.player_faction_culture_switch`)

**What it does:** A ruler can switch his faction's culture between Empire, Rebel, Hutt and Human (independent), which changes which troop tree his towns and minor planets recruit.

**How it works:** menu:change_culture options call change_culture_empire / _rebel / _hutt / _human, each rewriting the player faction's faction slots (culture and troop references: 9, 41-52, 77-79, 83-85 ...) and printing 'Player Faction culture is now ...'. Also offered at character start (menu:choose_skill begin_adventuring).

- **Hooks:** `menu:change_culture`, `menu:choose_skill/opt:begin_adventuring:conseq`
- **Scripts:** `change_culture_empire`, `change_culture_rebel`, `change_culture_hutt`, `change_culture_human`
- **Menus:** `menu_change_culture`
- **Slots:** `faction:9, 41-52, 77-79, 83-85`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `explain sw change_culture_empire: callers menu:change_culture, menu:choose_skill; faction slot writes`, `qstr 'Player Faction culture is now Galactic Empire.'`

<a id="vcmarshal-election"></a>
### Marshal elections with candidates and lord votes — vc (`vc.marshal_election`)

**What it does:** Instead of the king silently picking a marshal, a faction periodically holds an election: two candidates are put forward, lords give their support, the player can be asked to stand as a candidate (accept or decline) and sees a screen with each candidate's supporters.

**How it works:** strig:33 (every 24h) checks the player's faction and opens prsnt_marshal_selection (candidates #1/#2, 'Number of Supporters', 'Whom do you wish to support', '{s1} gives his support...'); globals $g_presentation_marshal_selection_max_renown_1/_2 (+_troop) hold the top-renown candidates. menu_marshal_selection_candidate_ask (accept / reject) when the player is suggested. The winner is installed by appoint_faction_marshal (a renamed copy of Native appoint_faction_marshall, 64 stmts: party_set_marshall, relation changes for disappointed lords, log entry 32).

- **Hooks:** `strig:33`, `menu:marshal_selection_candidate_ask`
- **Scripts:** `appoint_faction_marshal`, `party_count_fit_for_battle`, `party_get_ideal_size`
- **Menus:** `menu_marshal_selection_candidate_ask`
- **Presentations:** `prsnt_marshal_selection`
- **Slots:** `faction:8`, `faction:11`, `troop:157`
- **Globals:** `g_presentation_marshal_selection_max_renown_1`, `g_presentation_marshal_selection_max_renown_1_troop`, `g_presentation_marshal_selection_max_renown_2`, `g_presentation_marshal_selection_max_renown_2_troop`, `total_promotion_changes`
- **Relation to Native:** modifies-native
- **Confidence:** strongly-inferred
- **Evidence:** `dis vc script:appoint_faction_marshal = Native appoint_faction_marshall logic (64 stmts both)`, `sqlite refs: prsnt_marshal_selection <- strig:33, menu:marshal_selection_candidate_ask options`, `sqlite refs strig:33/prsnt: qstr Candidate_#1/#2, Number_of_Supporters, Whom_do_you_wish_to_...`
- **Overlaps:** `be.pas_marshal_campaign_ai`, `tld.faction_strength_war_progression`, `tld.war_theaters_advance_camps`

<a id="acanconspiracy-treason-trials"></a>
### Conspiracies against the ruler (palace assassination fights) and treason or embezzlement trials — acan (`acan.conspiracy_treason_trials`)

**What it does:** A player-ruler who enters their palace or castle can be ambushed by conspirators. The odds depend on unrest, honour, piety, right to rule, edicts and how much the lords hate them, and an attack becomes a fight in the palace. Lords, and the player, can also be put on trial for treason or embezzlement; friends and paid agents can intervene, and a guilty verdict strips offices.

**How it works:** menu:town options town_castle / visit_palace call cf_conspiracy_check (137 stmts). It scores lords' relations (troop_get_relation_with_troop), $g_unrest, $player_honor, $player_piety, $player_right_to_rule and $edict6, respects a cooldown ($g_last_assassination_attempt_time), and on success jumps to menu_conspiracy, whose 'continue' fills the palace scene with the conspirators from trp_array_villa_feast and starts mst_conspiracy_fight. Trials: indict_lord_for_treason (modified Native), menu:trial_guilty and dlg trial_guilty (remove_office_from_troop, gold fines). Wives/ladies or bought agents (Locusta, Crispinilla) can intervene via intervene_treason (troop slot 22, quest 6). Embezzlement from the treasury leads to menu_caught_embezzle_punished.

- **Hooks:** `menu:town/opt:town_castle:conseq`, `menu:town/opt:visit_palace:conseq`, `menu:conspiracy/opt:continue:conseq`, `menu:trial_guilty`, `dlg:5622:dlga_trial_guilty`, `dlg:7243:dlga_lady_treason_relation_check_roman`, `dlg:9722:dlga_locusta_treason_success`
- **Scripts:** `cf_conspiracy_check`, `intervene_treason`, `indict_lord_for_treason`, `remove_office_from_troop`, `search_troop_prisoner_of_party`, `change_troop_intrigue_impatience`, `cf_troop_can_intrigue`
- **Menus:** `menu_conspiracy`, `menu_trial_guilty`, `menu_treason`, `menu_caught_embezzle_punished`
- **Mission templates:** `mst_conspiracy_fight`, `mst_kill_supporters`
- **Slots:** `troop:22`, `troop:52`, `troop:178`, `troop:183`, `quest:6`
- **Globals:** `g_last_assassination_attempt_time`, `g_unrest`, `player_honor`, `player_piety`, `player_right_to_rule`, `edict6`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `explain acan cf_conspiracy_check: callers menu:town palace/castle options, globals g_unrest/player_honor/piety/right_to_rule/edict6, menu_conspiracy`, `dis acan menu:conspiracy/opt:continue:conseq: set_jump_mission mst_conspiracy_fight with conspirators from trp_array_villa_feast`, `explain acan intervene_treason: 'has agreed to intervene on your behalf. Wait now till the trial'`
- **Overlaps:** `acw.alliance_blocs`, `ad457.ai_tributary_states_casus_belli`, `ad457.minor_tribes_and_tributaries`, `awoiaf.letters_to_lords`, `awoiaf.spy_network_sabotage`, `awoiaf.static_wars_scripted_diplomacy`, `be.infamy_casus_belli_alliances`, `be.peace_negotiations_victory_points`, `bi.diplomacy_suite`, `tld.gift_bribe_courier_quest`

<a id="acansenate-influence-edicts"></a>
### Influence points, Senate support and kingdom-wide edicts voted in the Senate — acan (`acan.senate_influence_edicts`)

**What it does:** Influence becomes a currency the player spends on political actions: asking for titles, forcing peace talks, bribing lords and changing governors. The ruler also needs the Senate's support (40 senators, won by persuasion or bribes), and support passes or blocks kingdom edicts. Edicts are laws that add taxes or subsidies to the budget and raise or lower unrest.

**How it works:** Influence is stored in troop slot 6 and changed by change_influence (31 callers, 475 reachable entry points: dialogs, menus, quests). get_influence_cost_for_decision prices a decision from a base cost adjusted by culture difference, piety ($player_piety), the target lord's personality, honour, rank and province modifiers; it is used by the peace-declaration, bribe, honorary-title and governor-change dialogs and presentations. Senate support is a percentage on trp_senator_dummy slot 19, scaled to 40 senators. change_senate_support adjusts it, lowers the player's controversy (troop slot 166) and, per point, may raise relation with Rome (persuasion) or cost honour (bribery). prsnt:senate runs cf_menu_condition_senate (274 stmts, 93-block closure), the hub for speeches (give_a_speech), Senate decisions and office removal. Edicts are globals $edict1..$edict11 (for example libelli, securitatis publica, Christiani, slave manumission tax). Each is proposed in menu:debate_in_senat_2, where a majority vote passes or fails it, or issued through minister dialogs (dlg:4159-4178 edicts2). They feed calculate_bureaucratic_costs and calculate_edict_tax (budget), strig:19 (unrest/stability), strig:176, calculate_latifundium_rents and display_policy_string_to_reg.

- **Hooks:** `prsnt:senate/t0`, `prsnt:senate/t1`, `menu:debate_in_senat_2`, `menu:senate_decide`, `dlg:4159:dlga_edictum_christiani2`, `dlg:4163:dlga_edicts2`, `dlg:2950:dlga_senator_convince_persuade`, `dlg:2957:dlga_senate_talk_bribe5`, `strig:19`, `strig:176`
- **Scripts:** `change_influence`, `get_influence_cost_for_decision`, `change_senate_support`, `cf_menu_condition_senate`, `give_a_speech`, `display_policy_string_to_reg`, `calculate_edict_tax`, `calculate_bureaucratic_costs`, `change_troop_controversy`
- **Menus:** `menu_debate_in_senat_2`, `menu_senate_decide`, `menu_senate_discussion`
- **Presentations:** `prsnt_senate`, `prsnt_influence_nero`, `prsnt_influence_governor_change`, `prsnt_influence_governor_change_senate`
- **Mission templates:** `mst_senate_meeting`, `mst_senate_cuttscene`
- **Slots:** `troop:6`, `troop:166`, `troop:19`, `troop:52`
- **Globals:** `edict1`, `edict2`, `edict4`, `edict6`, `edict7`, `edict8`, `edict9`, `edict10`, `edict11`, `g_has_senat_sup`, `g_unrest`, `player_piety`, `player_honor`, `g_libelli`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis acan change_influence: troop slot 6, messages 'Your influence has changed from {reg11} to {reg12}'`, `explain acan get_influence_cost_for_decision: text '_Base:', 'Different culture', 'Pietas', 'Personality'`, `dis acan change_senate_support: trp_senator_dummy slot 19, x40 senators, troop 166 controversy`, `global acan edict4/edict11 writers/readers incl. menu:debate_in_senat_2 'The majority has voted for/against your proposal'`
- **Overlaps:** `acan.imperial_treasury_budget`, `acan.town_decrees`, `ad457.dplmc4_tax_inefficiency_and_extras`, `be.pps_political_simulation`

<a id="acwalliance-blocs"></a>
### Permanent two-bloc war (Union armies vs Confederate armies) — acw (`acw.alliance_blocs`)

**What it does:** The map's seven factions are grouped into fixed blocs: the three Union armies are permanently allied with each other and permanently at war with the three Confederate armies; only the Native faction makes war and peace freely. Random peace/war rolls, border incidents and truce bookkeeping skip bloc pairs.

**How it works:** strig:25 (daily) calls set_ally_script_behavior: diplomacy_start_peace_between_kingdoms for every intra-bloc pair (kingdoms 1,2,7 / 4,5,6) and diplomacy_start_war_between_kingdoms for every cross-bloc pair. check_factions_are_allies (same bloc, or the player's king-start faction joining its bloc) also forces set_relation 100 both ways; check_factions_are_enemies is the cross-bloc test; check_factions_cant_change_politics (allies OR enemies -> reg20=1) is consulted by diplomacy_faction_get_diplomatic_status_with_faction, diplomacy_start_peace_between_kingdoms, npc_decision_checklist_peace_or_war, randomly_start_war_peace_new and the border-incident/truce/casus-belli loop in strig:25, so those systems skip locked pairs.

- **Hooks:** `strig:25`, `script:game_start`
- **Scripts:** `set_ally_script_behavior`, `check_factions_are_allies`, `check_factions_are_enemies`, `check_factions_cant_change_politics`, `diplomacy_start_peace_between_kingdoms`, `diplomacy_start_war_between_kingdoms`, `diplomacy_faction_get_diplomatic_status_with_faction`, `randomly_start_war_peace_new`, `npc_decision_checklist_peace_or_war`
- **Slots:** `faction:21`
- **Globals:** `king_start`, `king_faction`, `players_kingdom`
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `dis acw set_ally_script_behavior / check_factions_are_allies / check_factions_cant_change_politics / strig:25`, `callers acw check_factions_cant_change_politics (6 call sites)`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_scripts.py 47290 set_ally_script_behavior`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_constants.py 2067-2076 union/confederate kingdom ranges; ID_factions.py (kingdom_7 = 17 between kingdom_1 = 16 and kingdom_2 = 18)`
- **Overlaps:** `acan.conspiracy_treason_trials`, `ad457.ai_tributary_states_casus_belli`, `ad457.minor_tribes_and_tributaries`, `awoiaf.letters_to_lords`, `awoiaf.spy_network_sabotage`, `awoiaf.static_wars_scripted_diplomacy`, `be.infamy_casus_belli_alliances`, `be.peace_negotiations_victory_points`, `bi.diplomacy_suite`, `tld.gift_bribe_courier_quest`

<a id="ad457ai-tributary-states-casus-belli"></a>
### Weak kingdoms become tributaries; provocations lead to reparation demands — ad457 (`ad457.ai_tributary_states_casus_belli`)

**What it does:** Kingdoms reduced to one to three fortresses look for protection: every two days one such kingdom may submit as a tributary to a stronger enemy that has a grudge against it, paying 20,000 and making peace; its other wars are ended or joined to its overlord's. The player's kingdom can be offered a tributary in the same way. When one realm has a casus belli against another, the aggrieved ruler may demand reparations (8,000 per town, 4,000 per castle of the offender) instead of going straight to war; the offender pays or war starts. The player can be on either side of such a demand.

**How it works:** strig:127 (every 48h): random active kingdom with faction slots 81+82 (castles+towns) in 1-3; for every active faction, reads the computed per-pair faction arrays at 820+other (friendly treaty state, >40 counted) and 1020+other (grievance/provocation score); picks the hostile faction with the highest grievance that is bigger, compares against a resistance score 300 - 30*(#factions it has grievances over) + 30*holdings + 30*friends; if beaten calls dplmc_start_tributary_between_kingdoms(weak, strong, 1), or if the strong one is the player's kingdom raises menu_notification_tributary_offer. dplmc_start_tributary_between_kingdoms (97 stmts): faction slot 100 = overlord, relation +15 (min 40), prisoner exchange, rulers' wealth -/+20000, player relation updates, notification menu_dplmc_notification_tribute_declared, peace both ways, sets 820+ pair slots to 160 and clears 1020+ grievances, makes the tributary leave wars with overlord's friends and join the overlord's wars. strig:27 -> randomly_start_war_peace_new_for_faction (269 stmts, per-faction variant of Native's war/peace script) raises menu_notification_casus_belli_decide: both sides run npc_decision_checklist_peace_or_war, ruler reputation types 1/4/5 are more aggressive; result is war, menu_notification_tribute_demanded (if the player rules the offender), reparations paid via add_to_troop_wealth, or war on refusal. menu_decide_ai_tribute handles the player's own demand. Expiries via menu_dplmc_notification_tribute_expired_*.

- **Hooks:** `strig:127`, `strig:27`, `menu:notification_casus_belli_decide`, `menu:decide_ai_tribute`, `menu:notification_tributary_offer`
- **Scripts:** `dplmc_start_tributary_between_kingdoms`, `randomly_start_war_peace_new_for_faction`, `npc_decision_checklist_peace_or_war`, `diplomacy_start_war_between_kingdoms`, `count_parties_of_faction_and_party_type`, `add_to_troop_wealth`, `exchange_prisoners_between_factions`, `count_wars_and_pacts`
- **Menus:** `menu_notification_casus_belli_decide`, `menu_notification_tribute_demanded`, `menu_decide_ai_tribute`, `menu_notification_tributary_offer`, `menu_dplmc_notification_tribute_declared`, `menu_dplmc_notification_tribute_expired_1_tribute_of_2`, `menu_dplmc_notification_tribute_expired_2_tribute_of_1`, `menu_notification_decide_tributary_war_decleration`, `menu_threat_war_reaction`, `menu_persuade_war_reaction`
- **Slots:** `faction:100`, `faction:81`, `faction:82`, `faction:21`, `faction:32`, `faction:820+f (computed per-pair array)`, `faction:1020+f (computed per-pair array)`, `troop:52`
- **Globals:** `g_notification_menu_var1`, `g_notification_menu_var2`, `g_last_acting_faction`, `g_last_target_faction`
- **Module-specific resources:** string: str_diplo_casus_expired_reparations_accepted, str_diplo_casus_expired_reparations_refused_war
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis ad457 strig:127: weak-faction selection by slots 81/82, grievance arrays 820/1020+f, call dplmc_start_tributary_between_kingdoms or menu_notification_tributary_offer`, `dis ad457 dplmc_start_tributary_between_kingdoms: slot 100, +/-20000 wealth, peace, war inheritance loops`, `dis ad457 menu:notification_casus_belli_decide: reparations 8000/town + 4000/castle, war on refusal, player branch -> menu_notification_tribute_demanded`, `refs ad457 menu menu_notification_casus_belli_decide: raised from strig:27`, `dis ad457 menu:decide_ai_tribute: player's own reparation demand pays troop_add_gold`
- **Overlaps:** `acan.conspiracy_treason_trials`, `acw.alliance_blocs`, `ad457.minor_tribes_and_tributaries`, `awoiaf.letters_to_lords`, `awoiaf.spy_network_sabotage`, `awoiaf.static_wars_scripted_diplomacy`, `be.infamy_casus_belli_alliances`, `be.peace_negotiations_victory_points`, `bi.diplomacy_suite`, `tld.gift_bribe_courier_quest`

<a id="ad457minor-tribes-and-tributaries"></a>
### Independent tribes with capitals, patrols, migration, conquest and tribute — ad457 (`ad457.minor_tribes_and_tributaries`)

**What it does:** About 37 small independent peoples (Aestii, Dani, Frisians, Vascones, Garamantes, steppe hordes and others) each have a capital, a king, a garrison and roaming patrols. The player can visit, recruit their warriors, attack the capital, and afterwards loot it, pillage it or turn the tribe into a tributary that pays a monthly tribute; tributary kings can be asked for levies or a special tribute. Nomadic tribes periodically pack up their camp, travel across the map and settle somewhere new.

**How it works:** init_minor_factions (598 stmts, game_start) sets up fac_minor_* factions (culture slot 10, leader 11, templates 41-52/77), their capital parties (p_aestii_village .. before p_religious_site_1) with scenes, kings and merchants, gold and ages. strig:117 (72h): spawn_minor_faction_patrols (up to 3 parties of template faction slot 77 per capital, patrol radius 25, home = party 123), restores a free king as leader of his capital's stack, keeps Mediterranean pirates (spawn_pirate, <3) and Roman fleets (spawn_naval_patrol_ravenna/naples/constantinople) alive. fully_refresh_minor_faction_garrison(capital, size) refills garrisons from slot 77. game_event_party_encounter -> menu_minor_faction_town (137 stmts: quest branches, hostility/tributary text via faction slot 299, burned -> menu_settlement_burned, looted (party 255) -> menu_settlement_looted), recruiting via prsnt_barracks, attack -> menu_minor_town_fight -> menu_minor_town_loot (options: tributary state, pillage, quest). Faction slot 299 = 1 marks a tributary of the player (set by the loot menu and dlg:5893 'I accept your offer. We will pay a monthly tribute of 1000...'; read by prsnt:budget_report and dialogs dlg:5852 levies / dlg:5859 special tribute). Migration in strig:147 stmts 53-132: a nomad/ship capital (icon nomad_camp/ship/steppe_lord) with a linked camp party (slot 123) rolls 1/180, picks a land point >5 away and >3 from other centres, sets icon steppe_lord and travels; on arrival sets icon nomad_camp and becomes enterable again ('The {s13} have settled near {s12}').

- **Hooks:** `script:game_start`, `strig:117`, `strig:147`, `script:game_event_party_encounter`, `menu:minor_faction_town`, `menu:minor_town_loot/opt:continue_tributary:conseq`
- **Scripts:** `init_minor_factions`, `init_minor_kings`, `spawn_minor_faction_patrols`, `fully_refresh_minor_faction_garrison`, `setup_minor_Faction_king_meeting`, `spawn_pirate`, `spawn_naval_patrol_ravenna`, `spawn_naval_patrol_naples`, `spawn_naval_patrol_constantinople`, `get_closest_center`
- **Menus:** `menu_minor_faction_town`, `menu_minor_town_fight`, `menu_minor_town_loot`, `menu_minor_town_pillage`, `menu_attack_minor_town`, `menu_settlement_burned`, `menu_settlement_looted`
- **Presentations:** `prsnt_barracks`, `prsnt_budget_report`
- **Mission templates:** `mst_visit_minor_town`, `mst_minor_village_attack`, `mst_minor_village_attack_quest`
- **Dialogs:** `dlg:5852`, `dlg:5859`, `dlg:5863`, `dlg:5893`
- **Slots:** `faction:299`, `faction:77`, `faction:10`, `faction:11`, `faction:21`, `party:123`, `party:255`, `troop:60`
- **Globals:** `g_last_rest_center`
- **Module-specific resources:** faction: fac_minor_aestii .. (37 minor factions); party: p_aestii_village, p_dani_village, p_onoguroi_village, p_garamantian_village_1, ... (tribal capitals); pt: pt_aestii_party_1, pt_dani_party, ... pt_pirates_mediterranean, pt_classis_ravenna/naples/constantinople; scene: scn_minor_roman_town, scn_aestii_town, scn_dani_town, scn_panticapaeum, ...; icon: nomad_camp, steppe_lord, ship
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `explain ad457 init_minor_factions: 37 fac_minor_* refs, tribal capitals, kings, scenes`, `dis ad457 strig:117: spawn_minor_faction_patrols, king re-attachment, pirates, Roman fleets`, `dis ad457 strig:147 stmts 53-132: migration with icons steppe_lord/nomad_camp and log 'The {s13} have settled ...'`, `dis ad457 menu:minor_faction_town; explain ad457 menu:minor_town_loot: options continue_tributary / continue_pillage`, `slot ad457 faction 299: writers = tributary dialogs/menu; readers = budget report, levy/tribute dialogs`
- **Overlaps:** `acan.conspiracy_treason_trials`, `acw.alliance_blocs`, `ad457.ai_tributary_states_casus_belli`, `awoiaf.letters_to_lords`, `awoiaf.spy_network_sabotage`, `awoiaf.static_wars_scripted_diplomacy`, `be.infamy_casus_belli_alliances`, `be.peace_negotiations_victory_points`, `bi.diplomacy_suite`, `tld.gift_bribe_courier_quest`

<a id="awoiafessos-war-peace-driver"></a>
### Separate Essos war/peace driver — awoiaf (`awoiaf.essos_war_peace_driver`)

**What it does:** Essos factions get their own daily random war/peace roll, independent from the Westeros factions, so the two continents run separate political theatres even in Static Wars mode.

**How it works:** strig:53 (24h, gated $campaign_type==9) calls find_neighbors then randomly_start_war_peace_essos (243 stmts), a copy of VC's randomly_start_war_peace_new (68% similar) restricted to the Essos faction range; strig:55 (1h) is the Essos twin of strig:54: strig:54 loops fac_kingdom_1..10 (Westeros), strig:55 picks a random faction in fac_kingdom_12..kingdoms_end (Essos) and ticks its truce/casus-belli/war-damage counters. find_neighbors fills faction slots 240+N with 1 when any town pair of the two factions is within 25 map units, so war candidates are limited to geographic neighbours.

- **Hooks:** `strig:53`, `strig:55`
- **Scripts:** `randomly_start_war_peace_essos`, `find_neighbors`
- **Slots:** `faction:240`
- **Globals:** `campaign_type`
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `dis strig:55: random faction in fac_kingdom_12..fac_kingdoms_end (Essos range) vs strig:54 fac_kingdom_1..10`, `similar awoiaf randomly_start_war_peace_essos -> 68% vc randomly_start_war_peace_new`, `dis strig:53: (eq,$campaign_type,9),(call find_neighbors),(call randomly_start_war_peace_essos,1)`, `dis find_neighbors: faction slot 240+i set to 1 for towns < 25 apart`

<a id="awoiafletters-to-lords"></a>
### Personal letters to lords (insult, duel challenge, demands, bribes) carried by a messenger party — awoiaf (`awoiaf.letters_to_lords`)

**What it does:** From a presentation the player composes a letter to any lord: choose a tone (friendly / formal / insulting) and up to several demands - challenge to a duel, meet me at a village, attack a party, accept a bribe, etc. A messenger party physically travels to the lord; on arrival the lord's relation-dependent reaction is applied (he may ride out to fight the player, march to the named place, take the bribe) and a written reply is generated and carried back.

**How it works:** prsnt_compose_message_hero (t1) stores target lord party (slot 309), optional target place (slot 310) and a bitmask of requests (slot 308) on a pt_personal_messenger party and sets $message_tone. strig:35 (every frame) finds an arrived messenger (party_is_in_any_town) and calls personal_messenger: for each set bit it applies change_player_relation_with_troop, describe_player_relations ($fac_relations), and makes the lord's party chase the player (ai behaviour 4 on p_main_party) or move to the target (behaviour 6), or calls bribe_party; failed parts clear the bit. When the messenger meets the player again, game_event_party_encounter -> build_reply assembles the reply from tone x relation x request outcome quick-strings; prsnt_view_message / prsnt_view_reply show the letter. Troop slot 167 stores a 24h 'await' deadline. Separate VC-inherited raven system (prsnt_messenger_system, strig:151) only carries plain orders.

- **Hooks:** `prsnt:compose_message_hero/t1`, `strig:35`, `script:game_event_party_encounter`
- **Scripts:** `personal_messenger`, `build_message_hero`, `build_reply`, `bribe_party`, `describe_player_relations`
- **Menus:** `menu_messenger_return`
- **Presentations:** `prsnt_compose_message_hero`, `prsnt_view_message`, `prsnt_view_reply`
- **Slots:** `party:308`, `party:309`, `party:310`, `troop:167`
- **Globals:** `message_tone`, `fac_relations`, `unable_to_duel`, `unable_to_pay`, `attack_party_answer`, `target1`, `target_2`
- **Module-specific resources:** pt: pt_personal_messenger
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis strig:35 + personal_messenger (bitmask loop over party slot 308, chase/target orders, bribe_party)`, `dis build_reply ($message_tone x $fac_relations reply strings)`, `qstr '_Challenge_{s1}_to_a_duel.', 'Your maester approaches with urgent news: A raven has returned... angered by your insult'`
- **Overlaps:** `acan.conspiracy_treason_trials`, `acw.alliance_blocs`, `ad457.ai_tributary_states_casus_belli`, `ad457.minor_tribes_and_tributaries`, `awoiaf.spy_network_sabotage`, `awoiaf.static_wars_scripted_diplomacy`, `be.infamy_casus_belli_alliances`, `be.peace_negotiations_victory_points`, `bi.diplomacy_suite`, `tld.gift_bribe_courier_quest`

<a id="awoiafspy-network-sabotage"></a>
### Spy network: plant spies in towns, read reports, order sabotage — awoiaf (`awoiaf.spy_network_sabotage`)

**What it does:** The player can plant a spy in any town via the map right-click menu, read periodic spy reports (garrison, prosperity, prisoners, lords present) from Reports, and order the spy to poison the well (wounds the garrison), poison food stores (rats/pox), stir civil unrest (riots, lowered prosperity/recruits), or stand by. Each day the spy risks capture depending on town type, local relation and how long he has been there; capture costs relation with the town and its lord. A spy can also rescue the player from a dungeon.

**How it works:** Context menu (game_context_menu_get_buttons 'Send Spy'/'Retrieve Spy' -> game_event_context_menu_button_clicked) sets party slot 300 (hour planted) on the town and decrements main-party slot 304 (spies available; seeded by set_town_spycount at game_start). prsnt_sabotage writes party slot 301 (1 poison well, 2 poison food, 3 unrest, 4 hold). strig:38 (24h) loops towns: roll = random(5,300) + town relation + faction relation, modified by center type and pending order; <=100 -> spy captured (slots cleared, -10 lord relation, -20 center relation, dialog_box str_spy_captured); else executes order via poison_well (party_wound_members on every garrison stack, -3 prosperity; for type 13 also lowers the lord's attributes), poison_food, unrest_sabotage (sets rioter walkers, cuts volunteers slot 53 / slot 205, -5 prosperity), then update_center_recon_notes. prsnt_spy_reports -> spy_report_info builds the intelligence text. menu_rescue_defeat uses the spy to escape captivity.

- **Hooks:** `strig:38`, `prsnt:spy_reports/t0`, `prsnt:spy_reports/t2`, `prsnt:sabotage/t2`, `script:game_event_context_menu_button_clicked`, `menu:reports/opt:spy_report`
- **Scripts:** `spy_report_info`, `set_town_spycount`, `poison_well`, `poison_food`, `unrest_sabotage`, `update_center_recon_notes`, `get_prosperity_for_spy_report`, `game_context_menu_get_buttons`, `game_event_context_menu_button_clicked`
- **Menus:** `menu_spy_report`, `menu_spy_confirm`, `menu_spy_party`, `menu_spy_sabotage`, `menu_rescue_defeat`
- **Presentations:** `prsnt_spy_reports`, `prsnt_sabotage`
- **Slots:** `party:300`, `party:301`, `party:302`, `party:304`, `party:53`, `party:205`
- **Globals:** `spy_target`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis strig:38 (capture roll, order dispatch to poison_well/poison_food/unrest_sabotage)`, `slot awoiaf party 300/301/304 writers: context-menu click handler, set_town_spycount, prsnt:sabotage/t2`, `roots spy_report_info -> prsnt:spy_reports/t2; qstr 'Send_Spy', 'Retrieve_Spy', 'Your_spy_in_{s5}_has_successfully_poisoned_the_well.'`, `dis poison_well: party_wound_members per stack, change_center_prosperity -3`
- **Overlaps:** `acan.conspiracy_treason_trials`, `acw.alliance_blocs`, `ad457.ai_tributary_states_casus_belli`, `ad457.minor_tribes_and_tributaries`, `awoiaf.letters_to_lords`, `awoiaf.static_wars_scripted_diplomacy`, `be.infamy_casus_belli_alliances`, `be.peace_negotiations_victory_points`, `bi.diplomacy_suite`, `tld.gift_bribe_courier_quest`

<a id="awoiafstatic-wars-scripted-diplomacy"></a>
### Static Wars: canon-locked diplomacy with scripted war declarations — awoiaf (`awoiaf.static_wars_scripted_diplomacy`)

**What it does:** In Static Wars mode the AI's free war/peace decisions are switched off and wars start on a scripted timeline that follows the War of the Five Kings (Westerlands attack the Riverlands ~day 50, Ironborn raid the North, Dragonstone vs Westerlands, Riverrun falls, etc.), each announced by a raven-letter menu. The player can later switch to sandbox.

**How it works:** Native's daily/hourly war-peace drivers are gated on $campaign_type==9 (strig:52 find_neighbors+randomly_start_war_peace_new, strig:54/55 truce & casus-belli counters on faction slots 120+/160+/200+, strig:64 lord politics). With $campaign_type==8, one-shot triggers (trig:36..40, rearm 1e8 = fire once) test day + faction-alive (faction slot 21 = state) and call diplomacy_start_war_between_kingdoms + set_relation, then jump_to_menu menu_westerlands_start_war_riverlands / menu_ironborn_start_war_north / menu_dragonstone_start_war_westerlands / menu_riverrun_taken_by_westerlands; strig:56 keeps kingdom_11 at war with whoever holds town_8.

- **Hooks:** `strig:52`, `strig:54`, `strig:55`, `strig:56`, `trig:36:cond`, `trig:37:cond`, `trig:38:cond`, `trig:39:cond`, `trig:40:cond`
- **Scripts:** `diplomacy_start_war_between_kingdoms`, `randomly_start_war_peace_new`, `find_neighbors`, `update_faction_notes`
- **Menus:** `menu_westerlands_start_war_riverlands`, `menu_ironborn_start_war_north`, `menu_dragonstone_start_war_westerlands`, `menu_westerlands_start_peace_reach`, `menu_riverrun_taken_by_westerlands`, `menu_static_wars_off_menu`
- **Slots:** `faction:21`, `faction:120`, `faction:160`, `faction:200`, `faction:240`
- **Globals:** `campaign_type`, `riverrun_taken_by_westerlands`
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `dis strig:52/53: (eq,$campaign_type,9) gate before find_neighbors + randomly_start_war_peace_new/_essos`, `dis trig:37: cond day>=50 and factions 18 & 5 alive; conseq diplomacy_start_war_between_kingdoms(18,5) + jump_to_menu westerlands_start_war_riverlands`, `dis trig:36, strig:56 gated on $campaign_type==8`, `menu texts: menu:ironborn_start_war_north 'Lord Balon Greyjoy has crowned himself... raiding parties to attack the northern coasts'`
- **Overlaps:** `acan.conspiracy_treason_trials`, `acw.alliance_blocs`, `ad457.ai_tributary_states_casus_belli`, `ad457.minor_tribes_and_tributaries`, `awoiaf.letters_to_lords`, `awoiaf.spy_network_sabotage`, `be.infamy_casus_belli_alliances`, `be.peace_negotiations_victory_points`, `bi.diplomacy_suite`, `tld.gift_bribe_courier_quest`

<a id="beinfamy-casus-belli-alliances"></a>
### Infamy, casus belli and alliance call-to-arms diplomacy — be (`be.infamy_casus_belli_alliances`)

**What it does:** Each nation has Infamy (0-150, 'badboy'): declaring war without a claim, breaking alliances or going bankrupt raises it; it decays by 1 every 3 days. Neighbouring nations randomly fabricate casus belli against each other (more readily against infamous targets). Allies are asked to join wars; an ally that refuses breaks the alliance and gains infamy; the player gets a menu to accept or decline. High infamy triggers a world-weariness notification.

**How it works:** faction slot 450 = infamy, changed only through faction_change_infamy (clamp 0..150, message for player nation). strig:118 (72 h) -1 to all. strig:136 (24 h) +1 to the player's nation while treasury slot 802 < 0. diplomacy_start_war_between_kingdoms (modified Native, 131 vs 86 stmts) adds +20/+30 infamy depending on the controversial-policy branch (no casus belli). strig:116 (async) calls create_random_provocation: random land-bordering pair at peace, chance (target infamy+30) x aggressor slot 499 /1400 -> casus belli stored in faction slot 160+target (10-20 days), relations reset to 0, aggressor +10-infamy, player gets menu_provocation_created1-4. strig:120 (0.1 h, one faction per tick): for each ally at war, cf_if_faction_decides_to_support_ally_against_enemy (base 125 +- power difference/3 + relation terms + infamy terms) x faction slot 500 >= 100 -> join war (casus belli slot 160+enemy set, war flag 455+enemy=500) else break_alliance_between_factions and infamy 15 - (ally infamy/2); for the player -> menu_alliance_support_ally_in_war. create_random_alliance / create_alliance_between_factions / break_alliance_between_factions; cf_if_faction_is_in_alliance_with_faction.

- **Hooks:** `strig:116`, `strig:118`, `strig:120`, `strig:136`, `menu:alliance_support_ally_in_war`, `menu:provocation_created1`, `menu:high_infamy_notification`, `menu:create_alliance`
- **Scripts:** `faction_change_infamy`, `create_random_provocation`, `create_random_alliance`, `create_alliance_between_factions`, `break_alliance_between_factions`, `cf_if_faction_decides_to_support_ally_against_enemy`, `cf_if_faction_is_in_alliance_with_faction`, `create_random_war_peace`, `create_random_relation_increasing`, `faction_calculate_power`, `cf_if_faction_borders_a_faction_by_land`, `diplomacy_start_war_between_kingdoms`
- **Menus:** `menu_alliance_support_ally_in_war`, `menu_provocation_created1`, `menu_provocation_created2`, `menu_provocation_created3`, `menu_provocation_created4`, `menu_high_infamy_notification`, `menu_long_war_notification`, `menu_create_alliance`, `menu_create_alliance2`
- **Slots:** `faction:450`, `faction:499`, `faction:500`, `faction:160+N (casus belli vs faction N)`, `faction:455+N (war-support flag)`, `faction:802`
- **Globals:** `war_supports_allies`, `create_alliance_chosen_faction`, `break_alliance_choosen_faction`, `create_casus_belli_chosen_faction`, `declare_war_chosen_faction`, `improve_relations_chosen_faction`
- **Module-specific resources:** quest: qst_cause_provocation
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis be faction_change_infamy, strig:118, strig:120, strig:136, create_random_provocation, cf_if_faction_decides_to_support_ally_against_enemy`, `text be 'infamy': faction note, peace negotiations, alliance menus, high-infamy menu`
- **Overlaps:** `acan.conspiracy_treason_trials`, `acw.alliance_blocs`, `ad457.ai_tributary_states_casus_belli`, `ad457.minor_tribes_and_tributaries`, `awoiaf.letters_to_lords`, `awoiaf.spy_network_sabotage`, `awoiaf.static_wars_scripted_diplomacy`, `be.peace_negotiations_victory_points`, `bi.diplomacy_suite`, `tld.gift_bribe_courier_quest`

<a id="bepeace-negotiations-victory-points"></a>
### Peace conference with victory points, territory and reparations — be (`be.peace_negotiations_victory_points`)

**What it does:** Instead of a yes/no peace offer, the player opens a peace conference screen: battles and captures during the war accumulate victory points per side (including allies); the player ticks which towns/castles change hands and sets reparations, the infamy cost of the demands is shown, and the enemy's diplomats accept or refuse ('cannot agree with terms') depending on whether the VP balance covers the demands.

**How it works:** prsnt_peace_negotiations (t0 load 184 stmts, t1 events): peace_negotiations_detect_allies_and_enemies fills trp_temp_array_c/d; peace_negotiations_calculate_victory_points sums faction slot 200+opponent for each side and allies (halved for Prussian unification quest targets); centres listed through cf_peace_negotiations_if_center_can_appear_in_the_list / _is_of_allies / _is_of_enemies and peace_negotiations_add_center (checkboxes); peace_negotiations_calculate_infamy_cost; peace_negotiations_enemy_rethink; on Make Peace, peace_negotiations_set_center_owners_to_official_for_factions transfers centres (party slot 144 = official owner) and applies reparations. Opened from menus 'menu_peace_negotiations_initial'.

- **Hooks:** `prsnt:peace_negotiations/t0`, `prsnt:peace_negotiations/t1`, `menu:peace_negotiations_initial`
- **Scripts:** `peace_negotiations_detect_allies_and_enemies`, `peace_negotiations_calculate_victory_points`, `peace_negotiations_calculate_infamy_cost`, `peace_negotiations_add_center`, `peace_negotiations_enemy_rethink`, `peace_negotiations_set_center_owners_to_official_for_factions`, `cf_peace_negotiations_if_center_can_appear_in_the_list`, `cf_peace_negotiations_if_center_is_of_allies`, `cf_peace_negotiations_if_center_is_of_enemies`, `cf_peace_negotiations_if_faction_is_ally`, `cf_peace_negotiations_if_faction_is_enemy`, `faction_calculate_victory_points_against_faction`, `faction_calculate_victory_points_against_itself`
- **Menus:** `menu_peace_negotiations_initial`
- **Presentations:** `prsnt_peace_negotiations`
- **Slots:** `faction:200+N (victory points vs N)`, `faction:447`, `party:144`, `party:145`, `party:147`
- **Globals:** `peace_negotiations_enemy_faction`, `peace_negotiations_ai_offer`, `number_of_allies`, `number_of_enemies`, `peace_negotiations_infamy_cost`
- **Module-specific resources:** mesh: mesh_checkbox_on, mesh_checkbox_off, mesh_menu_flag1, mesh_menu_flag2; quest: qst_prussia_unification_defeat_austria, qst_prussia_unification_defeat_france
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `explain be prsnt:peace_negotiations/t0: texts 'Victory_Points:_{reg20}/{reg10}', 'War_reparations_amount', 'Opposite_side_diplomats cannot agree with terms', 'Infamy_penalty'`, `dis be peace_negotiations_calculate_victory_points`, `writers of faction 200+N (battle results) not traced`
- **Overlaps:** `acan.conspiracy_treason_trials`, `acw.alliance_blocs`, `ad457.ai_tributary_states_casus_belli`, `ad457.minor_tribes_and_tributaries`, `awoiaf.letters_to_lords`, `awoiaf.spy_network_sabotage`, `awoiaf.static_wars_scripted_diplomacy`, `be.infamy_casus_belli_alliances`, `bi.diplomacy_suite`, `tld.gift_bribe_courier_quest`

<a id="bidiplomacy-suite"></a>
### Diplomacy mod (treaties, ministers, patrols, policies, gifts) — bi (`bi.diplomacy_suite`)

**What it does:** BI ships the Diplomacy package: alliances/defensive/trade/non-aggression treaties, chamberlain/constable/chancellor, patrols, scouts, messengers, gifts, domestic policy (centralisation, serfdom, economy) and the advanced preferences screen.

**How it works:** dplmc_* scripts, menus (dplmc_question_*_offer, dplmc_notification_*), prsnt:dplmc_policy_management, prsnt:adv_diplomacy_preferences, weekly/monthly strig:106/108/111/113/114/115 (lord exile return, patrol upkeep, policy drift).

- **Hooks:** `strig:106`, `strig:108`, `strig:111`, `strig:113`, `strig:114`, `strig:115`
- **Scripts:** `dplmc_send_patrol`, `dplmc_send_gift`, `dplmc_start_alliance_between_kingdoms`, `dplmc_lord_return_from_exile`, `dplmc_get_troop_standing_in_faction`
- **Menus:** `menu_dplmc_preferences`, `menu_dplmc_domestic_policy`
- **Presentations:** `prsnt_dplmc_policy_management`, `prsnt_adv_diplomacy_preferences`
- **Slots:** `faction:200`, `faction:201`, `faction:202`, `faction:203`, `faction:204`, `faction:205`, `faction:206`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Overlaps:** `acan.conspiracy_treason_trials`, `acw.alliance_blocs`, `ad457.ai_tributary_states_casus_belli`, `ad457.minor_tribes_and_tributaries`, `awoiaf.letters_to_lords`, `awoiaf.spy_network_sabotage`, `awoiaf.static_wars_scripted_diplomacy`, `be.infamy_casus_belli_alliances`, `be.peace_negotiations_victory_points`, `tld.gift_bribe_courier_quest`

<a id="tldgift-bribe-courier-quest"></a>
### Send gifts or bribes to another faction's ruler (RP courier quest) — tld (`tld.gift_bribe_courier_quest`)

**What it does:** A lord can be asked to send a gift (good factions) or bribe (evil ones) to another faction's leader. The player pays Resource Points up front, carries the gift personally, and on delivery the recipient faction credits the same RP to the player's account there and its ruler's relation with the player rises -- effectively a way to move wealth between factions while building friendships.

**How it works:** dlg:581-592: choose recipient faction and one of five gift tiers (cost 1000 + 1000*tier^2 RP, text str_<faction>_gift0..4); conseq deducts with add_faction_rps and starts quest 39 storing giver, recipient faction, value and gift string. dlg:579/580 at the recipient's ruler: finish_quest, add_faction_rps(recipient, value), change_player_relation_with_troop(ruler, value/2000 + 2).

- **Hooks:** `dlg:581:dlga_lord_talk:send_gift_1:cond`, `dlg:579:dlga_lord_talk:deliver_gift_1:cond`
- **Scripts:** `add_faction_rps`, `update_respoint`, `start_quest`, `finish_quest`, `change_player_relation_with_troop`
- **Dialogs:** `dlg:581:dlga_lord_talk:send_gift_1:cond`, `dlg:590:dlga_send_gift_4:send_gift_5:cond`, `dlg:592:dlga_send_gift_5:lord_pretalk:conseq`, `dlg:580:dlga_deliver_gift_1:lord_pretalk:cond`
- **Slots:** `quest:3`, `quest:6`, `quest:10`, `quest:14`, `quest:15`, `quest:22`, `faction:72`
- **Globals:** `temp`, `temp_2`
- **Module-specific resources:** quest: quest 39 (gift); string: str_gondor_gift0 .. per-faction gift names
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis tld dlg:592 conseq (cost formula, quest 39 slots, add_faction_rps negative)`, `dis tld dlg:580 cond (finish_quest, add_faction_rps recipient, relation +value/2000+2)`
- **Overlaps:** `acan.conspiracy_treason_trials`, `acw.alliance_blocs`, `ad457.ai_tributary_states_casus_belli`, `ad457.minor_tribes_and_tributaries`, `awoiaf.letters_to_lords`, `awoiaf.spy_network_sabotage`, `awoiaf.static_wars_scripted_diplomacy`, `be.infamy_casus_belli_alliances`, `be.peace_negotiations_victory_points`, `bi.diplomacy_suite`

<a id="vcfaction-restoration-and-adventurers"></a>
### Defeated kingdoms can be reborn; their landless lords roam as 'adventurers' — vc (`vc.faction_restoration_and_adventurers`)

**What it does:** When a kingdom is destroyed its lords do not just vanish: they become adventurers who roam, sell prisoners and seek service, and may defect into other kingdoms. Over time, rumours of rebellion grow and a destroyed kingdom can rise again by retaking a walled center, with its old king and supporting lords rejoining (about one restoration a month late in the game).

**How it works:** fac_adventurers (referenced in 39 blocks: party_get_ideal_size, calculate_troop_ai, npc_decision_checklist_party_ai, process_village_raids, spawn_bandits, strig:22/32/47/49...) is the holding faction for lords of defeated factions. strig:109 (every 0.05h) drives adventurer parties: wander near towns (patrol radius 35), sell prisoners via sell_prisoners, or hole up in their faction's center. strig:154 (every 30h): if the player's leadership + charisma/2 roll fails, picks a random defeated kingdom (faction slot 21 set, ruler troop without a party), counts its former lords now serving elsewhere and their fiefs, drops their relation with their current liege (-30) and posts '(Possible Rebellion) Rumors...' messages that escalate; on success the faction is restored (menu_notification_kingdom_reborn, change_troop_faction for leader + supporters). trig:51 (60h) handles center restoration (menu_notification_center_restoration, give_center_to_faction). Modified lord_find_alternative_faction / strig:49 run defections, now preferring culture and liege relation.

- **Hooks:** `strig:154`, `strig:109`, `trig:51:conseq`, `strig:49`
- **Scripts:** `sell_prisoners`, `change_troop_faction`, `lord_find_alternative_faction`, `troop_get_relation_with_troop`, `add_notification_menu`, `give_center_to_faction`
- **Menus:** `menu_notification_kingdom_reborn`, `menu_notification_center_restoration`, `menu_notification_lord_defects`
- **Slots:** `faction:21`, `troop:8`, `troop:14`, `party:7`
- **Module-specific resources:** faction: fac_adventurers
- **Relation to Native:** modifies-native
- **Confidence:** strongly-inferred
- **Evidence:** `dis vc strig:154: leadership/charisma gate, defeated faction pick, lords of that faction elsewhere, -30 liege relation, 'Possible Rebellion' messages, menu_notification_kingdom_reborn`, `dis vc strig:109: fac_adventurers lord parties, sell_prisoners in towns, patrol behaviour`, `sqlite refs fac_adventurers: 39 blocks`, `Changelog 2.025 FACTION RESTORATION section (one faction at a time, ~1/month, escalating rumours, supporting lords)`
- **Overlaps:** `acan.civil_war_usurpation_restoration`, `ad457.landless_faction_cleanup`, `ad457.town_rebellions_secession`, `tld.faction_defeat_redistribution_last_stand`

<a id="ad457lord-business-build-hire-upgrade"></a>
### AI lords spend their wealth: build in fiefs, hire mercenaries, upgrade their own gear — ad457 (`ad457.lord_business_build_hire_upgrade`)

**What it does:** When a lord visits his own town or castle he collects its accumulated rents and tariffs, and if he is rich (over 10,000) he commissions a building there himself. In towns and castles he can also hire the local mercenary stack for cash, and he trades his weapons/armour for better-quality versions (better item modifiers) at the town armourer, capped by an equipment budget that depends on his personality and his kingdom's policy.

**How it works:** troop_does_business_in_center (323 stmts; Native 52) runs whenever a lord is in a centre. Owner visit: adds party slots 47+48 (accumulated rents/tariffs) to troop wealth slot 11 and zeroes them. If $g_dplmc_ai_changes>=1, wealth >10000 and a build queue (162 or 164) is free: picks a random building id (128-145 for villages, 140-156 for towns/castles), filters by preconditions (e.g. 146/134 need the lord's culture != centre culture, 128 silver mine needs party 241, 133/138 need party 239), prices it with get_improvement_details scaled by faction slot 303 and the lord's Engineer skill (and prisoners as labour), deducts gold and calls improve_center. Villages: adds the village's queued recruits (party 88/89) to his party. Towns/castles: may hire mercenaries from party slots 90/91 using game_get_join_cost, budget = wealth/(faction slot 304 + 10). Then calculate_equipment_limit (3000, halved for reputation types 1-2, -1000 for type 8, -100 x faction slot 302) caps spending while it swaps each equipped item for a better-modifier copy in the town's armourer/weaponsmith/horse-merchant (party 21/22/24) paying the value difference, and finally fixes troop class (horse -> cavalry, ranged weapon -> archer).

- **Hooks:** `script:troop_does_business_in_center`
- **Scripts:** `troop_does_business_in_center`, `calculate_equipment_limit`, `improve_center`, `get_improvement_details`, `game_get_join_cost`, `dplmc_get_item_value_with_imod`, `dplmc_troop_can_use_item`
- **Slots:** `troop:11`, `troop:52`, `party:47`, `party:48`, `party:88`, `party:89`, `party:90`, `party:91`, `party:162`, `party:164`, `faction:302`, `faction:303`, `faction:304`
- **Globals:** `g_dplmc_ai_changes`, `g_improvement_type`, `cheat_mode`
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `dis ad457 troop_does_business_in_center stmts 31-130: rent collection, wealth>10000 build choice, improve_center call, log line '{s10} constructs a {...}'`, `dis ad457 troop_does_business_in_center stmts 169-215: mercenary hire from party 90/91, log '{s10} hires {reg2} {...}'`, `dis ad457 troop_does_business_in_center stmts 216-274 + dis calculate_equipment_limit: modifier swap with town merchants, log '{s10} upgrades {s3}{...}'`
- **Overlaps:** `acan.culture_specific_fief_buildings`, `acan.latifundium_estates`, `ad457.center_buildings_management`, `bi.ai_lords_build`, `bi.garrison_building_battle_bonuses`, `bi.roman_public_buildings`, `pop.fief_base_income_and_reports`, `pop.fief_heartbeat_problems`, `pop.fief_improvements_expanded`, `pop.fief_stewards_with_skills`, `sw.recruit_unlock_buildings`, `vc.extended_center_improvements`

<a id="awoiaflord-retinue-heroes"></a>
### Named retainers riding in lords' armies — awoiaf (`awoiaf.lord_retinue_heroes`)

**What it does:** Notable non-lord characters (e.g. Sandor Clegane with his liege, Brax and Crakehall knights) are added as hero troops to specific lords' parties whenever those parties are (re)created, so they appear and fight in that lord's army; story events can remove them.

**How it works:** Modified Native create_kingdom_hero_party: after hire_men_to_kingdom_hero_party, an if-chain keyed on the leader troop calls give_companion_to_lord(hero, $pout_party) (145 call sites) which adds the hero only if alive (troop slot 2 != 1), not leading a party (slot 8 < 1) and not already present. remove_companion_from_lord is used by the Hound event menus. Also called from game_start, strig:80 and the invasion triggers trig:101/102.

- **Hooks:** `script:create_kingdom_hero_party`, `strig:80`
- **Scripts:** `give_companion_to_lord`, `remove_companion_from_lord`, `create_kingdom_hero_party`
- **Slots:** `troop:2`, `troop:8`
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `callers give_companion_to_lord: 145 sites, mostly create_kingdom_hero_party`, `dis create_kingdom_hero_party stmt 43-57 (knight_18_1 -> trp_sandor_clegane ...)`, `dis give_companion_to_lord (alive / not leading / not present guard)`, `callers remove_companion_from_lord: menu:the_hound_event_*`
- **Overlaps:** `acw.lord_army_size_and_wages`, `laigle.lord_army_doctrine`

<a id="biai-lords-build"></a>
### AI lords build improvements in their fiefs — bi (`bi.ai_lords_build`)

**What it does:** AI lords spend their personal wealth to construct buildings in the fiefs they own, so NPC territory develops over time like the player's. Fiefs also start the game with buildings allocated from a wealth budget.

**How it works:** Native troop_does_business_in_center (lord visits his fief) now calls npc_upgrade_buildings(lord, center): wealth threshold depends on lord reputation type (troop slot 52); if lord wealth (troop slot 11) exceeds it and nothing is under construction (party slot 124), picks a random free building slot 130-154 (towns: 137+, Roman-only 148+ via cf_center_is_roman), computes build days from cost, lord engineer skill x intelligence, level and the center's prosperity, deducts the cost and calls improve_center. Player is told '{s10} constructs a {s0} in {s4}, finish in {reg0} days' for lords of their kingdom. game_start calls allocate_buildings to seed buildings.

- **Hooks:** `script:troop_does_business_in_center`, `script:game_start`
- **Scripts:** `npc_upgrade_buildings`, `improve_center`, `allocate_buildings`, `get_improvement_details`, `cf_center_is_roman`, `troop_does_business_in_center`
- **Slots:** `troop:11`, `troop:52`, `party:124`, `party:125`, `party:50`
- **Globals:** `g_improvement_type`
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `explain bi npc_upgrade_buildings: caller troop_does_business_in_center, displayed text '{s10}_constructs_a_{s0}_in_{s4},_finish_in_{reg0}_days'`, `dis bi npc_upgrade_buildings (random slot 130-155, cost/time formula)`, `explain bi allocate_buildings: caller game_start, text '{s51} allocated {reg0} wealth for buildings'`
- **Overlaps:** `acan.culture_specific_fief_buildings`, `acan.latifundium_estates`, `ad457.center_buildings_management`, `ad457.lord_business_build_hire_upgrade`, `bi.garrison_building_battle_bonuses`, `bi.roman_public_buildings`, `pop.fief_base_income_and_reports`, `pop.fief_heartbeat_problems`, `pop.fief_improvements_expanded`, `pop.fief_stewards_with_skills`, `sw.recruit_unlock_buildings`, `vc.extended_center_improvements`

<a id="laiglelord-army-doctrine"></a>
### Per-lord army doctrine for reinforcements — laigle (`laigle.lord_army_doctrine`)

**What it does:** Every lord is assigned one of five doctrines at game start (e.g. line, light, guard, cavalry-heavy). When his party reinforces it draws from that doctrine's three party templates instead of the faction's generic ones, so different lords field visibly different armies.

**How it works:** game_start writes troop slot 352 = 1..5 on ~140 lords. initialize_faction_troop_types (234 stmts vs Native 74) fills faction slots 77-79 (doctrine 1, Native reinforcement slots) and 100-111 (doctrines 2-5, three templates each). cf_reinforce_party: for a lord party (party slot 0 == 13) reads the leader's troop slot 352 and picks the matching faction-slot triple; garrisons (party type 2/3) keep 77-79.

- **Hooks:** `strig:22`, `script:game_start`
- **Scripts:** `cf_reinforce_party`, `initialize_faction_troop_types`, `game_start`
- **Slots:** `troop:352`, `faction:77`, `faction:78`, `faction:79`, `faction:100`, `faction:101`, `faction:102`, `faction:103`, `faction:104`, `faction:105`, `faction:106`, `faction:107`, `faction:108`, `faction:109`, `faction:110`, `faction:111`
- **Module-specific resources:** pt: per-faction doctrine party templates (faction slots 100-111)
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `slot laigle troop 352: written 140x in game_start (values 1-5), read in cf_reinforce_party`, `slot laigle faction 103: written in initialize_faction_troop_types (pt), read in cf_reinforce_party`, `dis laigle cf_reinforce_party stmts 18-53`
- **Overlaps:** `acw.lord_army_size_and_wages`, `awoiaf.lord_retinue_heroes`

<a id="tldlord-friendship-gifts"></a>
### Friendly lords periodically offer troops or equipment — tld (`tld.lord_friendship_gifts`)

**What it does:** Lords who like the player (relation 20+) slowly build up goodwill and, when it is ready, offer a gift when the player next talks to them -- either a group of their troops or a piece of equipment matched to the player, with quality scaled by the friendship.

**How it works:** strig:8 (daily) loops kingdom heroes (troop slot 2 == 2) and calls lord_friendship_reward_progress(lord, relation/20); the script adds to troop slot 167 (progress) and, if no offer is pending (slot 166 < 1), randomly picks troops (lord_reward_troops_type: chooses a troop type and count from the lord's party/faction) or equipment (lord_reward_equipment_type, item type by player's equipment, lord_reward_equipment_modifier for quality), storing the offer in slots 166/168. Dialogs dlg:811 (lord_offer_troops: 'I have N X who are prepared...') and dlg:814 (lord_offer_item) present the offer once progress reaches 100 and reset it. change_player_relation_with_troop also feeds progress.

- **Hooks:** `strig:8`, `dlg:811:dlga_lord_leave:lord_offer_troops:cond`, `dlg:814:dlga_lord_leave:lord_offer_item:cond`
- **Scripts:** `lord_friendship_reward_progress`, `lord_reward_troops_type`, `lord_reward_troops_count`, `lord_reward_equipment_type`, `lord_reward_equipment_modifier`, `troop_get_player_relation`, `change_player_relation_with_troop`
- **Dialogs:** `dlg:811:dlga_lord_leave:lord_offer_troops:cond`, `dlg:814:dlga_lord_leave:lord_offer_item:cond`, `dlg:459:dlga_lord_talk:lord_pretalk.1:cond`
- **Slots:** `troop:166`, `troop:167`, `troop:168`, `troop:165`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `dis tld lord_friendship_reward_progress (slots 166/167/168; random troops vs equipment)`, `dis tld strig:8 (relation >= 20 -> progress)`, `slot tld troop 167: readers dlg:811 / dlg:814 (const 100 threshold)`
- **Overlaps:** `awoiaf.commoner_trust`, `bi.triumphus`, `pop.post_battle_lord_relation_gain`

<a id="tldstrength-scaled-hosts-and-patrols"></a>
### Lords alternate between small patrols and full Hosts, with the number of Hosts set by faction strength — tld (`tld.strength_scaled_hosts_and_patrols`)

**What it does:** Idle lords do not all roam with full armies. Each faction may field only as many big 'Hosts' as its Strength allows (roughly one per 1000 strength, minus the marshal's own); other lords go out as small 'X's patrol' guarding their home or capital. When a lord switches role his party is renamed, refilled with recruits and upgraded according to his Trainer skill, so a strong faction visibly fields more and bigger armies than a weakened one.

**How it works:** decide_kingdom_party_ais (strig:21 every 3 h, and recalculate_ais) first applies the faction-wide AI state (faction slot 4: 1 gather at advance camp, 2 siege, 4/5 raid/attack) to the marshal (faction slot 7). It counts current hosts per faction in faction slot 152 (party slot 0 == 13 = host). For each lord whose party is in 'patrol' state (party slot 0 == 14) it computes allowed hosts = strength/1000 (or /700 for two factions under 4500) + 1, minus the marshal's host; if under the cap (or the lord is the marshal, on a personal oath quest, or flagged in troop slot 172) there is a 10% chance per run to become a host: party_set_name 'X's Host', party slot 0 = 13, slot 1 (strength value) = 80 or 160 for the marshal, 30-50 hire_men_to_kingdom_hero_party rounds and 2-8 + Trainer+5 upgrade_hero_party rounds; otherwise patrol: name 'X's patrol', slot 1 = 50, 15 hires, patrol radius 5 around its fief or capital. Then calculate_troop_ai / calculate_troop_ai_under_command for every lord.

- **Hooks:** `strig:21`, `script:recalculate_ais`
- **Scripts:** `decide_kingdom_party_ais`, `init_ai_calculation`, `calculate_troop_ai`, `calculate_troop_ai_under_command`, `kingdom_hero_decide_next_ai_state`, `hire_men_to_kingdom_hero_party`, `upgrade_hero_party`, `party_set_ai_state`
- **Slots:** `faction:4`, `faction:5`, `faction:7`, `faction:150`, `faction:152`, `party:0`, `party:1`, `party:4`, `party:123`, `troop:10`, `troop:59`, `troop:172`
- **Globals:** `tld_war_began`, `tld_host_size_multi`, `g_fac_str_siegable`
- **Module-specific resources:** string: str_s5_s_host, qstr_{s5}_s_patrol
- **Relation to Native:** modifies-native
- **Confidence:** strongly-inferred
- **Evidence:** `dis tld decide_kingdom_party_ais stmts 39-151 (faction slot 152 host count, strength/1000 cap, renames to Host/patrol, hire/upgrade loops)`, `explain tld decide_kingdom_party_ais: callers strig:21, recalculate_ais`
- **Overlaps:** `pop.order_chapter_knight_patrols`, `pop.sheriff_militia_patrols`, `sw.faction_town_patrols`

<a id="acwlord-army-size-and-wages"></a>
### Lord army size from leadership, renown, rank and fiefs; per-faction level-bracket wages — acw (`acw.lord_army_size_and_wages`)

**What it does:** AI lords' ideal army size is rebuilt: base 120 plus 15 per Leadership point, Charisma, renown/9, a ruler bonus, +50 for the marshal and +70 per town / +50 per castle-or-village owned, capped at 350 and scaled up with the player's level, with a few hand-tuned exceptions. Troop wages are set per faction by level bracket.

**How it works:** party_get_ideal_size (122 vs Native 34 stmts): as summarised; additionally a center that is one of its faction's last two gets +100 garrison; final * (80 + player level)/80; per-lord overrides (e.g. trp_knight_1_17 = 70). game_get_troop_wage (162 vs 43): explicit tables per kingdom (levels 1-21 -> 26, 22-24 -> 40, 28 -> 230 ...).

- **Hooks:** `script:party_get_ideal_size`, `script:game_get_troop_wage`
- **Scripts:** `party_get_ideal_size`, `game_get_troop_wage`
- **Slots:** `party:0`, `party:7`, `troop:7`, `faction:8`, `faction:11`, `faction:81`, `faction:82`
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `dis acw party_get_ideal_size (first 70 stmts)`, `dis acw game_get_troop_wage (first 30 stmts)`, `auto report Modified Native scripts`, `_module_system_source/README.txt item 3; dev docs/unit levels.txt`
- **Overlaps:** `awoiaf.lord_retinue_heroes`, `laigle.lord_army_doctrine`

<a id="acanimperial-treasury-budget"></a>
### Faction treasuries with a weekly budget: income/spending categories, corruption, tax fraud, embezzlement trials — acan (`acan.imperial_treasury_budget`)

**What it does:** Every kingdom keeps a real treasury that is refilled and drained weekly by categorised income (taxes, edict taxes, tributes) and spending (army upkeep, cohort refills, salaries, subsidies). Corruption skims a share of income. A ruler-player can read an imperial budget report, pay into or take from the treasury, and risk an embezzlement trial if they take too much.

**How it works:** add_to_faction_bugdet(category_slot, faction, amount) (62 callers) adds an amount to a category slot on the faction. Weekly netting (below) shows faction slots 270-274 are the income buckets and 262-269 the spending buckets. When the player is the ruler, positive postings to 270/271/273 are boosted, and negative postings to 266/267 shrunk, by household quality (get_household_modifier). trig:5 (weekly) runs weekly_imperial_balance, which sums and clears 262-269 (spending) and 270-274 (income). It handles slot 275 (the ruler's pay or draw, sign convention not resolved): it pays the ruler via add_to_troop_wealth, or event_player_takes_money_imperial_treasury when the ruler is the player, and adds it to the income side. It adds a corruption share of income (calculate_imperial_corruption: a percentage that a census ($conducted_census), extra tax collectors ($control_tax) and minister/chamberlain household quality reduce) plus 4% of faction slot 43 to the spending side, and books net = income + slot 275 - spending through add_to_faction_treasury (faction slots 43/44). calculate_bureaucratic_costs and calculate_edict_tax are posted from calculate_weekly_rents (strig:53/196). prsnt:imperial_budget_report and prsnt:budget_report draw the report (generate_imperial_bugdet_report, 427 stmts). The player-ruler can pay into or withdraw from the treasury (dlg:4620 imperial_treasury_action_take_money). Taking money raises suspicion, which leads to menu:caught_embezzle_punished and trial dialogs (trial_guilty -> remove_office_from_troop). calculate_staff_salary itemises minister, praefectus urbani and tax-collector salaries.

- **Hooks:** `trig:5:conseq`, `prsnt:imperial_budget_report/t0`, `prsnt:budget_report/t0`, `strig:53`, `strig:196`, `dlg:4620:dlga_imperial_treasury_action_take_money_3`, `menu:caught_embezzle_punished`
- **Scripts:** `add_to_faction_bugdet`, `add_to_faction_treasury`, `weekly_imperial_balance`, `calculate_imperial_corruption`, `calculate_bureaucratic_costs`, `calculate_edict_tax`, `generate_imperial_bugdet_report`, `event_player_takes_money_imperial_treasury`, `calculate_staff_salary`, `get_household_modifier`, `print_cost_distribution_to_s10`
- **Menus:** `menu_caught_embezzle_punished`, `menu_inspect_treasury`
- **Presentations:** `prsnt_imperial_budget_report`, `prsnt_budget_report`
- **Slots:** `faction:262`, `faction:263`, `faction:264`, `faction:265`, `faction:266`, `faction:267`, `faction:268`, `faction:269`, `faction:270`, `faction:271`, `faction:272`, `faction:273`, `faction:274`, `faction:275`, `faction:43`, `faction:44`, `faction:10`, `faction:225`
- **Globals:** `conducted_census`, `control_tax`, `g_player_chamberlain`, `g_player_minister`, `g_is_emperor`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis acan weekly_imperial_balance: sums/clears faction 262-269 (:l1, spending side) and 270-274 (:l4, income side); corruption % of :l4 added to :l1; :l4 += slot 275; :l4 -= :l1; add_to_faction_treasury(:l4)`, `explain acan calculate_imperial_corruption: reads conducted_census, control_tax, g_player_minister/chamberlain`, `explain acan add_to_faction_treasury: '{reg0} denarii have been added to/taken from the imperial treasury'`, `text 'Edict': str_faction_taxes_edicts / str_faction_spending_edicts budget lines`, `dis acan add_to_faction_bugdet: faction_set_slot(category) += amount; household bonus on positive 270/271/273 and on negative 266/267 when the player rules`
- **Overlaps:** `acan.senate_influence_edicts`, `acan.town_decrees`, `ad457.dplmc4_tax_inefficiency_and_extras`, `be.pps_political_simulation`

<a id="acanlatifundium-estates"></a>
### Private estates (latifundia) on the map with production buildings, slave labour and weekly rents — acan (`acan.latifundium_estates`)

**What it does:** The player can acquire land next to a village; it appears on the campaign map as their estate. There they build production works (vineyard and winepress, olive grove and oil press, silk and velvet, and more), assign slaves as labour, and draw weekly rent. Fires and other events can damage it, and how slaves are treated matters.

**How it works:** A village-elder dialog (dlg:8881 barb_estate_talk_3 / dlg:8904 lad_talk3) calls spawn_latifundium, which spawns a map party ('Latifundia/Estate near {s0}') via spawn_party and stores its buildings in party slots 214-243. get_building_details_lat gives each building's name, cost, build time and product. Weekly calculate_weekly_rents (strig:53 / strig:196) calls calculate_latifundium_rents (210 stmts): output per building x labour (get_labour_slave_skill_modifier on the slave troops present), times the event modifier (get_event_details, e.g. fire), honour (get_honor_factor) and household quality (get_household_modifier), with slave treatment/manumission settings ($g_slave_treatment, $g_slave_manu, edict11 slave tax). menu:latifundium and prsnt:estate_report show state, and menu_event_latifundium_fire_damage / _nodamage report fires. A blacksmith on the estate can improve items (dlg:11325 lat_item_improve).

- **Hooks:** `dlg:8881:dlga_barb_estate_talk_3`, `dlg:8904:dlga_lad_talk3`, `strig:53`, `strig:196`, `menu:latifundium`, `prsnt:estate_report/t0`, `dlg:11446:dlga_building_details`, `strig:82`
- **Scripts:** `spawn_latifundium`, `calculate_latifundium_rents`, `calculate_weekly_rents`, `get_building_details_lat`, `get_labour_slave_skill_modifier`, `get_honor_factor`, `get_household_modifier`, `spawn_party`
- **Menus:** `menu_latifundium`, `menu_event_latifundium_fire_damage`, `menu_event_latifundium_fire_nodamage`
- **Presentations:** `prsnt_estate_report`
- **Mission templates:** `mst_latifundium`, `mst_visit_villa`
- **Slots:** `party:214`, `party:218`, `party:219`, `party:220`, `party:221`, `party:222`, `party:223`, `party:224`, `party:225`, `party:226`, `party:227`, `party:228`, `party:229`, `party:230`, `party:231`, `party:235`, `party:236`, `party:237`, `party:238`, `party:239`, `party:240`, `party:242`, `party:243`, `party:32`, `party:43`, `party:105`
- **Globals:** `g_slave_treatment`, `g_slave_manu`, `edict11`, `g_effect_apllied`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `explain acan spawn_latifundium: texts 'Latifundia near {s0}', 'Estate near {s0}', building list`, `explain acan calculate_latifundium_rents: callees get_labour_slave_skill_modifier/get_event_details/get_honor_factor/get_household_modifier`, `explain acan get_building_details_lat: callers menu:latifundium, prsnt:estate_report, dlg building_details`
- **Overlaps:** `acan.culture_specific_fief_buildings`, `ad457.center_buildings_management`, `ad457.lord_business_build_hire_upgrade`, `bi.ai_lords_build`, `bi.garrison_building_battle_bonuses`, `bi.roman_public_buildings`, `pop.fief_base_income_and_reports`, `pop.fief_heartbeat_problems`, `pop.fief_improvements_expanded`, `pop.fief_stewards_with_skills`, `sw.recruit_unlock_buildings`, `vc.extended_center_improvements`

<a id="acwhunting"></a>
### Camp hunting: deer, boar and buffalo herds — acw (`acw.hunting`)

**What it does:** From the camp menu the player can go hunting (unless enemies are within 4 map units, or on water/desert). After a wait scaled by Tracking skill they encounter a deer, boar or buffalo herd, hunt it in a small mission, and loot meat and hides per kill.

**How it works:** menu:camp/opt:camp_go_hunting -> menu:camp_hunting_or_poaching (terrain + nearby-hostile checks) -> menu:hunting start_hunt: initialize_hunting_time (6 h x (11 - Tracking) +/- random) writes party slot 421 = end hour; set_hunting_found picks herd type slot 423 (deer ~70%, boar ~30%, buffalo 1%) and count slot 424; rest_for_hours. strig:98 hourly: when time reached, stop resting and jump to menu:deer_herd / boar_herd / buffalo_herd. 'Hunt' -> mission mst_deer_hunting etc. on scn_random_scene_plain_forest; animals are horse-type agents (itm_deer...) steered by t8 (flee from player within 25 m, else wander inside scene bounds); $num_hunted_animals_killed counts kills; back in the menu the kills are converted into deer/boar/buffalo meat + raw leather via change_screen_loot.

- **Hooks:** `menu:camp/opt:camp_go_hunting:conseq`, `menu:hunting/opt:start_hunt:conseq`, `strig:98`, `menu:deer_herd/opt:deer_kill:conseq`, `mst:deer_hunting/t8:conseq`
- **Scripts:** `initialize_hunting_time`, `set_hunting_found`
- **Menus:** `menu_camp_hunting_or_poaching`, `menu_hunting`, `menu_deer_herd`, `menu_boar_herd`, `menu_buffalo_herd`, `menu_deer_herd_kill_end`, `menu_boar_herd_kill_end`
- **Mission templates:** `mst_deer_hunting`, `mst_boar_hunting`, `mst_buffalo_hunting`
- **Slots:** `party:420`, `party:421`, `party:422`, `party:423`, `party:424`
- **Globals:** `player_hunting`, `num_hunted_animals_killed`, `leading_animal`, `g_infinite_camping`
- **Module-specific resources:** item: itm_deer, itm_boar, itm_buffalo, itm_deer_meat, itm_boar_meat, itm_buffalo_meat, itm_raw_leather; scene: scn_random_scene_plain_forest
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis acw menu:camp_hunting_or_poaching, menu:hunting/opt:start_hunt:conseq, strig:98, set_hunting_found, initialize_hunting_time, mst:deer_hunting/t8:conseq`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_scripts.py 45725 initialize_hunting_time; module_game_menus.py 19150-19172 caller passes reg1 from get_max_skill_of_player_party`
- **Overlaps:** `awoiaf.hunting_herds`, `tld.wilderness_encounters_hide_animal_ambush`

<a id="ad457dplmc4-tax-inefficiency-and-extras"></a>
### Diplomacy 4.x extras: tax inefficiency, disguises, taverngoer locations — ad457 (`ad457.dplmc4_tax_inefficiency_and_extras`)

**What it does:** Holding more fiefs than your administration can handle costs money: past a difficulty-based number of fiefs, each extra fief loses a growing share (up to 65%) of its taxes, reduced by having a chamberlain, a court and a spouse, and shifted by the kingdom's centralisation/policy settings. The chamberlain's overview and the budget report show the loss. Also present: buying disguises (pilgrim etc.) from minstrels, craftsmen and village elders to sneak into towns, and tavern travellers who list where ransom brokers, booksellers and minstrels can currently be found.

**How it works:** cf_dplmc_calculate_tax_inefficiency(num_fiefs, income, faction) (94 stmts; callers dlg:1058 dplmc_chamberlain_overview cond and prsnt:budget_report/t0): free fief count 2/4/6 by game_get_reduce_campaign_ai (+court bits from $players_kingdom_name_set, +1 if married), penalty per extra fief 5/4/3 %, capped at 65; reduction 10 with a chamberlain plus faction policy slots 301 (x5) and 303 (x3) (copied to the player faction from the liege when the player is a vassal); returns lost amount in reg0 and percent in reg1. acquire_disguise (dlg:3048/3054/3477/3658/3827/3944/3945) and set_disguise_override_items/get_disguise_string implement disguise outfits; list_known_taverngoers (dlg:3426/3431/3436) prints 'You can find {s10}s at {s11}'.

- **Hooks:** `dlg:1058:dlga_dplmc_chamberlain_overview:dplmc_chamberlain_pretalk:cond`, `prsnt:budget_report/t0`, `dlg:3426:dlga_tavern_traveler_minstrel_location_ask_money:tavern_traveler_npc_location_tell:conseq`, `dlg:3477:dlga_minstrel_disguise_teach:close_window:conseq`
- **Scripts:** `cf_dplmc_calculate_tax_inefficiency`, `acquire_disguise`, `set_disguise_override_items`, `get_disguise_string`, `list_known_taverngoers`, `cf_no_known_taverngoers`, `cf_find_alternative_town_for_taverngoers`
- **Menus:** `menu_dplmc_choose_disguise`
- **Presentations:** `prsnt_budget_report`
- **Dialogs:** `dlg:1058`, `dlg:3426`, `dlg:3431`, `dlg:3436`, `dlg:3477`, `dlg:3658`, `dlg:3944`
- **Slots:** `faction:301`, `faction:302`, `faction:303`, `faction:304`, `faction:306`, `troop:30`
- **Globals:** `g_dplmc_gold_changes`, `g_player_chamberlain`, `g_player_court`, `players_kingdom_name_set`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis ad457 cf_dplmc_calculate_tax_inefficiency: difficulty thresholds, 65% cap, chamberlain/policy reductions`, `explain ad457 cf_dplmc_calculate_tax_inefficiency: callers dlg:1058 and prsnt:budget_report/t0`, `explain ad457 acquire_disguise: 7 dialog callers, text 'Acquired {s0}'s clothing'`, `explain ad457 list_known_taverngoers: 3 tavern-traveller dialog callers`
- **Overlaps:** `acan.imperial_treasury_budget`, `acan.senate_influence_edicts`, `acan.town_decrees`, `be.pps_political_simulation`

<a id="awoiafiron-bank"></a>
### Iron Bank of Braavos: central deposits, loans with deadlines and war tax — awoiaf (`awoiaf.iron_bank`)

**What it does:** One bank in Braavos accepts deposits and grants loans. Interest rates depend on the player's honour, trade skill and the town's prosperity, and a 'war tax' reduces returns while the player's kingdom is at war. Missing a two-week repayment deadline compounds the debt, damages relations with Braavos and eventually with its faction.

**How it works:** prsnt_lazeras_bank_prsnt (t0) shows rating, rates (bank_report_rates), deposits (bank_report_deposit), cf_bank_war_tax and bank_get_prosperity_extra_to_s49; prsnt_bank handles borrow/repay on party slots 603/604 of $current_town (the bank is only offered in Braavos, p_town_42, which strig:11 polls). strig:11 (1h): if debt (p_town_42 slot 604) > 0 and hour >= deadline (slot 605) -> change_player_relation_with_center -5, debt *= $g_bank_debt_interest_rate/10 (capped 1,000,000), deadline += 336h; at cap -> faction relation -2; deposits (slot 809) accrue via bank_report_rates/bank_report_deposit.

- **Hooks:** `strig:11`, `prsnt:lazeras_bank_prsnt/t0`, `prsnt:bank/t0`
- **Scripts:** `bank_report_rates`, `bank_report_deposit`, `cf_bank_war_tax`, `bank_get_prosperity_extra_to_s49`
- **Menus:** `menu_lazeras_banking_menu`
- **Presentations:** `prsnt_lazeras_bank_prsnt`, `prsnt_bank`, `prsnt_bank_quickview`
- **Slots:** `party:603`, `party:604`, `party:605`, `party:806`, `party:809`
- **Globals:** `g_bank_debt_interest_rate`, `g_bank_deposit_interest_rate`, `g_apply_kaoses_bank_report_to_gold`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis strig:11 (deadline, interest compounding, relation penalties on p_town_42)`, `explain prsnt:lazeras_bank_prsnt/t0: callees cf_bank_war_tax, bank_report_rates, bank_report_deposit; text 'Rating', 'Poor/Average/Rich'`
- **Overlaps:** `sw.bank_interest_loans_payday`

<a id="awoiafside-jobs-and-camp-activities"></a>
### Odd jobs and camp activities (mines, village labour, music, gambling, fishing, smoking food) — awoiaf (`awoiaf.side_jobs_and_camp_activities`)

**What it does:** Low-tier ways to earn coin or supplies: volunteer to work in iron/salt/obsidian mines (needs tools), do day-labour in villages, perform music in taverns for income based on the Entertain skill, play 'find the lady' three-card gambling with tavern keepers, fish from camp (chance of treasure, risk of bandits), and smoke food to make it keep longer.

**How it works:** menu:iron_mine/salt_mine opt work_mines -> mine_work/mine_work2 (cf_player_has_tools_for_mine); menu_village_basic_work / menu_work_for_village_option; menu_perform_music -> entertain_income; dlga_tavern_tk_3cards -> prsnt_three_card; menu_camp_fishing; menu_camp_smoking_food -> rigale_smoke_food. Prisoners deposited in the salt and iron mines generate weekly slave-labour income with escape rolls (strig:75/76 -> menu_slave_labor).

- **Hooks:** `menu:iron_mine/opt:work_mines:conseq`, `menu:salt_mine/opt:work_mines:conseq`, `menu:perform_music`, `dlg:1011:dlga_tavern_tk_3cards:close_window:conseq`, `strig:75`, `strig:76`
- **Scripts:** `mine_work`, `mine_work2`, `cf_player_has_tools_for_mine`, `entertain_income`, `rigale_smoke_food`
- **Menus:** `menu_iron_mine`, `menu_obsidian_mine`, `menu_village_basic_work`, `menu_perform_music`, `menu_camp_fishing`, `menu_camp_smoking_food`, `menu_slave_labor`, `menu_slave_labor2`
- **Presentations:** `prsnt_three_card`
- **Globals:** `g_num_prisoners`, `g_earnings`, `g_num_escapees`, `g_num_prisoners2`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `roots mine_work -> menu:iron_mine/salt_mine opt work_mines`, `roots entertain_income -> menu:perform_music`, `refs prsnt_three_card <- dlga_tavern_tk_3cards`, `dis strig:75 (salt-mine slave labour: 12 coin/prisoner/week, escape roll, -2 honour)`

<a id="bepes-regional-economy"></a>
### Regional economy: population, resources, factories and supply — be (`be.pes_regional_economy`)

**What it does:** Towns have population, literacy, urbanisation and infrastructure; villages produce raw resources; towns build and staff factories that consume and produce resources, buy what they need from other centres (or overseas), raise prices, strike, fire workers or close. Nations tax and fund from it. Region and resource screens show production and demand.

**How it works:** strig:126 (every tick, one centre via trp_pes_centers list) -> pes_center_iteration: rolls per-iteration counters (party 561/562, 576-579), center_fix_owner, pes_center_change_population_literacy_urbanization, pes_center_calculate_infrastructure, pes_center_decide_build_factory, pes_center_villages_iteration, pes_employ_workers, pes_center_build_factories, per-factory pes_center_factory_iteration (355 stmts; 6 factory slots party 405-410), pes_center_population_buy_resources -> pes_find_and_buy_resource (183), then tops the garrison up with pas_reinforce_party. pes_iteration_start (taxes, oversea supply, price change, reshuffle). prsnt_pes_region / prsnt_pes_resource / prsnt_pes_region_build_factory; cf_if_player_is_allowed_to_manage_factory_in_center. Native process_player_enterprise emptied.

- **Hooks:** `strig:126`, `prsnt:pes_region/t0`, `prsnt:pes_resource/t0`, `prsnt:pes_region_build_factory/t0`
- **Scripts:** `pes_center_iteration`, `pes_center_factory_iteration`, `pes_find_and_buy_resource`, `pes_center_villages_iteration`, `pes_center_decide_build_factory`, `pes_create_factory_in_center`, `pes_employ_workers`, `pes_resource_bought`, `pes_resource_is_produced_by_center`, `pes_iteration_start`, `pes_init`, `pes_region_menu_display_region`, `pes_resource_menu_display_resource`
- **Presentations:** `prsnt_pes_region`, `prsnt_pes_resource`, `prsnt_pes_region_build_factory`
- **Slots:** `party:401-410`, `party:441-447`, `party:559-562`, `party:575-585`
- **Globals:** `pes_start_new_iteration_cycle`, `pes_region_selected_center`, `pes_resource_menu_return_to_region`
- **Module-specific resources:** troop: trp_pes_centers
- **Relation to Native:** replaces-native
- **Confidence:** strongly-inferred
- **Evidence:** `dis be strig:126, pes_center_iteration (call list)`, `explain be prsnt:pes_region/t0`, `auto report: process_player_enterprise 0/53 (emptied)`

<a id="cblnew-centre-economy-and-arena-wiring"></a>
### Trade routes, production and arenas for the new centres — cbl (`cbl.new_centre_economy_and_arena_wiring`)

**What it does:** The new towns and villages are wired into the economy: 102 extra land trade routes between town pairs, per-town and per-village production levels for the new centres, and arena/tournament data for the new towns.

**How it works:** All by explicit per-centre statements, not loops: initialize_trade_routes (195 stmts vs the base module 93) adds 102 set_trade_route_between_centers calls (e.g. p_town_24 <-> p_town_5/31/10/22/20/19/2); initialize_economic_information (559 vs 345) adds ~122 party_set_slot statements on new centres in the production slots 214-230 (one Native line moved from p_town_19 to p_town_20); initialize_town_arena_info (275 vs 137) adds arena layouts for the new towns. initialize_sea_trade_routes is emptied (0 statements; the base module has 22 that set coastal-town slots 63/450 and 7 sea routes), so cbl has no sea trade. Native's distance-based village binding (game_start) gives every new village a bound centre and owner automatically.

- **Hooks:** `script:game_start`
- **Scripts:** `initialize_trade_routes`, `initialize_economic_information`, `initialize_town_arena_info`, `initialize_sea_trade_routes`, `set_trade_route_between_centers`
- **Slots:** `party:63`, `party:214`, `party:215`, `party:219`, `party:221`, `party:222`, `party:223`, `party:224`, `party:225`, `party:226`, `party:227`, `party:228`, `party:229`, `party:230`, `party:450`
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Overlaps:** `cbl.expanded_calradia_map`, `cbl.twelve_borderland_kingdoms`, `cbl.v352_later_version_changes`

<a id="laigleold-native-baseline"></a>
### Pre-1.15x Native baseline (shared with CAE and 1860s) — laigle (`laigle.old_native_baseline`)

**What it does:** About 60 of L'Aigle's 'modified Native' scripts - the trade-good price model, center production, lord defection, merchant restocking via triggers - are not L'Aigle changes at all but an older Native version that CAE and 1860s Old America also use.

**How it works:** Shape-hash comparison: update_trade_good_prices (5 stmts in laigle/oa1860/cae/pop vs 37 in native/vc/awoiaf/be/acw), initialize_economic_information 231 vs 338, center_get_production 210 vs 235, lord_find_alternative_faction 32 vs 57. Merchant restocking lives in trig:1-4 (troop_add_merchandise_with_faction + troop_add_gold), and Native's refresh_center_armories/inventories/stables/weaponsmiths scripts are absent.

- **Hooks:** `trig:1:conseq`, `trig:2:conseq`, `trig:3:conseq`, `trig:4:conseq`
- **Scripts:** `update_trade_good_prices`, `initialize_economic_information`, `center_get_production`, `average_trade_good_prices`, `lord_find_alternative_faction`
- **Relation to Native:** replaces-native
- **Confidence:** confirmed
- **Evidence:** `sqlite shape_hash grouping of update_trade_good_prices / initialize_economic_information / center_get_production / lord_find_alternative_faction across modules`, `dis oa1860 trig:2:conseq (identical economy trigger family)`, `auto report: refresh_center_* listed as Native scripts absent`

<a id="laigleregimental-depots"></a>
### National regimental depots with rank-gated uniform shops — laigle (`laigle.regimental_depots`)

**What it does:** Each nation's capital has a Depot with sub-menus for troops, uniforms (line, light infantry, cavalry) and an Arsenal. Uniform options open a trade screen stocked with exactly that uniform set, but only if your rank is high enough.

**How it works:** menu:town/opt:<nation>_depot_entrance (cond: encountered town belongs to that kingdom and is a town) -> menu_<nation>_depot -> _troops / _uniform_types / _uniforms / _uniforms_light / _uniforms_cavalry. Each uniform option checks $character_rank, then troop_clear_inventory trp_depot_merchant, troop_add_item the set, change_screen_trade. 10 nations x 7 menus.

- **Hooks:** `menu:town/opt:french_depot_entrance:conseq`
- **Menus:** `menu_french_depot`, `menu_french_depot_troops`, `menu_french_depot_uniform_types`, `menu_french_depot_uniforms`, `menu_french_depot_uniforms_cavalry`, `menu_french_depot_uniforms_light`
- **Globals:** `character_rank`
- **Module-specific resources:** troop: trp_depot_merchant
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis laigle menu:town/opt:french_depot_entrance:cond`, `dis laigle menu:french_depot_uniforms/opt:grenadier:conseq (clear inventory, add set, change_screen_trade)`, `refs laigle menu menu_regiment_recruitment (9 Arsenal entries)`

<a id="perisnobank-and-gambling"></a>
### Town bank screen and a gambling game — perisno (`perisno.bank_and_gambling`)

**What it does:** Town menus offer a bank (visit the landlords and moneylenders) with a quick-view panel, and a mystic merchant offers a gambling mini-game.

**How it works:** menu:town option town_bank opens prsnt_bank; the presentation has event handlers that reopen it (7 references) and prsnt:bank_quickview shows balance. The treasury slot party[396] is read by the bank presentation. A dialog line with the mystic merchant opens prsnt_gambling, whose event handler is referenced 8 times. Interest or odds were not decoded.

- **Hooks:** `menu:town/opt:town_bank:conseq`, `dlg:6090:dlga_mystic_merchant_talk:close_window:conseq`
- **Scripts:** `trade_ledger_create`
- **Presentations:** `prsnt_bank`, `prsnt_bank_quickview`, `prsnt_gambling`
- **Slots:** `party:396`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `refs perisno prsnt prsnt_bank: opened from menu:town/opt:town_bank, re-entered from prsnt:bank/t1`, `refs perisno prsnt prsnt_gambling: opened from dlg:6090:dlga_mystic_merchant_talk, 7 self-references in prsnt:gambling/t2`, `slot perisno party 396 readers include prsnt:bank/t0 and prsnt:bank_quickview/t0`, `presentation bodies not disassembled`

<a id="perisnobudget-and-patrol-wages"></a>
### Hourly budget processing, patrol wages and budget report — perisno (`perisno.budget_and_patrol_wages`)

**What it does:** The game periodically pays the player's party wages, patrol wages, enterprise income and tax, tracks debt to party members, and shows it all in a budget report presentation. Companions can complain when unpaid.

**How it works:** strig:150 (every 1h) calls et_process_budgets -> process_budgets (833 stmts): hero wages via game_get_troop_wage, process_player_enterprise, tax description, party strength, withdrawals from the chamberlain's treasury (dplmc_withdraw_from_treasury), and pay_patrol_wages (304 stmts) which charges prisoner-price based amounts per patrol party and keeps party slot 396. prsnt:budget_report/t0 shows the totals.

- **Hooks:** `strig:150`, `prsnt:budget_report/t0`
- **Scripts:** `et_process_budgets`, `process_budgets`, `pay_patrol_wages`, `process_player_enterprise`, `dplmc_withdraw_from_treasury`, `game_get_troop_wage`
- **Slots:** `party:396`, `party:7`, `faction:111`
- **Globals:** `g_player_debt_to_party_members`, `et_payment_cost`, `g_cur_week_half_daily_wage_payments`, `npc_with_grievance`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `explain perisno process_budgets: caller et_process_budgets, entry strig:150 (every 1h); writes g_player_debt_to_party_members, et_payment_cost, npc_with_grievance`, `explain perisno pay_patrol_wages: callers process_budgets and prsnt:budget_report/t0; slots party[396], party[7]`, `slot perisno party 396: pay_patrol_wages, prsnt:bank/t0, et_chamberlain_collect_all_treasury (module-specific slot)`, `tree perisno process_budgets --depth 1: callees listed`

<a id="perisnotrade-ledger"></a>
### Merchant ledger (what a trade good would earn elsewhere) — perisno (`perisno.trade_ledger`)

**What it does:** From the reports menu the player opens a Merchant Ledger that lists goods by town with an assessed profit if sold in another town, based on the party's best trade skill.

**How it works:** menu:reports option action_view_trade_ledger opens prsnt_trade_ledger_basic. Its load handler (523 stmts) builds a table from the array library (array_get_element, array_pushback), reads get_max_skill_of_player_party / skl_trade, and prints '{s1} sold in {s2} would earn {reg0} aurums'. A related menu town_trade_assessment creates the ledger array on demand. Entries are trimmed and de-duplicated by cf_trade_ledger_trim_entries / ..._custom_assess_duplicates.

- **Hooks:** `menu:reports/opt:action_view_trade_ledger:conseq`, `menu:town_trade_assessment`, `prsnt:trade_ledger_basic/t0`
- **Scripts:** `trade_ledger_create`, `cf_trade_ledger_trim_entries`, `cf_trade_ledger_custom_assess_item`, `cf_trade_ledger_custom_assess_duplicates`, `get_max_skill_of_player_party`
- **Menus:** `menu:town_trade_assessment`
- **Presentations:** `prsnt_trade_ledger_basic`
- **Slots:** `party:997`, `party:999`, `troop:164`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `refs perisno prsnt prsnt_trade_ledger_basic: menu:reports/opt:action_view_trade_ledger`, `explain perisno prsnt:trade_ledger_basic/t0: callees array_*, get_max_skill_of_player_party; text 'Merchant Ledger', 'sold in ... would earn ... aurums'`, `explain perisno array_create: callers trade_ledger_create; entry menu:town_trade_assessment`, `slot perisno troop 164: s1 in trade_ledger_create`

<a id="swbank-interest-loans-payday"></a>
### Bank account with interest, 30-day loans, weekly pay-day from cash or account — sw (`sw.bank_interest_loans_payday`)

**What it does:** The player keeps credits in a bank account that earns interest every six days; fief taxes are paid straight into the account; he can take one loan at a time (1000/2500/5000) repayable within 30 days at a fixed rate; on pay day he chooses to pay troop wages from cash, from the account, or a mix.

**How it works:** Balances live in faction slots of fac_trade_federation (faction 6, the in-setting banker): 86 debt, 87 deposit, 88 loan rate (12), 89 deposit rate (8), 90 loan due hour; strig:95 (1 h) sets rates. strig:96 (24 h, when $g_taxes_calculated) sums each owned center's party slots 47+48 (accumulated rents/tariffs), zeroes them and adds the total to the deposit with a 'Weekly Income' dialog box. strig:97 (144 h) adds deposit x rate/500 interest. menu:bank shows balance, due date / overdue; menu:take_out_loan options add principal+interest to debt and set due date; menu:bank give_loan / give_loan_all repay. menu:pay_day (calculate_player_faction_wage) offers pay_account / pay_both_1 / pay_both_2.

- **Hooks:** `strig:95`, `strig:96`, `strig:97`, `menu:bank`, `menu:take_out_loan`, `menu:pay_day`
- **Scripts:** `calculate_player_faction_wage`
- **Menus:** `menu_bank`, `menu_take_out_loan`, `menu_pay_day`
- **Slots:** `faction:86-90 (fac_trade_federation = bank state)`, `party:47-48 (center accumulated income)`
- **Globals:** `g_player_debt`, `g_player_deposit`, `g_cur_interest_debt`, `g_taxes_calculated`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis sw menu:bank (faction slots 86-90)`, `global sw g_player_debt writers: take_out_loan 1000/2500/5000, bank give_loan/_all`, `dis sw strig:96 / strig:97 (tax deposit, interest)`, `slot sw faction 87: writers pay_day options, strig:96, strig:97`
- **Overlaps:** `awoiaf.iron_bank`

<a id="tldfaction-resource-points-upkeep"></a>
### Per-faction Resource Points purse with faction-paid troop upkeep — tld (`tld.faction_resource_points_upkeep`)

**What it does:** Instead of one gold purse, the player holds a separate pool of Resource Points (RP) with every faction. Gold shown on screen is just the RP of the faction whose territory you are in; troops are paid from the RP of their own faction, and if that pool runs dry the faction recalls (removes) its unpaid soldiers.

**How it works:** Faction slot 72 stores the player's RP with that faction. set_ambient_faction swaps the displayed troop gold to the new 'ambient' faction's RP when the player changes region/town (saving the old value back); update_respoint copies current gold back into slot 72. add_faction_rps(faction, amount) adjusts slot 72 (and the visible gold if it is the ambient faction) and prints 'You gained/lost N Resource Points of X' -- 41 callers (quest rewards, selling prisoners, gifts, disbanding troops). strig:7 (every 96.4 h) make_player_pay_upkeep loops factions 3-20, charges each faction's troops in the main party (inventory-management skill discounts 3%/level) plus half-wage for the player's reserve parties (troop 0 slots 50/309) against that faction's RP; troops it cannot pay are flagged (troop slot 48). strig:9 (every 4.15 h) make_unpaid_troop_go removes flagged troops ('Superior orders from X...'), refunding a disband value. menu:upkeep_report shows RP/party/reserve upkeep per faction. Mordor (6) and Dol Guldur (17) share one pool.

- **Hooks:** `strig:7`, `strig:9`, `menu:upkeep_report`, `menu:town/opt:town_leave:conseq`
- **Scripts:** `add_faction_rps`, `set_ambient_faction`, `update_respoint`, `make_player_pay_upkeep`, `make_unpaid_troop_go`, `compute_wage_per_faction`, `game_get_troop_wage`, `get_troop_disband_cost`, `get_party_disband_cost`
- **Menus:** `menu:upkeep_report`
- **Dialogs:** `dlg:285:dlga_player_hire_troop:tld_sell_prisoners_all:conseq`, `dlg:1298:dlga_disband_regular_member_confirm_yn:close_window:conseq`, `dlg:583:dlga_send_gift_1:lord_pretalk.1:cond`
- **Slots:** `faction:72`, `troop:48`, `troop:50 (player)`, `troop:309 (player)`
- **Globals:** `ambient_faction`, `g_player_troop`, `g_cur_week_half_daily_wage_payments`, `g_fast_mode`
- **Module-specific resources:** string: qstr_You_gained_{reg0}_Re, qstr_Short_of_Resource_Po
- **Relation to Native:** replaces-native
- **Confidence:** confirmed
- **Evidence:** `dis tld add_faction_rps / set_ambient_faction / update_respoint (faction slot 72 <-> troop gold)`, `dis tld make_player_pay_upkeep: per-faction loop, troop slot 48 unpaid flag, display 'Short of Resource Points'`, `dis tld make_unpaid_troop_go: party_remove_members on flagged troops`, `explain tld add_faction_rps: 41 direct callers, 90 entry points`

<a id="vctown-plunder-and-slaves"></a>
### Plundering captured towns, loot choices, recovery time and slave-taking — vc (`vc.town_plunder_and_slaves`)

**What it does:** When a town or fort falls the player can sack it (a street-fighting plunder scene and a lump of silver, keeping or not keeping control), which leaves it 'plundered' for weeks with a changed map icon. Raided villagers can be hunted down as slaves, slave traders operate in towns (and can be banned), and after battle a loot-options menu decides how the spoils are split.

**How it works:** menu:castle_taken offers castle_taken_plunder / castle_taken_keepplunder / castle_taken_native; plunder variants run mst_center_plunder, pay {reg7} silver and set party slot 344 (plunder timer, days) + change_party_icon_loot_state; strig:135 counts slot 344 down daily and restores the icon; menu_saqueo_loot_continue blocks re-looting. strig:103/check_town_menu_conditions read slot 344 (no conversion, reduced services). Village raids: menu_village_raid_villagers_toslaves / village_loot_no_resist_population_flee add slaves; slave market building (center_manage center_build_slavemarket / center_kill_slavemarket -> menu_remove_slaves, which warns it reduces income; it touches Native party slot 48 = accumulated tariffs) and sell_prisoners (adventurer AI, strig:109). menu_loot_options (loot_0..loot_3), reached from menu:total_victory after battle, with $loot_option / $loot_value_before / $loot_options_shown.

- **Hooks:** `menu:castle_taken`, `menu:castle_taken_plunder`, `menu:castle_taken_keepplunder`, `strig:135`, `menu:village_raid_villagers_toslaves`, `menu:loot_options`, `menu:remove_slaves`
- **Scripts:** `change_party_icon_loot_state`, `sell_prisoners`, `check_town_menu_conditions`
- **Menus:** `menu_castle_taken_plunder`, `menu_castle_taken_keepplunder`, `menu_castle_taken_native`, `menu_saqueo_loot_continue`, `menu_village_raid_villagers_toslaves`, `menu_village_loot_no_resist_population_flee`, `menu_loot_options`, `menu_remove_slaves`
- **Mission templates:** `mst_center_plunder`
- **Slots:** `party:344`, `party:48`
- **Globals:** `player_is_looting_town`, `plunder_battle_shown`, `loot_option`, `loot_options_shown`, `loot_value_before`
- **Module-specific resources:** troop: trp_slave
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `sqlite refs: mst_center_plunder <- menu:castle_taken_plunder, menu:castle_taken_keepplunder`, `sqlite texts: 'The {town/fort} is plundered. You have collected {reg7} peningas.'; 'Do you want to hunt the villagers down like animals and make them slaves?'; 'The battle is over. What do you want to do with the loot?'`, `dis vc strig:135: slot 344 countdown + change_party_icon_loot_state`, `slot vc party 344: writers castle_taken_plunder/keepplunder, saquear_*; readers town, castle_outside, port_encounter, check_town_menu_conditions`, `sqlite refs: menu_loot_options referenced from menu:total_victory`
- **Overlaps:** `acan.slave_economy`, `ad457.village_enslavement_and_repopulation`, `laigle.keep_battlefield_pickups`

<a id="vcweekly-trade-ledger"></a>
### Weekly trade ledger in the budget report and anti-exploit price formulas — vc (`vc.weekly_trade_ledger`)

**What it does:** Everything the player buys or sells is tallied for the week, split into trade goods and other items, and shown as its own lines in the weekly budget report. The buy/sell price formulas were also reworked so that buying and selling the same item repeatedly no longer makes money.

**How it works:** Modified engine-called game_event_buy_item / game_event_sell_item (58 vs Native 23 stmts) price the transaction via game_get_item_buy_price_factor / game_get_item_sell_price_factor (57/89 vs Native 18/20) and accumulate $num_buyed_goods_in_week / $buyed_goods_in_week_for (trade goods itm_mead..itm_siege_supply) or $num_buyed_items_in_week / $buyed_items_in_week_for (other items), with the mirror $num_selled_* / $selled_* on sales. They still push the town's trade-good price slot (party slot 251 + good index) up by 14 (buy) or 21 (buy-back), capped at 10000. prsnt:budget_report/t0 reads and resets the ledger weekly.

- **Hooks:** `script:game_event_buy_item`, `script:game_event_sell_item`, `prsnt:budget_report/t0`
- **Scripts:** `game_event_buy_item`, `game_event_sell_item`, `game_get_item_buy_price_factor`, `game_get_item_sell_price_factor`
- **Presentations:** `prsnt_budget_report`
- **Slots:** `party:251+good`
- **Globals:** `num_buyed_goods_in_week`, `buyed_goods_in_week_for`, `num_buyed_items_in_week`, `buyed_items_in_week_for`, `num_selled_goods_in_week`, `selled_goods_in_week_for`, `num_selled_items_in_week`, `selled_items_in_week_for`
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `dis vc game_event_buy_item: price factor, goods/items split into $num_buyed_*/$buyed_*_in_week_for, price slot 251+good +14/+21`, `sqlite globals buyed_goods_in_week_for etc.: r/w game_event_buy_item, game_event_sell_item, prsnt:budget_report/t0; reset in update_savegame_to_content_update`, `sqlite cmp: vc 58/58/57/89 vs native 23/23/18/20`, `Changelog 2.023 'Alter price adjustment formulas to avoid player from making money just by buying/selling a single item over and over again'; 2.025 'adjust pricing formulas'`

<a id="acanconquest-aftermath-culture-change"></a>
### Conquest aftermath: keep or plunder, exterminate/enslave the population, raze the settlement, repopulate and shift its culture — acan (`acan.conquest_aftermath_culture_change`)

**What it does:** After taking a town or fort the player chooses its fate: keep it, plunder it, kill or enslave the population, or raze it entirely. Exterminated settlements can be repopulated with the conqueror's people, which changes the place's culture (walkers, town watch, recruits, map icon). Harsh choices anger lords and can cost honorary titles.

**How it works:** menu:castle_taken_plunder / castle_taken_keepplunder / castle_taken_native / desert_town_loot2 handle plunder. menu:exterminate_population (152 stmts) turns locals into prisoners/slaves (troop_to_slave_mapping, party_add_wounded_members_as_prisoners), recomputes production and consumption, and may call destroy_center (prosperity crash, party destroyed, quests aborted, faction strength recalculated; text '{s21} is angry about {s20} and he may lose his honorary title!'). menu:repopulate ('Kill them all' special-tax option) and cf_check_building_finished call change_culture_of_center, which rewrites the settlement's culture, walkers (center_set_walker_to_type), town watch troops (update_town_watch: party 381-384) and walled icon (set_icon_for_walled_center), with the notice '{s0} changed from {s2} to {s1} culture'. Volunteers then follow the new culture via get_unit_according_to_subculture and get_peasant_warrior_for_culture.

- **Hooks:** `menu:castle_taken_plunder`, `menu:exterminate_population`, `menu:repopulate/opt:special_tax:conseq`, `menu:desert_town_loot2`, `strig:82`, `script:game_event_simulate_battle`
- **Scripts:** `destroy_center`, `change_culture_of_center`, `update_town_watch`, `center_set_walker_to_type`, `set_icon_for_walled_center`, `troop_to_slave_mapping`, `get_unit_according_to_subculture`, `get_peasant_warrior_for_culture`, `get_party_subculture_string_id`, `cohort_refil_garrison`
- **Menus:** `menu_castle_taken_plunder`, `menu_exterminate_population`, `menu_repopulate`, `menu_castle_taken_2`
- **Mission templates:** `mst_center_plunder`
- **Slots:** `party:10`, `party:381`, `party:382`, `party:383`, `party:384`, `party:406`, `party:407`, `party:408`, `party:46`, `party:68`
- **Globals:** `g_fire`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `explain acan menu:exterminate_population: callees troop_to_slave_mapping, get_unit_according_to_subculture, mst_center_plunder`, `explain acan destroy_center: callers castle_taken_plunder / desert_town_loot2 / exterminate_population, faction_recalculate_strength`, `explain acan change_culture_of_center: text '{s0} changed from {s2} to {s1} culture', update_town_watch slots 381-384`

<a id="acanculture-specific-fief-buildings"></a>
### Culture-specific fief buildings with culture drift (inherits ad457.center_buildings_management; acan adds culture shift and piety effects) — acan (`acan.culture_specific_fief_buildings`)

**What it does:** Towns and forts have about 34 building types, each with a name, description and cost that depend on the settlement's culture (a Roman sewer becomes a Persian kariz or a British sacred grove). AI lords build too. Finished buildings raise prosperity, health and relations, unlock unit recruitment and can gradually shift the settlement's culture.

**How it works:** get_improvement_details (828 vs Native 32 stmts) dispatches on the improvement slot (party 271-304) and the settlement culture to return name, description and cost (e.g. 294 sewers: rome/eastern/germanic/british/dacian/nomadic variants; 287 hospital; 291 training; 293 barracks). The player orders buildings from prsnt:center_management, and AI lords via improve_center from troop_does_business_in_center. strig:82 (about every 2 min) runs cf_check_building_finished (235 stmts): it completes the work, applies prosperity, renown, honour and relation changes and add_piety_culture_effect, and can call change_culture_of_center, which moves a settlement to the builder's culture (walkers, town watch, icon). Buildings then gate unit recruitment (cf_can_hire_cohort -> get_building_culture) and feed the epidemic roll (287/294).

- **Hooks:** `strig:82`, `prsnt:center_management/t0`, `prsnt:center_management/t4`, `script:troop_does_business_in_center`, `mst:center_management/t5`
- **Scripts:** `get_improvement_details`, `cf_check_building_finished`, `improve_center`, `get_building_culture`, `change_culture_of_center`, `get_improvement_picture`, `add_piety_culture_effect`, `set_icon_for_walled_center`
- **Presentations:** `prsnt_center_management`, `prsnt_fief_management`
- **Slots:** `party:271`, `party:272`, `party:273`, `party:274`, `party:275`, `party:276`, `party:277`, `party:278`, `party:279`, `party:280`, `party:281`, `party:282`, `party:283`, `party:284`, `party:285`, `party:286`, `party:287`, `party:288`, `party:289`, `party:290`, `party:291`, `party:292`, `party:293`, `party:294`, `party:295`, `party:296`, `party:297`, `party:298`, `party:299`, `party:300`, `party:301`, `party:302`, `party:303`, `party:304`, `party:305`, `party:306`, `party:326`, `party:327`
- **Globals:** `g_improvement_type`, `g_set_center_upgrades`, `g_fire`
- **Relation to Native:** replaces-native
- **Confidence:** strongly-inferred
- **Evidence:** `dis acan get_improvement_details: branch ids 271-304, culture-dependent str_sewers_name_rome/eastern..., str_hospital_*, str_barracks_name_rome, str_training_name_rome cost 80000`, `explain acan cf_check_building_finished: strig:82, callees change_culture_of_center/add_piety_culture_effect`, `text 'Health' --mods acan: sewers/hospital descriptions per culture`, `compare get_improvement_details/cf_check_building_finished/improve_center --mods acan,ad457: 79%/84%/93% shape; callees ad457 cf_check_building_finished: no change_culture_of_center / add_piety_culture_effect`
- **Overlaps:** `acan.latifundium_estates`, `ad457.center_buildings_management`, `ad457.lord_business_build_hire_upgrade`, `bi.ai_lords_build`, `bi.garrison_building_battle_bonuses`, `bi.roman_public_buildings`, `pop.fief_base_income_and_reports`, `pop.fief_heartbeat_problems`, `pop.fief_improvements_expanded`, `pop.fief_stewards_with_skills`, `sw.recruit_unlock_buildings`, `vc.extended_center_improvements`

<a id="acwtavern-musicians-ambience"></a>
### Tavern ambience: seated musicians playing banjo/fiddle, patrons sitting and drinking — acw (`acw.tavern_musicians_ambience`)

**What it does:** Taverns get seated musicians who play a banjo or fiddle tune, and patrons who sit, some with a drinking mug, instead of standing around.

**How it works:** Tuple `dedal_tavern_animations` (module_mission_templates.py 5117, credited '#dedal') in mst town_default, ti_on_agent_spawn while $talk_context = tc_tavern_talk: musicians (tavern_musicians_begin..end) holding itm_dedal_banjo / itm_dedal_fiddle get stand + current animation anim_lute_sitting / anim_lyre_sitting and agent_play_sound snd_dedal_tavern_banjo / _fiddle, animation progress randomised; walkers (walkers_begin..end) with a mug item get anim_sitting_drinking_low, others anim_sitting_low. menu:town 'Visit the tavern' adds the musicians with override instrument items.

- **Hooks:** `mst:town_default/t0:cond`, `menu:town/opt:town_tavern:conseq`
- **Menus:** `menu_town`
- **Mission templates:** `mst_town_default`
- **Globals:** `talk_context`
- **Module-specific resources:** item: itm_dedal_banjo, itm_dedal_fiddle, itm_dedal_kufel, itm_dedal_kufel_indian; anim: anim_lute_sitting, anim_lyre_sitting, anim_sitting_drinking_low, anim_sitting_low; sound: snd_dedal_tavern_banjo, snd_dedal_tavern_fiddle
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `grep dedal --mods acw -> menu:town/opt:town_tavern:conseq (override itm_dedal_banjo), mst:town_default/t0:cond`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_mission_templates.py 5117-5170 dedal_tavern_animations`

<a id="ad457village-enslavement-and-repopulation"></a>
### Enslaving villages and 'repopulating' hostile settlements — ad457 (`ad457.village_enslavement_and_repopulation`)

**What it does:** A ruthless player can enslave a village's inhabitants (big relation loss with the village, companion objections, lower honour, and soldiers of that kingdom think less of you) or, from the management screen of a hostile settlement he holds with 200+ men, kill the locals and give the land to his soldiers' families. The kingdom-wide soldier opinion feeds into the morale of troops of that origin in your party.

**How it works:** menu:village option -> menu_village_enslave_complete: achievement stats, objectionable_action(3, str_sell_slavery), village relation -25..-35, looted smoke particle, faction relation -2 if hostile, change_faction_troop_morale(faction, -75 x villagers (max -2000), notify=1). change_faction_troop_morale (44 stmts) adds to Native faction slot 99 (morale of player's troops from that faction) and messages when the hundreds digit changes; game_get_morale_of_troops_from_faction (modified) reads slot 99 per troop culture and adds a bonus for the player's own culture. menu_repopulate (from prsnt:center_management/t2, needs >=200 men and negative relation) -> menu_repopulate_complete; its 'Kill them all' option also writes $piety. strig:81 applies -5000 troop morale for a defeated faction.

- **Hooks:** `menu:village`, `menu:village_enslave_complete`, `prsnt:center_management/t2`, `menu:repopulate/opt:special_tax:conseq`, `strig:81`
- **Scripts:** `change_faction_troop_morale`, `game_get_morale_of_troops_from_faction`, `objectionable_action`, `change_player_relation_with_center`, `change_player_relation_with_faction`
- **Menus:** `menu_village_enslave_complete`, `menu_repopulate`, `menu_repopulate_complete`
- **Presentations:** `prsnt_center_management`
- **Slots:** `faction:99`, `faction:21`
- **Globals:** `qst_eliminate_bandits_infesting_village_num_villagers`, `current_town`, `piety`
- **Module-specific resources:** psys: psys_map_village_looted_smoke; mesh: mesh_pic_prisoner_wilderness
- **Relation to Native:** modifies-native
- **Confidence:** strongly-inferred
- **Evidence:** `refs ad457 menu menu_village_enslave_complete: from menu:village`, `dis ad457 menu:village_enslave_complete: relation -25..-35, objectionable_action, change_faction_troop_morale`, `dis ad457 change_faction_troop_morale and game_get_morale_of_troops_from_faction: faction slot 99`, `slot ad457 faction 99: Native slot also used by Native morale_report`
- **Overlaps:** `acan.slave_economy`, `laigle.keep_battlefield_pickups`, `vc.town_plunder_and_slaves`

<a id="biroman-public-buildings"></a>
### Roman public buildings in fiefs (18 improvement types, upkeep, effects) — bi (`bi.roman_public_buildings`)

**What it does:** Replaces Native's 6 village/castle improvements with 25 building slots: village works (manor, mill, watch tower, school, messenger post, prison tower, plantation, lumber yard) and town/castle buildings (mercenary hall, merchant guild, military academy, forge, arsenal, stables, training ground, shooting range) plus Roman-only monuments (horreum, thermae, templum, castra, basilica, aquaeductus, amphitheatrum). Each has a cost, build time, a monthly effect, and the Roman monuments charge the player a monthly upkeep.

**How it works:** Player picks a building in menu:center_manage (one option per building, gated by settlement type, existing slot, nearby-school for the academy, cf_center_is_roman for slots 148-154) -> menu:center_improve (lumber yard slot 134 lowers cost) -> improve_center stores the type in party slot 124 and finish-hour in 125 -> strig:69 (and a duplicate strig:112) every 12h sets party slot <type>=1 and logs 'Building of X finished'. Effects: strig:82 (every 720h) calls center_apply_monthly_building_effects (prosperity +1..+3 for plantation 133, merchant guild 139, forge 141, horreum 148, basilica 152, aquaeductus 153, +1 if romanitas>=50; garrison XP via party_upgrade_with_xp for training ground 144/shooting range 145/castra 151; castra adds 3-6 faction tier-2 troops; templum 150/thermae 149/amphitheatrum 154 add +1 village relation slot 26) and then charges upkeep 200-600 denars per monument from the player, or drops relation by 2 if unpaid. Other readers: strig:44 weekly rent +20% basilica / +10% merchant guild (party slot 47); update_mercenary_units_of_towns (mercenary hall 138: better and +4 mercenaries); refresh_center_stables (stables 143: extra horse merchandise); center_get_food_consumption (horreum: -40% food use); update_volunteer_troops_in_village (horreum x1.5 volunteers, templum better tier); enter_court (castra +2, arsenal +1 hall guards); get_center_ideal_prosperity (mill 146).

- **Hooks:** `menu:center_manage`, `menu:center_improve`, `strig:69`, `strig:112`, `strig:82`, `strig:44`, `script:update_mercenary_units_of_towns`, `script:refresh_center_stables`
- **Scripts:** `get_improvement_details`, `improve_center`, `get_improvement_progress`, `center_apply_monthly_building_effects`, `cf_center_infrastructure`, `cf_center_is_roman`, `center_get_food_consumption`, `update_mercenary_units_of_towns`, `refresh_center_stables`, `update_volunteer_troops_in_village`, `enter_court`, `initialize_improvement_info`
- **Menus:** `menu_center_manage`, `menu_center_improve`
- **Slots:** `party:124`, `party:125`, `party:130`, `party:132`, `party:133`, `party:134`, `party:135`, `party:136`, `party:137`, `party:138`, `party:139`, `party:140`, `party:141`, `party:142`, `party:143`, `party:144`, `party:145`, `party:146`, `party:147`, `party:148`, `party:149`, `party:150`, `party:151`, `party:152`, `party:153`, `party:154`, `party:26`, `party:47`
- **Globals:** `g_improvement_type`
- **Relation to Native:** replaces-native
- **Confidence:** confirmed
- **Evidence:** `dis bi get_improvement_details: 25 named buildings with costs (Manor 8000 ... Amphitheatrum 24000)`, `slot bi party 148/153: written only by menu:center_manage options, read by monthly effects/food/recruit scripts`, `dis bi strig:82: upkeep + 'You cannot pay for the upkeep of the public buildings in {s4}. They fall into disrepair.'`, `dis bi strig:69: completion sets party slot <type>=1`, `dis bi center_get_food_consumption / update_mercenary_units_of_towns / refresh_center_stables show slot reads`, `grep bi replace_scene_props|scene_prop_set_visibility|spawn_scene_prop: only change_flag_owner, remove_siege_objects, change_banners_and_chest, place_player_banner_near_inventory_bms and multiplayer blocks - none read improvement slots`
- **Overlaps:** `acan.culture_specific_fief_buildings`, `acan.latifundium_estates`, `ad457.center_buildings_management`, `ad457.lord_business_build_hire_upgrade`, `bi.ai_lords_build`, `bi.garrison_building_battle_bonuses`, `pop.fief_base_income_and_reports`, `pop.fief_heartbeat_problems`, `pop.fief_improvements_expanded`, `pop.fief_stewards_with_skills`, `sw.recruit_unlock_buildings`, `vc.extended_center_improvements`

<a id="perisnoperisno-inn"></a>
### Enterable inn with fights and a hired assassin — perisno (`perisno.perisno_inn`)

**What it does:** A town inn scene the player can enter; the visit can trigger a belligerent drunk fight or a hired-assassin attack, with musicians and decorative items present.

**How it works:** menu:perisno_inn / perisno_inn_first_time option 'Enter the Inn' calls cf_enter_perisno_inn (92 stmts), which runs initialize_tavern_variables and setup_tavern_attacker, sets perisno_inn_visited and the g_start_belligerent_drunk_fight / g_start_hired_assassin_fight globals, and starts scn_perisno_inn_interior with mst_town_default.

- **Hooks:** `menu:perisno_inn/opt:interior:conseq`, `menu:perisno_inn_first_time/opt:interior:conseq`
- **Scripts:** `cf_enter_perisno_inn`, `initialize_tavern_variables`, `setup_tavern_attacker`
- **Slots:** `party:95`, `party:96`, `party:107`, `party:108`
- **Globals:** `perisno_inn_visited`, `g_start_belligerent_drunk_fight`, `g_start_hired_assassin_fight`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `explain perisno cf_enter_perisno_inn: callers the two inn menu options; writes g_start_belligerent_drunk_fight, g_start_hired_assassin_fight`, `explain perisno cf_enter_perisno_inn: scene ref scn_perisno_inn_interior, troop refs trp_hired_assassin, trp_belligerent_drunk, trp_musican_male`, `scene_setup 95% behaviour profile of the closure`

<a id="popfief-heartbeat-problems"></a>
### Fief 'heartbeat' problems (steward summons to solve local crises) — pop (`pop.fief_heartbeat_problems`)

**What it does:** Every few days one of the player's fiefs may develop a problem (rats, flood, curse/witch, clan blood-feud, horse thieves, wolves, refugees, fire, poisoned wells, captured heretic, cult spies, shrine dispute, disease, mercenaries asking for work, thieves, castle repairs, deserters, trade-route petitions). A messenger summons the player; he can ride there and choose one of four responses, pay 500 denars to have it handled remotely, or ignore it and lose honour, morale and village relation.

**How it works:** strig:20 (every 96h, 50% chance) picks a random center led by the player (get_number_of_hero_centers / troop_get_leaded_center_with_index), stores a problem id 1-13 in party slot 296 and raises menu_heartbeat_quest via add_notification_menu (or just a log line if $notif_village_help=1). menu:heartbeat_quest offers accept / pay 500 (clears slot 296) / decline (-1 honour, -5 party morale, -5 center relation, clears slot). When the player talks to the elder or seneschal of that fief, dlg:1065 (start state) fires if slot 296>=1, shows a random intro string, dlg:1066-1067 state the problem (str_heartbeat_problem_statement_N + variants a-d) and dlg:1068-1071 offer four responses that call pop3_heartbeat_resolve(choice, problem). The 2056-statement resolver rolls success against the player's skill 7 and the steward's skills 15/22/7/8 plus bonuses from built improvements it reads up front (party slots 250 herbalist, 257 hunting lodge, 259 sheriff, 265 church, 267 fire brigade, 270 shrine, 274 training grounds, 276 hospital, 278 cathedral, 283 well cleaners, 286 thieves guild, 287 town crier, 288 civic patrols, 289 knighthood chapter) and applies prosperity, gold, relation (center/faction/troop), renown, honour and morale changes, sometimes spawning parties (looters, heretics, mercenaries).

- **Hooks:** `strig:20`, `menu:heartbeat_quest`, `dlg:1065:dlga_start:heartbeat_intro_response_1:cond`, `dlg:1068:dlga_heartbeat_problem_selection:close_window:conseq`, `dlg:1069:dlga_heartbeat_problem_selection:close_window:conseq`, `dlg:1070:dlga_heartbeat_problem_selection:close_window:conseq`, `dlg:1071:dlga_heartbeat_problem_selection:close_window:conseq`
- **Scripts:** `pop3_heartbeat_resolve`, `pop3_heartbeat_offset`, `pop_commoner_talk`, `get_message_color`, `change_center_prosperity`, `change_player_relation_with_center`, `change_player_honor`, `change_player_party_morale`
- **Menus:** `menu_heartbeat_quest`, `menu_test_heartbeat`, `menu_center_income_report`
- **Dialogs:** `dlg:1065`, `dlg:1066`, `dlg:1067`, `dlg:1068`, `dlg:1069`, `dlg:1070`, `dlg:1071`
- **Slots:** `party:296`, `party:293`, `party:250`, `party:257`, `party:259`, `party:265`, `party:267`, `party:270`, `party:274`, `party:276`, `party:278`, `party:283`, `party:286`, `party:287`, `party:288`, `party:289`
- **Globals:** `notif_village_help`, `g_notification_menu_var1`, `g_encountered_party`, `g_talk_troop`
- **Module-specific resources:** string: str_heartbeat_intro_1..7, str_heartbeat_intro_response_1..7, str_heartbeat_problem_statement_1..18, str_heartbeat_problem_N_a..d, str_heartbeat_problem_response_N_a..d, str_heartbeat_quest_notif; mesh: mesh_pic_messenger
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis strig:20: random player center -> party_set_slot 296, add_notification_menu menu_heartbeat_quest`, `dis menu:heartbeat_quest opts: pay 500 / decline -1 honour -5 morale -5 relation`, `dis dlg:1065 cond checks party slot 296>=1 for elder/seneschal`, `dis pop3_heartbeat_resolve lines 0-80: reads 14 improvement slots and steward skills`, `slot pop party 296: 8 accesses, all in this system`, `texts: 18 problem statements with a-d variants`
- **Overlaps:** `acan.culture_specific_fief_buildings`, `acan.latifundium_estates`, `acan.settlement_events_epidemics`, `ad457.center_buildings_management`, `ad457.lord_business_build_hire_upgrade`, `ad457.settlement_disasters_epidemics`, `bi.ai_lords_build`, `bi.garrison_building_battle_bonuses`, `bi.roman_public_buildings`, `pop.fief_base_income_and_reports`, `pop.fief_improvements_expanded`, `pop.fief_stewards_with_skills`, `sw.recruit_unlock_buildings`, `vc.extended_center_improvements`

<a id="popfief-improvements-expanded"></a>
### Expanded fief buildings with damage, auto-repair and AI lord construction — pop (`pop.fief_improvements_expanded`)

**What it does:** Villages, castles and towns each get their own long list of buildings (about 38 in total: mine and prospecting, herbalist, market, skilled craftsmen, manor, fish pond, school, watch tower, messenger post, prison tower, winery, hunting lodge, foresters, sheriff, shrine, blacksmith, hospital, university, thieves guild, training grounds, church, cathedral, monastery, chapel, crop rotation, court system, warehouse, guilds, lamplighters, well cleaners, street sweepers, building inspectors, renderers, tax office, fire brigade, town crier, civic patrols, improved roads, sanitation). Buildings add base income and prosperity, can be damaged by war and are repaired over time; AI lords also spend their own wealth building in their fiefs.

**How it works:** get_improvement_details (243 stmts vs Native 32) maps party slots 250-289 to name/description/cost; ranges are per center type (village 250-272, castle 260-275, town 262-288). Slot value 1 = built and working, 2..9 = damaged level. strig:76 (12h) completes construction from Native slots 124/125 (improvement in progress / finish hour) and calls center_base_income_change(center, slot, 1) which adds the building's income/prosperity effect (221 stmts, also called when buildings are damaged in game_event_simulate_battle, village_set_state, peace/truce dialogs). auto_repair_buildings (strig:123, ~weekly) walks damaged buildings: AI fiefs repair by the steward/lord engineering skill (skill 8) per week; player fiefs repair only if Skilled Craftsmen (slot 268) is built and the player can afford 200 x skill denars. random_build_buildings (strig:124, every ~20 days) lets non-player lords (troop slot 11 = wealth) roll to build a missing building, paying 1/5 of the cost. Mines (slot 269) take a prospecting result (get_mineral_value) and give direct income; can be closed by steward dialog (dlg:2294-2296).

- **Hooks:** `strig:76`, `strig:123`, `strig:124`, `menu:center_manage`, `menu:center_improve`, `menu:center_income_report`, `menu:center_construction_report`
- **Scripts:** `get_improvement_details`, `center_base_income_change`, `auto_repair_buildings`, `random_build_buildings`, `get_mineral_value`, `pop2_location_improvements`, `get_center_ideal_prosperity`
- **Menus:** `menu_center_manage`, `menu_center_improve`, `menu_center_income_report`, `menu_center_construction_report`
- **Dialogs:** `dlg:2294`, `dlg:2295`, `dlg:3395`
- **Slots:** `party:250-289`, `party:124`, `party:125`, `party:293`, `party:25`, `troop:11`
- **Globals:** `g_improvements_built`
- **Module-specific resources:** string: qstr_Mine, qstr_Herbalist, qstr_Market, ... ~38 building names and descriptions
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `dis get_improvement_details: 38 slot->name branches with descriptions incl. income/prosperity numbers`, `dis auto_repair_buildings: damaged range 2..9, steward skill 8, Skilled Craftsmen slot 268 gate, 200xskill gold`, `dis random_build_buildings: AI lords pay reg10/5 from troop slot 11`, `dis strig:76: slots 124/125 completion -> center_base_income_change`
- **Overlaps:** `acan.culture_specific_fief_buildings`, `acan.latifundium_estates`, `ad457.center_buildings_management`, `ad457.lord_business_build_hire_upgrade`, `bi.ai_lords_build`, `bi.garrison_building_battle_bonuses`, `bi.roman_public_buildings`, `pop.fief_base_income_and_reports`, `pop.fief_heartbeat_problems`, `pop.fief_stewards_with_skills`, `sw.recruit_unlock_buildings`, `vc.extended_center_improvements`

<a id="swrecruit-unlock-buildings"></a>
### Buildings that unlock special recruits (clone chamber, droid foundry, force temple, rancor pit) — sw (`sw.recruit_unlock_buildings`)

**What it does:** Besides the usual improvements, a player-owned minor planet (village) can build four special facilities; each one adds a recruitment option that sells a faction-appropriate elite or exotic troop (clone troopers, battle droids, force-sensitives, baby rancors) in limited numbers for a high price.

**How it works:** Improvements are the Native village-improvement mechanism (get_improvement_details, build menus, party slot per building) extended with four new slots (e.g. party slot 135 = cloning chamber). Menu options on the minor-planet menu are gated by cf_minorplanet_recruit_*_cond (planet not hostile/looted: slot 35 not 1/2, slot 39 < 1, building slot == 1). minorplanet_recruit_volunteers_* adds min(stock slot 93, free party room, gold/price) of the troop chosen by the planet's faction (e.g. faction 16 -> troop 135, 17 -> 162, else 133), charges 150-170 credits each and empties the stock slot (-1); refresh happens on the normal volunteer refresh.

- **Hooks:** `menu:recruit_clones`, `menu:recruit_force_sensitives`, `menu:recruit_droids`, `menu:recruit_rancors`, `script:get_improvement_details`
- **Scripts:** `cf_minorplanet_recruit_clones_cond`, `cf_minorplanet_recruit_droids_cond`, `cf_minorplanet_recruit_force_sensitives_cond`, `cf_minorplanet_recruit_rancors_cond`, `minorplanet_recruit_volunteers_clones`, `minorplanet_recruit_volunteers_droids`, `minorplanet_recruit_volunteers_force_sensitives`, `minorplanet_recruit_volunteers_rancors`, `get_improvement_details`
- **Menus:** `menu_recruit_clones`, `menu_recruit_force_sensitives`, `menu_recruit_droids_pre`, `menu_recruit_droids`, `menu_recruit_rancors`
- **Slots:** `party:35`, `party:39`, `party:93 (special stock)`, `party:135+ (building flags)`
- **Globals:** `g_droid_foundry_type`
- **Module-specific resources:** troop: clone/droid/force-sensitive/rancor troop lines per faction
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `dis sw cf_minorplanet_recruit_clones_cond (party slots 35/39/135)`, `dis sw minorplanet_recruit_volunteers_force_sensitives (stock slot 93, faction-based troop, 150/170 credits)`, `qstr 'A cloning chamber gives you the chance to recruit clone troopers.' etc. via get_improvement_details`
- **Overlaps:** `acan.culture_specific_fief_buildings`, `acan.latifundium_estates`, `ad457.center_buildings_management`, `ad457.lord_business_build_hire_upgrade`, `bi.ai_lords_build`, `bi.garrison_building_battle_bonuses`, `bi.roman_public_buildings`, `pop.fief_base_income_and_reports`, `pop.fief_heartbeat_problems`, `pop.fief_improvements_expanded`, `pop.fief_stewards_with_skills`, `vc.extended_center_improvements`

<a id="vcextended-center-improvements"></a>
### Expanded fief buildings (church/temple, mead hall, brewery, scriptorium, guild hall, slave market, blacksmith) — vc (`vc.extended_center_improvements`)

**What it does:** Fief owners get many more buildings than Native's six: Christian monastery or church, temple/shrine to the Norse gods, mead hall, brewery, merchants' rest hall, scriptorium, blacksmith and slave market, each with a price and an effect on religion, prosperity, relation, income or the player's learning.

**How it works:** Modified get_improvement_details (77 vs Native 32 stmts) maps improvement ids to names and costs: 130 Mead Hall 8000, 131 Mill 6000, 132 Watchtower 5000, 133 School 9000, 138 Messenger Post 4000, 139 Prison Tower 7000, 134 Christian Monastery 9000, 136 Temple to Odin 9000, 140 Christian Church 14000, 142 Shrine to Norse Gods 14000, 144 Blacksmith 4000, 145 Merchants' Rest Hall 8000, 146 Scriptorium 16000, 143 Slave Market 14000, 141 Brewery 5000. Built via menu:center_manage options (center_build_*). Effects live in other triggers: strig:103 (134/140 push Christian share, 136/142 pagan share, 145 +prosperity, 146 scriptorium may raise the player's reading, 141 raises relation), strig:116 weekly income, slave-market removal menu.

- **Hooks:** `menu:center_manage`, `strig:71`, `strig:103`, `strig:116`
- **Scripts:** `get_improvement_details`
- **Menus:** `menu_center_manage`, `menu_center_improve`
- **Slots:** `party:130-146`
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `dis vc get_improvement_details: id->name->cost table (15 buildings)`, `sqlite blocks: menu:center_manage options center_build_brewery/fish_pond/guilds/herreria/library/manor/religion1-4/slavemarket/...`, `dis vc strig:103 reads 134/136/140/141/142/145/146`
- **Overlaps:** `acan.culture_specific_fief_buildings`, `acan.latifundium_estates`, `ad457.center_buildings_management`, `ad457.lord_business_build_hire_upgrade`, `bi.ai_lords_build`, `bi.garrison_building_battle_bonuses`, `bi.roman_public_buildings`, `pop.fief_base_income_and_reports`, `pop.fief_heartbeat_problems`, `pop.fief_improvements_expanded`, `pop.fief_stewards_with_skills`, `sw.recruit_unlock_buildings`

<a id="vcplayer-refuge"></a>
### Player-built refuge (hideout) that grows into a fortified base — vc (`vc.player_refuge`)

**What it does:** Without owning a fief, the player can build a personal hidden refuge on the map: a base to rest, store troops, hold banquets, hire staff (captain, priest, bard, tavernkeeper, trainer, smith, armorer, barber, cook) and train recruits. The captain can expand it in stages and add jetties so ships can dock there; it can be demolished.

**How it works:** menu_build_refuge_new -> make_lair: relocates p_yourlair near the player, give_center_to_lord(player), enable_party, $lair_on=1, slot 390=0 (construction stage) and resets ten staff globals. menu_player_lair_menus offers hall/mead hall scenes, banquet, rename (prsnt_set_playerlair_name), staff hiring (prsnt_lair_hire_staff), garrison, ships/embark (if slot 241 coastal), demolish (demoler_lairm). Lair captain dialogs (lair_captain_improve*, lair_captain_add_port_*) start upgrades: slot 390 1->2->3->4 timed by slot 399 + strig:113 (every 24h: stage 1->2 once 160 h have passed since slot 399; strig:114 is the parallel later-stage timer, not disassembled); add_jetty_system sets slot 297. Training: trainer staff + strig:121 cf_process_training_fail (up to tier-3 troops). Battles near the refuge use scn_player_hideout_1/3/5 by stage (simple_encounter attack branch).

- **Hooks:** `menu:build_refuge_new/opt:refuge_here:conseq`, `menu:player_lair_menus`, `strig:113`, `strig:121`, `dlg:2083:dlga_lair_captain:lair_captain_improve:cond`, `dlg:2087:dlga_lair_captain:lair_captain_add_port_0:cond`
- **Scripts:** `make_lair`, `remove_lair`, `add_jetty_system`, `cf_process_training_fail`, `texto_refuge_construir`
- **Menus:** `menu_build_refuge_new`, `menu_player_lair_menus`, `menu_demoler_lairm`
- **Presentations:** `prsnt_lair_hire_staff`, `prsnt_set_playerlair_name`
- **Mission templates:** `mst_lair_interior`, `mst_lair_visit`
- **Dialogs:** `dlga_lair_captain`, `dlga_lair_captain_improve3`, `dlga_lair_captain_add_port_2`
- **Slots:** `party:390`, `party:399`, `party:297`, `party:241`
- **Globals:** `lair_on`, `captain_ok`, `hire_priest1`, `hire_trainer1`, `captain_hired_on`, `priest_hired_on`, `trainer_hired_on`, `smith_hired_on`, `armorer_hired_on`, `barber_hired_on`, `cook_hired_on`, `g_trainerlair_training_center`, `g_trainerlair_training_type`, `banquete_refuge`
- **Module-specific resources:** party: p_yourlair; scene: scn_player_hideout_1, scn_player_hideout_3, scn_player_hideout_5
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis vc make_lair: relocate/enable p_yourlair, give_center_to_lord player, staff globals`, `dis vc strig:113: slot 399 + 160 h -> slot 390 1->2`, `sqlite texts mopt menu:player_lair_menus: banquet, rename, hall, mead hall, captain, hire staff, garrison, demolish, ships, embark`, `dis vc menu:simple_encounter attack conseq: refuge stage selects scn_player_hideout_1/3/5`, `Changelog 2.023 'Fix refuge training. Limit it to produce only up to L3 troops'`

<a id="acanlegions-cohorts-army-organisation"></a>
### Unit-based army organisation: standing legions with HQs, cohort-limited party size, unit recruitment and province manpower — acan (`acan.legions_cohorts_army_organisation`)

**What it does:** Armies are built and refilled in whole units ('cohorts': officers, nobles, recruits and mercenaries) instead of single soldiers. How many units a party may hold depends on rank, offices, fiefs and culture. Standing legions exist as permanent parties with a headquarters town and a commander, are refilled from the province's manpower pool and paid from the faction budget. When their HQ falls they relocate.

**How it works:** get_cohort_limit (13 callers) returns the unit cap: towns 381/406, castles 401 (garrison capacity codes); the player 10-25 by $g_rank and emperor status; a legion legate (troop 178) 16-17; an auxiliary prefect (179) 11-12; otherwise 4 plus culture, faction-strength (faction 225), marshal and fiefs bonuses, capped at 25. prsnt:recruit_cohorts / manage_cohorts / manage_cohorts_town let the player hire, refill, dismiss or donate whole units, with building-culture requirements (cf_can_hire_cohort -> get_building_culture) and cost/upkeep lines. cohort_describe_strength_to_s5_and_refil runs periodically (strig:28/58/64/121) for AI and player parties: it counts each unit, buys replacements (game_get_join_cost) from the faction budget (add_to_faction_bugdet) or the lord's wealth, and takes men from the province pools (take_recruits_from_province: party slots 83/84/152). party_update_cohorts writes the unit roster into party slots 10-24 of a lord's party. strig:192 (daily) hires for legions, finds new commanders (find_new_commander_for_legion/aux) and moves a captured HQ (find_new_headquarter_for_legion -> get_closest_walled_center_of_faction, legion_hq_set_banner). Garrisons are kept in units too (cohort_refil_garrison after a capture, update_center_garrison).

- **Hooks:** `strig:28`, `strig:58`, `strig:64`, `strig:121`, `strig:192`, `prsnt:recruit_cohorts/t0`, `prsnt:manage_cohorts/t0`, `prsnt:manage_cohorts_town/t0`, `prsnt:legion_management/t0`, `menu:castle_taken_2`
- **Scripts:** `get_cohort_limit`, `cohort_describe_strength_to_s5_and_refil`, `cohort_refil_garrison`, `cohort_count_troop`, `take_recruits_from_province`, `party_update_cohorts`, `add_cohort_to_party_from_party`, `cohort_remove_from_party`, `cf_can_hire_cohort`, `get_cohort_name_to_s5`, `get_cohort_info_to_s5`, `get_representative_troop_for_cohort`, `display_available_recruits`, `find_new_headquarter_for_legion`, `legion_hq_set_banner`, `get_legion_banner`, `get_troop_headquarter`, `update_center_garrison`, `hire_men_to_kingdom_hero_party`, `get_unit_according_to_subculture`
- **Presentations:** `prsnt_recruit_cohorts`, `prsnt_manage_cohorts`, `prsnt_manage_cohorts_town`, `prsnt_legion_management`, `prsnt_select_legion_command`, `prsnt_select_auxiliar_cohort`, `prsnt_legion_select_hq`, `prsnt_barracks`
- **Slots:** `party:10`, `party:11`, `party:12`, `party:13`, `party:14`, `party:15`, `party:16`, `party:17`, `party:18`, `party:19`, `party:20`, `party:21`, `party:22`, `party:23`, `party:24`, `party:43`, `party:44`, `party:45`, `party:68`, `party:83`, `party:84`, `party:152`, `party:293`, `troop:177`, `troop:178`, `troop:179`, `faction:223`, `faction:225`, `faction:228`
- **Globals:** `g_rank`, `g_is_emperor`, `g_civil_war`, `g_hire_troops_and_controversy`
- **Module-specific resources:** pt: pt_cohors_aux, pt_ala_batavorum, pt_player_aux_inf, pt_player_aux_cav
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `dis acan get_cohort_limit: rank/emperor/legate/aux/fief/culture rules, cap 25`, `explain acan cohort_describe_strength_to_s5_and_refil: texts 'The {reg1}. cohort {s5} is fully manned', 'Refill cost / Upkeep cost', '{reg6} denarii were taken from the imperial treasury'`, `explain acan take_recruits_from_province: party slots 83/84/152`, `explain acan strig:192: 'The headquarter of {s7} in {s5} has been captured. Its new headquarter...'`
- **Overlaps:** `acw.conscription`, `acw.regional_regiment_recruitment`, `ad457.barracks_recruitment_screen`, `ad457.village_reinforcement_marches`, `awoiaf.hold_elite_trainers`, `be.manpower_conscription_dynamic_lords`, `bi.military_academy_upgrades`, `laigle.typed_volunteer_recruitment`, `pop.garrison_and_lord_training`, `pop.noble_recruit_pool`, `tld.town_volunteers_and_reserves`

<a id="acwcolor-guard-flagbearers"></a>
### Colour-guard troops: limit per party and battle spawning — acw (`acw.color_guard_flagbearers`)

**What it does:** About 200 colour-guard (national/regimental flag) troops are tagged; AI parties may keep only one flag-bearer per colour-guard stack and at most two kinds - extras are demoted to the troop they upgraded from. In quick battles each side gets a national and a regimental colour bearer spawned beside its line.

**How it works:** game_start -> initialize_flagbearers sets troop slot 182 = 1 on 206 colour-guard troops. strig:26 (every 48 h) gives lord parties party_upgrade_with_xp ((Trainer skill + 5) x 1000, x1.5 on hard) then refresh_flagbearers(party): check_unique_troops, then for each stack with slot 182, find its pre-upgrade troop (troop_get_upgrade_troop scan) and convert all but one (or all if more than 2 flag stacks) back. strig:103 re-adds large unwounded non-flag stacks so flags stay at the top. spawn_flagbearers (quick_battle templates only) spawns the faction's two colour troops (faction slots 47/48) behind the first infantry agents, agent slot 51 = 1 (excluded from casualty counts).

- **Hooks:** `strig:26`, `strig:103`, `mst:quick_battle_battle/t13:conseq`, `script:game_start`
- **Scripts:** `initialize_flagbearers`, `refresh_flagbearers`, `check_unique_troops`, `spawn_flagbearers`, `check_flagbearer`
- **Slots:** `troop:182`, `faction:47`, `faction:48`, `agent:51`
- **Globals:** `player_custom_faction`, `quick_enemy_faction`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `slot acw troop 182 (206 writes in initialize_flagbearers, readers refresh_flagbearers + strig:103)`, `dis acw refresh_flagbearers, spawn_flagbearers`, `dis acw strig:26 stmts 26-27 / 55-56`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_constants.py 1328; module_mission_templates.py 3327; module_simple_triggers.py 1173/1209`

<a id="acwconscription"></a>
### Conscription after volunteers run out — acw (`acw.conscription`)

**What it does:** When a friendly village or town has no volunteers left, the player can conscript 15-39 civilians as the faction's basic recruit for $28 each, at the cost of -1 relation with the place and -10 party morale; the place then cannot be drafted again until its pool resets.

**How it works:** menu:village/opt:force_recruit_volunteers (cond: pool slot 93 == -1, village not looted/raided (slot 35), not infested (slot 39), faction friendly or player's own, free capacity) -> menu:forced_recruit_volunteers: $temp = random 15-39 capped by capacity and gold/28; troop = faction slot 41 (basic recruit). force_recruit:conseq: change_player_relation_with_center -1, temporarily sets slot 93 = $temp, village_recruit_volunteers_recruit, then slot 93 = -3 (locked), change_player_party_morale -10. Town version (menu:forced_recruit_volunteers_town) uses 25 men and sets slot 92 = -2.

- **Hooks:** `menu:village/opt:force_recruit_volunteers:conseq`, `menu:forced_recruit_volunteers/opt:force_recruit:conseq`, `menu:forced_recruit_volunteers_town/opt:force_recruit:conseq`
- **Scripts:** `village_recruit_volunteers_recruit`, `change_player_relation_with_center`, `change_player_party_morale`
- **Menus:** `menu_forced_recruit_volunteers`, `menu_forced_recruit_volunteers_town`
- **Slots:** `party:93`, `party:92`, `party:35`, `party:39`, `faction:41`
- **Globals:** `temp`, `chosen_troop`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis acw menu:forced_recruit_volunteers + opt cond/conseq`, `dis acw menu:village/opt:force_recruit_volunteers:cond`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_game_menus.py 9066, 10014-10097`
- **Overlaps:** `acan.legions_cohorts_army_organisation`, `acw.regional_regiment_recruitment`, `ad457.barracks_recruitment_screen`, `ad457.village_reinforcement_marches`, `awoiaf.hold_elite_trainers`, `be.manpower_conscription_dynamic_lords`, `bi.military_academy_upgrades`, `laigle.typed_volunteer_recruitment`, `pop.garrison_and_lord_training`, `pop.noble_recruit_pool`, `tld.town_volunteers_and_reserves`

<a id="acwregional-regiment-recruitment"></a>
### Regional named-regiment recruitment ('area of recruitment') — acw (`acw.regional_regiment_recruitment`)

**What it does:** Each town, fort and village offers up to five specific historical regiments (e.g. 21st Ohio, 1st Michigan Sharpshooters, USCT) instead of one culture recruit. The player chooses which regiment to enlist from the shared volunteer pool, and can only recruit while the place is held by its original side. Each lord also has a signature regiment.

**How it works:** game_start -> initialize_special_troops (1835 stmts): 1720 party_set_slot writes fill center slots 374-378 with regiment troop ids, and 110 troop_set_slot write each lord's signature regiment into troop slot 374. menu:town 'Recruit Volunteers' -> menu:recruit_nobles / menu:recruit_volunteers: volunteer count from party slot 93, options recruit_them..recruit_them5/_cavalry/_veteran each read one slot (374-378), require town faction == original faction (party slot 61); town_recruit_volunteers_recruit adds min(pool, free capacity, gold/cost) of $chosen_troop at 28 (infantry) / 78 (faction special, faction slot 43) / 150 (horse-guaranteed troops), then clears the pool (slots 92/93 = -1). Troop slot 374 is read by lord enlistment (freelancer) and by the artillery spawner (cavalry generals bring no guns). [Source] Lords also field their regiment: '#MADSCI RECRUITING' in cf_reinforce_party (module_scripts.py 16234) reinforces a lord party with the lord's signature regiment (troop slot 374) while the lord still serves his original faction, else the faction tier-2 troop, else trp_hired_gun.

- **Hooks:** `menu:town/opt:recruit_nobles:conseq`, `menu:recruit_nobles`, `menu:recruit_volunteers`, `script:game_start`
- **Scripts:** `initialize_special_troops`, `town_recruit_volunteers_recruit`, `village_recruit_volunteers_recruit`, `update_volunteer_troops_in_village`
- **Menus:** `menu_recruit_nobles`, `menu_recruit_volunteers`
- **Slots:** `party:374`, `party:375`, `party:376`, `party:377`, `party:378`, `party:61`, `party:92`, `party:93`, `troop:374`, `faction:43`
- **Globals:** `chosen_troop`
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `dis acw initialize_special_troops (opcode histogram: 1720 party_set_slot, 110 troop_set_slot)`, `dis acw menu:recruit_nobles and opt:recruit_them2:cond/conseq`, `dis acw town_recruit_volunteers_recruit`, `FAQ: 'With the current area of recruitment system, the need for a troop tree has become obsolete'`, `slot acw party 375 (344 writes + 6 menu readers)`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_scripts.py 16234 cf_reinforce_party / ~18011 troop_does_business_in_center ('#MADSCI RECRUITING')`
- **Overlaps:** `acan.legions_cohorts_army_organisation`, `acw.conscription`, `ad457.barracks_recruitment_screen`, `ad457.village_reinforcement_marches`, `awoiaf.hold_elite_trainers`, `be.manpower_conscription_dynamic_lords`, `bi.military_academy_upgrades`, `laigle.typed_volunteer_recruitment`, `pop.garrison_and_lord_training`, `pop.noble_recruit_pool`, `tld.town_volunteers_and_reserves`

<a id="ad457barracks-recruitment-screen"></a>
### Barracks screen: pick exactly which troops to recruit — ad457 (`ad457.barracks_recruitment_screen`)

**What it does:** 'Recruit Volunteers' in towns (and in tribal capitals) opens a barracks screen showing the local culture's units with pictures and stats; the player picks a unit and a count and pays per head. Nobles and commoners are separate recruit pools, elite guard units unlock through story flags, and the screen shows party size, wage and limit. A troop-detail view shows each unit's equipment.

**How it works:** prsnt_barracks (t0 load 1386 stmts; t2 event 66 stmts) opened by menu:town/opt:recruit_volunteers_town_1 and menu:minor_faction_town/opt:recruit_minor_town; builds a list from the centre's culture (fac_culture_* slots) and unlock globals ($g_can_recruit_candidati/domestici/schola/shah_guard/noricum, $g_can_hire_arthurian_knights), splits availability with cf_is_noble ('Available nobles / commoners'), prices via game_get_join_cost, shows calculate_weekly_party_wage and game_get_party_companion_limit; t2 recruits ('Recruit {reg43} troops for {reg44} siliquae') or errors ('There are not enough recruits available!'). prsnt_troop_detail (VC troop_detail_* scripts) shows gear.

- **Hooks:** `menu:town/opt:recruit_volunteers_town_1:conseq`, `menu:minor_faction_town/opt:recruit_minor_town:conseq`, `prsnt:barracks/t0`, `prsnt:barracks/t2`
- **Scripts:** `cf_is_noble`, `game_get_join_cost`, `calculate_weekly_party_wage`, `game_get_party_companion_limit`, `troop_detail_change_screen`, `troop_detail_inventory`, `troop_detail_stats`
- **Presentations:** `prsnt_barracks`, `prsnt_troop_detail`
- **Slots:** `faction:10`, `faction:301`, `faction:302`, `faction:303`, `faction:304`
- **Globals:** `g_can_recruit_candidati`, `g_can_recruit_domestici`, `g_can_recruit_schola`, `g_can_recruit_shah_guard`, `g_can_hire_arthurian_knights`, `current_town`
- **Module-specific resources:** tableau: tab_troop_tree_pic
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `refs ad457 prsnt prsnt_barracks: town + minor town recruit options, troop_detail back-link`, `explain ad457 prsnt:barracks/t0: callees and text 'Available nobles', 'Available commoners', 'Party size ... Party wage ...'`, `explain ad457 prsnt:barracks/t2: 'Recruit {reg43} troops for {reg44} siliquae', 'There are not enough recruits available!'`
- **Overlaps:** `acan.legions_cohorts_army_organisation`, `acw.conscription`, `acw.regional_regiment_recruitment`, `ad457.village_reinforcement_marches`, `awoiaf.hold_elite_trainers`, `be.manpower_conscription_dynamic_lords`, `bi.military_academy_upgrades`, `laigle.typed_volunteer_recruitment`, `pop.garrison_and_lord_training`, `pop.noble_recruit_pool`, `tld.town_volunteers_and_reserves`

<a id="ad457village-reinforcement-marches"></a>
### Garrison reinforcements march in from the fief's villages — ad457 (`ad457.village_reinforcement_marches`)

**What it does:** Instead of soldiers appearing out of thin air in a castle or town, the holder's money buys reinforcements that are raised in the centre's bound villages and walk to the fortress as visible map parties ('X reinforcements'). They can be intercepted. The amount depends on the centre's treasury, difficulty setting and kingdom policy; the troop mix comes from the kingdom's (or the player's chosen culture's) three reinforcement templates.

**How it works:** strig:23 (every ~9 min, rotating $center_to_check over towns/castles) calls prune_prisoners then hire_men_to_center(center). hire_men_to_center (130 stmts): only for lord-owned centres not under siege (party 54 == -1); cost per batch 300/450/600 by game_get_reduce_campaign_ai (player's own kingdom fixed 450, 1 batch); uses faction slots 77/78/79 (Native reinforcement templates; player culture when $g_king_start and $g_player_culture set; special cases for fac_indigenoi castles). For each bound village (party 120 == center, village not looted: party 35 == 0) while half the centre's wealth (party 49) exceeds the cost: reuse or spawn pt_center_reinforcements at the village (party 60 links village -> party), roll 0-99 + clamp(faction slot 304,-3,4): <65 template a, <100 b, else c (fallback 15 x faction slot 41 or trp_manhunter), name '{village} reinf', set faction, party 0=6 (type), 5=target, 123=home village, AI behaviour 1 (travel) to the centre, flag 65536; deduct cost from party 49. Any batches left over use cf_reinforce_party(center) directly (Native-style). strig:82 (every 3h) handles arrival: a pt_center_reinforcements party (type 6) inside its target centre is merged with party_add_party, except stacks of looters or of a hostile foreign culture, which are put in the centre's prison; if the centre changed owner the party is dismissed, if it is in a different centre it is re-routed; the village link (party 60) is cleared.

- **Hooks:** `strig:23`, `strig:82`
- **Scripts:** `hire_men_to_center`, `prune_prisoners`, `cf_reinforce_party`, `party_add_party`
- **Slots:** `party:49`, `party:54`, `party:60`, `party:120`, `party:35`, `party:123`, `party:5`, `party:0`, `faction:77`, `faction:78`, `faction:79`, `faction:41`, `faction:304`
- **Globals:** `center_to_check`, `g_king_start`, `g_player_culture`, `players_kingdom`, `g_excubitors_founded`
- **Module-specific resources:** pt: pt_center_reinforcements, pt_culture_minor_*_reinforcements_a/b/c; string: str_s5_reinf
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis ad457 hire_men_to_center: village loop, spawn_around_party pt_center_reinforcements, party_set_name str_s5_reinf, ai object = centre, wealth slot 49 deduction`, `dis ad457 strig:23: rotating centre, prune_prisoners + hire_men_to_center`, `explain ad457 hire_men_to_center: text 'Reinforcements_from_{s5}'`, `refs ad457 pt pt_center_reinforcements + dis ad457 strig:82 stmts 123-205: arrival merge via party_add_party, hostile stacks to prison, re-route/dismiss`
- **Overlaps:** `acan.legions_cohorts_army_organisation`, `acw.conscription`, `acw.regional_regiment_recruitment`, `ad457.barracks_recruitment_screen`, `awoiaf.hold_elite_trainers`, `be.manpower_conscription_dynamic_lords`, `bi.military_academy_upgrades`, `laigle.typed_volunteer_recruitment`, `pop.garrison_and_lord_training`, `pop.noble_recruit_pool`, `tld.town_volunteers_and_reserves`

<a id="awoiafhold-elite-trainers"></a>
### Paid elite-troop training at great houses — awoiaf (`awoiaf.hold_elite_trainers`)

**What it does:** At ~40 seats (Winterfell/Stark, Karstark, Bolton, Lannister, Casterly, Frey, Riverrun, Pyke, King's Landing, Braavos, Volantis, Qohor, Thenn, giants beyond the Wall...) a trainer offers to raise a company of that house's elite soldiers for a lump sum (5,000 stags in both houses checked, Stark and Lannister). Two weeks later the player returns and receives a company of that house's recruits (40 in both houses checked).

**How it works:** Each house has a pair of globals <house>_train / next_recruit_time_<house> (40 pairs). Trainer dialog condition checks gold >= price and sets next_recruit_time = now + 336h; consequence sets <house>_train = 1 and removes gold. A later greeting (cond: hours >= next_recruit_time) adds 40 of the house's recruit troop (e.g. party_add_members p_main_party trp_north_stark_recruit 40) and resets the timer. Separate event menus (menu_special_wildling_recruitment via strig:4, menu_special_dorne_recruitment) offer unique units (giants) when renown is high.

- **Hooks:** `dlg:634:dlga_start:stark_trainer_lord:cond`, `dlg:641:dlga_start:stark_trainer_lord.1:cond`, `strig:4`
- **Menus:** `menu_special_wildling_recruitment`, `menu_special_dorne_recruitment`
- **Dialogs:** `dlga_stark_trainer_lord`, `dlga_start:stark_trainer_lord.1`
- **Globals:** `stark_train`, `next_recruit_time_stark`, `lannister_train`, `next_recruit_time_lannister`, `bolton_train`, `giant_amount`, `bloodrider_train`, `thenn_elite_guard_train`
- **Module-specific resources:** troop: trp_north_stark_recruit, per-house recruit troops
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `global awoiaf stark_train / next_recruit_time_stark: writers/readers are the stark_trainer_lord dialogs`, `dis dlg:639 cond (gold>=5000, timer = now+336) / conseq (stark_train=1, remove 5000)`, `dis dlg:641 conseq: party_add_members p_main_party trp_north_stark_recruit 40`, `dis dlg:678/680 (Lannister): same 5000 price, +336h, trp_westerlands_lannister_recruit x40`, `sqlite: 40 globals named *_train in awoiaf`, `refs menu_special_wildling_recruitment <- strig:4`
- **Overlaps:** `acan.legions_cohorts_army_organisation`, `acw.conscription`, `acw.regional_regiment_recruitment`, `ad457.barracks_recruitment_screen`, `ad457.village_reinforcement_marches`, `be.manpower_conscription_dynamic_lords`, `bi.military_academy_upgrades`, `laigle.typed_volunteer_recruitment`, `pop.garrison_and_lord_training`, `pop.noble_recruit_pool`, `tld.town_volunteers_and_reserves`

<a id="becustom-kingdom-troop-editor"></a>
### Custom kingdom troop designer — be (`be.custom_kingdom_troop_editor`)

**What it does:** When the player founds a nation, a presentation lets them design its troop line: spend attribute, skill and weapon-proficiency points on each troop and pick equipment from an allowed list, with running price and weight totals.

**How it works:** prsnt_custom_kingdom_troop / prsnt_custom_troop (t0 235 stmts) / prsnt_custom_troop_item: custom_troop_button_action (726 stmts) applies +/- on attributes, skills and proficiencies against $attribute_points/$skill_points/$weapon_points; get_custom_troop_info / store_custom_troop_info_to_slot stage values in trp_array_a slots 0-34; custom_troop_inventory_* (initialization, change, reset, total_price, total_weight), custom_troop_item_judge and cf_item_can_be_used_by_custom_troop (135) filter items; set_custom_troop_pionts_initialization at game start; set_player_kingdom_init (67 callers) applies the result.

- **Hooks:** `prsnt:custom_troop/t0`, `prsnt:custom_troop/t2`, `prsnt:custom_kingdom_troop/t0`, `prsnt:custom_troop_item/t1`
- **Scripts:** `custom_troop_button_action`, `get_custom_troop_info`, `store_custom_troop_info_to_slot`, `custom_troop_inventory_initialization`, `custom_troop_inventory_change`, `custom_troop_inventory_reset`, `custom_troop_inventory_total_price`, `custom_troop_inventory_total_weight`, `custom_troop_item_judge`, `cf_item_can_be_used_by_custom_troop`, `set_custom_troop_pionts_initialization`, `set_player_kingdom_init`
- **Presentations:** `prsnt_custom_troop`, `prsnt_custom_troop_item`, `prsnt_custom_kingdom_troop`
- **Slots:** `troop:0-34 on trp_array_a (scratch array)`, `troop:162`, `troop:313-317`
- **Globals:** `attribute_points`, `skill_points`, `weapon_points`, `temp_troop`, `current_item`
- **Module-specific resources:** troop: trp_array_a, trp_player_company_types
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `explain be custom_troop_button_action (troop_progression 97 %)`, `explain be prsnt:custom_troop/t0 texts 'Attribute_points', 'Skill_points', 'Weapon_points'`

<a id="beenlistment-service-ranks"></a>
### Enlistment office and rank promotion service — be (`be.enlistment_service_ranks`)

**What it does:** In a town's enlistment office the player can enlist as a soldier or officer of that nation; the player then rides with an assigned lord, fights his battles, wears the issued uniform and rifle, earns service points over time, and is promoted through ranks - NCO at rank 2, independent high-command officer with 40 men at rank 5, and finally marshal at rank 9.

**How it works:** menu_enlistment_office / _select_class / _enlisted(_officer/_soldier). strig:131 (0.1 h): while $pas_enlistment_lord > 0, camera follows and main party is relocated next to the lord's party; if the lord fights, jump to menu_pas_enlistment_menu; if the lord is gone, menu_pas_enlistment_reassign; equipment is overwritten every tick from the rank troop (or, at rank >= 4, the lord) with the faction's current rifle (item slot 1999+rifle type). strig:133 (0.1 h): +1 point, pas_enlistment_get_promotion thresholds 8000/18000/40000/70000/80000/160000/260000/380000/800000; rank 5 detaches the player with 40 troops; rank 9 sets the player as faction marshal (faction slot 8). pas_enlistment_retire, pas_enlistment_get_lord_to_enlist_for_faction.

- **Hooks:** `strig:131`, `strig:133`, `menu:enlistment_office`, `menu:pas_enlistment_menu`, `menu:pas_enlistment_reassign`, `menu:pas_enlistment_promoted`
- **Scripts:** `pas_enlistment_get_promotion`, `pas_enlistment_get_rank_from_renown`, `pas_enlistment_get_rank_name`, `pas_enlistment_get_lord_to_enlist_for_faction`, `pas_enlistment_retire`, `cf_get_faction_rifle_type`
- **Menus:** `menu_enlistment_office`, `menu_enlistment_office_select_class`, `menu_enlistment_office_enlisted`, `menu_pas_enlistment_menu`, `menu_pas_enlistment_reassign`, `menu_pas_enlistment_end_service_no_lords`, `menu_pas_enlistment_promoted`
- **Slots:** `troop:10`, `faction:8`, `faction:817`, `faction:818`, `item:2000-2006`
- **Globals:** `pas_enlistment_lord`, `pas_enlistment_rank`, `pas_enlistment_points`, `pas_enlistment_player_troop`, `pas_enlistment_player_troop_is_cav`, `pas_enlistment_opponent_to_ignore`, `pas_enlistment_opponent_to_ignore_timer`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis be strig:131, strig:133, pas_enlistment_get_promotion`, `explain be menu:pas_enlistment_menu texts 'You became a non-commissioned officer', 'high command officer', 'marshall of {s10}'`
- **Overlaps:** `acan.enlistment_career_events`, `acan.ranks_offices_titles`, `acw.enlistment_contract_career`, `acw.freelancer_extensions`, `ad457.court_offices_and_titles`, `ad457.freelancer_variant`, `bi.freelancer_reassignment`, `laigle.military_rank_career`, `pop.knighthood_order_membership`, `tld.faction_rank_influence`

<a id="benative-campaign-rule-changes"></a>
### Modified-Native campaign rules (recruitment, autocalc, lords, bandits) — be (`be.native_campaign_rule_changes`)

**What it does:** Several Native scripts are rewritten to fit the nation simulation: foreign villages no longer give you regular enemy troops - only your own nation's villages do; elsewhere you get regional irregulars/partisans. Auto-resolved battles and captured centres feed the PAS manpower/reinforcement system; lord party size follows the nation's lord count; bandit spawning is regional; volunteers only refresh from the national pool.

**How it works:** update_volunteer_troops_in_village (44 vs 35 stmts): if the village belongs to the player's kingdom, volunteers are the faction's base troop with random upgrades by relation; otherwise center_get_rebel_troop picks a regional rebel troop (trp_rebel_european1, _balkan1, _turkish1, _indian1, _arab1, _redshirt1 ...) by village culture/position. game_event_simulate_battle (528 vs 396): after a centre falls it calls pas_reinforce_party x3 on the new garrison and pas_faction_end_campaign when a marshal is defeated; recognises pt_pps_rebels. party_get_ideal_size (30 vs 34): from $preferred_ai_party_size and pas_get_faction_ideal_lord_number. create_kingdom_hero_party (22 vs 62): stripped to a plain spawn with generic party name. spawn_bandits (109 vs 178): regional bandit templates (turkish/indian/middleasia/persian/balkan) capped at 150 total. diplomacy_start_war_between_kingdoms (131 vs 86): infamy for wars without casus belli, notifications only for land neighbours. Emptied Native scripts: decide_run_away_or_not, battle_tactic_*, process_player_enterprise, create_village_farmer_party, calculate_castle_prosperities_by_using_its_villages.

- **Hooks:** `script:game_event_simulate_battle (engine)`, `script:update_volunteer_troops_in_village (Native callers)`, `strig:50`
- **Scripts:** `update_volunteer_troops_in_village`, `center_get_rebel_troop`, `game_event_simulate_battle`, `party_get_ideal_size`, `create_kingdom_hero_party`, `spawn_bandits`, `diplomacy_start_war_between_kingdoms`
- **Slots:** `party:92`, `party:93`, `party:26`, `party:580`
- **Globals:** `preferred_ai_party_size`
- **Module-specific resources:** troop: trp_rebel_european1, trp_rebel_polish1, trp_rebel_balkan1, trp_rebel_persian1, trp_rebel_turkish1, trp_rebel_indian1, trp_rebel_redshirt1, trp_rebel_middleasia1, trp_rebel_arab1; pt: pt_turkish_bandits, pt_indian_bandits, pt_middleasia_bandits, pt_persian_bandits, pt_balkan_bandits, pt_pps_rebels
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `dis be update_volunteer_troops_in_village (own-kingdom vs rebel branch)`, `dis be game_event_simulate_battle grep: pas_reinforce_party x3, pas_faction_end_campaign, pt_pps_rebels`, `dis be party_get_ideal_size, create_kingdom_hero_party, spawn_bandits`, `BUG: spawn_bandits stmt 23-24 store pt_persian_bandits and pt_balkan_bandits into the same local :l5, so Persian bandits are not counted toward the 150 cap`

<a id="bifreelancer-reassignment"></a>
### Freelancer: request reassignment to another troop line — bi (`bi.freelancer_reassignment`)

**What it does:** While enlisted in a lord's army, after 14 days the player can ask to be retrained as a different kind of soldier (infantry, archer or cavalry) of the same rank, receiving that troop's equipment.

**How it works:** Dialog lord_request_reassignment (cond: >14 days since quest slot 16 of the freelancer quest, current troop not the faction's tier-1) -> choose type -> cf_freelancer_get_reassign_troop builds a candidate list from a scratch troop's slots (upgrade tree of the faction) filtered by troop_is_guarantee_horse/ranged and cf_freelancer_player_can_upgrade, adds Intelligence/8 extra ranks of choice, picks one -> finish conseq: freelancer_unequip_troop, set $player_cur_troop, faction slot 101, freelancer_equip_troop, notes and quest slots 13/17 (XP to next promotion via freelancer_get_upgrade_xp).

- **Hooks:** `dlg:984:dlga_lord_request_reassignment:lord_request_reassignment_select:cond`, `dlg:992:dlga_lord_request_reassignment_finish:lord_pretalk:conseq`
- **Scripts:** `cf_freelancer_get_reassign_troop`, `freelancer_list_faction_troops`, `freelancer_get_upgrade_xp`, `freelancer_equip_troop`, `freelancer_unequip_troop`, `cf_freelancer_player_can_upgrade`
- **Dialogs:** `dlga_lord_request_reassignment`, `dlga_lord_request_reassignment_select`, `dlga_lord_request_reassignment_finish`
- **Slots:** `faction:101`, `faction:41`
- **Globals:** `player_cur_troop`, `enlisted_lord`, `temp`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `dis bi cf_freelancer_get_reassign_troop`, `dis bi dlg:984 cond and dlg:992 conseq`, `cmp.py bi acw: reassignment scripts op=1.00`
- **Overlaps:** `acan.enlistment_career_events`, `acan.ranks_offices_titles`, `acw.enlistment_contract_career`, `acw.freelancer_extensions`, `ad457.court_offices_and_titles`, `ad457.freelancer_variant`, `be.enlistment_service_ranks`, `laigle.military_rank_career`, `pop.knighthood_order_membership`, `tld.faction_rank_influence`

<a id="bimilitary-academy-upgrades"></a>
### Military academy: pay to upgrade troops in a town — bi (`bi.military_academy_upgrades`)

**What it does:** In your own kingdom's towns with a military academy, a town-menu option opens a screen where you can pay the normal join cost to upgrade soldiers in your party to either of their next troop types, limited by the academy's remaining capacity.

**How it works:** menu:town option town_upgrade (needs party slot 140 >= 1, town of player's kingdom, player or kingdom-owned) shows the capacity and starts prsnt:upgrade_troops. The presentation lists party stacks; picking upgrade path 0/1 (troop_get_upgrade_troop) multiplies game_get_join_cost by count, removes gold, swaps troops (party_remove_members/party_add_members) and writes the reduced capacity back to party slot 140. Building the academy (menu:center_manage center_build_academy) requires a village of that town to have a school (slot 135).

- **Hooks:** `menu:town/opt:town_upgrade:cond`, `menu:town/opt:town_upgrade:conseq`, `prsnt:upgrade_troops/t0`, `prsnt:upgrade_troops/t1`
- **Scripts:** `game_get_join_cost`
- **Menus:** `menu_town`
- **Presentations:** `prsnt_upgrade_troops`
- **Slots:** `party:140`, `party:135`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis bi menu:town/opt:town_upgrade:cond ('Enlist troops in the military academy ({reg12} available)')`, `grep bi: town_upgrade conseq -> start_presentation 49 = prsnt_upgrade_troops`, `dis bi prsnt:upgrade_troops/t1 @39-55 (join cost, troop swap, slot 140 decrement)`, `dis bi menu:center_manage/opt:center_build_academy:cond (school-in-bound-village check)`, `prsnt:upgrade_troops draws troops with Native tableau tab_game_party_window - no custom art needed`
- **Overlaps:** `acan.legions_cohorts_army_organisation`, `acw.conscription`, `acw.regional_regiment_recruitment`, `ad457.barracks_recruitment_screen`, `ad457.village_reinforcement_marches`, `awoiaf.hold_elite_trainers`, `be.manpower_conscription_dynamic_lords`, `laigle.typed_volunteer_recruitment`, `pop.garrison_and_lord_training`, `pop.noble_recruit_pool`, `tld.town_volunteers_and_reserves`

<a id="laigleartillery-park"></a>
### Buy and maintain an artillery park (player and AI lords) — laigle (`laigle.artillery_park`)

**What it does:** The player buys 3-, 6- or 12-pounder gun crews at a nation's Arsenal (inside the capital depot) and can disband them; the party menu reports how many guns you have. AI lords occasionally acquire guns when they reinforce, so enemy armies can field artillery too.

**How it works:** menu:regiment_recruitment (reached from every <nation>_depot 'Arsenal.' option) shows get_cannon_count and offers recruit/disband per caliber, writing party slots 502/503/504. cf_spawn_side_cannons (7 stmts): if a party has < 2 guns, +1 to a random slot 502-504; it is called from hire_men_to_kingdom_hero_party (daily lord reinforcement via strig:22). The counts feed laigle.field_artillery.

- **Hooks:** `menu:regiment_recruitment`, `menu:french_depot/opt:cannon_foundry_entrance:conseq`, `strig:22`
- **Scripts:** `get_cannon_count`, `cf_spawn_side_cannons`, `hire_men_to_kingdom_hero_party`
- **Menus:** `menu_regiment_recruitment`, `menu_french_depot`, `menu_british_depot`, `menu_austria_depot`, `menu_rhine_depot`, `menu_prussian_depot`, `menu_russian_depot`, `menu_polish_depot`, `menu_naples_depot`, `menu_italian_depot`, `menu_dutch_depot`
- **Slots:** `party:502`, `party:503`, `party:504`
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `callers laigle get_cannon_count (13 sites incl. 9 regiment_recruitment option blocks)`, `callers laigle cf_spawn_side_cannons -> hire_men_to_kingdom_hero_party @83`, `dis laigle cf_spawn_side_cannons`
- **Overlaps:** `acw.field_artillery`, `be.field_artillery_batteries`, `laigle.field_artillery`, `nw.crewed_artillery`, `oa1860.scripted_ballistic_hand_cannon`

<a id="laiglestandard-bearers-and-captured-colours"></a>
### Regimental standard bearers and captured enemy colours — laigle (`laigle.standard_bearers_and_captured_colours`)

**What it does:** At a depot you can add a standard-bearer troop for each regiment type in your party. Enemy standards (eagles/colours) picked up in battle can be presented to your lord for honour.

**How it works:** menu:<nation>_depot_troops/opt:recruit_guy calls cf_spawn_flags_in_party (219 stmts): for each regiment troop type present in the party, add the matching flag-bearer troop (trp_french_flag, trp_british_standard_foot, ... ~66 troops); message 'Standard Bearers added' or 'You lack enough troops'. dlg:1256 lord_standard_taken (cond check_for_standards: player carries an enemy itm_standard_*/itm_colours_* item) writes $glory.

- **Hooks:** `menu:french_depot_troops/opt:recruit_guy:conseq`, `dlg:1256:dlga_lord_standard_taken:lord_standard_taken_1:cond`
- **Scripts:** `cf_spawn_flags_in_party`, `check_for_standards`
- **Menus:** `menu_french_depot_troops`
- **Dialogs:** `dlg:1256:dlga_lord_standard_taken`
- **Globals:** `glory`
- **Module-specific resources:** item: itm_standard_french_infantry_eagle, itm_colours_british, itm_colours_russianinfantry; troop: trp_french_flag, trp_british_standard_foot
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `explain laigle cf_spawn_flags_in_party (11 depot callers, 66+ flag troop refs)`, `explain laigle check_for_standards (caller dlg:1256, item refs to standards)`, `global laigle glory: 3 writers, 0 readers`

<a id="laigletyped-volunteer-recruitment"></a>
### Recruit village volunteers as a chosen troop type — laigle (`laigle.typed_volunteer_recruitment`)

**What it does:** When recruiting village volunteers the player chooses what they become - line infantry, light infantry, or more expensive types - instead of always getting the culture's base recruit. Elite types cost more and you get only half as many; some regions supply a special recruit.

**How it works:** menu:recruit_volunteers options (e.g. 'Recruit them as Light Infantry ({reg6} francs)') set $recruit_type 1-4, then village_recruit_volunteers_recruit (42 stmts vs Native 11) picks faction slot 41 (default), 151, 152 or 154 of the village's original faction; party slot 351 == 1 (regional villages) uses faction slot 153 instead; a hard-coded case gives French players Polish lancers in kingdom_7 villages. Types 3/4 halve the count. Cost 10 per man.

- **Hooks:** `menu:recruit_volunteers/opt:recruit_them:conseq`, `menu:recruit_volunteers/opt:recruit_themlight:conseq`
- **Scripts:** `village_recruit_volunteers_recruit`, `update_volunteer_troops_in_village`, `update_volunteer_troops_in_town`, `update_volunteer_troops_in_castle`, `update_volunteer_troops_in_scotland`, `cf_town_castle_recruit_volunteers_cond`
- **Menus:** `menu_recruit_volunteers`, `menu_recruit_volunteers_town`
- **Slots:** `faction:41`, `faction:151`, `faction:152`, `faction:153`, `faction:154`, `party:351`, `party:93`, `party:19`
- **Globals:** `recruit_type`
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `dis laigle village_recruit_volunteers_recruit`, `slot laigle party 351: game_start writes 1 on 9 villages, read by the recruit script`, `auto report: town/castle volunteer scripts are new and called from strig:66`
- **Overlaps:** `acan.legions_cohorts_army_organisation`, `acw.conscription`, `acw.regional_regiment_recruitment`, `ad457.barracks_recruitment_screen`, `ad457.village_reinforcement_marches`, `awoiaf.hold_elite_trainers`, `be.manpower_conscription_dynamic_lords`, `bi.military_academy_upgrades`, `pop.garrison_and_lord_training`, `pop.noble_recruit_pool`, `tld.town_volunteers_and_reserves`

<a id="perisnoconstable-recruiters-and-training"></a>
### Chamberlain, constable recruiters and retainer training — perisno (`perisno.constable_recruiters_and_training`)

**What it does:** The player can appoint a chamberlain who handles money; a constable then sends recruiters to villages that bring recruits to the player's fiefs and trains retainer families over time, with letters announcing results.

**How it works:** g_player_chamberlain is written by dplmc_appoint_chamberlain / dialogs and read in 31 blocks (constable recruit dialogs refuse without a chamberlain). Hourly, strig:150 -> et_process_4hr_party_scanner (542 stmts, 32 callees) -> cf_et_process_dplmc_recruiters (283 stmts) spawns recruiter visits and posts 'A recruiter has brought N recruits to {s13}'. cf_et_process_hhg (74 stmts) advances et_train_hhg_time for trp_player_retainers_* and sends a constable letter.

- **Hooks:** `strig:150`, `dlg:2748:dlga_dplmc_constable_recruit:dplmc_constable_pretalk:cond`, `dlg:2804:dlga_et_train_hhg_finalized:dplmc_constable_pretalk.2:conseq`
- **Scripts:** `dplmc_appoint_chamberlain`, `et_process_4hr_party_scanner`, `cf_et_process_dplmc_recruiters`, `cf_et_process_hhg`, `dplmc_withdraw_from_treasury`
- **Slots:** `troop:400`, `troop:401`, `troop:403`, `troop:404`, `party:238`, `party:239`
- **Globals:** `g_player_chamberlain`, `et_hhg_training_proficiency`, `et_train_hhg_time`, `et_hhg_family`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `global perisno g_player_chamberlain: 5 writers, 31 readers incl. constable recruit dialogs dlg:2748-2750`, `explain perisno cf_et_process_dplmc_recruiters: caller et_process_4hr_party_scanner (strig:150); text 'A recruiter has brought {reg10} recruits to {s13}'`, `explain perisno cf_et_process_hhg: writes et_train_hhg_time; troop refs trp_player_retainers; letter text`

<a id="perisnocustom-troop-reequip"></a>
### Re-equip a soldier from a template and see its quality score — perisno (`perisno.custom_troop_reequip`)

**What it does:** Through dialog the player picks armour, helmet, boots, glove, shield and weapon categories for a custom troop type; the game then assesses the gear and reports a quality percentage per slot (armour, horses, shields, bows) and recalculates the troop's upkeep.

**How it works:** About 37 dialog lines under dlga_custom_troop_reequip_main_menu each call select_equipment_for_a_custom_troop with a category. The 'back' lines call recalculate_upkeep_of_a_custom_troop, which assesses each equipment type and prints '... was assessed. The quality of this soldier is N%'. assess_equipment_of_normal_soldiers is the batch version for ordinary stacks. Equipment is filtered with dplmc_troop_can_use_item.

- **Hooks:** `dlg:7618:dlga_custom_troop_reequip_main_menu:custom_troop_reequip_2:conseq`, `dlg:7657:dlga_custom_troop_reequip_main_menu:custom_troop_reequip_back:conseq`, `dlg:7616:dlga_regular_member_talk:custom_troop_reequip_back:conseq`
- **Scripts:** `select_equipment_for_a_custom_troop`, `recalculate_upkeep_of_a_custom_troop`, `assess_equipment_of_normal_soldiers`, `dplmc_troop_can_use_item`
- **Slots:** `troop:101`, `troop:102`, `troop:103`, `troop:104`, `troop:105`, `troop:106`, `troop:107`, `troop:108`
- **Globals:** `g_talk_troop`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `explain perisno select_equipment_for_a_custom_troop: 421 stmts, 37 direct dialog callers (dlg:7618..), NEW script`, `explain perisno recalculate_upkeep_of_a_custom_troop: 721 stmts, dialog callers dlg:7616/7656/7657/7658; text 'Armor was assessed. The quality of this soldier is {reg1}%'`, `explain perisno assess_equipment_of_normal_soldiers: 342 stmts, item_stats 93%, called from a script`, `slots troop 101-108 written by recalculate_upkeep (explain slots list)`

<a id="popgarrison-and-lord-training"></a>
### Passive training of lord parties and garrisons (with garrison sorting) — pop (`pop.garrison_and_lord_training`)

**What it does:** Every two days AI lords' parties and all non-player garrisons gain free upgrade XP (more on easy campaign AI, less on hard); player fiefs train their garrisons according to the steward's trainer skill and training grounds. Garrisons are re-sorted so the best troops sit at the top of the stack list.

**How it works:** strig:31 (48h): for each active lord (troop slot 2 = 2) with a party (troop slot 10), XP = (trainer skill 17 + 5) x 1000 at 30% chance (35%/x1.5 on campaign AI 0, 25%/x0.5 on 2, player's own kingdom unaffected) via party_upgrade_with_xp. For each center not owned by the player: 3000 XP at the same chance scaling, then pop_sort_garrison. For player centers: XP = (steward trainer skill x 50 + 250) x (1 + clamp(training grounds slot 274, 0..2)) unless slot 349 is set. pop_sort_garrison selection-sorts companion stacks by level and troop slot 169 (power rating), weighting by troop slot 172 (type) and down-weighting special troops, preserving wounded counts.

- **Hooks:** `strig:31`
- **Scripts:** `pop_sort_garrison`
- **Slots:** `troop:2`, `troop:10`, `troop:169`, `troop:172`, `party:7`, `party:293`, `party:274`, `party:349`
- **Globals:** `players_kingdom`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis strig:31: full 71 stmts`, `dis pop_sort_garrison: full 64 stmts`, `options_get_campaign_ai branches seen`, `sqlite: pop_sort_garrison only in pop`
- **Overlaps:** `acan.legions_cohorts_army_organisation`, `acw.conscription`, `acw.regional_regiment_recruitment`, `ad457.barracks_recruitment_screen`, `ad457.village_reinforcement_marches`, `awoiaf.hold_elite_trainers`, `be.manpower_conscription_dynamic_lords`, `bi.military_academy_upgrades`, `laigle.typed_volunteer_recruitment`, `pop.noble_recruit_pool`, `tld.town_volunteers_and_reserves`

<a id="popnoble-recruit-pool"></a>
### Noble recruit pool for the player's kingdom — pop (`pop.noble_recruit_pool`)

**What it does:** When the player rules a kingdom, each week a pool of noble recruits grows from the player's towns and castles (more with a shrine or church, scaled by renown and honour). From the steward's 'war room' the player buys them into his court at 500 denars each (x1, x10 or all) as noble-line troops.

**How it works:** generate_noble_recruits (strig:17, weekly): only if $players_kingdom>0; for each center owned by the player: towns add 0-2, castles 0-1, villages 25% for 1; Shrine (party slot 270) and Church (265) each add 25% for +1; a bonus roll 1..min(6, renown/500 + honour/50 + 1) is added once. Total accumulates in faction slot 70 of fac_player_faction, with a fanfare log message if a center with a knighthood chapter (slot 289) contributed. Consumed by dlg:2370-2376 (pop2_war_room_noble_recruits) which take 500 per recruit and decrement slot 70; the troop type comes from the faction's noble line (s17).

- **Hooks:** `strig:17`, `dlg:2350:dlga_pop2_war_room_menu:pop2_war_room_noble_recruits:cond`, `dlg:2374`, `dlg:2375`, `dlg:2376`
- **Scripts:** `generate_noble_recruits`, `initialize_faction_troop_types_player_kingdom_only`
- **Menus:** `menu_character_report`
- **Dialogs:** `dlg:2350`, `dlg:2370`, `dlg:2373`, `dlg:2374`, `dlg:2375`, `dlg:2376`
- **Slots:** `faction:70`, `party:7`, `party:265`, `party:270`, `party:289`, `troop:7`
- **Globals:** `players_kingdom`, `player_honor`
- **Module-specific resources:** sound: snd_fanfare1
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis generate_noble_recruits: full 79 stmts`, `slot pop faction 70: writer generate_noble_recruits + 3 purchase dialogs, readers war-room dialogs and character_report`, `text: '{reg0} noble recruits have joined your cause'`
- **Overlaps:** `acan.legions_cohorts_army_organisation`, `acw.conscription`, `acw.regional_regiment_recruitment`, `ad457.barracks_recruitment_screen`, `ad457.village_reinforcement_marches`, `awoiaf.hold_elite_trainers`, `be.manpower_conscription_dynamic_lords`, `bi.military_academy_upgrades`, `laigle.typed_volunteer_recruitment`, `pop.garrison_and_lord_training`, `tld.town_volunteers_and_reserves`

<a id="popplayer-founded-order"></a>
### Player-founded knighthood order with customizable, trainable troops — pop (`pop.player_founded_order`)

**What it does:** A ruling player can found a chapter of a knighthood order in one of his fiefs (20-30k denars plus a special item), name it and pick colours, induct ordinary troops into it for gold and prestige, pay to permanently improve the order's knights and sergeants, have a companion drill them for weeks, and upgrade their equipment at an order blacksmith. AI lords of fiefs with a chapter get order knights in their reinforcements.

**How it works:** War-room dialogs off the fief steward (dlg:2350-2431): create_order (dlg:2426) charges 20000/25000/30000 by order type and removes itm_qualis, sets party slot 289 (chapter troop) and prsnt_name_order/randomize_color; train_order_troops (dlg:2418-2422) converts troops for gold and prestige (player troop slot 156); improve_troops (dlg:2413-2414) raises attributes +2 and seven proficiencies +20 on the troop TEMPLATE (trp_player_knight or custom knights 419-425) and backs it up with copy_complete_troop. strig:10 (18h) lets a companion assigned as trainer (troop slot 152 = 9) raise the order troops' attributes/skills toward his own. Equipment upgrades: find_item_to_upgrade / get_item_upgrade_cost_and_time / order_blacksmith_* globals. Persistence: strig:3 (every frame) runs detect_load_restore_custom_troops which, when a dummy troop's inventory slot is empty (fresh load), copies the *_save backups back onto the live order troops. cf_reinforce_party adds 1-3 order knights (and drakes) to lords whose fief has slot 289.

- **Hooks:** `dlg:2351:dlga_pop2_war_room_menu:pop2_war_room_create_order:cond`, `dlg:2426:dlga_pop2_war_room_create_order:pop2_war_room_create_order_after:conseq`, `dlg:2414:dlga_pop2_war_room_improve_troops_response:pop2_war_room_improve_troops_done:conseq`, `dlg:2419`, `dlg:2420`, `dlg:2358:dlga_dismantle_ko_confirm1:pop2_war_room_menu:conseq`, `dlg:472:dlga_member_train_order_3:close_window:cond`, `strig:10`, `strig:18`, `strig:3`
- **Scripts:** `copy_complete_troop`, `copy_inventory`, `detect_load_restore_custom_troops`, `get_knighthood_order_info`, `find_item_to_upgrade`, `get_item_upgrade_cost_and_time`, `prepare_dummy_and_wardrobe_for_upgrade`, `copy_upgrade_to_all_heroes`, `cf_reinforce_party`, `randomize_color`
- **Menus:** `menu_upgrade_screen`, `menu_auto_name_order`, `menu_notification_order_founded`
- **Presentations:** `prsnt_name_order`, `prsnt_order_founded`
- **Dialogs:** `dlg:2350-2431 pop2_war_room_*`, `dlg:440-472 member_train_order_*`
- **Slots:** `party:289`, `troop:156`, `troop:152`, `troop:162`
- **Globals:** `players_order_name_set`, `order_blacksmith_days`, `order_blacksmith_item`, `order_blacksmith_modifier`, `order_stronghold_upgrade_days`, `cko_training_time_var`, `g_presentation_obj_name_order_knight`
- **Module-specific resources:** troop: trp_player_knight, trp_player_sergeant, trp_player_knight_save, trp_player_sergeant_save, trp_custom_knight_1..7(_save), trp_load_detector; item: itm_qualis
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis dlg:2426 conseq: cost tiers 20k/25k/30k + itm_qualis`, `dis dlg:2414 conseq: troop_raise_attribute / proficiency on order troop template + backup`, `dis detect_load_restore_custom_troops + strig:3`, `dis strig:10 head: trainer companion slot 152=9 raises order troop attributes`, `dis cf_reinforce_party 173-184: chapter slot 289 adds order knights to lords`

<a id="tldtown-volunteers-and-reserves"></a>
### Growing town volunteer pools, troop hand-over to towns, and stationed reserves — tld (`tld.town_volunteers_and_reserves`)

**What it does:** Each friendly town keeps its own pool of volunteers that refills daily and slowly gains experience while it waits, so the longer you leave a town alone the more veteran its recruits. The garrison commander lets you hire from it (paying RP), hand surplus soldiers to the town ('strengthen defences') for a refund and rank, and park troops as personal Reserves at your faction's capital or an advance camp and pick them up later.

**How it works:** strig:14 (daily) calls refresh_volunteers_in_town per center: the volunteers party (party slot 66, attached to the town, created by create_volunteers_party, named Volunteers/Reserves by alignment) grows by garrison/10 + 5*player rank with that faction + 10*Leadership, scaled by town slot 26 and per-faction temperament and $tld_volunteers_multi, and receives party_upgrade_with_xp so stacks upgrade over time. Hiring: dlg:261 sets set_mercenary_source_party to that pool; game_get_join_cost prices recruits by level*wage, town slot 26 and friend traits. Giving: dlg:262 opens an exchange with temp party 9 and pays get_party_disband_cost. Reserves: dlg:263 creates/opens the player's reserve party at the capital (troop 0 slot 50) or at the current advance camp (troop 0 slot 309), attached to the center; upkeep for reserves is half wage (make_player_pay_upkeep); when the faction's advance camp moves, strig:58 folds slot-309 reserves back into the capital reserve.

- **Hooks:** `strig:14`, `dlg:261:dlga_player_hire_troop:player_hire_troop_take:conseq`, `dlg:262:dlga_player_hire_troop:player_hire_troop_give:conseq`, `dlg:263:dlga_player_hire_troop:close_window:cond`
- **Scripts:** `refresh_volunteers_in_town`, `create_volunteers_party`, `delete_volunteers_party`, `game_get_join_cost`, `get_party_min_join_cost`, `get_party_disband_cost`, `get_troop_disband_cost`, `party_split_by_faction`, `party_eject_nonfaction`
- **Menus:** `menu:auto_player_garrison`, `menu:upkeep_report`
- **Dialogs:** `dlg:260:dlga_start:player_hire_troop:cond`, `dlg:263:dlga_player_hire_troop:close_window:cond`, `dlg:294:dlga_player_hire_troop_give:player_hire_troop_reunite:cond`
- **Slots:** `party:66`, `party:26`, `party:257`, `troop:50 (player)`, `troop:309 (player)`
- **Globals:** `hiring_from`, `num_hirable`, `cheapest_join`, `tld_volunteers_multi`, `initial_party_value`
- **Module-specific resources:** party: temp party 9
- **Relation to Native:** replaces-native
- **Confidence:** strongly-inferred
- **Evidence:** `dis tld refresh_volunteers_in_town (growth formula, party_upgrade_with_xp)`, `dis tld create_volunteers_party (spawn 255, attach, slot 66, name Volunteers/Reserves)`, `dis tld dlg:261 conseq (set_mercenary_source_party $hiring_from)`, `dis tld dlg:263 cond (troop 0 slot 50 / 309 reserve party)`
- **Overlaps:** `acan.legions_cohorts_army_organisation`, `acw.conscription`, `acw.regional_regiment_recruitment`, `ad457.barracks_recruitment_screen`, `ad457.village_reinforcement_marches`, `awoiaf.hold_elite_trainers`, `be.manpower_conscription_dynamic_lords`, `bi.military_academy_upgrades`, `laigle.typed_volunteer_recruitment`, `pop.garrison_and_lord_training`, `pop.noble_recruit_pool`

<a id="vcrecruitment-permissions"></a>
### Recruiting requires the local lord's permission, which can be revoked — vc (`vc.recruitment_permissions`)

**What it does:** Players cannot freely recruit in other lords' towns and villages: they ask the lord for permission. If the lord's (or the village's) opinion of the player drops too low the permission is revoked with a message; ownership changes also reset it.

**How it works:** Party slot 239 per center = permission state (0 none/allowed-by-default, 1 revoked/denied, 2/3 transient). dlga_reclutar_permiso1 (lord_talk) grants it; strig:161 (every 48h) resets transient states, and when $recruitment_on=0 revokes permission in towns whose lord's relation with the player is < -10 (50%), villages with center relation < -20, or lord relation < -25, printing '{lord} revokes your right to recruit'. give_center_to_lord clears it on new owners. prsnt_vc_submenu_recruits2 writes it from the recruit UI.

- **Hooks:** `strig:161`, `dlg:3123:dlga_reclutar_permiso1:lord_talk:conseq`, `prsnt:vc_submenu_recruits2/t1`
- **Scripts:** `give_center_to_lord`, `troop_get_player_relation`
- **Presentations:** `prsnt_vc_submenu_recruits`, `prsnt_vc_submenu_recruits2`
- **Dialogs:** `dlga_reclutar_permiso1`, `dlga_village_elder_recruit3`, `dlga_village_elder_recruit4_3`
- **Slots:** `party:239`, `party:26`, `party:7`
- **Globals:** `recruitment_on`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis vc strig:161: slot 239 transitions, relation thresholds -10/-20/-25, 'revokes your right to recruit' message`, `slot vc party 239: 41 accesses, writers give_center_to_lord, dlga_reclutar_permiso1, village elder recruit dialogs`, `Changelog 2.024 'player loses permission to recruit in center that gets new owner'`

<a id="acanhousehold-staff"></a>
### Household staff: captured prisoners made cooks and household slaves, with quality affecting feasts, budget and estates — acan (`acan.household_staff`)

**What it does:** A captured prisoner can be assigned as a household cook or household slave. The number of slots grows with renown. Staff quality becomes a 'household modifier' read by feasts, lord conversations, estate rents and imperial corruption.

**How it works:** dlg:9497 prisoner_chat_add_household_slave and prsnt:select_household_slave / household_management call assign_household_slave / assign_household_cook. These copy the prisoner into a household troop (trp_household_slave_1..trp_household_end, trp_household_cook_1), generate a face between keys, name it by culture and copy its inventory, writing troop slot 10. get_cook_limit / get_slave_limit and the renown thresholds cap the count; describe_cook_quality_to_s1 and describe_slave_skills_to_s0 describe them. get_household_modifier (23 callers) turns staff skills into a percentage used by add_to_faction_bugdet, calculate_imperial_corruption, calculate_latifundium_rents, feast and lord-talk conditions.

- **Hooks:** `dlg:9497:dlga_prisoner_chat_add_household_slave`, `prsnt:select_household_slave/t1`, `prsnt:household_management/t0`
- **Scripts:** `assign_household_slave`, `assign_household_cook`, `get_household_modifier`, `get_cook_limit`, `get_slave_limit`, `get_cook_slot_renown_threshold`, `get_slave_slot_renown_threshold`, `describe_cook_quality_to_s1`, `describe_slave_skills_to_s0`, `generate_random_face_between_keys`, `cf_can_assign_troop_as_houshold_cook`, `cf_can_assign_troop_as_houshold_slave`
- **Presentations:** `prsnt_household_management`, `prsnt_select_household_slave`
- **Slots:** `troop:10`, `troop:183`
- **Globals:** `g_talk_agent`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `grep UNKNOWN_op2749 --mods acan: script:assign_household_slave, script:assign_household_cook`, `explain acan get_household_modifier: 23 callers incl. budget, corruption, latifundium`, `explain acan assign_household_slave: troop slot 10, culture names`
- **Overlaps:** `acw.companion_bodyguards_and_disguise`, `bi.town_bodyguards`, `cbl.tavern_mentors`

<a id="acwcompanion-bodyguards-and-disguise"></a>
### Companion bodyguards in towns, villages and castles (with armed disguise when sneaking in) — acw (`acw.companion_bodyguards_and_disguise`)

**What it does:** When the player walks around a town, village, castle or tavern, up to three unwounded companions from the party appear next to him as bodyguards, follow him, fight for him if trouble starts, and are wounded in the party if they fall. If the player sneaks into an enemy town in disguise, he and his companions wear the pilgrim disguise but the player keeps his revolver and cartridges.

**How it works:** Python list `bodyguard_triggers` (module_mission_templates.py 2808-2950), appended to town_default, town_center, village_center, bandits_at_night, visit_town_castle, castle_visit and sneak_caught_fight. (1) ti_after_mission_start (not when $g_mt_mode is tcm_disguised): pick an entry point by context (village elder 11, prison guard 24 in towns/castles, tavern NPC 17), give the entry the player's horse override, add the first 3 unwounded hero stacks of p_main_party as visitors (prison breaks also set troop slot 158 slot_troop_will_join_prison_break), then order division 8 to follow (silently). If $sneaked_into_town: the entry gets af_override_head|body(|horse) with itm_pilgrim_disguise + itm_pilgrim_hood. (2) ti_on_agent_spawn: party heroes join the player's team, division 8, are alarmed, and are placed 1-2 m around the player. (3) ti_on_agent_killed_or_wounded: party_wound_members for a fallen companion. Separate '#madsci escape items' ti_on_agent_spawn triggers (town_center, visit_town_castle, castle_visit, sneak_caught_fight) strip non-disguise gear from the player/companions when sneaked in, and script players_gun re-equips the player's pistol + itm_cartridges_revolver. The leadership/renown formula for the guard count is commented out; it is a fixed 3.

- **Hooks:** `mst:town_default/t14:conseq`, `mst:town_center/t20:conseq`, `mst:village_center/t11:conseq`, `mst:bandits_at_night/t9:conseq`, `mst:visit_town_castle/t9:conseq`, `mst:castle_visit/t12:conseq`, `mst:sneak_caught_fight/t12:conseq`, `mst:town_center/t2:conseq`, `mst:castle_visit/t9:conseq`
- **Scripts:** `players_gun`
- **Mission templates:** `mst_town_default`, `mst_town_center`, `mst_village_center`, `mst_bandits_at_night`, `mst_visit_town_castle`, `mst_castle_visit`, `mst_sneak_caught_fight`
- **Slots:** `troop:158`
- **Globals:** `sneaked_into_town`, `talk_context`, `current_town`, `g_mt_mode`
- **Module-specific resources:** item: itm_pilgrim_disguise, itm_pilgrim_hood, itm_bowie_knife_invisible, itm_cartridges_revolver
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_mission_templates.py 2808-2950 bodyguard_triggers and its 7 attachment points (lines 5442, 5968, 6113, 6190, 6371, 7891, 8478)`, `grep itm_pilgrim_disguise --mods acw --kinds mst -> mission_tpl_entry_add_override_item in town_default/t14, town_center/t20, village_center/t11, bandits_at_night/t9, visit_town_castle/t9, castle_visit/t12, sneak_caught_fight/t12`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_scripts.py 54243 players_gun; '#madsci escape items' blocks at module_mission_templates.py 5548, 6312, 7823, 8388`
- **Overlaps:** `acan.household_staff`, `bi.town_bodyguards`, `cbl.tavern_mentors`

<a id="bitown-bodyguards"></a>
### Companions follow you as bodyguards in towns — bi (`bi.town_bodyguards`)

**What it does:** When you walk around a town, up to 4 of your companions appear in the scene with you as bodyguards; the number grows with Leadership and renown. Can be switched off in the PBOD options.

**How it works:** mst:town_default ti_before_mission_start calls add_player_bodyguards: requires PBOD preference p_main_party slot 83 >= 1 (default 1 in prebattle_set_default_prefs); count = leadership/3 + renown/300 (troop slot 7), max 4; for each NPC companion (troops 651-666) in the party and not a kingdom hero (troop slot 2 occupation != 2, i.e. not a companion who became a lord), add_visitors_to_current_scene at entry 0.

- **Hooks:** `mst:town_default/t1:conseq`
- **Scripts:** `add_player_bodyguards`, `prebattle_set_default_prefs`
- **Mission templates:** `mst_town_default`
- **Slots:** `party:83`, `troop:7`, `troop:2`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis bi add_player_bodyguards`, `roots bi add_player_bodyguards -> mst:town_default/t1:conseq`, `sqlite: no other module has a script of this name`
- **Overlaps:** `acan.household_staff`, `acw.companion_bodyguards_and_disguise`, `cbl.tavern_mentors`

<a id="popcompanion-unique-troop-requests"></a>
### Ask companions or friendly lords to find special troops — pop (`pop.companion_unique_troop_requests`)

**What it does:** The player can ask a companion (or a friendly lord) for help finding soldiers. Depending on a weekly random roll, the NPC offers a few troops tied to his background (e.g. a sword sister, Myst warriors, a D'Shar chieftain) for a price, says to ask again next week, or notes there is no room in the party.

**How it works:** ask_companions_for_unique_troops(npc, kind) uses weekly-refreshed randoms $event_rand_1a/1b (update_event_rand): <30 nothing, else maps each companion/lord to a background troop in reg35 and computes a count in reg36 (1-5 depending on kind); dialog states dlg:1483-1488 quote a cost in reg37, check party space and add the troops on acceptance. Entry from companion talk (dlg:438 member_question_2), companion re-meet/rehire (dlg:547/551/565) and lord talk (dlg:1482).

- **Hooks:** `dlg:438:dlga_member_question_2:ask_companions_for_unique_troops:conseq`, `dlg:547:dlga_companion_recruit_meet_again:ask_companions_for_unique_troops:conseq`, `dlg:551:dlga_companion_recruit_secondchance:ask_companions_for_unique_troops:conseq`, `dlg:1482:dlga_lord_talk_ask_something_2:ask_companions_for_unique_troops:conseq`, `dlg:1486:dlga_ask_companions_for_unique_troops_2:close_window:conseq`
- **Scripts:** `ask_companions_for_unique_troops`, `update_event_rand`
- **Dialogs:** `dlg:438`, `dlg:547`, `dlg:551`, `dlg:565`, `dlg:1482`, `dlg:1483-1488`
- **Globals:** `event_rand_1a`, `event_rand_1b`
- **Module-specific resources:** troop: ~20 companion->troop mappings (trp_sword_sister, trp_myst_warrior, trp_dshar_chieftain, trp_vanskerry_jarl, ...)
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `dis ask_companions_for_unique_troops lines 0-40 and 180-222`, `texts dlg:1483-1488 (offer/cost/no space/next week)`, `explain: 5 dialog callers`

<a id="tldcompanion-catchup-and-promotion"></a>
### Companion catch-up XP and promotion of companions to lords — tld (`tld.companion_catchup_and_promotion`)

**What it does:** Companions who are not in the player's party keep pace by earning XP toward the player's level, so a recruited or rejoining companion is not hopelessly behind. When a faction is losing (low strength and has lost lords), one of its eligible companions may be raised to lordship, getting his own party -- announced by a 'A new hero' event -- and the player can also ask a companion to leave and become a lord.

**How it works:** strig:64 (every 22 h, after the war starts): for companion troops (512-528 and 940-949) not in the party, not dead (troop slot 1 != 16) and not already lords, if level < player level: add_xp_to_troop(level*playerlevel*2/3). Then per faction with displayed strength <= 3500 (enemy) / 2000 (friendly) that has a dead lord, with chance (6000-strength)/6000 one such companion with Leadership >= 1 gets +1 Leadership and promote_companion_to_lord (sets occupation slot 2 = 2, creates a party, equipment, notes) and menu_companion_promoted_event is shown. Dialogs dlg:141-157 (member_promote_lord) and dlg:239-253 (companion_faction_dying) let the player trigger promotion.

- **Hooks:** `strig:64`, `dlg:157:dlga_member_talk:close_window.1:conseq`, `dlg:239:dlga_companion_faction_dying:close_window:conseq`
- **Scripts:** `promote_companion_to_lord`, `create_kingdom_hero_party`, `update_troop_notes`
- **Menus:** `menu:companion_promoted_event`
- **Dialogs:** `dlg:141:dlga_member_promote_lord:member_talk.3:cond`, `dlg:144:dlga_member_promote_lord_leaving:close_window:conseq`, `dlg:234:dlga_event_triggered:companion_faction_demolished:cond`
- **Slots:** `troop:1`, `troop:2`, `troop:59`, `faction:150`, `faction:153`
- **Globals:** `besieged_center_for_menu`, `besieged_by_troop_for_menu`, `besieged_by_faction_for_menu`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis tld strig:64 (catch-up loop add_xp_to_troop; promotion roll, jump_to_menu companion_promoted_event)`, `explain tld promote_companion_to_lord (82 stmts, 6 callers)`

<a id="tldpersistent-injuries-permadeath"></a>
### Persistent battle injuries, healing and optional hero permadeath — tld (`tld.persistent_injuries_permadeath`)

**What it does:** When the player or a companion is knocked out there is a chance of a lasting wound -- maimed leg (-athletics/riding/agility), arm (-20 weapon skills, -2 STR), head (-INT skills), cracked ribs -- that persists until it heals over days (faster with Wound Treatment, healers, or Athelas). Each existing wound raises the chance that the next knockout is fatal if the permadeath options are on; dead companions get a burial mound or pyre on the world map.

**How it works:** Mission triggers on main_hero_fallen / hero wounded (e.g. mst:lead_charge/t195, 1-in-5 with $tld_option_injuries) call injury_routine(troop): random roll over $wound_setting picks a body part; troop slot 1 holds a bitmask (arm 1, leg 2, head 4, chest 8; 16 = dead); the penalty is applied with troop_raise_attribute / troop_raise_proficiency_linear and reversed by healing_routine. Death roll = 10% per existing wound: NPCs (if $tld_option_death_npc) are removed and build_mound_for_dead_hero spawns a map prop near the faction capital; the player (if $tld_option_death_player) goes to menu_death. strig:61 (10 h) heals each companion with chance 15+wound-treatment and the player 30+wound-treatment; town/lord healers (dlg:504-509, 931-936) heal for RP/Influence; Athelas camp item boosts. $trait_check_battle_scarred counts player wounds for the Battle-scarred trait.

- **Hooks:** `mst:lead_charge/t195:conseq`, `strig:61`, `menu:total_defeat`, `menu:total_victory`
- **Scripts:** `injury_routine`, `healing_routine`, `healing_routine_full`, `build_mound_for_dead_hero`, `battle_health_management`, `wounded_hero_cap_mission_health`, `cf_is_troop_in_party_wounded`
- **Menus:** `menu:death`, `menu:camp_action/opt:camp_use_athelas`
- **Mission templates:** `mst_lead_charge`, `mst_besiege_inner_battle_castle`, `mst_castle_attack_walls_defenders_sally`
- **Dialogs:** `dlg:504:dlga_lord_healers_injured_check:lord_healers_injured_heal:cond`, `dlg:505:dlga_lord_healers_wound_check:lord_healers_wound_heal:cond`, `dlg:931:dlga_healers_injured_check:healers_injured_heal:cond`, `dlg:936:dlga_healers_wound_heal:healers_wound_done:conseq`
- **Slots:** `troop:1`, `troop:15`
- **Globals:** `wound_setting`, `healing_setting`, `tld_option_injuries`, `tld_option_death_npc`, `tld_option_death_player`, `trait_check_battle_scarred`
- **Module-specific resources:** item: itm_athelas_reward; menu: menu_death
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis tld injury_routine (bitmask, attribute/proficiency penalties, 10%/wound death, build_mound_for_dead_hero)`, `dis tld healing_routine (inverse bonuses, +10 HP)`, `dis tld strig:61 (healing chances with skl_wound_treatment)`, `explain tld injury_routine: 27 callers, 23 entry points`
- **Overlaps:** `acan.player_health_mortality`, `vc.player_persistent_injuries`

<a id="acanplayer-health-mortality"></a>
### Player health and mortality: sickness accumulates, can be treated, and can kill the character — acan (`acan.player_health_mortality`)

**What it does:** The player has a hidden ill-health score. It rises from wounds, drinking, orgies, disease and hardship, and falls with baths, barbers, herbal remedies and rest at a villa. Each day a very unhealthy character risks a 'Death waits' event; resisting it worsens health, and accepting it ends the game.

**How it works:** change_troop_health (218 callers) adds to troop slot 20 (a sickness score: higher = sicker, so a negative change correctly prints 'Your health increases!'). Healing and harm come from dialogs (barber dlg:3363, witch herbs dlg:2909, slave food/wine dlg:10272, orgies) and menus (baths, villa bath, which require slot 20 >= 600 / < 300). print_health_text_to_s0 describes 'fit and healthy' .. 'so unhealthy that death will strike soon' in prsnt:companion_overview. strig:183 (daily): if slot 20 >= 625, chance (slot-600)/3050 to jump to menu_death_waits. Its options are 'Go away, demon!' (+25 sickness, back to the map) or 'Take her hand' (menu_death, game over).

- **Hooks:** `strig:183`, `menu:death_waits`, `menu:baths/opt:use_bath`, `menu:villa/opt:bath`, `dlg:3363:dlga_barber_curel_2`, `dlg:2909:dlga_witch_talk_1_herbs_10`
- **Scripts:** `change_troop_health`, `print_health_text_to_s0`, `troop_set_training_health_from_agent`, `agent_apply_training_health`
- **Menus:** `menu_death_waits`, `menu_death`, `menu_baths`
- **Presentations:** `prsnt_companion_overview`
- **Slots:** `troop:20`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis acan change_troop_health: troop slot 20 sickness score, negative delta -> 'Your health increases!'`, `dis acan strig:183: ge 625 -> random(0,3050) < slot-600 -> menu_death_waits`, `dis acan menu:death_waits options: answere_1 +25 health / answere_2 jump_to_menu menu_death`, `grep trp_player slot 20: menu:baths, menu:villa bath, dlg barber_talk`
- **Overlaps:** `tld.persistent_injuries_permadeath`, `vc.player_persistent_injuries`

<a id="acwenlistment-contract-career"></a>
### Three-year junior-officer contract, reenlistment bounty and senior-officer promotion thresholds — acw (`acw.enlistment_contract_career`)

**What it does:** Native's mercenary contract becomes a 3-year enlistment with a $600 bounty; at the end of the term the player may reenlist (another $600 and an automatic promotion to 'general' = vassal) or muster out. Requesting promotion early needs a much higher reputation score than Native, and unaffiliated players only receive spontaneous offers at 1,500 renown with 45+ men.

**How it works:** menu:oath_fulfilled/opt:renew_oath:conseq: $mercenary_service_next_renew_day = today + 1095, +600 gold, player_join_faction (vassalage). dlg:1261/1262 lord_ask_enter_service: renown + 5 x relation + 50 x fiefs >= 3000 (Native dlg:1194 uses >= 150). strig:44 (every 32 h, player in no kingdom, not freelancer/king start): invite with a village if renown >= 1500, faction relation >= 0, liege relation >= 0, party >= 45, 50% roll; invite without center if player already owns fiefs (20% roll). Mercenary dialogs reworded to 'contract for three years, bounty of 600 dollars'.

- **Hooks:** `menu:oath_fulfilled/opt:renew_oath:conseq`, `dlg:1261:dlga_lord_ask_enter_service:lord_give_oath_1:cond`, `dlg:1262:dlga_lord_ask_enter_service:lord_give_oath_1.1:cond`, `strig:44`
- **Scripts:** `player_join_faction`, `get_number_of_hero_centers`, `get_poorest_village_of_faction`, `troop_get_player_relation`
- **Menus:** `menu_oath_fulfilled`, `menu_oath_fulfilled_kingdom_3`, `menu_invite_player_to_faction`
- **Slots:** `troop:7`
- **Globals:** `mercenary_service_next_renew_day`, `g_invite_faction`, `g_invite_offered_center`, `players_kingdom`
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `dis acw menu:oath_fulfilled/opt:renew_oath:conseq (1095 days, 600 gold, player_join_faction)`, `dis acw dlg:1262 cond (>= 3000) vs dis native dlg:1194 cond (>= 150)`, `dis acw strig:44 stmt 42 (renown >= 1500)`, `changelog: '1,500 renown to be promoted' is only true for the spontaneous offer (strig:44); asking a general needs a 3000 combined score (renown + 5x relation + 50x fiefs)`, `changelog: reenlistment -> automatic promotion: verified (player_join_faction)`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_simple_triggers.py 1818; module_dialogs.py 14567-14598`, `dev docs/renown requirements.txt (stale values)`
- **Overlaps:** `acan.enlistment_career_events`, `acan.ranks_offices_titles`, `acw.freelancer_extensions`, `ad457.court_offices_and_titles`, `ad457.freelancer_variant`, `be.enlistment_service_ranks`, `bi.freelancer_reassignment`, `laigle.military_rank_career`, `pop.knighthood_order_membership`, `tld.faction_rank_influence`

<a id="acwfreelancer-extensions"></a>
### Freelancer (enlist as a soldier) with ACW extensions — acw (`acw.freelancer_extensions`)

**What it does:** The OSP Freelancer system (enlist in a lord's army as a common soldier, get equipped, paid weekly, promoted along the troop tree, desert/revolt/vacation) - ACW adds enlistment with partisan bands, the lord's signature regiment as the starting troop, weekly bread ration, artillery that spawns for the enlisted lord's battles and a walkable army camp.

**How it works:** dlg:3058 lord_request_enlistment_confirm / dlg:3051 bandit_request_enlistment_confirm -> freelancer_event_player_enlists (troop from lord's troop slot 374 per dlg:3057). strig:101 keeps the player glued to $enlisted_party with its faction music; strig:100 (weekly) pays 10 x troop level, +70 XP, adds bread if < 10 food, opens menu:upgrade_path when XP threshold met (quest slots 13/17 of qst_freelancer_enlisted). strig:104 desertion; menus world_map_soldier, commander_aud, ask_revolt/revolt, ask_desert/desert, upgrade_path. Battle: mst:lead_charge/t28 spawn_cannon_pos2_freelancer for the lord's guns.

- **Hooks:** `dlg:3058:dlga_lord_request_enlistment_confirm:close_window:conseq`, `dlg:3051:dlga_bandit_request_enlistment_confirm:close_window:conseq`, `strig:100`, `strig:101`, `strig:104`, `mst:lead_charge/t28:conseq`
- **Scripts:** `freelancer_event_player_enlists`, `freelancer_equip_troop`, `freelancer_unequip_troop`, `freelancer_event_player_deserts`, `freelancer_event_player_revolts`, `freelancer_event_player_discharge`, `freelancer_event_player_returns`, `cf_freelancer_player_can_upgrade`, `freelancer_attach_party`, `freelancer_detach_party`, `spawn_cannon_pos2_freelancer`
- **Menus:** `menu_world_map_soldier`, `menu_commander_aud`, `menu_ask_revolt`, `menu_revolt`, `menu_ask_desert`, `menu_desert`, `menu_upgrade_path`
- **Slots:** `troop:374`, `quest:13`, `quest:14`, `quest:17`
- **Globals:** `freelancer_state`, `enlisted_party`, `enlisted_lord`, `player_cur_troop`, `enlisted_lord_faction`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `roots acw freelancer_event_player_enlists (lord + bandit dialogs)`, `dis acw strig:100, strig:101`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_scripts.py 46735 party_restore, 46776 get_desert_troops`
- **Overlaps:** `acan.enlistment_career_events`, `acan.ranks_offices_titles`, `acw.enlistment_contract_career`, `ad457.court_offices_and_titles`, `ad457.freelancer_variant`, `be.enlistment_service_ranks`, `bi.freelancer_reassignment`, `laigle.military_rank_career`, `pop.knighthood_order_membership`, `tld.faction_rank_influence`

<a id="awoiafbackground-character-creation"></a>
### Westerosi background character creation (nationality x job x reason x religion x trait) — awoiaf (`awoiaf.background_character_creation`)

**What it does:** A single-screen presentation replaces Native's menu chain for creating the hero: the player picks gender, nationality/build (which sets body type/height), childhood, 14 adult professions (bravo, slave, noble, bard, peasant, merchant, blacksmith, poacher, begging brother, assassin, pirate, Exalted Faceless Man, Sea Raider), reason for adventuring, religion (Seven / Old Gods / R'hllor / Drowned God...) and a trait. Each choice grants attributes, skills, proficiencies, starting gear, renown and honour, and sets faith, literacy and commoner-trust.

**How it works:** prsnt:player_background (t0 load builds the UI and calls update_strings / randomize_background; t1 state-change) -> script:init_char_stat (663 stmts) which reads $character_gender, $character_nationality (selects troop type/skin via troop_set_type and troop slot 171), $background_childhood/_job/_reason/_religion/_trait/_parent, and applies troop_raise_attribute/skill/proficiency, troop_add_item, change_troop_renown, change_player_honor; writes $g_player_faith, $can_read, $commoner_trust, $player_trait, $character_height, troop slot 7 (Native slot_troop_renown: starting renown by social class). Jobs 12 (Exalted Faceless Man) and 13 (Sea Raider) are 'preset' characters: they call set_troop_level then use non-vanilla opcodes 3708 (set attribute), 3707 (set skill), 3709 (set proficiency) to write ABSOLUTE values and 3701/3703/3705 (inferred: zero the unspent skill/attribute/proficiency point pools). Job 11 (Pirate) also uses one 3707 call (skill 26 := 1).

- **Hooks:** `prsnt:player_background/t0`, `prsnt:player_background/t1`
- **Scripts:** `init_char_stat`, `update_strings`, `randomize_background`, `set_troop_level`, `change_player_honor`, `change_troop_renown`
- **Presentations:** `prsnt_player_background`
- **Slots:** `troop:7`, `troop:171`
- **Globals:** `character_gender`, `character_nationality`, `character_height`, `background_childhood`, `background_job`, `background_reason`, `background_religion`, `background_trait`, `background_parent`, `g_player_faith`, `can_read`, `commoner_trust`, `player_trait`, `player_honor`
- **Relation to Native:** replaces-native
- **Confidence:** confirmed
- **Evidence:** `explain awoiaf init_char_stat: sole caller prsnt:player_background/t1; NON-VANILLA OPCODES {3707:54,3708:8,3709:10,3703:2,3705:2,3701:2}`, `dis init_char_stat: op sites at stmt 482 (job 11 branch) and 500-539, 554-592 (job 12 / job 13 branches, each after set_troop_level)`, `strings.txt str_childhood_acolyte..str_job_sea_raider gives job indices: 11 Pirate, 12 Exalted Faceless Man, 13 Sea Raider`, `the other 11 job branches use only vanilla troop_raise_* ops`

<a id="biforaging-skill"></a>
### Foraging party skill reduces food consumption — bi (`bi.foraging_skill`)

**What it does:** A new party skill, Foraging, lets the army live off the land: every 14 hours the party eats less of its stored food depending on the skill level, the terrain (forest/steppe best) and the wealth of nearby villages and towns.

**How it works:** skills.txt reserved slot 28 renamed skl_foraging ('Your men live off the land...'). The Native 14h food simple trigger (strig:57) now calls forage_for_food: get_max_skill_of_player_party(28) -> base by terrain (+4 forest, steppe-forest, desert-forest and bridge terrain; +2 steppe or plain) + for each village/town within 2xskill distance: production slots 205,206,209-213,216,220,232 scaled, +2 if plantation (party 133); multiplied by x1.5 (skill 2+), x2 (5+), x2.5 (8+) or x3 (10), capped at skill x5. The result is subtracted from the number of food units consumed and 'Your men forage from the land, sparing {reg7} of your supplies.' is shown.

- **Hooks:** `strig:57`
- **Scripts:** `forage_for_food`, `consume_food`, `get_max_skill_of_player_party`
- **Slots:** `party:205`, `party:206`, `party:209`, `party:210`, `party:211`, `party:213`, `party:216`, `party:220`, `party:232`, `party:133`
- **Module-specific resources:** skill: skl_foraging (index 28)
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `skills.txt: 'skl_foraging Foraging ... Reduces the food your party eats'`, `dis bi strig:57 @13-27 (forage reduction + message)`, `dis bi forage_for_food`, `same-name awoiaf forage_for_food differs (op ratio 0.56)`

<a id="cbltavern-mentors"></a>
### Tavern mentors: pay to train attributes — cbl (`cbl.tavern_mentors`)

**What it does:** Five mentors sit in the taverns of the five city-state/clan capitals and sell attribute training (Strength, Agility, Intelligence, Charisma, and a 'jack of all trades' option): basic 5,000 denars for +1, advanced 12,500 for +3, intensive 20,000 for +5, for the player or for a companion in the party. Training costs 12/24/36 hours of rest.

**How it works:** update_tavern_itemsellers (run by game_start and strig:68 every 72h) puts trp_tavern_mentor_strength/agility/intelligence/charisma/jack into party slot 102 (tavern item-seller slot) of p_town_44/46/45/43/42 and keeps random item sellers to p_town_1..p_town_41 range. 95 dialog blocks (dlga_start:tavern_mentor_*_talk -> *_introduction -> *_basic/medium/intensive -> *_select) check gold, list eligible heroes with a repeat-for-party-members option (companions: troop range trp_npc1..trp_heroes_end, slot 8 == -1), take the gold, rest_for_hours 12/24/36, troop_raise_attribute by 1/3/5 and finish_mission.

- **Hooks:** `script:update_tavern_itemsellers`, `strig:68`, `dlg:166:dlga_start:tavern_mentor_strength_talk:cond`, `dlg:186:dlga_start:tavern_mentor_agility_talk:cond`, `dlg:206:dlga_start:tavern_mentor_intelligence_talk:cond`, `dlg:226:dlga_start:tavern_mentor_charisma_talk:cond`, `dlg:246:dlga_start:tavern_mentor_jack_talk:cond`
- **Scripts:** `update_tavern_itemsellers`
- **Dialogs:** `dlga_start:tavern_mentor_*_talk`, `dlga_tavern_mentor_*_introduction`, `dlga_tavern_mentor_*_basic_select`, `dlga_tavern_mentor_*_medium_select`, `dlga_tavern_mentor_*_intensive_select`
- **Slots:** `party:102`, `troop:8`
- **Globals:** `$temp`, `$g_leave_town`
- **Module-specific resources:** troop: trp_tavern_mentor_strength, trp_tavern_mentor_agility, trp_tavern_mentor_intelligence, trp_tavern_mentor_charisma, trp_tavern_mentor_jack
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis cbl update_tavern_itemsellers @7-11 sets party slot 102 to the five mentors`, `dlg:174/175/178/179/182/183 strength select blocks: troop_remove_gold 5000/12500/20000, rest_for_hours 12/24/36, troop_raise_attribute +1/+3/+5`, `roots cbl update_tavern_itemsellers: game_start, strig:68`
- **Overlaps:** `acan.household_staff`, `acw.companion_bodyguards_and_disguise`, `bi.town_bodyguards`

<a id="laiglemilitary-rank-career"></a>
### Military rank ladder, purchasable commissions and rank salary — laigle (`laigle.military_rank_career`)

**What it does:** The player enlists with a nation's recruiter or liaison officer and climbs ten ranks (Sergeant to Marshal) by asking a lord for promotion once renown passes thresholds, or by buying Lieutenant/Captain/Major commissions. Rank sets how many troops you may lead, which uniforms you may buy, and a weekly salary.

**How it works:** Dialogs dlg:2779 recruiter_enter_service and dlg:1291-1293 lord_ask_commission (13750 / 37500 / 65000) write $character_rank. dlg:1280 lord_ask_promotion -> promotion_check: renown (troop slot 7 of trp_player) >= 140/250/300/400/500/600/700 raises $character_rank and shows 'You have been promoted to ...'. game_get_party_companion_limit (engine-called) = 10 + 8*leadership + CHA + a rank bonus of 1/10/30/50/70/100/150/200/300/400 (replaces Native's renown term). rank_salary_payment (called from prsnt:budget_report) pays 10..750 per week by rank. Depot uniform options are gated on $character_rank.

- **Hooks:** `dlg:1280:dlga_lord_ask_promotion:lord_ask_promotion_cont:conseq`, `dlg:2779:dlga_liason_talk:recruiter_enter_service:cond`, `prsnt:budget_report/t0`, `script:game_get_party_companion_limit`
- **Scripts:** `promotion_check`, `rank_salary_payment`, `game_get_party_companion_limit`
- **Menus:** `menu_french_depot_uniforms`, `menu_british_depot_uniforms`
- **Presentations:** `prsnt_budget_report`
- **Dialogs:** `dlg:1021:dlga_lord_talk:lord_ask_promotion`, `dlg:1287..1293 lord_ask_comission_*`, `dlg:2776..2783 liason_talk/recruiter_talk`
- **Slots:** `troop:7`
- **Globals:** `character_rank`, `promoted`
- **Module-specific resources:** troop: trp_liaison_french, trp_liaison_british, trp_liaison_rhine, trp_liaison_austrian, trp_liaison_prussian
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `explain laigle promotion_check (caller dlg:1280; texts 'You have been promoted to Marshal!' ...)`, `global laigle character_rank: 11 writers, 61 readers (dialogs, depot uniform conds, companion limit, salary)`, `dis laigle game_get_party_companion_limit`, `dis laigle rank_salary_payment; callers -> prsnt:budget_report/t0`
- **Overlaps:** `acan.enlistment_career_events`, `acan.ranks_offices_titles`, `acw.enlistment_contract_career`, `acw.freelancer_extensions`, `ad457.court_offices_and_titles`, `ad457.freelancer_variant`, `be.enlistment_service_ranks`, `bi.freelancer_reassignment`, `pop.knighthood_order_membership`, `tld.faction_rank_influence`

<a id="perisnoitem-equip-bonuses"></a>
### Special items grant skill bonuses while equipped, with tooltip text — perisno (`perisno.item_equip_bonuses`)

**What it does:** Certain named items (wolf armours, horses, boots, mounts) add skill points such as Spotting, Leadership, Athletics, Trainer or Path-finding while the hero carries them, and the item tooltip says 'While equipped: ... +2 Leadership'.

**How it works:** game_get_skill_modifier_for_troop (engine hook) calls xgm_get_skill_modifier_for_troop_by_items (1167 stmts), which counts specific items in the troop's inventory via get_troop_item_amount and adds modifiers for pathfinding, leadership, ironflesh, foraging, looting, trade, spotting, trainer, athletics, tactics, riding, wound treatment. The tooltip hook game_get_item_extra_text (593 stmts vs 54 in Native) calls cf_xgm_get_item_extra_text (599 stmts), a long chain of item-id tests that build the 'While equipped' lines.

- **Hooks:** `script:game_get_skill_modifier_for_troop`, `script:game_get_item_extra_text`
- **Scripts:** `xgm_get_skill_modifier_for_troop_by_items`, `get_troop_item_amount`, `cf_xgm_get_item_extra_text`, `game_get_item_extra_text`, `game_get_skill_modifier_for_troop`
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `explain perisno xgm_get_skill_modifier_for_troop_by_items: sole caller game_get_skill_modifier_for_troop; callee get_troop_item_amount; 13 skill refs`, `explain perisno cf_xgm_get_item_extra_text: sole caller game_get_item_extra_text; text 'While equipped: Royal Horse | +2 Leadership'`, `explain perisno script:game_get_item_extra_text: MODIFIED Native script 593 vs 54 stmts, 7% similar`, `compare cf_xgm_get_item_extra_text --mods perisno,native: absent in Native`

<a id="tldplayer-traits"></a>
### Earned character traits (Oathkeeper, Berserker, Battle-scarred, ...) — tld (`tld.player_traits`)

**What it does:** The player earns named traits from how they play -- keeping or breaking oaths, giving many battle orders, stealth successes, fighting unarmoured, repeated wounds, killing enemy captains, visiting landmarks, arena wins, despoiling villages. Each trait gives a permanent effect: attribute/skill changes, cheaper recruiting from a people, weekly morale or influence ticks, fewer animal ambushes, and so on, and is announced with a log message and sound.

**How it works:** trp_traits (troop 872) slots 1-26 are 0/1 flags. gain_trait(n) sets the flag, prints 'New trait gained: <title>' (str_trait_title_*) and plays a sound; ~25 cf_gain_trait_* wrappers apply one-off stat changes (e.g. Command Voice +2 CHA, Berserker +2 STR, Battle-scarred -1 CHA +1 Ironflesh). trig:20 (rearms every 90 h) applies periodic effects (Oathkeeper/Reverent/Merciful/Despoiler +2 Influence with the player's faction, Oathbreaker -2; Foe-hammer, Battle-scarred/Fell-beast, Orc-pit champion and Bravery +11% party morale, Accursed/Merciful -10%) and rolls acquisition chances from counters gathered during play ($trait_check_commands_issued x7%, $trait_check_stealth_success x10%, $trait_check_battle_scarred x3% over 15, landmarks visited party slot 300 >= 3 -> Well-travelled). Other traits are granted directly from dialogs/menus (Elf-friend, King's man, Orc-pit champion, Despoiler, Accursed, Blessed). Trait flags are read elsewhere: game_get_join_cost (-25% recruit cost for friend traits), increase_rank (Influence +/-), strig:66 (Animal-fighter avoids ambushes).

- **Hooks:** `trig:20:conseq`, `script:game_get_join_cost`
- **Scripts:** `gain_trait`, `gain_trait_well_travelled`, `cf_gain_trait_command_voice`, `cf_gain_trait_stealthy`, `cf_gain_trait_berserker`, `cf_gain_trait_battle_scarred`, `cf_gain_trait_fell_beast`, `cf_gain_trait_foe_hammer`, `cf_gain_trait_oathkeeper`, `cf_gain_trait_oathbreaker`, `cf_gain_trait_despoiler`, `cf_gain_trait_blessed`, `cf_gain_trait_elf_friend`, `cf_gain_trait_kings_man`
- **Dialogs:** `dlg:1235:dlga_player_upgrade_troll_buy_done:close_window:conseq`
- **Slots:** `troop:1..26 (on trp_traits)`, `party:300 (landmarks)`
- **Globals:** `trait_check_commands_issued`, `trait_check_stealth_success`, `trait_check_unarmored_berserker`, `trait_check_battle_scarred`
- **Module-specific resources:** troop: trp_traits; string: str_trait_title_*, str_trait_desc_*
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis tld gain_trait (troop_set_slot 872, n, 1; display 'New trait gained')`, `dis tld trig:20:conseq (periodic effects + acquisition rolls)`, `dis tld game_get_join_cost (troop_slot_eq 872 1..4 -> x3/4 cost)`, `texts tld str_trait_desc_* (26 descriptions)`
- **Overlaps:** `vc.player_goals`

<a id="vcplayer-goals"></a>
### Player ambitions ('Set goal') with tracked metrics and rewards — vc (`vc.player_goals`)

**What it does:** The player chooses a life goal - raider, warrior, lord, king, expand the realm, or a custom target - and sets sliders for renown, wealth, army size, reputation, marriage etc. The game tracks progress, reports success as an event and grants a goal-specific reward.

**How it works:** prsnt_set_goal (opened by button_open_set_goal_prsnt from the camp/character screens or menus) stores $goal_type and slider targets (goal_slider_values); prsnt_view_current_goal shows progress via view_goal_metric. trig:50 (every 25h) calls set_goal_check_success_event -> set_goal_check_metrics_progress, which tests cf_goal_renown_completed / cf_goal_wealth_completed / cf_goal_armysize_completed / cf_goal_reputation_completed / cf_goal_married_completed / cf_goal_rtr_completed / cf_goal_special_case_lord_king; on success set_goal_rewards: raider = +5 mountain bandits, warrior = +30 to all weapon proficiencies, lord/king/expand call set_goal_lord_reward / set_goal_king_reward / set_goal_expand_reward. update_savegame_to_content_update sets $set_goal_new_game_trigger for old saves.

- **Hooks:** `trig:50:conseq`, `prsnt:set_goal/t1`, `prsnt:view_current_goal/t1`
- **Scripts:** `button_open_set_goal_prsnt`, `set_goal_check_success_event`, `set_goal_check_metrics_progress`, `set_goal_rewards`, `set_goal_lord_reward`, `set_goal_king_reward`, `set_goal_expand_reward`, `cf_goal_renown_completed`, `cf_goal_wealth_completed`, `cf_goal_armysize_completed`, `cf_goal_reputation_completed`, `cf_goal_married_completed`, `cf_goal_rtr_completed`, `cf_goal_special_case_lord_king`, `goal_slider_values`, `view_goal_metric`
- **Presentations:** `prsnt_set_goal`, `prsnt_view_current_goal`
- **Globals:** `goal_type`, `set_goal_new_game_trigger`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis vc set_goal_rewards: $goal_type 1..6 -> custom/raider(+5 trp_mountain_bandit)/warrior(+30 proficiency)/lord/king/expand`, `sqlite calls: trig:50:conseq -> set_goal_check_success_event; cf_goal_* reached from menu4,prsnt1,trig1 (auto report)`, `sqlite texts: str_view_goal_hint_renown 'Renown: you desire fame above all...', str_set_goal_warrior_hint`
- **Overlaps:** `tld.player_traits`

<a id="vcplayer-persistent-injuries"></a>
### Lasting battle wounds on the player (head/face/body), healing and permanent scars — vc (`vc.player_persistent_injuries`)

**What it does:** A heavy blow in any battle can give the player a serious wound to a body location that temporarily costs attribute points. Each day the wound either heals (helped by Wound Treatment) or worsens toward a permanent scar; a wound report and character-screen section list healing wounds and scars, and barbers/physicians in larger towns can cure them for a fee. Can be turned off.

**How it works:** Every SP battle template has a ti_on_agent_hit trigger (e.g. mst:lead_charge/t21, village_attack_bandits/t37, sea_battle/t45 - ~50 templates) that, when $vc_wounds_on=1, the victim is the player and damage >= 20 (scaled by options_get_damage_to_player), rolls 20% and a further check against existing wounds and character level, picks a location from the hit bone (head/face/body), removes attribute points and records them in qst_vc_wounds quest slots: 31-34 = per-location timer (positive = days until permanent, negative = healing), 41-44 = attribute points lost, 51-54 = scars; increments $wounded_today / $total_wounds_ever. strig:133 (every 23.8h) advances each timer using party Wound Treatment x5 %: healed wounds give the attributes back (troop_raise_attribute: slot 41->INT, 42->CHA, 43->STR, 44->AGI); expired ones become permanent scars; posts a Wound Report dialog. store_wound_report builds the text for prsnt_character_screen_main and battle_debrief. Barber dialogs (dlga_barber_cureh_*) test slots 31-34 and cure.

- **Hooks:** `mst:lead_charge/t21:conseq`, `strig:133`, `dlg:2062:dlga_barber_talk:barber_cureh_1:cond`, `prsnt:character_screen_main/t0`
- **Scripts:** `store_wound_report`
- **Menus:** `menu_battle_debrief`
- **Presentations:** `prsnt_character_screen_main`
- **Mission templates:** `mst_lead_charge`, `mst_village_attack_bandits`, `mst_village_raid`, `mst_castle_attack_walls_belfry`, `mst_castle_attack_walls_ladder`, `mst_bandit_lair`, `mst_sea_battle`
- **Dialogs:** `dlga_barber_talk`, `dlga_barber_cureh_1`, `dlga_barber_cureh_3`
- **Slots:** `quest:31-34`, `quest:41-44`, `quest:51-54`
- **Globals:** `vc_wounds_on`, `wounded_today`, `total_wounds_ever`
- **Module-specific resources:** quest: qst_vc_wounds (used as a data store); skill: skl_wound_treatment
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis vc mst:lead_charge/t21:conseq (ti_on_agent_hit): $vc_wounds_on, damage>=20, 20% roll, quest slots 41-44, $total_wounds_ever`, `dis vc strig:133: daily healing vs worsening with skl_wound_treatment*5, troop_raise_attribute on heal, Wound Report dialog_box`, `sqlite slots quest obj qst_vc_wounds: get/set 41-44,51-54 across ~50 templates; barber dialogs test 31-34`, `sqlite refs store_wound_report <- menu:battle_debrief, prsnt:character_screen_main/t2`
- **Overlaps:** `acan.player_health_mortality`, `tld.persistent_injuries_permadeath`

<a id="acanslave-economy"></a>
### Slave economy: prisoners and conquered populations become culture-specific slaves, sold by town slave traders, slavers and special dealers — acan (`acan.slave_economy`)

**What it does:** Captured soldiers and the population of a sacked town are converted into slaves of their culture. Town slave traders, bandit slavers and special dealers buy and sell them. Slaves are then used as estate labour, household staff or for profit, and an edict can tax manumission.

**How it works:** troop_to_slave_mapping (326 stmts) maps any troop to its culture's slave troop (male or female) and is called when prisoners are added (party_prisoners_add_party_prisoners/companions, both modified Native) and from menu:castle_taken_plunder / menu:exterminate_population / strig:92. trig:17 refills slave merchants (refill_slave_merchant -> refill_slave_trader_town / _bandit / _special, troop slots 102-130 as stock), and mst_slave_market / slave_hideout are the visit scenes. count_party_slaves, remove_slaves_from_party, apply_changes_to_slave_trader, get_slave_merchant_troop and menu:camp_make_slaves handle party-side actions. $edict11 (Vicesima libertatis) taxes manumissions in the budget.

- **Hooks:** `trig:17:conseq`, `strig:92`, `menu:castle_taken_plunder`, `menu:exterminate_population`, `menu:camp_make_slaves`
- **Scripts:** `troop_to_slave_mapping`, `refill_slave_merchant`, `refill_slave_trader_town`, `refill_slave_trader_bandit`, `refill_slave_trader_special`, `get_slave_merchant_troop`, `count_party_slaves`, `remove_slaves_from_party`, `apply_changes_to_slave_trader`, `party_prisoners_add_party_prisoners`, `party_prisoners_add_party_companions`
- **Menus:** `menu_camp_make_slaves`, `menu_exterminate_population`
- **Mission templates:** `mst_slave_market`, `mst_slave_hideout`
- **Slots:** `troop:102`, `troop:103`, `troop:104`, `troop:105`, `troop:119`, `troop:125`, `party:18`
- **Globals:** `g_slave_treatment`, `g_slave_manu`, `edict11`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `explain acan troop_to_slave_mapping: 9 callers incl. prisoners-add scripts and plunder menus`, `explain acan trig:17:conseq -> refill_slave_merchant writes troop slots 102-130`, `global acan edict11: 'Vicesima Libertatis Vel Manumissionum' dialogs`
- **Overlaps:** `ad457.village_enslavement_and_repopulation`, `laigle.keep_battlefield_pickups`, `vc.town_plunder_and_slaves`

<a id="awoiaflord-execution-succession"></a>
### Executing captured lords, with honour/relation fallout and royal succession — awoiaf (`awoiaf.lord_execution_succession`)

**What it does:** The player can execute a captured lord from the prisoner chat. The lord dies permanently, his gear is looted, every other lord and kingdom reacts (scaled by the victim's personality and by whether they are his allies or enemies), honour and renown change, and if the victim was a king the highest-renown surviving lord of his faction becomes king; his fiefs pass to his faction (or to the player's rebel faction / no faction if none remains).

**How it works:** dlg:6457 (prisoner_chat_treason_execute) -> kill_prisoner_dialogue($g_talk_troop, faction): troop slot 2 := 1 (dead), slots 55/14 := fac_no_faction, loot_hero_items; base penalty = renown(slot 7)/-33 scaled by reputation type (troop slot 52: x1 martial/quarrelsome/..., /3 or /4 for some, x2 for others); loops all lords and kingdoms applying change_player_relation_with_troop/_faction by allegiance; change_player_honor, change_troop_renown; if faction slot 11 (leader) == victim, picks max-renown living lord of that faction -> faction slot 11 and 'X is the new King'; then give_center_to_faction for each of his centers; remove_troop_from_prison. The dialog also sets quest flags (brog_kills_tywin etc.).

- **Hooks:** `dlg:6457:dlga_prisoner_chat_treason_execute:close_window:conseq`
- **Scripts:** `kill_prisoner_dialogue`, `loot_hero_items`, `change_player_relation_with_troop`, `change_player_relation_with_faction`, `change_player_honor`, `change_troop_renown`, `give_center_to_faction`, `remove_troop_from_prison`
- **Slots:** `troop:2`, `troop:7`, `troop:14`, `troop:52`, `troop:55`, `troop:181`, `faction:11`, `faction:21`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `roots kill_prisoner_dialogue -> dlg:6457 prisoner_chat_treason_execute`, `dis kill_prisoner_dialogue: slot 2:=1, relation loops, faction slot 11 succession with qstr '{s1}_is_the_new_King', give_center_to_faction loop`

<a id="vcprisoner-revolts"></a>
### Prisoner revolts in over-stretched AI parties — vc (`vc.prisoner_revolts`)

**What it does:** Lords, bandits, sea raiders and farmers who carry far more prisoners than guards risk a revolt: the prisoners break free and become a roaming deserter band (with a leader if large), so big prisoner trains don't stay locked up forever.

**How it works:** strig:166 (every 36h) iterates all parties whose type is a lord party (party slot 0 = 13) or whose template is in the looters..kidnapped_girl, sea_raiders_ships..chimney_smoke or village_farmers ranges; if prisoners exceed fighting members by more than 4 (20 for ship raiders) all non-hero prisoner stacks are moved into one or two temp parties, spawned as pt_deserters near the party (sea raiders: near a random coastal point p_battle_stones..p_bjorn_camp), set to fac_deserters, patrol radius 40, and given trp_looter_leader2 if > 25 men. strig:169 (every 20h) then caps/splits oversize deserter parties (removes > 1000, thresholds 190/220/300).

- **Hooks:** `strig:166`, `strig:169`
- **Scripts:** `party_add_party`
- **Slots:** `party:0`
- **Module-specific resources:** pt: pt_deserters; troop: trp_looter_leader2; faction: fac_deserters
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis vc strig:166: prisoners vs guards test, spawn_around_party pt_deserters, party_set_faction fac_deserters, leader if >25`, `dis vc strig:169: deserter size thresholds 190/220/300/1000`
- **Overlaps:** `acw.prisoner_breakouts_and_refugees`, `pop.raid_refugees`

<a id="acwpartisan-bands"></a>
### Named partisan leaders and faction-aligned irregular bands that raid villages — acw (`acw.partisan_bands`)

**What it does:** Historical guerrilla leaders (Mosby, Quantrill, Jim Lane, Witcher...) lead roaming bands named '<Name>'s Raiders/Boys/Brigade/Gang' that respawn while the leader is free. Bushwhackers are kept friendly to the Confederacy and Jayhawkers to the Union; large bands patrol near enemy centers and occasionally raid enemy villages, with a notification if it is the player's.

**How it works:** strig:106 (every 48 h): for each partisan hero (trp_confed_partisan_1 .. trp_historical_figures_end) with 20% chance create_partisan_party (if not captive/in a party): maps the leader's faction to a bandit faction (Confederate -> mountain_bandits/Bushwhackers, Union -> forest_bandits/Jayhawkers, Native -> native_raiders), spawns the matching party template near a home center (get_closest_union/confederate_center), names and icons it, adds the leader. Same trigger resets relations so each bloc stays at 0 (not hostile) with its aligned bandit and commoner factions. strig:107 (hourly): partisan-led bands without a valid target patrol (radius 45) around the closest hostile center; bands > 50 men roll 0.6%/h to raid the closest enemy village within 100 units (ai state 5), and on arrival village_set_state 1 (being raided), party slot 371 = 10-day cooldown (decremented in strig:99), notification if the village belongs to the player.

- **Hooks:** `strig:106`, `strig:107`, `strig:99`, `script:game_start`
- **Scripts:** `create_partisan_party`, `get_closest_union_center`, `get_closest_confederate_center`, `get_closest_hostile_center`, `get_closest_enemy_village`, `party_set_ai_state`, `village_set_state`
- **Menus:** `menu_notification_bandit_raid_started`
- **Slots:** `party:371`, `party:4`, `party:5`, `party:8`, `troop:2`, `troop:8`, `troop:10`
- **Module-specific resources:** pt: pt_mountain_bandits, pt_sea_raiders, pt_steppe_bandits; icon: big_bushwhacker, big_jayhawker; troop: trp_confed_partisan_1.., trp_union_partisan_.., trp_frank_james
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `explain/dis acw create_partisan_party (names '{s1}'s_Raiders' etc.)`, `dis acw strig:106, strig:107`, `changelog: Jayhawker/Bushwhacker camps limited to 20, spawn further west; Witcher reassigned to the partisan faction as 'Witcher's Boys' -> consistent with the name table`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_simple_triggers.py 5041-5160`
- **Overlaps:** `cbl.regional_bandit_spawn_points`, `pop.lord_party_deserters`, `pop.minor_faction_repression_meter`, `pop.renegade_and_merc_warbands`, `pop.unique_signature_heroes`

<a id="cblregional-bandit-spawn-points"></a>
### Bandit spawn points for the new regions — cbl (`cbl.regional_bandit_spawn_points`)

**What it does:** Bandits also appear in the new lands: six extra spawn points (second forest/mountain/taiga/desert points, a third forest point and a third sea-raider point) feed the existing bandit types into the borderlands.

**How it works:** parties.txt inserts p_forest_bandit_spawn_point2 (17,-148), p_mountain_bandit_spawn_point2 (198,69), p_sea_raider_spawn_point_3 (-193,4), p_taiga_bandit_spawn_point2 (142,161), p_forest_bandit_spawn_point3 (219,-141), p_desert_bandit_spawn_point2 (-80,-190) after p_desert_bandit_spawn_point. spawn_bandits (328 stmts; the base module 374) registers them in party-template slot 5 and adds one spawn block per point (cap 16 per template). cbl's spawn_bandits does NOT contain the base module's sea-raider ship and pirate ship spawns (p_ship_raider_spawn_point_1..3), which cbl lacks.

- **Hooks:** `script:spawn_bandits`
- **Scripts:** `spawn_bandits`
- **Slots:** `pt:5`
- **Module-specific resources:** party: p_forest_bandit_spawn_point2, p_mountain_bandit_spawn_point2, p_sea_raider_spawn_point_3, p_taiga_bandit_spawn_point2, p_forest_bandit_spawn_point3, p_desert_bandit_spawn_point2
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `parties.txt parse cbl idx 448-453`
- **Overlaps:** `acw.partisan_bands`, `pop.lord_party_deserters`, `pop.minor_faction_repression_meter`, `pop.renegade_and_merc_warbands`, `pop.unique_signature_heroes`

<a id="poplord-party-deserters"></a>
### Deserter bands splitting off from lords' armies — pop (`pop.lord_party_deserters`)

**What it does:** Weekly, each active non-player-faction lord on the map has a 5% chance that a band of deserters (his faction's recruits, promoted one to three times, sized by player level) appears next to his army.

**How it works:** spawn_deserters (strig:17): cap 8 pt_deserters; for each active lord (troop slot 2 = 2) not in fac_player_supporters_faction whose party (troop slot 10) is not inside a town, 5% -> spawn_around_party radius 4, add 10..(2 x player level + 11) of the faction's tier-1 troop (faction slot 41, Native slot_faction_tier_1_troop), then party_upgrade_with_xp 1,000,000 one to three times.

- **Hooks:** `strig:17`
- **Scripts:** `spawn_deserters`
- **Slots:** `troop:2`, `troop:10`, `faction:41`
- **Module-specific resources:** pt: pt_deserters
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis spawn_deserters (full 29 stmts)`
- **Overlaps:** `acw.partisan_bands`, `cbl.regional_bandit_spawn_points`, `pop.minor_faction_repression_meter`, `pop.renegade_and_merc_warbands`, `pop.unique_signature_heroes`

<a id="popminor-faction-repression-meter"></a>
### Invader-faction strength meter driven by the player's kills — pop (`pop.minor_faction_repression_meter`)

**What it does:** Each hostile minor faction (Snake Cult, Jatu, Mystmountain, Heretics; also Vanskerry, Noldor, Inquisition reported) has a strength score shown in a victory-progress report as Obliterated..Overwhelming. Destroying their armies and warbands lowers the score, which lowers how often they spawn; leaving them alone lets them grow.

**How it works:** determine_victory_conditions_and_text (strig:83 every 42h, strig:84 daily, menu:victory_progress_report) computes for each faction score = 100 + weighted live parties (army 20, warband 3, unique 50, small 1) - weighted parties destroyed by the player (store_num_parties_destroyed_by_player: army 23, warband 4, unique 60) and stores it in faction slot 66; repression_string_info maps it to a word. spawn_snake_cult / spawn_jatu / spawn_mystmountain / spawn_heretics read faction slot 66 (val_max 50) as the percent chance to spawn this tick. strig:84 also flags kingdoms with zero centers/lord parties as defeated (faction slot 21) and clears related invader parties (e.g. Inquisition when D'Shar falls).

- **Hooks:** `strig:83`, `strig:84`, `strig:82`, `menu:victory_progress_report`
- **Scripts:** `determine_victory_conditions_and_text`, `repression_string_info`, `faction_relations_text_reporter`, `spawn_snake_cult`, `spawn_jatu`, `spawn_mystmountain`, `spawn_heretics`
- **Menus:** `menu_victory_progress_report`
- **Slots:** `faction:66`, `faction:20`, `faction:21`
- **Globals:** `inquisition_spawn_region`, `supported_pretender`
- **Module-specific resources:** faction: fac_snake_cult, fac_jatu, fac_mystmountain, fac_heretics; pt: pt_snake_cult(_army/_warband), pt_jatu_army, pt_mystmountain_army, pt_heretics_army, pt_dread_legion, ...
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis determine_victory_conditions_and_text lines 0-50 and 268-298 (formula)`, `slot pop faction 66: writer determine_victory_conditions_and_text/game_start (130), readers 4 spawn scripts`, `dis spawn_snake_cult head: faction_get_slot 66, val_max 50, compare to d100`, `dis strig:84 head`
- **Overlaps:** `acw.partisan_bands`, `cbl.regional_bandit_spawn_points`, `pop.lord_party_deserters`, `pop.renegade_and_merc_warbands`, `pop.unique_signature_heroes`

<a id="poprenegade-and-merc-warbands"></a>
### Level-scaled renegade knight and wandering mercenary warbands — pop (`pop.renegade_and_merc_warbands`)

**What it does:** Every four days the world may spawn a renegade band (renegade knights of a kingdom, outlaw orders, adventurer companies, treasure hunters) near a regional spawn point; their size scales with the player's level. Separately, each nationality of mercenaries (Barclay, Mettenheim incl. Freikorps, Veccavia, Melitine) has a 10% chance per tick to field a company near a training ground, and rarely a named mercenary captain leads it instead.

**How it works:** strig:15 (96h) -> spawn_renegade (679 stmts). A 1-105 roll selects a band type; cap of 24 pt_ren_knights. Composition comes from cf_generate_renegade_troop_amount: with L = min(player level, 40), knights = L/5 + 1..2, squires = L/2 + 3..6, footmen = L + 5..9 (reg16/17/18). Band name depends on whether the kingdom still exists (faction slot 21 = 0 -> 'Sarleon', else 'Eastern' etc.). Some carry captive ladies (party_add_prisoners) as rescue bait. Tail section (after day 10, 10% each): spawns pt_merc_* companies around p_training_ground_1..5 with per-template caps (3/2/4/3/4); 5% of those rolls instead spawn a unique captain party (Rufio, Obrist Heynrich, Verante, Kaspax) if unique_hero_can_spawn allows. Log messages + sounds announce rare spawns.

- **Hooks:** `strig:15`
- **Scripts:** `spawn_renegade`, `cf_generate_renegade_troop_amount`, `unique_hero_can_spawn`
- **Slots:** `faction:21`, `party_template:6`
- **Module-specific resources:** pt: pt_ren_knights, pt_adventurers, pt_fadventurers, pt_merc_barclay, pt_merc_freikorps_mettenheim, pt_merc_mettenheim, pt_merc_veccavian, pt_melitine_medium_spawn, pt_barclay_rufio, pt_mett_obrist, pt_vecc_verante, pt_melitine_kaspax; party: p_color1..5_*_spawn_point, p_training_ground_1..5; troop: 73 PoP troops (knights/squires/renegades)
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis spawn_renegade lines 0-140 and 556-679`, `dis cf_generate_renegade_troop_amount (full)`
- **Overlaps:** `acw.partisan_bands`, `cbl.regional_bandit_spawn_points`, `pop.lord_party_deserters`, `pop.minor_faction_repression_meter`, `pop.unique_signature_heroes`

<a id="acanenlistment-career-events"></a>
### Enlisting as a common soldier: career progress gated by about 30 random service events — acan (`acan.enlistment_career_events`)

**What it does:** The player can enlist in a lord's army as a soldier. They receive the unit's kit and advance through service, but promotion needs points earned from about 30 event menus (drinking, marsh duty, training, temptations, punishments) and drill sessions. Leaving or being discharged returns the player's own gear.

**How it works:** menu:player_attach -> start_freelancing (only in acan, not Caba'drin's Freelancer). It sets $enlisted_party, starts the service quest, and freelancer_add_player_items / freelancer_equip_troop swap the player's gear for the assigned troop's ('The equipment of a {s21}: {s2} is assigned to you'). Progress is quest 16 slots via freelancer_add_progress (67 callers). freelancer_get_event (208 stmts, strig:97) picks the next event menu (menu_freelancer_event_0..10, _1_wine, _marsh, _5_1 ... 33 menus) and freelancer_event_required_for_progess gates promotion. training_freelancer stages drill scenes, end_freelancing / freelancer_unequip_troop restore gear, and agent_reassign_team_freelancer handles battles.

- **Hooks:** `menu:player_attach`, `strig:97`, `menu:freelancer_event_0`, `menu:freelancer_event_10`
- **Scripts:** `start_freelancing`, `end_freelancing`, `freelancer_add_progress`, `freelancer_get_event`, `freelancer_event_required_for_progess`, `freelancer_equip_troop`, `freelancer_add_player_items`, `freelancer_unequip_troop`, `freelancer_remove_player_items`, `training_freelancer`, `agent_reassign_team_freelancer`
- **Menus:** `menu_player_attach`, `menu_freelancer_event_0`, `menu_freelancer_event_1`, `menu_freelancer_event_10`, `menu_freelancer_event_marsh`
- **Mission templates:** `mst_freelancer_mission_bandit`
- **Slots:** `quest:16`, `quest:11`, `party:195`
- **Globals:** `enlisted_party`, `g_stance`, `foragers_a`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `explain acan start_freelancing: menu:player_attach, text 'The equipment of a {s21}: {s2} is assigned to you'`, `explain acan freelancer_get_event: 33 freelancer_event menus, quest 16 slots`
- **Overlaps:** `acan.ranks_offices_titles`, `acw.enlistment_contract_career`, `acw.freelancer_extensions`, `ad457.court_offices_and_titles`, `ad457.freelancer_variant`, `be.enlistment_service_ranks`, `bi.freelancer_reassignment`, `laigle.military_rank_career`, `pop.knighthood_order_membership`, `tld.faction_rank_influence`

<a id="ad457freelancer-variant"></a>
### Freelancer (enlist as a soldier) - 457 AD variant — ad457 (`ad457.freelancer_variant`)

**What it does:** Enlisting under a lord as a common soldier, with weekly pay, promotion choice when eligible, leave, desertion, revolt and capture events, a commander's report and audience menu.

**How it works:** freelancer_event_player_enlists/discharge/vacation/returns/deserts/revolts/captured, cf_freelancer_player_can_upgrade, freelancer_equip_troop; strig:115 (168h, $freelancer_state 1) pays 10 x troop level, +70 xp, bread if low on food and jumps to menu_upgrade_path when promotion XP is reached; trig:55/57 -> menu_world_map_soldier (commander audience, report prsnt_taragoth_lords_report, revolt, desert).

- **Hooks:** `strig:115`, `trig:55:conseq`, `trig:57:conseq`, `trig:54:conseq`, `menu:world_map_soldier`
- **Scripts:** `freelancer_event_player_enlists`, `freelancer_event_player_revolts`, `freelancer_event_player_captured`, `cf_freelancer_player_can_upgrade`, `freelancer_get_upgrade_xp`, `freelancer_equip_troop`
- **Menus:** `menu_world_map_soldier`, `menu_upgrade_path`, `menu_commander_aud`, `menu_ask_revolt`, `menu_ask_desert`, `menu_desert`
- **Presentations:** `prsnt_taragoth_lords_report`
- **Slots:** `quest:13`, `quest:14`, `quest:17`
- **Globals:** `freelancer_state`, `enlisted_party`, `player_cur_troop`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `dis ad457 strig:115: weekly pay/xp and menu_upgrade_path`, `refs ad457 menu menu_world_map_soldier: trig:55/57`
- **Overlaps:** `acan.enlistment_career_events`, `acan.ranks_offices_titles`, `acw.enlistment_contract_career`, `acw.freelancer_extensions`, `ad457.court_offices_and_titles`, `be.enlistment_service_ranks`, `bi.freelancer_reassignment`, `laigle.military_rank_career`, `pop.knighthood_order_membership`, `tld.faction_rank_influence`

<a id="bilegion-mercenary-camps"></a>
### Legion and foreign mercenary camps on the map — bi (`bi.legion_mercenary_camps`)

**What it does:** Twelve fixed camps on the world map (six Roman legions plus Greek, Nubian, Egyptian, Iberian, Kushan and Illyrian mercenaries). Visiting one opens a menu to walk into a camp scene and talk to its commander, who tells its backstory and sells mercenaries through the standard hire screen. Camps restock every 3 days.

**How it works:** game_event_party_encounter jumps to menu 225 (menu_mercenary_camp) for camp parties p_camp_legion_1..p_camp_illyrian (party ids 21-32). Each option checks $g_encountered_party and jumps to scn_roman_camp_1 via mst_visit_town_castle with the commander (trp_heras, demetrios, mnasiboulos, aryesbokhe) at entry 2 and legionaries as set dressing. Dialogs dlga_start:mercenary_recruit -> backstory chains -> mercenary_buy_troops conseq: set_mercenary_source_party $g_talk_troop_party + change_screen_buy_mercenaries. strig:104 (every 72h) and game_start call refresh_mercenary_camp_troops: clears the camp party if it has >50 men, then party_add_template from pt_merc_camp_*_troops.

- **Hooks:** `script:game_event_party_encounter`, `menu:mercenary_camp`, `strig:104`, `dlg:2779:dlga_start:mercenary_recruit:cond`, `dlg:2784:dlga_mercenary_buy_troops:mercenary_buy_troops_2:conseq`
- **Scripts:** `refresh_mercenary_camp_troops`, `game_event_party_encounter`
- **Menus:** `menu_mercenary_camp`
- **Dialogs:** `dlga_start:mercenary_recruit`, `dlga_mercenary_buy_troops:mercenary_buy_troops_2`
- **Module-specific resources:** party: p_camp_legion_1, p_camp_legion_2, p_camp_legion_3, p_camp_legion_4, p_camp_legion_5, p_camp_legion_6, p_camp_greeks, p_camp_nubians, p_camp_egyptian, p_camp_iberian, p_camp_kushan, p_camp_illyrian; pt: pt_merc_camp_legion_1_troops, pt_merc_camp_greek_troops, pt_merc_camp_nubian_troops; troop: trp_heras, trp_demetrios, trp_mnasiboulos, trp_aryesbokhe; scene: scn_roman_camp_1; scene_prop: spr_tent_a, spr_tent_b, spr_oim_chastokol_long, spr_oim_tyn, spr_oim_tyn_spike, spr_410_watch_tower
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis bi refresh_mercenary_camp_troops; strig:104 every 72h`, `grep bi: game_event_party_encounter @69 (jump_to_menu, 225)`, `dis bi menu:mercenary_camp/opt:enter_camp_legion_1_camp:conseq (set_visitor commander, jump_to_scene 56)`, `dis bi dlg:2784 (set_mercenary_source_party + change_screen_buy_mercenaries)`, `names: parties 21-32 p_camp_*, pt 119-130 pt_merc_camp_*`
- **Overlaps:** `pop.king_hired_mercenary_companies`

<a id="perisnofreelancer-guild-contracts"></a>
### Freelancer Guild contracts and deserter bands — perisno (`perisno.freelancer_guild_contracts`)

**What it does:** A guild leader in one town sells contracts: the town pays a sum and groups of freelancers then join the garrison or patrol around a settlement. Freelancers who go rogue spawn as deserters to be defeated, and companies of freelancers can also be hired from the high marshal and constable.

**How it works:** Dialog chain gesprach_town_19_mayor_* explains the guild and collects 5,000 aurums; strig:121 posts 'A group of freelancers joined the garrison of {s8} according to the contract'. str_freerogues and str_defeat_freelancer_deserters describe the rogue spawn; hire dialogs offer 'Freelancers' Cavalry/Infantry Company' for aurums. The spawn and patrol scripts themselves were not traced.

- **Hooks:** `strig:121`, `dlg:1092:dlga_gesprach_town_19_mayor_11:gesprach_town_19_mayor_12:conseq`, `dlg:424:dlga_highmarshal_hire_foreignmercs_1:highmarshal_hire_foreignmercs_4.12:conseq`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `text freelancer --mods perisno: str_group_of_freelancers_joined used by strig:121; str_sign_contract_with_the_leader_of_freelancer_guild used by dlg:1096; dlg 1092-1093 guild explanation`, `text freelancer: dlg:424/425 hire Freelancers' Cavalry/Infantry Company`, `spawn/patrol scripts not traced`

<a id="popking-hired-mercenary-companies"></a>
### Kings hire named mercenary companies that shadow their armies — pop (`pop.king_hired_mercenary_companies`)

**What it does:** Occasionally a king hires a mercenary company (either a famous named company with its own captain, or a generic one) which spawns at his capital, joins his faction and follows/attaches to him. The player's minister can do the same for the player's kingdom, and the player can give the hired company orders. When a center comes under serious threat the company is detached to attack the threat.

**How it works:** cf_reinforce_party (620 stmts vs Native 49) for king parties: from day 2, if the king's troop slot 161 (hired company party) is empty/inactive, 4% chance per reinforcement; picks one of ~14 company options per kingdom (unique_hero_can_spawn gate for named captains, e.g. Griffonsword/Meregan, Ironsword/Kodan, Mettenheim, Veccavia, Barclay, Melitine, Marleons, Snow Lions, Unicorns) else a generic pt_merc_*; generate_mercenary_company(king, leader, template) spawns at the king's party (troop slot 10), sets faction, aggressiveness 6/courage 9/initiative 50, attaches to the king's attached-to party or escorts him (ai_behavior 10), stores the party in troop slot 161 and announces with snd_kinghorn. process_alarms (modified) detaches that company and sends it at an enemy whose strength >=7000 near a center. kt_party_calculate_strength_with_attachments counts attached parties in strength checks. Player side: dlg:611/627 pop_minister_hire_mercs, dlg:3915-3929 player_merc_talk/give_order/dismiss.

- **Hooks:** `strig:27`, `strig:56`, `strig:41`, `dlg:627:dlga_pop_minister_hire_mercs_confirm:minister_pretalk.1:conseq`, `dlg:3929:dlga_player_merc_dismiss:close_window:conseq`, `dlg:3921:dlga_player_merc_give_order:player_merc_give_order_answer:conseq`
- **Scripts:** `cf_reinforce_party`, `generate_mercenary_company`, `unique_hero_can_spawn`, `process_alarms`, `kt_party_calculate_strength_with_attachments`, `kt_party_calculate_strength`, `calculate_player_faction_wage`
- **Presentations:** `prsnt_budget_report`
- **Dialogs:** `dlg:611`, `dlg:627`, `dlg:3915`, `dlg:3916`, `dlg:3921`, `dlg:3926`, `dlg:3928`, `dlg:3929`
- **Slots:** `troop:161`, `troop:10`, `troop:8`, `party_template:6`
- **Module-specific resources:** pt: pt_griffonsword, pt_ironsword, pt_player_merc_generic, pt_player_merc_mettenheim, pt_player_merc_mettenheim_2, pt_player_merc_veccavian, pt_player_merc_barclay, pt_player_merc_melitine, pt_player_merc_marleons, pt_player_merc_snowlions, pt_player_merc_unicorns, pt_player_merc_jatu, pt_merc_generic, pt_merc_singalian, pt_merc_vanskerry; troop: trp_merc_leader_*, trp_hero_meregan, trp_hero_kodan, trp_morcas, trp_timothy; sound: snd_kinghorn
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `dis generate_mercenary_company: full 45 stmts`, `dis cf_reinforce_party lines 185-291: 4% roll, per-king company list, generate_mercenary_company call`, `diff process_alarms native vs pop: strength >=7000 + troop slot 161 detach and ai_behavior 10`, `slot pop troop 161: 26 accesses incl. minister hire/dismiss dialogs and budget_report`, `dis kt_party_calculate_strength_with_attachments: sums attached parties`
- **Overlaps:** `bi.legion_mercenary_camps`

<a id="poporder-chapter-knight-patrols"></a>
### Knight patrols sent out from knighthood chapterhouses — pop (`pop.order_chapter_knight_patrols`)

**What it does:** Fiefs hosting a knighthood order chapter periodically send out small knight patrols ('Errant Knights', 'Questing Lords', 'Order Knights'...) that patrol around the fief under the fief's or the order's colours, sometimes mixed with the order's sergeants. A separate band of mysterious knights roams one region.

**How it works:** spawn_errant_knights (game_start + strig:82 every 16h): for each center, reads its chapter troop (party slot 289) and order faction (faction slot 69 = sergeant troop); per-order probabilities decide whether the patrol flies the order's faction instead of the fief's and whether sergeants join. Global cap 9 pt_errant_knights; spawned around the fief, slot 123 = home, ai patrol radius 5, flag 65536, random knightly name, 4-12 knights or 6-20 knights + 10-25 sergeants. A second block (15%, cap 13) spawns Silvermist/Ebony 'Clandestine Patrol' knights at p_color5_black_spawn_point.

- **Hooks:** `strig:82`, `script:game_start`
- **Scripts:** `spawn_errant_knights`
- **Slots:** `party:289`, `party:123`, `faction:68`, `faction:69`
- **Module-specific resources:** pt: pt_errant_knights; faction: fac_silvermist_knights, fac_ebony_knights
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis spawn_errant_knights lines 0-40, 168-294`, `explain: callers game_start, strig:82`
- **Overlaps:** `pop.sheriff_militia_patrols`, `sw.faction_town_patrols`, `tld.strength_scaled_hosts_and_patrols`

<a id="popsheriff-militia-patrols"></a>
### Sheriff improvement spawns village militia patrols — pop (`pop.sheriff_militia_patrols`)

**What it does:** Villages where the holder has hired a Sheriff periodically send out a named '<Village> Militia Patrol' that patrols a small radius around the village under the village's faction, thinning bandits near home.

**How it works:** spawn_friendlies (21 stmts), called from game_start and strig:17 (weekly): for every village with party slot 259 (Sheriff) = 1, 13% chance, global cap of 9 pt_militia parties; spawn_around_party, set slot 123 to the home village, rename '{s1} Militia Patrol', set faction to the village's, ai_behavior 3 (patrol) radius 5 around the village, and flag 65536. The sheriff also feeds refresh_village_defenders and heartbeat bonuses, and is built via menu:center_manage/opt:center_build_sheriff.

- **Hooks:** `strig:17`, `script:game_start`, `menu:center_manage/opt:center_build_sheriff`
- **Scripts:** `spawn_friendlies`, `refresh_village_defenders`
- **Menus:** `menu_center_manage`
- **Dialogs:** `dlg:3413:dlga_village_elder_talk:village_elder_menu2.1`
- **Slots:** `party:259`, `party:123`
- **Module-specific resources:** pt: pt_militia
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis spawn_friendlies: full 21 stmts read`, `slot pop party 259: writers menu center_build_sheriff, readers spawn_friendlies/refresh_village_defenders/heartbeat`, `improvement text: 'sends out militia patrols'`, `explain: callers game_start, strig:17 (168h)`
- **Overlaps:** `pop.order_chapter_knight_patrols`, `sw.faction_town_patrols`, `tld.strength_scaled_hosts_and_patrols`

<a id="swfaction-town-patrols"></a>
### Automatic faction patrols based at towns (levels 1-3) — sw (`sw.faction_town_patrols`)

**What it does:** Selected towns and stations are patrol bases rated 1-3. Each base keeps two patrol parties of faction troops (15-50 men depending on level) that roam nearby, attack weaker enemies they meet, run home from much stronger ones, and never wander more than a day's ride from base.

**How it works:** strig:90 (once, $total_init_done) -> init_patrol_faction_settings + init_patrol_bases (party slot 800 = level per base via init_patrol_settings). strig:87 (8 h) for bases with level 1-3 and party slot 54 < 0 -> patrol_base_spawn_patrols: count existing pt 13 parties with party slot 123 == base; spawn up to 2 with troop types from faction slots 83/84/85 (15/5, 20/10/5 or 25/15/10 men), set icon by faction, then decide_next_patrol_location. strig:91 (0.5 h) -> process_patrol_ai: within 5 map units of a hostile party, attack if own strength >= 1.25x theirs, else retreat to base if outmatched by 100+; leash: beyond 24 drop the chase, beyond 20 return to a random point near base, under 5 pick a new waypoint. strig:92 (2 h) -> process_patrol_maintenance / patrol_unit_maintenance (top-up, prisoners). Patrol speed in game_get_party_speed_multiplier depends on base level (105/100/110).

- **Hooks:** `strig:87`, `strig:90`, `strig:91`, `strig:92`, `strig:93`
- **Scripts:** `init_patrol_bases`, `init_patrol_settings`, `init_patrol_faction_settings`, `patrol_base_spawn_patrols`, `decide_next_patrol_location`, `process_patrol_ai`, `process_patrol_maintenance`, `patrol_unit_maintenance`, `process_automated_attack_system`
- **Slots:** `party:800 (base level)`, `party:123 (home base)`, `party:54`, `faction:83-85 (patrol troop types)`
- **Globals:** `total_init_done`
- **Module-specific resources:** pt: pt 13 (patrol)
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `explain sw patrol_base_spawn_patrols / process_patrol_ai / process_patrol_maintenance (entry strig:87/91/92)`, `dis sw strig:90, strig:87`, `dis sw patrol_base_spawn_patrols (2 patrols per base, sizes by level)`, `dis sw process_patrol_ai (5/20/24 distance thresholds, 1.25x strength rule)`
- **Overlaps:** `pop.order_chapter_knight_patrols`, `pop.sheriff_militia_patrols`, `tld.strength_scaled_hosts_and_patrols`

<a id="bepas-marshal-campaign-ai"></a>
### PAS lord and marshal AI (direct campaign control) — be (`be.pas_marshal_campaign_ai`)

**What it does:** Replaces Native's lord decision-making with a simpler, direct controller: the marshal starts a campaign when at war, half of the lords follow him, the marshal patrols a threatened home centre or a random border centre of the enemy, attacks targets chosen by faction-level scripts, and ends the campaign when the target is invalid or peace is made. Lords not on campaign patrol near home and keep themselves topped up from manpower.

**How it works:** strig:130 (0.001 h) calls pas_ai_lord_decide for two lords per tick (cursor $async_simple_trigger35 over trp_npc1..trp_knight_1_1_wife). pas_ai_lord_decide (322 stmts): detaches lords sitting in foreign centres, pas_reinforce_party x2 (x5 for marshal), records nearest own centre (party 600); marshal: if at war and pas_faction_get_center_to_defend finds a threatened centre -> 50 % start campaign + patrol it; else start campaign 80 %; campaign states in party slot 581 (0 idle, 3 following marshal, 5/6/7/8 marshal modes) with target party 582 and cooldown 583; faction slot 815 = campaign active. pas_faction_start_campaign: marshal state 8, each idle lord 50 % -> pas_lord_follow_marshall; marshal patrols pas_get_random_war_border_center_for_faction_universal. pas_lord_patrol_center sets party_set_ai_behavior 3 (patrol) with aggressiveness/courage 15, initiative 100, helpfulness 200. pas_faction_end_campaign resets everyone to hold (behavior 2) at current position. Native process_kingdom_parties_ai is gone (async stub empty); npc_decision_checklist_party_ai is still present (99 % Native).

- **Hooks:** `strig:130`, `strig:124 (iteration)`
- **Scripts:** `pas_ai_lord_decide`, `pas_faction_start_campaign`, `pas_faction_end_campaign`, `pas_lord_follow_marshall`, `pas_lord_patrol_center`, `pas_faction_get_center_to_attack`, `pas_faction_get_center_to_defend`, `pas_get_random_border_center_for_faction`, `pas_get_random_war_border_center_for_faction`, `pas_get_random_war_border_center_for_faction_universal`, `cf_pas_if_faction_is_at_war_with_anyone`, `pas_reinforce_party`
- **Slots:** `party:581`, `party:582`, `party:583`, `party:600`, `faction:8`, `faction:815`, `troop:10`
- **Globals:** `async_simple_trigger35`, `g_display_pas_debug_messages`
- **Relation to Native:** replaces-native
- **Confidence:** confirmed
- **Evidence:** `dis be strig:130, pas_ai_lord_decide (first 150 stmts), pas_faction_start_campaign, pas_faction_end_campaign, pas_lord_patrol_center`, `async_process_kingdom_parties_ai body empty (dis)`
- **Overlaps:** `tld.faction_strength_war_progression`, `tld.war_theaters_advance_camps`, `vc.marshal_election`

<a id="perisnofreelancer-service"></a>
### Enlist as a freelancer soldier under a lord — perisno (`perisno.freelancer_service`)

**What it does:** The player can sign up as a common soldier in a lord's army, march attached to his party, take leave, return, be discharged, desert or be captured, and options in the mod-option screen enable it, ignore weak enemies, disable upgrades and enable re-gearing. A mod-option text warns the minimod was reported bugged.

**How it works:** freelancer_state (global) is written by dialog 'ask_return_from_leave' and by freelancer_event_player_enlists/returns/vacation/discharge/deserts/revolts/captured scripts and by game_start; 91 blocks read it (dialog conditions, party AI, wages). freelancer_attach_party attaches p_main_party to the lord's party. qst_freelancer_enlisted is the quest marker. A dialog line refuses marriage to 'a common soldier'.

- **Hooks:** `dlg:8135:dlga_lord_request_enlistment_confirm:close_window:conseq`, `dlg:4810:dlga_lord_talk:ask_return_from_leave:conseq`, `prsnt:mod_option/t0`
- **Scripts:** `freelancer_attach_party`, `freelancer_event_player_enlists`, `freelancer_event_player_returns`, `freelancer_event_player_vacation`, `freelancer_event_player_discharge`, `freelancer_event_player_deserts`, `freelancer_event_player_revolts`, `freelancer_event_player_captured`
- **Globals:** `freelancer_state`, `enlisted_party`, `enlisted_lord`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `global perisno freelancer_state: 8 writers (dlg ask_return_from_leave, freelancer_event_player_* scripts, game_start), 91 readers`, `explain perisno freelancer_attach_party: callers freelancer_event_player_enlists/returns; entry dlg:8135 and dlg:8151/8152; writes freelancer_state`, `text freelancer --mods perisno: 71 hits incl. mod_option labels 'Enable Freelancer', 'Disable Freelancer Upgrades', 'Enable Freelancer Regearing'`

<a id="tldwar-theaters-advance-camps"></a>
### War theatres with moving advance camps — tld (`tld.war_theaters_advance_camps`)

**What it does:** The map is split into four theatres. Each faction fights in one theatre at a time; when no enemy factions or enemy camps remain there it marches on to the next theatre and, after a delay, sets up an Advance Camp (a temporary fortified center) that acts as its forward base, wiping out any enemy camp in that theatre. The player's reserves and some quests follow the camp.

**How it works:** Faction slots: 159 home theatre, 160 active theatre (bit flags 1/2/4/8), 161 its advance-camp party, 162 time of last move, 181 pending move. find_next_theater walks a fixed per-home-theatre order; check_active_factions_in_theater / check_active_advance_camps decide if enemies remain. strig:67 (daily) and update_active_theaters move factions on, log 'The forces of X have moved to Y', disable the old camp and its volunteers. strig:58 (6 h): if a faction is away from home, strength > 3000, a week has passed and a strength-weighted roll succeeds, it spends 1000 strength, positions its camp with get_advcamp_pos_predefined, enables it, destroys enemy camps in that theatre, and refills the camp garrison. Lord AI targets (cf_get_random_center_in_theater, cf_find_target_patrolling_enemy_lord_in_theater) and quest generation are restricted to the active theatre.

- **Hooks:** `strig:67`, `strig:58`, `strig:65`, `strig:69`
- **Scripts:** `find_theater`, `find_next_theater`, `update_active_theaters`, `check_active_factions_in_theater`, `wott_check_active_factions_in_theater`, `check_active_advance_camps`, `get_advcamp_pos_predefined`, `theater_name_to_s15`, `cf_reinforce_next_theater`, `reinforce_next_theater_aux`, `cf_get_random_center_in_theater`
- **Slots:** `faction:159`, `faction:160`, `faction:161`, `faction:162`, `faction:181`, `party:259`, `party:4`
- **Globals:** `tld_war_began`
- **Module-specific resources:** party: advance camp parties 78-95
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis tld find_next_theater (bit-flag chain by slot 159)`, `dis tld strig:67 / update_active_theaters (slot 160 moves, log messages)`, `dis tld strig:58 (advance camp spawn, -1000 strength, destroy enemy camps)`
- **Overlaps:** `be.pas_marshal_campaign_ai`, `tld.faction_strength_war_progression`, `vc.marshal_election`

<a id="acansiege-planning-inherited"></a>
### Siege planning (blockade, sanitation, traitors, infiltration, ambushes, starvation, fortified siege camp): inherited Brytenwalda/VC system — acan (`acan.siege_planning_inherited`)

**What it does:** Before assaulting, the besieger meets advisers to set up a blockade, look for a traitor inside, infiltrate, ambush relief forces and fortify the siege camp. Defenders starve and may sally, surrender or die. This is the same Brytenwalda-lineage siege system that VC and 457 AD carry.

**How it works:** menu:siege_plan (same text in vc, ad457 and acan) sets $g_siege_saneamiento, $g_campos_cercanos, $g_traicion_interna and $g_infiltracion_interna. Menus include construct_circunvalation, construct_saneamiento, traicion_resultado1-5, infiltracion_resultado1-5, emboscada_*, fortify_siege_camp, nofood_siege_defenders_sally, surrender_siege_defenders_starved and suicide_siege_defenders_starved. menu:siege_assault resolves the assault (encounter_calculate_fit, mantlets $g_mantlets_1). acan stores siege state in party slots 310-315; VC uses 400-403 and ad457 275-278 for the same roles.

- **Hooks:** `menu:siege_plan`, `menu:siege_assault`, `menu:construct_circunvalation`, `menu:fortify_siege_camp`, `menu:nofood_siege_defenders_sally`, `strig:87`
- **Scripts:** `set_town_picture`, `encounter_calculate_fit`, `party_count_fit_regulars`, `get_max_skill_of_player_party`
- **Menus:** `menu_siege_plan`, `menu_siege_assault`, `menu_construct_circunvalation`, `menu_construct_saneamiento`, `menu_fortify_siege_camp`, `menu_nofood_siege_defenders_sally`, `menu_surrender_siege_defenders_starved`, `menu_traicion_interna2`, `menu_infiltracion_resultado1`, `menu_emboscada_player`
- **Slots:** `party:310`, `party:311`, `party:312`, `party:313`, `party:314`, `party:315`, `party:193`
- **Globals:** `g_siege_saneamiento`, `g_campos_cercanos`, `g_traicion_interna`, `g_infiltracion_interna`, `g_days_spent_starving`, `g_empieza_asedio`, `g_mantlets_1`, `g_listos_para_asalto`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `auto report menus: traicion_*, infiltracion_*, emboscada_*, construct_circunvalation, construct_saneamiento`
- **Overlaps:** `acw.siege_assault_waves_and_surrender`, `ad457.vc_siege_planning_and_camp_events_inherited`, `awoiaf.siege_ram_assault_and_hostage_surrender`, `bi.siege_town_militia`, `vc.siege_planning`

<a id="acwbesieged-map-smoke-and-caravan-spacing"></a>
### Smoke over besieged towns on the world map; caravans leave a town at most every 2 hours — acw (`acw.besieged_map_smoke_and_caravan_spacing`)

**What it does:** While a town or fort is under siege, fire and smoke rise from it on the world map, so sieges are visible at a glance; the effect disappears when the siege ends. Separately, a walled town only sends out one merchant caravan every two hours, so caravans do not leave in clumps.

**How it works:** strig:105 (hourly, module_simple_triggers.py 4979, '#Siege visual effects'): for each walled center, if slot_center_is_besieged_by holds an active party and party slot 372 (slot_siege_spikes) <= 0 -> party_add_particle_system psys_map_village_fire + psys_map_village_fire_smoke, slot 372 = 1; when the siege is gone -> party_clear_particle_systems, slot = -1. Same trigger ('#caravan timers') decrements party slot 373 (slot_caravan_timer) on walled centers; strig:51 ('Troop AI: Merchants thinking') refuses to dispatch a caravan from a center whose timer is > 0 and sets it to 2 after each departure; game_start initialises it to 0. The same hourly trigger also removes pt_scout_camp parties when qst_destroy_scout_camp is not active and completes qst_scout_enemy_town when the player comes within 4 map units of the target (unrelated quest housekeeping).

- **Hooks:** `strig:105`, `strig:51`
- **Slots:** `party:372`, `party:373`
- **Module-specific resources:** psys: psys_map_village_fire, psys_map_village_fire_smoke
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `grep party_add_particle_system --mods acw -> strig:105 stmt 8`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_simple_triggers.py 4979-5010 and 2180-2232; module_constants.py 837-838 slot_siege_spikes = 372, slot_caravan_timer = 373`
- **Overlaps:** `acw.army_size_map_icons`, `bi.culture_lord_map_icons`, `cbl.map_icons_by_party_type_and_ships`

<a id="acwsiege-assault-waves-and-surrender"></a>
### Wave-by-wave auto-resolved siege assault, plus surrender when besieged — acw (`acw.siege_assault_waves_and_surrender`)

**What it does:** When the player orders an assault without joining it, the result arrives one wave at a time with casualty reports; after each wave the player can keep attacking, personally lead the next wave (switching into the siege battle), or call the soldiers back and keep the siege. A player trapped inside a besieged town can also surrender instead of fighting.

**How it works:** menu:castle_attack_walls_simulate (rewritten): faction-specific background; inflict_casualties_to_party_group both ways using party_calculate_strength (attacker strength/10 vs defender/4); prints casualties; sets $no_soldiers_left / $battle_won. New options (absent in Native): continue_attacking (re-enter the same menu = next wave), lead_next_wave (set_jump_mission castle_attack_walls_belfry or _ladder by town slot 27, jump_to_scene the siege scene from party slot 18/10), call_soldiers_back (back to menu:castle_besiege, siege continues). menu:siege_started_defender/opt:surrender (new): $g_player_surrenders=1, $g_battle_result=-1, next menu captivity_start_under_siege_defeat via menu:total_defeat.

- **Hooks:** `menu:castle_attack_walls_simulate`, `menu:castle_attack_walls_simulate/opt:call_soldiers_back:conseq`, `menu:castle_attack_walls_simulate/opt:lead_next_wave:conseq`, `menu:siege_started_defender/opt:surrender:conseq`
- **Scripts:** `party_calculate_strength`, `print_casualties_to_s0`, `party_count_members_with_full_health`
- **Menus:** `menu_castle_attack_walls_simulate`, `menu_siege_started_defender`, `menu_castle_besiege`
- **Slots:** `party:18`, `party:10`, `party:27`
- **Globals:** `no_soldiers_left`, `battle_won`, `g_battle_result`, `g_player_surrenders`, `g_siege_battle_state`
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `dis acw menu:castle_attack_walls_simulate + 3 option conds/conseqs`, `dis acw menu:siege_started_defender/opt:surrender:cond/conseq`, `changelog 5/1/2026: 'ability for the player to withdraw from sieges after ordering their troops to attack without them' and 'ability for the player to surrender after entering into a besieged location' -> both verified`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_game_menus.py 7478, 8473`, `changelog v4.0 UPDATE 5/1/2026`
- **Overlaps:** `acan.siege_planning_inherited`, `ad457.vc_siege_planning_and_camp_events_inherited`, `awoiaf.siege_ram_assault_and_hostage_surrender`, `bi.siege_town_militia`, `vc.siege_planning`

<a id="ad457vc-siege-planning-and-camp-events-inherited"></a>
### Siege planning and siege-camp events (inherited from VC/Brytenwalda, extended) — ad457 (`ad457.vc_siege_planning_and_camp_events_inherited`)

**What it does:** Same multi-day siege layer as Viking Conquest: from 'Siege Warfare (Planning Siege)' the player builds circumvallation and latrines, seeks a traitor, sends infiltrators, forages nearby fields, places ladders/mantlets; starving defenders may sally or surrender. During a siege with enough men, random camp events fire - 457 AD has 29 siege-event menus (VC's own count not re-checked).

**How it works:** menu:castle_besiege/opt:siege_warfare_p -> menu_siege_plan with the Brytenwalda/VC Spanish-named sub-menus (construct_circunvalation, construct_saneamiento, traicion_*, infiltracion_*, campos_cercanos*, emboscada_*, poner_escaleras*, build_mantles2), globals $g_empieza_asedio, $g_siege_saneamiento, $g_campos_cercanos, $g_infiltracion_interna, $g_cabezas_dentro. strig:133 (60h, needs >30 men and no latrines) -> menu_event_siege_01..03; strig:134 (24h, >40 fit men) -> menu_event_siege_04..26 (some gated on party 275 != 2, one removes a regular via remove_regular_troops). Disease menus enfermedad*_siege.

- **Hooks:** `menu:castle_besiege/opt:siege_warfare_p:conseq`, `menu:siege_plan`, `strig:133`, `strig:134`
- **Scripts:** `remove_regular_troops`, `lift_siege`, `process_sieges`
- **Menus:** `menu_siege_plan`, `menu_siege_assault`, `menu_construct_circunvalation`, `menu_construct_saneamiento`, `menu_traicion_interna2`, `menu_infiltracion_resultado1`, `menu_campos_cercanos1`, `menu_nofood_siege_defenders_sally`, `menu_surrender_siege_defenders_starved`, `menu_event_siege_01`, `menu_event_siege_29`, `menu_enfermedad_siege`
- **Presentations:** `prsnt_infiltrationandsabotage`
- **Slots:** `party:275`
- **Globals:** `g_empieza_asedio`, `g_siege_saneamiento`, `g_campos_cercanos`, `g_infiltracion_interna`, `g_cabezas_dentro`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `dis ad457 strig:133 / strig:134: siege-camp event dispatch`, `menus-not-in-Native list (auto report): menu_event_siege_01..29, enfermedad*_siege`
- **Overlaps:** `acan.siege_planning_inherited`, `acw.siege_assault_waves_and_surrender`, `awoiaf.siege_ram_assault_and_hostage_surrender`, `bi.siege_town_militia`, `vc.siege_planning`

<a id="awoiafsiege-ram-assault-and-hostage-surrender"></a>
### Battering-ram assaults, and using a captured lord to force a surrender — awoiaf (`awoiaf.siege_ram_assault_and_hostage_surrender`)

**What it does:** Besiegers can spend hours building a battering ram (time scales with the best Engineer skill); the assault then uses a ram scene where AI soldiers push the ram to the gate and the player can join them. Alternatively, if the player holds the castle's own lord prisoner, he can persuade the garrison to surrender with the lord's help, or offer the lord's safe return in exchange for the castle - success depends on relations and skills.

**How it works:** menu:siege_assault/opt:build_battering_ram -> menu_battering_ram (engineer-based build hours) -> mst_castle_attack_walls_ram; its mission triggers t112 (siege_init_ai_and_ram), t113 (cf_siege_move_ram: moves ram props along stored path, $ram_num_men_pushing, $cur_ram_pos, scene slot 25), t115 (cf_siege_assign_men_to_ram: picks attackers to push), plus the fire-arrow routines (the ram can be burnt, $g_ram_was_destroyed). Surrender: menu:castle_guard options persuade_center_surrender_with_town_lord / take_lord_as_hostage -> menu_persuade_center_surrender / _2 ({reg30?...surrendered without bloodshed...}) -> menu_castle_taken_without_bloodshed.

- **Hooks:** `menu:siege_assault/opt:build_battering_ram:conseq`, `mst:castle_attack_walls_ram/t112:cond`, `mst:castle_attack_walls_ram/t113:cond`, `mst:castle_attack_walls_ram/t115:cond`, `menu:castle_guard/opt:take_lord_as_hostage:conseq`, `menu:castle_guard/opt:persuade_center_surrender_with_town_lord:conseq`
- **Scripts:** `siege_init_ai_and_ram`, `cf_siege_move_ram`, `cf_siege_assign_men_to_ram`
- **Menus:** `menu_battering_ram`, `menu_persuade_center_surrender`, `menu_persuade_center_surrender_2`, `menu_castle_taken_without_bloodshed`
- **Mission templates:** `mst_castle_attack_walls_ram`
- **Slots:** `scene:25`
- **Globals:** `ram_positioned`, `cur_ram_pos`, `ram_num_men_pushing`, `last_ram_object_pos`, `ram_rotating_objects_begin`, `g_ram_was_destroyed`
- **Module-specific resources:** scene_prop: spr_ram_body, spr_ram_shaft, spr_ram_wheel
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `refs mt mst_castle_attack_walls_ram <- menu:siege_assault, besiegers_camp_with_allies, siege_started_defender`, `roots siege_init_ai_and_ram / cf_siege_move_ram / cf_siege_assign_men_to_ram -> mst:castle_attack_walls_ram t112/t113/t115`, `texts menu:battering_ram 'As the party member with the highest Engineer skill... will take {reg4} hours'`, `refs menu_persuade_center_surrender(_2) <- menu:castle_guard opts persuade_center_surrender_with_town_lord / take_lord_as_hostage`
- **Overlaps:** `acan.siege_planning_inherited`, `acw.siege_assault_waves_and_surrender`, `ad457.vc_siege_planning_and_camp_events_inherited`, `bi.siege_town_militia`, `vc.siege_planning`

<a id="bisiege-town-militia"></a>
### Townsfolk take up arms when a town is besieged — bi (`bi.siege_town_militia`)

**What it does:** When an enemy army starts besieging a town or castle, a one-time levy of armed townsmen joins the garrison, sized by the town's prosperity and Romanitas (up to 30). The player gets a message for their own fiefs.

**How it works:** Inside Native's process_sieges loop (BI adds ~19 statements), when a besieger is found: if party slot 616 is 0 and the center is not a village, adds (prosperity/8 + romanitas/10, max 30) trp_townsman to the center, sets slot 616=1 and, for player-owned centers, logs '{reg4} townsfolk of {s4} take up arms.'. lift_siege resets slot 616 to 0 so the levy can happen again next siege.

- **Hooks:** `script:process_sieges`, `script:lift_siege`
- **Scripts:** `process_sieges`, `lift_siege`
- **Slots:** `party:616`, `party:605`, `party:50`
- **Module-specific resources:** troop: trp_townsman
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `dis bi process_sieges @56-75`, `slot bi party 616: process_sieges e1/s1, lift_siege s1`, `text: '{reg4}_townsfolk_of_{s4}_take_up_arms.'`
- **Overlaps:** `acan.siege_planning_inherited`, `acw.siege_assault_waves_and_surrender`, `ad457.vc_siege_planning_and_camp_events_inherited`, `awoiaf.siege_ram_assault_and_hostage_surrender`, `vc.siege_planning`

<a id="oa1860explosive-and-destructible-props"></a>
### Explosive powder barrels and destructible field cover — oa1860 (`oa1860.explosive_and_destructible_props`)

**What it does:** Scene props such as sandbags, sandbag walls, cavalry spikes, doors and earthwork sally gates can be shot or hacked to pieces; black-powder barrels explode when destroyed, damaging everyone within 3 m in proportion to how close they stood.

**How it works:** Generic destructible set on spr_sandbag, spr_sandbag_wall, spr_cav_spikes, spr_door_destructible, spr_earth_sally_gate_left/right: ti_on_scene_prop_init scene_prop_set_hit_points 10; ti_on_scene_prop_hit dummy sound + psys_dummy_smoke/straw; ti_on_scene_prop_destroy sinks the prop 12 m (prop_instance_animate_to_position). spr_blackpowder_barrel destroy (21 stmts): explosion smoke, sink, then for agents within 300 cm: damage = 300 - distance(cm), applied via agent_set_hit_points + agent_deliver_damage_to_agent (self-credited).

- **Hooks:** `spr:spr_blackpowder_barrel/t1`, `spr:spr_sandbag/t0`, `spr:spr_sandbag/t1`, `spr:spr_sandbag/t2`, `spr:spr_door_destructible/t1`
- **Module-specific resources:** scene_prop: spr_blackpowder_barrel, spr_sandbag, spr_sandbag_wall, spr_cav_spikes; psys: psys_dummy_smoke, psys_dummy_straw, psys_map_village_looted_smoke; sound: snd_dummy_hit, snd_dummy_destroyed, snd_explosion1
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `dis oa1860 spr:spr_sandbag/t0..t2`, `dis oa1860 spr:spr_blackpowder_barrel/t1`, `sqlite: spr_door_destructible triggers 2/5/3 stmts in oa1860 vs 8/2/40 in native/cae`
- **Overlaps:** `acw.explosive_grenades`, `awoiaf.fire_arrows_destructible_props`, `be.ww1_weapons_mg_gas_grenades`, `nw.explosives_destructible_props`, `oa1860.explosive_thrown_weapons`, `sw.scripted_grenade_ballistics`

<a id="vcsiege-planning"></a>
### Siege planning: blockade, sanitation, treachery, sabotage, burning fields, starvation and siege equipment — vc (`vc.siege_planning`)

**What it does:** Besieging becomes a multi-day operation. From a siege-planning menu the player can build a blockade (circumvallation) that protects the camp and starves the town, dig latrines to avoid disease, send men to find a traitor inside, send infiltrators to burn food stores or poison wells, and burn the surrounding fields (results depend on harvest season). Defenders run out of food, may sally out or surrender starving, can be asked for tribute or hostages, and the assault needs ladders/mantlets brought up first.

**How it works:** menu:castle_besiege offers siege_warfare_p -> menu:siege_plan, which summarises state into s15-s20 from party slot 400 (blockade 0/1 building/2 done), $g_traicion_interna (betrayal 1-4), $g_campos_cercanos (fields 1-3), $g_infiltracion_interna (infiltration 1-4), $g_siege_saneamiento (sanitation, timed off slot 403 hours) and offers build_circunvalation / close_circunvalation / build_varios / traicion_interna / infiltracion_interna / destruir_campos_a/b / town_investigar. Outcome menus: traicion_resultado1-5 / traicion_lucha, infiltracion_resultado1-5 (+_c variants), campos_cercanos1-4 (season-dependent food), construct_saneamiento, construct_circunvalation. prsnt_infiltrationandsabotage picks the sabotage target (writes slot 405). Starvation: $g_days_spent_starving / $g_next_sally_at / $g_sally_timer advanced in menu:castle_besiege -> menu_nofood_siege_defenders_sally or menu_surrender_siege_defenders_starved. Assault prep: menu:siege_assault with $g_listos_para_asalto, $g_mantlets_1, build_mantlet / build_ladders, menu_poner_escaleras(_mantlets); mst castle_attack_walls_belfry/t95 and _ladder/t69 read $g_mantlets_1. Negotiation dialogs player_siege_ask_surrender / player_hostage_surrender / player_siege_tributo read starvation state. lift_siege and castle_taken reset everything.

- **Hooks:** `menu:castle_besiege/opt:siege_warfare_p:conseq`, `menu:siege_plan`, `menu:castle_besiege`, `menu:siege_assault`, `prsnt:infiltrationandsabotage/t1`, `dlg:1547:dlga_player_siege_tributo:player_siege_tributo2:cond`
- **Scripts:** `lift_siege`, `process_sieges`
- **Menus:** `menu_siege_plan`, `menu_siege_assault`, `menu_construct_circunvalation`, `menu_construct_saneamiento`, `menu_traicion_interna2`, `menu_traicion_resultado1`, `menu_traicion_lucha`, `menu_infiltracion_resultado1`, `menu_campos_cercanos1`, `menu_poner_escaleras`, `menu_poner_escaleras_mantlets`, `menu_build_mantles2`, `menu_nofood_siege_defenders_sally`, `menu_surrender_siege_defenders_starved`, `menu_castle_attack_walls_simulate2`
- **Presentations:** `prsnt_infiltrationandsabotage`, `prsnt_camp_screen_siege`
- **Mission templates:** `mst_castle_attack_walls_belfry`, `mst_castle_attack_walls_ladder`
- **Dialogs:** `dlga_player_siege_ask_surrender`, `dlga_player_hostage_surrender`, `dlga_player_siege_tributo`
- **Slots:** `party:400`, `party:401`, `party:402`, `party:403`, `party:404`, `party:405`
- **Globals:** `g_siege_saneamiento`, `g_traicion_interna`, `g_infiltracion_interna`, `g_campos_cercanos`, `g_listos_para_asalto`, `g_mantlets_1`, `g_cabezas_dentro`, `g_days_spent_starving`, `g_next_sally_at`, `g_sally_timer`, `g_empieza_asedio`
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `sqlite texts menus: construct_circunvalation, construct_saneamiento, traicion_resultado1-5, infiltracion_resultado1-5, campos_cercanos1-4, nofood_siege_defenders_sally, surrender_siege_defenders_starved`, `sqlite globals: g_days_spent_starving/g_next_sally_at written by castle_besiege, read by siege surrender/tribute dialogs`
- **Overlaps:** `acan.siege_planning_inherited`, `acw.siege_assault_waves_and_surrender`, `ad457.vc_siege_planning_and_camp_events_inherited`, `awoiaf.siege_ram_assault_and_hostage_surrender`, `bi.siege_town_militia`

<a id="acanthrust-only-formation-weapons"></a>
### Thrust-only ('noswing') weapon swap for infantry in tight formation (spear and pike wall) — acan (`acan.thrust_only_formation_weapons`)

**What it does:** When infantry form a close formation, every long enough thrusting weapon is swapped for a thrust-only twin, so men in the ranks stab past their comrades instead of swinging into them. On formation end or death the real weapon is swapped back, so loot stays correct.

**How it works:** init_noswing_weapons (ti_before_mission_start in 10 battle templates, 278 stmts) writes a two-way map in item slot 46: weapon <-> its 'noswing_' twin (139 noswing item entries in item_kinds1.txt, which sit past itm_items_end). form_infantry calls switch_to_noswing_weapons(agent, min_length) for each formation member: it loops weapon slots 0-3, and for a thrusting weapon (cf_is_thrusting_weapon) at least min_length long swaps to the slot-46 twin. switch_from_noswing_weapons restores the original from formation_end and on ti_on_agent_killed_or_wounded in the same 10 templates.

- **Hooks:** `mst:lead_charge/t97:conseq (ti_before_mission_start)`, `mst:lead_charge/t100:conseq (ti_on_agent_killed_or_wounded)`, `script:form_infantry`, `script:formation_end`
- **Scripts:** `init_noswing_weapons`, `switch_to_noswing_weapons`, `switch_from_noswing_weapons`, `cf_is_thrusting_weapon`, `form_infantry`, `formation_end`
- **Mission templates:** `mst_lead_charge`, `mst_lead_charge_large`, `mst_quick_battle_battle`, `mst_besiege_inner_battle_castle`, `mst_besiege_inner_battle_town_center`, `mst_castle_attack_walls_defenders_sally`, `mst_village_raid`, `mst_village_attack_bandits`
- **Slots:** `item:46`
- **Module-specific resources:** item: itm_noswing_* (139 twin items)
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis acan switch_to_noswing_weapons / switch_from_noswing_weapons (item slot 46 swap, length threshold)`, `grep switch_to_noswing_weapons --mods acan: called only from script:form_infantry`, `callers acan switch_from_noswing_weapons: 10 templates ti_on_agent_killed_or_wounded + formation_end`, `compare switch_to_noswing_weapons: ad457/vc/awoiaf 100%; init_noswing_weapons vc 98%`, `grep -c noswing item_kinds1.txt = 139`
- **Overlaps:** `acan.vc_battle_stack_inherited`, `acw.scripted_ai_battle_plan`, `ad457.vc_battle_naval_layer_inherited`, `be.ai_battle_tactics_presets`, `be.infantry_square_and_field_works`, `bi.pbod_formations_ai`, `laigle.pbod_motomataru_stack`, `nw.division_gunpowder_ai`, `nw.locator_line_formations`, `pop.disciplined_faction_ai_gate`, `pop.formations_battle_ai_kit`, `sw.ranged_backstep_ai`, `tld.formations_motomataru_pop_lineage`, `vc.formations_order_translation`, `vc.persistent_division_formations`

<a id="acanvc-battle-stack-inherited"></a>
### Inherited VC battle stack: battlegroup formations AI, war cries/horns/shield taunts, courage spreading, shield bash; plus a ratio-based rout rule — acan (`acan.vc_battle_stack_inherited`)

**What it does:** acan's battle layer is Viking Conquest's: battlegroup formations with field tactics for the AI, horse-archer skirmishing, war cries, horns and shield taunts that lift courage, morale spreading from nearby deaths, and an AI shield bash. Its own additions are a rout rule (a side can only rout once its losses pass a set share of the men still standing), bodyguards in town scenes and a death camera.

**How it works:** Formations: store_battlegroup_data, form_infantry/archers/cavalry, team_field_melee_tactics, team_field_ranged_tactics, player_order_formations and battlegroup_* are 97-100% opcode-identical to VC (compare). Immersion: agent_perform_warcry/horn, shield_taunt_trigger, change_courage_around_agent (82% vs VC) and shield_bash_trigger (85% vs VC) run in about 29-44 templates. acan/ad457 add cf_calculate_battle_ratio (every 10 s, j_num_* globals) and cf_agent_can_rout (an agent may rout only if 10 x (dead+wounded+routed) > men still ready, i.e. about 9% losses), all_enemies_routed and agent_run_away. cf_can_spawn_as_body_guard spawns companions as bodyguards in town and hall scenes, and init_death_cam follows the player after death.

- **Hooks:** `mst:lead_charge (formation triggers every 0s/0.1s)`, `mst:lead_charge/t50:conseq (every 3s rout check)`, `mst:lead_charge/t52:conseq (ti_on_agent_killed_or_wounded)`
- **Scripts:** `store_battlegroup_data`, `form_infantry`, `team_field_melee_tactics`, `team_field_ranged_tactics`, `player_order_formations`, `horse_archer_skirmish`, `agent_perform_warcry`, `agent_perform_horn`, `shield_taunt_trigger`, `change_courage_around_agent`, `shield_bash_trigger`, `cf_calculate_battle_ratio`, `cf_agent_can_rout`, `all_enemies_routed`, `agent_run_away`, `cf_can_spawn_as_body_guard`, `init_death_cam`
- **Mission templates:** `mst_lead_charge`, `mst_lead_charge_large`, `mst_quick_battle_battle`
- **Slots:** `agent:3`, `agent:5`, `agent:9`, `agent:10`, `agent:11`, `agent:12`, `agent:13`, `item:46`, `troop:30`, `troop:31`, `troop:32`
- **Globals:** `j_num_us_ready`, `j_num_us_dead`, `j_num_enemies_ready`, `battle_ratio`, `g_charge_on`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `compare cf_agent_can_rout: ad457 100%, vc absent`, `dis acan cf_agent_can_rout: losses x10 > ready`
- **Overlaps:** `acan.thrust_only_formation_weapons`, `acw.scripted_ai_battle_plan`, `ad457.vc_battle_naval_layer_inherited`, `be.ai_battle_tactics_presets`, `be.infantry_square_and_field_works`, `bi.pbod_formations_ai`, `laigle.pbod_motomataru_stack`, `nw.division_gunpowder_ai`, `nw.locator_line_formations`, `pop.disciplined_faction_ai_gate`, `pop.formations_battle_ai_kit`, `sw.ranged_backstep_ai`, `tld.formations_motomataru_pop_lineage`, `vc.formations_order_translation`, `vc.persistent_division_formations`

<a id="acwcommand-all-allies"></a>
### Player commands every allied soldier in battle — acw (`acw.command_all_allies`)

**What it does:** In field battles where allied lords fight beside the player, their soldiers stay on the player's team and obey his orders, instead of forming a separate allied team the player cannot command. The FAQ calls this deliberate: the AI is too simple to command well.

**How it works:** agent_reassign_team (called from ti_on_agent_spawn in lead_charge and castle_attack_walls_defenders_sally) is Native's script that moves allied lords' agents to team + 2 unless the player is marshal of his own kingdom. ACW initialises its ':continue' flag to 0 (source comment '# default: 1'), so the final (eq, ':continue', 1) always fails and no ally is ever moved; it also skips agents without a party (artillery crews).

- **Hooks:** `mst:lead_charge/t0:conseq`, `mst:castle_attack_walls_defenders_sally/t0:conseq`
- **Scripts:** `agent_reassign_team`
- **Mission templates:** `mst_lead_charge`, `mst_castle_attack_walls_defenders_sally`
- **Slots:** `faction:8`
- **Globals:** `players_kingdom`
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `dis acw agent_reassign_team: stmt 9 (assign, :l3, 0) then stmt 21 (eq, :l3, 1) -> never reassigns`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_scripts.py 27222-27250 ('# default: 1', '##DrTomas - for cannon crew, they do not have party')`, `FAQ.txt: 'In battles, I always control both my own and my allies soldiers ... this is not a bug'`
- **Overlaps:** `acw.death_camera`, `be.aerial_command_view`

<a id="acwscripted-ai-battle-plan"></a>
### Timed AI battle plan, faction default formations and mounted-pistol auto-switch — acw (`acw.scripted_ai_battle_plan`)

**What it does:** Enemy AI follows a timed script: at 2 s (and again at 25 s) its infantry and skirmishers advance a third of the way toward the player's largest group and dress into 4-rank lines, at 3 s cavalry is posted beside its own infantry line, at 20 s cavalry charges and at 90 s everyone charges. Each team's formation style is chosen by its faction, and mounted AI carrying pistols/carbines are kept on their firearm unless ordered to melee.

**How it works:** $madsci_timer reset at ti_before_mission_start (t2), incremented by mst:lead_charge/t4 every 1 s. At 2/25 s: store_battlegroup_data, for each non-player team with infantry/archer battlegroups find a leader agent, get_biggest_enemy_group, place order position 1/3 of the distance plus 25 m lateral, team_give_order hold + form_archers / form_infantry (4 ranks, spacing 2). At 3 s: for each enemy team, take the first non-cavalry agent's position, point it toward the player, shift 1 m sideways and order the cavalry division (2) to hold there (beside its own line); at 20 s formation_end + charge for cavalry; at 90 s all divisions charge. t40 (once, 0.4 s) records each team's faction ($teamN_faction) and get_default_formation maps faction -> formation type (0 or 2). t51 every 4 s: mounted non-player agents with ammo, not hold-fire and not melee-only order, are switched to a wielded thrown/pistol/bow-type item (types 8/10/16) if they hold one.

- **Hooks:** `mst:lead_charge/t2:conseq`, `mst:lead_charge/t4:conseq`, `mst:lead_charge/t40:conseq`, `mst:lead_charge/t51:conseq`
- **Scripts:** `store_battlegroup_data`, `battlegroup_get_size`, `get_biggest_enemy_group`, `point_y_toward_position`, `form_infantry`, `form_archers`, `formation_end`, `get_default_formation`, `cf_formation`
- **Slots:** `agent:15`
- **Globals:** `madsci_timer`, `team0_faction`, `team1_faction`, `team2_faction`, `team3_faction`, `fplayer_agent_no`, `fplayer_team_no`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis acw mst:lead_charge/t4:conseq (madsci timeline)`, `dis acw get_default_formation`, `dis acw mst:lead_charge/t51:conseq`, `global acw madsci_timer (writers t2/t4 + quick battles)`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_mission_templates.py 1056-1200 formations_only_ai_triggers / AI_triggers (formAI_battle_phase_handling commented out)`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_mission_templates.py 6621 `(gt, ":infantry"),``
- **Overlaps:** `acan.thrust_only_formation_weapons`, `acan.vc_battle_stack_inherited`, `ad457.vc_battle_naval_layer_inherited`, `be.ai_battle_tactics_presets`, `be.infantry_square_and_field_works`, `bi.pbod_formations_ai`, `laigle.pbod_motomataru_stack`, `nw.division_gunpowder_ai`, `nw.locator_line_formations`, `pop.disciplined_faction_ai_gate`, `pop.formations_battle_ai_kit`, `sw.ranged_backstep_ai`, `tld.formations_motomataru_pop_lineage`, `vc.formations_order_translation`, `vc.persistent_division_formations`
- **Notes:** Oddity: t4 stmt 44 is (gt, :l4) with ONE operand - confirmed in the compiled bytes with dis --raw ('32 [l4]'); the engine reads the missing operand as whatever is there (in effect 'l4 > 0', the probable intent).

<a id="ad457vc-battle-naval-layer-inherited"></a>
### VC battle layer: formations, local courage, war cries/berserk, ship battles (inherited) — ad457 (`ad457.vc_battle_naval_layer_inherited`)

**What it does:** 457 AD carries Viking Conquest's battle code largely unchanged: Motomataru formations with saved division placements, AI field tactics, local courage/morale with war cry, horn, shield taunt and berserker rage, troop-detail screens, seasonal scene lighting, and deck-to-deck ship battles with Roman fleets and pirates.

**How it works:** Scripts identical or near-identical to VC (diff ad457 vc: 239 identical): battlegroup_*/form_*/player_order_formations/memorize_division_placements/process_player_division_positioning, field_tactics/team_field_melee_tactics, agent_perform_warcry/horn/shield_taunt, berserk_trigger, apply_effect_of_other_people_on_courage_scores_vc (= VC's apply_effect_of_other_people_on_courage_scores, named 100%/shape 100%), decide_run_away_or_not_vc (a VC variant of decide_run_away_or_not), inflict_casualties_to_party_vc (88% named to VC), ship_AI/spawn_ship/put_the_Klabautermann_into_the_ships/mst_sea_battle, calculate_season_light (213 callers in mission templates).

- **Hooks:** `mst:lead_charge`, `mst:sea_battle`
- **Scripts:** `player_order_formations`, `memorize_division_placements`, `field_tactics`, `team_field_melee_tactics`, `agent_perform_warcry`, `agent_perform_horn`, `agent_perform_shield_taunt`, `berserk_trigger`, `apply_effect_of_other_people_on_courage_scores_vc`, `apply_death_effect_on_courage_scores_vc`, `decide_run_away_or_not_vc`, `ship_AI`, `spawn_ship`, `calculate_season_light`
- **Presentations:** `prsnt_order_display`, `prsnt_formation_mod_option`, `prsnt_naval_ui`, `prsnt_troop_detail`
- **Mission templates:** `mst_sea_battle`
- **Slots:** `agent:23-47`, `team:1-13`, `scene_prop:6-48`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Overlaps:** `acan.thrust_only_formation_weapons`, `acan.vc_battle_stack_inherited`, `acw.scripted_ai_battle_plan`, `be.ai_battle_tactics_presets`, `be.infantry_square_and_field_works`, `bi.pbod_formations_ai`, `laigle.pbod_motomataru_stack`, `nw.division_gunpowder_ai`, `nw.locator_line_formations`, `pop.disciplined_faction_ai_gate`, `pop.formations_battle_ai_kit`, `sw.ranged_backstep_ai`, `tld.formations_motomataru_pop_lineage`, `vc.formations_order_translation`, `vc.persistent_division_formations`

<a id="beai-battle-tactics-presets"></a>
### AI battle plans: attack groups, leapfrog advance, counter-attack swap, defensive lines — be (`be.ai_battle_tactics_presets`)

**What it does:** AI armies fight with a plan. The attacker splits companies into attack groups that advance on preset formations with timers, charge when close, and a beaten attacker becomes the defender: if after ~400 s the attacking side has fallen below 35 % of the defenders' strength, roles swap and the former defender counter-attacks. Defenders man scene-placed defensive-line markers; siege defenders take cover behind walls.

**How it works:** mst:lead_charge/t109 (1 s, 255 stmts): counts humans per side, swaps $ai_attacker_team/$ai_defender_team (and the allied 'nai' teams) when ratio <= 35 % after $battle_timer >= 400; pai_set_up_attack_according_to_preset(team, preset 1 or 2 if technology 419, ...); pai_team_set_global_tactic / pai_set_team_timer / pai_tick_team_timer state machine (tactic values 3,4,15,16); pai_find_teams_company_closest_to_pos targets the nearest enemy company; pai_attack_group_set_position / pai_attack_group_charge move groups via company_hold_pos30 / company_charge. mst:lead_charge/t108 (9 s): defender logic incl. pai_siege_defender_take_cover (prop instances), company_hold_pos30_defensive_line over spr_pai_defensive_line instances. Native battle_tactic_init/_apply(_aux) emptied (0 stmts).

- **Hooks:** `mst:lead_charge/t109:cond`, `mst:lead_charge/t108:cond`, `mst:lead_charge/t30:conseq`
- **Scripts:** `pai_set_up_attack_according_to_preset`, `pai_team_set_global_tactic`, `pai_set_team_timer`, `pai_tick_team_timer`, `cf_pai_if_team_timer_is_zero`, `cf_pai_if_team_timer_is_more_than_zero`, `cf_pai_if_team_global_tactic_is_value`, `pai_find_teams_company_closest_to_pos`, `pai_attack_group_set_position`, `pai_attack_group_charge`, `cf_pai_attack_group_get_lead_company`, `pai_siege_defender_take_cover`, `company_hold_pos30`, `company_hold_pos30_defensive_line`, `company_charge`, `team_create_infantry_formation_on_pos1`
- **Slots:** `team:148`, `team:149`, `team:150`, `team:195`, `team:196`, `team:252`, `team:253`
- **Globals:** `ai_attacker_team`, `ai_defender_team`, `nai_attacker_team`, `nai_defender_team`, `battle_timer`
- **Module-specific resources:** spr: spr_pai_defensive_line, spr_pai_artillery_position
- **Relation to Native:** replaces-native
- **Confidence:** strongly-inferred
- **Evidence:** `dis be mst:lead_charge/t109:cond (role swap and preset calls)`, `dis be pai_set_up_attack_according_to_preset, pai_siege_defender_take_cover`, `auto report: battle_tactic_* modified 0/N (emptied)`
- **Overlaps:** `acan.thrust_only_formation_weapons`, `acan.vc_battle_stack_inherited`, `acw.scripted_ai_battle_plan`, `ad457.vc_battle_naval_layer_inherited`, `be.infantry_square_and_field_works`, `bi.pbod_formations_ai`, `laigle.pbod_motomataru_stack`, `nw.division_gunpowder_ai`, `nw.locator_line_formations`, `pop.disciplined_faction_ai_gate`, `pop.formations_battle_ai_kit`, `sw.ranged_backstep_ai`, `tld.formations_motomataru_pop_lineage`, `vc.formations_order_translation`, `vc.persistent_division_formations`

<a id="beinfantry-square-and-field-works"></a>
### Infantry square, prone/crouch fire and dig-in trenches — be (`be.infantry_square_and_field_works`)

**What it does:** Player can order an infantry company of 25+ men into a hollow square against cavalry; companies under fire automatically crouch or (later tech) go prone, which halves explosion damage; a dig-in order makes soldiers play a digging animation and spawns trench and sandbag props that cut artillery damage tenfold.

**How it works:** player_team_form_square (165 stmts, from prsnt:battle/t1 and prsnt:pbs/t2): needs >= 25 soldiers ('Cannot form square: too few soldiers'), takes the company centre (store_company_average_position_to_pos30) and assigns each agent a scripted destination on four faces (agent slots 30-32, 34). copmany_decide_prone_or_crouch (103 stmts, per frame via t90 when formation type 205+div in 3..5): for firearm users (item_get_accuracy != 0) toggles crouch/prone per agent (agent slot 46 = prone, used by explode_at_pos /2 and t82 accuracy). company_digin (83 stmts): once per company (team 235+div), spawns spr_pbs_trench2a/2b and spr_sandbags1/2 along the line and plays 'digging'; cf_if_agent_is_in_trench is checked in explode_at_pos (/10 damage).

- **Hooks:** `prsnt:battle/t1`, `prsnt:pbs/t2`, `mst:lead_charge/t90:conseq`
- **Scripts:** `player_team_form_square`, `copmany_decide_prone_or_crouch`, `company_digin`, `cf_if_agent_is_in_trench`, `calculate_company_average_coordinates`, `store_company_average_position_to_pos30`
- **Slots:** `agent:30`, `agent:31`, `agent:32`, `agent:34`, `agent:46`, `team:205-212`, `team:235-242`, `team:287-294`, `team:140-147`
- **Globals:** `menu_pbs_activeability_square`, `menu_pbs_activeability_digin`, `menu_pbs_activeability_pronemode`
- **Module-specific resources:** spr: spr_pbs_trench2a, spr_pbs_trench2b, spr_sandbags1, spr_sandbags2; anim: prone_rifle_idle, prone_rifle_shoot, prone_rifle_reload, digging; item: itm_shovel1
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `explain be player_team_form_square (message text, callers)`, `dis be company_digin (spawn_scene_prop trench/sandbags, digging anim)`, `dis be copmany_decide_prone_or_crouch (crouch per firearm user)`, `explode_at_pos: /10 in trench, /2 if agent slot 46`
- **Overlaps:** `acan.thrust_only_formation_weapons`, `acan.vc_battle_stack_inherited`, `acw.scripted_ai_battle_plan`, `ad457.vc_battle_naval_layer_inherited`, `be.ai_battle_tactics_presets`, `bi.pbod_formations_ai`, `laigle.pbod_motomataru_stack`, `nw.division_gunpowder_ai`, `nw.locator_line_formations`, `pop.disciplined_faction_ai_gate`, `pop.formations_battle_ai_kit`, `sw.ranged_backstep_ai`, `tld.formations_motomataru_pop_lineage`, `vc.formations_order_translation`, `vc.persistent_division_formations`

<a id="bipbod-formations-ai"></a>
### PBOD battle orders + Motomataru formations AI — bi (`bi.pbod_formations_ai`)

**What it does:** Pre-battle orders and custom deployment screens, extra orders (volley, brace, skirmish, weapon-type switch), formation AI for AI teams, custom camera and key rebinding - the standard PBOD/Formations stack.

**How it works:** prsnt:prebattle_orders/custom_deployment/custom_divisions, order_* scripts, battlegroup_*/form_*/formation_* scripts, field_tactics -> team_field_melee/ranged_tactics, cust_cam_*, init_key_config.

- **Hooks:** `mst:lead_charge/t63:conseq`, `mst:lead_charge/t64:conseq`, `prsnt:prebattle_orders/t1`
- **Scripts:** `field_tactics`, `field_ai_start_positions`, `team_field_melee_tactics`, `player_order_formations`, `prebattle_order_update_text_slot`, `order_volley_begin_end`, `equip_best_melee_weapon`, `init_item_score`
- **Presentations:** `prsnt_prebattle_orders`, `prsnt_prebattle_custom_deployment`, `prsnt_prebattle_custom_divisions`, `prsnt_pbod_redefine_keys`, `prsnt_caba_order_display`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `scratch op-sequence compare over battlegroup_/form_/order_/prebattle_ scripts`
- **Overlaps:** `acan.thrust_only_formation_weapons`, `acan.vc_battle_stack_inherited`, `acw.scripted_ai_battle_plan`, `ad457.vc_battle_naval_layer_inherited`, `be.ai_battle_tactics_presets`, `be.infantry_square_and_field_works`, `laigle.pbod_motomataru_stack`, `nw.division_gunpowder_ai`, `nw.locator_line_formations`, `pop.disciplined_faction_ai_gate`, `pop.formations_battle_ai_kit`, `sw.ranged_backstep_ai`, `tld.formations_motomataru_pop_lineage`, `vc.formations_order_translation`, `vc.persistent_division_formations`

<a id="laiglepbod-motomataru-stack"></a>
### PBOD orders/camera/deployment + Motomataru formations AI (older build) — laigle (`laigle.pbod_motomataru_stack`)

**What it does:** Volley/skirmish/brace orders, weapon-type switching, custom/death camera, prebattle orders and deployment, AI weapon choice, and Motomataru formations and field tactics for both sides.

**How it works:** Same families as the standard PBOD/Formations stack: player_order_formations, order_volley_begin_end, order_skirmish_*, order_sp_brace_begin_end, cust_cam_*, prebattle_order_*, weapon_use_*, team_field_melee_tactics/store_battlegroup_data. L'Aigle's entry is cf_formation (57 stmts), an older Motomataru dispatcher: cf_valid_formation_division returns a division role 0-5 (two extra roles: second-line infantry 3 m behind, skirmish screen 12 m ahead, flank cavalry) and calls form_infantry/form_archers/form_cavalry; form_infantry excludes cannon crew troops.

- **Hooks:** `mst:lead_charge/t27:conseq`, `mst:lead_charge/t36:conseq`, `mst:lead_charge/t55:conseq`, `strig:103`
- **Scripts:** `cf_formation`, `cf_valid_formation_division`, `form_infantry`, `form_archers`, `form_cavalry`, `player_order_formations`, `order_volley_begin_end`, `team_field_melee_tactics`, `init_item_score`, `equip_best_melee_weapon`
- **Presentations:** `prsnt_pbod_preferences`, `prsnt_prebattle_orders`, `prsnt_prebattle_custom_deployment`, `prsnt_caba_order_display`
- **Mission templates:** `mst_lead_charge`
- **Slots:** `agent:28`, `agent:29`, `agent:33`, `agent:34`, `item:41`, `item:42`, `item:43`, `item:44`, `item:45`
- **Globals:** `fplayer_agent_no`, `fplayer_team_no`, `autorotate_at_player`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `diff laigle vs pop cf_formation (division-role variant)`
- **Overlaps:** `acan.thrust_only_formation_weapons`, `acan.vc_battle_stack_inherited`, `acw.scripted_ai_battle_plan`, `ad457.vc_battle_naval_layer_inherited`, `be.ai_battle_tactics_presets`, `be.infantry_square_and_field_works`, `bi.pbod_formations_ai`, `nw.division_gunpowder_ai`, `nw.locator_line_formations`, `pop.disciplined_faction_ai_gate`, `pop.formations_battle_ai_kit`, `sw.ranged_backstep_ai`, `tld.formations_motomataru_pop_lineage`, `vc.formations_order_translation`, `vc.persistent_division_formations`

<a id="nwdivision-gunpowder-ai"></a>
### Division-level line-battle AI (advance to range, halt and fire, charge when close) — nw (`nw.division_gunpowder_ai`)

**What it does:** In NW's custom battles the AI handles each of its nine divisions separately: a division that can see an enemy division within about 200 m halts and fires at will, one that gets within 20 m (or is cavalry) charges, divisions out of contact hold with fire-on-command, and if nobody is engaged the army eventually switches to a general advance.

**How it works:** mst:quick_battle_battle/t17 (once) -> select_battle_tactic -> select_battle_tactic_aux (306 stmts: tallies infantry/cavalry/skirmish/artillery head-counts per side from trp_custom_battle_dummy_2 (456) slots 0-17/72-89 written by the custom-battle designer) and battle_tactic_init -> battle_tactic_init_aux. mst:quick_battle_battle/t20 (every 5 s) -> battle_tactic_apply -> battle_tactic_apply_aux (304): for each own division, find nearest enemy division (division_get_average_position) and line of sight (position_has_line_of_sight_to_position at +2 m); in LOS and <200 m or enemy within 25 m (get_closest3_distance_of_enemies_at_pos1) -> if cavalry or <20 m team_give_order charge (2) else hold at current spot + fire at will (13); otherwise hold + fire on command (17). With no division engaged a random roll against mission time switches tactic to 4 (advance) and stamps $g_last_tactic_change_at. mst:quick_battle_battle/t21 (every 1 s) re-issues charge/hold per division from slot 90+div/99+div.

- **Hooks:** `mst:quick_battle_battle/t17:conseq`, `mst:quick_battle_battle/t20:cond`, `mst:quick_battle_battle/t21:conseq`
- **Scripts:** `select_battle_tactic`, `select_battle_tactic_aux`, `battle_tactic_init`, `battle_tactic_init_aux`, `battle_tactic_apply`, `battle_tactic_apply_aux`, `division_get_average_position`, `get_closest3_distance_of_enemies_at_pos1`, `team_get_average_position_of_enemies`, `find_high_ground_around_pos1`
- **Mission templates:** `mst_quick_battle_battle`
- **Slots:** `troop:0-17, 36-53, 72-89, 90-107 (trp 456 division type/state/count/stance)`, `agent:23`
- **Globals:** `g_last_tactic_change_at`, `ai_team_1`, `ai_team_2`
- **Module-specific resources:** troop: trp 456 (custom-battle data troop)
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `explain nw battle_tactic_apply_aux: entry mst:quick_battle_battle/t20:cond [every 5s]; 304 vs Native 61`, `dis nw battle_tactic_apply_aux stmts 34-105 (LOS, 20000/8000/2000 thresholds, orders 2/13/17, tactic 4)`, `dis nw mst:quick_battle_battle/t21:conseq`
- **Overlaps:** `acan.thrust_only_formation_weapons`, `acan.vc_battle_stack_inherited`, `acw.scripted_ai_battle_plan`, `ad457.vc_battle_naval_layer_inherited`, `be.ai_battle_tactics_presets`, `be.infantry_square_and_field_works`, `bi.pbod_formations_ai`, `laigle.pbod_motomataru_stack`, `nw.locator_line_formations`, `pop.disciplined_faction_ai_gate`, `pop.formations_battle_ai_kit`, `sw.ranged_backstep_ai`, `tld.formations_motomataru_pop_lineage`, `vc.formations_order_translation`, `vc.persistent_division_formations`

<a id="nwlocator-line-formations"></a>
### Musket-line formations via invisible locator props (line/column/square/skirmish, wheel) — nw (`nw.locator_line_formations`)

**What it does:** Each division gets an invisible anchor prop. Orders move or rotate the anchor and every soldier is given an exact scripted spot around it: a line 2-4 ranks deep, a marching column, a hollow-ish square (side = sqrt(n)) or an open skirmish line, and the block can wheel 45 degrees left/right or turn to face the enemy.

**How it works:** mst:sp_campaign_*/t2 (once) spawns 20 copies of spr_formation_locator (prop 1560, one per team x division, invisible) and moves them to entry points; scene-independent because it uses spawn_scene_prop at runtime. On spawn/death correct_num_troops_in_formation keeps a live head-count per division in trp_custom_battle_dummy slots 20-38. give_mm_order (from the F4/F5 order presentation) writes the movement order (slot 100+div/110+div: 0 hold-here, 1 follow, 2 charge, 3 advance, 5 fall back) and the formation shape (slot 40+div/50+div: 0 line, 1 column, 2 square, 3 skirmish) and $g_wheel (1 left, 2 right, 3 face enemy). deploy_division_via_teleport (238 stmts; called from per-mission one-shot/state triggers t15/t19/t33) moves the locator (to the player for 'follow', +/-1.8 m for advance/fall back, rotated for wheel), then computes rank width from head-count (>59 -> n/4 per rank, >29 -> n/3, >5 -> n/2), spacing 100 (200 for skirmish, with staggered second rank) and gives each agent agent_set_scripted_destination (or _no_attack when the division is in hold-fire mode).

- **Hooks:** `mst:sp_campaign_vienna/t2:conseq`, `mst:sp_campaign_vienna/t1:conseq`, `mst:sp_campaign_vienna/t3:conseq`, `mst:sp_campaign_vienna/t15:conseq`, `mst:sp_campaign_vienna/t19:conseq`, `mst:sp_campaign_vienna/t33:conseq`, `prsnt:new_order_stuff/t1`
- **Scripts:** `deploy_division_via_teleport`, `give_mm_order`, `correct_num_troops_in_formation`, `division_get_average_position`, `team_get_average_position_of_enemies`
- **Presentations:** `prsnt_new_order_stuff`
- **Mission templates:** `mst_sp_campaign_vienna`, `mst_sp_campaign_austerlitz_1`, `mst_sp_campaign_austerlitz_1_old`, `mst_sp_campaign_dresden_1`, `mst_sp_campaign_dresden_2`
- **Slots:** `troop:20-38 (head-count)`, `troop:40-58 (formation shape)`, `troop:60-78 (fire mode)`, `troop:100-118 (movement order)`, `agent:23`
- **Globals:** `g_wheel`, `g_hold_position_arrow_instance`
- **Module-specific resources:** spr: spr_formation_locator (1560); troop: trp_custom_battle_dummy (455)
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis nw mst:sp_campaign_vienna/t2:conseq: 20x spawn_scene_prop 1560 + entry-point placement`, `sqlite names nw spr 1560 = spr_formation_locator`, `dis nw give_mm_order: slot writes 455 40/50/60/70/100/110 + display_message 'form line/column/square/skirmish', 'wheel left/right'`, `dis nw deploy_division_via_teleport: rank-width rules and agent_set_scripted_destination`, `dis nw correct_num_troops_in_formation: slot 20/30+div +/-1 from spawn (t1) and death (t3)`
- **Overlaps:** `acan.thrust_only_formation_weapons`, `acan.vc_battle_stack_inherited`, `acw.scripted_ai_battle_plan`, `ad457.vc_battle_naval_layer_inherited`, `be.ai_battle_tactics_presets`, `be.infantry_square_and_field_works`, `bi.pbod_formations_ai`, `laigle.pbod_motomataru_stack`, `nw.division_gunpowder_ai`, `pop.disciplined_faction_ai_gate`, `pop.formations_battle_ai_kit`, `sw.ranged_backstep_ai`, `tld.formations_motomataru_pop_lineage`, `vc.formations_order_translation`, `vc.persistent_division_formations`

<a id="nwvolley-fire"></a>
### Synchronised division volley fire — nw (`nw.volley_fire`)

**What it does:** When a musket division is set to volley mode, every soldier in it raises and holds his musket until the whole division is aimed, then all fire together on the next frame; soldiers without a musket in hand are made to draw one.

**How it works:** mst:sp_campaign_*/t5 (every frame) calls volley_fire. For each team (0/1) and each of 9 divisions it checks the storage troop trp_custom_battle_dummy (455) slot 60+div (team 0) / 70+div (team 1) == 2 (volley mode, written by give_mm_order from the F6 'firing' sub-menu). Phase slot 80+div / 90+div: phase 0 = 'make ready' -> agent_set_attack_action(agent,0,1) (ready and hold) for every human of that team+division whose agent slot 23 == 0 (not routed) and who is not >1 m from his scripted destination (i.e. still marching); any agent wielding a non-musket (item slot 1 != 12) is switched to a musket from inventory. If every agent reached the aimed-hold attack state (attack_action 5) the phase flips to 1 = 'fire' -> agent_set_attack_action(agent,0,0) releases everybody at once, then the phase flips back to 0.

- **Hooks:** `mst:sp_campaign_vienna/t5:conseq`, `mst:sp_campaign_austerlitz_1/t5:conseq`, `mst:sp_campaign_austerlitz_1_old/t5:conseq`, `mst:sp_campaign_dresden_1/t5:conseq`, `mst:sp_campaign_dresden_2/t5:conseq`
- **Scripts:** `volley_fire`
- **Mission templates:** `mst_sp_campaign_vienna`, `mst_sp_campaign_austerlitz_1`, `mst_sp_campaign_austerlitz_1_old`, `mst_sp_campaign_dresden_1`, `mst_sp_campaign_dresden_2`
- **Slots:** `troop:60-78 (trp_custom_battle_dummy, fire mode per team/division)`, `troop:80-98 (trp_custom_battle_dummy, volley phase)`, `agent:23`, `item:1`
- **Module-specific resources:** troop: trp_custom_battle_dummy (455)
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `explain nw volley_fire: 5 direct callers, all mst:sp_campaign_*/t5 [every 0s], bare-int call_script`, `dis nw volley_fire: slot 60/70 eq 2 test, phase slot 80/90, agent_set_attack_action 0,1 then 0,0`, `writer of slot 60+div: give_mm_order (l0==2 branch troop_set_slot 455 :l5 :l1)`

<a id="perisnobattle-formations-and-tactics"></a>
### Formation and battle-group AI for field battles — perisno (`perisno.battle_formations_and_tactics`)

**What it does:** In field battles (and ship and rebellion battles) the AI forms ranks, places battle groups around leaders, and picks melee, ranged and skirmish tactics instead of Native's plain charge, with per-team decision numbers and aggressive/defensive cavalry, archer, infantry behaviours.

**How it works:** A master trigger (pnb_mt_mastertrigger, run every 0.1s from mst lead_charge/t64, ship_battle/t56, vinica_rebellion/t57) calls scan_and_cache_agents to count infantry/archers/cavalry into pl_missopt_total_* globals and agent/team slots, then field_tactics -> team_field_melee_tactics (712 stmts) / team_field_ranged_tactics, which use battlegroup_* helpers and form_infantry (552 stmts) to compute positions. order_skirmish_begin_end is present but unreferenced in the call graph.

- **Hooks:** `mst:lead_charge/t64:conseq`, `mst:ship_battle/t56:conseq`, `mst:vinica_rebellion/t57:conseq`
- **Scripts:** `pnb_mt_mastertrigger`, `scan_and_cache_agents`, `field_tactics`, `team_field_melee_tactics`, `team_field_ranged_tactics`, `form_infantry`, `battlegroup_place_around_pos1`, `battlegroup_get_position`, `calculate_decision_numbers`, `order_skirmish_begin_end`
- **Slots:** `agent:15`, `agent:23`, `agent:24`, `agent:25`, `agent:27`, `team:5`, `team:8`, `team:9`, `team:11`, `team:12`, `team:13`
- **Globals:** `battle_phase`, `pl_missopt_total_soldiers`, `ai_team_1_battle_tactic`, `ai_team_2_battle_tactic`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `explain perisno form_infantry: 552 stmts, entry points mst:lead_charge/t64:conseq [every 0.1s] and two more; callers battlegroup_place_around_pos1, team_field_melee_tactics`, `explain perisno team_field_melee_tactics: 712 stmts, writes global battle_phase; reads ai_team_*_battle_tactic`, `explain perisno scan_and_cache_agents: caller pnb_mt_mastertrigger; writes pl_missopt_total_* globals; slots agent[15], team[3..8]`, `Perisno map lists battlegroup_* and cf_*_aggresive_ai as NEW scripts`
- **Notes:** Oddity: some tactic scripts (cf_infantry_aggresive_ai, order_skirmish_begin_end) are unreachable by static call graph; they may be called by computed id or may be dead.

<a id="perisnostarting-orders-screen"></a>
### Starting-orders presentation before joining a battle — perisno (`perisno.starting_orders_screen`)

**What it does:** Before a battle starts the player can open a Starting Orders / troop-organisation screen to set how troop groups are arranged.

**How it works:** menu:join_battle option join_battle_order and menu:simple_encounter option encounter_battle_order open prsnt_troop_organization (and a second version, troop_organization2). The presentation reuses its own event handler. What it writes (probably per-class group settings read by the battle AI) was not traced.

- **Hooks:** `menu:join_battle/opt:join_battle_order:conseq`, `menu:simple_encounter/opt:encounter_battle_order:conseq`
- **Presentations:** `prsnt_troop_organization`, `prsnt_troop_organization2`
- **Relation to Native:** new
- **Confidence:** speculative
- **Evidence:** `refs perisno prsnt prsnt_troop_organization: 3 references (two menu options, one self-reference)`, `link to the formation AI is an assumption from names; not traced`

<a id="popdisciplined-faction-ai-gate"></a>
### Only disciplined armies use formation AI; rabble fights as a mob — pop (`pop.disciplined_faction_ai_gate`)

**What it does:** Before a battle PoP decides whether the enemy is a 'disciplined' force. Bandits, outlaws, rebel peasants, tribal raiders, militia and similar rabble fight without formations or field tactics, while kingdoms, orders and named warlords use the full formation AI. Formation AI and rout behaviour are also switchable in mod options.

**How it works:** set_disciplined_faction (35 stmts; called from 7 menus and 4 mission triggers) sets $g_disciplined_faction = 1, then 0 if the encountered party or its ally ($g_encountered_party / $g_encountered_party_2) belongs to fac_outlaws, fac_red_brotherhood, fac_rebel_peasants, fac_mystmountain, fac_dshar_raiders, fac_militia, fac_mountain_bandits, fac_forest_bandits or fac_singalians AND its template is not a signature warlord (not between pt_wolfbode and pt_refugees). battle_tactic_init_aux / battle_tactic_apply_aux, mst_lead_charge t28-t63 and castle sally triggers test $g_disciplined_faction (and $g_option_formations) before running formation/field-tactics code. $g_option_routing gates the rout trigger mst:lead_charge/t32 (decide_run_away_or_not every 3s).

- **Hooks:** `mst:lead_charge/t28:conseq`, `mst:lead_charge/t32:cond`, `mst:lead_charge/t61:conseq`, `mst:castle_attack_walls_defenders_sally/t51:conseq`, `prsnt:mod_options/t2`
- **Scripts:** `set_disciplined_faction`, `battle_tactic_init_aux`, `battle_tactic_apply_aux`, `orig_decide_run_away_or_not`, `calculate_renown_value`
- **Presentations:** `prsnt_mod_options`, `prsnt_battle`
- **Mission templates:** `mst_lead_charge`, `mst_castle_attack_walls_defenders_sally`
- **Globals:** `g_disciplined_faction`, `g_option_formations`, `g_option_routing`, `g_encountered_party`, `g_encountered_party_2`, `g_encountered_party_faction`
- **Module-specific resources:** faction: fac_outlaws, fac_red_brotherhood, fac_rebel_peasants, fac_militia, fac_mountain_bandits, fac_forest_bandits
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `dis set_disciplined_faction (full)`, `sqlite globals pop g_disciplined_faction: 3 writers in set_disciplined_faction, readers in battle_tactic_*_aux, lead_charge t28-t63, sally t51-t53`, `dis mst:lead_charge/t32:cond: g_option_routing gate`
- **Overlaps:** `acan.thrust_only_formation_weapons`, `acan.vc_battle_stack_inherited`, `acw.scripted_ai_battle_plan`, `ad457.vc_battle_naval_layer_inherited`, `be.ai_battle_tactics_presets`, `be.infantry_square_and_field_works`, `bi.pbod_formations_ai`, `laigle.pbod_motomataru_stack`, `nw.division_gunpowder_ai`, `nw.locator_line_formations`, `pop.formations_battle_ai_kit`, `sw.ranged_backstep_ai`, `tld.formations_motomataru_pop_lineage`, `vc.formations_order_translation`, `vc.persistent_division_formations`

<a id="popformations-battle-ai-kit"></a>
### Formations and field-tactics battle AI (Motomataru-style kit, PoP variant) — pop (`pop.formations_battle_ai_kit`)

**What it does:** AI teams and the player get infantry/archer/cavalry formations (ranks, wedge/shield-wall style infantry, archer lines, cavalry wedges), formation move/hold orders, and a battle-phase AI that positions archers, finds high ground, times charges, sends reinforcements and decides disengagement. Toggleable from PoP's mod options.

**How it works:** Mission-template triggers in mst_lead_charge (t28-t63), mst_castle_attack_walls_defenders_sally, mst_camp_review_soldiers (and the unreferenced mst_ai_training_with_formations) call: cf_formation / form_infantry / form_archers / form_cavalry / set_formation_position / get_formation_position (formation geometry stored in globals formation_<team><class>_x/_y/_rot), player_order_formations + player_attempt_formation (player keys), and field_tactics -> team_field_melee_tactics (1011 stmts) / team_field_ranged_tactics fed by store_battlegroup_data (676 stmts, per-team globals team0_num_infantry.. team3_weapon_length_cavalry). Gated by $g_option_formations (prsnt_mod_options) and $g_disciplined_faction (see pop.disciplined_faction_ai_gate).

- **Hooks:** `mst:lead_charge/t58:conseq`, `mst:lead_charge/t59:conseq`, `mst:lead_charge/t61:conseq`, `mst:lead_charge/t63:conseq`, `mst:castle_attack_walls_defenders_sally/t51:conseq`, `mst:camp_review_soldiers/t25:conseq`, `prsnt:battle/t1`
- **Scripts:** `cf_formation`, `form_infantry`, `form_archers`, `form_cavalry`, `set_formation_position`, `get_formation_position`, `player_order_formations`, `player_attempt_formation`, `formation_move_position`, `formation_current_position`, `get_first_formation_member`, `field_tactics`, `team_field_melee_tactics`, `team_field_ranged_tactics`, `store_battlegroup_data`, `battlegroup_get_position`, `battlegroup_get_size`, `battlegroup_get_level`, `find_high_ground_around_pos1_corrected`, `formation_battle_tactic_apply_aux`, `formation_battle_tactic_init_aux`
- **Presentations:** `prsnt_battle`, `prsnt_mod_options`
- **Mission templates:** `mst_lead_charge`, `mst_castle_attack_walls_defenders_sally`, `mst_camp_review_soldiers`, `mst_ai_training_with_formations`
- **Slots:** `agent:15`
- **Globals:** `g_option_formations`, `infantry_formation_type`, `archer_formation_type`, `cavalry_formation_type`, `formation_00_x .. formation_32_rot`, `team0_num_infantry .. team3_level`, `battle_phase`, `charge_activated`, `disengage`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `explain cf_formation: 33 callers in 4 mission templates`, `explain team_field_melee_tactics: 1011 stmts, globals per team`, `refs pop mt mst_ai_training_with_formations: 0 references (unreachable)`
- **Overlaps:** `acan.thrust_only_formation_weapons`, `acan.vc_battle_stack_inherited`, `acw.scripted_ai_battle_plan`, `ad457.vc_battle_naval_layer_inherited`, `be.ai_battle_tactics_presets`, `be.infantry_square_and_field_works`, `bi.pbod_formations_ai`, `laigle.pbod_motomataru_stack`, `nw.division_gunpowder_ai`, `nw.locator_line_formations`, `pop.disciplined_faction_ai_gate`, `sw.ranged_backstep_ai`, `tld.formations_motomataru_pop_lineage`, `vc.formations_order_translation`, `vc.persistent_division_formations`

<a id="swranged-backstep-ai"></a>
### Ranged troops step back from melee — sw (`sw.ranged_backstep_ai`)

**What it does:** Shooters (archer-class agents with ammo, not ordered to charge) try to keep their distance: they back off 3 m, and keep backing off while an enemy is within 3 m, releasing control once enemies are more than 10 m away.

**How it works:** Every 0.3 s in 12 battle templates ranged_avoid_melee loops class-1 agents holding a non-melee weapon (outside items 758-814) with ammo and team movement order not 'charge'. If agent slot 4 == 1 (in avoid mode): closest enemy (get_closest3_distance_of_enemies_at_pos1) > 10 m -> agent_clear_scripted_mode, slot 4 = 0; <= 3 m -> scripted destination 3 m backwards. Else (not in avoid mode) -> scripted destination 3 m backwards and slot 4 = 1.

- **Hooks:** `mst:custom_battle/t21:conseq`, `mst:lead_charge_no_horse/t50:conseq`, `mst:besiege_inner_battle_castle/t33:conseq`, `mst:minorplanet_raid/t34:conseq`
- **Scripts:** `ranged_avoid_melee`, `get_closest3_distance_of_enemies_at_pos1`
- **Mission templates:** `mst_lead_charge_no_horse`, `mst_custom_battle`, `mst_custom_battle_2vs2`, `mst_custom_battle_standard`, `mst_besiege_inner_battle_castle`, `mst_besiege_inner_battle_town_center`, `mst_minorplanet_attack_bandits`, `mst_minorplanet_raid`, `mst_bandits_at_night`, `mst_back_alley_revolt`, `mst_sneak_caught_fight`, `mst_spacestation_attack_walls_defenders_sally`
- **Slots:** `agent:4 (avoid mode flag)`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis sw ranged_avoid_melee (41 stmts)`, `explain sw ranged_avoid_melee: 12 callers [every 0.3s]`
- **Overlaps:** `acan.thrust_only_formation_weapons`, `acan.vc_battle_stack_inherited`, `acw.scripted_ai_battle_plan`, `ad457.vc_battle_naval_layer_inherited`, `be.ai_battle_tactics_presets`, `be.infantry_square_and_field_works`, `bi.pbod_formations_ai`, `laigle.pbod_motomataru_stack`, `nw.division_gunpowder_ai`, `nw.locator_line_formations`, `pop.disciplined_faction_ai_gate`, `pop.formations_battle_ai_kit`, `tld.formations_motomataru_pop_lineage`, `vc.formations_order_translation`, `vc.persistent_division_formations`

<a id="tldformations-motomataru-pop-lineage"></a>
### Formations and battle AI (PoP-lineage set plus Motomataru '_moto' set, weapon-type orders) — tld (`tld.formations_motomataru_pop_lineage`)

**What it does:** TLD ships two complete formation/battle-AI packages side by side: the older formations kit it shares with Prophesy of Pendor (ranks, shieldwall, wedge, square via J/K/L keys; AI field tactics) and a newer Motomataru '_moto' kit with division placement, battlegroup data and improved melee/ranged tactics, plus a large 'order weapon type switch' command set (switch division to ranged/melee/polearm/shields).

**How it works:** PoP-lineage: cf_formation, form_infantry/form_archers/form_cavalry, player_order_formations, store_battlegroup_data, team_field_melee_tactics (1048 stmts) and team_field_ranged_tactics, called from mission templates and prsnt:formation_mod_option / prsnt:show_key_binds. Motomataru set: every name with _moto suffix (form_infantry_moto 708, store_battlegroup_data_moto 486, team_field_melee_tactics_moto 684, player_order_formations_moto 378, process_player_division_positioning_moto, memorize/default_division_placements_moto). order_weapon_type_switch (400 stmts) iterates agents of selected divisions and equips the matching weapon class. Options in menu:camp_field_ai toggle lord/horse-archer AI and archer aim vs orcs.

- **Hooks:** `mst:lead_charge (formation triggers)`, `prsnt:formation_mod_option/t0`, `prsnt:show_key_binds/t0`, `menu:camp_field_ai`
- **Scripts:** `cf_formation`, `form_infantry`, `form_archers`, `form_cavalry`, `player_order_formations`, `store_battlegroup_data`, `team_field_melee_tactics`, `team_field_ranged_tactics`, `form_infantry_moto`, `player_order_formations_moto`, `store_battlegroup_data_moto`, `team_field_melee_tactics_moto`, `order_weapon_type_switch`, `equip_best_melee_weapon_moto`, `get_item_modifier_effects_moto`
- **Menus:** `menu:camp_field_ai`
- **Presentations:** `prsnt:formation_mod_option`, `prsnt:show_key_binds`, `prsnt:order_display`
- **Slots:** `agent:12`, `agent:13`, `agent:14`, `agent:17`, `agent:24`, `agent:25`, `agent:28`, `team:1..13`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `auto report: _moto scripts all NEW with mst/prsnt entry points`
- **Overlaps:** `acan.thrust_only_formation_weapons`, `acan.vc_battle_stack_inherited`, `acw.scripted_ai_battle_plan`, `ad457.vc_battle_naval_layer_inherited`, `be.ai_battle_tactics_presets`, `be.infantry_square_and_field_works`, `bi.pbod_formations_ai`, `laigle.pbod_motomataru_stack`, `nw.division_gunpowder_ai`, `nw.locator_line_formations`, `pop.disciplined_faction_ai_gate`, `pop.formations_battle_ai_kit`, `sw.ranged_backstep_ai`, `vc.formations_order_translation`, `vc.persistent_division_formations`

<a id="vcformations-order-translation"></a>
### Formations v2 with on/off toggle and native-rank fallback — vc (`vc.formations_order_translation`)

**What it does:** VC ships a newer Motomataru 'complex formations' build: complex formations can be switched off in VC's options screen; when on, formation orders form true formations (ranks, shield wall, wedge, column); when off, the same orders fall back to Warband's native spacing orders. A first-use dialog explains the system.

**How it works:** Keyboard entry: mst:lead_charge/t133 (game_key_clicked 26 = order key) reads $FormAI_off (written only by prsnt:vc_options/t2): when on it sets $gk_order=26, shows prsnt_order_display (when $controller_in_use=0) and a one-time dialog_box (str_formations, bit 1024 of $first_time); when off it prints 'Formations turned OFF'; t129 (F1 hold-timer, $when_f1_first_detected >=250 ms), t136 (key_f7) and t137 (key_f8) dispatch to the formation scripts. Each formation key calls player_order_extended_formations (if $FormAI_off=0 -> player_attempt_formation per listening division) or player_order_regular_formations (-> formation_to_native_order). formation_to_native_order issues team_give_order stand_closer (7) N times to reach the requested spacing; its rank orders (mordr_form_1..5_row = 22..26) sit behind an always-true (eq,0,0) branch and are therefore dead code in this build. pick_native_formation -> calculate_default_ranks picks a rank count from division size. Support: form_infantry (536), form_cavalry, form_archers, battlegroup_place_around_pos1, store_battlegroup_data (486), formation_end, agent_fix_division. Wired into lead_charge, village_attack_bandits, village_raid, quick_battle_battle and VC story battles.

- **Hooks:** `mst:lead_charge/t133:conseq`, `mst:lead_charge/t129:conseq`, `mst:lead_charge/t137:conseq`, `mst:lead_charge/t126:conseq`
- **Scripts:** `player_order_formations`, `player_order_extended_formations`, `player_order_regular_formations`, `formation_to_native_order`, `pick_native_formation`, `calculate_default_ranks`, `player_attempt_formation`, `form_infantry`, `form_cavalry`, `form_archers`, `formation_end`, `store_battlegroup_data`, `battlegroup_place_around_pos1`, `get_default_formation`, `cf_valid_formation_member`, `switch_to_noswing_weapons`, `switch_from_noswing_weapons`
- **Presentations:** `prsnt_order_display`, `prsnt_vc_options`
- **Mission templates:** `mst_lead_charge`, `mst_village_attack_bandits`, `mst_village_raid`, `mst_quick_battle_battle`
- **Slots:** `team:14+div`, `team:194+div`, `team:203+div`, `team:221+div`, `team:293+div`
- **Globals:** `FormAI_off`, `gk_order`, `when_f1_first_detected`, `fplayer_team_no`, `FormAI_autorotate`, `FormAI_AI_no_defense`, `FormAI_player_in_division`, `first_time`, `controller_in_use`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis vc mst:lead_charge/t133:cond = game_key_clicked 26; conseq branches on $FormAI_off ($gk_order=26, prsnt_order_display, dialog_box str_formations) else 'Formations turned OFF'; sqlite globals: $FormAI_off written only in prsnt:vc_options/t2`, `dis vc formation_to_native_order: (eq,0,0) makes the form_N_row branches unreachable; only stand_closer(7) loop runs`, `dis vc player_order_regular/extended_formations: per listening class, team slots 293/14/194/221`
- **Overlaps:** `acan.thrust_only_formation_weapons`, `acan.vc_battle_stack_inherited`, `acw.scripted_ai_battle_plan`, `ad457.vc_battle_naval_layer_inherited`, `be.ai_battle_tactics_presets`, `be.infantry_square_and_field_works`, `bi.pbod_formations_ai`, `laigle.pbod_motomataru_stack`, `nw.division_gunpowder_ai`, `nw.locator_line_formations`, `pop.disciplined_faction_ai_gate`, `pop.formations_battle_ai_kit`, `sw.ranged_backstep_ai`, `tld.formations_motomataru_pop_lineage`, `vc.persistent_division_formations`

<a id="acanchariots-wse2"></a>
### Drivable chariots and chariot races (requires WSE2) — acan (`acan.chariots_wse2`)

**What it does:** Chariot 'horses' are items that spawn a chariot prop the rider drives, with crash and high-speed damage and a chariot camera. Dismounting a chariot needs a non-vanilla opcode, and the module itself says chariot races need WSE2.

**How it works:** init_chariot_item (ti_on_init_item on itm_basic_chariot_horse / _b_horse / quadriga) sets up the prop. chariot_trigger (522 call sites, every 0.5 s) moves the prop with the horse agent and calls check_chariots_crashed. chariot_on_destruction handles breakage. Each of about 174 templates has a dismount trigger that calls NON-VANILLA opcode 3313 (agent, -1), most consistent with WSE's 'detach rider from horse', then plays the dismount_chariot animation.

- **Hooks:** `itm:itm_basic_chariot_horse/t0`, `mst:town_default/t45:conseq`, `mst:lead_charge/t145:conseq`
- **Scripts:** `init_chariot_item`, `chariot_trigger`, `check_chariots_crashed`, `chariot_on_destruction`
- **Mission templates:** `mst_horse_racing`, `mst_town_default`, `mst_lead_charge`
- **Slots:** `agent:2`, `scene_prop:1`, `scene_prop:2`, `scene_prop:3`, `scene_prop:4`
- **Globals:** `g_player_chariot_agent`
- **Module-specific resources:** item: itm_basic_chariot_horse, itm_basic_chariot_b_horse, itm_quadriga_chariot_horse; anim: dismount_chariot
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `grep UNKNOWN_op3313 --mods acan: one dismount trigger per template, '(UNKNOWN_op3313, :l0, -1)' then agent_set_animation dismount_chariot`, `explain acan init_chariot_item: text 'Chariot races are only available if you are using WSE2.'`, `explain acan chariot_trigger: 522 callers, crash/high-speed damage texts`

<a id="acanspawn-equipment-variety-and-item-quality"></a>
### Spawn-time equipment variety and item-quality steps, plus blacksmith item improvement — acan (`acan.spawn_equipment_variety_and_item_quality`)

**What it does:** When a soldier spawns, his gear is reshuffled from his troop's inventory: a random helmet, armour or weapon from the allowed set, with surplus weapons dropped. Items can carry better or worse quality modifiers. A town or estate smith can upgrade an item one quality step for a fee.

**How it works:** ti_on_agent_spawn triggers in 25 templates (e.g. mst:bandit_lair/t43, 256 stmts) collect the troop's inventory items of a type with their modifiers (troop_get_inventory_slot_modifier), shuffle them (shuffle_troop_slots) and agent_equip_item one with its modifier. They also unequip duplicate one-handed or two-handed weapons and handle special troops. get_next_higher_imod_for_item / get_next_lower_imod_for_item (77/75 callers) step a modifier along the quality ladder, and get_item_modifier_effects names it. Smith dialogs (dlg:9564 item_improve, dlg:11325 lat_item_improve) quote and apply one step up. evaluate_item / equip_best_melee_weapon pick the best weapon for AI.

- **Hooks:** `mst:bandit_lair/t43:conseq (ti_on_agent_spawn)`, `mst:lead_charge (ti_on_agent_spawn)`, `dlg:9564:dlga_item_improve_1`, `dlg:11325:dlga_lat_item_improve_1`
- **Scripts:** `get_next_higher_imod_for_item`, `get_next_lower_imod_for_item`, `get_item_modifier_effects`, `shuffle_troop_slots`, `evaluate_item`, `equip_best_melee_weapon`
- **Globals:** `cheat_mode`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `dis acan mst:bandit_lair/t43:conseq: inventory collection by item type with modifiers, shuffle, agent_equip_item with modifier, duplicate weapon removal`, `explain acan get_next_higher_imod_for_item: 77 callers incl. item_improve dialogs`, `compare get_next_higher_imod_for_item / get_item_modifier_effects: vc 100%`
- **Overlaps:** `cbl.campaign_balance_retune`

<a id="acwexplosive-grenades"></a>
### Thrown hand grenades with area damage — acw (`acw.explosive_grenades`)

**What it does:** Two throwable grenades (Union 'Ketchum Grenade', Confederate 'Artillery Shell Grenade', 3 per stack) explode where they land: a bang, flash, smoke and debris, and every living person within 3 m (friend or foe, except the thrower) takes 100-299 damage.

**How it works:** Items itm_stones (renamed 'Ketchum Grenade', merchandise for kingdoms 1/2/7) and itm_grenade ('Artillery Shell Grenade', kingdoms 4/5/6): itp_type_thrown, max_ammo 3, thrust 100 pierce. Inline ti_on_missile_hit: copy hit position, play_sound_at_position snd_grenade, particle bursts (firearm_flash_original, musket_smoke, ladder_straw_6m/12m) ONCE at the impact point, then try_for_agents: alive, not the thrower, distance <= 300 cm -> agent_deliver_damage_to_agent thrower -> target, random 100-299, credited to the grenade item. No damage fall-off, no team check.

- **Hooks:** `itm:itm_stones/t0`, `itm:itm_grenade/t0`
- **Module-specific resources:** item: itm_stones (Ketchum Grenade), itm_grenade; sound: snd_grenade; psys: psys_firearm_flash_original, psys_musket_smoke, psys_ladder_straw_6m, psys_ladder_straw_12m
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `grep agent_deliver_damage_to_agent --mods acw --kinds itm -> itm:itm_stones/t0, itm:itm_grenade/t0 (and the cannonball item)`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_items.py 609-648 item definitions with inline ti_on_missile_hit`
- **Overlaps:** `awoiaf.fire_arrows_destructible_props`, `be.ww1_weapons_mg_gas_grenades`, `nw.explosives_destructible_props`, `oa1860.explosive_and_destructible_props`, `oa1860.explosive_thrown_weapons`, `sw.scripted_grenade_ballistics`

<a id="acwfield-artillery"></a>
### Recruitable field artillery batteries (player + AI lords) — acw (`acw.field_artillery`)

**What it does:** The player buys up to 2 field guns (6 types: 12-pdr Napoleon, 10-pdr Parrott, 3-inch Ordnance, 12/24-pdr howitzers, 6-pdr M1841) at a town foundry; each comes with a 3-man crew that joins the party. In field battles the guns are spawned as scene props in front of the player, crews walk to them and fire simulated cannonballs with splash damage and knock-down. Enemy lords' armies spawn 1-2 guns of their own.

**How it works:** Campaign: menu:cannon_recruitment (from the town foundry option) -> add_cannon_crew increments party slots 381-386 (one counter per gun type, slot index computed by get_cannon_count_per_type) and party_add_members a faction-specific cannon_operator troop (get_cannon_operator_for_faction) x3; cap reg8=2 guns (get_cannon_count). refill_crew_members tops crews up to 3/gun at $100 each; disband options call remove_cannon_crew. Battle (lead_charge, also siege/village_raid templates): t27 (ti_after_mission_start +3s) finds high ground 9 battlegroups toward the enemy (find_high_ground_around_pos1_corrected) and, if the enemy is a lord party (party slot 0 == 13) not Native faction and whose signature troop (troop slot 374) is not mounted, spawn_cannon_pos2 spawns 1 (2 if the player owns guns) random cannon prop + 3 revolver-armed crew agents (division 8), storing crew in scene_prop slots 300-302 and the prop in trp_cannon_array. t29 spawns the player's guns (one prop per counter in slots 381-386, max 4) 10 m ahead of the player and binds existing crew agents via cf_connect_cannons_and_operators (agent slot 303 = bound gun, scripted destinations around the gun). t30 every 1s checks crews: gun manned (prop slot 305) if the loader plus one helper alive; otherwise survivors are released. t32/t33 pick targets and rotate the barrel (brute_rotate_direction/brute_rotation_check). t34 every 3s fires: unless the artillery division (8) has hold-fire ordered, spawns an mp_cannonball prop with target = target agent pos +/-10 m scatter, flight countdown = distance/100 (prop slot 306), reload 30-39 s (slot 308), smoke/flash/sound; enemy crews draw revolvers. t35 every 1s lands balls: AoE damage 35-85 (+5*(1+gun type)) multiplied at <=1 m, full <=2 m, half <=4 m, quarter <=5 m via agent_deliver_damage_to_agent from the loader, knock-down animation for unmounted humans within 5 m. [Source names] Kit credited to DrTomas ('####DrTomas constants', '##DrTomas Cannon script'). Mission triggers are named tuples in module_mission_templates.py 3522-5090 ('#### cannons start/end'): list `cannons` = cannons_count, cannons_spawn_enemy, cannons_spawn_freelancer, cannons_spawn, cannons_operation_check, cannons_select_targets, cannons_rotate_to_target, cannons_reload, cannons_shoot, cannons_balls_move; variants `cannons_siege`, `cannons_village`, `cannons_custom` (custom battles). Tunables (module_constants.py 2741-2780): cannon_cost 3000, cannon_count_per_party 2, cannon_count_per_side 4, operators_per_cannon 3, cannon_reload_timer 30, cannon_division 8, battle/siege entry-point constants (battle_cannon_entry_point_* 1/3/4, siege_cannon_entry_point_* 0/40).

- **Hooks:** `menu:cannon_recruitment`, `mst:lead_charge/t27:conseq`, `mst:lead_charge/t28:conseq`, `mst:lead_charge/t29:conseq`, `mst:lead_charge/t30:conseq`, `mst:lead_charge/t32:conseq`, `mst:lead_charge/t33:conseq`, `mst:lead_charge/t34:conseq`, `mst:lead_charge/t35:conseq`, `mst:castle_attack_walls_ladder/t26:conseq`, `mst:castle_attack_walls_belfry/t28:conseq`, `mst:castle_attack_walls_defenders_sally/t20:conseq`
- **Scripts:** `add_cannon_crew`, `remove_cannon_crew`, `get_cannon_count`, `get_cannon_count_per_type`, `get_cannon_operator_for_faction`, `spawn_cannon_pos2`, `spawn_cannon_pos2_freelancer`, `spawn_cannon_pos2_custom`, `spawn_cannon_new`, `cf_connect_cannons_and_operators`, `brute_rotate_direction`, `brute_rotation_check`, `rotate_pos31_towards_pos30_xy`, `rotate_pos31_towards_pos30_yz`, `turn_pos_towards_pos`, `find_high_ground_around_pos1_corrected`, `team_get_position_of_enemies`, `store_battlegroup_data`
- **Menus:** `menu_cannon_recruitment`
- **Mission templates:** `mst_lead_charge`, `mst_castle_attack_walls_ladder`, `mst_castle_attack_walls_belfry`, `mst_castle_attack_walls_defenders_sally`, `mst_village_raid`, `mst_quick_battle_battle`, `mst_quick_battle_siege`
- **Slots:** `party:381`, `party:382`, `party:383`, `party:384`, `party:385`, `party:386`, `troop:374`, `agent:51`, `agent:301`, `agent:302`, `agent:303`, `scene_prop:300`, `scene_prop:301`, `scene_prop:302`, `scene_prop:304`, `scene_prop:305`, `scene_prop:306`, `scene_prop:307`, `scene_prop:308`, `scene_prop:309`, `agent:300`
- **Globals:** `total_cannon_count`, `freelancer_state`, `king_start`, `king_faction`
- **Module-specific resources:** spr: spr_cannon_m1841, spr_cannon_howitzer_12lb, spr_cannon_howitzer_24lb, spr_mp_cannon_12lb, spr_mp_cannon_6lb, spr_mp_cannon_3lb, spr_mp_cannonball_3lb; troop: trp_cannon_array, trp_cannon_operator, trp_union_cannon_operator_1.., trp_csa_cannon_operator_1..; psys: psys_cannon_smoke_madsci, psys_cannon_flash_madsci, psys_cannon_impact_smoke, psys_cannon_dirt; sound: snd_cannon_fire_a, snd_explosion1, snd_near_impact; item: itm_colt_navy_1861_revolver, itm_cartridges_revolver
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis acw spawn_cannon_pos2 / get_cannon_count / add_cannon_crew / cf_connect_cannons_and_operators`, `dis acw mst:lead_charge/t27,t29,t30,t34,t35`, `menu:cannon_recruitment cap reg8=2 and refill at 100/man`, `FAQ: 'recruit artillery from the foundry... crews at the very top of your party list... player's cannons only spawn in battles where the player is fighting alone' matches t29 (crews bound by agent iteration at ti_after_mission_start) and t28 freelancer variant`, `changelog: 'Fixed artillery being bugged in battles where the player is helping an allied general' -> t28 spawn_cannon_pos2_freelancer path`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_constants.py 2715-2810 (DrTomas cannon constants and slot names)`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_mission_templates.py 3522-5090 named trigger tuples cannons_* and lists cannons/cannons_siege/cannons_village/cannons_custom`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_items.py 3529 itm_cannonball ti_on_missile_hit (bug confirmed)`
- **Overlaps:** `be.field_artillery_batteries`, `laigle.artillery_park`, `laigle.field_artillery`, `nw.crewed_artillery`, `oa1860.scripted_ballistic_hand_cannon`

<a id="acwmulti-projectile-firearms"></a>
### Buck-and-ball / shotgun multi-pellet fire, distance-tiered gunshot sound, pan smoke and shell ejection — acw (`acw.multi_projectile_firearms`)

**What it does:** Every firearm has an on-attack item trigger: buck-and-ball muskets fire 1 ball + 3 buckshot, shotguns fire 8 pellets in a cone, flintlocks puff pan smoke, Spencer/Henry repeaters eject a visible shell, and the gunshot sound switches between far/medium/close depending on the camera distance.

**How it works:** Item triggers ti_on_weapon_attack (110 item-trigger blocks). Common body: mission_cam_get_position -> get_distance_between_positions_in_meters to the muzzle (pos1) -> play snd_gunshot_far (>=71 m) / _medium (60-70 m) / per-gun close sound; particle bursts musket_smoke, muzzle_sparks, firearm_flash at muzzle (+pan_smoke for flintlocks). Buck variants (itm_springfield_18xx_buck): store_trigger_param_1 shooter, add_missile of the main ball (itm_cartridges_musket, speed 8000) then a 3-iteration loop that copies the muzzle position, rotates it by a random +/-0.15 deg spread (position_rotate_x/y_floating) and add_missile itm_cartridges_shotgun. Shotguns/coachguns/sawed-off: 8-iteration loop with +/-2 deg spread. Spencer/Henry: extra particle_system_burst psys_shell_ejection_spencer(_fp) offset to the breech, first-person vs third-person offsets (is_camera_in_first_person).

- **Hooks:** `itm:itm_springfield_1842_buck/t0`, `itm:itm_shotgun/t0`, `itm:itm_coachgun/t0`, `itm:itm_sawed_off_shotgun/t0`, `itm:itm_spencer_rifle/t0`, `itm:itm_spencer_carbine/t0`, `itm:itm_henry_a/t0`, `itm:itm_springfield_1835_flint/t0`
- **Module-specific resources:** item: itm_cartridges_musket, itm_cartridges_shotgun, *_buck musket variants, itm_shotgun, itm_coachgun, itm_sawed_off_shotgun, itm_spencer_rifle, itm_henry_a; psys: psys_musket_smoke, psys_muzzle_sparks, psys_firearm_flash, psys_pan_smoke, psys_shell_ejection_spencer, psys_shell_ejection_spencer_fp; sound: snd_gunshot_far, snd_gunshot_medium, snd_gunshot_close, snd_shotgun, snd_spencer_carbine
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis acw itm:itm_springfield_1842_buck/t0 (1 + 3 add_missile)`, `dis acw itm:itm_shotgun/t0 (8 add_missile)`, `dis acw itm:itm_spencer_rifle/t0 (shell ejection)`, `changelog: 'Muskets that fire buck & ball will now shoot the correct number of 4 projectiles... All shotguns will now fire 8 projectiles... Created a simple shell ejection system for the Henrys and Spencers' -> verified`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_items.py springfield_1842_buck / shotgun / coachgun ti_on_weapon_attack bodies read in full`
- **Overlaps:** `be.firearm_hit_damage_model`, `be.missile_launch_firing_effects`, `be.shotgun_pellet_spread`, `cbl.flintlock_item_triggers`, `laigle.musket_item_effects`, `nw.missile_launch_effects`, `oa1860.firearm_muzzle_effects`

<a id="acwrifle-iron-sight-zoom"></a>
### Iron-sight aiming / zoom camera for long arms — acw (`acw.rifle_iron_sight_zoom`)

**What it does:** On foot in first person with a listed rifle-musket, holding attack lifts the camera to the sight line, and holding the zoom key additionally narrows the field of view (aperture 45) - a simple iron-sights/scope effect.

**How it works:** Every-frame mission trigger mst:lead_charge/t22 (also duplicated in the hunting templates' t1): if game key 20 (view character) is held -> normal camera; else if wielded item is in a hardcoded list of ~70 long guns and game key 19 (zoom) is down, on foot, first person -> agent_get_look_position, offset +7 x, +36 z, +17 y then +127 z with rotation preserved, mission_cam_set_mode 1, mission_cam_set_position, mission_cam_set_aperture 45; else if game key 6 (attack) down -> same offset without aperture change; else mission_cam_set_mode 0.

- **Hooks:** `mst:lead_charge/t22:conseq`, `mst:deer_hunting/t1:conseq`, `mst:boar_hunting/t1:conseq`, `mst:buffalo_hunting/t1:conseq`
- **Mission templates:** `mst_lead_charge`, `mst_deer_hunting`, `mst_boar_hunting`, `mst_buffalo_hunting`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis acw mst:lead_charge/t22:conseq (200 stmts: list + camera ops)`, `game key numbering per Warband header_triggers: 6 attack, 19 zoom, 20 view character (consistent with t23 using 29-38 = group-select keys)`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_mission_templates.py 1573 singleplayer_ironsight_mode`
- **Overlaps:** `be.ironsight_aiming`, `sw.scope_and_visor_overlays`

<a id="awoiaffire-arrows-destructible-props"></a>
### Fire arrows and burnable/destructible siege props — awoiaf (`awoiaf.fire_arrows_destructible_props`)

**What it does:** In siege battles archers can switch to fire arrows; arrows hitting flammable scene props (palisades, towers, houses, tents, belfries, the battering ram) spawn fire and smoke, wear down the prop's durability and finally destroy it - burning a belfry or ram stops that line of assault.

**How it works:** Siege templates (mst_castle_attack_walls_belfry/_ladder/_ram, t118/t120 every 0.01s) run fire_arrow_routine / flame_routine; initialize_agents_use_fire_arrow + toggle_fire_arrow_mode flip $g_fire_arrow_mode. 14 bows have ti_on_weapon_attack item triggers -> cf_set_fire_arrow (attaches flame to the missile while the mode is on). 386 scene props carry ti_on_scene_prop_hit -> cf_flammable_object_hit: hit_prop resolves damage, particle bursts (psys_fire_glow_1, cooking_fire, torch sparks), durability is stored in parallel troop arrays (trp_object_instance_no / trp_object_durability / trp_scene_prop_id indexed up to $g_flammable_object_slot); at 0 -> object_destroy, and for spr_belfry_* / spr_ram_body also destroys their platforms/wheels and sets $g_belfry_was_destroyed / $g_ram_was_destroyed. flammable_object_initialize / destructible_object_initialize register props at mission start.

- **Hooks:** `mst:castle_attack_walls_belfry/t120:conseq`, `mst:castle_attack_walls_ladder/t118:conseq`, `mst:castle_attack_walls_ram/t120:conseq`, `itm:itm_war_bow/t0`, `spr:spr_castle_z_tower/t1`
- **Scripts:** `fire_arrow_routine`, `flame_routine`, `cf_set_fire_arrow`, `toggle_fire_arrow_mode`, `initialize_agents_use_fire_arrow`, `cf_flammable_object_hit`, `hit_prop`, `object_destroy`, `flammable_object_initialize`, `destructible_object_initialize`, `cf_object_set_damage`
- **Mission templates:** `mst_castle_attack_walls_belfry`, `mst_castle_attack_walls_ladder`, `mst_castle_attack_walls_ram`
- **Globals:** `g_fire_arrow_mode`, `g_flammable_object_slot`, `g_flame_slot`, `g_belfry_was_destroyed`, `g_ram_was_destroyed`
- **Module-specific resources:** troop: trp_object_instance_no, trp_object_durability, trp_scene_prop_id, trp_frame_tick_count, trp_global_value; psys: psys_fire_glow_1, psys_cooking_fire_1, psys_war_smoke_tall; item: 14 bows with ti_on_weapon_attack
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `roots cf_flammable_object_hit -> 386 spr:*/t1 [ti_on_scene_prop_hit]`, `roots cf_set_fire_arrow -> 14 itm:*/t0 [ti_on_weapon_attack]`, `roots fire_arrow_routine -> mst:castle_attack_walls_* t118/t120 + multiplayer msts`, `dis cf_flammable_object_hit: durability arrays, belfry/ram destruction messages`
- **Overlaps:** `acw.explosive_grenades`, `be.ww1_weapons_mg_gas_grenades`, `nw.explosives_destructible_props`, `oa1860.explosive_and_destructible_props`, `oa1860.explosive_thrown_weapons`, `sw.scripted_grenade_ballistics`

<a id="befield-artillery-batteries"></a>
### Crewed field-gun and howitzer batteries (Yuri cannon system) — be (`be.field_artillery_batteries`)

**What it does:** Artillery-officer troops in a party turn into a fully animated gun battery when they spawn in battle: the officer brings three gunners and a multi-part gun (body, wheels, barrel, ropes, ramrods, shell). The crew walks to stations, swabs, loads, aims, fires; shells fly in an arc and explode with radial damage, craters and morale shock. Field guns fire flat at the officer's AI target; howitzers fire at 45 degrees.

**How it works:** Spawn: every mission template's ti_on_agent_spawn trigger (e.g. mst:lead_charge/t98) calls cf_YuriSpawnCannon(agent). If the agent is a cannoneer-officer troop (trp_factionplayer_fieldgun_cannoneer_officer..trp_factionplayer_fieldgun_cannoneer) and the team's battery counter team slot 178 (+ allied team's) is below 5 (10 with technology faction slot 416), it spawns 3 crew agents from the faction's crew troop (faction slot 403/404), spawns rope/ramrod/cannonball props, wheels and barrel, then the body last; the body's own ti_on_scene_prop_init (spr_*_body/t0 -> cannon_body_spawn) copies the just-set globals $g_cannoneer_officer/$g_cannoneer1-3/$g_rope1.../$g_barrel into scene_prop slots 192-206 and sets per-model geometry/reload slots 189-191, 209, 210, 213 (0=gun,1=howitzer), 214. Excess officers fade out. Gun model tier (1/2/3) is chosen by technology slots 415/416. Loop: mst:lead_charge/t95 (every 0.033 s) iterates every spr_fieldgun_1_body..spr_fieldgun_1_wheels instance and runs cannon_reassign_cannoneers, cannon_tick_timer, cannon_process_moving, cannon_process_reloading, cannon_process_aiming; scene_prop slot 197 is the state machine (2 arrive ->3 load ->4 aim ->5..7 ready -> 8 fired), slot 196 the countdown timer. cannon_fire plays crew Yuri_* animations, sets the shell prop's flight slots (167 in-flight, 177 projectile type from get_cannoneer_officer_faction_cannon_projectile_type, 178 calibre), animates the shell with prop_instance_animate_to_position (time = distance/150) at a randomised point near agent_ai_get_look_target (howitzer: rotate 45 deg, store target in slots 220-223), bursts psys_cannon_smoke/psys_musket_flash, plays near/far sounds. mst:lead_charge/t96 (every 0.01 s) detects arrival -> shell_hits_pos: 65-95% chance explode_at_pos (radial agent_deliver_damage_to_agent scaled by distance, /10 in trench, /2 prone, knock-down animation, adds suppression to team slot 52+division) else a bounce/crater prop (max 400 craters); gas shells spawn spr_gas_shell. YuriBatteryHoldPosition answers player orders (t97), cf_YuriCannonCanoneersRetreat (t59) handles crew rout.

- **Hooks:** `mst:lead_charge/t98:conseq`, `mst:lead_charge/t95:conseq`, `mst:lead_charge/t96:conseq`, `mst:lead_charge/t97:conseq`, `mst:lead_charge/t59:cond`, `spr:spr_fieldgun_1_body/t0`, `spr:spr_howitzer_1_body/t0`, `spr:spr_heavyhowitzer_3_body/t0`
- **Scripts:** `cf_YuriSpawnCannon`, `cannon_body_spawn`, `cannon_reassign_cannoneers`, `cannon_tick_timer`, `cannon_process_moving`, `cannon_process_reloading`, `cannon_process_aiming`, `cannon_fire`, `cannon_cancel_cannoneers_animations`, `shell_hits_pos`, `explode_at_pos`, `YuriBatteryHoldPosition`, `cf_YuriCannonCanoneersRetreat`, `cf_Yuri_DidCannoneerArriveAtHisPosition`, `cf_Yuri_IsAgentAlive`, `Yuri_PosAllignToGroundLevel`, `Yuri_PosAllignToTerrainLevel`, `get_cannoneer_officer_faction_cannon_projectile_type`, `play_distant_sound_at_pos_based_on_distance`, `turn_pos_towards_pos`, `get_modulus_of_value`, `YuriGetAngleForHowitzerAiming`, `Yuri_CannoneerApplyRamrodStance`
- **Menus:** `menu_cannoneers_store`
- **Presentations:** `prsnt_pbs`
- **Mission templates:** `all 25 (lead_charge, castle_attack_walls_*, besiege_inner_battle_*, town/arena/training templates too)`
- **Slots:** `scene_prop:167`, `scene_prop:177`, `scene_prop:178`, `scene_prop:189`, `scene_prop:190`, `scene_prop:191`, `scene_prop:192`, `scene_prop:193`, `scene_prop:194`, `scene_prop:195`, `scene_prop:196`, `scene_prop:197`, `scene_prop:200`, `scene_prop:201`, `scene_prop:202`, `scene_prop:203`, `scene_prop:204`, `scene_prop:205`, `scene_prop:206`, `scene_prop:209`, `scene_prop:210`, `scene_prop:213`, `scene_prop:214`, `scene_prop:216`, `scene_prop:220`, `scene_prop:221`, `scene_prop:222`, `scene_prop:223`, `team:178`, `agent:38`, `agent:61`, `faction:403`, `faction:404`, `faction:415`, `faction:416`
- **Globals:** `g_cannoneer_officer`, `g_cannoneer1`, `g_cannoneer2`, `g_cannoneer3`, `g_rope1`, `g_rope2`, `g_ramrod1`, `g_ramrod2`, `g_shell`, `g_wheels`, `g_barrel`, `number_of_craters`, `battle_timer`, `g_battle_type`
- **Module-specific resources:** spr: spr_fieldgun_1/2/3_body|wheels|barrel, spr_howitzer_1/2/3_*, spr_heavyhowitzer_3_*, spr_YuriCannon1_Rope1/2, spr_YuriCannon1_Ramrod1/2, spr_YuriCannon1_Cannonball, spr_YuriCannonballCrater, spr_YuriShellCrater, spr_gas_shell, spr_pai_artillery_position; anim: Yuri_CannonAiming, Yuri_CannonLighting(_Shot), Yuri_CannonEarsPlugging_Left/Right(_Shot), Yuri_CannonRamrod*, Yuri_CannonBarrelCleaning*, Yuri_CannonCartridgeInserting(Breech), Yuri_CannonRopePulling_Left/Right, YuriCancelAnimation; sound: snd_Yuri_Cannon_Fire1, snd_Yuri_Cannon_Fire_Far1, snd_Yuri_CannonballHit_Ground; psys: psys_cannon_smoke, psys_musket_flash, psys_cannon_ball_hit, psys_explosion_smoke_*; troop: trp_factionplayer_fieldgun_cannoneer_officer, trp_factionplayer_howitzer_cannoneer_officer, trp_factionplayer_heavyhowitzer_cannoneer_officer, trp_factionplayer_fieldgun_cannoneer, trp_cannoneers_end
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis be cf_YuriSpawnCannon (168 stmts): officer->3 crew + 7 props, cap team slot 178 <5/<10 (tech 416)`, `callers be cannon_body_spawn: 7 spr *_body ti_on_scene_prop_init triggers copy $g_cannoneer*/$g_* into prop slots 192-206`, `dis be mst:lead_charge/t95:conseq: per-prop state machine slot 197, every 0.033 s`, `dis be cannon_fire / shell_hits_pos / explode_at_pos: animate_to_position flight, 45-deg howitzer branch, radial damage with trench/prone divisors and team 52+div suppression`
- **Overlaps:** `acw.field_artillery`, `laigle.artillery_park`, `laigle.field_artillery`, `nw.crewed_artillery`, `oa1860.scripted_ballistic_hand_cannon`
- **Notes:** Oddity: the artillery triggers are injected into all 25 templates including arena and tavern ones (cf_YuriSpawnCannon only gates on $g_battle_type != 5).

<a id="befirearm-hit-damage-model"></a>
### Firearm range falloff, headshots and cover in one hit trigger — be (`be.firearm_hit_damage_model`)

**What it does:** Every rifle/carbine/LMG hit is recomputed: full damage up to 50 m, sliding down to 75 % at 175 m and beyond, doubled on a head hit, scaled by the player's friendly-fire and damage-to-player difficulty options, and cut to a third for siege defenders shot from 10 m or more (they are behind walls).

**How it works:** mst:lead_charge/t101 (ti_on_agent_hit, present in all 25 templates). Reads the attacking item from reg0; if it is itm_damage_pure, passes damage through. For listed firearm ranges (is_between blocks of rifle families + explicit items) it takes item_get_thrust_damage as base, gets distance in metres between attacker and victim: 50-175 m -> base x (100 - (d-50)/5) %; >=175 m -> 75 %. store_trigger_param 4 (hit bone) == 9 (head) -> x2. If the victim (trigger param 1) belongs to p_main_party and is not the player, options_get_damage_to_friends 0/1 -> /2 or x3/4; if the victim is the player, options_get_damage_to_player 0/1 -> /4 or /2. Siege ($g_battle_type 2) defender hit by non-player at >=10 m -> /3. set_trigger_result.

- **Hooks:** `mst:lead_charge/t101:conseq`
- **Mission templates:** `all 25 BE templates`
- **Globals:** `g_battle_type`
- **Module-specific resources:** item: itm_rifle_* families (italian/british/french/winchester/swiss/dutch/papal ranges), itm_lmg_lewis..itm_lmg_hotchkiss1909_m, itm_damage_pure
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis be mst:lead_charge/t101:conseq lines 91-145: falloff, bone 9 x2, difficulty options, siege /3`, `all operations vanilla (no WSE)`
- **Overlaps:** `acw.multi_projectile_firearms`, `be.missile_launch_firing_effects`, `be.shotgun_pellet_spread`, `cbl.flintlock_item_triggers`, `laigle.musket_item_effects`, `nw.missile_launch_effects`, `oa1860.firearm_muzzle_effects`

<a id="bemissile-launch-firing-effects"></a>
### Central per-weapon firing effects via engine hook game_missile_launch — be (`be.missile_launch_firing_effects`)

**What it does:** One engine callback decides, for every shot fired by anyone, which gunshot sound to play (near, or a distance-attenuated far sound beyond 55 m from the camera), how much muzzle smoke and flash to burst, whether to play a bolt-action/lever/pump cycling animation, and halves smoke once the faction has smokeless powder.

**How it works:** script game_missile_launch(agent, item) is called by the engine on missile launch (no script callers; same script name exists in nw, vc, acw, awoiaf). Skips when $ignore_script_game_missile_launch == 1 (set by shotgun_shot to avoid recursion). Big if-chain per weapon family sets locals: sound id, far sounds, smoke count, flash count, offsets, pan flash/pan smoke for flintlocks; sets agent_set_animation bolt_action_shot / bolt_shot_straightpull / lever_action_shot / spencer_shot / shotgun_shot; AI in skirmish mode (team 263+div == 1) gets bolt_action_shot_fast. mission_cam distance >= 5500 -> play_distant_sound_at_pos_based_on_distance else agent_play_sound; particle_system_burst_no_sync psys_musket_smoke (or psys_musket_smoke_smokelesspowder x0.3 if technology 408) and psys_musket_flash. Related: mst:lead_charge/t34 (every frame) enforces a per-weapon rate of fire from item slot 2006 using agent slots 52/53/59 (strongly-inferred).

- **Hooks:** `script:game_missile_launch (engine)`, `mst:lead_charge/t34:conseq`
- **Scripts:** `game_missile_launch`, `play_distant_sound_at_pos_based_on_distance`, `cf_if_agent_faction_invented_technology`
- **Mission templates:** `engine-wide`
- **Slots:** `team:263-270`, `item:2006`, `agent:52`, `agent:53`, `agent:59`
- **Globals:** `ignore_script_game_missile_launch`
- **Module-specific resources:** sound: snd_shot_pistol1, snd_shot_boltaction1, snd_shot_boltaction_straightpull1, snd_winch_shot, snd_shot_lmg1/2, snd_rifle_shot_far3, snd_rifle_shot_reflection_small, (~140 firearm sounds); psys: psys_musket_smoke, psys_musket_smoke_smokelesspowder, psys_musket_flash, psys_pan_flash, psys_pan_smoke; anim: bolt_action_shot, bolt_shot_straightpull, lever_action_shot, spencer_shot, shotgun_shot, bolt_action_shot_fast
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `dis be game_missile_launch (546 stmts): per-family sound/smoke/flash/animation table`, `callers be game_missile_launch: 0 call sites -> engine-called; name shared with vc/nw/acw/awoiaf (all vanilla-engine modules)`, `shotgun_shot sets $ignore_script_game_missile_launch around add_missile -> confirms it fires on add_missile too`
- **Overlaps:** `acw.multi_projectile_firearms`, `be.firearm_hit_damage_model`, `be.shotgun_pellet_spread`, `cbl.flintlock_item_triggers`, `laigle.musket_item_effects`, `nw.missile_launch_effects`, `oa1860.firearm_muzzle_effects`

<a id="beshotgun-pellet-spread"></a>
### Shotgun / scatter-gun pellet spread — be (`be.shotgun_pellet_spread`)

**What it does:** Shotguns fire several pellets in a random cone instead of one bullet.

**How it works:** itm:itm_shotgun_*/t0 (ti_on_weapon_attack, 7 items) call shotgun_shot(count, spread, pos, speed?, agent): sets $ignore_script_game_missile_launch = 1, loops count times copying the muzzle position, rotating it by random +-spread on x and z (fixed point 100) and add_missile with itm_ammo_rifle at speed 5500, then clears the flag.

- **Hooks:** `itm:itm_shotgun_caplock/t0`, `itm:itm_shotgun_doublebarrel/t0`, `itm:itm_shotgun_greener/t0`, `itm:itm_shotgun_winchester_m1897/t0`
- **Scripts:** `shotgun_shot`
- **Globals:** `ignore_script_game_missile_launch`
- **Module-specific resources:** item: itm_ammo_rifle, 7 itm_shotgun_*
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis be shotgun_shot (18 stmts)`, `callers be shotgun_shot: 7 shotgun ti_on_weapon_attack triggers`
- **Overlaps:** `acw.multi_projectile_firearms`, `be.firearm_hit_damage_model`, `be.missile_launch_firing_effects`, `cbl.flintlock_item_triggers`, `laigle.musket_item_effects`, `nw.missile_launch_effects`, `oa1860.firearm_muzzle_effects`

<a id="beww1-weapons-mg-gas-grenades"></a>
### Machine-gun teams, gas attacks, gas masks and grenades — be (`be.ww1_weapons_mg_gas_grenades`)

**What it does:** Late-game (WW1-era) battle content: MG operator troops deploy a tripod machine gun prop that fires bursts at targets in line of sight and suppresses them; companies can launch gas (gas shells/clouds) and wear gas masks (accuracy penalty); grenade attacks thrown by companies; campaign trigger tops up parties' machine guns once the tech is researched.

**How it works:** mg_spawn / mg_deploy / mg_undeploy / mg_decide_fire / mg_fire (agent + spawned spr_mg* props; mg_decide_fire calls add_penaltytodiscipline_fromfire_to_target_of_agent). mst:lead_charge/t44 (1 s) deploy/undeploy by line of sight, t45 every frame fire. company_launch_gas_attack, company_decide_wear_gasmasks, agent_faction_get_gasmask, spr_gas_shell slots 187/188 (cloud lifetime/owner). company_launch_grenade_attack, grenade_hit (item trigger), spr_grenade_timer. strig:128 (async) faction_get_machineguns: if technology 413 invented, add the faction's MG troop (faction slot 780) to lord parties/centres with cf_if_party_has_low_mg_amount.

- **Hooks:** `mst:lead_charge/t44:conseq`, `mst:lead_charge/t45:conseq`, `mst:lead_charge/t32:conseq`, `strig:128`, `itm:itm_grenade_*/t0`
- **Scripts:** `mg_spawn`, `mg_deploy`, `mg_undeploy`, `mg_decide_fire`, `mg_fire`, `get_mg_limit_for_party`, `faction_get_machineguns`, `cf_if_party_has_low_mg_amount`, `company_launch_gas_attack`, `company_decide_wear_gasmasks`, `agent_faction_get_gasmask`, `company_launch_grenade_attack`, `grenade_hit`, `agent_faction_get_lmg`, `agent_faction_get_smg`, `agent_faction_get_mg`
- **Slots:** `faction:413`, `faction:780`, `scene_prop:187`, `scene_prop:188`
- **Module-specific resources:** item: itm_mg1, itm_mg2_russian, itm_gasmask_*, itm_grenade_m15, itm_grenade_rg_12, itm_grenade_mills; spr: spr_mg3_german_barrel, spr_mg5_austrian_barrel, spr_mg7_american, spr_gas_shell, spr_grenade_timer; anim: mg_shooting1, mg_shooting2, grenade_throw
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `callers be add_penaltytodiscipline_fromfire_to_target_of_agent: mg_decide_fire`, `dis be strig:128, faction_get_machineguns`, `hooks be mst:lead_charge t32/t44/t45`
- **Overlaps:** `acw.explosive_grenades`, `awoiaf.fire_arrows_destructible_props`, `nw.explosives_destructible_props`, `oa1860.explosive_and_destructible_props`, `oa1860.explosive_thrown_weapons`, `sw.scripted_grenade_ballistics`

<a id="bifaction-agent-modifiers"></a>
### Per-faction troop combat modifiers (unfinished) — bi (`bi.faction_agent_modifiers`)

**What it does:** A spawn hook that would give every soldier of a kingdom faction-wide bonuses to damage, ranged damage, accuracy/reload, hit points and speed. As shipped it does nothing because the faction values are never set.

**How it works:** init_agent_modifiers is called from ti_on_agent_spawn in 20 mission templates; for agents whose troop faction equals their party's faction it applies agent_set_damage_modifier (faction slot 23), ranged damage (24), accuracy + reload (27), max HP add (25), and for horses speed/horse_speed_factor (26), storing agent slot 5090. No block ever writes faction slots 23-27, so every modifier is 100% (+0).

- **Hooks:** `mst:lead_charge/t1:conseq`, `mst:castle_attack_walls_ladder/t5:conseq`
- **Scripts:** `init_agent_modifiers`
- **Slots:** `faction:23`, `faction:24`, `faction:25`, `faction:26`, `faction:27`, `agent:5090`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `dis bi init_agent_modifiers`, `slot bi faction 23..27: one 'get' each, only in init_agent_modifiers; no faction_set_slot writers`, `roots bi init_agent_modifiers: 20 ti_on_agent_spawn triggers`

<a id="bigarrison-building-battle-bonuses"></a>
### Garrison combat bonuses from fief buildings — bi (`bi.garrison_building_battle_bonuses`)

**What it does:** Soldiers fighting for a settlement (its garrison) get damage and speed bonuses from that settlement's buildings, and an arsenal refills their ammunition during the battle.

**How it works:** ti_on_agent_spawn trigger in every field/siege mission template (e.g. mst:lead_charge/t5): if agent_get_party_id is a center (35..456), damage modifier +10% castra(151) +5% training ground(144) +5% templum(150); speed modifier +5% thermae(149) +5% amphitheatrum(154). A 20s trigger (mst:lead_charge/t6 and siege equivalents) calls agent_refill_ammo on garrison agents with no ammo if arsenal(142) is built.

- **Hooks:** `mst:lead_charge/t5:conseq`, `mst:lead_charge/t6:conseq`, `mst:castle_attack_walls_ladder/t3:conseq`, `mst:castle_attack_walls_ladder/t4:conseq`, `mst:besiege_inner_battle_castle/t3:conseq`, `mst:besiege_inner_battle_town_center/t3:conseq`
- **Mission templates:** `mst_lead_charge`, `mst_village_attack_bandits`, `mst_village_raid`, `mst_besiege_inner_battle_castle`, `mst_besiege_inner_battle_town_center`, `mst_castle_attack_walls_defenders_sally`, `mst_castle_attack_walls_belfry`, `mst_castle_attack_walls_ladder`
- **Slots:** `party:142`, `party:144`, `party:149`, `party:150`, `party:151`, `party:154`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis bi mst:lead_charge/t5:conseq (agent_set_damage_modifier / agent_set_speed_modifier by party slots)`, `dis bi mst:lead_charge/t6:conseq (agent_refill_ammo if party slot 142)`, `sqlite slots bi party 149/150/151/154 readers list the 8 mission templates`
- **Overlaps:** `acan.culture_specific_fief_buildings`, `acan.latifundium_estates`, `ad457.center_buildings_management`, `ad457.lord_business_build_hire_upgrade`, `bi.ai_lords_build`, `bi.roman_public_buildings`, `pop.fief_base_income_and_reports`, `pop.fief_heartbeat_problems`, `pop.fief_improvements_expanded`, `pop.fief_stewards_with_skills`, `sw.recruit_unlock_buildings`, `vc.extended_center_improvements`

<a id="cblflintlock-item-triggers"></a>
### Flintlock pistols and muskets with firing triggers — cbl (`cbl.flintlock_item_triggers`)

**What it does:** Eleven 'dd_' black-powder weapons (pistols, escopettes, musketoon, blunderbusses, arquebuses) carry item triggers for their firing effects.

**How it works:** item_kinds1 itm_dd_firecracker_pistol .. itm_dd_spadassin_arquebus each have one item trigger block (itm:<item>/t0) - the usual smoke/sound on-attack pattern of firearm packs.

- **Hooks:** `itm:itm_dd_blunderbuss/t0`, `itm:itm_dd_arquebus/t0`
- **Module-specific resources:** item: itm_dd_firecracker_pistol, itm_dd_blackpowder_pistol, itm_dd_elite_pistol, itm_dd_assassin_pistol, itm_dd_escopette, itm_dd_musketoon, itm_dd_blunderbuss, itm_dd_doubleshot_blunderbuss, itm_dd_heavy_escopette, itm_dd_arquebus, itm_dd_spadassin_arquebus
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Overlaps:** `acw.multi_projectile_firearms`, `be.firearm_hit_damage_model`, `be.missile_launch_firing_effects`, `be.shotgun_pellet_spread`, `laigle.musket_item_effects`, `nw.missile_launch_effects`, `oa1860.firearm_muzzle_effects`

<a id="laiglefield-artillery"></a>
### Crewed field artillery in campaign battles — laigle (`laigle.field_artillery`)

**What it does:** In ordinary campaign field battles, each side that owns guns gets up to two cannon placed in front of its spawn, each worked by a three-man crew that turns the gun, picks a random enemy, fires a ball that lands after a flight delay and kills or wounds everyone within about two metres. Guns are lost when crews die (intended; see bug notes).

**How it works:** mst:lead_charge/t76 (before start) zeroes the registry troop trp_cannon_array. t77 (after start) walks parties fighting the player, calls get_cannon_count (party slots 502/503/504 = 3/6/12-pounders), and spawn_cannon for up to 2 guns per side; spawn_cannon resolves an entry point (1 for the AI, 3 for the player), offsets 10 m sideways per gun and 20 m forward, spawn_scene_prop, then spawn_agent x3 (officer + 2 operators from get_cannon_operator_for_faction), stores crew in prop slots 300-302, division 8, scripted destinations around the gun. Caliber only sets prop slot 309 = damage multiplier 1/2/3 (all calibers use spr_twleve_pound_cannon). Every 3 s: t78 marks gun active if crew alive (prop slot 305) and releases crew (agent slot 16, clear scripted mode) when it is dead; t79 picks target agent (first enemy human, then 5% chance to switch to each later one) into slot 304; t80 rolls the gun back after recoil; t81 calls brute_rotation_check to turn the prop toward the target, sets slot 306 = aimed when rotation is 0 and the two operators are within 1.5 m of their posts. Every 1 s t82 is the reload: an operator walks to a point 3 m in front of the muzzle, and while within 1 m the counter slot 308 ticks down; on 0 slot 307 (loaded) is cleared. t83 (3 s) fires when active+loaded+aimed and team hold-fire order is off: spawns spr_cannon_ball 10 m underground at the muzzle, stores an aim point = target position +/-10 m random (ball slots 301/302), flight time = distance/100 one-second ticks (slot 306), muzzle particles (psys_cannon_smoke/longsmoke/flash/touchsmoke), snd_cannon_shot (+snd_cannon_distant if the player is 60 m+ away), animates 40 cm recoil, sets reload counter 30-39 s. t84 (1 s) counts each live ball down; at 0 it moves the ball to ground at the aim point, plays psys_shell_flash/longsmoke/dirtsplosion + snd_shell_explosion, and deals 50-100 damage (x slot 309 within 1 m) via agent_deliver_damage_to_agent from the gun officer to every agent within 2 m. count_mission_casualties_from_agents decrements party slot 502-504 when an officer dies.

- **Hooks:** `mst:lead_charge/t76:conseq`, `mst:lead_charge/t77:conseq`, `mst:lead_charge/t78:conseq`, `mst:lead_charge/t79:conseq`, `mst:lead_charge/t80:conseq`, `mst:lead_charge/t81:conseq`, `mst:lead_charge/t82:conseq`, `mst:lead_charge/t83:conseq`, `mst:lead_charge/t84:conseq`
- **Scripts:** `spawn_cannon`, `get_cannon_count`, `get_cannon_operator_for_faction`, `brute_rotation_check`, `count_mission_casualties_from_agents`, `form_infantry`
- **Mission templates:** `mst_lead_charge`
- **Slots:** `scene_prop:300`, `scene_prop:301`, `scene_prop:302`, `scene_prop:303`, `scene_prop:304`, `scene_prop:305`, `scene_prop:306`, `scene_prop:307`, `scene_prop:308`, `scene_prop:309`, `scene_prop:310`, `party:502`, `party:503`, `party:504`, `agent:301`, `agent:302`, `agent:16`, `troop:0 (on trp_cannon_array, running index)`
- **Globals:** `total_cannon_count`, `g_siege_method`, `g_encountered_party_2`
- **Module-specific resources:** scene_prop: spr_twleve_pound_cannon, spr_six_pound_cannon, spr_three_pound_cannon, spr_cannon_ball; psys: psys_cannon_smoke, psys_cannon_longsmoke, psys_cannon_flash, psys_cannon_touchsmoke, psys_shell_flash, psys_shell_longsmoke, psys_shell_dirtsplosion; sound: snd_cannon_shot, snd_cannon_distant, snd_shell_explosion; troop: trp_cannon_array, trp_french_cannon_operator, trp_french_cannon_officer, trp_british_cannon_operator, trp_bavarian_cannon_operator
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis laigle mst:lead_charge/t76..t84 (decoded above)`, `dis laigle spawn_cannon (spawn_agent x3, prop slots 300-302, 307=1, 308=30)`, `slot laigle scene_prop 309: written only in t77 (1/2/3), read only in t84`, `callers laigle get_cannon_count -> t77 x3, regiment_recruitment menu, cf_spawn_side_cannons`, `dis laigle count_mission_casualties_from_agents stmt 14-33 (gun loss)`, `form_infantry stmt 30: neg|is_between troop, trp_french_cannon_operator, trp_cannon_array (crew excluded from formations)`
- **Overlaps:** `acw.field_artillery`, `be.field_artillery_batteries`, `laigle.artillery_park`, `nw.crewed_artillery`, `oa1860.scripted_ballistic_hand_cannon`

<a id="laiglemusket-item-effects"></a>
### Firearm muzzle, pan-flash, distance-sound, scatter-shot and bullet-impact effects — laigle (`laigle.musket_item_effects`)

**What it does:** Each musket and pistol has its own firing effect placed at its muzzle and lock: smoke, flash, pan smoke, and a near or distant gunshot sound depending on how far the shooter is from the player. Blunderbusses fire six spread pellets. Bullets kick up dirt or dust where they land.

**How it works:** Item ti_on_weapon_attack triggers (11-28 stmts) on ~27 firearms: position offsets per model, particle_system_burst psys_musket_smoke/longsmoke/flash/pansmoke + psys_pistol_panflash, then play snd_pistol_shot if the player is < 60 m away else snd_musket_distant. itm_llew2_blunderbus: 6x add_missile with random +/-2 degree spread and itm_cartridges ammo. itm_cartridges/itm_cartridgesx ti_on_missile_hit -> bullet_land: psys_bullet_dirtsplosion or psys_bullet_dust/dirt by hit type.

- **Hooks:** `itm:itm_musket_brownbess/t0`, `itm:itm_llew2_blunderbus/t0`, `itm:itm_cartridges/t0`, `itm:itm_pistol_duelling/t0`
- **Scripts:** `bullet_land`
- **Module-specific resources:** psys: psys_musket_smoke, psys_musket_longsmoke, psys_musket_flash, psys_musket_pansmoke, psys_pistol_panflash, psys_bullet_dirtsplosion, psys_bullet_dust, psys_bullet_dirt; sound: snd_musket_distant, snd_musket_distant_long, snd_pistol_shot
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis laigle itm:itm_musket_brownbess/t0`, `dis laigle itm:itm_llew2_blunderbus/t0 (add_missile x6)`, `callers laigle bullet_land -> itm_cartridges/t0, itm_cartridgesx/t0 [ti_on_missile_hit]`
- **Overlaps:** `acw.multi_projectile_firearms`, `be.firearm_hit_damage_model`, `be.missile_launch_firing_effects`, `be.shotgun_pellet_spread`, `cbl.flintlock_item_triggers`, `nw.missile_launch_effects`, `oa1860.firearm_muzzle_effects`

<a id="nwcrewed-artillery"></a>
### Player-crewed artillery (12pdr, howitzer, mortar, fort, naval, carronade, swivel, rocket) — nw (`nw.crewed_artillery`)

**What it does:** Cannons are multi-part scene props the player walks up to and works step by step with use-buttons (sponge/load cartridge, load round/shell/canister/bomb, ram, aim, fire, limber to a horse); once 'controlling' a gun the player aims with the camera and fires with a key, and the ball flies, bounces, damages people and destructible props.

**How it works:** Cannon kinds are scene props 1482-1489 (spr_mm_cannon_12pdr_wood ... spr_mm_cannon_rocket_wood) with child props (wheels, barrel, limber, buttons). Button props (spr_mm_aim_button, spr_mm_load_cartridge_button, spr_mm_round_button, spr_mm_limber_button, ...) call use_item on ti_on_scene_prop_use; use_item is gated (this_or_next|multiplayer_is_server)(neg|game_in_multiplayer_mode) so it also runs in single player. A mission trigger (mst:tutorial/t9) reads game keys 6/7 while $g_currently_controlling_object==1 and, when not in multiplayer, calls handle_agent_control_command directly (SP branch) which sets agent slot 6 (5 = fire). mst:tutorial/t1 (every 0.5 s, same SP-inclusive guard) aims the barrel from agent_get_look_position and, on command 5, calls fire_cannon; recoil_cannon animates the recoil. mst:tutorial/t2 (every 0.125 s) moves balls: cannon_ball_hit_ground (bounce), cannon_explosion_on_position / explosion_at_position, deliver_damage_to_prop. State lives in ~60 scene-prop slots (6-50+) and agent slots 6/7.

- **Hooks:** `mst:tutorial/t1:cond`, `mst:tutorial/t1:conseq`, `mst:tutorial/t2:conseq`, `mst:tutorial/t9:cond`, `mst:tutorial/t9:conseq`, `spr:spr_mm_aim_button/t0`, `spr:spr_mm_load_cartridge_button/t0`, `mst:multiplayer_dm/t20:conseq`, `mst:multiplayer_tdm/t25:conseq`
- **Scripts:** `fire_cannon`, `cannon_ball_hit_ground`, `cannon_explosion_on_position`, `recoil_cannon`, `handle_agent_control_command`, `use_item`, `stop_agent_controlling_cannon`, `set_agent_controlling_prop`, `cannon_instance_get_barrel`, `cannon_instance_get_wheels`, `cannon_child_find_cannon_instance`, `agent_take_cannonball`, `limber_cannon_to_horse`, `unlimber_cannon_from_horse`, `attach_limber_to_horse`, `generate_bits_for_cannon_instance`, `search_for_first_ground_from_direction_to_angle`, `prop_instance_animate_to_position_with_childs`, `set_prop_child_active`, `set_prop_child_inactive`, `find_or_create_scene_prop_instance`
- **Presentations:** `prsnt_multiplayer_cannon_crosshair`, `prsnt_multiplayer_artillery_icons`
- **Mission templates:** `mst_tutorial`, `mst_multiplayer_dm`, `mst_multiplayer_tdm`, `mst_multiplayer_hq`, `mst_multiplayer_cf`, `mst_multiplayer_sg`, `mst_multiplayer_bt`, `mst_multiplayer_cb`, `mst_multiplayer_duel`, `mst_multiplayer_kh`, `mst_multiplayer_br`
- **Slots:** `scene_prop:6-50 (cannon/child state)`, `agent:6 (control command)`, `agent:7 (controlled prop)`
- **Globals:** `g_currently_controlling_object`, `g_cur_control_prop_kind`
- **Module-specific resources:** spr: spr_mm_cannon_12pdr_wood..spr_mm_cannon_rocket_wood (1482-1489), spr_mm_cannon_*_wheels, spr_mm_cannon_*_limber, spr_mm_*_button (aim/load/round/shell/canister/bomb/rocket/limber/push); psys: psys 70 (muzzle burst); sound: snd 173 (fire)
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis nw mst:tutorial/t1:cond = (this_or_next|multiplayer_is_server)(neg|game_in_multiplayer_mode)`, `dis nw mst:tutorial/t9:conseq: SP else-branch calls client_get_my_agent + handle_agent_control_command`, `dis nw use_item stmt 10-11: same SP-inclusive guard`, `roots nw fire_cannon: 10 mst_multiplayer_* + mst:tutorial/t1`, `menu:tutorial/opt:continue -> set_jump_mission 2 (= mst_tutorial)`, `tutorial string 'Finally! It is time for some artillery training. Walk up to the cannon'`
- **Overlaps:** `acw.field_artillery`, `be.field_artillery_batteries`, `laigle.artillery_park`, `laigle.field_artillery`, `oa1860.scripted_ballistic_hand_cannon`

<a id="nwexplosives-destructible-props"></a>
### Grenades, explosive shot and destructible props — nw (`nw.explosives_destructible_props`)

**What it does:** Thrown grenades and explosive bullets blow up on impact, hurting nearby people and chipping damage off destructible scenery (doors, walls, gabions, crates), which steps through damage stages until it collapses; explosive supply crates chain-explode.

**How it works:** Item triggers: itm_grenade/t1 and itm_explosive_bullets/t0 (ti_on_missile_hit) call explosion_at_position (142 stmts: area damage to agents, sound/particles, then deliver_damage_to_prop on props in radius). deliver_damage_to_prop (314) looks up prop health (get_default_health_for_prop_kind), applies damage to scene-prop slot health, advances to the next destruction stage (get_next_stage_acording_to_damage, get_next_destruction_stage_prop_kind 542 stmts of prop-kind tables) and spawns debris (spawn_crator_on_pos, clean_up_prop_instance). spr_mm_sp_crate_explosive and mst:sp_campaign_vienna/t39 reach the same chain in SP.

- **Hooks:** `itm:itm_grenade/t1`, `itm:itm_explosive_bullets/t0`, `mst:sp_campaign_vienna/t39:conseq`, `spr:spr_mm_sp_crate_explosive/t0`, `mst:tutorial/t4:conseq`
- **Scripts:** `explosion_at_position`, `deliver_damage_to_prop`, `get_default_health_for_prop_kind`, `get_next_stage_acording_to_damage`, `get_next_destruction_stage_prop_kind`, `get_prop_center`, `get_prop_kind_for_constr_kind`, `spawn_crator_on_pos`, `clean_up_prop_instance`, `multiplayer_server_play_hit_effect`, `handle_cannon_hit_effect_event`
- **Mission templates:** `mst_sp_campaign_vienna`, `mst_tutorial`, `mst_multiplayer_dm`, `mst_multiplayer_tdm`, `mst_multiplayer_hq`, `mst_multiplayer_cf`, `mst_multiplayer_sg`, `mst_multiplayer_bt`, `mst_multiplayer_cb`, `mst_multiplayer_duel`, `mst_multiplayer_kh`, `mst_multiplayer_br`
- **Slots:** `scene_prop:6-50 (health/stage)`
- **Module-specific resources:** item: itm_grenade, itm_explosive_bullets, itm_french_bomb; spr: spr_mm_sp_crate_explosive, destructible stage props (~100 kinds)
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `explain nw explosion_at_position: callers itm:itm_explosive_bullets/t0, itm:itm_grenade/t1 [ti_on_missile_hit], mst:sp_campaign_vienna/t39`, `roots nw deliver_damage_to_prop includes spr:spr_mm_sp_crate_explosive and mst:sp_campaign_vienna`, `sqlite blocks nw itm:* lists grenade t0/t1, explosive_bullets t0`
- **Overlaps:** `acw.explosive_grenades`, `awoiaf.fire_arrows_destructible_props`, `be.ww1_weapons_mg_gas_grenades`, `oa1860.explosive_and_destructible_props`, `oa1860.explosive_thrown_weapons`, `sw.scripted_grenade_ballistics`

<a id="nwmissile-launch-effects"></a>
### Central muzzle flash, smoke and report on every gunshot (engine hook) — nw (`nw.missile_launch_effects`)

**What it does:** Every time any firearm is discharged the game plays the right report sound and puffs muzzle smoke and flash at the barrel, scaled per weapon class (pistol, musket, rifle, blunderbuss), with lighter smoke for the player's own shot so his view is not blinded; bullet impacts throw dust/spark particles.

**How it works:** game_missile_launch is an engine callback (params: shooter agent, weapon item, missile item) - NW defines it so the engine calls it on every missile launch. It picks sound 164/165/166 and smoke offsets by weapon id band, scales the burst to 65% when the shooter is the local player (client_get_my_agent), and fires particle_system_burst_no_sync 65-68. Impacts: item triggers on itm_bullets, itm_pistol_ammo, itm_canister_ammo, itm_shell_fragment call mm_on_bullet_hit (psys 90/91 at pos63).

- **Hooks:** `script:game_missile_launch`, `itm:itm_bullets/t0`, `itm:itm_pistol_ammo/t0`, `itm:itm_canister_ammo/t0`, `itm:itm_shell_fragment/t0`, `script:game_missile_dives_into_water`
- **Scripts:** `game_missile_launch`, `mm_on_bullet_hit`, `game_missile_dives_into_water`, `client_get_my_agent`
- **Module-specific resources:** psys: psys 65-68 (muzzle smoke/flash), psys 90-91 (impact); sound: snd 164-166 (musket/pistol reports)
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `dis nw game_missile_launch (62 stmts) - sound + 4 particle bursts`, `sqlite: game_missile_launch exists only in nw and be (be = SP gunpowder mod, 546 stmts)`
- **Overlaps:** `acw.multi_projectile_firearms`, `be.firearm_hit_damage_model`, `be.missile_launch_firing_effects`, `be.shotgun_pellet_spread`, `cbl.flintlock_item_triggers`, `laigle.musket_item_effects`, `oa1860.firearm_muzzle_effects`

<a id="oa1860explosive-thrown-weapons"></a>
### Exploding grenades, dynamite and shells — oa1860 (`oa1860.explosive_thrown_weapons`)

**What it does:** Thrown grenades and dynamite (and several ammo items) explode where they land, hurting everyone within 2.5 m for 60-100 damage with fire and smoke.

**How it works:** ti_on_missile_hit trigger (19 stmts, identical block on itm_grenade, itm_dynamite_big, itm_us_grenade (18), itm_blackpowder_barrel, itm_cannonball, itm_cannonball_12lb, itm_arrows, itm_bodkin_arrows): runs on server or single-player; for every agent within 250 cm of the impact, store_agent_hit_points (absolute), subtract 60-99, agent_set_hit_points, and if that reaches 0 agent_deliver_damage_to_agent from the thrower to credit the kill; psys_pistol_smoke + psys_village_fire_big bursts and snd_gun_shoot at the impact.

- **Hooks:** `itm:itm_grenade/t0`, `itm:itm_dynamite_big/t0`, `itm:itm_us_grenade/t0`, `itm:itm_cannonball/t0`
- **Module-specific resources:** item: itm_grenade, itm_dynamite_big, itm_us_grenade; psys: psys_pistol_smoke, psys_village_fire_big; sound: snd_gun_shoot
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis oa1860 itm:itm_grenade/t0`, `diff of itm_arrows/t0 and itm_cannonball/t0 against itm_grenade/t0 -> identical`, `item_kinds1.txt names: 'Ketchum_Grenade_(handle_with_care)', 'Dynamite_(handle_with_care)'`
- **Overlaps:** `acw.explosive_grenades`, `awoiaf.fire_arrows_destructible_props`, `be.ww1_weapons_mg_gas_grenades`, `nw.explosives_destructible_props`, `oa1860.explosive_and_destructible_props`, `sw.scripted_grenade_ballistics`

<a id="oa1860firearm-muzzle-effects"></a>
### Per-gun muzzle smoke and fire effects — oa1860 (`oa1860.firearm_muzzle_effects`)

**What it does:** Each firearm emits smoke and a muzzle flash from its own barrel position when fired.

**How it works:** ti_on_weapon_attack item triggers of 4-7 statements on dozens of guns (113 item-trigger blocks in total) (e.g. itm_henry: sound, offset to the lock, psys_cooking_smoke, offset to the muzzle, psys_pistol_smoke + psys_cooking_fire_1).

- **Hooks:** `itm:itm_henry/t0`, `itm:itm_enfield/t0`, `itm:itm_spencer_rifle/t0`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis oa1860 itm:itm_henry/t0`
- **Overlaps:** `acw.multi_projectile_firearms`, `be.firearm_hit_damage_model`, `be.missile_launch_firing_effects`, `be.shotgun_pellet_spread`, `cbl.flintlock_item_triggers`, `laigle.musket_item_effects`, `nw.missile_launch_effects`

<a id="oa1860scripted-ballistic-hand-cannon"></a>
### Hand cannon with scripted cannonball arc — oa1860 (`oa1860.scripted_ballistic_hand_cannon`)

**What it does:** A carried 'hand cannon' (a cheat item) fires a scripted cannonball: the script traces a falling arc straight ahead of the shooter, killing anyone the ball passes within 1.5 m of and knocking down or stunning anyone within 3 m, until the arc reaches the ground where it throws up smoke and dirt.

**How it works:** itm_cannon_visible ti_on_weapon_attack (93 stmts; the same block is also attached to itm_cannonball_box_3lb): sound + muzzle fire/smoke; finds the nearest human (the shooter); then loops reg5 = 1..499, each step moving a probe 1.6 m further forward and dropping it by reg5^2/2 cm (a parabola). For every live agent: < 1.5 m from the probe -> agent_set_hit_points 0 + agent_deliver_damage_to_agent (kill) + blood burst; < 3 m -> humans lose HP scaled by item slot 79 of their shield and item slot 77 of their body armour, play rider_fall_roll + snd_man_stun, horses scaled by slot 77 and horse_rear; anyone left under 15 HP is killed. When the probe is at or below ground level the loop stops, bursts psys_war_smoke_tall/psys_map_village_fire_smoke and moves instance 0 of spr_city_swad_02 there (an impact marker animated upward).

- **Hooks:** `itm:itm_cannon_visible/t0`, `itm:itm_cannonball_box_3lb/t0`
- **Slots:** `item:77`, `item:79`
- **Module-specific resources:** item: itm_cannon_visible, itm_cannon_visible_melee, itm_cannonball_box_3lb; psys: psys_cooking_fire_1, psys_cooking_smoke, psys_war_smoke_tall, psys_map_village_fire_smoke, psys_game_blood; scene_prop: spr_city_swad_02; sound: snd_enemy_flag_taken, snd_man_stun, snd_horse_snort
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis oa1860 itm:itm_cannon_visible/t0`, `slot oa1860 item 77 / item 79: read-only, never written`, `item_kinds1.txt: itm_cannon_visible = 'Hand_Cannon_CHEAT_(Breech_Loading)'`, `refs oa1860 item itm_cannon_visible -> 0 bytecode references (inventory-only item)`
- **Overlaps:** `acw.field_artillery`, `be.field_artillery_batteries`, `laigle.artillery_park`, `laigle.field_artillery`, `nw.crewed_artillery`

<a id="perisnofire-ammo-explosions"></a>
### Fire arrows and fire bolts explode on impact — perisno (`perisno.fire_ammo_explosions`)

**What it does:** Fire arrows and fire bolts burst into smoke, sparks and dirt when they hit and hurt every enemy in a radius, scaled by distance, with a minimum damage.

**How it works:** The three items' missile-hit triggers call cf_create_explosion(agent, min_damage, damage, radius). It spawns particle bursts and sounds at the impact position, then loops all agents, finds enemies within the radius, computes damage falling with distance, calls agent_deliver_damage_to_agent, and adds 3x the actual HP lost into agent slot 46 (a kill/score accumulator) while recording the attacker in slot 48.

- **Hooks:** `itm:itm_fire_arrow2/t0`, `itm:itm_fire_arrow3/t0`, `itm:itm_fire_bolt/t0`
- **Scripts:** `cf_create_explosion`, `cf_create_explosion_large`, `cf_create_leafbomb_explosion`
- **Slots:** `agent:46`, `agent:48`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `callers perisno cf_create_explosion: 3 call sites, all ti_on_missile_hit triggers of fire arrows/bolt`, `dis perisno cf_create_explosion: try_for_agents loop, teams_are_enemies, distance falloff, agent_deliver_damage_to_agent, agent_set_slot 46/48`, `explain perisno cf_create_explosion: psys_explosive_explosion_sparks, snd_galwe_explode`

<a id="swfield-heal-consumable"></a>
### Field healing consumable (bacta injector + capsules) and other hotkey abilities — sw (`sw.field_heal_consumable`)

**What it does:** In battle the player can press a key to heal 20 HP if he carries an injector and at least one capsule (each use consumes a capsule); other hotkeys give a jump-pack leap (animation, not usable mounted), crouch, and a death-camera after falling.

**How it works:** mst:lead_charge/t26 (on $bacta_injector_key): if HP < 100%, scan inventory for item 65 (injector) and count item 66 (capsules); heal +20 (agent_set_hit_points absolute), remove one capsule from inventory, play sound 195 and report remaining capsules. t28 ($jetpack_key): requires itm_jetpack or itm_force_jump and no horse -> agent_set_animation 530 (a jump animation from actions.txt). t34 crouch key toggles $crouch_key_down. All keys are user-assignable (see sw.rebindable_ability_keys).

- **Hooks:** `mst:lead_charge/t26:cond`, `mst:lead_charge/t26:conseq`, `mst:lead_charge/t28:conseq`, `mst:lead_charge/t34:conseq`
- **Mission templates:** `mst_lead_charge`, `mst_lead_charge_no_horse`
- **Globals:** `bacta_injector_key`, `jetpack_key`, `crouch_key`, `crouch_key_down`, `g_player_troop`
- **Module-specific resources:** item: itm 65 (bacta injector), itm 66 (bacta capsule), itm_jetpack, itm_force_jump; anim: anim 530 (jump); sound: snd 195
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis sw mst:lead_charge/t26:conseq (items 65/66, +20 hp, capsule removal)`, `explain sw mst:lead_charge/t28:conseq texts 'Can't use while mounted!', 'You don't have a Jetpack or Force Jump'`, `sqlite names sw item 68 = itm_jetpack, 757 = itm_force_jump`

<a id="swscripted-grenade-ballistics"></a>
### Thrown grenades simulated by script (arc, gravity, bounce, fuse, blast) — sw (`sw.scripted_grenade_ballistics`)

**What it does:** Thermal detonators are not ordinary missiles: when thrown, a script spawns a simulated projectile that flies on a gravity arc, trails particles, bounces off the ground, and after its fuse explodes, damaging everyone in the blast radius with on-screen damage feedback.

**How it works:** itm_thermal_detonator1-3 ti_on_weapon_attack -> emit_projectile writes a free entry in a 256-row table kept on storage troops 975-991 (active flag, launch time, x/y/z, vx/vy/vz, particle system, owner). mst:lead_charge/t4 (every 0.05 s, condition block, 181 stmts) integrates every active row from $timer: position = p0 + v*t - g*t^2 (g = 981 units), bursts the row's particle system, tests ground contact against $ground_level / position_set_z_to_ground_level to bounce, checks agents in radius and calls agent_deliver_damage_to_agent ('Delivered {reg1} damage.' / 'Received %d damage.').

- **Hooks:** `itm:itm_thermal_detonator1/t0`, `itm:itm_thermal_detonator2/t0`, `itm:itm_thermal_detonator3/t0`, `mst:lead_charge/t4:cond`, `mst:lead_charge_no_horse/t7:cond`
- **Scripts:** `emit_projectile`, `agent_deliver_damage_to_agent`, `position_face_position`
- **Mission templates:** `mst_lead_charge`, `mst_lead_charge_no_horse`
- **Slots:** `troop:0-255 on storage troops 975-982, 991 (projectile table)`
- **Globals:** `timer`, `timer_speed`, `ground_level`
- **Module-specific resources:** item: itm_thermal_detonator1, itm_thermal_detonator2, itm_thermal_detonator3; psys: detonator trail/blast particles
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `explain sw emit_projectile: callers itm_thermal_detonator1-3 [ti_on_weapon_attack]`, `dis sw mst:lead_charge/t4:cond stmts 0-38 (troop 975-982 slot table, gravity 981, particle burst)`, `roots sw agent_deliver_damage_to_agent: lead_charge/t4, lead_charge_no_horse/t7`
- **Overlaps:** `acw.explosive_grenades`, `awoiaf.fire_arrows_destructible_props`, `be.ww1_weapons_mg_gas_grenades`, `nw.explosives_destructible_props`, `oa1860.explosive_and_destructible_props`, `oa1860.explosive_thrown_weapons`

<a id="swsupport-unit-auras"></a>
### Support units that resupply ammo and heal nearby allies in battle — sw (`sw.support_unit_auras`)

**What it does:** Soldiers fielding a power droid refill the ammunition of every friendly within 4 m every 30 seconds; a medical droid heals nearby friends; the player gets a message when he is the one helped.

**How it works:** mst:lead_charge/t32 (every 30 s): for each living human agent wearing a power-droid 'armour' item (items 417-419) loop all same-team agents within 400 cm and agent_refill_ammo; for an agent wearing itm_fxseries_droid_armor (420) restore hit points to nearby friends; display 'A Power Droid refilled your ammo!' / 'A Medical Droid refilled some of your health!' when the player is a recipient. ti_on_agent_spawn (t33) gives droid-equipped agents a special walk animation (528).

- **Hooks:** `mst:lead_charge/t32:conseq`, `mst:lead_charge/t33:conseq`
- **Mission templates:** `mst_lead_charge`, `mst_lead_charge_no_horse`
- **Module-specific resources:** item: itm_power_droid_grey, itm_power_droid_snow, itm_power_droid_tan, itm_fxseries_droid_armor; anim: anim 528 (droid walk)
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis sw mst:lead_charge/t32:conseq (agent_refill_ammo within 400, items 417-420)`, `explain sw mst:lead_charge/t32:conseq text 'A Power Droid refilled your ammo!'`, `sqlite names sw item 417-420`

<a id="swweapon-mode-toggle"></a>
### Hotkey weapon mode switch (swap a weapon for its alternate form in place) — sw (`sw.weapon_mode_toggle`)

**What it does:** Pressing a (rebindable) key swaps the wielded weapon for its paired alternate version - e.g. a blaster between modes, a staff between forms - keeping its quality modifier, with a short message.

**How it works:** mst:lead_charge/t29 (on $toggle_weapon_key) reads the wielded item; if item slot 6 holds an alternate item id it finds that item in the player's equipment slots 0-3, replaces it with the alternate (troop_set_inventory_slot + same modifier) and starts a one-line mission conversation (start_mission_conversation) - a trick that forces the engine to re-equip the agent from the troop's inventory immediately.

- **Hooks:** `mst:lead_charge/t29:cond`, `mst:lead_charge/t29:conseq`
- **Mission templates:** `mst_lead_charge`, `mst_lead_charge_no_horse`
- **Slots:** `item:6 (alternate item id)`
- **Globals:** `toggle_weapon_key`, `show_switch_weapon_dialog`, `g_player_troop`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis sw mst:lead_charge/t29:conseq (item slot 6, troop_set_inventory_slot, start_mission_conversation)`, `global sw toggle_weapon_key used by 29 mission-template conditions`

<a id="tldbattle-condition-modifiers"></a>
### Per-agent battle modifiers from terrain, night, race and faction weather auras — tld (`tld.battle_condition_modifiers`)

**What it does:** When each soldier spawns, the game adjusts his movement speed, horse speed, damage, accuracy and reload speed for the battle's terrain (forest/snow/marsh), time of day (orcs fight better at night, men worse), his race, and any supernatural weather in force (mists, storms or darkness raised near the strongholds of Lothlorien, Mordor, Isengard and Dol Guldur) -- heavy armour also slows hero agents more in difficult terrain.

**How it works:** Every field-battle template has a ti_on_agent_spawn trigger (e.g. mst:bandit_lair/t43, 162 stmts) that starts each modifier at 100 and subtracts by: party 0 slot 308 battle effect (1/4/5/6 set by strig:70) against the agent's alignment (faction slot 158), $terrain_condition (from store_terrain_condition_to_s17_s18 before the battle), is_currently_night with troop_get_type race classes and cf_is_a_night_troop, and encumbrance (ce_get_troop_encumbrance for heroes, Athletics for regulars). Results go to agent_set_horse_speed_factor, agent_set_damage_modifier, agent_set_accuracy_modifier, agent_set_speed_modifier, agent_set_reload_speed_modifier, agent_set_ranged_damage_modifier. strig:70 (5 h, option $battle_encounter_effects) checks whether the player is within 12-60 map units of the strongholds of Lothlorien (fac 8, effect 1), Mordor (fac 6, effect 4), Isengard (fac 7, effect 5) or Dol Guldur (fac 17, effect 6) and, with probability proportional to that faction's strength, sets the effect and map haze/cloud; the coherence script also gives +-10 coherence for the effect.

- **Hooks:** `mst:bandit_lair/t43:conseq`, `strig:70`
- **Scripts:** `ce_get_troop_encumbrance`, `cf_is_a_night_troop`, `store_terrain_condition_to_s17_s18`, `coherence`
- **Mission templates:** `mst_lead_charge`, `mst_bandit_lair`, `mst_custom_battle`, `mst_tld_caravan_help`, `mst_village_attack_bandits`
- **Slots:** `party:308`, `agent:32`, `faction:158`
- **Globals:** `terrain_condition`, `battle_encounter_effects`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis tld mst:bandit_lair/t43:conseq (modifier arithmetic and agent_set_* calls)`, `dis tld strig:70 (distance-to-stronghold weather roll, party 0 slot 308 values 1/4/5/6)`, `slot tld party 308: read in ~100 mission blocks`
- **Overlaps:** `acan.seasonal_light_fog_weather`, `be.campaign_weather_battle_atmosphere`, `laigle.weather_seasons`, `nw.battle_weather_generator`, `tld.day_night_proficiency_shift`, `vc.seasons_scene_lighting`

<a id="tldday-night-proficiency-shift"></a>
### Day/night combat proficiency shift by race — tld (`tld.day_night_proficiency_shift`)

**What it does:** At every sunrise and sunset the game rewrites weapon proficiencies for whole troop races: troops not flagged sun-immune (troop slot 169) lose a stored percentage of their proficiencies at daybreak (race-specific, e.g. 40% archery, 30% throwing) and get it back at nightfall -- i.e. orc-type creatures fight worse in daylight. No reverse (night) penalty for day-folk was seen in the code examined.

**How it works:** strig:53 (hourly, 1722 stmts) detects a day/night transition via $prev_day, then loops all 1033 troops; for each troop_get_type (race 0-15) and cf_is_a_night_troop (troop slot 169 not set) it either computes and stores a percentage of each proficiency in troop slots 41-42 (likely more per proficiency) (e.g. 40% archery, 30% throwing) and lowers it with troop_raise_proficiency_linear, or adds the stored amount back. trig:14 (once, $prev_day == 4) initialises the stored values for old saves. game_get_skill_modifier_for_troop also reads $prev_day.

- **Hooks:** `strig:53`, `trig:14:conseq`
- **Scripts:** `cf_is_a_night_troop`
- **Slots:** `troop:41`, `troop:42`, `troop:169`
- **Globals:** `prev_day`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `dis tld strig:53 (is_currently_night edge, loop 0..1033, troop_get_type branches 0-15, troop_raise_proficiency_linear)`, `dis tld trig:14:conseq (initial store into troop slots 41/42)`, `dis tld cf_is_a_night_troop (troop slot 169)`
- **Overlaps:** `acan.seasonal_light_fog_weather`, `be.campaign_weather_battle_atmosphere`, `laigle.weather_seasons`, `nw.battle_weather_generator`, `tld.battle_condition_modifiers`, `vc.seasons_scene_lighting`

<a id="tldencumbrance-and-fall-damage"></a>
### Armour encumbrance penalties and fall damage when a horse dies — tld (`tld.encumbrance_and_fall_damage`)

**What it does:** Hero agents carry an encumbrance value from the weight of their equipment. It reduces their speed in rough terrain and, when their horse is killed under them, they take fall damage scaled by encumbrance and horse speed (reduced by Riding skill) -- possibly being knocked out and credited as a kill to the attacker. Item tooltips show the skill penalty heavy gear imposes.

**How it works:** ce_get_troop_encumbrance(troop) sums item_get_weight of equipment slots in fixed-point and returns encumbrance in reg1 (used by 49 mission blocks). ti_on_agent_killed_or_wounded triggers (e.g. mst:bandit_lair/t109) fire when a non-human (horse) agent dies: rider = agent slot 304; damage = random 1-5 + encumbrance*speed/125, minus Riding*8% of that; applied via agent_set_hit_points / agent_deliver_damage_to_agent_advanced so the killer gets credit. game_get_item_extra_text (781 stmts) prints per-item penalties such as 'Athletics -N', 'Riding -N', 'Power Draw -N' or 'No skill penalty'.

- **Hooks:** `mst:bandit_lair/t109:conseq`, `mst:bandit_lair/t43:conseq`, `script:game_get_item_extra_text`
- **Scripts:** `ce_get_troop_encumbrance`, `game_get_item_extra_text`, `check_agent_armor`
- **Slots:** `agent:304`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `dis tld ce_get_troop_encumbrance (item_get_weight over inventory slots 0-8)`, `dis tld mst:bandit_lair/t109:conseq (fall damage formula, agent_deliver_damage_to_agent_advanced)`, `qstr tld 'Athletics___{reg31}', 'No_Skill_Penalty'`

<a id="vccombat-extras-dehorse-bash"></a>
### Dehorsing, horse blunt damage, falling, AI shield bash and weapon-dependent casualties — vc (`vc.combat_extras_dehorse_bash`)

**What it does:** Riders can be knocked off their horses by heavy hits, blunt blows hurt horses differently, AI infantry use shield bashes, and whether a downed man is killed or only wounded depends on what hit him (spears, axes and stones kill; clubs and sticks knock out).

**How it works:** ti_on_agent_hit triggers (mst:lead_charge/t45 etc., ~62 templates) call check_dehorsing (35 stmts) / check_falling_from_horse / check_horse_blunt_damage. Shield bash: shield_bash_trigger (player key, t48 delay 0.35 s rearm 1 s) and shield_bash_ai_trigger -> shield_bash_script (78 stmts) in ~66 templates; cf_agent_is_in_parrying_animation guards it. ti_on_agent_killed_or_wounded (t7) runs cf_casulties_complication_1 (missile kills: darts/long bow/stones/torch) and cf_casulties_complication_2 (wielded weapon: thrusting spear swings, piercing one-handers, stones, club/stick) to decide kill vs wound. Gore decals (cf_goredec, goredec_special_effects, goredec_player_bonus) attach blood on hit.

- **Hooks:** `mst:lead_charge/t45:conseq`, `mst:lead_charge/t48:conseq`, `mst:lead_charge/t7:conseq`, `mst:lead_charge/t29:conseq`
- **Scripts:** `check_dehorsing`, `check_falling_from_horse`, `check_horse_blunt_damage`, `shield_bash_trigger`, `shield_bash_ai_trigger`, `shield_bash_script`, `cf_agent_is_in_parrying_animation`, `cf_casulties_complication_1`, `cf_casulties_complication_2`, `cf_goredec`, `cf_goredec_probability`, `goredec_special_effects`, `goredec_player_bonus`
- **Mission templates:** `mst_lead_charge`, `mst_village_attack_bandits`, `mst_sea_battle`
- **Globals:** `goredec_player_bonus`
- **Module-specific resources:** item: itm_stones, itm_stones_siege, itm_club_hard, itm_wooden_stick, itm_light_spear1..itm_standard (spear range)
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `dis vc cf_casulties_complication_2: wielded-item tests -> kill flag`, `sqlite blocks meta: lead_charge t45 ti_on_agent_hit -> check_dehorsing; t48 -> shield_bash_trigger; t7 ti_on_agent_killed_or_wounded -> cf_casulties_complication_1/2`

<a id="acwbattle-cry-rout"></a>
### Rally-cry key (B): enemies near the player briefly flee — acw (`acw.battle_cry_rout`)

**What it does:** Pressing B in battle plays a Union/Rebel/Native yell; every enemy within range whose level is at most 2x the player's level + 1 is scripted to run directly away from the player for about 5-7 seconds, then 'Enemies regain their courage!'. 60-second cooldown.

**How it works:** mst:lead_charge/t36 (cond key_clicked key_b, player alive, player in an army or king start; rearm 60 s): faction-specific agent_play_sound (snd_union_yell / snd_rebel_yell / snd_native_yell) on the player; for each living enemy human with level <= 2*player level + 1 and distance < 500 (fixed-point 1 -> metres): compute a point 12x the offset away from the player and agent_set_scripted_destination there. t37 (same key, delay 5 s) and t38 (delay 7 s) agent_clear_scripted_mode on all enemies and print 'Enemies regain their courage!'.

- **Hooks:** `mst:lead_charge/t36:cond`, `mst:lead_charge/t36:conseq`, `mst:lead_charge/t37:conseq`, `mst:lead_charge/t38:conseq`
- **Globals:** `king_start`, `king_faction`, `players_kingdom`
- **Module-specific resources:** sound: snd_union_yell, snd_rebel_yell, snd_native_yell
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis acw mst:lead_charge/t36:cond/conseq, t37, t38`, `sqlite texts: qstr_You_unleash_a_fearso in acw and awoiaf only`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_mission_templates.py 2953-3048 EG3_Warcry`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_scripts.py 45805-45831 EG3 OSP exp-penalty scripts (unused)`
- **Overlaps:** `acw.bury_the_dead`, `be.company_discipline_rout`, `bi.courage_update_staggering`, `nw.morale_rout_rally`, `tld.battle_coherence_rout_rally`, `vc.battle_immersion_courage`
- **Notes:** Oddity: t37/t38 fire on any B press even when t36's condition failed (e.g. not in an army), so the 'regain courage' message can appear without a cry.

<a id="acwbury-the-dead"></a>
### Bury the dead after a victory (honor/morale trade-off) — acw (`acw.bury_the_dead`)

**What it does:** After a field victory the player chooses how to bury the dead: deep individual graves (8 h, +2 honor, +12 morale), shallow individual (6 h, +1 honor, +8 morale), deep mass (4 h, +5 morale), shallow mass (2 h, +3 morale), or leave them (-10 morale). A cemetery party appears on the map and slowly disappears.

**How it works:** menu:total_victory -> jump_to_menu menu_bury_dead (when not in a town fight). Five options all named mno_continue: each calls change_player_honor / change_player_party_morale, spawns pt_grave ('Cemetery') at the player, shows a message and rest_for_hours N; the 'no' option only applies -10 morale and leaves. strig:99 (daily) removes each grave party with 10% chance.

- **Hooks:** `menu:total_victory`, `menu:bury_dead/opt:continue:conseq`, `strig:99`
- **Scripts:** `change_player_honor`, `change_player_party_morale`
- **Menus:** `menu_bury_dead`
- **Module-specific resources:** pt: pt_grave; mesh: mesh_pic_bury_dead
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `raw menus.txt menu_bury_dead option bytecode (honor script #200 change_player_honor, morale #201 change_player_party_morale; amounts 2/12, 1/8, 5, 3, -10; rest 8/6/4/2 h)`, `dis acw menu:total_victory stmt 236`, `dis acw strig:99 (pt_grave removal)`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_game_menus.py 20300 bury_dead; module_simple_triggers.py 4537 '#graves'`
- **Overlaps:** `acw.battle_cry_rout`, `be.company_discipline_rout`, `bi.courage_update_staggering`, `nw.morale_rout_rally`, `tld.battle_coherence_rout_rally`, `vc.battle_immersion_courage`

<a id="becompany-discipline-rout"></a>
### Company discipline, suppression and rout — be (`be.company_discipline_rout`)

**What it does:** Every company (division) in battle has a live discipline score. Taking fire, artillery near-misses and casualties drain it; strength ratio, the faction's army morale, and the player's Captain skill (when the player is near the company) shore it up. Low discipline makes soldiers less accurate and slower, makes them break formation to crouch, and below a threshold the whole company sounds the retreat bugle and runs, rallying once a timer expires.

**How it works:** Per team (0-3) x division (0-7) team-slot arrays. Writers of penalties: mst:lead_charge/t104 (ti_on_agent_killed_or_wounded) adds 6000/quality(34+div) x formation multiplier to casualty slot 187+div; add_penaltytodiscipline_fromfire_to_target_of_agent (from mg_decide_fire) and explode_at_pos add distance-scaled suppression to slot 52+div; get_company_foramtion_discipline_penalty_multiplier scales by formation type (205+div: 40/90/100/110/120 %); technology 420 reduces penalties 20-25 %. mst:lead_charge/t84 (every 0.2 s) decays suppression by 25 and recomputes discipline 197+div = 9000 - suppression(52) - slot 60 - casualties(187) + 1000 x alive/initial(68/34) - (100 - faction slot 834)/5, -1500 if the player has fallen, + Captain skill (skl_reserved_1, id 3) x 100 if the player is within 20+3xskill m of the company's order point (team 100+div / 108+div); clamp 100..10000. mst:lead_charge/t82 (0.5 s) turns discipline (and fatigue 18+div, stance, gas masks, skirmish mode 263+div, tech 408) into agent_set_accuracy_modifier/speed/damage and stores company accuracy in 179+div. mst:lead_charge/t85 (1 s): at <=80 % discipline soldiers randomly take scripted cover and crouch for 6 s. mst:lead_charge/t86 (1 s): discipline < 1500 + Inspirer skill (id 5) x 100 -> company_retreat + snd_bugle_retreat + message; t87 counts down retreat timer 84+div and calls company_stop_retreat + snd_bugle_stop_retreat. Native decide_run_away_or_not is emptied (0/50 stmts) so this replaces Native's per-agent courage rout.

- **Hooks:** `mst:lead_charge/t84:cond`, `mst:lead_charge/t82:cond`, `mst:lead_charge/t85:cond`, `mst:lead_charge/t86:cond`, `mst:lead_charge/t87:cond`, `mst:lead_charge/t104:cond`, `mst:lead_charge/t105:cond`
- **Scripts:** `get_company_foramtion_discipline_penalty_multiplier`, `add_penaltytodiscipline_fromfire_to_target_of_agent`, `explode_at_pos`, `company_retreat`, `company_stop_retreat`, `company_play_bugle`, `reset_companies_accuracy`, `cf_if_company_has_soldiers`, `cf_if_team_faction_invented_technology`, `cf_if_agent_faction_invented_technology`, `cf_random`
- **Presentations:** `prsnt_pbs (shows company discipline/accuracy/energy)`
- **Mission templates:** `all 25 BE templates (same trigger block injected)`
- **Slots:** `team:52-59`, `team:60-67`, `team:68-75`, `team:34-41`, `team:76-83`, `team:84-91`, `team:100-115`, `team:179-186`, `team:187-194`, `team:197-204`, `team:205-212`, `team:263-270`, `agent:29`, `agent:30`, `agent:46`, `agent:63`, `faction:834`
- **Globals:** `g_player_team`, `battle_timer`, `bugle_cooldown`
- **Module-specific resources:** skill: skl_reserved_1 renamed Captain, skl_reserved_2 Desperate Stand (NOEFFECT), skl_reserved_3 Inspirer; sound: snd_bugle_retreat, snd_bugle_stop_retreat; item: itm_gasmask_* (accuracy factor)
- **Relation to Native:** replaces-native
- **Confidence:** confirmed
- **Evidence:** `dis be mst:lead_charge/t84:cond: the discipline formula`, `dis be mst:lead_charge/t86:cond: retreat below 1500 + skill 5 x100, bugle + message`, `dis be add_penaltytodiscipline_fromfire_to_target_of_agent and explode_at_pos: writers to team slot 52+div`, `be skills.txt: skl_reserved_1 'Captain - Increases discipline level of all companies...', skl_reserved_3 'Inspirer - Decreases retreat limit'`, `auto report: decide_run_away_or_not modified 0/50 (emptied)`
- **Overlaps:** `acw.battle_cry_rout`, `acw.bury_the_dead`, `bi.courage_update_staggering`, `nw.morale_rout_rally`, `tld.battle_coherence_rout_rally`, `vc.battle_immersion_courage`

<a id="nwmorale-rout-rally"></a>
### Courage, rout and rally per soldier (with retreat order and difficulty scale) — nw (`nw.morale_rout_rally`)

**What it does:** Each soldier starts with a courage score (scaled by a campaign difficulty modifier for the player's side); deaths nearby lower it, enemy deaths raise it, a soldier whose courage falls below a threshold that rises as he loses health runs away, and he can rally if courage recovers. Ordering a division to 'retreat' makes it rout on purpose.

**How it works:** ti_on_agent_spawn (mst:sp_campaign_*/t1) sets agent slot 24 = 3000-4000 (x $g_global_morale_modifier/10 for team 0) and slot 23 = 0. ti_on_agent_killed_or_wounded (t3) -> apply_death_effect_on_courage_scores: counts same-team agents within 13 m of the casualty, then for every agent within 100 m adds a distance-weighted delta (+10 for enemies; -15+nearby_count capped at -5 for friends, divided by 3 if the casualty was already routing) to slot 24. Every 3 s after 25 s (t9) -> decide_run_away_or_not: if the division's movement order is retreat (mordr 14) or courage < 3500 - 40*hp -> agent_start_running_away + slot 23 = 1; if routed and courage >= 3700 - 40*hp and no retreat order -> agent_stop_running_away (rally).

- **Hooks:** `mst:sp_campaign_vienna/t1:conseq`, `mst:sp_campaign_vienna/t3:conseq`, `mst:sp_campaign_vienna/t8:cond`, `mst:sp_campaign_vienna/t9:cond`, `mst:quick_battle_battle/t4:conseq`, `mst:quick_battle_battle/t19:conseq`
- **Scripts:** `apply_death_effect_on_courage_scores`, `decide_run_away_or_not`, `apply_effect_of_other_people_on_courage_scores`
- **Mission templates:** `mst_sp_campaign_vienna`, `mst_sp_campaign_austerlitz_1`, `mst_sp_campaign_austerlitz_1_old`, `mst_sp_campaign_dresden_1`, `mst_sp_campaign_dresden_2`, `mst_quick_battle_battle`
- **Slots:** `agent:23 (routed flag)`, `agent:24 (courage)`
- **Globals:** `g_global_morale_modifier`
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `dis nw decide_run_away_or_not (36 stmts) - retreat order 14 and rally branch`, `dis nw mst:sp_campaign_vienna/t1:conseq stmts 5-14`
- **Overlaps:** `acw.battle_cry_rout`, `acw.bury_the_dead`, `be.company_discipline_rout`, `bi.courage_update_staggering`, `tld.battle_coherence_rout_rally`, `vc.battle_immersion_courage`

<a id="tldbattle-coherence-rout-rally"></a>
### Side-wide battle morale (coherence), routs and player rallies — tld (`tld.battle_coherence_rout_rally`)

**What it does:** Each side has a coherence score built from troop levels, casualty ratio, leaders' Leadership, banner-bearers, party morale, kills and special presences (e.g. Nazgul). When one side's coherence falls far below the other, a share of its troops breaks and flees, with messages like 'Many of your enemies flee in terror!'. The player can press V to rally (a limited number of times per battle set by Charisma, Leadership and certain horn/whip items), boosting coherence.

**How it works:** coherence (mst triggers every 2 s, every frame and every 30 s across 22 battle templates) loops agents: cf_agent_get_morale per agent, sums ally/enemy level*4, counts routed (agent slot 21) and wounded (agent slot 19), adds hero Leadership (doubled for lords/companions) and fixed bonuses for standard-bearer troops, scales by force ratio, adds party morale, $new_kills, battle-effect bonuses (party slot 308) and persistent modifiers; stores $allies_coh / $enemies_coh. rout_check: gap >= 40 routs a fraction of the weaker side (rout_allies/rout_enemies) and shifts modifiers; morale_check: when a side is below 75 there is an (80-coh)% chance of a smaller rout. Rally: key_clicked key_v (cond $tld_option_morale) after 30 s and if allies_coh <= 80; rallies allowed = 1 + CHA/5 (+Leadership/3 with itm_angmar_whip_reward / itm_horn_gondor_reward), each adds (CHA/5*2 + Leadership*2) to $allies_coh_modifier, plays a cheer and an animation, and re-forms nearby fleeing allies. prsnt:show_num_rallies shows the counter. Routed parties can be spawned on the map afterwards (cf_spawn_routed_parties).

- **Hooks:** `mst:bandit_lair/t88:conseq`, `mst:bandit_lair/t92:conseq`, `mst:bandit_lair/t93:conseq`, `mst:bandit_lair/t90:cond`, `mst:bandit_lair/t90:conseq`
- **Scripts:** `coherence`, `cf_agent_get_morale`, `cf_agent_get_tier_morale`, `rout_check`, `morale_check`, `rout_allies`, `rout_enemies`, `healthbars`, `count_ally_agents_around_agent`, `cf_spawn_routed_parties`, `troop_get_cheer_sound`
- **Presentations:** `prsnt:show_num_rallies`
- **Mission templates:** `mst_lead_charge`, `mst_bandit_lair`, `mst_custom_battle`, `mst_town_brawl`, `mst_tld_caravan_help`
- **Slots:** `agent:19`, `agent:21`, `agent:22`, `party:308`
- **Globals:** `allies_coh`, `enemies_coh`, `allies_coh_modifier`, `enemies_coh_modifier`, `allies_leadership`, `new_kills`, `nazgul_in_battle`, `nazgul_team`, `tld_option_morale`
- **Module-specific resources:** item: itm_angmar_whip_reward, itm_horn_gondor_reward
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis tld coherence (207 stmts, writes $allies_coh/$enemies_coh)`, `dis tld rout_check / morale_check`, `dis tld mst:bandit_lair/t90 cond+conseq (key_v, rally count formula, horn items 857/858)`, `text tld 'You_rally_{reg10}_troops!', 'Rallies:'`
- **Overlaps:** `acw.battle_cry_rout`, `acw.bury_the_dead`, `be.company_discipline_rout`, `bi.courage_update_staggering`, `nw.morale_rout_rally`, `vc.battle_immersion_courage`

<a id="vcbattle-immersion-courage"></a>
### Battle immersion: war cries, horns, shield taunts, berserker rage and morale spreading from nearby events — vc (`vc.battle_immersion_courage`)

**What it does:** Morale in battle becomes local: kills, wounds and hits shake or steel the troops standing near them, with stronger effects close by. The player (and AI troops) can bellow a war cry, sound a horn or bang shields to raise nearby allies' courage, and the player can enter a timed berserker rage (more damage and speed, worse accuracy) with a cooldown and on-screen bar.

**How it works:** change_courage_around_agent(amount, agent) adds amount x 50/40/30/20/10 to agent slot 16 (Native's courage score) of every same-side human within 20/40/70/110/160 m; called from ti_on_agent_killed_or_wounded (mst:lead_charge/t72) and ti_on_agent_hit (t29) triggers in ~56 templates, on top of a modified apply_effect_of_other_people_on_courage_scores (189 vs Native 186 stmts) and apply_death_effect_on_courage_scores. Player actions: t56 (key_clicked key_t, rearm 3 s) and its gamepad twin t57 (key_xbox_x when $controller_keys=1) -> agent_perform_warcry / shield_taunt_trigger / berserk_trigger; berserk_trigger: once $berserk_cooldown=0 sets it to 180, damage x125%, speed 110% (advanced_agent_set_speed_modifier), accuracy and reload 50%, agent slots 46/42, $is_berserk, prsnt_staminabar shows the meter; berserk_cooldown_trigger / berserk_cooldown_modeai_tigger count down. AI: t94 (every 0.7 s) agent_perform_horn / agent_perform_warcry when cf_any_fighting; t46 horn_sp_trigger; t163 opening war cry. Changelog 2.049 'redo battle immersion to avoid sound overload'.

- **Hooks:** `mst:lead_charge/t29:conseq`, `mst:lead_charge/t72:conseq`, `mst:lead_charge/t56:conseq`, `mst:lead_charge/t57:conseq`, `mst:lead_charge/t94:conseq`, `mst:lead_charge/t46:conseq`, `mst:lead_charge/t163:conseq`
- **Scripts:** `change_courage_around_agent`, `apply_effect_of_other_people_on_courage_scores`, `apply_death_effect_on_courage_scores`, `agent_perform_warcry`, `agent_perform_horn`, `agent_perform_shield_taunt`, `shield_taunt_trigger`, `horn_sp_trigger`, `berserk_trigger`, `berserk_cooldown_trigger`, `berserk_cooldown_modeai_tigger`, `berserkermode_fortroop_on`, `advanced_agent_set_speed_modifier`, `cf_any_fighting`, `reset_bonus_effect`
- **Presentations:** `prsnt_staminabar`
- **Mission templates:** `mst_lead_charge`, `mst_village_attack_bandits`, `mst_village_raid`, `mst_sea_battle`
- **Slots:** `agent:16`, `agent:42`, `agent:46`
- **Globals:** `berserk_cooldown`, `is_berserk`, `courage_influence`
- **Module-specific resources:** sound: snd_man_warcry, snd_woman_yell, horn sounds
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `dis vc change_courage_around_agent: distance bands 2000/4000/7000/11000/16000 cm -> x50..x10 into agent slot 16`, `dis vc berserk_trigger: $berserk_cooldown 180, agent_set_damage_modifier 125, speed 110, accuracy/reload 50`, `sqlite blocks meta: lead_charge t29 ti_on_agent_hit, t72 ti_on_agent_killed_or_wounded, t94 check 0.7s, t56/t57 rearm 3 s/0`, `dis vc mst:lead_charge/t56:cond = key_clicked key_t + neg|main_hero_fallen; t57:cond = key_clicked key_xbox_x + $controller_keys=1`
- **Overlaps:** `acw.battle_cry_rout`, `acw.bury_the_dead`, `be.company_discipline_rout`, `bi.courage_update_staggering`, `nw.morale_rout_rally`, `tld.battle_coherence_rout_rally`

<a id="biskirmisher-detachment"></a>
### Skirmisher detachment screen (unreachable) — bi (`bi.skirmisher_detachment`)

**What it does:** A presentation for choosing how many skirmishers to detach into a separate 'Skirmish Party' on the map. It is never opened by any menu, dialog or trigger in 1.6.

**How it works:** prsnt_skirmishers (id 47) slider -> deploy_skirmishers spawns a party named 'Skirmish Party' (party slot 306) toward $skirmish_target; no start_presentation 47 exists anywhere.

- **Hooks:** `prsnt:skirmishers/t0`, `prsnt:skirmishers/t2`
- **Scripts:** `deploy_skirmishers`
- **Presentations:** `prsnt_skirmishers`
- **Slots:** `party:306`
- **Globals:** `skirmish_party_no`, `skirmish_size`, `skirmish_target`, `max_skirmishers`
- **Relation to Native:** new
- **Confidence:** speculative
- **Evidence:** `explain bi prsnt:skirmishers/t2 -> deploy_skirmishers`, `grep bi 'start_presentation, 47' -> no hits`, `cmp.py bi awoiaf deploy_skirmishers op=1.00`

<a id="laiglesize-aware-battlefields"></a>
### Hand-made battlefields chosen by battle size — laigle (`laigle.size_aware_battlefields`)

**What it does:** Field battles on plains are fought on one of eight hand-built maps: five small ones for battles of up to 125 men and three large ones for bigger fights, instead of a random terrain scene.

**How it works:** setup_random_scene (70 stmts vs Native 34) takes the battle size parameter; terrain 3 (plain): size <= 125 -> random scn_field_battle_small_1..5, else scn_field_battle_1..3; other terrains keep random_scene_* scenes.

- **Hooks:** `menu:simple_encounter/opt:encounter_attack:conseq`, `menu:join_battle/opt:join_attack:conseq`
- **Scripts:** `setup_random_scene`
- **Module-specific resources:** scene: scn_field_battle_small_1, scn_field_battle_small_5, scn_field_battle_1, scn_field_battle_3, scn_field_river_small_1
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `dis laigle setup_random_scene`, `explain laigle setup_random_scene (9 menu callers)`
- **Overlaps:** `acw.custom_battle_historical_scenarios`, `cbl.custom_field_battle_scenes`, `tld.region_tracking_and_battle_scenes`

<a id="vcpersistent-division-formations"></a>
### Remembered per-division formations and placements across battles — vc (`vc.persistent_division_formations`)

**What it does:** The player can save how each division should be formed and spaced; at the start of every later battle VC automatically re-applies those formations and spacing to each division and reports it ('Division N <class> formed ...').

**How it works:** memorize_division_placements (34 stmts) stores, per division 0-8, the current formation type and spacing into fac_player_faction slots 300+div (formation), 309+div (spacing) and 318+div (has-data flag); default_division_placements clears them. memorize is reached from the keyboard via mst:lead_charge/t136 (key_clicked key_f7, which also calls player_order_extended_formations) and from the gamepad division menu (t140 rows 5/6, which also offers default_division_placements); the same pair of triggers is repeated in village_attack_bandits, village_raid, quick_battle_battle and the story battles. mst:lead_charge/t150 fires once when $battle_phase=1 and cf_division_data_available: for each division with stored data it issues spread_out(8)/stand_closer(7) orders to reach the saved spacing, then player_attempt_formation (complex formation) or formation_to_native_order + battlegroup_place_around_leader, printing a per-division message.

- **Hooks:** `mst:lead_charge/t150:conseq`, `mst:lead_charge/t136:conseq`, `mst:lead_charge/t140:conseq`
- **Scripts:** `memorize_division_placements`, `default_division_placements`, `cf_division_data_available`, `division_reset_places`, `field_start_position`, `player_attempt_formation`, `formation_to_native_order`, `battlegroup_place_around_leader`, `process_player_division_positioning`, `process_place_divisions`
- **Presentations:** `prsnt_console_division_menu`
- **Mission templates:** `mst_lead_charge`
- **Slots:** `faction:300-308 (fac_player_faction)`, `faction:309-317`, `faction:318-326`, `team:194+div`, `team:203+div`
- **Globals:** `battle_phase`, `g_division_order_processing`, `fplayer_team_no`, `fplayer_agent_no`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis vc mst:lead_charge/t150: cond $battle_phase=1 + cf_division_data_available; reads fac_player_faction slots 300+/309+/318+div, loops team_give_order 7/8, calls player_attempt_formation`, `dis vc mst:lead_charge/t140 rows 5/6 -> memorize_division_placements / default_division_placements`, `sqlite cmp: memorize/default_division_placements vc+awoiaf only`, `dis vc mst:lead_charge/t136:cond = key_clicked key_f7; calls memorize_division_placements + player_order_extended_formations`
- **Overlaps:** `acan.thrust_only_formation_weapons`, `acan.vc_battle_stack_inherited`, `acw.scripted_ai_battle_plan`, `ad457.vc_battle_naval_layer_inherited`, `be.ai_battle_tactics_presets`, `be.infantry_square_and_field_works`, `bi.pbod_formations_ai`, `laigle.pbod_motomataru_stack`, `nw.division_gunpowder_ai`, `nw.locator_line_formations`, `pop.disciplined_faction_ai_gate`, `pop.formations_battle_ai_kit`, `sw.ranged_backstep_ai`, `tld.formations_motomataru_pop_lineage`, `vc.formations_order_translation`

<a id="awoiaftournament-invitations-tpe"></a>
### Tournament invitations and noble reactions (Floris/TPE tournament layer) — awoiaf (`awoiaf.tournament_invitations_tpe`)

**What it does:** Once the player has 200+ renown, lords invite him to the nearest friendly tournament (a timed quest); winning raises relations with the lords and ladies present and gives renown scaled by current fame; an options menu toggles an 'Expert' difficulty and faction-appropriate tournament gear.

**How it works:** strig:184 (12h, renown slot 7 >= 200): scans towns whose party slot 156 (tournament countdown) >= 3 and are friendly, starts qst_floris_active_tournament for the nearest, and fails/ends it when the tournament expires. menu_town_tournament_won -> tpe_noble_reaction_to_win, tpe_rep_gain_lords / tpe_rep_gain_ladies, tpe_determine_scaled_renown; set_items_for_tournament_new / set_items_for_tournament_by_factions choose gear; menu_torneo_opciones toggles expert difficulty.

- **Hooks:** `strig:184`, `menu:town_tournament_won`, `menu:town_tournament/opt:tournament_opciones:conseq`
- **Scripts:** `tpe_noble_reaction_to_win`, `tpe_rep_gain_lords`, `tpe_rep_gain_ladies`, `tpe_determine_scaled_renown`, `tpe_store_town_faction_to_reg0`, `quest_floris_active_tournament_hook_1`, `set_items_for_tournament_new`, `set_items_for_tournament_by_factions`
- **Menus:** `menu_torneo_opciones`
- **Slots:** `party:156`, `troop:7`
- **Module-specific resources:** quest: qst_floris_active_tournament
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `dis strig:184 (renown>=200, nearest friendly tournament town, qst_floris_active_tournament)`, `roots tpe_noble_reaction_to_win -> menu:town_tournament_won`, `refs menu_torneo_opciones <- menu:town_tournament/opt:tournament_opciones`

<a id="laigleboxing-ladder"></a>
### Bare-knuckle boxing ladder in town arenas — laigle (`laigle.boxing_ladder`)

**What it does:** Arena fights become one-on-one boxing bouts. The more bouts you have won, the tougher the opponent (novice to heavyweight) and the bigger the purse (10 to 100).

**How it works:** menu:town/opt:town_arena and the arena master dialog set_jump_mission mst_boxing_fight. mst:boxing_fight/t11 (0.5 s) picks $pugilist and $boxing_prize from $fights_won (>=3/10/15/20 -> regular/veteran/champion/heavyweight fighter, 35/50/75/100) and add_visitors_to_current_scene. t10 sorts agents into teams. Arena master dialog dlg:2652 pays $boxing_prize; $fights_won counts wins.

- **Hooks:** `menu:town/opt:town_arena:conseq`, `mst:boxing_fight/t11:conseq`, `dlg:2652:dlga_arena_master_fight_result:arena_master_pre_talk.1:conseq`
- **Scripts:** `end_tournament_fight`
- **Mission templates:** `mst_boxing_fight`, `mst_arena_melee_fight`
- **Dialogs:** `dlg:2652:dlga_arena_master_fight_result`, `dlg:2665:dlga_arena_master_melee_talk`
- **Slots:** `agent:7`
- **Globals:** `fights_won`, `pugilist`, `boxing_prize`, `recent_boxing_match`, `boxing_match_won`
- **Module-specific resources:** troop: trp_novice_fighter, trp_regular_fighter, trp_veteran_fighter, trp_champion_fighter, trp_heavyweight_fighter
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `grep laigle mst_boxing_fight (menu, dialog, arena template)`, `dis laigle mst:boxing_fight/t11:conseq`, `global laigle boxing_prize -> dlg:2652 pays it`

<a id="oa1860renamed-native-menus"></a>
### Showdowns, Shootouts and colonial army menus (renamed Native) — oa1860 (`oa1860.renamed_native_menus`)

**What it does:** The 'Showdowns' tournament, 'Shootouts' arena duels and 'colonies army' quest menus look new but are Native's tournament, arena-duel and kingdom-army menus with words replaced.

**How it works:** Shape-identical to Native: menu_town_Showdowns = menu_town_tournament (incl. 122-stmt join_next_fight), Showdowns_bet/_confirm/_participants = tournament_*, Shootouts_duel_fight/_conclusion = arena_duel_*, colonies_army_* = kingdom_army_*; menu:camp_action/opt:action_rename_colonies = Native rename kingdom.

- **Hooks:** `menu:town_Showdowns`, `menu:Shootouts_duel_fight/opt:continue:conseq`, `menu:colonies_army_quest_report_to_army`
- **Menus:** `menu_town_Showdowns`, `menu_Showdowns_bet`, `menu_Shootouts_duel_fight`, `menu_Shootouts_duel_conclusion`, `menu_colonies_army_quest_report_to_army`
- **Relation to Native:** native-identical
- **Confidence:** confirmed
- **Evidence:** `sqlite: oa1860 menu shape_hash == native menu shape_hash for every Showdowns/Shootouts/colonies block (n_stmts > 3)`

<a id="acwbounty-hunting-quests"></a>
### Tavern bounty-hunting quests — acw (`acw.bounty_hunting_quests`)

**What it does:** Tavern keepers offer bounties on named outlaws: the player gets a target leading a small band somewhere nearby and a cash reward for catching or killing him.

**How it works:** dlg:2119 tavernkeeper_tell_mission -> random_bounty(talk troop): picks the keeper's town/faction, tries up to 20 times to pick a free quest in qst_bounty_1..qst_kill_local_merchant range not on cooldown (quest slot 25), then sets up the target and quest text; globals bounty_target_1..6 track targets. [Source] Kit marked '# Bounty Hunter BEGIN' (module_scripts.py 47325, random_bounty: up to 20 tries over bounties_begin = qst_bounty_1 .. bounties_end = qst_kill_local_merchant, 7-day expiry, 7-day don't-give-again). Targets are stored in $bounty_target_1..6 and placed in villages; the `bounty_hunting` trigger list ('# Bounty Hunting triggers', module_mission_templates.py 339-559) is attached only to mst village_center: on leaving (Tab) each active bounty succeeds if its target's agent is dead, else fails. Menu block '#Bounty hunting' module_game_menus.py 9123-9322.

- **Hooks:** `dlg:2119:dlga_tavernkeeper_request_mission_ask:tavernkeeper_tell_mission:conseq`
- **Scripts:** `random_bounty`
- **Slots:** `quest:25`, `troop:10`
- **Globals:** `bounty_target_1`, `bounty_target_2`, `bounty_target_3`, `bounty_target_4`, `bounty_target_5`, `bounty_target_6`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `roots acw random_bounty -> tavernkeeper dialog`, `compare random_bounty --mods acw,awoiaf,sw`, `changelog: 'Fixed the bug with the quest to hunt down a fugitive only giving a $1 reward instead of $1,000'`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_scripts.py 47325 random_bounty; module_mission_templates.py 339-559 bounty_hunting; module_constants.py 3313 bounties_begin/end`

<a id="acwespionage-riot-quests"></a>
### President's espionage chain: rescue a spy, meet a spy, incite a riot in an enemy town — acw (`acw.espionage_riot_quests`)

**What it does:** Faction leaders (e.g. Lincoln) can hand the player a covert chain: rescue a captured agent, meet a spy in an enemy town's tavern, then give the signal in the streets to start a riot where townsfolk and guards fight, the town loses 50 prosperity and the player gains faction relation.

**How it works:** State machine in faction slot 390 (1 offered/2 ready/3 spy contacted/4 riot started). dlg:24/33 lincoln_talk_quest offers qst_save_spy; strig:101 hourly succeeds/cancels it by the spy's captivity slot. strig:103 (4 h, 1-in-6, faction slot 390 == 2): picks the faction's historical leader and a free spy hero (trp_union_spy_1..), the closest enemy town not under siege/owned by player, sets qst_talk_to_spy slots and a notification menu menu_qst_talk_to_spy; party slot 95 of the town = spy. dlg:50 talk_to_spy_d starts qst_incite_riot. dlg:40-42 incite_riot_signal: finish_quest, +5 faction relation, then in the town mission: guards/merchants (town troops) become team 1 and aggressive, 5 extra watchmen (faction slot 42) spawn, the faction's leader troop flees, commoners join the player; change_center_prosperity -50, doors locked, qst_the_riot started; mst:town_center/t12 resolves it. [Source, failure paths] The riot reuses the prison-break town mission ($talk_context tc_escape, module_mission_templates.py ~5765-5945): if the player falls, qst_the_riot is aborted and the player goes to captivity (mnu_captivity_start_castle_defeat); if all enemies are beaten (after >= 10 s) qst_the_riot finishes with 100 and the player loses 20 relation with the town's faction. strig:101 cancels talk_to_spy / incite_riot when the target town turns player-owned or non-hostile, when the player enlists (freelancer) or when the quest giver is dead or captured. Save-the-spy pays 5,000 dollars.

- **Hooks:** `dlg:24:dlga_start:lincoln_talk_quest:cond`, `strig:101`, `strig:103`, `dlg:50:dlga_talk_to_spy_d:close_window:conseq`, `dlg:42:dlga_incite_riot_signal_b:close_window:conseq`, `mst:town_center/t12:cond`
- **Scripts:** `get_closest_enemy_town_of_faction`, `add_notification_menu`, `start_quest`, `finish_quest`, `change_center_prosperity`, `change_player_relation_with_faction_ex`
- **Menus:** `menu_qst_talk_to_spy`
- **Dialogs:** `dlga_lincoln_talk_quest`, `dlga_talk_to_spy_d`, `dlga_incite_riot_signal`, `dlga_incite_riot_signal_b`
- **Slots:** `faction:390`, `faction:42`, `faction:51`, `party:95`
- **Globals:** `all_doors_locked`, `talk_context`
- **Module-specific resources:** quest: qst_save_spy, qst_talk_to_spy, qst_incite_riot, qst_the_riot, qst_talk_to_president; troop: trp_union_spy_1.., trp_abraham_lincoln..
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `slot acw faction 390 (writers dlg:22/23/24/33/42, strig:103)`, `dis acw strig:103 stmts 102-160`, `dis acw dlg:42 incite_riot_signal_b (68 stmts)`, `quests.txt titles: Rescue_{s10}, Meet_{s10}_in_{s11}, Incite_a_Riot_in_{s11}, Civil_Unrest`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_mission_templates.py 5765-5945 riot/prison-break triggers`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_simple_triggers.py 4593-4665 (strig:101) and 4907-4961 (strig:103)`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_dialogs.py 573-661 save_spy dialogs`

<a id="acwscout-camp-quest"></a>
### Lord quest: destroy an enemy scout camp — acw (`acw.scout_camp_quest`)

**What it does:** A lord asks the player to find and destroy an enemy scout camp near one of his centers without being seen; the camp is a map party that triggers a dedicated battle mission, with success/failure reported back to the lord.

**How it works:** get_quest (qst_destroy_scout_camp branch) picks target center/faction; dlg:1432/1435 accept names the camp party 'Union/Confederate/Native American Scout Camp' and starts the quest; game_event_party_encounter routes to menu:scout_camp_quest -> mst_destroy_scout_camp (a full battle template copy with the ACW battle triggers) -> menu:destroy_scout_camp_quest_result; dlg:658/659 resolve success/failure with the lord.

- **Hooks:** `dlg:1432:dlga_lord_tell_mission:lord_mission_destroy_scout_camp_a:cond`, `dlg:1435:dlga_lord_mission_destroy_scout_camp_accept:close_window:conseq`, `script:game_event_party_encounter`, `dlg:658:dlga_lord_start:lord_generic_mission_completed:cond`
- **Scripts:** `get_quest`, `abort_quest`
- **Menus:** `menu_scout_camp_quest`, `menu_destroy_scout_camp_quest_result`
- **Mission templates:** `mst_destroy_scout_camp`
- **Slots:** `quest:3`, `quest:7`, `quest:8`
- **Globals:** `random_quest_no`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `refs acw quest qst_destroy_scout_camp (31 refs)`, `grep destroy_scout --mods tld: script_destroy_scout_camp_consequences, dlg lord_mission_destroy_scout_camp_a`, `sqlite texts: TLD 'The_Scout_Camp_has_been_razed'`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/grep scout.camp comments -> none`

<a id="bilost-eagle-quest"></a>
### Senator's 'lost eagle' quest — bi (`bi.lost_eagle_quest`)

**What it does:** A senator NPC asks the player to recover a stolen legionary eagle from thieves; a party is spawned near a fixed location and returning the eagle completes the quest, rewarded with a sellable book.

**How it works:** dlga_start:god1 -> god3 -> godyes: setup_quest_text/start_quest 95, spawn_around_party 184 with template 20, $holy_relic=1; on return 'Did you find the eagle?' -> end_quest 95, $holy_relic=2.

- **Hooks:** `dlg:2721:dlga_start:god1:cond`, `dlg:2724:dlga_god3:godyes:conseq`, `dlg:2718:dlga_relic_find_question:relic_znaleziona:conseq`
- **Scripts:** `start_quest`, `end_quest`
- **Dialogs:** `dlga_start:god1`, `dlga_god3:godyes`, `dlga_relic_find_question`
- **Globals:** `holy_relic`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `global bi holy_relic: writers dlg:2720/2726, readers dlg:2715/2717/2721`, `dis bi dlg:2724 conseq (start_quest 95, spawn_around_party)`

<a id="laiglestory-start-missions"></a>
### Playable story start: inn brawl, pistol duel, smugglers raid — laigle (`laigle.story_start_missions`)

**What it does:** After choosing a starting capital the player plays short scripted scenes - an inn encounter, a formal pistol duel (fire before the signal and you are dishonoured) and a night raid on smugglers - with won/lost outcomes before the campaign begins.

**How it works:** menu:start_phase_3/5 -> mst_start_inn; menu:start_phase_4 -> mst_start_duel; menu:attack_smugglers -> mst_start_smugglers; then menu_start_final. In the duel, timed triggers (t1/t3/t6/t7, 1-5 s) set $duel_clear_to_fire; itm_pistol_duelling's ti_on_weapon_attack sets $duel_violated if the player fires early; dlg:297 start_duel_failed reacts. Outcome strings str_start_won_duel/str_start_lost_duel/str_start_smugglers_won/_lost.

- **Hooks:** `menu:start_phase_3/opt:continue:conseq`, `menu:start_phase_4/opt:continue:conseq`, `menu:attack_smugglers/opt:continue:conseq`, `itm:itm_pistol_duelling/t0`
- **Menus:** `menu_start_phase_5`, `menu_attack_smugglers`, `menu_start_final`
- **Mission templates:** `mst_start_inn`, `mst_start_duel`, `mst_start_smugglers`
- **Dialogs:** `dlg:297:dlga_start:start_duel_failed`
- **Globals:** `duel_started`, `duel_weapon`, `duel_clear_to_fire`, `duel_violated`, `duel_won`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `grep laigle mst_start_inn|mst_start_duel|mst_start_smugglers`, `global laigle duel_clear_to_fire (4 writers in mst_start_duel, read by itm_pistol_duelling)`, `dis laigle itm:itm_pistol_duelling/t0`
- **Overlaps:** `acw.play_as_ruler_start`, `ad457.royal_and_lord_sandbox_start`, `awoiaf.campaign_setup_options`, `cbl.invasion_date_options`, `tld.in_game_strategy_options`

<a id="nwhistorical-campaign-framework"></a>
### Scripted historical-battle campaign (briefing, camp, companion picker, cutscene camera) — nw (`nw.historical_campaign_framework`)

**What it does:** NW's single-player mode is a fixed chain of battles (Vienna bridge, Austerlitz, Dresden x2): a campaign map, a briefing, a walk-around camp with merchants and companions, a companion and companion-equipment picker, scripted fly-over camera intros with letterbox bars and timed objectives, and a memoir screen.

**How it works:** menu:run_mission_dummy branches on $g_finished_missions / $g_finished_sub_missions to jump to scenes 274/275/278/279 with mst_sp_campaign_vienna / austerlitz_1 / dresden_1 / dresden_2, else opens prsnt 59 (campaign map). Each sp_campaign template is a state machine on $g_mission_state: dozens of every-0s triggers each guarded by a mission-state value fire messages, move the cinematic camera (mission_cam_set_mode 1, mission_cam_animate_to_position, mission_cam_animate_to_screen_color fades), deploy divisions (deploy_division_via_teleport) and spawn objective markers. prsnt_singleplayer_companion_select / _companion_equipment_select choose which companions (trp 511-540) join and what they carry; mst_camp_1 is a walkable camp with merchants.

- **Hooks:** `menu:run_mission_dummy`, `menu:visit_camp_dummy`, `menu:go_briefing_dummy`, `mst:sp_campaign_vienna/t14:conseq`, `mst:sp_campaign_vienna/t16:conseq`, `prsnt:singleplayer_campain_map/t0`, `prsnt:singleplayer_camp_screen/t0`, `prsnt:singleplayer_companion_select/t1`
- **Scripts:** `sp_common_before_mission_start`, `deploy_division_via_teleport`, `sp_camp_set_merchandise`
- **Menus:** `menu_run_mission_dummy`, `menu_run_companion_dummy`, `menu_visit_camp_dummy`, `menu_go_briefing_dummy`, `menu_quit_dummy`
- **Presentations:** `prsnt_singleplayer_campain_map`, `prsnt_singleplayer_camp_screen`, `prsnt_singleplayer_memoir_screen`, `prsnt_singleplayer_companion_select`, `prsnt_singleplayer_companion_equipment_select`, `prsnt_singleplayer_cutscene_bars`
- **Mission templates:** `mst_sp_campaign_vienna`, `mst_sp_campaign_austerlitz_1`, `mst_sp_campaign_austerlitz_1_old`, `mst_sp_campaign_dresden_1`, `mst_sp_campaign_dresden_2`, `mst_camp_1`
- **Globals:** `g_finished_missions`, `g_finished_sub_missions`, `g_started_mission`, `g_mission_state`, `g_global_morale_modifier`
- **Module-specific resources:** scene: scn 274, 275, 278, 279 (campaign battlefields), camp scene
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `dis nw menu:run_mission_dummy (jump to scenes 274-279, set_jump_mission 15-19)`, `sqlite names nw mt 15-20 = mst_sp_campaign_* and mst_camp_1`, `dis nw mst:sp_campaign_vienna/t14,t16 (cinematic camera)`, `explain nw prsnt:singleplayer_companion_select/t1 globals g_finished_missions ...`

<a id="awoiafcommoner-trust"></a>
### Commoner trust: a kingdom-wide peasant reputation — awoiaf (`awoiaf.commoner_trust`)

**What it does:** Every relation gain or loss with a village also moves a single 'commoner trust' score shown on the character screen as a title from 'Reaper of peasants' to 'The People's King'. High trust slowly raises relation with every village each week and lets villagers host you for free rest; very low trust erodes relations everywhere.

**How it works:** Modified Native change_player_relation_with_center: when $commoners_trust_on and the center is a village (party slot 0 == 4) the delta is added to $commoner_trust. strig:39 (168h): trust in 400..1000 decays by 1; >400 -> +1 relation with every village; < -600 -> -1 with every village. peasant_approval maps the score to 10 titles for prsnt_character_screen_main. menu:village/opt:village_guest_wait requires trust >= 600 (rest_for_hours_interactive 168h for free). trig:61/62 (one-shot) congratulate the player at trust > 400 (str_peasant_trusted_friend) and >= 1000 (str_peasant_patron_saint). init_char_stat and set_town_spycount seed the starting value from background.

- **Hooks:** `strig:39`, `trig:61:cond`, `trig:62:cond`, `menu:village/opt:village_guest_wait:cond`
- **Scripts:** `change_player_relation_with_center`, `peasant_approval`
- **Menus:** `menu_set_up_commoners_trust`
- **Presentations:** `prsnt_character_screen_main`
- **Slots:** `party:0`
- **Globals:** `commoner_trust`, `commoners_trust_on`
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `global awoiaf commoner_trust: writers change_player_relation_with_center, strig:39, init_char_stat; readers peasant_approval, village_guest_wait, trig:61/62`, `dis change_player_relation_with_center stmt 21-33: val_add $commoner_trust by delta when village`, `dis strig:39 weekly drift`, `dis peasant_approval: 10 title bands`
- **Overlaps:** `bi.triumphus`, `pop.post_battle_lord_relation_gain`, `tld.lord_friendship_gifts`

<a id="bitriumphus"></a>
### Triumphus after taking a city — bi (`bi.triumphus`)

**What it does:** A vassal of a Roman faction with 150+ renown who captures a town (not castles: the gate is center id 35-99, BI's town range) and is on good terms (+10) with the emperor may be granted a triumph: a celebratory screen offering a parade through the city for +25 renown, +3 relation with the ruler and a cash share of the spoils (25 x the captured fief's prosperity, 500-2525 denars). It can be refused.

**How it works:** menu:castle_taken calls cf_player_deserves_triumphus(center): center is a town (ids 35-99), player has homage, player kingdom is one of the Roman factions, troop slot 7 (renown) >= 150, ruler (faction slot 11) relation >= 10 -> jump_to_menu 77 (menu_triumphus, bare integer). menu_triumphus computes spoils from party slot 50 (prosperity) into $g_triumphus_spoils; accept option calls change_troop_renown 25, change_player_relation_with_troop ruler 3, troop_add_gold.

- **Hooks:** `menu:castle_taken`, `menu:triumphus`, `menu:triumphus/opt:triumphus_accept:conseq`
- **Scripts:** `cf_player_deserves_triumphus`, `change_troop_renown`, `change_player_relation_with_troop`
- **Menus:** `menu_triumphus`, `menu_castle_taken`
- **Slots:** `troop:7`, `faction:11`, `party:50`
- **Globals:** `g_triumphus_spoils`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `grep bi: menu:castle_taken @27 (jump_to_menu, 77) after cf_player_deserves_triumphus call`, `dis bi menu:triumphus + opt triumphus_accept conseq`, `menu text 'The senate and people of {s10} have decreed a triumphus...'`, `menu:triumphus background is mesh_pic_messenger (Native picture) - no custom art needed`
- **Overlaps:** `awoiaf.commoner_trust`, `pop.post_battle_lord_relation_gain`, `tld.lord_friendship_gifts`

<a id="popknighthood-order-membership"></a>
### Joinable knighthood orders with rank points, order quests and expulsion — pop (`pop.knighthood_order_membership`)

**What it does:** The player can petition a knighthood order at its chapterhouse, pass a test of arms in the arena against the order's champion, and become a member. Order work (bounty hunting, winning a tournament in the order's name, a 'challenge' of many victories with lent order troops, settling a rivalry with another order) earns rank points; seven rank tiers unlock titles, order armour sets and recruitment of the order's knights. Acting against the order strips membership.

**How it works:** Membership is stored on the player as troop slot 162 (order leader/troop whose faction is the order). Joining: dlg:3877 (hall_order_join_confirm) sets $g_order_challenge_troop and jumps to mst_arena_heroic_challenge_fight in the nearest town's arena (party slot 16). change_rank_points_with_order(order_faction, points) scales points by (relation order<->player faction + 100)/100 and accumulates in faction slot 71; get_rank_from_rank_points maps 30/60/100/150/220/300 thresholds to ranks 1-7. Order quest givers (hall_order_guard_talk -> order_choose_quest dlg:3879-3884) issue qst_order_bounty / qst_order_tournament / order challenge / qst_order_rivalry; rewards (dlg:3891, 3898, 3904, 3912) give XP, renown, honour, faction relation and 6-8+ rank points (bounty scales by value killed). Promotions dlg:3796/3811; expulsion dlg:3799; resignation dlg:3867/3871; order books can be sold for rank (dlg:3842/3844); armour sets bought via buy_order_armour_set.

- **Hooks:** `dlg:3877:dlga_hall_order_join_confirm:close_window:conseq`, `dlg:3840:dlga_hall_order_guard_talk:order_choose_quest:cond`, `dlg:3891:dlga_order_bounty_reward:close_window:conseq`, `dlg:3898:dlga_order_tournament_reward:close_window:conseq`, `dlg:3904:dlga_order_challenge_reward:order_challenge_reward_mercs:conseq`, `dlg:3912:dlga_order_rivalry_reward:close_window:conseq`, `dlg:3796:dlga_start:close_window.56:conseq`, `dlg:3799:dlga_start:close_window.59:conseq`
- **Scripts:** `change_rank_points_with_order`, `get_rank_from_rank_points`, `get_knighthood_order_info`, `finish_quest_simple`, `reward_for_quest_per_player_level`
- **Menus:** `menu_order_relations_report`, `menu_camp_quests35`
- **Mission templates:** `mst_arena_heroic_challenge_fight`
- **Dialogs:** `dlg:3838-3849 hall_order_guard_talk`, `dlg:3867-3877 hall_order_join/resign`, `dlg:3879-3884 order_choose_quest`, `dlg:3891`, `dlg:3898`, `dlg:3904`, `dlg:3912`, `dlg:3796`, `dlg:3799`, `dlg:3811`
- **Slots:** `troop:162`, `faction:71`, `party:16`
- **Globals:** `g_order_challenge_won`, `g_order_challenge_troop`, `g_talk_troop_faction`
- **Module-specific resources:** quest: qst_order_bounty, qst_order_tournament, qst_order_rivalry; faction: fac_dragon_knights .. fac_player_knights (knighthood order factions); troop: trp_dragon_knight, trp_lion_knight, trp_radiant_cross_knight, ...
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis change_rank_points_with_order and get_rank_from_rank_points (full)`, `dis dlg:3877 conseq: arena challenge jump`, `dis reward dialogs 3891/3898/3912: rank point awards`, `slot pop troop 162: 51 accesses incl. promotion/expulsion/resign dialogs`, `texts: order quest prompts dlg:3880-3883`
- **Overlaps:** `acan.enlistment_career_events`, `acan.ranks_offices_titles`, `acw.enlistment_contract_career`, `acw.freelancer_extensions`, `ad457.court_offices_and_titles`, `ad457.freelancer_variant`, `be.enlistment_service_ranks`, `bi.freelancer_reassignment`, `laigle.military_rank_career`, `tld.faction_rank_influence`

<a id="poppost-battle-lord-relation-gain"></a>
### Automatic relation gain with lords who fought beside you — pop (`pop.post_battle_lord_relation_gain`)

**What it does:** After a battle the player wins together with allied lords, each lord who was on the player's side gains +1 relation (+2 for martial personalities), unless he already dislikes the player.

**How it works:** automatic_relation_gain_after_battles (called from game_event_simulate_battle, menu:total_victory, menu:castle_taken_by_friends): loops over lords/companion-lords; if a stack of that hero is in p_collective_friends and his relation with the player is >= -5, adds 1, or 2 when troop slot 52 (Native slot_lord_reputation_type) = 1 (martial), via troop_change_relation_with_troop.

- **Hooks:** `menu:total_victory`, `menu:castle_taken_by_friends`, `script:game_event_simulate_battle`
- **Scripts:** `automatic_relation_gain_after_battles`, `troop_change_relation_with_troop`, `troop_get_relation_with_troop`
- **Menus:** `menu_total_victory`, `menu_castle_taken_by_friends`
- **Slots:** `troop:2`, `troop:52`
- **Globals:** `players_kingdom`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis automatic_relation_gain_after_battles (full 32 stmts)`, `explain callers: menu:total_victory, menu:castle_taken_by_friends, game_event_simulate_battle`
- **Overlaps:** `awoiaf.commoner_trust`, `bi.triumphus`, `tld.lord_friendship_gifts`

<a id="tldfaction-rank-influence"></a>
### Rank and Influence per faction — tld (`tld.faction_rank_influence`)

**What it does:** Every faction tracks the player's rank points and a spendable Influence currency separately. Deeds for a faction raise its rank (named titles per faction), which pays a daily RP stipend, enlarges the party limit, and unlocks special services; Influence is spent on things money cannot buy -- special reward items, trolls/captains, healing, commanding allied armies, convincing a marshal.

**How it works:** Faction slot 71 = rank points, slot 70 = Influence. get_faction_rank turns points into a rank with a quadratic curve (points = 10r^2 + 40r; get_rank_points_for_rank is the inverse). increase_rank(faction, pts) (54 callers: quests, battles, dialogs) scales the gain by Charisma, player's own faction (+20%), option $tld_option_rank_gain_rate, halves gains before the war starts, and adds Influence = (pts+4)/8 with a carry-over remainder ($tld_influence_rest) and trait modifiers (Oathkeeper +, Oathbreaker -); on a rank change new_rank_attained plays a sound and announces the title. strig:8 rank_income_to_player pays 5r^2+10r RP per day per faction. spend_influence_of deducts slot 70 with a message. game_get_party_companion_limit adds the rank of every faction (double for the player's own). Titles come from get_*_rank_title_to_s24 (faction-specific strings). menu:rank_report lists all.

- **Hooks:** `strig:8`, `menu:rank_report`, `script:game_get_party_companion_limit`
- **Scripts:** `get_faction_rank`, `get_rank_points_for_rank`, `increase_rank`, `new_rank_attained`, `rank_income_to_player`, `spend_influence_of`, `get_rank_title_to_s24`, `get_own_rank_title_to_s24`, `get_allied_rank_title_to_s24`, `get_any_rank_title_to_s24`, `calculate_rank_gain_new`, `game_get_party_companion_limit`
- **Menus:** `menu:rank_report`, `menu:reports/opt:view_rank_report`
- **Dialogs:** `dlg:552:dlga_lord_talk:lord_get_reward_item_ask:cond`, `dlg:555:dlga_lord_get_reward_item:lord_get_reward_item_answer:conseq`, `dlg:274:dlga_player_hire_trolls_take:player_hire_trolls_how_many:cond`, `dlg:265:dlga_player_hire_captain_1:player_hire_captain_2:cond`, `dlg:578:dlga_marshall_answer:close_window:conseq`
- **Slots:** `faction:70`, `faction:71`, `troop:9 (trp_traits)`, `troop:10 (trp_traits)`
- **Globals:** `tld_option_rank_gain_rate`, `tld_option_influence_gain_rate`, `tld_influence_rest`, `tld_war_began`, `players_kingdom`
- **Module-specific resources:** string: rank title strings per faction, qstr_You_spent_{reg10}_of
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis tld get_faction_rank (sqrt of 4*10*pts + 40^2)`, `dis tld increase_rank: slots 70/71, option multipliers, trait 9/10 on trp_traits`, `dis tld rank_income_to_player called from strig:8`, `dis tld game_get_party_companion_limit loop 3..21 get_faction_rank`, `explain tld get_faction_rank: 60 callers incl. dlg154, menu47`
- **Overlaps:** `acan.enlistment_career_events`, `acan.ranks_offices_titles`, `acw.enlistment_contract_career`, `acw.freelancer_extensions`, `ad457.court_offices_and_titles`, `ad457.freelancer_variant`, `be.enlistment_service_ranks`, `bi.freelancer_reassignment`, `laigle.military_rank_career`, `pop.knighthood_order_membership`

<a id="acantown-decrees"></a>
### Town decrees (curfew, entry controls, garbage collection, social housing, strict law, begging ban) — acan (`acan.town_decrees`)

**What it does:** Each town or fort can carry up to six standing decrees. The player issues or revokes them for gold from the fief-management screen, and AI lords issue and revoke them on their own. Every decree trades prosperity, crime, disease or the townsfolk's goodwill against each other.

**How it works:** Each decree is a 0/1 flag in party slots 264-269 (curfew, entry controls, garbage collection, social housing, strict law enforcement, begging ban). Names and descriptions come from get_decree_details. The player toggles a decree in prsnt:center_management/t4, which shows a gold-cost confirmation. AI lords decide in troop_does_business_in_center via decide_decree_enact and decide_decree_revoke. Those two scripts roll against the lord's attribute, the town's prosperity (party slot 46), the lord's personality (troop slot 52) and a culture bonus for 'barbarian' factions. Effects read the flags in these places: cf_center_night_bandits_check (strig:188/189) for night bandit infestation, which curfew, housing and strict law affect; strig:158 for the epidemic chance, which garbage collection lowers; strig:157 for monthly-ish relation changes (housing raises relation, entry controls and strict law lower it); get_center_ideal_prosperity (housing, strict law, begging ban); do_merchant_town_trade and menu:control at the town gate (entry controls); town menu options and rumours (curfew); and center_get_capital. A notification fires when an AI lord enacts or revokes a decree.

- **Hooks:** `prsnt:center_management/t0`, `prsnt:center_management/t4`, `prsnt:fief_management/t0`, `script:troop_does_business_in_center`, `strig:157`, `strig:158`, `strig:188`, `strig:189`, `strig:19`, `strig:146`, `strig:147`, `menu:control`
- **Scripts:** `get_decree_details`, `decide_decree_enact`, `decide_decree_revoke`, `cf_center_night_bandits_check`, `get_center_ideal_prosperity`, `center_get_capital`, `do_merchant_town_trade`, `troop_does_business_in_center`, `get_generic_rumour_string_to_s4`
- **Menus:** `menu_control`, `menu_town`
- **Presentations:** `prsnt_center_management`, `prsnt_fief_management`
- **Dialogs:** `dlg:9624:dlga_town_dweller_talk (begging, slot 269)`, `dlg:9656-9658 town_dweller_ask_situation (slots 267/268)`
- **Slots:** `party:264`, `party:265`, `party:266`, `party:267`, `party:268`, `party:269`, `party:46`, `party:115`, `troop:52`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `slot acan party 264-269: writers prsnt:center_management/t4 + troop_does_business_in_center, readers listed above`, `dis acan decide_decree_enact: probability per decree by attribute/prosperity/personality`, `text 'decree' --mods acan: str_decree_*_name/description, 'Issuing a decree costs {reg0} denarii', '{s10} has enacted the decree {s30} in {s4}'`, `dis acan strig:158: party 266 (garbage collection) +50 to the epidemic-roll divisor`, `text 'Quarantine|Decree|Curfew' --mods ad457: only qstr 'Decree_Effects:' in prsnt:center_management/t0; compare decide_decree_enact --mods acan,ad457: ad457 absent`
- **Overlaps:** `acan.imperial_treasury_budget`, `acan.senate_influence_edicts`, `ad457.dplmc4_tax_inefficiency_and_extras`, `be.pps_political_simulation`

<a id="bepps-political-simulation"></a>
### Political simulation: classes, parties, parliament, laws, unrest and civil war — be (`be.pps_political_simulation`)

**What it does:** Every nation simulates five social classes (aristocracy, bourgeoisie, ... workers, peasants) with wealth, satisfaction and political activity, four political parties with influence and class support, a government type (monarchy to republic), parliament and executive elections, laws enforced by the ruling party, a budget and corruption, and popular movements (liberal and socialist) that escalate from demonstrations to riots to rebellions; a winning rebellion changes the government and may split the country in civil war. Battle casualties reduce town populations.

**How it works:** strig:124 (every tick, one faction) -> pps_faction_iteration: faction_calculate_pps_pes_slots, pps_calculate_faction_classes_wealth, pps_calculate_faction_classes_satisfaction (353 stmts), per-class political activity, per-party influence and class support, pps_ai_faction_manage_budget, republic/parliament/executive elections, pps_faction_calculate_budget, corruption, pps_faction_process_movements (245), propaganda/repression, pps_faction_random_event (364: anti-war protests if war weariness slot 841 > 2000, etc.), then PAS lord count, military resources, manpower, faction_remove_if_no_towns. Events -> menus menu_socialism_demonstration/riot/rebellion(_won), menu_liberal_*; pps_faction_process_event_effect_*_rebellion spawn rebel parties (pt_pps_rebels) using center_get_rebel_troop; pps_init_civil_war. pps_faction_inflict_battle_casualty (from every mission's ti_on_agent_killed_or_wounded, mst:lead_charge/t25) subtracts 600 x casualties from random towns' population (party slot 401). prsnt_pps_menu (1012 stmts) visualises it. Faction slots 501-520 (parties/classes), 839-843 (movements, war weariness).

- **Hooks:** `strig:124`, `strig:137`, `strig:138`, `strig:139`, `strig:140`, `mst:lead_charge/t25:conseq`, `prsnt:pps_menu/t0`
- **Scripts:** `pps_faction_iteration`, `pps_calculate_faction_classes_wealth`, `pps_calculate_faction_classes_satisfaction`, `pps_calculate_faction_class_political_activity`, `pps_calculate_faction_party_influence`, `pps_calculate_faction_class_support_of_party`, `pps_faction_parliament_election`, `pps_faction_executivebranch_election`, `pps_faction_republic_election`, `pps_faction_calculate_budget`, `pps_faction_calculate_corruption_level`, `pps_faction_process_movements`, `pps_faction_random_event`, `pps_faction_apply_law`, `pps_faction_change_government_type`, `pps_init_civil_war`, `pps_faction_inflict_battle_casualty`, `pps_init`, `pps_menu_display_faction`, `center_get_rebel_troop`
- **Menus:** `menu_socialism_demonstration`, `menu_socialism_riot`, `menu_socialism_rebellion`, `menu_socialism_rebellion_won`, `menu_liberal_demonstration`, `menu_liberal_riot`, `menu_liberal_rebellion`, `menu_pas_civil_war_side_choose`
- **Presentations:** `prsnt_pps_menu`, `prsnt_custom_faction_settings`
- **Slots:** `faction:501-520`, `faction:539-552`, `faction:802`, `faction:839-843`, `party:401`
- **Globals:** `pps_start_new_iteration_cycle`, `pps_ruling_party_change_cooldown`
- **Module-specific resources:** pt: pt_pps_rebels; troop: trp_rebel_european1, trp_rebel_balkan1, trp_rebel_turkish1, ...; mesh: mesh_pps_*
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `dis be pps_faction_iteration (call list)`, `explain be prsnt:pps_menu/t0 (class/party/parliament texts)`, `dis be pps_faction_inflict_battle_casualty`, `auto report: 40+ pps_* scripts, menus socialism/liberal *`
- **Overlaps:** `acan.imperial_treasury_budget`, `acan.senate_influence_edicts`, `acan.town_decrees`, `ad457.dplmc4_tax_inefficiency_and_extras`

<a id="acanpatron-gods-piety-miracles"></a>
### Patron deity, piety and sacrifices, with divine boons and in-battle miracles — acan (`acan.patron_gods_piety_miracles`)

**What it does:** The player chooses a patron god and builds piety by sacrificing at temples and priests and by pious acts. A sacrifice rolls for a boon (protection in fight, leadership, favour, wisdom, experience). In battle, a favoured player may get a miracle every few seconds: extra strength, courage for nearby troops, or healing. Piety also changes the price of political actions and how lords see you.

**How it works:** Piety is the global $player_piety, changed by add_piety (62 callers: dialogs, menus, strigs) and rated by get_piety_impact ('Hated by the gods'..'Honored by the gods'). Worship dialogs (dlg:10413/10494 worship_gods) set the patron (troop slot 23), and deity_compatibility_with_culture and add_piety_culture_effect adjust relations by the god's fit with a culture. make_sacrifice (priest dialogs dlg:10425/10465/10502) costs gold, rolls 'Probability {reg10} / Dice {reg11}' and grants a timed boon (quest 27 slot as the boon store, $can_sacrific cooldown). perform_miracle runs every 3 s in about 29 battle templates (gated by cf_can_perform_miracle) and can boost the player's strength, raise troop courage (agent slot 3) or heal. visit_temple and the temple submenus give scenes for each god. player_change_religion changes faith. Piety feeds get_influence_cost_for_decision and the conspiracy check.

- **Hooks:** `dlg:10413:dlga_worship_gods2_pagan`, `dlg:10494:dlga_worship_gods2`, `dlg:10425:dlga_pagano1_action_sacrifice_4`, `dlg:10502:dlga_sacrifice_male_sure_2`, `mst:lead_charge (perform_miracle every 3s)`, `menu:temples_submenu`, `menu:cattle_herd_kill_opfer`
- **Scripts:** `add_piety`, `get_piety_impact`, `make_sacrifice`, `perform_miracle`, `cf_can_perform_miracle`, `deity_compatibility_with_culture`, `add_piety_culture_effect`, `player_change_religion`, `visit_temple`, `get_sacrifice_value`, `get_priest_for_god`
- **Menus:** `menu_temples_submenu`, `menu_cattle_herd_kill_opfer`
- **Mission templates:** `mst_visit_temple`, `mst_cutscene_sacrifice`, `mst_paganholysite`
- **Slots:** `troop:23`, `agent:3`, `quest:27`
- **Globals:** `player_piety`, `can_sacrific`, `guard_god`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `explain acan add_piety: writes player_piety, 'You gained/lost {reg0} pietas'`, `explain acan make_sacrifice: 'Probability: {reg10}. Dice: {reg11}', boons '{s19} guards you in fight / help you to lead / favour you / blesses your mind / gives you experience'`, `explain acan perform_miracle: every 3s in 29 mission templates, texts 'increases your strength / gives your troops courage / heals you'`, `explain acan ai_assign_title text 'Hated by the gods'..'Honored by the gods'`
- **Overlaps:** `ad457.religion_faiths_and_piety`, `awoiaf.four_faiths_religion`, `vc.monasteries_and_hofs`, `vc.religion_center_conversion`

<a id="ad457religion-faiths-and-piety"></a>
### Faiths for lords and kingdoms, player conversion, piety and battle blessings — ad457 (`ad457.religion_faiths_and_piety`)

**What it does:** Every kingdom has an official faith (five Christian confessions, Roman paganism, Germanic/steppe paganism, two Zoroastrian schools, Judaism) and every lord has a personal faith. Every three days a random lord may convert to his kingdom's (or culture's) faith, which is announced. The player picks a faith at the start, can convert by talking to bishops/abbots/high priests, can dedicate himself to a pagan pantheon at shrines (which raises relation with lords of that faith), and earns piety by praying, sacrificing, donating, funding memorials and through event choices. With piety above 25 the player may receive a random blessing in battle (allies faster, damage changes, or the player healed). Religious sites are real map locations with monasteries, temples and shrines.

**How it works:** Faith codes 0-9 (0 Chalcedonian, 1 Arian, 2 Miaphysite, 3 Nestorian, 4 Donatist, 5 Paganism, 6 Roman paganism, 7 Mazdaist, 8 Zurvanite, 9 Judaism). init_religions (from game_start, 160 stmts) assigns religion factions (fac_roman_christians, fac_arian_christians, fac_coptic_christians, fac_nestorian_christians, fac_donatist_christians, fac_pagans, fac_roman_pagans, fac_zoroastrians...) to p_religious_site_* parties with scenes (christian_monastery, fire_temple, german_temple_*, celtic_stone_circle, steppe_shrine, roman_pagan_temple, siwa) and abbot/priest troops. Kingdom faith = faction slot 13, lord faith = troop slot 15 (spouse slot 30 follows). strig:15 (every 72h) calls check_lord_religion on a random hero: if his faith differs from his kingdom's, he converts when the kingdom is one of a listed set or his culture (troop 44) matches, and a log line names the new faith. Player faith $g_player_faith set by menu_religion_selection, MCC presets, player_is_king/lord, and conversion dialogs (dlg:4686, 4700, 4712, 4724, 5932-5981); the player can also ask a lord to convert (dlg:1204 lord_talk_convert, dlg:1208-1225 choices, each setting the lord's troop 15). $piety written by menu:religious_location_christian/generic options (pray/sacrifice +1 piety and 1 hour, memorial +5 honour, donate 500, raid, seize the monastery), event menus and quest dialogs. menu:religious_location_generic dedication options call change_player_relation_lords_religion(faith, amount), which loops lords and changes relation by faith match. mst:lead_charge/t91 (and the same trigger in other battle templates; check 3s, rearm 100000000 = once per battle) with $piety>25 and 16% chance applies a random blessing: allied agent_set_damage_modifier 95 or 110, agent_set_speed_modifier 110, or heals the player to full. Temple building 142 (ad457.center_buildings_management) is named after the holder's faith.

- **Hooks:** `strig:15`, `script:game_start`, `menu:religious_location_christian`, `menu:religious_location_generic`, `menu:religion_selection`, `mst:lead_charge/t91:conseq`, `dlg:4686:dlga_chalcedonian_bishop_talk:chalcedonian_bishop_talk_convert_1:conseq`
- **Scripts:** `init_religions`, `check_lord_religion`, `change_player_relation_lords_religion`, `change_player_relation_with_troop_religion`, `change_player_relation_with_troop`
- **Menus:** `menu_religion_selection`, `menu_religious_location_christian`, `menu_religious_location_generic`
- **Mission templates:** `mst_religious_center`, `mst_religious_center_noricum`
- **Dialogs:** `dlg:4686`, `dlg:4700`, `dlg:4712`, `dlg:4724`, `dlg:5932`, `dlg:5938`, `dlg:5944`, `dlg:5950`, `dlg:5956`, `dlg:5964`, `dlg:5972`, `dlg:5981`
- **Slots:** `troop:15`, `troop:30`, `troop:44`, `faction:13`, `party:255`
- **Globals:** `g_player_faith`, `piety`, `g_player_converted`, `g_paganism_dedication`
- **Module-specific resources:** faction: fac_roman_christians, fac_arian_christians, fac_coptic_christians, fac_nestorian_christians, fac_donatist_christians, fac_pagans, fac_roman_pagans, fac_zoroastrians, fac_zurvanism, fac_jews; party: p_religious_site_1..N; scene: scn_christian_monastery, scn_christian_monastery_desert, scn_fire_temple, scn_german_temple_1-3, scn_celtic_stone_circle, scn_steppe_shrine, scn_roman_pagan_temple, scn_siwa; troop: trp_roman_abbot, trp_coptic_abbot, trp_pagan_high_priest, trp_zoroastrian_high_priest, trp_roman_pagan_high_priest, trp_monk, trp_pagan_priest
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis ad457 check_lord_religion: troop 15 vs faction 13, conversion + log '{s35} has converted ...', faith names list`, `dis ad457 strig:15 stmt 1-2: random hero -> check_lord_religion every 72h`, `explain ad457 init_religions: religion faction refs, p_religious_site_* parties, temple scenes, priest troops`, `global ad457 g_player_faith: writers = religion_selection options + 12 conversion dialogs + MCC/sandbox scripts`, `global ad457 piety: writers = religious_location menus, event menus, dialogs; readers = battle templates t91 and menu:reports`, `dis ad457 mst:lead_charge/t91:conseq: $piety>25, 16% roll, damage/speed modifiers or heal, 'Your faith increases...'`, `slot ad457 troop 15: 340 accesses in 132 blocks, values 0-9; writers include init_religions, check_lord_religion, religion_selection options, lord_talk_convert dialogs 1210-1225`, `dis ad457 initialize_banner_info: slot 15 written only on trp_banner_background_color_array (array element), not on lords`
- **Overlaps:** `acan.patron_gods_piety_miracles`, `awoiaf.four_faiths_religion`, `vc.monasteries_and_hofs`, `vc.religion_center_conversion`
- **Notes:** Oddity: the 95 damage-modifier blessing lowers allied damage although it is announced as a faith boost.

<a id="awoiaffour-faiths-religion"></a>
### Four-faith religion (Seven, Old Gods, R'hllor, Drowned God) - extends VC's religion — awoiaf (`awoiaf.four_faiths_religion`)

**What it does:** The player's faith (chosen at creation or by conversion with a priest) gates temple visits, faith-specific recruits (red priests, old-gods worshippers, drowned men), religious loot choices after plundering, holy-man party encounters that attack non-believers, fief buildings (sept, weirwood grove, R'hllor temple, Drowned God shrine) and faith events; each center's mix of faiths drifts weekly.

**How it works:** inherits vc.religion ($g_player_faith, priest dialogs dlga_sacerdote_talk/pagano_talk, regular_member_talk faith actions) and extends it from VC's two faiths to four: added dlga_rhllor_talk / dlga_drowned_god_talk conversions, prsnt_rhllor_yesorno / old_gods_yesorno / drowned_god_yesorno, prsnt_loot_choice_fos/_old_gods/_rhllor/_drowned_god, menu_recruit_red_priests / recruit_old_gods / recruit_drowned_men, faith buildings in the chamberlain build list (dlg:2493-2500), and strig:161 (168h) that rebalances per-center faith shares in party slots 340-343 and writes $g_sod_global_faith.

- **Hooks:** `strig:161`, `dlg:5711:dlga_rhllor_talk:rhllor_ayuda.1:conseq`, `dlg:5724:dlga_drowned_god_talk:drowned_god_ayuda.1:conseq`
- **Menus:** `menu_recruit_red_priests`, `menu_recruit_old_gods`, `menu_recruit_drowned_men`, `menu_temple_visit`, `menu_godswood_visit`, `menu_driftwood_alter_visit`, `menu_septry_visit`
- **Presentations:** `prsnt_loot_choice_fos`, `prsnt_loot_choice_old_gods`, `prsnt_loot_choice_rhllor`, `prsnt_loot_choice_drowned_god`, `prsnt_rhllor_yesorno`, `prsnt_old_gods_yesorno`, `prsnt_drowned_god_yesorno`
- **Slots:** `party:340`, `party:341`, `party:342`, `party:343`
- **Globals:** `g_player_faith`, `g_sod_global_faith`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `global awoiaf g_player_faith: writers priest conversion dialogs (Seven, Old Gods, R'hllor, Drowned God) + yes/no presentations + init_char_stat`, `explain strig:161: party slots 340-343 + g_sod_global_faith`
- **Overlaps:** `acan.patron_gods_piety_miracles`, `ad457.religion_faiths_and_piety`, `vc.monasteries_and_hofs`, `vc.religion_center_conversion`

<a id="awoiafnights-watch-rules"></a>
### Night's Watch as a neutral sworn order: take the black, send prisoners to the Wall, rangers and free-folk raiders — awoiaf (`awoiaf.nights_watch_rules`)

**What it does:** The Night's Watch (fac_kingdom_10) is not a normal kingdom: it stays out of the Westeros war/peace churn, the player can swear the oath and serve as a brother (deserting makes every Westeros realm hostile), captured lords can be sent to the Wall instead of executed (they become Watch members with black gear, their fiefs revert and succession runs if they were king), common prisoners can be donated to the Watch for coin and honour (they reappear as Watch recruits in its commander's army), and every 72 h a ranger patrol and a free-folk raiding party are kept alive north of the Wall.

**How it works:** strig:54 loops fac_kingdom_1..fac_kingdom_10 with an exclusive upper bound, so the Watch never accrues truce/casus-belli; kill_prisoner_dialogue skips fac_kingdom_10 when spreading relation penalties. Joining: dlga_lord_request_enlistment nw_join_* dialogs (freelancer-style enlistment; price = commander level x10 via faction slot 101/41) - leaving/deserting runs event_player_deserts_nw (set_player_relation_with_faction -75 with kingdoms 1,2,4,5,6,8,9,10...). Take the black: dlg:6448/6458 prisoner_chat_treason_execute_wall -> change_troop_faction(lord, fac_kingdom_10), +50 relation with the Watch leader (faction slot 11), loot_hero_items + nightswatch gear, renown/relation penalties with his old faction, king succession by max renown, give_center_to_faction for his fiefs. Donation: dlga_lord_wall_prisoners / wandering crows / Ramun -> sell_all_prisoners_nw (pays game_get_prisoner_price, party_add_members <Watch leader party> trp_nw_recruit = number sold, +1 Watch relation, +1 honour). strig:106 (72h): if factions 11 / 10 alive, spawn_ff_raiding_parties / spawn_nw_patrol_parties keep one pt_ff_raiding_party and one pt_nw_ranger_patrol on the map.

- **Hooks:** `strig:106`, `strig:54`, `dlg:6458:dlga_prisoner_chat_treason_execute_wall1:close_window:conseq`, `dlg:4175:dlga_lord_wall_prisoners:lord_talk:conseq`, `dlg:4166:dlga_lord_talk:lord_request_enlistment.1:cond`
- **Scripts:** `sell_all_prisoners_nw`, `event_player_deserts_nw`, `freelancer_event_player_revolts_nw`, `spawn_nw_patrol_parties`, `spawn_ff_raiding_parties`, `change_troop_faction`, `loot_hero_items`
- **Dialogs:** `dlga_nw_join_06`, `dlga_lord_wall_prisoners`, `dlga_prisoner_chat_treason_execute_wall1`, `dlga_wandering_crows_sell_prisoners_all_2`
- **Slots:** `faction:11`, `faction:21`, `faction:41`, `faction:101`
- **Globals:** `leftnightswatch`, `freelancer_state`, `enlisted_lord`
- **Module-specific resources:** faction: fac_kingdom_10 (Night's Watch), fac_kingdom_11 (free folk); pt: pt_nw_ranger_patrol, pt_ff_raiding_party; troop: trp_nw_recruit, trp_wandering_crow_1..; item: itm_nightswatch_d_cloaked
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `refs awoiaf faction fac_kingdom_10: 117 refs incl. nw_join dialogs, prisoner_chat_treason_execute_wall, sell prisoners, event_player_deserts_nw`, `dis dlg:6458 conseq (change_troop_faction -> fac_kingdom_10, NW gear, succession, fief transfer)`, `dis sell_all_prisoners_nw (gold + trp_nw_recruit added to Watch leader party)`, `dis strig:106 + spawn_nw_patrol_parties / spawn_ff_raiding_parties`, `dis strig:54: try_for_range fac_kingdom_1..fac_kingdom_10 (exclusive bound)`, `texts menu:set_up_wars '...all factions (except the Night's Watch) are free to declare war and peace'`

<a id="biromanitas"></a>
### Romanitas (how Roman a settlement is) — bi (`bi.romanitas`)

**What it does:** Each settlement has a 0-100 'Romanitas' score built from its Roman monuments plus +25 if it belongs to a Roman faction. High Romanitas makes the settlement more prosperous, its people friendlier, its volunteers better, and its townsfolk more willing to fight under siege.

**How it works:** center_recalculate_romanitas (called monthly from center_apply_monthly_building_effects, strig:82) sums horreum 5, castra 5, templum 8, thermae 12, basilica 12, aquaeductus 15, amphitheatrum 18, +25 Roman faction, caps at 100, stores in party slot 605. Readers: monthly effects (+1 prosperity at >=50, +1 relation at >=70), update_volunteer_troops_in_village (>=50: +2 upgrade rolls, +15% chance -> higher-tier volunteers), process_sieges (romanitas/10 added to siege militia size).

- **Hooks:** `strig:82`
- **Scripts:** `center_recalculate_romanitas`, `cf_center_is_roman`, `center_apply_monthly_building_effects`, `update_volunteer_troops_in_village`, `process_sieges`
- **Slots:** `party:605`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis bi center_recalculate_romanitas`, `slot bi party 605: written only by center_recalculate_romanitas; read by process_sieges and update_volunteer_troops_in_village`, `dis bi cf_center_is_roman: faction ids map to fac_kingdom_1 Rome, 7 Roman Gallia, 8 Roman Illyricum, 9 Roman Asia, 10 Roman Hispania (factions.txt)`

<a id="vcmonasteries-and-hofs"></a>
### Monasteries and pagan hofs as visitable map sites (donate, learn to read, convert, recruit, pillage) — vc (`vc.monasteries_and_hofs`)

**What it does:** Monasteries and hofs are their own map locations. The player can visit the monks or the hof, donate 500 for a blessing, pay 4000 to learn to read, convert to that faith, recruit (monks/priests at monasteries, berserkers at hofs), or pillage the site for silver and goods - which leaves it ruined and smoking for weeks and stops it influencing local religion.

**How it works:** menu:monasterio_visit / menu:paganholysites_visit options: entermo/enter_hofho -> mst_monasterio / mst_paganholysite walk-around scenes; donatemo/donate_hofho set $g_rezar_monasterio (cooldown cleared by strig:106, every 90h); aprender_leermo teaches reading; convertirmo/convertir_norsegho write $g_player_faith; monasterio_recruitm / hof_recruitho recruit; pillage_monasterymo / pillage_hofho launch mst_monasterio_atacado / mst_paganholysites_atacado and then menu:saquear_monasterio / saquear_paganholysite: prisoners screen, loot screen built from trade goods (wine, ale, jewelry, amber, silver, food) scaled by skl_looting, gold reward, quest hook qst_blank_quest_3, and party slot 344 (plunder timer) + slot 38 (burning particle). strig:135 (every 23.7h) counts slot 344 down for towns, monasteries and hofs, clears the smoke particle and restores the icon via change_party_icon_loot_state. strig:103 ignores plundered sites when computing conversion pressure.

- **Hooks:** `menu:monasterio_visit`, `menu:paganholysites_visit`, `menu:saquear_monasterio`, `menu:saquear_paganholysite`, `strig:135`, `strig:106`
- **Scripts:** `change_party_icon_loot_state`, `party_add_wounded_members_as_prisoners`, `troop_add_gold`
- **Menus:** `menu_monasterio_visit`, `menu_paganholysites_visit`, `menu_saquear_monasterio`, `menu_saquear_paganholysite`
- **Mission templates:** `mst_monasterio`, `mst_monasterio_interior`, `mst_paganholysite`, `mst_monasterio_atacado`, `mst_paganholysites_atacado`
- **Dialogs:** `dlga_pagano1_action`
- **Slots:** `party:344`, `party:38`
- **Globals:** `g_rezar_monasterio`, `g_player_faith`, `capture_screen_shown`, `loot_screen_shown`
- **Module-specific resources:** party: p_monasterio1..p_yourlair, p_paganholysites1..p_oldpagan_hut; item: itm_wine, itm_ale, itm_jewelry, itm_amber, itm_silver; skill: skl_looting; scene: monastery and hof scenes
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `sqlite texts mopt: 'Make a donation to the monastery (500 peningas)', 'Learn how to read (4000 peningas)', 'Convert to Christianity', 'Try to recruit a berserker', 'Pillage the monastery/Hof'`, `sqlite refs: mst_monasterio_atacado <- monasterio_visit/opt:pillage_monasterymo, mst_paganholysites_atacado <- paganholysites_visit/opt:pillage_hofho`, `dis vc menu:saquear_monasterio: loot from trade goods scaled by skl_looting, gold, qst_blank_quest_3`, `dis vc strig:135: slot 344 countdown for towns/monasteries/hofs, party_clear_particle_systems`
- **Overlaps:** `acan.patron_gods_piety_miracles`, `ad457.religion_faiths_and_piety`, `awoiaf.four_faiths_religion`, `vc.religion_center_conversion`

<a id="vcreligion-center-conversion"></a>
### Christian/pagan religion of settlements, slow conversion and player faith — vc (`vc.religion_center_conversion`)

**What it does:** Every town, fort and village has an official religion (Christian or pagan) and a Christian-population percentage that drifts over time. Religious buildings, the lord's own faith and the nearest monastery or hof push it; when the minority grows past a threshold the settlement flips. The player picks a faith at character creation and can convert later; whether a settlement shares the holder's faith changes its relation with the player, and the player's minister reports kingdom-wide conversion progress. Faith also scales weekly fief income: strig:116 multiplies a player-owned center's rent by the share of people who share the player's faith.

**How it works:** strig:103 (every 0.62h) picks one random center (p_town_1..p_salt_mine) that is not plundered (party slot 344=0): party slot 235 = Christian share 0-100 is nudged by religion buildings (improvement slots 134 Christian Monastery / 140 Christian Church, 136 Temple to Odin / 142 Shrine to Norse Gods), the holder lord's faith (troop slot 16: 1=Christian, 2=pagan) and the closest unplundered monastery (p_monasterio1..) or hof (p_paganholysites1..) within 20 map units, with log messages; improvement 145 (Merchants' Rest Hall) also adds prosperity (slot 50), 146 (Scriptorium) can raise the player's reading and 141 (Brewery) relation. For centers the player owns, slot 26 (relation) moves up or down depending on $g_player_faith vs slot 234 (official religion 1/2) and the share; slot 397 modifies it. Above 80% share a pagan center may flip slot 234 to Christian (and the mirror case). $faith_conversion accumulates when centers of the player's kingdom move toward the player's faith and is reported by the minister (dlga_minister_faith). menu_village_force_convert1 lets the player forcibly convert a village (5 hours; success from persuasion, power strike, attributes, character-creation virtue/defect, the share), and the center_manage options center_build_religion1-4 build churches/hofs. Faith is chosen in menu_start_game_2/4 ($religion_type -> $g_player_faith) and changed at monasteries/hofs (vc.monasteries_and_hofs). cf_troop_religion_matches_players gates recruitment and some dialogs.

- **Hooks:** `strig:103`, `menu:village_force_convert1`, `menu:village_force_convert_confirm`, `menu:center_manage/opt:center_build_religion1:conseq`, `dlg:1327:dlga_minister_talk:minister_faith:cond`, `strig:116`
- **Scripts:** `cf_troop_religion_matches_players`, `change_player_relation_with_center`
- **Menus:** `menu_village_force_convert1`, `menu_village_force_convert_confirm`, `menu_center_manage`, `menu_start_game_2`, `menu_start_game_4`
- **Presentations:** `prsnt_player_sheet_bio`
- **Dialogs:** `dlga_minister_faith`, `dlga_sacerdote_talk`, `dlga_pagano_talk`
- **Slots:** `party:234`, `party:235`, `party:134`, `party:136`, `party:140`, `party:142`, `party:145`, `party:146`, `party:26`, `party:50`, `party:397`, `party:344`, `troop:16`
- **Globals:** `g_player_faith`, `faith_conversion`, `religion_type`, `virtue_type`, `defect_type`
- **Module-specific resources:** faction: fac_christians, fac_pagans; party: p_monasterio1..p_yourlair (monasteries), p_paganholysites1..p_oldpagan_hut (hofs)
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis vc strig:103 (249 stmts): slot 235 drift from buildings/lord faith/nearest monastery or hof, slot 26 relation by $g_player_faith vs slot 234, flip slot 234 when share >80`, `dis vc menu:village_force_convert1: success = persuasion/power strike/attributes scaled by slot 235 and $g_player_faith`, `sqlite globals g_player_faith: 55 reads incl. enter_court, set_goal_lord_reward, center_build_religion1-4 conds; writers game_start, start_game_4, monastery/hof convert options, priest dialogs`, `dis vc strig:116 (168h): center income x f(slot 235, $g_player_faith) for player-owned centers, reduced when plundered (slot 344)`
- **Overlaps:** `acan.patron_gods_piety_miracles`, `ad457.religion_faiths_and_piety`, `awoiaf.four_faiths_religion`, `vc.monasteries_and_hofs`

<a id="acansettlement-events-epidemics"></a>
### Settlement events and epidemics (inherits ad457.settlement_disasters_epidemics; acan adds harvests, winters, sanitation and wider effects) — acan (`acan.settlement_events_epidemics`)

**What it does:** Towns and villages get one active local event at a time: a good or poor harvest, a harsh or mild winter, drought, insects, an earthquake, a fire, or a disease outbreak (consumption, fevers, plague, measles and others). For its duration the event changes prosperity growth, rents, recruits and town-dweller talk. When the player owns the place they are notified, and for an epidemic they can order a quarantine.

**How it works:** Party slot 324 holds the active event id. get_event_details turns the id into a name, a description, a prosperity-rate percentage (reg0) and a prosperity delta (reg1); its id bands encode event type and severity. strig:158 (about hourly) picks a random town, rolls an epidemic weighted by month (winter is worse) and by sanitation (garbage-collection decree party 266, sewers improvement party 294, hospital improvement party 287), picks a disease, applies change_center_prosperity, sets slot 324 and notifies the holder with menu_epidemic_outbreak (option: 'Order a quarantine'). strig:163 rolls earthquakes in seismic regions (cf_can_have_earthquake reads the region in party 68) and sends menu_disaster_event. calculate_weekly_rents ages and clears events. Readers: get_center_ideal_prosperity, calculate_weekly_rents, calculate_latifundium_rents, get_volunteer_limits (fewer recruits), process_player_enterprise, get_rumor_to_s61, town and village menus and dweller dialogs.

- **Hooks:** `strig:158`, `strig:163`, `menu:epidemic_outbreak`, `menu:disaster_event`, `script:calculate_weekly_rents`
- **Scripts:** `get_event_details`, `cf_can_have_earthquake`, `change_center_prosperity`, `get_center_ideal_prosperity`, `get_volunteer_limits`, `calculate_weekly_rents`
- **Menus:** `menu_epidemic_outbreak`, `menu_disaster_event`, `menu_event_city_desaster_1`
- **Slots:** `party:324`, `party:325`, `party:266`, `party:287`, `party:294`, `party:68`, `party:46`
- **Globals:** `g_cur_month`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis acan get_event_details: id bands -> poor/good harvest, conquered, harsh/mild winter, earthquake, fire, drought, insects, Rome fire, consumption, slow fever, camp fever, plague, measles`, `dis acan strig:158: month weighting, slot 266/294/287 modifiers, sets party 324, add_notification_menu menu_epidemic_outbreak`, `slot acan party 324: 21 accesses in 15 blocks (menus, rents, volunteers, enterprise, rumours)`, `compare get_event_details: ad457 109 stmts/79% shape`, `compare get_event_details --mods acan,ad457: 166 vs 109 stmts, 79% shape; dis ad457 get_event_details: str_disease_* incl. smallpox/greatpox, no harvest/winter strings`
- **Overlaps:** `ad457.settlement_disasters_epidemics`, `pop.fief_heartbeat_problems`

<a id="acwhistorical-event-calendar"></a>
### Day-counted historical event calendar (incl. leader assassination) — acw (`acw.historical_event_calendar`)

**What it does:** A daily counter fires one-time news events on fixed campaign days (ironclads, locomotive chase, emancipation, bread riots, draft riots, Hunley, St. Albans raid, Stonewall). On day 1140 Lincoln is assassinated if still free: he is removed from all parties, quests involving him are cancelled, and Andrew Johnson is installed as the new president in Washington or the nearest Union town.

**How it works:** strig:8 (daily): decays faction slot 99 by player right-to-rule; $days_passed += 1 unless $game_ended; per event 'if days_passed > N and $X_event == 0 -> add_notification_menu (or display_message while camping) and set flag'. Day 426: trp_knight_4_1's party is ordered to retreat to the closest friendly walled center (party_set_ai_state 7) - the Stonewall notification itself comes from strig:9. Day 1140: troop slot 2 of Lincoln set to 15 (inactive), party_remove_members from every party, rename trp_andrew_johnson, cancel quests whose giver/target is Lincoln, party_add_leader Johnson to p_town_8 (if Union-held) else the closest Union center.

- **Hooks:** `strig:8`, `strig:9`
- **Scripts:** `add_notification_menu`, `cancel_quest`, `get_closest_union_center`, `party_set_ai_state`, `get_closest_allied_any_walled_center_of_faction_nonsiege`
- **Menus:** `menu_notification_ironclads`, `menu_notification_emancipation`, `menu_notification_locomotive_chase`, `menu_notification_bread_riots`, `menu_notification_draft_riots`, `menu_notification_st_albans_raid`, `menu_notification_hunley`, `menu_notification_lincoln`, `menu_notification_stonewall`
- **Slots:** `faction:99`, `troop:2`, `troop:8`, `troop:10`
- **Globals:** `days_passed`, `game_ended`, `ironclads_event`, `emancipation_event`, `locomotive_chase_event`, `bread_riots_event`, `draft_riots_event`, `st_albans_raid_event`, `hunley_event`, `hold_washington`, `hold_richmond`
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `dis acw strig:8 (170 stmts)`, `refs acw menu menu_notification_stonewall -> strig:9`, `global acw hold_washington: 1 writer (game_start), 0 readers`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_simple_triggers.py 425-500 commented capital counter; 506-540 Stonewall branch`
- **Overlaps:** `ad457.travel_random_events`, `awoiaf.canon_story_event_timeline`, `awoiaf.random_travel_events`, `sw.random_town_ambushes`, `vc.random_events_and_judgments`

<a id="acwprisoner-breakouts-and-refugees"></a>
### Prisoner break-outs from overloaded parties and refugee columns — acw (`acw.prisoner_breakouts_and_refugees`)

**What it does:** Any non-lord, non-center party holding more than 50 prisoners suffers a break-out: the prisoners become an 'Escaped Prisoners' party that heads for the nearest walled center of their own side. Separately, up to 8 'Escaped Slaves' parties at a time flee from Confederate towns toward the nearest Union town.

**How it works:** strig:103 (every 4 h): try_for_parties skipping main party / captor / centers / lord parties; party_get_num_prisoners > 50 -> spawn pt_routed_warriors named 'Escaped Prisoners', neutral, move all non-hero prisoner stacks (keeping wounded counts) into it; if its first troop belongs to a kingdom or aligned bandit faction it takes that faction and targets get_closest_allied_walled_center_of_faction; icon chosen by side/mounted. Then if fewer than 8 pt_escaped_slaves exist, create_escaped_slaves spawns one at a random Confederate town aimed at the closest hostile town. The same trigger also re-adds large unwounded non-flag stacks of lord parties (remove + force_add) and offers the spy quest (see espionage feature).

- **Hooks:** `strig:103`
- **Scripts:** `create_escaped_slaves`, `get_closest_allied_walled_center_of_faction`, `get_closest_hostile_town`
- **Slots:** `troop:182`
- **Globals:** `capturer_party`
- **Module-specific resources:** pt: pt_routed_warriors, pt_escaped_slaves
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis acw strig:103 stmts 0-78`, `dis acw create_escaped_slaves`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_simple_triggers.py 4682-4800`
- **Overlaps:** `pop.raid_refugees`, `vc.prisoner_revolts`

<a id="ad457settlement-disasters-epidemics"></a>
### Seasonal disasters and epidemics in settlements — ad457 (`ad457.settlement_disasters_epidemics`)

**What it does:** Towns and villages can be hit by epidemics, droughts, crop failures, fires and (rarely) earthquakes. Odds depend on the season and on buildings: sewers/baths and similar make plague less likely, while fires burn down several of the settlement's buildings. A hit costs prosperity and cuts the settlement's stored rents; the fief owner gets a notification menu describing what happened, and the event stays on the settlement (it shows in its management screen, rumours and ideal prosperity) until it expires.

**How it works:** Five random-centre triggers set an event code in party slot 800 (disaster) or 801 (epidemic) when that slot is 0: strig:142 (every 0.74h, towns/castles) epidemic: chance = season factor (1-3 by $g_cur_month) out of (180 - prosperity + 25, +100 if building 152, +50 if 145), severity 5-35 (-1 if both buildings), sets 801, notifies via menu_epidemic_outbreak; strig:143 (villages, code 120, odds out of 250-300, +200 with building 139, -50 with 135); strig:144 (villages, code 130, odds out of 350-400); strig:145 (all centres, code 100, 1/700, rents x0.25 - the earthquake-class event); strig:146 (towns, code 110 fire: 300 base, season 20-50, building 148 halves risk, port towns +25; loops building slots 128-156 except a protected list and randomly clears up to N buildings, owner gets 'The fire in {s60} de...' per building). Each sets party 47 (accumulated rents) to 75% (25% for code 100) and applies prosperity change reg1 from get_event_details (109 stmts: code -> name/description/prosperity effect). strig:47 (every 0.37h) reads/clears slot 800 over time; get_center_ideal_prosperity, center_get_capital, get_rumor_to_s61 and prsnt:center_management read it.

- **Hooks:** `strig:142`, `strig:143`, `strig:144`, `strig:145`, `strig:146`, `strig:47`
- **Scripts:** `get_event_details`, `change_center_prosperity`, `add_notification_menu`, `get_center_ideal_prosperity`, `get_rumor_to_s61`, `center_get_capital`
- **Menus:** `menu_disaster_event`, `menu_epidemic_outbreak`
- **Presentations:** `prsnt_center_management`
- **Dialogs:** `dlg:4286:dlga_town_dweller_ask_situation:town_dweller_talk:cond`
- **Slots:** `party:800`, `party:801`, `party:47`, `party:50`, `party:128-156 (buildings destroyed by fire)`, `party:139`, `party:135`, `party:145`, `party:148`, `party:152`
- **Globals:** `g_cur_month`
- **Module-specific resources:** string: event names/descriptions in get_event_details: recently conquered, earthquake, fire, drought, ...
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis ad457 strig:142/143/144/145/146: seasonal odds, building modifiers, slot 800/801 writes, menu_disaster_event / menu_epidemic_outbreak notifications`, `slot ad457 party 800: written by strig:47/143/144/145/146 (values 0,100,110,120,130), read by menu:disaster_event, center_get_capital, get_center_ideal_prosperity, get_rumor_to_s61`, `explain ad457 get_event_details: text 'recently_conquered | earthquake | fire | drought ...'`, `menu:disaster_event text 'Disaster!^^{s10} was hit by a disastrous {s0}. {s1}...'`
- **Overlaps:** `acan.settlement_events_epidemics`, `pop.fief_heartbeat_problems`

<a id="ad457town-rebellions-secession"></a>
### Town revolts that spawn rebel kingdoms, plus rebel reconciliation and riots in ownerless towns — ad457 (`ad457.town_rebellions_secession`)

**What it does:** Towns can rise in revolt: a rebel army appears and besieges the town, and if it wins, the town becomes the seat of a new breakaway kingdom named after it, using the culture and troops of the kingdom it left. Later, a sufficiently old rebel kingdom of the right culture may make peace with and rejoin the Western Roman Empire, handing back its towns and lords while its leader becomes an outlaw. Towns that end up with no proper owner are besieged by rioting citizens.

**How it works:** strig:147 (every 3h, random walled centre): if party slot 811 == 1 (revolt armed) and 813 holds a rebel faction, sets war (-100) with the holder, sets 811=0, 812 = 90-120 day cooldown, calls cf_launch_rebellion and jumps the player to menu_rebellion_launched; cf_launch_rebellion spawns pt_rebel_army at the town (party slot 123 = home), fills it 35-45 times from the rebel faction's reinforcement templates (faction slots 77/78), sets AI to besiege (behaviour 4, object = town), marks the town under siege (party 54 = rebel party, 64 = start hour) and calls village_set_state(5). Separately, with 1/50 chance for specific towns of listed kingdoms, cf_start_rebellion(town, parent faction) takes a free pooled faction from fac_rebel_kingdom_1..3 (faction slot 21 == 2 = unused), renames it after the town, copies culture (10), banner/troop slots 15/22/40-59 and reinforcement templates 77-79 from the parent (Hispania templates for listed towns), sets 811=3 (countdown) and 812 cooldown. strig:15 (72h) reconciliation: a rebel faction at peace with fac_kingdom_1, same culture, faction slot 1450 > 30, 1/20 chance -> marked defeated (21=2), its lords join kingdom_1, its centres go to kingdom_1, its leader becomes an outlaw, its parties change faction, player shown menu_rebels_join_rome. strig:117 (72h): any town/castle owned by fac_manhunters or fac_commoners gets a 600-man 'Rioting Citizens' party (fac_outlaws, besieging, ignore player).

- **Hooks:** `strig:147`, `strig:15`, `strig:117`
- **Scripts:** `cf_start_rebellion`, `cf_launch_rebellion`, `village_set_state`, `recalculate_ais_for_faction`, `change_troop_faction`, `give_center_to_faction`
- **Menus:** `menu_rebellion_launched`, `menu_rebels_join_rome`, `menu_generic_rebellion_launched`, `menu_uprising_successful`
- **Slots:** `party:811`, `party:812`, `party:813`, `party:54`, `party:64`, `party:123`, `faction:21`, `faction:10`, `faction:15`, `faction:22`, `faction:40-59`, `faction:77`, `faction:78`, `faction:79`, `faction:1450`
- **Globals:** `g_infinite_camping`, `freelancer_state`, `players_kingdom`
- **Module-specific resources:** faction: fac_rebel_kingdom_1, fac_rebel_kingdom_2, fac_rebel_kingdom_3; pt: pt_rebel_army, pt_hispenias_a/b/c; troop: trp_bandit, trp_brigand (riot filler)
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis ad457 strig:147 stmts 0-52: 811/812/813 state machine, set_relation -100, cf_launch_rebellion, jump_to_menu menu_rebellion_launched, log '{s10} has revolted!'`, `dis ad457 cf_start_rebellion: pooled fac_rebel_kingdom_1..3, faction_set_name from town, slot copies 40-60 and 77-80`, `dis ad457 cf_launch_rebellion: spawn pt_rebel_army, 35-45 template adds, besiege behaviour, party 54/64`, `dis ad457 strig:15 stmts 3-73: rebel faction rejoins fac_kingdom_1, menu_rebels_join_rome`, `dis ad457 strig:117 stmts 45-66: 'Rioting_Citizens' 300 bandits + 300 brigands besiege ownerless centres`
- **Overlaps:** `acan.civil_war_usurpation_restoration`, `ad457.landless_faction_cleanup`, `tld.faction_defeat_redistribution_last_stand`, `vc.faction_restoration_and_adventurers`

<a id="ad457travel-random-events"></a>
### Random travel events with moral choices — ad457 (`ad457.travel_random_events`)

**What it does:** Every few days a renowned player (200+ renown) leading more than 30 men on land may run into one of about 23 small events: a sacrificial animal, beggars, a hungry child, Huns offering to join for 300 silver, travellers asking for money, and so on. Each offers choices that cost or earn silver, piety, honour or men.

**How it works:** strig:132 (every 96h): map_free, not enlisted ($freelancer_state 0), not camping, not captive, land terrain, 1/5 roll, renown (troop 7) >= 200 and > 30 men -> random 0-43 picks menu_event_01..21 (some gated on terrain or troops_can_join), menu_event_pilos_1 and a second unique event (flags $g_unique_event_1/2). The menus' options write $piety, gold, honour or add troops (e.g. menu_event_03 Huns join for 300).

- **Hooks:** `strig:132`
- **Menus:** `menu_event_01`, `menu_event_02`, `menu_event_03`, `menu_event_06`, `menu_event_07`, `menu_event_18`, `menu_event_21`, `menu_event_pilos_1`, `menu_event_aurelian_1`
- **Slots:** `troop:7`
- **Globals:** `piety`, `g_unique_event_1`, `g_unique_event_2`, `freelancer_state`, `g_infinite_camping`
- **Module-specific resources:** mesh: event background pictures
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis ad457 strig:132: gating conditions and 23-way jump_to_menu`, `global ad457 piety writers: menu:event_01/02/06/07/18/pilos_1 option consequences`, `dis ad457 menu:event_03: 'You spot a small group of huns ... join you for a small fee of 300 siliquae.'`
- **Overlaps:** `acw.historical_event_calendar`, `awoiaf.canon_story_event_timeline`, `awoiaf.random_travel_events`, `sw.random_town_ambushes`, `vc.random_events_and_judgments`

<a id="awoiafcanon-story-event-timeline"></a>
### Canon story-event timeline (Red Wedding, Battle of the Bastards, Craster's Keep, Ned's death, Varys/Daenerys invasion...) — awoiaf (`awoiaf.canon_story_event_timeline`)

**What it does:** Book/show events fire on day thresholds when the involved lords are still alive and the player is not enlisted on the wrong side: the Red Wedding (lords gathered at the Twins, special interior/exterior battle), Battle of the Bastards (choose Jon or Ramsay, Jon Snow duel), mutiny at Craster's Keep, Ned's death, Robb Stark's marriage, the Hound rescue, Aegon/Daenerys landing to claim the throne, Dothraki raids, and 'King of the Seven Kingdoms' when one faction wins. Outcomes change faction ownership, kill or capture lords, and can hand the player rewards.

**How it works:** One-shot timed triggers (trig:6..33, rearm 1e8) check store_current_day thresholds, faction slot 21 (faction state) and troop slot 2 (lord dead/occupation) and $freelancer_state/$enlisted_lord, then move lord parties (party_attach_to_party to p_castle_39 for the Red Wedding) and jump_to_menu the event menu. Menus offer choices that launch dedicated mission templates (mst_red_wedding_interior/_exterior, mst_battle_of_the_bastards, mst_jon_snow_duel, mst_crasters_keep_mutiny, mst_bridge_of_skulls...) and resolve via scripts red_wedding_rob_lost, battle_of_the_bastards_jon_won/_lost. Varys/Doran/Ellaria quest dialogs advance $invasion_triggered; at value 5 trig:101 (book names: Aegon lands) or trig:102 (TV names: Daenerys) fires the Targaryen invasion. Faith-specific events (trig:6 -> menu_rhllor_event / fos_event / old_gods_event / drowned_god_event) depend on $background_reason and $g_player_faith.

- **Hooks:** `trig:6:cond`, `trig:25:cond`, `trig:30:cond`, `trig:101:conseq`, `trig:102:conseq`
- **Scripts:** `red_wedding_rob_lost`, `battle_of_the_bastards_jon_won`, `battle_of_the_bastards_jon_lost`
- **Menus:** `menu_red_wedding_event_menu`, `menu_red_wedding_interior`, `menu_red_wedding_exterior`, `menu_battle_of_the_bastards_part_one`, `menu_battle_of_the_bastards_battle`, `menu_mutiny_at_crasters_keep_request`, `menu_crasters_keep`, `menu_ned_dead_event_menu`, `menu_robb_stark_marraige`, `menu_the_hound_event`, `menu_varys_invasion`, `menu_varys_invasion_dany`, `menu_varys_dual_invasion_dany`, `menu_dothraki_event`, `menu_king_of_seven_kingdoms`, `menu_rhllor_event`, `menu_fos_event`, `menu_old_gods_event`, `menu_drowned_god_event`
- **Mission templates:** `mst_red_wedding_interior`, `mst_red_wedding_exterior`, `mst_battle_of_the_bastards`, `mst_jon_snow_duel`, `mst_crasters_keep_mutiny`, `mst_bridge_of_skulls`
- **Slots:** `faction:21`, `troop:2`, `troop:10`
- **Globals:** `red_wedding`, `battle_of_the_bastards`, `invasion_triggered`, `freelancer_state`, `enlisted_lord`, `g_player_faith`, `background_reason`
- **Module-specific resources:** scene: Twins interior/exterior, Winterfell field, Craster's Keep; troop: trp_kingdom_4_lord, trp_kingdom_5_lord, trp_knight_4_4, trp_knight_5_2
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis trig:30:cond: day>=150, $red_wedding==0, factions 4/5 alive, lords alive, attaches their parties to p_castle_39`, `dis trig:25:cond: day>=340 + Stark lady slots -> marriage event`, `dis trig:6: $background_reason==4 then faith-specific event menu`, `global awoiaf invasion_triggered: writers Varys/Doran/Ellaria quest dialogs, trig:101/102`, `mission templates not in VC/Native: mst_red_wedding_*, mst_battle_of_the_bastards, mst_crasters_keep_mutiny, mst_jon_snow_duel`
- **Overlaps:** `acw.historical_event_calendar`, `ad457.travel_random_events`, `awoiaf.random_travel_events`, `sw.random_town_ambushes`, `vc.random_events_and_judgments`

<a id="awoiafrandom-travel-events"></a>
### Random travel events (renown-gated choice events + weekly minor incidents) — awoiaf (`awoiaf.random_travel_events`)

**What it does:** While travelling the player periodically gets a random event: a bard sings of your deeds, beggars swarm your famous procession, freeriders or young nobles ask to join for extra pay, Red Priests burning a man, etc. Each offers choices with gold/honour/relation/troop outcomes. Separately, once a week a small incident pops up (training accident, toothache, found a gold bag, contaminated water, wagon of mead) that nudges health, morale, gold or items.

**How it works:** Six simple triggers on long, staggered periods (strig:166 194h, 167 310h, 168 284h, 169 260h, 170 224h, 171 170h) share a guard block (not enlisted, not in camp/siege/village-work, not captive, main-party slot 500 == 0, player troop slot 8 (Native slot_troop_leaded_party) < 0) and a renown threshold (player troop slot 7 > 330 etc.), roll store_random_in_range and jump_to_menu one of menu_event_01..42/101..103 (some guarded by one-shot globals like $kurkelet). strig:165 (168h) rolls one of 11 minor incidents (avoids repeating $g_lyx_last_random_event) applying change_troop_health, change_player_party_morale, troop_add_gold/item via dialog_box. strig:172 (315h, $player_is_king) walks the VC-inherited court-judgement menus (menu_event_NN_juicio) in order via $g_juicio.

- **Hooks:** `strig:165`, `strig:166`, `strig:167`, `strig:168`, `strig:169`, `strig:170`, `strig:171`, `strig:172`
- **Scripts:** `change_troop_health`, `change_player_party_morale`
- **Menus:** `menu_event_01`, `menu_event_02`, `menu_event_03`, `menu_event_23`, `menu_event_30`, `menu_event_101`, `menu_event_102`, `menu_event_103`, `menu_event_01_juicio`
- **Slots:** `troop:7`, `troop:8`, `party:500`
- **Globals:** `g_lyx_last_random_event`, `g_juicio`, `player_is_king`, `kurkelet`, `freelancer_state`, `g_camp_mode`, `g_empieza_asedio`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis strig:166: guard block + renown>330 + random pick of menu_event_01/23/24/26/02/03/07`, `dis strig:165: 11 minor incidents with change_troop_health / morale / gold`, `dis strig:172: $player_is_king gate, $g_juicio sequence through menu_event_0N_juicio`, `texts menu:event_01 'A bard composed a song about your noble deeds.', menu:event_101 'young nobles wish to join you... more pay'`, `98 menu_event_* menus in awoiaf; vc has only event_siege_* and event_NN_juicio`
- **Overlaps:** `acw.historical_event_calendar`, `ad457.travel_random_events`, `awoiaf.canon_story_event_timeline`, `sw.random_town_ambushes`, `vc.random_events_and_judgments`

<a id="awoiafwhite-walker-invasion"></a>
### White Walker invasion waves and the War for the Dawn — awoiaf (`awoiaf.white_walker_invasion`)

**What it does:** On the chosen day an undead army spawns beyond the Wall, followed by further waves near northern villages over the next days. The horde raids and burns villages; when every White Walker party is destroyed the invasion ends and an R'hllor 'War for the Dawn' questline offers rewards. Captured wights are handled as special prisoners.

**How it works:** trig:41 (check 168h, one-shot): day >= $whitewalker_invasion_day and not disabled -> spawn_around_party p_village_70 pt_whitewalkers_1, $whitewalkers_invaded=1, menu_white_walkers_invade. trig:42-45 then spawn pt_whitewalkers_2/3/5/6 around p_village_11/5/70 on later checks. strig:194 (10h) drives fac_whitewalkers parties (strig:195 is the same raid AI for fac_deserters, not part of this feature): target villages, village_set_state raid, notification menu if the player's fief. strig:7 (48h) counts parties of the 6 templates; when 0 sets $whitewalkers_invaded=2 and start_map_conversation trp_quest_fireborn_warrior_new (R'hllor 'war for the dawn' dialogs, dlg:1108-1113). Auto-resolved fights (script game_event_simulate_battle, menu_total_defeat) route undead through party_add_party_prisoners_wights / party_prisoners_add_party_companions_wights (wights are converted rather than kept as ordinary prisoners).

- **Hooks:** `trig:41:cond`, `trig:42:cond`, `trig:43:cond`, `trig:44:cond`, `trig:45:cond`, `strig:7`, `strig:194`
- **Scripts:** `village_set_state`, `add_notification_menu`, `party_add_party_prisoners_wights`, `party_prisoners_add_party_companions_wights`
- **Menus:** `menu_white_walkers_invade`, `menu_set_up_white_walker_invasion`, `menu_war_for_the_dawn`
- **Globals:** `whitewalkers_invaded`, `whitewalker_invasion_day`, `whitewalker_invasion_off`, `pt_whitewalkers_1`, `pt_whitewalkers_2`, `pt_whitewalkers_3`, `pt_whitewalkers_5`, `pt_whitewalkers_6`
- **Module-specific resources:** pt: pt_whitewalkers_1, pt_whitewalkers_2, pt_whitewalkers_3, pt_whitewalkers_4, pt_whitewalkers_5, pt_whitewalkers_6; faction: fac_whitewalkers; troop: trp_quest_fireborn_warrior_new
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis trig:41: spawn_around_party p_village_70 pt_whitewalkers_1; $whitewalkers_invaded=1; jump_to_menu white_walkers_invade`, `dis trig:42-45: further waves pt_whitewalkers_2/3/5/6`, `dis strig:7: all 6 templates counted; 0 left -> $whitewalkers_invaded=2 + start_map_conversation trp_quest_fireborn_warrior_new`, `dis strig:194: fac_whitewalkers parties raid villages (village_set_state 1, notification)`

<a id="cblinvasion-date-options"></a>
### Dark Knights invasion: 100/250/500-day options — cbl (`cbl.invasion_date_options`)

**What it does:** The 'when does the Dark Knights invasion start' preference gains fixed choices of 100, 250 or 500 days after the start, and the 'unknown date' option now draws from up to ~540 days instead of ~200.

**How it works:** menu:set_invasion adds options 100days/250days/500days writing $setting_invasion_time = 2400/6000/12000 hours, shows the matching label, and opt:unknown uses store_random_in_range 1..13000 (base 1..4800). The hourly invasion trigger reads $setting_invasion_time unchanged.

- **Hooks:** `menu:set_invasion`
- **Menus:** `menu_set_invasion`
- **Globals:** `$setting_invasion_time`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Overlaps:** `acw.play_as_ruler_start`, `ad457.royal_and_lord_sandbox_start`, `awoiaf.campaign_setup_options`, `laigle.story_start_missions`, `tld.in_game_strategy_options`

<a id="laigleweather-seasons"></a>
### Persistent seasonal weather and rain greatcoats — laigle (`laigle.weather_seasons`)

**What it does:** The world has a running day-of-year and season; every hour the sky is re-rolled (clear / cloudy / overcast with light or heavy fog), with rain chance depending on season and clouds. Battles and scenes then use that weather, and in heavy rain line troops swap their coats for greatcoats.

**How it works:** strig:100 (24h) advances $year_day and sets $season; strig:101 (1h) calls check_weather (179 stmts): per season, random 0-10 picks $clouds 0/1/2 with set_global_cloud_amount 0/25/75 and set_global_haze_amount 10/25/45/90 ($fog), then $rain from a cloud-dependent roll. ti_before_mission_start triggers in lead_charge and 10 other templates (sieges, town/village/castle visits) call set_rain (type 2 = snow when $season 3, else rain; strength 40-100). In lead_charge/t4, rain+overcast with $cold_uniforms 0 calls change_uniforms_rain (troop_remove_item/troop_add_item coat->greatcoat on ~25 regular troops) and clear weather calls change_uniforms_clear.

- **Hooks:** `strig:100`, `strig:101`, `mst:lead_charge/t4:conseq`, `mst:castle_attack_walls_ladder/t24:conseq`, `mst:town_center/t5:conseq`, `mst:village_center/t7:conseq`
- **Scripts:** `check_weather`, `change_uniforms_rain`, `change_uniforms_clear`
- **Mission templates:** `mst_lead_charge`, `mst_besiege_inner_battle_castle`, `mst_besiege_inner_battle_town_center`, `mst_castle_attack_walls_belfry`, `mst_castle_attack_walls_defenders_sally`, `mst_castle_attack_walls_ladder`, `mst_castle_visit`, `mst_town_center`, `mst_village_attack_bandits`, `mst_village_center`, `mst_village_raid`
- **Globals:** `season`, `year_day`, `rain`, `fog`, `clouds`, `cold_uniforms`
- **Module-specific resources:** item: itm_french_greatcoat_line, itm_french_greatcoat_gren, itm_british_greatcoat_line
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis laigle check_weather`, `dis laigle strig:100`, `global laigle season: writers start_game_0 options + strig:100, 12 template readers`, `dis laigle mst:lead_charge/t4:conseq`
- **Overlaps:** `acan.seasonal_light_fog_weather`, `be.campaign_weather_battle_atmosphere`, `nw.battle_weather_generator`, `tld.battle_condition_modifiers`, `tld.day_night_proficiency_shift`, `vc.seasons_scene_lighting`

<a id="nwbattle-weather-generator"></a>
### Random battle weather and time of day — nw (`nw.battle_weather_generator`)

**What it does:** Each NW map rolls weather and time: time of day, rain/snow strength, cloud cover and fog distance/colour, so the same field can be fought at dawn in fog or at noon in rain.

**How it works:** multiplayer_generate_weather (138 stmts) is called from multiplayer_mm_before_mission_start_common (also used by mst_tutorial, i.e. single player) and initialize_all_scene_prop_slots: it picks a day time (scene_set_day_time), set_rain(type, strength), set_global_cloud_amount and set_fog_distance($g_fog_distance, $g_fog_colour) from per-map settings and random rolls.

- **Hooks:** `mst:tutorial/t14:conseq`, `mst:multiplayer_cm/t3:conseq`
- **Scripts:** `multiplayer_generate_weather`, `multiplayer_mm_before_mission_start_common`
- **Mission templates:** `mst_tutorial`, `mst_multiplayer_dm`, `mst_multiplayer_tdm`, `mst_multiplayer_hq`, `mst_multiplayer_cf`, `mst_multiplayer_sg`, `mst_multiplayer_bt`, `mst_multiplayer_cb`, `mst_multiplayer_duel`, `mst_multiplayer_kh`, `mst_multiplayer_br`
- **Globals:** `g_fog_distance`, `g_fog_colour`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `explain nw multiplayer_generate_weather: callers incl. multiplayer_mm_before_mission_start_common; roots include mst:tutorial`, `dis nw multiplayer_generate_weather: scene_set_day_time, set_rain, set_global_cloud_amount, set_fog_distance`
- **Overlaps:** `acan.seasonal_light_fog_weather`, `be.campaign_weather_battle_atmosphere`, `laigle.weather_seasons`, `tld.battle_condition_modifiers`, `tld.day_night_proficiency_shift`, `vc.seasons_scene_lighting`

<a id="perisnorebels-and-mercenary-bands"></a>
### Scheduled rebel armies and unemployed-mercenary warbands — perisno (`perisno.rebels_and_mercenary_bands`)

**What it does:** Pretenders' rebels, a named peasant outlaw leader, a desert raider and a lord of mercenaries periodically gather armies on the map, with news messages, and unemployed mercenaries form 'Rogue Knight' bands.

**How it works:** strig:116 (every 67h) runs spawn_rebels (572 stmts), spawning rebel parties per kingdom (factions_rebels_kingdom_N_pretender globals) plus cf_et_spawn_teyva; messages say 'Nibor Hood has gathered an army...' and 'Teyva the Desert Scourge ... forms an army'. strig:115 (every 31h) runs spawn_outlaw_mercenary_warband (298 stmts) building parties like pt_rogue_knight_1 and pt_mercenaries and the message 'Several ... failed to find employers'. Both use cf_spawning_script_template.

- **Hooks:** `strig:116`, `strig:115`
- **Scripts:** `spawn_rebels`, `spawn_outlaw_mercenary_warband`, `cf_spawning_script_template`, `cf_et_spawn_teyva`
- **Slots:** `faction:40`, `party_template:6`, `party_template:400`, `party:74`
- **Globals:** `factions_rebels_kingdom_1_pretender`, `spontanen_meut`, `nibor`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `explain perisno spawn_rebels: sole caller strig:116 (every 67h); writes factions_rebels_kingdom_*_pretender globals; text 'Nibor Hood has gathered an army...'`, `explain perisno spawn_outlaw_mercenary_warband: sole caller strig:115 (every 31h); pt refs pt_rogue_knight_1, pt_mercenaries; text 'Several {s14} failed to find employers'`, `explain perisno cf_spawning_script_template: 53 callers, party_ai 60% party_spawn 40%`

<a id="popai-minor-order-generation"></a>
### Procedurally generated minor knighthood orders that settle in AI fiefs — pop (`pop.ai_minor_order_generation`)

**What it does:** Rarely (5% every 13 days) a new minor knighthood order is founded in an AI lord's castle: it gets a random colour/animal name, a randomly assembled knightly equipment set, diplomatic relations seeded from the host kingdom, and the host lord becomes affiliated. Orders whose last chapterhouse was lost can re-found after the first year once the player is above level 30.

**How it works:** strig:128 (312h, 5%): pick a random castle/town with no chapter (party slot 289 = 0), not under siege (slot 54 = -1), owned by a regular lord; generate_minor_order finds an unused minor-order faction (65-71) whose chapter troop (faction slot 68) is not placed, calls generate_minor_order_knight (949 stmts: builds a knight troop's inventory from pools of knightly helmets/armour/shields/horses via pop_add_item_to_list, troop_add_random_item_if_missing, gives a colour+animal name, saves via copy_complete_troop) and sets relations to the host faction 90 and to others = host's relation +-30. Then party slot 289 = chapter troop, lord troop slots 158/159/160 record affiliation, notification menu_notification_order_founded. strig:127 (384h, 5%, day>365, player level>30) re-founds a major order (fac_dragon_knights..fac_player_knights) that has no chapter in a random kingdom's free fief. Chapters spawn order patrols via spawn_errant_knights (strig:82).

- **Hooks:** `strig:127`, `strig:128`, `menu:camp_vader/opt:camp_vader_randorder1:conseq`
- **Scripts:** `generate_minor_order`, `generate_minor_order_knight`, `pop_add_item_to_list`, `troop_add_random_item_if_missing`, `troop_add_random_item`, `randomize_color`, `copy_complete_troop`, `cf_item_is_knightly`, `spawn_errant_knights`
- **Menus:** `menu_notification_order_founded`
- **Presentations:** `prsnt_order_founded`
- **Slots:** `party:289`, `party:54`, `party:7`, `faction:68`, `faction:22`, `faction:23`, `troop:158`, `troop:159`, `troop:160`, `troop:172`
- **Globals:** `pop_list_num_items`
- **Module-specific resources:** faction: minor order factions (ids 65-71); troop: trp_temp_array_a, trp_rav_knight, trp_custom_knight_1_save; item: ~360 knightly items referenced
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis strig:128 and strig:127 (head)`, `dis generate_minor_order (full)`, `explain generate_minor_order_knight: 949 stmts, inventory 53%, 368 item refs`

<a id="popraid-refugees"></a>
### Refugees and looters spawned by raids and conquests — pop (`pop.raid_refugees`)

**What it does:** When a village is raided or a castle/town falls, groups of refugees (some guarded), desperate looters and occasionally Red Brotherhood slavers spill out around it, giving the war visible aftermath and rescue/robbery opportunities.

**How it works:** generate_refugees(center, radius) is called from process_village_raids (on raid) and menu:castle_taken. It spawns 0-1 groups (+2 for towns); per group a d150 roll: <30 pt_refugees (cap 9, faction of the center, slot 123 = home), <50 pt_refugees_guarded (cap 11), <100 pt_looters renamed 'Desperate Refugees'/'Rabble'/'Hungry Refugees'/'Angry Peasants' (cap 18), else Red Brotherhood variants (thieves, outlaws, slavers with captive ladies).

- **Hooks:** `menu:castle_taken`, `script:process_village_raids`
- **Scripts:** `generate_refugees`, `process_village_raids`
- **Menus:** `menu_castle_taken`
- **Slots:** `party:123`, `party:0`
- **Module-specific resources:** pt: pt_refugees, pt_refugees_guarded, pt_looters, pt_red_brotherhood; faction: fac_innocents, fac_red_brotherhood
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `dis generate_refugees lines 0-45`, `explain: callers menu:castle_taken, script:process_village_raids`
- **Overlaps:** `acw.prisoner_breakouts_and_refugees`, `vc.prisoner_revolts`

<a id="popunique-signature-heroes"></a>
### Named 'signature' warlords with patrols, repeatable until defeated and dealt with — pop (`pop.unique_signature_heroes`)

**What it does:** Named villains and heroes (Burilgi the Usurper, Oswald de Fleur, Boris the Raven, Meregan/Griffonsword, Kodan/Ironsword, Shalavan, Syla, Wolfbode, Eyegrim, the Dread Legion, Three Seers, Inquisitor Rasmus...) appear with big unique armies announced by 'word reaches you' messages. Some field satellite patrols. After the player defeats and captures the leader he can execute him, ransom his armour, or exile him -- which permanently prevents that army from returning. Tavern/lord news points the player at them.

**How it works:** unique_hero_can_spawn(hero, template) is the shared gate used by 68 call sites: returns reg34=1 only if party_template slot 6 (retired) is 0, no party of that template exists, the hero is not the player's prisoner and not in the player's party; on success heals the hero to 100%. spawn_signature (strig:17 weekly, also from lord news dlg:1491 and manhunter dlg:214) rolls and spawns the named party at a fixed spawn point with message + sound. spawn_signature_patrols (strig:17) keeps up to 4 patrol parties around each living signature party (party_template slot 7 = home), patrolling radius 1. signature_repression_for_death_and_defeat (dlg:3681-3688 prisoner_chat_sig3) sets party_template slot 6 = 1 for the matching template (retire/exile/death), ending its respawns. game_event_simulate_battle also sets slot 6 on AI defeat in some cases.

- **Hooks:** `strig:17`, `dlg:1491:dlga_lord_tell_news:lord_pretalk:cond`, `dlg:214:dlga_manhunter_talk_b1:manhunter_talk_b2:conseq`, `dlg:3681:dlga_prisoner_chat_sig3:prisoner_chat_threat_retire:conseq`, `dlg:3688:dlga_prisoner_chat_sig3:close_window.4:conseq`
- **Scripts:** `unique_hero_can_spawn`, `spawn_signature`, `spawn_signature_patrols`, `signature_repression_for_death_and_defeat`, `sub_scenario_signature_information`, `cf_spawn_azi_death_cult`, `game_event_simulate_battle`
- **Dialogs:** `dlg:3681`, `dlg:3682`, `dlg:3683`, `dlg:3685`, `dlg:3688`, `dlg:1491`, `dlg:214`
- **Slots:** `party_template:6`, `party_template:7`
- **Module-specific resources:** pt: pt_burilgi_the_usurper, pt_oswald, pt_boristheraven, pt_griffonsword, pt_ironsword, pt_shalavan, pt_syla_uzas, pt_eyegrim(_patrol), pt_dread_legion(_patrol), pt_wolfbode(_patrol), pt_three_seers(_patrol), pt_inquisitor_rasmus_patrol; troop: trp_hero_* (19 signature heroes); sound: snd_bellchant, snd_drums
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis unique_hero_can_spawn (full 35 stmts)`, `slot pop party_template 6: writer signature_repression_for_death_and_defeat (19 sets), readers unique_hero_can_spawn/generate_mercenary_company`, `dis spawn_signature_patrols head`, `explain spawn_signature: 'Word reaches you...' strings`
- **Overlaps:** `acw.partisan_bands`, `cbl.regional_bandit_spawn_points`, `pop.lord_party_deserters`, `pop.minor_faction_repression_meter`, `pop.renegade_and_merc_warbands`

<a id="swrandom-town-ambushes"></a>
### Configurable random ambushes and assassins on landing in towns — sw (`sw.random_town_ambushes`)

**What it does:** When the player walks into a town there is a chance (set in the camp configuration menu, in %) that an assassin spawns at a nearby entry point and attacks, or that an enemy-faction squad raids the town as you land, turning the visit into a street fight.

**How it works:** mst:town_center/t7 (cond, 1.5 s after entry, once) rolls d100 against $random_scene_assassination -> init_town_fight + cf_setup_random_scene_assassination (spawn_agent of a random assassin troop 328-333 at entry point 30-39 if >1 m from player, team 3 hostile to player team, charge order), or against $random_scene_battles -> cf_setup_random_scene_encounter (enemy-faction squad, 'As you land your ship...' alert dialog, battle music). Percentages are edited in menu:camp_configuration.

- **Hooks:** `mst:town_center/t7:cond`, `menu:camp_configuration`
- **Scripts:** `cf_setup_random_scene_assassination`, `cf_setup_random_scene_encounter`, `init_town_fight`, `start_town_fight`
- **Menus:** `menu_camp_configuration`
- **Mission templates:** `mst_town_center`
- **Globals:** `random_scene_assassination`, `random_scene_battles`, `g_assassin`, `g_init_fight`, `g_started_battle_random_by_enemy_faction`
- **Module-specific resources:** troop: trp 328-333 (assassins)
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis sw mst:town_center/t7:cond`, `dis sw cf_setup_random_scene_assassination`, `global sw random_scene_assassination: writer menu:camp_configuration`
- **Overlaps:** `acw.historical_event_calendar`, `ad457.travel_random_events`, `awoiaf.canon_story_event_timeline`, `awoiaf.random_travel_events`, `vc.random_events_and_judgments`

<a id="tldfaction-defeat-redistribution-last-stand"></a>
### Faction defeat, territory redistribution, lord defection and last stand — tld (`tld.faction_defeat_redistribution_last_stand`)

**What it does:** When a faction's capital falls or its Strength hits zero it is destroyed: all its parties disband, its towns are handed to whichever enemy is strongest relative to distance (or to an active besieger), and each lord may escape to the nearest friendly faction of a compatible race, bringing +500 Strength with him. Shortly before, a dying faction calls every lord home to defend the capital. Side-wide victory is detected when only one alignment remains.

**How it works:** strig:55 (12 h): for each live faction, if capital (faction slot 154) is no longer its own or is flagged, set slot 21 = 1 (dead) and: detach/remove its parties; for each center, give to besieger (party slot 54) or to the enemy faction maximising min(strength,7000)*1000/distance (get_tld_distance), then cf_reinforce_party x5; 30% of its lords pick the closest allied faction by capital distance with race rules (troop_set_faction, +500 to that faction's slot 153, 'X managed to escape...'); free the player's hero prisoners of that faction; notification menu; update theatres. When strength < 1 it first sets slot 183, and strig:60 (3 h) runs last_faction_stand which orders every lord party (ai state 7) back to the capital. At the end strig:55 checks whether all live factions share one side (faction slot 158) and fires the ending conversation missions.

- **Hooks:** `strig:55`, `strig:60`
- **Scripts:** `give_center_to_faction`, `destroy_center`, `delete_volunteers_party`, `lift_siege`, `cf_reinforce_party`, `get_tld_distance`, `last_faction_stand`, `last_faction_stand_aux`, `last_faction_stand_aux_ai`, `update_active_theaters`, `cf_reinforce_next_theater`, `add_notification_menu`, `send_on_conversation_mission`
- **Dialogs:** `dlg:239:dlga_companion_faction_dying:close_window:conseq`
- **Slots:** `faction:21`, `faction:154`, `faction:158`, `faction:183`, `faction:153`, `party:54`, `party:258`, `troop:2`, `troop:10`
- **Globals:** `g_recalculate_ais`, `g_tld_conversations_done`, `g_tld_convo_subject`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis tld strig:55 (335 stmts) shown above: give_center_to_faction weighting, troop_set_faction + 153 += 500, display_log_message '{s2} was defeated!'`, `dis tld strig:60 + last_faction_stand_aux_ai (party_set_ai_state 7 to capital)`, `slot tld faction 183 writers strig:55/60`
- **Overlaps:** `acan.civil_war_usurpation_restoration`, `ad457.landless_faction_cleanup`, `ad457.town_rebellions_secession`, `vc.faction_restoration_and_adventurers`

<a id="vcrandom-events-and-judgments"></a>
### Random camp/siege events and lord's-court judgment cases — vc (`vc.random_events_and_judgments`)

**What it does:** Two families of choice events: siege-camp events (rats in the provisions, dysentery, sabotage of supplies, poisoned water, deserters - mostly avoidable by building sanitation/blockade) and, for fief holders, court cases where the player judges villagers' disputes (a disputed calf, theft, a missionary and a holy tree, fake relics, tax refusal, riots) with consequences for relations, money, prosperity and religion.

**How it works:** strig:155-158 (every 24-60h) roll siege-camp events (menu_event_siege_01..08) while the player besieges, keyed to the siege-plan state (sanitation, blockade). Judgments: menu:town offers event_01_juicio..event_22_juicio and event_juicio_end when $lord_event_possible/$event_oneuse allow (reset by strig:106); options test the center's religion (slot 234) and $g_player_faith, can change the Christian share (slot 235), and call change_player_relation_with_center, change_center_prosperity, change_player_honor, change_troop_renown, change_player_relation_with_faction, troop_add_gold, change_player_party_morale; menu_random_juice_events / prsnt_random_event_solution show outcomes.

- **Hooks:** `strig:155`, `strig:156`, `strig:157`, `strig:158`, `menu:town`, `menu:random_juice_events`
- **Scripts:** `change_player_relation_with_center`, `change_center_prosperity`, `change_player_honor`, `change_troop_renown`, `troop_add_gold`, `change_player_party_morale`
- **Menus:** `menu_event_siege_01`, `menu_event_01_juicio`, `menu_event_juicio_end`, `menu_random_juice_events`, `menu_riots_02`, `menu_nobody_want_paytax`
- **Presentations:** `prsnt_random_event_solution`, `prsnt_random_event_normalsolution`
- **Slots:** `party:234`, `party:235`, `party:53`
- **Globals:** `event_oneuse`, `lord_event_possible`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `sqlite refs: menu_event_siege_* <- strig:155..158; menu_event_01_juicio <- menu:town`, `sqlite texts: event_siege_01 'rats in the provisions', event_siege_02 'dysentery... could have been prevented', event_01_juicio 'Two farmers... ownership of a calf'`, `sqlite globals event_oneuse/lord_event_possible: r menu:town, w game_start/menu:town/strig:106`, `82 distinct menu:event_* records (sqlite texts)`, `sqlite slots/calls for menu:event_*_juicio: party 234 eq x11, 235 get/set; calls change_player_relation_with_center, change_center_prosperity, change_player_honor ...`
- **Overlaps:** `acw.historical_event_calendar`, `ad457.travel_random_events`, `awoiaf.canon_story_event_timeline`, `awoiaf.random_travel_events`, `sw.random_town_ambushes`

<a id="acwfast-travel-network"></a>
### Paid fast travel by ship, train or stagecoach between linked towns — acw (`acw.fast_travel_network`)

**What it does:** Towns have ticket sellers for ship, railroad and stagecoach. The player pays a per-head fare to a linked destination (only towns at peace with them), and is carried there by a transport party on the map; stagecoach is refused with 15+ men.

**How it works:** game_start -> initialize_fast_travel_routes (575 calls) -> set_fast_travel_route_between_centers(a,b,type) writes reciprocal destination slots 441-460 and type slots 461-480 (1 stagecoach, 2 train, 3 ship) on both towns. menu:town 'Talk to the fast travel agent' -> menu:fast_travel options open map conversations with per-town ticket-seller troops (party slots 481 = ship ticket seller, 482 = stagecoach agent, 485 = train ticket seller; trp_town_N_ft_ship/train/stagecoach) [corrected 2026-10-13: slot 483 is slot_town_arena_master, not fast travel]. dlg fast_travel_2 lists each destination (cond: cf_check_town_at_peace_with_faction_of_destination, cf_fast_travel_check_travel_type_match, not under siege - party slot 54). Fare reg63 x party size. On confirm (dlg:3012) spawns pt_fast_travel_ship/train/party next to the town with ai target = destination, sets $g_player_is_captive=1 (player is carried), camera follows it, rest_for_hours 168; strig:102 (hourly) jumps to menu:fast_travel_end when within 1 unit -> party_relocate_near_party player to destination, remove transport party.

- **Hooks:** `menu:town/opt:town_fast_travel:conseq`, `menu:fast_travel`, `dlg:3012:dlga_fast_travel_5:close_window:conseq`, `strig:102`, `menu:fast_travel_end`
- **Scripts:** `initialize_fast_travel_routes`, `set_fast_travel_route_between_centers`, `cf_fast_travel_check_travel_type_match`, `fast_travel_ship_train_wagon_text`, `cf_check_town_at_peace_with_faction_of_destination`, `cf_town_has_fast_travel_ship`, `cf_town_has_fast_travel_train`, `cf_town_has_fast_travel_wagon`
- **Menus:** `menu_fast_travel`, `menu_fast_travel_start`, `menu_fast_travel_end`
- **Dialogs:** `dlga_fast_travel_1..5`
- **Slots:** `party:440`, `party:441-460`, `party:461-480`, `party:481`, `party:482`, `party:485`
- **Globals:** `travel_destination`, `travel_type`, `fast_travel_guys`, `fast_travel_active`, `g_player_is_captive`
- **Module-specific resources:** pt: pt_fast_travel_ship, pt_fast_travel_train, pt_fast_travel_party; troop: trp_town_1_ft_ship_ticket_seller.., trp_town_1_ft_train_ticket_seller.., trp_town_1_ft_stagecoach..
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis acw set_fast_travel_route_between_centers / initialize_fast_travel_routes`, `dis acw dlg:3012 / strig:102 / menu:fast_travel_end`, `menu:fast_travel/opt:visit_stagecoach_denied:cond (party size >= 15)`, `changelog: fast-travel connection fixes for Savannah/Vicksburg corroborate the route table`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_constants.py 885-947 fast-travel slot names`, `slot acw party 483 -> arena master dialog/menu only; slot acw party 485 -> menu:fast_travel visit_train_station + cf_town_has_fast_travel_train`
- **Overlaps:** `vc.port_passage_travel`
- **Notes:** Oddity: dlg:3012 computes a bitmask in party slot 440 (val_or 1/2/4) and then immediately overwrites it with 7 on both towns.

<a id="biculture-lord-map-icons"></a>
### Lord parties use their faction's own map icon — bi (`bi.culture_lord_map_icons`)

**What it does:** Every lord's party on the world map is drawn with an icon for its people - a Roman army column for Rome and the four Roman provinces, Germanic nobles, Dacian nobles, Parthian cataphracts, Numidian riders, Sarmatian horse archers, Bosporan foot and so on - instead of Native's one generic lord icon. Emperor Marcus Aurelius's party also spawns with 300 Praetorians.

**How it works:** create_kingdom_hero_party (Native script, modified): after spawning pt_kingdom_hero_party and setting the banner icon, a try/else chain on the lord's faction (store_troop_faction; faction ids 36-62) calls party_set_icon with one of 13 BI map icons (map_roman_army, germanic_noble, dacian_noble, eastern_cataphract, numider, celtic_noble, british_foot, sarmatian_cavalry, icon_beduin, sarmatian_horsearcher, bosporan_foot, judean_noble, eastern_archer). The icons are rows in map_icons.txt whose meshes live in Resource/BI_Map_Icons.brf. Separately, if the lord is troop 667 (trp_kingdom_1_lord, Emperor Marcus Aurelius) the party gets 300 trp_roman_n_praetorian on creation.

- **Hooks:** `script:create_kingdom_hero_party`
- **Scripts:** `create_kingdom_hero_party`
- **Module-specific resources:** map_icon: map_roman_army, germanic_noble, dacian_noble, eastern_cataphract, numider, celtic_noble, british_foot, sarmatian_cavalry, icon_beduin, sarmatian_horsearcher, bosporan_foot, judean_noble, eastern_archer; brf: BI_Map_Icons; troop: trp_roman_n_praetorian
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `dis bi create_kingdom_hero_party @31-111: faction try-chain -> party_set_icon`, `map_icons.txt rows for all 13 icons (e.g. line 36 map_roman_army, line 60 germanic_noble)`, `all 13 icon meshes found in Resource/BI_Map_Icons.brf (scratch brfnames.py over the loaded BRFs)`, `sqlite names: bi troop 667 = trp_kingdom_1_lord (troops.txt: Emperor_Marcus_Aurelius)`
- **Overlaps:** `acw.army_size_map_icons`, `acw.besieged_map_smoke_and_caravan_spacing`, `cbl.map_icons_by_party_type_and_ships`

<a id="cblexpanded-calradia-map"></a>
### Enlarged Calradia map (Native kept, borderlands added) — cbl (`cbl.expanded_calradia_map`)

**What it does:** The campaign map keeps Native Calradia almost untouched (175 of Native's 180 towns/castles/villages sit at the same coordinates) and adds new lands around it: 23 more towns, 54 more castles and 136 more villages, for 45/102/246 in total. The playable area grows from -180..180 x -145..145 to -230..305 x -240..205 (about 2.2x Native's land).

**How it works:** Pure data plus centre setup. map.txt keeps Native's mesh topology (20,791 vertices, 41,387 faces) but 10,654 faces are recoded and 1,589 vertices moved (new coasts, mountains, 1,259 'bridge' (code 7) faces used as sea lanes). module.ini widens map_min/max_x/y. parties.txt inserts the new towns after p_town_22 (towns idx 22..66, numbered 1-22 and 24-46; there is no town 23), castles after them (67..168) and villages after them (169..414), so every Native range loop (p_town_1..p_castle_1, p_village_1..p_salt_mine, etc.) covers the new centres automatically. Every per-centre parallel array is extended in the same order: 9 per-town troop arrays (seneschal, arena master, armorer, weaponsmith, tavernkeeper, merchant, horse merchant, mayor, master craftsman) at 45 each, 102 castle seneschals, 246 village elders, 8 per-town scene arrays at 45 each, 102 castle scene triples and 246 village scenes. game_start's offset loops (store_sub town p_town_1 -> scn_town_1_center + offset, trp_town_1_mayor + offset, ...) then wire scenes and NPCs for all centres. Villages are bound to the nearest castle (one each) and then the nearest town by distance, so no per-village list is needed. All new-centre map icons are Native ones (town, town_desert, castle_a..d, village_a/c, ...).

- **Hooks:** `script:game_start`
- **Scripts:** `game_start`, `initialize_trade_routes`, `initialize_economic_information`, `initialize_town_arena_info`, `give_center_to_faction_aux`, `give_center_to_lord`
- **Slots:** `party:0`, `party:10`, `party:11`, `party:12`, `party:13`, `party:14`, `party:16`, `party:17`, `party:18`, `party:20`, `party:21`, `party:22`, `party:23`, `party:24`, `party:25`, `party:60`, `party:62`, `party:120`
- **Module-specific resources:** file: map.txt, module.ini (map_min_x -230, map_max_x 305, map_min_y -240, map_max_y 205), SceneObj (490 new-centre .sco, 114.7 MB); party: p_town_24..p_town_46, p_castle_49..p_castle_102, p_village_111..p_village_246; scene: scn_town_24_*..scn_town_46_*, scn_castle_49_*..scn_castle_102_*, scn_village_111..scn_village_246
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `parties.txt parse: cbl towns idx 22..66 (45, numbered 1-22,24-46), castles 67..168 (102), villages 169..414 (246), each contiguous`, `point-in-triangle test: all 393 cbl centres on land in cbl map.txt; Native bridges test as code 7 (method check)`, `script:game_start @441-520 offset loops (scn_town_1_center+off, trp_town_1_mayor+off, scn_castle_1_exterior+3*off, scn_village_1+off, trp_village_1_elder+off); @413-440 distance-based village binding (party slot 120)`
- **Overlaps:** `cbl.new_centre_economy_and_arena_wiring`, `cbl.twelve_borderland_kingdoms`, `cbl.v352_later_version_changes`

<a id="cblmap-icons-by-party-type-and-ships"></a>
### Map icons by party type, ship icon on sea lanes — cbl (`cbl.map_icons_by_party_type_and_ships`)

**What it does:** On the world map, bandits, caravans, patrols, farmers, lords and other parties get type-specific figures (axeman, grey knight, mule, peasant, khergit rider, woman, flag-bearer), and any party - including the player - switches to a ship icon while crossing the sea lanes.

**How it works:** strig:62 (interval 0 = every map tick): the player's icon becomes 'ship' when party_get_current_terrain p_main_party == 7; then try_for_parties over every party whose template is between pt_looters and pt_kingdom_1_reinforcements_a (plus Diplomacy recruiter/spouse/gift caravan) maps a hard-coded template list to an icon and calls party_set_icon (ship on terrain 7, type icon elsewhere). cbl's map uses terrain code 7 ('bridge') for 1,259 sea-lane faces, which parties can cross; setup_random_scene sends battles on code 7 to mst_ship_battle (shared with the base module).

- **Hooks:** `strig:62`
- **Globals:** `$g_player_party_icon`
- **Module-specific resources:** icon: icon_ship, icon_axeman, icon_gray_knight, icon_woman, icon_peasant, icon_mule, icon_khergit, icon_vaegir_knight, icon_flagbearer_a; pt: pt_looters..pt_kingdom_1_reinforcements_a range, 40+ named templates
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `dis cbl setup_random_scene @336-347: terrain 7 -> mst_ship_battle`
- **Overlaps:** `acw.army_size_map_icons`, `acw.besieged_map_smoke_and_caravan_spacing`, `bi.culture_lord_map_icons`

<a id="cblv352-later-version-changes"></a>
### Calradia Borderlands V3.52: what the later version adds — cbl (`cbl.v352_later_version_changes`)

**What it does:** The later V3.52 build (compiled tables only, no map) grows to 58 towns, 127 castles, 316 villages and 18 new kingdoms (adds Czaloca, Quetzal, Vhonylor, Trapegea, Tigrayand, New-Zendar), relocates several cbl regions, rewrites the random war/peace roll, and gives regions their own town pictures and burnt-village icons.

**How it works:** Script delta vs cbl: 826 identical, 32 modified, 1 new (randomly_start_war_peace_new_ooold = the old version). randomly_start_war_peace_new (206 stmts, 22% similar) now walks every kingdom pair once with a 50% roll instead of picking a random start offset. set_town_picture and process_village_raids use hard-coded centre sub-ranges per region (e.g. p_town_31..35 + p_town_46 -> mesh_pic_town_jap; p_village_301..312 -> village_zim icons), which also fixes cbl and the base module's 'every village after p_village_91 burns like a desert village' quirk. game_get_party_prisoner_limit x20 (cbl x10); coloured morale/honour messages; party_calculate_loot rewritten. Tables: 641 parties, 71 factions, 2,487 troops, 1,430 scenes. 58 spawn/forest points added (forest_smalla..bigab around x -230..-310) for the western continent.

- **Hooks:** `script:randomly_start_war_peace_new`, `script:set_town_picture`, `script:process_village_raids`
- **Scripts:** `randomly_start_war_peace_new`, `set_town_picture`, `process_village_raids`, `game_get_party_prisoner_limit`, `party_calculate_loot`, `change_player_party_morale`, `change_player_honor`
- **Slots:** `faction:21`
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `diff cbl352 cbl: identical 826, modified 32, only in cbl352 1`, `parties parse cbl352: towns 22..79 (58), castles 80..206 (127), villages 207..522 (316)`, `cbl352land.py: point-in-triangle of cbl352 centres on cbl map.txt`
- **Overlaps:** `cbl.expanded_calradia_map`, `cbl.new_centre_economy_and_arena_wiring`, `cbl.twelve_borderland_kingdoms`

<a id="laigleterrain-party-speed"></a>
### Terrain-dependent party speed on the map — laigle (`laigle.terrain_party_speed`)

**What it does:** Parties move slower in desert and snow and faster on water.

**How it works:** game_get_party_speed_multiplier (engine-called, 0 script callers): 100% base; terrain 5 (desert) 70%, 4 (snow) 60%, 7 (bridge) 20%, 0 (water) 150%; set_trigger_result.

- **Hooks:** `script:game_get_party_speed_multiplier`
- **Scripts:** `game_get_party_speed_multiplier`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `dis laigle game_get_party_speed_multiplier`, `callers laigle game_get_party_speed_multiplier -> 0 (engine hook)`

<a id="oa1860purchasable-ship"></a>
### Buy a ship in port towns — oa1860 (`oa1860.purchasable_ship`)

**What it does:** In nine coastal towns the player can pay 5000 to put to sea; the party is moved onto nearby water and travels as a ship.

**How it works:** menu:town/opt:sail_from_port: Native's cheat-only option, re-gated to 9 specific towns (this_or_next chain) and routed through menu_confirm_ship: if gold >= 5000, remove gold, $g_player_icon_state = 2, party_set_flags pf_is_ship (512), map_get_water_position_around_position, party_set_position, change_screen_return.

- **Hooks:** `menu:town/opt:sail_from_port:cond`, `menu:confirm_ship/opt:confirm:conseq`
- **Menus:** `menu_confirm_ship`
- **Globals:** `g_player_icon_state`
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `dis oa1860 menu:confirm_ship/opt:confirm:conseq`
- **Overlaps:** `acan.ports_ferries_sea_trade`, `laigle.naval_boarding_battle`, `sw.starship_upgrades`, `vc.deck_sea_battles`, `vc.port_passage_travel`, `vc.sea_ai_traffic`, `vc.sea_travel_map`, `vc.ship_fleet_ownership`

<a id="swstarship-upgrades"></a>
### Owned starship with buyable component upgrades that grant party bonuses — sw (`sw.starship_upgrades`)

**What it does:** The player buys a ship at a shipyard (stock depends on which faction's yard), then upgrades seven systems - drive, scanner, combat computer, troop capacity, medical bay, prisoner capacity, trade computer. The drive level speeds up map travel; the other levels add directly to the matching party skills (tactics, spotting, surgery/wound treatment, prisoner management, trade, ...). Ships can be sold back.

**How it works:** menu:shipyard calls setup_spaceship_slots (651 stmts: 31 ship models stored as 'ship model' parties 248-278 with stats in party slots 250-271: name, description, price, base speed, max level per component) and rolls 7 offers from faction-specific ranges by $g_encountered_party. prsnt_starship buys a ship (reset_starship_slots_for_troop writes troop 0 slots 300 = ship model, 301-316 = current/max level per component). prsnt_ship_details shows current/max and get_component_upgrade_price per step; get_ship_sell_value prices a resale. Effects ride two engine callbacks: game_get_party_speed_multiplier (player party speed = ship base speed (party slot 255) x (100 + 10 x drive level)%, x3.33 at night / x2 by day, clamped 0-600; also patrols and fixed-speed templates) and game_get_skill_modifier_for_troop (adds component levels to skills 11, 15, 9, 0 ... for the ship owner).

- **Hooks:** `menu:shipyard`, `menu:shipyard/opt:shipyard_1:conseq`, `prsnt:starship/t0`, `prsnt:starship/t1`, `prsnt:ship_details/t0`, `prsnt:ship_details/t1`, `script:game_get_party_speed_multiplier`, `script:game_get_skill_modifier_for_troop`
- **Scripts:** `setup_spaceship_slots`, `reset_starship_slots_for_troop`, `get_component_upgrade_price`, `get_ship_sell_value`, `game_get_party_speed_multiplier`, `game_get_skill_modifier_for_troop`
- **Menus:** `menu_shipyard`
- **Presentations:** `prsnt_starship`, `prsnt_ship_details`
- **Slots:** `party:250-271 (ship model stats)`, `troop:300-316 (owner's ship + component levels)`
- **Globals:** `g_ship_choice_1`, `g_ship_choice_2`, `g_ship_choice_3`, `g_ship_choice_4`, `g_ship_choice_5`, `g_ship_choice_6`, `g_ship_choice_7`, `g_ship_type`, `g_ship_icon`, `g_ship_price`
- **Module-specific resources:** party: p 248-278 (ship model dummy parties); mesh: ship pictures/icons
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `explain sw setup_spaceship_slots: callers menu:shipyard, game_start; party slots 250-271`, `dis sw game_get_party_speed_multiplier: troop 0 slot 300/315, party slot 255`, `dis sw game_get_skill_modifier_for_troop: troop slots 301-313 added to skills`, `sqlite slots sw troop 300-316 -> reset_starship_slots_for_troop, prsnt ship_details, get_ship_sell_value`, `qstr 'Upgrade Details: Base Speed, Drive, Scanner, Combat Computer, Troop Capacity, Medical Bay, Prisoner Capacity, Trade Computer'`
- **Overlaps:** `acan.ports_ferries_sea_trade`, `laigle.naval_boarding_battle`, `oa1860.purchasable_ship`, `vc.deck_sea_battles`, `vc.port_passage_travel`, `vc.sea_ai_traffic`, `vc.sea_travel_map`, `vc.ship_fleet_ownership`

<a id="tldregion-tracking-and-battle-scenes"></a>
### Named map regions: entry messages, region-picked battle scenes and landmarks — tld (`tld.region_tracking_and_battle_scenes`)

**What it does:** The world map is divided into named regions; crossing a border prints 'You are entering X, territory of Y'. The current region, terrain and nearby landmark decide which hand-made battle scene a field battle uses and which faction's 'ambient' purse is active; visiting landmarks counts toward the Well-travelled trait.

**How it works:** get_region_of_pos1 (354 stmts) tests the party position against hard-coded coordinate boxes and returns a region id; strig:12 (every 0.5 h) compares it with $current_player_region and logs entry/exit (region names are strings 2014+ / 2712+); region_get_faction resolves the holder. jump_to_random_scene(region, terrain, landmark) (357 stmts) picks a scene for battles, camp and ambushes; cf_store_landmark_description_in_s17 / get_close_landmark describe the spot.

- **Hooks:** `strig:12`, `script:start_current_battle`
- **Scripts:** `get_region_of_party`, `get_region_of_pos1`, `region_get_faction`, `jump_to_random_scene`, `get_close_landmark`, `cf_store_landmark_description_in_s17`, `store_terrain_condition_to_s17_s18`
- **Slots:** `party:300`
- **Globals:** `current_player_region`, `current_player_terrain`, `current_player_landmark`
- **Module-specific resources:** string: region name strings 2014+, 2712+
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis tld strig:12 (region change messages)`, `explain tld jump_to_random_scene (7 callers incl. start_current_battle, camp, ambush)`, `auto report: get_region_of_pos1 354 stmts positions 95%`
- **Overlaps:** `acw.custom_battle_historical_scenarios`, `cbl.custom_field_battle_scenes`, `laigle.size_aware_battlefields`

<a id="tldwilderness-encounters-hide-animal-ambush"></a>
### Hide from enemies and wilderness animal ambushes — tld (`tld.wilderness_encounters_hide_animal_ambush`)

**What it does:** When a hostile party forces an encounter, a small party (8 or fewer) or one with good Persuasion-renamed stealth skill can choose to hide and slip away. While travelling through wild regions the party may be ambushed by animals: a scout with high Spotting or Persuasion-type skill may avoid it (earning XP), otherwise the player and companions fight the beasts in a small separate battle.

**How it works:** menu:simple_encounter/opt:encounter_hide appears for non-friendly, no-escape encounters when cf_can_hide_from_enemy passes (party size <= 8, or <= 10 + 4*skill 7) and leads to menu_hide. trig:23 (8 h, $tld_option_animal_ambushes, player level >= 7) in listed wild regions, away from centers: roll 0-200 (0-400 with the Animal-fighter trait); avoided if roll <= party size*3 + 2*spotting(skill 13) [+3*skill 7], giving XP to the best scout; else jump_to_menu menu_animal_ambush (once per counter) -> mission 52 mst_animal_ambush with only heroes; success/fail menus.

- **Hooks:** `trig:23:conseq`, `menu:simple_encounter/opt:encounter_hide:cond`
- **Scripts:** `cf_can_hide_from_enemy`, `get_max_skill_of_player_party`, `jump_to_random_scene`
- **Menus:** `menu:hide`, `menu:animal_ambush`, `menu:animal_ambush_success`, `menu:animal_ambush_fail`
- **Mission templates:** `mst_animal_ambush`
- **Slots:** `troop:26 (trp_traits)`
- **Globals:** `tld_option_animal_ambushes`, `creature_ambush_counter`, `current_player_region`
- **Module-specific resources:** mt: mst_animal_ambush
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis tld cf_can_hide_from_enemy / menu:hide (party size <= 8, skl_persuasion*4+10)`, `dis tld trig:23:conseq (region list, avoidance roll, jump_to_menu menu_animal_ambush)`, `text tld 'Avoided_animal_ambush_via_Wildcraft.'`
- **Overlaps:** `acw.hunting`, `awoiaf.hunting_herds`

<a id="vcport-passage-travel"></a>
### Paid passage between ports — vc (`vc.port_passage_travel`)

**What it does:** A port chief can sell the player passage to another port: the party is carried by a transporter ship and auto-enters the destination town on arrival. Marshals with a whole army are refused unless a big enough passenger ship is in port.

**How it works:** Port chief dialogs (dlga_port_chief3 'I want to travel to another port' -> port_chief_travel_5 'Follow me!') read $travel_town/$current_town, move p_transporter and jump to menu_start_sea_travel (dlg:68 conseq). game_get_party_speed_multiplier gives p_transporter a fixed speed 15 while $travel_town is a town. strig:132 (every 0.7h) watches $travel_town / $auto_enter_town (and party slot 297 = linked jetty) and calls map_sea_ai_2; on arrival the player is placed in the town. Ferries (menu_ferry_encounter, p_ferry_*) are the short-hop equivalent across firths/rivers for a fee ({reg7}).

- **Hooks:** `strig:132`, `dlg:56:dlga_port_chief3:port_chief_travel:cond`, `dlg:68:dlga_port_chief_travel_5:close_window:conseq`, `menu:ferry_encounter/opt:continue:conseq`
- **Scripts:** `game_get_party_speed_multiplier`, `map_sea_ai_2`, `get_closest_port`
- **Menus:** `menu_ferry_encounter`, `menu_start_sea_travel`
- **Dialogs:** `dlga_port_chief_travel`, `dlga_port_chief_travel_5`
- **Slots:** `party:297`, `party:296`
- **Globals:** `travel_town`, `auto_enter_town`, `g_player_is_captive`
- **Module-specific resources:** party: p_transporter, p_ferry_1a.., p_jetty_1..p_jetty_5
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `sqlite refs strig:132: p_transporter, $travel_town, $auto_enter_town, party slot 297`, `dis vc game_get_party_speed_multiplier stmt 94-97: p_transporter speed 15 when $travel_town > p_castle_1`, `texts dlg 56/57: 'I want to travel to another port.' / refusal for a marshal and his whole army`, `slot vc party 296: menu:ferry_encounter writes it`, `sqlite refs dlg:68 conseq: menu_start_sea_travel, p_transporter x6; globals read travel_town/current_town`
- **Overlaps:** `acan.ports_ferries_sea_trade`, `acw.fast_travel_network`, `laigle.naval_boarding_battle`, `oa1860.purchasable_ship`, `sw.starship_upgrades`, `vc.deck_sea_battles`, `vc.sea_ai_traffic`, `vc.sea_travel_map`, `vc.ship_fleet_ownership`

<a id="acanports-ferries-sea-trade"></a>
### Ports, landings and ferries as map parties, sea trade routes, embarking armies and an overseas merchant fleet — acan (`acan.ports_ferries_sea_trade`)

**What it does:** At game start every coastal town gets a port party on the water, plus landings and ferries, so armies can embark from a port (minimum crew 15) and sail. Sea trade routes link coastal towns, and AI parties use sea lanes. Through a dialog the player can also send a merchant fleet to India for profit.

**How it works:** add_ports_jetty_and_ferry_system (game_start) spawns 'Port of {s1}' / 'Landing near {s2}' parties at get_next_water_position near each coastal centre ($g_number_ports; party slots 39/40/41 link port and centre). initialize_sea_trade_routes / set_sea_trade_route_between_centers build up to 15 routes per town, and cf_select_most_profitable_coastal_town_at_peace_with_faction_in_trade_route picks targets. menu:town_port 'Set sail from port' and menu:landet_ships_encounter call switch_to_water_consequences / switch_to_land_consequences (party icon, $players_ship, warn about leaving caravans behind). game_get_party_speed_multiplier (210 stmts) handles land/water moves with $wind_power. map_sea_ai_1-3 (strig:90 daily and others) send AI parties by sea (get_closest_port via party_set_ai_state), and bandits_go_to_lairs moves pirates/bandits. calculate_sea_caravan_cost prices the India fleet (dlg:10215).

- **Hooks:** `script:game_start`, `menu:town_port/opt:sail_from_port:conseq`, `menu:landet_ships_encounter`, `strig:90`, `strig:93`, `dlg:10215:dlga_india_send_caravan_plyr`
- **Scripts:** `add_ports_jetty_and_ferry_system`, `initialize_sea_trade_routes`, `set_sea_trade_route_between_centers`, `cf_select_most_profitable_coastal_town_at_peace_with_faction_in_trade_route`, `switch_to_water_consequences`, `switch_to_land_consequences`, `get_closest_port`, `cf_is_port_party`, `map_sea_ai_1`, `map_sea_ai_2`, `map_sea_ai_3`, `get_next_water_position`, `get_next_land_position`, `game_get_party_speed_multiplier`, `calculate_sea_caravan_cost`, `bandits_go_to_lairs`
- **Menus:** `menu_town_port`, `menu_landet_ships_encounter`, `menu_landet_ships_encounter_as_marshal`
- **Mission templates:** `mst_ship_battle`
- **Slots:** `party:39`, `party:40`, `party:41`, `party:68`
- **Globals:** `g_number_ports`, `players_ship`, `wind_power`, `cattle_in_ship`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `explain acan add_ports_jetty_and_ferry_system: 'Port of Ostia', 'Port of Piraeus', 'Port of {s1}', 'Landing near {s2}'`, `explain acan switch_to_water_consequences: menu:town_port 'Set sail from port.(Minimum crew 15 men)'`
- **Overlaps:** `laigle.naval_boarding_battle`, `oa1860.purchasable_ship`, `sw.starship_upgrades`, `vc.deck_sea_battles`, `vc.port_passage_travel`, `vc.sea_ai_traffic`, `vc.sea_travel_map`, `vc.ship_fleet_ownership`

<a id="laiglenaval-boarding-battle"></a>
### Sea encounters fought as boarding actions — laigle (`laigle.naval_boarding_battle`)

**What it does:** Meeting a party on water opens a naval encounter; attacking ('Close for boarding!') loads a ship-deck scene where generic sailors and marines represent each side, and the loser of the fight loses half of their real party.

**How it works:** game_event_party_encounter (129 stmts) jumps to menu_naval_encounter when party_get_current_terrain == 0. encounter_attack: set_jump_mission mst_naval_battle on scn_naval_battle1, set_visitors trp_regular_sailor / trp_regular_marine at entries 1-4 with half of each side's fit count. mst_naval_battle (lead_charge-like, with PBOD) ends via create_naval_casualties: removes half of the losing party's companions at random into p_enemy_casualties/p_player_casualties.

- **Hooks:** `script:game_event_party_encounter`, `menu:naval_encounter/opt:encounter_attack:conseq`, `mst:naval_battle/t1:conseq`, `mst:naval_battle/t8:conseq`
- **Scripts:** `create_naval_casualties`, `game_event_party_encounter`
- **Menus:** `menu_naval_encounter`
- **Mission templates:** `mst_naval_battle`
- **Module-specific resources:** scene: scn_naval_battle1; troop: trp_regular_sailor, trp_regular_marine
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `grep laigle mst_naval_battle|menu_naval_encounter`, `dis laigle menu:naval_encounter/opt:encounter_attack:conseq`, `dis laigle create_naval_casualties`
- **Overlaps:** `acan.ports_ferries_sea_trade`, `oa1860.purchasable_ship`, `sw.starship_upgrades`, `vc.deck_sea_battles`, `vc.port_passage_travel`, `vc.sea_ai_traffic`, `vc.sea_travel_map`, `vc.ship_fleet_ownership`

<a id="vcdeck-sea-battles"></a>
### Ship-to-ship deck battles with boarding — vc (`vc.deck_sea_battles`)

**What it does:** When the player's fleet meets an enemy at sea the fight happens on real ships on water: each side's ships are spawned as moving scene-prop hulls, agents ride on deck, ships sail, rock in the waves, collide, run aground and board each other. Weather (storm scenes, wind prop) and wave shaders are set per battle.

**How it works:** menu:simple_encounter/opt:encounter_attack:conseq (and join_battle) branch on party slot 296=1 (player at sea): prepare_party_ships_for_team copies the player's ship array to a team, randomize_ships_for_team_war_party / _civilian (called through a local variable) give the enemy ships, setup_random_sea_scene picks scn_sea_battle* and set_jump_mission(mst_sea_battle). mst_sea_battle has 140 trigger blocks / 2491 stmts: spawn_ship (spawns spr_dyn_ship_* parts for 9 hull types), put_the_klabautermann_into_the_ships (635 stmts, per-frame ship physics: movement, rocking, collision, docking, aground), ship_ai (196, AI helmsman), boarding_for_ship3 / ai_decide_stop_boarding / calculate_dockingpoint/meetingpoint_to_pos1, give_agent_position_on_ship + keep_crew_on_board, set_wave_shader/get_wave_properties (waves), prsnt_naval_ui. mst_ships_attack_port (menu:port_attack lead_attack) is the coastal-assault variant used on the port scenes.

- **Hooks:** `menu:simple_encounter/opt:encounter_attack:conseq`, `menu:join_battle/opt:join_attack:conseq`, `menu:port_attack/opt:lead_attack:conseq`, `mst:sea_battle`
- **Scripts:** `prepare_party_ships_for_team`, `randomize_ships_for_team`, `randomize_ships_for_team_war_party`, `randomize_ships_for_team_civilian`, `setup_random_sea_scene`, `spawn_ship`, `put_the_klabautermann_into_the_ships`, `ship_ai`, `check_aground`, `check_collision`, `calculate_movement_to_pos1`, `calculate_rocking_to_pos1`, `calculate_dockingpoint_to_pos1`, `calculate_meetingpoint_to_pos1`, `boarding_for_ship3`, `ai_decide_stop_boarding`, `give_agent_position_on_ship`, `keep_crew_on_board`, `make_crew`, `set_crew_free`, `check_player_ship`, `check_ship_team`, `set_wave_shader`, `get_wave_properties`, `set_wave_timer`, `spawn_sea_battle_visitors`
- **Menus:** `menu_port_attack`, `menu_ship_capture`
- **Presentations:** `prsnt_naval_ui`
- **Mission templates:** `mst_sea_battle`, `mst_ships_attack_port`, `mst_quick_battle_sea_battle`, `mst_quick_battle_coastal_battle`, `mst_camp_on_sea`
- **Slots:** `party:296`, `party:301-337`, `scene_prop:6-48 (ship part state)`, `agent:28`, `agent:38`, `agent:44`
- **Globals:** `player_team_in_sea_battle`, `startup_battle_size`, `team_0_ship_counter`, `team_1_ship_counter`, `Amplitude_x`, `Amplitude_y`, `wavespeed_y`, `wind_strenght`, `wave_timer`
- **Module-specific resources:** scene: scn_sea_battle, scn_sea_battle_storm, scn_sea_battle_fjord_1, scn_sea_battle_cliffs_1, scn_sea_battle_hills_1, scn_town_3_coastal; spr: spr_dyn_ship_* (136 records: 14 parts x busse/byrding/curragh/karvi/knorr/skeid/skeid2...), spr_wind, spr_barrier_ship; shader: VC wave shader (set_wave_shader)
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis vc menu:simple_encounter/opt:encounter_attack:conseq stmts 24-57: slot 296 branch -> set_jump_mission mst_sea_battle`, `sqlite blocks: mst:sea_battle = 140 blocks / 2491 stmts; callees include spawn_ship, put_the_klabautermann_into_the_ships, set_wave_shader`, `sqlite refs: mst_ships_attack_port launched only by menu:port_attack/opt:lead_attack`
- **Overlaps:** `acan.ports_ferries_sea_trade`, `laigle.naval_boarding_battle`, `oa1860.purchasable_ship`, `sw.starship_upgrades`, `vc.port_passage_travel`, `vc.sea_ai_traffic`, `vc.sea_travel_map`, `vc.ship_fleet_ownership`

<a id="vcsea-ai-traffic"></a>
### AI sea traffic: traders, fishers, slavers, travellers and sea kings sailing between ports — vc (`vc.sea_ai_traffic`)

**What it does:** The seas are populated by AI ships - fishing boats, slave traders, passenger ships, walrus hunters and Norse sea-king fleets - that embark at ports, sail to destination ports and land; raiders can land at coastal landing points. Pools are refilled over time and parties stranded on land are cleaned up.

**How it works:** trig:9 (every 10.2h) calls refill_sea_party_template (spawns pt_fisher_ship / pt_slave_trader_ship / pt_traveller_ship up to $pin_limit, marks party slot 296=1 at sea, slot 123 home) and refill_sea_king_partys (pt_sea_king_norweg / _danish). map_sea_ai_1 (strig:131, 33.3h) assigns destinations; map_sea_ai_2 (strig:132, 0.7h) moves embarked parties between ports, embarks/disembarks them (pt_landet_ships / pt_port) and handles player auto-travel; map_sea_ai_3 (strig:79, 3h) handles landed raiders/priest/pagan/routed parties. AI-party travel state lives in party slots 331-334 (target port, phase, timers) plus 297 (port link) and 73. remove_sea_parties_on_land (strig:131) deletes sea-only parties that end up ashore. Spawn points carry party slot 44 (sea zone 1/2) used by spawn_lairs / sea spawning.

- **Hooks:** `trig:9:conseq`, `strig:131`, `strig:132`, `strig:79`
- **Scripts:** `refill_sea_party_template`, `refill_sea_king_partys`, `map_sea_ai_1`, `map_sea_ai_2`, `map_sea_ai_3`, `remove_sea_parties_on_land`, `get_closest_port`, `store_random_eastern_port_to_reg0`, `store_random_western_port_to_reg0`, `cf_party_is_eastern_port`, `cf_party_is_western_port`
- **Slots:** `party:296`, `party:297`, `party:331`, `party:332`, `party:333`, `party:334`, `party:73`, `party:123`, `party:44`
- **Globals:** `pin_limit`, `pin_party_template`, `vc_debug_mode`
- **Module-specific resources:** pt: pt_fisher_ship, pt_slave_trader_ship, pt_traveller_ship, pt_walrus_hunter, pt_sea_king_norweg, pt_sea_king_danish, pt_landet_ships, pt_port
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `sqlite calls: trig:9 -> refill_sea_party_template/refill_sea_king_partys; strig:131 -> map_sea_ai_1/remove_sea_parties_on_land; strig:132 -> map_sea_ai_2; strig:79 -> map_sea_ai_3`, `sqlite refs: map_sea_ai_2 references pt_fisher_ship, pt_slave_trader_ship, pt_traveller_ship, pt_walrus_hunter, pt_sea_king_*, pt_landet_ships, pt_port`, `sqlite slots: map_sea_ai_* read/write party 296/297/331-334`
- **Overlaps:** `acan.ports_ferries_sea_trade`, `laigle.naval_boarding_battle`, `oa1860.purchasable_ship`, `sw.starship_upgrades`, `vc.deck_sea_battles`, `vc.port_passage_travel`, `vc.sea_travel_map`, `vc.ship_fleet_ownership`

<a id="vcsea-travel-map"></a>
### Sailing on the campaign map (land/sea switching, wind-and-navigation speed) — vc (`vc.sea_travel_map`)

**What it does:** Parties can leave the coast and move across open water on the world map. When a party enters a water face it becomes a fleet (ship icon, at-sea flag); its speed then depends on the Navigation skill, ship types, crew and the current wind ($beaufort). Reaching land near a port/jetty/landing point disembarks it again.

**How it works:** Engine callback script:game_get_party_speed_multiplier (187 stmts, VC-new) reads party_get_current_terrain; terrain 0/7/8 (water) -> calls calculate_party_speed_water (navigation skill skl_navigation, crew/ship types, $beaufort wind) and, for AI parties, sets party slot 296=1 + party flag 512 and calls update_party_icon (ship icon). Back on land it clears slot 296/flag 512. For the player, sea travel is gated by slot 296: if the player is on water without being 'at sea' it snaps him to the nearest ferry/jetty (p_ferry_1a..p_jetty_1) or port town (party slot 241 = coastal) and sets $auto_enter_town, else get_next_land_position. Embark/disembark run switch_to_water_consequences / switch_to_land_consequences from menus (landet_ships_encounter, landing_point_encounter, port_encounter, ferry_encounter, player_lair_menus embark). It also clamps the player inside the map bounds. strig:136 (every 2.1h, only while slot 296=1) applies at-sea morale loss at night or with low Navigation and storm damage to ships.

- **Hooks:** `script:game_get_party_speed_multiplier`, `strig:136`, `menu:landet_ships_encounter`, `menu:landing_point_encounter`, `menu:port_encounter`, `menu:ferry_encounter`, `menu:player_lair_menus/opt:embarkre:conseq`
- **Scripts:** `game_get_party_speed_multiplier`, `calculate_party_speed_water`, `get_next_water_position`, `get_next_land_position`, `switch_to_water_consequences`, `switch_to_land_consequences`, `get_closest_port`, `cf_is_port_party`, `update_party_icon`, `add_jetty_system`, `add_jetty_system_2`
- **Menus:** `menu_landet_ships_encounter`, `menu_landing_point_encounter`, `menu_port_encounter`, `menu_ferry_encounter`
- **Slots:** `party:296`, `party:241`, `party:297`
- **Globals:** `beaufort`, `auto_enter_town`, `travel_town`, `cattle_in_ship`, `followers_on`
- **Module-specific resources:** party: p_ferry_1a..p_jetty_1 (ferries/jetties), p_landing_point, p_transporter, p_the_fleet; skill: skl_navigation (repurposed skill: +5% sea speed per level); map: VC map.txt with navigable sea faces
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis vc game_get_party_speed_multiplier: terrain 0/7/8 branch -> calculate_party_speed_water, slot 296 set/clear, party_set_flags 512, update_party_icon`, `slot vc party 296: 211 accesses in 149 blocks (game_start, map_sea_ai_2, switch_to_* scripts, encounter menus)`, `dis vc strig:136: requires party_slot_eq p_main_party 296 1; morale -1 at night / low navigation; storm damage scales with $beaufort`, `skills.txt: skl_navigation 'Party map speed on sea is increased by 5% per skill level'`
- **Overlaps:** `acan.ports_ferries_sea_trade`, `laigle.naval_boarding_battle`, `oa1860.purchasable_ship`, `sw.starship_upgrades`, `vc.deck_sea_battles`, `vc.port_passage_travel`, `vc.sea_ai_traffic`, `vc.ship_fleet_ownership`

<a id="vcship-fleet-ownership"></a>
### Owning a fleet: ship types, crew capacity, hull damage, buying/building/capturing ships — vc (`vc.ship_fleet_ownership`)

**What it does:** The player owns up to 7 ships, each with a type (Busse, Skeid, Karvi, Snekkja, Knorr, Byrding and more), a name, a hull condition and build quality/material. Ship capacity limits how many troops you can carry to sea; storms can damage or sink ships and excess crew is lost. Ships are bought or built (choosing wood) from port chiefs, captured after sea battles and managed in a ship screen.

**How it works:** Ships are a struct array on the party: slots 301-307 = ship type, 311-317 = name (pseudo-troop or string), 321-327 = hull condition, 331-337 = encoded modifiers (decoded by decode_value / encode_values_to_reg0). get_ship_properties(type) returns the stat table in reg1..reg7 (speed, ?, ?, price, hit points, crew capacity reg6, name string). cf_crew_fit_in_ships sums reg6 over slots 301-307 and fails if party size exceeds it (used by embark menus/dialogs). strig:136 rolls storm damage per ship by $beaufort, compacts the array when a ship sinks, and removes random non-hero troops that no longer fit. Port chief dialogs (port_chief_buy_ship, port_chief_build_ship_main_*) and prsnt_vc_submenu_ships / prsnt_vc_submenu_ships_customize sell/customise ships; menu_ship_capture adds an enemy ship after victory; give_ships_to_towns (trig:6) seeds port inventories; calculate_ship_value prices them; merge_ships_from_party_to_party / give_player_ships_from_party_to_party move ships between the player and landed-ship parties.

- **Hooks:** `strig:136`, `trig:6:conseq`, `menu:ship_capture`, `dlg:42:dlga_port_chief3:port_chief_buy_ship:cond`, `dlg:92:dlga_port_chief_build_ship_main_4:port_chief_build_ship_main_5:cond`, `prsnt:vc_submenu_ships`
- **Scripts:** `get_ship_properties`, `cf_crew_fit_in_ships`, `calculate_ship_value`, `give_ships_to_towns`, `merge_ships_from_party_to_party`, `give_player_ships_from_party_to_party`, `condition_check_merging_ships`, `print_party_ship_info_to_s0`, `decode_value`, `encode_values_to_reg0`, `set_ship_materials`
- **Menus:** `menu_ship_capture`, `menu_primer_barco`
- **Presentations:** `prsnt_vc_submenu_ships`, `prsnt_vc_submenu_ships_customize`
- **Dialogs:** `dlga_port_chief_buy_ship`, `dlga_port_chief_build_ship_main_4`, `dlga_port_chief_info_main_1`
- **Slots:** `party:301-307`, `party:311-317`, `party:321-327`, `party:331-337`, `party:300`, `party:302`
- **Globals:** `beaufort`, `build_ship_type`, `build_ship_wood`, `build_ship_days`, `ship_menu`, `ship_menu_state`, `ship_menu_current_ship_price`, `ship_management_explained`
- **Module-specific resources:** string: str_busse, str_skeid, str_karvi, str_snekkja, str_knorr, str_byrding; troop: trp_pseudo_troop_01..trp_pseudo_troop_end (ship names)
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis vc get_ship_properties: per-type reg1..reg7 table, reg7=str_busse/skeid/karvi/snekkja/knorr/byrding`, `dis vc cf_crew_fit_in_ships: sums reg6 over party slots 301..307 vs party_get_num_companions`, `dis vc strig:136: slots 301+10/+20/+30 struct, storm sinking compacts the array, removes troops if crew no longer fits`, `texts: dlg 42 'I want to buy a ship.', dlg 53-55 port chief explains ship types/wood/wind`
- **Overlaps:** `acan.ports_ferries_sea_trade`, `laigle.naval_boarding_battle`, `oa1860.purchasable_ship`, `sw.starship_upgrades`, `vc.deck_sea_battles`, `vc.port_passage_travel`, `vc.sea_ai_traffic`, `vc.sea_travel_map`

<a id="acantroop-detail-and-upgrade-trees"></a>
### Troop detail screen and per-culture upgrade-tree presentations — acan (`acan.troop_detail_and_upgrade_trees`)

**What it does:** A troop-detail screen shows a unit's stats, attributes, weapons and inventory with tooltips, and 16 upgrade-tree screens draw each culture's troop lines.

**How it works:** prsnt:troop_detail uses troop_detail_layout / _draw_troop / _stats / _inventory / _inventory_tooltip (troop_detail_stats 215 stmts: 100% shape with ad457, 99% with VC). prsnt:upgrade_tree_1..14 use prsnt_upgrade_tree_troop_and_name / _lines / _ready / _switch (91% shape with AWOIAF's).

- **Hooks:** `prsnt:troop_detail/t0`, `prsnt:upgrade_tree_1/t0`
- **Scripts:** `troop_detail_layout`, `troop_detail_draw_troop`, `troop_detail_stats`, `troop_detail_inventory`, `troop_detail_inventory_tooltip`, `prsnt_upgrade_tree_troop_and_name`, `prsnt_upgrade_tree_lines`, `prsnt_upgrade_tree_ready`, `prsnt_upgrade_tree_switch`
- **Presentations:** `prsnt_troop_detail`, `prsnt_upgrade_tree_1`, `prsnt_upgrade_tree_14`
- **Globals:** `checkbox_show_item_details_val`, `temp_troop`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `explain acan prsnt:troop_detail/t0: texts 'Level', 'Hit Points', 'Atributes'`, `compare troop_detail_stats: ad457 100%, vc 99%, awoiaf 97%`, `compare prsnt_upgrade_tree_ready: awoiaf 91%`
- **Overlaps:** `be.faction_troop_tree_viewer`, `bi.world_map_presentation`, `vc.camp_and_report_screens`

<a id="acwarmy-size-map-icons"></a>
### Lord map icons that grow into an 'army' icon above 150 men — acw (`acw.army_size_map_icons`)

**What it does:** On the world map a general's party shows a flag-bearer icon in his side's colours, and switches to a larger 'army' icon once it has more than 150 men, so big armies are recognisable at a glance.

**How it works:** script check_party_icon(party): for active lord parties (slot_party_type = spt_kingdom_hero_party) with men: Union (or player's king-start Union faction) -> icon_union_army if > 150 men else icon_flagbearer_union; Confederate -> icon_confed_army / icon_flagbearer_confed; Plains tribes -> icon_khergit_horseman_b. Called whenever size or allegiance can change: create_kingdom_hero_party, hire_men_to_kingdom_hero_party, game_event_simulate_battle, party_set_ai_state, change_troop_faction, process_alarms.

- **Hooks:** `script:create_kingdom_hero_party`, `script:hire_men_to_kingdom_hero_party`, `script:game_event_simulate_battle`, `script:party_set_ai_state`, `script:change_troop_faction`, `script:process_alarms`
- **Scripts:** `check_party_icon`
- **Slots:** `party:0`
- **Globals:** `king_start`, `king_faction`
- **Module-specific resources:** map_icon: icon_union_army, icon_confed_army, icon_flagbearer_union, icon_flagbearer_confed, icon_khergit_horseman_b
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `callers acw check_party_icon -> 6 call sites`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_scripts.py 51433-51489 check_party_icon`
- **Overlaps:** `acw.besieged_map_smoke_and_caravan_spacing`, `bi.culture_lord_map_icons`, `cbl.map_icons_by_party_type_and_ships`

<a id="acwcustom-battle-historical-scenarios"></a>
### Custom battles: 35 historical battlefields, 38 playable generals, per-battle time of day and fog — acw (`acw.custom_battle_historical_scenarios`)

**What it does:** The custom-battle screen offers 35 historical battlefields (Manassas to Bentonville) and 38 historical generals with biographies; each battlefield loads at its historical time of day, some with fog, with artillery, colour-guards, war cry and bugles active.

**How it works:** Native presentation game_custom_battle_designer (module_presentations.py ~380-810) extended: combo label of quick_battle_troops (trp_quick_battle_troop_1 .. trp_quick_battle_troops_end, 38 entries) with biography text; scene combo filled from civil_war_custom_battle_scenes_begin = scn_civ_custom_battle_manassas .. scn_civ_custom_battle_end (35 scenes) and other scene categories (random, camp, town, castle, village, plus a debug 'Scene ID' browser of all edit scenes). mst quick_battle_battle/quick_battle_siege append custom_flagbearers + common_vader_deathcam_custom + custom_battle_ai (madsci_custom_ai: the enemy team is ordered to charge about 1-2 s in, unless $g_quick_battle_game_type = 1) + custom_weather (madsci_weather: scene_set_day_time / set_fog_distance per scene in its condition block) + cannons_custom + EG3_Warcry_custom + bugle_calls_custom.

- **Hooks:** `prsnt:game_custom_battle_designer`, `mst:quick_battle_battle/t21:cond`, `mst:quick_battle_siege/t24:cond`
- **Presentations:** `prsnt_game_custom_battle_designer`
- **Mission templates:** `mst_quick_battle_battle`, `mst_quick_battle_siege`
- **Slots:** `faction:41`, `faction:42`, `faction:47`, `faction:48`
- **Globals:** `g_quick_battle_troop`, `g_quick_battle_map`, `g_custom_battle_designer_scene_type`, `madsci_timer`
- **Module-specific resources:** scene: scn_civ_custom_battle_manassas .. scn_civ_custom_battle_end (35); troop: trp_quick_battle_troop_1 .. (38)
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_presentations.py 397-482 (combo_label of 38 generals, create_combo_button_overlay with the listbox alternative commented out), 801-807 civil_war_custom_battle_scenes loop`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_mission_templates.py 3196-3320 madsci_weather; 10388 and 10485 quick-battle bundle lists`, `grep set_fog_distance --mods acw --kinds mst -> quick_battle_battle/t21:cond, quick_battle_siege/t24:cond`, `FAQ.txt: without WSE2 not all custom battle maps are reachable (no scroll bar)`
- **Overlaps:** `cbl.custom_field_battle_scenes`, `laigle.size_aware_battlefields`, `tld.region_tracking_and_battle_scenes`

<a id="acwdeath-camera"></a>
### Death camera with automatic hold orders when the player falls (MadVader deathcam) — acw (`acw.death_camera`)

**What it does:** Four seconds after the player is knocked out in battle, the view lifts 2.5 m above his body and becomes a free-flying camera (mouse to look, movement keys to fly, X/E for height). At the same moment the player's own formations are dissolved and his team is ordered to stand ground and fire at will (in custom battles: charge).

**How it works:** Tuples in module_mission_templates.py 55-330 ('## MadVader deathcam begin/end'): common_init_deathcam (resets $pop_camera_* incl. ACW's added rotation bounds and menu-fix variables), common_start_deathcam (0, 4 s, once, main_hero_fallen: mission_cam_set_mode 1 at pos47 = body + 250 cm; formation_end for infantry/archers/cavalry; team_give_order everyone stand_ground + fire_at_will), common_move_deathcam (key_x/key_e/gk_move_*), common_deathcam_menu_fix and common_rotate_deathcam (mouse rotation with clamped pitch; the 4.0 'gyroscope' fixes). Grouped as list `common_vader_deathcam` (custom battles: `common_vader_deathcam_custom`, which orders a charge) and appended to lead_charge, sieges, village raid, bandit fights and scout-camp templates.

- **Hooks:** `mst:lead_charge/t46:conseq`, `mst:lead_charge/t47:conseq`, `mst:lead_charge/t48:cond`, `mst:quick_battle_battle/t14:conseq`, `mst:castle_attack_walls_ladder/t41:conseq`
- **Scripts:** `formation_end`
- **Mission templates:** `mst_lead_charge`, `mst_quick_battle_battle`, `mst_quick_battle_siege`, `mst_castle_attack_walls_ladder`, `mst_castle_attack_walls_belfry`, `mst_castle_attack_walls_defenders_sally`, `mst_village_raid`, `mst_village_attack_bandits`, `mst_destroy_scout_camp`, `mst_besiege_inner_battle_castle`, `mst_besiege_inner_battle_town_center`
- **Globals:** `pop_camera_on`, `pop_camera_rotx`, `pop_camera_roty`, `pop_camera_mouse_center_x`, `pop_camera_mouse_center_y`, `pop_camera_mouse_counter`, `pop_camera_menu_was_open`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `global acw $pop_camera_on -> 22 writer / 44 reader blocks across 11 battle templates`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_mission_templates.py 55-330 '## MadVader deathcam' tuples`, `changelog v4.0: death-cam rotation 'gyroscopic' bug 'sort of fixed' / 'mostly fixed' (10/9/2026)`
- **Overlaps:** `acw.command_all_allies`, `be.aerial_command_view`

<a id="acworder-voice-callouts"></a>
### Spoken / bugled order and group-selection callouts (with engine-native volley/rank orders) — acw (`acw.order_voice_callouts`)

**What it does:** When the player issues any battle order or selects a group, a soldier of the listening group plays a voiced/bugle call (halt, charge, fix bayonets, fire at will, form 1-5 ranks, left/middle/right fire now...). Volley and rank orders themselves come from the engine's Napoleonic-Wars order set, enabled by module.ini use_advanced_formation = 1.

**How it works:** mst:lead_charge/t43 ti_on_order_issued (cond; 3 s debounce via $bugle_timer): only if player is in a Union/Confederate army or king start; maps order id 0-26 (incl. NW-only ids 18 open fire, 19-21 left/middle/right fire now, 22-26 form 1-5 rows) to a (bugle, voice) sound pair and plays them on the first live non-player agent of a listening division (class_is_listening_order). t23 (every 0.05 s) maps group-select keys 29-38 to snd_select_* and plays it likewise. No scripted volley logic exists in ACW: grep team_give_order with ids 15-26 or 'volley' finds nothing; only t34 reads the artillery division's hold-fire order.

- **Hooks:** `mst:lead_charge/t43:cond`, `mst:lead_charge/t23:cond`, `mst:lead_charge/t23:conseq`
- **Globals:** `bugle_timer`, `saved_sound`
- **Module-specific resources:** sound: snd_halt(_voice), snd_charge(_voice), snd_fix_bayonets(_voice), snd_fire_at_will(_voice), snd_left_fire_now_voice, snd_form_1_row..snd_form_5_row, snd_select_*
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis acw mst:lead_charge/t43:cond`, `dis acw mst:lead_charge/t23:cond/conseq`, `module.ini (acw): use_advanced_formation = 1, can_crouch = 0, can_reload_while_moving = 1`, `grep volley --mods acw -> none`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_mission_templates.py 1202-1570 voice_orders / bugle / bugle_timer / bugle_timer_init`
- **Overlaps:** `bi.battle_event_messages`, `nw.fkey_order_tree`, `nw.objective_markers_hud`, `nw.voice_commands`, `sw.battle_start_speeches`

<a id="acwwalkable-party-camp"></a>
### Walk around your own camp (and the enlisted army's camp) — acw (`acw.walkable_party_camp`)

**What it does:** From the camp menu the player can enter a 3D camp scene sized to their party (small <=15, medium <=50, large) populated by their companions and soldiers who wander between camp spots; freelancers can do the same in their lord's camp.

**How it works:** menu:camp/opt:players_camp:conseq picks scn_players_camp_small/_medium/players_camp by party size, set_jump_mission mst_players_camp, modify_visitors_at_site + set_visitor for each party stack (heroes first, then up to 27 visitors round-robin over regular stacks). mst_players_camp t0 every 3 s calls camp_walkers -> set_camp_walker_destination: each non-player agent not at entries 1-4 has a 20% chance to walk to a random entry point 5-28 (agent slot 0). menu:world_map_soldier/opt:enlisted_camp:conseq does the same for the enlisted lord's party.

- **Hooks:** `menu:camp/opt:players_camp:conseq`, `menu:world_map_soldier/opt:enlisted_camp:conseq`, `mst:players_camp/t0:cond`
- **Scripts:** `camp_walkers`, `set_camp_walker_destination`
- **Menus:** `menu_camp`
- **Mission templates:** `mst_players_camp`
- **Slots:** `agent:0`
- **Module-specific resources:** scene: scn_players_camp, scn_players_camp_medium, scn_players_camp_small
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis acw menu:camp/opt:players_camp:conseq`, `dis acw camp_walkers`, `refs acw mt mst_players_camp (2 entry menus)`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_mission_templates.py 12233`
- **Overlaps:** `acan.player_permanent_camps`, `pop.camp_troop_review_drill`, `tld.camp_menu_actions`

<a id="ad457royal-and-lord-sandbox-start"></a>
### Start the game as ruler or vassal of an existing kingdom — ad457 (`ad457.royal_and_lord_sandbox_start`)

**What it does:** At game start the player can choose 'Royal Sandbox' to take over an existing kingdom as its ruler (picking from a kingdom-selection screen), or start as a landed lord, instead of the usual nobody start. The chosen realm's former ruler steps aside, the player gets its fortresses, faith and culture, and the realm keeps its existing alliances and tributaries. Character creation itself uses a one-screen point-buy menu.

**How it works:** menu:start_game_0 options 'Normal Sandbox' -> prsnt_mcc_character_creation (mcc_generate_skill_set 696 stmts, mcc_random_settings, mcc_default_settings) and 'Royal Sandbox' -> prsnt_select_king (t1 event handler) -> player_is_king(kingdom) (612 stmts): moves the old king, sets $g_king_start, $g_player_culture, $g_player_faith, background, activates the player faction (activate_player_faction), hands over centres (give_center_to_lord), creates kingdom hero parties, adjusts right to rule, re-creates tributary/alliance links (dplmc_start_tributary_between_kingdoms, dplmc_start_alliance_between_kingdoms) and re-initialises faction troop types; player_is_lord (169 stmts) does the vassal version. $g_king_start then changes recruitment (hire_men_to_center, cf_reinforce_party, create_kingdom_hero_party use the player's chosen culture) and enables the minister's office dialog.

- **Hooks:** `menu:start_game_0/opt:starting_as_king:conseq`, `menu:start_game_0/opt:continue:conseq`, `prsnt:select_king/t1`, `prsnt:mcc_character_creation/t1`
- **Scripts:** `player_is_king`, `player_is_lord`, `activate_player_faction`, `give_center_to_lord`, `create_kingdom_hero_party`, `change_player_right_to_rule`, `initialize_faction_troop_types`, `mcc_generate_skill_set`, `mcc_random_settings`, `mcc_default_settings`, `set_player_face_according_culture`
- **Menus:** `menu_start_game_0`, `menu_culture_selection`, `menu_religion_selection`
- **Presentations:** `prsnt_select_king`, `prsnt_select_lord`, `prsnt_mcc_character_creation`
- **Slots:** `faction:11`, `faction:10`, `faction:299`, `troop:156`
- **Globals:** `g_king_start`, `g_player_culture`, `g_player_faith`, `background_type`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `refs ad457 prsnt prsnt_select_king: menu:start_game_0/opt:starting_as_king:conseq 'Royal_Sandbox'`, `refs ad457 prsnt prsnt_mcc_character_creation: menu:start_game_0/opt:continue:conseq 'Normal_Sandbox'`, `explain ad457 player_is_king: callees change_troop_faction, activate_player_faction, give_center_to_lord, dplmc_start_tributary/alliance, initialize_faction_troop_types; writes g_king_start, g_player_culture, g_player_faith`, `global ad457 g_king_start: 29 readers incl. hire_men_to_center, cf_reinforce_party, create_kingdom_hero_party, minister office dialogs`
- **Overlaps:** `acw.play_as_ruler_start`, `awoiaf.campaign_setup_options`, `cbl.invasion_date_options`, `laigle.story_start_missions`, `tld.in_game_strategy_options`

<a id="awoiafcampaign-setup-options"></a>
### New-game setup choices (naming canon, static vs sandbox wars, commoner trust, wounds, start continent, White Walker date) — awoiaf (`awoiaf.campaign_setup_options`)

**What it does:** Before play starts the player answers a chain of option menus: book vs TV character names, 'Static Wars' (War of the Five Kings diplomacy locked to canon) vs 'Sandbox', commoner-trust reputation on/off, realistic vs basic wound system, start in Westeros (with main quest line) or Essos, and the day the White Walkers invade (600/750/850/1200).

**How it works:** menu_set_up_game -> menu_set_up_wars (writes $campaign_type = 8 static / 9 sandbox) -> menu_set_up_commoners_trust ($commoners_trust_on) -> menu_set_up_wounds -> menu_set_up_start_location_man/_mouse -> menu_set_up_white_walker_invasion ($whitewalker_invasion_day). Later systems read these globals: strig:52/53/54/55 run only when $campaign_type==9; trig:36-40 and strig:56 only when ==8; trig:41 compares current day to $whitewalker_invasion_day. menu_static_wars_off_menu (from Reports) lets the player switch static->sandbox permanently.

- **Hooks:** `menu:set_up_game`, `menu:set_up_wars`, `menu:reports/opt:reset_static_wars`
- **Menus:** `menu_set_up_game`, `menu_set_up_wars`, `menu_set_up_commoners_trust`, `menu_set_up_wounds`, `menu_set_up_start_location_man`, `menu_set_up_start_location_mouse`, `menu_set_up_white_walker_invasion`, `menu_static_wars_off_menu`
- **Globals:** `campaign_type`, `commoners_trust_on`, `whitewalker_invasion_day`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `global awoiaf campaign_type: writers menu:set_up_wars/opt:static_wars|normal_wars, menu:static_wars_off_menu; readers strig:52-56, strig:64, trig:36-40`, `texts: menu:set_up_wars 'Static wars: Westerosi factions will be locked in diplomacy according to the Wars of the Five Kings... Sandbox...'`, `global awoiaf whitewalker_invasion_day: writers set_up_white_walker_invasion opts day_600..day_1200; reader trig:41:cond`
- **Overlaps:** `acw.play_as_ruler_start`, `ad457.royal_and_lord_sandbox_start`, `cbl.invasion_date_options`, `laigle.story_start_missions`, `tld.in_game_strategy_options`

<a id="awoiafmain-menu-web-links"></a>
### Main-menu web link buttons (Steam/Epic/YouTube/Twitter/Discord) — awoiaf (`awoiaf.main_menu_web_links`)

**What it does:** Buttons on the title-screen presentation that open the mod's store pages and social links in the system browser.

**How it works:** prsnt:game_start t1 (ti_on_presentation_event_state_change) compares the clicked overlay to $g_url/$g_url_epic/$g_youtube/$g_twitter/$g_discord and calls non-vanilla opcode 3029 with a URL quick-string, then closes the presentation. Opcode 3029 is an engine-extension 'open URL' call; vanilla Warband has no way to open a browser.

- **Hooks:** `prsnt:game_start/t1`
- **Presentations:** `prsnt_game_start`
- **Globals:** `g_url`, `g_url_epic`, `g_youtube`, `g_twitter`, `g_discord`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `wbsd grep UNKNOWN_op --mods awoiaf -> prsnt:game_start/t1 stmt 3,7,11,15,19 (5x op3029)`, `dis prsnt:game_start/t1: each op3029 takes a qstr_https://... URL (steam, epic launcher, youtube, twitter, discord)`, `auto report: 3029 x5 total -> all five sites are in this one block`

<a id="awoiafparty-screen-hotkeys"></a>
### Party/loot exchange screen hotkeys (take all, drop all prisoners, move stacks) — awoiaf (`awoiaf.party_screen_hotkeys`)

**What it does:** While the party-exchange or loot screen is open, keyboard shortcuts act on whole stacks: Ctrl+A takes every prisoner from the loot/defeated party, Ctrl+S takes all freed troops, Up/Down/PageUp/PageDown reorder or move a troop stack between garrison and party, Right/Left Ctrl+arrow transfer whole groups to/from the other party, Ctrl+D hands all non-hero prisoners to the other party.

**How it works:** Trick: the engine calls game_get_troop_wage for every stack while the party screen is drawn, so AWOIAF's game_get_troop_wage first calls initialize_exchange_screen_extensions(troop). That script polls key_is_down combos and, depending on which screen is open (trp_globals_troop slot 12: 10 = loot/temp party, 12 = garrison/encounter exchange; slot 11 = troop under the cursor), moves stacks with party_add_prisoners/party_remove_prisoners/party_add_members using p_temp_party, $current_town or $g_encountered_party, respecting free capacity.

- **Hooks:** `script:game_get_troop_wage`
- **Scripts:** `initialize_exchange_screen_extensions`, `game_get_troop_wage`, `party_add_party_companions`
- **Slots:** `troop:11`, `troop:12`
- **Globals:** `current_town`, `g_encountered_party`
- **Module-specific resources:** troop: trp_globals_troop; party: p_temp_party
- **Relation to Native:** modifies-native
- **Confidence:** strongly-inferred
- **Evidence:** `callers initialize_exchange_screen_extensions: game_get_troop_wage @1 (only call site)`, `dis initialize_exchange_screen_extensions: key_left_control+key_a / +key_s / key_up / key_down / key_page_up / key_page_down / right_control+right / +left / left_control+key_d branches`, `slot awoiaf troop 12 used as screen-mode flag (const 10/12)`
- **Overlaps:** `pop.party_screen_hotkeys`, `tld.exchange_screen_hotkeys`

<a id="beaerial-command-view"></a>
### Aerial command camera with mouse-placed company positions (PBS) — be (`be.aerial_command_view`)

**What it does:** Pressing U in battle lifts the camera 10 m above the player, tilted down, freezes the player's body, and opens a company panel (type, strength, discipline, accuracy, energy, special abilities). Right-click-drag on the ground places the selected companies' hold position and facing; with several companies selected they are laid out side by side.

**How it works:** mst:lead_charge/t71 (key_u, 0.3 s delay): toggles $aerial_view_state, mission_cam_set_mode 1 + mission_cam_animate_to_position (+1000 z, -25 deg pitch), agent_set_no_dynamics on player and horse. mst:lead_charge/t70 (every frame while $aerial_view_state == 2): starts prsnt_pbs, uses store_mouse_projection_to_pos3 to project the cursor onto terrain into marker prop $pbs_point1; on release with the order timer free, for listening classes (class_is_listening_order, not retreating 76+div != 4, non-empty) calls company_hold_pos30 for one company, or spreads several along the drag line with rotate_pos31_towards_pos30, plays company_play_vo. prsnt_pbs (545 stmts) shows per-company info and ability buttons (covering fire, dig-in, gas, gas masks, grenades, merge, prone, square) whose availability depends on technology slots 417-422.

- **Hooks:** `mst:lead_charge/t71:cond`, `mst:lead_charge/t70:conseq`, `prsnt:pbs/t0`, `prsnt:pbs/t2`, `mst:lead_charge/t73:conseq`
- **Scripts:** `store_mouse_projection_to_pos3`, `company_hold_pos30`, `rotate_pos31_towards_pos30`, `get_company_soldiers_number`, `company_play_vo`, `company_get_name_pbs_menu`, `store_company_average_position_to_pos30`, `if_coveringfire_is_on_for_selected_companies`, `if_pronemode_is_on_for_selected_companies`, `if_gasmasks_is_on_for_selected_companies`
- **Presentations:** `prsnt_pbs`
- **Slots:** `team:76-83`, `team:205-212`, `faction:417`, `faction:418`, `faction:419`, `faction:420`, `faction:422`
- **Globals:** `aerial_view_state`, `aerial_view_hol_pos_order_timer`, `pbs_point1`, `player_company1_type..player_company8_type`, `menu_pbs_*`
- **Module-specific resources:** mesh: mesh_pbs_company_info, mesh_pbs_activeability
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `dis be mst:lead_charge/t71:cond (camera lift, no_dynamics)`, `dis be mst:lead_charge/t70:conseq (mouse projection, hold-position per company)`, `explain be prsnt:pbs/t0 (company info and ability globals)`
- **Overlaps:** `acw.command_all_allies`, `acw.death_camera`

<a id="befirearm-item-info-text"></a>
### Firearm descriptions in item tooltips — be (`be.firearm_item_info_text`)

**What it does:** Weapon tooltips gain coloured extra lines describing each gun: smoothbore vs rifled, cartridge type, second barrel, repeating action, era - generated from item slots filled once at game start.

**How it works:** game_get_item_extra_text (engine script, modified Native 331 vs 54 stmts): for extra-text line 0/1 sets a colour with set_trigger_result and a qstr per weapon family ('Has second barrel', 'Uses pistol cartridges', ...). Item slots 2000-2006 (rifle-family links, fire rate in 2006 used by mst:lead_charge/t34) are written by item_detial (5907 stmts, from game_start); 101/102/450 are touched on ~every item.

- **Hooks:** `script:game_get_item_extra_text (engine)`, `script:game_start (item_detial)`
- **Scripts:** `game_get_item_extra_text`, `item_detial`, `initialize_item_info`
- **Slots:** `item:2000-2006`, `item:101`, `item:102`, `item:450`
- **Relation to Native:** modifies-native
- **Confidence:** strongly-inferred
- **Evidence:** `dis be game_get_item_extra_text (first 32 stmts)`, `auto report: game_get_item_extra_text 331/54, initialize_item_info 603/264, item slots 2000-2006 accesses`

<a id="beironsight-aiming"></a>
### First-person iron-sight camera when aiming firearms — be (`be.ironsight_aiming`)

**What it does:** In first-person view, raising a musket or rifle moves the camera to the gun's sight line; after a bolt-action shot the camera stays down the sights for the cycling animation, then returns.

**How it works:** mst:lead_charge/t42 (every frame), gated by $ironsight_enabled. If the player's upper-body animation is ready_musket/release_musket/ready_crossbow/release_crossbow/bolt_action_shot/bolt_shot_straightpull, camera is first person and game key 21 not clicked: enter ironsight mode with a short delay ($ironsight_timer), then mission_cam_set_mode 1 and mission_cam_set_position at the right-hand bone (19) or, during bolt cycling, the head/hand bone (14) offset -10/-44 y and +9 z, rotated -90 deg. Leaves mode (mission_cam_set_mode 0) when the animation ends.

- **Hooks:** `mst:lead_charge/t42:conseq`
- **Mission templates:** `all 25 BE templates`
- **Globals:** `ironsight_enabled`, `ironsight_mode`, `ironsight_timer`, `ironsight_timer2`, `ironsight_aux`, `ironsight_aux2`
- **Module-specific resources:** anim: ready_musket, release_musket, ready_crossbow, release_crossbow, bolt_action_shot, bolt_shot_straightpull, lever_action_shot
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `dis be mst:lead_charge/t42:conseq (77 stmts)`, `no option toggle located (where $ironsight_enabled is set was not traced)`
- **Overlaps:** `acw.rifle_iron_sight_zoom`, `sw.scope_and_visor_overlays`

<a id="bibattle-event-messages"></a>
### Battle announcements: first blood, fallen heroes, kill milestones — bi (`bi.battle_event_messages`)

**What it does:** During battles the game announces who drew first blood, names every lord or companion who falls (red for allies, green for enemies), and congratulates the player at 5, 10, 20 and 40 personal kills.

**How it works:** ti_before_mission_start resets $g_battle_first_blood and $g_battle_player_kills; ti_on_agent_killed_or_wounded (mst:lead_charge/t4 and the siege/village equivalents) prints 'First blood is yours' / 'Your men draw first blood' / 'The enemy draws first blood', '{s5} has fallen' for heroes, and '{reg4} have fallen to your hand' at milestones.

- **Hooks:** `mst:lead_charge/t4:conseq`, `mst:castle_attack_walls_ladder/t2:conseq`, `mst:besiege_inner_battle_castle/t2:conseq`, `mst:village_raid/t1:conseq`
- **Mission templates:** `mst_lead_charge`, `mst_castle_attack_walls_ladder`, `mst_castle_attack_walls_belfry`, `mst_castle_attack_walls_defenders_sally`, `mst_besiege_inner_battle_castle`, `mst_besiege_inner_battle_town_center`, `mst_village_raid`, `mst_village_attack_bandits`
- **Globals:** `g_battle_first_blood`, `g_battle_player_kills`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis bi mst:lead_charge/t4:conseq`, `global bi g_battle_player_kills: 11 writers / 8 readers, all mission-template triggers`, `quick strings 'First_blood_is_yours', '{reg4}_have_fallen_t...'`
- **Overlaps:** `acw.order_voice_callouts`, `nw.fkey_order_tree`, `nw.objective_markers_hud`, `nw.voice_commands`, `sw.battle_start_speeches`

<a id="laiglefaro-card-game"></a>
### Faro gambling minigame — laigle (`laigle.faro_card_game`)

**What it does:** A tavern gambler offers games of Faro: a presentation with the 13 card ranks where you click to stack bets, deal, and win or lose depending on the dealer's and player's cards.

**How it works:** dlg:2217 faro_talk -> start_presentation prsnt_faro_play (t0 load 91, t1 event 66, t2 run 160 stmts). Bets per rank in $bet_ace..$bet_king, deck state in $spade_*; get_faro_card (159 stmts) draws cards; texts 'Deal Cards', 'Leave Table', 'Bet High Card'.

- **Hooks:** `dlg:2218:dlga_faro_talk:close_window:conseq`, `prsnt:faro_play/t0`, `prsnt:faro_play/t1`, `prsnt:faro_play/t2`
- **Scripts:** `get_faro_card`
- **Presentations:** `prsnt_faro_play`
- **Dialogs:** `dlg:2217:dlga_start:faro_talk`, `dlg:2219:dlga_faro_talk:faro_rules`
- **Globals:** `bet_ace`, `bet_king`, `spade_ace`, `dealer_card`, `player_card`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `grep laigle prsnt_faro_play -> dlg:2218`, `explain laigle prsnt:faro_play/t0 (globals/texts)`
- **Overlaps:** `sw.cantina_blackjack_and_brawls`

<a id="laiglekeep-battlefield-pickups"></a>
### Keep weapons and horse picked up in battle — laigle (`laigle.keep_battlefield_pickups`)

**What it does:** Every ten seconds of a battle, whatever weapon or horse the player is currently using is copied into their real inventory, so gear grabbed off the field is kept afterwards.

**How it works:** keep_flags (40 stmts) from a 10 s trigger in 11 battle templates (lead_charge/t17, sieges, naval, quick battles, village fights): for the player's wielded items (left and right hand) not in the troop's equipment, troop_add_item (optionally agent_unequip_item); if the ridden horse differs from inventory slot 8, moves the old horse to inventory and sets slot 8. Skipped in quick battles.

- **Hooks:** `mst:lead_charge/t17:conseq`, `mst:naval_battle/t10:conseq`, `mst:castle_attack_walls_ladder/t15:conseq`
- **Scripts:** `keep_flags`
- **Mission templates:** `mst_lead_charge`, `mst_naval_battle`, `mst_castle_attack_walls_ladder`, `mst_castle_attack_walls_belfry`, `mst_besiege_inner_battle_castle`, `mst_village_attack_bandits`
- **Globals:** `g_player_agent`, `g_player_troop`, `g_is_quick_battle`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis laigle keep_flags`, `explain laigle keep_flags (11 template callers)`
- **Overlaps:** `acan.slave_economy`, `ad457.village_enslavement_and_repopulation`, `vc.town_plunder_and_slaves`

<a id="nwcustom-battle-division-designer"></a>
### Custom battle designer by division — nw (`nw.custom_battle_division_designer`)

**What it does:** NW's custom battle screen lets the player compose both armies division by division (troop type and size for each of nine divisions per side, factions, banners) and then fights it with the division AI.

**How it works:** prsnt_game_custom_battle_designer (t0 592-stmt layout, t2 262-stmt event handler) writes per-division troop choice and count into trp_custom_battle_dummy (455) slots 0-19 and trp 456 tables, then spawn_quick_battle_army (98 stmts, modified Native) adds the troops and banners and jumps to mst_quick_battle_battle; custom_battle_set_division_names labels divisions; custom_battle_end closes.

- **Hooks:** `prsnt:game_custom_battle_designer/t0`, `prsnt:game_custom_battle_designer/t2`, `mst:quick_battle_battle/t9:conseq`
- **Scripts:** `spawn_quick_battle_army`, `custom_battle_set_division_names`, `custom_battle_end`, `custom_battle_deployment`
- **Presentations:** `prsnt_game_custom_battle_designer`
- **Mission templates:** `mst_quick_battle_battle`
- **Slots:** `troop:0-19 (trp 455)`, `troop:0-107 (trp 456)`
- **Globals:** `g_quick_battle_team_1_faction`, `g_quick_battle_team_2_faction`, `g_quick_battle_troop`, `g_is_quick_battle`
- **Relation to Native:** modifies-native
- **Confidence:** strongly-inferred
- **Evidence:** `explain nw spawn_quick_battle_army: caller prsnt:game_custom_battle_designer/t2`, `explain nw battle_tactic_init_aux text 'Centre_Inf','Lflank_Inf' ...`

<a id="nwfkey-order-tree"></a>
### F-key order tree with 'hold where I look' arrow — nw (`nw.fkey_order_tree`)

**What it does:** Pressing F4 opens a small order overlay: F4 again = movement (hold at the spot you are looking at, shown by a ground arrow while the key is held; follow; charge; advance; halt; fall back; retreat; slow/quick march), F5 = formation (line, column, square, skirmish, wheel left/right, face enemy), F6 = firing (fire at will / volley / hold).

**How it works:** mst:sp_campaign_*/t4 cond key_clicked F4 and presentation 52 not active -> start_presentation prsnt_new_order_stuff. Its ti_on_presentation_run (t1) reads F4-F12 and calls give_mm_order(menu, order, team). While F4 is held in the movement sub-menu it ray-marches from the player's look position (agent_get_look_position, step 5 cm until ground) and moves a visible arrow prop ($g_hold_position_arrow_instance, spawned in t7) there; releasing F4 issues 'hold here'. Orders are applied only to divisions selected in the Native order UI (class_is_listening_order) and echoed as '<division>, form square!' etc.

- **Hooks:** `mst:sp_campaign_vienna/t4:cond`, `mst:sp_campaign_vienna/t4:conseq`, `prsnt:new_order_stuff/t0`, `prsnt:new_order_stuff/t1`, `mst:sp_campaign_vienna/t7:conseq`
- **Scripts:** `give_mm_order`
- **Presentations:** `prsnt_new_order_stuff`, `prsnt_custom_order_menu`
- **Mission templates:** `mst_sp_campaign_vienna`, `mst_sp_campaign_austerlitz_1`, `mst_sp_campaign_austerlitz_1_old`, `mst_sp_campaign_dresden_1`, `mst_sp_campaign_dresden_2`
- **Slots:** `troop:40-118 (trp_custom_battle_dummy order arrays)`
- **Globals:** `g_presentation_order_screen`, `g_presentation_order_last_command_at`, `g_hold_position_arrow_instance`, `g_presentation_obj_order_screen_0`, `g_presentation_obj_order_screen_1`, `g_presentation_obj_order_screen_2`, `g_presentation_obj_order_screen_3`
- **Module-specific resources:** spr: spr 449 (hold-position arrow); mesh: order screen overlay meshes
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis nw mst:sp_campaign_vienna/t4:cond -> key_clicked key_f4, neg|is_presentation_active 52`, `sqlite names nw prsnt 52 = prsnt_new_order_stuff`, `dis nw prsnt:new_order_stuff/t1: 21 bare-int calls to give_mm_order keyed on F4..F12`, `explain nw give_mm_order text: 'hold this position!', 'follow me!', 'charge!', ...`
- **Overlaps:** `acw.order_voice_callouts`, `bi.battle_event_messages`, `nw.objective_markers_hud`, `nw.voice_commands`, `sw.battle_start_speeches`

<a id="nwobjective-markers-hud"></a>
### On-screen objective markers and mission timer/progress counter — nw (`nw.objective_markers_hud`)

**What it does:** Up to four objective markers float over their real-world positions on screen (hidden when off-screen), and a HUD counter shows either a countdown timer (m:ss) or a 'x of y' progress count for the current goal.

**How it works:** Mission triggers spawn invisible locator props (spr 1565) and move them to objective points ($g_objectives_locator_instance_1..4), then set $g_projection_state 1-4. prsnt_singleplayer_objective_projection_display/t1 (every frame) takes each locator's position +2.5 m, converts it with position_get_screen_projection and moves an overlay there (display only when inside -100..1100 x -100..850). prsnt_singleplayer_progress_counter/t1 mode 1 = countdown from $g_singleplayer_progress_counter_start_time/_max_value, mode 2 = string with reg0/reg1, mode -1 closes.

- **Hooks:** `prsnt:singleplayer_objective_projection_display/t0`, `prsnt:singleplayer_objective_projection_display/t1`, `prsnt:singleplayer_progress_counter/t0`, `prsnt:singleplayer_progress_counter/t1`, `mst:sp_campaign_vienna/t7:conseq`
- **Presentations:** `prsnt_singleplayer_objective_projection_display`, `prsnt_singleplayer_progress_counter`
- **Mission templates:** `mst_sp_campaign_vienna`, `mst_sp_campaign_austerlitz_1`, `mst_sp_campaign_austerlitz_1_old`, `mst_sp_campaign_dresden_1`, `mst_sp_campaign_dresden_2`, `mst_camp_1`
- **Globals:** `g_projection_state`, `g_objectives_locator_instance_1`, `g_objectives_locator_instance_2`, `g_objectives_locator_instance_3`, `g_objectives_locator_instance_4`, `g_singleplayer_progress_counter_mode`, `g_singleplayer_progress_counter_cur_value`, `g_singleplayer_progress_counter_max_value`, `g_singleplayer_progress_counter_start_time`, `g_singleplayer_progress_counter_string_id`, `g_singleplayer_progress_counter_overlay`
- **Module-specific resources:** spr: spr 1565 (objective locator); mesh: objective marker overlay mesh
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis nw prsnt:singleplayer_objective_projection_display/t1 (80 stmts)`, `dis nw prsnt:singleplayer_progress_counter/t1 (37 stmts)`, `global nw g_projection_state: 33 writers across sp_campaign_* and camp_1`
- **Overlaps:** `acw.order_voice_callouts`, `bi.battle_event_messages`, `nw.fkey_order_tree`, `nw.voice_commands`, `sw.battle_start_speeches`

<a id="nwvoice-commands"></a>
### Shouted voice commands and order call-outs — nw (`nw.voice_commands`)

**What it does:** The player (and officers) can shout a voice command with a key; NPC soldiers and officers audibly call out orders when the player issues them, with nationality- and gender-appropriate voice sets and a cooldown that is shorter for officers.

**How it works:** mst:quick_battle_battle/t0 (every frame, key 43 = voice-command key) -> if not multiplayer calls multiplayer_server_agent_play_voicecommand(agent, cmd) directly (SP branch); t1 (ti_on_order_issued) makes agents of the ordered divisions shout. The script (178 stmts, guard this_or_next|multiplayer_is_server / neg|game_in_multiplayer_mode) checks agent slot 1 (last shout time) against $g_time_between_voice_commands(_officer) by troop rank slot 12 (3-5 = officers), picks a voice set from troop faction/troop range and player gender, and plays the sound at the agent. Musicians and pianists are excluded.

- **Hooks:** `mst:quick_battle_battle/t0:conseq`, `mst:quick_battle_battle/t1:conseq`
- **Scripts:** `multiplayer_server_agent_play_voicecommand`, `cf_agent_is_playing_music`, `cf_agent_is_playing_piano`, `client_get_my_agent`
- **Mission templates:** `mst_quick_battle_battle`, `mst_multiplayer_dm`, `mst_multiplayer_tdm`, `mst_multiplayer_hq`, `mst_multiplayer_cf`, `mst_multiplayer_sg`, `mst_multiplayer_bt`, `mst_multiplayer_cb`, `mst_multiplayer_duel`, `mst_multiplayer_kh`, `mst_multiplayer_br`
- **Slots:** `agent:1 (last shout time)`, `troop:12 (rank class)`
- **Globals:** `g_time_between_voice_commands`, `g_time_between_voice_commands_officer`, `g_last_voice_command_at`
- **Module-specific resources:** sound: NW voice-command banks per nation (British, French, Prussian, Russian, Austrian, ...)
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis nw mst:quick_battle_battle/t0:cond/conseq - key 43, SP else-branch`, `roots nw multiplayer_server_agent_play_voicecommand includes mst:quick_battle_battle`, `dis nw multiplayer_server_agent_play_voicecommand stmts 0-46`
- **Overlaps:** `acw.order_voice_callouts`, `bi.battle_event_messages`, `nw.fkey_order_tree`, `nw.objective_markers_hud`, `sw.battle_start_speeches`

<a id="oa1860cheat-mode-camp-toggle"></a>
### Camp-menu cheat-mode toggle (broken) — oa1860 (`oa1860.cheat_mode_camp_toggle`)

**What it does:** Camp > Take an action offers 'Enable cheat mode' / 'Disable cheat mode', but the options flip the wrong variable, so cheat mode is not actually toggled.

**How it works:** menu:camp_action/opt:action_enable_cheat_mode: cond (eq $g_siege_final_menu 0), conseq (assign $g_siege_final_menu 1) and jump back; disable is the mirror. Native cheat options read $cheat_mode, which these never write.

- **Hooks:** `menu:camp_action/opt:action_enable_cheat_mode:conseq`, `menu:camp_action/opt:action_disable_cheat_mode:conseq`
- **Menus:** `menu_camp_action`
- **Globals:** `g_siege_final_menu`, `cheat_mode`
- **Relation to Native:** modifies-native
- **Confidence:** strongly-inferred
- **Evidence:** `dis oa1860 menu:camp_action/opt:action_enable_cheat_mode:cond/conseq (global resolves to $g_siege_final_menu)`, `sqlite: no other module has these option ids`

<a id="perisnoexchange-screen-extensions"></a>
### Party-exchange screen extensions (hover hotkeys on the troop screens) — perisno (`perisno.exchange_screen_extensions`)

**What it does:** While a party/loot/garrison exchange screen is open, extra keyboard shortcuts and automatic stack handling are active. The shortcuts are not named in the compiled tables; the script is a 563-statement input handler.

**How it works:** The engine calls game_get_troop_wage for every troop row it draws while a party screen is open. Perisno's replacement of that script (114 stmts vs 43 in Native) calls initialize_exchange_screen_extensions, which reads input state, keeps screen mode in trp_globals_troop slots 11/12 and party slot 421, and uses party_add_party_companions on p_temp_party to rebuild rosters. The exact key bindings were not traced.

- **Hooks:** `script:game_get_troop_wage`
- **Scripts:** `game_get_troop_wage`, `initialize_exchange_screen_extensions`, `party_add_party_companions`, `et_process_troop_swapping`
- **Slots:** `troop:11`, `troop:12`, `troop:28`, `party:421`
- **Globals:** `g_move_heroes`
- **Relation to Native:** modifies-native
- **Confidence:** strongly-inferred
- **Evidence:** `explain perisno initialize_exchange_screen_extensions: sole direct caller script:game_get_troop_wage; behaviour profile party_members 78%, input 10%; slots troop[11], troop[12], party[421]`, `explain perisno script:game_get_troop_wage: MODIFIED Native script, 114 stmts vs 43 (14% similar); callees include initialize_exchange_screen_extensions and et_process_troop_swapping`, `key bindings not decoded; no displayed text for the shortcuts`

<a id="popcamp-troop-review-drill"></a>
### Walk among and drill your army from the camp menu — pop (`pop.camp_troop_review_drill`)

**What it does:** From the camp menu the player can 'walk around and review your soldiers': the whole party is spawned in a random field scene where the player can inspect troops and practise formation orders without a battle.

**How it works:** menu:camp/opt:camp_action_1 sets jump mission mst_camp_review_soldiers, counts fit troops (party_count_fit_for_battle) and calls setup_random_scene, then change_screen_mission. The mission template carries the same formation/field-tactics triggers as lead_charge (t10-t30: cf_formation, field_tactics) plus a tab-to-leave trigger (t0).

- **Hooks:** `menu:camp/opt:camp_action_1:conseq`
- **Scripts:** `setup_random_scene`, `party_count_fit_for_battle`, `cf_formation`, `field_tactics`
- **Menus:** `menu_camp`
- **Mission templates:** `mst_camp_review_soldiers`
- **Globals:** `g_encountered_party`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `dis menu:camp/opt:camp_action_1:conseq (full)`, `sqlite blocks: mst_camp_review_soldiers triggers t0-t30 incl. formation calls`, `explain cf_formation entry points include camp_review_soldiers`
- **Overlaps:** `acan.player_permanent_camps`, `acw.walkable_party_camp`, `tld.camp_menu_actions`

<a id="popparty-screen-hotkeys"></a>
### Party/garrison exchange-screen hotkeys (take all, move stacks) — pop (`pop.party_screen_hotkeys`)

**What it does:** On the party exchange screen the player can press Ctrl+A to take all prisoners and Ctrl+S to take all troops from the other side (up to capacity, keeping wounded counts); in garrison management arrow keys and Page Up/Down move the selected troop stack between party and garrison or reorder it.

**How it works:** The engine calls game_get_troop_wage for every stack while the exchange screen is open; PoP's version stores the queried troop/party in troop slots 405/407 of a dummy troop (trp_quick_battle_6_player) and calls initialize_exchange_screen_extensions(troop) first. That script polls key_is_down: with slot 406 = 10 (loot/prisoner exchange opened from menus/trig:31) Ctrl+A moves p_temp_party prisoners into p_main_party and Ctrl+S moves companions (respecting free capacity and wounded); with slot 406 = 12 (garrison management opened via menu:town/opt:castle_station_troops, old_ruins, camp master) up/down/page-up/page-down move the hovered stack (slot 405 = last queried troop) between p_main_party and $current_town using party_add_party_companions on p_temp_party as scratch. Mode flag 406 is set by the menus that open the screen.

- **Hooks:** `script:game_get_troop_wage`, `menu:town/opt:castle_station_troops:conseq`, `menu:old_ruins/opt:camp_station_troops:conseq`, `dlg:3470:dlga_camp_master_garrison_1:camp_master_pretalk:conseq`, `trig:31:conseq`
- **Scripts:** `initialize_exchange_screen_extensions`, `game_get_troop_wage`, `party_add_party_companions`
- **Menus:** `menu_town`, `menu_old_ruins`
- **Dialogs:** `dlg:3470`
- **Slots:** `troop:405`, `troop:406`, `troop:407`
- **Globals:** `current_town`, `g_move_heroes`
- **Module-specific resources:** troop: trp_quick_battle_6_player (dummy slot holder)
- **Relation to Native:** modifies-native
- **Confidence:** strongly-inferred
- **Evidence:** `dis game_get_troop_wage head: troop_set_slot 407, call initialize_exchange_screen_extensions, troop_set_slot 405`, `dis initialize_exchange_screen_extensions: key_left_control+key_a / +key_s / key_up / key_down / key_page_up / key_page_down branches`, `slot pop troop 406: set to 10/12 by station-troops menus and trig:31`, `explain entry points include prsnt:budget_report and menu:morale_report (wage queries)`
- **Overlaps:** `awoiaf.party_screen_hotkeys`, `tld.exchange_screen_hotkeys`

<a id="swmass-upgrade-preview"></a>
### Upgrade-all with preview of who can be promoted — sw (`sw.mass_upgrade_preview`)

**What it does:** A party menu option simulates upgrading the whole army with its current experience and shows a paged list of every stack that can upgrade and into what (including branching choices), so the player can promote everyone in one go.

**How it works:** menu:ready_upgrade -> calculate_upgrade_troops: copies the main party into scratch party 1 (party_copy), runs party_upgrade_with_xp(1, 1, 1) on the copy, strips prisoners/heroes, then compares stacks against a second copy (party 3) to fill troop 907/908/909 slot tables (troop, count, target) - up to 32 rows; prsnt_upgrade_troops pages through them ('{reg3} {s0} can upgrade', 'Upgrade to {s1}').

- **Hooks:** `menu:ready_upgrade`, `prsnt:upgrade_troops/t0`, `prsnt:upgrade_troops/t2`
- **Scripts:** `calculate_upgrade_troops`, `party_copy`, `party_has_troop`, `party_remove_heroes`
- **Menus:** `menu_ready_upgrade`
- **Presentations:** `prsnt_upgrade_troops`
- **Slots:** `troop:0-31 on storage troops 907-909`, `troop:166`
- **Globals:** `g_move_heroes`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis sw calculate_upgrade_troops (party_copy, party_upgrade_with_xp on copy)`, `dis sw menu:ready_upgrade (troop 907/908 tables)`, `explain sw prsnt:upgrade_troops/t0 texts`

<a id="swrebindable-ability-keys"></a>
### In-game key assignment for mod abilities — sw (`sw.rebindable_ability_keys`)

**What it does:** A camp menu lists every mod hotkey (bacta injector, crouch, jetpack, toggle weapon, helmet view, death-cam forward/back); choosing one opens a 'press a key' screen and the new key is stored and shown by name.

**How it works:** menu:setup_keys options start prsnt_key_assignment, whose run trigger waits for any key_clicked and stores it in the chosen global ($bacta_injector_key, $crouch_key, $jetpack_key, $toggle_weapon_key, $helmet_view_key, $deathcam_forward_key, $deathcam_backward_key). get_key (328 stmts) maps a key code to its printable name; get_all_binds builds the menu text. Mission triggers test key_clicked/key_is_down on the globals.

- **Hooks:** `menu:setup_keys`, `prsnt:key_assignment/t1`
- **Scripts:** `get_key`, `get_all_binds`
- **Menus:** `menu_setup_keys`
- **Presentations:** `prsnt_key_assignment`
- **Globals:** `active_key`, `bacta_injector_key`, `crouch_key`, `jetpack_key`, `toggle_weapon_key`, `helmet_view_key`, `deathcam_forward_key`, `deathcam_backward_key`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `explain sw get_key: entry points menu:setup_keys, prsnt:key_assignment/t1; globals written bacta_injector_key ...`

<a id="swscope-and-visor-overlays"></a>
### Scope zoom overlay and first-person helmet visor — sw (`sw.scope_and_visor_overlays`)

**What it does:** Holding the zoom key with a ranged weapon shows a weapon-appropriate scope/crosshair overlay (binoculars when unarmed); a helmet-view hotkey draws the inside of the worn helmet (stormtrooper, Mandalorian, ...) over the screen.

**How it works:** mst:lead_charge/t27 (game_key_is_down zoom) -> start prsnt_zoom_view: picks overlay by wielded item type (none/melee/shield = binocular style, firearm/crossbow types = scope) and closes when the key is released (t1). Helmet view: $helmet_view_key toggles prsnt_helmet_view (150 stmts) which reads the head-armour inventory slot and creates the matching full-screen visor mesh overlay (meshes 63-66...).

- **Hooks:** `mst:lead_charge/t27:cond`, `mst:lead_charge/t27:conseq`, `prsnt:zoom_view/t0`, `prsnt:zoom_view/t1`, `prsnt:helmet_view/t0`
- **Presentations:** `prsnt_zoom_view`, `prsnt_helmet_view`, `prsnt_binocular_display`
- **Mission templates:** `mst_lead_charge`, `mst_lead_charge_no_horse`
- **Globals:** `helmet_view`, `helmet_view_key`, `binocular_magnification`
- **Module-specific resources:** mesh: scope/binocular overlays, helmet visor overlays
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis sw mst:lead_charge/t27 (game_key_is_down 19 -> start_presentation 3 = prsnt_zoom_view)`, `dis sw prsnt:zoom_view/t0 (item_get_type branches)`, `dis sw prsnt:helmet_view/t0 (head slot -> create_mesh_overlay)`
- **Overlaps:** `acw.rifle_iron_sight_zoom`, `be.ironsight_aiming`

<a id="tldcamp-menu-actions"></a>
### Camp menu: walk the camp, review troops in a scene, timed consumables, dynamic party icon — tld (`tld.camp_menu_actions`)

**What it does:** A camp menu on the world map lets the player walk around a terrain-appropriate camp scene, review their troops and prisoners standing in it, use camp consumables with timed effects (Orc brew, Athelas for wound treatment, pipe-weed for a short rest, Ent-water, Miruvor, drums of the deep), rest, or open mod options. The party's map icon also changes automatically between mounted, foot-archer, foot-melee and camping figures.

**How it works:** menu:camp options: camp_troop -> jump_to_random_scene(region, terrain, landmark) + mission 4 (mst_review_troops, troops spawned as visitors); camp_action menu consumes items by setting item slot 13 = active and slot 14 = expiry hour; strig:34 (3 h) decrements the stack and announces expiry; effects are read by game_get_skill_modifier_for_troop (item slot 13 tests) and morale scripts. strig:37 (every frame) inspects the player's equipment (horse slot 8, ranged weapon types) and $g_player_icon_state to call party_set_icon with mounted/archer/melee/camp icons.

- **Hooks:** `menu:camp`, `strig:34`, `strig:37`
- **Scripts:** `jump_to_random_scene`, `game_get_skill_modifier_for_troop`, `cf_correct_party_icon`, `determine_what_player_looks_like`
- **Menus:** `menu:camp`, `menu:camp_action`
- **Mission templates:** `mst_review_troops`
- **Slots:** `item:13`, `item:14`
- **Globals:** `g_camp_mode`, `g_player_icon_state`, `g_player_party_icon`, `g_player_icon_mounted`, `g_player_icon_foot_archer`, `g_player_icon_foot_melee`, `g_ent_water_taking_effect`
- **Module-specific resources:** item: itm_orc_brew, itm_athelas_reward, itm_pipeweed_reward, itm_ent_water; mt: mst_review_troops
- **Relation to Native:** modifies-native
- **Confidence:** strongly-inferred
- **Evidence:** `dis tld menu:camp/opt:camp_troop:conseq (set_jump_mission 4)`, `dis tld menu:camp_action options (item_set_slot 13/14)`, `dis tld strig:34 (expiry)`, `dis tld strig:37 (party_set_icon)`
- **Overlaps:** `acan.player_permanent_camps`, `acw.walkable_party_camp`, `pop.camp_troop_review_drill`

<a id="tldexchange-screen-hotkeys"></a>
### Party-exchange screen hotkeys (take/give all, reorder stacks) — tld (`tld.exchange_screen_hotkeys`)

**What it does:** On the loot screen and the garrison/reserve exchange screen the player can press Ctrl+A to take all prisoners, Ctrl+S to take all rescued troops, Up/Down/PgUp/PgDn while hovering a troop to move that stack in the other party's roster, Right-Ctrl+Right to take every troop, Right-Ctrl+Left to hand over every non-hero troop, and Ctrl+A / Ctrl+D to take or give all non-hero prisoners.

**How it works:** The engine calls game_get_troop_wage for every troop row it draws while a party screen is open, so TLD calls initialize_exchange_screen_extensions(troop) at the top of game_get_troop_wage and polls key_is_down there. trp_globals_troop (troop 1032) slot 12 holds a 'screen mode' set by the dialog/menu that opened the screen (10 = loot, 12 = garrison exchange), slot 10 holds the other party, slot 11 remembers the last hovered troop. The script then rebuilds the other party's roster (via party_add_party_companions into temp party 1) to reorder stacks, or moves whole stacks/prisoners between party 0 and the other party, respecting free capacity and keeping wounded counts.

- **Hooks:** `script:game_get_troop_wage`
- **Scripts:** `initialize_exchange_screen_extensions`, `game_get_troop_wage`, `party_add_party_companions`
- **Menus:** `menu:upkeep_report`
- **Dialogs:** `dlg:261:dlga_player_hire_troop:player_hire_troop_take:conseq`, `dlg:262:dlga_player_hire_troop:player_hire_troop_give:conseq`, `dlg:545:dlga_lord_give_troops:lord_give_troops_check:conseq`, `dlg:241:dlga_companion_give_troops:companion_give_troops_check:conseq`
- **Slots:** `troop:10 (on trp_globals_troop)`, `troop:11 (on trp_globals_troop)`, `troop:12 (on trp_globals_troop)`
- **Globals:** `g_move_heroes`
- **Module-specific resources:** troop: trp_globals_troop (1032); party: temp party 1
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis tld initialize_exchange_screen_extensions: key_is_down key_left_control+key_a/key_s (mode 10), key_up/down/page_up/page_down, key_right_control+key_right/left, key_left_control+key_a/key_d (mode 12)`, `dis tld game_get_troop_wage stmt 0 calls initialize_exchange_screen_extensions`
- **Overlaps:** `awoiaf.party_screen_hotkeys`, `pop.party_screen_hotkeys`

<a id="tldin-game-strategy-options"></a>
### In-game strategy, difficulty and AI tweak options — tld (`tld.in_game_strategy_options`)

**What it does:** A camp 'options' presentation and tweak menus let the player change campaign balance in-game: injuries and permadeath on/off, morale/rout system, animal ambushes, rank and influence gain rates, faction strength regeneration rate and limit, siege strength requirements and how fast they relax, maximum number of parties, and battlefield AI toggles (lord AI, horse-archer AI, archers aiming over orcs, slowing wounded agents, faction weather effects).

**How it works:** prsnt:tld_mod_options (256 stmts) and menus camp_tweaks / camp_strat_tweaks / camp_compat_tweaks / camp_field_ai write $tld_option_* globals (injuries, death_npc, death_player, morale, animal_ambushes, rank_gain_rate, influence_gain_rate, regen_rate, regen_limit, siege_reqs, siege_relax_rate) and $battle_encounter_effects; the systems above read them directly. Shift-click decrements numeric options. The presentation also calls update_savegame (inferred: save-version migration).

- **Hooks:** `menu:camp/opt:camp_options`, `prsnt:tld_mod_options/t0`
- **Scripts:** `update_savegame`
- **Menus:** `menu:camp_tweaks`, `menu:camp_strat_tweaks`, `menu:camp_compat_tweaks`, `menu:camp_field_ai`
- **Presentations:** `prsnt:tld_mod_options`
- **Globals:** `tld_option_injuries`, `tld_option_death_npc`, `tld_option_death_player`, `tld_option_morale`, `tld_option_animal_ambushes`, `tld_option_rank_gain_rate`, `tld_option_influence_gain_rate`, `tld_option_regen_rate`, `tld_option_regen_limit`, `tld_option_siege_reqs`, `tld_option_siege_relax_rate`, `battle_encounter_effects`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `texts tld menu:camp_strat_tweaks options ('Siege strength requirements', 'Strength regen rate', 'Influence gain rate', 'Rank gain rate')`, `texts tld menu:camp_field_ai options`, `global readers of tld_option_* in injury/morale/strength features`
- **Overlaps:** `acw.play_as_ruler_start`, `ad457.royal_and_lord_sandbox_start`, `awoiaf.campaign_setup_options`, `cbl.invasion_date_options`, `laigle.story_start_missions`

<a id="vcgamepad-order-menus"></a>
### Gamepad (Xbox d-pad) battle command menus — vc (`vc.gamepad_order_menus`)

**What it does:** Battle orders, division formations and player functions can be driven from a controller d-pad via small on-screen console menus.

**How it works:** mst:lead_charge/t140 (rearm 0.15 s) fires on key_is_down key_xbox_dpad_right while the hero is alive; it sets $controller_in_use=1 and steps a small state machine in $dpad_menu/$dpad_menu_row that opens prsnt_console_main_menu_extended, then prsnt_console_division_menu, using omit_key_once on the other d-pad keys and close_order_menu; the selected row calls player_order_extended_formations / player_order_regular_formations / player_order_formations / memorize_division_placements / default_division_placements. prsnt_console_player_functions is the third panel.

- **Hooks:** `mst:lead_charge/t140:conseq`
- **Scripts:** `player_order_regular_formations`, `player_order_extended_formations`, `memorize_division_placements`, `default_division_placements`
- **Presentations:** `prsnt_console_main_menu_extended`, `prsnt_console_division_menu`, `prsnt_console_player_functions`
- **Mission templates:** `mst_lead_charge`, `mst_sea_battle`
- **Globals:** `controller_in_use`, `controller_keys`, `dpad_menu`, `dpad_menu_row`, `switch_presentation_new`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis vc mst:lead_charge/t140:cond = key_is_down key_xbox_dpad_right, neg|main_hero_fallen`, `dis vc mst:lead_charge/t140:conseq: $dpad_menu state machine, prsnt_console_* switches, omit_key_once`, `sqlite refs prsnt_console_player_functions in mst:sea_battle`

<a id="vcsecond-outfit"></a>
### Civilian second outfit worn automatically in towns and halls — vc (`vc.second_outfit`)

**What it does:** The player keeps a second (civilian) outfit that is worn automatically when walking around towns, courts and certain quest scenes, instead of full battle gear; its shield still counts for skill modifiers.

**How it works:** init_second_outfit (26 stmts) swaps the player's equipment with a stored set (pseudo troop trp_pseudo_troop_end used as wardrobe) when entering mst_visit_town_castle and other civilian scenes; cf_player_use_second_outfit decides by $current_town and active quests (qst_hunt_down_fugitive etc.); called from 37 menu blocks and dialogs. Modified game_get_skill_modifier_for_troop (272 vs Native 20 stmts) accounts for the second outfit's shield.

- **Hooks:** `script:cf_player_use_second_outfit`, `script:init_second_outfit`
- **Scripts:** `init_second_outfit`, `cf_player_use_second_outfit`, `game_get_skill_modifier_for_troop`
- **Mission templates:** `mst_visit_town_castle`
- **Slots:** `quest:1`
- **Globals:** `current_town`
- **Module-specific resources:** troop: trp_pseudo_troop_end (wardrobe store)
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `sqlite refs init_second_outfit: mst_visit_town_castle, trp_pseudo_troop_end, itm_wooden_shield`, `auto report: cf_player_use_second_outfit 9 callers (dlg2, menu37, mst1)`, `Changelog 2.072 'consider shield in second outfit for skill modifiers'; 2.054 'fix skill modifiers from second outfit'`

<a id="befaction-troop-tree-viewer"></a>
### In-game faction troop-tree viewer — be (`be.faction_troop_tree_viewer`)

**What it does:** A presentation that draws any faction's full upgrade tree (troop portraits on tableau, connecting lines, tiers, pages), toggled between factions, outlaws and mercenaries; clicking a troop shows level, health, attributes, key skills and equipment.

**How it works:** prsnt_faction_troop_trees (t0 279 stmts): troop_tree_recursive_detect_max_tier and troop_tree_recursive_backtracking walk troop_get_upgrade_troop recursively from each faction's base troop, laying out nodes; get_page_no_of_troop_tree_for_troop_on paginates; prsnt_upgrade_tree_troop_and_name / prsnt_upgrade_tree_troop_cost / prsnt_line(s) draw nodes and lines; tab_game_party_window tableau for portraits; skill refs ironflesh..horse_archery for the info box. cf_get_faction_rifle_type swaps the shown rifle by technology.

- **Hooks:** `prsnt:faction_troop_trees/t0`, `prsnt:faction_troop_trees/t1`
- **Scripts:** `troop_tree_recursive_backtracking`, `troop_tree_recursive_detect_max_tier`, `get_page_no_of_troop_tree_for_troop_on`, `prsnt_upgrade_tree_troop_and_name`, `prsnt_upgrade_tree_troop_cost`, `prsnt_line`, `prsnt_lines`
- **Presentations:** `prsnt_faction_troop_trees`
- **Slots:** `troop:163`, `troop:313`
- **Globals:** `g_selected_page`, `g_selected_troop`, `g_cur_slot_no`
- **Module-specific resources:** mesh: mesh_white_plane, mesh_inv_slot; tableau: tab_game_party_window
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `explain be prsnt:faction_troop_trees/t0`
- **Overlaps:** `acan.troop_detail_and_upgrade_trees`, `bi.world_map_presentation`, `vc.camp_and_report_screens`

<a id="biworld-map-presentation"></a>
### Reports: zoomable political world map screen — bi (`bi.world_map_presentation`)

**What it does:** A Reports menu entry opens a full-screen schematic map showing every town, castle and village as coloured blocks by owning faction, with toggles for towns/castles/villages and names on mouse-over.

**How it works:** menu:reports option action_view_world_map -> start_presentation 52 (prsnt_world_map, 282-statement load trigger): iterates centers, reads positions and faction colours (faction slot 21), draws overlay blocks; checkboxes filter by type; get_closest_center used for hover labels.

- **Hooks:** `menu:reports/opt:action_view_world_map:conseq`, `prsnt:world_map/t0`
- **Scripts:** `get_closest_center`
- **Menus:** `menu_reports`
- **Presentations:** `prsnt_world_map`
- **Slots:** `faction:21`, `party:120`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `grep bi: menu:reports/opt:action_view_world_map:conseq (start_presentation, 52)`, `explain bi prsnt:world_map/t0: text 'The_World_Map', 'Show_towns/castles/villages', 'Tip: move the mouse onto the black blocks...'`, `grep bi create_mesh_overlay --kinds prsnt: prsnt:world_map draws only mesh_white_plane (Native core mesh) - no custom art needed`
- **Overlaps:** `acan.troop_detail_and_upgrade_trees`, `be.faction_troop_tree_viewer`, `vc.camp_and_report_screens`

<a id="nwbattle-results-payout"></a>
### Post-battle results screen with kill-based pay and casualty tally — nw (`nw.battle_results_payout`)

**What it does:** After each scripted battle a results screen lists enemies killed, the player's personal kills, allies and companions lost, and the money earned: +20 per personal kill, +10 per enemy killed by the army, -5 per soldier lost, -10 per companion lost; the player can accept or retry.

**How it works:** ti_on_agent_killed_or_wounded (mst:sp_campaign_*/t3) calls sp_process_death_for_battle_results(dead, killer) which updates $g_sp_allies_lost / $g_sp_companions_lost (troop range 511-540 = companions) / $g_sp_enemies_killed / $g_sp_personal_kills / $g_sp_money_gained. prsnt_singleplayer_mission_results (220 stmts on load) renders the table and sets $g_singleplayer_mission_results_done / _retry; the money is spent at the camp merchants (sp_camp_set_merchandise stocks trp 550/551 at mission start of mst_camp_1).

- **Hooks:** `mst:sp_campaign_vienna/t3:conseq`, `prsnt:singleplayer_mission_results/t0`, `prsnt:singleplayer_mission_results/t1`, `mst:camp_1/t2:conseq`
- **Scripts:** `sp_process_death_for_battle_results`, `sp_camp_set_merchandise`, `store_vince_random_in_range`
- **Presentations:** `prsnt_singleplayer_mission_results`
- **Mission templates:** `mst_sp_campaign_vienna`, `mst_sp_campaign_austerlitz_1`, `mst_sp_campaign_austerlitz_1_old`, `mst_sp_campaign_dresden_1`, `mst_sp_campaign_dresden_2`, `mst_camp_1`
- **Globals:** `g_sp_allies_lost`, `g_sp_companions_lost`, `g_sp_enemies_killed`, `g_sp_personal_kills`, `g_sp_money_gained`, `g_singleplayer_mission_results_done`, `g_singleplayer_mission_results_retry`
- **Module-specific resources:** troop: trp 550/551 (camp merchants), trp 511-540 (campaign companions)
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis nw sp_process_death_for_battle_results (29 stmts, money deltas +20/+10/-5/-10)`, `explain nw prsnt:singleplayer_mission_results/t0: reads g_sp_* globals, text 'Battle Results','Personal kills:','Allies lost:'`, `dis nw sp_camp_set_merchandise`

<a id="popfief-base-income-and-reports"></a>
### Per-fief base income with income and construction reports — pop (`pop.fief_base_income_and_reports`)

**What it does:** Every center has a 'base income' value (raised by buildings, lowered by damage and raids) that feeds its weekly wealth, and the Reports menu adds a fief income report (base income and prosperity of each of the player's fiefs, plus a list of fiefs with pending heartbeat crises) and a construction report (what is being built where and how many days remain).

**How it works:** Party slot 290 holds base income: initialised in pop2_location_improvements, changed by center_base_income_change (building completed/damaged/repaired, raids, peace deals) and a steward's lavish tournament (dlg:2307). strig:26 (weekly) adds 1000 + prosperity x 14 + base income x 4 (x1.3 in five capital towns) minus garrison wage (x3/4 when the player's spouse/minister owns it) to Native town wealth (slot 49) for non-player centers. menu:reports/opt:view_center_income_report -> menu:center_income_report lists player fiefs with slot 290 and slot 50 prosperity text; option lists fiefs with party slot 296 set; menu:center_construction_report reads Native slots 124/125 and get_improvement_details to print 'building X, N days left'. Steward/elder dialogs dlg:2431 / dlg:3407 report the same numbers in person.

- **Hooks:** `menu:reports/opt:view_center_income_report:conseq`, `menu:center_income_report/opt:construction:conseq`, `strig:26`, `dlg:2431:dlga_pop2_loc_status_center:steward_menu:cond`
- **Scripts:** `center_base_income_change`, `get_prosperity_text_to_s50`, `get_improvement_details`, `calculate_weekly_party_wage`, `calculate_hero_weekly_net_income_and_add_to_wealth`
- **Menus:** `menu_center_income_report`, `menu_center_construction_report`, `menu_center_reports`, `menu_reports`
- **Dialogs:** `dlg:2431`, `dlg:3407`, `dlg:2307`
- **Slots:** `party:290`, `party:49`, `party:50`, `party:124`, `party:125`, `party:296`
- **Module-specific resources:** mesh: mesh_pic_pendor_rep_cityincome, mesh_pic_pendor_rep_cityconstruction
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `dis menu:center_income_report and menu:center_construction_report (full)`, `slot pop party 290: 17 accesses (writers pop2_location_improvements, center_base_income_change, tourney dialog)`, `dis strig:26: base income x4 into slot 49`, `sqlite refs: entry from menu:reports`
- **Overlaps:** `acan.culture_specific_fief_buildings`, `acan.latifundium_estates`, `ad457.center_buildings_management`, `ad457.lord_business_build_hire_upgrade`, `bi.ai_lords_build`, `bi.garrison_building_battle_bonuses`, `bi.roman_public_buildings`, `pop.fief_heartbeat_problems`, `pop.fief_improvements_expanded`, `pop.fief_stewards_with_skills`, `sw.recruit_unlock_buildings`, `vc.extended_center_improvements`

<a id="poprumor-system"></a>
### Procedural rumours and gossip with per-NPC cooldowns — pop (`pop.rumor_system`)

**What it does:** Tavernkeepers, travellers, ransom brokers, merchants and the player's steward tell randomly assembled rumours (who told it, what it is about, main-story hints), or say they have nothing new if asked again too soon. A mod option sets how often rumours refresh.

**How it works:** random_rumor_talk(kind, npc) (966 stmts) checks troop slot 157 (last rumour day) + $g_rumor_interval against the current day; if on cooldown builds a 'no news' line from 9 variants; otherwise picks a topic via rumor_topic (206 stmts) and a source via rumor_who_from (650 stmts), seeded by weekly $event_rand_* (update_event_rand), occasionally main_scenario_conversation_overheard, and stores the new day in slot 157. Entry: dlg:2695 tavernkeeper, dlg:2855 traveller, dlg:2778 ransom broker, dlg:3724 merchant, dlg:2287 steward gossip.

- **Hooks:** `dlg:2695:dlga_tavernkeeper_talk:tavernkeeper_rumors:conseq`, `dlg:2855:dlga_tavern_traveler_talk:tavern_traveler_rumors:conseq`, `dlg:2778:dlga_ransom_broker_talk:ransom_broker_rumors:conseq`, `dlg:3724:dlga_town_merchant_talk:merchant_gossip:conseq`, `dlg:2287:dlga_steward_menu:steward_gossip:conseq`
- **Scripts:** `random_rumor_talk`, `rumor_topic`, `rumor_who_from`, `main_scenario_conversation_overheard`, `update_event_rand`, `gender_to_reg63`
- **Presentations:** `prsnt_mod_options`
- **Dialogs:** `dlg:2287`, `dlg:2695`, `dlg:2778`, `dlg:2855`, `dlg:3724`
- **Slots:** `troop:157`
- **Globals:** `g_rumor_interval`, `event_rand_0`, `event_rand_1a`, `event_rand_1b`, `event_rand_2a`, `event_rand_2b`, `event_rand_2c`, `event_rand_3`, `event_rand_4`, `current_town`
- **Module-specific resources:** string: qstr_no_tidbits_of_value ... (9 'no news' lines), str_rumor_talk_* families
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `dis random_rumor_talk lines 0-60: slot 157 + g_rumor_interval cooldown, 'no news' variants`, `explain random_rumor_talk: 5 dialog callers, callees rumor_topic/rumor_who_from`

<a id="vccamp-and-report-screens"></a>
### Camp, character, faction and troop-tree report screens — vc (`vc.camp_and_report_screens`)

**What it does:** A presentation-based camp menu replaces many Native report menus: tabbed screens for the character (bio, wounds, honour, goal), followers/companions (morale, opinions), kingdom (lords, relations, armies, economy, centres, diplomacy, orders), ships, a full troop upgrade tree, and a troop detail screen that shows a troop's equipment and stats on a 3D model.

**How it works:** menu:camp opens prsnt_camp_screen_main (also _siege and _sea variants); tabs build text via ~30 texto_* scripts (texto_kingdomlords_info 154, texto_lords_relation 153, texto_partysize_morale 163, texto_kingdom_economy 100, texto_kingdom_armies 59, texto_companions_report 246, texto_global_camp_info 128...). prsnt_character_screen_main (engine-hooked via game_character_screen_requested) and prsnt_faction_screen_main. prsnt_troop_tree / prsnt_game_troop_tree draw upgrade trees with troop_tree_precurse/recurse; prsnt_troop_detail uses troop_detail_* (layout, stats, inventory, tooltips, dummy agent tableaux) to inspect any troop. prsnt_show_companions + companions_camp_conversation for companion talk.

- **Hooks:** `menu:camp`, `script:game_character_screen_requested`, `prsnt:camp_screen_main/t1`
- **Scripts:** `game_character_screen_requested`, `texto_kingdomlords_info`, `texto_lords_relation`, `texto_partysize_morale`, `texto_kingdom_economy`, `texto_kingdom_armies`, `texto_companions_report`, `texto_global_camp_info`, `troop_tree_precurse`, `troop_tree_recurse`, `troop_detail_layout`, `troop_detail_stats`, `troop_detail_inventory`, `troop_detail_update_dummy`, `companions_camp_conversation`, `store_wound_report`
- **Presentations:** `prsnt_camp_screen_main`, `prsnt_camp_screen_siege`, `prsnt_camp_screen_sea`, `prsnt_character_screen_main`, `prsnt_faction_screen_main`, `prsnt_followers_screen_camp`, `prsnt_troop_tree`, `prsnt_game_troop_tree`, `prsnt_troop_detail`, `prsnt_show_companions`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `sqlite refs: prsnt_camp_screen_main <- menu:camp; prsnt_troop_tree <- camp_screen_main/siege/sea; prsnt_troop_detail <- troop_tree/t3; prsnt_character_screen_main <- game_character_screen_requested`, `auto report: texto_* scripts each reached from one presentation`
- **Overlaps:** `acan.troop_detail_and_upgrade_trees`, `be.faction_troop_tree_viewer`, `bi.world_map_presentation`

<a id="acanplayer-permanent-camps"></a>
### Permanent field camps commanded by a companion, which store troops and loot, ransom your prisoners and attract bandits — acan (`acan.player_permanent_camps`)

**What it does:** Near a friendly town the player can found a permanent camp (paid in gold) and leave a companion in charge. The camp holds troops, prisoners and goods. Every few hours the commander sells the prisoners for you, and the more valuables are stored, the more bandits it attracts, so it can come under attack.

**How it works:** menu:create_pcamp checks gold, an available companion, a leadership-based camp limit and distance to the nearest centre (get_closest_center_and_minor), then calls set_player_camp_commander (party slots 25/26, troop slots 10/28 on the commander; name '{s0}'s Camp'). menu:player_camp is the camp's own menu. strig:29 (every 6 h) runs pcamp_ransom_prisoners: it sells prisoners at game_get_prisoner_price and calls calc_player_camp_bandit_attraction (stored inventory value -> troop slots 32/33), which drives bandit raids defended in mst_camp_defend (with camp_defenders_move_to_defender_position). Dialogs let you replace the commander (replace_player_camp_commander) or disband the camp (disband_player_camp, cleanup_player_camp_slot); find_closest_player_camp and get_player_camp_scene support travel and scenes.

- **Hooks:** `menu:create_pcamp`, `menu:player_camp`, `strig:29`, `dlg:10253:dlga_player_camp_replace_confirm`, `dlg:10254:dlga_player_camp_disband_test_items`, `dlg:10260:dlga_player_camp_disband_full`
- **Scripts:** `set_player_camp_commander`, `replace_player_camp_commander`, `pcamp_ransom_prisoners`, `calc_player_camp_bandit_attraction`, `disband_player_camp`, `cleanup_player_camp_slot`, `cleanup_player_camp_commander`, `find_closest_player_camp`, `get_player_camp_scene`, `set_pcamp_banner_from_troop`, `camp_defenders_move_to_defender_position`
- **Menus:** `menu_create_pcamp`, `menu_player_camp`
- **Mission templates:** `mst_camp_defend`, `mst_camp`
- **Slots:** `party:25`, `party:26`, `party:89`, `troop:10`, `troop:28`, `troop:29`, `troop:31`, `troop:32`, `troop:33`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `explain acan menu:create_pcamp: texts 'too many active permanent camps', 'leadership skill does not allow', 'too far from {s0} for the camp to supply itself'`, `explain acan pcamp_ransom_prisoners: strig:29 every 6h, game_get_prisoner_price, debug '{s0} sold {reg1} {s1} for {reg0}'`, `explain acan calc_player_camp_bandit_attraction: callers menu:player_camp, disband dialog`, `compare set_player_camp_commander/pcamp_ransom_prisoners: acan only`
- **Overlaps:** `acw.walkable_party_camp`, `pop.camp_troop_review_drill`, `tld.camp_menu_actions`

<a id="perisnoautoloot-equipment-upgrade"></a>
### Companions auto-upgrade their gear from the loot pool — perisno (`perisno.autoloot_equipment_upgrade`)

**What it does:** From the loot-management menu the player can let heroes decide what to do with the loot: companions scan the pooled inventory and equip the best item they can use, then the pool is sorted.

**How it works:** menu:dplmc_manage_loot_pool option dplmc_auto_loot leads to menu:dplmc_auto_loot; its 'perform equipment upgrading' option calls dplmc_auto_loot_all, which loops over the party's companion stacks twice (trp_npc1..trp_khivachis) calling dplmc_auto_loot_troop with the pool troop. That script scores items with dplmc_get_item_score_with_imod and dplmc_scan_for_best_item_of_type and respects skills riding/shield/power draw/power throw. Finally troop_sort_inventory on the pool.

- **Hooks:** `menu:dplmc_manage_loot_pool/opt:dplmc_auto_loot:conseq`, `menu:dplmc_auto_loot/opt:dplmc_autoloot_yes:conseq`
- **Scripts:** `dplmc_auto_loot_all`, `dplmc_auto_loot_troop`, `dplmc_get_item_score_with_imod`, `dplmc_scan_for_best_item_of_type`, `dplmc_troop_can_use_item`, `dplmc_init_item_base_score`, `dplmc_init_item_difficulties`
- **Slots:** `troop:155`, `troop:156`, `troop:157`, `troop:158`, `troop:159`, `troop:160`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis perisno dplmc_auto_loot_all: 12 stmts, two loops over companion stacks calling dplmc_auto_loot_troop, then troop_sort_inventory`, `refs perisno menu menu_dplmc_auto_loot: reached from menu:dplmc_manage_loot_pool/opt:dplmc_auto_loot`, `explain perisno dplmc_auto_loot_troop: 172 stmts, inventory 80%, callees dplmc_get_item_score_with_imod, dplmc_scan_for_best_item_of_type`, `similar perisno dplmc_auto_loot_troop --mods: shape 97% match in another registered module, so it is shared code rather than Perisno-original`
- **Notes:** Oddity: the script is shared with other registered modules (shape 97%).

<a id="acwwse-break-loop-opcode8"></a>
### WSE break_loop (opcode 8) in the imprisoned-companion traveller dialog — acw (`acw.wse_break_loop_opcode8`)

**What it does:** The only non-vanilla opcode in ACW: two uses of opcode 8 inside the traveller dialog that tells you where an imprisoned companion is held. It is a real engine-extension statement (WSE/WSE2 loop break), not corrupt data; it only exits the town search early.

**How it works:** dlg:2207 dlga_tavern_traveler_companion_location_tell -> tavern_traveler_pretalk (cond): when the companion is a prisoner and not in a party, try_for_range :l3 p_town_1..p_salt_mine; party_count_prisoners_of_type > 0 -> assign :l0 = :l3 -> opcode 8 with 0 operands, then try_end. Both occurrences sit at the identical 'found it, stop' position. Opcode 8 is absent from the tool's vanilla opcode table; in the WSE/WSE2 header it is the loop-break operation. Without WSE the statement is unknown to the engine (likely ignored or logged), so the loop would simply continue and report the LAST matching town instead of the first - harmless.

- **Hooks:** `dlg:2207:dlga_tavern_traveler_companion_location_tell:tavern_traveler_pretalk:cond`
- **Scripts:** `wse_chat_message_received`, `wse_console_command_received`, `wse_game_saved`, `wse_savegame_loaded`, `wse_window_opened`, `wse_get_agent_scale`
- **Slots:** `troop:8`, `troop:12`
- **Globals:** `temp`
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `auto report: NON-VANILLA OPCODES {8: 2}`, `dis acw dlg:2207... shows (UNKNOWN_op8) at stmts 24 and 32 right after (assign, :l0, :l3)`, `raw conversation.txt: '... 2133 2 <l0> <l3> 8 0 3 0 ...' (well-formed 0-operand statement followed by try_end)`, `FAQ.txt tells users to run the mod with WSE2; 9 wse_* handler scripts exist (all empty/unreached stubs)`, `changelog: 'Fixed the bugged dialogue when paying travelers to tell you the location of an imprisoned companion' = the edit that introduced it`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/module_dialogs.py 22382 and 22392 `(break_loop),` inside the traveller companion-location search`, `src = ACW Revived 4.0.18/_module_system_source/acwr module system/header_operations.py 1904 `break_loop = 8 #(break_loop), #Break out of a loop` in the WSE2 block ('Add the following definitions to the end (!) of header_operations.py')`, `source scan: of the 399 names in the shipped WSE2 operation block, every hit other than break_loop is a vanilla operation re-declared with optional extra arguments (position_rotate_*, key_*_clicked, add_point_light...); no WSE trigger id (-100..-108), no is_vanilla_warband / store_wse_version - consistent with opcheck (op 8 only)`

<a id="ad457per-faction-ai-recalculation"></a>
### Targeted per-kingdom AI recalculation instead of world-wide rethinks — ad457 (`ad457.per_faction_ai_recalculation`)

**What it does:** When something changes for a kingdom (war or peace, a treaty, a centre changing hands, a lord changing sides, a battle result, a marshal change), 457 AD re-plans only the kingdoms involved, immediately, instead of setting Native's 'recalculate everything' flag that makes every kingdom and every lord re-plan. A slow round-robin also refreshes one kingdom per tick. This keeps campaign AI responsive and cheaper on big maps.

**How it works:** recalculate_ais_for_faction(faction) (13 stmts): for kingdoms (fac_player_supporters_faction..fac_manhunters) and minor factions -> init_ai_calculation_new(faction) (re-computes party strengths and nearby friend/enemy strengths only for that faction's lord parties, its centres and the player) -> decide_faction_ai(faction) -> calculate_troop_ai for that faction's lords only. 39 call sites replace Native's $g_recalculate_ais flag: diplomacy_start_war/peace_between_kingdoms and every dplmc_start_*_between_kingdoms (both factions), give_center_to_faction, change_troop_faction, player_join/leave_faction, activate_player_faction, game_event_simulate_battle, event_player_captured_as_prisoner, process_hero_ai, cf_launch_rebellion, marshal/feast/call-to-arms dialogs. strig:41 also calls it for one faction per tick. The global recalculate_ais remains only on the debug 'Force rethink for all factions' option.

- **Hooks:** `strig:41`, `script:diplomacy_start_war_between_kingdoms`, `script:give_center_to_faction`, `script:game_event_simulate_battle`
- **Scripts:** `recalculate_ais_for_faction`, `init_ai_calculation_new`, `decide_faction_ai`, `calculate_troop_ai`, `party_calculate_strength`, `party_calculate_and_set_nearby_friend_enemy_follower_strengths`
- **Dialogs:** `dlg:1356`, `dlg:2229`, `dlg:2234`, `dlg:2481`, `dlg:2829`
- **Slots:** `troop:2`, `troop:10`, `faction:21`
- **Globals:** `checked_faction`
- **Relation to Native:** replaces-native
- **Confidence:** confirmed
- **Evidence:** `dis ad457 recalculate_ais_for_faction and init_ai_calculation_new`, `callers ad457 recalculate_ais_for_faction: 39 call sites (diplomacy, centre transfer, battles, dialogs)`, `callers ad457 recalculate_ais: only menu:faction_orders/opt:faction_orders_rethink_all`
- **Overlaps:** `be.async_round_robin_campaign_ai`, `bi.courage_update_staggering`

<a id="beasync-round-robin-campaign-ai"></a>
### Round-robin ('async') campaign processing instead of hourly bulk loops — be (`be.async_round_robin_campaign_ai`)

**What it does:** Heavy campaign-map jobs that Native runs for every lord/centre at once on an hourly tick are spread out: near-every-frame triggers each process ONE lord, centre or faction and advance a cursor, so the map does not hitch on the hour even with many lords.

**How it works:** Pattern: a simple trigger with interval 0.001 h or 0 clamps a cursor global into [first,last), increments it, wraps, and calls the worker for that one entity. strig:35 -> async_process_alarms (one centre: Native process_alarms logic, slots party 55/66/67), async_allow_vassals_to_join_indoor_battle (one lord), async_process_kingdom_parties_ai (one lord; body now empty because PAS took over). strig:29 -> async_init_ai_calculation (party_calculate_strength / party_calculate_and_set_nearby_friend_enemy_follower_strengths for one lord, one centre, main party). strig:22 (0.01 h) one lord's centre-related income/AI (honours game_get_reduce_campaign_ai). strig:116 one faction pair for create_random_war_peace + provocation/relation/alliance rolls. strig:124 one faction per tick through pps_faction_iteration; strig:126 one centre through pes_center_iteration; strig:128 machine-gun top-up; strig:130 two lords per tick through pas_ai_lord_decide; strig:123 one faction's uniform update. Native process_alarms, process_kingdom_parties_ai, allow_vassals_to_join_indoor_battle are absent; create_village_farmer_party, calculate_castle_prosperities_by_using_its_villages emptied.

- **Hooks:** `strig:35`, `strig:29`, `strig:22`, `strig:116`, `strig:123`, `strig:124`, `strig:126`, `strig:128`, `strig:130`
- **Scripts:** `async_process_alarms`, `async_allow_vassals_to_join_indoor_battle`, `async_process_kingdom_parties_ai`, `async_init_ai_calculation`, `async_recalculate_ais`, `async_randomly_start_war_peace_new`, `async_calculate_castle_prosperities_by_using_its_villages`
- **Slots:** `party:55`, `party:66`, `party:67`, `troop:2`, `troop:8`, `troop:10`
- **Globals:** `async_process_alarms_1`, `async_process_alarms_2`, `async_allow_vassals_to_join_indoor_battle`, `async_process_kingdom_parties_ai`, `async_init_ai_calculation_1`, `async_init_ai_calculation_2`, `async_init_ai_calculation_3`, `async_init_ai_calculation_4`, `async_simple_trigger5`, `async_simple_trigger10`, `async_simple_trigger26`, `async_simple_trigger31`, `async_simple_trigger32`, `async_simple_trigger33`, `async_simple_trigger34`, `async_simple_trigger35`, `async_randomly_start_war_peace_new_cur_kingdom`, `async_randomly_start_war_peace_new_cur_kingdom_2`
- **Relation to Native:** replaces-native
- **Confidence:** confirmed
- **Evidence:** `dis be strig:35, strig:29, strig:130, strig:124, strig:126: cursor-clamp-increment-wrap pattern`, `dis be async_process_alarms (161 stmts) vs Native process_alarms (157)`, `auto report: Native scripts absent here: allow_vassals_to_join_indoor_battle, process_alarms, process_kingdom_parties_ai`
- **Overlaps:** `ad457.per_faction_ai_recalculation`, `bi.courage_update_staggering`

<a id="bicourage-update-staggering"></a>
### Battle morale recalculation spread over three ticks (performance) — bi (`bi.courage_update_staggering`)

**What it does:** Native's every-3-seconds morale pass compares every soldier with every other soldier, which lags big battles. BI processes only a third of the soldiers each pass, cutting that cost to a third.

**How it works:** apply_effect_of_other_people_on_courage_scores (called from mst:lead_charge/t19 every 3s) cycles $courage_update_phase 0-2 and only updates agents whose id mod 3 equals the phase; the inner all-agents loop is unchanged.

- **Hooks:** `mst:lead_charge/t19:cond`
- **Scripts:** `apply_effect_of_other_people_on_courage_scores`
- **Globals:** `courage_update_phase`
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Evidence:** `dis bi apply_effect_of_other_people_on_courage_scores @0-8`, `global bi courage_update_phase: sole writer/reader is that script`
- **Overlaps:** `acw.battle_cry_rout`, `acw.bury_the_dead`, `ad457.per_faction_ai_recalculation`, `be.async_round_robin_campaign_ai`, `be.company_discipline_rout`, `nw.morale_rout_rally`, `tld.battle_coherence_rout_rally`, `vc.battle_immersion_courage`

<a id="vcsavegame-content-update"></a>
### On-load savegame repair and content-update migration — vc (`vc.savegame_content_update`)

**What it does:** Every time the game returns to the world map, VC runs a large maintenance trigger: it repairs known save corruptions (banners, item info, a v2.049 bug with a dedicated 'your save is ruined' menu) and, once per save, migrates old saves to a content update (new globals, parties, troops, items) so players don't need a new game.

**How it works:** strig:165 has interval -75, which is the ti_on_switch_to_map event (not a periodic timer). Its 932 statements reset mission globals, re-run initialize_item_info, fix banners (give_troop_next_banner, 'fixing banners'), re-apply titles, food consumption, marshal checks, jump to menu_reconstruct_pre2049 when a known-corrupted state is detected, and finally - when neither $game_started_with_content_update nor $game_updated_to_content_update is 1 - call update_savegame_to_content_update (138 stmts: sets ~20 new globals, fixes p_ferry_4a/4b, jetties, tunics, ransom brokers, qst_vc_menu, prints 'Content update applied').

- **Hooks:** `strig:165`, `strig:137`
- **Scripts:** `update_savegame_to_content_update`, `initialize_item_info`, `give_troop_next_banner`, `troop_set_title_according_to_faction`, `appoint_faction_marshal`, `add_jetty_system_2`, `setup_debug_log`
- **Menus:** `menu_reconstruct_pre2049`
- **Slots:** `party:29`, `party:44`, `party:72`, `party:74`, `party:75`
- **Globals:** `game_started_with_content_update`, `game_updated_to_content_update`, `savegame_id`, `g_sgfix`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis vc strig:165 header: interval -75.0 (= ti_on_switch_to_map); stmt 78 jump_to_menu menu_reconstruct_pre2049; stmts 928-930 content-update gate -> update_savegame_to_content_update`, `sqlite refs/globals update_savegame_to_content_update: writes savegame_id, goal_type, g_sgfix...; refs p_ferry_4a/4b, qst_vc_menu`, `Changelog 2.025 'reinitialize item info (wiped out in someone's save game by unknown cause)'`

<a id="acanad457-base-inherited"></a>
### Inherited 457 AD base: lord business AI, sandbox ruler/vassal start, character creation (with acan's changes) — acan (`acan.ad457_base_inherited`)

**What it does:** A pointer record for systems acan takes from 457 AD, with what acan changed. AI lords spending wealth in their fiefs, starting as a king or vassal, the character-creation skill screen, the barracks screen and siege planning all come from the ad457 base.

**How it works:** (1) inherits ad457.lord_business_build_hire_upgrade: troop_does_business_in_center (acan 420 vs ad457 323 stmts, 66% shape). acan adds faction-budget postings (add_to_faction_bugdet), decree enact/revoke decisions and party_get_ideal_size sizing, and drops ad457's calculate_equipment_limit gear-upgrade step. (2) inherits ad457.royal_and_lord_sandbox_start: player_is_king is largely rewritten (15% shape). acan's version also triggers its story events (cf_start_jewish_revolt, cf_start_iazyges_invasion, cf_start_batava_revolt, start_year_of_four) from prsnt:select_kingdom, and player_is_lord is 74%. (3) mcc_generate_skill_set character creation is 88% (minor content changes). (4) inherits ad457.barracks_recruitment_screen, which acan reworked for cohorts (see acan.legions_cohorts_army_organisation). (5) inherits ad457.vc_siege_planning_and_camp_events_inherited (see acan.siege_planning_inherited).

- **Hooks:** `script:troop_does_business_in_center`, `prsnt:select_kingdom/t1`, `prsnt:barracks/t0`
- **Scripts:** `troop_does_business_in_center`, `player_is_king`, `player_is_lord`, `mcc_generate_skill_set`, `improve_center`, `decide_decree_enact`, `add_to_faction_bugdet`
- **Presentations:** `prsnt_select_kingdom`, `prsnt_barracks`
- **Slots:** `troop:52`, `party:46`
- **Globals:** `g_campaign_type`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `compare --mods acan,ad457: troop_does_business_in_center 66%, player_is_king 15%, player_is_lord 74%, mcc_generate_skill_set 88%`, `callees acan vs ad457 troop_does_business_in_center: acan adds add_to_faction_bugdet, decide_decree_enact/revoke, party_get_ideal_size; ad457 has calculate_equipment_limit`, `explain acan player_is_king: callees cf_start_jewish_revolt, cf_start_iazyges_invasion, cf_start_batava_revolt, start_year_of_four`

<a id="acanseasonal-light-fog-weather"></a>
### Month-based scene light, regional fog and snow in battle and town scenes — acan (`acan.seasonal_light_fog_weather`)

**What it does:** Scenes are lit according to the in-game month, fog is set per region and situation, snow appears in winter outside desert and Mediterranean regions, and clothing layers react to the weather.

**How it works:** calculate_season_light (447 call sites, every frame in 149 templates) reads $g_cur_month. change_scene_fog (1770 call sites, ti_before_mission_start in 118 templates) sets fog by region (get_region_of_pos22, 123 callers, 95% shape with ad457) and time. cf_snow_on_scene (649 call sites) and cf_is_desert_or_mediterreanian gate snow and winter visuals. menu:winter is the winter notice on the map.

- **Hooks:** `mst:* every 0s (calculate_season_light)`, `mst:* ti_before_mission_start (change_scene_fog)`, `menu:winter`
- **Scripts:** `calculate_season_light`, `change_scene_fog`, `cf_snow_on_scene`, `cf_is_desert_or_mediterreanian`, `cf_is_desert`, `get_region_of_pos22`
- **Menus:** `menu_winter`
- **Globals:** `g_cur_month`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `explain acan calculate_season_light: 447 callers, reads g_cur_month`, `explain acan change_scene_fog: 1770 call sites`, `compare get_region_of_pos22: ad457 95%`
- **Overlaps:** `be.campaign_weather_battle_atmosphere`, `laigle.weather_seasons`, `nw.battle_weather_generator`, `tld.battle_condition_modifiers`, `tld.day_night_proficiency_shift`, `vc.seasons_scene_lighting`

<a id="acanskin-matched-clothing-wse"></a>
### Skin-tone-matched bare arms and legs on clothing items (uses WSE op 2749) — acan (`acan.skin_matched_clothing_wse`)

**What it does:** Tunics, dresses and armours add bare-arm and bare-leg meshes whose skin texture matches the wearer's face (pale, rugged or African), switching to covered limbs in snow.

**How it works:** set_roman_clothing / _2 / _3 and about 22 init_* scripts (init_roman_poor, init_eastern_troop, init_dress_*, init_pants_long...) run from ti_on_init_item item triggers (about 580 item-trigger blocks). For an agent they read the face keys with NON-VANILLA opcode 2749 (operands: string register, agent), else str_store_troop_face_keys for a troop. face_keys_get_face_texture then selects str_arms_bare / _rugged / _african meshes via cur_item_add_mesh, and cf_snow_on_scene adds winter clothing.

- **Hooks:** `itm:* ti_on_init_item (set_roman_clothing: 121 items)`
- **Scripts:** `set_roman_clothing`, `set_roman_clothing_2`, `set_roman_clothing_3`, `init_roman_poor`, `init_roman_rich`, `init_eastern_troop`, `init_dress_arms`, `init_pants_long`, `init_armor_merc`, `cf_snow_on_scene`
- **Globals:** `character_sheet_is_active`, `tableau_active`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis acan script:set_roman_clothing stmt 44: (UNKNOWN_op2749, 70, :l0) in agent branch; else str_store_troop_face_keys`, `grep UNKNOWN_op2749: 24 clothing/init scripts + assign_household_cook/slave`

<a id="awoiafhunting-herds"></a>
### Wild animal herds on the map and hunting battles — awoiaf (`awoiaf.hunting_herds`)

**What it does:** Deer, boar, wolf, goat and wild-donkey herds roam the campaign map. Encountering one opens a menu to hunt; the hunt is a small mission where animals flee as mounted 'agents'. Kills yield meat and raw leather.

**How it works:** spawn_bandits keeps N herds alive per type (store_num_parties_of_template pt_deer_herd < 3 -> spawn_around_party p_deer_spawn_point; pt_boar_herd < 2, ...). game_event_party_encounter routes herd encounters to menu_deer_herd / boar_herd / wolf_herd / coat(b)_herd / wilddonkey_herd; 'Hunt' launches mst_deer_hunting etc., where trp_deer riders on itm_deer 'horse' items act as the animals; the herd menus hand out itm_deer_meat / itm_raw_leather; *_kill_end menus just return.

- **Hooks:** `script:game_event_party_encounter`, `menu:deer_herd/opt:deer_kill:conseq`
- **Scripts:** `spawn_bandits`, `game_event_party_encounter`
- **Menus:** `menu_deer_herd`, `menu_boar_herd`, `menu_wolf_herd`, `menu_coat_herd`, `menu_coatb_herd`, `menu_wilddonkey_herd`
- **Mission templates:** `mst_deer_hunting`, `mst_boar_hunting`, `mst_wolf_hunting`, `mst_coat_hunting`, `mst_coatb_hunting`, `mst_wilddonkey_hunting`
- **Module-specific resources:** pt: pt_deer_herd, pt_boar_herd, pt_wolf_herd; troop: trp_deer; item: itm_deer, itm_deer_meat, itm_raw_leather
- **Relation to Native:** modifies-native
- **Confidence:** strongly-inferred
- **Evidence:** `dis spawn_bandits stmt 262-275 (pt_deer_herd / pt_boar_herd spawn caps)`, `refs menu_deer_herd <- game_event_party_encounter; refs mst_deer_hunting <- menu:deer_herd/opt:deer_kill`, `sqlite refs: mst:deer_hunting uses itm_deer/trp_deer; menu:deer_herd references itm_deer_meat, itm_raw_leather`
- **Overlaps:** `acw.hunting`, `tld.wilderness_encounters_hide_animal_ambush`

<a id="becampaign-weather-battle-atmosphere"></a>
### Regional weather report and battle sky, rain, fog and ambience — be (`be.campaign_weather_battle_atmosphere`)

**What it does:** The campaign tracks weather for northern, middle and southern Europe (temperature, pressure, humidity, wind, clouds, precipitation) shown in a weather report menu; battles pick a matching sky, rain intensity and fog, and play layered positional ambience (rain left/right, birds, wind, terrain- and time-specific loops, tavern ambience).

**How it works:** pws_* globals per region (pws_n_/pws_m_/pws_s_ temperature, pressure, humidity, wind, clouds, precipitation) displayed by menu_weather_report. In battle: mst:lead_charge/t64 (ti_before_mission_start, 276 stmts) randomises ambience seeds, set_rain 0, set_fog_distance, picks $current_sky; t60 (156 stmts, once) if cf_current_sky_can_rain and seed <= $current_precipitation sets rain intensity and spawns invisible spr_ambience_prop emitters (rain left/right, front/back/left/right, sky) playing looped sounds chosen by terrain and time of day; t61-t63 move the emitters with the camera and fire random one-shot ambience. cf_current_sky_has_no_direct_sunlight used by a prop trigger.

- **Hooks:** `mst:lead_charge/t64:cond`, `mst:lead_charge/t60:cond`, `mst:lead_charge/t61:cond`, `mst:lead_charge/t62:cond`, `mst:lead_charge/t63:cond`, `menu:weather_report`
- **Scripts:** `cf_current_sky_can_rain`, `cf_current_sky_has_no_direct_sunlight`
- **Menus:** `menu_weather_report`
- **Globals:** `pws_n_temperature`, `pws_m_precipitation`, `pws_s_wind`, `current_sky`, `current_precipitation`, `g_rain_intensity`, `g_rain_state`, `current_fog_distance`, `ambience_sound_type`, `ambience_prop_rain_left`, `ambience_prop_rain_right`
- **Module-specific resources:** spr: spr_ambience_prop; sound: snd_ambience_rain1_left, snd_ambience_rain1_right, (ambience loops)
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `explain be menu:weather_report (pws_* globals, text 'Temperature ... Pressure ... Humidity ... Wind')`, `dis be mst:lead_charge/t60:cond, t64:cond`
- **Overlaps:** `acan.seasonal_light_fog_weather`, `laigle.weather_seasons`, `nw.battle_weather_generator`, `tld.battle_condition_modifiers`, `tld.day_night_proficiency_shift`, `vc.seasons_scene_lighting`

<a id="cblcampaign-balance-retune"></a>
### Campaign balance retune (party size, food, morale, rewards) — cbl (`cbl.campaign_balance_retune`)

**What it does:** A set of number changes against its base module: much larger parties from leadership and renown, far lower food use, stronger leadership morale, bigger tournament prizes, a stronger starting character, lords tolerating worse relations before leaving, a changed village-improvement cost/time formula and thinner merchant stock.

**How it works:** game_get_party_companion_limit: leadership x8 (base x5), renown/12 (base /25). strig:59 food: daily, one food item per 12 men (base every 14 h, per 3 men). get_player_party_morale_values: leadership morale x30/x20 (base x15/x12). faction_follows_controversial_policy: -15 instead of -3/-3. strig:35: lord relation threshold -90 (base -50). menu:town_tournament_won: 8000 denars, +30 renown, +15 relation, 2000 xp (base 200/25/10/1000). menu:choose_skill begin_adventuring: +4 to all four attributes, inventory management +6 and several skills. menu:center_improve: changed cost/time formula. refresh_center_weaponsmiths/stables: merchandise counts cut (e.g. 15 -> 5, horses 35 -> 15). strig:27 drops the truce/alliance/defensive/trade/casus-belli expiry notification pop-ups (log only).

- **Hooks:** `strig:59`, `strig:35`, `strig:27`, `menu:town_tournament_won`, `menu:choose_skill/opt:begin_adventuring:conseq`, `menu:center_improve`
- **Scripts:** `game_get_party_companion_limit`, `get_player_party_morale_values`, `faction_follows_controversial_policy`, `refresh_center_weaponsmiths`, `refresh_center_stables`
- **Menus:** `menu_town_tournament_won`, `menu_choose_skill`, `menu_center_improve`
- **Globals:** `$g_player_party_morale_modifier_leadership`
- **Relation to Native:** modifies-native
- **Confidence:** confirmed
- **Overlaps:** `acan.spawn_equipment_variety_and_item_quality`

<a id="cblcustom-field-battle-scenes"></a>
### 93 hand-made field battle scenes by terrain — cbl (`cbl.custom_field_battle_scenes`)

**What it does:** Field battles no longer always use a randomly generated terrain: depending on the terrain under the player's party, the battle loads one of 93 hand-built scenes (11 steppe, 20 plain, 10 plain-mountain, 5 plain-river, 11 plain-forest, 10 desert, 5 desert-forest, 11 snow, 5 snow-forest, 5 steppe-forest).

**How it works:** setup_random_scene (350 stmts vs the base module 34) reads party_get_current_terrain p_main_party, rolls 1..99 and picks scn_random_scene_<terrain>_custom_N by probability band (e.g. steppe: 10% each for 1-9, 5% for 10 and 11; plain: 3% bands across 20 plain and 10 plain-mountain scenes ...). Unhandled terrains fall back to the Native scn_random_scene_<terrain> generators; terrain 0 -> scn_water; terrain 7 (sea lane) -> mst_ship_battle on scn_sea_1/2/4 by battle size (same as the base module). Called from the 9 battle-start menu options (simple_encounter, join_battle, camp walk-around).

- **Hooks:** `menu:simple_encounter/opt:encounter_attack:conseq`, `menu:simple_encounter/opt:follow:conseq`, `menu:simple_encounter/opt:hold:conseq`, `menu:simple_encounter/opt:do_orders:conseq`, `menu:join_battle/opt:join_attack:conseq`, `menu:join_battle/opt:follow:conseq`, `menu:join_battle/opt:hold:conseq`, `menu:join_battle/opt:do_orders:conseq`, `menu:camp_action/opt:action_walk_around:conseq`
- **Scripts:** `setup_random_scene`
- **Module-specific resources:** scene: scn_random_scene_steppe_custom_1..11, scn_random_scene_plain_custom_1..20, scn_random_scene_plain_mountain_custom_1..10, scn_random_scene_plain_river_custom_1..5, scn_random_scene_plain_forest_custom_1..11, scn_random_scene_desert_custom_1..10, scn_random_scene_desert_forest_custom_1..5, scn_random_scene_snow_custom_1..11, scn_random_scene_snow_forest_custom_1..5, scn_random_scene_steppe_forest_custom_1..5; file: SceneObj/scn_random_scene_*_custom_*.sco (93)
- **Relation to Native:** replaces-native
- **Confidence:** confirmed
- **Overlaps:** `acw.custom_battle_historical_scenarios`, `laigle.size_aware_battlefields`, `tld.region_tracking_and_battle_scenes`

<a id="nwmp-only-systems"></a>
### Multiplayer-only systems (catalogue) — nw (`nw.mp_only_systems`)

**What it does:** Large parts of NW only make sense with human players and run only in multiplayer missions: sapper construction with team build points, battle royale weapon boxes, conquest/HQ flags, medics and bandages, musicians (drum/fife/bagpipe/piano) and multi-agent music sync, spyglass and drinking animations, admin/cheat/poll tools, rank-by-score, team balancing and teamkill penalties, troop/class availability limits.

**How it works:** Entry points are the ten mst_multiplayer_* templates and script game_receive_network_message (2771 stmts). Examples: multiplayer_server_construct_prop (reached only from itm_french_bomb and network messages), multiplayer_server_send_build_points, royale_* scripts (mst_multiplayer_br), server_handle_bandages_hit (MP templates only), multiplayer_server_agent_play_music (mst_multiplayer_cb + network), multiplayer_server_agent_use_spyglass (prsnt_spyglass_dummy + network), check_troop_availability / random_item_selection / quick_assign_item (MP item/troop select presentations), multiplayer_server_on_player_teamkilled_player.

- **Hooks:** `script:game_receive_network_message`, `mst:multiplayer_br/t4:conseq`
- **Scripts:** `multiplayer_server_construct_prop`, `multiplayer_server_send_build_points`, `royale_initialise_boxes`, `royale_initialise_cannons`, `royale_spawn_box`, `multiplayer_server_royale_use_weaponbox`, `server_handle_bandages_hit`, `multiplayer_server_agent_play_music`, `multiplayer_server_agent_stop_music`, `multiplayer_server_agent_use_spyglass`, `multiplayer_agent_drinking`, `check_troop_availability`, `random_item_selection`, `multiplayer_get_troop_rank`, `conquest_get_flag_name`, `multiplayer_server_on_player_teamkilled_player`
- **Presentations:** `prsnt_multiplayer_construct`, `prsnt_multiplayer_music`, `prsnt_spyglass_dummy`, `prsnt_drinking`, `prsnt_multiplayer_admin_chat`, `prsnt_multiplayer_cheat_menu`, `prsnt_conquest_flag_select`, `prsnt_multiplayer_medic_icons`
- **Mission templates:** `mst_multiplayer_dm`, `mst_multiplayer_tdm`, `mst_multiplayer_hq`, `mst_multiplayer_cf`, `mst_multiplayer_sg`, `mst_multiplayer_bt`, `mst_multiplayer_cb`, `mst_multiplayer_duel`, `mst_multiplayer_kh`, `mst_multiplayer_br`, `mst_multiplayer_cm`
- **Slots:** `player:40-51`, `agent:12-37`
- **Globals:** `g_team_1_build_points`, `g_team_2_build_points`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `roots nw for each listed script: only mst_multiplayer_* / game_receive_network_message / MP presentations (spyglass and drinking scripts carry an SP-inclusive guard but are only started from MP presentation flows)`, `roots nw multiplayer_server_construct_prop: itm:itm_french_bomb + game_receive_network_message`

<a id="oa1860cae-native-baseline"></a>
### Older-Native base shared with L'Aigle and CAE — oa1860 (`oa1860.cae_native_baseline`)

**What it does:** Almost all of 1860s' 155 'modified Native' scripts are not 1860s work: they are an older Native version that the CAE module and L'Aigle also run. 1860s itself only changed about ten scripts, nearly all multiplayer or custom-battle content.

**How it works:** Shape-hash classification of the 155 modified scripts: 145 have the same shape as CAE's copy - 71 of those are Native-shaped and differ only in renamed resource names, 74 are genuinely older-Native code (60 of them also shared with L'Aigle) - and only 10 differ from both CAE and Native: game_receive_network_message, game_quick_start (custom battles, 'Gabrilduro's special Custom Battles'), game_start, initialize_item_info, determine_team_flags (multiplayer CTF/HQ flags for kingdoms 7-10), money_management_after_agent_death (multiplayer) plus 4 other multiplayer scripts. The one 'new' script, center_change_trade_good_production, is unreachable and also present in L'Aigle.

- **Hooks:** `script:game_quick_start`, `script:determine_team_flags`
- **Scripts:** `game_quick_start`, `determine_team_flags`, `initialize_item_info`, `center_change_trade_good_production`
- **Relation to Native:** replaces-native
- **Confidence:** confirmed
- **Evidence:** `sqlite shape_hash classification oa1860 vs native/cae/laigle (counts above)`, `diff native vs oa1860 determine_team_flags (only multiplayer flag props added)`

<a id="perisnoarray-library"></a>
### Script-level array library on hidden temp parties — perisno (`perisno.array_library`)

**What it does:** A small data-structure library (create, get, set, insert, push, shift, remove, owner, size, version) used by the trade ledger; most of its functions are never called.

**How it works:** Arrays are stored in slots of p_temp_party-style holder parties (party slots 996-999 for ledger arrays) with its owner and version stored alongside. array_create prints 'array[N] created'. Of about 30 array_* and cf_array_* scripts only a handful are reached (from the ledger menu/presentation); the rest are flagged UNREACHED by the tool.

- **Hooks:** `menu:town_trade_assessment`, `prsnt:trade_ledger_basic/t2`
- **Scripts:** `array_create`, `array_get_element`, `array_set_element`, `array_pushback`, `array_insert`, `array_p_shift_range`, `cf_array_get_element`, `cf_array_is_array`, `cf_array_remove`
- **Slots:** `party:996`, `party:997`, `party:998`, `party:999`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `explain perisno array_create: slots party[996..999], caller trade_ledger_create, text 'array[{reg0}] created'`, `report perisno New scripts list: array_clear, array_insert_n, array_pushfront, array_remove_n marked UNREACHED; array_get_element 19 callers`, `explain perisno prsnt:trade_ledger_basic/t0: calls array_get_element, array_get_size, array_pushback`

<a id="perisnohard-mode-and-fog-of-war"></a>
### Start-of-game hard mode and fog of war toggles — perisno (`perisno.hard_mode_and_fog_of_war`)

**What it does:** At new-game start the player can toggle Hard Mode (harsher rules such as lost items when captured, wider effects on wages and recruiting) and Fog of War (fief locations hidden until revealed, e.g. by reading regional maps sold as items).

**How it works:** menu:start_game_0_5 has options hard_mode and fog_of_war that flip $g_hard_mode / $g_fog_of_war, with the current state printed in s10 and a summary text. g_hard_mode is read in 39 blocks (village elder recruit dialogs, ladder construction, game_get_troop_wage, spawn scripts). Map items' tooltips say they reveal fiefs if Fog of War is active (game_get_item_extra_text).

- **Hooks:** `menu:start_game_0_5/opt:hard_mode:conseq`, `menu:start_game_0_5/opt:fog_of_war:conseq`
- **Scripts:** `game_get_troop_wage`, `game_get_item_extra_text`, `spawn_rebels`
- **Menus:** `menu:start_game_0_5`
- **Globals:** `g_hard_mode`, `g_fog_of_war`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `global perisno g_hard_mode: 2 writers (menu:start_game_0, hard_mode option), 39 readers`, `global perisno g_fog_of_war: 3 writers (start menus), 6 readers (same menu)`, `text fog.of.war --mods perisno: 8 hits; regional map item tooltips used by script:game_get_item_extra_text; 'Hard mode is Active / Fog of War is permanently active' in menu:start_game_0_5`

<a id="perisnohunting-missions"></a>
### Hunting animal herds on the map — perisno (`perisno.hunting_missions`)

**What it does:** Map events present deer and boar herds that the player can hunt in a dedicated hunting scene.

**How it works:** menu:deer_herd option deer_kill and menu:boar_herd option boar_kill start mst_deer_hunting / mst_boar_hunting (plus wolf, coat and wild-donkey variants exist as mission templates). The mission triggers handle agent behaviour (deer_hunting/t0 runs every frame and prints a taunt text); kill counting and rewards were not traced.

- **Hooks:** `menu:deer_herd/opt:deer_kill:conseq`, `menu:boar_herd/opt:boar_kill:conseq`
- **Mission templates:** `mst_deer_hunting`, `mst_boar_hunting`, `mst_wolf_hunting`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `refs perisno mt mst_deer_hunting: 1 reference, menu:deer_herd/opt:deer_kill:conseq`, `refs perisno mt mst_boar_hunting: 1 reference, menu:boar_herd/opt:boar_kill:conseq`, `report perisno lists mst_wolf_hunting, mst_coat_hunting, mst_wilddonkey_hunting as not in Native`, `mission trigger bodies not disassembled`

<a id="swbattle-start-speeches"></a>
### Faction battle-start speech and shouts — sw (`sw.battle_start_speeches`)

**What it does:** At the start of field and custom battles a faction-specific speech/cheer plays (Empire, Rebel, Hutt, independent), with a second shout a few seconds later.

**How it works:** mst:lead_charge/t13 (1.39 s) and t40/t41 call battle_speech(type), which picks sound 288-312 by the player faction's culture (faction 15 slot 9) and play_sound.

- **Hooks:** `mst:lead_charge/t13:conseq`, `mst:lead_charge/t40:conseq`, `mst:custom_battle/t3:conseq`
- **Scripts:** `battle_speech`
- **Mission templates:** `mst_lead_charge`, `mst_custom_battle`, `mst_custom_battle_2vs2`, `mst_custom_battle_standard`
- **Slots:** `faction:9`
- **Module-specific resources:** sound: snd 288-312 (speech banks)
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `dis sw battle_speech (sound by culture)`, `explain sw battle_speech: 9 callers`
- **Overlaps:** `acw.order_voice_callouts`, `bi.battle_event_messages`, `nw.fkey_order_tree`, `nw.objective_markers_hud`, `nw.voice_commands`

<a id="swcantina-blackjack-and-brawls"></a>
### Cantina blackjack and tavern brawls — sw (`sw.cantina_blackjack_and_brawls`)

**What it does:** The player can play blackjack for credits against companions or lords from dialogue (hit / stay / double, natural-21 bonus and dealer-perfect penalty), and provoke cantina brawls in which every patron fights on a random side.

**How it works:** Dialogue options (dlg member_question_2_blackjack_3, lord_blackjack_3) start prsnt_blackjack (t0 136 + t1 594 stmts: card deck in presentation state, betting overlay, 'You have a perfect hand! You win 50% more...'). setup_tavern_brawl (from cantina walker dialogs) assigns every non-player agent to a random team 3-5, clears scripted mode, sets $g_init_fight and switches music.

- **Hooks:** `dlg:193:dlga_member_question_2_blackjack_3:close_window:conseq`, `dlg:556:dlga_lord_blackjack_3:close_window:conseq`, `dlg:1269:dlga_cantina_walkers_pre_brawl_4:close_window:conseq`, `prsnt:blackjack/t0`, `prsnt:blackjack/t1`
- **Scripts:** `setup_tavern_brawl`
- **Presentations:** `prsnt_blackjack`
- **Mission templates:** `mst_cantina_default`
- **Dialogs:** `dlga_member_question_2_blackjack_3`, `dlga_lord_blackjack_3`, `dlga_cantina_walkers_pre_brawl_4`
- **Globals:** `black_jack`, `tavern_brawl`, `g_init_fight`
- **Relation to Native:** new
- **Confidence:** confirmed
- **Evidence:** `grep sw start_presentation 21 -> two dialog conseqs`, `explain sw prsnt:blackjack/t1 texts`, `dis sw setup_tavern_brawl`
- **Overlaps:** `laigle.faro_card_game`

<a id="swspace-battle-minigame"></a>
### Space dogfight minigame (training ground only) — sw (`sw.space_battle_minigame`)

**What it does:** An experimental first-person fighter dogfight: the player flies a scene-prop ship with mouse/keys, shoots, and AI fighters chase and shoot back, with explosions and damage.

**How it works:** mst_space_battle (31 triggers): set_fighters, ai_viper_movements / ai_cylon_movements (scene-prop flight AI every 0.1 s), cf_ai_*_shot, calculate_fighter_damages, fighter_explosions; player input triggers move the camera-mounted prop. Reached only from menu:training_ground options space_entry / space_battle (set_jump_mission 43/44).

- **Hooks:** `menu:training_ground/opt:space_battle:conseq`, `mst:space_battle/t4:conseq`, `mst:space_battle/t25:conseq`, `mst:space_battle/t27:conseq`
- **Scripts:** `set_fighters`, `ai_viper_movements`, `ai_cylon_movements`, `cf_ai_viper_shot`, `cf_ai_cylon_shot`, `calculate_fighter_damages`, `fighter_explosions`
- **Mission templates:** `mst_space_battle`, `mst_space_battle_entry`, `mst_space_prop`
- **Globals:** `player_ship`, `player_speed`, `player_max_speed`, `player_rotate_x`, `player_rotate_y`, `player_rotate_z`, `player_missiles`, `player_cannons`, `player_damage`, `cam_follow`
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `sqlite names sw mt 43-45 = mst_space_battle_entry/mst_space_battle/mst_space_prop`, `grep sw set_jump_mission 43/44 -> only menu:training_ground`, `script names ai_viper_movements / ai_cylon_movements (Battlestar-Galactica placeholder names)`

<a id="vcseasons-scene-lighting"></a>
### Seasons that change scene lighting/shaders and map time — vc (`vc.seasons_scene_lighting`)

**What it does:** The year has seasons; every ten days a trigger advances the season, and every scene (towns, villages, battles) adjusts sun/ambient colours and season shader for spring, summer, autumn or winter. Season also feeds gameplay text such as harvest-time results when burning fields during a siege.

**How it works:** strig:138 (every 240.1h) advances $shader_season (also set at game_start; cheat menu option 'season'; menu_season_change). calculate_season_light (30 stmts, reads only $shader_season) is called from 85 mission templates' load triggers (town_default/t7, town_center/t9, lead_charge/t66...) and adjusts scene lighting per season. Siege menus campos_cercanos1-4 branch on harvest season. MP equivalent: scene_init_weather_and_sounds (MP templates only).

- **Hooks:** `strig:138`, `mst:lead_charge/t66:conseq`, `mst:town_center/t9:conseq`
- **Scripts:** `calculate_season_light`, `z_code_season`, `game_get_date_text`
- **Menus:** `menu_season_change`
- **Globals:** `shader_season`
- **Module-specific resources:** shader: VC season-aware shaders (mb.fx)
- **Relation to Native:** new
- **Confidence:** strongly-inferred
- **Evidence:** `sqlite globals shader_season: 102 reads, writers game_start, strig:138, z_code_season, cheat option`, `sqlite calls: calculate_season_light called from 85 templates`
- **Overlaps:** `acan.seasonal_light_fog_weather`, `be.campaign_weather_battle_atmosphere`, `laigle.weather_seasons`, `nw.battle_weather_generator`, `tld.battle_condition_modifiers`, `tld.day_night_proficiency_shift`
