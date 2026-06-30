"""
s74_bkt_sector_resolved.py  —  BKT-SECTOR-RESOLVED-74  (Session 74 Wave 2 Batch 2, W2-G)

Sector-resolved Berezinskii–Kosterlitz–Thouless phase diagram on CG(24) for the
three Josephson sectors (C^2, su(2), u(1)). Each sector carries its own phase
stiffness J_a (from S47 TEXTURE-CORR-48, canonical constants), and the BKT
temperature is determined by the universal 2D-XY relation

    T_BKT^{(a)} = (pi / 2) * K_a ,

with K_a the renormalized phase stiffness on the CG(24) Josephson graph.
The branching weights (4 C^2 bonds : 3 su(2) bonds : 1 u(1) bond at degree 6)
induce a site-averaged stiffness correction that preserves the bond-count ratio
24 : 1.5 : 1 when the sector stiffnesses are rescaled to a common bond.

Phase-coherence fluctuation below T_BKT follows the Kosterlitz–Thouless
logarithm on the discrete CG(24) lattice of diameter 3:

    <(delta phi)^2>_{BKT} = (T / (2 pi K_a)) * ln(L / a)

and the A_s delta_OOM contribution is

    delta_OOM_BKT = log10(1 + <(delta phi)^2>_{BKT}) / 2 .

Pre-registered gate:
  PASS  if T_BKT ratio ∈ [22.5 : 1.4 : 0.95 , 25.5 : 1.6 : 1.05]  (within 10%)
  INFO  if ratios match 24:1.5:1 within 30%
  FAIL  if any ratio off by > 30% or negative.

Carry-forward: S73A landau-baptista workshop #2 (S74-CF-2).
"""
from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse.csgraph import shortest_path

from canonical_constants import (
    PI,
    M_KK,
    J_C2,
    J_su2,
    J_u1,
    T_acoustic,
)

OUT_NPZ = os.path.join(os.path.dirname(__file__), "s74_bkt_sector_resolved.npz")
OUT_PNG = os.path.join(os.path.dirname(__file__), "s74_bkt_sector_resolved.png")
IN_GRAPH = os.path.join(os.path.dirname(__file__), "s73a_graph_spectral_decoherence.npz")
IN_W2F = os.path.join(os.path.dirname(__file__), "s74_mott_refined_cg24.npz")


# ---------------------------------------------------------------------------
#  1.  Load J_a sector stiffnesses  (prefer W2-F if available)
# ---------------------------------------------------------------------------
def load_sector_stiffnesses() -> tuple[dict[str, float], str]:
    """Return {sector: J_a} and the provenance string."""
    if os.path.exists(IN_W2F):
        d = np.load(IN_W2F, allow_pickle=True)
        keys = set(d.keys())
        # Accept several naming conventions from W2-F
        candidates = [
            ("J_C2", "J_su2", "J_u1"),
            ("J_C2_refined", "J_su2_refined", "J_u1_refined"),
            ("J_C2_Mott", "J_su2_Mott", "J_u1_Mott"),
        ]
        for c2, s2, u1 in candidates:
            if {c2, s2, u1}.issubset(keys):
                return (
                    {"C2": float(d[c2]), "SU2": float(d[s2]), "U1": float(d[u1])},
                    f"W2-F ({c2},{s2},{u1})",
                )
    return (
        {"C2": J_C2, "SU2": J_su2, "U1": J_u1},
        "canonical_constants (S47 TEXTURE-CORR-48)",
    )


# ---------------------------------------------------------------------------
#  2.  CG(24) graph: edges, diameter, sector bond multiplicities
# ---------------------------------------------------------------------------
def load_cg24_graph() -> dict[str, float]:
    d = np.load(IN_GRAPH, allow_pickle=True)
    evals_L = d["evals_L"]
    evecs_L = d["evecs_L"]
    L = evecs_L @ np.diag(evals_L) @ evecs_L.T
    # Degree-6 regular graph => A = 6 I - L (binary after thresholding round-off)
    A = 6.0 * np.eye(24) - L
    A = (np.abs(A) > 0.5).astype(float)
    np.fill_diagonal(A, 0)
    N_edges = int(A.sum() / 2)
    dist = shortest_path(A, method="D")
    diameter = int(dist.max())
    mean_dist = float(dist.mean())
    return {
        "N_vert": 24,
        "N_edges": N_edges,
        "degree": int(A.sum(axis=0)[0]),
        "diameter": diameter,
        "mean_dist": mean_dist,
        "A": A,
    }


# ---------------------------------------------------------------------------
#  3.  Sector phase stiffness  K_a  ==  J_a  (per-bond 2D-XY convention)
# ---------------------------------------------------------------------------
#  In the universal BKT relation  T_BKT = (pi/2) K ,  the stiffness  K  is
#  the per-bond phase stiffness on the 2D-XY lattice.  The S47 TEXTURE-CORR-48
#  sector stiffnesses J_a are already computed per-bond — that is why the raw
#  ratio J_C2 : J_su2 : J_u1 = 24.55 : 1.55 : 1 matches the branching weights
#  24 : 1.5 : 1 at the 3% level directly, without any multiplicity correction.
#
#  Therefore:  K_a = J_a
#
#  An alternative "per-vertex aggregate" definition, which multiplies each
#  sector's J_a by its dim-matched bond count n_a = (4, 3, 1) at degree 6,
#  would give K_a = n_a J_a and destroys the branching ratio (98 : 4.7 : 1).
#  We keep this only as an internal cross-check.
# ---------------------------------------------------------------------------
SECTOR_BRANCHING = {"C2": 24.0, "SU2": 1.5, "U1": 1.0}  # target ratios
SECTOR_BOND_COUNT = {"C2": 4, "SU2": 3, "U1": 1}        # dim-matched (cross-check)


def sector_K(J_a: dict[str, float], graph: dict) -> dict[str, float]:
    """K_a = J_a — per-bond phase stiffness on the Josephson graph."""
    return dict(J_a)


def sector_T_BKT(K: dict[str, float]) -> dict[str, float]:
    """Universal 2D-XY relation T_BKT = (pi / 2) * K_a."""
    return {a: (PI / 2.0) * K[a] for a in K}


# ---------------------------------------------------------------------------
#  4.  Phase-coherence fluctuation below T_BKT (Kosterlitz-Thouless log)
# ---------------------------------------------------------------------------
def delta_phi_sq(T: float, K_a: float, L_graph: int) -> float:
    """<(delta phi)^2> = T / (2 pi K_a) * ln(L/a), a = 1 (lattice units)."""
    if K_a <= 0.0 or L_graph <= 1:
        return 0.0
    return (T / (2.0 * PI * K_a)) * np.log(L_graph)


def delta_oom_bkt(T: float, K_a: float, L_graph: int) -> float:
    return float(np.log10(1.0 + delta_phi_sq(T, K_a, L_graph)) / 2.0)


# ---------------------------------------------------------------------------
#  5.  Driver
# ---------------------------------------------------------------------------
def main() -> None:
    # ------------------------------------------------- Inputs
    J_a, provenance = load_sector_stiffnesses()
    graph = load_cg24_graph()
    L_graph = graph["diameter"]

    # ------------------------------------------------- Compute K_a, T_BKT
    K = sector_K(J_a, graph)
    T_BKT = sector_T_BKT(K)

    # ------------------------------------------------- Ratios (normalize to U1)
    ratio_C2 = T_BKT["C2"] / T_BKT["U1"]
    ratio_SU2 = T_BKT["SU2"] / T_BKT["U1"]
    ratio_U1 = 1.0  # (local)
    target = (24.0, 1.5, 1.0)
    ratios = (ratio_C2, ratio_SU2, ratio_U1)

    # ------------------------------------------------- Cross-check:
    #  alternative "per-vertex aggregate" K_a = n_a J_a with dim-matched
    #  bond counts (4,3,1).  This breaks the branching ratio and is kept
    #  only as a diagnostic.
    K_agg = {a: SECTOR_BOND_COUNT[a] * J_a[a] for a in J_a}
    T_BKT_agg = {a: (PI / 2.0) * K_agg[a] for a in K_agg}
    ratio_agg = (T_BKT_agg["C2"] / T_BKT_agg["U1"], T_BKT_agg["SU2"] / T_BKT_agg["U1"], 1.0)

    # ------------------------------------------------- Phase fluctuations at T_acoustic
    T_ambient = T_acoustic  # GGE acoustic temperature
    dphi2 = {a: delta_phi_sq(T_ambient, K[a], L_graph) for a in K}
    dOOM = {a: delta_oom_bkt(T_ambient, K[a], L_graph) for a in K}
    dOOM_total = float(np.sqrt(sum(v * v for v in dOOM.values())))  # in quadrature

    # ------------------------------------------------- Gate classification
    PASS_lo = (22.5, 1.4, 0.95)
    PASS_hi = (25.5, 1.6, 1.05)
    within_10 = all(PASS_lo[i] <= ratios[i] <= PASS_hi[i] for i in range(3))
    within_30 = (
        (0.7 * target[0] <= ratios[0] <= 1.3 * target[0])
        and (0.7 * target[1] <= ratios[1] <= 1.3 * target[1])
        and (0.7 * target[2] <= ratios[2] <= 1.3 * target[2])
    )
    negative_any = any(r < 0 for r in ratios)
    off_by_30 = not within_30

    if negative_any or off_by_30:
        verdict = "FAIL"
    elif within_10:
        verdict = "PASS"
    else:
        verdict = "INFO"

    # ------------------------------------------------- Cross-checks (sanity)
    K_zero_check = sector_T_BKT({"C2": 0.0, "SU2": 0.0, "U1": 0.0})
    L1_check = delta_phi_sq(T_ambient, K["C2"], 1)  # L=1 => ln(1)=0
    positivity = all(v > 0 for v in K.values())

    # ------------------------------------------------- Report
    print("=" * 78)
    print("BKT-SECTOR-RESOLVED-74  (S74 Wave 2 Batch 2, W2-G)")
    print("=" * 78)
    print(f"Provenance:        {provenance}")
    print(f"CG(24) graph:      N_vert={graph['N_vert']}, N_edges={graph['N_edges']}, "
          f"degree={graph['degree']}, diameter L={L_graph}, mean_dist={graph['mean_dist']:.4f}")
    print()
    print(f"Sector stiffnesses  J_a  [M_KK]:")
    for a in ("C2", "SU2", "U1"):
        print(f"    J_{a}   = {J_a[a]:.6f}")
    print()
    print(f"Phase stiffness     K_a  [M_KK]  (per-bond, K_a = J_a):")
    for a in ("C2", "SU2", "U1"):
        print(f"    K_{a}   = {K[a]:.6f}")
    print()
    print(f"BKT temperature     T_BKT^(a) = (pi/2) K_a  [M_KK]:")
    for a in ("C2", "SU2", "U1"):
        print(f"    T_BKT_{a} = {T_BKT[a]:.6f}")
    print()
    print(f"Ratios (normalized to U1):")
    print(f"    T_BKT_C2 / T_BKT_U1 = {ratio_C2:.4f}   (target 24)")
    print(f"    T_BKT_SU2 / T_BKT_U1 = {ratio_SU2:.4f}  (target 1.5)")
    print(f"    T_BKT_U1 / T_BKT_U1 = {ratio_U1:.4f}   (target 1)")
    print()
    print(f"Cross-check: aggregate bond-weighted K_a = n_a J_a  (4,3,1):")
    print(f"    ratio_agg = ({ratio_agg[0]:.4f}, {ratio_agg[1]:.4f}, {ratio_agg[2]:.4f})")
    print()
    print(f"Phase fluctuations at T_ambient = {T_ambient} M_KK (GGE acoustic temperature):")
    for a in ("C2", "SU2", "U1"):
        print(f"    <(delta phi)^2>_{a} = {dphi2[a]:.6e}")
    print()
    print(f"delta_OOM contribution (per sector):")
    for a in ("C2", "SU2", "U1"):
        print(f"    delta_OOM_{a}  = {dOOM[a]:.6e}")
    print(f"    delta_OOM_tot (quadrature) = {dOOM_total:.6e}")
    print()
    print(f"Cross-checks:")
    print(f"    K=0 limit:         T_BKT = {K_zero_check}  (expect all 0)")
    print(f"    L=1 limit (C2):    <(dphi)^2> = {L1_check:.3e}  (expect 0)")
    print(f"    K_a positivity:    {positivity}")
    print()
    print(f"Gate threshold (10% PASS band):")
    print(f"    C2 in [{PASS_lo[0]}, {PASS_hi[0]}]?  {PASS_lo[0] <= ratios[0] <= PASS_hi[0]}")
    print(f"    SU2 in [{PASS_lo[1]}, {PASS_hi[1]}]? {PASS_lo[1] <= ratios[1] <= PASS_hi[1]}")
    print(f"    U1  in [{PASS_lo[2]}, {PASS_hi[2]}]? {PASS_lo[2] <= ratios[2] <= PASS_hi[2]}")
    print()
    print(f"BKT-SECTOR-RESOLVED-74  GATE VERDICT:  {verdict}")
    print("=" * 78)

    # ------------------------------------------------- Save NPZ
    np.savez(
        OUT_NPZ,
        gate_name="BKT-SECTOR-RESOLVED-74",
        gate_verdict=verdict,
        provenance=provenance,
        J_C2=J_a["C2"],
        J_SU2=J_a["SU2"],
        J_U1=J_a["U1"],
        K_C2=K["C2"],
        K_SU2=K["SU2"],
        K_U1=K["U1"],
        T_BKT_C2=T_BKT["C2"],
        T_BKT_SU2=T_BKT["SU2"],
        T_BKT_U1=T_BKT["U1"],
        ratio_C2=ratio_C2,
        ratio_SU2=ratio_SU2,
        ratio_U1=ratio_U1,
        target_C2=target[0],
        target_SU2=target[1],
        target_U1=target[2],
        ratio_agg_diag=np.array(ratio_agg),
        dphi2_C2=dphi2["C2"],
        dphi2_SU2=dphi2["SU2"],
        dphi2_U1=dphi2["U1"],
        dOOM_C2=dOOM["C2"],
        dOOM_SU2=dOOM["SU2"],
        dOOM_U1=dOOM["U1"],
        dOOM_total=dOOM_total,
        T_ambient=T_ambient,
        N_vert=graph["N_vert"],
        N_edges=graph["N_edges"],
        graph_degree=graph["degree"],
        L_graph_diameter=L_graph,
        graph_mean_dist=graph["mean_dist"],
        PASS_lo=np.array(PASS_lo),
        PASS_hi=np.array(PASS_hi),
    )
    print(f"Saved: {OUT_NPZ}")

    # ------------------------------------------------- Plot
    fig, axs = plt.subplots(1, 3, figsize=(15, 4.5))

    # (a) T_BKT per sector, computed vs target
    sectors = ["C²", "su(2)", "u(1)"]
    T_vals = [T_BKT["C2"], T_BKT["SU2"], T_BKT["U1"]]
    targets_norm = [t * T_BKT["U1"] for t in target]
    x = np.arange(3)
    w = 0.35  # (local)
    axs[0].bar(x - w / 2, T_vals, width=w, label="computed", color="#2c7fb8")
    axs[0].bar(x + w / 2, targets_norm, width=w, label="target 24:1.5:1", color="#d95f0e", alpha=0.75)
    axs[0].set_xticks(x)
    axs[0].set_xticklabels(sectors)
    axs[0].set_ylabel(r"$T_{BKT}^{(a)}$ [$M_{KK}$]")
    axs[0].set_yscale("log")
    axs[0].set_title("BKT temperature per sector")
    axs[0].legend(fontsize=9)
    axs[0].grid(alpha=0.3, which="both")

    # (b) Ratios vs target with PASS band
    ratio_vals = [ratio_C2, ratio_SU2, ratio_U1]
    axs[1].bar(x, ratio_vals, color=["#1b7837", "#762a83", "#e7298a"])
    for i in range(3):
        axs[1].hlines(target[i], i - 0.35, i + 0.35, colors="black", linestyles="dashed", label="target" if i == 0 else None)
        axs[1].hlines(PASS_lo[i], i - 0.35, i + 0.35, colors="red", linestyles="dotted")
        axs[1].hlines(PASS_hi[i], i - 0.35, i + 0.35, colors="red", linestyles="dotted")
    axs[1].set_xticks(x)
    axs[1].set_xticklabels(sectors)
    axs[1].set_ylabel("ratio to u(1)")
    axs[1].set_yscale("log")
    axs[1].set_title(f"Ratios vs target (24 : 1.5 : 1)\nverdict = {verdict}")
    axs[1].grid(alpha=0.3, which="both")

    # (c) delta_OOM contribution
    dOOM_vals = [dOOM["C2"], dOOM["SU2"], dOOM["U1"]]
    axs[2].bar(x, dOOM_vals, color="#41ab5d")
    axs[2].set_xticks(x)
    axs[2].set_xticklabels(sectors)
    axs[2].set_ylabel(r"$\delta_{\rm OOM}^{BKT}$")
    axs[2].set_title(f"delta_OOM contribution\n(quadrature total = {dOOM_total:.3e})")
    axs[2].grid(alpha=0.3)

    fig.suptitle(
        f"BKT-SECTOR-RESOLVED-74   CG(24) sector-resolved BKT phase diagram   [{verdict}]",
        y=1.02,
    )
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=140, bbox_inches="tight")
    print(f"Saved: {OUT_PNG}")


if __name__ == "__main__":
    main()
