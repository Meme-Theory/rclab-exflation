---
name: s117-lepto-pmns-joint-image
description: S117-W3-3 INFO — leptogenesis eps_1 and PMNS delta_CP co-sourced by one M_D phase but NON-independent; joint prediction DISSOLVED (delta_CP under-determined + eta_B K7-sourced)
metadata:
  type: project
---

S117-W3-3-LEPTO-PMNS-JOINT-IMAGE = **INFO** (sign=PASS / mag=INFO / regime=VALID). audit b3caaffac1768326. Final gate of the S117 Wave-3 lepton-CP chain (3-1→3-2→3-3 + 3-4). verdict-file L124-126.

**The structural [SIGN] content (sign=PASS, reusable):** with M_R real-diag B-branch (npz M_R_MKK=[1.0044,1.0786,1.1700]) and M_D=eps_LX^nu the sole phase source, the leptogenesis asymmetry eps_1(phi) and the PMNS Dirac phase delta_CP^PMNS(phi) are CO-SOURCED by one M_D off-diagonal phase phi but **NON-INDEPENDENT with DIFFERENT harmonic content**:
- eps_1(phi) propto Im[((M_D^dag M_D)_12)^2] = (Y2^2-Y3^2) w^2 sin(2phi) [Sage-exact, resid 4.55e-13] => period pi, **FOUR zeros** {0, pi/2, pi, 3pi/2}.
- |J_PMNS(phi)| vanishes ONLY at {0, pi} (=4.086e-3 at pi/2, 3pi/2) => period 2pi, **TWO zeros**. max|J|=4.086e-3 @ phi=pi/2 (delta_CP=238 deg).
- Shared zeros {0,pi}; eps_1 has EXTRA accidental zeros at {pi/2,3pi/2} (where ((Y dag Y)_12)^2 is real-negative). REFINES the plan's "both vanish at {0,pi}" oversimplification.

**m_1=0 does NOT kill delta_CP (reusable seesaw fact):** Y_1=0 (rank-2 M_D, S100a Casimir grading) => massless nu eigenvector = (1,0,0) EXACTLY for all phi (M_nu first row/col identically 0) => U_PMNS col-1 REAL, yet J_PMNS(phi)!=0. The Dirac phase lives in the complex 2-3 Takagi eigenvectors x the REAL U_eL gen-1 mixing. m_1=0 kills one MAJORANA phase, NOT the Dirac delta_CP. [[s116-lepton-pmns-texture]]

**Why INFO not PASS — the joint prediction is DISSOLVED (track_B):** the PASS reading "leptogenesis-sourced eta_B REQUIRES a DUNE-measurable delta_CP, a FALSIFIABLE joint prediction" is precluded at its root by the two upstream verdicts:
- 3-1 = INFO Scenario-III flat => delta_CP^PMNS UNDER-DETERMINED (substrate selects NO point on the joint curve; no predicted delta_CP to falsify).
- 3-2 = PASS-K7 => eta_B is K7-sourced (phi_CP^K7=pi/2, a DIFFERENT CP invariant per 3-4 RESOLVED dim=1 ORTHOGONAL dim=4), NOT leptogenesis-sourced => no eta_B<->delta_CP linkage.
DUNE measuring delta_CP LOCATES the free phase, it does NOT FALSIFY a linkage.

**Why INFO not FAIL:** a co-viable phi EXISTS (realisable — near phi~pi/2, eps_1 small but delta_CP large): at free physical kappa, rep phi=1.562 gives delta_CP=238.5 deg, eps=0.138, kappa_6e-10=1.31e-6 (SAME strong-washout ballpark as 3-2 K7 kappa_req=1.24e-6). delta_CP sweeps [6.3,353.7] deg on the off-{0,pi} branch. So NOT mutual-exclusion. The eta_B magnitude is efficiency-dependent (kappa free) AND scale oscillation-anchored PERMANENTLY ([[s100a-md-normalization]]) — not a zero-parameter prediction.

**Consistency note (NOT a prediction):** the joint curve passes delta_CP=238 deg at the J-max (phi=pi/2), inside NuFIT 3sig NO band [108,404] and near the central ~230 deg. phi free => consistency only.

**Cross-checks (all exact):** seesaw recon resid 0.0e+00; PMNS@phi=0 J=0, sin^2(th12,th23,th13)=(0.9956,0.0593,0.0087) bit-matches npz (angles S116-walled/under-determined but reproduced); |U_PMNS| mag-set match 1.26e-14.

**Constraint-map state after W3-3:** the entire lepton CP+mixing sector is under-determined on the substrate texture — angles WALLED (S116 mix_grp=0/4, [[s116_lepton_pmns_texture]] / [[s116_pmns_rescue]]), phase FLAT (S117 3-1), Majorana texture real (S60 internal eta_B=0). eta_B sourced by K7-transit (3-2), decoupled from leptonic delta_CP. Row #89 stays CONDITIONAL; capstone m_bb Row #80 inherits delta_CP-CONDITIONAL. Downstream routing -> mack (sole writer Row #89).

**How to apply:** when future neutrino-CP work asks "does the framework predict delta_CP?" the answer through S117 is NO — delta_CP is a free (flat) direction; the joint (eps_1, delta_CP) image is a real STRUCTURE/CONSISTENCY relationship, not a falsifiable pointwise prediction. The seesaw machinery (M_nu=M_D M_R^-1 M_D^T diag, rephasing-invariant Jarlskog from Hermitian M M^dag) is in computations/session-117/s117_lepto_pmns_joint_image.py — reuse it for any PMNS-phase scan.
