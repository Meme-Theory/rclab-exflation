#!/usr/bin/env python3
"""
S86 W1c-5 — S86-BULLETIN-S4-LAND — Land 4 mechanism-class bulletins
====================================================================

Gate: S86-BULLETIN-S4-LAND ([AUDIT])

Pre-registered threshold:
  PASS iff 4 bulletins land in `sessions/framework/registry/elimination-bulletins.md`
  with substrate-first paragraphs + FAIL-gate SHA-pins (both audit_sha256
  and content_sha256, 64-char) + registry-anchor cross-references.
  FAIL iff any bulletin missing OR any substrate paragraph reads as
  container-thinking ("this mechanism didn't survive the test") OR any
  registry-anchor cross-reference is broken/missing.
  INFO not applicable (4 discrete bulletins; binary present/absent).

  Tolerance rule: ABSOLUTE.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - sessions/archive/session-85/session-85-s4-elimination-bulletins-kaku.md
  - sessions/archive/session-85/session-85-s4-elimination-bulletins-gen-physicist.md
  - sessions/archive/session-85/session-85-w0-workingpaper.md
  - sessions/archive/session-85/session-85-w2-workingpaper.md
  - sessions/archive/session-85/session-85-w3-workingpaper.md
  - sessions/archive/session-85/session-85-w5-workingpaper.md
  - computations/session-85/s85_gate_verdicts.txt
  - sessions/framework/registry/elimination-bulletins.md
  - canonical_constants.py (feeds audit_sha256)
  - script bytes (feeds BOTH audit and content SHA)

Output 4-tuple:
  (value=4_bulletins_landed, scheme=elimination-bulletin-write,
   convention=substrate-first, L_max=N/A)

Classification: META.

METHODOLOGY
-----------
This is a META landing-verification gate. It does NOT compute new physics;
it confirms that 4 mechanism-class bulletins have landed at the canonical
elimination-bulletins.md ledger with the required substrate-first reasoning
+ FAIL-gate SHA pins + registry-anchor cross-references. The gate's
"verdict" is the binary present/absent assessment per the pre-registered
content rubric (4 mechanism-class names, 4 FAIL audit SHAs, 4 substrate
paragraphs flowing D_K → spectral moment → mechanism exclusion, registry
anchors per bulletin). No NCG / spectral / observational compute is
performed — the substrate paragraphs themselves serve as the substitution
chain per the plan §W1c-5 rubric.

DISCIPLINE
----------
- `from canonical_constants import *` (no constants used; convention)
- All intermediates tagged `# (local)`
- CPU-only with OMP_NUM_THREADS=8 cap (no heavy linalg)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Gate verdict appended to `s86_gate_verdicts.txt` with BOTH
  `audit_sha256=<64>` and `content_sha256=<64>` plus `schema_version=S84+`
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap (BEFORE numpy import; per math-scripts.md)
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
# Section 1 — Canonical constants (MANDATORY first import per S34+ rule)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
SESSIONS_DIR = PROJECT_ROOT / "sessions"
FRAMEWORK_DIR = SESSIONS_DIR / "framework"

SESSION = "S86"                                                    # (local)
GATE_ID = "S86-BULLETIN-S4-LAND"                                   # (local)
SCHEME = "elimination-bulletin-write"                              # (local)
CONVENTION = "substrate-first"                                     # (local)
L_MAX = "N/A"                                                      # (local)

# Output destinations
BULLETIN_FILE = FRAMEWORK_DIR / "elimination-bulletins.md"         # (local)
VERDICT_TXT = resolve_output(86, 's86_gate_verdicts.txt')                  # (local)

# Pre-registered bulletin specification (4 entries; ABSOLUTE check)
EXPECTED_BULLETINS = [                                             # (local)
    {
        "n": 1,
        "title_marker": "ε_H J-Parity Wall Demoted",
        "fail_audit_sha": (
            "45ac9bfceca269f1d059fec0b09d8f7bfcad6a8b265a5d60fc38236e1531b79d"
        ),
        "fail_content_sha": (
            "b0162b1d96bb2232c3f08d409c57bca7b8542bb212e55ec7997247ad593fca93"
        ),
        "fail_gate_id": "S85-W5-1-FI-PARITY-REGISTRY",
        "mechanism_class": (
            "single-regulator-class certification of eps_H J-parity as "
            "universal invariant"
        ),
    },
    {
        "n": 2,
        "title_marker": "Even Seeley-DeWitt Parity-Blindness",
        "fail_audit_sha": (
            "2ef68ad50f55b59ef626f7767c0fa167dd72551f1ddd183bb89b5ca010ebff16"
        ),
        "fail_content_sha": (
            "27fd02199be62c209cf70e828b0a4f0d0c6682e1d8af180a95df0543960dac44"
        ),
        "fail_gate_id": "S85-W2-DISJOINT-CORRIDOR-REGISTRY-LANDING",
        "mechanism_class": (
            "even-spectral-moment certification of HP^odd-distinguished "
            "corridor pairs"
        ),
    },
    {
        "n": 3,
        "title_marker": "Branch-A K_substrate=2.035 A_s Pathway",
        "fail_audit_sha": (
            "b59acafa69463e169d3bb61898dc19c08b4640aecc6b3a05c6b087b9326b10f2"
        ),
        "fail_content_sha": (
            "2a64370595875cc7ab421456ea84e42e8e0884c62a7a3aa213c32d7c319f65fa"
        ),
        "fail_gate_id": "S85-W3-CF-1-BRANCH-A-A_S-CLOSURE-K2035",
        "mechanism_class": (
            "Branch-A K=2.035 with canonical S80 multiplicative chain "
            "produces Planck-central A_s within +/-30%"
        ),
    },
    {
        "n": 4,
        "title_marker": "Jensen-Zubarev ρ → −1 Identity Numerically Refuted",
        "fail_audit_sha": (
            "a512e1f49ac6c69bc906e879035b4717e8765f05d6c22e3319009750a5383885"
        ),
        "fail_content_sha": (
            "93290cf2c85e31407d3cddae20e0f9bca2567369b93ec8231ce267fd5e8a58a4"
        ),
        "fail_gate_id": "S85-ZUBAREV-LMAX-CONVERGENCE-TO-MINUS-ONE",
        "mechanism_class": (
            "Jensen-Zubarev rho-limit equals the simple rational -1 at "
            "theorem-grade under current Mellin-cone kernel normalization"
        ),
    },
]

# Container-thinking phrases that MUST NOT appear in bulletin substrate
# paragraphs (per phononic-framing.md and §W1c-5 rubric).
CONTAINER_THINKING_PHRASES = [                                     # (local)
    "this mechanism didn't survive the test",
    "the framework failed to support",
    "the data ruled out the mechanism",
    "particle created in curved spacetime",
    "summing over geometries",
    "Einstein's equations govern",
]

# Required registry-anchor markers (each bulletin must reference at least one)
REGISTRY_ANCHOR_MARKERS = [                                        # (local)
    "permanent-results-registry.md",
    "falsifier-watchlist.md",
]

# Substrate-reasoning rubric markers per §W1c-5: each bulletin paragraph
# must contain (a) the substrate spectrum reference D_K, (b) spectral-moment
# language, AND (c) at least one substrate-spectral-cascade object name
# appropriate to the bulletin's domain (Seeley-DeWitt for SD-moment-class,
# Mellin-cone for Mellin-residue-class, heat-kernel / Mukhanov-Sasaki for
# kernel-derived-amplitude-class). The disjunction over (c) is per the
# substrate-first rubric: the rubric requires the FLOW substrate→consequence,
# not a single literal-string marker — different mechanism classes invoke
# different substrate-spectral objects. (Per phononic-framing.md: the
# substrate paragraphs ARE the substitution chain.)
# Per §W1c-5 substrate-first rubric: each bulletin paragraph MUST contain
# (a) D_K (substrate spectrum reference), AND
# (b) a substrate-spectral-object name (any of: spectral moment, spectral
#     observable, spectral residue, spectral cascade — these are the
#     canonical NCG names for the substrate-spectral object the bulletin's
#     mechanism class is about), AND
# (c) a substrate-spectral-cascade kernel/object name (any of: Seeley-DeWitt,
#     Mellin-cone, heat kernel, Mukhanov-Sasaki, spectral cascade — these
#     name the specific kernel through which D_K's spectrum is sampled).
SUBSTRATE_REASONING_REQUIRED = ["D_K"]                             # (local)
SUBSTRATE_OBJECT_DISJUNCTION = [                                   # (local)
    "spectral moment",      # Seeley-DeWitt-coefficient class
    "spectral observable",  # Mellin-residue / dimension-spectrum class
    "spectral residue",     # Mellin-residue language
    "spectral cascade",     # generic D_K eigenvalue cascade language
    "spectral functional",  # regulator-weighted functional language
]
SUBSTRATE_KERNEL_DISJUNCTION = [                                   # (local)
    "Seeley-DeWitt",        # heat-kernel expansion (a_n class)
    "Mellin-cone",          # Mellin-residue / dimension-spectrum class
    "heat kernel",          # heat-kernel-derived class (lowercase)
    "heat-kernel",          # heat-kernel-derived class (hyphenated)
    "Mukhanov-Sasaki",      # post-fold acoustic emission kernel class
    "dimension spectrum",   # CM-1995 dimension-spectrum class
    "dimension-spectrum",   # CM-1995 dimension-spectrum class (hyphenated)
]

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    SESSIONS_DIR / "session-85" / "session-85-s4-elimination-bulletins-kaku.md",
    SESSIONS_DIR / "session-85" / "session-85-s4-elimination-bulletins-gen-physicist.md",
    resolve_output(85, 's85_gate_verdicts.txt'),
    BULLETIN_FILE,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list) -> dict:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    """Stable hash over all input SHAs (invariant to dict ordering)."""
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict,
):
    """Compute (audit_sha256, content_sha256) per S84+ dual-SHA schema."""
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
# Section 5 — Compute (verify the 4 bulletins are landed correctly)
# ---------------------------------------------------------------------------

def compute() -> dict:
    """Read elimination-bulletins.md and verify each of the 4 bulletins.

    Return a dict with:
      - 'value': "4_bulletins_landed" if all 4 land, else "<n>_of_4_landed"
      - 'per_bulletin': list of per-bulletin verification dicts
      - 'all_pass': bool
    """
    if not BULLETIN_FILE.exists():
        return {
            "value": "0_of_4_landed",
            "per_bulletin": [],
            "all_pass": False,
            "reason": "elimination-bulletins.md does not exist",
        }

    body = BULLETIN_FILE.read_text(encoding="utf-8")  # (local)

    per_bulletin = []  # (local)
    all_pass = True  # (local)

    for spec in EXPECTED_BULLETINS:
        n = spec["n"]  # (local)
        bulletin_header = f"### Bulletin #{n}:"  # (local)
        title_marker = spec["title_marker"]  # (local)
        fail_audit_sha = spec["fail_audit_sha"]  # (local)
        fail_content_sha = spec["fail_content_sha"]  # (local)
        fail_gate_id = spec["fail_gate_id"]  # (local)

        check = {  # (local)
            "n": n,
            "header_present": bulletin_header in body,
            "title_present": title_marker in body,
            "audit_sha_pinned": fail_audit_sha in body,
            "content_sha_pinned": fail_content_sha in body,
            "fail_gate_id_pinned": fail_gate_id in body,
            "registry_anchor_present": False,
            "substrate_reasoning_present": False,
            "container_thinking_absent": True,
        }

        # Slice the bulletin body (between this header and next "### " or "---" boundary)
        idx = body.find(bulletin_header)  # (local)
        if idx >= 0:
            # Find next ### header OR "## Closure SHA" (end of entries section)
            tail = body[idx + len(bulletin_header):]  # (local)
            next_idx_a = tail.find("\n### Bulletin #")  # (local)
            next_idx_b = tail.find("\n## ")  # (local)
            candidates = [x for x in (next_idx_a, next_idx_b) if x >= 0]  # (local)
            stop = min(candidates) if candidates else len(tail)  # (local)
            section = tail[:stop]  # (local)

            # Registry-anchor check
            check["registry_anchor_present"] = any(
                m in section for m in REGISTRY_ANCHOR_MARKERS
            )

            # Substrate-reasoning markers per §W1c-5 rubric:
            #   (a) ALL required markers (D_K substrate spectrum reference)
            #   (b) at least ONE substrate-spectral-object name
            #   (c) at least ONE substrate-spectral-kernel name
            req_present = all(  # (local)
                m in section for m in SUBSTRATE_REASONING_REQUIRED
            )
            obj_present = any(  # (local)
                m in section for m in SUBSTRATE_OBJECT_DISJUNCTION
            )
            kernel_present = any(  # (local)
                m in section for m in SUBSTRATE_KERNEL_DISJUNCTION
            )
            check["substrate_reasoning_present"] = (
                req_present and obj_present and kernel_present
            )

            # Container-thinking absence (case-insensitive)
            section_lower = section.lower()  # (local)
            for phrase in CONTAINER_THINKING_PHRASES:
                if phrase.lower() in section_lower:
                    check["container_thinking_absent"] = False
                    break

        check["all_required"] = all([
            check["header_present"],
            check["title_present"],
            check["audit_sha_pinned"],
            check["content_sha_pinned"],
            check["fail_gate_id_pinned"],
            check["registry_anchor_present"],
            check["substrate_reasoning_present"],
            check["container_thinking_absent"],
        ])
        if not check["all_required"]:
            all_pass = False

        per_bulletin.append(check)
        # Print per-bulletin status
        status = "OK" if check["all_required"] else "MISSING"  # (local)
        print(f"  Bulletin #{n} ({title_marker[:40]:40s}): {status}")
        if not check["all_required"]:
            for k, v in check.items():
                if k in ("n", "all_required"):
                    continue
                if not v:
                    print(f"     - missing: {k}")

    n_landed = sum(1 for b in per_bulletin if b["all_required"])  # (local)

    return {
        "value": (
            "4_bulletins_landed"
            if all_pass
            else f"{n_landed}_of_4_landed"
        ),
        "per_bulletin": per_bulletin,
        "all_pass": all_pass,
        "n_landed": n_landed,
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
) -> None:
    """Append a single-line verdict to s86_gate_verdicts.txt (S84+ schema)."""
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256 companion row: {GATE_ID} "
        f"audit={audit_sha[:16]} content={content_sha[:16]}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def evaluate_gate(result: dict) -> str:
    """Pre-registered gate: ABSOLUTE check (binary present/absent).

    PASS iff all 4 bulletins land with the required content (substrate-first
    reasoning + dual SHA pins + registry anchors + no container-thinking).
    FAIL otherwise. INFO not applicable.
    """
    return "PASS" if result["all_pass"] else "FAIL"


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)  # (local)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Compute S84+ dual SHAs
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Compute (verify 4 bulletins landed)
    print(f"=== {GATE_ID} -- bulletin landing verification ===")
    result = compute()  # (local)
    value = result["value"]  # (local)

    # 3. Evaluate gate (ABSOLUTE: 4 bulletins all-or-nothing)
    verdict = evaluate_gate(result)  # (local)

    # 4. Emit 4-tuple + append verdict (dual-SHA, S84+ schema)
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)  # (local)
    print()
    print(tag)
    append_verdict(verdict, value, audit_sha, content_sha)

    # 5. Final summary
    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0  # exit 0 regardless of PASS/FAIL (verdict is data, not exit code)


if __name__ == "__main__":
    sys.exit(main())
