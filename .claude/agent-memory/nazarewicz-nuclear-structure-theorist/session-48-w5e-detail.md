---
name: session-48-w5e-detail
description: S48 W5-E nuclear structure computations (HFB, Nilsson, PBCS-0D, pair-rotation, protected-chain)
type: project
---

## S48 W5-E NUCLEAR-STRUCT-48 Results (5 sub-computations)

### HFB-SELFCONSIST-48: PASS
- Multi-gap BCS converges all configs (free/uniform/sector), < 32 iter, tol 1e-14
- Free solution: Delta_B2=0.122, Delta_B1=0.140, Delta_B3=0.090 (sector hierarchy preserved)
- Higher-rep screening NEGLIGIBLE: B3 repulsive channel (eig -0.072) vs B2 (eig 2.18) is 30:1 weaker
- Adding B3 to B2-only INCREASES Delta_B2 (0.041 -> 0.122), not decreases. B1 coupling is the key enhancer.
- BCS overestimates vs ED: mode-dependent ratio 0.67-1.72 (NUMBER PROJECTION effect, Paper 03)
- Tau sweep with frozen-V: Delta_B2 decreases monotonically, 10-30% systematic uncertainty
- E_cond at mu=midgap: BCS=-0.502, ED=-0.844 (discrepancy due to mu choice, not method)
- Nuclear benchmark: PBCS/BCS=0.635 matches sd-shell (0.5-0.8)

### NILSSON-48: INFO
- 1 overlap onset (B2 top / (3,0)/(0,3) bottom at tau~0.15)
- 2 near-crossings: (0,0)-(2,0)/(0,2) gap=0.0008 at fold; B2-(3,0)/(0,3) gap=0.037 at tau=0.10
- All branch bandwidths widen monotonically. Nilsson slopes: 0.75 to 1.89 (higher reps faster)
- B2-B3 gap CLOSES with tau (both branches overlap at all sampled tau)
- Fold is NOT a magic deformation. No shell closure. Pairing from VH flat band, not Nilsson crossing.
- Ricci anisotropy: 1.00 (tau=0) -> 1.23 (fold). Drives B1/B2/B3 block structure.

### PBCS-0D-48: INFO
- Condensate contrast: BCS(5.80e8), PBCS(5.81e8), ED(5.92e8) -- all within 2%
- Contrast 95% geometric (character shapes), 5% BCS occupation -- confirms S47 COHERENCE-RESPONSE
- Gap table: PBCS/BCS = 0.636/0.628/0.641 (B1/B2/B3). Matches Paper 03.
- E_cond: PBCS/ED = 0.999, BCS/ED = 0.169. BCS underestimates |E_cond| by 6x for N=1.
- 0D limit (L/xi_GL=0.031): condensate on T^2 is momentum-space pair distribution

### PAIR-ROTATION-48: INFO
- 12.5:1 curvature anisotropy -> only 5.5% pairing anisotropy (M_soft/M_hard=1.055)
- omega_PV anisotropy: 2.7% (soft/hard = 1.027)
- 3 FLAT directions (K=0, U(1)-SU(2)): topologically protected pair propagation channels
- Ricci eigenvalue structure {0.230(x4), 0.250(x1), 0.283(x3)} IS the B2+B1+B3 block structure
- Nuclear analog: weakly deformed pair transfer form factor varies < 5% with K-quantum number

### PROTECTED-CHAIN-48: PASS
- Tr(K_7^2)/16 = 1/8 exactly (not 1/16 -- Trap 3 was about a RATIO e/(a*c), not raw <K_7^2>)
- Authoritative q_7 from S48 joint diag: B2=+/-0.25, B1=0, B3=0
- <q_7^2>_8pos = 1/32 (half the C^16 value; only B2 carries charge)
- BCS-weighted <q_7^2> departs 81% from unweighted (SELECTION EFFECT: B2 enrichment 50% -> 91%)
- <Q_7>_gs = 0 exactly (charge conservation, [H,Q_7]=0 from S34)
- Cooper pairs carry net zero K_7 charge (q_7=+0.25 + q_7=-0.25 = 0)

### CONFIRMED Analogy Additions (S48 W5-E)
- Nilsson diagram of SU(3) ~ weakly deformed sd-shell nucleus (NILSSON-48)
- PBCS/BCS=0.63 matches Paper 03 sd-shell range 3rd independent confirmation (S46, S48 PBCS, S48 HFB)
- Ricci eigenvalue 4+1+3 split encodes B2+B1+B3 block structure (geometric origin of BCS blocks)

### Self-Corrections (S48 W5-E)
- Protected-chain: initially built grand canonical Fock space (N=0 ground state). Should have used N=1 sector. The per-particle weighted average (Section 5) is the correct quantity.
- Trap 3 identity: 1/16 was NOT <K_7^2>. It was e/(a*c) ratio. Actual <K_7^2> = 1/8.
- HFB E_cond discrepancy (BCS -0.502 vs canonical -0.137): mu choice matters for E_cond, not a self-consistency failure. The canonical E_cond uses the S36 N-fixed ED, not grand canonical BCS.
