# Session Log — Trait-based model improvements
**Date:** 2026-03-05

## Goal
Reframe model as trait-based: which tree functional traits determine competition vs facilitation?

## Changes Implemented

### 1. Continuous `leaf_fraction` parameter (replaces `phenology` string)
- **Tree class** (`9adc45cd`): `phenology` param removed; `leaf_fraction ∈ [0,1]` added
- **TreeCropModel.run()** (`3bed3936`): phenology block replaced with continuous logic:
  ```python
  leaf_day_limit = self.tree.leaf_fraction * self.crop.lgp
  if in_crop_season and dos > leaf_day_limit: tree_kc = 0.0; tree_LAI = 0.0
  ```
- **`_tree_sf()`** (`b2d38c76`): uses `leaf_fraction` instead of `phenology == "reverse"` check; scales by lf
- **All archetype dicts**: `phenology="reverse"` → `leaf_fraction=0.0`, `phenology="evergreen"` → `leaf_fraction=1.0`

### 2. T_MAX recalibration: 5.0 → 1.0 mm/day
- Updated in all tree archetype dicts in both notebooks
- At `canopy_cover=0.2`, plot-level peak T = 0.2 mm/day — matches Roupsard (1999) observation
- T_MAX sensitivity grid in `xdn2zql7gcc` preserved (intentional sweep)

### 3. New ARCHETYPES (both notebooks)
```python
"Faidherbia":        dict(Zr=1500, T_MAX=1.0, leaf_fraction=0.0, ...)
"Evergreen deep":    dict(Zr=1500, T_MAX=1.0, leaf_fraction=1.0, ...)
"Evergreen shallow": dict(Zr=600,  T_MAX=1.0, leaf_fraction=1.0, canopy_cover=0.3, ...)
```
Replaces old 2-archetype system (Co-season + Faidherbia).

### 4. Phenology × rainfall heatmap (new Fig 7 in 01_overpass.ipynb)
- New cells inserted after Fig 2 (after cell `cbb7lo2skf7`)
- 6 × 7 grid: `leaf_fraction` ∈ {0, 0.2, 0.4, 0.6, 0.8, 1.0} × `RF_SCALES` (7 levels)
- N=200 paired seasons per cell, full mechanisms (HR + shade + deep roots)
- Species overlay: Faidherbia (lf=0.0, 450mm), Grevillea (lf=1.0, 414mm), Leucaena (lf=0.9, 470mm)

## Files Modified
- `tree.ipynb`: cells `9adc45cd`, `3bed3936`, `b2d38c76`, `f6f289b8`, `f92563f5`, `cqxopwqakn`, `ddr4xsbwn2w`
- `exploratory_notebooks/01_overpass.ipynb`: cells `c3d4e5f6`, `a7b8c9d0`, `c9d0e1f2`, `e1f2a3b4`, `bvmrg188b2k`, `xdn2zql7gcc`, `qx1v0h0jsxe`, `j3n2twpw43l`; new cells for Fig 7

## Verification
- Smoke tests: `leaf_fraction=0.0` gives `T_tree=0.0` in-season ✓
- `leaf_fraction=0.1` gives `T_tree>0` for days 1-18, `T_tree=0` for days 19-180 ✓
- `leaf_fraction=1.0` gives `T_tree>0` throughout ✓
- No functional `phenology=` keyword args remaining ✓
- No `T_MAX=5.0` in archetype dicts (sensitivity grid preserved) ✓

## Open Items (not in scope for this session)
- Rerun all figures with new parameters (user must execute notebooks)
- Add `lgp=180` pass to `run_tree_scenario()` if needed
- Consider adding Fig 7 dual-panel (HR on/off) as suggested in plan

---
## Session: 2026-04-02 — Three-crop design + CETRAD climate fix

### Changes implemented
1. **CETRAD pre-computation cell** (new cell `cetrad_params`): calls `make_climate_parameters()` once, stores `_alpha_cetrad`, `_lambda_cetrad`, `_CLIMATE_KWARGS_FAST`. Confirmed: 555 mm/yr, 376 mm/247-day season.
2. **HR added to outside-canopy zone** in `ThreeCropModel.run()`: both zones computed simultaneously from same initial gradients, jointly capped by available deep water. Outside-canopy HR = `alpha_lateral × hr_max × ΔΨ/ΔΨ_ref`. New arrays: `HR_under`, `HR_outside` in `pre_allocate()` and `output_tree()`.
3. **All `Climate()` calls in simulation loops updated** to use `_CLIMATE_KWARGS_FAST` (calibrated params). Diagnostic cell uses `CLIMATE_KWARGS` (station-based, fine for one-off run).
4. **`_make_climate()` updated** to use `_alpha_cetrad`/`_lambda_cetrad` as base arrays.

### Verification
- HR fires in wet-enough years (HR_u/HR_o split confirmed for seeds 7, 17, 200).
- In true drought years (RF < 375 mm), HR = 0 — physically correct.
- Monte Carlo 300-sim results (baseline): under=1171, outside=763, mono=942 kg/acre.
- Mechanistic decompositions: outside−mono=−179 (competition), under−outside=+408 (facilitation), under−mono=+229 (net).
- Tree T_MAX=2.0 throughout.

### Open questions
- HR_outside > HR_under in some seasons (seed=200: 10 vs 5 mm). This is correct: oc=0.8 is 4× larger area than cc=0.2, so even with alpha_lateral=0.5 the outside zone has more total HR capacity. Per-unit-zone-area, under > outside as expected.
- Facilitation still dominates at T_MAX=2.0. Next step: sweep T_MAX to find competition/facilitation transition.
