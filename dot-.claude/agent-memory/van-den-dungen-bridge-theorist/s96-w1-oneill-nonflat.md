---
name: S96-W1-ONEILL-NONFLAT design + result
description: Spectral-action cross-terms S_cross under non-flat SU(3) bundle (O'Neill A!=0); quadratic in ||F_omega||; effacement-suppressed at Hubble-physical scale
metadata:
  type: project
---

# S96-W1-ONEILL-NONFLAT (van-den-dungen gate, S96 W1 gate 2)

**The question S83 deferred.** S83 W2-G24 (NONFLAT-T-CORRECTION-L2) addressed the INTERNAL SU(3) fiber Cartan-protection (p_1(T^V)=0 on Cartan, ratio=0 EXACT). Its boundary line: "Base M^4 Pontryagin contribution via Kasparov exterior product is a SEPARATE question, not addressed here." THIS gate IS that separate question: the spectral-action cross-terms when the BASE M^4 carries a non-flat principal connection (O'Neill A = connection curvature F_omega != 0).

**Structural anchors (knowledge MCP + corpus):**
- Paper 01 Prop 4.3 (session-73a-mack-vdd-workshop): `a_2(D_total)=a_0(D_M)a_2(D_K)+a_2(D_M)a_0(D_K)` with cross-terms BOUNDED BY the O'Neill tensors A and T. M^4 x SU(3): A=T=0 EXACT (S61).
- Baptista Paper 13 eq (3.4) (s74_a_tensor_correction.py): `R_P = R_M + R_K - |F|^2 - |S|^2 - |N|^2 - 2 d_check N`; F = O'Neill A-tensor (= connection curvature, vanishes iff horizontal distribution integrable = flat product); S = T-tensor (2nd fund form, Higgs kinetic); squared total Dirac `D_P^2 = D_M^2 + D_K^2 + V_AT + V_T`.
- S85 base-Pontryagin convention `Riemannian-submersion-with-non-flat-base`: `R_E = R_F + pi*R_M + A-tensor + T-tensor`; under A=T=0 -> `R_E = R_F (+) pi*R_M` direct sum (THE additivity); cross-term `2 tr(R_F ^ pi*R_M)`.
- O'Neill formula (session-54): `K_M(X,Y) = K_total(X,Y) + 3|A_X Y|^2`. A_X Y = (1/2)V[X^H,Y^H] = connection curvature. ||A|| prop ||F_omega|| LINEAR; a4^cross prop Tr(A A) prop ||F_omega||^2 QUADRATIC.

**A-tensor magnitude convention (S74 A-TENSOR-CORRECTION-74, established framework):**
- dimensionless A-tensor vertex param `eps_AT := (H/M_KK)^2`.
- matrix element bound `|A_{(p,q),(p',q')}| <= C_adj * omega_max[(p,q)] * sqrt(eps_AT)`, C_adj <= sqrt(Cas_adj)=sqrt(3)=1.7321.
- Wigner-Eckart selection rule: A connects (p,q)->(p',q') iff (p',q') in (p,q) (x) Ad=(1,1). CG decomp `(p,q)(x)(1,1) = (p+1,q+1)+(p+2,q-1)+(p-1,q+2)+(p+1,q-2)+(p-2,q+1)+2(p,q)+(p-1,q-1)` (drop negative indices).

**CRITICAL CONVENTION DECISION (||F_omega|| units):**
The plan scans ||F_omega|| in [0,1], "1.0 = phys scale". TWO readings:
- Reading A (Hubble-set, S74): ||F_omega||_phys <-> eps_AT_phys=(H_0/M_KK)^2 = 3.75e-118 (today). Cross-term ratio at phys ~10^-118 << 3e-7 INFO band; gate trivially PASS, no discrimination. This is the ACTUAL-PHYSICS value (effacement-suppressed).
- Reading B (O(1) curvature, units M_KK^2): ||F_omega||=1 means connection curvature of order the fiber scale. This is the STRUCTURAL STRESS TEST and the ONLY reading where the bands (1e-3 PASS / O(1) FAIL / 3e-7 INFO) discriminate.
PRIMARY scan = Reading B (the band-discriminating stress test). CROSS-CHECK = Reading A (shows actual physics is effacement-suppressed far below INFO). This is faithful: the substitution chain tests the quadratic COEFFICIENT; Reading B exposes it.

**Result:** (to be filled after run)
