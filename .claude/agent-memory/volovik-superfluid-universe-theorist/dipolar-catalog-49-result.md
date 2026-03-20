---
name: dipolar-catalog-49-result
description: S49 DIPOLAR-CATALOG-49 PASS. Leggett mode breaks U(1)_7 with epsilon=0.00248. m_G=omega_L1=0.070 M_KK (18% from n_s requirement). 10 mechanisms cataloged, 2 break, 8 preserve. Leggett = exact 3He dipolar analog. 7/8 generators K_7-charged.
type: project
---

## DIPOLAR-CATALOG-49 Result (Session 49 W1-S)

### Gate: PASS (2026-03-17)

**Primary breaker**: Leggett mode (inter-sector Josephson)
- epsilon = J_23/Delta_B2 = 0.00248
- m_G = omega_L1 = 0.0696 M_KK (parameter-free)
- Breaks U(1)_7 by pinning K_7-charged (B2, |q_7|=1/4) phase to K_7-neutral (B3, q_7=0)
- H_J = -J_23 cos(phi_B2 - phi_B3 + alpha/2) depends on U(1)_7 angle alpha

**Subsidiary breaker**: Inner fluctuations (Connes gauge sector)
- epsilon = 0.0522 (||[iK_7, D_phys]||/||D_phys||)
- m_G ~ 0.052 M_KK (lattice scale)
- Internal to spectral action, not external to BCS

### Key Numbers

| Quantity | Value |
|:---------|:------|
| omega_L1 / m_req(n_s) | 1.179 (18% overshoot) |
| omega_L1 / Delta_B2 | 0.0950 |
| 3He dipolar omega_L/Delta | ~10^{-3} |
| Framework/3He ratio | 95x |
| K_7-charged generators | 7/8 |
| K_7-neutral generators | 1/8 (only T_7 itself) |

### 8 Mechanisms That Preserve U(1)_7

1. Gravitational backreaction — trace theorem
2. Parallelizing torsion — Casimir-proportional
3. WZW term — eta=0 by PH, invariant under conjugation
4. Higher Seeley-DeWitt — exact trace theorem all orders
5. GGE finite-T — R-G integrals commute with K_7
6. Spectral flow anomaly — no Fermi points (3He-B class)
7. Nieh-Yan torsion — scalar 4-form, non-chiral
8. de Sitter expansion — Hubble friction K_7-universal

### Structural Correspondence

3He-A dipolar: H_D ~ g_D(d.l)^2 breaks SO(3)_S x SO(3)_L -> SO(3)_{S+L}
Framework Leggett: H_J = -J_23 cos(phi_B2-phi_B3) breaks U(1)_7

The "global U(1)_7 phase" IS the B2-relative-to-neutral phase. No separate global direction exists.

### Critical Finding

omega_L1 = 0.070 M_KK is the FIRST mechanism in 12+ n_s routes to produce a mass at the correct scale (m_req = 0.059 M_KK for n_s=0.965). Previous routes gave either 0 or 10^{-59} M_KK.

**Why:** The Leggett mode provides the dipolar breaking; its mass is set by J_23 and sector gaps, which are microscopic BCS parameters. No cosmological input needed.

**How to apply:** The Ornstein-Zernike power spectrum P(K) ~ 1/(K^2 + m_L^2) with m_L = omega_L1 should be tested against CMB n_s. The 18% overshoot may improve with self-consistent Delta(tau) or fabric-level corrections. This is the only open n_s channel.

Files: s49_dipolar_catalog.py, s49_dipolar_catalog.npz, s49_dipolar_catalog.png
