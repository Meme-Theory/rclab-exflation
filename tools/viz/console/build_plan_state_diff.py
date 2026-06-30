#!/usr/bin/env python3
"""
Plan-vs-state graph diff generator (Δ(P, S) Lyapunov metric).

Walks every session that has both a plan corpus
(`sessions/session-plan/session-{N}-plan-*.md`) and a verdict ledger
(`computations/s{N}_gate_verdicts.txt`), extracts:

  - Plan-DAG     : declared inputs from `**Method**:` / `Inputs (pinned):` blocks
                   in plan files (per `gate-verdicts.md` §Pre-Registration Protocol)
  - Realized-DAG : declared inputs from the producing script's docstring
                   "Inputs (SHA-256 dual-pinned[ at runtime]):" block — this is
                   the human-readable mirror of the input-pin map that closes
                   into `audit_sha256` at runtime, so it serves as a static
                   proxy for the realized-side input set.

Computes per-session:
  - planned_edges  / realized_edges  (gate -> input entity)
  - deviating_edges (symmetric difference, classified PLANNED_NOT_REALIZED
                     / REALIZED_NOT_PLANNED)
  - delta_norm     (count of deviating edges = Lyapunov scalar)
  - missing_gates  (planned but no verdict line)
  - extra_gates    (verdict line but no plan section)

Output:
  tools/viz/console/plan_state_diff.json   (consumed by buildPlanStateDiff view)

Run:
  "phonon-exflation-sim/.venv312/Scripts/python.exe" tools/viz/console/build_plan_state_diff.py
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent.parent.parent.parent       # project root
PLAN_DIR = ROOT / "sessions" / "session-plan"
PLAN_ARCHIVE = PLAN_DIR / "archive"
COMPUTATIONS = ROOT / "computations"
SHARED_DIR = COMPUTATIONS / "_shared"
CC_PATH = SHARED_DIR / "canonical_constants.py"
OUT_PATH = ROOT / "tools" / "viz" / "console" / "plan_state_diff.json"


# ---------------------------------------------------------------------------
# Canonical-constants vocabulary — used to disambiguate backticked tokens
# ---------------------------------------------------------------------------

def load_canonical_names() -> set[str]:
    if not CC_PATH.exists():
        return set()
    sys.path.insert(0, str(SHARED_DIR))
    try:
        import canonical_constants as CC  # noqa: WPS433
    except Exception:                        # noqa: BLE001
        return set()
    return {n for n in dir(CC) if not n.startswith("_") and n.isidentifier()}


# ---------------------------------------------------------------------------
# Plan-side parsing
# ---------------------------------------------------------------------------

# `## §W3-1. S85-W3-CF-5-PIXIE-KMFIRAS-PREREG`   or
# `## §W1a-2. S85-W1a-ALPHA-S-REGISTRY-UPGRADE` (lowercase wave letter) or
# `## §W2.5. S84-W2-...`                          or  bare `## {GATE_ID}`
GATE_HEADING_RE = re.compile(
    r"^##\s+§?[A-Za-z0-9.\-]*\.?\s*(S\d+[-A-Za-z0-9_]+)\s*$",
    re.MULTILINE,
)
# Fallback: first S-prefixed token in any heading line.
# Allow lowercase letters because gate IDs include wave-letter suffixes
# like `S85-W1a-...` and `S85-W7b-...`.
ID_LIKE_RE = re.compile(r"\bS\d+-[A-Za-z][A-Za-z0-9_-]{2,}\b")
# Generic gate-id regex (anywhere in prose).
GENERIC_GATE_RE = re.compile(r"\bS\d+(?:-W\d+[a-z]?)?-[A-Za-z][A-Za-z0-9_-]{2,}\b")
BACKTICK_RE = re.compile(r"`([^`]+)`")
FILE_RE = re.compile(
    r"\b([A-Za-z_][\w/\-]*\.(?:py|npz|json|md|txt|csv|yaml|h5|hdf5))\b"
)
WAVE_HEADER_RE = re.compile(
    r"^##\s+§?(?P<wave>W\d+[a-z]?)[-.]?(?P<idx>\d+)?\.?\s*(?P<id>[A-Z][A-Z0-9_-]+)?\s*$",
    re.MULTILINE,
)
# Legacy gate-ID tokens used in S26-S77 plans (narrative + table format).
# Examples: UMKLAPP-1, RPA-1, WALL-1, TOPO-T2, PARAM-B2, NEW-1, NEFF-35,
# NEFF-MAP-34, T-1, V-1, B-1, K-1, M-3, KC-1, L-1, C-3, E-4, K-29a.
# Match shape: stem [A-Z][A-Z0-9]* + 1-15 hyphenated segments + optional
# trailing single lowercase letter (sub-session suffix like K-29a/29b).
# Digit requirement is enforced post-match (see DIGIT_REQUIRED below).
LEGACY_GATE_TOKEN_RE = re.compile(
    r"\b([A-Z][A-Z0-9]*(?:-[A-Z0-9]+){1,15}[a-z]?)\b"
)
# Token must contain at least one decimal digit somewhere; rejects all-letter
# tokens like CMB-PARITY, NCG-AXIOM, etc.
LEGACY_GATE_DIGIT_REQUIRED = re.compile(r"\d")
# Aggressive false-positive filter: reject tokens that are pure-noise common
# prose words that happen to match the gate-ID shape.
LEGACY_GATE_REJECT = re.compile(r"^(?:HTTPS?|HTTP|UTC|UTF|ASCII|TODO|FIXME|XXX|NB|ETC|TBD)-")


@dataclass
class GatePlan:
    gate_id: str
    plan_file: str
    section: str
    inputs: set[str] = field(default_factory=set)            # raw entity names
    classification: str = ""
    trigger: str = ""


def split_gate_sections(text: str, plan_file: str) -> list[tuple[str, str, str]]:
    """Yield (gate_id, section_header, body) chunks from a plan file.

    Recognises both `## §W3-1. {ID}` and bare `## {ID}` headings; the section
    body runs to the next `## ` heading or end of file.
    """
    headings = []
    for m in re.finditer(r"^##\s+(.+)$", text, re.MULTILINE):
        headings.append((m.start(), m.end(), m.group(1).strip()))

    sections: list[tuple[str, str, str]] = []
    for i, (s, e, hdr) in enumerate(headings):
        body_end = headings[i + 1][0] if i + 1 < len(headings) else len(text)
        body = text[e:body_end]
        # Try to extract a gate ID from the heading line. Two patterns:
        # (a) `§W3-1. S85-W3-...` -> last token is the ID
        # (b) `§W3.5.` or other prefix without an explicit ID -> skip
        m_id = ID_LIKE_RE.search(hdr)
        if not m_id:
            continue
        gate_id = m_id.group(0)
        sections.append((gate_id, hdr, body))
    return sections


def extract_planned_inputs(body: str, canonical_names: set[str]) -> set[str]:
    r"""Pull declared inputs out of a gate's section body.

    Discipline: scope file/gate extraction to the explicit `Inputs (pinned):`
    bullet (or its `Inputs (SHA-256...):` siblings); scope canonical-constants
    extraction to the `from canonical_constants import` / `pull \`X\``
    bullet. Do NOT scan output-file declarations or framing-reminder prose.
    """
    inputs: set[str] = set()

    # 1. The Inputs (pinned) / Inputs (SHA-256 ...) bullet — authoritative input list
    inputs_chunks: list[str] = []
    for m in re.finditer(
        r"(?:^|\n)\s*[-*]\s*(?:\*\*)?Inputs?\b[^:]*:\s*(.+?)(?=\n\s*[-*]\s|\n\n|\n##\s|\Z)",
        body, re.S | re.I,
    ):
        inputs_chunks.append(m.group(1))
    inputs_text = "\n".join(inputs_chunks)

    for m in GENERIC_GATE_RE.finditer(inputs_text):
        inputs.add(m.group(0))
    for m in FILE_RE.finditer(inputs_text):
        inputs.add(m.group(1))
    if inputs_text and ("canonical_constants" in inputs_text):
        inputs.add("canonical_constants.py")

    # 2. The `from canonical_constants import` / `pull \`X\`, \`Y\`` bullet —
    #    authoritative constant list. Anchored on the import line; the backtick
    #    pull list is the planned constant set.
    cc_match = re.search(
        r"(?:from\s+canonical_constants\s+import\s+\*[^\n]*\n[^\n]*?pull\s+([^\n]+)"
        r"|pull\s+([^\n]+from\s+canonical_constants[^\n]*))",
        body, re.S | re.I,
    )
    if cc_match:
        chunk = cc_match.group(1) or cc_match.group(2) or ""
        for m in BACKTICK_RE.finditer(chunk):
            tok = m.group(1).strip()
            if tok in canonical_names:
                inputs.add(tok)
        # If we found a `from canonical_constants import` declaration at all,
        # record it as an edge (the script will too — same on both sides).
        inputs.add("canonical_constants.py")
    else:
        # Fallback: any backticked canonical name in the **Method**: prose.
        method_match = re.search(
            r"\*\*Method\*\*:\s*(.+?)(?=\n\*\*[A-Z]|\n##\s|\Z)",
            body, re.S,
        )
        if method_match:
            for m in BACKTICK_RE.finditer(method_match.group(1)):
                tok = m.group(1).strip()
                if tok in canonical_names:
                    inputs.add(tok)

    return inputs


def extract_meta(body: str) -> tuple[str, str]:
    """Extract Trigger and Classification labels from a gate body."""
    trig = ""
    cls = ""
    m = re.search(r"\*\*Trigger\*\*:\s*\[?([A-Z\-]+)\]?", body)
    if m:
        trig = m.group(1).strip()
    m = re.search(r"\*\*Classification\*\*:\s*([A-Z\- ]+)", body)
    if m:
        cls = m.group(1).strip().split("|")[0].strip()
    return trig, cls


def parse_plan_corpus(session_n: int, canonical_names: set[str]) -> dict[str, GatePlan]:
    """Walk all `session-{N}-plan-*.md` files for a session (BOTH the active
    plan dir and the archive) and assemble the planned-gate map
    (gate_id -> GatePlan).

    Three extraction passes per file:
      1. Modern `## §W{w}-{n}` heading sections with `S{N}-*` gate IDs
         (S82+; full inputs/method/threshold extraction via `split_gate_sections`).
      2. Modern plans MAY ALSO mention legacy-format gate IDs in prose; those
         are picked up by the token scan below.
      3. Legacy fallback: any token matching `LEGACY_GATE_TOKEN_RE` anywhere
         in the document becomes a planned gate with empty inputs. This covers
         pre-S82 plans where gate IDs appear in tables / bullet lists / prose
         instead of structured headings.
    """
    out: dict[str, GatePlan] = {}
    plan_paths: list[Path] = []
    # Per-session plan filename variants we accept:
    #   session-{N}-plan-{suffix}.md         (S34+ modern, multi-wave per session)
    #   session-{N}-plan.md                   (S26-S58 legacy, single-file plan)
    #   session-{N}{Letter}-plan-{suffix}.md  (collab plans: session-29A-plan-..., session-31B-plan-...)
    # Files NOT recognized as plans: `*-prompt.md` (S24-S35 prompt format),
    # `*-preplan-*.md`, `*-obselete-plan.md` — these are non-canonical and
    # excluded by the hyphen-prefix anchor `-plan` in the regex.
    valid_re = re.compile(rf"^session-{session_n}[a-zA-Z]?-plan(?:[-.]|$)")
    for top in (PLAN_DIR, PLAN_ARCHIVE):
        if not top.exists():
            continue
        for p in top.glob(f"session-{session_n}*plan*.md"):
            if valid_re.match(p.name):
                plan_paths.append(p)
    for path in sorted(plan_paths):
        text = path.read_text(encoding="utf-8", errors="ignore")
        # Pass 1 — structured `## §W{w}-{n}` heading extraction (modern plans).
        for gate_id, hdr, body in split_gate_sections(text, str(path)):
            if gate_id in out:                                     # first-wins
                continue
            inputs = extract_planned_inputs(body, canonical_names)
            trig, cls = extract_meta(body)
            out[gate_id] = GatePlan(
                gate_id=gate_id,
                plan_file=path.name,
                section=hdr[:120],
                inputs=inputs,
                trigger=trig,
                classification=cls,
            )
        # Pass 2/3 — legacy-token scan (catches pre-S82 narrative-style plans
        # AND any legacy-format gate IDs mentioned in modern plans). Empty
        # inputs because narrative plans don't have machine-extractable
        # per-gate input blocks.
        #
        # CROSS-SESSION FILTER: tokens that carry an `S{N}` prefix (modern
        # gate IDs) or `T<digit>-S{N}` prefix (Tier-3 batch-canonicalized
        # references) belong to that {N}, not this session. Only accept:
        #   - tokens with NO S\d+ prefix (pure legacy: `UMKLAPP-1`,
        #     `NEFF-35`, `T-1`, `K-3`) — these can't be cross-session because
        #     legacy IDs aren't session-prefixed
        #   - tokens with explicit `S{session_n}` prefix
        cross_sess_re = re.compile(r"^(?:T\d+-)?S(\d+)\b")
        for m in LEGACY_GATE_TOKEN_RE.finditer(text):
            tok = m.group(1)
            if not LEGACY_GATE_DIGIT_REQUIRED.search(tok):
                continue                               # all-letter token, not a gate
            if LEGACY_GATE_REJECT.match(tok):
                continue
            sm = cross_sess_re.match(tok)
            if sm and int(sm.group(1)) != session_n:
                continue                               # cross-session ref, skip
            if tok in out:
                continue
            out[tok] = GatePlan(
                gate_id=tok,
                plan_file=path.name,
                section="(legacy-token-scan)",
                inputs=set(),
                trigger="",
                classification="",
            )
    return out


# ---------------------------------------------------------------------------
# Realized-side parsing (script docstrings + verdict ledger)
# ---------------------------------------------------------------------------

# Verdict-line format taxonomy (in priority order; first match wins):
#
# (A) S81+ canonical: `<S{N}-gate>: VERDICT -- ... audit_sha256=... content_sha256=...`
# (B) Generic colon (S78+ transitional + S35 legacy):
#       `<gate>: VERDICT [-- prose ...]`  where <gate> contains ≥1 digit
# (C) Inline LEADING (S28/S52/S80 batch files):
#       `<gate>   VERDICT   prose tail`     — verdict directly after 2+ spaces
# (D) Inline TRAILING (S28-style verdict at line end):
#       `<gate>   prose            VERDICT` — verdict at end of line
# (E) Pre-S52 `GATE <id>:` legacy:
#       `GATE T-1: <name> -- PENDING`

# (A) S81+ canonical
VERDICT_RE = re.compile(
    r"^(?P<gate>S\d+[-A-Z0-9_]+):\s*(?P<verdict>PASS|FAIL|INFO|PENDING-EVENT|OPEN|DIAGNOSTIC)"
    r".*?audit_sha256=(?P<audit>[0-9a-f]+).*?content_sha256=(?P<content>[0-9a-f]+)",
    re.I,
)
# (B) Generic colon: gate has ≥1 digit anywhere (filters prose like "Note: ...")
VERDICT_RE_GENERIC = re.compile(
    r"^(?P<gate>[A-Z][A-Z0-9_-]*\d[A-Z0-9_-]*):\s+"
    r"(?P<verdict>PASS|FAIL|INFO|PENDING-EVENT|OPEN|DIAGNOSTIC|PASSED|FAILED|PENDING|CLOSED|RESOLVED|NEUTRAL|MARGINAL)\b"
)
# (C) Inline LEADING (S52/S80 batch style)
VERDICT_RE_INLINE_LEADING = re.compile(
    r"^(?P<gate>[A-Z][A-Z0-9]*(?:-[A-Z0-9]+){1,7}[a-z]?)\s{2,}"
    r"(?P<verdict>PASS|FAIL|INFO|CLOSED|PASSED|FAILED|PENDING|OPEN|NEUTRAL|RESOLVED|MARGINAL)\b"
)
# (D) Inline TRAILING (S28-style)
VERDICT_RE_INLINE_TRAILING = re.compile(
    r"^(?P<gate>[A-Z][A-Z0-9]*(?:-[A-Z0-9]+){1,7}[a-z]?)\s{2,}.+?"
    r"\s+(?P<verdict>PASS|FAIL|INFO|CLOSED|PASSED|FAILED|PENDING|OPEN|NEUTRAL|RESOLVED|MARGINAL)\s*$"
)
# (E) Pre-S52 GATE-prefixed legacy
VERDICT_RE_LEGACY = re.compile(
    r"^GATE\s+(?P<gate>[A-Z][A-Z0-9_-]+):"
    r"(?:[^\n]*?--\s+(?P<verdict>PENDING|PASS|FAIL|PASSED|FAILED|CLOSED|INFO))?",
    re.I,
)
DOCSTRING_INPUTS_RE = re.compile(
    r"Inputs\s*\(SHA-256\s+dual-pinned[^\n)]*\):\s*\n((?:\s*-\s+.+?\n)+)",
    re.I,
)
DOCSTRING_GATE_RE = re.compile(
    r"Gate\s*:?\s*(S\d+[-A-Z0-9_]+)",
    re.I,
)


@dataclass
class GateRealized:
    gate_id: str
    script_path: str = ""
    inputs: set[str] = field(default_factory=set)
    verdict: str = ""
    audit_sha256: str = ""
    content_sha256: str = ""


def parse_verdict_file(path: Path) -> dict[str, GateRealized]:
    """Extract gate verdicts across three format eras:
       - S81+ canonical (dual-SHA pinned)
       - S78-S80 transitional (modern prefix, no SHAs)
       - Pre-S78 legacy (`GATE X-N:` style)
    Latest-wins on gate-ID collision."""
    out: dict[str, GateRealized] = {}
    if not path.exists():
        return out
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("="):
            continue
        # (A) S81+ canonical (richest extraction; has dual SHAs)
        m = VERDICT_RE.match(stripped)
        if m:
            gid = m.group("gate")
            out[gid] = GateRealized(
                gate_id=gid,
                verdict=m.group("verdict").upper(),
                audit_sha256=m.group("audit"),
                content_sha256=m.group("content"),
            )
            continue
        # (B) Generic colon (S35/S78/S80 modern-prefix-or-not, no SHA)
        m = VERDICT_RE_GENERIC.match(stripped)
        if m:
            gid = m.group("gate")
            rec = out.get(gid) or GateRealized(gate_id=gid)
            if not rec.verdict:
                rec.verdict = m.group("verdict").upper()
            out[gid] = rec
            continue
        # (C) Inline LEADING (S52/S80 batch verdict format)
        m = VERDICT_RE_INLINE_LEADING.match(stripped)
        if m:
            gid = m.group("gate")
            if not re.search(r"\d", gid):
                continue
            rec = out.get(gid) or GateRealized(gate_id=gid)
            if not rec.verdict:
                rec.verdict = m.group("verdict").upper()
            out[gid] = rec
            continue
        # (D) Inline TRAILING (S28-style verdict at end-of-line)
        m = VERDICT_RE_INLINE_TRAILING.match(stripped)
        if m:
            gid = m.group("gate")
            if not re.search(r"\d", gid):
                continue
            rec = out.get(gid) or GateRealized(gate_id=gid)
            if not rec.verdict:
                rec.verdict = m.group("verdict").upper()
            out[gid] = rec
            continue
        # (E) Pre-S52 `GATE <id>:` legacy
        m = VERDICT_RE_LEGACY.match(stripped)
        if m:
            gid = m.group("gate")
            rec = out.get(gid) or GateRealized(gate_id=gid)
            if not rec.verdict and m.group("verdict"):
                rec.verdict = m.group("verdict").upper()
            elif not rec.verdict:
                rec.verdict = "PENDING"   # legacy heading without explicit marker
            out[gid] = rec
    return out


def parse_script_docstring(path: Path) -> tuple[str | None, set[str]]:
    """Return (gate_id_from_header, set of declared inputs) for one script.

    Inputs (SHA-256 dual-pinned[ at runtime]):
      - canonical_constants.py
      - s84_w5_57_data.npz (...)
      - script bytes ...

    Yields the bullet-name token (first whitespace-separated word).
    Skips 'script bytes' (self-reference, not an external edge).
    """
    if not path.exists():
        return (None, set())
    head = path.read_text(encoding="utf-8", errors="ignore")[:6000]
    gate_id = None
    m = DOCSTRING_GATE_RE.search(head)
    if m:
        gate_id = m.group(1)
    inputs: set[str] = set()
    blk = DOCSTRING_INPUTS_RE.search(head)
    if blk:
        for ln in blk.group(1).splitlines():
            ln = ln.strip()
            if not ln.startswith("-"):
                continue
            content = ln.lstrip("- ").strip()
            # First whitespace-separated token is the entity name.
            name = content.split()[0] if content else ""
            # Strip trailing punctuation/parens.
            name = name.rstrip(",;:()")
            if not name or name.lower().startswith("script"):
                continue
            inputs.add(name)
    return (gate_id, inputs)


def parse_realized_corpus(session_n: int) -> dict[str, GateRealized]:
    """Combine verdict ledger with all matching scripts for a session.

    Verdict file discovery (per `.claude/rules/gate-verdicts.md`
    §"Canonical Verdict-File Path"):
      1. Canonical: `computations/session-{N}/s{N}*_gate_verdicts.txt`
         (the `*` captures batch variants like `s81_batch_gate_verdicts.txt`)
      2. Misplaced fallback: `computations/_shared/s{N}_gate_verdicts.txt`
         (forbidden-by-rule but real on disk for some sessions)

    Script discovery: both per-session (`computations/session-{N}/s{N}_*.py`)
    AND shared (`computations/_shared/s{N}_*.py`).
    """
    realized: dict[str, GateRealized] = {}

    sess_dir = COMPUTATIONS / f"session-{session_n}"
    if sess_dir.exists():
        for vp in sorted(sess_dir.glob(f"s{session_n}*_gate_verdicts.txt")):
            for gid, rec in parse_verdict_file(vp).items():
                realized[gid] = rec
    # Misplaced fallback
    legacy_verdict = SHARED_DIR / f"s{session_n}_gate_verdicts.txt"
    if legacy_verdict.exists():
        for gid, rec in parse_verdict_file(legacy_verdict).items():
            # Latest-wins: misplaced fallback only fills gaps the canonical
            # location didn't supply.
            realized.setdefault(gid, rec)

    # Scripts in the per-session subdirectory (canonical location S81+)
    if sess_dir.exists():
        for script in sorted(sess_dir.glob(f"s{session_n}_*.py")):
            gid, inputs = parse_script_docstring(script)
            if not gid:
                continue
            rec = realized.setdefault(gid, GateRealized(gate_id=gid))
            rec.script_path = script.name
            rec.inputs |= inputs
    # Scripts in _shared/ (legacy + cross-session helpers)
    if SHARED_DIR.exists():
        for script in sorted(SHARED_DIR.glob(f"s{session_n}_*.py")):
            gid, inputs = parse_script_docstring(script)
            if not gid:
                continue
            rec = realized.setdefault(gid, GateRealized(gate_id=gid))
            if not rec.script_path:                                # don't overwrite
                rec.script_path = script.name
            rec.inputs |= inputs

    return realized


# ---------------------------------------------------------------------------
# Δ(P, S) per session
# ---------------------------------------------------------------------------

@dataclass
class SessionDiff:
    session_id: str
    delta_norm: int
    gate_count_planned: int
    gate_count_realized: int
    planned_edges: list[dict]
    realized_edges: list[dict]
    deviating_edges: list[dict]
    missing_gates: list[str]                # planned but no verdict
    extra_gates: list[str]                  # verdict but no plan section


def edge(src: str, tgt: str, kind: str) -> dict:
    return {"src": src, "tgt": tgt, "kind": kind}


def normalize_input(raw: str, canonical_names: set[str]) -> tuple[str, str]:
    """(token, type) where type ∈ {gate, constant, file, ref}."""
    t = raw.strip()
    if not t:
        return ("", "")
    if t in canonical_names:
        return (t, "constant")
    if "." in t and re.search(r"\.(py|npz|json|md|txt|csv|yaml|h5|hdf5)$", t):
        return (t, "file")
    if re.match(r"^S\d+", t):
        return (t, "gate")
    return (t, "ref")


def diff_session(
    session_n: int,
    planned: dict[str, GatePlan],
    realized: dict[str, GateRealized],
    canonical_names: set[str],
) -> SessionDiff:
    p_keys = set(planned)
    r_keys = set(realized)
    common = p_keys & r_keys

    planned_edges: list[dict] = []
    realized_edges: list[dict] = []
    deviating: list[dict] = []

    for gid in sorted(p_keys | r_keys):
        p_inputs = {normalize_input(x, canonical_names) for x in
                    planned.get(gid, GatePlan(gid, "", "")).inputs}
        r_inputs = {normalize_input(x, canonical_names) for x in
                    realized.get(gid, GateRealized(gid)).inputs}
        p_inputs.discard(("", ""))
        r_inputs.discard(("", ""))

        for tok, kind in p_inputs:
            planned_edges.append(edge(gid, tok, kind))
        for tok, kind in r_inputs:
            realized_edges.append(edge(gid, tok, kind))

        # Edge-level deviation: token+kind pair is the comparison key.
        only_planned = p_inputs - r_inputs
        only_realized = r_inputs - p_inputs
        for tok, kind in only_planned:
            deviating.append({**edge(gid, tok, kind),
                              "deviation": "PLANNED_NOT_REALIZED"})
        for tok, kind in only_realized:
            deviating.append({**edge(gid, tok, kind),
                              "deviation": "REALIZED_NOT_PLANNED"})

    missing = sorted(p_keys - r_keys)
    extra = sorted(r_keys - p_keys)
    # Lyapunov scalar Δ(P, S) sums BOTH layers of deviation:
    #   - edge-level: input-token symmetric-diff per gate
    #   - gate-level: gate-IDs present on only one side
    # This is the value that drops to zero iff plan and state agree fully.
    delta_norm = len(deviating) + len(missing) + len(extra)
    return SessionDiff(
        session_id=f"S{session_n}",
        delta_norm=delta_norm,
        gate_count_planned=len(p_keys),
        gate_count_realized=len(r_keys),
        planned_edges=planned_edges,
        realized_edges=realized_edges,
        deviating_edges=deviating,
        missing_gates=missing,
        extra_gates=extra,
    )


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def discover_sessions() -> list[int]:
    """Sessions that have BOTH a plan corpus AND a verdict ledger.

    Plans: `sessions/session-plan/session-{N}-plan-*.md` AND its `archive/`.
    Verdicts: `computations/session-{N}/s{N}*_gate_verdicts.txt` (canonical)
              OR `computations/_shared/s{N}_gate_verdicts.txt` (legacy fallback).
    """
    plans: set[int] = set()
    # Accept BOTH `session-{N}-plan-{suffix}.md` (modern) and
    # `session-{N}-plan.md` (S26-S58 legacy, no suffix). Reject `preplan`
    # and `obselete-plan` via the `-plan` hyphen-prefix anchor.
    plan_re = re.compile(r"session-(\d+)[a-zA-Z]?-plan(?:[-.]|$)")
    for top in (PLAN_DIR, PLAN_ARCHIVE):
        if not top.exists():
            continue
        for p in top.glob("session-*plan*.md"):
            m = plan_re.match(p.name)
            if m:
                plans.add(int(m.group(1)))

    verdicts: set[int] = set()
    # Canonical location: computations/session-{N}/s{N}*_gate_verdicts.txt
    for d in COMPUTATIONS.glob("session-*"):
        if not d.is_dir():
            continue
        m_dir = re.match(r"session-(\d+)", d.name)
        if not m_dir:
            continue
        for v in d.glob(f"s{m_dir.group(1)}*_gate_verdicts.txt"):
            verdicts.add(int(m_dir.group(1)))
            break
    # Legacy fallback: computations/_shared/s{N}_gate_verdicts.txt
    if SHARED_DIR.exists():
        for v in SHARED_DIR.glob("s*_gate_verdicts.txt"):
            m = re.match(r"s(\d+)_gate_verdicts\.txt$", v.name)
            if m:
                verdicts.add(int(m.group(1)))

    return sorted(plans & verdicts)


def main() -> None:
    canonical_names = load_canonical_names()
    sessions = discover_sessions()
    diffs: list[SessionDiff] = []

    for n in sessions:
        planned = parse_plan_corpus(n, canonical_names)
        realized = parse_realized_corpus(n)
        if not planned and not realized:
            continue
        diffs.append(diff_session(n, planned, realized, canonical_names))

    payload = {
        "generated_from": "tools/viz/console/build_plan_state_diff.py",
        "sessions": [d.__dict__ for d in diffs],
    }
    OUT_PATH.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # Compact stdout summary for ops visibility.
    for d in diffs:
        print(
            f"S{d.session_id[1:]:>3}  "
            f"planned={d.gate_count_planned:>3}  realized={d.gate_count_realized:>3}  "
            f"Δ={d.delta_norm:>4}  missing={len(d.missing_gates):>3}  "
            f"extra={len(d.extra_gates):>3}"
        )
    print(f"\n[build_plan_state_diff] wrote {OUT_PATH} "
          f"({OUT_PATH.stat().st_size:,} bytes, {len(diffs)} sessions)")


if __name__ == "__main__":
    main()
