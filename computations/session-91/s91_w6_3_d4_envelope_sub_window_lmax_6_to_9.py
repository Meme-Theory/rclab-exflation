#!/usr/bin/env python3
"""
S91 W6-3: S91-D4-ENVELOPE-SUB-WINDOW-L_MAX-6-TO-9 (T2.60 / W-6 CF-9)
======================================================================

Gate: S91-D4-ENVELOPE-SUB-WINDOW-L_MAX-6-TO-9 ([AUDIT])

CHEAP precursor 4-point log-log regression of δ_n_s on EXISTING S90 W8
FWD-C1 L_max-scan data at the pre-anchor monotone-descent sub-window
L_max ∈ {6, 7, 8, 9}. No new spectrum compute.

Per plan §W6-3 (lines 523-737), this gate isolates the pre-anchor regime
(per W8 WP §W8-7(l) lines 1326-1337) from the post-anchor
c_sub_corrected M_Pl_eff² anti-symmetry artifact. The empirical α_sub
at this sub-window IS the substrate-IS pre-asymptotic finite-L envelope
slope at d=4 substrate-distance-1 pole `s=3`.

Sage-Q rational arithmetic cross-checked against numpy.polyfit at
machine epsilon per mnemonic-vs-exact discipline
(math-scripts.md §"Mnemonic-vs-exact ratio discipline" RULE-3).

Verdict bands per workshop CF-9 spec (s90-w6-d4-envelope-identity.md L1321):
  PASS-A-partial: α_sub > 2.5 (Reading A pre-asymptotic confirmation)
  INFO:           α_sub ∈ [2.0, 2.5] (intermediate)
  FAIL:           α_sub ≈ 1.9 (Reading B partial confirmation)
                  OR R² < 0.95 (regression-quality failure)

Substitution chain (plan §10 pre-registered direction): per CM-1995
§III.4 finite-L correction δ_n_s(L) = L^{-3}·(C_0 + C_1·L^{-1} + ...),
the log-log slope at finite L equals -3 + (-C_1/C_0)·L^{-1} + O(L^{-2}).
PASS direction is α_sub > α_full_window=1.929 toward asymptotic α=3
(Reading A; C_1 < 0 over-performance regime per W-6 EV1, §VII.AF.1.OP-PROJ).
FAIL direction is α_sub ≈ 1.929 persistent across sub-windows
(Reading B; C_1 > 0 under-performance regime, §VII.AU.OP-PROJ).

Substrate framing: the sub-window L ∈ {6, 7, 8, 9} IS the substrate's
pre-asymptotic finite-L manifestation at the d=4 substrate-distance-1
pole `s=3` — not a slice OF some enveloping L-space container. The
C_1 subleading coefficient's sign IS a substrate-IS structural
signature.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import math
import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "computations" / "_shared"))
sys.path.insert(0, str(ROOT / "computations"))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import kappa_2_substrate_FW  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402


# ============================ Gate-block constants ============================
GATE_ID = "S91-D4-ENVELOPE-SUB-WINDOW-L_MAX-6-TO-9"
SCHEME = "log-log-regression-existing-S90-W8-FWD-C1-pre-anchor-sub-window"
CONVENTION = "Mellin-class-pre-asymptotic-sub-window-CACHE-PROJECTION"
L_MAX_TAG = 9  # (local) — gate-pre-registered L_max output tag per plan §6 L617
PROJECT_ROOT = ROOT
SHARED_DIR = ROOT / "computations" / "_shared"
SESSION_91_DIR = ROOT / "computations" / "session-91"
SESSION_90_DIR = ROOT / "computations" / "session-90"
VERDICT_TXT = SESSION_91_DIR / "s91_gate_verdicts.txt"
OUT_NPZ = SESSION_91_DIR / "s91_w6_3_d4_envelope_sub_window_lmax_6_to_9.npz"
OUT_PNG = SESSION_91_DIR / "s91_w6_3_d4_envelope_sub_window_lmax_6_to_9.png"

# Pinned input files (per plan §7)
INPUT_FILES = [
    SESSION_90_DIR / "s90_w8_fwd_c1_lmax_scan_parameterized_slope_a_canonical.npz",
    SHARED_DIR / "canonical_constants.py",
    ROOT / "sessions" / "session-90" / "workshops" / "s90-w6-d4-envelope-identity.md",
    ROOT / "sessions" / "session-90" / "session-90-w8-workingpaper.md",
]


# ============================ SHA helpers ============================
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    """audit_sha = SHA(script_bytes || canonical_bytes || sorted-pinmap-JSON);
       content_sha = SHA(script_bytes)."""
    script_bytes = script_path.read_bytes()
    canonical_bytes = canonical_path.read_bytes()
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()
    content = hashlib.sha256(script_bytes).hexdigest()
    return audit, content


# ============================ Section 5 — Sage-Q exact regression ============================
def regress_sage_q_exact(L_vals: list[int], delta_vals: list[float]
                         ) -> tuple[Fraction, Fraction, Fraction]:
    """4-point log-log regression in exact rational arithmetic
    on Fraction-quantized log values.

    Returns (slope_Q, intercept_Q, r_sq_Q) as Fraction approximations.

    Note: log values are intrinsically transcendental; we quantize at
    machine-double precision (Fraction.from_float on math.log) so the
    Sage-Q cross-check is bit-precise against numpy on the SAME quantized
    inputs. Any deviation from numpy.polyfit at machine epsilon would
    indicate a regression-arithmetic discrepancy (NOT a transcendence
    error; both paths consume the SAME float64 log inputs).
    """
    # Quantize log(L) and log(δ_n_s) as Fractions from their float64 values
    log_L_Q = [Fraction.from_float(math.log(float(L))) for L in L_vals]   # (local)
    log_d_Q = [Fraction.from_float(math.log(float(d))) for d in delta_vals]  # (local)

    n_Q = Fraction(len(L_vals))                                            # (local)
    sum_x = sum(log_L_Q, Fraction(0))                                      # (local)
    sum_y = sum(log_d_Q, Fraction(0))                                      # (local)
    sum_xy = sum((x * y for x, y in zip(log_L_Q, log_d_Q)), Fraction(0))   # (local)
    sum_xx = sum((x * x for x in log_L_Q), Fraction(0))                    # (local)

    # Linear regression closed form
    denom = n_Q * sum_xx - sum_x * sum_x                                   # (local)
    slope_Q = (n_Q * sum_xy - sum_x * sum_y) / denom                       # (local)
    intercept_Q = (sum_y - slope_Q * sum_x) / n_Q                          # (local)

    # R^2 (exact)
    mean_y = sum_y / n_Q                                                   # (local)
    ss_res = sum(((y - (slope_Q * x + intercept_Q)) ** 2
                  for x, y in zip(log_L_Q, log_d_Q)), Fraction(0))         # (local)
    ss_tot = sum(((y - mean_y) ** 2 for y in log_d_Q), Fraction(0))        # (local)
    r_sq_Q = Fraction(1) - ss_res / ss_tot                                 # (local)
    return slope_Q, intercept_Q, r_sq_Q


# ============================ Section 6 — Compute ============================
def compute() -> dict:
    # ---------------------------------------------------------------------------
    # Step 0: pre-anchor sub-window input (per plan §7 + W8 WP §W8-7(l) L1326-1337)
    # ---------------------------------------------------------------------------
    L_sub = np.array([6, 7, 8, 9], dtype=np.int64)                          # (local)
    delta_n_s_sub = np.array([3.103e-02, 2.545e-02, 1.960e-02, 1.112e-02],  # (local)
                             dtype=np.float64)

    # ---------------------------------------------------------------------------
    # Sanity: load existing S90 W8 FWD-C1 npz to verify the input file is
    # well-formed and SHA-pinable (per plan §7); the script does NOT recompute
    # the L_max scan — the δ_n_s pre-anchor sub-window values are pinned per
    # W8 WP §W8-7(l) lines 1326-1337 already.
    # ---------------------------------------------------------------------------
    fwd_c1_path = (SESSION_90_DIR
                   / "s90_w8_fwd_c1_lmax_scan_parameterized_slope_a_canonical.npz")
    fwd_c1_npz = np.load(fwd_c1_path, allow_pickle=True)
    fwd_c1_keys_present = sorted(list(fwd_c1_npz.files))                   # (local)
    print(f"S90 W8 FWD-C1 npz keys present: {fwd_c1_keys_present[:8]}"
          f"{'...' if len(fwd_c1_keys_present) > 8 else ''}")

    # ---------------------------------------------------------------------------
    # Step 1: take log-log of δ_n_s vs L (per plan §6 line 579-580)
    # ---------------------------------------------------------------------------
    log_L = np.log(L_sub.astype(np.float64))                               # (local)
    log_dns = np.log(delta_n_s_sub)                                        # (local)

    # ---------------------------------------------------------------------------
    # Step 2: 4-point linear regression via numpy.polyfit (per plan §6 L582-584)
    # ---------------------------------------------------------------------------
    slope_np, intercept_np = np.polyfit(log_L, log_dns, 1)
    alpha_sub_np = -float(slope_np)                                        # (local) sub-window α

    # ---------------------------------------------------------------------------
    # Sage-Q exact rational cross-check (mnemonic-vs-exact discipline per
    # math-scripts.md §"Mnemonic-vs-exact ratio discipline" RULE-3 + plan §6
    # line 575-576)
    # ---------------------------------------------------------------------------
    slope_Q, intercept_Q, r_sq_Q = regress_sage_q_exact(
        L_sub.tolist(), delta_n_s_sub.tolist())
    alpha_sub_Q = -float(slope_Q)                                          # (local)

    # ---------------------------------------------------------------------------
    # Step 3: R^2 goodness of fit (numpy path)
    # ---------------------------------------------------------------------------
    ss_res_np = float(np.sum((log_dns - (slope_np * log_L + intercept_np))**2))  # (local)
    ss_tot_np = float(np.sum((log_dns - log_dns.mean())**2))               # (local)
    r_squared_np = 1.0 - ss_res_np / ss_tot_np                             # (local)
    r_squared_Q_float = float(r_sq_Q)                                      # (local)

    # ---------------------------------------------------------------------------
    # Machine-epsilon cross-check Sage-Q vs numpy
    # ---------------------------------------------------------------------------
    alpha_dev = abs(alpha_sub_Q - alpha_sub_np)                            # (local)
    r2_dev = abs(r_squared_Q_float - r_squared_np)                         # (local)
    intercept_dev = abs(float(intercept_Q) - float(intercept_np))          # (local)
    print(f"\nSage-Q vs numpy cross-check (must be at machine epsilon):")
    print(f"  |α_sub_Q - α_sub_np| = {alpha_dev:.3e}")
    print(f"  |intercept_Q - intercept_np| = {intercept_dev:.3e}")
    print(f"  |R²_Q - R²_np|        = {r2_dev:.3e}")
    sageQ_numpy_machine_eps = (alpha_dev < 1e-12 and r2_dev < 1e-12)       # (local)

    # ---------------------------------------------------------------------------
    # Step 4: Verdict assignment per workshop CF-9 spec (plan §6 L592-603, §9)
    # ---------------------------------------------------------------------------
    if r_squared_np < 0.95:
        verdict = "FAIL"
        band_tag = "FAIL_R2"
    elif alpha_sub_np > 2.5:
        verdict = "PASS"
        band_tag = "PASS_A_partial"
    elif 2.0 <= alpha_sub_np <= 2.5:
        verdict = "INFO"
        band_tag = "INFO_intermediate"
    else:  # alpha_sub_np < 2.0
        verdict = "FAIL"
        band_tag = "FAIL_Reading_B_partial"

    # ---------------------------------------------------------------------------
    # Step 5: 3-tuple companion annotation per S87 schema-v2 (plan §6 L606-609)
    # ---------------------------------------------------------------------------
    # sign_verdict: PASS direction is "positive decay" (α_sub > 1.0); plan §10
    # Step 4 pre-registers PASS direction as α_sub > α_full_window=1.929 toward
    # asymptotic α=3. We use the cumulative direction band (α_sub > 1.0
    # for "positive decay sign" per plan §6 line 606; this is the wider band
    # the plan's snippet pre-registers as the sign axis).
    sign_v = "PASS" if alpha_sub_np > 1.0 else "FAIL"                      # (local)
    mag_v = ("PASS" if abs(alpha_sub_np - 3.0) < 0.5
             else "INFO" if abs(alpha_sub_np - 3.0) < 1.0
             else "FAIL")                                                   # (local)
    # regime_verdict pre-registered MARGINAL (plan §6 L609; sub-window L ≤ 9
    # is pre-asymptotic boundary layer; Friedrich-Bär saturation at L ≥ 12).
    regime_v = "MARGINAL"

    # ---------------------------------------------------------------------------
    # Substitution-chain direction read (per plan §10 Step 5)
    # ---------------------------------------------------------------------------
    alpha_full_window = 1.929                                              # (local) — CF-65 anchor
    sub_window_vs_full = alpha_sub_np - alpha_full_window                  # (local)
    reading_A_direction = sub_window_vs_full > 0                           # (local)

    return {
        "L_sub": L_sub,
        "delta_n_s_sub": delta_n_s_sub,
        "log_L": log_L,
        "log_dns": log_dns,
        # numpy regression
        "slope_np": float(slope_np),
        "intercept_np": float(intercept_np),
        "alpha_sub_np": alpha_sub_np,
        "r_squared_np": r_squared_np,
        # Sage-Q exact regression
        "slope_Q_str": str(slope_Q),
        "intercept_Q_str": str(intercept_Q),
        "alpha_sub_Q": alpha_sub_Q,
        "r_squared_Q": r_squared_Q_float,
        # cross-check
        "alpha_dev_Q_vs_np": alpha_dev,
        "r2_dev_Q_vs_np": r2_dev,
        "sageQ_numpy_machine_eps": sageQ_numpy_machine_eps,
        # verdict
        "verdict": verdict,
        "band_tag": band_tag,
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": regime_v,
        # substitution-chain direction
        "alpha_full_window": alpha_full_window,
        "sub_window_minus_full": sub_window_vs_full,
        "reading_A_direction": reading_A_direction,
        # provenance
        "kappa_2_substrate_FW": kappa_2_substrate_FW,
        "fwd_c1_keys_present_first_8": fwd_c1_keys_present[:8],
    }


# ============================ Section 7 — Plot ============================
def make_plot(r: dict) -> None:
    fig, ax = plt.subplots(1, 1, figsize=(8.0, 6.0), dpi=110)

    L_sub = r["L_sub"]                                                     # (local)
    delta = r["delta_n_s_sub"]                                             # (local)
    log_L = r["log_L"]                                                     # (local)
    log_dns = r["log_dns"]                                                 # (local)
    slope = r["slope_np"]                                                  # (local)
    intercept = r["intercept_np"]                                          # (local)

    # Scatter of (log L, log δ_n_s)
    ax.scatter(log_L, log_dns, s=72, color="C0", zorder=3,
               label=f"S90 W8 FWD-C1 pre-anchor sub-window data\n"
                     f"L ∈ {{6, 7, 8, 9}}; δ_n_s = "
                     f"[{delta[0]:.3e}, {delta[1]:.3e}, "
                     f"{delta[2]:.3e}, {delta[3]:.3e}]")

    # Best-fit line over the sub-window range
    x_line = np.linspace(log_L.min() - 0.05, log_L.max() + 0.05, 50)
    y_line = slope * x_line + intercept
    ax.plot(x_line, y_line, "-", color="C1", lw=1.8,
            label=f"4-point fit: α_sub = {r['alpha_sub_np']:.4f} "
                  f"(R² = {r['r_squared_np']:.4f})")

    # Reference α = 3 (Reading A asymptotic; CM-1995 §III.4 L^{-3})
    y_ref_3 = -3.0 * (x_line - log_L.mean()) + log_dns.mean()
    ax.plot(x_line, y_ref_3, ":", color="C2", lw=1.4,
            label="Reading A reference: α = 3 (CM-1995 §III.4 asymptotic L^{-3})")

    # Reference α = 1.929 (CF-65 full-window α; Reading B persistent)
    y_ref_19 = -1.929 * (x_line - log_L.mean()) + log_dns.mean()
    ax.plot(x_line, y_ref_19, "--", color="C3", lw=1.4,
            label="Reading B reference: α = 1.929 (CF-65 full-window α)")

    # PASS band ceiling (α = 2.5)
    y_ref_25 = -2.5 * (x_line - log_L.mean()) + log_dns.mean()
    ax.plot(x_line, y_ref_25, "-.", color="C4", lw=1.2,
            label="PASS-A-partial threshold: α = 2.5")

    title_fontsize = 10  # (local) — matplotlib display size
    ax.set_xlabel("log(L_max)", fontsize=11)
    ax.set_ylabel("log(δ_n_s)", fontsize=11)
    ax.set_title(
        f"{GATE_ID}\n"
        f"verdict = {r['verdict']} ({r['band_tag']}); "
        f"α_sub = {r['alpha_sub_np']:.4f}; α_full = 1.929; "
        f"sub−full = {r['sub_window_minus_full']:+.4f}",
        fontsize=title_fontsize,
    )
    ax.legend(loc="upper right", fontsize=8.5, framealpha=0.92)
    ax.grid(True, alpha=0.32)
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=110)
    plt.close(fig)
    print(f"plot written: {OUT_PNG}")


# ============================ Section 8 — Verdict emission ============================
def append_verdict(gate_id: str, verdict: str, value: str,
                   scheme: str, convention: str, L_max,
                   input_pin_map: dict,
                   schema_v2_annotation: dict,
                   script_path: Path, canonical_path: Path) -> tuple[str, str]:
    """Emit the canonical verdict line + dual-SHA companion comment row +
    schema-v2 3-tuple annotation companion row per
    `.claude/rules/gate-verdicts.md §"S87+ canonical form"`.

    audit_sha256 is computed as the closure hash over
        script_bytes || canonical_bytes || sorted(input_pin_map)JSON
    so that any change to the producing script, the canonical constants
    module, or the pinned input file SHAs yields a new audit_sha256
    (enforcing sig_5 uniqueness by construction).

    Returns (audit_sha, content_sha) for downstream diagnostics.
    """
    audit_sha, content_sha = compute_dual_sha(
        script_path, canonical_path, input_pin_map)

    canonical_line = (
        f"{gate_id}: {verdict} -- value='{value}' "
        f"scheme={scheme} convention={convention} L_max={L_max} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    dual_sha_row = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {gate_id} dual-SHA companion row (W9a-99 split)\n"
    )
    three_tuple_row = (
        f"# sign_verdict={schema_v2_annotation['sign_verdict']} "
        f"magnitude_verdict={schema_v2_annotation['magnitude_verdict']} "
        f"regime_verdict={schema_v2_annotation['regime_verdict']} "
        f"# {gate_id} 3-tuple annotation (S87 schema-v2)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(dual_sha_row)
        fp.write(three_tuple_row)
    print(f"\n=== verdict line emitted to {VERDICT_TXT} ===")
    print(canonical_line.rstrip())
    print(dual_sha_row.rstrip())
    print(three_tuple_row.rstrip())
    return audit_sha, content_sha


# ============================ Section 9 — main ============================
def main() -> int:
    pins = log_input_pins(INPUT_FILES)
    r = compute()
    make_plot(r)

    # ---------------------------------------------------------------------------
    # Save .npz per plan §6 lines 629-633 (keys: L_sub, delta_n_s_sub,
    # alpha_sub, r_squared, verdict, sign_verdict, magnitude_verdict,
    # regime_verdict) + diagnostic keys
    # ---------------------------------------------------------------------------
    save_dict = {
        "L_sub": r["L_sub"],
        "delta_n_s_sub": r["delta_n_s_sub"],
        "alpha_sub": np.array(r["alpha_sub_np"]),
        "r_squared": np.array(r["r_squared_np"]),
        "verdict": np.array(r["verdict"]),
        "sign_verdict": np.array(r["sign_verdict"]),
        "magnitude_verdict": np.array(r["magnitude_verdict"]),
        "regime_verdict": np.array(r["regime_verdict"]),
        # diagnostic / cross-check
        "alpha_sub_np": np.array(r["alpha_sub_np"]),
        "alpha_sub_Q": np.array(r["alpha_sub_Q"]),
        "slope_np": np.array(r["slope_np"]),
        "intercept_np": np.array(r["intercept_np"]),
        "r_squared_Q": np.array(r["r_squared_Q"]),
        "alpha_dev_Q_vs_np": np.array(r["alpha_dev_Q_vs_np"]),
        "r2_dev_Q_vs_np": np.array(r["r2_dev_Q_vs_np"]),
        "sageQ_numpy_machine_eps": np.array(r["sageQ_numpy_machine_eps"]),
        "band_tag": np.array(r["band_tag"]),
        "alpha_full_window": np.array(r["alpha_full_window"]),
        "sub_window_minus_full": np.array(r["sub_window_minus_full"]),
        "reading_A_direction": np.array(r["reading_A_direction"]),
        "kappa_2_substrate_FW": np.array(r["kappa_2_substrate_FW"]),
    }
    np.savez(OUT_NPZ, **save_dict)
    print(f"npz written: {OUT_NPZ}")

    # ---------------------------------------------------------------------------
    # value field per plan §8 expected output 4-tuple
    # ---------------------------------------------------------------------------
    value_field = (
        f"alpha_sub={r['alpha_sub_np']:.4f}"
        f"_R2={r['r_squared_np']:.4f}"
        f"_{r['band_tag']};"
        f"alpha_full_window=1.9290;"
        f"sub_minus_full={r['sub_window_minus_full']:+.4f};"
        f"slope_np={r['slope_np']:.6e};"
        f"intercept_np={r['intercept_np']:.6e};"
        f"sageQ_numpy_machine_eps={bool(r['sageQ_numpy_machine_eps'])};"
        f"alpha_dev_Q_vs_np={r['alpha_dev_Q_vs_np']:.3e};"
        f"r2_dev_Q_vs_np={r['r2_dev_Q_vs_np']:.3e};"
        f"reading_A_direction={bool(r['reading_A_direction'])}"
    )

    # 4-tuple output tag per gate-verdicts.md §"Pre-Registration Protocol"
    print(f"\n4-tuple: (value='{value_field[:80]}...', scheme={SCHEME}, "
          f"convention={CONVENTION[:60]}..., L_max={L_MAX_TAG})")

    # Build input_pin_map for closure SHA computation (includes all 4 INPUT_FILES
    # pinned per plan §7 + canonical_constants.py)
    input_pin_map = {
        rel: sha for rel, sha in pins.items()
    }
    input_pin_map["canonical_constants_kappa_2_substrate_FW"] = (
        f"{kappa_2_substrate_FW:.18e}")

    schema_v2_annotation = {
        "sign_verdict": r["sign_verdict"],
        "magnitude_verdict": r["magnitude_verdict"],
        "regime_verdict": r["regime_verdict"],
    }

    audit_sha, content_sha = append_verdict(
        gate_id=GATE_ID,
        verdict=r["verdict"],
        value=value_field,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX_TAG,
        input_pin_map=input_pin_map,
        schema_v2_annotation=schema_v2_annotation,
        script_path=Path(__file__),
        canonical_path=SHARED_DIR / "canonical_constants.py",
    )

    # Diagnostic summary
    print(f"\n=== {GATE_ID} summary ===")
    print(f"  L_sub:                {list(r['L_sub'])}")
    print(f"  δ_n_s:                {list(r['delta_n_s_sub'])}")
    print(f"  α_sub (numpy):        {r['alpha_sub_np']:.6f}")
    print(f"  α_sub (Sage-Q):       {r['alpha_sub_Q']:.6f}")
    print(f"  R² (numpy):           {r['r_squared_np']:.6f}")
    print(f"  R² (Sage-Q):          {r['r_squared_Q']:.6f}")
    print(f"  α_full_window (CF-65):{r['alpha_full_window']:.4f}")
    print(f"  α_sub - α_full:       {r['sub_window_minus_full']:+.4f}")
    print(f"  Reading A direction:  {bool(r['reading_A_direction'])}  "
          f"(PASS direction: sub > full)")
    print(f"  verdict:              {r['verdict']}  ({r['band_tag']})")
    print(f"  3-tuple:              sign={r['sign_verdict']} "
          f"mag={r['magnitude_verdict']} regime={r['regime_verdict']}")
    print(f"  audit_sha256:         {audit_sha}")
    print(f"  content_sha256:       {content_sha}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
