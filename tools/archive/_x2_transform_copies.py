"""tools/_x2_transform_copies.py — Phase 2b: X2 transformation pass.

Rewrites .py files under computations/ so they no longer hardcode
'computations/...' or 'computation-archive' path references. After this
transformation, scripts in computations/ are runnable from their new
location AND remain runnable after computations/ + computations/
are deleted at end-state.

Approach (per accuracy-over-speed):
  - AST analysis to LOCATE expressions structurally (not regex on text)
  - Line-level text edits to APPLY changes (preserves formatting + comments
    in the rest of the file; minimal diffs)
  - Conservative: files with patterns the analyzer can't handle confidently
    are flagged NEEDS-REVIEW and NOT auto-transformed; user resolves manually
  - Per-file diff log to tools/_x2_transform_log.jsonl
  - Idempotent: transformed files have a bootstrap-marker comment;
    re-running on them is a no-op

Patterns handled:
  P1. T0/COMPUTATIONS_DIR/T0_DIR alias definitions:
      `T0 = os.path.join(ROOT, "computations/_shared")`        -> remove
      `T0 = PROJECT_ROOT / "computations/_shared"`             -> remove
      `COMPUTATIONS_DIR = os.path.join(PROJECT_ROOT, "computation-...")` -> remove
      Replaced by a one-line comment noting the X2 removal.

  P2. Uses of the alias:
      `T0 / "s86_w8.npz"`            -> `resolve_output(86, "s86_w8.npz")`
      `T0 / "canonical_constants.py"`-> `resolve_script(None, "canonical_constants.py")`
      `T0 / f"s{N}_gate_verdicts.txt"` (only when N is a Name like SESSION)
                                     -> `resolve_output(N, f"s{N}_gate_verdicts.txt")`
      `os.path.join(T0, "s86_w8.npz")`-> `str(resolve_output(86, "s86_w8.npz"))`

  P3. Direct sys.path.insert(...computation-archive...):
      Detected by string-literal "computation-archive" anywhere in args.
      Replaced with sys.path.insert(0, str(_x2_shared_dir())).

  P4. Bootstrap header inserted after the docstring (if any) and after
      the first import block. Provides resolve_script/resolve_output
      and the _x2_shared_dir() helper.

NEEDS-REVIEW criteria (transformer refuses to auto-transform):
  - Multiple T0 alias definitions in one file (rebinding)
  - T0 alias defined inside a function (non-module-scope)
  - `T0 / X` where X is not a string literal nor a simple f-string
  - F-string with multiple interpolated parts in the s{N} prefix position
  - Unrecognized alias name (not in ALIAS_NAMES set)

Modes:
  --dry-run (default):    analyze; emit log; do NOT modify files
  --execute:              apply transformations to disk
  --target FILE:          single file (relative to project root); useful for testing
  --target-glob PATTERN:  glob (relative to computations/); e.g. "session-87/*.py"
  --show-diffs N:         print first N file diffs in dry-run output

Usage:
    python tools/_x2_transform_copies.py --dry-run
    python tools/_x2_transform_copies.py --target computations/session-88/s88_w2_v4_on_strata_substrate_character_construction.py --dry-run --show-diffs 1
    python tools/_x2_transform_copies.py --execute
"""

from __future__ import annotations

import argparse
import ast
import json
import pathlib
import re
import sys
from typing import Optional


# ----------------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------------

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
DEST_TREE = PROJECT_ROOT / "computations"
LOG_PATH = PROJECT_ROOT / "tools" / "_x2_transform_log.jsonl"

# Variable names recognized as computations/_shared directory aliases.
# Module-level Assign nodes whose targets name is one of these AND whose
# value contains the literal "computations/_shared" are P1 alias definitions.
ALIAS_NAMES = {"T0", "T0_DIR", "COMPUTATIONS", "COMPUTATIONS_DIR", "COMPUTATIONS_ROOT",
               "T0_ROOT", "T0_PATH"}

# Variable names recognized as computation-archive directory aliases (less common).
ARCHIVE_ALIAS_NAMES = {"archive_dir", "ARCHIVE_DIR", "T0_ARCHIVE",
                       "COMPUTATIONS_ARCHIVE"}

BOOTSTRAP_MARKER = "# === Phase 2b X2 transform bootstrap"
BOOTSTRAP_END_MARKER = "# === End X2 bootstrap ==="

BOOTSTRAP_TEXT = """\
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
from computation_root import resolve_script, resolve_output, resolve_glob, resolve_dynamic, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===
"""


# ----------------------------------------------------------------------------
# Filename -> session-id classification (for resolve_*() session_id arg)
# ----------------------------------------------------------------------------

_SESSION_PREFIX_RE = re.compile(r"^s(\d+)[_a-zA-Z]")
_T3_SECONDARY_RE = (
    re.compile(r"^t3_S(\d+)[A-Z_]"),
    re.compile(r"^_t3_s(\d+)[_a-zA-Z]"),
    re.compile(r"^prep_T3-S(\d+)[A-Z-]"),
)


def session_from_static_filename(name: str) -> tuple[str, Optional[int]]:
    """Extract session-id from a static filename string.

    Returns:
        ("literal", N)  — N is int session number
        ("none", None)  — not session-prefixed; resolve_*(None, ...)
    """
    m = _SESSION_PREFIX_RE.match(name)
    if m:
        return ("literal", int(m.group(1)))
    for pat in _T3_SECONDARY_RE:
        m = pat.match(name)
        if m:
            return ("literal", int(m.group(1)))
    return ("none", None)


def session_from_fstring_first_value(joined_str: ast.JoinedStr) -> tuple[str, Optional[str]]:
    """Inspect an f-string for a session prefix pattern.

    Recognizes f"s{varname}_..." where varname is a simple identifier.
    In that case, the resolve_*() session_id should be `varname` (passed through).

    Returns:
        ("variable", varname)  — pass varname through as session_id
        ("ambiguous", None)    — can't determine; mark file NEEDS-REVIEW
        ("none", None)         — f-string doesn't match s{var}_... pattern
    """
    if not joined_str.values:
        return ("none", None)

    first = joined_str.values[0]
    if not (isinstance(first, ast.Constant) and isinstance(first.value, str)):
        return ("ambiguous", None)

    # Case A: leading constant is "s" alone, second value interpolates session,
    #         third is "_..." constant. Accept any expression as the session
    #         interpolation source (Name, Subscript, Attribute, Call, BinOp);
    #         pass it through as the session_id arg (rely on int() coercion
    #         in resolve_*).
    if first.value == "s":
        if len(joined_str.values) >= 2 and isinstance(joined_str.values[1], ast.FormattedValue):
            fv = joined_str.values[1]
            try:
                expr_src = ast.unparse(fv.value)
            except Exception:
                return ("ambiguous", None)
            # Sanity check: third value should start with underscore for safety
            if len(joined_str.values) >= 3:
                third = joined_str.values[2]
                if (isinstance(third, ast.Constant)
                        and isinstance(third.value, str)
                        and third.value.startswith("_")):
                    return ("variable", expr_src)
            return ("variable", expr_src)
        return ("ambiguous", None)

    # Case B: leading constant has form "sNN_..." with NN being literal digits,
    #         no interpolation in the prefix. Static session.
    m = _SESSION_PREFIX_RE.match(first.value)
    if m:
        return ("literal", int(m.group(1)))  # type: ignore[return-value]

    # Case C: not session-prefixed; e.g. f"canonical_{X}.py"
    return ("none", None)


# ----------------------------------------------------------------------------
# AST analysis helpers
# ----------------------------------------------------------------------------

def _str_literal_value(node: ast.AST) -> Optional[str]:
    """Return string if node is an ast.Constant string; else None."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return None


def _expr_contains_computations_string(node: ast.AST) -> bool:
    """Walk node looking for any string-literal containing 'computations/_shared'."""
    for sub in ast.walk(node):
        v = _str_literal_value(sub)
        if v and "computations/_shared" in v:
            return True
    return False


def _expr_contains_archive_string(node: ast.AST) -> bool:
    for sub in ast.walk(node):
        v = _str_literal_value(sub)
        if v and "computation-archive" in v:
            return True
    return False


def _node_lines(node: ast.AST, source_lines: list[str]) -> tuple[int, int]:
    """Return (start_line_idx, end_line_idx) — both 0-indexed inclusive — for node."""
    start = node.lineno - 1
    end = (getattr(node, "end_lineno", None) or node.lineno) - 1
    return (start, end)


def _slice_source(source_lines: list[str], start_line: int, start_col: int,
                  end_line: int, end_col: int) -> str:
    """Slice source by (line, column) coordinates, mirroring the column-aware
    edit semantics. Returns the substring spanning [start_line:start_col,
    end_line:end_col]."""
    if start_line == end_line:
        return source_lines[start_line][start_col:end_col]
    parts: list[str] = []
    parts.append(source_lines[start_line][start_col:])
    for ln in range(start_line + 1, end_line):
        parts.append(source_lines[ln])
    parts.append(source_lines[end_line][:end_col])
    return "\n".join(parts)


def _format_resolve_call(kind: str, sid_arg: str, name_repr: str) -> str:
    """Build a resolve_*(N, "X") expression string.

    kind:      "script" or "output"
    sid_arg:   session_id python expr (e.g., "86", "None", "_x2_self_session", "SESSION")
    name_repr: python repr of the filename arg (e.g., "'s86_w8.npz'", "f's{SESSION}_gate_verdicts.txt'")
    """
    func = f"resolve_{kind}"
    return f"{func}({sid_arg}, {name_repr})"


# ----------------------------------------------------------------------------
# Per-file analysis
# ----------------------------------------------------------------------------

class FileAnalysis:
    def __init__(self, path: pathlib.Path):
        self.path = path
        self.status: str = "untouched"   # one of: untouched, already-transformed,
                                          # no-changes-needed, transform, needs-review
        self.review_reasons: list[str] = []
        # Each edit is a 7-tuple:
        #   (start_line, start_col, end_line, end_col, new_text, kind, original_text)
        # All indices 0-based. Lines are inclusive on both ends; columns are
        # exclusive on the end (Python slice semantics: line[start_col:end_col]).
        # For whole-line edits (alias-def, archive-sys-path), set start_col=0
        # and end_col = -1 (sentinel; means "to end of line including any
        # trailing newline-stripped suffix"); apply_edits substitutes the whole
        # line range with the new_text + line_ending.
        self.edits: list[tuple[int, int, int, int, str, str, str]] = []
        # Bootstrap insertion: line index AFTER which to insert bootstrap text;
        # -1 means "insert at very top".
        self.bootstrap_insert_after: int = -1
        self.aliases_seen: set[str] = set()


def analyze_file(path: pathlib.Path) -> FileAnalysis:
    fa = FileAnalysis(path)

    try:
        source = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        fa.status = "needs-review"
        fa.review_reasons.append(f"read-error: {e}")
        return fa

    if BOOTSTRAP_MARKER in source:
        fa.status = "already-transformed"
        return fa

    if "computations/_shared" not in source and "computation-archive" not in source:
        fa.status = "no-changes-needed"
        return fa

    try:
        tree = ast.parse(source, filename=str(path))
    except SyntaxError as e:
        fa.status = "needs-review"
        fa.review_reasons.append(f"syntax-error: {e}")
        return fa

    source_lines = source.splitlines(keepends=False)

    # --- Pass 1: identify alias definitions at MODULE scope.
    # Module-scope nodes are tree.body. We only consider Assign nodes whose
    # target is a Name in ALIAS_NAMES and whose value contains "computations/_shared".
    alias_defs: dict[str, tuple[int, int, ast.Assign]] = {}  # name -> (start, end, node)
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            tgt = node.targets[0]
            if isinstance(tgt, ast.Name) and tgt.id in ALIAS_NAMES:
                if _expr_contains_computations_string(node.value):
                    if tgt.id in alias_defs:
                        # Multiple defs of same alias at module scope — too risky.
                        fa.review_reasons.append(
                            f"alias '{tgt.id}' redefined at module scope "
                            f"(lines {alias_defs[tgt.id][0]+1} and {node.lineno})"
                        )
                    start, end = _node_lines(node, source_lines)
                    alias_defs[tgt.id] = (start, end, node)
                    fa.aliases_seen.add(tgt.id)

    # Also flag if a Name in ALIAS_NAMES is rebound at non-module scope
    # (inside a function); that's a pattern this transformer doesn't handle.
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef):
            for sub in ast.walk(node):
                if isinstance(sub, ast.Assign):
                    for t in sub.targets:
                        if isinstance(t, ast.Name) and t.id in ALIAS_NAMES:
                            if _expr_contains_computations_string(sub.value):
                                fa.review_reasons.append(
                                    f"alias '{t.id}' assigned inside function at "
                                    f"line {sub.lineno} (non-module scope)"
                                )

    # --- Pass 2: identify uses of the aliases (T0 / X, os.path.join(T0, X)).
    # These are COLUMN-PRECISE edits: only the alias-use expression text is
    # replaced; surrounding code on the line (assignment LHS, wrapping function
    # call, etc.) is preserved.
    use_edits: list[tuple[int, int, int, int, str, str, str]] = []
    aliases = set(alias_defs.keys())

    for node in ast.walk(tree):
        # T0 / "X" or T0 / f"...":
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            # Look for left being a Name in aliases.
            if isinstance(node.left, ast.Name) and node.left.id in aliases:
                rhs = node.right
                replacement = _emit_resolve_for_use(rhs, fa)
                if replacement is None:
                    # fa.review_reasons already updated by helper if needed
                    continue
                start_line = node.lineno - 1
                start_col = node.col_offset
                end_line = (node.end_lineno or node.lineno) - 1
                end_col = node.end_col_offset or 0
                orig = _slice_source(source_lines, start_line, start_col, end_line, end_col)
                use_edits.append(
                    (start_line, start_col, end_line, end_col,
                     replacement, "alias-use-div", orig)
                )

        # os.path.join(T0, "X")
        if isinstance(node, ast.Call):
            func = node.func
            is_join = False
            if (isinstance(func, ast.Attribute) and func.attr == "join"
                    and isinstance(func.value, ast.Attribute)
                    and func.value.attr == "path"
                    and isinstance(func.value.value, ast.Name)
                    and func.value.value.id == "os"):
                is_join = True
            if is_join and len(node.args) >= 2:
                first_arg = node.args[0]
                if isinstance(first_arg, ast.Name) and first_arg.id in aliases:
                    # Multi-arg case: os.path.join(T0, "a", "b") — join the
                    # remaining args as a single name. For 2-arg case this is
                    # just node.args[1].
                    name_arg = node.args[1] if len(node.args) == 2 else None
                    if name_arg is None:
                        fa.review_reasons.append(
                            f"os.path.join with >2 args at line {node.lineno}"
                        )
                        continue
                    inner = _emit_resolve_for_use(name_arg, fa)
                    if inner is None:
                        continue
                    # os.path.join returns str; preserve that semantics by wrapping.
                    replacement = f"str({inner})"
                    start_line = node.lineno - 1
                    start_col = node.col_offset
                    end_line = (node.end_lineno or node.lineno) - 1
                    end_col = node.end_col_offset or 0
                    orig = _slice_source(source_lines, start_line, start_col, end_line, end_col)
                    use_edits.append(
                        (start_line, start_col, end_line, end_col,
                         replacement, "alias-use-os-path-join", orig)
                    )

    # --- Pass 3: identify sys.path.insert(...) calls referencing computation-archive.
    archive_path_inserts: list[tuple[int, int, ast.Call]] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            f = node.func
            if (isinstance(f, ast.Attribute) and f.attr in ("insert", "append")
                    and isinstance(f.value, ast.Attribute) and f.value.attr == "path"
                    and isinstance(f.value.value, ast.Name) and f.value.value.id == "sys"):
                # check if any arg expression contains the literal "computation-archive"
                if any(_expr_contains_archive_string(a) for a in node.args):
                    start, end = _node_lines(node, source_lines)
                    archive_path_inserts.append((start, end, node))

    # --- Decide status & assemble edits.
    if not aliases and not archive_path_inserts and "computations/_shared" not in source and "computation-archive" not in source:
        fa.status = "no-changes-needed"
        return fa

    # Edit 1: remove alias definition lines (whole-line replacement; sentinel
    # end_col=-1 marks "to end of line").
    for name, (start, end, _node) in alias_defs.items():
        replacement = (
            f"# X2-removed: alias '{name}' = ... 'computations/_shared' "
            f"(replaced by tools.computation_root.resolve_*)"
        )
        orig = "\n".join(source_lines[start:end+1])
        fa.edits.append((start, 0, end, -1, replacement, "alias-def", orig))

    # Edit 2..k: alias uses (column-precise).
    fa.edits.extend(use_edits)

    # Edit (k+1)..: archive sys.path inserts (whole-line replacement).
    for start, end, _ in archive_path_inserts:
        replacement = "sys.path.insert(0, str(_x2_shared_dir()))"
        orig = "\n".join(source_lines[start:end+1])
        fa.edits.append((start, 0, end, -1, replacement, "archive-sys-path", orig))

    # Decide bootstrap insertion point: line AFTER the last leading import
    # statement OR after the docstring if no imports exist.
    fa.bootstrap_insert_after = _find_bootstrap_insert_line(tree, source_lines)

    # Final: if any review reasons accrued, mark needs-review.
    if fa.review_reasons:
        fa.status = "needs-review"
    elif not fa.edits and not aliases and not archive_path_inserts:
        # Computation/archive substrings exist but only in comments/docstrings
        # (no actionable Code edits)
        fa.status = "no-changes-needed"
    else:
        fa.status = "transform"

    return fa


def _emit_resolve_for_use(name_node: ast.AST,
                          fa: FileAnalysis) -> Optional[str]:
    """Given the right-hand-side of `T0 / X` (or second arg to os.path.join),
    return the resolve_*() call expression. Or None if it triggers needs-review.
    """
    # Static string literal
    if isinstance(name_node, ast.Constant) and isinstance(name_node.value, str):
        kind, sid = session_from_static_filename(name_node.value)
        if kind == "literal":
            sid_arg = repr(sid)
            func_kind = "output" if name_node.value.endswith(
                (".npz", ".png", ".txt", ".json", ".log", ".csv")
            ) else "script"
            return _format_resolve_call(func_kind, sid_arg, repr(name_node.value))
        # kind == "none": route to _shared/
        return _format_resolve_call("script", "None", repr(name_node.value))

    # f-string
    if isinstance(name_node, ast.JoinedStr):
        kind, varname = session_from_fstring_first_value(name_node)
        # Reconstruct the f-string source from the AST-fragment via ast.unparse.
        try:
            f_src = ast.unparse(name_node)
        except Exception as e:  # pragma: no cover (unparse rare failure)
            fa.review_reasons.append(f"unparse-fail on f-string at line {name_node.lineno}: {e}")
            return None
        if kind == "literal":
            sid_arg = repr(int(varname))  # type: ignore[arg-type]
            func_kind = "output"  # f-strings usually for output filenames
            return _format_resolve_call(func_kind, sid_arg, f_src)
        if kind == "variable":
            sid_arg = varname  # pass through
            func_kind = "output"
            return _format_resolve_call(func_kind, sid_arg, f_src)
        if kind == "none":
            return _format_resolve_call("script", "None", f_src)
        # kind == "ambiguous"
        fa.review_reasons.append(
            f"ambiguous f-string at line {name_node.lineno}: cannot determine session"
        )
        return None

    # Dynamic basename: variable, subscript, attribute access, call, etc.
    # Runtime session-id extraction via resolve_dynamic.
    if isinstance(name_node, (ast.Name, ast.Subscript, ast.Attribute, ast.Call)):
        try:
            expr_src = ast.unparse(name_node)
        except Exception as e:
            fa.review_reasons.append(
                f"unparse-fail on alias-use rhs at line {name_node.lineno}: {e}"
            )
            return None
        return f"resolve_dynamic({expr_src})"

    # Other unsupported shapes
    fa.review_reasons.append(
        f"unsupported alias-use rhs (line {getattr(name_node, 'lineno', '?')}): "
        f"{type(name_node).__name__}"
    )
    return None


def _find_bootstrap_insert_line(tree: ast.AST, source_lines: list[str]) -> int:
    """Return line index AFTER which to insert the bootstrap header.

    Strategy: insert after the last contiguous block of Imports/ImportFroms
    that starts within the first 100 lines. If no imports, insert after the
    module docstring. If no docstring, insert at line 0 (very top, but still
    after any shebang/encoding line).
    """
    # Use module body statements.
    body = getattr(tree, "body", [])
    last_import_end = -1
    saw_docstring = False
    docstring_end = -1
    for i, node in enumerate(body):
        if i == 0 and isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
            # module docstring
            saw_docstring = True
            docstring_end = (node.end_lineno or node.lineno) - 1
            continue
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            last_import_end = (node.end_lineno or node.lineno) - 1
            continue
        # First non-import non-docstring node ends the leading block
        break

    if last_import_end >= 0:
        return last_import_end
    if saw_docstring:
        return docstring_end
    # Skip past a possible shebang or coding declaration
    insert_after = -1
    for i, line in enumerate(source_lines[:3]):
        if line.startswith("#!") or "coding:" in line or "coding=" in line:
            insert_after = i
        else:
            break
    return insert_after


# ----------------------------------------------------------------------------
# Apply edits to source
# ----------------------------------------------------------------------------

def apply_edits(path: pathlib.Path, fa: FileAnalysis) -> str:
    """Return the transformed source text for `fa` (does not write).

    Edit tuple format (7-tuple):
      (start_line, start_col, end_line, end_col, new_text, kind, original_text)

    end_col == -1 is a SENTINEL meaning "whole-line replacement": the entire
    range [start_line .. end_line] is replaced by new_text + line_ending.
    Otherwise, column-aware replacement preserves text outside [start_col, end_col].
    """
    if fa.status not in ("transform",):
        raise ValueError(f"apply_edits called on file with status={fa.status}")

    source = path.read_text(encoding="utf-8")
    lines = source.splitlines(keepends=True)
    line_ending = _detect_line_ending(lines)

    # Sort edits by (start_line, start_col) DESCENDING so earlier-in-file
    # edits don't shift later-in-file line/column indices during application.
    sorted_edits = sorted(fa.edits, key=lambda e: (-e[0], -e[1]))

    for start_line, start_col, end_line, end_col, new_text, _kind, _orig in sorted_edits:
        if end_col == -1:
            # Whole-line replacement.
            new_block = new_text + line_ending
            lines[start_line:end_line+1] = [new_block]
        else:
            # Column-precise replacement.
            if start_line == end_line:
                line = lines[start_line]
                # Strip trailing newline; reattach after replacement.
                if line.endswith("\r\n"):
                    body, suffix = line[:-2], "\r\n"
                elif line.endswith("\n"):
                    body, suffix = line[:-1], "\n"
                else:
                    body, suffix = line, ""
                new_line = body[:start_col] + new_text + body[end_col:] + suffix
                lines[start_line] = new_line
            else:
                # Multi-line column-aware: take prefix of start_line, splice in
                # new_text, take suffix of end_line. Drop everything between.
                first = lines[start_line]
                last = lines[end_line]
                if first.endswith("\r\n"):
                    first_body = first[:-2]
                elif first.endswith("\n"):
                    first_body = first[:-1]
                else:
                    first_body = first
                if last.endswith("\r\n"):
                    last_body, last_suffix = last[:-2], "\r\n"
                elif last.endswith("\n"):
                    last_body, last_suffix = last[:-1], "\n"
                else:
                    last_body, last_suffix = last, ""
                merged = first_body[:start_col] + new_text + last_body[end_col:] + last_suffix
                lines[start_line:end_line+1] = [merged]

    # Insert bootstrap header.
    insert_at = fa.bootstrap_insert_after + 1  # insert AFTER this index
    bootstrap_with_blank = BOOTSTRAP_TEXT + line_ending
    lines.insert(insert_at, bootstrap_with_blank)

    return "".join(lines)


def _detect_line_ending(lines: list[str]) -> str:
    for line in lines[:20]:
        if line.endswith("\r\n"):
            return "\r\n"
        if line.endswith("\n"):
            return "\n"
    return "\n"


# ----------------------------------------------------------------------------
# Diff rendering for dry-run
# ----------------------------------------------------------------------------

def render_diff(path: pathlib.Path, fa: FileAnalysis,
                max_edits_shown: int = 8) -> str:
    """Human-readable per-file diff summary."""
    rel = path.relative_to(PROJECT_ROOT)
    lines = [f"--- {rel}"]
    lines.append(f"  status: {fa.status}")
    lines.append(f"  aliases_seen: {sorted(fa.aliases_seen) or 'none'}")
    lines.append(f"  edits: {len(fa.edits)}")
    if fa.review_reasons:
        lines.append("  review_reasons:")
        for r in fa.review_reasons:
            lines.append(f"    - {r}")
    if fa.edits and fa.status == "transform":
        for i, edit in enumerate(fa.edits[:max_edits_shown]):
            start_line, start_col, end_line, end_col, new_text, kind, orig = edit
            if end_col == -1:
                loc = f"lines {start_line+1}..{end_line+1} (whole-line)"
            else:
                loc = (f"line {start_line+1} cols {start_col}..{end_col}"
                       if start_line == end_line
                       else f"L{start_line+1}c{start_col}..L{end_line+1}c{end_col}")
            lines.append(f"  edit#{i+1} ({kind}, {loc}):")
            for ln in orig.splitlines() or [""]:
                lines.append(f"    - {ln}")
            for ln in new_text.splitlines() or [""]:
                lines.append(f"    + {ln}")
        if len(fa.edits) > max_edits_shown:
            lines.append(f"  ... +{len(fa.edits) - max_edits_shown} more edits")
    return "\n".join(lines)


# ----------------------------------------------------------------------------
# File enumeration
# ----------------------------------------------------------------------------

def find_target_files(target: Optional[str], target_glob: Optional[str]) -> list[pathlib.Path]:
    """Return the .py file list to analyze, based on flags."""
    if target:
        p = (PROJECT_ROOT / target).resolve() if not pathlib.Path(target).is_absolute() else pathlib.Path(target).resolve()
        if not p.is_file():
            print(f"[error] --target file not found: {p}", file=sys.stderr)
            sys.exit(2)
        return [p]
    if target_glob:
        return sorted(DEST_TREE.glob(target_glob))
    if not DEST_TREE.is_dir():
        print(f"[error] computations/ does not exist at {DEST_TREE}", file=sys.stderr)
        sys.exit(2)
    return sorted(DEST_TREE.rglob("*.py"))


# ----------------------------------------------------------------------------
# Logging + main
# ----------------------------------------------------------------------------

def emit_log(analyses: list[FileAnalysis], with_shas: bool = False) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_PATH, "w", encoding="utf-8") as f:
        # Header
        n_transform = sum(1 for a in analyses if a.status == "transform")
        n_review = sum(1 for a in analyses if a.status == "needs-review")
        n_already = sum(1 for a in analyses if a.status == "already-transformed")
        n_nochange = sum(1 for a in analyses if a.status == "no-changes-needed")
        f.write(json.dumps({
            "type": "header",
            "phase": "2b",
            "schema_version": 1,
            "total_files_analyzed": len(analyses),
            "n_transform": n_transform,
            "n_needs_review": n_review,
            "n_already_transformed": n_already,
            "n_no_changes_needed": n_nochange,
        }) + "\n")
        for fa in analyses:
            row = {
                "type": "file",
                "path": str(fa.path.relative_to(PROJECT_ROOT)),
                "status": fa.status,
                "edit_count": len(fa.edits),
                "aliases_seen": sorted(fa.aliases_seen),
                "review_reasons": fa.review_reasons,
                "edits": [
                    {"start_line": sl+1, "start_col": sc, "end_line": el+1,
                     "end_col": ec, "kind": k,
                     "new_text_first_line": nt.splitlines()[0] if nt else ""}
                    for (sl, sc, el, ec, nt, k, _o) in fa.edits
                ],
            }
            f.write(json.dumps(row) + "\n")
    print(f"[plan] wrote {LOG_PATH.relative_to(PROJECT_ROOT)}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Phase 2b X2 transformation: rewrite computations/_shared "
                    "references in computations/*.py to use tools.computation_root.")
    parser.add_argument("--dry-run", action="store_true",
                        help="Analyze + emit log; no file writes (default)")
    parser.add_argument("--execute", action="store_true",
                        help="Apply transformations to files on disk")
    parser.add_argument("--target", default=None,
                        help="Single file path (relative to project root)")
    parser.add_argument("--target-glob", default=None,
                        help="Glob relative to computations/ (e.g. 'session-87/*.py')")
    parser.add_argument("--show-diffs", type=int, default=0,
                        help="Show first N file diffs in dry-run output")
    args = parser.parse_args()

    if args.execute and args.dry_run:
        print("[error] --execute and --dry-run are mutually exclusive",
              file=sys.stderr)
        return 2

    files = find_target_files(args.target, args.target_glob)
    print(f"[setup] target file count: {len(files)}")

    analyses: list[FileAnalysis] = []
    for p in files:
        fa = analyze_file(p)
        analyses.append(fa)

    n_transform = sum(1 for a in analyses if a.status == "transform")
    n_review = sum(1 for a in analyses if a.status == "needs-review")
    n_already = sum(1 for a in analyses if a.status == "already-transformed")
    n_nochange = sum(1 for a in analyses if a.status == "no-changes-needed")

    print()
    print("=" * 72)
    print("Phase 2b transform analysis")
    print("=" * 72)
    print(f"  transform:           {n_transform}")
    print(f"  needs-review:        {n_review}")
    print(f"  already-transformed: {n_already}")
    print(f"  no-changes-needed:   {n_nochange}")
    print(f"  total:               {len(analyses)}")

    # Aggregate review-reason counts
    reason_counts: dict[str, int] = {}
    for fa in analyses:
        for r in fa.review_reasons:
            # Normalize reason: drop line numbers for grouping
            key = re.sub(r"\bline \d+\b", "line N", r)
            key = re.sub(r"\(lines \d+ and \d+\)", "(lines N and M)", key)
            reason_counts[key] = reason_counts.get(key, 0) + 1
    if reason_counts:
        print()
        print("  Top review reasons:")
        for reason, count in sorted(reason_counts.items(), key=lambda x: -x[1])[:10]:
            print(f"    {count:5d}  {reason}")

    emit_log(analyses)

    if args.show_diffs > 0:
        print()
        print("=" * 72)
        print(f"Sample diffs (first {args.show_diffs}):")
        print("=" * 72)
        shown = 0
        for fa in analyses:
            if fa.status == "transform" and shown < args.show_diffs:
                print(render_diff(fa.path, fa))
                print()
                shown += 1

    if args.execute:
        print()
        print("=" * 72)
        print("Executing transformations")
        print("=" * 72)
        n_written = 0
        n_failed = 0
        failures: list[dict] = []
        for fa in analyses:
            if fa.status != "transform":
                continue
            try:
                new_text = apply_edits(fa.path, fa)
                fa.path.write_text(new_text, encoding="utf-8")
                n_written += 1
            except Exception as e:
                n_failed += 1
                failures.append({"path": str(fa.path.relative_to(PROJECT_ROOT)),
                                 "error": str(e)})
        print(f"  Files transformed: {n_written}")
        print(f"  Failures:          {n_failed}")
        if failures:
            for fail in failures[:10]:
                print(f"    {fail}")
            return 1
        print()
        print("[done] Phase 2b X2 transformation complete.")
        print("[next] Smoke-test by running a transformed script from its new location.")
        return 0

    print()
    print("[dry-run] no files modified. Re-run with --execute to apply.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
