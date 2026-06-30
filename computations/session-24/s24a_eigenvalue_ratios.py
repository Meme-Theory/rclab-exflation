"""
S24a Step 6 — re-run: Eigenvalue Ratio Map (S81 canonical form)
====================================================================

Gate: S24A-EIGENVALUE-RATIOS
Original gate: R-1 (24a prompt Section IV) — "R in [17, 66] from H_eff diagonalization"
Original S24a verdict: FAIL (NO phi_paasch crossings at 0.1% or 1% tolerance)

Purpose
-------
Post-process the 16-eigenvalue singlet-sector spectrum at 9 tau points
from s23a_kosmann_singlet.npz and compute

    r_n(tau) = |lambda_{n+1}| / |lambda_n|    for n in 0..14

on the ABSOLUTE-SORTED ascending eigenvalues. Flag ratios within 0.1%
of phi_paasch = 1.531580 (PROVEN S12).

Substitution chain (direction claim: "phi_paasch crossings")
------------------------------------------------------------
  Step 1 (def):  r_n(tau) := |lambda_{n+1}(tau)| / |lambda_n(tau)|
                 with |lambda_0| <= |lambda_1| <= ... <= |lambda_15|
  Step 2 (sub):  monotone-ascending sort ==> r_n >= 1 for all n, tau
  Step 3 (simp): CROSS_n_tau := 1 iff |r_n(tau) - phi_paasch|/phi_paasch < 0.001
  Step 4 (dir):  verdict = "CROSS" if any(CROSS_n_tau) else "NO_CROSSING"

No sign-direction claim is made about phi_paasch relative to r_n prior
to the compute. Pass/fail is OUTPUT, not claim.

Environment
-----------
- Python: venv312 (torch 2.9.1+rocm available, not needed here — NPZ
  post-process only, no matrix diagonalization).
- CPU path: OMP_NUM_THREADS=8 capped (no heavy linalg).
- Canonical constants: phi_paasch, tau_fold imported from
  canonical_constants.py. NO HARDCODES.

Input pins (SHA-256, 64-char)
-----------------------------
- s23a_kosmann_singlet.npz:
    ef547e583cf73e91b3f0d26e1ba14ee74c28d3718ee08dde12e0f17ad2775214
- canonical_constants.py:
    68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f
- original s24a_eigenvalue_ratios.py (computations/_shared):
    64240ef8ad9c37122dfa650068486e364de1c6c57cf8cce1accc9ee1a585c85d

L_max pin
---------
L_max inherits from s23a upstream: 16 = dim(singlet sector) at
L_max = 3 per S52 singlet-projection lineage. Fixed by input; not a
free parameter at this stage.
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import hashlib
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Canonical constants (MANDATORY)
sys.path.insert(0, "C:/sandbox/Ainulindale Exflation/computations")
from canonical_constants import phi_paasch, tau_fold  # noqa: E402

# =====================================================================
# PINS
# =====================================================================
INPUT_NPZ = "C:/sandbox/Ainulindale Exflation/computations/session-23/s23a_kosmann_singlet.npz"
INPUT_NPZ_SHA256 = "ef547e583cf73e91b3f0d26e1ba14ee74c28d3718ee08dde12e0f17ad2775214"
CANONICAL_SHA256 = "68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f"
OUT_DIR = "C:/sandbox/Ainulindale Exflation/computations/_shared/t3-intake"
OUT_NPZ = f"{OUT_DIR}/s24a_eigenvalue_ratios.npz"
OUT_PNG = f"{OUT_DIR}/s24a_eigenvalue_ratios.png"

# Gate threshold: relative tolerance for ratio crossing
TOL_RATIO = 0.001  # (local) 0.1% — same as S24a R-1 gate
TOL_LOOSE = 0.01   # (local) 1% fallback diagnostic

# Expected singlet-sector dim (L_max=3 upstream)
N_EIG_EXPECTED = 16  # (local) structural — fixed by s23a
N_TAU_EXPECTED = 9   # (local) structural — fixed by s23a tau grid


def sha256_of(path: str) -> str:
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


# =====================================================================
# INPUT INTEGRITY
# =====================================================================
observed_sha = sha256_of(INPUT_NPZ)
if observed_sha != INPUT_NPZ_SHA256:
    raise RuntimeError(
        f"INPUT SHA MISMATCH for {INPUT_NPZ}:\n"
        f"  expected {INPUT_NPZ_SHA256}\n"
        f"  got      {observed_sha}"
    )
canonical_path = "C:/sandbox/Ainulindale Exflation/computations/_shared/canonical_constants.py"
observed_canonical = sha256_of(canonical_path)
if observed_canonical != CANONICAL_SHA256:
    print(
        f"NOTE: canonical_constants.py SHA changed since pin. "
        f"expected {CANONICAL_SHA256}, got {observed_canonical}. "
        f"Script continues; record both SHAs in verdict."
    )

print("=" * 60)
print("S24A-EIGENVALUE-RATIOS — re-run")
print("=" * 60)
print(f"phi_paasch (canonical): {phi_paasch}")
print(f"tau_fold   (canonical): {tau_fold}")
print(f"Input NPZ: {INPUT_NPZ}")
print(f"Input SHA: {observed_sha}")
print(f"TOL_RATIO: {TOL_RATIO} (0.1%)")

# =====================================================================
# LOAD
# =====================================================================
d = np.load(INPUT_NPZ)
tau_values = np.asarray(d["tau_values"])  # (local) from input npz
n_tau = len(tau_values)                   # (local)

if n_tau != N_TAU_EXPECTED:
    raise RuntimeError(f"tau count mismatch: {n_tau} vs {N_TAU_EXPECTED}")

print(f"tau_values = {tau_values}")
print(f"n_tau      = {n_tau}")

# =====================================================================
# COMPUTE RATIOS
# =====================================================================
# r_n(tau) = |lambda_{n+1}| / |lambda_n|, sorted ASCENDING abs
ratios = np.zeros((n_tau, N_EIG_EXPECTED - 1))   # (local)
abs_evals_all = np.zeros((n_tau, N_EIG_EXPECTED))  # (local)

for t_idx in range(n_tau):
    evals = np.asarray(d[f"eigenvalues_{t_idx}"])  # (local)
    if evals.shape != (N_EIG_EXPECTED,):
        raise RuntimeError(
            f"eigenvalues_{t_idx} shape {evals.shape} != ({N_EIG_EXPECTED},)"
        )
    abs_sorted = np.sort(np.abs(evals))  # (local)
    abs_evals_all[t_idx] = abs_sorted
    for n in range(N_EIG_EXPECTED - 1):
        if abs_sorted[n] < 1e-14:
            ratios[t_idx, n] = np.inf
        else:
            ratios[t_idx, n] = abs_sorted[n + 1] / abs_sorted[n]

# =====================================================================
# PHI CROSSINGS (pre-registered gate)
# =====================================================================
devs = np.abs(ratios - phi_paasch) / phi_paasch     # (local)
mask_tight = np.isfinite(ratios) & (devs < TOL_RATIO)  # (local)
mask_loose = np.isfinite(ratios) & (devs < TOL_LOOSE)  # (local)

n_tight = int(mask_tight.sum())  # (local)
n_loose = int(mask_loose.sum())  # (local)

print(f"\n--- GATE: phi_paasch crossings at {TOL_RATIO*100:.1f}% ---")
print(f"tight crossings (dev < {TOL_RATIO}): {n_tight}")
print(f"loose crossings (dev < {TOL_LOOSE}): {n_loose}")

if n_tight > 0:
    idx_pairs = np.argwhere(mask_tight)
    for t_idx, n in idx_pairs:
        print(
            f"  CROSSING: tau={tau_values[t_idx]:.3f}  n={n}  "
            f"r={ratios[t_idx,n]:.6f}  dev={devs[t_idx,n]*100:.4f}%"
        )

# Closest ratio overall
finite = np.isfinite(ratios)
if finite.any():
    flat_dev = np.where(finite, devs, np.inf)
    closest = np.unravel_index(np.argmin(flat_dev), flat_dev.shape)
    closest_t = float(tau_values[closest[0]])  # (local)
    closest_n = int(closest[1])                 # (local)
    closest_r = float(ratios[closest])          # (local)
    closest_dev = float(devs[closest])          # (local)
    print(
        f"\nClosest overall: tau={closest_t:.3f} n={closest_n} "
        f"r={closest_r:.6f} dev={closest_dev*100:.3f}%"
    )
else:
    closest_t = closest_n = closest_r = closest_dev = None  # (local)

# =====================================================================
# VERDICT (gate-level)
# =====================================================================
if n_tight > 0:
    verdict = "PASS"        # (local) phi_paasch appears in ratio spectrum
elif n_loose > 0:
    verdict = "INFO"        # (local) near-miss (1%) — structural signal, not gate pass
else:
    verdict = "FAIL"        # (local) no crossing — reproduces S24a R-1 FAIL

print(f"\nGATE VERDICT: {verdict}")

# =====================================================================
# SAVE
# =====================================================================
np.savez(
    OUT_NPZ,
    tau=tau_values,
    ratios=ratios,
    abs_eigenvalues=abs_evals_all,
    phi_paasch=phi_paasch,
    tol_ratio=TOL_RATIO,
    tol_loose=TOL_LOOSE,
    n_tight=n_tight,
    n_loose=n_loose,
    closest_tau=(np.nan if closest_t is None else closest_t),
    closest_n=(-1 if closest_n is None else closest_n),
    closest_ratio=(np.nan if closest_r is None else closest_r),
    closest_dev=(np.nan if closest_dev is None else closest_dev),
    verdict=verdict,
    input_sha256=observed_sha,
)
print(f"\nSaved: {OUT_NPZ}")

# =====================================================================
# PLOT
# =====================================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

ax = axes[0]
ratios_plot = np.clip(ratios, 0.5, 2.5)  # (local) plotting clip only
im = ax.imshow(
    ratios_plot.T,
    aspect="auto",
    origin="lower",
    extent=[tau_values[0], tau_values[-1], 0.5, 15.5],
    cmap="RdYlBu_r",
    vmin=0.8,
    vmax=2.0,
)
if n_tight > 0:
    for t_idx, n in np.argwhere(mask_tight):
        ax.plot(tau_values[t_idx], n + 0.5, "k*", markersize=15, markeredgecolor="white")
ax.axhline(y=phi_paasch, color="k", linestyle="--", alpha=0.3)
ax.axvline(x=tau_fold, color="g", linestyle=":", alpha=0.5, label=f"tau_fold={tau_fold}")
ax.set_xlabel("tau")
ax.set_ylabel("Ratio index n")
ax.set_title(f"r_n(tau) = |lambda_{{n+1}}|/|lambda_n|  (verdict: {verdict})")
plt.colorbar(im, ax=ax, label="Ratio")
ax.legend(loc="upper right", fontsize=9)

ax2 = axes[1]
for n in [0, 3, 7, 11, 14]:
    ax2.plot(tau_values, ratios[:, n], "-o", linewidth=1.5, markersize=5, label=f"n={n}")
ax2.axhline(y=phi_paasch, color="red", linestyle="--", linewidth=2, label=f"phi={phi_paasch}")
ax2.axvline(x=tau_fold, color="g", linestyle=":", alpha=0.5)
ax2.set_xlabel("tau")
ax2.set_ylabel("r_n(tau)")
ax2.set_title("Selected ratios vs tau")
ax2.legend(fontsize=9, ncol=2)
ax2.grid(True, alpha=0.3)
ax2.set_ylim(0.8, 2.0)

plt.tight_layout()
plt.savefig(OUT_PNG, dpi=150)
print(f"Saved: {OUT_PNG}")

print("=" * 60)
print("S24A-EIGENVALUE-RATIOS COMPLETE")
print("=" * 60)
