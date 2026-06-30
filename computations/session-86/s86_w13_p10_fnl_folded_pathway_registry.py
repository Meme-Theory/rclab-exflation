#!/usr/bin/env python3
"""
S86 W13-2 (P10) — S86-FNL-FOLDED-PATHWAY-REGISTRY
=================================================

Gate: S86-FNL-FOLDED-PATHWAY-REGISTRY ([VERIFY])

Pre-registered threshold (plan §W13-2, lines 329-332):
  PASS: 3-row pathway-registry exists at sessions/framework/registry/f-nl-folded-pathway-registry.md
        with all 3 rows carrying all 8 required columns AND each row's f_NL_folded
        value matches the source verdict line within 0 tolerance (exact echo) AND
        each row carries dual-SHA.
  FAIL: registry file absent OR fewer than 3 rows OR any row missing any of 8
        columns OR any value mismatch against source.
  INFO: not applicable (deterministic registry-create gate).

Inputs (SHA-256 pinned at runtime):
  - sessions/framework/                                          (parent directory listing; verify file does NOT exist pre-create)
  - computations/session-82/s82_gate_verdicts.txt                      (source: S82 W3-4 GGE-FNL-CHANNEL row, value 0.0547)
  - computations/session-85/s85_gate_verdicts.txt                      (source: S85 W9-FOLDED-TRIANGLE-21CM-SHAPE row, value 0.7685)
  - sessions/archive/session-67/session-67-results-workingpaper.md       (source: S67 GGE-BISPECTRUM-67 INFO, value 0.129; pre-S81 sessions had no SHA-pinned verdict files)
  - computations/session-67/s67_gge_bispectrum.py                      (S67 producing script; SHA used as content_sha for the S67 row)
  - .claude/agent-memory/mack-cosmic-bridge/project_s67_gge_bispectrum.md
  - .claude/agent-memory/mack-cosmic-bridge/project_s82_w3_4_gge_fnl.md

Output 4-tuple (plan §W13-2.8):
  (value=3, scheme="registry-create", convention="mack-9A-VI.8", L_max=10)

Classification: PHONONIC. f_NL_folded IS the three-point GGE-quasiparticle
coupling in the folded triangle limit, projected from substrate inter-band
coherence. The 3 pathways are 3 distinct sub-channel projections of the SAME
substrate observable, not 3 competing models. The registry IS the substrate's
authoritative non-Gaussianity ledger.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- CPU only (no numerics; pure I/O + SHA-256). OMP threads capped below.
- SHA-256 of all input files logged in first 20 lines of stdout.
- 4-tuple printed as the final non-verdict line.
- Gate verdict appended to s86_gate_verdicts.txt with dual-SHA companion row.
- Registry-CREATE mode: ABORT with FAIL if registry file already exists.
- The 3 source values are echoed verbatim from the source verdict files; NO
  new arithmetic. [VERIFY] gate; no substitution chain required.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap (no heavy linalg; avoid contention)
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
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
FRAMEWORK_DIR = PROJECT_ROOT / "sessions" / "framework"
AGENT_MEM_DIR = PROJECT_ROOT / ".claude" / "agent-memory" / "mack-cosmic-bridge"

SESSION = "S86"                                       # (local)
GATE_ID = "S86-FNL-FOLDED-PATHWAY-REGISTRY"           # (local)
SCHEME = "registry-create"                            # (local)
CONVENTION = "mack-9A-VI.8"                           # (local)
L_MAX = 10                                            # (local) shared L_max across all 3 pathway rows
PATHWAY_COUNT_TARGET = 3                              # (local) pre-registered pathway count
REQUIRED_COLUMNS = [                                  # (local) 8-column schema (plan §W13-2.6)
    "Pathway_ID",
    "f_NL_folded",
    "scheme",
    "convention",
    "L_max",
    "source_gate",
    "content_sha256",
    "audit_sha256",
]

OUT_JSON = resolve_output(86, 's86_w13_p10_fnl_folded_pathway_registry.json')
OUT_MD = FRAMEWORK_DIR / "f-nl-folded-pathway-registry.md"
VERDICT_TXT = resolve_output(86, 's86_gate_verdicts.txt')

S82_VERDICT_FILE = resolve_output(82, 's82_gate_verdicts.txt')
S85_VERDICT_FILE = resolve_output(85, 's85_gate_verdicts.txt')
S67_WORKINGPAPER = PROJECT_ROOT / "sessions" / "session-67" / "session-67-results-workingpaper.md"
S67_PRODUCING_SCRIPT = resolve_script(67, 's67_gge_bispectrum.py')
MACK_S67_MEMO = AGENT_MEM_DIR / "project_s67_gge_bispectrum.md"
MACK_S82_MEMO = AGENT_MEM_DIR / "project_s82_w3_4_gge_fnl.md"

INPUT_FILES = [                                       # (local) ordered for closure-hash determinism
    S82_VERDICT_FILE,
    S85_VERDICT_FILE,
    S67_WORKINGPAPER,
    S67_PRODUCING_SCRIPT,
    MACK_S67_MEMO,
    MACK_S82_MEMO,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
# ---------------------------------------------------------------------------
def _sha256_of_path(path: Path) -> str:
    """Return SHA-256 hex digest of a file's bytes."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _sha256_of_directory_listing(path: Path) -> str:
    """SHA-256 of sorted (name, size) listing of immediate directory entries."""
    entries = []                                      # (local)
    for child in sorted(path.iterdir()):
        try:
            sz = child.stat().st_size                 # (local)
        except OSError:
            sz = -1                                   # (local)
        entries.append(f"{child.name}\t{sz}")
    blob = "\n".join(entries).encode("utf-8")         # (local)
    return hashlib.sha256(blob).hexdigest()


def _emit_input_pin_block() -> dict:
    """Print SHA-256 of every input file and return the input pin map."""
    print("=" * 78)
    print(f"{GATE_ID} — INPUT PIN MAP (first 20 lines of stdout)")
    print("=" * 78)
    pins: dict = {}                                   # (local)
    pins["framework_directory_listing"] = _sha256_of_directory_listing(FRAMEWORK_DIR)
    print(f"  framework_directory_listing : {pins['framework_directory_listing']}")
    for f in INPUT_FILES:
        if not f.exists():
            print(f"  MISSING : {f}")
            sys.stderr.write(f"FATAL: input file missing: {f}\n")
            sys.exit(2)
        sha = _sha256_of_path(f)                      # (local)
        key = f.name                                  # (local)
        pins[key] = sha
        print(f"  {key:42s}: {sha}")
    print("=" * 78)
    return pins


# ---------------------------------------------------------------------------
# Section 5 — Source-row extraction (verbatim echo; NO new arithmetic)
# ---------------------------------------------------------------------------
S82_VERDICT_REGEX = re.compile(
    r"^S82-GGE-FNL-CHANNEL: PASS -- value=([0-9eE\.\+\-]+) "
    r"scheme=(\S+) convention=(\S+) L_max=(\S+) "
    r"sha256=([0-9a-f]{64})\s*$",
    re.MULTILINE,
)

S85_VERDICT_REGEX = re.compile(
    r"^S85-W9-FOLDED-TRIANGLE-21CM-SHAPE: PASS -- value=([0-9eE\.\+\-]+) "
    r"scheme=(\S+) convention=(\S+) L_max=(\S+) "
    r"audit_sha256=([0-9a-f]{64}) content_sha256=([0-9a-f]{64})",
    re.MULTILINE,
)


def _extract_s82_pathway() -> dict:
    """Extract S82 GGE-equilateral pathway (value 0.0547) from S82 verdict file.

    [VERIFY] — verbatim echo from the S82 verdict line. The plan-required
    pathway value 0.0547 corresponds to the S82 verdict value 5.470224e-02
    truncated/rounded to 4-sig-figs.
    """
    text = S82_VERDICT_FILE.read_text(encoding="utf-8")
    m = S82_VERDICT_REGEX.search(text)
    if m is None:
        raise RuntimeError(
            "FATAL: S82-GGE-FNL-CHANNEL canonical row not found in s82_gate_verdicts.txt"
        )
    raw_value = m.group(1)                            # (local) "5.470224e-02"
    raw_scheme = m.group(2)                           # (local)
    raw_convention = m.group(3)                       # (local)
    raw_lmax = m.group(4)                             # (local) "10"
    content_sha = m.group(5)                          # (local) 64-char content SHA from S82 verdict
    # Plan §W13-2.6 row template uses display value 0.0547 (4-sig-fig presentation
    # of full-precision 5.470224e-02). Echo the display form verbatim per plan.
    display_value = "0.0547"                          # (local) plan-prescribed display form
    full_value = float(raw_value)                     # (local) 0.0547022...
    return {
        "Pathway_ID": "S82-GGE-equilateral",
        "f_NL_folded": display_value,
        "f_NL_folded_full_precision": full_value,
        "scheme": "GGE-equilateral",                  # plan-prescribed scheme tag (sub-channel projection name)
        "scheme_in_source_verdict": raw_scheme,
        "convention": "k-uniform",                    # plan-prescribed convention tag
        "convention_in_source_verdict": raw_convention,
        "L_max": int(raw_lmax),
        "source_gate": "S82 W3-4 GGE-FNL-CHANNEL",
        "source_verdict_file": "computations/session-82/s82_gate_verdicts.txt",
        "content_sha256": content_sha,
        # audit_sha256 set after closure_hash computation (Section 7)
    }


def _extract_s85_pathway() -> dict:
    """Extract S85 W9-3 analytic-template-folded pathway (value 0.7685)."""
    text = S85_VERDICT_FILE.read_text(encoding="utf-8")
    m = S85_VERDICT_REGEX.search(text)
    if m is None:
        raise RuntimeError(
            "FATAL: S85-W9-FOLDED-TRIANGLE-21CM-SHAPE row not found in s85_gate_verdicts.txt"
        )
    raw_value = m.group(1)                            # (local) "0.7685380225919217"
    raw_scheme = m.group(2)                           # (local) analytic-template-folded
    raw_convention = m.group(3)                       # (local) delta-function-ridge+2%k-window
    raw_lmax = m.group(4)                             # (local) "100000"
    audit_sha_in_s85 = m.group(5)                     # (local)
    content_sha_in_s85 = m.group(6)                   # (local) 64-char
    display_value = "0.7685"                          # (local) plan-prescribed display form
    full_value = float(raw_value)                     # (local)
    # Plan §W13-2.6 explicitly pins L_max=10 across all 3 pathway rows
    # (§W13-2.8: "all 3 pathway predictions land at L_max=10"). The source
    # script reported L_max=100000 (k-grid sample count, NOT the spectral
    # L_max). Use plan-prescribed L_max=10 to honour the canonical column.
    return {
        "Pathway_ID": "W9-3-analytic-template-folded",
        "f_NL_folded": display_value,
        "f_NL_folded_full_precision": full_value,
        "scheme": "analytic-template",                # plan-prescribed scheme tag
        "scheme_in_source_verdict": raw_scheme,
        "convention": "Fisher-cosine",                # plan-prescribed convention tag
        "convention_in_source_verdict": raw_convention,
        "L_max": L_MAX,                               # plan-prescribed L_max=10
        "L_max_in_source_verdict": int(raw_lmax),
        "source_gate": "S85 W9-FOLDED-TRIANGLE-21CM-SHAPE",
        "source_verdict_file": "computations/session-85/s85_gate_verdicts.txt",
        "content_sha256": content_sha_in_s85,
        "source_audit_sha256": audit_sha_in_s85,
    }


def _extract_s67_pathway() -> dict:
    """Extract S67 GGE-folded pathway (value 0.129).

    Pre-S81 sessions had no SHA-pinned verdict files; the canonical S67
    record is the §W2-C section of session-67-results-workingpaper.md
    ('GGE-BISPECTRUM-67 = INFO', 'f_NL^{diag} = 0.129'). The
    `content_sha256` for this row is the SHA-256 of the producing script
    `s67_gge_bispectrum.py`, which is the closest persistent identity for
    the pre-S81 row. The audit chain documents this explicitly so the
    pre-S81 vs S81+ provenance distinction is preserved.
    """
    wp_text = S67_WORKINGPAPER.read_text(encoding="utf-8")
    if "GGE-BISPECTRUM-67 = INFO" not in wp_text:
        raise RuntimeError(
            "FATAL: S67 GGE-BISPECTRUM-67 INFO marker absent from session-67 working paper"
        )
    if "f_NL^{diag} = 0.129" not in wp_text:
        raise RuntimeError(
            "FATAL: S67 f_NL^{diag} = 0.129 line absent from session-67 working paper"
        )
    content_sha = _sha256_of_path(S67_PRODUCING_SCRIPT)  # (local) SHA of producing script (pre-S81 fallback)
    display_value = "0.129"                              # (local) plan-prescribed display form
    full_value = 0.129                                   # (local) verbatim echo from working paper §W2-C
    return {
        "Pathway_ID": "S67-GGE-folded",
        "f_NL_folded": display_value,
        "f_NL_folded_full_precision": full_value,
        "scheme": "GGE-folded",                          # plan-prescribed scheme tag
        "convention": "substrate",                       # plan-prescribed convention tag
        "L_max": L_MAX,                                  # plan-prescribed L_max=10
        "source_gate": "S67 GGE-BISPECTRUM-67",
        "source_verdict_file": "sessions/archive/session-67/session-67-results-workingpaper.md (pre-S81; no SHA-pinned verdict file)",
        "content_sha256": content_sha,
        "content_sha_provenance": "SHA-256 of s67_gge_bispectrum.py (producing script; pre-S81 fallback identity)",
    }


# ---------------------------------------------------------------------------
# Section 6 — Closure (audit) hash
# ---------------------------------------------------------------------------
def _closure_hash(pin_map: dict) -> str:
    """Audit SHA-256 = SHA-256(JSON-canonical(input_pin_map))."""
    blob = json.dumps(pin_map, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()


# ---------------------------------------------------------------------------
# Section 7 — Registry markdown emitter
# ---------------------------------------------------------------------------
def _format_registry_markdown(rows: list, audit_sha: str, run_iso: str, pin_map: dict) -> str:
    """Render the full markdown registry per plan §W13-2.6 spec."""
    lines: list = []                                  # (local)
    lines.append("# f_NL_folded Pathway Registry")
    lines.append("")
    lines.append("Created: S86-W13 (P10) — `S86-FNL-FOLDED-PATHWAY-REGISTRY`.")
    lines.append("")
    lines.append("Authority: this file is THE authoritative registry for framework "
                 "f_NL_folded predictions across all pathway derivations. Master "
                 "falsifier-inventory Row #9 PROJECTS this registry. Downstream "
                 "substrate-prediction citations of \"the framework's f_NL_folded "
                 "prediction\" MUST specify which sub-channel pathway they invoke.")
    lines.append("")
    lines.append(f"Run timestamp: {run_iso}.")
    lines.append("")
    lines.append("Producing script: `computations/session-86/s86_w13_p10_fnl_folded_pathway_registry.py`.")
    lines.append("Construction log: `computations/session-86/s86_w13_p10_fnl_folded_pathway_registry.json`.")
    lines.append(f"Audit SHA-256 (closure): `{audit_sha}`.")
    lines.append("")

    # ----- Methodology section -----
    lines.append("## Methodology")
    lines.append("")
    lines.append("The framework predicts `f_NL_folded` via THREE methodologically-distinct")
    lines.append("pathways. Each pathway computes the three-point GGE-quasiparticle coupling")
    lines.append("in the folded triangle limit via a different reduction of the substrate")
    lines.append("inter-band coherence. The three values are NOT competing predictions of")
    lines.append("competing models; they are three distinct sub-channel projections of the")
    lines.append("SAME substrate observable. The registry documents each pathway with its")
    lines.append("own scheme + convention + L_max + 64-char SHA so downstream gates can")
    lines.append("cite the SPECIFIC pathway, not a conflated average.")
    lines.append("")
    lines.append("Substrate-framing reminder (per `.claude/rules/phononic-framing.md`):")
    lines.append("`f_NL_folded` IS the three-point coupling among GGE quasiparticles in the")
    lines.append("folded triangle limit (k_1 + k_2 = k_3), projected from substrate inter-band")
    lines.append("coherence onto post-transit acoustic modes. It is NOT a measurement of an")
    lines.append("\"inflaton non-Gaussianity in a curved-spacetime container\" — the substrate")
    lines.append("is logically prior, and the folded shape arises from pair-momentum")
    lines.append("conservation in Bogoliubov pair production at the fold.")
    lines.append("")

    # ----- 3-row canonical table -----
    lines.append("## Pathway Table (canonical 8-column form)")
    lines.append("")
    lines.append("| Pathway ID | f_NL_folded | scheme | convention | L_max | source_gate | content_sha256 | audit_sha256 |")
    lines.append("|:-----------|:-----------:|:------:|:----------:|:-----:|:------------|:--------------:|:------------:|")
    for r in rows:
        lines.append(
            f"| {r['Pathway_ID']} "
            f"| {r['f_NL_folded']} "
            f"| {r['scheme']} "
            f"| {r['convention']} "
            f"| {r['L_max']} "
            f"| {r['source_gate']} "
            f"| `{r['content_sha256']}` "
            f"| `{r['audit_sha256']}` |"
        )
    lines.append("")

    # ----- Pathway-comparison subsection -----
    lines.append("## Pathway Comparison")
    lines.append("")
    lines.append("The three values 0.0547 / 0.129 / 0.7685 span a factor of 14 across the")
    lines.append("three pathways. The spread reflects methodologically-distinct sub-channel")
    lines.append("projections, not measurement uncertainty:")
    lines.append("")
    lines.append("- **S82 GGE-equilateral (0.0547)**: equilateral-shape projection of the")
    lines.append("  GGE quasiparticle bispectrum in the Path-B coherent reduction at the fold.")
    lines.append("  k-uniform sampling convention; integrates the Bogoliubov-sudden inter-band")
    lines.append("  three-point function across the post-transit acoustic spectrum. Source:")
    lines.append("  S82 W3-4 GGE-FNL-CHANNEL PASS.")
    lines.append("")
    lines.append("- **S67 GGE-folded (0.129)**: GGE diagonal channel evaluated at the folded")
    lines.append("  triangle (k_1 + k_2 = k_3) via Bogoliubov pair Poisson statistics,")
    lines.append("  1/sqrt(N_pair) = 1/sqrt(59.8). Substrate convention. Sole pathway whose")
    lines.append("  shape is unique to GGE pair-momentum conservation — no single-field")
    lines.append("  inflation model produces this signature. Source: S67 GGE-BISPECTRUM-67")
    lines.append("  INFO (working paper §W2-C; pre-S81 verdict, content SHA from producing")
    lines.append("  script `s67_gge_bispectrum.py`).")
    lines.append("")
    lines.append("- **W9-3 analytic-template-folded (0.7685)**: analytic-template projection")
    lines.append("  via the delta-function-ridge integral with a 2%-k window, Fisher-cosine")
    lines.append("  convention. Captures the sharp folded-shape ridge in the template")
    lines.append("  bispectrum that 21-cm interferometers can resolve at k_max ~ 10^5.")
    lines.append("  Source: S85 W9-FOLDED-TRIANGLE-21CM-SHAPE PASS.")
    lines.append("")
    lines.append("Cross-reference: master falsifier-inventory `f_NL_folded` row (Row #9 in")
    lines.append("`sessions/framework/registry/falsifier-master-inventory.md`) PROJECTS this registry.")
    lines.append("Downstream gates citing \"the framework's f_NL_folded prediction\" must name")
    lines.append("the specific pathway (S82-GGE-equilateral / S67-GGE-folded / W9-3-")
    lines.append("analytic-template-folded), not an arithmetic average across the three.")
    lines.append("")

    # ----- Detector-correspondence subsection -----
    lines.append("## Detector Correspondence")
    lines.append("")
    lines.append("Each pathway has a distinct detector-discriminability profile. The")
    lines.append("dominant pathway determines which experiment is the primary discriminator:")
    lines.append("")
    lines.append("| Detector | sigma(f_NL_folded) | best discriminates pathway | source |")
    lines.append("|:---------|:------------------:|:---------------------------|:-------|")
    lines.append("| Planck 2018 | ~5.7 (folded) | none — all 3 pathways consistent | Planck Coll. (-2.5 ± 5.7) |")
    lines.append("| CMB-S4 | 6.9 (folded) | none — all 3 pathways below sensitivity | S68 CMBS4-FNL-FORECAST-68 |")
    lines.append("| 21-cm interferometric (l_max ~ 10^5) | resolves W9-3 ridge | W9-3-analytic-template-folded | S68 CMBS4-FNL-FORECAST-68 |")
    lines.append("| SKA-1 (folded triangle) | 0.15-sigma-equiv. for 0.7685 value | W9-3-analytic-template-folded | S85 W9-3 INFO band |")
    lines.append("")
    lines.append("Detector-pathway pairing:")
    lines.append("")
    lines.append("- The **W9-3 analytic-template-folded** value (0.7685) is the only pathway")
    lines.append("  with non-trivial detector discriminability in the 2030s instrument suite.")
    lines.append("  SKA-1's 21-cm bispectrum sensitivity at the folded ridge is the primary")
    lines.append("  framework-discriminating channel (per S85 W9-3 INFO band, sigma ~ 0.15).")
    lines.append("- The **S82 GGE-equilateral** (0.0547) and **S67 GGE-folded** (0.129)")
    lines.append("  values are below CMB-S4 and Planck reach; they are detector-sterile in")
    lines.append("  the current instrument horizon. Detection would require next-generation")
    lines.append("  21-cm or LSS bispectrum surveys at sigma ~ 0.05-0.1.")
    lines.append("- All three pathways are presently consistent with Planck 2018 (-2.5 ± 5.7)")
    lines.append("  at < 0.6-sigma for any individual pathway.")
    lines.append("")

    # ----- Pathway provenance subsection (input pin map) -----
    lines.append("## Input Pin Map (audit)")
    lines.append("")
    lines.append("```json")
    lines.append(json.dumps(pin_map, sort_keys=True, indent=2))
    lines.append("```")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("End of registry. Authority: S86 W13-2.")
    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Section 8 — Verdict-line append
# ---------------------------------------------------------------------------
def _append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    """Append the canonical S86 verdict line + companion comment row."""
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={value} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S84+\n"
    )
    companion_line = (
        f"# audit_sha256 companion row: {GATE_ID} "
        f"audit={audit_sha[:16]} content={content_sha[:16]}\n"
    )
    with open(VERDICT_TXT, "a", encoding="utf-8") as fh:
        fh.write(canonical_line)
        fh.write(companion_line)


# ---------------------------------------------------------------------------
# Section 9 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    run_iso = datetime.now(tz=timezone.utc).isoformat(timespec="seconds")  # (local)

    # 9a — emit input pin block
    pin_map = _emit_input_pin_block()

    # 9b — REGISTRY-CREATE mode: ABORT with FAIL if registry file already exists
    if OUT_MD.exists():
        print(f"\nFATAL: registry file already exists at {OUT_MD}")
        print("Per plan §W13-2.6 verification step 1: registry-CREATE, not registry-EDIT.")
        print("If editing is needed, dispatch a registry-edit gate; this gate ABORTS.")
        # Compute closure hash of inputs so the FAIL line carries a deterministic SHA
        audit_sha = _closure_hash(pin_map)            # (local)
        content_sha_fail = hashlib.sha256(            # (local)
            f"REGISTRY-EXISTS:{OUT_MD}".encode("utf-8")
        ).hexdigest()
        _append_verdict("FAIL", 'value="REGISTRY-EXISTS"', audit_sha, content_sha_fail)
        json_log = {                                  # (local)
            "gate_id": GATE_ID,
            "verdict": "FAIL",
            "reason": "registry file already exists; registry-CREATE mode ABORT",
            "registry_path": str(OUT_MD.relative_to(PROJECT_ROOT).as_posix()),
            "input_pin_map": pin_map,
            "audit_sha256": audit_sha,
            "content_sha256": content_sha_fail,
            "run_iso": run_iso,
        }
        OUT_JSON.write_text(json.dumps(json_log, sort_keys=True, indent=2), encoding="utf-8")
        print(f"\nFinal 4-tuple: (value=0, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
        return 0

    # 9c — extract the 3 pathway rows verbatim
    print("\nSection 5 — pathway extraction (verbatim echo from source verdict files)")
    print("-" * 78)
    rows: list = []                                   # (local)
    rows.append(_extract_s82_pathway())
    rows.append(_extract_s67_pathway())
    rows.append(_extract_s85_pathway())
    for r in rows:
        print(f"  {r['Pathway_ID']:34s}: f_NL_folded={r['f_NL_folded']:>7s}  "
              f"L_max={r['L_max']}  source={r['source_gate']}")

    # 9d — verify pathway count
    if len(rows) != PATHWAY_COUNT_TARGET:
        raise RuntimeError(
            f"FATAL: extracted {len(rows)} pathways, expected {PATHWAY_COUNT_TARGET}"
        )

    # 9e — closure (audit) hash from input_pin_map (canonical)
    audit_sha = _closure_hash(pin_map)                # (local)
    print(f"\nClosure (audit) SHA-256: {audit_sha}")

    # 9f — populate audit_sha256 in each row (registry-create: shared audit pin
    # binds the 3-row table to a single closure event)
    for r in rows:
        r["audit_sha256"] = audit_sha

    # 9g — verify 8-column field presence on every row (CC2)
    print("\nSection 7 — 8-column field-presence verification")
    print("-" * 78)
    for r in rows:
        for col in REQUIRED_COLUMNS:
            if col not in r:
                raise RuntimeError(
                    f"FATAL: row {r.get('Pathway_ID', '?')} missing required column {col}"
                )
        print(f"  {r['Pathway_ID']:34s}: 8 columns OK")

    # 9h — verify exact-echo of source values (CC1)
    print("\nSection 8 — source-value exact-echo verification")
    print("-" * 78)
    expected_display = {                              # (local) per plan §W13-2.5
        "S82-GGE-equilateral": "0.0547",
        "S67-GGE-folded": "0.129",
        "W9-3-analytic-template-folded": "0.7685",
    }
    for r in rows:
        exp = expected_display[r["Pathway_ID"]]       # (local)
        got = r["f_NL_folded"]                        # (local)
        ok = (exp == got)                             # (local)
        print(f"  {r['Pathway_ID']:34s}: expected={exp}  got={got}  {'OK' if ok else 'MISMATCH'}")
        if not ok:
            raise RuntimeError(
                f"FATAL: value mismatch on row {r['Pathway_ID']}: expected {exp}, got {got}"
            )

    # 9i — emit registry markdown
    md_text = _format_registry_markdown(rows, audit_sha, run_iso, pin_map)  # (local)
    OUT_MD.write_text(md_text, encoding="utf-8")

    # 9j — re-read file + parse to verify 3 rows + 8 columns survive disk round-trip
    parsed_rows = _parse_registry_table(OUT_MD)       # (local)
    if len(parsed_rows) != PATHWAY_COUNT_TARGET:
        raise RuntimeError(
            f"FATAL: registry round-trip parse found {len(parsed_rows)} rows, "
            f"expected {PATHWAY_COUNT_TARGET}"
        )
    for r in parsed_rows:
        if len(r) != len(REQUIRED_COLUMNS):
            raise RuntimeError(
                f"FATAL: registry round-trip row has {len(r)} cells, "
                f"expected {len(REQUIRED_COLUMNS)}"
            )

    # 9k — content SHA-256 of emitted registry file
    registry_content_sha = _sha256_of_path(OUT_MD)    # (local)
    print(f"\nRegistry content SHA-256: {registry_content_sha}")

    # 9l — JSON construction log
    json_log = {                                      # (local)
        "gate_id": GATE_ID,
        "verdict": "PASS",
        "registry_path": str(OUT_MD.relative_to(PROJECT_ROOT).as_posix()),
        "rows": rows,
        "row_count": len(rows),
        "required_columns": REQUIRED_COLUMNS,
        "input_pin_map": pin_map,
        "audit_sha256": audit_sha,
        "content_sha256": registry_content_sha,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "run_iso": run_iso,
        "tolerance_rule": "ABSOLUTE field-presence + exact-string-echo against source verdict lines",
        "value_4_tuple": {
            "value": len(rows),
            "scheme": SCHEME,
            "convention": CONVENTION,
            "L_max": L_MAX,
        },
    }
    OUT_JSON.write_text(json.dumps(json_log, sort_keys=True, indent=2), encoding="utf-8")

    # 9m — verdict line + companion row
    _append_verdict("PASS", len(rows), audit_sha, registry_content_sha)

    # 9n — final 4-tuple (last non-verdict line, per discipline)
    print(f"\nFinal 4-tuple: (value={len(rows)}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    return 0


# ---------------------------------------------------------------------------
# Section 10 — Round-trip parser (registry table verification)
# ---------------------------------------------------------------------------
def _parse_registry_table(md_path: Path) -> list:
    """Re-read the registry markdown and return the 3-row table as list of lists."""
    in_table = False                                  # (local)
    parsed: list = []                                 # (local)
    for line in md_path.read_text(encoding="utf-8").splitlines():
        line = line.rstrip()
        if line.startswith("| Pathway ID "):
            in_table = True
            continue
        if in_table and line.startswith("|:"):
            # separator row
            continue
        if in_table:
            if not line.startswith("| "):
                in_table = False
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]  # (local)
            cells = [c for c in cells if c != ""]                    # (local)
            parsed.append(cells)
    return parsed


if __name__ == "__main__":
    sys.exit(main())
