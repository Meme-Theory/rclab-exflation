#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S96-CONSOL-3REGISTER-TABLE — falsifier-master-inventory.md ATOMIC append
========================================================================
mack-cosmic-bridge SOLE WRITER of falsifier-master-inventory.md (feedback_mack-bridge-role.md).

Lands the pending W6/W7 §7-surface falsifier-inventory rows consolidated at W8-2, per the
canonical write-order (verdict file -> canonical_constants.py [already complete] ->
falsifier-master-inventory.md [this step]):

  Row #71 — f*sigma_8(z) RSD growth discriminator         (W6-1 / W7-5 Row A)
  Row #72 — first-sound BAO ring A_FS = 0.204             (W6-2)
  Row #73 — neutrino normal mass ordering B1<B2<B3        (W7-5 Row B)
  Row #7.audit-2 — CGWB peak-FREQUENCY scope-correction   (W6-3; annotation on the existing Row #7.audit)

One-shot append-only writer (POSIX O_APPEND single open('a')) per
epistemic-discipline.md §"Registry-Write Hygiene under Parallel-Writer Race".
Values transcribed from canonical_constants.py (write-order Step 2 already complete).

NON-PHONONIC (methodology / falsifier-row landing on a curated registry).
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")

import sys
import hashlib
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
_SHARED = PROJECT_ROOT / "computations" / "_shared"
if str(_SHARED) not in sys.path:
    sys.path.insert(0, str(_SHARED))
from canonical_constants import (  # noqa: E402
    sigma_8,
    f_FW,
    f_LCDM,
    fsigma8_product_suppression_FW_max_pct,
    f_bare_suppression_FW_pct,
    A_FS_first_sound_ring,
    f_obs_CGWB_peak_kappa_nat,
    Omega_GW_Lambda_A_LISA,
)

INVENTORY = PROJECT_ROOT / "sessions" / "framework" / "registry" / "falsifier-master-inventory.md"

# verdict-line anchors (full-64) from this session's gates.
SHA_FSIGMA8 = "318df6edeadb621453a46be1f5e8568db3fbff780e6e1792a69cb5ba37e06027"   # W6-1
SHA_RING = "b74ccd561136efc57f3f994e7e302bd9a0215a7d616c9e0096810ab9bf64955c"  # W6-2 (full-64)
SHA_SELFINV = "92a368105c829e8394ec7a1be899e42813f496cbbf0926a1f86b8cb06f6d38f1"  # W7-5 (ordering)
SHA_CGWBPEAK = "646e6ad087dae6441515a62456300af48c7c135be103147767fbcbcbfbf2ee2e"  # W6-3
SHA_W82 = "014aea22370aa3f8465932c7dde5dc6bb18c6122b6700918b81eabfc9b0816fe"        # this gate


def main() -> int:
    original = INVENTORY.read_text(encoding="utf-8")
    orig_sha = hashlib.sha256(original.encode("utf-8")).hexdigest()
    print(f"[inv] inventory original sha256={orig_sha[:16]}... ({len(original)} chars)")

    # Idempotency: do not double-append.
    if "## NEW Rows #71-#73 — S96 W8-2 consolidation" in original:
        print("[inv] W8-2 rows already present -> idempotent no-op")
        return 0

    block = f"""

## NEW Rows #71-#73 — S96 W8-2 consolidation of W6/W7 pending §7-surface items (mack-cosmic-bridge sole-writer landing)

> **Origin**: gate `S96-CONSOL-3REGISTER-TABLE` (S96 W8-2, [AUDIT], INFO; audit_sha256=`{SHA_W82}`). Consolidates the pending W6/W7 inventory-row recommendations addressed to mack-cosmic-bridge in their WP sections (W6-1 f·σ₈, W6-2 first-sound ring, W7-5 normal ordering) per the canonical write-order (verdict → canonical_constants.py [complete] → falsifier-master-inventory.md [this landing]). mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md` (AMRI-PROMOTED 2026-04-28).
> **Substrate framing (PHONONIC)**: each row is a spectral moment of `D_K` at a single modulus, transduced through the `a₂`/`a₄` channel into an emergent observable — NOT a feature fit IN a ΛCDM container. Direction: `D_K eigenvalues → spectral-moment channel → emergent observable → detector`.

| # | Observable | Falsifier function | Channel(s) | Prediction value(s) | Live-watch envelope | Internal-consistency split | Detector / horizon | scheme | convention | L_max | content_sha256 | audit_sha256 | notes |
|:-:|:-----------|:-------------------|:-----------|:--------------------|:--------------------|:----------------------------|:--------------------|:-------|:-----------|:------|:----------------|:--------------|:------|
| 71 | f·σ₈(z) RSD growth-rate × amplitude (redshift-space distortion) | zero-parameter RSD discriminator; the f·σ₈ PRODUCT suppression breaks the static-σ₈ degeneracy by shape+sign | DESI / Euclid RSD multipoles; a₂ growth-channel (GGE-relic acoustic self-organization, the cosmic web) | FW: **{fsigma8_product_suppression_FW_max_pct}%** f·σ₈ PRODUCT suppression vs ΛCDM @ z=0.51 (zero-parameter; f_FW={f_FW:.7f} vs f_LCDM={f_LCDM:.7f}); **bare-f {f_bare_suppression_FW_pct}%** (C5 conflation guard: the −4.058% is the PRODUCT, NOT bare-f) | within current 1σ; at 1σ band-edge for DESI-5yr; ≥1σ at Euclid middle bins; **S₈-tension-relieving sign** (suppression negative ⇒ FW f·σ₈ below ΛCDM ⇒ relieves lensing-vs-Planck S₈ tension) | C5 conflation guard: PRODUCT (−4.058%) vs bare-f (−0.311%) MUST NOT be conflated; C10 borrowed-H(z) caveat (modulation-on-borrowed-H) flagged | DESI-5yr (~2029) → Euclid (2030s) | a₂-growth-channel-fσ8-product-suppression | zero-free-parameter-RSD-S8-tension-relieving | 10 | (this gate) | `{SHA_FSIGMA8}` | NEW S96 W8-2; W6-1 `S96-OBS-FSIGMA8-FORECAST` PASS; canonical pins `fsigma8_product_suppression_FW_max_pct`/`f_bare_suppression_FW_pct`/`f_FW`/`f_LCDM`; forecast σ-dist 1.013 DESI-Y5 / 1.534 Euclid (the full forecast-fetch σ-distance is a W6 compute CF) |
| 72 | first-sound BAO ring A_FS = c₂²/c₁² imprint on matter P(k) at k₁=0.0193 Mpc⁻¹ (r₁=325.3 Mpc) | zero-parameter two-fluid acoustic-ring falsifier; **NO ΛCDM counterpart** (the second-sound/condensate mode has no ΛCDM analog) | matter power spectrum P(k) at recombination; a₂ acoustic-metric channel (metric mode c₁=c, Goldstone/condensate mode c₂) | FW: **A_FS = {A_FS_first_sound_ring}** = c₂²/c₁² (two-fluid acoustic ratio, zero-parameter, live) | detectable in DESI full-shape NOW / Y5 | per-branch effacement sub-feature A_obs_B1 = 1.445e-3 is real but **OUTSIDE current rulers BY DESIGN** (0.60× the DESI-DR2 0.24% ruler) — keep "far below current rulers" scoped to THIS sub-feature, NOT the ring (the ring is 141× the sub-feature) | DESI full-shape / DESI-5yr (SNR **8.6**, σ_exp=2.35% FETCHED arXiv:2411.19738v2) / DESI-DR1 (SNR **5.1**) | a₂-acoustic-metric-first-second-sound-ratio | two-fluid-acoustic-ring-NO-LCDM-counterpart | 10 | (this gate) | `{SHA_RING}` | NEW S96 W8-2; W6-2 `S96-OBS-FIRST-SOUND-RING` PASS; canonical pin `A_FS_first_sound_ring`; closes the only stranded INFO in the S95 LSS harvest into a live BAO falsifier |
| 73 | neutrino mass ordering (Normal vs Inverted) | zero-parameter normal-ordering prediction; a NO-vs-IO detector verdict is a clean yes/no on the (1,1,0)-sector substrate ordering | D_K (1,1,0)-singlet eigenvalue ordering; a₄/fiber neutrino sector | FW: **Normal B1<B2<B3** (zero-free-parameter, machine-ε; dynamical via the τ=0.107 B1↓-below-B2 crossing of D_K's (1,1,0)-sector; S8/S34–36/S52/S56) | NuFit-6.0 prefers NO at ~2.5σ ⇒ consistent; a JUNO/DUNE NO-vs-IO verdict is decisive | structural prediction (no internal-consistency split — it is a discrete ordering, PROVEN at machine-ε) | JUNO 2026+ / DUNE 2030s | a₄-fiber-(1,1,0)-singlet-eigenvalue-ordering | zero-free-parameter-normal-ordering-tau-0.107-crossing | 10 | (this gate) | `{SHA_SELFINV}` (W7-5 S96-HYG-SELF-INVENTORY) | NEW S96 W8-2; W7-5 MACK-INVENTORY-RECOMMENDATION Row B; the entire neutrino sector was ABSENT from the inventory before this landing; `falsifier-rigor-registry.md` row + `s52_sector_ordering.txt` τ-evolution corroborate |

### Row #7.audit-2 — CGWB peak-FREQUENCY scope-correction (S96 W6-3; mack-cosmic-bridge sole-writer landing)

> **Origin**: gate `S96-OBS-CGWB-PEAK-FREQ` (S96 W6-3, FAIL — D4 resolved AGAINST the mHz peak). Canonical write-order Step 3 SCOPE-CORRECTION annotation on **Row #7 / Row #7.audit** (the LISA CGWB flagship). Verdict-line `audit_sha256={SHA_CGWBPEAK}`; canonical `f_obs_CGWB_peak_kappa_nat={f_obs_CGWB_peak_kappa_nat:.4e}`.

**The flagship row #7 must split TWO observables (they were conflated in the bare "FLAGSHIP" cell):**

- **(a) Ω_GW AMPLITUDE at the LISA pivot — UNCHANGED, LIVE.** `Ω_GW^(A) ~ {Omega_GW_Lambda_A_LISA:.0e}` at 3 mHz, 11+ OOM above LISA-PLS, GGE-acoustic / squeezed-graviton sourced (wall channel = 0 EXACTLY, π₀(U(1))=0; Row #7.audit). LISA samples the **IR-tail amplitude** of the acoustic spectrum in its band — this is the live flagship discriminator (`S96-OBS-OMEGAGW-GGE-VS-ZN` PASS, W6-4).
- **(b) CGWB peak FREQUENCY — CORRECTED, the mHz-peak placement is REFUTED.** `f_obs(κ_nat) = {f_obs_CGWB_peak_kappa_nat:.4e} Hz` (GHz+ band, 43.9 decades above LISA): the fold van-Hove ACOUSTIC emission `M_KK/(2π)` redshifted by `a_fold/a_now = 0.4723`. The asserted "peak in the LISA mHz band" is **REFUTED by the substrate redshift chain**. The peak-frequency placement is normalization-set (the open `M_KK⁻¹→s` knob — the SAME knob blocking the derived `a(t)`, §6.3); reaching LISA would require `κ = 25 s/M_KK⁻¹`, **42.5 OOM** from the natural `ħ/M_KK` and 11.4 OOM beyond the swept band.

**Tag**: the peak-frequency flagship is **NORMALIZATION-CONDITIONAL-AND-CURRENTLY-AGAINST-mHz** (pending a substrate-pinned κ); live-watch on the `M_KK⁻¹→s` normalization. **Read row #7 as the AMPLITUDE discriminator (live), NOT a peak-in-LISA-band claim.** The peak-frequency claim, naively read, is currently AGAINST the data; the amplitude flagship stands.

**Cross-references**: Row #7 ((A)/(C) regulator-class discriminator); Row #7.audit (W6-4 source-channel decomposition + FIDELITY NOTE); the capstone §7.2 carries the matching W8-2 scope-correction note (`S96-CONSOL-3REGISTER-TABLE` patch). The W6-4 FIDELITY NOTE (Row #7.audit line 159) — `1e-57/8.299e-58 = 1.205× = 0.081 OOM` (same-decade), NOT "~10×/~2 OOM" — is ratified by this W8-2 consolidation: the binding reason to use the Sage-exact `8.299e-58` is publication-precision hygiene (Class-8.3), not an OOM blunder.

### W8-2 consolidation summary (mack sole-writer)

The W8-2 3-register consolidation lands **three NEW falsifier rows** (#71 f·σ₈, #72 first-sound ring, #73 normal ordering) + **one scope-correction** (Row #7.audit-2 CGWB peak-frequency). The pending items routed to mack at W8-2 are fully discharged:

- **W6-1 f·σ₈** → Row #71 (LANDED).
- **W6-2 first-sound ring** → Row #72 (LANDED).
- **W6-3 CGWB peak-freq** → Row #7.audit-2 scope-correction (LANDED) + capstone §7.2 cross-ref note (LANDED via the §7.1 patch).
- **W7-5 normal ordering** → Row #73 (LANDED); W7-5 f·σ₈ Row A == Row #71 (same observable, single landing).
- **W6-4 Ω_GW round-figure fidelity** → ratified (already landed Row #7.audit line 159); bound to Class-8.3 publication-precision hygiene, NOT an OOM blunder.
- **§VII.BH (c_s²=0)** → mack-review verdict: NO §7-falsifier-surface retrofit needed — it is a §VII permanent-results CROSS-PILLAR BRIDGE entry (substrate-IS → Kasparov → lab-IN bound), not a falsifier-surface row; the §7.1 c_s² row stays as a SCORECARD POINTER (robust-spine member). No falsifier-inventory row created for c_s².
- **W6-7 σ₈/S₈** → Row #70 already landed (W6-7); the §7.1 σ₈ comparison anchor is fixed to Planck σ₈={sigma_8} (NOT S₈=0.829) in the capstone §7.1 patch (prose/citation fix also routes to W8-6).

The §7.1 "now" table is now split into 3 epistemic registers (robust-structural / conditional / currently-falsified; `S96-CONSOL-3REGISTER-TABLE` INFO, SUM-check 7+6+1=14 exact, no flattening, m_H disclosed dual-status straddle). mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md`.
"""

    # atomic append (single open('a'), POSIX O_APPEND).
    with INVENTORY.open("a", encoding="utf-8", newline="") as fp:
        fp.write(block)
        fp.flush()
        os.fsync(fp.fileno())

    new = INVENTORY.read_text(encoding="utf-8")
    new_sha = hashlib.sha256(new.encode("utf-8")).hexdigest()
    print(f"[inv] appended {len(block)} chars; new sha256={new_sha[:16]}... ({len(new)} chars)")
    print("[inv] Rows #71/#72/#73 + Row #7.audit-2 + W8-2 summary landed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
