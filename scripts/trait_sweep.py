"""
Trait surface sweep: leaf_fraction × Zr_tree → ΔY (Under−Mono)
================================================================
Run from the project root:
    conda run -n maize-Toff python scripts/trait_sweep.py

Outputs
-------
output/trait_sweep_data.csv   — simulation results (reuse for cosmetic edits)
output/trait_sweep.png        — figure

Workflow
--------
- If output/trait_sweep_data.csv already exists, skips simulation and goes
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

with open(_SCRIPT) as f:
    lines = f.readlines()

cutoff = len(lines)
for i, line in enumerate(lines):
    if line.strip().startswith("N_SIMS = 300"):
        cutoff = i
        break

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

LF_VALS  = [0.0, 0.25, 0.5, 0.75, 1.0]       # leaf_fraction (0=Faidherbia, 1=evergreen)
ZR_VALS  = [600, 800, 1000, 1250, 1500, 2000]  # root depth [mm]

N_SIMS = 150
SEED   = 42

# Fixed tree parameters (only lf and Zr vary)
_TREE_BASE = dict(
    T_MAX=2.0, sw_MPa=-4.0, s_star_MPa=-0.1,
    kc=1.0, canopy_cover=0.2,
)

# Baseline CETRAD climate
_FACTORY = lambda: _make_climate(alpha_scale=1.0, lambda_scale=1.0)

DATA_PATH = os.path.join(_ROOT, "output", "trait_sweep_data.csv")

# ── 2. SIMULATION ─────────────────────────────────────────────────────────────
if os.path.exists(DATA_PATH):
    print(f"Loading cached results from {DATA_PATH}")
    df_results = pd.read_csv(DATA_PATH)
else:
    print(f"Running {len(LF_VALS) * len(ZR_VALS)} grid cells × {N_SIMS} sims each...")
    rows = []
    for lf in LF_VALS:
        for zr in ZR_VALS:
            tree_params = {**_TREE_BASE, "leaf_fraction": lf, "Zr": zr}
            df_u, df_o, df_m = simulate_three_crops_regime(
                N_SIMS, climate_factory=_FACTORY, seed=SEED,
                n_spinup=5, tree_params=tree_params,
            )
            rows.append(dict(
                leaf_fraction = lf,
                Zr            = zr,
                med_under     = df_u.Yield.median(),
                med_outside   = df_o.Yield.median(),
                med_mono      = df_m.Yield.median(),
                dY_net        = df_u.Yield.median() - df_m.Yield.median(),   # Under − Mono
                dY_comp       = df_o.Yield.median() - df_m.Yield.median(),   # Outside − Mono
                dY_fac        = df_u.Yield.median() - df_o.Yield.median(),   # Under − Outside
            ))
            print(
                f"  lf={lf:.2f}  Zr={zr:4d} mm  "
                f"under={df_u.Yield.median():.0f}  "
                f"outside={df_o.Yield.median():.0f}  "
                f"mono={df_m.Yield.median():.0f}",
                flush=True,
            )

    df_results = pd.DataFrame(rows)
    df_results.to_csv(DATA_PATH, index=False)
    print(f"Saved simulation results → {DATA_PATH}")

# ── 3. FIGURE SECTION ─────────────────────────────────────────────────────────
# Edit anything below here for cosmetic changes; re-run to replot instantly.

lf_vals = sorted(df_results.leaf_fraction.unique())
zr_vals = sorted(df_results.Zr.unique())

def make_grid(col):
    pivot = df_results.pivot(index="Zr", columns="leaf_fraction", values=col)
    return pivot.reindex(index=zr_vals, columns=lf_vals).values

grid_net = make_grid("dY_net")    # Under − Mono

lf_labels = [f"{v:.2f}" for v in lf_vals]
zr_labels  = [f"{v}" for v in zr_vals]

fig, ax = plt.subplots(figsize=(5.5, 4.5))

vmax = np.nanmax(np.abs(grid_net))
if vmax == 0 or np.isnan(vmax):
    vmax = 1.0
norm = TwoSlopeNorm(vmin=-vmax, vcenter=0, vmax=vmax)

im = ax.pcolormesh(
    np.arange(len(lf_vals)), np.arange(len(zr_vals)),
    grid_net, norm=norm, cmap="RdBu", shading="nearest",
)

ax.set_xticks(range(len(lf_vals)))
ax.set_xticklabels(lf_labels, fontsize=8)
ax.set_xlabel("Leaf fraction (0 = Faidherbia, 1 = evergreen)", fontsize=9)
ax.set_yticks(range(len(zr_vals)))
ax.set_yticklabels(zr_labels, fontsize=8)
ax.set_ylabel("Root depth $Z_r$ [mm]", fontsize=9)
ax.set_title("Under canopy yield effect (Under − Mono)", fontsize=9, pad=6)

cb = fig.colorbar(im, ax=ax, shrink=0.85, pad=0.03)
cb.set_label("Under − Mono [kg/ha]", fontsize=8)

fig.suptitle(
    r"Trait surface  ($T_{MAX}=2.0$, $\alpha_{lat}=0.5$, baseline rainfall, "
    f"N={N_SIMS})",
    fontsize=10,
)
fig.tight_layout()

OUT_PATH = os.path.join(_ROOT, "output", "trait_sweep.png")
fig.savefig(OUT_PATH, dpi=150, bbox_inches="tight")
print(f"Saved figure → {OUT_PATH}")
