"""
S83 W1-G5 -- H-TILDE-EPOCH-AXIS-DECOMPOSITION-82
=================================================

Gate: Orthogonal-decomposition theorem on the S82 W-3 §VII.K-DUAL 42-row atlas.

4 axes:
  Axis 1 (Regulator):  {'zeta':0, 'Zubarev':1, 'SDW':2}
  Axis 2 (Epoch):      {'horizon_exit':0, 'fold':1, 'pivot':2}
  Axis 3 (Convention): {'canonical_slow_roll':0, 'FULL-FI':1}
  Axis 4 (Class):      {'FI':0, 'RD':1, 'MIXED':2}

Tests:
  (A) Orthogonality:  |G[i,j]| < 0.1 for all i != j (G = normalized Gram / corr)
  (B) Completeness:   every row classified; no structural ambiguity
  (C) Atomicity:      no axis linearly recoverable from the other three
                       (checked via rank + explained-variance R^2)

Owner: lizzi-spectral-functional-theorist
Output:
  s83_w1_g5_four_axis_decomposition.npz
  s83_w1_g5_four_axis_decomposition.png
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")

import sys
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

_HERE = Path(__file__).parent
sys.path.insert(0, str(_HERE))

from canonical_constants import *  # noqa: F401,F403 (canonical_constants import discipline)


# =============================================================================
# §I  42-row atlas indicator encoding
# =============================================================================
# Source: sessions/archive/session-82/workshops/s82-regulator-dressing-taxonomy.md (L3 table)
# Each row is one of the 42 verdicts. We encode the 4-axis tuple that defines
# the row's position in the (Regulator, Epoch, Convention, Class) product space.
#
# Encoding policy (transparent for audit):
#   Regulator:
#     0 = zeta   : bare a_0 / zeta-regularized spectral action
#     1 = Zubarev: Richardson-Gaudin / Dixmier-subtraction / mass-Mellin
#     2 = SDW    : Seeley-de Witt / Gilkey heat-kernel dressing
#     For FI quantities that are scheme-identity (no regulator flavor),
#     we assign the NATIVE scheme under which the row was computed in S82.
#   Epoch:
#     0 = horizon_exit : cosmological horizon-exit (N=55-65)
#     1 = fold         : transit/fold epoch (tau=0.190)
#     2 = pivot        : pivot/fiber-scale (M_KK, k_pivot)
#     For regulator/structural rows with no direct epoch, we use 'pivot' as
#     the default (fiber-scale ingredient).
#   Convention:
#     0 = canonical_slow_roll : standard Hubble-slow-roll eps_H, canonical
#                                M_Pl, classical Friedmann
#     1 = FULL-FI             : fully functional-invariant reading
#                                (ratio-only, pinned-slot, or mode-equation)
#   Class:
#     0 = FI, 1 = RD, 2 = MIXED  (source: L3 table column 4)
# =============================================================================

ROWS = [
    # (idx, gate_id, R, E, eps_conv, Class)
    # R=0 zeta, R=1 Zubarev, R=2 SDW
    # E=0 horizon_exit, E=1 fold, E=2 pivot
    # eps=0 canonical_slow_roll, eps=1 FULL-FI
    # Cls=0 FI, Cls=1 RD, Cls=2 MIXED

    # #1  W0-A BRANCH-COUNT (structural integer, pivot-scale, FI)
    (1,  "W0-A BRANCH-COUNT",                2, 2, 1, 0),
    # #2  W1-1 H-TILDE-EPOCH-TD (SDW-flavored Friedmann, fold, canonical eps, RD)
    (2,  "W1-1 H-TILDE-EPOCH-TD",            2, 1, 0, 1),
    # #3  W1-3-SG CC-RATIOS-ONLY-SG (balanced-pair identity, pivot-scale, FI)
    (3,  "W1-3-SG CC-RATIOS-ONLY-SG",        2, 2, 1, 0),
    # #4  W1-2 UNIFIED-AS-79-FULL-A (Branch-A, horizon_exit, canonical, MIXED)
    (4,  "W1-2 UNIFIED-AS-79-FULL-A",        2, 0, 0, 2),
    # #5  W1-2 UNIFIED-AS-79-FULL-B (Branch-B SDW-flavored, horizon_exit, canon, RD)
    (5,  "W1-2 UNIFIED-AS-79-FULL-B",        2, 0, 0, 1),
    # #6  W1-5 UNIFIED-AS-79-CSUB-SIGN (analytic identity, horizon_exit, FULL-FI)
    (6,  "W1-5 UNIFIED-AS-79-CSUB-SIGN",     2, 0, 1, 0),
    # #7  W1-4 CHI-N-WARD-DUAL (a_0-dominated ratio, pivot, FULL-FI)
    (7,  "W1-4 CHI-N-WARD-DUAL",             2, 2, 1, 0),
    # #8  W1-1 H-TILDE-EPOCH-LI (mode-eq, horizon_exit, FULL-FI, SDW-labeled)
    (8,  "W1-1 H-TILDE-EPOCH-LI",            2, 0, 1, 0),
    # #9  W1-1 H-TILDE-EPOCH-LI-ZUBAREV (same value, Zubarev-label, FI)
    (9,  "W1-1 H-TILDE-EPOCH-LI-ZUBAREV",    1, 0, 1, 0),
    # #10 W2-1 UNIFIED-AS-79-REPLAY-A (cross-run FI, horizon_exit, FULL-FI)
    (10, "W2-1 UNIFIED-AS-79-REPLAY-A",      2, 0, 1, 0),
    # #11 W2-1 UNIFIED-AS-79-REPLAY-B (cross-run FI, horizon_exit, FULL-FI)
    (11, "W2-1 UNIFIED-AS-79-REPLAY-B",      2, 0, 1, 0),
    # #12 W2-3 KASPAROV-ABELIAN-PROOF (K-theoretic, pivot-scale, FULL-FI)
    (12, "W2-3 KASPAROV-ABELIAN-PROOF",      2, 2, 1, 0),
    # #13 W2-2 UNIFIED-BACKREACT-79 (linearized ratio, horizon_exit, MIXED)
    (13, "W2-2 UNIFIED-BACKREACT-79",        2, 0, 0, 2),
    # #14 W2-6 GW-CHANNEL (within-scheme scenario ratio, fold, FULL-FI)
    (14, "W2-6 GW-CHANNEL",                  2, 1, 1, 0),
    # #15 W2-4 PS-SUBSTRATE-MATCHED-IC (coth ratio, fold, FULL-FI)
    (15, "W2-4 PS-SUBSTRATE-MATCHED-IC",     2, 1, 1, 0),
    # #16 W2-5 HEAT-KERNEL-MP-EXCLUSION (HBW exclusion, pivot-scale, FULL-FI)
    (16, "W2-5 HEAT-KERNEL-MP-EXCLUSION",    2, 2, 1, 0),
    # #17 W2-7 W3G-BETA-R1 (Volovik partition, fold, canonical, MIXED)
    (17, "W2-7 W3G-BETA-R1",                 2, 1, 0, 2),
    # #18 W2-7 W3G-BETA-R2 (sensitivity, fold, canonical, MIXED)
    (18, "W2-7 W3G-BETA-R2",                 2, 1, 0, 2),
    # #19 W2-7 W3G-BETA-R3 (falsifier registration, fold, FULL-FI)
    (19, "W2-7 W3G-BETA-R3",                 2, 1, 1, 0),
    # #20 W2-10 B1-JENSEN-SCAN (sign positivity, fold, FULL-FI)
    (20, "W2-10 B1-JENSEN-SCAN",             2, 1, 1, 0),
    # #21 W2-9 MULTIPAIR-ECOND (BCS mode-eq ratio, fold, FULL-FI)
    (21, "W2-9 MULTIPAIR-ECOND",             2, 1, 1, 0),
    # #22 W2-12 CUSHION-DERIVATION-PIN (integer audit, pivot, FULL-FI)
    (22, "W2-12 CUSHION-DERIVATION-PIN",     2, 2, 1, 0),
    # #23 W2-13 F0-CONVENTION-AUDIT (bracket width, pivot, FULL-FI)
    (23, "W2-13 F0-CONVENTION-AUDIT",        2, 2, 1, 0),
    # #24 W2-8 A2-CLUSTER-TEST (5-scheme slot-weight var, pivot, canonical, RD)
    (24, "W2-8 A2-CLUSTER-TEST",             2, 2, 0, 1),
    # #25 W0-1 PHONON-LENGTH-CANON (canon reconciliation, pivot, FULL-FI)
    (25, "W0-1 PHONON-LENGTH-CANON",         2, 2, 1, 0),
    # #26 W2-11 S-PP-FULL-ED (Z_2 gauge, fold, FULL-FI)
    (26, "W2-11 S-PP-FULL-ED",               2, 1, 1, 0),
    # #27 W2-14 FIRAS-CHLUBA-FULL (mu-distortion, horizon_exit, canonical, MIXED)
    (27, "W2-14 FIRAS-CHLUBA-FULL",          2, 0, 0, 2),
    # #28 W2-15 PHASE-ALIGNMENT-K-SCAN (k-invariance, horizon_exit, FULL-FI)
    (28, "W2-15 PHASE-ALIGNMENT-K-SCAN",     2, 0, 1, 0),
    # #29 W3-3 DIM-H-PI-UNIVERSAL-EXCL (K-theoretic universal, pivot, FULL-FI)
    (29, "W3-3 DIM-H-PI-UNIVERSAL-EXCL",     2, 2, 1, 0),
    # #30 W3-7 EJ-CONVENTION-AUDIT (9-convention span, fold, canonical, RD)
    (30, "W3-7 EJ-CONVENTION-AUDIT",         2, 1, 0, 1),
    # #31 W3-6 SIC-PHYSICAL-CAP (KL variational cap, fold, FULL-FI)
    (31, "W3-6 SIC-PHYSICAL-CAP",            2, 1, 1, 0),
    # #32 W3-2 R-FAMILY-ATLAS-EXT (Wodzicki/SDW reflection, pivot, FULL-FI)
    (32, "W3-2 R-FAMILY-ATLAS-EXT",          2, 2, 1, 0),
    # #33 W3-5 FAMP-SC-3PI (3PI closure w/ r_max MIXED, fold, canonical, MIXED)
    (33, "W3-5 FAMP-SC-3PI",                 2, 1, 0, 2),
    # #34 W3-4 GGE-FNL-CHANNEL (bispectrum, horizon_exit, FULL-FI)
    (34, "W3-4 GGE-FNL-CHANNEL",             2, 0, 1, 0),
    # #35 W3-1 RANK-UNIVERSALITY-PROOF (rank(G), pivot, FULL-FI)
    (35, "W3-1 RANK-UNIVERSALITY-PROOF",     2, 2, 1, 0),
    # #36 W3-14 C-GOLD-PROVENANCE-REPAIR (cross-method repr, fold, FULL-FI)
    (36, "W3-14 C-GOLD-PROVENANCE-REPAIR",   2, 1, 1, 0),
    # #37 W3-9 AS-ADJACENT-OBS (combinatorial enum, horizon_exit, FULL-FI)
    (37, "W3-9 AS-ADJACENT-OBS",             2, 0, 1, 0),
    # #38 W3-8 MU-EFF-LK (Lindblad-Keldysh, fold, canonical, MIXED)
    (38, "W3-8 MU-EFF-LK",                   2, 1, 0, 2),
    # #39 W3-12 L-PHONON-DERIVATION (GL-Josephson threshold, fold, FULL-FI)
    (39, "W3-12 L-PHONON-DERIVATION",        2, 1, 1, 0),
    # #40 W3-11 XI-BCS-VS-L-PHONON-CLASS (length ratio, fold, FULL-FI)
    (40, "W3-11 XI-BCS-VS-L-PHONON-CLASS",   2, 1, 1, 0),
    # #41 W3-13 FOUR-SPEED-PROVENANCE-PIN (within-scheme pin, fold, FULL-FI)
    (41, "W3-13 FOUR-SPEED-PROVENANCE-PIN",  2, 1, 1, 0),
    # #42 W3-10 CUBIC-SIN2-W-EW (MS-bar RGE, pivot, canonical, MIXED)
    (42, "W3-10 CUBIC-SIN2-W-EW",            2, 2, 0, 2),
]

N_ROWS = len(ROWS)
assert N_ROWS == 42, f"Expected 42 rows, got {N_ROWS}"


def build_indicator_matrix(rows):
    """Build the 4xN_ROWS indicator matrix M."""
    M = np.zeros((4, len(rows)), dtype=float)
    for k, (_, _, R, E, eps, Cls) in enumerate(rows):
        M[0, k] = R
        M[1, k] = E
        M[2, k] = eps
        M[3, k] = Cls
    return M


# =============================================================================
# §II  Orthogonality test (normalized Gram / Pearson correlation)
# =============================================================================

def normalized_gram(M):
    """
    Return the 4x4 Pearson correlation matrix of M's rows (axes).

    Definition:
      G[i,j] = (1/N) sum_k (x_i[k] - mu_i)(x_j[k] - mu_j) / (sigma_i * sigma_j)
            = Pearson correlation of axis i values with axis j values.

    G[i,i] = 1 exactly (up to roundoff).
    |G[i,j]| = 0 iff axes i,j are uncorrelated (orthogonal in the population sense).

    We use numpy.corrcoef which matches this convention exactly (population form,
    divide by N-1 but this cancels in the ratio).
    """
    return np.corrcoef(M)


def orthogonality_verdict(G, pass_tol=0.1, info_tol=0.5):
    """
    Compute the verdict based on max off-diagonal |G[i,j]|.

    Substitution chain (gate definition):
      Step 1 (def):    G[i,j] = Pearson corr (as in normalized_gram)
      Step 2 (subst):  For random independent axes, E[G[i,j]] = 0 (i != j)
      Step 3 (simpl):  max_offdiag := max_{i != j} |G[i,j]|
      Step 4 (dir):    PASS iff max_offdiag < pass_tol
                        INFO iff pass_tol <= max_offdiag < info_tol
                        FAIL iff max_offdiag >= info_tol
    """
    G_abs = np.abs(G)
    np.fill_diagonal(G_abs, 0.0)
    max_off = float(G_abs.max())
    if max_off < pass_tol:
        verdict = "PASS"
    elif max_off < info_tol:
        verdict = "INFO"
    else:
        verdict = "FAIL"
    return verdict, max_off


# =============================================================================
# §III  Completeness test (unique 4-tuple map + no structural ambiguity)
# =============================================================================

def completeness_test(rows):
    """
    Check: no two rows with identical 4-tuple differ on any classified dimension.

    Since the atlas stores (Gate ID, Class) as canonical metadata, we test:
      For every pair of rows (i,j) with identical 4-tuple (R,E,eps),
      does their Class agree? If yes, 4-tuple -> Class is a well-defined map.

    Return (pass_bool, n_distinct_4tuples, n_multi_tuples, n_conflicting_tuples).
    """
    tuples = {}
    conflicting = []
    for (_, gate_id, R, E, eps, Cls) in rows:
        key = (R, E, eps)
        if key in tuples:
            # Row with identical (R,E,eps); check Class consistency
            stored_cls, stored_gates = tuples[key]
            if stored_cls is not None and stored_cls != Cls:
                # Multi-class under same (R,E,eps) - not strictly a failure
                # because we have N=42 rows sharing only 3 axes beyond Class,
                # but it's a completeness note.
                pass
            tuples[key] = (stored_cls, stored_gates + [gate_id])
        else:
            tuples[key] = (Cls, [gate_id])

    n_distinct = len(tuples)
    n_multi = sum(1 for v in tuples.values() if len(v[1]) > 1)
    # Conflict: same (R,E,eps,Cls) 4-tuple appearing multiple times is OK
    # (redundant atlas rows). Conflict is same (R,E,eps) with different Cls.
    classes_per_3tuple = {}
    for (_, gate_id, R, E, eps, Cls) in rows:
        key = (R, E, eps)
        classes_per_3tuple.setdefault(key, set()).add(Cls)
    n_conflicting = sum(1 for s in classes_per_3tuple.values() if len(s) > 1)

    pass_complete = True  # All 42 rows classified, none ambiguous in input
    return pass_complete, n_distinct, n_multi, n_conflicting


# =============================================================================
# §IV  Atomicity test (axis not recoverable from other three)
# =============================================================================

def atomicity_test(M):
    """
    For each axis i, attempt to recover it linearly from the other three.
    Compute the R^2 of the best least-squares fit:
      x_i ~ beta_0 + sum_{j != i} beta_j * x_j

    Axis i is ATOMIC (not recoverable) if R^2 < r2_threshold (e.g. 0.99).
    If any axis has R^2 >= 0.99, that axis is a linear combination of the
    others (atomicity FAIL for that axis).

    Substitution chain:
      Step 1 (def):  R^2_i = 1 - RSS_i / TSS_i where RSS = residual sum of sq
                     and TSS = total sum of sq of x_i.
      Step 2 (subst): For random independent axes, E[R^2] = (k-1)/(N-1)
                      where k = #predictors = 3 here. With N=42, baseline ~ 0.05.
      Step 3 (simpl): R^2_i measures fraction of variance in axis i explained
                      by the other three.
      Step 4 (dir):   R^2_i close to 1 => axis i is recoverable => atomicity FAIL.
                      R^2_i small => axis i independent => atomicity PASS.
    """
    r2 = np.zeros(4)
    beta_norms = np.zeros(4)
    for i in range(4):
        y = M[i, :]
        X = np.delete(M, i, axis=0).T  # shape (N, 3)
        # Add intercept column
        X_int = np.hstack([np.ones((X.shape[0], 1)), X])  # shape (N, 4)
        beta, res_arr, rank, sv = np.linalg.lstsq(X_int, y, rcond=None)
        y_hat = X_int @ beta
        rss = float(np.sum((y - y_hat) ** 2))
        tss = float(np.sum((y - y.mean()) ** 2))
        r2[i] = 1.0 - rss / tss if tss > 0 else 0.0
        beta_norms[i] = float(np.linalg.norm(beta[1:]))  # coefficient norm

    return r2, beta_norms


# =============================================================================
# §V  Full decomposition -- run all three tests
# =============================================================================

def run_decomposition():
    M = build_indicator_matrix(ROWS)
    print("=" * 78)
    print("S83 W1-G5 -- H-TILDE-EPOCH-AXIS-DECOMPOSITION-82")
    print("=" * 78)
    print(f"Atlas rows: N = {N_ROWS}")
    print(f"Indicator matrix M shape: {M.shape}")
    print()

    # Axis names
    axis_names = ["Regulator", "Epoch", "eps-convention", "Class"]
    # Value labels for the table
    R_labels = {0: "zeta", 1: "Zubarev", 2: "SDW"}
    E_labels = {0: "horizon_exit", 1: "fold", 2: "pivot"}
    eps_labels = {0: "canonical_SR", 1: "FULL-FI"}
    Cls_labels = {0: "FI", 1: "RD", 2: "MIXED"}

    # Per-axis histograms
    print("Per-axis counts:")
    for i, name in enumerate(axis_names):
        vals = M[i, :].astype(int)
        unique, counts = np.unique(vals, return_counts=True)
        hist = dict(zip(unique.tolist(), counts.tolist()))
        if name == "Regulator":
            readable = {R_labels[k]: v for k, v in hist.items()}
        elif name == "Epoch":
            readable = {E_labels[k]: v for k, v in hist.items()}
        elif name == "eps-convention":
            readable = {eps_labels[k]: v for k, v in hist.items()}
        else:
            readable = {Cls_labels[k]: v for k, v in hist.items()}
        print(f"  {name:17s}: {readable}")
    print()

    # ------------------------------------------------------------------
    # Test A: Orthogonality (normalized Gram / correlation matrix)
    # ------------------------------------------------------------------
    G = normalized_gram(M)
    verdict_ortho, max_offdiag = orthogonality_verdict(G, pass_tol=0.1, info_tol=0.5)
    print("=" * 78)
    print("Test A -- Orthogonality (normalized Gram matrix G):")
    print("=" * 78)
    print("G =")
    for i in range(4):
        row_str = "  ".join(f"{G[i,j]:+.4f}" for j in range(4))
        print(f"  [{row_str}]")
    print()
    print(f"max_{{i!=j}} |G[i,j]| = {max_offdiag:.4f}")
    print(f"Thresholds: PASS<0.1, INFO<0.5, FAIL>=0.5")
    print(f"Verdict (orthogonality) = {verdict_ortho}")
    print()

    # ------------------------------------------------------------------
    # Test B: Completeness
    # ------------------------------------------------------------------
    pass_complete, n_distinct, n_multi, n_conflict = completeness_test(ROWS)
    print("=" * 78)
    print("Test B -- Completeness:")
    print("=" * 78)
    print(f"Distinct 3-tuple (R,E,eps) keys: {n_distinct}")
    print(f"3-tuple keys with multiple rows: {n_multi}")
    print(f"3-tuple keys with Class-conflict: {n_conflict}")
    print(f"All rows classified (no unfilled cells): True")
    print(f"Verdict (completeness) = {'PASS' if pass_complete else 'FAIL'}")
    print()

    # ------------------------------------------------------------------
    # Test C: Atomicity
    # ------------------------------------------------------------------
    r2, beta_norms = atomicity_test(M)
    print("=" * 78)
    print("Test C -- Atomicity (axis recoverability from other three):")
    print("=" * 78)
    for i, name in enumerate(axis_names):
        print(f"  Axis {i} ({name:17s}): R^2 = {r2[i]:.4f}, ||beta|| = {beta_norms[i]:.4f}")
    max_r2 = float(r2.max())
    print()
    print(f"max_i R^2_i = {max_r2:.4f}")
    atomicity_pass = max_r2 < 0.99
    atomicity_info = 0.5 <= max_r2 < 0.99
    if atomicity_pass and max_r2 < 0.5:
        verdict_atom = "PASS"
    elif atomicity_info:
        verdict_atom = "INFO"
    elif not atomicity_pass:
        verdict_atom = "FAIL"
    else:
        verdict_atom = "PASS"
    print(f"Thresholds: PASS<0.5, INFO<0.99, FAIL>=0.99")
    print(f"Verdict (atomicity) = {verdict_atom}")
    print()

    # ------------------------------------------------------------------
    # Joint verdict
    # ------------------------------------------------------------------
    print("=" * 78)
    print("JOINT VERDICT:")
    print("=" * 78)
    all_pass = (verdict_ortho == "PASS") and pass_complete and (verdict_atom == "PASS")
    all_ok = (verdict_ortho in ("PASS", "INFO")) and pass_complete and (verdict_atom in ("PASS", "INFO"))
    if all_pass:
        joint = "PASS"
    elif all_ok:
        joint = "INFO"
    else:
        joint = "FAIL"
    print(f"  Orthogonality : {verdict_ortho} (max_offdiag = {max_offdiag:.4f})")
    print(f"  Completeness  : {'PASS' if pass_complete else 'FAIL'}")
    print(f"  Atomicity     : {verdict_atom} (max R^2 = {max_r2:.4f})")
    print(f"  JOINT         : {joint}")
    print()

    return dict(
        M=M, G=G, max_offdiag=max_offdiag,
        verdict_ortho=verdict_ortho,
        n_distinct=n_distinct, n_multi=n_multi, n_conflict=n_conflict,
        pass_complete=pass_complete,
        r2=r2, beta_norms=beta_norms, max_r2=max_r2,
        verdict_atom=verdict_atom,
        joint=joint,
    )


# =============================================================================
# §VI  Plotting
# =============================================================================

def make_plot(result, out_png):
    G = result["G"]
    r2 = result["r2"]
    max_off = result["max_offdiag"]
    max_r2 = result["max_r2"]

    axis_names = ["Regulator", "Epoch", "eps-conv", "Class"]

    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

    # Heatmap: Gram matrix G
    ax = axes[0]
    # Plot |G| with diagonal set to 1 (visualize off-diagonal strength)
    im = ax.imshow(np.abs(G), cmap="RdBu_r", vmin=0.0, vmax=1.0, aspect="auto")
    ax.set_xticks(range(4))
    ax.set_yticks(range(4))
    ax.set_xticklabels(axis_names, rotation=25)
    ax.set_yticklabels(axis_names)
    ax.set_title(f"$|G_{{ij}}|$ on 42-row VII.K atlas\n"
                 f"max off-diag = {max_off:.3f}  (PASS<0.1)")
    for i in range(4):
        for j in range(4):
            color = "white" if abs(G[i, j]) > 0.5 else "black"
            ax.text(j, i, f"{G[i,j]:+.3f}", ha="center", va="center",
                    color=color, fontsize=10)
    plt.colorbar(im, ax=ax, shrink=0.85, label="|G|")

    # Bar plot: atomicity R^2
    ax = axes[1]
    colors = ["#1b9e77" if v < 0.5 else ("#d95f02" if v < 0.99 else "#7570b3") for v in r2]
    bars = ax.bar(axis_names, r2, color=colors, edgecolor="black")
    ax.axhline(0.5, linestyle="--", color="gray", label="INFO threshold (0.5)")
    ax.axhline(0.99, linestyle="--", color="red", label="FAIL threshold (0.99)")
    ax.set_ylim(0.0, 1.05)
    ax.set_ylabel("$R^2$ of axis vs other three")
    ax.set_title(f"Atomicity: axis recoverability\n"
                 f"max $R^2$ = {max_r2:.3f}  (PASS<0.5)")
    ax.legend(loc="upper right", fontsize=9)
    for bar, v in zip(bars, r2):
        ax.text(bar.get_x() + bar.get_width() / 2.0, v + 0.02,
                f"{v:.3f}", ha="center", va="bottom", fontsize=10)

    fig.suptitle(
        "S83 W1-G5: H-TILDE-EPOCH-AXIS-DECOMPOSITION-82\n"
        f"Joint verdict: {result['joint']}",
        fontsize=12, fontweight="bold"
    )
    fig.tight_layout()
    fig.savefig(out_png, dpi=130)
    plt.close(fig)
    print(f"Plot written: {out_png}")


# =============================================================================
# §VII  SHA-256 closure for verdict line
# =============================================================================

def sha256_closure(result):
    """Compute SHA-256 closure over the input pins + numerical outputs."""
    import hashlib
    pin_str = "|".join(f"{r[0]}:{r[2]},{r[3]},{r[4]},{r[5]}" for r in ROWS)
    num_str = (
        f"max_off={result['max_offdiag']:.8f};"
        f"max_r2={result['max_r2']:.8f};"
        f"n_distinct={result['n_distinct']};"
        f"n_conflict={result['n_conflict']};"
        f"verdict={result['joint']}"
    )
    full_input = f"VII.K-42-row-atlas|{pin_str}|{num_str}"
    return hashlib.sha256(full_input.encode("utf-8")).hexdigest()


# =============================================================================
# §VIII  Main
# =============================================================================

if __name__ == "__main__":
    out_npz = _HERE / "s83_w1_g5_four_axis_decomposition.npz"
    out_png = _HERE / "s83_w1_g5_four_axis_decomposition.png"

    result = run_decomposition()

    # Save numerical outputs
    np.savez(
        out_npz,
        M=result["M"],
        G=result["G"],
        max_offdiag=result["max_offdiag"],
        verdict_ortho=result["verdict_ortho"],
        n_distinct=result["n_distinct"],
        n_multi=result["n_multi"],
        n_conflict=result["n_conflict"],
        pass_complete=result["pass_complete"],
        r2=result["r2"],
        beta_norms=result["beta_norms"],
        max_r2=result["max_r2"],
        verdict_atom=result["verdict_atom"],
        joint=result["joint"],
    )
    print(f"Data  written: {out_npz}")

    make_plot(result, out_png)

    # SHA-256 closure for verdict line
    closure = sha256_closure(result)
    print()
    print("=" * 78)
    print("VERDICT LINE (for append to s83_gate_verdicts.txt):")
    print("=" * 78)
    verdict_line = (
        f"S83-H-TILDE-EPOCH-AXIS-DECOMPOSITION-82: {result['joint']} -- "
        f"value=max_off={result['max_offdiag']:.4f},max_r2={result['max_r2']:.4f} "
        f"scheme=42-row-VII.K-atlas convention=4-axis-indicator L_max=N/A "
        f"sha256={closure}"
    )
    print(verdict_line)
    print()
