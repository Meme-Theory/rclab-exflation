---
name: s100a-w1-1-q-frame-invariance
description: q-invariance theorem under constant conformal factors + three-frame ladder of the post-fold expansion (S100a W1-1 SF54-MAPPING, INFO/Track-B)
metadata:
  type: project
---

# S100a W1-1 — q frame-invariance theorem + post-fold three-frame ladder

**Fact**: S100a-W1-1-SF54-MAPPING closed INFO (sign=PASS, mag=INFO, regime=VALID; Track B 0.9): band_frac_corrected = 0.5015 < 0.90, median(q_corrected) = −0.8662 < 0, map well-defined. The S99 W1-1 SF54 band-miss is FRAME-ROBUST — a genuine substrate prediction (substrate mostly-accelerating post-fold), not a mapping defect. audit f41bdf1fc80562da.

**Why (the structural theorems — reusable)**:

1. **q-invariance theorem**: q = −a·ä/ȧ² is a logarithmic-derivative observable — EXACTLY invariant under a(τ) → C·a(τ) for any constant C (and under constant time rescalings). NO constant conformal/normalization factor (e.g. Ω_BA_fold = 2.241353) can move a deceleration history or its band fraction at all. Numerically: identity holds to ~5e-7 rel through a double-np.gradient pipeline (roundoff amplification, not violation).

2. **Exact conformal frame map (affine)**: for ã = ω(τ)·a, with h = a′/a, w = ω′/ω: H̃ = h + w (log-rates add) and
   `q̃(τ) = A(τ)·q(τ) + B(τ)`, `A = (h/H̃)² > 0`, `B = −1 + A − w′/H̃²`.
   Pointwise-exact (verified machine-ε, 2.5e-16). Slope A = (H_old/H_new)²: frame corrections are positive-multiplicative + additive — sign-preservation of the median is NOT automatic (B can dominate); it holds when B≈0.

3. **Three-frame ladder of the post-fold expansion** (τ ∈ [0.190, 0.451], S99 999-pt grid):
   - bare frame: H_bare ∈ [0.069, 0.306] (the well-conditioned S99 backbone; q median −0.8662, q ≤ ~0 everywhere, spikes to −514)
   - acoustic/AOFT frame: H_A ≈ 0 (a_eff stationary, relvar 1.8e-7) — q ill-defined (S98 0/0; A₁ ~ 1e11)
   - Connes-distance frame (SF54 generator): H_CD ≈ 2.6–3.95, median H_CD/H_bare = 26.1 — A₂ ~ 1.5e-3 (transport degenerate/circular: reproduces band generator)
   The three are pairwise conformally distinct (inter-proxy ratio rel-vars ~0.14).

4. **SF54 band anatomy**: [−0.97, +0.81] = full-window q-range of the S54 CD-proxy (10-pt grid τ ∈ [0, 0.347]); lower edge at τ=0 (PRE-fold quasi-dS), upper at τ=0.347. Post-fold-restricted SF54 range is [−0.786, +0.814]. Band conflates pre/post-fold regimes of a different-frame proxy — wrong comparison object for any post-fold bare-frame history.

**How to apply**: any future gate comparing deceleration/expansion histories across proxies MUST first declare the conformal frame of each side; constant normalizations are q-irrelevant (theorem 1); τ-dependent transports must check A(τ) = (H_old/H_new)² for degeneracy (A ≪ 1 erases the source history; A ≫ 1 or H_new crossing 0 is ill-defined). Cite the S100a npz (s100a_w1_sf54_mapping.npz) for the frame arrays.
