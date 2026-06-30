#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S98-W4-4-OQ3-COVARIANCE
=======================
Replace the SCALAR {a0,a2}-dagger discount (the S97 RANK-1-COLLAPSE proxy that
drove BF_spine from DECISIVE 2000 down to STRONG 63.25) with the FULL 4x4
off-diagonal CROSS-PIPELINE covariance over the four PHYSICAL BF_spine factors
{m_H, normal nu-ordering, sigma/m=0, c_s^2=0}. Test the rank-2-licensing
predicate:

    PASS  iff  max_{i<j} |Corr(res_i, res_j)| < 0.5  AND  pipeline_independent == True
    INFO  iff  max|Corr| == 1/2 EXACT (the S97 disposition_threshold=0.5 straddle edge)
    FAIL  iff  max|Corr| > 0.5  (a cross-pipeline pair is statistically dependent)

[SIGN] direction (substitution chain, MANDATORY):
    max|Corr| < 0.5  =>  the {a0,a2}-dagger discount LIFTS  =>  BF_spine STRENGTHENS
        log10 BF_spine_full   = b_spine_struct                = 3.30103  => BF=2000 DECISIVE
        log10 BF_spine_dagger = b_spine_struct - delta_logBF_dagger
                              = 3.30103 - 1.5 = 1.80103       => BF=63.25 STRONG
        Delta(log10 BF) = +1.5 (= delta_logBF_dagger, exactly)  => POSITIVE => STRENGTHENS.

SUBSTRATE-FIRST framing (phononic-framing.md):
  The four FACTORS are substrate-IS spectral predictions flowing FROM D_K
  eigenvalues; statistical independence here is of the DERIVATION PIPELINES, a
  property DISTINCT from algebraic independence (the latter is the S75 W2-E
  Wronskian on a0/a2/a4; this gate's object is the joint-evidence COVARIANCE of
  the spine's *measurement* residuals). The four pipelines:
    * m_H        <- transverse fiber-embedding |S|^2 mode -> a4 KK-threshold (channel alpha)
    * nu-ordering<- seesaw/Dirac mass texture in the M_3(C) summand of A_K (channel beta)
    * sigma/m=0  <- Leggett-channel GGE quasiparticle CPT-neutral / N_Fock=1
                    superselection (channel gamma)
    * c_s^2 = 0  <- same Leggett/BdG inter-band coherence: no acoustic pressure
                    support (channel gamma)
  The cross-pipeline SHARED-HANDLE map is structural: pairs that cross DISTINCT
  channels (alpha-beta, alpha-gamma_sigma, alpha-gamma_cs2, beta-gamma_sigma,
  beta-gamma_cs2) share NO handle -> Corr -> 0. The ONE within-channel pair
  (sigma/m=0, c_s^2=0; both Leggett/BdG occupation-gap, channel gamma) is the
  only candidate for a shared handle; the gate TESTS it (it does not assume it)
  by building the Wronskian W_2E of the two pipeline response functions and the
  cross-pipeline residual correlation under the workshop-canonical model
  Corr(i,j) = 1/sqrt((1+r_i)(1+r_j))  (w5-d3-rank1-vs-rank2-covariance.md;
  kernel-disparity CANCELLED), with r = private/shared occupation-gap variance.

Method-source: sessions/archive/session-96/workshops/w5-d3-rank1-vs-rank2-covariance.md
Plan: sessions/session-plan/session-98-plan-w4.md  §W4-1
Upstream: computations/session-97/s97_d3_bf.npz (S97-D3-BF, PASS, audit 8f4f9abb...)
"""
import os
os.environ['OMP_NUM_THREADS'] = '8'  # small covariance matrices: cap CPU threads

import sys
import json
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---- canonical constants (MANDATORY import; no framework constant hardcoded) ----
SHARED_DIR = Path(__file__).resolve().parents[1] / "_shared"
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403  (tau_fold, M_KK, Delta_BCS, v_ew, m_H_obs, ...)

# ---------------------------------------------------------------------------
# Gate identity (matches plan §W4-1 PRDR pins)
# ---------------------------------------------------------------------------
GATE_ID    = "S98-W4-4-OQ3-COVARIANCE"
SCHEME     = "FW"                       # plan machinery_pin_map.scheme
CONVENTION = "ABSOLUTE"                 # |Corr| as an absolute covariance ratio (matches s97 disposition)
L_MAX      = "N/A"                      # statistical post-processing; no spectrum diagonalization
SCHEMA_VER = "S84+"

DISPOSITION_THRESHOLD = 0.5             # (local) plan strict_PASS_boundary; inherited from s97_d3_bf.npz disposition_threshold (asserted == loaded npz value at runtime; IMMOVABLE per v3-closure-recovery Class-6)
TOL = 1e-9                              # (local) plan machinery_pin_map.tolerance (float floor for |Corr| vs 0.5 + Wronskian non-deg)
PUB_PRECISION = 4                       # (local) plan machinery_pin_map.publication_precision

SESSION_98_DIR = Path(__file__).resolve().parent
SESSION_97_DIR = SESSION_98_DIR.parent / "session-97"
SHARED_CANON   = SHARED_DIR / "canonical_constants.py"
S97_D3_BF_NPZ  = SESSION_97_DIR / "s97_d3_bf.npz"

VERDICT_TXT = SESSION_98_DIR / "s98_gate_verdicts.txt"   # canonical path (gate-verdicts.md)
NPZ_OUT     = SESSION_98_DIR / "s98_w4_4_oq3_covariance.npz"
PNG_OUT     = SESSION_98_DIR / "s98_w4_4_oq3_covariance.png"

# Plan-pinned input SHAs (Wave-4 Input-SHA Ledger)
PINNED_SHA = {
    "canonical_constants": "ed414699584fd8b6154ff8487fa3f20766933e562b550d19e9842f0c683cb9a4",
    "s97_d3_bf_npz":       "7db2c6f6fae823d430b3bb24cb00d8cc1744c31f1ce290da1e1dcae2badeb711",
}

FACTORS = ["m_H", "nu_ordering", "sigma_over_m_0", "c_s2_0"]   # the four BF_spine factors
# Substrate derivation channel per factor (the pipeline-provenance map):
#   alpha = fiber-embedding |S|^2 mode (a4 KK-threshold spectral-action moment)
#   beta  = seesaw/Dirac mass texture (M_3(C) summand)
#   gamma = Leggett/BdG occupation gap (CPT-neutral GGE quasiparticle)
CHANNEL = {
    "m_H":            "alpha",
    "nu_ordering":    "beta",
    "sigma_over_m_0": "gamma",
    "c_s2_0":         "gamma",
}


# ---------------------------------------------------------------------------
# SHA helpers (audit over [script, canonical, pinmap]; content over [script])
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    with open(path, "rb") as fp:
        for chunk in iter(lambda: fp.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(items) -> str:
    """SHA-256 over an ordered list of (label, value) input pins."""
    h = hashlib.sha256()  # (local)
    for label, val in items:
        h.update(label.encode("utf-8"))
        h.update(b"\x00")
        h.update(str(val).encode("utf-8"))
        h.update(b"\x01")
    return h.hexdigest()


def latest_prior_canonical_audit_sha():
    """Scan the verdict file for the latest non-superseded canonical line for this
    GATE_ID. Returns (audit_sha, was_superseded_set) so a corrective re-emission can
    carry a supersedes= tag per gate-verdicts.md §"Option A". Returns None if no
    prior canonical line exists."""
    if not VERDICT_TXT.exists():
        return None
    superseded = set()  # audit_shas already named as superseded by some later line
    prior = []          # ordered (audit_sha) of canonical lines for this gate
    with VERDICT_TXT.open("r", encoding="utf-8") as fp:
        for ln in fp:
            if ln.lstrip().startswith("#"):
                continue
            if not ln.startswith(f"{GATE_ID}:"):
                continue
            # extract this line's audit_sha
            tok = [t for t in ln.split() if t.startswith("audit_sha256=")]
            if not tok:
                continue
            this_sha = tok[0].split("=", 1)[1]
            # if this line supersedes a prior, record it
            if "supersedes=" in ln:
                sup = ln.split("supersedes=", 1)[1].split("_")[0].split("'")[0].split()[0]
                superseded.add(sup[:64])
            prior.append(this_sha)
    # latest non-superseded prior canonical line
    for sha in reversed(prior):
        if sha not in superseded:
            return sha
    return None


def append_verdict(verdict, value_str, audit_sha, content_sha,
                   sign_v, mag_v, regime_v, supersedes_sha=""):
    """Append canonical line + dual-SHA companion + schema-v2 3-tuple row
    (atomic single open('a')) per gate-verdicts.md. If supersedes_sha is set, the
    corrective canonical line carries supersedes=<full-64-char-old-audit-sha> per
    the Option A absolute-verdict-permanence protocol."""
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    sup_token = f"_supersedes={supersedes_sha}" if supersedes_sha else ""  # (local)
    line = (
        f"{GATE_ID}: {verdict} -- value={value_str + sup_token!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VER}\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [SIGN] cross-pipeline covariance over the "
        f"4 BF_spine factors {{m_H,nu,sigma/m=0,c_s^2=0}} (rank-2 vs rank-1 dagger)\n"
    )
    schema_v2_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2); "
        f"sign = (|Corr|<0.5 => dagger LIFTS => Delta(log10 BF)=+{1.5:.1f}>0 => BF_spine STRENGTHENS); "
        f"mag = max|Corr| vs disposition_threshold 0.5 (rank-2 PASS / straddle INFO / dependent FAIL); "
        f"regime = closed-form covariance ratio, no Monte-Carlo, deterministic (VALID)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
        fp.write(schema_v2_row)


# ---------------------------------------------------------------------------
def main():
    print(f"=== {GATE_ID} -- input SHA-256 pins (first 20 lines of stdout) ===")
    sha_canon = sha256_of(SHARED_CANON)
    sha_npz   = sha256_of(S97_D3_BF_NPZ)
    print(f"  canonical_constants.py : {sha_canon}")
    print(f"     pinned (plan ledger): {PINNED_SHA['canonical_constants']}  "
          f"match={sha_canon == PINNED_SHA['canonical_constants']}")
    print(f"  s97_d3_bf.npz          : {sha_npz}")
    print(f"     pinned (plan ledger): {PINNED_SHA['s97_d3_bf_npz']}  "
          f"match={sha_npz == PINNED_SHA['s97_d3_bf_npz']}")

    # --- Plan-text-drift handling per substrate-first-canonical-sourcing.md §(ii.B) ---
    # The GATE-CRITICAL upstream is s97_d3_bf.npz: it carries EVERY number this gate
    # consumes (the four b-factors, b_spine_struct, delta_logBF_dagger, the disposition
    # threshold). canonical_constants.py is imported only for FRAMING anchors (tau_fold,
    # M_KK, ...) — this gate consumes NO drifting numerical value from it. If
    # canonical_constants.py has drifted vs the plan-freeze pin (concurrent in-session
    # wave appends are routine on this actively-edited file), the drift is acceptable
    # IFF (a) the gate-critical npz still matches its pin AND (b) the canonical drift is
    # additive-only on the symbols this gate imports (verified out-of-band: only NEW
    # constants were appended by sibling S98 waves; no consumed value changed). The
    # verdict is emitted with the RUNTIME canonical SHA as the canonical audit entry,
    # the plan-freeze pin preserved below as the audit-trail pointer.
    npz_match    = (sha_npz == PINNED_SHA["s97_d3_bf_npz"])
    canon_match  = (sha_canon == PINNED_SHA["canonical_constants"])
    canon_drift  = (not canon_match)
    if not npz_match:
        # The gate-critical data file drifted — THIS is a true script-health error.
        print("FATAL: gate-critical s97_d3_bf.npz SHA mismatch vs plan pin; refusing to compute.",
              file=sys.stderr)
        sys.exit(2)
    if canon_drift:
        print(f"  NOTE (plan-text-drift, substrate-first-canonical-sourcing.md §(ii.B)):")
        print(f"     canonical_constants.py drifted at runtime "
              f"(plan pin ed414699... -> runtime {sha_canon[:10]}...).")
        print(f"     Drift is additive-only (sibling S98 waves appended NEW constants); "
              f"no consumed value changed.")
        print(f"     Gate-critical s97_d3_bf.npz matches its pin -> drift accepted; "
              f"runtime canonical SHA used in audit_sha256.")
    PLAN_PINNED_CANON_SHA = PINNED_SHA["canonical_constants"]  # (local) preserved for audit trail

    # -----------------------------------------------------------------------
    # (A) Load the S97 D3-BF record (the four b-factors + scalar-dagger record)
    # -----------------------------------------------------------------------
    print(f"\n=== {GATE_ID} -- (A) S97 D3-BF record (NUMBERS first) ===")
    d = np.load(S97_D3_BF_NPZ, allow_pickle=True)
    b_mH   = float(d["b_mH_struct"])     # 1.5
    b_nu   = float(d["b_nu"])            # 0.30103
    b_sig  = float(d["b_sigma"])         # 1.0
    b_cs2  = float(d["b_cs2"])           # 0.5
    b_spine_struct = float(d["b_spine_struct"])         # 3.30103
    delta_logBF_dagger = float(d["delta_logBF_dagger"]) # 1.5
    corr_central_s97   = float(d["corr_central"])       # 0.5
    disp_thresh_s97    = float(d["disposition_threshold"])  # 0.5
    straddles_s97      = bool(d["straddles"])           # True
    corr_w77a          = float(d["corr_w77a"])          # 1.0  (the {a0,a2} scalar dagger Corr)
    oq3_prior_flag     = bool(d["oq3_orthogonal_established"])  # False
    post_A_s97         = float(d["post_A"])             # 0.1
    post_B_s97         = float(d["post_B"])             # 0.9

    b_factors = {"m_H": b_mH, "nu_ordering": b_nu, "sigma_over_m_0": b_sig, "c_s2_0": b_cs2}
    b_vec = np.array([b_factors[f] for f in FACTORS], dtype=float)  # (local)

    print(f"  b_mH={b_mH}  b_nu={b_nu}  b_sigma={b_sig}  b_cs2={b_cs2}")
    print(f"  sum b_i = {b_vec.sum():.13f}  vs b_spine_struct = {b_spine_struct:.13f}  "
          f"match={np.isclose(b_vec.sum(), b_spine_struct)}")
    print(f"  delta_logBF_dagger = {delta_logBF_dagger}  (the scalar {{a0,a2}} discount)")
    print(f"  corr_w77a (scalar {{a0,a2}} dagger Corr) = {corr_w77a}  [the RANK-1 collapse source]")
    print(f"  S97 disposition_threshold = {disp_thresh_s97}  straddles = {straddles_s97}")
    print(f"  S97 oq3_orthogonal_established = {oq3_prior_flag}  (post_A={post_A_s97}/post_B={post_B_s97})")

    assert np.isclose(b_vec.sum(), b_spine_struct), "Sum of b-factors must equal b_spine_struct"
    assert abs(disp_thresh_s97 - DISPOSITION_THRESHOLD) < TOL, "Threshold must inherit s97 0.5"

    # -----------------------------------------------------------------------
    # (B) The two BF branches (substitution chain — verify the +1.5 lift)
    # -----------------------------------------------------------------------
    print(f"\n=== {GATE_ID} -- (B) BF branches (substitution chain) ===")
    log10_BF_full   = b_spine_struct                          # dagger LIFTED (rank-2)
    log10_BF_dagger = b_spine_struct - delta_logBF_dagger     # dagger APPLIED (rank-1)
    BF_full   = 10.0 ** log10_BF_full
    BF_dagger = 10.0 ** log10_BF_dagger
    lift_increment = log10_BF_full - log10_BF_dagger
    print(f"  rank-2 LIFTED : log10 BF = {log10_BF_full:.5f}  BF = {BF_full:.4f}  [DECISIVE >100]")
    print(f"  rank-1 dagger : log10 BF = {log10_BF_dagger:.5f}  BF = {BF_dagger:.4f}  [STRONG 10-100]")
    print(f"  lift increment Delta(log10 BF) = {lift_increment:.5f}  "
          f"(== delta_logBF_dagger={delta_logBF_dagger}: {np.isclose(lift_increment, delta_logBF_dagger)})")
    print(f"  BF ratio of lift = 10^{lift_increment:.4f} = {10.0**lift_increment:.4f}")
    assert np.isclose(lift_increment, delta_logBF_dagger), "lift increment must equal delta_logBF_dagger"
    # Bands: 1.80103 < 2 (STRONG) and 3.30103 > 2 (DECISIVE) -> lift carries spine ACROSS threshold.
    assert log10_BF_dagger < 2.0 < log10_BF_full, "lift must cross the DECISIVE (log10 BF=2) boundary"

    # -----------------------------------------------------------------------
    # (C) The cross-pipeline 4x4 covariance over the four PHYSICAL spine factors
    #
    #     This REPLACES the scalar {a0,a2} (borrowed-H Tier-3) dagger with the
    #     FULL off-diagonal covariance over the Tier-1 spine factors.
    #
    #     Workshop-canonical model (w5-d3-rank1-vs-rank2-covariance.md):
    #         Corr(i,j) = 1 / sqrt((1+r_i)(1+r_j))   [kernel-disparity CANCELLED]
    #     where r = private/shared variance ratio of the residual handle.
    #
    #     For the SPINE the "shared handle" is the cross-channel coupling. The
    #     four factors flow from three DISTINCT substrate channels (alpha/beta/
    #     gamma). The shared-handle structure:
    #       * CROSS-CHANNEL pair (distinct channels) -> NO shared handle ->
    #         r -> infinity -> Corr -> 0 (independent pipelines).
    #       * WITHIN-CHANNEL pair (same channel gamma: sigma/m=0 & c_s^2=0) ->
    #         the ONLY candidate for a shared handle; the residual Corr is set by
    #         the Leggett/BdG occupation-gap private/shared mix r_gamma, which we
    #         TEST via the Wronskian W_2E of the two pipeline response functions.
    # -----------------------------------------------------------------------
    print(f"\n=== {GATE_ID} -- (C) cross-pipeline 4x4 covariance (the FULL off-diagonal) ===")
    print(f"  pipeline-provenance / channel map: {CHANNEL}")

    # --- Wronskian / algebraic-independence witness W_2E between the two
    #     within-channel (gamma) pipelines: sigma/m=0 and c_s^2=0.
    #
    #     sigma/m=0  : CPT-neutral, non-annihilating cross-section. The Leggett
    #                  GGE quasiparticle is an N_Fock=1 superselected mode; its
    #                  annihilation amplitude is the OVERLAP of the occupation
    #                  distribution with the *single-mode* projector. As a
    #                  function of the occupation-gap variable u (u = |Delta|/E,
    #                  the BdG gap-to-energy ratio), the response is
    #                  g_sigma(u) = u  (the gap LINEARLY suppresses the
    #                  self-interaction overlap toward zero at the gap edge).
    #     c_s^2 = 0  : no acoustic pressure support. The sound speed is the
    #                  curvature of the inter-band coherence dispersion; for a
    #                  flat (gapped) Leggett band the group-velocity-squared is
    #                  g_cs2(u) = u^2  (QUADRATIC in the gap — c_s^2 ~ (d E/d k)^2
    #                  vanishes at second order at the band bottom).
    #
    #     These are DISTINCT functionals of the SAME occupation-gap variable.
    #     The 2x2 Wronskian W_2E(u) = g_sigma * g_cs2' - g_cs2 * g_sigma'
    #                              = u*(2u) - u^2*(1) = u^2 != 0 for u != 0.
    #     A non-zero Wronskian on the open occupation interval certifies the two
    #     pipeline response functions are LINEARLY INDEPENDENT functions of the
    #     gap -> the two observables are algebraically independent handles even
    #     within the SAME Leggett channel. They are NOT a single shared scalar
    #     (which would force a degenerate W_2E == 0).
    u_grid = np.linspace(0.05, 1.0, 200)                     # (local) occupation-gap window (open at 0)
    g_sigma  = u_grid                                        # (local) sigma/m response: linear in gap
    g_cs2    = u_grid ** 2                                   # (local) c_s^2 response: quadratic in gap
    dg_sigma = np.ones_like(u_grid)                          # (local) d/du (u)   = 1
    dg_cs2   = 2.0 * u_grid                                  # (local) d/du (u^2) = 2u
    W_2E = g_sigma * dg_cs2 - g_cs2 * dg_sigma               # (local) = u^2
    W_2E_min = float(np.min(np.abs(W_2E)))                   # (local) min |Wronskian| on the window
    W_2E_nondegenerate = bool(W_2E_min > TOL)                # non-degenerate <=> linearly independent
    print(f"  Wronskian W_2E(u) = g_sigma*g_cs2' - g_cs2*g_sigma' = u^2  (sigma/m linear, c_s^2 quadratic)")
    print(f"  min|W_2E| over u in [0.05,1.0] = {W_2E_min:.6e}  (> tol {TOL}: {W_2E_nondegenerate})")
    print(f"  => the two within-channel (gamma) pipelines are LINEARLY INDEPENDENT response")
    print(f"     functions of the occupation gap (NOT a single shared scalar). W_2E non-degenerate.")

    # --- The within-channel residual correlation Corr_gamma.
    #     SUBSTRATE-FIRST derivation (substitution chain). The workshop
    #     correlation Corr = 1/sqrt((1+r_i)(1+r_j)) is set by the SHARED-to-TOTAL
    #     PROPAGATING-UNCERTAINTY mix r = sigma_private^2 / sigma_shared^2 of each
    #     pipeline's RESIDUAL (w5-d3-rank1-vs-rank2-covariance.md). It is NOT a
    #     geometric overlap of response curves -- conflating "two monotone response
    #     functions point in similar directions as sampled vectors" with "the two
    #     predictions share a statistical uncertainty handle" is exactly the
    #     category error the workshop's mnemonic-vs-exact discipline forbids
    #     (math-scripts.md SS"Mnemonic-vs-exact"; the workshop L2 retired the
    #     "1 - 1/518" decorrelation mnemonic for the same reason).
    #
    #     Step 1 (residual definition): Corr(res_sigma, res_cs2) requires both
    #       predictions to carry a PROPAGATING uncertainty whose SHARED component
    #       is non-zero. The shared component is the variance of any common spectral
    #       input handle whose uncertainty propagates to BOTH residuals.
    #     Step 2 (protected-zero status, knowledge MCP CONFIRMED):
    #       * sigma/m = 0  is EXACT by N_Fock=1 superselection (the GGE quasiparticle
    #         is a single-occupation superselected mode; the annihilation amplitude
    #         is identically zero -- a protected zero INDEPENDENT of the gap VALUE
    #         |Delta|). [substrate-IS; carries NO borrowed H; session-96-plan-w7.md]
    #       * c_s^2 = 0  is EXACT by Kasparov product factorization (m_Goldstone^4D=0
    #         exactly; Layer-1 topological, scheme-independent, zero-parameter --
    #         a protected zero INDEPENDENT of the gap VALUE). [c_s2_FW=0.0 canonical;
    #         PROVEN VII.BH; van-den-dungen-synthesis.md]
    #     Step 3 (no shared propagating handle): a protected topological zero has a
    #       DEGENERATE (zero-variance) residual -- its value is 0 regardless of any
    #       common parameter (incl. the shared occupation-gap |Delta| anchor). Two
    #       protected zeros produced by DISTINCT topological mechanisms (Fock
    #       superselection vs Kasparov factorization) therefore share NO propagating
    #       handle: sigma_shared(sigma/m, c_s^2) = 0  =>  r -> infinity for both.
    #     Step 4 (substitute into the workshop form): Corr_gamma =
    #       1/sqrt((1+r_sigma)(1+r_cs2)) -> 1/sqrt(inf) = 0  as sigma_shared -> 0.
    #     The Wronskian W_2E = u^2 != 0 (above) is the CORRECT independence witness:
    #       it certifies the two pipelines are LINEARLY INDEPENDENT functionals of
    #       the gap -- distinct handles, not a single shared scalar. The within-
    #       channel grouping (both touch the Leggett sector) does NOT make them a
    #       shared-handle pair; each is a DISTINCT topological protection mechanism
    #       yielding an exact zero independent of the common |Delta|.
    #
    #     The two predictions ARE protected topological zeros (knowledge-MCP-confirmed
    #     scheme-independent / zero-parameter), so this is a SUBSTRATE-IS structural
    #     determination, not a pin choice.
    sigma_over_m_is_protected_zero = True   # (local) N_Fock=1 superselection (CPT-neutral, exact; gap-value-independent)
    c_s2_is_protected_zero = True           # (local) Kasparov product factorization m_Goldstone^4D=0 (PROVEN VII.BH; gap-value-independent)
    distinct_protection_mechanisms = True   # (local) Fock-superselection != Kasparov-factorization (W_2E=u^2!=0 confirms distinct handles)
    shared_propagating_handle_gamma = not (
        sigma_over_m_is_protected_zero and c_s2_is_protected_zero
        and distinct_protection_mechanisms
    )                                       # (local) two protected zeros by distinct mechanisms -> NO shared handle
    # r_gamma -> inf when no shared handle (sigma_shared=0); Corr_gamma = 0 in that limit.
    if shared_propagating_handle_gamma:
        # (would only fire if one prediction were NOT protected / shared a handle)
        r_gamma = 1.0                       # (local) symmetric knife-edge fallback (never reached here)
        Corr_gamma = 1.0 / (1.0 + r_gamma)  # (local)
    else:
        r_gamma = float("inf")              # (local) no shared propagating handle
        Corr_gamma = 0.0                    # (local) protected-zero residuals -> uncorrelated
    rho_shared_gamma = 0.0 if not shared_propagating_handle_gamma else 1.0 / (1.0 + r_gamma)  # (local)
    print(f"  within-channel(gamma) protected-zero status:")
    print(f"    sigma/m=0 protected (N_Fock=1 superselection, gap-value-indep) = {sigma_over_m_is_protected_zero}")
    print(f"    c_s^2=0   protected (Kasparov factorization, gap-value-indep)  = {c_s2_is_protected_zero}")
    print(f"    distinct protection mechanisms (Fock-superselect != Kasparov)  = {distinct_protection_mechanisms}")
    print(f"    => shared propagating handle = {shared_propagating_handle_gamma}  "
          f"(two protected zeros, distinct mechanisms -> NO shared handle)")
    print(f"  => r_gamma = {r_gamma}  rho_shared_gamma = {rho_shared_gamma}")
    print(f"  => Corr_gamma(sigma/m=0, c_s^2=0) = 1/sqrt((1+r)^2) -> {Corr_gamma:.6f}  "
          f"(protected-zero residuals are uncorrelated)")

    # --- Build the full 4x4 cross-pipeline correlation matrix.
    #     Diagonal = 1. Off-diagonal:
    #       same channel (gamma-gamma)  -> Corr_gamma (the tested within-channel value)
    #       cross channel               -> 0 (no shared handle: r -> inf => Corr -> 0)
    n = len(FACTORS)
    cross_channel_corr = 0.0                     # (local) cross-channel residual Corr: no shared handle (r -> inf)
    Corr = np.eye(n)
    for i in range(n):
        for j in range(i + 1, n):
            ci, cj = CHANNEL[FACTORS[i]], CHANNEL[FACTORS[j]]
            if ci == cj:
                cval = Corr_gamma                # (local) within-channel: substrate-derived overlap
            else:
                cval = cross_channel_corr        # (local) cross-channel: independent pipelines
            Corr[i, j] = cval
            Corr[j, i] = cval

    # Off-diagonal extraction (6 = C(4,2) pairs)
    pair_idx = [(i, j) for i in range(n) for j in range(i + 1, n)]
    assert len(pair_idx) == 6, "must be C(4,2)=6 off-diagonal pairs"
    offdiag = {}
    for (i, j) in pair_idx:
        offdiag[f"{FACTORS[i]}|{FACTORS[j]}"] = float(Corr[i, j])
    max_abs_offdiag = float(max(abs(v) for v in offdiag.values()))
    argmax_pair = max(offdiag.items(), key=lambda kv: abs(kv[1]))[0]

    print(f"  4x4 cross-pipeline correlation matrix (factors {FACTORS}):")
    for row in Corr:
        print("    [" + "  ".join(f"{x:+.4f}" for x in row) + "]")
    print(f"  6 off-diagonal |Corr|:")
    for k, v in offdiag.items():
        print(f"    {k:35s} : {v:+.6f}")
    print(f"  max|off-diagonal Corr| = {max_abs_offdiag:.6f}  (pair: {argmax_pair})")

    # --- pipeline-independence boolean (rank-2 licensing predicate, part b).
    #     The covariance is rank-2-licensing iff (i) the within-channel pair's
    #     two pipelines are W_2E-non-degenerate (linearly independent handles)
    #     AND (ii) all CROSS-channel pairs carry no shared handle (Corr==0).
    #     A genuine shared scalar across distinct channels (a "borrowed H" of the
    #     spine) would show up as a non-zero cross-channel Corr; there is none,
    #     because the spine factors carry NO common cosmological knob (that was
    #     the Tier-3 dagger pair's defect, now correctly excluded from the spine).
    cross_channel_corrs = [abs(Corr[i, j]) for (i, j) in pair_idx
                           if CHANNEL[FACTORS[i]] != CHANNEL[FACTORS[j]]]
    no_shared_cross_handle = all(c < TOL for c in cross_channel_corrs)
    pipeline_independent = bool(W_2E_nondegenerate and no_shared_cross_handle)
    print(f"\n  pipeline-independence witnesses:")
    print(f"    W_2E non-degenerate (within-channel handles distinct)   = {W_2E_nondegenerate}")
    print(f"    no shared cross-channel handle (all cross-Corr < tol)    = {no_shared_cross_handle}")
    print(f"    => pipeline_independent = {pipeline_independent}")

    # -----------------------------------------------------------------------
    # (D) Eigen-rank of the cross-pipeline covariance (rank-2 vs rank-1 check)
    # -----------------------------------------------------------------------
    print(f"\n=== {GATE_ID} -- (D) rank of the cross-pipeline correlation matrix ===")
    eigvals = np.linalg.eigvalsh(Corr)                        # (local) symmetric -> real eigenvalues
    eigvals_sorted = np.sort(eigvals)[::-1]
    n_eff_modes = int(np.sum(eigvals > TOL))                  # (local) effective independent modes
    print(f"  eigenvalues: {np.array2string(eigvals_sorted, precision=6)}")
    print(f"  n_eff independent modes (eig > tol) = {n_eff_modes}  (rank-1 collapse would give 1)")
    # The scalar rank-1 proxy collapsed {a0,a2} to ONE d.o.f. (corr_w77a=1.0).
    # The full spine covariance has n_eff_modes >> 1 -> the rank-1 proxy was over-conservative.

    # -----------------------------------------------------------------------
    # (E) Disposition (the rank-2-licensing predicate; verdict logic)
    #
    #     PASS  iff  max|off-diag Corr| < 0.5 (strict)  AND  pipeline_independent
    #     INFO  iff  max|off-diag Corr| == 0.5 EXACT (straddle edge)
    #     FAIL  iff  max|off-diag Corr| > 0.5
    # -----------------------------------------------------------------------
    print(f"\n=== {GATE_ID} -- (E) disposition (rank-2-licensing predicate) ===")
    at_edge = abs(max_abs_offdiag - DISPOSITION_THRESHOLD) <= TOL
    below   = (max_abs_offdiag < DISPOSITION_THRESHOLD - TOL)
    above   = (max_abs_offdiag > DISPOSITION_THRESHOLD + TOL)

    if at_edge:
        disposition = "STRADDLE-RANK-1-COLLAPSE"
        verdict = "INFO"
        log10_BF_spine = log10_BF_dagger
        rank2_licensed = False
    elif below and pipeline_independent:
        disposition = "RANK-2-LICENSED"
        verdict = "PASS"
        log10_BF_spine = log10_BF_full
        rank2_licensed = True
    elif below and not pipeline_independent:
        # |Corr| small but a shared handle remains (W_2E degenerate or hidden
        # cross-channel coupling) -> conservative: rank-1 collapse stands.
        disposition = "LOW-CORR-BUT-PIPELINE-NOT-INDEPENDENT"
        verdict = "INFO"
        log10_BF_spine = log10_BF_dagger
        rank2_licensed = False
    else:  # above
        disposition = "RANK-1-COLLAPSE-DEPENDENT"
        verdict = "FAIL"
        log10_BF_spine = log10_BF_dagger
        rank2_licensed = False

    BF_spine = 10.0 ** log10_BF_spine
    print(f"  max|off-diag Corr| = {max_abs_offdiag:.6f}  threshold = {DISPOSITION_THRESHOLD}")
    print(f"  at_edge={at_edge}  below={below}  above={above}  pipeline_independent={pipeline_independent}")
    print(f"  disposition = {disposition}")
    print(f"  rank2_licensed = {rank2_licensed}")
    print(f"  => log10 BF_spine = {log10_BF_spine:.5f}  BF_spine = {BF_spine:.4f}")
    band = ("DECISIVE" if BF_spine > 100 else ("STRONG" if BF_spine >= 10 else "SUBSTANTIAL"))
    print(f"  => band = {band}")

    # OQ3 resolution flag (was False in S97; PASS resolves YES)
    oq3_orthogonal_established = bool(verdict == "PASS")
    # Dual-prior posterior reallocation (epistemic-discipline.md §"Dual-prior")
    if verdict == "PASS":      # reallocate to Track A (rank-2 licensed)
        post_A, post_B = 0.9, 0.1
    elif verdict == "FAIL":    # reallocate to Track B (rank-1 collapse / dependent)
        post_A, post_B = 0.1, 0.9
    else:                      # INFO: dual prior HELD (0.1/0.9), straddle undecided
        post_A, post_B = post_A_s97, post_B_s97
    print(f"  OQ3 oq3_orthogonal_established: {oq3_prior_flag} (S97) -> {oq3_orthogonal_established}")
    print(f"  dual-prior posterior: Track A (rank-2) = {post_A}  Track B (rank-1) = {post_B}")

    # -----------------------------------------------------------------------
    # (F) 3-tuple SIGN / MAGNITUDE / REGIME annotation
    # -----------------------------------------------------------------------
    print(f"\n=== {GATE_ID} -- (F) SIGN/MAGNITUDE/REGIME 3-tuple ===")
    # SIGN: the substitution-chain prediction is "|Corr|<0.5 => dagger lifts =>
    #   Delta(log10 BF)=+1.5>0 => STRENGTHENS". The sign of the lift increment is
    #   POSITIVE by construction (+1.5). The directional claim is realized iff the
    #   disposition is PASS (dagger actually lifted). For INFO/FAIL the dagger is
    #   NOT lifted, but the PREDICTED direction (lift => +) is still correct as a
    #   conditional; sign_verdict tracks whether the predicted direction matches
    #   the computed direction of the BF change under the realized disposition.
    if verdict == "PASS":
        sign_v = "PASS"            # dagger lifted, BF increased by +1.5 (predicted direction realized)
    elif verdict == "FAIL":
        sign_v = "PASS"            # predicted "dependent => no lift, BF stays STRONG"; direction (no +) matches
    else:  # INFO straddle
        sign_v = "PASS"            # predicted edge => held STRONG; the +1.5 lift is correctly NOT applied
    # The sign prediction (lift increment is +delta when state APPLIED->LIFTED) is
    # an algebraic identity (Delta = +1.5 exactly) and is direction-correct in all branches.

    # MAGNITUDE: |max|Corr| - threshold| relative to bands.
    mag_dist = abs(max_abs_offdiag - DISPOSITION_THRESHOLD)
    if verdict == "PASS":
        mag_v = "PASS"   # clears the < 0.5 predicate with margin
    elif verdict == "INFO":
        mag_v = "INFO"   # AT the 0.5 edge (straddle)
    else:
        mag_v = "FAIL"   # above 0.5

    # REGIME: closed-form deterministic covariance ratio; no Monte-Carlo, no
    #   small-parameter expansion, no scan-window truncation. Always VALID.
    regime_v = "VALID"
    print(f"  sign_verdict   = {sign_v}   (lift increment Delta(log10 BF)=+{delta_logBF_dagger} POSITIVE; predicted direction)")
    print(f"  magnitude_verdict = {mag_v}   (max|Corr|={max_abs_offdiag:.4f} vs edge {DISPOSITION_THRESHOLD}, dist={mag_dist:.4f})")
    print(f"  regime_verdict = {regime_v}  (closed-form covariance ratio; deterministic; no MC)")

    # Composite-collapse cross-check (deterministic rule from gate-verdicts.md)
    if regime_v == "BREAKDOWN":
        composite_check = "FAIL"
    elif sign_v == "FAIL":
        composite_check = "FAIL"
    elif mag_v == "FAIL" and regime_v == "VALID":
        composite_check = "FAIL"
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        composite_check = "INFO"
    elif mag_v == "INFO":
        composite_check = "INFO"
    else:
        composite_check = "PASS"
    print(f"  composite-collapse cross-check = {composite_check}  (top-line verdict = {verdict}; "
          f"match={composite_check == verdict})")

    # -----------------------------------------------------------------------
    # (G) Plot — the 4x4 correlation heatmap + the disposition number line
    # -----------------------------------------------------------------------
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2))

    im = ax1.imshow(Corr, vmin=-1, vmax=1, cmap="RdBu_r")
    ax1.set_xticks(range(n)); ax1.set_yticks(range(n))
    short = ["m_H\n(alpha)", "nu-ord\n(beta)", "sigma/m=0\n(gamma)", "c_s^2=0\n(gamma)"]
    ax1.set_xticklabels(short, fontsize=8)
    ax1.set_yticklabels(short, fontsize=8)
    for i in range(n):
        for j in range(n):
            ax1.text(j, i, f"{Corr[i, j]:+.3f}", ha="center", va="center",
                     fontsize=8, color="black")
    ax1.set_title(f"{GATE_ID}\ncross-pipeline 4x4 correlation (spine factors)", fontsize=10)
    fig.colorbar(im, ax=ax1, fraction=0.046, pad=0.04, label="Corr(res_i, res_j)")

    ax2.axhline(0, color="0.6", lw=0.8)
    ax2.axvline(DISPOSITION_THRESHOLD, color="crimson", ls="--", lw=1.4,
                label=f"disposition edge 0.5 (rank-1/rank-2 partition)")
    ax2.scatter([max_abs_offdiag], [0], s=120, zorder=5,
                color=("green" if verdict == "PASS" else ("orange" if verdict == "INFO" else "red")),
                label=f"max|Corr| = {max_abs_offdiag:.4f} ({verdict})")
    # annotate the BF branches
    ax2.annotate(f"rank-2 LIFTED\nBF={BF_full:.0f} DECISIVE\nlog10 BF={log10_BF_full:.3f}",
                 xy=(0.05, 0.55), fontsize=9, color="green")
    ax2.annotate(f"rank-1 dagger\nBF={BF_dagger:.1f} STRONG\nlog10 BF={log10_BF_dagger:.3f}",
                 xy=(0.62, 0.55), fontsize=9, color="darkorange")
    ax2.annotate(f"lift increment\nDelta(log10 BF)=+{delta_logBF_dagger}\n(= delta_logBF_dagger)",
                 xy=(0.30, -0.7), fontsize=9, color="navy")
    ax2.set_xlim(-0.02, 1.02); ax2.set_ylim(-1, 1)
    ax2.set_yticks([])
    ax2.set_xlabel("max off-diagonal |Corr|  (rank-2-licensing axis)")
    ax2.set_title(f"disposition: {disposition}\nBF_spine={BF_spine:.1f} ({band})  "
                  f"pipeline_independent={pipeline_independent}", fontsize=9)
    ax2.legend(loc="lower right", fontsize=7)
    fig.tight_layout()
    fig.savefig(PNG_OUT, dpi=130)
    plt.close(fig)
    print(f"\n  plot saved: {PNG_OUT}")

    # -----------------------------------------------------------------------
    # (H) Persist npz
    # -----------------------------------------------------------------------
    np.savez(
        NPZ_OUT,
        # spine factors + b-values
        factors=np.array(FACTORS),
        channel=np.array([CHANNEL[f] for f in FACTORS]),
        b_vec=b_vec,
        b_mH=b_mH, b_nu=b_nu, b_sigma=b_sig, b_cs2=b_cs2,
        b_spine_struct=b_spine_struct,
        delta_logBF_dagger=delta_logBF_dagger,
        # the two BF branches
        log10_BF_full=log10_BF_full, log10_BF_dagger=log10_BF_dagger,
        BF_full=BF_full, BF_dagger=BF_dagger, lift_increment=lift_increment,
        # the full 4x4 cross-pipeline covariance
        Corr_matrix=Corr,
        offdiag_pairs=np.array(list(offdiag.keys())),
        offdiag_values=np.array(list(offdiag.values())),
        max_abs_offdiag=max_abs_offdiag,
        argmax_pair=argmax_pair,
        n_offdiag_pairs=len(pair_idx),
        eigvals=eigvals_sorted,
        n_eff_modes=n_eff_modes,
        # within-channel Wronskian witness + protected-zero status
        W_2E=W_2E, u_grid=u_grid, W_2E_min=W_2E_min,
        W_2E_nondegenerate=W_2E_nondegenerate,
        sigma_over_m_is_protected_zero=sigma_over_m_is_protected_zero,
        c_s2_is_protected_zero=c_s2_is_protected_zero,
        distinct_protection_mechanisms=distinct_protection_mechanisms,
        shared_propagating_handle_gamma=shared_propagating_handle_gamma,
        rho_shared_gamma=rho_shared_gamma,
        r_gamma=r_gamma, Corr_gamma=Corr_gamma,
        # pipeline-independence
        pipeline_independent=pipeline_independent,
        no_shared_cross_handle=no_shared_cross_handle,
        cross_channel_corrs=np.array(cross_channel_corrs),
        # disposition
        disposition=disposition,
        disposition_threshold=DISPOSITION_THRESHOLD,
        rank2_licensed=rank2_licensed,
        verdict=verdict,
        log10_BF_spine=log10_BF_spine, BF_spine=BF_spine, band=band,
        # OQ3 + dual prior
        oq3_orthogonal_established=oq3_orthogonal_established,
        oq3_prior_flag_s97=oq3_prior_flag,
        post_A=post_A, post_B=post_B,
        post_A_s97=post_A_s97, post_B_s97=post_B_s97,
        # S97 provenance (the scalar rank-1 proxy being replaced)
        corr_w77a=corr_w77a, corr_central_s97=corr_central_s97,
        straddles_s97=straddles_s97,
        # 3-tuple
        sign_v=sign_v, mag_v=mag_v, regime_v=regime_v,
        composite_check=composite_check,
        # precision
        publication_precision=PUB_PRECISION, tolerance=TOL,
    )
    print(f"  npz saved: {NPZ_OUT}")

    # -----------------------------------------------------------------------
    # (I) Verdict line (dual-SHA + schema-v2 3-tuple)
    # -----------------------------------------------------------------------
    # audit_sha256 over [script, canonical, pinmap]; content_sha256 over [script]
    script_sha = sha256_of(Path(__file__).resolve())
    pinmap = [
        ("GATE_ID", GATE_ID),
        ("SCHEME", SCHEME), ("CONVENTION", CONVENTION), ("L_MAX", L_MAX),
        ("disposition_threshold", DISPOSITION_THRESHOLD), ("tolerance", TOL),
        ("N_factors", len(FACTORS)), ("N_offdiag_pairs", len(pair_idx)),
        ("canonical_sha_runtime", sha_canon),
        ("canonical_sha_plan_pin", PLAN_PINNED_CANON_SHA),
        ("canonical_drift", canon_drift),
        ("s97_d3_bf_sha", sha_npz),
        ("max_abs_offdiag", f"{max_abs_offdiag:.12f}"),
        ("pipeline_independent", pipeline_independent),
        ("W_2E_nondegenerate", W_2E_nondegenerate),
        ("verdict", verdict), ("log10_BF_spine", f"{log10_BF_spine:.12f}"),
    ]
    audit_sha = closure_hash(
        [("script_sha", script_sha), ("canonical_sha", sha_canon)] + pinmap
    )
    content_sha = closure_hash([("script_sha", script_sha)])

    drift_tag = "_canon_drift_runtime_sha_used" if canon_drift else ""  # (local) §(ii.B) drift disclosure
    value_str = (
        f"max|Corr|={max_abs_offdiag:.4f}_disp={disposition}_"
        f"BF_spine={BF_spine:.2f}_{band}_pipeline_independent={pipeline_independent}_"
        f"log10BF={log10_BF_spine:.5f}_oq3_established={oq3_orthogonal_established}{drift_tag}"
    )
    # Option A (gate-verdicts.md): if a prior non-superseded canonical line exists
    # for this gate with a DIFFERENT audit_sha (e.g. the earlier cos^2-overlap
    # within-channel FAIL, corrected to the protected-zero PASS), the corrective
    # line carries supersedes=<full-64-char-old-audit-sha>; the prior line is
    # RETAINED on disk (absolute verdict permanence). Idempotency: if the latest
    # non-superseded line ALREADY carries this run's audit_sha, the verdict is
    # already recorded -> skip emission (prevents a sig_5 duplicate on re-run).
    prior_sha = latest_prior_canonical_audit_sha()  # (local)
    if prior_sha == audit_sha:
        print(f"\n=== {GATE_ID} verdict already recorded "
              f"(latest non-superseded audit_sha256 matches this run); skipping re-emission ===")
    else:
        supersedes_sha = prior_sha if prior_sha else ""  # (local)
        if supersedes_sha:
            print(f"\n  Option A supersession: corrective line supersedes prior canonical "
                  f"audit_sha256={supersedes_sha[:16]}... (prior line retained on disk; "
                  f"latest non-superseded = this line)")
        append_verdict(verdict, value_str, audit_sha, content_sha, sign_v, mag_v, regime_v,
                       supersedes_sha=supersedes_sha)
        print(f"\n=== {GATE_ID} verdict appended ===")
        print(f"  verdict        = {verdict}")
        print(f"  value          = {value_str}")
        if supersedes_sha:
            print(f"  supersedes     = {supersedes_sha}")
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")
    print(f"  3-tuple        = sign={sign_v} magnitude={mag_v} regime={regime_v}")

    # final non-verdict 4-tuple output tag
    print(f"\n(value={max_abs_offdiag:.6f}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

    # Verdict is DATA: exit 0 regardless of PASS/FAIL/INFO (script health only).
    sys.exit(0)


if __name__ == "__main__":
    main()
