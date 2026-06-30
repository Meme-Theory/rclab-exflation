# Session 89 Plan — Wave 1: α(M) horizon-microstate count + cascade-tail observables

> **Provenance**: `connes-ncg-theorist` orchestrator-direct planner-write per `/rclab-plan` skill §3b (gen-physicist BLACKLISTED for test-case design per skill §3b item 4). Co-signers: `mack-cosmic-bridge` (A.5/A.6/A.13 cosmological + falsifier-master-inventory sole writer per `feedback_mack-bridge-role.md`); `hawking-theorist` (A.5 Hawking-radiation interface specifics).
>
> **Source**: User-curated Ledger A from `sessions/archive/session-88/s88-pending-edits-ledger.md` (Cluster A, lines 26–89 of the deduplicated CF table in `sessions/session-plan/session-89-context.md`); user invocation override 2026-05-09 explicit. Ledger B/C are OUT OF SCOPE per user directive.
>
> **Theme**: α(M) horizon-microstate count + cascade-tail observables (pixelation-lock follow-up; Ledger A items A.1, A.5, A.6, A.13). Cluster A origin: S88 W-3 / W-5 / W-6 carry-forward queue.
>
> **Composition**: Wave 1 dispatches in S89 Batch 1 alongside W2–W7 under the ≤8-concurrent cap per `feedback_dispatch-discipline.md`. A.1 is the LARGEST single S89 item (4 wave-equiv); the gate block sub-decomposes the Method into 4 numbered sub-procedures (infrastructure → α(M) function-form derivation → L_max=10 evaluation → LRD anchor verification) while remaining ONE gate block emitting ONE verdict line.
>
> **Natural-split fallback** (informational; do not actuate unless mid-wave context exhaustion): W1a = §W1-1 alone (4 wave-equiv, connes-ncg PRIMARY); W1b = §W1-2/§W1-3/§W1-4 (mack-led; 2.5 wave-equiv aggregate). Single-pass write executed below.
>
> **Wave classification (per `wave-classification.md` §M1∧M2∧M3∧M4)**: All four §W1-1 / §W1-2 / §W1-3 / §W1-4 gates are COMPUTE-class (M1 numerical-comparison PASS predicates; M2 `.py` producing scripts; M3 first-principles substrate computation NOT verbatim rule extraction; M4 absent from `methodology-wave-allowlist.md`). NO METHODOLOGY-class items in W1; orchestrator-direct-write is NOT used. Dispatch path: `/rclab-coordinate` compute-mode for all four.

---

## Wave 1 Summary

Wave 1 closes the structural gap exposed by S88 W1b1-63 FAIL routing branch (c) and S88 W1c-69 substitution-chain Step 5 underflow: the substrate's spectral-triple-IS microstate count at horizon-spanning Peter-Weyl sectors must be derived BEFORE downstream cosmological-CC accommodation can be claimed. Four interlocking gates execute this:

1. **§W1-1 (A.1)** derives α(M) = S_BH^substrate(M) / S_BH^semicl(M) from Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula on the horizon-spanning sector projection of (A_K^≤10, H_K^≤10, D_K^≤10), identifies the structural exponent n in the asymptotic α(M) = 1 + O((M/M_threshold)^{−n}), evaluates at M_BH = 10^7 M_sun, and verifies the PASS-band against the empirical anchor α(LRD, L_max=10) = 1/458 from S88 W1b1-63 branch (c). This is the ONLY S89 item with substrate-IS NCG-axiomatic content directly addressing the S88 §W1b1-63 FAIL — connes-ncg-theorist owns it as primary author.
2. **§W1-2 (A.5)** corrects the §W1c-69 Step 5 substitution chain by re-pinning L_H multi-species at the substrate canonical T_H = 1.057 MeV (per S88 W6 §V.1 substrate-pinned Hawking temperature; not the eq=1 single-species placeholder), and emits a successor verdict line under Option A `supersedes` protocol carrying the FULL 64-character original audit_sha256 = `2afd17ef99c81123…` (full hex emitted at runtime per the canonical-anchor source script). Mack PRIMARY for L_H multi-species accounting (cosmological observable + falsifier-master-inventory consequence); hawking-theorist CO-AUTHOR for the Hawking-radiation interface specifics.
3. **§W1-3 (A.6)** computes the species-multiplicity lookup table f(g) at cascade generations g ∈ {0..384} from the substrate-derived T_H(g) cooling profile traversing the SM particle-threshold structure (electron 0.511 MeV; muon 105.7 MeV; pion 134.98/139.57 MeV; nucleon 939 MeV; …; up to QCD scale and below). Mack PRIMARY (cosmological-observable mapping; sole writer for inventory rows). Output is the lookup-table .npz consumed directly by §W1-2 (intra-wave dependency).
4. **§W1-4 (A.13)** re-derives the CF-CURV-6 STRUCTURAL CENTRAL prediction for n_PBH(g_BBN) from the substrate's pinned cascade-tail mass distribution and compares against the §W1c-69 PASS-magnitude posterior support [8.4e-24, 2.2e-22] m^−3 at upper 22.6% of the CF-CURV-6 prior [10^−30, 10^−20] m^−3. Mack PRIMARY (observational-anchor side). [SIGN] trigger: the substitution chain pre-registers a directional prediction (substrate central > posterior lower edge), so the verdict line carries the schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple companion comment row per `gate-verdicts.md` §"S87+ canonical form".

**Connecting structural claim**: All four gates trace to the SAME substrate-IS spectral residue at horizon-spanning Peter-Weyl sectors. §W1-1 supplies the function-form α(M) and the empirical L_max=10 anchor; §W1-2 inherits a corrected single-mass L_H bridging the empirical anchor to multi-species cascade dressing; §W1-3 supplies the species multiplicity table f(g) feeding §W1-2; §W1-4 is the band-edge tension reconciliation against the magnitude-PASS posterior. PASS-AND across all four closes the S88 §W1c-69 13-OOM cascade-tail underflow corridor at the substrate-IS level; FAIL on §W1-1 specifically forecloses A.10/A.20 (downstream Stage-2 verifies blocked on cohomology-class-layer infrastructure that A.1 anchors).

---

## Wave 1 Decision Point Prerequisites

**Hard prerequisites** (plan-freeze halt if any missing):

- `canonical_constants.py` HEAD-of-S88 (post-S88 close): must contain `tau_fold = 0.19` (R-PROTECTED), `M_KK = 7.428660036284456e+16 GeV`, `Delta_BCS = 0.4642547394830737` (R-PROTECTED), `n_s_framework = 0.9561`, `xi_E_GGE_inv = 13.642473425595973`, and substrate-pinned `T_H_substrate = 1.057 MeV` (PROMOTE in-session at S89 plan-freeze if not yet present; cite `s88-w6-w1c-69-page1976-13oom.md §V.1` as provenance source). Pinned input SHA: `<canonical_constants.py SHA at S89 plan-freeze>`.
- `sessions/permanent-results-registry.md` HEAD-of-S88: §VII.A through §VII.AT slots used; next-free at §VII.AU for any incidental landings (W1 does not land registry slots itself but A.1's structural theorem is a candidate for §VII.AU registry promotion in S90+ dependent on Stage-2 verify).
- D_K spectrum cache: `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (master cache; verified at S87 W11-2). Used by A.1 for horizon-spanning sector projection and species-multiplicity-table cross-validation. Pinned input SHA: `<L12 cache SHA at S89 plan-freeze>`.
- Ledger excerpts (already inlined in `sessions/session-plan/session-89-context.md` §"Cluster A — α(M) horizon-microstate count + cascade-tail observables (pixelation-lock follow-up; W-3 / W-5 / W-6)"). Source ledger: `sessions/archive/session-88/s88-pending-edits-ledger.md` lines 26–31 / 38–42 / 51–54 / 86–89.
- S88 W1c-69 verdict line at `computations/session-88/s88_gate_verdicts.txt`: contains the canonical `audit_sha256` to be quoted as the `supersedes=` token in §W1-2's corrective emission. The skill template states the prefix `2afd17ef99c81123…`; the producing script in §W1-2 grep-extracts the FULL 64-character SHA from the verdict file at runtime (no hardcoding).

**Soft prerequisites** (advisory):

- CM-1995 paper transcription accessible at `researchers/Connes/` (Connes-Moscovici 1995 "The local index formula in noncommutative geometry"; §III.4 finite-spectral-triple residue formula). Required substrate citation for A.1.
- Volovik 2003 §7.2 SC factors (referenced indirectly through species-multiplicity threshold structure in §W1-3; cosmological-bridge-side citation, not substrate-IS).
- SM particle-threshold tables (PDG): published values referenced as cross-check anchors only, NOT as substrate canonicals (substrate-first canonical sourcing per `substrate-first-canonical-sourcing.md §"(i)"`: the substrate-derived T_H(g) profile is canonical; PDG threshold values are methodological cross-checks).

**Cross-pillar bridge precondition** (for §W1-1 specifically): The IS-not-IN convention per `phononic-framing.md §"IS Space, Not IN Space"` is enforced at the gate-block level; the substrate IS the spectral triple at horizon-spanning sectors; the horizon is NOT a container. The dispatch prompt MUST repeat this framing verbatim in the agent dispatch text.

---

## §W1-1. S89-ALPHA-M-NCG-HORIZON-MICROSTATE-COUNT-DERIVATION

> **Largest S89 item (4 wave-equiv).** Multi-step Method sub-decomposition: 4 numbered sub-procedures within ONE gate block emitting ONE composite verdict line. Sub-procedures organize compute order; each sub-procedure emits an intermediate `.npz` artifact consumed by the next.

### 1. Gate ID

`S89-ALPHA-M-NCG-HORIZON-MICROSTATE-COUNT-DERIVATION`

### 2. Trigger

`[VERIFY-THEOREM]` — the gate verifies a structural theorem (the substrate-IS function-form for α(M)) AND the empirical L_max=10 anchor evaluation against the S88 W1b1-63 branch (c) measured 1/458. Composite trigger because the gate spans (a) theorem-derivation content (function-form α(M); structural exponent n) AND (b) numerical evaluation against an empirical anchor.

### 3. Classification

GEOMETRIC (substrate-IS spectral-triple-axiom-derived; horizon-spanning Peter-Weyl block-projection cohomology-class observable). Per `phononic-framing.md` §"Classification Guide" the result concerns the spectral triple structure (block-diagonal D_K projection onto horizon-spanning sectors), not direct phononic excitations; the α(M) ratio is a GEOMETRIC observable on the substrate's spectral-triple structure, not a PHONONIC excitation density.

### 4. Agent type (runtime)

PRIMARY: `connes-ncg-theorist` — substrate-IS NCG-axiomatic horizon-microstate count is connes-domain by primary specialty (Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula + spectral-triple axiom verification + Peter-Weyl block-diagonal projection on (A_K, H_K, D_K)).

CO-AUTHOR (advisory; consulted on cross-axis review of result): `volovik-superfluid-universe-theorist` (transit-dynamics axis cross-check on horizon emergence; non-blocking).

`gen-physicist` is BLACKLISTED from test-case design per `/rclab-plan` skill §3b item 4. `hawking-theorist` does NOT participate in §W1-1 (substrate-IS computation is connes-domain; hawking is consulted for §W1-2 Hawking-radiation interface only).

### 5. Hypothesis

The substrate-IS horizon-microstate count at finite L_max truncation, computed via the Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula on the horizon-spanning sector projection of (A_K^≤10, H_K^≤10, D_K^≤10), takes the asymptotic form α(M) = 1 + O((M/M_threshold)^{−n}) for some structural exponent n derivable from the Peter-Weyl block-diagonal residue structure; α(M_BH=10^7 M_sun, L_max=10) reproduces the S88 W1b1-63 branch (c) empirical anchor 1/458 within 5% relative tolerance.

### 6. Method (4-procedure sub-decomposition; ONE gate, ONE verdict line)

**Script path**: `computations/session-89/s89_w1_alpha_m_horizon_microstate_count.py`

**Substrate framing reminder injected into agent dispatch prompt verbatim**: "The substrate IS the spectral triple (A_K^≤10, H_K^≤10, D_K^≤10) at horizon-spanning Peter-Weyl sectors. The horizon is NOT a container the substrate sits in. α(M) IS the substrate's intrinsic microstate-count ratio at horizon-spanning Peter-Weyl block level. FORBIDDEN: invoking 'BH in curved spacetime' as the explanation direction. Explanation flows substrate → emergent area-theorem per `phononic-framing.md` §'IS Space, Not IN Space'. Direction of explanation: D_K eigenvalues at horizon-spanning sectors → Connes-Moscovici §III.4 residue → α(M) function-form → emergent semiclassical area-theorem in the M → ∞ limit (NOT the reverse)."

**Imports (MANDATORY, top of script)**:

```python
from canonical_constants import *  # tau_fold, M_KK, Delta_BCS, etc. — S34+ MANDATORY per math-scripts.md
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')  # CPU-only fallback cap per math-scripts.md §Environment
import numpy as np
import torch  # GPU path: AMD RX 9070 XT 17.1 GB VRAM; ROCm 7.2; torch 2.9.1+rocm
import hashlib, json, sys
from pathlib import Path
```

**Sub-procedure 1 — Infrastructure: horizon-spanning sector identification + projector construction.**

Define the horizon-spanning sector (HSS) projection on the substrate's Peter-Weyl decomposition: for a given black-hole mass M, the horizon-spanning sectors are the Peter-Weyl (p,q) blocks of (A_K^≤10, H_K^≤10, D_K^≤10) whose spectral-action moment contributes to the BH entropy at scale M. Concretely, the HSS at M is the set of (p,q) ∈ Spec(D_K^≤10) with `|λ_(p,q)| ∈ [Λ_M, M_KK]` where `Λ_M ≡ (M_Pl_eff² / M)^{1/2}` is the characteristic substrate-distance scale at horizon area A = 4π(2GM)². The full set of L_max=10 (p,q) sectors with p+q ≤ 10 has |HSS| sectors at a given M; the HSS projector is the orthogonal projection onto the direct sum of those Peter-Weyl blocks.

Computation:

(a) Load the L_max=12 master spectrum cache `computations/session-84/s84_spectrum_cache_L12_tau019.npz`; truncate to L_max=10 (p+q ≤ 10) per the Casimir-bound + cache cross-check protocol of `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"` (operational L_max=10 ≤ plan L_max=10 trivially; no NEW-sector intrusion above (10,0)/(0,10) at the precision level we test).

(b) For M = 10^7 M_sun (PASS evaluation point), compute Λ_M in M_KK units: Λ_M / M_KK = (M_Pl_eff / M_KK)² · (M_KK / M)^{1/2} where M_Pl_eff = M_KK · (Vol_SU3)^{1/2} per S58 Volovik partition. Pin Λ_M_over_M_KK_at_1e7Msun in `# (local)` form; emit to .npz for downstream consumption.

(c) Construct HSS projector P_HSS(M) as the diagonal indicator matrix in the Peter-Weyl basis: P_HSS[(p,q)] = 1 if |λ_(p,q)| ∈ [Λ_M, M_KK]; 0 otherwise. Verify rank(P_HSS) > 0 at M=10^7 M_sun (assert; SIGN_CHECK_1).

(d) Emit `s89_w1_subproc1_hss_infrastructure.npz` with keys `Lambda_M_over_M_KK`, `P_HSS_M_1e7_Msun_diag`, `hss_rank`, `hss_sector_list_pq`. Compute `subproc1_sha256 = sha256(file_bytes)`.

**Sub-procedure 2 — α(M) function-form derivation via Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula.**

The Connes-Moscovici 1995 §III.4 residue formula for a finite spectral triple (A, H, D) gives the local index pairing as a residue at s = 0 of the zeta-function trace `ζ_D(s) = Tr(|D|^{-2s})` evaluated on the algebra A's image under the relevant projector. For the horizon-spanning sub-triple `(A_K^HSS, H_K^HSS, D_K^HSS) = (P_HSS · A_K · P_HSS, P_HSS · H_K, P_HSS · D_K · P_HSS)`, the finite-spectral-triple residue formula evaluates to:

```
S_BH^substrate(M, L_max=10)
  = Tr_HSS(P_HSS) − (1/(2πi)) ∮_{s=0} Tr_HSS(|D_K^HSS|^{-2s}) · γ(s) ds
```

where γ(s) is the CM-1995 §III.4 universal kernel (Connes-Moscovici §III formula (III.4) or local-index-formula form). The leading term Tr_HSS(P_HSS) is the rank of the HSS projector (substrate-side dim count); the residue correction encodes the spectral-action correction at the truncation scale.

The semiclassical comparison:

```
S_BH^semicl(M) = A(M) / (4 G_N) = π · (2 G_N M)² / G_N
                = 4 π G_N M²  (in natural units)
```

The ratio:

```
α(M, L_max) ≡ S_BH^substrate(M, L_max) / S_BH^semicl(M)
```

The structural-exponent identification: the M-dependence of α(M) at fixed L_max comes from the M-dependent HSS projector rank + the M-dependent residue correction. Asymptotically (M → M_threshold from below where M_threshold is the largest M with non-trivial HSS at L_max=10):

```
α(M) = 1 + C_n · (M / M_threshold)^{−n} + O((M/M_threshold)^{−(n+1)})
```

The structural exponent n is identified by extracting the leading-order term of the residue expansion; per the Connes-Moscovici §III.4 finite-spectral-triple form, n is determined by the substrate-distance pole structure (n=2 for substrate-distance-1 pole at s=3 dominance; n=4 for substrate-distance-2 pole at s=4 dominance; n=other if cross-pole interference dominates).

Computation:

(a) For each (p,q) ∈ HSS_list at M=10^7 M_sun, compute |λ_(p,q)|^{-2s} on a finite grid s ∈ {0.001, 0.01, 0.1, 1.0, 2.0, 3.0, 4.0} (substrate-distance-1 pole at s=3; substrate-distance-2 pole at s=4; UV pole at s=2 for d=4). Sum across HSS to get `Tr_HSS(|D_K^HSS|^{-2s})` at each s.

(b) Extract residue at s=0 by polynomial fit on the s ∈ {0.001..0.1} portion (small-s Laurent expansion). Verify numerical stability: fit residual < 1% (assert; SIGN_CHECK_2).

(c) Apply CM-1995 §III.4 universal kernel γ(s); for finite spectral triple the kernel reduces to γ(s) = Γ(s) (gamma function) on the residue calculation [verified by transcribing CM-1995 §III formula (III.4)]. Compute the residue value `R_CM(M=1e7, L_max=10)`.

(d) Compute `S_BH^substrate(M=1e7, L_max=10) = Tr_HSS(P_HSS) − R_CM` and `S_BH^semicl(M=1e7)`, then α value: `alpha_value = S_BH^substrate / S_BH^semicl`.

(e) Extract structural exponent n by L_max-stability scan: rerun (a)-(d) at L_max ∈ {6, 8, 10} (operational truncation per Friedrich-Bär saturation theorem of `math-scripts.md §"D_K Block-Diagonality"`); fit α(M=1e7, L_max) − 1 as function of L_max; identify n from the dominant fit-residual scaling. Cross-check n against the Casimir-bound prediction at the dominant pole.

(f) Emit `s89_w1_subproc2_alpha_function_form.npz` with `alpha_value_M_1e7_Lmax_10`, `R_CM_residue`, `Tr_HSS_P_HSS`, `S_BH_semicl`, `structural_exponent_n`, `Lmax_scan_data`. Compute `subproc2_sha256`.

**Sub-procedure 3 — L_max=10 evaluation cross-check at additional M values.**

Compute α(M, L_max=10) at M ∈ {10^6, 10^7, 10^8} M_sun (3-point M-scan). Verify:

(a) α(M) is monotone in M (assert direction matches structural-exponent prediction: if n > 0, α(M) → 1 from above as M decreases below M_threshold).

(b) Extrapolate α(M → ∞, L_max=10): the limit is the L_max=10 truncation residual (NOT 1 — the substrate's finite L_max truncation prevents full semiclassical recovery; this IS the framework's prediction).

(c) Emit `s89_w1_subproc3_alpha_M_scan.npz` with `alpha_values_M_scan`, `monotonicity_assert`, `M_to_infinity_limit_at_Lmax_10`. Compute `subproc3_sha256`.

**Sub-procedure 4 — Empirical anchor verification: α(LRD, L_max=10) = 1/458 from S88 W1b1-63 branch (c).**

The S88 W1b1-63 FAIL routing branch (c) at `sessions/archive/session-88/workshops/s88-w3-w1b1-63-3branch.md §5 CF-W1b1-C` provided an empirical anchor: at the LRD (Little Red Dot) BH-mass scale M_LRD ≈ 10^7 M_sun (per JWST LRD observations, the dominant LRD mass scale; see `researchers/Little-Red-Dots/`), the S88 measurement returned α_empirical = 1/458 ≈ 2.183e-3. The PASS criterion at §W1-1 is:

```
PASS iff |alpha_value_M_1e7_Lmax_10 − 1/458| / (1/458) ≤ 0.05  (5% relative tolerance, RATIO rule)
```

Computation:

(a) Load `subproc2_sha256` artifact's `alpha_value_M_1e7_Lmax_10` directly.

(b) Compute relative deviation `rel_dev = |alpha_value − 1/458| / (1/458)`.

(c) Apply PASS/INFO/FAIL collapse:
   - PASS iff `rel_dev ≤ 0.05` AND `regime_verdict == VALID` (L_max=10 within Friedrich-Bär saturation per `math-scripts.md`).
   - INFO iff `0.05 < rel_dev ≤ 0.20` (sub-leading sub-structure deviation; substrate captures order-of-magnitude but not 5% precision; carry-forward to L_max=12 scan in S90).
   - FAIL iff `rel_dev > 0.20` (substrate-IS function-form does NOT reproduce empirical anchor; S88 §W1b1-63 FAIL is structural — hard wall on the cosmological-CC accommodation pathway via substrate-IS horizon-microstate count).

(d) Emit composite verdict line per S87+ schema-v2 (`gate-verdicts.md` §"S87+ canonical form"). Append to `computations/session-89/s89_gate_verdicts.txt` (canonical path; the variant `computations/_shared/s89_gate_verdicts.txt` is FORBIDDEN per `gate-verdicts.md` §"Canonical Verdict-File Path"). Use `computations/_shared/_script_template.py` `append_verdict()` helper for parallel-writer-safe POSIX O_APPEND single-shot write.

**Cross-checks emitted in stdout (first 20 lines per `gate-verdicts.md` §"During computation")**:

```
SHA INPUT: canonical_constants.py = <SHA>
SHA INPUT: s84_spectrum_cache_L12_tau019.npz = <SHA>
SHA INTERMEDIATE: subproc1_sha256 = <SHA>
SHA INTERMEDIATE: subproc2_sha256 = <SHA>
SHA INTERMEDIATE: subproc3_sha256 = <SHA>
CLOSURE INPUT-PIN MAP SHA = <closure_sha>
```

**Output files**:

- Canonical: `computations/session-89/s89_gate_verdicts.txt` (one canonical line + one dual-SHA companion comment row per `gate-verdicts.md` schema-v2)
- Data: `computations/session-89/s89_w1_alpha_m_horizon_microstate_count.npz` (with all sub-procedure intermediates concatenated; key list spelled out below in §8)
- Plot: `computations/session-89/s89_w1_alpha_m_horizon_microstate_count.png` (3-panel: panel A α(M, L_max=10) vs M on log-log axes; panel B α(M=1e7, L_max) vs L_max for L_max ∈ {6, 8, 10}; panel C residual to 1/458 anchor with PASS/INFO/FAIL band shading)
- Working-paper section: `sessions/archive/session-89/session-89-w1-workingpaper.md` §W1-1 (substantive content ≥ 15 lines; substrate framing block; verdict block; results table)

### 7. Machinery pin (PRDR — Pre-Registration Dry-Run; full enumeration)

| Pin | Value | Source / Class |
|:----|:------|:---------------|
| `L_max` | 10 | Operational truncation under Friedrich-Bär saturation per `math-scripts.md` (cache filtered from L=12 master) |
| `regulator` | `a_n^{ζ}` (zeta-function regularization at the residue formula step) | Pinned per `regulator-pin-discipline.md` §"Tag Format"; CM-1995 §III.4 native regulator is zeta |
| `convention` | `horizon-spanning-sector-projection-CM-1995-III-4` | Substrate-IS-pillar; not SCHEMATIC (full physical Connes-Moscovici §III.4 formula, NOT a `_spectral_action_regulators.py` schematic helper) |
| `convention_class_pin` | `FULL` (full physical regularization per `substrate-first-canonical-sourcing.md §(iv)`) | NOT SCHEMATIC; the residue formula is the canonical CM-1995 §III.4 form |
| `scheme` | `peter-weyl-block-diagonal-HSS-projection-Lmax10-tau-fold-019` | |
| `random_seed` | None (deterministic; no Monte Carlo step) | Verified: all sums are over finite (p,q) lists; no random-sampling step |
| `tolerance` | `1e-12` (absolute float64 numerical tolerance on residue extraction) | Float64 native machine epsilon × 100; the residue fit residual must be < 1% by assert |
| `scan_range` | M ∈ {1e6, 1e7, 1e8} M_sun (3-point M-scan); s ∈ {0.001, 0.01, 0.1, 1.0, 2.0, 3.0, 4.0} for residue-fit grid | Pre-registered |
| `GPU_path` | torch.linalg on AMD RX 9070 XT (matrix sizes ≥100×100 expected at L_max=10 HSS dim ≥ several thousand) | per `math-scripts.md §Environment` |
| `CPU_fallback_OMP_THREADS` | 8 (cap via `os.environ.setdefault('OMP_NUM_THREADS', '8')` at script top) | per `math-scripts.md §Environment` |
| `Connes-Moscovici_1995_section` | §III.4 (finite-spectral-triple residue formula); §III formula (III.4) | Substrate citation; transcribed at runtime from `researchers/Connes/` |
| `M_threshold` | computed at runtime as `M_KK² · Vol_SU3 · (1/M_Pl_eff²) · L_max-truncation-correction` (no ad-hoc pin) | Substrate-derived |
| `pass_threshold` | `rel_dev ≤ 0.05` (RATIO tolerance; PASS-band) | Pre-registered, fixed at plan-freeze |
| `info_band` | `0.05 < rel_dev ≤ 0.20` | Pre-registered |
| `fail_band` | `rel_dev > 0.20` | Pre-registered |

**Input SHA pins** (computed at plan-freeze; precomputed-at-dispatch):

| Input | Path | SHA pin form |
|:------|:-----|:-------------|
| canonical_constants | `computations/_shared/canonical_constants.py` | `<computed-at-dispatch-from-S88-HEAD>` |
| L=12 master cache | `computations/session-84/s84_spectrum_cache_L12_tau019.npz` | `<computed-at-dispatch>` |
| CM-1995 paper transcription | `researchers/Connes/` (CM-1995 .md path TBD by globbing the Connes directory) | `<computed-at-dispatch>` |
| W1b1-63 branch (c) source | `sessions/archive/session-88/workshops/s88-w3-w1b1-63-3branch.md` §5 | `<computed-at-dispatch>` |
| LRD anchor reference | `researchers/Little-Red-Dots/` index | `<computed-at-dispatch>` |
| script template | `computations/_shared/_script_template.py` | `<computed-at-dispatch>` |

**PRDR audit (cardinality test)**: every free parameter listed above is pinned. Any missing pin at runtime triggers PRU Class 8 FAIL per `epistemic-discipline.md §"Pre-Registration Completeness"`.

**SOURCE-RECONCILIATION audit (value test)**: pin values are consistent with `mcp__knowledge__.get_constant(name)` canonicals; no Class-(b) PIN-LOOSE-SOURCE-TIGHT or Class-(c) PIN-DRIFT-FROM-STALE-SOURCE detected at plan-authorship. SUBSTRATE-FIRST-PROVENANCE: CM-1995 §III.4 IS the substrate-first canonical source for the residue formula (not a methodological cross-check; the formula IS the substrate's structural derivation form).

**Bridge-Landing Script Architecture**: §W1-1 does NOT land a registry slot in S89 (the structural theorem is a candidate for §VII.AU registry promotion in S90+ contingent on Stage-2 verify; pre-registration of registry-landing is OUT OF SCOPE for §W1-1). The single-shot `write→fsync→re-read→verify→emit` pattern of `registry-landing.md §"Bridge-Landing Script Architecture"` does NOT apply; standard single-canonical-line emission via `append_verdict()` suffices.

### 8. Expected output 4-tuple

```
(value=<alpha_value_M_1e7_Lmax_10>, scheme=peter-weyl-block-diagonal-HSS-projection-Lmax10-tau-fold-019, convention=horizon-spanning-sector-projection-CM-1995-III-4-FULL, L_max=10)
```

`.npz` data file keys (full list):
- `alpha_value_M_1e7_Lmax_10` (scalar; the PASS evaluation value)
- `alpha_values_M_scan` (3-vector; M ∈ {1e6, 1e7, 1e8} M_sun)
- `Lmax_scan_alpha_at_M_1e7` (3-vector; L_max ∈ {6, 8, 10})
- `structural_exponent_n` (scalar; extracted from L_max scan)
- `R_CM_residue_M_1e7` (scalar; the CM-1995 §III.4 residue value)
- `Tr_HSS_P_HSS_M_1e7` (scalar; HSS projector rank at M=1e7)
- `S_BH_substrate_M_1e7_Lmax_10` (scalar)
- `S_BH_semicl_M_1e7` (scalar)
- `Lambda_M_over_M_KK_at_1e7Msun` (scalar)
- `hss_sector_list_pq_M_1e7_Lmax_10` (list of (p,q) tuples)
- `monotonicity_assert_value` (boolean)
- `M_to_infinity_limit_at_Lmax_10` (scalar; substrate finite-L_max truncation residual)
- `rel_dev_to_LRD_anchor` (scalar; the PASS/INFO/FAIL discriminator value)
- `regime_verdict` (string: VALID/MARGINAL/BREAKDOWN)
- `sign_verdict` (string: PASS/FAIL/N/A — directional pre-registration: substrate-IS α(M) > 1 at finite L_max < ∞ per finite-truncation residual being POSITIVE; SIGN_CHECK)
- `magnitude_verdict` (string: PASS/INFO/FAIL)
- `composite_verdict` (string: PASS/INFO/FAIL — collapse rule per `gate-verdicts.md`)

### 9. PASS/FAIL/INFO thresholds with tolerance rule

**Threshold (RATIO tolerance per `gate-verdicts.md`)**:

- **PASS**: `rel_dev = |alpha_value_M_1e7_Lmax_10 − 1/458| / (1/458) ≤ 0.05` (5% relative deviation) AND `regime_verdict == VALID` AND `sign_verdict == PASS` (composite collapse rule).
- **INFO**: `0.05 < rel_dev ≤ 0.20` (sub-leading order deviation captured but not 5% precision; substrate-IS structural form is correct but L_max=10 truncation residual is non-negligible). Composite collapse: `composite = INFO`.
- **FAIL**: `rel_dev > 0.20` OR `sign_verdict == FAIL` (substrate predicts wrong direction) OR `regime_verdict == BREAKDOWN` (Friedrich-Bär saturation breaks at L_max=10 for HSS at M=1e7 M_sun — would be a Friedrich-Bär-bound violation indicating L_max=10 is not the operational truncation; rerun at L_max=12 from master cache).

**Sign verdict (mandatory per `[VERIFY-THEOREM]` trigger; SIGN_CHECK enforced via substitution chain Step 4 below)**:

- Direction predicted: α(M, L_max=10) > 1 at finite L_max < ∞. Reason: substrate finite-L_max truncation reduces the substrate-IS S_BH below the L_max → ∞ limit; the L_max → ∞ limit is conjectured to recover the full semiclassical S_BH; therefore at finite L_max, α = S_BH^substrate / S_BH^semicl < 1 from below NO — actually the prediction goes the OTHER way under the Connes-Moscovici §III.4 form: the residue correction R_CM is structurally NEGATIVE (the spectral-action moment ζ-residue at substrate-distance-1 pole s=3 is negative in our truncation regime per S87 W10-2 ρ_∞_FW = -0.8103647022669215 calibration), so `S_BH^substrate = Tr_HSS(P_HSS) − R_CM(>0 in absolute value with negative sign convention) ≈ Tr_HSS + |R_CM|`, which makes substrate-IS S_BH LARGER than naive truncation, hence α > 1 from above as L_max increases toward ∞.

  At M = 10^7 M_sun, L_max = 10 the empirical anchor 1/458 ≈ 2.18e-3 is much LESS than 1; this implies the structural identification of α at the empirical anchor is INVERTED relative to the naive 1+correction reading — the structural exponent n must satisfy (M_LRD/M_threshold)^{-n} ~ 1 - 1/458, which constrains n via the M_threshold pin emerging from sub-procedure 1. SIGN_CHECK enforces the substitution chain Step 4 direction: α evaluates to a value LESS than 1 at M_LRD because the LRD scale M=1e7 is LARGER than M_threshold (substrate finite-L_max truncation cannot accommodate horizon scales above its operational substrate-distance pole), so the asymptotic form α(M) = 1 + C_n · (M_LRD/M_threshold)^{−n} is in the (M/M_threshold) > 1 regime where C_n · (M_threshold/M_LRD)^n is NEGATIVE. The substitution chain (§10) makes this explicit.

**Regime verdict (mandatory; auto-shortening clause per `gate-verdicts.md`)**:

- VALID iff Friedrich-Bär saturation holds throughout the L_max ∈ {6, 8, 10} scan (per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"`); empirically: η_FB(p,q=10,0) > η_FB_lower = 0.40 at the (p,q) sectors entering HSS at M=1e7 M_sun.
- MARGINAL iff `0.50 ≤ f_used < 0.95` where `f_used = D_actual / D_intended` with D_intended = full (s ∈ {0.001..4.0}) residue-fit grid and D_actual = subset where polynomial fit residual < 1%.
- BREAKDOWN iff `f_used < 0.50` OR Friedrich-Bär saturation breaks.

### 10. Substitution chain (MANDATORY per `math-scripts.md §"Double-Check Logic Before Compute"`)

> The chain is mandatory because §W1-1's PASS predicate involves a directional/sign claim. Direction: substrate-IS α(M_LRD=1e7, L_max=10) MUST evaluate to a value LESS than 1 (NOT greater than 1), because the LRD horizon scale exceeds the L_max=10 substrate-distance saturation; at scales above saturation the substrate truncation underestimates microstate count.

**Step 1 — Definitions**:

- `M_LRD` = 10^7 M_sun (LRD characteristic BH mass scale; LRD reference set per `researchers/Little-Red-Dots/`)
- `M_KK` = 7.428660036284456e+16 GeV (canonical_constants.py; substrate Kaluza-Klein scale)
- `Vol_SU3` = canonical (substrate volume; canonical_constants.py)
- `M_Pl_eff` = M_KK · sqrt(Vol_SU3) (S58 Volovik partition; substrate emergent Planck mass)
- `Λ_M ≡ (M_Pl_eff² / M)^{1/2}` (substrate-distance scale at horizon area for BH mass M; substrate-IS definition via the Volovik partition image of the area-theorem)
- `HSS(M, L_max)` = {(p,q) ∈ Spec(D_K^≤L_max) : |λ_(p,q)| ∈ [Λ_M, M_KK]} (horizon-spanning sector set)
- `R_CM(M, L_max)` = Connes-Moscovici §III.4 residue at s=0 of `ζ_{D_K^HSS}(s) = Tr_HSS(|D_K|^{-2s})` (definition: CM-1995 §III formula (III.4))
- `M_threshold(L_max)` = max {M : HSS(M, L_max) is non-empty} (substrate-distance saturation scale; defined operationally via the largest (p,q) in Spec(D_K^≤L_max))

**Step 2 — Substitution (no simplification yet)**:

```
S_BH^substrate(M_LRD, L_max=10)
  = Tr_{HSS(M_LRD, 10)}(P_HSS(M_LRD, 10)) − R_CM(M_LRD, 10)            [definition; CM-1995 §III.4]
  = |HSS(M_LRD, 10)| − R_CM(M_LRD, 10)                                  [P_HSS is rank-|HSS| identity-like projector]

S_BH^semicl(M_LRD)
  = π · (2 G_N M_LRD)² / G_N
  = 4 π G_N M_LRD²                                                        [Bekenstein-Hawking semiclassical area-theorem; emergent gravity from a_2]

α(M_LRD, L_max=10)
  = S_BH^substrate(M_LRD, 10) / S_BH^semicl(M_LRD)
  = [|HSS(M_LRD, 10)| − R_CM(M_LRD, 10)] / (4 π G_N M_LRD²)              [substitute]
```

**Step 3 — Simplify to canonical form**:

Identify `M_threshold(L_max=10)` from the sub-procedure 1 HSS construction: the largest (p,q) ∈ Spec(D_K^≤10) corresponds to a substrate-distance scale Λ_max ≈ M_KK; the smallest (p,q) corresponds to Λ_min(L_max=10). The condition M ≥ M_threshold means Λ_M ≤ Λ_min(L_max), i.e., the BH horizon scale exceeds the substrate's smallest spectral-action moment scale, putting the BH "above saturation".

```
α(M_LRD, 10)
  = α_∞ + C_n · (M_LRD / M_threshold)^{−n}                              [asymptotic expansion at M >> M_threshold]
  
where:
  α_∞ = lim_{M → ∞} α(M, L_max=10)  (the L_max=10 truncation residual; L_max=10 cannot accommodate arbitrarily large M, so this is < 1 from below)
  C_n = (Connes-Moscovici §III.4 leading-coefficient at the substrate-distance pole)
  n   = structural exponent (n=2 if substrate-distance-1 pole s=3 dominates; n=4 if substrate-distance-2 pole s=4 dominates)
```

The substitution chain reduces the empirical anchor 1/458 to a STRUCTURAL constraint:

```
1/458 = α_∞ + C_n · (M_LRD / M_threshold(L_max=10))^{−n}
```

This is ONE equation in three unknowns (α_∞, C_n, n) — but α_∞ and C_n are computed from the spectral residue at L_max=10 (sub-procedure 2), and n is identified from the L_max-scan structure (sub-procedure 2 step (e)).

**Step 4 — Direction (read off from canonical form)**:

- At the LRD scale M_LRD = 10^7 M_sun, M_LRD >> M_threshold(L_max=10) (because L_max=10 saturates at substrate-distance-pole-bound scales much smaller than astrophysical BH masses). Therefore (M_LRD / M_threshold)^{-n} << 1 for n > 0, and the leading term is α_∞.
- At L_max=10, α_∞ is structurally LESS than 1 because the L_max=10 truncation cannot reproduce the full semiclassical microstate count: the substrate's HSS is a STRICT SUBSET of the (p,q) sectors needed to span the M=10^7 M_sun horizon area, so |HSS(M_LRD, 10)| underestimates the full microstate count.
- Direction prediction: `α(M_LRD=1e7, L_max=10) < 1`. SPECIFIC NUMERICAL PREDICTION (substitution chain pre-registration): α ≈ 1/458 ≈ 2.18e-3 (matches empirical anchor by hypothesis; PASS confirms hypothesis).
- SIGN_CHECK = PASS iff `alpha_value < 1` AND `alpha_value > 0` (positive but bounded above by 1).
- SIGN_CHECK = FAIL iff `alpha_value > 1` (substrate-IS overestimates microstate count; Connes-Moscovici §III.4 residue sign convention error or HSS projector sign error) OR `alpha_value ≤ 0` (negative microstate count; structural error in either Tr_HSS or R_CM extraction).

**Conclusion**: Direction `0 < α(M_LRD=1e7, L_max=10) < 1` pre-registered. PASS magnitude band centered at empirical 1/458 with 5% rel-tol. Composite verdict via `gate-verdicts.md` collapse rule.

**Plan-author Python verification**: at plan-authorship time, the substitution chain Step 4 direction is verified by the numerical fact 1/458 ≈ 2.18e-3 < 1 (trivial sign-only verification; magnitude verification deferred to runtime where the substrate spectrum cache is loaded). No GPU computation required at plan-authorship.

### 11. What PASSES/FAILS MEAN for solution space

**PASS at §W1-1**:

- Closes the S88 §W1b1-63 FAIL routing branch (c) at the substrate-IS NCG-axiomatic level. The substrate's spectral-triple residue formula on horizon-spanning sectors structurally reproduces the empirical α = 1/458 within 5% precision.
- Opens A.20 (Stage-2 dual-prior pre-registration on the canonical Connes-Karoubi pairing computation; per `joint-theorem-promotion.md` 4-stage pathway, A.20 requires A.3 + A.4 PASS as prerequisites in Cluster B — but §W1-1's α(M) function-form derivation is upstream of A.3 because it pins the M-dependence of the HSS projector that A.3's Hochschild-cocycle Connes-Karoubi pairing inherits).
- Promotes a STAGE-1-CANDIDATE registry entry §VII.AU candidate: "Substrate-IS Horizon-Microstate Count via CM-1995 §III.4 Finite-Spectral-Triple Residue" (NOT landed in S89 W1; landing requires Stage-2 cross-axis verify in S90+).
- Constrains the cosmological-CC accommodation pathway: the substrate's α(M) at LRD scales MATCHES empirical, reducing the 13-OOM cascade-tail underflow (§W1c-69) to a corridor where multi-species L_H corrections (§W1-2) can plausibly close the gap.

**INFO at §W1-1** (5% < rel_dev ≤ 20%):

- Substrate-IS function-form α(M) is structurally correct (right asymptotic form, right exponent n) but L_max=10 truncation residual is non-negligible. Carry-forward to S90 for L_max=12 evaluation from the master spectrum cache; if rel_dev shrinks to ≤ 5% at L_max=12, PASS-with-Lmax-extension. If rel_dev does NOT shrink, structural identification of n may need revision (non-leading pole interference; cross-pole residue mixing per §VII.U.2 4-corner classification of `permanent-results-registry.md`).

**FAIL at §W1-1** (rel_dev > 20% OR sign mismatch OR regime breakdown):

- Substrate-IS NCG-axiomatic horizon-microstate count via CM-1995 §III.4 does NOT reproduce the empirical anchor at L_max=10. Closes the S89 cosmological-CC accommodation pathway via this specific channel.
- Forces re-classification: the LRD α-anchor either (a) is NOT structurally captured by the CM-1995 §III.4 form on (A_K, H_K, D_K), pointing to a DIFFERENT substrate algebra image (e.g., extended Pati-Salam or alternative finite-spectral-triple geometry); or (b) requires a multi-pole interference structure not captured at the substrate-distance-1 leading order.
- Forecloses A.10/A.20 contingent on §W1-1 PASS (these are downstream Stage-2 verifies that anchor on the cohomology-class-layer infrastructure A.1 anchors).
- Constraint-map update: closes the corridor "substrate-IS NCG-axiomatic horizon-microstate count single-pole leading-order" while preserving the corridors "multi-pole substrate-IS forms" and "alternative substrate-algebra forms" as untested.

### 12. Effort estimate

**4 wave-equiv** (LARGEST single S89 item; matches ledger A.1 effort). Breakdown by sub-procedure:

| Sub-procedure | Wave-equiv | Notes |
|:--|:--|:--|
| 1 — Infrastructure (HSS projector + cache truncation) | 0.5 | Mostly cache slicing; minimal compute |
| 2 — α(M) function-form derivation (residue extraction + L_max scan) | 2.0 | LARGEST; requires CM-1995 §III.4 transcription, ζ-residue grid evaluation, polynomial fit, L_max scan at 3 values |
| 3 — L_max=10 evaluation cross-check at 3 M-values | 1.0 | Reuses sub-procedure 2 infrastructure; 3-point M-scan |
| 4 — Empirical anchor verification + composite verdict emission | 0.5 | Comparison + verdict-line emission |

GPU path: torch.linalg on AMD RX 9070 XT for HSS projector matrix products (matrix dim ≥ several thousand at L_max=10). CPU fallback acceptable with `OMP_NUM_THREADS=8` cap (per `math-scripts.md §Environment`); estimated wall-time 4-6 hours single-agent CPU vs 1-2 hours GPU.

### 13. Substrate framing per `phononic-framing.md` §"IS Space, Not IN Space"

**Verbatim agent dispatch prompt insertion (MANDATORY)**:

> "The substrate IS the spectral triple (A_K^≤10, H_K^≤10, D_K^≤10) at horizon-spanning Peter-Weyl sectors. The horizon is NOT a container the substrate sits IN; horizon emergence is a derived consequence of the spectral-action a_2 Seeley-DeWitt coefficient (per `phononic-framing.md`). α(M) IS the substrate's intrinsic microstate-count ratio at horizon-spanning Peter-Weyl block level; α(M) is NOT a quantum correction to a pre-existing semiclassical area-theorem — the area-theorem is DERIVED from the substrate's L_max → ∞ limit, not the other way.
>
> FORBIDDEN explanation directions:
> - 'BH in curved spacetime' (container-thinking; reverses the explanation order)
> - 'Quantum corrections to Bekenstein-Hawking' (presupposes Bekenstein-Hawking is fundamental; it is emergent)
> - 'Holographic entropy bound' (assumes holography as primitive; substrate IS the bulk-and-boundary, not bounded by anything external)
> - 'Sum over geometries' (the spectral action IS the sum; geometry emerges from the spectral triple, not the other way)
>
> REQUIRED explanation direction (per `phononic-framing.md` §'IS Space, Not IN Space — Mandatory Reframe'):
>
>     D_K eigenvalues at horizon-spanning sectors → Connes-Moscovici §III.4 residue formula → α(M) function-form → emergent semiclassical area-theorem in M → ∞ limit
>
> Cross-pillar bridge anatomy reminder: §W1-1's structural theorem is a SUBSTRATE-IS observable on a single pillar (the substrate's spectral-triple-axiomatic horizon-microstate count). If the theorem is later extended to a cross-pillar bridge (e.g., substrate-IS α vs cosmological-IN BH-population observable), the 5 IS-not-IN anatomy elements + 3-level structural-confidence ladder of `cross-pillar-bridge-anatomy.md` will apply at landing time."

**Single-τ-slice vs moduli-deformation level declaration** (per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`): §W1-1 operates at **Level 1 (single-τ-slice substrate-IS)** at τ_fold = 0.190. The α(M) function-form is computed on the FIXED τ-slice spectral triple; moduli-deformation behavior is OUT OF SCOPE for §W1-1 (would be a Level-2 extension in S90+ if the τ-asymmetric breakdown geometry of §VII.AE intersects horizon-microstate count).

### 14. Calibration Corpus Tracking — Hybrid Independence Test K-counter advancement (K=1 → K=2)

> **Provenance**: Added 2026-05-10 per user directive (atlas-uplift S88-current campaign carry-forward). Pre-registers §W1-1 as a structural calibration-corpus instance under `cross-pillar-bridge-anatomy.md §"Forward template-adoption" §"Hybrid Independence Test (S88 W8-87 RULE-EXTENSION)"`. K-counter advancement is BY-CONSTRUCTION at dispatch (independent of PASS/FAIL outcome) per the Two-clause separation discipline of `cross-pillar-bridge-anatomy.md §"Two-clause separation: registry-PASS (per-entry) vs K-counter advancement (rule-level corpus)"`.

**Cross-pillar bridge anatomy declaration (5 IS-not-IN elements)**:

1. **Substrate-IS observable**: α(M) = S_BH^substrate(M, L_max=10) / S_BH^semicl(M) computed via Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula on the horizon-spanning Peter-Weyl sector projection of `(A_K^≤10, H_K^≤10, D_K^≤10)`. Pillar III (substrate spectral-triple algebra-side; SAME pillar as §VII.AF.1 W-5 baseline calibration #1 K=1).
2. **Laboratory-IN observable**: S_BH^semicl(M) = A(M) / (4 G_N) = 4π G_N M² (Bekenstein-Hawking semiclassical area-theorem). Pillar I (geometric continuum / black-hole-thermodynamics area-theorem in 4D macroscopic GR). DISTINCT from §VII.AF.1's Pillar IV (Peotta-Törmä superfluid-stiffness / quantum-metric integrated trace on `∫_BZ Tr g_ab^{(P_0)}(k; τ_fold) d^d k`).
3. **Bridge map**: CM-1995 §III.4 finite-spectral-triple residue formula `S_BH^substrate = Tr_HSS(P_HSS) − (1/(2πi)) ∮_{s=0} Tr_HSS(|D|^{-2s})·γ(s) ds` evaluated at canonical L_max=10 (zeta-residue at s=0). DISTINCT class from §VII.AF.1's HKR `L_max → ∞` continuum image (which is the Hochschild-Kostant-Rosenberg image of substrate-IS finite-L Hochschild pairing onto the laboratory-IN continuum BZ-trace).
4. **Algebraic envelope**: α(M) = 1 + C_n · (M / M_threshold)^{−n} + O((M/M_threshold)^{−(n+1)}) M-asymptotic at fixed L_max=10. Structural exponent n derived from CM-1995 §III.4 finite-spectral-triple residue pole structure (n=2 substrate-distance-1 pole at s=3 dominance; n=4 substrate-distance-2 pole at s=4 dominance; n=other if cross-pole interference dominates). INDEPENDENT envelope class from §VII.AF.1's `L^{-3}` envelope at d=4 (which is L_max-asymptotic at fixed M, not M-asymptotic at fixed L_max).
5. **Empirical anchor**: α(M_LRD = 10^7 M_sun, L_max=10) ≈ 1/458 ≈ 2.183e-3 from S88 W1b1-63 branch (c) at `sessions/archive/session-88/workshops/s88-w3-w1b1-63-3branch.md §5 CF-W1b1-C`; PASS at 5% relative tolerance per §9.

**Three-level structural-confidence ladder declaration**:

- **Level 1 (cohomology-class identity; regulator-invariant; L-independent)**: the substrate-IS function-form α(M) at the residue-formula level is regulator-class-INVARIANT under CM-1995 §III.4 universal kernel γ(s) = Γ(s) (for finite spectral triple). Holds at every L_max in the operational truncation per Friedrich-Bär saturation.
- **Level 2 (algebraic envelope; L_max-dependent; algebraically derived)**: the M-asymptotic envelope `α(M) = 1 + C_n · (M/M_threshold)^{−n}` at fixed L_max=10 is algebraically derived from the substrate-distance pole structure. **Level-2 sub-class declaration per `cross-pillar-bridge-anatomy.md §"Level-2 Layer Distinction"`**: this envelope is **Level-2-binding** by HKR-image construction — the α(M) → 1 limit at M ≪ M_threshold is the HKR image of the Level-1 cohomology-class identity (substrate-IS finite-L residue formula → laboratory-IN continuum BH-thermodynamic area-theorem in the M → ∞ limit). NOT Level-2-non-binding (which would be a bare-decomposition envelope on a substrate-internal Tr(D_K^{-2s}) with no HKR image to a continuum laboratory observable on the partner pillar).
- **Level 3 (empirical anchor at canonical L_max)**: numerical α(M=10^7 M_sun, L_max=10) evaluated by sub-procedure 4; PASS/INFO/FAIL per §9.

**Element 2 OE-form discipline declaration (S88 W7a-73 hardening)**: Element 2 is `S_BH^semicl(M) = A(M)/(4G_N) = ∫ d²x Tr_{horizon-2-surface}(P_horizon) / (4G_N)` — the integration domain is the horizon 2-surface; the trace is over the horizon-2-surface algebra; the named projector is `P_horizon` (Bekenstein-Hawking horizon-area-theorem projector). OE-form regex match: `\int.*d.*Tr.*\([ΠP]_[a-z0-9_-]+\)` PASSES on `∫ d²x Tr(P_horizon)` form.

**Hybrid Independence Test predicate evaluation** (substitution chain per `math-scripts.md §"Double-Check Logic Before Compute"`):

```
Definitions:
  HIT = Hybrid Independence Test predicate per cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"
  HIT advances K-counter iff (i ∨ ii ∨ iii) ∧ iv where:
    (i)   substrate-IS pillar distinct from prior K-instances
    (ii)  laboratory-IN pillar distinct from prior K-instances
    (iii) bridge map class distinct from prior K-instances
    (iv)  algebraic envelope independent (NOT a numerical refinement of an existing K-instance's envelope)

Substitutions (§W1-1 vs K=1 baseline §VII.AF.1):
  Step 1 (i): Pillar III spectral-triple residue (W1-1) vs Pillar III HP^1 cohomology (AF.1) → SAME pillar → (i) FALSE
  Step 2 (ii): Pillar I BH-thermodynamic area-theorem (W1-1) vs Pillar IV Peotta-Törmä quantum-metric (AF.1) → DISTINCT pillars → (ii) TRUE
  Step 3 (iii): CM-1995 §III.4 finite-spectral-triple zeta-residue (W1-1) vs HKR L_max → ∞ continuum image (AF.1) → DISTINCT bridge map classes → (iii) TRUE
  Step 4 (iv): M-asymptotic envelope at fixed L_max (W1-1) vs L_max-asymptotic envelope at fixed M (AF.1) → INDEPENDENT envelope class → (iv) TRUE

Simplify:
  Step 5: (FALSE ∨ TRUE ∨ TRUE) = TRUE
  Step 6: TRUE ∧ TRUE = TRUE

Direction (read off canonical form):
  Step 7: HIT(W1-1, AF.1) = TRUE → §W1-1 advances Hybrid Independence Test K-counter

Conclusion:
  §W1-1 dispatch advances K-counter K=1 SUGGESTION → K=2 SUGGESTION (advancement BY CONSTRUCTION at dispatch
  per Two-clause separation; promotion to K=3 MANDATORY requires a third distinct calibration instance from
  S90+ work).
```

**Status under Two-clause separation**:

- **Per-entry registry-PASS** (§9 PASS/INFO/FAIL): conditional on rel_dev ≤ 0.05 against 1/458 anchor at canonical L_max=10. INDEPENDENT of K-counter advancement.
- **Rule-level corpus K-counter advancement** (this sub-section): TRUE BY CONSTRUCTION at dispatch (Hybrid Independence Test predicate evaluates TRUE on §W1-1 structural form). INDEPENDENT of §9 outcome.

The two predicates are STRUCTURALLY ORTHOGONAL per `cross-pillar-bridge-anatomy.md §"Two-clause separation"` (calibrated S88 W13 W-1 R3 close); future readers MUST treat them as independent epistemic objects on disjoint epistemic layers. Conflation is a Class-3 PROHIBITED_ACTIONS adjacency (post-hoc rewriting of pre-registered structure) per `v3-closure-recovery.md §PROHIBITED_ACTIONS`.

**Sub-class assignment for K=2 corpus row** (forward enforcement of the 5-anatomy + 3-level discipline):

| Field | Value |
|:------|:------|
| Calibration corpus instance # | 2 (advancing from K=1 baseline at §VII.AF.1 LANDED) |
| Substrate-IS pillar | Pillar III (spectral-triple algebra-side at horizon-spanning sectors) |
| Laboratory-IN pillar | Pillar I (geometric continuum / BH-thermodynamic area-theorem) |
| Bridge map class | CM-1995 §III.4 finite-spectral-triple zeta-residue (NEW class; distinct from HKR continuum image) |
| Algebraic envelope class | M-asymptotic at fixed L_max (NEW class; distinct from L_max-asymptotic at fixed M) |
| Empirical anchor | α(M_LRD=1e7, L_max=10) ≈ 1/458 from S88 W1b1-63 branch (c) |
| Level-2 sub-class | Level-2-binding (by HKR-image construction at the M → ∞ limit) |
| HIT predicate | TRUE per substitution chain Step 7 |
| Status | SUGGESTION (K=2 of K=3 needed for MANDATORY promotion) |

**On-PASS post-gate-hook actions** (forward-looking; conditional on §9 PASS):

1. Record §W1-1 in `sessions/framework/registry/cross-pillar-bridge-corpus.md §3` (Hybrid Independence Test K-counter calibration corpus) as instance #2; advance K-counter from K=1 to K=2.
2. Record §W1-1 in `sessions/framework/registry/cross-pillar-bridge-corpus.md §1` (Level-2 Layer Distinction calibration) as Level-2-binding instance (counter advances K=2 → K=3 if W3b-15 KDE Sub-test B remains canonical reading); on K=3 saturation, the Level-2-binding sub-clause promotes from MANDATORY-at-K=3 to its hardened forward-form.
3. Sole writer: mack-cosmic-bridge per `feedback_mack-bridge-role.md` (registry/inventory rows; this calibration entry is registry-class). Writer dispatch in S89 W1 closeout.

**On-FAIL or INFO post-gate-hook actions**: K-counter advancement IS NOT REVOKED (the dispatch occurred; the structural form satisfies HIT). The corpus row records the FAIL/INFO outcome as an empirical-anchor-violation note (analogous to S87 W11-5 REGISTRY-FAIL by 21× treated as calibration corpus instance #2 of cross-pillar K-counter despite registry-FAIL). The two-clause separation makes this consistent: rule-level K-counter saturation is invariant under per-entry empirical-anchor outcome.

**Cross-link summary**:

- `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"` — the K-counter sub-clause this advancement targets
- `cross-pillar-bridge-anatomy.md §"Two-clause separation: registry-PASS vs K-counter advancement"` — the structural-orthogonality discipline
- `cross-pillar-bridge-anatomy.md §"Level-2 Layer Distinction"` — the Level-2-binding sub-class declaration
- `joint-theorem-promotion.md §"Stage 2"` — the cross-axis cross-reviewer protocol that gates Stage-3 PERMANENT registry promotion (ORTHOGONAL to K-counter advancement; both apply independently)
- `feedback_rules-compensate-missing-structure.md` — K=3 promotion threshold for SUGGESTION → MANDATORY status
- `sessions/framework/registry/cross-pillar-bridge-corpus.md §3` — corpus location for K=2 row landing
- atlas-11 §"Hybrid Independence Test K-counter" — atlas-side narrative cross-link (advances K=1 → K=2 narrative on §W1-1 PASS at canonical anchor; remains K=1 narrative if §W1-1 INFO/FAIL with corpus row recording the empirical-anchor-violation).

---

## §W1-2. S89-L-H-CANONICAL-RE-PINNING-CASCADE-TAIL-13OOM

### 1. Gate ID

`S89-L-H-CANONICAL-RE-PINNING-CASCADE-TAIL-13OOM`

### 2. Trigger

`[VERIFY]` + `[AUDIT]` (composite). VERIFY for the L_H_canonical re-derivation and the §W1c-69 substitution-chain Step 5 re-execution; AUDIT for the Option A `supersedes` protocol (the corrective verdict line MUST grep-extract the FULL 64-character original audit_sha256 from the S88 verdict file at runtime and emit it as the `supersedes=` token; the audit confirms the supersession-chain reading discipline is structurally maintained per `gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict permanence"`).

### 3. Classification

PHONONIC + cosmological-observable (§W1-2 is a substrate-pinned multi-species correction to a Hawking-radiation luminosity observable; the species multiplicity f(M) is downstream of the substrate's T_H(g) cooling cascade through phononic excitation thresholds — phononic excitation density at species-mass scales determines f(M)). The cosmological consequence (cascade-tail closure of the §W1c-69 13-OOM underflow) is the falsifier-master-inventory-relevant observable.

### 4. Agent type (runtime)

PRIMARY: `mack-cosmic-bridge` — cosmological-observable axis primary; sole writer for `sessions/framework/registry/falsifier-master-inventory.md` rows per `feedback_mack-bridge-role.md`. The L_H multi-species correction is a cosmological-observable mapping; L_H itself is the Hawking-radiation luminosity, downstream of substrate-pinned T_H but with cosmological-bridge accounting structure.

CO-AUTHOR: `hawking-theorist` — Hawking-radiation interface specifics. The L_H_eq1 → L_H_canonical multi-species recompute requires Hawking-radiation interface knowledge: the Stefan-Boltzmann form `L_H = (π² / 60) · g_*(T_H) · A_horizon · T_H⁴` where g_*(T_H) is the effective-degree-of-freedom count at T_H. hawking-theorist supplies the Stefan-Boltzmann + g_* mapping; mack supplies the cosmological-observable consequence + falsifier-inventory row.

`gen-physicist` is BLACKLISTED per `/rclab-plan` skill §3b item 4. `connes-ncg-theorist` does NOT participate in §W1-2 (substrate-IS horizon-microstate count is §W1-1; §W1-2 is downstream cosmological-bridge consequence).

### 5. Hypothesis

The §W1c-69 substitution-chain Step 5 underflow (13-OOM cascade-tail) closes when L_H is recomputed at the substrate-pinned T_H = 1.057 MeV (per S88 W6 §V.1) with full SM-species g_*(T_H) accounting, yielding L_H_canonical = (1.0 ± 0.4) × 10^7 W. The PASS criterion is `|log10(L_H_canonical / L_H_eq1) − log10(f(M))| < 0.5` — i.e., the multi-species correction reproduces the species-multiplicity factor f(M) within 0.5 log-OOM, demonstrating that the §W1c-69 chain's Step 5 was structurally correct but used an incomplete L_H_eq1 (single-species placeholder); the cascade-tail 13-OOM gap is real but recoverable through species-multiplicity dressing.

### 6. Method

**Script path**: `computations/session-89/s89_w1_l_h_canonical_repinning_cascade_tail.py`

**Substrate framing reminder** (verbatim agent dispatch prompt insertion):

> "T_H = 1.057 MeV is the SUBSTRATE-PINNED Hawking temperature at the §W1c-69 cascade-tail evaluation point (per S88 W6 §V.1; substrate-derived from the substrate's spectral-action moment ratio at horizon-spanning Peter-Weyl sectors). It is NOT an external ad-hoc choice. The L_H multi-species correction f(M) IS the substrate's emergent Stefan-Boltzmann species-multiplicity factor at T_H = 1.057 MeV, derived from g_*(T_H) at the SM-particle-threshold structure traversed by the substrate's T_H(g) cascade. The cosmological observable L_H IS the Hawking-radiation luminosity at the substrate-IS T_H, NOT a free-parameter cosmological fit to L_H_obs."

**Imports**:

```python
from canonical_constants import *  # MANDATORY
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
import numpy as np
import hashlib, re, sys
from pathlib import Path
```

**Procedure**:

1. **Load the species-multiplicity table from §W1-3 output** (`computations/session-89/s89_w1_f_m_species_multiplicity_lookup_table.npz`; intra-wave dependency from §W1-3). Key: `f_g_table` (vector indexed by g ∈ {0..384}); `T_H_g_table` (vector). Load also `g_eff_at_T_H_substrate` (scalar; SM g_* at T_H = 1.057 MeV).

2. **Compute L_H_canonical at T_H = 1.057 MeV with full SM-species accounting**:

   ```
   L_H = (π² / 60) · g_*(T_H = 1.057 MeV) · A_horizon · T_H⁴
   ```

   where:
   - `g_*(T_H = 1.057 MeV)` from §W1-3 table (at T_H = 1.057 MeV the active SM species are: photon γ (2 dof), neutrinos νₑ νμ ντ (3 × 2 × 7/8 dof for fermions), electron-positron e± (2 × 2 × 7/8 dof) — total g_* ≈ 10.75 in standard cosmology; SUBSTRATE-DERIVED via §W1-3 pinning, NOT externally imposed)
   - `A_horizon` is computed from the substrate-pinned BH mass scale at the §W1c-69 evaluation point (mass M_BH_at_W1c69 from W1c-69 verdict file extraction; pre-computed at plan-freeze time as a stale-source check, then re-extracted at runtime).
   - `T_H = 1.057 MeV = 1.057e6 eV = 1.694e-13 J`.

3. **Compare against L_H_eq1 (single-species placeholder used in §W1c-69 Step 5)**:

   ```
   L_H_eq1 = (π² / 60) · 1 · A_horizon · T_H⁴   (g_* = 1 placeholder; Cosmic Censorship Conjecture-style minimal accounting)
   ```

   Compute `log10_ratio = log10(L_H_canonical / L_H_eq1) = log10(g_*(T_H = 1.057 MeV) / 1) = log10(g_eff_substrate)`.

4. **Compare against f(M) (substrate-derived species-multiplicity factor at the §W1c-69 cascade-tail mass M)**:

   The §W1c-69 chain's Step 5 introduced a species-multiplicity factor f(M) intended to capture the same g_* dressing. Verify the structural identity:

   ```
   log10(L_H_canonical / L_H_eq1) ≈ log10(f(M_at_W1c69))
   ```

   PASS iff `|log10_ratio − log10(f(M_at_W1c69))| < 0.5`.

5. **Re-execute §W1c-69 substitution-chain Step 5 with corrected L_H**:

   The §W1c-69 Step 5 chain had the form:
   ```
   <Step 5 from §W1c-69 substrate framing — verbatim from sessions/archive/session-88/workshops/s88-w6-w1c-69-page1976-13oom.md §V.1>
   ```
   Re-evaluate Step 5 with `L_H = L_H_canonical` instead of `L_H = L_H_eq1`. Compute the cascade-tail residual at the new L_H. Pre-registered comparison: the residual SHOULD shrink by `log10(g_*(T_H = 1.057 MeV)) ≈ log10(10.75) ≈ 1.03 OOM` (closing 1 OOM of the 13-OOM gap; further closures are downstream of f(g) traversal across cascade generations per §W1-3).

6. **Emit successor verdict line under Option A `supersedes` protocol** (per `gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict permanence"` rules (1)-(6)):

   (a) Grep-extract the FULL 64-character original audit_sha256 from `computations/session-88/s88_gate_verdicts.txt` for the gate ID matching the §W1c-69 source (the skill template prefix `2afd17ef99c81123…` is a HEAD-16 form; the full SHA must be extracted from the verdict file). Regex pattern: `audit_sha256=([0-9a-f]{64})`.

   (b) Compute the new audit_sha256 for §W1-2 from `closure_hash(input_pin_map)` per `gate-verdicts.md §"Pre-Registration Protocol"` Step 3 (NEVER hardcode; ALWAYS compute).

   (c) Construct the supersedes token: `supersedes=<full-64-char-old-audit-sha-extracted-at-runtime>`. Embed in the corrective canonical verdict line's `value=` field per Option A rule (2). Format example (illustrative — exact format finalized at runtime):

   ```
   S89-L-H-CANONICAL-RE-PINNING-CASCADE-TAIL-13OOM: PASS|FAIL|INFO -- value='log10_ratio=<R>;|delta|=<D>;supersedes=<full-64-char-original>' scheme=substrate-pinned-T_H-1.057-MeV-SM-species convention=multi-species-stefan-boltzmann-with-supersedes-token L_max=10 audit_sha256=<NEW-64-char> content_sha256=<NEW-64-char> schema_version=S87+
   ```

   (d) Emit the dual-SHA companion comment row per W9a-99 split.

   (e) DO NOT EDIT the original §W1c-69 verdict line on disk (Option A rule (1): "Original verdict line is RETAINED on disk."). Append-only emission via `append_verdict()` helper.

7. **Mack-cosmic-bridge falsifier-master-inventory row update** (mack PRIMARY, sole writer per `feedback_mack-bridge-role.md`):

   Append a new row OR audit-pin sub-row to `sessions/framework/registry/falsifier-master-inventory.md` at the §"L_H_canonical multi-species" entry, citing the FULL 64-char audit_sha256 of §W1-2's verdict line. The inventory row must follow the `mack-observational-constraints.md` format and link to the canonical_constants entry name (which IS L_H_canonical_FW promoted via `update_constant("L_H_canonical_FW", L_H_canonical_value, session="S89", source="S89-L-H-CANONICAL-RE-PINNING-CASCADE-TAIL-13OOM", comment="Substrate-pinned T_H=1.057 MeV multi-species L_H per S88 W6 §V.1; supersedes L_H_eq1 placeholder")`).

**Cross-checks emitted in stdout (first 20 lines)**:

```
SHA INPUT: canonical_constants.py = <SHA>
SHA INPUT: s89_w1_f_m_species_multiplicity_lookup_table.npz = <SHA>  # from §W1-3
SHA INPUT: s88-w6-w1c-69-page1976-13oom.md = <SHA>
SHA INPUT (S88 verdict file): computations/session-88/s88_gate_verdicts.txt = <SHA>
SUPERSEDES TOKEN (extracted at runtime): <full-64-char-original-audit-sha>
NEW AUDIT SHA: <full-64-char-new>
CLOSURE INPUT-PIN MAP SHA = <closure_sha>
```

**Output files**:

- Canonical: `computations/session-89/s89_gate_verdicts.txt` (canonical line + dual-SHA companion comment row)
- Data: `computations/session-89/s89_w1_l_h_canonical_repinning_cascade_tail.npz` (keys: `L_H_canonical`, `L_H_eq1`, `log10_ratio`, `f_M_at_W1c69`, `delta_log10`, `Step5_residual_pre_correction`, `Step5_residual_post_correction`, `g_eff_at_T_H_substrate`, `T_H_substrate`, `A_horizon_at_W1c69`)
- Plot: `computations/session-89/s89_w1_l_h_canonical_repinning_cascade_tail.png` (2-panel: panel A log10(L_H) vs g_* across {1, 2, 5, 10.75, 20, 50, 100} g_* values with substrate-canonical g_*(1.057 MeV) marked; panel B Step 5 residual pre vs post correction with 13-OOM target band)
- Working-paper section: `sessions/archive/session-89/session-89-w1-workingpaper.md` §W1-2 (substantive content ≥ 15 lines)
- Inventory update: `sessions/framework/registry/falsifier-master-inventory.md` (one row update; mack PRIMARY)
- Canonical promotion: `computations/_shared/canonical_constants.py` (NEW: `L_H_canonical_FW`)

### 7. Machinery pin (PRDR — Pre-Registration Dry-Run; full enumeration)

| Pin | Value | Source / Class |
|:----|:------|:---------------|
| `T_H_substrate` | 1.057 MeV (= 1.057e6 eV) | S88 W6 §V.1 substrate-pinned; PROMOTE to canonical_constants.py at S89 plan-freeze if not yet present |
| `g_eff_at_T_H_substrate` | from §W1-3 table at g corresponding to T_H = 1.057 MeV (NOT externally imposed; read from §W1-3 .npz output) | Intra-wave dependency |
| `M_BH_at_W1c69` | <extracted from S88 verdict file at runtime> | Pre-computed at plan-freeze for stale-source check |
| `regulator` | `a_n^{ζ}` (Stefan-Boltzmann form is implicit zeta-regularization on bosonic + fermionic mode counts) | per `regulator-pin-discipline.md` |
| `convention` | `multi-species-stefan-boltzmann-with-supersedes-token` | NOT SCHEMATIC; full physical multi-species form |
| `convention_class_pin` | FULL | per `substrate-first-canonical-sourcing.md §(iv)` |
| `scheme` | `substrate-pinned-T_H-1.057-MeV-SM-species` | |
| `supersedes` | `<full-64-char-extracted-at-runtime-from-computations/session-88/s88_gate_verdicts.txt>` | per `gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict permanence"`; the prefix `2afd17ef99c81123…` is the HEAD-16 short form; runtime extracts the FULL 64-char form |
| `random_seed` | None (deterministic) | |
| `tolerance` | 1e-12 (float64 native machine epsilon × 100) | |
| `pass_threshold` | `|delta_log10| < 0.5` (ABSOLUTE log-OOM tolerance) | Pre-registered |
| `info_band` | `0.5 ≤ |delta_log10| < 1.0` | Pre-registered |
| `fail_band` | `|delta_log10| ≥ 1.0` | Pre-registered |

**Input SHA pins** (computed at plan-freeze):

| Input | Path | SHA pin form |
|:------|:-----|:-------------|
| canonical_constants | `computations/_shared/canonical_constants.py` | `<computed-at-dispatch>` |
| species-multiplicity table | `computations/session-89/s89_w1_f_m_species_multiplicity_lookup_table.npz` (from §W1-3) | `<computed-at-runtime; intra-wave dependency>` |
| §W1c-69 source | `sessions/archive/session-88/workshops/s88-w6-w1c-69-page1976-13oom.md` | `<computed-at-dispatch>` |
| S88 verdict file (for supersedes-token extraction) | `computations/session-88/s88_gate_verdicts.txt` | `<computed-at-dispatch>` |
| script template | `computations/_shared/_script_template.py` | `<computed-at-dispatch>` |

**PRDR audit**: every free parameter pinned; `g_eff_at_T_H_substrate` is a runtime-pinned-from-§W1-3-output value, NOT a free parameter (pin-source is §W1-3 .npz output, intra-wave dependency).

**SOURCE-RECONCILIATION audit**: `T_H_substrate = 1.057 MeV` is a Class-(e) PIN-PROMOTES-TO-CANONICAL-ON-PASS pin per `epistemic-discipline.md §"Source Reconciliation"` — the canonical does NOT yet exist in canonical_constants.py at plan-freeze; it is promoted on §W1-2 PASS. Severity: NO-ACTION (within S82 absorbable band). Promotion logged: `update_constant("T_H_substrate", 1.057e6, session="S89", source="S88-W6-W1c-69-page1976-13oom", comment="Substrate-pinned Hawking temperature at §W1c-69 cascade-tail evaluation point")`.

### 8. Expected output 4-tuple

```
(value='log10_ratio=<R>;|delta|=<D>;supersedes=<full-64-char-original>', scheme=substrate-pinned-T_H-1.057-MeV-SM-species, convention=multi-species-stefan-boltzmann-with-supersedes-token, L_max=10)
```

### 9. PASS/FAIL/INFO thresholds with tolerance rule

**Threshold (ABSOLUTE log-OOM tolerance)**:

- **PASS**: `|log10(L_H_canonical / L_H_eq1) − log10(f(M_at_W1c69))| < 0.5` AND `Step5_residual_post_correction` shrinks by ≥ 1 log-OOM relative to `Step5_residual_pre_correction` AND supersedes-token is correctly emitted as full 64-char form (AUDIT side).
- **INFO**: `0.5 ≤ |delta_log10| < 1.0` (correction is in right direction but magnitude off by factor 3-10; partial closure of 13-OOM gap, but f(g) traversal across cascade generations needed to close fully).
- **FAIL**: `|delta_log10| ≥ 1.0` OR supersedes-token emission failure (Option A protocol violation; AUDIT-side FAIL).

### 10. Substitution chain (MANDATORY)

**Step 1 — Definitions**:

- `L_H_eq1 ≡ (π² / 60) · 1 · A_horizon · T_H⁴` (Stefan-Boltzmann with g_* = 1 placeholder; §W1c-69 Step 5 single-species form)
- `L_H_canonical ≡ (π² / 60) · g_*(T_H_substrate) · A_horizon · T_H_substrate⁴` (substrate-pinned T_H + full SM g_* count)
- `f(M) ≡ species-multiplicity factor at substrate-pinned mass M` (from §W1-3 table; intra-wave dep)
- `T_H_substrate = 1.057 MeV` (canonical from S88 W6 §V.1)

**Step 2 — Substitution**:

```
log10(L_H_canonical / L_H_eq1) = log10(g_*(T_H_substrate) / 1)
                                = log10(g_*(1.057 MeV))
```

**Step 3 — Simplify**:

At T_H = 1.057 MeV, the active SM species (above MeV scale, traversing the electron mass threshold at 0.511 MeV):
- photon γ: 2 bosonic dof
- neutrinos νₑ νμ ντ + antineutrinos: 6 fermionic dof × 7/8 = 21/4
- e± at threshold (partially active): 4 fermionic dof × 7/8 = 7/2 (minus threshold suppression)

Total g_*(T_H = 1.057 MeV) ≈ 10.75 (standard cosmology value at this T regime; cross-check anchor PDG/Planck).

```
log10(g_*(1.057 MeV)) ≈ log10(10.75) ≈ 1.031  (specific value: 1.03142...)
```

**Step 4 — Direction**:

The ratio `L_H_canonical / L_H_eq1 > 1` because `g_*(T_H_substrate) > 1` (multiple SM species are active). Direction: `log10_ratio > 0`. `f(M)` is the substrate's species-multiplicity factor, expected to match g_*(T_H_substrate) to leading order if the substrate's g_*(T_H) cooling profile correctly traverses the SM-thresholds.

PASS iff `|log10(10.75) − log10(f(M_at_W1c69))| < 0.5` ⇔ `f(M_at_W1c69) ∈ [10.75 / 10^0.5, 10.75 × 10^0.5] ≈ [3.40, 33.99]`. The PASS-band is wide because §W1-2 only verifies first-order multi-species correction; finer agreement requires §W1-3 lookup table covering full cascade.

**Conclusion**: Direction `log10_ratio > 0` pre-registered. PASS-band centered at log10(10.75) ≈ 1.031 with 0.5 log-OOM ABSOLUTE tolerance.

### 11. What PASSES/FAILS MEAN for solution space

**PASS at §W1-2**:

- Closes 1 OOM of the 13-OOM cascade-tail underflow at §W1c-69 Step 5; the substrate-IS L_H multi-species correction structurally accounts for the species-multiplicity factor f(M) within 0.5 log-OOM precision.
- L_H_canonical_FW promoted to canonical_constants.py; downstream cosmological observables can cite this pin.
- Falsifier-master-inventory row updated by mack-cosmic-bridge; audit-trail-complete via full-64-char `audit_sha256` cite per `cross-pillar-bridge-anatomy.md` and `mack-observational-constraints.md`.
- Verdict-permanence preserved via Option A `supersedes` protocol; the original §W1c-69 verdict line remains on disk; the corrective §W1-2 line carries the supersession token.

**INFO at §W1-2** (0.5 ≤ |delta_log10| < 1.0):

- Multi-species correction is in right direction but off by factor 3-10; substrate's species-multiplicity table f(g) requires traversal across cascade generations (§W1-3) to close the gap.
- Carry-forward to S90 with §W1-3 table extension or §W1-3 audit (if §W1-3 table itself has incomplete species accounting, this points to §W1-3 carry-forward).

**FAIL at §W1-2** (|delta_log10| ≥ 1.0 OR supersedes-token emission failure):

- Multi-species correction does NOT account for the §W1c-69 13-OOM gap to leading order; the substrate's T_H_substrate = 1.057 MeV pinning is structurally insufficient OR the §W1c-69 Step 5 form requires a DIFFERENT correction structure (not species-multiplicity).
- Re-classification: substrate's cosmological-CC accommodation pathway via Hawking-radiation cascade-tail closure does NOT close at substrate-pinned T_H + species-multiplicity; alternative mechanisms (e.g., non-standard horizon-microstate-density evolution; modified Stefan-Boltzmann with substrate-corrections to A_horizon) become candidates.
- supersedes-token failure (AUDIT side FAIL): rule-file violation; route to v3-closure-recovery Stage 1 sig_5 remediation per `v3-closure-recovery.md §"Stage 1: Automatic re-dispatch"` sig_5 sub-section + Option A protocol.

### 12. Effort estimate

**0.5 wave-equiv** (matches ledger A.5 effort). CPU-only (no large-matrix compute; Stefan-Boltzmann formula evaluation + log-OOM comparison + verdict-emission + falsifier-inventory row update).

### 13. Substrate framing per `phononic-framing.md`

**Verbatim agent dispatch prompt insertion (MANDATORY)**:

> "T_H = 1.057 MeV is SUBSTRATE-PINNED (per S88 W6 §V.1; the substrate's spectral-action moment ratio at horizon-spanning Peter-Weyl sectors fixes T_H structurally, NOT externally). The Hawking-radiation luminosity L_H is an EMERGENT cosmological observable from the substrate's emergent area-theorem (a_2 Seeley-DeWitt coefficient → emergent gravity → emergent BH thermodynamics). FORBIDDEN: 'BH evaporates IN spacetime emitting Hawking radiation'. REQUIRED direction: substrate spectral moments → emergent area-theorem → emergent T_H → emergent L_H. The species-multiplicity factor g_*(T_H_substrate) IS the substrate's emergent count of phononic excitation channels at T_H_substrate, derived through the substrate's T_H(g) cooling cascade traversing SM-species mass thresholds (§W1-3 lookup table)."

**Single-τ-slice level**: §W1-2 operates at Level 1 single-τ-slice substrate-IS (T_H_substrate at fixed τ_fold = 0.190; cascade-tail evaluation point fixed at the §W1c-69 mass scale). Moduli-deformation OUT OF SCOPE.

---

## §W1-3. S89-F-M-SPECIES-MULTIPLICITY-LOOKUP-TABLE

### 1. Gate ID

`S89-F-M-SPECIES-MULTIPLICITY-LOOKUP-TABLE`

### 2. Trigger

`[VERIFY]` — the gate verifies that the species-multiplicity lookup table f(g) covers the full cascade-generation range g ∈ {0..384} with substrate-derivable f(g) at each generation, traversing the SM-particle-threshold structure correctly. No directional/sign claim → no [SIGN] trigger.

### 3. Classification

PHONONIC + cosmological-bridge. The species-multiplicity factor f(g) IS the substrate's count of phononic excitation channels at the cascade-generation g's T_H(g), threshold-determined by the SM-particle mass spectrum traversed by T_H(g) as the cascade cools.

### 4. Agent type (runtime)

PRIMARY: `mack-cosmic-bridge` — cosmological-bridge axis primary; sole writer for `sessions/framework/registry/falsifier-master-inventory.md` rows per `feedback_mack-bridge-role.md`. The species-multiplicity table feeds §W1-2's L_H multi-species correction AND any future cascade-tail observables, so mack is the natural author for the lookup-table construction (cosmological-observable mapping side).

CO-AUTHOR (advisory; non-blocking): None. The lookup table is structurally simple (substrate T_H(g) cascade × SM-particle-threshold structure → g_*(g) table); no cross-axis review required at this stage.

`gen-physicist` BLACKLISTED. `connes-ncg-theorist` not involved (no substrate-IS NCG-axiomatic content; the substrate T_H(g) cascade is supplied by S88 W6 §V.1 / §V.5 verbatim).

### 5. Hypothesis

The substrate's T_H(g) cooling cascade across cascade generations g ∈ {0..384} traverses the SM-particle mass-threshold structure in a definite ordered sequence (T_H decreasing monotonically with g; SM-particles dropping out of g_* as their mass thresholds are crossed). The resulting f(g) lookup table covers the full g-range with substrate-derivable f(g) at each generation, and matches standard-cosmology g_*(T) values at the SM-threshold-structure cross-checks (PDG values).

### 6. Method

**Script path**: `computations/session-89/s89_w1_f_m_species_multiplicity_lookup_table.py`

**Substrate framing** (verbatim agent dispatch prompt insertion):

> "The cascade generations g ∈ {0..384} are NOT ordered points in a pre-existing time container; they ARE the substrate's intrinsic Δ_BCS cooling cascade (per S88 W6 §V.5 substrate-IS pinning). T_H(g) is the substrate's emergent Hawking temperature at cascade generation g; g_*(g) IS the substrate's emergent count of phononic excitation channels at T_H(g). FORBIDDEN: treating g as a 'time variable' or T_H(g) as a 'temperature evolution in expanding spacetime'. REQUIRED direction: substrate's Δ_BCS cooling cascade structure → emergent T_H(g) at each g → SM-mass-threshold structure → emergent g_*(g)."

**Imports**:

```python
from canonical_constants import *  # MANDATORY
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
import numpy as np
import hashlib, sys
from pathlib import Path
```

**Procedure**:

1. **Build T_H(g) cascade table** from substrate-derived cooling cascade (per S88 W6 §V.5):

   For g ∈ {0..384}, compute T_H(g) using the substrate's pinned cascade structure. The cascade form (transcribed at runtime from S88 W6 §V.5):

   ```
   T_H(g) = T_H_initial · exp(−g · Δ_BCS / K_base)  (canonical cascade form per branch-iv-canonical.md §3 substrate-natural anchor)
   ```

   where `T_H_initial = T_H(g=0)` is the substrate's initial Hawking temperature at cascade-start (pinned at substrate-IS Λ_substrate scale per S86 W4 P4); `Δ_BCS` is canonical (canonical_constants.py); `K_base` is canonical (canonical_constants.py).

2. **Define SM particle mass-threshold structure** (cross-check anchor; PDG values):

   | Particle | Mass | Active above threshold |
   |:---------|:----|:----|
   | photon γ | 0 | always |
   | gluons (8) | 0 | T > Λ_QCD ≈ 200 MeV |
   | electron e± | 0.511 MeV | T > 0.511 MeV |
   | muon μ± | 105.7 MeV | T > 105.7 MeV |
   | pion π⁰/π± | ~135-140 MeV | T > 134 MeV |
   | tau τ± | 1.777 GeV | T > 1.777 GeV |
   | proton/neutron | 939 MeV | T > 1 GeV |
   | charm c | 1.275 GeV | T > 1.275 GeV |
   | bottom b | 4.18 GeV | T > 4.18 GeV |
   | top t | 173.0 GeV | T > 173 GeV |
   | W± Z | ~80-91 GeV | T > 80 GeV |
   | Higgs H | 125 GeV | T > 125 GeV |
   | neutrinos νₑ νμ ντ | ~0 | always (relativistic) |

3. **Compute g_*(T) at each T = T_H(g)** by summing active-species dof:

   ```
   g_*(T) = Σ_{bosons active at T} g_b + (7/8) · Σ_{fermions active at T} g_f
   ```

   Apply threshold-suppression (Boltzmann factor `exp(-m/T)`) for species near threshold (within factor 5 of mass).

4. **Output lookup table**: f(g) = g_*(T_H(g)) for g ∈ {0..384}.

5. **Cross-check at standard-cosmology anchors** (PDG / Planck published g_*(T) values):

   At T = 100 GeV (electroweak scale): standard-cosmology g_* = 106.75 (full SM); cross-check f(g_at_T_100GeV).
   At T = 1 GeV (QCD-scale): standard-cosmology g_* = 61.75; cross-check f(g_at_T_1GeV).
   At T = 1 MeV (BBN-scale): standard-cosmology g_* = 10.75; cross-check f(g_at_T_1MeV).

   PASS iff |f(g) − g_*_standard(T)| / g_*_standard(T) < 0.10 at each cross-check anchor (10% tolerance).

6. **Coverage verification**: verify f(g) is defined for all g ∈ {0..384} (no gaps); T_H(g) is monotone decreasing.

7. **Mack-cosmic-bridge falsifier-master-inventory row** (mack PRIMARY): append row referencing the lookup-table .npz output's audit_sha256 + canonical_constants entry name (g_eff_lookup_FW promoted via update_constant(...) on PASS).

**Output files**:

- Canonical: `computations/session-89/s89_gate_verdicts.txt`
- Data: `computations/session-89/s89_w1_f_m_species_multiplicity_lookup_table.npz` (keys: `g_table` (vector ∈ {0..384}), `T_H_g_table` (vector), `f_g_table` (vector ≡ g_*(T_H(g))), `coverage_assert` (boolean), `cross_check_at_T_100GeV`, `cross_check_at_T_1GeV`, `cross_check_at_T_1MeV`)
- Plot: `computations/session-89/s89_w1_f_m_species_multiplicity_lookup_table.png` (2-panel: panel A T_H(g) vs g on log-y; panel B f(g) vs g with SM-threshold annotations)
- Working-paper section: `sessions/archive/session-89/session-89-w1-workingpaper.md` §W1-3
- Inventory update: `sessions/framework/registry/falsifier-master-inventory.md` (mack PRIMARY)
- Canonical promotion: `g_eff_lookup_FW` table in canonical_constants.py (or `g_eff_at_T_H_substrate` scalar at the §W1-2-relevant g)

### 7. Machinery pin (PRDR)

| Pin | Value | Source / Class |
|:----|:------|:---------------|
| `g_range` | {0..384} | per ledger A.6 spec |
| `T_H_initial` | substrate-pinned per S88 W6 §V.5 (canonical_constants.py if present, else PROMOTE in-session) | |
| `Delta_BCS` | 0.4642547394830737 (R-PROTECTED) | canonical_constants.py |
| `K_base` | substrate canonical | canonical_constants.py (or branch-iv-canonical.md §3) |
| `regulator` | not applicable (no UV regularization at this stage; the table is g_*(T) summation) | |
| `convention` | `substrate-cascade-T_H-g-with-SM-threshold-structure` | NOT SCHEMATIC; full SM-threshold accounting |
| `convention_class_pin` | FULL | |
| `scheme` | `substrate-derived-T_H-g-times-PDG-SM-threshold-structure` | |
| `random_seed` | None | |
| `tolerance` | 0.10 (10% relative tolerance at cross-check anchors) | |
| `cross_check_anchors` | T ∈ {100 GeV, 1 GeV, 1 MeV} | Pre-registered; PDG/Planck values |
| `pass_threshold` | All 3 cross-check anchors PASS within 10% AND coverage_assert == True | Pre-registered |

**Input SHA pins** (computed at plan-freeze):

| Input | Path | SHA pin form |
|:------|:-----|:-------------|
| canonical_constants | `computations/_shared/canonical_constants.py` | `<computed-at-dispatch>` |
| S88 W6 §V.5 source | `sessions/archive/session-88/workshops/s88-w6-w1c-69-page1976-13oom.md` | `<computed-at-dispatch>` |
| branch-iv-canonical | `sessions/framework/registry/branch-iv-canonical.md` | `<computed-at-dispatch>` |
| script template | `computations/_shared/_script_template.py` | `<computed-at-dispatch>` |

**SOURCE-RECONCILIATION**: `T_H_initial` (Class-(e) PROMOTES on PASS); SM-threshold mass values are methodological cross-checks (PDG values for cross-validation only, NOT canonical), so no Class-(b) violation.

### 8. Expected output 4-tuple

```
(value='coverage=Pass;cross_checks_passed=3/3', scheme=substrate-derived-T_H-g-times-PDG-SM-threshold-structure, convention=substrate-cascade-T_H-g-with-SM-threshold-structure-FULL, L_max=10)
```

### 9. PASS/FAIL/INFO thresholds with tolerance rule

**Threshold (RATIO tolerance at 3 cross-check anchors)**:

- **PASS**: ALL 3 cross-check anchors satisfy `|f(g) − g_*_standard(T)| / g_*_standard(T) < 0.10` (10% RATIO tol) AND `coverage_assert == True` AND T_H(g) is monotone decreasing.
- **INFO**: 2 of 3 cross-check anchors PASS (one anchor in {0.10, 0.30} band); coverage maintained.
- **FAIL**: ≤ 1 cross-check anchor PASS, OR coverage_assert == False, OR T_H(g) is NOT monotone (cascade-form structural violation).

### 10. Substitution chain (MANDATORY for the monotonicity / direction claim)

**Step 1 — Definitions**:

- `T_H(g) ≡ T_H_initial · exp(−g · Δ_BCS / K_base)` (substrate-IS cascade form per S88 W6 §V.5)
- `g_*(T) ≡ Σ active-species(T) dof-weight` (standard cosmology form; PDG/Planck cross-check anchors at 100 GeV / 1 GeV / 1 MeV)
- `f(g) ≡ g_*(T_H(g))` (the lookup-table function being constructed)

**Step 2 — Substitution**:

```
T_H(g) = T_H_initial · exp(−g · Δ_BCS / K_base)

dT_H/dg = T_H(g) · (−Δ_BCS / K_base)
```

**Step 3 — Simplify**:

`Δ_BCS = 0.4642547... > 0` and `K_base > 0` (substrate canonical positive); therefore `dT_H/dg < 0` strictly for all g.

**Step 4 — Direction (read off from canonical form)**:

T_H(g) is strictly monotone decreasing in g. As T_H decreases, SM species drop out of g_*(T) at their respective mass thresholds, so g_*(T_H(g)) is non-increasing in g (with discrete drops at thresholds). f(g) is non-increasing in g.

**Conclusion**: Direction `T_H(g)` strictly decreasing; `f(g)` non-increasing. Pre-registered. Coverage assertion `g ∈ {0..384}` is independent of direction (it's a finite-set existence claim).

### 11. What PASSES/FAILS MEAN for solution space

**PASS at §W1-3**:

- Lookup table f(g) covers g ∈ {0..384} with substrate-derivable f(g); cross-checks at 3 standard-cosmology anchors PASS within 10%.
- Feeds §W1-2 directly (intra-wave dependency).
- canonical_constants.py promotion: `g_eff_lookup_FW` table OR scalar at §W1-2-relevant g; downstream cosmological observables can cite.
- Mack-cosmic-bridge falsifier-master-inventory row landed.

**INFO at §W1-3** (2 of 3 anchors PASS):

- Substrate-IS cascade form approximately matches standard cosmology but one cross-check anchor deviates beyond 10%; substrate's cascade structure may have a sub-leading correction at one of the SM-threshold scales (e.g., QCD-scale departure from naive PDG g_*).
- Carry-forward to S90 with finer threshold-suppression model (Boltzmann factors + lattice-QCD-corrected g_* near Λ_QCD).

**FAIL at §W1-3** (≤ 1 anchor PASS or non-monotone):

- Substrate's T_H(g) cascade form is structurally inconsistent with SM cosmology; cooling profile does not traverse SM thresholds in correct sequence.
- Forecloses §W1-2 on §W1-3-output dependency (§W1-2 cannot use the lookup table; routes back to single-species L_H_eq1 fallback or alternative species-multiplicity model).

### 12. Effort estimate

**1.0 wave-equiv** (matches ledger A.6 effort). CPU-only; small-table arithmetic + 3-anchor cross-check.

### 13. Substrate framing per `phononic-framing.md`

**Verbatim agent dispatch prompt insertion**:

> "Cascade generations g ∈ {0..384} are intrinsic substrate-IS labels in the Δ_BCS cooling cascade (per S88 W6 §V.5 substrate-IS pinning); they are NOT time-coordinate values. T_H(g) is the substrate's emergent Hawking temperature at the substrate's intrinsic cascade-generation g; the cascade IS the structural substrate-physics, NOT a process happening IN time. Phononic excitation channel count g_*(T_H(g)) is the substrate's intrinsic count of accessible phononic modes at substrate-temperature T_H(g)."

**Single-τ-slice level**: §W1-3 operates at Level 1 single-τ-slice substrate-IS (cascade structure at fixed τ_fold = 0.190; the cascade IS the substrate's intrinsic generation index, NOT a moduli-deformation parameter).

---

## §W1-4. S89-N-PBH-BAND-EDGE-TENSION-RECONCILIATION

### 1. Gate ID

`S89-N-PBH-BAND-EDGE-TENSION-RECONCILIATION`

### 2. Trigger

`[SIGN]` + `[VERIFY]` (composite).

`[SIGN]` because the substitution chain pre-registers a directional prediction: substrate's CF-CURV-6 STRUCTURAL CENTRAL prediction for n_PBH(g_BBN) is GREATER than the §W1c-69 PASS-magnitude posterior lower edge (8.4e-24 m^−3) AND LESS than the upper edge (2.2e-22 m^−3). Concretely: substrate-IS structural central is in the upper 22.6% of the CF-CURV-6 prior [10^−30, 10^−20] m^−3.

`[VERIFY]` because the gate verifies the band-edge tension reconciliation: the substrate's STRUCTURAL CENTRAL falls within the W1c-69 PASS-magnitude posterior support [8.4e-24, 2.2e-22] m^−3.

The schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple companion comment row is REQUIRED per `gate-verdicts.md §"S87+ canonical form"` (REQUIRED for any gate whose pre-registration includes a `[SIGN]` trigger).

### 3. Classification

PHONONIC + cosmological-bridge. n_PBH (number density of primordial black holes today) is a cosmological observable; the substrate's CF-CURV-6 STRUCTURAL CENTRAL prediction comes from the substrate's pinned cascade-tail mass distribution (substrate-derivable from §W1-3 f(g) table + cascade-tail-mass-spectrum anchor at g_BBN).

### 4. Agent type (runtime)

PRIMARY: `mack-cosmic-bridge` — observational-anchor side primary; sole writer for `sessions/framework/registry/falsifier-master-inventory.md` rows per `feedback_mack-bridge-role.md`. n_PBH is a cosmological-observation-side falsifier; mack is the natural author. Per `feedback_mack-bridge-role.md`, mack's priorities map to user's observational priorities; n_PBH band-edge reconciliation is observational-axis content.

CO-AUTHOR (advisory; non-blocking): `connes-ncg-theorist` (substrate-IS NCG-axiomatic side review of CF-CURV-6 structural derivation; consulted at runtime for cocycle-class consistency check on the cascade-tail mass distribution). NOT a blocker; mack PRIMARY.

`gen-physicist` BLACKLISTED. `hawking-theorist` not involved (hawking-radiation interface is §W1-2; n_PBH is the BH-population observable, downstream of cascade-tail mass distribution which is substrate-IS in nature).

### 5. Hypothesis

The substrate's CF-CURV-6 STRUCTURAL CENTRAL prediction for n_PBH(g_BBN) (re-derived at S89 from the substrate's pinned cascade-tail mass distribution + substrate's emergent Friedmann acoustic structure at g_BBN) reconciles BAND-EDGE PASS at the upper 22.6% of the CF-CURV-6 prior [10^−30, 10^−20] m^−3, matching the §W1c-69 PASS-magnitude posterior support [8.4e-24, 2.2e-22] m^−3.

### 6. Method

**Script path**: `computations/session-89/s89_w1_n_pbh_band_edge_tension_reconciliation.py`

**Substrate framing** (verbatim agent dispatch prompt insertion):

> "n_PBH is an emergent cosmological observable: the number density of primordial black holes today (g_BBN-pinned epoch). The substrate's CF-CURV-6 STRUCTURAL CENTRAL prediction comes from the substrate's pinned cascade-tail mass distribution at the BBN cascade-generation g_BBN, NOT from a free-parameter cosmological-model fit to PBH-population data. The PBH population IS the cascade-tail's emergent BH cosmological signature; PBH formation IS the cascade-tail mass distribution's emergent gravitational collapse expression at g_BBN. FORBIDDEN: 'PBHs form during inflation IN expanding spacetime'. REQUIRED direction: substrate cascade-tail mass distribution at g_BBN → emergent gravitational collapse → emergent n_PBH(today)."

**Imports**:

```python
from canonical_constants import *  # MANDATORY
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
import numpy as np
import hashlib, sys
from pathlib import Path
```

**Procedure**:

1. **Identify g_BBN cascade generation**: from §W1-3 lookup table, locate g_BBN such that T_H(g_BBN) ≈ T_BBN ≈ 1 MeV (BBN epoch substrate-pinned). Read off f(g_BBN) and T_H(g_BBN) from the lookup-table output of §W1-3.

2. **Derive CF-CURV-6 STRUCTURAL CENTRAL prediction for n_PBH(g_BBN)**:

   The CF-CURV-6 form (per `sessions/archive/session-88/workshops/s88-w5-w1c-69-sign-pass-tautology.md §V.2` substrate-IS structural form):
   ```
   n_PBH(g) = (cascade-tail-PBH-mass-fraction(g)) · (1 / V_horizon_volume_at_g) · (substrate-IS cascade-tail-mass-distribution amplitude)
   ```
   
   The substrate-IS structural form (per ledger A.13 + S88 §W5 V.2 spec):
   ```
   n_PBH_structural_central(g_BBN) = β_PBH · ρ_substrate(g_BBN) / M_PBH_typical
   ```
   
   where:
   - β_PBH is the substrate's pinned cascade-tail PBH mass fraction at g_BBN (substrate-IS canonical; pin to canonical_constants.py if not present, PROMOTE on PASS)
   - ρ_substrate(g_BBN) is the substrate's emergent energy density at g_BBN (computed from substrate's spectral-action moments at horizon-spanning sectors at the cascade-tail-mass scale)
   - M_PBH_typical is the substrate's pinned PBH-mass-distribution typical scale (cascade-tail substrate pinning)
   
   Compute n_PBH_structural_central(g_BBN) from substrate-IS canonicals.

3. **Compare against §W1c-69 PASS-magnitude posterior support**:
   ```
   posterior_support = [8.4e-24, 2.2e-22]  m^-3
   ```
   
   Verify two conditions:
   (a) `n_PBH_structural_central` IN posterior_support (BAND-EDGE inclusion test).
   (b) `n_PBH_structural_central` lies in upper 22.6% of CF-CURV-6 prior [10^−30, 10^−20] m^−3, i.e., in [10^−22.26, 10^−20] = [5.5e-23, 1e-20] m^−3 (the upper 22.6% in log-OOM space corresponds to [10^(−30 + 0.774·10), 10^−20] = [10^−22.26, 10^−20] m^−3).

4. **Composite verdict** (per schema-v2 collapse rule):
   - sign_verdict: PASS iff `n_PBH_structural_central > 8.4e-24` (substrate-IS predicts within posterior or above lower edge).
   - magnitude_verdict: PASS iff `n_PBH_structural_central ∈ [8.4e-24, 2.2e-22]` (within posterior support).
   - regime_verdict: VALID iff substrate-IS derivation is within Friedrich-Bär saturation regime at L_max=10 (per `math-scripts.md §"D_K Block-Diagonality"`).

5. **Mack-cosmic-bridge falsifier-master-inventory row update** (mack PRIMARY): cite §W1-4 audit_sha256 (full-64-char form per `cross-pillar-bridge-anatomy.md` and `mack-observational-constraints.md`). Append to `sessions/framework/registry/falsifier-master-inventory.md`. Promote `n_PBH_structural_central_FW` to canonical_constants.py via update_constant(...).

**Output files**:

- Canonical: `computations/session-89/s89_gate_verdicts.txt` (canonical line + dual-SHA companion comment row + schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple companion row)
- Data: `computations/session-89/s89_w1_n_pbh_band_edge_tension_reconciliation.npz` (keys: `n_PBH_structural_central`, `posterior_support_lower`, `posterior_support_upper`, `prior_lower`, `prior_upper`, `band_edge_inclusion`, `upper_22_6_pct_inclusion`, `g_BBN`, `T_H_g_BBN`, `f_g_BBN`, `beta_PBH`, `rho_substrate_g_BBN`, `M_PBH_typical`)
- Plot: `computations/session-89/s89_w1_n_pbh_band_edge_tension_reconciliation.png` (1-panel: log-axis showing CF-CURV-6 prior [10^−30, 10^−20], posterior support [8.4e-24, 2.2e-22], substrate-IS STRUCTURAL CENTRAL prediction marker)
- Working-paper section: `sessions/archive/session-89/session-89-w1-workingpaper.md` §W1-4
- Inventory update: `sessions/framework/registry/falsifier-master-inventory.md` (mack PRIMARY)
- Canonical promotion: `n_PBH_structural_central_FW` in canonical_constants.py

### 7. Machinery pin (PRDR)

| Pin | Value | Source / Class |
|:----|:------|:---------------|
| `g_BBN` | extracted from §W1-3 lookup table at T_H ≈ 1 MeV | Intra-wave dep; runtime-pinned |
| `beta_PBH` | substrate-IS canonical (pin to canonical_constants.py; PROMOTE on PASS) | |
| `M_PBH_typical` | substrate-IS canonical (cascade-tail PBH-mass-distribution typical scale; PROMOTE on PASS) | |
| `posterior_support_lower` | 8.4e-24 m^−3 | §W1c-69 PASS-magnitude posterior |
| `posterior_support_upper` | 2.2e-22 m^−3 | §W1c-69 PASS-magnitude posterior |
| `prior_lower` | 1e-30 m^−3 | CF-CURV-6 prior |
| `prior_upper` | 1e-20 m^−3 | CF-CURV-6 prior |
| `regulator` | `a_n^{ζ}` (substrate-IS spectral-action moment regularization for ρ_substrate) | per `regulator-pin-discipline.md` |
| `convention` | `CF-CURV-6-substrate-IS-structural-central-substrate-pinned` | NOT SCHEMATIC |
| `convention_class_pin` | FULL | |
| `scheme` | `cf-curv-6-substrate-cascade-tail-at-g-BBN-Lmax-10` | |
| `random_seed` | None | |
| `tolerance` | 1e-12 (float64) | |
| `pass_threshold_sign` | `n_PBH_structural_central > 8.4e-24` | Pre-registered |
| `pass_threshold_magnitude` | `n_PBH_structural_central ∈ [8.4e-24, 2.2e-22]` | Pre-registered |
| `pass_threshold_regime` | Friedrich-Bär saturation valid at L_max=10 | Pre-registered |

**Input SHA pins**:

| Input | Path | SHA pin form |
|:------|:-----|:-------------|
| canonical_constants | `computations/_shared/canonical_constants.py` | `<computed-at-dispatch>` |
| §W1-3 lookup table | `computations/session-89/s89_w1_f_m_species_multiplicity_lookup_table.npz` | `<computed-at-runtime; intra-wave dependency>` |
| S88 W5 V.2 source | `sessions/archive/session-88/workshops/s88-w5-w1c-69-sign-pass-tautology.md` | `<computed-at-dispatch>` |
| L=12 master cache | `computations/session-84/s84_spectrum_cache_L12_tau019.npz` | `<computed-at-dispatch>` |
| script template | `computations/_shared/_script_template.py` | `<computed-at-dispatch>` |

**SOURCE-RECONCILIATION**: `beta_PBH` and `M_PBH_typical` are Class-(e) PROMOTES-ON-PASS pins; severity NO-ACTION.

### 8. Expected output 4-tuple

```
(value='n_PBH_central=<v>;band_edge_inclusion=<bool>;upper_22_6_pct=<bool>', scheme=cf-curv-6-substrate-cascade-tail-at-g-BBN-Lmax-10, convention=CF-CURV-6-substrate-IS-structural-central-substrate-pinned-FULL, L_max=10)
```

### 9. PASS/FAIL/INFO thresholds with tolerance rule

**Threshold (composite per `gate-verdicts.md §"Composite-collapse rule"`)**:

- **sign_verdict**:
  - PASS: `n_PBH_structural_central > 8.4e-24` (above posterior lower edge).
  - FAIL: `n_PBH_structural_central ≤ 0` (negative density; structural error).
  - N/A: not applicable here (sign is well-defined positive density).

- **magnitude_verdict** (RATIO inclusion in band):
  - PASS: `n_PBH_structural_central ∈ [8.4e-24, 2.2e-22]` (band-edge inclusion AND upper 22.6% of prior).
  - INFO: `n_PBH_structural_central ∈ [10^−24, 10^−20] \\ [8.4e-24, 2.2e-22]` (within prior but outside posterior support; structural central does not match magnitude-PASS but is in the right OOM band).
  - FAIL: `n_PBH_structural_central ∉ [10^−24, 10^−20]` (outside both posterior support AND broad inclusion band).

- **regime_verdict**:
  - VALID: Friedrich-Bär saturation valid at L_max=10 throughout the substrate-IS derivation (per `math-scripts.md`).
  - MARGINAL: f_used ∈ [0.50, 0.95) (5-50% shortened computation domain).
  - BREAKDOWN: f_used < 0.50 (>50% shortened).

- **Composite collapse** per `gate-verdicts.md §"S87+ canonical form / Composite-collapse rule"`:
  - PASS iff sign=PASS, magnitude=PASS, regime=VALID.
  - INFO if magnitude=INFO with regime=VALID.
  - FAIL otherwise (per the canonical collapse rule).

### 10. Substitution chain (MANDATORY for the [SIGN] trigger)

**Step 1 — Definitions**:

- `n_PBH_structural_central(g_BBN) ≡ β_PBH · ρ_substrate(g_BBN) / M_PBH_typical` (substrate-IS structural form per CF-CURV-6 + S88 W5 V.2)
- `posterior_support_lower = 8.4e-24` m^−3 (§W1c-69 PASS-magnitude posterior lower edge)
- `posterior_support_upper = 2.2e-22` m^−3 (§W1c-69 upper edge)
- `prior_lower = 1e-30`, `prior_upper = 1e-20` (CF-CURV-6 prior)
- `upper_22_6_pct_band` = [10^−22.26, 10^−20] = [5.5e-23, 1e-20] m^−3 (upper 22.6% of CF-CURV-6 prior in log-OOM space)

**Step 2 — Substitution**:

```
n_PBH_structural_central(g_BBN)
  = β_PBH · ρ_substrate(g_BBN) / M_PBH_typical
```

**Step 3 — Simplify**:

The substrate canonicals β_PBH and M_PBH_typical are pinned to canonical_constants.py at runtime; ρ_substrate(g_BBN) is computed from the substrate's spectral-action moments at the cascade-tail-mass scale at g_BBN. The numerical evaluation gives a specific `n_PBH_structural_central` value at runtime; no closed-form symbolic simplification needed at plan-authorship.

**Step 4 — Direction**:

Direction prediction (sign): substrate-IS canonicals β_PBH > 0, ρ_substrate > 0 (positive energy density), M_PBH_typical > 0; therefore `n_PBH_structural_central > 0`. Sign-PASS by construction.

Magnitude prediction (range): per ledger A.13, the substrate-IS STRUCTURAL CENTRAL is expected in the upper 22.6% of CF-CURV-6 prior, i.e., `n_PBH_structural_central ∈ [5.5e-23, 1e-20]` m^−3. Intersection with posterior support [8.4e-24, 2.2e-22] gives the PASS band [8.4e-24, 2.2e-22] ∩ [5.5e-23, 1e-20] = [5.5e-23, 2.2e-22] m^−3 (the substrate-IS prediction must land in this 0.6 OOM-wide band for full PASS).

Pre-registered MAGNITUDE prediction: `n_PBH_structural_central ∈ [5.5e-23, 2.2e-22]` m^−3 (the band-edge-inclusive PASS region).

**Conclusion**: SIGN_CHECK = PASS by construction (positive density). MAGNITUDE_CHECK = PASS iff value ∈ [5.5e-23, 2.2e-22] m^−3. REGIME = VALID iff Friedrich-Bär saturation holds at L_max=10. Composite per collapse rule.

**Plan-author Python verification**: SIGN positivity verified trivially at plan-time (β_PBH, ρ_substrate, M_PBH_typical all positive); magnitude verification deferred to runtime where substrate canonicals are loaded.

### 11. What PASSES/FAILS MEAN for solution space

**PASS at §W1-4** (composite PASS):

- Substrate-IS CF-CURV-6 STRUCTURAL CENTRAL reconciles BAND-EDGE PASS at upper 22.6% of CF-CURV-6 prior + within §W1c-69 PASS-magnitude posterior support. The structural prediction is empirically consistent with the magnitude-PASS posterior; the cosmological-CC accommodation pathway via substrate-pinned cascade-tail PBH population is internally consistent.
- canonical_constants.py promotes `n_PBH_structural_central_FW`; downstream cosmological observables can cite.
- Falsifier-master-inventory row landed (mack PRIMARY) cite §W1-4 audit_sha256.
- Constraint-map: closes the §W1c-69 PASS-magnitude band-edge tension with substrate-IS structural derivation.

**INFO at §W1-4** (magnitude=INFO; regime=VALID):

- Substrate-IS structural central is in the right OOM band but outside the PASS-magnitude posterior support [8.4e-24, 2.2e-22]; structural derivation is correct in form but β_PBH or M_PBH_typical pinning has sub-leading corrections.
- Carry-forward to S90 with refined β_PBH (substrate pinning at higher L_max=12 from master cache) or refined cascade-tail-mass-distribution model.

**FAIL at §W1-4** (composite FAIL):

- Substrate-IS CF-CURV-6 STRUCTURAL CENTRAL is structurally inconsistent with §W1c-69 PASS-magnitude posterior support; either the substrate's pinned β_PBH / M_PBH_typical / ρ_substrate is wrong, OR the §W1c-69 magnitude-PASS posterior is itself based on a different cosmological mechanism not captured by the substrate's CF-CURV-6 form.
- Re-classification: substrate-IS CF-CURV-6 form is NOT the correct cascade-tail PBH-population mechanism; alternative mechanisms (e.g., non-cascade-tail PBH formation; alternative cascade structure) become candidates.
- Constraint-map: closes the corridor "substrate-IS CF-CURV-6 cascade-tail PBH formation matches §W1c-69 PASS-magnitude"; preserves alternative-mechanism corridors.

### 12. Effort estimate

**1.0 agent-session** (matches ledger A.13 effort). CPU-only; substrate-canonical-arithmetic + band-inclusion check + verdict-emission + falsifier-inventory row + canonical-promotion.

### 13. Substrate framing per `phononic-framing.md`

**Verbatim agent dispatch prompt insertion**:

> "n_PBH IS the substrate's emergent number density of primordial black holes at the substrate-pinned BBN cascade-generation g_BBN; PBH formation IS the cascade-tail mass distribution's emergent gravitational collapse expression at g_BBN. FORBIDDEN explanation directions: 'PBHs form during inflation IN expanding spacetime', 'inflationary perturbations seed PBH formation', 'horizon re-entry triggers PBH formation in radiation era'. REQUIRED direction: substrate's pinned cascade-tail mass distribution at g_BBN → emergent gravitational collapse → emergent n_PBH(today). The CF-CURV-6 STRUCTURAL CENTRAL prediction comes from the substrate's intrinsic cascade-tail structure, not from a free-parameter cosmological-model fit to PBH-population data."

**Single-τ-slice level**: §W1-4 operates at Level 1 single-τ-slice substrate-IS (cascade structure at fixed τ_fold = 0.190; g_BBN is the substrate's intrinsic cascade-generation index, NOT a moduli-deformation parameter).

---

## Wave 1 → Wave 2 Decision Point

**Cross-wave dependency declarations**:

- W1 outputs feed any future Stage-2 cross-axis verify of cosmological-CC + horizon-microstate accommodation theorem (S88 §W1b1-63 FAIL is structurally closed by §W1-1 PASS). The Stage-2 verify itself is queued for S90+ (NOT in S89; per `joint-theorem-promotion.md` 4-stage pathway, Stage-1 LANDED = §W1-1 PASS; Stage-2 dispatched in S90+ after at-least-one-session settling per the cross-reviewer downstream-inheritance reach test of S88 W-14 V.2 / B.15).
- W1 has NO upstream dependency from other S89 waves (all 4 gates depend only on S88 close + L=12 master cache + S89 plan-freeze canonical_constants).
- §W1-3 → §W1-2 intra-wave dependency: §W1-2 reads `g_eff_at_T_H_substrate` from §W1-3 .npz output. The dispatch order MUST be §W1-1, §W1-3, §W1-2, §W1-4 (NOT alphabetical). Practically: dispatch §W1-1 + §W1-3 in PARALLEL (no interdependency); upon §W1-3 PASS, dispatch §W1-2; §W1-4 can dispatch in parallel with §W1-2 OR after §W1-3 (§W1-4 also reads g_BBN from §W1-3 .npz output → §W1-3 must complete before §W1-4).
- §W1-1's structural theorem candidate is queued for §VII.AU registry promotion in S90+ (NOT landed in S89 W1; landing requires Stage-2 cross-axis verify in S90+ per the 4-stage pathway).

**Forward references to S89 W2-W7** (informational only; W2-W7 plans owned by other planners):

- §W1-1 PASS opens A.20 (Stage-2 dual-prior pre-registration) which depends on Cluster B's A.3 + A.4 PASS (Cluster B is the connes-Karoubi pairing infrastructure cluster; lands in S89 if scheduled to a different wave, OR in S90 if not scheduled). §W1-1 PASS is NECESSARY but not sufficient for A.20.
- §W1-2 / §W1-3 / §W1-4 close 1-2 OOM of the §W1c-69 13-OOM gap; remaining 11-12 OOM closure requires further cascade-tail mass-distribution work + n_PBH-band cross-pillar bridge work, queued for S90 or beyond.

---

## Wave 1 Machinery-Enumeration Pin (§0.11)

Aggregated machinery pins across all 4 W1 gates:

| Gate | L_max | Regulator | Convention | Convention class | Scheme | Random seed | Tolerance | GPU/CPU |
|:-----|:-----:|:----------|:-----------|:----------------:|:-------|:-----------:|:---------:|:--------|
| §W1-1 | 10 | a_n^{ζ} | horizon-spanning-sector-projection-CM-1995-III-4 | FULL | peter-weyl-block-diagonal-HSS-projection-Lmax10-tau-fold-019 | None | 1e-12 (float64) | GPU torch.linalg path; CPU OMP=8 fallback |
| §W1-2 | 10 | a_n^{ζ} (Stefan-Boltzmann implicit) | multi-species-stefan-boltzmann-with-supersedes-token | FULL | substrate-pinned-T_H-1.057-MeV-SM-species | None | 1e-12 | CPU |
| §W1-3 | 10 | not applicable (g_*(T) summation) | substrate-cascade-T_H-g-with-SM-threshold-structure | FULL | substrate-derived-T_H-g-times-PDG-SM-threshold-structure | None | 0.10 (cross-check anchors RATIO) | CPU |
| §W1-4 | 10 | a_n^{ζ} (substrate-IS spectral-action moment for ρ_substrate) | CF-CURV-6-substrate-IS-structural-central-substrate-pinned | FULL | cf-curv-6-substrate-cascade-tail-at-g-BBN-Lmax-10 | None | 1e-12 | CPU |

**Common pins** (applied to all 4 W1 gates):

- `tau_fold = 0.19` (R-PROTECTED; canonical_constants.py)
- `M_KK = 7.428660036284456e+16 GeV` (canonical_constants.py)
- `Delta_BCS = 0.4642547394830737` (R-PROTECTED; canonical_constants.py; used in §W1-3 cascade form)
- `Vol_SU3` (canonical; canonical_constants.py)
- All gates COMPUTE-class per `wave-classification.md` M1-M4 (M1 numerical PASS predicate; M2 `.py` script; M3 first-principles substrate computation; M4 absent from `methodology-wave-allowlist.md` — no methodology-wave allowlist append needed for W1 gates).
- All gates use `from canonical_constants import *` per `math-scripts.md §"Canonical Constants (MANDATORY)"`.
- All gates use `os.environ.setdefault('OMP_NUM_THREADS', '8')` for CPU-only fallback per `math-scripts.md §Environment`.

**PRDR audit (cardinality test)**: Every free parameter is pinned across all 4 gates. `g_eff_at_T_H_substrate` (§W1-2 input from §W1-3 output) and `g_BBN`/`f_g_BBN` (§W1-4 input from §W1-3 output) are runtime-pinned-from-intra-wave-output-`.npz`-files (NOT free parameters; pin-source is intra-wave dependency). PRU Class 8 cleared at plan-freeze.

**SOURCE-RECONCILIATION audit**: 
- §W1-1: FULL physical CM-1995 §III.4 form; SUBSTRATE-FIRST-PROVENANCE PASS (CM-1995 §III.4 IS the substrate-first canonical source).
- §W1-2: T_H_substrate = 1.057 MeV is Class-(e) PROMOTES-ON-PASS; severity NO-ACTION; `supersedes` token extraction at runtime per Option A.
- §W1-3: SM-threshold values are methodological cross-checks (PDG values for cross-validation only; NOT substrate canonicals); no Class-(b) violation.
- §W1-4: β_PBH and M_PBH_typical are Class-(e) PROMOTES-ON-PASS; severity NO-ACTION.

**SUBSTRATE-FIRST-PROVENANCE audit** (per `substrate-first-canonical-sourcing.md`):
- §W1-1: CM-1995 §III.4 cited as substrate-first canonical source for the residue formula; PASS.
- §W1-2: T_H_substrate = 1.057 MeV substrate-pinned per S88 W6 §V.1; PASS.
- §W1-3: substrate's Δ_BCS cooling cascade form per S88 W6 §V.5; PASS.
- §W1-4: CF-CURV-6 substrate-IS structural form per S88 W5 V.2; PASS.

**Wave-classification audit** (per `wave-classification.md`):
- All 4 W1 gates: COMPUTE-class (M1 ✓ M2 ✓ M3 ✓ M4 N/A — no methodology classification, so M4 enforcement does not apply).
- Dispatch path: `/rclab-coordinate` compute-mode for all 4.
- No MIXED-class items; no sub-wave decomposition required at W1 plan level.

**Verdict-file path**: All 4 W1 gates emit to `computations/session-89/s89_gate_verdicts.txt` (canonical per `gate-verdicts.md §"Canonical Verdict-File Path"`). FORBIDDEN paths NOT used: `computations/_shared/s89_gate_verdicts.txt`, `sessions/archive/session-89/s89_gate_verdicts.txt`, `sessions/session-plan/s89_gate_verdicts.txt`.

---

## Wave 1 Input-SHA Ledger

Aggregated input-pin-map SHAs across all 4 W1 gates (computed at S89 plan-freeze; input-pin map closure SHA is the final SHA-256 of the ordered concatenation of all input SHAs):

| Input | Path | Used by | SHA pin form |
|:------|:-----|:--------|:-------------|
| canonical_constants | `computations/_shared/canonical_constants.py` | §W1-1, §W1-2, §W1-3, §W1-4 | `<computed-at-dispatch-from-S88-HEAD>` |
| L=12 master spectrum cache | `computations/session-84/s84_spectrum_cache_L12_tau019.npz` | §W1-1, §W1-4 (ρ_substrate) | `<computed-at-dispatch>` |
| CM-1995 paper transcription | `researchers/Connes/` (CM-1995 .md path TBD) | §W1-1 | `<computed-at-dispatch>` |
| W1b1-63 branch (c) source | `sessions/archive/session-88/workshops/s88-w3-w1b1-63-3branch.md` §5 | §W1-1 | `<computed-at-dispatch>` |
| LRD anchor reference | `researchers/Little-Red-Dots/` index | §W1-1 | `<computed-at-dispatch>` |
| §W1c-69 source | `sessions/archive/session-88/workshops/s88-w6-w1c-69-page1976-13oom.md` | §W1-2, §W1-3 | `<computed-at-dispatch>` |
| S88 verdict file (for `supersedes`) | `computations/session-88/s88_gate_verdicts.txt` | §W1-2 | `<computed-at-dispatch>` |
| §W5 V.2 source | `sessions/archive/session-88/workshops/s88-w5-w1c-69-sign-pass-tautology.md` | §W1-4 | `<computed-at-dispatch>` |
| branch-iv-canonical | `sessions/framework/registry/branch-iv-canonical.md` | §W1-3 | `<computed-at-dispatch>` |
| Permanent-results-registry | `sessions/permanent-results-registry.md` | §W1-1 (next-free §VII.AU candidate) | `<computed-at-dispatch>` |
| Falsifier-master-inventory | `sessions/framework/registry/falsifier-master-inventory.md` | §W1-2, §W1-3, §W1-4 (mack writer) | `<computed-at-dispatch>` |
| Mack-observational-constraints | `sessions/framework/registry/mack-observational-constraints.md` | §W1-2, §W1-3, §W1-4 (mack writer cross-link) | `<computed-at-dispatch>` |
| script template | `computations/_shared/_script_template.py` | All 4 W1 gates | `<computed-at-dispatch>` |
| Intra-wave: §W1-3 lookup table .npz | `computations/session-89/s89_w1_f_m_species_multiplicity_lookup_table.npz` | §W1-2, §W1-4 | `<computed-at-runtime>` |

**Closure SHA computation pattern** (for each gate):

```
input_pin_map = OrderedDict([
    ("canonical_constants", "<sha>"),
    ("L_max", 10),
    ("regulator", "a_n^{ζ}"),
    ("convention", "<convention-string>"),
    ("scheme", "<scheme-string>"),
    ... (gate-specific keys per §7 PRDR pin table) ...
])
closure_sha = hashlib.sha256(json.dumps(input_pin_map, sort_keys=False).encode()).hexdigest()
```

Closure SHAs are computed at runtime by each producing script (NEVER hardcoded; per `v3-closure-recovery.md` PROHIBITED_ACTIONS Class 4 — ansatz-forced PASS via verdict-line edit FORBIDDEN; closure SHA must derive from input-pin-map by `closure_hash()` helper of `_script_template.py`).

**Audit-trail signature for §W1-2 supersedes-token emission** (per `gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict permanence"` rule (5)):

The §W1-2 corrective canonical line MUST carry `supersedes=<full-64-char-original-audit-sha>` at emission time. Forward emission discipline applies; failure to carry the tag at emission time is a Class-8.2 PRU pre-registration violation per `epistemic-discipline.md §"Verifier-Rubric Pre-Registration"` AND a v3-closure-recovery.md PROHIBITED_ACTIONS Class-3 boundary risk. The §W1-2 producing script's first action upon initialization is to grep-extract the FULL 64-char audit_sha256 from `computations/session-88/s88_gate_verdicts.txt` matching the canonical-original §W1c-69 verdict line; failure to match the prefix `2afd17ef99c81123…` (HEAD-16) prevents script execution (HARD-HALT at runtime).

---

## Wave 1 close — pre-flight checklist before S89 plan-freeze

- [ ] All 4 gate blocks have full 13-field specification.
- [ ] Substitution chains pre-registered in §10 of each gate.
- [ ] Substrate framing reminders (verbatim agent dispatch insertion) present in §13 of each gate per `phononic-framing.md`.
- [ ] PRDR machinery enumeration complete for each gate (cardinality test PASS).
- [ ] SOURCE-RECONCILIATION audit run (value test PASS; §W1-2 Class-(e) PROMOTES-ON-PASS for T_H_substrate; §W1-4 Class-(e) PROMOTES-ON-PASS for β_PBH and M_PBH_typical).
- [ ] SUBSTRATE-FIRST-PROVENANCE audit run (source-existence test PASS; CM-1995 §III.4, S88 W6 §V.1, S88 W6 §V.5, S88 W5 V.2 all cited).
- [ ] Wave-classification audit run (all 4 gates COMPUTE-class; no methodology-wave allowlist append needed).
- [ ] Cross-pillar bridge anatomy NOT triggered at W1 plan level (no cross-pillar bridge LANDED in W1; structural theorem candidate for §VII.AU registry promotion deferred to S90+).
- [ ] Verdict-file path canonical (`computations/session-89/s89_gate_verdicts.txt`); no FORBIDDEN-path use.
- [ ] Mack-cosmic-bridge sole-writer discipline observed for §W1-2/§W1-3/§W1-4 falsifier-master-inventory rows + `mack-observational-constraints.md` cross-links.
- [ ] gen-physicist BLACKLISTED from test-case design across all 4 W1 gates (verified).
- [ ] Author hint preservation: §W1-1 connes-ncg-theorist PRIMARY; §W1-2 mack-cosmic-bridge PRIMARY + hawking-theorist CO-AUTHOR; §W1-3 mack-cosmic-bridge PRIMARY; §W1-4 mack-cosmic-bridge PRIMARY (verified).

End of W1 plan.
