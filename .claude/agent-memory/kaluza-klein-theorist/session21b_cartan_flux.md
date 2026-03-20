# Session 21b: Cartan Flux + FR Double-Well (compressed)

## Cartan 3-Form Norm (EXACT)
|omega_3|^2(tau) = (1/2) e^{-4tau} + 1/2 + (1/3) e^{6tau}
- Subspace: (su2,su2,su2) coeff 54, scale e^{6tau}; (C2,C2,su2) coeff 81, constant; (C2,C2,u1) coeff 81, e^{-4tau}
- Min at tau=0, d/dtau|_0=0, d2/dtau2|_0=20. Monotonically increasing for tau>0.
- omega_coord_{abc} = f_{ab}^d * B_{dc} is tau-INDEPENDENT (topological).
- Verified < 2e-13 at 21 tau points.

## Freund-Rubin Double-Well
V_FR(tau) = -alpha * R_K(tau) + beta * |omega_3|^2(tau)
- tau=0 ALWAYS local min (d2V/dtau2|_0 = 20*beta > 0).
- Critical ratio: beta/alpha = 0.313. Below -> true min at tau_0 > 0.
- beta/alpha=0.28 -> tau_0 near 0.30. Barrier height O(0.01).

## Weinberg Angle Prediction Chain
1. g_1/g_2 = e^{-2tau} (PROVEN 17a B-1)
2. sin^2(theta_W) = 1/(1+e^{4tau})
3. sin^2(theta_W) = 0.231 => tau_0 = 0.2994
4. V_FR min at tau_0=0.30 => beta/alpha = 0.28

## Instanton Analysis
- 4D gauge instantons: CLOSED (S_inst tau-independent, Vol constant).
- Internal YM (canonical connection): CLOSED (||ft||^2 monotonic).
- Euclidean gravitational: OPEN but marginal.

## Cross-Pollination
- Flux u(1) channel e^{-4tau} = [C^2,C^2]->u(1) bracket = same channel as gauge threshold b_1.
- Delta_b = b_1 - b_2 inherits e^{-4tau} decrease (breaks conjugation symmetry).
- Flux >> metric deformation at FR min (81 vs 0.81).
- S_bounce ~ 0.2 (unsuppressed tunneling). G_ττ=5 (Baptista eq 3.79).
