---
name: alpha_s paper computation
description: Paper drafted for alpha_s = n_s^2 - 1 structural theorem. Key derivation details and 5 proofs verified.
type: project
---

## alpha_s = n_s^2 - 1 Paper (papers/alpha-s-ns/main.tex)

Paper drafted with full content. 13 pages, compiles clean.

**Core derivation**: From P(K) = T/(JK^2 + m^2), define y = m^2/(JK^2). Then n_s - 1 = -2/(1+y), y = (1+n_s)/(1-n_s). Since dy/d(ln K) = -2y, alpha_s = dn_s/d(ln K) = -4y/(1+y)^2 = -(1-n_s^2) = n_s^2 - 1.

**Five proofs of robustness** (all within Josephson phase sector):
1. 3-pole Leggett: poles 99.95% degenerate, delta_alpha_s = 5.8e-9
2. Running mass bound: gamma < 1 - n_s = 0.035 (algebraic). Physical gamma = -6.76e-4
3. Zero-mode protection: Goldstone is n=0 KK mode, <V>=0 identically
4. RPA suppression: delta_alpha_s = 1.1e-5, mass hierarchy kills it
5. Goldstone theorem: K^2 dispersion structural for broken U(1)

**Tension**: 6.1 sigma with Planck. Honest.

**Why:** Record of what was verified and computed for this paper.
**How to apply:** Reference when revisiting alpha_s computation or paper revisions.
