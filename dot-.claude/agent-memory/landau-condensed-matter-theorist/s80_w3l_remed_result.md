---
name: S80 W0-3 c_Gold SDW-moment remediation
description: S80 W0-3 [AUDIT] PRU remediation for c_Gold at L_max=5 — FAIL reveals c_Gold provenance is BCS-Josephson, NOT Seeley-DeWitt moment ratio
type: project
---

# S80 W0-3: c_Gold PRU Remediation — Provenance-Attribution Error Identified

**Gate**: S80-W3-L-REMED ([AUDIT])
**Verdict**: **FAIL** (agreement 59.414%, 12× the 5% INFO band)
**Script**: `computations/s80_w3l_remed.py`
**4-tuple**: `(c_Gold=0.371361, scheme=SDW, convention=canonical, L_max=5)`
**SHA-256 pin**: `b88d623dbc39379d...`

## Why: structural finding, not a numerical bust

**The canonical c_Gold = 0.915 M_KK is UNCHANGED.** It is still sourced from S52 GL-JOSEPHSON-52 (BCS Josephson phase-stiffness dispersion, `s52_gl_josephson.py` lines 615-649: `c_Gold^2 = (total phase stiffness)/(total phase inertia)` from the 32-cell Josephson model). The [AUDIT] tested whether c_Gold could ALSO be written as `sqrt(a_2/a_4 * c_norm)` under a single scheme-independent c_norm — the answer is no.

Key finding: the ratio `a_2/a_4` is **not L_max-stable**:
- L_max=3 (canonical half-zeta): `a_2/a_4 = 2.0553` (a_2 > a_4)
- L_max=5 (frozen zeta power sums): `a_2/a_4 = 0.3386` (a_2 < a_4)
- Drift: 83.5% — two orders of magnitude larger than the R-protected fold bound of 0.34%

## How to apply

1. **When asked about c_Gold**: it is a BCS Goldstone sound speed, NOT a bulk gravity/YM spectral-moment ratio. The ratio a_2/a_4 governs GR-to-GB imbalance, and has NO direct relationship to the Goldstone dispersion slope.

2. **When validating spectral-moment hypotheses**: the S75-era framing "c_Gold emergent c_light from a_2 + a_4" is a mis-documented provenance — c_Gold is EMERGENT, but not from the a_2/a_4 SDW moments. It emerges from the Josephson phase stiffness on the fabric.

3. **R-protection** (`c_Gold/c_fabric = 0.00436`, drift 0.00% per S74 W4-F #20) is a ratio-of-gradients quantity that bypasses the SDW expansion entirely — it sits in a different scheme-family from the a_2/a_4 ratio. Do NOT conflate.

4. **For future c_Gold computations**: the script `s52_gl_josephson.py` is the provenance source. If a later revision tries to derive c_Gold from bulk spectral action moments, this S80 W0-3 result falsifies that route at 59.4% drift.

## Substitution chain (Python-verified)

- **Step 1**: `a_2 <-> zeta_D(3) = sum_n d_n * |lam_n|^{-6}`; `a_4 <-> zeta_D(2) = sum_n d_n * |lam_n|^{-4}` (d=8 SDW map, s74_lmax_zeta_audit.py §4).
- **Step 2**: `ratio_L3 = 2776.17/1350.72 = 2.0553`; `ratio_L5 = 3743.07/11056.02 = 0.3386`; back-fit `c_norm_L3 = 0.915²/2.0553 = 0.4073`.
- **Step 3**: `c_Gold_L5 = sqrt(0.3386 × 0.4073) = sqrt(0.1379) = 0.3714`.
- **Step 4**: `agreement = |0.3714 - 0.915|/0.915 = 59.414%`.
- **Step 5**: 59.414% >> 5% INFO band → **FAIL**.

## Cross-checks

- CC1 (L_max=3 identity): PASS to machine epsilon (the fit is well-posed at L_max=3 by construction).
- CC2 (R-protected inheritance): If c_Gold were an SDW moment-ratio, it should inherit the 0.34% R-protected drift. Observed drift is 59.4% — **falsifies the moment-ratio hypothesis**.
- CC3 (SHA-256 PRU pin): deterministic over 8 keys including scheme/convention/L_max/tau/eigenvalue-list.
- CC4 (4-tuple output): saved to npz.

## Meta-success: the PRU machinery WORKED

This was a PRU remediation PASS in the meta-sense — SHA-256 pinning + 4-tuple freezing + explicit substitution chain REVEALED a Class-8 plan-level PRU failure that would otherwise have remained hidden under "obviously c_Gold = 0.915 from SDW moments" hand-waving. The gate did its job: it detected that c_Gold's provenance was underspecified/mis-attributed in S75.

## Recommendation carried forward to S81

Amend `canonical_constants.py` line 307 provenance block for `c_Gold` to add:
```python
"c_Gold": {"session": "S52", "source": "s52_gl_josephson.npz",
           "gate": "GL-JOSEPHSON-52", "superseded": False,
           "scheme_tag": "BCS-Josephson", "branch_scope": "per-branch",
           "L_max_tag": "n/a",
           "note": "Goldstone sound speed from BCS Josephson phase-stiffness "
                   "dispersion (s52_gl_josephson.py §14). NOT an SDW moment "
                   "ratio. S80-W3-L-REMED (FAIL, 59.4% drift) falsified the "
                   "a_2/a_4 moment-ratio hypothesis."},
```
