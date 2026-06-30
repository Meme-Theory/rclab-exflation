#!/usr/bin/env python3
"""
S84 W5-56 -- S84-R4-CROSS-CLASS-CONTROL
=======================================

Gate: W5-56 (GEOMETRIC / [AUDIT] [VERIFY])
Agent: volovik-superfluid-universe-theorist

Pre-registered hypothesis (from session-84-plan-w5.md section W5-56):
  The R4 FAIL at K=15.95 (S82 OOM ladder; S83 II.C "BCS-dimensional-inconsistency")
  is a property SPECIFIC to the 3He-B universality class (BDI, N_3=0, fully gapped
  topological superfluid). Recomputing R4 in an A-phase analog (AIII chiral class,
  Weyl points with N_3=2) either (a) confirms the FAIL is class-specific and the
  framework's 3He-B inheritance is preserved [PASS], or (b) confirms the FAIL is
  a cross-class universal dimensional error that the framework inherits regardless
  of topology [FAIL].

PASS/FAIL/INFO thresholds (verbatim from plan):
  PASS (class-specific, inheritance preserved): R4(AIII) < 3.0 (O(1), dimensionally
        consistent) while R4(3He-B)=15.95 preserved.
  FAIL (cross-class error): R4(AIII) >= 10 (same 15.95 regime); forces R4-ERROR
        global tag + convention-recount "5 -> 3 physical + 2 dim-error".
  INFO:  3 <= R4(AIII) < 10 (intermediate; class-dependent but not cleanly separated).
  Tolerance: ABSOLUTE (factor-of-3 threshold on R4).

Substitution chain (per plan Step 1-4):
  Step 1 (definitions):
    R4 := 1 + 2 * (n_pairs / N_modes) -- legacy naive Bogoliubov squeeze reading
          where n_pairs is a Fock-space integer and N_modes is a single-particle
          Hilbert-space dimension. The dimensional-grade mismatch (many-body
          integer / single-particle dim) is the S83 II.C diagnosed error.
    3He-B: AZ class BDI, T^2=+1, C^2=+1, N_3=0 (fully gapped bulk). Framework
          fold spectrum: 8 single-particle modes (4 x B2 + 1 x B1 + 3 x B3).
          n_pairs^BDI = 59.8 from Parker pair production at transit (S38).
    A-phase analog: AZ class AIII (chiral), Weyl points at K^(a) = +/- p_F l-hat,
          topological charge |N_3| = 2 per spin (Volovik 2003 Ch. 7-8; Volovik
          paper 10 Sec. 2; Volovik paper 03 Sec. 2(b)).
          Near each Weyl point the inverse propagator is
          G^{-1} = Gamma^mu (p_mu - p^(0)_mu), giving 2 chiralities per Fermi
          point (left/right). 2 Weyl points x 2 chiralities = 4 low-energy
          cone modes (minimal AIII mode count). Naive 8-mode (same as BDI)
          is also recorded as a sensitivity variant.
    f_Weyl(N_3=2): chiral-anomaly pair-production enhancement for a |N_3|-charge
          Fermi point (Volovik 1998 axial anomaly in 3He-A, paper 08 Eq. 2.13):
          anomalous pair-creation current scales with N_3. For pair count we
          record f_Weyl in {1.0 (no enhancement / anomaly-free texture),
                            2.0 (linear-in-N_3 Adler-Bell-Jackiw current),
                            4.0 (N_3^2 squared-enhancement bound)}.

  Step 2 (substitution):
    K_R4^BDI       = 1 + 2 * (n_pairs^BDI / N_modes^BDI)
                   = 1 + 2 * (59.8 / 8) = 15.95 (baseline, reproduced).
    K_R4^AIII(f, N_modes^AIII)
                   = 1 + 2 * (f_Weyl * n_pairs^BDI / N_modes^AIII).

  Step 3 (simplification):
    Evaluate K_R4^AIII on the grid f_Weyl in {1, 2, 4} x N_modes^AIII in {4, 8}.
    The MINIMUM of K_R4^AIII across these variants is the conservative PASS
    candidate (it gives the smallest AIII value; if even the MINIMUM exceeds
    10, the FAIL is cross-class-robust to all reasonable parametrizations).

  Step 4 (direction):
    Each sensible Weyl parametrization inflates the ratio (f_Weyl*n/N_modes)
    ABOVE the BDI value (because f_Weyl >= 1 and N_modes^AIII <= N_modes^BDI).
    Therefore K_R4^AIII >= K_R4^BDI = 15.95 >= 10 -> FAIL (cross-class error).
    Only a contrived choice f_Weyl=1 AND N_modes^AIII=8 reproduces the BDI
    value exactly (no "correction"); all other Weyl-physics-motivated choices
    push the FAIL further. No reasonable AIII parametrization lands at R4 < 3.0.

Machinery pin (PRDR, verbatim from plan):
  N_eval     : analytical point evaluation in BDI AND AIII
  L_max      : N/A
  scan_range : f_Weyl in {1.0, 2.0, 4.0}, N_modes^AIII in {4, 8}
  step_size  : N/A
  tolerance  : 1e-3 (analytical)
  scheme     : dim-conv (dimensional-convention canonical)
  convention : R4 (BCS 4-dim) evaluated in BDI and AIII
  random_seed: N/A
  GPU path   : N/A (analytical; no linear algebra)

Input SHA-256 pins (computed at runtime):
    computations/_shared/canonical_constants.py
    researchers/Volovik/03_2008_Volovik_Emergent_Physics_Fermi_Point.md   (Fermi-point classification)
    researchers/Volovik/08_1998_Volovik_Axial_Anomaly_3He_Baryogenesis.md (ABJ current, N_3 dependence)
    researchers/Volovik/10_2019_Volovik_Topological_Superfluids.md        (3He-A/B AZ-class survey; surrogate for 2003 monograph Ch. 7-8)
    researchers/Volovik/01_2001_Volovik_Superfluid_Analogies_Cosmological.md (3He-A Weyl emergent gravity)

  Note: the plan pins `researchers/Volovik/volovik-2003-universe-in-a-helium-droplet.md`,
  which is not present in the repo as a single markdown transcription (only the
  published-paper subset is transcribed). Papers 03, 08, 10, 01 cover the same
  Ch. 7-8 content (AZ classification; Weyl points with N_3=+/-2 in 3He-A; BDI
  fully-gapped structure of 3He-B; ABJ anomaly coefficient). The pin is replaced
  by these four with explicit SHA-256 hashes (cross-class class assignment is
  structurally unchanged under the surrogate).

Output 4-tuple (emitted on final non-verdict line):
    (value=<R4_AIII_min>, scheme=dim-conv, convention=R4, L_max=N/A)

Outputs:
    computations/session-84/s84_w5_56_data.npz
    computations/session-84/s84_w5_56_plot.png
    computations/session-84/s84_gate_verdicts.txt  (verdict line appended)
"""

import hashlib
import os
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Canonical-constants imports (MANDATORY)
from canonical_constants import n_pairs, N_dof_BCS

# ---------------------------------------------------------------------------
# Paths + input SHA-256 pins (emitted first 20 lines of stdout)
# ---------------------------------------------------------------------------
HERE = Path(__file__).resolve().parent                                      # (local)
PROJECT_ROOT = HERE.parent                                                  # (local)

INPUT_FILES = [                                                             # (local)
    HERE / "canonical_constants.py",
    PROJECT_ROOT / "researchers" / "Volovik" / "03_2008_Volovik_Emergent_Physics_Fermi_Point.md",
    PROJECT_ROOT / "researchers" / "Volovik" / "08_1998_Volovik_Axial_Anomaly_3He_Baryogenesis.md",
    PROJECT_ROOT / "researchers" / "Volovik" / "10_2019_Volovik_Topological_Superfluids.md",
    PROJECT_ROOT / "researchers" / "Volovik" / "01_2001_Volovik_Superfluid_Analogies_Cosmological.md",
]

def _sha256_of_path(p: Path) -> str:
    """SHA-256 hex of file contents; 'MISSING' token if absent."""
    if not p.exists():
        return "MISSING"
    h = hashlib.sha256()                                                    # (local)
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


INPUT_PIN_MAP = {                                                           # (local)
    str(p.relative_to(PROJECT_ROOT)).replace(os.sep, "/"): _sha256_of_path(p)
    for p in INPUT_FILES
}

print("=" * 78)
print("S84 W5-56 -- S84-R4-CROSS-CLASS-CONTROL")
print("=" * 78)
print("Input SHA-256 pins:")
for k, v in INPUT_PIN_MAP.items():
    print(f"  {k}: {v}")
print("-" * 78)


# ---------------------------------------------------------------------------
# R4 formula + class parametrizations
# ---------------------------------------------------------------------------
def R4_formula(n_pairs_eff: float, N_modes_eff: float) -> float:
    """Legacy naive Bogoliubov squeeze reading.

    K_R4 = 1 + 2 * (n_pairs_eff / N_modes_eff)

    The dimensional-grade error (S83 II.C) is that n_pairs is a Fock-space
    integer and N_modes is a single-particle Hilbert-space dimension; their
    ratio is not a per-mode occupation. We apply the SAME formula to both
    classes -- the test is whether the AIII parametrization rescues the
    dimensional inconsistency.
    """
    return 1.0 + 2.0 * (n_pairs_eff / N_modes_eff)


# --- BDI (3He-B analog, baseline) ------------------------------------------
n_pairs_BDI = n_pairs                                                       # (local) 59.8 from S38
N_modes_BDI = N_dof_BCS                                                     # (local) 8 = 4B2 + 1B1 + 3B3
R4_BDI = R4_formula(n_pairs_BDI, N_modes_BDI)                               # (local) = 15.95 baseline

# --- AIII (A-phase / Weyl analog) ------------------------------------------
# f_Weyl enumerates chiral-anomaly-enhancement choices for N_3=2:
#   1.0 = no enhancement (anomaly-free texture; lower bound)
#   2.0 = linear-in-N_3 Adler-Bell-Jackiw pair-creation current (Volovik
#         paper 08 Eq. 2.13: anomalous current proportional to N_3 for a
#         charge-N_3 Fermi point).
#   4.0 = N_3^2 = 4 squared-enhancement (anomaly-coefficient-squared upper
#         bound; appears in axial-current two-point functions).
# N_modes^AIII enumerates low-energy mode counts:
#   4 = 2 Weyl points x 2 chiralities (minimal Weyl cone count; the relevant
#       single-particle dim of the low-energy effective theory near the
#       N_3=2 Fermi points).
#   8 = naive BDI-matched count (records class-insensitive variant).
f_Weyl_grid = np.array([1.0, 2.0, 4.0])                                     # (local)
N_modes_AIII_grid = np.array([4, 8])                                        # (local)

# Full 2D grid of R4(AIII)
R4_AIII_grid = np.zeros((len(f_Weyl_grid), len(N_modes_AIII_grid)))         # (local)
for i, fW in enumerate(f_Weyl_grid):
    for j, Nm in enumerate(N_modes_AIII_grid):
        n_eff = fW * n_pairs_BDI                                            # (local)
        R4_AIII_grid[i, j] = R4_formula(n_eff, Nm)

# Min / max / reference AIII values
R4_AIII_min = float(np.min(R4_AIII_grid))                                   # (local)
R4_AIII_max = float(np.max(R4_AIII_grid))                                   # (local)

# Canonical-reference AIII point: f_Weyl = 2 (linear-in-N_3, Volovik paper 08),
# N_modes = 4 (minimal Weyl cone count). This is the "physics-natural" value.
R4_AIII_ref = R4_formula(2.0 * n_pairs_BDI, 4)                              # (local) = 1 + 2*(119.6/4) = 60.8

# ---------------------------------------------------------------------------
# Verdict logic (pre-registered thresholds)
# ---------------------------------------------------------------------------
# PASS:  R4_AIII_min  < 3.0 AND R4_BDI preserved at 15.95
# FAIL:  R4_AIII_min >= 10.0 (cross-class error)
# INFO:  3.0 <= R4_AIII_min < 10.0

# Note: we use R4_AIII_MIN as the decision variable (most-conservative /
# smallest AIII value across all Weyl parametrizations). If even the MINIMUM
# AIII value exceeds 10, the FAIL is cross-class-robust.

PASS_UPPER = 3.0                                                            # (local)
FAIL_LOWER = 10.0                                                           # (local)

if R4_AIII_min < PASS_UPPER:
    verdict = "PASS"                                                        # (local)
elif R4_AIII_min >= FAIL_LOWER:
    verdict = "FAIL"                                                        # (local)
else:
    verdict = "INFO"                                                        # (local)

# BDI baseline reproduction sanity check
assert abs(R4_BDI - 15.95) < 1e-2, f"BDI baseline drift: got {R4_BDI}"

print(f"n_pairs^BDI = {n_pairs_BDI}")
print(f"N_modes^BDI = {N_modes_BDI}")
print(f"R4_BDI      = 1 + 2*({n_pairs_BDI}/{N_modes_BDI}) = {R4_BDI:.4f}  (S82 baseline)")
print()
print("AIII grid (rows = f_Weyl, cols = N_modes^AIII):")
print(f"  f_Weyl   \\  N_modes = {list(N_modes_AIII_grid)}")
for i, fW in enumerate(f_Weyl_grid):
    row = ", ".join(f"{R4_AIII_grid[i,j]:.3f}" for j in range(len(N_modes_AIII_grid)))  # (local)
    print(f"  {fW:<8.2f}                   [{row}]")
print()
print(f"R4_AIII_min (most-conservative) = {R4_AIII_min:.4f}")
print(f"R4_AIII_max                     = {R4_AIII_max:.4f}")
print(f"R4_AIII_ref (f_Weyl=2, Nm=4)    = {R4_AIII_ref:.4f}")
print()
print(f"Verdict thresholds: PASS if R4_AIII_min < {PASS_UPPER}, "
      f"FAIL if R4_AIII_min >= {FAIL_LOWER}")
print(f"Decision variable R4_AIII_min = {R4_AIII_min:.4f} -> verdict = {verdict}")

# ---------------------------------------------------------------------------
# Closure SHA-256 (ordered input-pin map)
# ---------------------------------------------------------------------------
closure_serialization = "\n".join(                                          # (local)
    f"{k}={v}" for k, v in INPUT_PIN_MAP.items()
)
closure_sha256 = hashlib.sha256(closure_serialization.encode("utf-8")).hexdigest()  # (local)

# ---------------------------------------------------------------------------
# Save data
# ---------------------------------------------------------------------------
data_path = HERE / "s84_w5_56_data.npz"                                     # (local)
np.savez(
    data_path,
    R4_BDI=R4_BDI,
    R4_AIII_grid=R4_AIII_grid,
    R4_AIII_min=R4_AIII_min,
    R4_AIII_max=R4_AIII_max,
    R4_AIII_ref=R4_AIII_ref,
    f_Weyl_grid=f_Weyl_grid,
    N_modes_AIII_grid=N_modes_AIII_grid,
    n_pairs_BDI=n_pairs_BDI,
    N_modes_BDI=N_modes_BDI,
    PASS_UPPER=PASS_UPPER,
    FAIL_LOWER=FAIL_LOWER,
    verdict=verdict,
    closure_sha256=closure_sha256,
)
print(f"Data -> {data_path}")

# ---------------------------------------------------------------------------
# Plot: R4 in BDI vs AIII with factor-3 bands
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8.2, 5.6))                                  # (local)

# BDI point
ax.scatter([0], [R4_BDI], marker="s", s=170, color="C3", zorder=5,
           edgecolor="black", label=f"BDI (3He-B): R4 = {R4_BDI:.2f}")

# AIII grid scatter
markers = ["o", "^"]                                                        # (local)
colors = ["C0", "C1", "C2"]                                                 # (local)
for j, Nm in enumerate(N_modes_AIII_grid):
    for i, fW in enumerate(f_Weyl_grid):
        ax.scatter([1], [R4_AIII_grid[i, j]], marker=markers[j], s=160,
                   color=colors[i], zorder=4, edgecolor="black",
                   label=f"AIII f_W={fW:.0f}, N={Nm}: R4={R4_AIII_grid[i,j]:.2f}")

# Factor-3 PASS band around O(1) (dimensionally consistent region):
# PASS band is R4 in [0, 3.0]; INFO band [3.0, 10.0]; FAIL >= 10.
ax.axhspan(0.0,  PASS_UPPER, alpha=0.18, color="green",
           label=f"PASS (R4 < {PASS_UPPER})")
ax.axhspan(PASS_UPPER, FAIL_LOWER, alpha=0.15, color="goldenrod",
           label=f"INFO ({PASS_UPPER} <= R4 < {FAIL_LOWER})")
ax.axhspan(FAIL_LOWER, 70.0, alpha=0.12, color="red",
           label=f"FAIL (R4 >= {FAIL_LOWER})")

ax.axhline(15.95, linestyle="--", color="C3", linewidth=1.2,
           label="S82 baseline R4(BDI)=15.95")

ax.set_xticks([0, 1])
ax.set_xticklabels(["BDI (3He-B, N_3=0)", "AIII (A-phase Weyl analog, N_3=2)"])
ax.set_ylabel("R4 = 1 + 2*(n_pairs_eff / N_modes_eff)")
ax.set_ylim(0, 70)
ax.set_title("W5-56: R4 cross-class control\n"
             "Dimensional-error persists AIII parametrizations "
             f"-> verdict = {verdict}")
ax.grid(True, alpha=0.3)
# Legend outside plot (many entries)
ax.legend(loc="center left", bbox_to_anchor=(1.02, 0.5), fontsize=7,
          frameon=True)
plt.tight_layout()

plot_path = HERE / "s84_w5_56_plot.png"                                     # (local)
plt.savefig(plot_path, dpi=140, bbox_inches="tight")
plt.close(fig)
print(f"Plot -> {plot_path}")

# ---------------------------------------------------------------------------
# Verdict line (canonical S81+ form)
# ---------------------------------------------------------------------------
# value reports R4_AIII_min (decision variable, most-conservative AIII choice)
verdict_line = (                                                            # (local)
    f"W5-56: {verdict} -- value={R4_AIII_min:.4f} scheme=dim-conv "
    f"convention=R4 L_max=N/A sha256={closure_sha256}"
)
verdict_file = HERE / "s84_gate_verdicts.txt"                               # (local)
with open(verdict_file, "a", encoding="utf-8") as f:
    f.write(verdict_line + "\n")

# Final 4-tuple tag (last non-verdict line before verdict)
print()
print(f"4-tuple: (value={R4_AIII_min:.4f}, scheme=dim-conv, "
      f"convention=R4, L_max=N/A)")
print(verdict_line)
print(f"Appended -> {verdict_file}")
