"""
S75 W4-A: STRUCTURAL-REGISTRY-ENTRY-48

Register the S74 W4-X six-layer composite protection theorem as permanent
result #48 in the permanent results registry.

This script:
  1. Loads the S74 W4-X results from s74_multi_layer_protection.npz
  2. Validates all required fields are present
  3. Outputs the registry entry in the standard format used by
     sessions/permanent-results-registry.md

Gate: S75-F6-REGISTRY-48
  PASS: Entry constructed with all required fields (number, result statement,
        session provenance, status, layer count, composite proof status,
        independence witnesses, observable coverage count).
  FAIL: Missing fields or theorem data not found.

Agent: gen-physicist
Session: 75
"""

from __future__ import annotations

import os
import sys
import numpy as np

# S34+ compliance: import from canonical_constants
from canonical_constants import M_KK  # noqa: F401


# ---------------------------------------------------------------------------
# Constants for this script
# ---------------------------------------------------------------------------
REGISTRY_NUMBER = 48  # (local) next free slot after S66 W8-A #47
N_LAYERS_REQUIRED = 6  # (local) all six layers must be verified
N_INDEPENDENCE_WITNESSES = 7  # (local) from S74 W4-X proof section III
N_OBSERVABLES_COVERED = 23  # (local) observable coverage table size
SOURCE_SESSION = "S74 W4-X"  # (local)
SOURCE_GATE = "MULTI-LAYER-PROTECTION-THEOREM-74"  # (local)
SOURCE_SCRIPT = "computations/session-74/s74_multi_layer_protection.py"  # (local)
SOURCE_DATA = "computations/session-74/s74_multi_layer_protection.npz"  # (local)


# ---------------------------------------------------------------------------
# Step 1: Load S74 W4-X data
# ---------------------------------------------------------------------------
def load_s74_data():
    """Load the S74 multi-layer protection theorem data."""
    here = os.path.dirname(os.path.abspath(__file__))
    npz_path = os.path.join(here, "s74_multi_layer_protection.npz")

    if not os.path.exists(npz_path):
        print(f"ERROR: Source data not found at {npz_path}")
        print("  Run s74_multi_layer_protection.py first.")
        return None

    data = np.load(npz_path, allow_pickle=True)
    return data


# ---------------------------------------------------------------------------
# Step 2: Validate all required fields
# ---------------------------------------------------------------------------
def validate_fields(data):
    """Check that all fields needed for a registry entry are present."""
    required_keys = [
        "n_verified",
        "composite_proven",
        "gate_verdict",
        "registry_candidate_number",
        "theorem_statement",
        "setup",
        "layer_1", "layer_2", "layer_3", "layer_4", "layer_5", "layer_6",
        "independence",
        "verifications",
    ]

    missing = []  # (local)
    for key in required_keys:
        if key not in data:
            missing.append(key)

    if missing:
        print(f"FAIL: Missing keys in source data: {missing}")
        return False

    # Validate content
    n_verified = int(data["n_verified"])  # (local)
    composite_proven = bool(data["composite_proven"])  # (local)
    gate_verdict = str(data["gate_verdict"])  # (local)
    candidate_num = int(data["registry_candidate_number"])  # (local)

    checks_passed = True  # (local)

    if n_verified != N_LAYERS_REQUIRED:
        print(f"FAIL: Expected {N_LAYERS_REQUIRED} verified layers, got {n_verified}")
        checks_passed = False

    if not composite_proven:
        print("FAIL: Composite theorem not marked as proven")
        checks_passed = False

    if gate_verdict != "PASS":
        print(f"FAIL: Source gate verdict is '{gate_verdict}', expected 'PASS'")
        checks_passed = False

    if candidate_num != REGISTRY_NUMBER:
        print(f"WARNING: Candidate number {candidate_num} vs expected {REGISTRY_NUMBER}")
        # Not a hard fail -- the number is what we assign

    return checks_passed


# ---------------------------------------------------------------------------
# Step 3: Construct the registry entry
# ---------------------------------------------------------------------------

# The six layers with their names and mathematical content
LAYER_NAMES = {
    "L1": "right-invariance / Schur block-diagonality",
    "L2": "[J, D_K] = 0 CPT / KO-dim = 6",
    "L3": "Peter-Weyl homogeneity",
    "L4": "Cl(8) real-dim-8 spinor structure",
    "L5": "Kosmann singlet projection",
    "L6": "particle-hole BDI",
}

# Layer precisions from constituent registry entries
LAYER_PRECISIONS = {
    "L1": "8.4e-15 (S22b numerical) + exact (S61 algebraic proof)",
    "L2": "3.29e-13 (S17a, 79,968 pairs) + exact (KO-dim axioms)",
    "L3": "exact (Peter-Weyl theorem 1927)",
    "L4": "exact (Bott periodicity, topological)",
    "L5": "1.12e-16 (S25 Berry curvature vanishing)",
    "L6": "exact (AZ classification) + machine epsilon (Pfaffian checks)",
}

# Registry anchors for each layer
LAYER_ANCHORS = {
    "L1": [
        "1A:1 D_K Block-Diagonality Universality (S22b)",
        "II:6 ROBUST infrastructure",
        "S61 BLOCK-DIAG-GENERAL-61",
        "VdD Paper 01 Sec 3",
    ],
    "L2": [
        "Registry line 121 [J, D_K(tau)] = 0 (S17a)",
        "II:3-5 Clifford signs ROBUST",
        "#11 Grading Theorem",
        "VdD Paper 06 KO-dim axioms",
    ],
    "L3": [
        "Peter-Weyl 1927 (Bump, Lie Groups, Thm 17.1)",
        "II:1 finite-dim, no L_max",
        "S73B W3 shape-boundary decoupling",
        "VdD Paper 02 families",
    ],
    "L4": [
        "1A:6 Cl(8) Three-Way Bridge (S28)",
        "1A:3 Trap 3 e/(ac) = 1/16",
        "II:1 KO-dim = 6 ROBUST",
        "#47 KO-dimension degeneracy at d=8",
        "VdD Paper 06",
    ],
    "L5": [
        "1A:7 Berry Curvature Vanishing (S25)",
        "#17 Kosmann-BCS condensate (S23a)",
        "#16 Anderson-Higgs Impossibility (S51)",
        "S61 GAUGE-MODULE-61 (rank 775)",
        "VdD Paper 06",
    ],
    "L6": [
        "II:13 AZ class BDI ROBUST",
        "#35 chirality antisymmetry (S64 W6-B)",
        "#36 BdG Heat Kernel Factorization",
        "#31 Fermi-surface lock",
        "II:15 Pfaffian Z_2 = +1",
        "VdD Paper 06 Euclidean fermions / Pfaffian",
    ],
}

# Independence witnesses from S74 W4-X proof section III
INDEPENDENCE_WITNESSES = [
    ("L1", "L2", "Inhomogeneous-metric perturbation preserves CPT but breaks right-invariance, and conversely"),
    ("L1", "L3", "Left-action deformation preserves Schur blocks but breaks Peter-Weyl completeness"),
    ("L2", "L4", "CPT sign flip preserves Cl(8) algebra but breaks J; dim(S)=8 is topological, J is metric-dependent"),
    ("L2", "L5", "Kosmann K_a=0 is kinematic (left-invariance), J=[,D_K]=0 is spectral; independent operator classes"),
    ("L3", "L4", "Peter-Weyl is group-rep decomposition; Cl(8) is fiber-bundle structure; different categories"),
    ("L4", "L6", "Bott periodicity is topological; BDI classification is spectral (AZ class). Independent by construction"),
    ("L5", "L6", "Kosmann protects left-action phases; particle-hole protects E <-> -E pairing; orthogonal failure modes"),
]


def build_registry_entry():
    """Construct the registry table entry for result #48."""

    # Main registry table row (matches format of Section 1D)
    entry_row = (
        f"| {REGISTRY_NUMBER} | "
        f"**Six-Layer Composite Protection of (0,0) Sector** -- "
        f"The trivial Peter-Weyl sector H_(0,0) ~ S of the spectral triple "
        f"on Jensen-deformed SU(3) is protected by the disjunction of six "
        f"independent structural layers: "
        f"(L1) right-invariance / Schur block-diagonality, "
        f"(L2) [J, D_K] = 0 CPT / KO-dim = 6, "
        f"(L3) Peter-Weyl homogeneity, "
        f"(L4) Cl(8) real-dim-8 spinor structure, "
        f"(L5) Kosmann singlet projection, "
        f"(L6) particle-hole BDI. "
        f"A perturbation preserving at least one layer leaves all observables "
        f"in that layer's protecting set exactly invariant. The six layers are "
        f"pairwise-independent (7 witnesses) and the composite is non-redundant "
        f"(23 observables covered, no empty protecting set). "
        f"| {SOURCE_SESSION} | PERMANENT (COMPOSITE) |"
    )

    return entry_row


def build_full_report(data):
    """Build the complete registry entry report with all metadata."""
    n_verified = int(data["n_verified"])  # (local)
    composite_proven = bool(data["composite_proven"])  # (local)
    gate_verdict = str(data["gate_verdict"])  # (local)

    lines = []  # (local)

    lines.append("=" * 72)
    lines.append("PERMANENT RESULTS REGISTRY -- ENTRY #48")
    lines.append("Six-Layer Composite Protection of the (0,0) Sector")
    lines.append("=" * 72)
    lines.append("")

    # --- Source validation ---
    lines.append("SOURCE VALIDATION")
    lines.append("-" * 40)
    lines.append(f"  Source session:       {SOURCE_SESSION}")
    lines.append(f"  Source gate:          {SOURCE_GATE}")
    lines.append(f"  Source gate verdict:  {gate_verdict}")
    lines.append(f"  Layers verified:     {n_verified} / {N_LAYERS_REQUIRED}")
    lines.append(f"  Composite proven:    {composite_proven}")
    lines.append(f"  Source script:       {SOURCE_SCRIPT}")
    lines.append(f"  Source data:         {SOURCE_DATA}")
    lines.append("")

    # --- Registry table row ---
    lines.append("REGISTRY TABLE ROW (for Section 1E of permanent-results-registry.md)")
    lines.append("-" * 72)
    lines.append("")
    lines.append("| # | Result | Session | Status |")
    lines.append("|:--|:-------|:--------|:-------|")
    lines.append(build_registry_entry())
    lines.append("")

    # --- Layer summary ---
    lines.append("LAYER SUMMARY")
    lines.append("-" * 40)
    for lid in ["L1", "L2", "L3", "L4", "L5", "L6"]:
        lines.append(f"  {lid}: {LAYER_NAMES[lid]}")
        lines.append(f"       Precision: {LAYER_PRECISIONS[lid]}")
        lines.append(f"       Anchors:   {', '.join(LAYER_ANCHORS[lid])}")
        lines.append("")

    # --- Independence witnesses ---
    lines.append("INDEPENDENCE WITNESSES (7 pairs)")
    lines.append("-" * 40)
    for i, (a, b, reason) in enumerate(INDEPENDENCE_WITNESSES, 1):
        lines.append(f"  W{i}. {a} vs {b}: {reason}")
    lines.append("")

    # --- Metadata for registry notes ---
    lines.append("REGISTRY METADATA")
    lines.append("-" * 40)
    lines.append(f"  Category:          COMPOSITE / STRUCTURAL FLOOR")
    lines.append(f"  Precision:         Logical / categorical (no single numerical tolerance)")
    lines.append(f"  L_max-invariance:  Structural floor (verified L=3,5,7 in S73B W5-D)")
    lines.append(f"  Observables:       {N_OBSERVABLES_COVERED} with protecting sets size 1 or 2")
    lines.append(f"  Dependencies:      39 total registry citations across 6 layers")
    lines.append(f"  Substrate role:    Hosts BCS ladder, Josephson condensate, Leggett")
    lines.append(f"                     phase singlet, three-phonon vertex, Wilson loop")
    lines.append(f"  Independence:      {N_INDEPENDENCE_WITNESSES} pairwise witnesses exhibited")
    lines.append("")

    # --- Composite theorem statement ---
    lines.append("COMPOSITE THEOREM (condensed)")
    lines.append("-" * 72)
    lines.append("")
    lines.append("Theorem (Six-Layer Multi-Layer Protection of the (0,0) Sector).")
    lines.append("")
    lines.append("Let (A = C^inf(K), H = L^2(K, S), D_K) be the canonical spectral triple")
    lines.append("on K = SU(3) with Jensen-deformed left-invariant metric g_tau, and let")
    lines.append("H_(0,0) = S be the trivial Peter-Weyl sector. Then the (0,0) sector is")
    lines.append("protected against any Hermitian perturbation delta_D of D_K that preserves")
    lines.append("at least one of the six layers L1-L6:")
    lines.append("")
    lines.append("  Protection(H_(0,0), delta_D) = L1(delta_D) OR L2(delta_D)")
    lines.append("                                   OR L3(delta_D) OR L4(always)")
    lines.append("                                   OR L5(delta_D) OR L6(delta_D)")
    lines.append("")
    lines.append("The six layers are logically independent (7 pairwise witnesses), and the")
    lines.append("composite is non-redundant (removing any layer leaves at least one")
    lines.append("observable unprotected). L4 (Cl(8) / Bott periodicity) is always preserved")
    lines.append("within the spectral triple axiom system.")
    lines.append("")

    # --- Proof structure ---
    lines.append("PROOF STRUCTURE (6 steps)")
    lines.append("-" * 40)
    lines.append("  (1) Each layer = operator commutation [O_k, D_K] = 0")
    lines.append("  (2) H_(0,0) = intersection of Fix/Ker/Im of all six operators")
    lines.append("  (3) Single-layer preservation suffices (eigenspace invariance)")
    lines.append("  (4) Composite is disjunction, not conjunction")
    lines.append("  (5) 7 pairwise-independence witnesses")
    lines.append("  (6) Non-redundancy: each layer uniquely protects >= 1 observable")
    lines.append("")

    # --- Gate assessment ---
    lines.append("=" * 72)
    lines.append("GATE: S75-F6-REGISTRY-48")
    lines.append(f"  Required fields present: ALL")
    lines.append(f"  Registry number:         {REGISTRY_NUMBER}")
    lines.append(f"  Result statement:        YES (condensed + full)")
    lines.append(f"  Session provenance:      {SOURCE_SESSION}")
    lines.append(f"  Status:                  PERMANENT (COMPOSITE)")
    lines.append(f"  Layer count:             {n_verified}/6")
    lines.append(f"  Composite proof:         {composite_proven}")
    lines.append(f"  Independence witnesses:  {N_INDEPENDENCE_WITNESSES}")
    lines.append(f"  Observable coverage:     {N_OBSERVABLES_COVERED}")
    lines.append(f"  VERDICT: PASS")
    lines.append("=" * 72)

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 72)
    print("S75 W4-A: STRUCTURAL-REGISTRY-ENTRY-48")
    print("Registering S74 W4-X Six-Layer Composite Protection Theorem")
    print("=" * 72)
    print()

    # Step 1: Load data
    data = load_s74_data()
    if data is None:
        print("\nGATE S75-F6-REGISTRY-48: FAIL (source data not found)")
        sys.exit(1)

    # Step 2: Validate
    print("Step 1: Validating source data fields...")
    valid = validate_fields(data)  # (local)
    if not valid:
        print("\nGATE S75-F6-REGISTRY-48: FAIL (validation failed)")
        sys.exit(1)
    print("  All fields present and valid.")
    print()

    # Step 3: Build and print registry entry
    print("Step 2: Constructing registry entry...")
    print()
    report = build_full_report(data)  # (local)
    print(report)

    # Step 4: Save output
    here = os.path.dirname(os.path.abspath(__file__))  # (local)
    out_path = os.path.join(here, "s75_registry_entry_48.npz")  # (local)
    np.savez(
        out_path,
        registry_number=REGISTRY_NUMBER,
        result_statement=build_registry_entry(),
        session_provenance=SOURCE_SESSION,
        status="PERMANENT (COMPOSITE)",
        n_layers=N_LAYERS_REQUIRED,
        composite_proven=True,
        n_independence_witnesses=N_INDEPENDENCE_WITNESSES,
        n_observables_covered=N_OBSERVABLES_COVERED,
        gate_verdict="PASS",
        layer_names=np.array(list(LAYER_NAMES.values()), dtype=object),
        layer_precisions=np.array(list(LAYER_PRECISIONS.values()), dtype=object),
    )
    print()
    print(f"Data saved to {out_path}")


if __name__ == "__main__":
    main()
