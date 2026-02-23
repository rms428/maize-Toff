---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  :root {
    --color-primary: #1a3a5c;
    --color-accent:  #2980b9;
    --color-green:   #27ae60;
    --color-red:     #c0392b;
    --color-light:   #f4f6f9;
  }
  section {
    font-family: "Helvetica Neue", Arial, sans-serif;
    background: #ffffff;
    color: #1a1a1a;
    padding: 40px 52px;
  }
  section.lead {
    background: var(--color-primary);
    color: #ffffff;
    justify-content: center;
    align-items: flex-start;
  }
  section.lead h1 {
    color: #ffffff;
    font-size: 2.1em;
    line-height: 1.25;
    border: none;
    margin-bottom: 0.3em;
  }
  section.lead h2 {
    color: #a8d4f5;
    font-size: 1.1em;
    font-weight: 400;
    border: none;
    margin-top: 0;
  }
  section.lead p {
    color: #cde3f5;
    font-size: 0.85em;
    margin-top: 2em;
  }
  section.section-break {
    background: var(--color-accent);
    color: #ffffff;
    justify-content: center;
  }
  section.section-break h1 {
    color: #ffffff;
    font-size: 2em;
    border: none;
    text-align: center;
    width: 100%;
  }
  h1 {
    color: var(--color-primary);
    font-size: 1.45em;
    border-bottom: 3px solid var(--color-accent);
    padding-bottom: 6px;
    margin-bottom: 0.6em;
  }
  h2 {
    color: var(--color-accent);
    font-size: 1.05em;
    margin-top: 0.3em;
    margin-bottom: 0.3em;
  }
  ul { margin-top: 0.3em; padding-left: 1.3em; }
  li { margin-bottom: 0.35em; font-size: 0.92em; }
  li li { font-size: 0.88em; color: #444; margin-bottom: 0.15em; }
  strong { color: var(--color-primary); }
  em { color: #555; }
  .tag {
    display: inline-block;
    background: var(--color-accent);
    color: white;
    border-radius: 4px;
    padding: 2px 10px;
    font-size: 0.8em;
    margin-right: 6px;
    vertical-align: middle;
  }
  .green { color: var(--color-green); font-weight: bold; }
  .red   { color: var(--color-red);   font-weight: bold; }
  footer {
    color: #aaa;
    font-size: 0.7em;
  }
---

<!-- Slide 1: Title -->
<!-- _class: lead -->

# To tree or not to tree?
## A trait-based ecohydrological model for semi-arid agroforestry

Cella Schnabel · Larsen Lab · February 24, 2026


---

<!-- Slide 2: The puzzle -->

# Question

**Field evidence is contradictory:**

- *Faidherbia albida* (white acacia): consistently facilitates maize in the Sahel
- Most evergreen parkland trees: mixed results; competition documented under drought
- Reviews report +5–30% yield gains — but also yield *losses*

**Why?**

> Trees interact with crops through multiple simultaneous mechanisms.
> Whether the net effect on crop yield is positive or negative depends on
> **the tree** and **the climate.**

---

<!-- Slide 3: Literature framing -->

# What the field evidence shows — and doesn't explain

<!-- _footer: "Sileshi et al. (2008); Bayala & Prieto (2020); Bargués-Tobella et al. (2014, WRR); Kuyah et al. (2023); Garrity et al. (2010)" -->

## The average picture is strongly positive
- Sub-Saharan meta-analysis (126 studies, 1,106 obs.): **crop yield ~2× higher** in agroforestry vs. monoculture *(Agronomy Sustain. Dev. 2019)*
- *Faidherbia albida* specifically: **2–4× yield** of unfertilised plots across the Sahel *(Garrity et al. 2010)*
- Agroforestry facilitative in **68–77% of study cases** in East Africa *(Kuyah et al. 2023)*

## Hydraulic redistribution is documented
- Deep-rooted parkland trees lift **35–47 mm yr⁻¹** (8–10% of MAP) in Sahelian parklands *(Bargués-Tobella et al. 2014, WRR)*
- Tracer water applied to shrub roots reaches intercropped millet within **12–96 hours** *(Frontiers Env. Sci. 2018)*

## But the field literature cannot explain *why* outcomes vary
- Competition documented under drought, especially for shallow-rooted evergreen species *(Coulibaly et al. 2014)*
- Yield effect sign switches between species, sites, and seasons — with no unifying mechanistic framework
- Facilitation vs. competition attributed post-hoc to "deep roots," "phenology," or "N-fixation" separately — never decomposed together

> **Gap this work fills:** a process-based decomposition of which traits drive the competition→facilitation transition, and when.

---

<!-- Slide 4: Study system -->

# Study system

**Location:** smallholder maize farms, Laikipia Plateau, Kenya (semi-arid, ~500–700 mm/yr)

**Published model baseline:** Krell & Caylor (UCSB) — stochastic ecohydrology model, validated against Kenya Seed Co. yield data

**Extension:** add a tree component and ask — for three contrasting tree archetypes across three rainfall regimes, when does the tree help vs. hurt?

| Archetype | Phenology | Root depth | Canopy cover |
|---|---|---|---|
| *Faidherbia albida* | **Reverse** — leafless during crop season | 1500 mm | 20% |
| Evergreen deep | Evergreen | 1500 mm | 20% |
| Evergreen shallow | Evergreen | 600 mm | 30% |

---

<!-- Slide 5: Model schematic -->

# The two-layer model

![center height:480px](output/pres_fig1_schematic.png)

---

<!-- Slide 6: Four mechanisms -->

# Four tree–crop interaction mechanisms

<br>

## Competition
- **Shallow water competition** — tree roots draw from the same crop-zone bucket

## Facilitation
- **Shade** — tree canopy reduces soil evaporation (*E*) and transpiration via lower VPD
- **Deep roots** — tree preferentially fills demand from below the crop zone (deep-first allocation), leaving crop-zone water for the crop
- **Hydraulic redistribution (HR)** — at night, roots passively lift water from the deep layer into the crop zone along a water-potential gradient

> *Faidherbia adds a fifth lever: **reverse phenology** — no leaves during the crop season means zero competition and zero shade during the period that matters most.*

---

<!-- Slide 7: Single season -->

# A single season: Faidherbia in action

![center height:490px](output/pres_fig2_mechanism.png)

---

<!-- Slide 8: Factorial -->
<!-- _footer: "Factorial run: single season, evergreen tree (kc=1.0, cc=0.2, Zr=1500 mm, T_MAX=5.0 mm/day)" -->

# Which mechanisms drive facilitation?

![center height:490px](output/pres_fig4_factorial.png)

---

<!-- Slide 9: Faidherbia 300 seasons -->
<!-- _footer: "Faidherbia albida archetype · 300 simulated seasons · baseline rainfall regime" -->

# Faidherbia facilitates in 87% of seasons

![center height:490px](output/pres_fig3_transition.png)

---

<!-- Slide 10: Yield by regime -->
<!-- _footer: "200 simulated seasons × 3 rainfall regimes · Faidherbia albida" -->

# Yield gains hold across all rainfall regimes

![center height:490px](output/pres_fig5_yield_regime.png)

---

<!-- Slide 11: Cross-species scatter -->
<!-- _footer: "300 seasons × 3 rainfall regimes per archetype (n=900 season-pairs per archetype)" -->

# Trait space determines the outcome

![center height:490px](output/cross_species_scatter.png)

---

<!-- Slide 12: Cross-species heatmap -->
<!-- _footer: "300 seasons × 3 rainfall regimes per archetype" -->

# Summary: archetype × regime matrix

![center height:490px](output/cross_species_heatmap.png)

---

<!-- Slide 13: Key findings -->

# Key findings

<br>

1. **Phenology is the master switch.** *Faidherbia*'s reverse phenology eliminates competition and shade during the crop season — facilitative in **85–91%** of seasons across all rainfall regimes (+180 to +224 kg ha⁻¹).

2. **Deep roots help — but only with HR.** Deep roots alone intensify competition (tree has more water, draws more). HR is what converts deep-root access into a crop benefit.

3. **Shade is net facilitative via E reduction**, but only when water is the primary limiting factor (semi-arid conditions). Shade and deep roots reinforce each other.

4. **Shallow-rooted evergreen trees are reliably competitive** (−365 to −763 kg ha⁻¹; only 3–11% of seasons facilitative). Shallow roots + year-round demand = direct competition.

5. **Rainfall regime modulates magnitude, not direction** — for Faidherbia and evergreen-deep, facilitation holds regardless of regime. For evergreen-shallow, competition holds regardless.

---

<!-- Slide 14: Next steps -->

# Next steps

<br>

## Immediate
- **Sensitivity sweep:** vary `hr_max` (0.1–2.0 mm/day) and `canopy_cover` (0.1–0.4) — where does the competition→facilitation boundary sit in parameter space?

## Short-term
- **Nitrogen fixation:** add `Y_MAX × (1 + N_bonus)` term — *Faidherbia* fixed-N is estimated at +5–15% yield gain in the field; model predicts ~10% from HR alone, so N-fixation could double the benefit
- **Validation:** compare Δ yield predictions to Bayala et al. and Garrity et al. field data

## Longer-term
- **Deciduous vs. evergreen phenology sweep** — continuous trait rather than discrete archetypes
- **Climate change scenarios** — shift rainfall toward fewer/more-intense events and re-run regime analysis

---

<!-- Slide 15: Thank you -->
<!-- _class: lead -->

# Thank you

Questions?

*Figures and model code: `tree.ipynb`*
*Framework: Rodriguez-Iturbe & Porporato (2004), Laio et al. (2001), Porporato et al. (2001)*
*Agroforestry references: Bayala & Prieto (2020), Bargués-Tobella et al. (2014), Garrity et al. (2010)*
