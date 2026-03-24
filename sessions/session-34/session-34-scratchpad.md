# Session 34 Investigation Scratchpad

**Date**: 2026-03-06
**Focus**: D_phys spectrum, mechanism chain survival, 11% BCS shortfall hunt

---

## Timeline

### Wave 1: Session 34a Team (bap, connes, coord)

**DPHYS-34a-1: PASS** — B2 fold survives inner fluctuations. d2 = 1.226 at phi=gap (increases from bare 1.176). Fold stabilized, not weakened. 10/13 generator directions preserve fold. Destroyed at |phi|=0.18. Not Strong Pass.

**TRAP1-34a: CONFIRMED** — V(B1,B1) = 0 exact at all 9 tau, all 8 generators. Representation-theoretic (U(2) singlet). Permanent structural result.

**J operator correction** — C2 = gamma_1*gamma_3*gamma_5*gamma_7 is the correct charge conjugation (not B = sigma_2^{x4}). No upstream impact on mechanism chain. Prior J was wrong but never used in chain computations.

### Serial Baptista Computations

**DPHYS-34a-2: PASS** — Kosmann kernel reprojected into D_phys eigenbasis. V(B2,B2) = 0.086 at phi=gap (+50% over bare 0.057). Pairing enhanced, not weakened. U(1) generator dominant (63%).

**RPA-34a: CONSISTENT** — Spectral action curvature = 180.09 at phi=gap (8.82x bare, 333x over threshold). Monotonically increasing with phi. The fold concentrates curvature at the dump point.

**DPHYS-34a-3: FAIL** — M_max = 0.899 < 1.0 at all phi for all walls. The spinor-basis Kosmann kernel V(B2,B2) = 0.057 is insufficient for Thouless instability.

**CRITICAL UPSTREAM**: TRAP-33b RETRACTED. Session 33b used A_antisym (frame-space structure constants, V=0.287) instead of K_a_matrix (spinor matrix elements, V=0.057). These are different mathematical objects — frame indices ≠ eigenspinor indices. Tesla validation confirmed: Schur's lemma locks V(B2,B2) in spinor basis, frame V exceeds the Casimir spectral bound.

### Tesla Validation

Independent verification of DPHYS-34a-3. M_max = 0.902 confirmed. Schur's lemma: B2 carries irreducible rep of Kosmann algebra (all 4 Casimir eigenvalues = 0.1557). M_max is basis-independent to 5e-15 over 1000 random U(4) rotations.

---

## The 11% Hunt

### M_max = 0.902 vs threshold 1.0 (shortfall 10.9%)

### Tesla 11% Hunt (s34a_tesla_11pct.py)
- Van Hove smooth-wall DOS: rho_smooth ≈ 6.8-7.2 per mode (script), summary over-claimed 20.5/3.8x
- CT-4 impedance overcounting: T_branch = 0.998 → impedance should be ~1.0, not 1.56
- Combined: Tesla summary claimed M_max = 2.2-3.4, script gives ~0.95 van Hove alone

### QA 11% Hunt (s34a_qa_11pct.py)
- Van Hove: agrees with Tesla script (~6.8-7.2 per mode, ~25-33% enhancement)
- Chemical potential mu=0.083: trivially closes gap (M_max >> 1)
- Beyond-mean-field: AL+MT with N_eff=4, O(25%) correction, UNCOMPUTED
- BCS bootstrap: impossible (contraction mapping theorem)
- Full 16x16: only +1.4% from B3 cross-coupling

### MU-35a (Connes agent, s35a_mu_physical_basis.py): FAIL
- PH symmetry of D_K is EXACT ({gamma_9, D_K} = 0)
- dS/dmu|_{mu=0} = 0 PROVEN analytically for any PH-symmetric spectrum
- mu = 0 forced by canonical spectral action
- **BUT**: D_phys can break PH via inner fluctuations
- **AND**: grand canonical spectral action (van Suijlekom) with U(1) charge as N is a different object

---

## Key Insight: U(1) Charge as Number Operator

The Jensen deformation breaks SU(3) → U(2) = SU(2) × U(1). This provides:

1. **A conserved U(1) charge** — the hypercharge generator K_7
2. **Integer eigenvalues on branches**: B1(0), B2(±1), B3(0)
3. **A number operator N = K_7** for the grand canonical ensemble

The van Suijlekom formalism (Connes 16, arXiv:1903.09624) extends spectral action to:
  Z(beta, mu) = Tr exp(-beta(H - mu*N))
with N = particle number operator. K_7 IS such an operator.

The connes agent's PH proof used the CANONICAL spectral action S = Tr f(D^2/Lambda^2). The GRAND CANONICAL S(beta, mu) with N = K_7 charge is a different mathematical object. PH symmetry of D_K forces dS_canonical/dmu = 0, but the grand canonical free energy F = E - TS - mu*N has a mu-dependent minimum set by the charge distribution, not by PH.

### Physical picture
- Jensen deformation creates crystal field splitting → branches with U(1) quantum numbers
- Domain wall traps modes → local occupation → conserved charge in finite region
- Conserved charge + spectral gap → chemical potential (textbook semiconductor physics)
- The Fermi level sits inside the B2-B1 gap, not at zero

### What needs computing
- K_7 eigenvalues on the D_K eigenspinors (are they really ±1 on B2?)
- Grand canonical spectral action S(beta, mu) with N = K_7 at the wall
- Self-consistent mu from minimizing the grand canonical free energy
- M_max(mu_self_consistent) — does it cross 1.0?

---

## Literature Discovery

### Finite-density spectral action EXISTS in published literature

**Connes 15** (arXiv:1809.02944): Chamseddine, Connes, van Suijlekom. "Entropy and the Spectral Action." CMP 365, 707-721, 2019.
- Von Neumann entropy = spectral action (exact)
- Connection to Riemann zeta function
- Foundation for finite-density extension

**Connes 16** (arXiv:1903.09624): Dong, Khalkhali, van Suijlekom. "Second Quantization and the Spectral Action." JNCG 16, 567-603, 2022.
- Grand canonical Z(beta, mu) as spectral action
- Coefficients: modified Bessel functions I_nu
- Axioms preserved under finite-density extension
- Key formula: H_eff = H - mu*N, Z = Tr exp(-beta*H_eff)

**Gap in literature** (original contribution opportunity):
- Nobody has applied finite-density spectral action to BdG/BCS systems
- Nobody has computed it on compact internal spaces (SU(3))
- Nobody has used U(1) isometry charge as the number operator N
- This would be the FIRST application

---

## VH-IMP-35a: Van Hove + Impedance Arbitration (Script 1)

### Gate: PASS (M_max = 3.32 reported, but V-matrix concern)

**Van Hove** (RELIABLE):
- rho_per_mode = 14.02 at physical v_min = 0.012 (2.6x over step 5.40)
- Fold at tau_fold = 0.190 has v_B2 = 0 (1D van Hove singularity)
- Physical cutoff: v_min = 0.0117 (Delta_E_wall / w_wall, most conservative valid estimate)
- Critical v_min for M=1: 0.085 (7.2x safety margin)

**Impedance** (RELIABLE):
- T_branch = 0.998 (B2 spectral weight conserved within branch)
- Cross-branch leakage: < 10^{-28} (B1), < 10^{-29} (B3)
- CT-4 impedance 1.56 is OVERCOUNTED — physical impedance ≈ 1.0
- The "reflection" R=0.64 is intra-B2 basis rotation, not inter-branch scattering

**M_max** (NEEDS V-MATRIX CHECK):
- Reported M_max = 3.32 — cross-check reproduces TRAP-33b (2.06), suggesting A_antisym used
- Corrected estimate with K_a_matrix: M_max ≈ 0.902 × (14.67/8.81) = 1.50
- KK agent tasked with independent validation using explicitly verified K_a_matrix

### Corrected rho flow
```
rho_step = 5.40 (W-32b)
× multi-sector 1.046 = 5.65
× impedance 1.56 (CT-4) = 8.81 ← DPHYS-34a-3 baseline

Corrected:
rho_smooth = 14.02 (van Hove)
× multi-sector 1.046 = 14.67
× impedance 1.0 (corrected) = 14.67

Net: 8.81 → 14.67 (1.66x increase)
M_max: 0.902 → ~1.50 (linear scaling)
```

---

## Open Computations (as of this writing)

| Agent | Task | Status |
|:------|:-----|:-------|
| KK | Validate M_max with correct K_a_matrix at 4 rho scenarios | RUNNING |
| QA | Script 2: beyond-mean-field corrections | RUNNING |
| Connes | Evaluate U(1) charge as N in grand canonical spectral action | QUEUED |

---

## Assessment

The mechanism chain has three potential rescue paths, any one of which may close the 11%:

1. **Van Hove + impedance correction** (Script 1, KK validating): rho 8.81 → 14.67, M_max 0.90 → ~1.50. MOST LIKELY rescue. Needs K_a_matrix V confirmation.

2. **Beyond-mean-field fluctuations** (Script 2, QA computing): N_eff=4, Gi=0.25, fluctuation propagator L=10.2. Could add ~10-25% to M_max. UNCOMPUTED.

3. **Grand canonical spectral action with U(1) charge** (Connes queued): Jensen deformation provides N = K_7. Published formalism exists (Connes 15/16). First application to BdG/BCS on internal space. Could provide the PHYSICAL ORIGIN for mu that closes the gap through different physics.

The self-correcting pattern continues: TRAP-33b was wrong (frame V), DPHYS-34a-3 caught it but used step-function wall DOS. The correct computation needs smooth-wall van Hove + corrected impedance + correct spinor V. The framework keeps revealing its own errors and the corrections keep pointing to a narrow corridor of viability.
