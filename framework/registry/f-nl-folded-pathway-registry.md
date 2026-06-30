# f_NL_folded Pathway Registry

Created: S86-W13 (P10) — `S86-FNL-FOLDED-PATHWAY-REGISTRY`.

Authority: this file is THE authoritative registry for framework f_NL_folded predictions across all pathway derivations. Master falsifier-inventory Row #9a PROJECTS this registry. Downstream substrate-prediction citations of "the framework's f_NL_folded prediction" MUST specify which sub-channel pathway they invoke.

Run timestamp: 2026-04-26T22:12:13+00:00.

Producing script: `computations/s86_w13_p10_fnl_folded_pathway_registry.py`.
Construction log: `computations/s86_w13_p10_fnl_folded_pathway_registry.json`.
Audit SHA-256 (closure): `2f0cc965743dd95b9e0e3797179422527c66a8cf73df75ca1345fbbc1e093ec3`.

## Methodology

The framework predicts `f_NL_folded` via THREE methodologically-distinct
pathways. Each pathway computes the three-point GGE-quasiparticle coupling
in the folded triangle limit via a different reduction of the substrate
inter-band coherence. The three values are NOT competing predictions of
competing models; they are three distinct sub-channel projections of the
SAME substrate observable. The registry documents each pathway with its
own scheme + convention + L_max + 64-char SHA so downstream gates can
cite the SPECIFIC pathway, not a conflated average.

Substrate-framing reminder (per `.claude/rules/phononic-framing.md`):
`f_NL_folded` IS the three-point coupling among GGE quasiparticles in the
folded triangle limit (k_1 + k_2 = k_3), projected from substrate inter-band
coherence onto post-transit acoustic modes. It is NOT a measurement of an
"inflaton non-Gaussianity in a curved-spacetime container" — the substrate
is logically prior, and the folded shape arises from pair-momentum
conservation in Bogoliubov pair production at the fold.

## Pathway Table (canonical 8-column form)

| Pathway ID | f_NL_folded | scheme | convention | L_max | source_gate | content_sha256 | audit_sha256 |
|:-----------|:-----------:|:------:|:----------:|:-----:|:------------|:--------------:|:------------:|
| S82-GGE-equilateral | 0.0547 | GGE-equilateral | k-uniform | 10 | S82 W3-4 GGE-FNL-CHANNEL | `fe8c7d0e6b96187d5139a78adbea67a67736d75e555488fd9aa4c47889b483c9` | `2f0cc965743dd95b9e0e3797179422527c66a8cf73df75ca1345fbbc1e093ec3` |
| S67-GGE-folded | 0.129 | GGE-folded | substrate | 10 | S67 GGE-BISPECTRUM-67 | `80699ca912fd945fef92d2b4e9d883955dae983818fd55917e93055a2ec495f4` | `2f0cc965743dd95b9e0e3797179422527c66a8cf73df75ca1345fbbc1e093ec3` |
| W9-3-analytic-template-folded | 0.7685 | analytic-template | Fisher-cosine | 10 | S85 W9-FOLDED-TRIANGLE-21CM-SHAPE | `d0f08fb302eb13fc5779ca608c5c5b532ef38329e286df991bf5434510d87c1c` | `2f0cc965743dd95b9e0e3797179422527c66a8cf73df75ca1345fbbc1e093ec3` |

## Pathway Comparison

The three values 0.0547 / 0.129 / 0.7685 span a factor of 14 across the
three pathways. The spread reflects methodologically-distinct sub-channel
projections, not measurement uncertainty:

- **S82 GGE-equilateral (0.0547)**: equilateral-shape projection of the
  GGE quasiparticle bispectrum in the Path-B coherent reduction at the fold.
  k-uniform sampling convention; integrates the Bogoliubov-sudden inter-band
  three-point function across the post-transit acoustic spectrum. Source:
  S82 W3-4 GGE-FNL-CHANNEL PASS.

- **S67 GGE-folded (0.129)**: GGE diagonal channel evaluated at the folded
  triangle (k_1 + k_2 = k_3) via Bogoliubov pair Poisson statistics,
  1/sqrt(N_pair) = 1/sqrt(59.8). Substrate convention. Sole pathway whose
  shape is unique to GGE pair-momentum conservation — no single-field
  inflation model produces this signature. Source: S67 GGE-BISPECTRUM-67
  INFO (working paper §W2-C; pre-S81 verdict, content SHA from producing
  script `s67_gge_bispectrum.py`).

- **W9-3 analytic-template-folded (0.7685)**: analytic-template projection
  via the delta-function-ridge integral with a 2%-k window, Fisher-cosine
  convention. Captures the sharp folded-shape ridge in the template
  bispectrum that 21-cm interferometers can resolve at k_max ~ 10^5.
  Source: S85 W9-FOLDED-TRIANGLE-21CM-SHAPE PASS.

Cross-reference: master falsifier-inventory `f_NL_folded` row (Row #9a in
`sessions/framework/registry/falsifier-master-inventory.md`) PROJECTS this registry.
Downstream gates citing "the framework's f_NL_folded prediction" must name
the specific pathway (S82-GGE-equilateral / S67-GGE-folded / W9-3-
analytic-template-folded), not an arithmetic average across the three.

## Detector Correspondence

Each pathway has a distinct detector-discriminability profile. The
dominant pathway determines which experiment is the primary discriminator:

| Detector | sigma(f_NL_folded) | best discriminates pathway | source |
|:---------|:------------------:|:---------------------------|:-------|
| Planck 2018 | ~5.7 (folded) | none — all 3 pathways consistent | Planck Coll. (-2.5 ± 5.7) |
| CMB-S4 | 6.9 (folded) | none — all 3 pathways below sensitivity | S68 CMBS4-FNL-FORECAST-68 |
| 21-cm interferometric (l_max ~ 10^5) | resolves W9-3 ridge | W9-3-analytic-template-folded | S68 CMBS4-FNL-FORECAST-68 |
| SKA-1 (folded triangle) | 0.15-sigma-equiv. for 0.7685 value | W9-3-analytic-template-folded | S85 W9-3 INFO band |

Detector-pathway pairing:

- The **W9-3 analytic-template-folded** value (0.7685) is the only pathway
  with non-trivial detector discriminability in the 2030s instrument suite.
  SKA-1's 21-cm bispectrum sensitivity at the folded ridge is the primary
  framework-discriminating channel (per S85 W9-3 INFO band, sigma ~ 0.15).
- The **S82 GGE-equilateral** (0.0547) and **S67 GGE-folded** (0.129)
  values are below CMB-S4 and Planck reach; they are detector-sterile in
  the current instrument horizon. Detection would require next-generation
  21-cm or LSS bispectrum surveys at sigma ~ 0.05-0.1.
- All three pathways are presently consistent with Planck 2018 (-2.5 ± 5.7)
  at < 0.6-sigma for any individual pathway.

## Input Pin Map (audit)

```json
{
  "framework_directory_listing": "65f40866cc02393514b48fc977610da3c60701b62912316007fd38c7c8fc9384",
  "project_s67_gge_bispectrum.md": "b1fce98cf1347f04438bdfc2a1b504d53fc3393d393d11825a4ae9be29026590",
  "project_s82_w3_4_gge_fnl.md": "e5d8618eb677f005c6560ca950f4b805aec5d4aedf93220d8f952d924bbb8d73",
  "s67_gge_bispectrum.py": "80699ca912fd945fef92d2b4e9d883955dae983818fd55917e93055a2ec495f4",
  "s82_gate_verdicts.txt": "21ba45cbab42305bbe2c62d1c0ed94301e9b2644ef48c3d4b6315409067f5b89",
  "s85_gate_verdicts.txt": "1993c0e6ec6aeaef79721d4f7ad11c1bb60b06f8f3a5598d8a8d1f051ee67223",
  "session-67-results-workingpaper.md": "fafa612f87f1a25e61fee25ff48aecc89a182d7ad8da6a16187ad61fd007d560"
}
```


## Orphan-Pathway Sub-Row Landing (S88 W8-97)

Row #9a indicates orphan-pathway sub-row landing per S88 W8-97 (S87 W14-4 follow-up).

Context: at S87 W4-* the master falsifier inventory split the previously-bundled (pre-split) row ('1 observable, 3 pathway projections') into laboratory-IN Row #9a (3-pathway projection of the CMB / 21-cm bispectrum, projected from substrate-IS phi_3 cocycle under the HKR boundary map) AND substrate-IS Row #9b (phi_3 in HC^3(A_K), rank-3 Hochschild cocycle / 3-pt-connected vertex; CF-25 STAGE-1-CANDIDATE Channel-3 anchor). This pathway registry projects the LAB-IN side ONLY (Row #9a). For substrate-IS Row #9b provenance, consult `falsifier-master-inventory.md` Row #9b cell + Row #9b-F sub-row + Row #9b.audit. Per `cross-pillar-bridge-anatomy.md` 5-anatomy + 3-level ladder, this registry's three pathway entries (S82-GGE-equilateral, S67-GGE-folded, W9-3-analytic-template-folded) are the laboratory-IN Element 2 OE-form components ∫ d k Tr(...) projected from the substrate-IS phi_3 cocycle Element 1 Hochschild pairing.

Cross-link to `falsifier-master-inventory.md`: this registry projects Row #9a (laboratory-IN side); see also Row #9a-S sub-row (co-coordinates of pathways B + C on the shared N_pair_eff=59.8 1-D sub-manifold) and Row #9a.audit (full-64-hex per-pathway pins preserved verbatim from W14-4).

Provenance: S88 W8-97 (`S88-CF-28-ORPHAN-FNL-PATHWAY-REGISTRY-UPDATE`); method per plan `sessions/session-plan/session-88-plan-w8.md` §W8-97; executor gen-physicist sole writer per `feedback_mack-bridge-role.md` (falsifier-master-inventory.md untouched on this gate; mack-cosmic-bridge remains sole writer of that file).

---

End of registry. Authority: S86 W13-2.
