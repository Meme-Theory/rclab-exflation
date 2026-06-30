# WS-S113-2 TAUFOLD — Round 2 (rebuttal)

**lizzi-spectral-functional-theorist — Round 2, rebuttal**
**Workshop**: WS-S112-2 TAUFOLD. Responding to `transit-r1.md` (Reading A, threshold-crossing form).

**One-line**: Transit honestly abandoned the *attractor* reading and pivoted to a "van Hove cusp selects τ_fold, the transit merely crosses it" frame — but the S85 theorem that frame leans on is, by its own statement, a **non-stationarity** theorem (which IS my Reading-B claim), and as a *selector* of the value 0.190 it is regulator-CONDITIONAL: it verifies at a **pre-frozen** 0.190, computes **0.221** from scratch (L_max=8, FAIL), and FAILS under an alternative mesh (L_max=5). A selector whose location moves with the regulator is the textbook scheme-dependent feature my domain exists to flag — so the cusp does not rescue τ_fold from the empirical-import verdict; it relabels the same un-fixed number as "where-on-the-flank."

---

## 1. What transit got RIGHT — concede it cleanly, because the rebuttal is stronger for it

I will not strawman a careful R1. Three of transit's moves are correct and I adopt them:

1. **The attractor reading genuinely fails — and transit said so first.** Transit's own S112 EOM integration (transit-r1 §6, Threat 1) launches the modulus FROM τ_fold with v=26.545, overshoots to τ_max≈1.30, and settles at τ_final≈0.184 — *not* 0.190. So "a dynamical mechanism drives τ → 0.190 and holds it there" is false. **We agree.** This is exactly my R1 §4(a): a monotone action gives no interior attractor. Transit reached the same conclusion from the dynamics side. That convergence is not a draw — it removes the only reading on which Reading A could have *beaten* Reading B outright (a zero-parameter EOM attractor at 0.190). It is gone, by transit's own computation.

2. **The threshold-crossing frame is structurally legitimate.** Transit is right that in a non-equilibrium theory a quench "selects" T_c without settling there — nobody calls T_c "tuned" because the system ends at T≠T_c. I concede the *frame* fully. A modulus can be physically distinguished as "the threshold the flow is forced to cross" even with no well there. This is a real and substrate-first notion of distinguished-location.

3. **A van Hove cusp is categorically NOT a potential well.** Transit (§1) and I agree the NO-WELL-ONE-LOOP PASS is *consistent* with — not destructive of — a cusp at τ_fold, because a DOS singularity sits at non-stationarity of S. I grant this. The S95 corridors closed the variational selectors; they do not, by themselves, refute a cusp.

So the debate is now correctly localized. Reading A no longer claims an attractor. It claims: **the cusp is a parameter-free, substrate-IS selector pinning 0.190, and the transit crosses it like a quench crosses T_c.** Everything rides on whether the cusp genuinely *is* a parameter-free selector at 0.190. That is a spectral-geometry question — the center of my domain — and it is where transit's case breaks.

---

## 2. The theorem transit invokes proves NON-STATIONARITY — which is my claim, not a refutation of it

The load-bearing object in transit-r1 is `S85-W10-TAU-FOLD-UNIQUENESS-VAN-HOVE-THEOREM` (knowledge-index `proven_1424`/`proven_1905`; co-authored **connes + lizzi** — it is partly mine, so I can speak to what it does and does not establish). Transit names it "τ_fold has a PROVEN substrate selector." Let me quote what it actually proves, from the S85 W10 plan substitution chain (session-85-plan-w10.md, the gate's own Step 6 and locking condition):

> "`dS/dτ|_{τ_fold} = +58,673 ≠ 0` **locking the cusp as non-stationary**" … "Claim: τ_fold is a van Hove CUSP (**non-stationary**), **not a critical point**" … Step 6 "(Direction, **cusp non-stationarity**)".

The theorem's **verb is non-stationarity**. Its content is: *the spectral action has NO critical point at τ_fold* (`dS/dτ=+58,672.80 ≠ 0`, verified this round: a point with nonzero gradient is not a critical point). That is **precisely Reading B's claim** — the action does not select τ_fold by stationarity — stated as a theorem and co-signed by me. Transit is citing, as evidence *for* dynamical selection, a theorem whose mathematical content is that *the action does not select τ_fold*. The theorem is real and permanent; what it proves is the **absence** of the variational selector, not the presence of a substitute one.

This is the single most important correction to Reading A: the "PROVEN selector" is a PROVEN *non-selector* (in the action-stationarity sense). It establishes that τ_fold is a DOS cusp; it does not establish that the cusp's *location* picks out 0.190 parameter-free. Those are different claims, and only the second would defeat Reading B.

(Hygiene note, non-substantive to the physics: transit's pointer "§VII.M.W10-3" is a mislabel — that registry slot actually holds an unrelated S86 c_sub Γ-INEXACT residual entry; the genuine theorem is the gate `S85-W10-TAU-FOLD-UNIQUENESS-VAN-HOVE-THEOREM` / `proven_1424`, per mack's S112 W2 citation-anchor repair, registry line ~22259. Transit's physics does not rest on the label, so I set this aside.)

---

## 3. As a *selector of 0.190*, the cusp is regulator-CONDITIONAL — the scheme-dependence my domain exists to detect

Grant transit the threshold-crossing frame in full. The frame needs a selector that is **parameter-free and regulator-independent** — that is the whole point of the T_c analogy: a thermodynamic singularity is a property of the spectrum that does NOT move when you change your computational scheme. Does the substrate's cusp clear that bar? The verdict files say no, and transit (to its credit) disclosed the crack itself (Threat 3). Here is the full picture, with the gap computed exactly:

| Setting | What was computed | Result |
|:--|:--|:--|
| `S85-VAN-HOVE-CUSP-THEOREM`, **L_max=8**, DOS-cusp **from scratch** | the cusp peak location, computed | **0.221, FAIL** |
| `S85-W10-TAU-FOLD-UNIQUENESS-...`, **L_max=10** | non-stationarity **at the FROZEN 0.190** (`convention=canonical_constants-S85-freeze`; `value='promoted'`, a status string) | PASS — *verifies at imported 0.190, does not derive it* |
| `S84-ALTERNATIVE-TAU-MESH-UNIQUENESS`, **L_max=5**, alt mesh | uniqueness under a different τ-mesh | **FAIL (value=0)** |
| `S111-CF-TAUCUSP` | refined cusp vs canonical | INFO, `relDev=0.1626`, `cuspExcessFrac=0.4695` |

Three facts, each fatal to "parameter-free selector":

**(a) The from-scratch cusp lands at 0.221, not 0.190 — a 31/190 = 16.3% miss** (Sage-exact this round; cross-checks S111-CF-TAUCUSP `relDev=0.1626` to <0.001). The number the *spectral computation* produces is 0.221. The number the framework *uses* is 0.190. The "selector" and the "selected value" differ by 16%.

**(b) The L_max=10 "uniqueness" PASS did not compute 0.190 — it imported it.** Its convention is literally `canonical_constants-S85-freeze`; the plan (lines 374, 381-383) confirms "canonical_constants `tau_fold=0.190` is the pinned value," and the verdict value is the status string `'promoted'`, not a computed location. So the PASS verifies *the cusp is non-stationary at a value taken as given*; it is silent on whether the cusp's location, computed freely, is 0.190. It is not (see (a)).

**(c) The cusp location is regulator/mesh-dependent.** 0.221 at L_max=8 from scratch; FAIL under the L_max=5 alternative mesh. The S85 plan (line 473) *pre-registered this very escape*: "regulator-dependent, in which case τ_fold uniqueness requires a STRONGER" condition — i.e., the authors knew the uniqueness might be a truncation artifact and flagged it. A van Hove singularity that *moves when you change L_max or the mesh* is, in my functional-pluralism language, the definition of a **scheme-dependent feature** — not a structural invariant. This is the same diagnostic that separates the (scheme-dependent) cosmological constant a_0 from the (scheme-robust) ratios: I ask whether the quantity survives the change of regulator. The cusp *location* does not.

**Contrast with the real selectors.** The things the framework legitimately treats as parameter-free substrate constants — the t=1/2 closure (`u′(1/2)=0`, an exact symbolic identity at the gravity AND YM grades, grade-by-grade, f-INDEPENDENT), the α_s=n_s²−1 lock, the KO-dim=6 — are regulator-INDEPENDENT to machine precision. T_c in a genuine quench is likewise a regulator-independent thermodynamic singularity. The τ_fold cusp is in the *other* class: its location is L_max/mesh-conditional and 16% off the used value. A threshold-crossing selector built on a regulator-dependent threshold does not pin a parameter-free 0.190; it pins "somewhere in a cusp region whose location depends on your truncation, and we froze the canonical at 0.190 on its flank."

---

## 4. So does the cusp defeat "τ_fold is empirical, parallel to M_KK"? No — it relabels the free number

Transit's sharpest claim (its §2, §7, and decisive-consideration) is that my M_KK parallel is **false at the selector level**: "M_KK has no selector; τ_fold has a proven one." I now answer this directly, because it is the crux.

**The parallel survives, because the cusp does not select the *value*.** Strip the cusp claim to what is actually proven (§2–§3): there is a DOS non-analyticity in the τ-flow whose computed location is regulator-dependent (0.221 at L_max=8), and the canonical value 0.190 was frozen on its flank. That is not "the substrate fixes τ_fold = 0.190." It is "the substrate has a cusp *region*, and *which point in/near it* is the physical fold (0.190 vs 0.221 vs the crossing point) is set by an additional choice." Transit itself concedes this (Threat 3, Reading-B-favorable bullet): "the 16% gap between the selector (cusp peak 0.221) and the selected value (0.190) means the selector does NOT cleanly pick 0.190 — there is a residual tuning of *where on the flank* the canonical value sits."

That residual is the empirical input. The structure is identical to M_KK and to the rank-1 Normalization-Non-Universality theorem (§VII.BS, STAGE-3-PERMANENT): **the substrate fixes the dimensionless *shape* (here, that there is a cusp; that the flow crosses it monotonically; the transit rate-class) and imports one *value* (here, the precise fold location on the flank).** M_KK: substrate fixes all dimensionless content, imports one scale. τ_fold: substrate fixes the cusp *structure*, imports the fold *location*. The selector transit found constrains the value to a ~16%-wide cusp region — it does not pin it. A constraint-to-a-region is weaker than a selection-of-a-value, and the gap between them is exactly the empirical residual.

I therefore *refine*, not retract, the M_KK parallel: τ_fold is not "as unconstrained as M_KK" (M_KK has N₃=0, no substrate handle at all; τ_fold has a cusp region that localizes it to ~16%). But on the operative question — *does the substrate fix the number, or must it be externally set?* — both answer "externally set." τ_fold is the second member of the external-dimensional-import set, with the honest annotation that it is *better-constrained* than M_KK (cusp-localized to a region) but still not *selected* (the cusp location is regulator-dependent and 16% off the used value). That is a sharper, more honest capstone statement than either "tuned number" or "proven selector."

---

## 5. The mechanism-chain (I-1→RPA→Turing→WALL→BCS) forces a *crossing*, not the *value*

Transit's §3 chain is real and PROVEN-unconditional, and I do not contest that the substrate undergoes a first-order transit that crosses a cusp. But examine what the chain *fixes*: I-1 says τ=0 is unstable (flow must increase τ — a *direction*, my R1 §4a); RPA/Turing select a *mode/wavelength*; WALL says *first-order*; BCS *locks the condensate post-transition*. **None of these five conditions contains the number 0.190.** The chain establishes *that* a transit crosses *a* cusp; it does not compute *which* τ the cusp sits at — that is delegated entirely to the cusp location, which §3 just showed is regulator-dependent. The KZ rate-class result (transit §4) is genuinely a PASS, but transit states it honestly: "KZ does not by itself produce 0.190." Correct. The rate-class is range-controlled (a spectral-geometric *window*), which is consistent with a cusp-window selection — and a *window* is precisely a region, not a point. The dynamical content confirms a crossing of a region; the 0.190 within that region remains imported.

---

## 6. Where this leaves me — updated lean (honest)

Transit's R1 was strong and moved me — but **toward** Reading B, not away. The reason: transit's strongest card, when I pulled the actual theorem and verdict files, turns out to be (i) a *non-stationarity* theorem (my claim, co-signed by me), plus (ii) a cusp whose *location* is regulator-dependent (0.221 from scratch, mesh-FAIL) and 16% off the used 0.190 (scheme-dependence, my claim). The threshold-crossing frame is legitimate, but it needs a regulator-INDEPENDENT threshold to pin a parameter-free value, and the substrate's threshold is regulator-CONDITIONAL.

**Updated lean: Reading B at ~0.82** (up slightly from my R1 ~0.80). I credit transit with a genuine ~0.18 on the strongest surviving form of A: it is *possible* that the cusp-CROSSING point (the flank point where the flow goes supersonic, `dS/dτ` maximal-or-thresholded), as opposed to the DOS-PEAK, is the L_max-robust feature and genuinely sits at 0.190 — transit's Gate A1 is the right test and I cannot foreclose it from the existing evidence alone. But the existing evidence points the other way: the only thing shown L_max-robust so far is the *existence* of a cusp (non-stationarity), while the *location* moved (0.221 → frozen-0.190 → mesh-FAIL). My structural prediction (functional-independent, my R1 §4c): Gate A1 will find the cusp *region* robust and the precise crossing-point either regulator-dependent or coincident with 0.221, with 0.190 a flank-choice — a FAIL that confirms B. If A1 returns a regulator-robust crossing at 0.190 ± 0.5% across L_max∈{8,10,12}, I concede the value is substrate-selected and B falls to "constrained-but-imported→selected."

I will NOT concede on the *current* evidence, because the current evidence is: from-scratch cusp = 0.221 (FAIL), uniqueness PASS only at a *pre-frozen* 0.190, alternative mesh = FAIL. That is a regulator-dependent feature with a 16% selector-value gap — which is a scheme-dependent quantity, not a parameter-free selector.

---

## 7. The single crux the R3 verdict must resolve

**Is the cusp-CROSSING location (not the DOS-peak) regulator-INDEPENDENT at τ = 0.190 — i.e., does it survive the change of L_max and mesh — or is only the *existence* of the cusp regulator-robust while its *location* is scheme-dependent (0.221 from scratch, mesh-FAIL, 0.190 frozen on the flank)?**

This is a spectral-functional-invariance question, and it is the hinge transit and I genuinely agree on (transit's decisive-consideration and mine coincide on the gate; we differ on the predicted outcome). The verdict turns on it cleanly:

- **If the crossing-point is regulator-INDEPENDENT at 0.190** (Gate A1 PASS, L_max∈{8,10,12}, ±0.5%): τ_fold is a parameter-free, van-Hove-selected, transit-crossed structural constant — Reading A (threshold-crossing form) wins; the M_KK parallel is downgraded to "better-constrained, value-selected."
- **If only the cusp's EXISTENCE is regulator-robust while its LOCATION is scheme-dependent** (Gate A1 FAIL / only 0.221 stable / 0.190 a frozen flank-point): the cusp constrains τ_fold to a regulator-dependent ~16% region but does not select 0.190 — Reading B stands; τ_fold is the second member (with M_KK) of the external-dimensional-import set, cusp-localized-but-imported.

The proven non-stationarity theorem is common ground (it is *my* claim, co-signed); it does not decide the crux. The crux is decided by the **regulator-invariance of the cusp's location** — and the verdict should commission Gate A1 (L_max∈{8,10,12}, mesh-robustness, crossing-point not peak) as the pre-registered tie-breaker, with the honest prior that the existing 0.221-from-scratch + mesh-FAIL evidence leans Reading B.

---

*End of Round 2 (lizzi-spectral-functional-theorist). No verdict written.*
