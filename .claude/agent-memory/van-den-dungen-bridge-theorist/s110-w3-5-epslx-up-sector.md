---
name: s110-w3-5-epslx-up-sector
description: S110-CF2-YUK-EPSLX — external non-LI eps_LX with pairing-dependent off-diagonal texture reaches the UP-sector m_t:m_c:m_u hierarchy (INFO) but not full flavor; the Casimir-tower 9/5 log-gap lock is a permanent rep-theoretic identity
metadata:
  type: project
---

**S110-CF2-YUK-EPSLX verdict: INFO** (sign=PASS / mag=INFO / regime=VALID). audit_sha256 `6bf24987423ea20797d451fad5153a74a0eafddab0a351173e03f10276ee7be4`.

**Why:** the Yukawa rank-1 wall ([[s82-kasparov-abelian-proof]] family; J_12/J_23=19.52 PROVEN S62) is escaped ONLY by an external non-LI delta_A (S98-W3-1 existence-PROVEN, value=0.0; PROVEN corollary). S100a-FREEZEIN-OVERCONSTRAINED FAILED the magnitude with a SINGLE shared off-diagonal w (3 inputs {S0,|w|,argw}, mass_grp=2/6). This gate's refinement = pairing-dependent off-diagonal texture {rho13,rho23} (S100a is the rho=1 slice), 4 inputs.

**How to apply (durable structural findings for any future Yukawa-hierarchy gate):**

1. **The Casimir-tower 9/5 lock is a PERMANENT representation-theoretic identity** (NOT a fit artifact): in the diagonal-dominant branch with tower (1,0)/(1,1)/(3,0), C2=(4/3,3,6), the up-sector cross-gen log-gap ratio `ln(m_c/m_u)/ln(m_t/m_c) = (C2(1,1)-C2(3,0))/(C2(1,0)-C2(1,1)) = 3/(5/3) = 9/5 = 1.800 EXACT`. PDG wants 1.2992. A SINGLE shared w CANNOT move this (correlated perturbation preserves gap-ordering) — that is the structural reason S100a got mass_grp=2/6. This 9/5 identity will recur in ANY diagonal-Casimir Yukawa ansatz; cite it, do not re-derive.

2. **Pairing-dependent off-diagonal DOES break the 9/5 lock** (the 1<->3 = u<->t coupling w_13 decouples the two log-gaps): rank lifts 1->3, J_12/J_23 departs 19.52 by 99.96%, BOTH up ratios land in-band (m_c/m_u logdist 0.000, m_t/m_c logdist 0.035). This is the Kasparov-factorization-forbidden off-diagonal: a clean [D_M](x)[D_K] product (Paper 01 submersion) has NO inter-generation mixing; non-LI delta_A supplies it.

3. **SCOPE BOUNDARY (the load-bearing finding): up-sector reachable, full-flavor NOT** (this gate). mass_grp stays 2/6 = NON-PROMOTION-BY-HELD-NUMBER: the 4 held-out slots (3 same-gen ratios locked to ~1 by the Lambda_u=Lambda_d J-conjugacy [S100a D4], + down-only m_s/m_d) are structurally unaddressed by an up-only fit. The same-gen=1 J-conjugacy lock is the binding obstruction to a FULL-flavor PASS, NOT the off-diagonal texture. rho23 hit the physical floor 0.1 (boundary-limited, resid 0.081).

4. **Capstone #7 / §VII.BL discipline**: composite=INFO => do NOT tag m_t:m_c:m_u "DERIVED". The constructive complement to §VII.BL Generation-Blindness is STRENGTHENED for the up-sector but NOT promoted.

5. **Cross-gate pair**: CF1-YUK-C2COSET (§W3-4, baptista) FAILed same session — C²-coset multiplicity-scalar (|dY12/ddelta|0=8.7e-16), CV-8 Arm-G DEAD, internal route shut. CF1 (internal door shut) + CF2 (external door opens for up-sector only) are a clean adversarial pair. With Arm-G dead, eps_LX is the SOLE hierarchy route.

**Open carry-forward**: full-flavor magnitude = down-sector + CKM + breaking the same-gen J-conjugacy lock (Lambda_u != Lambda_d). The up-only texture cannot reach it; a future gate needs a mechanism that distinguishes the up and down towers' freeze-in normalizations.
