# Prep Block — S26-P2-COOLING-TRAJECTORY

## Gate Identification

- **Gate ID**: S26-P2-COOLING-TRAJECTORY
- **Parent script**: `computations/session-26/s26_p2_cooling_trajectory.py`
- **rerun script**: `computations/_shared/t3-intake/s26_p2_cooling_trajectory.py`
- **Output verdict**: `computations/_shared/t3-intake/s26_p2_cooling_trajectory_verdict.txt`
- **Trigger**: `[VERIFY]`
- **Classification**: PHONONIC — modulus-chemical-potential coupled dynamics in the BCS condensation window. The tau field is the Jensen deformation parameter driving spectral-action gradients; mu is the BCS chemical potential on the fiber.

## Hypothesis Under Test

**H0** (null, closure): The BCS condensation free energy `F_cond(tau, mu/lmin(tau))` does NOT generate a sustained equilibrium for the modulus tau during the cooling trajectory (mu diluted by Hubble expansion through the BCS window). Static adiabatic lock points in (tau, r) space exist but are dynamically inaccessible because the tau-settling timescale `t_roll ~ O(1)` is much shorter than the dilution timescale `t_dil ~ (mu_0 / lmin)^2 >> 1`.

**H1** (alternative, MARGINAL): At least one (tau_i, pi_i, mu_0, H_0, Tf) configuration in the scanned grid produces a **sustained** modulus lock: `dV_eff/dtau = 0`, `d^2V_eff/dtau^2 > 0`, inside the BCS window, with `|tau_dot| < 0.01 * max|tau_dot|`, and NOT at the V_spec cubic-spline artifact minimum.

## Pass / Fail / INFO Thresholds

| Outcome | Canonical tag | Criterion | Tolerance rule |
|:--------|:--------------|:----------|:---------------|
| **P2-LOCK: MARGINAL** (INFO) | `value=P2-LOCK:_MARGINAL` | `sustained >= 1` across all ODE scans (mu0, H0 coarse, H0 fine, 2D) | ABSOLUTE count |
| **P2-LOCK: CLOSED** (FAIL) | `value=P2-LOCK:_CLOSED` | `sustained == 0` AND no adiabatic lock dynamically accessible | ABSOLUTE count |
| PASS | — | N/A for closure gate — lock existence is negative result | — |

Note: this is a **closure gate**. A FAIL here means the mechanism is closed (maps out solution-space wall), not that the framework has failed.

## Machinery Pin (PRDR)

Every free parameter pinned from the parent script (physics UNCHANGED):

| Parameter | Pinned value | Note |
|:----------|:-------------|:-----|
| `G_TT` (alias `G_DeWitt`) | 5.0 (canonical) | S42 s42_gradient_stiffness |
| `TAU_MAX` | 0.5 | BCS data grid upper bound (`s26_multimode_bcs.npz`) |
| `TAU_I` | 0.15 | Fiducial initial modulus |
| `MR0` (mu_0 / lmin) | 10.0 | Fiducial ratio (above BCS window) |
| `H0` | 0.01 | Fiducial Hubble |
| `TF` | 0.0 | Zero temperature for fiducial |
| H0 coarse | `[0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1.0, 5.0, 10.0]` | 9 points |
| H0 fine | `np.geomspace(0.1, 10., 30)` | 30 log-spaced |
| mu_0 scan | `np.geomspace(2., 50., 20)` | 20 log-spaced |
| 2D scan | `tau_i in [0.02, 0.48] x 8`, `pi_i in [-0.05, 0.05] x 8` | 64 points |
| Tf scans | `{0.5, 0.9}` over H0 fine grid | 60 points total |
| Adiabatic 2D | `tau_scan = linspace(0.005, 0.495, 50)`, `r_scan = linspace(0.85, 1.45, 50)` | 2500 points |
| ODE method | `LSODA` | auto stiff/non-stiff |
| ODE rtol | `1e-4` | relative tolerance |
| ODE atol | `1e-6` | absolute tolerance |
| ODE max_step | `t_end / 100` | |
| exit event | `mu = mu_critical(tau)` terminal, direction=-1 | |
| Lock filter velocity threshold | `0.01 * max|pi|` | transient-rejection cutoff |
| Lock filter V_spec floor | `|dV_spec/dtau| < 0.1` excluded | excludes cubic-spline artifact at tau ~ 0.017 |
| d2V tolerance | `h = 1e-4` finite difference | |
| Random seed | N/A | deterministic integration |
| GPU path | N/A | all integrations are ODE on small state (3 variables); CPU threads capped to 8 |

## Input SHA-256 Pins

| File | SHA-256 |
|:-----|:--------|
| `computations/session-22/s22a_slow_roll.npz` | `57af53bbe9aa7287437562c0704a90151b9b1f89c1f15966c7d58dc231ba11ca` |
| `computations/session-24/s24a_vspec.npz` | `2880f8274d57d22336101766222457d367887114d6fec868f1b894d75a5a3790` |
| `computations/session-26/s26_multimode_bcs.npz` | `868f8e817f6c1472dfc2a1113809ab3ecf82c742a00160af7af88a9c00a2eea8` |
| `computations/session-26/s26_p2_cooling_trajectory.py` (parent) | `af9976d3dc7cd261797f4cc0004bfae8920b30290b451a22a75e10649616bc25` |
| `computations/_shared/canonical_constants.py` | `68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f` |

## Expected Output 4-Tuple

```
value    = P2-LOCK:_CLOSED | P2-LOCK:_MARGINAL
scheme   = LSODA_ODE
convention = G_DeWitt
L_max    = fiducial
```

## Substitution Chain — Cooling-Direction / Lock Criterion

**Step 1 — Definitions:**
- `tau(t)` — modulus (Jensen deformation parameter), dimensionless.
- `mu(t)` — BCS chemical potential, units of `M_KK`.
- `H(t) = H_0 * t_0 / t` — Hubble rate (script convention: `t_0 = 1`).
- `V_spec(tau)` — bare spectral-action potential loaded from `s24a_vspec.npz['V_spec_rho_0p010']`.
- `F_cond(tau, r)` — BCS condensation free energy; `r = mu / lmin(tau)` with `lmin(tau)` from `s26_multimode_bcs.npz` eigenvalues.
- `V_eff(tau, mu, Tf) = V_spec(tau) + F_cond(tau, r) * sqrt(max(0, 1 - Tf^2))`.
- `G_DeWitt = 5.0` — canonical modulus kinetic coefficient (S42).

**Step 2 — Equations of motion (substitute):**
```
  G_DeWitt * tau_ddot + 3*H*G_DeWitt*tau_dot + dV_eff/dtau = 0
  mu_dot = -H * mu
```
(first is Euler-Lagrange with Hubble friction; second is standard dilution.)

**Step 3 — Simplify to canonical lock predicate:**
A "sustained lock" at a point `(tau*, mu*)` along a trajectory is the Boolean conjunction:
```
  Lock = [ dV_eff/dtau|* = 0 ]                       (equilibrium)
       AND [ d^2V_eff/dtau^2|* > 0 ]                  (true minimum)
       AND [ r* in [rlo(tau*), rhi(tau*)] ]           (inside BCS window)
       AND [ |tau_dot|* < 0.01 * max_t |tau_dot| ]    (settled, not ringing)
       AND [ |dV_spec/dtau|(tau*) > 0.1 ]             (not V_spec artifact)
```

**Step 4 — Direction of verdict:**
- `sum over all ODE scans of sustained > 0` ⇒ **P2-LOCK: MARGINAL (INFO)**.
- `sum == 0` ⇒ **P2-LOCK: CLOSED (FAIL)**.
- Static adiabatic lock count (`adiab['lock_points']`) is diagnostic only and does NOT enter the verdict, because at physical `H_0 ~ 0.01`, `t_roll / t_dil ~ 1 / 100` so the modulus settles at `tau ~ 0.018` (V_spec minimum) before `mu` enters the BCS window.

**Step 5 — Constraint-surface consequence:**
- `CLOSED` ⇒ BCS-induced modulus stabilization is eliminated as a geometric channel for tau at this stage of the cooling trajectory. The modulus either pre-settles (low `H_0`) or overshoots the window (high `H_0`), but never locks to a BCS-induced minimum.
- `MARGINAL` ⇒ a narrow parameter wedge supports a sustained equilibrium; further stability analysis (perturbation spectrum, stochastic kicks, finite-T) required.

## Expected Result Justification (Pre-Registered)

Parent run (af9976d3...) yielded CLOSED. The re-run under canonical import and S81 verdict discipline is expected to reproduce this verdict to exact numerical equality since:
1. All physics parameters are imported from or match the parent.
2. `G_DeWitt = 5.0` exactly matches the parent's hardcoded `G_TT = 5.0` (verified via `get_constant("G_DeWitt")` vs source line 247 of canonical_constants.py).
3. No GPU code path — all scans are deterministic CPU ODE integrations.
4. `sd['G_tt'][0]` assertion in `load_and_build` confirms cross-file consistency to `1e-10`.

## What PASSES and What FAILS Mean (Solution-Space Boundaries)

- A **FAIL (CLOSED)** maps a wall: any framework mechanism that posits BCS condensation as the moduli-stabilization channel during dilute-phase cooling is eliminated by this gate.
- A **INFO (MARGINAL)** identifies a surviving sub-region of parameter space; the gate does not confirm BCS stabilization, only that it cannot be trivially excluded under the scanned configurations.
- There is no PASS for this gate — it is a closure/existence test; the binary is closed vs partially open.

## Compliance Checklist

- [x] `from canonical_constants import *` at top of script.
- [x] `G_DeWitt` imported (no hardcoded `G_TT = 5.0`).
- [x] `# (local)` tags on all intermediate / scan / threshold variables.
- [x] First-20-line SHA-256 input pin log in stdout.
- [x] Final closure SHA-256 emitted (64-char hex).
- [x] S81 canonical verdict line is FIRST LINE of verdict file.
- [x] Verdict line carries `value=<v>`, `scheme=<s>`, `convention=<c>`, `L_max=<L>`, `sha256=<64-char>`.
- [x] Substitution chain for direction claim written above.
- [x] Canonical constants file NOT modified.
- [x] OMP/MKL threads capped to 8 (CPU-only path, no heavy linalg).
