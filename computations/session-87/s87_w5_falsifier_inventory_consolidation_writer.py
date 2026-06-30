"""
S87 W5-2 + W5-3 + FWD-C1/C2/C3 inventory consolidation — one-shot append-only writer.

Author: mack-cosmic-bridge (sole writer per feedback_mack-bridge-role.md).
Source: sessions/archive/session-87/session-87-results-workingpaper.md §W5-2 (lines 4411-4512),
        §W5-3 (lines 4514-4602), §W11-5 (lines 9398-9580), §W6-1 (lines 4822-4868).

Per .claude/rules/epistemic-discipline.md §"Registry-Write Hygiene under Parallel-Writer Race":
this is an append-only Python writer (open mode "a"), NOT an Edit-tool round-trip — so it
avoids mtime conflicts under parallel workshop landings on the shared registry.

DOES NOT modify any file except sessions/framework/registry/falsifier-master-inventory.md.

Substrate framing (per phononic-framing.md §"IS Space, Not IN Space"):
the substrate IS the rank-2 cocycle pair ([φ_67], [φ_88]) in ker(ι_*) of the inheritance
morphism ι : (A_K, H_K, D_K) → 3He-{B,A} BdG sector. The substrate cohomology-class pairing
on the Jensen-deformed band-0 projector at τ_fold=0.190 IS the source of the 7.324992 ratio.
Lab-platform lab-IN measurements probe the substrate's signature; container-thinking inversion
is FORBIDDEN.
"""

from pathlib import Path
import sys

# Tier0 canonical-constants import per .claude/rules/math-scripts.md
# (this writer doesn't compute physics, but the discipline applies to all S34+ scripts).
from canonical_constants import *  # noqa: F401,F403

# Resolve project root (script lives in computations/_shared/, project root is parent).
PROJECT_ROOT = Path(__file__).resolve().parent.parent  # (local)
INVENTORY = PROJECT_ROOT / "sessions" / "framework" / "registry" / "falsifier-master-inventory.md"  # (local)

# Append-only payload. Built as a single string with explicit row IDs.
PAYLOAD = """

## NEW Rows #47--#51 -- 3He-B B-phase 4-gate falsifier protocol (S87 W5-2 LAB-FALSIFIER-A class)

> **Origin**: S87 W5-2 `S87-W11-C5-LAB-FALSIFIER` (volovik-superfluid-universe-theorist PRIMARY; connes-ncg-theorist co-signer; mack-cosmic-bridge sole writer of this section per `feedback_mack-bridge-role.md`). Verdict line `S87-W11-C5-LAB-FALSIFIER: PASS -- value=7.324992 scheme=Sage-exact-zeta-regulated-Hochschild-pairing-cancellation-theorem convention=3He-B-BDI-vortex-core-Caroli-Matricon L_max=10 audit_sha256=d40a8d26588a0d207ddb6adaad1f26149512e940c659ade32766054d33031a8b content_sha256=29b76a1a1eab56da55725a46af872e097934eef5d5327e5d6d36086fa9bf3469 schema_version=S87+` (`computations/session-87/s87_gate_verdicts.txt:176`).
> **Substrate framing (PHONONIC)**: each row is a substrate excitation channel in ker(ι_*) inheriting through χ : ℂ⊕ℍ⊕M_3(ℂ) → M_2(ℂ) (M_3(ℂ) → 0) into the 3He-B BdG sector at the Lancaster MCT-3 / Helsinki ROTA / RHUL labs. The substrate IS the rank-2 cocycle pair ([φ_67], [φ_88]); 3He-B is the BDI-protected child realization. Lab platforms probe the substrate's signature; container-thinking inversion is FORBIDDEN per `phononic-framing.md` §"IS Space, Not IN Space".
> **Inheritance protocol**: `.claude/rules/inheritance-falsifier-protocol.md` §"Four-Gate Structure"; W-5 W11-C5 calibration corpus (B-phase decisive triplet F1+F2+F5 + supporting F3+F4 + cocycle-degenerate Gate-4 multi-pressure slope discrimination).
> **(Δ_B/Δ_A)^p cancellation theorem**: Common p=2 for F1 (NMR longitudinal Δ²) and F5 (acoustic-mode Bogoliubov Δ²); cancellation operationally verified at 0.0e+00 Python residual per S86 W-5 DONE-5; substrate-derived ratio 7.324992 PRESERVED INTACT under any (Δ_B, Δ_A) values OR p choice.
> **EVOI tier**: LAB-FALSIFIER-A (decisive); 5-yr horizon = Lancaster MCT-3 / Helsinki ROTA / RHUL 2027-2030.
> **Cross-pillar bridge anatomy**: `.claude/rules/cross-pillar-bridge-anatomy.md` 5-element IS-not-IN + 3-level ladder declared at the cross-pillar §VII.AF.1 + §VII.AG.1 LANDED bridge entries.

| # | Observable | Falsifier function | Channel(s) | Prediction value(s) | Live-watch envelope | Internal-consistency split | Detector / horizon | scheme | convention | L_max | content_sha256 | audit_sha256 | notes |
|:-:|:-----------|:-------------------|:-----------|:--------------------|:--------------------|:----------------------------|:--------------------|:-------|:-----------|:------|:----------------|:--------------|:------|
| 47 | F1 Caroli-Matricon ladder asymmetry (B-phase decisive; φ_67 chiral-pair clean) | inheritance-morphism Class-A Gate-1 NULL kernel-signature falsifier | Lancaster MCT-3 vortex-core spectroscopy (PRIMARY); Pickett-group dilution-fridge sub-gap NMR-tipping | NULL on F1 substrate margin 0.573193 M_KK² (Hochschild pairing on Jensen-deformed band-0 projector at τ_fold=0.190) | PASS_lab if signal absent at >3σ_lab on F1; FAIL_lab if F1 returns non-NULL detection at >3σ_lab on Lancaster vortex-core spectrometer | rank-2 ker(ι_*) generator [φ_67] does not inherit through χ : ℂ⊕ℍ⊕M_3(ℂ) → M_2(ℂ); BDI-protected parent inheritance | Lancaster MCT-3 dilution-fridge campaign 2027-2030 horizon | Sage-exact-zeta-regulated-Hochschild-pairing-cancellation-theorem | 3He-B-BDI-vortex-core-Caroli-Matricon | 10 | `29b76a1a1eab56da` | `d40a8d26588a0d20` | NEW S87-W5-2 LAB-FALSIFIER-A; W-5 W11-C5 4-gate template Gate-1 decisive (F1 of decisive triplet F1+F2+F5); paper §W5-2 5-row F-table |
| 48 | F2 SABS axial-equatorial off-diagonal pair correlation (B-phase decisive second-cleanest; φ_67 chiral-pair clean) | inheritance-morphism Class-A Gate-1 NULL kernel-signature falsifier | TKK / Lancaster / RHUL specular-wall SABS (4He-coated 131Xe protocol) | NULL on F2 at Δ_B/2 ≈ 100 MHz substrate margin 0.573193 M_KK² (arXiv:1005.0546 protocol) | PASS_lab if no axial-equatorial pair correlation at >3σ_lab; FAIL_lab if non-NULL pair correlation detection at >3σ_lab | rank-2 ker(ι_*) [φ_67] does not inherit through χ; second-cleanest substrate signal after F1 | RHUL nanofluidic cells 2028+ horizon | Sage-exact-zeta-regulated-Hochschild-pairing-cancellation-theorem | 3He-B-BDI-vortex-core-Caroli-Matricon | 10 | `29b76a1a1eab56da` | `d40a8d26588a0d20` | NEW S87-W5-2 LAB-FALSIFIER-A; W-5 W11-C5 4-gate template Gate-1 decisive (F2 of decisive triplet); paper §W5-2 5-row F-table; Cross-validation platform |
| 49 | F3 Half-quantum vortex (HQV) splitting in restricted geometry (B-phase supporting; φ_67 dipolar-locking) | inheritance-morphism Class-A Gate-3 NULL kernel-signature supporting falsifier | RHUL / Helsinki restricted-slab cells (D < ξ_B); µSR or NMR detection of HQV splitting | NULL on F3 substrate margin 0.40 M_KK² (substrate magnitude 1.7267) | PASS_lab if no HQV splitting at >3σ_lab; FAIL_lab if HQV non-NULL detection at >3σ_lab | rank-2 ker(ι_*) [φ_67] dipolar-locking sub-channel; supporting-NULL because cocycle-mixed at restricted geometry | RHUL / Helsinki restricted-slab 2028+ horizon | Sage-exact-zeta-regulated-Hochschild-pairing-cancellation-theorem | 3He-B-BDI-vortex-core-Caroli-Matricon | 10 | `29b76a1a1eab56da` | `d40a8d26588a0d20` | NEW S87-W5-2 LAB-FALSIFIER-A; W-5 W11-C5 4-gate template Gate-3 supporting; paper §W5-2 5-row F-table |
| 50 | F4 Hypercharge-twist Larmor-frequency anomaly under combined (p,T) sweep (B-phase cocycle-degenerate; φ_88 Cartan hypercharge) | inheritance-morphism Class-A Gate-3 NULL + Gate-4 multi-pressure slope discrimination | Helsinki ROTA / Lancaster Larmor multi-pressure NMR sweep 0–34 bar in 4-bar increments | NULL on F4 substrate margin 0.30 M_KK²; Gate-4 slope discrimination Jacobi-cubic vs φ_88-linear over 0–34 bar window | PASS_lab if F4 NULL at >3σ_lab AND Gate-4 slope linear (consistent with φ_88-clean); FAIL_lab if non-NULL detection AND/OR slope cubic (φ_67-contamination) | rank-2 ker(ι_*) [φ_88] Cartan hypercharge — cocycle-degenerate at fixed (p,T); requires multi-pressure slope-discrimination | Helsinki ROTA dynamic-pressure scan 5-7 yr horizon | Sage-exact-zeta-regulated-Hochschild-pairing-cancellation-theorem | 3He-B-BDI-vortex-core-Caroli-Matricon | 10 | `29b76a1a1eab56da` | `d40a8d26588a0d20` | NEW S87-W5-2 LAB-FALSIFIER-A; W-5 W11-C5 4-gate template Gate-3 supporting + Gate-4 slope discrimination; paper §W5-2 5-row F-table; **W11-5 §VII.AJ INTEREST**: F4 slope-discrimination is the operational falsifier for the W11-5 "M_3(ℂ) Cartan-zone weight non-negligible" diagnostic (rank-1-effective scenario) |
| 51 | F5 Acoustic-mode dispersion offset under Jensen-modulus quench (B-phase decisive; φ_88 Cartan-hypercharge clean Jensen-direction) | inheritance-morphism Class-A Gate-1 NULL + Class-B Gate-2 ratio test denominator | Lancaster / RHUL pulse-NMR Jensen-modulus quench (KZ protocol; Bunkov+Volovik 1999 fast-thermal quench through T_c) | NULL on F5 substrate margin 0.573193 M_KK²; cross-row F1/F5 ratio = 7.324992 ± 0.1% | PASS_lab if F5 NULL AND |ratio_lab − 7.324992|/7.324992 < 0.001 (within ±0.1% Gate-2 band); FAIL_lab if non-NULL F5 detection at >3σ AND/OR ratio outside [7.3177, 7.3323] | rank-2 ker(ι_*) [φ_88] Cartan-clean Jensen-direction; (Δ_B/Δ_A)^p cancellation under common p=2 makes ratio test substrate-falsifying | Lancaster KZ-quench protocol 2027-2030 horizon | Sage-exact-zeta-regulated-Hochschild-pairing-cancellation-theorem | 3He-B-BDI-vortex-core-Caroli-Matricon | 10 | `29b76a1a1eab56da` | `d40a8d26588a0d20` | NEW S87-W5-2 LAB-FALSIFIER-A; W-5 W11-C5 4-gate template Gate-1 decisive (F5 of decisive triplet) + Gate-2 ratio denominator; paper §W5-2 5-row F-table |

**(Δ_B/Δ_A)^p cancellation theorem applicability** (per `inheritance-falsifier-protocol.md` §"Audit at plan-freeze" item 4): F1 and F5 share common p=2 (verified by `_extract_p_value()` integer extractor at producing-script `computations/session-87/s87_w5_w11_c5_lab_falsifier.py` line 176 emission); (Δ_B/Δ_A)^{p_1−p_5} = (Δ_B/Δ_A)^0 = 1 EXACTLY; substrate-derived F1/F5 ratio 7.324992 PRESERVED INTACT in lab measurement. The 5 rows SATURATE rank-2 ker(ι_*) Hochschild cohomology; F6 (φ_67 ⊗ φ_88 bilinear) is structurally redundant per W-5 R2-A Convergence #5.


## NEW Rows #52--#54b -- 3He-A A-phase 4-gate falsifier protocol cross-platform (S87 W5-3 LAB-FALSIFIER-A class)

> **Origin**: S87 W5-3 `S87-W11-C6-MUSR-FALSIFIER` (volovik-superfluid-universe-theorist PRIMARY; connes-ncg-theorist co-signer; mack-cosmic-bridge sole writer of this section per `feedback_mack-bridge-role.md`). Verdict line `S87-W11-C6-MUSR-FALSIFIER: PASS ... audit_sha256=3e8a066e1652c0c86eafa3b983e8ef99935c79c3ff8962c08017f86b6aa7c44b content_sha256=6dd153256f3c6767... schema_version=S87+` (`computations/session-87/s87_gate_verdicts.txt:167`).
> **Substrate framing (PHONONIC)**: same substrate cocycle pair ([φ_67], [φ_88]) in ker(ι_*); inheritance morphism ι_A : (A_K, H_K, D_K) → 3He-A chiral-AIII BdG sector via algebra projection χ_A. Substrate ratio ‖φ_67‖/‖φ_88‖ = 7.324992 IS computed on the substrate spectral triple, NOT on any BdG-sector restriction — therefore IDENTICAL to B-phase prediction by substrate-resident argument. Container-thinking inversion FORBIDDEN per `phononic-framing.md`.
> **A-phase chirality correction χ_A**: substrate-derived (NOT a fit parameter); χ_A = Δ_B²/⟨|Δ_A(k)|²⟩_FS = 1/(2/3) = 3/2 = 1.500000 EXACT (Volovik 2003 §3.4 axisymmetric A-phase Fermi-surface average); A-phase substrate margins are chi_A-rescaled from B-phase (multiplicative factor 3/2).
> **Cross-platform identical-ratio test (high-leverage)**: Both Lancaster B-phase (Rows #47-#51) AND Aalto LTL A-phase (these rows #52-#54b) predict r_lab(F_1)/r_lab(F_5) = 7.324992 ± 0.1% IDENTICALLY — disagreement falsifies substrate-resident framing of the cocycle pair and forces re-anatomy of `cross-pillar-bridge-anatomy.md` substrate-IS / laboratory-IN partition at S88+.
> **EVOI tier**: LAB-FALSIFIER-A (decisive); 5-yr horizon = Aalto LTL / RHUL µSR 2027-2030.

| # | Observable | Falsifier function | Channel(s) | Prediction value(s) | Live-watch envelope | Internal-consistency split | Detector / horizon | scheme | convention | L_max | content_sha256 | audit_sha256 | notes |
|:-:|:-----------|:-------------------|:-----------|:--------------------|:--------------------|:----------------------------|:--------------------|:-------|:-----------|:------|:----------------|:--------------|:------|
| 52 | F1_A chirality-modified Caroli-Matricon analog at A-phase domain wall (decisive; φ_67 chiral-pair clean) | inheritance-morphism Class-A Gate-1 NULL kernel-signature falsifier | Aalto LTL µSR (PRIMARY); muon stopping site at A-phase fermion-bound-state energy ~Δ_A/k_B ≈ few mK | NULL on F1_A chi_A-corrected substrate margin 0.859790 M_KK² (B-phase 0.573193 × χ_A=3/2) | PASS_lab if F1_A NULL at >3σ_lab on Aalto LTL µSR asymmetry; FAIL_lab if non-NULL detection at >3σ_lab | rank-2 ker(ι_*) [φ_67] does not inherit through χ_A; chiral-AIII vs B-phase BDI inheritance morphism — same substrate, different child | Aalto LTL µSR 2027-2030 horizon | Sage-exact-zeta-regulated-Hochschild-pairing-substrate-resident | 3He-A-chiral-muSR-A-phase-modified | 10 | `6dd153256f3c6767` | `3e8a066e1652c0c8` | NEW S87-W5-3 LAB-FALSIFIER-A; W-5 W11-C6 4-gate template Gate-1 decisive (F1_A of A-phase decisive triplet F1_A+F2_A+F5_A); paper §W5-3 5-row A-phase F-table |
| 53 | F2_A chirality-modified F2 chiral-pair second invariant in A-phase µSR asymmetry (decisive; φ_67 chiral-pair clean) | inheritance-morphism Class-A Gate-1 NULL kernel-signature falsifier | Aalto LTL µSR + RHUL µSR cross-validation | NULL on F2_A chi_A-corrected substrate margin 0.330230 M_KK² (B-phase 0.220153 × χ_A=3/2) | PASS_lab if F2_A NULL at >3σ_lab; FAIL_lab if non-NULL detection at >3σ_lab | rank-2 ker(ι_*) [φ_67] χ_A-rescaled second invariant in A-phase; cross-platform sister of B-phase F2 | RHUL µSR 2028+ horizon | Sage-exact-zeta-regulated-Hochschild-pairing-substrate-resident | 3He-A-chiral-muSR-A-phase-modified | 10 | `6dd153256f3c6767` | `3e8a066e1652c0c8` | NEW S87-W5-3 LAB-FALSIFIER-A; W-5 W11-C6 4-gate template Gate-1 decisive (F2_A of A-phase decisive triplet); paper §W5-3 5-row A-phase F-table |
| 54 | F3_A chirality-modified Cartan-hypercharge primary in A-phase µSR longitudinal-relaxation (supporting; φ_88 Cartan hypercharge) | inheritance-morphism Class-A Gate-3 NULL kernel-signature supporting | Aalto LTL µSR longitudinal-relaxation channel | NULL on F3_A chi_A-corrected substrate margin 0.162461 M_KK² (B-phase 0.108307 × χ_A=3/2) | PASS_lab if F3_A NULL at >3σ_lab; FAIL_lab if non-NULL longitudinal-relaxation at >3σ_lab | rank-2 ker(ι_*) [φ_88] χ_A-rescaled Cartan-hypercharge primary; supporting-NULL because cocycle-clean at A-phase FS-averaged Δ_A | Aalto LTL µSR 2028+ horizon | Sage-exact-zeta-regulated-Hochschild-pairing-substrate-resident | 3He-A-chiral-muSR-A-phase-modified | 10 | `6dd153256f3c6767` | `3e8a066e1652c0c8` | NEW S87-W5-3 LAB-FALSIFIER-A; W-5 W11-C6 4-gate template Gate-3 supporting; paper §W5-3 5-row A-phase F-table |
| 54a | F4_A cocycle-degenerate slope discrimination via A-phase µSR multi-pressure (cocycle-degenerate; mix) | inheritance-morphism Class-A Gate-4 multi-pressure slope discrimination | Aalto LTL µSR multi-pressure scan 0–34 bar in 4-bar increments | F4_A chi_A-corrected substrate margin 0.235980 M_KK² (B-phase 0.157320 × χ_A=3/2); Gate-4 slope sign + magnitude > 3σ consistent with φ_88-linear (substrate prediction) | PASS_lab if F4_A NULL AND slope linear; FAIL_lab if non-NULL detection AND/OR slope cubic | cocycle-degenerate (mix) — F4_A is the A-phase analog of the B-phase F4 cocycle-degenerate Gate-4 multi-pressure slope discriminator | Aalto LTL µSR dynamic-pressure scan 5-7 yr horizon | Sage-exact-zeta-regulated-Hochschild-pairing-substrate-resident | 3He-A-chiral-muSR-A-phase-modified | 10 | `6dd153256f3c6767` | `3e8a066e1652c0c8` | NEW S87-W5-3 LAB-FALSIFIER-A; W-5 W11-C6 4-gate template Gate-4 slope discrimination; paper §W5-3 5-row A-phase F-table; **W11-5 §VII.AJ INTEREST**: F4_A slope-discrimination is the A-phase analog of the F4 B-phase operational falsifier for the W11-5 M_3(ℂ) Cartan-zone weight non-negligible diagnostic |
| 54b | F5_A chirality-modified F5 chiral-pair derived in A-phase µSR transverse-relaxation (decisive; φ_67 chiral-pair clean) | inheritance-morphism Class-A Gate-1 NULL + Class-B Gate-2 ratio test denominator | Aalto LTL µSR transverse-relaxation channel | NULL on F5_A chi_A-corrected substrate margin 0.117398 M_KK² (B-phase 0.078265 × χ_A=3/2); cross-row F1_A/F5_A ratio = 7.324992 ± 0.1% (IDENTICAL to B-phase by substrate-resident argument) | PASS_lab if F5_A NULL AND |r_A − 7.324992|/7.324992 < 0.001 AND |r_A − r_B| < 0.1%; FAIL_lab if any criterion violated | rank-2 ker(ι_*) [φ_67] χ_A-rescaled F5 derived; **HIGH-LEVERAGE**: Cross-platform identical-ratio prediction (substrate-resident vs BdG-sector-resident) | Aalto LTL µSR 2027-2030 horizon | Sage-exact-zeta-regulated-Hochschild-pairing-substrate-resident | 3He-A-chiral-muSR-A-phase-modified | 10 | `6dd153256f3c6767` | `3e8a066e1652c0c8` | NEW S87-W5-3 LAB-FALSIFIER-A; W-5 W11-C6 4-gate template Gate-1 decisive + Gate-2 ratio + cross-platform identical-ratio test; paper §W5-3 5-row A-phase F-table; **HIGHEST-LEVERAGE row** in S87 falsifier portfolio |

**Cross-platform substrate-resident-ness gate** (high-leverage discriminator landed at S87): the cocycle ratio `‖φ_67‖/‖φ_88‖ = 7.324992` is computed on the substrate spectral triple `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})` — NOT on any BdG-sector restriction. Therefore B-phase (BDI inheritance morphism χ_B) and A-phase (chiral-AIII inheritance morphism χ_A) MUST predict IDENTICAL ratio. Two-platform agreement on r=7.324992 ± 0.1% across Lancaster MCT-3 (Rows #47-#51) AND Aalto LTL µSR (Rows #52-#54b) confirms substrate-residence locus = substrate spectral triple. Disagreement falsifies the substrate-IS framing structurally, forcing re-anatomy of cross-pillar-bridge-anatomy.md substrate-IS / laboratory-IN partition at S88+.


## Cross-row dependency map (S87 W5 consolidation; S-5 workshop output)

> **Origin**: mack-cosmic-bridge S87 S-5 consolidation per workshop schedule entry S-5; output target `sessions/archive/session-87/workshops/s87-falsifier-master-inventory-consolidation.md`. Documents the structural dependency between Class A (NULL) and Class B (RATIO) falsifier rows under the (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5; 0.0e+00 residual).

### Substitution chain — cancellation theorem operational form

```
Step 1 (definition):   lab(F_i) := ‖φ_a‖ · f_i · (Δ_B/Δ_A)^{p_i}
Step 2 (substitution): lab(F_i)/lab(F_j) = (‖φ_a‖/‖φ_b‖) · (f_i/f_j) · (Δ_B/Δ_A)^{p_i − p_j}
Step 3 (common-p):     For F1 (p=2 NMR longitudinal Δ²) and F5 (p=2 acoustic Bogoliubov Δ²):
                       (Δ_B/Δ_A)^{p_1 − p_5} = (Δ_B/Δ_A)^0 = 1 EXACTLY.
Step 4 (f_1/f_5 = 1):  Substrate-protocol normalization gives f_1/f_5 = 1 for cross-row
                       Caroli-Matricon vs Jensen-quench-acoustic configurations.
Step 5 (direction):    lab(F_1)/lab(F_5) = ‖φ_67‖/‖φ_88‖ · 1 · 1 = 7.324992 EXACTLY.
                       ⇒ Substrate ratio PRESERVED INTACT; INDEPENDENT of Δ_B/Δ_A or p.
```

Conclusion: Class B ratio test is substrate-falsifying rather than lab-conversion-dependent.

### Failure-mode propagation (Row #45 NULL × Row #46 RATIO joint interpretation)

| Row #45 (Class A NULL) outcome                                    | Row #46 (Class B RATIO) outcome                          | Joint interpretation                                                                                                                                                                                |
|:------------------------------------------------------------------|:-----------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **NULL on F1+F2+F5 (PASS_lab)**                                   | **VACUOUS** (no signal → no ratio computable)              | Substrate's BDI-protected inheritance hypothesis CONFIRMED on rank-2 ker(ι_*); Class B cannot discriminate substrate-resident vs BdG-resident at vacuous ratio.                                       |
| **Non-NULL on F1 OR F2 OR F5 at >3σ_lab (FAIL_lab Class A)**       | **PASS_lab if r ∈ [7.3177, 7.3323]**                       | Decisive-triplet detection AND ratio in band ⇒ φ_67-sector signal non-trivial AT THE LAB but cohomology-class structure preserved. Substrate cocycles BdG-sector-resident; force re-anatomy.        |
| **Non-NULL on F1 OR F2 OR F5 at >3σ_lab (FAIL_lab Class A)**       | **FAIL_lab if r ∉ [7.3177, 7.3323]**                       | Decisive-triplet detection AND ratio outside band ⇒ both Class A AND Class B falsified; substrate-IS framing AND BDI-protected inheritance falsified. Highest-impact FAIL.                          |
| **NULL on F1+F2+F5 (PASS_lab)** AND non-NULL on F3 OR F4 (Gate-3 supporting; rank-1 effective) | **VACUOUS at decisive level; supporting at F3/F4 may discriminate** | Decisive substrate-clean (PASS); supporting rows show signal — implies Cartan-hypercharge cocycle [φ_88] inherits weakly through χ. Coincides with W11-5 §VII.AJ "M_3(ℂ) Cartan-zone weight non-negligible" diagnostic. Gate-4 multi-pressure slope on F4 (Jacobi-cubic vs φ_88-linear) is operational falsifier. |

### Cross-platform identical-ratio test (Lancaster B-phase Row #51 ↔ Aalto A-phase Row #54b)

| Lancaster B-phase ratio outcome | Aalto A-phase ratio outcome | Joint interpretation |
|:-------------------------------:|:---------------------------:|:---------------------|
| `r_B ∈ [7.3177, 7.3323]` PASS | `r_A ∈ [7.3177, 7.3323]` PASS AND `|r_A − r_B| < 0.1%` | **Cocycles SUBSTRATE-RESIDENT** confirmed. Both BDI and chiral-AIII inheritance morphisms preserve substrate ratio; substrate-IS framing UPHELD. |
| `r_B ∈ [7.3177, 7.3323]` PASS | `r_A ∈ [7.3177, 7.3323]` PASS but `|r_A − r_B| > 0.1%` | **Cocycles BdG-SECTOR-RESIDENT** (different in B vs A phase but each accidentally near 7.324992). Substrate-IS framing FALSIFIED at the residence-locus level. |
| `r_B ∈ band` PASS | `r_A ∉ band` FAIL | **Asymmetric falsifier**: A-phase BdG-sector cocycle differs from substrate; substrate-IS holds for B-phase but fails A-phase. Forces inheritance-morphism re-derivation for chiral-AIII branch. |
| `r_B ∉ band` FAIL | `r_A ∈ band` PASS | **Asymmetric falsifier**: B-phase BdG-sector cocycle differs from substrate; substrate-IS holds for A-phase but fails B-phase. Forces re-derivation for BDI branch. |
| `r_B ∉ band` FAIL | `r_A ∉ band` FAIL | **Substrate cocycle ratio prediction fully falsified**. Substrate-IS framing for cohomology-asymmetry test BROKEN; cocycle norms must be re-derived from cross-pillar-bridge-anatomy alternative formulations. |


## W11-5 §VII.AJ REGISTRY-FAIL annotation block (S87 W5 consolidation)

> **Origin**: S87 W11-5 `S87-3HEB-EXCESS-INHERITANCE-COMPARISON` FAIL at ratio_mismatch=1.029166 (Level-3 1.029 violates Level-2 0.05 by ~21×). Verdict line `computations/session-87/s87_gate_verdicts.txt:292` audit_sha256=`e1aef7ce0deaed2d85d8031fce1d009384ed0842ffb25585e880a5f475efd9aa` content_sha256=`9c23976f1a02b3d1e687d98f4e48f87dfcbc0ee83abafff73746267d3fe8ca1d`. **§VII.AJ candidate is NOT registry-eligible** per `cross-pillar-bridge-anatomy.md` §"Registry-PASS criterion".
> **What this FAIL is**: observable-construction-specific (M_3(ℂ) Cartan-zone weight non-negligible at L_max=10 in multiplicity-weighted Mellin-pole-window scheme falsifies the rank-1 effective-truncation assumption that underwrites Level 2).
> **What this FAIL is NOT**: bridge-map-defective. Per W11-5 line 9564: "the inheritance morphism ι is structurally well-defined; the FAIL is at the level of the **specific spectral-excess observable construction**, not at the bridge map itself." S86 W1b-T8 inheritance-vs-analogy theorem PRESERVED; (Δ_B/Δ_A)^p cancellation theorem (CC1) holds; W-5 cohomology-asymmetry calibration ratio 7.3250 unaffected.

### Per-row interpretation under each W11-5 cause-attribution scenario

| Affected row(s) | (S1) observable-construction defect | (S2) kernel-rank invalid | (S3) bridge-map mis-specified |
|:----------------|:-------------------------------------|:--------------------------|:-------------------------------|
| **#45** Class A NULL | PRESERVED — kernel-signature unaffected by spectral-excess observable | SHIFTS — "decisive triplet" rebrand to "candidate" pending rank re-derivation | SHIFTS — NULL prediction may apply to different sub-algebra than M_3(ℂ) |
| **#46** Class B ratio | PRESERVED — substrate-resident ratio computed on (A_K, H_K, D_K), independent of W11-5 spectral-excess construction | SHIFTS — ratio test may become vacuous or rank-truncated under rank ≠ 2 | SHIFTS — sub-leading correction terms may widen [7.3177, 7.3323] band |
| **#47-#51** B-phase F1-F5 | PRESERVED for decisive Gate-1 NULL; supporting rows shift | SHIFTS as #45 | SHIFTS — χ-correction may flatten or reverse predictions |
| **#50** F4 cocycle-degenerate | **HIGHEST IMPACT**: F4 slope discrimination IS operational falsifier for (S1) M_3(ℂ) Cartan-zone weight diagnostic | SHIFTS — slope predicate re-evaluates under corrected rank | SHIFTS — χ-correction may invert slope sign |
| **#52-#54b** A-phase F1_A-F5_A | PRESERVED — cross-platform identical-ratio holds (substrate-resident) | SHIFTS as B-phase analogs; chi_A=3/2 intact but rank correction propagates | SHIFTS as B-phase analogs |
| **W2-1 paper §3 inheritance morphism** | PRESERVED at paper-artifact level; verdict line `1f38f988...` immutable | SHIFTS at interpretation level; carry-forward `S88-3HE-B-INHERITANCE-CARTESIAN-CONFIRM` is fix-in-S88 path | SHIFTS as (S2) |

### Adversarial-skeptic flag (per `feedback_mack-bridge-role.md`)

mack-cosmic-bridge flags Row #46 + Rows #52-#54b cross-platform identical-ratio prediction as **contested** by in-flight Slot-2 workshops:
- Slot-2 W-1 §VII.W-2 status (Pillar III↔IV bridge anatomy generalization to Pillar IV↔V)
- Slot-2 W-4 W11-5 cause attribution (S1)/(S2)/(S3) operational discriminator
- Slot-2 W-5 axis-of-observation (substrate-resident argument robustness against alternative inheritance-morphism formulations)

The W11-5 REGISTRY-FAIL is itself the strongest current evidence that calibration-corpus generalization to FWD-C3 is non-trivial (registry-FAIL is observable-construction-specific, not bridge-map-defective). Cocycle-asymmetry ratio test inherits robustness from the bridge map even under the FAIL.


## K-counter calibration tracking (S87 W5 consolidation; mirror of `cross-pillar-bridge-anatomy.md` lines 246-253)

> **Origin**: S87 S-5 mack-cosmic-bridge consolidation; mirrors `.claude/rules/cross-pillar-bridge-anatomy.md` §"Forward template-adoption (calibration-corpus tracking)" K-counter sub-section. K-counter at S87 close = **K=2** (1 PASS + 1 REGISTRY-FAIL); promotion threshold K_promotion=3; status = **SUGGESTION** (NOT MANDATORY).

### Substitution chain (K-counter logic)

```
Step 1 (definition):   K_eff       := count of distinct calibration-corpus instances
                        K_promotion := 3 (per feedback_rules-compensate-missing-structure.md) # (local)
                        status      := SUGGESTION if K_eff < K_promotion; MANDATORY otherwise
Step 2 (substitution): K_eff = 2 (1 PASS instance #1 + 1 REGISTRY-FAIL instance #2)
                        K_promotion = 3  # (local) restated from Step 1 definition
Step 3 (simplification): K_eff (2) < K_promotion (3) ⇒ status = SUGGESTION
Step 4 (direction):    Status retained at SUGGESTION; promotion event awaits 3rd instance.
```

### Calibration corpus table (S87 close state)

| # | Workshop | Bridge | Status | Level-3/Level-2 | Falsifier rows |
|:--|:---------|:-------|:-------|:--------------:|:----------------|
| 1 | S86 W-5 (volovik PRIMARY + connes CO-AUTHOR) | Pillar III ↔ Pillar IV (HP^1 cohomology ↔ Peotta-Törmä quantum-metric trace) | **LANDED** §VII.AF.1 | 0.0095% / 0.10% = 0.0950 (10× INSIDE envelope) | (no direct lab rows; abstract structural identity) |
| 2 | S87 W11-5 (volovik PRIMARY) | Pillar IV ↔ Pillar V (substrate spectral-excess ↔ 3He-B BdG-undoubled excess at polycritical pressure) | **REGISTRY-FAIL** §VII.AJ NOT eligible | 1.029 / 0.05 = 20.58 (~21× VIOLATES envelope) | (no rows landed; carry-forward S88-3HEB-EXCESS-INHERITANCE-M3C-PROJECTED-RETRY) |
| 3 | — | — | (awaits future high-density workshop) | — | — |

K_eff = 2 < K_promotion = 3 ⇒ **status = SUGGESTION** (NOT MANDATORY).

### Adversarial-skeptic note on REGISTRY-FAIL counting

The REGISTRY-FAIL on instance #2 STRENGTHENS the corpus calibration value (it demonstrates the rule correctly flags FAIL cases — saturating edge-case coverage that a PASS-only corpus cannot reach), but if the 3rd instance is also a FAIL, the FAIL_ratio = 2/3 > 0.5 should defer MANDATORY promotion pending rule-recalibration workshop. mack-cosmic-bridge flags this for the orchestrator at K=3 trigger event.


## NEW Rows #55-#57 -- Forward bridge candidates FWD-C1/C2/C3 (S87 W5-5 pre-registration)

> **Origin**: S87 W5-5 cross-pillar-bridge-anatomy template-adoption + this S-5 consolidation. Per `cross-pillar-bridge-anatomy.md` §"Three forward bridge candidates for S88+ dispatch", three forward candidates pre-registered with their substrate-IS / laboratory-IN identifications, bridge maps, algebraic envelopes, empirical anchor targets, and inheritance-kernel rank declarations.
> **Status**: SUGGESTION (NOT MANDATORY) at K=2 per K-counter sub-section above; each candidate adopts the 5-anatomy + 3-level discipline as design SUGGESTION pending K=3 promotion event.

| # | Observable | Falsifier function | Channel(s) | Prediction value(s) | Live-watch envelope | Internal-consistency split | Detector / horizon | scheme | convention | L_max | content_sha256 | audit_sha256 | notes |
|:-:|:-----------|:-------------------|:-----------|:--------------------|:--------------------|:----------------------------|:--------------------|:-------|:-----------|:------|:----------------|:--------------|:------|
| 55 | FWD-C1 Pillar I↔II n_s cross-pillar bridge candidate (substrate-IS n_s_FW vs Planck CMB lab-IN) | forward cross-pillar bridge §VII.AK candidate; rank(ker ι_*)=1 single-scalar | Planck 2018 TT,TE,EE+lowE+lensing scalar spectral index at k_pivot=0.05 Mpc⁻¹ | Substrate-IS: n_s_FW = 0.9561 (S65 BCS+1-loop; canonical_constants.py:1499); Lab-IN: Planck n_s = 0.9649 ± 0.0042; Level-3 absolute deviation 0.0088 (1.40σ) | Level-2 envelope: L⁻³ at d=4 → 0.001 at L_max=10 (W-5 inherited; pending substrate-first c_sub completion per `substrate-first-canonical-sourcing.md`) | Substrate-IS systematic floor vs W-5-inherited algebraic envelope; mack-cosmic-bridge flags Level-2 envelope re-derivation needed (Level-3 0.0088 > envelope 0.001 by ~9×) | CMB-S4 2030 / LiteBIRD 2030 / CMB-HD 2035 | Mukhanov-Sasaki-mode-function ∘ HKR-substrate-scalar-moment | n_s-spectral-action-prediction-substrate-IS | 10 | `<S88-FWD-C1-pending>` | `<S88-FWD-C1-pending>` | NEW S87-W5-5 SUGGESTION (K=2); §VII.AK candidate; 4-field carry-forward `S88-FWD-C1-PILLAR-I-II-N-S-BRIDGE-LANDING` ~6-10h post-c_sub |
| 56 | FWD-C2 Pillar II↔V Mellin-cone↔BdG cross-pillar bridge candidate (Mellin-residue ↔ BdG band-edge) | forward cross-pillar bridge §VII.AL candidate; rank(ker ι_*)≥2 multi-residue generators | Mellin-cone substrate-residue at s ∈ {3,4} ↔ BdG band-edge at K_0(M_2(ℂ)) image | Substrate-IS: Mellin-Barnes residue at substrate-distance s ∈ {3,4} on Pillar-II Mellin-cone (substrate-first cocycle norms ‖φ‖ Sage-exact per W-5 phi67/phi88); Lab-IN: BdG band-edge Pillar-V finite-rank K_0(M_2(ℂ)) image (3He-B child, Volovik 2003 §6 BDI Pf=−1) | Level-2 envelope: L_max⁻α with α ∈ {2,3} under spectral-distance scaling; α pinned post-Mellin-pole-closure at S87 W2-? cluster-span PASS | Multi-residue generators may differ across substrate-distance s={3,4} poles; binomial(rank, 2) cross-cocycle ratios pre-registered per `inheritance-falsifier-protocol.md` rank≥2 generalization | BdG band-edge ARPES on 3He-B child realization 2030+ horizon; cross-checks Pillar-II Mellin-cone closure | Connes-Karoubi-pairing ∘ K-theory-boundary-Pillar-II-Mellin-pole-to-Pillar-V-BdG | Mellin-cone-substrate-distance-multi-residue | 10 | `<S88-FWD-C2-pending>` | `<S88-FWD-C2-pending>` | NEW S87-W5-5 SUGGESTION (K=2); §VII.AL candidate; companion to W-6 quotient-functor framework; 4-field carry-forward `S88-FWD-C2-MELLIN-BDG-BRIDGE-LANDING` ~10-15h post-Mellin-closure |
| 57 | FWD-C3 Pillar IV↔V substrate cocycles ↔ 3He-B/A laboratory observables cross-pillar bridge candidate | forward cross-pillar bridge §VII.AM candidate; rank(ker ι_*)=2 [φ_67]+[φ_88] | Substrate-IS: ‖φ_67‖=0.793346 M_KK², ‖φ_88‖=0.108307 M_KK² (W-5 Sage-exact); Lab-IN: 3He-B vortex-core (Rows #47-#51) AND 3He-A µSR (Rows #52-#54b) 4-gate falsifier | Substrate-IS: ‖φ_67‖/‖φ_88‖ = 7.324992 (Sage-exact at machine precision; canonical S86 W-5 CANONICAL-5); Lab-IN: r_lab from Lancaster + Aalto cross-platform | Level-2 envelope: structural-exact form 7.3250 ± 0.1% (W-5 cancellation theorem; NOT L_max⁻α algebraic bound); Level-3 anchor: S88+ Lancaster MCT-3 + Aalto LTL µSR data | Cross-platform identical-ratio test (substrate-resident vs BdG-sector-resident) is high-leverage discriminator; W11-5 REGISTRY-FAIL is observable-construction-specific (not bridge-map-defective) so this candidate inherits bridge-map robustness | Lancaster MCT-3 + Aalto LTL 2027-2030 horizon (multi-year experimental cycle) | Sage-exact-zeta-regulated-Hochschild-pairing-cancellation-theorem-rank-2 | 3He-B-BDI ∪ 3He-A-chiral-AIII-cross-platform | 10 | `<S88+-FWD-C3-pending>` | `<S88+-FWD-C3-pending>` | NEW S87-W5-5 SUGGESTION (K=2); §VII.AM candidate; rank-2 generalization per `inheritance-falsifier-protocol.md` §"Generalization beyond 3He-B (W-5 Q8)"; partially LANDED via Rows #47-#54b lab pre-registrations; 4-field carry-forward `S88+-FWD-C3-COCYCLE-3HE-BRIDGE-LANDING` lab-blocked multi-year |

### FWD candidates 4-field carry-forwards (per `feedback_fix-in-session-never-defer.md` 4-field-spec discipline)

**`S88-FWD-C1-PILLAR-I-II-N-S-BRIDGE-LANDING`** (FWD-C1, Row #55):
1. **What**: register §VII.AK candidate cross-pillar bridge entry for Pillar I↔II n_s with all 5 IS-not-IN + 3-level declarations; pin Level-3 anchor at n_s_FW=0.9561 vs Planck 0.9649±0.0042; confirm Level-2 envelope at d=4 satisfies Level-3 0.0088 absolute deviation OR re-derive Level-2 from substrate-first c_sub (NOT W-5-inherited L⁻³).
2. **Inputs**: canonical_constants.py:1499 n_s_framework=0.9561 (S65 W3-G48 promotion); Planck 2018 anchor (mack-observational-constraints registry); S86 W5a Z-factor c_sub completion (BLOCKED on c_sub substrate-first canonical pin).
3. **Gate criterion**: PASS iff §VII.AK entry has all 5 anatomy + 3-level markers AND Level-3 < Level-2 envelope at canonical L_max=10; INFO if Level-3 ∈ (envelope, 10× envelope]; FAIL if > 10× envelope.
4. **Effort**: ~6-10h post-c_sub (Level-2 envelope re-evaluation + §VII.AK registry-write + falsifier-master-inventory row update).

**`S88-FWD-C2-MELLIN-BDG-BRIDGE-LANDING`** (FWD-C2, Row #56):
1. **What**: complete §VII.U/V family Mellin-cone closure; derive Pillar-II → Pillar-V Connes-Karoubi pairing explicitly; register §VII.AL candidate cross-pillar bridge with all 5 anatomy + 3-level declarations; pre-register binomial(rank, 2) cross-cocycle ratios per inheritance-falsifier-protocol.md rank≥2 generalization clause.
2. **Inputs**: Mellin-cone family closure at S87 W2-? cluster-span PASS (pending); cocycle norms per cohomology-class-pair from W-5 calibration; W-6 quotient-functor framework (cross-pillar-bridge-anatomy §"Quotient-functor pre-registration discipline").
3. **Gate criterion**: PASS iff §VII.AL entry has all 5 anatomy + 3-level markers AND Level-3 within Level-2 envelope at canonical L_max=10 AND binomial(rank, 2) cross-cocycle ratios pre-registered; INFO if 1+ ratio missing; FAIL if Level-3 > 10× envelope OR no ratio pre-registered.
4. **Effort**: ~10-15h post-Mellin-cone closure (depends on §VII.U/V family closure timeline).

**`S88+-FWD-C3-COCYCLE-3HE-BRIDGE-LANDING`** (FWD-C3, Row #57):
1. **What**: register §VII.AM candidate cross-pillar bridge entry with all 5 anatomy + 3-level declarations + binomial(2,2)=1 cross-cocycle ratio (canonical 7.324992); land at registry once Lancaster MCT-3 + Aalto LTL µSR data both available with measured ratios on F1/F5 cross-row.
2. **Inputs**: Lancaster MCT-3 vortex-core spectroscopy data (~2027-2030 horizon, Pickett group); Aalto LTL µSR data (~2027 horizon, Krusius/Tuoriniemi/Eltsov); W5-2+W5-3 Rows #47-#54b + their substrate-derived predictions; W-5 cancellation theorem (S86 W-5 DONE-5).
3. **Gate criterion**: PASS iff both lab ratios in [7.3177, 7.3323] AND |r_A − r_B| < 0.1% (cross-platform substrate-resident-ness confirmation); INFO if one ratio in band but not both; FAIL if either ratio outside band by > 1%.
4. **Effort**: 0.5 wave-equivalents (~2-4h) for the registry-write + falsifier-row append + Stage-1-CANDIDATE tagging once both lab datasets land; the lab-execution cycle itself is multi-year (2027-2030+ horizon).


## Section closure — S87 W5 consolidation (S-5 workshop output)

This section consolidates W5-2 (5 B-phase rows #47-#51) + W5-3 (5 A-phase rows #52-#54b) + W11-5 §VII.AJ REGISTRY-FAIL annotation + K-counter calibration tracking (K=2) + FWD-C1/C2/C3 forward candidates (rows #55-#57) into the falsifier-master-inventory. mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md`. Producing-script `computations/session-87/s87_w5_falsifier_inventory_consolidation_writer.py` (one-shot append-only Python writer per `epistemic-discipline.md` §"Registry-Write Hygiene under Parallel-Writer Race"); workshop output `sessions/archive/session-87/workshops/s87-falsifier-master-inventory-consolidation.md` (full table + narrative + adversarial-skeptic flags + 4-field carry-forwards).
"""


def main() -> int:
    """Append payload to inventory file."""
    if not INVENTORY.exists():
        print(f"ERROR: inventory not found at {INVENTORY}", file=sys.stderr)
        return 2

    pre_size = INVENTORY.stat().st_size  # (local)
    with INVENTORY.open("a", encoding="utf-8", newline="") as fh:
        fh.write(PAYLOAD)
    post_size = INVENTORY.stat().st_size  # (local)

    print(f"OK: appended {post_size - pre_size} bytes to {INVENTORY}")
    print(f"    pre_size  = {pre_size} bytes")
    print(f"    post_size = {post_size} bytes")
    print(f"    delta     = {post_size - pre_size} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
