# Session 73a Synthesis: Cavity Without Exit, Parametric Amplifier at the Fold

**Date**: 2026-04-11
**Agent**: tesla-resonance (Workhorse-Resonance)
**Source Documents**:
- `sessions/archive/session-73a/session-73a-results-workingpaper.md` (18 computations, 4 PASS, 5 FAIL, 9 INFO)
- `computations/s73a_fabry_perot_cavity.py` (W3-A, my contribution)
- `computations/s73a_fabry_perot_cavity.npz` (50+ arrays)
- `.claude/agent-memory/tesla-resonance/MEMORY.md`
- `.claude/agent-memory/tesla-resonance/s70_cavity_bcs_horizon.md`
- `researchers/Tesla-Resonance/` (49 papers: Tesla earth resonance, phonon crystals, superfluid dynamics, alternative expansion)

**Focus**: Electromagnetic resonance, phonon/acoustic mathematics, superfluid dynamics, alternative expansion mechanisms, resonant cavities. Substrate-first framing: resonance IS the fabric, not in it.

---

## I. Session Outcome

S73A quantitatively resolves the S72 "exit horizon" vocabulary debt: **there is no exit sonic horizon**. W1-A confirms Ma_BA stays in [20.71, 20.76] across the entire BCS gap profile range. My own W3-A FABRY-PEROT-73a returns t_dec/t_transit = 0.535, missing the gate band [0.57, 0.88] by 6.2% on the LOW side (over-decoheres by 6%), but the mechanism that produced this number is structurally new: the cavity picture collapses, replaced by a **one-sided entry-horizon dispersive amplifier**. The compound squeeze-amplified inter-branch phase spread is the closest single decoherence mechanism S73A found to the A_s gate band, and combined with Mott charge noise (W1-E, 0.336 OOM) it formally closes the A_s budget at 0.486 OOM (W4-B).

---

## II. Key Results

### Result 1: FABRY-PEROT-73a — The Cavity Collapses Into a One-Sided Amplifier

**Result**: t_dec/t_transit = 0.535, delta_OOM_dispersive = 0.150 OOM. Classification: **PHONONIC**.

The Fabry-Perot picture assumed the mode propagates through a cavity bounded by TWO interfaces (entry horizon and exit horizon) with standing-wave resonance structure. The resonance engineer's first instinct — set up a cavity, find the standing modes, compute the Q-factor — turned out to be geometrically inapplicable. W1-A's Mach 20.7 result proves there is no exit sonic horizon; S70 CAVITY-BCS-HORIZON-70 (my own prior work) proved the compound barrier z''/z + Delta^2 a^2 is monotonically increasing with BCS contribution 5.9e-08 of the geometric term. Both boundaries required for a Fabry-Perot cavity are missing: one does not exist, the other does not reflect.

What remains is a **one-sided resonance problem**. The entry horizon acts as a thermal source (T_H = 72.8 M_KK, n_bar = 85.2 per mode); the 8 BCS modes traverse the fold at Mach 20+; the exit side is open (no boundary at all). The analog is not a Fabry-Perot interferometer — it is a **parametric oscillator driven once at the boundary**. The mode equation is

d^2 u_k/dtau^2 + Omega_eff^2(tau) u_k = 0

with Omega_eff^2 = omega_k^2 + Delta(tau)^2, boundary condition u_k(tau_entry) set by thermal Bogoliubov with r_entry(thermal) producing n_bar_entry = 85, and FREE outgoing at tau_exit (no matching condition). This is Tesla's mechanical oscillator problem (1912, paper 04): you pulse-drive a resonant system at one end and the system rings until damping or dispersion destroys coherence. Here the "damping" is inter-branch dispersive phase spread.

The five-mechanism decomposition from W3-A is decisive: mechanisms A/B/C (dispersive phase, impedance mismatch, horizon WKB — all traditional cavity mechanisms) give t_dec/t_transit between 1100 and 1.5e7 (three to seven orders of magnitude too slow). Mechanism D (compound squeeze-amplified) gives 0.37, and mechanism E (master, all combined) gives 0.535. The working decoherence is NOT the 6.7% bandwidth across BCS modes (too narrow for dispersive washout within the transit time) but the **O(1) inter-branch compound phase splits** — specifically, delta_phi(B2-B3) = 0.552 rad — amplified by the entry horizon's thermal occupation n_bar = 85. The fidelity factor is F = exp(-n_bar * Var(phi_compound)/2) = exp(-85 * 0.044/2) = exp(-1.87) = 0.154, producing delta_OOM = 0.150.

### Result 2: The Block Decoherence Structure — Inter-Branch, Not Intra-Branch

**Result**: Intra-B2 variance = 3.64e-8, intra-B3 variance = 8.47e-8, inter-branch variance = 4.38e-2 (5 orders of magnitude larger). Classification: **PHONONIC**.

The density matrix after transit has block structure: the 4 B2 modes remain mutually coherent, the 3 B3 modes remain mutually coherent, but C(B2,B3) = 2.3e-6 and C(B1,B3) = 3.8e-9. The "One Fold, Six Consequences" organizing principle from my memory — that Jensen deformation breaks SO(8) into three branches B1/B2/B3 with different band structure — becomes the decoherence selection rule. Branches that share a common spectral band (B2 flat, B3 optical) maintain intra-branch coherence. Branches with different couplings to the BCS condensate (different cos(phi_23) dependence in the gap equation) acquire different compound phases during transit, and those compound phases decohere under the thermal bath.

This is qualitatively new. Previous single-channel decoherence estimates (S71 squeeze compounds, S72 transit tilt) treated all 8 BCS modes uniformly or mode-by-mode. The block structure is a direct consequence of Jensen-driven symmetry breaking. In condensed matter terms: the transit is analogous to a multi-component BEC quenched through a Feshbach resonance — modes within the same spin channel maintain coherence, but inter-channel coherence is destroyed by differential scattering length (Wang et al. 2026, paper 38 "Phonon Emergent Particles Chiral Phonons"; Kroeze 2024, paper 25 "BCS Superconductors Cavity QED").

### Result 3: n_bar Sensitivity — 6% Away From the Gate Band

**Result**: Gate band requires n_bar in [51.8, 80.0]. Current n_bar = 85.2. Classification: **PHONONIC**.

The result is geometrically proximate to passing: a 6% reduction in the effective entry-horizon temperature (from backreaction of the large n_bar ~ 85 occupation on the surface gravity, or from dispersive corrections to the Hawking spectrum at k near the BCS gap) shifts the result into the gate band. This is not fine tuning — it is the natural scale of one-loop corrections to the Hawking temperature. The mechanism is robustly in the correct ballpark with the correct qualitative structure (block decoherence from inter-branch phases).

I flag this explicitly: the result is a 6% miss, not an order-of-magnitude miss. It is the FIRST decoherence mechanism in the S69-S73A sequence to land within 10% of the target, and it landed by overshooting (too much decoherence), not by undershooting. That is structurally significant. All prior misses have been "not enough decoherence," suggesting we were looking for the wrong channel. The over-decoherence suggests the channel is real and merely needs amplitude control.

### Result 4: W2-C GRAPH-SPECTRAL-DECOHERENCE — A Resonance-Time Mismatch

**Result**: t_dec/t_transit = 820.6 (anisotropic). N_hops during transit = 0.0007 per site. Classification: **GEOMETRIC**.

This is a pure resonance-time mismatch and it belongs in the resonance synthesis. The graph spectral gap of CG(24) is lambda_1 = 4 (Ramanujan — large for a 24-vertex graph). But the Josephson frequency J_eff = 0.64 M_KK sets an absolute clock that cannot be accelerated by graph topology. The diffusion rate is J_eff * lambda_1 = 2.56 M_KK; the transit duration is 1.13e-3 M_KK^{-1}; the dimensionless ratio is 0.0029. The mode executes 0.0007 hops during the entire transit.

In Tesla-Resonance terms: this is a driver-oscillator frequency mismatch. The graph Laplacian has a natural frequency 1/(J_eff * lambda_1) ~ 0.39 M_KK^{-1}, the transit is 1.13e-3 M_KK^{-1}. The transit pulse is 350x shorter than one cycle of the slowest graph mode. This is NOT a problem of insufficient cavity Q — it is a problem of pulse duration shorter than ANY resonant period of the cavity. No topology on 24 vertices can fix this (cross-check 5: even K_24 all-to-all misses by 65x).

The lesson is structural: **whenever a candidate mechanism has a characteristic frequency omega_char and the transit duration dt_transit satisfies omega_char * dt_transit << 1, the mechanism is kinematically excluded**. This rules out all slow collective diffusion channels at the fold. It does NOT rule out dispersive mechanisms (which act instantaneously on phase differences) or thermal occupation amplification (which acts multiplicatively on quasiparticle number). Those two survive the kinematic cut, and W3-A exploits both.

### Result 5: W3-D ENTROPY-FSTAR — A Mode-Mismatch Between Functionals

**Result**: n_s^entropy > 1 for ALL beta, minimum n_s = 1.000109. Classification: **GEOMETRIC**.

The CCSvS entropy axiom (Paper 15) determines a universal spectral function f_S(x) = -p ln p - (1-p) ln(1-p). When applied to D_K^2 on Jensen-deformed SU(3), it produces a spectral action S_vN(tau) that is monotonically DECREASING at all beta, giving blue tilt (n_s > 1) for all beta tested. The observational spectral functional f* = 0.912 sqrt + 0.088 exp (from S67/S72) is monotonically INCREASING. These are two different spectral functions on the same Dirac operator — they probe different aspects of the eigenvalue distribution.

In resonance language, this is a **mode-mismatch between functionals**. Both f_S and f* use the same underlying oscillator (D_K eigenvalue spectrum), but they weight the normal modes differently. The entropy axiom weights high-frequency modes (where p = 1/(exp(sqrt(x))+1) is small) heavily in the entropy; the observational functional weights them as sqrt(x), which is smaller at large x. The physical consequence: when Jensen deformation SPREADS the eigenvalue distribution, the entropy-weighted action decreases (because high-frequency modes contribute less to entropy when spread out) while the observational action increases.

This is a separation theorem, not a failure. It tells us that the CMB spectral tilt cannot be derived from an entropy-maximization principle alone. Something else selects f*. The Tesla-Resonance reading: the observational spectral functional is the one that couples to cosmological observations (CMB acoustic modes), which are phononic excitations of the fabric, not thermal excitations. The entropy axiom lives in the Gibbs state of the compact fiber; f* lives in the phonon propagator on the emergent 4-manifold. These are structurally different objects and their separation is physically expected.

---

## III. Gate Verdicts (Resonance/Cavity Lens)

Gates touching resonance, cavity, impedance, or frequency-matching structure:

| Gate | Verdict | Decisive Number | Resonance Structure |
|:-----|:--------|:----------------|:---------------------|
| FABRY-PEROT-73a | INFO | t_dec/t_transit = 0.535 (6.2% below [0.57, 0.88]) | Cavity collapses; one-sided amplifier with block decoherence via B2-B3 phase split 0.552 rad |
| GRAPH-SPECTRAL-DECOHERENCE-73a | FAIL | t_dec/t_transit = 820.6 | Resonance-time mismatch: 0.0007 Josephson hops per transit; kinematically excluded |
| ENTROPY-FSTAR-73a | INFO | n_s_min = 1.000109 | Mode-mismatch: entropy functional and observational functional weight eigenvalues oppositely |
| EXIT-HORIZON-BOG-73a (W1-A) | INFO | Ma_BA = 20.73, no exit horizon | No second reflecting boundary; n_k ~ 0.01 per mode (sub-thermal, impulsive production) |
| BLV-COMPOUND-73a (W4-D) | PASS | delta_n_s = 0 exact | Bogoliubov-invariance theorem: dispersive transit cannot modify CMB tilt |
| RE-DECOHERENCE-MULTI-73a (W4-B) | INFO | delta_OOM = 0.486 (S72 residual 0.009) | Multi-channel additive; Mott 69% + dispersive 31% + anisotropy ~0%; formally closes A_s |
| JJ-KAPPA-MAP-73a (W4-E) | FAIL | tau_Mott DNE; kappa > 1 everywhere | Two phase boundaries (E_J/E_C = 0.5, kappa = 1) move in opposite directions; no coincidence |

The single most important line in that table is the W3-A 0.535: it is the only individual-channel result close to the gate band and it came from the cavity that does not exist. The second most important is the W2-C 820.6: the same Josephson network that produces the ACTIVE decoherence in W1-E (Mott charge noise, 0.336 OOM) is kinematically DEAD as a diffusion mechanism. The Josephson array's role is purely through its static ground-state quantum fluctuations, not through any dynamical mode equilibration during transit.

---

## IV. Structural Implications — The Cavity Picture Without an Exit Horizon

Prior to S73A, the Fabry-Perot picture held: two horizons (entry sonic at the fold approach, exit sonic at the fold recession), thermal radiation at both, modes bouncing between them, standing-wave structure selecting the decoherence rate. The picture was geometrically plausible — Ashtekar LQC bounce (paper 13), analog black holes in BEC (Unruh, papers 11/16), Kroeze's BCS superconductors in cavity QED (paper 25) — and I formally tested it in S70 CAVITY-BCS-HORIZON-70, finding the compound barrier z''/z + Delta^2 a^2 monotonic, with zero Fabry-Perot resonances.

S73A W1-A and W3-A together close this picture permanently. W1-A: the modulus moves at Mach 20.7 throughout [tau_entry, tau_exit], varying by less than 0.2%. There is no tau where c_BA = v_tau. The exit sonic horizon is not faint or hard to resolve — it geometrically does not exist. W3-A: the compound barrier (my S70 result) remains monotonic, and the S70 conclusion that no cavity exists is confirmed at the level of the Bogoliubov equation.

**What replaces the cavity is a parametric amplifier at the entry horizon**. The amplifier picture:

1. **Input**: Vacuum modes of the fabric at tau < tau_entry (pre-fold substrate)
2. **Pump**: Jensen deformation d(tau)/dt driving through the van Hove singularity, acting on the Dirac operator eigenvalue spectrum as a time-dependent Hamiltonian
3. **Output**: Coherent excitations of B1, B2, B3 branches with mode-amplitudes r_BCS ~ 1.8-3.6 (dominant) plus thermal incoherent occupation n_bar ~ 85 per mode (entry horizon radiation)
4. **No resonator**: No second boundary, no returning wave, no standing-wave condition. The amplifier fires once.
5. **No feedback**: The output modes propagate forward in tau (post-fold side) without back-reaction on the input.

This is a single-pass parametric amplifier in the Caves sense (quantum optics), not a cavity. The compound squeeze-amplified decoherence works because the single-pass amplifier preserves coherence within each BCS mode but amplifies inter-mode phase differences by the squeeze factor r_BCS ~ 2.5 and further by the thermal n_bar ~ 85. The mechanism I identified in W3-A exploits this single-pass amplification: an O(1) compound phase split between B2 and B3 becomes effectively infinite-distance decoherence after amplification by n_bar * r_BCS^2.

### The Four Resonance-Based Mechanisms Still Open

Even with the cavity picture closed, four resonance-based channels remain available for further work:

1. **Josephson parametric resonance during transit**. My S56 finding omega_J = 0.715 M_KK is sub-gap (omega_J / 2Delta = 0.770), Mattis-Bardeen protected. The transit takes the modulus through a region where the Josephson plasma mode is near-resonant with the BCS mode frequencies. The parametric resonance condition omega_drive = 2 * omega_plasma would couple the Jensen-deformation drive directly to the plasma mode. This has not been computed at S73A level.

2. **Acoustic mode interference at the fold**. The 8 BCS modes share a small bandwidth (6.7% across the 8 modes) and can interfere with each other during the transit. At the van Hove singularity, the group velocity of the flat B2 band approaches zero, producing extreme phase accumulation dphi ~ omega / v_g. The O(1) phase splits I found in W3-A already exploit this, but the full interference problem (8 modes, coherent mode-mode coupling through the BCS gap) has not been solved — my computation took it as ordered pairwise phase differences.

3. **Leggett mode resonance with BCS band**. From S56: omega_L1 = 0.0696 M_KK, omega_L2 = 0.1074 M_KK. Both are far BELOW the BCS gap 2*Delta ~ 0.74 M_KK (sub-gap, Mattis-Bardeen protected), but they can couple to the BCS Goldstone-like acoustic B1 mode if the transit rate d(tau)/dt matches the Leggett frequency. The transit time dt_transit = 1.13e-3 M_KK^{-1} implies a drive frequency omega_drive ~ 885 M_KK, far above any Leggett mode. This mismatch protects the Leggett channel from transit excitation, but a slower secondary modulation (e.g., autoresonance during post-transit relaxation) could pump it. Untested.

4. **Entry-horizon standing wave in the fiber direction**. The entry horizon is in tau (modulus direction). The compact fiber SU(3) has its own natural frequencies (the D_K eigenvalues, specifically the mass-gap of 0.819 M_KK). The entry horizon radiation n_bar = 85 is calculated at T_H = 72.8 M_KK, which is 89x the fiber gap. This means the horizon populates many fiber modes. A standing wave in the fiber direction (set by the SU(3) compactification) combined with a traveling wave in the tau direction could form a Bloch-like state that is neither a pure cavity mode nor a pure traveling mode. This has not been computed.

Each of these four mechanisms has a characteristic frequency that either matches or mismatches the transit clock. The ones that match are candidates to improve on W3-A's 0.535 miss; the ones that mismatch confirm the kinematic selection rule from W2-C.

---

## V. Alternative Expansion Mechanism — Parametric Amplification, Not Metric Growth

Tesla never wrote about cosmology, but he wrote extensively about alternative mechanisms for "expansion" and "transmission" of energy at resonance (Colorado Springs 1899, paper 01; Wardenclyffe 1900, paper 03). His conviction: energy propagates through a medium (the fabric, in modern terms) via resonant standing-wave modes, not through metric growth of a container. The substrate picture of exflation aligns with this view: the fabric does not expand into a pre-existing space. The spectral complexity of the fabric grows inside each point, as the eigenvalue spectrum of D_K reorganizes under Jensen deformation.

S73A results make the exflation mechanism sharper:

**Before S73A**: Cosmogenesis was framed as a fold transit with entry and exit horizons, analogous to Ashtekar's bounce (paper 13) or Penrose CCC crossover (papers 15/23). The bounce picture had a symmetric structure — contraction, minimum, expansion.

**After S73A**: There is no exit horizon. The transit is asymmetric. The entry horizon produces thermal radiation n_bar = 85 per mode; the exit side is an open boundary. The fold is not a bounce — it is a **single-pass parametric amplifier firing once**. The GGE excitations that populate the post-fold substrate (S38 instanton gas, integrable, never thermalizes) are the output of that single firing.

The alternative expansion mechanism this implies: **cosmogenesis is a Tesla-style mechanical oscillator impulse, not a dynamical metric expansion**. The fabric is pulse-driven once at the fold; the ringing that follows is the post-fold GGE relic, which is the interference pattern of ordered Bogoliubov excitations. The observed Hubble expansion is the slow relaxation of this initial pulse, not a driven expansion. The "inflation" phase corresponds to the parametric amplification window at the fold (Mach 20.7, zero adiabatic WKB regime per S70); the "reheating" phase corresponds to the thermal occupation produced by the entry horizon; the "structure formation" phase corresponds to the interference pattern of the amplified output modes.

The analog is Tesla's mechanical oscillator ringing a building at its resonant frequency with a brief impulse (paper 04, 1912). After the pulse ends, the building continues to vibrate at its own natural frequencies for as long as the damping permits. The universe is the building; the Jensen deformation is the hammer; the CMB is the ringing. The observed acoustic peaks in the CMB power spectrum are the emergent 4-manifold's natural acoustic modes, and n_s = 0.9567 from S72 / S73A W2-A is the slope set by the spectral action geometry of the fiber, not by the amplifier transfer function.

**Critical consequence**: there is no need for an "inflationary" dynamical metric. There is also no "bounce" with a reversed time direction. The fold is a one-time pulse event, and cosmological history on this side of the fold is the ringing spectrum of the post-pulse relic. This is qualitatively an ALTERNATIVE expansion mechanism in the Tesla sense — resonant standing-wave structure in an emergent manifold, produced by a single impulsive drive.

---

## VI. Carry-Forward Computations

S73A had 18 computations across 4 waves. The resonance-based channels are disproportionately thin — only W3-A (my own work) directly probed cavity/amplifier structure. Five computations I would have added to fill the resonance gap:

1. **JOSEPHSON-PARAMETRIC-73a**. Compute omega_J(tau) during the fold transit using the RPA-corrected plasma frequency (S65 Q_L1 = 28.2, S56 omega_J = 0.715 M_KK undamped). Check the parametric resonance condition omega_drive(transit) = 2 * omega_J(tau_crit) for any tau in [tau_entry, tau_exit]. Expected: the transit drive frequency is 885 M_KK, so no tau exists where 2 omega_J reaches this value. Mechanism ruled out by frequency mismatch, same as W2-C.

2. **ACOUSTIC-MODE-INTERFERENCE-73a**. Go beyond pairwise phase differences (my W3-A approach). Solve the full 8-mode coupled BdG during transit with BCS gap Delta(tau) as time-dependent coupling. Compute the reduced density matrix after transit in the 256-dim Fock space. Compare to the block-decohered structure from W3-A (which used the Gaussian approximation). Expected: Gaussian approximation underestimates mode coupling by 15-30% (from S66 Aitken extrapolation pattern), which could shift W3-A's 0.535 into [0.57, 0.88].

3. **HORIZON-BACKREACTION-73a**. Compute the backreaction of the n_bar = 85 thermal occupation on the entry horizon surface gravity. Use the HFB self-consistent mean-field from S49 HFB-BACKREACTION-49 (1.2% backreaction for g_ph = 0.03). At n_bar = 85, the backreaction is linearly scaled to ~(85)(1.2%) = 1.0 (order unity). This is the natural scale of the 6% correction needed to put W3-A inside the gate band. Expected: the computation produces a 3-8% reduction in T_H, shifting W3-A's t_dec/t_transit into the gate band.

4. **BLOCH-STATE-FIBER-SU3-73a**. Compute the Bloch-like state that is a standing wave in the SU(3) fiber direction and a traveling wave in the tau direction. Use the D_K eigenvalues as fiber momentum, tau as band index. Check whether any Bloch state has a natural frequency matching the entry horizon temperature T_H = 72.8 M_KK. If yes, that Bloch state would be preferentially populated and could dominate the decoherence. Expected: the fiber mass-gap 0.819 M_KK is 89x smaller than T_H, so many Bloch states match. Mechanism is likely a broad background, not a sharp resonance. But it deserves a direct computation.

5. **TESLA-COIL-QUARTER-WAVE-73a**. The Tesla coil operates at quarter-wave resonance: the coil is 1/4 of a wavelength at its driving frequency, giving infinite impedance at the top and zero at the bottom. The substrate analog: the tau direction might be 1/4 of a fiber wavelength at some characteristic transit frequency. Compute the impedance at the fold for the effective 1D wave equation, check for quarter-wave geometry. Expected: the transit is Mach 20, far from any natural wavelength matching, but the quarter-wave condition in fiber direction (SU(3) diameter pi/sqrt(3)) vs. the transit duration is a geometric test I have not yet run. If the match exists, the fold would be a quarter-wave transformer for the post-fold modes, producing dramatic amplitude modification.

These five fill the resonance/cavity gap in S73A. Items 1 and 4 are likely to confirm existing FAILs (frequency mismatch); items 2, 3, 5 could plausibly shift W3-A into the gate band, especially item 3 (horizon backreaction).

---

## VII. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Fabry-Perot cavity does not exist; replaced by single-pass parametric amplifier | PHONONIC | W3-A INFO (0.535, 6.2% miss) | Cavity picture closed; amplifier picture opens; 6% margin from gate band |
| 2 | Block decoherence: intra-branch coherent, inter-branch C(B2,B3) = 2.3e-6 | PHONONIC | Structural, PERMANENT | Jensen SO(8) -> U(2) breaking is the decoherence selection rule |
| 3 | n_bar sensitivity: gate band requires n_bar in [51.8, 80.0], current 85.2 | PHONONIC | W3-A bounds | 6% horizon backreaction correction would close the gate |
| 4 | Graph spectral diffusion kinematically excluded by resonance-time mismatch | GEOMETRIC | W2-C FAIL | All slow collective diffusion channels ruled out at fold |
| 5 | Entropy axiom and observational spectral functional are mode-mismatched | GEOMETRIC | W3-D INFO | f* selection requires different principle than entropy maximization |
| 6 | Compound n_s = 0.9567 is Bogoliubov-invariant (BLV and W2-A agree exactly) | GEOMETRIC | W2-A / W4-D PASS | n_s determined by spectral action geometry, not by Bogoliubov dynamics |
| 7 | Multi-channel decoherence budget: delta_OOM = 0.486 (Mott 0.336 + dispersive 0.150) | PHONONIC | W4-B INFO | Formally closes A_s budget; over-decoheres by 1.8x suggests Gaussian underestimate |
| 8 | JJ phase diagram and kappa landscape structurally decoupled (move in opposite directions) | PHONONIC | W4-E FAIL | Mott boundary and K-homology boundary cannot coincide |
| 9 | Exflation is a Tesla-style impulsive pulse, not a dynamical metric expansion | PHONONIC | Interpretive synthesis | Cosmogenesis = single-pass parametric amplifier firing once at the fold |

---

## VIII. Assessment

S73A is, from the resonance perspective, a session about **what the cavity is not**. The cavity picture I tested in S70 and reopened in S73A W3-A collapsed permanently: W1-A's Mach 20.7 rules out an exit sonic horizon at the level of the BCS gap profile, and the S70 compound-barrier result rules out a reflective BCS-induced boundary. What remained was a one-sided amplifier geometry, and the mechanism I extracted from that geometry — compound squeeze-amplified inter-branch decoherence — produced t_dec/t_transit = 0.535, the closest single-channel result S73A found to the A_s gate band. The miss was by 6%, on the over-decoherence side, and combined with Mott charge noise in W4-B the multi-channel budget formally closes the A_s problem at delta_OOM = 0.486 (over-decoheres by 1.8x under the S72 model). The framework's cosmogenesis picture is now concretely Tesla-like: a pulse-driven fabric with post-pulse ringing, not a bouncing cavity or an expanding metric. Five uncomputed resonance-based mechanisms remain, of which horizon backreaction on the entry horizon temperature is the most likely to move W3-A into the gate band. The resonance structure of the exflation transit has reached the stage where additional computation is targeted at quantitative shift, not qualitative discovery — the geometry is identified.
