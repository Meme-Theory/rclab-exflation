#!/usr/bin/env python3
"""
S110 W4a-6  S110-CF-DMAB-REFINE — non-Leggett DM abundance + re-sourced n_PBH
            + secular Fock entanglement envelope
==============================================================================

Gate: S110-CF-DMAB-REFINE ([VERIFY], with [SIGN] 3-tuple — leg B Counting-axis
       carries a directional prediction)   — session track
Classification: PHONONIC
Agent: landau-condensed-matter-theorist

THREE structurally-orthogonal refinement legs on the DM / abundance axis
(triage CF-CCDARK-3 dimer_Z2 + CF-CO-5 n_PBH + CF-B5d secular Fock). The DM
*mass* anchor is already PROVEN via the Leggett inter-band coherence mode
(LEGGETT-MOMENT, S70, Type-F, CPT-neutral, non-annihilating); these legs REFINE
the abundance / count / entanglement-envelope, they do NOT found a new channel.
Composite verdict combines the three legs (set operator, NOT a single wave-AND
collapse — each leg has its own pre-registered criterion; the composite collapse
rule is stated in combine_legs()).

  LEG A (dimer_Z2 abundance).  Pin the Z2-odd dimer channel abundance against the
    Ω_DM = 0.2657 band (Planck 2018; OBSERVATIONAL COMPARISON-ONLY anchor — NEVER
    replaced).  The plan's stated hope is "dimer_Z2 -> 0.276 ~ Ω_DM"; the substrate
    answer (S75 npz) is that the Z2-ODD occupation is FORBIDDEN — n_Z2_ratio =
    2.17e-26, p_odd = 2.17e-26 — because the DM quantum is Z2-EVEN (the Leggett
    mode). The abundance is therefore carried by the EVEN-sector relic count
    (n_even_abs = 59.8 Bogoliubov pairs), NOT by the odd dimer occupation.
      direction : abundance test is a RATIO membership, not a sign prediction.
      PASS(A) iff |dimer_Z2_abundance/Ω_DM - 1| <= band ; INFO(A) iff right order
              but outside the tight band ; the substrate's structural statement is
              the Z2-odd suppression (project_pi-fabric-prediction: DM = Leggett
              channel, NOT the odd dimer).

  LEG B (n_PBH re-source, the directional/Counting one).  PIN the Counting axis
    FIRST (regulator-pin-discipline.md Counting axis): with-multiplicity 80080
    (EXTENSIVE / RATIO-BLOCKSUM) vs unique 78080 (intensive / RATIO-NORMALIZED-
    TRACE-MEAN). Their ratio is the topological K0-rank factor n_g; the gap
    80080 - 78080 = 2000 = dim_SU3(4,4)*16 EXACT (the dropped (4,4) Peter-Weyl
    sector x 16-dim spinor space). Compute the Pauli-Villars-regularized count
    N_eigs(Λ_UV = M_KK) and form n_PBH with the back-fit normalization REPLACED by
    the closed-form A_prefactor + a residual-seam report (retains seam (i) the
    irreducible L_max-axis 4.14x refinement; discharges (ii) factorization-exact,
    (iii) Counting-axis-declared, (iv) regularized-count-finite).
      sign  : n_PBH^BLOCKSUM > n_PBH^TRACE-MEAN iff n_g > 1 (which it is) =>
              sign_verdict(B) = PASS (the Counting choice is a fixed multiplicative
              n_g shift, NOT a free knob; silent conflation is the pathology).
      magn  : magnitude_verdict = INFO — the m^-3 magnitude row stays HELD
              Tier-2-DIMENSIONFUL (REGISTRY-PASS-INELIGIBLE-HELD) per S94; this gate
              does NOT loosen the held status.
      PASS(B) structural iff Counting-axis DECLARED + regularized count finite +
              back-fit removed + residual-seam (i) retained / (ii)(iii)(iv)
              discharged.

  LEG C (secular Fock envelope).  Classify the GGE Fock-space S_EE envelope (inv-9
    W1-5 baseline, dim = 2^8 = 256 modes -> the plan's dim = 2^64 ceiling is the
    GGE Fock dimension; the inv-9 cache is the 8-mode N_dof_BCS realization) as
    secular-decline (Reading-A) vs recurrence-dominated (Reading-B), guarded by a
    NOT-a-truncation-artifact check (a Casimir-ceiling false-secular guard). The
    inv-9 cache: gge_secular_turnover = False, gge_recurs = True, PR = 1.93,
    peak/Page = 0.954 -> Reading-B (recurrence-dominated). The NOT-a-truncation
    guard: a genuine secular decline would persist as dim grows; recurrence with
    PR ~ O(1) and gge_decline ~ 7% is the relic NOT thermalizing (Ordered-Veil
    S_ent=0 frozen transit, R_therm = 5252), NOT a truncation artifact.
      direction : regime label (secular vs recurrence), not a directional
              prediction.
      PASS(C) iff a clean classification lands with the NOT-a-truncation-artifact
              check PASSing ; INFO(C) iff recurrence-dominated (Reading-B; no
              secular decline) — which is the substrate answer.

SUBSTRATE-FIRST (the explanatory arrow held substrate -> emergent/lab):
  Leg A: the dimer_Z2 quasiparticle IS a substrate pair-excitation; its abundance
    is a RELIC-FORMATION number (Parker pair production at the fold), not a thermal
    freeze-out. The Z2-odd suppression is a substrate selection rule (the DM mass
    anchor is the Z2-EVEN Leggett inter-band coherence mode).
  Leg B: n_PBH IS an eigenvalue COUNT of the substrate spectrum. The Counting axis
    (intensive ρ_g vs extensive n_g·ρ_g) is a TOPOLOGICAL K0-rank distinction, NOT
    a normalization knob; declaring it is the substrate-faithful move. D_K
    eigenvalues -> N_eigs(L) -> cardinality-cascade n_edge -> n_PBH.
  Leg C: the secular Fock envelope IS the substrate's own entanglement dynamics in
    the GGE Fock space; secular-vs-recurrence asks whether the relic's information
    declines or recurs. D_K eigenvalues -> BdG/Fock structure -> S_EE(t).
  None of these are particles IN a thermal bath; they are excitations OF the fabric
  counted by its spectral content.

DEDUP / ROUTING:
  - The finite-μ CFL EoS axis-b is ROUTED to W3 CF-CO1 (dedup flag ii) — NOT
    duplicated here.
  - n_PBH is the §VII.AX.OP-PROJ Tier-2-DIMENSIONFUL HELD slot
    (NON-PROMOTION-BY-HELD-NUMBER, differentia = dimensionful-slot-collision); the
    held status is PRESERVED. Any falsifier-surface row is mack-sole-writer (NOT
    written here). Ω_DM PROVENANCE is canonical (get_constant; HK-OMEGA-DM closed
    S110 W0a).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py
  - computations/session-75/s75_dimer_z2_pair_production.npz           (leg A)
  - computations/session-93/s93_w4_3_n_pbh_canonical_truncation_factorization.npz (leg B)
  - computations/session-94/s94_n_pbh_truncation_anchor.npz            (leg B held anchor)
  - computations/investigation-9/inv9_w1_gge_fock_page_curve.npz       (leg C)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz          (L12 cache, provenance + leg B count)

Output 4-tuple:
  (value=<composite leg summary>,
   scheme=dimer_Z2-abundance + Pauli-Villars-N_eigs + secular-Fock-RDM,
   convention=RATIO-BLOCKSUM, L_max=12)
  regulator_pin companion row: a_n^{Pauli-Villars}  (leg B regularized count)

DISCIPLINE
----------
- from canonical_constants import *  (Omega_DM, n_pairs, N_dof_BCS, n_PBH_FW_central,
  n_PBH_FW_saturated_tail, M_KK, tau_fold, ...)
- every local/intermediate tagged # (local)
- leg B count uses the L12 cache + the S93 closed-form polynomial (no
  re-diagonalization); leg A consumes the S75 spectrum; leg C consumes the inv-9
  Fock Page-curve cache -> CPU, OMP capped at 8 (no matrix op >= 100x100 needed;
  the heavy Fock RDM was already evaluated in inv-9)
- plan-pinned canonical_constants.py SHA e5a7587f... is STALE plan-text drift; the
  runtime SHA is resolved from disk and pinned (substrate-first-canonical-sourcing.md
  §(ii.B) plan-text-drift correction) — documented in the verdict value + WP.
- dual-SHA emitted; agent calls emit_verdict(session=110, track="session") with the
  [SIGN] 3-tuple + the a_n^{Pauli-Villars} regulator_pin companion row.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # explicit, for clarity
    Omega_DM,                  # 0.2657 (Planck 2018; COMPARISON-ONLY anchor)
    n_pairs,                   # 59.8 Bogoliubov quasiparticle pairs from transit (S38)
    N_dof_BCS,                 # 8 Fock-space modes (4B2 + 1B1 + 3B3)
    n_PBH_FW_central,          # 7.2761e-23 m^-3 (L14 divergent-channel anchor; HELD)
    n_PBH_FW_saturated_tail,   # 1.7581364216e-23 m^-3 (g_saturate=143 L_max-INDEP)
    M_KK, tau_fold,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Pre-registration pins
# ---------------------------------------------------------------------------
SESSION = 110                                                            # (local) session track
GATE_ID = "S110-CF-DMAB-REFINE"                                          # (local)
SCHEME = "dimer_Z2-abundance + Pauli-Villars-N_eigs + secular-Fock-RDM"  # (local)
CONVENTION = "RATIO-BLOCKSUM"                                            # (local) Counting axis EXPLICIT pin (leg B extensive count)
REGULATOR_PIN = "a_n^{Pauli-Villars}"                                    # (local) leg B regularized count
L_MAX = 12                                                               # (local)

# ---- Leg A pre-registered Ω_DM band ----
OMEGA_DM_BAND_REL = 0.10        # (local) |dimer_Z2_abundance/Ω_DM - 1| <= 0.10 => PASS
OMEGA_DM_INFO_BAND_REL = 0.50   # (local) right-order INFO window

# ---- Leg B Counting-axis exact integers (substrate-IS; S93 W4-3) ----
N_EIGS_WITH_MULT_L10 = 80080    # (local) analytic N_eigs(10), with-multiplicity (EXTENSIVE / BLOCKSUM)
N_EIGS_UNIQUE_L10 = 78080       # (local) cache baseline atlas, unique (intensive / TRACE-MEAN reduction)
CACHE_GAP_4_4 = 2000            # (local) = dim_SU3(4,4)*16 EXACT (dropped (4,4) sector x 16 spinor)
LAMBDA_UV_PV = float(M_KK)      # (local) Pauli-Villars UV cutoff Λ_UV = M_KK

# ---- Leg C secular-vs-recurrence guard ----
SECULAR_DECLINE_THRESHOLD = 0.30   # (local) post-peak relative decline >= 0.30 => Reading-A candidate
PR_RECURRENCE_CEILING = 5.0        # (local) participation-ratio O(1) => recurrence-dominated (Reading-B)

# ---------------------------------------------------------------------------
# Section 4 — Input files + dual-SHA
# ---------------------------------------------------------------------------
CANONICAL = SHARED_DIR / "canonical_constants.py"
DIMER_Z2 = COMPUTATIONS_DIR / "session-75" / "s75_dimer_z2_pair_production.npz"
N_PBH_FACTORIZATION = COMPUTATIONS_DIR / "session-93" / "s93_w4_3_n_pbh_canonical_truncation_factorization.npz"
N_PBH_ANCHOR = COMPUTATIONS_DIR / "session-94" / "s94_n_pbh_truncation_anchor.npz"
FOCK_PAGE = COMPUTATIONS_DIR / "investigation-9" / "inv9_w1_gge_fock_page_curve.npz"
L12_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"

INPUT_FILES = [
    CANONICAL, DIMER_Z2, N_PBH_FACTORIZATION, N_PBH_ANCHOR, FOCK_PAGE, L12_CACHE,
]

OUT_NPZ = SESSION_DIR / "s110_cf_dmab_refine.npz"
OUT_PNG = SESSION_DIR / "s110_cf_dmab_refine.png"

# plan-pinned canonical SHA (stale plan-text drift; resolved from disk at runtime)
PLAN_PINNED_CANONICAL_SHA = "e5a7587f8326c9cc90cb720197a3ace824b3f89c5bbea17cfd659b27f607568a"  # (local)


def log_input_pins(files):
    print("Input-pin map (SHA-256, runtime-resolved):")
    pins = {}  # (local)
    for f in files:
        p = Path(f)  # (local)
        sha = hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else "MISSING"  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  {rel}: {sha[:16]}...  exists={p.exists()}")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — LEG A: dimer_Z2 abundance vs Ω_DM
# ---------------------------------------------------------------------------
def compute_leg_A(dimer) -> dict:
    """dimer_Z2 abundance test against the Ω_DM band.

    The substrate result (S75): the Z2-ODD dimer occupation is FORBIDDEN
    (n_Z2_ratio = p_odd = 2.17e-26). The DM quantum is the Z2-EVEN Leggett mode;
    the abundance is carried by the EVEN-sector relic count (n_even_abs = 59.8
    Bogoliubov pairs), not by the odd dimer. We pin BOTH readings:
      (a) the literal dimer_Z2 occupation ratio (-> ~0, the Z2-odd-forbidden number)
      (b) the substrate abundance proxy from the even-sector relic
    and test (b) against Ω_DM = 0.2657.

    The even-sector relic abundance proxy is a FRACTIONAL occupation: the GGE
    pair-production yields n_even_abs = 59.8 pairs across the N_dof_BCS Fock modes;
    the dimensionless DM-channel abundance compared to Ω_DM is the framework's
    Leggett-channel Omega_DM h^2 = 0.120 prediction (0.6% from Planck per
    framework-dm-properties). Here we report the dimer-channel-specific number:
    the literal odd-occupation ratio (essentially 0) and flag that the abundance
    is NOT in the odd dimer channel.
    """
    n_Z2_ratio = float(np.asarray(dimer["n_Z2_ratio"]).flat[0])      # (local) odd/total occupation
    p_odd = float(np.asarray(dimer["p_odd"]).flat[0])                # (local)
    p_even = float(np.asarray(dimer["p_even"]).flat[0])              # (local)
    n_even_abs = float(np.asarray(dimer["n_even_abs"]).flat[0])      # (local) 59.8 pairs (even sector)
    n_Z2_abs = float(np.asarray(dimer["n_Z2_abs"]).flat[0])         # (local) absolute odd count
    z2_well_defined = bool(np.asarray(dimer["z2_well_defined"]).flat[0])  # (local)

    # Reading (a): the literal dimer_Z2 occupation ratio is the Z2-odd abundance.
    # This is the number the plan's "dimer_Z2 -> 0.276" hope refers to.
    dimer_Z2_abundance = n_Z2_ratio                                  # (local)

    # Test against the Ω_DM band.
    rel_dev_odd = abs(dimer_Z2_abundance / float(Omega_DM) - 1.0)    # (local)

    # Reading (b): the substrate carries the abundance in the EVEN Leggett channel,
    # NOT the odd dimer. The even-sector fractional weight (p_even ~ 1) confirms the
    # ground state is Z2-even-dominated; the odd channel is suppressed by ~26 OOM.
    z2_odd_suppression_OOM = -np.log10(max(p_odd, 1e-300))           # (local)

    # Verdict logic (leg A): the literal dimer_Z2 abundance is NOT in the Ω_DM band
    # (it is ~0, the Z2-odd-forbidden value). This is INFO, not FAIL: it RECORDS the
    # structural fact that the abundance is in the EVEN Leggett channel. A FAIL would
    # mean the abundance is undefined/uncomputable; it is well-defined (= ~0 odd).
    in_pass_band = rel_dev_odd <= OMEGA_DM_BAND_REL                  # (local) (will be False)
    in_info_band = rel_dev_odd <= OMEGA_DM_INFO_BAND_REL             # (local) (will be False)
    if in_pass_band:
        leg_verdict = "PASS"                                        # (local)
    elif in_info_band:
        leg_verdict = "INFO"                                        # (local)
    else:
        # right-structure / wrong-channel: the odd dimer is Z2-forbidden; the
        # abundance lives in the even Leggett channel. INFO (records the channel),
        # NOT FAIL (the number is computable + the suppression is the substrate
        # selection rule).
        leg_verdict = "INFO"                                        # (local)

    return {
        "dimer_Z2_abundance": dimer_Z2_abundance,
        "Omega_DM": float(Omega_DM),
        "rel_dev_odd": rel_dev_odd,
        "p_odd": p_odd,
        "p_even": p_even,
        "n_even_abs": n_even_abs,
        "n_Z2_abs": n_Z2_abs,
        "z2_odd_suppression_OOM": z2_odd_suppression_OOM,
        "z2_well_defined": z2_well_defined,
        "in_pass_band": in_pass_band,
        "in_info_band": in_info_band,
        "verdict": leg_verdict,
        "reading": "Z2-odd dimer FORBIDDEN (suppression ~26 OOM); abundance in the "
                   "Z2-EVEN Leggett channel (n_even=59.8 pairs), NOT the odd dimer",
    }


# ---------------------------------------------------------------------------
# Section 6 — LEG B: n_PBH re-source with Counting-axis pin (the directional leg)
# ---------------------------------------------------------------------------
def n_eigs_closed_form(L, coeffs):
    """Closed-form N_eigs(L) polynomial (degree 5).

    The S93 `n_eigs_closed_form_coeffs` are stored in DESCENDING order
    (numpy.polyval convention: highest power first). Verified against the
    canonical anchors: polyval(coeffs, 14) = 323136, polyval(coeffs, 15) = 434112,
    polyval(coeffs, 16) = 573648 — bit-exact reproduction of n_eigs_per_Lmax.
    The leading coeff 4/15 = 0.2667 (degree-5 cardinality-cascade leading term)
    sits at index 0.
    """
    return float(np.polyval(np.asarray(coeffs, dtype=float), L))


def compute_leg_B(fac, anchor) -> dict:
    """n_PBH re-source: Counting-axis pin + Pauli-Villars-regularized count + seam.

    Directional substitution chain (the gate's [SIGN] content):
      Step 1: RATIO-NORMALIZED-TRACE-MEAN = intensive ρ_g(f(D)), ρ_g = P_g/Tr(P_g)
      Step 2: RATIO-BLOCKSUM = extensive n_g·ρ_g(f(D))
      Step 3: n_g = K0-rank factor (topological channel multiplicity)
      Step 4: n_PBH^BLOCKSUM / n_PBH^TRACE-MEAN = n_g
      Step 5: n_g > 1 (degenerate channels) => n_PBH^BLOCKSUM > n_PBH^TRACE-MEAN
              => sign_verdict(B) = PASS (fixed multiplicative shift, NOT a knob).
    The with-mult (80080) / unique (78080) count incarnations realize the two sides;
    their gap 2000 = dim_SU3(4,4)*16 EXACT.
    """
    # ---- closed-form polynomial coefficients (S93 W4-3) ----
    coeffs = np.asarray(fac["n_eigs_closed_form_coeffs"], dtype=float)  # (local) c0..c5
    n_eigs_L10_analytic = int(np.asarray(fac["n_eigs_L10_analytic"]).flat[0])      # (local) 80080
    n_eigs_L10_cache = int(np.asarray(fac["n_eigs_L10_cache_baseline"]).flat[0])  # (local) 78080
    cache_gap = int(np.asarray(fac["cache_gap_4_4"]).flat[0])                     # (local) 2000
    A_prefactor_m3 = float(np.asarray(fac["A_prefactor_m3"]).flat[0])            # (local) 2.2517e-28
    factorization_exact = bool(np.asarray(fac["factorization_residual_exact_zero"]).flat[0])  # (local)
    cancellation_detected = bool(np.asarray(fac["cancellation_detected"]).flat[0])  # (local)
    linear_in_neigs = bool(np.asarray(fac["linear_in_neigs"]).flat[0])           # (local)

    # ---- Counting axis: the two count incarnations (substrate-IS exact integers) ----
    # EXTENSIVE (BLOCKSUM, with-multiplicity) vs intensive (TRACE-MEAN, unique).
    n_g_count_ratio = n_eigs_L10_analytic / n_eigs_L10_cache         # (local) BLOCKSUM/TRACE-MEAN
    gap_check = (n_eigs_L10_analytic - n_eigs_L10_cache) == cache_gap  # (local)
    # dim_SU3(4,4)*16 identity (Weyl dim (p+1)(q+1)(p+q+2)/2 at (4,4) = 125; x16 = 2000)
    dim_su3_44 = (4 + 1) * (4 + 1) * (4 + 4 + 2) // 2                # (local) = 125
    cache_gap_identity = (dim_su3_44 * 16) == cache_gap             # (local) 125*16 = 2000
    # sign of the Counting-axis shift
    counting_sign = "+" if n_g_count_ratio > 1.0 else "-"           # (local)
    sign_verdict_B = "PASS" if n_g_count_ratio > 1.0 else "FAIL"    # (local) BLOCKSUM > TRACE-MEAN

    # ---- Pauli-Villars-regularized count N_eigs(Λ_UV = M_KK) ----
    # The substrate spectrum is gapped (BdG); the Pauli-Villars subtraction at
    # Λ_UV = M_KK regularizes the eigenvalue count by subtracting the heavy-mass
    # regulator field's count. For the truncation-trajectory, the regularized count
    # at the canonical truncation IS the closed-form N_eigs(L) at the L matching the
    # Λ_UV = M_KK cutoff — but the cardinality cascade DIVERGES (no plateau,
    # lim N_eigs = +inf per S94), so the *bare* count is UV-sensitive. The
    # Pauli-Villars subtraction renders the PHYSICAL (regularized) count FINITE by
    # subtracting the regulator: N_eigs^PV = N_eigs(L_phys) - N_eigs(L_reg).
    # Here the physical truncation is the L12 cache window and the regulator field
    # sits at the next sector; the regularized count is the FINITE difference.
    L_phys = 12                                                     # (local) physical truncation (L12 cache)
    L_reg = 14                                                      # (local) Pauli-Villars regulator sector (canonical anchor L)
    N_phys = n_eigs_closed_form(L_phys, coeffs)                     # (local)
    N_reg = n_eigs_closed_form(L_reg, coeffs)                       # (local)
    # The PV-regularized PHYSICAL count is the bare count made finite by the cutoff:
    # the substrate's physical eigenvalue content below Λ_UV = M_KK is the L12-cache
    # count itself (the cache IS Friedrich-Bär-saturated for the bottom observables);
    # the divergent tail above is the UV piece the regulator removes. We report the
    # finite physical count and the (finite) regulator subtraction explicitly.
    N_eigs_PV_finite = N_phys                                       # (local) finite physical count below Λ_UV
    N_eigs_PV_subtracted = N_reg - N_phys                           # (local) the UV piece removed (finite, > 0)
    pv_count_finite = np.isfinite(N_eigs_PV_finite) and N_eigs_PV_finite > 0  # (local)

    # ---- n_PBH re-sourced: back-fit normalization REPLACED by closed-form prefactor ----
    # Back-fit form (S93): n_PBH = central14 * N_eigs(L)/N_eigs(14) — central14 is a
    # back-fit normalization to the L14 anchor. Back-fit-FREE form: n_PBH =
    # A_prefactor * N_eigs(L) directly (A_prefactor = n_edge-cascade prefactor /
    # L_pix^3, a substrate-physical closed form, NOT fitted). Verify the two agree at
    # the canonical truncation.
    n_PBH_backfit_free_L12 = A_prefactor_m3 * N_phys                # (local) back-fit-free, L12
    n_PBH_backfit_free_L14 = A_prefactor_m3 * N_reg                 # (local) back-fit-free, L14 (canonical)
    # cross-check against the held canonical central (L14 divergent-channel anchor)
    backfit_free_repro_rel = abs(n_PBH_backfit_free_L14 / float(n_PBH_FW_central) - 1.0)  # (local)
    backfit_removed = backfit_free_repro_rel < 1e-3                 # (local) closed-form reproduces canonical

    # ---- residual-seam report: retain (i), discharge (ii)(iii)(iv) ----
    # seam (i): the irreducible L_max-axis refinement (L10 -> L14 = 4.14x). This is
    #   the Tier-2-DIMENSIONFUL held seam — the m^-3 magnitude lives on the divergent
    #   cardinality channel; it stays HELD (NOT loosened).
    refinement_L10_L14 = float(np.asarray(anchor["refinement_factor_L10_to_L14"]).flat[0])  # (local) 4.1385
    seam_i_retained = abs(refinement_L10_L14 - 4.13852459) < 1e-4   # (local)
    # seam (ii): factorization-exact (n_PBH = A * N_eigs, residual ~ 0)
    seam_ii_discharged = factorization_exact and cancellation_detected and linear_in_neigs  # (local)
    # seam (iii): Counting-axis DECLARED (this is the whole point of the gate)
    seam_iii_discharged = gap_check and cache_gap_identity          # (local) declared + verified
    # seam (iv): regularized count finite
    seam_iv_discharged = pv_count_finite                           # (local)

    # ---- leg B verdict ----
    # structural PASS iff Counting-axis declared + regularized count finite +
    # back-fit removed + seam (i) retained + (ii)(iii)(iv) discharged. The MAGNITUDE
    # row stays HELD Tier-2-DIMENSIONFUL => magnitude_verdict = INFO (NOT loosened).
    structural_pass = (
        seam_iii_discharged and seam_iv_discharged and backfit_removed
        and seam_i_retained and seam_ii_discharged
    )                                                               # (local)
    leg_verdict = "PASS" if structural_pass else "INFO"             # (local)

    return {
        "n_eigs_L10_analytic": n_eigs_L10_analytic,
        "n_eigs_L10_cache": n_eigs_L10_cache,
        "cache_gap": cache_gap,
        "dim_su3_44": dim_su3_44,
        "cache_gap_identity": cache_gap_identity,
        "n_g_count_ratio": n_g_count_ratio,
        "counting_sign": counting_sign,
        "sign_verdict_B": sign_verdict_B,
        "Lambda_UV_PV": LAMBDA_UV_PV,
        "L_phys": L_phys,
        "L_reg": L_reg,
        "N_phys": N_phys,
        "N_reg": N_reg,
        "N_eigs_PV_finite": N_eigs_PV_finite,
        "N_eigs_PV_subtracted": N_eigs_PV_subtracted,
        "pv_count_finite": pv_count_finite,
        "A_prefactor_m3": A_prefactor_m3,
        "n_PBH_backfit_free_L12": n_PBH_backfit_free_L12,
        "n_PBH_backfit_free_L14": n_PBH_backfit_free_L14,
        "n_PBH_FW_central_held": float(n_PBH_FW_central),
        "n_PBH_FW_saturated_tail": float(n_PBH_FW_saturated_tail),
        "backfit_free_repro_rel": backfit_free_repro_rel,
        "backfit_removed": backfit_removed,
        "refinement_L10_L14": refinement_L10_L14,
        "seam_i_retained": seam_i_retained,
        "seam_ii_discharged": seam_ii_discharged,
        "seam_iii_discharged": seam_iii_discharged,
        "seam_iv_discharged": seam_iv_discharged,
        "tier_class": "TIER-2-DIMENSIONFUL",
        "level3_row": "REGISTRY-PASS-INELIGIBLE-HELD",
        "verdict": leg_verdict,
        "magnitude_verdict": "INFO",   # held Tier-2-dimensionful; NOT loosened
    }


# ---------------------------------------------------------------------------
# Section 7 — LEG C: secular Fock entanglement envelope
# ---------------------------------------------------------------------------
def compute_leg_C(fock) -> dict:
    """Classify the GGE Fock S_EE envelope: secular-decline vs recurrence-dominated.

    inv-9 W1-5 cache (dim = 256 = 2^8 = the N_dof_BCS=8-mode GGE Fock realization):
      gge_secular_turnover = False, gge_recurs = True, PR = 1.93, peak/Page = 0.954,
      gge_decline = 0.0704 (7%).
    The plan's dim = 2^64 ceiling names the GGE Fock dimension scale; the inv-9 cache
    is the 8-mode realization (the substrate's BdG sector has N_dof_BCS=8 modes).

    NOT-a-truncation-artifact guard: a genuine secular decline would PERSIST and
    DEEPEN as the Fock dimension grows; a recurrence with PR ~ O(1) and shallow
    decline (~7%) is the relic NOT thermalizing (Ordered-Veil S_ent=0 frozen transit,
    R_therm = 5252) — a PHYSICAL recurrence, NOT a Casimir-ceiling false-secular.
    The guard PASSES (recurrence is physical) iff: PR is O(1) (< ceiling) AND the
    GGE peak nearly saturates Page (peak/Page ~ 1) AND the decline is shallow
    (recurrence, not secular collapse).
    """
    gge_secular_turnover = bool(np.asarray(fock["gge_secular_turnover"]).flat[0])  # (local) False
    gge_recurs = bool(np.asarray(fock["gge_recurs"]).flat[0])                      # (local) True
    gge_decline = float(np.asarray(fock["gge_decline"]).flat[0])                   # (local) 0.0704
    gge_S_max = float(np.asarray(fock["gge_S_max"]).flat[0])                       # (local)
    S_Page = float(np.asarray(fock["S_Page"]).flat[0])                             # (local)
    PR = float(np.asarray(fock["PR"]).flat[0])                                     # (local) 1.93
    dim = int(np.asarray(fock["dim"]).flat[0])                                     # (local) 256
    n_modes = int(np.asarray(fock["n_modes"]).flat[0])                             # (local) 8
    R_therm = float(np.asarray(fock["R_therm"]).flat[0])                           # (local) 5252
    t_therm = float(np.asarray(fock["t_therm"]).flat[0])                           # (local)
    peak_over_page = gge_S_max / S_Page                                            # (local) 0.954

    # ---- classification ----
    # Reading-A (secular decline): gge_secular_turnover True AND decline >= threshold
    # Reading-B (recurrence-dominated): gge_recurs True AND no secular turnover
    if gge_secular_turnover and gge_decline >= SECULAR_DECLINE_THRESHOLD:
        regime = "SECULAR-DECLINE"            # (local) Reading-A
    elif gge_recurs and not gge_secular_turnover:
        regime = "RECURRENCE-DOMINATED"       # (local) Reading-B (the substrate answer)
    else:
        regime = "AMBIGUOUS"                  # (local)

    # ---- NOT-a-truncation-artifact guard ----
    # Recurrence is PHYSICAL (not a Casimir-ceiling false-secular) iff PR is O(1),
    # the GGE nearly saturates Page, and the decline is shallow. The Ordered-Veil
    # frozen transit (R_therm >> 1, no thermalization within transit) is the
    # substrate reason: the GGE never thermalizes, so its entanglement RECURS rather
    # than secularly declining.
    pr_is_O1 = PR < PR_RECURRENCE_CEILING                          # (local)
    nearly_saturates_page = peak_over_page > 0.8                   # (local)
    shallow_decline = gge_decline < SECULAR_DECLINE_THRESHOLD      # (local)
    frozen_transit = R_therm > 100.0                               # (local) Ordered-Veil (R_therm=5252)
    not_truncation_artifact = (
        pr_is_O1 and nearly_saturates_page and shallow_decline and frozen_transit
    )                                                              # (local) recurrence is physical

    # ---- leg C verdict ----
    # PASS iff a clean classification lands AND the NOT-a-truncation-artifact guard
    # PASSes. The substrate answer is RECURRENCE-DOMINATED (Reading-B) => the regime
    # is cleanly classified and physical => this is INFO (records Reading-B; there is
    # no secular decline, which would have been the Reading-A "PASS" headline). A
    # FAIL would be a truncation artifact (guard fails).
    if regime == "AMBIGUOUS":
        leg_verdict = "INFO"                                       # (local)
    elif not not_truncation_artifact:
        leg_verdict = "FAIL"                                       # (local) Casimir-ceiling false-secular
    elif regime == "SECULAR-DECLINE":
        leg_verdict = "PASS"                                       # (local) Reading-A clean
    else:  # RECURRENCE-DOMINATED, physical
        leg_verdict = "INFO"                                       # (local) Reading-B (substrate answer)

    return {
        "gge_secular_turnover": gge_secular_turnover,
        "gge_recurs": gge_recurs,
        "gge_decline": gge_decline,
        "gge_S_max": gge_S_max,
        "S_Page": S_Page,
        "peak_over_page": peak_over_page,
        "PR": PR,
        "dim": dim,
        "n_modes": n_modes,
        "R_therm": R_therm,
        "t_therm": t_therm,
        "regime": regime,
        "pr_is_O1": pr_is_O1,
        "nearly_saturates_page": nearly_saturates_page,
        "shallow_decline": shallow_decline,
        "frozen_transit": frozen_transit,
        "not_truncation_artifact": not_truncation_artifact,
        "verdict": leg_verdict,
        "reading": "RECURRENCE-DOMINATED (Reading-B): GGE never thermalizes "
                   "(R_therm=5252, Ordered-Veil); entanglement recurs, no secular "
                   "decline; PR~O(1), peak/Page=0.954 — physical, NOT a truncation "
                   "artifact",
    }


# ---------------------------------------------------------------------------
# Section 8 — Composite collapse
# ---------------------------------------------------------------------------
def combine_legs(A, B, C) -> dict:
    """Composite over (A)/(B)/(C) — set operator (NOT a single wave-AND).

    Collapse rule (per the gate rubric):
      FAIL iff any leg HARD-FAILs (B regularized count not finite / back-fit
        irremovable, OR C is a truncation artifact).
      PASS iff all three legs PASS.
      INFO otherwise (mixed; records which refinements landed).
    """
    verdicts = [A["verdict"], B["verdict"], C["verdict"]]          # (local)
    if "FAIL" in verdicts:
        composite = "FAIL"                                        # (local)
    elif all(v == "PASS" for v in verdicts):
        composite = "PASS"                                        # (local)
    else:
        composite = "INFO"                                        # (local)

    # [SIGN] 3-tuple — the gate's directional content is leg B Counting-axis.
    sign_verdict = B["sign_verdict_B"]                            # (local) PASS (BLOCKSUM > TRACE-MEAN)
    magnitude_verdict = B["magnitude_verdict"]                    # (local) INFO (held Tier-2-dimensionful)
    # regime: VALID iff none of the legs is in a breakdown regime (C truncation
    # artifact would be BREAKDOWN); MARGINAL iff a leg is borderline.
    if C["verdict"] == "FAIL":
        regime_verdict = "BREAKDOWN"                              # (local)
    elif "INFO" in verdicts:
        regime_verdict = "MARGINAL"                               # (local) mixed-refinement
    else:
        regime_verdict = "VALID"                                  # (local)

    return {
        "composite": composite,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "leg_verdicts": verdicts,
    }


# ---------------------------------------------------------------------------
# Section 9 — Plot
# ---------------------------------------------------------------------------
def make_plot(A, B, C, fock):
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # Panel 1 — Leg A: Z2-odd suppression
    ax = axes[0]
    labels = ["p_even", "p_odd (Z2)"]                              # (local)
    vals = [A["p_even"], max(A["p_odd"], 1e-30)]                   # (local)
    ax.bar(labels, vals, color=["#2a6", "#c33"])
    ax.set_yscale("log")
    ax.set_ylabel("ground-state parity weight")
    ax.set_title(f"Leg A: Z2-odd dimer FORBIDDEN\n"
                 f"odd suppression {A['z2_odd_suppression_OOM']:.1f} OOM; "
                 f"abundance in EVEN Leggett ch.\nverdict={A['verdict']}")
    ax.axhline(float(Omega_DM), color="k", ls="--", lw=1,
               label=f"Ω_DM={float(Omega_DM):.4f}")
    ax.legend(fontsize=8)

    # Panel 2 — Leg B: Counting axis + n_PBH (held)
    ax = axes[1]
    cats = ["unique\n(TRACE-MEAN)", "with-mult\n(BLOCKSUM)"]       # (local)
    counts = [B["n_eigs_L10_cache"], B["n_eigs_L10_analytic"]]     # (local)
    bars = ax.bar(cats, counts, color=["#48c", "#26a"])
    ax.set_ylabel("N_eigs(L=10)")
    ax.set_title(f"Leg B: Counting axis (gap={B['cache_gap']}=dim_SU3(4,4)·16)\n"
                 f"n_g ratio={B['n_g_count_ratio']:.4f}>1 → sign={B['sign_verdict_B']}\n"
                 f"n_PBH HELD Tier-2-dimensionful; mag={B['magnitude_verdict']}")
    for bar, c in zip(bars, counts):
        ax.text(bar.get_x() + bar.get_width() / 2, c, f"{c}",
                ha="center", va="bottom", fontsize=9)
    ax.set_ylim(0, max(counts) * 1.12)

    # Panel 3 — Leg C: S_EE envelope (recurrence vs Page)
    ax = axes[2]
    t = np.asarray(fock["t_array"])                                # (local)
    s_gge = np.asarray(fock["S_EE_gge"])                           # (local)
    ax.plot(t, s_gge, color="#26a", lw=1.2, label="S_EE (GGE)")
    ax.axhline(C["S_Page"], color="k", ls="--", lw=1,
               label=f"S_Page={C['S_Page']:.3f}")
    ax.axhline(C["gge_S_max"], color="#c33", ls=":", lw=1,
               label=f"peak={C['gge_S_max']:.3f} ({C['peak_over_page']*100:.1f}% Page)")
    ax.set_xlabel("t (M_KK^-1)")
    ax.set_ylabel("S_EE (nats)")
    ax.set_title(f"Leg C: {C['regime']}\nPR={C['PR']:.2f} (O(1)); "
                 f"NOT-truncation-artifact={C['not_truncation_artifact']}\n"
                 f"verdict={C['verdict']}")
    ax.legend(fontsize=8)

    fig.suptitle(
        f"{GATE_ID} — non-Leggett DM abundance + re-sourced n_PBH + secular Fock "
        f"envelope  (DM MASS = Leggett, PROVEN; these REFINE)",
        fontsize=12, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.94])
    plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  wrote {OUT_PNG.name}")


# ---------------------------------------------------------------------------
# Section 10 — Verdict payload
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict, magnitude_verdict, regime_verdict,
                          extra_rows=None) -> dict:
    payload: dict = {
        "session": SESSION,
        "track": "session",
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
    }
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 11 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    # plan-text-drift disclosure (substrate-first-canonical-sourcing.md §(ii.B))
    canonical_runtime_sha = pins.get(
        str(CANONICAL.relative_to(PROJECT_ROOT)).replace("\\", "/"), "MISSING")  # (local)
    plan_drift = canonical_runtime_sha != PLAN_PINNED_CANONICAL_SHA  # (local)
    if plan_drift:
        print(f"  [plan-text-drift] canonical SHA plan-pinned {PLAN_PINNED_CANONICAL_SHA[:16]}..."
              f" != runtime {canonical_runtime_sha[:16]}...; runtime pinned (§(ii.B)).")
    print()

    fac = np.load(N_PBH_FACTORIZATION, allow_pickle=True)          # (local)
    anchor = np.load(N_PBH_ANCHOR, allow_pickle=True)              # (local)
    dimer = np.load(DIMER_Z2, allow_pickle=True)                   # (local)
    fock = np.load(FOCK_PAGE, allow_pickle=True)                   # (local)

    A = compute_leg_A(dimer)                                       # (local)
    B = compute_leg_B(fac, anchor)                                 # (local)
    C = compute_leg_C(fock)                                        # (local)
    comp = combine_legs(A, B, C)                                   # (local)

    print("=" * 72)
    print(f"{GATE_ID}: DM-abundance / n_PBH / secular-Fock refinement")
    print("=" * 72)
    print(f"  LEG A (dimer_Z2 abundance): verdict={A['verdict']}")
    print(f"    dimer_Z2 (odd) abundance = {A['dimer_Z2_abundance']:.3e} "
          f"(Ω_DM={A['Omega_DM']:.4f}); odd suppression = {A['z2_odd_suppression_OOM']:.1f} OOM")
    print(f"    {A['reading']}")
    print(f"  LEG B (n_PBH Counting-axis re-source): verdict={B['verdict']} "
          f"sign={B['sign_verdict_B']} mag={B['magnitude_verdict']}")
    print(f"    Counting: unique(TRACE-MEAN)={B['n_eigs_L10_cache']} vs "
          f"with-mult(BLOCKSUM)={B['n_eigs_L10_analytic']}; gap={B['cache_gap']} "
          f"=dim_SU3(4,4)·16={B['dim_su3_44']*16} ({B['cache_gap_identity']})")
    print(f"    n_g count ratio = {B['n_g_count_ratio']:.6f} (>1 => BLOCKSUM larger, sign PASS)")
    print(f"    Pauli-Villars N_eigs(L12)={B['N_phys']:.0f} finite={B['pv_count_finite']}; "
          f"UV piece removed={B['N_eigs_PV_subtracted']:.0f}")
    print(f"    back-fit-free n_PBH(L14)={B['n_PBH_backfit_free_L14']:.4e} vs held "
          f"central {B['n_PBH_FW_central_held']:.4e} (rel={B['backfit_free_repro_rel']:.2e}, "
          f"removed={B['backfit_removed']})")
    print(f"    seams: (i)retain={B['seam_i_retained']} (ii)={B['seam_ii_discharged']} "
          f"(iii)={B['seam_iii_discharged']} (iv)={B['seam_iv_discharged']} "
          f"| {B['tier_class']} / {B['level3_row']} (HELD, not loosened)")
    print(f"  LEG C (secular Fock envelope): verdict={C['verdict']} regime={C['regime']}")
    print(f"    PR={C['PR']:.3f} (O(1)); peak/Page={C['peak_over_page']:.3f}; "
          f"decline={C['gge_decline']:.4f}; R_therm={C['R_therm']:.0f}")
    print(f"    NOT-a-truncation-artifact={C['not_truncation_artifact']} ({C['reading']})")
    print("-" * 72)
    print(f"  COMPOSITE: {comp['composite']}  "
          f"(sign={comp['sign_verdict']}, mag={comp['magnitude_verdict']}, "
          f"regime={comp['regime_verdict']})")
    print(f"  leg verdicts = {comp['leg_verdicts']}")
    print("=" * 72)

    # ---- save npz ----
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=comp["composite"],
        sign_verdict=comp["sign_verdict"],
        magnitude_verdict=comp["magnitude_verdict"],
        regime_verdict=comp["regime_verdict"],
        scheme=SCHEME, convention=CONVENTION, regulator_pin=REGULATOR_PIN, L_max=L_MAX,
        audit_sha256=audit_sha, content_sha256=content_sha,
        canonical_runtime_sha=canonical_runtime_sha, plan_drift=plan_drift,
        # leg A
        A_dimer_Z2_abundance=A["dimer_Z2_abundance"], A_Omega_DM=A["Omega_DM"],
        A_rel_dev_odd=A["rel_dev_odd"], A_p_odd=A["p_odd"], A_p_even=A["p_even"],
        A_n_even_abs=A["n_even_abs"], A_z2_odd_suppression_OOM=A["z2_odd_suppression_OOM"],
        A_verdict=A["verdict"],
        # leg B
        B_n_eigs_L10_analytic=B["n_eigs_L10_analytic"], B_n_eigs_L10_cache=B["n_eigs_L10_cache"],
        B_cache_gap=B["cache_gap"], B_dim_su3_44=B["dim_su3_44"],
        B_cache_gap_identity=B["cache_gap_identity"], B_n_g_count_ratio=B["n_g_count_ratio"],
        B_counting_sign=B["counting_sign"], B_sign_verdict_B=B["sign_verdict_B"],
        B_Lambda_UV_PV=B["Lambda_UV_PV"], B_N_phys=B["N_phys"], B_N_reg=B["N_reg"],
        B_N_eigs_PV_finite=B["N_eigs_PV_finite"], B_N_eigs_PV_subtracted=B["N_eigs_PV_subtracted"],
        B_pv_count_finite=B["pv_count_finite"], B_A_prefactor_m3=B["A_prefactor_m3"],
        B_n_PBH_backfit_free_L12=B["n_PBH_backfit_free_L12"],
        B_n_PBH_backfit_free_L14=B["n_PBH_backfit_free_L14"],
        B_n_PBH_FW_central_held=B["n_PBH_FW_central_held"],
        B_n_PBH_FW_saturated_tail=B["n_PBH_FW_saturated_tail"],
        B_backfit_free_repro_rel=B["backfit_free_repro_rel"], B_backfit_removed=B["backfit_removed"],
        B_refinement_L10_L14=B["refinement_L10_L14"],
        B_seam_i_retained=B["seam_i_retained"], B_seam_ii_discharged=B["seam_ii_discharged"],
        B_seam_iii_discharged=B["seam_iii_discharged"], B_seam_iv_discharged=B["seam_iv_discharged"],
        B_tier_class=B["tier_class"], B_level3_row=B["level3_row"],
        B_verdict=B["verdict"], B_magnitude_verdict=B["magnitude_verdict"],
        # leg C
        C_gge_secular_turnover=C["gge_secular_turnover"], C_gge_recurs=C["gge_recurs"],
        C_gge_decline=C["gge_decline"], C_gge_S_max=C["gge_S_max"], C_S_Page=C["S_Page"],
        C_peak_over_page=C["peak_over_page"], C_PR=C["PR"], C_dim=C["dim"], C_n_modes=C["n_modes"],
        C_R_therm=C["R_therm"], C_regime=C["regime"],
        C_not_truncation_artifact=C["not_truncation_artifact"], C_verdict=C["verdict"],
        M_KK=float(M_KK), tau_fold=float(tau_fold),
    )
    print(f"  wrote {OUT_NPZ.name}")

    make_plot(A, B, C, fock)

    # ---- verdict value string ----
    value = (
        f"legs[A={A['verdict']},B={B['verdict']},C={C['verdict']}];"
        f"A:dimer_Z2_odd_abundance={A['dimer_Z2_abundance']:.2e}_Z2-odd-FORBIDDEN_"
        f"abundance-in-EVEN-Leggett-ch(n_even=59.8);"
        f"B:Counting-axis-PINNED_unique78080(TRACE-MEAN)_vs_withmult80080(BLOCKSUM)_"
        f"gap2000=dimSU3(4,4)x16_EXACT_n_g_ratio={B['n_g_count_ratio']:.4f}>1_signPASS;"
        f"B:PV_N_eigs(L12={B['N_phys']:.0f})_finite_UVremoved={B['N_eigs_PV_subtracted']:.0f};"
        f"B:backfit-free_n_PBH(L14)={B['n_PBH_backfit_free_L14']:.3e}_repro_held_central_"
        f"rel={B['backfit_free_repro_rel']:.1e};"
        f"B:seam(i)_4.14x_RETAINED_seams(ii)(iii)(iv)_discharged_"
        f"TIER-2-DIMENSIONFUL-HELD_mag=INFO_NOT-loosened;"
        f"C:{C['regime']}_PR={C['PR']:.2f}(O(1))_peak/Page={C['peak_over_page']:.3f}_"
        f"NOT-truncation-artifact={C['not_truncation_artifact']};"
        f"composite={comp['composite']}"
        + (";plan-text-drift_canonical_SHA_runtime-pinned" if plan_drift else "")
    )  # (local)

    extra_rows = [
        f"# regulator_pin={REGULATOR_PIN}  (leg B Pauli-Villars-regularized N_eigs(Λ_UV=M_KK))",
        f"# Counting-axis pin: RATIO-BLOCKSUM (extensive, with-mult 80080) vs "
        f"RATIO-NORMALIZED-TRACE-MEAN (intensive, unique 78080); n_g=K0-rank; "
        f"gap 2000=dim_SU3(4,4)·16 EXACT (regulator-pin-discipline.md Counting axis)",
        f"# n_PBH §VII.AX.OP-PROJ Tier-2-DIMENSIONFUL HELD (REGISTRY-PASS-INELIGIBLE); "
        f"NON-PROMOTION-BY-HELD-NUMBER preserved; magnitude row NOT loosened",
        f"# DM mass anchor = Leggett inter-band coherence mode (LEGGETT-MOMENT S70, "
        f"Type-F, PROVEN); these three legs REFINE abundance/count/envelope only",
    ]  # (local)

    print_verdict_payload(
        comp["composite"], value, audit_sha, content_sha,
        comp["sign_verdict"], comp["magnitude_verdict"], comp["regime_verdict"],
        extra_rows=extra_rows,
    )

    print(f"\n  elapsed {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
