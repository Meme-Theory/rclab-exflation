---
name: register-sourced-gate-machinery-recovery
description: Authoring a register-sourced gate (no prior WP CF) — recover its machinery from the prior session's on-disk producing script via MCP, never an external placeholder
metadata:
  type: feedback
---

When `/rclab-plan` 1c-REGISTERS.CONSUME folds in a **register-sourced** gate (flagged by EVOI/atlas/open-channel, with NO prior-session WP carry-forward), its machinery is NOT inherited from a WP CF block — but it is almost always FULLY recoverable from a prior session's on-disk producing script. Do NOT invent an external-paper placeholder.

**Why**: `substrate-first-canonical-sourcing.md` FORBIDS external-paper canonical pins when a substrate-first source exists. A register-sourced gate looks like it has no machinery source, but the EVOI/atlas flag exists *because* a prior session already touched the observable. The MCP chain `search_knowledge → trace_entity(prior-gate) → query_entity(provenance, prior-script)` locates the prior `s{M}_*.py` whose docstring + pinned constants ARE the substrate machinery.

**How to apply** (the recovery recipe):
1. `search_knowledge` the observable + the FAIL-context gate the register flags.
2. `trace_entity` each prior gate-ID → get the producing `.py` path + npz.
3. `Read` the prior producing script's docstring — it carries the substitution chain, the pinned substrate constants (in `# (local)` form), and the input-SHA block. THIS is the machinery to PRDR-pin.
4. Pin the prior session's data files (the log/npz that hold the substrate-derived numbers) as Input-SHA entries — compute their real SHA-256 at plan-freeze, not `<computed-at-runtime>` (they are static).
5. The ONLY external pin admissible is the laboratory-IN falsifier threshold (a published observational bound, e.g. DESI Σm_ν<0.072 eV) — that lives in the gate's PASS criterion, and the executor adds it to `canonical_constants.py` via `update_constant` at execution (Class 8.3 write-order), NOT a substrate pin.

**Calibration instance — S99 W3-2 Σm_ν-SEESAW** (register-sourced, EVOI rank-3 + atlas-08 Q18b + open-channel §B4): machinery fully recovered from `s96_matter_seesaw_d5.py` + `s60_lepto_cp_log.txt`. The substrate seesaw is `m_i = Y_i²v²/(2M_i)` with M_R = the B-branch D_K fold energies (M_1=1.004396, M_2=1.078573, M_3=1.170003 M_KK; Majorana texture = KO-dim-6 Pfaffian on H_K⁺ per S96-MATTER-0NUBB), light masses m_1=0 / m_2=0.008678 / m_3=0.049528 eV (normal ordering, S60) ⇒ Σm_ν=0.058206 eV < 0.072 (DESI PASS). `[J,D_K]=0 ⇒ real M_R ⇒ δ_CP∈{0,π}, η_B=0` (T11 structural). DESI 0.072 eV is the sole external pin (gate threshold, not substrate constant). The seesaw-suppression direction (heavier M_R ⇒ lighter m_ν) is the [SIGN] substitution chain.

Related: [[cross_layer_shared_input_covariance]] (a different cross-domain audit recipe).
