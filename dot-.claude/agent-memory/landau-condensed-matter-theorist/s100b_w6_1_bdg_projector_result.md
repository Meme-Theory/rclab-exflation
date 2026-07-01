---
name: s100b-w6-1-bdg-projector-result
description: S100b W6-1 VII-AF1-BDG-PROJECTOR-CONFIRM PASS (Delta_disc=0.342, 342x floor) — projector-side pairing methodology + phi(P,P,P)=0 trap + channel anatomy
metadata:
  type: project
---

# S100b W6-1 — VII.AF.1 BdG-projector confirmation (PASS)

**Gate**: S100b-VII-AF1-BDG-PROJECTOR-CONFIRM — Element-5 structural confirmation of §VII.AF.1.OP-PROJ at the PRIMARY ζ-pairing layer (Porlles-Chen quasihole-projector reading). PASS: Delta_disc = 0.341975501613 (342× the 1e-3 Level-2 envelope), Mode-B (delta_BdG = 0 VACUOUS, pre-declared), sign/magnitude/regime = PASS/PASS/VALID. audit_sha 06206dbbd1f6ec38…, WP §W6-1 of session-100b-w6-workingpaper.md.

**Why:** closes the latent projector ambiguity in the §VII.AF.1 anchor chain — the bridge pairing is anchored to the ORDERED state (Landau requirement); R^N/R^BdG = 0.658.

**How to apply (methodology, re-usable):**

1. **φ(P,P,P) ≡ 0 trap**: the literal idempotent self-evaluation of a commutator-form Hochschild 2-cocycle φ(a0,a1,a2)=τ(a0[P,a1][P,a2]) vanishes IDENTICALLY for any projector ([P,P]=0) — no discriminating power. The projector-side Connes-Karoubi pairing is evaluated with the K_0 representative in the a_0 slot and GENERATOR-BASIS differentials in the cocycle legs (s86-hp1 eq. R-V1.3 form). Class-8.7-adjacent; check before pinning any pairing operator of this shape.
2. **Provost-Vallée identity check (free assert)**: Tr(P[P,J][P,J]) = −Tr(PJ(1−P)JP) = −‖(1−P)JP‖²_F — assert at machine precision; the evaluated object IS the quantum-metric trace.
3. **Generator representation on the (0,0) singlet fiber**: Kosmann spin-lift K_a = (1/8)Σ_{r,s}(Γ[s,r,a]−Γ[r,s,a])γ_rγ_s (S23a `kosmann_operator_antisymmetric`, Baptista P17 eq 4.1); J_a = iK_a Hermitian. Builder: ds.u2_invariant_metric(B,e^{2τ},e^{-2τ},e^{τ}) → orthonormal_frame → frame_structure_constants → connection_coefficients → spinor_connection_offset = D_(0,0) (16×16).
4. **Mode-B normalization-anchored discrimination is normalization-free**: Delta_disc = |1 − met_N/met_BdG| — N_pair, Tr/16, Vol(SU3), f_4 all cancel. Pre-declare Mode-A/Mode-B at plan time (npz key sufficiency set) so neither is convention-shopping.
5. **Channel anatomy at τ_fold (B1 pair, r0=2)**: metric content 94.8% in C² coset directions (λ4..λ7 = 9.9037e-3 each, isotropic), su(2) triple 7.1884e-4 bit-exact equal, **λ_8 = 4.9e-31 machine-zero = wall #5 ([iK_7,D_K]=0) manifest in the metric trace** (non-degenerate band ⇒ J_8 commutes with spectral projector). At τ=0 (16-fold |λ|-tie, √3/2, n=27): content spreads ~even; C² content drops 3.1× — the normal arm loses exactly the order-parameter-gated coset content.
6. **τ=0 tie-break robustness**: rank-2 representative orbit (8 Haar frames in the tied subspace, seed 100616) gives Delta_disc ∈ [0.301, 0.354] — verdict robust to the stable-eigh tie-break pin. d1 fixed-generator arm: 0.310 (projector swap dominates over generator τ-dependence).
7. **UNTRUSTED-UPSTREAM caveat carried** (verdict extra row + WP paragraph): s84 cache lineage = LC t=1/2 Lai-Teh point per S100b-TAU0-LAITEH-REDUCTION ESCALATION; results conditional on LC-lineage canonicity; both arms shift coherently under re-adjudication so the discrimination STRUCTURE is robust.
8. **Concurrent-WP write pattern**: anchored Python single-shot splice of own §-span + SHA-verify sibling span before/after (Edit tool mtime-races with concurrent sibling writers).

Related: [[framework-constants]], [[technical-notes]].
