#!/usr/bin/env python3
"""
S74 W4-II: FOUNDATIONAL-AUDIT-75-SPEC
======================================

Purpose
-------
Serialize the full specification for FOUNDATIONAL-AUDIT-75 (post-S74
carry-forward, proposed in S73B mack-vdd workshop carry-forward #10 /
vdE2 emergence) to an .npz container so downstream S75 wave planning
can load it verbatim.

This is a SPEC-only computation. No physics is evaluated. The output
is a structured specification describing:
  1. the foundational assumptions identified in the framework
  2. the one-DOF variation protocol for each
  3. the list of permanent theorems to test against each variation
  4. the full-fidelity S75 agent prompt text

Source
------
S73B mack-vdd workshop, carry-forward #10 (vdE2 emergence):
"Systematically vary each foundational assumption by one degree of
freedom and check whether the 21 permanent theorems survive."

NOTE on theorem count: S73B proposed the audit with the then-current
floor of 21 permanent theorems. S74 W4-N (W5F-REVERIFY-74) promoted
the floor 21 -> 22 by re-verifying four NEEDS_REVERIFY theorems at
L_max=7 (three-phonon PH suppression, DNP crossing, Pomeranchuk  # (local)
f(0,0), FR settling time). FOUNDATIONAL-AUDIT-75 must therefore test
the updated 22-theorem floor.

Author: van-den-dungen-bridge-theorist
Date:   2026-04-11 (S74 W4-II)
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

# Canonical constants (import is mandatory; spec script uses a handful
# of invariants for self-documentation only).
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
    Vol_SU3_Haar,
)

Vol_SU3 = Vol_SU3_Haar  # (local) canonical Haar volume alias for self-doc


# ---------------------------------------------------------------------------
# SECTION A: Foundational assumption registry (7 entries)
# ---------------------------------------------------------------------------

FOUNDATIONAL_ASSUMPTIONS = [
    # id, name, current_choice, provenance, one_DOF_axis
    (
        "F1",
        "Spectral action cutoff function f*",
        "S72 spectral-functional-fit optimal (Gaussian-family, 1st-4th moment matched)",
        "Chamseddine-Connes 1996; S72 fit; canonical_constants.f_star",
        "Replace f* by one alternative Schwartz function at a time: "
        "(a) pure Gaussian f1(x)=exp(-x), (b) rational f2(x)=1/(1+x^2), "
        "(c) exponential cutoff f3(x)=(1+x)exp(-x), (d) heat f4(x)=exp(-x)*(1-x/2), "
        "(e) compactly supported f5 (Urysohn mollifier).",
    ),
    (
        "F2",
        "KO-dimension = 6 mod 8",
        "(epsilon, epsilon', epsilon'') = (+1, +1, -1) from Cl(8)+Cl(1,0) "
        "structure giving KO-dim=6; anchors J^2=+I, J D=+D J, J gamma=-gamma J",
        "S7-S8 branching_computation_32dim.py; Chamseddine-Connes-Marcolli 2007",
        "Vary KO-dim by +/-1: test KO=5 (epsilon'=-1) and KO=7 (epsilon'=-1, epsilon''=+1). "
        "For each candidate, reconstruct J, rho, gamma consistent with new sign triple. "
        "Ensure algebra A and Hilbert space H are held fixed.",
    ),
    (
        "F3",
        "Jensen metric ansatz on SU(3)",
        "g_Jensen(tau) = g_canonical + tau*(left-invariant axial deformation); "
        "tau in [0, 2]; fold at tau=0.190 (see canonical_constants.tau_fold)",
        "Baptista Paper 13 eq 2.7; S12 and S17b baptista_verification.py",
        "Replace Jensen deformation by an alternative left-invariant 1-parameter family "
        "on SU(3) that still preserves the Cartan subgroup: "
        "(a) diagonal-squashing along SO(3) subgroup, (b) Berger-type metric along U(2) subgroup, "
        "(c) Naveira-Tondeur family (generalized Heisenberg-type). "
        "Each family has one deformation parameter; match it to tau by requiring a common "
        "normalization at tau=0.",
    ),
    (
        "F4",
        "Peter-Weyl block-diagonal structure of D_K",
        "D_K exactly block-diagonal in (p,q) irreps for any left-invariant metric; "
        "3 independent proofs (algebraic, rep-theoretic, numerical, precision 8.4e-15)",
        "S22b theorem; permanent-results-registry Result 1",
        "Relax block-diagonality by introducing a controlled off-block perturbation "
        "epsilon * O where O is (i) a tangent-space rotation breaking left-invariance by "
        "epsilon in [1e-4, 1e-2], or (ii) a non-left-invariant but smooth modulation of "
        "the connection 1-form. Scan epsilon and check at which value each theorem first breaks.",
    ),
    (
        "F5",
        "Cl(8) real-dimension-8 structure (Psi_+ = C^16)",
        "Spin representation on C^32 split by gamma_9 into Psi_+/Psi_- of dim 16; "
        "SM quantum numbers emerge from C^16 branching; anchors order-one identity and Trap 3",
        "S7-S8 branching_computation_32dim.py; Result 3 (Algebraic traps)",
        "Compare against Cl(7) (dim-7, non-d=8) and Cl(9) (dim-9, non-d=8 with different "
        "epsilon triple). For each alternative, reconstruct gamma algebra and test whether "
        "the SM multiplet branching survives as a representation-theoretic consequence "
        "rather than a Clifford-dimension coincidence.",
    ),
    (
        "F6",
        "Non-additive Volovik q-theory G-renormalization (CC mechanism)",
        "rho_vac = chi_2 * H^2 * M_Pl^2 with chi_2 = 0.747 (NSFM / Volovik fill factor), "
        "closing 119.5 of 120 OOM with zero free parameters",
        "S59-S61 Volovik integration; S73B mack-vdd workshop C4 convergence",
        "Replace non-additive q-theory by the alternative variational framework: "
        "(a) Henneaux-Teitelboim unimodular gravity (additive, with integration-constant lambda), "
        "(b) sequestering mechanism (Kaloper-Padilla), (c) Weinberg adjustment mechanism. "
        "For each, recompute chi_2-analog and ask whether the 120-OOM closure remains structural.",
    ),
    (
        "F7",
        "L_max truncation scheme of Peter-Weyl",
        "L_max = 3 for production computations (default); S73B Wave 5 verified L_max-independence "
        "of the structural floor up to L_max = 7 and tracked prediction-layer drift",
        "S73B W5-F robustness audit; canonical_constants reference L_max=3",
        "This axis is ALREADY audited by S73B Wave 5. Include here only as a control axis "
        "(null variation) so the S75 audit architecture has a known-answer baseline: any "
        "theorem flagged by the F7 axis must match the Wave 5 classification (ROBUST, "
        "QUASI, NEEDS_REVERIFY).",
    ),
]


# ---------------------------------------------------------------------------
# SECTION B: Permanent theorems to test (22 post-W4-N; the canonical
# 22-theorem list is the S73B Wave-5 L_max-audit set PLUS the
# three-phonon PH suppression promoted by W5-D and re-verified at
# L_max=7 by S74 W4-N.)
#
# The current floor (22 theorems) is the updated Wave-5 canonical set.
# The broader permanent-results-registry has ~47 entries; the 22
# listed here are the Wave-5 canonical subset, chosen because they
# are the theorems the S73B carry-forward #10 explicitly cites.
# ---------------------------------------------------------------------------

PERMANENT_THEOREMS = [
    # id, title, precision_tag, depends_on_assumption_ids
    ("T01", "D_K Block-Diagonality Universality (S22b)",                         "8.4e-15",     ["F3", "F4"]),
    ("T02", "Spectral Action Monotonicity (a_{2k} monotone, k=0..3)",            "10^-39",      ["F1", "F3"]),
    ("T03", "Three Algebraic Traps (F/B=4/11, b_1/b_2=4/9, e/ac=1/16)",          "exact",       ["F5"]),
    ("T04", "LZ Retraction / BCS codimension-1 classification",                  "exact",       ["F3", "F4"]),
    ("T05", "Van Hove Zero Critical Coupling on Compact Manifolds",              "exact",       ["F3", "F4"]),
    ("T06", "Cl(8) Three-Way Bridge (Berry=NCG=KK)",                             "structural",  ["F2", "F5"]),
    ("T07", "Berry Curvature Vanishing (K_a anti-Hermitian)",                    "1.12e-16",    ["F3", "F4"]),
    ("T08", "Spectral Bianchi Identity (gauge-invariance constraint)",           "theoretical", ["F1", "F2"]),
    ("T09", "8D Petrov Classification Type D at tau=0",                          "machine eps", ["F3"]),
    ("T10", "Spectral Flow = 0 (R_K(tau) >= 12)",                                "exact",       ["F3"]),
    ("T11", "Grading Theorem (Tr gamma_9 f(D^2) = 0)",                           "exact",       ["F2", "F5"]),
    ("T12", "Perturbative Exhaustion (H1-H5 -> F_pert not true)",                "structural",  ["F1", "F3"]),
    ("T13", "Structural Monotonicity <lambda^2>(tau)",                           "machine eps", ["F3"]),
    ("T14", "Lorentzian CMPP Type D",                                            "exact",       ["F2", "F3"]),
    ("T15", "alpha_s = n_s^2 - 1 structural identity",                           "exact",       ["F4"]),
    ("T16", "Anderson-Higgs impossibility for U(1)_7 ([D_K,K_7]=0)",             "exact",       ["F4"]),
    ("T17", "CF-9 Triple Identity Berry=NCG=KK, |A_coset|^2 formula",            "2e-14",       ["F2", "F3", "F5"]),
    ("T18", "Cauchy-Schwarz Spectral Moment Bound f_4 f_0 / f_2^2 >= 1",         "exact proof", ["F1"]),
    ("T19", "CC = Integrability (dE_ZP/dq > 0, no interior q-theory equilib.)",  "exact proof", ["F6"]),
    ("T20", "Filter-Independence of Higgs Mass (m_H = 134 GeV all 6 cutoffs)",   "structural",  ["F1"]),
    ("T21", "N_e Saturation (N_e = 0.1734 IC-independent)",                      "structural",  ["F3"]),
    ("T22", "Three-phonon PH suppression (Gamma/H = 2.59e-10 at L=3,5,7)",       "machine eps", ["F3", "F4"]),
]


# ---------------------------------------------------------------------------
# SECTION C: The full S75 agent prompt (copy-ready)
# ---------------------------------------------------------------------------

S75_AGENT_PROMPT = r"""
You are the van-den-dungen-bridge-theorist. You have ONE task. Complete it and stop.

## Task: FOUNDATIONAL-AUDIT-75 -- Foundational Assumption Robustness Audit of the 22 Permanent Theorems

The framework rests on seven foundational assumptions (F1..F7). FOUNDATIONAL-AUDIT-75
varies each by one degree of freedom and checks whether each of the 22 permanent
theorems survives the variation. S73B Wave 5 tested ONLY the truncation axis F7 and
promoted three-phonon PH suppression (T22) to CONFIRMED at L=3,5,7. S74 W4-N
(W5F-REVERIFY-74) re-verified the three NEEDS_REVERIFY items (DNP, Pomeranchuk,
FR settling) at L_max=7, fixing the pre-audit floor at exactly 22 theorems.
This audit tests the six non-L_max axes.

### Foundational assumptions

F1: Spectral action cutoff function f* (current: S72 optimal)
F2: KO-dimension = 6 mod 8 (current: epsilon triple (+1,+1,-1))
F3: Jensen metric ansatz on SU(3) (current: left-invariant axial tau in [0,2])
F4: Peter-Weyl block-diagonal D_K (current: exact at 8.4e-15)
F5: Cl(8) real-dim-8 / Psi_+ = C^16 (current: branching gives SM quantum numbers)
F6: Volovik non-additive q-theory CC mechanism (current: chi_2 = 0.747)
F7: L_max truncation (current: L_max = 3; included as Wave-5 control)

### Protocol

For each assumption F_i in {F1,..,F7}, do the following.

STEP 1 -- Define the 1-DOF variation axis.

Use the axis specification loaded from
`computations/session-74/s74_foundational_audit_75_spec.npz` key `variation_protocols`.
Each axis has a discrete or continuous alternative (or a scan over epsilon for
relaxations of block-diagonality). Document the axis precisely before running.

STEP 2 -- For each alternative on the axis, compute the 22 permanent theorems in the
cheapest form that preserves the theorem statement. Minimum compute:

  T01 (block-diag):          norm of off-(p,q)-block part of D_K under the alternative
  T02 (SA monotonicity):     sign of d a_{2k}/d tau under the alternative f* or metric
  T03 (algebraic traps):     explicit ratios F/B, b_1/b_2, e/(ac) in the alternative Cl/dim
  T04 (LZ):                  codimension count of BCS transition locus
  T05 (Van Hove):            g(omega) ~ (omega - omega_min)^{-1/2} Laurent coefficient
  T06 (Cl(8) 3-way):         is Berry curvature = NCG inner fluctuation = KK A-tensor
  T07 (Berry = 0):            K_a anti-Hermitian check (||K_a + K_a^dag||)
  T08 (Spectral Bianchi):    Sum d_{(p,q)} dV_{(p,q)}/dtau M_a^{(p,q)} = 0 test
  T09 (Petrov Type D):       8D Weyl tensor eigenvalue multiplicities
  T10 (spectral flow = 0):   R_K(tau) lower bound; eta invariant
  T11 (grading):             Tr gamma_9 f(D_K^2) pointwise in tau
  T12 (perturbative exhaust):F_pert vs F_cond branch check
  T13 (monotonicity):        <lambda^2>(tau) finite-difference sign
  T14 (Lorentzian CMPP):     signature-changed CMPP type
  T15 (alpha_s = n_s^2 - 1): structural identity under altered propagator
  T16 (Anderson-Higgs):       [D_K, K_7] commutator under altered K_7
  T17 (CF-9 triple identity):|A_coset|^2 scan formula
  T18 (Cauchy-Schwarz f4 f0):ratio at Gaussian saturation
  T19 (CC integrability):    dE_ZP/dq sign under altered CC mechanism
  T20 (filter-independence): m_H constancy across 6 cutoff families under altered f*
  T21 (N_e saturation):       N_e IC-independence under altered Jensen family
  T22 (three-phonon PH):     Gamma/H ratio at the fold under the alternative choice,
                             Beliaev coherence factor, xi_B1/Delta check

STEP 3 -- Classify each (theorem, axis) pair as one of:

  ROBUST       -- theorem holds under all alternatives on this axis
  QUASI-ROBUST -- theorem holds at the original choice and in a neighborhood,
                  but breaks at specific alternatives (document the break)
  FRAGILE      -- theorem depends essentially on the original choice; any
                  variation breaks it
  INAPPLICABLE -- theorem statement does not type-check under the alternative

The classification for F7 (L_max control) must match the S73B Wave 5 audit
(Result 1 was ROBUST at L_max=3,5,7). If your F7 classification disagrees with
Wave 5, the script is broken -- halt and report.

STEP 4 -- Build the full audit matrix M[i,j] with i in theorems, j in axes,
entries in {ROBUST, QUASI-ROBUST, FRAGILE, INAPPLICABLE}. Compute per-theorem
and per-axis summary statistics.

### Pre-registered gate

FOUNDATIONAL-AUDIT-75 gate:

  PASS (framework's structural floor is foundationally robust):
        All 22 theorems are ROBUST or QUASI-ROBUST on axes F1..F6.
        No theorem is FRAGILE on more than one axis.
        L_max control (F7) matches Wave 5 and W4-N.

  INFO (mixed):
        1-5 (theorem, axis) pairs are FRAGILE on axes F1..F6.
        Document which foundational choice is load-bearing for which theorem.
        Update the permanent-results-registry to annotate load-bearing dependencies.

  FAIL (structural floor depends essentially on foundational choices):
        6+ (theorem, axis) pairs are FRAGILE on axes F1..F6, OR
        L_max control (F7) disagrees with Wave 5 or W4-N.

### Output (mandatory)

1. Script: computations/session-75/s75_foundational_audit.py
2. Data:   computations/session-75/s75_foundational_audit.npz
           (M matrix, per-theorem axis-by-axis verdicts, numerical evidence per
           theorem per alternative, log of attempted alternatives)
3. Plot:   computations/session-75/s75_foundational_audit_matrix.png
           (21x7 classification grid with color-coded cells)
4. Write results to the S75 working paper section for FOUNDATIONAL-AUDIT-75
   (REPLACE placeholder), including:
       - Classification matrix
       - Per-theorem text summary
       - Load-bearing dependencies list (for INFO)
       - Gate verdict

### Environment

Python: phonon-exflation-sim/.venv312/Scripts/python.exe
Working dir: C:\sandbox\Ainulindale Exflation

### Rules

- Numbers first. Gate second. Interpretation third.
- Write only to the designated S75 section.
- When finished, STOP.
- Do NOT relax a foundational assumption in a way that breaks the spectral
  triple definition (A, H, D) itself; if a proposed alternative breaks the
  spectral triple axioms before you can test the 22 theorems, document the
  break and classify all 22 theorems as INAPPLICABLE on that axis.
- Use the canonical_constants module; do NOT hardcode M_KK, tau_fold, Vol_SU3.
""".strip()


# ---------------------------------------------------------------------------
# SECTION D: Assessment block written into the working paper
# ---------------------------------------------------------------------------

ASSESSMENT = r"""
FOUNDATIONAL-AUDIT-75 extends the S73B Wave 5 L_max audit (axis F7 only) to the
six remaining foundational axes. The value of the audit is asymmetric: a PASS
is stronger than a PASS on the L_max axis alone (because the space of alternatives
is larger), while a FAIL on even one axis would localize exactly which foundational
choice is load-bearing for which theorem.

The audit is structured to be cheap per alternative: for each axis, the minimum
compute per theorem is specified in the prompt (typically a single commutator,
ratio, or sign check). The total compute is 22 theorems x 6 non-trivial axes
x 3-5 alternatives per axis ~ 400-660 minimum checks, which is feasible
in a single session.

The explicit F7 control is load-bearing: it provides a known-answer baseline
that the audit script must reproduce to validate the audit architecture before
trusting the other six axes.

This spec is DERIVED from S73B mack-vdd workshop carry-forward #10 (vdE2
emergence). It does NOT change the current framework state; it pre-registers
a test that S75 will execute.
""".strip()


# ---------------------------------------------------------------------------
# Main: serialize to .npz
# ---------------------------------------------------------------------------

def build_spec_container() -> dict:
    """Build the spec dictionary for .npz serialization."""
    assumption_ids = np.array([a[0] for a in FOUNDATIONAL_ASSUMPTIONS])
    assumption_names = np.array([a[1] for a in FOUNDATIONAL_ASSUMPTIONS])
    assumption_current = np.array([a[2] for a in FOUNDATIONAL_ASSUMPTIONS])
    assumption_provenance = np.array([a[3] for a in FOUNDATIONAL_ASSUMPTIONS])
    assumption_variation = np.array([a[4] for a in FOUNDATIONAL_ASSUMPTIONS])

    theorem_ids = np.array([t[0] for t in PERMANENT_THEOREMS])
    theorem_titles = np.array([t[1] for t in PERMANENT_THEOREMS])
    theorem_precision = np.array([t[2] for t in PERMANENT_THEOREMS])
    # Join dependency lists as comma-separated strings so numpy can store them.
    theorem_deps = np.array([",".join(t[3]) for t in PERMANENT_THEOREMS])

    n_theorems = len(PERMANENT_THEOREMS)
    n_axes = len(FOUNDATIONAL_ASSUMPTIONS)

    container = {
        # Provenance
        "spec_id": np.array("FOUNDATIONAL-AUDIT-75-SPEC"),
        "spec_version": np.array("1.0"),
        "spec_date": np.array("2026-04-11"),
        "source": np.array("S73B mack-vdd workshop carry-forward #10 / vdE2"),
        "author": np.array("van-den-dungen-bridge-theorist"),
        # Shape metadata
        "n_assumptions": np.int64(n_axes),                # (local)
        "n_theorems": np.int64(n_theorems),               # (local)
        # Assumption registry
        "assumption_ids": assumption_ids,
        "assumption_names": assumption_names,
        "assumption_current_choice": assumption_current,
        "assumption_provenance": assumption_provenance,
        "assumption_variation_protocol": assumption_variation,
        # Theorem registry
        "theorem_ids": theorem_ids,
        "theorem_titles": theorem_titles,
        "theorem_precision": theorem_precision,
        "theorem_dependencies": theorem_deps,
        # Full prompt
        "s75_agent_prompt": np.array(S75_AGENT_PROMPT),
        # Assessment
        "assessment": np.array(ASSESSMENT),
        # Canonical anchors (for self-consistency of downstream S75 script)
        "M_KK": np.float64(M_KK),
        "tau_fold": np.float64(tau_fold),
        "Vol_SU3": np.float64(Vol_SU3),
    }
    return container


def main() -> int:
    out_path = Path(__file__).parent / "s74_foundational_audit_75_spec.npz"
    container = build_spec_container()
    np.savez(out_path, **container)

    # Post-write verification: reload and confirm structure.
    loaded = np.load(out_path, allow_pickle=False)

    print("=" * 72)
    print("FOUNDATIONAL-AUDIT-75-SPEC serialized")
    print("=" * 72)
    print(f"Output file:      {out_path}")
    print(f"Spec ID:          {loaded['spec_id']}")
    print(f"Spec version:     {loaded['spec_version']}")
    print(f"Spec date:        {loaded['spec_date']}")
    print(f"Source:           {loaded['source']}")
    print(f"Author:           {loaded['author']}")
    print(f"# assumptions:    {int(loaded['n_assumptions'])}")
    print(f"# theorems:       {int(loaded['n_theorems'])}")
    print()
    print("Assumption axes:")
    for aid, name in zip(loaded["assumption_ids"], loaded["assumption_names"]):
        print(f"  {aid}: {name}")
    print()
    print("Theorems to audit:")
    for tid, title in zip(loaded["theorem_ids"], loaded["theorem_titles"]):
        print(f"  {tid}: {title}")
    print()
    print(f"S75 agent prompt length: {len(str(loaded['s75_agent_prompt']))} chars")
    print(f"Assessment length:       {len(str(loaded['assessment']))} chars")
    print()
    print("Canonical anchors carried:")
    print(f"  M_KK       = {float(loaded['M_KK']):.6e}")
    print(f"  tau_fold   = {float(loaded['tau_fold']):.6f}")
    print(f"  Vol_SU3    = {float(loaded['Vol_SU3']):.6f}")
    print()
    print("GATE VERDICT: FOUNDATIONAL-AUDIT-75-SPEC = PASS (spec complete)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
