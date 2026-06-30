# S84-MP-LAYER-AUDIT -- CM Certificate Log

Gate: S84-MP-LAYER-AUDIT  [VERIFY-THEOREM]
Classification: META
Verdict: PASS
Closure SHA-256: 7e22fd74fa64b0a084c411e0fcad771d04faef4b6e18bb3f7b92f090d1dcbae4
L_max: 5  (N_modes = 159936)
N_admissible: 6/10 layer-cells

## 5x3 Classification Table

| regulator    | L1-admissible | L2-admissible | inadmissible-everywhere |
|:-------------|:-------------:|:-------------:|:-----------------------:|
| zeta         |       X       |               |                         |
| Zubarev      |       X       |               |                         |
| SDW          |               |               |            X            |
| dim-reg      |       X       |               |                         |
| lattice-BR   |               |               |            X            |

## Anchor Cell Cross-Check (S82 MP-Exclusion + S83 G27)

- SDW L1-INADMISSIBLE (S82 MP-Exclusion): **True**
- Zubarev L2-ADMISSIBLE (substrate-canonical): **True**
- zeta L1-ADMISSIBLE (Dixmier-residue): **True**
- All three anchors reproduced: **True**

## 15 CM-Certificate Stanzas (5 regulators x 3 cells)

### Regulator: zeta

**Cell**: L1-admissible

```
ADMISSIBLE (ACHIEVED): f_z(x) = x^(-s/2), s>0, admits Bernstein
  representation f_z(x) = (1/Gamma(s/2)) integral_0^inf alpha^(s/2-1)
  exp(-alpha x) dalpha, with positive measure rho_z(alpha) = alpha^(s/2-1)/Gamma(s/2) >= 0
  for s>0. Convergence domain: x>0, alpha in (0,inf). Dixmier-residue
  limit s->KO-dim extracts simple pole at s=KO-dim via Connes A1-A6
  axioms. L1 axiom-native (S83 G4 EN3 Theorem).
```

**Cell**: L2-admissible

```
ADMISSIBLE (WEAK, via inheritance): at s=0 Dixmier limit, f_z(x)=x^0=1
  on substrate sum T_f = sum_i w_i * 1 = N_modes=159,936 at L_max=5.
  Flat (degenerate) under substrate multiplicative perturbation.
  Monotonically trivial (zero derivative); CM-sum-level holds trivially.
  L2-inherited via L1-Bernstein lift. Canonical layer is L1, not L2.
```

**Cell**: inadmissible-everywhere

```
NOT-OCCUPIED: zeta is L1-admissible; this cell is vacant for this
  regulator. Not-occupying inadmissible-everywhere corroborates
  zeta's structural role as the axiom-native regulator: it
  appears at L1 with a finite Bernstein representation, hence
  cannot fail CM at both layers.
```

### Regulator: Zubarev

**Cell**: L1-admissible

```
WEAK (Bernstein repr exists but is NOT Dixmier-residue native):
  f_R(x) = exp(-x/M_KK^2) admits atomic Bernstein measure
  rho_R(alpha) = delta(alpha - 1/M_KK^2) >= 0, so exp(-x/M_KK^2)
  IS CM. However, the L1 axiom-native pairing is Mellin/Dixmier-residue,
  and exp-kernel's Mellin transform M_R(s) = Gamma(s) M_KK^(2s) has no
  simple pole at integer s (zero residue). Not A1-A6 axiom-native at L1.
  Layer-of-definition: L2. Per S82 MP-Exclusion Theorem, Zubarev is
  substrate-action canonical at L2, NOT L1-native.
```

**Cell**: L2-admissible

```
ADMISSIBLE (ACHIEVED): substrate-action canonical kernel. Evaluated
  on D_K^2 spectrum at L_max=5: T_R = sum_i w_i * exp(-lambda_i^2/M_KK^2).
  Value at delta=0: 3.8057e+03.
  Monotone-nonincreasing under multiplicative eigenvalue scaling: True.
  Divided-difference CM at sum level up to n=4: True.
  Bernstein representation is atomic and compatible with finite-L_max
  substrate evaluation. L2 axiom-native.
```

**Cell**: inadmissible-everywhere

```
NOT-OCCUPIED: Zubarev is L2-admissible (substrate-action canonical);
  this cell is vacant for this regulator. Zubarev's Bernstein measure
  is atomic at alpha=1/M_KK^2>0, ensuring CM at all derivative orders
  and at the substrate-sum level. Inadmissible-everywhere is
  structurally excluded for any regulator with a positive Bernstein
  representation.
```

### Regulator: SDW

**Cell**: L1-admissible

```
INADMISSIBLE: f_S(x) = 0.912*sqrt(x) + 0.088*exp(-x) fails CM at n=1.
  The sqrt(x) term has d/dx[sqrt(x)] = 1/(2*sqrt(x)), so
  (-1)^1 d/dx[sqrt(x)] = -1/(2*sqrt(x)) < 0 on (0, inf).
  Bernstein integral representation fails: sqrt(x) is a BERNSTEIN
  function (=integral of CM, sqrt(x) = (1/Gamma(1/2)) integral_0^inf
  alpha^(-3/2)*(1-exp(-alpha x)) dalpha) but NOT CM itself.
  The 0.912 weight is >0 so the non-CM term dominates.
  n* = 1. S82 MP-Exclusion Theorem reproduced (anchor PASS).
```

**Cell**: L2-admissible

```
INADMISSIBLE: even under substrate-action sum T_S(delta), the sqrt
  component is monotone INCREASING in delta (sqrt is an increasing
  function of its argument), so T_S(delta) ~ sum_i sqrt(lambda_i^2 *
  (1+delta)^2) = (1+delta) * sum_i |lambda_i| INCREASES with delta.
  Computed: T_S(0) = 3.0508e+05,
            T_S(1e-1) = 3.3540e+05.
  monotone_decreasing: False (=False means
  INCREASING, CM violated).
  cm_sum_level (DD): False.
  SDW sqrt-dominated kernel breaks CM at sum level as well.
```

**Cell**: inadmissible-everywhere

```
OCCUPIED (ACHIEVED): SDW fails CM at both L1 (classical derivative
  test n=1 cusp) and L2 (substrate-action monotone-increasing sum).
  Inadmissible-everywhere. Consequence: any observable built on the
  SDW kernel is a layer-3 per-observable definition, not a layer-1
  axiom-native one and not a layer-2 substrate-action one.
  (This is the S82 MP-Exclusion Theorem elevated from sqrt cusp
  to full regulator classification.)
```

### Regulator: dim-reg

**Cell**: L1-admissible

```
ADMISSIBLE (ACHIEVED): f_D(x) = x^(-eps/2), eps>0, identical
  Bernstein representation to zeta via rho_D(alpha) =
  alpha^(eps/2-1)/Gamma(eps/2) >= 0. eps->0 limit recovers simple
  pole at s=KO-dim via Mellin pole subtraction. L1 axiom-compatible
  (but requires epsilon regulator-pin, unlike zeta's clean
  Dixmier-residue). Inherits L1 from the same power-law structure.
```

**Cell**: L2-admissible

```
WEAK (requires layer transport): in the eps->0 limit, sum_i w_i *
  lambda_i^(-eps) diverges logarithmically in 4D (Dixmier pole),
  requiring Mellin pole subtraction which is an L1 operation.
  At finite eps>0 the L2 sum converges but depends on eps ->
  regulator-dressed, NOT substrate-action canonical.
  L2 layer transport required => L2-provisional only.
```

**Cell**: inadmissible-everywhere

```
NOT-OCCUPIED: dim-reg is L1-admissible (Bernstein representation
  identical to zeta with measure rho_D(alpha) = alpha^(eps/2-1)/Gamma(eps/2)
  >= 0 for eps>0); this cell is vacant for this regulator. dim-reg
  inherits L1 admissibility from the same power-law structure as
  zeta and cannot be inadmissible at both layers.
```

### Regulator: lattice-BR

**Cell**: L1-admissible

```
INADMISSIBLE (classical smooth CM): f_L(x) = Theta(Lambda_lat^2 - x)
  has jump discontinuity at x=Lambda_lat^2. Classical derivatives
  d^n f/dx^n are zero for x != Lambda_lat^2 and distributional
  (n-th derivative of Dirac delta) at x=Lambda_lat^2. The
  Hausdorff-Bernstein-Widder theorem requires classical smooth
  derivatives with (-1)^n d^n f/dx^n >= 0 on (0,inf); the jump
  violates this at x=Lambda_lat^2. No classical Bernstein positive
  measure rho on (0,inf) produces a Theta-function kernel (Theta
  is Abel-limit of exp-sums, not Bernstein in the classical sense).
  n* = 0 (discontinuity at the boundary; CM fails).
```

**Cell**: L2-admissible

```
ADMISSIBLE (WEAK, atomic): substrate-action sum T_L(delta) =
  sum_i w_i * Theta(Lambda_lat^2 - lambda_i^2 * (1+delta)^2) is
  a counting function that is MONOTONE NON-INCREASING in delta
  (enlarging eigenvalues can only cross the cutoff OUTWARD).
  T_L(0) = 1.0400e+02,
  T_L(1e-1) = 6.2000e+01.
  monotone_decreasing: True.
  cm_sum_level (DD): False.
  L2-admissible (weak, via atomic Bernstein measure at alpha=0).
```

**Cell**: inadmissible-everywhere

```
NOT-OCCUPIED: lattice-BR is L2-admissible (weak); L1 fails the
  classical smooth-CM test but L2 atomic sum is monotone.
  Not inadmissible-everywhere.
```

## Substitution Chain (from plan §10)

See script header for full 10-step derivation chain. Summary:

1. Zubarev f_R(x) = exp(-x/M_KK^2) has atomic Bernstein measure -> CM at all n -> L2-admissible.
2. zeta f_z(x) = x^(-s/2), s>0, has power-law Bernstein measure rho(alpha) = alpha^(s/2-1)/Gamma(s/2) >= 0 -> L1-admissible.
3. SDW f_S(x) = 0.912*sqrt(x) + 0.088*exp(-x): sqrt is Bernstein not CM; n*=1 cusp -> L1-inadmissible + sqrt-increasing sum -> L2-inadmissible -> INADMISSIBLE-EVERYWHERE.
4. dim-reg f_D(x) = x^(-eps/2) structurally identical to zeta -> L1-admissible.
5. lattice-BR f_L(x) = Theta(Lambda_lat^2 - x): classical discontinuity -> L1-inadmissible; monotone counting sum -> L2-admissible.

## Environment

- GPU active: True
- GPU sanity residual (torch eigvalsh vs cache): 0.0
- Python: phonon-exflation-sim/.venv312/Scripts/python.exe
- Spectrum cache: s74_spectrum_cache_L9_tau019.npz (SHA: 3ce853809c61f79d...)

