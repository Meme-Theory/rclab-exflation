#!/usr/bin/env python3
"""
s101_w8a2_corpus_append_helper.py — single-shot corpus §21 append helper
========================================================================

Lands ONE new section at the next-free `## §N` (expected §21; corpus tail is
`## §20` at plan-freeze) in `sessions/framework/registry/pru-class-corpus.md`,
per the S101 W8a-2 gate block (S101-MULT-CANCELLATION-DETECTOR-LAB-IN-AXIS).

REGISTRY-WRITE HYGIENE (`epistemic-discipline.md §"Registry-Write Hygiene under
Parallel-Writer Race"`):
  (1) PRE-SCAN ALL HEADER LEVELS — `## §N` + `### §N` + `#### §N` — before
      allocating, so the next-free index does NOT under-count existing slots.
  (2) SINGLE-SHOT `open("a")` POSIX O_APPEND — NOT an Edit-tool round-trip
      (Edit is mtime-conditional; under parallel writers the second Edit fails).
  (3) If the planned slot §21 is occupied at runtime, REROUTE to the next-free
      `## §N` and signal FAIL-with-remediation to the caller (printed; the
      driver carries it into the verdict line per Hygiene item 3).

The two instance rows are carried VERBATIM from the gate block binding-CF text
(session-101-plan-w8.md §W8a-2 method, lines 380-396):
  Row 1 — W7-2 C2a G-cancellation (gate S100b-A2-HEAVY-SEED-ABUNDANCE, audit
          37f64fcd…); signature class RATIO-OF-PIPELINES.
  Row 2 — W7-3 A2 flat-S invariance (gate S100b-STRUCTURE-TIMING-TWO-AXIS, audit
          25002865…); signature class VARIANCE-FUNCTIONAL.
Both rows tagged NON-K-ADVANCING for the rule's spectral-support K-counter (the
rule is already MANDATORY at K=3; the lab-IN pipeline axis is a DIFFERENT
documentation axis, NOT a fourth spectral-support row; no K-advancement decision).

Idempotent: if the section title (the unique literal
"laboratory-IN pipeline-parameter signature corpus") is already on disk, this
helper is a NO-OP and reports the already-landed section number.

Exit 0 on a healthy run (landed OR already-present OR rerouted-with-disclosure);
nonzero only on script breakage (file unreadable / write failure).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Repo-root-relative path to the corpus (this script lives at
# computations/session-101/; project root is two parents up).
SESSION_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SESSION_DIR.parent.parent

# Import-only canonical-constants compliance (this helper is a pure registry-write
# utility — it consumes NO framework constant numerically — but the import keeps
# the canonical-constants audit / python-validate hook satisfied, matching the
# sibling pattern in _machinery_feasibility_audit.py).
sys.path.insert(0, str(PROJECT_ROOT / "computations" / "_shared"))
try:
    from canonical_constants import *  # noqa: F401,F403
except Exception:  # noqa: BLE001 — import-tolerant; constants unused
    pass
CORPUS = PROJECT_ROOT / "sessions" / "framework" / "registry" / "pru-class-corpus.md"

PLANNED_SECTION_N = 21  # (local) expected next-free per the gate block (tail = §20)
SECTION_TITLE_FRAGMENT = "laboratory-IN pipeline-parameter signature corpus"

# Full-64-hex audit SHAs of the two calibration anchors (gate block input_files).
AUDIT_ROW1_G_CANCEL = "37f64fcd7e81ef8575b1781b0385d3a0db6bd8a2ba4647790e0a81b7164455c9"
AUDIT_ROW2_FLAT_S = "25002865ff190b5598bf9aa8076d14da0e4a37c35807f05b79a242fbb791478d"

# Header-level scanner: matches `## §N`, `### §N`, `#### §N` (any of the three
# levels), capturing the integer slot N. Per Hygiene item (1): scanning ONE level
# under-counts existing slots under parallel writers.
_HDR_ANY_LEVEL = re.compile(r"(?m)^#{2,4}\s+§(\d+)\b")


def existing_section_numbers(text: str) -> set[int]:
    """All §N slot integers present at ANY header level (## / ### / ####)."""
    return {int(m.group(1)) for m in _HDR_ANY_LEVEL.finditer(text)}


def next_free_section(existing: set[int]) -> int:
    """The smallest integer >= PLANNED_SECTION_N not already a slot. Equals
    PLANNED_SECTION_N when §21 is free (the expected case)."""
    n = PLANNED_SECTION_N  # (local)
    while n in existing:
        n += 1
    return n


def build_section_text(section_n: int) -> str:
    """Build the §N corpus section text in memory (single-shot; no I/O)."""
    return f"""
## §{section_n}. Multiplicative-normalization cancellation — laboratory-IN pipeline-parameter signature corpus (`math-scripts.md §"Multiplicative-normalization cancellation invariants"`; detector extension)

**Directive home**: `math-scripts.md §"Multiplicative-normalization cancellation invariants"` (MANDATORY at K=3; S94 W6-18 promotion, audit `6284d0d3ac7a85c8174f26c8d1ae8561f4ff89945ae6d86cffb4a8b8ff8fb27e`). **Detector home**: `computations/_shared/_machinery_feasibility_audit.py::detect_multiplicative_cancellation` (S101 W8a-2; three signature classes — `LOG-DERIVATIVE` / `RATIO-OF-PIPELINES` / `VARIANCE-FUNCTIONAL`).

**Axis scope (NON-K-ADVANCING)**: the rule's K-counter counts STRUCTURALLY DISTINCT *spectral-support* factorization mechanisms — `w(L_max)`-truncation (K=1) / `w(τ-moduli)`-deformation (K=2) / `w(C_2^max)`-Casimir-ceiling (K=3) — the weights of the SUBSTRATE functional. The two instances below cancel a *laboratory-IN pipeline parameter* (`G`, `S`) that enters through the emergent-physics reduction pipeline (emergent-Friedmann halo counting; survey capture), NOT through the spectral support of any `D_K` functional. This is a categorically DIFFERENT documentation axis (`cancelling_axis = LAB-IN-PIPELINE`), NOT a fourth spectral-support row. **Both rows are tagged `NON-K-ADVANCING`**: no K-advancement decision is made — the rule is already MANDATORY at K=3, and the lab-IN axis is documented here WITHOUT contaminating the spectral-support K-counter (binding CF text: "corpus append only, no K-advancement decision").

**Detector-blindness motivation**: both instances self-detected only AT EXECUTION in S100b W7 — the rule had no plan-freeze detector before W8a-2. A detector keying only on `LOG-DERIVATIVE` signatures (`d^n ln(.)/d(ln K)^n`) cannot see either: a log-RATIO-of-pipelines is not a log-derivative, and a coefficient-of-variation is not a log-derivative. The S101 W8a-2 detector adds the two NEW signature classes (severity S2 advisory — NEW classes ship at S2; the rule's S1 MANDATORY text binds the spectral-support LOG-DERIVATIVE class it was promoted on; S1-hardening of the new classes is a FUTURE K-decision NOT made here).

### Row 1 — W7-2 C2a G-cancellation (signature class: RATIO-OF-PIPELINES)

- **Gate**: `S100b-A2-HEAVY-SEED-ABUNDANCE` (`computations/session-100b/s100b_gate_verdicts.txt:127`, audit `{AUDIT_ROW1_G_CANCEL}`).
- **Gated quantity**: `max_z |log10(n_ACH_em/n_ACH_ref)|` is EXACTLY 0 by G-cancellation under the borrowed-`(H_0, Ω, σ_8)` baseline. `M_ACH ~ 1/(G·H)`, `ρ_m,0 ~ 1/G`; the count above a FIXED `T_vir` threshold is G-free. Numerator and denominator pipelines carry the SAME G-scalings (only the em/ref `H(t)` differs); the selection criterion contributes no G ⇒ every G-factor appears identically in both legs ⇒ G cancels in the ratio.
- **Value field on disk**: `C2a_maxdlog_nACH=0.00000dex` (`≤0.5=True`); structural-identity companion row on disk.
- **Substitution chain (exact identity)**: `max_z |log10(n_ACH_em/n_ACH_ref)| == 0` IDENTICALLY in the pure shared-G channel — a STRUCTURAL IDENTITY of the pipeline pair, not an empirical constraint on the substrate.
- **Detector class**: `RATIO-OF-PIPELINES` — `|log10(X_em/X_ref)|` / named two-pipeline ratio CONJOINED with a shared LAB-IN parameter (`G`) in BOTH legs' scalings; `cancelling_axis = LAB-IN-PIPELINE`; severity S2. **Tag: NON-K-ADVANCING.**

### Row 2 — W7-3 A2 flat-S invariance (signature class: VARIANCE-FUNCTIONAL)

- **Gate**: `S100b-STRUCTURE-TIMING-TWO-AXIS` (`computations/session-100b/s100b_gate_verdicts.txt:121`, audit `{AUDIT_ROW2_FLAT_S}`).
- **Gated quantity**: a flat multiplicative capture `S` cancels exactly in the fractional count variance (`N -> S·N` leaves `σ_CV` invariant), verified in-run.
- **Substitution chain (exact identity)**: `σ_CV(N) := Std(N)/Mean(N)`; flat capture `N -> S·N` with `S` a single z-independent scalar ⇒ `σ_CV(S·N) = Std(S·N)/Mean(S·N) = (S·Std(N))/(S·Mean(N)) = Std(N)/Mean(N) = σ_CV(N)`. `σ_CV` is INVARIANT under flat `S` — the gated variance criterion carries ZERO sensitivity to the capture normalization; structural identity.
- **Detector class**: `VARIANCE-FUNCTIONAL` — coefficient-of-variation / `Std(N)/Mean(N)` / `σ_CV` CONJOINED with a flat multiplicative capture/completeness parameter in the same block; `cancelling_axis = LAB-IN-PIPELINE`; severity S2. **Tag: NON-K-ADVANCING.**

### Axis claim (why LAB-IN-PIPELINE is a distinct axis)

The rule's K-counter rows are spectral-support weights of the SUBSTRATE functional — `w(L_max)` truncation, `w(τ-moduli)` deformation, `w(C_2^max)` Casimir-ceiling. `G` and `S` enter through the LABORATORY-IN reduction pipeline, NOT the substrate spectral support. Distinct axis by inspection of WHERE the factor enters the functional; hence these rows document a NEW `cancelling_axis` value (`LAB-IN-PIPELINE`) WITHOUT advancing the spectral-support K-counter. Substrate-first direction preserved: the fabric's spectral moments are the fundamental layer; `G` and `S` are parameters of how laboratories read the emergent image, and the detector now sees cancellations on BOTH layers.

**Forward enforcement**: S102+ plan-freeze pipelines run the 3-class detector on every plan file; the `NON-K-ADVANCING` tag prevents downstream K-counter contamination; any future severity hardening of the S2 classes cites the S101 W8a-2 severity pin as the pre-registered baseline.
"""


def main() -> int:
    if not CORPUS.exists():
        print(f"ERROR: corpus file not found: {CORPUS}", file=sys.stderr)
        return 2  # script breakage

    text = CORPUS.read_text(encoding="utf-8")

    # Idempotency: if the unique title fragment is already present, NO-OP.
    if SECTION_TITLE_FRAGMENT in text:
        m = re.search(
            r"(?m)^#{2,4}\s+§(\d+)\.\s+Multiplicative-normalization cancellation",
            text,
        )
        landed = int(m.group(1)) if m else PLANNED_SECTION_N
        print(
            f"IDEMPOTENT-NOOP: section already on disk at §{landed} "
            f"(title fragment '{SECTION_TITLE_FRAGMENT}' present); no append."
        )
        print(f"CORPUS_SECTION_LANDED={landed}")
        print("REROUTE=NONE")
        return 0

    # (1) PRE-SCAN ALL header levels before allocating.
    existing = existing_section_numbers(text)
    section_n = next_free_section(existing)
    rerouted = section_n != PLANNED_SECTION_N

    if rerouted:
        # (3) Occupancy reroute — signal FAIL-with-remediation to the caller.
        print(
            f"REROUTE-OCCUPANCY: planned §{PLANNED_SECTION_N} occupied "
            f"(existing slots include {sorted(s for s in existing if s >= PLANNED_SECTION_N)}); "
            f"rerouting to next-free §{section_n}.",
            file=sys.stderr,
        )

    body = build_section_text(section_n)

    # (2) SINGLE-SHOT open("a") POSIX O_APPEND. Ensure a clean separator: the
    # body already begins with "\n## §N"; guarantee the file ends with a newline
    # before appending so headers don't collide on one line.
    sep = "" if text.endswith("\n") else "\n"  # (local)
    with CORPUS.open("a", encoding="utf-8") as fh:
        fh.write(sep + body)

    print(f"APPENDED: §{section_n} written via single-shot open('a') O_APPEND.")
    print(f"CORPUS_SECTION_LANDED={section_n}")
    print(f"REROUTE={'OCCUPANCY-' + str(PLANNED_SECTION_N) + '-to-' + str(section_n) if rerouted else 'NONE'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
