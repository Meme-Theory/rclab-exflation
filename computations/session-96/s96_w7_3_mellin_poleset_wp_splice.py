"""
S96-HYG-MELLIN-POLESET — atomic section-scoped WP §W7-3 splice.

Replaces ONLY the §W7-3 stub body (Status..Results, all `*(pending...)*` blocks)
in sessions/archive/session-96/session-96-w7-workingpaper.md with the filled, on-disk-true
section. The §W7-3 header line (line 100) and every other section are preserved
byte-for-byte (atomic tmp + fsync + os.replace).

Run with:
  "phonon-exflation-sim/.venv312/Scripts/python.exe" \
    "computations/session-96/s96_w7_3_mellin_poleset_wp_splice.py"
"""
import os
import sys

PROJECT_ROOT = r"C:\sandbox\Ainulindale Exflation"
WP = os.path.join(PROJECT_ROOT, "sessions", "session-96", "session-96-w7-workingpaper.md")

# --- the OLD stub body to replace (verbatim, lines 102-121: Status..Results) ---
OLD_STUB = '''**Status**: NOT STARTED
**Gate ID**: `S96-HYG-MELLIN-POLESET`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (the dimension spectrum / Mellin pole structure of ζ_{D_K}(s) — the fabric's spectral content)
**Agent**: `lizzi-spectral-functional-theorist` (spectral-functional axis owns the Mellin-variable convention; lizzi V.1 is the source)
**Class note**: **METHODOLOGY-class** (M2 = Edit on capstone §3.3 + Sage MCP `n↔s` cross-check, NO threshold-producing `.py`; M3 = verbatim from lizzi V.1 `MELLIN-CONVENTION-RECONCILE` + CM-1995 dimension-spectrum definition; M4 → **allowlist-append FLAG `S96-HYG-MELLIN-POLESET`**). Dual-SHA: `content_sha256` over the §3.3 diff; `audit_sha256` over the input-pin map. Carries `regulator_pin=a_n^{Mellin}`.
**Hypothesis**: The §3.3 Mellin convention is internally inconsistent — ζ_{D_K}(s)=Σ m_k λ_k^{−2s} (printed λ^{−2s} power) has its residue poles in s at S_s={0,1,2,3,4}, NOT at {0,2,4,6,8} (the latter is the curvature-degree grading n=d−2s); citing `{0,2,4,6,8}` as the s-pole set creates a factor-2 mislabel risk for every downstream `s=N` citation (α_s at s=3; §VII.BE Pati-Salam at s=6; the s=4 substrate-distance-2 slot).
**Plan reference**: `sessions/session-plan/session-96-plan-w7.md` §W7-3 (n=d−2s map; corpus `s=N` citation audit).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
*(pending — METHODOLOGY-class: no producing `.py`. Confirm: (edit) `sessions/framework/phonic-exflation-equation.md §3.3` carries ONE Mellin convention with S_s in s + the explicit n=d−2s grading + a one-row reconciliation table; (edit) `.claude/rules/regulator-pin-discipline.md` Mellin pole-set labeling pin (orchestrator-only, directive-only); every corpus `s=N` citation (α_s s=3, §VII.BE s=6, s=4 slot) carries a convention tag; verdict line in `computations/session-96/s96_gate_verdicts.txt` matching `^S96-HYG-MELLIN-POLESET:.* (audit_sha256|content_sha256)=[a-f0-9]{64}` + dual-SHA companion row + schema-v2 3-tuple companion row (factor-2 directional sub-claim). Content presence only — no length/size targets.)*

**MCP Pre-Compute Audit**:
*(pending — list the `mcp__knowledge__*` queries executed before the convention audit, with one-line salient return each; mark PRE-CLOSED if a closure covers the gate. Per `.claude/rules/knowledge-index-usage.md`. Expected anchors: `search_knowledge('dimension spectrum Connes-Moscovici zeta D_K pole set s')`, `trace_entity('alpha_s')` (the s=3 / n=2 a₂-residue anchor), `search_knowledge('S31Aa dimension spectrum tau-independent')` (pole structure regulator-axis-independent), `get_constant('M_KK')` / `search_knowledge('VII.BE Pati-Salam s=6')` (the §VII.BE s=6 citation to re-confirm).)*

**Verdict**:
*(pending agent execution)*

**Results**:
*(pending — include: the canonical §3.3 reconciliation table (S_s={0,1,2,3,4} in s matching λ^{−2s}; n=d−2s∈{0,2,4,6,8} stated separately); Sage MCP `sage_eval` n↔s verification (d=8 ⇒ s=(d−n)/2); the convention-tag audit verdict for each of the 3 corpus citations (α_s s=3 ≡ §VII.BE s=6 same n=2 a₂-residue, OR discrepancy documented); 4-tuple (value=convention-consistency-PASS, scheme=Connes-Moscovici-1995-dimension-spectrum, convention=half-integer-friendly-zeta-lambda-power-minus-2s, L_max=N/A); the factor-2 substitution chain with substituted numbers (n=d−2s=8−2s; reading n as s mis-locates each pole by Δ=8−3s); the `a_n^{Mellin}` regulator-pin tag; dual-SHA (full 64-char, content over the §3.3 diff); SIGN/MAGNITUDE/REGIME 3-tuple; artifacts (capstone §3.3 + regulator-pin-discipline.md edits))*'''

NEW_BODY = r'''**Status**: COMPLETED
**Gate ID**: `S96-HYG-MELLIN-POLESET`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (the dimension spectrum / Mellin pole structure of ζ_{D_K}(s) — the fabric's spectral content)
**Agent**: `lizzi-spectral-functional-theorist` (spectral-functional axis owns the Mellin-variable convention; lizzi V.1 is the source)
**Class note**: **METHODOLOGY-class** (M2 = atomic section-scoped Edit on capstone §3.3 + Sage MCP `n↔s` cross-check, NO threshold-producing `.py`; M3 = verbatim from lizzi V.1 `MELLIN-CONVENTION-RECONCILE` + CM-1995 dimension-spectrum definition; M4 → **allowlist-append FLAG `S96-HYG-MELLIN-POLESET`**). Dual-SHA: `content_sha256` over the §3.3 diff; `audit_sha256` over the input-pin map. Carries `regulator_pin=a_n^{Mellin}`.
**Hypothesis**: The §3.3 Mellin convention is internally inconsistent — ζ_{D_K}(s)=Σ m_k λ_k^{−2s} (printed λ^{−2s} power) has its residue poles in s at S_s={0,1,2,3,4}, NOT at {0,2,4,6,8} (the latter is the curvature-degree grading n=d−2s); citing `{0,2,4,6,8}` as the s-pole set creates a factor-2 mislabel risk for every downstream `s=N` citation (α_s at s=3; §VII.BE Pati-Salam at s=6; the s=4 substrate-distance-2 slot).
**Plan reference**: `sessions/session-plan/session-96-plan-w7.md` §W7-3 (n=d−2s map; corpus `s=N` citation audit).

**Verdict**: **PASS** — value=`Mellin-firewall_LANDED; S_s_in_s={0,1,2,3,4}_matches_printed_λ^{−2s}; n=d−2s={0,2,4,6,8}_curvature-grading_stated_separately; map n=8−2s Sage-verified; α_s s=3 (Conv-A,n=2,a₂) == §VII.BE s=6 (Conv-B,n=2,a₂) SAME n=2; s_B/s_A=2 exact; §VII.BE on SU(4)_PS rank-4 extension; all corpus s=N convention-tagged=True`, scheme=`Connes-Moscovici-1995-dimension-spectrum`, convention=`half-integer-friendly-zeta-lambda-power-minus-2s`, L_max=N/A.
*(Composite PASS = all three firewall clauses hold: (a) §3.3 internally consistent — S_s={0,1,2,3,4} stated in s matches the printed λ^{−2s} power; (b) all 3 corpus s=N citations convention-tagged; (c) α_s s=3 ≡ §VII.BE s=6 both n=2 a₂-residue. The canonical line is the **PASS at line 177** (`audit_sha256=caae0b2c8e45741c…`), which **supersedes** the prior INFO at line 168 (`audit_sha256=057940334ec3046a…`) under an Option A within-dispatch script-bug correction — the bug was a malformed `clause_a` LaTeX-match predicate in the verdict script; the capstone §3.3 content was byte-identical across both emissions (`content_sha256=9472423adceaf769…` unchanged). Latest non-superseded line = the PASS.)*

**The n↔s firewall (the load-bearing reconciliation)**:

The §3.3 capstone prints the **double-power** zeta `ζ_{D_K}(s) = Σ_k m_k λ_k^{−2s}` (the CM-1995 dimension-spectrum convention) with residue poles at `s = (d−n)/2`. The boxed `{0,2,4,6,8}` is the **curvature-degree grading `n`** (≡ the CM-1995 dimension-spectrum label, the index of the Seeley-DeWitt coefficient `a_n`), **NOT** the pole set in the Mellin variable `s`. Under the printed `λ^{−2s}` power, the **pole set in `s`** is `S_s = {(d−n)/2 : n∈{0,2,4,6,8}} = {0,1,2,3,4}` at d=8.

The two integer meshes are related by the **exact algebraic identity** `n = d − 2s = 8 − 2s` (CM-1995 dimension spectrum; Sage-verified below). Stating `n` where `s` is meant mis-locates each pole by `Δ = n − s = 8 − 3s` — a **factor-≈2 mislabel** at the load-bearing poles (a₂, a₄). The firewall states `S_s` (in s) and `n=d−2s` (curvature grading) **separately** on every downstream `s=N` citation.

| curvature degree `n` | layer / residue | pole in `s` — Conv. A (`λ^{−2s}`, `s=(d−n)/2`) | pole in `s` — Conv. B (`λ^{−s}`, `s=d−n`) | corpus citation |
|:--|:--|:--|:--|:--|
| `n=0` | `a₀` (vacuum) | `s=4` | `s=8` | — |
| `n=2` | `a₂` (Einstein–Hilbert) | **`s=3`** | **`s=6`** | `α_s` → **Conv. A `s=3`**; `§VII.BE` (SU(4)_PS) → **Conv. B `s=6`** — *same `n=2` a₂ residue* |
| `n=4` | `a₄` (Yang–Mills + Higgs) | `s=2` | `s=4` | substrate-distance-2 slot `s=4` is **Conv. B** (`n=4`), the a₄ residue |
| `n=6` | `a₆` (corrections) | `s=1` | `s=2` | — |
| `n=8` | `a₈` (corrections) | `s=0` | `s=0` | — |

**Substitution chain (factor-2 mislabel claim)** — verbatim from lizzi V.1 + Sage-verified:

```
Claim:  Citing {0,2,4,6,8} as the s-pole set (vs the n=d−2s curvature grading)
        introduces a factor-2 mislabel in every downstream s=N residue citation.
Def 1:  ζ_{D_K}(s) := Σ_k m_k λ_k^{−2s}          [printed double power; CM-1995]
Def 2:  d := 8                                    [K-fiber + spinor dim carrying the SD grading]
Def 3:  n := d − 2s   (a_n at heat-trace order n; residue of ζ at s=(d−n)/2)
Sub  :  residues of Σ m_k λ_k^{−2s} sit at s=(d−n)/2 for n∈{0,2,4,6,8}
        ⇒ s ∈ {(8−0)/2,(8−2)/2,(8−4)/2,(8−6)/2,(8−8)/2} = {4,3,2,1,0}
Simp :  S_s = {0,1,2,3,4}  (pole set IN s)  ;  n = {0,2,4,6,8}  (curvature grading, NOT in s)
Canon:  s_pole and n related by n = d − 2s = 8 − 2s ; reading n as s mis-locates each pole
        by Δ = n − s = 8 − 3s   (Δ = +8,+5,+2,−1,−4 at s=0,1,2,3,4 — a factor-~2 scale error)
Dir  :  conflating the labels SHIFTS every downstream 's=N' anchor by the n=d−2s map
        ⇒ a factor-~2 magnitude mislabel — exactly the lizzi V.1 risk
Concl:  the canonical convention MUST state S_s in s AND n=d−2s separately; α_s 's=3' (n=2, a₂)
        and §VII.BE 's=6' (n=2, a₂) are the SAME residue under the map. [now justified]
```

**Sage MCP `n↔s` verification** (`sage_eval`; the exact algebraic map, regulator-axis-independent):

```
d = 8
n (curvature grading)        : [0, 2, 4, 6, 8]
s = (d−n)/2 (pole in s)       : [4, 3, 2, 1, 0]   ⇒  S_s = {0,1,2,3,4}
n = d − 2s (inverse)          : [8, 6, 4, 2, 0]   for s∈{0,1,2,3,4}
α_s s=3  ⇒ n = 8−2·3 = 2      (the a₂ residue)
§VII.BE  : n=2 ⇒ Conv-B s = d−n = 6   ; Conv-A s = (d−n)/2 = 3   ⇒ s_B/s_A = 6/3 = 2 (exact)
```

**Convention-tag audit (the 3 corpus `s=N` citations)** — each tagged with which convention + which `n`:

| corpus citation | as-printed `s` | convention | curvature `n` | residue | anchor (canonical_constants.py) | status |
|:--|:--|:--|:--|:--|:--|:--|
| `α_s` running | `s=3` | **Conv. A** (`λ^{−2s}`, `s=(d−n)/2`) | `n=2` | `a₂` | `alpha_s_substrate_distance_1 = −0.08587279` (S92) | **TAGGED ✓** |
| `§VII.BE` Pati-Salam | `s=6` | **Conv. B** (`λ^{−s}`, `s=d−n`); + on **SU(4)_PS rank-4 algebra** | `n=2` | `a₂` (SU(4)_PS Mellin-cone pole) | `residue_s6_PS_Linf = 9.3936e-4` (S95) | **TAGGED ✓** |
| substrate-distance-2 slot | `s=4` | **Conv. B** (`s=d−n`) | `n=4` | `a₄` | (S95: inherited s=4 SU(4)_PS pole DIVERGES — shell-sum L^{8−2s} converges iff s>9/2; rank-4 A₃ shifts threshold +1 vs SU(3) s>3/2) | **TAGGED ✓** |

**Anchor reconciliation (clause c, CONFIRMED)**: `α_s`'s `s=3` (Conv. A) and `§VII.BE`'s `s=6` (Conv. B) **both denote `n=2` — the a₂ residue**. The two `s`-labels are NOT a contradiction: they differ by exactly the factor-2 power-convention map (`s_B/s_A=2`, Sage-confirmed). The §VII.BE residue additionally lives on the **SU(4)_PS algebra extension** (`A_K^{PS}=ℂ⊕M₂(ℂ)_L⊕M₂(ℂ)_R⊕M₄(ℂ)`, rank-4), so its `s=6` is the SU(4)_PS Mellin-cone pole, not an SU(3) `s∈S_s` slot. With `S_s` and `n=d−2s` stated separately, no corpus `s=N` citation is mis-located. **Factor-2 downstream-citation risk: CLOSED.**

---

**ORCHESTRATOR-APPLY: regulator-pin-discipline.md Mellin pole-set pin** (I am harness-denied on rule files; this is the exact verbatim directive-only diff for you to apply — no session IDs, no per-instance narrative, per `feedback_rules-directive-only-no-session-info.md`):

> Insert as a new top-level section in `.claude/rules/regulator-pin-discipline.md` (suggested placement: immediately after the `## Tag Format` section, before `## Rationale`):

```markdown
## Mellin Pole-Set Labeling (S_s vs curvature-degree grading n)

Every citation of a Mellin-cone residue pole `s=N` of `ζ_{D_K}(s)` MUST declare
BOTH (a) the printed zeta power convention and (b) whether `N` is the pole index
in the Mellin variable `s` or the curvature-degree grading `n`. Bare `s=N`
(no convention + no S_s/n declaration) is FORBIDDEN going forward.

### Rule

The pole set in the Mellin variable `s` and the curvature-degree grading `n`
are DISTINCT integer meshes related by the exact map `n = d − 2s` (double-power
convention `ζ_{D_K}(s)=Σ m_k λ_k^{−2s}`, poles at `s=(d−n)/2`) OR `n = d − s`
(single-power convention `ζ_{D_K}(s)=Σ m_k λ_k^{−s}`, poles at `s=d−n`). At d=8:

- Double-power (Conv. A): `S_s = {0,1,2,3,4}`  ;  `n = {0,2,4,6,8} = 8 − 2s`
- Single-power (Conv. B): `S_s = {0,2,4,6,8}`  ;  `n = {0,2,4,6,8} = 8 − s`

`{0,2,4,6,8}` is ALWAYS the curvature-degree grading `n` (the CM-1995
dimension-spectrum label); it is the s-pole set ONLY under the single-power
convention. Reading `n` as if it were the double-power `s` mis-locates each pole
by `Δ = n − s = 8 − 3s` — a factor-≈2 mislabel at the load-bearing poles (a₂, a₄).

### Tag format

A Mellin residue citation carries `convention=...-poleconv-{A-double|B-single}`
AND states `(pole_in_s=N_s, curvature_grade_n=N_n)` explicitly. Example:
`a₂` residue at `s=3` (Conv. A) ≡ `s=6` (Conv. B), both `n=2`.

### Cross-algebra caveat

When the residue is evaluated on an algebra EXTENSION (e.g. SU(4)_PS rank-4
`A_K^{PS}=ℂ⊕M₂(ℂ)_L⊕M₂(ℂ)_R⊕M₄(ℂ)`), the pole index lives on the extended
spectral triple's dimension spectrum, NOT the SU(3) `S_s`; the convergence
threshold shifts (shell-sum `L^{d−2s}` converges iff `s > d_eff/2`; rank-4 A₃
shifts the threshold +1 unit vs SU(3)). Declare the algebra alongside the pole.

### Audit

`computations/_shared/_a_n_regulator_pin_audit.py` is extended to flag bare
`s=N` Mellin-residue citations lacking the `poleconv-{A|B}` tag and the
`(pole_in_s, curvature_grade_n)` declaration. Bare `s=N` → SOURCE-RECONCILIATION
advisory (S2); promotes to MANDATORY at K=3 per
`feedback_rules-compensate-missing-structure.md`.
```

---

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

- **(edit) capstone §3.3** — `sessions/framework/phonic-exflation-equation.md` lines 223–243: the printed-zeta statement relabeled (double-power convention named; `S_d={0,2,4,6,8}` annotated as the curvature grading `n`, **not** the pole index); inserted **Mellin-variable firewall** block with `S_s={0,1,2,3,4}` in s, the `n=d−2s=8−2s` map, the one-row reconciliation table, and the anchor reconciliation. Atomic section-scoped write (read → splice ONLY §3.3 → fsync + os.replace); diff-confirmed: only the §3.3 region changed (the §7-region hunks in the same file are pre-existing sibling-W7 edits, not this gate's). Firewall present exactly once.
- **(splice scripts)** — `computations/session-96/s96_w7_3_mellin_poleset_capstone_splice.py` (capstone §3.3 atomic splice + dual-SHA verdict emission; idempotent re-run guard) and `computations/session-96/s96_w7_3_mellin_poleset_wp_splice.py` (this WP section atomic splice).
- **(verdict line)** — `computations/session-96/s96_gate_verdicts.txt`: canonical PASS line (line 177) `^S96-HYG-MELLIN-POLESET:.* audit_sha256=[a-f0-9]{64}` + dual-SHA companion + schema-v2 3-tuple companion (factor-2 directional sub-claim). The PASS supersedes the prior INFO (line 168) per Option A; both `audit_sha256` are unique (sig_5 clean).
- **(ORCHESTRATOR-APPLY)** — `.claude/rules/regulator-pin-discipline.md` Mellin pole-set labeling pin: the verbatim directive-only diff block above (harness-denied to this agent; routed to orchestrator).
- No `.npz` / `.png` (METHODOLOGY-class; the artifacts ARE the capstone edit + verdict + the rule-pin recommendation).

**MCP Pre-Compute Audit** (queries executed BEFORE the convention audit; one-line salient return each):

- `search_knowledge('Connes-Moscovici dimension spectrum Mellin pole zeta_D s residue')` → CM-1995 §5 simple-dimension-spectrum theorem (PROVEN); `lizzi-spectral-functional.md` E58 boxes `S_d={0,2,4,6,8}` at d=8; `session-88-w5b` eq (1): `a_n = Res_{s=(d−n)/2} Tr(D^{−2s})` (the double-power convention — CONFIRMS the printed power).
- `search_knowledge('alpha_s s=3 substrate-distance Mellin residue a_2 running')` → `alpha_s_substrate_distance_1` derived at the Mellin-cone pole **s=3** (substrate-distance-1), `(a₄/a₂)²−1`; `session-94-plan-w2`: "s = Mellin-cone pole index = 3 [CM-1995 §III.4; Cell I]" — CONFIRMS α_s is Conv. A s=3 (n=2 a₂).
- `search_knowledge('VII.BE Pati-Salam SU(4) s=6 Mellin pole spectral dimension')` → `session-85-1d-vii-p-meta-lizzi`: "n=2 ⇒ pole at s=6 (residue ∝ a₂)" (the single-power Conv. B reading); `residue_s6_PS_Linf` = SU(4)_PS full-spectrum residue at **convergent pole s=6** (FWD-C4 §VII.BE Tier-1 re-anchor) — CONFIRMS §VII.BE s=6 is Conv-B/n=2 on the SU(4)_PS extension.
- `get_constant('alpha_s_substrate_distance_1')` → `−0.08587279` (S92, S92-AH-TR-1); provenance: "Mellin-cone pole s=3", FI-class regulator-invariant — anchor for the α_s s=3 / n=2 row.
- `get_constant('residue_s6_PS_Linf')` → `0.0009393639575775` (S95, CF-S95-VII-BE-TIER2-REANCHOR); provenance: "convergent pole s=6, L→inf; the inherited s=4 pole DIVERGES (s>9/2; rank-4 A₃ shifts threshold +1 vs SU(3) s>3/2)" — anchor for §VII.BE s=6 + the s=4 slot row.
- `sage_eval` (n↔s map, d=8): `s=(d−n)/2` ⇒ `S_s={0,1,2,3,4}`; `n=d−2s` inverse; `s_B/s_A=2` exact — the algebraic spine of the firewall.

**Substrate framing**: GEOMETRIC. The Mellin pole structure of `ζ_{D_K}(s)` **IS** the fabric's dimension spectrum — the substrate-IS set of residue locations encoding the Seeley-DeWitt curvature grading (n=0 cosmological a₀, n=2 Einstein-Hilbert a₂, n=4 Yang-Mills+Higgs a₄, …). Reading the curvature-degree grading `{0,2,4,6,8}` as if it were the s-pole set inverts the `D_K-eigenvalue → spectral-moment` direction by a factor-2 relabel: the substrate IS the pole at `s=(d−n)/2`, and a laboratory-IN observable (α_s read off the `s=3`/`n=2` residue) reads the a₂-channel moment. The firewall states `S_s` and `n=d−2s` separately so the substrate-IS pole index never drifts in any downstream laboratory-IN citation. The dimension spectrum is `τ`-independent (S31Aa) — the pole structure is regulator-axis-independent, so the firewall is a structural (FI) labeling, not a scheme-dependent one.'''


def atomic_write(path: str, text: str) -> None:
    tmp = path + ".tmp.s96w73wp"
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(text)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def main() -> int:
    with open(WP, "r", encoding="utf-8", newline="") as f:
        wp_text = f.read()  # (local)

    if "**The n↔s firewall (the load-bearing reconciliation)**" in wp_text:
        print("PREFLIGHT: §W7-3 already filled (idempotent re-run); no change.")
        return 0

    occ = wp_text.count(OLD_STUB)  # (local)
    if occ != 1:
        print(f"ERROR: OLD_STUB match count = {occ} (expected 1). Refusing to splice.")
        return 2

    new_text = wp_text.replace(OLD_STUB, NEW_BODY, 1)  # (local)

    # byte-for-byte preservation check
    roundtrip = new_text.replace(NEW_BODY, OLD_STUB, 1)  # (local)
    if roundtrip != wp_text:
        print("ERROR: byte-for-byte preservation FAILED (splice altered bytes outside §W7-3).")
        return 3

    atomic_write(WP, new_text)
    with open(WP, "r", encoding="utf-8", newline="") as f:
        disk = f.read()  # (local)
    if disk != new_text:
        print("ERROR: on-disk WP does not match intended spliced text.")
        return 4

    print("SPLICE: §W7-3 filled (atomic; only the §W7-3 stub body changed).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
