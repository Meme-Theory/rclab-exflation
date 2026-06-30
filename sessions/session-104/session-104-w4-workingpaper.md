# Session 104 Wave 4 — Transit-shape (gem-sourced) (Results Working Paper)

**Session**: 104 | **Wave**: 4 | **Plan**: session-104-plan-w4.md | **Theme**: Transit-shape gems from the S103 research-sweep triage — nonlinear-memory IR slope on the stiff transit EOS (internal-consistency vs blue tilt) + the proton-core type-IV EMT ↔ acoustic white-hole-interior bridge spec.

## Gate Sections

### §W4-1. S104-W4-1-NONLINEAR-MEMORY-IR-SLOPE (quantum-acoustics-theorist)

**Status**: COMPLETED
**Gate ID**: `S104-W4-1-NONLINEAR-MEMORY-IR-SLOPE`
**Trigger**: `[CHAIN]`
**Classification**: **PHONONIC** (GW memory tail is a substrate acoustic-relic SHAPE observable)
**Agent**: `quantum-acoustics-theorist` (cross-check: hawking-theorist — GR-universality of the nonlinear-memory background)
**Hypothesis**: On the stiff Zel'dovich transit EOS (w=1), the Ünal-Veske universal nonlinear-memory deep-IR slope is Ω_GW,mem ∝ f^2 (memory-tail branch), and that slope's effective-w is internally consistent (≤20%) with the effective-w of the independently-pinned blue transit tilt n_T(transit)=+0.4676 at the matched transit scale.
**Plan reference**: `sessions/session-plan/session-104-plan-w4.md` §W4-1 (machinery pin, thresholds, substitution chain source, EOS slot-distinction + scale-channel tag + RETIREMENT note).

**Output Artifacts**:

- **Script**: `computations/session-104/s104_w4_1_nonlinear_memory_ir_slope.py` — `grep -E 'from canonical_constants import|print_verdict_payload'` →
  `from canonical_constants import *  # noqa: F401,F403  (framework constants/provenance)` ; `def print_verdict_payload(verdict, value, audit_sha, content_sha,`
- **Data**: `computations/session-104/s104_w4_1_nonlinear_memory_ir_slope.npz` (13,833 B) — full float64 + exact-rational num/den pairs (`p_stiff_exact_num/den`, `w_slope_exact_num/den`, `w_nT_exact_num/den`, `dev_exact_num/den`) + the emitted transfer formula (`transfer_formula_forward = "n_T(w) = 2*(3w-1)/(3w+1)"`, `transfer_formula_inverse`) + `scale_channel = "TRANSIT-SCALE"` + the FORBIDDEN-comparator documentary fields + `retirement_note`.
- **Plot**: `computations/session-104/s104_w4_1_nonlinear_memory_ir_slope.png` (100,173 B) — `p(w)` over `w∈[0,1]` with the `w=1` memory-tail point (`p=2`, red), the `w=1/3` branch boundary (dashed), and the `n_T(transit)`-implied `w_nT=0.5368` overlay (green square) + consistency annotation.
- **Verdict line**: `computations/session-104/s104_gate_verdicts.txt` — `S104-W4-1-NONLINEAR-MEMORY-IR-SLOPE: FAIL -- value='dev=0.463236_…' … audit_sha256=aefd055be2c1e8181cecc37f77454f2397ce38eb991c3cfdef1d9dd5b661be53 content_sha256=05c95f575756312314c8f9b0a380287aeeaceb0a1f79be6532e7a58b45a767db schema_version=S84+` + dual-SHA companion row + schema-v2 3-tuple row (`sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=VALID`) + 3 extra companion rows (transfer-map / RETIREMENT / slot-distinction). Emitted via the race-safe `emit_verdict` knowledge-MCP tool (single lock-serialized writer; sig_5-unique).

**MCP Pre-Compute Audit**:

Queries executed BEFORE writing the script (per `.claude/rules/knowledge-index-usage.md`; query-first discipline):

- `search_knowledge("w_stiff Zel'dovich stiff EOS transit memory tail nonlinear")` → returns the plan's own equation graph (`p(w_stiff=1)=2`; `w_stiff=1>1/3 ⇒ memory-tail`; `a(t)=a_0(t/t_0)^{1/3} … Zel'dovich's stiff equation of state`); confirms the slot-distinction is documented and the memory-tail result is NOT a closed/canonical entry (genuinely new compute).
- `search_knowledge("n_T transit blue tensor tilt BLUE-65 production scale")` → `NT-BLUE-65 PASS`; `s65_blue_tensor_tilt.py --feeds_into--> gates:BLUE-65`; `n_T = +0.468 is a prediction for HIGH-FREQUENCY GW (k~M_KK), not for CMB B-modes` — confirms the transit-scale comparator and the scale-channel separation.
- `get_constant("n_T_transit")` / `get_constant("w_phonon")` → NOT canonical constants (the transit n_T lives in `s65_blue_tensor_tilt.npz` `n_T`; `w_phonon` in `s53_phonon_eos.npz`) — loaded directly from the frozen npz, not from a stale constant.
- `list_constants("n_T")` → `n_T_PathH_canonical = -0.000933812`, `n_T_PathC_canonical = -0.00146644`, `sigma_n_T_LiteBIRD = 0.0008` — confirms the CMB-pivot images are red and DISTINCT (the FORBIDDEN comparators).
- `trace_entity("nonlinear memory")` → no trace — the Ünal-Veske nonlinear-memory deep-IR slope is NOT yet in the knowledge graph; this gate is its first evaluation on the substrate. NOT PRE-CLOSED.
- `search_knowledge("tensor tilt transfer effective w EOS slow-roll consistency …")` → `n_T(CMB scale) = -3.02e-3 (standard slow-roll -2*eps)`; `Direction: c_T/c_S > 1 -> |n_T_two| > |n_T_single| (PROVEN)` — grounds the slow-roll-consistency transfer map and the scale-channel tagging.

**Verdict**: **FAIL** (composite). 3-tuple: `sign_verdict=PASS` (branch direction correct: `w_stiff=1 > 1/3` ⇒ memory-tail), `magnitude_verdict=FAIL` (consistency deviation `0.463236 > 0.20` band; no info_band pre-registered), `regime_verdict=VALID` (closed-form exact maps evaluated at the matched transit scale; no expansion/truncation breakdown). Collapse: `magnitude=FAIL ∧ regime=VALID ⇒ composite=FAIL`. Per the dual-prior discriminator this reallocates 0.90 to **Track_B** — a genuine **INTERNAL inconsistency** localized between the stiff-EOS pin and the `n_T(transit)` derivation, NOT a dead-detector readout.

`audit_sha256 = aefd055be2c1e8181cecc37f77454f2397ce38eb991c3cfdef1d9dd5b661be53`
`content_sha256 = 05c95f575756312314c8f9b0a380287aeeaceb0a1f79be6532e7a58b45a767db`

**Results**

NUMBERS FIRST (all exact via `Fraction`; Sage-QQ cross-validated at plan-freeze and here):

| Quantity | Value | Form |
|:---|:---|:---|
| `w_stiff` (MEMORY DRIVER, Zel'dovich) | `1` | EXACT (pinned from the Zel'dovich definition; `a(t)~t^{1/3}`) |
| `w_phonon` (DISTINCT relic-gas slot) | `0.202392` | loaded ONLY to PIN the slot-distinction; **NOT** substituted |
| `inner(w=1) = (3·1−1)/(3·1+1)` | `1/2` | EXACT |
| `p(w_stiff=1) = 3 − 2·\|1/2\|` | `2` | `= 2/1` EXACT (Ünal-Veske deep-IR exponent) |
| branch (`w_stiff > 1/3`?) | **memory-tail** | `1 > 1/3` strict ✓ |
| `Ω_GW,mem ∝ f^{p}` | `∝ f^2` | deep-IR memory-tail regime |
| `w_slope = inv_p(p=2, memory branch)` | `1` | `= 1/1` (round-trip exact) |
| `n_T(transit)` [NT-BLUE-65, PASS] | `+0.4676036872` | PRODUCTION/transit scale (`k~5.532e52 Mpc⁻¹`) |
| `w_nT = inv_transfer(n_T(transit))` | `0.536764` | exact rational image of the bit-faithful `Fraction(0.4676036871525688)` |
| `\|w_slope − w_nT\|/w_slope` | `0.463236` | RATIO; threshold `τ = 0.20` |

Cross-handle diagnostics (narrative-only; NOT gates): the memory-slope alone implies `n_T = +1` (maximally blue, what a clean `w=1` background gives); the blue tilt `n_T(transit)=+0.4676` alone implies `p = 2.5324` via `w_nT`. The two handles disagree.

**EOS slot-distinction (load-bearing, Class-8.7-adjacent hazard avoided)**: the memory driver is `w_stiff = 1` (Zel'dovich, `s53_exflation_flatness_output.txt` "w = 1.000004 at fold"; idealized stiff limit). `w_phonon = 0.202392` (`s53_phonon_eos.npz`; post-fold GGE relic-gas EOS at `T_acoustic=0.112`) is a **DISTINCT** object — the relic gas, NOT the expansion-driving background. The script carries a runtime assertion guard (`w_phonon != w_stiff`) so the relic-gas value can never be mis-substituted as the memory-tail driver.

**Scale-channel tag (MANDATORY per `phononic-framing.md`)**: the comparator is the TRANSIT-scale `n_T(transit)=+0.4676` (NT-BLUE-65; `k~k_transit=5.532e52 Mpc⁻¹`, M_KK scale; blue/stiff). The CMB-pivot images are red, DISTINCT, and **FORBIDDEN** as comparators (recorded in the npz as documentary, never used in the gate): `n_T(k_CMB,A) = −0.003024`, `n_T_PathH = −0.000933812`, `n_T_PathC = −0.00146644`; scale separation = `54.04` decades. The memory tail is sourced AT the stiff transit epoch ⇒ the matched scale is the transit scale; comparing the transit-scale memory slope against a CMB-pivot `n_T` would be a container-thinking / scale-conflation FAIL.

**TRANSFER ASSUMPTION (pre-registered, named) — SLOW-ROLL-CONSISTENCY-AT-TRANSIT-SCALE**. The exact `n_T → w_nT` map the script uses (and emits in the npz):
`n_T(w) = 2·(3w−1)/(3w+1)` (forward), inverse `w_nT = (1 + n_T/2) / (3·(1 − n_T/2))`. This is the standard GR relation between the tensor spectral index of a power-law-background GW spectrum and its EOS, evaluated at the SAME (transit/production) scale as `n_T`. It is validated at both EOS anchors: `n_T(w=1) = +1` (maximally blue stiff), `n_T(w=1/3) = 0` (radiation/flat) — and it produces exactly the `(3w−1)/(3w+1)` combination that ties it structurally to `p(w)`, so the two IR-shape handles are the same combination read two ways.

**Substitution chain (directional / threshold claim, per `math-scripts.md §Double-Check Logic`)**:

```
CLAIM: "On w=1 (stiff Zel'dovich), the Ünal-Veske memory slope is p=2 (memory-tail),
        and the consistency deviation EXCEEDS the 0.20 band (FAIL direction)."
Def 1: w_stiff = 1 EXACT                                   [Zel'dovich; s53_exflation_flatness]
Def 2: p(w) := 3 − 2·|(3w−1)/(3w+1)|                       [Ünal-Veske 2511.08514, End-Matter]
Def 3: n_T_transit = +0.4676036871525688                  [NT-BLUE-65, s65_blue_tensor_tilt.npz]
Step 1 (exponent): inner = (3·1−1)/(3·1+1) = 2/4 = 1/2; p(1) = 3 − 2·(1/2) = 2   [EXACT]
Step 2 (branch):   w_stiff = 1 > 1/3  ⇒  memory-tail branch                       [set-membership]
Step 3 (w_slope):  inner_back = (3 − p)/2 = (3 − 2)/2 = 1/2;
                   w_slope = (1 + 1/2)/(3·(1 − 1/2)) = (3/2)/(3/2) = 1            [inverse, round-trip]
Step 4 (w_nT):     inner_nT = n_T/2 = 0.233802;
                   w_nT = (1 + 0.233802)/(3·(1 − 0.233802)) = 1.233802/2.298594 = 0.536764
                                                                                  [SLOW-ROLL-CONSISTENCY-AT-TRANSIT-SCALE inverse]
Step 5 (deviation): dev = |w_slope − w_nT|/w_slope = |1 − 0.536764|/1 = 0.463236  [RATIO convention]
Step 6 (direction): dev − τ = 0.463236 − 0.20 = +0.263236 > 0  ⇒  consistency FAIL [read off canonical form]
Conclusion: p=2 memory-tail (sign PASS); the two effective-w handles disagree at 46.3% > 20%
            at the matched transit scale → genuine INTERNAL inconsistency (magnitude FAIL).
```

**RETIREMENT note (MANDATORY)**: this is a SHAPE / internal-consistency gate. It computes **NO** amplitude / detectability criterion. The Ω_GW amplitude flagship is RETIRED (`falsifier-master-inventory.md` Row #7.audit-3/-4; LISA-STERILE; `Omega_GW_acoustic_LISA_tail = 4.046e-132`), and the memory tail is further sub-threshold. The FAIL here is an **INTERNAL inconsistency** between two substrate-IS shape observables — it is **NOT** a dead-detector readout and must not be read as one.

**Substrate framing (PHONONIC)**: `D_K eigenvalues → stiff transit EOS (w=1, modulus-kinetic domination through the van-Hove fold) → emergent-metric a_2 self-coupling channel → the nonlinear-memory GW background whose deep-IR slope IS the EOS`. The memory tail is a substrate acoustic-relic SHAPE — the post-transit acoustic excitations' interference, whose IR power-law is fixed by the substrate's own stiff EOS through the GR-universal memory relation — NOT "GW produced IN an expanding container". The internal-consistency cross-check asks whether two substrate-IS shape observables (the memory slope and the blue tilt `n_T`), both sourced at the same transit/production scale, reproduce the same effective-w as the GR-universality of nonlinear memory demands. They do not (1.000 vs 0.537), so a substrate-IS inconsistency is localized.

**Assessment / solution-space**: The branch classification is robust and exact — `w_stiff=1` is unambiguously memory-tail, `p=2`. The consistency clause FAILs by a wide margin (46.3% vs the 20% band), which is informative: the memory-tail slope reads the GW-sourcing background as a clean `w=1` power law (which would demand `n_T=+1`), whereas the directly-derived `n_T(transit)=+0.4676` corresponds to `w≈0.54` — only ~halfway from radiation to stiff. The physical reading from the BLUE-65 provenance (`dln eps_H/dτ = +10.29` DOMINANT; the van-Hove DOS spike) is that `n_T(transit)` is set by the **fold-steepening density-of-states**, NOT by a clean power-law `w=1` background re-entry — so the two handles legitimately probe different aspects of the impulsive transit and need not coincide under the naive power-law transfer map. This localizes the suspect leg: the inconsistency is NOT in the Ünal-Veske exponent (exact, GR-universal) but in the mismatch between (i) treating the transit as a clean `w=1` power-law for the memory tail and (ii) the DOS-steepening derivation of `n_T(transit)`. This routes a remediation CF for S105 (whether the stiff-EOS power-law assumption or the slow-roll-consistency transfer reading is the suspect leg, given the DOS-dominated `n_T`). Per the dual-prior INFO clause, an alternative non-power-law transfer reading (steepening-DOS) is the named unpinned leg — but the FAIL stands under the pre-registered SLOW-ROLL-CONSISTENCY-AT-TRANSIT-SCALE map, and the `p=2` memory-tail classification stands regardless of the consistency verdict.

4-tuple: `(value=dev=0.463236_vs_tau=0.20_INTERNAL-INCONSISTENT;p=2_EXACT_memory-tail;w_slope=1.000000;w_nT=0.536764, scheme=UNAL-VESKE-2511.08514-memory-tail, convention=RATIO+set-membership_transfer=SLOW-ROLL-CONSISTENCY-AT-TRANSIT-SCALE, L_max=N/A)`.

---

### §W4-2. S104-W4-2-TYPEIV-EMT-BRIDGE-SPEC (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `S104-W4-2-TYPEIV-EMT-BRIDGE-SPEC`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (the proton core is relay-pattern structure ON the fabric; the acoustic white-hole interior is a substrate transit signature)
**Agent**: `transit-dynamics-theorist` (cross-check: schwarzschild-penrose-geometer — Hawking-Ellis type-IV EMT classification)
**Hypothesis**: A localized relay pattern's substrate acoustic-EMT (a_2 channel) carries a Γ_sub<0 type-IV interior reverting to type-I at the relay's acoustic horizon — the same signature as the PROVEN acoustic white-hole interior (S85-W6-1-AWH-FORMAL); the SPEC names the substrate objects playing Γ and the restoration radius, or honestly declares the construction unnameable.
**Plan reference**: `sessions/session-plan/session-104-plan-w4.md` §W4-2 (SPEC-first bridge discipline, nameability operator, bridge-anatomy + dead-BLV-exclusion pins).

**Output Artifacts**:

- **Script**: `computations/session-104/s104_w4_2_typeiv_emt_bridge_spec.py` — `grep -E 'from canonical_constants import|print_verdict_payload'` →
  `from canonical_constants import *  # noqa: E402,F401,F403` ; `def print_verdict_payload(`
- **Data**: `computations/session-104/s104_w4_2_typeiv_emt_bridge_spec.npz` — structured spec fields: `gamma_sub_object_named=True`, `restoration_radius_named=True`, `s105_spec_emitted=True`, `n_unpinned=1`, `verdict=INFO`, plus the full prose (`gamma_sub_object`, `gamma_sub_to_dumitru_map`, `restoration_radius_surface`, `unpinned_ingredients`, `s105_spec`, `bridge_anatomy`) + the Dumitru paper structural anchors read from the on-disk PDF (`dumitru_discriminant`, `dumitru_type_rule`, `dumitru_typeIV`, `dumitru_restoration`, `dumitru_anec_wall`) + the S85 white-hole side (`s85_value=0.016858`, `tau_H_minus=0.1831`, `tau_H_plus=0.1969`, `mach_at_fold=13.75`).
- **Plot**: `computations/session-104/s104_w4_2_typeiv_emt_bridge_spec.png` — SCHEMATIC cartoon: `Γ_sub(r)=c_s²(1−Mach(r)²)` for an ILLUSTRATIVE core-peaked `Mach(r)` (the real `v(r)` is the S105 prerequisite); type-IV core (Γ_sub<0, red) / type-I exterior (Γ_sub>0, green) / `r_g` Mach=1 crossover ↔ S85 white-hole interior.
- **Verdict line**: `computations/session-104/s104_gate_verdicts.txt` — `S104-W4-2-TYPEIV-EMT-BRIDGE-SPEC: INFO -- value='nameability=(...);n_unpinned=1;...' scheme=DUMITRU-NORONHA-2505.09720-typeIV-discriminant<->S85-W6-1-AWH-FORMAL convention=BRIDGE-SPEC L_max=N/A audit_sha256=644a02512b1e18a568ff4e44bb1acef0810febb8f9ecd65cc38bce37558a608b content_sha256=e8f730028fadbd91883fb2b435efc23022283af2c8f98efe16ee1f1dc2db3fc8 schema_version=S84+` + dual-SHA companion row + 3 extra companion rows (bridge_anatomy / dead_map_exclusion / s105_prerequisite). NO 3-tuple ([VERIFY], not [SIGN]). Emitted via the race-safe `emit_verdict` knowledge-MCP tool (single lock-serialized writer; sig_5-unique).

**MCP Pre-Compute Audit**:

Queries executed BEFORE writing the script (query-first discipline; the bridge composes WITH the S85 PROVEN theorem — confirmed present and asserted-state):

- `trace_entity("S85-W6-1-AWH-FORMAL")` → **gate S85-W6-1-AWH-FORMAL: PASS, value=0.016857840535543706, scheme=EF_null, convention=mostly_minus, L_max=NA**. The composed-with white-hole-interior pin is in the asserted state (PROVEN); the bridge is NOT closed on a broken upstream → no mechanical-closure required.
- `search_knowledge("acoustic white hole interior Killing vector spacelike transit horizon")` → theorem **"Acoustic white hole causal-disconnect FORMALIZED; pre/post-fold causally separated" (PROVEN, S85)**; acoustic metric `ds²_acoustic = (ρ/c_s)[−(c_s²−v²)dt² − 2v dt dτ + dτ²]`; transit `v_transit=6.67 M_KK > c_s=0.485 M_KK`, Mach=13.75; six-layer transit = (supersonic white-hole interior, van-Hove fold τ=0.19, exit horizon τ~0.16). Grounds the substrate side of the bridge.
- `search_knowledge("a2 emergent metric acoustic EMT stress energy tensor effective")` → `g^{μν}_acoustic = (ρ/c_s)·diag(v²/c_s²−1, −1,−1,−1)` (BLV form, S52/S63); `s67_acoustic_tensor.py` computes the acoustic stress tensor with `a2_fold`; `(β_T=0) the tensor sector crosses the fold freely on the a₂-emergent metric g_M`; the a₂ emergent Einstein equation `G_{μν}=8πG_N⟨T_{μν}⟩` (s-framework-parametric-amplification). Supplies the a₂-channel acoustic-EMT and the bridge-map link.
- `search_knowledge("BLV map dead N_pair=1 ... Barcelo Liberati Visser")` → the BLV acoustic metric is the **cosmological single-transit** flow (`a_acoustic = a_geom·√(ρ_s/c_s)`, S53; `N_pair=1, 229.5 hierarchy`); confirms the dead_map_exclusion — BLV is the global transit profile, NOT a localized relay's. The relay acoustic-EMT MUST source from the post-transit a₂ channel only.
- `search_knowledge("localized relay pattern hadron fiber excitation overlap proton substrate")` → a particle/hadron is "a **relay pattern** of modes propagating through the gauge connection" / "a **localized superposition of standing waves**" `Ψ(x,y)=Σ c_{(p,q),n}(x) ψ_{(p,q),n}(y)` (S40/S63). **LOAD-BEARING NEGATIVE**: the relay-pattern is a standing-wave superposition with NO constructed internal flow profile — this is the unpinned ingredient that fixes the verdict at INFO.
- `get_constant("Mach_max")=13.75`, `get_constant("a2_fold")=2776.1653888633655`, `get_constant("tau_fold")=0.19` — confirmed; the bridge is genuinely new (no closure covers the type-IV↔white-hole-interior identity; NOT PRE-CLOSED).

**Verdict**: **INFO**. The candidate type-IV↔acoustic-white-hole-interior identity is **STATEABLE** in substrate variables, and the 4-field S105 compute spec **IS emitted** — but **exactly ONE ingredient is unpinned**: the *localized-relay internal acoustic-flow profile v(r)/Mach(r)*. Per the rubric (`INFO ∈ {identity STATEABLE but ≥1 ingredient unpinned — the unpinned ingredient is NAMED}`), this is a clean INFO with the single unpinned ingredient named. NOT a PASS (the construction cannot run to numerical evaluation without v(r)); NOT a FAIL (the identity is fully nameable and the spec is dispatchable as the v(r)-construction gate).

`audit_sha256 = 644a02512b1e18a568ff4e44bb1acef0810febb8f9ecd65cc38bce37558a608b`
`content_sha256 = e8f730028fadbd91883fb2b435efc23022283af2c8f98efe16ee1f1dc2db3fc8`

**Results**

NUMBERS / STRUCTURE FIRST. The Dumitru-Noronha mechanism (read full-text from the on-disk PDF `05_Dumitru_Proton-EnergyCondition-Violation-GravRadius.pdf`, arXiv:2505.09720 v3, eq. 5 p.3 + §III–IV):

| Paper object | Definition | Hawking-Ellis type |
|:---|:---|:---|
| `Γ = (P_t + T₀₀)² − 4M⃗²` | eq. 5; `M⃗ = T^{0i}` = energy-flux, set by the **J (angular-momentum) GFF** | the discriminant |
| `Γ > 0` | one timelike eigenvector, all eigenvalues real, energy flux boostable away | **type I** (ordinary matter; static frame exists) |
| `Γ = 0` | two degenerate null eigenvectors | type II (radiation; the crossover) |
| `Γ < 0` | complex-conjugate eigenvalue pair, **no causal eigenvector**, NEC violated, "**cannot be static**" (no hypersurface-orthogonal timelike Killing vector, p.4) | **type IV** (proton core) |
| restoration radius | `Γ` crosses 0 at the gravitational radius (1–2 λ_C); in the tail `M⃗,P_t→0` so `Γ→T₀₀²>0` | type-IV → type-II → type-I |
| ANEC wall (eq. 12) | `∫_{−∞}^0 dt [m A(t) − (t/4m)(A(t)−2J(t))] ≥ 0` | model-independent QFT constraint on A,J GFFs |

The candidate bridge — the substrate side (S52/S63 acoustic metric, S85-W6-1 PROVEN):

**(a) The Γ_sub object — NAMED** (a₂-channel acoustic-EMT variables):

```
Γ_sub(r) := c_s² − v(r)²  =  c_s² (1 − Mach(r)²)      [the a₂-channel acoustic-EMT g_tt component,
                                                        sign-normalized so type-I > 0]
```

This is the sign of the acoustic-metric `g_tt ∝ (v²−c_s²)` — the timelike-Killing test. **Sage-verified** sign correspondence (this session): `Γ_sub(v=Mach·c_s) = −(Mach+1)(Mach−1)·c_s² = c_s²(1−Mach²)`, giving

- subsonic `Mach<1` → `Γ_sub>0` → **type I** (∂_t timelike, static acoustic frame exists) ↔ Dumitru `Γ>0`;
- `Mach=1` → `Γ_sub=0` → type II ↔ Dumitru `Γ=0`;
- supersonic `Mach>1` (incl. the transit Mach=13.75) → `Γ_sub<0` → **type IV** (∂_t spacelike, NO static frame) ↔ Dumitru `Γ<0`.

The **structural map to Dumitru's discriminant** (the genuine acoustic-limit map, NOT "analogous"): Dumitru's `Γ<0` is driven by `4M⃗² > (P_t+T₀₀)²` — the energy-flux (momentum-density `T^{0i}`, set by the J/angular-momentum GFF) dominating the diagonal-stress combination. The acoustic analog is the **flow momentum-density term (the `−2v dt dτ` cross term / `v²`) dominating `c_s²`**, flipping `g_tt`. Both are the **same eigenvector-causality question**: does the timelike Killing vector ∂_t stay timelike / does a static rest frame exist? The a₂ emergent Einstein equation `G_{μν}=8πG_N⟨T_{μν}⟩` is what links the acoustic-metric `g_tt` sign to the effective-EMT Hawking-Ellis type — so the map is a genuine acoustic-limit identity, not a verbal analogy.

**(b) The restoration-radius surface — NAMED**: `r_g : Mach(r)=1` — the relay's **acoustic horizon / Mach=1 surface**, where `Γ_sub` crosses 0 (the type-II crossover). This is the localized-relay analog of the PROVEN S85 fold/exit horizon (`tau_H_minus=0.1831`, `tau_H_plus=0.1969` bracketing `tau_fold=0.19`; `mach_at_fold=13.75`). The type-IV→type-I "classicalization" radius of the proton (1–2 λ_C) maps to the relay's Mach=1 surface, the substrate's own acoustic-horizon machinery applied at hadron scale.

**(c) The 4-field S105 compute spec — EMITTED** (with its one named prerequisite):

| Field | Content |
|:---|:---|
| **What** | Construct the localized-relay internal acoustic-flow profile `v(r)/Mach(r)` on the a₂ emergent-metric channel for a localized relay pattern (hadron analog = localized fiber-excitation overlap); evaluate `sign(Γ_sub(r))=sign(c_s²−v(r)²)` at small r vs large r; extract the crossover radius `r_g` where `Mach(r_g)=1` (type-IV→type-II→type-I restoration); operationalize the model-independent ANEC wall on the emergent GFFs. |
| **Inputs** | S85-W6-1-AWH-FORMAL (acoustic metric/horizon machinery, PROVEN); the a₂ acoustic-EMT (`s67_acoustic_tensor.py`, `a2_fold=2776.165`); the localized-relay standing-wave construction (S40/S63 `Ψ=Σ c ψ`) **PLUS the new v(r) flow profile [THE PREREQUISITE]**; the Dumitru ANEC inequality (eq. 12) transcribed to the substrate emergent GFFs; `canonical_constants.py` (`c_s`, `Mach`, `tau_fold`). |
| **Gate** | PASS iff `sign(Γ_sub)<0` at small r (type-IV core: no static acoustic rest frame) AND `sign(Γ_sub)>0` at large r (type-I exterior) AND a finite crossover `r_g` (Mach=1) exists AND the emergent-GFF ANEC wall holds; the crossover-radius and `Γ_sub`-sign tolerances pinned at the S105 plan-freeze. `convention=mostly_minus` (matching S85-W6-1). `[SIGN]` trigger (signed small-r vs large-r prediction). |
| **Effort** | 1–2 gates. Construct `v(r)` for a localized relay (the prerequisite; the open construction); evaluate the radial sign test on the a₂ acoustic-EMT; extract `r_g`; transcribe + test the ANEC wall. CPU-scale unless the relay construction needs the L_max-truncated D_K spectrum (then pin L_max per the Casimir-bound pre-check). |

**The unpinned ingredient (the INFO content) — NAMED**: the *localized-relay internal acoustic-flow profile `v(r)/Mach(r)`* — the a₂-channel analog of the proton's J/angular-momentum-GFF-sourced `T^{0i}(r)` energy-flux radial profile. **Why it is unpinned**: the substrate's relay-pattern is currently a **standing-wave superposition** `Ψ=Σ c_{(p,q),n} ψ_{(p,q),n}` (S40/S63), which has **no constructed internal flow profile** (a static standing wave carries zero net internal momentum-density by construction — `M⃗=0` ⇒ `Γ_sub=c_s²>0` everywhere ⇒ degenerate to type I, missing the type-IV core). The only *constructed* substrate flow is the **global transit** (Mach=13.75, N_pair=1), which is the **dead-BLV COSMOLOGICAL profile** — `dead_map_exclusion_pin`: EXCLUDED for a localized relay. So the small-r `Γ_sub<0` region and the crossover `r_g` cannot be evaluated until a *localized-relay* `v(r)` (the internal acoustic flow / momentum-density of a single relay) is constructed. That construction is precisely the S105 prerequisite the spec names.

**Bridge anatomy (pre-named; SPEC gate, no §VII slot landed)**: Pillar I (acoustic) ↔ Pillar VI (Hawking transit) ↔ Pillar IV (a₂ emergent metric).
- *Substrate-IS*: the a₂-channel acoustic-EMT Hawking-Ellis type of a localized relay (sign of `Γ_sub`).
- *Laboratory-IN*: the Breit-frame proton Wigner EMT Hawking-Ellis type (sign of Dumitru-Noronha `Γ`).
- *Bridge map*: GENUINE acoustic-limit map — `G_{μν}=8πG_N⟨T_{μν}⟩` links the acoustic-metric `g_tt` sign to the effective-EMT eigenvector causality; both reduce to the timelike-Killing / static-frame-existence question. NOT "analogous"/"corresponds to". A future §VII promotion adopts the 5-anatomy + 3-level discipline (`cross-pillar-bridge-anatomy.md`) and the Stage-0 authoring-exclusion (NOT the S85/S97 authors).

**Substitution chain (the structural correspondence stated in substrate variables, per `math-scripts.md §Double-Check Logic`)**:

```
CLAIM (the candidate identity, stated — INFO with one named-unpinned ingredient):
  "There is a substrate discriminant Γ_sub(r)=c_s²−v(r)² built from the a₂-channel
   acoustic-EMT g_tt, with sign(Γ_sub)<0 in the relay core (type IV: no static acoustic
   rest frame) and sign(Γ_sub)>0 in the exterior (type I), the crossover at Mach=1 = the
   relay's acoustic horizon — the SAME signature as the PROVEN S85-W6-1 white-hole interior."
Def 1: Γ (Dumitru eq. 5) = (P_t+T₀₀)²−4M⃗²; Γ<0 ⇒ type IV (complex eigenvalues, no causal
        eigenvector, "cannot be static").                          [PDF p.3-4, full-text read]
Def 2: S85-W6-1-AWH-FORMAL (PROVEN, value=0.016858, EF_null, mostly_minus): white-hole interior
        = ∂_t spacelike across the acoustic horizon (Mach=1).      [trace_entity]
Def 3: Γ_sub(r) := c_s²−v(r)² = c_s²(1−Mach(r)²)  [a₂-channel acoustic-EMT g_tt, type-I>0].
Step 1 (Sage): Γ_sub(v=Mach·c_s) = −(Mach+1)(Mach−1)c_s² = c_s²(1−Mach²).   [exact]
Step 2 (sign map): Mach<1 ⇒ Γ_sub>0 ⇒ type I (Dumitru Γ>0); Mach=1 ⇒ Γ_sub=0 ⇒ type II;
        Mach>1 ⇒ Γ_sub<0 ⇒ type IV (Dumitru Γ<0).                  [structural correspondence]
Step 3 (driver map): Dumitru Γ<0 ⟺ 4M⃗²>(P_t+T₀₀)² (J-GFF energy-flux dominates)
        ⟺ v²>c_s² (flow momentum-density dominates sound speed; g_tt flips).  [same question]
Step 4 (restoration): Dumitru type-IV→type-I at the gravitational radius (1-2 λ_C)
        ⟺ relay acoustic horizon Mach(r_g)=1 = S85 fold/exit-horizon analog.   [crossover map]
Step 5 (nameability, not a number): (a)∧(b)∧(c) all NAMEABLE ✓; n_unpinned=1 (the localized-relay
        v(r) profile) ⇒ verdict = INFO (stateable + spec emitted; one named-unpinned ingredient).
Conclusion: the candidate Pillar-I↔VI↔IV identity is stateable and its S105 sign-test spec is
        emitted; the one gating prerequisite is the construction of a localized-relay v(r). No
        number is computed this session; sign(Γ_sub)≶0 is the S105 forward gate.
```

**Cross-checks**:
- *Unitarity / type-I limit (substrate sanity)*: a static standing-wave relay (`v(r)≡0`) gives `Γ_sub=c_s²>0` everywhere → type I, exactly as a Wigner EMT with `T^{0i}=0` (the spin-0 pion case in the paper, p.6: "where `T^{0i}=0` will not be of type IV"). The substrate reproduces the paper's pion vs proton distinction structurally: only a relay with non-zero internal momentum-density (the proton's J-GFF analog) can carry a type-IV core. ✓
- *Adiabatic / tail limit*: in the paper `r→∞ ⇒ M⃗,P_t→0 ⇒ Γ→T₀₀²>0` (type I). The substrate analog: `v(r)→0` in the relay tail ⇒ `Γ_sub→c_s²>0` (type I). Same far-field restoration to ordinary matter. ✓
- *S85 horizon consistency*: the bridge's `Mach=1` crossover IS the S85 acoustic-horizon definition (`tau_H_minus/plus` bracketing the fold at the global scale); the bridge re-uses the PROVEN machinery without modification. ✓
- *dead-BLV exclusion respected*: the spec sources the relay acoustic-EMT from the a₂ channel and explicitly EXCLUDES the BLV global-transit flow (N_pair=1) as a candidate `v(r)` — the cosmological profile is not a localized relay's internal flow. ✓

**Substrate framing (PHONONIC)**: `D_K eigenvalues → relay-pattern structure ON the fabric (a hadron is a localized fiber-excitation overlap, NOT a particle IN a container) → the a₂ emergent-metric channel's effective acoustic-EMT for that localized relay → the Hawking-Ellis type of that EMT`. The direction is substrate-first: the substrate's transit mathematics (acoustic ergoregion / white-hole interior, where the timelike Killing vector turns spacelike and no static rest frame exists) is logically prior; the claim is that this SAME machinery shows up in a localized relay's acoustic-EMT — "**transit mathematics inside a proton**" — NOT that proton physics explains the substrate. The proton-core type-IV signature (Γ<0, complex eigenvalues, no causal rest frame, type-I restoration at the gravitational radius) IS the substrate's acoustic white-hole-interior signature read at hadron scale.

**Assessment / solution-space**: The candidate cross-pillar bridge (Pillar I acoustic ↔ Pillar VI Hawking transit ↔ Pillar IV a₂ emergent metric) connecting cosmogenesis transit mathematics to QCD hadron-core structure is **OPEN for S105** with zero hadron-specific free parameters — *contingent on one named construction*. The structural correspondence is exact at the sign level (Sage-verified: `Γ_sub<0 ⟺ supersonic ⟺ type IV ⟺ white-hole interior`), the bridge map is a genuine acoustic-limit identity (not a verbal analogy), and both far-field limits (pion `T^{0i}=0` → type I; tail `v→0` → type I) reproduce the paper's structure. The single gating gap — a *localized-relay* internal acoustic-flow profile `v(r)` (the substrate has only the standing-wave `Ψ=Σ c ψ`, which is flow-free, and the dead-BLV global transit, which is excluded) — is the exact INFO ingredient, named as the S105 prerequisite. This routes the v(r)-construction as the S105 forward gate; the structural identity stands as a candidate pending that one pin. The honest reading: the bridge is *not* NOT-DISPATCHABLE (the identity is fully nameable, unlike the S103-W4 FAIL risk), but it is *not yet* a runnable sign-test (the localized-relay flow profile is the missing object) — INFO is the correct, honest middle verdict.

4-tuple: `(value=nameability=(gamma_sub_named=True,restoration_radius_named=True,s105_spec_emitted=True);n_unpinned=1;unpinned=localized-relay_acoustic-flow_profile_v(r);verdict=INFO, scheme=DUMITRU-NORONHA-2505.09720-typeIV-discriminant ↔ S85-W6-1-AWH-FORMAL, convention=BRIDGE-SPEC, L_max=N/A)`.

---

## Wave 4 Synthesis (team-lead)

**Verdicts (2/2 landed, dual-SHA, sig_5-unique)**: W4-1 `S104-W4-1-NONLINEAR-MEMORY-IR-SLOPE` **FAIL** (`aefd055b…`; sign=PASS / magnitude=FAIL / regime=VALID — the pre-registered high-information internal-inconsistency branch) · W4-2 `S104-W4-2-TYPEIV-EMT-BRIDGE-SPEC` **INFO** (`644a0251…`; identity nameable, ONE ingredient unpinned).

- **W4-1**: the branch classification is exact and stands regardless — w_stiff = 1 > 1/3 ⇒ memory-tail, p(1) = 2 EXACT (Sage QQ), Ω_GW,mem ∝ f². The FAIL is the consistency half: the memory slope's effective-w (= 1, round-trip exact) and the n_T(transit) = +0.4676 effective-w (= 0.536764 under the named SLOW-ROLL-CONSISTENCY-AT-TRANSIT-SCALE map) disagree at 46.3% ≫ the 20% band. Because nonlinear memory is GR-universal, this is a **genuine INTERNAL inconsistency** — and the structural reading localizes it: the Ünal-Veske exponent and the transfer map are the SAME (3w−1)/(3w+1) combination read two ways, so the tension is between (i) the clean power-law w=1 reading the memory tail uses and (ii) the **fold-steepening density-of-states origin of n_T(transit)** (dln ε_H/dτ = +10.29 DOMINANT per BLUE-65 provenance — the van Hove DOS spike, not power-law re-entry). Track_B reallocated to 0.90. All three hard fences held: EOS slot-distinction (w_phonon never substituted), transit-scale matching (CMB-pivot images recorded FORBIDDEN), and the RETIREMENT note (zero amplitude/detectability content — this FAIL is NOT a detector statement).
- **W4-2**: the type-IV ↔ acoustic-white-hole-interior identity is **nameable at the acoustic-limit level**, not an analogy: Γ_sub(r) := c_s² − v(r)² = c_s²(1 − Mach(r)²) is the a₂-channel acoustic g_tt, with Sage-verified sign correspondence to the Dumitru-Noronha discriminant (subsonic ⇒ type-I; Mach=1 ⇒ type-II boundary; supersonic core ⇒ type-IV — both sides the SAME does-a-static-rest-frame-exist eigenvector-causality question); the restoration radius is the relay's Mach(r)=1 acoustic horizon (the localized analog of the PROVEN S85 fold/exit horizons). The ONE unpinned ingredient is named: the **localized-relay internal acoustic-flow profile v(r)** — the substrate's relay patterns are currently standing-wave superpositions (flow-free ⇒ Γ_sub > 0 everywhere, degenerate type-I), and the only constructed flow is the global transit profile = the dead-BLV map, EXCLUDED by pin. Limit cross-checks (pion T^{0i}=0 → type-I; tail v→0 → type-I) reproduce the paper's structure.

**Substrate framing (wave-level)**: both gates run the arrow D_K → transit EOS / a₂ emergent-metric channel → shape observables. The W4-1 FAIL constrains the SUBSTRATE-side derivation chain (which reading of n_T's origin is faithful), not any detector; the W4-2 spec asserts "transit mathematics inside a proton" as a nameable candidate, never proton physics explaining the substrate.

### Effected In-Session (NON-MATH — completed by the team-lead orchestrator)

- [x] post-hoc documentation-only annotation of the W4-2 source-PDF filename drift (plan cited `05_Dumitru_TypeIV-EMT.pdf`; on-disk file is `05_Dumitru_Proton-EnergyCondition-Violation-GravRadius.pdf`, same Rank-5 gem) — `sessions/session-plan/session-104-plan-w4.md` input_files block, `post-hoc:` prefixed per `v3-closure-recovery.md` Class-3 documentation-only allowance — runtime drift record in §W4-2

## Carry-Forward Computations

### CF-S105-MEMORY-NT-TRANSFER-ADJUDICATION — internal-inconsistency suspect-leg remediation [MATH]

> **Routing note**: the plan's pre-registered FAIL routing — "remediation CF naming the suspect leg" (plan §"Wave 4 → Wave 5 Decision Point"). The suspect leg is NAMED: the power-law-EOS vs steepening-DOS reading of the n_T(transit)→effective-w transfer.

1. **What**: derive the n_T(transit) → effective-w map under the **steepening-DOS reading** (n_T sourced by the van Hove fold's dln ε_H/dτ = +10.29 spike, not by power-law w-re-entry) and re-run the two-handle consistency comparison; adjudicate whether the transfer reading or the stiff-EOS pin carries the 46.3% discrepancy.
2. **Inputs**: `computations/session-104/s104_w4_1_nonlinear_memory_ir_slope.npz` (exact transfer formula emitted); `computations/session-65/s65_blue_tensor_tilt.npz` (DOS-steepening provenance); `computations/session-53/s53_exflation_flatness_output.txt` (w_stiff anchor); Ünal-Veske 2511.08514 closed form.
3. **Gate**: `S105-MEMORY-NT-TRANSFER` — PASS iff |w_slope − w_nT,DOS|/w_slope ≤ 0.20 under the DOS-steepening map (the transfer reading resolves the inconsistency; the stiff-EOS pin survives); FAIL iff > 0.20 under BOTH readings (the stiff-EOS pin itself becomes the suspect → escalate to a Q1 adjudication). Tolerance and map pinned at S105 plan-freeze.
4. **Effort**: 1 gate.

### CF-S105-RELAY-VR-CONSTRUCTION — localized-relay acoustic-flow profile + sign(Γ_sub) compute [MATH]

> **Routing note**: the plan's pre-registered INFO routing — "the one named unpinned ingredient becomes the S105 prerequisite" (plan §"Wave 4 → Wave 5 Decision Point"). The W4-2 spec block in §W4-2 carries the emitted 4-field detail; this CF mirrors it for `/rclab-plan`.

1. **What**: construct the localized-relay internal acoustic-flow profile v(r)/Mach(r) from the post-transit a₂-channel acoustic-EMT (NOT the dead-BLV global profile, excluded by pin), then evaluate sign(Γ_sub) at small-r vs large-r, extract the Mach=1 crossover radius, and operationalize the model-independent ANEC wall on the emergent GFFs.
2. **Inputs**: `computations/session-104/s104_w4_2_typeiv_emt_bridge_spec.npz` (named Γ_sub object + restoration surface + spec fields); `computations/session-85/s85_w6_acoustic_white_hole_formal.npz` (mostly_minus convention anchor); a₂ canonical (`a_2_FW_zeta`).
3. **Gate**: `S105-TYPEIV-EMT-COMPUTE` — PASS iff sign(Γ_sub) < 0 in the relay core ∧ > 0 in the exterior with the crossover at Mach(r)=1 (type-IV core certified — the Pillar I↔VI↔IV candidate opens for 5-anatomy registration); FAIL iff no sign flip (relay cores are type-I; corridor closes). Sign-test tolerances pinned at S105 plan-freeze.
4. **Effort**: 1.5 gates (v(r) construction + sign/crossover/ANEC evaluation).

## Constraint-Map Updates

| Date | Mechanism / gate | Prior state | New state | Reason |
|:-----|:-----------------|:------------|:----------|:-------|
| 2026-06-10 | Memory-tail branch classification (stiff transit EOS) | unevaluated on the substrate | w=1 ⇒ p=2 EXACT memory-tail (Ω_GW,mem ∝ f²) — stands regardless of the consistency FAIL | S104-W4-1 substitution chain, Sage QQ |
| 2026-06-10 | Two-handle IR-shape internal consistency (memory slope ↔ n_T transit) | single-handle n_T claim (`project_friedmann-wrong-question`) | INTERNALLY INCONSISTENT at 46.3% under the slow-roll transfer reading; suspect leg = power-law-vs-DOS-steepening n_T origin (NOT a detector statement; amplitude RETIRED) | S104-W4-1 FAIL (sign=PASS, magnitude=FAIL) |
| 2026-06-10 | Type-IV EMT ↔ acoustic white-hole-interior bridge (Pillar I↔VI↔IV) | unexamined gem candidate | identity NAMEABLE (Γ_sub = a₂-channel g_tt; restoration radius = Mach=1 surface); blocked on ONE named ingredient (localized-relay v(r)) | S104-W4-2 INFO |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Sizes |
|:-----|:-------|:------------|:------------|:------|
| W4-1 | `s104_w4_1_nonlinear_memory_ir_slope.py` | `s104_w4_1_nonlinear_memory_ir_slope.npz` | `s104_w4_1_nonlinear_memory_ir_slope.png` | 26.9 KB / 13.8 KB / 100 KB |
| W4-2 | `s104_w4_2_typeiv_emt_bridge_spec.py` | `s104_w4_2_typeiv_emt_bridge_spec.npz` | `s104_w4_2_typeiv_emt_bridge_spec.png` (schematic) | 28.3 KB / 25.7 KB / 79.0 KB |

Both verdict lines + dual-SHA companions in `computations/session-104/s104_gate_verdicts.txt` (race-safe `emit_verdict`; W4-1 carries the schema-v2 3-tuple row per its [CHAIN] directional pre-registration + 3 extra fence rows).
