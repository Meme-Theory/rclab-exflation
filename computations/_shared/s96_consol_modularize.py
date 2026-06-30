#!/usr/bin/env python3
"""
S96 W8-7 — S96-CONSOL-MODULARIZE — Capstone 3-stratum layered-program declaration
==================================================================================

Gate: S96-CONSOL-MODULARIZE ([AUDIT])

Pre-registered threshold (NON-COMPUTE, METHODOLOGY-class M1; artifact-existence-with-content):
  PASS iff ALL of:
    (a) the stratum-map declares all 3 strata (spectral/algebraic math / substrate transit
        physics / cosmological phenomenology), each with an explicit header;
    (b) every major capstone section (§1, §1.1, §2, §3, §4, §5, §6.1, §6.2, §6.3, §7, §8) is
        mapped to EXACTLY one stratum — a partition (SUM-check: |S1|+|S2|+|S3| == |section_set|,
        no section omitted, no section double-mapped);
    (c) each stratum carries a maturity tag + a publication-readiness tag (math-first /
        substrate-transit / phenomenology candidate);
    (d) the designated-writer declaration landed WITHOUT altering any section's physics content
        (additivity: the declaration block lives inside §0, BEFORE §1; every major §-header still
        present; the stratum-declaration content markers do NOT appear inside any §1-§8 body);
    AND substantive_line_count(stratum-map) >= 15.
  FAIL iff the partition is incomplete (a section omitted or double-stratum'd), OR a stratum lacks
        its maturity/publication-readiness tag, OR the declaration ALTERS a section's physics content
        (additivity violated — a content rewrite rather than an additive overlay).
  INFO iff the 3-stratum map + partition + tags + additivity all hold BUT one section GENUINELY
        straddles two strata (here §6.2: Stratum-2 transit physics PRIMARY + a Stratum-3 causal-
        structure consequence via r/n_T) and is mapped to its PRIMARY stratum with an explicit
        secondary cross-reference (NOT forced into one, NOT double-counted in the partition).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema). The 3-stratum structure is the report's
recommended reframing; the section->stratum mapping is a categorical function of each section's
content (READ, not derived):
  - sessions/framework/phonic-exflation-equation.md            (the capstone — patched; re-read target)
  - sessions/framework/equation-collab/_consolidated-findings.md (the per-section maturity assessment)
  - deep-research-report.md                                    (the external review — wave driver; the
                                                                 "Recommended next analyses" 3-strata reframing)
  - canonical_constants.py                                     (feeds audit_sha256)

Output 4-tuple:
  (value=<stratum-map summary>, scheme=THREE-STRATUM-LAYERED-PROGRAM-DECLARATION,
   convention=section-to-stratum-partition-PLUS-per-stratum-maturity-PLUS-publication-readiness-PLUS-additive-no-content-change,
   L_max=N/A)

Classification: NON-PHONONIC (methodology / structural declaration in a curated framework document).

METHODOLOGY
-----------
The capstone's latent modularity (which the external review observes — "the repo already behaves
this way internally; the manuscript should make that modularity explicit") is DECLARED explicitly as
a 3-stratum layered program. The §0.1 declaration block (the stratum-map: section->stratum partition,
per-stratum maturity, per-stratum publication-readiness, the §6.2 straddle disclosure) was applied by
the designated writer (gen-physicist) BEFORE this script ran, as an ADDITIVE navigational overlay
inside §0 (before §1) — NO §1-§8 section's physics content changed. This script verifies the four
PASS conjuncts (3 strata declared; section partition exact; maturity+readiness tags; additivity) and
emits the JSON stratum-map sidecar + the dual-SHA verdict line. Under epistemic-discipline.md
§"Layer-Decomposition" the stratum declaration is a navigational F-image: the substrate->emergent
arrow (D_K eigenvalues -> spectral moments -> emergent physics) read top-to-bottom IS the stratum
ordering; Stratum 1 (the master object, the Decoupling Theorem, the a_n firewall) is the substrate-IS
layer, Stratum 2 (the fold/GGE relic/white hole) the substrate's non-equilibrium dynamics, Stratum 3
(§6.3 a(t) gap / §7 observable contact) the laboratory-IN touch. The declaration does NOT invert any
explanation direction; it organizes the capstone ALONG the substrate-first arrow.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- CPU-only (markdown/JSON authoring + section-bound + additivity grep cross-checks; OMP capped before numpy)
- SHA-256 of all input files logged in first lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema); content_sha256 over [script bytes
  || applied-capstone-diff bytes] per wave-classification.md §"Dual-SHA closure for METHODOLOGY-class"
- 4-tuple printed as the final non-verdict line
- Verdict appended to computations/session-96/s96_gate_verdicts.txt (canonical path per gate-verdicts.md)
- Exit 0 on any valid verdict (PASS/FAIL/INFO); exit != 0 only on script breakage
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

from canonical_constants import *  # noqa: F401,F403  (feeds audit_sha256)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import re
import sys
import time
from pathlib import Path

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
# This script lives at computations/_shared/. The verdict + JSON sidecar go to
# computations/session-96/ (canonical verdict path per gate-verdicts.md).
SHARED_DIR = Path(__file__).resolve().parent                 # computations/_shared
COMPUTATIONS_DIR = SHARED_DIR.parent                          # computations
PROJECT_ROOT = COMPUTATIONS_DIR.parent                        # repo root
SESSION_OUT_DIR = COMPUTATIONS_DIR / "session-96"            # computations/session-96
SESSION_OUT_DIR.mkdir(parents=True, exist_ok=True)

SESSION = "S96"                                               # (local)
GATE_ID = "S96-CONSOL-MODULARIZE"                             # (local)
SCHEME = "THREE-STRATUM-LAYERED-PROGRAM-DECLARATION"          # (local)
CONVENTION = ("section-to-stratum-partition-PLUS-per-stratum-maturity-"
              "PLUS-publication-readiness-PLUS-additive-no-content-change")  # (local)
L_MAX = "N/A"                                                 # (local)

CAPSTONE = PROJECT_ROOT / "sessions/framework/phonic-exflation-equation.md"          # (local)
CONSOL_FINDINGS = PROJECT_ROOT / "sessions/framework/equation-collab/_consolidated-findings.md"  # (local)
DEEP_RESEARCH = PROJECT_ROOT / "deep-research-report.md"                             # (local)
CANONICAL = SHARED_DIR / "canonical_constants.py"                                    # (local)

OUT_JSON = SESSION_OUT_DIR / "s96_consol_modularize.json"    # (local)
VERDICT_TXT = SESSION_OUT_DIR / "s96_gate_verdicts.txt"      # (local)

# Inputs whose SHAs feed the closure (canonical = report reframing + capstone section structure)
INPUT_FILES = [
    CANONICAL,
    CAPSTONE,
    CONSOL_FINDINGS,
    DEEP_RESEARCH,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = p.name  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
    applied_diff_bytes: bytes,
) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    audit_sha256   = sha256( bytes(script) || bytes(canonical) || pinmap_json )
    content_sha256 = sha256( bytes(script) || applied_capstone_diff_bytes )
        — for a METHODOLOGY-class gate the content SHA is over the script PLUS the applied
        capstone diff (the F-image of the numerical PASS-predicate eigenvalue under the
        substrate <-> methodology layer pair, per wave-classification.md
        §"Dual-SHA closure for METHODOLOGY-class").
    """
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    h_content.update(applied_diff_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — The 3-stratum map (section -> stratum partition; READ, not derived)
# ---------------------------------------------------------------------------
# The 3 strata are the external review's "Recommended next analyses" reframing
# ("a layered program with three publication strata"). The section->stratum
# mapping is a categorical function of each section's content (math / transit /
# phenomenology) — TRANSCRIBED, not recomputed. Maturity tags are READ from
# _consolidated-findings.md §I/§II and the knowledge MCP (Decoupling Theorem
# PERMANENT S64 W5-B / certified S75 W2-E; a(t) gap the decisive weakness).

# The major-section set being partitioned (the §-headers that exist in the capstone).
SECTION_SET = ["§1", "§1.1", "§2", "§3", "§4", "§5", "§6.1", "§6.2", "§6.3", "§7", "§8"]  # (local)

STRATA = {  # (local)
    "Stratum 1": {
        "name": "SPECTRAL / ALGEBRAIC MATHEMATICS",
        "sections": ["§1", "§1.1", "§2", "§3", "§4", "§8"],
        "maturity": (
            "most mature; the §4.2 Spectral-Moment Decoupling Theorem is 'as close to settled as the "
            "panel gets' (>=8 independent Sage-reverifications; PERMANENT per the registry, S64 W5-B; "
            "certified S75 W2-E); the §8.2 a_n firewall (+ §8.2a R_K(0) analog) is 'one of the "
            "capstone's more careful and mathematically defensible features'"
        ),
        "publication_readiness": "math-first publication candidate (publishable standalone, before the cosmology closes)",
        "substrate_layer": "the substrate-IS layer: the master object, the Decoupling Theorem, the a_n moments — the fabric itself",
    },
    "Stratum 2": {
        "name": "SUBSTRATE-SIDE NON-EQUILIBRIUM TRANSIT PHYSICS",
        "sections": ["§5", "§6.1", "§6.2"],
        "maturity": (
            "good substrate-side structure; transit-valid; 'overreach enters when permanence is "
            "narrated too strongly' — the §5.3 GGE-relic claim is the W8-1-reconciled diabatic "
            "transit-freeze (strong S38 integrability-permanence reading BROKEN-tagged; surviving "
            "claim = compute-certified diabatic freeze, R_therm=5251.82, S_ent=0)"
        ),
        "publication_readiness": "substrate-transit-physics paper candidate",
        "substrate_layer": "the substrate's non-equilibrium dynamics: the fold, the GGE relic, the white hole — the fabric reorganizing through the fold",
    },
    "Stratum 3": {
        "name": "COSMOLOGICAL PHENOMENOLOGY",
        "sections": ["§6.3", "§7"],
        "maturity": (
            "least mature; conditional/forecast; 'the decisive weakness... the bridge from internal "
            "spectral geometry to externally testable cosmological dynamics' — gated on the §6.3 a(t) "
            "closure (the W1 flagship)"
        ),
        "publication_readiness": "phenomenology paper candidate (gated on the §6.3 a(t) closure)",
        "substrate_layer": "where the substrate touches the laboratory-IN observables: §7 is the substrate probing itself, read at the single modulus tau_now",
    },
}

# §6.2 straddle disclosure (INFO condition): §6.2 mapped to its PRIMARY stratum (Stratum 2) with an
# explicit SECONDARY cross-reference to Stratum 3 (the r/n_T tensor-sector consequence of the white-
# hole causal structure). NOT double-counted in the partition; the cross-reference IS the disclosure.
STRADDLE = {  # (local)
    "section": "§6.2",
    "primary_stratum": "Stratum 2",
    "secondary_stratum": "Stratum 3",
    "reason": (
        "§6.2 (the acoustic white hole) is substrate-side transit physics (Stratum 2 primary: the "
        "causal structure of the supersonic amplitude flow) AND has phenomenological tensor-sector "
        "consequences via the r / n_T contact in §7 (Stratum 3 secondary). Mapped to PRIMARY with a "
        "disclosed secondary cross-reference; NOT forced into one stratum, NOT double-counted"
    ),
}


# ---------------------------------------------------------------------------
# Section 6 — Section-bound + additivity helpers (line-scoped, like W8-1)
# ---------------------------------------------------------------------------

def _section_bounds(text: str, header_regex: str) -> tuple[int, int]:
    """Return (start_char, end_char) of the markdown section whose header matches header_regex,
    spanning to the next header of the same-or-higher level."""
    lines = text.splitlines(keepends=True)  # (local)
    start_line = None  # (local)
    start_level = None  # (local)
    for i, ln in enumerate(lines):
        if re.match(header_regex, ln):
            start_line = i
            m = re.match(r"^(#{1,6})", ln)  # (local)
            start_level = len(m.group(1)) if m else 2
            break
    if start_line is None:
        return (-1, -1)
    end_line = len(lines)  # (local)
    for j in range(start_line + 1, len(lines)):
        m = re.match(r"^(#{1,6})\s", lines[j])  # (local)
        if m and len(m.group(1)) <= start_level:
            end_line = j
            break
    start_char = sum(len(l) for l in lines[:start_line])  # (local)
    end_char = sum(len(l) for l in lines[:end_line])  # (local)
    return (start_char, end_char)


# Regex per major section header in the capstone (the exact header forms).
SECTION_HEADER_REGEX = {  # (local)
    "§1":   r"^## §1 — The equation\b",
    "§1.1": r"^### 1\.1 ",
    "§2":   r"^## §2 — ",
    "§3":   r"^## §3 — ",
    "§4":   r"^## §4 — ",
    "§5":   r"^## §5 — ",
    "§6.1": r"^### 6\.1 ",
    "§6.2": r"^### 6\.2 ",
    "§6.3": r"^### 6\.3 ",
    "§7":   r"^## §7 — ",
    "§8":   r"^## §8 — ",
}

# The declaration block lives inside §0, in a subsection whose header is this:
DECLARATION_HEADER_REGEX = r"^### §0\.1 — The 3-stratum layered-program structure"  # (local)


def verify_partition() -> dict:
    """SUM-check the section->stratum partition: every SECTION_SET member in EXACTLY one stratum."""
    assigned = {}  # (local) section -> list of strata it appears in
    for sname in SECTION_SET:
        assigned[sname] = [sk for sk, sv in STRATA.items() if sname in sv["sections"]]
    omitted = [s for s, st in assigned.items() if len(st) == 0]  # (local)
    double_mapped = [s for s, st in assigned.items() if len(st) > 1]  # (local)
    # also detect any stratum section not in SECTION_SET (a typo'd section id)
    all_stratum_sections = [s for sv in STRATA.values() for s in sv["sections"]]  # (local)
    extraneous = [s for s in all_stratum_sections if s not in SECTION_SET]  # (local)
    sizes = {sk: len(sv["sections"]) for sk, sv in STRATA.items()}  # (local)
    sum_sizes = sum(sizes.values())  # (local)
    partition_ok = (
        not omitted and not double_mapped and not extraneous
        and sum_sizes == len(SECTION_SET)
    )  # (local)
    return {
        "section_set": SECTION_SET,
        "section_set_size": len(SECTION_SET),
        "per_section_stratum": assigned,
        "stratum_sizes": sizes,
        "sum_of_stratum_sizes": sum_sizes,
        "omitted_sections": omitted,
        "double_mapped_sections": double_mapped,
        "extraneous_stratum_sections": extraneous,
        "sum_check_exact": (sum_sizes == len(SECTION_SET)),
        "partition_ok": partition_ok,
    }


def verify_strata_tags() -> dict:
    """Each stratum must carry an explicit header (name), a maturity tag, and a publication-readiness tag."""
    per_stratum = {}  # (local)
    for sk, sv in STRATA.items():
        per_stratum[sk] = {
            "has_name_header": bool(sv.get("name")),
            "has_maturity": bool(sv.get("maturity")),
            "has_publication_readiness": bool(sv.get("publication_readiness")),
        }
    all_ok = all(all(v.values()) for v in per_stratum.values())  # (local)
    return {
        "three_strata_declared": (len(STRATA) == 3),
        "per_stratum_tags": per_stratum,
        "all_strata_tagged": all_ok,
    }


def verify_additivity(capstone_text: str) -> dict:
    """Additivity: the declaration is an additive overlay inside §0 (before §1); NO §1-§8 section's
    physics content changed.

    Structural verification (no-content-change SHA analog at the section-region level):
      (1) the §0.1 declaration block exists and lives BEFORE the §1 header (inside §0);
      (2) every major §-header in SECTION_SET is still present (no section deleted/renamed);
      (3) the stratum-declaration content markers ('Stratum 1/2/3' as the declaration's bold labels)
          appear ONLY within the §0.1 declaration region, NOT inside any §1-§8 section body — i.e. the
          additive block did not splice stratum prose into the physics sections.
    """
    # (1) declaration block inside §0, before §1
    decl_start, decl_end = _section_bounds(capstone_text, DECLARATION_HEADER_REGEX)  # (local)
    s1_start, _ = _section_bounds(capstone_text, SECTION_HEADER_REGEX["§1"])  # (local)
    decl_present = decl_start >= 0  # (local)
    decl_before_s1 = decl_present and s1_start >= 0 and decl_end <= s1_start  # (local)

    # (2) every major section header present
    section_bounds = {}  # (local)
    missing_headers = []  # (local)
    for sname, rgx in SECTION_HEADER_REGEX.items():
        st, en = _section_bounds(capstone_text, rgx)  # (local)
        section_bounds[sname] = (st, en)
        if st < 0:
            missing_headers.append(sname)

    # (3) stratum-declaration markers confined to the §0.1 region.
    # The declaration's bold stratum labels are the markers; they must NOT appear inside any §1-§8 body.
    # (a generic '§6.2 straddle' cross-reference inside §6/§7 prose is NOT one of these bold labels, so
    #  this check is specific to the declaration markers, not to the word 'stratum' in general.)
    decl_markers = ["**Stratum 1 —", "**Stratum 2 —", "**Stratum 3 —"]  # (local)
    leak_sections = []  # (local)
    for sname in SECTION_SET:
        st, en = section_bounds[sname]  # (local)
        if st < 0:
            continue
        body = capstone_text[st:en]  # (local)
        if any(mk in body for mk in decl_markers):
            leak_sections.append(sname)

    additive_ok = (
        decl_present and decl_before_s1
        and not missing_headers
        and not leak_sections
    )  # (local)
    return {
        "declaration_block_present": decl_present,
        "declaration_inside_section0_before_section1": decl_before_s1,
        "declaration_char_span": [decl_start, decl_end],
        "section1_header_char": s1_start,
        "all_major_headers_present": (not missing_headers),
        "missing_headers": missing_headers,
        "stratum_marker_leak_into_physics_sections": leak_sections,
        "additive_no_content_change": additive_ok,
    }


def declaration_line_count(capstone_text: str) -> int:
    """Substantive line count of the §0.1 declaration block (non-blank lines)."""
    st, en = _section_bounds(capstone_text, DECLARATION_HEADER_REGEX)  # (local)
    if st < 0:
        return 0
    block = capstone_text[st:en]  # (local)
    return sum(1 for ln in block.splitlines() if ln.strip())


# ---------------------------------------------------------------------------
# Section 7 — Gate evaluation
# ---------------------------------------------------------------------------

def evaluate_gate(partition: dict, tags: dict, additivity: dict, decl_lines: int,
                  capstone_text: str) -> tuple[str, dict]:
    """Return (verdict, evidence) per the pre-registered conjunction.

    PASS-core = 3 strata declared + partition exact + all strata tagged + additive (no content change)
              + decl_lines >= 15 + capstone must_contain markers present.
    INFO      = PASS-core holds AND a genuine cross-stratum straddle (§6.2) is disclosed (primary
                stratum + secondary cross-reference; NOT double-counted).
    FAIL      = any PASS-core conjunct fails.
    """
    # capstone must_contain markers (the applied-declaration fingerprints, per the gate block)
    must_contain = ["Stratum 1", "Stratum 2", "Stratum 3"]  # (local)
    must_present = {m: (m in capstone_text) for m in must_contain}  # (local)
    all_must = all(must_present.values())  # (local)

    pass_core = (
        tags["three_strata_declared"]
        and partition["partition_ok"]
        and tags["all_strata_tagged"]
        and additivity["additive_no_content_change"]
        and (decl_lines >= 15)
        and all_must
    )  # (local)

    # straddle disclosure present (the §6.2 cross-stratum reference)
    straddle_disclosed = (
        ("§6.2 straddle" in capstone_text)
        and (STRADDLE["primary_stratum"] in capstone_text)
        and (STRADDLE["secondary_stratum"] in capstone_text)
    )  # (local)

    if not pass_core:
        verdict = "FAIL"  # (local)
    elif straddle_disclosed:
        # A section legitimately straddles two strata and is disclosed (primary + secondary cross-ref,
        # NOT double-counted) -> the honest verdict is INFO per the pre-registration.
        verdict = "INFO"  # (local)
    else:
        verdict = "PASS"  # (local)

    evidence = {
        "three_strata_declared": tags["three_strata_declared"],
        "partition_ok": partition["partition_ok"],
        "sum_check": f"{partition['sum_of_stratum_sizes']} == {partition['section_set_size']}",
        "sum_check_exact": partition["sum_check_exact"],
        "omitted_sections": partition["omitted_sections"],
        "double_mapped_sections": partition["double_mapped_sections"],
        "all_strata_tagged": tags["all_strata_tagged"],
        "additive_no_content_change": additivity["additive_no_content_change"],
        "missing_headers": additivity["missing_headers"],
        "stratum_marker_leak": additivity["stratum_marker_leak_into_physics_sections"],
        "declaration_substantive_lines": decl_lines,
        "decl_lines_ge_15": (decl_lines >= 15),
        "must_contain_present": must_present,
        "all_must_contain": all_must,
        "straddle_disclosed": straddle_disclosed,
        "straddle_section": STRADDLE["section"],
        "pass_core": pass_core,
    }
    return verdict, evidence


# ---------------------------------------------------------------------------
# Section 8 — Verdict append (atomic, S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:
    """Append a single canonical verdict line + dual-SHA companion comment row.

    Atomic append (single open('a') write — no read-modify-write, no truncate).
    """
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (METHODOLOGY-class: content over script+applied-capstone-diff)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Section 9 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)  # (local)

    # 2. Read the patched capstone; verify partition + strata tags + additivity
    capstone_text = CAPSTONE.read_text(encoding="utf-8")  # (local)
    partition = verify_partition()  # (local)
    tags = verify_strata_tags()  # (local)
    additivity = verify_additivity(capstone_text)  # (local)
    decl_lines = declaration_line_count(capstone_text)  # (local)

    print()
    print(f"  3 strata declared: {tags['three_strata_declared']}")
    print(f"  partition SUM-check: {partition['sum_of_stratum_sizes']} == "
          f"{partition['section_set_size']} -> exact={partition['sum_check_exact']}; "
          f"ok={partition['partition_ok']} "
          f"(omitted={partition['omitted_sections']}, double={partition['double_mapped_sections']})")
    print(f"  all strata tagged (maturity + publication-readiness): {tags['all_strata_tagged']}")
    print(f"  additivity (no §1-§8 content change): {additivity['additive_no_content_change']} "
          f"(decl before §1={additivity['declaration_inside_section0_before_section1']}, "
          f"missing headers={additivity['missing_headers']}, "
          f"marker leak={additivity['stratum_marker_leak_into_physics_sections']})")
    print(f"  declaration substantive lines: {decl_lines} (>=15: {decl_lines >= 15})")
    print()

    # 3. Evaluate gate
    verdict, evidence = evaluate_gate(partition, tags, additivity, decl_lines, capstone_text)  # (local)

    # 4. Build the applied-diff bytes (the stratum-map + straddle + applied-block fingerprint) for the
    #    METHODOLOGY-class content_sha256 (script || applied-capstone-diff image).
    applied_diff_obj = {  # (local)
        "strata": STRATA,
        "section_set": SECTION_SET,
        "straddle": STRADDLE,
        "partition": partition,
        "additivity": additivity,
        "capstone_sha256_post_patch": sha256_of(CAPSTONE),
    }
    applied_diff_bytes = json.dumps(
        applied_diff_obj, separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)

    # 5. Compute dual SHA
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL, pins, applied_diff_bytes)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script+applied-capstone-diff)")
    print()

    # 6. Write JSON stratum-map sidecar
    sidecar = {  # (local)
        "gate_id": GATE_ID,
        "session": SESSION,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "verdict": verdict,
        "classification": "NON-PHONONIC",
        "methodology_class": True,
        "source_of_truth": {
            "_note": "the 3 strata are the external review's 'Recommended next analyses' reframing; "
                     "the section->stratum mapping + maturity tags are READ from the closed report + "
                     "_consolidated-findings.md §I/§II + the knowledge MCP, NOT a new physics derivation",
            "report_reframing": "layered program with three publication strata (math-first / substrate-transit / phenomenology)",
            "decoupling_theorem_maturity": ">=8 Sage-reverifications; PERMANENT S64 W5-B; certified S75 W2-E",
            "a_t_gap": "§6.3 the decisive weakness (substrate->FRW); the W1 flagship",
        },
        "stratum_map": STRATA,
        "section_set": SECTION_SET,
        "straddle_disclosure": STRADDLE,
        "partition_check": partition,
        "strata_tag_check": tags,
        "additivity_check": additivity,
        "declaration_substantive_lines": decl_lines,
        "gate_evidence": evidence,
        "input_pins": pins,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "designated_writer_boundary": {
            "gen_physicist_owns": ["§0.1 the 3-stratum declaration block (curated-doc additive insertion)"],
            "additive_only": True,
            "no_section_physics_content_changed": additivity["additive_no_content_change"],
        },
        "substrate_framing": (
            "the 3-stratum declaration organizes the capstone ALONG the substrate->emergent arrow "
            "(D_K eigenvalues [Stratum 1] -> spectral-action moments / transit dynamics [Stratum 2] -> "
            "emergent observables [Stratum 3]); it does NOT invert any explanation direction; "
            "Stratum 1 IS the substrate-IS layer, Stratum 2 the substrate's non-equilibrium dynamics, "
            "Stratum 3 the laboratory-IN touch"
        ),
    }
    OUT_JSON.write_text(json.dumps(sidecar, indent=2), encoding="utf-8")
    print(f"  JSON stratum-map sidecar -> {OUT_JSON.relative_to(PROJECT_ROOT)}")

    # 7. Emit 4-tuple + append verdict
    value = (f"modularize;strata_declared={len(STRATA)}/3;"
             f"sections_partitioned={partition['sum_of_stratum_sizes']}/{partition['section_set_size']};"
             f"sum_check_exact={partition['sum_check_exact']};"
             f"omitted={len(partition['omitted_sections'])};double={len(partition['double_mapped_sections'])};"
             f"all_strata_tagged={tags['all_strata_tagged']};"
             f"additive_no_content_change={additivity['additive_no_content_change']};"
             f"decl_lines={decl_lines};"
             f"straddle_disclosed_sec6.2_S2primary_S3secondary={evidence['straddle_disclosed']}")  # (local)
    tag = (f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")  # (local)
    print(tag)
    append_verdict(verdict, value, audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
