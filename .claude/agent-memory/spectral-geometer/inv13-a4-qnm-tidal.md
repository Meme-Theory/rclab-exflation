---
name: inv13-a4-qnm-tidal
description: a_4 higher-curvature -> BH QNM ringdown + NS tidal Love correction; sign chain + OOM (INV13-W1-2 INFO, definite-sign sub-detectable)
metadata:
  type: project
---

INV13-W1-2-A4-HIGHER-CURVATURE-QNM-TIDAL ([SIGN] gate, investigation-13, INFO; audit_sha256 `86e848e88cb1b5391f084482590c8ae27cf55bc137843f8dcd46b9ac0a3dd50d`). The a_4 Seeley-DeWitt moment generates an emergent higher-curvature (R^2+Weyl^2+Gauss-Bonnet) correction to the EXTERIOR strong-field observables (distinct from inv-11 W5-2 interior construction).

**Sign chain (PERMANENT, reusable for any a_4 strong-field falsifier)**: delta_omega/omega and delta_k2/k2 are DEFINITE-POSITIVE.
- c_W = +2/360 (Gilkey a_4 Riem^2 coeff). On Schwarzschild/Kerr R=Ric=0 => Weyl^2 = Riem^2 = Kretschmann = +48 M^2/r^6 > 0; Gauss-Bonnet is a 4D total derivative (NO local EOM). So the dynamical Weyl^2 coupling inherits c_W>0.
- sign(delta_omega/omega) = sign(c_W)*sign(a_4/a_2)*sign(k_QNM) = (+)(+)(+) = + (positive Weyl^2 STIFFENS the Regge-Wheeler barrier => raises Re(omega) => blue-shift). delta_k2/k2 > 0 from the same c_W>0 (star marginally more deformable).

**Magnitude (OOM, the load-bearing INFO driver)**: emergent coupling alpha_HC = (a_4^{zeta}/a_2^{zeta})*ell_KK^2 = 3.433e-66 m^2, ell_KK = hbar/(M_KK c) = 2.656e-33 m (M_KK Compton length). Dimensionless eps = alpha_HC/r_scale^2.
- QNM 10 Msun: delta_omega/omega = +4.58e-78 (eps_QNM ~ 1.57e-74). Scales 1/M_BH^2 -> +4.58e-92 at 1e8 Msun.
- NS tidal 1.4 Msun: delta_k2/k2 = +1.32e-76 (eps_NS ~ 2.38e-74).
- m = max = 1.32e-76 vs D_thr=1e-3 => ~73 OOM below detectability => INFO (sign PASS, magnitude INFO, regime VALID). This is the universal (ell_fundamental/r_observable)^2 = (GUT-scale/astro-scale)^2 ~ (10^-37)^2 suppression -- ANY quantum-gravity/extra-dim correction to astrophysical-scale curvature is unobservable on this channel. Definite-sign sub-detectable NULL, NOT a falsification.

**Factor-counting note (where errors hide)**: script normalizes eps by M_geo^2 = (GM/c^2)^2 (the M=1 QNM convention, M*omega units); r_S^2 = (2GM/c^2)^2 = 4*M_geo^2 differs by exactly 4. OOM + verdict invariant. The M=1 convention is the QNM-standard choice.

**GR anchor cross-check**: Leaver l=2 n=0 M*omega = 0.373672 - 0.088962i; independent WKB(1) Re-part 0.3890 (4.1%) confirms self-sourced. k_QNM = 8.125e-5 from first-order potential-perturbation overlap of the localized WKB mode with the Kretschmann source.

Canonical pins: a_2_FW_zeta=2776.165389, a_4_FW_zeta=1350.7216, M_KK=7.42866e16 GeV (all CONST-FREEZE-42/S88/S75). The plan's a_2_fold/a_4_fold ARE these zeta values (not separate constants). Regulator: a_4^{zeta}+a_2^{zeta} (MANDATORY tag, bare a_n FORBIDDEN). Script: computations/investigation-13/inv13_w1_a4_higher_curvature_qnm_tidal.py. Related: [[key-results.md]] (heat-kernel hierarchy a_0>a_2>a_4).
