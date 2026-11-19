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
| [Desk](https://poly.pizza/m/ISpMh81QGq) | dook | CC-BY 3.0 |
| [Desk](https://poly.pizza/m/c406LNgto0n) | Niko Hokkanen | CC-BY 3.0 |
| [Computer](https://poly.pizza/m/2EHvZLax4Y3) | Poly by Google | CC-BY 3.0 |
| [Office Chair](https://poly.pizza/m/dCEsSsJJ1Md) | CMHT Oculus | CC-BY 3.0 |
| [Lounge Sofa](https://poly.pizza/m/jMu2iCmGxU) | Kenney | CC0 1.0 |
| [Couch | Wide](https://poly.pizza/m/7Q_Ab2HLll1) | Danni Bittman | CC-BY 3.0 |
| [Fiddle-leaf Plant](https://poly.pizza/m/2ag6_uuqsnb) | Poly by Google | CC-BY 3.0 |
| [Umbrella palm tree](https://poly.pizza/m/8Qwgncb6dJT) | Poly by Google | CC-BY 3.0 |
| [Vending Machine](https://poly.pizza/m/0CX6wj64Swu) | Don Carson | CC-BY 3.0 |
| [Vending Machine](https://poly.pizza/m/ZhziWexNWk) | J-Toastie | CC-BY 3.0 |
| [Water Cooler](https://poly.pizza/m/zWi9p5FSxD) | J-Toastie | CC-BY 3.0 |
| [Ping pong table](https://poly.pizza/m/3OK0PHaS9Wi) | Poly by Google | CC-BY 3.0 |
| [Electronic Game](https://poly.pizza/m/QIJoiNqjrk) | burunduk | CC-BY 3.0 |
| [Lemonade](https://poly.pizza/m/1qo2vlHOgUF) | zeoxo | CC-BY 3.0 |
| [Dumpster](https://poly.pizza/m/ASkP8wjEGs) | KolosStudios | CC-BY 3.0 |
| [Trash can](https://poly.pizza/m/0yT-YR5yO4L) | Poly by Google | CC-BY 3.0 |
| [Trash Bags](https://poly.pizza/m/eitNk4I4R1) | Quaternius | CC0 1.0 |
| [Cone](https://poly.pizza/m/itiogTZUAX) | Zsky | CC-BY 3.0 |
| [Traffic Barrier](https://poly.pizza/m/SInF9le9Ch) | Zsky | CC-BY 3.0 |
| [Fire hydrant](https://poly.pizza/m/eNPaSEPrst8) | Poly by Google | CC-BY 3.0 |
| [Cardboard Boxes](https://poly.pizza/m/V9KbWC8Vd6) | Quaternius | CC0 1.0 |
| [Red/White Beach Umbrella](https://poly.pizza/m/2li3sdSkmCI) | S. Paul Michael | CC-BY 3.0 |
| [Rainbow Beach Umbrella](https://poly.pizza/m/cAna-B5z-45) | S. Paul Michael | CC-BY 3.0 |
| [Bench](https://poly.pizza/m/dOSjmdmKaxi) | Ev Amitay | CC-BY 3.0 |
| [Picnic Table](https://poly.pizza/m/LM6QWe8kFT) | J-Toastie | CC-BY 3.0 |
| [Fountain](https://poly.pizza/m/4KKY7CmNe_r) | Poly by Google | CC-BY 3.0 |
| [Three way traffic light](https://poly.pizza/m/ayAwgj82oUR) | Poly by Google | CC-BY 3.0 |
| [Street Objects - Lamp Post](https://poly.pizza/m/awUS2qoxeSa) | Ev Amitay | CC-BY 3.0 |
| [Stop sign](https://poly.pizza/m/60GyU9CdZ9r) | Poly by Google | CC-BY 3.0 |
| [Safe](https://poly.pizza/m/N4egHD2Vms) | CreativeTrio | CC0 1.0 |
| [Cannon](https://poly.pizza/m/J15vlPVvKK) | Quaternius | CC0 1.0 |
| [Workbench Anvil](https://poly.pizza/m/bY1pp3kAAb) | Kenney | CC0 1.0 |
| [Telescope](https://poly.pizza/m/RjyTCQvA8b) | CreativeTrio | CC0 1.0 |
| [Clam](https://poly.pizza/m/8675QcluLQX) | Poly by Google | CC-BY 3.0 |
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

### Season 2 boats, helicopters, outfits, devices and event props
| Model | Author | License |
|---|---|---|
| [Boat](https://poly.pizza/m/8vekojz4Abf) | Poly by Google | CC-BY 3.0 |
| [Boat](https://poly.pizza/m/c2SYxaiPfF3) | Poly by Google | CC-BY 3.0 |
| [Helicopter](https://poly.pizza/m/eb7b31pjGtQ) | jeremy | CC-BY 3.0 |
| [Helicopter](https://poly.pizza/m/cTzINMr0WdS) | Poly by Google | CC-BY 3.0 |
| [Dock Long](https://poly.pizza/m/bN9Oz3niNm) | Quaternius | CC0 1.0 |
| [Witch](https://poly.pizza/m/QBEOV9ZUT8) | Quaternius | CC-BY 3.0 |
| [Shrine](https://poly.pizza/m/tFxdxO5clk) | Kay Lousberg | CC0 1.0 |
| [Bonfire](https://poly.pizza/m/Azj9hJwwwG) | Quaternius | CC0 1.0 |
| [Hammock](https://poly.pizza/m/bsp0Uzr6cSI) | Poly by Google | CC-BY 3.0 |
| [beach ball](https://poly.pizza/m/4IwPTeOmq6c) | the_ normalgamer | CC-BY 3.0 |
| [Bottle](https://poly.pizza/m/FAHsHFXfTf) | Quaternius | CC0 1.0 |
| [Fishing Pole](https://poly.pizza/m/eyuCxAqI9er) | Shawn Westphal | CC-BY 3.0 |
| [Logs](https://poly.pizza/m/fei4I7FfrJ) | Quaternius | CC0 1.0 |
| [Ammo Can](https://poly.pizza/m/9xeB2FkEYr) | Pichuliru | CC0 1.0 |
| [Crystal](https://poly.pizza/m/WzWPKHFMkL) | iPoly3D | CC0 1.0 |
| [Shovel](https://poly.pizza/m/oNBQSf87ZJ) | Quaternius | CC0 1.0 |
| [Sea Urchin](https://poly.pizza/m/f4iwEhEP3-d) | Poly by Google | CC-BY 3.0 |
| [Clam](https://poly.pizza/m/65ObbG0O7Ze) | Poly by Google | CC-BY 3.0 |
| [Ski lift pole](https://poly.pizza/m/1nMSE0mYj_C) | Poly by Google | CC-BY 3.0 |
| [Spiky Ball](https://poly.pizza/m/HEKBGK7iIk) | Quaternius | CC0 1.0 |
| [Balloon](https://poly.pizza/m/d1gDDhM7pTf) | Poly by Google | CC-BY 3.0 |
| [Heart](https://poly.pizza/m/8RA5hHU5gHK) | Poly by Google | CC-BY 3.0 |
| [Bush with Flowers](https://poly.pizza/m/U1ymDy8tbY) | Quaternius | CC0 1.0 |
| [Firework](https://poly.pizza/m/7ZuN5uYCrbf) | Josh Graham | CC-BY 3.0 |
| [Egg](https://poly.pizza/m/3xseQxXMXPL) | Poly by Google | CC-BY 3.0 |
| [Rubber Duck](https://poly.pizza/m/9pffFcv7LSm) | Poly by Google | CC-BY 3.0 |
| [Popsicle](https://poly.pizza/m/08qNOboczRk) | Poly by Google | CC-BY 3.0 |
| [Firework](https://poly.pizza/m/nExftOJJ8x) | GkStudio | CC-BY 3.0 |
| [Haystack](https://poly.pizza/m/6LeCqyw00RK) | Poly by Google | CC-BY 3.0 |
| [Corn](https://poly.pizza/m/IhhB7kGaAQ) | Quaternius | CC0 1.0 |
| [Pie](https://poly.pizza/m/eu-vRr2-5dY) | Poly by Google | CC-BY 3.0 |
| [Turkey](https://poly.pizza/m/4f31_AG9Iap) | Poly by Google | CC-BY 3.0 |
| [Christmas Tree](https://poly.pizza/m/exL-ilJKlZt) | Don Carson | CC-BY 3.0 |
| [Flower Group](https://poly.pizza/m/hfPzQAedOe) | Quaternius | CC0 1.0 |
| [Snow Man](https://poly.pizza/m/562IGbxkrTC) | Taiga Yonemoto | CC-BY 3.0 |
| [Present](https://poly.pizza/m/eHwOj9QQa3) | ParfaitUwU | CC-BY 3.0 |
| [Complex Health Potion](https://poly.pizza/m/5DvOJDIgDYu) | Garrett LeFever | CC-BY 3.0 |
| [Clover](https://poly.pizza/m/aCdjtvG0dvD) | Poly by Google | CC-BY 3.0 |
| [Pumpkin](https://poly.pizza/m/XYPzyxSw3c) | CreativeTrio | CC0 1.0 |
| [Pumpkin](https://poly.pizza/m/bvLvqnU1jX) | Quaternius | CC0 1.0 |
| [Scarecrow](https://poly.pizza/m/7qFs_DjjuVp) | Poly by Google | CC-BY 3.0 |
| [Character Animated (outfit body)](https://poly.pizza/m/DgOCW9ZCRJ) | Quaternius | CC0 1.0 |
| [Woman in Dress (outfit body)](https://poly.pizza/m/zMyPlQXBzq) | Quaternius | CC0 1.0 |
| [Astronaut (outfit body)](https://poly.pizza/m/3hC2i0CTuO) | Quaternius | CC0 1.0 |
| [Worker (outfit body)](https://poly.pizza/m/Yg2bQZO6Hj) | Quaternius | CC0 1.0 |
| [Animated Woman (outfit body)](https://poly.pizza/m/qJ2gsTUBHL) | Quaternius | CC0 1.0 |
| [Alien (outfit body)](https://poly.pizza/m/HYUUkdugoP) | Quaternius | CC0 1.0 |
| [King (outfit body)](https://poly.pizza/m/I1gTjmuK2m) | Quaternius | CC0 1.0 |
| [Ninja (outfit body)](https://poly.pizza/m/xGYmeDpfTu) | Quaternius | CC0 1.0 |
| [Man (outfit body)](https://poly.pizza/m/HMnuH5geEG) | Quaternius | CC0 1.0 |
| [Woman (outfit body)](https://poly.pizza/m/AQsd9ngvKU) | Quaternius | CC0 1.0 |
| [Man in Suit (outfit body)](https://poly.pizza/m/mQnGoME1ez) | Quaternius | CC0 1.0 |
| [Animated Woman (outfit body)](https://poly.pizza/m/9kF7eTDbhO) | Quaternius | CC0 1.0 |
| [Characters Shaun (outfit body)](https://poly.pizza/m/eJFT9MxzOM) | Quaternius | CC0 1.0 |
| [Bunny (outfit body)](https://poly.pizza/m/irZjWFARyl) | Quaternius | CC0 1.0 |
| [Animated Platformer Character (outfit body)](https://poly.pizza/m/kKtL4zvS3n) | Quaternius | CC0 1.0 |
| [Casual Character (outfit body)](https://poly.pizza/m/kZ3DmIoGip) | Quaternius | CC0 1.0 |
| [Astronaut (outfit body)](https://poly.pizza/m/0D54W8yfrA) | Quaternius | CC0 1.0 |
| [Alien (outfit body)](https://poly.pizza/m/RRliSQBP7r) | Quaternius | CC0 1.0 |
| [Farmer (outfit body)](https://poly.pizza/m/7pn3R6hPvE) | Quaternius | CC0 1.0 |
| [Worker (outfit body)](https://poly.pizza/m/E8079Ahx7k) | Quaternius | CC-BY 3.0 |
| [Animated Woman (outfit body)](https://poly.pizza/m/nIItLV9nxS) | Quaternius | CC0 1.0 |
| [Animated Wizard (outfit body)](https://poly.pizza/m/kttbFvCl2C) | Quaternius | CC-BY 3.0 |
| [Hacker-Craft Runabout](https://sketchfab.com/3d-models/hacker-craft-runabout-88fd71fc831f4332a97e27e3b0e6b857) | trivial.cat | Sketchfab Standard |

### PBR materials
Ground080, Grass005, Rock058, Ground054, Planks033B, PaintedWood009C, Tiles143, CorrugatedSteel007A and RoofingTiles014A and ThatchedRoof001A from [ambientCG](https://ambientcg.com), CC0 1.0.

### Music
"Island Meet and Greet", "Pamgaea", "Tiki Bar Mixer" and "Danger Storm" by **Kevin MacLeod** ([incompetech.com](https://incompetech.com)), licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

### Season 1 assets still included
Season 1 character models (Quaternius, Rafael, J-Toastie via Poly Pizza; Soldier, Michelle and X Bot from Mixamo via the three.js examples; the Ready Player Me sample avatar) and sidekick models (Quaternius, CC0) are still in `assets/models/` for players who own them.

### Code and fonts
- [three.js](https://threejs.org) by the three.js authors, MIT License.
- [Barlow / Barlow Condensed](https://fonts.google.com/specimen/Barlow) by Jeremy Tribby and [Luckiest Guy](https://fonts.google.com/specimen/Luckiest+Guy) by Astigmatic, SIL Open Font License.
