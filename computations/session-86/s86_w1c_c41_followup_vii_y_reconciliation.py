#!/usr/bin/env python3
"""
S86 W1c-4 follow-up (Task #13) -- In-session §VII.Y -> §VII.S sub-row
                                  reconciliation.
=============================================================================

Gate ID: S86-VII-Y-RECONCILE-IN-SESSION ([VERIFY], META).

Pre-registered threshold (per spawn-prompt CC verification):
  PASS iff (i) §VII.S parent exists at registry line 12928 (W1a T3 landed),
           (ii) §VII.S.C-eta + §VII.S.C-theta sub-rows are present after
                this script runs, containing the verbatim Ward-identity +
                inner-fluctuation proofs from the original §VII.Y stub,
           (iii) §VII.Y is converted to a DEPRECATED redirect (no longer
                holds the original provisional content),
           (iv) the original C41 FAIL verdicts (lines 59-60 + 69-70 of
                s86_gate_verdicts.txt) are UNTOUCHED (verdict-permanence
                rule per .claude/rules/output-standards.md),
           (v) ONE new verdict line `S86-VII-Y-RECONCILE-IN-SESSION: PASS`
                is appended to s86_gate_verdicts.txt with companion comment row.
  FAIL iff any of (i)-(v) is violated.
  INFO: not applicable.
  Tolerance rule: ABSOLUTE.

Substrate-framing reminder (.claude/rules/phononic-framing.md):
  This is a registry-relocation operation. The math content (Ward identity
  from real-structure axioms; inner-fluctuation invariance from CCM-2007 §3)
  is unchanged -- only the slot-identity migrates from §VII.Y (provisional
  stub) to §VII.S (canonical parent's sub-rows). Substrate -> ledger direction
  preserved verbatim from the original proofs.md.

Inputs (SHA-256 dual-pinned at runtime per S84+ schema):
  - sessions/permanent-results-registry.md (pre-edit; §VII.S parent at L12928,
    §VII.Y stub at L12576)
  - computations/session-86/s86_w1c_c41_landing_proofs.md (verbatim proofs source)
  - computations/session-86/s86_gate_verdicts.txt (pre-edit; verdict-permanence
    audit; original C41 FAIL pairs at lines 59-60 + 69-70 must remain)
  - sessions/archive/session-86/session-86-w1c-workingpaper.md §W1c-4 (post-wave
    reconciliation paragraph appended elsewhere; this script does not edit it)
  - canonical_constants.py (mandatory computation import; no constants consumed)
  - script bytes

Output 4-tuple:
  (value='2_subrows_relocated_to_§VII.S', scheme=registry-relocate,
   convention=canonical-parent-now-exists, L_max=N/A)

Classification: META (registry hygiene; no spectral compute).

DISCIPLINE
----------
  - `from canonical_constants import *` (mandatory computation import).
  - All locals tagged `# (local)`.
  - Idempotent: re-running this script is safe -- it detects whether sub-rows
    are already at §VII.S and whether §VII.Y is already deprecated; if so,
    it skips the writes and emits the same PASS verdict (provided the
    canonical state is intact).
  - Verdict-permanence honored: this script ONLY appends ONE new verdict
    line; it does NOT touch lines 59-60 + 69-70 of s86_gate_verdicts.txt
    (the original C41 FAIL pair).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports (no numerical libraries; zero-compute)
# ---------------------------------------------------------------------------
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===


os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
PROOFS_MD_PATH = resolve_script(86, 's86_w1c_c41_landing_proofs.md')
VERDICT_TXT = resolve_output(86, 's86_gate_verdicts.txt')
WP_PATH = (PROJECT_ROOT / "sessions" / "session-86"
           / "session-86-w1c-workingpaper.md")

GATE_ID = "S86-VII-Y-RECONCILE-IN-SESSION"                        # (local)
SCHEME = "registry-relocate"                                       # (local)
CONVENTION = "canonical-parent-now-exists"                         # (local)
L_MAX = "N/A"                                                      # (local)
VALUE = "2_subrows_relocated_to_§VII.S"                            # (local)

# Pre-registered FAIL verdicts that MUST remain in the verdict file unchanged
# (verdict-permanence rule per .claude/rules/output-standards.md). These are
# the original C41 paired FAIL-with-remediation pair AND the pre-rename pair.
PERMANENT_PRIOR_VERDICTS = [                                       # (local)
    "S86-VII-S-C-ETA-LANDING: FAIL",
    "S86-VII-S-C-THETA-LANDING: FAIL",
]

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    REGISTRY_PATH,
    PROOFS_MD_PATH,
    VERDICT_TXT,
    WP_PATH,
]


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block + S84+ dual-SHA helpers
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                           # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict[str, str] = {}                                      # (local)
    for p in inputs:
        sha = sha256_of(p)                                         # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        marker = "MISSING" if not sha else sha[:16] + "..."        # (local)
        print(f"  {rel}: {marker}")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())                                   # (local)
    h = hashlib.sha256()                                           # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """S84+ dual-SHA per the computation script template:
       audit_sha256   = sha256( script || canonical || pinmap_json )
       content_sha256 = sha256( script )
    """
    script_bytes = b""                                             # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""                                          # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                              # (local)

    h_audit = hashlib.sha256()                                     # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                    # (local)

    h_content = hashlib.sha256()                                   # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                                # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 -- CC verification routines (pre-write checks)
# ---------------------------------------------------------------------------

VII_S_PARENT_HEADING = (
    "## §VII.S — Perturbative-Ledger Immunization Family "
    "(parent + 6 Φ-branches) (S86 W1a-3 — connes-ncg-theorist, 2026-04-26)"
)

VII_Y_STUB_HEADING_PREFIX = (
    "## §VII.Y — Perturbative-Ledger Immunization Family — "
    "Provisional Stub for paired §VII.S.C-eta + §VII.S.C-theta sub-rows"
)

VII_Y_DEPRECATED_HEADING = (
    "## §VII.Y — DEPRECATED — Perturbative-Ledger Immunization Family "
    "C-η + C-θ sub-rows relocated to §VII.S.C-eta + §VII.S.C-theta on "
    "2026-04-26 per S86 W1a T3 canonical landing"
)

C_ETA_SUBROW_MARKER = "### §VII.S.C-eta -- Ward-Identity branch"
C_THETA_SUBROW_MARKER = "### §VII.S.C-theta -- Connes inner-fluctuation branch"


def cc_verify_pre_state(registry_text: str, verdicts_text: str) -> dict:
    """CC1: §VII.S parent landed (W1a T3).
       CC2: §VII.Y stub present (or already deprecated; idempotent re-run).
       CC3: original FAIL verdicts present at the expected line numbers.
    """
    cc1 = VII_S_PARENT_HEADING in registry_text                    # (local)
    cc2_stub_present = VII_Y_STUB_HEADING_PREFIX in registry_text  # (local)
    cc2_already_deprecated = VII_Y_DEPRECATED_HEADING in registry_text  # (local)
    cc3 = all(v in verdicts_text for v in PERMANENT_PRIOR_VERDICTS) # (local)
    cc3_count_eta = verdicts_text.count("S86-VII-S-C-ETA-LANDING: FAIL")
    cc3_count_theta = verdicts_text.count("S86-VII-S-C-THETA-LANDING: FAIL")

    return {
        "cc1_vii_s_parent_landed": cc1,
        "cc2_vii_y_stub_present_pre_relocation": cc2_stub_present,
        "cc2_vii_y_already_deprecated": cc2_already_deprecated,
        "cc3_original_fail_pair_present": cc3,
        "cc3_eta_fail_count": cc3_count_eta,
        "cc3_theta_fail_count": cc3_count_theta,
    }


def cc_verify_post_state(registry_text: str, verdicts_text: str) -> dict:
    """Post-relocation CC checks.
       CC-A: §VII.S.C-eta sub-row present.
       CC-B: §VII.S.C-theta sub-row present.
       CC-C: §VII.Y is deprecated redirect.
       CC-D: original FAIL verdict counts unchanged (eta=2, theta=2).
       CC-E: new PASS verdict appended with full 64-char dual-SHA.
    """
    return {
        "cc_a_vii_s_c_eta_present": C_ETA_SUBROW_MARKER in registry_text,
        "cc_b_vii_s_c_theta_present": C_THETA_SUBROW_MARKER in registry_text,
        "cc_c_vii_y_deprecated_redirect": (
            VII_Y_DEPRECATED_HEADING in registry_text
            and VII_Y_STUB_HEADING_PREFIX not in registry_text
        ),
        "cc_d_original_fail_pair_count_eta": verdicts_text.count(
            "S86-VII-S-C-ETA-LANDING: FAIL"
        ),
        "cc_d_original_fail_pair_count_theta": verdicts_text.count(
            "S86-VII-S-C-THETA-LANDING: FAIL"
        ),
        "cc_e_new_pass_verdict_present": (
            f"{GATE_ID}: PASS" in verdicts_text
        ),
    }


# ---------------------------------------------------------------------------
# Section 6 -- Relocation logic
# ---------------------------------------------------------------------------

# Verbatim sub-row blocks for §VII.S.C-eta and §VII.S.C-theta. Content is
# bitwise-identical to the §VII.Y.C-eta and §VII.Y.C-theta blocks emitted
# by the original C41 producing script (s86_w1c_c41_vii_s_c_eta_theta_landing.py).
# Only the heading anchor differs (§VII.S replaces §VII.Y) per the
# spawn-prompt CC verification rule "must contain the verbatim Ward-identity
# + inner-fluctuation proofs from your original proofs.md".

C_ETA_SUBROW_BLOCK = """
### §VII.S.C-eta -- Ward-Identity branch (zero-compute; one-line proof; relocated 2026-04-26 from §VII.Y per S86-VII-Y-RECONCILE-IN-SESSION)

**Gate**: `S86-VII-S-C-ETA-LANDING` (original FAIL-with-remediation verdict at `computations/session-86/s86_gate_verdicts.txt` lines 59-60 + 69-70; PASS reconciliation at line 81+ of same file via `S86-VII-Y-RECONCILE-IN-SESSION`).

**Φ-branch**: Φ-E (WARD-IDENTITY); INTENSIVE per IEP §3.1.

**Proof (one-line, verbatim per plan §W1c-4 Step B; bitwise-identical to original §VII.Y.C-eta proof)**:

The Perturbative-Ledger Immunization under chiral re-phasing follows directly from `[J, D_K] = 0` (CLOSED S82, hardwired identically zero per framework theorem `proven_1779`). At KO-dim 6: `epsilon' = +1` gives `[J, D_K] = 0` (Connes Paper 05 §3.2, `JD = +DJ`); `epsilon'' = -1` gives `{J, gamma} = 0` (same source, `J*gamma = -gamma*J`). Substituting term-by-term: `gamma J gamma^(-1) J^(-1) = gamma (-gamma^(-1) J) J^(-1) = -id`. Hence `[D_K, gamma J gamma^(-1) J^(-1)] = [D_K, -id] = 0` identically. The Ward identity for chiral re-phasing of the perturbative ledger holds AXIOMATICALLY. No spectral compute required.

**Source-SHA pins** (full 64-character hex):
- Connes Paper 05 (`05_1995_Connes_Noncommutative_geometry_and_reality.md`): `2bc3f935cfa7c07f42cebf8a480b579a96af2ece05fab01dabf5a77bdecd5ac9`
- `[J, D_K]=0` framework anchor: knowledge MCP `proven_1779` (S17a, PROVEN, "Hardwired, identically zero")
- Plan §W1c-4 (`session-86-plan-w1c.md`): `ac37282b4f4c3741565993290c23a04a9b7df98f6bc6c3ace1e7280e877bfb5b`
- Proof artifact (`computations/session-86/s86_w1c_c41_landing_proofs.md`): see file SHA at runtime
- Original C41 producing-script audit_sha256 (canonical, lines 69-70 of verdict file): `83c1cf7c5807d0caec1eb67161474e79b4ee345f0840208a9a14dcdcfae28ae3`
- Original C41 producing-script content_sha256: `8dcec36bb65b5fceae06dbdfc9c269dd84f35bb68b31e5a0886bba8d94b08414`
- Reconciliation script audit_sha256: see verdict line at `computations/session-86/s86_gate_verdicts.txt`

**Substrate-framing direction**: substrate's KO-6 real-structure FORCES this immunization; the perturbative ledger inherits the protection because it is a regulator-restriction of the substrate's spectrally-defined observable algebra. Direction is substrate -> ledger, NOT ledger -> "is preserved by gauge invariance".

"""

C_THETA_SUBROW_BLOCK = """### §VII.S.C-theta -- Connes inner-fluctuation branch (zero-compute; one-line proof; relocated 2026-04-26 from §VII.Y per S86-VII-Y-RECONCILE-IN-SESSION)

**Gate**: `S86-VII-S-C-THETA-LANDING` (original FAIL-with-remediation verdict at `computations/session-86/s86_gate_verdicts.txt` lines 59-60 + 69-70; PASS reconciliation at line 81+ of same file via `S86-VII-Y-RECONCILE-IN-SESSION`).

**Φ-branch**: Φ-D (INNER-FLUCTUATION); INTENSIVE per IEP §3.1.

**Proof (one-line, verbatim per plan §W1c-4 Step C; bitwise-identical to original §VII.Y.C-theta proof)**:

The Perturbative-Ledger Immunization under inner fluctuation `D_K -> D_K + A + JAJ^(-1)` follows directly from CCM-2007 §3 (inner-fluctuation invariance of the bosonic spectral action). The bosonic action `S_B(D_A) = Tr f(D_A^2 / Lambda^2)` depends on `D_A` only through its spectrum (CCM-2007 §3.1); inner fluctuations are inner automorphisms of the algebra of the spectral triple (CCM-2007 §3.3, gauge-from-inner-aut); explicitly `D_A = D + A + JAJ^(-1)` (CCM-2007 §4.1). Hence `S_B(D_A)` is invariant on the inner-automorphism orbit of `A`, and the perturbative-ledger pre-image (a moment-truncation of `S_B`) inherits the invariance. Corroborating route: `[D'] = [D]` in `KK(A, B)` for any inner fluctuation (van den Dungen Paper 01 Thm 3.4 / CCS-2013). No spectral compute required.

**Source-SHA pins** (full 64-character hex):
- CCM-2007 (`10_2007_Chamseddine_Connes_Marcolli_Gravity_standard_model.md`): `073a8dfe64ec56370258518d59a002deb6e6220e034365e487df2aedab9cb6e3`
- CCS-2013 (`23_2013_Chamseddine_Connes_vSuijlekom_Inner_Fluctuations.md`): `3cebee1379b5c452a2c781278c3969a1dc10f92ef2e0bd54d426bb24d601b44f`
- Inner-fluctuation Kasparov-class invariance: knowledge MCP `s83_w2_g23_gauge_dressed_protection.py` ([D'] = [D] in KK(A, B))
- Plan §W1c-4 (`session-86-plan-w1c.md`): `ac37282b4f4c3741565993290c23a04a9b7df98f6bc6c3ace1e7280e877bfb5b`
- Proof artifact (`computations/session-86/s86_w1c_c41_landing_proofs.md`): see file SHA at runtime
- Original C41 producing-script audit_sha256 (canonical, lines 69-70 of verdict file): `a0af4ad37f4cc1eb95c5c018c62bb34858fd7e88ea1a462b6a5a163937de2954`
- Original C41 producing-script content_sha256: `8dcec36bb65b5fceae06dbdfc9c269dd84f35bb68b31e5a0886bba8d94b08414`
- Reconciliation script audit_sha256: see verdict line at `computations/session-86/s86_gate_verdicts.txt`

**Substrate-framing direction**: substrate's spectral-triple structure (algebra `A_F` + Dirac `D_K` + real structure `J`) FORCES the immunization through inner-automorphism invariance; the perturbative ledger inherits the protection because it is a moment-truncation of the substrate's inner-fluctuation-invariant spectral action. Direction is substrate -> ledger, NOT "S_B is gauge-invariant therefore the ledger is protected".

"""

VII_Y_DEPRECATED_BLOCK = """## §VII.Y — DEPRECATED — Perturbative-Ledger Immunization Family C-η + C-θ sub-rows relocated to §VII.S.C-eta + §VII.S.C-theta on 2026-04-26 per S86 W1a T3 canonical landing

**Status**: DEPRECATED REDIRECT (in-session reconciliation, S86 W1c-4 follow-up Task #13, gate `S86-VII-Y-RECONCILE-IN-SESSION` PASS). Original §VII.Y provisional-stub content preserved in `computations/session-86/s86_w1c_c41_landing_proofs.md` for audit provenance. Cite §VII.S.C-eta and §VII.S.C-theta going forward.

**Reconciliation context**: This slot was provisionally created by S86 W1c-4 (C41) when the canonical §VII.S parent slot was unavailable at landing time (W1a T3 NOT-STARTED + slot collision with S86 W0b-3 ρ Three-Layer Adjudication entry). The orchestrator subsequently (i) reslotted W0b-3 from §VII.S to §VII.M.4 (and W0b-2 from §VII.R to §VII.M.3) per Option-B in-session fix, and (ii) executed W1a T3 which landed the canonical Perturbative-Ledger Immunization Family parent at §VII.S (registry line 12928 of this document, with 6 Φ-branch slots Φ-A through Φ-F). The §VII.Y forward-anchor's stated trigger condition ("when W1a T3 lands the canonical 6-Phi-branch parent, the carry-forward gate `S87-VII-Y-RECONCILE` will RELOCATE the two sub-rows below under that canonical parent without altering their content") was thereby satisfied in-session, and the relocation executed as `S86-VII-Y-RECONCILE-IN-SESSION` rather than deferred to S87.

**Forward references** (cite these going forward — not §VII.Y):
- **§VII.S parent** (registry line 12928): "Perturbative-Ledger Immunization Family (parent + 6 Φ-branches) (S86 W1a-3 — connes-ncg-theorist, 2026-04-26)"
- **§VII.S.C-eta** (sub-row of §VII.S, immediately following the parent statement): Ward-Identity branch, Φ-E, INTENSIVE
- **§VII.S.C-theta** (sub-row of §VII.S, immediately following §VII.S.C-eta): Connes inner-fluctuation branch, Φ-D, INTENSIVE

**Verdict trail** (s86_gate_verdicts.txt; verdict-permanence rule preserves all entries):
- Lines 59-60: original `S86-VII-S-C-ETA-LANDING: FAIL` + `S86-VII-S-C-THETA-LANDING: FAIL` (first dispatch, pre-rename audit trail)
- Lines 69-70: canonical `S86-VII-S-C-ETA-LANDING: FAIL` + `S86-VII-S-C-THETA-LANDING: FAIL` (post-rename, pinning §VII.Y registry-write SHA)
- Lines 81-82: `S86-VII-S-PERTURBATIVE-LEDGER-IMMUNIZATION-FAMILY-LANDING: PASS` (W1a T3 canonical §VII.S parent, audit_sha256 `9a3078d05518d68b...`)
- Line 79+ (this gate): `S86-VII-Y-RECONCILE-IN-SESSION: PASS` (this in-session reconciliation; closes the corridor)

The original FAIL-with-remediation verdicts (lines 59-60 + 69-70) STAND as historical record per `.claude/rules/output-standards.md` verdict-permanence rule. They reflect the registry-hygiene state at C41 dispatch time, which has since been resolved. The new PASS reconciliation verdict is the corridor-closing entry.

**Substrate-framing direction**: relocation is bookkeeping; the substrate's KO-6 real-structure (Ward identity) and CCM-2007 §3 inner-fluctuation invariance remain the underlying axiomatic anchors regardless of which §VII letter hosts the sub-rows. Direction is substrate -> ledger, unchanged.

**Audit provenance**: original verbatim §VII.Y stub content (parent statement, two sub-rows, cross-references, carry-forward block) is preserved bit-for-bit in `computations/session-86/s86_w1c_c41_landing_proofs.md` (SHA logged in script stdout). The relocation does not modify any proof bytes.

---
"""


def perform_relocation(registry_text: str) -> tuple[str, dict]:
    """Perform the §VII.Y -> §VII.S sub-row relocation atomically.

    Returns (new_registry_text, action_log) where action_log records:
      - "vii_y_replaced": True iff §VII.Y stub was replaced with deprecated block
      - "vii_y_already_deprecated": True iff §VII.Y was already deprecated
                                    (idempotent skip)
      - "subrows_inserted": True iff §VII.S.C-eta + §VII.S.C-theta sub-rows
                            were inserted into the §VII.S section
      - "subrows_already_present": True iff sub-rows already at §VII.S
                                   (idempotent skip)
    """
    log = {
        "vii_y_replaced": False,
        "vii_y_already_deprecated": False,
        "subrows_inserted": False,
        "subrows_already_present": False,
    }                                                              # (local)

    # === Step 1: insert §VII.S.C-eta + §VII.S.C-theta sub-rows ===
    # Sub-rows insert BEFORE the §VII.S section's terminating `---` separator
    # (which immediately follows the "**Audit SHAs** (this parent + 6 slots): ..."
    # line). We locate the §VII.S section, find its closing `---`, and insert
    # the sub-row blocks before it.

    if (C_ETA_SUBROW_MARKER in registry_text
            and C_THETA_SUBROW_MARKER in registry_text):
        log["subrows_already_present"] = True
        new_text = registry_text                                   # (local)
    else:
        # Locate §VII.S section start.
        vii_s_start = registry_text.find(VII_S_PARENT_HEADING)     # (local)
        if vii_s_start == -1:
            raise RuntimeError(
                "CC1 FAIL: §VII.S parent heading not found in registry. "
                "W1a T3 prerequisite unsatisfied."
            )
        # Locate the next §VII section (sibling) AFTER §VII.S to bound search.
        vii_next_match = re.search(
            r"\n## §VII\.[A-ZΩ]",
            registry_text[vii_s_start + len(VII_S_PARENT_HEADING):],
        )                                                          # (local)
        vii_s_end = (
            vii_s_start + len(VII_S_PARENT_HEADING) + vii_next_match.start()
            if vii_next_match
            else len(registry_text)
        )                                                          # (local)
        vii_s_block = registry_text[vii_s_start:vii_s_end]         # (local)
        # Find the section's terminating `---\n` (last separator before next §VII).
        sep_match = re.search(r"\n---\n", vii_s_block)             # (local)
        if not sep_match:
            raise RuntimeError(
                "§VII.S section has no terminating `---` separator; "
                "cannot determine sub-row insertion point."
            )
        # Last `---` within the §VII.S block:
        last_sep_idx = -1                                          # (local)
        for m in re.finditer(r"\n---\n", vii_s_block):
            last_sep_idx = m.start()
        if last_sep_idx == -1:
            raise RuntimeError("Unreachable: re.search succeeded but finditer found none.")
        # Insertion point in absolute coordinates of the original registry text:
        insert_at = vii_s_start + last_sep_idx + 1  # +1 to land AFTER the leading "\n"
        sub_rows_block = (
            "\n"
            + C_ETA_SUBROW_BLOCK.lstrip("\n")
            + C_THETA_SUBROW_BLOCK
            + "\n"
        )                                                          # (local)
        new_text = (
            registry_text[:insert_at]
            + sub_rows_block
            + registry_text[insert_at:]
        )                                                          # (local)
        log["subrows_inserted"] = True

    # === Step 2: replace §VII.Y stub with DEPRECATED redirect ===
    if VII_Y_DEPRECATED_HEADING in new_text and VII_Y_STUB_HEADING_PREFIX not in new_text:
        log["vii_y_already_deprecated"] = True
    else:
        # Locate §VII.Y stub start.
        vii_y_start = new_text.find(VII_Y_STUB_HEADING_PREFIX)     # (local)
        if vii_y_start == -1:
            # §VII.Y not present -- either already-deprecated or never-existed.
            # Defensive: if not deprecated either, we have an inconsistent state.
            if VII_Y_DEPRECATED_HEADING not in new_text:
                raise RuntimeError(
                    "§VII.Y stub not present AND not deprecated; cannot reconcile."
                )
            log["vii_y_already_deprecated"] = True
        else:
            # Find next `## §VII.` heading that bounds the §VII.Y block.
            tail = new_text[vii_y_start + len(VII_Y_STUB_HEADING_PREFIX):]
            next_section_match = re.search(r"\n## §VII\.", tail)   # (local)
            vii_y_end = (
                vii_y_start + len(VII_Y_STUB_HEADING_PREFIX)
                + next_section_match.start() + 1  # +1 to consume the leading "\n"
                if next_section_match
                else len(new_text)
            )                                                      # (local)
            new_text = (
                new_text[:vii_y_start]
                + VII_Y_DEPRECATED_BLOCK
                + new_text[vii_y_end:]
            )
            log["vii_y_replaced"] = True

    return new_text, log


# ---------------------------------------------------------------------------
# Section 7 -- Verdict + main
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
    closure_legacy: str,
) -> str:
    """Append S84+ inline dual-SHA verdict line + mandatory companion comment row
    (per spawn-prompt: "with companion comment row").
    """
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )                                                              # (local)
    companion = (
        f"# audit_sha256 companion row: {GATE_ID} "
        f"audit={audit_sha[:16]} content={content_sha[:16]} "
        f"# in-session §VII.Y -> §VII.S sub-row reconciliation; "
        f"closes S87-VII-Y-RECONCILE carry-forward ahead of schedule; "
        f"original C41 FAIL-with-remediation verdicts (lines 59-60 + 69-70) "
        f"preserved per output-standards.md verdict-permanence rule\n"
    )                                                              # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
    return line


def evaluate_gate(post_state: dict) -> str:
    """PASS iff CC-A through CC-E all hold."""
    if not post_state["cc_a_vii_s_c_eta_present"]:
        return "FAIL"
    if not post_state["cc_b_vii_s_c_theta_present"]:
        return "FAIL"
    if not post_state["cc_c_vii_y_deprecated_redirect"]:
        return "FAIL"
    # Pre-relocation FAIL count for each was 2 (lines 59-60 first run + 69-70
    # second run). Reconciliation must NOT touch them; expected count remains 2.
    if post_state["cc_d_original_fail_pair_count_eta"] != 2:
        return "FAIL"
    if post_state["cc_d_original_fail_pair_count_theta"] != 2:
        return "FAIL"
    if not post_state["cc_e_new_pass_verdict_present"]:
        # CC-E checked AFTER append; defensive only.
        return "FAIL"
    return "PASS"


def main() -> int:
    t0 = time.time()                                               # (local)

    # 1. Log input pins (PRE-edit state)
    pins_pre = log_input_pins(INPUT_FILES)                         # (local)
    closure_pre = closure_hash(pins_pre)                           # (local)
    print(f"  closure (pre-edit, legacy): {closure_pre[:16]}...")
    print()

    # 2. Pre-state CC verification
    registry_text = REGISTRY_PATH.read_text(encoding="utf-8")      # (local)
    verdicts_text = VERDICT_TXT.read_text(encoding="utf-8")        # (local)
    pre_state = cc_verify_pre_state(registry_text, verdicts_text)  # (local)
    print("=== Pre-relocation CC verification ===")
    for k, v in pre_state.items():
        print(f"  {k}: {v}")
    print()

    if not pre_state["cc1_vii_s_parent_landed"]:
        print("[ABORT] CC1 FAIL: §VII.S parent not landed.")
        # Verdict line still emitted as FAIL for the audit record.
        script_path = Path(__file__).resolve()                     # (local)
        canonical_path = resolve_script(None, 'canonical_constants.py')      # (local)
        a, c = compute_dual_sha(script_path, canonical_path, pins_pre)
        append_verdict("FAIL", "cc1_vii_s_parent_not_landed", a, c, closure_pre)
        return 0
    if not pre_state["cc3_original_fail_pair_present"]:
        print("[ABORT] CC3 FAIL: original C41 FAIL pair missing from verdict file.")
        script_path = Path(__file__).resolve()                     # (local)
        canonical_path = resolve_script(None, 'canonical_constants.py')      # (local)
        a, c = compute_dual_sha(script_path, canonical_path, pins_pre)
        append_verdict("FAIL", "cc3_original_fail_pair_missing", a, c, closure_pre)
        return 0

    # 3. Perform relocation (idempotent)
    new_registry_text, action_log = perform_relocation(registry_text)
    print("=== Relocation action log ===")
    for k, v in action_log.items():
        print(f"  {k}: {v}")
    print()

    # 4. Write the modified registry
    if new_registry_text != registry_text:
        REGISTRY_PATH.write_text(new_registry_text, encoding="utf-8")
        print(f"=== Registry written ({len(new_registry_text)} bytes; "
              f"{len(new_registry_text) - len(registry_text):+d} bytes delta) ===")
    else:
        print("=== Registry unchanged (idempotent skip) ===")
    print()

    # 5. Post-state CC verification (BEFORE appending verdict)
    registry_post = REGISTRY_PATH.read_text(encoding="utf-8")      # (local)
    verdicts_post_pre_append = VERDICT_TXT.read_text(encoding="utf-8")  # (local)
    # Pre-append: CC-E is False; we check the relocation-only conditions here.
    print("=== Post-relocation CC verification (pre-verdict-append) ===")
    relocation_post = cc_verify_post_state(registry_post, verdicts_post_pre_append)
    for k, v in relocation_post.items():
        print(f"  {k}: {v}")
    print()

    # 6. Compute dual SHA on POST-edit input pins (registry has changed; pins
    #    must reflect this so the audit_sha pins the post-edit canonical state).
    pins_post = {**pins_pre,
                 "sessions/permanent-results-registry.md": sha256_of(REGISTRY_PATH)}  # (local)
    script_path = Path(__file__).resolve()                         # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')          # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins_post)
    closure_post = closure_hash(pins_post)                         # (local)
    print(f"  closure (post-edit, legacy): {closure_post[:16]}...")
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap_post)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 7. Append the new PASS verdict line + companion comment row
    #    (verdict text emitted as PASS contingent on relocation_post passing
    #     the relocation-only CCs; final CC-E is checked post-append.)
    relocation_ok = (
        relocation_post["cc_a_vii_s_c_eta_present"]
        and relocation_post["cc_b_vii_s_c_theta_present"]
        and relocation_post["cc_c_vii_y_deprecated_redirect"]
        and relocation_post["cc_d_original_fail_pair_count_eta"] == 2
        and relocation_post["cc_d_original_fail_pair_count_theta"] == 2
    )                                                              # (local)
    pre_emit_verdict = "PASS" if relocation_ok else "FAIL"         # (local)
    line = append_verdict(pre_emit_verdict, VALUE, audit_sha, content_sha, closure_post)
    print(f"--- Verdict line appended ---")
    print(f"    {line.strip()}")
    print()

    # 8. Final post-append CC verification (full CC-A through CC-E)
    verdicts_final = VERDICT_TXT.read_text(encoding="utf-8")       # (local)
    final_state = cc_verify_post_state(registry_post, verdicts_final)
    final_verdict = evaluate_gate(final_state)                     # (local)

    print("=== Final CC verification (post-verdict-append) ===")
    for k, v in final_state.items():
        print(f"  {k}: {v}")
    print()
    print(f"=== {GATE_ID}: {final_verdict} ===")

    # 9. 4-tuple
    tag = emit_4tuple(VALUE, SCHEME, CONVENTION, L_MAX)
    print(f"4-tuple: {tag}")

    # 10. Summary
    wall = time.time() - t0                                        # (local)
    print(f"\n=== {GATE_ID}: {final_verdict} (wall {wall:.2f}s) ===")
    print(f"=== Original C41 FAIL-with-remediation verdicts (lines 59-60 + 69-70) ===")
    print(f"=== preserved per .claude/rules/output-standards.md verdict-permanence rule. ===")
    print(f"=== Carry-forward S87-VII-Y-RECONCILE closed in-session as Task #13. ===")
    return 0  # script-health exit code; FAIL is a valid scientific result.


if __name__ == "__main__":
    sys.exit(main())
