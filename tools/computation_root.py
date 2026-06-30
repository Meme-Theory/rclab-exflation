"""tools/computation_root.py — abstraction layer for computation <-> computations dual-root.

Phase 1 of the parallel-mirror restructure plan (S88+ rigging).

This module is the SINGLE source of truth for "where do computation-style computation
artifacts live?" — script paths, output paths, glob patterns. Consumers
(audit scripts, hooks, future extract_entities.py) call resolve_script(...),
resolve_output(...), resolve_glob(...) instead of hardcoding 'computations/'.

Active root (post-2026-05-03 Phase-4 cutover): the default is 'computations',
i.e. resolvers target the nested live tree (computations/session-N/ +
computations/_shared/). This default was HARDENED S96 W2 from the stale
pre-cutover 'computations/_shared' so that a missing config file falls back to
the CORRECT live tree rather than the obsolete flat layout.

The active root may be overridden (e.g. to roll back to the flat
'computations/_shared' layout) via computations/_shared/computation_root.json
(active_root field) OR the env-var override COMPUTATION_ROOT=computations/_shared.
The config file was RELOCATED S96 W2 from tools/ to computations/_shared/ (it is
runtime config for the computations/ tree, not knowledge-index infra; living in
tools/ exposed it to /weave --update hygiene, which deleted it in commit
5056e28a and silently reverted resolve_* to the flat default).

API:
    get_active_root() -> str
    resolve_script(session_id, basename) -> pathlib.Path
    resolve_output(session_id, output_name) -> pathlib.Path
    resolve_glob(session_id, pattern) -> list[pathlib.Path]
    is_mirror_active() -> bool
    get_known_roots() -> list[str]
    project_root() -> pathlib.Path
    config_path() -> pathlib.Path

session_id semantics:
    int (e.g. 86)        -> session-N folder under the active root
    None                 -> top-level (computations/) or _shared/ (computations/)

This module has NO side effects at import time. Path resolution is pure (no
filesystem reads beyond the optional config-file read in get_active_root()).
"""

from __future__ import annotations

import json
import os
import pathlib
import re
from typing import Optional

# ----------------------------------------------------------------------------
# Constants
# ----------------------------------------------------------------------------

DEFAULT_ROOT = "computations"  # S96 W2: hardened from "computations/_shared" (stale pre-cutover) to the post-2026-05-03 nested live tree, so a missing config can no longer silently misroute to the obsolete flat layout
KNOWN_ROOTS = ("computations/_shared", "computations")
ENV_VAR = "COMPUTATION_ROOT"
CONFIG_FILENAME = "computation_root.json"
SHARED_SUBDIR = "_shared"  # under computations/ only; computations/_shared is flat


# ----------------------------------------------------------------------------
# Project-root and config location
# ----------------------------------------------------------------------------

def project_root() -> pathlib.Path:
    """Return the project root directory.

    Computed as <this-file>/parent/parent (i.e., tools/computation_root.py
    -> tools/ -> project root). Works regardless of cwd.
    """
    return pathlib.Path(__file__).resolve().parent.parent


def config_path() -> pathlib.Path:
    """Return the absolute path to computations/_shared/computation_root.json.

    Relocated S96 W2 from tools/ to computations/_shared/: the flag is runtime
    config for the computations/ tree (shared computation infrastructure,
    alongside canonical_constants.py), NOT knowledge-index infra. Living in tools/
    exposed it to /weave --update 'audit-clean hygiene', which deleted it in
    commit 5056e28a and silently reverted resolve_* to the flat default. This
    path is active-root-INDEPENDENT (it is read in order to DETERMINE the active
    root), so it is a fixed project-relative location, never via resolve_*.
    """
    return project_root() / "computations" / "_shared" / CONFIG_FILENAME


# ----------------------------------------------------------------------------
# Active-root resolution
# ----------------------------------------------------------------------------

def get_known_roots() -> list[str]:
    """Return the list of valid root-name strings."""
    return list(KNOWN_ROOTS)


def get_active_root() -> str:
    """Return the active computation root name.

    Resolution order:
      1. Env var COMPUTATION_ROOT (per-process override, useful for testing)
      2. Config file computations/_shared/computation_root.json -> active_root field
      3. DEFAULT_ROOT ("computations") if config is missing or unreadable

    Raises ValueError if the resolved value is not in KNOWN_ROOTS.
    """
    env_value = os.environ.get(ENV_VAR)
    if env_value is not None:
        if env_value not in KNOWN_ROOTS:
            raise ValueError(
                f"Env var {ENV_VAR}={env_value!r} is not a known root; "
                f"must be one of {KNOWN_ROOTS}"
            )
        return env_value

    cfg = config_path()
    if not cfg.exists():
        # Graceful default: if config absent, fall back to the post-2026-05-03
        # cutover live tree (nested computations/session-N/ + computations/_shared/).
        # Hardened S96 W2 from the stale flat 'computations/_shared' so a deleted
        # config can no longer silently misroute to the obsolete flat layout.
        return DEFAULT_ROOT

    try:
        with open(cfg, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError):
        # Defensive: corrupt config -> fall back to default rather than crash
        # consumers. Inertness invariant: an unreadable config preserves
        # legacy behavior.
        return DEFAULT_ROOT

    root = data.get("active_root", DEFAULT_ROOT)
    if root not in KNOWN_ROOTS:
        raise ValueError(
            f"Config {cfg} has active_root={root!r}; "
            f"must be one of {KNOWN_ROOTS}"
        )
    return root


def is_mirror_active() -> bool:
    """Return True if BOTH computations/ and computations/ exist on disk.

    Useful for diagnostics during the parallel-mirror window. Does NOT
    indicate which root is currently active — that's get_active_root().
    """
    root = project_root()
    return (root / "computations/_shared").is_dir() and (root / "computations").is_dir()


# ----------------------------------------------------------------------------
# Path resolvers
# ----------------------------------------------------------------------------

def _root_dir(active: str) -> pathlib.Path:
    """Return absolute path of the active root directory."""
    return project_root() / active


def resolve_script(session_id: Optional[int], basename: str) -> pathlib.Path:
    """Resolve a script's filesystem path under the active root.

    Args:
        session_id: integer session number (e.g. 86), or None for top-level
                    files (canonical_constants.py, audit scripts, _shared infra).
        basename:   the filename, e.g. 's86_w8_2_audit.py'.

    Examples (active='computations/_shared' — flat layout, current canonical):
        resolve_script(86, 's86_w8.py')             -> computations/_shared/s86_w8.py
        resolve_script(None, 'canonical_constants.py')
                                                     -> computations/_shared/canonical_constants.py

    Examples (active='computations' — legacy nested layout):
        resolve_script(86, 's86_w8.py')             -> computations/session-86/s86_w8.py
        resolve_script(None, 'canonical_constants.py')
                                                     -> computations/_shared/canonical_constants.py

    NOTE: in BOTH active modes, the actual on-disk canonical file lives at
    `computations/_shared/canonical_constants.py`. The legacy mode reaches it
    via `root / SHARED_SUBDIR / basename` (i.e., 'computations' + '_shared');
    the flat mode reaches it via `root / basename` where root is already
    'computations/_shared'. NEVER use a bare path 'computations/canonical_constants.py'
    in scripts or documentation — the file does not exist at that path.
    """
    active = get_active_root()
    root = _root_dir(active)

    if active == "computations/_shared":
        # Flat layout: ignore session_id, return root/basename directly.
        return root / basename

    if active == "computations":
        if session_id is None:
            return root / SHARED_SUBDIR / basename
        return root / f"session-{int(session_id)}" / basename

    raise ValueError(f"Unknown active root: {active}")


def resolve_output(session_id: Optional[int], output_name: str) -> pathlib.Path:
    """Resolve an output artifact's filesystem path under the active root.

    Same routing rules as resolve_script(). Use this for verdict-file paths,
    .npz outputs, .png outputs, .txt logs.

    Examples (active='computations/_shared'):
        resolve_output(86, 's86_gate_verdicts.txt')
                                -> computations/s86_gate_verdicts.txt
        resolve_output(86, 's86_w8.npz')
                                -> computations/s86_w8.npz

    Examples (active='computations'):
        resolve_output(86, 's86_gate_verdicts.txt')
                                -> computations/session-86/s86_gate_verdicts.txt
        resolve_output(86, 's86_w8.npz')
                                -> computations/session-86/s86_w8.npz
    """
    # Identical routing logic to resolve_script; kept as a separate function
    # so the call-site reads as the writer-side intent (output artifact, not
    # script file) and so future divergence (e.g., an outputs/ subdirectory
    # under session-N/) can be implemented without refactoring callers.
    return resolve_script(session_id, output_name)


_DYNAMIC_SESSION_PATTERNS = (
    re.compile(r"^s(\d+)[_a-zA-Z]"),
    re.compile(r"^t3_S(\d+)[A-Z_]"),
    re.compile(r"^_t3_s(\d+)[_a-zA-Z]"),
    re.compile(r"^prep_T3-S(\d+)[A-Z-]"),
)


def resolve_dynamic(basename) -> pathlib.Path:
    """Resolve a basename whose session_id is not statically known.

    Used by Phase 2b X2-transformed scripts where `T0 / variable_name` or
    `T0 / Path(c).name` is replaced with `resolve_dynamic(variable_name)`.
    The session_id is extracted from the basename's prefix at runtime.

    Routing:
      - Basename matches s{N}_*       -> resolve_output(N, basename)
      - Basename matches t3 patterns  -> resolve_output(N, basename)
      - Otherwise                     -> resolve_script(None, basename)
    """
    name = str(basename)
    for pat in _DYNAMIC_SESSION_PATTERNS:
        m = pat.match(name)
        if m:
            return resolve_output(int(m.group(1)), name)
    return resolve_script(None, name)


def resolve_glob(session_id: Optional[int], pattern: str) -> list[pathlib.Path]:
    """Glob-replacement that honors the active root.

    Args:
        session_id: integer session number, or None to glob across ALL sessions
                    under the active root (computations) / across the flat tree
                    (computations/_shared).
        pattern:    glob pattern, e.g. 's*_*.py' or 's86_*.npz'.

    Examples (active='computations/_shared'):
        resolve_glob(None, 's*_*.py')
            -> [Path('computations/s05_*.py'), ..., Path('computations/s88_*.py')]
        resolve_glob(86, 's86_*.npz')
            -> [Path('computations/s86_*.npz') matches]

    Examples (active='computations'):
        resolve_glob(None, 's*_*.py')
            -> matches across computations/session-*/s*_*.py
        resolve_glob(86, 's86_*.npz')
            -> matches under computations/session-86/s86_*.npz

    Returns: list of pathlib.Path objects (sorted for determinism).
    """
    active = get_active_root()
    root = _root_dir(active)

    if active == "computations/_shared":
        # Flat: glob the whole root for the pattern (session_id is informational
        # only since the tree is flat; pattern restricts to the right session
        # via its 's86_*' naming convention).
        return sorted(root.glob(pattern))

    if active == "computations":
        if session_id is None:
            return sorted(root.glob(f"session-*/{pattern}"))
        return sorted((root / f"session-{int(session_id)}").glob(pattern))

    raise ValueError(f"Unknown active root: {active}")


# ----------------------------------------------------------------------------
# Self-test (safe to run; no side effects on consumers)
# ----------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 72)
    print("computation_root.py self-test")
    print("=" * 72)
    print(f"  project_root         = {project_root()}")
    print(f"  config_path          = {config_path()}")
    print(f"  config_path exists   = {config_path().exists()}")
    print(f"  get_known_roots()    = {get_known_roots()}")
    print(f"  get_active_root()    = {get_active_root()}")
    print(f"  is_mirror_active()   = {is_mirror_active()}")
    print()
    print("  Path resolutions under current active root:")
    print(f"    resolve_script(86, 's86_w8_audit.py')        = "
          f"{resolve_script(86, 's86_w8_audit.py')}")
    print(f"    resolve_script(None, 'canonical_constants.py') = "
          f"{resolve_script(None, 'canonical_constants.py')}")
    print(f"    resolve_output(86, 's86_gate_verdicts.txt')  = "
          f"{resolve_output(86, 's86_gate_verdicts.txt')}")
    print(f"    resolve_glob(86, 's86_*.npz')[:3]            = "
          f"{resolve_glob(86, 's86_*.npz')[:3]}")
    print()
    print("Phase 1 inert install: under default flag, every resolution above")
    print("must return a path under computations/. Verify visually OR")
    print("run tools/_phase1_inertness_check.py for an assertion-based check.")
