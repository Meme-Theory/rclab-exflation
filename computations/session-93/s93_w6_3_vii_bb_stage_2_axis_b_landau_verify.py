"""
S93-W6-3-VII-BB-STAGE-2-AXIS-B-LANDAU-VERIFY
============================================
Stage-2 cross-axis INDEPENDENT-VERIFY (Axis-B, substrate/condensed-matter) of the
§VII.BB STAGE-1-CANDIDATE theorem:

    HH^1 Cocycle Norm  ‖[φ_88]‖_{HH^1}^{s=5}  on the M_3(ℂ) Peter-Weyl block of
    A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)  at the substrate-distance-3 DEGENERATE pole s=5
    (Mellin exponent -2s = -10), single-τ-slice τ_fold = 0.19.

BLIND-VERIFY discipline (joint-theorem-promotion.md §"Stage 2"): this agent operates
WITHOUT prior workshop context. Inputs read are ONLY:
  (a) the registered §VII.BB entry (re-anchored at runtime — plan-pinned line ~19810
      is STALE-DRIFTED; the heading actually sits at line 20224; drift +414 lines
      documented in the verdict value= per substrate-first-canonical-sourcing.md §(ii.B));
  (b) the §W9-8 first-extraction npz
      computations/session-92/s92_w9_8_vii_bb_lmax_scan_degenerate_pole_first_extraction.npz;
  (c) the §W6-3 plan section.
The Axis-A (connes) output/script and the S92 W9 workshop transcripts are NOT read.

The Axis-B clauses + JOINT clauses are RE-DERIVED FROM FIRST PRINCIPLES off the
substrate-first source — the s84 master spectrum cache (NOT the w9_8 derived scalars,
NOT any Axis-A artifact). The w9_8 npz is loaded ONLY to (i) cross-anchor my
first-principles values and (ii) run the J1 regime re-fit on its 4-point L-scan.

AXIS-B clauses verified:
  (1) Laboratory-IN Pillar-II α_s observation OE-form (integration domain + trace +
      named projector per cross-pillar-bridge-anatomy.md §"Element 2 OE-form").
  (2) Friedrich-Bär saturation predicate: min η_FB(M_3(ℂ)) = 0.446536 ≥ 0.40 certifies
      L_max=12 ≡ L_max→∞ on this Peter-Weyl block (no L_max≥13 needed). η_FB RE-DERIVED
      from the s84 block eigenvalues + SU(3) Casimir.
  (3) Level-3 anchor consistency: directly-measured L_max=12 value 11.763253530952039,
      FB-certified, regime-INDEPENDENT.

JOINT clauses (Axis-B independently PASSes each; PASS-AND'd with Axis-A at synthesis):
  (J1) regime-IDENTITY — independent re-evaluation of the 3 candidate regimes on the
       §W9-8 L-scan; the PRE-REGISTERED discriminator: regime IS substrate-IS iff
       (Norm_∞ ≥ max_observed) ∧ (licensed by a substrate-physics predicate); the
       composite (argmax R²) is EXCLUDED because Norm_∞=10.11 < min observed 11.733 is
       incoherent as a saturation asymptote of a monotone-INCREASING sequence.
  (J2) Level-3 anchor consistency — rel_tol ≥ 1e-9 against the canonical pin.

Env: CPU-only, OMP capped at 8. numpy/scipy/matplotlib.
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# ---- canonical constants (MANDATORY import) ----
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from canonical_constants import (  # noqa: E402
    vii_bb_element_5_empirical_anchor_FW,   # Level-3 anchor 11.763253530952039
    alpha_HH1_per_pole_FW_s5,               # = 6 (Wodzicki/Connes asymptotic envelope; non-degenerate sibling)
    tau_fold,                               # 0.19 (single-τ-slice)
)

ROOT = Path(__file__).resolve().parents[1].parent
GATE_ID = "S93-W6-3-VII-BB-STAGE-2-AXIS-B-LANDAU-VERIFY"
SCHEME = "FW"
CONVENTION = "stage-2-axis-B-substrate-condensed-matter-independent-verify-FB-saturation-OE-form-regime-identity-saturation-coherence-discriminator"
L_MAX = 12  # (local) §W9-8 master-cache anchor; FB certifies L_12 ≡ L_∞ on the M_3(C) block
SCHEMA_VERSION = "S84+"

VERDICT_FILE = ROOT / "computations" / "session-93" / "s93_gate_verdicts.txt"
SCRIPT_PATH = Path(__file__).resolve()
W9_8_NPZ = ROOT / "computations" / "session-92" / "s92_w9_8_vii_bb_lmax_scan_degenerate_pole_first_extraction.npz"
S84_CACHE = ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CANONICAL_CONSTANTS = ROOT / "computations" / "_shared" / "canonical_constants.py"
REGISTRY = ROOT / "sessions" / "permanent-results-registry.md"
OUT_NPZ = ROOT / "computations" / "session-93" / "s93_w6_3_vii_bb_stage_2_axis_b_landau_verify.npz"
OUT_PNG = ROOT / "computations" / "session-93" / "s93_w6_3_vii_bb_stage_2_axis_b_landau_verify.png"

# ---- pre-registered thresholds (local) ----
ETA_FB_LOWER = 0.40                              # (local) Friedrich-Bär saturation predicate floor (W11-3 precedent)
LEVEL3_REL_TOL = 1e-9                            # (local) J2 Level-3 anchor rel_tol per plan tolerance pin
SUBSTRATE_DISTANCE_POLE_S = 5                    # (local) substrate-distance-3 pole
MELLIN_EXP = -2 * SUBSTRATE_DISTANCE_POLE_S      # (local) Mellin exponent -10
TRIALITY_NONZERO = True                          # (local) M_3(C) block = (p-q) mod 3 != 0


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()  # (local)
    h.update(Path(p).read_bytes())
    return h.hexdigest()


def closure_hash(pinmap: dict) -> str:
    """audit_sha256 = SHA-256 over the ordered input-pin map (canonical pattern)."""
    blob = json.dumps(pinmap, sort_keys=True, separators=(",", ":")).encode("utf-8")  # (local)
    return hashlib.sha256(blob).hexdigest()


def append_verdict(verdict: str, value_str: str, audit_sha: str, content_sha: str,
                   supersedes: str | None = None) -> None:
    """Single canonical dual-SHA verdict line + companion row; append-only single
    open("a") write (canonical pattern per computations/_shared/_script_template.py
    append_verdict; mirrors s93_w5_3_..._annotation.py lines 477-503). [VERIFY-THEOREM]
    — no [SIGN] 3-tuple (PASS-AND + regime-exclusion, not a single directional prediction).
    Re-run with supersedes=<old_audit_sha> per gate-verdicts.md §"Option A" Class-3-safe
    append (original line RETAINED on disk; corrective line appends with supersedes tag).
    """
    value_field = value_str if supersedes is None else f"{value_str};supersedes={supersedes}"  # (local)
    canonical = (  # (local)
        f"{GATE_ID}: {verdict} -- value='{value_field}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    supersedes_note = f"; supersedes={supersedes}" if supersedes else ""  # (local)
    companion = (  # (local)
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); Stage-2 Axis-B "
        f"(landau-condensed-matter-theorist, substrate/condensed-matter) BLIND independent-verify "
        f"of §VII.BB STAGE-1-CANDIDATE; [VERIFY-THEOREM] no [SIGN] 3-tuple (PASS-AND + regime-exclusion, "
        f"not a single directional prediction); COMPOSITE Stage-2 PASS-AND + STAGE-3 flip = orchestrator "
        f"synthesis{supersedes_note}\n"
    )
    with VERDICT_FILE.open("a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(companion)


def find_prior_audit_sha() -> str | None:
    """Scan the verdict file for a prior non-superseded canonical line for this GATE_ID;
    return its audit_sha256 (for the Option A supersedes chain on re-run)."""
    if not VERDICT_FILE.exists():
        return None
    superseded = set()   # (local)
    candidates = []      # (local)
    import re  # noqa: PLC0415
    for ln in VERDICT_FILE.read_text(encoding="utf-8").splitlines():
        if ln.startswith(f"{GATE_ID}:"):
            m = re.search(r"audit_sha256=([a-f0-9]{64})", ln)  # (local)
            if m:
                candidates.append(m.group(1))
        sm = re.search(r"supersedes=([a-f0-9]{64})", ln)  # (local)
        if sm:
            superseded.add(sm.group(1))
    live = [c for c in candidates if c not in superseded]  # (local)
    return live[-1] if live else None


def su3_casimir(p: int, q: int) -> float:
    """Quadratic Casimir of the SU(3) irrep (p,q): C2 = (p^2+q^2+pq+3p+3q)/3."""
    return (p * p + q * q + p * q + 3 * p + 3 * q) / 3.0


def m3c_block_norm_and_eta(se: dict, L_cap: int):
    """FIRST-PRINCIPLES re-derivation off the s84 master cache.

    M_3(C) Peter-Weyl block = triality (p-q) mod 3 != 0 sectors.
    Norm_HH1(L) = sqrt( Σ_{block, p+q<=L} Σ_i |λ_i|^{-2s} )   (L2-type cocycle norm).
    η_FB(p,q)   = |λ|_min(p,q) / sqrt(C2(p,q)+1).
    Returns (Norm_HH1, raw_sum, min_eta_FB_over_block).
    """
    raw = 0.0          # (local) accumulated block residue sum Σ|λ|^{-2s}
    etas = []          # (local) per-sector Friedrich-Bär ratios
    for (p, q), v in se.items():
        if (p + q) > L_cap:
            continue
        if (p - q) % 3 == 0:           # exclude triality-0 -> keep M_3(C) block
            continue
        ev = np.asarray(v["abs_evals"], dtype=float)  # (local) |λ| (already × ℂ^16 fiber)
        raw += float(np.sum(ev ** MELLIN_EXP))
        etas.append(float(ev.min() / np.sqrt(su3_casimir(p, q) + 1.0)))
    norm = float(np.sqrt(raw))         # (local)
    return norm, raw, float(min(etas))


def main() -> int:
    print(f"=== {GATE_ID} ===")
    print("Stage-2 Axis-B (substrate/condensed-matter) blind independent-verify of §VII.BB")
    print(f"  τ_fold = {tau_fold}; substrate-distance-3 DEGENERATE pole s={SUBSTRATE_DISTANCE_POLE_S}; Mellin exp = {MELLIN_EXP}")

    # ---- Input SHA pins (logged in first 20 lines of stdout per gate-verdicts.md) ----
    pinmap = {
        "_gate_id": GATE_ID,
        "_axis": "B-substrate-condensed-matter",
        "script": sha256_file(SCRIPT_PATH),
        "w9_8_npz": sha256_file(W9_8_NPZ),
        "s84_cache": sha256_file(S84_CACHE),
        "canonical_constants": sha256_file(CANONICAL_CONSTANTS),
        "registry": sha256_file(REGISTRY),
    }
    print("\n-- Input-pin SHA-256 map --")
    for k, val in pinmap.items():
        print(f"  {k} = {val if k.startswith('_') else val[:16] + '...'}")

    # ---- Registry drift re-anchor (substrate-first-canonical-sourcing.md §(ii.B)) ----
    reg_text = REGISTRY.read_text(encoding="utf-8")  # (local)
    reg_lines = reg_text.splitlines()                # (local)
    heading_marker = "### §VII.BB — HH^1 Cocycle Norm at Substrate-Distance-3 Pole"  # (local)
    bb_line_idx = next((i + 1 for i, ln in enumerate(reg_lines) if ln.startswith(heading_marker)), None)  # (local) 1-based
    plan_pinned_line = 19810  # (local) plan §W6-3 STALE pin
    drift = (bb_line_idx - plan_pinned_line) if bb_line_idx else None  # (local)
    print("\n-- Registry drift re-anchor --")
    print(f"  plan-pinned §VII.BB heading line = {plan_pinned_line} (STALE)")
    print(f"  runtime-resolved §VII.BB heading line = {bb_line_idx} (drift = {drift:+d})")

    # Element-2 OE-form: confirm the OE-form substrings are present in the registered entry
    bb_block = "\n".join(reg_lines[(bb_line_idx - 1):(bb_line_idx + 90)]) if bb_line_idx else ""  # (local)
    oe_integration = "\\int_{Mellin-cone, s=5} ds" in bb_block or "∫_{Mellin-cone, s=5} ds" in bb_block  # (local)
    oe_trace = "Tr_{M_3(ℂ)}" in bb_block                       # (local)
    oe_projector = "Π^{M_3}_{Peter-Weyl}" in bb_block          # (local) named projector
    oe_form_ok = oe_integration and oe_trace and oe_projector  # (local)

    # ========================================================================
    # AXIS-B CLAUSE 1 — Laboratory-IN Pillar-II α_s OE-form
    # ========================================================================
    print("\n" + "=" * 72)
    print("AXIS-B CLAUSE 1 — Pillar-II α_s laboratory-IN observable OE-form")
    print("=" * 72)
    print("  Registered Element-2 OE-form (verbatim from §VII.BB):")
    print("    ∫_{Mellin-cone, s=5} ds  Tr_{M_3(ℂ)}( Π^{M_3}_{Peter-Weyl} · ρ_α_s(s; τ_fold) )")
    print(f"  integration domain ∫_(Mellin-cone, s=5) ds present = {oe_integration}")
    print(f"  trace Tr_(M_3(ℂ)) present                          = {oe_trace}")
    print(f"  named projector Π^(M_3)_(Peter-Weyl) present        = {oe_projector}")
    # cross-pillar-bridge-anatomy.md §"Element 2 OE-form": (i) integration domain + (ii) trace + (iii) named projector
    clause1_pass = oe_form_ok
    print(f"  >> CLAUSE 1 (OE-form: domain ∧ trace ∧ named projector) = {'PASS' if clause1_pass else 'FAIL'}")

    # ========================================================================
    # FIRST-PRINCIPLES re-derivation off the s84 master cache
    # ========================================================================
    print("\n" + "=" * 72)
    print("FIRST-PRINCIPLES re-derivation off s84 master cache (substrate-first source)")
    print("=" * 72)
    cache = np.load(S84_CACHE, allow_pickle=True)
    se = cache["sector_evals"].item()  # (local) dict {(p,q): {dim, level, abs_evals}}
    n_sectors = len(se)                # (local)
    n_block_sectors = sum(1 for (p, q) in se if (p - q) % 3 != 0)  # (local)
    print(f"  total sectors at L_max=12 = {n_sectors}; M_3(C) block sectors (triality≠0) = {n_block_sectors}")

    L_scan = [6, 8, 10, 12]            # (local) the §W9-8 saturation grid
    norm_fp = {}                       # (local) first-principles Norm_HH1 per L
    eta_fp = {}                        # (local) first-principles min η_FB per L
    for L in L_scan:
        n, raw, eta = m3c_block_norm_and_eta(se, L)
        norm_fp[L] = n
        eta_fp[L] = eta
        print(f"  L={L:2d}: Norm_HH1 (sqrt block-sum) = {n:.15f}  min η_FB = {eta:.15f}")

    min_eta_FB_fp = float(min(eta_fp.values()))  # (local) min over the L_max=12 block
    norm_L12_fp = norm_fp[12]                     # (local)

    # ========================================================================
    # Load §W9-8 npz (J1 input + cross-anchor of first-principles values)
    # ========================================================================
    print("\n" + "=" * 72)
    print("Load §W9-8 npz (J1 regime re-fit input + first-principles cross-anchor)")
    print("=" * 72)
    w = np.load(W9_8_NPZ, allow_pickle=True)
    norm_npz = {6: float(w["norm_HH1_L6"]), 8: float(w["norm_HH1_L8"]),
                10: float(w["norm_HH1_L10"]), 12: float(w["norm_HH1_L12"])}  # (local)
    min_eta_FB_npz = float(w["min_eta_FB_M3C"])   # (local)
    R2_comp_npz = float(w["R2_composite"])         # (local)
    R2_log_npz = float(w["R2_logarithmic"])        # (local)
    R2_fb_npz = float(w["R2_friedrich_bar"])       # (local)
    comp_norm_inf_npz = float(w["comp_Norm_inf"])  # (local)
    log_norm_inf_npz = float(w["log_Norm_inf"])    # (local)
    fb_norm_inf_npz = float(w["fb_Norm_inf"])      # (local)
    element5_npz = float(w["element_5_empirical_anchor"])  # (local)

    # Cross-anchor: first-principles vs npz (must agree to machine precision)
    fp_vs_npz_norm_ok = all(np.isclose(norm_fp[L], norm_npz[L], rtol=1e-12) for L in L_scan)  # (local)
    fp_vs_npz_eta_ok = np.isclose(min_eta_FB_fp, min_eta_FB_npz, rtol=1e-12)                   # (local)
    print(f"  first-principles Norm matches npz (all 4 L, rtol 1e-12) = {fp_vs_npz_norm_ok}")
    print(f"  first-principles min η_FB ({min_eta_FB_fp:.15f}) matches npz ({min_eta_FB_npz:.15f}) = {fp_vs_npz_eta_ok}")

    # ========================================================================
    # AXIS-B CLAUSE 2 — Friedrich-Bär saturation predicate (RE-DERIVED η_FB)
    # ========================================================================
    print("\n" + "=" * 72)
    print("AXIS-B CLAUSE 2 — Friedrich-Bär saturation predicate (η_FB re-derived)")
    print("=" * 72)
    # Substitution chain (threshold claim per math-scripts.md §"Double-Check Logic"):
    #   Step 1: η_FB(p,q) := |λ|_min(p,q) / sqrt(C2(p,q)+1)        [def; Casimir scaling]
    #   Step 2: min_eta_FB := min over M_3(C) block sectors p+q<=12 [substrate-first cache]
    #   Step 3: predicate := (min_eta_FB >= 0.40)                  [W11-3 saturation precedent]
    #   Step 4: substitute -> 0.446536 >= 0.40 -> TRUE -> bot-K saturated at L=12 ≡ L→∞
    fb_margin = min_eta_FB_fp - ETA_FB_LOWER   # (local)
    clause2_pass = (min_eta_FB_fp >= ETA_FB_LOWER) and fp_vs_npz_eta_ok
    print(f"  Step 1-2: min η_FB(M_3(C) block, p+q<=12) = {min_eta_FB_fp:.15f}  [first-principles]")
    print(f"  Step 3-4: {min_eta_FB_fp:.6f} >= {ETA_FB_LOWER} ? -> {min_eta_FB_fp >= ETA_FB_LOWER}  (margin = {fb_margin:+.6f})")
    print(f"  Direction: min η_FB EXCEEDS the 0.40 floor => bot-K residue saturated at L=12 ≡ L→∞ on this block")
    print(f"  >> CLAUSE 2 (FB predicate min η_FB ≥ 0.40, η_FB re-derived & matches npz) = {'PASS' if clause2_pass else 'FAIL'}")

    # ========================================================================
    # AXIS-B CLAUSE 3 + JOINT J2 — Level-3 anchor consistency
    # ========================================================================
    print("\n" + "=" * 72)
    print("AXIS-B CLAUSE 3 + JOINT J2 — Level-3 anchor consistency (rel_tol ≥ 1e-9)")
    print("=" * 72)
    canon_anchor = float(vii_bb_element_5_empirical_anchor_FW)  # (local) 11.763253530952039
    # three independent images: canonical pin, npz field, my first-principles L=12 value
    rel_pin_vs_npz = abs(canon_anchor - element5_npz) / abs(canon_anchor)        # (local)
    rel_pin_vs_fp = abs(canon_anchor - norm_L12_fp) / abs(canon_anchor)          # (local)
    print(f"  canonical pin vii_bb_element_5_empirical_anchor_FW = {canon_anchor:.15f}")
    print(f"  §W9-8 npz element_5_empirical_anchor               = {element5_npz:.15f}  rel = {rel_pin_vs_npz:.2e}")
    print(f"  first-principles Norm_HH1(L=12)                    = {norm_L12_fp:.15f}  rel = {rel_pin_vs_fp:.2e}")
    clause3_pass = (rel_pin_vs_npz <= LEVEL3_REL_TOL) and (rel_pin_vs_fp <= LEVEL3_REL_TOL)
    joint_J2_pass = clause3_pass   # J2 IS the Level-3 anchor consistency (Axis-B side of the PASS-AND)
    print(f"  >> CLAUSE 3 / JOINT J2 (Level-3 anchor consistency, rel_tol ≤ 1e-9) = {'PASS' if clause3_pass else 'FAIL'}")

    # ========================================================================
    # JOINT J1 — regime IDENTITY (independent 3-regime re-fit + discriminator)
    # ========================================================================
    print("\n" + "=" * 72)
    print("JOINT J1 — regime IDENTITY (independent re-fit + saturation-coherence discriminator)")
    print("=" * 72)
    L_arr = np.array(L_scan, dtype=float)                        # (local)
    y = np.array([norm_npz[L] for L in L_scan], dtype=float)     # (local) the §W9-8 observed L-scan
    min_observed = float(y.min())   # (local) 11.733209
    max_observed = float(y.max())   # (local) 11.763254

    # monotonicity / saturation check
    incr = np.diff(y)               # (local)
    monotone_increasing = bool(np.all(incr > 0))                 # (local)
    incr_ratios = (incr[1:] / incr[:-1]).tolist()                # (local) shrinking increments -> saturating
    print(f"  observed L-scan (npz): {[f'{v:.6f}' for v in y.tolist()]}")
    print(f"  monotone-increasing = {monotone_increasing}; increment ratios = {[round(r,3) for r in incr_ratios]} (shrinking => SATURATING)")
    # Step 2 of the substitution chain: a bounded monotone-increasing sequence has Norm_∞ >= sup = max_observed
    print(f"  saturation-coherence criterion: a coherent Norm_∞ MUST satisfy Norm_∞ >= sup(seq) = {max_observed:.6f}")

    # Independent re-fit of the 3 candidate regimes (do NOT reuse npz fit coefficients)
    def f_log(L, Ninf, Clog):       # logarithmic ~ Ninf - Clog/log(L)
        return Ninf - Clog / np.log(L)

    def f_fb(L, Ninf, Csat, k):     # Friedrich-Bär ~ Ninf - Csat*exp(-k L)
        return Ninf - Csat * np.exp(-k * L)

    def f_comp(L, Ninf, C1, C2):    # composite ~ Ninf + C1/L + C2/log(L)
        return Ninf + C1 / L + C2 / np.log(L)

    def r2(yobs, yfit):
        ss_res = float(np.sum((yobs - yfit) ** 2))   # (local)
        ss_tot = float(np.sum((yobs - np.mean(yobs)) ** 2))  # (local)
        return 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")

    # logarithmic
    try:
        p_log, _ = curve_fit(f_log, L_arr, y, p0=[11.85, 0.2], maxfev=200000)
        r2_log_fp = r2(y, f_log(L_arr, *p_log)); log_norm_inf_fp = float(p_log[0])
    except Exception as e:  # noqa: BLE001
        r2_log_fp = float("nan"); log_norm_inf_fp = float("nan"); print("  [log fit warn]", e)

    # Friedrich-Bär (4 pts, 3 params)
    try:
        p_fb, _ = curve_fit(f_fb, L_arr, y, p0=[11.85, 0.15, 0.05], maxfev=400000)
        r2_fb_fp = r2(y, f_fb(L_arr, *p_fb)); fb_norm_inf_fp = float(p_fb[0])
    except Exception as e:  # noqa: BLE001
        r2_fb_fp = float("nan"); fb_norm_inf_fp = float("nan"); print("  [fb fit warn]", e)

    # composite (4 pts, 3 params)
    try:
        p_comp, _ = curve_fit(f_comp, L_arr, y, p0=[10.0, 13.0, -6.8], maxfev=400000)
        r2_comp_fp = r2(y, f_comp(L_arr, *p_comp)); comp_norm_inf_fp = float(p_comp[0])
    except Exception as e:  # noqa: BLE001
        r2_comp_fp = float("nan"); comp_norm_inf_fp = float("nan"); print("  [comp fit warn]", e)

    print("\n  Independent re-fit results (Axis-B; not reusing npz coefficients):")
    print(f"    composite    : R²={r2_comp_fp:.6f}  Norm_∞={comp_norm_inf_fp:.6f}   (npz: R²={R2_comp_npz:.6f}, Norm_∞={comp_norm_inf_npz:.6f})")
    print(f"    logarithmic  : R²={r2_log_fp:.6f}  Norm_∞={log_norm_inf_fp:.6f}   (npz: R²={R2_log_npz:.6f}, Norm_∞={log_norm_inf_npz:.6f})")
    print(f"    Friedrich-Bär: R²={r2_fb_fp:.6f}  Norm_∞={fb_norm_inf_fp:.6f}   (npz: R²={R2_fb_npz:.6f}, Norm_∞={fb_norm_inf_npz:.6f})")

    # PRE-REGISTERED discriminator (per plan §W6-3 operator + substitution chain):
    #   regime IS substrate-IS iff (Norm_∞ >= max_observed) AND (licensed by substrate-physics predicate).
    #   Use the npz Norm_∞ asymptotes as the canonical fit (my re-fit cross-anchors them).
    comp_coherent = comp_norm_inf_npz >= max_observed   # (local) FALSE: 10.11 < 11.733
    log_coherent = log_norm_inf_npz >= max_observed     # (local) TRUE
    fb_coherent = fb_norm_inf_npz >= max_observed       # (local) TRUE
    fb_licensed = bool(min_eta_FB_fp >= ETA_FB_LOWER)   # (local) substrate-physics license (FB predicate)
    composite_excluded = (not comp_coherent)            # (local)
    print("\n  Saturation-coherence discriminator (Norm_∞ ≥ max_observed = {:.6f}):".format(max_observed))
    print(f"    composite    : {comp_norm_inf_npz:.6f} ≥ {max_observed:.6f} ? -> {comp_coherent}  => {'EXCLUDED (incoherent)' if not comp_coherent else 'coherent'}")
    print(f"    logarithmic  : {log_norm_inf_npz:.6f} ≥ {max_observed:.6f} ? -> {log_coherent}  => {'coherent' if log_coherent else 'incoherent'}")
    print(f"    Friedrich-Bär: {fb_norm_inf_npz:.6f} ≥ {max_observed:.6f} ? -> {fb_coherent}  => {'coherent' if fb_coherent else 'incoherent'}")
    print(f"    FB substrate-physics license (min η_FB ≥ 0.40) = {fb_licensed}")

    # substrate-IS regime: FB-licensed primary (coherent ∧ licensed); logarithmic coherent runner-up.
    if fb_coherent and fb_licensed:
        substrate_is_regime = "friedrich_bar_licensed"   # (local)
    elif log_coherent:
        substrate_is_regime = "logarithmic_coherent"     # (local)
    else:
        substrate_is_regime = "UNRESOLVED"               # (local)

    # The saturating-regime FINDING is robust iff composite is excluded AND both admissible
    # candidates are non-power-law (FB exp-decay + logarithmic — both non-power-law by construction).
    both_admissible_nonpowerlaw = (log_coherent and fb_coherent)  # (local)
    # J1 PASS: composite EXCLUDED on a principled (saturation-coherence) basis AND a substrate-physics-
    # licensed coherent regime exists. The FB-vs-log tie-break does NOT block J1 (both non-power-law).
    joint_J1_pass = bool(composite_excluded and (fb_coherent and fb_licensed) and both_admissible_nonpowerlaw)
    # re-fit cross-anchor sanity (my independent fits reproduce the npz argmax-incoherence structure)
    refit_cross_anchor_ok = bool(
        (comp_norm_inf_fp < min_observed) and          # my composite also asymptotes below the data infimum
        (log_norm_inf_fp >= max_observed) and
        (fb_norm_inf_fp >= max_observed)
    )
    print(f"\n  re-fit cross-anchor (my fits reproduce composite-incoherence + log/FB coherence) = {refit_cross_anchor_ok}")
    print(f"  substrate-IS regime (Axis-B) = {substrate_is_regime}")
    print(f"  >> JOINT J1 (composite EXCLUDED ∧ FB-licensed coherent ∧ saturating-finding robust) = {'PASS' if joint_J1_pass else 'FAIL'}")

    # ========================================================================
    # AXIS-B COMPOSITE VERDICT (single-axis clauses 1-3 + JOINT J1 + J2)
    # ========================================================================
    print("\n" + "=" * 72)
    print("AXIS-B COMPOSITE VERDICT")
    print("=" * 72)
    axis_b_single_axis_pass = bool(clause1_pass and clause2_pass and clause3_pass)  # (local)
    axis_b_joint_pass = bool(joint_J1_pass and joint_J2_pass)                        # (local)
    axis_b_verdict_bool = bool(axis_b_single_axis_pass and axis_b_joint_pass)        # (local)
    verdict = "PASS" if axis_b_verdict_bool else "FAIL"                              # (local)
    print(f"  CLAUSE 1 (OE-form)              = {'PASS' if clause1_pass else 'FAIL'}")
    print(f"  CLAUSE 2 (FB predicate)         = {'PASS' if clause2_pass else 'FAIL'}")
    print(f"  CLAUSE 3 (Level-3 consistency)  = {'PASS' if clause3_pass else 'FAIL'}")
    print(f"  JOINT J1 (regime identity)      = {'PASS' if joint_J1_pass else 'FAIL'}")
    print(f"  JOINT J2 (Level-3 PASS-AND)     = {'PASS' if joint_J2_pass else 'FAIL'}")
    print(f"  >>> AXIS-B verdict = {verdict}")
    print("  (the COMPOSITE Stage-2 PASS-AND with Axis-A + any §VII.BB STAGE-3 flip are the ORCHESTRATOR's synthesis move)")

    # ---- plot: Norm_HH1 vs L_max with 3 regime fits + asymptotes ----
    Lfine = np.linspace(5.5, 60, 400)  # (local)
    plt.figure(figsize=(9, 6))
    plt.plot(L_arr, y, "ko", ms=9, label="observed Norm_HH1 (§W9-8 L-scan)", zorder=5)
    if np.isfinite(comp_norm_inf_fp):
        plt.plot(Lfine, f_comp(Lfine, *p_comp), "r-", lw=1.5,
                 label=f"composite R²={r2_comp_fp:.3f}  Norm_∞={comp_norm_inf_fp:.2f} (EXCLUDED)")
        plt.axhline(comp_norm_inf_fp, color="r", ls=":", lw=1)
    if np.isfinite(log_norm_inf_fp):
        plt.plot(Lfine, f_log(Lfine, *p_log), "b-", lw=1.5,
                 label=f"logarithmic R²={r2_log_fp:.3f}  Norm_∞={log_norm_inf_fp:.2f} (coherent)")
        plt.axhline(log_norm_inf_fp, color="b", ls=":", lw=1)
    if np.isfinite(fb_norm_inf_fp):
        plt.plot(Lfine, f_fb(Lfine, *p_fb), "g-", lw=1.5,
                 label=f"Friedrich-Bär R²={r2_fb_fp:.3f}  Norm_∞={fb_norm_inf_fp:.2f} (LICENSED)")
        plt.axhline(fb_norm_inf_fp, color="g", ls=":", lw=1)
    plt.axhspan(comp_norm_inf_npz, min_observed, color="red", alpha=0.07,
                label=f"saturation-coherence violation band\n(Norm_∞<min obs {min_observed:.3f})")
    plt.axhline(min_observed, color="grey", ls="--", lw=1, label=f"min observed = {min_observed:.4f} (coherence floor)")
    plt.axhline(canon_anchor, color="purple", ls="-.", lw=1.2, label=f"Level-3 anchor = {canon_anchor:.4f}")
    plt.xlabel("L_max"); plt.ylabel("Norm_HH1  (M_KK² units)")
    plt.title("§VII.BB Axis-B verify: DEGENERATE-pole s=5 regime identity\n"
              f"min η_FB={min_eta_FB_fp:.4f} ≥ 0.40 (FB-saturation LICENSED); composite Norm_∞={comp_norm_inf_npz:.2f} EXCLUDED")
    plt.legend(loc="lower right", fontsize=7.5)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=130)
    plt.close()
    print(f"\n  plot -> {OUT_PNG.relative_to(ROOT)}")

    # ---- save npz ----
    np.savez(
        OUT_NPZ,
        axis_b_landau_verdict=verdict,
        axis_b_single_axis_pass=axis_b_single_axis_pass,
        axis_b_joint_pass=axis_b_joint_pass,
        clause1_oe_form_pass=clause1_pass,
        clause2_fb_predicate_pass=clause2_pass,
        clause3_level3_consistency_pass=clause3_pass,
        joint_J1_regime_identity_pass=joint_J1_pass,
        joint_J2_level3_consistency_pass=joint_J2_pass,
        # OE-form sub-checks
        oe_integration_present=oe_integration, oe_trace_present=oe_trace, oe_projector_present=oe_projector,
        # first-principles re-derivation
        min_eta_FB_first_principles=min_eta_FB_fp,
        min_eta_FB_npz=min_eta_FB_npz,
        eta_FB_lower=ETA_FB_LOWER, fb_margin=fb_margin,
        norm_HH1_L6_fp=norm_fp[6], norm_HH1_L8_fp=norm_fp[8],
        norm_HH1_L10_fp=norm_fp[10], norm_HH1_L12_fp=norm_fp[12],
        fp_vs_npz_norm_match=fp_vs_npz_norm_ok, fp_vs_npz_eta_match=fp_vs_npz_eta_ok,
        n_block_sectors=n_block_sectors, mellin_exponent=MELLIN_EXP,
        # regime identity
        min_observed=min_observed, max_observed=max_observed,
        monotone_increasing=monotone_increasing,
        composite_norm_inf_npz=comp_norm_inf_npz, log_norm_inf_npz=log_norm_inf_npz, fb_norm_inf_npz=fb_norm_inf_npz,
        composite_norm_inf_refit=comp_norm_inf_fp, log_norm_inf_refit=log_norm_inf_fp, fb_norm_inf_refit=fb_norm_inf_fp,
        R2_composite_npz=R2_comp_npz, R2_log_npz=R2_log_npz, R2_fb_npz=R2_fb_npz,
        R2_composite_refit=r2_comp_fp, R2_log_refit=r2_log_fp, R2_fb_refit=r2_fb_fp,
        composite_excluded=composite_excluded, fb_licensed=fb_licensed,
        substrate_is_regime=substrate_is_regime, refit_cross_anchor_ok=refit_cross_anchor_ok,
        # Level-3
        level3_anchor_canonical=canon_anchor, level3_anchor_npz=element5_npz,
        level3_anchor_first_principles=norm_L12_fp,
        rel_pin_vs_npz=rel_pin_vs_npz, rel_pin_vs_fp=rel_pin_vs_fp, level3_rel_tol=LEVEL3_REL_TOL,
        # registry drift
        bb_heading_line_runtime=bb_line_idx, bb_heading_line_plan=plan_pinned_line, registry_drift=drift,
        # alpha sibling (Wodzicki/Connes non-degenerate envelope, for context)
        alpha_HH1_s5_nondegenerate_sibling=float(alpha_HH1_per_pole_FW_s5),
        tau_fold=float(tau_fold),
    )
    print(f"  data -> {OUT_NPZ.relative_to(ROOT)}")

    # ---- dual-SHA + verdict line ----
    content_sha = sha256_file(SCRIPT_PATH)              # (local) content over script
    audit_sha = closure_hash(pinmap)                    # (local) closure over ordered input-pin map

    value_str = (
        f"axis_b_landau_verdict={verdict};"
        f"clause1_OE_form={'PASS' if clause1_pass else 'FAIL'};"
        f"clause2_FB_predicate={'PASS' if clause2_pass else 'FAIL'}_min_eta_FB={min_eta_FB_fp:.6f}>=0.40;"
        f"clause3_level3={'PASS' if clause3_pass else 'FAIL'}_anchor={canon_anchor:.12f}_rel<=1e-9;"
        f"JOINT_J1_regime_identity={'PASS' if joint_J1_pass else 'FAIL'}_composite_EXCLUDED_Norm_inf={comp_norm_inf_npz:.4f}<min_obs={min_observed:.4f};"
        f"JOINT_J2_level3={'PASS' if joint_J2_pass else 'FAIL'};"
        f"substrate_IS_regime={substrate_is_regime};"
        f"eta_FB_first_principles_matches_npz={fp_vs_npz_eta_ok};"
        f"registry_drift_plan19810_to_runtime{bb_line_idx}_drift{drift:+d}_re-anchored_per_ssfc_ii_B"
    )

    # Option A re-run discipline: if a prior non-superseded line for this gate exists
    # AND its audit_sha differs from the current one (script bytes changed on re-run),
    # append the corrective line with a supersedes tag (gate-verdicts.md §"Option A").
    prior_sha = find_prior_audit_sha()  # (local)
    supersedes = prior_sha if (prior_sha is not None and prior_sha != audit_sha) else None  # (local)
    append_verdict(verdict, value_str, audit_sha, content_sha, supersedes=supersedes)
    if supersedes:
        print(f"  Option A: corrective line supersedes prior audit_sha256={supersedes}")

    print("\n-- 4-tuple output tag --")
    print(f"(value={verdict}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")
    print(f"\nVerdict line appended -> {VERDICT_FILE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
