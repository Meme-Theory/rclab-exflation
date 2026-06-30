"""
s84_w5_k_star_lab_framework_match.py — S84 W5-58

Gate: S84-K-STAR-LAB-FRAMEWORK-MATCH

Task: (a) functional-form audit of K_* = coth(x*) — which x* yields the numerical
anchor 1.313 quoted in the plan?  Direct evaluation settled offline:
  coth(0.5) = 2.1640   coth(1.0) = 1.3130
      ⇒ the plan-prose "coth(0.5) = 1.313" is inconsistent; 1.313 = coth(1).
(b) Compute K_*_lab from 3He-B lab ratio (Volovik 2003 Ch. 7 weak-coupling ≈ 1.76;
    measured 3He-B ≈ 1.96) under the substrate-native convention
      K = coth(Δ_BCS / (2 T_eff))
    (per `s83_w3_g39_leggett_bogoliubov.py`, confirmed via knowledge search).
    Under this convention the correct lab x* is
      x*_lab := Δ_3He / (2 k_B T_c) = (Δ/k_B T_c)/2 ∈ {1.76/2, 1.96/2} = {0.882, 0.98}.
(c) Compare K_*_lab to K_*_framework = 1.3130 (= coth(1)) and classify.

Pre-registered gate thresholds (§W5-58):
  PASS  : (a) x*=1 pinned AND (b) |K_lab-K_fw|/K_fw ≤ 0.10
  INFO  : 0.10 < ratio ≤ 0.30
  FAIL  : x* not pinned OR ratio > 0.30

SHA-256 pin: ordered input-pin map per `.claude/templates/script-template.py`.

Env: `phonon-exflation-sim/.venv312/Scripts/python.exe`
"""

from __future__ import annotations

import hashlib
import os
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from canonical_constants import (  # noqa: E402  (path set above)
    Delta_BCS,
    tau_fold,
)


# =============================================================================
# 1. Input pin map + closure SHA
# =============================================================================


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


INPUT_PINS: dict[str, str] = {
    "canonical_constants.py": _sha256_file(HERE / "canonical_constants.py"),
    # Volovik 2003 transcription file — pin the md file if present, else string hash.
}

volovik_md = HERE.parent / "researchers" / "Volovik" / "volovik-2003-universe-in-a-helium-droplet.md"
if volovik_md.exists():
    INPUT_PINS["volovik-2003-ch7-bcs-ratio"] = _sha256_file(volovik_md)
else:
    # Fallback: pin the Ch. 7 weak-coupling ratio as literal-string provenance
    INPUT_PINS["volovik-2003-ch7-bcs-ratio"] = hashlib.sha256(
        b"Volovik 2003 Ch. 7: Delta/k_B T_c = pi exp(-gamma_E) = 1.7639 (weak-coupling)"
    ).hexdigest()

# Prompt pin (captures the numerical anchor "1.313" under audit)
INPUT_PINS["prompt-anchor-K-star-1.313"] = hashlib.sha256(
    b"W5-58 prompt: K_* = coth(0.5) = 1.313  [AUDITED: coth(0.5)=2.1640; 1.313=coth(1)]"
).hexdigest()


def closure_sha256(pins: dict[str, str]) -> str:
    """Canonical closure = SHA256 of ordered 'name:hash\\n' map."""
    payload = "\n".join(f"{k}:{v}" for k, v in sorted(pins.items())).encode()
    return hashlib.sha256(payload).hexdigest()


CLOSURE_SHA = closure_sha256(INPUT_PINS)

print("=" * 72)
print("s84_w5_k_star_lab_framework_match.py — W5-58")
print("=" * 72)
print("Input SHA-256 pins:")
for name, sha in sorted(INPUT_PINS.items()):
    print(f"  {name}: {sha}")
print(f"Closure SHA-256: {CLOSURE_SHA}")
print("=" * 72)


# =============================================================================
# 2. Step 1 — definitions and numerical verification of coth
# =============================================================================


def coth(x: float | np.ndarray) -> float | np.ndarray:
    """coth(x) = (e^x + e^{-x}) / (e^x - e^{-x}) = 1/tanh(x)."""
    return 1.0 / np.tanh(x)


# Step 1 (definition): numerical verification anchors
coth_half = float(coth(0.5))    # (local)
coth_one = float(coth(1.0))     # (local)

print("\n[Step 1] coth numerical verification (substitution chain):")
print(f"  coth(0.5) = (e^0.5 + e^-0.5)/(e^0.5 - e^-0.5) = {coth_half:.4f}")
print(f"  coth(1.0) = (e   + e^-1  )/(e   - e^-1  )   = {coth_one:.4f}")
print(f"  Plan-prose anchor  K_* = 1.313  ⇒  x* must satisfy coth(x*) = 1.313")
print(f"  x* = arccoth(1.313) = 0.5 * ln((1.313+1)/(1.313-1)) "
      f"= {0.5*np.log((1.313+1)/(1.313-1)):.4f}")
print("  ⇒  x* = 1 (NOT 0.5).  Plan prose 'coth(0.5) = 1.313' is a TYPO;")
print("     numerical anchor 1.313 is consistent with coth(1).")


# =============================================================================
# 3. Step 2 — candidate x* from substrate-structural parameters
# =============================================================================

# Candidate x* values (pre-registered set from plan §W5-58 scan_range)
x_candidates = {
    "x*=0.5 (plan-prose reading)":       0.5,
    "x*=1.0 (plan-numeric reading)":     1.0,
    "x*=2*tau_fold":                     2.0 * tau_fold,          # (local)
    "x*=1/Delta_BCS":                    1.0 / Delta_BCS,          # (local)
}

print("\n[Step 2] Framework K_*_fw = coth(x*) for candidate x*:")
K_fw_of_candidate: dict[str, float] = {}
for label, xv in x_candidates.items():
    K_fw = float(coth(xv))
    K_fw_of_candidate[label] = K_fw
    print(f"  {label:35s}  x*={xv:.4f}  ⇒  K_fw = coth(x*) = {K_fw:.4f}")

# Pin x* = 1 as substrate-native (matches prompt numerical anchor 1.313)
x_star_framework = 1.0                          # (local, pinned by Step 2 audit)
K_star_framework = float(coth(x_star_framework))    # (local) = 1.3130
print(f"\n  PINNED:  x*_framework = {x_star_framework:.4f}  "
      f"⇒  K_*_framework = {K_star_framework:.4f}")


# =============================================================================
# 4. Step 3 — lab 3He-B K_*_lab from Volovik 2003 Ch. 7
# =============================================================================
#
# Volovik 2003 Ch. 7 weak-coupling BCS:  Δ(0)/(k_B T_c) = π e^{-γ_E} ≈ 1.7639
# Measured 3He-B (p-wave, strong-coupling enhanced):     Δ/(k_B T_c) ≈ 1.96
#
# Substrate-native convention (from `s83_w3_g39_leggett_bogoliubov.py`):
#     K = coth( Δ_BCS / (2 T_eff) )
# so the x for lab eval at T = T_c is:
#     x_lab = Δ_3He / (2 k_B T_c)  =  (Δ/k_B T_c) / 2

ratio_weak_coupling = 1.7639         # (local) Volovik Ch. 7 πe^{-γ_E} analytic result
ratio_measured_3HeB = 1.96           # (local) Volovik Ch. 7 p-wave measured

# Convention A: x* = Δ/(2 k_B T_c)  — the Leggett-Bogoliubov substrate-native form.
x_lab_A_wc = ratio_weak_coupling / 2.0          # (local)
x_lab_A_me = ratio_measured_3HeB / 2.0          # (local)
K_lab_A_wc = float(coth(x_lab_A_wc))            # (local)
K_lab_A_me = float(coth(x_lab_A_me))            # (local)

# Convention B: x* = Δ/(k_B T_c)  — used for completeness (audit).
x_lab_B_wc = ratio_weak_coupling                # (local)
x_lab_B_me = ratio_measured_3HeB                # (local)
K_lab_B_wc = float(coth(x_lab_B_wc))            # (local)
K_lab_B_me = float(coth(x_lab_B_me))            # (local)

print("\n[Step 3] Lab 3He-B K_*_lab (Volovik 2003 Ch. 7):")
print(f"  weak-coupling Δ/k_BT_c ≈ 1.7639 (analytic πe^-γE)")
print(f"  measured 3He-B Δ/k_BT_c ≈ 1.96 (strong-coupling enhanced)")
print()
print("  Convention A: x_lab = Δ/(2 k_B T_c)  [substrate-native — matches"
      " s83_w3_g39 K = coth(Δ/(2 T_eff))]")
print(f"     weak-coupling:  x={x_lab_A_wc:.4f}  K_lab = {K_lab_A_wc:.4f}")
print(f"     measured:       x={x_lab_A_me:.4f}  K_lab = {K_lab_A_me:.4f}")
print("  Convention B: x_lab = Δ/(k_B T_c)  [audit only]")
print(f"     weak-coupling:  x={x_lab_B_wc:.4f}  K_lab = {K_lab_B_wc:.4f}")
print(f"     measured:       x={x_lab_B_me:.4f}  K_lab = {K_lab_B_me:.4f}")


# =============================================================================
# 5. Step 4 — pre-registered ratio + gate verdict
# =============================================================================

def abs_rel(K_lab: float, K_fw: float) -> float:
    """|K_lab - K_fw| / K_fw — plan-pre-registered PASS/FAIL metric."""
    return abs(K_lab - K_fw) / K_fw

# Primary comparison: Convention A (substrate-native) with measured 3He-B.
ratio_primary = abs_rel(K_lab_A_me, K_star_framework)   # (local)

# Cross-compare: Convention A weak-coupling (analytic Volovik limit)
ratio_wc_A = abs_rel(K_lab_A_wc, K_star_framework)      # (local)

# Audit-only (Convention B)
ratio_B_me = abs_rel(K_lab_B_me, K_star_framework)      # (local)
ratio_B_wc = abs_rel(K_lab_B_wc, K_star_framework)      # (local)

print("\n[Step 4] Pre-registered metric |K_lab - K_fw| / K_fw:")
print(f"  K_fw = {K_star_framework:.4f}  (coth(1), pinned)")
print(f"  PRIMARY — Conv.A + measured 3He-B:    K_lab = {K_lab_A_me:.4f}  "
      f"ratio = {ratio_primary:.4f}  ({ratio_primary*100:.2f}%)")
print(f"  Cross  — Conv.A + weak-coupling:      K_lab = {K_lab_A_wc:.4f}  "
      f"ratio = {ratio_wc_A:.4f}  ({ratio_wc_A*100:.2f}%)")
print(f"  Audit  — Conv.B + measured 3He-B:     K_lab = {K_lab_B_me:.4f}  "
      f"ratio = {ratio_B_me:.4f}  ({ratio_B_me*100:.2f}%)")
print(f"  Audit  — Conv.B + weak-coupling:      K_lab = {K_lab_B_wc:.4f}  "
      f"ratio = {ratio_B_wc:.4f}  ({ratio_B_wc*100:.2f}%)")


# ---- gate classification ----
def classify(ratio: float) -> str:
    """PASS if ratio ≤ 0.10, INFO if 0.10 < ratio ≤ 0.30, FAIL if > 0.30."""
    if ratio <= 0.10:
        return "PASS"
    if ratio <= 0.30:
        return "INFO"
    return "FAIL"


verdict_primary = classify(ratio_primary)
value = ratio_primary   # (local) — the pre-registered output value

print("\n" + "=" * 72)
print(f"VERDICT (primary metric, Convention A + measured 3He-B):  {verdict_primary}")
print(f"  value = |K_lab - K_fw|/K_fw = {value:.6f}  ({value*100:.2f}%)")
print(f"  K_*_framework = coth(1) = {K_star_framework:.4f}   (x* PINNED)")
print(f"  K_*_lab       = coth(Δ/(2 k_B T_c)) "
      f"= coth(0.98) = {K_lab_A_me:.4f}  [measured 3He-B]")
print("=" * 72)


# =============================================================================
# 6. Plot — K_* candidates + lab value + 10% band
# =============================================================================

fig, ax = plt.subplots(figsize=(9, 5.5))

# Framework candidate K_fw values
labels_fw = list(x_candidates.keys())
K_vals_fw = [K_fw_of_candidate[l] for l in labels_fw]
x_positions = np.arange(len(labels_fw))

colors = ["#1f77b4", "#2ca02c", "#9467bd", "#8c564b"]
for i, (lbl, K, xv) in enumerate(zip(labels_fw, K_vals_fw,
                                     [x_candidates[l] for l in labels_fw])):
    ax.scatter(x_positions[i], K, s=120, c=colors[i], zorder=3,
               label=f"{lbl} → K={K:.4f}")

# Lab values
ax.axhline(K_lab_A_me, color="crimson", ls="-", lw=2,
           label=f"K_lab (Conv.A, measured 3He-B, Δ/k_BT_c=1.96) = {K_lab_A_me:.4f}")
ax.axhline(K_lab_A_wc, color="crimson", ls="--", lw=1.5, alpha=0.7,
           label=f"K_lab (Conv.A, weak-coupling, Δ/k_BT_c=1.7639) = {K_lab_A_wc:.4f}")

# 10% band around K_*_framework = coth(1)
ax.axhspan(K_star_framework * 0.90, K_star_framework * 1.10,
           color="gold", alpha=0.25, label="±10% band around K_fw=coth(1)")
ax.axhline(K_star_framework, color="black", ls=":", lw=1.5,
           label=f"K_*_framework = coth(1) = {K_star_framework:.4f}  [PINNED]")

ax.set_xticks(x_positions)
ax.set_xticklabels([l.split(" (")[0] for l in labels_fw], rotation=15, ha="right")
ax.set_ylabel("K_* = coth(x*)")
ax.set_title(f"W5-58 K-STAR-LAB-FRAMEWORK-MATCH — VERDICT: {verdict_primary}\n"
             f"ratio (primary) = {ratio_primary:.4f} ({ratio_primary*100:.2f}%),"
             f" threshold 10% PASS / 30% FAIL")
ax.legend(fontsize=8, loc="upper right")
ax.set_ylim(0.9, max(K_vals_fw) * 1.05)
ax.grid(True, alpha=0.3)

out_plot = HERE / "s84_w5_58_plot.png"
fig.tight_layout()
fig.savefig(out_plot, dpi=140)
plt.close(fig)
print(f"Plot saved: {out_plot}")


# =============================================================================
# 7. Data dump + verdict 4-tuple
# =============================================================================

out_npz = HERE / "s84_w5_58_data.npz"
np.savez(
    out_npz,
    # coth verification
    coth_half=coth_half,
    coth_one=coth_one,
    # candidate x* scan
    x_candidate_labels=np.array(list(x_candidates.keys()), dtype=object),
    x_candidate_values=np.array(list(x_candidates.values())),
    K_fw_candidates=np.array([K_fw_of_candidate[k] for k in x_candidates.keys()]),
    # pinned framework
    x_star_framework=x_star_framework,
    K_star_framework=K_star_framework,
    # lab (Convention A, substrate-native)
    x_lab_A_wc=x_lab_A_wc,
    x_lab_A_me=x_lab_A_me,
    K_lab_A_wc=K_lab_A_wc,
    K_lab_A_me=K_lab_A_me,
    # audit (Convention B)
    x_lab_B_wc=x_lab_B_wc,
    x_lab_B_me=x_lab_B_me,
    K_lab_B_wc=K_lab_B_wc,
    K_lab_B_me=K_lab_B_me,
    # ratios
    ratio_primary=ratio_primary,
    ratio_wc_A=ratio_wc_A,
    ratio_B_me=ratio_B_me,
    ratio_B_wc=ratio_B_wc,
    # closure
    closure_sha=CLOSURE_SHA,
    verdict=verdict_primary,
    # lab inputs
    ratio_weak_coupling_Volovik_Ch7=ratio_weak_coupling,
    ratio_measured_3HeB=ratio_measured_3HeB,
)
print(f"Data saved: {out_npz}")


# =============================================================================
# 8. Output 4-tuple (final non-verdict line) + verdict line
# =============================================================================

tuple_line = (
    f"(value={value:.6f}, scheme=coth, convention=Volovik-3HeB, L_max=N/A)"
)
print("\nExpected output 4-tuple:")
print(f"  {tuple_line}")

verdict_line = (
    f"W5-58: {verdict_primary} -- value={value:.6f} "
    f"scheme=coth convention=Volovik-3HeB L_max=N/A "
    f"sha256={CLOSURE_SHA}"
)
print("\nVERDICT LINE:")
print(f"  {verdict_line}")

# Append to verdict file (session directory)
verdict_file = HERE.parent / "sessions" / "session-84" / "s84_gate_verdicts.txt"
if verdict_file.parent.exists():
    with open(verdict_file, "a", encoding="utf-8") as fh:
        fh.write(verdict_line + "\n")
    print(f"Verdict appended to: {verdict_file}")
else:
    # fallback: computations/_shared/
    fallback = HERE / "s84_gate_verdicts.txt"
    with open(fallback, "a", encoding="utf-8") as fh:
        fh.write(verdict_line + "\n")
    print(f"Verdict appended to fallback: {fallback}")
