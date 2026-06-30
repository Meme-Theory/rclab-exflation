---
name: s111-clockloc2-monotone-corridor
description: S111 CLOCKLOC2 PASS — Level-2 clock tau strictly monotone on transit corridor [0,0.19], first turning point tau_overshoot=1.614 NEC-censored. The dimensionless-modulus EOM normalization lesson for any future turning-point/phase-flow gate on the Jensen manifold.
metadata:
  type: project
---

# S111 CLOCKLOC2-MONOTONE — corridor monotonicity PASS + the EOM-normalization lesson

**Result (S111-CF-CLOCKLOC2-MONOTONE, PASS, [SIGN] PASS/PASS/VALID).** The Level-2 clock tau (Jensen modulus) is strictly monotone (tau_dot>0) on the transit corridor [0,0.19]: min(tau_dot)|[0,0.19]=1.814473>0, NO interior zero on the landed domain [0,0.5]. First turning point tau_turn=tau_overshoot=1.614 (S77 energy-conservation turnaround E_turnaround=V(1.614), S76 T1.4), in the NEC-censored region tau>tau_NEC=1.383. So [0,0.19] strictly interior to (0, tau_turn) => the (D)-deparametrization t_internal:=int dtau/tau_dot is well-posed on the corridor (tau_dot != 0), bounding CLOCKLOC1's (D)-leg integration domain. This CLOSES the monotone-corridor leg the S110 WS-CLOCKLOC entry pre-registered (see [[s110-ws-clockloc-layer-resolution]] "CF-2 well-posed on transit corridor [0,0.19]"). The N_zeros=1 single-asymmetric-open Penrose diagram (S96-GEOM-PENROSE-2CONE) is the causal image of this one-directional clock.
audit_sha256 = 62619fb344de965fa47a6ea738387b2039824830565f550da86aece64e056b78.

## EOM-normalization lesson (the non-obvious part; recurs for CLOCKLOC1 + any modulus-EOM gate)

**Why:** the substrate is DIMENSIONLESS (tau, a dimensionless; t in M_KK^{-1}; INV4 inv4_w2_raychaudhuri_focusing.py:397). The S19b homogeneous-sector EOM is `tau_ddot = -3H tau_dot - (1/G_DeWitt) dV/dtau` with G_DeWitt=5.0 (so 1/G_DeWitt=1/5, matching the plan's -(1/5)dV/dtau). The (C) Hamiltonian constraint (ws-clockloc.md:196) closes H: `3 M_P^2 H^2 = (5/2)tau_dot^2 + V(tau)` (emergent-4D FRW is shear-free sigma_4D=0, so the internal Kasner shear sigma^2=5 tau_dot^2 enters (C) ONLY as the (5/2)tau_dot^2 kinetic term; G_DeWitt=5 => KE=(1/2)G_DeWitt tau_dot^2=(5/2)tau_dot^2).

**The trap (cost me one wrong run):** feeding the RAW `dV/dtau ~= 58672` (= dS_fold, the spectral-action gradient) into the EOM in a dimensionless frame where H~O(1) OVER-DRIVES the deceleration by ~4 OOM. The landed V_spec(tau)=S_full(tau) ~ 2.5e5 carries an overall Lambda^4 a_0 magnitude that is NOT the kinematic scale. Symptom: tau_dot driven to 0 at tau~0.008 (a SPURIOUS turning point), and a friction-scan oscillating True/False/True (the tau_dot=0 event detector catching +/-0 float crossings at a degenerate IC). That is a NUMERICAL bug, NOT physics.

**How to apply:** the physically-commensurate force in the dimensionless modulus EOM is the LOGARITHMIC (scale-free) gradient `-(1/G_DeWitt) * d ln V/dtau`. At the fold d ln V/dtau = dS_fold/V_fold = 58672.80/250360.68 = 0.234353 — an O(1) dimensionless driving, commensurate with H~O(1). CRUCIAL: sign(d ln V/dtau) == sign(dV/dtau) (V>0 everywhere), so the normalization choice CANNOT flip a directional [SIGN] verdict — only the turning-point magnitude scale. For the turning point ABOVE the landed domain [0,0.5], do NOT integrate to it (would need D_K diagonalization, forbidden) — ANCHOR tau_turn to the S77 energy-conservation map (tau_overshoot=1.614). Integrate in tau (the Level-2 clock) as the independent variable; cross-check against the INV4 raychaudhuri tau_dot trajectory (tau_dot=3H, S101 n=2 closure; min tau_dot|[0,0.22]=0.4915>0).

## Canonical anchors used (verified this run)
- G_DeWitt=5.0, tau_fold=0.19, tau_NEC=1.383, tau_overshoot=1.614, dS_fold=58672.80241318 (all canonical_constants.py).
- V_spec(fold)=S_full(0.19)=250360.68 (s36_sfull_tau_stabilization.npz; spline dV reproduces dS_fold to rel 2.3e-10 = CC1).
- Landed potential domain [0,0.5] only (16 pts); above it, the turning-point MAP governs.
