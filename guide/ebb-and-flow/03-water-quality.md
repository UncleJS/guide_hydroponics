# Guide 03 — Water Quality
## Sources, Testing, Treatment, and Management

[![Docs: Home Hydroponics](https://img.shields.io/badge/Docs-Home%20Hydroponics-2d6a4f)](../../README.md)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)


---

## Table of Contents

- [1. Why Starting Water Quality Matters](#1-why-starting-water-quality-matters)
- [2. TDS (Total Dissolved Solids) and EC Baseline](#2-tds-total-dissolved-solids-and-ec-baseline)
  - [Testing Your Source Water](#testing-your-source-water)
  - [Why Source EC Matters](#why-source-ec-matters)
  - [Interpreting Your Local Water Report](#interpreting-your-local-water-report)
- [3. Tap Water: Chlorine, Chloramine, and Hardness](#3-tap-water-chlorine-chloramine-and-hardness)
  - [Chlorine vs Chloramine — Critical Difference](#chlorine-vs-chloramine-critical-difference)
  - [Hard Water Management in E&F](#hard-water-management-in-ef)
- [4. Well Water Issues](#4-well-water-issues)
- [5. Reverse Osmosis (RO) — When It's Worth It](#5-reverse-osmosis-ro-when-its-worth-it)
  - [What RO Does](#what-ro-does)
  - [Is RO Worth It for This System?](#is-ro-worth-it-for-this-system)
- [6. Rainwater Harvesting](#6-rainwater-harvesting)
  - [Rainwater Characteristics](#rainwater-characteristics)
  - [Collection System](#collection-system)
- [7. pH Testing Methods Compared](#7-ph-testing-methods-compared)
  - [Digital pH Meters (Recommended)](#digital-ph-meters-recommended)
  - [Calibrating a pH Meter](#calibrating-a-ph-meter)
- [8. EC Meters: Types, Calibration, and Use](#8-ec-meters-types-calibration-and-use)
  - [EC Meter Types](#ec-meter-types)
  - [Testing in E&F: Reservoir vs Media EC](#testing-in-ef-reservoir-vs-media-ec)
- [9. pH Up and pH Down — Safe Handling](#9-ph-up-and-ph-down-safe-handling)
  - [pH Adjustment Protocol for E&F](#ph-adjustment-protocol-for-ef)
- [10. Water Temperature Management Outdoors](#10-water-temperature-management-outdoors)
  - [The Outdoor Heat Problem](#the-outdoor-heat-problem)
  - [E&F Reservoir Positioning Advantage](#ef-reservoir-positioning-advantage)
  - [Management Strategies](#management-strategies)
- [11. Algae Prevention in E&F Systems](#11-algae-prevention-in-ef-systems)
  - [E&F Algae Risk Profile](#ef-algae-risk-profile)
  - [Prevention Checklist](#prevention-checklist)
  - [Treatment](#treatment)
- [12. Salt Accumulation and Flush Scheduling](#12-salt-accumulation-and-flush-scheduling)
  - [EC Monitoring Protocol](#ec-monitoring-protocol)
- [13. Full Water Change Protocol](#13-full-water-change-protocol)
  - [Step-by-Step Reservoir Change](#step-by-step-reservoir-change)

---


## 1. Why Starting Water Quality Matters

In all hydroponic systems, the quality of your source water determines your baseline. In Ebb & Flow specifically, water quality issues compound in a way that is unique to media-based systems: poor source water not only affects the reservoir chemistry but also accumulates in the clay pebble or coco coir media over repeated flood cycles. A problem that might cause one week of stress in an NFT system can persist for months as mineral deposits in flood table media.

Your source water directly affects:

- **EC baseline:** All tap water contains dissolved minerals. These contribute to total EC before you add a single nutrient. The baseline must be known and subtracted when targeting reservoir EC.
- **pH stability:** Hard (bicarbonate-rich) water resists pH adjustment and continuously pushes pH upward — requiring more pH-down and more frequent corrections in both the reservoir and the media.
- **Nutrient interference:** High calcium or magnesium in source water may create Ca:Mg imbalance, especially when combined with media buffering effects.
- **Pathogen introduction:** Any untreated surface water or collected roof water can introduce Pythium, algae, and bacteria that spread to every plant in the flood cycle.
- **Media deposit risk:** Every flood cycle leaves some source water minerals behind in the media pore spaces — hard water with high mineral content accelerates salt accumulation.

**First step before filling the reservoir for the first time:** Test your source water's EC and pH. This information determines how you mix nutrients, how you manage pH, and whether you need pre-treatment.

[↑ Back to TOC](#table-of-contents)

---


## 2. TDS (Total Dissolved Solids) and EC Baseline

### Testing Your Source Water

Before adding any nutrients, measure your tap water straight from the tap:

```
  WHAT TO LOOK FOR:

  Source water EC:    0.0–0.2 mS/cm   → Excellent (soft/RO/rainwater)
                      0.2–0.4 mS/cm   → Good (mild minerals, workable)
                      0.4–0.6 mS/cm   → Acceptable (hard water — monitor media accumulation)
                      0.6–1.0 mS/cm   → Problematic — consider RO or rainwater blending
                      1.0+ mS/cm      → RO or rainwater essential

  Source water pH:    6.5–7.5         → Typical tap range
                      7.5–9.0         → Hard/alkaline — needs correction every fill
                      < 6.5           → Acidic (unusual for tap)
```

### Why Source EC Matters

Your source water EC is a floor you start from — all nutrients are added on top of it:

```
  TOTAL EC = SOURCE WATER EC + NUTRIENTS EC

  Example 1 (soft water):
  Source EC: 0.1 mS/cm + Nutrients: 1.5 mS/cm = Final: 1.6 mS/cm ← near target

  Example 2 (hard water):
  Source EC: 0.6 mS/cm + Nutrients: 1.5 mS/cm = Final: 2.1 mS/cm ← too high for lettuce

  E&F ADDITIONAL CONCERN:
  Hard water top-ups over several days:
  ─ Each top-up adds more Ca/Mg minerals to the media
  ─ Even if reservoir EC stays in range, media mineral load increases
  ─ After 2–3 weeks, media EC can exceed reservoir EC by 0.5–1.0 mS/cm
  ─ Hard water growers need more frequent media flushes (every 2–3 weeks vs monthly)
```

### Interpreting Your Local Water Report

Most municipal water suppliers publish annual quality reports. Look for:
- **Total Dissolved Solids (TDS)** or **electrical conductivity** — your EC baseline
- **Hardness** (as CaCO₃ or mg/L Ca+Mg) — affects pH buffering and media accumulation
- **Chlorine/chloramine** — affects roots and beneficial microbes
- **pH** — your starting point before nutrient addition
- **Iron, manganese, copper** — can cause problems at elevated levels

[↑ Back to TOC](#table-of-contents)

---


## 3. Tap Water: Chlorine, Chloramine, and Hardness

### Chlorine vs Chloramine — Critical Difference

| Property | Chlorine (Cl₂) | Chloramine (NH₂Cl) |
|----------|---------------|-------------------|
| **Used by** | Older water systems | Most modern municipal systems |
| **Removal method** | Leave to stand 24h, or activated carbon | **Cannot be removed by standing** |
| **How to remove** | Aeration, activated carbon, UV | Vitamin C (ascorbic acid), sodium thiosulphate, activated carbon |
| **Harm to plants** | Damages roots and microbes above ~2mg/L | Same, but persists longer |
| **Detection** | Smell dissipates after standing | No smell change after standing |

**E&F relevance:** In NFT, fresh water flows constantly through the system, diluting chlorine accumulation. In E&F, each flood cycle introduces the full chlorine/chloramine load of your source water directly to the root zone, then some of it stays in the media between floods. Over time, residual chlorine can stress or damage beneficial microbes in the media, especially for organic growers.

**Chloramine removal:**
```
  METHOD 1 — Vitamin C (Ascorbic Acid):
  Add 1 gram per 40 litres of water. Neutralises chloramine within minutes.
  Slightly lowers pH — adjust pH after adding.
  Buy food-grade vitamin C powder — inexpensive.

  METHOD 2 — Sodium Thiosulphate:
  Standard aquarium dechlorinator. Works in seconds.

  METHOD 3 — Activated Carbon Filter:
  In-line carbon block filter on your fill hose.
  Best permanent solution for frequent reservoir refilling.
```

### Hard Water Management in E&F

Hard water causes the same problems as in NFT (pH creep, scale, excess Ca/Mg) but with an additional E&F-specific problem: calcium carbonate scale deposits inside the clay pebble pore structure. Over a growing season this can:
- Permanently clog media pore spaces (reducing aeration and drainage)
- Create pH micro-zones inside the media that differ from the reservoir
- Require acid soaking of clay pebbles at season end to remove deposits

```
  HARD WATER MANAGEMENT STRATEGIES FOR E&F:

  Strategy 1 — Reduce Ca in nutrient recipe:
  If source water Ca > 100 mg/L, reduce Calcium Nitrate dose by 20–30%.
  Verify with a full water test or local water quality report.

  Strategy 2 — Acidify to neutralise bicarbonates:
  Phosphoric acid (pH Down) consumes bicarbonate as well as lowering pH.
  Hard water simply requires more pH-down per litre — this is normal.

  Strategy 3 — Blend with RO or rainwater:
  50/50 blend halves the mineral load. Most practical and cost-effective.

  Strategy 4 — Increase media flush frequency:
  With hard water, flush media every 2 weeks instead of monthly.
  Hard water deposits accumulate faster in pore spaces.

  Strategy 5 — End-of-season acid soak:
  Soak clay pebbles in pH 4.0–4.5 water for 24h to dissolve calcium carbonate.
  Follow with thorough rinsing and standard pH re-conditioning.
```

[↑ Back to TOC](#table-of-contents)

---


## 4. Well Water Issues

If you use well water, test it thoroughly before use. Common problems in well water relevant to E&F:

| Contaminant | Problem | E&F-Specific Risk | Solution |
|-------------|---------|-------------------|---------|
| **High iron (>0.3mg/L)** | Staining, pump blockage, iron toxicity | Iron deposits in clay pebbles — can clog media permanently | Sediment filter + iron removal; or RO |
| **High sulfur (rotten egg smell)** | Toxic to roots at high levels | Anaerobic smell masked by flood cycle noise | Activated carbon + aeration |
| **High hardness (Ca+Mg)** | pH creep, scale | Accelerated media mineral accumulation | Softener or RO; more frequent flushes |
| **Bacteria / E. coli** | Dangerous for edible crops | Flood cycle spreads pathogens to all plants | UV sterilisation or chlorination then dechlorination |
| **Nitrates (from agriculture)** | Adds to nutrient load unpredictably | EC baseline higher than expected | Test and adjust nutrient recipe accordingly |
| **Low pH (acidic)** | Corrosive | Leaches minerals from clay pebbles faster | pH Up to correct; test media EC weekly |

**Recommendation:** If using well water, buy a basic water test kit from a hardware store or send a sample to a lab before starting. The $15–$50 cost is trivial compared to losing a season of crops.

[↑ Back to TOC](#table-of-contents)

---


## 5. Reverse Osmosis (RO) — When It's Worth It

### What RO Does

Reverse osmosis forces water through a semi-permeable membrane that removes 95–99% of all dissolved solids, heavy metals, chlorine, chloramine, bacteria, and viruses. The result is near-pure water (EC: 0.00–0.05 mS/cm) with maximum nutrient control.

| Pros | Cons |
|------|------|
| Perfect baseline water (EC ~0.0) | Cost: $50–$200 for a basic unit |
| No chlorine/chloramine issues | Waste water: 3–4L waste per 1L RO water |
| No hard water scale in clay pebbles | Slow output: 50–200 L/day for home units |
| Maximum nutrient precision | Removes Ca/Mg — must add back via CalMag or Masterblend |
| Consistent results season to season | Membrane replacement every 1–2 years |

### Is RO Worth It for This System?

```
  DECISION GUIDE:

  Tap water EC < 0.3 mS/cm:      → RO unnecessary — tap water is fine
  Tap water EC 0.3–0.6 mS/cm:    → RO useful but not essential; blend or adjust recipe
  Tap water EC > 0.6 mS/cm:      → RO strongly recommended
  Hard water (CaCO₃ > 250 mg/L): → RO strongly recommended (prevents clay pebble scaling)
  Well water with iron/sulfur:    → RO recommended
  You are organic growing in E&F: → RO or rainwater preferred (chloramine harms microbes)
```

For a 100L reservoir requiring weekly full changes, a countertop RO unit with a 10–20L storage tank is sufficient. Fill slowly over 12–24 hours, store in the tank, use for reservoir fill.

[↑ Back to TOC](#table-of-contents)

---


## 6. Rainwater Harvesting

Outdoor systems have a natural advantage: free, soft, near-pure water falls from the sky. For an outdoor E&F system, rainwater is arguably the ideal source water.

### Rainwater Characteristics

- **EC:** 0.01–0.05 mS/cm — essentially mineral-free, perfect baseline
- **pH:** 5.5–6.5 — slightly acidic due to dissolved CO₂, often within ideal hydroponic range
- **Chlorine/chloramine:** None — natural water cycle
- **Contaminants:** Dust, bird droppings, roof material leachate (first-flush diverter removes most)

### Collection System

```mermaid
flowchart TD
    A["Roof area (any pitch)"] -->|rainwater| B["Guttering"]
    B --> C["First-flush diverter<br/>(discards first 5–10L per 25m² of roof<br/>— removes initial dirty wash-off)"]
    C --> D["Rainwater butt or IBC tank<br/>(200–1000L)"]
    D --> E["Outlet tap or siphon hose"]
    E --> F["Reservoir fill"]
    D:::tank
    classDef tank stroke-dasharray: 5 5
```

**Collection system rules:**
- Cover the tank — prevents algae, debris, and mosquito breeding
- Use a first-flush diverter — the first few litres from a roof carry bird droppings and dust; these should not enter your tank
- Use a fine mesh filter (200 micron) at the tank outlet before adding to your reservoir
- Test pH and EC when you first start using a new collection system

**Legality note:** Rainwater harvesting is permitted and encouraged in most of Europe, UK, Australia, and Canada. In the US it is now legal in nearly all states (historically restricted in a few western states). Check your local regulations before investing in a large system.

[↑ Back to TOC](#table-of-contents)

---


## 7. pH Testing Methods Compared

### Digital pH Meters (Recommended)

```
  HOW IT WORKS: Glass electrode measures H⁺ ion concentration electronically.

  Accuracy:    ±0.01–0.05 pH when calibrated
  Speed:       Reading stable in 10–30 seconds
  Key issue:   Requires regular calibration and storage in electrode storage solution

  Budget:      Vivosun, Dr.meter (~$12–$20) — acceptable, short electrode life
  Mid-range:   Apera PH20, Bluelab (~$35–$60) — excellent accuracy and durability
  Professional: Hanna HI98100+ (~$80+) — lab grade

  Recommendation: Apera PH20 for this system — auto-calibrating, reliable.

  NEVER store the electrode in distilled water or dry air — this destroys the
  glass membrane. Always store in electrode storage solution (KCl) or the cap
  that comes with the meter filled with storage solution.
```

**pH drops / test kits:** Cheap ($5–$10), no calibration, works for backup. Accuracy ±0.2–0.5 — acceptable for rough checks only.

**pH test strips:** Not recommended for nutrient solution — coloured solution masks colour comparison. ±0.5–1.0 accuracy. Use only as absolute last resort.

### Calibrating a pH Meter

```
  CALIBRATION PROCEDURE (2-point calibration):

  Materials:
  ─ pH 4.0 buffer solution (usually red/orange)
  ─ pH 7.0 buffer solution (usually yellow)
  ─ Distilled or RO water for rinsing

  Steps:
  1. Remove electrode from storage cap — rinse with distilled water
  2. Submerge in pH 7.0 buffer — wait for reading to stabilise — press CAL
  3. Rinse electrode with distilled water
  4. Submerge in pH 4.0 buffer — wait for reading to stabilise — press CAL
  5. Rinse with distilled water before each measurement
  6. Return to storage solution after use

  Calibrate: weekly during active growing season
  Replace electrode: every 12–18 months (or when calibration drifts >0.3 pH)

  E&F NOTE: Test reservoir pH AND media pH separately.
  Media pH test: press probe into moist media immediately after a flood cycle.
  Media pH is frequently 0.2–0.5 higher than reservoir pH in E&F systems.
```

[↑ Back to TOC](#table-of-contents)

---


## 8. EC Meters: Types, Calibration, and Use

### EC Meter Types

| Type | Accuracy | Cost | Notes |
|------|----------|------|-------|
| Basic pen meter | ±0.1 mS/cm | $10–$20 | Good enough for home use; single-point calibration |
| Mid-range digital | ±0.05 mS/cm | $20–$50 | Better accuracy, automatic temperature compensation |
| Combination EC/pH | ±0.1 EC, ±0.05 pH | $30–$80 | Convenient; acceptable accuracy for both |
| BlueLab Truncheon | ±0.1 mS/cm | $50+ | No display; LED indicators — highly durable |
| Professional inline | ±0.02 mS/cm | $100+ | Continuous monitoring with data logging |

**Critical feature:** Always buy a meter with **Automatic Temperature Compensation (ATC)**. EC readings change with temperature — a meter without ATC will give inaccurate readings in outdoor conditions where water temperature fluctuates.

### Testing in E&F: Reservoir vs Media EC

This is unique to media-based systems. Your management routine should include both measurements:

```
  E&F EC TESTING PROTOCOL:

  Test 1 — RESERVOIR (daily):
  ─ Dip probe directly into reservoir
  ─ This is your nutrient solution concentration
  ─ Target: crop-specific EC range (see Guide 02, Section 4)

  Test 2 — MEDIA EC (weekly):
  ─ Perform immediately after a flood cycle (media fully wet)
  ─ Method: push EC probe tip 3–5cm into clay pebbles
  ─ Read the EC while probe is in wet media
  ─ Compare to reservoir EC

  INTERPRETING MEDIA EC:
  Media EC = Reservoir EC ± 0.3 mS/cm:    → Normal; minor variation
  Media EC > Reservoir EC + 0.5 mS/cm:    → Salt accumulation beginning — monitor closely
  Media EC > Reservoir EC + 1.0 mS/cm:    → Flush media now (see Guide 02, Section 10)
  Media EC < Reservoir EC − 0.5 mS/cm:    → Media depleted — check for channelling/dry zones
```

[↑ Back to TOC](#table-of-contents)

---


## 9. pH Up and pH Down — Safe Handling

**pH Down (Acid)** — most commonly **phosphoric acid (H₃PO₄)**, sold as pH Down or pH Minus.

```
  Concentration: Typically 25–81% solution — corrosive; dilute before skin contact.

  Safe use:
  ─ Wear gloves and eye protection
  ─ Always add acid TO WATER, never water to acid
  ─ Start with small doses: 1ml per 4L, stir, wait 30 seconds, remeasure
  ─ Rinse skin immediately if contact occurs

  Citric acid: natural, safe, used by organic growers — gentler and less corrosive.
  Not recommended for E&F: citric acid can feed bacterial growth in warm reservoirs.
```

**pH Up (Base)** — most commonly **potassium hydroxide (KOH)**, sold as pH Up or pH Plus.

```
  Concentration: Typically 1–25% solution — caustic, corrosive to skin and eyes.

  Safe use:
  ─ Wear gloves and eye protection
  ─ Add drop by drop: 1ml per 4L, stir, remeasure
  ─ Store upright, cool, dark location
  ─ Rinse skin immediately if contact

  Alternative: Sodium bicarbonate (baking soda) — gentle, cheap, but adds Na which
  can accumulate in clay pebbles over time and stress roots. Emergency use only.
```

### pH Adjustment Protocol for E&F

```
  ADJUSTING RESERVOIR pH TO TARGET (5.8–6.2):

  1. Mix complete nutrient solution first (nutrients change pH significantly)
  2. Measure pH
  3. pH > 6.5: add pH Down 1ml at a time, stir, wait 30 seconds, remeasure
  4. pH < 5.5: add pH Up 1ml at a time, stir, wait 30 seconds, remeasure
  5. Repeat until within target range
  6. Final check after 5 minutes
  7. Run first flood cycle — then test media pH immediately after flood
  8. If media pH > 6.5: increase pH Down dose slightly on next reservoir fill

  E&F NOTE: After mixing and adjusting reservoir, check pH again after the FIRST flood.
  New clay pebbles may have released alkalinity into the solution during the flood,
  pushing pH back up. This is normal in weeks 1–4 with new media. Adjust and recheck.
```

[↑ Back to TOC](#table-of-contents)

---


## 10. Water Temperature Management Outdoors

### The Outdoor Heat Problem

An outdoor reservoir in summer can reach 28–35°C — temperatures where:
- Dissolved oxygen (DO) drops sharply (from 9mg/L at 20°C to <7mg/L at 30°C)
- Pythium and other water moulds thrive exponentially
- Nutrient uptake by roots becomes impaired
- Beneficial microbial balance is disrupted

### E&F Reservoir Positioning Advantage

Unlike NFT (where the reservoir typically sits beside the channels in open air), the E&F reservoir in this system sits **under the flood tables**. The tables act as a roof, shading the reservoir naturally. This is a significant thermal advantage — the reservoir in this system will typically run 3–6°C cooler than an equivalently sized exposed reservoir.

Maximise this advantage:
- Ensure the flood tables fully overhang the reservoir on all sides
- Use a lid on the reservoir (also prevents light entry and algae)
- Orient tables so the prevailing shade from nearby walls or fences protects the under-table space

### Management Strategies

```
  STRATEGY 1 — MAXIMISE NATURAL SHADE (free):
  As above — use table overhang. Add shade cloth to reservoir sides if gaps exist.

  STRATEGY 2 — INSULATION ($5–$20):
  Wrap reservoir exterior in:
  ─ Reflective bubble wrap insulation (best — reflects + insulates)
  ─ Foam camping mat glued to exterior
  ─ Partially bury reservoir in the ground (1/3 depth = effective thermal mass)

  STRATEGY 3 — WHITE/REFLECTIVE PAINT (free if you have paint):
  Paint exterior of reservoir white or silver.
  Reduces radiant heat absorption — can reduce water temp by 2–4°C vs black container.

  STRATEGY 4 — FROZEN BOTTLES (free, temporary):
  Fill 500ml–1L bottles with water and freeze.
  Drop into reservoir through lid port on hot days.
  Each 1L bottle absorbs ~80kcal of heat as it melts — effective for short spikes.
  Replace daily in peak summer.

  STRATEGY 5 — AQUARIUM CHILLER ($50–$200):
  Most effective, most expensive.
  Inline chiller maintains water at precise temperature.
  Worth considering if summer temperatures regularly exceed 30°C.
```

[↑ Back to TOC](#table-of-contents)

---


## 11. Algae Prevention in E&F Systems

### E&F Algae Risk Profile

Algae requires two things: **light** and **nutrients**. Your reservoir and flood tables have both. E&F presents specific algae challenges that differ from NFT:

**Higher risk areas in E&F:**
- **Clay pebble surface:** Pebbles at the surface of the flood table are intermittently wet and exposed to light — ideal algae habitat
- **Table edges and overflow fittings:** Wet surfaces in light breed algae quickly
- **Reservoir lid gaps:** Any light entering the reservoir enables algae growth

**Consequences in E&F:**
- Algae mat on clay pebble surface can block air exchange into the media
- Algae in overflow fittings partially blocks the drain — flood levels rise unexpectedly
- Algae in the reservoir depletes dissolved oxygen at night, stressing roots during the overnight period between flood cycles

### Prevention Checklist

```
  ALGAE PREVENTION FOR E&F:

  [ ] Cover clay pebble surface in flood tables with a black or silver plastic sheet
      (cut holes for net pots) — eliminates surface algae completely
  [ ] Keep reservoir lid light-tight — seal all gaps with black tape or foam
  [ ] Use opaque (black or white) flood tables — not clear or translucent
  [ ] Clean overflow fittings weekly — algae builds up inside the standpipe housing
  [ ] Ensure all return lines and hoses are opaque black — not clear vinyl
  [ ] Avoid overhead lighting that directly illuminates flood table media surface
```

### Treatment

If algae is already established:

```
  H₂O₂ (Hydrogen Peroxide) TREATMENT:

  Product: 3% food-grade H₂O₂ (available at pharmacies)
  Dose: 2–3ml per litre of reservoir volume

  Procedure:
  1. Remove all plants from affected tables
  2. Add H₂O₂ to reservoir at 2–3ml/L
  3. Run 2–3 flood cycles (circulates through tables and media)
  4. Let sit for 30 minutes between cycles
  5. Drain reservoir completely
  6. Flush media with plain water — 2–3 flood cycles with plain water
  7. Drain again — the H₂O₂ degrades to water and oxygen within hours
  8. Refill with fresh nutrient solution
  9. Replant

  CAUTION: H₂O₂ kills algae, beneficial microbes, AND can stress plant roots.
  Always remove plants before treatment. Rinse completely before replanting.
  For organic growers: H₂O₂ treatment destroys your beneficial microbe colony —
  you will need to re-inoculate after treatment (worm tea, Hydroguard).
```

[↑ Back to TOC](#table-of-contents)

---


## 12. Salt Accumulation and Flush Scheduling

The most important water management practice unique to E&F is **monitoring and managing salt accumulation in the growing media**. This does not occur in NFT (solution flows continuously, washing salts), but is a significant concern in any media-based system.

### EC Monitoring Protocol

```
  WEEKLY EC CHECK ROUTINE:

  Day and timing: Any day, immediately after a flood cycle ends

  Step 1: Test RESERVOIR EC → record value
  Step 2: Push EC probe 3–5cm into clay pebbles in multiple locations
          (Test at least 3 spots: near fill inlet, middle of table, near drain)
          Record each value
  Step 3: Calculate average media EC

  DECISION TABLE:
  ────────────────────────────────────────────────────────────────────
  Media EC vs Reservoir EC     Action
  ────────────────────────────────────────────────────────────────────
  Within ±0.3 mS/cm            Normal — no action needed
  +0.3 to +0.5 mS/cm           Mild accumulation — plan flush next week
  +0.5 to +1.0 mS/cm           Moderate — flush this week
  >+1.0 mS/cm                  Urgent — flush today; inspect roots for tip burn
  ────────────────────────────────────────────────────────────────────

  Record in a log: date, reservoir EC, media EC, any symptoms observed.
  Trends over weeks tell you whether your flush frequency is adequate.
```

[↑ Back to TOC](#table-of-contents)

---


## 13. Full Water Change Protocol

### Step-by-Step Reservoir Change

```
  FREQUENCY: Every 7 days recommended; maximum 14 days.
  Also perform on any trigger condition from Section 10.

  WHAT YOU NEED:
  ─ Siphon hose or small submersible utility pump
  ─ Bucket for old solution disposal
  ─ Scrub brush / sponge / microfibre cloth
  ─ 10% bleach solution (1 part bleach : 9 parts water)
  ─ Fresh water supply (tap, RO, or rainwater)
  ─ Nutrient concentrates and pH adjustment chemicals
  ─ Calibrated EC and pH meters
  ─ Gloves and eye protection

  STEPS:
  1.  Turn off the pump (prevent dry-running during drain)
  2.  Remove the pump from the reservoir
  3.  Siphon or pump out all old nutrient solution
  4.  Wipe interior walls and floor of reservoir with a cloth
      ─ Remove biofilm, algae patches, and mineral deposits
  5.  Add 2–3L of 10% bleach solution, swirl to coat all surfaces
  6.  Leave 10–15 minutes (sterilisation contact time)
  7.  Drain bleach solution completely
  8.  Triple rinse: fill with fresh water, slosh, drain — repeat 3 times
      (No bleach residue must remain — it kills plant roots and beneficial microbes)
  9.  Clean pump filter/strainer — remove accumulated debris
  10. Inspect all fittings and drain lines — clear any partial blockages
  11. If this is also a media flush day (see Guide 02, Section 10):
      ─ Fill reservoir with plain pH-adjusted water
      ─ Run 3–4 flood cycles before adding nutrients
      ─ Drain reservoir after flush cycles
  12. Refill reservoir with fresh source water
  13. Add nutrients (Masterblend or Flora Series) to target EC
  14. Adjust pH to 5.8–6.2
  15. Verify final EC and pH before restarting pump
  16. Restart pump — confirm flow reaching all tables
  17. Log the date of reservoir change and any observations
```

---


*Next: [`guide/ebb-and-flow/04-lighting.md`](04-lighting.md) — Outdoor light, PAR, DLI, shade management, and seasons*

[↑ Back to TOC](#table-of-contents)

---

<!-- copyright -->
*Copyright (c) 2026 UncleJS. Licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) — free to share and adapt for non-commercial purposes with attribution and ShareAlike.*
