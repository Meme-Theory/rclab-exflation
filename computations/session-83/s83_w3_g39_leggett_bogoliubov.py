#!/usr/bin/env python3
"""
S83 W3-G39 — LEGGETT-BOGOLIUBOV-PARTITION
==========================================

Gate: [VERIFY] S83-LEGGETT-BOGOLIUBOV-PARTITION
Classification: PHONONIC
Hypothesis: At K = {1.1, 2.035, 10, 100, 1000, 3.56e5}, the Leggett-vs-Bogoliubov
mode-partition ratio R(K) = W_Leg(K)/W_Bog(K) is MONOTONIC across the K sequence.
PASS: strictly monotonic (all ascending or all descending).
INFO: mostly monotonic (interior reversals that are tiny but non-zero).
FAIL: non-monotonic with an interior extremum outside numerical noise.

SUBSTITUTION CHAIN ([VERIFY])
----------------------------
Step 1 (def):
    K = coth( Delta_BCS / (2 T_eff) )
  ⇒ x = Delta_BCS / T_eff = 2 arccoth(K) = ln( (K+1)/(K-1) )
  ⇒ T_eff(K) = Delta_BCS / ln( (K+1)/(K-1) )

Step 2 (def):
    W_Leg(K) = n_L = 1 / ( exp(Delta_Leggett/T_eff) - 1 )
    W_Bog(K) = n_B = 1 / ( exp(Delta_BCS    /T_eff) - 1 )
  where Delta_Leggett = 0.3061 M_KK (B1↔B2 interband splitting, S82 II.B),
        Delta_BCS     = 0.4643 M_KK (canonical, S70).

Step 3 (subst):
    R(K) = W_Leg/W_Bog = [ exp(Delta_BCS/T_eff) - 1 ] / [ exp(Delta_Leggett/T_eff) - 1 ]
         = [ exp(x)     - 1 ] / [ exp(b*x)       - 1 ]
  where b = Delta_Leggett/Delta_BCS = 0.3061/0.4643 = 0.6593 < 1.

Step 4 (simpl / direction):
    K → 1+   : x → +∞ , exp(x) ≫ exp(b*x) (since b<1) ⇒ R(K) → +∞.
    K → ∞    : x → 0+ , exp(x)-1 ~ x and exp(b*x)-1 ~ b*x ⇒ R(K) → 1/b = 1.517.
  ⇒ R(K) monotonically DECREASES from +∞ at K=1+ toward the asymptote 1/b = 1.517
    as K → ∞, provided monotonicity holds on the full interior. This script
    verifies monotonicity at the six pre-registered K values.

Step 5: Python computation (below). Strict-decreasing check on the 6 values.

ENVIRONMENT: computations venv Python 3.12.
RX 9070 XT / ROCm 7.2 NOT required here (all arithmetic is O(1) per K).
"""

from __future__ import annotations

import hashlib
import os
import sys
from pathlib import Path

# CPU-only: small analytic formulas, no linear algebra. Cap threads.
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------
# Canonical constants — MANDATORY import (no hardcoding framework constants)
# ------------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from canonical_constants import Delta_BCS, M_KK  # noqa: E402

# ------------------------------------------------------------------------------
# Provenance: SHA-256 pin of canonical_constants.py
# ------------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()

CC_PATH = SCRIPT_DIR / "canonical_constants.py"
CC_SHA = sha256_of(CC_PATH)

# ------------------------------------------------------------------------------
# Inputs (printed to stdout in first 20 lines for audit)
# ------------------------------------------------------------------------------
# Delta_Leggett is the B1-B2 interband splitting documented in S82 II.B:
#   Delta_B1 = 0.4645 M_KK, Delta_B2 = 0.7705 M_KK
#   Delta_Leggett = |Delta_B2 - Delta_B1| = 0.3060 M_KK ≈ 0.3061 M_KK (S82 II.B)
Delta_Leggett = 0.3061    # (local) M_KK units, B1-B2 interband splitting (S82 II.B)

K_list = np.array([1.1, 2.035, 10.0, 100.0, 1000.0, 3.56e5])  # (local) 6-point pre-registered K grid

# Derived dimensionless ratio
b = Delta_Leggett / Delta_BCS  # (local) ~ 0.6593, <1 by II.B structure

# ------------------------------------------------------------------------------
# Print audit header (SHA + constants in first 20 lines)
# ------------------------------------------------------------------------------
print("=" * 78)
print("S83 W3-G39 — LEGGETT-BOGOLIUBOV-PARTITION")
print("=" * 78)
print(f"canonical_constants.py SHA-256 = {CC_SHA}")
print(f"Delta_BCS      = {Delta_BCS:.16f}  M_KK  [CANONICAL, Delta_0_OES alias, S70]")
print(f"Delta_Leggett  = {Delta_Leggett:.4f}            M_KK  [LOCAL, S82 II.B B1-B2 splitting]")
print(f"b = Delta_Leggett/Delta_BCS = {b:.6f}")
print(f"M_KK (gravity) = {M_KK:.6e} GeV")
print(f"K_list (6 pts) = {K_list}")
print(f"Sequence convention: probe goes FROM K=1.1 TO K=3.56e5 (ascending in K).")
print("Substitution chain (from docstring):")
print("  x(K)     = ln((K+1)/(K-1))")
print("  T_eff(K) = Delta_BCS / x(K)")
print("  W_Bog(K) = 1/(exp(x) - 1)           [Bose factor at energy Delta_BCS]")
print("  W_Leg(K) = 1/(exp(b*x) - 1)          [Bose factor at energy Delta_Leg]")
print("  R(K)     = W_Leg(K)/W_Bog(K)")
print("           = (exp(x) - 1) / (exp(b*x) - 1)")
print("-" * 78)

# ------------------------------------------------------------------------------
# Core computation
# ------------------------------------------------------------------------------
def x_of_K(K: np.ndarray | float) -> np.ndarray | float:
    """x = Delta_BCS/T_eff = ln((K+1)/(K-1)), defined for K>1."""
    return np.log((K + 1.0) / (K - 1.0))

def T_eff_of_K(K: np.ndarray | float) -> np.ndarray | float:
    """T_eff(K)/M_KK = Delta_BCS / x(K)."""
    return Delta_BCS / x_of_K(K)

def W_Bog_of_K(K: np.ndarray | float) -> np.ndarray | float:
    """Bogoliubov pair-breaking mode occupation (Bose-Einstein at Delta_BCS)."""
    x = x_of_K(K)
    return 1.0 / (np.exp(x) - 1.0)

def W_Leg_of_K(K: np.ndarray | float) -> np.ndarray | float:
    """Leggett interband phase-coherence mode occupation (Bose-Einstein at Delta_Leggett)."""
    x = x_of_K(K)
    return 1.0 / (np.exp(b * x) - 1.0)

def R_of_K(K: np.ndarray | float) -> np.ndarray | float:
    """R(K) = W_Leg/W_Bog = (exp(x)-1)/(exp(b*x)-1)."""
    x = x_of_K(K)
    return (np.exp(x) - 1.0) / (np.exp(b * x) - 1.0)

# Evaluate
x_vals = x_of_K(K_list)
T_vals = T_eff_of_K(K_list)
W_Leg = W_Leg_of_K(K_list)
W_Bog = W_Bog_of_K(K_list)
R_vals = R_of_K(K_list)

# Also compute the S82 V.2-style fraction (frac_L = n_L / (n_L + n_B)) for
# cross-check against pre-verified S82 numbers.
frac_L = W_Leg / (W_Leg + W_Bog)  # (local)
frac_B = W_Bog / (W_Leg + W_Bog)  # (local)

# ------------------------------------------------------------------------------
# Monotonicity diagnosis
# ------------------------------------------------------------------------------
diffs = np.diff(R_vals)  # (local)
strict_inc = bool(np.all(diffs > 0.0))
strict_dec = bool(np.all(diffs < 0.0))
monotonic = strict_inc or strict_dec
# Relative step for numerical-noise judgement
rel_steps = diffs / R_vals[:-1]  # (local)
sign_list = np.sign(diffs).astype(int).tolist()  # (local)
# Weak monotonicity (allow zero but no reversal)
weak_inc = bool(np.all(diffs >= 0.0))
weak_dec = bool(np.all(diffs <= 0.0))
weak_mono = weak_inc or weak_dec

# Locate any interior extremum (sign reversal)
reversal_idx = [i for i in range(len(diffs) - 1) if sign_list[i] * sign_list[i + 1] < 0]  # (local)

# ------------------------------------------------------------------------------
# Verdict
# ------------------------------------------------------------------------------
if monotonic:
    verdict = "PASS"
elif weak_mono:
    verdict = "INFO"
else:
    verdict = "INFO" if abs(max(rel_steps, key=abs)) < 1e-6 else "FAIL"

# ------------------------------------------------------------------------------
# Cross-check against S82 V.2 pre-verified numbers
# ------------------------------------------------------------------------------
# S82 V.2: frac_L(K=2.035) = 0.652, frac_L(K=1.1) ~ 0.756, frac_L(K→∞) ~ 0.603
# Verify our computation agrees to 3 decimals.
idx_2035 = int(np.argmin(np.abs(K_list - 2.035)))  # (local)
fracL_2035 = float(frac_L[idx_2035])  # (local)
fracL_1p1 = float(frac_L[0])  # (local) at K=1.1

print("\n--- Results table ---")
print(f"{'K':>12} {'x=D/T':>10} {'T/D_BCS':>10} {'W_Bog':>14} {'W_Leg':>14} {'R=L/B':>14} {'frac_L':>8}")
for i, K in enumerate(K_list):
    print(
        f"{K:>12.4g} {x_vals[i]:>10.5f} {1.0/x_vals[i]:>10.5f} "
        f"{W_Bog[i]:>14.6e} {W_Leg[i]:>14.6e} {R_vals[i]:>14.6e} {frac_L[i]:>8.4f}"
    )

print("\n--- Monotonicity analysis ---")
print(f"R(K) sequence:   {[f'{r:.6e}' for r in R_vals]}")
print(f"delta R_i:       {[f'{d:+.3e}' for d in diffs]}")
print(f"sign(delta R_i): {sign_list}")
print(f"relative steps:  {[f'{r:+.3e}' for r in rel_steps]}")
print(f"strict_decreasing: {strict_dec}")
print(f"strict_increasing: {strict_inc}")
print(f"monotonic (strict): {monotonic}")
print(f"weak_monotonic:     {weak_mono}")
print(f"reversal indices:   {reversal_idx}")

print("\n--- S82 V.2 cross-check ---")
print(f"frac_L(K=2.035) predicted by S82: 0.652   observed here: {fracL_2035:.4f}")
print(f"frac_L(K=1.1)   predicted by S82: 0.756   observed here: {fracL_1p1:.4f}")
print(f"frac_L(K→∞) asymptote (S82):      0.603   observed at K=3.56e5: {float(frac_L[-1]):.4f}")

# Asymptotic check
R_inf_predicted = 1.0 / b  # (local) limiting value as K->inf
print(f"\nAsymptote R(∞) = 1/b = {R_inf_predicted:.6f}")
print(f"R at K=3.56e5     = {R_vals[-1]:.6f}")

# ------------------------------------------------------------------------------
# Plot
# ------------------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

ax = axes[0]
ax.loglog(K_list, R_vals, "o-", lw=2, ms=8, label=r"$R(K)=W_{\rm Leg}/W_{\rm Bog}$")
ax.axhline(R_inf_predicted, color="gray", ls="--", lw=1, label=rf"$1/b = {R_inf_predicted:.3f}$")
for K, R in zip(K_list, R_vals):
    ax.annotate(f"{R:.3f}", (K, R), textcoords="offset points", xytext=(6, 6), fontsize=8)
ax.set_xlabel(r"$K$")
ax.set_ylabel(r"$R(K) = W_{\rm Leg}/W_{\rm Bog}$")
ax.set_title("Leggett-Bogoliubov ratio across K-corridor")
ax.grid(True, which="both", alpha=0.3)
ax.legend()

ax = axes[1]
ax.semilogx(K_list, frac_L, "o-", lw=2, ms=8, color="C1", label=r"$f_L = n_L/(n_L+n_B)$")
ax.semilogx(K_list, frac_B, "s-", lw=2, ms=8, color="C2", label=r"$f_B = n_B/(n_L+n_B)$")
ax.axhline(0.5, color="gray", ls="--", lw=1)
ax.set_xlabel(r"$K$")
ax.set_ylabel("fraction")
ax.set_ylim(0, 1)
ax.set_title("S82 V.2 fraction form (cross-check)")
ax.grid(True, which="both", alpha=0.3)
ax.legend()

fig.suptitle(
    f"S83 W3-G39: Leggett-Bogoliubov partition — verdict: {verdict}", fontsize=12
)
fig.tight_layout()
out_png = SCRIPT_DIR / "s83_w3_g39_leggett_bogoliubov.png"
fig.savefig(out_png, dpi=130)
plt.close(fig)

# ------------------------------------------------------------------------------
# Save results
# ------------------------------------------------------------------------------
out_npz = SCRIPT_DIR / "s83_w3_g39_leggett_bogoliubov.npz"
np.savez(
    out_npz,
    K_list=K_list,
    x_vals=x_vals,
    T_eff_over_Delta=1.0 / x_vals,
    W_Bog=W_Bog,
    W_Leg=W_Leg,
    R_vals=R_vals,
    frac_L=frac_L,
    frac_B=frac_B,
    Delta_BCS=Delta_BCS,
    Delta_Leggett=Delta_Leggett,
    b_ratio=b,
    diffs=diffs,
    rel_steps=rel_steps,
    sign_list=np.array(sign_list),
    strict_inc=strict_inc,
    strict_dec=strict_dec,
    monotonic=monotonic,
    weak_monotonic=weak_mono,
    reversal_idx=np.array(reversal_idx, dtype=int),
    verdict=verdict,
)

# ------------------------------------------------------------------------------
# Closure SHA-256 — over the ordered input-pin map
# ------------------------------------------------------------------------------
closure_input = (
    f"canonical_constants.py={CC_SHA}|"
    f"Delta_BCS={Delta_BCS:.16e}|"
    f"Delta_Leggett={Delta_Leggett:.6e}|"
    f"K_list={list(K_list)}|"
    f"b={b:.16e}|"
    f"R_vals={[f'{r:.12e}' for r in R_vals]}"
)
closure_sha = hashlib.sha256(closure_input.encode()).hexdigest()  # (local)

# ------------------------------------------------------------------------------
# 4-tuple output tag (final non-verdict line, then verdict line)
# ------------------------------------------------------------------------------
print("\n" + "=" * 78)
scheme_tag = "Bose-Einstein-per-mode"  # (local) convention for occupation computation
convention_tag = "Delta_BCS_canonical_Delta_Leggett_S82-II.B"  # (local)
print(
    f"4-tuple: (value={verdict}, scheme={scheme_tag}, "
    f"convention={convention_tag}, L_max=NA)"
)
print(f"closure_sha256 = {closure_sha}")

# ------------------------------------------------------------------------------
# Append verdict line (S81+ canonical form)
# ------------------------------------------------------------------------------
verdict_file = SCRIPT_DIR / "s83_gate_verdicts.txt"
verdict_line = (
    f"S83-LEGGETT-BOGOLIUBOV-PARTITION: {verdict} -- "
    f"value={verdict} scheme={scheme_tag} convention={convention_tag} "
    f"L_max=NA sha256={closure_sha}\n"
)
with open(verdict_file, "a", encoding="utf-8") as f:
    f.write(verdict_line)

print(f"\nVerdict line appended to: {verdict_file}")
print(verdict_line.strip())
print("=" * 78)
