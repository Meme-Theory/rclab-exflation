# §5–§6 — The Equation at τ (the Flow) and at Time t

> **Section owner**: Workhorse-Transit-Dynamics (transit-dynamics-theorist).
> **Scope**: the genesis→now trajectory of the one equation, and the τ↔time map.
> **Canonical spine**: `sessions/framework/Atlas/atlas-03-equation-flow.md` (E1–E60); `atlas-04-assumptions.md` (C1, T1–T8, B8–B9).
> **Discipline**: substrate-first (`.claude/rules/phononic-framing.md`). Space does not expand; spectral complexity grows inside each point. Every constant is queried from the knowledge MCP and tagged; non-canonical quantities are marked **PRELIMINARY**. The missing FRW scale factor a(t) is flagged in §6.4.

---

## §5 — THE EQUATION AT τ (THE FLOW)

The single equation of §1 is the Chamseddine–Connes spectral action on the Jensen-deformed internal geometry (E4):

$$
S[D_K,\,f,\,\Lambda] \;=\; \mathrm{Tr}\,f\!\left(\frac{D_K(\tau)^2}{\Lambda^2}\right)
\;=\; 2 f_4 \Lambda^4\, a_0 \;+\; 2 f_2 \Lambda^2\, a_2(\tau) \;+\; f_0\, a_4(\tau) \;+\; \mathcal{O}(\Lambda^{-2}).
\tag{§5.0}
$$

Everything in §5 is a statement about how this one functional behaves as the **single modulus** τ — the Jensen deformation parameter (E1) — runs from genesis (τ = 0) toward the present epoch. There is exactly one dynamical degree of freedom at this level: τ. The flow of the universe IS the flow of τ through the spectrum of $D_K(\tau)$.

### §5.1 The driver: the spectral-action gradient and why there is NO potential well

**The flow functional.** Following the canonical spine (atlas-03), the fabric's internal action is read off the leading Seeley–DeWitt moments:

$$
S_{\mathrm{SA}}(\tau) \;=\; a_0(\tau) \;-\; a_2(\tau) \;+\; a_4(\tau),
\tag{§5.1a}
$$

with the moments interpreted as substrate spectral data, NOT as terms in a Lagrangian on a background:
- $a_0(\tau)$ — Seeley–DeWitt zeroth moment; fabric spectral density (the substrate analog of the "$a_0$" zeroth moment, a *different* spectral moment than gravity — see the exflation/inflation vocabulary table, `phononic-framing.md`: vacuum energy ↔ $a_0$, gravity ↔ $a_2$).
- $a_2(\tau)$ — SDW second moment; second-eigenvalue-sum; sources the Newton coupling (E30, Sakharov induced gravity $G_N^{\mathrm{ind}}$).
- $a_4(\tau)$ — SDW fourth moment; Yang–Mills + Higgs quartic content (E36: $a_2^{\mathrm{bos}}/a_2^{\mathrm{Dirac}} = 61/20$ exact).

**The gradient is the engine.** The driver of the flow is the τ-derivative of the spectral action. The canonical value at the fold (queried; `s83-dynamics-dressing-audit.md`, `session-40-hawking-collab.md`, knowledge MCP equation entries):

$$
\boxed{\;\frac{dS}{d\tau}\bigg|_{\tau_{\mathrm{fold}}} \;=\; +58{,}672.8\;}\qquad
\big(S_{\mathrm{fold}} = 2.5036\times 10^{5}\ \text{at}\ \tau_{\mathrm{fold}} = 0.190\big).
\tag{§5.1b}
$$

Locally near the entry horizon the gradient is even steeper, $dS/d\tau|_{\tau=0.2195} = 68{,}095$ (S71 W2-C, `session-71-sp-synthesis.md`). Both are enormous, positive, and — this is the load-bearing point — **monotone**.

**Substitution chain — sign and direction of the driver** (per `math-scripts.md §"Double-Check Logic Before Compute"`):

```
Claim: "S_SA(τ) has NO stationary point at any τ ≥ 0; the gradient never vanishes."

  Step 1:  E7 (Structural Monotonicity Theorem, atlas-03):
              d⟨λ²⟩/dτ > 0   for the spectrum {λ_k(τ)} of D_K(τ).         [S37; 9,600 checks]
  Step 2:  For any monotone-increasing cutoff f and any Λ, each weighted
              moment a_{2k}(τ) inherits the sign of d⟨λ²⟩/dτ
              (a_{2k} individually monotone, k = 0,1,2,3).                  [E4; S24a, 10^-39 periodic-orbit bound]
  Step 3:  S_f(τ) = Σ_{2k} (moment) ⇒ dS_f/dτ = Σ_{2k} (d/dτ moment),
              every summand > 0.                                            [linearity of d/dτ]
  Step 4:  Σ of strictly-positive terms > 0  ⇒  dS_f/dτ > 0  ∀ τ ≥ 0,
              ∀ monotone f, ∀ Λ, ∀ all 10 sectors.                          [9,600/9,600]
  Step 5:  dS/dτ > 0 everywhere ⇒ no τ* with dS/dτ|_{τ*} = 0.
  Conclusion: S_SA(τ) is strictly increasing; there is NO minimum, NO
              potential well, NO equilibrium τ-stabilization at any τ.       [E7; S1 DISSOLVED, T5 BROKEN]
```

This is the single most important structural fact for the entire §5–§6 flow. **The standard inflationary picture — a field slow-rolling down a potential $V(\phi)$ toward a minimum — does not apply.** There is no $V(\tau)$ with a minimum to roll into. The spectral action is a strictly monotone ramp. Twenty-seven attempted equilibrium closures across S17–S40 all failed; HESS-40 showed all 22 transverse Hessian eigenvalues positive in the full 28-D moduli space (T5 BROKEN); S76 W2-J confirmed a 35-D restoring potential with ridge-confined trajectories and **zero-dimensional constraint surface** in the moduli landscape. The dissolution of "SA stabilizes τ at the fold" (S1 DISSOLVED) is canonical.

**Consequence — this is transit physics, not slow-roll.** Because the driver is a monotone gradient and not a restoring potential, τ does not settle; it **transits**. The dynamics is the dynamics of a system swept through a critical region by an external monotone forcing — the regime in which the adiabatic vacuum breaks down and real excitations are produced (Parker 1968 [01]; Birrell–Davies [02]). The slow-roll parameters $\varepsilon,\eta$ are not the controlling small quantities here; the controlling quantity is the **diabaticity** of the sweep through the fold (§5.2–§5.3). Applying slow-roll formulae ($r = 16\varepsilon$, $n_s = 1 - 6\varepsilon + 2\eta$) outside this regime is exactly the error the vocabulary table forbids ("$r = 16\varepsilon$" → INAPPLICABLE; five independent arguments, VdD–Hawking workshop).

> **Substrate framing (IS not IN).** $S_{\mathrm{SA}}(\tau)$ is not a field energy *in* a spacetime container. It is the fabric's own internal action — the total weighted eigenvalue content of the structure at each point. "The universe evolves" means: the eigenvalue spectrum of $D_K(\tau)$ reorganizes (complexifies) as τ climbs the monotone ramp. Nothing expands; the spectral weight redistributes.

### §5.2 The trajectory: cold-big-bang maximum → supersonic transit → now

The trajectory has three landmarks on the τ-line. None of them is a singularity.

**(i) τ = 0 — the cold big bang (unstable maximum of symmetry).**
At τ = 0 the Jensen metric (E1) is the round, maximally symmetric SU(3) metric: $g_0 = 3\cdot\mathrm{diag}(1,\dots,1)$, scalar curvature $R_K(0) = 2$ (E3). This is the state of **maximal symmetry and minimal spectral complexity** — the "cold big bang vacuum floor" (project memory: τ=0 is an unstable maximum, cascade inevitable). It is genesis not because anything explodes, but because it is the unique unstable extremum from which the monotone gradient drives the system: $dS/d\tau > 0$ pushes τ off zero, and there is no restoring force to bring it back. Symmetry breaks; complexity grows. **There is no t=0 singularity** — τ=0 is a perfectly regular geometric configuration (the round group manifold), and the spectral gap never closes ($\lambda^2 \ge R_K(\tau)/4 \ge 3 > 0$ for all τ, E5, Lichnerowicz; five proofs). The genesis is a *cold, regular, maximally-symmetric starting configuration*, not a hot dense point.

**(ii) τ_fold = 0.190 — the first-order transit through the van Hove fold.**
As τ climbs, the Dirac spectrum reorganizes until it reaches the van Hove fold at $\tau_{\mathrm{fold}} = 0.190$ (queried: CONST-FREEZE-42; R-protected). Here the density of states develops a van Hove singularity ($g(\omega) \sim 1/\sqrt{\omega - \omega_{\min}}$, an $A_2$ catastrophe fold), and the BCS 1D theorem (E13) guarantees that *any* attractive coupling $g>0$ flows to strong coupling — Cooper instability is a **theorem**, with zero critical coupling. The transit is **first-order** (E17, Perturbative Exhaustion; the BCS transition is first-order, the only escape from monotonicity), and it is **supersonic and impulsive**:

$$
\mathrm{Mach} \;=\; \frac{v_{\mathrm{transit}}}{c_{\mathrm{fabric}}} \;=\; 13.75 \quad(\text{canonical; baseline-findings-s66, T1}),
\qquad c_{\mathrm{fabric}} = 209.97\ M_{KK}.
\tag{§5.2a}
$$

> **Conflation guard.** 13.75 is the canonical baseline Mach number (transit speed / sound speed). A *distinct* fold-local acoustic reading $\mathrm{Mach}_{\mathrm{fold}} = 421.3$ appears in `s59_spatial_aniso_log.txt` built from $R_{\mathrm{acoustic}}(\mathrm{fold}) = 442.95\ M_{KK}^2$; it is a different observable (an acoustic-radius ratio, not the canonical velocity Mach). Cite 13.75 as canonical; do NOT average the two.

The impulsiveness is quantified by the **sudden-quench ratio** (T1, PROVEN):

$$
\frac{\delta t_{\mathrm{transit}}}{T_L} \;=\; 1.25\times 10^{-5}
\qquad(\text{dwell time } 38{,}600\times \text{ shorter than BCS formation time}),
\tag{§5.2b}
$$

with transit duration $\delta t_{\mathrm{transit}} = 1.130\times 10^{-3}\ M_{KK}^{-1}$ (queried; `dt_transit`). The system crosses the fold far faster than the condensate can form — the diabatic / sudden limit of the mode equation (§5.3). This is "supersonic transit through the van Hove fold," NOT "slow-roll inflation" (vocabulary table). The genesis-of-structure event is a *sonic boom in the fabric*, not a slow descent.

**(iii) τ_now — the current epoch.**
Post-fold, τ continues up the monotone ramp toward the present-epoch value. The framework does not fix a sharp $\tau_{\mathrm{now}}$ from first principles (this is part of the τ↔t gap, §6.4); the Weinberg-angle match $\sin^2\theta_W = e^{-4\tau}/(1+e^{-4\tau})$ is reproduced at $\tau_0 = 0.2994$ (E26), which is the cleanest present-epoch τ-anchor available, while the cosmological observables (DE, DM, CMB) are read off the **post-transit GGE relic** (§5.3) and the Volovik tracking-vacuum partition (E44–E45). The modulus is effectively **frozen** at late times: the clock constraint (E27) bounds $|\dot\tau| < 2.4\times10^{-6}\,\tau_0/t_H$ (a rolling modulus would violate atomic-clock $\delta\alpha/\alpha$ bounds by $\sim$15,000×), and the frozen-spectrum theorem (B9, C12; PROVEN at $10^{-113}$) makes the substrate spectrum invariant under transit at machine precision. So: rapid impulsive transit through the fold, then a frozen post-transit plateau. The arrow τ: 0 → 0.19 → ~0.3 is the arrow of cosmic time (C1, §6.1).

```
   S_SA(τ)  ▲
            │                                              ·  ·  ·  (frozen plateau, τ_now)
            │                                        · ·
            │                              ┌─ τ_fold = 0.190 ─┐
            │                         · · ·│  VAN HOVE FOLD   │· ·
            │                   · · ·      │  (first-order,   │
            │             · · ·            │   Mach 13.75,    │
            │       · · ·                  │   impulsive)     │
   S(0) ────●· ·                           └──────────────────┘
            │  τ = 0  (cold big bang: unstable max of symmetry, R_K=2, NO singularity)
            └────────────────────────────────────────────────────────────▶  τ
                 dS/dτ = +58,673 > 0 everywhere  —  MONOTONE RAMP, no well
```

### §5.3 GGE-relic formation at the fold: Bogoliubov pair production (the reheating-analog)

This is the transit-dynamics core: what the impulsive supersonic crossing *produces*. The reheating-analog of the framework is the formation of the **Generalized Gibbs Ensemble (GGE) relic** by Bogoliubov pair production at the fold.

**The mode equation and the sudden (diabatic) limit.** Each substrate mode obeys the parametric-oscillator mode equation with a time-dependent frequency set by the Jensen sweep,

$$
u_k'' \;+\; \omega_k^2(\tau(t))\, u_k \;=\; 0,
\qquad \omega_k^2 = E_k^2,\quad
E_k = \sqrt{(\lambda_k^2 - \mu^2)^2 + \Delta_k^2}\,,
\tag{§5.3a}
$$

where $E_k$ is the BdG quasiparticle dispersion on the Dirac spectrum (E12). The in/out vacua are connected by a Bogoliubov transformation with coefficients $(\alpha_k,\beta_k)$, $|\alpha_k|^2 - |\beta_k|^2 = 1$ (unitarity; Bogoliubov–Valatin [20]). The crossing is **diabatic**: $\delta t_{\mathrm{transit}}/T_L = 1.25\times10^{-5} \ll 1$ (§5.2b), so the adiabatic condition $\omega'/\omega^2 \ll 1$ is maximally violated. In the sudden limit the out-state is the in-state expressed in the new basis, and the occupation per mode saturates,

$$
P_{\mathrm{exc}} \;=\; |\beta_k|^2/(1+|\beta_k|^2)\big|_{\mathrm{sudden}} \;\longrightarrow\; 1.000
\qquad(\text{queried } P\_exc\_kz = 1.0;\ \text{T1, S38}),
\tag{§5.3b}
$$

i.e. **every mode is excited** — the condensate is completely destroyed, not perturbatively dressed. The Bogoliubov fraction per mode is $n_{\mathrm{Bog}} = 0.998633$ (`s53_q_theory_gge_output.txt`). This is the cleanest possible diabatic outcome: the sweep is so fast that pair production saturates.

**The relic content.** The total production over the spectrum is the canonical relic (E18; queried):

$$
\boxed{\;N_{\mathrm{pair}} = 59.8 \text{ quasiparticle pairs},\quad
S_{\mathrm{inst}} = 0.0686,\quad
P_{\mathrm{exc}} = 1.000,\quad
E_{\mathrm{exc}}/|E_{\mathrm{cond}}| = 443\;}
\tag{§5.3c}
$$

with $E_{\mathrm{exc}} = 60.6248\ M_{KK}$, $E_{\mathrm{cond}} = -0.136851\ M_{KK}$ (E14, ED-CONV-36). The instanton action $S_{\mathrm{inst}} = 0.0686$ (queried `S_inst`; S37/S38) puts the system in the **dense instanton-gas / liquid regime** ($n\cdot\xi = 1.35$–$4.03$): this is a quantum critical point, not dilute tunneling. The pair wavefunction is 93% B2, 6.3% B1, 0.7% B3 (T4). Caveat per S53 Baptista–Volovik reinterpretation: the 59.8 figure is the BCS-projection count at $N_{\mathrm{pair}}=1$ exact reduction (confirmed $1.2\times10^{-14}$); the correct description is one Fock pair carrying the relic charge $\langle Q\rangle_{\mathrm{GGE}} = N_{\mathrm{pair}} = 59.8$ (S74 Noether chain).

**Kibble–Zurek freeze-out.** The production is also describable in Kibble–Zurek language (Kibble 1980 [05]; Zurek 1985 [06]; del Campo–Zurek [11]; Dziarmaga [24]): the impulse–adiabatic matching at the critical slowing-down of the fold sets the frozen-out defect/excitation density. The KZ excitation probability saturates to $P_{\mathrm{exc}} = 1$ (queried `P_exc_kz`; S38, P=1 exactly) — consistent with the sudden-quench Bogoliubov result, as it must be. The two descriptions (Bogoliubov sudden-quench and Kibble–Zurek impulse-matching) are the same physics read two ways.

**The output state is a GGE, and it does not thermalize during transit.** Post-transit the system is an analytic GGE (E? / T2, PROVEN): $\lambda_k^{\mathrm{GGE}} = -\ln|\psi_{\mathrm{pair}}[k]|^2$, with three distinct Lagrange multipliers reflecting the SU(3) branch structure, and a **product state** ($S_{\mathrm{ent}} = 0$ identically). This is the framework's "reheating": the impulsive transit dumps energy into a non-thermal, integrable relic distribution determined by the **Bogoliubov coefficients**, not by a temperature (Calabrese–Essler [23]; Rigol [13]; Langen [21]). The post-transit observed CMB is the acoustic signature of this GGE relic — "not thermal equilibrium radiation" (vocabulary table). **THE ORDERED VEIL**: the GGE relic is integrable, not chaotic, so it never thermalizes on transit timescales (it eventually relaxes to Gibbs only on cosmological timescales, $t_{\mathrm{therm}}/t_{\mathrm{Hubble}} = 9\times10^{-48}$, T3 — i.e. essentially never on any relevant clock). This is the reheating-analog: parametric amplification of fluctuations through a resonance, producing a non-thermal relic — exactly the structure of preheating (Kofman–Linde–Starobinsky [04]; Amin [17]; Bassett geometric reheating [25]), but driven by an impulsive *fold crossing* rather than an oscillating inflaton.

> **Substrate framing.** The 59.8 pairs are not "particles created in a spacetime that reheated." They are the fiber eigenvalue-spectrum reorganizing at the fold — the excitations ARE the reorganization (vocabulary table). The energy that appears in the GGE comes from the spectral-action gradient $dS/d\tau$ doing work as τ climbs through the fold; this is the substrate's reheating channel.

---

## §6 — THE EQUATION AT TIME t

§5 ran the equation along the internal modulus τ. §6 asks the harder question: what is the map from τ to laboratory cosmic time t, and what does the equation's causal structure look like in t? Here I am scrupulous about the boundary between **derived** and **postulated**, because the central honest gap of the whole document lives in this section (§6.4).

### §6.1 The τ↔t map: what is postulated, what is derived

**Postulated (C1, ASSUMED, S1).** The foundational link is the C1 postulate (atlas-04):

$$
\textbf{C1:}\quad \tau \ \text{parameterizes cosmic time} \quad (\tau\text{-evolution} \;=\; \text{cosmic expansion}).
\tag{§6.1a}
$$

C1 is explicitly **ASSUMED**, not derived. Its registry status reads verbatim: *"Core framework postulate. τ = 0 is the initial state (round SU(3)); increasing τ drives compactification. The mapping from internal modulus to FRW scale factor is not derived from first principles."* So the *ordering* and *orientation* of the time arrow (τ increasing ⇔ t increasing, genesis at τ=0) is postulated, and it is consistent with the monotone gradient of §5.1: because $dS/d\tau > 0$ with no stationary point, τ is a globally monotone function of t, hence invertible, hence a legitimate clock variable. **That τ is a good monotone time coordinate is derived from E7; that it equals cosmic time is postulated (C1).**

**Derived (transit dynamics).** What the transit dynamics *does* supply is the *rate* structure, i.e. $d\tau/dt$ near the fold, through the velocity and dwell-time data:
- transit velocity / sound-speed ratio: Mach $= 13.75$, $c_{\mathrm{fabric}} = 209.97\,M_{KK}$ (§5.2a) — gives $v_{\mathrm{transit}} = \dot\tau\cdot(\text{metric factor})$ in $M_{KK}$ units;
- transit duration $\delta t_{\mathrm{transit}} = 1.130\times10^{-3}\,M_{KK}^{-1}$ (queried `dt_transit`);
- sudden-quench ratio $\delta t_{\mathrm{transit}}/T_L = 1.25\times10^{-5}$ (T1).

From these, the *local* time-reparameterization across the fold is fixed up to the overall $M_{KK}$ scale: the crossing takes $\sim 10^{-3}\,M_{KK}^{-1}$ of substrate time, and the modulus moves through a finite τ-interval (the entry→exit window, §6.2). What is **NOT** derived is the global function $t(\tau)$ over the full history, because that requires a scale factor $a(t)$ (§6.4).

**Precise statement of the map.** Writing it honestly:

$$
t(\tau) \;=\; t_0 \;+\; \int_{\tau_0}^{\tau} \frac{d\tau'}{\dot\tau(\tau')},
\qquad
\dot\tau(\tau) \ \text{known only LOCALLY at the fold (transit data); GLOBALLY UNDETERMINED.}
\tag{§6.1b}
$$

The integrand $1/\dot\tau$ is pinned near $\tau_{\mathrm{fold}}$ by the supersonic-transit kinematics, and the late-time behavior is pinned by the clock constraint ($\dot\tau \to$ frozen, E27), but the intermediate history — and crucially the overall normalization that would convert substrate time $M_{KK}^{-1}$ into seconds and τ-intervals into e-folds — is not closed. This is the vocabulary debt (§6.4).

### §6.2 The six-layer causal structure (S70/S71): TWO sonic horizons + white-hole interior

The temporal/causal architecture of exflation is an **acoustic white hole** with two distinct sonic horizons and a supersonic interior between them. This is the substrate analog of the Schwarzschild white hole, made precise by S70 (PENUMBRA-70), S71 (W2-C, SPECTRUM-71), S73a (BOG-73a), S74 (AUDIT-74), and formalized at S85 (acoustic-white-hole causal-disconnect, PROVEN). The causal structure is **kinematic**: the horizons are painted onto a spectrally rigid background by the modulus velocity exceeding the sound speed — a sonic boom, not an equation-of-state transition (S71 line 69).

**The two horizons (the asymmetric fold).** The crossing has an entry horizon and an exit horizon at *different* τ, controlled by *different* spectral moments:

| | **ENTRY sonic horizon** | **EXIT sonic horizon** |
|:--|:--|:--|
| Location | $\tau \simeq 0.2195$ (S71 W2-C, exact) | $\tau \sim 0.16$ (S70/S73a) |
| Controlled by | $a_2$ — geometric/kinematic (E30 channel) | $a_4$ — matter/BCS condensation (E36 channel) |
| Spectral content | **featureless**: $N_{\mathrm{crossings}}^{\mathrm{phys}} = 0$ (all 85 raw crossings are conjugate-symmetry degeneracies) | **active**: van Hove $dB2/d\tau = 0$ at $\tau=0.19$ ⇒ $N_{\mathrm{crossings}} \neq 0$; BCS gap opens |
| Analog temperature | $T_{\mathrm{entry}} = \kappa_v/2\pi = 72.8\,M_{KK}$ (pure kinematic; $\kappa_v \equiv \lvert dv/d\tau\rvert$ — see κ-definition note) | $T_{\mathrm{compound}} = 7.578\,M_{KK}$ (decoherence-regulated) |
| Gap behavior | B2–B1 gap **OPENS** as τ decreases through entry (opposite of BCS) | BCS gap **opens**; squeeze produced |
| Character | "where the modulus breaks the sound barrier" | "where the BCS gap opens" |

> **κ-definition note (S95 W4 / HAW-V1 disambiguation).** The entry analog temperature $T_{\mathrm{entry}}=72.8\,M_{KK}$ is keyed to the **bare velocity-gradient** surface gravity $\kappa_v \equiv \lvert dv/d\tau\rvert_{\tau=0.2195} = 457.66\,M_{KK}$ (S71-adopted; S73A `kappa_entry = dv_g/d\tau`), NOT the Visser/BLV form $\kappa_{\mathrm{Visser}}=\tfrac12\lvert\partial_n(c^2-v^2)\rvert = c_{\mathrm{BLV}}\lvert dv/dn\rvert$. The two analog-gravity surface-gravity conventions differ by exactly the factor $c_{\mathrm{BLV}}=0.485$ (Sage-exact reduction of $\tfrac12\partial_n(c^2-v^2)$ at $v=c$, S95 W4). **"Entry temperature" in this corpus = $T_{\mathrm{entry}}=72.8$ at the $a_2$-kinematic surface $\tau=0.2195$ under $\kappa_v$**, and is the single canonical value. It is NOT the same observable as the S95 W4-1 quantity $T_a=2.948\,M_{KK}$, which is the Visser $\kappa=\tfrac12\partial_n(c^2-v^2)=18.520\,M_{KK}$ at the **distinct** BLV-scalar discriminant crossing $\tau_0=0.1125$ — a different surface (|Δτ|=0.107) AND a different κ-convention; 2.948 is not a corpus "entry temperature" and does not double-value this label. See `sessions/archive/session-95/session-95-hawking-theorist-synthesis.md` (S-3).

The differential response $|d\ln a_4/d\ln a_2| = 1.43$ at the fold (S71) confirms the asymmetry: the gauge moment $a_4$ responds 1.43× faster than the gravity moment $a_2$ to the Jensen deformation, so the two horizons crossing-points separate. **Entry is an $a_2$ (geometric) event; exit is an $a_4$ (matter) event** — categorically different horizons (S71 line 37; this confirms the S70 Hawking-workshop proposal PC1).

**The white-hole interior.** Between the two horizons ($0.16 \lesssim \tau \lesssim 0.22$) is the **supersonic interior** — the white-hole region, causally disconnected from the exterior by the supersonic flow:

```
   SCHWARZSCHILD WHITE HOLE              SUBSTRATE WHITE HOLE (S71 revised)
   ─────────────────────────            ──────────────────────────────────
   INTERIOR (expanding)         ↔        SUPERSONIC INTERIOR  (0.16 ≲ τ ≲ 0.22)
   EVENT HORIZON (null, r=2M)   ↔        EXIT SONIC HORIZON  (τ ~ 0.16)
   Thermal emission             ↔        Decoherence-regulated squeeze
   S_BH = A/(4G_N)              ↔        S_GGE = 3.54 bits  (the relic, §5.3)
```

Causal flow: **subsonic → supersonic → subsonic** (S71 line 168). Pre-fold and post-fold are causally disconnected — this is the substrate's resolution of the "horizon problem," recast as an acoustic white hole rather than as inflationary stretching (vocabulary table: "horizon problem solved by inflation" → acoustic white hole, pre/post-transit causally disconnected by supersonic flow). The squeeze that becomes the observed scalar amplitude $A_s$ is *produced* in the white-hole interior at the fold and *regulated* at the exit horizon by decoherence (S71 line 129): the white hole produces enormous squeeze ($\sim$7.7× the observed $A_s$), and the exit horizon + decoherence filters it down — "the horizon determines what escapes, not what is produced" (the substrate analog of Hawking-radiation filtering).

**On "six layers" — a precision note for the orchestrator.** There are TWO distinct "six-layer" structures in the corpus, and they must not be conflated:
1. **The S70/S71 causal architecture** (what the spawn brief means by "SIX-LAYER CAUSAL STRUCTURE"): the temporal/causal layering of the transit — (1) subsonic approach, (2) **entry horizon** τ≈0.22 [$a_2$], (3) **supersonic white-hole interior**, (4) **van Hove fold** τ=0.19 [GGE production], (5) **exit horizon** τ~0.16 [$a_4$], (6) subsonic GGE-relic plateau. This is the causal/temporal layering and is the §6.2 deliverable.
2. **The S62/S49 "six-layer censorship"** (COSMIC-CENSORSHIP-49, triple-layered core: energy + friction + no trapped surfaces; S71 line 170 extends it to six: energy, friction, no trapped surfaces, Josephson, fragmentation, one-loop stabilization). This is the set of mechanisms that *protect* the causal structure (no naked breach during transit). It is a SEPARATE registry object.

These are complementary: (1) is the causal architecture; (2) is the censorship that keeps it well-posed. I present (1) as the six-layer causal structure per the brief and cross-reference (2) as its protection. **PRELIMINARY** label: the precise 6-fold enumeration of architecture (1) above is my synthesis of the S70/S71 entry/interior/fold/exit data into six causal strata; the *individual* elements (entry τ=0.2195, exit τ~0.16, interior, fold, the two temperatures) are canonical, but the specific "six-stratum" partition is a presentational organization, not a separately-registered S70 theorem. The orchestrator should treat the entry/exit/interior triple + GGE production as the load-bearing content.

### §6.3 The effacement layer — why the GGE relic does not poison the late-time equation

A transit-dynamics point that matters for running the equation to *now*: the enormous fold-energy and the GGE relic do NOT corrupt the late-time spectral action. The effacement ratio (E34, Wall W10, S42):

$$
\frac{|E_{\mathrm{BCS}}|}{S_{\mathrm{fold}}} \;=\; 3\times 10^{-7}.
\tag{§6.3a}
$$

The BCS condensation energy is $10^{-7}$ of the spectral action, so all BCS/GGE corrections to the late-time equation of state are defeated — this is what lets the late-time $w_0$ be read off the monotone-gradient + Volovik-partition channel (E28, E44–E45) rather than off the relic. The "dark energy / quintessence" of the late universe is the **effacement residual** — 0.03% leakage through the impedance mismatch $\Gamma_{\mathrm{eff}} = 0.99970$ (vocabulary table) — together with the Volovik tracking-vacuum $\rho_{\mathrm{vac}}(t)\sim M_{\mathrm{Pl}}^2 H^2(t)$ that closes the 114-OOM cosmological-constant gap to 0.01 OOM today ($\rho_{\mathrm{vac}}/\rho_{\mathrm{obs}} = 1.032$, E45, DILUTION-CC-66). The relic itself supplies the dark matter channel (E29 CDM-by-construction; E47 Leggett-moment, $\Omega_{\mathrm DM}h^2 = 0.1200$ vs Planck 0.1207). So the equation at time t, late, reads:

$$
S_{\mathrm{SA}}(\tau_{\mathrm{now}}) \;\text{with}\; \tau\ \text{frozen (E27, B9)} \;+\; \rho_{\mathrm{vac}}(H)\ \text{Volovik-tracked (E44)} \;\Rightarrow\; w_0 = -0.918,\ w_a = 0\ \text{(triple-locked, E28)}.
\tag{§6.3b}
$$

### §6.4 THE HONEST GAP: there is no derived FRW scale factor a(t)

**This is the most important caveat in §6, and I state it without softening.** The framework does **not** possess a derived Friedmann–Robertson–Walker scale factor $a(t)$ obeying a Friedmann equation derived from the substrate. This is a logged vocabulary debt, and it must not be papered over.

**What is missing.**
1. C1 explicitly says (atlas-04, verbatim): *"The mapping from internal modulus to FRW scale factor is not derived from first principles."* C2 (K_pivot mapping) is **BROKEN-WITH-LIVE-RESEARCH-PATHWAY**: *"The K_pivot mapping paradox remains the framework's load-bearing gap."* T6 (Friedmann–BCS coupling can dynamically lock τ) is **BROKEN** (FRIED-39: shortfall 133,200×; the 155,984-mode spectral action overwhelms the 8-mode BCS by construction). The S74 transit-einstein workshop (in `researchers/`-adjacent session work) and the S74 W1-E Friedmann result are **structural FAILs**: there is no substrate-derived $H^2 = (8\pi G/3)\rho$ closing the loop back to a metric scale factor.
2. There is no derived function $a(t)$, and consequently no derived $H(t) = \dot a/a$ purely from the spectral action. The Volovik tracking law $\rho_{\mathrm{vac}}(t) = \rho_{\mathrm{vac}}(0)(t_{\mathrm{relax}}/t)^2$ (E44) and the BBN-tracking Friedmann $H^2 = (8\pi G/3)[\rho_{\mathrm{rad}} + \rho_{\mathrm{matter}} + \rho_{\mathrm{vac}}(H)]$ (E46) **assume** a standard FRW $H$ as an external input and feed $\rho_{\mathrm{vac}}$ into it; they do not derive $a(t)$ from $D_K(\tau)$.

**What exists instead (and must be labelled as PROXY, not a(t)).** Two proxy constructions appear in the corpus; both are explicitly *effective* substitutes, NOT derived scale factors:
- **$a_{\mathrm{eff}}(\tau) = (a_2(\tau)/a_2(\tau_{\mathrm{today}}))^{1/2}$** (S73b plan). This is an "effective scale factor" built from the $a_2$ spectral moment as a *spectral-complexity measure*, explicitly not metric expansion. It is a PROXY: it relabels a spectral moment as a scale factor by fiat; it is not a solution of any derived Friedmann equation.
- **$a(\tau)$ from Connes distance** (SCALE-FACTOR-54, FACTOR-54). This gives an $a(\tau)$ with deceleration parameter $q$ transitioning from $-0.97$ (quasi-de Sitter) to $+0.81$ (decelerating), and a conformal time $\eta = \int d\tau/a(\tau)$ (S54 QA–Hawking workshop). This is a *Connes-distance* construction on the spectral triple, **PRELIMINARY** and not promoted; it is a different object from the FRW $a(t)$ and is not derived from a Friedmann equation either.

Neither proxy is a derived FRW scale factor. **I will not invent one, and the document must not present either proxy as if it were $a(t)$.**

**What would be needed to close it.** To genuinely run the equation "at time t" with a derived $a(t)$, the framework would need:
1. A derived map from the spectral action $S_{\mathrm{SA}}(\tau)$ (or its $a_2$ moment, the Einstein–Hilbert channel) to a 4D effective gravitational action whose variation yields a Friedmann equation — i.e. a substrate-derivation of $H^2(\tau) = F[S_{\mathrm{SA}},\,a_2(\tau),\,\rho_{\mathrm{substrate}}]$ rather than an assumed FRW $H$. The pieces exist in isolation (E30 Sakharov induced $G_N$; E36 $a_2$ ratio) but the loop back to $a(t)$ is open.
2. A resolution of the **K_pivot mapping paradox** (C2, the load-bearing gap): the physical e-fold mapping gives $K = 4.3\times10^{-57}\,M_{KK}$ (flat, $n_s=1$), while viable $n_s = 0.965$ needs $K^* = 0.087\,M_{KK}$, and no physical mechanism places K at the intermediate value (E31, EFOLD-MAPPING-52, the decisive gate). Closing $a(t)$ and closing $K_{\mathrm{pivot}}$ are the same gap viewed from two sides: both require converting the internal τ-flow into an external e-fold/scale-factor history.
3. The overall normalization converting substrate time ($M_{KK}^{-1}$) into physical time (seconds), which currently floats with the undetermined $M_{KK}$ (queried $M_{KK} = 7.43\times10^{16}$ GeV, PROVENANCE missing; C6, M_KK undetermined).

Until those three are closed, the equation "at time t" is honestly stated as: *τ is a derived monotone clock (E7); C1 postulates τ = cosmic time; the local transit rate near the fold is fixed by Mach 13.75 and $\delta t_{\mathrm{transit}}$; the global $t(\tau)$ and any FRW $a(t)$ are NOT derived.* The causal structure (§6.2) and the GGE production (§5.3) are real and canonical; the metric clock that would turn them into $a(t)$ is the open frontier.

---

## Consideration (note for the orchestrator)

**How to present "the equation at time t" honestly.** My recommendation is to present §6 as a **two-tier** claim, kept visibly distinct so a reader cannot mistake the second tier for the first:

- **Tier 1 (solid, derived/postulated cleanly):** the equation runs *along τ* (§5), and τ is a legitimate globally-monotone clock because $dS/d\tau > 0$ has no stationary point (E7). The arrow τ: 0 → 0.19 → ~0.3 is cosmic time *by the C1 postulate*, and the causal architecture in that τ-variable — two sonic horizons + white-hole interior + GGE production — is canonical and load-bearing. This is the honest, strong content. **Lead with it.**

- **Tier 2 (open, must be flagged):** the conversion τ → physical time t and the FRW scale factor a(t) are **not derived**. Present this as a *named open frontier*, not a footnote. I would put the a(t) gap in its own boxed subsection (I drafted it as §6.4) with the verbatim C1/C2/T6 registry statuses, so the document's own ledger speaks rather than the narrative.

**The single biggest presentational risk** is that a capstone document titled "The Phonon-Exflation Equation" *invites* the reader to expect a closed $a(t)$ — the very thing the framework does not have. The two proxy constructions ($a_{\mathrm{eff}} = (a_2/a_2^{\mathrm{today}})^{1/2}$ and the Connes-distance $a(\tau)$) are seductive and will be tempting to promote to "the scale factor." **They must be labelled PROXY/PRELIMINARY every time they appear.** If the orchestrator wants a figure of "a vs t," it should be drawn against τ (the derived clock), axis-labelled τ, NOT t, with an explicit caption that t(τ) is undetermined.

**One framing caveat.** The whole point of exflation is that there is *no metric scale factor doing the work* — "space does not expand; spectral complexity grows inside each point" (`phononic-framing.md`). So the missing $a(t)$ is not merely an unfinished calculation; it is partly a *category statement*: the framework deliberately does not have an expanding-container $a(t)$ in the LCDM sense. The honest gap is narrower and sharper than "we haven't derived a(t)" — it is: *we have not yet derived the effective 4D Friedmann map that an external observer who insists on a container-picture would use to translate the internal τ-flow into their $a(t)$.* I recommend the document state the gap in exactly that form, so it reads as a frontier of the substrate→emergent bridge (the E30/E46 channel), not as a hole in LCDM.

**Cross-section dependency.** §5.1's monotonicity result (E7) and §6.4's a(t) gap are the two hinges of the whole genesis→now narrative; whatever §1 (the single equation) and §4 (layers) say must be consistent with: (i) no potential well, ever; (ii) no derived a(t). If another section asserts a minimum of the spectral action or a derived FRW scale factor, it contradicts the canonical registry (S1 DISSOLVED, T5/T6/C2 BROKEN) and should be reconciled against this section.
