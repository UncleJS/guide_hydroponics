# Home Hydroponics — Outdoor Hydroponic Systems Guide

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

A complete DIY guide for building and running outdoor hydroponic systems in a temperate backyard. Two full systems are covered — **Nutrient Film Technique (NFT)** and **Ebb & Flow (flood-and-drain)** — each with 13 in-depth guides, from first principles to automation, on a **$150–$600 budget**.

---

## Choose Your System

| | NFT — Nutrient Film Technique | Ebb & Flow — Flood & Drain |
|---|---|---|
| **How it works** | Thin film of solution flows continuously past bare roots | Table floods periodically, then fully drains back to reservoir |
| **Media** | Minimal — clay pebbles in net pots only | Substantial — 10–15cm LECA fill in flood tables |
| **Power failure risk** | High — roots dry in 15–30 min | Moderate — media buffers 8–24h |
| **Timer failure risk** | Low | **High** — pump stuck ON floods roots in 2–4h |
| **Best for** | Leafy greens, herbs, fast succession crops | Leafy greens + fruiting crops (tomatoes, cucumbers, courgettes, peppers) |
| **Crop range** | Narrow — not for heavy/deep-rooted crops | Wide — handles virtually all non-root crops |
| **Complexity** | Medium | Medium |
| **Build cost** | $150–$500 | $200–$600 |
| **Guide set** | [`guide/nft/`](guide/nft/) | [`guide/ebb-and-flow/`](guide/ebb-and-flow/) |

Both systems share the same **Zone B (Microgreens)** and **Zone C (Root Veg Grow Bags)** designs. Only Zone A differs.

---

## Shared Reference Documents

| Document | Description |
|----------|-------------|
| [`zones.md`](zones.md) | Full zone layout with spatial diagrams, dimensions, plumbing routes, and maintenance access map |
| [`guide/glossary.md`](guide/glossary.md) | All acronyms, abbreviations, and technical terms used across both guide sets — nutrients, units, electronics, materials, and methods |

---

## NFT Guide Library

> 4 channels, continuous flow, minimal media. Best for high-turnover leafy greens and herbs.

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

---

## Ebb & Flow Guide Library

> 2 flood tables, timer-controlled cycles, LECA media. Best for fruiting crops alongside leafy greens.

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

---

## Cross-System Comparison Guides

> Running both systems, or deciding between them? These guides compare NFT and E&F side-by-side on the topics where the systems differ most.

| # | File | What It Covers |
|---|------|----------------|
| 01 | [`guide/compare/01-nutrients.md`](guide/compare/01-nutrients.md) | EC management, media EC vs reservoir EC, salt accumulation, flush protocol, nutrient recipes, deficiency patterns |
| 02 | [`guide/compare/02-crops.md`](guide/compare/02-crops.md) | Which crops belong in which system, yield estimates, succession calendars, transplanting, crop-specific problems |
| 03 | [`guide/compare/03-automation.md`](guide/compare/03-automation.md) | Failure mode hierarchies, sensor priorities, drain confirmation vs flow confirmation, alert logic, two-system dashboard |
| 04 | [`guide/compare/04-cost.md`](guide/compare/04-cost.md) | Build costs by tier, running costs, yield value, payback periods, where each system saves, spend priorities |

---

## Quick-Start Paths

### NFT — new to hydroponics
1. **[NFT Guide 00 — System Overview](guide/nft/00-system-overview.md)** — inventory, build timeline, grow calendar
2. **[`zones.md`](zones.md)** — visualise the space
3. **[NFT Guide 11 — Build](guide/nft/11-build-guide.md)** — construct the system
4. **[NFT Guide 01 — Basics](guide/nft/01-nft-basics.md)** — understand how NFT works
5. **[NFT Guide 02 — Nutrients](guide/nft/02-nutrient-solution.md)** — mix your first solution
6. **[NFT Guide 06 — Crops](guide/nft/06-crops.md)** — plant selection and care
7. **[NFT Guide 08 — Maintenance](guide/nft/08-system-maintenance.md)** — keep it running

### Ebb & Flow — want fruiting crops
1. **[E&F Guide 00 — System Overview](guide/ebb-and-flow/00-system-overview.md)** — inventory, build timeline, grow calendar
2. **[E&F Guide 01 — Basics](guide/ebb-and-flow/01-ebb-flow-basics.md)** — understand flood-drain and timer safety
3. **[E&F Guide 05 — Media](guide/ebb-and-flow/05-growing-media.md)** — LECA preparation (do this first)
4. **[E&F Guide 11 — Build](guide/ebb-and-flow/11-build-guide.md)** — construct the system
5. **[E&F Guide 02 — Nutrients](guide/ebb-and-flow/02-nutrient-solution.md)** — mix and manage solution with media
6. **[E&F Guide 06 — Crops](guide/ebb-and-flow/06-crops.md)** — full crop guide including tomatoes, cucumbers, courgettes
7. **[E&F Guide 08 — Maintenance](guide/ebb-and-flow/08-system-maintenance.md)** — flood cycle checks and salt management
8. **[E&F Guide 13 — Automation](guide/ebb-and-flow/13-automation.md)** — drain confirmation sensor (strongly recommended)

---

*Last updated: March 2026*

---

<!-- copyright -->
*Copyright (c) 2026 UncleJS. Licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) — free to share and adapt for non-commercial purposes with attribution.*
