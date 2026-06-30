# -*- coding: utf-8 -*-
# (local helper) Single-shot read-modify-write of WP section W6-3 ONLY.
# Anchored between the W6-3 heading and the "## Wave 6 Synthesis" heading so
# sibling sections (W6-1 COMPLETED, W6-2 in progress) are byte-preserved.
# Section content mirrors: plan session-100b-plan-w6.md §W6-3 (method D1-D4,
# substitution chains A/B/C, channel_classes pin, CANONICAL-FORM LAW) +
# the producing-script stdout numbers (run of s100b_leggett_damping_inheritance.py).
from pathlib import Path

WP = Path(__file__).resolve().parents[2] / "sessions" / "session-100b" / "session-100b-w6-workingpaper.md"

START = "### §W6-3. S100b-LEGGETT-DAMPING-INHERITANCE (landau-condensed-matter-theorist)"
END = "## Wave 6 Synthesis (team-lead)"

NEW_SECTION = """### §W6-3. S100b-LEGGETT-DAMPING-INHERITANCE (landau-condensed-matter-theorist)

**Status**: COMPLETED
**Gate ID**: `S100b-LEGGETT-DAMPING-INHERITANCE`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (χ-inheritance transport audit: MgB₂ Leggett damping → substrate DM inter-band-coherence channel; CANONICAL-FORM LAW binds all survival outputs to ratio/inequality form)
**Agent**: `landau-condensed-matter-theorist`
**Hypothesis**: The Yuan MgB₂ Leggett-mode damping, transported through χ : ℂ ⊕ ℍ ⊕ M₃(ℂ) → M₂(ℂ) (M₃(ℂ) → 0), classifies entirely into χ-closed channel classes — pair-breaking continuum (kinematically/Z₂-blocked) and extrinsic bath (no substrate counterpart) — so Γ_grav < H_0 holds and the CONDITIONAL survival ratio τ_DM/t_univ = 1.13e65 stands.
**Plan reference**: `sessions/session-plan/session-100b-plan-w6.md` §W6-3 (PDF-extraction honesty pins, χ morphism pin, 3-class channel set, CANONICAL-FORM LAW, substitution chains A/B/C).

**MCP Pre-Compute Audit**:

| Query | Salient return |
|:------|:---------------|
| `search_knowledge("Leggett damping MgB2 inheritance")` | No prior gate covers the χ-transport audit — NOT PRE-CLOSED. Prior Leggett-damping artifacts are substrate-internal channels (S50/S53/S61); the LEGGETT-DAMPING-50 PASS row carries the historical ω_L = 0.070 / Q = 6.7e5 values. |
| `get_constant("Delta_BCS")` | 0.4642547394830737 (R-PROTECTED; S70 BCS-GAP-CANONICAL-70) — matches plan pin. |
| `get_constant("omega_L1")` | 0.138 (no PROVENANCE entry in knowledge DB; canonical_constants.py:733 is the authoritative import). |
| `get_constant("Mass_LeggettDM_over_Delta_BCS")` | 11.97 (S70 LEGGETT-MOMENT-70; CONDITIONAL on Γ_grav < H_0; pinned S96 W7-2). |
| `get_constant("H_0_inv_s")`, `get_constant("t_universe_s")` | 2.184e-18 s⁻¹; 4.35e17 s (PDG/Planck-class; no PROVENANCE rows). |
| `get_constant("M_KK_inv_seconds")` | 8.860439881925477e-42 s (S96-W1-MKK-SECONDS). |
| `get_constant("Q_Leggett")` | 670000.0 (knowledge DB; see tension (2) below). |
| `get_constant("tau_fold")` | 0.19 (CONST-FREEZE-42) — context only. |
| `trace_entity("LEGGETT-GRAV-DECAY")` | Theorem proven_2046 (CRITICAL conditional: Γ_grav > H_0 ⇒ DM sector collapses); gates -67 (PASS, Γ_grav < H_0), -73a (PASS, τ_DM/t_univ = 1.13e65, Z₂ parity P_L from J-evenness), S95 LEGGETT-GRAV-DECAY-CONDITIONAL (Row #68; Γ_grav/H₀ ≈ 8.85e-66; 65 OOM margin; Ω_DM h² = 0.120 = 0.7σ vs Planck). All plan survival anchors confirmed — this gate re-affirms, it does not re-derive. |

**Provenance tensions recorded** (per the wave's mandatory pre-compute-audit clause; record-only, NOT re-adjudicated): (1) ω_L1 — the atlas-07 LEGGETT-MODE-48 row carries the historical S48 values (ω_L1 = 0.070, Q = 670,000); canonical_constants.py:733 carries the authoritative ω_L1 = 0.138 (imported). (2) Q_Leggett — the plan text asserts "Q_Leggett = 18.6 provenanced S50 LEGGETT-DAMPING-50", but the on-disk canonical_constants.py:2222 carries `Q_Leggett = 6.7e5`, which matches the S50 producing artifact itself (s50_leggett_damping.npz: Q_total = 665595 ≈ 6.7e5, Γ_grav-limited at T = 0; S53/S61 npz also checked, no 18.6 anywhere). The 18.6 figure matches no on-disk artifact — plan-text drift recorded per `substrate-first-canonical-sourcing.md §(ii.B)`; the script imports the on-disk canonical. Q_Leggett is DIAGNOSTIC-only in this gate (formation-epoch comparator); no PASS impact on any clause.

**Verdict**: **PASS** (composite; schema-v2 3-tuple: `sign_verdict=PASS`, `magnitude_verdict=PASS`, `regime_verdict=VALID`; gate-verdicts.md collapse rule applied verbatim and asserted equal to the pre-registered operator conjunction in-script)

4-tuple: `(value=<channel-closure summary>, scheme=CHI-INHERITANCE-TRANSPORT-AUDIT, convention=RATIO, L_max=N/A)`
Dual-SHA: `audit_sha256=cd5b0bc3a037aa68d40cbb85199baa2c4a438c71fa8bae10ef89dfa6c320b573` · `content_sha256=0c6f08b4889acdb178ef3a806ebf7dc223d898e16458c6b7886af34d69673139` (schema_version=S84+). Emitted race-safe via `emit_verdict` — canonical line + dual-SHA companion + 3-tuple row + 4 audit rows (7 rows total).

**Results**:

*D1 — Extraction (as-printed; SHA-pinned PDF `f8f38970…` verified at runtime; all 33 pages read via the Skill(pdf) 4-chunk route)*:

| Element | As-printed value | Source location in arXiv 2412.13830 |
|:--------|:-----------------|:------------------------------------|
| ω_L (observed) | **1.8 THz ± 0.8 THz** — overdamped oscillation; center + error bar by Lorentz fitting of segmented-FFT spectra; "broad peak", softens with T | main text p.4 + p.12; Fig. 3B/3G; p.11 (fit method) |
| ω_L (calculated) | **1.81 ± 0.27 THz** (zero-T) — Eq. (11) ω_L² = (N_σ+N_π)/(N_σN_π) · 4V_σπΔ_σΔ_π/detV with N_σ = 2.04, N_π = 2.78 Ry⁻¹spin⁻¹cell⁻¹, 3 pairing-potential sets (Liu/Choi/Golubov) | SI §XII p.26-27 |
| Δ_π | **0.44 THz** (2Δ_π = 0.88 ± 0.05 THz onset absorption in σ₁ at 2 K) | p.10; SI §XII |
| Δ_σ | **1.32 THz** (empirical Δ_σ ≈ 3Δ_π; 2Δ_σ ≈ 2.64 THz) | p.10; SI §XII |
| Γ_L / linewidth | **No separately-named Γ_L or decay-time constant is printed.** Width-class published number: the ±0.8 THz Lorentz-fit spread of the explicitly "overdamped"/"broad" feature → width-proxy (Γ_L/ω_L)_lab = 0.8/1.8 = 0.444 (derived-from-printed; DIAGNOSTIC only — the PASS predicate never consumes the Γ_L magnitude). Extraction judged COMPLETE on the "Γ_L or linewidth" element with this qualification recorded. | p.11-12; Fig. 3E/3G |
| Mechanism attribution (paper's own) | Mode = Leggett (relative π/σ condensate phase): "over-damped oscillation corresponding to the Leggett mode" (abstract). Damping: "overdamped"/"strongly damped"/"heavily damped"; decay "much faster than that observed in NbN" (Fig. 3E: "Fast-decay Leggett-mode" vs "Persisting Higgs-mode"). Attribution sentence (p.12): "the presence of inter-band coupling between the two superconductivity order parameters changes the spectrum of collective modes and affects their nonlinear responses." Kinematic position fixed by the paper's own printed numbers: ω_L = 1.8 THz > 2Δ_π = 0.88 THz (mode INSIDE the π-band pair-breaking continuum) and < 2Δ_σ = 2.64 THz. Per the paper's own refs [20] (Leggett 1966) + [24] (Blumberg 2007 — the source of its SI Eq. 11), continuum (pair-breaking) decay is OPEN when ω_L > 2Δ_min ⇒ continuum-resonant. UNAMBIGUOUS at channel-class level — the INFO arm does not fire. | abstract; p.11-12; Fig. 3E |

*D2 — Kinematic + protection-layer map (substitution chains A/B executed with substituted numbers)*:

```
Chain A (substrate L1 collective mode):
  x_L1 = ω_L1/(2·Δ_BCS) = 0.138/(2 × 0.4642547394830737)
       = 0.138/0.9285094789661474 = 0.148625   (6 s.f.; plan pin reproduced exactly)
  0.148625 < 1 ⇒ L1 BELOW the pair-breaking edge — quasiparticle channel kinematically CLOSED.

Chain B (substrate DM relic quantum — protection NOT kinematic):
  x_DM = (m_DM/Δ_BCS)/2 = 11.97/2 = 5.985 > 1 ⇒ relic ABOVE the edge
  ⇒ protection = Z₂ parity P_L from J-evenness (LEGGETT-GRAV-DECAY-73a)
    + single-Leggett decay FORBIDDEN (S67, PROVEN) — symmetry selection rule, not kinematics.

Lab (as-printed Yuan values):
  x_lab,π = ω_L/(2Δ_π) = 1.8/0.88 = 2.045455 ≥ 1  (π continuum OPEN — overdamping is continuum-resonant)
  x_lab,σ = ω_L/(2Δ_σ) = 1.8/2.64 = 0.681818      (diagnostic; below the σ edge)
```

The two substrate Leggett-channel objects are NOT conflated (plan D2 law): the THz-driven lab mode is the analog of the L1 mode (kinematically protected, x = 0.148625); the survival claim concerns the relic quantum (symmetry-protected, x = 5.985).

*Chain C — transported-rate edge (class (iii) only)*:

```
m_DM  = 11.97 × 0.4642547394830737 = 5.5571292 M_KK
      = 5.5571292 / 8.860439881925477e-42 s = 6.271844e41 s⁻¹
transport_factor = m_DM/H_0 = 6.271844e41 / 2.184e-18 = 2.871723e59
survival edge (Γ_L/ω_L)_crit = 1/transport_factor = 3.482230e-60
```

Plan 6 s.f. pins (2.87172e59; 3.48222e-60) reproduced from canonical imports; the last-digit wobble on the edge is the plan's rounded-intermediate artifact (within Class-8.3 publication precision; full float64 in the npz).

*D3 — χ-transport audit (pre-registered 3-class classification of every extracted mechanism; χ : ℂ ⊕ ℍ ⊕ M₃(ℂ) → M₂(ℂ), M₃(ℂ) → 0, ker χ = M₃(ℂ) — `inheritance-falsifier-protocol.md` canonical realization + `3HeB-inheritance-canonical.md`)*:

| Channel class | Fired by extraction? | χ-closure for the substrate relic |
|:--------------|:---------------------|:----------------------------------|
| (i) PAIR-BREAKING CONTINUUM | **YES** — the single extracted mechanism (coded rule: x_lab,π = 2.045455 ≥ 1; continuum-resonant overdamping) | **χ-CLOSED on both substrate objects.** L1 mode: kinematic (x_L1 = 0.148625 < 1; the dimensionless continuum position is evaluated per system, and the substrate's is on the protected side of the edge — opposite the lab mode). DM relic quantum: pair-breaking of a single relic quantum requires a Z₂-ODD single-quantum vertex — FORBIDDEN (73a P_L from J-evenness + S67 PROVEN single-Leggett-decay prohibition). |
| (ii) EXTRINSIC BATH | NO — the paper makes no extrinsic (impurity/inhomogeneity/thermal/phonon-bath) attribution for the LEGGETT damping; the p.9 dirty-limit remark concerns the π-band Higgs/THG channel | Would be χ-closed regardless: no substrate counterpart (substrate-IS; no container bath per `phononic-framing.md`). Substrate-internal comparator Q_Leggett (S50, formation-epoch acoustic channel) cited DIAGNOSTIC-only, scoped to the transit/GGE-formation epoch; the relic state is protected by fabric-scale Ordered-Veil integrability (RECONCILED scope: fabric-scale Poisson ⟨r⟩ = 0.367; the retracted single-cell permanence is NOT invoked). |
| (iii) INTRINSIC PARITY-EVEN MULTI-QUANTUM | **EMPTY** — no below-threshold, bath-free, parity-even intrinsic mechanism is proposed anywhere in the paper; structurally, the observed damping operates AT/ABOVE the continuum edge (x ≥ 1) while class (iii) is defined by below-threshold operation | No member transports. The quantitative test is vacuous. Counterfactual diagnostic (NOT fired): IF the lab width-proxy were χ-open, Γ_inherit/H₀ = 0.444 × 2.871723e59 = 1.276e59 ≫ 1 — confirming the pre-registered structural consequence: ANY measurable χ-open lab damping (≳1e-6 of the mode frequency) exceeds the 3.48e-60 edge by ≳54 OOM, so the gate's evidential content IS the channel-closure audit, not the smallness of a transported number. |

*D4 — Survival statement (wave CANONICAL-FORM LAW: ratio/inequality form ONLY)*:

- **Γ_grav < H₀ holds**: Γ_grav/H₀ ≈ 8.85e-66 (S95 LEGGETT-GRAV-DECAY-CONDITIONAL, Row #68; 65 OOM margin).
- **Survival margin ratio**: τ_DM/t_univ = 1.13e65 (LEGGETT-GRAV-DECAY-73a PASS; Z₂ parity P_L from J-evenness).
- **Consistency identity**: H_0_inv_s × t_universe_s = 2.184e-18 × 4.35e17 = 0.950 ~ O(1), and 1/(Γ_grav/H₀) = 1.12994e65 vs τ_DM/t_univ = 1.13e65 — the same statement to O(1), identical at 3 s.f.
- Non-canonical caveat (single pre-authorized sentence): the index's τ_DM = 4.93e82 s is non-canonical — do not propagate.

*Operator conjunction (pre-registered)*: extraction_complete = True ∧ (every extracted mechanism in class (i)/(ii) AND χ-closed) = True ∧ (no transported channel ≥ 1) = True (class-(iii) members: 0) ⇒ operator PASS; collapse-rule composite = PASS (in-script assert: collapse == operator).

*[SIGN] 3-tuple*: sign_verdict = **PASS** (pre-registered direction Chain C Step 5 — the extracted MgB₂ damping attribution lands in class (i)/(ii), expected continuum-resonant or extrinsic: realized as class (i) continuum-resonant); magnitude_verdict = **PASS** (no transported channel ≥ 1; substrate anchor 8.85e-66 ≪ 1); regime_verdict = **VALID** (exact float64 scalar ratio arithmetic on canonical pins; no scan, no expansion regime; the extraction width-proxy qualification is an extraction-precision note, not a regime breach — the PASS predicate never consumes the Γ_L magnitude).

*Cross-checks*: (1) static input SHAs verified at runtime against plan pins (yuan_pdf `f8f38970…` ✓, chi_morphism_canonical `f5a4204a…` ✓; mismatch ⇒ hard abort); (2) plan 6 s.f. pins x_L1 = 0.148625, x_DM = 5.98500, transport 2.87172e59, edge 3.48222e-60 all reproduced from canonical imports; (3) paper-internal ω_L consistency: observed 1.8 ± 0.8 THz vs calculated 1.81 ± 0.27 THz (SI Eq. 11) — mutually consistent; (4) 73a ↔ S95 anchor consistency through H₀t_univ = 0.950 (above); (5) collapse-rule-vs-operator equality asserted.

*Dual-prior discriminator (plan)*: PASS → **0.95 to Track A** (lab Leggett damping is χ-closed for the relic; substrate protections — kinematic for L1, Z₂/J-evenness for the DM quantum — untouched).

**Output Artifacts**:

| Artifact | Path | Content |
|:---------|:-----|:--------|
| Script | `computations/session-100b/s100b_leggett_damping_inheritance.py` | D1-D4 pipeline; chains A/B/C; 3-class audit; dual-SHA; `print_verdict_payload` |
| Data | `computations/session-100b/s100b_leggett_damping_inheritance.npz` | extraction record (as-printed + quotes), kinematic ratios, transport edge, classification JSON, survival anchors, verdict block, full-float64 values |
| Plot | `computations/session-100b/s100b_leggett_damping_inheritance.png` | Panel A: per-system pair-breaking-edge map x = ω/(2Δ) (lab π/σ; substrate L1/DM; edge x = 1); Panel B: χ-transport edge on log axis (lab width-proxy NOT transported vs Γ_grav/H₀ = 8.85e-66 vs edge 3.48e-60) |
| Verdict | `computations/session-100b/s100b_gate_verdicts.txt` | canonical line + dual-SHA companion + schema-v2 3-tuple + 4 audit rows (D1/D3/D4/provenance), emitted via race-safe `emit_verdict` |

**Substrate framing (PHONONIC)**: The framework's dark matter IS a Leggett-channel GGE quasiparticle — an inter-band relative-phase coherence mode of the substrate condensate, CPT-neutral and non-annihilating, with mass anchor 11.97 × Δ_BCS on the BCS gap scale (substrate-IS). MgB₂'s THz-driven Leggett mode is a laboratory-IN shadow: a two-condensate child in which the same relative-phase degree of freedom is driven and its damping measured. Direction of explanation: substrate condensate sectors → inter-band coherence mode (substrate-IS) → χ inheritance morphism (M₃(ℂ) → 0) → two-band laboratory Leggett mode (laboratory-IN). The audit direction never inverts — the lab measurement CONSTRAINS the universality class of decay channels; it does not define the substrate mode. Landau reading: the Leggett mode is the relative-phase Goldstone-class oscillation between two condensate order parameters; its decay channels are classified by symmetry (Z₂ parity from J-evenness) and kinematics (position relative to the 2Δ pair-breaking edge) BEFORE any rate is computed — the three-class transport audit executed here IS that classification, run against the extracted lab attribution. Slot-law compliance: this section makes no quantum-metric claim; the wave's bridge object is §VII.AF.1.OP-PROJ (never §VII.W).

**Assessment**: The first laboratory anchor on the DM-mode lifetime question lands CONSISTENT. MgB₂'s overdamped Leggett mode — the most direct laboratory realization of the substrate's inter-band coherence channel — derives its entire measured damping from a channel class (pair-breaking continuum, continuum-resonant at x_lab = 2.045455) that the χ morphism cannot transport onto the substrate relic: the substrate L1 mode sits at x_L1 = 0.148625, kinematically below its own edge (the opposite side from the lab mode), and the DM relic quantum at x_DM = 5.985 is protected by the Z₂/J-evenness selection rule (single-quantum vertex Z₂-odd, FORBIDDEN per 73a + S67). The lab system exhibits NO universality-class (below-threshold, bath-free, parity-even) decay channel — exactly the class whose existence would have transported through χ and threatened the non-annihilation claim. Constraint-map content: the region "the best available two-band laboratory child exhibits a χ-open inter-band-coherence decay class" is EXCLUDED at the current extraction; the C11 conditional (Leggett-channel DM mass anchor, CONDITIONAL on Γ_grav < H₀) gains a lab-side consistency leg, while the CONDITIONAL tag itself is NOT discharged — this gate cannot discharge it (Element-annotation routed to mack-cosmic-bridge as sole falsifier-surface writer, per the Wave 6 → Wave 7 decision point).

---

"""

text = WP.read_text(encoding="utf-8")
i0 = text.index(START)
i1 = text.index(END)
assert i0 < i1, "anchor order broken"
new_text = text[:i0] + NEW_SECTION + text[i1:]
WP.write_text(new_text, encoding="utf-8")
print("WP W6-3 section written:", WP)
print("old-span chars:", i1 - i0, "-> new-span chars:", len(NEW_SECTION))
