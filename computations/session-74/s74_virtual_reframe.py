"""
S74 W4-BB: VIRTUAL-REFRAME-74 — Revise Framework Documents Using "Virtual Particle" Language

Task: Audit framework documents for QFT container-thinking language around
"virtual particles", "vacuum fluctuations", "zero-point energy", "propagators",
"off-shell" — and propose substrate-framing revisions per project memory
`project_virtual-particles-decoherence.md`.

The substrate reframing (S72 user insight):
  - virtual particle        -> decohered laminar flow / off-shell fiber mode
  - vacuum fluctuation      -> unrealized substrate flow that decoheres for
                                lack of local stimulation
  - zero-point energy       -> aggregate energy of flows that do not self-sustain
                                (still fine as a numerical quantity, but the
                                 physical interpretation must be reframed)
  - propagator exp(-mr)     -> decorrelation length of unstimulated flow
  - off-shell               -> flow that does not self-sustain on the CG(24)
                                Josephson lattice

Only PROPOSE revisions. Do NOT edit framework documents.

Gate: VIRTUAL-REFRAME-74
  PASS if >= 3 revisions proposed.
  INFO if 1-2 revisions proposed.
  FAIL if 0 revisions proposed.

Outputs:
  s74_virtual_reframe.npz  — revision table (old text, new text, rationale)
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import M_KK  # noqa: F401  (provenance check)

# -----------------------------------------------------------------------------
# Audit configuration
# -----------------------------------------------------------------------------

PROJECT_ROOT = Path(r"C:\sandbox\Ainulindale Exflation")

# Container-thinking tokens we are auditing for.
AUDIT_TOKENS = [
    "virtual particle",
    "vacuum fluctuation",
    "quantum fluctuation",
    "zero-point energy",
    "off-shell",
    "propagator",
    "one-loop correction",
    "quantum depletion",
]

# Files to scan (framework-level, not session minutes).
FRAMEWORK_DOCS = [
    PROJECT_ROOT / "phonon_exflation_cosmology.md",
    PROJECT_ROOT / "Ainulindale Exflation Nutshell.md",
    PROJECT_ROOT / "nutshell.md",
    PROJECT_ROOT / "sessions" / "framework" / "Atlas" / "atlas-03-equation-flow.md",
    PROJECT_ROOT / "sessions" / "framework" / "Atlas" / "atlas-07-permanent-results.md",
]


# -----------------------------------------------------------------------------
# Revision table — manually curated from audit of the above files.
# Each entry is:
#   (doc, line, old_text, new_text, rationale, severity)
# severity: "high"  = explicit container phrase, misleading
#           "medium" = technical term (zero-point, one-loop) where physical
#                       interpretation is container-flavored
#           "low"    = context-dependent; flag for stylistic note
# -----------------------------------------------------------------------------

REVISIONS = [
    # ------------------------------------------------------------------
    # phonon_exflation_cosmology.md  — Section 5.5 (CC as integrability)
    # ------------------------------------------------------------------
    {
        "doc": "phonon_exflation_cosmology.md",
        "line": 231,
        "old": (
            "The cosmological constant problem arises only in effective field "
            "theories that compute vacuum energy without UV completion."
        ),
        "new": (
            "The cosmological constant problem arises only in effective field "
            "theories that compute the aggregate energy of unrealized substrate "
            "flows (conventionally called \"vacuum energy\") without a UV "
            "completion of the fabric's spectral content."
        ),
        "rationale": (
            "Replaces container-thinking phrase \"vacuum energy\" in the "
            "explanatory sentence with the substrate description: the CC puzzle "
            "is about aggregate energy of decohered laminar flows, not about a "
            "reservoir of energy existing IN a pre-existing spacetime container."
        ),
        "severity": "high",
    },
    {
        "doc": "phonon_exflation_cosmology.md",
        "line": 233,
        "old": (
            "The zero-point energy of the 992-mode Dirac spectrum on K, weighted "
            "by the GGE occupation numbers, gives E_ZP(GGE) = 81,493 M_KK."
        ),
        "new": (
            "The aggregate energy of decohered laminar flows across the 992-mode "
            "D_K spectrum on K (conventionally called the \"zero-point energy\"), "
            "weighted by the GGE occupation numbers, gives "
            "E_flow(GGE) = 81,493 M_KK. In the substrate picture, each mode "
            "corresponds to an off-shell fiber excitation whose laminar flow "
            "never finds a self-sustaining CG(24) neighbor, and the accumulated "
            "mismatch energy is what effective field theory mislabels as "
            "\"vacuum fluctuations.\""
        ),
        "rationale": (
            "Keeps the numerical quantity (E_ZP = 81,493 M_KK) unchanged — the "
            "spectral sum is correct — but relabels its physical interpretation "
            "from 'zero-point energy of a field IN a vacuum' to 'aggregate "
            "decohered laminar flow energy of the fabric itself'. This is the "
            "core substrate reframing: the numbers survive, the container "
            "metaphor does not."
        ),
        "severity": "high",
    },
    # ------------------------------------------------------------------
    # phonon_exflation_cosmology.md  — Section 5.6 (quantum depletion)
    # ------------------------------------------------------------------
    {
        "doc": "phonon_exflation_cosmology.md",
        "line": 247,
        "old": (
            "In 3He-B language, this corresponds to a quantum depletion parameter "
            "of 0.447---44.7% of the condensate is quantum-depleted, firmly in "
            "the strong-coupling regime where Bogoliubov theory requires "
            "resummation."
        ),
        "new": (
            "In 3He-B language, this corresponds to a quantum depletion parameter "
            "of 0.447 — 44.7% of the condensate's laminar flow is siphoned into "
            "decohered off-shell fiber modes (what QFT calls \"virtual pairs\" "
            "and Bogoliubov theory calls \"quasiparticle occupation of the "
            "ground state\"), firmly in the strong-coupling regime where "
            "Bogoliubov theory requires resummation."
        ),
        "rationale": (
            "The phrase 'quantum depletion' is a condensed-matter QFT container "
            "notion. Substrate reframing: depletion = laminar flow that fails to "
            "lock with its neighbor across the CG(24) Josephson graph, and "
            "decoheres. The numerical value (0.447) is preserved."
        ),
        "severity": "medium",
    },
    # ------------------------------------------------------------------
    # phonon_exflation_cosmology.md  — Section 2, Ornstein-Zernike wording
    # ------------------------------------------------------------------
    {
        "doc": "phonon_exflation_cosmology.md",
        "line": 220,
        "old": (
            "The BCS gap must survive not only the transit quench but also "
            "fluctuations of the internal metric away from the fold saddle."
        ),
        "new": (
            "The BCS gap must survive not only the transit quench but also "
            "coherent excursions of the internal metric away from the fold "
            "saddle — i.e., substrate flows along the moduli directions that, "
            "unlike virtual off-shell flows, DO self-sustain as coherent moduli "
            "motion."
        ),
        "rationale": (
            "Distinguishes 'fluctuations of the internal metric' (which here "
            "means coherent moduli-space motion, NOT QFT vacuum fluctuations) "
            "from the decohered-laminar-flow reading of 'fluctuation' that "
            "would be imported by a QFT-trained reader. The language upgrade "
            "prevents the container-thinking misread of this specific sentence."
        ),
        "severity": "low",
    },
    # ------------------------------------------------------------------
    # atlas-03-equation-flow.md  — E20 Ornstein-Zernike propagator label
    # ------------------------------------------------------------------
    {
        "doc": "sessions/framework/Atlas/atlas-03-equation-flow.md",
        "line": 75,
        "old": (
            "E20: Ornstein-Zernike Propagator -- P_G(K) = T/(J K^2 + m_G^2)\n"
            "Goldstone phase propagator on Josephson lattice."
        ),
        "new": (
            "E20: Ornstein-Zernike Correlator (substrate decorrelation kernel) "
            "-- P_G(K) = T/(J K^2 + m_G^2)\n"
            "Goldstone phase correlator on the CG(24) Josephson lattice. In the "
            "substrate picture, the K^{-2} form encodes the decorrelation length "
            "of an unstimulated laminar flow rather than a Feynman propagator "
            "for a particle moving THROUGH a vacuum. The 1/m_G prefactor is the "
            "Leggett-mode decorrelation scale at which off-shell fiber modes "
            "decohere."
        ),
        "rationale": (
            "The word 'propagator' (Feynman sense) carries container thinking: "
            "a particle propagating THROUGH spacetime. Substrate reading: the "
            "Ornstein-Zernike kernel is the two-point decorrelation function "
            "for substrate flow patterns across CG(24). Per S72 memory: "
            "propagator exp(-mr) = decorrelation length of unstimulated "
            "fluctuation. Relabel to 'correlator / decorrelation kernel'."
        ),
        "severity": "high",
    },
    # ------------------------------------------------------------------
    # atlas-03-equation-flow.md  — E23 propagator phrasing
    # ------------------------------------------------------------------
    {
        "doc": "sessions/framework/Atlas/atlas-03-equation-flow.md",
        "line": 84,
        "old": (
            "alpha_s = n_s^2 - 1 Identity -- Five proofs lock running to tilt "
            "for K^2 propagators on compact Josephson lattices"
        ),
        "new": (
            "alpha_s = n_s^2 - 1 Identity -- Five proofs lock running to tilt "
            "for K^2 two-point correlators on compact Josephson lattices (the "
            "K^{-2} kernel is the substrate's decorrelation kernel, not a "
            "Feynman propagator)"
        ),
        "rationale": (
            "Same reframing as E20: 'propagator' -> 'two-point correlator / "
            "decorrelation kernel' to stay consistent with substrate framing. "
            "Preserves the alpha_s = n_s^2 - 1 theorem unchanged."
        ),
        "severity": "medium",
    },
    # ------------------------------------------------------------------
    # atlas-07-permanent-results.md — A9 CC Monotonicity theorem wording
    # ------------------------------------------------------------------
    {
        "doc": "sessions/framework/Atlas/atlas-07-permanent-results.md",
        "line": 29,
        "old": (
            "A9 | CC Monotonicity Theorem (q-theory) -- dE_ZP/dq = (1/4) sum "
            "(2N_n + 1) d_n / omega_n(q) > 0 for all q > -lambda_min^2. The "
            "zero-point energy of any spectrum with positive weights is "
            "monotonically increasing in the shift parameter q."
        ),
        "new": (
            "A9 | CC Monotonicity Theorem (q-theory) -- dE_flow/dq = (1/4) sum "
            "(2N_n + 1) d_n / omega_n(q) > 0 for all q > -lambda_min^2. The "
            "aggregate energy of decohered laminar flows across any D_K "
            "spectrum with positive weights (the quantity conventionally called "
            "'zero-point energy') is monotonically increasing in the q-theory "
            "shift parameter."
        ),
        "rationale": (
            "Permanent theorem A9 is stated in QFT zero-point language. "
            "Substrate reframing: 'zero-point energy' -> 'aggregate energy of "
            "decohered laminar flows'. The mathematical content is unchanged; "
            "the physical interpretation is corrected so A9 is read as a "
            "substrate theorem about flow monotonicity rather than a vacuum "
            "energy theorem in a container."
        ),
        "severity": "medium",
    },
    # ------------------------------------------------------------------
    # Ainulindale Exflation Nutshell.md — GGE fluctuation phrasing
    # ------------------------------------------------------------------
    {
        "doc": "Ainulindale Exflation Nutshell.md",
        "line": 124,
        "old": (
            "The GGE relic is not a thermal state. It's not a fluctuation. "
            "It's a permanent quantum state protected by integrability"
        ),
        "new": (
            "The GGE relic is not a thermal state. It's not a decohered flow. "
            "It's a permanent coherent-flow pattern across the fabric, "
            "protected by Richardson-Gaudin integrability — 8 resonant "
            "frequencies that no interaction within the integrable dynamics "
            "can redistribute."
        ),
        "rationale": (
            "The contrast 'not a fluctuation' imports the QFT container reading "
            "of 'fluctuation' (= vacuum fluctuation). In the substrate picture "
            "the relevant contrast is 'not a decohered flow' (decohered = "
            "virtual = fails to self-sustain). This sharpens the GGE claim: "
            "the relic is a permanent laminar-flow pattern that self-sustains "
            "because integrability keeps each of its 8 modes locked, unlike "
            "virtual flows which fail to self-sustain and decohere."
        ),
        "severity": "high",
    },
]


# -----------------------------------------------------------------------------
# Audit pass: verify each flagged doc exists and is readable
# -----------------------------------------------------------------------------

def audit_sources() -> dict:
    """Verify all flagged documents exist. Count token occurrences."""
    report = {}
    for doc in FRAMEWORK_DOCS:
        if not doc.exists():
            report[doc.name] = {"exists": False}
            continue
        text = doc.read_text(encoding="utf-8", errors="replace")
        counts = {tok: text.lower().count(tok.lower()) for tok in AUDIT_TOKENS}
        report[doc.name] = {
            "exists": True,
            "n_lines": text.count("\n"),
            "token_counts": counts,
            "total_hits": sum(counts.values()),
        }
    return report


# -----------------------------------------------------------------------------
# Gate evaluation
# -----------------------------------------------------------------------------

def evaluate_gate(n_revisions: int) -> str:
    if n_revisions >= 3:
        return "PASS"
    if n_revisions >= 1:
        return "INFO"
    return "FAIL"


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

def main() -> None:
    print("=" * 72)
    print("S74 W4-BB: VIRTUAL-REFRAME-74 — Virtual Particle Reframing Audit")
    print("=" * 72)

    # Source audit
    print("\n[1/3] Auditing framework source documents for container tokens.")
    src_report = audit_sources()
    for doc, info in src_report.items():
        if not info["exists"]:
            print(f"  MISSING: {doc}")
            continue
        print(f"  {doc}: {info['total_hits']} container-token hits "
              f"across {info['n_lines']} lines")
        for tok, cnt in info["token_counts"].items():
            if cnt:
                print(f"    - {tok!r}: {cnt}")

    # Revision table
    print(f"\n[2/3] Proposed revisions: {len(REVISIONS)}")
    for i, rev in enumerate(REVISIONS, 1):
        print(f"  R{i}: [{rev['severity']:>6}] {rev['doc']} L{rev['line']}")
        print(f"       rationale: {rev['rationale'][:110]}...")

    # Gate
    n_rev = len(REVISIONS)
    verdict = evaluate_gate(n_rev)
    print(f"\n[3/3] Gate VIRTUAL-REFRAME-74: {verdict} "
          f"({n_rev} revisions; PASS>=3, INFO>=1, FAIL=0)")

    # Save to npz
    out = Path(__file__).parent / "s74_virtual_reframe.npz"
    np.savez(
        out,
        n_revisions=n_rev,
        gate_verdict=verdict,
        docs_audited=np.array([d.name for d in FRAMEWORK_DOCS], dtype=object),
        audit_tokens=np.array(AUDIT_TOKENS, dtype=object),
        revision_doc=np.array([r["doc"] for r in REVISIONS], dtype=object),
        revision_line=np.array([r["line"] for r in REVISIONS], dtype=np.int32),
        revision_old=np.array([r["old"] for r in REVISIONS], dtype=object),
        revision_new=np.array([r["new"] for r in REVISIONS], dtype=object),
        revision_rationale=np.array(
            [r["rationale"] for r in REVISIONS], dtype=object
        ),
        revision_severity=np.array(
            [r["severity"] for r in REVISIONS], dtype=object
        ),
        src_report_keys=np.array(list(src_report.keys()), dtype=object),
        src_report_hits=np.array(
            [src_report[k].get("total_hits", -1) for k in src_report],
            dtype=np.int32,
        ),
    )
    print(f"\nWrote: {out}")
    print("\nNOTE: This script DOES NOT modify framework documents. "
          "Revisions are proposals only, per task spec.")


if __name__ == "__main__":
    main()
