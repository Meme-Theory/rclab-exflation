# Session 96 Wave 5 — Geometry / Causal Structure / Transition Order (Results Working Paper)

**Session**: 96 | **Wave**: 5 | **Plan**: session-96-plan-w5.md | **Theme**: Geometry / causal-structure / transition-order carry-forwards from the capstone-review panel (cluster C5 meta-hygiene + the geometric §V blocks of sp / landau / berry / kk). Seven GEOMETRIC/PARTICLE-class gates resolving the transition-order (E13/E17) reconciliation, the asymmetric acoustic-white-hole Penrose diagram, the τ→∞ Petrov/CMPP classification, the WCH/CCC reading, the off-Jensen Chern number, the gauge-group sourcing reconciliation, and the M_KK-bracket → a₀ propagation. Held substrate-first: causal structure / Penrose type / Petrov type / topology are EMERGENT from how the a₂ spectral weight distributes — never a pre-existing 4D container.

## Gate Sections

### §W5-1. S96-GEOM-LANDAU-FE-ORDER (schwarzschild-penrose-geometer)

**Status**: COMPLETED
**Gate ID**: `S96-GEOM-LANDAU-FE-ORDER`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (F(η;τ) is a functional of D_K(τ)'s spectral data; the order parameter is a curvature/occupation observable of the fabric)
**Agent**: `schwarzschild-penrose-geometer`
**Hypothesis**: The τ_fold transition is sector-split — the pairing sector (η = BdG gap amplitude) has a CONTINUOUS (zero-critical-coupling van-Hove, E13) onset, while any first-order (E17) discontinuity lives in the MODULUS (τ) sector or a derived band-occupation order parameter; the most general Ad U(2)-invariant Landau free energy F(η;τ) reproduces this split.
**Plan reference**: `sessions/session-plan/session-96-plan-w5.md` §W5-1 (machinery pin, thresholds, substitution chain source).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

- **script** `computations/session-96/s96_geom_landau_fe_order.py` — EXISTS (27,331 B). `grep` must_contain:
  - `from canonical_constants import` → `from canonical_constants import (   # noqa: E402`
  - `append_verdict` → `def append_verdict(verdict: str, value, audit_sha: str, content_sha: str,` + `append_verdict(res["verdict"], res["value"], audit_sha, content_sha,`
- **data** `computations/session-96/s96_geom_landau_fe_order.npz` — EXISTS (24,508 B; full-float64 F(η;τ) scan arrays per sector + classification flags + dual-SHA).
- **plot** `computations/session-96/s96_geom_landau_fe_order.png` — EXISTS (230,780 B; 4-panel: pairing F(η) continuous onset / van-Hove I(Δ)→∞ / modulus S_SA(τ) monotone / occupation catastrophe cusp).
- **verdict line** `computations/session-96/s96_gate_verdicts.txt` (line 103) — matches `^S96-GEOM-LANDAU-FE-ORDER:.* audit_sha256=[a-f0-9]{64}`:
  `S96-GEOM-LANDAU-FE-ORDER: INFO -- value='sector-split:pairing-CONTINUOUS(E13,g_crit=0)+occupation-FIRST-ORDER(E17,cubic!=0)+modulus-MONOTONE(E7)' scheme=SA-zeta convention=ABSOLUTE L_max=10 audit_sha256=8a1744b23952ce3f6a2baeb6f700211c835e9fab38fdfcd8550a7315af3d8175 content_sha256=8b812a8d19a94774f9ccc4ae2b09671984316c56b27a9382baa3ca746b0df02f schema_version=S84+`
  - dual-SHA companion row (line 104): `# audit_sha256_short=8a1744b23952ce3f content_sha256_short=8b812a8d19a94774 # S96-GEOM-LANDAU-FE-ORDER dual-SHA companion row`
  - schema-v2 3-tuple companion row (line 105, REQUIRED — [SIGN] trigger): `# sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID # S96-GEOM-LANDAU-FE-ORDER 3-tuple annotation (schema-v2)`
  - audit_sha256 unique across the verdict file (grep count = 1; no sig_5 collision).

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script; query-first discipline per `.claude/rules/knowledge-index-usage.md`):

- `search_knowledge('Landau free energy transition order first-order van Hove BCS modulus')` → **Perturbative Exhaustion Theorem (S22c, D4 PERMANENT)** = "standard first-order phase transition thermodynamics with metastable branches"; `landau-synthesis.md` already records the E17 first-order verdict + E13 van-Hove DOS + Delta_BCS + S_SA(τ)=a₀−a₂+a₄ inputs. The gate's job is the explicit F(η;τ) reconciliation these source-docs name but never write.
- `search_knowledge('first-order phase transition fold E17 latent heat occupation')` → catastrophe normal form `F(x;λ,μ)=x⁴+λx²+μx` (session-22-berry-collab; Paper 09 CO-2); `latent_heat=0.00111`, `Delta_jump=0.318`, `c=0.007 (cubic, Z₃-invariant from L-9)` (s33b_gate_verdicts.txt). The occupation-sector first-order carrier.
- `trace_entity('Perturbative Exhaustion Theorem')` → PROVEN/PERMANENT (S19d, S22c; closed_mechanism + atlas-07-permanent-results D4); H1–H5 verified, F_pert is NOT the true free energy ⇒ first-order. Cubic `V'''(0)≠0`.
- `search_knowledge('RG-BCS-35 zero critical coupling g_critical continuous onset van Hove')` → **RG-BCS-35 PROVEN** (S35, atlas-07): "any g>0 flows to strong coupling, 3 independent methods"; **Van-Hove-Zero-Critical-Coupling S28c PROVEN**: `g_critical=0`, 43–51× enhancement. The pairing-sector continuous carrier (E13).
- `get_constant('Delta_BCS')` → 0.4642547394830737 (R-PROTECTED, S70 BCS-GAP-CANONICAL-70). Sets the pairing η-scale + scan range η∈[0, 2·Delta_BCS].
- `get_constant('tau_fold')` → 0.19 (S12/S42 CONST-FREEZE-42).
- `get_constant('E_cond')` → −0.13685… (S36 ED-CONV-36, 8-mode); `get_constant('Delta_B1')` → 0.371795 (S53, B1-band GL gap = occupation scale).
- `list_constants('S_fold|dS|d2S')` → `dS_fold=58672.80241318`, `S_fold=250360.677`, `d2S_fold=317862.849` (E7 modulus-monotonicity slope at fold). `a_{0,2,4}_FW_zeta = 6440.0 / 2776.165389 / 1350.7216` confirmed in canonical_constants.py.
- **Sage MCP pre-flight** (`sage_eval`): (i) van-Hove band-edge integral `I(Δ)~Δ^{−1/2}·J`, `J=½β(¼,¼)=3.708149` Sage-exact (finite) ⇒ diverges as Δ→0 ⇒ g_critical=0; (ii) U(2)-invariant `F_pair=A·s+B·s²` (s=|η|²) — no smooth cubic invariant ⇒ continuous onset; (iii) occupation `F_occ=a x²+c x³+b x⁴` with c=0.007≠0 ⇒ 3 real critical points {−11,10,0} ⇒ double-well first-order.
- **PRE-CLOSED status**: the two halves are each PRE-CLOSED (RG-BCS-35 PROVEN + Perturbative Exhaustion S22c PERMANENT). This gate is NOT a rediscovery — it COMPOSES the two PROVEN theorems into one closed-form F(η;τ) and pins which sector carries the discontinuity (the un-written reconciliation `landau-synthesis.md §IV.1/§V.1` names as the ripest harvest).

**Verdict**: **INFO** — value `sector-split:pairing-CONTINUOUS(E13,g_crit=0)+occupation-FIRST-ORDER(E17,cubic!=0)+modulus-MONOTONE(E7)`; scheme=SA-zeta, convention=ABSOLUTE, L_max=10. schema-v2 3-tuple `sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID` ⇒ composite collapse → INFO (magnitude=PASS but the order is genuinely two-sector, so the pre-registered INFO_meaning "order is sector-dependent and both readings coexist" fires — the most-likely outcome per the substitution chain). dual-SHA: `audit_sha256=8a1744b23952ce3f6a2baeb6f700211c835e9fab38fdfcd8550a7315af3d8175`, `content_sha256=8b812a8d19a94774f9ccc4ae2b09671984316c56b27a9382baa3ca746b0df02f` (full 64-char).

**Results**:

**The closed-form Ad U(2)-invariant Landau free energy F(η;τ)** — three sectors, three order parameters, ONE landscape:

```
F(η; τ) = F_pair(|η_Δ|²; τ)  ⊕  F_mod(τ)  ⊕  F_occ(η_occ; τ)

  PAIRING sector   F_pair = A(τ)|η_Δ|² + B|η_Δ|⁴          (η_Δ = Δ, BdG gap amplitude)
                   U(2)-invariant ⇒ only invariants s=|η_Δ|², s² ; NO smooth cubic invariant.
                   A(τ) driven < 0 at the fold by the van-Hove DOS ⇒ η_min=√(−A/2B) smooth from 0.
  MODULUS sector   F_mod(τ) = S_SA(τ) = a₀^ζ − a₂^ζ + a₄^ζ   (η = τ, the Landau order parameter)
                   strictly monotone (no interior well).
  OCCUPATION sector F_occ = a·x² + c·x³ + b·x⁴             (x = band-occupation / condensate amp.)
                   cubic c ≠ 0 (Z₃-invariant, Perturbative Exhaustion) ⇒ catastrophe cusp.
```

**4-tuple**: `(value='sector-split:pairing-CONTINUOUS(E13,g_crit=0)+occupation-FIRST-ORDER(E17,cubic!=0)+modulus-MONOTONE(E7)', scheme=SA-zeta, convention=ABSOLUTE, L_max=10)`.

**Sector classification (the gate's decisive numbers)**:

| Sector | Order parameter η | F(η) form | Order | Decisive number |
|:-------|:------------------|:----------|:------|:----------------|
| **PAIRING** | η = Δ (BdG gap amplitude) | `A\|η\|²+B\|η\|⁴`, U(2)-invariant, **no cubic** | **CONTINUOUS** (E13) | g_critical = 0 (I(Δ) grows as Δ→0); 1 minimum/phase; η_min = Δ_BCS = 0.4643 |
| **MODULUS** | η = τ (the dial) | `S_SA(τ)=a₀−a₂+a₄` | **no transition in τ** (monotone) | dS/dτ\|_fold = +58,672.8 > 0 (E7); **0** interior wells |
| **OCCUPATION** | x = band occupation / condensate amp. | `a x²+c x³+b x⁴` catastrophe cusp | **FIRST-ORDER** (E17) | cubic c = 0.007 ≠ 0; **2** minima; crit pts {−10.87, 0, 10.39}; Δ_jump=0.318, L₉=0.00111 |

**CC1 — BCS gap-equation band-edge divergence ⇒ g_critical = 0 (pairing CONTINUOUS, E13)**. Sage-exact: with van-Hove DOS `g(ω)=(ω−ω_min)^{−1/2}`, the gap-equation integral `I(Δ)=∫ g(ω)/√(ω²+Δ²) dω` scales as `Δ^{−1/2}·J` with `J=½β(¼,¼)=3.708149` (finite). As Δ→0, `I(Δ)→+∞`, so `g·I(Δ)=1` has a solution Δ>0 for **any** g>0 ⇒ g_critical=0. Numerically `I(Δ)` rises monotonically from Δ=1 to Δ=0.001 (grid-cutoff `g_critical_numeric=2.87×10⁻³`, → 0 as the cutoff is removed). g_critical=0 ⇒ Δ(g) is a SMOOTH onset from Δ=0 ⇒ pairing transition is CONTINUOUS (second-order-like). [PROVEN: RG-BCS-35, S28c, 3 methods]

**CC2 — modulus action S_SA(τ)=a₀−a₂+a₄ monotonicity (no τ-well, E7)**. With a₀^ζ=6440.0, a₂^ζ=2776.165389, a₄^ζ=1350.7216, S_SA(fold)=5014.5562; the canonical slope dS/dτ|_fold=+58,672.8 > 0 (E7, 9,600/9,600 PROVEN). The local quadratic model S_fold + dS_fold(τ−τ_fold) + ½d²S_fold(τ−τ_fold)² is strictly increasing across τ∈[0.05,0.35] (0 interior minima). ⇒ no double-well in τ ⇒ "first-order" (E17), if real, cannot be a τ-well or a pairing jump — it must be a cross-fold discontinuity in a DERIVED order parameter (band occupation).

**The E13/E17 sector-reconciliation substitution chain (substituted numbers)**:
- Step 1: pairing η := Δ (Delta_BCS=0.4642547, R-protected).
- Step 2: van-Hove DOS g(ω)=(ω−ω_min)^{−1/2} (1D cusp of D_K(τ) spectrum).
- Step 3: BCS gap equation 1 = g∫dω g(ω)/√(ω²+Δ²).
- Step 4: substitute Step 2 → Step 4: I(Δ) = Δ^{−1/2}·½β(¼,¼) diverges as Δ→0 ⇒ solution for ANY g>0 ⇒ g_critical=0 (PROVEN S28c/RG-BCS-35).
- Step 5: g_critical=0 ⇒ Δ(g) smooth onset, NOT a jump ⇒ **pairing transition CONTINUOUS** [direction +].
- Step 6: separately, S_SA(τ) monotone (dS/dτ|_fold=+58,672.8>0, E7) ⇒ no τ-well ⇒ first-order (E17), if real, is a discontinuity in band occupation ACROSS the fold (catastrophe cusp: cubic c=0.007≠0 ⇒ 2 competing minima, Δ_jump=0.318).
- **Conclusion**: E13 (continuous van-Hove BCS pairing onset) and E17 (first-order occupation jump) are **SECTOR-DISTINCT statements, not a contradiction**. The capstone §5.2 "first-order (E17)" is scoped to the OCCUPATION sector; the pairing-η onset is CONTINUOUS; the modulus τ has no well at all.

**schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple**: `sign_verdict=PASS` (all three directional predictions of the substitution chain match: pairing CONTINUOUS [I grows as Δ→0], modulus MONOTONE-up [dS/dτ>0], occupation FIRST-ORDER [cubic c≠0]); `magnitude_verdict=PASS` (sector-split established — single closed-form F(η;τ) + all three sectors classified); `regime_verdict=VALID` (Landau extremization is exact closed-form; the van-Hove (−1/2) cusp and E7 monotonicity both hold across the whole intended window).

**Artifacts**: `s96_geom_landau_fe_order.py` / `.npz` / `.png` (paths in Output Artifacts above). dual-SHA full 64-char: audit_sha256=`8a1744b23952ce3f6a2baeb6f700211c835e9fab38fdfcd8550a7315af3d8175`, content_sha256=`8b812a8d19a94774f9ccc4ae2b09671984316c56b27a9382baa3ca746b0df02f`.

**Substrate framing (GEOMETRIC)**: η is NOT a field in a container — it is the BdG gap amplitude (a spectral observable of D_K(τ)) or the band-occupation (a Peter-Weyl sector cardinality of D_K(τ)). F(η;τ) is a functional of the fabric's OWN spectral data: D_K eigenvalues → spectral moments (a₀,a₂,a₄) → S_SA(τ) modulus action + van-Hove DOS g(ω) → F(η;τ). The "transition order" is a statement about the SHAPE of this spectral free-energy landscape, NOT about a phase transition happening IN a pre-existing thermodynamic box. The first-order/continuous distinction is the substrate's own answer to whether the cascade SU(3)²/ℤ₃ → (SU(3)×SU(2)×U(1))/ℤ₆ proceeds by a discontinuous band-occupation jump (occupation sector, E17) or a smooth pairing onset (pairing sector, E13) — and the answer is: **both, in different sectors**. Direction of explanation held substrate-first throughout: the catastrophe cusp and the van-Hove cusp are both properties of the EMERGENT free-energy landscape of D_K(τ), never imported from an external thermodynamics.

---

### §W5-2. S96-GEOM-PENROSE-2CONE (schwarzschild-penrose-geometer)

**Status**: COMPLETED
**Gate ID**: `S96-GEOM-PENROSE-2CONE`
**Trigger**: `[VERIFY]` (carries a directional cone-width claim ⇒ schema-v2 3-tuple companion row required)
**Classification**: **GEOMETRIC** (conformal compactification of the emergent causal structure of the fabric)
**Agent**: `schwarzschild-penrose-geometer`
**Hypothesis**: The §6.2 acoustic white hole admits a null-consistent, visually asymmetric Penrose diagram — ONE post-genesis entry sonic surface (τ₀≈0.1125, |κ_entry|=18.52 M_KK), an UNBOUNDED supersonic expulsion region toward ℐ⁺, no future-trapped exit horizon / no bounce, TWO distinct null cones (scalar on g_acoustic, tensor on g_M decoupled by [T3] β_T=0) — reproducing the SCALE-FACTOR-54 conformal-time ordering η=∫dτ/a(τ).
**Plan reference**: `sessions/session-plan/session-96-plan-w5.md` §W5-2.

**Verdict**: **PASS** — composite collapse PASS from the 3-tuple (sign=PASS, magnitude=PASS, regime=VALID). Canonical line (latest non-superseded, `audit_sha256=a16ab32351e9fbfd2976a6750a4e82f06169fcd8c8475c6092185869cee01ed9`):
```
S96-GEOM-PENROSE-2CONE: PASS -- value='asym_white_hole;N_zeros=1;single_entry=True;open_exit=True;tau0=0.112466;kappa_entry=18.5201_MKK;scalar_narrower=True;hdist_ratio=229.4794x;eta_monotone=True;eta_entry=0.090720<eta_fold=0.133811;labels=5;tikz=exflation-asymmetric-white-hole.tex_supersedes=...' scheme=BLV-acoustic convention=conformal-compactification L_max=N/A audit_sha256=a16ab323...ee01ed9 content_sha256=9a0cad9c...d1bcc674 schema_version=S84+
# sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID  # S96-GEOM-PENROSE-2CONE 3-tuple (schema-v2)
```
The PASS conjunction (operator.form) all holds: (i) artifact-existence-with-content (TikZ has all 5 conformal-infinity labels + entry sonic surface + censored τ→∞ boundary + both cones); (ii) null-consistency (scalar cone narrower than tensor; entry surface at 45° on the scalar cone; tensor cone a distinct slope); (iii) asymmetry visually unambiguous (N_zeros=1 single entry surface, open supersonic exit, no symmetric throat); (iv) reproduces the S55/SCALE-FACTOR-54 conformal-time ordering. The diagram passed the /penrose-diagram skill Author→Compile→Review loop (3 cycles, converged: clean xelatex compile + PDF rubric-checked at each cycle; entry-label/callout-overlap/worldline-clip fixes applied across iterations 1→3).

**Verdict (4-tuple)**: `(value=construction-PASS [asymmetric two-cone white-hole diagram null-consistent], scheme=BLV-acoustic, convention=conformal-compactification, L_max=N/A)`.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML — content presence only, no length targets):

| Artifact | Path | must_contain | Verified |
|:---------|:-----|:-------------|:---------|
| script | `computations/session-96/s96_geom_penrose_2cone.py` | `from canonical_constants import`, `append_verdict` | ✓ (both present; grep below) |
| data | `computations/session-96/s96_geom_penrose_2cone.npz` | (exists) | ✓ |
| plot (primary; canonical TikZ) | `figures/penrose/exflation-asymmetric-white-hole.tex` | (exists; compiles clean → `.pdf`/`.png`) | ✓ |
| verdict_line | `computations/session-96/s96_gate_verdicts.txt` | `^S96-GEOM-PENROSE-2CONE:.* audit_sha256=[a-f0-9]{64}` + dual-SHA companion + schema-v2 3-tuple | ✓ (canonical line + companion + 3-tuple present) |

Auxiliary (not in plan `output_artifacts:` but produced): `computations/session-96/s96_geom_penrose_2cone.png` (diagnostic: η(τ)-ordering + cone-width bar); `figures/penrose/exflation-asymmetric-white-hole.pdf` (compiled diagram).

**MCP Pre-Compute Audit** (query-first discipline; per `.claude/rules/knowledge-index-usage.md`; queries executed BEFORE writing the script):
- `get_constant('c_Gold')` → **0.915** (S52 GL-JOSEPHSON-52; Goldstone scalar sound speed, M_KK units). Used for the scalar cone.
- `get_constant('c_fabric')` → **209.97368021** (S42 s42_gradient_stiffness; substrate sound speed ~ c_geom). Used for the tensor cone.
- `get_constant('c_BLV')` → **0.485** (S64 s64_sound_speed; BLV scalar c_s; Mach_max=v_transit/c_BLV=13.75).
- `get_constant('tau_fold')` → **0.19** (S42 CONST-FREEZE-42; van Hove fold).
- `search_knowledge('acoustic white hole asymmetric entry sonic surface kappa_entry surface gravity 6.2')` → S95-W4-1 entry-surface ledger; S85 W6-1 formalized causal-disconnect (PROVEN, Diagram J); `transit-synthesis.md` 6-walls `κ_entry=+18.52 M_KK`.
- `trace_entity('SCALE-FACTOR-54')` → gate PASS, `eta=∫dτ/a(τ)`, q(τ): −0.97→+0.81 (Connes-distance **proxy**, NOT a_eff). Used for the conformal-time ordering check.
- `search_knowledge('S95 W4 white hole kinematic consistency tau0 kappa0 asymmetric open exit six walls')` → **S95-W4-1 npz**: `N_zeros=1`, `root_taus=[0.1124658]`, `kappa_values=[18.520134]`, `monotone_supersonic_exit=True`, `composite=PASS`. This is the canonical entry-surface ledger this gate renders.
- **NOT PRE-CLOSED as a figure**: the §6.2 asymmetric-white-hole *conformal diagram* does not exist in `Phononic-Penrose-Diagrams.md`; Diagram C is a bi-metric two-panel comparison (geometric vs acoustic cone, no white-hole entry/exit architecture), Diagram J is a plain symmetric Minkowski-diamond stub (no entry surface, no open-exit asymmetry, no τ-axis, no second cone). This gate produces the genuinely new single conformal compactification that closes the §6.2 figure gap.

**Source-reconciliation note (κ_entry sign — pinned + disclosed)**: the plan and `transit-synthesis.md` cite `κ_entry = +18.52 M_KK`; the S95-W4-1 npz `kappa_values = +18.520134` (RATIO convention, magnitude). An earlier kinematic emission (S95-W4-1 verdict-file line) recorded `kappa0 = −18.442205` under the ingoing-null sign convention. A white-hole surface gravity carries a sign that flips with the ingoing/outgoing null normalization; the **magnitude ~18.52 M_KK is convention-independent** and is what the diagram annotates. The diagram is sign-convention-agnostic (it labels the entry surface, not a signed κ). I used the npz canonical value `18.520134` (= the plan's `+18.52`) directly.

**Results**:

*The cone-width substitution chain (the [SIGN] directional claim) — scalar cone NARROWER than tensor cone:*
- Step 1: `c_Gold   = 0.915 M_KK` [canonical_constants.py; Goldstone scalar sound speed]
- Step 2: `c_fabric = 209.97368021 M_KK` [canonical_constants.py; substrate fabric speed ~ c_geom (tensor cone)]
- Step 3: opening ratio `= arctan(c_Gold/c_fabric) / arctan(1)` [tensor cone normalized to 45°]
- Step 4: `= arctan(0.915/209.97368021)/(π/4) = arctan(0.0043577)/0.7853982 ≈ 0.0043577/0.7853982 ≈ 0.005549`; horizon-distance ratio `c_fabric/c_Gold = 209.97368021/0.915 = 229.4794`. Computed: **scalar_angle = 0.249676°**, **tensor_angle = 45.000000°**, **opening_ratio = 5.548347e−03**.
- Step 5: `c_Gold/c_fabric = 4.357689e−03 ≪ 1` ⇒ scalar opening angle ≪ tensor ⇒ the **SCALAR (acoustic) cone is NARROWER** [direction]. `scalar_narrower = True`.
- Conclusion: the scalar cone is **~229× narrower** in horizon distance than the tensor cone. On the diagram the entry sonic surface is drawn at 45° relative to the scalar cone (the cone it is null on); the tensor cone is a distinct shallower slope; by [T3] β_T=0 the tensor sector sees no white hole and crosses the fold freely. This is the asymmetric two-cone structure. (`sign_verdict=PASS`: predicted direction "scalar narrower" matches computed `scalar_angle < tensor_angle`.)

*Null-consistency record (the [VERIFY] consistency conjunction):*
- (a) **Artifact-existence-with-content**: TikZ written (≈9.5 kB); all 5 conformal-infinity labels present (`i⁺`, `i⁻`, `i⁰`, `ℐ⁺`, `ℐ⁻` — `labels_present=True`); entry sonic surface present; censored τ→∞ boundary present (`\tau→∞` + `singularity` zigzag); two cones present (`scalar cone` + `tensor cone`). `artifact_ok=True`.
- (b) **Null-consistency**: entry surface at 45° on the scalar cone (the cone it is null on); the tensor cone is a distinct slope from the same vertex; both cones drawn together so the 229× asymmetry is visible (true ratio labeled numerically per the Diagram-C convention). `null_consistency_ok=True`.
- (c) **Asymmetry visually unambiguous** (cross-checked against the S95-W4-1 entry-surface ledger): `N_zeros=1` (single entry surface, not a symmetric throat); `root_taus=[0.1124658]` (matches pinned τ₀=0.112466); `kappa_values=[18.520134]` (matches pinned |κ_entry|); `monotone_supersonic_exit=True` (open exit toward ℐ⁺, no future horizon). `asymmetry_ok = single_entry ∧ open_exit = True`.
- (d) **Reproduces the S55/SCALE-FACTOR-54 conformal-time ordering** `η(τ)=∫dτ/a(τ)`: with a(τ) interpolated from SCALE-FACTOR-54 onto the dense τ∈[0,0.30] grid (200 pts), `a(τ)>0` everywhere (range [1.0000, 3.0564]); η monotone-increasing (`min dη = 4.919e−04` > tol 1e−6); **η(τ₀=0.1125) = 0.090720 < η(τ_fold=0.19) = 0.133811** ⇒ entry surface precedes the fold in conformal time (`ordering_ok=True`, `reproduces_ordering=True`). NOTE (proxy-conditional caveat per §6.3): SCALE-FACTOR-54 a(τ) is the **Connes-distance proxy**, not a_eff; the monotone η-ordering is reproduced at proxy level. This does not down-grade the construction — the figure's causal architecture (entry surface, open exit, two cones, censored boundary) is independent of the a(τ) normalization; only the numerical η-values carry the proxy tag.

*The diagram (figures/penrose/exflation-asymmetric-white-hole.tex):* a single conformal compactification in (τ-Jensen, conformal-time η) coordinates. Genesis (τ=0 cold-regular) at the past-left i⁻ vertex; the SINGLE entry sonic surface ℋ_entry (blue, 45° on the scalar cone) separates the subsonic pre-entry region (blue fill, left) from the supersonic white-hole interior (red fill, Mach=13.75, anti-trapped analog) which opens FREELY to ℐ⁺ (open exit, no future horizon, no bounce). The two decoupled null cones are shown at a sample interior event: the scalar cone (green, near-vertical, pinched — the acoustic causal diamond closes) and the tensor cone (orange, near-45°, opens freely — the geometric diamond stays open), with the 229× ratio labeled. The censored τ→∞ Kasner boundary (red zigzag, K~e^{4τ}) is held off the physical region by the COSMIC-CENSORSHIP-49 barrier (τ≈0.19). All five conformal-infinity boundaries labeled (i⁺, i⁻, i⁰, ℐ⁺, ℐ⁻). This EXTENDS `Phononic-Penrose-Diagrams.md` and does NOT duplicate Diagram C (bi-metric two-panel) or Diagram J (symmetric-diamond stub).

*Closes the §6.2 figure gap*: the capstone §6.2 described this entirely in prose with no Penrose diagram and no citation to the canonical document. The strongest visual argument for "horizon problem resolved by causal disconnection, not inflationary stretching" and "singularity censored" now exists as a coordinate-invariant conformal diagram. Artifacts: `computations/session-96/s96_geom_penrose_2cone.py` / `.npz` / `.png`; `figures/penrose/exflation-asymmetric-white-hole.tex` / `.pdf`. Dual-SHA full-64-char (`audit_sha256=a16ab32351e9fbfd2976a6750a4e82f06169fcd8c8475c6092185869cee01ed9`, `content_sha256=9a0cad9cab8e248be15c938f1935fcd244c7793440f266fd0bfa9ea4d1bcc674`); three runs across the review loop produced a clean supersession chain (verdict-file lines: original → corrective → latest-canonical) per gate-verdicts.md "Option A".

**Substrate framing**: GEOMETRIC. The Penrose diagram is NOT a picture of the fabric sitting inside a spacetime box. The causal structure is EMERGENT: D_K eigenvalues → a₂ Seeley-DeWitt moment → emergent metric g_M (tensor cone) AND the BLV acoustic metric g_acoustic on the scalar condensate (scalar cone). The two cones are two emergent effective metrics seen by two field sectors (the Kasparov product U_total = 1_M ⊗ U_K, [T3] β_T=0), NOT two observers in one container. The "white hole" is the acoustic causal disconnect: the supersonic transit (Mach 13.75) pinches the acoustic causal diamond at the fold while the geometric diamond stays open — this is why pre/post-transit are causally disconnected (the horizon problem is resolved by DISCONNECTION, not by inflationary stretching of a pre-existing space). Conformal infinity (i⁺, ℐ⁺, i⁰) is the 4D-factor construct; SU(3) is compact and does not reach the conformal boundary. Direction of explanation: substrate spectral-weight redistribution → emergent bi-metric causal architecture → the asymmetric white hole, never a singularity/horizon forming inside a container.

---

### §W5-3. S96-GEOM-TAUINF-PETROV (schwarzschild-penrose-geometer)

**Status**: COMPLETED
**Gate ID**: `S96-GEOM-TAUINF-PETROV`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **GEOMETRIC** (Petrov/CMPP type of the censored singular boundary of the fabric's geometry)
**Agent**: `schwarzschild-penrose-geometer`
**Hypothesis**: The Petrov/CMPP type of the τ→∞ anisotropic Kasner-type singular boundary of the 12D product metric is determined unambiguously (expected continuation of the dynamic Type-G / static Type-D type-invariance theorem; Type N/III would indicate radiative character), AND the timelike(SU(2))/spacelike(ℂ²,U(1)) split is reproduced at the Weyl-spinor Ψ_ABCD eigenstructure level (matching S49 per-block conformal distances ℂ²=2.581989, U(1)=1.290994 within 1e-6).
**Plan reference**: `sessions/session-plan/session-96-plan-w5.md` §W5-3 (extends the PERMANENT S84-W8B-95 type-invariance theorem to τ→∞).

**Verdict**: **PASS** (composite). 3-tuple: `sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`. The τ→∞ Petrov/CMPP type is determined **unambiguously** — the asymptotic emergent-Lorentzian type is **static Type D** (machine-zero min(bw+2)≈5.26×10⁻⁶⁸ at all 12 τ-samples {1.5,…,50}), the Schwarzschild/Kerr algebraic class, in continuation of the PERMANENT S84-W8B-95 static-D result. The SU(2)-timelike / (ℂ²,U(1))-spacelike split is reproduced from the Ψ_ABCD/Weyl-operator block-eigenstructure and the per-block conformal distances match S49 to **|diff| = 0.0** (≪ 1e-6, the strict PASS boundary). The dynamic Type G is a transit-regime cross-check (Type G throughout its resolvable window τ≲5, S84-all-G confirmed) — the modulus is **censored** from reaching τ→∞ (COSMIC-CENSORSHIP-49, barrier τ≈0.19 ≪ τ_NEC≈1.38), so the dynamic type at the singular boundary is physically counterfactual and numerically below round-off (see Results §regime note).

**4-tuple**: `(value='static_tauinf=Type-D-all-12; dynamic_resolvable=Type-G; charA=timelike-SU2,spacelike-C2U1; cd_C2=2.581989; cd_U1=1.290994; K8_slope=4.0000; A3_mult=[20,8]→[15,10,3]', scheme=NP-CMPP, convention=anti-Hermitian-generators-a2-reduction, L_max=N/A)`.
**Dual-SHA (full 64-char)**: `audit_sha256=8f49af075339ccac65f14478b944d57720033de4892e27ed0d785a739c761074`, `content_sha256=978a2dd6718f7adbad70892cd3150b13e01707edffe197d1aa127ad107e02717`. Latest non-superseded canonical line; supersession chain `f260302b → 4789decf → ec803215 → 8f49af07` (see §Methodology note on the regime-misattribution correction).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

- **script** `computations/session-96/s96_geom_tauinf_petrov.py` — EXISTS (63,641 B). `grep -c 'from canonical_constants import'` → **1**; `grep -c 'append_verdict'` → **3**. ✓
- **data** `computations/session-96/s96_geom_tauinf_petrov.npz` — EXISTS (26,352 B); Ψ_ABCD/Λ²(R⁸) 28-eigenvalue stack (12×28), per-block conformal distances, asymptotic-type-vs-τ table, A3 multiplicity, S84 cross-check, 3-tuple. ✓
- **plot** `computations/session-96/s96_geom_tauinf_petrov.png` — EXISTS (232,540 B); 4-panel: (a) K₈,|C|²₈ ~e^{4τ}; (b) per-block conformal distance (causal character); (c) static-D/dynamic-G CMPP with the dynamic resolvable-window boundary; (d) Λ²(R⁸) Weyl eigenvalue spectrum. ✓
- **verdict line** `computations/session-96/s96_gate_verdicts.txt` — `grep -cE '^S96-GEOM-TAUINF-PETROV:.* audit_sha256=[a-f0-9]{64}'` → **4** (chain; latest = PASS). Canonical PASS line + dual-SHA companion row + schema-v2 3-tuple companion row all present (directional timelike/spacelike claim). ✓ Content presence verified; no length targets.

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script):

- `search_knowledge('S84 W8B CMPP Petrov type invariance static D dynamic G')` → **S84-W8B-95-CMPP-PETROV-TYPE-INVARIANCE**: `value=D/D/D/D/D/D/D/D/G/G/G/G/G/G/G/G`, `convention=a2-reduction-4D`, PASS, `sha256=f2cf5c7c…` (the PERMANENT type-invariance baseline this gate extends).
- `search_knowledge('S49 conformal distance per-block SU(2) timelike C2 U(1) spacelike singularity tau infinity')` → **S95-W4-5-SP-12D-SINGULARITY-CENSOR**: `cd_C2=2.581989; cd_U1=1.290994; K12_slope=4.0000; charA=timelike-SU2,spacelike-C2U1` (direct anchor for the conformal distances + Kretschmann exponent).
- `trace_entity('CMPP-TRANSITION-49')` → **CMPP-TRANSITION-49** FAIL: "Type II at all 16 τ; Riemannian signature locks CMPP type" — the **category-error artifact** the plan warns of; corrected by the a₂-reduction Lorentzian classification (A4/S50: Type D). HONORED.
- `search_knowledge('A3 8D Riemannian Petrov classification Type D tau=0 algebraically general multiplicity')` → **A3 / D07 / baseline item 9**: "8D Petrov Classification of Jensen-Deformed SU(3) — Type D at τ=0, algebraically general at τ>0, stable multiplicity {3,4,1,2,4,3,3,8}"; **A4/S50**: "Lorentzian CMPP Type D — corrects Riemannian artifact, Schwarzschild/Kerr class, permanent across all τ".
- `get_constant('tau_fold')` → 0.19 (S12/S42); `get_constant('tau_NEC')` → 1.383 (canonical, S95 W4-5; censoring barrier τ≈0.19 ≪ τ_NEC). `get_constant('G_DeWitt')`-equivalent via `canonical_constants.py:502` → 5.0 (norm = √(5/3) for the conformal-distance integrals).
- **Not PRE-CLOSED**: S84-W8B-95 covers the 8 FINITE τ-points; CONFORMAL-TRANSITION-49 / S95-W4-5 establish the conformal-distance character at the fiber/12D level but NOT the Petrov/CMPP type AT the τ→∞ boundary. This gate is the new structural result extending the type-invariance theorem to the singular boundary.

**Results**:

**1. τ→∞ Petrov/CMPP type (unambiguous: static Type D).** The emergent-Lorentzian CMPP classification of the 12D product metric `ds²=−dt²+a(t)²dx₃²+g_ab(τ)dyᵃdyᵇ` at the 12 τ-samples {1.5,2,3,4,5,6,8,10,15,20,30,50} approaching τ→∞ returns **static Type D at every sample** — the boost-weight +2 fraction is machine-zero (min(bw+2)≈5.26×10⁻⁶⁸, dropping to exact 0.0 at τ≥20 where the magnitude saturates float64), forced by the product topology `M^{3,1}×SU(3)(τ)` (Ψ₂-only spinor content, magnitude-INDEPENDENT). This is the Schwarzschild/Kerr algebraic class, **continuing the PERMANENT S84-W8B-95 static-D result to the singular boundary**. Cross-check: S84 static = `[D×8]`, dynamic = `[G×8]`, audit `f2cf5c7c…` — reproduced exactly.

**2. Ψ_ABCD eigenstructure (Λ²(R⁸) Weyl operator, the spinor analog) + timelike/spacelike split.** The 8D Riemannian Weyl operator on the 28-dim 2-form space Λ²(R⁸) — whose eigenvalue multiplicity IS the A3 classification (the Riemannian analog of the Weyl spinor Ψ_ABCD) — has multiplicity structure **{20,8} at τ=0** (the Einstein/Type-D degenerate point) **→ {15,10,3} at τ=50** (algebraically general: the singular boundary is NOT the special τ=0 structure). The per-block Weyl-operator Frobenius-norm log-slopes `d ln‖C_block‖/dτ` are **SU(2): +2.00000, ℂ²: +1.99680** — both track the e^{2τ} fiber-Weyl-eigenvalue scale (√K₈ ~ ½e^{2τ}), i.e. the contracting SU(2) channel and the divergent Weyl content live on the SAME exponent. This is the **Ψ_ABCD-level realization** of the causal split (not merely the tortoise integral): the divergent, timelike Weyl content is carried by the SU(2) block; the convergent, spacelike content by ℂ²/U(1).

**3. Per-block conformal distances (Sage-exact, match S49 to 0.0).** Tortoise/conformal distance `d_block = √(5/3)·∫₀^∞ (1/b_block) dτ` with the Jensen length scales b_SU2=e^{−τ} (contracting), b_C2=e^{+τ/2}, b_U1=e^{+τ} (expanding):

| Block | length scale | conformal distance | character | S49 value | \|diff\| |
|:------|:-------------|:-------------------|:----------|:----------|:--------|
| **SU(2)** | b=e^{−τ} (CONTRACTS) | √(5/3)·(e^T−1) → **+∞** | **TIMELIKE** (i⁺ analog) | divergent | — |
| **ℂ²** | b=e^{+τ/2} (EXPANDS) | 2√(5/3) = **2.581988897471611** | **SPACELIKE** (r=0 analog) | 2.581988897471611 | **0.0** |
| **U(1)** | b=e^{+τ} (EXPANDS) | √(5/3) = **1.290994448735806** | **SPACELIKE** (r=0 analog) | 1.290994448735806 | **0.0** |

Sage-verified: `d_SU2(T)=√(5/3)(e^T−1)→+∞`; `d_C2=2√(5/3)`, `d_U1=√(5/3)`, ratio `d_C2/d_U1=2` exact. Both finite distances match S49 to machine precision (≪ 1e-6, the strict PASS boundary). ✓

**4. Kretschmann leading exponent +4 (genuine curvature singularity, not coordinate).** `K₈(τ)` rises 5.35×10⁻¹ → 6.02×10⁸⁵ over τ=0.19→50; log-slope on the deep tail (τ≥5) = **3.99999999990** (Sage symbolic: K ~ a₄ ~ R_K² ~ (½e^{2τ})² = ¼e^{4τ} ⇒ exponent +4). Matches S95-W4-5 K12_slope=3.99999 exactly. The Weyl-to-Kretschmann tail ratio `|C|²₈/K₈ → 0.4762` (Weyl persists ~48% asymptotically) — Type O (|C|²=0) is impossible (SU(3) structure constants force |C|²>0); WCH-consistent (Ricci grows faster, so |C|²/K decreases while |C|² itself diverges).

**5. The timelike/spacelike substitution chain (substituted numbers).**
- Step 1: g_τ = 3·diag(e^{−2τ}×3, e^{τ}×4, e^{2τ}×1) [E1; volume-preserving 2−6+4=0; `jensen_metric` L1=e^{2s}(u1), L2=e^{−2s}(su2), L3=e^{s}(C²)].
- Step 2: d_block = √(5/3)·∫₀^∞ (1/b_block) dτ.
- Step 3 (SU(2), CONTRACTING): d_SU2 = √(5/3)·∫₀^∞ e^{+τ}dτ → +∞ ⇒ infinite conformal distance ⇒ **TIMELIKE** (i⁺).
- Step 4 (ℂ²/U(1), EXPANDING): d_C2 = 2√(5/3) = 2.581989, d_U1 = √(5/3) = 1.290994 (finite) ⇒ **SPACELIKE** (r=0).
- Step 5: contracting ⇒ τ* diverges ⇒ TIMELIKE; expanding ⇒ τ* finite ⇒ SPACELIKE. The volume-preserving constraint (SU(2) contracts as ℂ²/U(1) expand) FORCES the anisotropic split. Kretschmann leading exponent +4 ⇒ genuine curvature singularity.

**6. Methodology note — regime-of-validity correction (Class-1-boundary honest disclosure).** The first emission read the dynamic CMPP type as a D/G-continuation FAILURE. Diagnosis (Sage-verified scale separation): the dynamic Type-G signal comes from the extrinsic-curvature cross-term `|K_diag|²_max = (v_terminal/2)²·4 = 704.64` — **fixed** in τ — while the fiber Weyl eigenvalue scale grows as √K₈ ~ ½e^{2τ}. The dimensionless ratio `r_dyn = |K_diag|²/√K₈` crosses the float64-detectability floor near τ≈5–6; beyond it the Type-G boost-weight signal sinks **below round-off** and the classifier spuriously reverts to the static Type D (`G→I→D` at τ=6,8,10). This is a **NUMERICAL REGIME artifact**, not a physical type change — AND it occurs only where the modulus is **censored** (COSMIC-CENSORSHIP-49: the modulus never reaches τ≳0.22, let alone τ→∞), so the dynamic type at the singular boundary is physically counterfactual. The corrected gate scopes the dynamic-type assessment to its resolvable transit window (Type G for τ≲5, `r_dyn`-pinned) and reports `r_dyn` per sample. The PASS criterion (plan `operator.form` / `strict_PASS_boundary`) — (a) unambiguous τ→∞ type + (b) conformal-distance match <1e-6 — is met by the **static** Type D (a) and the S49-exact distances (b); the dynamic-G is the S84 cross-check, NOT a PASS condition. Correction disclosed via the Option-A supersession chain (4 lines retained on disk; latest = PASS).

**7. Substrate framing (substrate-first, IS-not-IN).** GEOMETRIC. The Petrov/CMPP type is NOT the algebraic type of a spacetime the fabric lives IN — it is the type of the EMERGENT Lorentzian Weyl content read off the substrate's own geometry: `D_K eigenvalues → Jensen fiber metric g_τ → 12D product lift → a₂-reduced emergent 4D Lorentzian metric → Petrov type`. The τ→∞ singularity is the fabric's internal geometry running to maximal anisotropy (SU(2) block contracting to zero, ℂ²/U(1) expanding) — a Kasner-type behaviour of the order-parameter texture, NOT a singularity forming inside a container. The canonical framework lesson (Diagram A; S49→S50): classifying the RAW EUCLIDEAN fiber Weyl directly gives the category-error Type II (CMPP-TRANSITION-49 FAIL — Riemannian signature locks the type); the PHYSICAL type is the a₂-reduced emergent-Lorentzian Type D (A4/S50, Schwarzschild/Kerr class). This gate carries that lesson into the τ→∞ limit and the censorship (barrier τ≈0.19 ≪ τ_NEC≈1.38) keeps the physical epoch causally clear of the singular boundary.

**Artifacts**: `computations/session-96/s96_geom_tauinf_petrov.py` / `.npz` / `.png`.

---

### §W5-4. S96-GEOM-CCC-WEYL (schwarzschild-penrose-geometer)

**Status**: COMPLETED
**Gate ID**: `S96-GEOM-CCC-WEYL`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (Weyl-curvature trajectory of the fabric across the full modulus flow)
**Agent**: `schwarzschild-penrose-geometer`
**Hypothesis**: The Weyl-curvature scalar |C|²(τ) is monotone-increasing from its genesis minimum |C|²(0)=5/14 across the full physical flow (Weyl-Curvature-Hypothesis reading: minimal Weyl at the cold-regular genesis, growing through gravitational clumping), AND a conformal-rescaling map relating the censored τ→∞ boundary to a new τ=0-like low-Weyl surface (a substrate-internal Penrose-CCC aeon analog) is either CONSTRUCTED or shown OBSTRUCTED with an explicit obstruction reason.
**Plan reference**: `sessions/session-plan/session-96-plan-w5.md` §W5-4.

**Verdict**: **PASS** — SIGN/MAGNITUDE/REGIME = **PASS / PASS / VALID**. (i) `d|C|²/dτ > 0` confirmed strictly on (0, 2.0] (0 decreasing steps over the 201-point grid) from the genesis minimum `|C|²(0) = 5/14` (anchor reproduced to 5.55e-17). (ii) The substrate-internal CCC conformal-rescaling map is **OBSTRUCTED**, with four explicit, mutually-reinforcing obstruction reasons (O1–O4 below). Both clauses of the pre-registered PASS criterion are satisfied (monotone sign **and** CCC-map resolved as a clean obstruction).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

- **script** `computations/session-96/s96_geom_ccc_weyl.py` — EXISTS. `grep -E 'from canonical_constants import|append_verdict'`:
  - `from canonical_constants import tau_NEC, tau_fold` (framework constants imported)
  - `def append_verdict(...)` + call site (verdict emission helper present)
- **data** `computations/session-96/s96_geom_ccc_weyl.npz` — EXISTS (full trajectory `tau,K,R,Ric2,weyl2,ratio` + CCC record + 3-tuple).
- **plot** `computations/session-96/s96_geom_ccc_weyl.png` — EXISTS (4-panel: curvature invariants log; |C|² genesis detail; |C|²/K fraction; d|C|²/dτ sign).
- **verdict_line** in `computations/session-96/s96_gate_verdicts.txt` — EXISTS, matches `^S96-GEOM-CCC-WEYL:.* audit_sha256=[a-f0-9]{64}`:
  - canonical (corrective, Option A): `S96-GEOM-CCC-WEYL: PASS -- value='WCH:d|C|2/dtau>0_from_5/14_mono=True_|C|2(0)=0.357143_|C|2(2.0)=1.187e+02_ratioNETdec=True;CCC:OBSTRUCTED-O1O2O3O4' supersedes=27641ab5…e613e5 scheme=Weyl-scalar-Riemannian convention=Bianchi-identity L_max=NA audit_sha256=b5c1787368ff1145dcf393c436c2ddb3f97505d2999ce73b2affc3dd90ee84a0 content_sha256=80557eb646e3ffd582c44ebc790e7975a301641686233c7a102e0e60b544d531 schema_version=S84+`
  - dual-SHA companion row: `# audit_sha256_short=b5c1787368ff1145 content_sha256_short=80557eb646e3ffd5 # S96-GEOM-CCC-WEYL dual-SHA companion row supersedes=27641ab5…e613e5`
  - schema-v2 3-tuple row ([SIGN]): `# sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID # S96-GEOM-CCC-WEYL 3-tuple annotation (schema-v2)`
  - (Original line `audit_sha256=27641ab5…e613e5` RETAINED on disk per absolute verdict permanence; the corrective line supersedes it after a 1-line script refinement that split the `|C|²/K` flag into NET-decreasing vs global-monotone. Verdict unchanged: PASS in both.)

**MCP Pre-Compute Audit** (query-first per `.claude/rules/knowledge-index-usage.md`; executed before writing the script):

- `search_knowledge("Weyl curvature |C|^2 genesis minimum 5/14 SP-2 monotonicity")` → **SP-2** (gate, CLOSED, `session-22/s22a_weyl_curvature.py`); open_channel "tau = 0 (round metric)": *"|C|² = 5/14 (SP-2). Not zero, but the MINIMUM on the Jensen curve. Triple-selected (Session 29): WCH + J-maximality + DNP instability."* — anchor confirmed.
- `search_knowledge("session-49 sp-collab WCH Weyl Ricci dominance opposite 4D collapse")` → **theorem "WCH consistent"** (PROVEN, `session-49-sp-collab`): *"Extended to tau = 2.0, and the decreasing |C|²/K ratio established (Ricci dominance grows, opposite to 4D collapse)."* + open_channel "Curvature sign hierarchy": *K_sect → Weyl → Ric at 0.537 → 0.895 → 1.382.* — WCH-consistency fact confirmed.
- `get_constant`-equivalent grep on `canonical_constants.py` → `tau_NEC = 1.383` (S95 W4-5 12D censorship; `tau_fold = 0.19`). Imported, not hardcoded.
- `trace_entity("|C|^2/K decreasing Ricci dominance")` → no direct trace (the result lives in `session-49-sp-collab` as the "WCH consistent" theorem, captured above). No closure PRE-CLOSES this gate: SP-2 fixes only the τ=0 anchor; session-49 establishes the *net* |C|²/K trend to τ=2.0; the **full 201-point |C|²(τ) monotonicity sign** and the **CCC construct/obstruct decision** are NEW work this gate performs.

**Results**

**(i) WCH monotonicity — `d|C|²/dτ > 0` (SIGN = PASS).**

Curvature invariants computed substrate-first on the Jensen metric `g_τ = 3·diag(e^{−2τ}×3, e^{τ}×4, e^{2τ}×1)` on SU(3): `K(τ)` and `R(τ)` from their exact closed forms (SP-2, machine-ε verified in `r20a`/`s22a`), `|Ric|²(τ)` numerically from the canonical Riemann-tensor builder `compute_riemann_tensor_ON_fast(τ)` (`r20a_riemann_tensor.py`) over a clean 201-point grid. `|C|²(τ)` via the **Bianchi-identity route** (MEMORY-pinned to avoid the Ricci-sign trap of the direct `C = R − Schouten` form).

Trajectory anchors (201-pt grid, τ ∈ [0, 2.0]):

| τ | \|C\|² | K | \|Ric\|² | \|C\|²/K |
|:--|:--|:--|:--|:--|
| 0.000 | **0.357143** (=5/14) | 0.5000 | 0.5000 | 0.714286 |
| 0.190 (fold) | 0.385917 | 0.5346 | 0.5139 | 0.721945 |
| 0.200 | 0.388729 | 0.5384 | 0.5163 | **0.721952** (ratio peak) |
| 1.380 (≈τ_NEC) | 10.323877 | 21.0731 | 20.8707 | 0.489908 |
| 2.000 | 118.655950 | 248.7751 | 248.4904 | 0.476961 |

- `|C|²(0) = 0.357142857143` vs `5/14 = 0.357142857143` — anchor err **5.55e-17** (SP-2 reproduced to machine ε via the clean Bianchi route).
- `|C|²` minimum is at index 0 (τ=0): **the genesis IS the global minimum** (WCH minimum).
- **Strictly increasing**: `n_decreasing_steps = 0` of 200; `d|C|²/dτ > 0` throughout (0, 2.0].

**Monotonicity substitution chain** (the [SIGN] direction claim, with substituted numbers):

```
Claim: |C|²(τ) is monotone-INCREASING from its genesis minimum 5/14 (WCH: Weyl small at genesis, grows through the flow).
Step 1: |C|²(0) = 5/14 = 0.357143                                     [SP-2, S22a; MINIMUM on the Jensen curve, NOT zero]
Step 2: |C|² via Bianchi identity (n=8): |C|² = K − (4/(n−2))|Ric|² + (2/((n−1)(n−2)))R²
                                              = K − (2/3)|Ric|² + (1/21)R²   [coeff of |Ric|² NEGATIVE, of R² POSITIVE]
Step 3: K(τ), R(τ) exact closed-form (SP-2); |Ric|²(τ) numeric from r20a Riemann builder
Step 4: Substitute: |C|²(0)=0.357143 < |C|²(0.19)=0.385917  ⇒  Δ|C|² = +0.028774 > 0 over [0, 0.19]
        and K ∼ (1/12)e^{4τ} tail (a₄ ∝ R_K² ∼ ¼e^{4τ}) drives |C|² up monotonically as τ→∞ (|C|²(2.0)=118.66)
Step 5: d|C|²/dτ > 0 on (0, 2.0]  (0 decreasing steps of 200)  ⇒  Weyl curvature GROWS from the genesis minimum   [direction]
Conclusion: |C|² is minimal at the cold-regular genesis (τ=0, WCH minimum) and grows monotonically — the substrate-
            internal realization of Penrose's Weyl-Curvature-Hypothesis (low Weyl at the low-entropy initial state).
```

**The distinction (MEMORY, load-bearing) — refined.** `|C|²` is **globally** monotone-increasing (strict, 0 decreasing steps) while `|C|²/K` is **NET-decreasing** over [0, 2.0] (0.714286 → 0.476961; Ricci grows faster overall, reproducing the session-49 "WCH consistent" theorem). The clean recompute **refines** the local picture beyond session-49: `|C|²/K` is NOT *globally* monotone-decreasing — it **rises** from 5/14 to a peak `0.721952` at τ≈0.20 (right at the fold), then the `K ∼ e^{4τ}` Ricci tail drives it down. Physically: very close to genesis the volume-preserving TT shear seeds Weyl (tidal) curvature slightly faster than Ricci, peaking at the fold, after which Ricci dominance takes over. This is consistent with session-49 (which stated the *net* trend on [0, 2.0]) and is a faithful sharpening of it. The npz records both `ratio_net_decreasing=True` and `ratio_locally_monotone_dec=False` with `ratio_peak_tau=0.200`.

**Type O is impossible.** `|C|²` never reaches zero (minimum 5/14 at genesis); the SU(3) structure constants force `|C|² > 0`. The WCH-analog is therefore **"minimal Weyl"** (5/14), not Penrose's exact conformal flatness ("zero Weyl") — the cold-regular genesis is an extremum of symmetry (the E7-unstable maximal-symmetry round metric), not a conformally-flat surface.

**(ii) CCC conformal-rescaling map — OBSTRUCTED (four reasons).**

Grounding (read-only): Meissner–Penrose 2025 (*Physics of CCC*, arXiv:2503.24263) + Penrose 2010 (*Cycles of Time*). CCC's crossover requirements: a single **smooth spacelike conformal 3-surface X** joining each aeon's future infinity ℐ⁺ to the next aeon's stretched big bang, with (R2) **Ψ_ABCD → 0 at ℐ⁺** (Friedrich's result — Weyl *vanishes* at the future boundary; the conformally-rescaled `ψ_ABCD` of weight −1 carries crossover information), (R3) a **Weyl-DOMINATED** pre-crossover epoch (C ≫ E,S — the Gravitational Wave Epoch), all matter conformally invariant (massless), ρ→0, a→∞, and (R4) the conformal factor Ω→0 monotonically toward a single spacelike boundary.

The substrate's τ→∞ boundary fails **all four** requirements:

| CCC requirement | Substrate behaviour | Verdict |
|:--|:--|:--|
| **R1** smooth spacelike conformal boundary | `K ∼ e^{4.00000·τ} → ∞` (leading exponent fitted 4.00000; matches S95 W4-5 slope 3.99999) — a **genuine curvature singularity**, not a smooth boundary | **O1: FAIL** |
| **R2** Ψ→0 at ℐ⁺ (Friedrich) | `|C|²` **GROWS** 0.357143 → 1.1866e+02 (→∞); Weyl does NOT vanish — the **opposite** of Friedrich | **O2: FAIL** |
| **R3** Weyl-dominated GWE (C ≫ E,S) | `|C|²/K` NET-**decreases** 0.714286 → 0.476961 (Ricci dominance **grows**) — CCC needs C≫E,S, the reverse | **O3: FAIL** |
| **R4** single smooth spacelike crossover X | boundary is **ANISOTROPIC (Kasner)**: SU(2) block TIMELIKE (conformal time `η_SU2 ≈ 6.59e+25` → ∞, an i⁺ analog), ℂ²/U(1) SPACELIKE (finite `η`; S49 distances ℂ²=2.581989, U(1)=1.290994) — **no single spacelike 3-surface** to rescale | **O4: FAIL** |

**`ccc_constructible = False`.** All four CCC crossover conditions are violated; the obstruction is structurally over-determined (any one of O1–O4 alone suffices). The deepest is **O3 + O4**: CCC needs the pre-crossover epoch to become Weyl-*dominated* and conformally-smooth as it approaches a single spacelike ℐ⁺, whereas the substrate's modulus flow runs to a **Ricci-dominated, anisotropic Kasner curvature singularity** — the polar opposite of a low-Weyl conformal crossover. The substrate's arrow-of-time-from-geometry is genuinely WCH-flavoured at the *genesis* end (minimal Weyl at τ=0, growing through clumping), but it does **not** close into a Penrose CCC cycle: there is no low-Weyl future crossover to rescale onto a new τ=0-like surface. The two ends of the modulus flow are **NOT** the two ends of a CCC aeon.

Note the explanatory-direction inversion preserved throughout (vs the CCC literature, which is GR-first): in CCC the classical Weyl-dominated gravitational gas is *fundamental* at crossover; here the Weyl scalar `|C|²(τ)` is an **emergent** curvature invariant of the Jensen metric `g_τ`, itself read off the `a₂` spectral weight of `D_K` on Jensen-deformed SU(3). The obstruction is therefore a statement about the substrate's own spectral-geometry flow, not about a 4D container.

**4-tuple**: `(value = "WCH:d|C|2/dtau>0_from_5/14;CCC:OBSTRUCTED-O1O2O3O4", scheme = Weyl-scalar-Riemannian, convention = Bianchi-identity, L_max = N/A)`. SIGN/MAGNITUDE/REGIME = PASS/PASS/VALID. Dual-SHA: `audit=b5c1787368ff1145dcf393c436c2ddb3f97505d2999ce73b2affc3dd90ee84a0`, `content=80557eb646e3ffd582c44ebc790e7975a301641686233c7a102e0e60b544d531`.

**Substrate framing.** GEOMETRIC. The Weyl-Curvature-Hypothesis is Penrose's proposal that the Weyl tensor was near-zero at the low-entropy initial state and grows through gravitational clumping — the arrow of time written into geometry. Here this is NOT a statement about a 4D spacetime's initial conditions: `D_K(0)` IS the round maximally-symmetric SU(3) (the WCH minimum, `|C|²=5/14`, cold-regular genesis, E7-unstable maximum of symmetry), and as τ flows the order-parameter texture shears (volume-preserving TT) and `|C|²` grows. Direction of explanation held throughout: `D_K eigenvalues → curvature invariants |C|²(τ), K(τ) → WCH arrow-of-time reading → CCC structural question`. The CCC question — whether the censored τ→∞ boundary conformally rescales to a new τ=0-like low-Weyl surface — asks whether the substrate admits a cyclic aeon structure *internal to its own modulus space*. The answer is **NO** (obstructed): the substrate has a genuine, Ricci-dominated, anisotropic Kasner curvature singularity at τ→∞, censored by COSMIC-CENSORSHIP-49 (barrier at τ≈0.19 ≪ τ_NEC=1.383, keeping the physical epoch causally clear of it), not a smooth low-Weyl conformal crossover. The substrate is WCH-consistent at genesis but is NOT a Penrose CCC cycle.

---

### §W5-5. S96-GEOM-OFFJENSEN-CHERN (berry-geometric-phase-theorist)

**Status**: COMPLETED
**Gate ID**: `S96-GEOM-OFFJENSEN-CHERN`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (Berry curvature / Chern number on the modulus-space eigenbundle of D_K)
**Agent**: `berry-geometric-phase-theorist`
**Hypothesis**: The Berry curvature 2-form Ω(τ,μ) and integrated Chern number C=(1/2π)∮ Ω dτ dμ on the 2-parameter Ad U(2)-invariant deformation surface either remain trivial (|C|<1e-3, C quantized to 0 — strengthening the §9 spine to "topology trivial on the FULL physical deformation surface") OR carry a nonzero integer Chern (|C−n|<1e-3, n≠0 — a genuine substrate topological invariant); the 1D-Jensen-line result Ω=0 does NOT determine the off-Jensen surface.
**Plan reference**: `sessions/session-plan/session-96-plan-w5.md` §W5-5 (closes the C11/C12 OFF-JENSEN open channel, S29).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| Artifact | Path | Exists | must_contain check |
|:--|:--|:--|:--|
| script | `computations/session-96/s96_geom_offjensen_chern.py` | ✓ (36,838 B) | `grep -E 'from canonical_constants import'` → 2 hits (L147 `from canonical_constants import *`; L148 `... import tau_fold`); `grep -E 'append_verdict'` → L245 `def append_verdict(...)` + L664 call site |
| data | `computations/session-96/s96_geom_offjensen_chern.npz` | ✓ (48,655 B) | NPZ with `F_plaq` (50×50 FHS field strength), `Omega_cont` (50×50 BP-4 continuum curvature), `jensen_omega`, `C_fhs=9.78e-15`, `C_cont=-5.37e-29`, `max_absOmega=2.27e-23`, `band_deg=2`, `sector_chern_vals` (5 sectors), `v_jensen`, `v_mu`, `verdict='PASS'`, `branch='PASS-TRIVIAL'` |
| plot | `computations/session-96/s96_geom_offjensen_chern.png` | ✓ (115,807 B) | 2-panel: BP-4 continuum Ω(τ,μ) heatmap (fold line τ=0.19 + Jensen line μ=0 marked) ‖ FHS lattice field strength F_plaq |
| verdict line | `computations/session-96/s96_gate_verdicts.txt` (line 125) | ✓ | `grep -E '^S96-GEOM-OFFJENSEN-CHERN:.* audit_sha256=[a-f0-9]{64}'` → 1 canonical line; dual-SHA companion row present (line 126); NO schema-v2 3-tuple (correct — `schema_v2_3tuple_required: false`; [VERIFY] integer-quantization, membership in {trivial, nontrivial}, no signed delta); `audit_sha256` unique across the file (grep count = 1, no sig_5 collision) |

Content presence only — no length/size targets.

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script; query-first discipline per `.claude/rules/knowledge-index-usage.md`):

- `search_knowledge('Berry curvature Jensen line anti-Hermitian zero Chern off-Jensen')` → **Berry Curvature Vanishing (S25, theorem proven_1810/proven_1752/proven_1880, PROVEN)** = "K_a anti-Hermitian ⟹ Ω=0 identically, all eigenstates, all sectors, all τ" (`baseline-findings-s66.md` / `constraint-mega-matrix.md` W5; closure error 1.12e-16). The 1D-Jensen-line baseline this gate extends to the 2-parameter surface.
- `search_knowledge(...)` → **open_channel C11/C12 (Berry on Jensen)**: "OPEN OFF-JENSEN — May reappear on U(2)-invariant surface" (`session-29-fusion-synthesis.md`). **This is the open channel the gate closes.**
- `search_knowledge(...)` → **Curvature-robustness (W11-5, S85)**: "Chern-Weil additivity + O'Neill A=T=0 + even-base Spin^c — PERMANENT for product-metric Riemannian submersions at τ_fold; **Conditional off-fold: A and T may become non-zero away from τ_fold**." Flags that the off-fold surface is genuinely undetermined by the at-fold result — the structural reason this gate is needed.
- `trace_entity('Berry Curvature Vanishing')` → 3 theorem hits (proven_1810, proven_1752, proven_1880), all S25, all "K_a anti-Hermitian ⟹ Ω=0 identically." No off-Jensen 2-parameter result exists — confirms the gate is NOT a rediscovery.
- `get_constant('tau_fold')` → 0.19 (S12/S42 CONST-FREEZE-42). The fold the closed (τ,μ) surface encloses (at μ=0).
- `get_constant('Delta_BCS')` → 0.4642547394830737 (R-PROTECTED, S70). Sector context (bottom-band scale).
- **Sage MCP pre-flight** (`sage_eval`): verified the 2-parameter TT-surface geometry exactly — Jensen `v_J=(2,−2,1)` and second TT eigendirection `v_μ = n × v_J = (11,7,−8)` with `n=(1,3,4)` (block multiplicities); both volume-preserving (`n·v_J = n·v_μ = 0`), orthogonal (`v_J·v_μ = 0`), `rank[v_J;v_μ]=2` (span the full 2D volume-preserving plane), `|v_J|²=9`, `|v_μ|²=234`.
- **NOT PRE-CLOSED**: the at-fold / Jensen-line Ω=0 is PROVEN (S25), but the **off-Jensen 2-parameter surface is the OPEN C11/C12 channel** (S29) with W11-5 (S85) explicitly flagging it conditional off-fold. The gate computes the previously-uncomputed object.

**Verdict**: **PASS [PASS-TRIVIAL]** — value `C_FHS=9.777563e-15_round=0_branch=PASS-TRIVIAL_maxOmega=2.272e-23_C_cont=-5.368374e-29_jensenOmega=2.496e-27_allsectorsTrivial=True`; scheme=FHS-Wilson-loop, convention=ABSOLUTE, L_max=10. The integrated Chern number is **integer-quantized to 0** (|C−round(C)| = 9.78e-15 ≪ 1e-3 tolerance), the Berry curvature is **machine-zero across the ENTIRE surface** (max|Ω| = 2.27e-23 ≪ the 1e-12 trivial floor), and the FHS lattice-Chern and continuum BP-4 estimators **agree** (C_cont = −5.37e-29). dual-SHA: `audit_sha256=943cb408ea41192ad057ccbcd7713ee58a09f507c0f026fbe89344dfd1cdb4f9`, `content_sha256=3da9e6336567957d71a375a321e50b0472397760131fad44e94093fc7c5da16f` (full 64-char). **This closes the C11/C12 OFF-JENSEN open channel / the P-30w gate.**

**Results**:

**The geometric object — the 2-parameter U(2)-invariant TT deformation surface.** The U(2)-invariant left-invariant metrics on SU(3) form a 3-parameter family with scale factors `(L1,L2,L3)` on the reductive blocks `su(3)=u(1)⊕su(2)⊕C²` (multiplicities `(1,3,4)`; `dirac_spectrum.u2_invariant_metric`). In log-coordinates `ℓ=(ln L1,ln L2,ln L3)` the volume-preserving (TT) condition is `n·ℓ=0` with `n=(1,3,4)` — a 2D plane. The two deformation axes that span this plane (Sage-exact):

| Direction | Vector in `(ℓ1,ℓ2,ℓ3)` | Volume-preserving `n·v` | `\|v\|²` | Role |
|:--|:--|:--|:--|:--|
| Jensen `v_J` | `(2, −2, 1)` | `2−6+4 = 0` ✓ | 9 | `L=(e^{2τ},e^{−2τ},e^{τ})`; fold at τ=0.19; μ=0 IS this line |
| Second TT `v_μ = n × v_J` | `(11, 7, −8)` | `11+21−32 = 0` ✓ | 234 | the unique vol-preserving direction ⊥ Jensen (`v_J·v_μ=0`) |

Parameterization `ℓ(τ,μ) = τ·v_J + (μ/\|v_μ\|)·v_μ`, so at μ=0 the metric is the canonical Jensen metric **bit-for-bit** (verified at the fold: `(L1,L2,L3)=(1.462285, 0.683861, 1.209250)` = `(e^{0.38}, e^{−0.38}, e^{0.19})`). The closed scan surface is `τ ∈ [0.10, 0.30] × μ ∈ [−0.10, 0.10]` (51×51 nodes → 50×50 = 2500 plaquettes), enclosing the fold at μ=0.

**The dimension-count substitution chain (plan §W5-5 Step 1–5; the structural reason the gate is non-trivial):**

- **Step 1**: Berry curvature 2-form `Ω = dA`, `A_i = i⟨n|∂_i|n⟩`, `i ∈ {τ, μ}`.
- **Step 2**: On the 1D Jensen line (μ fixed = 0) the parameter base is 1-dimensional ⇒ `Ω = dA` needs a 2-form, but a 1D base carries **no** 2-form (`dτ ∧ dμ` has no `dμ` when μ is fixed) ⇒ `Ω ≡ 0` on the Jensen line **by dimension count** (plus the deeper anti-Hermitian `K_a` ⟹ real eigenstates, S25/W5).
- **Step 3**: On the 2-parameter surface (τ, μ both varying), `Ω = (∂_τ A_μ − ∂_μ A_τ) dτ ∧ dμ` is a **genuine** 2-form ⇒ Ω **can** be nonzero off-Jensen even though it vanishes on the μ=0 slice.
- **Step 4**: anti-Hermitian-`K_a` (W5) gives real eigenstates on the Jensen line ⇒ A real ⇒ gauge-trivial there; off-Jensen the `v_μ` direction is **not** the Jensen shear and may break the reality ⇒ complex eigenstate phase ⇒ possibly nonzero Ω.
- **Step 5**: `1D-base Ω=0 ⇏ 2D-base C=0` [triviality on a slice does not imply triviality on the surface]. **Conclusion**: the off-Jensen Chern is genuinely undetermined by the Jensen-line result; `C = (1/2π)∮ Ω dτ dμ` is the decisive object.

**What the computation found (NUMBERS first):**

| Quantity | Value | Threshold | Status |
|:--|:--|:--|:--|
| `C_FHS` (non-Abelian Fukui-Hatsugai-Suzuki lattice Chern, deg-2 lowest band) | **9.78e-15** | `\|C−round(C)\| ≤ 1e-3`; round=0 | integer-quantized to **0** |
| `max\|F_plaq\|` (max per-plaquette FHS field strength) | 6.14e-14 | — | machine-zero |
| `C_cont` (BP-4 continuum, `(1/2π)∫Ω dτ dμ`) | **−5.37e-29** | agree with FHS | agrees (C=0) |
| `max\|Ω\|` (BP-4 continuum curvature, full surface) | **2.27e-23** | trivial floor 1e-12 | ≪ floor ⇒ **trivial** |
| `max\|Ω(τ, μ=0)\|` (Jensen-line baseline) | 2.50e-27 | reproduce S25/W5 Ω=0 | ✓ machine-zero |

**Robustness — ALL five low-lying Peter-Weyl sectors trivial** (non-Abelian FHS, each sector's lowest band-group degeneracy detected independently; all deg=2 Kramers/J multiplets):

| Sector (p,q) | `C_FHS` | `\|C−round\|` |
|:--|:--|:--|
| (0,0) | 9.78e-15 | 9.78e-15 |
| (1,0) | 3.37e-16 | 3.37e-16 |
| (0,1) | −8.64e-18 | 8.64e-18 |
| (1,1) | −3.60e-18 | 3.60e-18 |
| (2,0) | 3.30e-16 | 3.30e-16 |

`all_trivial_sectors = True` (max|C_sector| = 9.78e-15). C=0 on every sector of the eigenbundle, not just the bottom band.

**The degenerate-band subtlety (geometric reading; the methodological care that makes the FHS estimator correct).** The lowest Dirac band on the SU(3) eigenbundle is a **2-fold Kramers/J-degenerate multiplet** (the (0,0) singlet bottom band: `|λ|_min = 0.819741`, doubled). A naive *single-band* FHS link `⟨n(k)|n(k+1)⟩` inside a degenerate subspace is gauge-ill-defined — it tracks an arbitrary U(2) basis rotation within the degenerate band-group, producing spurious large per-plaquette field strength (a smoke test gave C ≈ 0.78, max|F| ≈ 2.96 rad — pure gauge noise). The correct estimator is the **non-Abelian (Wilczek-Zee) FHS**: det-normalized U(deg) link matrices `M_ab = ⟨n_a(k)|n_b(k+1)⟩`, plaquette holonomy `arg det(...)`. This is gauge-invariant under U(deg) rotations of the multiplet (the arbitrary basis rotation cancels around every plaquette), and it reduces the spurious 0.78 to a clean 9.78e-15. The continuum BP-4 companion uses the matching non-Abelian *trace* (sum over the degenerate band-group, intra-multiplet terms excluded by the `(λ_n−λ_m)² > gap_floor` guard) and independently returns 0.

**Geometric interpretation — the deeper mechanism.** Off-Jensen, D_K is genuinely complex (`max|Re D|/max|D| = 0.64`; D is neither purely real nor purely imaginary), so the naive "real D ⟹ real eigenstates ⟹ Ω=0" argument does *not* apply on the surface. Yet the continuum Berry curvature is machine-zero everywhere. This directly confirms the **second** vanishing mechanism (distinct from the Jensen-line anti-Hermiticity): the Berry curvature is `Im(QGT)` (imaginary part of the quantum geometric tensor), and the combined `J + U(2)` invariance structure forces `Im(QGT) = 0 identically` on the **full** U(2)-invariant surface — the surface is **metrically rich** (the quantum metric `Re(QGT)` is non-zero; the eigenstates rotate as the metric deforms) but **topologically trivial** (the symplectic / curvature part vanishes). The substrate carries no Berry monopole anywhere on its own physical modulus-space.

**Substrate framing.** GEOMETRIC. The Berry curvature lives on the eigenbundle of D_K fibered over the substrate's OWN parameter space — the moduli-space of U(2)-invariant TT deformations IS substrate-IS (Level-2 per `phononic-framing.md`), NOT a container the operator sits in. Direction of explanation held throughout: `D_K eigenbundle → Berry connection A → curvature Ω → Chern number C`. This is the cleanest test of the §9 "geometry vs topology" spine: the spine claims the representation-theoretic / topological outputs survive the continuum dissolution while the geometric magnitudes do not. The PASS-TRIVIAL verdict **strengthens** that spine — topology is trivial not just on the 1D Jensen slice but on the **entire 2-parameter physical deformation surface**. The off-Jensen Chern is the THIRD topological object of the framework (distinct from the momentum-space `N₃=0` BDI Fermi-surface class and the Jensen-line `Ω=0` modulus-space curvature on the 1D slice) — the modulus-space Chern on the 2-parameter surface — and it too is zero. Off-Jensen was the SOLE open route to nontrivial substrate topology (the P-30w gate); that route is now closed trivially.

**Solution-space update.** C11/C12 (S29 OPEN) → **CLOSED-TRIVIAL**. The §9 spine upgrades from "topology survives dissolution on the Jensen line" to "topology trivial on the full physical U(2)-invariant deformation surface." No topological-protection mechanism for the relic/CC arises from modulus-space Berry curvature — consistent with (and strengthening) the L0–L7 triviality chain (11 independent invariants all zero) and the W11-5 (S85) at-fold Chern-Weil-triviality result, now extended off-fold across the closed surface enclosing the fold. The off-Jensen modulus-space Chern — the framework's sole open topological route — is **0**.

**4-tuple**: (value=`C_FHS=9.777563e-15_round=0_branch=PASS-TRIVIAL_maxOmega=2.272e-23_...`, scheme=`FHS-Wilson-loop`, convention=`ABSOLUTE`, L_max=`10`). Artifacts: `computations/session-96/s96_geom_offjensen_chern.py` / `.npz` / `.png`.

---

### §W5-6. S96-GEOM-GAUGE-SOURCING (kaluza-klein-theorist)

**Status**: COMPLETED
**Gate ID**: `S96-GEOM-GAUGE-SOURCING`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **PARTICLE** (gauge-group content = representation-theoretic content of D_K and the isometry of g_τ)
**Agent**: `kaluza-klein-theorist`
**Hypothesis**: The NCG-algebra gauge group SU(A_K)=U(1)×SU(2)×SU(3) (13 generators, §1.1 inner-fluctuation route) and the KK-isometry gauge group (the Jensen-metric stabilizer in Isom(SU(3),g_bi-inv), expected residual SU(3)_L×U(2)_R = 12 generators, §2.4 route) either deliver the SAME group with the SAME chiral SM charge assignment OR agree only on a common subgroup — and the S61 13/13-generator gate's actual sourcing route is decidable from the Ψ₊=ℂ¹⁶ branching under both groups.
**Plan reference**: `sessions/session-plan/session-96-plan-w5.md` §W5-6 (Weinberg gauge=isometry theorem; S61 PROVEN 13/13 matched to a route, never overturned).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| Artifact | Path | Exists | must_contain check |
|:--|:--|:--|:--|
| script | `computations/session-96/s96_geom_gauge_sourcing.py` | ✓ (33,806 B) | `grep -E 'from canonical_constants import'` → 3 hits (incl. `from canonical_constants import *`, `... import tau_fold`); `grep -E 'append_verdict'` → `def append_verdict(...)` + call site |
| data | `computations/session-96/s96_geom_gauge_sourcing.npz` | ✓ (11,655 B) | NPZ with `A_ncg_raw_generators=13`, `A_ncg_sm_dim=12`, `B_isom_biinv_dim=16`, `B_isom_jensen_dim=12`, `c16_total=16`, `verdict=FAIL`, 3-tuple keys |
| plot | `computations/session-96/s96_geom_gauge_sourcing.png` | ✓ (142,987 B) | side-by-side generator-count bars (NCG vs KK) + Ψ₊=ℂ¹⁶ chiral-branching panel |
| verdict line | `computations/session-96/s96_gate_verdicts.txt` | ✓ | `grep -E '^S96-GEOM-GAUGE-SOURCING:.* audit_sha256=[a-f0-9]{64}'` → 2 canonical lines (original `f545446b…` retained + corrective `4dd165bd…` with `supersedes=` per Option A); dual-SHA companion + schema-v2 3-tuple companion both present |

Canonical verdict line: `audit_sha256=4dd165bd53700b5d93e0445fff1eee07f4c9d4ef80c15507d9eb1d9f4be29147`, `content_sha256=4637e989066f4855268208583a167603778154d2dff41f64fb92bc005ef31c84` (full 64-char; latest non-superseded). The original emission (`f545446b…`) pinned the plan-named `dk_builder` path `phonon-exflation-sim/src/dirac_spectrum.py`, which is MISSING on disk; per `substrate-first-canonical-sourcing.md §(ii.B)` plan-text-drift, the path was corrected to the substrate-canonical `computations/_shared/dirac_spectrum.py` and the corrective line carries the `supersedes` tag (verdict permanence: original retained byte-for-byte). Content presence only — no length/size targets.

**MCP Pre-Compute Audit**:
Queried the knowledge MCP before writing the script (query-first discipline; this gate is NOT pre-closed — it is a reconciliation/decision over two PROVEN inputs, not a re-derivation):

- `search_knowledge('SM gauge group recovery 13 generators SU(A_K) unimodular unitary')` → **[NEW S61] SM gauge group recovery (13/13 generators)**, theorem `proven_1403`, PROVEN `<1e-13`, source `s61_gauge_module.py` (on-disk: `s61_gauge_module_check.py`). Confirmed the S61 13/13 anchor.
- `search_knowledge('isometry gauge group SU(3)_L U(2)_R Jensen metric stabilizer Weinberg')` → eq (2.7) `(SU(3)×SU(3))/ℤ₃ → (SU(3)×SU(2)×U(1))/ℤ₆` (Baptista Paper 15 §3.8); session-31Aa equation hit: *"this is the gauge group from NCG inner fluctuations, which the framework does not use. The framework's gauge group from KK isometries is U(1)×SU(3)_R for the Jensen-deformed metric."* — the decisive NCG-vs-isometry dichotomy.
- `query_entity(theorems, 'SM gauge group recovery')` → `proven_1403`, precision `1e-13`, statement "13 generators". Confirmed provenance.
- `trace_entity('SM gauge group recovery 13 generators')` → single theorem hit, atlas-07 permanent-results, S61.
- `search_knowledge('Psi+ C16 branching Peter-Weyl chiral SM charge assignment (3,2,1/6) … Session 7')` → **SM quantum numbers from Psi_+ = C^16** (theorem, atlas-07, S7, PROVEN, 6 multiplets, Exact); per-sub-block dims (lepton-L 2, quark-L 6, lepton-R 2, quark-R 6, total 16). Pinned the chiral-charge home.
- `get_constant('tau_fold')` → `0.19` (S12/S42, CONST-FREEZE-42). Jensen evaluation point (stabilizer τ-independent for τ≠0).

Direct source reads (provenance for the substitution chain): `s61_gauge_module_check.py` `build_unitary_generators` (the 1+3+8+1=13 enumeration: u(1), su(2)_L on H, su(3) on right-M₃ colour, u(1)_color); `session-31Aa-synthesis.md` line 478 (NCG vs KK-isometry, U(1)×SU(3)_R); `session-19d-baptista-collab.md` line 85 ("the left SU(3) symmetry is BROKEN to the left SU(3) × right U(2) isometry"). Substitution-chain arithmetic cross-checked Sage-exact (13≠12; 16→12 with broken-coset dim 4).

**Verdict**: **FAIL** — outcome `isometry≠SM`. The two gauge-group sourcing routes deliver **structurally different groups**: the KK-isometry route (residual `SU(3)_L × U(2)_R`, 12 gen) carries its SU(2) inside the **RIGHT** `U(2)_R` factor, which is **not** the chiral `SU(2)_L` of the Standard Model. The pre-registered PASS (SAME-group-SAME-charges) is therefore excluded. 3-tuple: `sign_verdict=PASS` (the substitution-chain Step-4 prediction "routes give DIFFERENT groups" is **confirmed**: 13≠12 and SU(2) chirality OPPOSITE), `magnitude_verdict=FAIL` (strongest separation: `isometry≠SM`), `regime_verdict=VALID` (exact integer arithmetic — Lie-algebra dims + Peter-Weyl branching — no truncation/expansion regime to break). Composite collapse: `sign=PASS, magnitude=FAIL, regime=VALID ⇒ FAIL`. **Decisive output**: the S61 13/13-generator gate (PROVEN `<1e-13`) used the **NCG inner-fluctuation route** (Route A), not the KK-isometry route — it is **matched** to its route, **never overturned**.

4-tuple: `(value=isometry≠SM, scheme=isometry-stabilizer-vs-NCG-unitary, convention=left-isometry-Peter-Weyl, L_max=10)`. Canonical dual-SHA: `audit_sha256=4dd165bd53700b5d93e0445fff1eee07f4c9d4ef80c15507d9eb1d9f4be29147`, `content_sha256=4637e989066f4855268208583a167603778154d2dff41f64fb92bc005ef31c84`.

**Solution-space reading** (per the gate's `FAIL_meaning`): "gauge fields from pure geometry" (the capstone §0 KK promise) is the **NCG-algebra route ONLY**; the §2.4 eq-2.7 isometry reading is the source of the **left (p,q) Peter-Weyl LABELS** that organise the Ψ₊=ℂ¹⁶ branching, **not** the gauge group as such. The capstone §0 framing must be **scoped to the NCG inner-fluctuation route** — a genuine structural **clarification**, NOT an overturn of S61. This couples to **W5-7** (which route's M_KK is the gauge-route value) and to the KK-level-charge content (a W6/W7 follow-up).

**Results**:

**Route A — NCG inner-fluctuation route** (unimodular unitaries of `A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ)`; S61 `build_unitary_generators`):

| factor | generators | placement / chirality |
|:--|:--|:--|
| u(1) | 1 | C factor |
| su(2)_L | 3 | H block (rows 2–3) — **chiral LEFT** doublet |
| su(3) | 8 | right `M₃` — **colour** |
| u(1)_color | 1 | right `M₃` trace (the extra U(3) generator) |
| **raw U(A)** | **13** | ← **S61 reports 13/13 PROVEN `<1e-13`** |
| **physical SM** | **12** | one U(1) removed by global unimodularity (det=1) ⇒ `U(1)_Y × SU(2)_L × SU(3)_c` |

**Route B — KK-isometry route** (Killing-vector stabilizer of the Jensen metric `g_τ`; Weinberg/DeWitt/Witten):

| factor | generators | placement / chirality |
|:--|:--|:--|
| `Isom(SU(3), g_bi-inv)` at τ=0 | **16** | `(SU(3)_L × SU(3)_R)/ℤ₃` |
| su(3)_L isometry (τ>0) | 8 | surviving **LEFT** isometry |
| u(2)_R (τ>0) | 4 | surviving **RIGHT** factor (`1+3`; contains the SU(2) **and** U(1)) |
| **residual isometry (τ>0)** | **12** | `SU(3)_L × U(2)_R` (session-19d, session-31Aa) |
| broken (SU(3)_R→U(2)_R coset) | 4 | `8−4` |

**Substitution chain** (the decisive structural claim, Sage-exact integers):
- Step 1: `dim SU(A_K)` raw `= 1+3+8+1 = 13` [NCG, S61].
- Step 2: `Isom(SU(3), g_bi-inv) = 8+8 = 16` at τ=0 [KK].
- Step 3: Jensen τ>0 ⇒ `SU(3)_R → U(2)_R` ⇒ residual `= 8+4 = 12` [KK].
- Step 4 (compare): `13 (NCG raw) ≠ 12 (KK residual)` = **True**; `12 (NCG SM) == 12 (KK residual)` = True *(dims only)*; SU(2) chirality `NCG(LEFT) vs KK(RIGHT)` OPPOSITE = **True**; SU(3) placement `NCG(colour, right-M₃) vs KK(left-isometry)` DIFFER = **True**.
- Step 5: `SU(2)_R` (right) `≠ SU(2)_L` (left, chiral) ⇒ the KK-isometry group is **not** the chiral SM group.
- Conclusion: the two routes give structurally **DIFFERENT** groups (the SU(2) sits on opposite chiralities) ⇒ FAIL branch.

**Ψ₊ = ℂ¹⁶ chiral SM branching** (PROVEN S7, "SM quantum numbers from Psi_+ = C^16", Exact — where the chiral charges actually live):

| multiplet `(SU3_c, SU2, Y)` | dim | chirality | content |
|:--|:--|:--|:--|
| `(1, 2, −1/2)` | 2 | **L** | lepton doublet (ν_L, e_L) |
| `(1, 1, 0)` | 1 | R | ν_R singlet |
| `(1, 1, −1)` | 1 | R | e_R singlet |
| `(3, 2, 1/6)` | 6 | **L** | quark doublet (u_L, d_L) × colour |
| `(3, 1, 2/3)` | 3 | R | u_R singlet × colour |
| `(3, 1, −1/3)` | 3 | R | d_R singlet × colour |
| **total** | **16** | | one generation |

LEFT `(·,2,·)` doublet dims `= 2 + 6 = 8`; these carry the chiral `SU(2)_L` charge — the **NCG H-block `SU(2)_L`** (Route A), **NOT** the KK-isometry `SU(2)_R` (Route B). The Peter-Weyl `(p,q)` labels that organise the branching are LEFT-isometry; the KK-isometry route therefore supplies the **labelling structure**, while the **gauge** content is the NCG unimodular-unitary group.

**Weinberg gauge=isometry reading**: the foundational non-Abelian KK theorem (Weinberg 1983; DeWitt 1963; Witten 1981) gives the KK-promise gauge group `= Isom(K, g) = SU(3)_L × U(2)_R` for τ>0. Because its SU(2) is a RIGHT-isometry factor, this group does **not** reproduce the chiral SM — so the framework's SM gauge group is the **NCG unimodular-unitary route**, with the KK-isometry providing the LEFT (p,q) Peter-Weyl labels, not the gauge group itself.

**Decision (which route S61 used)**: S61 `build_unitary_generators` enumerates `U(A_K)` unimodular unitaries with SU(3)=colour on the **right** `M₃` and SU(2)_L on the H-block — this **is** Route A (NCG inner fluctuations), confirmed verbatim by session-31Aa line 478. `s61_route = NCG-inner-fluctuation`; raw-count match (13) = True. S61 PROVEN `<1e-13` is matched to its route, never overturned.

Artifacts: `computations/session-96/s96_geom_gauge_sourcing.{py,npz,png}`.

**Substrate framing** (PARTICLE): the gauge group is **read FROM the fabric's representation-theoretic content**, never imposed on a container. Direction of explanation: `D_K + g_τ → {Isom(K,g_τ) [Killing vectors], U(A_K) [unimodular unitaries]} → gauge group → Ψ₊=ℂ¹⁶ chiral charge assignment`. Two substrate-derived readings compete — both flow FROM `D_K`, but they give different groups: the KK-isometry (`SU(3)_L × U(2)_R`, right-handed SU(2)) versus the NCG unimodular-unitary group (`U(1)×SU(2)_L×SU(3)_c`, chiral). The substrate's actual gauge content is the latter; the internal isometry of `g_τ` provides the Peter-Weyl `(p,q)` labelling of the same `D_K` spectrum. The chiral SU(2)_L charge is a property of how the fabric's spectral weight distributes over the H-block doublet (NCG route), not of the residual right-isometry of the deformed internal metric. "Gauge from pure geometry" remains true in the precise sense that the gauge group is the unimodular unitary group of the finite algebra `A_K` — itself a piece of the substrate geometry — but the *Kaluza-Klein-isometry* promise (pure metric isometry → gauge fields) is the labelling layer, not the gauge layer, for the chiral SM.

---

### §W5-7. S96-GEOM-MKK-BRACKET (kaluza-klein-theorist)

**Status**: COMPLETED
**Gate ID**: `S96-GEOM-MKK-BRACKET`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (M_KK is the compactification scale — a property of the internal geometry; a₀ is the a₀ Seeley-DeWitt moment)
**Agent**: `kaluza-klein-theorist`
**Hypothesis**: The gravity-route M_KK (1/(16πG_N)=f₂Λ²a₂^ζ/(48π²), 7.4287e16 GeV) and the Kerner gauge-metric-route M_KK (from the 4D gauge-kinetic normalization, 5.04e17 GeV) either AGREE within a stated tolerance (the 0.83-decade bracket illusory, single M_KK justified) OR the bracket is real and injects a (M_KK,Kerner/M_KK,gravity)⁴ ≈ (6.79)⁴ ≈ 2122× band into the absolute a₀ (Λ⁴) magnitude — a SECOND independent source of absolute-magnitude uncertainty beyond SDW convergence.
**Plan reference**: `sessions/session-plan/session-96-plan-w5.md` §W5-7 (consumes the W5-6 gauge-route reconciliation outcome; does NOT hard-block on W5-6 — tags a₀ band "gauge-route-disputed" if W5-6 FAILs).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- **script** `computations/session-96/s96_geom_mkk_bracket.py` — EXISTS. `grep -E 'from canonical_constants import' → "from canonical_constants import ("` ✓; `grep -E 'append_verdict' → def append_verdict(...) + append_verdict(composite, ...)` ✓.
- **data** `computations/session-96/s96_geom_mkk_bracket.npz` — EXISTS (full float64 round-trip: `R`, `log10R`, `R2`, `R4`, `rho_Lambda_{gravity,kerner}`, `rho_band`, `hierarchy_preserved`, verdict 3-tuple).
- **plot** `computations/session-96/s96_geom_mkk_bracket.png` — EXISTS (2 panels: the two M_KK routes on a log axis with the 0.83-decade bracket annotated; the Λ⁴/Λ²/Λ⁰ band-propagation bar chart R⁴=2121.58× / R²=46.06× / R⁰=1).
- **verdict line** `computations/session-96/s96_gate_verdicts.txt` — matches `^S96-GEOM-MKK-BRACKET:.* audit_sha256=[a-f0-9]{64}` ✓; dual-SHA companion row present ✓; schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple companion row present ✓ ([SIGN] trigger). `audit_sha256` = `5399e817f769e285fd3b701f5c2cffa72d9fe010bef5e287f93a860de1b6d94a` (full-64, unique in the session file — sig_5 OK).

**MCP Pre-Compute Audit** (query-first discipline; executed before writing the script):
- `get_constant('M_KK')` → 7.428660036284456e16 (alias of M_KK_gravity, CONST-FREEZE-42, not superseded). CONFIRMS the plan-cited canonical.
- `get_constant('M_KK_gravity')` → 7.428660036284456e16 GeV (spectral-zeta / Newton's-constant route, S42 CONST-FREEZE-42).
- `get_constant('M_KK_kerner')` → 5.041679838376001e17 GeV (Kerner gauge-metric route, S42 CONST-FREEZE-42, not superseded).
- `get_constant('OOM_diff_MKK')` → 0.831664779390838 (= log10(M_KK_kerner/M_KK_gravity), S42). The canonical 0.83-decade bracket anchor.
- `search_knowledge('M_KK gravity Kerner bracket 0.83 decade a0 spectral action magnitude')` → class **"Kaluza-Klein scale tower"** (two routes bracket M_KK at 0.83 decades); edge `T3-S42-CONSTANTS-SNAPSHOT --reproduces--> M_KK_kerner` ("OOM_diff = 0.831665, CONST-FREEZE-42 PASS iff < 1"); equation `a0_fold = 6440.0 (spectral action volume term)`. NOT pre-closed as a propagation gate — the band into absolute a₀ is computed here for the first time; the bracket itself is canonical.
- `get_constant('a0_zeta')`/`get_constant('a2_zeta')` → not found under those names; the exact canonical names are `a_0_FW_zeta = 6440.0` and `a_2_FW_zeta = 2776.165389` (verified directly in `canonical_constants.py`, S88 canonical-write-order promotion; regulator_pin `a_n^{ζ}`).

**Verdict**: **INFO** — the M_KK bracket is REAL. R = M_KK,Kerner/M_KK,gravity = 6.786795752868596; |R−1| = 5.787 ≫ 0.10 ⇒ PASS (bracket-illusory) excluded. Per the plan rubric this is the pre-registered most-likely INFO branch (sign PASS + magnitude-outside-PASS-band + regime MARGINAL ⇒ composite INFO via the gate-verdicts.md collapse rule). **NOT a structural FAIL**: the routes legitimately differ; the unification consistency is not broken (the FAIL branch — gauge-route M_KK breaking g₃²=g₂²=⅗g₁² — did not fire). 4-tuple: (value=R=6.7868, scheme=SA-zeta, convention=ABSOLUTE, L_max=10). Schema-v2 3-tuple: **sign_verdict=PASS** (R>1 predicted & computed; the Kerner route sits 0.83 decades ABOVE the gravity route ⇒ absolute magnitudes scale UP), **magnitude_verdict=FAIL** (|R−1|=5.787 ≫ 0.10 PASS-band ⇒ bracket real, band quantified), **regime_verdict=MARGINAL** (bracket-real is the pre-registered INFO branch; structural integrity checks all PASS — canonical-OOM match, hierarchy preserved, alias-conservative, ρ_Λ consistency). W5-6 soft-dependency NOT yet on disk at runtime ⇒ a₀ band tagged **"gauge-route-disputed"** per the plan (no hard-block, no honest-close).

**Results**:

*Both routes (canonical CONST-FREEZE-42 pins):*
- gravity route M_KK,gravity = **7.428660036284456e16 GeV** (1/(16πG_N) = f₂Λ²a₂^ζ/(48π²); through Newton's constant, Λ² weight).
- Kerner gauge-metric route M_KK,Kerner = **5.041679838376001e17 GeV** (1/g² ∝ M_KK^{d−4}·vol; through the 4D gauge-kinetic normalization).

*The bracket ratio and decade span:*
- **R = M_KK,Kerner / M_KK,gravity = 6.786795752868596** (6 s.f.: 6.78680).
- **log10(R) = 0.8316647793908398** — matches canonical `OOM_diff_MKK = 0.831664779390838` to **|Δ| = 1.78e-15** (machine precision). The 0.83-decade gravity-vs-Kerner bracket, confirmed.

*Λ⁴/Λ² band propagation into absolute magnitudes:*
- a₀ vacuum term ∝ Λ⁴ ⇒ **a₀-magnitude band = R⁴ = 2121.578558** (3.327 decades on a₀).
- a₂ gravity term ∝ Λ² ⇒ **a₂-magnitude band = R² = 46.060597** (1.663 decades on a₂).
- a₄ (YM/Higgs-quartic) ∝ Λ⁰ ⇒ **a₄-magnitude band = R⁰ = 1** (M_KK-INDEPENDENT; the dimensionless gauge-kinetic coefficient carries NO bracket).
- absolute CC magnitude cross-check (ρ_Λ = (2/π²)·a₀^ζ·M_KK⁴): ρ_Λ(gravity) = 3.974276e70 GeV⁴, ρ_Λ(Kerner) = 8.431739e73 GeV⁴ (= canonical `rho_Lambda_spectral`); ratio = 2121.578558 = R⁴ **exactly** (`rho_band_consistent=True`), confirming the Λ⁴ propagation is the same factor the canonical CC magnitude already carries via its M_KK_kerner⁴ prefactor.

*Substitution chain (the R⁴-band direction claim, with substituted numbers):*
- Step 1: M_KK,gravity = 7.428660036284456e16 GeV. Step 2: M_KK,Kerner = 5.041679838376001e17 GeV. Step 3: R := Kerner/gravity. Step 4: R = 6.786795752868596, log10(R) = 0.8316647793908398 (the 0.83-decade bracket). Step 5: a₀ ∝ Λ⁴ ⇒ band = R⁴ = 2121.578558; a₂ ∝ Λ² ⇒ band = R² = 46.060597. Step 6: R = 6.787 > 1 by 0.83 decades ⇒ |R−1| = 5.787 ≫ 0.10 ⇒ bracket REAL ⇒ factor-R⁴ = 2121.58× on a₀ (R²=46.06× on a₂); the Λ-power exponents (4, 2, 0) are R-INVARIANT (R⁴ > R² > R⁰=1 preserves the ordering) ⇒ the HIERARCHY is robust, only the absolute MAGNITUDES inherit the band.

*Plan rounded-R note:* the plan substitution chain used the rounded R=6.7868, quoting R⁴≈2122.4; the exact canonical-pinned ratio R=6.786795752868596 gives R⁴=2121.578558 (relative difference 2.5e-6 — rounding-of-R only, NOT a substrate disagreement). This section reports the exact value.

*Unification-consistency (the FAIL branch):* the FAIL criterion is "the gauge-route M_KK breaks the g₃²=g₂²=⅗g₁² unification". The Kerner-route M_KK is the canonical CONST-FREEZE-42 value; it does NOT break the unification relation (which is a constraint on the COUPLING ratios at the GUT scale, not on the absolute M_KK), so the FAIL branch did not fire — the outcome is INFO, not FAIL.

*Substrate / KK reading:* M_KK is the SU(3)-fiber size — a property of the internal geometry, fixed two canonical non-Abelian KK ways (gravitational via G_N, gauge-kinetic via Kerner). The factor-6.79 discrepancy IS the KK statement "do the gauge and gravity sectors agree on the size of the extra dimensions?" — answer: no, by 0.83 decades. Propagated through the Λ⁴ scaling of the a₀ vacuum term, this is a ~2122× band on the absolute CC magnitude — a SECOND, independent absolute-magnitude uncertainty source beyond the SDW-convergence FAIL (capstone §8.5, C2; flag alongside JACOBSON-NONLOCAL-64). CRUCIALLY: the Λ-power HIERARCHY (Λ⁴≫Λ²≫Λ⁰) is INVARIANT under the bracket — the structure of the spectral-action expansion is robust; only the absolute energy magnitudes (CC, A_s) inherit the factor-R⁴ band. **M_KK is a bracket, not a point.**

**Substrate framing**: GEOMETRIC. The direction of explanation flows FROM the substrate: D_K eigenvalues → spectral-action Seeley-DeWitt moments (a₀, a₂) → {Newton's constant G_N via a₂ at Λ²; unified gauge coupling g² via the Kerner gauge-metric normalization} → M_KK (two routes) → absolute a₀ (Λ⁴) / a₂ (Λ²) magnitude band. M_KK is NOT an externally imposed cutoff the fabric lives inside — it emerges from how the a₂ spectral weight distributes (gravity route) and how the gauge-kinetic term normalizes (Kerner route). The dimensionless R-protected moments a₀^ζ=6440 = Tr(1) and a₂^ζ=2776.165389 are unchanged; the band acts on the M_KK^n prefactors (M_KK⁴ for the vacuum term, M_KK² for the gravity term), not on the spectral coefficients. Reading M_KK as a single tunable scale that fixes the CC is the container-thinking error this gate corrects: the substrate's own geometry brackets the scale, and the Λ⁴ propagation makes the bracket a real constraint on absolute vacuum-energy magnitude while leaving the qualitative spectral-action hierarchy intact.

---

## Wave 5 Synthesis (team-lead)

Seven geometric gates, all held substrate-first (causal / Petrov / topology structure is EMERGENT from the a₂ spectral-weight distribution, never a pre-existing 4D container). Verdicts:

| Gate | Verdict | Result |
|:-----|:--------|:-------|
| W5-1 LANDAU-FE-ORDER | INFO | `F(η;τ)` derived; E13/E17 reconciled sector-split (pairing-η CONTINUOUS / band-occupation FIRST-ORDER / modulus-τ MONOTONE) |
| W5-2 PENROSE-2CONE | PASS | Asymmetric two-cone white-hole Penrose diagram; scalar cone 229× narrower; §6.2 figure gap closed |
| W5-3 TAUINF-PETROV | PASS | τ→∞ = static Type D; Ψ_ABCD conformal distances match S49 to 0.0 (ℂ²=2.582, U(1)=1.291); extends S84-W8B-95 |
| W5-4 CCC-WEYL | PASS | WCH monotone from |C|²(0)=5/14; CCC conformal-cycle OBSTRUCTED (4 over-determined reasons) |
| W5-5 OFFJENSEN-CHERN | PASS-TRIVIAL | off-Jensen Chern = 0 (non-Abelian FHS 9.78e-15) on the FULL 2-param U(2)-invariant surface |
| W5-6 GAUGE-SOURCING | FAIL | isometry≠SM (13 vs 12, SU(2) LEFT vs RIGHT); S61 used the NCG route; capstone clarification (not overturn) |
| W5-7 MKK-BRACKET | INFO | M_KK bracket R=6.787 (0.83 dec) → R⁴ a₀ band / R² a₂ band; a₄ + Λ-power hierarchy INVARIANT |

W5-6 → W5-7 coupling: W5-7's a₀ band was tagged "gauge-route-disputed" (W5-6 verdict not yet on disk at W5-7 runtime) per the soft-dependency pre-registration — no hard-block.

### What Changed

**(a) Numerical revisions** — W5-3 per-block conformal distances ℂ²=2.581989 / U(1)=1.290994 (Ψ_ABCD-exact, ratio 2); W5-7 R⁴=2121.58 a₀ band / R²=46.06 a₂ band; W5-4 |C|²(0)=5/14 reproduced to 5.5e-17, |C|²/K peaks 0.722 at the fold (sharpens session-49 "decreasing" → NET-decreasing).

**(b) Structural changes** — W5-1 E13/E17 prose-tension → sector-resolved Landau theorem; W5-2 §6.2 prose → coordinate-invariant Penrose diagram (epistemic type: prose → figure); W5-4 NEW hard-wall (substrate is WCH-consistent at genesis but is NOT a Penrose CCC cycle); W5-5 topology-trivial extended 1D-Jensen-line → 2D-physical-surface (dimensional reading change); W5-6 gauge-sourcing disambiguated (single-route → NCG-canonical + KK-isometry-labels-only).

### Effected In-Session (NON-MATH — completed before STOP)

- [x] **open_channel C11/C12 (Berry on Jensen) OPEN → RESOLVED-TRIVIAL** — W5-5: off-Jensen Chern = 0 on the full 2-param U(2)-invariant surface; the S29 "may reappear on U(2)-invariant surface" channel did NOT reappear. Knowledge `open` entity (src session-29); `/weave --update` re-extracts from this synthesis; S29 historical doc untouched (chronological-integrity). — recorded here + housekeeping §A.
- [x] **Capstone §0 gauge-route scoping note** — W5-6 disambiguation landed orchestrator-direct: NCG inner-fluctuation route (unimodular unitaries of A_K, 13 generators, S61) sources the gauge group; the KK-isometry of g_τ gives a structurally-different SU(3)_L×U(2)_R supplying the Peter-Weyl (p,q) labels, NOT the chiral SM gauge group. — `sessions/framework/phonic-exflation-equation.md:90`.
- [x] **CCC-OBSTRUCTION structural wall recorded** — W5-4: 4 obstruction reasons (genuine K~e^4τ singularity; |C|² grows not →0 at ℐ⁺; Ricci-dominated not Weyl-dominated; anisotropic Kasner boundary). Recorded in WP §W5-4 + the sp agent's MEMORY hard-wall.

### Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:---------|:-------|
| 2026-05-30 | C11/C12 off-Jensen Berry | OPEN OFF-JENSEN | CLOSED-TRIVIAL | W5-5 Chern=0, full 2-param surface |
| 2026-05-30 | §5.2 τ→∞ singularity | type uncharacterized | static Type D + conformal boundary | W5-3 |
| 2026-05-30 | §6.2 causal-structure figure | prose-only | Penrose diagram landed (canonical TikZ) | W5-2 |
| 2026-05-30 | E13/E17 transition order | prose-tension | sector-resolved (3-sector) | W5-1 |
| 2026-05-30 | CCC-aeon reading | untested | OBSTRUCTED (4 reasons) | W5-4 |
| 2026-05-30 | gauge-sourcing route | ambiguous (NCG vs KK) | NCG-canonical, KK=labels | W5-6 |

## Carry-Forward Computations

**No substrate-physics compute carry-forwards: all W5 physics outcomes closed in-session.** The plan's flagged novelty-candidates resolved in directions that do NOT generate future compute: W5-4 OBSTRUCTED the CCC cycle (a closed negative structural result, not an aeon session); W5-5 returned Chern=0 (trivial topology — no topological-protection re-open; the C11/C12 channel is CLOSED); W5-3 landed PASS static Type D (not the radiative Type N/III that would have seeded a Weyl-spinor workshop); W5-6's KK-level-charge content is the LABEL provenance already pinned by the §0 scoping note (Effected In-Session above), not a forward compute. Honest physics-compute count = 0 (per `Investigating-Workshops.md` honest-count discipline).

### CF-W5-1 — S96-GEOM-TAUINF-PETROV superseded-companion-row boilerplate touch-up (annotation hygiene; NO substrate-physics compute)

*Appended by the S96 `/rclab-investigate` consolidator: a genuinely-NEW gate-finalization annotation-hygiene item the W5 wave-synthesis did not catch (surfaced by the investigator per `Investigating-Workshops.md §"Enforcement at /rclab-investigate"`). NOT a workshop (no substrate-physics tension: static Type D is unambiguous; dynamic-G at the censored boundary is physically counterfactual and below float64). Listed here for `/rclab-plan` visibility; it is a mechanical session-close decision, not a physics compute.*

| Field | Spec |
|:------|:-----|
| **What** | The `S96-GEOM-TAUINF-PETROV` dual-SHA companion-comment text (verdict-file lines 123/128/131/134) carries the stale boilerplate "static Type D / dynamic Type G PERSIST to tau->inf" across all four Option-A re-emissions, while the authoritative `value=` field of the final canonical line (133) reads `dyn_window=tau<=6(6/12)` (dynamic resolvable only to τ≤6; asymptotic dynamic=I below round-off). DECISION: either (a) a companion-row text touch-up at session-close so the comment matches the corrected value-field window, OR (b) leave as-is (the value field is authoritative and the methodology §6 note already discloses the regime artifact). NO recompute either way — verdict permanence preserves the canonical lines byte-for-byte; only the non-load-bearing companion-comment annotation is at issue. |
| **Inputs** | `computations/session-96/s96_gate_verdicts.txt` lines 123/128/131/134 (the four `S96-GEOM-TAUINF-PETROV` companion rows); the canonical line 133 `value=` field (`dyn_window=tau<=6`); W5 WP §W5-3 methodology §6 regime-artifact disclosure. No data file, no script. |
| **Gate** | Annotation-hygiene (not a numerical PASS/FAIL): companion-comment text consistent with the canonical value-field window (resolution (a)), OR an explicit "value-field governs; comment left as historical boilerplate" note (resolution (b)). Either is acceptable; the decision is which. |
| **Effort** | <0.1 wave (a mechanical comment touch-up at session-close, or a one-line leave-as-is note). |

## Constraint-Map Updates

See the **Constraint-Map Updates** table in the Wave 5 Synthesis (team-lead) section above — 6 state changes (C11/C12 OPEN→CLOSED, §5.2 τ→∞ type, §6.2 figure, E13/E17, CCC-aeon, gauge-route).

## Files Produced

*(One row per gate. Columns: Gate | Script | Data (.npz) | Plot (.png / .tex) | JSON | Size. Expected: 7 producing scripts under `computations/session-96/`, 7 .npz, 6 .png + 1 .tex (W5-2 → `figures/penrose/exflation-asymmetric-white-hole.tex`), plus the shared verdict file `computations/session-96/s96_gate_verdicts.txt`.)*
