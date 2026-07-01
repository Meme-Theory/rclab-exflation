---
name: S73B Functional Selection (all L_max)
description: FUNCTIONAL-SELECT-73B FAIL + L7-FLIP CONFIRMED-PERMANENT -- shape/boundary incompatibility theorem, f(x) is UV data, n_s=0.9567 bare, 4 routes closed at all L=3..7
type: project
---

## FUNCTIONAL-SELECT-73B: FAIL
f(x) cannot be derived from first principles. Shape/boundary incompatibility theorem:
- **Shape** (f' for x>0) -> n_s via SA derivatives
- **Boundary** (f(0)) -> m_H via Higgs quartic f_4
These are algebraically independent. No single-parameter family satisfies both.

### 4 Routes CLOSED
1. **Eliashberg**: SA is Bogoliubov-invariant (v^2+u^2=1). f unconstrained by BCS.
2. **1-param mixing**: n_s requires t=0.088 (sqrt-dominated), m_H requires t=0.966 (exp-dominated). Delta_t=0.877.
3. **Dilaton family**: f(0)=0 for ALL phi -> m_H=0. EXCLUDED.
4. **Additive constant**: 0 joint solutions in (c,t) plane.

### Bare prediction: n_s=0.9567 (1.95 sigma from Planck, marginal). m_H scheme-dependent.

## FUNCTIONAL-SELECT-L7-FLIP: CONFIRMED-PERMANENT
Delta_t >= 0.505 at ALL L=3..7. Non-monotone (S70 mH_by_L bump at L=7).
- t*(n_s) drifts 0.088->0.109 (slow, tau-derivative protected, 0.23% n_s drift).
- t*(m_H) drifts 0.593->0.807 (non-monotone, tracks mH_ref).
- Window overlap: FALSE at all L_max. Would need L~170 to close gap.
- Dilaton f(0)=0 algebraic at all L_max. Additive constant: 0 solutions at L=7.
- All 4 routes still closed at L=7. PERMANENT.
