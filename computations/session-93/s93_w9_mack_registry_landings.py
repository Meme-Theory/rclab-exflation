#!/usr/bin/env python
"""
S93 Wave 9 — mack-cosmic-bridge registry/corpus landings (3 landings, 5 sub-edits).

SOLE-WRITER landing dispatch (mack-cosmic-bridge per feedback_mack-bridge-role.md) for the
three S93 W9 registry-side flags. NOT a new gate -- registry/corpus landing only; NO new
verdict line (the W9-3/W9-4/W9-5 gate verdicts already on disk supply the closure SHAs).

AFTER-pattern (registry-landing.md "Bridge-Landing Script Architecture"):
  build_all_edits_in_memory -> atomic_write_with_fsync -> re_read + verify_each_anchor.

Parallel-writer-safe atomic single-section replacement (epistemic-discipline.md
"Registry-Write Hygiene under Parallel-Writer Race"): each edit is an exact unique-string
replacement; the whole-file new content is built in memory then written atomically via a
temp file + os.replace.

LANDING 1 -- corpus §10 Instance #3 (Bridge-map-scheme suffix discipline, axis β) K=2->K=3.
LANDING 2 -- corpus §8 Instance #4 (Per-Bulletin-per-pole) pole-distinct K=2->K=3.
LANDING 3 -- W9-5 Layer-Functor F CLOSE: registry §VII.AU.OP-PROJ REINDEX block (Block A + Block B)
            FALSIFIED-at-K=2 -> CLOSED; W6-1 alpha=2.6926237 anchor re-scoped to a Level-3
            record of the S82 within-channel F_2-axis FI contour-deformation identity (PRESERVED).

NOTE on spawn-prompt anchor mismatches (reported, not fabricated):
 - There is NO standalone "open-channel ledger" file with a FALSIFIED-at-K=2 entry for the
   Layer-Functor F channel; the open_channels knowledge-DB type is a derived synthesis of
   registry/atlas prose. The Layer-Functor F K=2 SUGGESTION entity lives ONLY as the REINDEX
   block at permanent-results-registry.md §VII.AU.OP-PROJ. The CLOSE lands there.
 - There is NO Layer-Functor F K=2 SUGGESTION row in cross-pillar-bridge-corpus.md §"Hybrid
   Independence Test" (§3 is the §VII.AF.1/AG.1 K=1 baseline). No corpus row to retire; the
   REINDEX corpus is the registry §VII.AU.OP-PROJ block. No corpus §3 edit is made.
"""

import os
import sys
import hashlib

# Canonical-constants import (math-scripts.md MANDATORY for S34+). This landing script writes
# registry/corpus TEXT only; the one framework constant it touches is the substrate slice the
# three landings cite (tau_fold). The assertion below guards against a stale tau_fold drifting
# into the registry text -- all three landings reference the tau_fold=0.19 substrate slice.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_shared"))
from canonical_constants import tau_fold

ROOT = r"C:\sandbox\Ainulindale Exflation"
TAU_FOLD_CITED = 0.19  # (local) the substrate slice the W9-3/W9-4 landings cite, asserted == canonical
CORPUS = os.path.join(ROOT, "sessions", "framework", "registry", "cross-pillar-bridge-corpus.md")
REGISTRY = os.path.join(ROOT, "sessions", "permanent-results-registry.md")

# --- W9-3 / W9-4 / W9-5 closure SHAs (from on-disk verdict lines; NOT recomputed) ---
W9_3_AUDIT = "4bf4a91786f1bd8b34300f2c0dddb8ff6fc61e43012f9479b63412f8172eea27"   # (local)
W9_4_AUDIT = "a370d0fdcda9c469644d670260751bfb3f6d5bd7e22dee3f01b86f123fa829a0"   # (local)
W9_5_AUDIT = "ee62172902c2cf26269ba8a12cc4cc5a2d36b6b76f44b6211861de132700c253"   # (local)
K1_SUFFIX_SHA = "f634be0d942241095e40ce71562b69fee522faaa520c9ce861844c15f02a8f77"  # (local) S90 W7-4
K2_SUFFIX_SHA = "1fef32c8f88d89f39548f0b086717b7efea8e82f3c015b73c947977f9d573f58"  # (local) S91 W9-11


def atomic_write(path, text):  # (local) temp + os.replace; fsync for durability
    tmp = path + ".tmp_mack_s93"
    with open(tmp, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, path)


def apply_unique(text, old, new, label):  # (local) exact unique-string replacement; idempotent
    if new in text and text.count(old) == 0:
        print(f"[idempotent] {label}: NEW text already present, OLD anchor gone -- skip (re-run safe).")
        return text
    n = text.count(old)
    if n != 1:
        raise SystemExit(f"ANCHOR-FAIL [{label}]: expected exactly 1 occurrence of OLD, found {n}. NOT landing.")
    return text.replace(old, new)


# ======================================================================================
# LANDING 1 -- corpus §10 Instance #3 row + status flip K=2 -> K=3 MANDATORY (axis beta).
# Anchor: the "Element 3 status" K=1 line + the §10 cross-reference closing block.
# ======================================================================================

L1_STATUS_OLD = """### Element 3 status

K=1 at 2026-05-08; advisory until K=3."""

L1_STATUS_NEW = """### Element 3 status

Element-3 fiducial-anchor binding axis (n_s pre-substrate pin track): K=1 at 2026-05-08; advisory until K=3.

Bridge-map-scheme suffix discipline (axis β) track: **K=3 MANDATORY** at 2026-05-24 (S93 W9-3 third HIT-distinct calibration instance; Instance #3 below). K_pre=2 (S91 W9-11) → K_post=3. The parent rule `.claude/rules/cross-pillar-bridge-anatomy.md §"Bridge-map-scheme suffix discipline"` status flips SUGGESTION → MANDATORY at K=3 (orchestrator wave-close edit; subagents edit-denied on `.claude/rules/`)."""

L1_INSTANCE3 = """
#### Instance #3 — S93 W9-3 ρ-invariant scheme-INDEPENDENCE on the Pillar-V BdG sector (2026-05-24)

**Bridge-map-scheme suffix discipline calibration corpus instance #3** (K_pre=2 → K_post=3 **MANDATORY** on axis β = Bridge-map-scheme suffix discipline). This is the THIRD structurally-independent calibration instance; the K-counter advancement criterion of `feedback_rules-compensate-missing-structure.md` (K=3 promotion threshold) is satisfied, so the parent rule promotes SUGGESTION → MANDATORY. The K=3 promotion candidate "queued for S93+" in Instance #2's cross-references (ρ-invariant on Pillar-V BdG sector under three η-schemes) IS this landing.

**S93 W9-3 verdict trace** (canonical line at `computations/session-93/s93_gate_verdicts.txt:187`):
- Gate: `S93-W9-3-BRIDGE-MAP-SCHEME-SUFFIX-K3-MANDATORY-THIRD-INSTANCE`
- audit_sha256 = `4bf4a91786f1bd8b34300f2c0dddb8ff6fc61e43012f9479b63412f8172eea27`
- content_sha256 = `eb4ff4cf24f81bb42e2f92bf4fb598fc1dffccde4744f2be4401bc1e11cac734`
- Composite verdict: PASS (LEG 1 COMPUTE Reading A); LEG 2 METHODOLOGY K=3 advancement LICENSED.
- Substrate-IS observable: the Atiyah-Patodi-Singer ρ-invariant on the Pillar-V BdG sector — the `M_2(ℂ) ⊂ A_K` image of the χ inheritance morphism `χ : ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ)` (3He-B vortex-core spectroscopy realization per `inheritance-falsifier-protocol.md`), evaluated on the S90 W8 FULL-BdG corner-IV rederivation spectrum at L_max=12, τ_fold=0.19.
- Three η-form schemes: `ρ_APS = ρ_CS = ρ_BC = 0.000000e+00` EXACTLY (M_KK² units). Pairwise: `diff_AC = diff_AB = diff_CB = 0.000000e+00`; **`max_pairwise_diff = 0.000000e+00`** vs band `EPS_INDEP = 1e-3` → 0 ≤ 1e-3 by ~13 OOM margin (Reading A scheme-INDEPENDENCE).
- BdG positive branch `E_k = [0.7629, 0.8690 (×3), 1.1437, 1.1306 (×3)]` M_KK; `E_min = 0.762915 > 0` ⇒ the sector is GAPPED (IR-self-regularized by R-PROTECTED `Delta_BCS = 0.4642547`). Full Nambu spectrum sum-of-signs = 0.0 (exact BDI ±-pairing) ⇒ `dim ker(D_BdG) = 0`.
- Pins: `level_class_pin = FULL` (S90 W8 FULL-BdG); `regulator_pin = a_n^{Mellin}` (reduced-eta Mellin class); `binding_axis = substrate-natural-binding` (the BdG ρ-invariant is the substrate's OWN secondary-class evaluation — NO canonical-import pin; distinct from K=2's `canonical-import-binding` cross-pin anchor).

**HIT (Hybrid Independence Test) — K=3 advancement criterion `(i ∨ ii ∨ iii) ∧ iv`**:

| Instance | substrate-IS pillar | bridge-map class | algebraic envelope |
|:---------|:--------------------|:-----------------|:-------------------|
| K=1 (S90 W7-4 CF-55, `f634be0d…`) | Pillar III (C_H, C_εH) parity-twin | GV-Heitsch (Godbillon-Vey secondary class on HP¹) | HP¹ GV-Heitsch τ-response envelope |
| K=2 (S91 W9-11, `1fef32c8…`) | §VII.AQ HP¹ pillar | GV-Heitsch | §VII.AQ HP¹ GV-Heitsch τ-response envelope |
| **K=3 (this gate, `4bf4a917…`)** | **Pillar V (3He-B BdG sector)** | **ρ-invariant (reduced eta on the BdG K-homology class)** | **BdG-sector reduced-eta envelope (M_2(ℂ) Nambu spectrum)** |

- **(i) distinct substrate-IS pillar** = TRUE (Pillar V ≠ Pillar III, ≠ §VII.AQ HP¹).
- **(iii) distinct bridge-map class** = TRUE (ρ-invariant ≠ GV-Heitsch on both prior instances).
- **(iv) independent algebraic envelope** = TRUE (BdG-sector reduced-eta envelope, NOT a numerical refinement of the §VII.AQ HP¹ GV-Heitsch envelope).
- HIT predicate `(i ∨ iii) ∧ iv = True` (in fact (i) ∧ (iii) ∧ (iv) all hold) ⇒ K=3 MANDATORY advancement LICENSED (K_pre=2 → K_post=3). This is NOT a numerical refinement of K=1/K=2 (axis (iv) PASS): a genuinely new (pillar, bridge-class, envelope) instance.

**Substrate framing** (per `phononic-framing.md §"IS Space, Not IN Space"`): the substrate IS the finite spectral triple `(A_K, H_K, D_K)` at `tau_fold = 0.19`; the substrate's BdG ρ-invariant on the `M_2(ℂ)` inheritance image IS scheme-INDEPENDENT at the cohomology-class layer BECAUSE all three η-form schemes are F-images of the SAME Connes-Karoubi secondary-class pairing on the BdG K-homology class, and the BDI ±-pairing forces η ≡ 0 in EVERY scheme: the sign-sum (APS), the z=0 sign-asymmetry residue (CS), and the heat-kernel-weighted trace `Tr(D_BdG e^{−tD²}) = Σ_{±E}(±E)e^{−tE²} = 0` (BC) all cancel term-by-term. Agreement IS structural identity (the substrate's intrinsic robustness AT the secondary-class evaluation morphism). Container-thinking FORBIDDEN: NOT "the three schemes happen to agree"; INVERT to "the substrate's BdG ρ-invariant IS scheme-INDEPENDENT at the cohomology-class level". The corpus Instance #3 row REGISTERS this substrate-IS structural identity at the audit-text layer; direction flows FROM the substrate (BdG ρ-invariant) TOWARD the methodology consequence (axis-β K=3 MANDATORY).
"""

# The §10 closing cross-reference block: update the K=3-promotion-candidate line + parent-rule
# status line to record the landed K=3 MANDATORY.
L1_XREF_OLD = """- Parent rule: `.claude/rules/cross-pillar-bridge-anatomy.md §"Bridge-map-scheme suffix discipline"` (SUGGESTION at K=2 after this landing).
- K=1 calibration instance: S90 W7-4 CF-55 substrate-physics adjudicator landing; companion rationale entry at `sessions/framework/registry/methodology-wave-instances.md` S90 W7-4 axis β block; verdict line at `computations/session-90/s90_gate_verdicts.txt:128` (audit_sha256=`f634be0d942241095e40ce71562b69fee522faaa520c9ce861844c15f02a8f77`).
- K=2 calibration instance (this row): S91 W9-11 audit (audit_sha256=`1fef32c8f88d89f39548f0b086717b7efea8e82f3c015b73c947977f9d573f58`); verdict line at `computations/session-91/s91_gate_verdicts.txt:218`; producing script `computations/session-91/s91_w9_bridge_map_scheme_independence_audit.py`.
- K=3 promotion candidate (queued for S93+): ρ-invariant on Pillar-V BdG sector under three η-schemes; HIT (i)-distinct substrate-IS pillar + (iii)-distinct bridge map class vs both K=1 and K=2 instances; K=3 MANDATORY threshold pending."""

L1_XREF_NEW = """- Parent rule: `.claude/rules/cross-pillar-bridge-anatomy.md §"Bridge-map-scheme suffix discipline"` (**MANDATORY at K=3** after the S93 W9-3 Instance #3 landing; orchestrator flips SUGGESTION → MANDATORY at the rule-file).
- K=1 calibration instance: S90 W7-4 CF-55 substrate-physics adjudicator landing; companion rationale entry at `sessions/framework/registry/methodology-wave-instances.md` S90 W7-4 axis β block; verdict line at `computations/session-90/s90_gate_verdicts.txt:128` (audit_sha256=`f634be0d942241095e40ce71562b69fee522faaa520c9ce861844c15f02a8f77`).
- K=2 calibration instance: S91 W9-11 audit (audit_sha256=`1fef32c8f88d89f39548f0b086717b7efea8e82f3c015b73c947977f9d573f58`); verdict line at `computations/session-91/s91_gate_verdicts.txt:218`; producing script `computations/session-91/s91_w9_bridge_map_scheme_independence_audit.py`.
- K=3 calibration instance (Instance #3 above; LANDED S93 W9-3): ρ-invariant on Pillar-V BdG sector under three η-schemes; HIT (i)-distinct substrate-IS pillar (Pillar V) + (iii)-distinct bridge map class (ρ-invariant) + (iv)-independent envelope vs both K=1 and K=2 instances; audit_sha256=`4bf4a91786f1bd8b34300f2c0dddb8ff6fc61e43012f9479b63412f8172eea27`; verdict line at `computations/session-93/s93_gate_verdicts.txt:187`; producing script `computations/session-93/s93_w9_3_bridge_map_scheme_suffix_k3_rho_invariant_pillar_v_bdg.py`. **K=3 MANDATORY threshold reached.**"""


# ======================================================================================
# LANDING 2 -- corpus §8 Instance #4 row + status flip (pole-distinct K=2 -> K=3 MANDATORY).
# The existing §8 Status declared "K=3 at cohomology-class-distinct dimension" but
# "SUGGESTION-pending-pole-distinct-K=3 for ... NEW substrate-distance poles s ∈ {5,6,7,...}".
# W9-4 supplies the pole-distinct (s=5) third instance, completing the pole-distinct criterion.
# ======================================================================================

L2_STATUS_OLD = """### Status

K=3 at cohomology-class-distinct dimension (MANDATORY-at-cohomology-class-distinct-K=3 for S89+ Pillar-VII Bulletin-class entries SHARING substrate-distance pole with existing corpus instances). SUGGESTION-pending-pole-distinct-K=3 for S89+ entries at NEW substrate-distance poles s ∈ {5, 6, 7, ...}; the §W10-120 DORMANT shell is queued to surface the pole-distinct third instance, at which point the rule promotes to fully-MANDATORY at K=3 across both criteria.

The standard K=3 project-wide promotion threshold per `feedback_rules-compensate-missing-structure.md` is met; the stricter pole-distinct criterion (`s ∉ {s=3, s=4}`) remains pending."""

L2_STATUS_NEW = """### Status

K=3 at cohomology-class-distinct dimension (MANDATORY-at-cohomology-class-distinct-K=3 for S89+ Pillar-VII Bulletin-class entries SHARING substrate-distance pole with existing corpus instances).

**Pole-distinct criterion: K=3 MANDATORY at 2026-05-24** (S93 W9-4 third pole-distinct instance at substrate-distance-3 pole **s=5**; Instance #4 below). The stricter pole-distinct criterion (`s ∉ {3, 4}`) that was previously pending is now SATISFIED — the S93 W9-4 (s=5) landing surfaces the pole-distinct third instance that the §W10-120 DORMANT shell was queued for, so the rule promotes to **fully-MANDATORY at K=3 across both criteria** (cohomology-class-distinct AND pole-distinct). Future Pillar-VII Bulletin-class entries at distinct poles MUST declare the per-pole 4-tuple `(pole_index, regulator-invariance, observable-class, layer)` AND provide the per-pole Level-1/2/3 ladder.

The standard K=3 project-wide promotion threshold per `feedback_rules-compensate-missing-structure.md` is met on BOTH criteria. The parent rule `.claude/rules/cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` flips advisory(pole-distinct) → MANDATORY at K=3 (orchestrator wave-close edit; subagents edit-denied on `.claude/rules/`)."""

# Insert Instance #4 narrative immediately AFTER the existing Instance #3 narrative block
# (anchor: the §VII.AR Instance #3 narrative closing sentence about §W10-120 DORMANT shell).
L2_INST3_TAIL_OLD = """This instance is at substrate-distance pole s=4, sharing the pole with §VII.K-PROP.W10-4 but distinct at the cohomology-class structure dimension (W10-4 is the ρ_∞ permanent-wall; W7a-74 is the LEVEL-DRESSED rank-ordering). The §W10-120 DORMANT shell is queued to surface the pole-distinct third instance when activated, completing the fully-MANDATORY promotion."""

L2_INST3_TAIL_NEW = """This instance is at substrate-distance pole s=4, sharing the pole with §VII.K-PROP.W10-4 but distinct at the cohomology-class structure dimension (W10-4 is the ρ_∞ permanent-wall; W7a-74 is the LEVEL-DRESSED rank-ordering). The pole-distinct third instance (a NEW pole `s ∉ {3, 4}`) that the §W10-120 DORMANT shell was queued for is supplied by Instance #4 below (S93 W9-4 at substrate-distance-3 pole s=5), completing the fully-MANDATORY promotion.

### Instance #4 — S93 W9-4 closed-form β at the NEW substrate-distance-3 pole s=5 (pole-distinct K=3; 2026-05-24)

**Pole-distinct calibration corpus instance** (the third pole-distinct instance, completing the stricter `s ∉ {3, 4}` criterion). NEW triplet = **(P_BdG Cartan-diagonal projector [p=q], K-theory-boundary bridge, substrate-distance-3 pole s=5)**.

**S93 W9-4 verdict trace** (canonical line at `computations/session-93/s93_gate_verdicts.txt:191`):
- Gate: `S93-W9-4-PER-BULLETIN-PER-POLE-K3-ADVANCEMENT`
- audit_sha256 = `a370d0fdcda9c469644d670260751bfb3f6d5bd7e22dee3f01b86f123fa829a0`
- content_sha256 = `3ebdd60470b4ad70fce1a96af8e9649b1fc7602d010784a0e4791952b8bc4c86`
- Composite verdict: PASS (`max_rel_dev = 0.000e+00 ≤ 0.05` substrate-derived closed-form reproduction; HIT predicate True).

| Level | Per-Bulletin-per-pole form | s=5 value |
|:------|:---------------------------|:----------|
| Level-1 (cohomology-class identity) | per-pole substrate-distance-IS spectral identity at the s-th Mellin-cone pole; FI, algebra-INVARIANT | single balanced Cartan sector `S(2p) = dim(p,p)·(C_2(p,p)+1)^{−5} = (p+1)^{3−2s} = (p+1)^{−7}` (CM-1995 §III.4 residue; `dim(p,p)=(p+1)³`, `C_2(p,p)+1=(p+1)²`; Sage-verified 200-bit) |
| Level-2 (algebraic envelope) | per-pole `L^{−α(s)}` truncation envelope | asymptotic strip [10,100] → `α^∞ = 2s−3 = 7`; in-cache {4,6,8,10} β=4.160504504605278; asymptotic-strip β=5.97051278441794; (cache 4.16 < asym 5.97 < asymptote 7, monotone) |
| Level-3 (empirical anchor) | numerical value at canonical L_max | `β_substrate = β_emp = 4.160504504605278` at in-cache window; `rel_dev = 0.000e+00 ≤ 0.05` (substrate-DERIVED, zero free parameters; the single-Cartan-sector combinatorial sum IS the exact rational the closed form expresses) |

Per-pole 4-tuple: `(pole_index=5, FI, algebra-INVARIANT, atlas-row)` — FI because the single-sector shell sum is an exact rational (regulator-invariant, no IR scale; F_2-class FI inheritance per `regulator-pin-discipline.md §"β_shell FI Classification"`); algebra-INVARIANT because `S(L)` is a spectrum-only combinatorial functional `Σ m_k g(λ_k)`; atlas-row because the closed form is the locked-norm closed-form algebraic identity (`substrate-first-canonical-sourcing.md §(ii.A)`).

**HIT distinctness** (`cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"` `(i ∨ ii ∨ iii) ∧ iv`):

| Instance | pole_index | bridge-map class | α^∞ = 2s−3 (envelope) |
|:---------|:----------:|:-----------------|:---------------------:|
| K=1 (S92 W8-3 O_2) | s=3 | HKR | 3 |
| K=2 (S92 W8-3 O_3) | s=4 | Connes-Karoubi (sub-dist-2) | 5 |
| **K=3 (this gate)** | **s=5** | **K-theory boundary** | **7** |

- (iii) bridge-map class **K-theory boundary** is distinct from HKR (K=1) and Connes-Karoubi (K=2) — the HKR / Connes-Karoubi / K-theory-boundary trichotomy named in the bridge anatomy. **TRUE.**
- (iv) independent algebraic envelope: `α^∞ = 7 ∉ {3, 5}`; also pole_index s=5 ∉ {3, 4}. **TRUE.**
- HIT `= (i ∨ ii ∨ iii) ∧ iv = (iii) ∧ (iv) = True` ⇒ pole-distinct K=3 MANDATORY advancement LICENSED.

**Substrate framing** (per `phononic-framing.md §"IS Space, Not IN Space"`): the substrate IS the finite spectral triple `(A_K, H_K, D_K)` at the τ_fold=0.190 slice of the Jensen flow; the per-pole convergence exponent β IS a substrate-IS Mellin-cone functional — the rate at which the substrate's finite-L Cartan-diagonal shell sum at pole s=5 converges to its L→∞ image. The closed form is substrate-FIXED (a Wodzicki/Mellin residue, NOT a fit); the `rel_dev = 0` reproduction CERTIFIES the substrate derivation rather than tuning to a target. Direction flows FROM the substrate (D_K eigenvalues → Cartan single-sector shell sum `(p+1)^{−7}` → CM-1995 §III.4 residue exponent `α^∞ = 2s−3 = 7`) TOWARD the methodology consequence (per-pole pole-distinct K=3 MANDATORY); NEVER inverted.

- Producing script: `computations/session-93/s93_w9_4_per_bulletin_per_pole_k3_closed_form_beta.py`."""


# ======================================================================================
# LANDING 3 -- W9-5 Layer-Functor F CLOSE.
#   3-A: registry §VII.AU.OP-PROJ REINDEX Block A -- "SUGGESTION at K=2 PRESERVED under REINDEX"
#        -> FALSIFIED-at-K=2 -> CLOSED, with closure rationale + S82 carve-out preservation.
#   3-B: registry §VII.AU.OP-PROJ Block B -- "Layer-Functor F K=2 SUGGESTION REINDEXED" pin in the
#        STAGE-1-CANDIDATE promotion sub-section -> CLOSED annotation (no contradictory live K=2).
#   3-C: W6-1 alpha=2.6926237 anchor re-scoped from a universal-envelope theorem anchor to a
#        Level-3 record of the S82 within-channel F_2-axis FI contour-deformation identity.
# ======================================================================================

# 3-A: open the REINDEX block with a CLOSE banner (prepended to the block header line).
L3A_HEADER_OLD = """**S91 W5/W6 Layer-Functor F K-counter REINDEX documentation** (in-session FIX-IN-SESSION landing 2026-05-22 per `feedback_fix-in-session-never-defer.md` + user correction "only math carries forward; everything else is done at the time — rules are clear on this"; W5 workshop "What Changed" (b) Structural changes #1 line 1360 CF-W6-4-S91-4 = Edit 9; mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`):"""

L3A_HEADER_NEW = """> **[S93 W9-5 CLOSE — FALSIFIED-at-K=2 → CLOSED, 2026-05-24]** The Layer-Functor F Verdict-Shape Consistency Theorem **universal-envelope / asymptotic-universal reading documented in this REINDEX block is RETIRED (CLOSED) at K=2** by the S93 W9-5 adversarial workshop (lizzi × landau; VERDICT-B CLOSE; `audit_sha256=ee62172902c2cf26269ba8a12cc4cc5a2d36b6b76f44b6211861de132700c253` at `computations/session-93/s93_gate_verdicts.txt:195`). **Decisive evidence** (regulator-INVARIANT, at the Friedrich-Bär-SATURATED L→∞ layer where Level-1 lives): §W9-3 CF-W6-4-S91-1 σ_β **GREW** from the cache baseline 0.8936 to **1.065** under FB saturation (η_FB=0.547 ≥ 0.40 CERTIFIED; β_O1/O2/O3/O4 = 1.354/2.092/3.428/1.029, a 2.5× spread WIDER than cache) — the asymptotic-universal Level-1 prediction σ_β → 0 is contradicted at the exact layer it was placed by S92 W8-1 Reading_Hybrid. **Corroborating leg** (RD/SCHEME-DEPENDENT): §W9-5 Richardson α_sub=0.876 (sub-geometric; divergent step ratio 2.105; anchor-crossing L=10; α_∞=−10.71). The CLOSE does NOT retroactively overturn S92 W8-1 (which left FB-saturation as the pending Level-1 confirmation; §W9-3 IS that test and returned disconfirmation). **PRESERVED carve-out**: the S82 W-3 within-channel F_2-axis FI contour-deformation identity (α_Mellin = α_zeta EXACT at the simple pole s=3, CM-1995 §III.4) is independently PROVEN, FI, and UNTOUCHED — it is NOT the universal-envelope SUGGESTION and survives the CLOSE; the W6-1 α=2.6926237 EXACT anchor is re-scoped (below) as a Level-3 record of THAT within-channel identity, not a universal-envelope theorem anchor. The REINDEX text below is RETAINED on disk for audit provenance; its K=2 SUGGESTION status is superseded by this CLOSE banner.

**S91 W5/W6 Layer-Functor F K-counter REINDEX documentation** (in-session FIX-IN-SESSION landing 2026-05-22 per `feedback_fix-in-session-never-defer.md` + user correction "only math carries forward; everything else is done at the time — rules are clear on this"; W5 workshop "What Changed" (b) Structural changes #1 line 1360 CF-W6-4-S91-4 = Edit 9; mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`):"""

# 3-A status line inside the REINDEX block (Step 5 "SUGGESTION at K=2 PRESERVED under REINDEX").
L3A_STEP5_OLD = """- **Step 5 (direction)**: SUGGESTION at K=2 PRESERVED under REINDEX; calibration corpus instances (§VII.AF.1.OP-PROJ + §VII.AU.OP-PROJ) BOTH PASS the REINDEXED scope predicate at the asymptotic Level-1 leading-term `-3` layer. K=3 MANDATORY promotion requires a THIRD substantively distinct calibration instance per `feedback_rules-compensate-missing-structure.md` K-counter threshold; queued for forward saturation at future Cell I × same-pole bridge-anatomy entries."""

L3A_STEP5_NEW = """- **Step 5 (direction)**: ~~SUGGESTION at K=2 PRESERVED under REINDEX~~ — **SUPERSEDED: FALSIFIED-at-K=2 → CLOSED (S93 W9-5; see CLOSE banner above)**. The K=2-distinctive universal-envelope / asymptotic-universal content is falsified at the FB-saturated L→∞ layer (§W9-3 σ_β=1.065, GREW under saturation) and corroborated by the §W9-5 Richardson divergence; the K-counter does NOT promote to K=3 and does NOT survive at "K=2-weak" (no non-empty intersection of {distinctly-K=2} ∩ {survives the evidence} per the W9-5 R3 substitution-chain). The forward-saturation queue for a THIRD calibration instance is **withdrawn** — the corridor closes. The substantive substrate-physics content that survives is the S82 within-channel F_2-axis FI contour-deformation identity (independently PROVEN, FI), NOT a distinctly-K=2 universal-envelope claim."""

# 3-B: Block B pin in the STAGE-1-CANDIDATE sub-section (lines ~19087): annotate as CLOSED.
L3B_OLD = """- **Layer-Functor F K=2 SUGGESTION REINDEXED** (W5 workshop R2 Convergence #5 + EMRG-V-R2-4 + Re:L4 DISAGREE #2): SUGGESTION at K=2 calibration corpus saturation under REINDEXED scope to "Level-1 leading-term -3 universal across Cell I + same-pole bridge-anatomy corpus" — INSTANCE #1 = §VII.AF.1.OP-PROJ HP^1 cohomology norm at Pillar III ↔ Pillar IV Cell I × s=3; INSTANCE #2 = §VII.AU.OP-PROJ `n_s² − 1 ≡ α_s` Sage-QQ identity at Pillar I ↔ Pillar II Cell I × s=3. Hybrid Independence Test predicate `(i ∨ ii ∨ iii) ∧ iv = (YES ∨ YES ∨ NO) ∧ YES = YES` PASSes at K=2 saturation: (i) Pillar I vs Pillar III distinct substrate-IS pillar; (ii) Pillar II vs Pillar IV distinct laboratory-IN pillar; (iii) HKR `L_max → ∞` shared bridge map class — disjunction PASS via (i) AND (ii); (iv) HP^1 cohomology norm vs `n_s² − 1 ≡ α_s` Sage-QQ identity in Q — independent algebraic envelope. K=3 MANDATORY promotion requires THIRD substantively distinct calibration instance per `feedback_rules-compensate-missing-structure.md` K-counter threshold."""

L3B_NEW = """- **Layer-Functor F K=2 SUGGESTION REINDEXED** — **CLOSED at K=2 (S93 W9-5 VERDICT-B; FALSIFIED-at-K=2 → CLOSED; `audit_sha256=ee62172902c2cf26269ba8a12cc4cc5a2d36b6b76f44b6211861de132700c253`)**. The universal-envelope / asymptotic-universal "Level-1 leading-term -3 universal across Cell I + same-pole bridge-anatomy corpus" reading is RETIRED: §W9-3 σ_β GREW 0.8936 → 1.065 at the Friedrich-Bär-SATURATED L→∞ layer (regulator-INVARIANT; the decisive FI blow at the exact layer Level-1 was placed), corroborated by §W9-5 Richardson sub-geometric divergence (α_sub=0.876). Two NEGATIVE-CALIBRATION records absorbed into the closure rationale: Reading B-strong 4-observable-family universal FALSIFIED at finite L (S91 W6-4 σ_β=0.8936); Level-1 asymptotic-universal (Reading_Hybrid) FALSIFIED at the FB-saturation layer (§W9-3 σ_β=1.065). The K-counter does NOT promote to K=3 and does NOT survive at "K=2-weak". ~~The historical K=2-saturation Hybrid Independence Test predicate `(i ∨ ii ∨ iii) ∧ iv = YES` is RETAINED below for audit provenance only — it no longer licenses a live K=2 SUGGESTION:~~ [historical] (i) Pillar I vs Pillar III distinct substrate-IS pillar; (ii) Pillar II vs Pillar IV distinct laboratory-IN pillar; (iii) HKR `L_max → ∞` shared bridge map class; (iv) HP^1 cohomology norm vs `n_s² − 1 ≡ α_s` Sage-QQ identity — independent algebraic envelope. **PRESERVED carve-out**: the S82 within-channel F_2-axis FI contour-deformation identity (α_Mellin = α_zeta EXACT at pole s=3) is independently PROVEN, FI, and untouched (re-scoped W6-1 anchor below). The §VII.AU.OP-PROJ STAGE-1-CANDIDATE status is UNAFFECTED — the algebra-axis K=3 MANDATORY classification (next bullet) and the S82 within-channel FI identity remain the structural pins; the Layer-Functor F K=2 universal-envelope pin is retired, not replaced by a different live SUGGESTION."""

# 3-C: re-scope the W6-1 alpha=2.6926237 anchor. The cleanest single load-bearing site is the
# Element-5 numerical-sample line (19075), which currently frames alpha=2.6926 as "F_2-axis FI
# agreement". Add the S82 within-channel identity Level-3-record re-scoping there.
L3C_OLD = """**Element 5 numerical sample** (per W5 workshop EC1 + EMERGE #1 dual-pin landing): `α_Mellin = α_zeta = 2.692624 EXACT` at L_fit ∈ [15, 22] on §VII.AU.OP-PROJ pathway-b direct Connes-Karoubi pairing (Sage-Q rational); F_2-axis FI agreement at α=2.6926 within F_2 = {ζ, SDW} K-invariant identity sub-atlas at L_max=12. Out-of-F-contour PV-cutoff-lattice readings deferred-pending CF-S91-W6-1-PV-CUTOFF-LATTICE-FULL-PHYSICAL-RETRY (S92+; OPEN-VERDICT per `epistemic-discipline.md §"Cross-Proxy Adjudication"` clause 2 with 3-outcome pre-registration Lizzi-PASS / Connes-PASS / INFO)."""

L3C_NEW = """**Element 5 numerical sample** (per W5 workshop EC1 + EMERGE #1 dual-pin landing): `α_Mellin = α_zeta = 2.692624 EXACT` at L_fit ∈ [15, 22] on §VII.AU.OP-PROJ pathway-b direct Connes-Karoubi pairing (Sage-Q rational); F_2-axis FI agreement at α=2.6926 within F_2 = {ζ, SDW} K-invariant identity sub-atlas at L_max=12. **[S93 W9-5 re-scope, 2026-05-24]** This `α_Mellin = α_zeta = 2.6926237 EXACT` agreement IS a Level-3 record of the **S82 W-3 within-channel F_2-axis FI contour-deformation identity** (α_Mellin = α_zeta EXACT at the simple pole s=3, CM-1995 §III.4) — an independently PROVEN, FI, regulator-class-INVARIANT identity within the F_2 = {ζ, SDW} sub-atlas. It is **NOT** an anchor of the (now-CLOSED) Layer-Functor F universal-envelope / Verdict-Shape Consistency reading (S93 W9-5 VERDICT-B; `audit_sha256=ee62172902c2cf26269ba8a12cc4cc5a2d36b6b76f44b6211861de132700c253`). The within-channel S82 identity (α_Mellin = α_zeta within ONE fixed (projector, bridge, pole) channel) and the retired cross-observable universal-envelope SUGGESTION (σ_β → 0 ACROSS observables) are STRUCTURALLY DISTINCT claims; the CLOSE retires the latter and leaves the former intact. Out-of-F-contour PV-cutoff-lattice readings deferred-pending CF-S91-W6-1-PV-CUTOFF-LATTICE-FULL-PHYSICAL-RETRY (S92+; OPEN-VERDICT per `epistemic-discipline.md §"Cross-Proxy Adjudication"` clause 2 with 3-outcome pre-registration Lizzi-PASS / Connes-PASS / INFO)."""


def main():
    # ---- guard: the substrate slice the landings cite MUST match the canonical tau_fold ----
    assert abs(tau_fold - TAU_FOLD_CITED) < 1e-12, (
        f"tau_fold drift: canonical={tau_fold} != cited-in-landings={TAU_FOLD_CITED}; "
        "registry text would mis-state the substrate slice. NOT landing."
    )
    print(f"[guard] tau_fold canonical={tau_fold} == cited={TAU_FOLD_CITED}")

    # ---- read both files ----
    with open(CORPUS, "r", encoding="utf-8", newline="") as fh:
        corpus = fh.read()
    with open(REGISTRY, "r", encoding="utf-8", newline="") as fh:
        registry = fh.read()

    corpus_in_sha = hashlib.sha256(corpus.encode("utf-8")).hexdigest()      # (local)
    registry_in_sha = hashlib.sha256(registry.encode("utf-8")).hexdigest()  # (local)
    print(f"[pre]  corpus   sha256={corpus_in_sha}")
    print(f"[pre]  registry sha256={registry_in_sha}")

    # ---- build all corpus edits in memory ----
    c = corpus
    c = apply_unique(c, L1_STATUS_OLD, L1_STATUS_NEW, "L1 §10 status")
    # append Instance #3 narrative immediately before the §10 cross-references block:
    # anchor it after Instance #2's substrate-framing paragraph, before "**Cross-references**:"
    L1_INST3_MARKER = "#### Instance #3 — S93 W9-3 ρ-invariant scheme-INDEPENDENCE on the Pillar-V BdG sector"
    L1_XREF_HEADER = "**Cross-references**:\n- Parent rule: `.claude/rules/cross-pillar-bridge-anatomy.md §\"Bridge-map-scheme suffix discipline\"`"
    if L1_INST3_MARKER in c:
        print("[idempotent] L1 §10 Instance #3: already present -- skip insertion.")
    else:
        if c.count(L1_XREF_HEADER) != 1:
            raise SystemExit("ANCHOR-FAIL [L1 §10 xref header]: not unique.")
        c = c.replace(L1_XREF_HEADER, L1_INSTANCE3 + "\n" + L1_XREF_HEADER)
    c = apply_unique(c, L1_XREF_OLD, L1_XREF_NEW, "L1 §10 cross-references")

    c = apply_unique(c, L2_STATUS_OLD, L2_STATUS_NEW, "L2 §8 status")
    c = apply_unique(c, L2_INST3_TAIL_OLD, L2_INST3_TAIL_NEW, "L2 §8 Instance #4")

    # ---- build all registry edits in memory ----
    r = registry
    # L3A header banner: L3A_HEADER_NEW ENDS with L3A_HEADER_OLD (banner is PREPENDED), so the
    # generic apply_unique "new contains old" guard mis-fires -> guard on the banner token itself.
    L3A_BANNER_TOKEN = "> **[S93 W9-5 CLOSE — FALSIFIED-at-K=2 → CLOSED, 2026-05-24]**"
    if L3A_BANNER_TOKEN in r:
        print("[idempotent] L3A REINDEX header CLOSE banner: already present -- skip (re-run safe).")
    else:
        r = apply_unique(r, L3A_HEADER_OLD, L3A_HEADER_NEW, "L3A REINDEX header CLOSE banner")
    r = apply_unique(r, L3A_STEP5_OLD, L3A_STEP5_NEW, "L3A Step5 CLOSE")
    r = apply_unique(r, L3B_OLD, L3B_NEW, "L3B Block-B pin CLOSE")
    r = apply_unique(r, L3C_OLD, L3C_NEW, "L3C Element-5 anchor re-scope")

    # ---- atomic write ----
    atomic_write(CORPUS, c)
    atomic_write(REGISTRY, r)

    # ---- re-read + verify each anchor landed and no stale anchor remains ----
    with open(CORPUS, "r", encoding="utf-8", newline="") as fh:
        c2 = fh.read()
    with open(REGISTRY, "r", encoding="utf-8", newline="") as fh:
        r2 = fh.read()

    checks = [  # (local) (label, must_be_present, must_be_absent)
        ("L1 §10 status K=3", "Bridge-map-scheme suffix discipline (axis β) track: **K=3 MANDATORY**", "### Element 3 status\n\nK=1 at 2026-05-08; advisory until K=3."),
        ("L1 §10 Instance #3", "#### Instance #3 — S93 W9-3 ρ-invariant scheme-INDEPENDENCE on the Pillar-V BdG sector", None),
        ("L1 §10 xref K=3", "**K=3 MANDATORY threshold reached.**", "K=3 MANDATORY threshold pending."),
        ("L2 §8 status pole-distinct K=3", "Pole-distinct criterion: K=3 MANDATORY at 2026-05-24", "SUGGESTION-pending-pole-distinct-K=3 for S89+ entries at NEW substrate-distance poles s ∈ {5, 6, 7, ...}"),
        ("L2 §8 Instance #4", "### Instance #4 — S93 W9-4 closed-form β at the NEW substrate-distance-3 pole s=5", None),
        ("L3A CLOSE banner", "[S93 W9-5 CLOSE — FALSIFIED-at-K=2 → CLOSED, 2026-05-24]", None),
        ("L3A Step5 superseded", "**SUPERSEDED: FALSIFIED-at-K=2 → CLOSED (S93 W9-5; see CLOSE banner above)**", "**Step 5 (direction)**: SUGGESTION at K=2 PRESERVED under REINDEX; calibration corpus"),
        ("L3B Block-B CLOSED", "**Layer-Functor F K=2 SUGGESTION REINDEXED** — **CLOSED at K=2 (S93 W9-5 VERDICT-B", None),
        ("L3C anchor re-scope", "This `α_Mellin = α_zeta = 2.6926237 EXACT` agreement IS a Level-3 record of the **S82 W-3 within-channel F_2-axis FI contour-deformation identity**", None),
    ]
    ok = True
    for label, present, absent in checks:
        if present not in c2 and present not in r2:
            print(f"[VERIFY-FAIL] {label}: expected text NOT found on disk")
            ok = False
        else:
            print(f"[verify-ok ] {label}")
        if absent is not None and (absent in c2 or absent in r2):
            print(f"[VERIFY-FAIL] {label}: stale text STILL present on disk: {absent[:60]!r}")
            ok = False

    corpus_out_sha = hashlib.sha256(c2.encode("utf-8")).hexdigest()      # (local)
    registry_out_sha = hashlib.sha256(r2.encode("utf-8")).hexdigest()    # (local)
    print(f"[post] corpus   sha256={corpus_out_sha}")
    print(f"[post] registry sha256={registry_out_sha}")
    print("ALL-VERIFY-PASS" if ok else "VERIFY-FAILED")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
