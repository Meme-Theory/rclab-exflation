#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S96-CONSOL-3REGISTER-TABLE — W8 working-paper §W8-2 ATOMIC section-scoped write
==============================================================================
mack-cosmic-bridge. Replaces the §W8-2 stub in session-96-w8-workingpaper.md with
the completed section (atomic read -> splice ONLY the §W8-2 region -> fsync + os.replace).
Preserves all other WP sections (W8-1, W8-3..W8-7) byte-for-byte.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")

import sys
import json
import hashlib
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
WP = PROJECT_ROOT / "sessions" / "session-96" / "session-96-w8-workingpaper.md"
REG_MD = PROJECT_ROOT / "computations" / "session-96" / "s96_consol_3register_table.md"
PARTITION_JSON = PROJECT_ROOT / "computations" / "session-96" / "s96_consol_3register_table.json"

_SHARED = PROJECT_ROOT / "computations" / "_shared"
if str(_SHARED) not in sys.path:
    sys.path.insert(0, str(_SHARED))
from canonical_constants import sigma_8  # noqa: E402  used in the σ₈ anchor-fix narrative

# pull the partition counts from the JSON (single source of truth)
pm = json.loads(PARTITION_JSON.read_text(encoding="utf-8"))
N_ROBUST = pm["sum_check"]["n_robust"]            # (local)
N_COND = pm["sum_check"]["n_conditional"]         # (local)
N_FALS = pm["sum_check"]["n_falsified"]           # (local)
N_TOTAL = pm["sum_check"]["n_total"]              # (local)
VERDICT = pm["verdict"]                           # (local)
AUDIT = "014aea22370aa3f8465932c7dde5dc6bb18c6122b6700918b81eabfc9b0816fe"   # (local)
CONTENT = "9bd3b43e4a2ceda01d1fdc512c541fbdf8ae265340ec74e22fe6178c9653f688" # (local)

reg_md = REG_MD.read_text(encoding="utf-8").rstrip("\n")

SECTION = f"""### §W8-2. S96-CONSOL-3REGISTER-TABLE (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `S96-CONSOL-3REGISTER-TABLE`
**Trigger**: `[AUDIT]`
**Classification**: **NON-PHONONIC** (methodology / observable-table restructuring of a curated framework document) — **METHODOLOGY-class** (M1–M4); **DEPENDS ON W8-1** (forward-pinned-follow-up; the W8-1 status-diff feeds the partition)
**Agent**: `mack-cosmic-bridge` (the §7 falsifier/observable-table sole writer per `feedback_mack-bridge-role.md`; agent_type AND designated writer)
**Hypothesis**: The §7.1 "now" table — flagged by the external review as "visually flattening conditional and unconditional claims into a common rhetorical register" — partitions into THREE registers (robust-structural / conditional / currently-falsified) keyed by the W8-1-reconciled status tags, each observable row in exactly one register, NO row's epistemic type flattened, each row's substrate-moment-layer (a₀/a₂/a₄) preserved.
**Plan reference**: `sessions/session-plan/session-96-plan-w8.md` §W8-2.

**Verdict**: **{VERDICT}** — the §7.1 "now" table is split into three epistemic registers; the partition is exact (`{N_ROBUST}` robust + `{N_COND}` conditional + `{N_FALS}` falsified = `{N_TOTAL}` rows; **SUM-check exact**, no omission, no double-count); **no-flattening holds** (zero BROKEN/CONDITIONAL rows in the robust register); each row carries its substrate-moment-layer tag (a₀/a₂/a₄); and exactly one genuine **dual-status straddle** (`m_H`: robust-on-magnitude / conditional-on-route) is **disclosed and placed in CONDITIONAL**, NOT flattened into the robust register. The honest verdict is **INFO** (gate `INFO_meaning`): the 3-register split lands cleanly AND a legitimately-straddling row is disclosed rather than forced into one register. dual-SHA: `audit_sha256={AUDIT}`, `content_sha256={CONTENT}` (full-64; the prior `ba39384d…` line is superseded per `gate-verdicts.md` Option A — a same-session script-bug fix that escaped literal table pipes). 4-tuple: `(value=⟨3-register split: {N_ROBUST}/{N_COND}/{N_FALS}, SUM-check exact⟩, scheme=THREE-REGISTER-PARTITION-ROBUST-CONDITIONAL-FALSIFIED, convention=register-keyed-by-W8-1-status-tag+substrate-moment-layer+no-flattening, L_max=N/A)`.

**Results**:

The NUMBERS first: the 14 §7.1 observable rows (post-W7 landings) partition by their W8-1-reconciled status tag (the register is a *categorical function of the status tag*: PROVEN/PASS-structural/BOUND-Gaussian-by-Wick → robust; CONDITIONAL/SCHEME-DEPENDENT/route-dependent/VIABLE → conditional; BROKEN → falsified). No value is recomputed; the σ-distances and central values are transcribed from §7.1 (which W8-1 already reconciled against the register).

**The 3 registers (the §7 "now" observational-anchor surface):**

{reg_md}

**Partition (SUM-check, no-flattening):**

| Register | Count | Members |
|:--|:-:|:--|
| **A — ROBUST-STRUCTURAL** | {N_ROBUST} | CC closure, r, f_NL (Gaussian-by-Wick BOUND), σ/m=0, f·σ₈, ν mass ordering, c_s²=0 |
| **B — CONDITIONAL** | {N_COND} | w₀, n_s (scheme-dependent), α_s, m_H (dual-status straddle), Ω_DM h², σ₈ |
| **C — CURRENTLY-FALSIFIED** | {N_FALS} | w_a=0 (C5 BROKEN, 3.43σ — the live wager) |

SUM-check: **{N_ROBUST} + {N_COND} + {N_FALS} = {N_ROBUST+N_COND+N_FALS} == {N_TOTAL}** (exact). No-flattening: **zero** BROKEN/CONDITIONAL rows in Register A (verified by the producing script's `is_non_robust_status` predicate over the robust set). Dual-status straddle (disclosed): **m_H** — robust-on-magnitude (~2% theory budget PASS) but conditional-on-route (zeta 138.5 GeV excluded; μ_BC 188 GeV is an ACCOMMODATION) → placed in CONDITIONAL with an explicit annotation, the honest INFO per the gate rubric. The §7.3 honest-scorecard already makes the SAME distinction in prose ("a single layer — Ω_DM and σ₈ are both a₂-channel — must not be multiplied"; the zero-parameter structural spine carries no borrowed H); this gate makes it structural in the TABLE.

**Consolidated §7-surface items (the pending W6/W7 falsifier-inventory + §7 updates landed this gate; mack sole writer per the canonical write-order verdict → canonical_constants.py [complete] → falsifier-master-inventory.md [landed]):**

- **W6-1 (`S96-OBS-FSIGMA8-FORECAST`, INFO→PASS)** → falsifier-inventory **Row #71** (f·σ₈ RSD discriminator): −4.058% f·σ₈ PRODUCT suppression vs ΛCDM @ z=0.51 (bare-f −0.311%, **C5 conflation guard explicit**), S₈-tension-relieving sign; DESI-5yr → Euclid; forecast σ-dist 1.013 (DESI-Y5) / 1.534 (Euclid). Canonical pins `fsigma8_product_suppression_FW_max_pct`/`f_bare_suppression_FW_pct`/`f_FW`/`f_LCDM` (already in `canonical_constants.py`); verdict `audit_sha256=318df6ed…`. Also appears in §7.1 Register A.
- **W6-2 (`S96-OBS-FIRST-SOUND-RING`, PASS)** → falsifier-inventory **Row #72** (first-sound BAO ring): `A_FS = 0.204` = c₂²/c₁² ring imprint at k₁=0.0193 Mpc⁻¹ (r₁=325.3 Mpc), **NO ΛCDM counterpart**; SNR 8.6 (DESI-5yr, σ_exp=2.35% FETCHED arXiv:2411.19738v2) / 5.1 (DESI-DR1). Contrast disclosed: the per-branch effacement sub-feature A_obs_B1=1.445e-3 is OUTSIDE current rulers BY DESIGN (0.60× DESI-DR2 ruler) — "far below current rulers" is scoped to THIS sub-feature, NOT the ring (141× the sub-feature). Canonical pin `A_FS_first_sound_ring`; verdict `audit_sha256=b74ccd56…` (full-64 in the row).
- **W6-3 (`S96-OBS-CGWB-PEAK-FREQ`, FAIL — D4 resolved AGAINST mHz)** → falsifier-inventory **Row #7.audit-2** scope-correction + capstone §7.2 cross-ref note. The §7.2 / Row #7 LISA CGWB flagship is SCOPE-CORRECTED to split two observables: **(a) Ω_GW AMPLITUDE** at the LISA pivot UNCHANGED/LIVE (LISA samples the IR-tail amplitude `Ω_GW^(A)~1e-10`, 11+ OOM above LISA-PLS, W6-4 PASS); **(b) CGWB peak FREQUENCY** CORRECTED to `f_obs=8.4835e39 Hz` (GHz+, 43.9 decades above LISA — the asserted mHz-peak placement is REFUTED; reaching LISA needs κ=25 s/M_KK⁻¹, 42.5 OOM from natural ħ/M_KK). Tag: peak-frequency flagship is `NORMALIZATION-CONDITIONAL-AND-CURRENTLY-AGAINST-mHz`. Read row #7 as the **amplitude** discriminator, NOT a peak-in-band claim. Canonical `f_obs_CGWB_peak_kappa_nat=8.4835e39`; verdict `audit_sha256=646e6ad0…`.
- **W7-5 MACK-INVENTORY-RECOMMENDATION** → falsifier-inventory **Row #73** (neutrino normal mass ordering B1<B2<B3, zero-free-parameter, machine-ε, dynamical τ=0.107 (1,1,0)-crossing; JUNO 2026+ / DUNE 2030s; NuFit-6.0 NO ~2.5σ consistent). The entire neutrino sector was ABSENT from the inventory before this landing. W7-5's f·σ₈ "Row A" is the SAME observable as Row #71 (single landing, no duplicate). Verdict anchor `audit_sha256=92a36810…` (W7-5 `S96-HYG-SELF-INVENTORY`).
- **W6-4 FIDELITY NOTE** → **ratified** (already landed in Row #7.audit line 159; bound to publication-precision hygiene, Class-8.3). The Ω_GW^(C) round-figure `1e-57` vs Sage-exact `8.299e-58` is `1.205× = 0.081 OOM` (**same-decade**), NOT the "~10×/~2 OOM" the rule/plan prose claimed. The DISCIPLINE (use the Sage-exact `8.299e-58`, never `1e-57`) is correct and binding — but the *binding reason* is publication-precision hygiene (Class-8.3), NOT an OOM blunder. The W6-4 verdict line itself records `round_fig_1e-57_understate=1.205x_0.081OOM`. **This is itself a do-not-overstate correction of the rule prose** (`regulator-pin-discipline.md §"Sage-Exact Rationals"` says "~10×/~1 OOM"; the exact figure is 0.081 OOM) — flagged for the rule-prose fix at W8-6/W8-7.
- **§VII.BH (c_s²=0)** → **mack-review-at-W8-2 verdict: NO §7-falsifier-surface retrofit needed.** §VII.BH is a §VII permanent-results **CROSS-PILLAR BRIDGE** entry (substrate-IS Kasparov-factorized triple → Kasparov-product bridge map → laboratory-IN dark-sector c_s² bound), NOT a §7 falsifier-SURFACE row. The c_s² row stays in §7.1 Register A as a robust-spine **scorecard pointer** (the §7.3 joint-BF spine member: `m_H`, mass ordering, σ/m=0, c_s²=0 — the no-borrowed-H spine), with the full 5-anatomy + 3-level ladder at §VII.BH (W7-8, `_cross_pillar_bridge_audit.py` 3/3 tiers, 5/5 anatomy). No falsifier-master-inventory row is created (a registry bridge is not a falsifier).
- **W6-7 (σ₈/S₈ labeling)** → **§7.1 anchor-citation FIX applied**: the capstone σ₈ row comparison anchor now cites **Planck σ₈ = `{sigma_8}`** (the canonical Planck σ₈; `canonical_constants.py:sigma_8={sigma_8}`), NOT `0.829` — which is the **S₈** value the prose mis-labeled as σ₈. The flat-table cell now reads `Planck σ₈ {sigma_8} (S₈ 0.829)`. The prose/citation fix also routes to W8-6. Row #70 (the σ₈/S₈ inventory row) was already landed by W6-7.

**Substrate framing.** NON-PHONONIC (methodology / observable-table restructuring of a curated framework document). No substrate-physics compute; this gate restructures the §7 observable surface so its epistemic stratification is visible. The substrate-IS framing is preserved per row: each observable remains "a spectral moment of `D_K` at the single modulus `τ_now`" — the §7.1 header is unchanged ("No observable below is fit"; "When the substrate measures one of these, the substrate is probing itself"). The 3-register split changes **no value** and **no substrate-moment-layer attribution** (a₀/a₂/a₄); it only sorts the rows by epistemic register so the robust zero-parameter spine (CC closure, σ/m=0, T(k)=1, c_s²=0, ν-ordering, f_NL-bound, f·σ₈) is not visually conflated with the conditional forecasts (Ω_DM h², n_s scheme-dependence, σ₈, m_H, w₀, α_s) or the live wager (w_a=0 BROKEN). Direction held throughout: `D_K eigenvalues → spectral-moment channel (a₀/a₂/a₄) → emergent observable → detector` — never an observable fit IN a ΛCDM container.

**Output Artifacts** (closure-verification checklist):
- **script** `computations/_shared/s96_consol_3register_table.py` — EXISTS; `grep`: `from canonical_constants import` ✓ (12 pins: w0_FW, sigma_8, f_FW, f_LCDM, fsigma8_product_suppression_FW_max_pct, f_bare_suppression_FW_pct, A_FS_first_sound_ring, f_obs_CGWB_peak_kappa_nat, Omega_GW_Lambda_A_LISA, Omega_GW_Companion_null, OOM_split_AC_regulator_class); `append_verdict` ✓ (def + invocation).
- **data** `computations/session-96/s96_consol_3register_table.json` — EXISTS (the partition map: row → register + substrate-moment-layer tag + register-source status + SUM-check counts + consolidated §7-surface items + anchor fixes).
- **plot** `computations/session-96/s96_consol_3register_table.png` — EXISTS (register-population bar: robust/conditional/falsified counts + no-flattening + dual-status annotation).
- **3-register tables markdown** `computations/session-96/s96_consol_3register_table.md` — EXISTS (the 3 register-tables, spliced into the capstone §7.1).
- **npz** `computations/session-96/s96_consol_3register_table.npz` — EXISTS (partition arrays for downstream).
- **capstone_patch** `sessions/framework/phonic-exflation-equation.md` §7.1 — APPLIED (atomic section-scoped: read → splice §7.1 → fsync+os.replace via `s96_consol_3register_capstone_patch.py`): 3-register split inserted as the PRIMARY view, flat table retained as flat-reference, σ₈ anchor fixed (Planck σ₈ {sigma_8}), §7.2 CGWB scope-correction cross-ref added. **W7-landed sections preserved byte-for-byte** (diff-guard verified: §3.3, §5.3, §7.2, §7.3, §8.2a, §9 markers all intact; the patch ASSERTS all 5 W7 guard markers survive).
- **falsifier-master-inventory** `sessions/framework/registry/falsifier-master-inventory.md` — Rows **#71** (f·σ₈), **#72** (first-sound ring), **#73** (normal ordering) + **Row #7.audit-2** (CGWB peak-freq scope-correction) + W8-2 consolidation summary APPENDED (atomic O_APPEND single `open('a')` via `s96_consol_inventory_append.py`; all 4 verdict-anchor SHAs full-64). mack-cosmic-bridge sole writer.
- **verdict line** `computations/session-96/s96_gate_verdicts.txt` — `S96-CONSOL-3REGISTER-TABLE: {VERDICT}` + dual-SHA companion row; `audit_sha256={AUDIT}` (unique in file, sig_5 clean; carries `supersedes=ba39384d…` per Option A — the prior pipe-unescaped line is superseded, not edited-in-place); no [SIGN] 3-tuple (`schema_v2_3tuple_required: false`).

**MCP Pre-Compute Audit** (queries executed BEFORE the consolidation, per query-first discipline; the per-row status tags ARE the W8-1 status-diff output — NOT re-derived here; `get_constant` validates the W8-1 transcription + the canonical pins):
- `search_knowledge('S96 3-register table consolidation falsifier inventory')` → S87 W5 falsifier-inventory-consolidation precedent (`s87-falsifier-master-inventory-consolidation.md`); no prior W8-2 landing. **Confirms the consolidation is new; the inventory append-pattern follows the S87 precedent.**
- Read `computations/session-96/s96_consol_status_sync.json` (W8-1 status-diff, the upstream prereq) → `cell_register_map` (11 §7.1 rows with reconciled status tags); verdict INFO; `forbidden_violations=0`; D2+D5 forward-routed. **The register assignment is keyed to these tags (categorical function), not re-derived.**
- `get_constant('fsigma8_product_suppression_FW_max_pct')` → −4.058 (S96-OBS-FSIGMA8-FORECAST). `get_constant('A_FS_first_sound_ring')` → 0.204 (S96-OBS-FIRST-SOUND-RING). `get_constant('f_obs_CGWB_peak_kappa_nat')` → 8.4835e39 (S96-OBS-CGWB-PEAK-FREQ; "D4 resolved AGAINST mHz"). `get_constant('sigma_8')` → 0.811 (S96-OBS-ANCHOR-HYGIENE; "Planck-2018 σ₈ = 0.811 ± 0.006" — confirms W6-7: capstone "0.829" is S₈, NOT σ₈). `get_constant('f_FW')` → 0.5254916… **All consolidated values transcribe from canonical_constants.py (write-order Step 2 complete); no value recomputed.**
- `get_constant('Omega_GW_Companion_null')` → 8.299e-58 (Sage-exact); `get_constant('OOM_split_AC_regulator_class')` → 47.081. **Confirms the W6-4 fidelity figure: 1e-57/8.299e-58 = 1.205× = 0.081 OOM (same-decade), NOT ~10×/~2 OOM.**

---
"""

# ----- atomic section-scoped splice -----
original = WP.read_text(encoding="utf-8")
lines = original.splitlines(keepends=True)

start = None   # '### §W8-2.' header
end = None      # next '### §W8-3.' header
for i, ln in enumerate(lines):
    if ln.startswith("### §W8-2. S96-CONSOL-3REGISTER-TABLE"):
        start = i
    elif start is not None and ln.startswith("### §W8-3."):
        end = i
        break
assert start is not None, "§W8-2 header not found in WP"
assert end is not None and end > start, "§W8-3 header (end boundary) not found after §W8-2"

# guard: the other WP sections must survive
GUARDS = ["### §W8-1. S96-CONSOL-STATUS-SYNC", "### §W8-3. S96-CONSOL-HYGIENE-GATE",
          "### §W8-4. S96-CONSOL-DK-DF-EQUIV", "### §W8-7. S96-CONSOL-MODULARIZE"]

new_text = "".join(lines[:start]) + SECTION + "\n" + "".join(lines[end:])
for g in GUARDS:
    assert g in new_text, f"WP guard section LOST: {g!r}"

tmp = WP.with_suffix(".md.tmp_w82wp")
with tmp.open("w", encoding="utf-8", newline="") as fp:
    fp.write(new_text)
    fp.flush()
    os.fsync(fp.fileno())
os.replace(tmp, WP)

new_sha = hashlib.sha256(new_text.encode("utf-8")).hexdigest()
print(f"[wp] §W8-2 section written; WP sha256={new_sha[:16]}... ({len(new_text)} chars; "
      f"+{len(new_text) - len(original)} chars)")
print("[wp] all guard sections (W8-1/W8-3/W8-4/W8-7) intact.")
sys.exit(0)
