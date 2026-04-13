"""
2D rainfall sweep: alpha × lambda → ΔY (Under−Mono, Outside−Mono)
===================================================================
Run from the project root:
    conda run -n maize-Toff python scripts/rainfall_2d_sweep.py

Outputs
-------
output/rainfall_2d_data.csv   — simulation results (reuse for cosmetic edits)
output/rainfall_2d.png        — figure

Workflow
--------
- If output/rainfall_2d_data.csv already exists, skips simulation and goes
  straight to plotting. Delete the CSV to force a re-run.
- Edit the FIGURE SECTION below to change colors, labels, layout, etc.,
  then re-run — it will read the CSV and replot in seconds.
"""

import os, sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm

# ── 0. Bootstrap: inject model code ──────────────────────────────────────────
# The model lives in tree.ipynb. We need the converted .py temporarily.
# Run from project root so relative paths (data/, farm/) resolve correctly.

_HERE   = os.path.dirname(os.path.abspath(__file__))
_ROOT   = os.path.dirname(_HERE)
_SCRIPT = os.path.join(_ROOT, "_tmp_model_core.py")

os.chdir(_ROOT)

if not os.path.exists(_SCRIPT):
    print("Converting tree.ipynb to script...")
    ret = os.system(
        f"conda run -n maize-Toff jupyter nbconvert --to script tree.ipynb "
        f"--output _tmp_model_core 2>/dev/null"
    )
    if ret != 0 or not os.path.exists(_SCRIPT):
        sys.exit("ERROR: Could not convert tree.ipynb. Run from project root with maize-Toff env active.")

# Execute model core (classes, CETRAD setup, simulate_three_crops_regime)
# We only need up through the function definitions — stop before the expensive
# diagnostic and Monte Carlo cells (marked by the N_SIMS = 300 block).
with open(_SCRIPT) as f:
    lines = f.readlines()

# Find cutoff: first line of the expensive simulation block
cutoff = len(lines)
for i, line in enumerate(lines):
    if line.strip().startswith("N_SIMS = 300"):
        cutoff = i
        break

# Also skip the single-season diagnostic block (lines after "Single-season diagnostic")
diag_start = None
for i, line in enumerate(lines):
    if "Single-season diagnostic" in line and "##" in line:
        diag_start = i
        break

if diag_start is not None:
    core_lines = lines[:diag_start] + lines[
        next(i for i in range(diag_start, cutoff) if "# In[12]:" in lines[i] or "_make_climate" in lines[i]):cutoff
    ]
else:
    core_lines = lines[:cutoff]

_CORE_TMP = os.path.join(_ROOT, "_tmp_core_exec.py")
with open(_CORE_TMP, "w") as f:
    f.writelines(core_lines)

exec(compile(open(_CORE_TMP).read(), _CORE_TMP, "exec"), globals())

os.remove(_CORE_TMP)

# ── 1. SWEEP PARAMETERS ──────────────────────────────────────────────────────
# Edit these to change the grid resolution and simulation count.

# Alpha scale values (storm depth multiplier relative to CETRAD baseline)
ALPHA_SCALES  = [0.5, 0.75, 1.0, 1.25, 1.5, 2.0]

# Lambda scale values (storm frequency multiplier relative to CETRAD baseline)
LAMBDA_SCALES = [0.5, 0.75, 1.0, 1.25, 1.5, 2.0]

N_SIMS = 150    # simulations per grid cell (increase for smoother surface)
SEED   = 42

_TREE = dict(
    Zr=1500, T_MAX=2.0, sw_MPa=-4.0, s_star_MPa=-0.1,
    kc=1.0, canopy_cover=0.2, leaf_fraction=1.0,
)

DATA_PATH = os.path.join(_ROOT, "output", "rainfall_2d_data.csv")

# ── 2. SIMULATION ─────────────────────────────────────────────────────────────
if os.path.exists(DATA_PATH):
    print(f"Loading cached results from {DATA_PATH}")
    df_results = pd.read_csv(DATA_PATH)
else:
    print(f"Running {len(ALPHA_SCALES) * len(LAMBDA_SCALES)} grid cells × {N_SIMS} sims each...")
    rows = []
    for a_scale in ALPHA_SCALES:
        for l_scale in LAMBDA_SCALES:
            factory = lambda a=a_scale, l=l_scale: _make_climate(
                alpha_scale=a, lambda_scale=l
            )
            df_u, df_o, df_m = simulate_three_crops_regime(
                N_SIMS, climate_factory=factory, seed=SEED,
                n_spinup=5, tree_params=_TREE,
            )
            mean_rf = df_m.RF.mean()
            rows.append(dict(
                alpha_scale   = a_scale,
                lambda_scale  = l_scale,
                mean_rf       = mean_rf,
                # Mean seasonal alpha and lambda (for axis labels)
                mean_alpha    = np.mean(_alpha_cetrad) * a_scale,
                mean_lambda   = np.mean(_lambda_cetrad) * l_scale,
                # Yield summaries
                med_under     = df_u.Yield.median(),
                med_outside   = df_o.Yield.median(),
                med_mono      = df_m.Yield.median(),
                mean_under    = df_u.Yield.mean(),
                mean_outside  = df_o.Yield.mean(),
                mean_mono     = df_m.Yield.mean(),
                # Treatment effects
                dY_under      = df_u.Yield.median() - df_m.Yield.median(),
                dY_outside    = df_o.Yield.median() - df_m.Yield.median(),
                dY_net        = df_u.Yield.median() - df_m.Yield.median(),   # Under − Mono
                dY_comp       = df_o.Yield.median() - df_m.Yield.median(),   # Outside − Mono
                dY_fac        = df_u.Yield.median() - df_o.Yield.median(),   # Under − Outside
            ))
            print(
                f"  alpha={a_scale:.2f}× lambda={l_scale:.2f}×  "
                f"RF={mean_rf:.0f} mm  "
                f"under={df_u.Yield.median():.0f}  "
                f"outside={df_o.Yield.median():.0f}  "
                f"mono={df_m.Yield.median():.0f}",
                flush=True,
            )

    df_results = pd.DataFrame(rows)
    df_results.to_csv(DATA_PATH, index=False)
    print(f"Saved simulation results → {DATA_PATH}")

# ── 3. FIGURE SECTION ─────────────────────────────────────────────────────────
# Edit anything below here for cosmetic changes; re-run to see results instantly
# (simulation is skipped because DATA_PATH already exists).

a_vals = sorted(df_results.alpha_scale.unique())
l_vals = sorted(df_results.lambda_scale.unique())

def make_grid(col):
    """Pivot df_results column into (len(a_vals) × len(l_vals)) array."""
    pivot = df_results.pivot(index="alpha_scale", columns="lambda_scale", values=col)
    return pivot.reindex(index=a_vals, columns=l_vals).values

grid_net = make_grid("dY_net")    # Under − Mono

# Axis tick labels
a_labels = [f"{v:.2f}×" for v in a_vals]
l_labels = [f"{v:.2f}×" for v in l_vals]

fig, ax = plt.subplots(figsize=(5.5, 4.5))

vmax = np.nanmax(np.abs(grid_net))
if vmax == 0 or np.isnan(vmax):
    vmax = 1.0
norm = TwoSlopeNorm(vmin=-vmax, vcenter=0, vmax=vmax)

im = ax.pcolormesh(
    np.arange(len(l_vals)), np.arange(len(a_vals)),
    grid_net, norm=norm, cmap="RdBu", shading="nearest",
)

ax.set_xticks(range(len(l_vals)))
ax.set_xticklabels(l_labels, fontsize=8)
ax.set_xlabel("λ (storm frequency)", fontsize=9)
ax.set_yticks(range(len(a_vals)))
ax.set_yticklabels(a_labels, fontsize=8)
ax.set_ylabel("α (storm depth)", fontsize=9)
ax.set_title("Under canopy yield effect (Under − Mono)", fontsize=9, pad=6)

cb = fig.colorbar(im, ax=ax, shrink=0.85, pad=0.03)
cb.set_label("Under − Mono [kg/ha]", fontsize=8)

fig.suptitle(
    r"ΔY vs. storm character  ($Z_r=1500$, $T_{MAX}=2.0$, $\alpha_{lat}=0.5$, "
    f"N={N_SIMS})",
    fontsize=10,
)
fig.tight_layout()

OUT_PATH = os.path.join(_ROOT, "output", "rainfall_2d.png")
fig.savefig(OUT_PATH, dpi=150, bbox_inches="tight")
print(f"Saved figure → {OUT_PATH}")
