---
name: bao-substrate-emergent-transport
description: How to translate an M_KK-internal substrate speed/split into an observational BAO peak-position shift — the effacement-projection transport + the S43 first-sound-ring channel
metadata:
  type: project
---

# BAO substrate-IS → emergent-observable transport (S94 S-1)

**Methodological note** (re-usable at spawn): M_KK-unit substrate branch speeds do NOT directly give a measurable BAO shift. A substrate-internal fractional speed split `s_b = δ_b/c_b²` must be transported onto the EMERGENT 4D acoustic channel before any detector comparison.

**Why**: the observed BAO peak position is set by the emergent acoustic sound speed (the Goldstone `c_Gold=0.915` is the one true 4D light cone), NOT by the sub-luminal M_KK-internal branch speed `c_b^(2) ≪ 1`. Treating the internal branch speed AS the emergent acoustic speed is a container-thinking conflation forbidden by `phononic-framing.md §"IS Space, Not IN Space"`.

**How to apply** (the transport, per `cross-pillar-bridge-anatomy.md §"Per-observable transport-degree scale-separation"` corpus §23 — NON-SCALAR transport, substrate ≠ pivot):
- effacement-projection weight: `A_eff,b = (c_b^(2)/c_Gold)²` (the S43 KK-CMB-TF-43 `A_FS = c₂²/c₁² = 1/[3(1+R*)] = 0.2045` first-sound→BAO projection FORM)
- observed fractional peak shift: `Δr_s/r_s = Δk/k = Δθ_s/θ_s = s_b · A_eff,b` (NOT `s_b` alone)
- S94 S-1 numbers (Sage-QQ exact): B1 `A_eff = 17689/2325625 = 0.0076` → shift **0.14452%**; B3 `A_eff = 0.0233` → shift **0.44290%**. The naive 19% is the substrate-INTERNAL split (Reading-S, container-thinking).

**Verdict pattern**: B1-dominant 0.14% is OUTSIDE DESI DR2 ruler (0.24%, `researchers/Cosmic-Web/19`) and OUTSIDE DESI per-tracer (~1–3%, `researchers/Mack/30`). Below current galaxy-BAO peak-position reach.

**Amplitude-vs-position caveat**: a peak-POSITION translation is not a detection forecast. The substrate channel imprints at suppressed A_FS-amplitude as an ADDITIONAL feature, not a displacement of the dominant photon-baryon peak. Planck `100θ_*=1.04077±0.00032` (0.031%) is the recombination ruler, NOT directly shifted by the internal split.

**The genuinely-distinctive live channel** for the two-speed structure is the S43 first-sound ring at **r₁ = 325.3 Mpc (k₁ = 0.0193 Mpc⁻¹)**, NO LCDM counterpart, amplitude-gated (Γ_eff=0.99970 leakage vs S43 A_FS=0.204 imprint). Carry-forward `CF-S95-BAO-TWO-SPEED-AMPLITUDE-TRANSPORT` converts the position sensitivity-bound into an amplitude detection-forecast.

**Canonical data home**: the observational numbers + Row #67 QUALIFY disposition live in `sessions/framework/registry/falsifier-master-inventory.md` Row #67 (AMRI discipline — this memory holds the METHOD, not the data table). Compute: `computations/session-94/s94_s1_bao_observational_reach.py`. Synthesis: `sessions/archive/session-94/session-94-s1-bao-observational-reach-synthesis.md`.

Links: [[key-constraints]] (observational anchors), the S84 PROVEN `c_T/c_S=2.062` two-speed structure this refines.
