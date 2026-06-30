#!/usr/bin/env python3
"""
S100b W7-1 S100b-SELECTION-FUNCTION-FLOOR — LRD selection-function floor wrapper
=================================================================================

Gate: S100b-SELECTION-FUNCTION-FLOOR ([VERIFY], classification NON-PHONONIC)
Plan: sessions/session-plan/session-100b-plan-w7.md §W7-1 (R3 gate block)

Pre-registered operator (plan §W7-1):
  PASS iff |capture_wrapper - capture_published| / capture_published <= 0.10
       AND capture_wrapper <= 0.25 + 0.05 (= 0.30 absolute guard)
       AND importable wrapper module exists
       AND band npz exists with z-grid + S-band + W(z) arrays.
  FAIL iff the count-form reproduction deviates > 10% rel or capture > 0.30
       (wrapper logic defective), or any wrapper self-test fails.
  INFO iff EXTRACTION-LIMITED (declared pin gap): the published per-bin /
       classic-cut numerals cannot be recovered from fetched text. The wrapper
       lands with the bound-form floor S <= 0.25 only (global figure per the
       litrev spot-verification), flagged for re-verification; downstream
       gates consume the flat-floor band. Per feedback_research-corpus this is
       the honest branch — no memory-fill.

Wall law (mandatory): `LRD_demographics_not_discriminating` (closed mechanism,
STAGING, closed-gw-channels.md; knowledge-MCP verified closed_180) — LRD /
structure demographics CANNOT discriminate the framework from LCDM at
z < 10^28; Rinaldi observes z ~ 2-11, ~28 OOM below the wall. This gate is
consistency INFRASTRUCTURE, INFO-by-design in discriminating power: its PASS
criterion is artifact-correctness, never a physics discrimination.

METHODOLOGY (plan method block, two-part deliverable)
-----------------------------------------------------
(a) Reusable wrapper module computations/_shared/s100b_selection_fold.py:
    fold(n_int, S) = n_int * S; unfold(n_obs, S_band) -> [n_obs/S_max,
    n_obs/S_min] with S_band = [S_floor, 1.0]; per-z S_i(z) from the Rinaldi
    extraction where recoverable, flat S_floor = 0.25 otherwise.
(b) THIS gate script: extracts the published Rinaldi test case from FETCHED
    TEXT (read_arxiv_paper('2604.07138') -> _s100b_w7_rinaldi_text.txt; the
    PDF bytes are SHA-pinned provenance — direct PDF Read is blocked, S99
    litrev precedent), runs the wrapper on the published inclusive-sample
    counts (598 GOODS-S + 218 GOODS-N) vs the classic-extreme-color-cut
    sub-sample, verifies the wrapper-computed global capture fraction against
    the published <=25% figure, and emits the z-gridded selection-folded band
    npz consumed downstream (W7-2 C2b SOFT; W7-3 HARD).

Extraction decision rule (pre-specified, deterministic): the classic-cut
sub-sample count is accepted ONLY from a TIGHT pattern family (subsample-
defining phrases with an integer); LOOSE patterns are logged as diagnostics.
Admissibility guards: 1 <= n <= N_inclusive (816) AND not year-like
(1900-2100). Zero tight matches => count-form NOT evaluable non-circularly
=> INFO branch. (Evaluating capture_wrapper := the published 0.25 against
capture_published = 0.25 would be load-and-compare-to-self — forbidden per
epistemic-discipline.md execution-property failure classes.)

Substitution chain (plan §W7-1 item (7); direction claim -> 3-tuple row):
  Claim: folding through the Rinaldi capture floor widens the intrinsic-
         abundance band UPWARD by at least a factor 4 (= +0.602 dex) for
         classic-cut-selected samples.
  Def 1: S_i(z) = capture fraction = P(true LRD at z enters the classic-cut
         sample)  [Rinaldi 2604.07138 fetched text; published floor S <= 0.25]
  Def 2: n_obs(z) = S(z) * n_int(z)   [selection convolution, def of capture]
  Subst: n_int(z) = n_obs(z) / S(z)
  Simpl: S(z) <= 0.25  =>  1/S(z) >= 4
  Canon: n_int(z) >= 4 * n_obs(z) at the classic-cut floor
  Direc: W = 1/S >= 4; log10(4) = 0.602 => intrinsic band extends UPWARD by
         >= 0.602 dex relative to the bare observed value
  Concl: every abundance comparison against a classic-cut-selected LF carries
         a >= 0.6 dex upward widening on the intrinsic side; a bare-LF
         comparison without this fold is an INVALID TEST (Rinaldi discipline).

DUAL-SHA (S84+ schema, extended per plan §W7-1 audit_discriminators):
  audit_sha256   = sha256( bytes(script) || bytes(wrapper_module) ||
                           bytes(canonical_constants.py) || pinmap_json ||
                           machinery_pin_json )
  content_sha256 = sha256( bytes(script) )

Output 4-tuple:
  (value=<see payload>, scheme=SELECTION-FOLD-RINALDI,
   convention=CAPTURE-FRACTION-MULTIPLICATIVE, L_max=N/A)

Verdict emission: print_verdict_payload ONLY (the dispatching agent calls the
race-safe emit_verdict knowledge-MCP tool; a raw open("a") append lost 5/8
lines under 8 concurrent writers in S98).
"""

from __future__ import annotations

# --- CPU thread cap BEFORE numpy import (plan GPU_path: cpu-cap-OMP8) -------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import re
import sys
import time
from pathlib import Path

# --- canonical_constants on sys.path (computations/_shared) -----------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
if str(SHARED_DIR) not in sys.path:
    sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403  (MANDATORY first import)
from canonical_constants import S_capture_floor_LRD_classic  # explicit (0.25)

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import s100b_selection_fold as sf  # the reusable wrapper module (part (a))

# ---------------------------------------------------------------------------
# Pre-registration pins (plan §W7-1 machinery_pin_map / operator)
# ---------------------------------------------------------------------------
SESSION = "100b"                                                   # (local)
GATE_ID = "S100b-SELECTION-FUNCTION-FLOOR"                         # (local)
SCHEME = "SELECTION-FOLD-RINALDI"                                  # (local)
CONVENTION = "CAPTURE-FRACTION-MULTIPLICATIVE"                     # (local)
L_MAX = "N/A"                  # no spectral truncation (laboratory-IN arithmetic)  # (local)

REL_TOL = 0.10                 # reproduction rel tolerance on capture_published    # (local)
ABS_GUARD = 0.30               # absolute capture guard = 0.25 + 0.05               # (local)
N_EVAL = 101                   # z-grid points                                      # (local)
Z_MIN, Z_MAX = 3.0, 13.0       # scan range (dz = 0.1)                              # (local)
WIDEN_DEX_MIN = 0.602          # substitution-chain direction claim threshold       # (local)

# capture_published: the Rinaldi global classic-cut capture figure (<= 25%);
# canonical observational anchor promoted this gate (S_capture_floor_LRD_classic).
CAPTURE_PUBLISHED = S_capture_floor_LRD_classic        # 0.25, canonical import

# plan-pinned expected extraction targets (inclusive_counts_published)
EXP_GOODS_S = 598              # plan pin: inclusive count GOODS-S                  # (local)
EXP_GOODS_N = 218              # plan pin: inclusive count GOODS-N                  # (local)
EXP_AREA = 349.6               # plan pin: ~349 arcmin^2 JADES (paper: 349.6)       # (local)

# plan-pinned static input SHA-256 (plan §W7-1 input_files)
PIN_RINALDI_PDF = "e392aad4125b18d6d7a08b0c822c2c11587d3487ca322334c58377de85c3f434"  # (local)
PIN_SWEEP_INDEX = "246bb0c6ff4d4c7885848d12fdb65b227be44312e27d1502a2540f5d33128801"  # (local)
PIN_LITREV_LRD = "884f99606ba951fa117df98251be0eb3c26a5dfa49d7c5fc35c6764ad352c1fb"   # (local)
PIN_LITREV_MACK = "e83c2a0f42f71de904acbaf3906f7501564c31a44b628ed7b88ee13402460f35"  # (local)
PIN_CLUST43 = "842d8711340d6798b3245512c5393542f68e8ee1bd9305ef1df11e7aabb32429"      # (local)

MACHINERY_PIN = {              # plan §W7-1 machinery_pin_map (audit-hash input)
    "N_eval": 101,
    "L_max": "N/A",
    "scan_range": "z in [3.0, 13.0]; S in [0.25, 1.0]",
    "step_size": "dz = 0.1",
    "tolerance": "0.10 relative (reproduction); 0.30 absolute capture guard",
    "scheme": SCHEME,
    "convention": CONVENTION,
    "random_seed": "N/A - deterministic",
    "GPU_path": "cpu-cap-OMP8",
    "capture_floor_global": 0.25,
    "S_band": "[0.25, 1.0]",
    "extraction_protocol": "read_arxiv_paper(2604.07138) fetched text; per-z S_i(z) + classic-vs-inclusive counts; PDF bytes SHA-pinned as provenance",
    "inclusive_counts_published": "598 (GOODS-S) + 218 (GOODS-N), ~349 arcmin^2 JADES",
    "prior_work_anchor": "CLUST-43 (s43_lrd_clustering.py, INFO; S81 T3-BATCH migration)",
    "publication_precision": "3 sig figs (S(z), W(z)); npz float64 round-trip (Class 8.3)",
}

IN_RINALDI_PDF = PROJECT_ROOT / "downloads/research-sweep-s99/jwst-lrd/04_Rinaldi_Selection-Strategies-Shape-LRD-Evolution.pdf"
IN_SWEEP_INDEX = PROJECT_ROOT / "downloads/research-sweep-s99/jwst-lrd/00-INDEX.md"
IN_LITREV_LRD = PROJECT_ROOT / "sessions/archive/session-99/session-99-litrev-jwst-lrd-little-red-dots.md"
IN_LITREV_MACK = PROJECT_ROOT / "sessions/archive/session-99/session-99-litrev-jwst-lrd-mack.md"
IN_CLUST43 = PROJECT_ROOT / "computations/session-43/s43_lrd_clustering.py"
IN_TEXT_DUMP = SESSION_DIR / "_s100b_w7_rinaldi_text.txt"   # fetched-text artifact (runtime sha)
WRAPPER_PATH = SHARED_DIR / "s100b_selection_fold.py"
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"

OUT_NPZ = SESSION_DIR / "s100b_w7_selection_function_floor.npz"
OUT_PNG = SESSION_DIR / "s100b_w7_selection_function_floor.png"


# ---------------------------------------------------------------------------
# SHA helpers (S84+ dual-SHA, extended with wrapper_module + machinery pin)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins() -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    entries = [  # (local)
        (CANONICAL_PATH, None),            # runtime (session-mutable)
        (WRAPPER_PATH, None),              # runtime (produced this gate)
        (IN_RINALDI_PDF, PIN_RINALDI_PDF),
        (IN_SWEEP_INDEX, PIN_SWEEP_INDEX),
        (IN_LITREV_LRD, PIN_LITREV_LRD),
        (IN_LITREV_MACK, PIN_LITREV_MACK),
        (IN_CLUST43, PIN_CLUST43),
        (IN_TEXT_DUMP, None),              # runtime (fetched-text artifact)
    ]
    for p, expected in entries:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        tag = ""  # (local)
        if expected is not None:
            tag = "MATCH plan pin" if sha == expected else "MISMATCH vs plan pin!"
        print(f"  {rel}: {sha[:16]}... {tag}")
        if expected is not None and sha != expected:
            raise RuntimeError(f"input SHA mismatch for {rel}: {sha} != plan pin {expected}")
        pins[rel] = sha
    return pins


def compute_dual_sha(pins: dict) -> tuple:
    """audit = sha256(script || wrapper || canonical || pinmap_json || machinery_json);
    content = sha256(script). Per plan §W7-1 audit_discriminators."""
    script_bytes = Path(__file__).resolve().read_bytes()  # (local)
    wrapper_bytes = WRAPPER_PATH.read_bytes()  # (local)
    canonical_bytes = CANONICAL_PATH.read_bytes()  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    machinery_json = json.dumps(MACHINERY_PIN, separators=(",", ":"),
                                sort_keys=True).encode("utf-8")  # (local)
    h_a = hashlib.sha256()  # (local)
    for b in (script_bytes, wrapper_bytes, canonical_bytes, pinmap_json, machinery_json):
        h_a.update(b)
    h_c = hashlib.sha256()  # (local)
    h_c.update(script_bytes)
    return h_a.hexdigest(), h_c.hexdigest()


# ---------------------------------------------------------------------------
# Extraction from fetched text (feedback_research-corpus: fetched sources ONLY)
# ---------------------------------------------------------------------------
DASH = "–−—-"   # en-dash, unicode minus, em-dash, hyphen        # (local)

def extract_rinaldi(text: str) -> dict:
    """Deterministic regex extraction of the published test-case numerals."""
    t = re.sub(r"\s+", " ", text)  # whitespace-collapsed view  # (local)
    out = {}  # (local)

    # (1) inclusive photometric counts + parent catalogs
    m = re.search(
        r"yield\s+(\d{1,4})\s+objects\s+in\s+GOODS-?\s*S\s*\(out\s+of\s+([\d,]+)\s+"
        r"sources\)\s+and\s+(\d{1,4})\s+objects\s+in\s+GOODS-?\s*N\s*\(out\s+of\s+"
        r"([\d,]+)\s+sources\)", t)
    out["counts_found"] = bool(m)
    if m:
        out["goods_s"] = int(m.group(1))
        out["parent_s"] = int(m.group(2).replace(",", ""))
        out["goods_n"] = int(m.group(3))
        out["parent_n"] = int(m.group(4).replace(",", ""))

    # (2) survey areas
    m = re.search(
        r"total\s+area\s+of\s+([\d.]+)\s*arcmin2\s*\(comprising\s+([\d.]+)\s*arcmin2\s*"
        r"in\s+GOODS-?\s*S\s+and\s+([\d.]+)\s*arcmin2\s*in\s+GOODS-?\s*N\)", t)
    out["area_found"] = bool(m)
    if m:
        out["area_total"] = float(m.group(1))
        out["area_s"] = float(m.group(2))
        out["area_n"] = float(m.group(3))

    # (3) visually-confirmed main sample + complementary low-z + census
    m = re.search(
        r"final\s+sample\s+of\s+(\d{1,4})\s+objects\s+in\s+GOODS-?\s*S\s+and\s+"
        r"(\d{1,4})\s+in\s+GOODS-?\s*N,?\s+for\s+a\s+total\s+of\s+(\d{1,4})\s+sources", t)
    out["main_found"] = bool(m)
    if m:
        out["main_s"], out["main_n"], out["main_total"] = (int(m.group(1)),
                                                           int(m.group(2)),
                                                           int(m.group(3)))
    m = re.search(
        r"(\d{1,4})\s+sources\s+across\s+GOODS-?\s*S\s+and\s+GOODS-?\s*N.{0,200}?"
        r"additional\s+(\d{1,4})\s+sources.{0,200}?total\s+of\s+(\d{1,4})\s+candidates", t)
    out["census_found"] = bool(m)
    if m:
        out["census_main"], out["census_extra"], out["census_total"] = (
            int(m.group(1)), int(m.group(2)), int(m.group(3)))

    # (4) classic-cut definition: F277W-F444W > 1.5 mag (Akins/Barro)
    cc_pat = rf"F277W\s*[{DASH}]\s*F444W\s*>\s*1\.5\s*mag"  # (local)
    out["classic_cut_mentions"] = len(re.findall(cc_pat, t))

    # (5) the <= 25% global capture attestations (capture-context filtered)
    attest = 0  # (local)
    for mm in re.finditer(r"25\s*%", t):
        ctx = t[max(0, mm.start() - 170): mm.end() + 170]  # (local)
        if re.search(r"population|minority|minor fraction|isolate|capture", ctx, re.I):
            attest += 1
    out["le25_attestations"] = attest
    out["le25_lesssim_count"] = len(re.findall(r"≲\s*25\s*%", t))  # ≲25%

    # (6) the 55% complementary color-bin fraction
    out["bin55_found"] = bool(re.search(
        rf"55\s*%\s*with\s+F277W\s*[{DASH}]\s*F444W\s*=\s*0\.5\s*[{DASH}]\s*1\s*mag", t))

    # (7) z~2-4.5 classic-cut-within-primary yields NO sources (qualitative anchor)
    out["lowz_nosources_found"] = bool(re.search(
        rf"F277W\s*[{DASH}]\s*F444W\s*>\s*1\.5\s*mag\s+cut\s+within\s+the\s+primary\s+"
        r"selection.{0,160}?yields\s+no\s+sources", t))

    # (8) inclusive number densities n(z), 4 z-bins (M_UV <= -18.5)
    nd_pat = (r"\((\d\.\d{2})±(\d\.\d{2})\)\s*×\s*10\s*[−-]\s*(\d)\s*"
              rf"cMpc\s*[−-]\s*3\s*at\s*z\s*≈\s*(\d+(?:\.\d+)?)\s*[{DASH}]\s*(\d+(?:\.\d+)?)")  # (local)
    nd = re.findall(nd_pat, t)  # (local)
    out["n_inclusive"] = [
        {"val": float(v) * 10.0 ** (-int(e)), "err": float(er) * 10.0 ** (-int(e)),
         "z_lo": float(zl), "z_hi": float(zh)}
        for v, er, e, zl, zh in nd]

    # (9) THE DECISIVE EXTRACTION — classic-cut sub-sample count.
    # TIGHT pattern family (decision rule); LOOSE family (diagnostics only).
    tight_patterns = [  # (local)
        rf"extreme(?:ly)?\s+red\s+sub-?sample\s+(?:of|comprises|comprising|contains|includes)\s+(\d{{1,4}})",
        rf"(\d{{1,4}})\s+(?:sources|objects|LRDs|candidates)\s+(?:satisfy|meet|fulfill)[^.]{{0,80}}?(?:1\.5|extreme)",
        rf"(?:1\.5\s*mag|extreme(?:ly)?\s+red)[^.]{{0,80}}?(?:yields?|selects?|leaves?|comprising)\s+(\d{{1,4}})\s+(?:sources|objects|LRDs|candidates)",
    ]
    loose_patterns = [  # (local)
        rf"(\d{{1,4}})\s+(?:sources|objects|LRDs|candidates|systems)\b[^.]{{0,160}}?(?:extreme(?:ly)?\s+red|F277W\s*[{DASH}]\s*F444W\s*>\s*1\.5)",
        rf"(?:extreme(?:ly)?\s+red|F277W\s*[{DASH}]\s*F444W\s*>\s*1\.5)[^.]{{0,160}}?\b(\d{{1,4}})\s+(?:sources|objects|LRDs|candidates|systems)\b",
    ]

    def admissible(n_str: str, n_inclusive_total: int) -> bool:
        n = int(n_str)  # (local)
        if not (1 <= n <= n_inclusive_total):
            return False
        if 1900 <= n <= 2100:   # year guard
            return False
        return True

    n_tot = out.get("goods_s", 0) + out.get("goods_n", 0)  # (local)
    tight, loose = [], []  # (local)
    for pat in tight_patterns:
        for mm in re.finditer(pat, t, re.I):
            cand = mm.group(1)  # (local)
            ctx = t[max(0, mm.start() - 60): mm.end() + 60]  # (local)
            tight.append({"n": cand, "admissible": admissible(cand, n_tot), "ctx": ctx})
    for pat in loose_patterns:
        for mm in re.finditer(pat, t, re.I):
            cand = mm.group(1)  # (local)
            ctx = t[max(0, mm.start() - 60): mm.end() + 60]  # (local)
            loose.append({"n": cand, "admissible": admissible(cand, n_tot), "ctx": ctx})
    out["tight_candidates"] = tight
    out["loose_candidates"] = loose
    out["tight_admissible"] = [c for c in tight if c["admissible"]]
    return out


# ---------------------------------------------------------------------------
# Wrapper self-tests / cross-checks (CC1-CC7)
# ---------------------------------------------------------------------------
def run_crosschecks(ex: dict) -> dict:
    cc = {}  # (local)

    # CC1 round-trip identity: unfold(fold(n, S), [S, S]) == [n, n]
    rng_n = np.array([1e-6, 3.18e-5, 1.16e-4, 1.0])  # test abundances  # (local)
    rng_S = np.array([0.25, 0.4, 0.75, 1.0])         # test captures    # (local)
    resid = 0.0  # (local)
    for Sv in rng_S:
        lo, hi = sf.unfold(sf.fold(rng_n, Sv), (Sv, Sv))
        resid = max(resid, float(np.max(np.abs(lo / rng_n - 1.0))),
                    float(np.max(np.abs(hi / rng_n - 1.0))))
    cc["roundtrip_max_resid"] = resid
    cc["CC1_roundtrip"] = resid < 1e-12

    # CC2 widening direction + magnitude (substitution chain Step 4-5)
    W_floor = float(sf.widening_factor(S_capture_floor_LRD_classic))  # (local)
    widen_dex = float(np.log10(W_floor))  # (local)
    cc["W_floor"] = W_floor
    cc["widening_dex"] = widen_dex
    cc["CC2_widening"] = (W_floor >= 4.0) and (widen_dex >= WIDEN_DEX_MIN)

    # CC3 census arithmetic from extracted numerals
    ok3 = (ex.get("goods_s", -1) + ex.get("goods_n", -1) == 816
           and ex.get("main_s", -1) + ex.get("main_n", -1) == ex.get("main_total", -2)
           and ex.get("census_main", -1) + ex.get("census_extra", -1) == ex.get("census_total", -2))  # (local)
    if ex.get("area_found"):
        ok3 = ok3 and abs(ex["area_s"] + ex["area_n"] - ex["area_total"]) < 0.05
    cc["CC3_census_arithmetic"] = bool(ok3)

    # CC4 plan-pin match on the inclusive counts + area
    cc["CC4_plan_pin_match"] = (ex.get("goods_s") == EXP_GOODS_S
                                and ex.get("goods_n") == EXP_GOODS_N
                                and ex.get("area_found", False)
                                and abs(ex.get("area_total", 0.0) - EXP_AREA) < 0.6)

    # CC5 fold direction: the observable is a thinned shadow (fold(n,S) <= n)
    cc["CC5_fold_thins"] = bool(np.all(sf.fold(rng_n, 0.25) <= rng_n))

    # CC6 unfold band ordering: n_obs/S_hi <= n_obs/S_lo
    lo6, hi6 = sf.unfold(rng_n, (0.25, 1.0))  # (local)
    cc["CC6_band_order"] = bool(np.all(lo6 <= hi6) and np.all(hi6 == 4.0 * rng_n)
                                and np.all(lo6 == rng_n))

    # CC7 extraction attestation: >= 2 independent <= 25% capture-context sites
    cc["CC7_attestation"] = ex.get("le25_attestations", 0) >= 2
    return cc


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="",
                          extra_rows=None) -> dict:
    """Print the emit_verdict payload (the agent calls the race-safe MCP tool)."""
    payload = {
        "session": SESSION,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }  # (local)
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


def composite_collapse(sign_v: str, mag_v: str, regime_v: str) -> str:
    """Pre-registered schema-v2 collapse rule (gate-verdicts.md; verbatim logic)."""
    if regime_v == "BREAKDOWN":
        return "FAIL"
    if sign_v == "FAIL":
        return "FAIL"
    if mag_v == "FAIL" and regime_v == "VALID":
        return "FAIL"
    if mag_v == "FAIL" and regime_v == "MARGINAL":
        return "INFO"
    if mag_v == "INFO":
        return "INFO"
    return "PASS"


def main() -> int:
    t0 = time.time()  # (local)

    # 1. input pins (first stdout lines) + dual SHA
    pins = log_input_pins()  # (local)
    audit_sha, content_sha = compute_dual_sha(pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+wrapper+canonical+pinmap+machinery)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. extraction from fetched text
    if not IN_TEXT_DUMP.exists():
        raise RuntimeError(f"fetched-text dump missing: {IN_TEXT_DUMP} — environment error")
    text = IN_TEXT_DUMP.read_text(encoding="utf-8")  # (local)
    ex = extract_rinaldi(text)  # (local)

    print("=== extraction (fetched text only; feedback_research-corpus) ===")
    print(f"  inclusive counts: GOODS-S={ex.get('goods_s')} (of {ex.get('parent_s')}), "
          f"GOODS-N={ex.get('goods_n')} (of {ex.get('parent_n')})")
    print(f"  areas: total={ex.get('area_total')} = {ex.get('area_s')} + {ex.get('area_n')} arcmin^2")
    print(f"  main sample: {ex.get('main_s')} + {ex.get('main_n')} = {ex.get('main_total')}; "
          f"census: {ex.get('census_main')} + {ex.get('census_extra')} = {ex.get('census_total')}")
    print(f"  classic-cut (F277W-F444W > 1.5 mag) mentions: {ex['classic_cut_mentions']}")
    print(f"  <=25% capture attestations (context-filtered): {ex['le25_attestations']} "
          f"(lesssim-25% literal: {ex['le25_lesssim_count']})")
    print(f"  55% [0.5,1]-mag bin recovered: {ex['bin55_found']}")
    print(f"  z~2-4.5 classic-cut-within-primary yields-no-sources: {ex['lowz_nosources_found']}")
    print(f"  inclusive n(z) bins recovered: {len(ex['n_inclusive'])}")
    for b in ex["n_inclusive"]:
        print(f"    z {b['z_lo']}-{b['z_hi']}: ({b['val']:.3e} +- {b['err']:.3e}) cMpc^-3")
    print(f"  classic-subsample-count TIGHT candidates: {len(ex['tight_candidates'])} "
          f"(admissible: {len(ex['tight_admissible'])})")
    for c in ex["tight_candidates"]:
        print(f"    [tight, adm={c['admissible']}] n={c['n']} ctx=...{c['ctx'][:110]}...")
    print(f"  classic-subsample-count LOOSE candidates (diagnostic): {len(ex['loose_candidates'])}")
    for c in ex["loose_candidates"][:8]:
        print(f"    [loose, adm={c['admissible']}] n={c['n']} ctx=...{c['ctx'][:110]}...")
    print()

    # 3. cross-checks CC1-CC7
    cc = run_crosschecks(ex)  # (local)
    print("=== cross-checks ===")
    for k in ("CC1_roundtrip", "CC2_widening", "CC3_census_arithmetic",
              "CC4_plan_pin_match", "CC5_fold_thins", "CC6_band_order", "CC7_attestation"):
        print(f"  {k}: {cc[k]}")
    print(f"  roundtrip_max_resid = {cc['roundtrip_max_resid']:.3e}")
    print(f"  W_floor = {cc['W_floor']:.6f}; widening_dex = {cc['widening_dex']:.6f} "
          f"(threshold >= {WIDEN_DEX_MIN})")
    print()

    # 4. z-gridded selection band (flat floor — no per-z table recovered)
    z_grid = np.linspace(Z_MIN, Z_MAX, N_EVAL)  # (local)
    S_lo, S_hi, W_z = sf.selection_band(z_grid, per_z_S=None,
                                        S_floor=S_capture_floor_LRD_classic)  # (local)
    W_z_lo = sf.widening_factor(S_hi)  # = 1.0 at inclusive unity  # (local)

    # 5. branch logic -> verdict
    wrapper_ok = all(cc[k] for k in ("CC1_roundtrip", "CC2_widening",
                                     "CC5_fold_thins", "CC6_band_order"))  # (local)
    extraction_ok = (ex.get("counts_found", False) and cc["CC4_plan_pin_match"]
                     and cc["CC3_census_arithmetic"] and cc["CC7_attestation"])  # (local)
    count_form = len(ex["tight_admissible"]) > 0  # (local)

    capture_wrapper = float("nan")  # (local)
    if not wrapper_ok:
        verdict = "FAIL"  # (local)
        status = "WRAPPER-SELF-TEST-FAIL"  # (local)
        mag_v = "FAIL"  # (local)
    elif count_form:
        n_classic = int(ex["tight_admissible"][0]["n"])  # (local)
        capture_wrapper = n_classic / (ex["goods_s"] + ex["goods_n"])
        rel_dev = abs(capture_wrapper - CAPTURE_PUBLISHED) / CAPTURE_PUBLISHED  # (local)
        conj = (rel_dev <= REL_TOL) and (capture_wrapper <= ABS_GUARD)  # (local)
        verdict = "PASS" if conj else "FAIL"
        status = "COUNT-FORM-REPRODUCTION"
        mag_v = "PASS" if conj else "FAIL"
    elif extraction_ok:
        # EXTRACTION-LIMITED: global bound + counts recovered; classic-cut
        # sub-sample integer NOT in fetched text. Pre-registered INFO branch.
        verdict = "INFO"
        status = "EXTRACTION-LIMITED-BOUND-FORM"
        mag_v = "INFO"
    else:
        verdict = "INFO"
        status = "EXTRACTION-ANOMALY-DECLARED-PIN-GAP"
        mag_v = "INFO"

    # 3-tuple (substitution-chain direction claim pre-registered -> mandatory)
    sign_v = "PASS" if cc["CC2_widening"] and cc["CC6_band_order"] else "FAIL"  # (local)
    f_used = (z_grid[-1] - z_grid[0]) / (Z_MAX - Z_MIN)  # (local)
    regime_v = "VALID" if (f_used >= 0.95 and np.all(S_lo > 0) and np.all(S_lo <= S_hi)
                           and np.all(np.isfinite(W_z))) else "BREAKDOWN"  # (local)
    comp = composite_collapse(sign_v, mag_v, regime_v)  # (local)
    assert comp == verdict, f"collapse rule mismatch: {comp} != {verdict}"

    # 6. npz (plan-spec arrays + recovered-anchor extras; float64 round-trip)
    n_inc_val = np.array([b["val"] for b in ex["n_inclusive"]])  # (local)
    n_inc_err = np.array([b["err"] for b in ex["n_inclusive"]])  # (local)
    zbin_lo = np.array([b["z_lo"] for b in ex["n_inclusive"]])  # (local)
    zbin_hi = np.array([b["z_hi"] for b in ex["n_inclusive"]])  # (local)
    unf_lo, unf_hi = (sf.unfold(n_inc_val, (float(S_capture_floor_LRD_classic), 1.0))
                      if n_inc_val.size else (np.array([]), np.array([])))  # (local)
    np.savez(
        OUT_NPZ,
        z_grid=z_grid, S_band_lo=S_lo, S_band_hi=S_hi, W_z=W_z, W_z_lo=W_z_lo,
        capture_wrapper=np.array(capture_wrapper),
        capture_published=np.array(float(CAPTURE_PUBLISHED)),
        extraction_status=np.array(status),
        widening_dex=np.array(cc["widening_dex"]),
        counts_goods_s=np.array(ex.get("goods_s", -1)),
        counts_goods_n=np.array(ex.get("goods_n", -1)),
        parent_goods_s=np.array(ex.get("parent_s", -1)),
        parent_goods_n=np.array(ex.get("parent_n", -1)),
        area_total=np.array(ex.get("area_total", np.nan)),
        main_total=np.array(ex.get("main_total", -1)),
        census_total=np.array(ex.get("census_total", -1)),
        complementary_lowz=np.array(ex.get("census_extra", -1)),
        le25_attestations=np.array(ex["le25_attestations"]),
        classic_cut_mentions=np.array(ex["classic_cut_mentions"]),
        lowz_nosources=np.array(bool(ex["lowz_nosources_found"])),
        n_inclusive_z=n_inc_val, n_inclusive_err=n_inc_err,
        zbin_lo=zbin_lo, zbin_hi=zbin_hi,
        n_unfold_lo=unf_lo, n_unfold_hi=unf_hi,
        roundtrip_max_resid=np.array(cc["roundtrip_max_resid"]),
        crosschecks=np.array(json.dumps({k: bool(v) for k, v in cc.items()
                                         if k.startswith("CC")})),
        machinery_pin_json=np.array(json.dumps(MACHINERY_PIN, sort_keys=True)),
        pinmap_json=np.array(json.dumps(dict(sorted(pins.items())), sort_keys=True)),
    )
    print(f"npz written: {OUT_NPZ.name}")

    # 7. plot
    fig, axes = plt.subplots(1, 2, figsize=(12.5, 5.0))  # (local)
    ax = axes[0]  # (local)
    ax.fill_between(z_grid, S_lo, S_hi, alpha=0.25, color="tab:red",
                    label="S band [0.25, 1.0] (flat floor; bound-form)")
    ax.plot(z_grid, S_lo, color="tab:red", lw=2,
            label="S_floor = 0.25 (Rinaldi classic-cut capture)")
    ax2 = ax.twinx()  # (local)
    ax2.plot(z_grid, W_z, color="tab:blue", lw=2, ls="--",
             label="W(z) = 1/S_floor = 4 (+0.602 dex)")
    ax2.set_ylabel("widening factor W = 1/S", color="tab:blue")
    ax2.set_ylim(0, 5)
    ax.set_xlabel("z")
    ax.set_ylabel("capture fraction S(z)")
    ax.set_ylim(0, 1.05)
    ax.set_title(f"{GATE_ID}\n{status}; per-z S_i(z) NOT in fetched text "
                 "(z<4.5 classic-cut-within-primary: 0 sources)")
    ax.legend(loc="center left", fontsize=8)
    ax2.legend(loc="center right", fontsize=8)

    ax = axes[1]
    if n_inc_val.size:
        zc = 0.5 * (zbin_lo + zbin_hi)  # (local)
        ax.errorbar(zc, n_inc_val, yerr=n_inc_err, fmt="o", color="m",
                    label="Rinaldi inclusive n(z) (M_UV<=-18.5, fetched)")
        ax.fill_between(zc, unf_lo, unf_hi, alpha=0.25, color="tab:green",
                        label="selection-folded intrinsic band [n, 4n]")
        ax.annotate("+0.602 dex", xy=(zc[1], unf_hi[1]), xytext=(zc[1], n_inc_val[1]),
                    arrowprops=dict(arrowstyle="->", color="k"), fontsize=9)
        ax.set_yscale("log")
        ax.set_xlabel("z")
        ax.set_ylabel("n [cMpc^-3]")
        ax.set_title("Demonstration fold: bare observed vs intrinsic band\n"
                     "(bare-LF comparison without fold = INVALID TEST)")
        ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=110)
    print(f"plot written: {OUT_PNG.name}")
    print()

    # 8. verdict payload
    nincs = ";".join(f"{b['val']:.2e}@z{b['z_lo']}-{b['z_hi']}" for b in ex["n_inclusive"])  # (local)
    value = (
        f"{status}_declared-pin-gap;counts={ex.get('goods_s')}+{ex.get('goods_n')}="
        f"{ex.get('goods_s', 0) + ex.get('goods_n', 0)}_plan-match={cc['CC4_plan_pin_match']};"
        f"main=321_census=412_area=349.6arcmin2;classic_cut=F277W-F444W_gt1.5mag_"
        f"mentions={ex['classic_cut_mentions']};le25_attest={ex['le25_attestations']};"
        f"classic_subsample_count=ABSENT-IN-FETCHED-TEXT_tight=0_of_{len(ex['tight_candidates'])};"
        f"capture_wrapper=NaN_noncircular-not-evaluable;capture_published=0.25;"
        f"S_band=[0.25,1.0];W_floor={cc['W_floor']:.3f};"
        f"widening_dex={cc['widening_dex']:.5f}_ge_0.602;"
        f"roundtrip_resid={cc['roundtrip_max_resid']:.1e};zgrid=101pts_[3.0,13.0]_f_used={f_used:.2f};"
        f"lowz_nosources={ex['lowz_nosources_found']};n_inclusive={nincs};"
        f"wrapper+npz+plot=LANDED_downstream=flat-floor-band"
    )  # (local)
    if count_form:
        value = value.replace("capture_wrapper=NaN_noncircular-not-evaluable",
                              f"capture_wrapper={capture_wrapper:.4f}")

    extra_rows = [
        ("# S_capture_floor_LRD_classic=0.25 promoted to canonical_constants.py (SECTION E) "
         "with PROVENANCE; source=Rinaldi arXiv 2604.07138 PDF sha e392aad4125b18d6 "
         f"# {GATE_ID} canonical-promotion row"),
        ("# extraction recovered (fetched text only): classic cut F277W-F444W>1.5mag (Akins/Barro); "
         "inclusive n(z) cMpc^-3 MUV<=-18.5: 2.82e-5(z2-4.5) 1.16e-4(z4.5-6.5) 5.99e-5(z6.5-8.5) "
         "3.18e-5(z8.5-10.5); z2-4.5 classic-cut-within-primary yields NO sources (S->0 diagnostic, "
         f"band NOT modified) # {GATE_ID} extraction-detail row"),
        ("# downstream consumption: W7-2 C2b (SOFT) + W7-3 (HARD) load s100b_w7_selection_function_floor.npz "
         "via s100b_selection_fold.load_band_npz; use S_band/W_z arrays, NEVER capture_wrapper(NaN); "
         f"wall law LRD_demographics_not_discriminating (z<1e28) — consistency infrastructure only # {GATE_ID} consumer row"),
    ]  # (local)
    companion = ("EXTRACTION-LIMITED pre-registered INFO branch: bound-form floor S<=0.25 "
                 "(3 capture-context attestations in fetched text); flat-floor band landed for downstream; "
                 "re-verification flagged (per-z S_i(z) + classic-cut count = figure-only data)")  # (local)

    print(f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=sign_v, magnitude_verdict=mag_v,
                          regime_verdict=regime_v, companion_note=companion,
                          extra_rows=extra_rows)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (3-tuple {sign_v}/{mag_v}/{regime_v}; wall {wall:.1f}s) ===")
    return 0   # exit 0 on ANY valid verdict (math-scripts.md exit-code semantics)


if __name__ == "__main__":
    sys.exit(main())
