# Session 28b Results: Landau Diagnostics + NCG Axiom Gates

**Date**: 2026-02-27
**Computations**: 8 (1 NCG axiom + 5 Landau diagnostics + 1 Hessian + 1 CC estimate)
**Runtime**: ~15 min total (4 parallel agent groups)
**Input data**: s27_multisector_bcs.npz, s27_torsion_gap_gate.npz, s28a_torsionful_bcs.npz, s28a_thermal_spectral_action.npz, tier1_dirac_spectrum.py, s22c_order_one.py infrastructure

---

## I. GATE VERDICTS

| # | Gate | Verdict | Decisive Number | Feeds Into |
|:--|:-----|:--------|:----------------|:-----------|
| 28b-1 | C-3 Order-One Condition | **FAIL** | Max norm 3.117, O(1) violation | C-6 deprioritized |
| 28b-2 | L-3 Relaxation Times | **PASS** | (2,0) re-entrant, τ_c1=0.069, τ_c2=0.499 | S-4 Berry curvature |
| 28b-3 | L-5 Pomeranchuk Map | **DIAGNOSTIC** | ALL sectors unstable, deepest f₀=-434 (D_can) | Context for Constraint Chain |
| 28b-4 | L-6 Quasiparticle Weight | **DIAGNOSTIC** | Z_min=0.585 in (0,1), moderate mixing | Torsion mechanism |
| 28b-5 | L-9 Cubic Invariant | **PASS** | (3,0)/(0,3) first-order: c=0.006-0.007 | First-order BCS |
| 28b-6 | L-7 Self-Consistent (τ,T) | **PASS_REDUCED_WEAK** | 6 interior minima, global at τ=0 boundary | KC-3 target |
| 28b-7 | S-3 Hessian | **PASS** | 3 genuine minima, λ₁,λ₂ > 0 | KC-3 validation |
| 28b-8 | E-5 Λ_eff | **DIAGNOSTIC** | 10¹¹³ orders too large at GUT scale | CC problem |

**Score: 3 PASS, 1 FAIL, 1 WEAK PASS, 3 DIAGNOSTICS. No new closes.**

---

## II. DETAILED RESULTS

### 28b-1: C-3 Order-One Condition for D_can — FAIL (Structural)

The NCG order-one condition [[M_Lie, a_F], J b_F J⁻¹] = 0 is **not satisfied** for D_can on non-trivial sectors.

**Key numbers:**

| τ | (0,0) | (1,0) | (0,1) | (1,1) |
|---|-------|-------|-------|-------|
| 0.00 | **0.000** | 2.309 | 2.309 | 2.309 |
| 0.15 | **0.000** | 2.683 | 2.683 | 2.683 |
| 0.30 | **0.000** | 3.117 | 3.117 | 3.117 |

- D_can violation is **purely Clifford** (no Ω_LC contribution). The condition is τ-independent; only the norm varies.
- D_can is 20% cleaner than D_K (ratio 0.80), but both fail at O(1).
- (0,0) singlet passes trivially (M_Lie = 0 for trivial representation).
- The 32-dim Clifford space has max violation 4.000 (worst: γ₁, a=H_i, b=H_i).

**Physical interpretation:** This is the known Baptista-Connes representation mismatch from Session 9-10. The Baptista bimodule identification of C¹⁶ is not unitarily equivalent to the Connes spinor identification. Neither D_K nor D_can satisfies the standard NCG order-one axiom in the Baptista representation. This is NOT a new framework closure — it is the structural open problem that persists regardless of connection choice.

**Implication for 28c:** C-6 (12D axiom verification) is deprioritized — the order-one condition fails at the sub-manifold level, so the full 12D axiom check cannot pass.

**Output**: `s28b_order_one.npz`, `s28b_order_one.txt`

---

### 28b-2: L-3 Landau-Khalatnikov Relaxation Times — PASS

**Key numbers (D_K, μ = λ_min):**

| Sector | τ_c1 | τ_c2 | Re-entrant? | Window width |
|--------|-------|-------|-------------|-------------|
| (2,0) | 0.069 | 0.499 | **YES** | 0.430 |
| (0,2) | 0.068 | 0.499 | **YES** | 0.431 |
| (1,1) | 0.095 | — | No (single transition) | — |
| (2,1) | 0.303 | — | No (single transition) | — |

- (2,0)/(0,2) confirmed re-entrant: M_max=1.723 at τ=0, drops to 0.826 at τ=0.30, re-enters supercritical near τ=0.50.
- Relaxation time τ_LK diverges at both crossings (peaks ~1076 and ~6393).
- **D_can comparison:** Enhancement of 2-13× makes ALL sectors always supercritical. The torsionful connection eliminates all subcritical windows. Re-entrant trapping is Levi-Civita specific.

**Physical interpretation:** The two τ_LK divergences in the (2,0) sector bracket a subcritical window [0.069, 0.499]. At each boundary, critical slowing down naturally drives τ̇ → 0, consistent with the atomic clock constraint (Closure 14). However, this trapping mechanism operates only for D_K — D_can shows no subcritical windows at μ = λ_min.

**Output**: `s28b_relaxation_times.npz`, `s28b_relaxation_times.png`

---

### 28b-3: L-5 Per-Sector Pomeranchuk Map — DIAGNOSTIC (Universal Instability)

**Key numbers:**

D_K basis:
- ALL 9/9 sectors Pomeranchuk-unstable (f₀ < -1) at some τ
- Deepest instability: (1,0) at τ=0.35, f₀ = -312.8
- (0,0) singlet at τ=0.30: f₀ = -6.6 (consistent with S22c value of -4.687)

D_can basis:
- ALL 8/8 sectors unstable
- Deepest: (2,1) at τ=0.05, f₀ = -434.1
- Mean torsion enhancement: 5.59×

**Instability map at τ=0.30 (D_K):**
| Sector | f₀ | Interpretation |
|--------|-----|---------------|
| (0,0) | -6.6 | Unstable |
| (1,0)/(0,1) | -83.1 | Deeply unstable |
| (1,1) | -1.2 | Marginally unstable |
| (2,1) | -3.0 | Unstable |
| (3,0)/(0,3) | -6.1 | Unstable |

**Physical interpretation:** Universal Pomeranchuk instability (f₀ << -1 everywhere) means the system WANTS to condense in every sector. But M_max(μ=0) < 1 says the interaction isn't strong enough for self-consistent BCS condensation without chemical potential. The tension between "strongly attractive" (Pomeranchuk) and "subcritical" (BCS) is the spectral gap problem: the discrete KK spectrum has too few modes near the gap edge. This is consistent with a strong-coupling / BEC-crossover regime where Landau Fermi-liquid theory breaks down.

**Output**: `s28b_pomeranchuk.npz`, `s28b_pomeranchuk.png`

---

### 28b-4: L-6 Quasiparticle Weight Z(τ) — DIAGNOSTIC (Moderate Mixing)

**Key numbers (τ > 0 only; τ=0 values are degeneracy artifacts):**

| Sector | Z_min(τ>0) | at τ | IPR range | Interpretation |
|--------|-----------|------|-----------|----------------|
| (1,0) | 0.817 | 0.20 | 1.0-1.5 | Weak mixing |
| (0,1) | **0.585** | 0.15 | 1.0-2.5 | **Moderate** |
| (1,1) | 0.836 | 0.50 | 1.0-2.5 | Weak mixing |
| (2,0) | 0.646 | 0.15 | 1.0-2.0 | Moderate |
| (0,2) | 0.666 | 0.35 | 1.0-2.0 | Moderate |
| (3,0) | 0.799 | 0.50 | 1.0-2.0 | Weak mixing |
| (0,3) | 0.713 | 0.30 | 1.0-2.0 | Weak mixing |
| (2,1) | 0.793 | 0.50 | 1.0-3.0 | Weak mixing |

- **Global Z_min(τ>0) = 0.585** in (0,1) at τ=0.15. No sector reaches strong mixing (Z < 0.5).
- Gap-to-gap overlap Z_gg ≈ 0 everywhere: D_can λ_min is 2-5× smaller than D_K λ_min, so gap-edge states live at different energy scales.
- IPR (effective K-mode count): 1.0-3.9 — D_can gap-edge states are superpositions of 1-4 D_K modes.

**Physical interpretation:** Torsion's dominant effect is **spectral compression** (eigenvalues shrink 2-5×), not wavefunction reshuffling (Z > 0.5). The D_can eigenstates look similar to D_K eigenstates but at dramatically lower energies. This explains the 4.83× M_max enhancement from 28a: the BCS kernel benefits from smaller denominators (gap reduction), not fundamentally different mode structure.

**Output**: `s28b_quasiparticle_weight.npz`, `s28b_quasiparticle_weight.png`

---

### 28b-5: L-9 Cubic Invariant / First-Order Transition — PASS

**Landau expansion at μ/λ_min = 1.20:**

| Sector | c (cubic coefficient) | Character |
|--------|----------------------|-----------|
| (3,0) | **0.00552** | First-order |
| (0,3) | **0.00723** | First-order |
| (1,0) | 0.00013 | Second-order |
| (0,1) | 0.00026 | Second-order |

- 5 discontinuities in d³F_total/dτ³ detected at sector boundaries, with jumps of magnitude 168,000 to 452,000.
- Higher-weight sectors (3,0)/(0,3) show c > 0 at 10⁻³ level — first-order transition character.
- Lower-weight fundamentals (1,0)/(0,1) are second-order (c ~ 10⁻⁴).

**Physical interpretation:** The multi-sector BCS system has genuine first-order phase transitions at sector on/off boundaries. This is qualitatively distinct from all 20 closed perturbative mechanisms, which relied on continuous potentials. A first-order BCS transition stabilizes the modulus via discontinuous jump, not continuous rolling — consistent with the atomic clock constraint (Closure 14: any continuous τ̇ violates by 15,000×, but a discontinuous jump to τ̇ = 0 satisfies it).

**Output**: `s28b_cubic_invariant.npz`, `s28b_cubic_invariant.png`

---

### 28b-6: L-7 Self-Consistent (τ, T) — PASS_REDUCED_WEAK

L-1 CLOSED the thermal channel → L-7 runs in reduced form (BCS-only at T=0).

**Interior minima found (F < 0):**

| τ | μ/λ_min | F_total | Type | Hessian |
|---|---------|---------|------|---------|
| 0.35 | 1.50 | **-43.55** | Interior local | Genuine min (S-3) |
| 0.35 | 1.20 | -18.56 | Interior local | Genuine min (S-3) |
| 0.20 | 1.20 | -3.69 | Interior local | Saddle (S-3) |
| 0.15 | 1.10 | -1.03 | Interior local | Genuine min (S-3) |
| 0.15 | 1.05 | -0.22 | Interior local | Saddle (S-3) |
| 0.35 | 2.00 | -0.07 | Interior local | Saddle (S-3) |

**Global minimum: τ=0.00, μ/λ_min=1.50, F=-127.10** (boundary, saddle by S-3).

- The deepest genuine interior minimum is at τ=0.35, μ/λ_min=1.50 (F=-43.55).
- Sector breakdown at τ=0.35, μ/λ_min=1.20: (3,0)+(0,3) contribute 93% of F_total (multiplicity 100 each).

**Physical interpretation:** BCS condensation creates well-defined local free energy basins at τ=0.35 (metastable, not globally stable). The global minimum is at the boundary (τ=0, round metric). Adding the closed thermal channel would only strengthen the boundary preference. BCS alone cannot stabilize τ away from zero globally, but it creates metastable traps that could capture the modulus if initial conditions place it nearby.

**Output**: `s28b_self_consistent_tau_T.npz`, `s28b_self_consistent_tau_T.png`

---

### 28b-7: S-3 Hessian of F_total — PASS

**Genuine minima (both Hessian eigenvalues positive):**

| Location | F_total | λ₁ | λ₂ | det(H) |
|----------|---------|-----|-----|--------|
| τ=0.35, μ/λ_min=1.50 | **-43.55** | 425.7 | 31,996 | 13.6M |
| τ=0.35, μ/λ_min=1.20 | -18.56 | 437.7 | 6,842 | 2.99M |
| τ=0.15, μ/λ_min=1.10 | -1.03 | 253.6 | 917 | 233K |

**Saddle points (one negative eigenvalue):** 7 other candidates including the global minimum at τ=0.

All genuine minima have strongly positive eigenvalues (order 100-30,000) — these are tightly confined wells, not marginal. The key result: the **global "minimum" at τ=0 is actually a saddle** (H has one negative eigenvalue: -7,745 at τ=0, μ/λ_min=1.50). This means the F_total landscape has no genuine global minimum within the grid — the boundary saddle is the deepest point, but the interior minima at τ=0.35 are the only genuine wells.

**Output**: `s28b_hessian.npz`, `s28b_hessian.txt`

---

### 28b-8: E-5 Cosmological Constant from Condensation Energy — DIAGNOSTIC

| M_KK (GeV) | ρ_BCS / ρ_obs | Orders too large |
|-------------|---------------|------------------|
| 10¹⁴ | 10¹⁰⁴ | 104 |
| 10¹⁵ | 10¹⁰⁸ | 108 |
| **2×10¹⁶** | **10¹¹³** | **113** |
| 10¹⁷ | 10¹¹⁶ | 116 |
| 10¹⁸ | 10¹²⁰ | 120 |

M_KK needed to match ρ_obs: ~10⁻¹² GeV (sub-eV, physically excluded).

**Physical interpretation:** The BCS condensation energy is one more O(M_KK⁴) term in the vacuum energy budget. It inherits the standard cosmological constant problem at 113 orders of magnitude (GUT scale). This neither solves nor worsens the CC problem — it is structural to any KK framework with compactification at high energy.

**Output**: `s28b_lambda_eff.txt`

---

## III. SYNTHESIS

### What Session 28b Established

**Three central findings:**

1. **C-3 FAIL: The NCG apparatus does not apply to D_can.** The order-one condition fails at O(1) on all non-trivial sectors — structural, not numerical. This closes the possibility that D_can defines a valid noncommutative geometry in the Baptista representation. The spectral action, Connes distance formula, and gauge invariance machinery cannot be formally applied to the torsionful operator. This reinforces the 28a C-1 CLOSED: the torsionful spectral action is physically undefined, not just monotone.

2. **S-3 PASS + L-7 WEAK: The interior minima are genuine but metastable.** The Hessian confirms 3 true minima at τ=0.35 with strongly positive curvature. But the global minimum is at the boundary (τ=0), and it is itself a saddle — the F_total landscape has no genuine global minimum. The interior wells are metastable traps that could capture the modulus only if it starts nearby. The thermal channel (L-1 CLOSED) cannot help.

3. **L-3 + L-5 + L-6 + L-9: The BCS condensed matter picture is internally consistent.** Universal Pomeranchuk instability (attractive in all sectors), first-order transitions at sector boundaries, re-entrant behavior in (2,0), moderate torsion mixing (Z > 0.5). Torsion's main effect is spectral compression (2-5× gap reduction), not wavefunction mixing. The persistent problem: strong attraction (f₀ << -1) coexists with subcritical BCS (M_max < 1 at μ=0).

### The Spectral Gap Problem

Session 28b crystallizes the central obstruction: **the discrete KK spectrum has a gap that prevents spontaneous BCS condensation at μ=0.**

- Pomeranchuk says: the interaction is strongly attractive in every sector
- BCS says: the gap-edge level spacing is too large for the coupling to sustain a condensate
- Torsion helps (5× enhancement) but not enough (1.9× short)
- The Constraint Chain KC-1 → KC-5 is the remaining path: if parametric amplification (KC-1 PASS confirmed) can generate μ_eff ≥ 0.95·λ_min, the gap is effectively filled and condensation occurs

### What Feeds Into Session 28c

| Result | Feeds Into | Status |
|:-------|:-----------|:-------|
| C-3 FAIL | C-6 (12D axioms) | **DEPRIORITIZED** — order-one fails at sub-manifold level |
| L-7 WEAK + S-3 PASS | KC-3 (steady-state μ_eff) | **PROCEED** — validated interior minimum as target |
| L-3 re-entrant (2,0) | S-4 (Berry curvature) | **PROCEED** — sector boundaries are transition points |
| L-9 first-order | KC-3/KC-5 | **SUPPORTS** — first-order transitions stabilize via jump, not rolling |
| L-5 universal instability | Constraint Chain context | The system wants to condense; just needs μ_eff > 0.95·λ_min |
| L-6 moderate mixing | Mechanism understanding | Torsion = spectral compression, not mode mixing |

### Updated Summary

Session 28b adds **no new closes** (C-3 FAIL is the known structural mismatch, not a mechanism death). Closed Mechanism remain at 20 (18 prior + 2 from 28a).

The framework's survival path narrows to a single quantitative question for 28c:

```
KC-1 (PASS) → KC-2 (phonon T-matrix) → KC-3 (μ_eff from kinetics)
                                                ↓
                                   μ_eff ≥ 0.95·λ_min_can?
                                   YES → M_max > 1, condensation, framework ALIVE
                                   NO → Last mechanism closed, framework probability ≤ 3%
```

The S-3 + L-9 results add a refinement: the BCS minimum is genuine (positive Hessian) and first-order (cubic invariant), meaning if μ_eff crosses the threshold, the modulus jumps discontinuously to τ=0.35 and freezes — satisfying the atomic clock constraint (Closure 14) via first-order transition rather than slow roll.

---

## IV. OUTPUT FILES

| File | Computation | Gate |
|:-----|:-----------|:-----|
| `tier0-computation/s28b_order_one.py` | C-3 script | FAIL |
| `tier0-computation/s28b_order_one.npz` | C-3 data | FAIL |
| `tier0-computation/s28b_order_one.txt` | C-3 verdict | FAIL |
| `tier0-computation/s28b_relaxation_times.py` | L-3 script | PASS |
| `tier0-computation/s28b_relaxation_times.npz` | L-3 data | PASS |
| `tier0-computation/s28b_relaxation_times.png` | L-3 plot | PASS |
| `tier0-computation/s28b_pomeranchuk.py` | L-5 script | DIAGNOSTIC |
| `tier0-computation/s28b_pomeranchuk.npz` | L-5 data | DIAGNOSTIC |
| `tier0-computation/s28b_pomeranchuk.png` | L-5 plot | DIAGNOSTIC |
| `tier0-computation/s28b_quasiparticle_weight.py` | L-6 script | DIAGNOSTIC |
| `tier0-computation/s28b_quasiparticle_weight.npz` | L-6 data | DIAGNOSTIC |
| `tier0-computation/s28b_quasiparticle_weight.png` | L-6 plot | DIAGNOSTIC |
| `tier0-computation/s28b_cubic_invariant.py` | L-9 script | PASS |
| `tier0-computation/s28b_cubic_invariant.npz` | L-9 data | PASS |
| `tier0-computation/s28b_cubic_invariant.png` | L-9 plot | PASS |
| `tier0-computation/s28b_self_consistent_tau_T.py` | L-7 script | WEAK PASS |
| `tier0-computation/s28b_self_consistent_tau_T.npz` | L-7 data | WEAK PASS |
| `tier0-computation/s28b_self_consistent_tau_T.png` | L-7 plot | WEAK PASS |
| `tier0-computation/s28b_hessian.py` | S-3 script | PASS |
| `tier0-computation/s28b_hessian.npz` | S-3 data | PASS |
| `tier0-computation/s28b_hessian.txt` | S-3 verdict | PASS |
| `tier0-computation/s28b_lambda_eff.py` | E-5 script | DIAGNOSTIC |
| `tier0-computation/s28b_lambda_eff.txt` | E-5 estimate | DIAGNOSTIC |
| `tier0-computation/s28b_gate_verdicts.txt` | All gate verdicts | — |
