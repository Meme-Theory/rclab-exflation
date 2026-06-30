#!/usr/bin/env python3
"""
_yaml_gate_validator.py — R3 gate-block compliance validator (S84+)

Purpose
-------
Verify that every gate block in a session plan file declares
schema_version == "R3" AND populates all 8 PRDR machinery-enumeration
checklist items with non-empty content.

The 8 required checklist keys (REQUIRED_CHECKLIST_KEYS) are:
    operator
    strict_PASS_boundary
    boundary_reachable_analytically
    reachable_rationals
    machinery_pin_map
    audit_discriminators
    substitution_chain
    input_files

`substitution_chain` is trigger-conditional (S95 reconcile with
math-scripts.md): a real chain is required for [SIGN]/[CHAIN] gates,
[VERIFY-THEOREM]/[AUDIT] are auto-exempt, and [VERIFY]/unknown gates may
state an explicit exemption ("structural — no directional claim", or YAML
`substitution_chain.required: false`). See _chain_satisfied().

Two input formats are supported per §W9a-100 of the S84 W9a plan:

  (A) Native YAML — a `schema_version: "R3"` key-value block following
      the template at .claude/templates/r3-yaml-gate-block.yaml. Parsed
      via PyYAML.

  (B) Markdown gate block — sections delimited by `## §<gate-slug>`
      with sub-headings `### Trigger`, `### Classification`, `### PRDR`,
      `### Substitution chain`, `### 4-tuple`, `### PASS / FAIL / INFO`,
      `### Method`, `### Effort`, etc. The 13-field plan spec maps to
      the 8-item checklist via KEY_MARKDOWN_MAP below.

The validator's own pin-map (see §W9a-100 PRDR):
    CHECKLIST_ITEM_COUNT = 8                        (PIN)
    REQUIRED_CHECKLIST_KEYS = (see list below)      (PIN)
    SCHEMA_VERSION = "R3"                           (PIN)
    TEMPLATE_PATH = ".claude/templates/r3-yaml-gate-block.yaml"  (PIN)
    VALIDATOR_PATH = "computations/_shared/_yaml_gate_validator.py" (PIN)

Usage
-----
    python _yaml_gate_validator.py <plan_file.md> [<plan_file.md> ...]
    python _yaml_gate_validator.py --gate-slug W9a-97 <plan_file.md>
    python _yaml_gate_validator.py --json <plan_file.md>

Exit codes
----------
    0 — all parsed gates are R3-compliant (PASS)
    1 — at least one gate is non-compliant (FAIL)
    2 — parse error / no gates found

No framework constants are imported (NON-PHONONIC methodology tool).
Local intermediates tagged `# (local)` per .claude/rules/math-scripts.md.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # (local) CPU thread cap

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional

# NOTE: No `from canonical_constants import *` — this is a NON-PHONONIC
# methodology tool (plan-scope static analysis). It imports zero framework
# physical constants. The pins below are template-schema parameters, not
# framework constants; they belong here, not in canonical_constants.py.

# --- Pre-registration pins (S84 W9a-100) ---
CHECKLIST_ITEM_COUNT = 8  # (local) PRDR pin: # of required checklist keys
REQUIRED_CHECKLIST_KEYS = [
    "operator",
    "strict_PASS_boundary",
    "boundary_reachable_analytically",
    "reachable_rationals",
    "machinery_pin_map",
    "audit_discriminators",
    "substitution_chain",
    "input_files",
]
SCHEMA_VERSION = "R3"
TEMPLATE_PATH = ".claude/templates/r3-yaml-gate-block.yaml"
VALIDATOR_PATH = "computations/_shared/_yaml_gate_validator.py"

assert len(REQUIRED_CHECKLIST_KEYS) == CHECKLIST_ITEM_COUNT, (
    "REQUIRED_CHECKLIST_KEYS length must equal CHECKLIST_ITEM_COUNT"
)

# --- substitution_chain trigger-conditionality (S95: reconcile with math-scripts.md) ---
# math-scripts.md §"Double-Check Logic Before Compute" requires a substitution
# chain ONLY for sign/direction/threshold claims; it is explicitly NOT required
# for definitions-only / existence / structural gates. The validator now agrees:
#   - DIRECTIONAL triggers ([SIGN], [CHAIN]) -> a REAL chain is required, and an
#     exemption phrase is rejected (a directional gate cannot dodge via "N/A").
#   - STRUCTURAL triggers ([VERIFY-THEOREM], [AUDIT]) -> auto-exempt.
#   - [VERIFY] / unknown -> require a chain UNLESS the gate states an explicit
#     exemption (markdown phrase, or YAML substitution_chain.required: false).
DIRECTIONAL_TRIGGERS = frozenset({"SIGN", "CHAIN"})
STRUCTURAL_EXEMPT_TRIGGERS = frozenset({"VERIFY-THEOREM", "AUDIT"})
# Ordered alternation: VERIFY-THEOREM before VERIFY so the longer token wins.
TRIGGER_TOKEN_RE = re.compile(r"(SIGN|CHAIN|VERIFY-THEOREM|AUDIT|VERIFY)", re.IGNORECASE)
# Explicit, documented exemption phrases a planner may write in the chain slot.
CHAIN_EXEMPTION_RE = re.compile(
    r"(?:structural\s*[—:\-]\s*no\s+directional\s+claim"
    r"|no\s+(?:sign|direction|threshold)\s+claim"
    r"|definitions?[\-\s]only"
    r"|exempt\s+per\s+math[\-\s]scripts"
    r"|N/?A\s*[—:\-]?\s*(?:structural|definitions?|existence))",
    re.IGNORECASE,
)


def _extract_trigger(text: str) -> str:
    """Return the first trigger token (uppercased) in `text`, or '' if none."""
    m = TRIGGER_TOKEN_RE.search(text or "")  # (local)
    return m.group(1).upper() if m else ""


def _chain_satisfied(trigger: str, chain_nonempty: bool,
                     chain_has_exemption: bool, yaml_required=None) -> bool:
    """Trigger-conditional substitution_chain satisfaction (S95 reconcile).

    [SIGN]/[CHAIN]      -> real chain required; an exemption phrase does NOT count.
    [VERIFY-THEOREM]/[AUDIT] -> auto-exempt (structural/existence).
    [VERIFY]/unknown    -> chain required unless an explicit exemption is stated
                           (markdown phrase, or YAML substitution_chain.required==False).
    """
    t = (trigger or "").upper()  # (local)
    if t in DIRECTIONAL_TRIGGERS:
        return chain_nonempty and not chain_has_exemption
    if t in STRUCTURAL_EXEMPT_TRIGGERS:
        return True
    if yaml_required is False:
        return True
    return chain_nonempty or chain_has_exemption

# --- S86 W0a-3: cutoff_axis YAML schema field (PRDR — schema-pin) ---
# A gate block whose machinery pin invokes a cutoff (Λ_cut, K_cut, K_R5,
# K_crit, K_FIRAS, K_floor, K_wall, cutoff_sqrt — the 8 keyword triggers)
# MUST declare cutoff_axis ∈ {spectral, coherence, both}. Absence emits
# PRE-REG-INC (PRDR Class 8 plan-property failure). The 8 triggers match
# the K-family R5 disambiguates and the Mellin-cone cutoff family.
CUTOFF_KEYWORD_TRIGGERS = (
    r"Λ_cut",  # Λ_cut (spectral cutoff on D_K eigenvalues)
    r"K_cut",
    r"K_R5",
    r"K_crit",
    r"K_FIRAS",
    r"K_floor",
    r"K_wall",
    r"cutoff_sqrt",
)
CUTOFF_KEYWORD_RE = re.compile("|".join(CUTOFF_KEYWORD_TRIGGERS))
CUTOFF_AXIS_VALID_VALUES = ("spectral", "coherence", "both")
CUTOFF_AXIS_FIELD_NAME = "cutoff_axis"
CUTOFF_AXIS_RE = re.compile(
    r"cutoff_axis\s*[:=]\s*[\"\']?(spectral|coherence|both)[\"\']?",
    re.IGNORECASE,
)

# --- Markdown-section -> checklist-key map (13-field spec to 8-item checklist) ---
# Each checklist key is satisfied if ANY of its listed markdown sections
# is present and has non-empty content (>= 10 non-whitespace chars).
KEY_MARKDOWN_MAP: Dict[str, List[str]] = {
    "operator": [
        "PASS / FAIL / INFO",
        "PASS/FAIL/INFO",
        "Pass/Fail/INFO Threshold",
        "Pass/Fail criterion",
        "4-tuple",
        "4-tuple (value, scheme, convention, L_max)",
        "Expected output 4-tuple",
    ],
    "strict_PASS_boundary": [
        "PASS / FAIL / INFO",
        "PASS/FAIL/INFO",
        "Pass/Fail/INFO Threshold",
        "Pass/Fail criterion",
    ],
    "boundary_reachable_analytically": [
        "Substitution chain",
        "Hypothesis",
        "Hypothesis being tested",
        "Meaning",
    ],
    "reachable_rationals": [
        "PRDR",
        "PRDR (Pre-Registration Dry-Run)",
        "Machinery pin",
        "Machinery pin (PRDR)",
    ],
    "machinery_pin_map": [
        "PRDR",
        "PRDR (Pre-Registration Dry-Run)",
        "Machinery pin",
        "Machinery pin (PRDR)",
    ],
    "audit_discriminators": [
        "4-tuple",
        "4-tuple (value, scheme, convention, L_max)",
        "Expected output 4-tuple",
        "Method",
        "Input SHA-256 pins",
    ],
    "substitution_chain": [
        "Substitution chain",
    ],
    "input_files": [
        "Method",
        "Effort",
        "Script prefix",
        "Input SHA-256 pins",
        "Output files",
    ],
}

# Gate header: `## §<slug>` followed by either ` — <title>`, ` - <title>`,
# or `. <title>` (w3/w1a period-style). Title is optional (some plans use
# just `## §<slug>` with bold fields below).
GATE_HEADER_RE = re.compile(
    r"^##\s+§([A-Za-z0-9\-]+)[\s\.\-—]*(.*?)\s*$",
    re.MULTILINE,
)
# Sub-sections can be rendered three ways across the S84 plan corpus:
#   (w9a) `### <Name>`                       — bare sub-heading
#   (w9b) `### N. <Name>`                    — numbered sub-heading
#   (w3)  `**<Name>**:` at line start        — bold field label
SUBHEADER_RE = re.compile(r"^###\s+(?:\d+\.\s+)?(.+?)\s*$", re.MULTILINE)
BOLD_FIELD_RE = re.compile(r"^\*\*([A-Za-z][A-Za-z0-9 ()/\-]*)\*\*:\s*(.*)$", re.MULTILINE)


# --------------------------------------------------------------------------
# Parse markdown plan files
# --------------------------------------------------------------------------

# Noise slugs that match `## §<slug>` but are not physics gates — they're
# structural sections of a plan file (summaries, decision points, pin lists).
_NON_GATE_SLUGS = {
    "summary",
    "decision",
    "prerequisites",
    "dispatch",
    "pin",
    "ledger",
    "note",
    "constants",
    "input-sha",
    "machinery-enumeration",
}


def _is_gate_slug(slug: str, title: str) -> bool:
    """Heuristic: real gate slugs have a wave+index form (W3-21, W9b-105,
    W1a-1). Filter out prose section headers whose slug is empty or a
    known non-gate keyword.
    """
    if not slug:
        return False
    s_lower = slug.lower()  # (local)
    for bad in _NON_GATE_SLUGS:
        if bad in s_lower:
            return False
    # Require a digit in the slug (W3-21, W9a-100) — prose headers like
    # "Decision Point Prerequisites" lack this.
    if not re.search(r"\d", slug):
        return False
    return True


def _body_has_valid_yaml_gate(body: str) -> bool:
    """True iff `body` contains a fenced ```yaml block parsing as an R3 gate
    (a dict with schema_version == SCHEMA_VERSION).

    Used to suppress the legacy markdown-parser's phantom UNIDENTIFIED gate for a
    `## §<slug>` section whose gate is authored as a YAML block (the S84+ fanout
    convention): _extract_yaml_gates is authoritative for such sections, so
    emitting a second markdown gate double-counts and yields a phantom FAIL.
    Guard semantics (no silent loss): a malformed / non-R3 YAML block returns
    False so the markdown gate is kept and still FAILs visibly; if PyYAML is
    unavailable this returns False so legacy prose-gate plans validate as before.
    """
    try:
        import yaml  # (local) optional dep; mirrors _extract_yaml_gates fallback
    except ImportError:
        return False
    for m in re.finditer(r"```yaml\s*\n(.*?)\n```", body, re.DOTALL):
        try:
            data = yaml.safe_load(m.group(1))  # (local)
        except yaml.YAMLError:
            continue
        if isinstance(data, dict) and data.get("schema_version") == SCHEMA_VERSION:
            return True
    return False


def _extract_gate_blocks_markdown(text: str) -> List[Dict]:
    """Split a plan markdown file into per-gate blocks."""
    gates = []  # (local)
    headers = [
        m
        for m in GATE_HEADER_RE.finditer(text)
        if _is_gate_slug(m.group(1), m.group(2))
    ]  # (local)
    for i, m in enumerate(headers):
        slug = m.group(1)  # (local) e.g. "W9a-100"
        title = m.group(2).strip()  # (local) e.g. "S84-W1-CF-PRDR-TEMPLATE"
        start = m.end()  # (local)
        end = headers[i + 1].start() if i + 1 < len(headers) else len(text)  # (local)
        body = text[start:end]  # (local)
        # A `## §<slug>` section whose gate is authored as a fenced ```yaml R3
        # block is handled authoritatively by _extract_yaml_gates below; skip it
        # here so it is not double-counted as a phantom UNIDENTIFIED markdown gate.
        if _body_has_valid_yaml_gate(body):
            continue
        # Gate ID can appear as `### Gate ID` (w9a), `### 1. Gate ID` (w9b),
        # or `**Gate ID**:` (w3).
        gate_id = None  # (local)
        m_hdr = re.search(r"###\s+(?:\d+\.\s+)?Gate ID\s*\n+\s*`?([A-Z0-9_\-/ ]+?)`?\s*(?:\n|$)", body)  # (local)
        if m_hdr:
            gate_id = m_hdr.group(1).strip().split("/")[0].strip()
        else:
            m_bold = re.search(r"\*\*Gate ID\*\*:\s*`?([A-Z0-9_\-/ ]+?)`?(?:\s*\(.*?\))?\s*(?:/|\n|$)", body)  # (local)
            if m_bold:
                gate_id = m_bold.group(1).strip().split("/")[0].strip()
        if not gate_id:
            gate_id = f"UNIDENTIFIED-{slug}"
        subsections = _split_subsections(body)  # (local)
        gates.append(
            {
                "slug": slug,
                "title": title,
                "gate_id": gate_id,
                "body": body,
                "subsections": subsections,
            }
        )
    return gates


def _split_subsections(body: str) -> Dict[str, str]:
    """Split a gate-body into {subsection_name: content}.
    Handles three sub-heading formats:
      1. `### <Name>` (w9a)
      2. `### N. <Name>` (w9b, numbered)
      3. `**<Name>**:` at line start (w3, bold field)
    Returned dict uses the normalized name WITHOUT the leading `N. `.
    """
    out: Dict[str, str] = {}  # (local)
    # Format 1 + 2: `### <Name>` sub-headings (with optional "N. " prefix)
    subs = list(SUBHEADER_RE.finditer(body))  # (local)
    for i, m in enumerate(subs):
        name = m.group(1).strip()  # (local)
        start = m.end()  # (local)
        end = subs[i + 1].start() if i + 1 < len(subs) else len(body)  # (local)
        content = body[start:end].strip()  # (local)
        if name not in out or len(content) > len(out.get(name, "")):
            out[name] = content
    # Format 3: `**<Name>**:` bold fields (w3 style). Content is from ':'
    # to the next blank line OR the next bold field.
    bold_matches = list(BOLD_FIELD_RE.finditer(body))  # (local)
    for j, m in enumerate(bold_matches):
        name = m.group(1).strip()  # (local)
        first_line = m.group(2).strip()  # (local)
        start = m.end()  # (local)
        end = bold_matches[j + 1].start() if j + 1 < len(bold_matches) else len(body)  # (local)
        tail = body[start:end].strip()  # (local)
        content = (first_line + "\n" + tail).strip() if first_line else tail  # (local)
        if name not in out or len(content) > len(out.get(name, "")):
            out[name] = content
    return out


def _nonempty(content: str, min_chars: int = 10) -> bool:
    """Non-empty iff it contains >= min_chars of non-whitespace text."""
    stripped = re.sub(r"\s+", "", content or "")  # (local)
    return len(stripped) >= min_chars


# --------------------------------------------------------------------------
# Parse YAML gate blocks (if any)
# --------------------------------------------------------------------------

def _extract_yaml_gates(text: str) -> List[Dict]:
    """Find ```yaml fenced blocks that look like R3 gates."""
    try:
        import yaml  # (local) optional dep; fall back to zero YAML gates if absent
    except ImportError:
        return []
    out = []  # (local)
    fence_re = re.compile(r"```yaml\s*\n(.*?)\n```", re.DOTALL)  # (local)
    for m in fence_re.finditer(text):
        try:
            data = yaml.safe_load(m.group(1))  # (local)
        except yaml.YAMLError:
            continue
        if isinstance(data, dict) and data.get("schema_version") == SCHEMA_VERSION:
            out.append(data)
    return out


# --------------------------------------------------------------------------
# Compliance check
# --------------------------------------------------------------------------

def _check_gate_markdown(gate: Dict) -> Tuple[bool, List[str], Dict[str, bool]]:
    """Return (is_r3, missing_keys, per_key_status)."""
    subs = gate["subsections"]  # (local)
    trigger = _extract_trigger(gate.get("body", ""))  # (local)
    per_key: Dict[str, bool] = {}  # (local)
    for key in REQUIRED_CHECKLIST_KEYS:
        md_names = KEY_MARKDOWN_MAP[key]  # (local)
        content = ""  # (local) longest matching subsection content
        for name in md_names:
            for sub_name, sub_content in subs.items():
                if sub_name.startswith(name) and len(sub_content) > len(content):
                    content = sub_content
        if key == "substitution_chain":
            # S95 reconcile with math-scripts.md: required only for
            # [SIGN]/[CHAIN]; [VERIFY-THEOREM]/[AUDIT] auto-exempt;
            # [VERIFY]/unknown may state an explicit exemption phrase.
            per_key[key] = _chain_satisfied(
                trigger,
                _nonempty(content),
                bool(CHAIN_EXEMPTION_RE.search(content)),
            )
        else:
            per_key[key] = _nonempty(content)
    missing = [k for k, v in per_key.items() if not v]  # (local)
    return (len(missing) == 0), missing, per_key


def check_cutoff_axis(gate_body: str) -> Tuple[str, Optional[str]]:
    """S86 W0a-3 cutoff_axis check.

    Returns (status, axis_value) where status ∈ {"NOT-APPLICABLE",
    "PASS", "PRE-REG-INC", "INVALID-VALUE"}:
      - NOT-APPLICABLE: gate body contains none of the 8 cutoff keyword
        triggers; cutoff_axis is not required.
      - PASS: gate invokes a cutoff AND declares cutoff_axis with a
        valid value ∈ {spectral, coherence, both}.
      - PRE-REG-INC: gate invokes a cutoff but cutoff_axis field is
        absent (PRDR Class 8 plan-property failure per
        .claude/rules/epistemic-discipline.md §Pre-Registration
        Completeness — analogous to Class 8 PRU but specific to
        spectral/coherence axis ambiguity).
      - INVALID-VALUE: cutoff_axis present but value not in the enum.
    """
    has_cutoff_kw = bool(CUTOFF_KEYWORD_RE.search(gate_body))  # (local)
    if not has_cutoff_kw:
        return ("NOT-APPLICABLE", None)
    m = CUTOFF_AXIS_RE.search(gate_body)  # (local)
    if not m:
        return ("PRE-REG-INC", None)
    axis_val = m.group(1).lower()  # (local)
    if axis_val not in CUTOFF_AXIS_VALID_VALUES:
        return ("INVALID-VALUE", axis_val)
    return ("PASS", axis_val)


def _check_gate_yaml(gate: Dict) -> Tuple[bool, List[str], Dict[str, bool]]:
    """Check a native-YAML gate block against REQUIRED_CHECKLIST_KEYS."""
    trigger = _extract_trigger(str(gate.get("trigger", "")))  # (local)
    per_key: Dict[str, bool] = {}  # (local)
    for key in REQUIRED_CHECKLIST_KEYS:
        val = gate.get(key)  # (local)
        if key == "substitution_chain":
            # S95 reconcile with math-scripts.md (trigger-conditional).
            sc = val if isinstance(val, dict) else {}  # (local)
            content = sc.get("content")  # (local)
            content_str = content if isinstance(content, str) else ""  # (local)
            yaml_required = sc.get("required")  # (local) None unless declared
            per_key[key] = _chain_satisfied(
                trigger,
                _nonempty(content_str),
                bool(CHAIN_EXEMPTION_RE.search(content_str)),
                yaml_required=yaml_required,
            )
            continue
        satisfied = (
            val is not None
            and (
                (isinstance(val, dict) and any(val.values()))
                or (isinstance(val, str) and _nonempty(val))
                or (isinstance(val, list) and len(val) > 0)
                or (isinstance(val, bool))
            )
        )
        per_key[key] = bool(satisfied)
    missing = [k for k, v in per_key.items() if not v]  # (local)
    return (len(missing) == 0), missing, per_key


# --------------------------------------------------------------------------
# Closure-hash (audit + content SHA per gate-verdicts discipline)
# --------------------------------------------------------------------------

def compute_closure_sha(pin_map: Dict) -> str:
    """Canonical SHA-256 over the sorted-key pin map."""
    canonical = json.dumps(pin_map, sort_keys=True, separators=(",", ":"))  # (local)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


# --------------------------------------------------------------------------
# Main per-file driver
# --------------------------------------------------------------------------

def validate_plan_file(path: Path) -> Dict:
    """Validate every gate in a plan markdown file. Returns report dict."""
    text = path.read_text(encoding="utf-8")  # (local)
    md_gates = _extract_gate_blocks_markdown(text)  # (local)
    yaml_gates = _extract_yaml_gates(text)  # (local)

    report = {
        "file": str(path).replace("\\", "/"),
        "n_markdown_gates": len(md_gates),
        "n_yaml_gates": len(yaml_gates),
        "gates": [],
        "n_pass": 0,
        "n_fail": 0,
    }

    # S86 W0a-3 cutoff_axis enforcement counters (per-file aggregate)
    report["cutoff_axis_pass"] = 0
    report["cutoff_axis_pre_reg_inc"] = 0
    report["cutoff_axis_invalid_value"] = 0
    report["cutoff_axis_not_applicable"] = 0

    for g in md_gates:
        is_r3, missing, per_key = _check_gate_markdown(g)  # (local)
        ca_status, ca_value = check_cutoff_axis(g["body"])  # (local)
        report["gates"].append(
            {
                "gate_id": g["gate_id"],
                "slug": g["slug"],
                "source_format": "markdown",
                "r3_compliant": is_r3,
                "missing_keys": missing,
                "per_key_status": per_key,
                "cutoff_axis_status": ca_status,
                "cutoff_axis_value": ca_value,
            }
        )
        if ca_status == "PASS":
            report["cutoff_axis_pass"] += 1
        elif ca_status == "PRE-REG-INC":
            report["cutoff_axis_pre_reg_inc"] += 1
        elif ca_status == "INVALID-VALUE":
            report["cutoff_axis_invalid_value"] += 1
        else:
            report["cutoff_axis_not_applicable"] += 1
        if is_r3:
            report["n_pass"] += 1
        else:
            report["n_fail"] += 1

    for g in yaml_gates:
        is_r3, missing, per_key = _check_gate_yaml(g)  # (local)
        # YAML gate: cutoff_axis is a top-level key (preferred form).
        ca_axis = g.get(CUTOFF_AXIS_FIELD_NAME)  # (local)
        # Detect cutoff invocation: render gate as JSON and grep for any keyword.
        gate_text = json.dumps(g)  # (local)
        has_kw = bool(CUTOFF_KEYWORD_RE.search(gate_text))  # (local)
        if not has_kw:
            ca_status = "NOT-APPLICABLE"
        elif ca_axis is None:
            ca_status = "PRE-REG-INC"
        elif ca_axis not in CUTOFF_AXIS_VALID_VALUES:
            ca_status = "INVALID-VALUE"
        else:
            ca_status = "PASS"
        report["gates"].append(
            {
                "gate_id": g.get("gate_id", "UNIDENTIFIED-YAML"),
                "slug": "yaml-fenced",
                "source_format": "yaml",
                "r3_compliant": is_r3,
                "missing_keys": missing,
                "per_key_status": per_key,
                "cutoff_axis_status": ca_status,
                "cutoff_axis_value": ca_axis if isinstance(ca_axis, str) else None,
            }
        )
        if ca_status == "PASS":
            report["cutoff_axis_pass"] += 1
        elif ca_status == "PRE-REG-INC":
            report["cutoff_axis_pre_reg_inc"] += 1
        elif ca_status == "INVALID-VALUE":
            report["cutoff_axis_invalid_value"] += 1
        else:
            report["cutoff_axis_not_applicable"] += 1
        if is_r3:
            report["n_pass"] += 1
        else:
            report["n_fail"] += 1

    return report


def _summarise_cli(report: Dict, gate_filter: Optional[str] = None) -> int:
    """Print human-readable summary, return exit code."""
    any_fail = False  # (local)
    print(f"[R3 VALIDATOR] file: {report['file']}")
    print(
        f"  gates: {len(report['gates'])} "
        f"(markdown={report['n_markdown_gates']}, yaml={report['n_yaml_gates']})"
    )
    for g in report["gates"]:
        if gate_filter and gate_filter not in g["slug"] and gate_filter not in g["gate_id"]:
            continue
        status = "PASS" if g["r3_compliant"] else "FAIL"  # (local)
        ca_tag = ""  # (local)
        ca_st = g.get("cutoff_axis_status")  # (local)
        if ca_st and ca_st != "NOT-APPLICABLE":
            ca_tag = (
                f"  cutoff_axis={ca_st}"
                + (f"={g['cutoff_axis_value']}" if g.get("cutoff_axis_value") else "")
            )
        print(
            f"    {g['gate_id']:<40s} [{g['source_format']:>8s}] {status}"
            + (f"  missing={g['missing_keys']}" if g["missing_keys"] else "")
            + ca_tag
        )
        if not g["r3_compliant"]:
            any_fail = True
    print(
        f"  PASS: {report['n_pass']} | FAIL: {report['n_fail']}"
        + f" | cutoff_axis: PASS={report.get('cutoff_axis_pass', 0)}"
        + f" PRE-REG-INC={report.get('cutoff_axis_pre_reg_inc', 0)}"
        + f" INVALID={report.get('cutoff_axis_invalid_value', 0)}"
        + f" N/A={report.get('cutoff_axis_not_applicable', 0)}"
    )
    return 1 if any_fail else 0


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="R3 gate-block compliance validator (S84+)"
    )
    parser.add_argument("files", nargs="+", help="plan .md files to validate")
    parser.add_argument("--gate-slug", help="only report gates with this slug substring")
    parser.add_argument("--json", action="store_true", help="emit JSON report")
    parser.add_argument("--out", help="write JSON report to this path")
    args = parser.parse_args(argv)

    overall_pass = 0  # (local)
    overall_fail = 0  # (local)
    reports = []  # (local)
    exit_code = 0  # (local)
    for fp in args.files:
        p = Path(fp)  # (local)
        if not p.exists():
            print(f"[R3 VALIDATOR] ERROR: file not found: {fp}", file=sys.stderr)
            exit_code = 2  # (local) exit: file-not-found
            continue
        report = validate_plan_file(p)  # (local)
        reports.append(report)
        overall_pass += report["n_pass"]
        overall_fail += report["n_fail"]
        if not args.json:
            ec = _summarise_cli(report, args.gate_slug)  # (local)
            if ec != 0:
                exit_code = 1  # (local) exit: at-least-one-FAIL

    if args.json:
        # S86 W0a-3: aggregate cutoff_axis counters across all reports
        agg_ca_pass = sum(r.get("cutoff_axis_pass", 0) for r in reports)  # (local)
        agg_ca_pri = sum(r.get("cutoff_axis_pre_reg_inc", 0) for r in reports)  # (local)
        agg_ca_inv = sum(r.get("cutoff_axis_invalid_value", 0) for r in reports)  # (local)
        agg_ca_na = sum(r.get("cutoff_axis_not_applicable", 0) for r in reports)  # (local)
        payload = {
            "schema_version": SCHEMA_VERSION,
            "checklist_item_count": CHECKLIST_ITEM_COUNT,
            "required_keys": REQUIRED_CHECKLIST_KEYS,
            "cutoff_axis_field_name": CUTOFF_AXIS_FIELD_NAME,
            "cutoff_axis_valid_values": list(CUTOFF_AXIS_VALID_VALUES),
            "cutoff_keyword_triggers": list(CUTOFF_KEYWORD_TRIGGERS),
            "reports": reports,
            "total_pass": overall_pass,
            "total_fail": overall_fail,
            "cutoff_axis_total_pass": agg_ca_pass,
            "cutoff_axis_total_pre_reg_inc": agg_ca_pri,
            "cutoff_axis_total_invalid_value": agg_ca_inv,
            "cutoff_axis_total_not_applicable": agg_ca_na,
        }
        blob = json.dumps(payload, indent=2)  # (local)
        if args.out:
            Path(args.out).write_text(blob, encoding="utf-8")
        else:
            print(blob)
        if overall_fail > 0 and exit_code == 0:
            exit_code = 1  # (local) exit: JSON-mode FAIL

    if not args.json:
        print(
            f"[R3 VALIDATOR] TOTAL: PASS={overall_pass} "
            f"FAIL={overall_fail} files={len(reports)}"
        )
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
