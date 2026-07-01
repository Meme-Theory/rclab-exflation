# Quantum-Acoustics Theorist Agent Memory

## Active Context
- Phonon-exflation: M4 x SU(3) substrate with Jensen TT-deformation. Particles = phononic excitations.
- Goal: Explain WHY QM has its structure via phononic emergence + dimensional projection.
- Sources: `researchers/Quantum-Acoustics/` (28 papers, canonical `index.md`); Baptista 13-18; Klein 1926; Connes NCG.
- Active substrate dictionary: B1(acoustic,1) | B2(flat-optical,4)=BIC | B3(dispersive-optical,3).
- Core canonical numbers (frequently cited):
  Jensen g|_{u(1)}=e^{2s}, g|_{su(2)}=e^{-2s}, g|_{C^2}=e^{s}; F/B=0.55; CP-1 S_b1/S_b2=4/9.
  E_J=7.042/bond; E_J/E_c=194 SUPERFLUID; eps_canonical=0.00374; omega_L1=0.0492; omega_L2=0.087.
  Four-speed: c_mod=1.0, c_BLV=0.485, c_BA=0.399, c_L=0.025; Mach=13.8.
  n_s=0.9595 (BCS+CW, 1.28 sigma); r(CMB)=0.0242; r(transit)=0.0071; alpha_s=-0.038 (transit).
  Omega_DM h^2=0.120 (Leggett-only); f_DM=0.161; z_eq=3425; T_RH=1.70e15 GeV.

## Reference Index (Session Detail Files)
- [foundations-s5-s20.md](foundations-s5-s20.md) — QM emergence, Bell, CG, Jensen, perturbative closure, TT discovery
- [sessions-s40-s54.md](sessions-s40-s54.md) — phononic crystal, DOS, Bragg, GL Rosetta, TB reframe, CG graph
- [sessions-s55-s59.md](sessions-s55-s59.md) — fabric (E_J=7.042), BA spectrum, Leggett, Josephson dominance, eps_canonical
- [sessions-s60-s64.md](sessions-s60-s64.md) — S60 audit, n_s PASS, Hawking workshops, four-speed, linewidth FAIL
- [sessions-s65-s70.md](sessions-s65-s70.md) — Bispectrum, DM, Z_2 decay, tensor, 3He match, analog designs
- [sessions-s72-s74.md](sessions-s72-s74.md) — laminar flow, decoherence budget, branch-resolved, spectral independence
- [sessions-s75.md](sessions-s75.md) — f_conv PASS, Parker canonical, DC FAIL, Mach exponential, N_eff exact
- [sessions-s76.md](sessions-s76.md) — f_NL PASS, modulus grav-decay, f_conv permanent, CC 0.47 OOM, instanton CLOSED
- [sessions-s77.md](sessions-s77.md) — multi-cell E=29.42, BCS timing PASS, A_s INVERTED to overproduction
- [project_substrate-not-c-limited.md](project_substrate-not-c-limited.md) — c bounds propagation, not substrate dynamics

## Permanent Theorems & Closures (high-leverage; full provenance in detail files)
- Josephson dominance: F_J/F_BA ~ 14. Fluctuations OF order cannot overwhelm order.
- Two-adiabaticity: Josephson(13 M_KK)=adiabatic, Leggett(0.1 M_KK)=non-adiabatic.
- Mode-independent BA: omega_n(tau)=f(tau)*sqrt(lambda_n). All 31 modes identical |beta|^2.
- Leggett = harmonic oscillators, NOT two-level. Bogoliubov squeezing, not LZ.
- CC = phonon lifetime = integrability = zero phonon-phonon scattering. Same obstruction 3 ways.
- CC monotonicity: dE_ZP/dq = sum positive terms > 0. No interior equilibrium.
- BCS coherence suppression WORSENS CC (condensate strengthens monotonicity).
- BCS-Sakharov decoupled: a_2(gravity), a_4(pairing) independent at self-consistency.
- Parker canonical for supersonic transit; T_H(acoustic) phononic, NOT gravitational A_s. Category error.
- Mach scaling EXPONENTIAL: T_eff ~ exp(2r_0 Ma). Power-law CLOSED.
- f_conv = pi^4/(9216*a_0^2). a_2 cancels EXACTLY. Family monotone in n.
- f_conv FAMILY: f^{(n,p)} = (M_KK/M_Pl)^4 * (a_n/a_0)^p. p=2 variances; p=1 energy. NCG analog of multi-response hierarchy.
- Multi-mode squeezed vacuum GAUSSIAN; non-Gaussianity needs H_3 cubic vertex.
- Instanton liquid bounded by mode-counting: |V_liquid/V_bare| <= N_BCS/N_total ~ 8/6440.
- 35D off-Jensen Hessian: ALL eigenvalues negative. Jensen line is RIDGE.
- CM_factor=1 EXACTLY for finite spectral triples (zeta entire). JLO no CC correction.
- Level 0/1 separation: f_conv applies to perturbations, not background Friedmann.
- Multi-cell coherent Bogoliubov: E=29.42 from E_J/E_c=194 (superradiance analog).
- BCS timing hierarchy: dt_transit << tau_relax << t_BCS << T_BCS_osc. Gap absent during squeeze.
- Z_2 single decay FORBIDDEN exactly (a_2(phi)=a_2(-phi)). Pair: Gamma/H_0=9.3e-66.
- DW GW retracted (Josephson bias kills walls 15,000x before reheating).
- Inter-sector Yukawa = 0 EXACTLY (block-diag + J-conjugation).
- c_s^2=0 CLASSIFICATION PROPERTY (spectral moment, not field). Phononic fingerprint.
- A_s gap INVERTED at S77: overproduction by 9.5 OOM after k_pivot/N_pivot fix.
- Level-1 predictions (w_0, n_s, r, ISW, f*sigma_8) are SUBSTRATE TESTS, normalization-independent.

## Methodological Rules (compressed)
- TRAP: V_bare and V_constrained are DIFFERENT MODELS, not rescalings. V_bare canonical.
- TRAP: Frame V vs spinor V. Frame {0..7} != branch labels {B3,B2,B1}.
- Transport != scattering on discrete spectra. Flat bands ENHANCE scattering (Lorentzian).
- Flat-band BRANCH intuition fails repeatedly (linewidth, n_bar, kappa). Compute mode-by-mode FIRST.
- Squeezed-state variance exp(-2r)/4, NOT thermal 1/(1+n). Factor 10^4.
- Josephson anisotropy = E_J ratio (INTER-cell), not c_Gold ratio.
- Hawking broadening, Mach: use four-speed hierarchy explicitly.
- Use OBSERVABLE-scale metric for additivity, NOT delta-scale (denominator pathology).
- Linear phase averaging near +/-pi WRONG. Use circular mean ALWAYS.
- Hybridization gaps OPPOSE decoherence (protect inter-branch coherence).
- Volovik partition != two-fluid hydro (no mutual friction, no relative velocity).
- Z_fabric != Z_single^N (phase coherence reduces effective mode count).
- "Mode count wins" only for non-interacting cells (E_J/E_c=194 violates).
- Partition formula (2-band) underpredicts; use full 3-band eigenvalue problem.
- Back-of-envelope FIRST. F_Josephson ~ 350 was knowable before detailed F_BA.
- Adversarial threats list: Diosi-Penrose decoherence, ETH thermalization, quasiparticle breakdown.
