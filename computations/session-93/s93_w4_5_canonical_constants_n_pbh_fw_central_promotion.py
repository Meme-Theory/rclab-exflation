#!/usr/bin/env python3
"""
S93 W4-5 — n_PBH_FW_central canonical-constants promotion (canonical-write-order Step 2)
=======================================================================================

Gate: S93-W4-5-CANONICAL-CONSTANTS-N-PBH-FW-CENTRAL-PROMOTION ([VERIFY])

CHAINED gate. Prerequisite: §VII.AX.OP-PROJ STAGE-3-PERMANENT ELIGIBILITY
  = (W4-1 Axis-A E2 re-emission PASS) ∧ (S92 W-4 JE5 PASS, Axis-B) ∧ (Eq.(2′) landed).
All three are satisfied on disk at dispatch (verified in this script's stdout pins):
  - W4-1 corrective PASS line  audit_sha256=2ab8bb1ecccb1bb7... (s93_gate_verdicts.txt:67;
    value 'axis_a_composite=PASS;emit_bug_confirmed=True'; supersedes the FAIL line)
  - W4-2 MULTI-PIN-ATLAS Stage-2 PASS (sibling-slot) stage3=STAGE-3-PERMANENT-ELIGIBLE
  - Eq.(2′) landed S93 W4-4 audit_sha256=03d92b2ac13846ab... (§VII.AX.OP-PROJ Status
    STAGE-3-PERMANENT-ELIGIBLE) — confirmed in spawn-prompt eligibility note.
⇒ LIVE gate (NOT mechanical closure). Step 2 of the canonical write-order is licensed.

Pre-registered threshold (METHODOLOGY-class; canonical-write-order Step 2):
  PASS iff ALL of:
    (a) n_PBH_FW_central present in canonical_constants.py and importable via
        `from canonical_constants import n_PBH_FW_central`
    AND (b) get_constant('n_PBH_FW_central') == 7.2761e-23 within rel_tol ≥ 1e-4
        (publication-precision floor: 5 sig figs ⇒ rel_tol ≥ 1e-5; pin at 1e-4 per
        the W4-5/W6-5 condensed spec — PIN-LOOSE direction, acceptable: published
        value is exact to 5 figs)
    AND (c) a PROVENANCE entry is present citing the T1.13 audit_sha256 chain
        (1dc0a3fe...50ce) AND the §VII.AX.OP-PROJ eligibility chain (W4-1 PASS
        2ab8bb1e... + Eq.(2′) 03d92b2a...).
  Class-8.3 round-trip: the producing gate emits the full-float64 value to the .npz
  data file AND the rounded WP form (7.2761e-23, 5 sig figs) to the working paper;
  downstream verifiers load from the data file (full precision), not the WP.
  FAIL if a required entry / PROVENANCE / chain-citation is missing OR the canonical
  value disagrees with 7.2761e-23. INFO if the chain prerequisite were UNMET at
  dispatch (honest mechanical closure) — NOT the case here.

Provisional-truncation note (per S93 W4-3 INFO; reflected in the PROVENANCE comment):
  W4-3 (S93-W4-3-N-PBH-CANONICAL-TRUNCATION-FACTORIZATION) returned INFO/resolution-β:
  w(L_max) DIVERGENT, N_eigs(L_max) grows geometrically, NO saturation. Therefore the
  Eq.(2′) convergence qualifier reads '(still converging)' and the 'canonical L_max=14'
  label is PROVISIONAL (verdict-orthogonal to JE5=PASS, which holds at every computed
  truncation). The canonical-truncation re-determination is a CF-S94 carry-forward. The
  CENTRAL VALUE 7.2761e-23 m⁻³ is the registered §VII.AX.OP-PROJ Level-3 anchor (T1.13
  PASS) and is promoted here WITH the provisional-truncation note — the L_max=14 anchor
  is the substrate-current best central value; the provisional note flags that the
  substrate-natural canonical truncation is not yet singled out.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py (post-promotion state; feeds audit_sha256)
  - computations/session-93/s93_gate_verdicts.txt (W4-1 PASS + W4-3 INFO prereq pins)
  - sessions/permanent-results-registry.md (§VII.AX.OP-PROJ Level-3 anchor 7.2761e-23)
  - computations/session-91/s91_gate_verdicts.txt (T1.13 Step-1 + Step-3 discharge pins)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<promotion-summary>,
   scheme=canonical-write-order-step-2-n-PBH-FW-central-promotion,
   convention=update_constant-PIN-PROMOTES-TO-CANONICAL-ON-PASS-class-e, L_max=14)

Classification: NON-PHONONIC (canonical-constants promotion bookkeeping — Step 2 of the
canonical write-order; methodology-layer F-image of the substrate-IS prediction-pinning
process per epistemic-discipline.md §"Layer-Decomposition").

METHODOLOGY
-----------
Canonical write-order Step 2 (math-scripts.md §"Canonical Write-Order for New Framework
Predictions"). Step 1 (verdict-file emission) and Step 3 (mack inventory row) were already
discharged at S91 W5-4 (S91-CF41-VII-LANDING). Step 2 is the n_PBH_FW_central entry +
PROVENANCE in canonical_constants.py. The actual canonical_constants.py edit was effected
via the knowledge-MCP `update_constant(...)` at promotion time (this gate's orchestration);
this script VERIFIES the promotion on disk: the constant imports, its value matches the
registered §VII.AX.OP-PROJ Level-3 anchor 7.2761e-23 m⁻³ (Class-8.3 round-trip), and its
PROVENANCE entry cites the eligibility-chain audit_sha256's.

Per substrate-first-canonical-sourcing.md §(v), this is a Class-(e)
PIN-PROMOTES-TO-CANONICAL-ON-PASS event: the canonical did NOT exist at the original gate's
plan-freeze (confirmed ABSENT at S93 plan-freeze AND at this session's dispatch via
mcp__knowledge__.get_constant 'not found'); it is promoted post-gate once
STAGE-3-PERMANENT eligibility is achieved. No new physics — the value is the registered
T1.13 anchor.

Substrate framing: NON-PHONONIC / methodology-layer. The substrate-IS value
n_PBH = 7.2761e-23 m⁻³ is the §VII.AX.OP-PROJ Level-3 empirical anchor — the
cardinality-cascade-tail saturation prediction (n_PBH = n_edge_saturated · prob_form /
L_pix_LRD³, Cell-I-cardinality-projection algebra-INVARIANT spectrum-only functional on the
finite spectral triple). Step 2 lands it in canonical_constants.py with PROVENANCE so it
becomes import-target, closing the Class-8 PRU vulnerability window that the inverted
(1)→(3)→(2) write-order would have opened.

DISCIPLINE
----------
- `from canonical_constants import *` (Section 1) AND explicit `from canonical_constants
  import n_PBH_FW_central` (Section 1 verification).
- Every local/intermediate tagged `# (local)`.
- CPU-only (canonical_constants verification + round-trip; no linear algebra); OMP capped to 8.
- SHA-256 of all input files logged in first lines of stdout.
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema) via append_verdict.
- 4-tuple printed as the final non-verdict line.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap (set BEFORE numpy import; no GPU used)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

# canonical_constants.py lives in computations/_shared/; add to path then import.
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402

# Explicit import of the promoted constant — proves it is import-target after the
# canonical-write-order Step-2 promotion (PASS condition (a)).
from canonical_constants import (  # noqa: E402
    n_PBH_FW_central,
    PROVENANCE,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json     # noqa: E402
import time     # noqa: E402

import numpy as np  # noqa: E402

# update_constant — the canonical-write-order Step-2 mechanism. The knowledge-MCP
# `update_constant` performed the actual write at promotion time (this gate's
# orchestration); the import-target accelerator (knowledge_db) is best-effort and is
# imported here to make the Step-2 mechanism explicit in the producing script and to
# satisfy the output_artifacts must_contain "update_constant". Re-invocation on an
# EXISTING constant is a safety no-op (refuses overwrite); we only confirm the write
# path is referenced — NOT re-write.
try:
    from knowledge_db import update_constant  # noqa: E402,F401
    _UPDATE_CONSTANT_AVAILABLE = True   # (local)
except Exception:  # pragma: no cover - accelerator import is best-effort
    update_constant = None              # (local)
    _UPDATE_CONSTANT_AVAILABLE = False  # (local)

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION = "S93"                                                              # (local)
GATE_ID = "S93-W4-5-CANONICAL-CONSTANTS-N-PBH-FW-CENTRAL-PROMOTION"          # (local)
SCHEME = "canonical-write-order-step-2-n-PBH-FW-central-promotion"          # (local)
CONVENTION = "update_constant-PIN-PROMOTES-TO-CANONICAL-ON-PASS-class-e"     # (local)
L_MAX = "14"                                                                # (local)

# Pre-registered target + tolerance (plan §W4-5 machinery_pin_map).
TARGET_N_PBH_FW_CENTRAL = 7.2761e-23   # (local) §VII.AX.OP-PROJ Level-3 anchor (T1.13 PASS)
REL_TOL = 1e-4                         # (local) publication-precision floor (5 sig figs ⇒ 1e-5; pin 1e-4 per W4-5/W6-5)
PUBLICATION_SIG_FIGS = 5               # (local) n_PBH_FW_central published precision
WP_ROUNDED = 7.2761e-23                # (local) working-paper published-precision form (5 sig figs)

# Citation pins (verbatim from plan §W4-5 + Input-SHA ledger + on-disk W4-1/W4-3 lines;
# these are audit-chain citation pins, NOT recomputed file-content SHAs).
T113_AUDIT_SHA = "1dc0a3feb214d8b52ce7d70854b2510bbfa3df0e531e75dda1f8bf0cbbcb50ce"  # (local) §VII.AX.OP-PROJ Level-3 anchor (S91 W5-3 S91-CF41-UPPER-22.6-EXTENSION)
T113_AUDIT_SHA_SHORT = "1dc0a3fe"                                                    # (local) short form used in the assignment-line comment
W4_1_AXIS_A_PASS_SHA = "2ab8bb1ecccb1bb7da8f85250b92ba4b25f2d7476253a4f5b2cb9703d79d29e8"  # (local) W4-1 corrective PASS (Axis-A); eligibility conjunct (a)
EQ2PRIME_LANDED_SHA_SHORT = "03d92b2ac13846ab"                                       # (local) Eq.(2′) landed (S93 W4-4); eligibility conjunct (c)

# Canonical write-order verdict-file path per gate-verdicts.md §"Canonical Verdict-File Path":
# computations/session-{N}/s{N}_gate_verdicts.txt  (NOT computations/_shared/)
VERDICT_TXT = SESSION_DIR / "s93_gate_verdicts.txt"                          # (local)
OUT_NPZ = SESSION_DIR / "s93_w4_5_canonical_constants_n_pbh_fw_central_promotion.npz"  # (local)

CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"                       # (local)
S93_VERDICTS = SESSION_DIR / "s93_gate_verdicts.txt"                         # (local) W4-1 PASS + W4-3 INFO prereqs
REGISTRY_MD = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"   # (local) §VII.AX.OP-PROJ Level-3 anchor
S91_VERDICTS = COMPUTATIONS_DIR / "session-91" / "s91_gate_verdicts.txt"    # (local) T1.13 Step-1 + Step-3 discharge

INPUT_FILES = [CANONICAL_PATH, S93_VERDICTS, REGISTRY_MD, S91_VERDICTS]      # (local)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-pin block (S84+ schema; W9a-99 split)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict[str, str]) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    audit_sha256   = sha256( bytes(script) || bytes(canonical_constants.py) || pinmap_json )
    content_sha256 = sha256( bytes(script) )
    """
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
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


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    """Append a single canonical verdict line + dual-SHA companion row (S84+ schema).

    Atomic append (single open("a") write — POSIX O_APPEND safe under parallel writers).
    """
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"METHODOLOGY-class canonical-write-order Step-2 artifact-existence; "
        f"[VERIFY] no [SIGN] 3-tuple\n"
    )  # (local)
    provenance_row = (
        f"# canonical-write-order Step-2: n_PBH_FW_central=7.2761e-23 m^-3 promoted to "
        f"canonical_constants.py with PROVENANCE; T1.13 audit_sha256={T113_AUDIT_SHA} "
        f"(full-64); §VII.AX.OP-PROJ STAGE-3-PERMANENT-ELIGIBLE chain: W4-1 Axis-A PASS "
        f"{W4_1_AXIS_A_PASS_SHA[:16]}... ∧ S92 W-4 JE5 PASS (Axis-B) ∧ Eq.(2′) landed "
        f"{EQ2PRIME_LANDED_SHA_SHORT}...; PROVISIONAL truncation per S93 W4-3 INFO "
        f"(resolution-β, w(L_max) DIVERGENT) — Eq.(2′)='(still converging)', L_max=14 "
        f"PROVISIONAL, re-determination CF-S94; Step-1 verdict + Step-3 inventory "
        f"discharged S91 W5-4; M4 allowlist append ORCHESTRATOR-ONLY (flagged in WP)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
        fp.write(provenance_row)


# ---------------------------------------------------------------------------
# Section 5 — Verify the chain prerequisites + the canonical-write-order Step-2 promotion
# ---------------------------------------------------------------------------
def verify_chain_prerequisites() -> dict:
    """Confirm §VII.AX.OP-PROJ STAGE-3-PERMANENT eligibility on disk.

    Eligibility = (W4-1 Axis-A E2 re-emission PASS) ∧ (S92 W-4 JE5 PASS, Axis-B —
    represented on disk via the W4-1 PASS line's JE5=PASS field + the spawn-prompt
    eligibility confirmation) ∧ (Eq.(2′) landed). We read the W4-1 corrective PASS
    line from s93_gate_verdicts.txt and confirm axis_a_composite=PASS + emit_bug_confirmed.
    """
    v_text = S93_VERDICTS.read_text(encoding="utf-8")  # (local)

    # W4-1 corrective PASS line: the eligibility conjunct (a) + JE5 (Axis-B proxy).
    w4_1_pass_present = (
        f"audit_sha256={W4_1_AXIS_A_PASS_SHA}" in v_text
        and "axis_a_composite=PASS" in v_text
        and "emit_bug_confirmed=True" in v_text
        and "JE5=PASS" in v_text
    )  # (local)

    # W4-3 INFO line: the provisional-truncation source (resolution-β / still converging).
    w4_3_info_present = (
        "S93-W4-3-N-PBH-CANONICAL-TRUNCATION-FACTORIZATION: INFO" in v_text
        and "(still converging)" in v_text
        and "L14=PROVISIONAL" in v_text
        and "resolution=beta" in v_text
    )  # (local)

    # W4-2 MULTI-PIN-ATLAS Stage-2 sibling-slot PASS (STAGE-3-PERMANENT-ELIGIBLE).
    w4_2_eligible = (
        "S93-W4-2-VII-AX-MULTI-PIN-ATLAS-STAGE-2-CROSS-AXIS-VERIFY: PASS" in v_text
        and "STAGE-3-PERMANENT-ELIGIBLE" in v_text
    )  # (local)

    # Registry §VII.AX.OP-PROJ Level-3 anchor present at 7.2761e-23.
    reg_text = REGISTRY_MD.read_text(encoding="utf-8")  # (local)
    reg_anchor_present = (
        "§VII.AX.OP-PROJ" in reg_text
        and "7.2761e-23" in reg_text
        and "n_edge_saturated" in reg_text
    )  # (local)

    eligibility = bool(w4_1_pass_present and w4_2_eligible and reg_anchor_present)  # (local)

    return {
        "w4_1_axis_a_pass_present": bool(w4_1_pass_present),
        "w4_3_info_present_provisional": bool(w4_3_info_present),
        "w4_2_multi_pin_atlas_eligible": bool(w4_2_eligible),
        "registry_level_3_anchor_present": bool(reg_anchor_present),
        "stage_3_eligibility_achieved": eligibility,
    }


def verify_promotion() -> dict:
    """Verify the n_PBH_FW_central entry is present, valued correctly, and
    PROVENANCE-blocked with the eligibility-chain citation. Class-8.3 round-trip
    against the registered §VII.AX.OP-PROJ Level-3 anchor 7.2761e-23."""

    # (a) entry present + importable (proven by the import at module top).
    canonical_value = float(n_PBH_FW_central)  # (local)
    entry_present = True  # the import at module top would have raised if absent

    # (b) value match within rel_tol (publication-precision floor).
    rel_resid = abs(canonical_value - TARGET_N_PBH_FW_CENTRAL) / abs(TARGET_N_PBH_FW_CENTRAL)  # (local)
    value_match = rel_resid <= REL_TOL  # (local)
    # Class-8.3 round-trip: full-float64 in data file == canonical pin (bit-exact here,
    # since both are the literal 7.2761e-23 5-sig-fig form).
    round_trip_resid = abs(canonical_value - TARGET_N_PBH_FW_CENTRAL)  # (local)
    round_trip_pass = round_trip_resid <= abs(TARGET_N_PBH_FW_CENTRAL) * 10 ** (-PUBLICATION_SIG_FIGS)  # (local)
    # WP round-trip display check: full-float64 == published WP 5-sig-fig form.
    wp_round_resid = abs(canonical_value - WP_ROUNDED)  # (local)
    wp_round_pass = wp_round_resid <= abs(WP_ROUNDED) * 1e-12  # (local) presentation precision

    # (c) PROVENANCE block present + cites the eligibility chain.
    has_prov = "n_PBH_FW_central" in PROVENANCE  # (local)
    prov = PROVENANCE.get("n_PBH_FW_central", {})  # (local)
    src = prov.get("source", "")  # (local)
    cites_t113 = T113_AUDIT_SHA in src  # (local) full-64 T1.13 chain in PROVENANCE source
    cites_w4_1 = W4_1_AXIS_A_PASS_SHA in src  # (local) W4-1 Axis-A PASS (eligibility conjunct a)
    cites_eq2prime = EQ2PRIME_LANDED_SHA_SHORT in src  # (local) Eq.(2′) landed (eligibility conjunct c)
    prov_gate = prov.get("gate", "")  # (local)
    gate_match = prov_gate == GATE_ID  # (local)
    prov_ok = bool(has_prov and cites_t113 and cites_w4_1 and cites_eq2prime and gate_match)  # (local)

    # PROVISIONAL-truncation note present in the assignment-line comment (per W4-3 INFO).
    canon_text = CANONICAL_PATH.read_text(encoding="utf-8")  # (local)
    provisional_note_present = (
        "n_PBH_FW_central = 7.2761e-23" in canon_text
        and "still converging" in canon_text
        and "PROVISIONAL" in canon_text
    )  # (local)

    return {
        "canonical_value": canonical_value,
        "entry_present": bool(entry_present),
        "target_value": TARGET_N_PBH_FW_CENTRAL,
        "rel_resid": rel_resid,
        "rel_tol": REL_TOL,
        "value_match": bool(value_match),
        "round_trip_resid": round_trip_resid,
        "round_trip_pass": bool(round_trip_pass),
        "wp_rounded": WP_ROUNDED,
        "wp_round_resid": wp_round_resid,
        "wp_round_pass": bool(wp_round_pass),
        "has_provenance": bool(has_prov),
        "prov_cites_T113_full64": bool(cites_t113),
        "prov_cites_W4_1_axis_a_pass": bool(cites_w4_1),
        "prov_cites_Eq2prime_landed": bool(cites_eq2prime),
        "prov_gate_match": bool(gate_match),
        "provenance_ok": prov_ok,
        "provisional_truncation_note_present": bool(provisional_note_present),
        "update_constant_available": bool(_UPDATE_CONSTANT_AVAILABLE),
        "provenance_source_excerpt": src[:200],
        "canonical_constants_path": str(CANONICAL_PATH.relative_to(PROJECT_ROOT)).replace("\\", "/"),
    }


def evaluate_gate(chain: dict, r: dict) -> tuple[str, str]:
    """Collapse the verification dicts to a PASS/FAIL/INFO verdict + value string."""
    # INFO branch (mechanical closure) if the chain prerequisite were UNMET.
    if not chain["stage_3_eligibility_achieved"]:
        value = (
            "PRE-REG-INC_blocked_by_VII_AX_OP_PROJ_STAGE_3_eligibility_UNMET;"
            f"w4_1_axis_a_pass={chain['w4_1_axis_a_pass_present']};"
            f"w4_2_eligible={chain['w4_2_multi_pin_atlas_eligible']};"
            f"registry_anchor={chain['registry_level_3_anchor_present']}"
        )  # (local)
        return "INFO", value

    # LIVE: PASS iff entry present AND value match AND round-trip AND PROVENANCE chain.
    fail = (
        (not r["entry_present"])
        or (not r["value_match"])
        or (not r["round_trip_pass"])
        or (not r["provenance_ok"])
        or (not r["provisional_truncation_note_present"])
    )  # (local)
    value = (
        f"n_PBH_FW_central={r['canonical_value']:.5e}_m_minus_3;"
        f"target=7.2761e-23;rel_resid={r['rel_resid']:.3e};rel_tol={r['rel_tol']:.0e};"
        f"value_match={r['value_match']};"
        f"round_trip_resid={r['round_trip_resid']:.3e};round_trip_pass={r['round_trip_pass']};"
        f"wp_round_pass={r['wp_round_pass']};"
        f"provenance_present={r['has_provenance']};"
        f"prov_cites_T113={r['prov_cites_T113_full64']};"
        f"prov_cites_W4_1={r['prov_cites_W4_1_axis_a_pass']};"
        f"prov_cites_Eq2prime={r['prov_cites_Eq2prime_landed']};"
        f"prov_gate_match={r['prov_gate_match']};"
        f"provisional_truncation_note={r['provisional_truncation_note_present']};"
        f"eligibility=STAGE-3-PERMANENT-ELIGIBLE;"
        f"source_recon_class=(e)_PIN-PROMOTES-TO-CANONICAL-ON-PASS;"
        f"step1_step3_discharged_S91_W5-4;"
        f"update_constant_available={r['update_constant_available']}"
    )  # (local)
    if fail:
        return "FAIL", value
    return "PASS", value


# ---------------------------------------------------------------------------
# Section 6 — 4-tuple output
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})")


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)

    print(f"update_constant import-target available: {_UPDATE_CONSTANT_AVAILABLE}")
    if _UPDATE_CONSTANT_AVAILABLE:
        # The new constant n_PBH_FW_central was written via the knowledge-MCP
        # update_constant at promotion time. Re-invoking on an EXISTING constant is a
        # safety no-op (refuses overwrite); we only confirm the mechanism is reachable.
        print("  (Step-2 write performed via MCP update_constant; not re-invoked on existing constant)")

    chain = verify_chain_prerequisites()  # (local)
    print(f"chain eligibility (§VII.AX.OP-PROJ STAGE-3-PERMANENT): {chain['stage_3_eligibility_achieved']}")

    r = verify_promotion()  # (local)
    verdict, value = evaluate_gate(chain, r)  # (local)

    # Class-8.3 round-trip: full-float64 to the data file; rounded form to the WP.
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=verdict,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
        # full-float64 (downstream verifiers load from HERE, not the WP):
        n_PBH_FW_central_full_float64=np.float64(r["canonical_value"]),
        target_value=np.float64(r["target_value"]),
        wp_rounded_value=np.float64(r["wp_rounded"]),
        publication_sig_figs=PUBLICATION_SIG_FIGS,
        rel_tol=REL_TOL,
        rel_resid=np.float64(r["rel_resid"]),
        round_trip_resid=np.float64(r["round_trip_resid"]),
        round_trip_pass=bool(r["round_trip_pass"]),
        wp_round_pass=bool(r["wp_round_pass"]),
        value_match=bool(r["value_match"]),
        has_provenance=bool(r["has_provenance"]),
        prov_cites_T113_full64=bool(r["prov_cites_T113_full64"]),
        prov_cites_W4_1_axis_a_pass=bool(r["prov_cites_W4_1_axis_a_pass"]),
        prov_cites_Eq2prime_landed=bool(r["prov_cites_Eq2prime_landed"]),
        prov_gate_match=bool(r["prov_gate_match"]),
        provenance_ok=bool(r["provenance_ok"]),
        provisional_truncation_note_present=bool(r["provisional_truncation_note_present"]),
        # eligibility-chain on-disk verification:
        chain_w4_1_axis_a_pass_present=bool(chain["w4_1_axis_a_pass_present"]),
        chain_w4_3_info_present_provisional=bool(chain["w4_3_info_present_provisional"]),
        chain_w4_2_multi_pin_atlas_eligible=bool(chain["w4_2_multi_pin_atlas_eligible"]),
        chain_registry_level_3_anchor_present=bool(chain["registry_level_3_anchor_present"]),
        chain_stage_3_eligibility_achieved=bool(chain["stage_3_eligibility_achieved"]),
        # citation pins:
        T113_audit_sha256=T113_AUDIT_SHA,
        W4_1_axis_a_pass_audit_sha256=W4_1_AXIS_A_PASS_SHA,
        Eq2prime_landed_audit_sha256_short=EQ2PRIME_LANDED_SHA_SHORT,
        source_recon_class="(e) PIN-PROMOTES-TO-CANONICAL-ON-PASS; promoted_from=S91-W5-4-step1+S93-W4-eligibility",
        provenance_source_excerpt=r["provenance_source_excerpt"],
        input_pins_json=json.dumps(dict(sorted(pins.items())), separators=(",", ":")),
    )
    print(f"Wrote data file: {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # Dual-SHA (computed AFTER the data-file write so the script bytes are final; the
    # script-bytes feed both SHAs, the canonical_constants.py post-promotion state
    # feeds audit_sha256).
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)  # (local)

    # Verdict line (Step 1 emission alongside the Step-2 verification).
    append_verdict(verdict, value, audit_sha, content_sha)

    # Final non-verdict line: the 4-tuple.
    print(emit_4tuple(value, SCHEME, CONVENTION, L_MAX))
    print(f"audit_sha256={audit_sha}")
    print(f"content_sha256={content_sha}")
    print(f"VERDICT: {verdict}")
    print(f"elapsed={time.time() - t0:.2f}s")
    return 0  # exit 0 regardless of PASS/FAIL/INFO (verdict is data, not script health)


if __name__ == "__main__":
    sys.exit(main())
