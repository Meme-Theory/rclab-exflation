#!/usr/bin/env python3
"""Atomic in-place WP §W7-5 substantive content replacement; survives parallel-
writer race by reading immediately before write and restricting the edit
target to the §W7-5 block (delimited by '### §W7-5.' and the next '### §W7-6.'
or '---' boundary marker)."""
from __future__ import annotations

import sys
from pathlib import Path

WP_PATH = Path(r"C:\sandbox\Ainulindale Exflation\sessions\archive\session-92\session-92-w7-workingpaper.md")

NEW_BODY = """### §W7-5. S92-W7-CF-W8-CONSOLIDATED-6-CF-W9-10-A-HH-1-FIRST-EXTRACTION-S4 (connes-ncg-theorist)

**Status**: COMPLETED
**Gate ID**: `S92-W7-CF-W8-CONSOLIDATED-6-CF-W9-10-A-HH-1-FIRST-EXTRACTION-S4`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (substrate-IS Hochschild-cocycle norm L_max-scan first-extraction at substrate-distance-2 pole `s=4` on M_3(ℂ) ⊂ A_K Wedderburn block via FULL CM-1995 §III.4 simple-pole residue evaluator + Friedrich-Bär saturation theorem)
**Agent**: `connes-ncg-theorist` (PRIMARY; `van-den-dungen-bridge-theorist` ALTERNATE for Kasparov KK-projection cross-check via sub-option (c) CONFIRMER re-run)
**Hypothesis**: The empirical HH^1 Hochschild-cocycle norm operational envelope `α_HH^1_emp(s=4)` at substrate-distance-2 pole on M_3(ℂ) ⊂ A_K at τ_fold = 0.19, extracted via FULL `_cm_1995_residue_formula.py` (NOT SCHEMATIC `_spectral_action_regulators.py` per `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY level-pin discipline) at L_max=14 master cache + Friedrich-Bär saturation per W11-3 precedent, falls inside the pre-registered band `[1.5, 4.0]` AND matches the Wodzicki/Connes d=4 substrate-physics prediction `α_HH^1(s) = 2(s − 2) → α_HH^1(s=4) = 4` within publication-precision floor (Class 8.3); replaces §VII.AZ.OP-PROJ Element 4 sub-class tag from REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION to STAGE-1-CANDIDATE-FIRST-EXTRACTED at S93+ via mack downstream gate.
**Plan reference**: `sessions/session-plan/session-92-plan-w7.md` §W7-5 (four sub-options (a) direct CM-1995 residue at s_0=4 / (b) Friedrich-Bär saturation analytical certification / (c) Casimir-bound cross-check W11-2 precedent / (d) Wodzicki/Connes d=4 prediction; decision predicate PASS/INFO/FAIL bands).

**Output Artifacts**:

| Artifact | Path | SHA / Verification |
|:---------|:-----|:-------------------|
| Producing script | `computations/session-92/s92_w7_5_hh_1_first_extraction_s4.py` | content_sha256=`0c73e292b383c74ce34e956bb9352fe973f598026febabfeba31565f3f884f56` |
| Data file (.npz) | `computations/session-92/s92_w7_5_hh_1_first_extraction_s4.npz` | 8.2 KB; `alpha_HH1_emp_s4=0.194312`, `norm_HH1_at_L{10,12,14}`, per-sector η_FB table (80 sectors), per-level partial sums, sub-option PASS/FAIL flags |
| Plot file (.png) | `computations/session-92/s92_w7_5_hh_1_first_extraction_s4.png` | 107 KB; 2-panel: (a) log-log fit with Wodzicki/Connes target reference line, (b) Casimir-bound truncation_consistent bar chart at L_op ∈ {6, 8, 10, 12, 14} |
| Verdict line | `computations/session-92/s92_gate_verdicts.txt` | `INFO -- ... audit_sha256=38ee9db31658bb25941ccdc2e2db3551f7db4b0379d802d1043c8c45a9522cf6 content_sha256=0c73e292b383c74ce34e956bb9352fe973f598026febabfeba31565f3f884f56 schema_version=S87+` |
| Dual-SHA companion | same file | `# audit_sha256_short=38ee9db31658bb25 content_sha256_short=0c73e292b383c74c` |
| Schema-v2 3-tuple companion | same file | `# sign_verdict=PASS magnitude_verdict=INFO regime_verdict=VALID` |
| 4-axis level-pin companion | same file | `# LEVEL_CLASS_PIN=FULL MACHINERY_SCOPE_PIN=CACHE-PROJECTION BINDING_AXIS_PIN=substrate-natural-binding A_N_REGULATOR_PIN=a_2^{Mellin}` |

Must-contain pattern verification (grep against `s92_w7_5_hh_1_first_extraction_s4.py`):

- `from canonical_constants import` — PRESENT (`from canonical_constants import *` after sys.path insertion)
- `append_verdict` — PRESENT (function `append_verdict_line` defined; called once at end of `main()`)
- `from _cm_1995_residue_formula import` — PRESENT (imports `su3_casimir`, `su3_dimension`, `CLASS`, `REGULATOR_PIN`)
- `s_0 = 4` — PRESENT (`s_0 = 4  # (local) substrate-distance-2 pole`)
- `alpha_HH1_emp` — PRESENT (variable name; appears 50+ times)
- `friedrich_bar` — PRESENT (function `friedrich_baer_tail_bound_s4`)
- `M_3` — PRESENT (`M3C_PETER_WEYL_BLOCK_INDEX`, `is_m3c_sector`)
- `FULL` — PRESENT (`LEVEL_PIN = "FULL"`; convention suffix `substrate-distance-2-pole-s4-FULL`)

**MCP Pre-Compute Audit**:

| Query | Tool | Salient return |
|:------|:-----|:----------------|
| `HH^1 first-extraction substrate-distance-2 pole M_3 Hochschild` | `mcp__knowledge__search_knowledge` | 8 hits; no prior closure of HH^1 first-extraction at substrate-distance-2 pole s=4 in L_max=14 cache; S91 §W9-10 baseline at substrate-distance-1 pole s=3 (`s91_w9_hh1_finite_alpha_first_extraction.py`) is structurally distinct (different pole, Mellin exponent -6 vs -8). |
| `CM-1995 residue formula` | `mcp__knowledge__trace_entity` | No trace; module `_cm_1995_residue_formula.py` not yet indexed. Direct file inspection used. |
| `M_KK` | `mcp__knowledge__get_constant` | Value `7.428660036284456e+16`; no PROVENANCE entry. Used by `_cm_1995_residue_formula.py` via `from canonical_constants import M_KK, tau_fold`. |
| `Friedrich-Bar saturation theorem L_max W11-3` | `mcp__knowledge__search_knowledge` | 5 hits; theorem PROVEN (S87 W11-3 origin; S88 W11-3 calibration; S89 W3-1 PASS LANDED; S90 W6 CF-47 analogue). `eta_FB_lower = 0.40` is canonical 8.4% safety margin below empirical floor 0.4365 at sector (1,1). Pin re-used here. |

Status: **NOT PRE-CLOSED**. First-extraction at substrate-distance-2 pole s=4 on L_max=14 master cache is a new substrate-physics evaluation.

**Verdict**: **INFO**

| Component | Value |
|:----------|:------|
| Composite | **INFO** |
| sign_verdict | **PASS** (`α_HH^1_emp(s=4) = 0.194312 > 0`; Wodzicki/Connes d=4 direction confirmed) |
| magnitude_verdict | **INFO** (`α ∈ (0, 1.5)`; below PASS band `[1.5, 4.0]`; matches plan §W7-5 INFO band direction-matches case) |
| regime_verdict | **VALID** (Friedrich-Bär saturation operates throughout L_scan; truncation_consistent across `L_op ∈ {6, 8, 10, 12, 14}`) |

**Results**:

#### 1. Empirical first-extraction at substrate-distance-2 pole `s_0 = 4`

Per-L HH^1 cocycle norm on M_3(ℂ) ⊂ A_K Wedderburn block at Mellin exponent `-2s = -8`:

| L_max | norm_HH^1 | n_sectors_M3(C) | η_FB_floor_observed | η_FB ≥ 0.40 satisfied |
|:------|:-----------|:-----------------|:-----------------------|:---------------------|
| 10 | 1.556423e+02 | 44 | 0.446536 | True |
| 12 | 1.565154e+02 | 60 | 0.446536 | True |
| 14 | 1.570238e+02 | 80 | 0.446536 | True |

The cocycle-norm series is monotonically increasing in L (each new sector at higher `(p+q)` adds positive `|λ|^{-8}` contribution); Friedrich-Bär floor is L-INVARIANT under M_3(ℂ)-triality filter (minimum-η sectors `(1,2)` / `(2,1)`, `C_2 = 10/3`, `λ_min = 1.6695682`, `η_FB ≈ 0.4465`).

#### 2. Log-log regression for `α_HH^1_emp(s=4)` (sub-option (a))

Friedrich-Bär-anchored canonical proxy: `norm_canonical_FB = 1.570238e+02 + 2.054383e+01 = 1.775677e+02`. Per-L deltas + fit:

| L_max | δ(L) |
|:------|:-----|
| 10 | 2.192532e+01 |
| 12 | 2.105227e+01 |
| 14 | 2.054383e+01 |

- **α_HH^1_emp(s=4) = 0.194312**
- C_HH^1 = 3.424111e+01
- Residuals: `[+1.636e-03, -3.571e-03, +1.935e-03]` (max ≈ 3.6e-3; clean log-log fit)

#### 3. Wodzicki/Connes d=4 prediction cross-check (sub-option (d))

| Quantity | Value |
|:---------|:------|
| α_HH^1_emp(s=4) | 0.194312 |
| Wodzicki/Connes d=4 target `α(s=4) = 2(4−2)` | 4.0 |
| ABS(α_emp − target) | 3.805688 |
| Within publication-precision tolerance ±1.5? | **False** (2.54× over tolerance) |

**Substrate-physics interpretation**: empirical α at L_max=14 is two OOM below Wodzicki/Connes asymptotic. Structurally consistent with S91 §W9-10 substrate-distance-1 pole baseline (`α(s=3) = 0.110434` vs target 2.0; off by 18×). Cache-ceiling boundary effect at L_max=14 + Friedrich-Bär tail bound: convergence rate of L-truncated cocycle-norm series to FB-anchored canonical proxy is SUPER-POLYNOMIALLY damped under high Mellin exponent `-8`, so log-log slope is the slow-residual exponent visible at L ∈ {10, 12, 14}, not the asymptotic exponent at `L → ∞`. Pathway (i) `L_max ≥ 16` or Pathway (iii) FULL CC 1996 §2.2-2.3 physical multipliers are the substrate-physics refinement paths per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"`.

#### 4. Friedrich-Bär ratio table at L=14 (sub-option (b))

80 sectors `(p,q)` satisfying triality `(p−q) mod 3 ≠ 0`. Sample (first 6 by `p+q`):

| (p,q) | C_2(p,q) | η_FB(p,q) = `|λ|_min / √(C_2+1)` |
|:------|:---------|:------|
| (0, 1) | 4/3 | 0.547221 |
| (1, 0) | 4/3 | 0.547221 |
| (0, 2) | 10/3 | 0.467052 |
| (2, 0) | 10/3 | 0.467052 |
| (1, 2) | 10/3 | **0.446536** (floor) |
| (2, 1) | 10/3 | **0.446536** (floor) |

The η_FB floor `0.446536` exceeds canonical pin `η_FB_lower = 0.40` by 11.6%. **Friedrich-Bär saturation theorem certified** across all 80 sectors; NEW-sector intrusion at L_max=14 → ∞ analytically bounded by `tail_FB_bound = 2.054e+01` (super-polynomial decay `(C_2)^{-4}` at pole s=4 — faster than `(C_2)^{-3}` at pole s=3).

#### 5. Sub-option (c) Casimir-bound `truncation_consistent` flag scan

L_op ∈ {6, 8, 10, 12, 14} truncation scan; relative differences to L_op_max=14:

| L_op | norm_HH^1 | rel_diff_vs_L_op_max |
|:-----|:----------|:----------|
| 6 | 1.504593e+02 | 4.180626e-02 (4.18%) |
| 8 | 1.539861e+02 | 1.934568e-02 (1.93%) |
| 10 | 1.556423e+02 | 8.797999e-03 (0.88%) |
| 12 | 1.565154e+02 | 3.238002e-03 (0.32%) |
| 14 | 1.570238e+02 | 0 |

Rel-diff strictly decreasing as L_op approaches L_op_max; per-truncation norm strictly increasing. **truncation_consistent_flag = True**. Decay rate `4.18% → 0.32%` over L_op 6→12 (compound factor ≈ 0.45 per increment) — super-polynomial in L_op, consistent with Friedrich-Bär theorem at substrate-distance-2 pole.

#### 6. Decision band (plan §W7-5 `strict_PASS_boundary` 4-sub-option conjunction)

| Sub-option | Predicate | Result |
|:-----------|:----------|:-------|
| (a) | α_HH^1_emp(s=4) ∈ [1.5, 4.0] | **False** (0.194312 < 1.5) |
| (b) | η_FB_lower(L=14) ≥ 0.40 across M_3(ℂ)-sectors | True (0.446536 > 0.40) |
| (c) | truncation_consistent across L_op ∈ {6,8,10,12,14} | True |
| (d) | α_emp(s=4) > 0 AND ABS(α_emp − 4) ≤ 1.5 | **False** (positive YES; ABS=3.81 > 1.5 NO) |

Composite collapse per `gate-verdicts.md §"S87+ composite-collapse rule"`: `magnitude_verdict == INFO ⇒ composite = INFO`. **Verdict: INFO** per plan §W7-5 `INFO_meaning` (α ∈ (0, 1.5) AND direction matches but outside [1.5, 4.0]).

#### 7. 4-tuple + 4-axis pin compliance

| Field | Value |
|:------|:------|
| scheme | `full-cm-1995-iii-4-simple-pole-residue` |
| convention | `substrate-distance-2-pole-s4-FULL` |
| L_max | 14 |
| LEVEL_CLASS_PIN | FULL (substrate-natural CM-1995 §III.4 evaluator; NOT SCHEMATIC) |
| MACHINERY_SCOPE_PIN | CACHE-PROJECTION (L_max=14 master cache + Friedrich-Bär tail bound) |
| BINDING_AXIS_PIN | substrate-natural-binding (HH^1 cocycle norm IS substrate-IS) |
| A_N_REGULATOR_PIN | a_2^{Mellin} (per `regulator-pin-discipline.md` MANDATORY tagging) |

Audit/content SHAs (full 64-char):

- audit_sha256 = `38ee9db31658bb25941ccdc2e2db3551f7db4b0379d802d1043c8c45a9522cf6`
- content_sha256 = `0c73e292b383c74ce34e956bb9352fe973f598026febabfeba31565f3f884f56`
- SHA-uniqueness verified: audit_sha256 appears once in `s92_gate_verdicts.txt` (no sig_5 duplication).

#### 8. Substrate framing (per `phononic-framing.md §"IS Space, Not IN Space"`)

The substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold = 0.19))` at Pillar 1. The M_3(ℂ) ⊂ A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) Wedderburn summand IS substrate-IS at the algebra-axiomatic axiom layer; the Hochschild-cocycle norm asymptotic envelope `α_HH^1(s)` IS substrate-IS at the CM-1995 §III.4 simple-pole residue layer per Wodzicki 1984 + Connes 1995 §III dimensional analysis.

Direction substrate → emergent:

```
D_K eigenvalues at L_max=14 truncation
  → Peter-Weyl per-sector cardinality decomposition on M_3(ℂ) ⊂ A_K
    (triality (p−q) mod 3 ≠ 0; 80 sectors at L=14)
  → CM-1995 §III.4 simple-pole residue at s_0 = 4 (Mellin weight |λ|^{-8})
  → per-shell log-log regression empirical α exponent (0.194312)
  → comparison with Wodzicki/Connes d=4 prediction α_HH^1(s=4) = 4
  → INFO verdict at publication-precision floor; sign PASS, magnitude outside [1.5, 4.0]
```

Container-thinking FORBIDDEN: "the L_max=14 master cache CONTAINS the cocycle norm" → INVERT: "the cocycle norm IS substrate-IS at the Peter-Weyl eigenvalue-gap layer of D_K on M_3(ℂ) ⊂ A_K; the L_max=14 master cache IS the methodology-floor F-image at the cache-projection evaluation convention". The Wodzicki/Connes d=4 prediction `α_HH^1(s) = 2(s − 2)` is a STRUCTURAL THEOREM at every L_max (regulator-invariant; L-independent at the cohomology-class layer); the empirical first-extraction at L_max=14 is the methodology-floor F-image per `epistemic-discipline.md §"Layer-Decomposition"`.

#### 9. Downstream consumers + §VII.AZ.OP-PROJ Element 4 sub-class tag routing

- **§W7-6 per-pole α(s) exponent table at central pole s=4** (CHAINED on §W7-5 INFO): this gate's `α_HH^1_emp(s=4) = 0.194312` is the cross-anchor; per plan §W7-6 routing on INFO outcome, the per-pole table at s=4 will be tagged `PROVISIONAL-PENDING-FIRST-EXTRACTION` rather than canonical.
- **§W7-7 T2.12 cocycle-asymmetry inheritance audit** (paired with §W7-5): this gate's α-VALUE is α-INDEPENDENT per the `(Δ_B/Δ_A)^p Cancellation Theorem operational form`; cocycle-asymmetry ratio `‖[φ_67]‖ / ‖[φ_88]‖ = 7.324992` preserved INTACT under slower convergence at substrate-distance-2 pole.
- **§VII.AZ.OP-PROJ Element 4 sub-class tag**: REMAINS at `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` per plan §W7-5 INFO routing (does NOT replace with `STAGE-1-CANDIDATE-FIRST-EXTRACTED`); promotion deferred to S93+ pending Pathway (i) `L_max ≥ 16` or Pathway (iii) FULL CC 1996 multipliers.
- **canonical_constants.py promotion** of `alpha_HH1_FW_s4`: DEFERRED per plan §W7-6 routing on INFO.
"""


def replace_w7_5_block(path: Path, new_body: str, max_retries: int = 10) -> int:
    """Atomic in-place replacement of §W7-5 block.

    Reads the file, locates the §W7-5 block (from '### §W7-5.' through the
    next '### §W7-6.' header, exclusive of the §W7-6 header line), then
    writes back atomically. Retries up to max_retries times under mtime
    contention via fresh re-read.
    """
    import os
    import time

    BLOCK_HEADER = "### §W7-5. S92-W7-CF-W8-CONSOLIDATED-6-CF-W9-10-A-HH-1-FIRST-EXTRACTION-S4"  # (local)
    NEXT_HEADER = "### §W7-6."  # (local)

    for attempt in range(max_retries):
        text = path.read_text(encoding="utf-8")  # (local)
        start_idx = text.find(BLOCK_HEADER)  # (local)
        if start_idx < 0:
            print(f"ERROR: block header not found: {BLOCK_HEADER!r}")
            return 1
        next_idx = text.find(NEXT_HEADER, start_idx + len(BLOCK_HEADER))  # (local)
        if next_idx < 0:
            print(f"ERROR: next header not found: {NEXT_HEADER!r}")
            return 1
        # Preserve the trailing "---\n\n" separator that sits between blocks.
        # The original block ends with "---\n\n" before the next header. We
        # locate the immediate '---' line preceding NEXT_HEADER.
        sep_marker = "\n---\n"  # (local)
        sep_idx = text.rfind(sep_marker, start_idx, next_idx)  # (local)
        if sep_idx < 0:
            print(f"ERROR: '---' separator not found between §W7-5 and §W7-6")
            return 1
        # The replacement is [start_idx, sep_idx) -> new_body; preserve
        # the '\n---\n\n' through to next_idx.
        new_text = text[:start_idx] + new_body + text[sep_idx:]  # (local)
        # Write atomically via temp + rename
        tmp_path = path.with_suffix(path.suffix + ".tmp")  # (local)
        tmp_path.write_text(new_text, encoding="utf-8")
        try:
            os.replace(str(tmp_path), str(path))
        except OSError as e:
            print(f"  attempt {attempt + 1}: rename failed ({e}); retrying in 0.2s")
            time.sleep(0.2)
            continue
        # Verify post-write: re-read and confirm patch present
        post = path.read_text(encoding="utf-8")  # (local)
        if "alpha_HH^1_emp(s=4) = 0.194312" in post and "**Status**: COMPLETED" in post[start_idx:start_idx + 2000]:
            print(f"  attempt {attempt + 1}: PATCH applied + verified")
            return 0
        print(f"  attempt {attempt + 1}: post-write verification failed; retrying")
        time.sleep(0.2)
    print(f"ERROR: max_retries exhausted")
    return 1


if __name__ == "__main__":
    sys.exit(replace_w7_5_block(WP_PATH, NEW_BODY))
