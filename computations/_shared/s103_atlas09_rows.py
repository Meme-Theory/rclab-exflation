#!/usr/bin/env python3
"""
S103 W1-7 S103-ATLAS09-ROWS — atlas-09 register-authoring: land 3 interpretive-DOF CORRECTION rows
==================================================================================================

Gate: S103-ATLAS09-ROWS ([AUDIT])

Pre-registered threshold:
  PASS iff (3 new atlas-09 CORRECTION rows present in item-37 exemplar form:
              row i  = alpha_s transport-degree scale-and-channel separation,
              row ii = SF54 frame-robust closure,
              row iii= CGWB GW->LSS migration)
           AND each row carries (Type CORRECTION + original-tension + rescoping-move
              + register-of-record + NEW-binding-test + binding-instrument)
           AND the interpretive-DOF-ledger atlas-09 cross-reference resolution re-run
              returns 4/4 (was 1/4 -- only Item 37 / w_0 resolved)
           AND verify == True.
  FAIL iff verify == False (a row absent, OR resolution count < 4/4, OR row-number collision).
  INFO iff the atlas-09 scope/numbering on disk has drifted from the plan-pinned 46-item state
           (a prior session added items) -> author at runtime next-free numbers per
           substrate-first-canonical-sourcing.md §(ii.B) plan-text-drift correction.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - sessions/framework/registry/interpretive-dof-ledger.md  (the assembled rows + register-of-record
        cites + populated binding tests; the W5-5 resolution-check source)
  - sessions/framework/Atlas/atlas-09-retractions.md        (46-item scope, item-37 exemplar form;
        pre-write SHA captured for audit trail)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<resolution_count e.g. 4/4>, scheme=REGISTER-AUTHORING-AFTER-PATTERN,
   convention=ATLAS-09-CORRECTION-ROWS-ITEM-37-EXEMPLAR-FORM;CROSS-RESOLVE-FROM-DOF-LEDGER-4-OF-4,
   L_max=N/A)

Classification: NON-PHONONIC (atlas-09 retraction-ledger register maintenance; Q2-hygiene
  cross-reference resolution). This gate does NOT compute a substrate observable -- it TRANSCRIBES
  three ALREADY-ESTABLISHED rescopings (each with its own prior substitution chain + verdict, cited
  from the DOF-ledger register-of-record) into the formal atlas-09 CORRECTION-row form so the
  interpretive-DOF-ledger cross-references resolve to a single migration-ledger-of-record.

METHODOLOGY
-----------
Register-authoring AFTER-pattern per registry-landing.md §"Bridge-Landing Script Architecture":
  build_rows_text (full text in memory) -> write_atomic_with_fsync -> re_read + verify -> exactly ONE
  print_verdict_payload. The three rescopings (alpha_s transport-degree S92->S93 deg(T)=+2 NON-SCALAR;
  SF54 S100a frame-robust q log-derivative; CGWB S96 W8-2 GW->LSS migration) are transcribed VERBATIM
  from the DOF-ledger §"Per-row detail"; NOTHING is re-derived. The substitution-chain is N/A
  (math-scripts.md §"When the chain is NOT required": citing prior canonical-ledger results verbatim;
  no new direction claim is asserted by THIS gate). The cited canonical values
  (alpha_s_substrate_distance_1 = -0.08587279; alpha_s_pivot_goldstone = 0.0; q median = -0.8662;
  CGWB f_obs ~ 8.4835e39 Hz) are quoted from the DOF-ledger register-of-record cites.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- String assembly + SHA + file I/O only (cpu; OMP 8)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- AFTER-pattern: write FULL text once, re-read + verify, emit exactly ONE verdict payload.
  If verify FAILs, emit FAIL once (no corrective in-script rewrite) per mechanical-closure-discipline.md.
- Gate verdict emitted via the `emit_verdict` knowledge-MCP tool (race-safe; the script PRINTS the
  payload, the dispatching AGENT calls emit_verdict). The script does NOT write the verdict file.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (
    alpha_s_substrate_distance_1,
    alpha_s_pivot_goldstone,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import re
import sys
import time
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SHARED_DIR = Path(__file__).resolve().parent            # computations/_shared
COMPUTATIONS_DIR = SHARED_DIR.parent                    # computations/
PROJECT_ROOT = COMPUTATIONS_DIR.parent                  # project root
SESSION_OUT_DIR = COMPUTATIONS_DIR / "session-103"      # per-session outputs land here

SESSION = "S103"                                        # (local)
GATE_ID = "S103-ATLAS09-ROWS"                           # (local)
SCHEME = "REGISTER-AUTHORING-AFTER-PATTERN"             # (local)
CONVENTION = ("ATLAS-09-CORRECTION-ROWS-ITEM-37-EXEMPLAR-FORM;"
              "CROSS-RESOLVE-FROM-DOF-LEDGER-4-OF-4")    # (local)
L_MAX = "N/A"                                           # (local)

# Pre-registered: the resolution count must reach 4/4 (was 1/4); 4 DOF-ledger rescopings.
RESOLUTION_TARGET = 4                                   # (local)
N_DOF_RESCOPINGS = 4                                    # (local)
PLAN_PINNED_ITEM_COUNT = 46                             # (local) atlas-09 plan-pinned scope (S1-88)

ATLAS09 = PROJECT_ROOT / "sessions" / "framework" / "Atlas" / "atlas-09-retractions.md"
DOF_LEDGER = (PROJECT_ROOT / "sessions" / "framework" / "registry"
              / "interpretive-dof-ledger.md")
CANONICAL = SHARED_DIR / "canonical_constants.py"

OUT_NPZ = SESSION_OUT_DIR / "s103_atlas09_rows.npz"
OUT_PNG = SESSION_OUT_DIR / "s103_atlas09_rows.png"

INPUT_FILES = [CANONICAL, DOF_LEDGER, ATLAS09]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def sha256_of_text(text: str) -> str:
    h = hashlib.sha256()  # (local)
    h.update(text.encode("utf-8"))
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
    """audit = sha256(script || canonical || pinmap_json); content = sha256(script)."""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Build rows text (in-memory; AFTER-pattern step 1)
# ---------------------------------------------------------------------------

def scan_next_free_rows(atlas_text: str) -> tuple[list[int], int]:
    """Scan ALL master-table-row item numbers across every sub-table; return
    (next_free_three, max_item). Item rows look like '| 47 | CORRECTION | ...'.
    Header rows ('| # | Type |') and separator rows ('|:--|') are excluded by the
    integer-first-cell match."""
    nums = set()  # (local)
    for m in re.finditer(r"^\|\s*(\d+)\s*\|", atlas_text, flags=re.MULTILINE):
        nums.add(int(m.group(1)))
    max_item = max(nums) if nums else 0  # (local)
    nxt = [max_item + 1, max_item + 2, max_item + 3]  # (local)
    return nxt, max_item


def build_rows_text(n47: int, n48: int, n49: int) -> tuple[str, str]:
    """Return (master_table_block, narrative_block). Both mirror the item-37 exemplar form.

    Canonical values quoted (NOT re-derived) from the DOF-ledger register-of-record cites:
      alpha_s_substrate_distance_1 = -0.08587279 ; alpha_s_pivot_goldstone = 0.0
      substrate q median = -0.8662 (S100a SF54-mapping npz)
      CGWB f_obs = 8.4835e39 Hz (S96-OBS-CGWB-PEAK-FREQ)
    """
    a_sub = alpha_s_substrate_distance_1  # (local) -0.08587279
    a_piv = alpha_s_pivot_goldstone       # (local) 0.0

    # --- Master-table block (Type | Claim | Session Made | Session Retracted/Corrected
    #                          | Reason | Probability Impact), exemplar = Item 37 ---
    master = (
        "\n"
        "## S92-S100a Interpretive-DOF Rescopings (Items "
        f"{n47}-{n49})\n"
        "\n"
        "These three CORRECTION rows formalize the PENDING-formal-row rescopings assembled in "
        "`sessions/framework/registry/interpretive-dof-ledger.md` (gate "
        "`W5-5-S102-INTERPRETIVE-DOF-LEDGER`, S102). Each is a substrate-first finding already "
        "established at its own register-of-record (cited below); these rows give it its formal "
        "atlas-09 CORRECTION row so the DOF-ledger cross-references resolve to a single "
        "migration-ledger-of-record (resolution 1/4 -> 4/4). Per `feedback_reporting-framing.md`, "
        "each row records WHERE the falsifier MOVED, never that it was defined out of existence.\n"
        "\n"
        "| # | Type | Claim | Session Made | Session Retracted/Corrected | Reason | Probability Impact |\n"
        "|:--|:-----|:------|:-------------|:----------------------------|:-------|:-------------------|\n"
        f"| {n47} | CORRECTION | alpha_s single-Planck-pivot comparison as a 'first multi-sigma "
        "falsifier' (-12.146 sigma Planck-18 / -13.99 sigma Aiola-2020) | S92 AH-TR-1 | S93 W7-1 | "
        "SCALE-AND-CHANNEL separation (alpha_s transport-degree): the substrate carries TWO "
        "scale-separated alpha_s observables, not one -- a substrate-distance running "
        f"(alpha_s_substrate_distance_1 = {a_sub}, inside the BZ, s=3 Mellin pole) and a "
        f"Goldstone-pivot running (alpha_s_pivot_goldstone = {a_piv}, CMB pivot). WHICH a detector "
        "measures is set by the single computable transport degree deg(T_BZ->pivot). S93 W7-1 "
        "RESOLVED deg=+2 NON-SCALAR (w(L_max).kappa(k) factorization_holds=False) => the "
        "scalar-transport (-12.146 sigma) reading is the FALSIFIED leaf; it RELOCATES off-pivot as a "
        "SCALE-MISMATCH (NOT a falsification). The -12.146 sigma did NOT vanish -- it MOVED to the "
        "matched substrate-sensitivity channel (CMB-S4 2030 ~37 sigma / CMB-HD 2035 ~78 sigma reach) "
        "as a live ~34-sigma-class prediction; the pivot leaf (~0, +0.67 sigma) is the matched "
        "Planck-channel reading. Register-of-record: falsifier-master-inventory Row "
        "#3.rescope-AH-TR-1 (CLOSED-NON-SCALAR-TRANSPORT-RESOLVED) + canonical_constants "
        "alpha_s_substrate_distance_1 / alpha_s_pivot_goldstone + cross-pillar-bridge-corpus.md "
        "§23 (SCALE-AND-CHANNEL-TAGGING, alpha_s = instance 2). NEAREST prior atlas-09 anchor: Item "
        "36 (eps_H Spectral Functional Crisis) -- the transport-degree rescoping is a DISTINCT, "
        "FINER claim (a scale/channel separation set by deg(T)=+2, not a cutoff-family ambiguity). | "
        "Low (scale-and-channel re-scope; the multi-sigma reading RELOCATES to the matched channel "
        "as a live prediction -- a strength, not a defined-away tension) |\n"
        f"| {n48} | CORRECTION | SF54 deceleration band q: -0.97 -> +0.81 not reproduced by the "
        "substrate q(z) (S96-W1-VOLOVIK-2FLUID FAIL; q_min_volovik = -0.1115, upper edge "
        "unreachable) -- apparent failure to match the SCALE-FACTOR-54 trajectory | S96 "
        "W1-VOLOVIK-2FLUID | S100a W1-1 (SF54-MAPPING) | FRAME-ROBUST closure: q is a LOG-DERIVATIVE "
        "frame-INVARIANT (Spearman rho = 1.0 between bare and corrected q). The S99/S96 band-MISS is "
        "FRAME-ROBUST -- SF54 is simply the WRONG conformal frame (frame_ratio_median ~ 26.1x faster "
        "Connes-distance frame); the substrate is MOSTLY-ACCELERATING post-fold (q<0 fraction = "
        "0.6677; substrate q median = -0.8662). SF54 axis is CLOSED frame-robust; the surviving "
        "cosmic-time route (C1) is the KV back-reaction channel (CF-S101-W1-QEQ), NOT the SF54 band. "
        "Because q is frame-invariant, ANY observational reconstruction of late-time q(z) "
        "(DESI/Euclid expansion history; SNIa Hubble-flow) BINDS the substrate prediction directly. "
        "Register-of-record: atlas-08-freshness-S100 Q13 (tau-evolution -> cosmic time / C1) + gate "
        "S100a-W1-1-SF54-MAPPING + little-red-dots-synthesis.md (SCALE-FACTOR-54 deceleration "
        "band). | Low (frame-robust closure; band-miss is real and frame-invariant -- the surviving "
        "cosmic-time route is C1/KV back-reaction, not SF54) |\n"
        f"| {n49} | CORRECTION | CGWB acoustic peak as the flagship LISA discriminator (acoustic vs "
        "Companion-null) | S96-OBS-CGWB-PEAK-FREQ | S96 W8-2 / S97 re-pin | GW -> LSS migration: the "
        "acoustic peak FREQUENCY evaporates to GHz+ (f_obs = 8.4835e39 Hz; +28.9 decades above the "
        "optimistic HF-detector ceiling, +42.45 decades above LISA) -- the CGWB peak is a member of "
        "NO GW-detector band (PTA / LISA / LIGO-ET / resonant-HF), GW-detector-sterile. The "
        "falsifier does NOT vanish; it RELOCATES to the correct instrument: the substrate has ONE "
        "frequency scale (M_KK); the fold radiates at it (~1e40 Hz, above every GW detector); the "
        "acoustic IMPRINT lives at the matter-clustering scale (k1 = 0.0193 Mpc^-1) where galaxy "
        "surveys operate. The GW-detector flagship is RETIRED; the LIVE near-term zero-parameter "
        "replacements are at the LSS instrument -- (P4) first-sound BAO ring (inventory Row #72, "
        "S96-OBS-FIRST-SOUND-RING PASS, A_FS = 0.204000, SNR 8.6341 DESI-5yr, NO LCDM counterpart) "
        "and (P5) f.sigma_8 growth suppression (inventory Row #71, product_supp_max = -4.058% @ "
        "z=0.51, S8-relieving). The surviving structural companions (wall=0 null; (A)/(C) "
        "regulator-class split 47.081 OOM) are NON-detector-testable STRUCTURAL-ORTHOGONAL-"
        "COMPANIONS, never co-primary. NOTE: it is the GW-DETECTOR FREQUENCY/peak that migrated, NOT "
        "the acoustic signal -- the ACOUSTIC (A)-class Omega_GW stays LIVE (no retirement of the "
        "acoustic prediction). Register-of-record: falsifier-master-inventory Row #7.audit-3 "
        "(GW->LSS migration) + gate S96-OBS-CGWB-PEAK-FREQ + S98-KAPPA-INDEP-FROM-CGWB-FREQ + "
        "capstone section 7.2. | Low (instrument migration; the flagship RELOCATES from the "
        "GW-detector-sterile peak frequency to the LSS instrument -- BAO ring + f.sigma_8 are the "
        "binding tests) |\n"
    )

    # --- Narrative detail block (mirrors the '### Item 37:' detail form) ---
    narrative = (
        "\n"
        f"### Items {n47}-{n49}: Interpretive-DOF Rescopings (S102 DOF-ledger formalization)\n"
        "\n"
        "These three rows discharge the 3/4 PENDING-formal-row state recorded in "
        "`interpretive-dof-ledger.md` §\"atlas-09 cross-reference reconciliation\". atlas-09's prior "
        "scope ended at S88, so the S92-S100a rescopings lived in `atlas-08-freshness-S100` + "
        "`falsifier-master-inventory.md` with their formal atlas-09 rows PENDING. The DOF-ledger's "
        "W5-5 verdict (INFO; 1/4 resolved -- only Item 37 / w_0) named each PENDING row's "
        "register-of-record; these CORRECTION rows transcribe those rescopings into the formal "
        "atlas-09 row form so the cross-references resolve 4/4. Substrate-first framing preserved: "
        "each rescoping records WHERE the falsifier MOVED (matched-channel relocation; frame-invariant "
        "band-miss; instrument migration), never that it was defined out of existence "
        "(`feedback_reporting-framing.md`).\n"
        "\n"
        f"#### Item {n47}: alpha_s Transport-Degree Scale-and-Channel Separation (S92 AH-TR-1 -> S93 W7-1)\n"
        "\n"
        "The single-Planck-pivot comparison gave alpha_s^substrate = "
        f"{alpha_s_substrate_distance_1} vs Planck-2018 (-0.0045 +/- 0.0067) = -12.146 sigma "
        "(13.99 sigma against Aiola-2020), read as a 'first multi-sigma falsifier'. The substrate "
        "value was being compared against the WRONG datum -- a BZ-scale O(M_KK) running put up "
        "against the CMB pivot. The framework carries TWO scale-separated alpha_s observables: a "
        f"substrate-distance running (alpha_s_substrate_distance_1 = {alpha_s_substrate_distance_1}, "
        f"s=3 Mellin pole) and a Goldstone-pivot running (alpha_s_pivot_goldstone = "
        f"{alpha_s_pivot_goldstone}, CMB pivot, +0.67 sigma vs Planck). WHICH a detector measures is "
        "set by the single computable transport degree deg(T_BZ->pivot). S93 W7-1 RESOLVED deg=+2 "
        "NON-SCALAR (w(L_max).kappa(k) factorization_holds=False), so the scalar-transport (-12.146 "
        "sigma) reading is the FALSIFIED leaf -- it RELOCATES off-pivot as a SCALE-MISMATCH, not a "
        "falsification. The -12.146 sigma MOVED to the matched substrate-sensitivity channel "
        "(CMB-S4 2030, sigma_alpha_s ~ 2.3e-3 => ~37 sigma reach; CMB-HD 2035, sigma_alpha_s ~ "
        "1.1e-3 => ~78 sigma reach) where alpha_s^substrate is a live ~34-sigma-class discriminator. "
        "This is a DISTINCT, FINER claim than Item 36 (eps_H Spectral Functional Crisis, the "
        "cutoff-family n_s/alpha_s SCHEME-dependence): a scale/channel separation set by deg(T)=+2, "
        "not a cutoff-family sign-ambiguity. Register-of-record: falsifier-master-inventory Row "
        "#3.rescope-AH-TR-1 + canonical_constants alpha_s_substrate_distance_1 / "
        "alpha_s_pivot_goldstone + cross-pillar-bridge-corpus.md §23 (SCALE-AND-CHANNEL-TAGGING, "
        "alpha_s = instance 2). Binding test: CMB-S4 2030 / CMB-HD 2035 (substrate-sensitivity "
        "channel).\n"
        "\n"
        f"#### Item {n48}: SF54 Frame-Robust Closure (S96 W1-VOLOVIK-2FLUID -> S100a W1-1)\n"
        "\n"
        "The SCALE-FACTOR-54 gate carried a deceleration band q: -0.97 -> +0.81 (Connes-distance "
        "proxy). The substrate q(z) did NOT reproduce it (S96-W1-VOLOVIK-2FLUID FAIL; q_min_volovik "
        "= -0.1115, upper edge unreachable). The S100a LRD re-scope (gate S100a-W1-1-SF54-MAPPING) "
        "showed q is a LOG-DERIVATIVE frame-INVARIANT (Spearman rho = 1.0 between bare and corrected "
        "q), so the band-MISS is FRAME-ROBUST -- SF54 is simply the WRONG conformal frame "
        "(frame_ratio_median ~ 26.1x faster Connes-distance frame). The substrate is "
        "MOSTLY-ACCELERATING post-fold (q<0 fraction = 0.6677; substrate q median = -0.8662). The "
        "SF54 axis is CLOSED frame-robust; the surviving cosmic-time route (C1) is the KV "
        "back-reaction channel (CF-S101-W1-QEQ), NOT the SF54 band. Because q is a frame-invariant "
        "log-derivative, ANY observational reconstruction of late-time q(z) (DESI/Euclid expansion "
        "history; SNIa Hubble-flow) BINDS the substrate prediction directly -- frame choice cannot "
        "rescue a band-miss. Register-of-record: atlas-08-freshness-S100 Q13 (tau-evolution -> "
        "cosmic time / C1) + gate S100a-W1-1-SF54-MAPPING + little-red-dots-synthesis.md. Binding "
        "test: DESI/Euclid expansion-history q(z) + SNIa Hubble-flow (frame-invariant).\n"
        "\n"
        f"#### Item {n49}: CGWB GW->LSS Migration (S96-OBS-CGWB-PEAK-FREQ -> S96 W8-2 / S97 re-pin)\n"
        "\n"
        "The CGWB was the flagship LISA discriminator (acoustic vs Companion-null). But the acoustic "
        "peak FREQUENCY evaporates to GHz+: S96-OBS-CGWB-PEAK-FREQ FAIL (f_obs = 8.4835e39 Hz; +28.9 "
        "decades above the optimistic HF-detector ceiling, +42.45 decades above LISA). The CGWB peak "
        "is a member of NO GW-detector band (PTA / LISA / LIGO-ET / resonant-HF) -- GW-detector-"
        "sterile. The falsifier does NOT vanish; it RELOCATES to the correct instrument. The "
        "substrate has ONE frequency scale (M_KK); the fold radiates at it (~1e40 Hz, above every GW "
        "detector); the acoustic IMPRINT lives at the matter-clustering scale (k1 = 0.0193 Mpc^-1) "
        "where galaxy surveys operate. The GW-detector flagship is RETIRED; the LIVE near-term "
        "zero-parameter replacements at the LSS instrument are (P4) the first-sound BAO ring "
        "(inventory Row #72, S96-OBS-FIRST-SOUND-RING PASS; A_FS = 0.204000 = c2^2/c1^2 at k1 = "
        "0.0193150 Mpc^-1, SNR 8.6341 DESI-5yr / 5.0789 DESI-DR1, NO LCDM counterpart) and (P5) "
        "f.sigma_8 growth suppression (inventory Row #71, S96-OBS-FSIGMA8-FORECAST INFO; "
        "product_supp_max = -4.058% @ z=0.51, S8-relieving, sigma_DESI5yr = 1.013). The surviving "
        "structural companions (wall=0 null; (A)/(C) regulator-class split 47.081 OOM) are "
        "NON-detector-testable STRUCTURAL-ORTHOGONAL-COMPANIONS, never co-primary. It is the "
        "GW-DETECTOR FREQUENCY/peak that migrated, NOT the acoustic signal: the ACOUSTIC (A)-class "
        "Omega_GW stays LIVE (no retirement; no D09 needed for the acoustic prediction itself -- the "
        "migration is of the GW-detector flagship FREQUENCY to the LSS instrument). Register-of-"
        "record: falsifier-master-inventory Row #7.audit-3 (GW->LSS migration) + gate "
        "S96-OBS-CGWB-PEAK-FREQ + S98-KAPPA-INDEP-FROM-CGWB-FREQ + capstone section 7.2. Binding "
        "test: DESI/Euclid P(k) -- first-sound BAO ring (Row #72) + f.sigma_8 (Row #71).\n"
    )
    return master, narrative


def build_atlas_text(atlas_text: str, master: str, narrative: str,
                     n49: int) -> str:
    """Insert the master-table block + narrative block, and bump the header/footer totals.

    Insertion point: the master block is inserted immediately BEFORE the final footer line
    '**Total retractions/corrections through S88: 46**' (which closes the document); the narrative
    block is inserted right after the master block. The final-total footer line is then updated to
    name the new top item. The header 'Total entries' / 'Scope' lines are updated to S102."""
    new_total = n49  # (local) the new highest item number
    n_new = 3        # (local)

    # The final footer line (a bolded total, at end of file).
    footer_pat = re.compile(
        r"\*\*Total retractions/corrections through S88: 46\*\*.*?$",
        flags=re.MULTILINE | re.DOTALL,
    )
    m = footer_pat.search(atlas_text)  # (local)
    if m is None:
        # Footer not found -> append at end (defensive; verify will catch any anomaly).
        return atlas_text + master + narrative

    insert_at = m.start()  # (local)
    block = (
        master
        + narrative
        + "\n---\n\n"
        f"**Total retractions/corrections through S102: {new_total}** "
        f"(46 through S88 + {n_new} S92-S100a interpretive-DOF rescopings, Items "
        f"{new_total - n_new + 1}-{new_total}: alpha_s transport-degree, SF54 frame-robust closure, "
        "CGWB GW->LSS migration).\n\n"
        "*(Items 1-46 footer, retained verbatim below.)*\n\n"
    )
    new_text = atlas_text[:insert_at] + block + atlas_text[insert_at:]

    # Bump the header 'Total entries' and 'Scope' + 'Updated' lines.
    new_text = new_text.replace(
        "**Scope**: Sessions 1-88",
        "**Scope**: Sessions 1-88 (master baseline); S92-S100a interpretive-DOF rescopings "
        f"appended (Items {new_total - n_new + 1}-{new_total})",
        1,
    )
    new_text = new_text.replace(
        "**Total entries**: 46 (34 baseline through S66 + 12 new S67-S88)",
        f"**Total entries**: {new_total} (34 baseline through S66 + 12 new S67-S88 + {n_new} "
        "S92-S100a interpretive-DOF rescopings)",
        1,
    )
    return new_text


def write_atomic_with_fsync(path: Path, text: str) -> None:
    """Write text to a temp file, fsync, then atomic-replace the target."""
    tmp = path.with_suffix(path.suffix + ".tmp")  # (local)
    data = text.encode("utf-8")  # (local)
    with open(tmp, "wb") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


# ---------------------------------------------------------------------------
# Section 5b — W5-5 resolution check (AFTER-pattern verify step)
# ---------------------------------------------------------------------------

def count_atlas09_resolutions(atlas_text: str) -> tuple[int, dict]:
    """Re-run the DOF-ledger W5-5 atlas-09 cross-reference resolution check.

    The 4 DOF-ledger rescopings each claim an atlas-09 formal CORRECTION row. A rescoping RESOLVES
    iff atlas-09 contains a formal CORRECTION row carrying its discriminating marker:
      row 1 (alpha_s transport-degree)      -> marker 'transport-degree' present in a CORRECTION context
      row 2 (SF54 frame-robust)             -> marker 'SF54' + 'frame-robust' (frame-robust closure row)
      row 3 (CGWB GW->LSS migration)        -> marker 'GW->LSS' (the migration)
      row 4 (w_0 R_918->R_842)              -> Item 37 (the pre-existing clean CORRECTION row)
    Returns (count, per_row_dict)."""
    checks = {}  # (local)
    # Row 4: w_0 R_918 -> R_842 (Item 37; pre-existing). Match the rectangle-migration claim.
    checks["row4_w0_R918_R842"] = bool(
        re.search(r"R_918", atlas_text) and re.search(r"R_842", atlas_text)
        and re.search(r"Rectangle Migration", atlas_text)
    )
    # Row 1: alpha_s transport-degree scale-and-channel separation (new CORRECTION row).
    checks["row1_alpha_s_transport_degree"] = bool(
        re.search(r"transport-degree", atlas_text)
        and re.search(r"deg=\+2 NON-SCALAR", atlas_text)
        and re.search(r"CORRECTION", atlas_text)
    )
    # Row 2: SF54 frame-robust closure (new CORRECTION row).
    checks["row2_SF54_frame_robust"] = bool(
        re.search(r"SF54", atlas_text)
        and re.search(r"[Ff]rame-[Rr]obust", atlas_text)
        and re.search(r"Spearman rho = 1\.0", atlas_text)
    )
    # Row 3: CGWB GW->LSS migration (new CORRECTION row).
    checks["row3_CGWB_GW_to_LSS"] = bool(
        re.search(r"GW->LSS", atlas_text)
        and re.search(r"GW-detector-sterile", atlas_text)
        and re.search(r"first-sound BAO ring", atlas_text)
    )
    count = sum(1 for v in checks.values() if v)  # (local)
    return count, checks


# ---------------------------------------------------------------------------
# Section 6 — Compute (orchestration of the AFTER-pattern)
# ---------------------------------------------------------------------------

def compute() -> dict:
    atlas_pre = ATLAS09.read_text(encoding="utf-8")  # (local)
    pre_sha = sha256_of_text(atlas_pre)              # (local)
    dof_text = DOF_LEDGER.read_text(encoding="utf-8")  # (local)
    dof_sha = sha256_of_text(dof_text)               # (local)

    # --- pre-write baseline resolution (should be 1/4: only Item 37 / w_0) ---
    pre_count, pre_checks = count_atlas09_resolutions(atlas_pre)  # (local)

    # --- scan next-free row numbers (runtime; plan-text-drift aware) ---
    next_free, max_item = scan_next_free_rows(atlas_pre)  # (local)
    n47, n48, n49 = next_free  # (local)
    drift = (max_item != PLAN_PINNED_ITEM_COUNT)  # (local) True if scope drifted from S1-88/46

    # collision guard: the three new numbers must not already be present.
    existing_nums = set()  # (local)
    for m in re.finditer(r"^\|\s*(\d+)\s*\|", atlas_pre, flags=re.MULTILINE):
        existing_nums.add(int(m.group(1)))
    collision = any(n in existing_nums for n in (n47, n48, n49))  # (local)

    # --- build the rows text in memory (AFTER-pattern step 1) ---
    master, narrative = build_rows_text(n47, n48, n49)
    rows_span = master + narrative  # (local)
    rows_span_sha = sha256_of_text(rows_span)  # (local)

    # --- assemble full new atlas text ---
    new_atlas = build_atlas_text(atlas_pre, master, narrative, n49)  # (local)

    # idempotency: if the new rows are ALREADY present (re-run), do not double-append.
    already_present = bool(
        re.search(r"Interpretive-DOF Rescopings", atlas_pre)
        and re.search(r"alpha_s Transport-Degree Scale-and-Channel Separation", atlas_pre)
    )

    if collision:
        # Do NOT write; emit FAIL (mechanical-closure: no corrective rewrite).
        return {
            "value": "row-number-collision",
            "verdict": "FAIL",
            "pre_sha": pre_sha, "dof_sha": dof_sha, "rows_span_sha": rows_span_sha,
            "resolution_count": pre_count, "next_free": next_free, "max_item": max_item,
            "drift": drift, "collision": collision, "checks": pre_checks,
            "post_sha": pre_sha,
        }

    if already_present:
        # Idempotent re-run: file already carries the rows; verify on the on-disk state.
        post_atlas = atlas_pre  # (local)
    else:
        write_atomic_with_fsync(ATLAS09, new_atlas)  # (local) AFTER-pattern step 2
        post_atlas = ATLAS09.read_text(encoding="utf-8")  # (local) step 3: re-read

    post_sha = sha256_of_text(post_atlas)  # (local)

    # --- verify (AFTER-pattern step 3): rows present AND resolution count 4/4 ---
    post_count, post_checks = count_atlas09_resolutions(post_atlas)  # (local)
    rows_present = (
        ("transport-degree" in post_atlas)
        and ("SF54" in post_atlas)
        and ("GW->LSS" in post_atlas)
        # narrative detail sections present
        and ("alpha_s Transport-Degree Scale-and-Channel Separation" in post_atlas)
        and ("SF54 Frame-Robust Closure" in post_atlas)
        and ("CGWB GW->LSS Migration" in post_atlas)
    )  # (local)
    verify = bool(rows_present and (post_count == RESOLUTION_TARGET) and (not collision))  # (local)

    verdict = "PASS" if verify else "FAIL"
    if drift and verify:
        # scope drifted but rows authored at runtime next-free numbers + 4/4 -> INFO per rubric
        verdict = "INFO"

    value = (
        f"{post_count}/{N_DOF_RESCOPINGS}-resolved;"
        f"rows=[{n47}-alpha_s-transport-deg+2,{n48}-SF54-frame-robust-q-median-0.8662,"
        f"{n49}-CGWB-GW-to-LSS];pre={pre_count}/{N_DOF_RESCOPINGS};"
        f"verify={verify};drift={drift}"
    )

    return {
        "value": value,
        "verdict": verdict,
        "pre_sha": pre_sha, "dof_sha": dof_sha, "rows_span_sha": rows_span_sha,
        "post_sha": post_sha,
        "resolution_count": post_count, "pre_resolution_count": pre_count,
        "next_free": next_free, "max_item": max_item,
        "drift": drift, "collision": collision,
        "rows_present": rows_present, "verify": verify, "checks": post_checks,
        "pre_checks": pre_checks,
    }


# ---------------------------------------------------------------------------
# Section 7 — verdict payload + 4-tuple + npz
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          extra_rows=None) -> dict:
    payload = {
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
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


def main() -> int:
    t0 = time.time()  # (local)

    # 1. input pins (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)

    # 1b. dual SHAs
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. compute (AFTER-pattern: build -> write -> re-read -> verify)
    res = compute()
    value = res["value"]
    verdict = res["verdict"]

    # 3. extend the audit pinmap with the runtime SHAs declared in the plan
    #    (audit_sha256_inputs = [script, dof_ledger, atlas09_pre, rows_span, pinmap]).
    #    Recompute audit_sha over the FULL declared input set so the verdict's audit SHA
    #    binds the rows-span + pre-write atlas SHA (per the plan audit_discriminators block).
    extended_pins = dict(pins)  # (local)
    extended_pins["__atlas09_pre_write_sha"] = res["pre_sha"]
    extended_pins["__interpretive_dof_ledger_sha"] = res["dof_sha"]
    extended_pins["__rows_span_sha"] = res["rows_span_sha"]
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL, extended_pins)
    print(f"  audit_sha256 (extended w/ atlas-pre + dof + rows-span): {audit_sha[:16]}...")

    print("\n=== resolution check (W5-5 re-run) ===")
    print(f"  pre-write resolution:  {res['pre_resolution_count'] if 'pre_resolution_count' in res else res['resolution_count']}/{N_DOF_RESCOPINGS}")
    print(f"  post-write resolution: {res['resolution_count']}/{N_DOF_RESCOPINGS}")
    print(f"  per-row checks: {json.dumps(res['checks'])}")
    print(f"  next-free rows: {res['next_free']}  (max prior item={res['max_item']})")
    print(f"  drift={res['drift']}  collision={res['collision']}  rows_present={res.get('rows_present')}")
    print(f"  verify={res.get('verify')}")

    # 4. npz: store pre-write atlas SHA + rows-span SHA + the 4/4 resolution count + 3 row numbers
    SESSION_OUT_DIR.mkdir(parents=True, exist_ok=True)
    np.savez(
        OUT_NPZ,
        atlas09_pre_write_sha=res["pre_sha"],
        atlas09_post_write_sha=res["post_sha"],
        interpretive_dof_ledger_sha=res["dof_sha"],
        rows_span_sha=res["rows_span_sha"],
        resolution_count=res["resolution_count"],
        resolution_target=RESOLUTION_TARGET,
        n_dof_rescopings=N_DOF_RESCOPINGS,
        new_row_numbers=np.array(res["next_free"], dtype=np.int64),
        max_prior_item=res["max_item"],
        plan_pinned_item_count=PLAN_PINNED_ITEM_COUNT,
        drift=res["drift"],
        collision=res["collision"],
        verify=res.get("verify", False),
        verdict=verdict,
        per_row_check_keys=np.array(list(res["checks"].keys())),
        per_row_check_vals=np.array([res["checks"][k] for k in res["checks"]], dtype=bool),
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        alpha_s_substrate_distance_1=alpha_s_substrate_distance_1,
        alpha_s_pivot_goldstone=alpha_s_pivot_goldstone,
    )
    print(f"\n  npz -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # 5. 4-tuple + verdict payload (exactly ONE emission)
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)
    extra = [
        f"# rows_span_sha256={res['rows_span_sha']} atlas09_pre_write_sha256={res['pre_sha']} "
        f"# {GATE_ID} register-authoring provenance (3 CORRECTION rows, Items {res['next_free'][0]}-{res['next_free'][2]})",
    ]
    print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0  # verdict is data; script health == 0 regardless of PASS/FAIL/INFO


if __name__ == "__main__":
    sys.exit(main())
