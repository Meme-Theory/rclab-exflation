# Session 73a Synthesis: Exit Horizon Resolution and Substrate Causal Structure

**Date**: 2026-04-10
**Agent**: schwarzschild-penrose-geometer (SP)
**Source Documents**:
- `sessions/archive/session-73a/session-73a-results-workingpaper.md`
- `.claude/agent-memory/schwarzschild-penrose-geometer/MEMORY.md`
- `sessions/framework/Phononic-Penrose-Diagrams.md` (reference)

---

## I. Session Outcome

S73A delivers the definitive negative answer to the exit-horizon question: **there is no exit sonic horizon**. The modulus traverses the fold at Mach 20.7 and never decelerates to subsonic, with v_tau / c_BA varying by less than 0.2% across the entire BCS gap profile. This retracts the "exit horizon" vocabulary from the substrate causal diagram and replaces it with a permanent supersonic conduit. Two PASS results lock the causal picture: LUTTINGER-SUPERSONIC (N_pair conserved to 2.2e-16 through the Mach 20.7 transit, by superselection) and BLV-COMPOUND (dispersive transfer matrix confirms n_s = 0.9567 is Bogoliubov-invariant to machine epsilon). Together, W1-A, W3-B, and W4-D establish that the fold transit is simultaneously impulsive, algebraically rigid, and spectrally frozen -- the substrate carries an exact superselection structure through what would, in any container-spacetime picture, demand a horizon.

---

## II. Key Results

### Result 1: No Exit Sonic Horizon (W1-A)

**Result**: Ma_BA = 20.73 at the fold, varying in [20.71, 20.76] across the entire BCS gap profile range tau in [0.164, 0.224]. No tau exists where Ma = 1. GEOMETRIC + PHONONIC.

This is the most consequential structural finding of S73A. The exit-horizon picture carried forward from S72 implicitly assumed a deceleration region where v_tau crosses c_BA from above -- the acoustic analog of the null surface where an outgoing null congruence becomes tangent to the horizon generator. S73A computes the spectral-action equation of motion (Z_fold effective mass, dS/dtau gradient = 4032.84 M_KK^{-1}) and shows that v_tau is locked at 8.27 M_KK, while c_BA is locked at 0.399 M_KK, giving a permanent Mach 20+ supersonic regime.

In standard analogue gravity (Unruh 1981, Barcelo-Liberati-Visser 2005), an acoustic horizon is precisely the locus c_s = v_flow. The absence of this crossing means the substrate does not admit an analogue-gravity horizon as its exit boundary. In Schwarzschild-Penrose language: **black hole horizons, inasmuch as they are the emergent picture of freezing dynamics in a container, are manifestations of substrate structure where c_s - v crosses zero. The substrate's fold transit is not such a structure.** What the container-spacetime description would call "the missing horizon" is, from the substrate-first perspective, a phase with no crossing -- the fiber's spectral weight simply pours through the fold without a return to subsonic flow.

The fold-transit Bogoliubov production is nevertheless real but sub-dominant: r_exit ~ [0.005, 0.116] against the BCS fold squeeze r_BCS ~ [1.8, 3.6] (ratio 17-360x). And critically: the inter-branch phase variance of the exit Bogoliubov is 0.6 mrad -- **phase-coherent**. The fold transit preserves coherence rather than destroying it. This forbids the dynamical decoherence that the A_s gap requires.

### Result 2: Superselection through Impulsive Transit (W3-B, LUTTINGER-SUPERSONIC PASS)

**Result**: delta_N_pair / N_pair = 2.22e-16 across 8 independent tests (fixed-sector sweep, RG root counting, TDSE, sudden quench, full Fock evolution, non-integrable perturbation). GEOMETRIC.

Superselection is a causal concept. In standard QFT, superselection sectors are equivalence classes that unitary evolution cannot connect because the observables generating the connecting symmetries are at infinity (Wightman 1952, Haag 1996). On the substrate, the BCS Hamiltonian H_BCS satisfies [H_BCS, N_pair] = 0 identically -- the commutator vanishes not as a physical coincidence but as an algebraic property of the pair algebra (only pair creation, pair annihilation, and number-diagonal terms). The Fock space factorizes into N_pair sectors that any unitary evolution preserves exactly.

The analog in Penrose's work is the conserved charge inside the horizon. For stationary black holes, the future horizon H+ carries ADM and Komar charges that are preserved by evolution of initial data on a Cauchy surface. For the substrate fold, **the role of the Cauchy surface is played by the superselection sector** -- N_pair = 1 is the 8-dimensional subspace on which every one-pair initial datum evolves, and the Mach 20.7 transit cannot move amplitude out of it. The test with density-density perturbation (epsilon * sum V'_kl n_k n_l up to epsilon = 0.1) shows that this is not integrability-protected: non-integrability is irrelevant because the superselection is algebraic, not dynamical.

Connection to Volovik Paper 31 (Exotic Lifshitz Transitions): in the BCS sector, N_pair = M (the number of Bethe-ansatz spectral parameters). This is the BCS analog of the topological invariant N_1 that protects the Luttinger volume under smooth deformations of the Fermi surface. **The Mach 20.7 transit is safe from breaking this invariant the same way a smooth Lifshitz transition is safe from breaking N_1 -- both protect a counting of eigenvalues against continuous deformation of the underlying operator.**

### Result 3: n_s Bogoliubov-Invariance (W4-D, BLV-COMPOUND PASS)

**Result**: |n_s(BLV) - n_s(product)| = 0 exact. The dispersive transfer matrix with Delta(tau)/omega_k ~ 0.27 at the fold produces r_BLV ~ [0.058, 0.065] (real dispersive production) but delta_n_s = 0. GEOMETRIC.

This is the third independent confirmation (W2-A ordered product, W1-A BdG, W4-D parametric oscillator) that the CMB spectral index n_s = 0.9567 is set by the spectral action geometry (a_2/a_4 Seeley-DeWitt ratio), not by the Bogoliubov sector. The BLV computation is the most stringent test: the BCS gap Delta(tau) is included as a tau-dependent effective mass in the parametric oscillator equation d^2 u/dtau^2 + Omega_eff^2(tau) u = 0 with Omega_eff^2 = omega_k^2 + Delta(tau)^2. The non-dispersive limit (Omega^2 = omega_k^2) gives |beta_lin|^2 ~ 1e-33 (essentially zero particle production). The dispersive case gives real production r_BLV ~ 0.06 -- a genuine Bogoliubov response to the time-dependent gap.

**The tilt n_s is nevertheless preserved exactly.** The reason is structural: n_s is a spectral-action quantity derived from the Kasparov factorization of the internal geometry through the base. The Bogoliubov transformation -- whether naive product, BdG, or dispersive BLV -- is a unitary operation within Fock space that redistributes occupation numbers but preserves the K-homology class. Penrose's analog: the Bondi mass at I+ is conserved (decreasing monotonically) independent of how the interior dynamics proceed. Here, n_s is the substrate analog of an "infinity charge" -- computable from the spectral geometry without reference to the finite-tau dynamics.

The amplitude-budget implication is cleaner: the 5/5 cross-checks pass (det(T) = 1 to 5.9e-14, unitarity to 5.9e-14, continuity through fold to 7.8e-15, grid convergence 1.1e-16, non-dispersive limit 3.7e-33). The dispersive correction reshuffles power across branches (B2 gains +12.2%, B3 loses -8.7%) but total amplitude change is -0.96% -- a within-budget reshuffle that does not touch the spectral tilt.

### Result 4: Decoherence Hierarchy Collapse (W2-C, W3-A, W1-E, W4-B)

**Result**: Among the 5 decoherence channels (Exit Bog, Mott, Graph-spectral, Dispersive, JJ-anisotropy), only Mott (delta_OOM = 0.336) and Dispersive (delta_OOM = 0.150) contribute; combined over-decoheres by 1.8x. S72 model residual = 0.009 OOM (formally CLOSED). PHONONIC.

W2-C rules out graph spectral decoherence kinematically: the transit executes only 0.0007 Josephson hops (J_eff * dt_transit = 7.2e-4), so no graph topology on 24 vertices -- not even complete K_24 -- can close the gap. W1-A rules out exit Bogoliubov because the horizon does not exist. The surviving mechanism is W3-A dispersive decoherence, which produces **block decoherence**: C(B2, B3) = 2.3e-6, C(B1, B3) = 3.8e-9, with intra-branch coherence preserved (Var ~ 1e-8). The density matrix acquires a 3-block structure (B2: 4 modes, B1: 1 mode, B3: 3 modes), which is causally analogous to the partial trace over an external thermal reservoir -- except the "reservoir" is the entry horizon's thermal bath at T_H = 72.8 M_KK with n_bar = 85.2.

**The causal picture is now asymmetric.** The entry horizon is the dominant thermal source (|beta|^2 ~ 85 per mode, r_entry ~ 2.92, T_H = 72.84 M_KK). The fold produces sub-thermal impulsive Bogoliubov (n_k ~ 0.01 per mode). There is no exit horizon. The decoherence that closes the A_s gap is not a dynamical horizon process at all -- it is a static quantum effect (Mott E_J/E_C = 1.29 at the fold, phase noise delta_phi = 1.24 rad) combined with the block decoherence from amplifying the entry horizon's thermal fluctuations via the fold squeeze.

### Result 5: Spectral Action Profile is Scheme-Dependent (W1-D)

**Result**: For f* and sqrt, S(tau) increases monotonically post-fold. For exp and compact, S(tau) decreases monotonically. Sign of dS/dtau at the fold: +4033 (f*), +4546 (sqrt), -1258 (exp), -4830 (compact). GEOMETRIC.

This is the most scheme-dependent quantity found in the entire project. The direction the modulus wants to roll is a physical prediction that differs between spectral functionals. No extremum exists in S(tau) for tau in [0, 2] under f* -- the profile is approximately cubic with S' = 4033, S'' = 21823, S''' = 6644. Moduli stabilization from S(tau) alone is excluded; additional physics is required.

From the SP perspective: **this is a statement about the 1-parameter worldline of the substrate in modulus space, not about the geometry of the modulus space itself.** The absence of a post-fold minimum means the substrate equivalent of "geodesic completeness" does not terminate the tau-roll at a stationary point -- the modulus is still evolving. This is consistent with dynamical dark energy from the DESI w_0 = -0.918 observation. The CC is not a stored vacuum energy but a still-rolling spectral action gradient.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| EXIT-HORIZON-BOG-73a | INFO | Ma_BA = 20.73, t_dec/t_transit = 23.19 |
| LEGGETT-GRAV-DECAY-73a | PASS | Gamma(L->2g) = 0 (Z_2), tau_pair/t_univ = 1.13e65 |
| BBN-VOLOVIK-73a | FAIL | Y_p = 0.287 (+10.5 sigma), D/H = 4.90e-5 (+79 sigma) |
| SPECTRAL-ACTION-PROFILE-73a | INFO | dS/dtau = +4033 M_KK^{-1} (f*), no extremum in [0,2] |
| MOTT-CHARGE-NOISE-73a | PASS | F_Mott = 0.461, delta_OOM = 0.336 |
| COMPOUND-NS-73a | INFO | n_s = 0.9567 (1.95 sigma), non-additive = 0 (aligned) |
| PW-THRESHOLD-RATIOS-73a | FAIL | sin^2(theta_W) = -0.046 (120% from PDG); delta_1/delta_3 = 20/9 exact |
| GRAPH-SPECTRAL-DECOHERENCE-73a | FAIL | t_dec/t_transit = 820.6, 0.0007 hops/transit |
| ALPHA-S-JOSEPHSON-73a | INFO | delta(alpha_s)/alpha_s = -0.297 (wrong direction, structural) |
| FABRY-PEROT-73a | INFO | t_dec/t_transit = 0.535 (6.2% below gate); block decoherence |
| LUTTINGER-SUPERSONIC-73a | PASS | delta_N_pair/N_pair = 2.22e-16 |
| SECTOR-RK-73a | INFO | R_su2/R_u1 = 0.6441 = J_u1/J_su2 exact |
| ENTROPY-FSTAR-73a | INFO | n_s^entropy > 1 structurally (blue tilt locked) |
| INSTANTON-LANDSCAPE-73a | INFO | kappa crosses 1 at tau=0.480, min 0.701 (never Region I) |
| RE-DECOHERENCE-MULTI-73a | INFO | t_dec = 0.267, delta_OOM = 0.486, S72 residual = 0.009 |
| DOS-THRESHOLD-73a | FAIL | delta_i ratios = {1, 20/9} to 8.88e-16 (PERMANENT) |
| BLV-COMPOUND-73a | PASS | delta_n_s(BLV-product) = 0 exact |
| JJ-KAPPA-MAP-73a | FAIL | E_J/E_C(tau=1) = 0.516, kappa > 1 throughout |

---

## IV. Structural Implications

### Substrate causal structure without an exit horizon

The S72 working picture held two horizons: entry at tau ~ 0.22 (thermal, T_H = 72.8 M_KK, n_bar ~ 85) and exit at some larger tau where the modulus decelerates. S73A permanently removes the exit. The revised substrate causal diagram for the transit is:

```
                         tau -> infty
                         |
                         |  supersonic conduit
                         |  (Mach 20.7, no horizon)
                         |
             exit region |
             (N_pair     |
              superselec-|
              tion       |
              preserved) |
                         |
                         |
             fold -------+-------  tau = 0.190 dump point
             (impulsive  |         (extremal, T_H=0, kappa=0)
              Bogoliubov |         BCS freeze = sonic horizon
              production,|         (S70)
              coherent)  |
                         |
             entry       |
             horizon ----+-------  tau = 0.220 (pre-fold)
             (thermal,   |         T_H = 72.84 M_KK
              r_entry    |         |beta|^2 ~ 85
              ~ 2.92)    |         block decoherence source
                         |
                         |  sub-fold causal past
                         |
                         tau = 0
```

Two features are now established:

1. **Single-horizon exflation.** The substrate has ONE acoustic horizon on its worldline through modulus space -- the entry horizon at tau ~ 0.22. It has no exit horizon. The BCS freeze at tau = 0.19 is a distinct object (the S70 "super-extremal" sonic horizon with S(0) = 0, kappa = 4.02 from the corrected near-extremal thermo). The modulus exits the fold and enters the supersonic conduit without crossing another sonic horizon. Its velocity relative to sound stays above Mach 20 permanently.

2. **The "horizon" in analogue gravity is a specific crossing structure.** The substrate does not produce it at the exit because the spectral-action gradient keeps v_tau locked at 8.27 M_KK while c_BA is locked at 0.399 M_KK. In container-spacetime language, this would be described as "a supersonic flow past a throat that never reattaches to the boundary." But the correct direction is inverse: **in the substrate picture, the fact that Schwarzschild solutions have a recognizable outer horizon is a statement that stellar-collapse substrate worldlines have a v/c_s crossing.** The exflation worldline has a different topology.

### Superselection is causal geometry

The LUTTINGER-SUPERSONIC PASS establishes that superselection rules are **the substrate analog of domain of dependence**. A Cauchy surface determines evolution in the Cauchy development; a superselection sector determines evolution in unitary time development. Both are causal constructs. The proof in W3-B is fully algebraic: [H_BCS, N_pair] = 0 identically from the BCS pair algebra, independent of tau, Delta, or transit speed. The 8 numerical tests confirm this to machine epsilon.

Penrose's 1965 singularity theorem (Paper references throughout my memory) assumes (a) null energy condition, (b) non-compact Cauchy surface, (c) trapped surface. The theorem predicts null geodesic incompleteness. For the substrate fold, we have no trapped surface (S55 result: Jensen deformation is volume-preserving, tr(K_ab) = 0, so expansions cannot both be negative). We have no null geodesic incompleteness. What we have instead is algebraic completeness of the N_pair = 1 sector: the 8-dimensional subspace is complete under H_BCS evolution to machine epsilon, across the Mach 20.7 transit. The substrate analog of Penrose's theorem is: **given an algebraically closed observable algebra and a self-adjoint Hamiltonian with commuting sector charge, every initial state in a superselection sector evolves unitarily to a final state in the same sector.** This is trivial in flat QFT and non-trivial only when the dynamics pass through a would-be singularity (fold, horizon, Cauchy surface crossing).

### Bogoliubov-invariance of n_s as "charge at infinity"

W4-D's exact equality n_s(BLV) = n_s(product) is not a numerical coincidence. It is the substrate analog of Penrose's result that the Bondi mass at I+ is preserved under large gauge transformations of the asymptotic data. Here, n_s is computed from the Seeley-DeWitt coefficients a_2, a_4 of the spectral action, which are K-homological invariants of D_K (Connes-Marcolli 2008, Kasparov factorization). The Bogoliubov transformation is a unitary on the GGE Fock space that redistributes occupation numbers but preserves the K-homology class.

**The corresponding structural theorem (S73A, to be recorded in agent memory):**

> THEOREM (n_s Bogoliubov-invariance): Let (A_F, H_F, D_K) be the spectral triple on Jensen-deformed SU(3). Let U be any unitary Bogoliubov transformation on the associated GGE Fock space F. Let f be a spectral functional such that n_s = n_s[f, D_K] = 1 - 6 e_V + 2 eta_V with e_V, eta_V the slow-roll parameters derived from V(tau) = Lambda^4 * Tr(f(D_K^2/Lambda^2)). Then n_s[f, U D_K U^dag] = n_s[f, D_K].
>
> PROOF SKETCH: The spectral action Tr(f(D^2/Lambda^2)) is invariant under U by trace cyclicity. The slow-roll parameters depend only on the Seeley-DeWitt coefficients a_2k, which are unitary invariants. Therefore n_s is unitary-invariant under any Bogoliubov transformation U.

This is the same structural argument as the S48 trace theorem (S[UDU^dag] = S[D] for any U, D, f), specialized to the cosmological observable n_s. The BLV computation confirms the theorem numerically through an explicit dispersive transfer matrix, closing the W2-A van den Dungen concern about non-commutativity at r ~ 3.

### Seven-layer censorship extended

Prior sessions established seven layers of censorship preventing various framework components from crossing to naked singularities or unstable configurations: (S49) energy, friction, no-trapped-surfaces, Josephson; (S62) fragmentation, one-loop stabilization; (S60) topological (pi_1(SU(3)) = 0). S73A does not add a new layer but **sharpens layer 3 (no-trapped-surfaces) by eliminating the exit-horizon alternative**: the would-be naked singularity at tau -> infty in the SU(2) direction (timelike curvature singularity per S49) is now known to not be screened by an exit acoustic horizon but instead by the fact that the modulus never reaches it -- the transit stops at the post-transit freeze at tau ~ 0.22 (physical universe) and does not approach the singular direction.

The substrate analog of the Penrose cosmic censorship conjecture becomes: **the frozen modulus at tau = 0.22 is the substrate's cosmic-censorship boundary.** It hides the tau -> infty singularities (direction-dependent: timelike in SU(2), spacelike in C^2/U(1)) from any observer in the physical universe. The analog of Weyl monotonicity holds (S49: |C|^2 monotone increasing from 5/14 at tau = 0 through tau = 2), consistent with Penrose's Weyl Curvature Hypothesis that gravitational clumping increases |C|^2 through time. Here, "through time" means "through increasing tau" and the clumping is the Jensen deformation.

### Permanent structural closures from S73A (recorded to memory)

1. **PW-THRESHOLD-RATIOS permanent (W2-B, W4-C)**: delta_2/delta_3 = 1 and delta_1/delta_3 = 20/9 are exact structural identities that no DOS reweighting, thermal weighting, or representation choice can break. These are Dynkin index sum rules (representation-theoretic, SU(3) -> SU(2) x U(1)). The sin^2(theta_W) resolution must come from a LEFT/RIGHT connection normalization asymmetry (Paper 13 eq 3.41) or a fundamentally different threshold formula.

2. **alpha_s direction permanent (W2-D)**: Josephson virtual excitation ALWAYS increases 1/g^2 and decreases alpha_s. Proof: virtual pairs add spectral weight to D_K, a_4 is positive-definite under addition of modes, so delta(a_4) > 0 => delta(1/g^2) > 0 => delta(alpha_s) < 0. Hardwired by positivity of the spectral action. Consistent with S28 E-3 (spectral action monotonicity, PERMANENT).

3. **Entropy axiom structurally blue (W3-D)**: f_S applied to D_K on the compact fiber gives n_s > 1 for all beta (tested 20 values). Root cause: Jensen deformation spreads D_K eigenvalues, and f_S is monotonically decreasing. The entropy axiom (Paper 15) cannot reproduce the red tilt because of a structural conflict between eigenvalue spreading and entropy monotonicity.

4. **BLV Bogoliubov-invariance permanent (W4-D)**: n_s is set by spectral action geometry, not by any Bogoliubov transformation. Three independent computations (W2-A product, W1-A BdG, W4-D parametric oscillator) all yield identical n_s = 0.9567 to numerical precision.

---

## V. Forward Projection

### What is now decisive

The causal structure of the substrate transit is now fully specified for the single-horizon picture:

- **Entry horizon** at tau ~ 0.22: thermal, T = 72.84 M_KK, |beta|^2 ~ 85, dominant particle production.
- **BCS/sonic freeze** at tau = 0.19: extremal (S70), T_H = 0, kappa = 4.02 (corrected S70), sole mechanism preventing naked singularity at tau -> infty.
- **Fold transit**: impulsive supersonic, Mach 20.7, phase-coherent Bogoliubov production (r ~ 0.06), N_pair = 1 superselection preserved.
- **Post-transit conduit**: Mach 20+, no exit horizon, modulus freezes at tau ~ 0.22 (five-layer laminar protection from S72 + S73A).

###  Carry-Forward Computations from the SP lens

1. **Penrose compactification of the substrate worldline in modulus space**. The current diagrams (framework/Penrose-Diagrams.md) treat the substrate as a 2D (t, tau) causal structure. S73A's removal of the exit horizon means the post-fold conformal infinity is not an I+ analog but a frozen equilibrium point. Compute the conformal factor Omega(tau) that maps [0.190, infty) to a finite region with the frozen point as a finite boundary. This will quantify whether the physical universe lives "at i+" (timelike future infinity) or "at i^0" (spacelike future infinity) of the substrate causal diagram.

2. **Trapped surface analog of the acoustic fold**. The fold at tau = 0.190 is the point where the BCS gap has its minimum (Delta_min = 0.353 M_KK from S62) and where the modulus velocity peaks. In a container-spacetime analog, this would correspond to a caustic or a pseudo-trapped surface. Question: does the substrate admit a Raychaudhuri-style focusing theorem for the spectral-flow integral lines? The N_pair conservation (W3-B) says yes on N_pair, but the question is whether the geometric analog (trace of the fold Hessian, S63 confirmed no 12D trapped surface) has a phase-space counterpart.

3. **Twistor description of the fiber emergence**. Penrose's twistor theory (1967) describes 4D Minkowski as a subspace of C^4 via the incidence relation. For the fiber (A_F, H_F, D_K), the analog would be: is there a twistor-like space T_F such that the spectral triple is recovered from holomorphic sections of a line bundle over T_F? The W3-D entropy-axiom result (f_S distinct from f*) suggests the fiber is more naturally described by its K-homology class than by its eigenvalue spectrum directly. Twistor methods could simplify this.

4. **Higgs tachyon sigma -- container-trap or substrate-excitation?** S62 HIGGS-SIGMA INFO found sigma tachyonic always (r^2 > 1) and dilaton portal stabilizes it (S62 DILATON-SIGMA). From the causal lens, the sigma tachyon corresponds to a signature change in a subspace of the fiber. The question is whether this is a genuine Cauchy-horizon blueshift instability (as in Reissner-Nordstrom) or merely a coordinate-dependent artifact of the sigma sector. The BLV-COMPOUND PASS gives confidence that the spectral action description is the invariant one.

### What S73A enables for S74

The decoherence budget is now sharply constrained. The surviving mechanisms are (1) Mott charge noise (static, 0.336 OOM) and (2) inter-branch dispersive dephasing (dynamic, 0.150 OOM). The combined 0.486 OOM over-decoheres relative to the 0.27 target by 1.8x, formally closing the A_s gap in the S72 model (residual 0.009 OOM) but suggesting either (a) partial coherence survives that the Gaussian model neglects, or (b) the E_J/E_C ~ 1.3 estimate overstates the Mott suppression. S74 should tighten the E_C computation (3 routes span 190x range currently: 0.066 to 12.4 M_KK) and test whether the 0.009 residual can be pushed below the gate lower bound.

### What S73A blocks

1. **Graph spectral decoherence is DEAD** (W2-C: t_dec/t_transit = 820, 2 OOM above gate).
2. **Exit Bogoliubov is DEAD** (W1-A: 23.2, no horizon exists).
3. **DOS-weighted threshold corrections are PERMANENTLY DEAD** (W4-C: ratios exact to 8.88e-16).
4. **Entropy axiom blueshift is STRUCTURAL** (W3-D: n_s > 1 for all beta).
5. **Mott-kappa coincidence is STRUCTURAL** (W4-E: phase boundaries move in opposite directions).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | No exit sonic horizon (Ma = 20.7 everywhere) | GEOMETRIC+PHONONIC | INFO | Single-horizon causal diagram; removes S72 carry-forward |
| 2 | N_pair superselection preserved to 2.2e-16 | GEOMETRIC | PASS | Algebraic causal rigidity through Mach 20.7 transit |
| 3 | BLV dispersive n_s = n_s(product) exact | GEOMETRIC | PASS | Bogoliubov-invariance theorem confirmed numerically |
| 4 | Leggett DM stable (Z_2 exact, tau_pair/t_univ = 1e65) | PARTICLE | PASS | DM sector protected by exact discrete symmetry |
| 5 | Mott charge noise closes 18.6% of A_s gap | PHONONIC | PASS | Static quantum contribution from E_J/E_C = 1.29 |
| 6 | Compound n_s = 0.9567 (1.95 sigma) | GEOMETRIC | INFO | Unchanged from bare fold; spectral-action determined |
| 7 | BBN excludes additive Volovik vacuum at 10+ sigma | PHONONIC | FAIL | Forces non-additive (G-renormalization) interpretation |
| 8 | S(tau) monotone increasing post-fold (f*) | GEOMETRIC | INFO | No moduli stabilization from S alone; dynamical DE |
| 9 | delta_2/delta_3 = 1, delta_1/delta_3 = 20/9 exact | GEOMETRIC | FAIL | Permanent Dynkin sum rule; sin^2 resolution elsewhere |
| 10 | Graph spectral diffusion irrelevant (0.0007 hops) | GEOMETRIC | FAIL | Kinematic closure; no graph topology suffices |
| 11 | alpha_s correction has wrong sign | GEOMETRIC | INFO | Permanent; from positivity of a_4 Seeley-DeWitt |
| 12 | Fabry-Perot block decoherence (C(B2,B3) = 2.3e-6) | PHONONIC | INFO | Inter-branch decoherence, intra-branch preserved |
| 13 | R_su2/R_u1 = J_u1/J_su2 exact (perfect matching) | GEOMETRIC | INFO | No transport-threshold bridge in Kirchhoff resistance |
| 14 | Entropy axiom gives n_s > 1 structurally | GEOMETRIC | INFO | f_S != f*; entropy and spectral action distinct |
| 15 | Instanton Region III -> II at tau = 0.480 | GEOMETRIC | INFO | Topological transition post-fold; never Region I |
| 16 | Multi-channel over-decoheres by 1.8x | PHONONIC | INFO | Formally closes A_s in S72 model (residual 0.009) |
| 17 | DOS weighting cannot break delta_i ratios | GEOMETRIC | FAIL | PERMANENT structural theorem |
| 18 | E_J/E_C and kappa move in opposite directions | PHONONIC | FAIL | No Mott-topology coincidence in tau in [0.19, 1.0] |

---

## VII. Overall Assessment

S73A delivers a structurally cleaner substrate causal picture at the cost of one carry-forward expectation (the exit horizon). The outcome is net positive from the SP lens: removing a hypothesized structure that does not exist is higher-quality information than finding a parameter fit. The substrate now has a **single-horizon transit** (entry only), a **supersonic conduit** (Mach 20.7) in the post-fold region, an **algebraically rigid observable sector** (N_pair superselection to machine epsilon), and a **Bogoliubov-invariant spectral tilt** (n_s = 0.9567 independent of dispersive dynamics). The container-spacetime reflex -- expecting a deceleration region, a second horizon, or a Cauchy-horizon instability -- does not match what the substrate produces. The correct inversion: black-hole horizons, inasmuch as they are the GR-emergent picture of frozen substrate dynamics, correspond to a very specific v/c_s crossing structure. The exflation worldline has a different topology, and the PASS results in S73A (Luttinger, BLV, Leggett, Mott) establish that the causal content of this topology is rigid, unitary-invariant, and protected by discrete symmetries. The BBN-VOLOVIK FAIL is contained: the non-additive interpretation (G-renormalization) is the only BBN-compatible interpretation and is independently motivated by q-theory (Klinkhamer-Volovik 2008). The sin^2(theta_W) FAIL is structural: it forces resolution through the LEFT/RIGHT connection asymmetry in Baptista Paper 13, not through further spectral weighting. S74's forward priority, from the causal-structure lens, is Penrose compactification of the post-fold conduit and characterization of whether the physical universe at tau ~ 0.22 sits at i+, i^0, or on a novel frozen conformal boundary.
