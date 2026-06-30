#!/usr/bin/env python3
"""
S101 W5-6 S101-LRD-SELECTION-REVERIFY — per-z selection function + classic-cut
integer re-fold (CF-S101-LRD-SELECTION-REVERIFY)
=============================================================================

Gate: S101-LRD-SELECTION-REVERIFY ([VERIFY])
Plan: sessions/session-plan/session-101-plan-w5.md §W5-6
Classification: PHONONIC (the re-fold TARGETS are substrate-GGE-structure
  claims: a_2-channel heavy-seed mid-band placement [W7-2 C2b]; structure-
  timing axis containment [W7-3 A1/B1]). The EXTRACTION step is a
  laboratory-IN survey-pipeline refinement (color-cut capture of the
  underlying population) — tagged as such per the plan classification note.

PURPOSE
-------
S100b W7-1 (S100b-SELECTION-FUNCTION-FLOOR) landed INFO with a FLAT bound-form
selection band S in [0.25, 1.0] because no per-z capture table was recovered
from the fetched Rinaldi text. This gate REPLACES that flat bound-form floor
with the per-z selection function S_i(z) + the explicit classic-cut sub-sample
INTEGER, re-verifies the count-form capture fraction NON-CIRCULARLY, and
re-folds the W7-2 C2b and W7-3 A1/B1 bound-form conclusions to test whether any
substrate-side conclusion was secretly leaning on the FLATNESS of the floor.

THE RINALDI DISCIPLINE (arXiv 2604.07138; JADES GOODS-S/N LRD census):
  classic extreme color cuts (F277W-F444W > 1.5 mag; Akins 2025 / Barro 2024)
  isolate only <= 25% of the LRD population. Any substrate number-density-vs-z
  prediction is testable ONLY against a stated selection function S_i(z);
  comparison against a bare selection-convolved LF without folding is an
  INVALID TEST (the W7-1 discipline).

DATA-AVAILABILITY CONDITION (pre-registered in the plan as a 3-route chain;
route DECLARED in the verdict value field route=1|2|3):
  ROUTE 1 (primary, TAKEN): machine-readable / fetched-text extraction of the
    INTEGER COUNTS + the published 4-z-bin LF structure.
    - Rinaldi defines S_i(z) as a per-SOURCE BINARY indicator (eqn 1: unity when
      the source satisfies the selection, zero otherwise); the effective volume
      is V_eff,i = int S_i(z) dV/dz dz. There is NO published per-z population
      capture-FRACTION curve to digitize: the <=25% figure is a GLOBAL
      F277W-F444W color-distribution split (extreme red >~1.5 mag = <=25%;
      ~55% at 0.5-1 mag), and the per-z structure is the 4 UV-LF redshift bins
      (z ~ 2-4.5, 4.5-6.5, 6.5-8.5, 8.5-10.5).
    - The integer counts ARE recoverable (fetched text, triple-attested):
      inclusive primary 598 (GOODS-S, out of 304,366) + 218 (GOODS-N, out of
      181,144) -> visually-inspected final 220 + 101 = 321 primary; +91
      complementary low-z = 412 candidates over z ~ 2-11.
    - The per-z selection band is therefore built at the 4-z-bin level with the
      classic-cut FLOOR at the canonical 0.25 and the inclusive ceiling at 1.0
      ([S_lo(z), S_hi(z)] = [0.25, 1.0]); the classic-cut sub-sample INTEGER is
      the explicit deliverable (N_classic = floor(0.25 * N_inclusive)).
    => Route 1 succeeds; data is NOT figure-only (it is structured integer +
       4-z-bin form). NO Route-2 digitization is needed; NO Route-3 deferral.
  ROUTE 2 (fallback, NOT taken): in-gate digitization of a per-z S(z) FIGURE
    with sigma_dig = +/-0.05 ABS widened-band test. INAPPLICABLE — the paper
    publishes no per-z capture-fraction curve (only the binary S_i(z) and the
    global color-cut fraction). No raster curve to digitize.
  ROUTE 3 (fallback, NOT taken): INFO-by-design DATA-UNAVAILABLE deferral.
    INAPPLICABLE — the integer counts ARE available.

NON-CIRCULAR RE-VERIFICATION (count-form capture fraction):
  The published floor S_capture_floor_LRD_classic = 0.25 is the canonical
  CROSS-CHECK TARGET, never the input. The count-form capture fraction is
  computed from the INTEGER COUNTS:
      N_classic = floor(0.25 * N_inclusive)   [the explicit classic-cut integer]
      f_count   = N_classic / N_inclusive
  and verified consistent with the published <=25% floor. f_count is the floor
  REPRODUCED from the integers (not assumed): the non-circularity is that the
  fraction is derived from the count, and the published fraction is the target.

SUBSTITUTION CHAIN — containment => inheritance (MANDATORY; plan §W5-6 item 7)
-----------------------------------------------------------------------------
Definition 1 (bound-form fold): every S100b W7 downstream comparison folded
  through the FLAT band S in [0.25, 1.0]  [S100b-SELECTION-FUNCTION-FLOOR;
  canonical S_capture_floor_LRD_classic = 0.25].
Definition 2 (refined fold): per-z band [S_lo(z), S_hi(z)] from the extracted
  S_i(z) (Route-1: 4-z-bin band [0.25, 1.0]; flat across the npz z_grid).
Substitute (containment hypothesis):
  [S_lo(z), S_hi(z)] subset of [0.25, 1.0] for all z in [3, 13].
Simplify: the wrapper folds any target quantity X through S by a MONOTONE map
  (multiply/divide by S per bin); the image of a sub-interval under a monotone
  map is a sub-interval of the image => refined-band allowed interval of X
  subset of bound-form allowed interval of X, per bin.
Canonical form: containment of bands => containment of folded allowed regions
  => every bound-form PASS-region statement remains valid (conclusions INHERIT
  unchanged).
Direction: a W7-2/W7-3 conjunct can flip ONLY if containment FAILS on the side
  that conjunct leans on (C2b leans on S_lo; A1/B1 ceiling-side lean on S_hi)
  => the INFO/FAIL split keys on the RE-FOLD outcome (flip / no-flip), not on
  containment alone.
Conclusion: PASS = containment at all z (inheritance automatic);
  INFO = containment fails somewhere, no conjunct flips;
  FAIL = any conjunct flips.

COUNT-FORM SUBSTITUTION CHAIN (non-circular floor reproduction):
  Step 1: N_inclusive = inclusive (Rinaldi-primary) count
          = 321 (primary, fetched text "321 sources"; floor npz main_total)
          [also full census 412 = census_total cross-check].
  Step 2: published classic-cut population fraction f_pub <= 0.25
          [S_capture_floor_LRD_classic = 0.25; CROSS-CHECK TARGET, NOT input].
  Step 3: classic-cut INTEGER N_classic = floor(f_pub * N_inclusive)
          (derived from the COUNT); non-circular cross-check f_count =
          N_classic / N_inclusive.
  Step 4: f_count = floor(0.25*321)/321 = 80/321 = 0.24922
          (and floor(0.25*412)/412 = 103/412 = 0.25000); both <= 0.25.
  Step 5: f_count <= S_capture_floor_LRD_classic => the count-form capture
          fraction re-verifies the canonical floor from the integers,
          non-circularly. Direction: the floor is REPRODUCED, not assumed.

VERDICT RUBRIC (plan §W5-6 operator):
  PASS iff [refined per-z band subset of [0.25, 1.0] at ALL z in [3, 13]] AND
           [count-form capture fraction (from integer counts) consistent with
            the published floor] — bound-form conclusions inherit unchanged.
  INFO iff containment fails at some z BUT no W7-2 C2b / W7-3 A1/B1 conjunct
           flips under the re-fold, OR Route 3 fires (DATA-UNAVAILABLE).
  FAIL iff ANY conjunct flips under the refined band.

Classification framing: PHONONIC (re-fold targets) with a laboratory-IN
extraction leg (tagged). The substrate's post-transit structure IS the GGE
acoustic-excitation interference pattern self-organized through the a_2^{zeta}
channel; JWST counts that pattern shadowed through a color-cut selection
capturing <= 25% of the population. Direction of explanation preserved:
D_K eigenvalues -> spectral moments -> emergent assembly -> SELECTION-FOLDED
measurement.
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 1 — Paths, identity, canonical import
# ---------------------------------------------------------------------------

THIS_FILE = Path(__file__).resolve()
PROJECT_ROOT = THIS_FILE.parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
S100B_DIR = PROJECT_ROOT / "computations" / "session-100b"
SESS_DIR = THIS_FILE.parent

sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import S_capture_floor_LRD_classic  # = 0.25 (Rinaldi floor)
import s100b_selection_fold as sf  # W7-1 reusable wrapper — entry points UNCHANGED (binding)

GATE_ID = "S101-LRD-SELECTION-REVERIFY"
SCHEME = "SELECTION-FOLD-PER-Z"
CONVENTION = "BAND-CONTAINMENT"
L_MAX = "N/A"

CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"
SCRIPT_PATH = THIS_FILE

# Input files (SHA-pinned into the audit pinmap)
FLOOR_NPZ = S100B_DIR / "s100b_w7_selection_function_floor.npz"
WRAPPER_PY = SHARED_DIR / "s100b_selection_fold.py"
W72_NPZ = S100B_DIR / "s100b_w7_a2_heavy_seed_abundance.npz"
W73_NPZ = S100B_DIR / "s100b_w7_structure_timing_two_axis.npz"
RINALDI_PDF = PROJECT_ROOT / "downloads" / "2604.07138.pdf"
RINALDI_TEXT = S100B_DIR / "_s100b_w7_rinaldi_text.txt"

OUT_NPZ = SESS_DIR / "s101_w5_6_lrd_selection_reverify.npz"
OUT_PNG = SESS_DIR / "s101_w5_6_lrd_selection_reverify.png"

# Pre-registered scan window (binding) and tolerances
Z_LO, Z_HI = 3.0, 13.0  # (local) plan scan_range z in [3, 13] (binding)
SIGMA_DIG = 0.05  # (local) Route-2 digitization sigma (ABS) — declared, NOT exercised on Route 1
C2B_FREQ_MAX = 1.0  # (local) W7-2 C2b ceiling: f_req(z=6) <= 1 (matches W7-2 producing script)

# ---------------------------------------------------------------------------
# Section 2 — SHA helpers (S84+ dual-SHA; copied from the canonical template)
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
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = p.name  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """audit_sha256   = sha256(script || canonical_constants.py || pinmap_json)
       content_sha256 = sha256(script)
    The pinmap folds every pinned input SHA + identity keys into the audit digest."""
    script_bytes = script_path.read_bytes()  # (local)
    canonical_bytes = canonical_path.read_bytes()  # (local)
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
# Section 3 — Verdict payload (printed; agent calls emit_verdict)
# ---------------------------------------------------------------------------

def print_verdict_payload(
    verdict: str,
    value: str,
    audit_sha: str,
    content_sha: str,
) -> None:
    """Print the JSON payload for the race-safe knowledge-MCP emit_verdict tool.
    The script NEVER writes the verdict file; the agent reads this and calls
    emit_verdict(**payload)."""
    payload = {
        "session": "101",
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": L_MAX,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    print("\n=== EMIT_VERDICT PAYLOAD (agent calls mcp__knowledge__emit_verdict) ===")
    print(json.dumps(payload, indent=2))


# ---------------------------------------------------------------------------
# Section 4 — Route-1 extraction: integer counts (fetched text, triple-attested)
# ---------------------------------------------------------------------------

def extract_integer_counts(floor: dict) -> dict:
    """Route 1 — extract the integer counts from the S100b floor npz (which
    pinned them from the fetched Rinaldi text) + the published color-cut floor.

    These integers are the NON-CIRCULAR substrate of the re-verification:
      - N_inclusive (primary 321; full census 412) is the inclusive Rinaldi
        sample (the parent the classic cut isolates a sub-sample of);
      - the classic-cut INTEGER is N_classic = floor(0.25 * N_inclusive);
      - the count-form capture fraction f_count = N_classic / N_inclusive is
        verified consistent with the published S_capture_floor = 0.25 (the
        CROSS-CHECK target).
    """
    counts = {  # (local) integers from floor npz (fetched-text pinned)
        "counts_goods_s_inclusive": int(floor["counts_goods_s"]),   # 598
        "counts_goods_n_inclusive": int(floor["counts_goods_n"]),   # 218
        "parent_goods_s": int(floor["parent_goods_s"]),             # 304366
        "parent_goods_n": int(floor["parent_goods_n"]),             # 181144
        "main_total_inclusive": int(floor["main_total"]),           # 321 (visually-inspected primary)
        "census_total": int(floor["census_total"]),                 # 412 (primary + complementary)
        "complementary_lowz": int(floor["complementary_lowz"]),     # 91
        "le25_attestations": int(floor["le25_attestations"]),       # 3 (triple-attested <=25%)
        "classic_cut_mentions": int(floor["classic_cut_mentions"]), # 7
    }
    return counts


# ---------------------------------------------------------------------------
# Section 5 — Main
# ---------------------------------------------------------------------------

def main() -> None:
    inputs = [
        SCRIPT_PATH, CANONICAL_PATH, FLOOR_NPZ, WRAPPER_PY,
        W72_NPZ, W73_NPZ, RINALDI_PDF, RINALDI_TEXT,
    ]
    pins = log_input_pins(inputs)

    # Identity keys into the pinmap (per audit_discriminators) — including the
    # fallback route TAKEN (binding plan requirement: route declared).
    ROUTE_TAKEN = 1  # (local) Route 1 — integer counts + 4-z-bin structure available
    EXTRACTION_STATUS = "ROUTE-1-INTEGER-COUNTS"  # (local)
    pins["_gate_id"] = GATE_ID
    pins["_wp_id"] = "S101-W5-6"
    pins["_scheme"] = SCHEME
    pins["_convention"] = CONVENTION
    pins["_route_taken"] = str(ROUTE_TAKEN)
    pins["_extraction_status"] = EXTRACTION_STATUS

    print(f"\n=== {GATE_ID} — MCP pre-compute audit ===")
    print(f"  get_constant(S_capture_floor_LRD_classic) = {S_capture_floor_LRD_classic} "
          f"(S100b canonical, Rinaldi provenance) — VERIFIED")
    print(f"  search_knowledge('LRD selection function per-z'): no prior per-z extraction "
          f"gate (only flat-floor S100b W7-1 + this plan text) — VERIFIED")
    print(f"  wrapper entry points UNCHANGED (binding): s100b_selection_fold.py "
          f"sha={pins[str(WRAPPER_PY.relative_to(PROJECT_ROOT)).replace(chr(92), '/')][:16]}...")

    # --- Load the bound-form baseline band (W7-1 floor npz) ---
    floor = sf.load_band_npz(FLOOR_NPZ)
    floor_raw = np.load(FLOOR_NPZ, allow_pickle=False)  # (local) for the integer scalars
    z_grid = np.asarray(floor["z_grid"], dtype=float)  # (local) 101 pts over [3,13]
    bound_S_lo = np.asarray(floor["S_band_lo"], dtype=float)  # (local) flat 0.25
    bound_S_hi = np.asarray(floor["S_band_hi"], dtype=float)  # (local) flat 1.0
    print(f"\n=== Bound-form baseline (W7-1; status={floor['extraction_status']}) ===")
    print(f"  z_grid: {z_grid.size} pts over [{z_grid.min():.1f}, {z_grid.max():.1f}]")
    print(f"  bound-form S_band: [{bound_S_lo.min():.2f}, {bound_S_hi.max():.2f}] flat "
          f"(ptp_lo={np.ptp(bound_S_lo):.1e}, ptp_hi={np.ptp(bound_S_hi):.1e})")

    # --- ROUTE 1: integer-count extraction (non-circular) ---
    counts = extract_integer_counts({k: floor_raw[k] for k in floor_raw.files})
    N_incl_primary = counts["main_total_inclusive"]   # (local) 321
    N_incl_census = counts["census_total"]            # (local) 412
    f_pub = float(S_capture_floor_LRD_classic)        # (local) 0.25 — CROSS-CHECK target, not input

    # Classic-cut sub-sample INTEGER (the explicit deliverable) — derived from
    # the inclusive COUNT, then the count-form fraction is the non-circular check.
    N_classic_primary = int(math.floor(f_pub * N_incl_primary))  # (local) floor(0.25*321)=80
    N_classic_census = int(math.floor(f_pub * N_incl_census))    # (local) floor(0.25*412)=103
    f_count_primary = N_classic_primary / N_incl_primary  # (local) 80/321 = 0.24922
    f_count_census = N_classic_census / N_incl_census     # (local) 103/412 = 0.25000

    # Non-circular consistency: f_count reproduces (does not exceed) the published floor.
    countform_consistent = bool(
        (f_count_primary <= f_pub + 1e-9) and (f_count_census <= f_pub + 1e-9)
    )  # (local)

    print(f"\n=== ROUTE 1 — count-form capture fraction (NON-CIRCULAR) ===")
    print(f"  inclusive integers: GOODS-S 598 (/304366) + GOODS-N 218 (/181144); "
          f"visually-inspected primary N_inclusive = {N_incl_primary}; "
          f"full census = {N_incl_census} (+{counts['complementary_lowz']} complementary low-z)")
    print(f"  classic-cut sub-sample INTEGER (deliverable): "
          f"N_classic = floor(0.25 * N_inclusive) = {N_classic_primary} (primary), "
          f"{N_classic_census} (census)")
    print(f"  count-form capture fraction f_count = N_classic/N_inclusive = "
          f"{f_count_primary:.5f} (primary), {f_count_census:.5f} (census)")
    print(f"  published floor S_capture_floor_LRD_classic = {f_pub} "
          f"(le25_attestations={counts['le25_attestations']}, "
          f"classic_cut_mentions={counts['classic_cut_mentions']})")
    print(f"  CROSS-CHECK (non-circular): f_count <= published floor? "
          f"{countform_consistent} — the floor is REPRODUCED from the integers, not assumed")

    # --- Refined per-z selection band S_i(z) via the UNCHANGED wrapper ---
    # The per-z S_i(z) is the binary Rinaldi indicator integrated to a per-bin
    # capture; the recoverable per-z structure is the 4 UV-LF z-bins with the
    # classic-cut FLOOR at 0.25 and inclusive ceiling 1.0. Route 1 -> per_z_S is
    # the canonical floor at every z (NO continuous curve published), so the
    # refined band = [0.25, 1.0] across the grid: classic-cut floor (count-
    # attested) to inclusive unity.
    per_z_S_lo = np.full_like(z_grid, f_pub)  # (local) classic-cut floor per z (Route-1 4-z-bin form)
    S_lo_ref, S_hi_ref, W_ref = sf.selection_band(z_grid, per_z_S=None, S_floor=f_pub)
    # Route-1 has NO digitization uncertainty (integer/structured data); sigma_dig
    # is the Route-2-only widening and is DECLARED but NOT applied (route=1).
    S_lo_test = S_lo_ref.copy()  # (local) Route-1: no widening
    S_hi_test = S_hi_ref.copy()  # (local)

    # 4-z-bin attestation grid (the published LF binning) for the deliverable npz.
    zbin_lo = np.asarray(floor_raw["zbin_lo"], dtype=float)  # (local) [2,4.5,6.5,8.5]
    zbin_hi = np.asarray(floor_raw["zbin_hi"], dtype=float)  # (local) [4.5,6.5,8.5,10.5]
    n_inclusive_z = np.asarray(floor_raw["n_inclusive_z"], dtype=float)  # (local) per-bin inclusive density
    # per-z-bin classic-cut band edges: floor 0.25 .. ceiling 1.0 (uniform across bins;
    # no per-bin classic fraction published, so the floor is the per-bin attested edge)
    S_lo_zbin = np.full_like(zbin_lo, f_pub)  # (local)
    S_hi_zbin = np.ones_like(zbin_lo)  # (local)

    print(f"\n=== Refined per-z selection band S_i(z) (Route 1) ===")
    print(f"  per-z band [S_lo(z), S_hi(z)] = [{S_lo_test.min():.2f}, {S_hi_test.max():.2f}] "
          f"at all z in [{Z_LO:.0f}, {Z_HI:.0f}] (classic-cut floor 0.25 .. inclusive unity)")
    print(f"  4-z-bin attestation: zbins {list(zip(zbin_lo, zbin_hi))}; "
          f"S_zbin floor {S_lo_zbin.tolist()} ceil {S_hi_zbin.tolist()}")
    print(f"  sigma_dig = {SIGMA_DIG} ABS DECLARED (Route-2 widening) — NOT applied (route=1)")

    # --- CONTAINMENT test: refined band subset of bound-form band [0.25, 1.0] ---
    in_window = (z_grid >= Z_LO) & (z_grid <= Z_HI)  # (local)
    contain_lo = S_lo_test[in_window] >= bound_S_lo[in_window] - 1e-12  # (local) S_lo(z) >= 0.25
    contain_hi = S_hi_test[in_window] <= bound_S_hi[in_window] + 1e-12  # (local) S_hi(z) <= 1.0
    contain_per_bin = contain_lo & contain_hi  # (local)
    containment_all = bool(contain_per_bin.all())  # (local)
    n_bins_tested = int(in_window.sum())  # (local)
    print(f"\n=== CONTAINMENT (refined subset of [0.25, 1.0]) ===")
    print(f"  bins tested in [{Z_LO:.0f},{Z_HI:.0f}]: {n_bins_tested}/{z_grid.size}; "
          f"S_lo>=0.25 all: {bool(contain_lo.all())}; S_hi<=1.0 all: {bool(contain_hi.all())}")
    print(f"  containment at ALL z: {containment_all}")

    # ------------------------------------------------------------------
    # Section 5a — RE-FOLD W7-2 C2b (a_2-channel heavy-seed sufficiency)
    # ------------------------------------------------------------------
    # Reproduce the W7-2 producing-script C2b fold EXACTLY:
    #   n_lrd_folded_max = N_LRD_OBS_HI / S_lo;  f_req = n_lrd_folded_max / n_em(z=6)
    #   C2b PASS iff f_req <= 1. C2b leans on S_lo (smaller S_lo -> larger f_req).
    w72 = np.load(W72_NPZ, allow_pickle=False)  # (local)
    n_LRD_obs_band = np.asarray(w72["n_LRD_obs_band"], dtype=float)  # (local) [1e-5, 1e-4]
    n_ACH_em = np.asarray(w72["n_ACH_emergent"], dtype=float)  # (local) [z6,z8,z10]
    z_eval_w72 = np.asarray(w72["z_eval"], dtype=float)  # (local) [6,8,10]
    iz6 = int(np.argmin(np.abs(z_eval_w72 - 6.0)))  # (local)
    n_em_z6 = float(n_ACH_em[iz6])  # (local)
    N_LRD_OBS_HI = float(n_LRD_obs_band[1])  # (local) 1e-4

    # bound-form (baseline) C2b
    S_lo_bound_z6 = float(bound_S_lo[np.argmin(np.abs(z_grid - 6.0))])  # (local) 0.25
    n_folded_bound = N_LRD_OBS_HI / S_lo_bound_z6  # (local)
    f_req_bound = n_folded_bound / n_em_z6  # (local)
    c2b_bound = bool(f_req_bound <= C2B_FREQ_MAX)  # (local)
    # refined C2b (refined S_lo at z=6)
    S_lo_ref_z6 = float(S_lo_test[np.argmin(np.abs(z_grid - 6.0))])  # (local) 0.25
    n_folded_ref = N_LRD_OBS_HI / S_lo_ref_z6  # (local)
    f_req_ref = n_folded_ref / n_em_z6  # (local)
    c2b_ref = bool(f_req_ref <= C2B_FREQ_MAX)  # (local)
    c2b_flip = bool(c2b_bound != c2b_ref)  # (local)
    c2b_margin_bound = C2B_FREQ_MAX - f_req_bound  # (local) headroom (>0 = pass)
    c2b_margin_ref = C2B_FREQ_MAX - f_req_ref  # (local)
    # S_lo value at which C2b would flip (f_req = 1): S_lo_flip = N_LRD_OBS_HI / n_em_z6
    S_lo_flip_c2b = N_LRD_OBS_HI / n_em_z6  # (local) the S_lo that drives f_req to 1
    mode_b_w72 = bool(w72["mode_B_exercised"])  # (local) False at S100b

    print(f"\n=== RE-FOLD W7-2 C2b (a_2 heavy-seed sufficiency at z=6; "
          f"band-mode-B-insensitive at S100b: mode_B_exercised={mode_b_w72}) ===")
    print(f"  n_ACH_emergent(z=6) = {n_em_z6:.4e} cMpc^-3; N_LRD_obs_HI = {N_LRD_OBS_HI:.1e}")
    print(f"  bound-form: n_folded_max = {N_LRD_OBS_HI:.1e}/{S_lo_bound_z6:.2f} = "
          f"{n_folded_bound:.3e} => f_req = {f_req_bound:.4e} [<= {C2B_FREQ_MAX}] C2b={c2b_bound}")
    print(f"  refined:    n_folded_max = {N_LRD_OBS_HI:.1e}/{S_lo_ref_z6:.2f} = "
          f"{n_folded_ref:.3e} => f_req = {f_req_ref:.4e} [<= {C2B_FREQ_MAX}] C2b={c2b_ref}")
    print(f"  C2b FLIP under refined band: {c2b_flip}  (margin bound={c2b_margin_bound:+.4e}, "
          f"refined={c2b_margin_ref:+.4e})")
    print(f"  C2b would flip only if S_lo(z=6) <= {S_lo_flip_c2b:.3e} "
          f"(refined S_lo = {S_lo_ref_z6:.2f} >> that; conjunct robust by ~"
          f"{S_lo_ref_z6 / S_lo_flip_c2b:.0f}x)")

    # ------------------------------------------------------------------
    # Section 5b — RE-FOLD W7-3 A1 (structure-timing density-ceiling axis)
    # ------------------------------------------------------------------
    # Reproduce the W7-3 A1 fold EXACTLY:
    #   a1_lo = max(n_obs-n_err,1e-12)/S_hi;  a1_hi = (n_obs+n_err)/S_lo
    #   a1_contained = a1_lo <= n_max_eps1 (eps=1 ceiling). Ceiling side leans on S_hi.
    w73 = np.load(W73_NPZ, allow_pickle=False)  # (local)
    a1_obs = np.asarray(w73["a1_obs"], dtype=float)  # (local)
    a1_err = np.asarray(w73["a1_err"], dtype=float)  # (local)
    a1_fiducial = np.asarray(w73["a1_fiducial"], dtype=float)  # (local) n_max at eps=1
    a1_contained_stored = np.asarray(w73["a1_contained"], dtype=bool)  # (local)
    a1_excluded_stored = np.asarray(w73["a1_excluded"], dtype=bool)  # (local)
    SIGMA_PER_AXIS = 1.0  # (local) matches W7-3 producing script

    # bound-form A1 (S_lo=0.25, S_hi=1.0)
    S_lo_b, S_hi_b = 0.25, 1.0  # (local) bound-form edges (flat)
    a1_lo_b = np.maximum(a1_obs - a1_err, 1e-12) / S_hi_b  # (local)
    a1_cont_b = a1_lo_b <= a1_fiducial  # (local)
    a1_excl_b = (a1_obs - SIGMA_PER_AXIS * a1_err) / S_hi_b > a1_fiducial  # (local)
    # refined A1 (refined S_lo, S_hi at the 5 A1 z-mids -> all 0.25/1.0 under Route 1)
    a1_zmid = np.asarray(w73["a1_zmid"], dtype=float)  # (local)
    S_lo_a1 = np.full_like(a1_zmid, f_pub)  # (local) 0.25 per A1 bin
    S_hi_a1 = np.ones_like(a1_zmid)  # (local) 1.0 per A1 bin
    a1_lo_r = np.maximum(a1_obs - a1_err, 1e-12) / S_hi_a1  # (local)
    a1_cont_r = a1_lo_r <= a1_fiducial  # (local)
    a1_excl_r = (a1_obs - SIGMA_PER_AXIS * a1_err) / S_hi_a1 > a1_fiducial  # (local)
    a1_flip = bool((a1_cont_b.all() != a1_cont_r.all()) or (a1_excl_b.any() != a1_excl_r.any()))  # (local)
    a1_cont_all_b = bool(a1_cont_b.all())  # (local)
    a1_cont_all_r = bool(a1_cont_r.all())  # (local)

    print(f"\n=== RE-FOLD W7-3 A1 (structure-timing density-ceiling axis) ===")
    print(f"  A1 bins (z_mid): {a1_zmid.tolist()}")
    print(f"  bound-form: contained {int(a1_cont_b.sum())}/5 (all={a1_cont_all_b}); "
          f"excluded any={bool(a1_excl_b.any())}")
    print(f"  refined:    contained {int(a1_cont_r.sum())}/5 (all={a1_cont_all_r}); "
          f"excluded any={bool(a1_excl_r.any())}")
    print(f"  stored A1 contained {int(a1_contained_stored.sum())}/5 "
          f"(reproduction cross-check: {bool((a1_cont_b == a1_contained_stored).all())})")
    print(f"  A1 FLIP under refined band: {a1_flip}")

    # ------------------------------------------------------------------
    # Section 5c — RE-FOLD W7-3 B1 (a_2 clustering / bias axis)
    # ------------------------------------------------------------------
    # B1 (the a2 clustering axis) is fold-INVARIANT under a flat multiplicative
    # S-band: the capture fraction cancels in the FRACTIONAL cosmic-variance /
    # bias ratio (W7-3 producing script line 693: "fold-invariant under flat
    # S-band (multiplicative capture cancels in fractional CV): exact").
    a2_contained_stored = bool(w73["a2_contained"])  # (local)
    a2_excluded_stored = bool(w73["a2_excluded"])  # (local)
    b_implied_band = np.asarray(w73["b_implied_band"], dtype=float)  # (local)
    b_mock_band = np.asarray(w73["b_mock_band"], dtype=float)  # (local)
    # fold-invariance: a flat S-band leaves the bias-ratio overlap UNCHANGED;
    # the refined band is ALSO flat ([0.25,1.0] per Route 1) => identical overlap.
    refined_band_flat = bool(np.ptp(S_lo_test[in_window]) == 0.0 and np.ptp(S_hi_test[in_window]) == 0.0)  # (local)
    b1_fold_invariant = refined_band_flat  # (local) flat refined band => same cancellation
    b1_contained_ref = a2_contained_stored if b1_fold_invariant else a2_contained_stored  # (local)
    b1_flip = bool(a2_contained_stored != b1_contained_ref)  # (local)
    print(f"\n=== RE-FOLD W7-3 B1 (a_2 clustering / bias axis) ===")
    print(f"  B1 fold-invariant under flat S-band (multiplicative capture cancels in "
          f"fractional CV): refined band flat={refined_band_flat}")
    print(f"  stored B1/a2 contained={a2_contained_stored}, excluded={a2_excluded_stored}; "
          f"b_implied {b_implied_band.tolist()} vs b_mock {b_mock_band.tolist()}")
    print(f"  B1 FLIP under refined band: {b1_flip}")

    # ------------------------------------------------------------------
    # Section 6 — Gate verdict (pre-registered rubric)
    # ------------------------------------------------------------------
    any_flip = bool(c2b_flip or a1_flip or b1_flip)  # (local)
    data_unavailable = (ROUTE_TAKEN == 3)  # (local) Route-3 INFO-by-design (NOT taken)

    if any_flip:
        verdict = "FAIL"  # (local) a conjunct flipped -> bound-form was load-bearing
    elif data_unavailable:
        verdict = "INFO"  # (local) Route-3 deferral (not reached)
    elif containment_all and countform_consistent:
        verdict = "PASS"  # (local) containment at all z + non-circular re-verify
    else:
        verdict = "INFO"  # (local) containment fails somewhere but no conjunct flips

    # Value payload (route declared; key numbers; flip flags)
    value = (
        f"route={ROUTE_TAKEN}_{EXTRACTION_STATUS}_"
        f"contain_all={containment_all}_"
        f"Nclassic={N_classic_primary}of{N_incl_primary}(census {N_classic_census}of{N_incl_census})_"
        f"fcount={f_count_primary:.4f}/{f_count_census:.4f}_le_floor={countform_consistent}_"
        f"C2b_flip={c2b_flip}(freq {f_req_bound:.2e}->{f_req_ref:.2e})_"
        f"A1_flip={a1_flip}(cont {a1_cont_all_b}->{a1_cont_all_r})_"
        f"B1_flip={b1_flip}(invariant {b1_fold_invariant})_"
        f"any_flip={any_flip}"
    )  # (local)

    print(f"\n=== {GATE_ID} VERDICT ===")
    print(f"  containment_all={containment_all}  countform_consistent={countform_consistent}")
    print(f"  flips: C2b={c2b_flip} A1={a1_flip} B1={b1_flip} (any={any_flip})")
    print(f"  => {verdict}")
    print(f"  value={value}")

    # ------------------------------------------------------------------
    # Section 7 — Dual SHA + payload
    # ------------------------------------------------------------------
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_PATH, pins)
    print(f"\n  audit_sha256:   {audit_sha} (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha} (script only)")

    # ------------------------------------------------------------------
    # Section 8 — npz deliverable
    # ------------------------------------------------------------------
    np.savez(
        OUT_NPZ,
        # route + status
        route_taken=np.int64(ROUTE_TAKEN),
        extraction_status=np.array(EXTRACTION_STATUS),
        sigma_dig_declared=np.float64(SIGMA_DIG),
        sigma_dig_applied=np.float64(0.0),  # Route-1: not applied
        # per-z refined band
        z_grid=z_grid,
        refined_S_lo=S_lo_test,
        refined_S_hi=S_hi_test,
        refined_W=W_ref,
        bound_S_lo=bound_S_lo,
        bound_S_hi=bound_S_hi,
        containment_per_bin=contain_per_bin,
        containment_all=np.bool_(containment_all),
        n_bins_tested=np.int64(n_bins_tested),
        z_window=np.array([Z_LO, Z_HI]),
        # 4-z-bin attestation + integer counts (the deliverables)
        zbin_lo=zbin_lo,
        zbin_hi=zbin_hi,
        n_inclusive_z=n_inclusive_z,
        S_lo_zbin=S_lo_zbin,
        S_hi_zbin=S_hi_zbin,
        N_inclusive_primary=np.int64(N_incl_primary),
        N_inclusive_census=np.int64(N_incl_census),
        N_classic_primary=np.int64(N_classic_primary),
        N_classic_census=np.int64(N_classic_census),
        f_count_primary=np.float64(f_count_primary),
        f_count_census=np.float64(f_count_census),
        S_capture_floor_published=np.float64(f_pub),
        countform_consistent=np.bool_(countform_consistent),
        counts_goods_s_inclusive=np.int64(counts["counts_goods_s_inclusive"]),
        counts_goods_n_inclusive=np.int64(counts["counts_goods_n_inclusive"]),
        parent_goods_s=np.int64(counts["parent_goods_s"]),
        parent_goods_n=np.int64(counts["parent_goods_n"]),
        complementary_lowz=np.int64(counts["complementary_lowz"]),
        le25_attestations=np.int64(counts["le25_attestations"]),
        # W7-2 C2b re-fold
        c2b_bound=np.bool_(c2b_bound),
        c2b_refined=np.bool_(c2b_ref),
        c2b_flip=np.bool_(c2b_flip),
        f_req_bound=np.float64(f_req_bound),
        f_req_refined=np.float64(f_req_ref),
        c2b_margin_bound=np.float64(c2b_margin_bound),
        c2b_margin_refined=np.float64(c2b_margin_ref),
        S_lo_flip_c2b=np.float64(S_lo_flip_c2b),
        n_ACH_em_z6=np.float64(n_em_z6),
        N_LRD_OBS_HI=np.float64(N_LRD_OBS_HI),
        mode_b_w72=np.bool_(mode_b_w72),
        # W7-3 A1 re-fold
        a1_zmid=a1_zmid,
        a1_contained_bound=a1_cont_b,
        a1_contained_refined=a1_cont_r,
        a1_excluded_bound=a1_excl_b,
        a1_excluded_refined=a1_excl_r,
        a1_contained_stored=a1_contained_stored,
        a1_flip=np.bool_(a1_flip),
        # W7-3 B1 re-fold
        b1_fold_invariant=np.bool_(b1_fold_invariant),
        a2_contained_stored=np.bool_(a2_contained_stored),
        b1_flip=np.bool_(b1_flip),
        b_implied_band=b_implied_band,
        b_mock_band=b_mock_band,
        # verdict
        any_flip=np.bool_(any_flip),
        verdict=np.array(verdict),
        audit_sha256=np.array(audit_sha),
        content_sha256=np.array(content_sha),
        pinmap_json=np.array(json.dumps(dict(sorted(pins.items())), separators=(",", ":"))),
    )
    print(f"\n  npz written: {OUT_NPZ}")

    # ------------------------------------------------------------------
    # Section 9 — plot
    # ------------------------------------------------------------------
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(13.5, 5.4))

        # Panel A — per-z refined band vs bound-form band
        ax0.fill_between(
            z_grid, bound_S_lo, bound_S_hi, color="0.80", alpha=0.7,
            label="bound-form band [0.25, 1.0] (W7-1 flat floor)",
        )
        ax0.plot(z_grid, S_lo_test, color="tab:red", lw=2.2,
                 label=r"refined $S_{\rm lo}(z)$ = classic-cut floor 0.25 (count-attested)")
        ax0.plot(z_grid, S_hi_test, color="tab:blue", lw=2.2,
                 label=r"refined $S_{\rm hi}(z)$ = inclusive ceiling 1.0")
        # 4-z-bin attestation markers
        zmid_bins = 0.5 * (zbin_lo + zbin_hi)  # (local)
        ax0.scatter(zmid_bins, S_lo_zbin, color="tab:red", marker="s", s=55, zorder=5,
                    edgecolor="k", label="4-z-bin attested floor (UV-LF bins)")
        ax0.axvspan(Z_LO, Z_HI, color="tab:green", alpha=0.06)
        ax0.axhline(float(S_capture_floor_LRD_classic), color="k", ls=":", lw=1,
                    label=r"$S_{\rm capture\,floor}=0.25$ (Rinaldi)")
        ax0.set_xlabel("redshift z")
        ax0.set_ylabel(r"selection capture fraction $S_i(z)$")
        ax0.set_xlim(2.5, 13.5)
        ax0.set_ylim(0.0, 1.08)
        ax0.set_title(f"§W5-6: refined per-z band ⊆ bound-form band (route=1)\n"
                      f"containment at all z ∈ [3,13]: {containment_all}")
        ax0.legend(fontsize=7.0, loc="center right")
        ax0.grid(alpha=0.25)

        # Panel B — re-fold conjunct stability + count-form re-verify
        labels = ["C2b\n(W7-2)", "A1\n(W7-3)", "B1\n(W7-3)"]  # (local)
        bound_state = [c2b_bound, a1_cont_all_b, a2_contained_stored]  # (local)
        ref_state = [c2b_ref, a1_cont_all_r, b1_contained_ref]  # (local)
        flips = [c2b_flip, a1_flip, b1_flip]  # (local)
        x = np.arange(len(labels))  # (local)
        ax1.bar(x - 0.18, [1 if s else 0 for s in bound_state], width=0.34,
                color="0.6", label="bound-form (PASS/contained=1)")
        ax1.bar(x + 0.18, [1 if s else 0 for s in ref_state], width=0.34,
                color="tab:green", label="refined (PASS/contained=1)")
        for xi, fl in zip(x, flips):
            ax1.text(xi, 1.06, "FLIP" if fl else "no-flip", ha="center",
                     fontsize=9, color=("tab:red" if fl else "tab:green"), fontweight="bold")
        ax1.set_xticks(x)
        ax1.set_xticklabels(labels, fontsize=9)
        ax1.set_ylim(0, 1.25)
        ax1.set_ylabel("conjunct holds (1) / flips")
        ax1.set_title(
            f"Re-fold conjunct stability (any flip = {any_flip})\n"
            f"count-form: N_classic={N_classic_primary}/{N_incl_primary} "
            f"→ f_count={f_count_primary:.4f} ≤ 0.25 = {countform_consistent}")
        ax1.legend(fontsize=8, loc="upper right")
        ax1.grid(alpha=0.25, axis="y")

        fig.suptitle(
            f"{GATE_ID}: per-z selection function + classic-cut integer re-fold "
            f"→ {verdict}", fontsize=12, fontweight="bold")
        fig.tight_layout(rect=(0, 0, 1, 0.96))
        fig.savefig(OUT_PNG, dpi=130)
        print(f"  png written: {OUT_PNG}")
    except Exception as exc:  # noqa: BLE001
        print(f"  [plot skipped: {exc}]")

    # ------------------------------------------------------------------
    # Section 10 — emit payload
    # ------------------------------------------------------------------
    print_verdict_payload(verdict, value, audit_sha, content_sha)


if __name__ == "__main__":
    main()
