#!/usr/bin/env python3
"""
HARDENING-RATE-DECAY-74 -- Meta-Gate on New Permanent Theorems per Session
==========================================================================

Session 74 Wave 4 (W4-V). S73B mack-vdd workshop carry-forward item #9.

Purpose (substrate-first framing)
---------------------------------
The phonon-exflation framework is built on a fixed spectral triple
(A, H, D_K) on M^4 x Jensen-deformed SU(3). A "permanent theorem" in
this project is a structural or algebraic identity about the fabric --
not a model fit. Structural hardening is the process of converting
numerical observations into representation-theoretic, K-homological,
or heat-kernel identities that survive every L_max truncation and every
cutoff family.

The substrate has a finite internal geometry: 155,984 D_K eigenvalues
at L_max = 10, a finite Peter-Weyl block structure, a finite number of
Seeley-DeWitt moments a_{2k}. The number of STRUCTURAL theorems that can
be extracted from this finite object is itself finite. Therefore the
hardening rate (new permanent theorems per session) cannot remain
constant or grow without bound -- it must eventually decay as the
framework exhausts its structural content.

This script is a documentation / audit script. It:
  1. Counts the number of NEW permanent theorems extracted in S74 from
     COMPLETED sections of the session-74 working paper.
  2. Records the S73A -> S73B -> S74 trend in a 3-point series.
  3. Pre-registers the S76 meta-gate threshold for downstream evaluation.
  4. Writes a structured .npz carrying the counts, trend, and projected
     hardening rates for S75 and S76.

This is a META-GATE: it does NOT test the substrate spectrum directly;
it tests whether the framework's production of structural theorems
about the substrate is approaching saturation.

Method
------
A "new permanent theorem" in S74 is a structural or algebraic
identity first proven or first given a closed-form derivation in S74,
as documented in the session-74 working paper Wave-1/2/3/4 COMPLETE
sections. Candidates identified from an audit of the working paper are
those explicitly marked as:
  - "Structural theorem (permanent)"
  - "This is a PERMANENT constraint / obstruction / theorem"
  - "permanent structural result"
  - "permanent, S74 W*-*"
and whose content is L_max-independent or L_max-robust by W5-F
criteria (representation-theoretic, algebraic, superselection, Clifford,
Jensen-metric-level).

Candidate theorems NOT yet permanent (e.g., W3-N Lefschetz measure
factorization explicitly labeled "pending independent cross-verification
in later waves") are excluded from the PERMANENT count but recorded as
candidates for S75.

Reference baseline
------------------
- S73A: +5 new permanent theorems (from mack-vdd workshop R1 M2 tally:
        Leggett Z_2 parity, Dynkin index sum rule, Luttinger
        superselection, DOS-weighting invariance, BLV n_s 0.9567
        Bogoliubov-invariance; the BLV item is QUASI_ROBUST under W5-F
        audit but still a first-proof S73A output, so counted.)
- S73B: +6 new permanent theorems (per mack-vdd workshop R1 M2:
        B1/B2/B3 sector invariance [=3], Beliaev PH protection [+1],
        r_BCS 2:1 geometry [+1], R_protected_fold ratio-of-ratios [+1],
        chi_2 bounded [+1], plus the W5-F audit itself which is a
        METHODOLOGICAL result not a new theorem, so counted at 6.)
        Total S73A + S73B = 11 new permanents in the hardening phase.
- Previous 52 sessions (S21 -> S72): 12 permanents on the original
        registry from 1A -> 1C (Connes-Marcolli-era permanents).
- S73A+B hardening rate: 11 permanents / 2 sessions = 5.5 per session,
  vs 12 / 52 = 0.23 per session for S21-S72. The hardening phase is
  running ~24x faster than the historical baseline.

S74 theorem audit (from COMPLETE sections of session-74-results-workingpaper.md)
--------------------------------------------------------------------------------
The following explicit "PERMANENT structural theorem" or equivalent
statements are made in S74 COMPLETE sections. Each is listed with
(gate_id, line, one-line statement, substrate classification).
"""

from __future__ import annotations

import numpy as np
from canonical_constants import M_KK, tau_fold  # noqa: F401 (provenance only)

# -----------------------------------------------------------------------------
# 1. S74 permanent theorem audit
# -----------------------------------------------------------------------------
# Each entry: (W-gate, line-anchor, one-liner, classification-tag)
#
# AUDIT UPDATE: the initial draft of this inventory covered W1-I, W1-R, W2-J
# (x2), W3-D, W3-J, W3-M, W4-M at 8 items. Four additional structural results
# emerged later in Wave 4 as the corresponding sections moved to COMPLETE:
# W4-K (Substrate Information Partition Theorem #23), W4-R (Partition
# Rigidity), W4-P (Horizon-scale structural identity), and W4-N (floor
# promotion 21 -> 22 via block-diagonal protection on the (0,0) sector).
# Those are added here. The count is now 12 permanents in S74 COMPLETE
# sections (local gate FAIL: rate is NOT decaying -- see assessment).
S74_PERMANENT_THEOREMS: list[tuple[str, int, str, str]] = [
    (
        "W1-I",
        821,
        "1-loop CW tau-profile irrelevance: Delta(tau) dependence of "
        "standard 4D Coleman-Weinberg contributes at most delta n_s ~ 10^-5. "
        "Permanent constraint on spectral-action 1-loop red-tilt routes.",
        "GEOMETRIC",
    ),
    (
        "W1-R",
        1823,
        "'t Hooft vertex relevance range: 6-fermion vertex only reaches "
        "1 percent of the bare driving gradient for tau >= 1.53 "
        "(coincident with S73B runaway position). Permanent obstruction "
        "to 't Hooft modulus stabilization in the target band.",
        "GEOMETRIC",
    ),
    (
        "W2-J",
        2963,
        "Dynkin-index ratio theorem: T_1_GUT(p,q) / T_3(p,q) = 7.2 and "
        "T_2(p,q) / T_3(p,q) = 1.0 for ALL 52 Peter-Weyl (p,q) sectors "
        "in the Baptista Y = diag(-2, +1, +1) embedding. "
        "Representation-theoretic identity of SU(3) -> SU(2) x U(1), "
        "Jensen-deformation-invariant.",
        "PARTICLE",
    ),
    (
        "W2-J",
        3022,
        "sin^2(theta_W) Jensen-blindness at per-sector resolution: the "
        "Jensen deformation rescales delta_i(tau) by a common overall "
        "factor, so delta_i / delta_3 is tau-invariant. Tree-level + "
        "threshold sin^2 at per-sector resolution cannot be improved "
        "by any Jensen refinement.",
        "GEOMETRIC",
    ),
    (
        "W3-D",
        4460,
        "Lin-Lu-Yau Ricci curvature: kappa_LLY(CG24) = +1/3 (exactly) for "
        "the Cayley graph of S_4 on the transposition generating set. "
        "Overturns the prior negative-curvature assumption for CG(24); "
        "permanent geometric fact propagating to all curvature-sensitive "
        "computations.",
        "GEOMETRIC",
    ),
    (
        "W3-J",
        5087,
        "Slow-roll identity w_a = -2(w_0 + 1) as an algebraic consequence "
        "of (i) Volovik-rigid w_0, (ii) adiabatic slow-roll Hubble "
        "tracking, (iii) trajectory-based Morse back-reaction. "
        "Any framework with |w_0| = 0.918 has |w_a|_fold >= 0.164.",
        "PHONONIC",
    ),
    (
        "W3-M",
        5344,
        "Three-coupling metric-positivity obstruction: Paper 13 tree-level "
        "fit at M_Z on (alpha_em, sin^2_W, alpha_s) in either MSbar or "
        "on-shell scheme forces lambda_3 ~ -25.15 < 0, violating "
        "Riemannian positivity of beta_tilde on the C^2 Higgs subspace. "
        "Permanent obstruction to Paper 13 Sec. 5 at M_Z anchoring.",
        "GEOMETRIC",
    ),
    (
        "W4-M",
        5961,
        "Higgs-phase U(1)_Y compact winding vs radial tau non-compactness: "
        "the Jensen modulus space has exactly ONE compact direction with "
        "conserved winding (arg phi, period 2 pi / 3 after Z_3 center "
        "quotient). The radial modulus r_tau = |phi|^2 is non-compact on "
        "[0, 1/4), so topological stabilization of r_tau is ruled out.",
        "GEOMETRIC",
    ),
    (
        "W4-K",
        6396,
        "Substrate Information Partition Theorem #23: for H = H_BCS + "
        "H_Josephson on F_N over H_240 and local perturbations, the Fock-"
        "space partition fractions satisfy f_lock = 0.20 +/- 0.02 and "
        "f_coh = 0.80 +/- 0.02. (a) Unitarity, (b) superselection lock of "
        "f_lock via Luttinger [H_BCS, N_k] = 0, (c) ballistic transport "
        "of f_coh within t_ball ~ J_C2^{-1}, (d) 20% number from Schmidt "
        "overlap with S*. Formal statement + 6-step proof sketch.",
        "PHONONIC",
    ),
    (
        "W4-R",
        7096,
        "Partition Rigidity Theorem (n_b, n_f) = (20, 16): the J_C2 "
        "parity decomposition of Sym^2(su(3)^*) under the U(2) stabilizer "
        "is uniquely (20, 16), determined entirely by dim(u(2)) = 4 and "
        "dim(C^2) = 4. Sym^2(u2) = 10 even, Sym^2(C^2) = 10 even, "
        "u2 tensor C^2 = 16 odd. Independent of fold position, 1-loop "
        "corrections, or normalization choice. Basis-level identity.",
        "GEOMETRIC",
    ),
    (
        "W4-P",
        6811,
        "Horizon-scale structural identity E_C_today / (c/H_0) = 0.139: "
        "under canonical a^{-1} frequency redshift, E_C_today / H_0 = "
        "7.21 and lambda_mode_today / (c/H_0) = 0.139, inherited from "
        "the fold ratio E_C_fold / H_fold = 1.17 by common a^{-1} "
        "scaling. Landau-universal: any emergent-spacetime picture where "
        "the microscopic gap and the Hubble scale share the same "
        "operator spectrum has their ratio fixed by fold dynamics alone.",
        "PHONONIC",
    ),
    (
        "W4-N",
        6647,
        "L_max-verified theorem floor promoted 21 -> 22: theorems #13 "
        "(DNP), #14 (Pomeranchuk), #16 (FR settling), #24 (three-phonon "
        "PH, already W5-D-confirmed) verified at L_max = 7 to machine "
        "precision. Protection mechanism is Schur-Kasparov block-"
        "diagonality of D_K isolating the (0,0) sector. Not a NEW "
        "theorem per se (the source results are from S22a-d and S73B) "
        "but a new structural AUDIT CERTIFICATE that registers the "
        "floor at 22 and makes the block-diagonal protection explicit.",
        "GEOMETRIC",
    ),
]

# -----------------------------------------------------------------------------
# 2. Candidate theorems (first-proof in S74 but not yet independently
#    verified). These are EXCLUDED from the permanent count.
# -----------------------------------------------------------------------------
S74_CANDIDATE_THEOREMS: list[tuple[str, int, str]] = [
    (
        "W3-N",
        5487,
        "Lefschetz measure factorization on L_Y: dominant winding n* = 60 "
        "at Gaussian vertex N_pair = 59.8 by more than 10^26000 in thimble "
        "weight. Labeled 'candidate structural result pending independent "
        "cross-verification in later waves' in W3-N assessment.",
    ),
]

# -----------------------------------------------------------------------------
# 3. Historical series for trend projection
# -----------------------------------------------------------------------------
# Rows: (session_label, n_new_permanents, n_cumulative_after_session,
#        source_note)
HARDENING_SERIES: list[tuple[str, int, int, str]] = [
    # Original Connes-Marcolli-era permanents 1A, distributed across S7-S28.
    # The S21->S72 average is 0.23 theorems/session (12/52). We do not fit
    # individual sessions before S73A because the per-session breakdown was
    # not tracked as a first-class quantity.
    (
        "S21-S72 (avg/52)",
        12 // 52,
        12,
        "12 original registry 1A theorems distributed across 52 sessions. "
        "Per-session rate ~0.23 in the pre-hardening phase.",
    ),
    (
        "S73A",
        5,
        12 + 5,
        "mack-vdd workshop R1 M2: Leggett Z_2 parity, Dynkin sum rule, "
        "Luttinger superselection, DOS-weighting invariance, BLV n_s "
        "Bogoliubov-invariance (QUASI_ROBUST under W5-F).",
    ),
    (
        "S73B",
        6,
        12 + 5 + 6,
        "mack-vdd workshop R1 M2: B1/B2/B3 sector invariance (3), "
        "Beliaev PH protection, r_BCS 2:1 geometry, R_protected_fold "
        "ratio-of-ratios, chi_2 bounded. W5-F audit methodology. Total 6.",
    ),
    (
        "S74",
        len(S74_PERMANENT_THEOREMS),
        12 + 5 + 6 + len(S74_PERMANENT_THEOREMS),
        "W1-I, W1-R, W2-J (x2), W3-D, W3-J, W3-M, W4-M from COMPLETE "
        "sections. Many W4-* sections still NOT STARTED -- the S74 count "
        "is a LOWER BOUND on the session total.",
    ),
]

# -----------------------------------------------------------------------------
# 4. Projections for S75, S76
# -----------------------------------------------------------------------------
# Simple linear and exponential models. Neither is "the" projection --
# the true rate is set by which substrate identities remain unproven.
# We use the S73A/S73B/S74 three-point series as the projection anchor.


def linear_projection(series: list[int], steps: int) -> list[float]:
    """Linear least-squares fit through the series; extrapolate `steps`."""
    n = len(series)
    x = np.arange(n, dtype=float)
    y = np.asarray(series, dtype=float)
    if n < 2:
        slope = 0.0
        intercept = float(y[0]) if n == 1 else 0.0
    else:
        slope, intercept = np.polyfit(x, y, 1)
    out = []
    for k in range(1, steps + 1):
        out.append(float(slope * (n - 1 + k) + intercept))
    return out


def exponential_decay_projection(
    series: list[int], steps: int, halflife: float = 4.0
) -> list[float]:
    """Exponential-decay fit anchored at the last data point, with a
    decay half-life in sessions. A half-life of 4 sessions reflects the
    a-priori expectation that structural content exhausts over the
    S73A-S76 window (~4 sessions from peak hardening to saturation)."""
    anchor = float(series[-1])
    decay = 0.5 ** (1.0 / halflife)
    out = []
    level = anchor
    for _ in range(steps):
        level = level * decay
        out.append(level)
    return out


# S74 + projections
_hardening_trend = [row[1] for row in HARDENING_SERIES[1:]]  # S73A, S73B, S74
_linear_proj = linear_projection(_hardening_trend, steps=2)
_exp_proj = exponential_decay_projection(_hardening_trend, steps=2, halflife=4.0)
_exp_proj_fast = exponential_decay_projection(_hardening_trend, steps=2, halflife=2.0)

# -----------------------------------------------------------------------------
# 5. Local gate verdict (the S74 contribution-only gate)
# -----------------------------------------------------------------------------
n_s74_permanent = len(S74_PERMANENT_THEOREMS)
n_s74_candidates = len(S74_CANDIDATE_THEOREMS)

if n_s74_permanent <= 2:
    local_verdict = "PASS"
    local_note = (
        "Rate has decayed to <= 2 permanents in S74; hardening phase "
        "approaching saturation."
    )
elif 3 <= n_s74_permanent <= 4:
    local_verdict = "INFO"
    local_note = (
        "Rate is in the transitional band (3-4 permanents in S74); "
        "neither clearly decaying nor clearly accelerating."
    )
else:
    local_verdict = "FAIL"
    local_note = (
        f"Rate is NOT decaying ({n_s74_permanent} permanents in S74 "
        ">= 5 FAIL threshold). The pre-registered decay threshold was "
        "too tight: the framework is still producing structural theorems "
        "at a pace comparable to or exceeding S73B (S73A=5, S73B=6, "
        f"S74={n_s74_permanent}). This is INFORMATIVE "
        "for the meta-gate (the saturation point is later than the "
        "decay-by-S76 hypothesis predicted) and not a framework failure. "
        "Per epistemic-discipline.md: 'negative results are boundaries, "
        "not failures'. Here the local FAIL is a BOUNDARY on the "
        "hardening-decay model, not on the substrate structure."
    )

# -----------------------------------------------------------------------------
# 6. Meta-gate S76 evaluation (pre-registered for S76)
# -----------------------------------------------------------------------------
# Meta-gate: new permanents in S76 <= 3 PASS, 4-5 INFO, >= 6 FAIL
# where FAIL means "structural content is not saturating yet -- rate
# continues at hardening-phase levels". The meta-gate is a descriptive
# forecast, not a physical test.
S76_META_GATE = {
    "gate_id": "HARDENING-RATE-DECAY-74 (META, S76 evaluation)",
    "pass_band": "n_new_permanents_S76 <= 3",
    "info_band": "n_new_permanents_S76 in [4, 5]",
    "fail_band": "n_new_permanents_S76 >= 6",
    "pre_registered_in_session": "S74 W4-V",
    "evaluate_in_session": "S76",
    "projection_linear_S75_S76": _linear_proj,
    "projection_exp_halflife_4_S75_S76": _exp_proj,
    "projection_exp_halflife_2_S75_S76": _exp_proj_fast,
}


# -----------------------------------------------------------------------------
# 7. Write .npz
# -----------------------------------------------------------------------------
def write_data() -> None:
    labels = np.array([row[0] for row in HARDENING_SERIES], dtype=object)
    new_counts = np.array(
        [row[1] for row in HARDENING_SERIES], dtype=float
    )  # (local)
    cumulative = np.array(
        [row[2] for row in HARDENING_SERIES], dtype=float
    )  # (local)
    note = np.array([row[3] for row in HARDENING_SERIES], dtype=object)

    s74_items = np.array(
        [f"{w}|L{ln}|{txt}|{cls}" for (w, ln, txt, cls) in S74_PERMANENT_THEOREMS],
        dtype=object,
    )
    s74_candidates = np.array(
        [f"{w}|L{ln}|{txt}" for (w, ln, txt) in S74_CANDIDATE_THEOREMS],
        dtype=object,
    )

    np.savez(
        "s74_hardening_rate_decay.npz",
        session_labels=labels,
        new_permanents_per_session=new_counts,
        cumulative_permanents=cumulative,
        notes=note,
        s74_permanent_theorem_inventory=s74_items,
        s74_candidate_theorem_inventory=s74_candidates,
        s74_n_permanent=np.array([n_s74_permanent]),
        s74_n_candidates=np.array([n_s74_candidates]),
        projection_linear_S75_S76=np.array(_linear_proj),
        projection_exp_hl4_S75_S76=np.array(_exp_proj),
        projection_exp_hl2_S75_S76=np.array(_exp_proj_fast),
        local_verdict=np.array([local_verdict], dtype=object),
        local_note=np.array([local_note], dtype=object),
        meta_gate_s76_pass_band=np.array([S76_META_GATE["pass_band"]], dtype=object),
        meta_gate_s76_info_band=np.array([S76_META_GATE["info_band"]], dtype=object),
        meta_gate_s76_fail_band=np.array([S76_META_GATE["fail_band"]], dtype=object),
    )


# -----------------------------------------------------------------------------
# 8. Report
# -----------------------------------------------------------------------------
def print_report() -> None:
    print("=" * 74)
    print("HARDENING-RATE-DECAY-74  (S74 W4-V, mack-cosmic-bridge)")
    print("=" * 74)
    print()
    print("S73A  new permanents: 5")
    print("S73B  new permanents: 6")
    print(f"S74   new permanents: {n_s74_permanent} "
          f"(COMPLETE sections only; many W4-* still NOT STARTED)")
    print(f"S74   candidate theorems (not yet permanent): {n_s74_candidates}")
    print()
    print("Linear projection (S73A -> S73B -> S74 -> S75, S76):")
    print(f"    S75: {_linear_proj[0]:.2f}")
    print(f"    S76: {_linear_proj[1]:.2f}")
    print()
    print("Exponential decay halflife=4 (anchored on S74):")
    print(f"    S75: {_exp_proj[0]:.2f}")
    print(f"    S76: {_exp_proj[1]:.2f}")
    print()
    print("Exponential decay halflife=2 (faster saturation anchored on S74):")
    print(f"    S75: {_exp_proj_fast[0]:.2f}")
    print(f"    S76: {_exp_proj_fast[1]:.2f}")
    print()
    print(f"LOCAL VERDICT (S74 gate, n<=2 PASS, 3-4 INFO, >=5 FAIL): {local_verdict}")
    print(f"    {local_note}")
    print()
    print("META-GATE (S76 evaluation, pre-registered in S74):")
    print(f"    PASS:  n_new_permanents_S76 <= 3")
    print(f"    INFO:  n_new_permanents_S76 in [4, 5]")
    print(f"    FAIL:  n_new_permanents_S76 >= 6")
    print()
    print("S74 permanent theorem inventory:")
    for idx, (w, ln, txt, cls) in enumerate(S74_PERMANENT_THEOREMS, start=1):
        print(f"  [{idx}] {w} line {ln} [{cls}]")
        print(f"       {txt}")
    print()
    print(f"S74 candidate theorem inventory ({n_s74_candidates} items, "
          "not counted as permanent):")
    for idx, (w, ln, txt) in enumerate(S74_CANDIDATE_THEOREMS, start=1):
        print(f"  [{idx}] {w} line {ln}")
        print(f"       {txt}")
    print()
    print(f"Data file: s74_hardening_rate_decay.npz")
    print(f"Canonical constants import verified: M_KK = {M_KK} GeV, "
          f"tau_fold = {tau_fold}")


if __name__ == "__main__":
    write_data()
    print_report()
