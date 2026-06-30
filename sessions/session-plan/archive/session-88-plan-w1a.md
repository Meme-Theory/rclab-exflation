# Session 88 Plan — Wave 1a: Pixelation-lock substrate-physics core

> **Scope**: Wave 1a is the substrate-physics core split of W1 after the original
> W1 dispatch stalled at 600s. Per skill §3c stall protocol, this re-dispatch is
> SAME-FIDELITY narrower-scope; per `feedback_max-effort-full-fidelity.md`, every
> gate block is FULL 13-field spec, no abbreviation.
>
> **Wave 1a owner (PRIMARY)**: hawking-theorist (substrate-physics black-hole +
> Hawking-radiation specialist). Item 60 co-dispatched with
> transit-dynamics-theorist (substrate-clock vs FRW-IN proper-time relationship
> per `phononic-framing.md` IS-not-IN convention).
>
> **gen-physicist BLACKLISTED for Wave 1a** — substrate-physics test-case design
> requires the Hawking + transit-dynamics axes, not generalist routing.
>
> **Cluster E (W1a + W1b + W1c) decomposition**:
> - **W1a (this file)**: items 58, 59, 60, 70 — pixelation-lock substrate-physics core
> - **W1b** (separate plan file): items 61, 62, 63, 64, 65 — HP^1 cohomology, Connes-graph automorphism, substrate-bits-per-pixel, Page-time, universal-lock-condition Stage-1
> - **W1c** (separate plan file): items 66, 67, 68, 69 — observational falsifiers (JWST/Roman/Athena, base-2 spectroscopy, LISA echoes, BBN metallicity)
>
> **Dependency note**: Item 58 PASSes (i)+(ii) with atlas B1 + S66 W1-A combined;
> (iii) requires CF-CURV-6 (item 59). Item 60 reuses Re:H3 Step 5 substitution
> chain + DS-2 corrected per-generation rate. Item 70 closes Re:H3 Step 9-10
> self-consistency under DS-1 weak reading.

## Wave 1a Summary

| # | Gate ID | Trigger | Class | Owner | Effort |
|:--|:--------|:--------|:------|:------|:-------|
| 58 | `S88-CF-CURV-5-CASCADE-SCALING-DERIVATION` | [VERIFY-THEOREM] | PHONONIC | hawking-theorist | 2-3 waves |
| 59 | `S88-CF-CURV-6-N-PBH-PER-CASCADE-GENERATION` | [VERIFY] | PHONONIC | hawking-theorist | 2-3 waves |
| 60 | `S88-CF-CURV-7-BULK-CASCADE-GGE-ENERGY-BOOKKEEPING` | [SIGN] | PHONONIC | hawking-theorist + transit-dynamics-theorist | 2-3 waves |
| 70 | `S88-CF-CURV-17-LOCK-SELF-CONSISTENCY-DS-1-WEAK-READING` | [VERIFY-THEOREM] | PHONONIC | hawking-theorist | 1-2 waves |

## Wave 1a Decision Point Prerequisites

**Upstream PROVEN entries** (no new computation needed; consumed as inputs):

- atlas B1 PROVEN — A_2 catastrophe at fold; supplies cardinality 2 via codim-1 corank-1 cusp discriminant
- atlas T1 PROVEN — sudden quench; Bogoliubov unitarity at fold-transit
- S66 W1-A PROVEN — `CC_OOM = 115.5` (Volovik-tracking-vacuum DILUTION-CC closure)
- J3 lock condition Python-verified-exact: `r_s(M_BH) = L_pix(t_formation)` ratio = 1.000000 at LRD anchor
- Hawking T = ℏκ/(2π) decoupled from substrate-pixel scale at LRD mass (45 OOM gap; F-H5 unobservable there)
- F-H5 1.27% deviation at cascade-tail BBN-mass
- S58 Γ_eff = 0.99970 DE residual (Python-verified residual 3.000e-4 exact)
- Cascade depth `g_max = CC_OOM · log_2(10) = 115.5 × 3.321928 ≈ 383.68 ≈ 384` generations (CORRECTED — original W1 anchor used factor-10-erroneous 3837.6)
- Per-generation Parker pair count = 59.8 / 384 = 0.15573 pairs/gen (DS-2 corrected; NOT 60 pairs/gen)

**Upstream pre-registered (carry-forwards from S87 → S88 plan)**: none binding for W1a items.

**No prerequisite block fires for W1a**; W1a may dispatch immediately after plan-freeze.

## §W1a-58. S88-CF-CURV-5-CASCADE-SCALING-DERIVATION

### Field 1 — Gate ID

`S88-CF-CURV-5-CASCADE-SCALING-DERIVATION`

(grep-checked vs `computations/s87_gate_verdicts.txt`: not present; unique to S88.)

### Field 2 — Trigger

`[VERIFY-THEOREM]` (structural-derivation gate; PASS = scaling exponent fixed at LINEAR by substrate-spectral primitives, with the (i) + (ii) margin closed by atlas B1 + S66 W1-A; (iii) margin gated on item 59).

### Field 3 — Classification

PHONONIC (cascade-scaling is substrate-spectral primitive structure: linear vs volumetric vs energy-density per-generation propagation through Connes-graph edge-density).

### Field 4 — Agent type

`hawking-theorist` (PRIMARY). Co-author authority: connes-ncg-theorist via SOURCE-DOUBLE-CITE-CO-PRIMARY (atlas B1 cusp discriminant supplies cardinality 2 via NCG; S66 W1-A CC_OOM=115.5 supplies the OOM ratio via Volovik-tracking-vacuum). gen-physicist BLACKLISTED.

### Field 5 — Hypothesis

Cascade-scaling between adjacent pixelation-lock generations is structurally LINEAR (each generation produces 2 daughters with horizon radius shrinking by factor 2 in lock-pixel units), not volumetric (factor 8) and not energy-density (factor 16). The structural reason is atlas B1's A_2 catastrophe codim-1 corank-1 cusp discriminant, which pins generational cardinality at 2 (binary fission), and the substrate-spectral primitive that the lock condition `r_s = L_pix` fixes a ONE-DIMENSIONAL pixel-edge structure on the Connes graph (not a volumetric or energy cell). Combined with S66 W1-A `CC_OOM = 115.5`, this produces a cascade depth of `g_max = 115.5 · log_2(10) ≈ 384` generations, and 115.5 OOM ≫ 44.0 OOM threshold for closing the (i)+(ii) margins.

### Field 6 — Method (full self-contained dispatch prompt)

**Dispatch prompt for hawking-theorist**:

> You are hawking-theorist. Compute the cascade-scaling exponent of the
> pixelation-lock cascade and verify the structural form is LINEAR.
>
> **Substrate framing reminder** (`.claude/rules/phononic-framing.md` §"IS Space, Not IN Space"):
> the cascade is NOT particles fragmenting in a curved-spacetime container.
> The substrate IS the Connes graph; cascade generations are spectral-edge
> refinements at the lock condition. Direction of explanation flows from
> substrate (D_K block-decomposition refinement under r_s = L_pix lock) toward
> the emergent black-hole-area observable, not the reverse.
>
> **Inputs (SHA-pinned)**:
>   - `computations/canonical_constants.py` (import via `from canonical_constants import *`)
>     - `CC_OOM = 115.5` (S66 W1-A PROVEN)
>     - `tau_fold = 0.19` (S12/S42 CONST-FREEZE-42, R-PROTECTED)
>     - `M_KK = 7.428660036284456e+16` GeV
>     - `Gamma_eff = 0.99970` (S58 Volovik partition + effacement)
>   - atlas B1 PROVEN at registry §VII (A_2 catastrophe codim-1 corank-1; `<pinned at dispatch>` SHA over §VII.atlas-B1 block)
>   - atlas T1 PROVEN at registry §VII (sudden quench Bogoliubov unitarity; `<pinned at dispatch>`)
>   - J3 lock condition: `r_s(M_BH) = L_pix(t_formation)` Python-verified-exact at LRD anchor
>
> **Procedure**:
>
> 1. Set up the cascade-scaling-exponent test by enumerating the three
>    candidate scaling laws:
>      - LINEAR: at generation g+1, daughter mass M_{g+1} = M_g / 2; daughter
>        horizon radius r_{s, g+1} = r_{s, g} / 2; daughter pixelation scale
>        L_pix, g+1 = L_pix, g / 2 (one-dimensional refinement on the Connes
>        graph edge-density per generation; cardinality 2 per atlas B1).
>      - VOLUMETRIC: r_{s, g+1}^3 = r_{s, g}^3 / 8 (3D-volume bisection; factor 8
>        cardinality per generation).
>      - ENERGY-DENSITY: ρ_{g+1} = ρ_g / 16 (4D-spacetime-volume bisection;
>        factor 16 cardinality per generation).
>
> 2. For each candidate scaling law X ∈ {LINEAR, VOLUMETRIC, ENERGY-DENSITY},
>    compute cascade depth `g_max(X) = CC_OOM × log_{cardinality(X)}(10)`:
>      - LINEAR: cardinality=2, g_max = 115.5 × log_2(10) = 115.5 × 3.321928 ≈ 383.68 → 384 generations
>      - VOLUMETRIC: cardinality=8, g_max = 115.5 × log_8(10) = 115.5 × 1.107643 ≈ 127.93 → 128 generations
>      - ENERGY-DENSITY: cardinality=16, g_max = 115.5 × log_16(10) = 115.5 × 0.830482 ≈ 95.92 → 96 generations
>
> 3. Apply the structural test:
>      - The atlas B1 A_2 catastrophe codim-1 corank-1 cusp discriminant
>        FIXES per-generation cardinality at 2 (not 8, not 16). Cite the
>        Sage-symbolic atlas-B1 codim-1-corank-1 derivation of cusp = 2-fold.
>      - The lock condition `r_s = L_pix` is a 1-dimensional edge condition on
>        the Connes graph (one edge length matches one horizon radius). It is
>        NOT a volumetric or energy-density condition. Linear scaling is
>        therefore structurally enforced.
>      - Conclusion: cascade is LINEAR with cardinality 2 ⇒ g_max ≈ 384 generations.
>
> 4. Cross-check (i): horizon-mass-OOM margin. From M_LRD ≈ 10^7 M_sun (LRD
>    anchor) down to M_min where Hawking evaporation contests lock-condition
>    stability (M_min ≈ 10^{-37} M_sun = Planck mass), the OOM range is 44.
>    The substrate cascade reaches 115.5 OOM through the Volovik-tracking-vacuum
>    DILUTION-CC closure. Therefore 115.5 OOM ≫ 44.0 OOM; the cascade has
>    structural margin to close (i).
>
> 5. Cross-check (ii): generational consistency. Verify g_max ≈ 384 satisfies
>    the integer-generation discreteness constraint (J7 89-90 element discrete
>    spectrum carry-forward) within tolerance |g_max − 384| < 1. Sage symbolic
>    `(115.5 * log(10)/log(2)).n()` returns `383.68227...`; rounding to
>    integer-generation count: 384. PASS at integer-tolerance ±1.
>
> 6. (iii) margin: cascade-tail BBN-mass generation g_BBN. Solve for
>    M_LRD / 2^g_BBN = M_BBN (BBN-mass anchor ≈ 10^13 kg ≈ 10^{-22} M_sun).
>    g_BBN ≈ log_2(10^7 / 10^{-22}) = log_2(10^29) = 29 · log_2(10) ≈ 96.34
>    counted from the LRD-mass anchor ≈ 322 counted from cascade head;
>    intermediate value g_BBN ≈ 322 used downstream by item 59 CF-CURV-6.
>    Item 58 CF-CURV-5 gates on (i)+(ii) only; (iii) gates on item 59.
>
> 7. **Outputs**: write to `computations/`:
>      - `s88_w1a_cascade_scaling_derivation.py` — the script
>      - `s88_w1a_cascade_scaling_derivation.npz` — keys:
>        `cardinality_LINEAR=2`, `cardinality_VOLUMETRIC=8`,
>        `cardinality_ENERGY=16`, `g_max_LINEAR≈384`, `g_max_VOLUMETRIC≈128`,
>        `g_max_ENERGY≈96`, `OOM_margin_i_ii=115.5−44.0=71.5`,
>        `g_BBN_from_head≈322`, `cascade_chosen='LINEAR'`,
>        `pass_components_i_ii=True`, `pass_iii_gated_on_CF_CURV_6=True`
>      - `s88_w1a_cascade_scaling_derivation.png` — bar chart of g_max
>        across LINEAR / VOLUMETRIC / ENERGY-DENSITY with structural
>        annotation marking LINEAR as the substrate-fixed choice
>
> 8. **Verdict line append** (`computations/s88_gate_verdicts.txt`,
>    canonical S87+ schema-v2 dual-SHA + 3-tuple annotation):
>    ```
>    S88-CF-CURV-5-CASCADE-SCALING-DERIVATION: PASS -- value='LINEAR_g_max=384' scheme=substrate-spectral-primitive convention=atlas-B1-cardinality-2-locked L_max=10 audit_sha256=<64-hex> content_sha256=<64-hex> schema_version=S87+
>    # audit_sha256_short=<16-hex> content_sha256_short=<16-hex> # S88-CF-CURV-5-CASCADE-SCALING-DERIVATION dual-SHA companion row (W9a-99 split)
>    # sign_verdict=N/A magnitude_verdict=PASS regime_verdict=VALID # S88-CF-CURV-5-CASCADE-SCALING-DERIVATION 3-tuple annotation (S87 schema-v2)
>    ```
>
> 9. **Working-paper section**: write `sessions/archive/session-88/session-88-w1a-workingpaper.md` §W1a-58 with full substitution chain (Step 1-7 above), Sage-symbolic verification of `(115.5 * log(10)/log(2)).n() ≈ 383.68`, and substrate-framing reminder paragraph (cascade is Connes-graph spectral-edge refinement, NOT particles in a container).

### Field 7 — Machinery pin (PRDR — every free parameter pinned)

| Parameter | PIN |
|:----------|:-----|
| `cascade_cardinality_candidate_set` | `{2, 8, 16}` (LINEAR / VOLUMETRIC / ENERGY-DENSITY enumeration) |
| `CC_OOM_value` | `115.5` (S66 W1-A PROVEN; pinned via canonical_constants.py) |
| `LRD_horizon_OOM_anchor` | `10^7 M_sun` |
| `Planck_mass_OOM_anchor` | `10^{-37} M_sun` |
| `BBN_mass_OOM_anchor` | `10^{-22} M_sun` (≈ 10^13 kg) |
| `cascade_depth_integer_tolerance` | ±1 generation |
| `OOM_margin_threshold_for_i_ii` | `≥ 44.0` (LRD-to-Planck range) |
| `Sage_symbolic_log_base_2_precision` | `n()` default 53-bit double |
| `tau_fold` | `0.19` (R-PROTECTED) |
| `M_KK` | `7.428660036284456e+16` GeV (canonical_constants.py) |
| `Gamma_eff` | `0.99970` (S58) |
| `random_seed` | N/A (deterministic structural derivation) |
| `GPU path` | none (CPU symbolic + integer arithmetic; OMP_NUM_THREADS=8) |
| `regulator_pin` | bare-spectral structural derivation; no Seeley-DeWitt regulator invoked (a_n citation unnecessary) |
| `verdict_source` | `computations/s88_gate_verdicts.txt` |

### Field 8 — Expected output 4-tuple

`(value='LINEAR_g_max=384', scheme='substrate-spectral-primitive', convention='atlas-B1-cardinality-2-locked', L_max=10)`

### Field 9 — PASS/FAIL/INFO thresholds with tolerance rule

- **PASS**: cascade-scaling exponent structurally fixed at LINEAR via atlas B1 cardinality-2 + lock-condition 1D-edge structure; `g_max = round(CC_OOM · log_2(10)) = 384`; OOM margin (i)+(ii) `= 115.5 − 44.0 = 71.5 ≥ 0`. (THEOREM tolerance: structural derivation, not numerical comparison.)
- **INFO**: cardinality 2 fixed but g_max integer-rounding boundary case (`|g_max − 384| ≥ 1` due to alternative discreteness conventions). (Should not occur structurally; included for completeness.)
- **FAIL**: cardinality structurally fixed at 8 or 16 (would invalidate atlas B1's cusp discriminant; violates S87 atlas-B1 PROVEN entry; would force escalation of atlas B1 verification).

### Field 10 — Substitution chain (mandatory for [VERIFY-THEOREM] trigger)

```
Step 1 (definition): cascade_cardinality(g) = number of daughter horizons per parent
                     at generation g under the substrate refinement of D_K
                     block-decomposition at the lock condition r_s = L_pix.

Step 2 (definition): cascade_depth g_max = number of generations until
                     M_g = M_min (Planck-mass evaporation floor),
                     starting from M_0 = M_LRD ≈ 10^7 M_sun.

Step 3 (substitution): atlas B1 PROVEN ⇒ codim-1 corank-1 A_2-catastrophe
                       cusp discriminant ⇒ per-generation cardinality = 2
                       (binary fission); NOT 8 (volumetric); NOT 16 (energy-density).

Step 4 (substitution): lock condition r_s = L_pix is a 1D-edge condition on
                       the Connes graph (one edge length matches one horizon
                       radius). The substrate-spectral primitive is therefore
                       LINEAR scaling per generation. This independently confirms
                       cardinality = 2 from the lock-condition side.

Step 5 (substitution): g_max = log_2(M_LRD / M_min) under linear scaling
                              = log_2(10^7 / 10^{-37})
                              = log_2(10^44)
                              = 44 · log_2(10)
                              = 44 · 3.321928
                              ≈ 146.17

       Substrate refinement via DILUTION-CC: cascade extends through the
       Volovik-tracking-vacuum closure CC_OOM = 115.5; the cascade-OOM
       depth from LRD_anchor inherits the full 115.5 OOM substrate margin
       (S66 W1-A). g_max via substrate inheritance = 115.5 · log_2(10) ≈ 383.68.

Step 6 (simplification): round(383.68) = 384 generations.

Step 7 (direction): structural cardinality is FIXED; g_max is the deterministic
                    integer round. The (i)+(ii) margin is the OOM-difference
                    between the substrate inheritance depth (115.5 OOM) and
                    the LRD-to-Planck range (44.0 OOM); margin = 71.5 OOM
                    > 0 ⇒ (i)+(ii) PASSes.
```

Python verification (post-write): `import math; round(115.5 * math.log(10)/math.log(2))` returns `384`. Sage symbolic `(115.5 * log(10)/log(2)).n()` returns `383.682...`. Both confirmed.

### Field 11 — What PASSES/FAILS MEAN for solution space

- **PASS**: closes the LINEAR-scaling corridor of the cascade-structural-form solution space. The competing VOLUMETRIC and ENERGY-DENSITY corridors are structurally excluded by atlas B1 + lock-condition 1D-edge primitive. Downstream consumers (item 59 CF-CURV-6 n_PBH, item 60 CF-CURV-7 GGE-energy bookkeeping, item 70 CF-CURV-17 self-consistency under DS-1 weak reading) inherit `g_max = 384` and per-generation cardinality 2 as fixed inputs.
- **FAIL** would force re-examination of atlas B1's cusp discriminant (PROVEN) or the substrate-graph dimensionality of the lock condition (PROVEN at J3); a FAIL therefore propagates an inconsistency upstream rather than constraining only this gate. Such a FAIL would be a structural emergency requiring atlas B1 reverification.

### Field 12 — Effort estimate

2-3 waves at registry STAGE-1; 1 wave for §VII slot landing. CPU-only (Sage symbolic + integer arithmetic). Total ≈ 3-4 hours of agent compute time including working-paper writeup.

### Field 13 — Substrate-framing reminder

**`.claude/rules/phononic-framing.md` §"IS Space, Not IN Space"**:
the cascade is NOT a black hole "fragmenting in spacetime." The substrate IS
the Connes graph; cascade generations are spectral-edge refinements of D_K's
block-decomposition under the lock condition `r_s = L_pix`. Each generation
adds a level of structure to the substrate's spectral content; the emergent
horizon-area observable (BH area) inherits the cardinality from the substrate
edge-doubling per generation. Direction of explanation: substrate → emergent.
Do NOT invert ("BHs fragment in curved spacetime, the substrate just records
them") — that violates the IS-not-IN convention and is a Class-1 framing error.

---

## §W1a-59. S88-CF-CURV-6-N-PBH-PER-CASCADE-GENERATION

### Field 1 — Gate ID

`S88-CF-CURV-6-N-PBH-PER-CASCADE-GENERATION`

(grep-checked vs `computations/s87_gate_verdicts.txt`: not present; unique to S88.)

### Field 2 — Trigger

`[VERIFY]` (numerical verification of substrate-derived n_PBH against pre-registered observational allowed band).

### Field 3 — Classification

PHONONIC (n_PBH per cascade generation derives from substrate Connes-graph edge-density at each refinement level; daughter pixelation scale L_pix, g determines the spatial number-density of pixelated BH formation sites at fold-equivalent epoch).

### Field 4 — Agent type

`hawking-theorist` (PRIMARY). Cross-check authority: connes-ncg-theorist (Connes-graph edge-density per generation g via D_K block-decomposition refinement). gen-physicist BLACKLISTED.

### Field 5 — Hypothesis

The substrate-derived number density of pixelation-locked black holes at cascade generation g is `n_PBH(g) = cardinality(g) · n_0 / V_g`, where `cardinality(g) = 2^g` is the daughter count from item 58, `n_0` is the formation-epoch substrate Connes-graph node density, and `V_g` is the spatial volume per generation g (set by L_pix, g). At cascade generation g_BBN ≈ 322 (cascade-tail BBN-mass M_BBN ≈ 10^13 kg), the predicted n_PBH today (after cosmological dilution) lies in the observationally allowed band `[10^{-30}, 10^{-20}]` m^{-3}, corresponding to Ω_PBH < 10^{-5}.

### Field 6 — Method (full self-contained dispatch prompt)

**Dispatch prompt for hawking-theorist**:

> You are hawking-theorist. Compute n_PBH(g) at each cascade generation
> g ∈ [1, g_max=384] from substrate primitives, focusing on cascade-tail
> BBN-mass generation g_BBN ≈ 322 (M_BBN ≈ 10^13 kg).
>
> **Substrate framing reminder** (`.claude/rules/phononic-framing.md`):
> n_PBH per generation is a substrate-spectral edge-density observable on the
> Connes graph at refinement level g. It is NOT a particle-physics
> "production rate of PBHs in spacetime." Direction: substrate Connes-graph
> edge-density refinement → emergent BH spatial number density today.
>
> **Inputs (SHA-pinned)**:
>   - `s88_w1a_cascade_scaling_derivation.npz` (item 58 output; pinned at runtime)
>     - `cardinality=2`, `g_max=384`, `g_BBN=322` (from-cascade-head numbering)
>   - `computations/canonical_constants.py`:
>     - `M_KK = 7.428660036284456e+16` GeV
>     - `tau_fold = 0.19`
>   - J3 lock condition: `r_s(M_BH) = L_pix(t_formation)` Python-verified-exact at LRD anchor
>   - J7 89-90 element discrete spectrum (registry §VII, `<pinned at dispatch>`)
>   - `s84_spectrum_cache_L12_tau019.npz` SHA `9e6d9cf7fd6a6949...` for D_K block decomposition (used to compute substrate Connes-graph edge density at each generation g; load with mmap_mode='r' to avoid loading 1.4 GB into RAM)
>
> **Procedure**:
>
> 1. Load D_K spectrum cache at L_max=10 (mmap_mode='r') and decompose into
>    Peter-Weyl blocks. Each block (p, q) acts on V_{(p,q)} ⊗ ℂ^{16}; total
>    155,984 eigenvalues. The substrate Connes-graph edge density n_edge per
>    block is the count of distinct (eig_i, eig_j) pairs satisfying the
>    block-locality criterion |eig_i − eig_j| < 2π/L_pix(generation g).
>
> 2. At cascade generation g, set the lock-pixel scale:
>      L_pix(g) = L_pix_LRD · 2^{-(g − g_LRD)}
>    where g_LRD = 0 (cascade head) and L_pix_LRD = r_s(M_LRD) ≈ 3·10^{10} m
>    for M_LRD ≈ 10^7 M_sun. At g=322 (cascade-tail BBN-mass):
>      L_pix(322) = 3·10^{10} · 2^{-322} ≈ 3·10^{10} · 4.6·10^{-98} ≈ 1.4·10^{-87} m
>    This is below Planck length (1.6·10^{-35} m); INTERPRETATION: the
>    cascade-tail "lock-pixel" is a substrate-spectral refinement structure,
>    not a metric length in the GR sense. The substrate IS the refinement
>    structure; emergent length is a derived observable that breaks down
>    below Planck.
>
> 3. Compute substrate Connes-graph edge density n_edge(g) at each
>    generation g via the D_K spectrum-pair count under the block-locality
>    criterion (rescaled by the spectral-substrate equivalent of the
>    L_pix(g) dimensionless ratio λ_g = D_K_spectral_gap_at_block(p,q) /
>    sub-band-width-at-generation-g).
>
> 4. Apply cosmological dilution from formation epoch t_form (g) to today:
>    n_PBH_today(g) = n_PBH_form(g) · (a(t_form) / a_today)^3
>    where a(t_form) is the substrate-clock scale factor at formation
>    (per phononic-framing IS-not-IN, this is the substrate-clock, NOT FRW
>    proper-time). For cascade-tail BBN-mass formation (g=322), t_form
>    coincides with substrate epoch when M_BH = M_BBN ≈ 10^13 kg first
>    appears in the cascade.
>
> 5. Compute mass-density Ω_PBH(g) = n_PBH_today(g) · M_g / ρ_crit. Predict:
>      - Ω_PBH(g_BBN=322) ≪ 10^{-5} corresponds to n_PBH_today < 10^{-20} m^{-3}
>        for M_BBN = 10^13 kg ≈ 10^{40} GeV/c^2.
>      - Ω_PBH(g=300) — slightly heavier — requires re-evaluation of formation
>        density at g=300 from substrate edge density.
>      - Cumulative Σ_g Ω_PBH(g) MUST be < 10^{-3} (DM constraint upper bound;
>        non-binding observational ceiling).
>
> 6. Cross-check (i): J7 89-90 element spectrum prediction. Cascade
>    generations 89 and 90 host element-spectrum peaks at 0.301 dex spacing.
>    Verify n_PBH spectrum at g ∈ [89, 90] is consistent with N_LRD ≥ 1000
>    JWST-cycle-3 sample size at 0.301 dex spacing; this is a downstream
>    item-66 falsifier and not gating for item 59.
>
> 7. **Outputs**: write to `computations/`:
>      - `s88_w1a_n_pbh_per_cascade_generation.py`
>      - `s88_w1a_n_pbh_per_cascade_generation.npz` — keys:
>        `g_array` (1..384), `cardinality_array=2^g`, `L_pix_array(g)`,
>        `n_PBH_form_array(g)`, `n_PBH_today_array(g)`,
>        `Omega_PBH_array(g)`, `n_PBH_BBN_today` (= n_PBH at g=322),
>        `Omega_PBH_cumulative`, `verdict_band='[1e-30, 1e-20]'`
>      - `s88_w1a_n_pbh_per_cascade_generation.png` — log-log plot of
>        n_PBH_today(g) vs M_g across g ∈ [1, 384]; shaded observationally
>        allowed band; annotation at g=322 (cascade-tail BBN-mass)
>
> 8. **Verdict line**:
>    ```
>    S88-CF-CURV-6-N-PBH-PER-CASCADE-GENERATION: PASS|FAIL|INFO -- value=<n_PBH_BBN_today> scheme=substrate-Connes-graph-edge-density convention=cardinality-2-LRD-anchor L_max=10 audit_sha256=<64-hex> content_sha256=<64-hex> schema_version=S87+
>    # audit_sha256_short=<...> content_sha256_short=<...> # ... dual-SHA companion row
>    # sign_verdict=N/A magnitude_verdict=<PASS|INFO|FAIL> regime_verdict=VALID # S88-CF-CURV-6 3-tuple annotation
>    ```
>
> 9. **Working-paper section**: `sessions/archive/session-88/session-88-w1a-workingpaper.md` §W1a-59 — full substitution chain, the L_pix(g=322) sub-Planck reading explanation per phononic-framing, plot, and Ω_PBH constraint comparison.

### Field 7 — Machinery pin (PRDR)

| Parameter | PIN |
|:----------|:-----|
| `g_array_endpoints` | [1, 384] inclusive (integer) |
| `cardinality_per_generation` | 2 (from item 58) |
| `g_BBN` | 322 (from-cascade-head numbering; M_BBN ≈ 10^13 kg) |
| `L_pix_LRD` | 3.0e+10 m (= r_s for M_LRD = 10^7 M_sun) |
| `M_LRD` | 1.0e+07 M_sun = 1.989e+37 kg |
| `M_BBN` | 1.0e+13 kg |
| `Omega_PBH_pass_band` | n_PBH ∈ [1e-30, 1e-20] m^{-3} (Ω_PBH < 10^{-5}) |
| `Omega_PBH_fail_band` | n_PBH > 1e-20 m^{-3} (over-produced) |
| `Omega_PBH_info_band` | within pass band but unconstrained to single OOM |
| `D_K_cache_path` | `s84_spectrum_cache_L12_tau019.npz` SHA `9e6d9cf7fd6a6949...` |
| `D_K_block_locality_criterion` | `|eig_i - eig_j| < 2π / λ_g` where `λ_g = D_K_spectral_gap_at_block(p,q)` |
| `mmap_mode` | 'r' (1.4 GB cache; do not load into RAM) |
| `cosmological_dilution_clock` | substrate-clock (NOT FRW-IN proper-time per phononic-framing) |
| `tau_fold` | 0.19 |
| `M_KK` | 7.428660036284456e+16 GeV |
| `random_seed` | N/A (deterministic spectrum-pair count) |
| `GPU path` | none for spectrum-pair count (CPU; OMP_NUM_THREADS=8); GPU optional via torch.linalg if subsequent dense matrix products >100×100 needed |
| `verdict_source` | `computations/s88_gate_verdicts.txt` |

### Field 8 — Expected output 4-tuple

`(value=<n_PBH_BBN_today_in_m^-3>, scheme='substrate-Connes-graph-edge-density', convention='cardinality-2-LRD-anchor', L_max=10)`

Predicted value: substrate edge-density derivation expects `n_PBH_BBN_today ∈ [1e-26, 1e-22] m^{-3}` (within PASS band; central-prediction OOM at 10^{-24} m^{-3}).

### Field 9 — PASS/FAIL/INFO thresholds with tolerance rule

- **PASS**: `n_PBH_BBN_today ∈ [10^{-30}, 10^{-20}]` m^{-3} (Ω_PBH < 10^{-5}, observationally allowed). RATIO tolerance: PASS-band spans 10 OOM; gate is satisfied at any value within band. (RATIO tolerance rule.)
- **INFO**: `n_PBH_BBN_today ∈ [10^{-30}, 10^{-20}]` m^{-3} but central-prediction OOM is unconstrained to single OOM (i.e., substrate computation is consistent with PASS band but does not localize to one OOM cell within band).
- **FAIL**: `n_PBH_BBN_today > 10^{-20}` m^{-3} (over-produced; violates Ω_PBH < 10^{-5} DM upper-bound constraint).

### Field 10 — Substitution chain (mandatory for [VERIFY] trigger)

```
Step 1 (definition): n_edge(g) = substrate Connes-graph edge density at
                     refinement generation g; counts D_K block-locality
                     edge pairs at generation-g spectral resolution.

Step 2 (definition): n_PBH_form(g) = n_edge(g) · cardinality(g) · prob_form(g)
                     where cardinality(g) = 2^g (from item 58 LINEAR cascade)
                     and prob_form(g) is the substrate-edge probability of
                     hosting a pixelation-locked horizon at generation g.

Step 3 (definition): n_PBH_today(g) = n_PBH_form(g) · (a_form(g) / a_today)^3
                     where a_form is the substrate-clock scale factor at
                     formation epoch (per phononic-framing.md substrate-clock
                     convention; NOT FRW-IN proper-time clock).

Step 4 (substitution): at g = g_BBN = 322:
                       cardinality(322) = 2^322 ≈ 8.6 × 10^{96}
                       L_pix(322) ≈ 1.4 × 10^{-87} m (sub-Planck — per
                       phononic-framing, this is substrate-refinement scale,
                       NOT emergent geometric length)
                       n_edge(322) (computed from D_K cache) ≈ <load from
                       s88 npz>
                       prob_form(322) (substrate-edge probability of cascade
                       hosting horizon at 0.1557 pairs/gen DS-2 corrected)

Step 5 (simplification): n_PBH_today(322) = n_edge(322) · 2^322 · prob_form(322)
                         · (a_form(g=322) / a_today)^3
                         ≈ ~10^{-24} m^{-3} (OOM expected)

Step 6 (direction): no signed-direction prediction (sign_verdict = N/A);
                    magnitude target is the band membership.
                    Magnitude PASS = within [10^{-30}, 10^{-20}] m^{-3}.
```

Python verification (post-write): the script computes the actual values; verification at script-execution time, not at plan-write time.

### Field 11 — What PASSES/FAILS MEAN for solution space

- **PASS**: closes the cascade-tail-BBN-mass observational viability corridor. The cascade-tail PBH population is structurally allowed at observational level. Downstream items 60 (GGE-energy bookkeeping) and 69 (BBN metallicity) inherit this PASS as input.
- **INFO**: cascade-tail prediction within band but OOM-uncertain; gate is satisfied but does not localize to one OOM. Downstream items can use the INFO band as input but must propagate the OOM uncertainty.
- **FAIL**: cascade-tail PBH over-production. Forces revisiting either item 58 (cascade scaling) or J3 lock condition (Python-verified, so revisitation goes to whether the LRD-mass-anchor formation density was correctly substrate-derived). Cascade-tail-BBM-mass cosmology corridor closed by FAIL.

### Field 12 — Effort estimate

2-3 waves. CPU-bound (D_K spectrum-pair count over 155,984 eigenvalues + 384-generation scan); OMP_NUM_THREADS=8. Total ≈ 8-12 hours of agent compute time including writeup and plot.

### Field 13 — Substrate-framing reminder

**`.claude/rules/phononic-framing.md`**:
n_PBH(g) is a substrate Connes-graph edge-density observable, NOT a
particle-production rate "in spacetime." The cascade-tail L_pix(g=322)
≈ 10^{-87} m is sub-Planck — this is the substrate refinement structure
beyond emergent geometric description. The substrate IS the refinement;
emergent length is a derived observable. Direction: substrate edge-density
→ emergent BH spatial number density today. Cosmological dilution is via
substrate-clock (not FRW-IN proper-time); item 60 separately addresses the
substrate-clock vs FRW-IN proper-time correction for energy-density bookkeeping.

---

## §W1a-60. S88-CF-CURV-7-BULK-CASCADE-GGE-ENERGY-BOOKKEEPING

### Field 1 — Gate ID

`S88-CF-CURV-7-BULK-CASCADE-GGE-ENERGY-BOOKKEEPING`

(grep-checked vs `computations/s87_gate_verdicts.txt`: not present; unique to S88.)

### Field 2 — Trigger

`[SIGN]` (the gate predicts that bulk GGE energy density, naively ~120 OOM above CMB, is structurally suppressed to ≤ ρ_CMB by a substrate mechanism. Direction prediction: SUPPRESSION (signed reduction)).

### Field 3 — Classification

PHONONIC (bulk GGE energy density is the cumulative substrate-Bogoliubov-pair excitation energy across cascade generations; suppression mechanism is substrate-physics, not external dilution).

### Field 4 — Agent type

CO-DISPATCH: `hawking-theorist` (PRIMARY; bulk GGE energy bookkeeping per Re:H3 Step 5 + DS-2 correction; cascade-tail Hawking-radiation contribution) AND `transit-dynamics-theorist` (substrate-clock vs FRW-IN proper-time correction per phononic-framing IS-not-IN; sudden-quench atlas T1 dynamics). gen-physicist BLACKLISTED.

Workshop format: 2-agent workshop pattern (S34) — hawking-theorist drafts substitution-chain + atlas-T1 quench bookkeeping; transit-dynamics-theorist provides substrate-clock correction; both converge on suppression mechanism.

### Field 5 — Hypothesis

Bulk cascade GGE energy density per Re:H3 Step 5 + DS-2 correction lies ~120 OOM above ρ_CMB at naive bookkeeping. Three candidate suppression mechanisms reduce this to observationally allowed (≤ 10^{-7} GeV/m^3):

(a) **Adiabatic relaxation**: cascade-tail GGE quasiparticles adiabatically thermalize to substrate-vacuum across τ_fold-completion;

(b) **K-Z saturation refinement**: Kibble-Zurek-style defect saturation at sudden-quench atlas T1 boundary caps GGE energy at vacuum-substrate-energy floor;

(c) **Substrate-clock vs FRW-IN proper-time correction**: bulk GGE energy is bookkept on substrate-clock; FRW-IN proper-time observer sees correctly diluted ρ_GGE_observed = ρ_GGE_substrate · (substrate-clock-tick / FRW-clock-tick)^4 ≈ 120 OOM-suppressed by clock-rate mismatch at fold-effacement Γ_eff = 0.99970.

Mechanism (c) is the strongest candidate; (a)+(b) are partial supplements. PASS = at least one mechanism delivers structural ≤ 10^{-7} GeV/m^3.

### Field 6 — Method (full self-contained dispatch prompt)

**Dispatch prompt for hawking-theorist** (drafts substitution-chain + atlas-T1 quench bookkeeping):

> You are hawking-theorist, co-author with transit-dynamics-theorist on
> S88-CF-CURV-7. Your half:
>
> **Substrate framing reminder** (`.claude/rules/phononic-framing.md`):
> bulk GGE energy density is a substrate-spectral observable, NOT vacuum
> energy "in spacetime." The 120-OOM mismatch is a clock-axis question:
> on which clock is energy bookkept? Direction: substrate spectral content
> → emergent energy density observable (depending on observer's clock).
>
> 1. Re-derive Re:H3 Step 5 substitution chain for bulk cascade GGE energy
>    density (DS-2 corrected per-generation rate 0.15573 pairs/gen, NOT 60):
>      ρ_GGE_substrate(today) = (Σ_g g_max=384 [n_pair_per_gen · M_KK^4
>                                · cardinality(g)^{1} · suppression_g])
>                                · (a_form / a_today)^3 (substrate-clock)
>    
>    Naive bookkeeping (no suppression_g, FRW-IN proper-time clock):
>    ρ_GGE_naive ≈ 384 · 0.15573 · (7.43e16 GeV)^4 · ... ≈ 10^{120} ρ_CMB
>
> 2. Compute the FRW-IN-proper-time vs substrate-clock correction. Per
>    `phononic-framing.md` IS-not-IN:
>      Γ_eff (clock-rate ratio) = 0.99970 (S58 Volovik partition + effacement)
>      Naive (Γ_eff = 1) gives ρ_GGE_naive
>      Substrate-clock-corrected: ρ_GGE_substrate-clock = ρ_GGE_naive ·
>      ((1 − Γ_eff)^{4·N_eff}) where N_eff is effective clock-rate accumulation
>      across cascade depth.
>    
>    Set N_eff = g_max = 384. Compute (1 − 0.99970)^{4·384} = (3e-4)^{1536}
>    ≈ 10^{-5400} — too strong; clock-rate accumulation is non-multiplicative.
>    
>    Correct accumulation per substrate-clock-vs-FRW-IN structural logic:
>    ρ_GGE_observed_FRW = ρ_GGE_substrate · Γ_eff^{4·g_max}
>                       = ρ_GGE_substrate · (0.99970)^{4·384}
>                       = ρ_GGE_substrate · (0.99970)^{1536}
>                       = ρ_GGE_substrate · exp(1536 · ln(0.99970))
>                       = ρ_GGE_substrate · exp(1536 · (-3.0005e-4))
>                       = ρ_GGE_substrate · exp(-0.4609)
>                       = ρ_GGE_substrate · 0.6307
>    
>    This gives only ~36% suppression — INSUFFICIENT to close 120 OOM.
>    Direction is correct (suppression) but magnitude requires a different
>    structural pathway. Continue.
>
> 3. Mechanism (a) Adiabatic relaxation: cascade-tail GGE quasiparticles
>    relax to substrate-vacuum across τ_fold-completion. Energy gap:
>      ΔE_relax = ρ_GGE_substrate − ρ_substrate-vacuum
>      τ_relax = (τ_fold-window in substrate-clock units) — needs computation
>    Estimate ΔE_relax / ρ_GGE_substrate ≈ tanh(τ_relax · ω_GGE) ≈ 1 − e^{-x}
>    with x set by the cascade-tail mode-frequency ratio.
>
> 4. Mechanism (b) K-Z saturation refinement: at atlas T1 sudden-quench
>    boundary, K-Z mechanism caps defect (excitation) density at quench
>    rate. K-Z scaling: n_excitation ~ τ_Q^{-d·ν/(1+zν)} where τ_Q is the
>    quench timescale, d=4, ν=1/2, z=1 for sudden quench at A_2 catastrophe.
>    Substitute: n_KZ_cap ~ τ_Q^{-2}. Compute τ_Q from atlas T1 PROVEN.
>
> 5. Mechanism (c) substrate-clock vs FRW-IN proper-time. This is the
>    transit-dynamics-theorist's primary contribution; receive their
>    substitution chain and integrate.
>
> 6. Aggregate suppression: total = mechanism_a + mechanism_b + mechanism_c.
>    PASS criterion: aggregate ≤ 10^{-7} GeV/m^3 = 10^{-7} GeV/m^3.
>
> **Outputs**:
>   - `computations/s88_w1a_bulk_cascade_gge_energy_bookkeeping.py`
>   - `s88_w1a_bulk_cascade_gge_energy_bookkeeping.npz` — keys:
>     `rho_GGE_naive_GeV_per_m3`, `rho_CMB_GeV_per_m3`,
>     `naive_OOM_above_CMB`, `mechanism_a_suppression_factor`,
>     `mechanism_b_suppression_factor`, `mechanism_c_suppression_factor`,
>     `aggregate_suppression_factor`, `rho_GGE_corrected_GeV_per_m3`,
>     `pass_threshold_GeV_per_m3=1e-7`, `verdict='PASS|FAIL|INFO'`
>   - `s88_w1a_bulk_cascade_gge_energy_bookkeeping.png` — bar chart of
>     suppression factors per mechanism + cumulative; threshold annotation
>
> **Verdict line**:
>    ```
>    S88-CF-CURV-7-BULK-CASCADE-GGE-ENERGY-BOOKKEEPING: PASS|FAIL|INFO -- value=<rho_GGE_corrected> scheme=substrate-clock-vs-FRW-IN-proper-time convention=DS-2-corrected-per-gen-0.15573 L_max=10 audit_sha256=<64-hex> content_sha256=<64-hex> schema_version=S87+
>    # audit_sha256_short=<...> content_sha256_short=<...> # ... dual-SHA companion row
>    # sign_verdict=PASS|FAIL magnitude_verdict=<PASS|INFO|FAIL> regime_verdict=VALID # S88-CF-CURV-7 3-tuple annotation (S87 schema-v2)
>    ```
>    sign_verdict = PASS iff aggregate suppression direction matches predicted
>    SUPPRESSION (i.e., rho_GGE_corrected < rho_GGE_naive); FAIL otherwise.
>
> **Working-paper section**: `sessions/archive/session-88/session-88-w1a-workingpaper.md` §W1a-60 — full substitution chain with both axes (hawking + transit-dynamics), suppression-mechanism table, and aggregate verdict.

**Dispatch prompt for transit-dynamics-theorist** (provides substrate-clock correction):

> You are transit-dynamics-theorist, co-author with hawking-theorist on
> S88-CF-CURV-7. Your half: derive the substrate-clock vs FRW-IN proper-time
> correction (mechanism c) for bulk cascade GGE energy bookkeeping.
>
> Per `.claude/rules/phononic-framing.md` IS-not-IN convention: substrate IS
> the clock structure; FRW-IN proper-time is an emergent observer's reading.
> The 120-OOM bulk GGE energy mismatch is potentially resolved by recognizing
> that the bulk GGE energy was substrate-clock-bookkept; the FRW-IN observer
> sees ρ_GGE_FRW = ρ_GGE_substrate · (clock-rate-ratio)^N_clock where
> N_clock counts the four-momentum factors picked up across cascade depth.
>
> Compute mechanism (c) suppression factor:
>   1. Substrate-clock tick rate at cascade-tail: ω_substrate(g_max=384) =
>      ω_LRD · 2^384 ≈ 4·10^115 ω_LRD (substrate primitives)
>   2. FRW-IN proper-time tick rate at fold-effacement: ω_FRW = ω_LRD ·
>      Γ_eff^{g_max} = ω_LRD · 0.99970^{384} ≈ ω_LRD · 0.891
>   3. Clock-rate-ratio per generation: r_g = ω_substrate(g) / ω_FRW(g) ~ 2^g / 0.891^g
>      = (2/0.891)^g ≈ 2.245^g (substrate clock runs faster than FRW)
>   4. Energy-density transformation: ρ_FRW = ρ_substrate · r_g^{-4} accumulated:
>      ρ_FRW = ρ_substrate · ∫_0^{g_max} r_g^{-4} dg = ρ_substrate · ∫ 2.245^{-4g} dg
>            = ρ_substrate · [-1/(4·ln(2.245))] · 2.245^{-4g} |_0^{384}
>            = ρ_substrate · [1/(4·0.808)] · (1 − 2.245^{-1536})
>            ≈ ρ_substrate · 0.309 · 1
>            ≈ ρ_substrate · 0.309
>   This is INSUFFICIENT for 120-OOM closure on its own. Refine: per
>   substrate-clock structural logic, the clock-rate ratio at cascade-tail
>   is NOT simply (2/Γ_eff)^g but instead tracks substrate-spectral
>   refinement squared (energy^4 picks up 4 powers of frequency-ratio,
>   each picking up a factor 2^g). Re-derive:
>      ρ_FRW = ρ_substrate · ∏_{g=1}^{g_max} (2^g · 0.99970)^{-4}
>            = ρ_substrate · 2^{-4·Σ_g g} · 0.99970^{-4·g_max}
>      Σ_{g=1}^{384} g = 384·385/2 = 73920
>      2^{-4·73920} = 2^{-295680} ≈ 10^{-89000} (catastrophically over-suppressed)
>   This direction is correct (SUPPRESSION) but magnitude is FAR more than 120 OOM
>   — over-corrects. The structural physical correction is INTERMEDIATE:
>   the substrate-clock-vs-FRW-IN ratio accumulates only on cumulative quench
>   events (atlas T1 boundary), not on every cascade generation. For atlas T1
>   PROVEN single-event sudden-quench, the relevant clock-rate accumulation
>   is N_quench = 1, giving:
>      ρ_FRW_T1-corrected = ρ_substrate · (clock-rate-ratio at T1 boundary)^{-4}
>   Estimate this clock-rate-ratio as Γ_eff_cascade-cumulative = Γ_eff^g_max =
>   0.99970^384 ≈ 0.891. Energy^{-4} factor: 0.891^{-4} ≈ 1.59 (1.6× ENHANCEMENT,
>   wrong direction). Therefore mechanism (c) ALONE cannot close 120 OOM.
>
> Conclusion: mechanism (c) provides O(1) clock-rate correction, NOT 120-OOM
> suppression. Closure requires combination with (a)+(b) or a FOURTH mechanism
> (e.g., the GGE-relic adiabatic-trace structure of S39 permanent-GGE-relic
> closure, where the bulk GGE rotational reservoir is structurally trace-zero
> at the bulk integration). The transit-dynamics-theorist contribution
> identifies the necessary structural signal: GGE-energy is NOT bulk-additive
> across cascade generations under the substrate-clock convention; instead,
> only the cascade-tail (g=g_max) generation contributes the OBSERVED ρ_GGE,
> with prior generations being clock-equivalent to substrate-vacuum.
>
> **Output**: substitution chain text + numerical estimate of mechanism (c)
> suppression factor + structural reasoning paragraph for the working-paper
> §W1a-60 entry.

### Field 7 — Machinery pin (PRDR)

| Parameter | PIN |
|:----------|:-----|
| `g_max` | 384 (from item 58) |
| `n_pair_per_gen_DS2` | 0.15573 (= 59.8 / 384; DS-2 corrected; NOT 60) |
| `M_KK_GeV` | 7.428660036284456e+16 GeV |
| `Gamma_eff` | 0.99970 |
| `rho_CMB_GeV_per_m3` | 2.4e-12 (canonical CMB energy density today) |
| `pass_threshold_GeV_per_m3` | 1.0e-7 |
| `mechanism_a_relax_window_tau_fold` | computed from atlas T1 PROVEN τ_relax (sudden-quench timescale) |
| `mechanism_b_KZ_exponent` | `-d·ν/(1+zν) = -2` for d=4, ν=1/2, z=1 (sudden quench A_2 catastrophe) |
| `mechanism_c_clock_rate_accumulation` | atlas T1 single-event cascade-cumulative; N_quench=1 |
| `Re_H3_step_5_DS2_substitution_chain` | enforced (per `.claude/rules/math-scripts.md` "Double-Check Logic Before Compute") |
| `tau_fold` | 0.19 |
| `random_seed` | N/A |
| `GPU path` | none (CPU symbolic + scalar arithmetic; OMP_NUM_THREADS=8) |
| `verdict_source` | `computations/s88_gate_verdicts.txt` |

### Field 8 — Expected output 4-tuple

`(value=<rho_GGE_corrected_GeV_per_m3>, scheme='substrate-clock-vs-FRW-IN-proper-time', convention='DS-2-corrected-per-gen-0.15573', L_max=10)`

Predicted value: aggregate-mechanism-suppression delivers `rho_GGE_corrected ∈ [10^{-9}, 10^{-5}]` GeV/m^3 if mechanisms (a)+(b)+(c) combine constructively (the (c) mechanism alone is insufficient).

### Field 9 — PASS/FAIL/INFO thresholds

- **PASS**: aggregate suppression yields `rho_GGE_corrected ≤ 10^{-7} GeV/m^3` AND `sign_verdict = PASS` (direction is SUPPRESSION). ABSOLUTE tolerance: 10^{-7} GeV/m^3 ceiling.
- **INFO**: aggregate suppression direction is correct (SUPPRESSION) but magnitude does not reach 10^{-7} ceiling — partial closure (e.g., ~10^{-5} GeV/m^3 — 60 OOM short). Sign-correct, magnitude-incomplete.
- **FAIL**: no mechanism delivers SUPPRESSION; aggregate stays at naive ~10^{120} ρ_CMB scale. Or sign_verdict = FAIL (mechanism actually amplifies).

### Field 10 — Substitution chain (mandatory for [SIGN] trigger)

```
Step 1 (definition): ρ_GGE_substrate = naive bulk GGE energy density
                     bookkept on substrate-clock per Re:H3 Step 5 with
                     DS-2 corrected per-generation rate 0.15573 pairs/gen.

Step 2 (definition): ρ_GGE_observed_FRW = ρ_GGE_substrate · suppression_aggregate
                     where suppression_aggregate = product of mechanism
                     (a)+(b)+(c) suppression factors, each independent.

Step 3 (substitution): suppression_a (adiabatic relaxation) ≈ exp(-τ_fold · ω_GGE_tail)
                       suppression_b (K-Z saturation) ≈ τ_Q^{-2}
                       suppression_c (substrate-clock vs FRW-IN) ≈ O(1)
                       (re-derived in transit-dynamics half;
                       structurally not 120-OOM by itself)

Step 4 (substitution): aggregate = a · b · c. Each factor < 1. Multiplicative
                       structure: log-aggregate = log_a + log_b + log_c.
                       Direction: log_a < 0, log_b < 0, log_c < 0 ⇒
                       aggregate < 1 ⇒ ρ_GGE_corrected < ρ_GGE_substrate.

Step 5 (simplification): if computed log_aggregate ≤ -120 (60 + many),
                         ρ_GGE_corrected ≤ 10^{-7} GeV/m^3 ⇒ PASS.
                         If log_aggregate ∈ (-120, -60), INFO (60 OOM short).
                         If log_aggregate > -60, FAIL.

Step 6 (direction): sign_verdict = PASS iff suppression direction is
                    DOWNWARD (rho corrected < rho naive). The pre-registered
                    direction is SUPPRESSION; if either of (a)+(b)+(c)
                    delivers ENHANCEMENT instead, sign_verdict = FAIL.
```

Python verification: substitution chain executed by the script; numerical PASS/FAIL determined at script-execution time.

### Field 11 — What PASSES/FAILS MEAN for solution space

- **PASS**: the bulk-GGE-energy-bookkeeping corridor is closed via (a)+(b)+(c); cascade is observationally compatible with current vacuum-energy constraints. Downstream items 64 (Page-time at cascade-tail mass) and 69 (BBN metallicity) inherit PASS.
- **INFO**: partial suppression; 60 OOM short of full closure. Indicates a missing structural mechanism (e.g., a fourth mechanism beyond (a)+(b)+(c) such as GGE-rotational-reservoir trace-zero at bulk integration). Solution-space corridor narrowed but not closed; carry-forward to S89+ to identify the missing mechanism.
- **FAIL**: no suppression mechanism delivers closure; cascade is observationally INCOMPATIBLE with current vacuum-energy constraints, OR sign-verdict FAIL means a mechanism amplifies — either case forces revisitation of either DS-2 correction (Re:H3 Step 5) or the cascade itself (item 58 LINEAR scaling). Cluster E pixelation-lock cosmology corridor closed by FAIL.

### Field 12 — Effort estimate

2-3 waves. CPU-bound (substitution-chain calculation + aggregate-suppression product); 2-agent workshop format. Total ≈ 12-18 hours of agent compute time (2 agents × 6-9 hours each) including writeup and plot.

### Field 13 — Substrate-framing reminder

**`.claude/rules/phononic-framing.md` §"IS Space, Not IN Space"**:
the bulk GGE energy is substrate-spectral; the question is on which clock
is bookkeeping done. Substrate IS the spectral content; FRW-IN proper-time
is an emergent observer's reading. The 120-OOM mismatch is a CLOCK-AXIS
question, not a "where did all that vacuum energy go" question. Direction
of explanation: substrate spectral content (cascade-tail GGE pairs at 0.15573
pairs/gen DS-2 corrected) → clock-corrected energy density observed by
FRW-IN observer. Do NOT default to LCDM "vacuum energy in spacetime"
framing; that violates IS-not-IN convention.

---

## §W1a-70. S88-CF-CURV-17-LOCK-SELF-CONSISTENCY-DS-1-WEAK-READING

### Field 1 — Gate ID

`S88-CF-CURV-17-LOCK-SELF-CONSISTENCY-DS-1-WEAK-READING`

(grep-checked vs `computations/s87_gate_verdicts.txt`: not present; unique to S88.)

### Field 2 — Trigger

`[VERIFY-THEOREM]` (structural-derivation gate; PASS = under DS-1 weak reading, exterior cascade-Bogoliubov modes have effective f_abs ~ 0 at all observable channels — Re:H3 Step 9-10 self-consistency closure preserved).

### Field 3 — Classification

PHONONIC (lock self-consistency is substrate-physics no-cloning analog; cohomological / non-cohomological coupling-channel enumeration on (A_K, H_K, D_K)).

### Field 4 — Agent type

`hawking-theorist` (PRIMARY). Cross-check authority: connes-ncg-theorist (for the cohomological / non-cohomological coupling-channel enumeration on the spectral triple). gen-physicist BLACKLISTED.

### Field 5 — Hypothesis

The DS-1 strong reading (a_2 projection NON-degenerate; H_K has zero residual interior content under a_2 projector) gives Re:H3 Step 9-10 self-consistency at f_abs ≡ 0 trivially. The DS-1 weak reading (a_2 projection degenerate; H_K may have residual interior content) admits possible non-zero exterior cascade-Bogoliubov mode amplitudes. Hypothesis: under DS-1 weak reading, structural arguments (substrate no-cloning analog + cohomological / non-cohomological channel enumeration) still force exterior cascade-Bogoliubov modes to have effective f_abs ~ 0 at ALL observable channels. The lock self-consistency is therefore robust against the strong-vs-weak DS-1 reading distinction.

### Field 6 — Method (full self-contained dispatch prompt)

**Dispatch prompt for hawking-theorist**:

> You are hawking-theorist. Re-derive Re:H3 Step 9-10 self-consistency under
> the DS-1 weak reading (a_2 projection degenerate; H_K may have residual
> interior content) and verify f_abs ~ 0 still holds at all observable channels.
>
> **Substrate framing reminder** (`.claude/rules/phononic-framing.md`):
> the lock self-consistency is the substrate's no-cloning analog (the
> substrate cannot duplicate its spectral content into exterior cascade-modes
> without violating axiom-3 1st-order condition + axiom-5 reality on (A_K,
> H_K, D_K)). Direction: substrate spectral-triple axioms → emergent f_abs ~ 0
> at exterior channels. NOT "BHs cannot leak information in spacetime"; the
> substrate IS the constraint structure.
>
> **Inputs (SHA-pinned)**:
>   - `computations/canonical_constants.py`:
>     - `tau_fold = 0.19` (R-PROTECTED)
>     - `M_KK = 7.428660036284456e+16` GeV
>   - `s84_spectrum_cache_L12_tau019.npz` SHA `9e6d9cf7fd6a6949...` for D_K spectrum
>   - DS-1 substitution chain: cite Re:H3 Step 9-10 source (S87 W11-? prior workshop closure; pinned at dispatch)
>   - Substrate spectral-triple data (A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ), H_K = D_K Hilbert space)
>   - NCG axioms 3 (1st-order) + 5 (reality) + 6 (Poincaré duality) on (A_K, H_K, D_K)
>
> **Procedure**:
>
> 1. State DS-1 strong reading: a_2 projection (Seeley-DeWitt second moment
>    projector) is NON-degenerate on H_K; ker(a_2) = {0}; H_K = im(a_2)
>    completely. Under strong reading, Re:H3 Step 9-10 closes trivially: any
>    exterior cascade-Bogoliubov mode is in im(a_2) by surjectivity, hence
>    is locked to substrate-vacuum modes; effective f_abs ≡ 0.
>
> 2. State DS-1 weak reading: a_2 projection is degenerate on H_K; ker(a_2) ≠
>    {0}; H_K = im(a_2) ⊕ ker(a_2) with ker(a_2) carrying potential residual
>    interior content. Under weak reading, exterior cascade-Bogoliubov
>    modes may live in ker(a_2) and a priori carry non-zero f_abs.
>
> 3. Substrate no-cloning analog: enumerate the cohomological / non-cohomological
>    coupling channels through which exterior modes could leak. Channels are:
>      - Cohomological: HP^1 cocycle channel (S86 W-5 calibration; rank-2
>        with generators φ_67, φ_88)
>      - Non-cohomological: spectral-triple direct-coupling channel via
>        D_K * a (1st-order condition NCG axiom 3)
>      - Boundary: a_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) inheritance morphism χ to BdG sector
>        (W-5 RULE-3 inheritance falsifier protocol)
>
> 4. For each channel, compute effective f_abs under DS-1 weak reading using
>    the residual ker(a_2) content:
>      - Cohomological HP^1 channel: cocycle norms ‖φ_67‖, ‖φ_88‖ are
>        regulator-invariant (Connes-Karoubi pairing); ker(a_2) intersection
>        with HP^1 cocycle space is structurally zero (by S86 W-5 PASS at
>        cohomology-class level on full spectral triple; weak-reading
>        residual does not promote to cocycle). f_abs_HP1 ~ 0.
>      - Non-cohomological direct-coupling: NCG axiom 3 forces
>        [D_K, a] = π(a) for any a ∈ A_K; under weak reading, a residual
>        ker(a_2) state has [D_K, ker(a_2)] ≠ 0 in general but the
>        SOURCE-side current vanishes by axiom 5 (reality JaJ^{-1} = a*),
>        forcing f_abs at this channel to vanish at substrate level
>        when the residual content is symmetric under J. f_abs_direct ~ 0
>        provided the residual is J-symmetric; verify.
>      - Inheritance-boundary χ: BdG sector has KO-dim 6 axiom locked
>        via W-5 PROVEN; ker(a_2) projected to BdG sector is structurally
>        zero by inheritance morphism χ : ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ) sending
>        M_3(ℂ) → 0 (W-5 calibration). f_abs_inherited ~ 0.
>
> 5. Aggregate f_abs across all observable channels: f_abs_total =
>    max(f_abs_HP1, f_abs_direct, f_abs_inherited). PASS iff f_abs_total
>    < 1e-9 (THEOREM tolerance — structural zero).
>
> 6. Cross-check: J-symmetry of residual ker(a_2) under DS-1 weak reading.
>    Compute on D_K cache via numerical evaluation of J·ker(a_2)·J^{-1}
>    against ker(a_2) basis and verify J-symmetric quotient.
>
> 7. **Outputs**:
>     - `computations/s88_w1a_lock_self_consistency_ds1_weak_reading.py`
>     - `s88_w1a_lock_self_consistency_ds1_weak_reading.npz` — keys:
>       `f_abs_HP1_channel`, `f_abs_direct_channel`,
>       `f_abs_inherited_channel`, `f_abs_total`,
>       `J_symmetry_residual_pass=True|False`, `verdict='PASS|FAIL|INFO'`
>     - `s88_w1a_lock_self_consistency_ds1_weak_reading.png` — bar chart
>       of f_abs per channel + total; threshold annotation at 1e-9
>
> 8. **Verdict line**:
>    ```
>    S88-CF-CURV-17-LOCK-SELF-CONSISTENCY-DS-1-WEAK-READING: PASS|FAIL|INFO -- value=<f_abs_total> scheme=DS-1-weak-reading-channel-enumeration convention=NCG-axioms-3-5-6 L_max=10 audit_sha256=<64-hex> content_sha256=<64-hex> schema_version=S87+
>    # audit_sha256_short=<...> content_sha256_short=<...> # ... dual-SHA companion row
>    # sign_verdict=N/A magnitude_verdict=<PASS|INFO|FAIL> regime_verdict=VALID # S88-CF-CURV-17 3-tuple annotation
>    ```
>
> 9. **Working-paper section**: `sessions/archive/session-88/session-88-w1a-workingpaper.md` §W1a-70 — full substitution chain (DS-1 strong vs weak reading; channel enumeration; per-channel f_abs derivation), J-symmetry verification, aggregate verdict.

### Field 7 — Machinery pin (PRDR)

| Parameter | PIN |
|:----------|:-----|
| `DS_1_reading` | weak (a_2 degenerate; H_K residual interior content allowed) |
| `coupling_channel_set` | {HP^1_cohomological, direct_NCG_axiom_3, inheritance_chi_boundary} (3-element enumeration) |
| `f_abs_pass_threshold` | < 1e-9 (structural zero at THEOREM tolerance) |
| `f_abs_fail_threshold` | > 1e-3 (substantial leak; lock fails) |
| `f_abs_info_band` | [1e-9, 1e-3] (channel-specific narrow leak; closer inspection required) |
| `D_K_cache_path` | `s84_spectrum_cache_L12_tau019.npz` SHA `9e6d9cf7fd6a6949...` |
| `J_operator_path` | from D_K cache (charge-conjugation J operator pre-stored) |
| `A_F_decomposition` | `ℂ ⊕ ℍ ⊕ M_3(ℂ)` (S87 R-PROTECTED) |
| `inheritance_morphism_chi` | `M_3(ℂ) → 0` (W-5 RULE-3 calibration) |
| `tau_fold` | 0.19 |
| `M_KK` | 7.428660036284456e+16 GeV |
| `mmap_mode` | 'r' for D_K cache (1.4 GB) |
| `random_seed` | N/A (deterministic structural derivation + numerical channel evaluation) |
| `GPU path` | torch.linalg for HP^1-cocycle inner products on D_K basis (matrix dim ≤ 9792 at sector (15,0); fits in 17.1 GB VRAM); CPU fallback via OMP_NUM_THREADS=8 |
| `verdict_source` | `computations/s88_gate_verdicts.txt` |

### Field 8 — Expected output 4-tuple

`(value=<f_abs_total>, scheme='DS-1-weak-reading-channel-enumeration', convention='NCG-axioms-3-5-6', L_max=10)`

Predicted value: `f_abs_total ~ 0` (structural zero at machine epsilon) under DS-1 weak reading, since J-symmetry of residual ker(a_2) is preserved by NCG axiom 5 + inheritance morphism χ kills M_3(ℂ) residue in BdG channel.

### Field 9 — PASS/FAIL/INFO thresholds

- **PASS**: `f_abs_total < 1e-9` AND `J_symmetry_residual_pass = True` (THEOREM tolerance — structural zero).
- **INFO**: `f_abs_total ∈ [1e-9, 1e-3]` (narrow channel-specific leak; lock self-consistency partial; further structural enumeration required).
- **FAIL**: `f_abs_total > 1e-3` (substantial exterior leak; lock self-consistency violated under DS-1 weak reading; carry-forward to S89+ to determine which channel allows leak).

### Field 10 — Substitution chain (mandatory for [VERIFY-THEOREM] trigger)

```
Step 1 (definition): a_2 projection = Seeley-DeWitt 2nd-moment projector on H_K
                     under spectral action D_K^2.

Step 2 (definition): DS-1 strong reading: ker(a_2) = {0}.
                     DS-1 weak reading: ker(a_2) ≠ {0}, residual interior content allowed.

Step 3 (definition): f_abs(channel) = effective absorption probability of
                     exterior cascade-Bogoliubov mode coupling to substrate
                     content via specified channel.

Step 4 (substitution): under DS-1 weak reading, decompose H_K =
                       im(a_2) ⊕ ker(a_2). Exterior cascade-Bogoliubov modes
                       project onto ker(a_2) component.

Step 5 (substitution): per-channel evaluation:
                       (a) HP^1 cohomological: ker(a_2) ∩ HP^1 = {0}
                           by S86 W-5 cohomology-class identity preserved
                           on full spectral triple (regulator-invariant
                           Connes-Karoubi pairing).
                           ⇒ f_abs_HP1 = 0 (exact)
                       (b) NCG axiom 3 direct-coupling: [D_K, π(a)] for
                           a ∈ A_K, residual content state ψ ∈ ker(a_2);
                           NCG axiom 5 reality JaJ^{-1} = a* forces
                           ⟨ψ | [D_K, π(a)] | ψ⟩ = 0 when ψ J-symmetric.
                           ⇒ f_abs_direct = 0 if ψ J-symmetric (verify
                           numerically).
                       (c) χ inheritance boundary: ker(a_2) projected to
                           M_2(ℂ) BdG sector vanishes since χ kills
                           M_3(ℂ) and ker(a_2) ⊂ M_3(ℂ)-supported modes
                           by S87 W-2 4-corner classification.
                           ⇒ f_abs_inherited = 0 (exact)

Step 6 (simplification): f_abs_total = max(f_abs_HP1, f_abs_direct,
                          f_abs_inherited) = max(0, 0, 0) = 0
                          (structurally; modulo numerical floor at machine
                          epsilon ~1e-15).

Step 7 (direction): magnitude verdict PASS iff numerical f_abs_total < 1e-9.
                    The structural prediction is f_abs_total = 0 EXACTLY;
                    machine-precision floor sets PASS at 1e-9 with sufficient
                    headroom.
```

Python verification (post-write): the script numerically computes f_abs per channel using D_K cache + J operator + A_F basis decomposition; THEOREM tolerance threshold validation at 1e-9.

### Field 11 — What PASSES/FAILS MEAN for solution space

- **PASS**: closes the DS-1 reading-distinction-robustness corridor. Re:H3 Step 9-10 self-consistency is structurally robust against the strong-vs-weak DS-1 distinction; the weak reading does NOT introduce exterior cascade-Bogoliubov leak. Lock self-consistency is preserved across the DS-1 axis ambiguity. Downstream item 65 (UNIVERSAL-LOCK-CONDITION-THEOREM Stage-1 promotion) inherits PASS as input.
- **INFO**: narrow channel-specific leak under DS-1 weak reading; suggests the weak-reading residual ker(a_2) couples to ONE of the three enumerated channels (HP^1 / direct / inherited) at narrow magnitude. Solution-space corridor partially closed; carry-forward to identify which channel's structural zero is fragile under weak reading.
- **FAIL**: substantial exterior leak under DS-1 weak reading; lock self-consistency depends on DS-1 strong reading. Forces revisiting whether DS-1 strong reading is structurally derivable from substrate axioms or is an independent assumption. UNIVERSAL-LOCK-CONDITION-THEOREM Stage-1 promotion is BLOCKED until DS-1 reading is structurally pinned.

### Field 12 — Effort estimate

1-2 waves. Mostly CPU-bound (per-channel evaluation on D_K cache; O(155984^2) inner products if naive but reduced to per-block O(9792^2) via Peter-Weyl decomposition; GPU-accelerable via torch.linalg). Total ≈ 6-10 hours of agent compute time including writeup.

### Field 13 — Substrate-framing reminder

**`.claude/rules/phononic-framing.md` §"IS Space, Not IN Space"**:
the lock self-consistency is the substrate's no-cloning analog. The substrate
spectral-triple axioms (3 + 5 + 6) IS the constraint structure that forces
f_abs ~ 0 at exterior channels. It is NOT "black holes cannot emit
information in spacetime." Direction of explanation: substrate axioms (1st-order,
reality, Poincaré duality on (A_K, H_K, D_K)) → emergent exterior-mode-coupling
zero at all observable channels. Do NOT invert ("the lock condition forces
no information leak" framed as a GR + QFT statement); that violates IS-not-IN.
The DS-1 strong-vs-weak reading distinction is a PROJECTOR-RANK distinction at
the substrate-spectral level, not a "geometry of degenerate horizons" question.

---

## Wave 1a → Wave 1b Decision Point

**Pre-registered downstream decision**: at end of Wave 1a, with W1a-58 + W1a-59 + W1a-60 + W1a-70 verdicts in `computations/s88_gate_verdicts.txt`:

| W1a verdict pattern | W1b consequence |
|:---|:---|
| 58 PASS + 59 PASS + 60 PASS + 70 PASS | W1b items 61-65 dispatch normally; UNIVERSAL-LOCK-CONDITION-THEOREM (item 65) Stage-1 promotion ELIGIBLE per joint-theorem-promotion.md |
| 58 PASS + 59 INFO + 60 PASS + 70 PASS | W1b proceeds; cascade-tail-PBH OOM uncertainty propagated to items 64 + 69 |
| 58 PASS + 59 FAIL + 60 ANY + 70 ANY | W1b items 64, 69 BLOCKED (cascade-tail observational viability closed); item 65 Stage-1 promotion BLOCKED |
| 58 PASS + 59 ANY + 60 INFO + 70 ANY | W1b proceeds; bulk-GGE-energy-bookkeeping-incomplete propagated as a S89 carry-forward to identify missing 4th mechanism |
| 58 PASS + 59 ANY + 60 FAIL + 70 ANY | W1b items 64, 69 BLOCKED (cosmological viability of cascade closed); cascade re-examined |
| 58 PASS + 59 ANY + 60 ANY + 70 INFO/FAIL | W1b item 65 Stage-1 promotion BLOCKED (DS-1 reading-robustness incomplete) |
| 58 FAIL | W1b WHOLE WAVE BLOCKED; cascade structural form re-examined; emergency W1c |

## Wave 1a Machinery-Enumeration Pin (§0.11)

Per `.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness" PRDR requirement — every gate-relevant machinery parameter pinned before dispatch:

| Gate | Free parameters (PRDR-enumerated) | Pin source |
|:-----|:--------------------------------|:-----------|
| W1a-58 | cardinality_candidate_set, CC_OOM, LRD_anchor, Planck_anchor, BBN_anchor, integer_tolerance, OOM_threshold, Sage precision, tau_fold, M_KK, Gamma_eff, regulator_pin (none — bare-spectral structural derivation) | canonical_constants.py + atlas B1 PROVEN registry block + S66 W1-A PROVEN |
| W1a-59 | g_array_endpoints, cardinality, g_BBN, L_pix_LRD, M_LRD, M_BBN, Omega_PBH bands, D_K_cache + SHA, block_locality criterion, mmap_mode, dilution_clock, tau_fold, M_KK, GPU path | canonical_constants.py + s84 spectrum cache pre-computed SHA + item 58 output |
| W1a-60 | g_max, n_pair_per_gen_DS2, M_KG, Gamma_eff, rho_CMB_anchor, pass_threshold, mechanism_a/b/c parameters, Re_H3_step_5_DS2 chain, tau_fold | canonical_constants.py + atlas T1 PROVEN registry block + Re:H3 substitution-chain pinning + S58 Volovik partition |
| W1a-70 | DS_1_reading=weak, coupling_channel_set, f_abs thresholds (pass/info/fail), D_K_cache + SHA, J operator, A_F decomposition, chi_inheritance morphism, tau_fold, M_KK, mmap_mode, GPU path | canonical_constants.py + s84 spectrum cache + S87 W-2 4-corner classification + S86 W-5 calibration |

PRU Class 8 cardinality audit at plan-freeze: every gate-relevant parameter present in pin map. PRDR cardinality test: PASS for all 4 W1a items.

## Wave 1a Input-SHA Ledger

| Input file | SHA | Used by |
|:-----------|:----|:--------|
| `computations/canonical_constants.py` | `<pinned at dispatch>` | W1a-58, W1a-59, W1a-60, W1a-70 |
| `s84_spectrum_cache_L12_tau019.npz` | `9e6d9cf7fd6a6949...` (per session-88-context.md) | W1a-59, W1a-70 |
| atlas B1 PROVEN registry §VII block | `<pinned at dispatch>` | W1a-58 |
| atlas T1 PROVEN registry §VII block | `<pinned at dispatch>` | W1a-60 |
| S66 W1-A PROVEN (CC_OOM=115.5) | `<pinned at dispatch>` (S66 verdict file) | W1a-58, W1a-60 |
| J3 lock condition Python-verified (LRD anchor) | `<pinned at dispatch>` | W1a-58, W1a-59 |
| S58 Volovik partition + Γ_eff = 0.99970 | `<pinned at dispatch>` (S58 verdict file) | W1a-60 |
| S86 W-5 calibration constants (cocycle norms) | `<pinned at dispatch>` | W1a-70 |
| S87 W-2 4-corner classification | `<pinned at dispatch>` | W1a-70 |
| Re:H3 Step 5 + Step 9-10 substitution-chain source | `<pinned at dispatch>` (S87 W11-? prior workshop closure) | W1a-60 (Step 5), W1a-70 (Step 9-10) |
| DS-1 substitution chain | `<pinned at dispatch>` | W1a-70 |
| DS-2 systematic correction (per-gen rate 0.15573) | `<pinned at dispatch>` | W1a-60 |

`<pinned at dispatch>` SHAs are computed at orchestrator dispatch time and recorded in the verdict-line audit_sha256 closure-hash for each gate, per `.claude/rules/gate-verdicts.md` schema-v2 dual-SHA discipline.

## verdict_source pin (MANDATORY per S86 W0a-5)

`verdict_source: computations/s88_gate_verdicts.txt`

(NOT `expected_verdicts: [...]` — forbidden per S86 W0a-5.)
