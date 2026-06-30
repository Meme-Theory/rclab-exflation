# -*- coding: utf-8 -*-
"""
Atomic section-scoped writer for the WP §W7-5 section.
Replaces ONLY the `### §W7-5. S96-HYG-SELF-INVENTORY (gen-physicist)` block
(from its header up to the trailing `---` that precedes §W7-6), preserving
every other section byte-for-byte. fsync + os.replace under concurrent contention.
"""
import os
import sys
from pathlib import Path

ROOT = Path(r"C:\sandbox\Ainulindale Exflation")
WP = ROOT / "sessions" / "session-96" / "session-96-w7-workingpaper.md"

START_ANCHOR = "### §W7-5. S96-HYG-SELF-INVENTORY (gen-physicist)"
NEXT_ANCHOR = "### §W7-6. S96-HYG-KIND-TAG-S53 (hawking-theorist)"

NEW_SECTION = r"""### §W7-5. S96-HYG-SELF-INVENTORY (gen-physicist)

**Status**: COMPLETED
**Gate ID**: `S96-HYG-SELF-INVENTORY`
**Trigger**: `[AUDIT]`
**Classification**: **PHONONIC** (the four omitted results are substrate predictions — growth-rate, neutrino ordering, sound-speed, holonomy)
**Agent**: `gen-physicist` (cross-domain: pulls from 4 distinct reviewer axes — LSS, neutrino, NCG-bridge, Berry-phase)
**Class note**: **METHODOLOGY-class** (M2 = capstone §7/§9 Edit, no threshold `.py`; M3 = verbatim from PROVEN priors — cosmic-web V.3 `f·σ₈`, neutrino §V, van-den-dungen V.4 `c_s²=0`, berry verdict-2 `Ω=0`; M4 → **allowlist-append FLAG `S96-HYG-SELF-INVENTORY`** routed to orchestrator). The `c_s²=0` row here is the §7 SCORECARD pointer; the deeper §VII REGISTRY entry with full Kasparov anatomy is the separate W7-8 gate. Falsifier-inventory rows route to `mack-cosmic-bridge` (sole writer).
**Plan reference**: `sessions/session-plan/session-96-plan-w7.md` §W7-5.

**Verdict**: **PASS** — all four omitted PROVEN results landed in the capstone §7.1/§7.2/§9 with value + provenance + Layer/classification tag. The §7/§9 self-inventory completeness gap (C7) closes for these four. Verdict line + dual-SHA companion + schema-v2 3-tuple companion appended to `computations/session-96/s96_gate_verdicts.txt`.

**4-tuple**: `value=` 4-row set (f·σ₈ −4.058%, ν normal-ordering, c_s²=0, Ω=0) `scheme=scorecard-self-inventory-completion convention=row-with-provenance-and-Layer-tag L_max=N/A`.

**Results** — NUMBERS first.

**The four landed rows (verbatim from PROVEN priors; transcribed, not re-derived):**

1. **f·σ₈(z) — RSD growth (§7.1 row + §7.2 #5 falsifier).** `a₂` growth channel / E33. Framework value: **−4.058%** f·σ₈ **PRODUCT** suppression vs ΛCDM at z=0.51 (zero-free-parameter). Underlying pins (`canonical_constants.py`): `f_FW = 0.5254916357116971`, `f_LCDM = 0.5271303865722888` (bare-f suppression **−0.311%**), `σ₈(FW) ≈ 0.793166`. **C5 conflation guard (explicit):** the "~4% suppression" is the f·σ₈ PRODUCT figure (`fsigma8_product_suppression_FW_max_pct = −4.058`), distinct from the bare growth-rate suppression `f_bare_suppression_FW_pct = −0.311%`; the two MUST NOT be conflated. **Correct S₈ sign:** the suppression is negative ⇒ FW f·σ₈ sits BELOW ΛCDM ⇒ relieves the S₈ tension (lensing prefers ~0.76 < Planck 0.811). Forecast σ-distance 1.013 (DESI-Y5) / 1.534 (Euclid). Provenance: S77 PROVEN (cosmic-web V.3) / canonical-pin gate `S96-OBS-FSIGMA8-FORECAST`; underlying compute S42 (s8_tension/FABRIC-42) → S59 (s59_growth_factor: growth_ratio=0.978009) → S65 → S70 (s70_bulk_flow).

2. **Normal mass ordering — neutrino sector (§7.1 row + §7.2 #6 falsifier).** `a₄`/fiber neutrino. Framework value: **Normal B1 < B2 < B3** (zero-free-parameter), dynamical via the **τ=0.107 B1↓-below-B2 crossing** of D_K's (1,1,0)-singlet sector. Provenance: PROVEN, ZERO-FREE-PARAMETER, machine-ε (S8 / S34–36 / S52 / S56); `falsifier-rigor-registry.md` row; the τ-ordering evolution is on record in `s52_sector_ordering.txt` (τ=0.10: B2<B1<B3; τ=0.15: B1<B2<B3 — the B1↓-below-B2 crossing interpolates to τ=0.107). NuFit-6.0 prefers NO at ~2.5σ ⇒ consistent. (The entire neutrino sector was ABSENT from the scorecard before this landing.)

3. **c_s² = 0 — dark-sector sound speed (§7.1 row, SCORECARD pointer).** `a₂` Goldstone / Kasparov-factorized. Framework value: **0 exactly** (Layer-1 topological; `m_Goldstone^{4D} = 0` exactly by **Kasparov product factorization**), bound `< 9.21×10⁻⁴`, scheme-independent. Provenance: PROVEN (van-den-dungen synthesis V.4; S61 all-5-conditions Kasparov product factorization; S71–72 bound). **Scope note:** this is the §7 SCORECARD entry only — a pointer row. The full §VII REGISTRY entry with complete Kasparov anatomy is the **separate W7-8 gate** (`S96-HYG-CS2-REGISTRY`, van-den-dungen-theorist). No double-landing.

4. **Ω = 0 — trivial Berry holonomy (§9 geometry/topology spine).** Framework value: closed-loop holonomy `γ = 0`, Fubini–Study distance `d_FS = 0` on the Jensen line (S61; the SU(3) connection is flat). **SCOPE (per plan, load-bearing):** landed as "**the computed holonomy invariants are trivial** — read as *the invariants we computed came out trivial*, NOT as a claim that the substrate topology is nontrivial." This is the cleanest illustration of the §9 geometry-vs-topology spine: the triviality is a representation-theoretic fact surviving continuum dissolution unchanged. Provenance: S61 berry-relook ("On SU(3), the holonomy is trivial (flat connection)"); cross-ref B-30a Pfaffian-trivial-on-Jensen.

**Substitution chain (comparative discriminating-power claim — gate-block verbatim):**

> Claim: "f·σ₈(z) is a MORE discriminating LSS observable than the static σ₈ already in the scorecard, so its omission under-sells the framework's reach."
>
> - **Definition 1**: σ₈ := the z=0 matter-power-spectrum normalization amplitude [§7.1 lists σ₈ = 0.799, VIABLE ~2σ between Planck 0.811 and lensing ~0.76].
> - **Definition 2**: f·σ₈(z) := growth-rate × amplitude, the RSD observable [S77 PROVEN: −4.058% product suppression vs ΛCDM at z=0.51, correct S₈ sign; `f_FW = 0.525492` vs `f_LCDM = 0.527130`].
> - **Substitute (discriminating power)**: a static σ₈ near 0.799 is reproducible by MANY models (modified gravity, massive ν, evolving DE) ⇒ degeneracy HIGH ⇒ discriminating power LOW. f·σ₈(z) is a z-dependent SHAPE with a zero-parameter −4.058% suppression ⇒ degeneracy LOW ⇒ discriminating power HIGH.
> - **Simplify**: discriminating_power(f·σ₈) > discriminating_power(σ₈), because the shape+sign of a zero-parameter growth suppression breaks degeneracies the static amplitude cannot.
> - **Canonical form**: the MORE discriminating observable (f·σ₈) was ABSENT while the LESS discriminating one (σ₈) was PRESENT.
> - **Direction**: omitting f·σ₈ UNDER-states the framework's LSS reach (the stronger discriminator is missing) ⇒ adding it STRENGTHENS the §7 inventory.
> - **Conclusion**: add f·σ₈(z) (and the three other omitted PROVEN results) to §7/§9. [now justified]

The schema-v2 3-tuple reads off this chain: `sign_verdict = PASS` (computed direction — MORE-discriminating absent, LESS present — matches the predicted under-statement), `magnitude_verdict = PASS` (artifact-existence set-membership, all 4 rows landed), `regime_verdict = VALID` (documentation Edit, no expansion / numerical window).

**MACK-INVENTORY-RECOMMENDATION block** *(NOT written to `falsifier-master-inventory.md` — `mack-cosmic-bridge` is sole writer per `feedback_mack-bridge-role.md`; these two rows are recommended for mack to land, with the canonical write-order verdict→canonical→inventory):*

```
# === FOR mack-cosmic-bridge: two new falsifier-master-inventory.md rows ===
# Row A — f·sigma8(z) RSD growth discriminator
#   Observable    : f*sigma8(z) growth-rate * amplitude (RSD)
#   Substrate-IS  : a2 growth-channel signature (GGE-relic acoustic self-organization, the cosmic web)
#   FW value      : -4.058% f*sigma8 PRODUCT suppression vs LCDM @ z=0.51 (zero-parameter); bare-f -0.311% (C5 guard)
#   S8 sign       : negative => relieves S8 tension (lensing ~0.76 < Planck 0.811)
#   Detector      : DESI-5yr (Y5) 2029 -> Euclid 2030s
#   Forecast sigma: 1.013 (DESI-Y5) / 1.534 (Euclid)   [in-session scorecard; full forecast-fetch = W6 compute CF]
#   Canonical pin : fsigma8_product_suppression_FW_max_pct = -4.058 ; f_FW=0.5254916 ; f_LCDM=0.5271304
#   Verdict anchor: S96-OBS-FSIGMA8-FORECAST (PASS) ; this gate S96-HYG-SELF-INVENTORY audit_sha256 (see verdict file)
#   Note          : the forecast sigma-distance ROW is a W6 forecast-fetch carry-forward (INFO clause of this gate)
#
# Row B — Neutrino normal mass ordering
#   Observable    : neutrino mass ordering (Normal vs Inverted)
#   Substrate-IS  : D_K (1,1,0)-singlet eigenvalue ordering B1<B2<B3, dynamical via tau=0.107 crossing
#   FW value      : Normal ordering, ZERO-FREE-PARAMETER, machine-eps (S8/S34-36/S52/S56)
#   Detector      : JUNO 2026+ / DUNE 2030s (a NO-vs-IO verdict is a clean yes/no)
#   Status        : NuFit-6.0 NO preferred ~2.5sigma => consistent
#   Verdict anchor: this gate S96-HYG-SELF-INVENTORY audit_sha256 (see verdict file)
# === END mack recommendation ===
```

Routing: per `.claude/rules/math-scripts.md §"Canonical Write-Order"`, the f·σ₈ canonical pins already exist in `canonical_constants.py` (Step 2 complete: `f_FW`, `f_LCDM`, `fsigma8_product_suppression_FW_max_pct`, `f_bare_suppression_FW_pct`, gate `S96-OBS-FSIGMA8-FORECAST`); the inventory-row landing (Step 3) is mack's. The forecast σ-distance rows (DESI/Euclid + JUNO/DUNE) are the **INFO clause** of this gate — the scorecard entry is in-session, the forecast σ-distance is a W6 forecast-fetch compute CF.

**Output Artifacts** (closure-verification checklist):
- **Capstone edit** `sessions/framework/phonic-exflation-equation.md` §7.1/§7.2/§9 — LANDED (+1945 bytes, 106706→108651 at edit time; +25 net content lines). Four rows verified present, each exactly once: §7.1 f·σ₈ + ν-ordering + c_s²=0; §7.2 #5 + #6; §9 Ω=0 spine clause. **Concurrent-write safe:** atomic read→splice→fsync+os.replace preserved the concurrent W7-3 (Mellin firewall) and W7-7a (joint-evidence §7.3) edits byte-for-byte; all three sources coexist.
- **Edit script** `computations/session-96/s96_hyg_self_inventory_edit.py` (atomic section-scoped splicer; imports canonical pins; drift-tripwire asserts).
- **WP-writer script** `computations/session-96/s96_hyg_self_inventory_wp.py` (this section, atomic section-scoped).
- **Verdict line** `computations/session-96/s96_gate_verdicts.txt` — canonical `S96-HYG-SELF-INVENTORY: PASS` + dual-SHA companion (`audit_sha256=92a368105c829e8394ec7a1be899e42813f496cbbf0926a1f86b8cb06f6d38f1`, `content_sha256=3490eee47454d3fad3d7772e1f5ddd91ef59138a8fc96711fa2b45ab1dcdb032`) + schema-v2 3-tuple companion. audit_sha256 unique across the file (count=1).
- No `.py` threshold, no `.npz`/`.png` (METHODOLOGY-class).

**MCP Pre-Compute Audit** (queries run BEFORE the §7/§9 edit; per query-first discipline):
- `search_knowledge('f sigma8 growth rate suppression S8 tension RSD')` → `f_LCDM = 0.527130` (s70_bulk_flow), `sigma8_fw = 0.793166` / growth_ratio=0.978009 (s59/s65), s8_tension/FABRIC-42 provenance. **Confirms f·σ₈ provenance.**
- `get_constant('f_LCDM')` → `0.5271303865722888`, gate `S96-OBS-FSIGMA8-FORECAST`. `get_constant('sigma8_fw')` → not found (lives as `sigma8_fw=0.793166` in s59/s65 logs + capstone σ₈=0.799 row). Grep `canonical_constants.py`: `f_FW=0.5254916`, `fsigma8_product_suppression_FW_max_pct=-4.058`, `f_bare_suppression_FW_pct=-0.311` (C5 guard) — **the −4.058% PRODUCT vs −0.311% bare-f distinction surfaced here, preventing a C5 conflation in the landed row.**
- `search_knowledge('normal mass ordering neutrino B1 B2 B3 tau crossing zero-parameter')` → `falsifier-rigor-registry.md` "Neutrino mass ordering | ZERO-FREE-PARAMETER | Normal (B1<B2<B3; machine ε S8/S34-36/S52/S56)"; `s52_sector_ordering.txt` τ-evolution. **Confirms normal-ordering PROVEN + τ-crossing.**
- `search_knowledge('c_s squared zero Goldstone sound speed Kasparov product factorization')` → `m_Goldstone^{4D}=0 (exactly, by Kasparov product factorization)` (session-74-qa-vdd-workshop); van-den-dungen-synthesis "c_s²=0 (<9.21e-4, topological, scheme-independent) PROVEN". **Confirms c_s²=0; cross-refs W7-8.**
- `search_knowledge('trivial Berry holonomy Omega zero Jensen line Fubini-Study')` → session-61-berry-relook "On SU(3), the holonomy is trivial (flat connection)"; B-30a Pfaffian-trivial-on-Jensen. **Confirms Ω=0; scope = computed-invariants-trivial.**
- `trace_entity('f sigma8 growth suppression')` → no direct trace (the result lives under S96-OBS-FSIGMA8-FORECAST + the s59/s65/s70 compute chain, confirmed by the search hits above).
- **PRE-CLOSED status**: all four results are PROVEN priors (no new derivation); this gate is a verbatim self-inventory landing, not a recompute.

**Substrate framing.** PHONONIC — all four are substrate predictions, each flowing `D_K → spectral moment / topological invariant → observable`. **f·σ₈(z)** is the `a₂`-growth-channel signature of how the GGE relic's acoustic interference self-organizes gravitationally (the cosmic web); the substrate IS the growth history, not a fluid evolving IN expanding space. **Normal mass ordering** is the substrate eigenvalue ordering of the (1,1,0)-singlet neutrino sector of D_K, dynamical via the τ=0.107 crossing — the ordering IS a property of the Dirac spectrum, not an external mass matrix. **c_s²=0** is the Kasparov-factorized topological statement that the 4D Goldstone sound speed vanishes exactly (`m_Goldstone^{4D}=0` by product factorization) — a topological invariant, not a tuned EOS. **Ω=0** is the trivial Berry holonomy on the Jensen line, a substrate-IS topological invariant that survives continuum dissolution — the cleanest illustration of the §9 geometry/topology spine (the geometry dissolves; the trivial-holonomy invariant does not). The gate's contribution: documenting that the scorecard SHOULD carry these four substrate predictions; the direction of explanation is FROM D_K TOWARD the observable, never the reverse.

---

"""


def main():
    text = WP.read_text(encoding="utf-8")
    if START_ANCHOR not in text:
        sys.stderr.write("WP-ANCHOR-FAIL: §W7-5 header not found\n")
        sys.exit(2)
    if NEXT_ANCHOR not in text:
        sys.stderr.write("WP-ANCHOR-FAIL: §W7-6 header (section boundary) not found\n")
        sys.exit(2)
    start = text.index(START_ANCHOR)
    end = text.index(NEXT_ANCHOR)
    if end <= start:
        sys.stderr.write("WP-ANCHOR-FAIL: section boundaries inverted\n")
        sys.exit(2)
    new_text = text[:start] + NEW_SECTION + text[end:]

    tmp = WP.with_suffix(".md.s96w75wp.tmp")
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(new_text)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, WP)
    print(f"WP §W7-5 written: {len(text)} -> {len(new_text)} chars (delta={len(new_text)-len(text)})")
    sys.exit(0)


if __name__ == "__main__":
    main()
