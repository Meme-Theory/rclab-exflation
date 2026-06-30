# Neutrino-Detection-Specialist Agent Memory

## Topic Files
- `gate-registry.md` -- S22-S40 pre-registered gate ledger (closed verdicts; reference only)
- `s52_offjensen_pmns.md` -- S52 INTERMEDIATE: singlet PMNS is 2x2 (B1,B3); B2 isolated structural wall
- `s52_msw_transit.md` -- S52 INFO: B1-B2 crossing at tau=0.107, non-adiabatic, ordering dynamical
- `s56_fabric_neutrino.md` -- S56: mu-shift worsens R, adiabatic gap protects eigenvalues, N_eff irrelevant to BBN
- `s96_intersector_pmns.md` -- S96 INFO: non-left-invariant L_X LIFTS B2 wall (theta_12/theta_23 open from 0, [iK_7,D_K]=0 kept); R unreachable (peak 6.87 vs floor 17); "angles open, R does not"
- `s100a_md_normalization.md` -- S100a INFO: substrate-forward Y_i maps NON-UNIQUE (47% split, ~100x below band); Sigma_mnu oscillation-anchored PERMANENTLY (track_B 0.9); MAP-B Casimir grading gives Y_1=0 EXACT
- `inv11_w2_majorana_moment.md` -- INV11-W2-3 PASS (investigation track): diagonal μ=0 EXACT (Majorana antisym from [J,D_K]=0); texture-fixed μ_23/μ_13=0.998 from S60 V_B3; 2nd self-conjugacy channel; NOT yet session-promoted
- `inv11_w2_abs_mass_triangle.md` -- INV11-W2-2 INFO (investigation track): 1 S99-W3 triple lands in all 3 direct-mass windows (Σ=0.0582 19% below DESI; m_β=8.75 meV NON-DETECTION KATRIN/P8; m_ββ central=3.695 meV reldiff 0.0 vs m_bb_FW, ON Row#80 upper edge=marginal=INFO); REUSABLE: PMNS PDG(0.307/0.0220)=primary vs NuFit6.0(0.303/0.02225)=diagnostic (plan "NuFit-6.0" mislabel, −0.60% irrelevant); Class-8.3 edge-tol fix
- `s116_lepton_pmns_texture.md` -- S116-W2 FAIL: external-ε_LX lepton PMNS WALLED (mix_grp=0/4); θ12 OVERSHOOTS (sin²=0.996, quark-V_us analog) + J=0 (δ_CP∈{0,π}); masses do NOT fix mixing (U_eL FREE, soft wall, obs reachable @1.53× minimal)
- `s116_pmns_rescue.md` -- S116-W2-PMNS-RESCUE workshop verdict: lepton shape leg WALLED-AS-UNDER-DETERMINED (Track B); seesaw metric REAL+spectrum-pinned+quark-inaccessible (connes-conceded) but sufficiency-FAILED at near-deg B-branch M_R (√(B₂/B₁)=1.036); COROLLARY both lepton+quark mixing under-determined (V_us=0.3107 = multistart artifact); binding open channel R
- `s117_quark_ckm_underdetermination.md` -- S117-W2-4 PASS: quark V_us UNDER-DETERMINED quantified (texture-adm interval [0.053,0.986] width 0.933 at FIXED masses; seed-indep CV=1.5e-3); 0.3107 = multistart artifact; PDG reachable @1.559× min eps_LX (quark analog of lepton 1.53×); reconciles 0.3107-overshoot + ~3124×-zero-mixing as 2 points on 1 free orbit; COROLLARY both quark+lepton mixing under-determined (pairs §W2-5 lizzi PASS=flat)
- `s117_seesaw_resonance_wall.md` -- S117-W2-3 FAIL (clean): seesaw single-RH-dominance resonance CANNOT relieve PMNS wall; θ12 M_R-INVARIANT (rank-2 Y_1=0 ⇒ |U_e1|²=|U_eL[0,0]|²=0.0044, 156× below NuFIT ⇒ sin²θ12≥0.9956, slot WALLED ⇒ mix_grp≤2 any M_R) + flat bowtie (on-form max √(B2/B1)=1.034 vs need 2.488, 124 cands); off-form (A_K-degen 0/3, θ_ν env 2/3) also <3; §VII.CK D4→WALLED; FB-saturated op-L4 method
- `s117_lepto_pmns_joint_image.md` -- S117-W3-3 INFO (sign=PASS/mag=INFO): eps_1(φ)∝sin2φ (4 zeros) & δ_CP^PMNS(φ) (2 zeros @{0,π}) CO-SOURCED by 1 M_D phase but NON-independent; joint prediction DISSOLVED (δ_CP UNDER-DET per 3-1 flat + η_B K7-sourced per 3-2); m_1=0 leaves Dirac δ_CP physical (massless eigvec=(1,0,0)); co-viable φ exists (δ_CP=238° consistency, NuFIT band) but NOT a prediction; whole lepton CP+mixing sector under-determined
- `s118_pmns_joint_admissibility.md` -- S118-W2-1 PASS: joint NuFIT 5.2 NO 3σ box (R+3 angles) NON-EMPTY over free (U_eL,V_DR) texture family; under-det SURVIVES. Witness lands all 4 (R_bare=31.576; angles at band centers). f_adm_free=6.85e-5(137/2e6)=f_R·f_angle EXACT; **f_R=1.0 structural** (near-deg B-branch M_R confines R to [27.25,51.01]⊂[17,66]). Contrast shared-εLX R=113.564 OUT→f_adm_shared=0 (V_DR freedom, not Majorana scale, relieves R-overshoot). Closes S117 W2 joint Q. Oscillation-anchored (compatibility≠prediction); J=0 real-textures; CP=separate §VII.BL

External: unified constraint map at `.claude/agent-memory/constraint-map.md`. Knowledge MCP for canonical constants.

## Agent-Private Discipline
- Project context: phonon-exflation on M4 x SU(3); neutrino masses = lightest D_K(s_0) eigenvalues, zero free Yukawa
- Reference papers: `researchers/Neutrino-Detection/` (12 papers, Pauli 1930 -> KATRIN 2024). Library gaps: NuFit-6.0, T2K+NOvA joint, JUNO first results, 0nu-beta-beta, CEvNS (full request: agent-requests/neutrino-request.md)
- Domain working values: keep PDG/NuFit numbers in working memory only; never pin them in agent files (canonical_constants.py is the source of truth)

## Critical Numerical Anchors (working memory; verify against canonical_constants.py before citing)

NuFit-6.0 (Sept 2024) — query mcp__knowledge__.get_constant for canonical pin if downstream cites:
- Delta m^2_21 = 7.41e-5 eV^2; |Delta m^2_32| = 2.507e-3 eV^2 (NO); ratio R_target ~ 33.8
- sin^2(theta_12) = 0.303; sin^2(theta_23) = 0.451 (NO best fit); sin^2(theta_13) = 0.02225
- Mass ordering: NO preferred Delta chi^2 = 6.1
- KATRIN: m_nu < 0.45 eV (90% CL); Planck+DESI DR2: Sum m_i < 0.064 eV (LCDM), < 0.16 eV (w0wa)

## Framework-Side Neutrino Predictions (state through S56)

Structural (parameter-free):
- Lightest D_K(s_0=0.2994) eigenvalues = neutrino masses; mass ordering = sign(lambda_3^2 - lambda_2^2)
- NORMAL ordering predicted; B1<B2<B3 at all tau>0 (bowtie topology)
- Tridiagonal selection rules: V(L1,L3)=0 exact (NNI texture). theta_12 >> theta_13 forced
- Clock constraint: tau frozen 25 ppm => constant masses since condensation

PMNS gate state (post-S52/S56):
- sin^2(theta_13): tunable, achievable at off-Jensen C^2 split eps=0.0918 -> 0.02225 (matches NuFit). Level 4
- sin^2(theta_12), sin^2(theta_23): structurally blocked at Level 5; singlet PMNS is 2x2 (B1,B3); B2 isolated
- R = Delta m^2_32 / Delta m^2_21 ~ 33.8: NOT achieved on Jensen curve. Bare R = 27.2 at fold; sweeps 33 near tau~0.21 but mixing=0 (Schur on U(2))
- All Jensen-curve mechanisms CLOSED through S37 K7-G1 FAIL
- Off-Jensen singlet R at matching split = 7.03 (4.8x below 33.8)

Open routes (uncomputed):
- KK modified Lie derivative coupling Peter-Weyl sectors
- Inter-sector or non-left-invariant mechanisms (required for full 3x3)
- Scale bridge UNRESOLVED: D_K eigenvalues O(1)*M_KK, m_nu < 0.45 eV. M_KK ~ 0.03-0.04 eV from Delta m^2_21 spacing (S40)

## Experimental Landscape (operational status)

JUNO operating since Aug 2025 (mass ordering ~2030); DUNE construction (5sigma ordering 2 yr beam-on); Hyper-K cavern excavated 2025 (data 2028); KATRIN running (final ~0.3 eV); LEGEND-200 first results 2025; KamLAND-Zen complete 2024 (T_1/2 > 3.8e26 yr); MicroBooNE complete Dec 2025 (single sterile neutrino excluded); CONUS+ first reactor CEvNS 2025 (3.7sigma).

## Agent Discipline Reminders (this agent only)
- Demand specific numerical predictions (Delta m^2, mixing angles) when challenged on framework claims
- Frame outcomes as constraints on surviving solution space
- A non-detection constrains as strongly as a detection
- The PMNS Level 4 (theta_13) / Level 5 (theta_12, theta_23) split is the framework's sharpest open neutrino question
