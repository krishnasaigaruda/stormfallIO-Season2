# Stormfall Season 2: Deep Tide

A 3D battle royale that runs in your browser, built with three.js. Season 2 rebuilds Stormfall around the ocean: a bright tropical island with rolling hills, turquoise lagoons, coral reefs, palm beaches, a lighthouse, shipwrecks and giant sea-creature statues, plus a new crew of pirate and beach characters, sea-creature sidekicks, ocean-themed menus and a new soundtrack.

## What's new in Season 2

- **New island look:** rolling green hills, three inland lagoons, sandy beaches, clear tropical water with sun glitter and shore foam, puffy cloud banks, and a full day/night cycle in matches (morning, sunset, starry night, dawn).
- **Real 3D models everywhere:** round tropical trees, palms, coral and anemones, rocks and sea stacks, beach huts, stilt houses, a seaside resort and hotel by the lagoons, pirate ship-houses, umbrellas, surfboards, sandcastles, a lighthouse, a beached shipwreck, a ship offshore, and anchor/octopus/blowfish/turtle statues.
- **Photo-scanned PBR materials** from ambientCG for the ground (sand, grass, sea rock, seabed) and buildings (planks, painted wood, limestone, corrugated metal, roof tiles).
- **Wildlife:** sharks circling the island, clownfish over the reef, glowing jellyfish.
- **New characters:** Captain Tidebeard, Anne Reefrunner, Mako, Sharky, Deckhand Henry, Bonesy and Beach Bum (free Season 2 gift). Every outfit now uses a Season 2 body and bots are the new crew.
- **Sea-creature sidekicks** that swim through the air beside you: clownfish, butterflyfish, lionfish, sunfish, anglerfish, shark and swordfish.
- **New weapon models** for every gun, ocean names for heals (Seaweed Wraps, Coral Kit, Small Bubble, Bubble Shield, Sea Splash, Tide Jug), tools and gliders.
- **Pearls** replace Storm Bucks. New towns: Coral Cove, Rusty Reef, Sunset Lagoon, Lighthouse Ridge, Kelp Flats, Pearl Plaza, Barnacle Bay, plus Beacon Point, Wreck Beach and the lagoon resorts.
- **Ocean UI:** new DEEP TIDE logo, turquoise menus, a grassy hilltop lobby.
- **Tropical towns:** thatched roofs (ambientCG ThatchedRoof001A) and beach-house colours.
- **Flying pirate ship** drop, a **tidal storm** with rain and bubbles, **water bomb** grenades, taller hills, **enterable lagoon resorts**, new cars, treasure chests, furniture, seven model-based harvesting tools, four new gliders, N to switch build materials and a Pro bot difficulty.
- **Season 2 Battle Pass:** Golden Tidebeard, Coral Anne, Ghost Bonesy and Abyss Sharky.

All Season 2 assets load before the island is built; if one can't load, the game falls back to the Season 1 procedural version of that thing.

## Play it on your own computer

You need **Python 3** and a modern browser (Chrome recommended).

1. Open a terminal in this folder and run `./start.sh` (or `python3 -m http.server 8080`).
2. Open **http://localhost:8080/stormfall.html**.

You can also just **double-click `stormfall.html`**. Chrome blocks web pages opened from disk from reading other files, so when the game is opened that way it loads the 3D models and textures from the packed copies in `assets/pack/` instead (the web version never downloads them). After adding or changing anything in `assets/models` or `assets/textures`, run `python3 tools/build_pack.py` to refresh the packs.

## Project layout

```
index.html            sends visitors to the game
stormfall.html        the whole game (HTML, CSS and JavaScript); Season 2 code is in the "SEASON 2: DEEP TIDE" section
start.sh              starts a local server
assets/js/            three.js r128, GLTFLoader, SkeletonUtils
assets/models/s2/     Season 2 props, buildings, guns, wildlife
assets/models/chars/  character models (Season 2 crew + Season 1 characters)
assets/models/pets/   sidekick models
assets/textures/s2/   ambientCG PBR maps (colour, normal, roughness)
assets/music/         soundtrack
sample/sample.html    the original sample version
assets/pack/          packed models and textures for double-click play (generated)
tools/build_pack.py   rebuilds assets/pack
```

## Credits

### Game
- **Main updated version:** [krishnasaigaruda](https://github.com/krishnasaigaruda)
- **Sample version:** [crasebot1234](https://github.com/crasebot1234). Play it at `sample/sample.html`.

### Season 2 characters (via [Poly Pizza](https://poly.pizza))
| Model | Author | License |
|---|---|---|
| [Pirate Captain](https://poly.pizza/m/sN18LyyHAU) | Quaternius | CC0 1.0 |
| [Anne](https://poly.pizza/m/tZYaOQ4l94) | Quaternius | CC0 1.0 |
| [Mako](https://poly.pizza/m/2urczqZ9Xf) | Quaternius | CC0 1.0 |
| [Sharky](https://poly.pizza/m/iPV5YmAoIv) | Quaternius | CC0 1.0 |
| [Henry](https://poly.pizza/m/yEdSk8tRKc) | Quaternius | CC0 1.0 |
| [Skeleton](https://poly.pizza/m/yq5ATpujSt) | Quaternius | CC0 1.0 |
| [Beach Character](https://poly.pizza/m/DojKLcO34E) | Quaternius | CC0 1.0 |

### Season 2 props, buildings, guns and wildlife (via [Poly Pizza](https://poly.pizza))
| Model | Author | License |
|---|---|---|
| [Palm Tree](https://poly.pizza/m/A6cKJYFsIb) | Quaternius | CC0 1.0 |
| [Palm Tree](https://poly.pizza/m/DsrrAYmucG) | Quaternius | CC0 1.0 |
| [Palm Tree](https://poly.pizza/m/P0tgwyXBgr) | Quaternius | CC0 1.0 |
| [small palm trees 3](https://poly.pizza/m/0rs2mKeKQxr) | Steve B | CC-BY 3.0 |
| [coral](https://poly.pizza/m/7Cs3rTEcpcD) | Kelli Ray | CC-BY 3.0 |
| [Orange Coral](https://poly.pizza/m/3HEc6LvqCJd) | Device Lab | CC-BY 3.0 |
| [Coral](https://poly.pizza/m/4KUXdtDdgHR) | Poly by Google | CC-BY 3.0 |
| [kelp](https://poly.pizza/m/5ECC8rIOZJl) | M Smith Jonn | CC-BY 3.0 |
| [Anemone](https://poly.pizza/m/eUZruaSm-9X) | Poly by Google | CC-BY 3.0 |
| [Anemone](https://poly.pizza/m/1FMGb52XdD-) | Poly by Google | CC-BY 3.0 |
| [coral](https://poly.pizza/m/5AfRNBTWHLo) | Kelli Ray | CC-BY 3.0 |
| [Seaweed 3](https://poly.pizza/m/f_gXhnf06Oc) | Laney XR Labs | CC-BY 3.0 |
| [Kelp](https://poly.pizza/m/4cFllH6Iazk) | Poly by Google | CC-BY 3.0 |
| [Seaweed 2](https://poly.pizza/m/b_eanaL8C6j) | Laney XR Labs | CC-BY 3.0 |
| [Rocks](https://poly.pizza/m/OQvi8PIZ40) | Quaternius | CC0 1.0 |
| [Rock](https://poly.pizza/m/RtLRqYjfMs) | Quaternius | CC0 1.0 |
| [rocks](https://poly.pizza/m/94w1VXmnB6) | cyprienxld | CC-BY 3.0 |
| [Rock](https://poly.pizza/m/62bVOJt7vHv) | jeremy | CC-BY 3.0 |
| [Rock Formation](https://poly.pizza/m/pRY9BCFbmQ) | Kenney | CC0 1.0 |
| [Nautilus shell](https://poly.pizza/m/bceVxKNzLaJ) | Poly by Google | CC-BY 3.0 |
| [Turtle](https://poly.pizza/m/fklSEvGm1Q8) | Poly by Google | CC-BY 3.0 |
| [Assault Rifle](https://poly.pizza/m/Bgvuu4CUMV) | Quaternius | CC0 1.0 |
| [Submachine Gun](https://poly.pizza/m/nsP3JukU73) | Quaternius | CC0 1.0 |
| [Shotgun Short Stock](https://poly.pizza/m/MHv3uOV6ja) | Quaternius | CC0 1.0 |
| [Pistol](https://poly.pizza/m/3To2e7sKmO) | Zsky | CC-BY 3.0 |
| [Sniper Rifle](https://poly.pizza/m/ASOMZIErq3) | Quaternius | CC0 1.0 |
| [Rocket Launcher](https://poly.pizza/m/GCqUvqleqN) | Quaternius | CC0 1.0 |
| [Anchor](https://poly.pizza/m/fjAwIosTQHy) | Poly by Google | CC-BY 3.0 |
| [Light House](https://poly.pizza/m/KRebJXIRb8) | MaverickFX | CC0 1.0 |
| [Ship Wreck](https://poly.pizza/m/4qia78IBmZ) | Kenney | CC0 1.0 |
| [Ship](https://poly.pizza/m/mEQj2wZ3GC) | Quaternius | CC0 1.0 |
| [Life preserver](https://poly.pizza/m/7n1vrlFN0GH) | Poly by Google | CC-BY 3.0 |
| [Lifeguard Tower](https://poly.pizza/m/eTXK45QuLQT) | Daniel Doran | CC-BY 3.0 |
| [Jellyfish](https://poly.pizza/m/dA5osnS0Rzj) | Poly by Google | CC-BY 3.0 |
| [Octopus](https://poly.pizza/m/6KQsV8qo5E0) | jeremy | CC-BY 3.0 |
| [Blowfish](https://poly.pizza/m/8DXeKkgTS_s) | jeremy | CC-BY 3.0 |
| [Tree](https://poly.pizza/m/6Yjt8nIwLsD) | Marc Solà | CC-BY 3.0 |
| [Tree](https://poly.pizza/m/MSuchZNT2G) | ParfaitUwU | CC-BY 3.0 |
| [Tree-2](https://poly.pizza/m/cRipmFHCEVU) | Marc Solà | CC-BY 3.0 |
| [Tree](https://poly.pizza/m/6pwiq7hSrHr) | Poly by Google | CC-BY 3.0 |
| [Hut](https://poly.pizza/m/oZDPz5saXE) | Pixel | CC-BY 3.0 |
| [Prairie Shed](https://poly.pizza/m/cJotNkUGLMw) | Zebo | CC-BY 3.0 |
| [Umbrella and chairs](https://poly.pizza/m/8jd7pa_LdMY) | Poly by Google | CC-BY 3.0 |
| [Red/White Beach Umbrella](https://poly.pizza/m/2li3sdSkmCI) | S. Paul Michael | CC-BY 3.0 |
| [Blue/White Beach Umbrella](https://poly.pizza/m/1BLLDjRdxoa) | S. Paul Michael | CC-BY 3.0 |
| [SeaSide Villa](https://poly.pizza/m/03rq-iA54uU) | Yogoshimo 2.0 | CC-BY 3.0 |
| [Hostel](https://poly.pizza/m/e0NvYcgQABj) | Poly by Google | CC-BY 3.0 |
| [Sand castle](https://poly.pizza/m/5iuHHfVoaza) | Poly by Google | CC-BY 3.0 |
| [House](https://poly.pizza/m/fdaqERLQCc) | Pixel | CC-BY 3.0 |
| [House](https://poly.pizza/m/g7eSJLFi4V) | Quaternius | CC0 1.0 |
| [House](https://poly.pizza/m/2kytqGs4rH) | Quaternius | CC0 1.0 |
| [Surfboard](https://poly.pizza/m/dkwqsVsI2R0) | Poly by Google | CC-BY 3.0 |
| [Black Lion Fish](https://poly.pizza/m/4k2s68UrSg) | Quaternius | CC0 1.0 |
| [Butterfly Fish](https://poly.pizza/m/s2MkBeSzGy) | Quaternius | CC0 1.0 |
| [Anglerfish](https://poly.pizza/m/MRjSlwCjHM) | Quaternius | CC0 1.0 |
| [Sunfish](https://poly.pizza/m/UpDxLf8yue) | Quaternius | CC0 1.0 |
| [Swordfish](https://poly.pizza/m/7hMOlBjln0) | Quaternius | CC0 1.0 |

### Season 2 cars, chests, furniture and harvesting tools (via [Poly Pizza](https://poly.pizza))
| Model | Author | License |
|---|---|---|
| [Car](https://poly.pizza/m/75h3mi6uHuC) | Poly by Google | CC-BY 3.0 |
| [Sports Car](https://poly.pizza/m/1mkmFkAz5v) | Quaternius | CC0 1.0 |
| [Pickup Truck](https://poly.pizza/m/qn4grQgHm8) | Quaternius | CC0 1.0 |
| [Jeep](https://poly.pizza/m/AcSdGGrgYP) | Zsky | CC-BY 3.0 |
| [Dining Set](https://poly.pizza/m/4yb-xySr7VT) | CMHT Oculus | CC-BY 3.0 |
| [Bed Double](https://poly.pizza/m/wcmbCZ63mg) | Kenney | CC0 1.0 |
| [Lounge Sofa](https://poly.pizza/m/jMu2iCmGxU) | Kenney | CC0 1.0 |
| [Books on Bookshelf](https://poly.pizza/m/8G2I4M-QVEf) | sirkitree | CC-BY 3.0 |
| [Crate 1](https://poly.pizza/m/uJVMXFRdqJ) | CircuitZ | CC0 1.0 |
| [Trident](https://poly.pizza/m/fephtx6tRg) | MiniPoly | CC0 1.0 |
| [Paddle](https://poly.pizza/m/cJ__sUf4Dry) | Poly by Google | CC-BY 3.0 |
| [Sword](https://poly.pizza/m/9lLmH8Et4K) | Quaternius | CC0 1.0 |
| [Diamond Pickaxe](https://poly.pizza/m/2M0LyYml6j) | Quaternius | CC0 1.0 |
| [Axe](https://poly.pizza/m/jYnW3DNd7J) | Armory_3D | CC0 1.0 |
| [Spear](https://poly.pizza/m/fH1zmvjPNx) | Quaternius | CC0 1.0 |
| [Chest](https://poly.pizza/m/O72u4Drp8k) | Quaternius | CC0 1.0 |
| [Glass Cannon](https://poly.pizza/m/86xRCoaXxKe) | Ray Fields | CC-BY 3.0 |
| [Crossbow](https://poly.pizza/m/kHb0kA11oD) | CreativeTrio | CC0 1.0 |
| [Pistol](https://poly.pizza/m/ldAlSSvuqT) | Quaternius | CC0 1.0 |
| [Shotgun](https://poly.pizza/m/aHe2ssjror) | Zsky | CC-BY 3.0 |
| [Scifi Gun](https://poly.pizza/m/kd1jjjCni7) | MiniPoly | CC0 1.0 |
| [Toilet](https://poly.pizza/m/23BWsguAdkf) | Pat Siefring | CC-BY 3.0 |
| [Bathtub](https://poly.pizza/m/2MbbdwbTjt) | CreativeTrio | CC0 1.0 |
| [Fridge](https://poly.pizza/m/3NYolcXB1o) | Quaternius | CC0 1.0 |
| [Stove Oven](https://poly.pizza/m/uBzXbRF6LQ) | MilkAndBanana | CC0 1.0 |
| [Kitchen Cabinet](https://poly.pizza/m/tWyOLYYHPw) | Kenney | CC0 1.0 |
| [TV](https://poly.pizza/m/2flJebZTUrg) | Jarlan Perez | CC-BY 3.0 |

### PBR materials
Ground080, Grass005, Rock058, Ground054, Planks033B, PaintedWood009C, Tiles143, CorrugatedSteel007A and RoofingTiles014A and ThatchedRoof001A from [ambientCG](https://ambientcg.com), CC0 1.0.

### Music
"Island Meet and Greet", "Pamgaea", "Tiki Bar Mixer" and "Danger Storm" by **Kevin MacLeod** ([incompetech.com](https://incompetech.com)), licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

### Season 1 assets still included
Season 1 character models (Quaternius, Rafael, J-Toastie via Poly Pizza; Soldier, Michelle and X Bot from Mixamo via the three.js examples; the Ready Player Me sample avatar) and sidekick models (Quaternius, CC0) are still in `assets/models/` for players who own them.

### Code and fonts
- [three.js](https://threejs.org) by the three.js authors, MIT License.
- [Barlow / Barlow Condensed](https://fonts.google.com/specimen/Barlow) by Jeremy Tribby and [Luckiest Guy](https://fonts.google.com/specimen/Luckiest+Guy) by Astigmatic, SIL Open Font License.
