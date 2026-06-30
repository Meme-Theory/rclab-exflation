#!/usr/bin/env python3
"""
S104 W1-1 S104-VIIAM-L11-ANCHOR — deeper-truncation (L=11) Level-3-vs-Level-2
scalar inequality on the §VII.AM envelope row.
=============================================================================

Gate: S104-VIIAM-L11-ANCHOR ([SIGN])

Pre-registered threshold (strict scalar inequality, NO tolerance band):
  anchor(L=11) < env_prefac(L=11)   [equiv: ratio_prefac(11) = anchor(11)/env_prefac(11) < 1]
  emit PASS iff ratio_prefac(11) < 1 strict, under the PRE-REGISTERED prefactored
  'ii' comparator env_prefac(L) = C * L^(-alpha) (the Registry-PASS arbiter; pinned
  at plan-freeze — anti-comparator-shopping). The bare comparator
  env_bare(L) = L^(-alpha) / ratio_bare(11) is REPORTED as a cross-check ONLY and
  does NOT gate; the runtime may NOT switch to bare to flip the verdict.

This gate pushes the S103 L-indexed envelope-row comparison one truncation deeper
to L=11 under the SAME L-indexed rule the S103 W2-3 FAIL (b47ccf98, ratio 1.1578 at
L=10) left open. anchor(L) := dGamma_over_Gamma[idx(L)] with idx(L) = L - 8 over the
pinned domain L in [8,9,10,11]; so anchor(11) = dGamma_over_Gamma[3].

Upstream-consistency sentinel: re-derive anchor(L=10), env_prefac(L=10) and
reproduce the S103 ratio_prefac(10)=1.157832 / ratio_bare(10)=2.156107 within 1e-6.
If the sentinel does NOT reproduce, an input-pin drift is signalled -> INFO
(routes to input-SHA re-verification, NOT a substrate verdict).

Inputs (SHA-256 pinned at runtime):
  - computations/session-101/s101_viiam_alpha_envelope_pin.npz  (dGamma_over_Gamma
      array [L in 8..11], alpha, intercept -> C source)
  - computations/session-102/s102_w2_viiam_l2l3_recon.npz        (prefactored
      comparator C, alpha; comparator_used = prefactored(ii) arbiter)
  - computations/session-103/s103_viiam_lindexed_anchor.npz      (L-indexed rule +
      L=10 baseline sentinel ratio_prefac/ratio_bare)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<ratio_prefac(11) + PASS/FAIL>, scheme=cross-pillar-bridge-anatomy-
   Registry-PASS-criterion-Lindexed-anchor,
   convention=envelope-comparator-PRE-REGISTERED-prefactored-ii/alpha=4.6905/
   anchor=Lindexed-dGamma/L=11, L_max=11)

Classification: GEOMETRIC (the §VII.AM observable is a fabric-side effacement
quantity — the spectral-action zeroth-moment effacement ratio dGamma/Gamma — at
truncation L on the finite spectral triple (A_K^{<=L}, H_K^{<=L}, D_K^{<=L})).

METHODOLOGY
-----------
D_K eigenvalues -> the spectral-action zeroth-moment effacement ratio dGamma/Gamma
(the impedance-mismatch leakage of the acoustic white-hole transit; Gamma_eff =
0.9997 canonical at L_ref=12) -> the Level-3 empirical anchor at truncation L. The
Level-2 envelope C*L^(-alpha) is the substrate's algebraic convergence rate of that
finite-L moment toward its continuum (laboratory-IN) image. The gate asks whether,
one truncation deeper (L=10 -> L=11), the substrate-IS effacement anchor has
descended INSIDE its own convergence envelope. Between L=10 and L=11 the anchor
decays dGamma_over_Gamma: 4.39680436e-05 -> 2.10947710e-05 (factor 0.4798), while
the prefactored envelope decays 3.79744506e-05 -> 2.42849792e-05 (factor 0.6395);
the anchor decays FASTER than the L^(-alpha=4.6905) envelope, so the ratio crosses
from 1.1578 (outside, L=10) to 0.8686 (inside, L=11). The Level-1 cohomology-class
identity is regulator-invariant and L-independent (STAGE-3-PERMANENT); this gate
touches ONLY the Level-2/Level-3 numerical ladder of the envelope row.

DISCIPLINE
----------
- `from canonical_constants import *`
- scalar arithmetic on pinned float64 (matrices < 100x100) -> CPU; OMP_NUM_THREADS=8.
- SHA-256 of all input files logged in the first 20 lines of stdout.
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema).
- Gate verdict emitted via the `emit_verdict` knowledge-MCP tool (race-safe);
  this script PRINTS the payload (print_verdict_payload), never writes the verdict
  file directly.
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_shared"))
from canonical_constants import *  # noqa: F401,F403

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
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S104"                                                   # (local)
GATE_ID = "S104-VIIAM-L11-ANCHOR"                                  # (local)
SCHEME = "cross-pillar-bridge-anatomy-Registry-PASS-criterion-Lindexed-anchor"  # (local)
CONVENTION = (
    "envelope-comparator-PRE-REGISTERED-prefactored-ii/alpha=4.6905/"
    "anchor=Lindexed-dGamma/L=11"
)                                                                 # (local)
L_MAX = 11                                                         # (local) deeper-truncation slice

# The deeper truncation slice + the sentinel slice.
L_TARGET = 11                                                     # (local) the gate
L_SENTINEL = 10                                                   # (local) upstream-consistency reproduction
L_DOMAIN_BASE = 8                                                 # (local) idx(L) = L - 8 over L in [8,9,10,11]

# Sentinel reproduction targets (S103-VIIAM-LINDEXED-ANCHOR, audit b47ccf98).
SENTINEL_RATIO_PREFAC_10 = 1.157832                              # (local) target ratio_prefac(10)
SENTINEL_RATIO_BARE_10 = 2.156107                               # (local) target ratio_bare(10)
SENTINEL_TOL = 1e-6                                              # (local) upstream-consistency tolerance

# Frozen-input file references
S101_NPZ = COMPUTATIONS_DIR / "session-101" / "s101_viiam_alpha_envelope_pin.npz"
S102_NPZ = COMPUTATIONS_DIR / "session-102" / "s102_w2_viiam_l2l3_recon.npz"
S103_NPZ = COMPUTATIONS_DIR / "session-103" / "s103_viiam_lindexed_anchor.npz"

OUT_NPZ = SESSION_DIR / "s104_viiam_l11_anchor.npz"
OUT_PNG = SESSION_DIR / "s104_viiam_l11_anchor.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    S101_NPZ,
    S102_NPZ,
    S103_NPZ,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY)
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
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path, canonical_path: Path, pins: dict[str, str]
) -> tuple[str, str]:
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
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
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
# Section 5 — Compute
# ---------------------------------------------------------------------------

def compute() -> dict:
    """Scalar inequality anchor(11) < env_prefac(11) on pinned float64."""
    d101 = np.load(S101_NPZ, allow_pickle=True)  # (local)
    d102 = np.load(S102_NPZ, allow_pickle=True)  # (local)
    d103 = np.load(S103_NPZ, allow_pickle=True)  # (local)

    # --- Definition 1: anchor(L) := dGamma_over_Gamma[idx(L)], idx(L) = L - 8 ---
    #   dGamma_over_Gamma = [9.70015970e-05, 6.90093678e-05, 4.39680436e-05, 2.10947710e-05]
    #   over L in [8,9,10,11]; idx(L=10)=2, idx(L=11)=3.
    dGamma = np.asarray(d101["dGamma_over_Gamma"], dtype=np.float64)  # (local)
    # cross-check the S103 copy is bit-identical (both consume the s101 pin)
    dGamma_s103 = np.asarray(d103["dGamma_over_Gamma"], dtype=np.float64)  # (local)
    dGamma_copies_match = bool(np.array_equal(dGamma, dGamma_s103))  # (local)

    def idx(L: int) -> int:
        return L - L_DOMAIN_BASE  # (local)

    def anchor(L: int) -> float:
        return float(dGamma[idx(L)])  # (local)

    # --- Definition 2: env_prefac(L) := C * L^(-alpha), C = exp(intercept) ---
    alpha = float(d102["alpha"])          # (local) 4.690533158119443
    intercept = float(d101["intercept"])  # (local) 0.6217547500863554
    C = float(np.exp(intercept))          # (local) 1.8621928596201978

    # cross-check C against the s102 stored C (comparator source)
    C_s102 = float(d102["C"])             # (local) 1.86219286
    alpha_s101 = float(d101["alpha"])     # (local) 4.69053316
    C_cross_ok = bool(abs(C - C_s102) < 1e-9)             # (local)
    alpha_cross_ok = bool(abs(alpha - alpha_s101) < 1e-12)  # (local)
    # comparator arbiter declaration: s102 carries `comparator_decision`,
    # s103 carries `comparator_used`; both name the prefactored(ii) arbiter.
    comparator_s102 = str(d102["comparator_decision"]) if "comparator_decision" in d102.files else ""  # (local)
    comparator_s103 = str(d103["comparator_used"]) if "comparator_used" in d103.files else ""  # (local)
    comparator_used = comparator_s103 or comparator_s102  # (local)
    prefactored_arbiter_confirmed = bool(("prefactored(ii)" in comparator_used)
                                         or ("comparator-arbiter=prefactored" in comparator_used))  # (local)

    def env_prefac(L: int) -> float:
        return C * (float(L) ** (-alpha))  # (local) prefactored 'ii' arbiter

    def env_bare(L: int) -> float:
        return float(L) ** (-alpha)        # (local) bare cross-check ONLY

    # ============================================================
    #   L = 11 — the gate (prefactored arbiter)
    # ============================================================
    a11 = anchor(L_TARGET)            # (local) 2.10947710e-05
    ep11 = env_prefac(L_TARGET)       # (local) prefactored comparator
    eb11 = env_bare(L_TARGET)         # (local) bare comparator (REPORTED-NOT-GATING)
    pow11 = float(L_TARGET) ** (-alpha)  # (local) 11^(-alpha)
    ratio_prefac_11 = a11 / ep11      # (local) PASS iff < 1  (the arbiter)
    ratio_bare_11 = a11 / eb11        # (local) REPORTED-NOT-GATING cross-check
    pass_prefac_11 = bool(a11 < ep11)            # (local) == ratio_prefac_11 < 1
    pass_bare_11 = bool(a11 < eb11)              # (local) cross-check only

    # ============================================================
    #   L = 10 — upstream-consistency sentinel (S103 reproduction)
    # ============================================================
    a10 = anchor(L_SENTINEL)          # (local) 4.39680436e-05
    ep10 = env_prefac(L_SENTINEL)     # (local) 3.79744506e-05
    eb10 = env_bare(L_SENTINEL)       # (local) 2.03923296e-05
    ratio_prefac_10 = a10 / ep10      # (local) target 1.157832
    ratio_bare_10 = a10 / eb10        # (local) target 2.156107

    # cross-check the rederived L=10 ratios against the S103 stored values
    s103_ratio_prefac = float(d103["ratio_prefac"])  # (local) 1.15783225
    s103_ratio_bare = float(d103["ratio_bare"])      # (local) 2.15610695
    s103_env_prefac = float(d103["env_prefac"])      # (local) 3.79744506e-05
    s103_anchor_L10 = float(d103["anchor_L10"])      # (local) 4.39680436e-05
    s103_idx_L10 = int(d103["idx_L10"])              # (local) 2

    # sentinel deviations vs the PLAN targets (the upstream-consistency assertion)
    dev_ratio_prefac_10 = abs(ratio_prefac_10 - SENTINEL_RATIO_PREFAC_10)  # (local)
    dev_ratio_bare_10 = abs(ratio_bare_10 - SENTINEL_RATIO_BARE_10)        # (local)
    sentinel_prefac_ok = bool(dev_ratio_prefac_10 < SENTINEL_TOL)          # (local)
    sentinel_bare_ok = bool(dev_ratio_bare_10 < SENTINEL_TOL)             # (local)
    sentinel_ok = bool(sentinel_prefac_ok and sentinel_bare_ok)           # (local)

    # bit-exact reproduction vs the S103 stored ratios (much tighter than 1e-6)
    bitexact_prefac_10 = abs(ratio_prefac_10 - s103_ratio_prefac)  # (local)
    bitexact_bare_10 = abs(ratio_bare_10 - s103_ratio_bare)        # (local)
    idx_L10_ok = bool(s103_idx_L10 == idx(L_SENTINEL))            # (local)

    # mechanism: decay factors L=10 -> L=11
    anchor_decay_10_to_11 = a11 / a10        # (local) 0.47977...
    env_prefac_decay_10_to_11 = ep11 / ep10  # (local) 0.63950...

    # --- Verdict logic ---
    # INFO is ONLY for sentinel non-reproduction (input-pin drift). Otherwise the
    # gate adjudicates the strict inequality under the prefactored arbiter.
    if not sentinel_ok:
        verdict = "INFO"  # (local) sentinel drift -> input-SHA re-verification
        sign_v, mag_v, regime_v = "N/A", "INFO", "VALID"  # (local)
    elif pass_prefac_11:
        verdict = "PASS"  # (local) anchor(11) < env_prefac(11) strict
        sign_v, mag_v, regime_v = "PASS", "PASS", "VALID"  # (local)
    else:
        verdict = "FAIL"  # (local) anchor(11) >= env_prefac(11)
        sign_v, mag_v, regime_v = "FAIL", "FAIL", "VALID"  # (local)

    return {
        "value": float(ratio_prefac_11),
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": regime_v,
        "verdict": verdict,
        # --- L=11 gate quantities ---
        "anchor_11": a11,
        "env_prefac_11": ep11,
        "env_bare_11": eb11,
        "pow11_neg_alpha": pow11,
        "ratio_prefac_11": float(ratio_prefac_11),
        "ratio_bare_11": float(ratio_bare_11),
        "pass_prefac_11": pass_prefac_11,
        "pass_bare_11": pass_bare_11,
        "signed_margin_11": float(a11 - ep11),  # < 0 => PASS (anchor inside envelope)
        # --- comparator parameters ---
        "alpha": alpha,
        "intercept": intercept,
        "C": C,
        "C_s102": C_s102,
        "alpha_s101": alpha_s101,
        "C_cross_ok": C_cross_ok,
        "alpha_cross_ok": alpha_cross_ok,
        "comparator_used": comparator_used,
        "prefactored_arbiter_confirmed": prefactored_arbiter_confirmed,
        # --- L=10 sentinel ---
        "anchor_10": a10,
        "env_prefac_10": ep10,
        "env_bare_10": eb10,
        "ratio_prefac_10": float(ratio_prefac_10),
        "ratio_bare_10": float(ratio_bare_10),
        "sentinel_ratio_prefac_target": SENTINEL_RATIO_PREFAC_10,
        "sentinel_ratio_bare_target": SENTINEL_RATIO_BARE_10,
        "dev_ratio_prefac_10": float(dev_ratio_prefac_10),
        "dev_ratio_bare_10": float(dev_ratio_bare_10),
        "sentinel_prefac_ok": sentinel_prefac_ok,
        "sentinel_bare_ok": sentinel_bare_ok,
        "sentinel_ok": sentinel_ok,
        # --- bit-exact reproduction vs S103 stored ---
        "s103_ratio_prefac": s103_ratio_prefac,
        "s103_ratio_bare": s103_ratio_bare,
        "s103_env_prefac": s103_env_prefac,
        "s103_anchor_L10": s103_anchor_L10,
        "s103_idx_L10": s103_idx_L10,
        "bitexact_prefac_10": float(bitexact_prefac_10),
        "bitexact_bare_10": float(bitexact_bare_10),
        "idx_L10_ok": idx_L10_ok,
        # --- mechanism ---
        "anchor_decay_10_to_11": float(anchor_decay_10_to_11),
        "env_prefac_decay_10_to_11": float(env_prefac_decay_10_to_11),
        # --- provenance ---
        "dGamma_over_Gamma": dGamma,
        "dGamma_copies_match": dGamma_copies_match,
        "idx_target_11": idx(L_TARGET),
        "idx_sentinel_10": idx(L_SENTINEL),
        "L_target": L_TARGET,
        "L_sentinel": L_SENTINEL,
        "gamma_effacement_canonical": float(Gamma_effacement),
    }


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------

def make_plot(r: dict) -> None:
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))

    # Panel 1 — anchor(L) vs prefactored & bare envelopes over L in [8..11]
    Ls = np.array([8, 9, 10, 11], dtype=float)  # (local)
    dGamma = np.asarray(r["dGamma_over_Gamma"], dtype=float)  # (local)
    alpha = r["alpha"]  # (local)
    C = r["C"]          # (local)
    env_pre = C * Ls ** (-alpha)  # (local)
    env_bar = Ls ** (-alpha)      # (local)

    ax[0].semilogy(Ls, dGamma, "o-", color="navy", lw=2, ms=7,
                   label="anchor(L) = dGamma/Gamma")
    ax[0].semilogy(Ls, env_pre, "s--", color="crimson", lw=2, ms=6,
                   label=r"env_prefac(L) = $C\cdot L^{-\alpha}$ (ARBITER)")
    ax[0].semilogy(Ls, env_bar, "^:", color="gray", lw=1.5, ms=6,
                   label=r"env_bare(L) = $L^{-\alpha}$ (cross-check only)")
    # mark the L=10 (outside) and L=11 (inside) prefactored crossing
    ax[0].annotate("L=10: ratio_prefac=1.1578 (OUTSIDE)",
                   xy=(10, dGamma[2]), xytext=(8.6, dGamma[2] * 2.4),
                   fontsize=8, color="darkred",
                   arrowprops=dict(arrowstyle="->", color="darkred", lw=1))
    ax[0].annotate("L=11: ratio_prefac=0.8686 (INSIDE)",
                   xy=(11, dGamma[3]), xytext=(9.2, dGamma[3] * 0.45),
                   fontsize=8, color="darkgreen",
                   arrowprops=dict(arrowstyle="->", color="darkgreen", lw=1))
    ax[0].set_xlabel("truncation L")
    ax[0].set_ylabel("Level-3 anchor / Level-2 envelope")
    ax[0].set_xticks([8, 9, 10, 11])
    ax[0].set_title("§VII.AM envelope row: anchor enters prefactored envelope at L=11")
    ax[0].legend(fontsize=7, loc="upper right")
    ax[0].grid(True, which="both", alpha=0.3)

    # Panel 2 — the ratio_prefac(L) crossing below 1 + bare cross-check
    rp = dGamma / env_pre  # (local)
    rb = dGamma / env_bar  # (local)
    ax[1].plot(Ls, rp, "o-", color="crimson", lw=2, ms=7,
               label="ratio_prefac(L) (ARBITER)")
    ax[1].plot(Ls, rb, "^:", color="gray", lw=1.5, ms=6,
               label="ratio_bare(L) (cross-check only)")
    ax[1].axhline(1.0, color="k", lw=1.2, ls="-",
                  label="PASS boundary (ratio = 1)")
    ax[1].annotate(
        f"L=11 ARBITER: ratio_prefac = {r['ratio_prefac_11']:.6f} < 1  => PASS\n"
        f"L=11 bare (NOT gating): ratio_bare = {r['ratio_bare_11']:.6f} > 1\n"
        f"anchor decays x{r['anchor_decay_10_to_11']:.4f} vs env x{r['env_prefac_decay_10_to_11']:.4f}",
        xy=(0.03, 0.06), xycoords="axes fraction", fontsize=8,
        bbox=dict(boxstyle="round", fc="honeydew", ec="seagreen"),
    )
    ax[1].set_xlabel("truncation L")
    ax[1].set_ylabel("ratio = anchor / envelope")
    ax[1].set_xticks([8, 9, 10, 11])
    ax[1].set_title(
        f"ratio_prefac crosses below 1 at L=11  "
        f"(verdict {r['verdict']}, prefactored arbiter)"
    )
    ax[1].legend(fontsize=7, loc="upper right")
    ax[1].grid(True, alpha=0.3)

    fig.suptitle(
        "S104-VIIAM-L11-ANCHOR — Level-3 anchor descends INSIDE the prefactored "
        "Level-2 envelope at the deeper L=11 truncation (PASS)",
        fontsize=11,
    )
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"  plot -> {OUT_PNG.name}")


# ---------------------------------------------------------------------------
# Section 7 — Verdict payload helper
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
    sign_verdict: str | None = None,
    magnitude_verdict: str | None = None,
    regime_verdict: str | None = None,
    companion_note: str = "",
    extra_rows: list[str] | None = None,
) -> dict:
    payload: dict = {
        "session": SESSION.lstrip("Ss"),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if not (sign_verdict is None and magnitude_verdict is None
            and regime_verdict is None):
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()

    print("  === Definitions (pinned floats) ===")
    print(f"  alpha          = {r['alpha']!r}")
    print(f"  C = exp({r['intercept']:.16f}) = {r['C']!r}")
    print(f"  dGamma/Gamma   = {np.asarray(r['dGamma_over_Gamma'])}  (L in [8,9,10,11])")
    print(f"  idx(L=11)      = {r['idx_target_11']} ; idx(L=10) = {r['idx_sentinel_10']}")
    print()
    print("  === L=11 (the gate; prefactored arbiter) ===")
    print(f"  anchor(11)        = {r['anchor_11']:.8e}")
    print(f"  11^(-alpha)       = {r['pow11_neg_alpha']:.8e}")
    print(f"  env_prefac(11)    = {r['env_prefac_11']:.8e}  (ARBITER = C*11^-alpha)")
    print(f"  env_bare(11)      = {r['env_bare_11']:.8e}  (cross-check only)")
    print(f"  ratio_prefac(11)  = {r['ratio_prefac_11']:.6f}  < 1 => {r['pass_prefac_11']}  (ARBITER)")
    print(f"  ratio_bare(11)    = {r['ratio_bare_11']:.6f}  < 1 => {r['pass_bare_11']}  (REPORTED-NOT-GATING)")
    print(f"  signed_margin(11) = {r['signed_margin_11']:.8e}  (anchor - env_prefac; <0 => INSIDE)")
    print()
    print("  === L=10 upstream-consistency sentinel ===")
    print(f"  anchor(10)        = {r['anchor_10']:.8e}  (S103 anchor_L10 {r['s103_anchor_L10']:.8e})")
    print(f"  env_prefac(10)    = {r['env_prefac_10']:.8e}  (S103 env_prefac {r['s103_env_prefac']:.8e})")
    print(f"  ratio_prefac(10)  = {r['ratio_prefac_10']:.6f}  target {r['sentinel_ratio_prefac_target']:.6f}  dev {r['dev_ratio_prefac_10']:.3e}  ok={r['sentinel_prefac_ok']}")
    print(f"  ratio_bare(10)    = {r['ratio_bare_10']:.6f}  target {r['sentinel_ratio_bare_target']:.6f}  dev {r['dev_ratio_bare_10']:.3e}  ok={r['sentinel_bare_ok']}")
    print(f"  idx_L10 (S103=2)  = {r['s103_idx_L10']} ok={r['idx_L10_ok']}")
    print(f"  bit-exact vs S103: prefac resid {r['bitexact_prefac_10']:.3e}  bare resid {r['bitexact_bare_10']:.3e}")
    print(f"  sentinel_ok       = {r['sentinel_ok']}")
    print()
    print("  === mechanism (decay factors L=10 -> L=11) ===")
    print(f"  anchor decay      = {r['anchor_decay_10_to_11']:.6f}  (FASTER)")
    print(f"  env_prefac decay  = {r['env_prefac_decay_10_to_11']:.6f}  (slower)")
    print(f"  => ratio crosses below 1; comparator_used = {r['comparator_used']}")
    print(f"  prefactored_arbiter_confirmed = {r['prefactored_arbiter_confirmed']}  (anti-comparator-shopping)")
    print(f"  C_cross_ok={r['C_cross_ok']} alpha_cross_ok={r['alpha_cross_ok']} dGamma_copies_match={r['dGamma_copies_match']}")
    print()

    # --- Hard cross-check assertions (sentinels + provenance) ---
    # These are pre-registered consistency anchors. Their failure is a SHA/pin
    # drift, NOT a substrate FAIL — but if the sentinel reproduces (it must, given
    # the pinned npz), the verdict logic in compute() already routes any drift to
    # INFO. We additionally hard-assert the bit-exact reproduction against the
    # S103 stored ratios (tolerance far tighter than the 1e-6 plan sentinel).
    assert r["idx_L10_ok"], (
        f"idx(L=10) mismatch: this={r['idx_sentinel_10']} S103={r['s103_idx_L10']}"
    )
    assert r["dGamma_copies_match"], (
        "s101 and s103 dGamma_over_Gamma copies are not bit-identical"
    )
    assert r["C_cross_ok"] and r["alpha_cross_ok"], (
        "comparator C/alpha do not cross-reproduce across s101/s102"
    )
    assert r["prefactored_arbiter_confirmed"], (
        "upstream npz provenance does not confirm the prefactored(ii) comparator as "
        "the Registry-PASS arbiter (anti-comparator-shopping guard)"
    )
    assert r["bitexact_prefac_10"] < 1e-6, (
        f"ratio_prefac(10) does not reproduce S103 stored within 1e-6 "
        f"(resid {r['bitexact_prefac_10']:.3e})"
    )
    assert r["bitexact_bare_10"] < 1e-6, (
        f"ratio_bare(10) does not reproduce S103 stored within 1e-6 "
        f"(resid {r['bitexact_bare_10']:.3e})"
    )

    np.savez(OUT_NPZ, **{k: v for k, v in r.items()})
    print(f"  data -> {OUT_NPZ.name}")
    make_plot(r)
    print()

    tag = emit_4tuple(
        f"ratio_prefac(11)={r['ratio_prefac_11']:.6f};{'PASS' if r['pass_prefac_11'] else 'FAIL'}",
        SCHEME, CONVENTION, L_MAX,
    )
    print(tag)

    # Build the value payload (no single-quote chars — the tool wraps value='...').
    value_payload = (
        f"anchor(11)={r['anchor_11']:.6e}_vs_env_prefac(11)={r['env_prefac_11']:.6e}@Lmax11;"
        f"ratio_prefac(11)={r['ratio_prefac_11']:.6f}(<1=>{'PASS' if r['pass_prefac_11'] else 'FAIL'});"
        f"env_bare(11)={r['env_bare_11']:.6e}(xcheck:ratio_bare(11)={r['ratio_bare_11']:.6f}>1=REPORTED-NOT-GATING);"
        f"alpha={r['alpha']:.6f};C=exp({r['intercept']:.6f})={r['C']:.6f};"
        f"Lindex(L=11)=idx3(of_dGamma_len4_at_L[8,9,10,11]);"
        f"sentinel_L10:ratio_prefac(10)={r['ratio_prefac_10']:.6f}(tgt1.157832,dev{r['dev_ratio_prefac_10']:.2e}),"
        f"ratio_bare(10)={r['ratio_bare_10']:.6f}(tgt2.156107,dev{r['dev_ratio_bare_10']:.2e}),sentinel_ok={r['sentinel_ok']};"
        f"registry_pass_prefac={r['pass_prefac_11']};registry_pass_bare={r['pass_bare_11']};"
        f"theorem-STRUCTURE=STAGE-3-PERMANENT(Level-1-out-of-scope)"
    )

    extra_rows = [
        "# regulator_pin=N/A (effacement zeroth-moment ratio dGamma/Gamma, NOT a Seeley-DeWitt a_n citation)",
        f"# comparator-arbiter=prefactored-ii(C*L^-alpha); bare(L^-alpha) REPORTED-NOT-GATING "
        f"(anti-comparator-shopping per S104-context Wave1 item-1.3): ratio_bare(11)={r['ratio_bare_11']:.6f}>1 does NOT flip verdict",
        f"# sentinel-L10 reproduces S103 b47ccf98: ratio_prefac(10)={r['ratio_prefac_10']:.6f} "
        f"(S103 {r['s103_ratio_prefac']:.6f}, resid {r['bitexact_prefac_10']:.2e}); "
        f"ratio_bare(10)={r['ratio_bare_10']:.6f} (S103 {r['s103_ratio_bare']:.6f}, resid {r['bitexact_bare_10']:.2e})",
        f"# mechanism: anchor decays x{r['anchor_decay_10_to_11']:.4f} FASTER than env_prefac x{r['env_prefac_decay_10_to_11']:.4f} "
        f"across L=10->11 => ratio crosses 1.1578(out)->0.8686(in)",
    ]

    print_verdict_payload(
        r["verdict"], value_payload, audit_sha, content_sha,
        sign_verdict=r["sign_verdict"],
        magnitude_verdict=r["magnitude_verdict"],
        regime_verdict=r["regime_verdict"],
        extra_rows=extra_rows,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {r['verdict']} (wall {wall:.1f}s) ===")
    return 0  # verdict is data; exit 0 on a successful run regardless of PASS/FAIL/INFO


if __name__ == "__main__":
    sys.exit(main())
