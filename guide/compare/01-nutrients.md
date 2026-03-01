# Comparison Guide 01 — Nutrient Management: NFT vs Ebb & Flow
## How the two systems handle feeding, EC, pH, salt, and solution changes differently

---

## Table of Contents

- [Introduction](#introduction)
- [1. How Each System Delivers Nutrients](#1-how-each-system-delivers-nutrients)
  - [NFT: Thin Continuous Film](#nft-thin-continuous-film)
  - [Ebb & Flow: Flood-Drain Cycles](#ebb--flow-flood-drain-cycles)
- [2. EC Management](#2-ec-management)
  - [Target Ranges Side-by-Side](#target-ranges-side-by-side)
  - [The Media EC Problem (E&F Only)](#the-media-ec-problem-ef-only)
  - [How to Test Correctly in Each System](#how-to-test-correctly-in-each-system)
- [3. pH Management](#3-ph-management)
  - [Drift Patterns and Causes](#drift-patterns-and-causes)
  - [Buffering Behaviour](#buffering-behaviour)
  - [Correction Frequency](#correction-frequency)
- [4. Salt Accumulation](#4-salt-accumulation)
  - [Why E&F Accumulates Salts Faster](#why-ef-accumulates-salts-faster)
  - [The Monthly Media Flush Protocol (E&F)](#the-monthly-media-flush-protocol-ef)
  - [NFT: No Media, No Flush](#nft-no-media-no-flush)
- [5. Nutrient Solution Changes](#5-nutrient-solution-changes)
  - [Reservoir Volume and Change Frequency](#reservoir-volume-and-change-frequency)
  - [Top-Up vs Full Change](#top-up-vs-full-change)
  - [Disposing of Old Solution](#disposing-of-old-solution)
- [6. Nutrient Recipes: Are They Interchangeable?](#6-nutrient-recipes-are-they-interchangeable)
  - [Masterblend in Both Systems](#masterblend-in-both-systems)
  - [Calcium and Magnesium Needs](#calcium-and-magnesium-needs)
  - [Adjusting for Fruiting Crops (E&F)](#adjusting-for-fruiting-crops-ef)
- [7. Deficiency and Toxicity Patterns](#7-deficiency-and-toxicity-patterns)
  - [Common NFT Deficiency Patterns](#common-nft-deficiency-patterns)
  - [Common E&F Deficiency Patterns](#common-ef-deficiency-patterns)
  - [Why the Same Symptom Can Mean Different Things](#why-the-same-symptom-can-mean-different-things)
- [8. Monitoring Regimen Comparison](#8-monitoring-regimen-comparison)
- [9. Quick-Reference Decision Table](#9-quick-reference-decision-table)

---


[↑ Back to TOC](#table-of-contents)

## Introduction

Both NFT and Ebb & Flow use the same nutrient chemistry — the 17 essential elements dissolved in water — but they interact with those nutrients in fundamentally different ways. In NFT, roots sit directly in flowing solution; there is no media to absorb, buffer, or accumulate minerals. In Ebb & Flow, every litre of nutrient solution that floods the table and drains back leaves a residue in the LECA. That residue is cumulative.

This guide compares how you manage nutrients in practice across both systems: what you measure, how often, what drifts, what accumulates, and where the failure modes differ.

---


[↑ Back to TOC](#table-of-contents)

## 1. How Each System Delivers Nutrients

### NFT: Thin Continuous Film

In NFT, a pump runs continuously (or on a very short off-cycle at night). A 2–3 mm film of solution flows along the bottom of each PVC channel, roots hang through the film, and the rest of the root mass hangs in moist air above the film — which is where oxygen uptake primarily happens.

Key delivery characteristics:
- **Contact is constant** — roots touch solution at all times
- **Solution moves fast** — typical flow rate 1–2 L/min per channel; root zone is fully refreshed continuously
- **No media reservoir** — there is no LECA, coco, or rockwool holding solution between flows; what the plant gets is exactly what is in the reservoir
- **Root zone EC = reservoir EC** — with no media buffer, the concentration seen by the roots is essentially identical to what you measure in the reservoir tank

Because there is no lag between reservoir and root zone, NFT responds quickly to nutrient changes — both beneficial corrections and mistakes.

```mermaid
graph LR
  A[Reservoir<br/>EC / pH set here] -->|pump| B[Channel inlet<br/>thin film]
  B -->|gravity flow| C[Root zone<br/>EC ≈ reservoir]
  C -->|drain| D[Return pipe<br/>back to reservoir]
```

### Ebb & Flow: Flood-Drain Cycles

In E&F, the pump floods the entire grow table to a depth of 3–5 cm (or until the overflow fitting triggers), holds for typically 20–30 minutes, then the pump stops and solution drains by gravity back to the reservoir. This cycle repeats 2–6 times per day depending on temperature and crop stage.

Key delivery characteristics:
- **Contact is intermittent** — roots access solution only during flood periods
- **Solution volume is large** — 20–25 L of LECA per table holds 4–6 L of solution after drain-back; this retained moisture sustains the plant between floods
- **Media acts as a sponge** — LECA absorbs and holds solution; as water evaporates and plants transpire between floods, the nutrient concentration left in the media rises
- **Media EC ≠ reservoir EC** — this is the central challenge of E&F nutrient management (covered in depth in Section 2)

```mermaid
graph TD
  A[Reservoir<br/>EC / pH set here] -->|pump ON| B[Flood table<br/>solution rises to 3-5 cm]
  B -->|roots in flood| C[Root zone<br/>absorbs nutrients]
  B -->|pump OFF| D[Drain back<br/>gravity to reservoir]
  D --> A
  C -->|between floods| E[LECA retains<br/>moisture + salts]
  E -->|next flood dilutes<br/>or compounds salts| C
```

---


[↑ Back to TOC](#table-of-contents)

## 2. EC Management

### Target Ranges Side-by-Side

| Stage | NFT target EC (mS/cm) | E&F reservoir EC (mS/cm) | E&F media EC (mS/cm) |
|---|---|---|---|
| Seedling / transplant | 0.8 – 1.2 | 0.8 – 1.0 | 0.8 – 1.2 |
| Early vegetative | 1.2 – 1.6 | 1.2 – 1.4 | 1.4 – 1.8 |
| Full vegetative (leafy crops) | 1.4 – 2.0 | 1.4 – 1.8 | 1.6 – 2.2 |
| Flowering / fruiting | 1.8 – 2.4 | 1.8 – 2.2 | 2.0 – 2.8 |
| Late fruiting / final flush | 0.5 – 1.0 | 0.5 – 1.0 | 0.8 – 1.4 |

**E&F media EC is always higher than reservoir EC** — typically 0.5–1.0 mS/cm above the reservoir reading. This is normal and expected. What matters is that media EC does not climb above ~3.0 mS/cm in vegetative growth or ~3.5 mS/cm in fruiting stages, as above these thresholds nutrient lockout begins.

In NFT, you only need one measurement: the reservoir. In E&F, you need two.

### The Media EC Problem (E&F Only)

Between floods, the LECA surface area is large relative to the volume of solution retained. As the plant transpires and water evaporates from the media surface, the remaining moisture becomes increasingly concentrated with the mineral salts that didn't evaporate.

This effect compounds with every cycle:

1. Flood at reservoir EC 1.6 — media wets to ~1.6
2. Plant transpires, water evaporates — media EC rises to ~2.0
3. Next flood at 1.6 — media partially dilutes, settles at ~1.9
4. Further transpiration — media EC rises to ~2.4
5. Over days without correction — continues to rise

Hot weather, high VPD, and large fruiting plants with high transpiration rates all accelerate this drift. A media EC of 3.5+ can cause wilting even when the reservoir EC looks perfectly correct.

**Prevention**:
- Run reservoir EC at the lower end of target ranges, especially in summer
- Monitor media EC weekly with a probe pushed 5–8 cm deep into the LECA
- If media EC is >0.8 mS/cm above reservoir EC, flush (see Section 4)

### How to Test Correctly in Each System

**NFT:**
1. Take reservoir sample (50–100 mL from mid-depth, away from inlet/outlet)
2. Rinse meter probe with RO or distilled water before use
3. Read EC and pH
4. Done — one test, one value

**E&F:**
1. Take reservoir sample as above
2. Take media sample: push probe 5–8 cm into LECA in the centre of the table, in the root zone (not at the edge)
3. Alternatively, collect runoff from the table's drain port at the end of a flood cycle
4. Compare reservoir EC vs media EC
5. If media EC > reservoir EC by more than 1.0 mS/cm, flush is overdue

---


[↑ Back to TOC](#table-of-contents)

## 3. pH Management

### Drift Patterns and Causes

pH drift is a feature of all recirculating hydroponic systems, but the direction and speed differ between NFT and E&F.

**NFT pH drift:**
- Typically drifts **upward** (alkaline) as plants uptake more cations (NH₄⁺, K⁺, Ca²⁺, Mg²⁺) than anions, leaving excess OH⁻ in solution
- Can also drift upward if CO₂ is being degassed from the reservoir (especially in warm, sunny weather with exposed reservoir surface)
- Rate: typically 0.1–0.3 pH units per day in a healthy, actively growing system
- With leafy crops at peak growth, upward drift of 0.4–0.5/day is possible

**E&F pH drift:**
- Also typically upward, but the media buffer slows the apparent rate
- LECA is pH-neutral after pre-soaking and has minimal buffering; rockwool and coco coir can introduce initial pH shifts in the first week
- Drift in the reservoir may appear slower than NFT because not all solution is in the reservoir — some is retained in the media
- After a flush (when media solution returns to reservoir), you may see a pH spike or drop depending on what had accumulated in the media

### Buffering Behaviour

In NFT, the full reservoir volume acts as the buffer. A 100 L reservoir with 15 L plant-accessible root zone means that a plant-induced pH shift is diluted across the full 100 L. Corrections apply immediately to the full system.

In E&F, roughly 15–20% of total solution volume is retained in the media at any time. When you correct the reservoir pH, the media retains its old pH. The full correction only propagates through the entire system after 2–3 flood cycles. This means:

- Do not over-correct expecting immediate results — wait for the next 2–3 flood cycles
- If pH is 6.2 in the reservoir and you want 5.8, adding pH down for 5.8 may create a dip to 5.5 in the reservoir once the media slowly homogenises
- Make gradual corrections of 0.2–0.3 units; test again after 3–4 flood cycles

### Correction Frequency

| System | Check frequency | Correction method |
|---|---|---|
| NFT | Twice daily (morning and late afternoon) | Add pH up/down to reservoir, circulates immediately |
| E&F | Once daily (after morning flood cycle) | Add pH up/down to reservoir; full equilibration takes 2–3 flood cycles |

For both systems, the target pH range is **5.5–6.5**, with the sweet spot at **5.8–6.2** for most crops.

---


[↑ Back to TOC](#table-of-contents)

## 4. Salt Accumulation

### Why E&F Accumulates Salts Faster

Every evaporation cycle in E&F leaves behind dissolved minerals. The LECA particle surfaces are porous, giving a very high total surface area — roughly 200 m²/kg of media. This large surface area adsorbs minerals efficiently, which is excellent for short-term plant uptake but becomes a problem over time as adsorbed salts accumulate faster than flood cycles can wash them.

Contributing factors:
- **High temperatures** increase evaporation rate → more concentration per cycle
- **Long dry periods between floods** allow more concentration (this is why over-spacing flood cycles in summer is risky)
- **High-EC nutrient solution** — running at 2.4 when 1.8 would suffice accelerates accumulation
- **Mature media** — LECA that has been used for multiple seasons has higher starting mineral content

Visible signs of salt accumulation:
- White or pale orange crystalline crust on the surface of LECA (especially at the table edges)
- LECA turning progressively paler/more mineral-coated compared to freshly rinsed media
- Media EC consistently running 1.5+ mS/cm above reservoir EC

### The Monthly Media Flush Protocol (E&F)

This protocol should be run once per month during the growing season, and at the start and end of every season.

**Equipment needed:**
- RO or low-EC tap water (EC < 0.5)
- pH down (to bring flush water to pH 5.8–6.0)
- Measuring jugs
- EC/pH meter

**Procedure:**
1. Mix flush water to EC 0.3–0.5 and pH 5.8. Do not use plain RO water — the extreme low EC causes osmotic stress.
2. Disconnect or bypass the reservoir inlet so the flood pump pulls from a separate flush bucket.
3. Flood the table fully (to the overflow fitting level) with flush water.
4. Allow to sit for 10–15 minutes — this dissolves accumulated salt crystals back into solution.
5. Drain fully back to a waste bucket (do not return to the reservoir — this water is heavily contaminated with accumulated salts).
6. Flood again with fresh flush water.
7. Drain again to waste.
8. Flood a third time with standard nutrient solution at target EC.
9. Drain back to reservoir (this is your first normal feed cycle post-flush).
10. Check reservoir EC after the cycle — it will likely have risen 0.1–0.3 mS/cm from media bleed-off. Adjust if needed.

**Post-flush expectations:**
- Media EC should be within 0.3 mS/cm of reservoir EC the day after flushing
- Plants may show a brief uptake surge in the following 24–48 hours as they recover from the flush
- Some temporary wilting is normal during the flush itself (osmotic shock from low-EC water) — this resolves within hours

### NFT: No Media, No Flush

NFT has no growing media in the channels (only small net pot inserts at each planting site). There is no adsorptive surface area to accumulate salts between plants, no media flush protocol, and no media EC to monitor.

The only accumulation risk in NFT is:
- **Residue on channel walls** — this is cleaned between crop cycles with a 10% bleach solution or hydrogen peroxide soak, not a mineral flush
- **Reservoir mineral build-up** — after 3–4 weeks, the reservoir itself should be fully changed to reset the dissolved mineral profile (see Section 5)

This is one of the genuine operational simplicity advantages of NFT over E&F.

---


[↑ Back to TOC](#table-of-contents)

## 5. Nutrient Solution Changes

### Reservoir Volume and Change Frequency

| System | Typical reservoir volume | Recommended full change frequency |
|---|---|---|
| NFT (3-zone system) | 100–150 L | Every 3–4 weeks, or when EC/pH become unmanageable |
| E&F (3-zone system) | 150–200 L | Every 2–3 weeks, or after any media flush |

E&F requires a larger reservoir because solution is stored both in the reservoir and in the media (up to 15–20% of total volume is always in the LECA). The larger reservoir volume also helps buffer the media EC fluctuations described above.

The shorter change interval for E&F exists because:
1. Salt accumulation in media accelerates solution degradation faster
2. Flush events return contaminated (high-salt) water to the reservoir
3. Fruiting crops (tomatoes, cucumbers, courgettes) common in E&F consume nutrients unevenly, causing element imbalance faster than leafy crops

### Top-Up vs Full Change

For both systems, you should distinguish between:
- **Top-up**: adding fresh nutrient solution (at target EC) to replace volume lost to plant uptake and evaporation — done daily or as needed
- **Full change**: emptying the entire reservoir, cleaning it, and refilling with fresh solution — done on schedule or when the solution becomes unmanageable

**Top-up rule (both systems):**
Prepare top-up solution at the target EC. Do not top up with plain water (which dilutes the solution and upsets the mineral ratio) unless you are specifically trying to lower EC.

**When a full change is due (either system):**
- EC has risen despite not adding nutrients (indicates element imbalance — certain minerals accumulating as plants preferentially take up others)
- pH correction is consuming more acid/alkali than usual (indicates buffering capacity is exhausted)
- Solution has been running for more than the scheduled interval
- Algae or biological contamination is visible
- After a pest or disease event (sterilise reservoir, tubing, and pump before refilling)

### Disposing of Old Solution

Old nutrient solution is a mild fertiliser. Options:
- **Garden irrigation**: dilute 1:3 with plain water and use on non-edible garden beds or lawns. Do not use on edible root vegetables.
- **Compost accelerant**: nutrient-rich liquid speeds decomposition in compost heaps
- **Drain to sewer**: legal in most jurisdictions for domestic-scale systems (check local rules). Flush the drain with water after.
- **Do not** pour undiluted old solution repeatedly onto the same garden patch — salt build-up will damage soil over time.

---


[↑ Back to TOC](#table-of-contents)

## 6. Nutrient Recipes: Are They Interchangeable?

### Masterblend in Both Systems

The Masterblend 4-18-38 three-part formula (Masterblend + calcium nitrate + Epsom salt) works in both systems at the same base ratios:
- 2.4 g/L Masterblend 4-18-38
- 2.4 g/L calcium nitrate
- 1.2 g/L Epsom salt (magnesium sulphate)

This produces a reservoir EC of approximately 1.6–1.8 mS/cm in typical tap water, which suits most vegetative stages in both systems.

**Adjustments for E&F:**
- Run the reservoir EC 0.2–0.3 mS/cm lower than the NFT target for the same crop/stage. The media will add 0.5–0.8 mS/cm on top; starting lower prevents the media EC from climbing dangerously high.
- Example: If NFT target for early fruiting is EC 2.0, set E&F reservoir EC to 1.7–1.8

### Calcium and Magnesium Needs

Calcium and magnesium requirements differ slightly:

**NFT:**
- Calcium needs are moderate; blossom end rot (calcium deficiency) is uncommon in NFT because continuous flow means a constant calcium supply even at high crop densities
- Magnesium deficiency (interveinal chlorosis on older leaves) is the more common deficiency

**E&F:**
- Calcium demands are higher in fruiting crops (tomatoes, cucumbers, peppers)
- The intermittent nature of flood-drain means that during dry periods between floods, calcium mobility through the plant slows — making blossom end rot more common, especially in summer when flood intervals may be longer than intended
- Consider increasing calcium nitrate by 0.3–0.4 g/L above the base recipe during fruit swelling stages

### Adjusting for Fruiting Crops (E&F)

E&F supports fruiting crops that NFT cannot sustain (cucumbers, courgettes, aubergine, large tomato varieties). These crops have specific nutrient requirements at different growth stages:

**Tomatoes — fruiting stage (E&F):**
- Reduce nitrogen: Masterblend can be dropped from 2.4 to 2.0 g/L
- Increase potassium: add 0.4 g/L potassium sulphate
- Increase calcium nitrate to 2.8 g/L
- Target reservoir EC: 1.8–2.2 mS/cm

**Cucumbers — fruiting stage (E&F):**
- Higher magnesium requirement: increase Epsom salt to 1.6 g/L
- Higher overall EC tolerance: can push to 2.2–2.4 mS/cm in peak fruiting
- Sensitive to sodium — use reverse osmosis or low-sodium water sources if available

**Courgettes (E&F):**
- Lower EC requirements than cucumbers and tomatoes: keep at 1.6–2.0 mS/cm
- Very high potassium during fruiting: add 0.3 g/L potassium sulphate from first fruit set

---


[↑ Back to TOC](#table-of-contents)

## 7. Deficiency and Toxicity Patterns

### Common NFT Deficiency Patterns

| Deficiency | Visual symptom | Primary cause in NFT |
|---|---|---|
| Nitrogen | Uniform yellowing, oldest leaves first | EC too low; solution too old; high temperatures increasing uptake |
| Iron | Interveinal chlorosis on young leaves (yellow between green veins) | pH above 6.5 locks out iron; iron precipitates at high pH |
| Magnesium | Interveinal chlorosis on older leaves | Low magnesium in recipe; pH outside range; calcium antagonism |
| Calcium | Tip burn on lettuce; blossom end rot on tomato (rare in NFT) | pH below 5.5; low transpiration; high ammonium competing with calcium |
| Phosphorus | Purple/red colouring on undersides of leaves and stems | pH below 5.5; cold root zone; solution too old |

**NFT-specific note:** Iron deficiency is the most common micronutrient problem in NFT because the solution pH can creep up quickly (as described in Section 3). Iron becomes nearly insoluble above pH 6.8. A pH spike to 7.0+ even for a few days can trigger iron chlorosis.

### Common E&F Deficiency Patterns

| Deficiency | Visual symptom | Primary cause in E&F |
|---|---|---|
| Calcium | Blossom end rot (dark, sunken patch on fruit base); tip burn | Long dry periods between floods; high media EC reducing calcium uptake |
| Magnesium | Interveinal chlorosis on older leaves | Salt accumulation in media competing with magnesium uptake |
| Potassium | Brown leaf edges (scorch); poor fruit set | High-sodium water source; old solution with depleted potassium |
| Nitrogen | Uniform pale/yellowing | Solution too old; media EC high but nutrient profile depleted |
| Iron | Young leaf chlorosis | pH drift in media (may not match reservoir pH) |

**E&F-specific note:** Calcium is the most common deficiency in E&F. This is because calcium moves with the transpiration stream — during the period between floods when no water is moving, calcium transport slows. In summer heat with high VPD, the plant may transpire faster than calcium can be delivered even when the reservoir EC and calcium level are correct. Increasing flood frequency (from 3× to 5× daily) during peak summer heat resolves most calcium deficiency issues in E&F.

### Why the Same Symptom Can Mean Different Things

**Brown leaf tips / tip burn:**
- **In NFT (lettuce):** Usually calcium deficiency from pH creep; check pH first
- **In E&F (lettuce):** Usually calcium deficiency from under-flooding or high media EC; check flood frequency and media EC first

**Interveinal chlorosis on young leaves:**
- **In NFT:** Almost always iron; check pH (is it above 6.5?)
- **In E&F:** Could be iron (pH), but also check if media EC is very high (multi-element lockout)

**Overall stunting and dark green, thick leaves:**
- **In both systems:** Phosphorus excess or pH below 5.2; check pH immediately

---


[↑ Back to TOC](#table-of-contents)

## 8. Monitoring Regimen Comparison

| Task | NFT frequency | E&F frequency | Notes |
|---|---|---|---|
| Reservoir EC check | Twice daily | Once daily | E&F reservoir changes more slowly |
| Reservoir pH check | Twice daily | Once daily | E&F reservoir changes more slowly |
| Media EC check (E&F only) | — | Weekly | Push probe into LECA root zone |
| Nutrient top-up | As needed (daily in summer) | As needed (daily in summer) | Top up at target EC |
| pH correction | As needed | As needed, gradual | E&F: wait 2–3 flood cycles for equilibration |
| Full solution change | Every 3–4 weeks | Every 2–3 weeks | E&F: also after any media flush event |
| Media flush (E&F only) | — | Monthly | See Section 4 for protocol |
| Reservoir clean | With each full change | With each full change | Scrub with dilute hydrogen peroxide |
| Channel/table clean | Between crop cycles | Between crop cycles | NFT: bleach soak; E&F: bleach + LECA rinse |

---


[↑ Back to TOC](#table-of-contents)

## 9. Quick-Reference Decision Table

| Scenario | NFT action | E&F action |
|---|---|---|
| EC too high in reservoir | Remove some solution, top up with RO/plain water | Same; also check media EC — may need flush |
| EC too low in reservoir | Add concentrated nutrient mix | Same; media will also be low — do not over-correct |
| pH too high (>6.5) | Add pH down directly to reservoir | Add pH down to reservoir; wait 3 flood cycles to equilibrate |
| pH too low (<5.5) | Add pH up directly to reservoir | Add pH up to reservoir; wait 3 flood cycles |
| Media EC >1.0 mS/cm above reservoir (E&F only) | N/A | Run monthly flush protocol immediately |
| Blossom end rot on fruit | Rare — check pH and calcium | Increase flood frequency; check media EC; increase calcium nitrate |
| Iron chlorosis on young leaves | Check pH (is it above 6.5?) | Check reservoir pH and media pH (media pH may differ from reservoir) |
| Salt crust on media surface (E&F only) | N/A | Flush is overdue; run monthly flush protocol |
| Solution change overdue | Full reservoir drain and refill | Full reservoir drain and refill; follow with media flush |

---


[↑ Back to TOC](#table-of-contents)

*Next: [Comparison Guide 02 — Crops: NFT vs Ebb & Flow](02-crops.md) — which system suits which plants, yield comparisons, and crop scheduling differences*
