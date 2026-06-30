"""
S74 W4-HH: EVOI Recalibration from S74 Findings.

Carry-forward #10 from S73B landau-baptista workshop.

PURPOSE
-------
Update the S73B EVOI priority table (21 items N1..N21) with S74 findings
from all 4 waves. For each item:
  - Classify status: RESOLVED-PASS / RESOLVED-FAIL / INFO / OPEN
  - Recompute EVOI = P(pass) * |delta_P(pass)| + P(fail) * |delta_P(fail)|
  - Flag items that collapse (resolved) vs. items that remain
Then add NEW items from S74 structural findings (Wave 1-4 verdicts).

METHOD (constraint-mapping, not probability-mongering)
------
Every verdict is pre-registered. Every resolution is permanent. The EVOI
numbers for STILL-OPEN items are pulled from the S73B table (unchanged
unless a S74 finding explicitly updates their P(pass) prior). New items
get P(pass) estimates based on their dependency structure.

OUTPUT
------
computations/session-74/s74_evoi_recalibration.npz
  - item_ids (string)
  - statuses (string: RESOLVED-PASS / RESOLVED-FAIL / INFO / OPEN / SUPERSEDED)
  - p_pass (float array)
  - evoi (float array)
  - tier (int array)
  - sources (string: S74 wave ID or "carry-from-S73B")
  - verdict_notes (string descriptions)
"""

import os
import sys
import numpy as np

# canonical constants for provenance only
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import M_KK, tau_fold  # noqa: F401


# -----------------------------------------------------------------------------
# Status constants
# -----------------------------------------------------------------------------
PASS = "RESOLVED-PASS"
FAIL = "RESOLVED-FAIL"
INFO = "INFO"
OPEN = "OPEN"
SUPER = "SUPERSEDED"


def evoi(p_pass, dp_up, dp_down):
    """Expected Value of Information.

    EVOI = P(pass) * |delta_P(pass)| + P(fail) * |delta_P(fail)|
    """
    p_pass = float(p_pass)
    dp_up = float(dp_up)
    dp_down = float(dp_down)
    return p_pass * abs(dp_up) + (1.0 - p_pass) * abs(dp_down)  # (local)


# -----------------------------------------------------------------------------
# S73B 21 items (N1..N21) — update status from S74 verdicts
# -----------------------------------------------------------------------------
# Each entry: (id, s74_item, status, p_pass, dp_up, dp_down, tier, note)
# p_pass, dp_up, dp_down are RETAINED where OPEN; ZEROED on resolution.

updates_s73b = [
    # ========================================================
    # LEVEL 1 — CRITICAL (S73B)
    # ========================================================
    (
        "N1 TRANSFER-FUNCTION-74",
        "W1-A",
        INFO,
        0.0, 0.0, 0.0,
        1,
        "INFO: |alpha_s(k_pivot)| = 8.4e-15 << 0.015 (PASS clause), "
        "but n_s(k_pivot) = 1.000 OUT of Planck 1-sigma [0.9607, 0.9691] "
        "(FAIL clause). Sasaki-Stewart multifield delta-N is exactly scale-"
        "invariant (J_b^2 cancels H_cross^2 at every k). S73B alpha_s = +0.833 "
        "125-sigma tension ELIMINATED. Red-tilt origin confirmed NOT in "
        "multifield transfer; must come from BCS-CW (S66 route) or dispersive "
        "r_b(k) running. RESOLVED as INFO — partial.",
    ),
    (
        "N2 MODULI-STABILIZATION-74",
        "W1-B",
        FAIL,
        0.0, 0.0, 0.0,
        1,
        "FAIL: NO V_eff minimum in [0.45,0.70] for any of 4 sub-gates "
        "((a) instanton back-reaction, (b) BCS dressing, (c) GGE relic, "
        "(d) L_max in {3,5,7}). Restoring/driving ratio = 0.28% (309x "
        "shortfall). Modulus requires external physics — multi-instanton "
        "(L_max>=10) and cross-moment back-reaction remain UNCOMPUTED. "
        "Perturbative + 1-instanton stabilization CLOSED.",
    ),
    (
        "N3 L-MAX-ZETA-REGULARIZATION-73B-W5",
        "W1-C",
        FAIL,
        0.0, 0.0, 0.0,
        1,
        "FAIL: Three routes disagree at L_max=7 by 231% (not 3%). "
        "(a_0/a_2)/(a_2/a_4) drift L=3->L=7 is 19.4% (not 5%). R_3 drifts "
        "29% outside R_1. Direct zeta power sums DIVERGENT -- truncated "
        "spectrum has no valid small-t expansion. Canonical Chamseddine-"
        "Connes SDW with cutoff f is the ONLY physically meaningful route. "
        "Confirms SDW-VALIDATION structural issue.",
    ),
    (
        "N4 E_C-RESOLUTION-74",
        "W1-D",
        PASS,
        0.0, 0.0, 0.0,
        1,
        "PASS: E_C^{OES,CG24} = 0.4643 M_KK (Method A, single-cell spectral "
        "invariant, finite-size bound 0.39%). Dead center of PASS band "
        "[0.30, 0.60]. Methods B (9.01 M_KK, Bogoliubov fixed point) and "
        "C (0.061 M_KK, 4-cell exact diag) diagnose separate physical "
        "content. Canonical value established. Mott/BKT closures unblocked.",
    ),

    # ========================================================
    # LEVEL 2 — HIGH (S73B)
    # ========================================================
    (
        "N5 GGE-TRANSFER-74",
        "(carry: implicit in W1-A/W1-K)",
        OPEN,
        0.50, 0.15, 0.10,
        2,
        "OPEN: W1-A showed the per-branch Planck/Jacobian products are "
        "scale-invariant -- the GGE-to-CMB transfer alone cannot produce "
        "a red tilt. W1-K overlap matrix finds B1 is 69% tensor after "
        "SU(3)->SO(3) Elliott branching, so the GGE transfer rerouting "
        "through the tensor channel is an OPEN question. EVOI retained.",
    ),
    (
        "N6 SIN2-LR-NORMALIZATION-74",
        "W2-J + W3-I + W3-M",
        FAIL,
        0.0, 0.0, 0.0,
        2,
        "FAIL: W2-J JENSEN-THRESHOLD-74 FAIL (sin^2 = -0.046, 466x above "
        "threshold). W3-I MODULAR-SIN2-74 FAIL (decoupled threshold sum "
        "preserves the 7.2:1 ratio to 2.3e-15 along the entire modular "
        "flow; per-component escape hypothesis CLOSED). W3-M HETEROTIC-"
        "LR-74 sub-gate (B) PASS (sin^2 in [0.21, 0.25]) but sub-gate "
        "(A) FAIL (lambda_3 = -25.15 violates Riemannian metric "
        "positivity on C^2 Higgs subspace). LEFT/RIGHT asymmetry route "
        "CLOSED in its natural formulation.",
    ),
    (
        "N7 EC-UNIFIED-74",
        "W1-D",
        PASS,
        0.0, 0.0, 0.0,
        2,
        "PASS (folded into N4): W1-D established Method A (single-cell "
        "spectral invariant) as canonical. Routes B and C diagnose "
        "orthogonal physical content (inter-cell Josephson vs exact "
        "small-cluster energy). The 1133x spread becomes structural, "
        "not a confusion — each route measures a DIFFERENT observable "
        "on the same underlying E_C. Resolution is TAXONOMIC, not "
        "reconciliation.",
    ),
    (
        "N8 CC-M1-REGULARIZATION-74",
        "W2-Q",
        INFO,
        0.0, 0.0, 0.0,
        2,
        "INFO (split): FAIL on literal Scheme A (f_0 * M_1 * M_KK^4 "
        "= +123 OOM, as expected for bare Planck-scale M_1). PASS on "
        "Scheme B (f_0 * <|lambda|> * H_0^2 * M_Pl^2 = +0.12 OOM, "
        "factor 1.3 from rho_obs). W2-Q cross-validates W2-K HP4 "
        "pairing (chi_2 = <|lambda|>/lam_max identity). All three CC "
        "routes (S66 Volovik, W2-K HP4, W2-Q M1-B) land within 1 OOM "
        "of rho_obs under gravity-sector normalization.",
    ),
    (
        "N9 INSTANTON-STABILIZATION-74",
        "W2-R + W1-P + W1-Q + W1-R + W2-S",
        INFO,
        0.0, 0.0, 0.0,
        2,
        "INFO: W2-R dV_inst/dtau sign CORRECT but magnitude 213x too "
        "small. W1-P connected 2-instanton correlator FAIL (conservative "
        "valley). W1-Q Coulomb-gas V_eff FAIL. W1-R 't Hooft 6-fermion "
        "vertex FAIL. W2-S I-Ibar valley Jacobian FAIL (conservative/"
        "band-low). The entire multi-instanton+vertex channel for "
        "stabilization CLOSED under conservative Jensen valley bounds. "
        "Would flip to PASS only under BPS saturation (alpha > 1.77).",
    ),
    (
        "N10 B1-WEIGHT-AUDIT-74",
        "W4-A",
        FAIL,
        0.0, 0.0, 0.0,
        2,
        "FAIL: Audited W_B1 = 0.031 vs reference 0.150 (-79%). The two "
        "W_B1 constructions compute DIFFERENT spectral moments — "
        "cannot be substituted. Internal accounting inconsistency "
        "requires resolution. The 0.150 figure is the Peter-Weyl "
        "weight; the 0.031 figure is a different projection. "
        "Diagnostic outcome: the TRANSIT-PS/W1-A pipeline uses one "
        "convention and W1-G/W1-K another.",
    ),
    (
        "N11 DC-PERMANENCE-74",
        "W4-B",
        FAIL,
        0.0, 0.0, 0.0,
        2,
        "FAIL: dc_fraction(12-cell) = 0.04627 outside INFO window "
        "[0.10, 0.30]. Decay ~ N_cells^{-1.26} super-linear (4-cell "
        "0.204 -> 8-cell 0.139 -> 12-cell 0.046). The S73B 20% DC "
        "component is NOT a structural constant of the Josephson "
        "fabric -- it is finite-size diagonal-ensemble residue in "
        "the 4-cell cluster. Any framework argument that cited ~20% "
        "DC as universal non-propagating fraction must be reframed.",
    ),

    # ========================================================
    # LEVEL 3 — MEDIUM (S73B)
    # ========================================================
    (
        "N12 DEGENERACY-LIFT-ALPHA-S-74",
        "W4-C",
        PASS,
        0.0, 0.0, 0.0,
        3,
        "PASS (via observable-scale metric): P_s^{mode}(k)/P_s^{branch}"
        "(k) = 0.9985 +/- 3e-16 across 201 k-values (k-independent to "
        "machine precision). alpha_s structurally IDENTICAL between "
        "mode-level and branch-level 8-mode vs 3-branch groupings. "
        "No hidden mode dependence. Naive rel_diff 19.7% is denominator "
        "pathology (both |alpha_s|~1e-14). Consistency test passes.",
    ),
    (
        "N13 GGE-BISPECTRUM-74",
        "W4-D",
        PASS,
        0.0, 0.0, 0.0,
        3,
        "PASS: f_NL^{equil} = 0.853526 in [0.6, 1.1]. 0.06% high vs "
        "S70 target 0.853. 0.57 sigma from Planck 2019 best-fit -26. "
        "Senatore-Zaldarriaga (85/324)(1/c_s^2 - 1) exact with "
        "c_s = c_BLV = 0.484875 from spectral action stiffness. "
        "Not a Planck-sensitivity discriminant but a sub-permille "
        "structural consistency between S67, S70, S74. A detection "
        "|f_NL^{equil}|>50 would falsify.",
    ),
    (
        "N14 BAYESIAN-FUNCTIONAL-74",
        "W2-I (F-STAR-JOINT-74)",
        FAIL,
        0.0, 0.0, 0.0,
        3,
        "FAIL (decisively): W2-I 4-parameter joint fit yields "
        "chi^2/dof = 67.9 >> 3. Best-fit category-4-locked on constant "
        "c_0 = 0.9629 but with n_s = 0.9991 (8.15 sigma above Planck). "
        "Frustration triangle is now a STRUCTURAL WALL in the 4-"
        "dimensional simplex. The spectral functional cannot be "
        "Bayesian-fit to observations — it is UV data that must be "
        "determined by consistency or dynamics, not optimization.",
    ),
    (
        "N15 MODULUS-DECAY-74",
        "W4-E",
        PASS,
        0.0, 0.0, 0.0,
        3,
        "PASS: T_rh = 1.37e13 MeV = 1.37e10 GeV, twelve orders of "
        "magnitude above the BBN floor (1 MeV). Modulus decay via "
        "instanton-mediated gauge field production is a consistent "
        "reheating channel. IMPORTANT: this PASS is CONDITIONED on "
        "the modulus actually reaching a non-relativistic state — "
        "a condition that is NOT established by N2 FAIL.",
    ),
    (
        "N16 RATIO-OF-RATIOS-PROTECTED-74",
        "(carry: W1-C + W1-M + W4-F)",
        INFO,
        0.0, 0.0, 0.0,
        3,
        "INFO: W1-C confirms R_1 drifts 19.4% at L=7 in Wodzicki "
        "convention; R_3 drifts 29%. W1-M establishes R_protected_"
        "fold = 1.128655 canonical at L=3 in project convention, "
        "with only 1.07% drift to L=7 (stronger protection than "
        "S73B claimed). R-family protection is CONVENTION-DEPENDENT: "
        "strong in project SDW convention, weak in Wodzicki "
        "convention. Not uniformly a scheme-independent invariant.",
    ),
    (
        "N17 FRAMEWORK-RESCALE-74",
        "W4-G",
        FAIL,
        0.0, 0.0, 0.0,
        3,
        "FAIL: max drift 7->9 = 72.29% (CC ratio), 30.25% m_H, "
        "12.34% sin^2(M_Z), all above 15% FAIL threshold. PW zeta "
        "sums monotonically DIVERGENT; Gaussian-regulated S_PW "
        "OSCILLATORY (flips sign L=7 -> L=9). log10(CC) drift 0.47% "
        "STABLE — linear metric is FAIL, log metric is PASS. "
        "Sufficient for 120 OOM CC hierarchy bookkeeping; NOT "
        "sufficient for linear absolute predictions. Framework not "
        "converged at L_max <= 9 in linear metric.",
    ),

    # ========================================================
    # TIER 4 — LOW (S73B)
    # ========================================================
    (
        "N18 HIGHER-MOMENT-74",
        "W2-M (R-FAMILY-STABILITY) + W1-C",
        FAIL,
        0.0, 0.0, 0.0,
        4,
        "FAIL: W2-M R-FAMILY-STABILITY-74 FAIL -- |R_i(L=5) - R_i(L=7)| "
        "/ R_i(L=7) exceeds 5% for R_3, and |R_2 - R_1| = 0.196 ~ "
        "0.2 marginal. R-family convergence does NOT extend cleanly. "
        "Higher moment a_8 from W1-C is just N_weighted (not a true "
        "Seeley-DeWitt coefficient at d=8). The SDW expansion past "
        "a_4 has no structural meaning in the project convention.",
    ),
    (
        "N19 BA-LIFETIME-FABRIC-74",
        "(not planned in S74)",
        OPEN,
        0.50, 0.04, 0.03,
        4,
        "OPEN: Not planned in S74. Carry from S66 P5. "
        "W1-A TRANSFER-FUNCTION showed that the scale-dependent "
        "physics lives in BCS dressing, not in BA phonon "
        "thermalization per se. Supersession partially in effect.",
    ),
    (
        "N20 OSC-METRIC-74",
        "(not planned in S74 -- methodology)",
        OPEN,
        0.90, 0.02, 0.01,
        4,
        "OPEN: Methodology task, not a physics gate. Deferred.",
    ),
    (
        "N21 VIRTUAL-REFRAME-74",
        "W4-BB + W4-S + W4-AA",
        PASS,
        0.0, 0.0, 0.0,
        4,
        "PASS: W4-AA exit-horizon vocabulary audit PASS (66 updates "
        "proposed across 6 scripts, preserving canonical gate IDs). "
        "W4-S external-comm-reframe PASS (13 instances replaced). "
        "W4-BB virtual-reframe PASS. Framework vocabulary aligned "
        "to constraint-surface methodology. Documentation closure.",
    ),
]


# -----------------------------------------------------------------------------
# NEW items from S74 Wave 1-4 findings (not in S73B table)
# -----------------------------------------------------------------------------
# These are items that S74 raised but did not resolve. They become the
# S75 queue priorities.

new_items = [
    # --- From W1-B FAIL: surviving stabilization channels ---
    (
        "N22 MULTI-INSTANTON-LMAX10-75",
        "W1-B sub-gate (d) surviving channel",
        OPEN,
        0.30, 0.15, 0.10,
        1,
        "NEW: The W1-B sub-gate (d) L_max scan {3,5,7} shows "
        "strict monotonicity in dS/dtau. Multi-instanton sectors "
        "from (p+q)>=8 irreps (requiring L_max>=10) are the sole "
        "surviving substrate-internal stabilization candidate. "
        "Pre-registered: PASS if V_eff minimum appears in [0.45, "
        "0.70] at L_max=10. FAIL if monotonicity persists.",
    ),
    (
        "N23 CROSS-MOMENT-STABILIZATION-75",
        "W1-B + W1-H + W2-Q",
        OPEN,
        0.35, 0.12, 0.08,
        1,
        "NEW: W1-B sub-gate (d) tested only the a_0 cutoff action. "
        "W1-H showed a_2 Einstein sector is structurally zero on "
        "Omega_k. W2-Q showed the sqrt-moment <|lambda|> drifts "
        "19% from L=7 to L=9. The a_4 Yang-Mills sector and the "
        "f*-weighted sqrt-moment sector may carry tau-dependence "
        "that modifies V_eff(tau). Pre-registered: PASS if the "
        "combined a_0 + a_2 + a_4 + f* V_eff has a minimum in "
        "[0.45, 0.70]. Cross-spectral coupling is the remaining "
        "substrate-internal stabilization window.",
    ),
    # --- From W1-F FAIL: effacement channel shortfall ---
    (
        "N24 EFFACEMENT-CHANNEL-REBUILD-75",
        "W1-F FAIL driver",
        OPEN,
        0.40, 0.10, 0.08,
        2,
        "NEW: W1-F GGE-PARTITION-74 FAIL because effacement channel "
        "fraction is 2.82e-4 (2425x below FAIL floor 0.0685). a_2 "
        "channel is overfull (f=0.941) and Leggett underfull "
        "(f=0.059). The three-channel partition needs rebuilding: "
        "either (a) effacement is NOT a_0-type (reassign spectral "
        "carrier), (b) the partition weights are wrong, or (c) the "
        "Omega_Lambda target is not the effacement budget. Gated "
        "by W1-O Noether chain PASS — the thermodynamic w_0 is "
        "secure, so the three-channel fit is about PARTITION not "
        "total.",
    ),
    # --- From W1-G FAIL: A_s closure ---
    (
        "N25 A-S-DISSIPATIVE-CHANNEL-75",
        "W1-G FAIL + W2-H A_s budget closure FAIL",
        OPEN,
        0.40, 0.12, 0.08,
        1,
        "NEW: W1-G Bogoliubov-amplitude A_s gap = +9.47 OOM (worse "
        "than baseline). W2-H A_s budget closure delta_OOM^{closure} "
        "= 0.400 < 0.45 FAIL threshold. The Mott+BKT+Thimble "
        "decoherence contributions sum to 0.251 OOM — substantially "
        "SMALLER than the S73A single-route 0.336. A dissipative "
        "channel NOT in {Mott, BKT, Thimble, a_2-sector} is required "
        "to close the A_s gap. Pre-registered: PASS if an additional "
        "channel contributes >= 0.30 OOM with structural derivation.",
    ),
    # --- From W1-J FAIL: w_0 zeta route scheme-sensitivity ---
    (
        "N26 W0-SCHEME-CLOSURE-75",
        "W1-J FAIL (scheme-sensitive)",
        OPEN,
        0.35, 0.08, 0.05,
        3,
        "NEW: W1-J W0-ZETA-74 FAIL. Zeta-regularized modular trace "
        "at s=4 gives w_0 = -0.424 (canonical beta) to -1.67 (stale "
        "omega_L1 beta). The beta = 12.76 M_KK^-1 that recovers "
        "-0.918 does not correspond to ANY framework temperature "
        "scale. The Volovik partition -0.918 remains the sole "
        "canonical route, BUT it is NOT scheme-independent. Pre-"
        "registered: IDENTIFY a physical beta_canonical from first "
        "principles (spectral triple + GGE) that gives w_0 = -0.918 "
        "+/- 0.015.",
    ),
    # --- From W1-K: overlap matrix non-diagonality ---
    (
        "N27 M-OVERLAP-PROPAGATION-75",
        "W1-K + W1-A re-run",
        OPEN,
        0.45, 0.10, 0.06,
        2,
        "NEW: W1-K INFO. The 3x3 overlap matrix has Frobenius "
        "distance 1.58 from identity (91% of max). B1 'acoustic' "
        "branch is 69% tensor after Elliott SU(3)->SO(3), not "
        "scalar. The W1-A transfer function ran on the diagonal "
        "fallback M=I. Pre-registered: PASS if the rerun with full "
        "M (i) produces an enhanced r/scalar ratio prediction AND "
        "(ii) does not disrupt |alpha_s(k_pivot)| < 0.015. FAIL "
        "if the redistribution breaks the W1-A Sasaki-Stewart "
        "closure. INFO if the closure survives but r changes by "
        "< factor 2.",
    ),
    # --- From W2-A INFO: branch n_bar 48.23 ---
    (
        "N28 NBAR-BRANCH-REWEIGHT-75",
        "W2-A INFO",
        OPEN,
        0.35, 0.06, 0.04,
        3,
        "NEW: W2-A branch-resolved <n_bar>_{weighted} = 48.23, in "
        "the INFO band [40, 51.8], NOT matching the canonical N_pair "
        "59.8. This discrepancy suggests the 1:4:3 branch-population "
        "weighting is not the right average. Pre-registered: test "
        "alternative weightings {psi_b from W1-A, n_pair-matched, "
        "Plancherel dim(p,q)^2}.",
    ),
    # --- From W2-C FAIL: entry horizon backreaction ---
    (
        "N29 HFB-ENTRY-BACKREACTION-75",
        "W2-C FAIL",
        OPEN,
        0.30, 0.06, 0.04,
        3,
        "NEW: W2-C HFB-HORIZON-BACKREACTION-74 FAIL. delta_kappa = "
        "0.00487 below 2% INFO floor. The fold-squeeze back-reaction "
        "on the entry-horizon Bogoliubov mixing is 4x smaller than "
        "the assumed S73A value. Pre-registered: re-derive entry-"
        "horizon structure WITHOUT this back-reaction term.",
    ),
    # --- From W2-M FAIL: R-family stability ---
    (
        "N30 R-FAMILY-CONVENTION-75",
        "W2-M FAIL + W1-M PASS",
        OPEN,
        0.50, 0.05, 0.04,
        3,
        "NEW: W2-M FAIL (R-family stability) + W1-M PASS (R_protected "
        "_fold = 1.128655 in project convention). The R-family is "
        "convention-dependent. Pre-registered: test whether ANY "
        "convention gives all three R_1, R_2, R_3 stable to < 5% "
        "drift at L=7. Candidates: (a) project SDW, (b) Wodzicki, "
        "(c) anomaly-derived, (d) zeta at half-integers.",
    ),
    # --- From W2-N FAIL: Leggett vacuum CC ---
    (
        "N31 LEGGETT-VACUUM-REALLOC-75",
        "W2-N FAIL",
        OPEN,
        0.30, 0.05, 0.04,
        3,
        "NEW: W2-N LEGGETT-VACUUM-CC-74 FAIL. chi_Leggett_log10 = "
        "-1.20 vs target +0.47 (delta 1.67, 16.7x tolerance). "
        "Leggett zero-point energy does NOT supply the 0.47 OOM CC "
        "correction. Closes one route for reallocating the CC "
        "budget to substrate-internal zero-point energies.",
    ),
    # --- From W2-O FAIL: R-protected triple-route ---
    (
        "N32 R-PROTECTED-DEFINITIONS-75",
        "W2-O FAIL",
        OPEN,
        0.40, 0.05, 0.04,
        3,
        "NEW: W2-O R-PROTECTED-TRIPLE-74 FAIL with 134% max pairwise "
        "deviation (threshold 3% PASS / 10% FAIL). The three routes "
        "(spectral, curvature, zeta) probe DIFFERENT fabric slices "
        "that cannot be numerically identified. Pre-registered: "
        "identify which route defines R_protected canonically. "
        "W1-M already answers: the project convention (spectral "
        "partial sum) is canonical.",
    ),
    # --- From W3-A INFO: branch kappa wrong sign ---
    (
        "N33 BRANCH-KAPPA-SIGN-75",
        "W3-A INFO",
        OPEN,
        0.30, 0.05, 0.04,
        3,
        "NEW: W3-A BRANCH-KAPPA-74 INFO. delta_kappa_B3B2 = -0.318 "
        "(wrong sign). B3 exceeds B2 by 32% on branch-averaged "
        "kappa_eff, not reduced. Second explicit failure of flat-"
        "band dominance intuition (after W2-A n_bar). Pre-"
        "registered: derive branch-kappa ordering from first "
        "principles using the actual D_K dispersion surface, not "
        "the flat-band approximation.",
    ),
    # --- From W3-B PASS: T_H consistency ---
    (
        "N34 T-H-KAPPA-BIFURCATION-75",
        "W3-B PASS + W3-E FAIL",
        OPEN,
        0.40, 0.04, 0.03,
        3,
        "NEW: W3-B PASSES (2*pi*T_H = kappa_entry_v2 at machine "
        "precision); W3-E FAILS (T_entry from D_K first principles "
        "differs by 4420x). Two routes to T_entry give different "
        "numbers. Pre-registered: identify which route defines "
        "T_entry canonically. W3-B + group-velocity route is "
        "kinematic; W3-E structural spectral c_spec is the "
        "spectral-triple native definition.",
    ),
    # --- From W3-D INFO: Josephson overlap F on CG(24) ---
    (
        "N35 F-OVERLAP-DEFINITION-75",
        "W3-D INFO",
        OPEN,
        0.45, 0.04, 0.03,
        3,
        "NEW: W3-D GS-OVERLAP-CG24-74 INFO. F_1j = 0.404 PASSES "
        "band but CG(24)-corrected definitions span [0.256, 0.930] "
        "(3.6x spread). Ollivier curvature kappa_LLY(CG24) = +1/3 "
        "(POSITIVE), overturning the S73A assumption of negative "
        "curvature. Pre-registered: reconcile F definitions on "
        "positive-curvature 6-regular graph.",
    ),
    # --- From W3-G INFO: Page curve consistency ---
    (
        "N36 PAGE-CURVE-SHAPE-75",
        "W3-G INFO",
        OPEN,
        0.50, 0.03, 0.02,
        4,
        "NEW: W3-G ISLAND-LEFSCHETZ-CONSISTENCY-74 INFO. Max rel "
        "dev = 20.8% at k=3; peak matches exactly; saturation "
        "matches to 2%. Second-order bipartition-geometry difference. "
        "Not a failure but a diagnostic of the bipartition manifold.",
    ),
    # --- From W3-J FAIL (marginal): modular w_a ---
    (
        "N37 MODULAR-WA-REFINED-75",
        "W3-J FAIL (marginal)",
        OPEN,
        0.45, 0.06, 0.04,
        3,
        "NEW: W3-J MODULAR-WA-74 FAIL marginal. w_a = +0.162 with "
        "distance 0.012 (8.1%) above FAIL threshold 0.15. w_a is "
        "OPPOSITE in sign to DESI DR3 DR2 trend. The conservative "
        "sensitivity scan drops to +3.5e-3 if dw_0/dtau picks up "
        "another factor of eps_H. W1-B FAIL (modulus runaway) "
        "favors the O(eps_H^2) reading. Pre-registered: determine "
        "whether Z(tau) response is O(eps_H) or O(eps_H^2).",
    ),
    # --- From W3-K INFO: PS-threshold m_H extension ---
    (
        "N38 PS-M-H-BOUNDARY-75",
        "W3-K INFO",
        OPEN,
        0.40, 0.05, 0.03,
        3,
        "NEW: W3-K PS-THRESHOLD-EXTENDED-M-H-74 INFO (structurally "
        "informative boundary case). m_H^{ext} = 131.83 GeV, 5.38% "
        "off — sits BETWEEN INFO(5%) and FAIL(10%) thresholds. "
        "Gauge module extension 173->775 does NOT change m_H because "
        "spectral moments and Dynkin indices are bimodule-invariant. "
        "Closes the 'gauge module extension modifies m_H' route.",
    ),
    # --- W3-M heterotic-LR FAIL ---
    (
        "N39 HETEROTIC-C2-METRIC-75",
        "W3-M FAIL",
        OPEN,
        0.35, 0.06, 0.04,
        3,
        "NEW: W3-M HETEROTIC-LR-74 sub-gate (A) FAIL. Fitted "
        "lambda_3 = -25.15 structurally negative in both MSbar and "
        "on-shell schemes, violating Riemannian metric positivity "
        "requirement of Paper 13 Sec 5. The 5-input-to-3-unknown "
        "system is NUMERICALLY consistent (0.52% error, e^2/g_s "
        "round-trip exact) but the resulting metric is indefinite. "
        "Pre-registered: find alternative route to sin^2 compatible "
        "with positive-definite C^2 Higgs metric.",
    ),
    # --- From W3-L PASS: (n_s, w_0) joint ---
    (
        "N40 NS-W0-JOINT-SIGMA-75",
        "W3-L PASS (conservative)",
        OPEN,
        0.60, 0.04, 0.02,
        3,
        "NEW: W3-L NS-W0-JOINT-74 PASS (conservative sigma(w_0) = "
        "0.06). All 3 DR3 scenarios inside 2-sigma ellipse. Under "
        "tighter sigma(w_0) = 0.02, Scenario C would FAIL. Pre-"
        "registered: determine canonical sigma(w_0) from first "
        "principles. Depends on N26 (scheme closure).",
    ),
    # --- From W3-O INFO/PASS: soft hair FDM ---
    (
        "N41 SOFT-HAIR-N-CELLS-CALIBR-75",
        "W3-O INFO/PASS",
        OPEN,
        0.55, 0.04, 0.03,
        3,
        "NEW: W3-O SOFT-HAIR-FDM-74 INFO at N_cells=32 (R_soft/"
        "0.27 = 12.15) just above PASS upper bound 10; CG(24) "
        "cross-check at N_cells=24 PASSES (8.19). Pre-registered: "
        "determine canonical N_cells for the cosmological R-G "
        "sector count.",
    ),
    # --- From W3-N PASS: Lefschetz winding ---
    (
        "N42 LEFSCHETZ-WINDING-STRUCTURAL-75",
        "W3-N PASS",
        PASS,
        0.0, 0.0, 0.0,
        4,
        "PASS: W3-N LEFSCHETZ-MEASURE-FACTORIZATION-74 PASS. "
        "Dominant winding n* = 60 = int(N_pair). Single-saddle "
        "approximation exact to 26,000 orders of magnitude. Gaussian "
        "parabola vertex at N_pair = 59.8 exactly. Added to "
        "permanent structural theorem list.",
    ),
    # --- From W1-H PASS: flatness ---
    (
        "N43 FLATNESS-STRUCTURAL-THEOREM",
        "W1-H PASS",
        PASS,
        0.0, 0.0, 0.0,
        4,
        "PASS: W1-H FLATNESS-FROM-A2-74 PASS. |Omega_k| = 0 "
        "structurally, independent of H_0. Theorem proven via "
        "three ingredients: (i) SU(3) bi-invariance -> spatial "
        "constant curvature, (ii) [J,D_K]=0 block-diagonal, "
        "(iii) only the 6k/a^2 term in a_2 couples to 3-slice "
        "intrinsic curvature. Added to permanent theorem list.",
    ),
    # --- From W2-P PASS: A-tensor correction ---
    (
        "N44 A-TENSOR-CORRECTION-STRUCTURAL",
        "W2-P PASS",
        PASS,
        0.0, 0.0, 0.0,
        4,
        "PASS: W2-P A-TENSOR-CORRECTION-74 PASS by 116 OOM. "
        "Max fractional A-tensor correction to CORE quantities "
        "= 1.86e-118. eps_AT = (H_0/M_KK)^2 = 3.75e-118. Flat-base "
        "approximation justified at the fold to 1 part in 10^116. "
        "Confirms direct-product limit approximation structural.",
    ),
    # --- From W1-O PASS: Noether chain ---
    (
        "N45 NOETHER-CHAIN-STRUCTURAL",
        "W1-O PASS",
        PASS,
        0.0, 0.0, 0.0,
        4,
        "PASS: W1-O NOETHER-CHAIN-VERIFICATION-74 PASS. All 5 "
        "steps + w_0 recovery verify to 0.084% (inside 0.5% "
        "bracket). Gibbs-Duhem identity E + PV = TS + mu*N "
        "holds to machine zero. Volovik identity P = N - E "
        "re-derived from thermodynamics, not postulated. w_0 "
        "algebraically anchored to -0.918 independent of the "
        "three-channel W1-F partition.",
    ),
    # --- From W3-C PASS: QCD opening ---
    (
        "N46 ALPHA-S-INSTANTON-STRUCTURAL",
        "W3-C PASS",
        PASS,
        0.0, 0.0, 0.0,
        4,
        "PASS: W3-C QCD-OPENING-74 PASS on both gravity and kerner "
        "routes. |alpha_s^{inst} - alpha_s^{pert}| / alpha_s^{pert} "
        "< 0.10. 1-instanton correction is small at tau > 0.48 "
        "where kappa falls below 1 (topological obstruction "
        "releases). Confirms Region II QCD is well-defined.",
    ),
    # --- From W1-N PASS: multi-cell Plancherel integrability ---
    (
        "N47 PLANCHEREL-INTEGRABILITY-STRUCTURAL",
        "W1-N PASS",
        PASS,
        0.0, 0.0, 0.0,
        4,
        "PASS: W1-N MULTI-CELL-PLANCHEREL-74 PASS. r_pooled_global "
        "= 0.4220 < 0.45. Ordered Veil intact on pooled D_K "
        "spectrum across 10 PW irreps at L_max=3. Integrability "
        "confirmed at Poisson level, consistent with W3-B single-"
        "sector <r>=0.4044 and W3-A three-cell cross-check.",
    ),
    # --- From W1-L PASS: HP4 regime ---
    (
        "N48 HP4-BARE-DECISION",
        "W1-L PASS",
        PASS,
        0.0, 0.0, 0.0,
        4,
        "PASS: W1-L HP4-REGIME-74 PASS. BARE D_K decision with "
        "confidence 0.95, 3 supporting args. Unblocks W2-K HP4-"
        "PAIRING canonical input. K-homology invariance + Paper 10 "
        "locally bounded perturbations + L_max robustness converge.",
    ),
    # --- From W2-F INFO: refined Mott ---
    (
        "N49 MOTT-REFINED-PARTITION-75",
        "W2-F INFO",
        OPEN,
        0.40, 0.05, 0.03,
        3,
        "NEW: W2-F MOTT-REFINED-CG24-74 INFO. delta_OOM_Mott = "
        "0.1411 in INFO band [0.10, 0.40] but below PASS [0.18, "
        "0.28]. C^2 structurally zero. 2.38x smaller than S73A "
        "Hawking workshop baseline 0.336. The partition into "
        "orthogonal phase channels (W2-F Mott + W2-G BKT = 0.251) "
        "reduces the S73A single-route closure budget, directly "
        "feeding into N25 (A_s dissipative channel).",
    ),
    # --- From W2-H FAIL: A_s budget closure driver ---
    (
        "N50 A-S-SHORTFALL-STRUCTURAL",
        "W2-H FAIL",
        OPEN,
        0.40, 0.08, 0.05,
        1,
        "NEW: W2-H A-S-BUDGET-CLOSURE-74 FAIL. delta_OOM^{closure} "
        "= 0.400 < 0.45 FAIL threshold. Residual gap 0.316 OOM "
        "vs target 0.716. Against W1-G post-computation 9.47 OOM "
        "baseline, residual is 9.07 OOM excluding PW correction. "
        "This is a LEVEL-1 gap — no single surviving S73A "
        "channel closes it. Major S75 priority. Gated by N25 "
        "(dissipative) and N27 (overlap matrix).",
    ),
]


# -----------------------------------------------------------------------------
# Assemble final table
# -----------------------------------------------------------------------------
all_items = updates_s73b + new_items

item_ids = [t[0] for t in all_items]
s74_sources = [t[1] for t in all_items]
statuses = [t[2] for t in all_items]
p_pass_arr = np.array([t[3] for t in all_items], dtype=float)
dp_up_arr = np.array([t[4] for t in all_items], dtype=float)
dp_down_arr = np.array([t[5] for t in all_items], dtype=float)
tier_arr = np.array([t[6] for t in all_items], dtype=int)
notes = [t[7] for t in all_items]

# Compute EVOI
evoi_arr = np.array(
    [evoi(p, u, d) for p, u, d in zip(p_pass_arr, dp_up_arr, dp_down_arr)]
)

# -----------------------------------------------------------------------------
# Gate verdict
# -----------------------------------------------------------------------------
n_s73b_updated = len(updates_s73b)  # (local)
n_new_s74 = len(new_items)  # (local)
n_resolved_pass = sum(1 for s in statuses if s == PASS)  # (local)
n_resolved_fail = sum(1 for s in statuses if s == FAIL)  # (local)
n_info = sum(1 for s in statuses if s == INFO)  # (local)
n_open = sum(1 for s in statuses if s == OPEN)  # (local)

# Gate: PASS if all 21 S73B items updated AND new items added from S74
gate_s73b_all_updated = n_s73b_updated == 21  # (local)
gate_new_items_added = n_new_s74 >= 5  # (local)
gate_pass = gate_s73b_all_updated and gate_new_items_added  # (local)

# -----------------------------------------------------------------------------
# Top-5 S75 priorities (OPEN items sorted by EVOI descending)
# -----------------------------------------------------------------------------
open_mask = np.array([s == OPEN for s in statuses])
open_evoi = evoi_arr.copy()
open_evoi[~open_mask] = -1.0  # exclude non-open from sorting
top5_idx = np.argsort(-open_evoi)[:5]
top5_ids = [item_ids[i] for i in top5_idx]  # (local)
top5_evoi = [float(open_evoi[i]) for i in top5_idx]  # (local)
top5_notes = [notes[i] for i in top5_idx]  # (local)

# -----------------------------------------------------------------------------
# Save data
# -----------------------------------------------------------------------------
outpath = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "s74_evoi_recalibration.npz",
)

np.savez(
    outpath,
    item_ids=np.array(item_ids, dtype=object),
    s74_sources=np.array(s74_sources, dtype=object),
    statuses=np.array(statuses, dtype=object),
    p_pass=p_pass_arr,
    delta_p_up=dp_up_arr,
    delta_p_down=dp_down_arr,
    evoi=evoi_arr,
    tier=tier_arr,
    notes=np.array(notes, dtype=object),
    top5_ids=np.array(top5_ids, dtype=object),
    top5_evoi=np.array(top5_evoi, dtype=float),
    gate_pass=gate_pass,
    n_s73b_updated=n_s73b_updated,
    n_new_s74=n_new_s74,
    n_resolved_pass=n_resolved_pass,
    n_resolved_fail=n_resolved_fail,
    n_info=n_info,
    n_open=n_open,
)

# -----------------------------------------------------------------------------
# Print summary
# -----------------------------------------------------------------------------
print("=" * 70)
print("S74 W4-HH EVOI RECALIBRATION SUMMARY")
print("=" * 70)
print(f"S73B items updated:     {n_s73b_updated} / 21")
print(f"New items added:        {n_new_s74}")
print(f"Total items in table:   {len(all_items)}")
print()
print(f"Status distribution:")
print(f"  RESOLVED-PASS:  {n_resolved_pass}")
print(f"  RESOLVED-FAIL:  {n_resolved_fail}")
print(f"  INFO:           {n_info}")
print(f"  OPEN:           {n_open}")
print()
print(f"Gate verdict: {'PASS' if gate_pass else 'FAIL/INFO'}")
print(f"  21/21 S73B items updated: {gate_s73b_all_updated}")
print(f"  New items added (>=5):    {gate_new_items_added} ({n_new_s74})")
print()
print("TOP-5 S75 PRIORITIES (by EVOI descending):")
for rank, (id_, ev) in enumerate(zip(top5_ids, top5_evoi), start=1):
    print(f"  {rank}. {id_}  EVOI = {ev:.4f}")
print()
print(f"Data written: {outpath}")
print()
print("S73B CARRY-FORWARD CLOSURES (S74 resolutions):")
closures = [(i, s, n) for i, s, n in zip(item_ids[:21], statuses[:21], s74_sources[:21])]
for i, s, src in closures:
    marker = "*" if s in (PASS, FAIL) else (" " if s in (INFO,) else " ")
    print(f"  [{s:15s}] {i} <- {src}")
print()
print("NEW S74 ITEMS (for S75 queue):")
for i, s, src, ev in zip(
    item_ids[21:], statuses[21:], s74_sources[21:], evoi_arr[21:]
):
    print(f"  [{s:15s}] {i}  (EVOI={ev:.3f})  <- {src}")
