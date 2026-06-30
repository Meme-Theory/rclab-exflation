#!/usr/bin/env python3
"""
Harvest relation edges from re-run verdict files.

Scans every `computations/_shared/t3-intake/t3_*_verdict.txt` and the
consolidated `computations/session-81/s81_gate_verdicts.txt`, extracts explicit
and implicit cross-entity relations expressed in prose comments, and emits
`[EDGE:type] src -> tgt # comment` lines into
`computations/session-81/s81_harvested_edges.txt` (a separate file so the
extractor ingests them without contaminating the verdict log).

The harvester is deliberately conservative: it only emits an edge when a
regex pattern AND a well-defined source/target pair are both present.
Ambiguous prose is left for human follow-up.

Gate ID for this tool: S81-EDGE-HARVEST (NON-PHONONIC, infrastructure).
"""
from __future__ import annotations

from canonical_constants import *  # noqa: F401,F403

import argparse
import re
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


PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'COMPUTATIONS_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
INTAKE_DIR = resolve_script(None, 't3-intake')
MASTER_VERDICTS = resolve_output(81, 's81_gate_verdicts.txt')
OUT_FILE = resolve_output(81, 's81_harvested_edges.txt')

# S81 canonical line — identifies the "self" gate for a verdict file.
RE_S81_LINE = re.compile(
    r"^(T3-[A-Z][A-Z0-9\-]+):\s+(PASS|FAIL|INFO|PRE-REG|INCOMPUTABLE|"
    r"CANCELLED|INTERMEDIATE)",
    re.MULTILINE,
)

# --- Patterns for harvestable relations ---
#
# Each pattern is (regex, edge_type, extractor-fn) where extractor-fn
# returns (src_type, src_id, tgt_type, tgt_id, comment). The
# `self_gate` argument is the T3 gate whose verdict file the pattern
# was matched in.
#
# The patterns target the prose comment dialects used by the 37 verdict
# files already landed in S81 (by-hand audit). Regexes are written to
# be specific; prefer miss over false-positive.

# Reproduction claims: "reproduces MCP foo" / "matches MCP canonical bar"
# Stricter: require a distinctive constant-like name pattern (at least one
# digit, or a known prefix like "phi_", "m_", "M_", "alpha_", etc.), to
# avoid capturing English words like "the", "bit", "archive", "witness".
_CONSTANT_NAME_STRICT = re.compile(
    r"^(?:"
    r"[A-Z][A-Za-z0-9_]*_[A-Za-z0-9_]+"    # CamelOrConst_with_underscore
    r"|phi_\w+|m_[A-Za-z0-9]+|M_[A-Za-z0-9]+|Delta_\w+|alpha_\w+"
    r"|beta_\w+|gamma_\w+|theta_\w+|omega_\w+|Omega_\w+|tau_\w+"
    r"|H_\d+|kappa_\w+|rho_\w+|Vol_\w+|T_\w+|J_\w+|S_\w+|E_\w+"
    r"|[A-Za-z]+_[A-Za-z0-9_]+\d|[A-Za-z]+\d[A-Za-z0-9_]*"
    r")$"
)
RE_REPRODUCES_CONSTANT = re.compile(
    r"reproduc[ei]\w*\s+(?:MCP\s+)?(?:canonical\s+)?"
    r"(?:constant\s+)?`?([A-Za-z_]\w{2,40})`?",
    re.IGNORECASE,
)
RE_REPRODUCES_THEOREM = re.compile(
    r"reproduc[ei]\w*.{0,40}?proven_\d+",
    re.IGNORECASE,
)
RE_REPRODUCES_GATE = re.compile(
    r"reproduc[ei]\w*.{0,40}?([A-Z]{2,4}-\d+[a-z]?)",
)
RE_REPRODUCES_CLOSED = re.compile(
    r"reproduc[ei]\w*.{0,40}?closed_\d+",
    re.IGNORECASE,
)

# Refers-to pattern:  "matches/confirms MCP tau_fold = 0.19"
RE_MATCHES_CONSTANT = re.compile(
    r"(?:matches?|confirms?|validates?|agrees? with)\s+"
    r"(?:MCP\s+)?(?:canonical\s+)?"
    r"`?([A-Za-z_]\w{1,40})`?\s*=",
    re.IGNORECASE,
)

# Downstream consumer:  "result referenced by X / feeds into X / cited by"
RE_FEEDS_INTO = re.compile(
    r"(?:feeds?\s+into|referenced\s+by|cited\s+by|consumed\s+by|"
    r"used\s+in|input\s+to)\s+`?(s\d+[a-z]?_[A-Za-z0-9_]+\.py)`?",
    re.IGNORECASE,
)

# Contradiction / refutation:  "contradicts X" / "refutes prior claim Y"
RE_CONTRADICTS_GATE = re.compile(
    r"(?:contradicts?|refutes?|overrides?)\s+"
    r"(?:prior\s+|original\s+)?(?:claim\s+|narrative\s+)?"
    r"(?:from\s+)?`?(T3-[A-Z][A-Z0-9\-]+|[A-Z]{2,4}-\d+[a-z]?)`?",
    re.IGNORECASE,
)

# Supersession:  "supersedes the original Y" / "closes session-N-result"
RE_SUPERSEDES = re.compile(
    r"supersedes?\s+.{0,40}?"
    r"(?:session-(\d+[a-z]?)|s(\d+[a-z]?)_[A-Za-z0-9_]+)",
    re.IGNORECASE,
)

# Input data dependency (SHA pin list implies depends_on):
# Capture format examples:
#   "input      s24a_vspec.npz               2880f827..."
#   "script     s29a_derived_drive_rate.py   472d9244..."
# The filename must not start with "_" (bare "_constants.py" from partial
# capture) — require at least one alphanumeric before the first dot.
RE_INPUT_PIN = re.compile(
    r"^\s*(?:input|script|canonical|input_npz_sha|script_sha|canon_sha)"
    r"\s*[:]?\s*"
    r"(?:\w+\s+)*?"
    r"([A-Za-z][A-Za-z0-9_\-]{2,}\.(?:npz|npy|h5|py))\s*:?\s*"
    r"([0-9a-fA-F]{40,})",
    re.MULTILINE,
)

# Direct cross-reference to another T3 gate:
#   "cross-reference to T3-S37-FOO" / "cf. T3-S22B-BAR"
RE_T3_CROSSREF = re.compile(
    r"(?:cross[- ]ref\w*|cf\.|compare|see(?:\s+also)?)\s+to?\s*"
    r"(T3-[A-Z][A-Z0-9\-]+)",
    re.IGNORECASE,
)

# Confirm a permanent / structural theorem:  "reproduces PERMANENT / confirms PROVEN"
RE_PERMANENT_CONFIRM = re.compile(
    r"(?:permanent|structural)\s+(?:theorem|result|closure)\s+"
    r"(?:reproduced|confirmed)",
    re.IGNORECASE,
)

# Closure linkage: "gate X closed by / B-Nnn FIRES"
RE_GATE_FIRES = re.compile(
    r"([A-Z]{1,5}-\d+[a-z]?)\s+FIRES",
)
RE_GATE_CLOSES = re.compile(
    r"([A-Z]{1,5}-\d+[a-z]?)\s+(?:DOES[- ]NOT[- ]FIRE|CLOSED|DOES-NOT-FIRE)",
)


def _iter_verdict_files() -> list[Path]:
    out: list[Path] = []
    if INTAKE_DIR.is_dir():
        out.extend(sorted(INTAKE_DIR.glob("t3_*_verdict.txt")))
    if MASTER_VERDICTS.exists():
        out.append(MASTER_VERDICTS)
    return out


def _self_gate(path: Path, text: str) -> str | None:
    """Return the T3 gate ID the file belongs to (first S81 line)."""
    if path.name.startswith("t3_") and path.name.endswith("_verdict.txt"):
        m = RE_S81_LINE.search(text)
        if m:
            return m.group(1)
    return None


def _classify_gate(gid: str) -> tuple[str, str]:
    """Classify a gate-ID into (entity_type, id) for the edge schema."""
    gid = gid.strip()
    if gid.startswith("T3-"):
        return ("gates", gid)
    if re.match(r"^proven_\d+$", gid):
        return ("theorems", gid)
    if re.match(r"^closed_\d+$", gid):
        return ("closed_mechanisms", gid)
    return ("gates", gid)


def _dedup_emit(collected: list[dict]) -> list[dict]:
    seen = set()
    out: list[dict] = []
    for e in collected:
        key = (
            e["type"], e["src_type"], e["src_id"].lower(),
            e["tgt_type"], e["tgt_id"].lower(),
        )
        if key in seen:
            continue
        seen.add(key)
        out.append(e)
    return out


def harvest_file(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8", errors="replace")
    self_gate = _self_gate(path, text)
    edges: list[dict] = []

    # For each file, we need the self-gate as the "src" when the file
    # is a per-anchor verdict. For the master verdict log, we scan per
    # gate-ID block — treat each block's S81 line as the local self-gate.

    def emit(etype: str, src: str, tgt: tuple[str, str], comment: str):
        st, sid = _classify_gate(src)
        tt, tid = tgt
        edges.append({
            "type": etype,
            "src_type": st, "src_id": sid,
            "tgt_type": tt, "tgt_id": tid,
            "comment": comment[:200],
        })

    if self_gate is None:
        # Master verdict log — split by S81 canonical line blocks.
        blocks = RE_S81_LINE.finditer(text)
        prev = None
        block_list: list[tuple[str, str]] = []
        for m in blocks:
            if prev:
                block_list.append(
                    (prev.group(1), text[prev.start():m.start()]))
            prev = m
        if prev:
            block_list.append((prev.group(1), text[prev.start():]))
        for bgate, btext in block_list:
            edges.extend(_harvest_block(bgate, btext))
        return _dedup_emit(edges)

    # Per-anchor verdict file: the whole file is one block.
    edges.extend(_harvest_block(self_gate, text))
    return _dedup_emit(edges)


def _harvest_block(self_gate: str, text: str) -> list[dict]:
    out: list[dict] = []

    def add(etype: str, tgt_type: str, tgt_id: str, comment: str):
        if not tgt_id:
            return
        out.append({
            "type": etype,
            "src_type": "gates", "src_id": self_gate,
            "tgt_type": tgt_type, "tgt_id": tgt_id,
            "comment": comment[:200],
        })

    # --- reproduces ... proven_NNN / closed_NNN / constant / gate / session
    for m in RE_REPRODUCES_THEOREM.finditer(text):
        thm = re.search(r"proven_\d+", m.group(0))
        if thm:
            add("reproduces", "theorems", thm.group(0),
                "harvested: reproduction claim")
    for m in RE_REPRODUCES_CLOSED.finditer(text):
        cl = re.search(r"closed_\d+", m.group(0))
        if cl:
            add("reproduces", "closed_mechanisms", cl.group(0),
                "harvested: reproduction of closed mechanism")
    # "reproduces S24a R-1" / "matches S30Ab / S17c" — session-level claim.
    for m in re.finditer(
            r"reproduc\w*\s+S(\d+[a-z]?)(?:\s+([A-Z]{1,4}-\d+[a-z]?))?",
            text, re.IGNORECASE):
        session_id = m.group(1)
        sub_gate = m.group(2)
        add("reproduces", "sessions", session_id,
            f"harvested: session-level reproduction"
            + (f" (sub-gate {sub_gate})" if sub_gate else ""))
    for m in RE_REPRODUCES_CONSTANT.finditer(text):
        name = m.group(1).strip()
        # Filter noise: short all-uppercase gate IDs are handled below
        if len(name) < 3 or name.isupper() and "-" in name:
            continue
        # Reject session references (S24a, S30Ab, S35, s22a_paasch_curve)
        # captured by the loose prose regex. Session refs match ^[Ss]\d+.
        # A real constant name has internal structure we require.
        if re.match(r"^[Ss]\d+[A-Za-z]*$", name):
            continue
        # Reject filenames that slipped through (ending in _curve, _analysis,
        # _trajectory, etc. are script basenames, not constants)
        if name.endswith(("_curve", "_analysis", "_trajectory", "_workshop",
                          "_extraction", "_classify", "_action", "_results",
                          "_dispersion", "_spectrum", "_running", "_matrix",
                          "_pfaffian", "_bound", "_wz", "_defects",
                          "_comparison", "_snapshot", "_corrected", "_audit",
                          "_temperature", "_transition", "_sigma",
                          "_instanton_action", "_instanton_mc")):
            continue
        # Must look like a canonical-constant name AND match the strict
        # naming pattern — English words like "the", "archive", "witness"
        # fail the strict regex and are dropped.
        if (re.match(r"^[A-Za-z_][A-Za-z0-9_]+$", name)
                and _CONSTANT_NAME_STRICT.match(name)):
            add("reproduces", "constants", name,
                "harvested: reproduction claim")
    for m in RE_REPRODUCES_GATE.finditer(text):
        gid = m.group(1)
        if gid != self_gate and _is_gate_id(gid):
            add("reproduces", "gates", gid,
                "harvested: reproduction claim")

    # --- matches / confirms constant=value
    for m in RE_MATCHES_CONSTANT.finditer(text):
        name = m.group(1).strip()
        if (len(name) >= 3
                and re.match(r"^[A-Za-z_][A-Za-z0-9_]+$", name)
                and _CONSTANT_NAME_STRICT.match(name)):
            add("reproduces", "constants", name,
                "harvested: value-match claim")

    # --- feeds_into <script.py>
    for m in RE_FEEDS_INTO.finditer(text):
        add("feeds_into", "data_provenance", m.group(1),
            "harvested: downstream-consumer claim")

    # --- contradicts / refutes prior gate
    for m in RE_CONTRADICTS_GATE.finditer(text):
        gid = m.group(1)
        if gid != self_gate and _is_gate_id(gid):
            add("contradicts", "gates", gid,
                "harvested: contradiction claim")

    # --- supersedes (session-NN or sNN_script)
    for m in RE_SUPERSEDES.finditer(text):
        sess = m.group(1) or m.group(2)
        if sess:
            add("supersedes", "sessions", sess,
                "harvested: session supersession")

    # --- Input data SHA pins → depends_on edges
    for m in RE_INPUT_PIN.finditer(text):
        fname = m.group(1).strip()
        if fname.endswith(".py"):
            add("depends_on", "data_provenance", fname,
                "harvested: SHA-pinned input script")
        else:
            add("depends_on", "data_provenance", fname,
                "harvested: SHA-pinned input data")

    # --- Cross-reference to another T3 gate
    for m in RE_T3_CROSSREF.finditer(text):
        gid = m.group(1)
        if gid != self_gate:
            add("cross_validates", "gates", gid,
                "harvested: cross-reference")

    # --- Permanent theorem confirmation
    if RE_PERMANENT_CONFIRM.search(text):
        # Attach as a structural confirmation — we can't identify the
        # specific theorem by name here, so emit a gate->self edge of
        # type confirms with an annotation. The human-readable form
        # lives in the verdict comment.
        add("confirms", "theorems", "PERMANENT-STRUCTURAL",
            "harvested: permanent/structural confirmation")

    # --- Gate FIRES / DOES NOT FIRE — closure signal
    for m in RE_GATE_FIRES.finditer(text):
        gid = m.group(1)
        if gid != self_gate and _is_gate_id(gid):
            add("implies", "gates", f"{gid}-FIRES",
                "harvested: sub-gate FIRES signal")
    for m in RE_GATE_CLOSES.finditer(text):
        gid = m.group(1)
        if gid != self_gate and _is_gate_id(gid):
            add("implies", "gates", f"{gid}-DOES-NOT-FIRE",
                "harvested: sub-gate DOES-NOT-FIRE signal")

    return out


def _is_gate_id(s: str) -> bool:
    """Reject common false-positives that look like gate IDs but aren't."""
    if not s:
        return False
    if len(s) < 3:
        return False
    # Common prose words picked up by [A-Z]{2,4}-\d+
    BLACKLIST = {
        "UTF-8", "SHA-256", "CCM-portal", "KO-6", "KO-1",
        "P-17", "P-18", "S-1",  # (paper-number/section references)
    }
    if s in BLACKLIST:
        return False
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry", action="store_true", help="Preview edges only.")
    args = ap.parse_args()

    files = _iter_verdict_files()
    if not files:
        print("No verdict files found.")
        return 0

    all_edges: list[dict] = []
    per_file_counts: list[tuple[str, int]] = []
    for f in files:
        edges = harvest_file(f)
        all_edges.extend(edges)
        per_file_counts.append((f.name, len(edges)))

    # Global dedup
    seen = set()
    deduped: list[dict] = []
    for e in all_edges:
        key = (e["type"], e["src_type"], e["src_id"].lower(),
               e["tgt_type"], e["tgt_id"].lower())
        if key in seen:
            continue
        seen.add(key)
        deduped.append(e)

    # Type breakdown
    from collections import Counter
    type_counts = Counter(e["type"] for e in deduped)

    print(f"Scanned {len(files)} verdict file(s); "
          f"harvested {len(deduped)} unique edge(s) "
          f"(from {len(all_edges)} raw hits).")
    print("By type:")
    for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f"  {t:20s}  {c}")
    print("By file (top 20 by edge count):")
    for fname, c in sorted(per_file_counts, key=lambda x: -x[1])[:20]:
        if c > 0:
            print(f"  {c:4d}  {fname}")

    if args.dry:
        print("\n--- dry-run: first 30 edges ---")
        for e in deduped[:30]:
            print(f"[EDGE:{e['type']}] {e['src_type']}:{e['src_id']} -> "
                  f"{e['tgt_type']}:{e['tgt_id']}  # {e['comment']}")
        return 0

    lines = [
        "## S81 Harvested Edges (generated by _harvest_edges.py)\n",
        "## These edges are machine-extracted from verdict-file prose and\n",
        "## are subject to the conservative-harvest discipline: prefer miss\n",
        "## over false-positive. Re-run after each new batch of verdicts.\n",
        "\n",
    ]
    for e in deduped:
        lines.append(
            f"[EDGE:{e['type']}] {e['src_type']}:{e['src_id']} -> "
            f"{e['tgt_type']}:{e['tgt_id']}  # {e['comment']}\n"
        )
    OUT_FILE.write_text("".join(lines), encoding="utf-8")
    print(f"\nWrote {len(deduped)} edges to {OUT_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
