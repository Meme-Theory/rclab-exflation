"""whitelist.py — centralized canonical-vocabulary data for the tools/ pipeline.

Consolidates the cross-cutting vocabulary that multiple scripts need to share
(edge-type taxonomy + entity-type normalization). Local vocabularies that
only one script consumes (e.g. ROLE_VOCAB in format_generations.py) stay
co-located with their consumer.

Import what you need; do not duplicate these structures in producing scripts.
"""

# ---------------------------------------------------------------------------
# Edge-type taxonomy (consumed by extract_entities.extract_edges)
# ---------------------------------------------------------------------------
# Maps every accepted edge-relation phrasing to its canonical form. Multi-key
# alias entries collapse synonyms (e.g. "closes" → "closed_by", "depends" →
# "depends_on") so the index sees one canonical relation regardless of which
# wording the session author used.

EDGE_TYPE_CANONICAL = {
    # Logical entailment
    "implies": "implies",
    "supersedes": "supersedes",
    "superseded_by": "superseded_by",
    # Closure / refutation
    "closed_by": "closed_by",
    "closes": "closed_by",
    "refutes": "refutes",
    "refuted_by": "refuted_by",
    "contradicts": "contradicts",
    # Dependency
    "depends_on": "depends_on",
    "depends": "depends_on",
    "derived_from": "derived_from",
    "derives_from": "derived_from",
    "enables": "enables",
    # Validation (added S81 for cross-verdict chains)
    "reproduces": "reproduces",       # this gate's value matches a canonical result
    "cross_validates": "cross_validates",  # agrees w/ another gate on the same quantity
    "confirms": "confirms",            # provides independent evidence for
    "validates": "confirms",           # alias
    "grounds": "grounds",              # provides numerical basis for
    "feeds_into": "feeds_into",        # output used as input by downstream gate
    "consumes": "feeds_into",          # alias (reverse phrasing)
    "bounds": "bounds",                # provides constraint on (upper/lower)
    "refines": "refines",              # provides tighter value than prior
    # Attribution edges (Phase 1 / harvester.py attribution subcommand).
    "authored_by": "authored_by",          # primary authorship (gate/file/session -> researcher)
    "co_authored_by": "co_authored_by",    # co-author / co-signer attribution
    "reviewed_by": "reviewed_by",          # adversarial review / evaluator
    "participates_in": "participates_in",  # researcher -> workshop participant
    "authored_round": "authored_round",    # researcher -> workshop round opener/responder
    "cites_prior_session": "cites_prior_session",  # gate -> prior-session provenance
    "discussed_in": "discussed_in",        # body-text mention (G1 inference)
    "synthesized_by": "synthesized_by",    # orchestrator-aggregated section
    "excluded_from": "excluded_from",      # BLACKLISTED tag (negative authorship)
    "cited_in": "cited_in",                # researcher -> session/data_provenance (paper cited in framework file)
    # Chain-of-custody edges (Phase 1.1 / harvester.py chain-of-custody subcommand).
    "carries_forward": "carries_forward",  # sessions -> gates:CF-N (4-field carry-forward spec)
    "anchored_in": "anchored_in",          # gates -> sessions (verdict-file ground truth)
    "succ_of": "succ_of",                  # gates -> gates (within-wave dispatch adjacency)
}


# ---------------------------------------------------------------------------
# Entity-type alias normalization (consumed by extract_entities.extract_edges)
# ---------------------------------------------------------------------------
# Maps every accepted entity-type label (singular/plural/legacy form) to its
# canonical table name. Producing scripts emit edges keyed on whatever
# pluralization the author used; extract_entities.py normalizes via this map.

ENTITY_TYPE_ALIASES = {
    "theorems": "theorems",
    "theorem": "theorems",
    "closed": "closed_mechanisms",
    "closed_mechanisms": "closed_mechanisms",
    "mechanism": "closed_mechanisms",
    "gates": "gates",
    "gate": "gates",
    "open": "open_channels",
    "open_channels": "open_channels",
    "sessions": "sessions",
    "session": "sessions",
    "researchers": "researchers",
    "researcher": "researchers",
    "agents": "agents",
    "agent": "agents",
    "session_files": "session_files",
    "session_file": "session_files",
    "registries": "registries",
    "registry": "registries",
    "data": "data_provenance",
    "data_provenance": "data_provenance",
    "script": "data_provenance",
    "equations": "equations",
    "equation": "equations",
    "constants": "constants",
    "constant": "constants",
}
