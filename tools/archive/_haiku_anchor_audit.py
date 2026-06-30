"""
_haiku_anchor_audit.py — Prepare per-table anchor batches for Haiku adjudication.

Pulls all anchors of one table type from tools/knowledge.db, attaches a 30-line
source context window, and emits JSON batch files (25 anchors each) to
tools/anchor_validation_batches/{table}_{NNN}.json.

The actual judgment runs via Haiku Agent dispatches (model="haiku"); each
spawned agent reads one batch file, evaluates per the rubric in
tools/_haiku_evaluator_prompt.md, and writes results to
tools/anchor_validation_results/{table}_{NNN}.json.

Per-anchor input schema (matches user's plan verbatim):
{
  "anchor_id":            "<re-joinable to DB row>",
  "anchor_type":          "<table name>",
  "name":                 "<DB name field>",
  "session":              "<session tag, if any>",
  "gate_id":              "<gate id, if any>",
  "closed_by":            "<closed-by value, if any>",
  "source_file":          "<DB source_file>",
  "source_context_30_lines": "<+/-15 lines around name match in source_file>"
}
Extra type-specific fields (statement, condition, etc.) are also attached
when present in the source row.

Usage:
    python tools/_haiku_anchor_audit.py --table closed_mechanisms
    python tools/_haiku_anchor_audit.py --table equations --sample 500
    python tools/_haiku_anchor_audit.py --list-batches closed_mechanisms
"""

import argparse
import json
import random
import sqlite3
from pathlib import Path

DB_PATH = Path("tools/knowledge.db")
ROOT = Path(".")
OUT_BATCHES = Path("tools/anchor_validation_batches")
OUT_RESULTS = Path("tools/anchor_validation_results")
BATCH_SIZE = 10
CONTEXT_WINDOW = 8  # +/- lines around match
MAX_CONTEXT_BYTES = 1500  # cap per-anchor context — must fit one-shot Haiku Read


def normalize_path(p: str | None) -> str | None:
    """Convert Windows backslashes to forward slashes."""
    if not p:
        return p
    return p.replace("\\", "/")


def get_source_context(source_file: str | None, name: str | None = None,
                       line: int | None = None, window: int = CONTEXT_WINDOW) -> str:
    """Read +/- window lines around a name match (or explicit line) in source_file.

    Returns a string with line-numbered context, or a diagnostic placeholder
    if the file is missing or the name can't be found.
    """
    if not source_file:
        return "<source_file missing>"
    p = ROOT / normalize_path(source_file)
    if not p.exists():
        return f"<source file not found: {p}>"
    try:
        text = p.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()
    except Exception as e:
        return f"<read error: {e}>"

    target = None
    if line and isinstance(line, int) and line > 0:
        target = line
    elif name:
        # Find first line containing the name as a substring.
        # Use a generous fallback: first try whole-name match, then first-30-chars.
        needle_candidates = [name]
        if len(name) > 30:
            needle_candidates.append(name[:30])
        for needle in needle_candidates:
            for i, ln in enumerate(lines):
                if needle in ln:
                    target = i + 1
                    break
            if target is not None:
                break

    if target is None:
        # Name not found — return file head as diagnostic context.
        head = "\n".join(f"{i+1:>5}: {ln}" for i, ln in enumerate(lines[:30]))
        return f"<name '{name}' not found in source>\n--- file head ---\n{head}"

    start = max(0, target - 1 - window)
    end = min(len(lines), target - 1 + window + 1)
    chunk = "\n".join(f"{i+1:>5}: {lines[i]}" for i in range(start, end))
    if len(chunk) > MAX_CONTEXT_BYTES:
        chunk = chunk[:MAX_CONTEXT_BYTES] + "\n... [truncated]"
    return chunk


def _trim(s, n=120):
    if not s:
        return s
    return s if len(s) <= n else s[:n] + "..."


def fetch_anchors(table: str):
    """Yield anchor-dicts for the given table type."""
    c = sqlite3.connect(DB_PATH)
    cur = c.cursor()

    if table == "closed_mechanisms":
        cur.execute("SELECT id, name, session, gate_id, closed_by, source_file FROM closed_mechanisms")
        for id_, name, sess, gate, cb, src in cur.fetchall():
            yield {
                "anchor_id": id_,
                "anchor_type": table,
                "name": name,
                "session": sess,
                "gate_id": gate,
                "closed_by": cb,
                "source_file": src,
            }

    elif table == "open_channels":
        cur.execute("SELECT rowid, name, detail_1, detail_2, session, source_file FROM open_channels")
        for rid, name, d1, d2, sess, src in cur.fetchall():
            yield {
                "anchor_id": f"open_{rid}",
                "anchor_type": table,
                "name": name,
                "detail_1": _trim(d1),
                "detail_2": _trim(d2),
                "session": sess,
                "source_file": src,
            }

    elif table == "theorems":
        cur.execute("SELECT id, name, status, sessions, statement, source_file FROM theorems")
        for id_, name, status, sess, stmt, src in cur.fetchall():
            yield {
                "anchor_id": id_,
                "anchor_type": table,
                "name": name,
                "status": status,
                "sessions": sess,
                "statement": _trim(stmt, 300),
                "source_file": src,
            }

    elif table == "gates":
        cur.execute("SELECT id, name, session, condition, verdict, source_file FROM gates")
        for id_, name, sess, cond, verd, src in cur.fetchall():
            yield {
                "anchor_id": f"gate_{id_[:60]}" if id_ else "gate_<null>",
                "anchor_type": table,
                "name": name,
                "session": sess,
                "condition": _trim(cond),
                "verdict": verd,
                "source_file": src,
            }

    elif table == "data_provenance":
        cur.execute("SELECT rowid, script, session, name, inputs, outputs FROM data_provenance")
        for rid, script, sess, name, ins, outs in cur.fetchall():
            yield {
                "anchor_id": f"prov_{rid}",
                "anchor_type": table,
                "name": name,
                "script_path": script,
                "session": sess,
                "inputs": _trim(ins),
                "outputs": _trim(outs),
                # For provenance, the script file itself is the artifact to inspect.
                "source_file": ("computations/" + script) if script else None,
            }

    elif table == "session_files":
        cur.execute("SELECT id, session, filename, path, size_bytes FROM session_files")
        for id_, sess, fn, path, sz in cur.fetchall():
            yield {
                "anchor_id": f"sf_{id_}" if id_ else f"sf_<{fn}>",
                "anchor_type": table,
                "name": fn,
                "path": path,
                "session": sess,
                "size_bytes": sz,
                "source_file": path,
            }

    elif table == "equations":
        cur.execute("SELECT id, type, raw, file, line, context, source_file FROM equations")
        for id_, typ, raw, fp, ln, ctx, src in cur.fetchall():
            yield {
                "anchor_id": id_,
                "anchor_type": table,
                "name": _trim(raw, 200),
                "eq_type": typ,
                "file": fp,
                "line": ln,
                "context_snippet": _trim(ctx, 300),
                "source_file": src or fp,
            }

    elif table == "researchers":
        cur.execute("SELECT domain, path, paper_count, description FROM researchers")
        for dom, path, n, desc in cur.fetchall():
            idx_file = (path.rstrip("/") + "/index.md") if path else None
            yield {
                "anchor_id": f"researcher_{dom}",
                "anchor_type": table,
                "name": dom,
                "path": path,
                "paper_count": n,
                "description": _trim(desc, 300),
                "source_file": idx_file,
            }

    elif table == "agents":
        cur.execute("SELECT slug, name, persona, source_file FROM agents")
        for slug, nm, pers, src in cur.fetchall():
            yield {
                "anchor_id": f"agent_{slug}",
                "anchor_type": table,
                "name": nm,
                "persona": _trim(pers, 300),
                "source_file": src,
            }

    elif table == "constants":
        cur.execute("SELECT name, value, session, source FROM constants")
        for nm, val, sess, src in cur.fetchall():
            yield {
                "anchor_id": f"const_{nm}",
                "anchor_type": table,
                "name": nm,
                "value": val,
                "session": sess,
                "source_citation": src,
                # Canonical home for constants:
                "source_file": "computations/_shared/canonical_constants.py",
            }

    elif table == "registries":
        cur.execute("SELECT id, registry_id, title, source_file FROM registries")
        for id_, reg_id, title, src in cur.fetchall():
            yield {
                "anchor_id": id_,
                "anchor_type": table,
                "name": title,
                "registry_id": reg_id,
                "source_file": src,
            }

    else:
        raise SystemExit(f"Unknown table: {table}")

    c.close()


def build_batches(table: str, sample_n: int | None = None, seed: int = 42):
    """Build batch JSON files for a table. Returns list of (batch_path, result_path)."""
    anchors = list(fetch_anchors(table))
    total = len(anchors)
    if sample_n is not None and sample_n < total:
        random.seed(seed)
        anchors = random.sample(anchors, sample_n)
        print(f"[{table}] Sampled {sample_n} of {total} rows (seed={seed})")
    else:
        print(f"[{table}] All {total} rows")

    # Attach source context per anchor
    print(f"[{table}] Attaching source context...")
    for i, a in enumerate(anchors):
        ln = a.get("line")
        nm = a.get("name")
        src = a.get("source_file")
        # For equations we have an explicit line number; otherwise grep by name.
        a["source_context_30_lines"] = get_source_context(src, name=nm, line=ln)
        if (i + 1) % 200 == 0:
            print(f"  ...{i+1}/{len(anchors)}")

    # Chunk
    OUT_BATCHES.mkdir(parents=True, exist_ok=True)
    OUT_RESULTS.mkdir(parents=True, exist_ok=True)

    pairs = []
    for i in range(0, len(anchors), BATCH_SIZE):
        bid = i // BATCH_SIZE + 1
        bpath = OUT_BATCHES / f"{table}_{bid:03d}.json"
        rpath = OUT_RESULTS / f"{table}_{bid:03d}.json"
        batch = {
            "table": table,
            "batch_id": bid,
            "count": len(anchors[i:i + BATCH_SIZE]),
            "anchors": anchors[i:i + BATCH_SIZE],
        }
        bpath.write_text(json.dumps(batch, indent=2, ensure_ascii=False), encoding="utf-8")
        pairs.append((bpath, rpath))

    print(f"[{table}] Wrote {len(pairs)} batch files to {OUT_BATCHES}/")
    return pairs


def list_batches(table: str):
    """List existing batch files + result-file existence for a table."""
    bs = sorted(OUT_BATCHES.glob(f"{table}_*.json"))
    print(f"[{table}] {len(bs)} batches")
    for b in bs:
        rid = b.name
        r = OUT_RESULTS / rid
        marker = "OK" if r.exists() else "PENDING"
        print(f"  {marker:8s} batch={b}  result={r}")
    pending = [b for b in bs if not (OUT_RESULTS / b.name).exists()]
    print(f"[{table}] {len(pending)} pending")
    return pending


def aggregate_results(tables: list[str] | None = None,
                      out_path: Path = Path("tools/_anchor_validation_results.json")):
    """Collect per-batch result JSONs into a single keyed dict.

    Normalizes Pass-6 schema-drift: 2 of 50 equations batches (027, 041) emitted
    "REAL" instead of "VALID" due to vocabulary collision between the rubric
    document and dispatch-prompt schema. See ANCHOR_VALIDATION_STATUS.md item 5.
    """
    agg = {}
    parse_errors = []
    drift_counts = {}        # table -> count of REAL->VALID normalizations
    verdict_counts = {}      # table -> {verdict_label: count}
    src_tables = tables or [
        "closed_mechanisms", "open_channels", "theorems", "gates",
        "data_provenance", "session_files", "equations",
        "researchers", "agents", "constants", "registries",
    ]
    for t in src_tables:
        agg[t] = {}
        drift_counts[t] = 0
        verdict_counts[t] = {}
        for r in sorted(OUT_RESULTS.glob(f"{t}_*.json")):
            try:
                payload = json.loads(r.read_text(encoding="utf-8"))
            except Exception as e:
                print(f"[agg] {r}: parse error: {e}")
                parse_errors.append({"file": str(r), "error": str(e)})
                continue
            verdicts = payload if isinstance(payload, list) else payload.get("verdicts", [])
            for v in verdicts:
                aid = v.get("anchor_id")
                if not aid:
                    continue
                verdict = v.get("verdict")
                if verdict == "REAL":
                    verdict = "VALID"
                    drift_counts[t] += 1
                verdict_counts[t][verdict] = verdict_counts[t].get(verdict, 0) + 1
                agg[t][aid] = {"verdict": verdict, "reason": v.get("reason")}
        line = f"[agg] {t}: {len(agg[t])} verdicts"
        if drift_counts[t]:
            line += f" (normalized REAL->VALID: {drift_counts[t]})"
        print(line)
    out_path.write_text(json.dumps(agg, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[agg] wrote {out_path}")

    # Write a sibling summary file for the post-validation report
    summary = {
        "tables": {
            t: {
                "total": sum(verdict_counts[t].values()),
                "by_verdict": verdict_counts[t],
                "real_to_valid_normalized": drift_counts[t],
            }
            for t in src_tables
        },
        "parse_errors": parse_errors,
    }
    summary_path = out_path.with_name(out_path.stem + "_summary.json")
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[agg] wrote {summary_path}")
    return agg


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--table", help="Table to prepare")
    ap.add_argument("--sample", type=int, default=None, help="Random sample size")
    ap.add_argument("--list-batches", help="List existing batches for a table")
    ap.add_argument("--aggregate", action="store_true", help="Aggregate all per-batch results")
    args = ap.parse_args()

    if args.list_batches:
        list_batches(args.list_batches)
    elif args.aggregate:
        aggregate_results()
    elif args.table:
        build_batches(args.table, sample_n=args.sample)
    else:
        ap.print_help()
