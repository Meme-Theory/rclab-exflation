#!/usr/bin/env python3
"""One-shot WP section writer for S100a-W1-4 (landau). Replaces ONLY the
SS W1-4 section (anchor '### §W1-4.' .. next '---' before SS Synthesis) in
sessions/session-100a/session-100a-w1-workingpaper.md. Single read-modify-write
to minimize the concurrent-writer window (other W1 agents own other sections).
"""
import io, sys
from pathlib import Path

WP = Path(r"C:\sandbox\Ainulindale Exflation\sessions\session-100a\session-100a-w1-workingpaper.md")

NEW_SECTION = """### §W1-4. S100a-W1-4-SIGMA-DM-NUCLEON (landau-condensed-matter-theorist)

**Status**: COMPLETED
**Gate ID**: `S100a-W1-4-SIGMA-DM-NUCLEON`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC**
**Agent**: `landau-condensed-matter-theorist`
**Hypothesis**: The spin-independent DM-nucleon cross-section σ_SI of the Leggett-channel GGE quasiparticle (mass `M_DM = 11.97·Δ_BCS·M_KK`) lies below the LZ/XENONnT exclusion at that mass and at/below the neutrino fog — a falsifiable-but-currently-unexcluded direct-detection prediction consistent with the collisionless σ/m anchor.
**Plan reference**: `sessions/session-plan/session-100a-plan-w1.md` §W1-4 (closed-form M_DM + σ_SI from Leggett-channel constants, LZ-2024 exclusion digitization, laboratory-vs-substrate rest-energy frame resolution; mack-cosmic-bridge writes any falsifier-inventory row).

**Verdict**: **PASS** — σ_SI(M_DM) = 1.30e-63 cm² sits **30.92 OOM below** the LZ-2024 exclusion and **30.02 OOM below** the xenon neutrino fog at M_DM = 4.13e17 GeV. Schema-v2 3-tuple: `sign_verdict=PASS` (sign(σ_excl − σ_SI) = +1, the pre-registered PASS direction), `magnitude_verdict=PASS` (σ_SI ≤ σ_νfog — at/below the fog), `regime_verdict=VALID` (frame resolved: Frame A binds; verdict frame-robust; flux-floor and Born-regime checks VALID). Composite per the pre-registered collapse rule: PASS.

**Results**:

4-tuple: `(value=sigma_SI=1.299e-63_cm2_at_M_DM=4.128e+17_GeV(FrameA-substrate-anchor-binds);..., scheme=FW, convention=LEGGETT-CHANNEL-SUBSTRATE-COUPLING, L_max=N/A)`

| Quantity | Value | Provenance |
|:---------|:------|:-----------|
| M_DM (substrate units) | 5.5571 M_KK = 11.97 × Δ_BCS | `Mass_LeggettDM_over_Delta_BCS=11.97` (LEGGETT-MOMENT-70) × `Delta_BCS=0.4642547394830737` (BCS-GAP-CANONICAL-70, R-protected) |
| M_DM laboratory rest energy (Frame A, **binds**) | **4.128202e17 GeV** (3 sf: 4.13e17) | × `M_KK=7.428660036284456e16` GeV (CONST-FREEZE-42) |
| σ_SI per nucleon (canonical) | **1.298925e-63 cm²** (3 sf: 1.30e-63) | pure gravitational vertex α_A = G_N M_DM m_Xe = 3.387e-19; full float64 in npz |
| σ_A(Xe, >E_th) | 3.729e-55 cm² | Rutherford recoil spectrum, E_th = 5 keV, v = 1.1e-3 c |
| σ_excl^LZ(M_DM) | 1.073e-32 cm² | digitized LZ-2024 curve, iso-rate σ ∝ M extrapolation beyond 1e4 GeV |
| σ_νfog(M_DM) | 1.362e-33 cm² | digitized Xe n=2 fog (O'Hare 2021), same extrapolation |
| Margin below exclusion / fog | 30.92 / 30.02 OOM | sign(σ_excl − σ_SI) = +1 |
| DM-DM σ_T/m at Bullet v | 1.688e-53 cm²/g ≤ anchor 5.7e-51 | CC1, `sigma_over_m` (S42, promoted to canonical_constants this gate) |

**Substitution chain** (sign claim, math-scripts.md; substituted numbers):

```
Claim: sigma_SI(M_DM) < sigma_excl^LZ(M_DM)
Step 1: M_DM = Mass_LeggettDM_over_Delta_BCS * Delta_BCS * M_KK
             = 11.97 * 0.4642547394830737 * 7.428660036284456e16 GeV
             = 4.128202e17 GeV                       [Frame A binds; see resolution below]
Step 2: alpha_A = G_N * M_DM * m_Xe = (1/M_Pl^2) M_DM m_Xe
              = 6.7087e-39 * 4.1282e17 * 122.295 = 3.3870e-19   [pure gravitational vertex]
Step 3: sigma_A(>E_th) = (2 pi alpha_A^2/(m_Xe v^2))(1/E_th - 1/E_max)
              = 3.7291e-55 cm^2     [E_max = 2 mu_A^2 v^2/m_Xe = 296 keV; E_th = 5 keV]
Step 4: sigma_SI = sigma_A / [A^2 (mu_A/mu_n)^2 (1 - E_th/E_max)] = 1.2989e-63 cm^2
              [equal-above-threshold-rate contact-SI per-nucleon normalization
               = the axis the LZ curve is published on]
Step 5: sigma_excl^LZ(M_DM) = sigma_excl(1e4 GeV) * (M_DM/1e4) = 1.0733e-32 cm^2
              [iso-rate scaling exact at M >> m_A: rate ~ (rho/M) sigma]
Step 6: sign(sigma_excl - sigma_SI) = sign(1.073e-32 - 1.299e-63) = +1
        => BELOW exclusion (PASS direction), 30.92 OOM margin; 30.02 OOM below fog.
```

**Laboratory-frame vs substrate-M_KK-scale rest-energy resolution (Def 1 core — FRAME A BINDS)**:

- **Frame A (BINDS)**: M_DM^lab = 11.97·Δ_BCS·M_KK = 4.128e17 GeV — the substrate anchor read through the framework's **single unit map**. Three independent arguments: (i) the spectral triple converts M_KK units to GeV exactly once, via the a_2/G_N gravity bridge (CONST-FREEZE-42); every GeV-valued framework observable (KK tower, m_H threshold corrections, v_ew) uses this one conversion — a mode-specific second conversion does not exist in the spectral triple and introducing one would un-pin every PROVEN GeV-valued result. (ii) The Leggett mode is a **gapped quasiparticle**: emergent-4D dispersion ω²(k) = ω₀² + c²k² with ħω₀ = 11.97·Δ_BCS·M_KK; by the Landau quasiparticle correspondence (E² = (mc²)² + (cp)²) the laboratory rest energy IS ħω₀ — rest energy is frame-invariant, the relic is comoving (T^{0i}_4D = 0 exact, atlas-04 C7), and the laboratory moves at only v ~ 1e-3 c relative to it. (iii) GGE bookkeeping: the Parker-pair relic energy budget is fixed in M_KK units; rescaling the per-quantum mass by ~17 OOM without rescaling number density would break the Ω_DM closure by the same ~17 OOM.
- **Frame B (EXCLUDED reading)**: the gap-scale anchor misread as a laboratory-GeV rest energy, M_DM = 5.557 GeV. Computed anyway for frame-robustness: at 5.557 GeV the gravitational σ_SI(>E_th) is a **kinematic null** (E_max = 0.559 keV < E_th = 5 keV; an above-threshold Xe recoil requires v = 3.29e-3 c > the SHM ceiling 2.6e-3 c), i.e. trivially below exclusion as well. **The sign verdict is frame-robust** — the regime_verdict=VALID rests on the structural resolution (i)–(iii), not on the frame choice.

**Coupling-channel derivation (symmetry first — why σ_SI is the pure gravitational floor)**: (1) D_K is block-diagonal (S22b PERMANENT): inter-sector matrix elements vanish identically — no direct Dirac vertex between the BCS-sector coherence mode and SM zero modes. (2) V(gap,gap) = 0 EXACTLY (S23a selection rule) and B1 couples only to B2 (S34 Trap 1) — no cubic vertex routes inter-band coherence into SM channels. (3) The Leggett mode is a CPT-neutral gauge singlet; the relative-phase mode couples to band-density *differences*, so its linear coupling to total-mass-density probes vanishes — the leading surviving coupling is quadratic through the stress tensor. (4) Two-layer architecture (S72 PERMANENT): the BCS sector communicates with the spectral sector only through the metric moments (a_2 = gravity). Therefore α = G_N M_DM m_N with **zero free parameters** — the same coupling class as the S42/S44 collisionless anchor, which is itself the gravitational Rutherford transport cross-section (s44_cdm_construct.py: σ_T = 4π(G_N m)²/v⁴·lnΛ). Born validity: α_A/v = 3.1e-16 ≪ 1 (CC4 VALID). Helm form factor at threshold (qR_Xe ≈ 0.85) is O(1) — immaterial at ≥30-OOM margins, as is any alternative threshold/velocity convention (≤ few OOM).

**Cross-checks** (all PASS):
- **CC1 (σ/m anchor bounds the coupling)**: DM-DM gravitational transport at Bullet-Cluster velocity, σ_T/m = 1.688e-53 cm²/g ≤ anchor `sigma_over_m` = 5.7e-51 cm²/g — CONSISTENT (factor ~340 inside the bound; same zero-free-parameter G_N² class).
- **CC2 (independent event-rate route)**: N_transit(LZ exposure) = 12.1; P(>E_th scatter)/crossing = 7.24e-31; predicted events = 8.78e-30; event-route margin = 29.61 OOM vs curve-route 30.92 OOM; |diff| = 1.30 OOM ≤ 2.0 — the two independent comparison routes AGREE (residual bundles detector geometry/efficiency conventions).
- **CC3 (flux floor)**: 12.1 DM transits through LZ during WS2022+WS2024 — the iso-rate σ ∝ M extrapolation is inside its validity domain at M_DM (it evaporates only at M ≳ 1e19 GeV where fewer than one particle crosses).
- **CC4 (Born regime)**: α_A/v = 3.08e-16 ≪ 1 — deep Born regime, Rutherford form valid.

**Methodology notes (empirical-input digitization)**: `s100a_lz2024_si_exclusion.csv` digitized by this gate from the published LZ-2024 SI limit — LZ collaboration, arXiv:2410.17036, Fig. 6 (WS2022+WS2024 combined, 90% CL observed); published anchor exact: minimum 2.2e-48 cm² at 40 GeV (abstract); 24 points 9 GeV–1e4 GeV at ±0.15 dex figure-read fidelity. Xenon neutrino-fog n=2 boundary digitized from O'Hare, PRL 127, 251802 (2021) + the LZ-2024 plotted boundary (14 points, ±0.3 dex). Both are METHODOLOGICAL empirical cross-check inputs per substrate-first-canonical-sourcing §(i) (citation given; no substrate canonical replaced). Beyond 1e4 GeV both curves are extrapolated linearly in M (iso-rate scaling, exact for M ≫ m_A since rate ∝ (ρ/M)·σ with mass-independent kinematics); digitization fidelity is immaterial against ≥30-OOM margins. Curve interpolation: log-log, well inside the 1e-3 log10(σ) tolerance pin.

**Canonical write-order (executed)**: (1) verdict line emitted via `emit_verdict` (race-safe MCP; canonical line + dual-SHA companion + schema-v2 3-tuple row + frame-resolution companion row in `computations/session-100a/s100a_gate_verdicts.txt`); (2) `sigma_DM_nucleon_FW = 1.2989252548383697e-63` (cm²) and `M_DM_Leggett_GeV = 4.128202383934713e17` promoted to `canonical_constants.py` SECTION E via `update_constant` (session=S100a, source=S100a-W1-4-SIGMA-DM-NUCLEON; both inherit the C7/LEGGETT-MOMENT-70 conditionality Γ_grav < H_0); `sigma_over_m = 5.7e-51` cm²/g (S42 provenance) was promoted to module level pre-compute (it existed only in the audit allowlist). (3) Falsifier-master-inventory row: NOT this gate's — routes to mack-cosmic-bridge (sole writer) at session close.

**Substrate framing**: PHONONIC. Dark matter IS a Leggett-channel GGE quasiparticle — an inter-band coherence mode of the (0,0) BdG sector of D_K, CPT-neutral and non-annihilating. The arrow flows D_K eigenvalues → BdG gap Δ_BCS → Leggett inter-band coherence mode → DM rest mass (11.97·Δ_BCS·M_KK through the one a_2/G_N unit map) → nucleon coupling (gravitational floor, the only inter-sector channel) → σ_SI. A laboratory direct-detection experiment is substrate probing substrate: the coherence mode perturbing a nucleon fiber's eigenvalue spectrum — and the substrate says that perturbation is mediated by the a_2 moment alone. **Constraint-map reading**: the framework predicts a direct-detection NULL at every current and projected experiment (30 OOM below the fog); the falsifier INVERTS — any confirmed DM-nucleon scattering above the gravitational floor falsifies the Leggett-channel DM identity outright. This is a sharp, zero-free-parameter, pre-registered discriminator; per the plan's pre-registered dual-prior discriminator, the PASS outcome routes to Track A (suppressed nucleon coupling consistent with the collisionless anchor). What remains uncomputed: nothing within this gate; the observational row lands via mack-cosmic-bridge.

**Output Artifacts**:
- `computations/session-100a/s100a_w1_sigma_dm_nucleon.py` — producing script (`from canonical_constants import *`, `print_verdict_payload`); exit 0
- `computations/session-100a/s100a_w1_sigma_dm_nucleon.npz` — full-float64 results (masses both frames, σ_SI, curves, margins, CC1–CC4, machinery pins)
- `computations/session-100a/s100a_w1_sigma_dm_nucleon.png` — (M, σ_SI) plane: LZ-2024 curve + iso-rate extrapolation, fog boundary + shaded fog region, Frame-A point (star), Frame-B dotted line
- `computations/session-100a/s100a_lz2024_si_exclusion.csv` — LZ-2024 digitization (header carries source + fidelity + date)
- Verdict line: `S100a-W1-4-SIGMA-DM-NUCLEON: PASS ...` in `computations/session-100a/s100a_gate_verdicts.txt`; `audit_sha256=206a7453699145089f96d07ca56298cf951926dcfc3c39a10b373e0f96b8a444`, `content_sha256=16da18e9adbb9cec1fc1783f3d46d80ae55f1f45d07659343889b25a6c5a150c`; dual-SHA companion + 3-tuple (`sign=PASS magnitude=PASS regime=VALID`) + frame-resolution rows present

**MCP Pre-Compute Audit**:
- `search_knowledge("Leggett DM nucleon cross-section direct detection sigma_SI")` — no prior σ_SI(DM-nucleon) gate exists; nearest hits are abundance gates (LEGGETT-DM-ABUND-60 FAIL lineage) and the C7 conditional anchor — gate NOT pre-closed.
- `search_knowledge("sigma_over_m collisionless self-interaction 5.7e-51")` — atlas-04 C7 + atlas-07 row "[NEW S42] sigma/m (CDM) = 5.7e-51 cm²/g Computed" confirm the anchor's provenance.
- `search_knowledge("neutrino fog LZ XENONnT exclusion direct detection")` — no prior LZ digitization in the corpus; CSV creation confirmed as this gate's first step.
- `get_constant("Mass_LeggettDM_over_Delta_BCS")` = 11.97 (LEGGETT-MOMENT-70; CONDITIONAL Γ_grav < H_0) — matches plan pin.
- `get_constant("Delta_BCS")` = 0.4642547394830737 (R-protected) — matches plan pin.
- `get_constant("M_KK")` = 7.428660036284456e16 GeV (CONST-FREEZE-42) — matches plan pin.
- `get_constant("sigma_over_m")` — NOT FOUND at module level (allowlist-only); promoted to `canonical_constants.py` SECTION E with S42 provenance BEFORE compute (math-scripts.md mandate), then imported.
- `trace_entity("DIRECT-58")` — resolves to EPSILON-DIRECT-58 (effacement gate, unrelated) — confirms no prior direct-detection σ computation. Structural priors retrieved: V(gap,gap)=0 EXACT (S23a), single-Leggett gravitational decay FORBIDDEN (S67), T^{0i}_4D=0 exact (C7).

---
"""

def main() -> int:
    text = WP.read_text(encoding="utf-8")
    start_anchor = "### §W1-4. S100a-W1-4-SIGMA-DM-NUCLEON"
    end_anchor = "## Wave 1 Synthesis"
    i = text.find(start_anchor)
    j = text.find(end_anchor)
    if i < 0 or j < 0 or j <= i:
        print(f"ANCHOR FAILURE: start={i} end={j}; aborting without write")
        return 1
    new_text = text[:i] + NEW_SECTION + "\n" + text[j:]
    WP.write_text(new_text, encoding="utf-8")
    print(f"WP section §W1-4 replaced: [{i}:{j}] -> {len(NEW_SECTION)} chars; file now {len(new_text)} chars")
    return 0

if __name__ == "__main__":
    sys.exit(main())
