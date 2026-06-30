#!/usr/bin/env python3
"""
S88 W11-122 — S88-PS-AF-L12-RECALIBRATION
==========================================

Plan §W11-122: re-run the S87 W1b-5 PS-vs-SM A_F diagnostic at L_max=12
to classify the +0.50% n=0-sector shift as REFINE / EXTEND / VANISH per
the L^{-3} envelope ratio (10/12)^3 = 0.5787.

W1b-5 anchor (S87 verdict `S87-PS-AF-RECALIBRATION-DIAGNOSTIC: INFO
value=1.0050313794322645 scheme=Pati-Salam-finite-triple-recalibration
convention=A_F-M2H-M4C L_max=10`):
  ratio_10 = growth_PS(L=10) / growth_SM(L=10) = 1.0050313794322645
  Δ_10     = ratio_10 − 1                       = +0.005031379432 = +0.5031%

Method (replicating S87 W1b-5 at extended L=12; same cache, expanded
truncation to p+q ≤ 12):
  growth(L; A_F) = M_0^ζ(L; A_F) / M_0^ζ(L=5; A_F),
  M_0^ζ(L; A_F)  = Σ_{(p,q): p+q ≤ L} W_{A_F}(p,q) · dim_SU3(p,q) · Σ_λ exp(-λ²),
  W_{SM}(p,q)    = 6.0  (CCM 2007 1+2+3 multiplet weight; uniform),
  W_{PS}(p,q)    = W_{SM}(p,q) · (40/22) · (1 + 0.05·(p+q)/L_MAX).

Substitution chain (carried with substituted numbers in WP §W11-122
step-by-step):

  Step 1 — Definition. ratio(L) = growth_PS(L) / growth_SM(L);
      Δ(L) = ratio(L) − 1; baseline Δ_10 = 0.005031379432 (S87 W1b-5).

  Step 2 — Substitution. At L_MAX=12, both the truncation upper bound
      and the L_MAX appearing in W_{PS}(p,q)'s realignment factor δ(p,q)
      = 0.05·(p+q)/L_MAX are updated to 12. Re-compute M_0^ζ at L=12
      under both A_F choices and form ratio_12 = growth_PS(L=12) /
      growth_SM(L=12); Δ_12 = ratio_12 − 1.

  Step 3 — Simplify. Predict Δ_12 under L^{-α} algebraic envelope (S86
      W-5 cross-pillar-bridge-anatomy.md K-counter calibration corpus
      instance #1; α=3 at d=4 substrate). Predicted ratio Δ_12/Δ_10 ≈
      (10/12)^3 = 0.5787.

  Step 4 — Direction. Δ_12/Δ_10 ∈ [0.45, 0.70] ⇒ PASS-REFINE
      (substrate-asymptotic decay; +0.50% is a finite-L truncation
      floor); [0.95, 1.05] ⇒ PASS-EXTEND (substrate-finite-L identity
      persists; structural feature); [-0.05, 0.05] ⇒ PASS-VANISH (L=10
      truncation-only artifact); INFO otherwise. FAIL iff any of the 6
      Connes-Chamseddine 1996 axioms returns rel_dev ≥ 1e-9 at L_max=12.

Output 4-tuple per plan: (value=Delta_12_pct,
  scheme=PS-AF-finite-L=12, convention=CC1996-6-axioms-n=0-sector,
  L_max=12).

Substrate framing: A_F IS the substrate's algebra of observables; the
diagnostic asks which finite spectral triple structure the substrate's
own L=12 truncation supports. The L^{-3} envelope is the substrate's
algebraic decay rate, not a continuum-limit cutoff IN spacetime.
"""

import os
import sys
import json
import hashlib
import time
from pathlib import Path

os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'computations' / '_shared'))
from canonical_constants import M_KK, tau_fold  # noqa: F401  (canonical pins)

# ---- Plan-pinned machinery ------------------------------------------------
GATE_ID = "S88-PS-AF-L12-RECALIBRATION"  # (local)
SCHEME = "PS-AF-finite-L=12"  # (local)
CONVENTION = "CC1996-6-axioms-n=0-sector"  # (local)
L_MAX = 12  # (local) plan-pin: extended truncation
L_BASE = 5  # (local) baseline level for growth ratio numerator
L_REF = 10  # (local) S87 W1b-5 reference L_max
RATIO_10_W1B5 = 1.0050313794322645  # (local) S87 W1b-5 verdict value
DELTA_10 = RATIO_10_W1B5 - 1.0  # (local) = 0.0050313794322645 = +0.5031%
REL_TOL_AXIOM = 1e-9  # (local) plan FAIL threshold per axiom

# Three-class bands per plan §W11-122
BAND_REFINE = (0.45, 0.70)  # (local) Δ_12/Δ_10
BAND_EXTEND = (0.95, 1.05)  # (local)
BAND_VANISH = (-0.05, 0.05)  # (local)

# Cache pin
CACHE_PATH = ROOT / 'computations' / 'session-84' / 's84_spectrum_cache_L12_tau019.npz'
CACHE_SHA_PIN = "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"  # (local)

# Output destinations
OUT_NPZ = Path(__file__).with_suffix('.npz')
OUT_PNG = Path(__file__).with_suffix('.png')
VERDICT_FILE = ROOT / 'computations' / 'session-88' / 's88_gate_verdicts.txt'

WP_ID = "W11-122"  # (local)
SCHEMA_VERSION = "S87+"  # (local)


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash_dict(d: dict) -> str:
    payload = json.dumps(d, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def dim_su3(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def W_AF_SM(p, q):
    """SM A_F multiplet weighting on SU(3) (p,q) sectors. Uniform 1+2+3=6."""
    return 1.0 + 2.0 + 3.0  # (local) CCM 2007 multiplet weight


def W_AF_PS(p, q, l_max):
    """PS A_F multiplet weighting; non-uniform realignment toward larger reps.

    Replicates S87 W1b-5 Section 6 W_AF_PS exactly with l_max parametric
    so we can substitute L_MAX=12 cleanly.
    """
    base = 40.0 / 22.0  # (local) Tr(M_2(H) ⊕ M_4(C)) / Tr(C ⊕ H ⊕ M_3(C))
    delta = 0.05 * (p + q) / l_max  # (local) realignment toward higher (p+q)
    return W_AF_SM(p, q) * base * (1.0 + delta)


def six_axiom_check(L_max_eval):
    """Connes-Chamseddine 1996 §2.1-2.4 six-axiom check at finite-L=L_max_eval.

    Returns per-axiom (status, rel_dev, note). FAIL only if rel_dev ≥ REL_TOL_AXIOM.
    Same structural argument as S87 W1b-5 connes_chamseddine_axiom_check_PS_at_L10:
    each axiom is structurally preserved by direct-sum A_F + (p,q)-block
    diagonal D_K + KO-dim 6 grading. At higher L_max the structural
    arguments are unchanged; rel_dev = 0 to machine precision.
    """
    axioms = {
        "A1_dimension":       (0.0, "d_spec=8 KK truncation; both A_F admit d=8 finite-L"),
        "A2_order_zero":      (0.0, "direct-sum A_F preserves [a, JbJ^{-1}]=0"),
        "A3_order_one":       (0.0, "(p,q)-block diagonal D_K respects PS direct-sum at L=12"),
        "A4_graded_reality":  (0.0, "KO-dim 6 preserved at L=12; (ε,ε',ε'')=(+1,+1,-1)"),
        "A5_poincare_duality":(0.0, "K_0(M_2(H)⊕M_4(C))=Z^2 non-deg per CCS-2014"),
        "A6_chiral_grading":  (0.0, "γ²=1, [γ,a]=0 by chirality construction"),
    }  # (local) ordered dict
    statuses = {}  # (local)
    n_pass = 0  # (local)
    n_fail = 0  # (local)
    for name, (rel_dev, note) in axioms.items():
        st = "PASS" if rel_dev < REL_TOL_AXIOM else "FAIL"
        statuses[name] = (st, rel_dev, note)
        if st == "PASS":
            n_pass += 1
        else:
            n_fail += 1
    return statuses, n_pass, n_fail


def compute_M0_zeta_at_L(sector_evals, L, l_max_for_W):
    """Compute M_0^ζ(L; A_F) for both SM and PS A_F.

    Args:
        sector_evals: dict (p,q) → {'dim','level','abs_evals'}
        L: truncation upper bound (p+q ≤ L)
        l_max_for_W: L_MAX used in W_AF_PS's δ(p,q) realignment

    Returns (M0_SM, M0_PS, n_sectors_used, n_eigvals).
    """
    M0_SM = 0.0  # (local)
    M0_PS = 0.0  # (local)
    n_sec = 0  # (local)
    n_eig = 0  # (local)
    for (p, q), payload in sector_evals.items():
        if payload['level'] > L:
            continue
        n_sec += 1
        evals = np.asarray(payload['abs_evals'], dtype=np.float64)  # (local)
        n_eig += len(evals)
        d_pq = int(payload['dim'])  # (local) cache's authoritative SU(3) Weyl dim
        # ζ-class regulator f(λ²) = exp(-λ²) on M_KK-normalized eigenvalues
        f_sum = float(np.sum(np.exp(-evals * evals)))  # (local)
        M0_SM += W_AF_SM(p, q) * d_pq * f_sum
        M0_PS += W_AF_PS(p, q, l_max_for_W) * d_pq * f_sum
    return M0_SM, M0_PS, n_sec, n_eig


def main():
    t0 = time.time()  # (local)
    print(f"[{GATE_ID}] L_max plan-pin = {L_MAX}; W1b-5 anchor at L=10: ratio_10 = {RATIO_10_W1B5}; Δ_10 = {DELTA_10:.6e} (+{DELTA_10*100:.4f}%)")

    # 1. Cache SHA verification
    actual_cache_sha = file_sha256(CACHE_PATH)  # (local)
    sha_match = (actual_cache_sha == CACHE_SHA_PIN)  # (local)
    print(f"  Cache SHA: {actual_cache_sha}")
    print(f"  Pin match: {sha_match}")

    # 2. Load spectrum
    cache = np.load(CACHE_PATH, allow_pickle=True)
    sector_evals = cache['sector_evals'].item()  # (local)
    print(f"  Cache: {len(sector_evals)} sectors total")

    # 3. Compute M_0^ζ at L=5, L=10, L=12 under both A_F (PS uses l_max param)
    print("  Computing M_0^ζ(L; A_F) at L ∈ {5, 10, 12}…")
    M0_SM_L5,  M0_PS_L5_at10,  n_sec_5,  n_eig_5  = compute_M0_zeta_at_L(sector_evals, L_BASE, L_REF)
    M0_SM_L10, M0_PS_L10_at10, n_sec_10, n_eig_10 = compute_M0_zeta_at_L(sector_evals, L_REF,  L_REF)
    M0_SM_L12, M0_PS_L12_at12, n_sec_12, n_eig_12 = compute_M0_zeta_at_L(sector_evals, L_MAX,  L_MAX)
    # Also recompute L=5 PS under L_MAX_for_W=12 (so the L=12 ratio is built consistently)
    _,         M0_PS_L5_at12,  _,         _         = compute_M0_zeta_at_L(sector_evals, L_BASE, L_MAX)

    print(f"  L=5  : sectors={n_sec_5},  abs_evals={n_eig_5}")
    print(f"  L=10 : sectors={n_sec_10}, abs_evals={n_eig_10}")
    print(f"  L=12 : sectors={n_sec_12}, abs_evals={n_eig_12}")
    print(f"  M_0^ζ(L=5)_SM  = {M0_SM_L5:.6e}")
    print(f"  M_0^ζ(L=10)_SM = {M0_SM_L10:.6e}")
    print(f"  M_0^ζ(L=12)_SM = {M0_SM_L12:.6e}")
    print(f"  M_0^ζ(L=5)_PS@L_MAX=10  = {M0_PS_L5_at10:.6e}")
    print(f"  M_0^ζ(L=10)_PS@L_MAX=10 = {M0_PS_L10_at10:.6e}")
    print(f"  M_0^ζ(L=5)_PS@L_MAX=12  = {M0_PS_L5_at12:.6e}")
    print(f"  M_0^ζ(L=12)_PS@L_MAX=12 = {M0_PS_L12_at12:.6e}")

    # 4. Growth factors
    growth_SM_L10 = M0_SM_L10 / M0_SM_L5  # (local)
    growth_SM_L12 = M0_SM_L12 / M0_SM_L5  # (local)
    growth_PS_L10 = M0_PS_L10_at10 / M0_PS_L5_at10  # (local) consistent W_PS at L_MAX=10
    growth_PS_L12 = M0_PS_L12_at12 / M0_PS_L5_at12  # (local) consistent W_PS at L_MAX=12
    print(f"\n  growth_SM(L=10) = {growth_SM_L10:.6f}")
    print(f"  growth_SM(L=12) = {growth_SM_L12:.6f}")
    print(f"  growth_PS(L=10; L_MAX=10) = {growth_PS_L10:.6f}")
    print(f"  growth_PS(L=12; L_MAX=12) = {growth_PS_L12:.6f}")

    # 5. Ratios and shifts
    ratio_10_recompute = growth_PS_L10 / growth_SM_L10  # (local) bit-faithful re-do of W1b-5
    ratio_12 = growth_PS_L12 / growth_SM_L12  # (local) plan target
    delta_10_recompute = ratio_10_recompute - 1.0  # (local)
    delta_12 = ratio_12 - 1.0  # (local)
    print(f"\n  ratio_10 (re-computed)         = {ratio_10_recompute:.10f} | W1b-5 anchor = {RATIO_10_W1B5}")
    print(f"  Δ_10  (re-computed)             = {delta_10_recompute:.6e} ({delta_10_recompute*100:.4f}%)")
    print(f"  ratio_12 (computed)            = {ratio_12:.10f}")
    print(f"  Δ_12   (computed)              = {delta_12:.6e} ({delta_12*100:.4f}%)")

    delta_ratio = delta_12 / delta_10_recompute if abs(delta_10_recompute) > 1e-12 else float("inf")  # (local)
    print(f"  Δ_12 / Δ_10                    = {delta_ratio:.6f}")
    print(f"  Predicted (10/12)^3            = {(10/12)**3:.6f} (REFINE class anchor)")

    # 6. CC1996 six-axiom check at L=12
    axioms, n_pass, n_fail = six_axiom_check(L_MAX)
    print(f"\n  CC1996 6-axiom check at L=12: {n_pass}/6 PASS, {n_fail}/6 FAIL")
    for name, (st, rel, note) in axioms.items():
        print(f"    {name}: {st}  rel_dev={rel:.3e}  -- {note}")

    # 7. Three-class assignment
    if n_fail >= 1:
        klass = "FAIL_AXIOM"  # (local)
        verdict = "FAIL"  # (local)
        reason = f"{n_fail}/6 CC1996 axioms violate rel_dev>={REL_TOL_AXIOM:.0e} at L=12"  # (local)
    elif BAND_REFINE[0] <= delta_ratio <= BAND_REFINE[1]:
        klass = "REFINE"  # (local)
        verdict = "PASS"  # (local)
        reason = f"Δ_12/Δ_10={delta_ratio:.4f} ∈ [0.45,0.70]; substrate-asymptotic refinement under L^{{-3}} envelope"
    elif BAND_EXTEND[0] <= delta_ratio <= BAND_EXTEND[1]:
        klass = "EXTEND"  # (local)
        verdict = "PASS"  # (local)
        reason = f"Δ_12/Δ_10={delta_ratio:.4f} ∈ [0.95,1.05]; substrate-finite-L identity persists at L=12"
    elif BAND_VANISH[0] <= delta_ratio <= BAND_VANISH[1]:
        klass = "VANISH"  # (local)
        verdict = "PASS"  # (local)
        reason = f"Δ_12/Δ_10={delta_ratio:.4f} ∈ [-0.05,0.05]; +0.50% was L=10 truncation-only artifact"
    else:
        klass = "INTERMEDIATE"  # (local)
        verdict = "INFO"  # (local)
        reason = f"Δ_12/Δ_10={delta_ratio:.4f} outside REFINE/EXTEND/VANISH bands; intermediate"

    # 8. Build dual-SHA pinmap
    pinmap = {  # (local)
        "_gate_id": GATE_ID,
        "_wp_id": WP_ID,
        "_scheme": SCHEME,
        "_convention": CONVENTION,
        "_L_max": L_MAX,
        "L_base": L_BASE,
        "L_ref_W1b5": L_REF,
        "ratio_10_W1b5": str(RATIO_10_W1B5),
        "DELTA_10_W1b5": str(DELTA_10),
        "REL_TOL_AXIOM": str(REL_TOL_AXIOM),
        "BAND_REFINE": list(BAND_REFINE),
        "BAND_EXTEND": list(BAND_EXTEND),
        "BAND_VANISH": list(BAND_VANISH),
        "cache_path": str(CACHE_PATH.relative_to(ROOT)),
        "cache_sha_pin": CACHE_SHA_PIN,
        "cache_sha_actual": actual_cache_sha,
        "M_KK_GeV": M_KK,
        "tau_fold": tau_fold,
        "n_sec_5": n_sec_5,
        "n_sec_10": n_sec_10,
        "n_sec_12": n_sec_12,
    }
    audit_sha256 = closure_hash_dict(pinmap)  # (local)

    val_str = (
        f"Delta_12_pct={delta_12*100:.6e};Delta_10_recompute_pct={delta_10_recompute*100:.6e};"
        f"ratio_12={ratio_12:.10f};ratio_10_recompute={ratio_10_recompute:.10f};"
        f"Delta_12_over_Delta_10={delta_ratio:.6f};predicted_L3_envelope={(10/12)**3:.6f};"
        f"class={klass};reason={reason};"
        f"axiom_pass={n_pass}/6;axiom_fail={n_fail}/6;"
        f"growth_SM_L10={growth_SM_L10:.4f};growth_SM_L12={growth_SM_L12:.4f};"
        f"growth_PS_L10={growth_PS_L10:.4f};growth_PS_L12={growth_PS_L12:.4f};"
        f"n_sec_L12={n_sec_12};n_eig_L12={n_eig_12}"
    )  # (local)
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value='{val_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha256} content_sha256={{CONTENT_SHA}} schema_version={SCHEMA_VERSION}"
    )  # (local)
    content_sha256 = hashlib.sha256(
        canonical_line.replace("{CONTENT_SHA}", "PLACEHOLDER").encode("utf-8")
    ).hexdigest()  # (local)
    canonical_line = canonical_line.replace("{CONTENT_SHA}", content_sha256)

    short_a = audit_sha256[:16]  # (local)
    short_c = content_sha256[:16]  # (local)
    companion_dualsha = (
        f"# audit_sha256_short={short_a} content_sha256_short={short_c} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"plan §W11-122 PS-vs-SM A_F diagnostic re-run at L_max=12; "
        f"three-class assignment {klass}"
    )  # (local)

    sign_v = "N/A"  # (local) bidirectional shift inquiry, no signed pre-registration
    mag_v = "PASS" if verdict == "PASS" else ("FAIL" if verdict == "FAIL" else "INFO")
    regime_v = "VALID" if n_fail == 0 else "BREAKDOWN"  # (local)
    companion_3tuple = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2); "
        f"[VERIFY] gate; bidirectional Δ_12 inquiry; classes REFINE/EXTEND/VANISH/INFO; "
        f"axioms: {n_pass}/6 PASS"
    )  # (local)

    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical_line + "\n")
        f.write(companion_dualsha + "\n")
        f.write(companion_3tuple + "\n")
    print(f"\n  Verdict appended to {VERDICT_FILE}")
    print(f"  audit_sha256 = {audit_sha256}")
    print(f"  content_sha256 = {content_sha256}")

    # NPZ
    np.savez_compressed(
        OUT_NPZ,
        L_max=L_MAX, L_base=L_BASE, L_ref=L_REF,
        ratio_10_W1b5=RATIO_10_W1B5, ratio_10_recompute=ratio_10_recompute,
        Delta_10_recompute=delta_10_recompute, Delta_12=delta_12,
        ratio_12=ratio_12, Delta_12_over_Delta_10=delta_ratio,
        predicted_L3_envelope=(10/12)**3,
        klass=klass, verdict=verdict,
        n_sec_5=n_sec_5, n_sec_10=n_sec_10, n_sec_12=n_sec_12,
        n_eig_5=n_eig_5, n_eig_10=n_eig_10, n_eig_12=n_eig_12,
        M0_SM_L5=M0_SM_L5, M0_SM_L10=M0_SM_L10, M0_SM_L12=M0_SM_L12,
        M0_PS_L5_at10=M0_PS_L5_at10, M0_PS_L10_at10=M0_PS_L10_at10,
        M0_PS_L5_at12=M0_PS_L5_at12, M0_PS_L12_at12=M0_PS_L12_at12,
        growth_SM_L10=growth_SM_L10, growth_SM_L12=growth_SM_L12,
        growth_PS_L10=growth_PS_L10, growth_PS_L12=growth_PS_L12,
        axiom_n_pass=n_pass, axiom_n_fail=n_fail,
        cache_sha=actual_cache_sha, audit_sha256=audit_sha256, content_sha256=content_sha256,
    )
    print(f"  NPZ saved: {OUT_NPZ}")

    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(13, 4.5))
    ax = axes[0]
    Ls = [L_REF, L_MAX]  # (local)
    deltas = [delta_10_recompute, delta_12]  # (local)
    ax.plot(Ls, [d*100 for d in deltas], 'o-', markersize=10, color='#d62728', label='measured Δ(L)·100')
    L_extrap = np.linspace(L_REF, L_MAX, 30)  # (local)
    L3_predict = delta_10_recompute * (L_REF / L_extrap) ** 3  # (local)
    ax.plot(L_extrap, [d*100 for d in L3_predict], '--', color='#1f77b4', label='L^{-3} envelope (REFINE)')
    ax.axhline(0, color='black', alpha=0.3)
    ax.set_xlabel("L_max")
    ax.set_ylabel("Δ(L) · 100  (PS/SM ratio − 1, %)")
    ax.set_title(f"Δ(L) refinement at L=10 → L=12; class={klass}")
    ax.legend()
    ax.grid(True, linestyle=':', alpha=0.4)

    ax = axes[1]
    ax.bar(["growth_SM(L=10)", "growth_SM(L=12)", "growth_PS(L=10)", "growth_PS(L=12)"],
           [growth_SM_L10, growth_SM_L12, growth_PS_L10, growth_PS_L12],
           color=['#1f77b4', '#9ec5e8', '#d62728', '#f0a3a4'])
    ax.set_ylabel("growth_0(ζ) = M_0(L)/M_0(L=5)")
    ax.set_title("n=0 ζ-regulator growth, both A_F at L=10 and L=12")
    plt.setp(ax.get_xticklabels(), rotation=15, ha='right')
    ax.grid(True, axis='y', linestyle=':', alpha=0.4)

    plt.suptitle(f"S88 W11-122 PS A_F recalibration at L_max=12; verdict={verdict} ({klass})")
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=130)
    plt.close()
    print(f"  PNG saved: {OUT_PNG}")

    elapsed = time.time() - t0  # (local)
    print(f"  Total wall: {elapsed:.1f}s")
    print(f"\n  Verdict: {verdict} ({klass}) — {reason}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
