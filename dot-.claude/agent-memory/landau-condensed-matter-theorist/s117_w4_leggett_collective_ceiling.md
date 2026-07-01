---
name: s117-w4-leggett-collective-ceiling
description: Leggett collective-mode ceiling via the parameter-free continuum-edge cap + sqrt(N)-saturation; the 4-2 ladder-top-cap vs 4-3 lowest-edge distinction
metadata:
  type: reference
---

# S117 W4-2 — Protected Leggett collective-mode ceiling (CF-S117-LEGGETT-COLLECTIVE-CEILING, PASS)

Gate confirmed the 170x structure-formation target is unreachable by the protected
inter-band collective Leggett spectrum: frac170 = m_heaviest_protected/(170·Δ_BCS)
= 0.0704 ∈ [0.06,0.08]. The verdict/numbers live in the verdict file + WP §W4-2 +
knowledge.db — this note records the REUSABLE METHODOLOGY only.

## The durable physics insight (reuse for any collective-mode ceiling question)

**The heaviest PROTECTED collective mode is bounded by the two-quasiparticle
continuum edge — a PARAMETER-FREE kinematic ceiling (Landau damping), NOT a
formula needing an unpinned Josephson coupling J_⊥.** A collective mode above its
inter-band two-qp continuum edge decays into the continuum (finite linewidth), so
it stops being a sharp/protected bound state. Hence
`m_heaviest_protected ≤ E_edge^⊥,cap = Δ_BCS + max|λ|_fib(L_max)`.
This sidesteps the PRU trap of modeling ω_Leg² = J_⊥/χ_- with unpinned J_⊥, χ_-
(the susceptibility normalizations are NOT framework-pinned — do not invent them;
use the kinematic edge bound instead).

**√N-saturation**: the single-fiber ladder top scales as HIGH-PW-51 (collab eq 1)
`max|λ| = 0.633·√C_2(p,q) + 0.555`, C_2=(p²+q²+pq+3p+3q)/3, so the cap grows only
as √C_2 ~ √N. Reaching 170·Δ_BCS needs C_2≈15147 ⇒ p+q≈212 — structurally
unreachable at any physical L_max. This is WHY the protected spectrum saturates.

## Convention pin — the 4-2 (ladder-top cap) vs 4-3 (lowest edge) distinction

Two DIFFERENT continuum edges, both legitimate, answer two DIFFERENT questions —
do not conflate them:
- **4-2 ceiling** uses the **ladder-top cap** = Δ_BCS + max|λ| over all sectors
  (the HIGHEST continuum edge, at (10,0)/(0,10), ≈ 11·Δ_BCS). Answers: how heavy
  can a protected mode get? Answer: ~11·Δ_BCS, not 170.
- **4-3 sharpness** uses the **lowest edge** = Δ_BCS + √3 = 4.73·Δ_BCS (τ=0
  Lichnerowicz ideal fiber gap). Answers: is the registered anchor below ITS edge?
  Answer: no, x^⊥ = 11.97/4.73 = 2.53 > 1 (finite-linewidth).
Both consistent: the anchor (11.97·Δ_BCS, LEGGETT-MOMENT-70) sits AT the saturated
ceiling (≈0.8·Δ_BCS above the cache cap 11.06·Δ_BCS) AND above its lowest edge.

## Lichnerowicz floor caveat (τ-deformation)

The √3 Lichnerowicz fiber-gap floor is the **τ=0 (round SU(3)) ideal**. At
τ_fold=0.190 the Jensen deformation squeezes the lightest off-(0,0) gap to 0.836
M_KK (sector (0,1)) — BELOW √3. So "respected at τ_fold = False" is EXPECTED, not
a bug. The 4-3 sharpness edge uses the τ=0 ideal √3 by convention (a clean
energy-scale anchor), not the deformed cache gap. Watch this when reading the
cache: cache min|λ| ≠ √3.

## Reusable computational facts

- The S84 master cache `computations/session-84/s84_spectrum_cache_L12_tau019.npz`
  IS the faithful block-diagonal D_K(τ_fold) diagonalization (wall #2). Verified
  here to 2.4e-15: re-diagonalizing sector (1,0) from scratch via
  `dirac_spectrum.collect_spectrum(τ_fold, gens, f_abc, gammas, max_pq_sum=1)`
  matched the cache |λ| over 48 evals. **No need to re-diagonalize — use the cache**
  (key `sector_evals` → 0-d object dict `(p,q) → {dim, level, abs_evals}`; filter
  off-(0,0), p+q≤L). Builder = `computations/_shared/dirac_spectrum.py`.
- HIGH-PW-51 empirical ladder scaling matches the exact cache to ~1.1% at (10,0)
  (cache 4.6702 vs scaling 4.7219 M_KK). Use the cache for exactness, the scaling
  for the analytic/extrapolation argument.
- 170× target ratio + the "re-typed OFF the mass axis" framing = S116-W3-DISORDER-
  CLOSURE. This gate confirms the re-typing from the collective-mode-spectrum side.

## Scope guard

This is a KINEMATIC ceiling verdict. It does NOT touch relic SURVIVAL, which is
Reading A (CPT non-annihilation + GGE integrability S_ent=0 + Γ_grav<H_0,
atlas-04 C11-conditional) — see [[s116-w2-leggett-dm-edge-survival]]. Sharpness ⊥
survival is the load-bearing W-2 frame. Related: [[s116-w3-goldstone-mass-ceiling]],
[[s117-w4-freestream-which-velocity]] (the W4-1 sibling on v_fs^4D=0 coldness).
