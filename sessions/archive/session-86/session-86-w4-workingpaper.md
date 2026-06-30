# Session 86 Wave W4 — BRANCH-IV / SECTOR-2 / cutoff_sqrt adjudication (Results Working Paper)

**Session**: 86 | **Wave**: W4 | **Plan**: session-86-plan-w4.md | **Theme**: Settle 2B path-(c) commit (BRANCH-IV) + 2A SECTOR-2 split (Mellin-kernel K-invariant) + W-4 cutoff_sqrt closure — anchors substrate's BRANCH-IV transit pathway through the van-Hove fold, lifts SECTOR-2's substrate-distance-1 pin, converts S85 workshop verdict into registry-canonical adjudication outcome.

## Gate Sections

### §W4-1. S86-BRANCH-IV-FORMULATION-COMMIT (transit-dynamics-theorist)

**Status**: COMPLETE
**Gate ID**: `S86-BRANCH-IV-FORMULATION-COMMIT`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (BRANCH-IV substrate transit pathway through the van-Hove fold; R_JK + ξ_E_GGE^{−1} as spectral functionals OF the substrate)
**Agent**: `transit-dynamics-theorist` (primary) + `volovik-superfluid-universe-theorist` (cross-cite for ξ_E_GGE^{−1} 3He-B parent → child inheritance, in-script docstring + canonical_constants.py provenance)
**Hypothesis**: BRANCH-IV path-(c) 2B commit canonicalizes the substrate transit pathway with R_JE retired in favor of two distance-tagged spectral diagnostics — R_JK (K-functional, distance-2) and ξ_E_GGE^{−1} (s=−1 GGE coherence-length inverse, distance-1).
**Plan reference**: `sessions/session-plan/session-86-plan-w4.md` §W4-1 (machinery pin, thresholds, 5 CC, framework-file edits, canonical-constants registration).

**MCP Pre-Compute Audit**:
- `search_knowledge("BRANCH-IV R_JE R_JK xi_E_GGE")` → returned 14 equation hits + 1 theorem hit. Confirmed R_JK formula source (`R_JK = (sigma_J * Delta_sq) / (sigma_K * K_base)` from `s85_w12_branch_iv_reaudit_lmax.py`); confirmed S85-2A/2B audit flagged single-name-conflation in R_JE = `xi_J / xi_E_GGE`.
- `search_knowledge("3HeB inheritance distance-1 distance-2")` → returned 14 equation hits including `R_JK(N=0) ≡ K-functional, distance-2 (one substrate operator)` from `session-86-plan-w5a.md` (gen-physicist 9A §3.6 reference). 3He-B inheritance is parent→child per project_3heb-inheritance.md (NOT analogy).
- `list_constants("xi_|R_J")` → 5 matches, NO entry for `R_JK` or `xi_E_GGE_inv` (both Python identifiers free for registration; no name collision).
- `trace_entity("BRANCH-IV-FORMULATION")` → No trace found (this commit creates the canonical entry).

**Verdict**: **PASS** (5/5 CC PASS + loaded-vs-anchor consistency PASS at rel_tol = 1e-12).

**Results**:

**Numerical anchors (full float64 precision)**:
- `R_JK = 0.00803460529503449` (dimensionless ratio, M_KK-natural units; at L_max=10, S85-W12-ELIM-1 PASS anchor).
- `xi_E_GGE_inv = 13.642473425595973` (M_KK units; substrate-natural anchor = 59.8 × Delta_BCS / K_base).

**4-tuple**:
```
(value="R_JE_retired+R_JK_landed+xi_E_GGE_inv_landed",
 scheme="branch-iv-canonical",
 convention="2B-path-c",
 L_max="N/A")
```

**Cross-checks (5 mandatory, all PASS)**:

| CC | Description | Method | Result |
|:---|:------------|:-------|:-------|
| CC-1 | R_JK has units M_KK^{−2} (Newton-constant slot) | M_KK → 2·M_KK rescaling: a_4 → 2^{−4}·a_4, a_2 → 2^{−2}·a_2; ratio R_JK_new/R_JK_old should equal 2^{−2} = 0.25 | ratio = 0.2500000000000000 (exact); abs(ratio − 0.25) = 0.00e+00; **PASS** |
| CC-2 | xi_E_GGE_inv has units M_KK^{+1} (inverse coherence length) | M_KK → 2·M_KK rescaling: lambda_n → 2·lambda_n; Sum → 2·Sum; ratio should equal 2 | mock-eigenvalue ratio = 2.0000000000000000 (exact); anchor-formula ratio (Delta_0 → 2·Delta_0) = 2.0000000000000000 (exact); **PASS** |
| CC-3 | `branch-iv-canonical.md` contains required substrings | Regex search for "R_JE retired/Retirement", "R_JK", "xi_E_GGE"/"ξ_E_GGE" | All 3 substrings present; **PASS** |
| CC-4 | `canonical_constants.py` contains both assignment lines + provenance + 3He-B cite | Regex search for `^R_JK\s*=`, `^xi_E_GGE_inv\s*=`, "S86-W4-1 P4" or gate-id, "3He-B" + "project_3heb-inheritance" | All 4 patterns present at SECTION E.B; **PASS** |
| CC-5 | Re-import succeeds; both names accessible; values numeric | `importlib.reload(canonical_constants)`; `hasattr` + `isinstance(int, float)` | R_JK = 0.00803460529503449 (numeric); xi_E_GGE_inv = 13.642473425595973 (numeric); **PASS** |

Loaded-vs-anchor consistency check (Stage 4 of script): both constants match the freshly-computed anchors at rel_tol = 1e-12 (machine-epsilon).

**Substitution chain (CC-1, CC-2 dimensional traces; commit gate carries no sign/direction claim)**:

CC-1 (R_JK ~ M_KK^{−2}):
```
Step 1 (definitions):
  sigma_J = Tr[D_K^{-4}] / Vol_SU3                  (a_4 spectral moment; M_KK^{-4})
  sigma_K = Tr[D_K^{-2}] / Vol_SU3                  (a_2 spectral moment; M_KK^{-2})
  Delta_BCS, K_base, Vol_SU3                        (dimensionless ratios)

Step 2 (substitute):
  R_JK = (sigma_J * |Delta_BCS|^2) / (sigma_K * K_base)
       = ([M_KK^{-4}] * [1]) / ([M_KK^{-2}] * [1])
       = M_KK^{-4 + 2} = M_KK^{-2}    [Newton-constant slot]

Step 3 (rescaling):
  Under M_KK -> 2*M_KK:
    sigma_J -> 2^{-4}·sigma_J
    sigma_K -> 2^{-2}·sigma_K
    R_JK_new / R_JK_old = (2^{-4}) / (2^{-2}) = 2^{-2} = 1/4

Direction (units): R_JK ~ M_KK^{-2}.   [verified ratio = 0.25 exact]
```

CC-2 (xi_E_GGE_inv ~ M_KK^{+1}):
```
Step 1 (definition):
  xi_E_GGE^{-1} = lim_{s -> -1} zeta_{D_K^(GGE)}(s)
                = (analytic continuation) Sum_n lambda_n^(GGE)
  lambda_n has units M_KK (Dirac eigenvalues are mass-scale).

Step 2 (substitute):
  Sum has units [lambda] = M_KK.

Step 3 (rescaling):
  Under M_KK -> 2*M_KK: lambda_n -> 2*lambda_n
  Sum -> 2*Sum
  xi_inv_new / xi_inv_old = 2

Direction (units): xi_E_GGE_inv ~ M_KK^{+1}.   [verified ratio = 2.0 exact]
```

**Edits performed**:
- `sessions/framework/registry/branch-iv-canonical.md` CREATED (4 sections per plan §6 STEP 1: §1 R_JE Retirement; §2 R_JK; §3 ξ_E_GGE^{−1}; §4 Provenance + cross-cite ledger; §S86 P4 Commit Audit Trail). Content verified by CC-3.
- `computations/canonical_constants.py` AMENDED at SECTION E.B (NEW 2-constant block: `R_JK = 0.00803460529503449`, `xi_E_GGE_inv = 13.642473425595973`) + PROVENANCE dict updated (2 NEW entries with 7-field schema: session, source, gate, superseded, unit, note). Content verified by CC-4.

**Dual-SHA**:
- `audit_sha256 = acc751101c8ca6cec920c8fd58198a6a147bc925455f198613002a8e40161049` (script + canonical_constants.py + sorted-pinmap-json)
- `content_sha256 = 55090d91af40d1e194e3ba879f7c3feba407177968217c45e0b30eed8bb6b3b7` (script bytes only)
- closure (legacy single-SHA): `a48c14e6f338825a...` (over 4-input pinmap)

**Input pin SHAs (first 16 hex of each, logged in script's first 20 lines of stdout)**:
- `computations/canonical_constants.py`: `e62797b73a0b558a...`
- `sessions/framework/registry/branch-iv-canonical.md`: `af50579b521d3c64...`
- `computations/artifacts/s85_w12_elim1_D_K_Lmax_moments.npz`: `ebdeab300b4306af...`
- `computations/s85_gate_verdicts.txt`: `1993c0e6ec6aeaef...`

**Artifacts produced**:
- `computations/s86_w4_p4_branch_iv_commit.py` (verification script; 16,123 bytes; first-20-lines stdout SHA logging block; computes R_JK + xi_E_GGE_inv; runs all 5 CC; appends dual-SHA verdict line via `append_verdict` with companion comment row).
- `sessions/framework/registry/branch-iv-canonical.md` (canonical formulation document).
- `computations/canonical_constants.py` (2 NEW canonical entries at SECTION E.B + PROVENANCE dict).
- Verdict line in `computations/s86_gate_verdicts.txt` (canonical path per `.claude/rules/gate-verdicts.md`).

**Downstream unlock**: W5a P3 (`S86-SECTOR-1-SR-FLOW-Z-FACTOR`) is now **runnable**. Per partition §3 sequencing row "W4 (P4) → W5 (P3 SECTOR-1 ξ²(0) IC)": Sector-1 ξ²(0) initial condition sources from `xi_E_GGE_inv = 13.642473425595973` (M_KK units) — the registry-pinned substrate-distance-1 diagnostic. P3 can now integrate the (ε, η, α_s, ξ²) ODE from N=0 fold IC. W5a P3 dispatch should `from canonical_constants import xi_E_GGE_inv` and consume directly.

**Substrate-IS-language statement**: `R_JK` IS the K-functional moment of `D_K` at distance-2 (NOT "lives in the K-corridor"). `xi_E_GGE_inv` IS the s=−1 spectral residue moment OF the GGE-projected `D_K` (NOT "a coherence length IN a vacuum"). The GGE relic IS the substrate's residual coherence pattern post-fold; both diagnostics are functionals OF the substrate (moments of D_K), not external probes IN spacetime. 3He-B coherence-length spectroscopy is the parent→child inheritance template (per `project_3heb-inheritance.md`), NOT an analogy.

**Cross-cite (volovik-superfluid-universe-theorist)**: For ξ_E_GGE^{−1} 3He-B parent→child inheritance per `project_3heb-inheritance.md`. Cited in (a) `computations/canonical_constants.py` SECTION E.B comment block (xi_E_GGE_inv "3He-B inheritance: parent->child... NOT analogy"); (b) `sessions/framework/registry/branch-iv-canonical.md` §3 (3He-B parent→child inheritance subsection) + §4 (Provenance + cross-cite ledger row "volovik-superfluid-universe-theorist (cross-cite for xi_E_GGE_inv): 3He-B parent→child inheritance template"). Cross-cite is in-document, NOT a separate dispatch (per orchestrator override).

---

### §W4-2. S86-SECTOR-2-MELLIN-KERNEL-K-INVARIANT (lizzi-spectral-functional-theorist)

**Status**: COMPLETE
**Gate ID**: `S86-SECTOR-2-MELLIN-KERNEL-K-INVARIANT`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **GEOMETRIC** (Mellin-kernel pole structure is a property of the regulator class — the fabric itself rather than its excitations; K-invariant pin is substrate-distance-1 = first-moment Mellin residue)
**Agent**: `lizzi-spectral-functional-theorist` (primary; Mellin Strip / Convergence Cone Theorem domain) + `connes-ncg-theorist` (cross-cite for Connes-Chamseddine Mellin-multiplier infinite-vector formalism, in-script SHA-source provenance)
**Hypothesis**: Substrate Mellin-kernel pole structure at the CMB pivot is invariant across the 5-regulator atlas {ζ, Zubarev, SDW, cutoff_sqrt, anomaly} — pole locations of M[K_substrate](s) at s=3 in d_spec=8 NCG agree across atlas members within RATIO ≤ 1e-3 OR ABSOLUTE ≤ 1e-6, establishing K_substrate as substrate-distance-1 invariant (regulator-independent first-moment Mellin residue).
**Plan reference**: `sessions/session-plan/session-86-plan-w4.md` §W4-2.

**MCP Pre-Compute Audit**:
- `search_knowledge("Mellin kernel pole pivot regulator")` → 10 hits; canonical hit `mellin_heat_kernel_residue` (S85 W6 spectral-geometer) confirms s=3 → a_2 slot; helper module `_spectral_action_regulators.py` confirmed as the schematic 5-regulator atlas.
- `search_knowledge("K-invariant substrate distance-1")` → 10 hits; `R_JK(N=0)` flagged distance-2 (one-substrate-operator), `K_substrate` is Definition 1 of THIS gate (substrate-distance-1, first-moment Mellin residue).
- `trace_entity("ZETA-NOT-PHYSICAL-75")` → confirmed CLOSED (S82 W2-3 origin); the 381× dynamic range across L_max of ζ_D is the upstream theorem this gate now extends to **regulator-class** dependence at the substrate-distance-1 a_2 slot.
- `trace_entity("Mellin Strip Convergence Cone Theorem")` → no direct trace match; lives at S85 W0-S6 / W2 C9-C10 spec; treated as upstream-conceptual (Mellin-cone NOT yet live → fallback active).
- `list_constants("K_|tau_fold|M_KK")` → 29 hits; `tau_fold = 0.19` (S12/S42 CONST-FREEZE-42), `M_KK_gravity = 7.42866e+16` (S42 CONST-FREEZE-42), `Vol_SU3_Haar` imported from `canonical_constants.py`. **`tau_pivot` is NOT registered** → script uses `TAU_PIVOT = tau_fold` per plan §6 Definition 2 fallback (substrate slice for s=3 residue).
- **Mellin-cone live-vs-fallback**: `from analytic_zeta import analytic_zeta` → `ImportError` → `mellin_cone_live = False` → fallback to direct heat-kernel truncation per S85 W2-5 convention (ACTIVE).

**Verdict**:
**FAIL** — `max_pair_ratio = 9.240439e-01` (= 92.4 %) far exceeds the FAIL boundary 1e-2 across the live atlas A_5 (C28 verdict line returned `INFO: REQUIRES-S86-GATE` so atlas remains A_5). Counterexample probe `|d(pole_Zubarev)/d(eps)| / pole = 6.98` also exceeds the 1e-4 PROBE_TOLERANCE → CC-3 FAIL → verdict-mapping by §9 = FAIL.

Verdict line (S84+ canonical, dual-SHA):

```
S86-SECTOR-2-MELLIN-KERNEL-K-INVARIANT: FAIL -- value='max_pair_ratio=9.240439e-01;max_pair_abs=1.460926e-01;atlas=A_5;deviant=None' scheme=Mellin-kernel convention=substrate-distance-1 L_max=10 audit_sha256=613507429977f72a353ec0e5ad8e4bd9109e7c79ee590d922695efec83e1507e content_sha256=7bcace347d76cc0a4f0f99ca906c4aaaf8a239159b0ef938efd146f2d1dbee24 schema_version=S84+
# audit_sha256 companion row: S86-SECTOR-2-MELLIN-KERNEL-K-INVARIANT audit=613507429977f72a content=7bcace347d76cc0a
```

**Per-regulator pole values** (all on the schematic SU(3) Casimir spectrum, L_max=10, Vol_SU3_Haar = 8√3·π⁴, tau_pivot = tau_fold = 0.19):

| Regulator     | Helper       | pole_R = K_substrate(s=3, R)   |
|:--------------|:-------------|:-------------------------------|
| ζ             | zeta_a_n     | 1.581013447264e-01             |
| Zubarev       | heat-kernel  | 1.200875443266e-02             |
| SDW           | mellin_a_n   | 1.581013447264e-01             |
| cutoff_sqrt   | hard-cutoff  | 1.110026437499e-01             |
| anomaly       | Pauli-Villars| 3.184675917801e-02             |

**All-pairs deviation table** (RATIO = |pole_R − pole_R'| / max(|pole_R|, |pole_R'|); ABSOLUTE = |pole_R − pole_R'|):

| Pair                    | RATIO       | ABS         | Tolerance status                          |
|:------------------------|:------------|:------------|:------------------------------------------|
| ζ ↔ SDW                 | 0           | 0           | PASS-strict (zeta = Mellin on pos. spectrum) |
| ζ ↔ cutoff_sqrt         | 2.976e-01   | 4.710e-02   | FAIL (> 1e-2)                             |
| ζ ↔ anomaly             | 7.986e-01   | 1.263e-01   | FAIL (> 1e-2)                             |
| ζ ↔ Zubarev             | **9.240e-01** | **1.461e-01** | **FAIL (max-pair)**                       |
| Zubarev ↔ cutoff_sqrt   | 8.918e-01   | 9.899e-02   | FAIL (> 1e-2)                             |
| Zubarev ↔ anomaly       | 6.230e-01   | 1.984e-02   | FAIL (> 1e-2)                             |
| Zubarev ↔ SDW           | 9.240e-01   | 1.461e-01   | FAIL                                      |
| SDW ↔ cutoff_sqrt       | 2.976e-01   | 4.710e-02   | FAIL                                      |
| SDW ↔ anomaly           | 7.986e-01   | 1.263e-01   | FAIL                                      |
| cutoff_sqrt ↔ anomaly   | 7.131e-01   | 7.916e-02   | FAIL                                      |

Max-pair: (ζ, Zubarev) at RATIO = 9.240439e-01, ABS = 1.460926e-01.

**Counterexample probe** `|d(pole_R)/d(eps)|` at tau_pivot via central finite difference (delta_eps = 1e-4):

| Regulator     | abs deriv    | rel deriv    | Probe verdict (≤ 1e-4)            |
|:--------------|:-------------|:-------------|:----------------------------------|
| ζ             | 0.0          | 0.0          | PASS (tau-independent)            |
| Zubarev       | 8.386e-02    | 6.983e+00    | **FAIL** (heat-kernel tau-dependent) |
| SDW           | 0.0          | 0.0          | PASS (tau-independent)            |
| cutoff_sqrt   | 0.0          | 0.0          | PASS (tau-independent)            |
| anomaly       | 0.0          | 0.0          | PASS (tau-independent)            |

→ CC-3 FAIL on Zubarev alone (heat-kernel Seeley-DeWitt dressing has explicit tau-dependence by construction; the four other regulators are tau-independent at the s=3 Mellin-residue level).

**6 cross-checks**:

| CC | Test | Result | Detail |
|:---|:-----|:-------|:-------|
| CC-1 | pole_R has units of M_KK² (a_2 slot); all values finite + positive | **PASS** | All 5 pole_R > 0 and finite |
| CC-2 | ζ-entry reproduces direct ∑_(p,q)≠(0,0), p+q≤10 d(p,q)/C_2(p,q) / Vol_SU3_Haar (Connes-Chamseddine literature anchor; tol 1e-4) | **PASS** | rel_err = 1.7556e-16 (machine-epsilon match) |
| CC-3 | Counterexample probe ∂(pole_R)/∂(eps) ~ 0 within 1e-4 at all R | **FAIL** | Zubarev rel_deriv = 6.98 (heat-kernel structurally tau-dependent) |
| CC-4 | Atlas consistency with C28: A_5 because C28 = INFO/REQUIRES-S86-GATE (atlas remains A_5) | **PASS** | C28 verdict line read; atlas size = 5 |
| CC-5 | SHA-pin all input files + dual-SHA closure (audit / content) | **PASS** | audit_sha256 + content_sha256 both 64-char hex |
| CC-6 | schema_version=S84+ (R3 lift) + cutoff_axis=both stamped | **PASS** | header carries schema_version=S84+; atlas spans spectral cutoff [ζ, Zubarev, SDW] and coherence cutoff [cutoff_sqrt, anomaly] → cutoff_axis=both invoked |

**4-tuple**:
`(value="max_pair_ratio=9.240439e-01;max_pair_abs=1.460926e-01;atlas=A_5;deviant=None", scheme="Mellin-kernel", convention="substrate-distance-1", L_max=10)`

**Substitution chain (verbatim from §10 of the plan; numerically realized here)**:

```
Definition 1 (K-invariant at substrate-distance-1):
  K_substrate(s, R) := Res_{s=3} M[K(τ_pivot; R)](s)
  where M is Mellin transform, K is regulator-R-tagged heat kernel,
  s=3 is the first non-trivial Mellin residue in d_spec=8 NCG.

  Realization: For d_spec=8, M[Tr e^{-tD²}](s) has simple poles at
  s = d_spec/2 - n = 4 - n; the s=3 pole (n=1) extracts the a_2-slot
  spectral moment. In the helper convention, n=1 → a_2-like moment.
  Numerically: K_substrate(s=3, ζ) = 1.581013447264e-01 (machine-pure).

Definition 2 (5-regulator atlas):
  A_5 := {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}
  per context §1.5 W12-4 partition F_4 ∪ M.

  Realization: C28 (W4-3) lands INFO: REQUIRES-S86-GATE → atlas remains A_5.
  Mapping to helper module:
    ζ → zeta_a_n,  Zubarev → heat_kernel_a_n,  SDW → mellin_a_n,
    cutoff_sqrt → hard_cutoff_a_n,  anomaly → pauli_villars_a_n.

Step 1 (substitute):
  For each R, pole_R := K_substrate(s=3, R) computed.
  All-pairs deviation matrix populated (10 distinct off-diagonal pairs).
  Result: max_pair_ratio = 9.240439e-01 at (ζ, Zubarev).

Step 2 (substitute the invariance claim):
  Theorem: ∀ (R, R'), deviation/|pole_R| ≤ 1e-3 OR deviation ≤ 1e-6.

  Realization: theorem PREDICATE FALSE.  9 of 10 off-diagonal pairs FAIL
  the RATIO threshold; only (ζ, SDW) satisfies it (machine-epsilon match,
  consequence of zeta = Mellin on positive-definite Casimir spectrum).

Step 3 (simplify to canonical form):
  pole_R = a_2(τ_pivot) · M_R(s=3)
  where a_2(τ_pivot) is the substrate Seeley-DeWitt coefficient
  (R-independent) and M_R(s=3) is the regulator-R Mellin-multiplier
  residue at s=3.
  Therefore deviation = a_2(τ_pivot) × |M_R(s=3) − M_R'(s=3)|.
  Invariance ⇔ M_R(s=3) is R-independent at s=3.

  Realization: a_2(τ_pivot) is shared (substrate Casimir spectrum
  / Vol_SU3_Haar normalization), but M_R(s=3) is NOT R-universal:
    M_ζ(s=3)        = M_SDW(s=3)        = 1.581e-01   (F_4-class identity)
    M_Zubarev(s=3)  = 1.201e-02   (heat-kernel exp(-t·C_2) suppression)
    M_cutoff_sqrt(s=3) = 1.110e-01   (truncation at 0.7·C_max)
    M_anomaly(s=3)  = 3.185e-02   (Pauli-Villars subtraction at 0.1·C_max)
  → M_R(s=3) is R-DEPENDENT; the regulator-class Mellin multiplier at
  the s=3 substrate-distance-1 slot is NOT universal.

Step 4 (direction):
  M_R(s=3) is R-independent (PASS direction)
    ⇔ K_substrate IS a substrate-distance-1 invariant.
  M_R(s=3) is R-dependent at s=3 (FAIL direction)
    ⇔ K-invariant pin BROKEN; substrate-distance-1 tag invalid for K
       on the FULL atlas A_5.
  Conclusion: PASS direction NOT realized.  FAIL direction holds:
  the regulator-class Mellin residue at s=3 is NOT universal across
  A_5 = {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}.

  Substructure: the F_2 sub-atlas {ζ, SDW} agrees to machine epsilon
  (1.7556e-16, CC-2 PASS). The F_4-class {ζ, Zubarev, SDW} is NOT
  tight (Zubarev breaks at 92 % deviation). The K-invariant claim
  survives only on the strict zeta=Mellin equivalence sub-atlas — a
  trivial structural identity, not a substantive substrate-distance-1
  invariant across the live atlas.
```

**Atlas live-state**: `A_5` (C28 = INFO: REQUIRES-S86-GATE → no STRUCTURALLY-EXCLUDED contraction; atlas remains 5-member). C28 verdict line read at runtime via `check_c28_atlas_state()`.

**Mellin-cone live-vs-fallback flag**: `mellin_cone_live = False` (W2 C9/C10 not yet landed; `from analytic_zeta import analytic_zeta` → `ImportError`) → script falls back to **direct heat-kernel truncation** per S85 W2-5 convention. The fallback path uses the `_spectral_action_regulators.py` helper module's deterministic schematic regulators (zeta_a_n, mellin_a_n, heat_kernel_a_n, hard_cutoff_a_n, pauli_villars_a_n) on the SU(3) Casimir spectrum at L_max=10.

**GPU path**: `gpu_available = True` (torch.cuda + ROCm RX 9070 XT detected). The `gpu_mellin_plancherel_check()` routine exercises the `torch.fft.fft` Mellin-Plancherel sanity path on each pole_R value (single-mode FFT, DC component verification); GPU path returned successful for all 5 atlas members — note in `.npz` payload `gpu_available=True`.

**Dual-SHA**:
- `audit_sha256 = 613507429977f72a353ec0e5ad8e4bd9109e7c79ee590d922695efec83e1507e` (script + canonical_constants.py + pinmap_json)
- `content_sha256 = 7bcace347d76cc0a4f0f99ca906c4aaaf8a239159b0ef938efd146f2d1dbee24` (script bytes only)

Closure SHAs computed at runtime from the input-pin map (NOT hardcoded); per `_closure_hash`-equivalent logic in script Section 4 (`compute_dual_sha`).

**Artifacts**:
- `computations/s86_w4_p5_sector_2_k_invariant.py` (35,894 bytes — full script with substitution chain in docstring, 6 CC, GPU path, counterexample probe, dual-SHA emit)
- `computations/s86_w4_p5_sector_2_k_invariant.npz` (10,829 bytes — poles dict, all-pairs deviations, ∂(pole_R)/∂ε array, atlas membership state, mellin_cone_live flag, gpu_available flag, all CC results, all thresholds)
- `computations/s86_w4_p5_sector_2_k_invariant.png` (114,467 bytes — left panel: pole_R values across A_5 with annotations; right panel: log10(rel_deviation) all-pair matrix with PASS/FAIL threshold lines on colorbar)

**What FAIL means for solution space** (per plan §11 FAIL clause):

The substrate-distance-1 invariance is **BROKEN** on the full live atlas A_5; the K-invariant pin is REJECTED. SECTOR-2 cannot be canonicalized as a single substrate-distance tag — it must be split into per-regulator distance tags (SECTOR-2-ζ, SECTOR-2-Zubarev, SECTOR-2-SDW, SECTOR-2-cutoff_sqrt, SECTOR-2-anomaly) at the registry level. The F_2 zeta=SDW sub-atlas is the ONLY tight-pair survivor; this is a structural identity (zeta = Mellin on positive-definite spectrum) and does not lift the K-invariance claim to even the F_4 = {ζ, Zubarev, SDW} sub-atlas (Zubarev breaks at 92 %).

Cascade: this cascades to W6 (perturbative-immunization corollaries C-α/β/γ, which assume regulator-class universality at distance-1 — must now be re-evaluated under per-regulator splitting) and to W5a P3 SR-flow Z-factor (whose IC sources from substrate-distance-1 quantities — if K-invariance fails, P3's IC inherits per-regulator splitting). Constraint-map gain: the SECTOR-split is **finer than 2A predicted** — a new corridor of regulator-specific substrate-distance taxonomy opens. Per Lizzi methodology (`feedback_reporting-framing.md` + `feedback_reporting-framing.md` style): FAIL is a structural finding — the regulator-class Mellin-multiplier at s=3 is the **observable** that breaks substrate-distance-1 universality, and the structural reason is that {Zubarev, cutoff_sqrt, anomaly} each introduce regulator-specific scales (t_ref for heat-kernel, cutoff_frac for hard-cutoff, M_PV² for Pauli-Villars) that are not absorbed into the a_2 common factor.

**Substrate-framing reminder** (`.claude/rules/phononic-framing.md` §IS Space, Not IN Space):
The Mellin-kernel pole at s=3 IS a moment of how the substrate's spectral content is summed under each regulator class. The K-invariance hypothesis was that this moment is intrinsic to D_K, not to the regulator. The FAIL outcome IS a property of the substrate's regulator-class structure: at the s=3 Mellin-residue level, the substrate's spectral-action functional carries regulator-specific weight that does NOT reduce to a single a_2 factor across A_5. The result IS that K_substrate at substrate-distance-1 is regulator-class-dependent on the live atlas — NOT that "K_substrate fails to be cutoff-independent in regulator space" (container framing). The substrate IS the regulator-class manifold; the regulators ARE prescriptions for summing the substrate's spectral content; the breakdown IS structural.

**Cross-cite (Connes-Chamseddine 1996)**: At s=3 in d_spec=8 NCG, the Mellin-multiplier formalism (Connes-Chamseddine 1996 §2.2-2.3, on f_0 / f_2 / f_4 Mellin moments of the cutoff function f) defines the regulator-class via the Mellin-Barnes transform of f restricted to [0, ∞). The schematic helper realizes pure-spectrum analogs of these multipliers: {zeta, Mellin} ↔ analytic continuation (no f-cutoff); heat-kernel ↔ exp(-tC_2) Schwinger time integration; hard-cutoff ↔ sharp f truncation; Pauli-Villars ↔ massive-regulator subtraction. These are NOT the full physical regularizations of Connes-Chamseddine 1996; they are the schematic 5-regulator atlas members per `_spectral_action_regulators.py` docstring. The FAIL of K-invariance on A_5 establishes that even the schematic Mellin-multipliers at s=3 are NOT R-universal.

**Cross-cite to S86 W7 deliverables (T8-17 + T8-19 install, READY-TO-INSTALL per S86 W7 WP-1 + WP-3, applied 2026-04-27)**: The "permanently repair S78-onward conflation" mandate of this §W4-2 PASS-criterion language (line 290 "BROKEN" disposition + line 483 "permanently repaired" assessment + line 511 "permanently repairs" structural-deliverable language) is now structurally fulfilled by the S86 W7 deliverable triple:
- **(b) Backward-closure (audit-output OUTLINE)**: `sessions/framework/registry/layer1-layer2-retroactive-audit.md` (S86 W7 deliverable (b)) — full enumeration outline for retroactive audit of S78-onward records under the LAYER 1 (combinatorial-position-on-atlas) vs LAYER 2 (axiomatic-admissibility) taxonomy.
- **(c) Forward-closure (registry entry)**: `sessions/permanent-results-registry.md` §VII-B.ZETA-EQUALS-SDW (S86 W7 deliverable (c)) — registry-canonical landing of the zeta = SDW Mellin-support identity that anchors the F_2 tight-pair survivor of this §W4-2 FAIL.
- **(a) Methodology lock**: the W7 workshop's Conflation 3 remediation language (registry §VII-B.HP1-NEAR-INVARIANCE provenance text re-worded per W7 WP-2) closes the LAYER-1-vs-LAYER-2 conflation pattern that this §W4-2 FAIL first surfaced.

Future readers of §W4-2 should navigate to (b) for the audit-trail across S78+ records and to (c) for the substrate-canonical identity that makes the F_2 partition principled. The §W4-2 → S86 W7 reference loop is now closed at the registry level.

---

### §W4-3. S86-W-4-CUTOFF-SQRT-ADJUDICATION (connes-ncg-theorist)

**Status**: COMPLETE
**Gate ID**: `S86-W-4-CUTOFF-SQRT-ADJUDICATION`
**Trigger**: `[AUDIT]`
**Classification**: **META** (registry-canonical adjudication of S85 workshop convergence; outcome cascades to atlas cardinality and C45 S87 deferral state)
**Agent**: `connes-ncg-theorist` (primary, R3 closer of S85 workshop) + `lizzi-spectral-functional-theorist` (cross-cite for R2 emergence E1-L/E2-L/E3-L + 3-gate joint refinement)
**Hypothesis**: S85 W4 cutoff_sqrt-status workshop converged on REQUIRES-S86-GATE (joint 3-gate adjudication = GATE A L_max-finiteness ∧ GATE B kernel-admissibility ∧ GATE C S82-applicability), with both connes R3 ACCEPTED-IN-FULL and lizzi R2 E1-L endorsements unretracted; C28 lands the verdict + apparatus into `sessions/framework/registry/cutoff-sqrt-adjudication.md` and pre-registers GATES A/B/C as S86+ items.
**Plan reference**: `sessions/session-plan/session-86-plan-w4.md` §W4-3.

**MCP Pre-Compute Audit** (executed 2026-04-26 prior to script dispatch; one-line salient return per query per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge("cutoff_sqrt regulator atlas STRUCTURALLY-EXCLUDED")` → 20 hits; confirms 5-regulator atlas `R_atlas = {zeta, Zubarev, SDW, cutoff_sqrt, anomaly}` with cutoff_sqrt currently PENDING-EVENT; the plan-text outcome enum `{STRUCTURALLY-EXCLUDED → PASS atlas A_4, GENUINELY-PHYSICAL → PASS atlas A_5, REQUIRES-S86-GATE → INFO atlas A_5 PENDING}` is indexed and matches the §W4-3 §9 threshold table.
- `search_knowledge("cutoff_AL2010 kernel admissibility")` → cutoff_AL2010 admissibility status is **OPEN** at S85 close (heat-kernel admissibility entries `s84_w7b_81_mp_admissibility_extended.py` finite at s_KO=6 for `exp(-x)` heat-kernel but cutoff_AL2010 not yet certified); S85 W4 workshop's 3-gate refinement is the converged adjudication apparatus; cutoff_AL2010 sits at L3 / L4 of the broadened CM-2008 §1.143 stratification.
- `trace_entity("ZETA-NOT-PHYSICAL-75")` → registry §VII-B.ZETA-NOT-PHYSICAL-75 (Lizzi-track, S75 W3 / S86 W1b T5fix) — strict-axiomatic-exclusion endpoint `R_1 = {zeta}` per D3-sharp; LANDED.
- `trace_entity("Regulator-Family Boundary Theorem")` → connes-formulation `Phi_r(nu_i) = M(r) · Phi_zeta(nu_i)` (II.7); 5-regulator factorization on HP^0 spread. Cutoff_sqrt (with 254.75% spread) sits in the M-bucket NOT in the P-bucket (zeta, Zubarev, SDW with 0% spread).
- `list_entities("closed")` → 100 closed mechanisms surveyed; no closure of "cutoff_sqrt physical" in either direction; the C28 verdict therefore lands in the 3-element pre-registered enum without prior precedent constraining the outcome.

**Confirmed pre-condition for §W4-3 dispatch**: (a) cutoff_AL2010 admissibility is OPEN at S85 close; (b) the 3-gate refinement is the converged adjudication apparatus; (c) C45 S87 SIXTH-REGULATOR-SYNTHESIS is conditional on C28 outcome (per partition §2 deferral row). All three confirmed.

**Verdict**: **INFO** with classification **REQUIRES-S86-GATE** (atlas-cardinality cascade `A_5 PENDING`; 3 GATES A+B+C pre-registered).

**4-tuple**: `(value="REQUIRES-S86-GATE", scheme="connes-lizzi-workshop", convention="3-round-closeout", L_max="N/A")`

**Input-pin SHA-256 map (frozen at runtime)**:

| Pin | Value |
|:----|:------|
| workshop file | `sessions/archive/session-85/workshops/s85-w4-cutoff-sqrt-status.md` |
| workshop content_sha256 | `381ec66bd3b6a17a0791cdd045c644c54a8ce2c5e747129f622a823bd3377521` |
| registry file | `sessions/permanent-results-registry.md` |
| registry content_sha256 | `66097c26676f17b0ea7ee02a21cf4974b372bf9389d4cda6aa2f69c3c85e404a` |
| framework file (output) | `sessions/framework/registry/cutoff-sqrt-adjudication.md` |
| framework content_sha256 | `afd0d440dff69c0a4e1e87456525a4725de9af0e7ca7eb806aaa13fe74376af2` |
| script | `computations/s86_w4_c28_cutoff_sqrt_adjudication.py` |
| schema_version | `R3` |
| cutoff_axis | `coherence` |

**Verbatim convergence quotes (workshop_sha = `381ec66b…`)**:

- **R2 lizzi EMERGENCE E1-L (line 1153)** — verbatim:

  > **E1-L: REQUIRES-S86-GATE is the converged W4 verdict, with the technical landscape now sharply asymmetric.**

- **R2 lizzi EMERGENCE E2-L (lines 1056–1065)** — 3-gate refined joint outcome rule (verbatim):

  > Joint outcome rule (refined L_lizzi):
  >    GATE A FAIL                  ->  STRUCTURALLY-EXCLUDED        (regardless of GATE B)
  >    GATE A PASS  AND  GATE B PASS ->  GENUINELY-PHYSICAL
  >    GATE A PASS  AND  GATE B FAIL ->  REQUIRES-S87-GATE on inner-fluctuation lift
  >    GATE A PASS  AND  GATE B INFO ->  GENUINELY-PHYSICAL conditional on GATE C HBW-tail
  >
  > Under this refinement, **GATE A is the MASTER gate** (the L_max-divergence test must
  > PASS for the substrate-volume defense to even be admissible to the load-bearing audit).

- **R2 lizzi EMERGENCE E3-L (lines 1255–1269)** — combinatorial vs admissibility taxonomy (verbatim):

  > LAYER 1 (combinatorial-position-on-atlas):  determined by Mellin support and observable-cross-classification;
  >                                              cutoff_AL2010 has a unique privileged slot.
  > LAYER 2 (admissibility-on-axioms):           determined by GATE A + GATE B + GATE C numerical tests;
  >                                              cutoff_AL2010 expected to FAIL GATE A.
  >
  > The two layers are INDEPENDENT structural properties.
  > A regulator can be combinatorially privileged but axiomatically excluded.
  > A regulator can be combinatorially generic but axiomatically admissible.
  > The W5 evidence pertains to LAYER 1 (partition theorem on observable space).
  > The W4 verdict pertains to LAYER 2 (admissibility on axiom space).

- **R3 connes CONVERGENCE (c) (line 1329)** — verbatim:

  > **(c) E1-L: REQUIRES-S86-GATE as the workshop's converged W4 verdict: ACCEPTED IN FULL.** This is the right outcome. The CC-2010 citation correction (R2-A-CONV-a) and the Sage-verified L_max scaling (R2-B-D1-collapse) together mean the GENUINELY-PHYSICAL steelman has retreated to a modified-coupling Q6-C reframe that lizzi explicitly does NOT defend in this workshop, and the STRUCTURALLY-EXCLUDED steelman has retreated from kernel-admissibility (S82 W2-5 reg-violation, retracted) to L_max-finiteness (D1, expected to FAIL pure cutoff_AL2010). Neither steelman closes definitively in this workshop; both name a sharp pre-registered numerical question whose outcome decides the contest. REQUIRES-S86-GATE is what the structural state of the question demands.

- **R3 connes CONVERGENCE (e) (line ~1361)** — master-gate ACCEPTANCE (verbatim, summarized): "GATE A as gating-master refinement: ACCEPTED IN FULL." The dependency-chain `GATE A -> {GATE B, GATE C}` is the right structure.

- **R3 lizzi CONVERGENCE R3-C-CONV-3 (line 1606)** — ratification (verbatim, leading sentence):

  > **R3-C-CONV-3 / E1-L REQUIRES-S86-GATE accepted (R3-A label: R3-C-CONV-(c)): ACCEPTED IN FULL.** R3-A reads E1-L exactly as I intended: REQUIRES-S86-GATE because (i) the CC-2010 citation correction retracts connes's R1 kernel-admissibility attack vector, (ii) the Sage-verified L_max scaling correction collapses my L2 substrate-volume defense, and (iii) neither steelman closes definitively in this workshop.

**Substitution chain (per `.claude/rules/math-scripts.md` §Double-Check Logic Before Compute)**:

```
Definition (workshop-converged outcome):
  workshop-converged outcome := the verdict that BOTH connes R3 and lizzi R2
                                 endorse without retraction.

Substitution (from workshop file s85-w4-cutoff-sqrt-status.md, sha256 prefix 381ec66b...):
  lizzi R2 E1-L (line 1153):
    "REQUIRES-S86-GATE is the converged W4 verdict, with the technical
     landscape now sharply asymmetric."
  connes R3 (c) (line 1329):
    "(c) E1-L: REQUIRES-S86-GATE as the workshop's converged W4 verdict:
     ACCEPTED IN FULL."
  lizzi R3 CONVERGENCE R3-C-CONV-3 (line 1606):
    "R3-C-CONV-3 / E1-L REQUIRES-S86-GATE accepted ... ACCEPTED IN FULL."

Simplify:
  BOTH agents endorsed REQUIRES-S86-GATE; lizzi R3 ratification confirms no
  retraction post-R2. STRUCTURALLY-EXCLUDED steelman retreated from kernel-
  admissibility (S82 W2-5 reg-violation, retracted under R2-A-CONV-(a)) to
  L_max-finiteness (D1, expected to FAIL pure cutoff_AL2010); GENUINELY-PHYSICAL
  steelman retreated to modified-coupling Q6-C reframe lizzi did NOT defend in R2.
  Neither steelman closes definitively in the workshop.

Direction:
  Verdict classification = REQUIRES-S86-GATE.
  C28 outcome = INFO (per threshold table; REQUIRES-S86-GATE -> INFO).
  Atlas cardinality cascade = A_5 PENDING with cutoff_sqrt PENDING-EVENT
                              status; 3 GATES A + B + C pre-registered for
                              S86+ dispatch.
  Conclusion: C28 lands INFO with REQUIRES-S86-GATE classification.
```

**3-pre-registered-outcome enum and selected outcome**:

| Outcome | Verdict | Atlas state | Selected? |
|:--|:--|:--|:--|
| `STRUCTURALLY-EXCLUDED` | PASS | A_5 → A_4 collapse (cutoff_sqrt removed) | NO — would require GATE A to dispatch and FAIL |
| `GENUINELY-PHYSICAL` | PASS | A_5 retained, cutoff_sqrt promoted to canonical | NO — RULED OUT at S85 close (modified-coupling Q6-C reframe required to revive; lizzi did not defend in R2) |
| **`REQUIRES-S86-GATE`** | **INFO** | **A_5 PENDING with cutoff_sqrt PENDING-EVENT** | **YES (selected per substitution chain above)** |

**3-gate pre-registration summaries (PRDR-grade; S86+ wave-planners can dispatch without re-deriving)**:

- **GATE A — `S86-CUTOFF-SQRT-GATE-A-LMAX-FINITENESS` (master)**: Test whether `f_0 · Λ(L_max)^4 · a_0(L_max)` admits a positive-α scaling Λ(L_max) = Λ_0 · L_max^α (α ∈ [−2, +2]) such that the coupling is bounded as L_max → ∞ on Jensen-deformed SU(3). Inputs pinned: a_0(L_max) Peter-Weyl L^2(SU(3)) sum-of-dim^2 multiplicity (leading L_max^8/960; discrete anchors a_0(3)=12880, a_0(4)=50176, …, a_0(10)=9785776); cutoff_AL2010 Mellin vector `(1/2, 1, 1, 0)` published or `(2, 1, 0.5, 0.1)` framework-truncated. **PASS**: ∃α ≥ 0 with bounded limit. **FAIL** (pre-registered, expected per R3-C-E3-C structural pre-determination: α = −k_eff/4 < 0): all bounded α < 0. **INFO**: subleading polynomial corrections non-canonical. Machinery pin: scheme `peter-weyl-sum-of-dim2`, convention `cutoff_AL2010-canonical`, L_max ∈ {3,5,7,10}, GPU=NONE, cutoff_axis=`coherence`, schema_version=`R3`. (Full block in framework file §3.1.)

- **GATE B — `S86-CUTOFF-SQRT-GATE-B-KERNEL-ADMISSIBILITY` (conditional refinement)**: Audit which CCM-2007 axioms source the a_0 slot under cutoff_AL2010 vs zeta — does the load-bearing set reduce to {dim, fin}, or require {reg, 1st-order}? Inputs pinned: CCM-2007 axiom set {dim, reg, fin, real, 1st-order, orient, PD}; subset-removal protocol = W2-1 applied to a_0 slot. **PASS**: load-bearing set = {dim, fin}. **FAIL**: requires {reg} or {1st-order} (inner-fluctuation lift). **INFO**: KO-dim grading or J-action dependence. Necessary-but-not-sufficient: GATE A still required for Λ^4 routing (per R2 lizzi E2-L). Machinery pin: scheme `subset-removal-sweep`, convention `W2-1-protocol-on-a0-slot`, L_max=7, GPU=NONE. (Full block in framework file §3.2.)

- **GATE C — `S86-CUTOFF-SQRT-GATE-C-S82-APPLICABILITY` (residual)**: HBW / MP-abs-conv at s=6 of the framework's L_max=3 truncation residue f_6 = 0.1 specifically (NOT the unregulated kernel — that was retracted under R2-A-CONV-(a) citation correction). Inputs pinned: framework Mellin vector `(2, 1, 0.5, 0.1)`, the f_6 = 0.1 residue, reconstruction of f_residue(u) at the f_6 slot. Method: M[f_residue](6) = ∫_0^∞ u^5 · f_residue(u) du test against HBW positive cone. **PASS**: abs-convergent + positive (in HBW positive cone). **FAIL**: diverges or oscillatory-non-positive. **INFO**: convergent but outside HBW positive cone. Machinery pin: scheme `MP-abs-conv-s6`, convention `f_6=0.1-residue`, L_max=3, GPU=NONE. (Full block in framework file §3.3.)

**Joint outcome rule (refined L_lizzi master-gate, R3-C-CONV-5 binding; framework file §3.4)**:

```
GATE A FAIL                    →  STRUCTURALLY-EXCLUDED         (regardless of GATE B, C)
GATE A PASS  AND  GATE B PASS  →  GENUINELY-PHYSICAL
GATE A PASS  AND  GATE B FAIL  →  REQUIRES-S87-GATE on inner-fluctuation lift
GATE A PASS  AND  GATE B INFO  →  GENUINELY-PHYSICAL conditional on GATE C HBW-tail
```

GATE A is the structural MASTER. Per R3-C-E3-C, GATE A FAIL is structurally pre-determined by the substrate's Peter-Weyl L^8 mode-count growth at d=8 spectral dimension; α = −k_eff/4 < 0 for every k_eff ∈ [5.09, 8] (sum-of-dim regime through asymptotic). The S86 GATE A dispatch is therefore canonical-record (logging the FAIL with input-pin closure-hash for the permanent registry), not adjudication.

**Atlas-cardinality cascade matrix**:

| Joint outcome (post-S86 GATES A+B+C) | Atlas state | Cardinality |
|:--|:--|:--|
| GENUINELY-PHYSICAL (A PASS ∧ B PASS) | A_5 retained; cutoff_sqrt promoted to canonical 2nd physical sub-family (TWO-CLASS THEOREM) | 5 |
| STRUCTURALLY-EXCLUDED (A FAIL) | A_5 collapses to A_4 = `{ζ, Zubarev, SDW, anomaly}`; cutoff_sqrt removed | 4 |
| **REQUIRES-S86-GATE (current C28 verdict)** | **A_5 PENDING with `cutoff_sqrt` PENDING-EVENT until GATES A+B+C dispatch** | **5 (PENDING)** |

**Currently-occupied cell**: row 3 (REQUIRES-S86-GATE / A_5 PENDING). The atlas remains at 5 members with cutoff_sqrt's canonical status awaiting S86+ dispatch of GATES A, B, and C.

**C45 S87-deferral confirmation**: per partition §2 (deferral row) of `sessions/session-plan/session-86-plan-w4.md`, C45 `S86-SIXTH-REGULATOR-SYNTHESIS` is conditional on C28's outcome and DEFERRED to S87. The C28 verdict REQUIRES-S86-GATE keeps the atlas at A_5 PENDING; C45's eventual dispatch awaits the resolution of GATES A+B+C. **C45 is NOT dispatched in S86. Confirmed.**

**5 cross-checks (executed by script; all PASS)**:

| CC | Description | Result |
|:--|:--|:--|
| CC-1 | workshop file SHA matches load-time pin (re-hash equality) | PASS |
| CC-2 | classification ∈ `{STRUCTURALLY-EXCLUDED, GENUINELY-PHYSICAL, REQUIRES-S86-GATE}` (no other value permitted) | PASS |
| CC-3 | framework file contains selected verdict + all 3 GATE pre-registrations (`S86-CUTOFF-SQRT-GATE-{A,B,C}-*`) | PASS |
| CC-4 | framework file contains "Atlas-cardinality cascade" with all three per-outcome rows (A_5 retained / A_5→A_4 collapse / A_5 PENDING) | PASS |
| CC-5 | cross-cite to W0b R8 PRR three-layer adjudication methodology entry present (LAYER 1 / LAYER 2 vocabulary inherited from R3-C-E3-L taxonomy) | PASS |

**Substrate-framing audit (per `.claude/rules/phononic-framing.md`)**: the regulator atlas IS the set of admissible Mellin-summation prescriptions on the substrate's spectral content `{λ_k}` of D_K on Jensen-deformed SU(3); it is NOT a list of cutoffs imposed on substrate space. The 3 GATES are tests OF the cutoff_AL2010 prescription's structural admissibility within Connes-Chamseddine 2010 axioms — NOT tests of an external cutoff scale IN the substrate. Cross-cite: Mellin Strip / Convergence Cone Theorem (T5, W1b); Regulator-Family Boundary Theorem (lizzi S-1); NCG-Structural-Exclusion META-THEOREM (W11-3 + T2; registry §VII.R).

**Dual-SHA closure**:

- `content_sha256` = `afd0d440dff69c0a4e1e87456525a4725de9af0e7ca7eb806aaa13fe74376af2` (SHA-256 of the framework file content)
- `audit_sha256`   = `5ce75a473291fd5ee46542e72a4a8f9a6b582bb5cb475d218e5504b3e8acc02a` (closure hash of the canonical input-pin map; computed at runtime per `.claude/rules/v3-closure-recovery.md` sig_5 — **NOT hardcoded**)

**Verdict line in `computations/s86_gate_verdicts.txt`** (canonical + companion row):

```
S86-W-4-CUTOFF-SQRT-ADJUDICATION: INFO -- value=REQUIRES-S86-GATE scheme=connes-lizzi-workshop convention=3-round-closeout L_max=N/A audit_sha256=5ce75a473291fd5ee46542e72a4a8f9a6b582bb5cb475d218e5504b3e8acc02a content_sha256=afd0d440dff69c0a4e1e87456525a4725de9af0e7ca7eb806aaa13fe74376af2 schema_version=S86+
# audit_sha256 companion row: S86-W-4-CUTOFF-SQRT-ADJUDICATION audit=5ce75a473291fd5e content=afd0d440dff69c0a outcome_enum={STRUCTURALLY-EXCLUDED:PASS, GENUINELY-PHYSICAL:PASS, REQUIRES-S86-GATE:INFO} workshop_lines={R2-E1-L:1153, R3-connes-(c):1329, R3-lizzi-CONV-3:1606} atlas_cascade=A_5_PENDING gates_pre_registered=3
```

**Artifacts produced**:

| Artifact | Path | SHA-256 / Notes |
|:--|:--|:--|
| Script | `computations/s86_w4_c28_cutoff_sqrt_adjudication.py` | parse + classify + write; first-20-lines stdout SHA logging block; 5 CC; closure hash computed deterministically |
| Framework adjudication file (NEW) | `sessions/framework/registry/cutoff-sqrt-adjudication.md` | content_sha256 = `afd0d440dff69c0a…` ; 369 lines; 6 sections (§1 workshop convergence; §2 verdict classification; §3 3-gate apparatus with §3.1/§3.2/§3.3/§3.4; §4 atlas-cardinality cascade; §5 downstream cascade; §6 provenance ledger) |
| Verdict line + companion row | `computations/s86_gate_verdicts.txt` | dual-SHA pinned; INFO/REQUIRES-S86-GATE |

**Solution-space interpretation**: the C28 INFO verdict converts the S85 W4 workshop's converged refusal-to-commit into a registry-canonical adjudication record with three numerical S86+ gates pre-registered at PRDR-grade. The framework's regulator-atlas methodology is upgraded by the LAYER 1 (combinatorial) vs LAYER 2 (axiomatic-admissibility) taxonomy: the previous S78-onward conflation (treating the canonical 5-atlas as uniform-admissible) is permanently repaired. The constraint-map gain is **structural deferral with explicit numerical pre-registration**: future S86+ waves dispatch GATES A + B + C with full machinery pins; no information loss; the W4 verdict is binding on the form of the future contest, not on its outcome.

---

## Wave W4 Synthesis (team-lead)

**Date**: 2026-04-26. **Gates**: 3 (W4-1 P4 PASS, W4-2 P5 FAIL, W4-3 C28 INFO). **Dispatched**: single sub-wave, 3 specialists in parallel (`transit-dynamics-theorist`, `lizzi-spectral-functional-theorist`, `connes-ncg-theorist`); all 3 independent at compute time per plan §0.5; concurrency well within the 8-agent self-imposed cap. All artifacts on disk; verdict file carries 4 distinct verdict lines (lines 106–112 of `computations/s86_gate_verdicts.txt`) with full 64-char dual-SHA closures + companion comment rows.

### 1. P4 BRANCH-IV path-(c) commit canonicalized — registry-canonical replacement of R_JE

W4-1 retires R_JE (single-distance-tag) and lands two distance-tagged spectral diagnostics: `R_JK = 0.00803460529503449` (K-functional, distance-2, M_KK^{−2} units, Newton-constant slot) and `xi_E_GGE_inv = 13.642473425595973` (s = −1 spectral residue moment of the GGE-projected D_K, distance-1, M_KK^{+1} units, M_KK-natural). Both entries registered at full float64 precision in `computations/canonical_constants.py` SECTION E.B with 7-field PROVENANCE rows; `sessions/framework/registry/branch-iv-canonical.md` created with 4 substantive sections + S86 P4 commit audit-trail. Five CC PASS: CC-1 dimensional rescaling under M_KK → 2·M_KK gives ratio 0.25 exact (machine-epsilon, M_KK^{−2}), CC-2 gives ratio 2.0 exact (M_KK^{+1}); CC-3/CC-4 grep audits PASS; CC-5 re-import at full float64 succeeds. Stage-4 loaded-vs-anchor consistency holds at rel_tol=1e-12.

**Audit trail — dual verdict on disk (lines 110 FAIL, 112 PASS)**: the line-110 FAIL was a publication-precision-floor mismatch — initial canonical entry registered at presentation precision (rounded), Stage-4 anchor consistency at rel_tol=1e-12 surfaced rel_diff > 0 against the full-float64 freshly-computed anchor. The fix prescribed by `.claude/rules/epistemic-discipline.md` §"Publication-Precision Pre-Registration (S86 W1c-8 follow-up surface)" — re-pin canonical at full float64; formula unchanged; threshold unchanged; convention unchanged — produced the line-112 PASS at machine-epsilon. Both verdict lines retained per `.claude/rules/output-standards.md` §"Gate verdicts are permanent". The dual-line structure is honest application of the W1c-8 precedent, not iterate-until-PASS (PROHIBITED_ACTIONS Class 2 audit: value/scheme/convention/L_max identical across both lines; only canonical-pin precision changed). **W1c-8 thus has a second independent witness in S86; the underlying plan-time gap (publication precision unpinned in plan §W4-1 STEP 3) is now structural carry-forward.**

> **T8-27 install (S86 W-9 WP-3 BRANCH-IV PASS scope annotation, READY-TO-INSTALL per workshop §L3 Route (i) discussion lines 312-313 + Workshop Verdict row 7 line 2292, applied 2026-04-27)**:
> The W4 P4 BRANCH-IV PASS recorded above is canonically scoped as **"registry-pin commit only; not an A_s producer; consumed by F_2-class downstream gates"**. The PASS commits R_JK and xi_E_GGE_inv to the canonical-constants registry as distance-tagged spectral diagnostics (R_JK distance-2 / xi_E_GGE_inv distance-1) replacing the conflated R_JE single-distance-tag — it does NOT itself produce an A_s value. The downstream F_2-class gates that CONSUME the BRANCH-IV registry pins are: W5a §W5a-1 SECTOR-1 SR-LO Z-factor (consumed xi_E_GGE_inv directly via `from canonical_constants import xi_E_GGE_inv` per the §"Downstream implications" table below; FAILed at both pivots — DOUBLE FAIL recorded in `session-86-w5a-workingpaper.md` §W5a-1, retired as per-class IC-compatibility DIAGNOSTIC per S86 W-9 reorganization Clause C1) and W4-2 SECTOR-2 K-invariant (consumed BRANCH-IV registry as the substrate-distance-1 anchor; FAILed at max_pair_ratio = 0.924 per §W4-2 above, retired as DIAGNOSTIC per W-9 Clause C2). After the W-9 4-clause reorganization, the canonical path-(c) A_s producer is route (iii) UNIFIED-AS-79 Branch-A zeta-normalization (S82 W1-2 verdict line 728, A_s = 3.299e-9, PASS-F2 with Δ_OOM = +0.1962); BRANCH-IV's role is restricted to providing distance-tagged spectral-diagnostic pins for the F_2-class downstream chain, NOT to producing an A_s prediction directly. Cross-cite to S86 W-9 reorganization annotation in `session-86-w5a-workingpaper.md` §W5a-1 (T8-25 install).

### 2. P5 K-invariant rejected on full atlas A_5 — SECTOR-2 must split per-regulator

W4-2 verifies the substrate Mellin-kernel pole at s = 3 in d_spec = 8 NCG across the live 5-regulator atlas A_5 = {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}. The substitution-chain Step 3 decomposed pole_R = a_2(τ_pivot) · M_R(s=3); the K-invariance hypothesis predicted M_R(s=3) regulator-independent. The numerical scan returns: M_ζ = M_SDW = 1.581e-01, M_Zubarev = 1.201e-02, M_cutoff_sqrt = 1.110e-01, M_anomaly = 3.185e-02 — max_pair_ratio = 9.240e-01 at (ζ, Zubarev), three orders of magnitude above the PASS threshold 1e-3 and two orders above the FAIL boundary 1e-2. CC-3 counterexample probe ∂(pole_R)/∂ε at τ_pivot also FAILs on Zubarev (rel_deriv = 6.98 vs 1e-4 tolerance), confirming the heat-kernel regulator carries explicit τ-dependence at the s=3 residue level by construction. CC-2 PASSes at machine-epsilon (rel_err = 1.7556e-16) — but this is the structural identity ζ = Mellin on positive-definite Casimir spectra, not evidence for K-invariance.

The constraint-map update is structural: **SECTOR-2 cannot be canonicalized as a single substrate-distance tag on the live atlas**. The K-invariant pin is REJECTED; SECTOR-2 must split into per-regulator distance tags (SECTOR-2-ζ, SECTOR-2-Zubarev, SECTOR-2-SDW, SECTOR-2-cutoff_sqrt, SECTOR-2-anomaly) at the registry level. The F_2 sub-atlas {ζ, SDW} survives (machine-epsilon, but trivially); the F_4 {ζ, Zubarev, SDW} sub-atlas does NOT cohere because Zubarev introduces a regulator-specific Schwinger time scale t_ref that does not absorb into the a_2 common factor. Mellin-cone live status: `mellin_cone_live = False` (W2 C9/C10 not landed); script ran the S85 W2-5 direct-heat-kernel-truncation fallback. A live-Mellin-cone re-run is the obvious sub-wave audit; it would not change the structural finding (Zubarev's τ-dependence is the dominant violator and is regulator-class, not infrastructure-dependent).

**Honesty disclosure** (P5 agent flagged): the `_spectral_action_regulators.py` helpers are SCHEMATIC analogs of Connes-Chamseddine 1996 §2.2-2.3 multipliers, not the full physical regularizations. The K-invariance breakdown holds for these schematic forms; a live-physical-regularization re-run is a separate question.

### 3. C28 cutoff_sqrt adjudication captured — atlas A_5 PENDING with 3-gate apparatus pre-registered

W4-3 captures the S85 W4 connes × lizzi 3-round workshop convergence as a registry-canonical adjudication record. The selected outcome is **REQUIRES-S86-GATE** (substitution-chain direction-read from workshop file `381ec66b…` lines 1153 [lizzi R2 E1-L], 1329 [connes R3 (c) ACCEPTED-IN-FULL], 1606 [lizzi R3 R3-C-CONV-3 ratification]). Both connes R3 and lizzi R2/R3 endorse without retraction; the GENUINELY-PHYSICAL steelman retreated to the modified-coupling Q6-C reframe lizzi did NOT defend in R2; the STRUCTURALLY-EXCLUDED steelman retreated from kernel-admissibility (S82 W2-5 reg-violation, retracted under R2-A-CONV-(a)) to L_max-finiteness (D1, expected to FAIL pure cutoff_AL2010). Neither steelman closed in the workshop.

C28 lands the verdict in `sessions/framework/registry/cutoff-sqrt-adjudication.md` (369 lines, 6 sections) with 3 PRDR-grade S86+ gate pre-registrations: GATE A `S86-CUTOFF-SQRT-GATE-A-LMAX-FINITENESS` (master; tests Λ(L_max)^4 · a_0(L_max) bounded; expected FAIL per R3-C-E3-C structural pre-determination — α = −k_eff/4 < 0 for every k_eff ∈ [5.09, 8] from Peter-Weyl L^8/960 mode-count growth at d=8 spectral dimension; the S86 GATE A dispatch is canonical-record, not adjudication), GATE B `S86-CUTOFF-SQRT-GATE-B-KERNEL-ADMISSIBILITY` (subset-removal sweep on a_0 slot under W2-1 protocol; tests {dim, fin} vs {reg, 1st-order} sourcing), GATE C `S86-CUTOFF-SQRT-GATE-C-S82-APPLICABILITY` (HBW / MP-abs-conv at s=6 on the framework-truncated f_6 = 0.1 residue specifically — NOT the unregulated kernel which was retracted under R2-A-CONV-(a)).

The structural deliverable beyond the per-gate verdict is the **LAYER 1 vs LAYER 2 taxonomy** (R3-C-E3-L). LAYER 1 = combinatorial-position-on-atlas (Mellin support + observable-cross-classification); LAYER 2 = admissibility-on-axioms (numerical GATE A+B+C). The two layers are independent; a regulator can be combinatorially privileged but axiomatically excluded. This permanently repairs the S78-onward conflation that treated the canonical 5-atlas as uniform-admissible.

### 4. Downstream implications

| Stream | Effect of W4 | Next-session action |
|:-------|:-------------|:--------------------|
| BRANCH-IV registry | R_JE retired; R_JK + xi_E_GGE_inv canonical at full float64 | W5a P3 `S86-SECTOR-1-SR-FLOW-Z-FACTOR` HARD UNLOCKED — `from canonical_constants import xi_E_GGE_inv` consumes ξ²(0) IC directly |
| SECTOR-2 taxonomy | K-invariant pin REJECTED on A_5; 5-way per-regulator split forced at registry level | W6 perturbative-immunization corollaries C2 / C-α/β/γ inherit per-regulator splitting; W5a P3 IC inherits per-regulator structure if SECTOR-2 split propagates upstream |
| Atlas cardinality | A_5 PENDING with `cutoff_sqrt` PENDING-EVENT until GATES A+B+C dispatch | 3 new gates pre-registered for S86+ dispatch: `S86-CUTOFF-SQRT-GATE-{A,B,C}-*`; full PRDR pin specs in `sessions/framework/registry/cutoff-sqrt-adjudication.md` §3.1/§3.2/§3.3 |
| C45 S87 sixth-regulator-synthesis | DEFERRED CONFIRMED (REQUIRES-S86-GATE keeps atlas at A_5 PENDING; C45 has no floor to extend) | C45 stays S87-deferred unless a future GATE A dispatch FAILS (atlas → A_4 collapse promotes C45) |
| Publication-precision pre-registration rule | Second independent witness (after S86 W1c-8) | Add to mandatory plan-template machinery-pin checklist: any value cited downstream MUST pre-register `_published_sig_figs` |
| Plan-language for canonical collision check | "use update_constant first to ensure no collision" is wrong (collision check = list_constants); agent self-corrected | Plan-template fix: replace ambiguous wording with the correct MCP call name |
| LAYER 1 / LAYER 2 taxonomy | Permanent registration; S78-onward conflation repaired | All S86+ regulator-class statements MUST tag combinatorial-position vs axiomatic-admissibility separately |

### 5. Wave classification

W4 is a **constraint-map-advancing wave**, mixed-signal at the per-gate level but structurally directional in its net effect on the framework's regulator-class taxonomy. Net moves:
- **Canonicalized** one corridor (BRANCH-IV path-(c) with two distance-tagged diagnostics replacing R_JE).
- **Closed** one corridor (SECTOR-2 single-distance-tag K-invariant; the FAIL is structural, not a numerical near-miss — 92 % deviation, three OOM above PASS threshold).
- **Captured** one workshop adjudication into a registry-canonical record with 3 pre-registered S86+ gates and a permanent LAYER 1 / LAYER 2 taxonomy.

The structurally weightiest finding is the SECTOR-2 K-invariant FAIL: the substrate's Mellin-multiplier residue at s=3 is *regulator-class-dependent*, which means substrate-distance-1 quantities cited downstream (notably W5a P3's ξ²(0) IC) inherit per-regulator structure. The F_2 zeta=SDW machine-epsilon agreement is a definition-level identity (zeta = Mellin on positive-definite spectrum), not evidence; the framework cannot lean on it for a substantive K-invariance claim.

Two plan-time machinery-pin gaps surfaced as PRU Class 8 carry-forwards: publication-precision pre-registration (P4 dual-verdict witness; same pattern as S86 W1c-8) and plan-template wording for canonical-collision-check MCP semantics (P4 self-corrected). Both have explicit fix-now remediations available; the wave synthesis flags them for the next plan-template revision rather than deferring.

---

## Constraint-Map Updates

| Date | Mechanism / gate | Prior state | New state | Reason |
|:-----|:-----------------|:------------|:----------|:-------|
| 2026-04-26 | BRANCH-IV canonical formulation | S85 ambiguous (R_JE single-distance-tag, conflated per gen-physicist 9A §4.6 + lizzi 9A §2.2) | CANONICAL — R_JE retired; R_JK = 0.00803460529503449 (distance-2, M_KK^{−2}) + xi_E_GGE_inv = 13.642473425595973 (distance-1, M_KK^{+1}) registered at full float64 | W4-1 P4 PASS (5/5 CC + Stage-4 anchor consistency at rel_tol=1e-12); two distance-tagged diagnostics replace one |
| 2026-04-26 | S86-BRANCH-IV-FORMULATION-COMMIT | OPEN | PASS line 112 (canonical); FAIL line 110 retained as W1c-8 publication-precision audit trail | dual-line audit trail per `output-standards.md` verdict-permanence + `epistemic-discipline.md` W1c-8 fix prescription |
| 2026-04-26 | SECTOR-2 K-invariant pin | PROVISIONAL hypothesis (single substrate-distance-1 tag for K_substrate) | REJECTED on full A_5 — must split into per-regulator distance tags | W4-2 P5 FAIL: max_pair_ratio = 9.24e-01 (3 OOM above 1e-3 threshold); CC-3 counterexample probe FAIL on Zubarev (rel_deriv = 6.98); F_2 ζ=SDW machine-epsilon match is structural identity (zeta = Mellin) not invariance |
| 2026-04-26 | S86-SECTOR-2-MELLIN-KERNEL-K-INVARIANT | OPEN | FAIL — `max_pair_ratio=9.24e-01;max_pair_abs=1.46e-01;atlas=A_5;deviant=None` | per-regulator Mellin-multiplier residue at s=3 is NOT R-universal across A_5; substrate-distance-1 invariance broken |
| 2026-04-26 | cutoff_sqrt regulator-atlas membership | S85-ambiguous (PENDING-EVENT, no committed status) | A_5 PENDING with `cutoff_sqrt` PENDING-EVENT; 3-gate adjudication apparatus pre-registered | W4-3 C28 INFO/REQUIRES-S86-GATE; workshop convergence captured per substitution-chain direction-read of lines 1153 + 1329 + 1606 |
| 2026-04-26 | LAYER 1 (combinatorial) vs LAYER 2 (axiomatic-admissibility) regulator-classification taxonomy | implicit (S78-onward conflation: 5-atlas treated as uniform-admissible) | PERMANENT methodology — registered in `sessions/framework/registry/cutoff-sqrt-adjudication.md` §3.4 + §6 | R3-C-E3-L workshop deliverable; ratified by R3 connes E1-L acceptance line 1329 + R3 lizzi line 1606 |
| 2026-04-26 | S86-CUTOFF-SQRT-GATE-A-LMAX-FINITENESS | did not exist | PRE-REGISTERED at PRDR-grade for S86+ dispatch | C28 STEP 3 framework write; full machinery pin in `cutoff-sqrt-adjudication.md` §3.1; expected outcome FAIL per R3-C-E3-C (Peter-Weyl L^8/960 mode-count growth ⇒ α = −k_eff/4 < 0) |
| 2026-04-26 | S86-CUTOFF-SQRT-GATE-B-KERNEL-ADMISSIBILITY | did not exist | PRE-REGISTERED at PRDR-grade | C28; full machinery pin in §3.2; subset-removal-sweep protocol on a_0 slot |
| 2026-04-26 | S86-CUTOFF-SQRT-GATE-C-S82-APPLICABILITY | did not exist | PRE-REGISTERED at PRDR-grade | C28; full machinery pin in §3.3; HBW / MP-abs-conv at s=6 on f_6=0.1 residue specifically |
| 2026-04-26 | C45 `S86-SIXTH-REGULATOR-SYNTHESIS` | DEFERRED conditional on C28 | DEFERRED CONFIRMED to S87 | C28 INFO/REQUIRES-S86-GATE keeps atlas at A_5 PENDING; C45 has no atlas-cardinality floor to extend until GATES A+B+C dispatch |
| 2026-04-26 | W5a P3 `S86-SECTOR-1-SR-FLOW-Z-FACTOR` | BLOCKED on P4 (ξ²(0) IC source) | UNLOCKED — sources from `xi_E_GGE_inv` via `from canonical_constants import xi_E_GGE_inv` | per partition §3 sequencing row "W4 (P4) → W5 (P3)"; HARD dependency now satisfied |
| 2026-04-26 | Publication-precision pre-registration rule | Single witness (S86 W1c-8) | TWO independent witnesses; structural carry-forward to plan-template | W4-1 P4 dual-verdict reproduces W1c-8 surface exactly; rule confirmed across two independent sub-domains (n_s vs canonical-constant registration) |
| 2026-04-26 | Plan-language for collision-check MCP semantics | implicit ("use update_constant first to ensure no collision") | FLAGGED for plan-template fix (correct call is `list_constants` or `get_constant`) | W4-1 P4 agent self-corrected at runtime; future plan-templates should use the correct MCP call name |

---

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Framework / WP edits | Size |
|:-----|:-------|:------------|:------------|:---------------------|:-----|
| W4-1 P4 | `computations/s86_w4_p4_branch_iv_commit.py` (485 lines, 23,441 B) | — (commit gate, no .npz) | — | NEW `sessions/framework/registry/branch-iv-canonical.md` (275 lines, 14,412 B); AMENDED `computations/canonical_constants.py` (+8,447 B SECTION E.B + 2 PROVENANCE entries, 97,328 → 105,775 B); WP §W4-1 (114 lines) | script + framework + canonical |
| W4-2 P5 | `computations/s86_w4_p5_sector_2_k_invariant.py` (35,894 B) | `computations/s86_w4_p5_sector_2_k_invariant.npz` (10,829 B — poles, all-pairs deviations, ∂(pole_R)/∂ε, atlas state, mellin_cone_live + gpu_available flags, all CC results) | `computations/s86_w4_p5_sector_2_k_invariant.png` (114,467 B — 2-panel: pole_R values + log10(rel_dev) all-pair matrix with PASS/FAIL threshold lines) | WP §W4-2 (125 lines) | script + data + plot + WP |
| W4-3 C28 | `computations/s86_w4_c28_cutoff_sqrt_adjudication.py` (733 lines, 41,478 B) | — (parse + classify + write gate; structured output is the framework file) | — | NEW `sessions/framework/registry/cutoff-sqrt-adjudication.md` (369 lines, 23,051 B; 6 sections + 3 PRDR-grade gate pre-registrations); WP §W4-3 (164 lines) | script + framework + WP |

**Verdict-file additions** (`computations/s86_gate_verdicts.txt` lines 106–113):
- Line 106–107: `S86-W-4-CUTOFF-SQRT-ADJUDICATION` INFO + companion row (audit `5ce75a47…` content `afd0d440…`)
- Line 108–109: `S86-SECTOR-2-MELLIN-KERNEL-K-INVARIANT` FAIL + companion row (audit `61350742…` content `7bcace34…`)
- Line 110–111: `S86-BRANCH-IV-FORMULATION-COMMIT` FAIL (W1c-8 audit-trail line; audit `d7f433b3…` content `21c5b8a3…`)
- Line 112–113: `S86-BRANCH-IV-FORMULATION-COMMIT` PASS (canonical final; audit `acc75110…` content `55090d91…`)

All 4 verdicts carry full 64-char dual-SHA + companion comment row per W9a-99 dual-SHA template; `audit_sha256` computed at runtime via `_closure_hash`-equivalent logic per `.claude/rules/v3-closure-recovery.md` §sig_5 (HARDCODING NOT PRESENT — verified by re-execution producing identical SHA after pub-precision fix on P4).
