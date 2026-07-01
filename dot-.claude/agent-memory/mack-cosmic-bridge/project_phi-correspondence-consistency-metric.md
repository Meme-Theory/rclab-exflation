---
name: phi-correspondence-consistency-metric
description: Phi_correspondence_consistency_ratio field is the |ratio-1| deviation-from-unity metric (F-image inconsistency), NOT a bare ratio — convention-translation note for §VII.AV-class disambiguation/Stage-2 audits
metadata:
  type: project
---

The `Phi_correspondence_consistency_ratio` field emitted by layer-attribution / F-image-disambiguation gates (canonical instance: `S92-W3-CF-S92-W5-1-C-VII-AV-LAYER-ATTRIBUTION-DISAMBIGUATION`, npz `s92_w3_9_vii_av_layer_attribution_disambiguation.npz`) is the **deviation-from-unity metric** `|ratio - 1|`, NOT the bare ratio.

Worked check (S93 W3-6 Axis-B): two candidate F-images B_LAYER_A = 375.2271 (Cell II OP-PROJ — see [[vii-u-2-corner-partition-and-stage2-caught-defect]]) and |B_LAYER_B| = F_image = 7.046336 (Cell IV STATE-PROJ). Bare ratio = 375.2271/7.046336 = **53.2514**; recorded `Phi_correspondence_consistency_ratio` = **52.2514**; the difference is exactly **1.0** => the field is `(bare_ratio - 1)`.

**Why:** the discriminator semantics are "F-image-consistent IFF metric <= phi_info_ceiling (0.3); else F_IMAGE_INCONSISTENT => MANDATORY split." If two values were genuine regulator-class F-images of ONE observable the ratio would be ~1 and the consistency metric ~0. The `-1` makes 0 mean "consistent." `phi_pass_ceiling=0.1`, `phi_info_ceiling=0.3`.

**How to apply:** when auditing a §VII.AV-class slot-split or any F-image-consistency / layer-attribution verdict, do NOT recompute the bare ratio and compare to the recorded field expecting equality — subtract 1 first. The MANDATORY-split verdict itself is robust to the exact metric definition when the metric is >> ceiling (52.25 and 53.25 both exceed 0.3 by >2 OOM), but the audit-trail number reconciles ONLY under the `|ratio-1|` reading.

**Companion lesson (Stage-2 cross-axis JSON schema drift):** the two Stage-2 cross-reviewers (Axis-A vdd, Axis-B mack) wrote schematically DIFFERENT verdict JSONs — different sub-slot key spelling (`OP-PROJ`/`STATE-PROJ` vs `OP_PROJ`/`STATE_PROJ`), different clause-group names (`single_axis_clauses_axis_A` + `joint_clauses_axis_A_view` vs `axis_B_single_axis_clauses` + `joint_clauses`), and different JOINT-clause key strings. The aggregation/emission script MUST pair JOINT clauses by **semantic identity** (bridge-map <-> bridge-map; orthogonal-companion <-> orthogonal-companion), not exact key string, and walk substrate-input-orthogonality keys **key-path-aware** (a `did_NOT_load`/`reserved` field's path tokens must NOT count as loaded inputs). See `computations/session-93/s93_w3_6_vii_av_stage_2_cross_axis_verify.py`.

Related: [[reference_key-constraints]] (registry data home), `cross-pillar-bridge-anatomy.md §"Composite Bridge-Map Dimensional-Class Admissibility"` (the Phi-correspondence is the §VII.BA T-taxonomy F-image consistency test).
