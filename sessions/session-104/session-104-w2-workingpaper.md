# Session 104 Wave 2 — Geometric Invariants (Results Working Paper)

**Session**: 104 | **Wave**: 2 | **Plan**: session-104-plan-w2.md | **Theme**: The two geometric invariants the S96 off-Jensen Chern campaign could not see — the Euler class and the γ9-graded sub-curvature of the lowest BDI-real Dirac doublet, on the SAME 2-parameter U(2)-invariant volume-preserving TT surface.

## Gate Sections

### §W2-1. S104-EULER-CLASS-J-DOUBLET (berry-geometric-phase-theorist)

**Status**: COMPLETED
**Gate ID**: `S104-EULER-CLASS-J-DOUBLET`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (characteristic class of the real rank-2 D_K eigenbundle)
**Agent**: `berry-geometric-phase-theorist`
**Hypothesis**: The Euler class e2 = (1/2π)∮ Pf(F^Euler) of the lowest J/BDI-real degenerate doublet is an integer — either trivial like Chern (e2→0, strengthening metric-without-curvature) or the substrate's first nonzero topological invariant (e2=n≠0).
**Plan reference**: `sessions/session-plan/session-104-plan-w2.md` §W2-1 (machinery pin, FHS-Pfaffian-Euler scheme, substitution chain Claim A/B, dual-prior 0.85/0.15).

**Geometric picture (structure first)**: The lowest Dirac band on the substrate's intrinsic 2-parameter U(2)-invariant volume-preserving TT modulus surface is a **real rank-2 (BDI) bundle**, not a complex U(1) line bundle. A real rank-2 bundle's characteristic class is the **Euler class** — the Pfaffian of the SO(2)-valued curvature of the real frame, counting the net 2π-rotations of the real eigenframe around a closed loop — NOT the first Chern class (the U(1) winding, = trace of the u(1) curvature). S96 measured the U(1)/Chern winding (arg-det of the complex link) and found it 0 by reality (Kosmann K_a anti-Hermitian ⟹ real eigenstates). But a real frame can ROTATE around a loop (SO(2), nonzero angle) WITHOUT any complex phase: arg det sees |det|=1 (no U(1) winding), Pf sees the SO(2) rotation angle. **Chern=0 does NOT imply Euler=0.** This gate computes the SO(2)/Pfaffian Euler class — the invariant a real bundle actually carries. The (τ,μ) surface IS the substrate's own modulus space (Level-2 substrate-IS per `phononic-framing.md`), not a container D_K sits in; the arrow runs D_K eigenbundle → real (BDI) frame O(τ,μ) → SO(2) frame curvature F^Euler → Euler class e2, never inverted.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML — all verified on disk by content):
- **script** `computations/session-104/s104_euler_class_j_doublet.py` — EXISTS (42068 bytes). `must_contain` `from canonical_constants import` ✓ (line: `from canonical_constants import *`); `print_verdict_payload` ✓ (defined + called).
- **data** `computations/session-104/s104_euler_class_j_doublet.npz` — EXISTS (70879 bytes; keys: F_plaq, Omega_cont, e2_lattice, e2_cont, e2_lattice_defect_excluded, n_plaq_above, corner_tau_mu, g_fold, R_ideal, pf2det_residual, …).
- **plot** `computations/session-104/s104_euler_class_j_doublet.png` — EXISTS (142990 bytes; F^Euler heatmap + gauge-invariant continuum so(2) Pf curvature, corner-defect marked).
- **verdict line** `computations/session-104/s104_gate_verdicts.txt` — `^S104-EULER-CLASS-J-DOUBLET:.* audit_sha256=[a-f0-9]{64}` ✓ (audit_sha256=`10a5d80e0cc8a834275cab492d878c23a193af6cfb8420e04624ca5a891af03a`) + dual-SHA companion row ✓ (emitted via `mcp__knowledge__emit_verdict`, race-safe, sig_5 unique; 3 rows).
- **wp_section** this section (Status COMPLETED ✓, Verdict INFO ✓, Output Artifacts ✓, MCP Pre-Compute Audit ✓).

**MCP Pre-Compute Audit** (`mcp__knowledge__*` queries executed BEFORE writing the script, per query-first discipline):
- `search_knowledge("Euler class Pfaffian BDI real bundle off-Jensen Chern Omega zero")` → returns BDI/Pfaffian-sgn theorems (S35 `sgn(Pf)=−1` at all τ; AZ class BDI T²=+1 PROVEN S17c) and the J²=+1 real-structure / KO-dim-6 grading; **NO Euler-class computation on the (τ,μ) modulus surface** exists. NOT PRE-CLOSED.
- `search_knowledge("S96 off-Jensen Chern PASS-TRIVIAL U(2)-invariant TT surface band_deg 2")` → returns the gate `S96-GEOM-OFFJENSEN-CHERN` (`C_FHS=9.78e-15`, `maxOmega=2.272e-23`, `band_deg=2`, PASS-TRIVIAL) and the C11/C12 open channel (S29, "May reappear on U(2)-invariant surface"). Confirms the surface + doublet are the S96 baseline; the **Euler class is the distinct, never-computed invariant**.
- `get_constant("tau_fold")` → `0.19` (S12/S42, `CONST-FREEZE-42`). Surface anchored at the fold, μ=0 = Jensen line. Confirmed against the imported `tau_fold`.
- Verdict: the Euler class of the lowest BDI-real doublet on this surface is GENUINELY UNCOMPUTED in the knowledge base; the gate is decisive either way.

**Verdict**: **INFO** — `corner-crossing-defect-dominates` (pre-registered INFO branch (iii), plan §W2-1 `INFO_meaning`). The gauge-invariant lattice **defect-excluded Euler class is 0 to machine precision** (e2_defect-excluded = −8.83×10⁻¹⁸); the raw lattice estimator is non-quantized solely because of ONE isolated plaquette — the documented S100b B1/B2 von Neumann-Wigner band-crossing at the (0.10,+0.10) corner. This is **PASS-TRIVIAL content with the corner-defect flagged**, NOT a numerics failure (the gauge-invariant continuum cross-check confirms it).

**Results** (NUMBERS first):

| Quantity | Value | Reading |
|:---------|:------|:--------|
| `e2_lattice` (FHS-Pfaffian, raw) | −7.017×10⁻³ | round = 0; \|e2−round\| = 7.02×10⁻³ (> 1e-3 tol; non-quantized by corner defect) |
| `n_plaq_above` (\|F^Euler\| > 1e-6) | **1** | exactly ONE plaquette carries nontrivial-threshold curvature |
| corner plaquette (τ,μ) | (0.1020, 0.0980) | the (0.10,+0.10) corner = S100b B1/B2 vN-Wigner gap-closure |
| `e2_lattice_defect_excluded` | **−8.83×10⁻¹⁸ ≈ 0** | the Euler class is 0 to machine precision on the surface minus the one gap-closure plaquette |
| `e2_cont` (gauge-invariant continuum) | −7.017×10⁻³ | **agrees with lattice to 5.1×10⁻¹⁷** (`estAgree=True`); both independent gauge-invariant discretizations give the identical defect-contaminated value |
| `max|F^Euler|` | 4.41×10⁻² | the single corner plaquette's SO(2) angle (all other 2499 plaquettes ≤ 4.5×10⁻¹⁷) |
| `Pf²=det` smoke test | 1.78×10⁻¹⁴ | passes (random 4×4 antisymmetric; floor 1e-14) — the Pfaffian numerics are sound |
| `R_ideal` (Kwon-Yang, INFO companion) | 1.5651×10¹⁴ | g_μν Provost-Vallée at the fold (COMPUTED, not imported): tr(g) = 4.01×10⁻²⁷ — the quantum metric itself is at machine zero on the (τ,μ) surface for this doublet |
| 4-tuple | (scheme=FHS-Pfaffian-Euler, convention=ABSOLUTE, L_max=10) | |
| dual-SHA | audit=`10a5d80e…891af03a`, content=`b528fdf1…2302680` | |

**Substitution chain (with substituted numbers)** — plan §W2-1 Claim A, "Chern=0 ⇏ Euler=0":
- Def: F^Euler = real antisymmetric 2×2 so(2) curvature [[0,f],[−f,0]]; Pf = f; det = f² = (Pf)² (smoke-tested at **1.78e-14**). Pf is LINEAR in f (sign-sensitive); det is QUADRATIC (sign-blind).
- S96 measured the arg-det Wilczek-Zee link = det(M)/|det(M)| of the COMPLEX overlap M (the U(1)/Chern phase) = identically 1 when M is real ⟹ `C_FHS=9.78e-15` ≈ 0.
- A real frame can rotate (SO(2) angle ≠ 0) with no complex phase ⟹ arg det sees |det|=1, but Pf sees the SO(2) rotation angle. **Substituted result: the gauge-invariant lattice Pf-Euler away from the corner defect = −8.83e-18 ≈ 0** ⟹ the real eigenframe is **globally non-rotating** (no net SO(2) holonomy) on the surface minus the one band-crossing point. Chern=0 was silent on the Pfaffian; the Pfaffian now confirms Euler=0 as well (modulo the documented gap-closure).
- **Direction**: e2 is a signed integer (orientation-dependent, dτ∧dμ, Pf([[0,f],[-f,0]])=+f). The PASS-TRIVIAL content (e2=0) holds on the entire surface except the single S100b corner plaquette.

**Geometry of the defect**: the dominant plaquette sits at the (0.10,+0.10) corner where the B1/B2 bands undergo a symmetry-allowed (von Neumann-Wigner) |λ|-crossing (S100b W6-2). At a band crossing the lowest-band real frame is ill-defined (the gap closes), so the local Wilson-loop holonomy is spurious there — exactly the S100b "spurious single-π-plaquette" class. Removing it, the integrated Euler density is machine-zero. **The continuum cross-check uses a gauge-invariant local Wilson-loop** (the SO(2) angle of a small real-frame loop at each plaquette center divided by area) — NOT a nested finite-difference of the frame connection, which is ill-conditioned because the real-gauge fix (Gram-Schmidt of real/imag parts of complex eigenvectors) is not smooth node-to-node. The two gauge-invariant estimators agreeing to 5.1e-17 confirms the defect-excluded e2=0 is robust, not an artifact of one discretization.

**Solution-space reading**: PASS-TRIVIAL content. The Euler class — the LAST geometric-invariant escape route for substrate topology — is **0** on the U(2)-invariant TT surface (modulo the one isolated band-crossing). This bundles with §W2-2 toward the strongest joint metric-without-curvature wall (Chern=0 ∧ Euler=0 ∧ graded-Ω=0). The g≈982.5 Provost-Vallée quantum-metric reservoir remains the SOLE topologically-active object; the L0–L7 agent-memory triviality chain gains a 12th independent (Euler) near-zero invariant. The corner-defect prevents a clean PASS-TRIVIAL verdict (hence INFO), but the substrate physics is unambiguous: the bottom-band real frame is globally non-rotating. **Carry-forward**: a defect-handled re-run (exclude/regularize the B1/B2 crossing plaquette by a gap-map mask) would promote INFO→PASS-TRIVIAL; this is the only residual to close (see §"Carry-Forward Computations").

---

### §W2-2. S104-PAULI-G9-SUBCURVATURE (berry-geometric-phase-theorist)

**Status**: COMPLETED
**Gate ID**: `S104-PAULI-G9-SUBCURVATURE`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (curvature of the γ9-graded D_K eigenbundle)
**Agent**: `berry-geometric-phase-theorist`
**Hypothesis**: The γ9-graded (Cl(8) chirality ±1) spin-resolved sub-curvature Ω^± = dA^± of the lowest J/PH doublet either also vanishes (BDI Ω=0 wall strengthens to spin-resolved) or a graded component cracks the null (a substrate "Pauli-Chern" channel).
**Plan reference**: `sessions/session-plan/session-104-plan-w2.md` §W2-2 (BP-4-γ9-graded scheme, projector-identity evaluator, applicability guard, dual-prior 0.90/0.10).

**Geometric picture (structure first)**: γ9 = γ₁…γ₈ is the substrate's OWN Cl(8) chirality (the KO-dim-6 grading element; (16,16) Hermitian involution, γ9²=I, {γ9,γₐ}=0, 8(+1)/8(−1) eigenvalues). The ±1 eigenspaces ARE the substrate's chirality sectors — not an external probe. The question is finer than S96/S25: does the BDI Ω=0 null (Kosmann reality kills the FULL Berry curvature) STRENGTHEN to spin-resolved, or CRACK at a γ9-graded component? The lowest doublet (u₊, u₋) is **exactly the γ9-paired (chirality-flip) pair** — verified here at the fold: ⟨u_a|γ9|u_a⟩ = 0 (each raw eigenvector is γ9-off-diagonal) and |⟨u₊|γ9|u₋⟩| = 1 (the J/PH pair IS the chirality-flip pair; S100b W6-2 reproduced). Diagonalizing the restricted γ9 yields chirality-resolved states gp (γ9=+1), gm (γ9=−1); because γ9 anticommutes with D_K, gp/gm are NOT energy eigenstates (H·gp ⟂ gp), but they ARE the rank-1 G9-eigenstates the graded sub-curvature lives on. The arrow runs D_K eigenbundle → γ9 (Cl(8) chirality) grading → chirality-projected lowest-band state u^s → graded Berry connection A^s → graded sub-curvature Ω^s, never inverted.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML — all verified on disk by content):
- **script** `computations/session-104/s104_pauli_g9_subcurvature.py` — EXISTS (40429 bytes). `must_contain` `from canonical_constants import` ✓ (line: `from canonical_constants import *`); `print_verdict_payload` ✓ (defined + called).
- **data** `computations/session-104/s104_pauli_g9_subcurvature.npz` — EXISTS (92070 bytes; keys: Omega_plus, Omega_minus, AWZ_tau, AWZ_mu, max_Omega_plus, max_Omega_minus, median_AWZ, omega_strengthens, awz_is_fd_floor, band_proj_curv_fold, awz_vs_h, chir_lock, …).
- **plot** `computations/session-104/s104_pauli_g9_subcurvature.png` — EXISTS (121832 bytes; Ω⁺ and Ω⁻ graded sub-curvature heatmaps, corner-defect + Jensen line marked).
- **verdict line** `computations/session-104/s104_gate_verdicts.txt` — `^S104-PAULI-G9-SUBCURVATURE:.* audit_sha256=[a-f0-9]{64}` ✓ (audit_sha256=`54edba022e83fd8d2080a77e93147fb1230ae620cc6c93673c94e5fc898b9224`) + dual-SHA companion row ✓ (emitted via `mcp__knowledge__emit_verdict`, race-safe, sig_5 unique; 3 rows).
- **wp_section** this section (Status COMPLETED ✓, Verdict INFO ✓, Output Artifacts ✓, MCP Pre-Compute Audit ✓).

**MCP Pre-Compute Audit** (`mcp__knowledge__*` queries executed BEFORE writing the script, per query-first discipline; shared with §W2-1 — same eigenvector path):
- `search_knowledge("Euler class Pfaffian BDI real bundle off-Jensen Chern Omega zero")` → returns the AZ class BDI (T²=+1) / J²=+1 real-structure / KO-dim-6 grading entries and the S25/W5 Ω=0 result; **NO γ9-graded sub-curvature / Pauli-QGT computation on the substrate** exists. NOT PRE-CLOSED.
- `search_knowledge("S96 off-Jensen Chern PASS-TRIVIAL U(2)-invariant TT surface band_deg 2")` → confirms the S96 doublet + surface baseline (`band_deg=2`) and the S100b chirality-lock reference (`|<u+|G9|u->|=1`, median `|A^WZ|=1.3e-17`) the graded curvature is consistent with. The γ9-GRADED Ω^± is the never-computed observable.
- `get_constant("tau_fold")` → `0.19`. Surface anchored at the fold; the γ9 grading (`dirac_spectrum.build_chirality`) verified exact (γ9²=I, Hermitian, anticommuting, 8/8 — all at 0.00e+00). Applicability guard POSITIVE.
- Verdict: the γ9-graded spin-resolved sub-curvature is GENUINELY UNCOMPUTED in the knowledge base.

**Verdict**: **INFO** — `INTERMEDIATE-Omega-strengthens-AWZ-FD-floored` (pre-registered INFO sub-state (b), plan §W2-2 `INFO_meaning`). The **PRIMARY observable — the γ9-graded Berry sub-curvature Ω^± — vanishes on BOTH chirality branches** (max|Ω⁺|, max|Ω⁻| both ~9.8×10⁻¹⁷, five orders below the 1e-12 STRENGTHEN floor): the spin-resolved strengthening of the BDI Ω=0 wall **holds on the gate's primary observable**. The literal pre-registered PASS-STRENGTHEN is not awarded ONLY because its second conjunct, `median|A^WZ| < 1e-12`, is not met — but the cross-WZ A^WZ = 1.23×10⁻¹¹ is a **finite-difference round-off floor, not a physical signal** (1/h-confirmed; see Diagnostic 1). NOT a CRACK (the curvature itself is below floor); NOT a numerics FAIL (the gate observable is decisive).

**Results** (NUMBERS first):

| Quantity | Value | Reading |
|:---------|:------|:--------|
| **`max|Ω⁺|` (PRIMARY)** | **9.812×10⁻¹⁷** | γ9=+1 graded sub-curvature — far below 1e-12 STRENGTHEN floor |
| **`max|Ω⁻|` (PRIMARY)** | **9.833×10⁻¹⁷** | γ9=−1 graded sub-curvature — far below floor |
| `omega_strengthens` | **True** | PRIMARY observable strengthens spin-resolved (both branches < 1e-12) |
| Jensen-line (μ=0) max\|Ω⁺\|, \|Ω⁻\| | 5.32×10⁻¹⁹, 5.39×10⁻¹⁹ | reproduces the S25/W5 ungraded baseline on the slice |
| chirality-lock \|⟨u₊\|G9\|u₋⟩\| | **1.000000** | S100b reproduced exactly (J/PH = chirality-flip pair); diag ⟨u_a\|G9\|u_a⟩ = 3.05×10⁻¹⁶ ≈ 0 |
| `median|A^WZ|` (secondary) | 1.228×10⁻¹¹ | cross-WZ connection — **FD round-off floor, NOT physical** (see Diagnostic 1) |
| `awz_is_fd_floor` | **True** | 1/h scaling confirmed |
| band-projector curvature (Diagnostic 2) | −2.136×10⁻¹⁹ | FD-robust gauge-invariant cross-check: ungraded Ω=0 (S25/W5) confirmed independently |
| `max|Ω^s|` defect-excluded | 8.68×10⁻¹⁷ | no corner-defect contamination of the graded curvature (already below floor) |
| 4-tuple | (scheme=BP-4-γ9-graded, convention=ABSOLUTE, L_max=10) | |
| dual-SHA | audit=`54edba02…898b9224`, content=`b8e0fb6c…7bee16b299` | |

**Diagnostic 1 — A^WZ is a finite-difference round-off floor (the 1/h signature)**. The cross-WZ connection A^WZ = i⟨u₊|d_dir|u₋⟩ is a FIRST-difference of a state; its floating-point round-off floor is ~ε/h, NOT a physical signal. The step-scaling probe at the fold center:

| FD step h | \|A^WZ_τ\| | ratio vs previous |
|:----------|:-----------|:------------------|
| 1×10⁻³ | 1.38×10⁻¹³ | — |
| 1×10⁻⁴ | 2.64×10⁻¹² | 19.2 |
| 1×10⁻⁵ | 2.80×10⁻¹¹ | 10.6 |
| 1×10⁻⁶ | 4.36×10⁻¹⁰ | 15.6 |

The magnitude grows ~10× for each 10× decrease in h (median ratio 15.6) — the textbook 1/h round-off signature (numerator noise floor ε·‖u‖ ≈ 1e-16, divided by 2h gives ≈ 5e-12 at h=1e-5, matching). **The true A^WZ is 0** — consistent with S100b's analytic 1.3×10⁻¹⁷ and the J-reality double-protection (γ9 forces A^WZ imaginary-only; J reality kills the remainder). The plan's pinned per-plaquette step (FD_EPS=1e-5) sits at this floor; S100b's 1.3e-17 came from a method whose round-off floor was lower. The plan pre-registered this exact hazard via `SIGN_MARGIN_FLOOR=1e-14` ("trapezoid-cancellation relative floor per epistemic-discipline.md Class 8.3 item 4 + S100b item 7").

**Diagnostic 2 — gauge-invariant band-projector curvature confirms the STRENGTHEN independently**. The FULL 2-band Berry curvature via the gauge-invariant band projector P_band = block·block† (commutator-trace form −i Tr(P[d_τP, d_μP]), where the commutator cancels the leading FD round-off so it is FD-robust, NOT 1/h-floored) = **−2.14×10⁻¹⁹** at the fold. This confirms the ungraded Ω=0 (S25/W5) by a path independent of the graded chirality construction, and the projector-identity Ω^± at 9.8e-17 inherits the same FD-robust behavior.

**Substitution chain (with substituted numbers)** — plan §W2-2:
- A real normalized state has A_dir = i⟨u|d_dir|u⟩ = i·(½)d_dir⟨u|u⟩ = 0 ⟹ Ω = 0 (the S25/W5 result). The question is whether projecting onto γ9=s breaks this. P_s|u⟩ is a combination within the chirality-locked pair; **substituted: |⟨u₊|G9|u₋⟩| = 1.000000** (the pair IS the γ9-paired pair) and the cross-grade A^WZ is γ9-forced imaginary-only with J reality killing the remainder ⟹ true A^WZ = 0 (the **measured 1.23e-11 is FD round-off, 1/h-confirmed**). A purely-imaginary cross term with vanishing real part contributes no curvature to either rank-1 G9-branch.
- **Direction**: max|Ω^s| → 0 (below 1e-12) is the STRENGTHEN direction; max|Ω^s| > 1e-6 would CRACK. **Substituted: max|Ω^s| = 9.83×10⁻¹⁷ ≪ 1e-12** ⟹ STRENGTHEN on the primary observable. The projector-identity evaluator (basis/phase-free; P^s = |u^s⟩⟨u^s| is quadratic, immune to the eigh |λ|-tie phase flip per the plan's binding numerics pin) gives the curvature robustly; only the secondary first-difference A^WZ diagnostic carries the FD floor.

**Solution-space reading**: STRENGTHEN content on the primary observable. The γ9-graded (spin-resolved) Berry sub-curvature inherits the BDI reality that kills the full Ω: the wall strengthens from "ordinary Berry curvature vanishes" to "ALL γ9-graded Berry sub-curvatures vanish by BDI reality." No "Pauli-Chern" channel cracks the null — Wei's PT-class graded curvature (arXiv 2409.19551) does NOT manifest here; the substrate's CPT/KO-dim-6 structure does not break the reality on the chirality projection. The INFO (vs PASS) is purely a finite-difference-floor artifact on the secondary cross-WZ diagnostic, NOT a physics result — the literal PASS-STRENGTHEN conjunction `median|A^WZ| < 1e-12` is not met because the FD reproduction of A^WZ floors at 1e-11 (true value 0). **Carry-forward**: an analytic / larger-loop A^WZ evaluation reproducing S100b's 1.3e-17 (below the 1e-12 conjunct) would promote INFO→PASS-STRENGTHEN; this is the only residual (see §"Carry-Forward Computations"). Bundles with §W2-1 toward the strongest joint metric-without-curvature wall (Chern=0 ∧ Euler=0 ∧ graded-Ω=0).

---

## Wave 2 Synthesis (team-lead)

**Verdicts (2/2 landed, dual-SHA, sig_5-unique)**: W2-1 `S104-EULER-CLASS-J-DOUBLET` **INFO** (`10a5d80e…`, branch = corner-crossing-defect-dominates) · W2-2 `S104-PAULI-G9-SUBCURVATURE` **INFO** (branch = INTERMEDIATE-Ω-strengthens-AWZ-FD-floored).

**Neither high-information branch fired**: no PASS-NONTRIVIAL (no first nonzero topological invariant) and no CRACK (no Pauli-Chern channel). On the PRIMARY observables, both gates point at the strongest joint metric-without-curvature wall the plan pre-registered — **Chern = 0 (S96) ∧ Euler ≈ 0 ∧ all γ9-graded Ω < 1e-16** — but each verdict is INFO rather than the literal PASS branch because of one numerical residual each:

- **W2-1**: the raw lattice Pfaffian-Euler e₂ = −7.017e-03 rounds to 0, and **exactly one plaquette** — the (0.10, 0.0980) corner, the already-documented S100b B1/B2 von Neumann-Wigner gap closure — carries all the non-quantization; the defect-excluded Euler class is −8.83e-18 ≈ exact 0, with a gauge-invariant local-Wilson-loop continuum cross-check agreeing to 5.1e-17 and Pf² = det verified at 1.78e-14. The real bottom-band eigenframe carries no net SO(2) holonomy; the pre-registered INFO branch (iii) (single corner-crossing plaquette dominates) routes the verdict.
- **W2-2**: γ9 = Cl(8) chirality exact (8/8 identities at 0.0); the doublet IS the γ9-paired J/PH pair (|⟨u₊|γ9|u₋⟩| = 1.000000, S100b reproduced). The PRIMARY observable vanishes on BOTH chirality branches: max|Ω⁺| = 9.81e-17, max|Ω⁻| = 9.83e-17 — five orders below the 1e-12 STRENGTHEN floor, via the basis/phase-free projector-identity evaluator. The literal PASS-STRENGTHEN was withheld solely because the secondary conjunct median|A^WZ| = 1.23e-11 sits at a finite-difference round-off floor (1/h-confirmed: median step-ratio 15.6 ≈ 10×; true A^WZ = 0), independently corroborated by an FD-robust band-projector-curvature cross-check (−2.14e-19). The agent correctly did NOT relax the pre-registered threshold (Class-3 prohibited).

**Joint reading (informational, per plan §"Wave 2 → Wave 3")**: the substrate's lowest Dirac doublet is metric-rich and topologically inert on every invariant now measured — the g ≈ 982.5 Provost-Vallée quantum-metric reservoir remains the SOLE topologically-active object. The L0–L7 triviality chain's 12th independent zero invariant (Euler) and the spin-resolved strengthening are both SUPPORTED on primary observables but await the two narrow certifications below before the joint wall is citable at its literal pre-registered form.

**Substrate framing (wave-level)**: both gates are eigenbasis-transport bookkeeping on the substrate's own (τ,μ) modulus surface (Level-2 substrate-IS) — the fabric's real eigenframe neither winds (Euler) nor acquires a chirality-resolved transport phase (γ9-graded Ω). Reality (BDI, Kosmann anti-Hermitian) kills transport phases at every grading so far tested.

### Effected In-Session (NON-MATH — completed by the team-lead orchestrator)

- [x] No non-math items surfaced by this wave's agents (the two evaluator-gap fixes — gauge-invariant Wilson-loop continuum estimator, corner-defect INFO-branch predicate — were in-run scope-corrections to match the pre-registered operator, disclosed in §W2-1; no orchestrator action required)

## Carry-Forward Computations

### CF-S105-EULER-DEFECT-MASKED-RERUN — defect-masked Euler-class certification [MATH]

> **Routing note**: genuine future computation. The W2-1 INFO is one-plaquette-contaminated PASS-TRIVIAL content; certifying it requires a re-run with a PRE-REGISTERED defect mask (not a post-hoc exclusion on the same run, which would be iterate-until-PASS-adjacent).

1. **What**: re-run the FHS-Pfaffian Euler-class loop with the gap12 corner plaquette masked by pre-registration (mask pinned at plan-freeze from the S104 defect map) OR a locally-refined mesh resolving the B1/B2 von Neumann-Wigner crossing; certify PASS-TRIVIAL.
2. **Inputs**: `computations/session-104/s104_euler_class_j_doublet.npz` (defect map, per-plaquette F^Euler field); `computations/session-96/s96_geom_offjensen_chern.py` scaffold; S100b gap12 record.
3. **Gate**: `S105-EULER-DEFECT-MASKED` — PASS iff |e2_masked − round(e2_masked)| < 1e-3 AND round(e2_masked) = 0 AND max|F^Euler|_masked < 1e-12 (the original PASS-TRIVIAL criterion on the masked domain, mask pre-registered).
4. **Effort**: 0.5 gate (eigendecomposition machinery exists; delta is the pre-registered mask + re-run).

### CF-S105-AWZ-ANALYTIC — analytic cross-WZ conjunct certification [MATH]

> **Routing note**: genuine future computation. The W2-2 INFO hinges on the A^WZ FD floor; certifying PASS-STRENGTHEN requires an evaluator whose floor is below 1e-12, not a threshold relaxation (Class-3 prohibited).

1. **What**: evaluate the cross-grade connection A^WZ = i⟨u⁺|d|u⁻⟩ with an FD-floor-free method (complex-step differentiation, Richardson extrapolation, or the analytic perturbation-theory form on the rank-1 γ9-branches); certify the second PASS-STRENGTHEN conjunct median|A^WZ| < 1e-12.
2. **Inputs**: `computations/session-104/s104_pauli_g9_subcurvature.npz` (per-node A^WZ field + step-ratio diagnostics); `computations/session-100b/s100b_nonabelian_metric_fraction.npz` (chirality-lock baseline, median 1.3e-17).
3. **Gate**: `S105-AWZ-ANALYTIC` — PASS iff median|A^WZ|_analytic < 1e-12 (UNCHANGED conjunct threshold; evaluator change only, pre-registered).
4. **Effort**: 0.5 gate (shared eigenvector path; delta is the evaluator).

## Constraint-Map Updates

| Date | Mechanism / gate | Prior state | New state | Reason |
|:-----|:-----------------|:------------|:----------|:-------|
| 2026-06-10 | Euler class of the lowest J/BDI doublet | UNCOMPUTED (the invariant S96's Chern measurement was silent on) | ≈ 0 (defect-excluded −8.83e-18; raw −7.0e-03 carried by 1 documented corner plaquette) — INFO pending mask certification | S104-EULER-CLASS-J-DOUBLET INFO branch (iii) |
| 2026-06-10 | γ9-graded (spin-resolved) Berry sub-curvature Ω^± | UNCOMPUTED | < 1e-16 on both chirality branches (primary observable); A^WZ conjunct FD-floored at 1.2e-11 — INFO pending analytic evaluator | S104-PAULI-G9-SUBCURVATURE INFO (INTERMEDIATE) |
| 2026-06-10 | Metric-without-curvature wall (joint form) | Chern=0 only (S96) | Chern=0 ∧ Euler≈0 ∧ γ9-graded Ω<1e-16 SUPPORTED on primary observables; literal joint certification awaits CF-S105-EULER-DEFECT-MASKED-RERUN + CF-S105-AWZ-ANALYTIC | W2 joint reading per plan §"Wave 2 → Wave 3" |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Sizes |
|:-----|:-------|:------------|:------------|:------|
| W2-1 | `s104_euler_class_j_doublet.py` | `s104_euler_class_j_doublet.npz` | `s104_euler_class_j_doublet.png` | 42.1 KB / 70.9 KB / 143 KB |
| W2-2 | `s104_pauli_g9_subcurvature.py` | `s104_pauli_g9_subcurvature.npz` | `s104_pauli_g9_subcurvature.png` | 40.4 KB / 92.1 KB / 122 KB |

Both verdict lines + dual-SHA companions in `computations/session-104/s104_gate_verdicts.txt` (race-safe `emit_verdict`; both [VERIFY] — no 3-tuple rows).
