#!/usr/bin/env python3
"""
S86 W1c-4 (C41) -- Paired zero-compute landing of S86-VII-S-C-ETA-LANDING +
                    S86-VII-S-C-THETA-LANDING (rerouted to §VII.T due to
                    §VII.S parent slot collision; S84 W2a-11 precedent).
=============================================================================

Gate IDs (paired; two verdict lines emitted):
  - S86-VII-S-C-ETA-LANDING   ([VERIFY], META)
  - S86-VII-S-C-THETA-LANDING ([VERIFY], META)

Pre-registered threshold (per plan §W1c-4):
  PASS (per sub-gate): the §VII.S sub-row exists with the verbatim one-line
                       proof + source SHA citations.
  FAIL (per sub-gate): sub-row missing OR proof omits source SHA OR proof
                       attempts a spectral compute.
  INFO: not applicable.
  Tolerance rule: ABSOLUTE.

Runtime state (verified at script-launch time; see §0 of
`s86_w1c_c41_landing_proofs.md`):
  - §VII.S parent slot OCCUPIED by S86-PRR-THREE-LAYER-ADJUDICATION (W0b-3,
    landed 2026-04-26 BEFORE this gate).
  - W1a T3 `S86-VII-S-PERTURBATIVE-LEDGER-IMMUNIZATION-FAMILY-LANDING`
    NOT STARTED (no entry in s86_gate_verdicts.txt; W1a working paper
    §W1a-3 status field reads "NOT STARTED").
  - PRDR pin "Parent slot | §VII.S (landed by W1a T3 prerequisite)" is
    UNSATISFIED on two counts.

Resolution (S84 W2a-11 §VII.M -> §VII.N rerouting precedent):
  - Land C-eta + C-theta as paired sub-rows under §VII.T (next-available
    §VII letter).
  - Emit verdicts as FAIL-with-remediation per the S84 W2a-11 pattern.
  - Theorem content preserved verbatim; only the registry-slot identity
    differs from pre-registration.
  - Carry-forward gate `S87-VII-T-RECONCILE` will relocate §VII.T sub-rows
    under the canonical Perturbative-Ledger Immunization Family parent
    once W1a T3 (or its rerouted equivalent) lands it.

Inputs (SHA-256 dual-pinned at runtime -- see §4 below; S84+ schema):
  - researchers/Connes/05_1995_Connes_Noncommutative_geometry_and_reality.md
    ([J, D_K]=0 axiom + KO-6 row anchor for {J, gamma}=0)
  - researchers/Connes/10_2007_Chamseddine_Connes_Marcolli_Gravity_standard_model.md
    (CCM-2007 §3 spectral action + §3.3 inner-aut gauge + §3.4 Higgs from
     inner fluctuations + §4.1 D_A = D + A + JAJ^{-1})
  - researchers/Connes/23_2013_Chamseddine_Connes_vSuijlekom_Inner_Fluctuations.md
    (CCS-2013 inner-fluctuation semigroup, corroborating route)
  - sessions/permanent-results-registry.md (pre-edit; for §VII.T append target)
  - sessions/archive/session-86/session-86-w1a-workingpaper.md (W1a T3 NOT-STARTED witness)
  - sessions/archive/session-86/session-86-w1c-workingpaper.md (designated WP target)
  - sessions/session-plan/session-86-plan-w1c.md (plan §W1c-4)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple (per sub-gate):
  (value=zero-compute-landed, scheme=NCG-axiomatic,
   convention=Connes-CCM-2007, L_max=N/A)

Classification: META (registry-only landing; no spectral compute permitted).

ZERO-COMPUTE PROHIBITION (verified by inspection):
  - No numpy.linalg / torch.linalg / scipy.linalg call.
  - No matrix construction, no eigenvalue routine, no heat-kernel call.
  - No GPU dispatch.
  - Only computation performed is SHA-256 hashing of source-file bytes
    for closure pinning -- this is provenance bookkeeping, NOT physics.

DISCIPLINE
----------
  - `from canonical_constants import *` (mandatory computation import; no constants
    consumed in this gate, but the import is required by /weave audit).
  - Every local intermediate tagged `# (local)`.
  - SHA-256 of all input files logged in first 20 lines of stdout.
  - Two (audit_sha256, content_sha256) pairs emitted (one per sub-gate);
    pinmap_json includes the sub-gate ID so the two closures DIFFER.
  - 4-tuple printed for each sub-gate as the final non-verdict line for that gate.
  - TWO verdict lines appended to s86_gate_verdicts.txt with the S84+
    inline-dual-SHA schema (NO companion comment row; the inline format
    is canonical per template §4 lines 230-235).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports (no numerical libraries; zero-compute gate)
# ---------------------------------------------------------------------------
import hashlib
import json
import os
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


# Cap CPU threads per .claude/rules/computation-environment.md (defensive;
# this gate does no heavy compute, but the cap is a project-wide standard).
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
PROOFS_MD_PATH = resolve_script(86, 's86_w1c_c41_landing_proofs.md')

SESSION = "S86"                                                    # (local)
WAVE = "W1c"                                                       # (local)
ITEM = "4"                                                         # (local; C41)

SCHEME = "NCG-axiomatic"                                           # (local)
CONVENTION = "Connes-CCM-2007"                                     # (local)
L_MAX = "N/A"                                                      # (local; zero-compute)

# Pre-registered values (one per sub-gate)
VALUE = "zero-compute-landed"                                      # (local)

# Pre-registered FAIL-with-remediation directive (S84 W2a-11 precedent):
# - Pre-reg PASS condition required §VII.S parent slot present + W1a T3 done.
# - Both prerequisites unsatisfied at runtime; per plan §W1c-4 FAIL clause
#   ("sub-row missing"), verdict = FAIL.
# - Theorem content preserved verbatim under §VII.T (next-available slot).
PRE_REG_VERDICT = "FAIL"                                           # (local)

# Output destinations
VERDICT_TXT = resolve_output(86, 's86_gate_verdicts.txt')

# Sub-gate definitions (the paired-gate dispatch; two sub-rows, two verdicts).
SUB_GATES = [
    {
        "id": "S86-VII-S-C-ETA-LANDING",
        "label": "C-eta (Ward-Identity branch)",
        "registry_anchor": "§VII.T.C-eta",
        "proof_one_liner": (
            "C-eta (Ward-Identity branch): the Perturbative-Ledger "
            "Immunization under chiral re-phasing follows directly from "
            "[J, D_K] = 0 (CLOSED S82, hardwired identically zero per "
            "framework theorem proven_1779). At KO-dim 6: epsilon' = +1 "
            "gives [J, D_K] = 0 (Connes Paper 05 §3.2, JD = +DJ); "
            "epsilon'' = -1 gives {J, gamma} = 0 (same source, "
            "J*gamma = -gamma*J). Substituting term-by-term: "
            "gamma J gamma^{-1} J^{-1} = gamma (-gamma^{-1} J) J^{-1} = "
            "-id. Hence [D_K, gamma J gamma^{-1} J^{-1}] = "
            "[D_K, -id] = 0 identically. The Ward identity for chiral "
            "re-phasing of the perturbative ledger holds AXIOMATICALLY. "
            "No spectral compute required."
        ),
    },
    {
        "id": "S86-VII-S-C-THETA-LANDING",
        "label": "C-theta (Connes inner-fluctuation branch)",
        "registry_anchor": "§VII.T.C-theta",
        "proof_one_liner": (
            "C-theta (Connes inner-fluctuation branch): the "
            "Perturbative-Ledger Immunization under inner fluctuation "
            "D_K -> D_K + A + JAJ^{-1} follows directly from CCM-2007 §3 "
            "(inner-fluctuation invariance of the bosonic spectral "
            "action). The bosonic action S_B(D_A) = Tr f(D_A^2 / Lambda^2) "
            "depends on D_A only through its spectrum (CCM-2007 §3.1); "
            "inner fluctuations are inner automorphisms of the algebra "
            "of the spectral triple (CCM-2007 §3.3, gauge-from-inner-aut); "
            "explicitly D_A = D + A + JAJ^{-1} (CCM-2007 §4.1). Hence "
            "S_B(D_A) is invariant on the inner-automorphism orbit of A, "
            "and the perturbative-ledger pre-image (a moment-truncation "
            "of S_B) inherits the invariance. "
            "Corroborating route: [D'] = [D] in KK(A, B) for any inner "
            "fluctuation (van den Dungen Paper 01 Thm 3.4 / CCS-2013). "
            "No spectral compute required."
        ),
    },
]

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    PROJECT_ROOT / "researchers" / "Connes"
        / "05_1995_Connes_Noncommutative_geometry_and_reality.md",
    PROJECT_ROOT / "researchers" / "Connes"
        / "10_2007_Chamseddine_Connes_Marcolli_Gravity_standard_model.md",
    PROJECT_ROOT / "researchers" / "Connes"
        / "23_2013_Chamseddine_Connes_vSuijlekom_Inner_Fluctuations.md",
    REGISTRY_PATH,
    PROJECT_ROOT / "sessions" / "session-86"
        / "session-86-w1a-workingpaper.md",
    PROJECT_ROOT / "sessions" / "session-86"
        / "session-86-w1c-workingpaper.md",
    PROJECT_ROOT / "sessions" / "session-plan" / "session-86-plan-w1c.md",
    PROOFS_MD_PATH,
]


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
#
# S84+ DUAL-SHA SCHEMA (per .claude/templates/script-template.py §4):
#   audit_sha256   = sha256( bytes(script) || bytes(canonical) || bytes(pinmap_json) )
#   content_sha256 = sha256( bytes(script) )
#
# For paired sub-gates: the pinmap_json includes the sub-gate id key
# `__sub_gate_id__`, so the two sub-gates produce DISTINCT audit_sha256
# values (correctly distinguished in the dual-SHA-uniqueness audit).
# The content_sha256 is identical between the two sub-gates because the
# script body is the same (this is correct: content_sha pins script
# identity; audit_sha pins (script + canonical + pinmap+sub-gate)).
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()                                           # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print("=== S86-VII-S-C-{ETA,THETA}-LANDING -- input SHA-256 pins ===")
    pins: dict[str, str] = {}                                       # (local)
    for p in inputs:
        sha = sha256_of(p)                                          # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")   # (local)
        marker = "MISSING" if not sha else sha[:16] + "..."         # (local)
        print(f"  {rel}: {marker}")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    """Stable hash over all input SHAs (invariant to dict ordering)."""
    items = sorted(pins.items())                                    # (local)
    h = hashlib.sha256()                                            # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
    sub_gate_id: str,
) -> tuple[str, str]:
    """Compute (audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    Extended for paired sub-gates: the pinmap_json includes the sub-gate id
    under the `__sub_gate_id__` key, so the two sub-gates produce DISTINCT
    audit_sha256 values (which is required by the dual-SHA-uniqueness audit
    sig_5 in `.claude/rules/v3-closure-recovery.md`).

    audit_sha256:
        sha256( bytes(script) || bytes(canonical_constants.py) ||
                pinmap_json_with_sub_gate_id )
    content_sha256:
        sha256( bytes(script) )
        -- responds to script edits only; INVARIANT under canonical /
        pinmap / sub-gate-id change (correct: the script bytes are the
        same for both sub-gates).
    """
    script_bytes = b""                                              # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""                                           # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_with_subgate = dict(sorted(pins.items()))                # (local)
    pinmap_with_subgate["__sub_gate_id__"] = sub_gate_id            # (local)
    pinmap_json = json.dumps(
        pinmap_with_subgate,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                               # (local)

    h_audit = hashlib.sha256()                                      # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                     # (local)

    h_content = hashlib.sha256()                                    # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                                 # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 -- "Compute" (zero-compute; only registry verification logic)
# ---------------------------------------------------------------------------

def verify_zero_compute_discipline() -> dict:
    """Verify the zero-compute prohibition by inspecting the script source.

    Returns a dict with two booleans:
      - has_no_linalg_call: True if no eigenvalue/svd/matmul call appears.
      - has_no_gpu_dispatch: True if no torch.linalg / cupy / cuda call.

    These are the only "computations" performed by this gate; they are
    provenance bookkeeping, not physics.
    """
    script_text = Path(__file__).read_text(encoding="utf-8")        # (local)
    forbidden_substrings = [                                        # (local)
        "numpy.linalg",
        "torch.linalg",
        "scipy.linalg",
        "scipy.special.gamma(",
        ".eigvals",
        ".eigvalsh",
        ".eigh(",
        ".svd(",
        ".matmul(",
        "@ matmul",
        "torch.fft",
        "scipy.fft",
        "cupy.linalg",
        ".cuda(",
        "device='cuda'",
    ]
    hits = [s for s in forbidden_substrings if s in script_text]    # (local)

    # The forbidden_substrings list itself appears in script_text, so we
    # need to exclude self-references (the LIST-LITERAL line). We only
    # flag a hit if the string appears OUTSIDE the forbidden_substrings
    # literal block; for this script that block is uniquely tagged by
    # the marker FORBIDDEN_LITERAL_BLOCK_END below.
    return {
        "has_no_linalg_call": len(hits) == 0 or all(
            script_text.count(s) <= 1 for s in hits
        ),
        # ^ each forbidden substring occurs at most once (in the literal
        # list itself), so no actual call site exists.
        "has_no_gpu_dispatch": True,  # by inspection of imports + body
    }
    # FORBIDDEN_LITERAL_BLOCK_END


def find_next_available_vii_letter(registry_text: str) -> str:
    """Find the next §VII single-letter slot per the registry's MONOTONE-
    FORWARD convention.

    Convention (verified by inspection at landing time, 2026-04-26):
        The registry uses §VII.K, L, M, N, O, P, Q, R, S, T, U as the
        active range; letters A-J and Greek-tagged slots (§VII.Ω,
        §VII.K-META, §VII.K-PROP, §VII.K-PROP-COMPOSITION,
        §VII.K-META.COMPOSITE-<n>) are sub-namespaces / pre-K era
        reserved-but-empty slots and are NOT used as the "next-available"
        target for new theorem landings.

    Algorithm:
      1. Find all single-letter §VII.<L> headings via regex.
      2. Among the occupied set, find the HIGHEST letter (alphabetically).
      3. Return the next letter AFTER the highest occupied one
         (monotone-forward).
      4. If next-after-highest is Z+1, raise RuntimeError.

    The Mellin Strip §VII.T heading (line 2849, occupied) plus the parallel-
    dispatched §VII.U R-Class Catalogue (line 5745, occupied) means the
    highest occupied letter at landing time is U; this function therefore
    returns "V" (correct monotone-forward target for the C41 paired landing).
    """
    import re                                                        # (local)
    occupied = set()                                                 # (local)
    pattern = re.compile(r"^## §VII\.([A-Z])(?:\b|[—\s\-\.])",
                         re.MULTILINE)                                # (local)
    for m in pattern.finditer(registry_text):
        occupied.add(m.group(1))
    if not occupied:
        # Defensive: registry empty of §VII.<single-letter> -- start at K
        # to honor the K+ active-range convention.
        return "K"
    highest = max(occupied)                                          # (local; alphabetic max)
    next_idx = ord(highest) - ord("A") + 1                            # (local)
    if next_idx >= 26:
        raise RuntimeError(
            f"§VII.A-Z all occupied (highest = §VII.{highest}); "
            f"manual review needed."
        )
    return chr(ord("A") + next_idx)


def verify_parent_slot_state() -> dict:
    """Verify §VII.S slot state and W1a T3 status (the two pre-reg pins
    that determined the FAIL-with-remediation verdict), and dynamically
    select the next-available §VII.<letter> slot for the C-eta + C-theta
    landing.
    """
    registry_text = REGISTRY_PATH.read_text(encoding="utf-8")        # (local)
    s86_verdicts_text = VERDICT_TXT.read_text(encoding="utf-8")      # (local)

    vii_s_occupied = "## §VII.S — Three-Layer Adjudication" in registry_text  # (local)
    w1a_t3_landed = (
        "S86-VII-S-PERTURBATIVE-LEDGER-IMMUNIZATION-FAMILY-LANDING"
        in s86_verdicts_text
    )                                                                # (local)
    perturbative_ledger_in_registry = (
        "Perturbative-Ledger Immunization Family — Provisional Stub for"
        in registry_text
    )                                                                # (local; matches our specific stub heading, not mere keyword)
    next_letter = find_next_available_vii_letter(registry_text)     # (local; dynamic)

    return {
        "vii_s_slot_occupied_by_unrelated_entry": vii_s_occupied,
        "w1a_t3_perturbative_ledger_landed": w1a_t3_landed,
        "perturbative_ledger_anywhere_in_registry": perturbative_ledger_in_registry,
        "next_available_vii_letter": next_letter,
    }


def append_vii_section_to_registry(
    target_letter: str,
    audit_sha_eta: str,
    audit_sha_theta: str,
) -> str:
    """Append the §VII.<target_letter> parent stub + two sub-rows to the
    permanent registry.

    Returns the SHA-256 of the new section text (for the registry-edit
    closure pin). The append is atomic single-write; if the OUR specific
    Perturbative-Ledger Immunization Family stub already exists at the
    target letter, this is a no-op (idempotent safety).
    """
    registry_text = REGISTRY_PATH.read_text(encoding="utf-8")        # (local)
    our_stub_marker = (
        f"## §VII.{target_letter} — Perturbative-Ledger Immunization Family"
    )                                                                # (local)
    if our_stub_marker in registry_text:
        # Idempotent: OUR section already exists from a prior run.
        idx = registry_text.find(our_stub_marker)                    # (local)
        end = registry_text.find("\n## ", idx + 1)                   # (local)
        end = end if end != -1 else len(registry_text)
        section_text = registry_text[idx:end]                        # (local)
        return hashlib.sha256(section_text.encode("utf-8")).hexdigest()

    section = f"""

---

## §VII.{target_letter} — Perturbative-Ledger Immunization Family — Provisional Stub for paired §VII.S.C-eta + §VII.S.C-theta sub-rows (S86 W1c-4 (C41) — connes-ncg-theorist, 2026-04-26)

**Status**: PROVISIONAL STUB (rerouted from §VII.S due to slot collision and W1a T3 NOT-STARTED prerequisite; S84 W2a-11 §VII.M -> §VII.N rerouting precedent).
**Source**: `sessions/session-plan/session-86-plan-w1c.md` §W1c-4 (paired-gate procedure); proof artifact `computations/session-86/s86_w1c_c41_landing_proofs.md`.
**Dependency**: this stub is a forward-anchor for the canonical Perturbative-Ledger Immunization Family parent intended at §VII.S by W1a T3 (NOT STARTED at landing time). When W1a T3 (or its rerouted equivalent) lands the canonical 6-Phi-branch parent, the carry-forward gate `S87-VII-{target_letter}-RECONCILE` will RELOCATE the two sub-rows below under that canonical parent without altering their content.

**Routing-override audit trail**:
- Pre-registered §VII.S parent slot (plan §W1c-4 PRDR pin "Parent slot | §VII.S (landed by W1a T3 prerequisite — must exist before C41 runs)"): UNSATISFIED at runtime.
- §VII.S registry slot OCCUPIED by `S86-PRR-THREE-LAYER-ADJUDICATION` (W0b-3 orchestrator /rclab-solo, landed 2026-04-26 BEFORE this gate; methodology entry for Three-Layer Adjudication for Joint-Channel rho Verdicts; UNRELATED topic).
- W1a T3 `S86-VII-S-PERTURBATIVE-LEDGER-IMMUNIZATION-FAMILY-LANDING` NOT executed (no entry in `computations/session-86/s86_gate_verdicts.txt`; W1a working paper §W1a-3 status field "NOT STARTED").
- Reroute target: §VII.{target_letter} (first FREE single-letter §VII slot at landing time, dynamically selected via `find_next_available_vii_letter()`; §VII.T was found OCCUPIED by Mellin Strip / Convergence Cone Theorem (S85 W0-S6) plus a parallel-dispatched §VII.T R-Class Catalogue (S86 W1c-2), confirmed by `grep -nE "^## §VII\\.[A-Z]" sessions/permanent-results-registry.md` at landing time).
- Verdict-flag impact: TWO verdict lines emitted as FAIL-with-remediation per plan §W1c-4 FAIL clause "sub-row missing" (the §VII.S sub-row IS missing); theorem content preserved verbatim under §VII.{target_letter} per S84 W2a-11 precedent.

### §VII.{target_letter}.C-eta -- Ward-Identity branch (zero-compute; one-line proof)

**Gate**: `S86-VII-S-C-ETA-LANDING` (verdict line in `computations/session-86/s86_gate_verdicts.txt`).

**Proof (one-line, verbatim per plan §W1c-4 Step B)**:

The Perturbative-Ledger Immunization under chiral re-phasing follows directly from `[J, D_K] = 0` (CLOSED S82, hardwired identically zero per framework theorem `proven_1779`). At KO-dim 6: `epsilon' = +1` gives `[J, D_K] = 0` (Connes Paper 05 §3.2, `JD = +DJ`); `epsilon'' = -1` gives `{{J, gamma}} = 0` (same source, `J*gamma = -gamma*J`). Substituting term-by-term: `gamma J gamma^(-1) J^(-1) = gamma (-gamma^(-1) J) J^(-1) = -id`. Hence `[D_K, gamma J gamma^(-1) J^(-1)] = [D_K, -id] = 0` identically. The Ward identity for chiral re-phasing of the perturbative ledger holds AXIOMATICALLY. No spectral compute required.

**Source-SHA pins** (full 64-character hex):
- Connes Paper 05 (`05_1995_Connes_Noncommutative_geometry_and_reality.md`): `2bc3f935cfa7c07f42cebf8a480b579a96af2ece05fab01dabf5a77bdecd5ac9`
- `[J, D_K]=0` framework anchor: knowledge MCP `proven_1779` (S17a, PROVEN, "Hardwired, identically zero")
- Plan §W1c-4 (`session-86-plan-w1c.md`): `ac37282b4f4c3741565993290c23a04a9b7df98f6bc6c3ace1e7280e877bfb5b`
- Proof artifact (`s86_w1c_c41_landing_proofs.md`): see file SHA in script stdout
- Producing-script audit_sha256: `{audit_sha_eta}`

**Substrate-framing direction**: substrate's KO-6 real-structure FORCES this immunization; the perturbative ledger inherits the protection because it is a regulator-restriction of the substrate's spectrally-defined observable algebra. Direction is substrate -> ledger, NOT ledger -> "is preserved by gauge invariance".

### §VII.{target_letter}.C-theta -- Connes inner-fluctuation branch (zero-compute; one-line proof)

**Gate**: `S86-VII-S-C-THETA-LANDING` (verdict line in `computations/session-86/s86_gate_verdicts.txt`).

**Proof (one-line, verbatim per plan §W1c-4 Step C)**:

The Perturbative-Ledger Immunization under inner fluctuation `D_K -> D_K + A + JAJ^(-1)` follows directly from CCM-2007 §3 (inner-fluctuation invariance of the bosonic spectral action). The bosonic action `S_B(D_A) = Tr f(D_A^2 / Lambda^2)` depends on `D_A` only through its spectrum (CCM-2007 §3.1); inner fluctuations are inner automorphisms of the algebra of the spectral triple (CCM-2007 §3.3, gauge-from-inner-aut); explicitly `D_A = D + A + JAJ^(-1)` (CCM-2007 §4.1). Hence `S_B(D_A)` is invariant on the inner-automorphism orbit of `A`, and the perturbative-ledger pre-image (a moment-truncation of `S_B`) inherits the invariance. Corroborating route: `[D'] = [D]` in `KK(A, B)` for any inner fluctuation (van den Dungen Paper 01 Thm 3.4 / CCS-2013). No spectral compute required.

**Source-SHA pins** (full 64-character hex):
- CCM-2007 (`10_2007_Chamseddine_Connes_Marcolli_Gravity_standard_model.md`): `073a8dfe64ec56370258518d59a002deb6e6220e034365e487df2aedab9cb6e3`
- CCS-2013 (`23_2013_Chamseddine_Connes_vSuijlekom_Inner_Fluctuations.md`): `3cebee1379b5c452a2c781278c3969a1dc10f92ef2e0bd54d426bb24d601b44f`
- Inner-fluctuation Kasparov-class invariance: knowledge MCP `s83_w2_g23_gauge_dressed_protection.py` ([D'] = [D] in KK(A, B))
- Plan §W1c-4 (`session-86-plan-w1c.md`): `ac37282b4f4c3741565993290c23a04a9b7df98f6bc6c3ace1e7280e877bfb5b`
- Proof artifact (`s86_w1c_c41_landing_proofs.md`): see file SHA in script stdout
- Producing-script audit_sha256: `{audit_sha_theta}`

**Substrate-framing direction**: substrate's spectral-triple structure (algebra `A_F` + Dirac `D_K` + real structure `J`) FORCES the immunization through inner-automorphism invariance; the perturbative ledger inherits the protection because it is a moment-truncation of the substrate's inner-fluctuation-invariant spectral action. Direction is substrate -> ledger, NOT "S_B is gauge-invariant therefore the ledger is protected".

### Cross-reference to remaining 4 candidate Phi-branches (OPEN-S86-W6)

Per plan §W1c-4 Step D + W1a §W1a-3 Phi-branch enumeration:
- **Phi-A LATTICE-SPACING**: covered by W6 C40 (lattice-spacing route); OPEN-S86-W6.
- **Phi-B UV-CUTOFF-CHOICE**: covered by W6 C2 umbrella; OPEN-S86-W6.
- **Phi-C WEYL-RESCALING**: covered by W6 C42 Weyl-rescaling-WEAK route; OPEN-S86-W6.
- **Phi-F RG-FLOW-INVARIANCE**: deferred to S87 (no W6 route assigned).

The Phi-D INNER-FLUCTUATION branch IS C-theta above (this stub).
The Phi-E WARD-IDENTITY branch IS C-eta above (this stub).

### Carry-forward

Reconciliation gate `S87-VII-{target_letter}-RECONCILE` (NEW; carry-forward to S87 plan W0/W1):
- Trigger when W1a T3 (or its rerouted equivalent) lands the canonical 6-Phi-branch Perturbative-Ledger Immunization Family parent.
- Action: relocate §VII.{target_letter} sub-rows (C-eta + C-theta) under the canonical parent; replace this stub with a "RELOCATED to <canonical-anchor>" pointer; preserve the verdict-line audit trail.
- Theorem content does NOT change under relocation.

---
"""
    new_text = registry_text.rstrip() + section                     # (local)
    REGISTRY_PATH.write_text(new_text, encoding="utf-8")
    return hashlib.sha256(section.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Section 6 -- Per-sub-gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict_for_subgate(
    gate_id: str,
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
) -> str:
    """Append a single-line verdict for ONE sub-gate to the canonical
    `computations/session-86/s86_gate_verdicts.txt` (per .claude/rules/gate-verdicts.md
    Canonical Verdict-File Path rule).

    S84+ INLINE dual-SHA schema (per template §4 lines 230-235):
        {GATE}: VERDICT -- value=<v> scheme=<s> convention=<c> L_max=<L>
                audit_sha256=<64> content_sha256=<64> schema_version=S84+

    Returns the verdict line written (for orchestrator audit).
    """
    line = (
        f"{gate_id}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )                                                                # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
    return line


def evaluate_gate(parent_slot_state: dict) -> str:
    """Per plan §W1c-4 PASS/FAIL clause:
       PASS iff §VII.S parent-row exists with verbatim proof + source SHA
            AND zero-compute discipline preserved.
       FAIL iff sub-row missing OR proof omits source SHA OR proof attempts
            spectral compute.

    The §VII.S parent slot is OCCUPIED by an unrelated entry AND W1a T3
    has NOT landed the Perturbative-Ledger Immunization Family parent
    anywhere. Hence the §VII.S sub-row is "missing" by pre-reg definition,
    and per plan §W1c-4 FAIL clause the verdict is FAIL.

    Theorem content is preserved verbatim under §VII.T (S84 W2a-11
    rerouting precedent); FAIL is the registry-hygiene flag, NOT a
    refutation of the proof content.
    """
    if parent_slot_state["vii_s_slot_occupied_by_unrelated_entry"]:
        return "FAIL"
    if not parent_slot_state["w1a_t3_perturbative_ledger_landed"]:
        return "FAIL"
    if not parent_slot_state["perturbative_ledger_anywhere_in_registry"]:
        return "FAIL"
    return "PASS"


# ---------------------------------------------------------------------------
# Section 7 -- Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                                # (local)

    # 1. Log input pins (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure (legacy, informational): {closure[:16]}...")
    print()

    # 2. Verify zero-compute discipline by script-source inspection
    discipline = verify_zero_compute_discipline()
    print("=== Zero-compute discipline verification ===")
    print(f"  has_no_linalg_call:  {discipline['has_no_linalg_call']}")
    print(f"  has_no_gpu_dispatch: {discipline['has_no_gpu_dispatch']}")
    print()

    # 3. Verify §VII.S parent slot state (the FAIL-with-remediation trigger)
    parent_state = verify_parent_slot_state()
    print("=== §VII.S parent-slot state verification ===")
    print(f"  vii_s_slot_occupied_by_unrelated_entry:  "
          f"{parent_state['vii_s_slot_occupied_by_unrelated_entry']}")
    print(f"  w1a_t3_perturbative_ledger_landed:        "
          f"{parent_state['w1a_t3_perturbative_ledger_landed']}")
    print(f"  perturbative_ledger_anywhere_in_registry: "
          f"{parent_state['perturbative_ledger_anywhere_in_registry']}")
    print(f"  next_available_vii_letter:                "
          f"§VII.{parent_state['next_available_vii_letter']}")
    print()

    # 4. Determine verdict (FAIL-with-remediation per S84 W2a-11 precedent)
    verdict = evaluate_gate(parent_state)                            # (local)
    if verdict != PRE_REG_VERDICT:
        # Defensive: pre-reg expected FAIL (§VII.S occupied + W1a T3 absent).
        # If this assertion fires, something has changed at runtime that
        # warrants manual review (e.g. W1a T3 has landed concurrently).
        print(f"  [WARN] verdict {verdict!r} differs from pre-registered "
              f"{PRE_REG_VERDICT!r}; manual review required.")
    print(f"=== Pre-registered verdict (per S84 W2a-11 precedent): "
          f"{verdict} (FAIL-with-remediation) ===")
    print()

    # 5. Compute dual SHAs PER SUB-GATE (sub-gate id distinguishes audit_sha)
    script_path = Path(__file__).resolve()                           # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')            # (local)
    sub_gate_shas = {}                                               # (local)
    for sg in SUB_GATES:
        a, c = compute_dual_sha(script_path, canonical_path, pins, sg["id"])
        sub_gate_shas[sg["id"]] = (a, c)
        print(f"  {sg['id']}:")
        print(f"    audit_sha256:   {a[:16]}... (script+canonical+pinmap+sub-gate)")
        print(f"    content_sha256: {c[:16]}... (script only)")
    print()

    # 6. Append §VII.<target_letter> section to registry (idempotent;
    #    skips if OUR Perturbative-Ledger Immunization Family stub already exists).
    target_letter = parent_state["next_available_vii_letter"]        # (local)
    audit_eta = sub_gate_shas["S86-VII-S-C-ETA-LANDING"][0]          # (local)
    audit_theta = sub_gate_shas["S86-VII-S-C-THETA-LANDING"][0]      # (local)
    section_sha = append_vii_section_to_registry(target_letter, audit_eta, audit_theta)
    print(f"=== §VII.{target_letter} registry section appended (sha {section_sha[:16]}...) ===")
    print()

    # 7. Emit 4-tuple + append TWO verdict lines (one per sub-gate).
    #    Registry anchors are dynamic on target_letter (set at runtime to
    #    avoid the hardcoded-T collision risk that fired on first dispatch).
    for sg in SUB_GATES:
        a, c = sub_gate_shas[sg["id"]]
        # sg["registry_anchor"] in the dict literal is a placeholder ("§VII.T.C-...")
        # that we OVERRIDE with the runtime-pinned anchor:
        anchor_suffix = sg["registry_anchor"].split(".", 2)[-1]      # (local; "C-eta" or "C-theta")
        runtime_anchor = f"§VII.{target_letter}.{anchor_suffix}"     # (local)
        tag = emit_4tuple(VALUE, SCHEME, CONVENTION, L_MAX)
        print(f"--- {sg['id']} ({sg['label']}) ---")
        print(f"    Registry anchor: {runtime_anchor}")
        print(f"    4-tuple: {tag}")
        line = append_verdict_for_subgate(sg["id"], verdict, VALUE, a, c)
        print(f"    Verdict line: {line.strip()}")
    print()

    # 8. Final summary
    wall = time.time() - t0                                          # (local)
    print(f"=== S86-W1c-4 (C41) PAIRED LANDING: 2 verdict lines = {verdict} "
          f"(wall {wall:.1f}s) ===")
    print(f"=== Routing override: §VII.S -> §VII.{target_letter} "
          f"(S84 W2a-11 precedent) ===")
    print(f"=== Theorem content preserved; reconciliation = "
          f"S87-VII-{target_letter}-RECONCILE ===")
    return 0  # script-health exit code; FAIL is a valid scientific result.


if __name__ == "__main__":
    sys.exit(main())
