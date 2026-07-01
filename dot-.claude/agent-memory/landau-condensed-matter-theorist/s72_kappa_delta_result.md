---
name: S72 KAPPA-DELTA-72 Result
description: Self-consistent BCS gap curvature at van Hove fold — gap has nonzero first derivative, decoherence from amplitude negligible
type: project
---

## KAPPA-DELTA-72 — Gate: INFO

**Key result**: Delta(tau) does NOT have a maximum at the van Hove fold. d(Delta)/dtau = -0.245 M_KK at fold (nonzero linear slope). The gap decreases monotonically with increasing tau across the entire scan range.

**Why:** The task assumed d(Delta)/dtau = 0 at fold (van Hove = maximum of gap). Wrong. The van Hove singularity maximizes the DOS, but the gap depends on both DOS and mode energies. As tau increases through the fold, all mode energies decrease, reducing pairing strength faster than the DOS enhancement at fold can compensate.

**How to apply:** The Landau-Khalatnikov decoherence formula (E1.2/E1.4 WS3) assumed quadratic gap variation. With LINEAR variation dominating, decoherence from gap amplitude dynamics is negligible (t_dec/t_transit ~ 5.5e9, delta_OOM ~ 1.6e-10). The A_s budget cannot be closed by gap curvature. Decoherence must come from PHASE dynamics (Leggett mode, Josephson phase diffusion), not amplitude dynamics.

**Numbers:**
- kappa_Delta (d^2Delta/dtau^2 at fold) = +0.330 M_KK (positive = decelerating decrease)
- d(Delta)/dtau at fold = -0.245 M_KK (dominant linear term)
- Delta_fold = 0.46425 M_KK (matches canonical exactly)
- Delta variation over transit: 0.5% (negligible)
- t_dec/t_transit = 5.5e9

**PERMANENT**: chirp kappa_n(B2) ~ 6e8 is d^2(k_tach)/dtau^2, NOT d^2(eps)/dtau^2 ~ 4.4. These are different quantities by ~8 OOM.

**PERMANENT**: BCS Hamiltonian requires DOS weighting (V * sqrt(rho_k*rho_l)) to reproduce canonical Delta_BCS = 0.4643. Without DOS weighting, gap = 0.180 (different quantity). The s36/s37 Hamiltonian is the canonical one.

Files: `computations/s72_kappa_delta.{py,npz,png}`
