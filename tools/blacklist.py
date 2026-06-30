"""blacklist.py — centralized exclusion data for the tools/ pipeline.

Consolidates exclusion sets that were previously scattered across
extract_entities.py, _build_constants_table.py, _path_existence_audit.py,
_dump_kb_to_markdown.py, and _phase3_path_string_migration.py.

Import what you need; do not duplicate these sets in producing scripts.
"""

# ---------------------------------------------------------------------------
# canonical_constants.py entity-table exclusions
# ---------------------------------------------------------------------------
# Module-level names that appear in canonical_constants.py but are NOT
# data constants — config dicts, audit-internal, etc. Used by
# extract_entities.extract_canonical_constants_entities() to filter the
# constants table.

CONSTANTS_EXCLUDED_NAMES = frozenset({
    "PROVENANCE",        # the provenance metadata dict — joined separately
    "CHANNEL_LABELS",    # config dict, not a physics constant
})

# Any name starting with one of these prefixes is extractor-internal
# configuration, not a physics constant.
CONSTANTS_EXCLUDED_PREFIXES = (
    "AUDIT_",     # AUDIT_EXEMPT_SCRIPTS, AUDIT_PATTERNS_COMPILED, AUDIT_SESSION_FLOOR
    "EXEMPT_",    # EXEMPT_FILES
)


def is_constants_excluded(name: str) -> bool:
    """True if a canonical_constants.py top-level name should be skipped."""
    if name in CONSTANTS_EXCLUDED_NAMES:
        return True
    return any(name.startswith(p) for p in CONSTANTS_EXCLUDED_PREFIXES)


# ---------------------------------------------------------------------------
# Path-existence audit self-skips
# ---------------------------------------------------------------------------
# Audit/migration tooling whose docstrings/source contain example path
# patterns by design — would produce false positives in a path-existence scan.

PATH_AUDIT_SELF_SKIP = frozenset({
    "tools/_path_existence_audit.py",
    "tools/path_existence.py",                  # consolidated successor (S92+)
    "tools/_path_existence_fix.py",
    "tools/_phase3_path_string_migration.py",
})


# ---------------------------------------------------------------------------
# Knowledge-index markdown dump filters
# ---------------------------------------------------------------------------
# Keys to skip when dumping knowledge-index.json to a flat markdown
# representation (used by _dump_kb_to_markdown.py historically).

KB_DUMP_SKIP_KEYS = frozenset({
    "$schema",
    "generated",
})
