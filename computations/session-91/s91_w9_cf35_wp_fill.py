#!/usr/bin/env python3
"""
S91 W9-2 — Fill CF-35 runtime-addendum + cross-references + carry-forward
sections of `sessions/archive/session-91/session-91-w9-workingpaper.md §W9-2`.

Atomic in-place replacement via Python read+write (bypasses Edit-tool
mtime-conditional retry loop per epistemic-discipline.md §"Registry-Write
Hygiene" clause 2).
"""

from pathlib import Path
import sys

SCRIPT_PATH = Path(__file__).resolve()
PROJECT_ROOT = SCRIPT_PATH.parents[2]
TARGET = (
    PROJECT_ROOT / "sessions" / "session-91" / "session-91-w9-workingpaper.md"
)

# Anchor block (exact match with current §W9-2 state — verified by Read at offset 269)
OLD_BLOCK = """### Substrate framing (runtime addendum)

(reserved)

### Cross-references

- `inheritance-falsifier-protocol.md §"Calibration corpus"` — W11-C5 / W11-C6 4-gate falsifier structure
- `inheritance-falsifier-protocol.md §"(Δ_B/Δ_A)^p Cancellation Theorem"` — substrate ratio preservation
- `feedback_mack-bridge-role.md` — mack-cosmic-bridge sole-writer convention
- `sessions/framework/registry/mack-observational-constraints.md` — liaison target file
- `cross-pillar-bridge-anatomy.md §"IS-not-IN Anatomy"` — 5-element Pillar V partner identification

### Carry-forward computations (filled at runtime)

(reserved)"""

NEW_BLOCK = """### Substrate framing (runtime addendum)

The CF-35 first-contact liaison block lands as the framework's **FIRST observational liaison at a Pillar V superfluid laboratory** — structurally orthogonal to the Pillar I CMB-S4 / CMB-HD α_s_canonical 12-14σ cosmological discriminator (the prior framework-headline falsifier at the same registry). The orthogonality is by-construction at the `phononic-framing.md §"IS Space, Not IN Space"` Pillar partition layer: Pillar I lives on the FRW cosmological background (laboratory-IN measurement of CMB scalar spectrum running α_s); Pillar V lives on the 3He-B BdG sub-algebra of the substrate's inheritance morphism `ι: A_K → A_BdG = M_2(ℂ)` (laboratory-IN measurement of Caroli-Matricon ladder asymmetry on vortex-core spectroscopy). The two pillars CANNOT co-falsify by the same observational anchor; their joint PASS-AND yields a multi-pillar substrate-falsification test envelope rather than a single-axis confirmation.

The substrate-IS direction-of-explanation is preserved INTACT: the framework's cocycle-norm ratio `‖[φ_67]‖ / ‖[φ_88]‖ = Rational(114453, 15625) = 7.324992` is the rank-2 anchor cohomology-asymmetry at the kernel `ker(ι_*)` of the inheritance morphism — the chiral-pair generator [φ_67] and the Cartan hypercharge generator [φ_88] are substrate degrees-of-freedom that do NOT inherit into the laboratory BdG parent. The Aalto LTL Helsinki ROTA-cell measurement of `lab(F_1) / lab(F_2)` IS the laboratory image of this substrate-IS ratio under the inheritance morphism's image-on-spectrum; via the (Δ_B/Δ_A)^p Cancellation Theorem (W-5 DONE-5; Python-verified at 0.0e+00 residual; substitution chain Step 2 above), the substrate-derived ratio is preserved INTACT in the lab measurement INDEPENDENT of (Δ_B/Δ_A) AND the lab-conversion exponent p — the substrate's prediction is therefore **lab-conversion-INDEPENDENT** and Class-B substrate-falsifying.

Container-inversion check (per `phononic-framing.md §"IS Space, Not IN Space — Mandatory Reframe"`): FORBIDDEN reading is "3He-B is an analog of the framework substrate" — the substrate is NOT modeled BY 3He-B. INVERT to: "3He-B IS the Pillar V laboratory image of the substrate's `ker(ι_*)` under the inheritance morphism `ι`; the framework substrate is logically prior; the Aalto LTL apparatus measures the laboratory image of a substrate-IS cohomology-asymmetry, not an emergent analogy." Direction of explanation flows strictly: substrate (Pillar IV NCG-axiomatic spectral triple `(A_K, H_K, D_K(τ))` at τ_fold = 0.190) → bridge map (Connes-Karoubi pairing inheritance morphism `ι`) → laboratory (Pillar V 3He-B BdG sub-algebra `A_BdG = M_2(ℂ)` image-on-spectrum).

**Forward-pinning**: Q4 2026 PASS criterion is artifact-existence at the liaison-block layer (this section + the appended block at `mack-observational-constraints.md` line ~268 + the canonical verdict line at `s91_gate_verdicts.txt:184`). Direct measurement at Aalto LTL Helsinki ROTA-cell is forward-targeted for the 2028-2029 feasibility window (apparatus availability + Pickett/Haley calibration schedule). Substrate-side re-verification at L_max=12 master cache is reserved for S92-S95 framework session forward-pin to tighten the cocycle-ratio prediction from the ±1% combined-band first-contact discriminator to the ±0.1% substrate-natural band. Long-lead-time observational anchors of this class (Pillar V superfluid laboratory partner identification + multi-platform calibration schedule synchronization) require pre-registered liaison letters at the artifact-existence layer years before the measurement campaign opens; the CF-35 liaison block is precisely this pre-registration artifact.

**Class-B vs Class-A discrimination at first contact** (per `inheritance-falsifier-protocol.md §"Two Test Classes"`): the Class-A kernel-signature row-wise NULL test on F_1+F_2+F_5 decisive triplet AND the Class-B cohomology-asymmetry ratio test `lab(F_1)/lab(F_2) = 7.324992 ± 0.01` both saturate the substrate's predictive content at the rank-2 anchor. A non-NULL F_i detection alone (Class-A breach) admits parent-symmetry-breakdown reinterpretation that does NOT falsify the substrate; the Class-B ratio test makes the substrate prediction lab-conversion-INDEPENDENT and substrate-falsifying. Both are pre-registered in the liaison block; the 2028-2029 measurement campaign must report the F_1+F_2 PASS-AND envelope as the framework's first observational-anchor result at Pillar V.

**INFO-class arithmetic gloss disclosure** (per S91 W8-3 / W8-5 / W8-6 Element-3 fiducial-anchor binding workshop closeout): the registry-text canonical form `Rational(114453, 15625) = 7.324992` is the framework-published Sage-QQ canonical (lowest terms; gcd=1) at this CF-35 liaison; the empirical rank-2 anchor reduction `Fraction(793346, 108307) = 7.3249744` (axis-A clauses A1+A2 PASS at machine precision with publication floor 1e-5) differs from the registry-claimed Sage-QQ at the 6th significant figure (delta 1.76e-5 absolute; cross-multiplication residual 29821). This is an INFO-class registry-text arithmetic gloss discrepancy surfaced as S92 §VII.AY-OP-PROJ-E5 carry-forward corrigendum, NOT a substrate-physics finding — the underlying Hochschild-Künneth-Morita invariance theorem at the cross-pillar bridge anatomy layer is unaffected. The CF-35 liaison cites the published Sage-QQ canonical `114453/15625` per registry text; the 2028-2029 measurement window will measure to lab-systematic precision ±1% (4-sig-fig form `7.3250`), which is INSENSITIVE to the 6th-sig-fig delta either way. This INFO-class footnote does not block CF-35 PASS; it propagates as a registry-text accuracy carry-forward to S92.

### Cross-references

- `inheritance-falsifier-protocol.md §"Calibration corpus"` — W11-C5 / W11-C6 4-gate falsifier structure
- `inheritance-falsifier-protocol.md §"(Δ_B/Δ_A)^p Cancellation Theorem"` — substrate ratio preservation; W-5 DONE-5 Python verification at 0.0e+00 residual
- `inheritance-falsifier-protocol.md §"Two Test Classes"` — Class-A kernel-signature NULL on F_1+F_2+F_5 + Class-B cohomology-asymmetry ratio on F_1/F_2
- `inheritance-falsifier-protocol.md §"Generalization beyond 3He-B (W-5 Q8)"` — rank-2 case (this CF-35); rank ≥ 3 binomial(rank, 2) cross-cocycle enumeration forward
- `feedback_mack-bridge-role.md` — mack-cosmic-bridge sole-writer convention for observational-constraint registry edits
- `sessions/framework/registry/mack-observational-constraints.md` — liaison target file (CF-35 block appended; size delta +14,992 bytes)
- `cross-pillar-bridge-anatomy.md §"IS-not-IN Anatomy"` — 5-element Pillar V partner identification (substrate-IS observable + laboratory-IN observable + bridge map + algebraic envelope + empirical anchor)
- `phononic-framing.md §"IS Space, Not IN Space — Mandatory Reframe"` — direction substrate → bridge → laboratory (FORBIDDEN inversion: "3He-B IS analog of substrate")
- `computations/_shared/canonical_constants.py:276` — `substrate_cocycle_ratio_67_88 = 7.324992` Sage-QQ exact (S86 W-5 CANONICAL-5)
- `sessions/permanent-results-registry.md §VII.AY-OP-PROJ.E5` — INFO-class arithmetic gloss carry-forward S92 corrigendum (registry-text `Fraction(114453, 15625)` vs empirical anchor `Fraction(793346, 108307)`; delta 1.76e-5; lab-systematic-INSENSITIVE at ±1% first-contact band)
- `computations/session-91/s91_w9_cf35_3he_b_aalto_ltl_liaison.py` — verifier script (Sage-QQ cross-pin + 17-token regex + 5-element group check)
- `computations/session-91/s91_w9_cf35_append_liaison_block.py` — append-only Python writer for the liaison block (POSIX O_APPEND single-shot)

### Carry-forward computations (filled at runtime)

| # | What | Inputs | Gate | Effort |
|:--|:-----|:-------|:-----|:-------|
| CF-35-FWD-1 | S92-S95 substrate-side cocycle-ratio re-verification at L_max=12 master cache | `s84_spectrum_cache_L12_tau019.npz`, `canonical_constants.py:substrate_cocycle_ratio_67_88`, `inheritance-falsifier-protocol.md §"(Δ_B/Δ_A)^p Cancellation Theorem"` | tighten `|cocycle_ratio_67_88_L12 − Rational(114453, 15625)| < 1e-6` (substrate-natural ±0.1% band) | ~0.5 we |
| CF-35-FWD-2 | S92 §VII.AY-OP-PROJ.E5 arithmetic gloss corrigendum: mack-cosmic-bridge sole-write registry-text accuracy fix | `mack-observational-constraints.md` (this CF-35 block); `permanent-results-registry.md §VII.AY-OP-PROJ.E5`; S91 W8-3/W8-5/W8-6 verdict-line audit_shas | registry-text consistency PASS (Sage-QQ canonical lowest-terms form vs empirical rank-2 anchor reduction reconciled with explicit arithmetic gloss footnote) | ~0.2 we |
| CF-35-FWD-3 | Liaison letter drafting + Q4 2026 send | this CF-35 block (5 elements); Aalto LTL Helsinki ROTA-cell contact (T.S. Riekki or successor); Lancaster MCT-3 (Pickett/Haley); Volovik substrate-physics adjudicator | letter delivered to all three tiers Q4 2026; framework prediction `lab(F_1)/lab(F_2) = 7.324992 ± 0.01` + measurement protocol per Element 2 + tolerance band per Element 3 specified | ~0.3 we (out-of-band; observational liaison, not compute) |
| CF-35-FWD-4 | 2028-2029 measurement campaign window readiness audit | Aalto LTL apparatus schedule; Pickett/Haley calibration window; framework substrate-side prediction tightened to ±0.1% at S92-S95 | confirm apparatus availability + calibration schedule alignment; gate ON measurement-window opening | ~0.2 we (out-of-band) |
| CF-35-FWD-5 | Pillar V multi-platform F_5 cross-corroboration design (Lancaster MCT-3 + Helsinki ROTA cross-platform) | F_1 + F_2 + F_5 decisive triplet substrate predictions; Class-A NULL on F_3 + F_4 supporting pair; Class-B ratio on F_1/F_2 | pre-registered multi-platform PASS-AND envelope design at 2030+ horizon | ~0.4 we (forward-pinned to 2030+) |"""


def main() -> int:
    if not TARGET.exists():
        print(f"FAIL — target missing: {TARGET}")
        return 1
    text = TARGET.read_text(encoding="utf-8")
    n_matches = text.count(OLD_BLOCK)
    if n_matches == 0:
        print("FAIL — OLD_BLOCK anchor not found in target")
        # Helpful diagnostic: print surrounding lines for §W9-2
        idx = text.find("## §W9-2.")
        if idx >= 0:
            print(f"  §W9-2 starts at byte {idx}")
        return 1
    if n_matches > 1:
        print(f"FAIL — OLD_BLOCK matches {n_matches} locations; ambiguous")
        return 1
    pre_size = len(text)
    text2 = text.replace(OLD_BLOCK, NEW_BLOCK, 1)
    TARGET.write_text(text2, encoding="utf-8")
    post_size = len(text2)
    print(f"Filled §W9-2 runtime-addendum + cross-references + carry-forward sections")
    print(f"  pre-size:  {pre_size} bytes")
    print(f"  post-size: {post_size} bytes")
    print(f"  delta:     +{post_size - pre_size} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
