"""Axis-B per-element verdict heatmap + n_PBH band-edge inside-conjunct diagnostic.

Source citation: derivative output — mirrors plan §W6-3 plot output_artifact
(session-92-plan-w6.md lines 1578-1581) which describes "per-element PASS/FAIL/
INFO heatmap (5 elements × 2 axes; JOINT elements requiring PASS-AND on both)".
This is the Axis-B half of that heatmap, with diagnostic band-edge overlay.
"""
from pathlib import Path
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path("computations/_shared").resolve()))
from canonical_constants import tau_fold, M_KK_gravity  # noqa: F401 — canonical pin per math-scripts.md

npz = np.load("computations/session-92/s92_w6_3_axis_b_volovik_vii_ax_stage_2_verify.npz", allow_pickle=True)

# Per-element verdicts (Axis-B audits Element 1 + 4 + JOINT 3 + JOINT 5)
elements = ["Element 1\n(substrate-IS)", "Element 4\n(env Level-2-binding)",
            "JOINT Element 3\n(bridge map)", "JOINT Element 5\n(Level-3 anchor)"]
verdicts = [str(npz["element_1_verdict"]), str(npz["element_4_verdict"]),
            str(npz["joint_element_3_verdict"]), str(npz["joint_element_5_verdict"])]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5), gridspec_kw={"width_ratios": [1.0, 1.4]})

# Panel 1: per-element verdict bar
colors = ["#2ca02c" if v == "PASS" else ("#d62728" if v == "FAIL" else "#ff7f0e") for v in verdicts]
ypos = np.arange(len(elements))
ax1.barh(ypos, [1] * len(elements), color=colors, edgecolor="black")
for i, v in enumerate(verdicts):
    ax1.text(0.5, i, v, ha="center", va="center", fontsize=13, fontweight="bold", color="white")
ax1.set_yticks(ypos)
ax1.set_yticklabels(elements)
ax1.set_xticks([])
ax1.set_xlim(0, 1)
ax1.set_title(f"Axis-B (volovik) per-element verdicts\nComposite: {str(npz['axis_b_composite_verdict'])}",
              fontsize=12, fontweight="bold")
ax1.invert_yaxis()

# Panel 2: n_PBH band-edge diagnostic
n_central = float(npz["n_PBH_central"])
sigma_lo = float(npz["n_PBH_1sigma_lower"])
sigma_hi = float(npz["n_PBH_1sigma_upper"])
conj_lo = float(npz["upper_22_6_conjunct_lower"])
conj_hi = float(npz["upper_22_6_conjunct_upper"])

# Use log scale
ax2.set_xscale("log")
# Upper-22.6%-conjunct band (target)
ax2.axvspan(conj_lo, conj_hi, ymin=0.55, ymax=0.85, alpha=0.25, color="#1f77b4",
            label=f"Upper-22.6%-conjunct\n[{conj_lo:.3e}, {conj_hi:.3e}]")
# 1σ band (substrate-IS prediction)
ax2.axvspan(sigma_lo, sigma_hi, ymin=0.15, ymax=0.45, alpha=0.45, color="#d62728",
            label=f"1σ band substrate-IS\n[{sigma_lo:.3e}, {sigma_hi:.3e}]")
# Central
ax2.axvline(n_central, color="black", linestyle="--", linewidth=2,
            label=f"n_PBH_central = {n_central:.4e}")
ax2.axvline(conj_lo, color="#1f77b4", linestyle=":", linewidth=1.5)

# Annotate the FAIL: lower 1σ edge below conjunct lower edge
ax2.annotate(
    f"FAIL: 1σ lower {sigma_lo:.3e} < conjunct lower {conj_lo:.3e}\n(below by {(conj_lo - sigma_lo) * 1e23:.3f}e-23)",
    xy=(sigma_lo, 0.30), xytext=(1e-23, 0.95),
    arrowprops=dict(arrowstyle="->", color="darkred", lw=1.5),
    fontsize=9, color="darkred", fontweight="bold",
    bbox=dict(boxstyle="round,pad=0.4", facecolor="#ffe6e6", edgecolor="darkred"),
)

ax2.set_xlim(5e-24, 5e-22)
ax2.set_ylim(0, 1)
ax2.set_xlabel("n_PBH (m⁻³)", fontsize=11)
ax2.set_yticks([])
ax2.set_title(
    f"JOINT Element 5: 1σ band-edge vs upper-22.6%-conjunct\n"
    f"refinement at L_max=14: {float(npz['refinement_at_Lmax14']):.4f}× "
    f"(target {float(npz['refinement_target']):.4f}×)",
    fontsize=11, fontweight="bold")
ax2.legend(loc="lower right", fontsize=8)
ax2.grid(True, which="both", linestyle=":", alpha=0.4)

plt.suptitle(
    "S92-W6-CF-S92-W5-4-STAGE-2-VII-AX-CROSS-AXIS-VERIFY-AXIS-B  (volovik-superfluid-universe-theorist)\n"
    "Stage-2 cross-axis verify on §VII.AX.OP-PROJ STAGE-1-CANDIDATE  |  obs_2 = s91_w5_3_cf41_upper_22_6.npz (Axis-B-ONLY)",
    fontsize=11, y=1.02)
plt.tight_layout()
out = Path("computations/session-92/s92_w6_3_axis_b_volovik_vii_ax_stage_2_verify.png")
plt.savefig(out, dpi=110, bbox_inches="tight")
print(f"Plot saved: {out}")
