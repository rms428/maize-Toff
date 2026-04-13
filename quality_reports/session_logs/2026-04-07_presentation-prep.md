---
date: 2026-04-07
description: Presentation prep — diagnostic figure edits, model review
---

## Session goal
Prepare threecrop_diagnostic.png for presentation; review model mechanics.

## Decisions / findings

- **threecrop_diagnostic.png** regenerated from latest model state. Removed HR dashed line (panel c) and Deep (shared) line (panel a). Added s_w / s* to legend instead of direct text labels.

- **Baseline rainfall** = CETRAD OL JOGI FARM calibrated parameters (~555 mm/yr, 376 mm/season).

- **T_tree_lateral >> T_tree_under**: confirmed not a bug. Geometric consequence of area-weighting: outside zone covers 4× the area of under-canopy zone, so at alpha_lateral=0.5 the plot-level lateral supply capacity is 2× the under-canopy supply. Code is internally consistent (all quantities at plot-level).

## Open questions / flags

**T_MAX × cc scaling may be incorrect (medium priority)**
In Krell (2021), T_max is a plot-level quantity — the crop implicitly has cc=1 so no area scaling appears. Our ThreeCropModel applies `T_canopy_pot = T_MAX × cc`, which treats T_MAX as per-unit-canopy-area and scales down to plot level. This may double-count the area effect if T_MAX=2.0 is calibrated as a plot-level rate (like crop T_MAX=4.0). At cc=0.2, the tree's demand is only 0.4 mm/day — possibly too low.
- Fix is non-trivial: removing cc from the demand term also requires reformulating the supply terms (under: `calc_T(s_u) × cc`; lateral: `calc_T(s_o) × alpha_lat × oc`) so the tree is not perpetually supply-limited.
- Do not fix before understanding the supply-demand balance implications.

**alpha_lateral = 0.5 — is this the right value?**
At alpha_lateral=0.5, lateral supply = 2× under-canopy supply, meaning the tree sources ~67% of its water from outside the drip line. Ecologically plausible for large parkland trees (root spread >> canopy spread), but the value is somewhat arbitrary. Should be grounded in literature or sensitivity-tested.
- To equalize under vs lateral supply: alpha_lateral ≈ cc/oc = 0.2/0.8 = 0.25
- Low priority — does not affect model correctness, only parameter realism.
