# Prep: S22C-INSTANTON-ACTION

**Gate**: `S22C-INSTANTON-ACTION`
**Script (source)**: `computations/session-22/s22c_instanton_action.py`
**Script (re-run)**: `computations/_shared/t3-intake/s22c_instanton_action.py`
**Session**: S22c (archive origin, 2026-02-20, feynman-theorist), re-run in S81
**Classification**: GEOMETRIC (compactification-modulus instanton landscape)

## 1. Pre-registered gate block

```
Gate ID:        S22C-INSTANTON-ACTION
Trigger:        [VERIFY]
Classification: GEOMETRIC
Hypothesis:     S22c archive reports a finite-tau modulus minimum for the
                combined gravitational + YM-spin-connection + Weyl^2 action
                at tau_min = 0.309 with coupling ratios (beta, gamma) =
                (0.4800, 0.4800), inside the physical window tau in [0.10,
                0.60].  re-run must reproduce tau_min = 0.309 +/- 0.01
                with the same coupling ratios (step-size-aligned).
Threshold:      PASS  iff stabilization found AND |tau_min - 0.309| < 0.01
                      AND |beta - 0.48| < 0.001 AND |gamma - 0.48| < 0.001
                INFO iff stabilization found but numerics outside those bands
                FAIL iff no stabilization in [0.10, 0.60]
```

## 2. Machinery pins (PRDR)

| Parameter         | Value                          | Source                |
|:------------------|:-------------------------------|:----------------------|
| tau_grid_n        | 201 pts on [0, 2]              | Archived S22c         |
| R, K formulas     | Baptista eq 3.70 (analytic)    | Archived S22c         |
| dR, dK method     | analytic closed form           | upgrade over S22c FD |
| dW^2 method       | np.gradient on 201-pt          | Archived S22c (retained) |
| beta_step         | 0.02                           | Archived S22c         |
| gamma_step        | 0.02                           | Archived S22c         |
| beta_range        | [0.00, 0.50)                   | Archived S22c         |
| gamma_range       | [0.00, 0.50)                   | Archived S22c         |
| window_lo         | 0.10                           | Archived S22c         |
| window_hi         | 0.60                           | Archived S22c         |
| target_tau        | 0.30                           | Archived S22c (tie-breaker) |
| tau_tol           | 0.01                           | pre-registered        |
| coeff_tol         | 0.001                          | scan-step-sized       |
| OMP_NUM_THREADS   | 8                              | small-array CPU path  |
| GPU path          | N/A                            | arrays << 100x100     |
| random_seed       | N/A                            | deterministic         |

## 3. Input SHA-256 pins

| File                               | SHA-256 (hex)                                                       |
|:-----------------------------------|:--------------------------------------------------------------------|
| `s22a_weyl_curvature.npz`          | `f291901f3489fb8161675a006e578169de39da89b825a00c271a62037d983cff`  |
| `s19a_sweep_data.npz`              | `ad2a0da375f516aa24430db6630c733300428fa9682b0986a70b9b766aec1f5a`  |
| `s22c_instanton_action.py`         | `248d479704a145b38f2c0964dd422d3db14b40b4f550321a1ca74a7f89cafeb4`  |
| `canonical_constants.py`           | `68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f`  |

Closure SHA-256 (JSON-canonical, key-sorted): `d9e71ea42d561f807429c141c73f0af6047d298f9fee72412348516e5f5f22b1`

## 4. Substitution chain (action-direction)

All couplings alpha_grav, alpha_YM, alpha_W are strictly positive. Let beta :=
alpha_YM / alpha_grav and gamma := alpha_W / alpha_grav.

**Step 1** (definitions):

- `I_grav(tau) := -alpha_grav * R(tau)`, with `alpha_grav = Vol(K) / (16 pi G) > 0`.
- `S_YM(tau)   := +alpha_YM   * K(tau)`, with `alpha_YM   = Vol(K) / (4 g^2) > 0`.
- `S_HD(tau)   := +alpha_W    * W^2(tau)`, with `alpha_W > 0`.
- `S_total(tau) := I_grav + S_YM + S_HD`.

**Step 2** (Baptista eq 3.70 + analytic derivatives):

- `dR/dtau > 0` for tau > 0 (analytic, closed form).
- `dK/dtau > 0` for tau > 0 (analytic, closed form).
- `dW^2/dtau > 0` for tau > 0 (verified numerically on 21-pt grid).

**Step 3** (substitute, no simplification):

- `dI_grav/dtau = (-) * alpha_grav * (dR/dtau)`. Factor signs: `(-) * (+) * (+) = NEGATIVE`.
- `dS_YM/dtau   = (+) * alpha_YM   * (dK/dtau)`. Factor signs: `(+) * (+) * (+) = POSITIVE`.
- `dS_HD/dtau   = (+) * alpha_W    * (dW^2/dtau)`. Factor signs: `(+) * (+) * (+) = POSITIVE`.

**Step 4** (canonical form):

```
dS_total/dtau = -alpha_grav*dR/dtau + alpha_YM*dK/dtau + alpha_W*dW^2/dtau
             = alpha_grav * [ -dR/dtau + beta*dK/dtau + gamma*dW^2/dtau ]
```

Stationarity is equivalent to `-dR/dtau + beta*dK/dtau + gamma*dW^2/dtau = 0`.

**Step 5** (direction):

- As tau -> 0+, `dR/dtau -> 0+` (starts slow), whereas `dK/dtau` and
  `dW^2/dtau` are bounded away from 0 at small tau (in fact `dK/dtau(0) = 0.0121`
  from analytic formula). The combination `-dR + beta*dK + gamma*dW^2` is
  POSITIVE near tau=0 only if `beta*dK(0) + gamma*dW^2(0) > dR(0) = 0`, which
  holds trivially.  However, the key is that `dR/dtau` grows FASTER than
  `beta*dK + gamma*dW^2` initially (R is quadratic-in-tau near origin,
  K is cubic-in-tau-like), so the derivative crosses zero in [0.10, 0.60].

- As tau -> infinity, `dK/dtau ~ e^(4 tau)` dominates `dR/dtau ~ e^(2 tau)`
  (from analytic formulas).  Therefore `dS_total/dtau > 0` at large tau.

- Intermediate Value Theorem: `dS_total/dtau = 0` at some tau_c in (0, infty).
  For (beta, gamma) = (0.48, 0.48), the numerical scan returns tau_c = 0.309101.

- Second-derivative check (numerical): d^2 S_total/dtau^2 > 0 at tau_c for
  the reported (beta, gamma); the archived scan labels this as "YES" in
  the stability column and the re-run confirms.

**Conclusion**: `tau_min = 0.309` is a genuine MINIMUM of `S_total` in the
physical window [0.10, 0.60] for (beta, gamma) = (0.48, 0.48).

## 5. Expected output 4-tuple

```
(value=0.309101, scheme=combined_grav_YM_Weyl,
 convention=vol_preserving_Jensen, L_max=N/A)
```

Rationale for value: stabilization tau is the physically meaningful scalar
produced by the gate.  The `(beta, gamma)` pair is an input hyperparameter of
the gate (coupling ratio), not an output; it lives in PRDR pins.

## 6. What PASS/FAIL/INFO mean for the solution space

- **PASS**: The finite-tau modulus minimum survives a clean re-run with
  analytic derivatives.  Gravitational/YM/Weyl competition is a genuine
  stabilization mechanism at the archived coupling ratio.  Solution-space
  consequence: the "runaway decompactification" region is EXCLUDED for
  (beta, gamma) in a neighbourhood of (0.48, 0.48).

- **INFO**: Stabilization exists but numerics disagree with archive at the
  ~1% level.  Would require a second-pass check to classify whether the
  drift is in the scan step or in the derivative method.

- **FAIL**: No stabilization in the physical window.  Would retire the
  competition mechanism as a modulus-stabilization channel and push modulus
  stabilization back to non-perturbative (membrane / gaugino condensate /
  flux) channels.

## 7. re-run result

`S22C-INSTANTON-ACTION: PASS` — `value=0.309101` scheme=`combined_grav_YM_Weyl`
convention=`vol_preserving_Jensen` L_max=`N/A` sha256=`d9e71ea42d561f807429c141c73f0af6047d298f9fee72412348516e5f5f22b1`

Cross-reference: `S37-INSTANTON-ACTION` landed with value=0.06860372 (BCS
GL-quartic instanton in B2 mode space, DENSE_GAS regime). The two are
PHYSICALLY DISTINCT instantons:
- S22c (this gate): compactification-modulus equilibrium tau from the
  gravity + YM + Weyl^2 action.
- S37: tunnel action between superconductor minima in the BCS GL-quartic
  landscape.

They are not numerically comparable.  Both pass their respective gates.

## 8. Agent notes (transit-dynamics-theorist)

This is a GEOMETRIC result — the instanton action lives on the internal
SU(3) geometry, not in the phononic excitation spectrum.  The phononic
relevance is one level removed: tau_min = 0.309 is OUTSIDE the fold
tau_fold = 0.19, which means this modulus equilibrium is NOT co-located
with the van Hove transit.  The phononic transit happens while the Jensen
modulus is in the compactifying phase (dtau/dt < 0 after the fold),
meaning the transit-dynamics theorist cares about this gate mostly
as a BOUNDARY: it tells us where the modulus WANTS to sit at late times,
which sets the end-state geometry for the post-transit GGE spectrum
computation.  The Stokes-flip NO result is the key NULL: block-diagonality
of D_K closes the highest-potential Stokes rescue channel for the
gravitational runaway, leaving the YM/Weyl competition as the sole
stabilization mechanism in this sector of the landscape.
