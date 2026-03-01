# Zone Layout & Spatial Design
## Outdoor Hybrid Hydroponics Station

---

## Overview

The hybrid growing station is designed to occupy a **backyard footprint of approximately 4m × 3m** (12m²). This is enough for the full three-zone system with clearance for maintenance access on all sides and a comfortable working aisle.

The station is oriented with the **long axis running east–west** so that the south-facing side of the channels receives maximum sun exposure in the Northern Hemisphere. Adjust to north-facing if you are in the Southern Hemisphere.

---

## Full Site Layout Map (Top-Down View)

```mermaid
flowchart TD
    NORTH["NORTH ↑"]:::label
    SOUTH["SOUTH — direction of sunlight ↓"]:::label

    subgraph SITE["Site Footprint  ←  4.0 metres wide  →"]
        WB["WIND BREAK / FENCE / TRELLIS MESH\n(north edge)"]

        subgraph ZA["ZONE A — NFT CHANNEL ARRAY\nFrame height: 80 cm"]
            direction LR
            RES["RES\nReservoir 80L"] --> P["P\nPump"] --> M["M\nManifold"]
            M --> CH1["CH1 ══════════ ▶ D\n(75mm, 2.4m long)"]
            M --> CH2["CH2 ══════════ ▶ D\n(75mm, 2.4m long)"]
            M --> CH3["CH3 ══════════ ▶ D\n(75mm, 2.4m long)"]
            M --> CH4["CH4 ══════════ ▶ D\n(100mm wide channel, 2.4m long)"]
        end

        subgraph SOUTH_ROW["South row"]
            direction LR
            subgraph ZB["ZONE B\nMicrogreens Tray Shelf\n2-tier"]
            end
            subgraph ZC["ZONE C\nRoot Veg Bags\nB B B\nB B B"]
            end
        end

        BENCH["WORK / MIXING BENCH"]
        STORE["STORAGE BOX"]
    end

    NORTH --> SITE
    SITE --> SOUTH

    classDef label fill:none,stroke:none,font-weight:bold
```
> **Legend:** RES = Reservoir · P = Pump · M = Manifold · D = Drain return · CH1–4 = NFT channels · B = Grow bag · ══ = NFT channel with net pot holes

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

---

## Zone A — NFT Channel Array (Detailed)

### Frame Side-View Diagram

```mermaid
block-beta
    columns 3
    HIGH["HIGH END\n(inlet)\n80 cm post"]:1
    CHANNELS:1
    LOW["LOW END\n(drain)\n72 cm post"]:1

    block:CHANNELS:1
        columns 1
        CH1["CH1 — 75mm square tube"]
        CH2["CH2 — 75mm square tube"]
        CH3["CH3 — 75mm square tube"]
        CH4["CH4 — 100mm square tube"]
    end

    SLOPE["Slope: 8 cm drop over 2.4 m = 1:30 ratio (3.3%)\nChannels rest on cross-supports at each end\n←────────────── 2.4 metres ──────────────→"]:3
```

### Channel Spacing (Front-View Cross Section)

```mermaid
block-beta
    columns 5
    RAIL["Frame top rail\n←────────── ~1.0 metre ──────────→"]:5
    CH1["CH1\n75 mm"]:1
    GAP1[" "]:1
    CH2["CH2\n75 mm"]:1
    GAP2[" "]:1
    CH3["CH3\n75 mm"]:1
    CH4["CH4\n100 mm"]:2
    NOTE["↕ 15 cm gap between channels for airflow"]:3
```

### Net Pot Hole Layout Per Channel

```mermaid
flowchart LR
    INLET["← inlet end"]
    P1["[O]\nSite 1"] --> P2["[O]\nSite 2"] --> P3["[O]\nSite 3"] --> P4["[O]\nSite 4"] --> P5["[O]\nSite 5"] --> P6["[O]\nSite 6"] --> P7["[O]\nSite 7 (CH1–3)"]
    INLET --> P1
    P7 --> DRAIN["drain end →"]

    W1["[O]\nSite 1"] --> W2["[O]\nSite 2"] --> W3["[O]\nSite 3"] --> W4["[O]\nSite 4"] --> W5["[O]\nSite 5"] --> W6["[O]\nSite 6"]
    W6 --> DRAIN4["drain end →"]

    note1["CH1–3: 75mm channel · 50mm net pots · 230mm spacing\n11 sites per channel (50mm edge buffer each end)\nTotal CH1–3: 11 × 3 = 33 sites"]
    note2["CH4: 100mm channel · 75mm net pots · 300mm spacing\n7 plant sites"]
    note3["Total Zone A sites: (11 × 3) + 7 = 40 plant sites"]
```

### Reservoir Placement

```mermaid
flowchart TD
    RES["RESERVOIR 80L\n(placed BESIDE frame at LOW end of slope)"]
    LID["Lid with 2 holes:\n1. Pump power cable\n2. Inlet / return pipe"]
    BODY["Exterior: painted white\n+ insulated with foam sheet"]
    POS["Position: low end of channels\nso gravity returns flow naturally.\nShade: under the frame or\nwrapped with reflective foam."]

    RES --> LID
    LID --> BODY
    BODY --> POS
```

### Plumbing Route

```mermaid
flowchart TD
    RES1["RESERVOIR"]
    PUMP["PUMP\nsubmersible · 600–800 L/h\nsitting on reservoir floor"]
    OUTLET["25mm outlet pipe\nup through lid"]
    MANIFOLD["25mm PVC manifold\nruns along HIGH end of frame"]
    CH1["CH1\n13mm inlet tube"]
    CH2["CH2\n13mm inlet tube"]
    CH3["CH3\n13mm inlet tube"]
    CH4["CH4\n13mm inlet tube"]
    RETURN["19–25mm return pipe\nruns along LOW end of frame · gravity"]
    RES2["RESERVOIR\n← gravity drain-back · no second pump needed"]

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
        H80["80 cm\n(Tier 2 height)"] TIER2["Tier 2 trays\n← top tier"]
        H40["40 cm\n(Tier 1 height)"] TIER1["Tier 1 trays\n← bottom tier"]
    end

    DIMS["Shelf: 60 cm wide × 55 cm deep × 90 cm tall\nBuild from: 2×4 timber + plywood, or wire shelving unit"]:3
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

---

## Zone C — Root Vegetable Grow Bags (Detailed)

### Bag Layout

```mermaid
block-beta
    columns 3
    TITLE["TOP VIEW — Grow Bag Layout"]:3
    B1["Radish 20L"] B2["Radish 20L"] B3["Beetroot 20L"]
    B4["Carrot 30L"] B5["Carrot 30L"] B6["Carrot 30L"]
    NOTE["All bags sit on a slatted wooden pallet or gravel/bark chip bed for drainage.\nEnsure no standing water under bags."]:3
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
    NOTE["Moisten coco before filling.\nDo NOT use garden soil."]
```

### Fertigation Schedule (Zone C)

| Crop Stage | Frequency | Solution EC | pH |
|------------|-----------|-------------|-----|
| Seedling (0–2 weeks) | 1× daily | 0.8–1.0 mS/cm | 6.0–6.5 |
| Vegetative (2–6 weeks) | 2× daily | 1.2–1.6 mS/cm | 6.0–6.5 |
| Root bulking (6+ weeks) | 2× daily | 1.6–2.0 mS/cm | 6.0–6.5 |

**Method:** Mix nutrient solution in a watering can. Water until runoff drains from bag bottom (20% runoff recommended to prevent salt buildup).

---

## Shade Cloth & Environmental Controls

### Shade Cloth Positioning

```mermaid
flowchart TD
    CLOTH["Shade cloth 40%\nstretched over bamboo/conduit frame\n(summer: June–August peak)"]
    GAP["↓ 30–50 cm clearance ↓"]
    ZONES["NFT CHANNELS  ·  ZONE B  ·  ZONE C"]
    NOTE["Deploy when daily temps exceed 28°C\nor plants show heat stress.\nRemove in overcast / autumn conditions\nto maximise light."]

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

---

## Maintenance Access Map

```mermaid
flowchart TD
    NORTH["NORTH SIDE\nWind break — no access needed"]
    NFT["NFT CHANNELS\nAccessible from SOUTH SIDE\n→ Net pots · channel inspection · inlet check"]
    RES_ACCESS["RESERVOIR — LOW END (right/east side)\n→ Fill point · pump check · EC/pH testing"]
    ZB_ACCESS["ZONE B SHELF — EAST side\n→ Tray swap · watering · harvest"]
    ZC_ACCESS["ZONE C BAGS — SOUTH-EAST corner\n→ Daily watering · harvest"]
    BENCH_ACCESS["WORK BENCH — SOUTH side, central\n→ Nutrient mixing · propagation · tools"]
    SOUTH["SOUTH SIDE\nMain access aisle — 0.6 m wide"]

    NORTH --> NFT --> RES_ACCESS --> ZB_ACCESS --> ZC_ACCESS --> BENCH_ACCESS --> SOUTH
```

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

---

<!-- copyright -->
*Copyright (c) 2026 UncleJS. Licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) — free to share and adapt for non-commercial purposes with attribution.*
