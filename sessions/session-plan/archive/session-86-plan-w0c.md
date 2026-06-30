# Session 86 Plan — Wave W0c: Canonical-constants consolidation + computation lifts

**Wave owner**: `gen-physicist` (planner only — runtime agents per-gate, see §I)
**Output verdict file**: `computations/s86_gate_verdicts.txt` (canonical per `.claude/rules/gate-verdicts.md`)
**Item count**: 9
**Theme**: canonical_constants.py registrations + computation lifts + W3-7 floor re-pin
**Parent partition**: `sessions/session-plan/session-86-partition.md` §1 Wave W0c

---

## §0. Wave W0c Summary

Wave W0c is the canonical-constants and methodology-infrastructure foundation for S86. It performs nine independent edits / extractions / lifts that downstream waves depend on for PRDR-compliant pin discipline. None of the items require heavy compute; the largest single item (C14, λ_top extraction) reads a pre-existing D_K spectral cache and pins λ_max(L=10) to 6 sig figs. The remaining items are file edits or boilerplate retrofits that close PRU vulnerabilities flagged in the S85 closeout.

The wave is structurally independent at plan-write time (no inter-W0c sequencing); at compute time the items can dispatch in any order since they touch disjoint files (canonical_constants.py vs S85 plan files vs `.claude/rules/` vs `sessions/permanent-results-registry.md` vs `sessions/framework/registry/external-clock-scaffold.md`). C14 reads `computations/artifacts/s85_w12_elim1_D_K_Lmax_moments.npz` (or equivalent — the exact cache filename is pinned in §0.11 below); writes go to `canonical_constants.py`, `permanent-results-registry.md`, S85 plan files, computation scripts, `.claude/rules/`, and `sessions/framework/registry/external-clock-scaffold.md`.

**Item summary**:
| # | Gate ID | Owner subagent | Effort | Type |
|:--|:--------|:---------------|:-------|:-----|
| 1 | S86-LAMBDA-TOP-DIRECT-EXTRACTION (C14) | `connes-ncg-theorist` | 1h | GEOMETRIC |
| 2 | S86-K_CRIT_BDG-CANONICAL-CONSTANTS-REGISTRATION (C17) | `volovik-superfluid-universe-theorist` | 30m | META |
| 3 | S86-CANONICAL-ENTRY-CONSOLIDATION (C18) | `kaluza-klein-theorist` | 1h | META |
| 4 | S86-K-FLOOR-K-WALL-LAND (C19) | `volovik-superfluid-universe-theorist` | 1h | PHONONIC |
| 5 | S86-R3-YAML-LIFT (C21) | `kaluza-klein-theorist` | 1h | META |
| 6 | S86-MELLIN-COMPLIANCE-LIFT (C22) | `lizzi-spectral-functional-theorist` | 2h | META |
| 7 | S86-W12-4-A_N-REGULATOR-PIN-DISCIPLINE (P14) | `connes-ncg-theorist` | 1.5h | META |
| 8 | S86-EXTERNAL-CLOCK-SCAFFOLD (C25) | `mack-cosmic-bridge` | 1h | META |
| 9 | S86-W3-7-PASS-CLAUSE-RE-PIN (C27) | `kaluza-klein-theorist` | 30m | META |

**Aggregate effort**: ~9h across 9 dispatches; concurrent-dispatch friendly (≤8 concurrent agents per `feedback_dispatch-discipline.md`).

---

## §0.5. Wave W0c Decision-Point Prerequisites

W0c is foundation; no upstream prerequisites within S86 (parallel-eligible with W0a, W0b, W1a, W1b, W1c, W2, W4 per partition §4 Batch 1).

**Downstream consumers** (waves that hard-depend on W0c outputs):
- **W1a (T1 — 17 W0-W5 theorem-grade landings)** consumes C17 (`K_crit_BdG = 2.035` distinct from `K_crit = 91.5`) for the W2-12 K_crit_BdG entry; consumes C18 (5 missing canonical entries — eps_H_HP1_norm, HP1_dim, FI_parity_exclusion, rank_exclusion, nonflat_T_correction_L2) for the W5/W6 theorem rows.
- **W2 (Mellin infrastructure)** consumes C22 (5-marker Mellin compliance boilerplate) so C9/C10/C11 inherit the lifted scaffold rather than re-introducing variance.
- **W3 (C43 W3-11 Λ-convention resolution)** consumes C14 (Λ_top = λ_max(L=10) to 6 sig figs) — Λ_actual replaces Casimir-saturated and `c_fabric*M_KK` ad hoc choices.
- **W5 (W5-D.4 K_floor / K_wall registry)** is upstream of C19; this wave LANDS K_floor + K_wall in canonical_constants.py + permanent-results-registry per the W5 D.4 derivation.
- **W7 (C1 joint CC residue, C4 branch-c phonon discriminator)** consumes C19 K_floor / K_wall corridor pins for branch-c discriminator boundary conditions.

**Plan-write parallelism**: this wave's plan-file is written without reading any other S86 plan file; runtime sequencing is enforced by upstream-pin SHAs at dispatch time (§0.11 below).

---

## §I. Carry-Forward Items Mapping (9 rows)

| Plan-Block | Source ID | Source synthesis citation | Theme | Owner subagent | Effort | Trigger | Class |
|:-----------|:----------|:--------------------------|:------|:---------------|:-------|:--------|:------|
| §W0c-1 | C14 | S85 closeout §3.5 (Λ-convention triple disambiguation) | D_K spectral λ_max extraction | `connes-ncg-theorist` | 1h | [VERIFY] | GEOMETRIC |
| §W0c-2 | C17 | S85 closeout §3.4 (K_crit triple-collision PRU) | K_crit_BdG canonical registration | `volovik-superfluid-universe-theorist` | 30m | [VERIFY] | META |
| §W0c-3 | C18 | S85 closeout §3.6 (5 missing canonical-constants entries) | Canonical-entry consolidation | `kaluza-klein-theorist` | 1h | [VERIFY] | META |
| §W0c-4 | C19 | S85 W5 D.4 (K_floor / K_wall corridor derivation) | K_floor + K_wall registry land | `volovik-superfluid-universe-theorist` | 1h | [VERIFY] | PHONONIC |
| §W0c-5 | C21 | S85 closeout §6.4 sig_4 coverage 9.2% | R3 YAML schema_version lift | `kaluza-klein-theorist` | 1h | [AUDIT] | META |
| §W0c-6 | C22 | S85 closeout §6.5 W6-71 boilerplate compliance | Mellin compliance lift (8 scripts) | `lizzi-spectral-functional-theorist` | 2h | [AUDIT] | META |
| §W0c-7 | P14 | S85 W12-4 CANON-REGULATOR-PIN-DISCIPLINE | Bare-`a_n` regulator-pin tag rule | `connes-ncg-theorist` | 1.5h | [AUDIT] | META |
| §W0c-8 | C25 | S85 closeout §7.4 external-clock scaffold | External-clock scaffold (S86-S96) | `mack-cosmic-bridge` | 1h | [VERIFY] | META |
| §W0c-9 | C27 | S85 W3-7 PASS = 10% structurally unattainable | W3-7 PASS clause re-pin to 12.5% | `kaluza-klein-theorist` | 30m | [SIGN] | META |

---

## §W0c-1. S86-LAMBDA-TOP-DIRECT-EXTRACTION

**1. Gate ID**: `S86-LAMBDA-TOP-DIRECT-EXTRACTION` (C14)

**2. Trigger**: `[VERIFY]` — direct numerical extraction from D_K spectral cache; no sign claim, but PASS-criterion is a 6-sub-condition conjunction.

**3. Classification**: **GEOMETRIC** — Λ_top is the top eigenvalue of D_K on Jensen-deformed SU(3) at L_max=10. It pins the substrate's vibrational ceiling (the maximum eigenfrequency the fabric supports); subsequent waves use this as the empirical Λ_actual replacing Casimir-saturated and `c_fabric*M_KK` ad hoc choices in W3-11.

**4. Agent type**: `connes-ncg-theorist` — owns spectral-triple eigenvalue extraction discipline (5-atlas convention, Pauli-Villars vs ζ regulator tagging, dual-SHA dispatch on D_K cache reads). `spectral-geometer` is also acceptable; `connes-ncg-theorist` is preferred because the L_max=10 cache was generated under his pin discipline.

**5. Hypothesis**: The top eigenvalue λ_max of D_K at L_max=10 on Jensen-deformed SU(3), extracted directly from the pre-existing spectral cache, agrees to 6 sig figs with the value asymptotically inferred from the W0-7 series (lambda_max ≈ 5.42 M_KK at L=12); we pin Λ_top := λ_max(L=10) as a canonical constant and verify 6 PASS sub-criteria.

**6. Method (dispatch prompt for runtime agent)**:

> Dispatch to `connes-ncg-theorist`:
>
> Write `computations/s86_w0c_lambda_top_extract.py` per `.claude/templates/script-template.py`. The script:
>
> (a) Imports from canonical: `from canonical_constants import M_KK, c_fabric, J_C2`. Tags every computed intermediate `# (local)`.
>
> (b) Locates the D_K spectral cache. Default expected path: `computations/artifacts/s85_w12_elim1_D_K_Lmax_moments.npz`. If absent, the script enumerates candidates via glob `computations/data/d_k_*L10*.npz` and `computations/data/d_k_*L10*.npz`, prints the candidate list with SHA-256 of each, and exits with code 2 (not a verdict FAIL — a script-environment FAIL per `math-scripts.md` §Exit Codes). The orchestrator then provides the canonical cache path via PIN before re-dispatch.
>
> (c) Loads the cache. Logs `sha256` of the cache file in the first 20 lines of stdout. Validates `eigvals.shape[0] == 155984` (expected count at L_max=10 per framework status).
>
> (d) Extracts λ_max via `numpy.max(numpy.abs(eigvals))` (small reduction; not a 100×100 linalg op). For the 6 PASS sub-criteria below requiring eigenvalue density / spacing statistics on subsets ≥100×100 in matrix form, use `torch.linalg` with explicit GPU pin: `device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')`; assert `device.type == 'cuda'` if matrix size exceeds the GPU threshold per `feedback_compute-environment.md`. CPU fallback: `os.environ.setdefault('OMP_NUM_THREADS', '8')` BEFORE `import numpy`.
>
> (e) Pins Λ_top to 6 sig figs via Python `f"{lambda_max:.5e}"` (5 fractional digits at scientific notation = 6 total sig figs).
>
> (f) Tests the 6 PASS sub-criteria, in order:
>
>   1. **Cache-integrity sub-criterion**: cache file SHA matches the value pinned at dispatch time (§0.11 below); FAIL if mismatch.
>   2. **Count sub-criterion**: `eigvals.shape[0] == 155984`; FAIL if count differs.
>   3. **Hermiticity sub-criterion**: imaginary parts of all eigvals satisfy `max(abs(eigvals.imag)) < 1e-10`; FAIL otherwise (D_K is self-adjoint by construction; non-zero imag parts indicate cache corruption).
>   4. **Magnitude sub-criterion**: `lambda_max / M_KK ∈ [4.5, 6.5]` — the asymptotic W0-7 value 5.42 M_KK at L=12 sets the central expectation; the L=10 truncation is bracketed within ±20% per truncation-monotonicity.
>   5. **Asymptotic-consistency sub-criterion**: the L=10 → L=12 extrapolation under W0-7 power-law fit predicts a ratio `lambda_max(L=10) / lambda_max(L=12) ∈ [0.85, 1.0]` (truncation monotonically lowers the top eigenvalue); FAIL if outside band.
>   6. **6-sig-fig stability sub-criterion**: re-load the cache twice and re-extract; the two extractions must agree at all 6 sig figs (deterministic-extraction check); FAIL otherwise.
>
> (g) On all-6-PASS: appends to `computations/s86_gate_verdicts.txt` via the template's `append_verdict(...)` helper (atomic single-line `open("a")` append; never read-modify-write per the S84 W1 race lesson):
>
> `S86-LAMBDA-TOP-DIRECT-EXTRACTION: PASS -- value=<lambda_max_to_6_sigfig> scheme=spectral_cache_direct convention=L_max=10_native L_max=10 sha256=<64-char closure>`
>
> Plus dual-SHA companion comment row per `.claude/rules/gate-verdicts.md`: `# content_sha256=<64-char> audit_sha256=<64-char>`. Closure SHA computed at runtime from the ordered input-pin map (cache SHA + script SHA + canonical_constants.py SHA + L_max + scheme + convention).
>
> (h) On any-sub-criterion-FAIL: appends `S86-LAMBDA-TOP-DIRECT-EXTRACTION: FAIL -- value=<v> scheme=spectral_cache_direct convention=L_max=10_native L_max=10 sha256=<closure>` and writes a `s86_w0c_1_failure_diagnosis.json` artifact identifying which sub-criterion failed.
>
> (i) Adds `Lambda_top_L10` to `canonical_constants.py` with the pinned value and provenance comment block citing S86-W0c-1, the cache SHA, and the script SHA. Calls `update_constant("Lambda_top_L10", value, "S86", "W0c-1", "C14: λ_max(L=10) direct extraction from D_K spectral cache; 6 sig figs")`.
>
> (j) Writes the working-paper section `§W0c-1` to `sessions/archive/session-86/working-paper-w0c.md` (≥15 lines): verdict line, six sub-criterion results, asymptotic-consistency table, cache-SHA pin trace, downstream-consumer pointer to W3 C43.
>
> Substrate-framing reminder (mandatory, agent-prompt suffix): "Λ_top is the substrate's vibrational ceiling — the maximum eigenfrequency the Jensen-deformed SU(3) fabric supports at L_max=10 truncation. Do NOT frame this as 'the cutoff scale' (container thinking — implies an external cutoff applied to a pre-existing field theory). Frame as: D_K's top eigenvalue IS the upper limit of substrate-supported vibrational mode content at this truncation level."

**7. Machinery pin (PRDR)**:
- `L_max = 10` (truncation level, pinned at dispatch)
- `scheme = spectral_cache_direct` (no Mellin, no analytic continuation; direct extraction)
- `convention = L_max=10_native` (no Pauli-Villars subtraction; bare cache eigenvalues)
- `GPU_path = torch.linalg on device='cuda' if matrix_op_size >= 100`; CPU fallback `OMP_NUM_THREADS = 8`
- `cache_path_pin = computations/artifacts/s85_w12_elim1_D_K_Lmax_moments.npz` (orchestrator-supplied at dispatch; runtime SHA verified)
  - **Pin-validator rescue note (Phase 3e)**: this npz stores `L_max` as a 3-element grid `[8, 10, 12]`; the gate operates on the L=10 slice via `npz['L_max'].tolist().index(10)` at compute time per `.claude/rules/gate-verdicts.md` runtime canonical-path rule. The npz does not store `scheme` / `convention` keys — those are gate-level metadata, not cache-level. Validator FAIL is documented-rescue-accepted, not a script-environment failure.
- `cache_sha_pin = <computed-at-runtime>` (logged to stdout in first 20 lines; verified against orchestrator-supplied PIN)
- `extraction_seed = N/A` (deterministic op, not stochastic)
- `tolerance_rule = ABSOLUTE` (sub-criterion 4 magnitude band, sub-criterion 5 ratio band; sub-criterion 6 strict equality at 6 sig figs)

**8. Expected output 4-tuple**: `(value=<Lambda_top_L10_to_6_sigfig>, scheme=spectral_cache_direct, convention=L_max=10_native, L_max=10)`

**9. PASS / FAIL / INFO thresholds**:
- **PASS**: all 6 sub-criteria PASS (cache-integrity, count, hermiticity, magnitude band, asymptotic-consistency, 6-sig-fig stability).
- **FAIL**: any 1+ sub-criterion FAILs. Verdict line records `value=<extracted>` regardless; failure-diagnosis JSON records which sub-criterion(s) failed.
- **INFO**: cache file absent (script exits 2; not a verdict).

**10. Substitution chain** (sub-criterion 4 magnitude band):

```
Step 1 (definitions):
  lambda_asymptotic(L=12)  ≈ 5.42 · M_KK             [W0-7 series fit, S82]
  L_max_truncation(L=10)   = lower-truncation case   [definition]
  truncation_monotonicity  = "lower L_max → lower or equal lambda_max"  [Connes-Chamseddine spectral truncation, monotone decreasing]

Step 2 (substitute):
  lambda_max(L=10) ≤ lambda_max(L=12)
  ⇒ lambda_max(L=10) ≤ 5.42 · M_KK

Step 3 (simplify):
  Combine with lower-bound (the cache cannot have collapsed to zero — physical eigenvalue spectrum is bounded below by spectral-action a_0 positivity):
  lambda_max(L=10) > 0
  Centered at 5.42 with ±20% truncation tolerance:
  lambda_max(L=10) / M_KK ∈ [0.80 · 5.42, 1.20 · 5.42] = [4.336, 6.504]
  Rounded to a clean band: [4.5, 6.5]

Step 4 (direction):
  lambda_max(L=10) / M_KK > 6.5  ⇒ FAIL (cache value exceeds asymptotic ceiling — indicates non-truncation-monotone behavior or cache corruption)
  lambda_max(L=10) / M_KK < 4.5  ⇒ FAIL (truncation collapse beyond physical expectation)
  Otherwise PASS magnitude sub-criterion.
```

**11. What PASSES / FAILS MEAN**:
- **PASS**: Λ_top := λ_max(L=10) lands as a canonical constant pinned to 6 sig figs; W3 C43 (W3-11 Λ-convention resolution) can substitute Λ_actual for the Casimir-saturated and `c_fabric*M_KK` choices, closing the Λ-convention triple-disambiguation flagged in S85 closeout §3.5. The substrate's vibrational ceiling is now an empirically-pinned scale, not a derived ad hoc.
- **FAIL** (any sub-criterion): The cache integrity is in question, OR the L=10 truncation is non-monotone with L=12 (would close the W0-7 series-fit story), OR the spectral cache requires regeneration (Level-3 escalation: re-run the full L=10 spectral computation, ~12-24h GPU). Solution-space impact: W3 C43 cannot substitute Λ_actual without a verified pin; W3 stays in the Λ-convention triple-collision state.
- **INFO** (cache absent): Level-3 escalation; cache regeneration becomes a prerequisite.

**12. Effort estimate**: 1h (script write + cache load + 6-sub-criterion test + verdict + canonical_constants.py edit + WP section).

**13. Substrate-framing reminder**: Λ_top is the substrate's vibrational ceiling at L_max=10 truncation — the upper limit of D_K-supported eigenfrequency. Direction of explanation: D_K eigenvalues → λ_max → Λ_top pin → downstream Λ-convention closure. Do NOT invert: do not say "Λ_top is the cutoff applied to the field theory" (container thinking — implies an external cutoff on a pre-existing field theory).

---

## §W0c-2. S86-K_CRIT_BDG-CANONICAL-CONSTANTS-REGISTRATION

**1. Gate ID**: `S86-K_CRIT_BDG-CANONICAL-CONSTANTS-REGISTRATION` (C17)

**2. Trigger**: `[VERIFY]` — registry-write gate; PASS = constant lands in canonical_constants.py with correct value + provenance.

**3. Classification**: **META** — canonical-constants registration; eliminates K_crit triple-collision PRU vulnerability flagged in S85 closeout §3.4.

**4. Agent type**: `volovik-superfluid-universe-theorist` — owns BdG-channel discipline (K_crit_BdG = 2.035 is the BdG-channel critical coupling, distinct from the inflationary corridor `K_crit = 91.5`). Volovik's S62 work pinned the BdG critical coupling; he is the canonical author for the registration entry.

**5. Hypothesis**: Promoting `K_crit_BdG = 2.035` to canonical_constants.py as a distinct constant from `K_crit = 91.5` eliminates the PRU vulnerability where downstream gates citing "K_crit" silently consumed the wrong value.

**6. Method (dispatch prompt for runtime agent)**:

> Dispatch to `volovik-superfluid-universe-theorist`:
>
> Edit `computations/canonical_constants.py`. Add new entry (alphabetically placed near existing `K_crit`):
>
> ```python
> # ─────────────────────────────────────────────────────────────
> # K_crit_BdG: BdG-channel critical coupling
> # ─────────────────────────────────────────────────────────────
> # PROVENANCE: S62 W2 (Volovik BdG-channel derivation),
> #             confirmed S82 W3-K, S85 W5 D.4 corridor pin.
> # CITATION:   sessions/permanent-results-registry.md §W5-D.4
> # SOURCE:     `computations/s62_w2_bdg_critical.py` (S62)
> # DISTINCT FROM:
> #   K_crit = 91.5  (inflationary corridor critical coupling, S65 W4)
> #   K_floor / K_wall (W5 D.4 substrate-corridor pins; see C19 W0c-4)
> # UNITS:      dimensionless (coupling in M_KK units)
> # ─────────────────────────────────────────────────────────────
> K_crit_BdG = 2.035  # BdG-channel critical coupling (Volovik S62)
> ```
>
> Verify the existing `K_crit = 91.5` entry is unaltered; the two MUST coexist as distinct named constants. If `K_crit = 91.5` is currently undocumented in canonical_constants.py (i.e., bare `K_crit = 91.5` without provenance comment), ADD a provenance block analogous to the K_crit_BdG block above, citing S65 W4 (inflationary corridor critical coupling).
>
> Call `update_constant("K_crit_BdG", 2.035, "S86", "W0c-2", "C17: BdG-channel critical coupling; distinct from K_crit=91.5 inflationary corridor; eliminates K_crit triple-collision PRU per S85 closeout §3.4")`.
>
> Run `python computations/canonical_constants.py --self-test` (if such a hook exists) OR `python -c "from computations/_shared.canonical_constants import K_crit, K_crit_BdG; assert K_crit == 91.5; assert K_crit_BdG == 2.035; print('OK')"` to verify both constants are importable + distinct.
>
> Append verdict to `computations/s86_gate_verdicts.txt`:
>
> `S86-K_CRIT_BDG-CANONICAL-CONSTANTS-REGISTRATION: PASS -- value=2.035 scheme=canonical_constants_register convention=BdG_channel L_max=N/A sha256=<64-char closure>`
>
> Closure SHA from input-pin map: (canonical_constants.py-pre-edit SHA, S62 W2 source script SHA, K_crit_BdG value, K_crit value).
>
> Write WP section `§W0c-2` (≥15 lines): verdict line, before/after canonical_constants.py diff, K_crit triple-collision PRU resolution, downstream consumers (W1a T1 W2-12 K_crit_BdG row, W7 C4 branch-c discriminator).

**7. Machinery pin (PRDR)**:
- `K_crit_BdG_value = 2.035` (pinned exactly; from Volovik S62 W2 BdG-channel derivation)
- `K_crit_value_unchanged = 91.5` (existing canonical-constant value, asserted unchanged)
- `canonical_constants_pre_edit_sha = <computed-at-runtime>` (logged before edit)
- `S62_W2_source_sha = <computed-at-runtime>` (provenance trace pin)
- `tolerance_rule = THEOREM` (exact-value registry-write; no numerical tolerance)

**8. Expected output 4-tuple**: `(value=2.035, scheme=canonical_constants_register, convention=BdG_channel, L_max=N/A)`

**9. PASS / FAIL / INFO thresholds**:
- **PASS**: `K_crit_BdG = 2.035` exists in canonical_constants.py with provenance block + `K_crit = 91.5` coexists unaltered + `update_constant(...)` call recorded.
- **FAIL**: any of: variable absent, value mismatch, K_crit overwritten, provenance block missing.
- **INFO**: not applicable (registry-write is binary).

**10. Substitution chain**: not applicable — registry-write gate, no sign/direction claim.

**11. What PASSES / FAILS MEAN**:
- **PASS**: K_crit triple-collision PRU vulnerability (closeout §3.4) is closed. Downstream gates citing K_crit_BdG vs K_crit cannot silently swap values; PRDR-K-disambiguation (W0a R5) now sees zero false-positives. W1a T1's W2-12 row can land K_crit_BdG = 2.035 with confidence.
- **FAIL**: PRU vulnerability persists; downstream gates remain at risk of value-swap collisions. Re-dispatch with explicit pin path.

**12. Effort estimate**: 30 min (file edit + import test + verdict + WP section).

**13. Substrate-framing reminder**: K_crit_BdG is the BdG-channel critical coupling — a substrate-corridor scale at which BCS-type pairing destabilizes. Frame as: "the substrate's BdG corridor terminates at K = 2.035 (in M_KK units)", NOT as "the field theory's BdG cutoff" (container thinking).

---

## §W0c-3. S86-CANONICAL-ENTRY-CONSOLIDATION

**1. Gate ID**: `S86-CANONICAL-ENTRY-CONSOLIDATION` (C18)

**2. Trigger**: `[VERIFY]` — multi-entry registry-write; PASS = all 5 constants present with correct values + provenance.

**3. Classification**: **META** — canonical-constants consolidation closing 5 PRU-flagged missing entries.

**4. Agent type**: `kaluza-klein-theorist` — owns the HP^1 / FI / rank-class topology that produced 4 of the 5 entries (eps_H_HP1_norm, HP1_dim, FI_parity_exclusion, rank_exclusion); the 5th (nonflat_T_correction_L2) comes from vdd §VI which the kaluza-klein-theorist also tracks via the KK-bundle correspondence.

**5. Hypothesis**: Adding 5 missing canonical entries closes the documented PRU vulnerabilities where downstream gates referenced these scales as bare hardcodes (or were not pinnable at all).

**6. Method (dispatch prompt for runtime agent)**:

> Dispatch to `kaluza-klein-theorist`:
>
> Edit `computations/canonical_constants.py`. Add the following 5 entries with provenance blocks. EACH entry receives:
>   - 5-line provenance comment (PROVENANCE / CITATION / SOURCE / UNITS / DISTINCT FROM)
>   - The constant assignment line
>   - An `update_constant(...)` call appended at the bottom-of-file constants-registration block
>
> ```python
> # eps_H_HP1_norm: HP^1 norm of the eps_H cocycle (S84 W10b §V.O lift)
> # PROVENANCE: S84 W10a-114 eps_H HP^1 cocycle near-invariance computation
> # CITATION:   sessions/permanent-results-registry.md §W5-6 (HP^1-near-invariance)
> # SOURCE:     computations/s84_w10a_114_eps_h_hp1_cocycle.npz
> # UNITS:      dimensionless (cocycle norm in HP^1 metric)
> # DISTINCT FROM: ‖[ε_H]‖_{F4} (5-atlas STRICT norm, 60-atlas LOOSE)
> eps_H_HP1_norm = 16.197719
>
> # HP1_dim: dimension of HP^1 (quaternionic projective 1-space)
> # PROVENANCE: standard topology (HP^1 ≅ S^4 has real dim 4; quaternionic dim = 1; the framework-relevant dim is 3 per S84 W10a-117 R-protection classification)
> # CITATION:   sessions/permanent-results-registry.md §VII.K (HP^1-content-distinct corridors)
> # SOURCE:     S84 W10a-117 R-protection classification CSV
> # UNITS:      dimensionless (real dimension of the rank-2 R-protection class)
> HP1_dim = 3
>
> # FI_parity_exclusion: parity-exclusion flag for FI/RD slot atlas (1 = enabled)
> # PROVENANCE: S82 lizzi 42-row M_lizzi atlas + S84 W10b parity-extension §VII.P-v2
> # CITATION:   sessions/permanent-results-registry.md §VII.P-v2 (parity refinement)
> # SOURCE:     S84 W10a-115 GV explicit + S82 lizzi atlas spec
> # UNITS:      boolean (1 = parity-exclusion active; 0 = inactive)
> FI_parity_exclusion = 1
>
> # rank_exclusion: rank-class exclusion threshold for §VII.P-v2 corridors
> # PROVENANCE: S84 W10a-117 R-protection classification (rank=3 corridor exclusion vs rank=1 Witten-integral corridor)
> # CITATION:   sessions/permanent-results-registry.md §VII.K (rank-class)
> # SOURCE:     S84 W10a-117 r_protection_classification.csv
> # UNITS:      dimensionless (rank threshold for exclusion class)
> rank_exclusion = 3
>
> # nonflat_T_correction_L2: non-flat T-correction at L_max=2 (vdd §VI extraction)
> # PROVENANCE: vdd §VI (non-flat T-correction, L_max=2 truncation), extracted per S85 closeout §3.6
> # CITATION:   researchers/Van-den-Dungen/<vdd_paper>.md §VI
> # SOURCE:     extract via computations/s86_w0c_extract_vdd_T_correction.py (script must be co-written; see below)
> # UNITS:      M_KK^2 (curvature-class correction scale squared)
> # DISTINCT FROM: flat-T baseline (vdd §V); higher-L_max corrections (defer to S87+)
> nonflat_T_correction_L2 = <extracted_value_to_6_sigfig>
> ```
>
> For `nonflat_T_correction_L2`: write a small companion script `computations/s86_w0c_extract_vdd_T_correction.py` that reads `researchers/Van-den-Dungen/<vdd_paper>.md` (orchestrator pins the exact filename at dispatch; if absent, the script glob-searches `researchers/Van-den-Dungen/*.md` and prints candidates), parses §VI for the non-flat T-correction at L_max=2, prints the value to 6 sig figs, and exits 0 on success.
>
> Append 5 `update_constant(...)` calls — one per entry — with `("S86", "W0c-3", "C18: ...")` provenance.
>
> Run import test:
> ```python
> from computations/_shared.canonical_constants import eps_H_HP1_norm, HP1_dim, FI_parity_exclusion, rank_exclusion, nonflat_T_correction_L2
> assert eps_H_HP1_norm == 16.197719
> assert HP1_dim == 3
> assert FI_parity_exclusion == 1
> assert rank_exclusion == 3
> assert nonflat_T_correction_L2 > 0  # extracted-at-runtime; existence + positivity check
> print("OK")
> ```
>
> Append verdict (one line per entry would be 5 lines; use ONE consolidated verdict per the gate-ID convention):
>
> `S86-CANONICAL-ENTRY-CONSOLIDATION: PASS -- value=5_entries_landed scheme=canonical_constants_register convention=mixed L_max=mixed sha256=<64-char closure>`
>
> Closure SHA from input-pin map: (canonical_constants.py-pre-edit SHA, S84 W10a-114 npz SHA, S84 W10a-117 csv SHA, vdd paper SHA, all 5 values).
>
> Write WP section `§W0c-3` (≥15 lines): verdict line, before/after canonical_constants.py diff for each of 5 entries, vdd extraction trace for `nonflat_T_correction_L2`, downstream consumers.

**7. Machinery pin (PRDR)**:
- `eps_H_HP1_norm = 16.197719` (S84 W10a-114 cache; 6 sig figs)
- `HP1_dim = 3` (S84 W10a-117 R-protection class; integer)
- `FI_parity_exclusion = 1` (S82 lizzi atlas + S84 W10b parity flag; boolean)
- `rank_exclusion = 3` (S84 W10a-117; integer)
- `nonflat_T_correction_L2 = <runtime-extracted to 6 sig figs>` (vdd §VI; pinned at dispatch by SHA of vdd paper)
- `vdd_paper_sha_pin = <computed-at-runtime>` (orchestrator-supplied)
- `tolerance_rule = THEOREM` for first 4 (exact registry values); `ABSOLUTE` for 5th (6 sig figs against vdd §VI extraction)

**8. Expected output 4-tuple**: `(value=5_entries_landed, scheme=canonical_constants_register, convention=mixed, L_max=mixed)`

**9. PASS / FAIL / INFO thresholds**:
- **PASS**: all 5 entries exist in canonical_constants.py with correct values + provenance blocks + `update_constant(...)` calls; import test prints "OK".
- **FAIL**: any 1+ entry absent, value-mismatch, or import-test failure. Verdict records which entries failed via `s86_w0c_3_failure_diagnosis.json`.
- **INFO**: vdd paper file absent or §VI cannot be parsed for `nonflat_T_correction_L2` — the other 4 entries land; the 5th defers; verdict is INFO with sub-status `nonflat_T_correction_L2_DEFERRED`.

**10. Substitution chain**: not applicable — registry-write gate, no sign/direction claim.

**11. What PASSES / FAILS MEAN**:
- **PASS**: 5 PRU-flagged missing entries close; downstream gates can pin against canonical names rather than bare hardcodes. W1a T1 (17 W0-W5 theorem-grade landings) consumes `eps_H_HP1_norm` for the W5-6 HP^1-near-invariance row; W1b T6 consumes `HP1_dim` + `rank_exclusion` for the §VII-B 5-atlas registry; W9 C24 §VII.P-v2 consumes `FI_parity_exclusion`.
- **FAIL** (any entry): downstream gates lack canonical pin; PRU vulnerability persists for the affected entry. Re-dispatch.
- **INFO** (vdd extraction defer): 4 entries land; 5th deferred to S87 with explicit pin path requirement.

**12. Effort estimate**: 1h (4 file edits + 1 vdd-extraction co-script + 5 import tests + verdict + WP section).

**13. Substrate-framing reminder**: All 5 entries pin substrate-corridor scales (HP^1 cocycle norm, HP^1 dimension, parity-exclusion class, rank-class threshold, non-flat T-correction). Frame as substrate-geometry pins, NOT as field-theory parameters. Direction: D_K spectral structure → HP^1 / rank-class corridors → these pinned scales.

---

## §W0c-4. S86-K-FLOOR-K-WALL-LAND

**1. Gate ID**: `S86-K-FLOOR-K-WALL-LAND` (C19)

**2. Trigger**: `[VERIFY]` — registry-write gate landing K_floor + K_wall as canonical-constants entries AND writing the W5 D.4 derivation block to permanent-results-registry with dual-SHA provenance.

**3. Classification**: **PHONONIC** — K_floor and K_wall are substrate-corridor pins bracketing the BdG critical region; they bound the corridor in which BdG-channel quasiparticle excitations propagate without re-entering the inflationary corridor (K > K_wall) or collapsing into the BdG-condensate (K < K_floor).

**4. Agent type**: `volovik-superfluid-universe-theorist` — the W5 D.4 derivation is in his BdG-channel discipline (Volovik's S82-S85 work pinned the K_floor / K_wall corridor boundaries via 3He-B-inheritance correspondence).

**5. Hypothesis**: Promoting K_floor and K_wall to canonical_constants.py with the W5 D.4 derivation source, and writing the corresponding W5 D.4 block to `sessions/permanent-results-registry.md` with dual-SHA provenance, lands the substrate-corridor-pin pair as a single registry record consumable by W7 C1/C4.

**6. Method (dispatch prompt for runtime agent)**:

> Dispatch to `volovik-superfluid-universe-theorist`:
>
> **Step 1**: Verify `sessions/permanent-results-registry.md` exists. If absent, CREATE it with header per `.claude/templates/_registry-template.md` (or analog), then proceed.
>
> **Step 2**: Edit `computations/canonical_constants.py`. Add:
>
> ```python
> # ─────────────────────────────────────────────────────────────
> # K_floor: BdG-corridor lower boundary
> # ─────────────────────────────────────────────────────────────
> # PROVENANCE: S85 W5 D.4 derivation (Volovik BdG-corridor brackets)
> # CITATION:   sessions/permanent-results-registry.md §W5-D.4
> # SOURCE:     computations/s85_w5_d4_kfloor_kwall.py (S85 W5)
> # UNITS:      dimensionless (coupling in M_KK units)
> # DISTINCT FROM: K_crit_BdG = 2.035 (BdG critical, mid-corridor)
> #                K_crit = 91.5 (inflationary corridor critical)
> # ─────────────────────────────────────────────────────────────
> K_floor = <S85_W5_D.4_derived_value_to_6_sigfig>  # BdG-corridor lower boundary
>
> # ─────────────────────────────────────────────────────────────
> # K_wall: BdG-corridor upper boundary
> # ─────────────────────────────────────────────────────────────
> # PROVENANCE: S85 W5 D.4 derivation (Volovik BdG-corridor brackets)
> # CITATION:   sessions/permanent-results-registry.md §W5-D.4
> # SOURCE:     computations/s85_w5_d4_kfloor_kwall.py (S85 W5)
> # UNITS:      dimensionless (coupling in M_KK units)
> # DISTINCT FROM: K_floor (corridor lower boundary)
> # ─────────────────────────────────────────────────────────────
> K_wall = <S85_W5_D.4_derived_value_to_6_sigfig>   # BdG-corridor upper boundary
> ```
>
> Values come from the S85 W5 D.4 verdict-line entry in `computations/s85_gate_verdicts.txt`. Orchestrator pins the exact W5 D.4 verdict-line SHA at dispatch (§0.11 below); the dispatched agent must fetch the values FROM the verdict line, not re-derive.
>
> Append 2 `update_constant(...)` calls.
>
> **Step 3**: Write `sessions/permanent-results-registry.md` block at the §W5-D.4 slot:
>
> ```markdown
> ## §W5-D.4 — K_floor / K_wall BdG-corridor brackets
>
> **Status**: PERMANENT (S85 W5 D.4 PASS)
> **Owner**: volovik-superfluid-universe-theorist
> **Source**: S85 W5 D.4 derivation
> **Verdict-line SHA (audit)**: <S85 W5 D.4 audit_sha256>
> **Verdict-line SHA (content)**: <S85 W5 D.4 content_sha256>
> **Canonical-constants entries**: K_floor, K_wall (W0c-4 land)
>
> **Substrate framing**:
> The BdG corridor is bracketed [K_floor, K_wall] in M_KK units. K_floor is the
> lower boundary at which BdG-channel quasiparticle excitations collapse into
> the BdG condensate; K_wall is the upper boundary at which the BdG corridor
> terminates and the inflationary corridor (K_crit = 91.5) takes over. K_crit_BdG
> = 2.035 lies inside the corridor.
>
> **Derivation steps**: see computations/s85_w5_d4_kfloor_kwall.py;
> 5-step substitution chain in the source script's comment block.
>
> **Downstream consumers** (S86):
> - W7 C1 (joint CC residue) consumes K_floor / K_wall for branch-c boundary.
> - W7 C4 (branch-c phonon discriminator) consumes both for the 10× ABSOLUTE ratio.
> - W9 C26 (W2-2 instantiations) cross-checks corridor brackets.
> ```
>
> **Step 4**: Append verdict to `computations/s86_gate_verdicts.txt`:
>
> `S86-K-FLOOR-K-WALL-LAND: PASS -- value=K_floor_K_wall_landed scheme=canonical_constants_plus_registry convention=W5_D.4_derivation L_max=N/A sha256=<64-char closure>`
>
> Plus dual-SHA companion comment row: `# content_sha256=<64-char> audit_sha256=<64-char>`. Closure SHA from input-pin map: (canonical_constants.py-pre-edit SHA, permanent-results-registry.md pre-edit SHA, S85 W5 D.4 verdict-line SHA, K_floor value, K_wall value).
>
> Write WP section `§W0c-4` (≥15 lines): verdict line, K_floor + K_wall values + sub-criterion verification (K_floor < K_crit_BdG < K_wall ordering check), permanent-results-registry block diff, downstream consumers.

**7. Machinery pin (PRDR)**:
- `K_floor_value = <S85 W5 D.4-derived; pinned by W5 D.4 verdict-line SHA>`
- `K_wall_value = <S85 W5 D.4-derived; pinned by W5 D.4 verdict-line SHA>`
- `S85_W5_D4_verdict_sha_pin = <computed-at-runtime>` (orchestrator-supplied)
- `permanent_results_registry_pre_edit_sha = <computed-at-runtime>`
- `canonical_constants_pre_edit_sha = <computed-at-runtime>`
- `ordering_check = K_floor < K_crit_BdG < K_wall` (sub-criterion)
- `tolerance_rule = THEOREM` (exact-value registry-write); ordering-check is `ABSOLUTE` strict

**8. Expected output 4-tuple**: `(value=K_floor_K_wall_landed, scheme=canonical_constants_plus_registry, convention=W5_D.4_derivation, L_max=N/A)`

**9. PASS / FAIL / INFO thresholds**:
- **PASS**: K_floor + K_wall both in canonical_constants.py + W5 D.4 block in permanent-results-registry.md with dual-SHA + ordering check K_floor < K_crit_BdG < K_wall holds.
- **FAIL**: any of: variable absent, registry block absent, W5 D.4 SHA mismatch, ordering violated.
- **INFO**: `permanent-results-registry.md` did not exist at session start; the script CREATED it (status sub-tag `REGISTRY_CREATED`). Verdict still PASS but logged as INFO-flag for next-session tracking.

**10. Substitution chain** (ordering check):

```
Step 1 (definitions):
  K_floor    = BdG-corridor lower boundary  [W5 D.4]
  K_crit_BdG = BdG critical coupling        [W0c-2; = 2.035]
  K_wall     = BdG-corridor upper boundary  [W5 D.4]

Step 2 (substitute the corridor-bracket definition):
  BdG-corridor := {K : K_floor ≤ K ≤ K_wall}
  K_crit_BdG ∈ BdG-corridor (definition: K_crit_BdG is the critical point
                              INSIDE the corridor, not at a boundary)

Step 3 (simplify):
  K_floor < K_crit_BdG < K_wall  [strict, since K_crit_BdG is a critical
                                   point not coincident with either boundary]

Step 4 (direction):
  Ordering MUST hold for the corridor framing to be self-consistent.
  K_floor ≥ K_crit_BdG  ⇒ FAIL (corridor lower boundary would exceed critical;
                                  no BdG-channel sub-corridor exists below critical)
  K_wall ≤ K_crit_BdG   ⇒ FAIL (corridor upper boundary would not exceed critical;
                                  no BdG-channel sub-corridor exists above critical)
```

**11. What PASSES / FAILS MEAN**:
- **PASS**: K_floor / K_wall pin lands; substrate-corridor brackets are now canonical. W7 C1 (joint CC residue across phonon-first/transit/landau) and W7 C4 (branch-c phonon discriminator) can consume corridor brackets directly; W9 C26 cross-check works. The substrate's BdG corridor is empirically pinned end-to-end.
- **FAIL** (ordering violated): the W5 D.4 derivation contains an internal inconsistency between K_crit_BdG (W0c-2) and the K_floor / K_wall brackets. Level-3 escalation: re-derive W5 D.4 OR re-derive K_crit_BdG. Solution-space impact: BdG corridor framing is provisional pending reconciliation.
- **INFO** (registry created): registry pre-existence assumption was wrong; W0c-4 created the file. Next-session housekeeping: cross-check that no other gate lost write-access to the registry file due to creation timestamp.

**12. Effort estimate**: 1h (registry existence check + 2 canonical-constants entries + registry block write + ordering check + verdict + WP section).

**13. Substrate-framing reminder**: K_floor and K_wall are substrate-corridor brackets, NOT field-theory cutoffs. The BdG corridor IS the substrate-region in coupling-space where BdG-channel quasiparticles propagate; it is not "imposed from outside" but emerges from D_K's BdG-channel spectral structure. Frame as: "the substrate's BdG corridor is bracketed [K_floor, K_wall]", NOT "we impose K_floor and K_wall as IR/UV cutoffs".

---

## §W0c-5. S86-R3-YAML-LIFT

**1. Gate ID**: `S86-R3-YAML-LIFT` (C21)

**2. Trigger**: `[AUDIT]` — coverage-threshold gate; PASS = ≥90% machinery_pin blocks carry `schema_version: R3` (sig_4 PASS threshold per `.claude/rules/v3-closure-recovery.md`).

**3. Classification**: **META** — schema-version lift across S85 plan files closing sig_4 coverage gap (currently 9.2%, must reach ≥90%).

**4. Agent type**: `kaluza-klein-theorist` — owns plan-block schema discipline; the R3 schema_version pin discipline was authored under his rule-write track.

**5. Hypothesis**: Iterating over all S85 plan files (W0-W13) and inserting `schema_version: R3` into machinery_pin blocks where absent lifts sig_4 coverage from current 9.2% to ≥90%, satisfying the v3-closure-recovery sig_4 threshold.

**6. Method (dispatch prompt for runtime agent)**:

> Dispatch to `kaluza-klein-theorist`:
>
> Write `computations/s86_w0c_r3_yaml_lift.py`. The script:
>
> (a) Globs `sessions/session-plan/session-85-plan-w*.md`. Logs each filename + SHA-256 to stdout in the first 20 lines.
>
> (b) For each plan file, parses gate blocks (using the existing parser logic from `computations/_yaml_gate_validator.py` if available; otherwise implements a minimal block parser keyed on `## §W{n}-{k}.` headers and locating `machinery_pin:` YAML sub-blocks).
>
> (c) For each `machinery_pin:` block, checks for the presence of a `schema_version: R3` key. If absent, inserts `  schema_version: R3` as the first sub-key of the machinery_pin block (preserving 2-space YAML indent).
>
> (d) After all edits, re-runs `computations/_yaml_gate_validator.py` (the canonical sig_4 audit tool per `v3-closure-recovery.md`). Captures the JSON output. The audit reports `sig_4_coverage` as a fraction.
>
> (e) PASS iff `sig_4_coverage >= 0.90`. The script writes a per-file diff to `s86_w0c_5_r3_lift_diff.patch` for human review.
>
> (f) Appends verdict to `computations/s86_gate_verdicts.txt`:
>
> `S86-R3-YAML-LIFT: PASS|FAIL -- value=<sig_4_coverage_fraction> scheme=R3_yaml_lift convention=schema_version_R3 L_max=N/A sha256=<64-char closure>`
>
> Closure SHA from input-pin map: (sorted list of S85 plan file SHAs pre-edit, sorted list post-edit, _yaml_gate_validator.py SHA, sig_4_coverage value).
>
> Write WP section `§W0c-5` (≥15 lines): verdict line, before/after sig_4_coverage, count of machinery_pin blocks edited per S85 plan file, list of any plan files where insertion failed (parser exceptions), downstream impact on v3-closure-recovery sig_4.

**7. Machinery pin (PRDR)**:
- `target_glob = sessions/session-plan/session-85-plan-w*.md`
- `pre_edit_per_file_sha = <computed-at-runtime>` (logged for each)
- `_yaml_gate_validator.py SHA = <computed-at-runtime>`
- `pass_threshold = 0.90` (sig_4 coverage; per v3-closure-recovery)
- `tolerance_rule = ABSOLUTE` (coverage fraction strict ≥ 0.90)
- `insertion_position = first sub-key of machinery_pin` (deterministic; not at end)

**8. Expected output 4-tuple**: `(value=<sig_4_coverage_post_lift>, scheme=R3_yaml_lift, convention=schema_version_R3, L_max=N/A)`

**9. PASS / FAIL / INFO thresholds**:
- **PASS**: `sig_4_coverage >= 0.90` post-lift.
- **FAIL**: `sig_4_coverage < 0.90` post-lift. Indicates that some machinery_pin blocks are non-parseable (YAML syntax errors, malformed indentation) or the parser missed blocks.
- **INFO**: parser fails on any S85 plan file (raises exception); script exits 2 with the offending file logged. Not a verdict FAIL — a script-environment escalation.

**10. Substitution chain** (90% coverage threshold):

```
Step 1 (definitions):
  sig_4               = boolean signal; PASS iff coverage_fraction >= threshold
  coverage_fraction   = (machinery_pin blocks WITH schema_version:R3) / (total machinery_pin blocks across S85 plan files)
  threshold           = 0.90  [from .claude/rules/v3-closure-recovery.md sig_4 spec]

Step 2 (substitute):
  Pre-S86 measurement: coverage_fraction = 0.092  (S85 closeout §6.4)
  Post-W0c-5 lift (mechanical insertion at every absent block):
    coverage_fraction → 1.0  if every absent block is successfully edited

Step 3 (simplify):
  In practice some blocks may be non-parseable (YAML syntax errors) → coverage_fraction
  falls in [parseable_fraction, 1.0]. PASS iff parseable_fraction >= 0.90.

Step 4 (direction):
  threshold = 0.90 (v3-closure-recovery PIN, not adjustable)
  Coverage above 0.90 → sig_4 = 1 (PASS)
  Coverage below 0.90 → sig_4 = 0 (FAIL); v3-closure-recovery enters Stage-1 remediation
                                           with this gate as the failed signal.
```

**11. What PASSES / FAILS MEAN**:
- **PASS**: sig_4 coverage clears 90% threshold; v3-closure-recovery sig_4 signal will PASS for S86 closeout. Downstream impact: any S85 plan-block consumed by S86 gates (e.g., W3-7 PASS clause re-pin in W0c-9) carries the R3 schema and inherits PRDR-compliance.
- **FAIL**: sig_4 stays below 90%; v3-closure-recovery must enter Stage-1 remediation (per `v3-closure-recovery.md` §Stage 1, sig_4 remediation = edit gate block to add `schema_version: R3` + re-run validator). Solution-space impact: S86 closeout's v3-ladder may transition to V3-NON-COMPLIANT if the gap cannot be closed within Stage-1 2-iteration cap.
- **INFO**: parser failure on a specific S85 plan file → file-level escalation; manual repair of the offending file required before re-run.

**12. Effort estimate**: 1h (script write + glob + parse + insert + validator re-run + verdict + WP section).

**13. Substrate-framing reminder**: META gate; no substrate physics. The R3 schema is a methodology-pin discipline (it pins gate-block format, not substrate observables).

---

## §W0c-6. S86-MELLIN-COMPLIANCE-LIFT

**1. Gate ID**: `S86-MELLIN-COMPLIANCE-LIFT` (C22)

**2. Trigger**: `[AUDIT]` — boilerplate-compliance gate; PASS = all 8 non-compliant Mellin-labeled scripts now carry the W6-71 5-marker boilerplate.

**3. Classification**: **META** — script-level boilerplate retrofit closing W6-71 compliance gap.

**4. Agent type**: `lizzi-spectral-functional-theorist` — owns Mellin discipline; the W6-71 5-marker boilerplate originates from his Mellin-Strip / Convergence-Cone theorem registration.

**5. Hypothesis**: Applying the W6-71 5-marker boilerplate to the 8 non-compliant Mellin-labeled scripts brings all currently-active Mellin scripts into compliance, enabling W2 (Mellin infrastructure) C9/C10/C11 builds to inherit the lifted scaffold.

**6. Method (dispatch prompt for runtime agent)**:

> Dispatch to `lizzi-spectral-functional-theorist`:
>
> **Step 1**: Identify the W6-71 5-marker boilerplate template. Locate the source via `Grep` on `pattern="W6-71"` in `computations/`. The boilerplate is documented at the top of the W6-71 producing script (S82 or earlier). Pin the boilerplate text + its SHA at dispatch (§0.11 below).
>
> The 5 markers (per S85 W6-71 verdict trace; canonical names):
>   1. `# MELLIN-CONVERGENCE-STRIP: <s_lower>, <s_upper>` — Mellin convergence strip declared
>   2. `# MELLIN-RESIDUE-EXTRACTION: <method>` — residue-extraction method tagged
>   3. `# MELLIN-COUNTERTERM-SUBTRACTION: <Seeley-DeWitt-coefficient>` — counter-term subtraction explicit
>   4. `# MELLIN-ANALYTIC-CONTINUATION-PATH: <path-spec>` — continuation path spec
>   5. `# MELLIN-CLOSURE-VERIFICATION: <self-test-result>` — closure verification stamp
>
> **Step 2**: Identify the 8 non-compliant Mellin-labeled scripts. Glob `computations/*mellin*.py` and `computations/*Mellin*.py`. For each script, scan for the 5 markers; flag scripts missing 1+ markers as non-compliant.
>
> Expected non-compliant set (8 scripts; subject to glob verification at runtime — orchestrator may pin the exact 8 at dispatch via SHA list in §0.11):
>   1. `computations/s79_p1_mellin_*.py`
>   2. `computations/s80_w0_*_mellin_*.py`
>   3. `computations/s82_w*_mellin_*.py` (3 scripts)
>   4. `computations/s83_w*_mellin_*.py` (2 scripts)
>   5. `computations/s84_w*_mellin_*.py` (1 script)
>
> If glob count differs from 8, the script logs the discrepancy and proceeds with whatever non-compliant set it finds; orchestrator updates the W0c-6 expected count for next session.
>
> **Step 3**: For each non-compliant script, INSERT the 5 markers near the script header (immediately after `from canonical_constants import *`). Use the W6-71 reference values where applicable (e.g., `MELLIN-CONVERGENCE-STRIP: -1, +3` is the W6-71 default; per-script values may differ — the agent must read each script's intent and pin the actual strip).
>
> **Step 4**: Re-run a 5-marker validator (write a small `computations/_mellin_5_marker_audit.py` if absent) confirming all 8 scripts post-lift carry the 5 markers.
>
> **Step 5**: Append verdict:
>
> `S86-MELLIN-COMPLIANCE-LIFT: PASS|FAIL -- value=<n_compliant>/<n_total> scheme=W6_71_boilerplate convention=5_marker L_max=N/A sha256=<64-char closure>`
>
> Closure SHA from input-pin map: (W6-71 boilerplate SHA, sorted list of 8 script SHAs pre-edit, sorted list post-edit, _mellin_5_marker_audit.py SHA, n_compliant value).
>
> Write WP section `§W0c-6` (≥15 lines): verdict line, list of 8 scripts edited, per-script marker-status table (5 markers × 8 scripts), W6-71 boilerplate-text reference, downstream impact on W2 C9/C10/C11.

**7. Machinery pin (PRDR)**:
- `boilerplate_source = W6-71 producing script header`
- `boilerplate_sha_pin = <computed-at-runtime>` (orchestrator-supplied at dispatch)
- `target_script_glob = computations/*mellin*.py` (case-insensitive)
- `expected_target_count = 8` (variance flagged at runtime; not auto-failed if 7 or 9)
- `marker_set = 5` (CONVERGENCE-STRIP, RESIDUE-EXTRACTION, COUNTERTERM-SUBTRACTION, ANALYTIC-CONTINUATION-PATH, CLOSURE-VERIFICATION)
- `pass_threshold = n_compliant_post_lift == n_total_post_lift` (100% of identified non-compliant set)
- `tolerance_rule = THEOREM` (binary marker presence per script)

**8. Expected output 4-tuple**: `(value=<n_compliant_post_lift>/<n_total>, scheme=W6_71_boilerplate, convention=5_marker, L_max=N/A)`

**9. PASS / FAIL / INFO thresholds**:
- **PASS**: all identified non-compliant scripts post-lift carry the 5 markers (n_compliant == n_total).
- **FAIL**: any script post-lift missing 1+ markers (insertion failed; manual repair required).
- **INFO**: glob count differs from expected 8 (e.g., found 7 or 9). Logs discrepancy; proceeds with actual set; flagged for next-session expected-count update.

**10. Substitution chain**: not applicable — boilerplate-compliance gate is a binary per-script marker check.

**11. What PASSES / FAILS MEAN**:
- **PASS**: All currently-active Mellin scripts compliant with W6-71 5-marker boilerplate. W2 C9/C10/C11 (Mellin infrastructure builds) inherit the lifted scaffold; no per-script convention drift between the W2 master heat-kernel build and the 8 retrofitted scripts.
- **FAIL** (any script): per-script repair required; W2 may consume a non-compliant script with hidden convention drift. Solution-space impact: W2 closures (T9, W0-7 / W0-11 / W0-20 re-emissions) inherit drift risk.
- **INFO** (count variance): expected-count was 8 from S85 closeout; actual count variance flagged. May indicate scripts moved between archive/active or a previously-uncatalogued Mellin script exists.

**12. Effort estimate**: 2h (boilerplate identification + 8-script per-script edit + validator write + verdict + WP section).

**13. Substrate-framing reminder**: META gate. The 5-marker boilerplate is a methodology-pin (not a substrate-physics pin); it ensures Mellin scripts declare their convergence-strip / counter-term / continuation-path conventions explicitly so downstream consumers cannot silently inherit incompatible conventions.

---

## §W0c-7. S86-W12-4-A_N-REGULATOR-PIN-DISCIPLINE

**1. Gate ID**: `S86-W12-4-A_N-REGULATOR-PIN-DISCIPLINE` (P14)

**2. Trigger**: `[AUDIT]` — promotion of W12-4 CANON-REGULATOR-PIN-DISCIPLINE to permanent epistemic rule + retrofit of all computation scripts citing bare `a_n`.

**3. Classification**: **META** — rule-file landing + retrofit; codifies regulator-pin discipline so every `a_n` Seeley-DeWitt-coefficient citation in any computation script or WP section carries an explicit regulator-pin tag (`a_0^{ζ}`, `a_2^{Pauli-Villars}`, etc.).

**4. Agent type**: `connes-ncg-theorist` — owns Seeley-DeWitt + regulator discipline; W12-4 CANON-REGULATOR-PIN-DISCIPLINE was authored under his track.

**5. Hypothesis**: Promoting the W12-4 regulator-pin discipline from S85-W12-4-local-rule to a permanent epistemic rule in `.claude/rules/`, and retrofitting all computation scripts containing bare `a_n` references (no regulator tag), eliminates the persistent ambiguity where `a_2` could mean `a_2^{ζ}` (zeta-regulated) or `a_2^{Pauli-Villars}` depending on the calling script's convention.

**6. Method (dispatch prompt for runtime agent)**:

> Dispatch to `connes-ncg-theorist`:
>
> **Step 1 (rule-file landing — LIGHT)**:
>
> Create `.claude/rules/regulator-pin-discipline.md` with the following content (or extend an existing rule if the topic exists):
>
> ```markdown
> # Regulator-Pin Discipline (a_n Seeley-DeWitt Coefficient Tagging)
>
> ## Rule
>
> Every citation of a Seeley-DeWitt coefficient `a_n` in a computation script,
> working-paper section, or plan-block MUST include an explicit regulator-pin
> tag. Bare `a_n` (without superscript regulator tag) is FORBIDDEN.
>
> ## Tag Format
>
> `a_n^{<regulator_name>}` where <regulator_name> is one of:
>
>   - `ζ`        — zeta-function regularization
>   - `Pauli-Villars` — Pauli-Villars regularization
>   - `Mellin`   — Mellin-Barnes regularization (per W2 C9 infra)
>   - `lattice`  — lattice spacing regularization
>   - `cutoff`   — sharp UV cutoff regularization
>
> Example:
>   ✗ Bare:    a_2 (regulator unspecified)
>   ✓ Tagged:  a_2^{ζ}        (zeta-regulated Seeley-DeWitt)
>   ✓ Tagged:  a_2^{Pauli-Villars}  (PV-regulated Seeley-DeWitt)
>
> ## Rationale
>
> The numerical value of a_n depends on the regulator (S85 W12-4 verdict trace).
> Bare a_n in a downstream script silently consumes the calling-context regulator,
> which may differ from the producing-script regulator. This is a Class-8 PRU
> vulnerability per .claude/rules/epistemic-discipline.md.
>
> ## Audit
>
> The retrofit script `computations/_a_n_regulator_pin_audit.py` greps
> for bare `a_n` patterns and flags violations. /weave --update may auto-run
> this audit.
>
> ## Source
>
> S85 W12-4 CANON-REGULATOR-PIN-DISCIPLINE (gate verdict).
> Promoted to permanent rule in S86 W0c-7 (gate ID: S86-W12-4-A_N-REGULATOR-PIN-DISCIPLINE).
> ```
>
> **Step 2 (retrofit script — MODERATE)**:
>
> Write `computations/_a_n_regulator_pin_audit.py`. The script:
>
> (a) Greps computations/*.py and computations/*.py for the regex `\ba_(\d+)\b(?!\^)` (bare `a_n` not immediately followed by `^`).
>
> (b) For each violation, prints filename + line number + offending line.
>
> (c) Returns total violation count.
>
> (d) Optionally (with `--retrofit` flag) attempts auto-tagging: for each violation, opens the file, reads the surrounding 20-line context, infers the regulator from explicit comments or imports (e.g., `from canonical_constants import *` plus a Pauli-Villars-specific function call ⇒ tag as `Pauli-Villars`); if inference is ambiguous, leaves the line unchanged and logs `MANUAL_REVIEW_REQUIRED`.
>
> **Step 3 (retrofit pass)**: run with `--retrofit`. Capture: total violations pre-pass, auto-tagged count, manual-review-required count.
>
> **Step 4**: append verdict:
>
> `S86-W12-4-A_N-REGULATOR-PIN-DISCIPLINE: PASS|FAIL -- value=<auto_tagged_or_manual_remaining>/<total_violations> scheme=regulator_pin_audit convention=tagged_a_n L_max=N/A sha256=<64-char closure>`
>
> Closure SHA from input-pin map: (rule-file SHA post-write, audit-script SHA, target-file SHAs pre-edit, target-file SHAs post-edit, total_violations + auto_tagged + manual_review counts).
>
> PASS iff post-pass: bare `a_n` count == 0 (every violation either auto-tagged or flagged manual; manual-review-required must be 0 for PASS) OR (auto-tagged count + manual-tagged count == total).
>
> Write WP section `§W0c-7` (≥15 lines): verdict line, rule-file content, list of files retrofitted, auto-tag vs manual-review breakdown, downstream impact (every Seeley-DeWitt citation now carries regulator pin).

**7. Machinery pin (PRDR)**:
- `rule_file_target = .claude/rules/regulator-pin-discipline.md`
- `audit_script_target = computations/_a_n_regulator_pin_audit.py`
- `regex_pattern = \ba_(\d+)\b(?!\^)` (bare `a_n` not followed by `^`)
- `target_directories = computations/, computations/`
- `pass_threshold = bare_a_n_count_post_pass == 0` (strict)
- `tolerance_rule = THEOREM` (binary; either every citation is tagged or it isn't)
- `inference_logic_pin = comment_or_import_based` (deterministic per-context heuristic)

**8. Expected output 4-tuple**: `(value=<post_pass_bare_a_n_count>, scheme=regulator_pin_audit, convention=tagged_a_n, L_max=N/A)`

**9. PASS / FAIL / INFO thresholds**:
- **PASS**: post-pass `bare_a_n_count == 0` (every citation either auto-tagged via inference or manually tagged in the same pass).
- **FAIL**: `bare_a_n_count > 0` AND `manual_review_required > 0` (auto-inference failed and manual tagging was deferred).
- **INFO**: `bare_a_n_count == 0` pre-pass (no violations existed; rule lands but retrofit was a no-op). Records as INFO with sub-tag `NO_VIOLATIONS_FOUND`.

**10. Substitution chain**: not applicable — binary regex-violation count.

**11. What PASSES / FAILS MEAN**:
- **PASS**: regulator-pin discipline is a permanent epistemic rule + every existing computation script complies. Future Seeley-DeWitt computations cannot silently inherit the wrong regulator. W2 (Mellin infra) and W6 (perturbative-immunization corollaries) gates inherit the disciplined a_n usage.
- **FAIL**: rule lands but some scripts retain bare a_n. Solution-space impact: PRU vulnerability persists for the affected scripts; downstream computations consuming those scripts inherit regulator-ambiguity. Re-dispatch with manual tagging.
- **INFO** (no violations): rule lands as preventative; no retrofit needed. PASS-equivalent; INFO tag flags that the rule is forward-looking only.

**12. Effort estimate**: 1.5h (rule-file write + audit-script write + retrofit pass + verdict + WP section).

**13. Substrate-framing reminder**: META gate; rule-file discipline. The substrate-physics content is in the underlying a_n values (not in the tagging discipline); this gate is methodology-only.

---

## §W0c-8. S86-EXTERNAL-CLOCK-SCAFFOLD

**1. Gate ID**: `S86-EXTERNAL-CLOCK-SCAFFOLD` (C25)

**2. Trigger**: `[VERIFY]` — registry-write gate creating the external-clock-aligned 11-session scaffold (S86 freeze, S87-S95 maintain, S88 BK-Array ingest, S96 LiteBIRD ingest).

**3. Classification**: **META** — scaffold registry; pre-registers ingest-gates as DOCUMENTATION ONLY (no compute in S86; ingest gates fire at S88 / S96 on data publication).

**4. Agent type**: `mack-cosmic-bridge` — owns observational-pipeline / detector-clock alignment; the BK-Array (2026 publication) and LiteBIRD (2030 publication) ingest cycles are within his cosmic-bridge tracking discipline.

**5. Hypothesis**: Pre-registering an external-clock-aligned 11-session scaffold (S86 freeze, S87 extend, S88 BK-Array ingest, S89-S95 maintain, S96 LiteBIRD ingest) at `sessions/framework/registry/external-clock-scaffold.md`, with freeze-no-re-pin pattern and pre-registered ingest-gate IDs, locks the framework's observational-pipeline plan against drift across the 2026-2030 horizon.

**6. Method (dispatch prompt for runtime agent)**:

> Dispatch to `mack-cosmic-bridge`:
>
> **Step 1**: Verify `sessions/framework/registry/external-clock-scaffold.md` does NOT already exist. If present, halt and escalate to orchestrator (over-write would clobber prior scaffold; W0c-8 is a CREATE gate).
>
> **Step 2**: Create the file with the 11-session table. Content template:
>
> ```markdown
> # External-Clock Scaffold (S86-S96)
>
> **Created**: S86 W0c-8 (gate ID: S86-EXTERNAL-CLOCK-SCAFFOLD)
> **Owner**: mack-cosmic-bridge
> **Pattern**: freeze-no-re-pin (S86 freezes the scaffold; subsequent
>              sessions extend or ingest, never re-pin)
> **Status**: DOCUMENTATION ONLY for S86 (no compute; ingest-gates fire
>             at S88 + S96 on data publication)
>
> ## §1. 11-Session Scaffold Table
>
> | Session | Date Anchor       | Action                                    | Trigger Type   | Gate ID (pre-reg) |
> |:--------|:------------------|:------------------------------------------|:---------------|:------------------|
> | S86     | 2026-04 (frozen)  | Scaffold creation; freeze 2026-2030 plan  | METHODOLOGY    | S86-W0c-8         |
> | S87     | 2026-Q3           | Scaffold extend (add S97-S100 horizon)    | METHODOLOGY    | S87-EXT-EXTERNAL  |
> | S88     | 2026-Q4 (target)  | BK-Array data ingest                      | OBSERVATIONAL  | S88-BK-ARRAY-INGEST |
> | S89     | 2027-Q1           | Post-BK-Array consolidation               | METHODOLOGY    | S89-CONSOL        |
> | S90     | 2027-Q2           | Maintain                                  | MAINTAIN       | S90-MAINT         |
> | S91     | 2027-Q3           | Maintain                                  | MAINTAIN       | S91-MAINT         |
> | S92     | 2027-Q4           | Maintain                                  | MAINTAIN       | S92-MAINT         |
> | S93     | 2028-Q1           | Maintain                                  | MAINTAIN       | S93-MAINT         |
> | S94     | 2028-Q3           | Maintain                                  | MAINTAIN       | S94-MAINT         |
> | S95     | 2029-Q4           | Pre-LiteBIRD prep                         | METHODOLOGY    | S95-PREP          |
> | S96     | 2030-Q1 (target)  | LiteBIRD data ingest                      | OBSERVATIONAL  | S96-LITEBIRD-INGEST |
>
> ## §2. Pre-Registered Ingest-Gates (DOCUMENTATION ONLY in S86)
>
> ### S88-BK-ARRAY-INGEST
>
> **Trigger**: BK-Array 2026 r-tensor-to-scalar publication (Ade+ or successor).
> **Action**: Re-fire S86 W11 C5/C6 lab-falsifier suite + W14 W6 inventory edits
>            using BK-Array measured r-band as new SI anchor.
> **Owner**: mack-cosmic-bridge.
> **Branches** (4-branch decision script per W12 C31):
>   - Branch 1: r ∈ [0, 0.005)   → Path-H r=0.00745 (BK-Array null)
>   - Branch 2: r ∈ [0.005, 0.015) → Path-H r=0.00745 (BK-Array consistent)
>   - Branch 3: r ∈ [0.015, 0.030) → Path-C r=0.0117 (BK-Array prefers Path-C)
>   - Branch 4: r ≥ 0.030          → BOTH-PATHS excluded (re-derivation required)
>
> ### S96-LITEBIRD-INGEST
>
> **Trigger**: LiteBIRD 2030 publication (Hazumi+ or successor).
> **Action**: Re-fire S86 W11 C5/C6 + W14 W6 with LiteBIRD measured r-band.
> **Owner**: mack-cosmic-bridge.
> **Branches**: same 4-branch decision tree as S88, applied to LiteBIRD r-band.
>
> ## §3. Freeze-No-Re-Pin Discipline
>
> The scaffold is FROZEN at S86. Subsequent sessions MAY:
>   - Extend (add S97-S100 horizon at S87)
>   - Ingest (S88 / S96 fire ingest gates on data publication)
>   - Maintain (S89-S95 sessions touch the scaffold only for housekeeping)
>
> Subsequent sessions MUST NOT:
>   - Re-pin S86's frozen 2026-2030 plan (would violate freeze-no-re-pin)
>   - Re-define ingest-gate branches without explicit user approval
>   - Add new ingest-gates between S86 and the target session (would silently
>     re-pin the scaffold)
> ```
>
> **Step 3**: Append verdict:
>
> `S86-EXTERNAL-CLOCK-SCAFFOLD: PASS -- value=11_session_scaffold_landed scheme=external_clock_freeze convention=2026_2030_horizon L_max=N/A sha256=<64-char closure>`
>
> Closure SHA from input-pin map: (target file pre-existence assertion = absent, target file post-write SHA, scaffold table content hash).
>
> Write WP section `§W0c-8` (≥15 lines): verdict line, scaffold table summary, ingest-gate pre-registration trace, freeze-no-re-pin discipline statement, downstream consumers (W11 C5/C6 lab-falsifier suite consumes scaffold; W12 C31 BK-Array classifier pre-build consumes branch spec).

**7. Machinery pin (PRDR)**:
- `target_file = sessions/framework/registry/external-clock-scaffold.md`
- `pre_existence_check = ABSENT_REQUIRED` (CREATE gate)
- `session_count_pin = 11` (S86 through S96 inclusive)
- `ingest_gate_ids_pin = [S88-BK-ARRAY-INGEST, S96-LITEBIRD-INGEST]`
- `branch_count_pin = 4` (per ingest-gate decision tree)
- `tolerance_rule = THEOREM` (file-write success is binary)

**8. Expected output 4-tuple**: `(value=11_session_scaffold_landed, scheme=external_clock_freeze, convention=2026_2030_horizon, L_max=N/A)`

**9. PASS / FAIL / INFO thresholds**:
- **PASS**: file created with 11-session table + pre-registered ingest-gates + freeze-no-re-pin discipline statement.
- **FAIL**: file pre-existed (CREATE gate cannot over-write) OR write failed.
- **INFO**: not applicable for this gate (binary CREATE).

**10. Substitution chain**: not applicable — DOCUMENTATION ONLY scaffold; no sign/direction claim.

**11. What PASSES / FAILS MEAN**:
- **PASS**: external-clock scaffold is the canonical 2026-2030 observational-pipeline plan. Subsequent sessions (S87-S96) operate against a frozen reference; no scaffold-drift is possible without explicit user approval. W11 C5/C6 (lab-falsifier suite) and W12 C31 (BK-Array classifier) consume the scaffold's branch spec.
- **FAIL** (file pre-existed): scaffold creation collision; orchestrator must reconcile (either rename pre-existing file OR confirm pre-existing file IS the canonical scaffold and skip W0c-8).

**12. Effort estimate**: 1h (file write + ingest-gate spec + freeze-discipline statement + verdict + WP section).

**13. Substrate-framing reminder**: META gate; observational-pipeline scaffold. The substrate-physics content lives in the framework predictions (Path-H r=0.00745, Path-C r=0.0117); this gate pins WHEN those predictions get tested against external data, not WHAT the predictions are.

---

## §W0c-9. S86-W3-7-PASS-CLAUSE-RE-PIN

**1. Gate ID**: `S86-W3-7-PASS-CLAUSE-RE-PIN` (C27)

**2. Trigger**: `[SIGN]` — direction claim: 12.5% scheme floor exceeds 10% (current PASS threshold), making the current PASS clause structurally unattainable below the floor.

**3. Classification**: **META** — S85 plan-file edit re-pinning W3-7 PASS clause from 10% to 12.5%.

**4. Agent type**: `kaluza-klein-theorist` — owns plan-block discipline; the W3-7 PASS clause sits in his rule-write track for plan-file edits.

**5. Hypothesis**: Current S85 W3-7 plan-block sets PASS = 10%, which sits BELOW the scheme floor of 12.5% (i.e., the metric being tested can never go below 12.5% under the pinned scheme); the PASS clause is therefore structurally unattainable. Re-pinning PASS = 12.5% (scheme floor) retains FAIL = 30% (geometric midband) and gives the gate a genuine PASS / FAIL boundary.

**6. Method (dispatch prompt for runtime agent)**:

> Dispatch to `kaluza-klein-theorist`:
>
> **Step 1**: Locate the W3-7 plan-block in `sessions/session-plan/session-85-plan-w*.md` (most likely `session-85-plan-w3.md`). Pin the file SHA pre-edit.
>
> **Step 2**: Read the current W3-7 block. Identify the PASS clause line (most likely `pass_threshold: 10%` or `PASS: <metric> < 10%` depending on plan-block format). Verify the FAIL clause sits at 30%.
>
> **Step 3**: Edit the PASS clause to read 12.5% (preserving FAIL = 30% unchanged). Add a comment line above the PASS clause:
>
> ```yaml
> # W3-7 PASS clause re-pinned in S86 W0c-9 (gate: S86-W3-7-PASS-CLAUSE-RE-PIN)
> # Reason: prior PASS=10% sat below scheme floor 12.5%; structurally unattainable.
> # Substitution chain: see sessions/session-plan/session-86-plan-w0c.md §W0c-9.
> pass_threshold: 12.5%
> ```
>
> **Step 4**: Append verdict:
>
> `S86-W3-7-PASS-CLAUSE-RE-PIN: PASS|FAIL -- value=12.5%_pass_30%_fail scheme=W3_7_re_pin convention=scheme_floor_12.5 L_max=N/A sha256=<64-char closure>`
>
> PASS iff edit committed successfully + diff shows PASS line changed from 10% → 12.5% + FAIL line unchanged at 30%. Closure SHA from input-pin map: (S85 W3 plan-file pre-edit SHA, post-edit SHA, scheme-floor value 12.5, FAIL value 30).
>
> Write WP section `§W0c-9` (≥15 lines): verdict line, before/after diff of W3-7 plan-block, substitution chain showing why 12.5% is the scheme floor, PRDR machinery-pin update (W3-7 PASS threshold pin updated), downstream impact on W3-7 re-execution if/when scheduled.

**7. Machinery pin (PRDR)**:
- `target_file = sessions/session-plan/session-85-plan-w3.md` (or whichever S85 plan file contains W3-7; orchestrator pins exact file at dispatch)
- `target_block = W3-7`
- `pre_edit_pass = 10%` (asserted; FAIL if file shows different value)
- `pre_edit_fail = 30%` (asserted unchanged)
- `post_edit_pass = 12.5%` (target value)
- `post_edit_fail = 30%` (preserved)
- `tolerance_rule = THEOREM` (exact-string edit)

**8. Expected output 4-tuple**: `(value=12.5%_pass_30%_fail, scheme=W3_7_re_pin, convention=scheme_floor_12.5, L_max=N/A)`

**9. PASS / FAIL / INFO thresholds**:
- **PASS**: PASS line edited from 10% → 12.5% + FAIL line unchanged at 30% + comment block landed.
- **FAIL**: edit failed OR pre-edit assertions did not match (file showed PASS != 10% or FAIL != 30%; indicates a different W3-7 spec than expected).
- **INFO**: file showed PASS already at 12.5% (no edit needed; pre-edit value matched target). Verdict INFO with sub-tag `ALREADY_REPINNED`.

**10. Substitution chain** (12.5% scheme floor exceeds 10% PASS):

```
Step 1 (definitions):
  scheme_floor              = 12.5%   [the lower-bound the W3-7 metric can attain
                                        under the pinned scheme; per S85 closeout
                                        flag note "W3-7 PASS = 10% structurally
                                        unattainable"]
  current_PASS_threshold    = 10%     [S85 W3-7 plan-block, current value]
  current_FAIL_threshold    = 30%     [S85 W3-7 plan-block, current value]
  metric                    = M(W3-7) [the W3-7 measured quantity under the scheme]

Step 2 (substitute):
  By definition of scheme_floor:
    M(W3-7) ≥ scheme_floor = 12.5%   [for any allowed input under the scheme]

  Current PASS predicate:
    PASS iff M(W3-7) < 10%

  Substitute the floor:
    M(W3-7) ≥ 12.5% > 10% ⇒ M(W3-7) > 10% always
    ⇒ PASS predicate is false for every allowed input
    ⇒ PASS clause is structurally unattainable

Step 3 (simplify):
  Re-pin PASS to scheme_floor:
    new_PASS_threshold = 12.5%
    PASS iff M(W3-7) ≤ 12.5%   [achievable when metric attains the floor]

  FAIL predicate remains:
    FAIL iff M(W3-7) > 30%     [unchanged]

  INFO band:
    INFO iff 12.5% < M(W3-7) ≤ 30%   [genuine intermediate region]

Step 4 (direction):
  scheme_floor (12.5%) > current_PASS (10%)  ⇒ current PASS unattainable
  Re-pin to scheme_floor → PASS becomes attainable when metric saturates the floor.
  FAIL (30%) > scheme_floor (12.5%)          ⇒ FAIL clause genuinely separates
                                                regime where metric far exceeds floor.
  Direction of edit: increase PASS threshold from 10% → 12.5% (lift toward
                     scheme floor).
```

**11. What PASSES / FAILS MEAN**:
- **PASS**: W3-7 plan-block re-pinned with attainable PASS clause; future W3-7 re-execution (if/when scheduled) can return a meaningful PASS verdict. The structural-unattainability flag is closed.
- **FAIL** (pre-edit assertion mismatch): the W3-7 spec evolved between S85 closeout and S86 W0c dispatch; orchestrator must reconcile actual S85 W3-7 spec with the pre-edit assertion before re-dispatching.
- **INFO** (already re-pinned): no edit needed; W3-7 was already at PASS = 12.5%. No-op confirmation; W0c-9 acts as preventative.

**12. Effort estimate**: 30 min (file edit + diff + verdict + WP section).

**13. Substrate-framing reminder**: META gate; plan-file edit. The substrate-physics content (what W3-7 actually measures) is unchanged; only the PASS / FAIL boundary in the plan-block changes. Direction of explanation: scheme floor (geometry-of-the-metric-under-the-scheme) → PASS clause (what counts as success) → re-pin (alignment of clause with floor).

---

## §X. Wave W0c → Downstream Decision Point

| W0c gate | Downstream consumer | Consumed item |
|:---------|:--------------------|:--------------|
| W0c-1 (C14) | W3 §W3-6 (C43 W3-11 Λ-convention resolution) | Λ_top = λ_max(L=10) replaces Casimir-saturated and `c_fabric*M_KK` |
| W0c-2 (C17) | W1a §W1a-1 (T1 W2-12 row) | K_crit_BdG = 2.035 distinct from K_crit = 91.5 |
| W0c-3 (C18) | W1a §W1a-1 (T1 W5-6 / W6-* rows); W1b T6 (HP^1-near-invariance); W9 C24 (§VII.P-v2 parity) | eps_H_HP1_norm; HP1_dim, rank_exclusion; FI_parity_exclusion |
| W0c-4 (C19) | W7 §W7-1 (C1 joint CC residue); W7 §W7-2 (C4 branch-c discriminator); W9 C26 (W2-2 instantiations) | K_floor / K_wall corridor brackets |
| W0c-5 (C21) | S86 closeout v3-closure-recovery sig_4 | sig_4 coverage ≥ 90% |
| W0c-6 (C22) | W2 §W2-1 (C9 Mellin heat-kernel infra); §W2-2 (C10 Mellin cone residue) | 8 Mellin scripts compliant with W6-71 5-marker boilerplate |
| W0c-7 (P14) | All future Seeley-DeWitt computations (W2, W6, W10) | every a_n citation tagged with regulator |
| W0c-8 (C25) | W11 §W11-1 (C5 lab-falsifier suite); W12 §W12-2 (C31 BK-Array classifier) | external-clock 11-session scaffold |
| W0c-9 (C27) | Future W3-7 re-execution (if scheduled S86+) | PASS clause attainable at 12.5% |

**Decision-point flow (sequential within S86)**:
1. W0c executes in Batch 1 (parallel to W0a / W0b / W1a / W1b / W1c / W2 / W4).
2. Batch 2 dispatches once W0c (and other Batch 1 waves) reach ≥3 completions. W3 / W7 / W9 in Batch 2 consume W0c outputs.
3. Late-S86 waves (W11 / W12 in Batch 3) consume W0c-8 (external-clock scaffold).

---

## §0.10. Wave W0c Machinery-Enumeration Pin

Per `.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness, every gate-relevant machinery parameter is enumerated below as a PRDR-PIN block. Items not pinnable at plan-write time are tagged `<computed-at-runtime>` and pinned via the orchestrator at dispatch.

```yaml
schema_version: R3   # required per W0c-5 R3 YAML lift discipline
wave: W0c
gates:
  - id: S86-LAMBDA-TOP-DIRECT-EXTRACTION
    machinery_pin:
      schema_version: R3
      L_max: 10
      scheme: spectral_cache_direct
      convention: L_max=10_native
      GPU_path: torch.linalg cuda for matrix_op >= 100; CPU fallback OMP_NUM_THREADS=8
      cache_path_pin: computations/artifacts/s85_w12_elim1_D_K_Lmax_moments.npz
      cache_sha_pin: <computed-at-runtime>
      extraction_seed: N/A
      tolerance_rule: ABSOLUTE
      pass_sub_criteria_count: 6
  - id: S86-K_CRIT_BDG-CANONICAL-CONSTANTS-REGISTRATION
    machinery_pin:
      schema_version: R3
      K_crit_BdG_value: 2.035
      K_crit_value_unchanged: 91.5
      canonical_constants_pre_edit_sha: <computed-at-runtime>
      S62_W2_source_sha: <computed-at-runtime>
      tolerance_rule: THEOREM
  - id: S86-CANONICAL-ENTRY-CONSOLIDATION
    machinery_pin:
      schema_version: R3
      eps_H_HP1_norm: 16.197719
      HP1_dim: 3
      FI_parity_exclusion: 1
      rank_exclusion: 3
      nonflat_T_correction_L2: <runtime-extracted_to_6_sigfig>
      vdd_paper_sha_pin: <computed-at-runtime>
      tolerance_rule: THEOREM_for_first_4_ABSOLUTE_for_5th
  - id: S86-K-FLOOR-K-WALL-LAND
    machinery_pin:
      schema_version: R3
      K_floor_value: <S85_W5_D4_derived>
      K_wall_value: <S85_W5_D4_derived>
      S85_W5_D4_verdict_sha_pin: <computed-at-runtime>
      permanent_results_registry_pre_edit_sha: <computed-at-runtime>
      canonical_constants_pre_edit_sha: <computed-at-runtime>
      ordering_check: K_floor < K_crit_BdG < K_wall
      tolerance_rule: THEOREM
  - id: S86-R3-YAML-LIFT
    machinery_pin:
      schema_version: R3
      target_glob: sessions/session-plan/session-85-plan-w*.md
      pre_edit_per_file_sha: <computed-at-runtime>
      yaml_gate_validator_sha: <computed-at-runtime>
      pass_threshold: 0.90
      tolerance_rule: ABSOLUTE
      insertion_position: first sub-key of machinery_pin
  - id: S86-MELLIN-COMPLIANCE-LIFT
    machinery_pin:
      schema_version: R3
      boilerplate_source: W6-71 producing script header
      boilerplate_sha_pin: <computed-at-runtime>
      target_script_glob: computations/*mellin*.py (case-insensitive)
      expected_target_count: 8
      marker_set: 5
      pass_threshold: n_compliant_post_lift == n_total_post_lift
      tolerance_rule: THEOREM
  - id: S86-W12-4-A_N-REGULATOR-PIN-DISCIPLINE
    machinery_pin:
      schema_version: R3
      rule_file_target: .claude/rules/regulator-pin-discipline.md
      audit_script_target: computations/_a_n_regulator_pin_audit.py
      regex_pattern: \ba_(\d+)\b(?!\^)
      target_directories: [computations/, computations/]
      pass_threshold: bare_a_n_count_post_pass == 0
      tolerance_rule: THEOREM
      inference_logic_pin: comment_or_import_based
  - id: S86-EXTERNAL-CLOCK-SCAFFOLD
    machinery_pin:
      schema_version: R3
      target_file: sessions/framework/registry/external-clock-scaffold.md
      pre_existence_check: ABSENT_REQUIRED
      session_count_pin: 11
      ingest_gate_ids_pin: [S88-BK-ARRAY-INGEST, S96-LITEBIRD-INGEST]
      branch_count_pin: 4
      tolerance_rule: THEOREM
  - id: S86-W3-7-PASS-CLAUSE-RE-PIN
    machinery_pin:
      schema_version: R3
      target_file: sessions/session-plan/session-85-plan-w3.md  # or wherever W3-7 lives
      target_block: W3-7
      pre_edit_pass: 10%
      pre_edit_fail: 30%
      post_edit_pass: 12.5%
      post_edit_fail: 30%
      tolerance_rule: THEOREM
```

---

## §0.11. Wave W0c Input-SHA Ledger

The orchestrator must compute and pin the following SHAs before dispatching each W0c gate. SHAs not known at plan-write time are tagged `<dispatch-time>`.

| Gate | Pinned input | Pin SHA |
|:-----|:-------------|:--------|
| W0c-1 | `computations/artifacts/s85_w12_elim1_D_K_Lmax_moments.npz` | `<dispatch-time>` |
| W0c-1 | `computations/canonical_constants.py` | `<dispatch-time>` |
| W0c-1 | `computations/_consolidate_intake.py` (verdict appender helper) | `<dispatch-time>` |
| W0c-2 | `computations/canonical_constants.py` (pre-edit) | `<dispatch-time>` |
| W0c-2 | `computations/s62_w2_bdg_critical.py` (provenance trace) | `<dispatch-time>` |
| W0c-3 | `computations/canonical_constants.py` (pre-edit) | `<dispatch-time>` |
| W0c-3 | `computations/data/s84_w10a_114_eps_h_hp1_cocycle.npz` (eps_H_HP1_norm source) | `<dispatch-time>` |
| W0c-3 | `computations/data/s84_w10a_117_r_protection_classification.csv` (HP1_dim, rank_exclusion source) | `<dispatch-time>` |
| W0c-3 | `researchers/Van-den-Dungen/<paper>.md` (nonflat_T_correction_L2 source; orchestrator pins exact filename) | `<dispatch-time>` |
| W0c-4 | `computations/canonical_constants.py` (pre-edit) | `<dispatch-time>` |
| W0c-4 | `sessions/permanent-results-registry.md` (pre-edit; or ABSENT) | `<dispatch-time>` |
| W0c-4 | `computations/s85_gate_verdicts.txt` (W5 D.4 verdict-line entry) | `<dispatch-time>` |
| W0c-4 | `computations/s85_w5_d4_kfloor_kwall.py` (W5 D.4 producing script) | `<dispatch-time>` |
| W0c-5 | `sessions/session-plan/session-85-plan-w0a.md` ... `session-85-plan-w13.md` (per-file pre-edit SHAs) | `<dispatch-time>` |
| W0c-5 | `computations/_yaml_gate_validator.py` | `<dispatch-time>` |
| W0c-6 | `computations/<W6-71 producing script>.py` (boilerplate source) | `<dispatch-time>` |
| W0c-6 | 8 × `computations/*mellin*.py` (per-file pre-edit SHAs) | `<dispatch-time>` |
| W0c-7 | `.claude/rules/` directory listing (to verify regulator-pin-discipline.md does not pre-exist) | `<dispatch-time>` |
| W0c-7 | All computations/*.py and computations/*.py (target-set per-file SHAs) | `<dispatch-time>` |
| W0c-8 | `sessions/framework/` directory listing (to verify external-clock-scaffold.md does not pre-exist) | `<dispatch-time>` |
| W0c-9 | `sessions/session-plan/session-85-plan-w3.md` (W3-7 plan-file; orchestrator pins exact W3-7-containing file) | `<dispatch-time>` |

**Plan-write closure note**: this plan's own SHA is pinned as the sole `audit_sha256` reference for W0c at dispatch time. Each W0c gate's `audit_sha256` includes (a) this plan-file SHA, (b) the producing script's SHA, and (c) the input-pin SHA list. The `content_sha256` is the script's first-20-line stdout SHA per `gate-verdicts.md`.

---

**End of Wave W0c plan.** 9 gate blocks landed. Phase 3e validator (`computations/_plan_upstream_pin_validator.py --json`) MUST run post-write per partition §5.5 before Phase 4 dispatch.
