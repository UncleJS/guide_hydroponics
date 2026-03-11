# Zone Layout & Spatial Design
## Outdoor Hybrid Hydroponics Station

[![Docs: Home Hydroponics](https://img.shields.io/badge/Docs-Home%20Hydroponics-2d6a4f)](README.md)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)


---

## Table of Contents

- [Overview](#overview)
- [Full Site Layout Map (Top-Down View)](#full-site-layout-map-top-down-view)
- [Dimensions & Clearances](#dimensions-clearances)
- [Zone A — NFT Channel Array (Detailed)](#zone-a-nft-channel-array-detailed)
  - [Frame Side-View Diagram](#frame-side-view-diagram)
  - [Channel Spacing (Front-View Cross Section)](#channel-spacing-front-view-cross-section)
  - [Net Pot Hole Layout Per Channel](#net-pot-hole-layout-per-channel)
  - [Reservoir Placement](#reservoir-placement)
  - [Plumbing Route](#plumbing-route)
- [Zone B — Microgreens Tray Station (Detailed)](#zone-b-microgreens-tray-station-detailed)
  - [Shelf Structure](#shelf-structure)
  - [Tray Configuration](#tray-configuration)
  - [Microgreens Protocol Summary](#microgreens-protocol-summary)
- [Zone C — Root Vegetable Grow Bags (Detailed)](#zone-c-root-vegetable-grow-bags-detailed)
  - [Bag Layout](#bag-layout)
  - [Bag Sizes and Depths](#bag-sizes-and-depths)
  - [Media Mix for Grow Bags](#media-mix-for-grow-bags)
  - [Fertigation Schedule (Zone C)](#fertigation-schedule-zone-c)
- [Shade Cloth & Environmental Controls](#shade-cloth-environmental-controls)
  - [Shade Cloth Positioning](#shade-cloth-positioning)
  - [Frost Fleece Deployment](#frost-fleece-deployment)
  - [Wind Break](#wind-break)
- [Maintenance Access Map](#maintenance-access-map)
- [Utility Requirements](#utility-requirements)

---


## Overview

The hybrid growing station is designed to occupy a **backyard footprint of approximately 4m × 3m** (12m²). This is enough for the full three-zone system with clearance for maintenance access on all sides and a comfortable working aisle.

The station is oriented with the **long axis running east–west** so that the south-facing side of the channels receives maximum sun exposure in the Northern Hemisphere. Adjust to north-facing if you are in the Southern Hemisphere.

[↑ Back to TOC](#table-of-contents)

---

## Full Site Layout Map (Top-Down View)

**↑ NORTH — wind break / fence / trellis mesh (north edge)**

```mermaid
flowchart TD
    WB["WIND BREAK / FENCE / TRELLIS MESH — north edge"]

    subgraph ZA["ZONE A — NFT CHANNEL ARRAY  (frame height: 80 cm)"]
        RES["RES — Reservoir 80L"] --> P["P — Pump"] --> M["M — Manifold"]
        M --> CH1["CH1 ══════════ D  (75mm, 2.4m)"]
        M --> CH2["CH2 ══════════ D  (75mm, 2.4m)"]
        M --> CH3["CH3 ══════════ D  (75mm, 2.4m)"]
        M --> CH4["CH4 ══════════ D  (100mm, 2.4m)"]
    end

    subgraph ZB["ZONE B — Microgreens Tray Shelf  (2-tier)"]
        B["Tier 1 trays · Tier 2 trays"]
    end

    subgraph ZC["ZONE C — Root Veg Bags"]
        C["B B B<br/>B B B"]
    end

    BENCH["WORK / MIXING BENCH"]
    STORE["STORAGE BOX"]

    WB --> ZA
    ZA --> ZB
    ZA --> ZC
    ZB --> BENCH
    ZC --> BENCH
    BENCH --> STORE
```

**↓ SOUTH — direction of sunlight · main access aisle (0.6 m)**

> **Legend:** RES = Reservoir · P = Pump · M = Manifold · D = Drain return · CH1–4 = NFT channels · B = Grow bag · ══ = NFT channel with net pot holes
> **Legend:** RES = Reservoir · P = Pump · M = Manifold · D = Drain return · CH1–4 = NFT channels · B = Grow bag · ══ = NFT channel with net pot holes

[↑ Back to TOC](#table-of-contents)

---

## Dimensions & Clearances

| Area | Dimensions | Notes |
|------|-----------|-------|
| Total site footprint | 4.0m × 3.0m | Includes all 3 zones and work area |
| Zone A (NFT array) | 2.6m × 1.2m | Frame + reservoir beside it |
| Zone B (microgreens shelf) | 0.6m × 0.5m | 2-tier shelf, fits 3 trays per tier |
| Zone C (grow bags) | 1.2m × 0.6m | 6 bags, 2 rows of 3 |
| Working aisle | 0.6m | Front access to all zones |
| Work/mixing bench | 0.8m × 0.5m | Optional — a table or board on sawhorses |
| Wind break clearance | 0.3m | From fence/wall to system |

**Minimum workable footprint:** 3.5m × 2.5m if space is tight — compress Zone B/C side by side under a shelf.

[↑ Back to TOC](#table-of-contents)

---

## Zone A — NFT Channel Array (Detailed)

### Frame Side-View Diagram

```mermaid
block-beta
    columns 3
    HIGH["HIGH END<br/>(inlet)<br/>80 cm post"]:1
    CHANNELS:1
    LOW["LOW END<br/>(drain)<br/>72 cm post"]:1

    block:CHANNELS:1
        columns 1
        CH1["CH1 — 75mm square tube"]
        CH2["CH2 — 75mm square tube"]
        CH3["CH3 — 75mm square tube"]
        CH4["CH4 — 100mm square tube"]
    end

    SLOPE["Slope: 8 cm drop over 2.4 m = 1:30 ratio (3.3%)<br/>Channels rest on cross-supports at each end<br/>←────────────── 2.4 metres ──────────────→"]:3
```

### Channel Spacing (Front-View Cross Section)

```mermaid
block-beta
    columns 5
    RAIL["Frame top rail<br/>←────────── ~1.0 metre ──────────→"]:5
    CH1["CH1<br/>75 mm"]:1
    GAP1[" "]:1
    CH2["CH2<br/>75 mm"]:1
    GAP2[" "]:1
    CH3["CH3<br/>75 mm"]:1
    CH4["CH4<br/>100 mm"]:2
    NOTE["↕ 15 cm gap between channels for airflow"]:3
```

### Net Pot Hole Layout Per Channel

```mermaid
flowchart LR
    INLET["← inlet end"]
    P1["[O]<br/>Site 1"] --> P2["[O]<br/>Site 2"] --> P3["[O]<br/>Site 3"] --> P4["[O]<br/>Site 4"] --> P5["[O]<br/>Site 5"] --> P6["[O]<br/>Site 6"] --> P7["[O]<br/>Site 7 (CH1–3)"]
    INLET --> P1
    P7 --> DRAIN["drain end →"]

    W1["[O]<br/>Site 1"] --> W2["[O]<br/>Site 2"] --> W3["[O]<br/>Site 3"] --> W4["[O]<br/>Site 4"] --> W5["[O]<br/>Site 5"] --> W6["[O]<br/>Site 6"]
    W6 --> DRAIN4["drain end →"]

    note1["CH1–3: 75mm channel · 50mm net pots · 230mm spacing<br/>11 sites per channel (50mm edge buffer each end)<br/>Total CH1–3: 11 × 3 = 33 sites"]
    note2["CH4: 100mm channel · 75mm net pots · 300mm spacing<br/>7 plant sites"]
    note3["Total Zone A sites: (11 × 3) + 7 = 40 plant sites"]
```

### Reservoir Placement

```mermaid
flowchart TD
    RES["RESERVOIR 80L<br/>(placed BESIDE frame at LOW end of slope)"]
    LID["Lid with 2 holes:<br/>1. Pump power cable<br/>2. Inlet / return pipe"]
    BODY["Exterior: painted white<br/>+ insulated with foam sheet"]
    POS["Position: low end of channels<br/>so gravity returns flow naturally.<br/>Shade: under the frame or<br/>wrapped with reflective foam."]

    RES --> LID
    LID --> BODY
    BODY --> POS
```

### Plumbing Route

```mermaid
flowchart TD
    RES1["RESERVOIR"]
    PUMP["PUMP<br/>submersible · 600–800 L/h<br/>sitting on reservoir floor"]
    OUTLET["25mm outlet pipe<br/>up through lid"]
    MANIFOLD["25mm PVC manifold<br/>runs along HIGH end of frame"]
    CH1["CH1<br/>13mm inlet tube"]
    CH2["CH2<br/>13mm inlet tube"]
    CH3["CH3<br/>13mm inlet tube"]
    CH4["CH4<br/>13mm inlet tube"]
    RETURN["19–25mm return pipe<br/>runs along LOW end of frame · gravity"]
    RES2["RESERVOIR<br/>← gravity drain-back · no second pump needed"]

    RES1 --> PUMP --> OUTLET --> MANIFOLD
    MANIFOLD --> CH1
    MANIFOLD --> CH2
    MANIFOLD --> CH3
    MANIFOLD --> CH4
    CH1 --> RETURN
    CH2 --> RETURN
    CH3 --> RETURN
    CH4 --> RETURN
    RETURN --> RES2
```

[↑ Back to TOC](#table-of-contents)

---

## Zone B — Microgreens Tray Station (Detailed)

### Shelf Structure

```mermaid
block-beta
    columns 3

    block:TOPVIEW["TOP VIEW — shelf"]:3
        columns 3
        T1["TRAY 1"] T2["TRAY 2"] T3["TRAY 3"]
        T4["TRAY 4"] T5["TRAY 5"] T6["TRAY 6"]
    end

    block:SIDEVIEW["SIDE VIEW"]:3
        columns 2
        H80["80 cm<br/>(Tier 2 height)"] TIER2["Tier 2 trays<br/>← top tier"]
        H40["40 cm<br/>(Tier 1 height)"] TIER1["Tier 1 trays<br/>← bottom tier"]
    end

    DIMS["Shelf: 60 cm wide × 55 cm deep × 90 cm tall<br/>Build from: 2×4 timber + plywood, or wire shelving unit"]:3
```

### Tray Configuration

| Tray | Crop | Sow Date Rotation |
|------|------|-------------------|
| Tray 1 | Sunflower shoots | Week 1 |
| Tray 2 | Pea shoots | Week 1 |
| Tray 3 | Radish microgreens | Week 2 |
| Tray 4 | Broccoli microgreens | Week 2 |
| Tray 5 | Amaranth | Week 3 |
| Tray 6 | Wheatgrass | Week 3 |

**Rotation cycle:** Sow a new tray every 3–5 days to maintain continuous harvest.

### Microgreens Protocol Summary

1. **Fill tray** with 2–3cm of moistened coco coir
2. **Broadcast seeds** evenly (no spacing — dense mat)
3. **Press seeds** gently into media with a flat board
4. **Blackout phase:** Cover with empty tray + weight for 2–4 days (germination)
5. **Light phase:** Uncover when shoots reach 2–3cm, place in full outdoor light (or partial shade in peak summer)
6. **Water:** Mist surface 2× daily during blackout, bottom-water after uncovering
7. **Harvest:** Cut at soil level when first true leaves appear (7–14 days depending on variety)

[↑ Back to TOC](#table-of-contents)

---

## Zone C — Root Vegetable Grow Bags (Detailed)

### Bag Layout

```mermaid
block-beta
    columns 3
    TITLE["TOP VIEW — Grow Bag Layout"]:3
    B1["Radish 20L"] B2["Radish 20L"] B3["Beetroot 20L"]
    B4["Carrot 30L"] B5["Carrot 30L"] B6["Carrot 30L"]
    NOTE["All bags sit on a slatted wooden pallet or gravel/bark chip bed for drainage.<br/>Ensure no standing water under bags."]:3
```

### Bag Sizes and Depths

| Crop | Bag Size | Depth Needed | Why |
|------|----------|-------------|-----|
| Radishes | 20L (round, wide) | 20–25cm | Short tap root, wide spread |
| Beetroot | 20L (round, wide) | 20–25cm | Moderate root depth |
| Carrots | 30L (tall/deep bag) | 30–40cm | Long tap root needs depth |

### Media Mix for Grow Bags

```mermaid
block-beta
    columns 1
    TITLE["PER 20L BAG — Media Mix"]
    COCO["Coco coir · 12L · 60%"]
    PERL["Perlite · 6L · 30%"]
    VERM["Vermiculite · 2L · 10%"]
    NOTE["Moisten coco before filling.<br/>Do NOT use garden soil."]
```

### Fertigation Schedule (Zone C)

| Crop Stage | Frequency | Solution EC | pH |
|------------|-----------|-------------|-----|
| Seedling (0–2 weeks) | 1× daily | 0.8–1.0 mS/cm | 6.0–6.5 |
| Vegetative (2–6 weeks) | 2× daily | 1.2–1.6 mS/cm | 6.0–6.5 |
| Root bulking (6+ weeks) | 2× daily | 1.6–2.0 mS/cm | 6.0–6.5 |

**Method:** Mix nutrient solution in a watering can. Water until runoff drains from bag bottom (20% runoff recommended to prevent salt buildup).

[↑ Back to TOC](#table-of-contents)

---

## Shade Cloth & Environmental Controls

### Shade Cloth Positioning

```mermaid
flowchart TD
    CLOTH["Shade cloth 40%<br/>stretched over bamboo/conduit frame<br/>(summer: June–August peak)"]
    GAP["↓ 30–50 cm clearance ↓"]
    ZONES["NFT CHANNELS  ·  ZONE B  ·  ZONE C"]
    NOTE["Deploy when daily temps exceed 28°C<br/>or plants show heat stress.<br/>Remove in overcast / autumn conditions<br/>to maximise light."]

    CLOTH --> GAP --> ZONES
    ZONES --> NOTE
```

### Frost Fleece Deployment

```
  Autumn / cold nights (below 5°C):

  Drape horticultural fleece (30–50g/m²) over entire zone.
  Anchor edges with clips or stones.
  Remove during warm sunny days — fleece traps heat and humidity.

  Do NOT leave fleece on during heavy rain — weight can damage plants.
```

### Wind Break

- Install mesh fencing or slatted timber on the **north and east** sides
- Leave south and west open for sunlight and gentle air movement
- Secure all channels and the reservoir to the frame with cable ties or straps in high-wind conditions
- Taller plants (tomatoes, peppers) need individual staking/trellis regardless

[↑ Back to TOC](#table-of-contents)

---

## Maintenance Access Map

```mermaid
flowchart TD
    NORTH["NORTH SIDE<br/>Wind break — no access needed"]
    NFT["NFT CHANNELS<br/>Accessible from SOUTH SIDE<br/>→ Net pots · channel inspection · inlet check"]
    RES_ACCESS["RESERVOIR — LOW END (right/east side)<br/>→ Fill point · pump check · EC/pH testing"]
    ZB_ACCESS["ZONE B SHELF — EAST side<br/>→ Tray swap · watering · harvest"]
    ZC_ACCESS["ZONE C BAGS — SOUTH-EAST corner<br/>→ Daily watering · harvest"]
    BENCH_ACCESS["WORK BENCH — SOUTH side, central<br/>→ Nutrient mixing · propagation · tools"]
    SOUTH["SOUTH SIDE<br/>Main access aisle — 0.6 m wide"]

    NORTH --> NFT --> RES_ACCESS --> ZB_ACCESS --> ZC_ACCESS --> BENCH_ACCESS --> SOUTH
```

[↑ Back to TOC](#table-of-contents)

---

## Utility Requirements

| Utility | Requirement | Notes |
|---------|------------|-------|
| **Electricity** | 1 outdoor socket within ~3m | For submersible pump (5–15W). Use outdoor-rated extension lead and waterproof socket cover |
| **Water** | Garden hose or tap within ~5m | For topping up reservoir and mixing nutrient solution |
| **Drainage** | Ground drainage or drain slab | Overflow from reservoir and runoff from grow bags must drain away |
| **Storage** | Weatherproof box (optional) | For pH/EC meters, nutrients, spare fittings — keep out of sunlight |

---

*See [`guide/nft/11-build-guide.md`](guide/nft/11-build-guide.md) for NFT construction instructions*

[↑ Back to TOC](#table-of-contents)

---

<!-- copyright -->
*Copyright (c) 2026 UncleJS. Licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) — free to share and adapt for non-commercial purposes with attribution and ShareAlike.*
