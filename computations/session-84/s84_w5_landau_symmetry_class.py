"""
s84_w5_landau_symmetry_class.py

W5-66 GATE-LANDAU-SYMMETRY-CLASS: Landau symmetry-classification of the K-corridor.

Method (analytical, representation-theoretic):
  1) Enumerate the substrate symmetry group G (unbroken at K -> infinity).
  2) Identify the residual stabilizer H under K-finite band-weighting B1/B2/B3 = {3,3,2}.
  3) Compute dim(G/H) = N_OP (full coset) and compare with 3He-B N_OP = 5
     (Volovik 2003 Ch. 7: SO(3)_L x SO(3)_S x U(1)/SO(3)_{L+S} + gap modulus).
  4) Identify AZ universality class (BDI, AIII, ...) via (T^2, C^2, S^2)
     per framework-constants.md (T^2 = +1 forced by PH symmetry, mu = 0).
  5) Incorporate sub-wave-A feeds:
       - W5-55 FAIL: K_crit = K_anchor/eps_anchor = 91.543 splits corridor
         into inflationary (1D Landau) and kinetic-dominated (OFF-manifold).
       - W5-58 PASS: K_*_framework = coth(1) = 1.3130 matches 3He-B lab at 1.13%.
       - W5-56 FAIL (R4): formula-level, NOT universality-class level -> BDI holds.
       - W5-54 FAIL (scheme): K itself is regulator-dependent; OP coordinate
         is NOT scheme-invariant.

Verdict logic:
  PASS  : N_OP_framework == N_OP_3HeB == 5  AND  AZ class == BDI  AND  1D corridor monotone.
  INFO  : G/H identified, AZ class = BDI inherited, but N_OP != 5 OR corridor
          multi-valued (K_crit split).
  FAIL  : No consistent G/H exists, or AZ class not BDI.

Expected outcome: INFO (N_OP = 8, not 5; multi-valued across K_crit).

Canonical constants: K_anchor = 2.035, eps_anchor_PS = 0.02223 (from W5-55),
K_star = 1.3130 = coth(1).

Author: landau-condensed-matter-theorist (S84 W5-66)
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

import numpy as np

# Canonical constants (S84+ mandatory import)
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (  # noqa: E402
    K_star,
    M_KK,
    Delta_BCS,
    tau_fold,
)

# ============================================================================
# Section 1. SHA-256 input-pin map and closure hash
# ============================================================================

INPUT_PINS = {
    # Static files (hashed at runtime)
    "canonical_constants.py": Path(__file__).parent / "canonical_constants.py",
    "volovik_26_3HeB_BDI": Path(__file__).parent.parent
        / "researchers" / "Volovik" / "26_2009_Volovik_3He_B_Topological_BDI.md",
    "volovik_10_topological_superfluids": Path(__file__).parent.parent
        / "researchers" / "Volovik" / "10_2019_Volovik_Topological_Superfluids.md",
    "landau_synthesis_s83": Path(__file__).parent.parent
        / "sessions" / "session-83" / "session-83-landau-synthesis.md",
    "framework_constants_memory": Path(__file__).parent.parent
        / ".claude" / "agent-memory" / "landau-condensed-matter-theorist"
        / "framework-constants.md",
    "w5_58_k_star_match": Path(__file__).parent.parent
        / ".claude" / "agent-memory" / "volovik-superfluid-universe-theorist"
        / "w5-58-k-star-lab-match-84.md",
    "framework_3heb_comparison": Path(__file__).parent.parent
        / ".claude" / "agent-memory" / "volovik-superfluid-universe-theorist"
        / "framework-3heb-comparison.md",
}


def sha256_of_file(p: Path) -> str:
    h = hashlib.sha256()
    if p.exists():
        with p.open("rb") as f:
            for block in iter(lambda: f.read(65536), b""):
                h.update(block)
    else:
        h.update(f"MISSING:{p}".encode())
    return h.hexdigest()


INPUT_SHAS = {k: sha256_of_file(v) for k, v in INPUT_PINS.items()}

print("=" * 78)
print("S84 W5-66 GATE-LANDAU-SYMMETRY-CLASS -- Input pin map (SHA-256)")
print("=" * 78)
for k, v in INPUT_SHAS.items():
    print(f"  {k:40s} : {v}")
print("-" * 78)

# ============================================================================
# Section 2. Group-theoretic data
# ============================================================================

# Dimensions of compact Lie groups (standard)
DIM = {
    "SU(3)": 8,
    "SU(2)": 3,
    "U(1)": 1,
    "SO(3)": 3,
    "SO(2)": 1,
    "Z_2": 0,   # discrete, dim 0
    "Z_6": 0,   # discrete, dim 0
    "T": 0,     # time-reversal, discrete, dim 0
    "R_dil": 1, # R-dilation (K-axis)
}


@dataclass
class GroupFactor:
    name: str
    dim: int
    is_discrete: bool = False


@dataclass
class Coset:
    G_factors: list
    H_factors: list
    label: str

    def dim_G(self) -> int:
        return sum(f.dim for f in self.G_factors)

    def dim_H(self) -> int:
        return sum(f.dim for f in self.H_factors)

    def dim_quotient(self) -> int:
        return self.dim_G() - self.dim_H()


# ----------------------------------------------------------------------------
# Framework substrate G at K -> infinity (single-mode fine-structure limit)
# ----------------------------------------------------------------------------
# Per framework-constants.md:
#   - Internal SU(3) gauge (D_K on SU(3), group manifold)
#   - SO(3) rotations in the 8-mode fiber (occupation rotation symmetry)
#   - U(1)_rel relative phase between Leggett bands (two-band symmetry)
#   - T (time-reversal), T^2 = +1, BDI class
# ----------------------------------------------------------------------------
G_framework = [
    GroupFactor("SU(3)", DIM["SU(3)"]),
    GroupFactor("SO(3)", DIM["SO(3)"]),
    GroupFactor("U(1)_rel", DIM["U(1)"]),
    GroupFactor("T", DIM["T"], is_discrete=True),
]

# ----------------------------------------------------------------------------
# Framework residual H at finite K (K-weighted GGE state)
# ----------------------------------------------------------------------------
# Per framework-constants.md + S43 band multiplicities {3,3,2}:
#   - SU(3) -> SU(2) x U(1) residual (stabilizer of 3/3/2 weight pattern;
#     diagonal Cartan picked out by band multiplicity breaking)
#   - SO(3) -> SO(2) axial (stabilizer of the K-axis in occupation space)
#   - U(1)_rel -> Z_2 relative-phase lock (per S82 W2-11: s++ / s+- = Z_2 gauge)
#   - T preserved (BDI forced by PH, framework-constants.md #5)
# ----------------------------------------------------------------------------
H_framework = [
    GroupFactor("SU(2)", DIM["SU(2)"]),
    GroupFactor("U(1)", DIM["U(1)"]),
    GroupFactor("SO(2)", DIM["SO(2)"]),
    GroupFactor("Z_2", DIM["Z_2"], is_discrete=True),
    GroupFactor("T", DIM["T"], is_discrete=True),
]

framework_coset = Coset(G_framework, H_framework, "framework K-corridor G/H")

# ----------------------------------------------------------------------------
# 3He-B reference (Volovik 2003 Ch. 7; Leggett 1975)
# ----------------------------------------------------------------------------
# G_3HeB = SO(3)_L x SO(3)_S x U(1)_phi x T
#   (orbital rotation, spin rotation, U(1) gauge, time-reversal)
# H_3HeB = SO(3)_{L+S} x Z_2 x T
#   (diagonal locked rotation J = L + S -- the celebrated "broken relative
#    spin-orbit rotation" pattern of 3He-B; residual Z_2 phase)
# dim_OP_3HeB_coset = 3+3+1 - 3 = 4
# Plus 1 for gap modulus |Delta| (gauge-invariant magnitude) = 5 total components.
# ----------------------------------------------------------------------------
G_3HeB = [
    GroupFactor("SO(3)_L", DIM["SO(3)"]),
    GroupFactor("SO(3)_S", DIM["SO(3)"]),
    GroupFactor("U(1)_phi", DIM["U(1)"]),
    GroupFactor("T", DIM["T"], is_discrete=True),
]
H_3HeB = [
    GroupFactor("SO(3)_{L+S}", DIM["SO(3)"]),
    GroupFactor("Z_2", DIM["Z_2"], is_discrete=True),
    GroupFactor("T", DIM["T"], is_discrete=True),
]
coset_3HeB = Coset(G_3HeB, H_3HeB, "3He-B G/H (Volovik 2003 Ch. 7)")

# ============================================================================
# Section 3. Compute G/H decomposition + N_OP
# ============================================================================

# Framework decomposition -- broken directions:
# SU(3)/(SU(2)xU(1)) : 4 (Grassmannian Gr(1,3) = CP^2)
# SO(3)/SO(2)        : 2 (S^2 unit sphere)
# U(1)_rel/Z_2       : 1 (continuous relative phase)
# K-dilation axis    : 1 (gap modulus / OP magnitude)

framework_components = {
    "SU(3)/(SU(2)xU(1))":  DIM["SU(3)"] - DIM["SU(2)"] - DIM["U(1)"],   # 4
    "SO(3)/SO(2)":         DIM["SO(3)"] - DIM["SO(2)"],                 # 2
    "U(1)_rel/Z_2":        DIM["U(1)"],                                 # 1
    "K-dilation axis":     1,                                            # 1
}
N_framework = sum(framework_components.values())

heb_components = {
    "SO(3)_L x SO(3)_S / SO(3)_{L+S}": (DIM["SO(3)"] + DIM["SO(3)"])
                                       - DIM["SO(3)"],                  # 3
    "U(1)_phi / Z_2":                  DIM["U(1)"],                      # 1
    "Gap modulus |Delta|":             1,                                # 1
}
N_3HeB = sum(heb_components.values())

print()
print("Section 3. Framework G/H decomposition")
print("-" * 78)
print(f"G_framework = SU(3) x SO(3) x U(1)_rel x T, dim_G = "
      f"{framework_coset.dim_G()}")
print(f"H_framework = SU(2) x U(1) x SO(2) x Z_2 x T, dim_H = "
      f"{framework_coset.dim_H()}")
print(f"dim(G/H)_framework = {framework_coset.dim_quotient()}")
for k, v in framework_components.items():
    print(f"    {k:40s} : dim = {v}")
print(f"  TOTAL N_OP_framework = {N_framework}")

print()
print("Section 3b. 3He-B reference G/H decomposition (Volovik 2003 Ch. 7)")
print("-" * 78)
print(f"G_3HeB = SO(3)_L x SO(3)_S x U(1)_phi x T, dim_G = "
      f"{coset_3HeB.dim_G()}")
print(f"H_3HeB = SO(3)_{{L+S}} x Z_2 x T, dim_H = {coset_3HeB.dim_H()}")
print(f"dim(G/H)_3HeB = {coset_3HeB.dim_quotient()}")
for k, v in heb_components.items():
    print(f"    {k:40s} : dim = {v}")
print(f"  TOTAL N_OP_3HeB = {N_3HeB}")

# ============================================================================
# Section 4. AZ universality class (BDI check)
# ============================================================================
# BDI: T^2 = +1, C^2 = +1, S = T*C present (chiral)
# Framework AZ class: BDI (framework-constants.md #5: [iK_7, D_K] = 0,
# #6: mu = 0 forced by PH symmetry)
# 3He-B AZ class: DIII in the textbook classification (Ryu-Schnyder-Ludwig)
#   BUT per Volovik 2003 Ch. 7 + Volovik 2009 paper #26: the d-vector structure
#   and BDI label apply on particular submanifolds; see framework-3heb-comparison.md
#   which identifies topology inheritance as BDI at the algebraic level.

AZ_class_framework = "BDI"            # T^2 = +1, C^2 = +1, S present
AZ_T2_framework = +1
AZ_C2_framework = +1
AZ_S_framework = True

# 3He-B canonical AZ is DIII (T^2 = -1, C^2 = +1, S present), but the framework
# inherits the BDI submanifold structure via the Jensen deformation + PH forcing
# mu = 0 (framework-constants.md #6); this is the "inheritance-hybrid" per S79
# P3-A workshop -- topology is 3He-B, AZ class is framework-unique BDI.
AZ_class_3HeB = "DIII"
AZ_T2_3HeB = -1  # (local)

AZ_match = (AZ_class_framework == AZ_class_3HeB)
print()
print("Section 4. AZ universality class check")
print("-" * 78)
print(f"AZ class framework = {AZ_class_framework}, (T^2, C^2, S) = "
      f"({AZ_T2_framework}, {AZ_C2_framework}, {AZ_S_framework})")
print(f"AZ class 3He-B canonical = {AZ_class_3HeB} (T^2 = {AZ_T2_3HeB})")
print(f"AZ class identity match: {AZ_match}")
print("  -> Inheritance is HYBRID: topology BDI-label shared (framework's BDI "
      "via PH-forced mu=0), but textbook 3He-B AZ is DIII.")

# ============================================================================
# Section 5. Multi-valued OP test (W5-55 feed: K_crit = 91.5)
# ============================================================================
K_anchor = 2.035  # (local)  -- PS-SUBSTRATE-MATCHED-IC canonical; S82 W2-4
eps_anchor = 0.02223  # (local)  -- (1 - n_s)/(1 + n_s) at W2-4 pivot; W5-55 calibration
K_crit = K_anchor / eps_anchor
corridor_samples = [1.1, 2.035, 10.0, 100.0, 1000.0, 3.556e5]
inflationary = [K for K in corridor_samples if K < K_crit]
kinetic = [K for K in corridor_samples if K >= K_crit]
is_single_valued = len(kinetic) == 0   # False -> corridor is multi-valued

print()
print("Section 5. Corridor multi-valuedness (W5-55 feed)")
print("-" * 78)
print(f"K_crit = K_anchor / eps_anchor = {K_anchor}/{eps_anchor} = {K_crit:.3f}")
print(f"Inflationary sub-corridor (1D Landau-valid) : {inflationary}")
print(f"Kinetic-dominated sub-corridor (OFF-manifold): {kinetic}")
print(f"Single-valued 1D OP? {is_single_valued}")

# ============================================================================
# Section 6. K_star lab match (W5-58 PASS feed)
# ============================================================================
K_star_computed = 1.0 / math.tanh(1.0)  # coth(1)
K_star_lab_3HeB = 1.0 / math.tanh(0.98)  # Measured 3He-B Delta/(k_B T_c) = 1.96
ratio_k_star = abs(K_star_lab_3HeB - K_star_computed) / K_star_computed

print()
print("Section 6. K_star match (W5-58 PASS feed)")
print("-" * 78)
print(f"K_star_framework = coth(1) = {K_star_computed:.6f}")
print(f"K_star_lab_3HeB = coth(Delta/(2 k_B T_c)) = coth(0.98) "
      f"= {K_star_lab_3HeB:.6f}")
print(f"ratio = {ratio_k_star:.6f} (PASS at 1.13%, 9x margin under 10% tol)")
print(f"canonical_constants K_star = {K_star}")
print(f"internal self-check |K_star - coth(1)| = "
      f"{abs(K_star - K_star_computed):.2e}")

# ============================================================================
# Section 7. Regulator-dependence (W5-54 FAIL feed)
# ============================================================================
# K under Zubarev at R5: 32.40; K under zeta at R5: 0.6366 -> ratio ~50x.
# The OP coordinate K is NOT scheme-invariant. OP is a Landau-valid
# coordinate, but the *mapping* K(scheme) is regulator-frame-dependent.
K_Zubarev = 32.4021  # (local)  -- from W5-54 verdict line
K_zeta = 0.6366  # (local)  -- from W5-54 verdict line
K_scheme_span_oom = math.log10(K_Zubarev / K_zeta)

print()
print("Section 7. Regulator-frame dependence of K (W5-54 FAIL feed)")
print("-" * 78)
print(f"K_R5_Zubarev = {K_Zubarev:.4f}; K_R5_zeta = {K_zeta:.4f}; "
      f"span = 10^{K_scheme_span_oom:.2f}")
print(f"K is regulator-dependent -> the G/H decomposition classifies the "
      f"substrate-native convention only.")

# ============================================================================
# Section 8. Verdict
# ============================================================================
N_MATCH = (N_framework == N_3HeB)          # 8 == 5 ? No.
CLASS_MATCH = (AZ_class_framework == AZ_class_3HeB)
# PASS conditions (pre-registered):
PASS = (N_MATCH and CLASS_MATCH and is_single_valued)
# FAIL conditions:
FAIL_NO_GH = False  # G/H decomposition was constructed cleanly
FAIL_CLASS = False  # BDI label applies to the framework (even if 3He-B is DIII)
# INFO conditions:
INFO = (not PASS) and (not FAIL_NO_GH) and (not FAIL_CLASS)

if PASS:
    verdict = "PASS"
elif FAIL_NO_GH or FAIL_CLASS:
    verdict = "FAIL"
else:
    verdict = "INFO"

print()
print("Section 8. Verdict")
print("-" * 78)
print(f"N_framework = {N_framework}, N_3HeB = {N_3HeB}, match? {N_MATCH}")
print(f"AZ class framework = {AZ_class_framework}, 3He-B = {AZ_class_3HeB}; "
      f"match? {CLASS_MATCH}")
print(f"Single-valued 1D OP? {is_single_valued} "
      f"(FALSE across full corridor; TRUE on inflationary sub-corridor)")
print(f"VERDICT: {verdict}")

# ============================================================================
# Section 9. Output 4-tuple
# ============================================================================
G_symbol = "SU(3) x SO(3) x U(1)_rel x T"
H_symbol = "SU(2) x U(1) x SO(2) x Z_2 x T"
N_OP = N_framework
az_class = AZ_class_framework
value_tuple_str = (f"({G_symbol} | {H_symbol} | N_OP={N_OP} | class={az_class} | "
                   f"N_match={N_MATCH} | corridor_1D={is_single_valued})")

print()
print(f"4-tuple: value={value_tuple_str} scheme=Landau-Ginzburg "
      f"convention=Volovik-2003-Ch7 L_max=N/A")

# ============================================================================
# Section 10. Closure SHA (ordered input-pin map)
# ============================================================================
closure_src = json.dumps(
    {
        "pins": INPUT_SHAS,
        "value": value_tuple_str,
        "verdict": verdict,
        "scheme": "Landau-Ginzburg",
        "convention": "Volovik-2003-Ch7",
        "N_framework": N_framework,
        "N_3HeB": N_3HeB,
        "AZ_framework": AZ_class_framework,
        "AZ_3HeB": AZ_class_3HeB,
        "K_crit": K_crit,
        "K_star_computed": K_star_computed,
        "ratio_K_star_lab": ratio_k_star,
        "is_single_valued_1D": is_single_valued,
    },
    sort_keys=True,
).encode()
closure_sha = hashlib.sha256(closure_src).hexdigest()

print()
print("Closure SHA-256 (ordered input-pin map + verdict):")
print(f"  {closure_sha}")

# ============================================================================
# Section 11. Persist NPZ data
# ============================================================================
out_dir = Path(__file__).parent
npz_path = out_dir / "s84_w5_66_data.npz"

np.savez(
    npz_path,
    # String fields (kept as numpy arrays of length-1)
    G_symbol=np.array(G_symbol),
    H_symbol=np.array(H_symbol),
    G_symbol_3HeB=np.array("SO(3)_L x SO(3)_S x U(1)_phi x T"),
    H_symbol_3HeB=np.array("SO(3)_{L+S} x Z_2 x T"),
    AZ_class_framework=np.array(AZ_class_framework),
    AZ_class_3HeB=np.array(AZ_class_3HeB),
    verdict=np.array(verdict),
    # Numeric fields
    N_OP_framework=N_framework,
    N_OP_3HeB=N_3HeB,
    dim_G_framework=framework_coset.dim_G(),
    dim_H_framework=framework_coset.dim_H(),
    dim_G_3HeB=coset_3HeB.dim_G(),
    dim_H_3HeB=coset_3HeB.dim_H(),
    K_anchor=K_anchor,
    eps_anchor=eps_anchor,
    K_crit=K_crit,
    K_star_computed=K_star_computed,
    K_star_lab_3HeB=K_star_lab_3HeB,
    ratio_K_star=ratio_k_star,
    K_R5_Zubarev=K_Zubarev,
    K_R5_zeta=K_zeta,
    K_scheme_span_oom=K_scheme_span_oom,
    is_single_valued_1D=int(is_single_valued),
    AZ_T2_framework=AZ_T2_framework,
    AZ_T2_3HeB=AZ_T2_3HeB,
    N_MATCH=int(N_MATCH),
    CLASS_MATCH=int(CLASS_MATCH),
    framework_component_dims=np.array(list(framework_components.values())),
    heb_component_dims=np.array(list(heb_components.values())),
    closure_sha=np.array(closure_sha),
)
print(f"\nData written to: {npz_path}")

# ============================================================================
# Section 12. Plot G/H decomposition diagram
# ============================================================================
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

fig, axs = plt.subplots(1, 2, figsize=(14, 6.5))

# Panel A: stacked bar -- framework G/H vs 3He-B G/H
ax = axs[0]
fw_labels = list(framework_components.keys())
fw_dims = list(framework_components.values())
heb_labels = list(heb_components.keys())
heb_dims = list(heb_components.values())

colors_fw = ["#2E86AB", "#A23B72", "#F18F01", "#C73E1D"]
colors_heb = ["#6A994E", "#BC4749", "#386641"]

x = [0, 1]
bottom_fw = 0  # (local)
for d, lbl, col in zip(fw_dims, fw_labels, colors_fw):
    ax.bar(0, d, bottom=bottom_fw, color=col, edgecolor="black",
           label=f"FW: {lbl} ({d})")
    ax.text(0, bottom_fw + d / 2, f"{lbl}\ndim={d}", ha="center", va="center",
            fontsize=8, color="white" if d > 1 else "black")
    bottom_fw += d

bottom_heb = 0  # (local)
for d, lbl, col in zip(heb_dims, heb_labels, colors_heb):
    ax.bar(1, d, bottom=bottom_heb, color=col, edgecolor="black",
           label=f"3He-B: {lbl} ({d})")
    ax.text(1, bottom_heb + d / 2, f"{lbl}\ndim={d}", ha="center", va="center",
            fontsize=8, color="white" if d > 1 else "black")
    bottom_heb += d

ax.set_xticks([0, 1])
ax.set_xticklabels([f"Framework\nN_OP = {N_framework}",
                    f"3He-B\nN_OP = {N_3HeB}"], fontsize=11)
ax.set_ylabel("dim(G/H) broken directions", fontsize=11)
ax.set_title("W5-66: G/H decomposition comparison\n"
             "(framework K-corridor vs 3He-B parent)", fontsize=11)
ax.axhline(N_3HeB, color="red", linestyle="--", alpha=0.6,
           label=f"3He-B N_OP = {N_3HeB} reference")
ax.grid(True, alpha=0.3, axis="y")
ax.set_ylim(0, max(N_framework, N_3HeB) + 1)

# Panel B: K-corridor multi-valuedness diagram
ax = axs[1]
K_arr = np.logspace(0, 6, 400)
eps_arr = eps_anchor * (K_arr / K_anchor)
ax.loglog(K_arr, eps_arr, "b-", lw=2, label=r"$\epsilon_{\rm eff}(K)$")
ax.axhline(1.0, color="red", linestyle="--",
           label=r"$\epsilon_{\rm eff}=1$ pole")
ax.axvline(K_crit, color="red", linestyle=":",
           label=f"K_crit = {K_crit:.1f}")
ax.axvline(K_star_computed, color="green", linestyle=":",
           label=f"K_* = coth(1) = {K_star_computed:.4f}")
for K in corridor_samples:
    eps = eps_anchor * K / K_anchor
    marker = "o" if K < K_crit else "x"
    color = "green" if K < K_crit else "red"
    ax.plot(K, eps, marker=marker, color=color, markersize=10,
            markeredgecolor="black", markeredgewidth=1.2)
ax.fill_betweenx([1e-3, 1], 1, K_crit, color="lightgreen", alpha=0.25,
                 label="Inflationary (1D Landau)")
ax.fill_betweenx([1, 1e4], K_crit, 1e6, color="mistyrose", alpha=0.35,
                 label="Kinetic-dominated (OFF-manifold)")
ax.set_xlabel("K (order parameter)", fontsize=11)
ax.set_ylabel(r"$\epsilon_{\rm eff}(K)$", fontsize=11)
ax.set_title("W5-55 feed: K-corridor is multi-valued across K_crit\n"
             "Inflationary (K<91.5) is 1D Landau; kinetic is off-manifold",
             fontsize=10.5)
ax.legend(loc="lower right", fontsize=8)
ax.grid(True, alpha=0.3, which="both")

plt.suptitle(
    f"W5-66 GATE-LANDAU-SYMMETRY-CLASS  |  verdict = {verdict}  |  "
    f"N_framework={N_framework}, N_3HeB={N_3HeB}, AZ={AZ_class_framework}",
    fontsize=12, y=1.02,
)
plt.tight_layout()
plot_path = out_dir / "s84_w5_66_plot.png"
plt.savefig(plot_path, dpi=120, bbox_inches="tight")
plt.close()
print(f"Plot written to: {plot_path}")

# ============================================================================
# Section 13. Verdict line (append to canonical verdict file)
# ============================================================================
verdict_line = (
    f"W5-66: {verdict} -- "
    f"value=(G:{G_symbol.replace(' ', '')}|H:{H_symbol.replace(' ', '')}|"
    f"N_OP={N_OP}|class={az_class}) "
    f"scheme=Landau-Ginzburg convention=Volovik-2003-Ch7 L_max=N/A "
    f"sha256={closure_sha}\n"
)
vf = out_dir / "s84_gate_verdicts.txt"
# Read current contents and check for prior W5-66
existing = vf.read_text(encoding="utf-8") if vf.exists() else ""
if "W5-66:" in existing:
    print("\nNote: W5-66 line already exists in s84_gate_verdicts.txt "
          "(appending this evaluation).")
with vf.open("a", encoding="utf-8") as f:
    f.write(verdict_line)
print(f"\nVerdict line appended to: {vf}")
print(verdict_line.rstrip())

print()
print("=" * 78)
print("S84 W5-66 COMPLETE")
print("=" * 78)
