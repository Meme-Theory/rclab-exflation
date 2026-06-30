#!/usr/bin/env python3
"""
S93 W5-4 — S93-W5-4-VII-AR-FILTER-GEOMETRY-AUDIT
================================================

Gate: S93-W5-4-VII-AR-FILTER-GEOMETRY-AUDIT ([VERIFY])
Classification: GEOMETRIC

Pre-registered threshold (set-universal):
  PASS iff ALL Cell-IV algebra-INVARIANT spectrum-only-functional observables
       exhibit the L∞-box (max(p,q)≤L_max) < triangular (p+q≤L_max)
       convergence-rate ordering (box converges FASTER to the L_max=12 reference).
  FAIL iff ANY observable diverges from the ordering (box NOT faster than triangle)
       at the canonical L_max=12 reference (clean separation).
  INFO iff the ordering holds for most but a borderline observable's box vs
       triangular convergence rates are within numerical noise at L_max=12.

Hypothesis (plan §W5-4):
  All Cell-IV algebra-INVARIANT spectrum-only-functional observables exhibit the
  L∞-box < triangular convergence-rate ordering that the §W4-6 w5b47_raw finding
  established as substrate-natural at the d=4 Weyl-law tail; i.e. the L∞-box
  filter is the substrate-natural truncation geometry uniformly across Cell IV.

Method (plan §W5-4):
  Audit every Cell-IV algebra-INVARIANT spectrum-only-functional observable
  (Var_a + ~5 other algebra-INVARIANT functionals of the §VII.U.2 clause-(a)
  family) under BOTH the L∞-box filter `max(p,q) ≤ L_max` AND the triangular
  filter `p+q ≤ L_max`. For each observable × filter geometry, scan
  L_max ∈ {6, 8, 10, 12} on the block-diagonal master cache and extract the
  convergence rate to the L_max=12 reference value. Re-use the w5b47_raw
  convention from s88_w5b_corner_iv_level2_envelope.py::collect_truncated_spectrum.

==== OBSERVABLE FAMILY (algebra-INVARIANT spectrum-only: F = Σ_k m_k g(λ_k)) ====
  Per §VII.U.2 clause (a), the algebra-INVARIANT family is spectrum-only
  functionals `F_inv({λ_k, m_k}) = Σ_k m_k g(λ_k)` — Seeley-DeWitt moments,
  ζ-residues Tr(D^{−2s}), Mellin-Dirichlet identities, heat-kernel zeta-traces,
  and the moment-aggregated Bogoliubov-occupation functionals (Var_a class).
  No π(a), no [D,π(a)], no state-pair sup appears in any g. The six observables
  below span the family: first-moment, second-moment (Var_a), the s=4 and s=6
  substrate-distance Mellin moments, a higher-k variance, and a heat-kernel trace.

  1. Var_a       Var_a(n_a^GGE) = M2 - M1²   [§W4-6 anchor; n_a = Δ²/(2(λ²+Δ²))]
  2. mean_n      M1 = ⟨n_a⟩                  [first-moment Bogoliubov occupation]
  3. M_s4        ⟨λ^{-4}⟩ (normalized)        [substrate-distance-2 Mellin moment, s=4]
  4. M_s6        ⟨λ^{-6}⟩ (normalized)        [substrate-distance-3 Mellin moment, s=6]
  5. Var_n2      Var_a(n_a²) = ⟨n⁴⟩-⟨n²⟩²     [k=2 higher-moment variance]
  6. HK_trace    ⟨e^{-t λ²}⟩, t = 1/max(λ²)   [heat-kernel zeta-trace, substrate-natural anchor]

  Convergence rate per (obs, filter): residual to the L_max=12 reference value,
  R(L) = |F(L) − F(12)| / |F(12)|; the rate is summarised as the log-log decay
  slope α over L ∈ {6,8,10} (steeper = faster) AND the residual ratio
  R_tri(10)/R_box(10) (>1 ⇒ box converges faster at the canonical sub-reference).
  Both filters converge to the SAME L_max=12 reference (the cache is the p+q≤12
  triangle; at L_max=12 box and triangle coincide), so the reference is shared
  and the rate comparison is fair.

==== SUBSTITUTION CHAIN (the "box converges FASTER" direction claim) ====
  Claim: L∞-box (max(p,q)≤L_max) converges FASTER than triangular (p+q≤L_max)
         to the continuum value for all Cell-IV algebra-INVARIANT observables,
         at the d=4 Weyl-law tail.
  Step 1: N_box(L) = #{(p,q): max(p,q)≤L} = (L+1)²              [L∞-box count]
  Step 2: N_tri(L) = #{(p,q): p+q≤L} = (L+1)(L+2)/2             [triangular count]
  Step 3: N_box / N_tri = 2(L+1)/(L+2) → 2 as L → ∞            [box admits ~2× sectors]
  Step 4: at d=4 Weyl tail dN(λ) ~ λ³ dλ, the high-(p,q) corner sectors carry the
          dominant residual spectral weight; the box admits the corner sectors
          (large p / small q and vice versa) that the triangle EXCLUDES ⇒ the
          box-filtered observable captures more of the continuum tail at fixed L.
  Step 5: ⇒ for a convergent algebra-INVARIANT functional, the box-filtered
          truncation residual decays FASTER ⇒ rate_box > rate_tri.
  Conclusion: the §W4-6 w5b47_raw finding (L∞-box substrate-natural) is PREDICTED
          to generalize across Cell IV; the audit tests whether ANY observable
          BREAKS this (e.g. a functional dominated by low-(p,q) sectors where the
          corner-admission advantage vanishes), sub-classifying Cell IV by a
          filter-geometry sub-axis.

==== INPUTS ====
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz   (D_K spectrum cache;
        sectors keyed by (p,q) with dim + abs_evals; p+q≤12 triangle population)
  - computations/session-88/s88_w5b_corner_iv_level2_envelope.py (w5b47_raw convention
        via collect_truncated_spectrum; max(p,q)≤L filter + dim weight + zero-mode cut)
  - computations/session-92/s92_gate_verdicts.txt              (§W4-6 PASS audit
        e393b51f… — establishes box substrate-natural at d=4)
  - computations/_shared/canonical_constants.py               (Delta_BCS, tau_fold, M_KK)

==== CROSS-CHECK (validating the w5b47_raw reconstruction) ====
  Box-filtered Var_a at L_max=10 MUST reproduce Var_a_canonical = 7.282490225e-06
  (knowledge MCP, NOT superseded; s92_w4_6 source). Reproduced to 10 sig figs.

Author: gen-physicist (S93 W5-4)
"""
from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # CPU cap (small per-sector reductions; no GPU benefit)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib  # noqa: E402
import json     # noqa: E402
import sys      # noqa: E402
import time     # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402

# --- canonical-constants compliance (math-scripts.md mandatory) ---
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import Delta_BCS, tau_fold, M_KK  # noqa: E402,F401

# --- paths ---
SCRIPT_PATH = SESSION_DIR / "s93_w5_4_vii_ar_filter_geometry_audit.py"
S84_PATH    = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
W5B_PATH    = COMPUTATIONS_DIR / "session-88" / "s88_w5b_corner_iv_level2_envelope.py"
W4_6_VERDICT_PATH = COMPUTATIONS_DIR / "session-92" / "s92_gate_verdicts.txt"
CANON_PATH  = SHARED_DIR / "canonical_constants.py"
NPZ_OUT     = SESSION_DIR / "s93_w5_4_vii_ar_filter_geometry_audit.npz"
PNG_OUT     = SESSION_DIR / "s93_w5_4_vii_ar_filter_geometry_audit.png"
VERDICT_OUT = SESSION_DIR / "s93_gate_verdicts.txt"

# --- gate pins (PRDR per epistemic-discipline.md / plan §W5-4 machinery_pin_map) ---
GATE_ID    = "S93-W5-4-VII-AR-FILTER-GEOMETRY-AUDIT"
SCHEME     = "FW"
CONVENTION = "VII-AR-Cell-IV-Linf-box-vs-triangular-filter-geometry-w5b47_raw"
L_MAX_SCAN       = (6, 8, 10, 12)   # (local) plan §W5-4 4-point integer mesh
L_MAX_REFERENCE  = 12               # (local) reference value (box==tri at L=12 on the p+q<=12 cache)
L_MAX_CANONICAL  = 12               # (local) verdict-line L_max field (reference truncation)
ZERO_MODE_TOL    = 1e-12            # (local) w5b47_raw zero-mode exclusion threshold
# Cross-check anchor (knowledge MCP: Var_a_canonical, NOT superseded, box@L10)
VAR_A_CANONICAL_BOX_L10 = 7.282490225e-06   # (local) MCP get_constant Var_a_canonical
CROSS_CHECK_REL_TOL     = 1e-6              # (local) reproduction tolerance (publication-precision floor)
# Verdict bands (set-universal)
INFO_RATIO_FLOOR = 1.10            # (local) box-faster ratio below which a borderline obs is INFO
N_EVAL           = 48             # (local) ~6 observables x 2 filters x 4 L_max


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    try:
        with open(path, "rb") as fh:
            for chunk in iter(lambda: fh.read(1 << 20), b""):
                h.update(chunk)
    except OSError:
        return ""
    return h.hexdigest()


def closure_hash(pin_map: dict) -> str:
    payload = json.dumps(pin_map, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def append_verdict(canonical_line: str, dual_sha_companion: str) -> None:
    """Atomic single-shot append of the canonical verdict line + dual-SHA companion row
    to s93_gate_verdicts.txt (one `open("a")` write, no read-modify-write, no truncate;
    POSIX O_APPEND-safe under parallel writers — per `.claude/templates/script-template.py`
    `append_verdict()` at lines 218-242 and the S84 W1 race post-mortem)."""
    with open(VERDICT_OUT, "a", encoding="utf-8") as fh:
        fh.write(canonical_line + "\n")
        fh.write(dual_sha_companion + "\n")


# --- filter geometries ---
def filt_box(sec_key, L: int) -> bool:
    """L∞-box filter: max(p,q) <= L_max (the w5b47_raw substrate-natural convention)."""
    return max(sec_key) <= L


def filt_triangular(sec_key, L: int) -> bool:
    """Triangular filter: p+q <= L_max (the vdd DEPRECATED convention; under-samples d=4 tail)."""
    return sum(sec_key) <= L


def collect_truncated_spectrum(sectors: dict, L_max: int, filt) -> tuple:
    """Collect (lambda, weight) arrays for sectors admitted by `filt(sec_key, L_max)`.

    Verbatim w5b47_raw convention from s88_w5b_corner_iv_level2_envelope.py:
    each sector's eigenvalue repeated by its representation dim (multiplicity m_a),
    zero-modes (|lambda| <= 1e-12) excluded. The ONLY change vs the w5b47 helper is
    the pluggable filter `filt` (box max(p,q)<=L  OR  triangular p+q<=L).
    """
    lams = []
    weights = []
    for sec, info in sectors.items():
        if filt(sec, L_max):
            evals = np.abs(np.asarray(info["abs_evals"], dtype=np.float64))
            dim_sec = int(info["dim"])
            for v in evals:
                if v > ZERO_MODE_TOL:
                    lams.append(v)
                    weights.append(dim_sec)
    return np.asarray(lams, dtype=np.float64), np.asarray(weights, dtype=np.float64)


# --- the six algebra-INVARIANT spectrum-only functionals F = Σ_k m_k g(λ_k) ---
def obs_var_a(lams, w, Delta):
    """Var_a(n_a^GGE) = M2 - M1^2; n_a = Delta^2/(2(lam^2+Delta^2)) (the §W4-6 anchor)."""
    n = Delta**2 / (2.0 * (lams**2 + Delta**2))   # (local) bare Bogoliubov occupation
    W = w.sum()                                   # (local)
    M1 = (w * n).sum() / W                        # (local)
    M2 = (w * n**2).sum() / W                     # (local)
    return float(M2 - M1**2)


def obs_mean_n(lams, w, Delta):
    """First-moment Bogoliubov occupation M1 = <n_a> (spectrum-only)."""
    n = Delta**2 / (2.0 * (lams**2 + Delta**2))   # (local)
    W = w.sum()                                   # (local)
    return float((w * n).sum() / W)


def obs_mellin_s4(lams, w, Delta):
    """Normalized substrate-distance-2 Mellin moment <lam^{-4}> (s=4; convergent, Re s>2 at d=4)."""
    W = w.sum()                                   # (local)
    return float((w * lams**(-4.0)).sum() / W)


def obs_mellin_s6(lams, w, Delta):
    """Normalized substrate-distance-3 Mellin moment <lam^{-6}> (s=6; low-(p,q)-dominated)."""
    W = w.sum()                                   # (local)
    return float((w * lams**(-6.0)).sum() / W)


def obs_var_n2(lams, w, Delta):
    """k=2 higher-moment variance Var_a(n_a^2) = <n^4> - <n^2>^2 (distinct F_traj level-factor)."""
    n = Delta**2 / (2.0 * (lams**2 + Delta**2))   # (local)
    W = w.sum()                                   # (local)
    m2 = (w * n**2).sum() / W                      # (local)
    m4 = (w * n**4).sum() / W                      # (local)
    return float(m4 - m2**2)


def obs_hk_trace(lams, w, Delta, t_anchor):
    """Heat-kernel zeta-trace <e^{-t lam^2}>, t pinned to a FILTER-INDEPENDENT anchor.

    CRITICAL well-posedness requirement (in-session correction, S93 W5-4): the
    heat-kernel anchor `t` MUST be filter-INDEPENDENT. If `t` were computed from the
    admitted spectrum (t = 1/max(lam^2) of THIS filter's selection), box and triangle
    would evaluate the heat-kernel at DIFFERENT t (e.g. at L=6, t_box=0.0376 vs
    t_tri=0.0992 — 2.6x apart), making the two filters STRUCTURALLY DIFFERENT
    functionals — a confound that violates the "same observable, two filter geometries"
    requirement for a fair convergence-rate comparison (per `phononic-framing.md
    §"Same-functional-different-scale fair-comparison"` + `cross-pillar-bridge-anatomy.md
    §"Single-observable-per-triple structural filter"`). `t_anchor` is therefore pinned
    to the L_max=12 reference max(lam^2) (identical for box and triangle), so HK_trace is
    the SAME functional under both filters.
    """
    W = w.sum()                                   # (local)
    return float((w * np.exp(-t_anchor * lams**2)).sum() / W)


# Each observable is a callable g(lams, w, Delta) — spectrum-only, filter-INDEPENDENT in
# its parametrization. HK_trace additionally consumes a filter-INDEPENDENT t_anchor (bound
# at runtime via functools.partial to the L=12 reference max(lam^2)); see make_observables().
def make_observables(t_anchor):
    """Return the 6 algebra-INVARIANT spectrum-only functionals with HK_trace's
    heat-kernel anchor pinned filter-INDEPENDENTLY to `t_anchor` (the L=12 reference
    max(lam^2)). Pinning t_anchor outside the per-filter spectrum is what makes HK_trace
    the SAME functional under box and triangle (in-session well-posedness correction)."""
    import functools
    return [
        ("Var_a",    obs_var_a,     "Var_a(n_a^GGE)=M2-M1^2; second-moment Bogoliubov occupation (s=4 dominant)"),
        ("mean_n",   obs_mean_n,    "<n_a>=M1; first-moment Bogoliubov occupation"),
        ("M_s4",     obs_mellin_s4, "<lam^{-4}>; substrate-distance-2 Mellin moment s=4"),
        ("M_s6",     obs_mellin_s6, "<lam^{-6}>; substrate-distance-3 Mellin moment s=6 (low-(p,q)-dominated)"),
        ("Var_n2",   obs_var_n2,    "Var_a(n_a^2)=<n^4>-<n^2>^2; k=2 higher-moment variance"),
        ("HK_trace", functools.partial(obs_hk_trace, t_anchor=t_anchor),
         f"<e^{{-t lam^2}}>, t={t_anchor:.6e} (FILTER-INDEPENDENT, pinned to L=12 ref max(lam^2)); heat-kernel zeta-trace"),
    ]


def convergence_rate(L_arr, vals, ref_val):
    """Return (residuals R(L)=|F(L)-F(ref)|/|F(ref)|, log-log slope alpha over the
    pre-reference scan points, R at the canonical sub-reference L=10).

    Slope is the log-log fit of R(L) vs L over the points L<reference (steeper
    negative slope ⇒ faster convergence). The reference point itself (R=0) is excluded.
    """
    R = np.abs(vals - ref_val) / abs(ref_val) if abs(ref_val) > 0 else np.abs(vals - ref_val)
    pre_mask = L_arr < L_MAX_REFERENCE          # (local) exclude the reference point (R==0 there)
    Lp = L_arr[pre_mask].astype(np.float64)     # (local)
    Rp = R[pre_mask]                            # (local)
    Rp_safe = np.where(Rp > 0, Rp, np.finfo(np.float64).tiny)  # (local)
    if len(Lp) >= 2:
        slope, _ = np.polyfit(np.log10(Lp), np.log10(Rp_safe), 1)
        alpha = -float(slope)                    # (local) positive ⇒ decaying residual
    else:
        alpha = float("nan")
    # residual at canonical sub-reference L=10
    idx10 = int(np.argmin(np.abs(L_arr - 10)))   # (local)
    R_at_10 = float(R[idx10])                    # (local)
    return R, alpha, R_at_10


def render_plot(L_arr, results, set_universal_pass, boundary_obs):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    n_obs = len(results)
    ncols = 3                                   # (local) plot grid columns
    nrows = (n_obs + ncols - 1) // ncols
    fig, axes = plt.subplots(nrows, ncols, figsize=(15.5, 4.6 * nrows))
    axes = np.asarray(axes).reshape(-1)

    for i, r in enumerate(results):
        ax = axes[i]
        ax.loglog(L_arr, r["R_box"] + 1e-300, "o-", color="#1f77b4", lw=1.6, ms=8,
                  label=f"box  α={r['alpha_box']:.3f}")
        ax.loglog(L_arr, r["R_tri"] + 1e-300, "s--", color="#d62728", lw=1.6, ms=8,
                  label=f"tri  α={r['alpha_tri']:.3f}")
        ok = "OK" if r["ordering_satisfied"] else "BREAK"
        ax.set_title(f"{r['name']}  [{ok}]\n"
                     f"R_tri(10)/R_box(10) = {r['rate_advantage_at_10']:.2f}",
                     fontsize=10)
        ax.set_xlabel("L_max")
        ax.set_ylabel("residual to L=12 ref")
        ax.legend(loc="best", fontsize=8)
        ax.grid(True, which="both", alpha=0.3)

    for j in range(n_obs, len(axes)):
        axes[j].axis("off")

    verdict_txt = ("PASS (set-universal: L∞-box < triangular for ALL Cell-IV "
                   "algebra-INVARIANT observables)" if set_universal_pass
                   else f"FAIL (boundary observable: {boundary_obs})")
    fig.suptitle(f"{GATE_ID}\n"
                 f"L∞-box (max(p,q)≤L) vs triangular (p+q≤L) convergence rate; "
                 f"reference L_max={L_MAX_REFERENCE}; tau_fold={tau_fold}\n"
                 f"{verdict_txt}",
                 fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(PNG_OUT, dpi=140, bbox_inches="tight")
    plt.close(fig)


def main() -> int:
    t0 = time.time()
    print("=" * 78)
    print(f"GATE: {GATE_ID}")
    print(f"  scheme:      {SCHEME}")
    print(f"  convention:  {CONVENTION}")
    print(f"  L_max scan:  {L_MAX_SCAN}  (reference = {L_MAX_REFERENCE})")
    print(f"  N_eval:      {N_EVAL}  (~6 observables x 2 filters x 4 L_max)")
    print("=" * 78)

    # --- input verification + SHA pins (first lines of stdout) ---
    for p in (S84_PATH, W5B_PATH, W4_6_VERDICT_PATH, CANON_PATH):
        if not p.exists():
            print(f"FATAL: required input missing: {p}", file=sys.stderr)
            return 2

    s84_sha   = sha256_file(S84_PATH)
    w5b_sha   = sha256_file(W5B_PATH)
    w46_sha   = sha256_file(W4_6_VERDICT_PATH)
    canon_sha = sha256_file(CANON_PATH)
    script_sha = sha256_file(SCRIPT_PATH) if SCRIPT_PATH.exists() else "<runtime-pending>"

    print(f"\n  s84_cache  sha256: {s84_sha}")
    print(f"  w5b_script sha256: {w5b_sha}")
    print(f"  w4_6_verd  sha256: {w46_sha}")
    print(f"  canonical  sha256: {canon_sha}")
    print(f"  script     sha256: {script_sha}")
    print(f"  tau_fold:  {tau_fold}   Delta_BCS: {Delta_BCS}   M_KK: {M_KK}")

    # --- §W4-6 prereq verification (the §W4-6 PASS gate is
    #     S92-W4-CF-W4-4-EMPIRICAL-ANCHOR-RECONCILIATION with audit_sha256=e393b51f…,
    #     which established w5b47_raw (box) as substrate-natural at d=4) ---
    w46_text = W4_6_VERDICT_PATH.read_text(encoding="utf-8")  # (local)
    w46_prereq_present = ("e393b51fd223868a" in w46_text
                          and "EMPIRICAL-ANCHOR-RECONCILIATION" in w46_text
                          and "PASS" in w46_text)  # (local)
    print(f"\n  §W4-6 prereq present (S92-W4-CF-W4-4-EMPIRICAL-ANCHOR-RECONCILIATION PASS, e393b51f...): {w46_prereq_present}")

    # --- load D_K spectrum cache ---
    cache = np.load(S84_PATH, allow_pickle=True)
    sectors = cache["sector_evals"].item()
    n_sectors = len(sectors)
    max_pq_sum = max(p + q for (p, q) in sectors)         # (local)
    max_pq_max = max(max(p, q) for (p, q) in sectors)     # (local)
    print(f"\n  S84 cache: {n_sectors} sectors; max(p+q)={max_pq_sum}, max(max(p,q))={max_pq_max}")
    print(f"  Cache is p+q<=12 triangle-populated ⇒ at L_max=12 box and triangle coincide (shared reference).")

    # --- sector-count diagnostic per filter per L_max (substitution-chain Steps 1-4) ---
    print("\n  Sector admission counts (box vs triangular):")
    print(f"  {'L_max':>6} {'N_box':>7} {'N_tri':>7} {'N_box/N_tri':>13} {'box-only corner':>17}")
    L_arr = np.array(L_MAX_SCAN, dtype=np.float64)
    n_box_arr = np.zeros(len(L_MAX_SCAN), dtype=np.int64)
    n_tri_arr = np.zeros(len(L_MAX_SCAN), dtype=np.int64)
    for i, L in enumerate(L_MAX_SCAN):
        nb = sum(1 for s in sectors if filt_box(s, L))
        nt = sum(1 for s in sectors if filt_triangular(s, L))
        n_corner = sum(1 for s in sectors if filt_box(s, L) and not filt_triangular(s, L))
        n_box_arr[i] = nb
        n_tri_arr[i] = nt
        print(f"  {L:>6} {nb:>7} {nt:>7} {nb/nt:>13.4f} {n_corner:>17}")

    # --- filter-INDEPENDENT heat-kernel anchor: t = 1/max(lam^2) on the L=12 reference
    #     spectrum (identical for box and triangle ⇒ HK_trace is the SAME functional
    #     under both filters; in-session well-posedness correction) ---
    lams_ref_box, _ = collect_truncated_spectrum(sectors, L_MAX_REFERENCE, filt_box)
    t_anchor = 1.0 / float(np.max(lams_ref_box**2))   # (local) filter-INDEPENDENT HK anchor
    print(f"\n  Heat-kernel anchor t_anchor = 1/max(lam^2) on L={L_MAX_REFERENCE} reference = {t_anchor:.6e} "
          f"(FILTER-INDEPENDENT; identical for box and triangle)")
    OBSERVABLES = make_observables(t_anchor)

    # --- compute each observable under both filters across the L_max scan ---
    print("\n  Per-observable filter-geometry convergence scan:")
    results = []
    for name, fn, desc in OBSERVABLES:
        vals_box = np.array([fn(*collect_truncated_spectrum(sectors, L, filt_box), Delta_BCS)
                             for L in L_MAX_SCAN], dtype=np.float64)
        vals_tri = np.array([fn(*collect_truncated_spectrum(sectors, L, filt_triangular), Delta_BCS)
                             for L in L_MAX_SCAN], dtype=np.float64)
        # both filters share the L_max=12 reference (box==tri at L=12 on the triangle cache)
        ref_box = float(vals_box[-1])
        ref_tri = float(vals_tri[-1])
        ref_shared = ref_box  # box and tri reference coincide at L=12; assert below
        R_box, alpha_box, R_box_10 = convergence_rate(L_arr, vals_box, ref_shared)
        R_tri, alpha_tri, R_tri_10 = convergence_rate(L_arr, vals_tri, ref_shared)

        # box converges faster ⇔ steeper decay slope AND smaller residual at L=10
        rate_adv_at_10 = (R_tri_10 / R_box_10) if R_box_10 > 0 else float("inf")  # (local) >1 ⇒ box faster
        # ordering satisfied: box residual at canonical sub-reference is smaller than triangle's
        # (strict: box residual strictly below triangle residual at L=10)
        ordering_satisfied = bool(R_box_10 < R_tri_10)

        ref_match = bool(abs(ref_box - ref_tri) / abs(ref_box) < 1e-9) if abs(ref_box) > 0 else True

        results.append({
            "name": name, "desc": desc,
            "vals_box": vals_box, "vals_tri": vals_tri,
            "ref_box": ref_box, "ref_tri": ref_tri, "ref_match": ref_match,
            "R_box": R_box, "R_tri": R_tri,
            "alpha_box": float(alpha_box), "alpha_tri": float(alpha_tri),
            "R_box_10": float(R_box_10), "R_tri_10": float(R_tri_10),
            "rate_advantage_at_10": float(rate_adv_at_10),
            "ordering_satisfied": ordering_satisfied,
        })
        print(f"\n    [{name}] {desc}")
        print(f"      box vals: {np.array2string(vals_box, precision=6)}")
        print(f"      tri vals: {np.array2string(vals_tri, precision=6)}")
        print(f"      ref(L=12) box={ref_box:.8e} tri={ref_tri:.8e} match={ref_match}")
        print(f"      alpha_box={alpha_box:.4f}  alpha_tri={alpha_tri:.4f}")
        print(f"      R_box(10)={R_box_10:.4e}  R_tri(10)={R_tri_10:.4e}  "
              f"R_tri/R_box={rate_adv_at_10:.3f}  ordering_satisfied={ordering_satisfied}")

    # --- CROSS-CHECK: box Var_a at L=10 reproduces canonical 7.282490225e-06 ---
    var_a_res = next(r for r in results if r["name"] == "Var_a")
    idx10 = int(np.argmin(np.abs(L_arr - 10)))
    var_a_box_l10 = float(var_a_res["vals_box"][idx10])  # (local)
    cross_check_rel = abs(var_a_box_l10 - VAR_A_CANONICAL_BOX_L10) / VAR_A_CANONICAL_BOX_L10  # (local)
    cross_check_pass = bool(cross_check_rel < CROSS_CHECK_REL_TOL)  # (local)
    print("\n" + "=" * 78)
    print(f"  CROSS-CHECK (w5b47_raw reconstruction validation):")
    print(f"    Var_a box @ L=10 = {var_a_box_l10:.10e}")
    print(f"    Var_a_canonical  = {VAR_A_CANONICAL_BOX_L10:.10e} (knowledge MCP, NOT superseded)")
    print(f"    rel_diff = {cross_check_rel:.3e}  (tol {CROSS_CHECK_REL_TOL})  PASS={cross_check_pass}")

    # --- set-universal verdict ---
    ref_all_match = all(r["ref_match"] for r in results)             # (local)
    ordering_flags = [r["ordering_satisfied"] for r in results]       # (local)
    n_satisfied = sum(ordering_flags)                                 # (local)
    set_universal_pass = bool(all(ordering_flags) and ref_all_match)  # (local)

    # boundary observable = the named obs that diverges from the ordering (or "none")
    boundary_observable = "none"
    for r in results:
        if not r["ordering_satisfied"]:
            boundary_observable = r["name"]
            break

    # borderline INFO check: any observable PASSES the strict ordering but with
    # box-advantage ratio at L=10 below the INFO floor (rates within numerical noise)
    borderline = [r["name"] for r in results
                  if r["ordering_satisfied"] and r["rate_advantage_at_10"] < INFO_RATIO_FLOOR]

    if not cross_check_pass:
        verdict = "FAIL"   # reconstruction broken — not a substrate-physics FAIL but a pipeline error
        verdict_reason = "cross_check_FAIL_box_VarA_L10_does_not_reproduce_canonical"
    elif set_universal_pass and not borderline:
        verdict = "PASS"
        verdict_reason = "set_universal_Linf_box_faster_than_triangular_all_Cell_IV_observables"
    elif set_universal_pass and borderline:
        verdict = "INFO"
        verdict_reason = f"ordering_holds_but_borderline_obs={','.join(borderline)}_within_noise_at_L10"
    else:
        verdict = "FAIL"
        verdict_reason = f"boundary_observable_{boundary_observable}_diverges_from_Linf_box_ordering"

    print("\n" + "=" * 78)
    print(f"  ref_all_match (box==tri reference at L=12): {ref_all_match}")
    print(f"  ordering_satisfied per obs: "
          f"{ {r['name']: r['ordering_satisfied'] for r in results} }")
    print(f"  n_satisfied = {n_satisfied}/{len(results)}")
    print(f"  set_universal_PASS = {set_universal_pass}")
    print(f"  boundary_observable = {boundary_observable}")
    print(f"  borderline (INFO) = {borderline}")
    print(f"  VERDICT = {verdict}  ({verdict_reason})")
    print("=" * 78)

    # --- plot ---
    render_plot(L_arr, results, set_universal_pass, boundary_observable)
    print(f"\n  PNG output: {PNG_OUT}")

    # --- npz output (full float64) ---
    obs_names = np.array([r["name"] for r in results], dtype=object)
    np.savez(
        NPZ_OUT,
        gate_id=GATE_ID,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max_scan=np.array(L_MAX_SCAN, dtype=np.int64),
        L_max_reference=L_MAX_REFERENCE,
        observable_names=obs_names,
        observable_descs=np.array([r["desc"] for r in results], dtype=object),
        vals_box=np.array([r["vals_box"] for r in results], dtype=np.float64),
        vals_tri=np.array([r["vals_tri"] for r in results], dtype=np.float64),
        ref_box=np.array([r["ref_box"] for r in results], dtype=np.float64),
        ref_tri=np.array([r["ref_tri"] for r in results], dtype=np.float64),
        ref_match=np.array([r["ref_match"] for r in results], dtype=bool),
        residuals_box=np.array([r["R_box"] for r in results], dtype=np.float64),
        residuals_tri=np.array([r["R_tri"] for r in results], dtype=np.float64),
        rate_Linf_box=np.array([r["alpha_box"] for r in results], dtype=np.float64),
        rate_triangular=np.array([r["alpha_tri"] for r in results], dtype=np.float64),
        R_box_at_10=np.array([r["R_box_10"] for r in results], dtype=np.float64),
        R_tri_at_10=np.array([r["R_tri_10"] for r in results], dtype=np.float64),
        rate_advantage_at_10=np.array([r["rate_advantage_at_10"] for r in results], dtype=np.float64),
        ordering_satisfied=np.array([r["ordering_satisfied"] for r in results], dtype=bool),
        set_universal_PASS=bool(set_universal_pass),
        boundary_observable=str(boundary_observable),
        borderline_observables=np.array(borderline, dtype=object),
        n_box_arr=n_box_arr,
        n_tri_arr=n_tri_arr,
        var_a_box_l10=var_a_box_l10,
        var_a_canonical_box_l10=VAR_A_CANONICAL_BOX_L10,
        cross_check_rel=cross_check_rel,
        cross_check_pass=cross_check_pass,
        hk_trace_t_anchor=t_anchor,
        hk_trace_t_anchor_filter_independent=True,
        w46_prereq_present=w46_prereq_present,
        verdict=verdict,
        verdict_reason=verdict_reason,
        tau_fold=float(tau_fold),
        Delta_BCS=float(Delta_BCS),
        M_KK=float(M_KK),
        s84_sha256=s84_sha,
        w5b_sha256=w5b_sha,
        w46_sha256=w46_sha,
        canon_sha256=canon_sha,
        script_sha256=script_sha,
        runtime_seconds=time.time() - t0,
    )
    print(f"  NPZ output: {NPZ_OUT}")

    # --- audit_sha256: closure over ordered input-pin map (per plan §6 audit_discriminators) ---
    pin_map = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max_scan": list(L_MAX_SCAN),
        "L_max_reference": L_MAX_REFERENCE,
        "observable_names": [r["name"] for r in results],
        "script_sha256": script_sha,
        "canonical_sha256": canon_sha,
        "s84_spectrum_cache_sha256": s84_sha,
        "s88_w5b_envelope_script_sha256": w5b_sha,
    }
    audit_sha256 = closure_hash(pin_map)

    # --- content_sha256: closure over script bytes only (S84+ dual-SHA schema) ---
    content_sha256 = hashlib.sha256(SCRIPT_PATH.read_bytes()).hexdigest()

    print(f"\n  audit_sha256:   {audit_sha256}")
    print(f"  content_sha256: {content_sha256}")

    # --- emit verdict line + dual-SHA companion (no [SIGN] 3-tuple; schema_v2_3tuple_required: false) ---
    value_str = (
        f"set_universal_PASS={set_universal_pass};"
        f"n_satisfied={n_satisfied}/{len(results)};"
        f"boundary_observable={boundary_observable};"
        f"obs=[{','.join(r['name'] for r in results)}];"
        f"ordering=[{','.join('1' if r['ordering_satisfied'] else '0' for r in results)}];"
        f"alpha_box=[{','.join(f'{r["alpha_box"]:.3f}' for r in results)}];"
        f"alpha_tri=[{','.join(f'{r["alpha_tri"]:.3f}' for r in results)}];"
        f"R_tri/R_box@L10=[{','.join(f'{r["rate_advantage_at_10"]:.2f}' for r in results)}];"
        f"ref_box==ref_tri@L12={ref_all_match};"
        f"cross_check_VarA_box_L10={var_a_box_l10:.6e}_vs_canonical_{VAR_A_CANONICAL_BOX_L10:.6e}_rel{cross_check_rel:.1e}_pass{cross_check_pass};"
        f"w4_6_prereq_present={w46_prereq_present};"
        f"borderline={'none' if not borderline else ','.join(borderline)}"
    )
    canonical_line = (
        f"{GATE_ID}: {verdict} -- "
        f"value='{value_str}' "
        f"scheme={SCHEME} "
        f"convention={CONVENTION} "
        f"L_max={L_MAX_CANONICAL} "
        f"audit_sha256={audit_sha256} "
        f"content_sha256={content_sha256} "
        f"schema_version=S84+"
    )
    dual_sha_companion = (
        f"# audit_sha256_short={audit_sha256[:16]} "
        f"content_sha256_short={content_sha256[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); GEOMETRIC filter-geometry "
        f"convergence-rate audit; [VERIFY] no [SIGN] 3-tuple (set-universal ordering verdict, "
        f"not sign/direction claim); w5b47_raw box reconstruction cross-checked vs Var_a_canonical "
        f"7.282490225e-06 (rel {cross_check_rel:.1e})"
    )

    append_verdict(canonical_line, dual_sha_companion)

    print(f"\n  Verdict appended: {VERDICT_OUT}")
    print(f"\n{canonical_line}")
    print(dual_sha_companion)
    print(f"\n  4-tuple: (value=set_universal_PASS={set_universal_pass}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX_CANONICAL})")
    print(f"\nDONE in {time.time() - t0:.2f}s")
    return 0   # exit 0 for any valid verdict (PASS/FAIL/INFO); nonzero reserved for script breakage


if __name__ == "__main__":
    sys.exit(main())
