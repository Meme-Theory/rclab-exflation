"""S85-W7-CC-GAMMA — W7-3.

[VERIFY] gate: reconcile impedance-mismatch Γ with observed DM/DE ratio
0.385 (Planck 2020 DR2) within 15% RATIO tolerance.

Hypothesis (plan §W7-3 step 5):
  Ω_DM/Ω_DE = f_GGE / (1 − Γ), where Γ = 0.99970 (S37 canonical pin),
  f_GGE is GGE Leggett-channel quasiparticle density fraction from
  S50 GGE-permanence theorem. The gate tests whether the framework-
  intrinsic ratio reproduces 0.385 to within 15%.

Substitution chain (plan §W7-3 step 10):

  Step 1 (definitions):
    Γ       = 0.99970    [S37 canonical impedance-transmission]
    ε_eff   = 1 − Γ = 3e-4   [effacement residual → DE-like leakage]
    f_GGE   = GGE Leggett-channel fraction of substrate rest-energy
             ≡ (1/Vol_SU3) · Σ_k |β_k|² ω_k / ρ_substrate   [S50 formula]
    ρ_DM    = f_GGE · ρ_substrate                [DM from Leggett GGE]
    ρ_DE    = ε_eff · ρ_substrate                [DE from effacement]
    Ω_DM/Ω_DE = f_GGE / ε_eff

  Step 2 (plan, substitution):
    ratio_derived = f_GGE / ε_eff = f_GGE / 3e-4

  Step 3 (simplification — plan's required f_GGE for exact PASS):
    ratio_derived = 0.385   ⇒   f_GGE_required = 0.385 · 3e-4 = 1.155e-4
    (Python-verified: 0.385 × 0.00030 = 1.155e-4)

  Step 4 (direction):
    Microscopic f_GGE from (1/Vol_SU3) · Σ_k |β_k|² ω_k uses S78 W1-E
    |β|²_pivot = 4.255e+04 and Parker integrand built in W7-2. For
    normalization by ρ_substrate = M_KK^4 × Vol_SU3_Haar:
      f_GGE = 2 · ρ_Parker / (M_KK^4 · Vol_SU3_Haar²)
    Direction: ratio_derived = f_GGE / ε_eff; PASS iff lands in 15%
    of 0.385.

PASS/FAIL/INFO (plan §W7-3 step 9):
  PASS: |ratio_derived − 0.385| / 0.385 ≤ 0.15 (RATIO 15%)
  FAIL: |residual| / 0.385 > 0.50
  INFO: 0.15 < |residual|/0.385 ≤ 0.50

Machinery pin (plan §7):
  L_max=10, scheme=S37-effacement-canonical, convention=Planck-2020-DR2,
  Γ=0.99970 (DO NOT recompute), tolerance=15% RATIO, random_seed=42,
  GPU path=N/A (scalar).

Outputs:
  computations/session-85/s85_w7_cc_gamma_dm_de_ratio.npz
  computations/session-85/s85_w7_cc_gamma_dm_de_ratio.png
Verdict appended to computations/session-85/s85_gate_verdicts.txt with
S85+ dual-SHA.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

from canonical_constants import (  # noqa: E402
    Gamma_effacement,
    Vol_SU3_Haar,
    Omega_DM_obs,
    Omega_DE_obs,
    Omega_DM,
    Omega_Lambda,
    M_KK_gravity,
    tau_fold,
    PI,
    n_Bog,
    dt_transit,
)


# ----------------------------------------------------------------------------
# Section 0 — input-pin map and closure SHA
# ----------------------------------------------------------------------------
def _file_sha(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


INPUT_PINS: dict[str, str] = {}

_static_files = [
    _HERE / "canonical_constants.py",
    _HERE / "s78_pre_fold_vacuum.py",
    _HERE / "s78_pre_fold_vacuum.npz",
    _HERE / "s85_w7_cc6_parker_residue.npz",  # W7-2 output for ρ_Parker anchor
]
for _sf in _static_files:
    if _sf.exists():
        INPUT_PINS[_sf.name] = _file_sha(_sf)
    else:
        INPUT_PINS[_sf.name] = "MISSING"


# Machinery pins (plan §7)
L_max = 10  # (local) plan §7
scheme = "S37-Gamma-canonical"  # (local) plan §8
convention = "Planck2020-DR2"  # (local) plan §8
tolerance_RATIO = 0.15  # (local) plan §9 PASS
FAIL_RATIO = 0.50  # (local) plan §9 FAIL
random_seed = 42  # (local) unused

INPUT_PINS["L_max"] = f"{L_max:d}"
INPUT_PINS["scheme"] = scheme
INPUT_PINS["convention"] = convention
INPUT_PINS["tolerance_RATIO"] = f"{tolerance_RATIO:.6f}"
INPUT_PINS["FAIL_RATIO"] = f"{FAIL_RATIO:.6f}"
INPUT_PINS["random_seed"] = f"{random_seed:d}"

# Canonical-constant pins
INPUT_PINS["Gamma_effacement"] = f"{Gamma_effacement:.10e}"
INPUT_PINS["Omega_DM_obs"] = f"{Omega_DM_obs:.10e}"
INPUT_PINS["Omega_DE_obs"] = f"{Omega_DE_obs:.10e}"
INPUT_PINS["Vol_SU3_Haar"] = f"{Vol_SU3_Haar:.10e}"
INPUT_PINS["M_KK_gravity_GeV"] = f"{M_KK_gravity:.10e}"

CLOSURE_INPUT = json.dumps(INPUT_PINS, sort_keys=True, separators=(",", ":"))
CLOSURE_SHA = hashlib.sha256(CLOSURE_INPUT.encode("utf-8")).hexdigest()

print("=" * 78)
print("S85 W7-3: CC-GAMMA Ω_DM/Ω_DE reconciliation via impedance mismatch")
print("=" * 78)
print(f"closure SHA-256 (64 char): {CLOSURE_SHA}")
print(f"closure SHA-256 (16 head): {CLOSURE_SHA[:16]}")
print()
print("--- input pin SHAs and values ---")
for _k, _v in INPUT_PINS.items():
    print(f"  {_k:<32s}: {_v}")
print()


# ----------------------------------------------------------------------------
# Section 1 — Plan step 1/2 canonical arithmetic
# ----------------------------------------------------------------------------
eps_eff = 1.0 - Gamma_effacement  # (local) plan step 1 effacement residual
ratio_obs_2020 = Omega_DM_obs / Omega_DE_obs  # (local) Planck 2020 DR2
ratio_obs_2018 = Omega_DM / Omega_Lambda  # (local) Planck 2018 canonical
# Plan cites observed ratio 0.385; we verify against 2020 DR2.
f_GGE_required = ratio_obs_2020 * eps_eff  # (local) plan step 3 Python-verified

print("--- Plan step 1/2 canonical arithmetic ---")
print(f"  Γ (Gamma_effacement)       = {Gamma_effacement:.6f}")
print(f"  ε_eff = 1 − Γ              = {eps_eff:.6e}")
print(f"  Ω_DM_obs (Planck 2020 DR2) = {Omega_DM_obs:.6f}")
print(f"  Ω_DE_obs (Planck 2020 DR2) = {Omega_DE_obs:.6f}")
print(f"  ratio_obs_2020             = {ratio_obs_2020:.6f}")
print(f"  ratio_obs_2018 (cf.)       = {ratio_obs_2018:.6f}")
print(f"  plan cited ratio_obs       = 0.385")
print(f"  f_GGE_required (plan eq.)  = ratio_obs × ε_eff = {f_GGE_required:.6e}")
print(f"  plan Python-verified       = 1.155e-4")
print()
# Assertion: plan's Python-verified value matches canonical-constants arithmetic
assert abs(f_GGE_required - 1.155e-4) / 1.155e-4 < 0.01, (
    f"plan target f_GGE_required={f_GGE_required:.6e} doesn't match 1.155e-4"
)


# ----------------------------------------------------------------------------
# Section 2 — Three independent f_GGE derivations (plan §10 step 4)
# ----------------------------------------------------------------------------
# Derivation A: plan's formula (1/Vol_SU3) · Σ_k |β_k|² ω_k, normalized by
#               ρ_substrate = M_KK^4 × Vol_SU3_Haar
# Source: W7-2 Parker integral ρ_Parker = (1/(4π²)) ∫ k³ |β|² dk = 8.2058e69 GeV^4
#         and Σ_k |β|² ω_k in Parker-like convention = 2 · (4π²) · ρ_Parker

# Load W7-2 Parker residue output (if available)
w7_2_npz = _HERE / "s85_w7_cc6_parker_residue.npz"
if w7_2_npz.exists():
    _d72 = np.load(w7_2_npz)
    rho_Parker_input = float(_d72["rho_Parker_total"])  # (local) GeV^4 from W7-2
    print(f"--- W7-2 Parker residue input ---")
    print(f"  ρ_Parker_total (from W7-2)  = {rho_Parker_input:.6e}  GeV^4")
    print()
else:
    rho_Parker_input = 8.2058e69  # (local) analytic fallback
    print(f"--- W7-2 Parker residue input (fallback analytic) ---")
    print(f"  ρ_Parker_total (fallback)   = {rho_Parker_input:.6e}  GeV^4")
    print()

# The Parker-like sum Σ_k |β|² ω_k integrates to 2·ρ_Parker in our convention
# (ρ_Parker = (1/2) ∫ d³k/(2π)³ · ω_k · |β_k|²; the sum Σ ≡ ∫ d³k/(2π)³ has the
# same measure but drops the 1/2 Parker-pair prefactor; so Σ_k |β|² ω_k = 2·ρ_Parker).
sum_beta_sq_omega = 2.0 * rho_Parker_input  # (local) GeV^4

# Derivation A — plan's formula, normalized by M_KK^4 × Vol_SU3_Haar
rho_substrate_natural = (M_KK_gravity ** 4) * Vol_SU3_Haar  # (local) GeV^4
f_GGE_derived_A = (1.0 / Vol_SU3_Haar) * sum_beta_sq_omega / rho_substrate_natural  # (local)
# = sum_beta_sq_omega / (Vol_SU3² × M_KK^4) = 2·ρ_Parker / (M_KK^4 · Vol_SU3²)

print("--- Derivation A: plan's formula (1/Vol_SU3)·Σ|β|²ω / (M_KK^4 × Vol_SU3) ---")
print(f"  Σ_k |β_k|² ω_k             = 2·ρ_Parker = {sum_beta_sq_omega:.6e}  GeV^4")
print(f"  ρ_substrate_natural       = M_KK^4 × Vol_SU3_Haar = {rho_substrate_natural:.6e}  GeV^4")
print(f"  f_GGE_derived_A           = {f_GGE_derived_A:.6e}")
print(f"  ratio_derived_A           = f_GGE_derived_A / ε_eff = {f_GGE_derived_A/eps_eff:.6e}")
print()

# Derivation B — direct Bogoliubov-occupancy normalization (S38 canonical)
# f_GGE_B ≡ n_Bog × (1 − Γ): substrate's Bogoliubov fraction times effacement residual.
# This tests the simplest substrate-inheritance hypothesis.
f_GGE_derived_B = n_Bog * eps_eff  # (local) S38 × S37
print("--- Derivation B: n_Bog × ε_eff (simplest substrate-inheritance) ---")
print(f"  n_Bog (S38)               = {n_Bog:.8f}")
print(f"  ε_eff                     = {eps_eff:.6e}")
print(f"  f_GGE_derived_B           = {f_GGE_derived_B:.6e}")
print(f"  ratio_derived_B           = f_GGE_derived_B / ε_eff = {f_GGE_derived_B/eps_eff:.6f} (= n_Bog)")
print()

# Derivation C — Omega-mapping inversion (plan step 3 self-consistency)
# If we impose ratio_derived = Ω_DM_obs / Ω_DE_obs and solve for f_GGE:
f_GGE_derived_C = ratio_obs_2020 * eps_eff  # (local) by construction = f_GGE_required
print("--- Derivation C: Omega-mapping inversion (self-consistent by construction) ---")
print(f"  f_GGE_derived_C           = Ω_DM_obs × ε_eff / Ω_DE_obs × ε_eff... wait, re-derive:")
print(f"                            = (Ω_DM_obs/Ω_DE_obs) × ε_eff = {f_GGE_derived_C:.6e}")
print(f"  ratio_derived_C           = by construction = {ratio_obs_2020:.6f}")
print()


# ----------------------------------------------------------------------------
# Section 3 — Gate verdicts for each derivation
# ----------------------------------------------------------------------------
def _verdict_for_ratio(ratio_derived: float, ratio_obs: float) -> tuple[str, float]:
    """Return (verdict, |residual/obs|) per plan §9."""
    residual = abs(ratio_derived - ratio_obs) / ratio_obs
    if residual <= tolerance_RATIO:
        return "PASS", residual
    elif residual <= FAIL_RATIO:
        return "INFO", residual
    else:
        return "FAIL", residual


ratio_A = f_GGE_derived_A / eps_eff  # (local)
ratio_B = f_GGE_derived_B / eps_eff  # (local)  = n_Bog
ratio_C = f_GGE_derived_C / eps_eff  # (local)  = ratio_obs_2020 (self-consistent)

verdict_A, res_A = _verdict_for_ratio(ratio_A, ratio_obs_2020)
verdict_B, res_B = _verdict_for_ratio(ratio_B, ratio_obs_2020)
verdict_C, res_C = _verdict_for_ratio(ratio_C, ratio_obs_2020)

print("--- Per-derivation verdicts (plan §9 AND-conjunction is over ONE ratio_derived) ---")
print(f"  [A] S50-formula-normalized: ratio_A={ratio_A:.4e}, residual={res_A:.3e}  →  {verdict_A}")
print(f"  [B] substrate-inheritance : ratio_B={ratio_B:.4f}, residual={res_B:.3e}  →  {verdict_B}")
print(f"  [C] Omega-mapping (tautological): ratio_C={ratio_C:.4f}, residual={res_C:.3e}  →  {verdict_C}")
print()

# The primary verdict is Derivation A (plan's explicit formula).
# Derivation C is self-consistent (tautological PASS by construction).
# Derivation B is a simple substrate-inheritance cross-check.
# Emit verdict based on A (the plan's primary microscopic derivation).
ratio_derived = ratio_A
verdict = verdict_A
residual = res_A

print("--- PRIMARY verdict (Derivation A — plan's S50 formula) ---")
print(f"  ratio_derived = {ratio_derived:.6e}")
print(f"  ratio_obs     = {ratio_obs_2020:.6f}")
print(f"  residual/obs  = {residual:.6e}")
print(f"  PASS threshold ≤ {tolerance_RATIO:.2f}; FAIL > {FAIL_RATIO:.2f}")
print(f"  VERDICT: {verdict}")
print()


# ----------------------------------------------------------------------------
# Section 4 — artifacts
# ----------------------------------------------------------------------------
npz_path = _HERE / "s85_w7_cc_gamma_dm_de_ratio.npz"
png_path = _HERE / "s85_w7_cc_gamma_dm_de_ratio.png"

np.savez(
    npz_path,
    # Primary
    ratio_derived=ratio_derived,
    ratio_obs=ratio_obs_2020,
    residual_RATIO=residual,
    # Derivations
    f_GGE_derived_A=f_GGE_derived_A,
    f_GGE_derived_B=f_GGE_derived_B,
    f_GGE_derived_C=f_GGE_derived_C,
    f_GGE_required=f_GGE_required,
    ratio_A=ratio_A,
    ratio_B=ratio_B,
    ratio_C=ratio_C,
    verdict_A=verdict_A,
    verdict_B=verdict_B,
    verdict_C=verdict_C,
    # Canonical pins
    Gamma_value=Gamma_effacement,
    f_GGE_value=f_GGE_derived_A,
    eps_eff=eps_eff,
    Omega_DM_obs=Omega_DM_obs,
    Omega_DE_obs=Omega_DE_obs,
    rho_substrate_natural=rho_substrate_natural,
    rho_Parker_input=rho_Parker_input,
    sum_beta_sq_omega=sum_beta_sq_omega,
    # Gate state
    verdict=verdict,
    tolerance_RATIO=tolerance_RATIO,
    FAIL_RATIO=FAIL_RATIO,
    # 4-tuple
    value=ratio_derived,
    scheme=scheme,
    convention=convention,
    L_max=L_max,
    # SHAs
    closure_sha=CLOSURE_SHA,
)

# Plot: bar chart observed vs three derived ratios
fig, ax = plt.subplots(figsize=(10, 6.2), dpi=130)
labels = [
    "Ω_DM/Ω_DE\n(Planck 2020 DR2)",
    "Derivation A\n(plan S50 formula)",
    "Derivation B\n(n_Bog × ε_eff / ε_eff\n= n_Bog)",
    "Derivation C\n(Ω-mapping\ntautology)",
]
values = [ratio_obs_2020, ratio_A, ratio_B, ratio_C]
colors = ["tab:blue", "tab:red", "tab:orange", "tab:green"]
verds = ["OBSERVED", verdict_A, verdict_B, verdict_C]
bars = ax.bar(labels, values, color=colors, alpha=0.8)
# Labels on bars
for bar, v, verd in zip(bars, values, verds):
    ax.text(
        bar.get_x() + bar.get_width() / 2.0,
        bar.get_height() * 1.05,
        f"{v:.3e}\n{verd}",
        ha="center",
        fontsize=9,
    )
# Tolerance bands
ax.axhline(
    ratio_obs_2020 * (1 + tolerance_RATIO),
    color="tab:green",
    ls="--",
    lw=1,
    alpha=0.5,
    label=f"PASS ±{100*tolerance_RATIO:.0f}%",
)
ax.axhline(ratio_obs_2020 * (1 - tolerance_RATIO), color="tab:green", ls="--", lw=1, alpha=0.5)
ax.axhline(
    ratio_obs_2020 * (1 + FAIL_RATIO),
    color="tab:red",
    ls=":",
    lw=1,
    alpha=0.5,
    label=f"FAIL ±{100*FAIL_RATIO:.0f}%",
)
ax.axhline(ratio_obs_2020 * (1 - FAIL_RATIO), color="tab:red", ls=":", lw=1, alpha=0.5)
ax.set_yscale("log")
ax.set_ylabel(r"$\Omega_{DM} / \Omega_{DE}$  (log scale)")
ax.set_title(
    f"S85-W7-3 CC-Γ — primary verdict (Derivation A): {verdict}\n"
    f"residual/obs = {residual:.3e}; observed = {ratio_obs_2020:.4f}"
)
ax.legend(loc="best", fontsize=9)
ax.grid(True, alpha=0.3, which="both", axis="y")
plt.tight_layout()
plt.savefig(png_path, dpi=130)
plt.close()

print("--- outputs ---")
print(f"  .npz: {npz_path.name} ({npz_path.stat().st_size} bytes)")
print(f"  .png: {png_path.name} ({png_path.stat().st_size} bytes)")
print()


# ----------------------------------------------------------------------------
# Section 5 — verdict append with S85+ dual-SHA
# ----------------------------------------------------------------------------
GATE_ID = "S85-W7-CC-GAMMA"
verdict_path = _HERE / "s85_gate_verdicts.txt"
content_sha = _file_sha(npz_path)
audit_sha = CLOSURE_SHA

value_str = f"{ratio_derived:.6e}"
canonical_line = (
    f"{GATE_ID}: {verdict} -- "
    f"value={value_str} scheme={scheme} convention={convention} "
    f"L_max={L_max} sha256={audit_sha}"
)
dual_sha_comment = (
    f"# {GATE_ID} dual-SHA: "
    f"content_sha256={content_sha} audit_sha256={audit_sha}"
)

with verdict_path.open("a", encoding="utf-8") as fh:
    fh.write(canonical_line + "\n")
    fh.write(dual_sha_comment + "\n")

print("--- verdict line appended ---")
print(f"  {canonical_line}")
print(f"  {dual_sha_comment}")
print()
print(
    f"FINAL 4-tuple: (value={value_str}, scheme={scheme}, "
    f"convention={convention}, L_max={L_max})"
)

sys.exit(0)
