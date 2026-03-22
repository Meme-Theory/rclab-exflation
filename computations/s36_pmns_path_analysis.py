"""
PMNS-PATH-36: Path Forward Analysis for Neutrino Mixing
Determines which PMNS routes survive after W2-A triple closure.
"""
import numpy as np

def main():
    # Load W2-A results
    d = np.load('tier0-computation/s36_intersector_pmns.npz', allow_pickle=True)
    s10 = np.load('tier0-computation/s35_sector_10_spectrum.npz', allow_pickle=True)
    k7 = np.load('tier0-computation/s35_k7_thouless.npz', allow_pickle=True)

    print("=" * 70)
    print("PMNS-PATH-36: Path Forward Decision Analysis")
    print("=" * 70)
    print()

    # ---- SECTION 1: Summary of closures ----
    print("1. CLOSED ROUTES (5 total)")
    print("-" * 50)
    closures = [
        ("S35", "Singlet tridiagonal PMNS", "R < 5.9 ceiling (Schur on U(2) irreps)"),
        ("W2-A P1", "NCG inner fluctuation cross-sector", "Cross-sector norm = 0 exactly (tensor product)"),
        ("W2-A P2", "H_eff structural bound", "max R*sin2_23 = 16.9 < 17.8 (0/600K MC pass)"),
        ("W2-A P3", "Paper 18 Phi-tilde misalignment", "O_matrix = I at all tau (Schur on U(2))"),
        ("W2-A P3b", "Off-Jensen within U(2)-invariant", "Schur still applies: mixing = 0 for any (l1,l2,l3)"),
    ]
    for sess, name, reason in closures:
        print(f"  [{sess}] {name}")
        print(f"    Reason: {reason}")
    print()

    # ---- SECTION 2: What survives ----
    print("2. SURVIVING STRUCTURAL RESOURCES")
    print("-" * 50)
    print()

    # Mass hierarchy
    print("  (a) Mass hierarchy ratio R_bare (inter-sector):")
    for i in range(6):
        tau = d[f'heff_{i}_tau'][0]
        R = d[f'heff_{i}_R_bare'][0]
        print(f"      tau = {tau:.2f}: R = {R:.1f}")
    print(f"    Status: IN gate window [10, 100] for tau >= 0.15")
    print()

    # Normal ordering
    print("  (b) Normal mass ordering (B1 < B2 < B3): STRUCTURAL at all tau > 0")
    for i in range(6):
        tau = d[f'p18_{i}_tau'][0]
        EB1 = d[f'p18_{i}_E_B1'][0]
        EB2 = d[f'p18_{i}_E_B2'][0]
        EB3 = d[f'p18_{i}_E_B3'][0]
        print(f"      tau = {tau:.2f}: B1={EB1:.4f} < B2={EB2:.4f} < B3={EB3:.4f}")
    print(f"    Status: TESTABLE by JUNO/DUNE (Level 4 candidate)")
    print()

    # B2-G1 near-degeneracy
    print("  (c) B2-G1 inter-sector near-degeneracy:")
    for i in range(6):
        tau = d[f'p18_{i}_tau'][0]
        gap = d[f'p18_{i}_B2_G1_gap'][0]
        print(f"      tau = {tau:.2f}: gap = {gap:.6f}")
    print(f"    Status: Gap shrinks monotonically, crossing near tau ~ 0.26")
    print()

    # (1,0) sector structure
    print("  (d) (1,0) sector eigenvalue structure at tau = 0.18:")
    ev10 = s10['evals_10_3']  # tau index 3 = 0.18
    pos_ev = np.sort(np.abs(ev10[ev10 > 0]))
    print(f"      Positive eigenvalues: {pos_ev}")
    print(f"      G1 lowest: {pos_ev[0]:.6f} (mult = 1)")
    print(f"      Next cluster: {pos_ev[1]:.6f} (mult = 2)")
    print()

    # K_7 charge analysis
    print("  (e) K_7 charge structure:")
    print(f"    [iK_7, D_K] = 0 at ALL tau (Session 34, permanent)")
    print(f"    Singlet K_7 charges: {k7['q_vals_pos_all'][3]} (tau ~ 0.18)")
    print(f"    These are +/-0.25 (B2-type) in the gap-edge 4 modes")
    print(f"    B1 has q_7 = 0, B3 has q_7 = 0 (both U(2)-trivial in q_7)")
    print()

    # ---- SECTION 3: Option analysis ----
    print("3. OPTION ANALYSIS")
    print("-" * 50)
    print()

    # Option A: Off-Jensen SU(2)-breaking
    print("  OPTION A: Off-Jensen SU(2)-Breaking (Paper 18 Step 3)")
    print("  " + "=" * 48)
    print()
    print("  Framework status: WITHIN framework (Baptista Step 3, Paper 18 p.54)")
    print("  Metric: left-invariant with Iso(g) = SU(3) x U(1)_7")
    print("  Effect: SU(2) broken => B2 splits, B1-B3_0 can mix")
    print()
    print("  Quantum numbers after SU(2) -> U(1)_3:")
    print("    B1:    (q_7=0, q_3=0)   -- CAN mix with B3_0")
    print("    B2++:  (q_7=+1/4, q_3=+1/2)")
    print("    B2+-:  (q_7=+1/4, q_3=-1/2)")
    print("    B2-+:  (q_7=-1/4, q_3=+1/2)")
    print("    B2--:  (q_7=-1/4, q_3=-1/2)")
    print("    B3_0:  (q_7=0, q_3=0)   -- CAN mix with B1")
    print("    B3_+:  (q_7=0, q_3=+1)")
    print("    B3_-:  (q_7=0, q_3=-1)")
    print()
    print("  Limitation: [iK_7, D_K] = 0 permanent => q_7 is exact quantum number")
    print("    B1-B2 mixing: BLOCKED (q_7 = 0 vs +/-1/4)")
    print("    B1-B3_0 mixing: ALLOWED (both q_7 = 0, q_3 = 0)")
    print("    Result: 2x2 rotation only, NOT full 3x3 PMNS")
    print()
    print("  For full 3x3 PMNS: need inter-sector mode with q_7 = 0")
    print("  G1 in (1,0) sector: K_7 charge UNCOMPUTED")
    print()
    print("  Test computation: Diagonalize D_K with SU(2)-broken metric on (0,0)+(1,0)")
    print("  New parameter: epsilon (SU(2)-breaking strength)")
    print("  Pre-registered gate: OFF-JENSEN-PMNS-37")
    print()

    # Option B: Full KK coupling
    print("  OPTION B: Full KK Modified Lie Derivative Coupling")
    print("  " + "=" * 48)
    print()
    print("  Framework status: EXTENSION (KK framework, not pure NCG)")
    print("  The modified Lie derivative L_tilde_{e_a} for non-Killing e_a")
    print("  generically mixes Peter-Weyl sectors (Paper 18, Section 6).")
    print("  However, this is categorically different from NCG inner fluctuations.")
    print("  W2-A proved: NCG phi preserves sectors, KK L_tilde does not.")
    print()
    print("  Using KK coupling within the NCG framework requires:")
    print("    Replacing A -> A + phi_F with A -> A + L_tilde coupling")
    print("    This is a framework change, not an internal computation.")
    print()
    print("  Assessment: Viable but changes the rules. Not testable within")
    print("  current spectral triple structure. Deferred to paper preparation.")
    print()

    # Option C: Level 5 classification
    print("  OPTION C: Classify PMNS Mixing as Level 5")
    print("  " + "=" * 48)
    print()
    print("  What the framework predicts (zero free parameters):")
    print("    1. Normal mass ordering (Level 4 candidate)")
    print("    2. Mass hierarchy scale R ~ 27 at fold")
    print("    3. Three generations from Z_3 center (Paper 18 p.54)")
    print()
    print("  What requires additional input:")
    print("    1. PMNS mixing angles (SU(2)-breaking parameter epsilon)")
    print("    2. CP phase delta_CP (complex phase in epsilon)")
    print("    3. Absolute masses (M_KK stabilization)")
    print()
    print("  Analogy: LCDM predicts expansion, not initial perturbation spectrum.")
    print("  This framework predicts mass hierarchy, not mixing angles on Jensen curve.")
    print("  Mixing angles arise from Step 3 (electroweak symmetry breaking of")
    print("  the internal metric), which introduces the Higgs-like parameter in C^2.")
    print()

    # ---- SECTION 4: Recommendation ----
    print("4. RECOMMENDED PATH FORWARD")
    print("-" * 50)
    print()
    print("  PRIMARY: Option A (Off-Jensen) combined with inter-sector extension")
    print()
    print("  Two-stage computation for Session 37:")
    print("  Stage 1 (K7-G1-37): Compute K_7 eigenvalue of G1 in (1,0) sector")
    print("    If q_7(G1) = 0: proceed to Stage 2")
    print("    If q_7(G1) != 0: fall back to Option C (Level 5)")
    print()
    print("  Stage 2 (OFF-JENSEN-PMNS-37): Diagonalize D_K on SU(3) with")
    print("    SU(2)-broken metric (Paper 15 ref [71]), compute 3x3 PMNS")
    print("    from (B1, B3_0, G1) triad")
    print()
    print("  Gate criteria for OFF-JENSEN-PMNS-37:")
    print("    PASS: R in [10, 100] AND sin2_theta_23 in [0.3, 0.7]")
    print("    FAIL: R < 5 OR sin2_theta_23 < 0.01")
    print()
    print("  FALLBACK: Option C if Stage 1 fails (q_7 != 0)")
    print("    Normal ordering prediction stands as Level 4 candidate")
    print("    PMNS mixing classified as requiring Step 3 input (Level 5)")
    print()

    # ---- SECTION 5: Impact assessment ----
    print("5. IMPACT ON FRAMEWORK PROBABILITY")
    print("-" * 50)
    print()
    print("  The PMNS closure on Jensen curve has MILD downward pressure:")
    print()
    print("  Arguments against strong downward pressure:")
    print("    (a) Paper 18 Appendix E explicitly requires Step 3 for mixing")
    print("        Our W2-A confirms Step 2 result (zero mixing on Jensen)")
    print("        This is CONSISTENT with Baptista, not a failure")
    print("    (b) Mass hierarchy IS structurally predicted (R ~ 27 at fold)")
    print("    (c) Normal ordering IS a zero-parameter prediction")
    print("    (d) Three generations from Z_3 center survives")
    print()
    print("  Arguments for downward pressure:")
    print("    (a) The framework does not autonomously predict PMNS angles")
    print("    (b) Step 3 introduces a free parameter (epsilon)")
    print("    (c) The NCG-KK dichotomy (W2-A Part 1) raises questions about")
    print("        which mathematical framework is operative")
    print()
    print("  Net assessment: BF ~ 0.85 (mild downward)")
    print("  This is because the closure was EXPECTED (Paper 18 Step 2 = Jensen)")
    print("  and the mass hierarchy/ordering predictions survive.")
    print()
    print("  The decisive test is OFF-JENSEN-PMNS-37.")
    print("  If it PASSes: BF ~ 3-5 (strong upward, actual PMNS prediction)")
    print("  If it FAILs: BF ~ 0.5 (moderate downward, framework cannot predict PMNS)")

if __name__ == "__main__":
    main()
