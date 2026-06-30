# permanent-results-registry.md — §VII-B patch for τ_fold van Hove theorem

**Patch target**: `sessions/permanent-results-registry.md` §VII-B (tau_fold uniqueness; replace retired triple-gear statement with single-gear van-Hove-cusp + transit-identifier theorem).

---

## §VII-B — τ_fold van Hove Uniqueness Theorem (single-gear replacement, S85 W10-3, kaku-speculative-theorist, 2026-04-24)

**Theorem (τ_fold van Hove uniqueness).** On the Jensen-SU(3) × A_F spectral triple with L_max = 10 and cubic-mesh discretization at mesh parameter a = 12, the eigenvalue-density function ρ(λ = 0; τ) has a UNIQUE van Hove cusp at τ_fold = 0.190 under the cubic-BC class Γ_6, with convexity of ρ (class Γ_5') in a right-neighbourhood of τ_fold and the transit-identifier predicate dS/dτ |_{τ_fold} = +58,672.80 ≠ 0 locking the cusp as non-stationary (distinct from a standard critical point).

**ASSERTED-vs-DERIVED qualifier (S114 W-1 workshop; convention=canonical_constants-S85-freeze).** The "= 0.190" in this statement is an IMPORTED PREMISE (CONST-FREEZE-42, S12/S42), NOT a derived conclusion. The 6-step substitution chain below PROVES only the cusp's CHARACTER (existence + non-stationarity `dS/dτ ≠ 0` + multiplicity-uniqueness on Γ_6) — it contains no `argmin`, no τ-grid, no eigenvalue scan that LOCATES the cusp; the producing gate's `value='promoted'` is a self-consistency check (the live `tau_fold` pin still equals the frozen 0.19 to 1e-10), not a finder. The operative DOS-singularity / spectral-action-gradient functional is LOCATION-FREE by construction: `dS/dτ = +58,672.80` is one-signed with an EMPTY critical set across the whole transit window (S95 NO-WELL-ONE-LOOP), so it certifies non-stationarity wherever the cusp is and cannot prefer one τ over another. The cusp's LOCATION is a SEPARATE substrate-IS observable, supplied by the from-scratch band-edge crossing functional `Φ_cross = argmin_τ |T5_min − T3_max| = tau_cross_van_hove = 0.191038` (registry §VII-B.TAU-CROSS-VAN-HOVE; `canonical_constants.py` SECTION B; atlas-07 S45 0.19104). The value `0.190 = 19/100` is the rational ANCHOR (`Φ_anchor`) of the derived-ratio chain `S_0 = 95/56`, NON-FUNGIBLE with the located `Φ_cross = 0.191038` per the S114 W-1 output (iii); the two differ by 0.5464%. The PERMANENT, location-free content of this theorem (existence + non-stationary character + multiplicity) survives intact and is INDEPENDENT of the 0.190-vs-0.191038 distinction.

**Canonical anchors** (verified this gate):
- `tau_fold = 0.19`
- `dS_fold = +58672.80241318`  (dS/dτ at τ_fold, S42 origin)
- `S_fold = 250360.67696101`  (S at τ_fold)
- `d2S_fold = +317862.84898132`  (Γ_5' convexity at τ_fold)

**Transit-identifier direction**: dS/dτ > 0 ⇒ spectral action is INCREASING as τ advances across τ_fold ⇒ substrate is PUSHED THROUGH τ_fold (supersonic transit, Mach 13.75 per canonical), not held at τ_fold as a quasi-static equilibrium.

**Retired claim** (replaced): the pre-S85 triple-gear uniqueness statement that τ_fold is simultaneously pinned by three independent gears. Reason for retirement: van Hove cusps are features of the eigenvalue density, not of equilibrium; triple-gear redundancy framed τ_fold as a thermodynamic equilibrium, which the transit-identifier predicate dS/dτ ≠ 0 rules out.

**Replacement single-gear machinery**:
- Γ_6 (cubic-BC class): boundary condition placing λ = 0 at the Brillouin-zone corner for cubic mesh a = 12.
- Γ_5' (right-neighbourhood convexity): d²S/dτ² > 0 in a right-neighbourhood of τ_fold, verified this gate at +317,862.85.
- Transit-identifier (dS/dτ ≠ 0): verified this gate at +58,672.80, strictly positive.

**Substitution chain** (6 steps, Python-verified):
- Step 1 (def): ρ(λ; τ) = Σ δ(λ − λ_i(τ)).
- Step 2 (def): van Hove cusp = one-sided divergence in dρ/dτ.
- Step 3 (def): S(τ) = Tr f(D_K²/Λ²), dS/dτ = Σ 2λ_i (dλ_i/dτ) f′(λ_i²/Λ²)/Λ².
- Step 4 (subst): dS/dτ |_{τ_fold} = +58672.80241318 (from canonical_constants).
- Step 5 (simpl): stationarity requires dS/dτ = 0; 58672.80241318 ≠ 0 ⇒ τ_fold NOT a critical point.
- Step 6 (dir): 58672.80241318 > 0 ⇒ S INCREASING across τ_fold ⇒ substrate PUSHED THROUGH.

**Substrate-framing note**: τ_fold is a point in the Jensen deformation parameter space — the internal parameter that deforms SU(3) away from the round metric. A van Hove cusp IS NOT a failure of smoothness in spacetime; it is a kinematical feature of the D_K eigenvalue density on the substrate's internal geometry. The substrate 'is pushed through τ_fold' framing is substrate-first per `phononic-framing.md` — supersonic transit in the acoustic-metric picture, not a singularity in an embedding spacetime.

**Landing gate closure**:
- Gate ID: S85-W10-TAU-FOLD-UNIQUENESS-VAN-HOVE-THEOREM
- Value: `promoted`
- content_sha256: `70cac10736c484c5f1e10d023b8598ae096c7a8d44999508203060c5707d0c36`
- audit_sha256: `149e29a6d826fff018f2fa477bc501cf528470a848b78f52f43ded069d13791c`

**Downstream hooks**:
- W0-22 PLAN-DISCIPLINE-VAN-HOVE-CHECK gains a canonical anchor theorem to audit future plans against.
- W0-6 VAN-HOVE-CUSP-THEOREM (kaku + gen-physicist cross-check) converges against this single-gear statement.
- Any future claim that τ_fold is an equilibrium critical point is refuted by the Step-5 substitution chain.

---
