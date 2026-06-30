---
name: S96 Inter-Sector PMNS (B2 wall lifts, R does not)
description: S96-MATTER-PMNS-3X3 INFO — non-left-invariant L_X LIFTS the B2 Schur wall (theta_12/theta_23 open from 0, monotonic, [iK_7,D_K]=0 preserved) but no single eps_LX delivers all four NuFit bands; R structurally unreachable (peak 6.87, band floor 17)
metadata:
  type: project
---

## S96-MATTER-PMNS-3X3 Gate: INFO

**Why:** The hypothesis (a KK-modified NON-left-invariant Lie-derivative L_X breaks the B2 isolation) is PARTIALLY vindicated. The B2 Schur wall IS liftable — turning on L_X opens theta_12 and theta_23 monotonically from exactly 0, with the [iK_7,D_K]=0 Jensen side-condition preserved at every scan point. This is the decisive NEW structural finding: no prior route (S52 off-Jensen, S36 inter-sector left-invariant, S81 T3-S32C) delivered nonzero theta_12/theta_23. The block-diagonality closure (closed_61) bars only LEFT-invariant inter-sector coupling; the non-left-invariant L_X is structurally outside its scope.

**How to apply:** The framework's sharpest open neutrino result is now reframed: **the angles open, R does not.** Future PMNS work should target (a) the family-number frontier #7 and (b) the R scale-bridge, NOT the B2-isolation per se (it is no longer the wall). Do NOT re-run the inter-sector-L_X corridor expecting a full 3x3 PASS — it cannot land all four bands.

## Key Numerical Results (eps_LX scan [0.0,0.10] step 0.005 at tau_fold=0.19)

- Lepton diagonal (M_KK units, from L12 cache sector minima): B1=(0,0) E1=0.8197; B2=(0,1)/(1,0) E2=0.8359 (Schur-walled fundamental); B3=(1,1) E3=0.8730. Bit-exact vs s52 transit fold (resid 2.2e-16).
- CC1 PASS: eps_LX=0 reproduces sin2_12=sin2_23=0.00 EXACT (recovers closed OFFJENSEN-PMNS-52 B2 wall); sin2_13=0.02225 retained (off-Jensen C^2 anchor).
- Wall lifts MONOTONICALLY: sin2_12, sin2_23 both non-decreasing from 0; reach 0.9034/0.4245 at eps_LX=0.10.
- Side-condition: ||[iK_7,M_lep]|| = 0.00e+00 at ALL scan points (q_7-neutral coupling; Jensen SU(3)->U(1)_7 NOT re-broken).
- Anchor eps_LX=0.05: sin2_12=0.7908, sin2_23=0.3322, sin2_13=0.0330, R=4.166 — ALL FOUR out of band.
- Simultaneous membership FALSE at EVERY eps_LX; no point lands even all THREE angles (theta_13 wants eps<=0.035, theta_23 wants eps>=0.060 — mutually exclusive).
- **R is the binding wall**: peak R=6.868 at eps_LX=0.030, 2.48x below NuFit floor [17,66]. Mechanism-INDEPENDENT shortfall (bare fold 3.37 / off-Jensen 7.03 / MSW 3.37 / inter-sector 6.87 — all 2.5-10x short). R set by D_K eigenvalue SPACING at frozen tau; inter-sector coupling cannot fix it.

## Structural Reading

- Track B's "B2 wall is a Level-5 structural obstruction" is PARTIALLY SUPERSEDED: the wall is liftable, contradicting strict structural-obstruction. dual_prior INFO -> posterior UNCHANGED (0.35/0.65).
- Updates the Level-4/Level-5 PMNS split in MEMORY.md: theta_12/theta_23 are no longer "structurally blocked at Level 5" in the absolute sense — they are blocked for LEFT-invariant operators but OPENABLE by non-left-invariant L_X. The residual wall is the JOINT (all-four-simultaneous + R) package, not the angle-isolation.

## Downstream Feed (W4-3 0nubb)

s96_matter_pmns_3x3.npz stores: U (PMNS, U[alpha,i] ascending-mass flavor basis, unitary to 1e-8); m_i=[0.7992,0.8214,0.9081] (|D_K eval|, M_KK units, ascending); U_ei=[-0.4497,0.8745,0.1817] for m_bb=|sum U_ei^2 m_i|. W4-3 sets the absolute eV scale.

## Files
- `computations/session-96/s96_matter_pmns_3x3.py` / `.npz` / `.png`
- Verdict: `computations/session-96/s96_gate_verdicts.txt` audit_sha256=29d70247182d5243b417bdee2c0f2270a073be978b7112aa87ec87017a5a6140
