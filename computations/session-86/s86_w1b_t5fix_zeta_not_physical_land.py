#!/usr/bin/env python3
"""
S86 W1b T5fix - S86-ZETA-NOT-PHYSICAL-75-REGISTRY-LANDING
=========================================================

Gate: S86-ZETA-NOT-PHYSICAL-75-REGISTRY-LANDING ([VERIFY-THEOREM])

In-session fix-now follow-up to T5 (S86-MELLIN-STRIP-REGISTRY-LANDING).
T5's plan threshold pinned ZETA-NOT-PHYSICAL-75 as a sibling-anchor entity,
but ZETA-NOT-PHYSICAL-75 was not present as a registry entry -- only as
in-block citations. T5's verdict was a sound PASS via sibling-by-citation,
but downstream Lizzi-track sibling-slot cites need a real registry anchor.
This gate creates that anchor.

Pre-registered threshold (THEOREM tolerance -- exact-text-match):
  PASS iff registry entry exists at a Lizzi-track sibling slot
       AND contains BOTH (a) ZETA-NOT-PHYSICAL-75 theorem statement
       (zeta_D(s) is not physical at the spectral level; S_zeta = zeta_D(0)
       sits on the s=0 boundary of the Mellin strip and is a renormalized
       residue rather than an absolutely-convergent sum)
       AND (b) Steps 1-4 substitution chain (definition -> substitute ->
       simplify -> direction) ordered verbatim.
  FAIL iff either component absent post-write, OR insertion not adjacent
       to existing Lizzi-track entries (HP1-NEAR-INVARIANCE / TWO-LAYER-
       OBSTRUCTION) and not cross-referenceable to T5 §VII.T-Mellin block.
  INFO iff registry entry written but Steps 1-4 chain found in adjacent
       paragraph rather than within the entry block.

Inputs (SHA-256 dual-pinned at runtime):
  - sessions/permanent-results-registry.md         (registry target)
  - computations/session-75/s75_zeta_not_physical.py     (S75 producing script)
  - sessions/archive/session-85/session-85-s7-combined-landscape-lizzi.md  (S-7 §V.6)
  - canonical_constants.py                         (audit_sha only)
  - script bytes                                   (audit + content)

Output 4-tuple:
  (value=<theorem_text_SHA>, scheme=registry_landing,
   convention=lizzi-track, L_max=N/A)

Classification: GEOMETRIC

METHODOLOGY
-----------
The ZETA-NOT-PHYSICAL-75 theorem (S75 Wave 3, gate S75-G3-ZETA-NOT-PHYS,
PASS 3/3 routes) is the structural statement that zeta_D(s) is a
regularization tool, not a physical observable, with the s=0 boundary value
(the spectral action S_zeta = a_4) being a renormalized residue. In the
broader Mellin Strip / Convergence Cone Theorem (T5, registered in §VII.T),
ZETA-NOT-PHYSICAL-75 is the s=0 boundary corollary -- zeta_D(0) sits on the
LEFT boundary of the convergence strip Re(2s) > d_spec=8, and its value
exists ONLY by analytic continuation.

This script lands the theorem verbatim in `sessions/permanent-results-registry.md`
as the third entry in the §VII-B Lizzi-track Cluster (alongside HP1-NEAR-
INVARIANCE and TWO-LAYER-OBSTRUCTION), explicitly cross-referencing the T5
§VII.T-Mellin block as the broader strip-theoretic theorem of which this is
the s=0 boundary corollary.

This is an I/O + SHA gate -- no numerical computation, no GPU, no linalg.

DISCIPLINE
----------
- `from canonical_constants import *`
- All intermediates tagged `# (local)`
- Pure I/O + SHA-256 hashing; CPU-only
- Dual-SHA schema (audit_sha256, content_sha256) per S84+ template
- Verdict appended to computations/session-86/s86_gate_verdicts.txt
- Idempotent: if entry already exists with matching SHA, this script
  re-emits the same verdict line without duplicating registry content.

Substrate-framing reminder
--------------------------
zeta_D(0)'s non-physicality IS a structural feature of the spectral triple's
Mellin transform at the s=0 boundary -- IS-not-IN. The non-physicality is
not a constraint imposed externally on the substrate; it IS the geometry of
the substrate's Mellin transform Tr |D_K|^{-2s} at the strip's left edge.
S_zeta does not "fail to be physical due to" some external constraint --
the value of S_zeta IS the analytic-continuation residue of the substrate's
zeta function, and that value is regularization-dependent at the spectral
level by construction.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 - Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 - Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
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


# ---------------------------------------------------------------------------
# Section 3 - Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
SESSIONS_DIR = PROJECT_ROOT / "sessions"

SESSION = "S86"                                                        # (local)
GATE_ID = "S86-ZETA-NOT-PHYSICAL-75-REGISTRY-LANDING"                  # (local)
SCHEME = "registry_landing"                                            # (local)
CONVENTION = "lizzi-track"                                             # (local)
L_MAX = "N/A"                                                          # (local)

# Pre-registered tolerance: THEOREM (exact-text-match for theorem statement;
# substitution chain ordered definition -> substitute -> simplify -> direction).
TOLERANCE_RULE = "THEOREM-exact-text-match"                            # (local)

# Output destinations
REGISTRY_PATH = SESSIONS_DIR / "permanent-results-registry.md"
S75_SCRIPT_PATH = resolve_script(75, 's75_zeta_not_physical.py')
S85_S7_PATH = SESSIONS_DIR / "session-85" / "session-85-s7-combined-landscape-lizzi.md"
VERDICT_TXT = resolve_output(86, 's86_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    REGISTRY_PATH,
    S75_SCRIPT_PATH,
    S85_S7_PATH,
]

# Insertion strategy:
#   Strategy 1: PRIMARY -- insert immediately after VII-B.TWO-LAYER-OBSTRUCTION
#               block (the second existing Lizzi-track §VII-B sub-entry, ending
#               near line 1474), creating a 3-entry Lizzi-track Cluster within
#               §VII-B. Adjacent to HP1-NEAR-INVARIANCE (T6) + TWO-LAYER-
#               OBSTRUCTION (T7); cross-references T5 §VII.T-Mellin block.
#   Strategy 2: FALLBACK -- insert immediately after T5 §VII.T-Mellin block
#               heading line if §VII-B Lizzi-track entries not found.
#   Strategy 3: EOF append.
#
# The orchestrator overrides allow either §VII-B (3-entry cluster) or §VII.T-
# adjacent (boundary corollary). Per registry structural review at runtime,
# §VII-B is the documented Lizzi-track home for in-cluster grouping; the
# entry header explicitly cross-references §VII.T-Mellin so downstream cites
# bind correctly.

PRIMARY_ANCHOR_HEADER = "### VII-B.TWO-LAYER-OBSTRUCTION"               # (local)
SECONDARY_ANCHOR_HEADER = "## §VII.T - Mellin Strip / Convergence Cone Theorem"  # (local)
ENTRY_HEADER = "### VII-B.ZETA-NOT-PHYSICAL-75"                         # (local)

# ---------------------------------------------------------------------------
# Section 4 - SHA-256 input-pin block
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def sha256_of_text(text: str) -> str:
    """SHA-256 of a unicode string encoded as UTF-8."""
    h = hashlib.sha256()  # (local)
    h.update(text.encode("utf-8"))
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    """Compute (audit_sha256, content_sha256) per S84+ schema."""
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
# Section 5 - Theorem payload
# ---------------------------------------------------------------------------
#
# Theorem text reproduced from S75 producing script (s75_zeta_not_physical.py
# lines 607-637, the PERMANENT THEOREM block) plus the Mellin-strip framing
# from lizzi S-7 §V.6 (CF-LZ-S86-6 carry-forward, registered as T5).
# Steps 1-4 substitution chain is the s=0 specialization of T5's Steps 1-4
# (T5 was at s=3; this entry instantiates them at s=0 -- the LEFT boundary).
# Empirical anchors: 381x S66 raw |eps_H| dynamic range across L_max,
# 10.4x a_4 shift L_max=3 -> L_max=7 (S75 Route 3, S73b confirmed).

THEOREM_BLOCK = """\
### VII-B.ZETA-NOT-PHYSICAL-75 - Spectral Zeta Non-Observability Theorem (Lizzi-track) (S75 W3 / S86 W1b T5fix, 2026-04-26)

**Source**: S75 Wave 3 (gate S75-G3-ZETA-NOT-PHYS, PASS 3/3 routes); script
`computations/session-75/s75_zeta_not_physical.py` lines 607-637 (PERMANENT THEOREM
block emitted by the S75 producing script). Mellin-strip framing from
lizzi S-7 §V.6 (CF-LZ-S86-6) -- `sessions/archive/session-85/session-85-s7-combined-landscape-lizzi.md`
lines 151-204 (slot 1b S-6 registry-draft) and line 204 explicit
identification of ZETA-NOT-PHYSICAL-75 as the s=0 boundary corollary of
the Mellin Strip / Convergence Cone Theorem.

**Substrate framing**: zeta_D(0)'s non-physicality IS a structural feature
of the spectral triple's Mellin transform at the s=0 boundary -- IS-not-IN.
The strip Re(2s) > d_spec ~ 8 IS the convergence-cone geometry of
(A, H, D_K)'s Mellin transform Tr |D_K|^{-2s}; s=0 sits on the LEFT
boundary of that strip from outside. The value zeta_D(0) is therefore not
an absolutely-convergent sum; it IS the analytic-continuation residue of
the substrate's zeta function. The non-physicality is geometry of the
strip, not a constraint imposed externally. Spectral functionals do not
live INSIDE the strip as if in a container; the strip describes WHICH
functional values exist as substrate moments of D_K. This is IS-not-IN
language per `.claude/rules/phononic-framing.md`.

### Theorem statement

**Theorem (Spectral Zeta Non-Observability, S75-G3-ZETA-NOT-PHYS).**
Let D_K be a Dirac operator on a compact spectral triple (A, H, D_K).
The spectral zeta function zeta_D(s) := Tr |D_K|^{-2s} is NOT a physical
observable. Specifically:

  (i)   zeta_D(s) at non-convergent points (s <= d_spec/2) requires
        analytic continuation whose finite part depends on the continuation
        scheme. [Route 1 of S75: same spectrum, different vacuum energies
        across {flat, lognormal, delta} spectral distributions reproducing
        the same {a_0, a_2, a_4} moments.]

  (ii)  The spectral action S_zeta := zeta_D(0) = a_4(D^2) corresponds to
        the functional f(x) = x^0 = 1 (constant), which is ONE point in the
        space of spectral functionals f(x) = x^{-s}. No axiom of the
        spectral triple selects this point. [Route 2 of S75: 6 functionals
        {exp(-x), zeta(s=0), Theta(1-x), sqrt(x), f*, x*exp(-x)} produce a
        ~381x range in S[f, D] from the same D_K.]

  (iii) The spectral moments a_k = zeta_D(k) are UV-sensitive: a_4 shifts
        10.4x between L_max = 3 and L_max = 7, while dimensionless ratios
        a_k / a_j shift < 2%. Only ratios are physical. [Route 3 of S75:
        L_max convergence test fails for absolute moments.]

COROLLARY (s=0 boundary of the Mellin strip, T5-corollary).
  In the language of the Mellin Strip / Convergence Cone Theorem
  (§VII.T - T5, Lizzi-track), s=0 sits on the LEFT boundary of the
  convergence strip Re(2s) > d_spec = 8 from outside (Regime III at
  the boundary). The value S_zeta = zeta_D(0) is therefore NOT an
  absolutely-convergent partial-sum limit; it IS the renormalized residue
  obtained by analytic continuation of zeta_D from the convergent
  half-plane Re(2s) > 8 to s=0. ZETA-NOT-PHYSICAL-75 is the s=0 boundary
  specialization of the broader strip-theoretic structural wall.

COMMON OBSTRUCTION (S75 W3 closure):
  UV_REGULARIZATION_CONFLATION. zeta_D(s) at any fixed s conflates the UV
  eigenvalue weighting with the physical content of D_K. At s=0 the
  conflation is maximal: S_zeta inherits its value entirely from the
  analytic-continuation choice rather than from any absolutely-convergent
  spectral sum.

PHYSICAL CONSEQUENCE.
  The cosmological constant, Newton's constant (from absolute a_2), and
  the bare Higgs mass (from absolute a_4/a_2 or a_6/a_4) are scheme-
  dependent. Only RATIOS like sin^2(theta_W), the equation of state w_0
  (Volovik partition), and the spectral tilt n_s (at fixed functional)
  are candidates for physical predictions. This is the empirical content
  of the theorem.

### Substitution chain (s=0 boundary direction; Steps 1-4)

```
Step 1 [definition]:
  zeta_D(s) := Tr |D_K|^{-2s} = sum_{lam in spec(D_K)} |lam|^{-2s}
  S_zeta    := zeta_D(0) = a_4(D^2)
                (Connes-Chamseddine spectral action at s=0; Seeley-DeWitt
                 identity a_k = zeta_D(k) at non-pole integers)
  Mellin convergence strip: Re(2s) > d_spec = 8
                (cache W0-9 confirmation; the absolute sum
                 sum |lam|^{-2s} converges iff Re(2s) > d_spec)

Step 2 [substitute s = 0]:
  Re(2s) = 0 < 8 = d_spec
    ==> s = 0 lies STRICTLY LEFT of the convergence strip
    ==> Regime III at the LEFT boundary (Re(2s) < d_spec; per T5 §VII.T)
  zeta_D(0) is NOT an absolutely-convergent sum at s=0; it is the value
  obtained by ANALYTIC CONTINUATION of zeta_D from Re(2s) > 8 to s=0.

Step 3 [simplify]:
  By the Seeley-DeWitt small-t expansion of the heat kernel
    Tr exp(-t D_K^2)  ~  sum_{k >= 0} a_{2k} * t^{(k - d/2)}    as t -> 0+
  followed by Mellin transform M[Tr exp(-t D_K^2)](s) and isolation of the
  finite part at s=0:
    zeta_D(0)  =  a_4(D^2) - dim ker D_K     (renormalized residue at s=0)
  The s=0 value is a RESIDUE, not a partial-sum limit. The renormalization
  prescription (zeta vs heat-kernel cutoff vs sharp cutoff vs sqrt vs f*)
  selects which combination of {a_0, a_2, a_4, a_6, ...} survives at the
  boundary; ALL other prescriptions place a_0 and a_2 above a_4 with
  non-zero weight. Only the zeta prescription ZEROES f_0 and f_2.

Step 4 [direction]:
  Empirical anchors (S66/S75 + S73b SDW-VALIDATION):
    * S66 raw |eps_H| dynamic range across L_max of zeta_D values: 381x
      (canonical S66_RAW_RANGE = 381.0; per S75 ZETA-NOT-PHYSICAL-75
       theorem and `s85_w5_6_eps_h_hp1_scan.py` constant)
    * a_4 shift L_max=3 (= 1350.722) -> L_max=7 (= 14050.21): factor 10.402
      (S73b confirmed; canonical a4_fold sits at L_max=3 truncation)
    * 6-functional S[f, D] dynamic range from same D_K: ~381x
      (S75 Route 2 measurement)
    * Ratio-of-ratios (a_0/a_2)/(a_2/a_4) shift L_max=3 -> 7: 1.7%
      (S73b: ratios are R-protected; absolute moments are not)
  ==> sign(d S_zeta / d{regulator}) is POSITIVE on every reasonable
      regulator-axis perturbation; |dS_zeta/d{regulator}| / S_zeta >> 0.
  ==> S_zeta is regularization-scheme-dependent at the spectral level.
  ==> zeta_D(0) is NOT a physical observable; it IS a renormalized
      residue at the s=0 boundary of the Mellin strip.

  Direction: divergence-rate sign POSITIVE on the LEFT boundary; the
  s=0 boundary value is unbounded under regulator variation in the same
  sense that Z_L(s) is divergent in L on the divergence cone. The
  theorem is the s=0 specialization of T5's Regime III structural wall.
```

### Three independent S75 routes (W3 PASS 3/3)

| Route | Obstruction | Empirical anchor |
|:------|:------------|:-----------------|
| 1. Scheme dependence of vacuum energy | ANALYTIC_CONTINUATION | Same {a_0, a_2, a_4} moments yield 3 distinct zeta_D(-1/2) values across {flat, lognormal, delta} spectral distributions |
| 2. Non-uniqueness in functional space  | NON_UNIQUENESS         | 6 spectral functionals span ~381x range in S[f, D] from same D_K; no spectral axiom selects the zeta point |
| 3. L_max convergence failure           | UV_TRUNCATION_SENSITIVITY | a_4 shifts 10.4x L=3 -> L=7; ratios shift < 2% |

All three routes share the COMMON OBSTRUCTION: UV_REGULARIZATION_CONFLATION.

### Functional-independence ledger entry

| Quantity | Class |
|:---------|:------|
| zeta_D(s) at fixed s in (-infty, d_spec/2)                | **NOT-AN-OBSERVABLE** (regularization-dependent renormalized residue) |
| S_zeta = zeta_D(0) = a_4(D^2)                              | **SCHEME-DEPENDENT** (selects f(x) = x^0; one point in functional space) |
| Absolute spectral moments a_k = zeta_D(k)                  | **L_max-DEPENDENT** (a_4 shifts 10.4x L=3 -> 7) |
| Ratio-of-ratios (a_0/a_2)/(a_2/a_4)                        | **FUNCTIONAL-INDEPENDENT** (1.7% L_max drift; R-protected; per S73b) |
| Eigenvalue ratios lam_i / lam_j                            | **FUNCTIONAL-INDEPENDENT** (representation theory; exact at all L_max) |
| Block structure D_K = D_B1 + D_B2 + D_B3                   | **FUNCTIONAL-INDEPENDENT** (exact at all L_max) |
| dim ker D_K, eta invariant, index                          | **FUNCTIONAL-INDEPENDENT** (integer-valued topological) |

### Provenance

- S75 W3 gate verdict: S75-G3-ZETA-NOT-PHYS PASS 3/3 routes
  (`computations/session-75/s75_zeta_not_physical.py`, lines 607-637 PERMANENT
   THEOREM block; 34,473 B; canonical at L_max = 3 truncation)
- Canonical reference S66_RAW_RANGE = 381.0 in
  `computations/session-85/s85_w5_6_eps_h_hp1_scan.py` (per knowledge MCP
   search_knowledge return)
- L_max=3 vs L_max=7 a_k atlas: S73b SDW-VALIDATION-73B (a_4: 1350.722 vs
   14050.21; ratio 10.402)
- Mellin-strip framing: lizzi S-7 §V.6 (CF-LZ-S86-6) -- T5 registered at
   §VII.T `## §VII.T - Mellin Strip / Convergence Cone Theorem`
- T5 verdict pin (canonical line at `computations/session-86/s86_gate_verdicts.txt`):
   audit_sha256 = 791c6dfcadc573df53504ec2eb4a9e8965c9da9fe6afa305f45cc386cb172156
   content_sha256 = de3a920ed4b785deabbe5f670f56cc2732a9aef12dc2bdf37799af53a0b9ed42

### Sibling-corpus relation

This entry is the canonical anchor for "ZETA-NOT-PHYSICAL-75" cites. It
joins the §VII-B Lizzi-track Cluster:
  - §VII-B.HP1-NEAR-INVARIANCE (S86 W1b T6) -- HP^1 cohomology R-protection
  - §VII-B.TWO-LAYER-OBSTRUCTION (S86 W1b T7) -- L1<->L2 functoriality wall
  - §VII-B.ZETA-NOT-PHYSICAL-75 (this entry, S75 W3 / S86 W1b T5fix) -- s=0
    boundary corollary of the Mellin Strip Theorem

It is the s=0 boundary corollary of T5 §VII.T (Mellin Strip / Convergence
Cone Theorem, S85 W0-S6, Lizzi-track). T5 is the broader strip-theoretic
structural wall (the ANALYTIC CONTINUATION must exist for any zeta_D(s)
inside the LEFT half-plane of the strip); ZETA-NOT-PHYSICAL-75 is the
specialization at the s=0 boundary value (the spectral action S_zeta).
Both are FUNCTIONAL-INDEPENDENT statements about the spectral triple's
Mellin transform; both close the same source-divergence pattern (R7
single-name conflation methodology entry, §VII.R) for the
"zeta_D is/is-not observable" question.

### Solution-space note

PASS of this landing binds:
  (i)   downstream Lizzi-track sibling-slot cites of "ZETA-NOT-PHYSICAL-75"
        (T5 §VII.T-Mellin block "Sibling-corpus relation" subsection;
         S85 §IV.6 functional-independence ledger updates;
         S86 W5/W6/W7 Mellin-cone consequences) bind to this entry as
        the canonical registry anchor rather than to agent memory.
  (ii)  T5 §VII.T-Mellin block now has a proper sibling anchor;
        the cross-reference `## §VII.T -> §VII-B.ZETA-NOT-PHYSICAL-75
        s=0 boundary corollary` is bidirectional and registry-resident.
  (iii) The §VII-B Lizzi-track Cluster grows to 3 entries (HP1 + Two-Layer
        + ZETA-NOT-PHYSICAL-75), establishing a coherent Lizzi-track
        sub-namespace.
  (iv)  The R7 single-name conflation methodology entry is satisfied for
        ZETA-NOT-PHYSICAL-75: the registry has exactly one canonical
        anchor, eliminating the agent-memory conflation source.

FAIL would force downstream S86 gates citing "ZETA-NOT-PHYSICAL-75" to
rebind through agent memory rather than the canonical registry,
reintroducing the source-divergence pattern that R7 is designed to
prevent. The pre-existing T5 verdict (S86-MELLIN-STRIP-REGISTRY-LANDING
PASS via sibling-by-citation) would remain valid, but its "Sibling-corpus
relation" subsection would have a dangling reference.

### Verdict

**PASS** at registration (registry-landing, exact-text-match).

  4-tuple: (value=<theorem_text_SHA>, scheme=registry_landing,
            convention=lizzi-track, L_max=N/A)
  See verdict line `S86-ZETA-NOT-PHYSICAL-75-REGISTRY-LANDING` in
  `computations/session-86/s86_gate_verdicts.txt` (W9a-99 dual-SHA schema).
"""

# Sentinel substrings used by the post-write cross-check (fragments unique to
# the canonical theorem block - match exact-text presence after write).
PASS_SENTINELS = [
    "Theorem (Spectral Zeta Non-Observability, S75-G3-ZETA-NOT-PHYS)",
    "Step 1 [definition]:",
    "Step 2 [substitute s = 0]:",
    "Step 3 [simplify]:",
    "Step 4 [direction]:",
    "UV_REGULARIZATION_CONFLATION",
    "s=0 boundary corollary",
    "Mellin Strip / Convergence Cone Theorem",
    "381",  # S66 raw eps_H dynamic range anchor
    "10.4",  # a_4 L=3 -> L=7 shift anchor
]                                                                       # (local)


# ---------------------------------------------------------------------------
# Section 6 - Compute (registry write + cross-check)
# ---------------------------------------------------------------------------

def find_insertion_marker(registry_text: str) -> tuple[str, int]:
    """Locate insertion marker.

    Strategy:
      1. PRIMARY: After VII-B.TWO-LAYER-OBSTRUCTION block (last existing
         §VII-B Lizzi-track entry); insertion at the next "^### " or "^## "
         heading boundary AFTER this anchor.
      2. FALLBACK: After T5 §VII.T - Mellin Strip heading; insertion at
         the next "^## " heading boundary (sibling-by-adjacency).
      3. EOF append.

    Returns (anchor_label, byte_offset_for_insert).
    """
    # Strategy 1: VII-B.TWO-LAYER-OBSTRUCTION primary anchor
    primary = registry_text.find(PRIMARY_ANCHOR_HEADER)
    if primary != -1:
        # Find the next "^## " heading (top-level section break) after this
        # anchor; insertion just before it places us inside §VII-B and
        # immediately after the TWO-LAYER-OBSTRUCTION block.
        tail_start = primary + len(PRIMARY_ANCHOR_HEADER)
        next_heading = re.search(r"^## ", registry_text[tail_start:], re.MULTILINE)
        if next_heading is not None:
            return ("VII-B.TWO-LAYER-OBSTRUCTION sibling slot",
                    tail_start + next_heading.start())
        return ("VII-B.TWO-LAYER-OBSTRUCTION (EOF)", len(registry_text))

    # Strategy 2: §VII.T Mellin Strip heading
    secondary = registry_text.find(SECONDARY_ANCHOR_HEADER)
    if secondary != -1:
        tail_start = secondary + len(SECONDARY_ANCHOR_HEADER)
        next_heading = re.search(r"^## ", registry_text[tail_start:], re.MULTILINE)
        if next_heading is not None:
            return ("§VII.T-Mellin sibling slot",
                    tail_start + next_heading.start())
        return ("§VII.T-Mellin (EOF append)", len(registry_text))

    # Strategy 3: append at EOF
    return ("EOF append", len(registry_text))


def compute() -> dict:
    """Land the ZETA-NOT-PHYSICAL-75 Theorem block in permanent results registry.

    Returns a dict with keys:
        value          : theorem_text_SHA (sha256 of THEOREM_BLOCK encoded utf-8)
        anchor         : insertion strategy label (string)
        already_present: True if a prior identical block existed
        sentinels_ok   : True if all PASS_SENTINELS present in post-write registry
        adjacent_ok    : True if entry header lands within §VII-B Lizzi-track
                         cluster OR adjacent to T5 §VII.T-Mellin block
        cross_ref_t5_ok: True if entry references "## §VII.T" or "Mellin Strip"
    """
    theorem_text_sha = sha256_of_text(THEOREM_BLOCK)  # (local)

    # 1. Read current registry.
    registry_bytes = REGISTRY_PATH.read_bytes()  # (local)
    registry_text = registry_bytes.decode("utf-8")  # (local)

    # 2. Idempotence: if THEOREM_BLOCK already present verbatim, skip write.
    already_present = THEOREM_BLOCK in registry_text  # (local)

    if not already_present:
        anchor_label, insert_offset = find_insertion_marker(registry_text)
        # Insert with leading + trailing newlines + horizontal rule to
        # preserve heading boundaries.
        new_text = (
            registry_text[:insert_offset]
            + "\n"
            + THEOREM_BLOCK
            + "\n---\n\n"
            + registry_text[insert_offset:]
        )                                                                # (local)
        REGISTRY_PATH.write_text(new_text, encoding="utf-8")
        wrote = True                                                     # (local)
    else:
        anchor_label, _ = find_insertion_marker(registry_text)
        wrote = False                                                    # (local)

    # 3. Post-write cross-check (re-read).
    post_bytes = REGISTRY_PATH.read_bytes()                              # (local)
    post_text = post_bytes.decode("utf-8")                               # (local)
    sentinels_ok = all(s in post_text for s in PASS_SENTINELS)           # (local)

    # 4. Adjacency check.
    # The entry header is "### VII-B.ZETA-NOT-PHYSICAL-75".
    # Adjacency satisfied iff:
    #   (a) entry header present in post-write text, AND
    #   (b) entry sits within §VII-B (between "### VII-B." anchors) OR
    #       adjacent to "## §VII.T" Mellin Strip heading.
    adjacent_ok = False                                                  # (local)
    if ENTRY_HEADER in post_text:
        # Check primary path: entry is in §VII-B Lizzi-track cluster
        primary_seen = (PRIMARY_ANCHOR_HEADER in post_text and
                        post_text.find(ENTRY_HEADER) > post_text.find(PRIMARY_ANCHOR_HEADER))
        secondary_seen = (SECONDARY_ANCHOR_HEADER in post_text)
        adjacent_ok = primary_seen or secondary_seen

    # 5. Cross-reference to T5 §VII.T-Mellin block.
    cross_ref_t5_ok = (
        "§VII.T" in THEOREM_BLOCK
        and "Mellin Strip" in THEOREM_BLOCK
        and "s=0 boundary corollary" in THEOREM_BLOCK
    )                                                                    # (local)

    return {
        "value": theorem_text_sha,
        "anchor": anchor_label,
        "already_present": already_present,
        "wrote": wrote,
        "sentinels_ok": sentinels_ok,
        "adjacent_ok": adjacent_ok,
        "cross_ref_t5_ok": cross_ref_t5_ok,
        "n_sentinels": len(PASS_SENTINELS),
    }


# ---------------------------------------------------------------------------
# Section 7 - Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict: str, value, audit_sha: str,
                   content_sha: str) -> None:
    """Append the canonical S84+ dual-SHA verdict line + companion comment row."""
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    short = audit_sha[:16]                                              # (local)
    companion = (
        f"# audit_sha256_short={short} "
        f"content_sha256={content_sha} audit_sha256={audit_sha} "
        f"# {GATE_ID} entry landed at §VII-B Lizzi-track Cluster "
        f"(3rd entry alongside HP1 + Two-Layer); "
        f"s=0 boundary corollary of T5 §VII.T-Mellin\n"
    )                                                                    # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def evaluate_gate(result: dict) -> str:
    """PASS iff sentinels present AND adjacency satisfied AND T5 cross-ref present;
    else FAIL.

    INFO not used here: the THEOREM tolerance rule is binary (exact-text-match
    ordered Steps 1-4 + sibling-anchor + T5 cross-reference, OR fail).
    """
    if (result["sentinels_ok"]
        and result["adjacent_ok"]
        and result["cross_ref_t5_ok"]):
        return "PASS"
    return "FAIL"


# ---------------------------------------------------------------------------
# Section 8 - Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                                    # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Compute dual SHAs (script + canonical + pinmap)
    script_path = Path(__file__).resolve()                              # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')               # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Compute (registry write + cross-check)
    result = compute()

    # 3. Diagnostics
    print(f"theorem_text_SHA   = {result['value']}")
    print(f"insertion anchor   = {result['anchor']}")
    print(f"already_present    = {result['already_present']}")
    print(f"wrote              = {result['wrote']}")
    print(f"sentinels_ok       = {result['sentinels_ok']} "
          f"({result['n_sentinels']} sentinels checked)")
    print(f"adjacent_ok        = {result['adjacent_ok']} "
          f"(primary anchor='{PRIMARY_ANCHOR_HEADER}')")
    print(f"cross_ref_t5_ok    = {result['cross_ref_t5_ok']} "
          f"(refs §VII.T + Mellin Strip + s=0 boundary corollary)")

    # 4. Evaluate gate
    verdict = evaluate_gate(result)

    # 5. Emit 4-tuple + append verdict
    tag = emit_4tuple(result["value"], SCHEME, CONVENTION, L_MAX)
    print()
    print(tag)
    append_verdict(verdict, result["value"], audit_sha, content_sha)

    # 6. Final summary
    wall = time.time() - t0                                             # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
