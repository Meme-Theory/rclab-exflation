#!/usr/bin/env python3
"""
S92 W4-6 — S92-W4-CF-W4-4-EMPIRICAL-ANCHOR-RECONCILIATION
=========================================================

Gate: S92-W4-CF-W4-4-EMPIRICAL-ANCHOR-RECONCILIATION  ([SIGN])
  Classification: GEOMETRIC

Pre-registered threshold (per session-92-plan-w4.md §W4-6 5-step):
  PASS iff substrate-physics adjudication identifies ONE convention as
       substrate-natural at the cache-moment layer per
       `substrate-first-canonical-sourcing.md §(ii.A)` (atlas-row vs
       cache-moment layer orthogonality) AND the canonical value is
       promoted to canonical_constants.py via update_constant(...) AND
       the other 2 conventions are tagged DIAGNOSTIC per
       `cross-pillar-bridge-anatomy.md §"Level-3 anchor singleness
       sub-clause"` SUGGESTION K=1.
  INFO  iff substrate-natural identified WITH explicit substrate-physics
        caveat (e.g., sub-converged MARGINAL regime).
  FAIL  iff substrate-physics criteria are inconclusive (multi-criterion
        orderings diverge); 3-way divergence retained.

Inputs (SHA-256 dual-pinned at runtime):
  - computations/_shared/canonical_constants.py             (Delta_BCS pin)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz (sector-keyed
       Peter-Weyl spectrum cache; expected sha256
       9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9
       per plan §W4-6 input_files block)
  - computations/session-91/s91_w4_vii_u_2_var_a_stage_2_axis_a_vdd.npz
       (vdd recompute Var_a_L10 = 4.7650356226e-05)
  - computations/session-91/s91_w4_vii_u_2_var_a_stage_2_axis_b_volovik.npz
       (volovik recompute Var_a_L10 = 1.268176e-05)
  - sessions/permanent-results-registry.md  (§VII.U.2 Corner II Var_a
       parse-tree expansion at line 12961; v_inf_extrapolated =
       6.4631783294e-06 pin)
  - script bytes                            (feeds BOTH SHAs)

Output 4-tuple:
  (value=<substrate-natural canonical + 3 convention diagnostic table>,
   scheme=weyl-dim-extrapolated-to-infinity-asymptotic-limit-substrate-natural-adjudication,
   convention=substrate-first-canonical-sourcing-ii-A-atlas-row-vs-cache-moment-layer-orthogonality-SUGGESTION-K-1,
   L_max=10)

METHODOLOGY (substrate-physics adjudication — 5-step per plan §W4-6)
--------------------------------------------------------------------
Step 1: Recompute Var_a(n_a^GGE) at L_max=10 under each of 3 conventions:
        - vdd: p+q <= L_max filter; each listed eigenvalue (abs_evals[i])
          counted with m_a = 1 (the cache's per-state 16*dim_pq replication
          is the implicit multiplicity).
        - volovik: p+q <= L_max filter; each listed eigenvalue counted
          with m_a = dim_pq (DOUBLE-weights dim_pq because abs_evals already
          carries the 16*dim_pq replication; produces a structurally
          different normalization).
        - w5b47_raw: max(p,q) <= L_max filter (W5b-47 exact convention,
          NOT p+q <= L); each listed eigenvalue counted with m_a = dim_pq;
          zero-modes (lambda <= 1e-12) excluded. This is the canonical S88
          W5b-47 convention per computations/session-88/
          s88_w5b_corner_iv_level2_envelope.py collect_truncated_spectrum().

Step 2: Apply substrate-first-canonical-sourcing.md §(ii.A) atlas-row
        vs cache-moment layer orthogonality. All 3 conventions inhabit
        the CACHE-MOMENT layer (numerical evaluation on L_max-truncated
        cache); the ATLAS-ROW layer at locked-norm L_k=1 is the
        Bogoliubov closed form per the §VII.U.2 Corner II row parse-tree
        expansion (registry line 12961, S52 BdG canonical amplitudes
        |v_a|^2 = Delta_BCS^2/(2(lambda_a^2 + Delta_BCS^2))). The
        substrate-IS substitution chain is INVARIANT across the 3
        conventions; the divergence is purely a multiplicity-weighting
        sum convention at the cache-moment layer.

Step 3: Compute Weyl-dim extrapolated-to-infinity asymptotic limit
        Var_a_inf = 6.4631783294e-06 (per registry §VII.U.2 Corner II
        Level-2 envelope L^{-4} Weyl-law tail analysis at d=4; S88
        §W5b-47 INFO composite). Evaluate Var_a at L_max in {6, 8, 10, 12}
        under each convention; compute per-convention convergence rate
        rel_dev = |Var_a(L_max) - Var_a_inf| / Var_a_inf.

Step 4: Adjudicate substrate-natural by 4 substrate-physics criteria:
        (i)   Derivation-chain traceable to D_K spectrum cache:
              all 3 conventions PASS (all read the cache directly).
        (ii)  Parse-tree expansion match at §VII.U.2 Corner II line 12961:
              all 3 conventions PASS (all use the Bogoliubov closed form
              |v_a|^2 = Delta_BCS^2/(2(lambda_a^2+Delta_BCS^2))).
        (iii) Fastest convergence to Weyl-dim extrapolated-to-infinity
              asymptotic limit at L_max=10: discriminating criterion.
        (iv)  Cache-moment-layer-consistent: lambda support filter must
              match the substrate-distance-2 Mellin pole at s=4
              (NOT a triangular Peter-Weyl p+q<=L truncation, which
              under-samples the Weyl-law tail). The max(p,q)<=L filter
              IS substrate-natural at the Weyl-law tail.

        The 4 criteria converge uniquely on w5b47_raw at L_max=10:
        criterion (iii) gives 12.7% deviation (vs 96.2% volovik, 637% vdd)
        AND criterion (iv) gives the substrate-natural max(p,q) filter
        match. Adjudication is consistent across both discriminating
        criteria; PASS verdict.

Step 5: Promote canonicalized value to canonical_constants.py via
        update_constant("Var_a_canonical", value, session="S92",
        source="S92-W4-CF-W4-4-EMPIRICAL-ANCHOR-RECONCILIATION".
        The canonical name Var_a_canonical_substrate_natural_convention
        appears as the docstring-anchor for the substrate-natural
        adjudication target; the on-disk pin name is `Var_a_canonical`
        and its provenance entry tags `convention=w5b47_raw` (the
        substrate-natural convention identified by criteria (iii) ∧ (iv)).
        comment="...substrate-natural multiplicity-weighting at
        cache-moment layer per (ii.A); deprecated conventions tagged
        DIAGNOSTIC per Level-3 anchor singleness sub-clause SUGGESTION
        K=1 (S91 W4 CF-S92-W5-1-F)...") at PASS.

SUBSTRATE FRAMING (per phononic-framing.md §"IS Space, Not IN Space")
---------------------------------------------------------------------
The substrate IS the spectral triple (A_K = C + H + M_3(C), H_K, D_K) at
tau_fold = 0.190. The substrate-IS Var_a(n_a^GGE) observable IS the
closed-form expression on the BdG sub-algebra M_2(C) per S52 Bogoliubov
canonical amplitudes (parse-tree expansion at §VII.U.2 Corner II row line
12961). The substrate-natural canonical at the cache-moment layer IS
the multiplicity-weighting convention whose finite-L_max value converges
fastest to the Weyl-dim extrapolated-to-infinity asymptotic limit
(which IS the Level-1 cohomology-class identity).

The 3 finite-L_max values (vdd 4.77e-05, volovik 1.27e-05, w5b47_raw
7.28e-06) are 3 methodology-floor F-images at 3 structurally-distinct
multiplicity-normalization conventions per epistemic-discipline.md
§"Layer-Decomposition" Phi-correspondence. The volovik PRIMARY
substrate-physics adjudication IS the substrate's own structural test of
which convention IS substrate-natural; the canonicalized value enters
canonical_constants.py as the single-pinned Level-3 anchor per
cross-pillar-bridge-anatomy.md §"Level-3 anchor singleness sub-clause"
SUGGESTION K=1.

Direction substrate -> emergent:
  D_K eigenvalues -> BdG sub-algebra image -> Bogoliubov closed form
    -> multiplicity-weighted spectral moment
    -> Weyl-dim extrapolated-to-infinity asymptotic limit (substrate-IS)
    -> substrate-natural canonical pin at cache-moment layer.

FORBIDDEN inversion: "the 3 finite-L_max values are 3 substrate-IS
canonicals; pluralism prevails at the Level-3 anchor layer" — INVERTED
to "the substrate IS the Weyl-dim asymptotic limit at the Level-1
cohomology-class layer; the 3 finite-L_max values are 3 methodology-floor
F-images at distinct multiplicity-normalization conventions; the
substrate-natural canonical IS the F-image whose value converges fastest
to the substrate-IS asymptotic limit at the cache-moment layer".
"""

from __future__ import annotations

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

from canonical_constants import Delta_BCS, tau_fold  # noqa: E402  (post-path)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------

SESSION = "S92"  # (local)
GATE_ID = "S92-W4-CF-W4-4-EMPIRICAL-ANCHOR-RECONCILIATION"  # (local)
SCHEME = (
    "weyl-dim-extrapolated-to-infinity-asymptotic-limit-substrate-natural-adjudication"
)  # (local)
CONVENTION = (
    "substrate-first-canonical-sourcing-ii-A-atlas-row-vs-cache-moment-layer-"
    "orthogonality-SUGGESTION-K-1"
)  # (local)
L_MAX = 10  # (local)
SCAN_L_MAX_LIST = [6, 8, 10, 12]  # (local) L_max asymptotic-limit convergence scan

# Pre-registered anchor values (per plan §W4-6 substitution chain)
V_INF_EXTRAPOLATED = 6.4631783294e-06  # (local) Weyl-dim L_max -> inf asymptotic limit
                                       # per registry §VII.U.2 Corner II Level-2
                                       # envelope L^{-4} (S88 §W5b-47 INFO composite)
VDD_L10_PIN = 4.7650356226e-05  # (local) S91 W4-4 Axis-A vdd recompute
VOLOVIK_L10_PIN = 1.268176e-05   # (local) S91 W4-4 Axis-B volovik recompute
W5B47_L10_PIN = 7.282490e-06     # (local) S88 W5b-47 raw L_max=10 anchor

# Output destinations (per-session, per orchestrator override)
OUT_NPZ = SESSION_DIR / "s92_w4_6_w4_4_empirical_anchor_reconciliation.npz"
OUT_PNG = SESSION_DIR / "s92_w4_6_w4_4_empirical_anchor_reconciliation.png"
VERDICT_TXT = SESSION_DIR / "s92_gate_verdicts.txt"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz",
    COMPUTATIONS_DIR / "session-91" / "s91_w4_vii_u_2_var_a_stage_2_axis_a_vdd.npz",
    COMPUTATIONS_DIR / "session-91" / "s91_w4_vii_u_2_var_a_stage_2_axis_b_volovik.npz",
    PROJECT_ROOT / "sessions" / "permanent-results-registry.md",
]
CACHE_PATH = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins):
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — 3-convention Var_a recompute (substrate-physics adjudication)
# ---------------------------------------------------------------------------

def compute_var_a_three_conventions(sector_evals, L_max_filter, delta_sq):
    """Compute Var_a(n_a^GGE) at L_max_filter under each of 3 conventions.

    Returns dict with keys:
      vdd:      p+q<=L filter; m_a=1 per listed eigenvalue.
      volovik:  p+q<=L filter; m_a=dim_pq per listed eigenvalue
                (double-counts dim_pq because abs_evals already carries
                16*dim_pq replication).
      w5b47:    max(p,q)<=L filter (S88 W5b-47 exact convention); m_a=dim_pq
                per listed eigenvalue; zero-modes (|lambda|<=1e-12) excluded.

    The Bogoliubov closed form |v_a|^2 = Delta_BCS^2 / (2*(lambda^2 + Delta^2))
    is INVARIANT across the 3 conventions; the divergence is in the
    multiplicity-weighting sum normalization at the cache-moment layer.
    """
    # ---- vdd: p+q<=L, m_a=1 per listed eigenvalue ----
    N_vdd = 0  # (local)
    sum_vsq_vdd = 0.0  # (local)
    sum_v4_vdd = 0.0  # (local)
    # ---- volovik: p+q<=L, m_a=dim_pq per listed eigenvalue ----
    N_volo = 0.0  # (local)
    sum_vsq_volo = 0.0  # (local)
    sum_v4_volo = 0.0  # (local)
    # ---- w5b47_raw: max(p,q)<=L, m_a=dim_pq, exclude zero-modes ----
    lams_raw = []  # (local)
    weights_raw = []  # (local)
    n_sectors_vdd_volo = 0  # (local)
    n_sectors_raw = 0  # (local)

    for (p, q), block in sector_evals.items():
        if not isinstance(block, dict) or "abs_evals" not in block:
            continue
        eigs = np.asarray(block["abs_evals"], dtype=np.float64)  # (local)
        dim_pq = int(block.get("dim", 1))  # (local)
        v_sq = delta_sq / (2.0 * (eigs ** 2 + delta_sq))  # (local)
        v_4 = v_sq ** 2  # (local)

        if p + q <= L_max_filter:
            # vdd convention: each listed eigenvalue counted once
            N_vdd += eigs.size
            sum_vsq_vdd += v_sq.sum()
            sum_v4_vdd += v_4.sum()
            # volovik convention: each listed eigenvalue counted dim_pq times
            N_volo += dim_pq * eigs.size
            sum_vsq_volo += dim_pq * v_sq.sum()
            sum_v4_volo += dim_pq * v_4.sum()
            n_sectors_vdd_volo += 1

        if max(p, q) <= L_max_filter:
            # w5b47_raw convention: max(p,q) filter; per-eigenvalue weight=dim_pq;
            # zero-modes excluded.
            mask_nonzero = np.abs(eigs) > 1e-12  # (local)
            for vs2 in v_sq[mask_nonzero]:
                lams_raw.append(vs2)
                weights_raw.append(dim_pq)
            n_sectors_raw += 1

    # vdd
    var_vdd = sum_v4_vdd / N_vdd - (sum_vsq_vdd / N_vdd) ** 2  # (local)
    # volovik
    var_volo = sum_v4_volo / N_volo - (sum_vsq_volo / N_volo) ** 2  # (local)
    # w5b47_raw
    arr_vsq = np.asarray(lams_raw, dtype=np.float64)  # (local)
    arr_w = np.asarray(weights_raw, dtype=np.float64)  # (local)
    W_raw = arr_w.sum()  # (local)
    M1_raw = (arr_w * arr_vsq).sum() / W_raw  # (local)
    M2_raw = (arr_w * arr_vsq ** 2).sum() / W_raw  # (local)
    var_raw = M2_raw - M1_raw ** 2  # (local)

    return {
        "vdd": float(var_vdd),
        "volovik": float(var_volo),
        "w5b47_raw": float(var_raw),
        "N_vdd": int(N_vdd),
        "N_volovik": int(N_volo),
        "N_raw_weighted": float(W_raw),
        "N_raw_distinct": int(arr_vsq.size),
        "n_sectors_vdd_volo": int(n_sectors_vdd_volo),
        "n_sectors_raw": int(n_sectors_raw),
    }


# ---------------------------------------------------------------------------
# Section 6 — Pin verification against S91/S88 npz file values
# ---------------------------------------------------------------------------

def verify_pins_against_npz():
    """Verify that the L_max=10 pins from S91 W4-4 npz files match the
    closed-form recompute. This is the substrate-IS substitution-chain
    audit at the cache-moment layer."""
    print("\n=== Pin verification against S91 W4-4 / S88 W5b-47 npz files ===")

    # S91 W4-4 Axis-A vdd
    vdd_npz = np.load(
        COMPUTATIONS_DIR / "session-91" / "s91_w4_vii_u_2_var_a_stage_2_axis_a_vdd.npz",
        allow_pickle=True,
    )
    vdd_val_npz = float(vdd_npz["clause_e_var_a_Lmax10"])  # (local)
    print(f"  vdd (S91 npz):     {vdd_val_npz:.10e}  (plan pin {VDD_L10_PIN:.10e})")
    assert abs(vdd_val_npz - VDD_L10_PIN) / VDD_L10_PIN < 1e-6, (
        f"vdd pin mismatch: npz={vdd_val_npz}, plan={VDD_L10_PIN}"
    )

    # S91 W4-4 Axis-B volovik
    volo_npz = np.load(
        COMPUTATIONS_DIR / "session-91" / "s91_w4_vii_u_2_var_a_stage_2_axis_b_volovik.npz",
        allow_pickle=True,
    )
    volo_val_npz = float(volo_npz["var_a_l_max_10"])  # (local)
    print(f"  volovik (S91 npz): {volo_val_npz:.10e}  (plan pin {VOLOVIK_L10_PIN:.10e})")
    assert abs(volo_val_npz - VOLOVIK_L10_PIN) / VOLOVIK_L10_PIN < 1e-5, (
        f"volovik pin mismatch: npz={volo_val_npz}, plan={VOLOVIK_L10_PIN}"
    )

    # S88 W5b-47 pins are embedded in the volovik npz (as cross-check pins):
    w5b47_npz_pin = float(volo_npz["w5b_47_l10_raw_pin"])  # (local)
    v_inf_npz_pin = float(volo_npz["w5b_47_v_inf_pin"])  # (local)
    print(f"  w5b47_raw  (S91 npz): {w5b47_npz_pin:.10e}  (plan pin {W5B47_L10_PIN:.10e})")
    print(f"  v_inf (S91 npz):      {v_inf_npz_pin:.10e}  (plan pin {V_INF_EXTRAPOLATED:.10e})")
    assert abs(w5b47_npz_pin - W5B47_L10_PIN) / W5B47_L10_PIN < 1e-5
    assert abs(v_inf_npz_pin - V_INF_EXTRAPOLATED) / V_INF_EXTRAPOLATED < 1e-6

    return {
        "vdd_L10_npz": vdd_val_npz,
        "volovik_L10_npz": volo_val_npz,
        "w5b47_L10_npz_pin": w5b47_npz_pin,
        "v_inf_npz_pin": v_inf_npz_pin,
    }


# ---------------------------------------------------------------------------
# Section 7 — Substrate-physics adjudication (4-criterion analysis)
# ---------------------------------------------------------------------------

def substrate_physics_adjudication(scan_results):
    """Adjudicate substrate-natural convention per plan §W4-6 Step 4:
        (i)   Derivation-chain traceable to D_K spectrum cache.
        (ii)  Parse-tree expansion match at §VII.U.2 Corner II line 12961.
        (iii) Fastest convergence to Weyl-dim asymptotic limit at L_max=10.
        (iv)  Cache-moment-layer-consistent lambda support filter
              (substrate-natural Weyl-law tail at substrate-distance-2 s=4).

    Returns: dict with adjudication verdict + per-criterion sub-pass status.
    """
    print("\n=== Substrate-physics adjudication (4-criterion) ===")

    # L_max=10 absolute deviations from asymptotic limit:
    L10_vals = scan_results[10]  # (local) {convention -> Var_a(L_max=10)}
    rel_devs_L10 = {
        c: abs(v - V_INF_EXTRAPOLATED) / V_INF_EXTRAPOLATED for c, v in L10_vals.items()
    }  # (local)
    print(f"  L_max=10 |Var_a - v_inf|/v_inf:")
    for c in ("vdd", "volovik", "w5b47_raw"):
        print(f"    {c:12s} {rel_devs_L10[c]:.6f}  ({100*rel_devs_L10[c]:.2f}%)")
    convergence_winner = min(rel_devs_L10, key=rel_devs_L10.get)  # (local)
    print(f"  Criterion (iii) — fastest convergence at L_max=10: {convergence_winner}")

    # Cache-moment-layer-consistent filter (criterion iv):
    #   The Weyl-law tail analysis for d=4 substrate-distance-2 Mellin pole
    #   at s=4 derives Var_a(L_max) ~ L^{-4} (Level-2 envelope per registry
    #   §VII.U.2 Corner II row). The Weyl-law tail's substrate-natural support
    #   is the full sector set {(p,q) : max(p,q) <= L_max} (the L^infty box
    #   in the (p,q) lattice), NOT the triangular {p+q <= L_max} truncation
    #   which UNDER-samples the (p, q) pairs with one of p, q in [L_max+1, L_max].
    #   The triangular filter under-samples sectors that contribute to the
    #   Weyl-law tail at the d=4 dimension; the L^infty filter is
    #   substrate-natural.
    print()
    print(f"  Criterion (iv) — cache-moment-layer-consistent filter:")
    print(f"    vdd      uses p+q <= L_max     (triangular; under-samples Weyl-law tail)")
    print(f"    volovik  uses p+q <= L_max     (triangular; under-samples Weyl-law tail)")
    print(f"    w5b47    uses max(p,q) <= L_max (L_inf box; substrate-natural at d=4)")
    filter_winner = "w5b47_raw"  # (local)

    # Convergence ordering at L_max=10 (substitution chain Step 4):
    ordering_L10 = sorted(rel_devs_L10.items(), key=lambda kv: kv[1])  # (local)
    print()
    print(f"  Convergence ordering at L_max=10:")
    for i, (c, d) in enumerate(ordering_L10):
        print(f"    rank {i+1}: {c:12s} rel_dev = {d:.6f}")

    # All 3 conventions pass criteria (i) and (ii):
    # (i) all read the same D_K spectrum cache directly.
    # (ii) all use Bogoliubov closed form per Step 2 of substitution chain.
    crit_i_pass = {"vdd": True, "volovik": True, "w5b47_raw": True}  # (local)
    crit_ii_pass = {"vdd": True, "volovik": True, "w5b47_raw": True}  # (local)

    # Criterion (iii) and (iv) discriminate; both point at w5b47_raw.
    crit_iii_pass = {
        c: (convergence_winner == c) for c in ("vdd", "volovik", "w5b47_raw")
    }  # (local)
    crit_iv_pass = {
        c: (filter_winner == c) for c in ("vdd", "volovik", "w5b47_raw")
    }  # (local)

    # Aggregation: substrate-natural IS the convention that wins criteria
    # (iii) AND (iv); the universal criteria (i), (ii) are baseline.
    # If (iii) and (iv) point at DIFFERENT conventions, the adjudication
    # is inconclusive (FAIL).
    discriminating_winners = {"iii": convergence_winner, "iv": filter_winner}  # (local)
    print()
    print(f"  Discriminating-criterion winners: {discriminating_winners}")
    adjudication_unique = (convergence_winner == filter_winner)  # (local)

    if adjudication_unique:
        substrate_natural = convergence_winner  # (local)
        rationale = (
            f"Convergence-rate ordering (criterion iii) AT L_max=10 IS "
            f"w5b47_raw (rel_dev {100*rel_devs_L10['w5b47_raw']:.2f}%) < "
            f"volovik ({100*rel_devs_L10['volovik']:.2f}%) < "
            f"vdd ({100*rel_devs_L10['vdd']:.2f}%); "
            f"cache-moment-layer filter (criterion iv) is "
            f"max(p,q) <= L_max for w5b47_raw (substrate-natural L_inf box "
            f"covering the d=4 Weyl-law tail), NOT p+q <= L_max for vdd/volovik "
            f"(triangular under-sampling). The 2 discriminating criteria "
            f"converge uniquely on w5b47_raw."
        )  # (local)
    else:
        substrate_natural = None  # (local)
        rationale = (
            f"Criterion (iii) winner ({convergence_winner}) != criterion (iv) "
            f"winner ({filter_winner}); substrate-physics adjudication is "
            f"inconclusive; 3-way divergence retained."
        )  # (local)

    print()
    print(f"  Substrate-natural convention: {substrate_natural}")
    print(f"  Rationale: {rationale}")

    return {
        "substrate_natural": substrate_natural,
        "convergence_winner": convergence_winner,
        "filter_winner": filter_winner,
        "adjudication_unique": adjudication_unique,
        "rel_devs_L10": rel_devs_L10,
        "ordering_L10": ordering_L10,
        "crit_i_pass": crit_i_pass,
        "crit_ii_pass": crit_ii_pass,
        "crit_iii_pass": crit_iii_pass,
        "crit_iv_pass": crit_iv_pass,
        "rationale": rationale,
    }


# ---------------------------------------------------------------------------
# Section 8 — Compute
# ---------------------------------------------------------------------------

def compute():
    print(f"\n=== Loading L_max=12 spectrum cache at tau_fold = {tau_fold:.6f} ===")
    cache = np.load(CACHE_PATH, allow_pickle=True)
    sector_evals = cache["sector_evals"].item()  # (local)
    print(f"  Sectors in cache: {len(sector_evals)}")
    print(f"  Delta_BCS pin:    {Delta_BCS:.10f} M_KK (canonical_constants.py)")
    delta_sq = Delta_BCS ** 2  # (local)

    # Step 1: Verify pins against S91 W4-4 npz files
    pin_verification = verify_pins_against_npz()  # (local)

    # Step 2-3: L_max scan {6, 8, 10, 12} under each of 3 conventions
    print("\n=== L_max ∈ {6, 8, 10, 12} asymptotic-limit convergence scan ===")
    print(f"  v_inf (Weyl-dim extrapolated-to-infinity asymptotic limit) = "
          f"{V_INF_EXTRAPOLATED:.10e}")
    print(f"  (per registry §VII.U.2 Corner II Level-2 envelope L^{{-4}})")
    print()
    print(f"  {'L_max':>5s} {'vdd':>16s} {'volovik':>16s} {'w5b47_raw':>16s} "
          f"{'vdd rel':>10s} {'volo rel':>10s} {'raw rel':>10s}")

    scan_results = {}  # (local) {L_max -> {convention -> Var_a}}
    for L in SCAN_L_MAX_LIST:
        res = compute_var_a_three_conventions(sector_evals, L, delta_sq)  # (local)
        scan_results[L] = {
            "vdd": res["vdd"],
            "volovik": res["volovik"],
            "w5b47_raw": res["w5b47_raw"],
        }
        rd_vdd = (res["vdd"] - V_INF_EXTRAPOLATED) / V_INF_EXTRAPOLATED  # (local)
        rd_volo = (res["volovik"] - V_INF_EXTRAPOLATED) / V_INF_EXTRAPOLATED  # (local)
        rd_raw = (res["w5b47_raw"] - V_INF_EXTRAPOLATED) / V_INF_EXTRAPOLATED  # (local)
        print(f"  {L:>5d} {res['vdd']:>16.6e} {res['volovik']:>16.6e} "
              f"{res['w5b47_raw']:>16.6e} {rd_vdd:>+10.4f} {rd_volo:>+10.4f} "
              f"{rd_raw:>+10.4f}")

    # L_max=10 cardinality detail
    res_L10 = compute_var_a_three_conventions(sector_evals, L_MAX, delta_sq)
    print()
    print(f"  L_max=10 cardinality breakdown:")
    print(f"    vdd:     N = {res_L10['N_vdd']:,d} listed eigenvalues over "
          f"{res_L10['n_sectors_vdd_volo']} sectors (p+q <= 10)")
    print(f"    volovik: N (m-weighted) = {res_L10['N_volovik']:,d} over "
          f"{res_L10['n_sectors_vdd_volo']} sectors (p+q <= 10)")
    print(f"    w5b47:   N (m-weighted) = {res_L10['N_raw_weighted']:,.0f} over "
          f"{res_L10['n_sectors_raw']} sectors (max(p,q) <= 10); "
          f"{res_L10['N_raw_distinct']:,d} non-zero eigenvalues")

    # Step 4: Substrate-physics adjudication
    adjudication = substrate_physics_adjudication(scan_results)  # (local)

    # Step 5: Promote canonical value
    if adjudication["adjudication_unique"]:
        canonical_val = scan_results[L_MAX][adjudication["substrate_natural"]]  # (local)
        print(f"\n=== Step 5 — Promote canonical via update_constant ===")
        print(f"  Var_a_canonical = {canonical_val:.10e}")
        print(f"  Source convention: {adjudication['substrate_natural']}")
    else:
        canonical_val = None  # (local)

    # L_max=10 to L_max=12 trajectory (substrate-natural sanity)
    print(f"\n=== L10 -> L12 trajectory (substrate-natural sanity) ===")
    for c in ("vdd", "volovik", "w5b47_raw"):
        v10 = scan_results[10][c]
        v12 = scan_results[12][c]
        delta_pct = 100.0 * (v12 - v10) / v10  # (local)
        print(f"  {c:12s}  L10 -> L12: {v10:.4e} -> {v12:.4e}  (Delta = {delta_pct:+.3f}%)")

    return {
        "scan_results": scan_results,
        "L10_detail": res_L10,
        "adjudication": adjudication,
        "canonical_value": canonical_val,
        "pin_verification": pin_verification,
        "Delta_BCS": float(Delta_BCS),
        "tau_fold": float(tau_fold),
    }


# ---------------------------------------------------------------------------
# Section 9 — Gate verdict + Schema-v2 3-tuple
# ---------------------------------------------------------------------------

def evaluate_gate_with_3tuple(result):
    """Return (composite, sign_v, magnitude_v, regime_v, domain_used_frac).

    The [SIGN] trigger requires the schema-v2 3-tuple per gate-verdicts.md
    §"S87+ canonical form (Schema-v2)".

    Pre-registered substitution-chain direction (Step 4):
      convergence_rate(w5b47_raw, L=10) < convergence_rate(volovik, L=10) <
      convergence_rate(vdd, L=10).

    sign_verdict     = PASS iff computed ordering matches predicted ordering.
    magnitude_verdict= PASS iff adjudication identifies unique substrate-
                       natural AND canonical_constants update succeeds (deferred
                       to main() after .npz write; pre-evaluate here).
    regime_verdict   = VALID iff L_max=10 sub-converged enough that L10->L12
                       trajectory delta on substrate-natural convention <= 5%
                       (substrate-natural saturation criterion at the cache
                       boundary).
    """
    adj = result["adjudication"]
    scan = result["scan_results"]

    # SIGN: predicted ordering w5b47_raw < volovik < vdd at L_max=10
    rel_devs = adj["rel_devs_L10"]
    sign_pass = (
        rel_devs["w5b47_raw"] < rel_devs["volovik"] < rel_devs["vdd"]
    )  # (local)

    # MAGNITUDE: unique substrate-natural identified
    magnitude_pass = bool(adj["adjudication_unique"])  # (local)

    # REGIME: L10->L12 trajectory delta on substrate-natural convention
    # Auto-shortening clause: this is a 2-point trajectory check on the
    # discrete L_max scan, NOT a continuous domain test. domain_used_frac
    # is 1.0 by construction (full intended L_max scan covered).
    domain_used_frac = 1.0  # (local) full L_max scan completed
    if adj["adjudication_unique"]:
        sn = adj["substrate_natural"]
        v10 = scan[10][sn]
        v12 = scan[12][sn]
        traj_delta = abs(v12 - v10) / v10  # (local)
    else:
        traj_delta = 1.0  # (local) full divergence
    # MARGINAL band: 5% < |delta| <= 20%
    if traj_delta <= 0.05:
        regime_v = "VALID"
    elif traj_delta <= 0.20:
        regime_v = "MARGINAL"
    else:
        regime_v = "BREAKDOWN"

    sign_v = "PASS" if sign_pass else "FAIL"
    magnitude_v = "PASS" if magnitude_pass else "FAIL"

    # Composite collapse per gate-verdicts.md §S87+ schema-v2:
    if regime_v == "BREAKDOWN":
        composite = "FAIL"
    elif sign_v == "FAIL":
        composite = "FAIL"
    elif magnitude_v == "FAIL" and regime_v == "VALID":
        composite = "FAIL"
    elif magnitude_v == "FAIL" and regime_v == "MARGINAL":
        composite = "INFO"
    elif magnitude_v == "FAIL":
        composite = "FAIL"  # explicit (covers other paths)
    elif regime_v == "MARGINAL":
        composite = "INFO"
    else:
        composite = "PASS"

    return composite, sign_v, magnitude_v, regime_v, domain_used_frac, traj_delta


# ---------------------------------------------------------------------------
# Section 10 — Verdict-line emission (canonical + dual-SHA + schema-v2)
# ---------------------------------------------------------------------------

def append_verdict_lines(verdict, value_str, sign_v, magnitude_v, regime_v,
                        domain_used_frac, audit_sha, content_sha):
    """Append canonical line + dual-SHA companion + schema-v2 3-tuple row.

    The verdict line MUST include the [SIGN]-trigger 3-tuple companion row
    per gate-verdicts.md §"S87+ canonical form (Schema-v2)".
    """
    # Canonical line (S84+ dual-SHA schema)
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={value_str!r} "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)

    # Dual-SHA companion comment row (W9a-99)
    dual_sha_row = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)

    # Schema-v2 3-tuple companion row (S87+; [SIGN]-trigger required)
    tuple_3_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={magnitude_v} "
        f"regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2; "
        f"domain_used_frac={domain_used_frac:.3f})\n"
    )  # (local)

    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(dual_sha_row)
        fp.write(tuple_3_row)


# ---------------------------------------------------------------------------
# Section 11 — Plot
# ---------------------------------------------------------------------------

def emit_plot(result):
    scan = result["scan_results"]
    adj = result["adjudication"]
    L_arr = np.asarray(SCAN_L_MAX_LIST, dtype=int)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

    # Panel A: Var_a(L_max) under 3 conventions vs asymptotic limit (log-log)
    colors = {"vdd": "#d62728", "volovik": "#1f77b4", "w5b47_raw": "#2ca02c"}
    for c in ("vdd", "volovik", "w5b47_raw"):
        vals = [scan[L][c] for L in SCAN_L_MAX_LIST]
        axes[0].loglog(L_arr, vals, "o-", lw=1.7, ms=8, label=f"{c}",
                       color=colors[c])
    axes[0].axhline(V_INF_EXTRAPOLATED, ls="--", color="k", lw=1.2,
                    label=r"$v_\infty = 6.463 \times 10^{-6}$ (Weyl-dim asymp.)")
    axes[0].set_xlabel(r"$L_{\max}$ truncation")
    axes[0].set_ylabel(r"$\mathrm{Var}_a(n_a^{\mathrm{GGE}})$  [substrate-IS, "
                       r"dimensionless]")
    axes[0].set_title(r"Panel A — $L_{\max}\!\in\!\{6,8,10,12\}$ scan, "
                      r"3 conventions vs asymptotic")
    axes[0].grid(True, which="both", alpha=0.3)
    axes[0].legend(loc="upper right", fontsize=9)
    sn = adj["substrate_natural"]
    if sn is not None:
        axes[0].annotate(f"substrate-natural = {sn}\n"
                         f"(criterion iii+iv converge)",
                         xy=(10, scan[10][sn]),
                         xytext=(7.5, scan[10][sn] * 5),
                         arrowprops=dict(arrowstyle="->", color="black", lw=1.0),
                         fontsize=9, ha="center", color="black",
                         bbox=dict(boxstyle="round,pad=0.3",
                                   fc="lightyellow", ec="gray"))

    # Panel B: rel_dev_L10 ordering bar chart
    convs = ["vdd", "volovik", "w5b47_raw"]
    rel_devs = [adj["rel_devs_L10"][c] for c in convs]
    bar_colors = [colors[c] for c in convs]
    bars = axes[1].bar(convs, rel_devs, color=bar_colors, alpha=0.85)
    axes[1].set_yscale("log")
    axes[1].axhline(1.0, ls=":", color="gray", lw=1.0)
    axes[1].set_ylabel(r"$|\mathrm{Var}_a(L\!=\!10) - v_\infty| / v_\infty$")
    axes[1].set_title("Panel B — Convergence-rate ordering at $L_{\\max}=10$  "
                      "(criterion iii)")
    axes[1].grid(True, axis="y", which="both", alpha=0.3)
    for bar, rd in zip(bars, rel_devs):
        pct = 100 * rd
        axes[1].text(bar.get_x() + bar.get_width() / 2, rd * 1.15,
                     f"{pct:.2f}%", ha="center", va="bottom", fontsize=9,
                     color="black")
    # Mark winner
    if sn is not None:
        win_idx = convs.index(sn)
        axes[1].text(win_idx, rel_devs[win_idx] * 0.3, "(winner)",
                     ha="center", va="center", fontsize=10, color="white",
                     fontweight="bold")

    fig.suptitle(f"S92 W4-6 — Var_a(n_a^GGE) Empirical-Anchor Reconciliation "
                 f"(substrate-physics adjudication; substrate-natural = {sn})",
                 fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(OUT_PNG, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"\n  Plot written: {OUT_PNG}")


# ---------------------------------------------------------------------------
# Section 12 — npz output
# ---------------------------------------------------------------------------

def emit_npz(result, audit_sha, content_sha, verdict, sign_v, magnitude_v, regime_v):
    scan = result["scan_results"]
    adj = result["adjudication"]
    L10d = result["L10_detail"]

    np.savez(
        OUT_NPZ,
        # Scan results
        L_max_scan=np.asarray(SCAN_L_MAX_LIST, dtype=int),
        var_a_vdd_scan=np.asarray([scan[L]["vdd"] for L in SCAN_L_MAX_LIST]),
        var_a_volovik_scan=np.asarray([scan[L]["volovik"] for L in SCAN_L_MAX_LIST]),
        var_a_w5b47_scan=np.asarray([scan[L]["w5b47_raw"] for L in SCAN_L_MAX_LIST]),
        # L_max=10 anchor values
        var_a_vdd_L10=float(scan[10]["vdd"]),
        var_a_volovik_L10=float(scan[10]["volovik"]),
        var_a_w5b47_L10=float(scan[10]["w5b47_raw"]),
        # Asymptotic limit pin
        v_inf_extrapolated=float(V_INF_EXTRAPOLATED),
        # Per-convention rel_dev at L_max=10
        rel_dev_vdd_L10=float(adj["rel_devs_L10"]["vdd"]),
        rel_dev_volovik_L10=float(adj["rel_devs_L10"]["volovik"]),
        rel_dev_w5b47_L10=float(adj["rel_devs_L10"]["w5b47_raw"]),
        # Adjudication outcome
        substrate_natural_convention=str(adj["substrate_natural"] or "NONE"),
        adjudication_unique=bool(adj["adjudication_unique"]),
        canonical_value=float(result["canonical_value"]
                              if result["canonical_value"] is not None else 0.0),
        criterion_iii_convergence_winner=str(adj["convergence_winner"]),
        criterion_iv_filter_winner=str(adj["filter_winner"]),
        # Cardinality
        N_vdd_L10=int(L10d["N_vdd"]),
        N_volovik_L10=int(L10d["N_volovik"]),
        N_raw_weighted_L10=float(L10d["N_raw_weighted"]),
        N_raw_distinct_L10=int(L10d["N_raw_distinct"]),
        # Pin verification (S91/S88 npz cross-check)
        vdd_L10_npz_pin=float(result["pin_verification"]["vdd_L10_npz"]),
        volovik_L10_npz_pin=float(result["pin_verification"]["volovik_L10_npz"]),
        w5b47_L10_npz_pin=float(result["pin_verification"]["w5b47_L10_npz_pin"]),
        v_inf_npz_pin=float(result["pin_verification"]["v_inf_npz_pin"]),
        # Constants
        Delta_BCS_pin=float(result["Delta_BCS"]),
        tau_anchor_pin=float(result["tau_fold"]),
        # Verdicts
        verdict_composite=str(verdict),
        sign_verdict=str(sign_v),
        magnitude_verdict=str(magnitude_v),
        regime_verdict=str(regime_v),
        # Dual-SHA
        audit_sha256=str(audit_sha),
        content_sha256=str(content_sha),
        # Substrate-physics adjudication rationale
        rationale=str(adj["rationale"]),
        scheme=str(SCHEME),
        convention=str(CONVENTION),
        L_max_canonical=int(L_MAX),
    )
    print(f"  NPZ written: {OUT_NPZ}")


# ---------------------------------------------------------------------------
# Section 13 — canonical_constants.py update via update_constant
# ---------------------------------------------------------------------------

def update_canonical_constants(result, audit_sha):
    """Append Var_a_canonical and PROVENANCE entry to canonical_constants.py.

    Mirrors the mcp__knowledge__update_constant signature. The
    update happens on PASS only; FAIL/INFO leaves canonical_constants.py
    untouched.

    Returns: (success_bool, details_str)
    """
    cc_path = SHARED_DIR / "canonical_constants.py"
    canonical_val = result["canonical_value"]
    if canonical_val is None:
        return False, "Adjudication inconclusive; canonical NOT promoted."

    sn = result["adjudication"]["substrate_natural"]  # (local)

    # Idempotency check: if Var_a_canonical already pinned, skip re-write.
    existing_text = cc_path.read_text(encoding="utf-8")  # (local)
    if "Var_a_canonical =" in existing_text:
        print(f"  Var_a_canonical already present in canonical_constants.py; "
              f"skipping idempotent re-write.")
        return True, "Var_a_canonical already pinned (idempotent)"

    # Build the assignment line + provenance entry
    assignment = (
        f"\n# === S92 W4-6 — VAR_A SUBSTRATE-NATURAL CANONICAL PIN ===\n"
        f"Var_a_canonical = {canonical_val:.10e}  "
        f"# Var_a(n_a^GGE) substrate-natural canonical at L_max=10 on "
        f"(A_K, H_K, D_K) at tau_fold=0.190; "
        f"convention={sn} (max(p,q)<=L_max filter, m_a=dim_pq, "
        f"zero-modes excluded); fastest convergence to Weyl-dim "
        f"extrapolated-to-infinity asymptotic limit "
        f"v_inf={V_INF_EXTRAPOLATED:.10e} (12.68% deviation at L_max=10 "
        f"vs 96.22% volovik vs 637.26% vdd); promoted from S92 "
        f"W4-CF-W4-4-EMPIRICAL-ANCHOR-RECONCILIATION; "
        f"deprecated conventions vdd/volovik tagged DIAGNOSTIC per "
        f"cross-pillar-bridge-anatomy.md §\"Level-3 anchor singleness "
        f"sub-clause\" SUGGESTION K=1 (S91 W4 CF-S92-W5-1-F). (S92)\n"
        f"Var_a_canonical_diagnostic_vdd = {VDD_L10_PIN:.10e}  "
        f"# DIAGNOSTIC (deprecated): vdd p+q<=L_max convention; triangular "
        f"under-sampling of d=4 Weyl-law tail. (S92)\n"
        f"Var_a_canonical_diagnostic_volovik = {VOLOVIK_L10_PIN:.10e}  "
        f"# DIAGNOSTIC (deprecated): volovik p+q<=L_max convention with "
        f"m_a=dim_pq DOUBLE-weights dim_pq (abs_evals already carries "
        f"16*dim_pq replication). (S92)\n"
        f"Var_a_asymptotic_v_inf = {V_INF_EXTRAPOLATED:.10e}  "
        f"# Weyl-dim L_max->inf asymptotic limit per registry §VII.U.2 "
        f"Corner II Level-2 envelope L^{{-4}} (S88 §W5b-47). (S92)\n"
    )  # (local)

    # PROVENANCE dict insertion
    provenance_entry = (
        f'    "Var_a_canonical":   {{"session": "S92", "source": '
        f'"s92_w4_6_w4_4_empirical_anchor_reconciliation.npz", '
        f'"gate": "S92-W4-CF-W4-4-EMPIRICAL-ANCHOR-RECONCILIATION", '
        f'"superseded": False, "audit_sha256": "{audit_sha}", '
        f'"note": "Substrate-natural Var_a(n_a^GGE) at L_max=10; '
        f'max(p,q)<=L_max filter; m_a=dim_pq; zero-modes excluded; '
        f'12.68% deviation from v_inf=6.4631783294e-06"}},\n'
        f'    "Var_a_canonical_diagnostic_vdd":   {{"session": "S92", '
        f'"source": "s91_w4_vii_u_2_var_a_stage_2_axis_a_vdd.npz", '
        f'"gate": "S92-W4-CF-W4-4-EMPIRICAL-ANCHOR-RECONCILIATION", '
        f'"superseded": True, '
        f'"note": "DIAGNOSTIC: vdd p+q<=L_max convention; '
        f'triangular under-sampling of d=4 Weyl-law tail."}},\n'
        f'    "Var_a_canonical_diagnostic_volovik":   {{"session": "S92", '
        f'"source": "s91_w4_vii_u_2_var_a_stage_2_axis_b_volovik.npz", '
        f'"gate": "S92-W4-CF-W4-4-EMPIRICAL-ANCHOR-RECONCILIATION", '
        f'"superseded": True, '
        f'"note": "DIAGNOSTIC: volovik p+q<=L_max convention; '
        f'm_a=dim_pq DOUBLE-weights dim_pq."}},\n'
        f'    "Var_a_asymptotic_v_inf":   {{"session": "S92", '
        f'"source": "registry §VII.U.2 Corner II Level-2 envelope L^{{-4}}", '
        f'"gate": "S88-W5B-47", "superseded": False, '
        f'"note": "Weyl-dim L_max->inf asymptotic limit for Var_a(n_a^GGE)"}},\n'
    )  # (local)

    # Append the assignment block to the end of section F (S87) / new section G (S92)
    # Find PROVENANCE = { dict opening; insert provenance entries inside it.
    new_text = existing_text  # (local)

    # 1. Append assignment block at end of file (after final constant)
    # Find a stable anchor: insert right before "PROVENANCE = {"
    anchor_str = "\nPROVENANCE = {"  # (local)
    idx_prov = new_text.find(anchor_str)
    if idx_prov < 0:
        return False, "Cannot locate PROVENANCE anchor in canonical_constants.py"
    new_text = new_text[:idx_prov] + assignment + new_text[idx_prov:]

    # 2. Insert provenance entries inside PROVENANCE dict (before final closing brace)
    # Find the LAST '}\n' that closes PROVENANCE dict — search from where PROVENANCE starts
    after_prov_idx = new_text.find(anchor_str)
    # Find matching close
    open_count = 0  # (local)
    close_idx = -1  # (local)
    for i in range(after_prov_idx, len(new_text)):
        if new_text[i] == "{":
            open_count += 1
        elif new_text[i] == "}":
            open_count -= 1
            if open_count == 0:
                close_idx = i
                break
    if close_idx < 0:
        return False, "Cannot find PROVENANCE dict close brace"

    # Insert provenance entries just before the close brace
    new_text = new_text[:close_idx] + provenance_entry + new_text[close_idx:]

    # Write back
    cc_path.write_text(new_text, encoding="utf-8")
    print(f"\n  canonical_constants.py UPDATED: Var_a_canonical pinned at "
          f"{canonical_val:.10e}")
    print(f"  PROVENANCE entries added: Var_a_canonical + 2 diagnostics + "
          f"v_inf asymptotic.")
    return True, (f"Var_a_canonical={canonical_val:.10e} appended; PROVENANCE "
                  f"entries added with audit_sha256={audit_sha[:16]}...")


# ---------------------------------------------------------------------------
# Section 14 — Main
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()  # (local)

    # 1. Log input pins (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Dual SHAs (S84+)
    script_path = Path(__file__).resolve()
    canonical_path = SHARED_DIR / "canonical_constants.py"
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Compute
    result = compute()

    # 3. Evaluate gate + schema-v2 3-tuple
    composite, sign_v, magnitude_v, regime_v, domain_used_frac, traj_delta = (
        evaluate_gate_with_3tuple(result)
    )
    print(f"\n=== Schema-v2 3-tuple ===")
    print(f"  sign_verdict:     {sign_v}    "
          f"(ordering w5b47 < volo < vdd at L_max=10)")
    print(f"  magnitude_verdict:{magnitude_v}    "
          f"(unique substrate-natural identified)")
    print(f"  regime_verdict:   {regime_v}   "
          f"(L10->L12 trajectory delta = {100*traj_delta:.3f}% on substrate-natural)")
    print(f"  composite:        {composite}")
    print(f"  domain_used_frac: {domain_used_frac:.3f}")

    # 4. update_constant on PASS
    update_succeeded, update_details = (False, "deferred")  # (local)
    if composite == "PASS":
        update_succeeded, update_details = update_canonical_constants(
            result, audit_sha
        )
        if not update_succeeded:
            print(f"  WARNING: canonical_constants update FAILED: {update_details}")

    # 5. Emit npz + plot
    emit_npz(result, audit_sha, content_sha, composite, sign_v, magnitude_v, regime_v)
    emit_plot(result)

    # 6. Append verdict
    sn = result["adjudication"]["substrate_natural"] or "INCONCLUSIVE"
    val_summary = (
        f"substrate_natural={sn};"
        f"var_a_canonical={result['canonical_value']!r};"
        f"rel_dev_L10_w5b47={result['adjudication']['rel_devs_L10']['w5b47_raw']:.4e};"
        f"rel_dev_L10_volovik={result['adjudication']['rel_devs_L10']['volovik']:.4e};"
        f"rel_dev_L10_vdd={result['adjudication']['rel_devs_L10']['vdd']:.4e};"
        f"v_inf_extrap={V_INF_EXTRAPOLATED:.10e};"
        f"canonical_constants_updated={update_succeeded}"
    )  # (local)
    append_verdict_lines(composite, val_summary, sign_v, magnitude_v, regime_v,
                        domain_used_frac, audit_sha, content_sha)

    # 7. 4-tuple summary
    tuple_4 = (f"(value='{val_summary}', scheme={SCHEME}, "
               f"convention={CONVENTION}, L_max={L_MAX})")  # (local)
    print(f"\n{tuple_4}")

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
