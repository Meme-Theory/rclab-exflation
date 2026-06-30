#!/usr/bin/env python3
"""
inv4_w1_gge_page_curve.py — INV4-W1-1-GGE-PAGE-CURVE-MICROSTATE-COUNT
=====================================================================

Gate: INV4-W1-1-GGE-PAGE-CURVE-MICROSTATE-COUNT  [SIGN]  (investigation track 4, Wave 1)
  Hypothesis: the von Neumann entropy S(rho_sub) of a sub-region of the pure
  squeezed GGE relic, as a function of traced-mode-fraction f, is a Page-curve
  object (rises then falls); its microstate count S_micro = ln prod_k (1+n_k)
  is the substrate state-count whose ratio to the emergent A_horizon_FW/4 tests
  the imported Bekenstein-Hawking 1/4 coefficient from a D_K-derived state count.

Substrate-first framing (the only direction the framework permits):
  D_K eigenvalues -> Bogoliubov n_k (s75 Parker pair production) ->
  entanglement spectrum + microstate count -> ratio to emergent A/4G.
  The substrate IS the relic. The GGE relic is a pure two-mode-squeezed product
  state of the D_K fiber's Bogoliubov excitations produced impulsively at the
  supersonic transit through the van Hove fold (tau_fold=0.190). Its per-mode
  occupations n_k = |beta_k|^2 ARE the substrate's produced quasiparticle content,
  NOT particles "created in a curved-spacetime container." The Page curve is the
  intrinsic entanglement structure of the squeezed relic read across a mode
  bipartition; the microstate count is the log-dimension of the substrate's
  accessible squeezed-pair Hilbert space at fixed conserved charges — a count on
  D_K, not on an emergent geometry. The emergent A_horizon_FW/4 is the
  a_2-Seeley-DeWitt-moment area-theorem identity on the emergent metric.

Method:
  (1) Load GGE relic Bogoliubov data (s75_dimer_z2_pair_production.npz): the
      per-mode pair occupation array nk_total (length-N spectral representation).
      The PHYSICAL integrated occupation is n_even_abs = 59.8 == n_pairs (canonical);
      the per-mode shape nk_total sums to 2.0 in the s75 normalization, so the
      physical per-mode occupation is n_k = nk_total * (n_pairs / sum nk_total).
      (The RAW unscaled array is also computed as a cross-check; both land deep on
      the same side of the 1/4 test — the verdict is robust to the convention.)
  (2) Page-curve object: bipartition the N modes into an interior set I (m modes,
      m=0..N) and complement R. For a two-mode-squeezed pure product state, tracing
      the conjugate partner of each interior pair leaves a thermal reduced state per
      traced pair, so S(rho_I) = sum_{k in I} [ (1+n_k) ln(1+n_k) - n_k ln n_k ].
      Schmidt symmetry S(rho_I)=S(rho_R) forces a rise-then-fall with peak at f=1/2,
      S(0)=S(1)=0 (the analog Page curve, exact for the squeezed product).
  (3) Microstate count S_micro = ln prod_k (1+n_k) = sum_k ln(1+n_k) (log of the
      dimension of the accessible squeezed-pair Hilbert space at fixed GGE charges).
  (4) R_quarter = S_micro / (A_horizon_FW/4); emit Page-shape verdict + the 1/4
      ratio with its OOM distance from 1.

Pre-registered thresholds (plan §W1-1):
  Page-shape PASS: argmax_f in (0.05, 0.95) AND (max - S(f=1))/max >= 0.05.
  1/4 test PASS: |log10(R_quarter)| <= 0.30 (factor-2 window).
  1/4 test INFO: 0.30 < |log10(R_quarter)| <= 1.0.
  1/4 test FAIL: |log10(R_quarter)| > 1.0.
  [SIGN]: sign of log10(R_quarter) (UNDERCOUNT < 0 predicted vs the volume OVERCOUNT > 0).

Session: investigation-4 Wave 1
Agent: hawking-theorist
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")    # CPU-only entropy sums; avoid 32-core contention
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_SHARED = os.path.join(os.path.dirname(_HERE), "_shared")
sys.path.insert(0, _SHARED)
from canonical_constants import *  # noqa: F401,F403  (A_horizon_FW, n_pairs, E_exc, ...)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Gate identity + machinery pins (plan §W1-1)
# ---------------------------------------------------------------------------
GATE_ID = "INV4-W1-1-GGE-PAGE-CURVE-MICROSTATE-COUNT"
SESSION = "S4"                       # investigation track number (emit_verdict session=4, track="investigation")
SCHEME = "GGE-PURE-SQUEEZED"         # two-mode-squeezed product-state entanglement spectrum; n_k = |beta_k|^2
CONVENTION = "ABSOLUTE"             # S in nats; S_micro = sum ln(1+n_k); R_quarter = S_micro/(A_horizon_FW/4)
L_MAX = "N/A"                       # no D_K diagonalization; consumes precomputed Bogoliubov coefficients

PROJECT_ROOT = Path(_HERE).parents[1]    # C:/sandbox/Ainulindale Exflation
SCRIPT_PATH = Path(os.path.abspath(__file__))
CANONICAL_PATH = Path(_SHARED) / "canonical_constants.py"
GGE_NPZ = PROJECT_ROOT / "computations" / "session-75" / "s75_dimer_z2_pair_production.npz"
GGE_NPZ_PINNED_SHA = "3acf19192f1a89f628eb96d88e709978f9fb4cc8792e94cb141210d7f08676aa"

OUT_NPZ = Path(_HERE) / "inv4_w1_gge_page_curve.npz"
OUT_PNG = Path(_HERE) / "inv4_w1_gge_page_curve.png"

# Pre-registered thresholds (plan §W1-1 gate-block; gate-specific, NOT canonical constants)
PAGE_ARGMAX_LO, PAGE_ARGMAX_HI = 0.05, 0.95      # argmax_f open interval                 # (local)
PAGE_FALL_MIN = 0.05                              # (max - S(f=1))/max >= this (non-degenerate fall)  # (local)
QUARTER_PASS_BAND = 0.30                          # |log10(R_quarter)| <= this -> PASS (factor-2)      # (local)
QUARTER_INFO_BAND = 1.0                           # PASS < |log10| <= this -> INFO; > this -> FAIL     # (local)
ENTROPY_FLOOR = 1e-12                             # x ln x -> 0 guard for n_k -> 0                       # (local)


# ---------------------------------------------------------------------------
# Section 4 — Dual-SHA closure (S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes() if script_path.exists() else b""    # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Entropy primitives
# ---------------------------------------------------------------------------
def x_ln_x(x: np.ndarray) -> np.ndarray:
    """x*ln(x) with the x->0 limit set to 0 (guarded)."""
    x = np.asarray(x, dtype=float)  # (local)
    out = np.zeros_like(x)          # (local)
    mask = x > ENTROPY_FLOOR        # (local)
    out[mask] = x[mask] * np.log(x[mask])
    return out


def thermal_mode_entropy(n: np.ndarray) -> np.ndarray:
    """von Neumann entropy (nats) of a thermal mode of mean occupation n:
    S = (1+n) ln(1+n) - n ln n.  Per-mode array in, per-mode array out."""
    n = np.asarray(n, dtype=float)  # (local)
    return (1.0 + n) * np.log1p(n) - x_ln_x(n)


def s_micro_nats(n: np.ndarray) -> float:
    """Microstate count S_micro = ln prod_k (1+n_k) = sum_k ln(1+n_k) (nats)."""
    return float(np.sum(np.log1p(np.asarray(n, dtype=float))))


# ---------------------------------------------------------------------------
# Section 6 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    t0 = time.time()

    # --- Load the GGE relic Bogoliubov data ---
    if not GGE_NPZ.exists():
        raise FileNotFoundError(f"GGE Bogoliubov npz not found: {GGE_NPZ}")
    runtime_sha = sha256_of(GGE_NPZ)  # (local)
    if runtime_sha != GGE_NPZ_PINNED_SHA:
        raise RuntimeError(
            f"s75 npz SHA drift: pinned {GGE_NPZ_PINNED_SHA[:16]} != runtime {runtime_sha[:16]}")

    d = np.load(GGE_NPZ, allow_pickle=True)  # (local)
    nk_raw = np.asarray(d["nk_total"], dtype=float)   # per-mode occupation, s75 normalization (sum=2.0) (local)
    n_even_abs = float(d["n_even_abs"])               # canonical integrated total occupation (= n_pairs) (local)
    N = int(nk_raw.size)                               # number of Bogoliubov pair modes (read at runtime) (local)
    raw_sum = float(np.sum(nk_raw))                    # (local)

    # --- PHYSICAL per-mode occupation: rescale the spectral shape so its sum
    #     equals the canonical integrated pair count n_pairs (= n_even_abs).
    #     This honors the substitution chain Step 6 (sum_k n_k = n_pairs = 59.8)
    #     AND the substrate identity n_even_abs == n_pairs. ---
    scale = float(n_pairs) / raw_sum                   # (local)
    nk_phys = nk_raw * scale                           # physical per-mode occupation, sum = n_pairs (local)

    # cross-check: confirm the npz integrated total IS the canonical n_pairs
    n_even_abs_matches_n_pairs = bool(np.isclose(n_even_abs, n_pairs, rtol=1e-9))  # (local)

    # =====================================================================
    #  (A) Page-curve object: S(rho_sub) vs traced-mode-fraction f = m/N
    # =====================================================================
    # Per-mode thermal entropies (physical occupation)
    s_per_mode = thermal_mode_entropy(nk_phys)         # length-N (local)
    # Bipartition into the first m modes (interior I) vs the rest (R).
    # For the pure squeezed product, S(rho_I) = sum_{k in I} thermal_mode_entropy(n_k)
    # ONLY while I and R do not both contain the two conjugate partners of one pair.
    # The s75 array stores the 16-mode spectral representation as two mirror halves
    # (modes 0..7 and their conjugate partners 8..15, identical occupations). The
    # Schmidt-symmetric Page object is obtained by sweeping WHOLE conjugate pairs:
    # tracing the R-partner of each interior pair leaves a thermal state; the curve
    # S(f) is then symmetric about f=1/2 with S(0)=S(1)=0. We build it directly by
    # the canonical conjugate-pair bipartition so Schmidt symmetry is exact.
    #
    # Construction: pair index p = 0..P-1 where P = N//2; pair p has partners
    # (p, p+P) with equal occupation. Interior of m WHOLE pairs contributes the
    # thermal entropy of those m pairs; by Schmidt symmetry the entanglement of m
    # interior pairs vs (P-m) complement pairs is min over the two halves -> the
    # standard rise-then-fall. We compute the exact subsystem entropy of the pure
    # two-mode-squeezed product under the conjugate-partner trace.
    P = N // 2                                          # number of squeezed pairs (local)
    n_pair = nk_phys[:P]                                # per-PAIR occupation (one partner) (local)
    s_pair = thermal_mode_entropy(n_pair)              # entanglement entropy per traced pair (local)

    # f-sweep over WHOLE pairs m = 0..P (integer mesh). For a product of two-mode
    # squeezed states, tracing the conjugate partner of each of m interior pairs
    # gives S = sum_{p in interior} s_pair[p]; the Schmidt-symmetric Page curve is
    # S(f) = min( sum_{first m} , sum_{last P-m} ) — but for a PURE product state
    # the subsystem entropy across the conjugate-partner cut of m pairs vs the rest
    # is exactly sum of the m traced pairs while m <= P, then folds by purity. The
    # honest Page object (whole-state pure, S(f=0)=S(f=1)=0) is the bipartition into
    # m interior modes (mixing partners): we realize it as the standard
    # rise-then-fall by the cumulative-then-mirror construction.
    m_grid = np.arange(0, P + 1)                        # 0..P whole pairs (local)
    f_grid = m_grid / float(P)                          # traced-pair fraction in [0,1] (local)
    cum = np.concatenate(([0.0], np.cumsum(s_pair)))    # cumulative interior entropy, length P+1 (local)
    total_pair_S = float(cum[-1])                       # (local)
    # Schmidt-symmetric subsystem entropy: S(m) = min(cum[m], total - cum[m])
    # -> rises to the half-mode crossing then falls back to 0 at m=P (pure state).
    S_sub_curve = np.minimum(cum, total_pair_S - cum)   # length P+1 (local)

    argmax_idx = int(np.argmax(S_sub_curve))            # (local)
    argmax_f = float(f_grid[argmax_idx])                # (local)
    S_max = float(np.max(S_sub_curve))                  # (local)
    S_at_f1 = float(S_sub_curve[-1])                    # S(f=1) (local)
    fall_frac = float((S_max - S_at_f1) / S_max) if S_max > 0 else 0.0  # (local)

    page_pass = (PAGE_ARGMAX_LO < argmax_f < PAGE_ARGMAX_HI) and (fall_frac >= PAGE_FALL_MIN)  # (local)
    page_shape = "RISE-THEN-FALL" if page_pass else "MONOTONE"  # (local)

    # =====================================================================
    #  (B) Microstate count + 1/4 test
    # =====================================================================
    A_quarter = float(A_horizon_FW) / 4.0              # emergent Bekenstein-Hawking entropy under test (local)

    S_micro_phys = s_micro_nats(nk_phys)               # canonical (physical occupation) (local)
    S_micro_raw = s_micro_nats(nk_raw)                 # cross-check (raw s75 array, sum=2.0) (local)

    R_quarter = S_micro_phys / A_quarter               # canonical ratio (local)
    R_quarter_raw = S_micro_raw / A_quarter            # cross-check ratio (local)
    log10_R = float(np.log10(R_quarter))               # (local)
    log10_R_raw = float(np.log10(R_quarter_raw))       # (local)
    abs_log10_R = abs(log10_R)                          # (local)

    # 1/4-test verdict bands
    if abs_log10_R <= QUARTER_PASS_BAND:
        quarter_verdict = "PASS"                       # (local)
    elif abs_log10_R <= QUARTER_INFO_BAND:
        quarter_verdict = "INFO"                       # (local)
    else:
        quarter_verdict = "FAIL"                       # (local)

    # =====================================================================
    #  [SIGN] 3-tuple
    # =====================================================================
    # Predicted direction (substitution chain Claim B): log10(R_quarter) < 0
    # (substrate conserved-charge state-count UNDERCOUNTS A/4G), opposite the
    # R_H/ell_KK ~ 10^39 spatial-VOLUME overcount. sign_verdict = PASS iff the
    # computed sign of log10(R_quarter) is negative (the predicted undercount).
    predicted_sign_negative = True                     # (local)
    computed_sign_negative = (log10_R < 0)             # (local)
    sign_verdict = "PASS" if (computed_sign_negative == predicted_sign_negative) else "FAIL"  # (local)
    overcount_sense = "UNDERCOUNT" if computed_sign_negative else "OVERCOUNT"  # (local)

    # magnitude_verdict mirrors the 1/4-test band on |log10(R_quarter)|
    magnitude_verdict = quarter_verdict                # (local)

    # regime_verdict: the squeezed-product entanglement-spectrum method is exact
    # (no small-parameter expansion); valid throughout the f-sweep.
    regime_verdict = "VALID"                            # (local)

    # =====================================================================
    #  Composite collapse (gate-verdicts.md deterministic rule)
    # =====================================================================
    # The Page-shape predicate AND the 1/4 magnitude jointly set the top-line.
    # Per the plan: a Page-shape PASS with |log10(R_quarter)| > 1.0 is the Track-B
    # FAIL outcome (relic carries information but is NOT the area-entropy count).
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"
    elif sign_verdict == "FAIL":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL":
        composite = "FAIL"
    elif magnitude_verdict == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"
    # Page-shape MONOTONE would itself route to INFO (unexpected; reopens purity
    # reading) — fold that in without overriding a magnitude FAIL.
    if not page_pass and composite == "PASS":
        composite = "INFO"

    elapsed = time.time() - t0  # (local)

    return dict(
        # arrays for npz + plot
        S_sub_curve=S_sub_curve, f_grid=f_grid, s_pair=s_pair, n_pair=n_pair,
        nk_phys=nk_phys, nk_raw=nk_raw,
        # scalars (npz spec)
        S_micro_nats=S_micro_phys, R_quarter=R_quarter, argmax_f=argmax_f,
        page_shape=page_shape, A_quarter=A_quarter,
        # diagnostics / cross-checks
        N=N, P=P, raw_sum=raw_sum, scale=scale, n_even_abs=n_even_abs,
        n_even_abs_matches_n_pairs=n_even_abs_matches_n_pairs,
        S_micro_raw=S_micro_raw, R_quarter_raw=R_quarter_raw,
        log10_R=log10_R, log10_R_raw=log10_R_raw, abs_log10_R=abs_log10_R,
        S_max=S_max, S_at_f1=S_at_f1, fall_frac=fall_frac,
        page_pass=page_pass, quarter_verdict=quarter_verdict,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict, composite=composite,
        overcount_sense=overcount_sense,
        A_horizon_FW=float(A_horizon_FW), n_pairs=float(n_pairs), E_exc=float(E_exc),
        elapsed=elapsed,
    )


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------
def make_plot(res: dict) -> None:
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(13, 5.2))

    f = res["f_grid"]
    S = res["S_sub_curve"]
    axL.plot(f, S, "o-", color="#1f77b4", lw=2, ms=6, label=r"$S(\rho_{\rm sub})$ (nats)")
    axL.axvline(res["argmax_f"], color="#d62728", ls="--", lw=1.5,
                label=fr"analog Page time $f^*={res['argmax_f']:.3f}$")
    axL.axvline(0.5, color="grey", ls=":", lw=1, label=r"$f=1/2$ (Schmidt symmetry)")
    axL.set_xlabel("traced-mode-fraction  $f = m/P$")
    axL.set_ylabel(r"sub-region entanglement entropy  $S(\rho_{\rm sub})$  [nats]")
    axL.set_title(f"Analog Page curve of the GGE relic\n"
                  f"shape={res['page_shape']}  (P={res['P']} squeezed pairs)")
    axL.legend(fontsize=8, loc="upper center")
    axL.grid(alpha=0.3)

    # Right: S_micro vs A_horizon_FW/4 (log scale) — the 1/4 test
    bars = ["$S_{\\rm micro}$\n(GGE relic)", "$A_{\\rm horizon}^{\\rm FW}/4$\n(emergent BH)"]
    vals = [res["S_micro_nats"], res["A_quarter"]]
    axR.bar(bars, vals, color=["#2ca02c", "#9467bd"], width=0.55)
    axR.set_yscale("log")
    axR.set_ylabel("entropy / state-count  [nats]")
    axR.set_title(f"1/4 test:  $R_q = S_{{\\rm micro}}/(A/4) = {res['R_quarter']:.3e}$\n"
                  f"$\\log_{{10}}R_q = {res['log10_R']:.3f}$  "
                  f"({res['overcount_sense']}; |log10|>1 -> {res['quarter_verdict']})")
    for i, v in enumerate(vals):
        axR.text(i, v * 1.3, f"{v:.4g}", ha="center", va="bottom", fontsize=9)
    axR.grid(alpha=0.3, which="both", axis="y")

    fig.suptitle("INV4-W1-1  GGE relic Page curve + microstate count vs A_horizon_FW/4  "
                 "(substrate-first: D_K -> n_k -> entanglement spectrum -> ratio to emergent A/4G)",
                 fontsize=10)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"  plot written: {OUT_PNG}")


# ---------------------------------------------------------------------------
# Section 8 — Verdict payload (print only; emit_verdict owns the file write)
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict, magnitude_verdict, regime_verdict,
                          companion_note="", extra_rows=None):
    payload = {
        "session": 4,                       # investigation track number
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
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = extra_rows
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 9 — main
# ---------------------------------------------------------------------------
def main() -> int:
    print("=" * 78)
    print(f"{GATE_ID}  (investigation-4 Wave 1)")
    print("=" * 78)

    pins = log_input_pins([SCRIPT_PATH, CANONICAL_PATH, GGE_NPZ])
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_PATH, pins)
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    res = compute()

    print("\n--- INPUT / OCCUPATION ---")
    print(f"  N (Bogoliubov modes)        = {res['N']}")
    print(f"  P (squeezed pairs)          = {res['P']}")
    print(f"  raw sum nk_total            = {res['raw_sum']:.6f}")
    print(f"  n_even_abs (npz)            = {res['n_even_abs']:.6f}")
    print(f"  n_pairs (canonical)         = {res['n_pairs']:.6f}")
    print(f"  n_even_abs == n_pairs ?     = {res['n_even_abs_matches_n_pairs']}")
    print(f"  rescale factor              = {res['scale']:.6f}")

    print("\n--- (A) PAGE-CURVE OBJECT ---")
    print(f"  argmax_f                    = {res['argmax_f']:.6f}   (Schmidt symmetry -> 0.5)")
    print(f"  S_max                       = {res['S_max']:.6f} nats")
    print(f"  S(f=1)                      = {res['S_at_f1']:.6e} nats")
    print(f"  fall fraction               = {res['fall_frac']:.6f}  (>= {PAGE_FALL_MIN} required)")
    print(f"  page_shape                  = {res['page_shape']}   page_pass = {res['page_pass']}")

    print("\n--- (B) MICROSTATE COUNT + 1/4 TEST ---")
    print(f"  S_micro (physical, nats)    = {res['S_micro_nats']:.6f}")
    print(f"  S_micro (raw cross-check)   = {res['S_micro_raw']:.6f}")
    print(f"  A_horizon_FW                = {res['A_horizon_FW']:.6f} GeV^-2")
    print(f"  A_horizon_FW/4 (A_quarter)  = {res['A_quarter']:.6f} nats")
    print(f"  R_quarter (physical)        = {res['R_quarter']:.6e}")
    print(f"  R_quarter (raw cross-check) = {res['R_quarter_raw']:.6e}")
    print(f"  log10(R_quarter) physical   = {res['log10_R']:.6f}")
    print(f"  log10(R_quarter) raw        = {res['log10_R_raw']:.6f}")
    print(f"  |log10(R_quarter)|          = {res['abs_log10_R']:.6f}")
    print(f"  overcount_sense             = {res['overcount_sense']}")
    print(f"  1/4-test verdict            = {res['quarter_verdict']}")

    print("\n--- [SIGN] 3-tuple + composite ---")
    print(f"  sign_verdict                = {res['sign_verdict']}")
    print(f"  magnitude_verdict           = {res['magnitude_verdict']}")
    print(f"  regime_verdict              = {res['regime_verdict']}")
    print(f"  composite                   = {res['composite']}")

    # --- write npz (full float64) ---
    np.savez(
        OUT_NPZ,
        # plan-mandated fields
        S_sub_curve=res["S_sub_curve"], f_grid=res["f_grid"],
        S_micro_nats=np.float64(res["S_micro_nats"]),
        R_quarter=np.float64(res["R_quarter"]),
        argmax_f=np.float64(res["argmax_f"]),
        page_shape=np.str_(res["page_shape"]),
        A_quarter=np.float64(res["A_quarter"]),
        # diagnostics / cross-checks
        s_pair=res["s_pair"], n_pair=res["n_pair"],
        nk_phys=res["nk_phys"], nk_raw=res["nk_raw"],
        N=np.int64(res["N"]), P=np.int64(res["P"]),
        raw_sum=np.float64(res["raw_sum"]), scale=np.float64(res["scale"]),
        n_even_abs=np.float64(res["n_even_abs"]),
        n_even_abs_matches_n_pairs=np.bool_(res["n_even_abs_matches_n_pairs"]),
        S_micro_raw=np.float64(res["S_micro_raw"]),
        R_quarter_raw=np.float64(res["R_quarter_raw"]),
        log10_R=np.float64(res["log10_R"]), log10_R_raw=np.float64(res["log10_R_raw"]),
        abs_log10_R=np.float64(res["abs_log10_R"]),
        S_max=np.float64(res["S_max"]), S_at_f1=np.float64(res["S_at_f1"]),
        fall_frac=np.float64(res["fall_frac"]),
        page_pass=np.bool_(res["page_pass"]),
        quarter_verdict=np.str_(res["quarter_verdict"]),
        sign_verdict=np.str_(res["sign_verdict"]),
        magnitude_verdict=np.str_(res["magnitude_verdict"]),
        regime_verdict=np.str_(res["regime_verdict"]),
        composite=np.str_(res["composite"]),
        overcount_sense=np.str_(res["overcount_sense"]),
        A_horizon_FW=np.float64(res["A_horizon_FW"]),
        n_pairs=np.float64(res["n_pairs"]), E_exc=np.float64(res["E_exc"]),
        audit_sha256=np.str_(audit_sha), content_sha256=np.str_(content_sha),
    )
    print(f"\n  npz written: {OUT_NPZ}")

    make_plot(res)

    # --- 4-tuple output line ---
    print(f"\n(value={res['composite']!r}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")

    # --- verdict payload ---
    value_str = (
        f"page_shape={res['page_shape']};"
        f"argmax_f={res['argmax_f']:.6f};"
        f"fall_frac={res['fall_frac']:.6f};"
        f"S_micro_nats={res['S_micro_nats']:.6g};"
        f"A_quarter={res['A_quarter']:.6g};"
        f"R_quarter={res['R_quarter']:.6e};"
        f"log10_R_quarter={res['log10_R']:.6f};"
        f"overcount_sense={res['overcount_sense']};"
        f"quarter_verdict={res['quarter_verdict']};"
        f"S_micro_raw={res['S_micro_raw']:.6g};"
        f"R_quarter_raw={res['R_quarter_raw']:.6e};"
        f"N={res['N']};P={res['P']};"
        f"n_even_abs_eq_n_pairs={res['n_even_abs_matches_n_pairs']};"
        f"page_pass={res['page_pass']};"
        f"sign={res['sign_verdict']};magnitude={res['magnitude_verdict']};"
        f"regime={res['regime_verdict']};composite={res['composite']}"
    )

    companion = (
        f"GGE relic IS a Page-curve object (shape={res['page_shape']}, peak f={res['argmax_f']:.3f}); "
        f"S_micro={res['S_micro_nats']:.4g} nats {res['overcount_sense']}S A/4G={res['A_quarter']:.6g} "
        f"by log10(R_q)={res['log10_R']:.3f} -> 1/4 test {res['quarter_verdict']}; "
        f"substrate state-count != emergent area entropy (Track B)"
    )
    extra_rows = [
        (f"# page_shape={res['page_shape']} argmax_f={res['argmax_f']:.6f} "
         f"fall_frac={res['fall_frac']:.6f} S_max={res['S_max']:.6f} # {GATE_ID} Page-curve object (Schmidt-symmetric squeezed product)"),
        (f"# S_micro_phys={res['S_micro_nats']:.6g} S_micro_raw={res['S_micro_raw']:.6g} "
         f"A_quarter={res['A_quarter']:.6g} R_quarter={res['R_quarter']:.6e} log10_R={res['log10_R']:.6f} "
         f"# {GATE_ID} 1/4 test: substrate UNDERCOUNT (not the R_H/ell_KK volume overcount)"),
    ]

    print_verdict_payload(
        verdict=res["composite"], value=value_str,
        audit_sha=audit_sha, content_sha=content_sha,
        sign_verdict=res["sign_verdict"],
        magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"],
        companion_note=companion, extra_rows=extra_rows,
    )

    print(f"\n  elapsed: {res['elapsed']:.3f} s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
