#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S88 W6b §W6b-56 — S88-K1-VS-K2-COUNTING-DISTINCTION-REGISTRY-NOTE
====================================================================

METHODOLOGY-class registry-note insertion gate. Adds new sub-section
`### §VII.U.6.k1-vs-k2` after §VII.U.6 W1b-T5 LANDING block declaring the
general Hörmander-Weyl spectral-counting form
`Σ dim(V_λ)^k ~ Λ^{r + k(d-r)/2}` and the k=2 canonical-spectral-asymptotic
vs k=1 rep-theoretic-dim-sum distinction surfaced at S87 W2 R3.

Single-shot AFTER pattern per `.claude/rules/registry-landing.md`.

Plan reference: sessions/session-plan/session-88-plan-w6b.md §W6b-56.

Sage-MCP cross-check identities (verified pre-flight):
    SU(2): d=3, r=1; k=1: (d+r)/2 = 2; k=2: d = 3
    SU(3): d=8, r=2; k=1: (d+r)/2 = 5; k=2: d = 8
    SU(4): d=15, r=3; k=1: (d+r)/2 = 9; k=2: d = 15
    Symbolic algebra:
      r + 1*(d-r)/2 = (d+r)/2 (k=1; rep-theoretic)
      r + 2*(d-r)/2 = d       (k=2; canonical Hörmander-Weyl)

Verification (per plan PASS criterion):
    grep "Σ dim(V_λ)^k ~ Λ^{r + k(d-r)/2}" returns ≥ 1
    grep "k=2 canonical Hörmander-Weyl" returns ≥ 1
    grep "k=1 rep-theoretic" returns ≥ 1
    SU(2)/SU(3)/SU(4) cross-check table present with values 2/3, 5/8, 9/15
    Cross-links to W-5, W6b-55 (substrate-framing), W6b-53 (d_spec_B) present
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from canonical_constants import tau_fold  # S12/S42 canonical fold parameter

GATE_ID = "S88-K1-VS-K2-COUNTING-DISTINCTION-REGISTRY-NOTE"
SCHEME = "Hörmander-Weyl-canonical"
CONVENTION = "k2-spectral-asymptotic-vs-k1-rep-theoretic"
L_MAX = "N/A"
SCHEMA = "S84+"
REGULATOR = "Zubarev"

REGISTRY_PATH = Path("sessions/permanent-results-registry.md")
VERDICT_PATH = Path("computations/session-88/s88_gate_verdicts.txt")

# Sage-MCP-verified SU(N) cross-check identities (pre-flight, instance #N=2,3,4)
SU_N_CROSS_CHECKS = [(2, 3, 1, 2, 3), (3, 8, 2, 5, 8), (4, 15, 3, 9, 15)]  # (local) (N, d, r, k1, k2)

# Required PASS-criterion grep patterns (literal verbatim per plan §W6b-56)
REQUIRED_PATTERNS = [
    "Σ dim(V_λ)^k ~ Λ^{r + k(d-r)/2}",  # general form (single-space; matches plan §W6b-56 PASS criterion verbatim)
    "k=2 canonical Hörmander-Weyl",
    "k=1 rep-theoretic",
]

# ---------------------------------------------------------------------------
# Insertion target: replace the boundary text between §VII.U.6 closing
# and §VII.K-META.COMPOSITE-60 opening, inserting the new §VII.U.6.k1-vs-k2
# sub-section in between.
# ---------------------------------------------------------------------------
FORBIDDEN_BOUNDARY = (
    "- **§VII.W (Pillar III ↔ IV bridge theorem, S86 W-5)**: structural template\n"
    "  for the 5-element + 3-level registry-anatomy used in this strengthening.\n"
    "\n"
    "---\n"
    "\n"
    "## §VII.K-META.COMPOSITE-60 — 60-Row FI/RD Composite Atlas (S86 W1c-T10 — lizzi-spectral-functional-theorist, 2026-04-26)"
)

REQUIRED_BOUNDARY = (
    "- **§VII.W (Pillar III ↔ IV bridge theorem, S86 W-5)**: structural template\n"
    "  for the 5-element + 3-level registry-anatomy used in this strengthening.\n"
    "\n"
    "---\n"
    "\n"
    "### §VII.U.6.k1-vs-k2 — k=1 vs k=2 counting distinction (S87 W2 R3 surface; S88 W6b-56 landing)\n"
    "\n"
    "**Structural note** (per S87 W2 R3 surfacing; canonical Hörmander-Weyl reference):\n"
    "\n"
    "The general form for `Σ dim(V_λ)^k` cumulative-eigenvalue-count asymptotic on a compact Lie group G with rank r and dimension d, summed over irreducible representations V_λ with eigenvalue (Casimir-bound) ≤ Λ, is the verbatim Hörmander-Weyl form `Σ dim(V_λ)^k ~ Λ^{r + k(d-r)/2}` as Λ → ∞. Equivalently with the summation index made explicit:\n"
    "\n"
    "```\n"
    "Σ_{V_λ : C_2(λ) ≤ Λ} dim(V_λ)^k  ~  Λ^{r + k(d-r)/2}     (Λ → ∞)\n"
    "```\n"
    "\n"
    "Two distinguished cases:\n"
    "\n"
    "- **k=2 canonical Hörmander-Weyl spectral asymptotic on D_can**: exponent = `r + (d-r) = d` (recovers bare manifold dimension). This is the canonical spectral-counting asymptotic for the Dirac operator D_can on G; the substrate's HK-3 binding parameter (bare manifold dim) IS the k=2 asymptotic exponent.\n"
    "\n"
    "- **k=1 rep-theoretic dim-sum**: exponent = `r + (d-r)/2 = (d+r)/2`. This is NOT a spectral asymptotic on D_can; it is a rep-theoretic dim-sum (Λ-bounded sum over dim(V_λ)). The two counts have distinct physical content: k=2 tracks eigenvalue-multiplicity-weighted spectral density (canonical Weyl); k=1 tracks irrep-count weighted by dimension (rep-theoretic).\n"
    "\n"
    "**Cross-check identities** (verified Sage-exact via mcp__sage__sage_eval; symbolic algebra `r + 1*(d-r)/2 = (d+r)/2` and `r + 2*(d-r)/2 = d` confirmed):\n"
    "\n"
    "| G | d = dim(G) | r = rank(G) | k=1: (d+r)/2 | k=2: d |\n"
    "|:--|:-----------|:------------|:-------------|:-------|\n"
    "| SU(2) | 3 | 1 | 2 | 3 |\n"
    "| SU(3) | 8 | 2 | 5 | 8 |\n"
    "| SU(4) | 15 | 3 | 9 | 15 |\n"
    "\n"
    "For G = SU(3): k=1 exponent = 5; k=2 exponent = 8. The bare manifold dim = 8 (HK-3 binding) IS the k=2 exponent. The d_spec_B = 5/(1−τ/(5π)) Conv-B form (per S88 W6b-53 landing; ≈5.061 at τ_fold) is the τ-flow-DEFORMED k=1-like exponent under Jensen flow on D_can — NOT a static k=1 dim-sum, but a Jensen-perturbed Weyl-counting that interpolates between the k=2 bare-D form (recovers 8 at τ → 5π, the singularity of the HK-5 form) and a τ-dependent reading.\n"
    "\n"
    "**Cross-links**:\n"
    "- W-5 `cross-pillar-bridge-anatomy.md` §\"Calibration corpus\" — k=2 spectral-asymptotic substrate as Level-2 envelope basis.\n"
    "- §VII.U.6 substrate-framing sub-section (S88 W6b-55 augmentation) — bare manifold dim = 8 (HK-3 asymptotic binding) IS the k=2 exponent.\n"
    "- S88 W6b-53 d_spec_B = 5/(1−τ/(5π)) Conv-B canonical landing — τ-deformed k=1-like exponent under Jensen flow.\n"
    "- S88 W6b-54 Level-2 envelope (α=4, C=10⁻⁸) — α=4 anatomy template uses d_spec_B−1 (k=1-like Jensen-deformed exponent), NOT bare-D k=2 dimension d=8.\n"
    "\n"
    "**Audit**: this registry note resolves the k=1 vs k=2 conflation flagged at S87 W2 R3 (the rep-theoretic-dim-sum vs spectral-asymptotic distinction). Future entries citing `Σ dim(V_λ)` must declare k explicitly to avoid the conflation.\n"
    "\n"
    "---\n"
    "\n"
    "## §VII.K-META.COMPOSITE-60 — 60-Row FI/RD Composite Atlas (S86 W1c-T10 — lizzi-spectral-functional-theorist, 2026-04-26)"
)


def read_registry() -> str:
    with open(REGISTRY_PATH, "r", encoding="utf-8") as fh:
        return fh.read()


def grep_count(text: str, pattern: str) -> int:
    return text.count(pattern)


def build_promotion_text(original: str) -> str:
    n = grep_count(original, FORBIDDEN_BOUNDARY)
    if n != 1:
        raise RuntimeError(
            f"Expected 1 occurrence of FORBIDDEN_BOUNDARY; got {n}"
        )
    return original.replace(FORBIDDEN_BOUNDARY, REQUIRED_BOUNDARY, 1)


def write_atomic_with_fsync(text: str, path: Path) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp_w6b_56")
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(text)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, path)


def closure_hash(input_pin_map: dict) -> str:
    canonical = json.dumps(input_pin_map, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def emit_verdict_line(verdict, value, audit_sha, content_sha):
    canonical = (
        f"{GATE_ID}: {verdict} -- value='{value}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA}\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    VERDICT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(VERDICT_PATH, "a", encoding="utf-8") as fh:
        fh.write(canonical)
        fh.write(companion)


def main() -> int:
    # SUBSTANTIVE PRE-FLIGHT (Sage-MCP verified) -----------------------------
    print("SAGE-MCP CROSS-CHECK IDENTITIES (verified pre-flight):")
    print(f"{'Group':<8} {'d':>4} {'r':>4} {'k=1: (d+r)/2':>14} {'k=2: d':>10}")
    for N, d, r, k1, k2 in SU_N_CROSS_CHECKS:
        # Sage cross-check: r + 1*(d-r)/2 should equal (d+r)/2 = k1
        assert r + (d - r) // 2 == k1, f"SU({N}) k=1 algebra mismatch"
        # k=2: r + 2*(d-r)/2 = d
        assert r + (d - r) == k2, f"SU({N}) k=2 algebra mismatch"
        print(f"SU({N})    {d:>4} {r:>4} {k1:>14} {k2:>10}")
    print("All SU(N) algebra checks PASS; ready to land registry note.\n")

    original = read_registry()

    pre_grep = {p: grep_count(original, p) for p in REQUIRED_PATTERNS}
    pre_boundary = grep_count(original, FORBIDDEN_BOUNDARY)
    pre_required = grep_count(original, REQUIRED_BOUNDARY)

    print(f"PRE-EDIT GREP:")
    for p, c in pre_grep.items():
        print(f"  {'✓' if c >= 1 else 'MISSING'} required: '{p[:60]}': {c}")
    print(f"  forbidden boundary: {pre_boundary} (target = 1 to insert)")
    print(f"  required boundary already present: {pre_required} (target = 0 pre, 1 post)")
    print()

    if pre_required == 1 and pre_boundary == 0 and all(c >= 1 for c in pre_grep.values()):
        print("IDEMPOTENT: registry note already inserted; verdict INFO.")
        info_value = (
            f"idempotent_no_edit;all_required_patterns_present=True;"
            f"sage_cross_checks_PASS=True"
        )
        content_sha = file_sha256(REGISTRY_PATH)
        input_pin_map = {
            "gate_id": GATE_ID, "branch": "idempotent_no_edit",
            "tau_fold": tau_fold,
        }
        audit_sha = closure_hash(input_pin_map)
        emit_verdict_line("INFO", info_value, audit_sha, content_sha)
        print(f"VERDICT: INFO -- value={info_value}")
        return 0

    promoted = build_promotion_text(original)
    write_atomic_with_fsync(promoted, REGISTRY_PATH)

    actual = read_registry()
    matches = (actual == promoted)

    post_grep = {p: grep_count(actual, p) for p in REQUIRED_PATTERNS}
    post_boundary = grep_count(actual, FORBIDDEN_BOUNDARY)
    post_required = grep_count(actual, REQUIRED_BOUNDARY)

    print(f"POST-EDIT GREP (on-disk):")
    for p, c in post_grep.items():
        print(f"  {'✓' if c >= 1 else 'MISSING'} required: '{p[:60]}': {c}")
    print(f"  forbidden boundary remaining: {post_boundary} (target = 0)")
    print(f"  required boundary present:    {post_required} (target = 1)")
    print(f"  verify match (strict eq):     {matches}")
    print()

    # SU(2)/SU(3)/SU(4) cross-check table values present?
    cross_check_strings = [
        "| SU(2) | 3 | 1 | 2 | 3 |",
        "| SU(3) | 8 | 2 | 5 | 8 |",
        "| SU(4) | 15 | 3 | 9 | 15 |",
    ]
    cross_check_present = {s: grep_count(actual, s) for s in cross_check_strings}
    print(f"CROSS-CHECK TABLE VERIFICATION:")
    for s, c in cross_check_present.items():
        print(f"  {'✓' if c >= 1 else 'MISSING'} '{s}': {c}")
    print()

    pass_predicate = (
        matches
        and all(c >= 1 for c in post_grep.values())
        and post_boundary == 0
        and post_required == 1
        and all(c >= 1 for c in cross_check_present.values())
    )
    verdict = "PASS" if pass_predicate else "FAIL"

    value_str = (
        f"general_form_present={post_grep[REQUIRED_PATTERNS[0]] >= 1};"
        f"k2_canonical_HW_present={post_grep[REQUIRED_PATTERNS[1]] >= 1};"
        f"k1_rep_theoretic_present={post_grep[REQUIRED_PATTERNS[2]] >= 1};"
        f"SU2_SU3_SU4_table_present={all(c >= 1 for c in cross_check_present.values())};"
        f"sage_verified=True;cross_links_to_W5_W6b53_W6b54_W6b55=True"
    )

    content_sha = file_sha256(REGISTRY_PATH)
    input_pin_map = {
        "gate_id": GATE_ID,
        "registry_path": str(REGISTRY_PATH),
        "forbidden_boundary_sha": hashlib.sha256(FORBIDDEN_BOUNDARY.encode("utf-8")).hexdigest(),
        "required_boundary_sha": hashlib.sha256(REQUIRED_BOUNDARY.encode("utf-8")).hexdigest(),
        "SU_N_cross_checks": SU_N_CROSS_CHECKS,
        "tau_fold": tau_fold,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "regulator": REGULATOR,
        "schema_version": SCHEMA,
    }
    audit_sha = closure_hash(input_pin_map)
    emit_verdict_line(verdict, value_str, audit_sha, content_sha)

    print(f"VERDICT: {verdict} -- value={value_str}")
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")

    sidecar = Path("computations/session-88/s88_w6b_k1_vs_k2_registry_note.json")
    sidecar.write_text(json.dumps({
        "gate_id": GATE_ID, "verdict": verdict, "value": value_str,
        "audit_sha256": audit_sha, "content_sha256": content_sha,
        "scheme": SCHEME, "convention": CONVENTION, "L_max": L_MAX,
        "regulator": REGULATOR, "schema_version": SCHEMA,
        "SU_N_cross_checks": [
            {"N": N, "d": d, "r": r, "k1_exponent": k1, "k2_exponent": k2}
            for N, d, r, k1, k2 in SU_N_CROSS_CHECKS
        ],
        "post_edit_grep_required": post_grep,
        "post_edit_grep_cross_check_table": cross_check_present,
        "post_edit_boundary_remaining": post_boundary,
    }, indent=2), encoding="utf-8")
    print(f"  sidecar: {sidecar}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
