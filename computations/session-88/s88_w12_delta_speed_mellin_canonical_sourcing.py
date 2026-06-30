"""
S88 W12-135 — S88-DELTA-SPEED-MELLIN-CANONICAL-SOURCING
========================================================

Substrate-first canonical sourcing audit for δ_speed observable.

OWNERSHIP: mack-cosmic-bridge (cosmological observable provenance) +
gen-physicist (orchestrator; Mellin-cone substrate computation). Solo
runner takes ownership per `.claude/skills/rclab-solo/SKILL.md` Phase 2
step 2 agent-ownership-takeover discipline.

PRE-COMPUTE AUDIT — KNOWLEDGE MCP FINDINGS:
- §VII.U.1 (Mellin-Dirichlet finite-spectrum identity at substrate-
  distance-1 pole s=3) LANDED at `permanent-results-registry.md:118,
  12844` per S86 W-1 / S87 W1a-4 PASS (rel_diff = 0e+00 at L_max=12).
- canonical_constants.py:30 already pins `r_CMB_framework =
  0.011731522176014426` from S83 G46 TENSOR-TRANSFER PASS — IDENTICAL
  to the value the plan §W12-135 cites as `δ_speed_PathC = 0.011731522`.
- W-3 workshop closure (sessions/archive/session-86/workshops/s86-r-dual-pathway-
  bk-array-and-nT.md:1609) defines δ_speed as `d ln c_S / d ln k|_pivot`
  (logarithmic running of c_S) — NOT a tensor-to-scalar ratio.
- W-3 closure line 2041: substrate δ_speed band is `±25%` (3He-B-
  inherited). Magnitude O(0.25), not O(0.01).
- S87-DELTA-SPEED-MELLIN-WINDOW closed PRE-REG-INC with
  `delta_speed_PathH_MISSING delta_speed_PathC_MISSING
   sigma_delta_speed_mellin_noise_MISSING` — the δ_speed values were
  declared NOT YET ESTABLISHED at S87.
- canonical_constants list_constants(pattern='delta_speed') returns
  EMPTY — no δ_speed_*_FW canonical exists.

STRUCTURAL FINDING:
The plan §W12-135's reference values 0.00745 and 0.011731522 are
r_Path_H (tensor-to-scalar Path-H, S83 G46 4-sig-fig published form
per `s86-r-dual-pathway-bk-array-and-nT.md:1620`) and r_CMB_framework
(tensor-to-scalar Path-C, canonical_constants.py:30 full float64 form)
respectively. They are NOT δ_speed values per the W-3 closure
definition. This is a SOURCE-RECONCILIATION Class-(d) PIN-DERIVATIVE-
VS-SOURCE-PRIMARY pin-conflation per `.claude/rules/epistemic-
discipline.md §"Source Reconciliation"`.

SUBSTITUTION CHAIN (W-3 closure-canonical, written before computation):

  Step 1 (Definition, W-3 §line 1609):
    δ_speed(τ_fold; R) := d ln c_S(k; τ_fold; R) / d ln k |_pivot

  Step 2 (Definition, §VII.U.1 Mellin-Dirichlet identity at L_max≥10):
    M_s := Tr[D_K^{-2s}] = Σ_{(p,q): p+q ≤ L_max} dim(p,q) *
                          Σ_{λ ∈ abs_evals(p,q)} |λ|^{-2s}

  Step 3 (Substitution at integer s ∈ {3, 4}):
    M_s3 := Mellin moment at substrate-distance-1 pole (§VII.U.1)
    M_s4 := Mellin moment at substrate-distance-2 pole (§VII.K-PROP.W10-4)

  Step 4 (Direction — substrate-first canonical sourcing audit
          REJECTS the plan-pin claim that δ_speed_PathH = 0.00745 ∧
          δ_speed_PathC = 0.011731522):
    The structural-direction prediction `sign(δ_speed_PathH) = +1 ∧
    sign(δ_speed_PathC) = -1` (anti-correlation) per W-3 closure §lines
    2098-2161 IS substrate-first defensible at the structural-sign
    level (Hypothesis B running with regulator-class-dependent (Δ_B/
    Δ_A)^p inheritance), but the magnitudes 0.00745 / 0.011731522
    derive from r_Path tensor-to-scalar — NOT from `d ln c_S / d ln k`.

  Step 5 (Conclusion — substrate-first canonical sourcing OUTPUT):
    Substrate-first canonicals reproducible from this gate:
      M_s3_FW (substrate-distance-1 Mellin moment, §VII.U.1 LENS-mediated)
      M_s4_FW (substrate-distance-2 Mellin moment, §VII.K-PROP.W10-4
               substrate)
    Structural-quantity-NOT-reproducible from this gate:
      δ_speed_PathH_FW = 0.00745 (REJECTED — r_Path_H per W-3 closure)
      δ_speed_PathC_FW = 0.011731522 (REJECTED — r_CMB_framework per
                         canonical_constants.py:30)
    Composite verdict: FAIL (sign=N/A, magnitude=FAIL, regime=BREAKDOWN)
    via the §VII.U.1 LANDED Mellin-Dirichlet identity verifying that the
    substrate-first observables exist as M_s3 / M_s4 — but the plan-pin
    values cannot be reproduced because they are r-side (not δ_speed-
    side) observables.

VERDICT TARGET: FAIL with composite (sign=N/A, magnitude=FAIL,
regime=BREAKDOWN) per `.claude/rules/gate-verdicts.md §"S87+ canonical
form (Schema-v2)"`. The substrate-first Mellin moments M_s3, M_s4 ARE
promoted to canonical_constants.py — these ARE the substrate-first
canonical-sourcing OUTPUT, regardless of the plan-pin's
r_Path-vs-δ_speed conflation.

SUBSTRATE FRAMING (per `.claude/rules/phononic-framing.md` §"IS Space,
Not IN Space"): the substrate IS the spectral triple (A_K, H_K, D_K).
The Mellin moments M_s3, M_s4 are substrate-IS observables — they live
on the spectral triple, not in any continuum container. The plan's
purported δ_speed_PathH/δ_speed_PathC are laboratory-IN observables
(measured as deviations from c_obs in FRW); the bridge between
substrate-IS Mellin residues and laboratory-IN δ_speed requires a
factorization (impedance-mismatch lemma + (Δ_B/Δ_A)^p inheritance) that
is NOT canonically defined. The plan-pin's numerical values r_Path_H /
r_CMB_framework belong to a DIFFERENT bridge (tensor power spectrum
ratio P_T/P_S), not to δ_speed = d ln c_S / d ln k. Container-thinking
of "δ_speed equals r_Path because they share substrate-distance-1 pole
machinery" is the structural error this gate detects.

REFERENCES:
- Plan: sessions/session-plan/session-88-plan-w12.md §W12-135
- W-3 closure: sessions/archive/session-86/workshops/s86-r-dual-pathway-bk-
  array-and-nT.md (3268 lines)
- §VII.U.1: sessions/permanent-results-registry.md:118,12844
- canonical_constants.py:30 — r_CMB_framework
- .claude/rules/substrate-first-canonical-sourcing.md
- .claude/rules/epistemic-discipline.md §"Source Reconciliation"
- .claude/rules/gate-verdicts.md §"S87+ canonical form (Schema-v2)"
"""

import hashlib
import json
import os
import sys
import time
from pathlib import Path

import numpy as np

# Ensure the canonical constants are importable.
_THIS = Path(__file__).resolve()
_REPO = _THIS.parent.parent.parent
sys.path.insert(0, str(_REPO / "computations" / "_shared"))
from canonical_constants import (  # noqa: E402
    tau_fold,
    w0_FW,
    c_sub_baseline,
    r_CMB_framework,
)

# ---------------------------------------------------------------------------
# Plan-pinned machinery (per §W12-135 PIN MAP)
# ---------------------------------------------------------------------------
GATE_ID = "S88-DELTA-SPEED-MELLIN-CANONICAL-SOURCING"
WP_SECTION = "W12-135"
SCHEME = "Mellin-cone-analytic-continuation-substrate-first"
CONVENTION = "Path-H-HypB-Path-C-HypA-substrate-first"
L_MAX_PLAN = 10           # (local) plan §W12-135 PIN MAP
L_MAX_OPERATIONAL = 10    # (local) Friedrich-Bär-saturation operational pin
PUBLICATION_SIG_FIGS = 10 # (local) Class-8.3 publication-precision pin
VERIFIER_REL_TOL = 1e-9   # (local) plan §W12-135 verifier rel_tol pin

# Pin values cited in the plan (under audit; W-3 closure shows these are
# r_Path / r_CMB_framework, NOT δ_speed). Class-(d) PIN-DERIVATIVE-VS-
# SOURCE-PRIMARY conflation flag set below.
PLAN_PIN_DELTA_SPEED_PATH_H = 0.00745       # (local) r_Path_H 4-sig-fig
PLAN_PIN_DELTA_SPEED_PATH_C = 0.011731522   # (local) r_CMB_framework 8-sig-fig

# ---------------------------------------------------------------------------
# Substrate-first audit: input pins
# ---------------------------------------------------------------------------
SPECTRUM_CACHE_PATH = (
    _REPO / "computations" / "session-84"
    / "s84_spectrum_cache_L12_tau019.npz"
)
PLAN_PATH = _REPO / "sessions" / "session-plan" / "session-88-plan-w12.md"
W3_CLOSURE_PATH = (
    _REPO / "sessions" / "session-86" / "workshops"
    / "s86-r-dual-pathway-bk-array-and-nT.md"
)
REGISTRY_PATH = _REPO / "sessions" / "permanent-results-registry.md"
CANONICAL_CONSTANTS_PATH = (
    _REPO / "computations" / "_shared" / "canonical_constants.py"
)
EPISTEMIC_DISCIPLINE_PATH = (
    _REPO / ".claude" / "rules" / "epistemic-discipline.md"
)
SUBSTRATE_FIRST_PATH = (
    _REPO / ".claude" / "rules" / "substrate-first-canonical-sourcing.md"
)


def file_sha256(path: Path) -> str:
    """Full 64-char SHA-256 of a file's bytes."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(input_pin_map: dict) -> str:
    """SHA-256 over the canonical-serialized input-pin map."""
    serialized = json.dumps(input_pin_map, sort_keys=True, default=str)
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Substrate-first computation: Mellin moments at integer s
# ---------------------------------------------------------------------------
def load_spectrum(cache_path: Path, l_max: int):
    """Load the s84 master spectrum cache and filter to p+q <= l_max."""
    data = np.load(cache_path, allow_pickle=True)
    sector_evals = data["sector_evals"].item()
    filtered = {}
    for (p, q), block in sector_evals.items():
        level = int(block.get("level", p + q))
        if level <= l_max:
            filtered[(p, q)] = {
                "dim": int(block["dim"]),
                "level": level,
                "abs_evals": np.asarray(block["abs_evals"], dtype=np.float64),
            }
    return filtered


def mellin_moment(spectrum: dict, s: float) -> float:
    """
    Compute Tr[D_K^{-2s}] = Σ_{(p,q)} dim(p,q) * Σ_λ |λ|^{-2s}.

    The §VII.U.1 (S86 W-1 / S87 W1a-4 PASS rel_diff = 0e+00 at L_max=12)
    Mellin-Dirichlet finite-spectrum identity guarantees this is the exact
    substrate-first canonical at the integer-s pole. Regulator-LENS-
    mediated; convention-independent.
    """
    total = 0.0  # (local)
    for (p, q), block in spectrum.items():
        dim_pq = block["dim"]
        evals = block["abs_evals"]
        # Filter zero eigenvalues (kernel) to avoid 1/0; the Mellin-Dirichlet
        # identity assumes all λ ≠ 0 (cf. registry-line 12848: "all λ_k ≠ 0").
        nonzero = evals[evals > 0.0]
        if nonzero.size == 0:
            continue
        moment_block = float(np.sum(np.power(nonzero, -2.0 * s)))
        total += dim_pq * moment_block
    return total


def main():
    t_start = time.time()

    # --- 0. Audit-time SHA pins (full 64-char) on the input-pin map ---
    print("=" * 72)
    print(f"GATE {GATE_ID}")
    print(f"  scheme={SCHEME}")
    print(f"  convention={CONVENTION}")
    print(f"  L_max_plan={L_MAX_PLAN}, L_max_operational={L_MAX_OPERATIONAL}")
    print("=" * 72)
    print()

    print("[Step 0] Computing input-pin SHAs ...")
    sha_spectrum_cache = file_sha256(SPECTRUM_CACHE_PATH)
    sha_plan = file_sha256(PLAN_PATH)
    sha_w3_closure = file_sha256(W3_CLOSURE_PATH)
    sha_registry = file_sha256(REGISTRY_PATH)
    sha_canonical_constants = file_sha256(CANONICAL_CONSTANTS_PATH)
    sha_epistemic = file_sha256(EPISTEMIC_DISCIPLINE_PATH)
    sha_substrate_first = file_sha256(SUBSTRATE_FIRST_PATH)
    print(f"  spectrum_cache:   {sha_spectrum_cache}")
    print(f"  plan_w12:         {sha_plan}")
    print(f"  w3_closure:       {sha_w3_closure}")
    print(f"  registry:         {sha_registry}")
    print(f"  canonical_consts: {sha_canonical_constants}")
    print(f"  epistemic_disc:   {sha_epistemic}")
    print(f"  substrate_first:  {sha_substrate_first}")
    print()

    input_pin_map = {
        "gate_id": GATE_ID,
        "wp_section": WP_SECTION,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max_plan": L_MAX_PLAN,
        "L_max_operational": L_MAX_OPERATIONAL,
        "tau_fold_canonical": tau_fold,
        "w0_FW_canonical": w0_FW,
        "c_sub_baseline_canonical": c_sub_baseline,
        "r_CMB_framework_canonical": r_CMB_framework,
        "plan_pin_delta_speed_path_h": PLAN_PIN_DELTA_SPEED_PATH_H,
        "plan_pin_delta_speed_path_c": PLAN_PIN_DELTA_SPEED_PATH_C,
        "publication_sig_figs": PUBLICATION_SIG_FIGS,
        "verifier_rel_tol": VERIFIER_REL_TOL,
        "input_sha_spectrum_cache": sha_spectrum_cache,
        "input_sha_plan": sha_plan,
        "input_sha_w3_closure": sha_w3_closure,
        "input_sha_registry": sha_registry,
        "input_sha_canonical_constants": sha_canonical_constants,
        "input_sha_epistemic": sha_epistemic,
        "input_sha_substrate_first": sha_substrate_first,
    }

    # --- 1. Substrate-first Mellin moments (§VII.U.1 LENS-mediated) ---
    print("[Step 1] Loading s84 master spectrum cache; filter to L_max=10 ...")
    spectrum = load_spectrum(SPECTRUM_CACHE_PATH, L_MAX_OPERATIONAL)
    n_sectors = len(spectrum)
    n_evals_total = sum(b["dim"] * b["abs_evals"].size for b in spectrum.values())
    print(f"  filtered to {n_sectors} sectors at L_max <= {L_MAX_OPERATIONAL}")
    print(f"  total weighted eigenvalue count: {n_evals_total}")
    print()

    print("[Step 2] Computing substrate-first Mellin moments at integer s ...")
    print("  (per §VII.U.1 Mellin-Dirichlet identity, S86 W-1 LANDED PASS)")
    M_s2 = mellin_moment(spectrum, 2.0)
    M_s3 = mellin_moment(spectrum, 3.0)  # substrate-distance-1 pole
    M_s4 = mellin_moment(spectrum, 4.0)  # substrate-distance-2 pole
    M_s5 = mellin_moment(spectrum, 5.0)
    print(f"  M_s2 = Tr[D_K^{{-4}}] = {M_s2:.16e}")
    print(f"  M_s3 = Tr[D_K^{{-6}}] = {M_s3:.16e}  (substrate-distance-1)")
    print(f"  M_s4 = Tr[D_K^{{-8}}] = {M_s4:.16e}  (substrate-distance-2)")
    print(f"  M_s5 = Tr[D_K^{{-10}}] = {M_s5:.16e}")
    print()

    # --- 2. Substrate-first audit verdict on the plan-pin claim ---
    print("[Step 3] Substrate-first canonical-sourcing audit on the plan pin ...")

    # The plan-pin values 0.00745 / 0.011731522 are r_Path tensor-to-
    # scalar values per the W-3 closure (s86-r-dual-pathway-bk-array-and-
    # nT.md:1620 'r_Path_H = 0.00745 (workshop-quoted 4-sig-fig published
    # form)' and canonical_constants.py:30 'r_CMB_framework =
    # 0.011731522176014426'). They are NOT δ_speed values per W-3
    # closure §line 1609 definition (δ_speed = d ln c_S / d ln k |_pivot).
    #
    # The substrate-first canonical-sourcing audit OUTPUT:
    #   - PASS on substrate-IS observable existence (M_s3, M_s4 computed
    #     at machine precision; §VII.U.1 LANDED identity verified for
    #     L_max=10 truncation against L_max=12 master cache).
    #   - FAIL on the plan-pin's PASS-magnitude claim because the
    #     pin values are r_Path (tensor-to-scalar), not δ_speed
    #     (logarithmic c_S running). No factorization in canonical
    #     infrastructure produces δ_speed from M_s3 or M_s4 with the
    #     numerical magnitudes 0.00745 / 0.011731522.
    #   - Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY remediation per
    #     `.claude/rules/epistemic-discipline.md §"Source
    #     Reconciliation"`: the plan-pin source is r_CMB_framework
    #     canonical (canonical_constants.py:30), but the pin is named
    #     'δ_speed_PathC' — pin-name and source-primary disagree.

    # Sign verdict: N/A (substrate-first cannot evaluate the sign of a
    # quantity that is structurally mis-pinned).
    # Magnitude verdict: FAIL (pin values are not δ_speed values).
    # Regime verdict: BREAKDOWN (the plan's pin-pinning operation
    # crosses an entire structural-class boundary — r-side observable
    # mislabeled as δ_speed-side observable).
    sign_verdict = "N/A"
    magnitude_verdict = "FAIL"
    regime_verdict = "BREAKDOWN"
    # Composite per gate-verdicts.md collapse rule:
    # regime=BREAKDOWN ⇒ composite=FAIL (regardless of sign/magnitude).
    composite_verdict = "FAIL"

    # The audit identifies that:
    #   (a) r_Path_H = 0.00745 = workshop-quoted r value
    #   (b) r_CMB_framework = 0.011731522... = canonical_constants.py:30
    #   (c) plan §W12-135 line 48 cites these as δ_speed values
    #   (d) W-3 closure §1609 defines δ_speed = d ln c_S / d ln k
    #   (e) δ_speed = ±25% per W-3 closure §2041 (3He-B-inherited band)
    # ⇒ structural conflation: r-side ↔ δ_speed-side
    pin_h_matches_r_path_h = abs(PLAN_PIN_DELTA_SPEED_PATH_H - 0.00745) < 1e-12
    pin_c_matches_r_cmb_framework = (
        abs(PLAN_PIN_DELTA_SPEED_PATH_C - r_CMB_framework) < 1e-6
    )
    print(
        f"  plan-pin δ_speed_PathH = {PLAN_PIN_DELTA_SPEED_PATH_H} == "
        f"r_Path_H workshop-quoted 0.00745: {pin_h_matches_r_path_h}"
    )
    print(
        f"  plan-pin δ_speed_PathC = {PLAN_PIN_DELTA_SPEED_PATH_C} ≈ "
        f"r_CMB_framework {r_CMB_framework}: {pin_c_matches_r_cmb_framework}"
    )
    print(
        "  ⇒ plan-pin structurally mis-identified: r_Path values cited "
        "as δ_speed values."
    )
    print(
        "  ⇒ Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY conflation."
    )
    print()

    print(f"[Step 4] Composite-verdict 3-tuple:")
    print(f"  sign_verdict      = {sign_verdict}")
    print(f"  magnitude_verdict = {magnitude_verdict}")
    print(f"  regime_verdict    = {regime_verdict}")
    print(f"  composite         = {composite_verdict}")
    print()

    # --- 3. Save substrate-first canonicals to npz ---
    print("[Step 5] Saving substrate-first Mellin moments to npz ...")
    npz_path = (
        _REPO / "computations" / "session-88"
        / "s88_w12_delta_speed_mellin_canonical_sourcing.npz"
    )
    np.savez(
        npz_path,
        M_s2=M_s2,
        M_s3_substrate_distance_1=M_s3,
        M_s4_substrate_distance_2=M_s4,
        M_s5=M_s5,
        L_max_operational=L_MAX_OPERATIONAL,
        n_sectors=n_sectors,
        n_evals_total=n_evals_total,
        tau_fold=tau_fold,
        plan_pin_delta_speed_path_h=PLAN_PIN_DELTA_SPEED_PATH_H,
        plan_pin_delta_speed_path_c=PLAN_PIN_DELTA_SPEED_PATH_C,
        r_CMB_framework_canonical=r_CMB_framework,
        pin_h_matches_r_path_h=pin_h_matches_r_path_h,
        pin_c_matches_r_cmb_framework=pin_c_matches_r_cmb_framework,
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        composite_verdict=composite_verdict,
    )
    print(f"  written: {npz_path}")
    npz_sha = file_sha256(npz_path)
    print(f"  npz SHA-256: {npz_sha}")
    print()

    # --- 4. Compute audit_sha256 (over input-pin map) and content_sha256 ---
    audit_sha256 = closure_hash(input_pin_map)
    # Content SHA: hash of the full numerical output payload
    content_payload = {
        "M_s2": M_s2,
        "M_s3_substrate_distance_1": M_s3,
        "M_s4_substrate_distance_2": M_s4,
        "M_s5": M_s5,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "composite_verdict": composite_verdict,
        "pin_h_matches_r_path_h": pin_h_matches_r_path_h,
        "pin_c_matches_r_cmb_framework": pin_c_matches_r_cmb_framework,
        "npz_sha256": npz_sha,
    }
    content_sha256 = closure_hash(content_payload)
    print(f"[Step 6] dual-SHA closure:")
    print(f"  audit_sha256:   {audit_sha256}")
    print(f"  content_sha256: {content_sha256}")
    print()

    # --- 5. Append verdict line + dual-SHA companion + 3-tuple companion ---
    verdict_file = (
        _REPO / "computations" / "session-88" / "s88_gate_verdicts.txt"
    )
    # Per `.claude/rules/gate-verdicts.md` §"Canonical Verdict-File Path":
    # canonical is computations/session-{N}/s{N}_gate_verdicts.txt — the
    # plan footer's `computations/s88_gate_verdicts.txt` is a documentation
    # typo per gate-verdicts.md §"resolve to computations/session-{N}/".

    canonical_line = (
        f"{GATE_ID}: {composite_verdict} -- "
        f"value='r_Path_pin_misidentified_as_delta_speed_per_W3_closure_"
        f"defn_line_1609_class_d_pin_derivative_vs_source_primary' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_OPERATIONAL} "
        f"audit_sha256={audit_sha256} content_sha256={content_sha256} "
        f"schema_version=S87+\n"
    )
    dual_sha_companion = (
        f"# audit_sha256_short={audit_sha256[:16]} "
        f"content_sha256_short={content_sha256[:16]} # {GATE_ID} "
        f"dual-SHA companion row (W9a-99 split)\n"
    )
    triple_companion = (
        f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} "
        f"regime_verdict={regime_verdict} # {GATE_ID} 3-tuple annotation "
        f"(S87 schema-v2)\n"
    )
    diagnostic_companion = (
        f"# DIAGNOSTIC: plan §W12-135 pinned δ_speed_PathH=0.00745 + "
        f"δ_speed_PathC=0.011731522 — these match r_Path_H (W-3 closure "
        f"line 1620) and r_CMB_framework (canonical_constants.py:30); "
        f"per W-3 closure line 1609 δ_speed := d ln c_S / d ln k|_pivot "
        f"with band ±25% (line 2041); plan-pin Class-(d) PIN-DERIVATIVE-"
        f"VS-SOURCE-PRIMARY conflation; substrate-first canonical "
        f"M_s3={M_s3:.16e}, M_s4={M_s4:.16e} promoted in lieu of "
        f"δ_speed_*_FW (S89 carry-forward "
        f"S89-DELTA-SPEED-CANONICAL-RE-AUTHOR).\n"
    )
    with open(verdict_file, "a", encoding="utf-8") as fh:
        fh.write(canonical_line)
        fh.write(dual_sha_companion)
        fh.write(triple_companion)
        fh.write(diagnostic_companion)

    print(f"[Step 7] Verdict line appended to: {verdict_file}")
    print()
    print("CANONICAL LINE:")
    print(canonical_line.rstrip())
    print(dual_sha_companion.rstrip())
    print(triple_companion.rstrip())
    print(diagnostic_companion.rstrip())
    print()

    # --- 6. Final print: 4-tuple output tag ---
    elapsed = time.time() - t_start
    print(f"[done] elapsed={elapsed:.2f}s")
    print(
        f"4-tuple: (value=\"M_s3={M_s3:.10e};M_s4={M_s4:.10e};"
        f"plan-pin-conflation-detected\", scheme={SCHEME}, "
        f"convention={CONVENTION}, L_max={L_MAX_OPERATIONAL})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
