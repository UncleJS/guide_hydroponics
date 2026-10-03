# Design Constants
## Single source of truth for both guide sets

[![Docs: Home Hydroponics](https://img.shields.io/badge/Docs-Home%20Hydroponics-2d6a4f)](../README.md)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

---

## Table of Contents

- [How to use this file](#how-to-use-this-file)
- [Bracket convention](#bracket-convention)
- [Worked climate](#worked-climate)
- [Site](#site)
- [NFT Zone A](#nft-zone-a)
- [Ebb and Flow Zone A](#ebb-and-flow-zone-a)
- [Zone B and Zone C](#zone-b-and-zone-c)
- [Nutrients and water](#nutrients-and-water)
- [Electrical and safety](#electrical-and-safety)
- [Do not write](#do-not-write)

---

## How to use this file

Every dimension, price, dose, and calendar date in the NFT guides, the Ebb and Flow guides, the comparison guides, `zones.md`, the glossary, and the README is copied from this file. If a guide disagrees with this file, the guide is wrong.

USA value first. South African equivalent in brackets.

[↑ Back to TOC](#table-of-contents)

---

## Bracket convention

| Kind | Form | Example |
|------|------|---------|
| Length, area, volume, temperature, flow | Imperial, then metric | `8 ft (2.44 m)`, `20 US gal (76 L)`, `70°F (21°C)`, `160 US gph (600 L/h)` |
| Mass dose | Per US gallon, then per liter | `2.4 g/US gal (0.63 g/L)` |
| Money | Dollars, then rand | `$25 (R450)` |
| Calendar | US month, then South African month six months later | mid-April (SA: mid-October) |
| EC, pH, DLI | No conversion | `1.4–1.6 mS/cm` |

Gallons are always **US gal** (3.785 L), never the imperial gallon (4.55 L).

**Planning exchange rate:** `$1 = R18.00`, frozen **3 October 2026**. This is a planning rate, not a live quote. Round rand to the nearest rand. Worked electricity price: **$0.15/kWh (R2.70/kWh)**.

[↑ Back to TOC](#table-of-contents)

---

## Worked climate

Inland mid-USA, about **38°N**, USDA zones **6b–7a** (Kansas City, St. Louis, Louisville, Richmond). Not the Pacific coast at the same latitude.

| Item | Value |
|------|-------|
| Last spring frost (planning) | April 15 (SA: October 15) |
| First fall frost (planning) | October 20 (SA: April 20) |
| Outdoor season | mid-April through mid-October (SA: mid-October through mid-April) |
| Summer afternoon highs | 90–100°F (32–38°C), June–August (SA: December–February) |
| Winter lows in this band | 0–15°F (−18 to −9°C) |
| Clear-sky DLI, summer | 45–55 mol/m²/day |
| Clear-sky DLI, spring and fall | 25–35 mol/m²/day |
| Clear-sky DLI, winter | 10–15 mol/m²/day |
| Shade cloth | 40%, deploy when afternoon highs hold above 85°F (29°C) |
| Long-axis facing | South (SA: north) |
| Unprotected deep winter | Do not run outdoor NFT through December–February (SA: June–August) |

The South African month is a six-month shift so a southern-hemisphere reader can use the same season. It is not a second climate dataset.

[↑ Back to TOC](#table-of-contents)

---

## Site

| Item | Value |
|------|-------|
| Footprint | 13 ft × 10 ft (4.0 m × 3.0 m) |
| Working aisle | 24 in (61 cm) on the south side |
| Wind break | North edge, about 12 in (30 cm) clear of the frame |
| Work bench | 32 in × 20 in (81 cm × 51 cm), optional |

Zone B and Zone C are the same whichever Zone A you build. Build one Zone A: NFT or Ebb and Flow.

[↑ Back to TOC](#table-of-contents)

---

## NFT Zone A

Two reservoirs. CH1–CH3 never share solution with CH4.

### Greens loop

| Item | Value |
|------|-------|
| Channels | CH1, CH2, CH3 |
| Channel | 3 in (76 mm) square, 8 ft (2.44 m) |
| Sites | 11 per channel, 33 total |
| Net pots | 2 in (51 mm) |
| Spacing | 9 in (229 mm), about 2 in (51 mm) clear of each end |
| Crops | CH1 lettuce. CH2 herbs (basil, cilantro, parsley, chives). CH3 spinach, kale, mint, and strawberries in 3–4 of the 11 sites |
| Reservoir | 20 US gal (76 L), black body, white exterior, shaded |
| Pump | 160–210 US gph (600–800 L/h), about 15 W (range 10–20 W) |
| Runtime | 24 hours a day. No overnight off. No 15-on / 45-off schedule |
| Flow per channel | 0.26–0.53 US gpm (1–2 L/min) |
| EC | 0.8–1.8 mS/cm. Lettuce stays at or below 1.8 |
| Full change | Every 7 days |

### Fruiting loop

| Item | Value |
|------|-------|
| Channel | CH4 only, 4 in (102 mm) square, 8 ft (2.44 m) |
| Sites | 7 holes at 12 in (305 mm) |
| Net pots | 3 in (76 mm) |
| Crops | Cherry tomato and pepper only. Not strawberries |
| How many plants | 4–5 indeterminate cherries (skip holes) or up to 7 compact determinate plants |
| Reservoir | 10 US gal (38 L), black body, white exterior, shaded. Own pump. Not teed into the greens manifold |
| Pump | 50–100 US gph (200–400 L/h), about 8 W (range 5–12 W) |
| Runtime | 24 hours a day |
| EC | Tomato fruiting 2.5–3.5 mS/cm. Pepper fruiting 2.0–3.0 mS/cm. These targets apply only to this tank |
| Full change | Every 5–7 days |
| Planning yield | 4–6 lb (1.8–2.7 kg) of cherry tomatoes per plant |

### Shared NFT frame and plumbing

| Item | Value |
|------|-------|
| Total sites | 40 |
| Slope | 1:30, a 3¼ in (83 mm) drop over 8 ft (2.44 m) |
| Posts | 36 in (91 cm) at the high (inlet) end, 32¾ in (83 cm) at the low (drain) end |
| Greens manifold | 1 in (25 mm) along the high end, feeding CH1–CH3 only |
| Channel inlets | ½ in (13 mm) |
| Return | ¾–1 in (19–25 mm), gravity, each loop back to its own reservoir |
| Dry-out window | 15–30 minutes in warm weather. Treat that as the action time |
| Air pump | Recommended in both reservoirs |
| Frame footprint | About 9 ft × 4 ft (2.7 m × 1.2 m), including both reservoirs at the low end |

[↑ Back to TOC](#table-of-contents)

---

## Ebb and Flow Zone A

| Item | Value |
|------|-------|
| Tables | 3, each 4 ft × 2 ft (1.22 m × 0.61 m), perfectly level |
| Table 1 | Indeterminate tomato or cucumber, 1 plant |
| Table 2 | Pepper, eggplant (aubergine), or zucchini (courgette), 1–2 plants |
| Table 3 | Lettuce, herbs, pak choi, strawberries, or a later fruiting crop |
| Media | LECA, 5 in (13 cm) deep |
| LECA per table | 25 US gal (95 L) |
| LECA for 3 tables | 75 US gal (284 L). Buy 90 US gal (340 L) to cover rinse loss |
| Flood level | About ¾ in (2 cm) below the LECA surface, set by the overflow standpipe |
| Flood duration | 15–30 minutes |
| Vegetative floods | 3 times per day |
| Fruiting floods | 4 times per day. This is the ceiling |
| Heatwave | Keep 4 floods. Shorten them if needed. Add 40% shade. Do not drop to 2 and do not add a 5th |
| Reservoir | 45 US gal (170 L) recommended. Acceptable range 40–50 US gal (151–189 L). Sits below the drains |
| Pump | 250 US gph (950 L/h) recommended. Range 200–300 US gph (760–1,140 L/h). About 35 W (range 25–45 W) |
| Timer | Digital, 1-minute resolution, in a weatherproof box. Not a mechanical timer as the outdoor default |
| Overflow | 1½ in (40 mm) bulkhead and standpipe, one per table |
| Drain | 1 in (25 mm) bulkhead, one per table |
| Full change | Every 10–14 days |
| Missed-flood buffer | Moist LECA holds 8–24 hours. Do not describe wilt in 1.5–2 hours as the normal case |
| Stuck pump ON | Root rot risk in 2–4 hours. A drain-confirmation float that cuts the pump is the primary safety device |

[↑ Back to TOC](#table-of-contents)

---

## Zone B and Zone C

These blocks are identical in the NFT set and the Ebb and Flow set.

### Zone B — microgreens

| Item | Value |
|------|-------|
| Shelf | 24 in × 20 in (61 cm × 51 cm), two tiers, about 36 in (91 cm) tall |
| Trays | 6 trays, each 10 in × 20 in (25 cm × 50 cm) |
| Coco depth | 1–1¼ in (2.5–3 cm) |
| Standard crops | pH-adjusted water only, pH 5.8–6.2. No nutrients |
| Sunflower and pea only | Optional EC 0.4–0.8 mS/cm if the grow runs long |
| Watering | Mist twice a day |

### Zone C — grow bags

| Bag | Count | Crop |
|-----|-------|------|
| 5 US gal (19 L) | 2 | Radish |
| 5 US gal (19 L) | 1 | Beet (beetroot) |
| 10 US gal (38 L) | 3 | Carrot |

Media, by volume: 60% coco, 30% perlite, 10% vermiculite. No garden soil.

Fertigation EC ceiling is **2.0 mS/cm**. Beet (beetroot) does not get a higher target.

One season, planning yields, used by both budget guides:

| Crop | Yield |
|------|-------|
| Radish | 15 lb (6.8 kg) |
| Beet (beetroot) | 8 lb (3.6 kg) |
| Carrot | 20 lb (9.1 kg) |
| Zone C total | 43 lb (20 kg), about $80–$110 (R1,440–R1,980) |

[↑ Back to TOC](#table-of-contents)

---

## Nutrients and water

### Masterblend base (vegetative, EC about 1.4–1.6 mS/cm)

Per **1 US gal (3.8 L)**:

- Masterblend 4-18-38: **2.4 g (0.63 g/L)**
- Calcium nitrate: **2.4 g (0.63 g/L)**
- Epsom salt: **1.2 g (0.32 g/L)**

Never write this recipe as 2.4 g/L. That is about four times the dose.

Scale the same ratio for the 20 US gal, 10 US gal, and 45 US gal reservoirs. Raise or lower the whole recipe to hit the crop EC. Do not change the ratio to chase one element unless a guide section is specifically about a deficiency correction.

### Top-up

- EC at or above target: add plain water, pH-adjusted to 5.8–6.2.
- EC below target: add nutrient stock, then recheck EC and pH.
- Do not write “always top up at full target EC” and do not write “always top up with plain water.”

### pH

Working window **5.8–6.2**. Acceptable band **5.5–6.5**.

### Solution temperature

Aim for **64–72°F (18–22°C)**. Above **77°F (25°C)**, dissolved oxygen falls and pythium risk rises. That is the heat action line for both systems.

### Reservoir changes

| Reservoir | Interval |
|-----------|----------|
| NFT greens, 20 US gal (76 L) | Every 7 days |
| NFT fruiting, 10 US gal (38 L) | Every 5–7 days |
| Ebb and Flow, 45 US gal (170 L) | Every 10–14 days |

Also change sooner if EC will not hold, the solution smells, or roots slime.

### Hydrogen peroxide

A 3% hydrogen-peroxide flush is a cleaning step. Remove plants, or hand-water them, before the flush. Do not run that dose through a live root zone.

### Bleach soak

Pump off, plants out (or hand-watered on a tray), then soak. NFT roots dry in 15–30 minutes. Do not leave plants in a stopped channel during a soak.

[↑ Back to TOC](#table-of-contents)

---

## Electrical and safety

| Item | USA | South Africa (bracket) |
|------|-----|------------------------|
| Mains | 120 V | 230 V |
| Person protection | Outdoor GFCI | 30 mA earth-leakage breaker |
| Timer and plugs | Weatherproof box, outdoor-rated | Same requirement |

Also required in the nutrient guides:

- Gloves, eye protection, and a dust mask when handling dry salts, phosphoric acid, or potassium hydroxide.
- Nutrient concentrates, acids, and pesticides in a latched box, away from children and pets.
- Any line about the garden being good for children also says the chemicals are locked.

Ebb and Flow Guide 13: the primary automatic safety action is **stuck-ON cutoff** (float still up after the pump should be off → open the pump relay). A second timer that only restarts a stopped pump is not the safety story.

[↑ Back to TOC](#table-of-contents)

---

## Do not write

These are leftovers. They fail the guide.

- `2.4 g/L` as the Masterblend dose
- `~48` plant sites, or 12 sites on CH1
- LECA at 20–30 L or 20–25 L per table
- Flood depth of 3–5 cm as the design flood
- A 5th flood per day as advice
- Overnight pump-off, or 15 minutes on / 45 minutes off, as the NFT default
- Dry-out in 2–4 hours, or a 1–2 hour NFT critical window, as the design number
- One shared NFT reservoir for tomatoes and lettuce
- Strawberries on CH4
- Herbs on Channel 3
- Peppers “Ebb and Flow only” or peppers on the greens loop
- UK, 50–55°N, or 60°N as the worked example
- Sterling prices
- A link to `PLAN.md`
- Metric-first dimensions (`2.4 m` with no feet in front)
- Ebb and Flow wilt “in 1.5–2 hours” as the normal buffer
- Table 1 as the leafy table
- Mechanical timer as the recommended outdoor Ebb and Flow timer
- Compare-guide hardware that is a different machine (4 ft channels presented as a smaller separate design, a 100 L Ebb and Flow reservoir)

[↑ Back to TOC](#table-of-contents)

---

<!-- copyright -->
*Copyright (c) 2026 UncleJS. Licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) — free to share and adapt for non-commercial purposes with attribution and ShareAlike.*
