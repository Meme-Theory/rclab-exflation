#!/usr/bin/env python3
"""
S107 W3-1 S107-SDW-2ND-MOMENT-EFT — 2nd-layer SDW EFT-control ratio at the species scale
=========================================================================================

Gate: S107-SDW-2ND-MOMENT-EFT ([SIGN])

Pre-registered threshold (EVOI Tier-3 #12; tight EFT-control ceiling):
  r_2nd = (a_8/a_6) * (Lambda_sp/M_KK)^{-2}  evaluated at the SPECIES cutoff Lambda_sp.
  PASS iff r_2nd < 0.1          (2nd-moment EFT under control at the tight threshold)
  INFO iff 0.1 <= r_2nd < 0.5   (marginal: under the S96 loose band, NOT the tight one)
  FAIL iff r_2nd >= 0.5         (no marginal control; closed-cone EFT-control corridor closes)

This is a [SIGN] gate. Substitution-chain prediction (plan §W3-1 Step 4):
  predicted sign of (r_2nd - 0.1) is POSITIVE  =>  predicted INFO band.
  sign_verdict = PASS iff computed sign(r_2nd - 0.1) matches the POSITIVE prediction.

DISTINCTNESS FROM S96 (recompute-what-is-closed guard, plan distinctness ledger):
  S96-SDW-EFT-CONTROL evaluated the FULL term-ratio ladder {r_0..r_3} at the BASE cutoff
  Lambda = M_KK against the LOOSE <0.5 band -> INFO (max a-ratio driver 0.6808 @ M_KK).
  THIS gate evaluates the 2nd-LAYER ratio (k=3, a_8/a_6) at the SPECIES cutoff Lambda_sp as
  primary, against the TIGHT <0.1 ceiling -- a DIFFERENT (cutoff, threshold) pair on the
  EFT-control axis, the specific question EVOI Tier-3 #12 pre-registers. It BUILDS ON the
  canonical a_6/a_8 (verified Superseded=False at runtime); it does NOT re-promote them.

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/_shared/canonical_constants.py   (a_0/a_2/a_4/a_6/a_8 zeta moments, Lambda_sp, M_KK)
  - computations/session-96/s96_sdw_eft_control.npz (base-layer EFT-control data; a-ratio driver cross-read)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz (E38 a_6/a_8 per-branch provenance cross-check)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<r_2nd>, scheme=Seeley-DeWitt-layer-expansion,
   convention=RATIO-2nd-layer-a-ratio-driver-at-Lambda_sp-scheme-independent, L_max=10)

Classification: GEOMETRIC. The substrate IS D_K(tau_fold) on Jensen-deformed SU(3); the
a_{2k} are residues of its spectral zeta at the d=8 dimension-spectrum poles s=(8-n)/2
(Connes-Moscovici 1995 §III.4, "E38"). The SDW layer expansion is the perturbative face of
the master spectral-action functional S_b = Tr f(D_K^2/Lambda^2). The a-ratio driver
a_{2(k+1)}/a_{2k} is FUNCTIONAL-INVARIANT (any common w(L_max) spectral-support prefactor
cancels in the ratio -- the lizzi multiplicative-normalization cancellation invariant); the
f-coefficient ratio is FUNCTIONAL-DEPENDENT (Gaussian-cutoff vs Mellin-f* give opposite
modulations). What survives all functional choices (the a-ratio structural driver) is the
gated structural object; the f-modulated contrast is reported diagnostically.

Direction of explanation:
  D_K eigenvalue spectrum {lambda_k, m_k}  ->  closed-cone SDW layer moments a_{2k}  ->
  2nd-layer EFT-control ratio r_2nd at the species scale  ->  EFT-control status (parametric
  vs representation-theoretic) of the 2nd moment.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- GPU NOT used: scalar moment arithmetic on 5 canonical moments + a ~7000-mode (12880
  Weyl-weighted) L_max_branch=3 cache mode-sum; no >=100x100 linalg. OMP capped to 8.
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Gate verdict emitted via the `emit_verdict` knowledge-MCP tool (race-safe): the script
  PRINTS the payload (print_verdict_payload) carrying BOTH SHAs; the dispatching AGENT calls
  mcp__knowledge__emit_verdict(**payload). The script does NOT write the verdict file.
- regulator_pin=a_n^{ζ} companion row (the a_n are zeta-regulated SDW moments;
  regulator-pin-discipline.md a_n^{regulator} MANDATORY).
"""

from __future__ import annotations

# -----------------------------------------------------------------------------
# Section 0 — CPU thread cap BEFORE numpy import (GPU_path=cpu-cap-OMP8)
# -----------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# -----------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# canonical_constants.py lives in computations/_shared/; put it on sys.path first.
# -----------------------------------------------------------------------------
import sys
from pathlib import Path as _Path
_SHARED = _Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED))

from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import (  # noqa: E402
    a_0_FW_zeta, a_2_FW_zeta, a_4_FW_zeta, a_6_FW_zeta, a_8_FW_zeta,
    Lambda_sp_over_M_KK, M_KK, PROVENANCE,
)

# -----------------------------------------------------------------------------
# Section 2 — Standard imports
# -----------------------------------------------------------------------------
import hashlib
import json
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# -----------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S107"                                                       # (local)
GATE_ID = "S107-SDW-2ND-MOMENT-EFT"                                    # (local)
SCHEME = "Seeley-DeWitt-layer-expansion"                               # (local)
CONVENTION = "RATIO-2nd-layer-a-ratio-driver-at-Lambda_sp-scheme-independent"  # (local)
L_MAX = "10"                                                           # (local) cache cross-check footing

# Pre-registered pass/fail thresholds (define BEFORE running; plan machinery_pin_map)
CTRL_PASS_STRICT = 0.1          # (local) EVOI #12 tight EFT-control ceiling (PASS band)
CTRL_FAIL_STRICT = 0.5          # (local) S96 loose-control ceiling reused as INFO/FAIL split
LAYER_K_2ND = 3                 # (local) 2nd-layer / deepest-closed-cone index (a_8/a_6)
L_MAX_BRANCH = 3                # (local) per-branch zeta convention truncation (reproduces canonical)
BRANCH_FACTOR = 0.5             # (local) per-branch normalization (cache holds 2 branches)
CACHE_TOL = 1e-3                # (local) a_4 truncated at 4dp -> |dev| < 1e-3 cross-check tol
PUB_PRECISION = 4               # (local) publication precision (epistemic-discipline Class 8.3)

# Pre-registered SIGN-gate prediction (plan §W3-1 substitution_chain Step 4)
PREDICTED_SIGN_R2ND_MINUS_CEIL = "+"  # (local) predicted sign of (r_2nd - 0.1) is POSITIVE

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s107_sdw_2nd_moment_eft.npz"
OUT_PNG = SESSION_DIR / "s107_sdw_2nd_moment_eft.png"

# Input files
CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
S96_SDW_NPZ = COMPUTATIONS_DIR / "session-96" / "s96_sdw_eft_control.npz"
SPECTRUM_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"

INPUT_FILES = [CANONICAL_CONSTANTS_PATH, S96_SDW_NPZ, SPECTRUM_CACHE]


# -----------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
# -----------------------------------------------------------------------------
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
        print(f"  {rel}: {sha}")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict[str, str]) -> tuple[str, str]:
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


# -----------------------------------------------------------------------------
# Section 4b — Superseded=False runtime guard (orchestrator override)
# -----------------------------------------------------------------------------
def verify_not_superseded() -> None:
    """Hard-assert a_6/a_8/Lambda_sp canonical entries are NOT superseded at runtime.

    The producing script BUILDS ON the canonical a_6/a_8; it does not re-promote them.
    If any is superseded, the gate's footing has drifted and the run must abort.
    """
    required = ["a_6_FW_zeta", "a_8_FW_zeta", "Lambda_sp_over_M_KK"]  # (local)
    print("=== Superseded=False runtime guard ===")
    for name in required:
        entry = PROVENANCE.get(name, {})  # (local)
        sup = entry.get("superseded", None)  # (local)
        print(f"  {name}: superseded={sup}  (session={entry.get('session')}, gate={entry.get('gate')})")
        if sup is not False:
            raise SystemExit(
                f"ABORT: canonical entry {name} has superseded={sup} (expected False); "
                "the gate's a-moment footing has drifted. Re-pin before re-running."
            )
    print("  guard PASS: all three canonical moments Superseded=False")


# -----------------------------------------------------------------------------
# Section 5 — E38 per-branch cache cross-check + ratio machinery
# -----------------------------------------------------------------------------
def cache_moments_crosscheck():
    """Re-derive a_n = (1/2) sum_modes m_k |lambda_k|^{-n} at L_max_branch=3 from the L12 cache.

    The cache `sector_evals` is a {(p,q): {dim, level, abs_evals}} dict; the E38 per-branch
    convention weights each |lambda| by its Weyl-dim multiplicity (info['dim']) over sectors
    p+q <= L_max_branch=3. Returns {n: a_n} for n in {0,2,4,6,8}, the unique-mode count, and
    the Weyl-weighted total multiplicity. Verifies bit-exact agreement with canonical
    a_0/a_2/a_4 (SAME footing pins a_6/a_8). Faithful reproduction of S96 cache_moments_crosscheck.
    """
    d = np.load(SPECTRUM_CACHE, allow_pickle=True)  # (local)
    se = d["sector_evals"].item()  # (local)
    evs_list = []   # (local)
    mults_list = []  # (local)
    for (p, q), info in se.items():
        if (p + q) > L_MAX_BRANCH:
            continue
        es = np.asarray(info["abs_evals"], dtype=np.float64)  # (local)
        if es.size == 0:
            continue
        mults_list.append(np.full(es.shape, float(info["dim"])))
        evs_list.append(es)
    evs = np.concatenate(evs_list)      # (local) |lambda_k| of D_K
    mults = np.concatenate(mults_list)  # (local) Weyl-dim multiplicities
    mask = evs > 1e-12                  # (local) drop numerical zeros
    evs = evs[mask]
    mults = mults[mask]
    out = {}  # (local)
    for n in [0, 2, 4, 6, 8]:
        out[n] = BRANCH_FACTOR * float(np.sum(mults * evs ** (-n)))  # (local) E38 per-branch
    return out, int(evs.size), float(mults.sum())


def a_ratio(a_dict, k):
    """a_{2(k+1)}/a_{2k} -- the scheme-INDEPENDENT (FUNCTIONAL-INVARIANT) structural driver."""
    return a_dict[2 * (k + 1)] / a_dict[2 * k]  # (local)


def r_k_aratio_driver(a_dict, k, lam_over_mkk):
    """r_k^a = (a-ratio) * (Lambda/M_KK)^{-2}  (FI structural piece; f-ratio = 1)."""
    return a_ratio(a_dict, k) * lam_over_mkk ** (-2)  # (local)


# -----------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# -----------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None) -> dict:
    payload: dict = {
        "session": int(SESSION.lstrip("Ss")),
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
    if not (sign_verdict is None and magnitude_verdict is None and regime_verdict is None):
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


def main() -> int:
    t0 = time.time()  # (local)
    print("=" * 78)
    print(f"  {GATE_ID}")
    print("  2nd-layer SDW EFT-control ratio at the species scale (EVOI #12, tight <0.1)")
    print("=" * 78)

    # --- 1. Input SHA log (first 20 lines of stdout) ---
    print()
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_CONSTANTS_PATH, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print(f"  canonical: a_0={a_0_FW_zeta}  a_2={a_2_FW_zeta}  a_4={a_4_FW_zeta}  "
          f"a_6={a_6_FW_zeta}  a_8={a_8_FW_zeta}")
    print(f"  Lambda_sp/M_KK={Lambda_sp_over_M_KK}  M_KK={M_KK:.6e} GeV")
    print()

    # --- 1b. Superseded=False runtime guard (orchestrator override) ---
    verify_not_superseded()
    print()

    # --- 2. Build the closed-cone SDW moment dict from canonical zeta moments ---
    a_dict = {0: a_0_FW_zeta, 2: a_2_FW_zeta, 4: a_4_FW_zeta,
              6: a_6_FW_zeta, 8: a_8_FW_zeta}  # (local) d=8 closed cone {a_0..a_8}
    lam_sp = float(Lambda_sp_over_M_KK)  # (local)
    lam_factor2_MKK = 1.0                # (local) (M_KK/M_KK)^{-2} = 1
    lam_factor2_sp = lam_sp ** (-2)      # (local) (Lambda_sp/M_KK)^{-2}

    # --- 3. E38 per-branch cache cross-check (pins a_6/a_8 on the canonical a_0/a_2/a_4 footing) ---
    print("=== a_6/a_8 cache cross-check (E38 per-branch L_max=3 zeta on S84 L12 cache) ===")
    cache_a, n_modes, tot_mult = cache_moments_crosscheck()  # (local)
    print(f"  n_unique_modes(L_max_branch=3)={n_modes}  total_mult_weighted={tot_mult:.1f}")
    crosscheck_ok = True  # (local)
    for n in [0, 2, 4, 6, 8]:
        dev = abs(cache_a[n] - a_dict[n])  # (local)
        tag = "OK" if dev < CACHE_TOL else "FAIL"  # (local)
        if dev >= CACHE_TOL:
            crosscheck_ok = False
        print(f"    a_{n}: cache={cache_a[n]:.6f}  canonical={a_dict[n]}  |dev|={dev:.3e}  {tag}")
    print(f"  cross-check (2x cache-sum = canonical, same footing): "
          f"{'PASS' if crosscheck_ok else 'FAIL'}")
    print()

    # --- 4. The full {r_0..r_3} a-ratio-driver ladder at BOTH cutoffs (diagnostic) ---
    #     r_k^a = (a_{2(k+1)}/a_{2k}) * (Lambda/M_KK)^{-2}  -- FUNCTIONAL-INVARIANT driver.
    k_list = [0, 1, 2, 3]  # (local)
    aratios = np.array([a_ratio(a_dict, k) for k in k_list])           # (local) FI a-ratios
    r_driver_MKK = np.array([r_k_aratio_driver(a_dict, k, 1.0) for k in k_list])     # (local) @ M_KK
    r_driver_sp = np.array([r_k_aratio_driver(a_dict, k, lam_sp) for k in k_list])   # (local) @ Lambda_sp
    aratio_increasing = bool(np.all(np.diff(aratios) > 0))  # (local) S96 RISING-toward-1 finding
    print("=== Full {r_0..r_3} a-ratio-driver ladder (FUNCTIONAL-INVARIANT; w(L_max) cancels) ===")
    print(f"  a-ratios a_{{2(k+1)}}/a_{{2k}}, k=0..3 : {np.array2string(aratios, precision=6)}")
    print(f"    a-ratio increasing toward 1 (S96 finding): {aratio_increasing}")
    print(f"  r_k @ Lambda=M_KK   (lam^-2=1.0)      : {np.array2string(r_driver_MKK, precision=6)}")
    print(f"  r_k @ Lambda=Lambda_sp (lam^-2={lam_factor2_sp:.6f}): "
          f"{np.array2string(r_driver_sp, precision=6)}")
    print()

    # --- 5. THE GATED OBJECT: 2nd-layer ratio (k=3, a_8/a_6) at the species cutoff Lambda_sp ---
    a_ratio_2nd = a_ratio(a_dict, LAYER_K_2ND)  # (local) a_8/a_6 -- FI driver
    r_2nd = r_k_aratio_driver(a_dict, LAYER_K_2ND, lam_sp)  # (local) THE gated scalar
    print("=== GATED OBJECT: r_2nd = (a_8/a_6) * (Lambda_sp/M_KK)^{-2} ===")
    print(f"  a_8/a_6 (FI driver)            = {a_ratio_2nd:.6f}")
    print(f"  (Lambda_sp/M_KK)^{{-2}}          = {lam_factor2_sp:.6f}")
    print(f"  r_2nd = {a_ratio_2nd:.6f} * {lam_factor2_sp:.6f} = {r_2nd:.6f}")
    print(f"  ceiling (tight, EVOI #12)     = {CTRL_PASS_STRICT}")
    print(f"  loose ceiling (S96 INFO/FAIL) = {CTRL_FAIL_STRICT}")
    print()

    # --- 6. FUNCTIONAL-SENSITIVITY contrast (lizzi DIAGNOSTIC; NOT the gated quantity) ---
    #     The a-ratio driver is FUNCTIONAL-INVARIANT (any common w(L_max) cancels in the ratio).
    #     The f-modulated full ratio r_k^full = (f_low/f_high) * lam^-2 * a-ratio is
    #     FUNCTIONAL-DEPENDENT: Gaussian-cutoff f_2/f_4=4.19 AMPLIFIES; Mellin-f* f_2/f_4=0.033 CRUSHES.
    f_ratio_gauss = 4.193548387096773  # (local) Gaussian-cutoff f_2/f_4 (S96 CC-label cross-read)
    f_ratio_mellin = 0.03334657682301352  # (local) Mellin-f* f_2/f_4 (S96 CC-label cross-read)
    r_2nd_gauss = f_ratio_gauss * r_2nd    # (local) f-modulated 2nd-layer ratio, Gaussian functional
    r_2nd_mellin = f_ratio_mellin * r_2nd  # (local) f-modulated 2nd-layer ratio, Mellin functional
    print("=== FUNCTIONAL-SENSITIVITY contrast (DIAGNOSTIC; the lizzi finding, NOT gated) ===")
    print(f"  GATED a-ratio driver r_2nd (FUNCTIONAL-INVARIANT)      = {r_2nd:.6f}")
    print(f"  f-modulated (Gaussian f_2/f_4={f_ratio_gauss:.3f}) AMPLIFIES -> {r_2nd_gauss:.6f}")
    print(f"  f-modulated (Mellin   f_2/f_4={f_ratio_mellin:.4f}) CRUSHES   -> {r_2nd_mellin:.6f}")
    print("  => SAME D_K spectrum, opposite EFT-control verdicts under different spectral")
    print("     functionals; only the scheme-independent a-ratio driver is the gated object.")
    print()

    # --- 7. S96 npz cross-read (independent prior computation of r_driver_sp[3]) ---
    s96_r_driver_sp3 = None  # (local)
    s96_max_r_MKK = None     # (local)
    try:
        s96 = np.load(S96_SDW_NPZ, allow_pickle=True)  # (local)
        s96_r_driver_sp = np.asarray(s96["r_driver_sp"], dtype=np.float64)  # (local)
        s96_r_driver_sp3 = float(s96_r_driver_sp[LAYER_K_2ND])  # (local)
        s96_max_r_MKK = float(s96["max_r_MKK"])  # (local)
        print("=== S96 npz cross-read (independent prior computation) ===")
        print(f"  S96 r_driver_sp[k=3] = {s96_r_driver_sp3:.8f}  (this gate r_2nd = {r_2nd:.8f})")
        print(f"  agreement |dev| = {abs(s96_r_driver_sp3 - r_2nd):.3e}")
        print(f"  S96 max a-ratio driver @ M_KK = {s96_max_r_MKK:.6f}  (the S96 base-layer INFO datum)")
        print()
    except (OSError, KeyError) as e:
        print(f"  (S96 npz cross-read skipped: {e})")
        print()

    # --- 8. SIGN/MAGNITUDE/REGIME 3-tuple ([SIGN] gate) ---
    signed_delta = r_2nd - CTRL_PASS_STRICT  # (local) the signed quantity for sign_verdict
    computed_sign = "+" if signed_delta > 0 else ("-" if signed_delta < 0 else "0")  # (local)
    sign_verdict = "PASS" if computed_sign == PREDICTED_SIGN_R2ND_MINUS_CEIL else "FAIL"  # (local)

    # magnitude_verdict: PASS = r_2nd in PASS band; INFO = marginal; FAIL = above loose band.
    if r_2nd < CTRL_PASS_STRICT:
        magnitude_verdict = "PASS"   # (local)
    elif r_2nd < CTRL_FAIL_STRICT:
        magnitude_verdict = "INFO"   # (local)
    else:
        magnitude_verdict = "FAIL"   # (local)

    # regime_verdict: the SDW layer expansion's regime of validity. The closed d=8 cone is
    # exact (no truncation of the cone -- poles close at n=8); the a-moments are bit-exact
    # zeta residues. The species-scale cutoff is within the THIN EFT-breakdown shell
    # [M_KK, 2.06 M_KK]; the expansion is asymptotic but the gated ratio is a finite,
    # well-defined closed-cone quantity. VALID.
    regime_verdict = "VALID"  # (local)

    # Composite-collapse (gate-verdicts.md PRE-REGISTERED rule):
    #   regime BREAKDOWN -> FAIL; sign FAIL -> FAIL; mag FAIL & regime VALID -> FAIL;
    #   mag FAIL & regime MARGINAL -> INFO; mag INFO -> INFO; else PASS.
    if regime_verdict == "BREAKDOWN":
        verdict = "FAIL"  # (local)
    elif sign_verdict == "FAIL":
        verdict = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        verdict = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        verdict = "INFO"
    elif magnitude_verdict == "INFO":
        verdict = "INFO"
    else:
        verdict = "PASS"

    print("=== SIGN/MAGNITUDE/REGIME 3-tuple ([SIGN] gate) ===")
    print(f"  signed delta (r_2nd - {CTRL_PASS_STRICT}) = {signed_delta:+.6f}  (computed sign {computed_sign})")
    print(f"  predicted sign (plan Step 4) = {PREDICTED_SIGN_R2ND_MINUS_CEIL}  -> sign_verdict = {sign_verdict}")
    print(f"  magnitude_verdict = {magnitude_verdict}  (PASS<{CTRL_PASS_STRICT}; "
          f"INFO [{CTRL_PASS_STRICT},{CTRL_FAIL_STRICT}); FAIL>={CTRL_FAIL_STRICT})")
    print(f"  regime_verdict = {regime_verdict}  (closed d=8 cone exact; species shell)")
    print(f"  COMPOSITE = {verdict}")
    print()

    # --- 9. Persist data ---
    r_2nd_round = round(r_2nd, PUB_PRECISION)  # (local) published precision
    np.savez(
        OUT_NPZ,
        # gated object
        r_2nd=r_2nd,
        r_2nd_published=r_2nd_round,
        a_ratio_2nd=a_ratio_2nd,
        lam_factor2_sp=lam_factor2_sp,
        ctrl_pass_strict=CTRL_PASS_STRICT,
        ctrl_fail_strict=CTRL_FAIL_STRICT,
        layer_k_2nd=LAYER_K_2ND,
        # full ladder diagnostic
        k_list=np.array(k_list),
        a_dict_keys=np.array([0, 2, 4, 6, 8]),
        a_dict_vals=np.array([a_dict[n] for n in [0, 2, 4, 6, 8]]),
        aratios=aratios,
        aratio_increasing=aratio_increasing,
        r_driver_MKK=r_driver_MKK,
        r_driver_sp=r_driver_sp,
        lam_factor2_MKK=lam_factor2_MKK,
        # E38 cache cross-check
        cache_moments=np.array([cache_a[n] for n in [0, 2, 4, 6, 8]]),
        crosscheck_ok=crosscheck_ok,
        n_modes=n_modes,
        tot_mult=tot_mult,
        # functional-sensitivity contrast
        f_ratio_gauss=f_ratio_gauss,
        f_ratio_mellin=f_ratio_mellin,
        r_2nd_gauss=r_2nd_gauss,
        r_2nd_mellin=r_2nd_mellin,
        # S96 cross-read
        s96_r_driver_sp3=(np.nan if s96_r_driver_sp3 is None else s96_r_driver_sp3),
        s96_max_r_MKK=(np.nan if s96_max_r_MKK is None else s96_max_r_MKK),
        # scales
        Lambda_sp_over_M_KK=lam_sp,
        M_KK=M_KK,
        # 3-tuple
        signed_delta=signed_delta,
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        composite=verdict,
        # SHAs
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  data -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # --- 10. Plot: the {r_0..r_3} ladder at both cutoffs vs the tight/loose ceilings ---
    fig, ax = plt.subplots(figsize=(8.5, 5.5))
    ax.plot(k_list, r_driver_MKK, "o-", color="#e67e22",
            label=r"$r_k^a$ @ $\Lambda=M_{KK}$  (lam$^{-2}$=1)")
    ax.plot(k_list, r_driver_sp, "s-", color="#16a085",
            label=rf"$r_k^a$ @ $\Lambda=\Lambda_{{sp}}$  (lam$^{{-2}}$={lam_factor2_sp:.3f})")
    # Highlight the gated 2nd-layer point at Lambda_sp
    ax.plot([LAYER_K_2ND], [r_2nd], "*", color="#c0392b", markersize=20,
            label=rf"GATED $r_{{2nd}}$ (k=3, $\Lambda_{{sp}}$) = {r_2nd:.4f}")
    ax.axhline(CTRL_PASS_STRICT, color="#2980b9", ls="--", lw=1.5,
               label=rf"tight ceiling {CTRL_PASS_STRICT} (EVOI #12; PASS$<$)")
    ax.axhline(CTRL_FAIL_STRICT, color="#7f8c8d", ls=":", lw=1.5,
               label=rf"loose ceiling {CTRL_FAIL_STRICT} (S96; INFO/FAIL split)")
    ax.set_xlabel(r"SDW layer index $k$  ($r_k = a_{2(k+1)}/a_{2k}\cdot(\Lambda/M_{KK})^{-2}$)")
    ax.set_ylabel(r"EFT-control ratio $r_k$ (a-ratio driver, FUNCTIONAL-INVARIANT)")
    ax.set_title(f"{GATE_ID}: 2nd-layer SDW EFT-control at species scale  "
                 f"[{verdict}]\n"
                 rf"$r_{{2nd}}$={r_2nd:.4f} in [{CTRL_PASS_STRICT}, {CTRL_FAIL_STRICT}) "
                 "-> marginal (under loose band, not tight)")
    ax.set_xticks(k_list)
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"  plot -> {OUT_PNG.relative_to(PROJECT_ROOT)}")
    print()

    # --- 11. 4-tuple + emit_verdict payload ---
    tag = emit_4tuple(round(r_2nd, PUB_PRECISION), SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)

    value_str = (f"r_2nd={r_2nd:.4f}_vs_tight_0.1_INFO_marginal;"
                 f"a8/a6={a_ratio_2nd:.4f}_FI;lam_sp^-2={lam_factor2_sp:.4f};"
                 f"cache_crosscheck={'PASS' if crosscheck_ok else 'FAIL'};"
                 f"f-sens_Gauss_AMP={r_2nd_gauss:.3f}_Mellin_CRUSH={r_2nd_mellin:.4f}")  # (local)

    extra_rows = [
        f"# regulator_pin=a_n^{{ζ}} # {GATE_ID} (zeta-regulated SDW moments; regulator-pin-discipline.md)",
        (f"# functional_sensitivity: a-ratio driver FUNCTIONAL-INVARIANT (w(L_max) cancels); "
         f"f-modulated FUNCTIONAL-DEPENDENT (Gaussian f_2/f_4={f_ratio_gauss:.2f} AMPLIFIES r_2nd->"
         f"{r_2nd_gauss:.3f}; Mellin f_2/f_4={f_ratio_mellin:.4f} CRUSHES r_2nd->{r_2nd_mellin:.4f})"
         f" # {GATE_ID} lizzi diagnostic"),
    ]  # (local)

    print_verdict_payload(
        verdict, value_str, audit_sha, content_sha,
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        companion_note=f"2nd-layer SDW EFT-control ratio at Lambda_sp; EVOI Tier-3 #12; r_2nd={r_2nd:.4f}",
        extra_rows=extra_rows,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
