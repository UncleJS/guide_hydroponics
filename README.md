# Home Hydroponics — Outdoor Hydroponic Systems Guide

[![Docs: Home Hydroponics](https://img.shields.io/badge/Docs-Home%20Hydroponics-2d6a4f)](README.md)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)


A complete DIY guide for building and running outdoor hydroponic systems in an inland mid-USA backyard, about **38°N** (USDA zones 6b–7a: Kansas City, St. Louis, Louisville, Richmond). Two full systems are covered — **Nutrient Film Technique (NFT)** and **Ebb and Flow (flood-and-drain)** — each with **14 guides (00–13)**, from first principles to automation.

Prices are US dollars with South African rand in brackets, at a planning rate of **$1 = R18** (3 October 2026). Measurements are imperial first, metric in brackets. Seasonal months are US dates with the South African month six months later in brackets. The number set lives in [`guide/design-constants.md`](guide/design-constants.md). Hardware totals live in each system’s Guide 12.

---

## Table of Contents

- [Choose Your System](#choose-your-system)
- [Shared Reference Documents](#shared-reference-documents)
- [NFT Guide Library](#nft-guide-library)
- [Ebb & Flow Guide Library](#ebb-flow-guide-library)
- [Cross-System Comparison Guides](#cross-system-comparison-guides)
- [Quick-Start Paths](#quick-start-paths)
  - [NFT — new to hydroponics](#nft-new-to-hydroponics)
  - [Ebb and Flow — want fruiting crops](#ebb-and-flow--want-fruiting-crops)

---


## Choose Your System

| | NFT — Nutrient Film Technique | Ebb and Flow — Flood and Drain |
|---|---|---|
| **How it works** | A thin film runs 24 hours a day. Two pumps, two reservoirs | Tables flood, then drain. One pump on a digital timer |
| **Reservoirs** | Greens 20 US gal (76 L) for CH1–CH3. Fruiting 10 US gal (38 L) for CH4 only | 45 US gal (170 L) under the tables |
| **Media** | Clay pebbles in net pots only | 5 in (13 cm) of LECA, 25 US gal (95 L) per table |
| **Power failure** | High — roots dry in 15–30 minutes in warm weather | Moderate — moist LECA buffers 8–24 hours |
| **Timer failure** | Not used for the pumps | **High** — a pump stuck ON rots roots in 2–4 hours |
| **Best for** | Lettuce, herbs, spinach, kale, plus cherry tomato and pepper on CH4 | Those crops, plus cucumber, courgette, and aubergine |
| **Crop limit** | No cucumber, courgette, aubergine, or root crops in the channels | No root crops in the tables. Carrots, radish, and beet stay in Zone C |
| **Build cost** | Full three-zone Lean / Standard / Optimised **$468 / $769 / $1,080** (R8,424 / R13,842 / R19,440). BOM in [NFT Guide 12](guide/nft/12-budget-and-sourcing.md) | Full three-zone Budget / Mid / Premium **$711 / $1,115 / $1,624** (R12,798 / R20,070 / R29,232). BOM in [Ebb and Flow Guide 12](guide/ebb-and-flow/12-budget-and-sourcing.md) |
| **Guide set** | [`guide/nft/`](guide/nft/) | [`guide/ebb-and-flow/`](guide/ebb-and-flow/) |

Both systems share **Zone B (microgreens)** and **Zone C (root-vegetable grow bags)**. Only Zone A changes. The yard map for both is [`zones.md`](zones.md). Mains power is a **120 V outdoor GFCI** (SA: **230 V**, **30 mA earth-leakage**).

[↑ Back to TOC](#table-of-contents)

---

## Shared Reference Documents

| Document | Description |
|----------|-------------|
| [`zones.md`](zones.md) | Yard layout for NFT and for Ebb and Flow, plus the shared microgreen and grow-bag zones |
| [`guide/design-constants.md`](guide/design-constants.md) | The only number set: sizes, doses, flood ceiling, climate, and the dollar/rand rate |
| [`guide/glossary.md`](guide/glossary.md) | Acronyms and technical terms used across both guide sets |

[↑ Back to TOC](#table-of-contents)

---

## NFT Guide Library

> Four 8 ft (2.44 m) channels, two reservoirs, continuous flow. Leafy greens and herbs on CH1–CH3. Cherry tomato and pepper on CH4 only.

| # | File | What It Covers |
|---|------|----------------|
| 00 | [`guide/nft/00-system-overview.md`](guide/nft/00-system-overview.md) | System design, zone layout, component inventory, 4-week build timeline, grow calendar, daily checklist |
| 01 | [`guide/nft/01-nft-basics.md`](guide/nft/01-nft-basics.md) | How NFT works, channel slope, flow rate, root oxygenation, pump failure, scaling, pros/cons |
| 02 | [`guide/nft/02-nutrient-solution.md`](guide/nft/02-nutrient-solution.md) | The 17 essential nutrients, EC, pH, Masterblend & GH Flora recipes, deficiency guide |
| 03 | [`guide/nft/03-water-quality.md`](guide/nft/03-water-quality.md) | Tap, well, RO, and rainwater; chlorine/chloramine; algae prevention; reservoir sizing |
| 04 | [`guide/nft/04-lighting.md`](guide/nft/04-lighting.md) | PAR, DLI, sun mapping, shade cloth, seasonal strategy, supplemental lighting |
| 05 | [`guide/nft/05-growing-media.md`](guide/nft/05-growing-media.md) | Net pots, clay pebbles, rockwool, coco coir, germination methods, media reuse |
| 06 | [`guide/nft/06-crops.md`](guide/nft/06-crops.md) | Per-crop growing guide for every plant in the system, plus succession planning |
| 07 | [`guide/nft/07-pests-and-disease.md`](guide/nft/07-pests-and-disease.md) | IPM framework, pest and disease ID, beneficial insects, PHI reference, sterilisation |
| 08 | [`guide/nft/08-system-maintenance.md`](guide/nft/08-system-maintenance.md) | Daily, twice-weekly, weekly, and seasonal maintenance schedules and logbook template |
| 09 | [`guide/nft/09-troubleshooting.md`](guide/nft/09-troubleshooting.md) | Symptom → cause → fix decision trees for water, plant, equipment, and combined problems |
| 10 | [`guide/nft/10-climate-management.md`](guide/nft/10-climate-management.md) | Heat, frost, wind, rain, humidity — seasonal action plans and climate monitoring setup |
| 11 | [`guide/nft/11-build-guide.md`](guide/nft/11-build-guide.md) | Step-by-step DIY build instructions from site prep to first nutrient fill |
| 12 | [`guide/nft/12-budget-and-sourcing.md`](guide/nft/12-budget-and-sourcing.md) | Full BOM by tier, where to buy, running costs, yield estimates, and ROI/payback analysis |
| 13 | [`guide/nft/13-automation.md`](guide/nft/13-automation.md) | From a $15 WiFi thermometer to a full ESP32 sensor network with dashboards and alerts |

[↑ Back to TOC](#table-of-contents)

---

## Ebb & Flow Guide Library

> Three 4 ft × 2 ft (1.22 m × 0.61 m) tables, vegetative starts at 3 floods a day, fruiting up to 4 (the ceiling), 5 in (13 cm) of LECA. Fruiting crops, including ones NFT cannot hold.

| # | File | What It Covers |
|---|------|----------------|
| 00 | [`guide/ebb-and-flow/00-system-overview.md`](guide/ebb-and-flow/00-system-overview.md) | System design, zone layout, component inventory, 4-week build timeline, grow calendar, daily checklist |
| 01 | [`guide/ebb-and-flow/01-ebb-flow-basics.md`](guide/ebb-and-flow/01-ebb-flow-basics.md) | Flood-drain principle, overflow fittings, flood frequency science, timer failure modes, pros/cons |
| 02 | [`guide/ebb-and-flow/02-nutrient-solution.md`](guide/ebb-and-flow/02-nutrient-solution.md) | Nutrients, EC, pH — with E&F media interaction, salt accumulation, and media flush protocol |
| 03 | [`guide/ebb-and-flow/03-water-quality.md`](guide/ebb-and-flow/03-water-quality.md) | Water sources, testing, treatment — with LECA salt buildup monitoring and flush schedules |
| 04 | [`guide/ebb-and-flow/04-lighting.md`](guide/ebb-and-flow/04-lighting.md) | PAR, DLI, shade cloth — with flood table-specific light distribution and canopy spacing |
| 05 | [`guide/ebb-and-flow/05-growing-media.md`](guide/ebb-and-flow/05-growing-media.md) | Clay pebbles (LECA) preparation, media depth, coco coir, germination, media reuse/sterilisation |
| 06 | [`guide/ebb-and-flow/06-crops.md`](guide/ebb-and-flow/06-crops.md) | Per-crop guide including cucumbers, courgettes, and aubergine not possible in NFT |
| 07 | [`guide/ebb-and-flow/07-pests-and-disease.md`](guide/ebb-and-flow/07-pests-and-disease.md) | IPM, pests, diseases — with E&F risks: fungus gnats, Pythium from over-flooding, algae in LECA |
| 08 | [`guide/ebb-and-flow/08-system-maintenance.md`](guide/ebb-and-flow/08-system-maintenance.md) | Daily/weekly/seasonal schedules — flood cycle verification, salt crust, overflow fitting checks |
| 09 | [`guide/ebb-and-flow/09-troubleshooting.md`](guide/ebb-and-flow/09-troubleshooting.md) | Decision trees for flood/drain problems, timer failure, root rot, salt lockout, liner leaks |
| 10 | [`guide/ebb-and-flow/10-climate-management.md`](guide/ebb-and-flow/10-climate-management.md) | Heat, frost, wind, rain — open table rain dilution, thermal mass differences, seasonal plans |
| 11 | [`guide/ebb-and-flow/11-build-guide.md`](guide/ebb-and-flow/11-build-guide.md) | Full DIY build — level tables, two-fitting system, reservoir positioning, timer setup, all 3 zones |
| 12 | [`guide/ebb-and-flow/12-budget-and-sourcing.md`](guide/ebb-and-flow/12-budget-and-sourcing.md) | BOM across 3 tiers, bulkhead fittings, LECA costs, yield estimates, ROI including fruiting crops |
| 13 | [`guide/ebb-and-flow/13-automation.md`](guide/ebb-and-flow/13-automation.md) | Drain confirmation sensor (float switch), flood cycle logging, stuck-ON detection, ESP32, dashboards |

[↑ Back to TOC](#table-of-contents)

---

## Cross-System Comparison Guides

> Running both systems, or deciding between them? These guides compare NFT and E&F side-by-side on the topics where the systems differ most.

| # | File | What It Covers |
|---|------|----------------|
| 01 | [`guide/compare/01-nutrients.md`](guide/compare/01-nutrients.md) | EC management, media EC vs reservoir EC, salt accumulation, flush protocol, nutrient recipes, deficiency patterns |
| 02 | [`guide/compare/02-crops.md`](guide/compare/02-crops.md) | Which crops belong in which system, yield estimates, succession calendars, transplanting, crop-specific problems |
| 03 | [`guide/compare/03-automation.md`](guide/compare/03-automation.md) | Failure mode hierarchies, sensor priorities, drain confirmation vs flow confirmation, alert logic, two-system dashboard |
| 04 | [`guide/compare/04-cost.md`](guide/compare/04-cost.md) | Build costs by tier, running costs, yield value, payback periods, where each system saves, spend priorities |

[↑ Back to TOC](#table-of-contents)

---

## Quick-Start Paths

### NFT — new to hydroponics
1. **[NFT Guide 00 — System Overview](guide/nft/00-system-overview.md)** — inventory, build timeline, grow calendar
2. **[`zones.md`](zones.md)** — the yard, including the two NFT reservoirs
3. **[`guide/design-constants.md`](guide/design-constants.md)** — sizes and doses
4. **[NFT Guide 11 — Build](guide/nft/11-build-guide.md)** — construct the system
5. **[NFT Guide 01 — Basics](guide/nft/01-nft-basics.md)** — understand how NFT works
6. **[NFT Guide 02 — Nutrients](guide/nft/02-nutrient-solution.md)** — mix your first solution
7. **[NFT Guide 06 — Crops](guide/nft/06-crops.md)** — plant selection and care
8. **[NFT Guide 08 — Maintenance](guide/nft/08-system-maintenance.md)** — keep it running

### Ebb and Flow — want fruiting crops
1. **[Ebb and Flow Guide 00 — System Overview](guide/ebb-and-flow/00-system-overview.md)** — inventory, build timeline, grow calendar
2. **[`zones.md`](zones.md)** — the flood-table layout
3. **[Ebb and Flow Guide 01 — Basics](guide/ebb-and-flow/01-ebb-flow-basics.md)** — flood-drain and timer safety
4. **[Ebb and Flow Guide 05 — Media](guide/ebb-and-flow/05-growing-media.md)** — LECA preparation (do this before the first flood)
5. **[Ebb and Flow Guide 11 — Build](guide/ebb-and-flow/11-build-guide.md)** — construct the system
6. **[Ebb and Flow Guide 02 — Nutrients](guide/ebb-and-flow/02-nutrient-solution.md)** — mix and manage solution with media
7. **[Ebb and Flow Guide 06 — Crops](guide/ebb-and-flow/06-crops.md)** — tomatoes, cucumbers, courgettes, and the rest
8. **[Ebb and Flow Guide 08 — Maintenance](guide/ebb-and-flow/08-system-maintenance.md)** — flood-cycle checks and salt
9. **[Ebb and Flow Guide 13 — Automation](guide/ebb-and-flow/13-automation.md)** — the drain-confirmation cutoff

---

*Last updated: October 2026*

[↑ Back to TOC](#table-of-contents)

---

<!-- copyright -->
*Copyright (c) 2026 UncleJS. Licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) — free to share and adapt for non-commercial purposes with attribution and ShareAlike.*
