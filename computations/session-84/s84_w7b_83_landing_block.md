
---

## §VII.O — Admissibility Singleton and IKKT Anti-Correspondence Theorem (S84 W7b-83, 2026-04-19)

**Source**: S84 W7b-83. Script `computations/session-84/s84_w7b_83_vii_n_registry_landing.py`; data `s84_w7b_83_data.npz`; block `s84_w7b_83_landing_block.md`.

**Classification**: GEOMETRIC (theorem-landing). Substrate framing: the eigenvalue spectrum of D_K on Jensen-deformed SU(3) admits exactly one (d_total, KO-dim, A_F) configuration consistent with (i) Mellin-cone d-singleton, (ii) CCM KO-dim=6 sign-table row, (iii) three-generation SM gauge content, and (iv) two-scale power-law |E_cond(L)| interpolating between finite-L b ∈ [4.58, 4.78] and asymptotic b → 7 = d_int − 1 (Weyl). The singleton is (12, 6, C ⊕ H ⊕ M_3(C)).

**Slot-allocation note**: Target slot §VII.N was occupied by the Three-Layer Regulator Theorem (S84 W2a-11, 2026-04-19) which itself cascaded from §VII.M (W1b-9 DR3-RESPONSE-PROTOCOL). Landing cascades to §VII.O per the same slot-allocation remediation precedent documented within §VII.N itself. Registry-hygiene violation logged; theorem content unaffected.

### Formal statement

**Theorem VII.O (Admissibility Singleton and IKKT Anti-Correspondence).** Let (A_F, H_F, D_F) be a finite-dim spectral triple over a product spacetime M^4 × K with K a compact simple Lie group, equipped with Mellin-cone pairing Tr(|D|^{−s}) and Connes-Marcolli KO-dim sign-table classification (CCM 2013 Table 1). The admissibility requirements

  (i)   d_total-singleton via Mellin-cone residue (S83-G32);
  (ii)  KO-dim = 6 via CCM 2013 Table 1 (S82 MG-2);
  (iii) SM gauge content (three generations + gauge bosons);
  (iv)  power-law |E_cond(L)| ~ L^b with
          b_finiteL ∈ [4.58, 4.78] at L ∈ [3..8],
          b_midL   ≈ 4.92          at L ∈ [3..12],
          b_asymp  → 7 = d_int − 1 (Weyl limit)
        (S83-G36 + W7b-75 + W7b-76);
  (v)   twist-triple non-extension under Connes-Moscovici (2008) axioms (W7b-77),

together uniquely determine (d_total, KO-dim, A_F) = (12, 6, C ⊕ H ⊕ M_3(C)). The IKKT large-N matrix model (linear-L scaling, b = 1) is excluded **analytically** by the Seeley-DeWitt Weyl limit in (iv), not merely empirically by a finite-L fit. Eleven-dimensional M-theory compactifications — which require d_total = 11, or d_total = 12 with a distinct A_F — are excluded.

### 4-proof chain

**Sub-proof (1) — Mellin-cone d-singleton.** S83-G32 DIMREDUCTION-AUDIT PASS established that the Mellin-cone residue pairing Tr(|D|^{−s}) admits a unique residue-positive cone at d = 12 under KO-dim = 6 constraint; d = 11 is excluded (A4, A5, SM violations). Anchor SHA: `edcee689643101efd442d0c0ca895c32560d31c8ef258b14873d1c94ab5ee216`.

**Sub-proof (2) — CCM KO-dim=6 sign-table reduction.** Connes-Marcolli (2013) Table 1 together with S82 MG-2 even-KO and SM-chirality constraints reduces the admissible triples to (12, 6, A_F) with A_F = C ⊕ H ⊕ M_3(C). Anchor (G36 V-rescaled branch): `86347fac0c61085bedb467ea13f77920f6b09c8e16a08245d64404f321825578`.

**Sub-proof (3) — Power-law scaling with SDW analytic match (IKKT excluded).** S83-G36 recovered a PASS power-law fit b_power = 4.681 at L ≤ 8. W7b-75 extended the L scan to L ≤ 12 and found b drifting: b = 4.681 (L ≤ 8) → 4.988 (L ≤ 12) → 5.02 (all points). W7b-76 derived the drift **analytically** via the Seeley-DeWitt heat-kernel expansion: b(L) interpolates between a finite-L plateau b_finiteL ∈ [4.58, 4.78] (set by the lowest-order a_k coefficients) and an asymptotic Weyl limit b_asymp → 7 = d_int − 1 (the internal-space dimension minus one). IKKT linear scaling (b = 1) is thus excluded not by a single empirical fit but by the **analytic Weyl asymptote** itself — any b → 1 limit would require d_int = 2, which contradicts d_total = 12 under KO-dim = 6. Anchors: W7b-75 `786f6ce3e0f992722e3d19afea3d4f740e076bf985b9cd4d2008526c4e2a1c53` (FAIL; drift-confirmed) + W7b-76 `0a60ebfd6dafcbc2f1bb622814873cfae6fb97cf18136aafd2e62e40817538f0` (PASS; analytic SDW).

**Sub-proof (4) — Twist-triple non-extension.** W7b-77 scanned 16 Connes-Moscovici (2008) twisted-triple candidates and confirmed that zero admissible twists extend the singleton; the M-theory twist-sector pathway is closed. Anchor SHA: `7308dd7e2244c1a8797e6935cdd6ebfec41a894b61bc359aec8fd1a810c5d9ab`. W7b-78 closed the correspondence table (0 open; 11 ANTI / 5 GENUINE / 12 STRUCTURAL / 3 SUGGESTIVE): `bcbc592918397a7568c5871e0f408a97c972f440029109dd2ab579f1d140c120`.

**Regulator-uniqueness NOT in chain.** W7b-81 returned FAIL (8/11 MP-admissible); the MP-filter is not a regulator-uniqueness argument. The 4-proof chain above is complete WITHOUT citing regulator-uniqueness.

### Scope

This theorem applies to spectral triples (A_F, H_F, D_F) over product spacetimes M^4 × K with K a **compact simple Lie group**, KO-dim = 6, and finite-dim A_F over the complex numbers. Extensions to non-compact K, higher-rank exceptional groups, or twisted (Connes-Moscovici 2008) spectral triples require re-derivation; W7b-77 confirmed that no such twisted extension admits the singleton, but the scope of the non-extension is itself axiom-set-specific (CM2008-twist).

### Falsifier (two-scale predicate)

The theorem is falsified by any string or matrix-model construction demonstrating **BOTH**:

  (a) KO-dim = 6 irreducible representation structure consistent with CCM 2013 Table 1; **AND**
  (b) |E_cond(L)| power-law scaling with b ∈ [4.58, 4.78] at finite L (L ∈ [3..8]) AND b → 7 at asymptotic L (Weyl d_int − 1 limit).

Both conditions must be met **simultaneously**; demonstrating either in isolation does not falsify. The two-scale predicate reflects W7b-76's SDW interpolation result: a single-scale empirical match at finite L is insufficient, because the drift itself is structural (set by the a_k coefficients). The Weyl asymptote is the robust signature.

### Cross-references

- **S83-G32** DIMREDUCTION-AUDIT — d_total-singleton
- **S83-G36** MATRIX-MODEL-CLASSIFICATION — power-law finite-L fit
- **S84-W7b-75** B-POWER-STABILITY — drift confirmation
- **S84-W7b-76** SDW-B-PREDICTION — analytic Weyl limit
- **S84-W7b-77** TWISTED-TRIPLE-ADMISSIBILITY — twist-sector closure
- **S84-W7b-78** CORRESPONDENCE-TABLE-CLOSURE — 11 ANTI / 5 GENUINE / 12 STRUCTURAL / 3 SUGGESTIVE
- **Connes-Marcolli 2013 Table 1** — KO-dim sign-table source
- **Connes-Moscovici 2008** — twisted spectral triple axioms (scope of (5))

### Anchor-SHA pin block

  S83-DIMREDUCTION-AUDIT                             : sha256 = `edcee689643101efd442d0c0ca895c32560d31c8ef258b14873d1c94ab5ee216`
  S83-MATRIX-MODEL-CLASSIFICATION-V-RESCALED         : sha256 = `86347fac0c61085bedb467ea13f77920f6b09c8e16a08245d64404f321825578`
  S84-W7b-75-B-POWER-STABILITY                       : sha256 = `786f6ce3e0f992722e3d19afea3d4f740e076bf985b9cd4d2008526c4e2a1c53`
  S84-W7b-76-SDW-B-PREDICTION                        : sha256 = `0a60ebfd6dafcbc2f1bb622814873cfae6fb97cf18136aafd2e62e40817538f0`
  S84-W7b-77-TWISTED-TRIPLE-ADMISSIBILITY            : sha256 = `7308dd7e2244c1a8797e6935cdd6ebfec41a894b61bc359aec8fd1a810c5d9ab`
  S84-W7b-78-CORRESPONDENCE-TABLE-CLOSURE            : sha256 = `bcbc592918397a7568c5871e0f408a97c972f440029109dd2ab579f1d140c120`

**Combined audit SHA** (over ordered input-pin map of 8 input files):

  audit_sha256 = `0835e999079db622ae8ec18bad2a3f3444e4107397277339dd8e3709465dc0be`

### Verdict

**PASS** at registration (landing under §VII.O; intended §VII.N occupied — cascade logged above).

  4-tuple: (value=6_of_6_components_present, scheme=registry-landing-audit, convention=permanent-results-registry-S84, L_max=N/A)
  Entry closure audit_sha256 = `0835e999079db622ae8ec18bad2a3f3444e4107397277339dd8e3709465dc0be`

**What PASS means**: The admissibility singleton (12, 6, C ⊕ H ⊕ M_3(C)) and IKKT anti-correspondence are now permanent framework theorems. Future sessions cite §VII.O by reference; the 4-proof chain is closed. The upgrade from S83-G36's finite-L empirical fit to W7b-76's analytic Weyl limit makes the IKKT exclusion **structural**, not fit-dependent.

**Not in chain**: regulator-uniqueness (W7b-81 FAIL). MP-filter does not select a unique regulator; the theorem does not depend on it. §VII.N's three-layer regulator stratification (W2a-11) handles regulator classification independently.

**Artifacts**: `computations/session-84/s84_w7b_83_vii_n_registry_landing.py` (this script), `s84_w7b_83_data.npz` (combined-SHA anchor + component-audit matrix), `s84_w7b_83_landing_block.md` (standalone block copy), `s84_w7b_83_landing_block.json` (structured payload). **Session working paper**: `sessions/archive/session-84/session-84-w7-workingpaper.md` §W7-83.
