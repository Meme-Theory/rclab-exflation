"""Read-only scanner for prose contamination in `equations[*].raw`.

Reads `tools/knowledge-index.json`, runs a cascade of detectors against each
equation entry's `raw` field, and emits:
  - stdout: per-detector tally + up to 10 sample (eq_id, extracted_span) per detector
  - tools/_scan_equations_prose_results.json: full per-row classification

Detectors (independent — a single row may match several):
  CROSS_REF_TAG      trailing (C-48), (PB-1), (D-1)
  PAREN_PROSE        (...) with >=2 lowercase english words (not Greek/unit/func)
  PROVENANCE_REF     (canonical_constants.py:1571; PDG 2024), (file.py:N)
  BRACKET_ANNOT      [vacuum energy, zeroth SDW moment]
  TRAILING_PROSE     ... is a / are the / defines / denotes ...
  CODE_LIKE          dotted method call or for-in loop syntax outside LaTeX
  TYPE_CODE          row.type == "code"
  TYPE_COMMENT       row.type == "comment"

This script does NOT modify the index. Run, eyeball, tune detectors.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parent
INDEX_PATH = ROOT / "knowledge-index.json"
OUT_PATH = ROOT / "_scan_equations_prose_results.json"

# ---------------------------------------------------------------------------
# Safe-word allowlists (do not count as english prose words).
# Lowercase comparison except where capitalization is meaningful.
# ---------------------------------------------------------------------------

GREEK_LC = {
    "alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta",
    "theta", "iota", "kappa", "lambda", "mu", "nu", "xi", "omicron",
    "pi", "rho", "sigma", "tau", "upsilon", "phi", "chi", "psi", "omega",
    "varepsilon", "vartheta", "varphi", "varpi", "varrho", "varsigma",
}

GREEK_CAPS = {w.capitalize() for w in GREEK_LC}

MATH_FUNCS = {
    "log", "ln", "exp", "sin", "cos", "tan", "sec", "csc", "cot",
    "sinh", "cosh", "tanh", "sqrt", "abs", "det", "Tr", "tr", "Res",
    "Re", "Im", "max", "min", "sup", "inf", "lim", "arg", "mod", "gcd",
    "lcm", "dim", "rank", "ker", "deg", "diag", "exp",
}

UNITS = {
    "GeV", "MeV", "eV", "keV", "TeV", "K", "Hz", "cm", "m", "mm", "km",
    "kg", "g", "J", "fm", "pc", "kpc", "Mpc", "Gpc", "Gyr", "Myr", "yr",
    "s", "ms", "ns", "ps", "fs", "Pa", "N", "W", "V", "A", "C", "T",
    "bar",
}

# Tokens that look word-ish but are actually math constants/variables.
BARE_VARS = {
    "hbar", "kB", "kT", "rms", "RMS", "obs", "eff", "max", "min",
    "fwd", "bwd", "lo", "hi",
}

SAFE_LC = {w.lower() for w in (GREEK_LC | MATH_FUNCS | UNITS | BARE_VARS)}
SAFE_CASE = GREEK_LC | GREEK_CAPS | MATH_FUNCS | UNITS | BARE_VARS

# ---------------------------------------------------------------------------
# Masking — strip math regions so they don't false-positive english detection.
# ---------------------------------------------------------------------------


def _mask_with_underscores(s: str, pattern: str) -> str:
    """Replace every match of `pattern` in s with '_' of equal length."""
    return re.sub(pattern, lambda m: "_" * len(m.group(0)), s)


def mask_math(raw: str) -> str:
    """Mask LaTeX commands, braced groups, and sub/superscript tails."""
    s = raw
    # LaTeX commands with one braced arg: \mathrm{...}, \text{...}
    s = _mask_with_underscores(s, r"\\[a-zA-Z]+\{[^{}]*\}")
    # bare LaTeX commands: \zeta, \sum
    s = _mask_with_underscores(s, r"\\[a-zA-Z]+")
    # braced groups (single level) — common subscript/superscript args
    for _ in range(3):
        new = _mask_with_underscores(s, r"\{[^{}]*\}")
        if new == s:
            break
        s = new
    # _identifier and ^identifier subscript/superscript tails (when not braced)
    s = _mask_with_underscores(s, r"[_^][A-Za-z][A-Za-z0-9]*")
    return s


# ---------------------------------------------------------------------------
# Detectors. Each returns a list of (label, extracted_span) tuples.
# ---------------------------------------------------------------------------

_CROSS_REF_RE = re.compile(r"\(\s*[A-Z]{1,4}-?\d{1,4}\s*\)\s*$")
_PROVENANCE_RE = re.compile(
    r"\([^()]*\.(?:py|md|json|sh|txt|csv|npz|png|yaml|yml|toml|ini)[^()]*\)"
)
_PROVENANCE_NUMERIC_RE = re.compile(r"\([^()]*\b(?:PDG|Planck|DESI|BICEP)\s*\d{4}[^()]*\)")
_BRACKET_ANNOT_RE = re.compile(r"\[\s*[A-Za-z][^\[\]]{3,}[A-Za-z0-9_)]\s*\]")
_PAREN_RE = re.compile(r"\(([^()]+)\)")
_TRAILING_PROSE_RE = re.compile(
    r"\b(is|are|denotes?|refers?\s+to|gives?|defines?|holds?|reads?|"
    r"reduces?|expands?|maps?|admits?|yields?|forms?|equals?|approaches?|"
    r"becomes?|represents?|implies|follows?\s+from|describes?)\s+"
    r"(a|the|an|to|from|by|that|this|these|those)?\s*[a-z]"
)
_CODE_LIKE_RE = re.compile(
    r"(?:\.[a-z_][a-zA-Z_0-9]*\(|"          # method call .foo(
    r"\bfor\s+[A-Za-z_][\w]*\s+in\s+|"      # for x in y
    r"\bimport\s+[a-z]|"                    # import foo
    r"\b(?:def|class|return)\s)"            # python keywords; `lambda` excluded — it's Greek λ here
)


def _word_tokens_lowercase(s: str) -> list[str]:
    """Pull lowercase-only alphabetic tokens of length >= 2."""
    return re.findall(r"\b[a-z][a-z]+\b", s)


def detect_cross_ref_tag(raw: str) -> list[tuple[str, str]]:
    m = _CROSS_REF_RE.search(raw.rstrip())
    return [("CROSS_REF_TAG", m.group(0))] if m else []


def detect_provenance(raw: str) -> list[tuple[str, str]]:
    hits = []
    for r in (_PROVENANCE_RE, _PROVENANCE_NUMERIC_RE):
        for m in r.finditer(raw):
            hits.append(("PROVENANCE_REF", m.group(0)))
    return hits


def detect_bracket_annot(raw: str, masked: str) -> list[tuple[str, str]]:
    hits = []
    for m in _BRACKET_ANNOT_RE.finditer(masked):
        # Restore original span by index
        inner = raw[m.start():m.end()]
        words = _word_tokens_lowercase(inner)
        non_safe = [w for w in words if w not in SAFE_LC]
        if len(non_safe) >= 2:
            hits.append(("BRACKET_ANNOT", inner))
    return hits


def detect_paren_prose(raw: str, masked: str) -> list[tuple[str, str]]:
    hits = []
    for m in _PAREN_RE.finditer(masked):
        inner_masked = m.group(1)
        inner_raw = raw[m.start() + 1:m.end() - 1]
        # Skip cross-ref tags
        if re.fullmatch(r"\s*[A-Z]{1,4}-?\d{1,4}\s*", inner_masked):
            continue
        # Skip provenance — already covered by its own detector
        if re.search(r"\.[a-z]{2,5}\b|\bPDG\s*\d{4}", inner_raw):
            continue
        # Count non-safe english words
        words = _word_tokens_lowercase(inner_masked)
        non_safe = [w for w in words if w not in SAFE_LC]
        if len(non_safe) >= 2:
            hits.append(("PAREN_PROSE", "(" + inner_raw + ")"))
    return hits


def detect_trailing_prose(raw: str, masked: str) -> list[tuple[str, str]]:
    m = _TRAILING_PROSE_RE.search(masked)
    if not m:
        return []
    # Extract a window of original text around the match
    start = max(0, m.start() - 10)
    end = min(len(raw), m.end() + 50)
    return [("TRAILING_PROSE", raw[start:end])]


def detect_code_like(raw: str, masked: str) -> list[tuple[str, str]]:
    m = _CODE_LIKE_RE.search(masked)
    return [("CODE_LIKE", m.group(0))] if m else []


# ---------------------------------------------------------------------------
# Main scan.
# ---------------------------------------------------------------------------

def scan() -> dict:
    with INDEX_PATH.open("r", encoding="utf-8") as f:
        idx = json.load(f)

    equations = idx.get("equations", [])
    results: list[dict] = []
    detector_counts: Counter = Counter()
    detector_samples: dict[str, list[tuple[str, str]]] = defaultdict(list)
    cooccurrence: Counter = Counter()
    type_x_detector: Counter = Counter()

    for row in equations:
        if not isinstance(row, dict):
            continue
        eq_id = row.get("id", "")
        raw = row.get("raw", "") or ""
        type_ = row.get("type", "") or ""

        detections: list[tuple[str, str]] = []

        # Type-based pre-classification.
        if type_ == "code":
            detections.append(("TYPE_CODE", "<type=code>"))
        if type_ == "comment":
            detections.append(("TYPE_COMMENT", "<type=comment>"))

        if not raw.strip():
            detections.append(("EMPTY_RAW", ""))
        elif type_ in ("code", "comment"):
            # Short-circuit: code and comment rows are categorically not
            # equation-prose-contamination — they belong in their own
            # remediation pipeline. Avoid spurious PROVENANCE_REF hits
            # like ('.py') in Python list comprehensions.
            pass
        else:
            masked = mask_math(raw)
            detections.extend(detect_cross_ref_tag(raw))
            detections.extend(detect_provenance(raw))
            detections.extend(detect_bracket_annot(raw, masked))
            detections.extend(detect_paren_prose(raw, masked))
            detections.extend(detect_trailing_prose(raw, masked))
            detections.extend(detect_code_like(raw, masked))

        labels = sorted({d[0] for d in detections})

        if not labels:
            labels = ["CLEAN"]

        for lbl in labels:
            detector_counts[lbl] += 1
            type_x_detector[(type_, lbl)] += 1
            if len(detector_samples[lbl]) < 10:
                # Pick the most representative span for this label
                span = next((s for l, s in detections if l == lbl), "")
                detector_samples[lbl].append((eq_id, span, raw))

        cooccurrence[tuple(labels)] += 1

        results.append({
            "id": eq_id,
            "type": type_,
            "labels": labels,
            "detections": [{"label": l, "span": s} for l, s in detections],
            "raw": raw,
        })

    return {
        "total": len(equations),
        "detector_counts": dict(detector_counts.most_common()),
        "cooccurrence_top20": [
            {"labels": list(k), "count": v}
            for k, v in cooccurrence.most_common(20)
        ],
        "type_x_detector": {
            f"{t}__{l}": c
            for (t, l), c in sorted(type_x_detector.items(), key=lambda x: -x[1])[:50]
        },
        "samples": {
            lbl: [{"id": eqid, "span": span, "raw": raw}
                  for eqid, span, raw in detector_samples[lbl]]
            for lbl in detector_counts
        },
        "rows": results,
    }


def main() -> None:
    report = scan()
    rows = report.pop("rows")

    with OUT_PATH.open("w", encoding="utf-8") as f:
        json.dump({**report, "rows": rows}, f, ensure_ascii=False, indent=2)

    # Pretty stdout summary
    print(f"\nScanned {report['total']:,} equation entries.\n")
    print("Detector counts (one row can match multiple):")
    print(f"  {'Detector':<22} {'Count':>8}  {'%':>6}")
    print("  " + "-" * 38)
    for lbl, n in report["detector_counts"].items():
        pct = 100.0 * n / report["total"]
        print(f"  {lbl:<22} {n:>8,}  {pct:>5.1f}%")

    print("\nTop 20 co-occurrence patterns:")
    for entry in report["cooccurrence_top20"]:
        labels = " + ".join(entry["labels"])
        print(f"  {entry['count']:>6,}  [{labels}]")

    print("\nSamples per detector (up to 10):")
    for lbl, samples in report["samples"].items():
        print(f"\n[{lbl}]")
        for s in samples:
            span = s["span"]
            if len(span) > 80:
                span = span[:77] + "..."
            raw_brief = s["raw"]
            if len(raw_brief) > 100:
                raw_brief = raw_brief[:97] + "..."
            print(f"  {s['id']:<8}  span={span!r}")
            print(f"            raw={raw_brief!r}")

    print(f"\nFull per-row JSON written to: {OUT_PATH}")


if __name__ == "__main__":
    main()
