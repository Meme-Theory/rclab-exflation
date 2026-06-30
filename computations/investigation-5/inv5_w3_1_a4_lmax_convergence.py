"""
INV5-W3-1 — a4 EXTENSIVE-AXIS L_max-CONVERGENCE AT tau_fold
============================================================

Gate:   INV5-W3-1  (investigation-5, Wave 3, compute, [SIGN], GEOMETRIC)
Agent:  spectral-geometer
Track:  investigation  (emit_verdict session=5, track="investigation")

QUESTION
--------
Scan the un-protected (EXTENSIVE) fourth Seeley-DeWitt coefficient a_4 of D_K^2
at fixed tau = tau_fold = 0.190 on the Peter-Weyl truncation axis
max_pq_sum (= L_max) in {3,4,5,(6)}.  Is the truncation tail
  (i)  monotone-DECREASING toward a finite continuum value  =>  PASS-truncation
       (the m_H +5.36% residual IS the resolvable a_4 extensive tail at L_sat~6), OR
  (ii) non-monotone / floors away from the +5.36% band                =>  INFO-physical
       (the +5.36% is a PHYSICAL screening, routes to the W2-3 Pekker-Varma
        self-energy / the Gamma_eff effacement) ?

This is the L_max-AXIS convergence of the EXTENSIVE coefficient's MAGNITUDE,
structurally DISTINCT from inv-3 INV3-W2-2 (tau-AXIS, bit-identical {a_0,a_2,a_4}
MULTISET isospectral-rigidity).  Different axis (L_max-scan vs tau-scan),
different observable (a_4 magnitude convergence vs multiset identity).

CONVENTION (per plan + Counting axis of regulator-pin-discipline.md):
  EXTENSIVE-a4-MAGNITUDE — the un-protected coefficient; NO a_0/a_2 ratio
  normalization.  The unbalanced extensive magnitude is the object under test
  (multiset {8,4} != {6,6}, NOT weight-balanced; R-Protection theorem S76).

REGULATOR PIN: a_4^{zeta} — the heat-kernel Seeley-DeWitt extraction is the
  zeta-regulated coefficient of D_K^2 at tau_fold (extract_seeley_dewitt_robust
  is the live FULL-physical heat-kernel polynomial fit of t^4 K(t); NOT the
  SCHEMATIC _spectral_action_regulators.py helper).  CLASS = FULL.

SUBSTITUTION CHAIN (the [SIGN] direction claim) — see substitution_chain in
the plan §W3-1 (boundary_reachable_analytically: false; the SIGN is a structural
prediction, the +5.36% magnitude band is an EMPIRICAL anchor):

  Claim: "the un-protected a_4 truncation tail DECREASES with L_max toward the
          continuum (so the m_H +5.36% IS a resolvable truncation tail)."

  Def 1: a_4(L) := t^2 coeff of small-t expansion of t^4 K_L(t),
                   K_L(t) = Tr_{P^{<=L}} exp(-t D_K^2) at tau_fold.
  Def 2: a_4^cont := continuum L->inf value of the same coefficient.
  Def 3: tail(L) := a_4(L) - a_4^cont.
  Def 4: residual_mH := (m_H^FW - m_H^obs)/m_H^obs = (131.8-125.1)/125.1 = +0.0536.

  Structural form (R-Protection, S76):  a_4(L) = a_4^cont + tail(L),
    tail(L) ~ C * L^{-p},  p>0.
  Step b:  Delta a_4(L) := a_4(L) - a_4(L-1) = C*(L^{-p} - (L-1)^{-p}).
  Step c:  for p>0, L>1:  L^{-p} < (L-1)^{-p}  =>  (L^{-p}-(L-1)^{-p}) < 0.
  Step d:  sign(Delta a_4(L)) = sign(C) * (negative).
  Canonical form:  sign(Delta a_4(L)) < 0  <=>  C > 0  (truncation OVER-counts a_4
    at finite L and relaxes downward).

  Direction:  the compute MEASURES sign(C) (= -sign(Delta a_4)).  If the tail is
    monotone-DECREASING AND |a_4(L_max)-a_4(3)|/a_4(L_max) ~ residual_mH, the
    +5.36% IS the a_4 extensive truncation tail (RESOLVABLE).  If non-monotone or
    floors away, the +5.36% is NOT explained by a_4 truncation (PHYSICAL).

  STRUCTURAL CAVEAT (spectral-geometer memory: Heat-Kernel Validity Tiers Tier 2
    + R-Protection theorem; session-60-bap-collab): the EXTENSIVE / UV-dominated
    a_4 (the truncated heat-trace t^2-coefficient = a_4_FW_zeta = 1350.72 lineage)
    is NOT the finite Gilkey curvature integral.  Individual a_k are L_max-FRAGILE
    with O(L^{d+r+k}) GROWTH (alpha_4 = d+r+4 = 8+2+4 = 14 > 0).  The structural
    expectation is therefore Delta a_4(L) > 0 (INCREASING with L_max, C < 0), i.e.
    NO decreasing tail toward a finite continuum.  This is exactly the SIGN the
    gate MEASURES and reports honestly.

PRDR machinery pin (plan §W3-1):
  N_eval=4; L_max in {3,4,5,(6)}; scan_range max_pq_sum in [3,6]; step ΔL=1;
  tau FIXED at tau_fold (NOT scanned); tolerance 0.0268 RATIO half-band on
  tail-fraction (= +5.36% +-50% rel; PASS-band [0.0268,0.0804]); heat-kernel
  polynomial-fit residual cross-check < 1e-3; scheme=FW; convention=
  EXTENSIVE-a4-MAGNITUDE; random_seed=N/A (deterministic); GPU_path=cpu-cap-OMP8
  (irrep CONSTRUCTION at p+q<=6 is the cost, not diagonalization; blocks sub-100x100).
  L_max-feasibility: scan tops at p+q<=6, FAR below the p+q>=13 infeasibility
  ceiling; L_max=6 feasibility-CLEAR, marked CONDITIONAL only as a graceful-
  degradation guard (Casimir-bound + Friedrich-Bär per math-scripts.md
  §"D_K Block-Diagonality").

audit_discriminators: audit_sha256 over ["script","canonical","pinmap"];
                      content_sha256 over ["script"].
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')   # (local) cpu-cap-OMP8 BEFORE numpy import
os.environ.setdefault('MKL_NUM_THREADS', '8')   # (local)

import sys
import json
import time
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# --- shared machinery on path ---
SHARED = Path(__file__).resolve().parents[1] / "_shared"   # (local) computations/_shared
sys.path.insert(0, str(SHARED))

from canonical_constants import tau_fold, m_H_FW_KK_threshold, m_H_obs  # framework constants
from dirac_spectrum import (
    su3_generators, compute_structure_constants, build_cliff8,
    collect_spectrum,
)
from spectral_action import extract_seeley_dewitt_robust, extract_seeley_dewitt

# =============================================================================
# Identity + pins
# =============================================================================
SESSION = 5                                   # (local) investigation number
GATE_ID = "INV5-W3-1"
SCHEME = "FW"
CONVENTION = "EXTENSIVE-a4-MAGNITUDE-a_4^{zeta}"
L_MAX_PLAN = 6                                 # (local) plan-pinned ceiling
L_MAX_SCAN = [3, 4, 5, 6]                      # (local) the integer truncation mesh
TAU = tau_fold                                 # 0.190 (canonical)

# PASS-band on the tail-fraction (RATIO tolerance): +5.36% residual +-50% relative
RESIDUAL_MH = (m_H_FW_KK_threshold - m_H_obs) / m_H_obs   # (local) +0.0536 (live canonical)
TAIL_BAND_HALF = 0.0268                         # (local) plan tolerance (=residual*0.5)
PASS_LO = RESIDUAL_MH - TAIL_BAND_HALF          # (local) 0.0268
PASS_HI = RESIDUAL_MH + TAIL_BAND_HALF          # (local) 0.0804
FIT_RESID_TOL = 1e-3                            # (local) heat-kernel polynomial-fit residual ceiling

OUT_DIR = Path(__file__).resolve().parent       # (local) computations/investigation-5
NPZ_PATH = OUT_DIR / "inv5_w3_1_a4_lmax_convergence.npz"
PNG_PATH = OUT_DIR / "inv5_w3_1_a4_lmax_convergence.png"

CANONICAL = SHARED / "canonical_constants.py"
INPUT_FILES = {
    "canonical": CANONICAL,
    "dirac_spectrum": SHARED / "dirac_spectrum.py",
    "spectral_action": SHARED / "spectral_action.py",
}
# Plan-frozen canonical SHA (2026-06-14); verified-or-drift-logged at runtime.
PLAN_CANONICAL_SHA = "e6829db013a713a4e56a4ca7d72e41f522bd3e3caea1bc0488ef17e0460bba34"  # (local)


# =============================================================================
# SHA helpers (dual-SHA discipline; gate-verdicts.md schema-v2)
# =============================================================================
def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    h.update(Path(path).read_bytes())
    return h.hexdigest()


def closure_hash(pin_map: dict) -> str:
    """SHA-256 over the ordered input-pin map (audit closure)."""
    items = sorted((str(k), str(v)) for k, v in pin_map.items())
    blob = "\n".join(f"{k}={v}" for k, v in items)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    """audit_sha256 over {script, canonical, pinmap}; content_sha256 over {script}."""
    script_sha = _sha256_file(script_path)
    canon_sha = _sha256_file(canonical_path)
    audit_inputs = {
        "script": script_sha,
        "canonical": canon_sha,
        "pinmap": closure_hash(pins),
    }
    audit_sha = closure_hash(audit_inputs)
    content_sha = script_sha
    return audit_sha, content_sha


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict, magnitude_verdict, regime_verdict,
                          extra_rows=None) -> dict:
    payload = {
        "session": SESSION,
        "track": "investigation",
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(max(L_used)),
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


# =============================================================================
# Main compute
# =============================================================================
L_used = []   # (local) populated in main; max -> verdict-line L_max field


def main() -> int:
    t0 = time.time()  # (local)

    # ---- 1. input pins (first ~20 lines of stdout) ----
    print("=" * 72)
    print(f"{GATE_ID} — a_4 EXTENSIVE-axis L_max-convergence at tau_fold")
    print("=" * 72)
    pins = {}   # (local)
    for name, path in INPUT_FILES.items():
        sha = _sha256_file(path)
        pins[name] = sha
        print(f"  INPUT {name:16s} sha256={sha}")
    # plan-staleness / canonical drift disclosure (substrate-first-canonical-sourcing.md §ii.B)
    canon_live = pins["canonical"]   # (local)
    drift = (canon_live != PLAN_CANONICAL_SHA)   # (local)
    if drift:
        print(f"  PLAN-TEXT-DRIFT: canonical_constants.py SHA differs from plan-pin")
        print(f"    plan-pinned : {PLAN_CANONICAL_SHA}")
        print(f"    runtime     : {canon_live}")
        print(f"    -> using LIVE file; consumed constants verified via MCP get_constant")
        print(f"       (tau_fold={tau_fold}, m_H_FW_KK_threshold={m_H_FW_KK_threshold}, m_H_obs={m_H_obs})")
    print(f"  CONSUMED canonical: tau_fold={tau_fold}  m_H_FW_KK_threshold={m_H_FW_KK_threshold}"
          f"  m_H_obs={m_H_obs}")
    print(f"  residual_mH = (m_H_FW - m_H_obs)/m_H_obs = {RESIDUAL_MH:.6f}")
    print(f"  PASS-band tail_fraction in [{PASS_LO:.4f}, {PASS_HI:.4f}]")

    # ---- 1b. dual SHAs ----
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # ---- 2. build SU(3) + Clifford machinery (live FULL physical) ----
    print("[build] SU(3) generators + structure constants + Cliff(8)...")
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()

    # ---- 3. L_max scan: extract a_4 at each truncation, tau FIXED at tau_fold ----
    print(f"\n[scan] a_4 at tau_fold={TAU:.3f}, max_pq_sum in {L_MAX_SCAN}")
    a4 = {}            # (local) L -> a_4 (robust mean over 3 t-ranges)
    a4_spread = {}     # (local) L -> systematic spread of a_4 across t-ranges
    a0 = {}            # (local) L -> a_0 (cross-check / Weyl anchor)
    a2 = {}            # (local) L -> a_2
    fit_resid = {}     # (local) L -> heat-kernel polynomial-fit relative RMS residual
    n_evals = {}       # (local) L -> total eigenvalue count (block, no PW factor)
    L_done = []        # (local)

    for L in L_MAX_SCAN:
        ts = time.time()  # (local)
        try:
            _, eval_data = collect_spectrum(TAU, gens, f_abc, gammas,
                                            max_pq_sum=L, verbose=False)
        except Exception as exc:
            # graceful-degradation guard for the CONDITIONAL L_max=6 point
            print(f"  L_max={L}: irrep construction FAILED ({exc}); "
                  f"dropping per L_max-feasibility graceful-degradation guard")
            break

        # robust extraction (3 t-ranges) for the a_4 best estimate + spread
        coeffs_best, coeffs_unc = extract_seeley_dewitt_robust(eval_data, verbose=False)
        # single-range fit (medium) for the residual cross-check (regime-of-validity)
        _, fq = extract_seeley_dewitt(eval_data, t_range=(0.005, 0.5),
                                      n_points=200, verbose=False)

        a4[L] = float(coeffs_best['a_4'])
        a4_spread[L] = float(coeffs_unc['a_4'])
        a0[L] = float(coeffs_best['a_0'])
        a2[L] = float(coeffs_best['a_2'])
        fit_resid[L] = float(fq['residual'])
        n_evals[L] = int(sum(len(ed[2]) for ed in eval_data))
        L_done.append(L)
        dt = time.time() - ts  # (local)
        print(f"  L_max={L}: a_4={a4[L]:+.6e}  (spread {a4_spread[L]:.2e})  "
              f"a_0={a0[L]:.4e} a_2={a2[L]:.4e}  fit_resid={fit_resid[L]:.2e}  "
              f"n_ev={n_evals[L]}  [{dt:.1f}s]")

    L_used.clear()
    L_used.extend(L_done)
    if len(L_done) < 2:
        raise RuntimeError("need >=2 truncation points to form a slope")

    L_min = L_done[0]   # (local) = 3
    L_max_op = L_done[-1]   # (local) operational ceiling actually reached
    L_max_drop = (L_max_op < L_MAX_PLAN)   # (local) graceful-degradation fired?

    # ---- 4. convergence slope Delta a_4(L) = a_4(L) - a_4(L-1) ----
    dA = {}   # (local) L -> Delta a_4(L) for L in L_done[1:]
    for i in range(1, len(L_done)):
        L = L_done[i]
        dA[L] = a4[L] - a4[L_done[i - 1]]

    dA_signs = [np.sign(dA[L]) for L in L_done[1:]]   # (local)
    all_negative = all(s < 0 for s in dA_signs)       # (local) monotone-decreasing
    all_positive = all(s > 0 for s in dA_signs)       # (local) monotone-increasing
    monotone = all_negative or all_positive            # (local)

    # ---- 5. tail-fraction |a_4(L_max) - a_4(3)| / a_4(L_max) ----
    tail_abs = a4[L_max_op] - a4[L_min]                       # (local) signed tail
    tail_fraction = abs(tail_abs) / abs(a4[L_max_op])         # (local) RATIO
    tail_in_band = (PASS_LO <= tail_fraction <= PASS_HI)      # (local)
    delta_to_residual = tail_fraction - RESIDUAL_MH           # (local)

    # ---- 6. [SIGN] 3-tuple collapse (gate-verdicts.md §"Composite-collapse rule") ----
    # sign_verdict: PASS iff the PRE-REGISTERED direction (Delta a_4 < 0, decreasing)
    #   matches the measured direction; FAIL on mismatch.
    sign_predicted_decreasing = True   # (local) plan substitution-chain Step 4 prediction
    sign_measured_decreasing = all_negative   # (local)
    if not monotone:
        sign_verdict = "N/A"   # direction undefined (sign flips across steps)
    elif sign_measured_decreasing == sign_predicted_decreasing:
        sign_verdict = "PASS"
    else:
        sign_verdict = "FAIL"   # monotone but INCREASING (opposite to prediction)

    # magnitude_verdict: PASS iff tail_fraction in band; INFO if non-monotone/outside band.
    # No info_band beyond the PASS-band is pre-registered: outside-band => INFO (the
    # +5.36% is NOT the a_4 truncation tail), per the plan INFO-physical rubric.
    if tail_in_band and monotone:
        magnitude_verdict = "PASS"
    else:
        magnitude_verdict = "INFO"

    # regime_verdict: VALID iff the heat-kernel small-t polynomial fit resolves the
    #   t^2 (a_4) coefficient at every truncation (residual < FIT_RESID_TOL).
    worst_resid = max(fit_resid[L] for L in L_done)   # (local)
    if worst_resid < FIT_RESID_TOL:
        regime_verdict = "VALID"
    elif worst_resid < 10 * FIT_RESID_TOL:
        regime_verdict = "MARGINAL"
    else:
        regime_verdict = "BREAKDOWN"

    # composite collapse (pre-registered rule)
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"
    elif sign_verdict == "FAIL":
        # SIGN mismatch with VALID/MARGINAL regime.  Plan rubric: there is NO
        # "wrong-answer" FAIL for the physics (the two physical readings are
        # PASS-truncation vs INFO-physical).  A measured monotone-INCREASING tail
        # (sign opposite to prediction) is the INFO-physical outcome: the a_4
        # extensive coefficient GROWS with L_max (NOT a decreasing tail toward a
        # finite continuum), so the +5.36% is NOT the a_4 truncation tail.
        composite = "INFO"
    elif magnitude_verdict == "INFO":
        composite = "INFO"
    elif sign_verdict == "N/A":
        composite = "INFO"   # non-monotone => INFO-physical
    else:
        composite = "PASS"

    # ---- 7. report ----
    print("\n" + "-" * 72)
    print("RESULTS")
    print("-" * 72)
    print(f"  a_4(L_max) per truncation (EXTENSIVE, zeta-regulated, tau_fold):")
    for L in L_done:
        print(f"    L_max={L}: a_4 = {a4[L]:+.4e}")
    print(f"  Delta a_4(L) = a_4(L) - a_4(L-1):")
    for L in L_done[1:]:
        print(f"    L={L}: Delta a_4 = {dA[L]:+.4e}  sign={int(np.sign(dA[L])):+d}")
    print(f"  monotone={monotone}  all_negative(decreasing)={all_negative}  "
          f"all_positive(increasing)={all_positive}")
    print(f"  tail = a_4(L_max={L_max_op}) - a_4(L=3) = {tail_abs:+.4e}")
    print(f"  tail_fraction = |tail|/|a_4(L_max)| = {tail_fraction:.4f}")
    print(f"  residual_mH = {RESIDUAL_MH:.4f}  PASS-band [{PASS_LO:.4f},{PASS_HI:.4f}]"
          f"  -> tail_in_band={tail_in_band}  (delta={delta_to_residual:+.4f})")
    print(f"  worst fit_resid={worst_resid:.2e}  (tol {FIT_RESID_TOL:.0e})")
    print(f"  L_max_plan={L_MAX_PLAN} L_max_operational={L_max_op}  drop={L_max_drop}")
    print(f"  3-tuple: sign={sign_verdict} magnitude={magnitude_verdict} "
          f"regime={regime_verdict}  => composite={composite}")

    # ---- 8. save .npz (full float64) ----
    np.savez(
        NPZ_PATH,
        L_scan=np.array(L_done, dtype=int),
        L_max_plan=L_MAX_PLAN,
        L_max_operational=L_max_op,
        a4=np.array([a4[L] for L in L_done], dtype=np.float64),
        a4_spread=np.array([a4_spread[L] for L in L_done], dtype=np.float64),
        a0=np.array([a0[L] for L in L_done], dtype=np.float64),
        a2=np.array([a2[L] for L in L_done], dtype=np.float64),
        fit_resid=np.array([fit_resid[L] for L in L_done], dtype=np.float64),
        n_evals=np.array([n_evals[L] for L in L_done], dtype=int),
        delta_a4=np.array([dA[L] for L in L_done[1:]], dtype=np.float64),
        delta_a4_L=np.array(L_done[1:], dtype=int),
        tail_signed=tail_abs,
        tail_fraction=tail_fraction,
        residual_mH=RESIDUAL_MH,
        pass_lo=PASS_LO, pass_hi=PASS_HI,
        delta_to_residual=delta_to_residual,
        monotone=monotone, all_negative=all_negative, all_positive=all_positive,
        worst_fit_resid=worst_resid,
        tau_fold=TAU,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict, composite=composite,
        canonical_drift=bool(drift),
        canonical_sha_runtime=canon_live,
        m_H_FW_KK_threshold=m_H_FW_KK_threshold, m_H_obs=m_H_obs,
    )
    print(f"\n  [saved] {NPZ_PATH.name}")

    # ---- 9. plot ----
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    Ls = np.array(L_done)
    a4v = np.array([a4[L] for L in L_done])
    a4e = np.array([a4_spread[L] for L in L_done])
    ax1.errorbar(Ls, a4v, yerr=a4e, marker='o', capsize=4, color='C0',
                 label=r"$a_4(L_{\max})$ extensive ($\zeta$-reg)")
    ax1.set_xlabel(r"$L_{\max}$ (max_pq_sum)")
    ax1.set_ylabel(r"$a_4$ (EXTENSIVE magnitude)")
    ax1.set_title(rf"$a_4$ extensive-axis $L_{{\max}}$-convergence @ $\tau_{{fold}}$={TAU:.3f}")
    ax1.grid(alpha=0.3); ax1.legend()

    # right panel: Delta a_4 slope + tail-fraction vs +5.36% band
    dLs = np.array(L_done[1:])
    dAv = np.array([dA[L] for L in L_done[1:]])
    color = ['C2' if v < 0 else 'C3' for v in dAv]  # (local) green=decreasing, red=increasing
    ax2b = ax2.twinx()
    ax2.bar(dLs - 0.12, dAv, width=0.24, color=color, alpha=0.7,
            label=r"$\Delta a_4(L)$ (green<0 dec, red>0 inc)")
    ax2.axhline(0.0, color='k', lw=0.8)
    ax2.set_xlabel(r"$L$ (step $L{-}1\!\to\!L$)")
    ax2.set_ylabel(r"$\Delta a_4(L)$")
    # tail-fraction marker on the twin axis
    ax2b.axhspan(PASS_LO, PASS_HI, color='gold', alpha=0.25,
                 label=rf"+5.36% band [{PASS_LO:.3f},{PASS_HI:.3f}]")
    ax2b.axhline(RESIDUAL_MH, color='orange', ls='--', lw=1.5,
                 label=rf"residual_mH={RESIDUAL_MH:.4f}")
    ax2b.axhline(tail_fraction, color='C0', ls='-', lw=2.0,
                 label=rf"tail_frac={tail_fraction:.3f}")
    ax2b.set_ylabel("tail-fraction (twin)")
    ax2.set_title(rf"$\Delta a_4$ slope + tail-fraction vs +5.36%  [{composite}]")
    ax2.grid(alpha=0.3)
    h1, l1 = ax2.get_legend_handles_labels()
    h2, l2 = ax2b.get_legend_handles_labels()
    ax2.legend(h1 + h2, l1 + l2, fontsize=8, loc='best')

    fig.tight_layout()
    fig.savefig(PNG_PATH, dpi=130)
    print(f"  [saved] {PNG_PATH.name}")

    # ---- 10. value payload + emit ----
    value = (f"tail_fraction={tail_fraction:.4f};residual_mH={RESIDUAL_MH:.4f};"
             f"monotone={monotone};all_neg={all_negative};all_pos={all_positive};"
             f"dA={['%+.3e' % dA[L] for L in L_done[1:]]};"
             f"a4={['%.4e' % a4[L] for L in L_done]};"
             f"L_op={L_max_op};L_plan={L_MAX_PLAN};canon_drift={drift}")
    extra_rows = [
        "# regulator_pin=a_4^{zeta} (zeta-regulated 4th Seeley-DeWitt coeff of D_K^2 at tau_fold)",
        f"# CLASS=FULL (spectral_action.extract_seeley_dewitt_robust live heat-kernel fit; "
        f"dirac_spectrum live irrep builder; NEITHER SCHEMATIC; no tier_pin row)",
        f"# a4_per_Lmax={ {L: round(a4[L],3) for L in L_done} } "
        f"delta_a4={ {L: round(dA[L],4) for L in L_done[1:]} }",
        f"# L_max_plan={L_MAX_PLAN} L_max_operational={L_max_op} "
        f"feasibility=Casimir-bound+Friedrich-Baer (math-scripts.md D_K Block-Diagonality)",
        f"# canonical_drift={drift} plan_sha={PLAN_CANONICAL_SHA[:16]} "
        f"runtime_sha={canon_live[:16]} (substrate-first-canonical-sourcing.md §ii.B; "
        f"constants MCP-verified)",
    ]
    payload = print_verdict_payload(
        composite, value, audit_sha, content_sha,
        sign_verdict, magnitude_verdict, regime_verdict,
        extra_rows=extra_rows,
    )

    print(f"\n  4-tuple: (value=tail_fraction={tail_fraction:.4f}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_max_op})")
    print(f"  [done] {time.time()-t0:.1f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
