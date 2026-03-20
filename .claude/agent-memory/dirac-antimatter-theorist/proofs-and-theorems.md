# Proofs, Theorems, and Key Derivations

## T1: [J, D_K(s)] = 0 — CPT Exact (Session 17, PERMANENT)
- J = Xi*conj, Xi = [[0,-G5],[-G5,0]], G5 = diag of -gamma_5 column signs
- D on C^32 block-diagonal: D_+ on Psi_+, D_- = G5*conj(D_+)*G5 on Psi_-
- [J,D]=0 reduces to G5*conj(D_-)=D_+*G5. Substituting D_-: LHS=G5*G5*D_+*G5=D_+*G5=RHS
- Uses ONLY: G5^2=I, G5 real, G5 symmetric. Holds for ANY left-invariant metric.
- Numerical: max ||[D_K tensor I_32, I tensor Xi]|| = 0.00e+00 (exactly zero)
- Inner fluctuation extension: [J, D_phys]=0 algebraic identity (J^2=+1 only). PERMANENT.

## T2: Pfaffian Z_2 = +1 (Session 17c, PERMANENT)
- M(s) = Xi*D(s) antisymmetric (from [J,D]=0 + D anti-Hermitian)
- Pf changes sign iff det(D)=0 iff spectral gap closes
- (0,0) sector: 100 s-values, sgn(Pf)=+1 constant. Min gap: 0.8184 at s=0.2273
- All 28 sectors (p+q<=6): gap OPEN. Overall min gap: 0.8188. Z_2 trivial.

## T3: Spectral Pairing lambda <-> -lambda (Session 17c, PERMANENT)
- Two independent symmetries:
  1. Chirality: {gamma_9, D_pi}=0 maps lambda->-lambda WITHIN each sector
  2. Conjugate sectors: spec(D_{(p,q)}) = -spec(D_{(q,p)})
- 11,424 eigenvalues at 7 s-values. Max pairing error = 3.29e-13.

## T4: BdG Class = BDI, T^2=+1 (Session 17c, PERMANENT)
- C=J: C^2=+1. S=gamma_9: S^2=+1, {S,D}=0. T=C*S: T^2=+1 => CLASS BDI (not DIII)
- Z_2 at d=0 for both BDI and DIII, so Pfaffian valid either way
- Consequence: no protected Majorana zero modes from topology. nu_R mass from Yukawa.

## T5: D_K Block-Diagonal in Peter-Weyl (Session 22b, 3 proofs, PERMANENT)
- D_K exactly block-diagonal. Proven at 8.4e-15.
- Holds for ANY left-invariant metric on compact Lie group.

## T6: Perturbative Exhaustion (Session 22c L-3, PERMANENT)
- H1-H5 verified. F_pert not true free energy. All perturbative mechanisms closed.

## T7: Chirality-Graded Spectral Action = 0 (Session 25, PERMANENT)
- Tr(gamma_9 * f(D_K^2/Lambda^2)) = 0 identically (from BDI spectral pairing)
- Thermal graded sum is the viable alternative.

## T8: Trap 4 — Inter-Branch Decoupling (Sessions 32-33, PERMANENT)
- V_eff(B_i, B_j) = 0 exactly (Schur orthogonality between U(2) branches)
- Extended to full U(2)-invariant submanifold. Any U(2)-equivariant perturbation.

## T9: Trap 5 — Partial (Session 33 W1, PARTIALLY PERMANENT)
**Proven (NCG axioms, KO-dim 6):**
- M_ph purely imaginary for real reps. 4-step proof:
  1. J antilinear with J^2=+1 => J-eigenbasis where all ops become real
  2. gamma_9 in J-basis: IMAGINARY ANTISYMMETRIC (from J*gamma_9=-gamma_9*J)
  3. delta_D in J-basis: REAL SYMMETRIC (from [J,delta_D]=0)
  4. M_ph = v^dag*gamma_9*delta_D*v, v real => M_ph*=-M_ph => M_ph in iR
**NOT proven:** M_ph=0 from abstract axioms. 4 independent routes all give M in iR only.
**Numerical:** B1=0 (trivial), B3=0 (<10^-14, analytically OPEN), B2=4.24 (complex rep escapes)

## T10: QGT Selection Rule (Session 33 W1, with Berry)
- Berry curvature Omega=0 for ALL branches on U(2)-invariant submanifold
- Quantum metric g>=0 (generically nonzero)
- Spectral action curvature from quantum metric ONLY, restricted to B2
- Berry curvature generically nonzero along U(2)-breaking T3/T4 for B2

## T11: J-Symmetry for Arbitrary Left-Invariant Metric on SU(3) (Session 43 W5-1, PERMANENT)
- C_2*conj(D_K)*C_2 = D_K for ANY left-invariant metric, not just Jensen.
- Proof: conj(gamma_a) = s_a*gamma_a, C2*gamma_a*C2 = t_a*gamma_a, t_a = -s_a for ALL a.
  Connection coefficients Gamma^b_{ac} are real. Triple product sign: (s_a*t_a)^3 = (-1)^3 = -1.
  C2*conj(Omega)*C2 = -Omega. D_K = i*Omega => C2*conj(D_K)*C2 = D_K.
- Extends T1 from Jensen 1D to full 36D moduli space of left-invariant metrics.
- spec(D_{(p,q)}) = spec(D_{(q,p)}) verified to 2e-15 on random non-diagonal metric.
- CLOSES ALL internal baryogenesis via J-breaking (Jensen + off-Jensen + arbitrary).
- {gamma_9, D_pi} = 0 also holds for all left-invariant metrics (spectral pairing preserved).

## Permanence Hierarchy
- **Layer 1 (NCG permanent):** T1-T4, T7, T9-proven, T10, T11
- **Layer 2 (SU(3)+U(2)):** T5, T6, T8, fold stability (Thom A_2), gamma_9 branch preservation
- **Layer 3 (numerically verified, analytically open):** T9-numerical (B3=0)

## Key Equations

### KO-dimension 6 conditions
J^2=+I (eps=+1), JD=DJ (eps'=+1), J*gamma=-gamma*J (eps''=-1)

### Xi construction (Baptista eq 2.12)
gamma_5=diag(1,1,-1,-1), G5[k]=-gamma_5[col(k)], Xi=[[0,-G5],[-G5,0]], J=Xi*conj

### Dirac operator per sector
D_pi(s) = sum_{a,b} E_{ab}(s)*[rho_pi(X_b) tensor gamma_a] + I tensor Omega(s)

### Jensen metric
g_s = e^{2s}*g_0|_{u(1)} + e^{-2s}*g_0|_{su(2)} + e^s*g_0|_{C^2}
Volume: e^{2s}*(e^{-2s})^3*(e^s)^4 = 1 (preserved)

### Clifford conventions
gamma_{2k-1} REAL, gamma_{2k} IMAGINARY

### Pfaffian
M(s) = Xi*D_F(s), antisymmetric if [J,D]=0. sgn(Pf(M(s))) = Z_2 invariant.
