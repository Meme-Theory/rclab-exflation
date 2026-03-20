---
name: cdm-construct-43-result
description: CDM-CONSTRUCT-43 PASS. GGE quasiparticles are CDM by construction (T^{0i}=0, v_fs=0, w=0). Both S42 and S43 lambda_fs estimates RETRACTED as category errors. Internal modes carry energy not 4D momentum. Supersedes CDM-RETRACTION-44 and FLAT-DM-44.
type: project
---

## CDM-CONSTRUCT-43: GGE is CDM by Construction

### Gate Result: PASS (2026-03-14)

GGE quasiparticles have T^{0i}_4D = 0 identically. They are CDM by construction, not by parameter tuning.

### Core Argument

GGE modes are occupation numbers n_k of internal-space KK harmonics Y_n(y) on SU(3). After KK reduction, phi(x,y) = sum psi_n(x) Y_n(y), each 4D field psi_n has mass m_n but k_4D = 0 (homogeneous quench creates excitations at rest). The GGE is a product state (S_ent=0). Therefore:
- T^{0i} = 0 (no 4D momentum density)
- T^{ij} = 0 (no pressure, w=0 exactly)
- T^{mu nu} = diag(rho, 0, 0, 0) = pressureless dust

### Key Numbers
- v_fs = 0 c (exact, by construction)
- v_eff (domain wall upper bound) = 2.37e-6 c << 10^{-3} c (CDM threshold)
- w = 0 (pressureless dust)
- c_q_4D = 1.28 c (S43 WRONG -- superluminal = category error smoking gun)

### Two Prior Estimates RETRACTED
- S42: lambda_fs = 3.1e-48 Mpc (conflated internal/external momentum)
- S43 W2-1: lambda_fs = 89 Mpc (converted internal c_q to 4D velocity)
- CORRECT: lambda_fs = 0 Mpc (internal modes don't free-stream in 4D)

### Superfluid Analog
GGE modes are NOT Volovik's "normal component" (Paper 37). Normal component requires propagating excitations with v_g != 0 in spacetime. GGE modes have v_g = 0 in 4D. Correct analog: impurities frozen in crystal lattice (gravitate but don't flow).

### Dissolved Gates
1. FLAT-DM-44 (mixed CDM/HDM): DISSOLVED (all branches v_4D = 0)
2. CDM-RETRACTION-44: SUPERSEDED (concept doesn't apply)
3. DM-DE-RATIO-44: DM part clarified (all CDM, problem = abundance = CC)

**Why:** Resolves the DM categorization question permanently. The free-streaming concept is a category error when applied to internal-space occupation numbers.

**How to apply:** Never again compute lambda_fs for internal modes. The DM problem is now exclusively an abundance problem (= CC problem). Any future DM discussion should start from "CDM by construction" and focus on rho_DM magnitude.
