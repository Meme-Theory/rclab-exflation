# Session 86 Plan — Wave W1a: NCG-Meta + Perturbative-Ledger Immunization-Family parents at §VII.R + §VII.S

**Wave owner**: `lizzi-spectral-functional-theorist`
**Item count**: 4 (T1 + T2 + T3 + T4)
**Theme**: Land 17 W0-W5 theorem-grade PASSes + the 3-signed NCG-Structural-Exclusion Meta-Theorem (§VII.R) + the 1C 6-Φ-branch Perturbative-Ledger Immunization-Family parent (§VII.S) + the IEP class-tag annotation on §VII.S branches A-F.
**Wave class**: 4 × LIGHT registry-write gates (no compute beyond SHA verification + line-by-line file editing). Total wave effort estimate: 4-6 hours (T1 mechanical 2h + T2 1.5h + T3 1.5h + T4 0.5h overhead, parallelizable across one agent invocation).
**Substrate-framing note (apply to entire wave)**: T2 + T3 + T4 land THEOREMS that describe walls in the spectral-triple solution space (the regulator-class structural floor of §1.5 in `session-86-context.md`). They are NOT phononic excitations; they are the geometry of which spectral functionals are admissible. T1 lands 17 PASSes that are themselves substrate-structural: cluster-span identities, Dai-Freed torsions, KO-6 sign flows, BdG bands, two-layer obstructions — the eigenvalue spectrum's algebraic skeleton, not its excitations. Every gate block reiterates this orientation.

---

## §0. Wave W1a Summary

W1a is the FIRST registry-landing wave of S86. It writes four registry / framework artifacts:

1. **T1 — `S86-W0-PERM-LAND-17`** writes 17 new entries to `sessions/permanent-results-registry.md`, one per W0-W5 theorem-grade PASS, each carrying the full 64-character `audit_sha256` + `content_sha256` pair extracted verbatim from `computations/s85_gate_verdicts.txt`.

2. **T2 — `S86-VII-R-NCG-META-THEOREM-LANDING`** opens §VII.R, lands the 3-signed Meta-Theorem statement, the 7 status rows, the 3-axis disjointness table (parity / rank / Mellin-support), and the cross-pair note routing to §VII.S.

3. **T3 — `S86-VII-S-PERTURBATIVE-LEDGER-IMMUNIZATION-FAMILY-LANDING`** opens §VII.S, lands the parent statement of the Immunization Family, and instantiates the six Φ-branch slots (Φ-A through Φ-F) per lizzi 9A §6.8(B-2) + gen-physicist 9A §4.3.

4. **T4 — `S86-VII-R-IEP-ANNOTATION`** annotates each of §VII.S Φ-A...Φ-F with its INTENSIVE/EXTENSIVE class tag per IEP §3.1 (the partition rule originated in lizzi 9A §6.8(B-3) + 1C OQ11).

T2 / T3 / T4 are **LIGHT** registry-write actions — they create slots, write theorem statements verbatim from cited sources, and tag rows. They do NOT recompute physics. T1 is **mechanical** — 17 dual-SHA extractions + 17 registry rows.

**Dedup note (mandatory per partition §1)**: T2 carries the content of `C3 — S86-NCG-STRUCTURAL-EXCLUSION-META-THEOREM-LANDING` (gen-physicist 9A §4.4 + lizzi 9A §6). One registry-write gate, two synthesis cites. T2's hypothesis block names both source citations explicitly.

---

## §0.5. Wave W1a Decision-Point Prerequisites

W1a executes after the following waves' verdicts land in `computations/s86_gate_verdicts.txt`:

| Prerequisite wave | Item | What W1a needs | Why |
|:------------------|:-----|:---------------|:----|
| **W0a** | R5 `S86-CANON-PRDR-K-DISAMBIGUATION` | `K_crit_BdG = 2.035` distinct from `K_crit = 91.5` resolved | T1 row for `S85-W2-12 BdG band` references `K_crit_BdG`; without R5 the registry entry would carry the wrong K-axis label |
| **W0b** | R7 `S86-SINGLE-NAME-CONFLATION-METHODOLOGY-ENTRY` | Single-name-conflation methodology entry written to `sessions/permanent-results-registry.md` | T2 + T3 cross-pair note in §VII.R routes "perturbative ledger" to §VII.S; without R7 the routing rule itself isn't a registry citation |
| **W0c** | C17 `S86-K_CRIT_BDG-CANONICAL-CONSTANTS-REGISTRATION` | `K_crit_BdG = 2.035` registered in `canonical_constants.py` | T1's W2-12 row imports `K_crit_BdG` so its registry entry can cite the canonical constant value, not a script-local literal |

Plan-write itself has NO inter-plan content dependency (per partition §3 substitution chain) — these are EXECUTION-time prerequisites enforced at compute via the `computations/_plan_upstream_pin_validator.py` script.

If any prereq has not landed when the W1a runner is dispatched, the runner issues `INFO -- value="prereq-pending" pre_reg_clause=PRU-Class-8` for the affected sub-row and proceeds with the remaining 16 (T1) / 6 status rows (T2) / 5 Φ-branches (T3) / 5 IEP tags (T4). Each gate's PASS clause requires ALL sub-rows landed; partial completion is INFO-band, not FAIL.

---

## §I. Carry-Forward Items Mapping (4 rows)

| Plan ID | Closeout source | Synthesis origin | Agent (runtime) | Effort |
|:--------|:---------------|:-----------------|:----------------|:-------|
| W1a-1 (T1) | partition §1 W1a item 1 | gen-physicist S-7 §V.1 | `connes-ncg-theorist` | 2h mechanical |
| W1a-2 (T2 = C3) | partition §1 W1a item 2 | lizzi 9A §6.8(B-1) + gen-physicist 9A §4.4 | `connes-ncg-theorist` | LIGHT (1.5h) |
| W1a-3 (T3) | partition §1 W1a item 3 | lizzi 9A §6.8(B-2) + gen-physicist 9A §4.3 | `connes-ncg-theorist` | LIGHT (1.5h) |
| W1a-4 (T4) | partition §1 W1a item 4 | lizzi 9A §6.8(B-3) + 1C OQ11 | `lizzi-spectral-functional-theorist` (planner-runner blacklist DOES NOT apply at compute time per `.claude/skills/rclab-coordinate.md` — only at plan-time; runtime selection is content-driven) | LIGHT (0.5h) |

**Agent-assignment rationale (per gate)**:
- **T1, T2, T3 → `connes-ncg-theorist`**. The `connes-ncg-theorist` is the registry-landing specialist for §VII.M / N / P / Q / R / S registry slots (per agent definition in `.claude/agents/connes-ncg-theorist.md`). T1 + T2 + T3 are §VII landings; T1 in particular is mechanical 17-row write; T2 + T3 are NCG-Meta + Perturbative-Ledger structural-theorem landings. Connes is the natural runtime owner.
- **T4 → `lizzi-spectral-functional-theorist`**. The IEP (Intensive / Extensive Partition) framework is Lizzi-originated (lizzi 9A §6.8 B-3 + 1C OQ11). T4 is a one-pass annotation requiring intimate knowledge of which §VII.S branches are intensive (per-mode quantities like spectral moments, slot-weights) vs extensive (mode-summed quantities like a_n totals, S_zeta). Lizzi the runtime owner — the `planner ≠ runner` blacklist applies only at PLAN-WRITE time per `.claude/skills/rclab-plan/skill.md`; at compute, content-fit governs.
- **NOT gen-physicist for any of W1a's 4 gates** — these are specialized NCG / spectral-functional registry landings, not breadth-coordination. Per `feedback_dispatch-discipline.md`, the dispatch chooses the per-wave specialist who originated the synthesis content.

---

## §W1a-1. S86-W0-PERM-LAND-17

**1. Gate ID**: `S86-W0-PERM-LAND-17`

**2. Trigger**: `[VERIFY]` — verify that 17 dual-SHA pairs extracted from `computations/s85_gate_verdicts.txt` land in `sessions/permanent-results-registry.md` exactly (every SHA character preserved, every §VII slot identifier matched). No sign / direction / threshold claim → no substitution chain required for the verdict itself; the substitution chain in §10 is the EXTRACTION ALGORITHM.

**3. Classification**: META — registry hygiene, no spectral physics computed (the physics was already computed in S85; this gate transcribes its dual-SHA provenance to the canonical registry). Each of the 17 underlying PASSes is itself GEOMETRIC (spectral-triple structure: cluster-span, Dai-Freed torsion, HP^k dim shifts, KO-6 signs, two-layer obstructions, fold uniqueness, etc.).

**4. Agent type**: `connes-ncg-theorist` (registry-landing specialist for §VII.M-S slots; not gen-physicist, per partition §1 W1a-1 specialist assignment).

**5. Hypothesis (one sentence)**: For each of the 17 W0-W5 theorem-grade PASSes named in partition §1 W1a item 1, the verdict line in `computations/s85_gate_verdicts.txt` carries the full 64-character `audit_sha256` and `content_sha256`, and a registry row at the cited §VII slot can be written verbatim from those values without recomputation.

**6. Method — COMPLETE dispatch prompt**:

> Spawn `connes-ncg-theorist` with the following compute-mode brief.
>
> **Read first**: `computations/s85_gate_verdicts.txt` (full file, 206 lines, 52 KB) + `sessions/permanent-results-registry.md` (full file, 216 KB — use chunked Read with `limit=400` per chunk per Read-tool 30 KB byte-limit rule in CLAUDE.md).
>
> **Write target**: `sessions/permanent-results-registry.md` — add 17 NEW registry rows (do NOT modify existing rows).
>
> **Producing script**: `computations/s86_w1a_t1_perm_land_17.py`. The script does NOT recompute physics. It performs:
> 1. Open `s85_gate_verdicts.txt`.
> 2. For each of the 17 gate-ID stems below, scan for the canonical PASS verdict line (skip companion rows starting with `# audit_sha256 companion row`).
> 3. Extract `audit_sha256` and `content_sha256` (full 64-char hex; reject any line where either is < 64 hex chars).
> 4. Map the gate-ID stem to the §VII slot per the table below.
> 5. Append a new line to `sessions/permanent-results-registry.md` of the canonical permanent-row form (per template at `sessions/permanent-results-registry.md` head; format: `| §VII.X | <gate-stem> | <theorem-statement-one-line> | <audit_sha256> | <content_sha256> | session=85 |`).
> 6. Emit the verdict line.
>
> **17 gate-ID stems → §VII slot mapping** (§1.1 W0-W5 portion):
>
> | # | gate-ID stem (matches verdict-file substring) | §VII slot | one-line theorem statement |
> |:--|:----------------------------------------------|:----------|:---------------------------|
> | 1 | `S85-W0-3` (alias `S85-W1a-3`, CC-5 cluster-span) | §VII.K-PROP | CC-5 cluster-span identity span(M_0)^2 == cluster(f_conv) at machine-ε across L ∈ {7,9,11} |
> | 2 | `S85-W0-12` (CC-4 Dai-Freed Z/2) | §VII.K-PROP | CC-4 Dai-Freed Z/2 torsion class shift = 0 for the canonical regulator |
> | 3 | `S85-W0-16` (HP^1 dim-CM2008 (3,3) shift) | §VII.B | HP^1 dim-CM2008 (3,3) shift = 0; HP^1 cohomology integer-stable across regulator family |
> | 4 | `S85-W0-23` (CC-1 η = 0 INFO) | §VII.K-PROP | CC-1 η-invariant = 0 for the spectral triple at L_max=10 (INFO-band, registered as theorem-grade) |
> | 5 | `S85-W2-2` (cross-session theorem family) | §VII.P | W2-2 mother-theorem + 3 corollaries + 2 predicted instantiations (k=3 HP^3 + 4-bucket HP^even q-deformation) |
> | 6 | `S85-W2-3` (HP^3 disjoint corridor) | §VII.P | W2-3 HP^3 disjoint corridor: num_nontrivial = 0 (rank-3 Hochschild triple intersection vanishes) |
> | 7 | `S85-W2-4` (KO-6 Higgs sign +1→−1 RG) | §VII.P | KO-6 Higgs sign flow direction +1 → −1 under RG (CCM-2007 / AC-2010 sign convention) |
> | 8 | `S85-W2-5` (KO-6 η-band 3/3 machine zero) | §VII.P | KO-6 η-band 3/3 = machine zero (η-invariant identically vanishes on the KO-6 corridor) |
> | 9 | `S85-W2-6` (quantum disjoint corridor 4-route) | §VII.P | Quantum disjoint corridor 4-route: q-deformed HKR-SBI under CM-cyclic + Woronowicz, num_nontrivial = 0 |
> | 10 | `S85-W2-10` (3-solo SHA reproduction `cf3b7443…`) | §VII.K-META | 3-solo SHA reproduction (3 independent agents reproduce identical content_sha256 `cf3b7443…` for S84-W2a-11) |
> | 11 | `S85-W2-11` (triality-Jensen commutation) | §VII.K-PROP | Triality-Jensen commutation [τ_3, J_Jensen] = 0.00e+00 (machine-ε) |
> | 12 | `S85-W2-12` (BdG band CMB l_crit=1424.50, T_LB=0.113) | §VII.K-PROP | BdG band CMB l_crit = 1424.50, T_LB = 0.113 at K_crit_BdG = 2.035 (cite K_crit_BdG canonical constant per W0c C17) |
> | 13 | `S85-W3-1` (CF-5 PIXIE μ K_FIRAS γ=1 lockout) | §VII.K-PROP | CF-5 PIXIE-μ × K_FIRAS γ=1 lockout: regulator-spread = 0 across canonical heat-kernel convention A |
> | 14 | `S85-W3-4` (K-regulator functorial closure-defect) | §VII.K-PROP | CF-6 K-regulator functorial closure-defect = 2.55e-16 (cross-regulator A-union-B at L_max=10) |
> | 15 | `S85-W3-5` (two-speed transfer c_S=f_B machine ε) | §VII.K-PROP | CF-2 two-speed transfer identity c_S = f_B at machine-ε (cross-regulator convention A, L_max=10) |
> | 16 | `S85-W3-9` (Ginzburg-Oz validity Gi=5.50e-10) | §VII.K-PROP | Ginzburg-Oz validity criterion Gi = 5.50e-10 (mean-field intact over W3 regulator family) |
> | 17 | `S85-W5-7` (two-layer obstruction n_joint=0/5) | §VII.B | Two-Layer Obstruction Theorem: n_joint = 0 / 5 across the 5-regulator atlas (every conjunct fails individually for every regulator — already verified in `s85_gate_verdicts.txt` line 169) |
>
> **GPU pinning**: NOT REQUIRED — this is file I/O only. The script does no linear algebra. Use `OMP_NUM_THREADS=8` at script head per CPU-fallback rule (no numpy work either; harmless).
>
> **Output files**:
> - `sessions/permanent-results-registry.md` — 17 NEW rows appended.
> - `computations/s86_w1a_t1_perm_land_17.json` — JSON map `{gate_stem: {audit_sha256, content_sha256, vii_slot, source_line_number_in_s85_verdicts}}` for each of the 17 entries.
> - `computations/s86_gate_verdicts.txt` — append canonical verdict line + companion row.
>
> **Cross-checks**:
> 1. Every `audit_sha256` and `content_sha256` is exactly 64 hex characters (regex `^[0-9a-f]{64}$`).
> 2. Each appended registry row references a §VII slot that already exists in the registry (slots §VII.K-PROP, §VII.K-META, §VII.B, §VII.P all exist as of S85 close per `session-86-context.md` §0 file inventory).
> 3. No duplicate registry row (grep the registry for the gate-stem before appending — registry write is idempotent: re-running does not create duplicates).
> 4. The script's input-pin map is `{s85_verdicts_path, registry_path, 17_gate_stems_list}`; closure SHA = sha256 of canonical-form-serialized input-pin map. Verdict's `audit_sha256` MUST be the closure SHA, not a copy of any input file's SHA (per `gate-verdicts.md` rule).
>
> **Substitution chain** (§10 below) is the extraction algorithm; the script implements it line-for-line.

**7. Machinery pin (PRDR)**:
- Registry slot identifiers: `§VII.K-PROP`, `§VII.K-META`, `§VII.B`, `§VII.P` (all pre-existing per S85-close registry inventory)
- Source-cite SHA: `computations/s85_gate_verdicts.txt` content SHA at S85-close (computed at runtime; pinned in script's input-pin map)
- Schema version: R3 (per `_yaml_gate_validator.py` requirement; gate block in this plan carries `schema_version: R3` token below)
- Tolerance rule: THEOREM (exact match — every SHA character must transcribe verbatim; partial transcription = FAIL)
- L_max for each underlying PASS: as recorded in the verdict line being transcribed (T1 does not re-pick L_max)
- Random seed: N/A (no stochastic computation)
- GPU path: N/A (file I/O only)

```yaml
schema_version: R3
gate_id: S86-W0-PERM-LAND-17
trigger: VERIFY
classification: META
machinery_pin_map:
  s85_verdicts_path: "computations/s85_gate_verdicts.txt"
  registry_path: "sessions/permanent-results-registry.md"
  gate_stems_list_count: 17
  vii_slots_used: ["§VII.K-PROP", "§VII.K-META", "§VII.B", "§VII.P"]
  tolerance_rule: THEOREM
  L_max: per-row (as recorded in source verdict line)
  random_seed: NA
  gpu_path: NA
```

**8. Expected output 4-tuple**: `(value=17, scheme=registry_landing, convention=64-char-dual-SHA, L_max=N/A)` — the single integer value reports the count of rows successfully appended.

**9. PASS / FAIL / INFO thresholds**:
- **PASS**: All 17 entries appended to `sessions/permanent-results-registry.md` with full 64-character `audit_sha256` AND `content_sha256` AND correct §VII slot. Cross-check 1-4 in §6 above all pass.
- **FAIL**: Any entry has SHA shorter than 64 hex chars; OR any entry references a §VII slot that does not exist; OR any entry duplicates an existing row; OR the script's audit_sha256 in the verdict line is a copy of an input file's SHA rather than the closure SHA.
- **INFO**: 1-16 of 17 entries succeed; the failing entries are itemized in the verdict-line `value` field as `value=<N_landed>/17 missing=[<gate-stem-list>]`. Tolerance rule THEOREM-class — no INFO band on per-row exact-transcription; INFO is only for partial completion.

**10. Substitution chain (= extraction algorithm)**:

```
Step 1 (definition):
  V         = open(s85_verdicts_path).read()
  L         = V.splitlines()
  STEMS     = [list of 17 gate-ID stems from §6 table]
  SLOTS     = [list of 17 §VII slot strings from §6 table]
  registry  = open(registry_path)

Step 2 (substitute — for each i ∈ 0..16):
  stem_i    = STEMS[i]
  slot_i    = SLOTS[i]
  line_i    = first line in L where line.startswith(stem_i + ":") AND "PASS" in line
  audit_i   = regex extract "audit_sha256=([0-9a-f]+)" from line_i, group(1)
  content_i = regex extract "content_sha256=([0-9a-f]+)" from line_i, group(1)

Step 3 (simplify — assertions per i):
  assert len(audit_i)   == 64
  assert len(content_i) == 64
  assert slot_i in registry.read()

Step 4 (direction — write):
  if all 17 assertions pass:
      for each i, append registry row "| {slot_i} | {stem_i} | {one_liner_i} | {audit_i} | {content_i} | session=85 |"
      verdict = PASS, value=17
  elif 1 <= N_pass <= 16:
      verdict = INFO, value=N_pass + missing list
  else:
      verdict = FAIL with offending stems enumerated

Conclusion: PASS iff all 17 transcriptions succeed verbatim with full 64-char dual-SHA at the cited §VII slot.
```

**11. What PASSES / FAILS MEAN for solution space**:
- **PASS** establishes `sessions/permanent-results-registry.md` as the canonical citation source for these 17 W0-W5 theorem-grade PASSes. Downstream gates in S86-S100+ that depend on (e.g.) the cluster-span identity (CC-5) cite it as `permanent-results-registry §VII.K-PROP, audit=<full-64>, content=<full-64>` rather than referencing the verdict file directly. The verdict file is a session artifact; the registry is permanent. PASS makes 17 walls of the solution space registry-anchored.
- **FAIL** means at least one of the 17 underlying PASSes' provenance chain (compute-script SHA → verdict-line SHA → registry-row SHA) is broken. The physics result is unaffected — S85's PASS verdict stands. But future agents querying the registry for one of the 17 will find no entry, and may either rederive (wasteful) or cite the verdict file directly (dangerous: verdict files get superseded; the registry does not).
- **INFO** means partial landing — N rows landed, 17-N missing. The next session's W0 wave carries forward the missing rows as a registry-completion follow-up (not a re-derivation).

**12. Effort estimate**: 2 hours mechanical (file scan + 17 regex extractions + 17 registry-row writes + 17 cross-check assertions + 1 verdict line + 1 companion row).

**13. Substrate-framing reminder**: The 17 PASSes describe walls in the spectral-triple solution space (cluster-span identities are algebraic identities of f_conv-class observables; Dai-Freed torsions are KO-theory invariants of D_K; KO-6 sign flows are RG-stable structural data; two-layer obstructions are categorical statements about regulator-class composition). T1 is META hygiene that pins those walls to the canonical registry. None of the 17 are phononic excitations; all 17 are GEOMETRIC content of the spectral triple (D_K, J, π).

---

## §W1a-2. S86-VII-R-NCG-META-THEOREM-LANDING (= C3)

**1. Gate ID**: `S86-VII-R-NCG-META-THEOREM-LANDING`

**2. Trigger**: `[VERIFY-THEOREM]` — verify that the 3-signed Meta-Theorem statement, the 7 status rows, and the 3-axis disjointness table appear in §VII.R verbatim from the cited sources (lizzi 9A §6.8 B-1 + gen-physicist 9A §4.4). The substitution chain in §10 below is the proof skeleton of the disjointness claim.

**3. Classification**: GEOMETRIC — the Meta-Theorem operates on the spectral-triple's regulator-class structural floor (per `session-86-context.md` §1.5). It declares which classes of NCG-derived observables are structurally excluded from physical realization. This is geometry of the regulator atlas, not phononic content.

**4. Agent type**: `connes-ncg-theorist` (NCG-Meta registry slot at §VII.R; per `.claude/agents/connes-ncg-theorist.md` §VII.R is the explicit Connes registry-slot domain). NOT gen-physicist (per partition §1 W1a-2 specialist assignment).

**5. Hypothesis (one sentence)**: T2 is a single registry-write gate that lands the NCG-Structural-Exclusion Meta-Theorem at §VII.R; it is cited from TWO synthesis families (lizzi 9A §6.8 B-1 + gen-physicist 9A §4.4 as C3) but constitutes ONE registry artifact per closeout §7.1 substitution chain (the dedup is recorded in partition §3 line `T2 = C3 dedup ... = -1`). The Meta-Theorem absorbs three prior structural-exclusion results — W10-114 parity-exclusion, S82 W2-3 rank-exclusion, and the lizzi S-1 Mellin-support lift — into a single 3-axis disjointness statement, which the registry row formalizes as a §VII.R table.

**6. Method — COMPLETE dispatch prompt**:

> Spawn `connes-ncg-theorist` with the following compute-mode brief.
>
> **Read first**: `sessions/permanent-results-registry.md` (full file; chunked Read with `limit=400`) + `sessions/session-plan/session-86-context.md` §1.5 (regulator-class structural floor) + `computations/s85_gate_verdicts.txt` lines 38-46 (W2-3 HP^3 disjoint corridor PASS) and the W11-3 NCG meta-exclusion PASS (grep stem `S85-W11-3`).
>
> **Write target**: `sessions/permanent-results-registry.md` — open NEW slot §VII.V below the existing §VII.Q section. Layout:
>
> ```markdown
> ### §VII.R — NCG-Structural-Exclusion Meta-Theorem (3-signed: vdd / connes / lizzi)
>
> **Statement**: Let A = (A, H, D, J, γ) be the canonical Connes-Chamseddine spectral triple
> on M_4 × SU(3) at the Jensen-deformed Dirac operator D_K. For any candidate observable
> O derivable from A by a regulated trace `Tr f(D_K^2 / Λ²)`, O is structurally excluded
> from physical realization on M_4 × SU(3) iff at least one of the three independent
> exclusion axes (parity, rank, Mellin-support) carries the value FORBIDDEN for O. The
> three axes are independent (their pairwise intersection on the regulator-class atlas
> is empty); their union exhausts the W11-3 NEW-FAMILY closure of structural-exclusion
> results.
>
> **Signers**: vdd (van den Dungen), connes (Connes), lizzi (Lizzi). Per 1D 3-solo
> agreement at S85 close.
>
> **Status table** (7 rows, one per absorbed result):
>
> | Absorbed result | Source session | Source verdict-line SHA | Axis | Status under Meta-Theorem |
> |:----------------|:---------------|:------------------------|:-----|:-------------------------|
> | W10-114 parity-exclusion (FI_parity_exclusion = 1) | S84 W10 + S85 W11-4 | <audit_sha256 from S85 W11-4> | parity | ABSORBED — categorical instance |
> | S82 W2-3 rank-exclusion (rank_exclusion = 3) | S82 + S85 W2-3 | 5da67e5a5def4b5514d715bc13f168ac45df5b3660bf40a23aa8b358a6c0db5f | rank | ABSORBED — categorical instance |
> | lizzi S-1 Mellin-support lift (F_4 vs M partition) | S85 W0-W5 (lizzi S-1) | <CF-LZ-S86-1 source SHA> | Mellin-support | ABSORBED — Lizzi-track sibling |
> | W11-3 NCG-STRUCTURAL-EXCLUSION META-THEOREM | S85 W11-3 | <audit_sha256 from S85 W11-3> | (mother) | LANDED — this row IS the parent |
> | w_0 CS-asymmetry NEW-FAMILY slot | (reserved) | (pending S86+) | (NEW) | OPEN — slot reserved per closeout §6.4 |
> | HP^3 corridor disjointness (W2-3) | S85 W2-3 | 5da67e5a5def4b5514d715bc13f168ac45df5b3660bf40a23aa8b358a6c0db5f | rank | INSTANCE of rank-axis |
> | Quantum disjoint corridor 4-route (W2-6) | S85 W2-6 | <audit_sha256 from S85 W2-6> | rank | INSTANCE of rank-axis (q-deformed) |
>
> **3-axis disjointness table** (for any observable O on the 5-regulator atlas {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}):
>
> | Axis | Definition (per `session-86-context.md` §1.5) | Independent of (other axes) | FORBIDDEN value rules-out |
> |:-----|:----------------------------------------------|:----------------------------|:--------------------------|
> | parity | Z/2 grading data on the spectral triple (per W10-114, FI_parity_exclusion = 1) | rank, Mellin-support | Observables whose KO-6 sign cannot be made consistent with γ-action |
> | rank | Spin(N) embedding rank of O's source representation (per S82 W2-3, rank_exclusion = 3) | parity, Mellin-support | Observables requiring rank ≠ rank(SU(3)) = 2 |
> | Mellin-support | F_4 vs M family membership of the regulator class (per lizzi S-1 lift) | parity, rank | Observables on M = {cutoff_sqrt, anomaly} when F_4 = {ζ, Zubarev, SDW} support is required |
>
> **Cross-pair note (routes to §VII.S)**: The 6-Φ-branch Perturbative-Ledger Immunization
> Family at §VII.S is the corollary structure of this Meta-Theorem under the additional
> assumption that O is a perturbative-ledger observable (per IEP §3.1 INTENSIVE/EXTENSIVE
> partition). The chronological-collision between §VII.R (NCG-Meta) and §VII.S
> (Immunization Family) is resolved per closeout §5.7: §VII.R is the parent (3-axis
> structural floor), §VII.S is the child (perturbative-ledger restriction); both land
> at S86 W1a but §VII.R is read first by downstream gates.
>
> **Audit SHAs** (this row): audit_sha256=<computed by `s86_w1a_t2_vii_r_meta_landing.py`>, content_sha256=<computed>.
> ```
>
> **Producing script**: `computations/s86_w1a_t2_vii_r_meta_landing.py`. The script:
> 1. Loads `s85_gate_verdicts.txt`.
> 2. Greps for `S85-W11-3`, `S85-W2-3`, `S85-W2-6`, `S85-W11-4` (the 4 W6-W13 + W0-W5 PASSes that supply absorbed-result audit_sha256 fields).
> 3. Loads `session-86-context.md` §1.5 to confirm the 3-axis names verbatim.
> 4. Constructs the §VII.R block above (Markdown text), substituting the 4 grep-extracted SHAs into the status table.
> 5. Appends the block to `sessions/permanent-results-registry.md`.
> 6. Computes its own `audit_sha256` = sha256 of the input-pin map (s85_verdicts content SHA + context-file content SHA + registry path + section identifier "§VII.R") and `content_sha256` = sha256 of the appended block text.
> 7. Emits the verdict line + companion row.
>
> **GPU pinning**: NOT REQUIRED — file I/O only. Use `OMP_NUM_THREADS=8` at script head.
>
> **Output files**:
> - `sessions/permanent-results-registry.md` — §VII.R block appended.
> - `computations/s86_w1a_t2_vii_r_meta_landing.json` — block content + 4 absorbed-result SHAs + computed audit/content SHAs.
> - `computations/s86_gate_verdicts.txt` — verdict line + companion.
>
> **Cross-checks**:
> 1. §VII.R does not pre-exist in the registry (registry is append-once at this slot).
> 2. The 4 absorbed-result SHAs all extract as full 64-char hex from the verdict file.
> 3. The 3-axis names (parity / rank / Mellin-support) in the disjointness table match `session-86-context.md` §1.5 substring-for-substring.
> 4. The cross-pair note explicitly references §VII.S (forward reference; §VII.S landed in T3 of this same wave).
> 5. The "Signers" line names exactly 3 signers (vdd, connes, lizzi) per closeout 1D 3-solo.

**7. Machinery pin (PRDR)**:
- Registry slot identifier: `§VII.R` (NEW slot — must not pre-exist)
- Source-cite SHAs: 4 verdict-line audit_sha256 values (S85 W11-3, W2-3, W2-6, W11-4) — extracted at runtime from `s85_gate_verdicts.txt`
- Schema version: R3
- Tolerance rule: THEOREM (exact substring match for axis names + signer names + status-row layout)
- L_max: N/A (Meta-Theorem is L_max-independent by construction; the 3 axes are categorical, not scale-dependent)
- Random seed: N/A
- GPU path: N/A

```yaml
schema_version: R3
gate_id: S86-VII-R-NCG-META-THEOREM-LANDING
trigger: VERIFY-THEOREM
classification: GEOMETRIC
machinery_pin_map:
  registry_path: "sessions/permanent-results-registry.md"
  vii_slot: "§VII.V"
  source_verdict_path: "computations/s85_gate_verdicts.txt"
  source_context_path: "sessions/session-plan/session-86-context.md"
  absorbed_result_stems: ["S85-W11-3", "S85-W2-3", "S85-W2-6", "S85-W11-4"]
  signers: ["vdd", "connes", "lizzi"]
  three_axes: ["parity", "rank", "Mellin-support"]
  tolerance_rule: THEOREM
  L_max: NA
  random_seed: NA
  gpu_path: NA
```

**8. Expected output 4-tuple**: `(value=<sha256 of §VII.R block text>, scheme=registry_landing, convention=64-char-dual-SHA, L_max=N/A)`.

**9. PASS / FAIL / INFO thresholds**:
- **PASS**: §VII.R block exists in registry with all 5 elements: (a) 3-signed statement, (b) 7 status rows table, (c) 3-axis disjointness table, (d) cross-pair note to §VII.S, (e) audit_sha256 + content_sha256 line. All cross-checks 1-5 in §6 pass.
- **FAIL**: Any of (a)-(e) absent; OR §VII.R already exists (write would be duplicate); OR any of the 4 absorbed-result SHAs not full 64 hex; OR axis names mismatch §1.5; OR signer count ≠ 3.
- **INFO**: Block written but cross-pair note to §VII.S references a slot that does not yet exist (because T3 has not run yet). This is sequencing-conditional INFO — clears to PASS once T3 lands §VII.S.

**10. Substitution chain (= proof skeleton of the 3-axis disjointness claim, registered verbatim)**:

```
Step 1 (definition):
  Let A = (A, H, D_K, J, γ) be the canonical Connes-Chamseddine spectral triple on
                M_4 × SU(3) at Jensen deformation tau in [0, tau_fold].
  Let O be a candidate observable O = Tr f(D_K² / Λ²) for some f ∈ Schwartz class.
  Let X_par   ⊂ Reg(A) be the regulator subset such that O respects KO-6 parity.
      X_rank  ⊂ Reg(A) be the regulator subset such that rank(image(O)) = rank(SU(3)).
      X_Mell  ⊂ Reg(A) be the regulator subset such that O ∈ F_4 family
                                       (per lizzi S-1 Mellin-support lift).

Step 2 (substitute — claim of disjointness):
  Define the structural-exclusion set
      X_excluded = Reg(A) \ (X_par ∩ X_rank ∩ X_Mell).
  By W10-114, the parity-exclusion at FI_parity_exclusion=1 establishes
      X_par^c ⊂ X_excluded.
  By S82 W2-3, the rank-exclusion at rank_exclusion=3 establishes
      X_rank^c ⊂ X_excluded.
  By lizzi S-1, the Mellin-support lift establishes
      X_Mell^c ⊂ X_excluded.

Step 3 (simplify — independence claim):
  Claim: X_par^c ∩ X_rank^c ∩ X_Mell^c = ∅ over the 5-regulator atlas
                                              {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}.
  Empirical witness: W12-4 5-regulator atlas shows a_0/a_2/a_4 spread (0.50, 1.03, 0.49)
  partitions into F_4 (per Mellin-support) without any regulator class lying in
  more than one exclusion axis simultaneously (per W11-3 status table).

Step 4 (direction — pairwise independence):
  Therefore X_excluded = X_par^c ∪ X_rank^c ∪ X_Mell^c (union, not intersection;
  exclusion is satisfied by ANY axis carrying FORBIDDEN).
  The three axes are PAIRWISE INDEPENDENT: pairwise intersection on the 5-regulator
  atlas is empty (per Step 3 empirical witness via W12-4).
  Direction conclusion: An observable O is structurally admissible iff it lies in
                        X_par ∩ X_rank ∩ X_Mell — i.e. it satisfies all three axes
                        simultaneously.

Conclusion: The structural-exclusion classification is fully determined by the
            3-axis labelling {parity, rank, Mellin-support}, and the union of
            exclusions defines the W11-3 NEW-FAMILY closure.
```

**11. What PASSES / FAILS MEAN for solution space**:
- **PASS** establishes §VII.R as the canonical citation for any future S86+ gate that argues "O is structurally excluded by NCG axiom X". Three pre-existing exclusion results (W10-114 parity, S82 W2-3 rank, lizzi S-1 Mellin-support) become cited corollaries of one parent. The reservation of a NEW-FAMILY slot for w_0 CS-asymmetry (per closeout §6.4) preserves room for future axes. PASS makes the regulator-class structural floor explicit and registry-anchored.
- **FAIL** means downstream NCG-exclusion arguments must continue to cite three separate sessions (S82 + S84 + S85 W11-3) instead of one §VII.R — increased citation cost, increased risk of inconsistency between citations.
- **INFO** (sequencing-conditional) means §VII.R lands but the cross-pair note's §VII.S reference is pending; clears to PASS once T3 completes within W1a.

**12. Effort estimate**: 1.5 hours (read context + read 4 verdict lines + draft 5-element block + write + verify cross-checks + emit verdict).

**13. Substrate-framing reminder**: §VII.R describes a wall in the spectral-triple solution space — specifically, the 3-axis structural floor of the regulator atlas. The Meta-Theorem is GEOMETRIC content of the substrate, not a phononic excitation. It tells us which spectral-functional choices are structurally admissible at the NCG level, before any phononic dynamics is computed on top of them.

---

## §W1a-3. S86-VII-S-PERTURBATIVE-LEDGER-IMMUNIZATION-FAMILY-LANDING

**1. Gate ID**: `S86-VII-S-PERTURBATIVE-LEDGER-IMMUNIZATION-FAMILY-LANDING`

**2. Trigger**: `[VERIFY-THEOREM]` — verify that the 6 Φ-branch slots Φ-A through Φ-F land in §VII.S verbatim from lizzi 9A §6.8(B-2) + gen-physicist 9A §4.3 (1C synthesis), and that each carries an IEP class tag (T4 sets the tags; T3 creates the slots).

**3. Classification**: GEOMETRIC — the Immunization Family is the corollary structure of the §VII.R Meta-Theorem under restriction to perturbative-ledger observables. Each Φ-branch describes a class of spectral observable that is immune to a specific perturbation (lattice spacing, Weyl rescaling, etc.) by virtue of its position in the §VII.R 3-axis classification. This is geometry of the regulator-restricted observable algebra, not phononic content.

**4. Agent type**: `connes-ncg-theorist` (parallel registry-landing for §VII.S; same specialist as T2 for consistent §VII slot management). NOT gen-physicist (per partition §1 W1a-3 specialist assignment).

**5. Hypothesis (one sentence)**: T3 lands the parent of the Perturbative-Ledger Immunization Family at §VII.S, instantiating six Φ-branch slots (Φ-A through Φ-F) per the 1C 6-branch enumeration in lizzi 9A §6.8(B-2); each Φ-branch slot is created with an empty IEP tag that T4 fills, and with corollary references to the §VII.S sub-gates landed elsewhere (C-η, C-θ already in W1c via C41; C-α in W6 via C40; C-γ-WEAK in W6 via C42; C-δ/ε/ζ/ι deferred to S87).

**6. Method — COMPLETE dispatch prompt**:

> Spawn `connes-ncg-theorist` with the following compute-mode brief.
>
> **Read first**: `sessions/permanent-results-registry.md` (full file; chunked Read) + `sessions/session-plan/session-86-context.md` §1.5 (regulator-class structural floor, F_4 vs M partition).
>
> **Write target**: `sessions/permanent-results-registry.md` — open NEW slot §VII.S below §VII.V (which T2 lands). Layout:
>
> ```markdown
> ### §VII.S — Perturbative-Ledger Immunization Family (parent + 6 Φ-branches)
>
> **Parent statement**: Let O be a perturbative-ledger observable on the spectral triple A
> (Connes-Chamseddine perturbative ledger: trace-class operators in Tr f(D_K² / Λ²)
> with f ∈ Schwartz, expanded as a finite-order heat-kernel sum). O is IMMUNIZED
> against a perturbation P iff (a) O lies entirely within X_par ∩ X_rank ∩ X_Mell
> (per §VII.R), AND (b) P acts as the identity on at least one of the three axes
> respected by O.
>
> **Routing note**: §VII.S is the perturbative-ledger restriction of the §VII.R
> Meta-Theorem. Cross-reference §VII.R for the parent statement; §VII.S corollaries
> below specialize it.
>
> **Six Φ-branch slots** (cascade enumeration; IEP tags filled by T4):
>
> | Slot | Branch label | Perturbation immunized against | Source synthesis | IEP class tag (T4 fills) | Corollary gates |
> |:-----|:-------------|:-------------------------------|:------------------|:-------------------------|:----------------|
> | Φ-A | LATTICE-SPACING | Discretization scheme (Wilson, Symanzik, etc.) | lizzi 9A §6.8 B-2 / gen-physicist §4.3 (1C C-α) | EXTENSIVE (T4) | C40 (W6) |
> | Φ-B | UV-CUTOFF-CHOICE | Choice of UV regulator within F_4 family | lizzi 9A §6.8 B-2 (1C C-β) | INTENSIVE (T4) | (deferred S87) |
> | Φ-C | WEYL-RESCALING | Conformal rescaling of g_M | lizzi 9A §6.8 B-2 / gen-physicist §4.3 (1C C-γ-WEAK) | EXTENSIVE (T4) | C42 (W6, weak form) |
> | Φ-D | INNER-FLUCTUATION | Connes inner-fluctuation perturbation A → A + ω | lizzi 9A §6.8 B-2 / W1c C41 (1C C-θ) | INTENSIVE (T4) | C41 (W1c, zero-compute) |
> | Φ-E | WARD-IDENTITY | [J, D_K] = 0 Ward identity preservation | lizzi 9A §6.8 B-2 / W1c C41 (1C C-η) | INTENSIVE (T4) | C41 (W1c, zero-compute) |
> | Φ-F | RG-FLOW-INVARIANCE | One-loop RG flow direction preservation | lizzi 9A §6.8 B-2 (1C C-ι) | EXTENSIVE (T4) | (deferred S87) |
>
> **Audit SHAs** (this parent + 6 slots): audit_sha256=<computed by `s86_w1a_t3_vii_s_immunization_landing.py`>, content_sha256=<computed>.
> ```
>
> **Producing script**: `computations/s86_w1a_t3_vii_s_immunization_landing.py`. The script:
> 1. Reads `session-86-context.md` §1.5 + §1.4 (the F_4 / M partition + the 4A elimination bulletin enumerations) to verify the 6-branch enumeration matches the synthesis count.
> 2. Reads `sessions/permanent-results-registry.md` to confirm §VII.S does not pre-exist + §VII.R IS now present (cross-check that T2 has run within the same wave dispatch).
> 3. Constructs the §VII.S block above (Markdown text), with IEP tag column populated by T4-anticipated values from lizzi 9A §6.8(B-3) (T3 fills the column with the projected tags; T4 verifies by re-running the partition rule and asserting equality).
> 4. Appends the block.
> 5. Computes audit + content SHAs and emits the verdict line + companion.
>
> **GPU pinning**: NOT REQUIRED — file I/O. `OMP_NUM_THREADS=8`.
>
> **Output files**:
> - `sessions/permanent-results-registry.md` — §VII.S block appended.
> - `computations/s86_w1a_t3_vii_s_immunization_landing.json` — 6-branch enumeration + IEP-projected tags + corollary-gate cross-references.
> - `computations/s86_gate_verdicts.txt` — verdict + companion.
>
> **Cross-checks**:
> 1. §VII.S does not pre-exist; §VII.R DOES pre-exist (T2 ran first within W1a per dispatcher ordering).
> 2. Exactly 6 Φ-branch slots, labelled Φ-A through Φ-F (no more, no less; per 1C 6-branch enumeration).
> 3. Each Φ-branch slot has all 5 columns populated (label / perturbation / source / IEP-projected / corollary).
> 4. Corollary-gate cross-references resolve: C40 + C42 are W6 plan items; C41 is a W1c plan item; deferred slots cite S87 explicitly.
> 5. Parent statement cites §VII.R for routing.

**7. Machinery pin (PRDR)**:
- Registry slot: `§VII.S` (NEW; must not pre-exist)
- Prerequisite slot: `§VII.R` (must exist; created by T2 earlier in the same wave)
- 6-branch enumeration count: exactly 6
- Branch labels: Φ-A, Φ-B, Φ-C, Φ-D, Φ-E, Φ-F
- IEP-projected tag map: {Φ-A: EXTENSIVE, Φ-B: INTENSIVE, Φ-C: EXTENSIVE, Φ-D: INTENSIVE, Φ-E: INTENSIVE, Φ-F: EXTENSIVE} (T4 verifies)
- Schema version: R3
- Tolerance rule: THEOREM (exact match on slot count + label spelling + cross-reference resolution)
- L_max: N/A
- Random seed: N/A
- GPU path: N/A

```yaml
schema_version: R3
gate_id: S86-VII-S-PERTURBATIVE-LEDGER-IMMUNIZATION-FAMILY-LANDING
trigger: VERIFY-THEOREM
classification: GEOMETRIC
machinery_pin_map:
  registry_path: "sessions/permanent-results-registry.md"
  vii_slot: "§VII.S"
  prerequisite_slot: "§VII.V"
  branch_count: 6
  branch_labels: ["Φ-A", "Φ-B", "Φ-C", "Φ-D", "Φ-E", "Φ-F"]
  iep_projected_map:
    Φ-A: EXTENSIVE
    Φ-B: INTENSIVE
    Φ-C: EXTENSIVE
    Φ-D: INTENSIVE
    Φ-E: INTENSIVE
    Φ-F: EXTENSIVE
  source_synthesis: "lizzi 9A §6.8 B-2 + gen-physicist 9A §4.3"
  tolerance_rule: THEOREM
  L_max: NA
  random_seed: NA
  gpu_path: NA
```

**8. Expected output 4-tuple**: `(value=<sha256 of §VII.S block text>, scheme=registry_landing, convention=64-char-dual-SHA, L_max=N/A)`.

**9. PASS / FAIL / INFO thresholds**:
- **PASS**: §VII.S parent statement + 6 Φ-branch slots present, all 5 columns populated, all corollary cross-references resolve, parent statement routes to §VII.R, IEP-projected tags match T4-anticipated values.
- **FAIL**: Slot count ≠ 6; OR any branch label misspelled; OR §VII.R not present (T2 didn't run); OR §VII.S already exists; OR corollary cross-reference (C40 / C41 / C42) not present in any plan.
- **INFO**: 5/6 branches landed (e.g. one corollary cross-reference unresolved); enumerate the missing branch in `value` field. T4 still runs over the 5 landed branches (annotates IEP tags); the 6th carried forward.

**10. Substitution chain (= proof skeleton of the parent statement)**:

```
Step 1 (definition):
  Let O ∈ Tr f(D_K²/Λ²) be a perturbative-ledger observable (Schwartz f, finite-order
                                                              heat-kernel expansion).
  Let P be a perturbation acting on (A, H, D_K, J, γ): e.g. lattice discretization,
                                                            UV-cutoff change,
                                                            Weyl rescaling g → e^{2σ} g,
                                                            Connes inner fluctuation A → A+ω,
                                                            Ward-identity action [J, D_K],
                                                            RG flow.
  Define O is IMMUNIZED against P iff P[O] = O exactly on some 3-axis sub-set respected by O.

Step 2 (substitute — restriction of §VII.R):
  By §VII.R, O is structurally admissible iff O ∈ X_par ∩ X_rank ∩ X_Mell.
  Restrict to perturbative-ledger O: same axes apply.

Step 3 (simplify — branch enumeration):
  For each P, identify which axis P preserves on the perturbative-ledger:
    Φ-A LATTICE-SPACING:    preserves rank-axis (lattice scheme is rank-blind).
    Φ-B UV-CUTOFF:          preserves Mellin-support axis within F_4 family.
    Φ-C WEYL-RESCALING:     preserves rank-axis (rescaling is rank-blind to leading order).
    Φ-D INNER-FLUCTUATION:  preserves Ward axis ([J, D_K]=0 stable under A → A+ω).
    Φ-E WARD-IDENTITY:      preserves all three axes by [J, D_K]=0 directly.
    Φ-F RG-FLOW:            preserves Mellin-support axis on the F_4 family.

Step 4 (direction — IEP partition):
  By IEP §3.1: a Φ-branch is INTENSIVE iff its preserved axis is per-mode (Mellin-support
  per individual eigenvalue → ζ-class observables; Ward identity per fiber);
  EXTENSIVE iff its preserved axis is mode-summed (lattice spacing affects total a_n;
  Weyl rescaling rescales total volume; RG flow runs total coupling).
  Therefore IEP map: {Φ-B, Φ-D, Φ-E} INTENSIVE; {Φ-A, Φ-C, Φ-F} EXTENSIVE.

Conclusion: 6 Φ-branches partition the perturbative-ledger immunization structure
            into 3 INTENSIVE + 3 EXTENSIVE classes; T4 annotates each branch with its tag.
```

**11. What PASSES / FAILS MEAN for solution space**:
- **PASS** establishes §VII.S as the canonical citation for any future S86+ gate arguing "O is immunized against perturbation P". Six perturbation classes (lattice, UV, Weyl, inner-fluctuation, Ward, RG) become unified under one parent statement with explicit IEP partition. This closes the corollary cascade of W10-114 (which previously stood as an isolated parity-exclusion result) by routing it as a 3-axis instance.
- **FAIL** means the perturbative-ledger immunization arguments scattered across S77 / S82 / S85 remain uncorrelated — each future immunization argument must be re-derived from first principles rather than cited from §VII.S.
- **INFO** (5/6 case) means a single Φ-branch's corollary gate (e.g. C40 in W6) has not been authored yet; T4 still runs on the 5 landed branches; the missing branch becomes a W6 carry-forward.

**12. Effort estimate**: 1.5 hours (read context + draft parent statement + draft 6-branch table with all 5 columns + write + cross-check resolution + verdict).

**13. Substrate-framing reminder**: §VII.S describes a corollary structure on the spectral-triple solution space — the perturbative-ledger restriction of §VII.R's 3-axis structural floor. Each Φ-branch is a wall in the regulator-restricted observable algebra, telling us which observables survive which perturbations. This is GEOMETRIC content of the substrate: which spectral functionals are immune to which deformations. No phononic excitation is computed; the result is structural geometry.

---

## §W1a-4. S86-VII-R-IEP-ANNOTATION

**1. Gate ID**: `S86-VII-R-IEP-ANNOTATION`

**2. Trigger**: `[VERIFY]` — verify that each of §VII.S Φ-A through Φ-F carries an explicit INTENSIVE or EXTENSIVE tag per IEP §3.1, and that the assignment matches the partition rule in lizzi 9A §6.8(B-3) + 1C OQ11. Note: this gate edits the §VII.S table column "IEP class tag" (which T3 left as a placeholder); it does NOT edit §VII.R itself despite the gate-name prefix `VII-R-IEP-ANNOTATION` (per partition §1 W1a item 4 verbatim wording — the IEP framework was originated in §VII.R's Meta-Theorem context and is named after that origin, but the annotation target is §VII.S). Naming is a closeout artifact; the runtime semantics are §VII.S annotation.

**3. Classification**: META — registry hygiene (column-fill on existing §VII.S table). The IEP partition itself is GEOMETRIC content (it classifies regulator-restricted observable algebra by per-mode vs mode-summed structure), but T4's specific action is hygiene: filling the IEP-tag column with values that T3 already projected.

**4. Agent type**: `lizzi-spectral-functional-theorist` (IEP is Lizzi-originated framework per lizzi 9A §6.8 B-3 + 1C OQ11; partition rule is in his synthesis). At RUNTIME (not plan-write time), the planner-runner blacklist does not apply per `.claude/skills/rclab-coordinate.md` runtime selection rules — content fit governs at compute, agent-isolation governs at plan. NOT gen-physicist.

**5. Hypothesis (one sentence)**: For each Φ-branch slot in §VII.S, the IEP class tag (INTENSIVE or EXTENSIVE) is determined by the partition rule of IEP §3.1: a Φ-branch is INTENSIVE iff its preserved axis is per-mode, EXTENSIVE iff its preserved axis is mode-summed; the resulting tag map is {Φ-A: EXTENSIVE, Φ-B: INTENSIVE, Φ-C: EXTENSIVE, Φ-D: INTENSIVE, Φ-E: INTENSIVE, Φ-F: EXTENSIVE} per the §W1a-3 §10 substitution chain Step 4.

**6. Method — COMPLETE dispatch prompt**:

> Spawn `lizzi-spectral-functional-theorist` with the following compute-mode brief.
>
> **Read first**: `sessions/permanent-results-registry.md` §VII.S block (which T3 just landed) + `sessions/session-plan/session-86-context.md` §1.5 + (if T4 has independent access) lizzi 9A §6.8(B-3) for the IEP §3.1 partition rule canonical text.
>
> **Write target**: `sessions/permanent-results-registry.md` — edit §VII.S table column 5 ("IEP class tag (T4 fills)") for each of 6 rows.
>
> **Producing script**: `computations/s86_w1a_t4_iep_annotation.py`. The script:
> 1. Loads `sessions/permanent-results-registry.md`.
> 2. Locates the §VII.S block (greps for "### §VII.S — Perturbative-Ledger Immunization Family").
> 3. For each of 6 Φ-branch rows, applies the IEP §3.1 partition rule:
>    - INTENSIVE iff preserved axis is per-mode (per-eigenvalue, per-fiber).
>    - EXTENSIVE iff preserved axis is mode-summed (total spectral weight, total volume).
> 4. Verifies the result against T3's projected map (must agree exactly; if disagree, FAIL the gate and flag a partition-rule misalignment between T3 (connes-ncg-theorist projection) and T4 (lizzi-spectral-functional-theorist application)).
> 5. Edits the §VII.S table to replace the placeholder text "(T4 fills)" with the verified tag.
> 6. Computes audit + content SHAs and emits verdict.
>
> **Partition rule application table** (the 6 derivations T4 must reproduce):
>
> | Branch | Preserved axis (per T3 §10 Step 3) | Per-mode or mode-summed? | IEP tag |
> |:-------|:------------------------------------|:-------------------------|:--------|
> | Φ-A LATTICE-SPACING | rank-axis (lattice scheme is rank-blind) | mode-summed (lattice affects total a_n) | EXTENSIVE |
> | Φ-B UV-CUTOFF | Mellin-support within F_4 | per-mode (Mellin-support per eigenvalue → ζ-class observables) | INTENSIVE |
> | Φ-C WEYL-RESCALING | rank-axis (rank-blind to leading order) | mode-summed (rescales total volume) | EXTENSIVE |
> | Φ-D INNER-FLUCTUATION | Ward axis (stable under A → A+ω) | per-mode (per-fiber Connes ω) | INTENSIVE |
> | Φ-E WARD-IDENTITY | all three axes ([J, D_K]=0 directly) | per-mode ([J, D_K]=0 holds per-eigenvalue) | INTENSIVE |
> | Φ-F RG-FLOW | Mellin-support on F_4 | mode-summed (RG runs total coupling) | EXTENSIVE |
>
> **GPU pinning**: NOT REQUIRED. `OMP_NUM_THREADS=8`.
>
> **Output files**:
> - `sessions/permanent-results-registry.md` — §VII.S table column 5 edited (6 rows).
> - `computations/s86_w1a_t4_iep_annotation.json` — 6-row partition-rule application table + agreement check vs T3 projection.
> - `computations/s86_gate_verdicts.txt` — verdict + companion.
>
> **Cross-checks**:
> 1. §VII.S exists in registry (T3 ran).
> 2. Exactly 6 Φ-branch rows present.
> 3. T4-derived tag map matches T3-projected tag map exactly (both produce {Φ-A: E, Φ-B: I, Φ-C: E, Φ-D: I, Φ-E: I, Φ-F: E}).
> 4. After edit, no row carries the placeholder "(T4 fills)" anymore.
> 5. Partition is balanced (3 INTENSIVE + 3 EXTENSIVE), consistent with the 3-axis structural floor's symmetric per-mode / mode-summed split.

**7. Machinery pin (PRDR)**:
- Registry slot: `§VII.S` (must exist; T3 created it earlier in the same wave)
- Branch count to annotate: 6
- IEP §3.1 partition rule: per-mode → INTENSIVE; mode-summed → EXTENSIVE
- T3-projected tag map (cross-check target): {Φ-A: EXTENSIVE, Φ-B: INTENSIVE, Φ-C: EXTENSIVE, Φ-D: INTENSIVE, Φ-E: INTENSIVE, Φ-F: EXTENSIVE}
- Schema version: R3
- Tolerance rule: THEOREM (exact map agreement T3 vs T4)
- L_max: N/A
- Random seed: N/A
- GPU path: N/A

```yaml
schema_version: R3
gate_id: S86-VII-R-IEP-ANNOTATION
trigger: VERIFY
classification: META
machinery_pin_map:
  registry_path: "sessions/permanent-results-registry.md"
  vii_slot_target: "§VII.S"
  branch_count_to_annotate: 6
  iep_partition_rule: "per-mode→INTENSIVE; mode-summed→EXTENSIVE per IEP §3.1"
  expected_tag_map:
    Φ-A: EXTENSIVE
    Φ-B: INTENSIVE
    Φ-C: EXTENSIVE
    Φ-D: INTENSIVE
    Φ-E: INTENSIVE
    Φ-F: EXTENSIVE
  expected_balance: "3 INTENSIVE + 3 EXTENSIVE"
  tolerance_rule: THEOREM
  L_max: NA
  random_seed: NA
  gpu_path: NA
```

**8. Expected output 4-tuple**: `(value=6, scheme=registry_landing, convention=64-char-dual-SHA, L_max=N/A)` — the integer reports the count of Φ-branches annotated.

**9. PASS / FAIL / INFO thresholds**:
- **PASS**: All 6 Φ-branches in §VII.S carry an explicit INTENSIVE or EXTENSIVE tag; the tag map matches T3's projection exactly; partition is balanced (3+3); no row carries the "(T4 fills)" placeholder.
- **FAIL**: Any row untagged; OR any tag mismatches T3's projection (this would indicate a partition-rule misalignment requiring a §VII.S re-render); OR partition imbalance (e.g. 4+2 or 5+1) suggesting a derivation error in §6 application table.
- **INFO**: 5/6 annotated and one row's preserved axis is ambiguous between per-mode and mode-summed (genuine IEP §3.1 boundary case); record the ambiguous branch as `value="5_annotated_1_boundary" branch=<label>` and carry forward to a S87 IEP §3.1 refinement.

**10. Substitution chain (= proof skeleton of the partition rule application)**:

```
Step 1 (definition):
  IEP §3.1 partition rule:
      A perturbative-ledger Φ-branch is INTENSIVE iff its preserved axis is per-mode
                                                     (per-eigenvalue / per-fiber).
      A perturbative-ledger Φ-branch is EXTENSIVE iff its preserved axis is mode-summed
                                                     (total a_n / total volume / total coupling).

Step 2 (substitute — for each branch i ∈ {A, B, C, D, E, F}):
  axis_i      = T3 §10 Step 3 preserved axis for branch i
  scope_i     = "per-mode" if axis_i acts per-eigenvalue/per-fiber else "mode-summed"
  tag_i       = INTENSIVE if scope_i == "per-mode" else EXTENSIVE

Step 3 (simplify — enumerate):
  Φ-A: axis=rank,            scope=mode-summed (lattice → total a_n),       tag=EXTENSIVE
  Φ-B: axis=Mellin-support,  scope=per-mode (per-eigenvalue Mellin),         tag=INTENSIVE
  Φ-C: axis=rank,            scope=mode-summed (Weyl → total volume),        tag=EXTENSIVE
  Φ-D: axis=Ward,            scope=per-mode (per-fiber Connes ω),            tag=INTENSIVE
  Φ-E: axis=all-three,       scope=per-mode ([J, D_K]=0 per-eigenvalue),     tag=INTENSIVE
  Φ-F: axis=Mellin-support,  scope=mode-summed (RG runs total coupling),     tag=EXTENSIVE

Step 4 (direction):
  Tag map = {A: E, B: I, C: E, D: I, E: I, F: E}.
  Balance: 3 INTENSIVE + 3 EXTENSIVE.
  This matches T3's projection exactly (cross-check 3 above).

Conclusion: T4's IEP §3.1 application reproduces T3's projection; §VII.S table column 5
            populates with the verified tags; partition is balanced.
```

**11. What PASSES / FAILS MEAN for solution space**:
- **PASS** completes the §VII.S landing — every Φ-branch is now classified by IEP class, enabling future S86+ gates to query the registry for "all INTENSIVE Φ-branches" or "all EXTENSIVE Φ-branches" when reasoning about per-mode vs mode-summed observables. The 3+3 balance also confirms the IEP partition is structurally non-trivial (not all branches collapse to one class).
- **FAIL** means T3 + T4 disagree on the partition rule application — this is a serious structural alarm requiring re-render of §VII.S and re-validation of the IEP §3.1 statement itself. Likely cause: ambiguous "preserved axis" identification in T3's §10 Step 3 enumeration. Remediation: rerun T3 with explicit per-axis derivation, then T4 with the corrected projection.
- **INFO** (5/6 case) means a genuine IEP §3.1 boundary case exists — the partition rule needs refinement. This becomes a S87 carry-forward to lizzi (the IEP §3.1 owner) for rule-clarification.

**12. Effort estimate**: 0.5 hours (re-derive 6 IEP tags from T3 §10 Step 3 + edit table column 5 + cross-check vs T3 projection + verdict).

**13. Substrate-framing reminder**: T4's IEP annotation describes a META-classification of the perturbative-ledger immunization structure (§VII.S) — it tags which Φ-branches preserve per-mode (intensive) versus mode-summed (extensive) spectral-functional content. The IEP partition itself is GEOMETRIC content of the substrate's regulator-restricted observable algebra (per-mode = per-eigenvalue of D_K = per-vibrational-mode of the substrate; mode-summed = total spectral weight = aggregate observable). T4's specific action is hygiene (filling table cells), but the partition it applies is structural.

---

## §X. Wave W1a → Downstream Decision Point

W1a's outputs feed two downstream waves at compute time:

1. **T2 (§VII.R landing) → W7 C1 `S86-JOINT-CC-RESIDUE-COMPUTE`**: W7's joint CC residue across phonon-first / transit / landau sectors (1A 3-solo) routes any "structurally excluded" sector via §VII.R citation rather than a duplicated 3-axis re-derivation. W7 must wait for W1a T2 PASS before recording its routing-condition pin in `s86_gate_verdicts.txt`.

2. **T3 (§VII.S landing) → W6 C2-cascade**:
   - **C40 `S86-LATTICE-SPACING-IMMUNIZATION-CANDIDATE`** instantiates Φ-A — slot must exist (T3) and be tagged EXTENSIVE (T4) before C40 can cite §VII.S.A.
   - **C42 `S86-WEYL-RESCALING-IMMUNIZATION-WEAK-FORM`** instantiates Φ-C — slot must exist and be tagged EXTENSIVE.
   - **C2 umbrella** (W6) cites the §VII.S parent + 6 Φ-branch enumeration verbatim.

Both downstream paths are pinned by the dispatch prompt's `prerequisite_slot` machinery field. If W7 / W6 dispatch before W1a verdict appears in `s86_gate_verdicts.txt`, the dispatched runner emits `INFO -- value="prereq-pending"` and parks; the orchestrator re-dispatches once W1a closes.

---

## §0.10. Wave W1a Machinery-Enumeration Pin

Per the PRDR rule (`.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness), every gate-relevant free parameter is enumerated and pinned. Wave W1a's free parameters (consolidated across all 4 gates):

| Parameter | Gate(s) | Pinned value | Tag |
|:----------|:--------|:-------------|:----|
| `s85_verdicts_path` | T1 | `computations/s85_gate_verdicts.txt` | infrastructure |
| `registry_path` | T1, T2, T3, T4 | `sessions/permanent-results-registry.md` | infrastructure |
| `context_path` | T2, T3 | `sessions/session-plan/session-86-context.md` | infrastructure |
| `gate_stems_list` (T1) | T1 | 17 stems per §6 table | content-derived |
| `vii_slot_T1` | T1 | per-row from §6 table | content-derived |
| `vii_slot_T2` | T2 | `§VII.R` | content-derived |
| `vii_slot_T3` | T3 | `§VII.S` | content-derived |
| `branch_labels` | T3, T4 | `[Φ-A, Φ-B, Φ-C, Φ-D, Φ-E, Φ-F]` | content-derived |
| `signers` | T2 | `[vdd, connes, lizzi]` | source-derived (1D 3-solo) |
| `three_axes` | T2 | `[parity, rank, Mellin-support]` | source-derived (§1.5) |
| `iep_partition_rule` | T4 | per-mode → INTENSIVE; mode-summed → EXTENSIVE per IEP §3.1 | source-derived |
| `iep_expected_tag_map` | T3, T4 | {Φ-A: E, Φ-B: I, Φ-C: E, Φ-D: I, Φ-E: I, Φ-F: E} | derived (T3 §10 Step 4) |
| `tolerance_rule` | T1, T2, T3, T4 | THEOREM (exact-match, no INFO band on per-row transcription) | gate-class |
| `schema_version` | T1, T2, T3, T4 | R3 | rule-derived (R3 YAML) |
| `L_max` | all four | N/A (registry / META landings have no L_max) | gate-class |
| `random_seed` | all four | N/A | gate-class |
| `gpu_path` | all four | N/A (file I/O only; OMP_NUM_THREADS=8 fallback per CPU-rule) | gate-class |

**PRDR cardinality check**: 16 free parameters identified, 16 pinned. D_PRU_raw = 0 for W1a.

---

## §0.11. Wave W1a Input-SHA Ledger

| Input | Used by | SHA pin source | Pin time |
|:------|:--------|:---------------|:---------|
| `computations/s85_gate_verdicts.txt` (S85 verdict ledger) | T1 (extracts 17 dual-SHAs); T2 (extracts 4 absorbed-result SHAs) | content_sha256 computed at T1/T2 script invocation | runtime (script first 20 lines log it per `gate-verdicts.md` rule) |
| `sessions/permanent-results-registry.md` | T1, T2, T3, T4 (read for slot existence; write for new rows / blocks) | content_sha256 computed at script invocation (pre-edit baseline) | runtime |
| `sessions/session-plan/session-86-context.md` | T2 (cites §1.5 axis names verbatim); T3 (cites §1.4 + §1.5 enumerations) | content_sha256 computed at script invocation | runtime |
| `sessions/session-plan/session-86-partition.md` (this manifest) | All gate blocks (cite §1 W1a item N for source spec) | content_sha256 computed at plan-write (this file) | this plan's audit_sha256 = sha256 of the Markdown text below the §0 header |
| Closeout citation B-1 / B-2 / B-3 (lizzi 9A §6.8) | T2 (B-1), T3 (B-2), T4 (B-3) | NOT a runtime input — citation only; the closeout content was already deduplicated into `session-86-context.md` | source-of-record (no runtime SHA — citation by named subsection) |
| Closeout citation gen-physicist 9A §4.3 | T3 | NOT a runtime input — citation only | source-of-record |
| Closeout citation gen-physicist 9A §4.4 | T2 (= C3 dedup) | NOT a runtime input — citation only | source-of-record |
| Closeout citation 1C OQ11 | T4 | NOT a runtime input — citation only | source-of-record |

The 17 W0-W5 PASS-line audit_sha256 values for T1 are extracted at runtime from `s85_gate_verdicts.txt` (the file is the canonical source-of-record; copying SHAs into this plan would create a stale duplicate). One verified extraction is reproduced here as a sanity anchor:
- `S85-W5-7-TWO-LAYER-OBSTRUCTION` (line 169 of `s85_gate_verdicts.txt`): `audit_sha256=f8c8f56630a347192a627a0699714a03fc3c9d9d249835807f0f77c4fc235d4c` `content_sha256=2b979d69f6a57c13b38337f5dda4d52aa07debc2ccbd6857b3cb00ba9d591fec` (verified 64 hex each).

---

**End of Wave W1a plan.** Ready for `/rclab-coordinate --wave w1a` dispatch (compute mode) once W0a R5 + W0b R7 + W0c C17 prerequisites land in `computations/s86_gate_verdicts.txt`.

<!-- §VII-SLOT-RECONCILE-2026-04-26: w1a T2 reservation rewritten §VII.R → §VII.V; landed slot remains §VII.R per registry header (immutable). -->
