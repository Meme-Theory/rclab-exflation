#!/usr/bin/env python3
"""
S87 W3-1 — S87-PATH-H-PATH-C-MULTI-VALUED-REGISTRY-LANDING (CF-20)
==================================================================

Gate: S87-PATH-H-PATH-C-MULTI-VALUED-REGISTRY-LANDING ([VERIFY])

Pre-registered threshold (5 boolean criteria — all must hold for PASS):
  (a) §VII.AC.1 + §VII.AC.4 placeholder DEFERRED markers REMOVED post-write
  (b) ANCHOR-1 (V1: 3He-B BDI 0D inheritance arrow) text present in both rows
  (c) ANCHOR-2 (C1: Connes 1996 + NCG axioms 3+5+6 + Schur orthogonality) present
  (d) STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY tag present
  (e) Closure SHA pin matches S86 W-3 R3-A Convergence #2 closure verdict
      (full 64-char audit_sha256 from `computations/session-86/s86_gate_verdicts.txt`,
       row `S86-R-BOTH-PATHWAYS-WATCHLIST-LANDING` —
       the W-3 workshop closure verdict that landed the dual-pathway
       Path-H/Path-C structure to the watchlist as the registry-internal
       projection of the W-3 R3-A Convergence #2 closure).

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - sessions/permanent-results-registry.md            (registry being patched)
  - computations/session-86/s86_gate_verdicts.txt           (W-3 closure SHA source)
  - sessions/session-plan/session-87-plan-w3.md       (plan §W3-1 spec)
  - .claude/rules/registry-landing.md                 (CO-PRIMARY schema)
  - canonical_constants.py                            (audit_sha256 only)
  - script bytes                                      (audit_sha256 + content_sha256)

Output 4-tuple:
  (value=<bool_5_criteria_met>, scheme=registry-landing,
   convention=SOURCE-DOUBLE-CITE-CO-PRIMARY, L_max=N/A)

Classification: GEOMETRIC

METHODOLOGY
-----------
Composes the SOURCE-DOUBLE-CITE-CO-PRIMARY anchor block per
`.claude/rules/registry-landing.md` schema and atomically rewrites the
two §VII.AC.1 + §VII.AC.4 sub-row bodies in
`sessions/permanent-results-registry.md`. The W-3 closure SHA is read from
the canonical W-3 watchlist-landing verdict line in
`computations/session-86/s86_gate_verdicts.txt` (full 64-char form, no
head-truncation per `.claude/rules/gate-verdicts.md`). The script uses an
atomic-rewrite Python writer (read full file → splice replacement at
section positions → atomic-rename via `Path.replace`) per
`.claude/rules/epistemic-discipline.md` §"Registry-Write Hygiene under
Parallel-Writer Race".

DISCIPLINE
----------
- `from canonical_constants import *` at script head
- Every local/intermediate tagged `# (local)`
- No GPU (registry-write gate; no eigenvalue computation)
- OMP_NUM_THREADS = 8 (capped before any numpy import)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Atomic single-`open("a")` append to s87_gate_verdicts.txt
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap (no GPU on this gate)
# ---------------------------------------------------------------------------
import os
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
# Section 1 — Canonical constants (MANDATORY first project import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
import re
import tempfile
import numpy as np
from pathlib import Path

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
SESSIONS_DIR = PROJECT_ROOT / "sessions"

SESSION = "S87"                                                        # (local)
GATE_ID = "S87-PATH-H-PATH-C-MULTI-VALUED-REGISTRY-LANDING"            # (local)
SCHEME = "registry-landing"                                            # (local)
CONVENTION = "SOURCE-DOUBLE-CITE-CO-PRIMARY"                           # (local)
L_MAX_TAG = "N/A"                                                      # (local)
N_EVAL = 5  # 5 PASS-criteria booleans                                 # (local)

REGISTRY_PATH = SESSIONS_DIR / "permanent-results-registry.md"         # (local)
S86_VERDICT_PATH = resolve_output(86, 's86_gate_verdicts.txt')                 # (local)
PLAN_W3_PATH = SESSIONS_DIR / "session-plan" / "session-87-plan-w3.md" # (local)
RULE_REG_LANDING = PROJECT_ROOT / ".claude" / "rules" / "registry-landing.md"  # (local)

# Output destinations
OUT_NPZ = resolve_output(87, 's87_w3_path_h_path_c_registry_landing.npz')      # (local)
OUT_JSON = resolve_output(87, 's87_w3_path_h_path_c_registry_landing.json')    # (local)
VERDICT_TXT = resolve_output(87, 's87_gate_verdicts.txt')                      # (local)

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    REGISTRY_PATH,
    S86_VERDICT_PATH,
    PLAN_W3_PATH,
    RULE_REG_LANDING,
]

# W-3 R3-A Convergence #2 closure-verdict gate-ID (the canonical W-3
# workshop-closure verdict line that landed the dual-pathway Path-H/Path-C
# structure to the watchlist as the registry-internal projection of the
# R3-A Convergence #2 closure). Per plan §W3-1.6 method block, the gate's
# closure SHA pin is the audit_sha256 of THIS verdict row.
W3_CLOSURE_GATE_ID = "S86-R-BOTH-PATHWAYS-WATCHLIST-LANDING"           # (local)


# ---------------------------------------------------------------------------
# Section 4 — SHA helpers (S84+ dual-SHA schema; canonical pattern)
# ---------------------------------------------------------------------------

def sha256_of_bytes(data: bytes) -> str:
    h = hashlib.sha256()  # (local)
    h.update(data)
    return h.hexdigest()


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
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

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
# Section 5 — Read W-3 closure SHA from s86_gate_verdicts.txt
# ---------------------------------------------------------------------------

_AUDIT_RE = re.compile(r"audit_sha256=([0-9a-fA-F]{64})")  # (local)


def read_w3_closure_sha(verdict_path: Path, gate_id: str) -> str:
    """Extract the FULL 64-char audit_sha256 of `gate_id` from verdict file.

    No head-truncation, no \\n stripping that drops trailing chars. Per plan
    §W3-1.10 substitution chain Step 4: the gate's closure SHA pin is the
    audit_sha256 verbatim — exact-match parsing. Returns the 64-hex string,
    raises ValueError if the gate row is absent or SHA is malformed.
    """
    if not verdict_path.exists():
        raise FileNotFoundError(f"verdict file not found: {verdict_path}")
    text = verdict_path.read_text(encoding="utf-8")  # (local)
    for line in text.splitlines():
        if line.startswith(f"{gate_id}:"):
            m = _AUDIT_RE.search(line)
            if m is None:
                raise ValueError(
                    f"no 64-char audit_sha256 found in row for {gate_id}: {line[:120]!r}"
                )
            sha = m.group(1).lower()  # (local)
            if len(sha) != 64:
                raise ValueError(
                    f"audit_sha256 length != 64 for {gate_id}: len={len(sha)}"
                )
            return sha
    raise ValueError(f"gate row not found in {verdict_path}: {gate_id}")


# ---------------------------------------------------------------------------
# Section 6 — Compose anchor blocks for §VII.AC.1 and §VII.AC.4
# ---------------------------------------------------------------------------

def compose_anchor_block_ac1(closure_sha_64: str) -> str:
    """Compose §VII.AC.1 SOURCE-DOUBLE-CITE-CO-PRIMARY landing block.

    Schema per `.claude/rules/registry-landing.md`:
      ANCHOR-1 (input layer, V1)
      ANCHOR-2 (output layer, C1)
      STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY
      Derivation chain: V1 → A_F → C1 → conclusion
      Closure SHA pin: <full 64-char>

    The block REPLACES the existing DEFERRED placeholder body for §VII.AC.1.
    """
    block = f"""### §VII.AC.1 — Path-H/Path-C Multi-Valued Classification (a) Landing (W-3 REG-1; landed S87 CF-20)

**Status**: LANDED — S87 W3-1 CF-20 `S87-PATH-H-PATH-C-MULTI-VALUED-REGISTRY-LANDING` closure (2026-04-28). The pre-registered statement below is now registry-anchored under the SOURCE-DOUBLE-CITE-CO-PRIMARY pattern per `.claude/rules/registry-landing.md`. The pre-S87 placeholder marker is removed; downstream consumers MAY cite §VII.AC.1 as the canonical anchor for the Path-H/Path-C dual-pathway structure.

**Theorem statement**: Classification (a) — Path-H and Path-C are TWO distinct projections of a single substrate observable `r`, multi-valued partition between B1 longitudinal-acoustic and B2 transverse-fiber eigenvalue clusters of `D_K²` at τ_fold; binary-not-continuous (forced by Schur orthogonality of `P_α` under NCG axioms 3+5+6 acting on `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)`); SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure (V1 input layer + C1 output layer; neither anchor is decoration; both must remain accessible for the derivational provenance to hold).

**ANCHOR-1 (input layer, V1)**: 3He-B BDI 0D inheritance arrow (S58 Volovik-partition canonical). The 3He-B parent supplies the BDI-class 0D inheritance premise that fixes the spectral algebra structure of the finite-dimensional sector. Provenance: `canonical_constants.py:1243` `w0_FW = -0.918` (S58 Volovik-partition canonical); cross-link to `sessions/framework/registry/branch-iv-canonical.md` §3 substrate-natural anchor `59.8 · Δ_BCS / K_base`. The inheritance arrow forces the smallest finite spectral algebra consistent with BDI 0D + the finite-spectrum sub-axis (inheritance-to-`A_F` map `ι_*: A_parent → A_F`); without it, `A_F` is freely chosen and the V1+C1 sequential chain has no input premise.

**ANCHOR-2 (output layer, C1)**: Connes 1996 reconstruction (Connes, "Gravity coupled with matter and the foundation of non-commutative geometry", Comm. Math. Phys. 182, 155-176 (1996)) + NCG axioms 3 (orientability via Hochschild cycle), 5 (first-order condition `[[D, a], b^o] = 0`), 6 (real structure `J`) + Schur orthogonality of irreducible `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)`-modules. Once V1 fixes `A_F`, the NCG-axiomatic + Schur output layer yields the unique B1/B2 block decomposition of `D²` (Wedderburn structure theorem provides the irrep enumeration; KO-dim 6 fixes parity grading `γ_P`; the 96-dim `H_F` decomposes uniquely as B1 (longitudinal-acoustic) ⊕ B2 (transverse-fiber)). C1 alone, without V1, is conditional on a free `A_F` choice — neither anchor stands alone.

**STRUCTURE**: SOURCE-DOUBLE-CITE-CO-PRIMARY (per `.claude/rules/registry-landing.md` schema). Two anchors at equal-weight; sequential V → A_F → C dependency; non-fungible (cannot be swapped or reordered); both must remain accessible.

**Derivation chain:** V1 (3He-B BDI 0D inheritance arrow fixes `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)` as the spectral-algebra premise) → A_F (Connes-Chamseddine finite-dimensional spectral algebra; Wedderburn + KO-dim-6 grading) → C1 (NCG axioms 3+5+6 + Schur orthogonality on `A_F` yield uniqueness of the B1/B2 block decomposition of `D²`; Path-H = projection onto B1 cluster, Path-C = projection onto B2 cluster) → conclusion (Path-H and Path-C are multi-valued substrate observables; each cell is a regulator-class projection of the same fiber spectrum at τ_fold).

**Closure SHA pin:** `{closure_sha_64}` (full 64-char `audit_sha256` of the W-3 R3-A Convergence #2 closure verdict, `{W3_CLOSURE_GATE_ID}` row in `computations/session-86/s86_gate_verdicts.txt`; this is the workshop-closure SHA that landed the dual-pathway Path-H/Path-C structure to the watchlist as the registry-internal projection of the R3-A Convergence #2 closure).

**Source**: workshop §Round 3 connes Convergence #2 (`sessions/archive/session-86/workshops/s86-r-dual-pathway-bk-array-and-nT.md`, lines 2840-2879); §Workshop Verdict row 2 (line 3170); §Carry-Forward 1 spec (lines 3238-3243); §Closing Line (line 3268). Volovik R2-A V1-PRIMARY framing was REVOKED at R3-A Convergence #2 in favor of CO-PRIMARY (workshop lines 2472-2507 + 2840-2879); this landing reflects the post-revocation structure.

**Substrate framing**: The Path-H/Path-C structure is NOT "two competing inflationary models." It is a multi-valued substrate observable expressing the regulator-class lattice's two-cell decomposition of the same fiber spectrum at τ_fold. The substrate IS the spectrum; Path-H is the projection of that spectrum onto the B1 longitudinal-acoustic cluster, Path-C is the projection onto the B2 transverse-fiber cluster. Direction of explanation flows substrate → bridge → laboratory: D_K eigenvalues at τ_fold → B1/B2 block decomposition → r-projection per pathway → LiteBIRD/LISA discrimination. Treating Path-H/Path-C as "two phenomenological choices" inverts the direction and is a container-thinking violation per `.claude/rules/phononic-framing.md`.
"""
    return block


def compose_anchor_block_ac4(closure_sha_64: str) -> str:
    """Compose §VII.AC.4 V1-C1 sequential-chain landing block.

    Per `.claude/rules/registry-landing.md`: §VII.AC.4 is the per-anchor-
    rationale companion row — the sequential-chain derivation explicit in
    text. It repeats the SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure
    with derivation-chain emphasis (each step explicit; both anchors
    sequential, non-fungible, co-primary).
    """
    block = f"""### §VII.AC.4 — V1+C1 Sequential-Chain Derivation of Classification (a) (W-3 REG-4; landed S87 CF-20)

**Status**: LANDED — S87 W3-1 CF-20 `S87-PATH-H-PATH-C-MULTI-VALUED-REGISTRY-LANDING` closure (2026-04-28). The pre-registered V1+C1 sequential-chain derivation is now registry-anchored as the per-anchor-rationale companion row to §VII.AC.1 under the SOURCE-DOUBLE-CITE-CO-PRIMARY pattern. The pre-S87 placeholder marker is removed.

**Theorem statement**: The Path-H/Path-C multi-valued classification (a) is derivable in a strict sequential chain V1 → A_F → C1 → conclusion in which neither anchor establishes the conclusion alone:

  - V1 (3He-B BDI 0D parent — input layer) supplies the BDI-class 0D inheritance arrow `ι_*: A_parent → A_F`; this forces `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)` as the smallest finite spectral algebra consistent with BDI 0D inheritance.
  - A_F (Connes-Chamseddine finite-dimensional spectral algebra) supplies the Wedderburn irrep enumeration (one C-component, one ℍ-component, one M_3(ℂ)-component); KO-dim 6 fixes the parity grading `γ_P`; the 96-dim `H_F` is the conjugate-doubled fundamental representation.
  - C1 (Connes 1996 reconstruction + NCG axioms 3+5+6 + Schur orthogonality — output layer) supplies the unique B1/B2 block decomposition of `D²` at the irrep level.
  - Conclusion: Path-H and Path-C are dual-valued projections of the substrate observable `r` onto the B1/B2 partition; binary-not-continuous; multi-valued in the substrate's structural sense.

**ANCHOR-1 (input layer, V1)**: 3He-B BDI 0D inheritance arrow (S58 Volovik-partition canonical; `canonical_constants.py:1243` `w0_FW = -0.918`; cross-link to `sessions/framework/registry/branch-iv-canonical.md` §3 substrate-natural anchor `59.8 · Δ_BCS / K_base`). V1 alone does NOT establish the classification — it supplies the BDI 0D premise that A_F must satisfy, but C1 (Connes + axioms 3+5+6 + Schur) is needed to derive the uniqueness of the block decomposition.

**ANCHOR-2 (output layer, C1)**: Connes 1996 reconstruction (Comm. Math. Phys. 182, 155-176 (1996)) + NCG axioms 3 (orientability via Hochschild cycle), 5 (first-order condition `[[D, a], b^o] = 0`), 6 (real structure `J`) + Schur orthogonality of irreducible `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)`-modules. C1 alone is CONDITIONAL on the `A_F` choice — without V1's BDI 0D inheritance, `A_F` is freely selected and the C1 uniqueness theorem applies to whatever `A_F` is named (rendering the derivation tautological). Together V1 + C1 fix the conclusion uniquely; this is why CO-PRIMARY (not PRIMARY+CONFIRMATION) is the correct anchor structure: PRIMARY+CONFIRMATION assumes independent reproduction of the same conclusion via parallel routes, but V1 and C1 are sequential, not parallel — neither is decoration.

**STRUCTURE**: SOURCE-DOUBLE-CITE-CO-PRIMARY (per `.claude/rules/registry-landing.md` schema; calibration corpus row for the sequential V+C chain pattern). Sequential dependency: C1 cannot be invoked WITHOUT first invoking V1; non-fungible (the two anchors cannot be swapped or reordered without breaking the chain); both must remain accessible for the derivational provenance to hold.

**Derivation chain:** (explicit per-step)
  1. V1: 3He-B BDI 0D inheritance arrow → `A_F` = smallest finite spectral algebra with C ⊕ H ⊕ M_3(C) structure consistent with BDI class.
  2. A_F structure → Wedderburn irrep enumeration: `A_F` has three irreducible representations (the C-rep `χ_C`, the H-rep `χ_H`, the M_3(C)-rep `χ_3`).
  3. KO-dim 6 + grading γ_P fixes the conjugate-doubled `H_F` decomposition: `H_F = H_F^B1 ⊕ H_F^B2` where B1 and B2 are the parity-graded sub-modules.
  4. NCG Axiom 3 (real structure J) + Axiom 5 ([[D,a],b^o]=0) + Axiom 6 (orientability) act jointly: each commutes with the irrep block-projector P_α, forcing [D, P_α] = 0 at the irrep level (proof via Hochschild-cycle representation of the orientability cycle + first-order condition on multipliers).
  5. Schur orthogonality of irreducible A_F-modules: P_{{B1}} · P_{{B2}} = 0; the decomposition is binary-not-continuous (no free unitary mixing parameter).
  6. r-projection: each pathway `r_α = ⟨P_α · D² · P_α⟩_{{a_4^ζ}}` is a block-restricted variational derivative of the same `a_4^ζ` Seeley-DeWitt moment — Path-H = `r_{{B1}}` (longitudinal-acoustic); Path-C = `r_{{B2}}` (transverse-fiber).

**Closure SHA pin:** `{closure_sha_64}` (full 64-char `audit_sha256` of the W-3 R3-A Convergence #2 closure verdict, `{W3_CLOSURE_GATE_ID}` row in `computations/session-86/s86_gate_verdicts.txt`; identical to §VII.AC.1 closure SHA pin — both rows close against the same workshop-closure verdict).

**Source**: workshop §R3-A Convergence #2 (lines 2472-2507); §R3-B Convergence #2 (lines 2840-2879); §Emergence #2 (lines 3116-3160). Calibration corpus row for `.claude/rules/registry-landing.md` §"Calibration corpus".

**Substrate framing**: The V1+C1 sequential-chain derivation is itself a structural property of the substrate's finite spectral triple. V1 (the inheritance arrow `ι_*` from the 3He-B parent) is a substrate-IS observable (the kernel structure of the parent → child algebra map); C1 (the NCG-axiomatic block-decomposition theorem) is the substrate's structural-uniqueness statement at the finite-L spectral-triple level. Neither is "external evidence" for the conclusion — both are internal structural properties of the substrate. This is why the chain produces a registry-grade theorem rather than a phenomenological correlation.
"""
    return block


# ---------------------------------------------------------------------------
# Section 7 — Atomic in-place rewrite of the registry file
# ---------------------------------------------------------------------------

# Splice locators: each block runs from the §VII.AC.X header (either the
# pre-S87 DEFERRED form or the in-progress S87 CF-20 LANDED form — the
# script is idempotent under partial-apply re-runs) up to (but not
# including) the next "### " or "## " header. We anchor on the §VII.AC.X
# section number directly.
#
# Flexible match: matches "### §VII.AC.1 — DEFERRED — ..." OR
# "### §VII.AC.1 — Path-H/Path-C Multi-Valued Classification ..." (either
# state — pre-write or partially-written from a prior run that FAILed
# rubric).

_HEADER_AC1_RE = re.compile(
    r"^### §VII\.AC\.1 —.*?(?=^### |^## |\Z)",
    re.MULTILINE | re.DOTALL,
)  # (local)

_HEADER_AC4_RE = re.compile(
    r"^### §VII\.AC\.4 —.*?(?=^### |^## |\Z)",
    re.MULTILINE | re.DOTALL,
)  # (local)

# Top-of-file table rows. Flexible match: either pre-S87 DEFERRED form OR
# the in-progress S87 CF-20 LANDED form. Captures the entire row.
_TABLE_ROW_AC1_RE = re.compile(
    r"^\| §VII\.AC\.1 \| THM \|[^\|]*\|[^\|]*\|[^\|]*\|$",
    re.MULTILINE,
)  # (local)

_TABLE_ROW_AC4_RE = re.compile(
    r"^\| §VII\.AC\.4 \| THM \|[^\|]*\|[^\|]*\|[^\|]*\|$",
    re.MULTILINE,
)  # (local)


def patch_registry(
    registry_path: Path,
    new_ac1_block: str,
    new_ac4_block: str,
) -> dict:
    """Atomic in-place rewrite of permanent-results-registry.md.

    Pattern (per `.claude/rules/epistemic-discipline.md` §"Registry-Write
    Hygiene under Parallel-Writer Race"):
      1. Read full file bytes.
      2. Splice replacement at section positions via regex sub (single-pass).
      3. Atomic-rename via Path.replace from a sibling tempfile.

    Returns a diagnostic dict.
    """
    original_text = registry_path.read_text(encoding="utf-8")  # (local)
    original_len = len(original_text)  # (local)

    # 1) Replace the SECTION blocks
    text_after_ac1, n_ac1 = _HEADER_AC1_RE.subn(
        new_ac1_block + "\n", original_text
    )
    if n_ac1 != 1:
        raise RuntimeError(
            f"§VII.AC.1 DEFERRED block: expected exactly 1 match, got {n_ac1}"
        )

    text_after_ac4, n_ac4 = _HEADER_AC4_RE.subn(
        new_ac4_block + "\n", text_after_ac1
    )
    if n_ac4 != 1:
        raise RuntimeError(
            f"§VII.AC.4 DEFERRED block: expected exactly 1 match, got {n_ac4}"
        )

    # 2) Update the top-of-file table rows (line 87 / 90 in plan grep cite)
    new_table_row_ac1 = (
        "| §VII.AC.1 | THM | Path-H/Path-C Multi-Valued Classification (a) "
        "Landing (S86 W-3 sub-row C.1; CO-PRIMARY anchor structure landed "
        "S87 CF-20, 2026-04-28) | gen-physicist | 2026-04-28 |"
    )  # (local)
    text_after_tbl1, n_tbl1 = _TABLE_ROW_AC1_RE.subn(
        new_table_row_ac1, text_after_ac4
    )
    if n_tbl1 != 1:
        raise RuntimeError(
            f"§VII.AC.1 table row: expected exactly 1 match, got {n_tbl1}"
        )

    new_table_row_ac4 = (
        "| §VII.AC.4 | THM | V1+C1 Sequential-Chain Derivation of "
        "Classification (a) (S86 W-3 sub-row C.4; CO-PRIMARY companion "
        "row landed S87 CF-20, 2026-04-28) | gen-physicist | 2026-04-28 |"
    )  # (local)
    text_after_tbl4, n_tbl4 = _TABLE_ROW_AC4_RE.subn(
        new_table_row_ac4, text_after_tbl1
    )
    if n_tbl4 != 1:
        raise RuntimeError(
            f"§VII.AC.4 table row: expected exactly 1 match, got {n_tbl4}"
        )

    new_text = text_after_tbl4  # (local)
    new_len = len(new_text)  # (local)

    # 3) Atomic write via sibling tempfile + os.replace
    tmp = registry_path.with_suffix(registry_path.suffix + ".tmp.s87w3")  # (local)
    tmp.write_text(new_text, encoding="utf-8")
    os.replace(str(tmp), str(registry_path))

    return {
        "original_byte_len": original_len,
        "new_byte_len": new_len,
        "delta_bytes": new_len - original_len,
        "n_ac1_section_replacements": n_ac1,
        "n_ac4_section_replacements": n_ac4,
        "n_ac1_table_replacements": n_tbl1,
        "n_ac4_table_replacements": n_tbl4,
    }


# ---------------------------------------------------------------------------
# Section 8 — Post-write verification: 5 PASS criteria
# ---------------------------------------------------------------------------

def verify_pass_criteria(
    registry_path: Path,
    closure_sha_64: str,
) -> dict:
    """Re-read registry and check the 5 PASS criteria.

    (a) DEFERRED markers REMOVED in §VII.AC.1 + §VII.AC.4 sub-row bodies
    (b) ANCHOR-1 (V1) text present in both rows
    (c) ANCHOR-2 (C1) text present in both rows
    (d) STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY tag present in both
    (e) Closure SHA pin matches W-3 closure SHA in both
    """
    text = registry_path.read_text(encoding="utf-8")  # (local)

    # Slice the §VII.AC.1 + §VII.AC.4 sub-row sections (post-write)
    ac1_re = re.compile(
        r"^### §VII\.AC\.1 —.*?(?=^### |^## |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    ac4_re = re.compile(
        r"^### §VII\.AC\.4 —.*?(?=^### |^## |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    m1 = ac1_re.search(text)  # (local)
    m4 = ac4_re.search(text)  # (local)
    if m1 is None or m4 is None:
        raise RuntimeError(
            f"post-write: §VII.AC.1 found={m1 is not None}, "
            f"§VII.AC.4 found={m4 is not None}"
        )
    ac1_body = m1.group(0)  # (local)
    ac4_body = m4.group(0)  # (local)

    # (a) DEFERRED markers absent
    a_ac1 = "DEFERRED" not in ac1_body
    a_ac4 = "DEFERRED" not in ac4_body

    # (b) ANCHOR-1 V1 present
    v1_marker = "3He-B BDI 0D inheritance arrow"  # (local)
    b_ac1 = ("ANCHOR-1 (input layer, V1)" in ac1_body) and (v1_marker in ac1_body)
    b_ac4 = ("ANCHOR-1 (input layer, V1)" in ac4_body) and (v1_marker in ac4_body)

    # (c) ANCHOR-2 C1 present
    c_marker_1 = "Connes 1996"  # (local)
    c_marker_2 = "Schur orthogonality"  # (local)
    c_marker_3 = "axioms 3"  # (local)  matches "axioms 3+5+6" / "axioms 3 ("
    c_ac1 = (
        ("ANCHOR-2 (output layer, C1)" in ac1_body)
        and (c_marker_1 in ac1_body)
        and (c_marker_2 in ac1_body)
        and (c_marker_3 in ac1_body)
    )
    c_ac4 = (
        ("ANCHOR-2 (output layer, C1)" in ac4_body)
        and (c_marker_1 in ac4_body)
        and (c_marker_2 in ac4_body)
        and (c_marker_3 in ac4_body)
    )

    # (d) STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY present
    struct_marker = "SOURCE-DOUBLE-CITE-CO-PRIMARY"  # (local)
    d_ac1 = ("STRUCTURE" in ac1_body) and (struct_marker in ac1_body)
    d_ac4 = ("STRUCTURE" in ac4_body) and (struct_marker in ac4_body)

    # (e) Closure SHA pin matches W-3 closure SHA verbatim (case-fold)
    sha = closure_sha_64.lower()  # (local)
    e_ac1 = (sha in ac1_body.lower()) and ("Closure SHA pin" in ac1_body)
    e_ac4 = (sha in ac4_body.lower()) and ("Closure SHA pin" in ac4_body)

    diag = {
        "criterion_a_DEFERRED_removed_AC1": bool(a_ac1),
        "criterion_a_DEFERRED_removed_AC4": bool(a_ac4),
        "criterion_b_ANCHOR1_V1_present_AC1": bool(b_ac1),
        "criterion_b_ANCHOR1_V1_present_AC4": bool(b_ac4),
        "criterion_c_ANCHOR2_C1_present_AC1": bool(c_ac1),
        "criterion_c_ANCHOR2_C1_present_AC4": bool(c_ac4),
        "criterion_d_STRUCTURE_tag_present_AC1": bool(d_ac1),
        "criterion_d_STRUCTURE_tag_present_AC4": bool(d_ac4),
        "criterion_e_closure_SHA_match_AC1": bool(e_ac1),
        "criterion_e_closure_SHA_match_AC4": bool(e_ac4),
        "ac1_block_byte_len": len(ac1_body.encode("utf-8")),
        "ac4_block_byte_len": len(ac4_body.encode("utf-8")),
    }
    diag["all_a"] = a_ac1 and a_ac4
    diag["all_b"] = b_ac1 and b_ac4
    diag["all_c"] = c_ac1 and c_ac4
    diag["all_d"] = d_ac1 and d_ac4
    diag["all_e"] = e_ac1 and e_ac4
    diag["all_5_criteria_met"] = (
        diag["all_a"]
        and diag["all_b"]
        and diag["all_c"]
        and diag["all_d"]
        and diag["all_e"]
    )

    # Verifier-rubric pre-registration: 5-string conjunction
    rubric_strings = [
        "ANCHOR-1 (input layer, V1)",
        "ANCHOR-2 (output layer, C1)",
        "STRUCTURE",
        "Derivation chain:",
        "Closure SHA pin:",
    ]
    rubric_ac1 = all(s in ac1_body for s in rubric_strings)  # (local)
    rubric_ac4 = all(s in ac4_body for s in rubric_strings)  # (local)
    diag["rubric_5string_conjunction_AC1"] = bool(rubric_ac1)
    diag["rubric_5string_conjunction_AC4"] = bool(rubric_ac4)

    return diag


# ---------------------------------------------------------------------------
# Section 9 — Verdict-line append (atomic single open("a"))
# ---------------------------------------------------------------------------

def append_verdict(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
) -> str:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX_TAG} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
    return line


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (
        f"(value={value!r}, scheme={scheme}, "
        f"convention={convention}, L_max={L_max})"
    )


# ---------------------------------------------------------------------------
# Section 10 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)  # (local)
    print(f"  legacy closure: {closure[:16]}... (informational)")

    # 2. Compute dual SHAs
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 3. Read W-3 closure SHA from s86_gate_verdicts.txt (full 64-char)
    w3_closure_sha = read_w3_closure_sha(S86_VERDICT_PATH, W3_CLOSURE_GATE_ID)  # (local)
    print(f"=== W-3 closure SHA extracted ===")
    print(f"  gate: {W3_CLOSURE_GATE_ID}")
    print(f"  audit_sha256 (full 64): {w3_closure_sha}")
    print(f"  length: {len(w3_closure_sha)} chars")
    print()

    # 4. Compose the SOURCE-DOUBLE-CITE-CO-PRIMARY anchor blocks
    block_ac1 = compose_anchor_block_ac1(w3_closure_sha)  # (local)
    block_ac4 = compose_anchor_block_ac4(w3_closure_sha)  # (local)

    block_ac1_chars = len(block_ac1)  # (local)
    block_ac4_chars = len(block_ac4)  # (local)
    print(f"=== Composed anchor blocks ===")
    print(f"  §VII.AC.1 block: {block_ac1_chars} chars")
    print(f"  §VII.AC.4 block: {block_ac4_chars} chars")
    print()

    # Anchor-block content_sha256 (over the two blocks concatenated)
    block_concat_bytes = (block_ac1 + block_ac4).encode("utf-8")  # (local)
    block_content_sha = sha256_of_bytes(block_concat_bytes)  # (local)
    print(f"  §VII.AC.1 + §VII.AC.4 block content_sha256: {block_content_sha[:16]}...")
    print()

    # 5. Atomic in-place rewrite of permanent-results-registry.md
    print(f"=== Patching {REGISTRY_PATH} ===")
    patch_diag = patch_registry(REGISTRY_PATH, block_ac1, block_ac4)  # (local)
    for k, v in patch_diag.items():
        print(f"  {k}: {v}")
    print()

    # 6. Post-write verification (5 PASS criteria)
    print(f"=== Post-write verification ===")
    verify_diag = verify_pass_criteria(REGISTRY_PATH, w3_closure_sha)  # (local)
    for k, v in verify_diag.items():
        print(f"  {k}: {v}")
    print()

    # 7. Determine verdict
    all_5_met = bool(verify_diag["all_5_criteria_met"])  # (local)
    if all_5_met:
        # Check INFO branch: criteria a-d met but e SHA mismatch within first 32 chars
        # (already encoded by all_5_met logic; INFO not triggered in PASS path)
        verdict = "PASS"  # (local)
    else:
        # If a-d all pass but e fails on SHA (precise mismatch in first 32 chars only)
        if (verify_diag["all_a"] and verify_diag["all_b"]
                and verify_diag["all_c"] and verify_diag["all_d"]
                and not verify_diag["all_e"]):
            # SHA-only mismatch -> INFO per plan §W3-1.9 INFO clause
            verdict = "INFO"  # (local)
        else:
            verdict = "FAIL"  # (local)

    # 8. Emit 4-tuple
    value = all_5_met  # (local)
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX_TAG)  # (local)
    print(tag)
    print()

    # 9. Save NPZ + JSON artifacts
    np.savez(
        OUT_NPZ,
        gate_id=np.bytes_(GATE_ID.encode("utf-8")),
        verdict=np.bytes_(verdict.encode("utf-8")),
        all_5_criteria_met=np.bool_(all_5_met),
        w3_closure_sha=np.bytes_(w3_closure_sha.encode("utf-8")),
        w3_closure_gate_id=np.bytes_(W3_CLOSURE_GATE_ID.encode("utf-8")),
        block_ac1_chars=np.int64(block_ac1_chars),
        block_ac4_chars=np.int64(block_ac4_chars),
        block_concat_content_sha256=np.bytes_(block_content_sha.encode("utf-8")),
        registry_byte_len_after=np.int64(patch_diag["new_byte_len"]),
        registry_byte_len_before=np.int64(patch_diag["original_byte_len"]),
        audit_sha256=np.bytes_(audit_sha.encode("utf-8")),
        content_sha256=np.bytes_(content_sha.encode("utf-8")),
        anchor1_v1_citation=np.bytes_(
            "3He-B BDI 0D inheritance arrow (S58 Volovik-partition canonical; "
            "canonical_constants.py:1243 w0_FW = -0.918; cross-link to "
            "sessions/framework/registry/branch-iv-canonical.md §3 substrate-"
            "natural anchor 59.8 * Delta_BCS / K_base)".encode("utf-8")
        ),
        anchor2_c1_citation=np.bytes_(
            "Connes 1996 reconstruction (Comm. Math. Phys. 182, 155-176, 1996) "
            "+ NCG axioms 3 (orientability) + 5 (first-order) + 6 (real "
            "structure J) + Schur orthogonality of A_F = C + H + M_3(C)".encode("utf-8")
        ),
    )
    print(f"  saved NPZ: {OUT_NPZ.name}")

    json_diag = {
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value_all_5_criteria_met": all_5_met,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX_TAG,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "w3_closure_gate_id": W3_CLOSURE_GATE_ID,
        "w3_closure_sha_64": w3_closure_sha,
        "patch_diag": patch_diag,
        "verify_diag": verify_diag,
        "block_ac1_chars": block_ac1_chars,
        "block_ac4_chars": block_ac4_chars,
        "block_concat_content_sha256": block_content_sha,
        "n_eval_pass_criteria": N_EVAL,
    }
    OUT_JSON.write_text(
        json.dumps(json_diag, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    print(f"  saved JSON: {OUT_JSON.name}")
    print()

    # 10. Append verdict line + dual-SHA companion row (atomic open("a"))
    line = append_verdict(verdict, value, audit_sha, content_sha)  # (local)
    print(f"=== Verdict appended to {VERDICT_TXT.name} ===")
    print(f"  {line.strip()}")
    print()

    # 11. Final summary
    wall = time.time() - t0  # (local)
    print(f"=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
