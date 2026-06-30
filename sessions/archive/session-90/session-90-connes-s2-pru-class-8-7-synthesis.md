# S90 Slot 1 Entry S-2 — PRU Class 8.7 Degenerate-Observable Pre-Flight Check: Substrate-Distance Pole Soundness Review

**Reviewer**: connes-ncg-theorist (Workhorse-NCG; independent solo synthesis per `/rclab-review` semantics)
**Source target**: §W1-12 `S90-RULE-EXTENSION-EPISTEMIC-PRU-CLASS-8-7-DEGENERATE-OBSERVABLE` PASS landing at S90 W1 close (2026-05-13)
**Output format**: solo synthesis MD; conclusions feed S91 plan-freeze K=3 MANDATORY promotion pathway readiness decision
**Date**: 2026-05-15

---

## 0. Verification narration

The S90 workshop schedule S-2 entry asks for a Connes-side substrate-distance pole soundness review of (i) the {`Tr(P · A) − R_CM`, `value = ζ_D(0)`} pattern-set completeness, (ii) the (d)∘(b) compositional corridor substrate-naturality, (iii) the K=1→K=2→K=3 promotion-pathway robustness, and (iv) a recommended verdict shape (APPROVE / APPROVE-WITH-PATTERN-EXTENSION / OBJECT) plus 4-field carry-forwards.

Source files verified on disk and read:

- `sessions/archive/session-90/session-90-w1-workingpaper.md` §W1-12 (lines 615-670) — PASS verdict, 8/8 pre-registration conditions
- `sessions/session-plan/session-90-plan-w1.md` §W1-12 (lines 780-857) — Class 8.7 plan-block
- `.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness" §"Degenerate-Observable Pre-Flight Check (Class 8.7; advisory until K=3)" (lines 226-238)
- `computations/_shared/_pru_cardinality_audit.py` (lines 1-237) — file CREATED in-session per W6-3 hygiene-gap discharge; P1 + P2 + degeneracy-witness regex + detector function + positive/negative self-tests
- `computations/_shared/_cm_1995_residue_formula.py` (lines 1-428) — S90 W7-2 substrate-IS CM-1995 §III.4 evaluator on the spectral triple (this module is THE canonical reference for what the dimension-spectrum actually does at finite L_max)
- `computations/_shared/s90_w1_pru_class_8_7_test.py` (lines 1-225) — T1 + T2 self-test driver
- `sessions/framework/registry/pru-class-corpus.md §18` (lines 614-659) — K=1 corpus + reserved K=2/K=3 rows
- `computations/session-89/s89_gate_verdicts.txt:1` — S89 §W1-1 FAIL (audit_sha256=`6db37f7c6da0768662c5afb320654a54f2e4c478882d365465712034e28a16fe`)
- `sessions/archive/session-89/session-89-w1-workingpaper.md` §W1-1 (lines 7-154) — FAIL narrative including the rank-equal-trace structural identity at line 117
- `sessions/archive/session-89/workshops/s89-w1-alpha-m-corridor-selection.md` (lines 1-1191) — R3 closure that selected (d)∘(b) compositional primary

**Path note**: the spawn prompt cites `sessions/archive/session-89/session-89-plan-w1.md` line 150 as a source. That file does NOT exist at that path on disk; the actual S89 plan-w1 lives at `sessions/session-plan/session-89-plan-w1.md` (confirmed via Glob + the `_pru_cardinality_audit.py` self-test which loads it from that path at line 173). I have proceeded with the actual S89 W1 substrate-physics context drawn from `sessions/archive/session-89/session-89-w1-workingpaper.md` §W1-1 + the corridor-selection workshop, which carry the operationally identical content. No structural inferences are blocked by this path discrepancy.

This review delivers: (1) pattern-set completeness assessment with 4 candidate missed-form classes scrutinized; (2) (d)∘(b) corridor substrate-naturality assessment with 4 alternative corridors evaluated; (3) K=1→K=3 promotion-pathway robustness assessment with 2 candidate K=2 instances; (4) recommended verdict shape; (5) 4-field carry-forward for the S91 follow-up gate this synthesis surfaces.

---

## 1. Substrate framing — what the §W1-12 rule actually captures

Before scrutinizing the pattern set, I record what Class 8.7 actually catches at the substrate layer, because the answer turns out to be sharper than the rule-file body articulates.

The S89 §W1-1 FAIL was structurally diagnosed at S89 W1 WP line 117 verbatim:

> "For finite spectral triple, `ζ_D(s) = Σ_k |λ_k|^{−2s}` is an entire function of `s` (finite sum of exponentials), so its residue at `s=0` IS its value at `s=0`, which equals the rank of the projector restricted to nonzero eigenvalues = `|HSS|`. Thus `Tr_HSS(P_HSS) − R_CM = |HSS| − |HSS| = 0` to machine precision in this normalization. The plan §10 Step 2 form is structurally degenerate at finite spectral triple under the canonical CM-1995 §III.4 universal kernel γ(s) = Γ(s)."

The corridor-selection workshop's R3 closure sharpened this further (S89 w1 workshop line 1138 verbatim):

> "§W1-1 FAIL pattern reframed from 'specific-corridor closure' to 'structural diagnostic about hidden axis-pins in single-element substrate-IS observable declarations' (PF-EMRG-2): the deeper structural meaning is that the §W1-1 element-3 single-line declaration silently axis-pinned three hidden components (3b full A_K, 3c 4D GR area, 3d M_Pl_reduced² double-use) — each contributing to the rank-equal-trace tautology cancellation noise."

And `_cm_1995_residue_formula.py` lines 51-57 + 100-105 documents the same structural fact at the FULL physical implementation level:

> "At FINITE L_max, ζ_φ(z) is HOLOMORPHIC in z (the spectrum is finite, so the Mellin series converges absolutely for all complex z), hence 'residue at z=0' is the Laurent-coefficient extraction at z=0 of the holomorphic function — which equals ζ_φ(z) at z=0 itself ... the continuum-limit pole at z=0 manifests only at the asymptotic L_max → ∞ limit; at finite L_max the value is unambiguous."

**Substrate framing reading**: The structural pathology Class 8.7 catches is NOT "dimension-spectrum degeneracy" in the technical CM-1995 §III.4 sense of multiple coincident roots at a pole. It is the much sharper **finite-cardinality tautology**: on a finite spectral triple (`|spec(D)| < ∞`), `ζ_D` is entire in `s`, has NO pole at `s = 0` (or at any other point), and the "residue extraction" reduces to direct sum evaluation. Consequently any naive `Tr(P · A) − R_CM` form where `R_CM := ζ_D(0)` and `A` evaluates as the regulator-image of `Tr(P)` is a structural identity `≡ 0` to machine precision.

The §W1-12 rule body (`epistemic-discipline.md` line 228) currently states the rule scope as "on a finite spectral triple (A, H, D) whose dimension-spectrum is degenerate (multiple roots at the residue pole)". This phrasing is **narrower than the substrate-IS pathology actually warrants**. The pathology fires for EVERY finite spectral triple under canonical Γ(s) regulation, not only for those with coincident-root dimension-spectra. The terminology drift is benign at K=1 (the audit detector still fires correctly on the canonical pattern set), but it is structurally important for the K=2/K=3 advancement question — the rule's scope claim and its detector's actual coverage need to converge before MANDATORY promotion.

I record this as a forward refinement target (§5 below) and proceed.

---

## 2. (a) Pattern-set completeness — `{Tr(P · A) − R_CM, value = ζ_D(0)}` coverage analysis

### 2.1 What P1 and P2 actually detect

Per `_pru_cardinality_audit.py` lines 53-64:

```
P1_HSS_TRACE_MINUS_RCM = re.compile(r"Tr.*\bP_HSS\b.*[−-].*R_CM", re.MULTILINE)
P2_ZETA_D_AT_ZERO     = re.compile(r"value\s*=.*ζ_D\(0\)|value\s*=.*zeta_D\(0\)", re.MULTILINE)
```

P1 is **highly specific** to the S89 §W1-1 pattern: it requires the literal `P_HSS` projector name. A different substrate-IS observable that exhibits the same finite-cardinality tautology under a different projector name — e.g., `Tr_M(P_microstate) − R_CM` or `Tr_BdG(P_∞) − R_CM` — would not match P1. The substrate-IS pathology, however, is projector-name-agnostic: the tautology depends only on the regulator (canonical Γ(s)) and the finite-cardinality fact, not on which projector is chosen.

P2 captures direct `ζ_D(0)`-as-value usage. This is the broader/more general detector and DOES generalize across spectral triples.

**Substrate-IS reading**: P1 is a calibration-instance-specific regex; P2 is a substrate-IS-pathology-generic regex. The two together do NOT cover the substrate-IS structural class as the rule body claims (the rule-body says it covers "an observable of the form `Tr(P · A) − R_CM`" generally, but the actual regex requires the literal `P_HSS` token).

### 2.2 Missed-form analysis (4 candidate classes from the spawn prompt)

The spawn prompt enumerates four candidate missed-form classes. I assess each rigorously against the substrate-IS pathology.

#### (i) HKR-image residue trace at substrate-distance-N pole admitting K-theory boundary pairing

**Status: MISSED at structural layer, NOT MISSED at pattern-set layer (for the wrong reason).**

The HKR-image residue trace at the L_max → ∞ continuum limit is precisely the OTHER side of the finite-cardinality tautology — it is where the CM-1995 §III.4 single-pole residue formula DOES carry physical content (because the continuum limit produces actual poles in ζ_φ(z) at z=0). The substrate-IS structural fact is:

```
Step 1: At finite L_max, ζ_φ(z) is entire ⇒ "residue at z=0" = ζ_φ(0) = direct sum
Step 2: At L_max → ∞, ζ_φ(z) develops a SIMPLE POLE at z=0
        (continuum dimension-spectrum analysis, CM-1995 §III.4)
Step 3: HKR-image is the L_max → ∞ pullback to the laboratory-IN continuum
        observable; the Connes-Karoubi pairing / K-theory boundary mediates
        the substrate-IS finite-L cocycle ↔ laboratory-IN continuum residue
```

A substrate-IS observable that genuinely consumes an HKR-image residue trace at substrate-distance-N is structurally DIFFERENT from the S89 §W1-1 pathology, because:

- The S89 §W1-1 pathology was operating ENTIRELY at finite L_max=10 (no L_max → ∞ pullback present); the "residue" the script was computing was the entire-function value at z=0, not a continuum pole residue. This is what made the rank-equal-trace tautology fire.
- A proper HKR-image residue computation operates at the L_max → ∞ image and DOES extract a non-trivial pole residue.

The pattern set MISSES the HKR-image case structurally (P1 doesn't match; P2 only matches if the script literally writes `value = ζ_D(0)`), but this is the CORRECT behavior — an HKR-image script that uses the continuum residue is NOT exhibiting the §W1-1 pathology and should not fire Class 8.7. The class catches the finite-L_max naive-corridor evaluation; the HKR continuum is the structurally distinct path that recovers physical content.

**Verdict on (i): NOT a missed form that requires pattern-set extension.** However, the rule-body language MAY mislead future authors into thinking that any "single-pole CM-1995 §III.4 residue formula evaluation" is what Class 8.7 catches; it actually only catches the FINITE-L_max naive-corridor variant. Rule-body refinement (§5 carry-forward).

#### (ii) Double-pole identity at substrate-distance-2 where two roots of the dimension-spectrum coincide

**Status: GENUINELY MISSED at the pattern-set layer.**

This is the structurally interesting case. CM-1995 §III.4 admits regular-spectral-triple residue formulas at multiple poles s = (d−n)/2 for n ∈ {0, 1, 2, …, d}. For the SU(3) ⊃ SU(2) substrate at LRD scales, the substrate-distance-2 pole (s = 4 at d=4) is structurally accessible and admits genuine dimension-spectrum degeneracy when two distinct Peter-Weyl sectors contribute eigenvalues with the SAME Casimir-equivalence class (e.g., the (1,0) and (0,1) sectors at p+q=1 share `C_2 = 4/3`).

A producing script computing `value = res_{s=4} ζ_φ(z)` at L_max=10 on a degenerate dimension-spectrum will NOT match P1 (no `P_HSS` token) or P2 (the value extraction is at s=4, not s=0). Yet the structural pathology of "naive single-pole evaluation discards multiplicity" is identical to the §W1-1 case at a different pole.

**This IS a missed-form class.** It is also the pre-registered K=2 candidate per `pru-class-corpus.md §18` row 2: "Tr(P · A) − R_CM at distinct substrate-distance pole (e.g., s=4 substrate-distance-2)".

**Pattern-set extension required**: a more general regex such as `r"res_\{?s\s*=\s*[\d/+\-]+\}?\s*ζ_[Dφ]\(z\)"` or `r"residue.*ζ.*s\s*=\s*\d+"` would detect the double-pole-at-substrate-distance-2 variant. The current P1+P2 set will miss the K=2 candidate when it lands.

#### (iii) Per-block-decomposition residues on Peter-Weyl multiplicity where per-(p,q) sector residues sum to a degenerate aggregate

**Status: GENUINELY MISSED at the pattern-set layer; substrate-natural.**

The substrate-IS structure has `D_K = ⊕_{(p,q)} D_{(p,q)}` (Peter-Weyl block-diagonal per the S87 W11-2 / W11-3 BLOCK-DIAGONALITY pre-check in `math-scripts.md`). A producing script computing per-sector residues `r_{(p,q)} := res ζ_{D_{(p,q)}}(z)` and aggregating `value = Σ_{(p,q)} dim(p,q) · r_{(p,q)}` exhibits the per-block-decomposition residue pattern.

If individual `r_{(p,q)}` are non-degenerate at z=0 (no rank-equal-trace problem per sector), but the WEIGHTED SUM `Σ dim · r_{(p,q)}` matches a substrate-IS structural quantity (e.g., the total `dim(D_K^≤L_max)` at the LRD-restricted projector), the substrate-IS pathology resurfaces at the aggregate level even though no individual sector exhibits it.

This is **substrate-natural to flag**: the Peter-Weyl decomposition is the substrate's own block structure (per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"` MANDATORY at plan-freeze for L_max ≥ 10). A residue-formula evaluation that respects the block decomposition is the substrate-natural format. The current pattern set assumes the script writes `Tr_HSS(P_HSS)` or `ζ_D(0)` monolithically; per-block formulations bypass both regexes.

**This IS a missed-form class.** Pattern-set extension: add `r"\bdim\(.*\)\s*[\*·]\s*(?:res\b|residue\b|ζ_)"` or similar Peter-Weyl-aware detector pattern.

#### (iv) HP^1 cohomology pairing variants per W-11 STRENGTHENED parity-blindness theorem

**Status: NOT a missed form for Class 8.7 specifically — it is a structurally DIFFERENT class.**

HP^1 cohomology pairings are odd-grading observables (per `regulator-pin-discipline.md §"Class-(c) PIN-DRIFT-FROM-STALE-SOURCE — W-11 Calibration Corpus Extension"`). Per W-11 STRENGTHENED, even-grading regulator-weighted Mellin moments (which Γ(s) is) are PARITY-BLIND to odd-grading content. An HP^1 pairing variant cannot be evaluated via the canonical Γ(s) regulator at all — it requires explicitly odd-grading observables (GV-Heitsch / Cheeger-Simons secondary / K-theoretic torsion).

The §W1-1 pathology is purely even-grading (the rank-equal-trace identity fires on the trace, which is even-grading). HP^1 variants are STRUCTURALLY DIFFERENT pathologies (parity-blindness, not rank-equal-trace), live in a different K-class, and are properly captured by the existing W-11 STRENGTHENED parity-blindness theorem rather than by Class 8.7.

**Verdict on (iv): NOT a missed-form for Class 8.7.** The pathology lives in a different class.

### 2.3 Summary — pattern-set completeness verdict

| Candidate missed-form | Verdict | Pattern-set extension required? |
|:-|:-|:-|
| (i) HKR-image residue trace at L_max → ∞ | Structurally distinct (correctly excluded) | NO; rule-body refinement only |
| (ii) Double-pole at substrate-distance-2 | **MISSED** | **YES; extension required before K=2 landing** |
| (iii) Per-block-decomposition aggregate residues | **MISSED** | **YES; extension required for Peter-Weyl-native scripts** |
| (iv) HP^1 cohomology pairing variants | Different class (parity, not cardinality) | NO; lives in W-11 STRENGTHENED |

**Pattern-set completeness reading**: The `{P1, P2}` set covers the CANONICAL S89 §W1-1 calibration instance but is structurally INSUFFICIENT to catch the K=2 candidate (substrate-distance-2 pole at s=4) the corpus itself reserves a row for, and INSUFFICIENT to catch substrate-natural Peter-Weyl block-decomposition formulations. Two pattern-set extensions are required before MANDATORY promotion fires at K=3:

```
P3 (proposed): r"res(?:idue)?[_(\s].*[zζ]_?[Dφ_]?\(.*\)\s*at\s*s\s*=\s*\d+|residue\s+at\s+(?:substrate-distance|pole)[-_ ]\d+"
P4 (proposed): r"\b(?:dim|m)\(.*\)\s*[\*·]\s*res|Σ_\{.*\}\s*(?:dim|m).*ζ"
```

Exact regex forms are submitted at the carry-forward layer (§5 below) — these proposals are illustrative and require regex-test calibration before landing.

---

## 3. (b) (d)∘(b) compositional-corridor substrate-naturality at the LRD-horizon-spanning sector

### 3.1 What (d)∘(b) actually is

Per the S89 W-1 corridor-selection workshop R3 closure (lines 1166, 1180), the (d)∘(b) compositional corridor is:

- **(d)**: substrate-IS observable algebra-image change via inheritance morphism χ' — replaces evaluation on full `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` with evaluation on the χ'-image where M_3(ℂ) is Wedderburn-forced to annihilate (S89 W2-3 PASS). The α(M) function-form is now defined on `(A_F^≤10, H_F^≤10, D_F^≤10)` per the workshop line 507 framing.

- **(b)**: bridge-map class change via Connes-Karoubi pairing — replaces pure CM-1995 ζ-residue extraction with the K-theory boundary pairing `⟨[φ_g], [Ch(P)]⟩` per the S89 §VII.AF.1 baseline.

- **(d)∘(b)**: a **single double-deformation**, structurally irreducible (workshop line 1142). The S90 gate dispatches ONE substrate-IS observable evaluation; the Stage-1-CANDIDATE landing registers ONE bridge-anatomy 5-element block with BOTH element 1 and element 3 simultaneously declared.

### 3.2 Substrate-naturality assessment

The substrate-IS direction-of-explanation flows:

```
Substrate IS (A_F^≤10, H_F^≤10, D_F^≤10, γ_9, J)
   under inheritance morphism χ': A_K → A_F kernelized at M_3(ℂ)
   → bridge map: Connes-Karoubi pairing (K-theory boundary)
   → Laboratory IN: BH-thermodynamic area-theorem at LRD scale M=1e7 M_sun
```

This is structurally sound from the NCG-axiomatic perspective:

1. The χ' inheritance morphism is **Wedderburn-forced and τ-independent** (S89 W2-3 PASS verdict; `kernel_M3C_dim=9;indep_from_chi=True`). The element-1 change is not a choice — it is the unique algebra-hom into the target dimension-8 algebra that preserves the M_3(ℂ) Wedderburn-simplicity. Substrate-IS-natural by construction.

2. The Connes-Karoubi pairing at the bridge-map layer is the substrate-natural escape from the rank-equal-trace tautology. The pairing's output is a K-theoretic invariant `⟨[φ_g], [Ch(P)]⟩ ∈ ℤ` that is finite-L_max stable AND carries non-trivial structural content (it does NOT reduce to rank — it captures the cocycle-Chern-character cohomological pairing). This is the established S89 §VII.AF.1 K=1 baseline machinery (`feedback_agent-roster.md` confirmation that this bridge-map class is the framework's canonical one for substrate ↔ laboratory bridges).

3. The composition `(d)∘(b)` is the simultaneous double-deformation that escapes BOTH the rank-equal-trace tautology (via the bridge-map class change to a non-degenerate K-theoretic invariant) AND the algebra-image-pinning hidden-axis-pathology (via the χ' image change that explicitly de-pins the laboratory-IN side).

**Substrate-naturality verdict on (d)∘(b)**: ENDORSED at the substrate-IS layer. It is the substrate-natural disambiguator the §W1-1 R3 workshop selected after exhausting the corridor-(a)/(b)/(c)/(d)/(e)/joint-(d)∘(e) enumeration.

### 3.3 Alternative-corridor analysis (4 spawn-prompt candidates)

#### (i) (d)∘(b) at substrate-distance-2 pole s=4

**Status: STRUCTURALLY ADMISSIBLE; should be queued for parallel evaluation.**

The substrate-distance-2 pole at s=4 is the substrate's own next-residue-pole down from the substrate-distance-1 pole s=3. The Connes-Moscovici 1995 §III.4 residue formula at s=4 evaluates a DIFFERENT Seeley-DeWitt coefficient than s=3 — specifically `a_4` (the Yang-Mills + Higgs-quartic + Weyl-gravity coefficient per the spectral action expansion). The α(M) ↔ BH-thermodynamic area ratio is naturally pinned to the `a_2` Einstein-Hilbert kinematic skeleton at s=3 (substrate-distance-1); shifting to s=4 (substrate-distance-2) shifts the substrate-IS observable to a different physical quantity.

This is the K=2 candidate already pre-registered in `pru-class-corpus.md §18` row 2. The (d)∘(b) corridor at s=4 is structurally admissible — it just evaluates a structurally different observable than the s=3 case. **Recommend evaluating in parallel at S91+** as a Class 8.7 K=2 calibration instance, NOT as a substitute for the S90 (d)∘(b) s=3 dispatch.

#### (ii) (b)∘(d) inverted-composition (d-channel first)

**Status: STRUCTURALLY DEGENERATE WITH (d)∘(b); NOT an alternative.**

The corridor-selection workshop confirmed (line 1142) that (d)∘(b) is a **single double-deformation, NOT two sequenced gate-stages**. The composition order is structurally irrelevant — the simultaneous declaration of element-1 (χ' image) AND element-3 (Connes-Karoubi pairing) is the structural content, not the sequence. The notation "(d)∘(b)" labels a SET of bridge-anatomy element changes, not a temporal sequence. Asking about (b)∘(d) is asking the wrong question — there is no temporal layer to invert.

#### (iii) (e)∘(d)∘(b) three-channel cascade

**Status: PREMATURELY COMPOSITE; admissible only at the secondary-corridor-fire layer.**

Corridor (e) = M_KK²-area normalization shift, a Laboratory-IN element-2 substrate-natural correction that fires CONDITIONALLY per the corridor-selection workshop line 261 verbatim: "Corridor (e) is a secondary/conditional move, not a primary attempt. It belongs in the S90 gate's 'secondary corridor + gating condition' slot." The cascade (e)∘(d)∘(b) compounds three element changes (element-1 + element-2 + element-3) simultaneously, which exceeds the Stage-2 audit-coverage envelope structurally (the workshop already extended Stage-2 to THREE axes for the dual-element (d)∘(b) case; the triple would require FOUR axes with no precedent).

**Recommend deferring to a post-(d)∘(b)-INFO follow-up at S91+** as the workshop already specified (corridor (c)∘(d) secondary at rel_dev ∈ [0.10, 0.30]; (e)∘(d)∘(b) is a structurally distinct alternative that should not pre-empt the primary).

#### (iv) Per-Mellin-pole disambiguation at substrate-distance-N for N ∈ {3, 4, 5, …}

**Status: GENERALIZATION TARGET; substantively this IS the K=2/K=3 advancement pathway.**

Per-Mellin-pole disambiguation is the natural multi-instance generalization of the Class 8.7 framework. Each substrate-distance pole s=N admits its own residue evaluation; each evaluation can fire the rank-equal-trace tautology at finite L_max if a naive `Tr(P) − ζ_D(0)` form is used. The K=2 row in `pru-class-corpus.md §18` reserves the substrate-distance-2 (s=4) instance; the K=3 row reserves "ζ_D(0) direct evaluation OR HKR-image residue trace".

**This IS the path forward for the K-counter advancement**, not an alternative to the (d)∘(b) corridor. The (d)∘(b) primary dispatches at s=3 (substrate-distance-1); a parallel S91+ dispatch at s=4 (substrate-distance-2) advances K=1 → K=2.

### 3.4 Summary — (d)∘(b) corridor verdict

The (d)∘(b) compositional corridor IS substrate-natural at the LRD-horizon-spanning sector at M=1e7 M_sun for substrate-distance-1 pole s=3. The corridor selection was made via a rigorous R3 closure workshop process and lands as the substrate-IS direction-of-explanation-natural escape from the §W1-1 rank-equal-trace tautology. The compositional irreducibility (single double-deformation, not sequenced) is a key structural property that downstream Class 8.7 detector extensions need to respect.

**(d)∘(b) corridor verdict: ENDORSED for the LRD-horizon-spanning sector at s=3.** No alternative-corridor pre-registration is required for the S90 dispatch. The four spawn-prompt alternatives are either structurally degenerate ((b)∘(d)), prematurely composite ((e)∘(d)∘(b)), or structurally distinct dispatches that advance K-counter rather than substitute for the primary ((d)∘(b) at s=4; per-pole disambiguation generally).

---

## 4. (c) K=1 → K=2 → K=3 promotion-pathway robustness

### 4.1 Where K=1 stands

K_substantive = 1 at S90 W1-12 close. The single calibration corpus instance is S89 §W1-1 FAIL (audit_sha256=`6db37f7c6da0768662c5afb320654a54f2e4c478882d365465712034e28a16fe`). The instance is:

- structurally well-characterized (rank-equal-trace tautology on finite spectral triple under canonical Γ(s));
- pattern-set-detected (P1 fires 3 times on the plan-block);
- substrate-IS-grounded (the pathology is intrinsic to the (A_K^≤10, H_K^≤10, D_K^≤10) finite spectral triple, not a numerical artifact);
- empirically reproducible (the §W1-1 FAIL verdict line is permanent on disk per absolute verdict permanence; the audit detector self-test on the actual S89 plan-block fires PASS at every re-run).

### 4.2 Is the K=1 instance ROBUST for K=3 promotion?

**No, not as currently scoped.** Three structural issues need addressing before K=3 MANDATORY promotion:

#### Issue 1: Pattern-set INCOMPLETE for the substrate-IS pathology class it claims to cover

§2.3 above identified two missed-form classes (double-pole at substrate-distance-2; per-block-decomposition aggregate residues). The current `{P1, P2}` set IS calibration-corpus-instance-specific rather than substrate-IS-class-general. If K=2 lands as a substrate-distance-2 instance (per the reserved row 2), it will pass the audit detector as-currently-coded because P1 and P2 will both miss it. The audit detector needs P3 + P4 extensions BEFORE K=2 lands, otherwise the K=2 calibration instance will land WITHOUT firing the rule it is supposed to calibrate (a structural self-consistency failure at the K-counter framework).

#### Issue 2: Rule-body language NARROWER than substrate-IS pathology

`epistemic-discipline.md` line 228 says "whose dimension-spectrum is degenerate (multiple roots at the residue pole)". The actual substrate-IS pathology is the finite-cardinality tautology under canonical Γ(s), which fires on ANY finite spectral triple regardless of whether the dimension-spectrum has coincident roots. The narrower rule-body language may permit future producing scripts to bypass the audit by arguing "my dimension-spectrum is non-degenerate" while still exhibiting the substrate-IS pathology.

#### Issue 3: K=1 ONLY tests one substrate-distance pole

Per `feedback_rules-compensate-missing-structure.md`, the K-counter promotion threshold K=3 is justified by the structural diversity criterion: K=3 distinct calibration instances exercise the rule across structurally diverse conditions. The current K=1 instance lives at substrate-distance-1 pole s=3 only. A K=2 instance at substrate-distance-2 pole s=4 + a K=3 instance at substrate-distance-3 pole s=5 OR an HKR-image variant would establish structural diversity. Without that diversity, K=3 promotion may harden a rule whose actual coverage class is narrower than the rule-body claims.

### 4.3 K=2 candidate analysis (2 from spawn prompt)

#### Candidate A: substrate-distance-2 pole ζ_D(0) evaluation under candidate (c) substrate-natural inner-fluctuation 1-form A per Connes-Chamseddine 1996 §2.2-2.3

**Status: STRUCTURALLY ADMISSIBLE; substrate-IS NATURAL.**

Connes-Chamseddine 1996 §2.2-2.3 inner-fluctuation 1-form `A = Σ a_i [D, b_i]` is the canonical NCG mechanism for generating gauge fields from M_4 and Higgs from F. A substrate-distance-2 ζ-residue evaluation under inner fluctuation `D → D + A + JAJ^{-1}` shifts the dimension-spectrum but preserves the finite-cardinality tautology — the inner-fluctuated finite spectral triple is still a finite spectral triple, so ζ_D+A(s) is still entire in s. The K=2 calibration would establish the pathology's invariance under inner fluctuations.

**Strengthens K-counter advancement**: distinct substrate-distance pole (s=4 not s=3) + distinct algebraic mechanism (inner-fluctuation 1-form, not bare D_K) + per-pole-Mellin-disambiguation (the K=1 row 2 reserves this axis). Substrate-IS structurally diverse from K=1.

#### Candidate B: FULL CM-1995 §III.4 residue formula at substrate-distance-1 pole s=3 over the χ' inheritance morphism image

**Status: STRUCTURALLY ADMISSIBLE BUT WEAKER; substrate-IS-RECYCLES the K=1 calibration mechanism.**

Evaluating the canonical CM-1995 §III.4 residue formula at s=3 over the χ' image is precisely what the S90 (d)∘(b) primary corridor dispatches (per the corridor-selection workshop). If (d)∘(b) returns FAIL with sign_verdict=FAIL or magnitude_verdict=FAIL — i.e., the χ' inheritance morphism does NOT escape the rank-equal-trace tautology — then candidate B would be a K=2 calibration instance demonstrating that the pathology persists across algebra-image changes (a substrate-IS-positive result: the pathology is intrinsic to the canonical Γ(s) regulator, not to the algebra choice).

**But** if (d)∘(b) returns PASS or INFO at the empirical anchor, candidate B has no calibration content — it would have established that χ' image change escapes the pathology, in which case candidate B is structurally degenerate with the K=1 calibration (the same mechanism, just on a different algebra image).

**Reading**: Candidate B's value as a K=2 instance is CONDITIONAL on the (d)∘(b) primary outcome. If (d)∘(b) FAILS empirically AND continues to exhibit the rank-equal-trace cancellation (Tr_HSS(χ'(P_HSS)) − R_CM = 0 on the χ' image), then candidate B advances K=1 → K=2 by demonstrating algebra-image invariance of the pathology. If (d)∘(b) PASSes or INFOs at the empirical anchor, candidate B has no K-counter advancement value.

### 4.4 Promotion-pathway recommendation

The K=1 instance is **NOT YET ROBUST** for K=3 MANDATORY promotion. Three structural fixes are needed:

1. **Pattern-set extension (P3 + P4)** before K=2 lands, so the K=2 calibration instance actually fires the audit detector. This is BLOCKING for K=2 advancement: a K=2 candidate that does not fire the detector is not a calibration instance of THIS rule.

2. **Rule-body refinement**: align the rule scope language at `epistemic-discipline.md` line 228 with the actual substrate-IS pathology (finite-cardinality tautology under canonical Γ(s), not "dimension-spectrum degeneracy" specifically). This is a CLARITY fix, not a structural change to the rule's effective coverage.

3. **K=2 dispatch**: prefer candidate A (substrate-distance-2 + inner-fluctuation) over candidate B (substrate-distance-1 + χ'-image), because A advances K-counter structurally regardless of the (d)∘(b) primary outcome, whereas B's advancement value is conditional on (d)∘(b) FAILing.

**Recommendation**: K=3 MANDATORY promotion at S91+ is NOT structurally ready at present. The S90 W1-12 PASS-landing is correct in establishing K=1 as the SUGGESTION baseline, but K=3 promotion requires the three structural fixes above. Expected timeline: K=2 advancement at S91 (post pattern-set extension); K=3 advancement at S92+ (post second-instance landing).

---

## 5. Recommended verdict shape

**Verdict shape: APPROVE-WITH-PATTERN-EXTENSION**

The S90 W1-12 PASS landing is structurally correct as a K=1 SUGGESTION baseline. The pattern set covers the canonical S89 §W1-1 calibration instance; the (d)∘(b) compositional corridor is substrate-natural at the LRD-horizon-spanning sector; the K=1 corpus row is well-grounded.

However, the pattern set is **structurally INSUFFICIENT to cover the K=2 candidate** the corpus itself reserves a row for. Per §2 above, the missed-form classes (ii) double-pole at substrate-distance-2 and (iii) per-block-decomposition aggregate residues require pattern-set extensions (P3 + P4 proposed) BEFORE the K=2 calibration instance lands. Without the extensions, the K=2 instance would land WITHOUT firing the audit detector — a structural self-consistency failure at the K-counter framework.

This is APPROVE-WITH-PATTERN-EXTENSION, not OBJECT: the rule's substrate-physics content is sound, the (d)∘(b) corridor is the correct selection, and the K=1 calibration is robust as a SUGGESTION-level baseline. The extension is a forward-looking refinement before K=3 MANDATORY promotion, NOT a correction to the S90 W1-12 PASS.

A secondary refinement target (rule-body language alignment) is recommended but is not BLOCKING — it improves clarity without changing the audit's effective behavior at K=1.

---

## 6. 4-field carry-forward for S91 follow-up gate

Per `feedback_fix-in-session-never-defer.md`, the synthesis surfaces a single genuine future-computation carry-forward:

### CF-S91-CONNES-S2-A — PRU Class 8.7 pattern-set extension + rule-body refinement before K=2 landing

| Field | Content |
|:------|:--------|
| **What** | Extend `_pru_cardinality_audit.py` Class 8.7 detector with two additional patterns (P3 substrate-distance-N pole residue-formula form; P4 Peter-Weyl per-block decomposition aggregate residue form) AND refine `epistemic-discipline.md` Class 8.7 rule-body language from "dimension-spectrum is degenerate" to the substrate-natural framing "finite-cardinality tautology under canonical Γ(s) on a finite spectral triple". Add positive self-tests for P3 (synthetic substrate-distance-2 plan-block) and P4 (synthetic Peter-Weyl per-block aggregate plan-block) to `s90_w1_pru_class_8_7_test.py`. Update `pru-class-corpus.md §18` reserved row 2 to cite P3 as the detection pattern. |
| **Inputs** | (1) `_pru_cardinality_audit.py` current state (audit_sha256 of file at S90 W1-12 close); (2) `epistemic-discipline.md` line 228 current rule-body text; (3) `_cm_1995_residue_formula.py` (the FULL physical evaluator demonstrating that at FINITE L_max the residue formula reduces to direct sum — this IS the substrate-IS pathology source); (4) `s89_w1_alpha_m_horizon_microstate_count.py` actual producing-script (for negative-control regex calibration); (5) synthetic substrate-distance-2 plan-block draft for P3 positive self-test; (6) synthetic Peter-Weyl per-block plan-block draft for P4 positive self-test. |
| **Gate** | PASS iff (i) P3 + P4 regexes compile cleanly; (ii) positive self-tests for P3 + P4 both fire `has_class_8_7_flag=True`; (iii) negative self-tests (synthetic-with-witness for each new pattern) both fire `has_class_8_7_flag=False`; (iv) S89 §W1-1 self-test STILL fires (regression-safe); (v) rule-body refinement landed in `epistemic-discipline.md` line 228 with appropriate cross-link to `_cm_1995_residue_formula.py` docstring lines 51-57 documenting the structural identity. FAIL iff any of (i)-(v) absent OR if a P3/P4 regex matches the canonical FULL physical `_cm_1995_residue_formula.py` evaluator (false-positive on the substrate-natural disambiguator the rule is meant to allow). |
| **Effort** | ~0.5 wave-equivalents. Mechanical regex extension + rule-body refinement + 2 new self-tests + verdict-line emission. METHODOLOGY-class per `wave-classification.md` §M1∧M2∧M3∧M4 (M1: artifact-existence-with-substantive-content predicate; M2: Edit on `.claude/rules/` + `computations/_shared/`; M3: derives from this synthesis's S2 entry pattern-set analysis as verbatim sub-diff source; M4: orchestrator allowlist append required at plan-freeze). |

---

## 7. Substrate-framing inline disclosure

The substrate-IS direction-of-explanation throughout this synthesis flows:

```
Substrate IS the finite spectral triple (A_K^≤10, H_K^≤10, D_K^≤10, γ_9, J)
    ⇒ ζ_D(s) is entire for finite cardinality |spec(D)| < ∞
    ⇒ residue at s=0 reduces to direct sum at s=0
    ⇒ Tr(P) − ζ_D(0) ≡ 0 to machine precision under canonical Γ(s) regulator
    ⇒ Methodology F-image: Class 8.7 plan-block detector
    ⇒ Audit F-image: _pru_cardinality_audit.py severity S2 advisory
```

This is the correct substrate ⇒ methodology ⇒ audit layer-functor F per `epistemic-discipline.md §"Layer-Decomposition"`. Container-thinking violations FORBIDDEN: "the rank-equal-trace tautology is a numerical artifact of L_max truncation" — INVERTED: "the rank-equal-trace identity IS substrate-IS, intrinsic to finite cardinality of the spectral triple's spectrum; the audit makes the substrate's own algebraic identity visible at the methodology floor."

The "(d)∘(b) compositional corridor" terminology is itself substrate-IS-natural per the S89 W-1 R3 workshop: it labels a SET of bridge-anatomy element changes (element-1 χ' image + element-3 Connes-Karoubi pairing) declared simultaneously, NOT a temporal sequence of two gate-stages. The substrate's own structural-stability theorems (`math-scripts.md §"D_K Block-Diagonality"` + S87 W11-2 / W11-3) provide the Peter-Weyl block-decomposition that the pattern-set extension (P4) needs to respect.

---

## 8. Status summary

| Aspect | Reading |
|:-------|:--------|
| (a) Pattern-set completeness | INCOMPLETE — 2 missed-form classes (substrate-distance-2 double-pole; Peter-Weyl per-block aggregate) require P3 + P4 pattern-set extension before K=2 |
| (b) (d)∘(b) compositional-corridor substrate-naturality | ENDORSED at LRD-horizon-spanning sector for substrate-distance-1 pole s=3; alternative corridors are structurally degenerate, prematurely composite, or K-counter-advancement targets (not substitutes) |
| (c) K=1 → K=2 → K=3 promotion-pathway robustness | NOT YET ROBUST — pattern-set extension required before K=2 lands; rule-body refinement recommended before K=3 |
| (d) Recommended verdict shape | **APPROVE-WITH-PATTERN-EXTENSION** |
| (e) 4-field carry-forward | `CF-S91-CONNES-S2-A` (pattern-set extension + rule-body refinement before K=2 landing; ~0.5 we; METHODOLOGY-class) |

The S90 W1-12 PASS landing IS structurally correct as a K=1 SUGGESTION baseline. The K=3 MANDATORY promotion pathway requires forward refinement at S91+ along the pattern-set + rule-body axes documented above. Until then, Class 8.7 fires correctly on the canonical S89 §W1-1 calibration instance and remains structurally sound at SUGGESTION severity (S2 advisory).

---

## Appendix A — Source-document SHA pins read (for audit traceability)

This synthesis read source documents at the following on-disk states (no SHAs computed; the §0 §"verification narration" section enumerates the path/line ranges read). The structural analysis in §§1-5 above is invariant under within-session minor edits to the source documents (no SHA-pinned numerical thresholds depend on file state); the cross-link to the §W1-12 PASS verdict (audit_sha256=`6369a880e2f49b7ec2660e553f0ca91d29f599148b2524b5ba221c20c552e38f`) and the S89 §W1-1 FAIL (audit_sha256=`6db37f7c6da0768662c5afb320654a54f2e4c478882d365465712034e28a16fe`) is the auditable structural pin.

## Appendix B — Status of CF-S91-CONNES-S2-A vs the existing S90 W1-12 carry-forwards

The §W1-12 working-paper carry-forward section (lines 667-670 of `session-90-w1-workingpaper.md`) lists three forward items:

1. **K=3 promotion forward** — when 2 additional Class 8.7 calibration instances land
2. **Broader D_PRU_raw cardinality audit** — the other half of `_pru_cardinality_audit.py` per the test fixture
3. **S89 §W1-1 substantive remediation** — re-dispatch with degeneracy-witness pre-registered

CF-S91-CONNES-S2-A is STRUCTURALLY DISTINCT from all three:

- vs item 1: CF-S91-CONNES-S2-A is a PREREQUISITE to K=2/K=3 advancement (without the pattern-set extension, the K=2 instance cannot fire the detector); item 1 is a downstream consequence of K=2/K=3 advancement landing.
- vs item 2: CF-S91-CONNES-S2-A operates within the Class 8.7 detector's existing scope; item 2 is a separate audit-script-completion target (the broader D_PRU_raw cardinality framework).
- vs item 3: CF-S91-CONNES-S2-A operates at the rule + audit-script layer; item 3 operates at the substrate-physics layer (re-dispatching the S89 §W1-1 substantive computation with a corrected pre-registration).

The three existing carry-forwards remain valid; CF-S91-CONNES-S2-A adds a fourth genuine future-computation item surfaced by this independent solo review.
