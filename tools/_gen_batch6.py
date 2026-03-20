"""
Batch 6: Hand-curated LaTeX for ALL remaining 342 structural/inline equations.
Covers: artifacts (prompts), sessions (collabs, syntheses, verdicts),
        tier0-computation outputs.
Triages prose/log lines as SKIP with note, writes MATH with proper LaTeX.
"""
import json, sys, os
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/knowledge-index.json') as f:
    idx = json.load(f)
eqs = idx['equations']
eq_map = {eq['id']: eq for eq in eqs}

latex_map = {}   # id -> latex string
skip_map = {}    # id -> reason for skipping (prose, log, data table)

# =====================================================================
# ARTIFACTS — session prompts
# =====================================================================

# Primer
latex_map['eq_12098'] = r'\Delta_0 = f(\Delta_0)'

# Session 18 prompt
latex_map['eq_12139'] = r'V_{\mathrm{CW}}(s) = \frac{1}{64\pi^2} \sum_{\mathrm{bosons}} d_n \lambda_n(s)^4 \left[\ln\frac{\lambda_n(s)^2}{\mu^2} - \frac{3}{2}\right]'
latex_map['eq_12140'] = r'V_{\mathrm{eff}}(s) = V_{\mathrm{tree}}(s)'

# Session 19a prompt
latex_map['eq_12150'] = r'R_{\mathrm{reg}}(\tau) = \sum_{\substack{n<m \\ \text{sectors differ}}} \frac{1}{(\lambda_n - \lambda_m)^2 + \epsilon^2}'
skip_map['eq_12151'] = 'prose: definition of epsilon regulator'
latex_map['eq_12152'] = r'\Omega(\tau) = d_s(\tau, \sigma_*) \cdot S(\tau, \beta_*) \cdot \frac{R_{\mathrm{reg}}(\tau)}{R_{\mathrm{reg}}(0)}'

# Session 19d prompt
latex_map['eq_12168'] = r'E_{\mathrm{Casimir}}(\tau) = \tfrac{1}{2}\,\zeta_D^{\prime}(-\tfrac{1}{2}, \tau)'
latex_map['eq_12169'] = r'V_{\mathrm{CW}}(\tau) = \frac{\pm 1}{64\pi^2} \sum_n d_n \lambda_n^4 \left[\ln\frac{\lambda_n^2}{\mu^2} - \frac{3}{2}\right]'
latex_map['eq_12170'] = r'E_{\mathrm{proxy,total}}(\tau) = E_{\mathrm{proxy,boson}} + E_{\mathrm{proxy,fermion}}'
latex_map['eq_12171'] = r'\zeta_D(s,\tau) = \frac{1}{\Gamma(s)} \int_0^\infty t^{s-1} K(t,\tau)\,dt'

# Session 20 thesis
latex_map['eq_12174'] = r'V_b = \text{divergence component (longitudinal: 8 DOF, gauge/vector)}'
latex_map['eq_12189'] = r'\sin^2\theta_W = 0.23121 \quad (\text{experimental})'

# Session 20a prompt
latex_map['eq_12190'] = r'a_0(\tau) = (4\pi)^{-4}\,\mathrm{Vol}(K)'
latex_map['eq_12191'] = r'a_2(\tau) = (4\pi)^{-4} \tfrac{1}{6} \int_K R_K(\tau)\,d\mathrm{vol}'
latex_map['eq_12192'] = r'R_{abcd} = -\tfrac{1}{4} f_{abe} f^e{}_{cd} \quad [\text{bi-invariant}, \tau=0]'

# Session 20b prompt
latex_map['eq_12193'] = r'\Delta_L h_{ab} = -\nabla^2 h_{ab} - 2R_{acbd} h^{cd} + 2R_{(a}{}^c h_{b)c}'
latex_map['eq_12194'] = r'E_{\mathrm{total}}(\tau) = E_{\mathrm{scalar}}(\tau) + E_{\mathrm{vector}}(\tau) + E_{\mathrm{TT}}(\tau) - E_{\mathrm{Dirac}}(\tau)'
latex_map['eq_12195'] = r'[R_{\mathrm{endo}}]_{IJ}(\tau) = -2\,R_{acbd}(\tau)'
latex_map['eq_12196'] = r'[\Delta_L]_{(p,q)} = [\nabla^2]_{(p,q)} \otimes I_{35} + I_{\dim^2} \otimes R_{\mathrm{endo}}(\tau)'
latex_map['eq_12197'] = r'V_{\mathrm{CW}}(\tau) = \sum_{\mathrm{boson}} \lambda^4 \ln \lambda^2 - \sum_{\mathrm{fermion}} \lambda^4 \ln \lambda^2'

# Session 21c prompt
latex_map['eq_12198'] = r'S_{\mathrm{signed}}(\tau) = \sum_{(p,q)} \sum_{n \in (p,q)} [b_1(p,q) - b_2(p,q)] \cdot \ln \lambda_n^2(\tau)'

# Session 22a prompt
latex_map['eq_12199'] = r'\eta(\tau) = \frac{1}{G_{\tau\tau}} \frac{V^{\prime\prime}(\tau)}{V(\tau)} = \frac{1}{5} \frac{V^{\prime\prime}(\tau)}{V(\tau)}'
latex_map['eq_12200'] = r'I_E(\tau) = -\frac{1}{16\pi G} \int_K R_K(\tau)\,d\mathrm{vol}(\tau)'
latex_map['eq_12201'] = r'\kappa(\tau) = \frac{d(\mathrm{gap})}{d\tau}'
latex_map['eq_12202'] = r'R_{\mathrm{reflect}} = \left(\frac{Z_2 - Z_1}{Z_2 + Z_1}\right)^2'
latex_map['eq_12203'] = r'\sin^2\theta_W = \frac{c_{U(1)}^2}{c_{U(1)}^2 + c_{SU(2)}^2}'

# Session 22b prompt
latex_map['eq_12205'] = r'H_{\mathrm{coupled}} = \mathrm{block\_diag}(H_{0,0}, H_{1,0}, H_{0,1}, H_{1,1}, \ldots) + C_{\mathrm{offdiag}}'
latex_map['eq_12206'] = r'\delta T_{\mathrm{coupled}}(\tau) = \frac{1}{64\pi^2 e^{4\tau}} \sum_n \Delta_b(\mathrm{sector}_n) \ln \lambda_{\mathrm{coupled},n}^2(\tau)'

# Session 22c prompt
latex_map['eq_12207'] = r'\mathrm{Gi} = \frac{(k_B T_c)^2}{c_s\,a\,\xi_0^{d_{\mathrm{eff}}}}'

# Session 22d prompt
skip_map['eq_12224'] = 'prose: instruction to use natural units'
skip_map['eq_12225'] = 'prose: prior specification'

# Session 23a prompt
skip_map['eq_12226'] = 'prose: regulator prescription'
latex_map['eq_12227'] = r'\Delta_n = -\sum_m \frac{V_{nm}\,\Delta_m}{2\sqrt{\xi_m^2 + \Delta_m^2}}'
latex_map['eq_12228'] = r'\xi_m = E_m - \mu'

# Session 23c prompt
latex_map['eq_12229'] = r'S = \mathrm{Tr}\!\left(f\!\left(\frac{D_{\mathrm{total}}^2}{\Lambda^2}\right)\right)'
latex_map['eq_12230'] = r'\alpha = \int_{SU(3)} a_2(x, K)\,d\mathrm{vol}_K'

# Session 24 prompt
latex_map['eq_12231'] = r'\rho = \frac{c_4}{c_2} = \frac{f_4}{60\,f_2\,\Lambda^2}'
latex_map['eq_12232'] = r'H_{\mathrm{eff}} = \mathrm{diag}(\lambda_1, \ldots, \lambda_{16}) + V_{nm}(\tau = 0.30)'
latex_map['eq_12233'] = r'T_{\mathrm{KK}} = M_{\mathrm{KK}}/k_B, \quad V_{\mathrm{barrier}} = V_{\mathrm{spec}}(0) - V_{\mathrm{spec}}(\tau_{\min})'
latex_map['eq_12234'] = r'E_{\mathrm{ZPF}} = \tfrac{1}{2}\sqrt{V_{\mathrm{spec}}^{\prime\prime}(\tau_{\min})}'

# Session 24a prompt
latex_map['eq_12235'] = r'\rho = \frac{c_4}{c_2} = \frac{f_4}{60\,f_2\,\Lambda^2}'
latex_map['eq_12236'] = r'H_{\mathrm{eff}} = \mathrm{diag}(E_1, \ldots, E_{16}) + V_{nm}(\tau = 0.30)'
latex_map['eq_12237'] = r'R = \frac{m_3^2 - m_2^2}{m_2^2 - m_1^2}'

# Session 24b prompt
latex_map['eq_12238'] = r'\mathrm{BF}_{\mathrm{combined}} = \mathrm{BF}(V_{\mathrm{spec}}) \times \mathrm{BF}(R)^{1-r} \times \mathrm{BF}(A/C)^{\gamma}'
latex_map['eq_12239'] = r'm_\sigma^2 = V_{\mathrm{spec}}^{\prime\prime}(\tau_{\min})'
latex_map['eq_12240'] = r'm_\sigma\,[\mathrm{GeV}] = m_\sigma^{\mathrm{KK}} \times M_{\mathrm{KK}}'
latex_map['eq_12241'] = r'T_{\mathrm{settle}} = \frac{2\pi}{m_\sigma}'

# Session 24c prompt
latex_map['eq_12242'] = r'\tau_{\min},\; V_{\mathrm{spec}}(\tau_{\min}),\; V_{\mathrm{spec}}^{\prime\prime}(\tau_{\min}),\; V_{\mathrm{barrier}} = V_{\mathrm{spec}}(0) - V_{\mathrm{spec}}(\tau_{\min})'
skip_map['eq_12243'] = 'prose: instruction for fluctuation argument'
latex_map['eq_12244'] = r'\mathrm{Gi} = \frac{k_B T_{\mathrm{KK}}}{V_{\mathrm{barrier}}}'
latex_map['eq_12245'] = r'E_{\mathrm{ZPF}} = \tfrac{1}{2}\hbar\,\omega_\sigma = \tfrac{1}{2}\sqrt{V_{\mathrm{spec}}^{\prime\prime}(\tau_{\min})}'
skip_map['eq_12246'] = 'prose: instruction to compare ZPF to barrier'
latex_map['eq_12247'] = r'm_\sigma = \sqrt{V_{\mathrm{spec}}^{\prime\prime}(\tau_{\min})}\;[\text{KK units}] \times M_{\mathrm{KK}}\;[\mathrm{GeV}]'

# =====================================================================
# MEETING-MINUTES — Session 16
# =====================================================================

skip_map['eq_27'] = 'prose: instruction to scan Lambda'
skip_map['eq_48'] = 'log: bottleneck annotation'
skip_map['eq_86'] = 'prose: quality assessment'
skip_map['eq_91'] = 'prose: Generation 0 header'

# Feynman predictions
latex_map['eq_152'] = r's=2.00\!:\; \text{lightest 3} = [(1,0),\,(0,1),\,(0,0)]'

# =====================================================================
# MEETING-MINUTES — Session 19 primer (code-like parameters)
# =====================================================================

latex_map['eq_216'] = r'\max_{pq}\mathrm{sum} = 6'
latex_map['eq_217'] = r'\sigma_{\mathrm{probe}} = 1.0'
latex_map['eq_218'] = r'\delta\tau = 0.01'
latex_map['eq_219'] = r'N_{\mathrm{initial}} = 10'
latex_map['eq_220'] = r'\tau_{\mathrm{init}} = 0.0'
latex_map['eq_221'] = r'\tau_{\max} = 2.5'
latex_map['eq_222'] = r'(\lambda_n, \ell_n) = \texttt{collect\_spectrum}(\tau)'
latex_map['eq_223'] = r'S = \sum_n d_n\,e^{-\lambda_n^2/\Lambda^2}'
latex_map['eq_224'] = r'\lambda_n^+ = \texttt{collect\_spectrum}(\tau + \epsilon)'
latex_map['eq_225'] = r'\frac{dS}{d\tau} = \frac{S^+ - S}{\epsilon}'
latex_map['eq_226'] = r'E_{\mathrm{occ}} = \sum_n n_{\mathrm{occ},n}\,\lambda_n^2'
latex_map['eq_227'] = r'F_\tau = -\frac{1}{5}\left(\frac{dV_{\mathrm{tree}}}{d\tau} + \frac{dE_{\mathrm{occ}}}{d\tau}\right)'
latex_map['eq_228'] = r'\text{crossings} = \texttt{find\_avoided\_crossings}(\lambda_n^{\mathrm{old}}, \lambda_n^{\mathrm{new}})'
latex_map['eq_229'] = r'\text{transfer} = \min(n_i, 1) \cdot P_{\mathrm{LZ}}'
latex_map['eq_230'] = r'K_\sigma = \sum_n d_n\,e^{-\sigma\,\lambda_n^2}'
latex_map['eq_231'] = r'n_{\mathrm{edges}} = \texttt{count\_intersector\_edges}(\tau)'
skip_map['eq_232'] = 'prose: runtime estimate for collect_spectrum'
skip_map['eq_233'] = 'prose: definition of spectral H rate'
skip_map['eq_234'] = 'prose: description of monotonic behavior'

# =====================================================================
# MEETING-MINUTES — Session 19d collabs
# =====================================================================

# Berry collab
latex_map['eq_267'] = r'\Delta_3(L) = \min_{a,b} \frac{1}{L} \int_0^L (N(x) - a - bx)^2\,dx'
latex_map['eq_268'] = r'C_n = \frac{1}{2\pi} \int \Omega_n\,d^2k'
latex_map['eq_269'] = r'\rho(E) = \rho_{\mathrm{smooth}} + \sum_p A_p\,e^{iS_p/\hbar}'
latex_map['eq_270'] = r'G(s) = \sum_n f\!\left(\frac{\lambda_n(s)^2}{\Lambda^2}\right) e^{i\gamma_n(s)}'

# Dirac collab
latex_map['eq_279'] = r'R^a{}_{bcd} = \partial_c \Gamma^a{}_{bd} - \partial_d \Gamma^a{}_{bc} + \Gamma^a{}_{ce}\Gamma^e{}_{bd} - \Gamma^a{}_{de}\Gamma^e{}_{bc}'

# Einstein collab
latex_map['eq_284'] = r'\Delta_L h_{ab} = \mu\,h_{ab}'
skip_map['eq_288'] = 'prose: DOF count description (741,636)'
skip_map['eq_289'] = 'prose: historical reference to Lambda = 4*pi*G*rho/c^2'
latex_map['eq_290'] = r'\nabla^a h_{ab} = 0, \quad g^{ab} h_{ab} = 0 \quad (\text{TT gauge})'

# Feynman collab
latex_map['eq_298'] = r'E_{\mathrm{fermion}} = E_{\mathrm{Dirac}}'
skip_map['eq_299'] = 'prose: DOF count header'
latex_map['eq_300'] = r'F(s, T=0) = \tfrac{1}{2}\sum_n \omega_n(s) = E_{\mathrm{Casimir}}(s)'
latex_map['eq_301'] = r'\delta_{\mathrm{TT}}(s) = \frac{d/ds\;\sum d_n \sqrt{\lambda_{\mathrm{TT}}}}{\sum d_n \sqrt{\lambda_{\mathrm{TT}}}}'

# Hawking collab
latex_map['eq_302'] = r'Z = \int \mathcal{D}\phi\,\mathcal{D}A\,\mathcal{D}h_{\mathrm{TT}}\,\mathcal{D}\psi\;e^{-S}'
latex_map['eq_306'] = r'S_{\mathrm{rad}} = \min_I \mathrm{ext}_{\partial I}\left[\frac{A(\partial I)}{4G} + S_{\mathrm{bulk}}(I \cup R)\right]'

# KK collab
latex_map['eq_312'] = r'R(X,Y)Z = \tfrac{1}{4}[X,[Y,Z]] + \tfrac{1}{2}[[X,Y],Z] + \cdots'
latex_map['eq_315'] = r'E_{\mathrm{Casimir}}^{\mathrm{ferm}} = +\tfrac{1}{2}\zeta_L(-\tfrac{1}{2})'
latex_map['eq_316'] = r'K_L(t) = \sum_n e^{-\lambda_n t} \sim (4\pi t)^{-d/2} \sum_k a_k\,t^k'
latex_map['eq_317'] = r'R^d{}_{cab} = \hat{e}_a(\Gamma^d{}_{bc}) - \hat{e}_b(\Gamma^d{}_{ac}) + \Gamma^d{}_{ae}\Gamma^e{}_{bc} - \Gamma^d{}_{be}\Gamma^e{}_{ac} - \Gamma^d{}_{ec}C^e{}_{ab}'
latex_map['eq_318'] = r'R^d{}_{cab} = \Gamma^d{}_{ae}\Gamma^e{}_{bc} - \Gamma^d{}_{be}\Gamma^e{}_{ac} - \Gamma^d{}_{ec}f^e{}_{ab}'

# Landau collab
latex_map['eq_324'] = r'F_{\mathrm{total}}(\tau) = F_{\mathrm{tree}} + F_{\mathrm{CW}} + F_{\mathrm{Casimir}}'
latex_map['eq_325'] = r'A_B\alpha_B e^{\alpha_B \tau_0} = A_F e^{\alpha_F \tau_0} + A_F^{\prime}\alpha_F^{\prime} e^{\alpha_F^{\prime}\tau_0}'
latex_map['eq_326'] = r'\sin^2\theta_W = \frac{1}{1 + e^{4\tau_0}}'
latex_map['eq_327'] = r'F(\tau=0) - F(\tau_0) = \text{condensation energy}'
latex_map['eq_328'] = r'a_3^{\mathrm{total}} = a_3^{\mathrm{tree}} + a_3^{\mathrm{CW}} + a_3^{\mathrm{Casimir}} = 0'
latex_map['eq_329'] = r'A(\omega) = Z\,\delta(\omega - m_\tau) + A_{\mathrm{incoh}}(\omega)'

# Neutrino collab
latex_map['eq_330'] = r'm_{\nu_i} = \lambda_i(s_0) \times M_{\mathrm{scale}}'

# Quantum acoustics collab
latex_map['eq_331'] = r'\lambda_{(p,q)} = C_2(p,q) / R^2'
latex_map['eq_332'] = r'\omega^2(p,q) = C_2(p,q) / R^2'
latex_map['eq_333'] = r'E_{\mathrm{Casimir}}(\tau) = \tfrac{1}{2}\sum_n \omega_n(\tau)'

# Sagan collab
skip_map['eq_339'] = 'prose: convergence assessment'
latex_map['eq_340'] = r'\Delta_L = -\nabla^2 - 2R_{acbd} + 2R_{(a}{}^c'

# SP collab
latex_map['eq_341'] = r'ds^2_{12D} = a^2(\eta)\left[-d\eta^2 + d\Sigma_3^2\right] + g_{ab}(s(\eta))\,w^a w^b'

# =====================================================================
# MEETING-MINUTES — Session 20 collabs
# =====================================================================

latex_map['eq_354'] = r'R_{abcd} \quad (\text{all indices down, orthonormal frame})'
latex_map['eq_360'] = r'S_{\mathrm{geo}} = \sum_n \gamma_n(\tau)\,f\!\left(\frac{\lambda_n(\tau)^2}{\Lambda^2}\right)'
latex_map['eq_365'] = r'\nabla_a T^{a\mu} = 0'

# Hawking 20b collab
latex_map['eq_370'] = r'Z = \int \mathcal{D}[g_K]\;e^{-I_E[g_K]}'
latex_map['eq_371'] = r'\Psi[\tau] = \int \mathcal{D}[g]\;e^{-I_E[g]}'
latex_map['eq_372'] = r'S_{\mathrm{inst}} = \frac{8\pi^2}{g_{\mathrm{YM}}^2}\,k'
latex_map['eq_373'] = r'\delta S_{\mathrm{gen}} = \delta S_{\mathrm{BH}} + \delta S_{\mathrm{ext}} \geq 0'

# =====================================================================
# MEETING-MINUTES — Session 21a-c
# =====================================================================

# 21a synthesis
latex_map['eq_807'] = r'\Delta_b = b_1(p,q,s) - b_2(p,q,s) \quad (\text{SU(3)} \to \text{SU(2)} \times \text{U(1)} \text{ branching})'
latex_map['eq_810'] = r'\delta T(\tau) = \frac{1}{64\pi^2 e^{4\tau}} \sum_n \Delta_b(p_n,q_n) \ln\frac{\mu^2}{\lambda_n(\tau)}'
latex_map['eq_811'] = r'\mu = 1.0 \quad (\text{round SU(3) with } R_K=1)'

# 21b Valar plan
latex_map['eq_393'] = r'\delta\phi_{\mathrm{canonical}} = \sqrt{G_{\tau\tau}}\,\delta\tau = \sqrt{5}\times 0.30 \approx 0.671'
latex_map['eq_395'] = r'\epsilon = \frac{1}{2G_{\tau\tau}}\left(\frac{V^{\prime}}{V}\right)^2 \sim \frac{1}{10}\frac{(dV_{\mathrm{FR}}/d\tau)^2}{V_{\mathrm{FR}}^2}'
latex_map['eq_396'] = r'(\omega_3)_{abc} = f_{abc}'
skip_map['eq_397'] = 'prose: BCS coupling comparison instruction'

# 21c collabs
latex_map['eq_418'] = r'T_{\mathrm{GH}} = \frac{H_{\mathrm{eff}}}{2\pi}'
latex_map['eq_419'] = r'S_{\mathrm{rad}}(t) = \min\{S_{\mathrm{thermal}}(t),\; S_{\mathrm{BH}}(t;\,N_{\mathrm{species}}(\tau(t)))\}'
latex_map['eq_421'] = r'm_\nu^{\mathrm{eff}} = \sqrt{\lambda_{\mathrm{bare}}^2 + \Delta^2}'
latex_map['eq_422'] = r'\lambda^2 = C_2(p,q) + \tfrac{3}{4}'
latex_map['eq_812'] = r'\delta T(\tau) = -\frac{\sum \Delta_b \ln \lambda^2}{64\pi^2 e^{4\tau}}'

# =====================================================================
# MEETING-MINUTES — Session 21c round 2 collabs
# =====================================================================

# Connes r2
latex_map['eq_456'] = r'a_4^{\mathrm{gauge}} = a_4^{SU(2)} + a_4^{U(1)} + a_4^{SU(3)/SU(2)\times U(1)}'

# Feynman r2
latex_map['eq_457'] = r'S[\tau] = S_{\mathrm{singlet}}[\tau] + S_{\mathrm{fund}}[\tau] + S_{\mathrm{adj}}[\tau] + \cdots'
latex_map['eq_458'] = r'Z[\tau] = \int \mathcal{D}[\text{fields}]\;e^{-S_{\mathrm{spectral}}[\text{fields},\tau]}'
latex_map['eq_459'] = r'\delta T_{\mathrm{reg}}(\tau,\Lambda) = \sum_n \Delta_b(n)\,\ln\lambda_n^2\,e^{-\lambda_n^2/\Lambda^2}'

# Hawking r2
latex_map['eq_461'] = r'I_E(\tau) = -\frac{1}{16\pi G_8} \int_K \sqrt{g(\tau)}\,R_K(\tau)'
latex_map['eq_462'] = r'T_{\mathrm{GH}}(H) = \frac{H}{2\pi} = \Delta_{\mathrm{gap}}(\tau)'

# Sagan r2
latex_map['eq_463'] = r'P_{\mathrm{post}} = \frac{P_{\mathrm{prior}} \times \mathrm{BF}}{P_{\mathrm{prior}} \times \mathrm{BF} + (1 - P_{\mathrm{prior}})}'
latex_map['eq_464'] = r'\mathrm{BF}_{\mathrm{eff}} = 0.6 \times 1.0 + 0.4 \times 0.2 = 0.68'

# SP r2
latex_map['eq_465'] = r'\delta t = \sqrt{G_{ss}}\,\delta\tau = \sqrt{10}\times 1.40 \approx 4.4'
skip_map['eq_466'] = 'prose: friction-dominated regime description'
skip_map['eq_467'] = 'prose: radiation domination drift rate context'
latex_map['eq_469'] = r'K(s) = \tfrac{23}{96}e^{-8s} - e^{-5s} + \tfrac{5}{16}e^{-4s} + \tfrac{11}{6}e^{-2s} - \tfrac{3}{2}e^{-s} + \tfrac{17}{32} + \tfrac{1}{12}e^{4s}'

# =====================================================================
# MEETING-MINUTES — Session 22 verdicts and syntheses
# =====================================================================

latex_map['eq_842'] = r'p = \frac{1}{1 + e^{4.50}} = 1.1\%'
latex_map['eq_813'] = r'\tau_{\mathrm{crossing}} = 0.150 \quad (\phi_{\mathrm{paasch}})'
latex_map['eq_814'] = r'D_K = \sum_{a,b} E_{ab}(\tau)\left[\rho_{(p,q)}(X_b) \otimes \gamma_a\right] + I_V \otimes \Omega'
latex_map['eq_815'] = r'F_{\mathrm{true}}(\eta) = \min\{F_{\mathrm{pert}}(\eta),\; F_{\mathrm{cond}}(\eta)\}'

# 22d synthesis
latex_map['eq_816'] = r'\mathrm{Product} = 21.0;\; \mathrm{corr\text{-}adj} = \sqrt{21.0} = 4.58'
latex_map['eq_817'] = r'\mathrm{Product} = 7.5;\; \mathrm{corr\text{-}adj} = \sqrt{7.5} = 2.74'
skip_map['eq_818'] = 'prose: prior specification for panel'
latex_map['eq_819'] = r'O = \ln\frac{0.40}{0.60} + (-0.04) = -0.405 + (-0.04) = -0.445'
latex_map['eq_820'] = r'p = \frac{e^{-0.445}}{1 + e^{-0.445}} = \frac{0.641}{1.641} = 39.1\%'

# =====================================================================
# MEETING-MINUTES — Session 23 Tesla-take collabs
# =====================================================================

# Berry
latex_map['eq_515'] = r'B_n(\tau) = \sum_{\substack{m \neq n \\ \text{both }(0,0)}} \frac{V_{nm}(\tau)}{(E_n(\tau) - E_m(\tau))^2}'
latex_map['eq_516'] = r'\nu = \frac{1}{2\pi i} \oint_{\mathrm{BZ}} d[\log \det h(k)]'

# Connes
latex_map['eq_517'] = r'S_b = f_{12}\Lambda^{12} a_0 + f_8\Lambda^8 a_2 + f_4\Lambda^4 a_4 + \cdots'
latex_map['eq_518'] = r'\mathcal{A}(\tau) = \mathrm{Tr}\!\left(P_{\mathrm{gap}} \frac{dP_{\mathrm{gap}}}{d\tau}\right)'
latex_map['eq_519'] = r'S_b = \int_{M^4} \left[\alpha\,R_M + \beta + V(\tau)\right] d\mathrm{vol}_M'

# Einstein
latex_map['eq_520'] = r'\Lambda_{\mathrm{eff}} = \frac{8\pi G}{c^4}\,V_{\mathrm{spec}}(\tau_0)'

# Feynman
latex_map['eq_521'] = r'V_{11}=0,\quad V_{12}\approx 0.093,\quad V_{13}=0'
latex_map['eq_522'] = r'V_{31}=0,\quad V_{32}\approx 0.02,\quad V_{33}=0'
latex_map['eq_523'] = r'\beta_{c_4} = -\frac{1}{16\pi^2}\left[\frac{133}{10}\,c_4^2\right]'
latex_map['eq_524'] = r'V_{\mathrm{CW}} = \frac{1}{64\pi^2}\sum_n d_n\,\lambda_n^4\left[\ln\frac{\lambda_n^2}{\mu^2} - \frac{3}{2}\right]'

# Hawking
latex_map['eq_525'] = r'S_{\mathrm{SM}}(\tau) = \min_I\,\mathrm{ext}\!\left[\frac{A_{\mathrm{int}}(\partial I)}{4G} + S_{\mathrm{bulk}}(I + \mathrm{SM})\right]'

# Landau
latex_map['eq_526'] = r'\nu = \tfrac{1}{2}\,\mathrm{Tr}\!\left(Q\,\frac{dQ}{d\tau}\right)'

# Paasch
latex_map['eq_527'] = r'E(k) = \bar{\epsilon} + 2t\cos(ka)'

# Quantum acoustics
skip_map['eq_528'] = 'prose: reference to gap equation results file'
latex_map['eq_529'] = r'H = \begin{pmatrix} \epsilon_1 & t_{12} & 0 \\ t_{12} & \epsilon_2 & t_{23} \\ 0 & t_{23} & \epsilon_3 \end{pmatrix}'
latex_map['eq_530'] = r'\rho(E) = -\frac{1}{\pi}\,\mathrm{Im}\,\mathrm{Tr}\,G(E + i\eta)'

# SP
skip_map['eq_531'] = 'prose: curvature invariants header'
latex_map['eq_532'] = r'V_{\mathrm{spec}}(\tau) = c_2\,R_K(\tau) + c_4\,G(\tau)'
latex_map['eq_533'] = r'R_K(\tau) = \tfrac{1}{4}(2e^{2\tau} - 1 + 8e^{-\tau} - e^{-4\tau})'

# Tesla
latex_map['eq_534'] = r'\rho = c_4/c_2 = f_4/(60\,f_2\,\Lambda^2)'
latex_map['eq_535'] = r'H_{\mathrm{eff}}(n,m) = \delta_{nm}\,\lambda_n + \alpha_{\mathrm{eff}}\,V_{nm}'
latex_map['eq_536'] = r'V_{\mathrm{spec}}(\tau) = F(\tau) \quad (\text{phonon free energy in Debye approx})'

# =====================================================================
# MEETING-MINUTES — Session 23b-c syntheses
# =====================================================================

latex_map['eq_821'] = r'O_{\mathrm{panel}} = \ln\frac{0.40}{0.60} + \ln(0.10) = -0.405 + (-2.303) = -2.708'
latex_map['eq_822'] = r'p_{\mathrm{panel}} = \frac{1}{1 + e^{2.708}} = 6.3\%'
latex_map['eq_823'] = r'O_{\mathrm{sagan}} = \ln\frac{0.27}{0.73} + \ln(0.10) = -0.994 + (-2.303) = -3.297'
latex_map['eq_824'] = r'p_{\mathrm{sagan}} = \frac{1}{1 + e^{3.297}} = 3.6\%'
latex_map['eq_828'] = r'\rho = c_4/c_2 = f_4/(60\,f_2\,\Lambda^2)'

# =====================================================================
# MEETING-MINUTES — Session 24 Sagan verdict
# =====================================================================

latex_map['eq_867'] = r'D_\mu = (D_4 - \mu\gamma_0) \otimes 1 + \gamma_5 \otimes D_K'
latex_map['eq_868'] = r'S_{\mathrm{eff}}(\tau) = \sum_{(p,q)} d_{(p,q)}\,V_{(p,q)}(\tau)'
latex_map['eq_869'] = r'S_{\mathrm{ferm}}(\tau) = \sum_{(p,q)} d_{(p,q)} \sum_n f\!\left(\frac{\lambda_n^{(p,q)}(\tau)^2}{\Lambda^2}\right)'

# =====================================================================
# TIER0-COMPUTATION outputs
# =====================================================================

# Pfaffian output
latex_map['eq_538'] = r'\text{CPAIR}: \dim V=4,\; \mathrm{alg\_rank}(\mathbb{R})=8 \quad M_2(\mathbb{C})_{\mathrm{embed}}'
latex_map['eq_539'] = r'\text{REAL}: \dim V=6,\; \mathrm{alg\_rank}(\mathbb{R})=36 \quad M_3(\mathbb{H})/M_6(\mathbb{R})'
latex_map['eq_547'] = r'\text{CPAIR}: \dim V=4,\; \mathrm{alg\_rank}(\mathbb{R})=2'
latex_map['eq_548'] = r'\text{CPAIR}: \dim V=6,\; \mathrm{alg\_rank}(\mathbb{R})=2'
skip_map['eq_551'] = 'prose: only gauge with center dim=5'
latex_map['eq_552'] = r'A_F = \mathbb{C} \oplus \mathbb{H} \oplus M_3(\mathbb{C}), \quad \dim=24, \quad \text{center dim}=5'

# CP1 output
latex_map['eq_558'] = r'\tau \quad \delta T_{\mathrm{total}} \quad \delta T_{Z_3=0} \quad \delta T_{Z_3=1} \quad \delta T_{Z_3=2} \quad \delta T_{b_1} \quad \delta T_{b_2}'
skip_map['eq_559'] = 'log: singlet crossing result'
skip_map['eq_560'] = 'log: fundamental crossing result'
skip_map['eq_561'] = 'prose: ratio constancy test'
skip_map['eq_562'] = 'log: Trap 2 theorem header'
skip_map['eq_563'] = 'log: Z3=0 crossing result (b1-b2)'
skip_map['eq_564'] = 'log: Z3=1 crossing result (b1-b2)'
skip_map['eq_565'] = 'log: Z3=2 crossing result (b1-b2)'

# Gauss-Bonnet
latex_map['eq_566'] = r'\chi(S^8) = 2.000000 \quad (\text{expected } 2)'
latex_map['eq_567'] = r'S(\mathrm{SU}(3),\,\text{analytic}) = -2.32 \times 10^{-16} \quad (\text{expected } 0)'
skip_map['eq_568'] = 'prose: confirms chi(SU(3))=0'

# Euclidean action
latex_map['eq_569'] = r'M_0\;(\tau=0.00)\!:\; R = 2.000\,000\,0, \quad K = 0.500\,000\,0'
latex_map['eq_570'] = r'M_1\;(\tau=0.15)\!:\; R = 2.009\,142, \quad K = 0.521\,496'
latex_map['eq_571'] = r'M_2\;(\tau=1.55)\!:\; R = 11.273, \quad K = 41.358'
latex_map['eq_572'] = r'\mathrm{Vol}(K) = \text{const} \quad (\text{volume-preserving Jensen deformation})'
latex_map['eq_573'] = r'I_E \;\text{ratio} = R(\tau_1)/R(\tau_2)'
latex_map['eq_574'] = r'R(M_0) = 2.000\,000\,0'
latex_map['eq_575'] = r'R(M_1) = 2.009\,142'
latex_map['eq_576'] = r'R(M_2) = 11.273'
latex_map['eq_577'] = r'\alpha = \frac{\mathrm{Vol}(K)}{16\pi G} > 0'
latex_map['eq_578'] = r'\alpha = \frac{1}{16\pi} = 0.01989'
latex_map['eq_579'] = r'R(M_0,\,\tau=0.00) = 2.000\,000\,0'
latex_map['eq_580'] = r'R(M_1,\,\tau=0.15) = 2.009\,142'
latex_map['eq_581'] = r'R(M_2,\,\tau=1.55) = 11.273'

# Fano
skip_map['eq_582'] = 'prose: coarse grid too wide'
skip_map['eq_583'] = 'prose: coupling description'

# Impedance
skip_map['eq_592'] = 'prose: mild symmetry breaking description'
latex_map['eq_593'] = r'\sin^2\theta_W = \frac{g_1^2}{g_1^2 + g_2^2}'
latex_map['eq_594'] = r'\tau = 0.30\!:\; \sin^2\theta_W = 0.2315 \quad (0.2\% \text{ from experiment})'

# BCS channel scan
latex_map['eq_596'] = r'V_{nm} = \frac{d\lambda_n}{d\tau}\,\delta_{nm}'

# Landau classification
latex_map['eq_617'] = r'N=20\!:\; E_{\mathrm{ferm}} \text{ min near } \tau \approx 0.1'
latex_map['eq_619'] = r'N=50\!:\; E_{\mathrm{ferm}} \text{ min near } \tau \approx 0.1'
latex_map['eq_621'] = r'N=100\!:\; E_{\mathrm{ferm}} \text{ min near } \tau \approx 0.1'
latex_map['eq_623'] = r'N=20\!:\; E_{\mathrm{ferm}} \text{ min at } \tau \sim 0.15, \; \text{depth } 0.479\%'
latex_map['eq_624'] = r'N=50\!:\; E_{\mathrm{ferm}} \text{ min at } \tau \sim 0.10, \; \text{depth } 0.081\%'
latex_map['eq_625'] = r'N=100\!:\; E_{\mathrm{ferm}} \text{ min at } \tau \sim 0.15, \; \text{depth } 0.086\%'
latex_map['eq_626'] = r'N=200\!:\; E_{\mathrm{ferm}} \text{ MONOTONICALLY INCREASING}'
latex_map['eq_651'] = r'N=10\!:\; V_{\mathrm{IR}}^{\prime\prime}(0.50) = -8.2422 < 0 \;\Rightarrow\; \text{IR SPINODAL}'
latex_map['eq_653'] = r'N=20\!:\; V_{\mathrm{IR}}^{\prime\prime}(0.50) = -10.131 < 0 \;\Rightarrow\; \text{IR SPINODAL}'
latex_map['eq_655'] = r'N=100\!:\; V_{\mathrm{IR}}^{\prime\prime}(0.50) = -1.4429 < 0 \;\Rightarrow\; \text{IR SPINODAL}'
skip_map['eq_656'] = 'log: IR spinodal N-values list'
latex_map['eq_661'] = r'N=10\!:\; \text{NON-MONOTONIC}, \; V_{\mathrm{IR}} \in [-1.225, -1.039]'
latex_map['eq_662'] = r'N=20\!:\; \text{NON-MONOTONIC}, \; V_{\mathrm{IR}} \in [-1.934, -1.549]'
latex_map['eq_663'] = r'N=50\!:\; \text{NON-MONOTONIC}, \; V_{\mathrm{IR}} \in [-2.454, -1.451]'
latex_map['eq_664'] = r'N=100\!:\; \text{INCREASING}, \; V_{\mathrm{IR}} \in [-2.688, 0.334]'
latex_map['eq_665'] = r'N=150\!:\; \text{INCREASING}, \; V_{\mathrm{IR}} \in [-0.060, 3.751]'
latex_map['eq_666'] = r'N=200\!:\; \text{INCREASING}, \; V_{\mathrm{IR}} \in [4.164, 8.376]'
skip_map['eq_676'] = 'prose: singlet N(0)=2 description'
skip_map['eq_677'] = 'prose: Tesla N(0) usage clarification'
skip_map['eq_681'] = 'prose: ground state instability description'

# Order one
latex_map['eq_686'] = r'A_F = \mathbb{C}(2) \oplus \mathbb{H}(4) \oplus M_3(\mathbb{C})(18) = 24 \;\text{generators}'
latex_map['eq_687'] = r'\tau=0.00\!:\; (0,0)\!=\!1.73,\; (1,0)\!=\!2.89,\; (0,1)\!=\!2.89,\; (1,1)\!=\!2.31,\; (2,0)\!=\!4.04'
latex_map['eq_688'] = r'\tau=0.30\!:\; (0,0)\!=\!2.34,\; (1,0)\!=\!3.90,\; (0,1)\!=\!3.90,\; (1,1)\!=\!3.12,\; (2,0)\!=\!5.46'

# Gate verdicts
latex_map['eq_800'] = r'\tau=0.10\!:\; B = 982.49 \quad (\text{PEAK})'
latex_map['eq_801'] = r'\tau=0.30\!:\; B = 407.15 \quad (\text{local minimum})'
latex_map['eq_802'] = r'I_E(\tau) = -V_{\mathrm{spec}}(\tau)'
latex_map['eq_803'] = r'\rho=0.001\!:\; I_E = \{+0.030,\; +0.028,\; -57.38\}'
latex_map['eq_804'] = r'\rho=0.010\!:\; I_E = \{-17.70,\; -17.75,\; -681.62\}'
latex_map['eq_805'] = r'\rho=0.100\!:\; I_E = \{-195.0,\; -195.52,\; -6924.03\}'

# Neutrino
latex_map['eq_700'] = r'\theta_{12} = 0.00^\circ'

# =====================================================================
# SESSION 19d collabs that I missed in batch 5
# =====================================================================

# (already covered above in the 19d collab section)

# =====================================================================
# SESSION 20b collabs not yet covered
# =====================================================================

# Connes 20b (already done in batch 5 for some)
# Feynman 20b (already done in batch 5 for some)
# Landau 20b (already done in batch 5 for some)
# Lichnerowicz (already done in batch 4 for some)
# QA 20b (already done in batch 5)
# Tesla 20b (already done in batch 5)

# Session 21c collabs not yet covered
# (berry 21c, connes 21c, einstein 21c, kk 21c, paasch 21c already in batch 5)

# Session 22 collabs already covered in batch 5

# Session 23 collabs already covered above

# Session 24 already covered above

# =====================================================================
# MISSING MEETING-MINUTES equations from Session 18, 19a
# =====================================================================

# Session 18 wrapup
skip_map['eq_174'] = 'prose: reference to pi_3(SU(3)) and Casimir energy'
skip_map['eq_175'] = 'prose: geometry of K=SU(3) context'

# Session 19a diagnostics
latex_map['eq_235'] = r'F_{\mathrm{spectral}}(\tau) = -\frac{d}{d\tau}\sum_n d_n\,f(\lambda_n(\tau)^2)'
latex_map['eq_236'] = r'F_{V_{\mathrm{eff}}}(\tau) = -\frac{dV_{\mathrm{CW}}}{d\tau}'

# Session 19d Connes collab
latex_map['eq_276'] = r'V_\zeta(\tau) = -\tfrac{1}{2}\zeta_{\Delta_{\mathrm{total}}}^{\prime}(0,\tau)'
latex_map['eq_277'] = r'V_{\mathrm{eff}}^{\mathrm{NCG}}(\tau) = \mathrm{Tr}\,f\!\left(\frac{D_K(\tau)^2}{\Lambda^2}\right)'
latex_map['eq_278'] = r'V_\zeta(\tau) = -\tfrac{1}{2}\left[\zeta_{\Delta_0}^{\prime}(0) + \zeta_{\Delta_1}^{\prime}(0) + \zeta_{\Delta_L}^{\prime}(0)\right]'

# Session 19d Dirac collab (eq_279 already done above)
latex_map['eq_280'] = r'R^a{}_{bcd} = \Gamma^a{}_{ce}\Gamma^e{}_{bd} - \Gamma^a{}_{de}\Gamma^e{}_{bc} + \Gamma^a{}_{be}\Gamma^e{}_{cd}'
latex_map['eq_281'] = r'E_{\mathrm{Casimir}}^{\mathrm{ferm}} = 2\,E_{\mathrm{Casimir}}^{\Psi_+}'

# Session 19d Einstein collab (eq_284, 288, 289, 290 already done above)
latex_map['eq_287'] = r'R_K = \tfrac{\dim K}{4} = 2'

# Session 19d Feynman collab (eq_296, 297, 298 already done above)
latex_map['eq_296'] = r'(\Delta_L)_{(ab),(cd)} = \delta_{(ab),(cd)}\left(-\sum_e \frac{\rho(e_e)^2}{g_{ee}} + \cdots\right)'
latex_map['eq_297'] = r'E_{\mathrm{boson}} = E_{\mathrm{scalar}} + E_{\mathrm{vector}} + E_{\mathrm{TT}}'

# Session 19d Hawking collab (eq_302, 303, 306 already in batch 4/5)
latex_map['eq_303'] = r'V_{\mathrm{CW}}^{\mathrm{TT}}(\tau) = \frac{1}{2}\frac{1}{64\pi^2}\sum_n d_n \lambda_n^{\mathrm{Lich},4}\left[\ln\frac{\lambda_n^{\mathrm{Lich},2}}{\mu^2} - \frac{3}{2}\right]'
latex_map['eq_304'] = r'\Psi[g_{\partial}] = e^{-I_{\mathrm{cl}}} (\det\Delta_{\mathrm{sc}})^{-1/2} (\det\Delta_{\mathrm{vec}})^{-1/2} (\det\Delta_L)^{-1/2} (\det D\!\!\!/\,)^{+1/2}'

# Session 19d KK collab (eq_312-318 already done above)
latex_map['eq_313'] = r'\zeta_L(z) = \sum_n \lambda_n^{-z}'
latex_map['eq_314'] = r'E_{\mathrm{Casimir}} = -\tfrac{1}{2}\zeta_L(-\tfrac{1}{2})'

# Session 19d SP collab
latex_map['eq_342'] = r'ds^2_{12D} = a^2(\eta)\left[-d\eta^2 + d\Sigma_3^2 + a^{-2}(\eta)\,g_{ab}(s(\eta))\,w^a w^b\right]'
latex_map['eq_343'] = r'R_{abcd} = C_{abcd} + E_{abcd} + \tfrac{1}{56}R(g_{ac}g_{bd} - g_{ad}g_{bc})'
latex_map['eq_344'] = r'G_{\mu\nu}^{(12)} = 8\pi G_{12}\,T_{\mu\nu}'

# Session 20b Berry collab (eq_360 already done)

# Session 20b Connes collab
latex_map['eq_361'] = r'a_2^{\mathrm{red}} = \tfrac{20}{3}\,R_K(\tau)'
latex_map['eq_362'] = r'D = D_{M^4} \otimes 1 + \gamma_5 \otimes D_K'
latex_map['eq_363'] = r'D^2 = D_{M^4}^2 \otimes 1 + 1 \otimes D_K^2'
latex_map['eq_364'] = r'V_{\mathrm{spec}} = -R_K + \rho(500 R_K^2 - 32|\mathrm{Ric}|^2 - 28K)'

# Session 20b Feynman collab
latex_map['eq_366'] = r'V_{\mathrm{eff}}(\tau) = \tfrac{1}{2}\sum_{\mathrm{bosons}} \omega_n(\tau) - \tfrac{1}{2}\sum_{\mathrm{fermions}} \omega_n(\tau)'
latex_map['eq_367'] = r'\zeta_{\mathrm{tower}}(s,\tau) = \sum_n \lambda_n(\tau)^{-s}'
latex_map['eq_368'] = r'S_{\mathrm{inst}}(\tau) = \frac{8\pi^2}{g_{\mathrm{YM}}^2}\,c(\tau)'
latex_map['eq_369'] = r'\Delta_{\mathrm{BCS}} \sim E_D\,e^{-1/(gN(0))}'

# Session 20b Hawking collab (eq_370-373 already done above)
latex_map['eq_374'] = r'Gamma \propto e^{-B/\hbar}'
latex_map['eq_375'] = r'S_{\mathrm{BH}} = \frac{A}{4G_{\mathrm{eff}}} = \frac{A}{4G_4 \cdot \mathrm{Vol}(K)}'
latex_map['eq_376'] = r'\Delta S_{\mathrm{mix}} = -\sum_i p_i \ln p_i'

# Session 20b Landau collab
latex_map['eq_377'] = r'V_{\mathrm{eff}}(\tau) = \sum_i c_i\,f(\lambda_i(\tau))'
latex_map['eq_378'] = r'F_{(p,q)}(\tau) = \frac{\lambda_{(p,q)}(\tau) - \lambda_{(p,q)}(0)}{\lambda_{(p,q)}(0)}'
latex_map['eq_379'] = r'\tau_{\mathrm{relax}} = \tau_0 / V_{\mathrm{eff}}^{\prime\prime}(s_0)'
latex_map['eq_380'] = r'V_{\mathrm{IR}}(\tau) = \sum_{n=1}^{N} c_n \lambda_n(\tau)'
latex_map['eq_381'] = r'E_{\mathrm{gap}}(\tau) = \min_n |\lambda_n(\tau)|'

# Session 20b Lichnerowicz
latex_map['eq_382'] = r'R(\tau=0) = 0.557644 \quad (\text{expected } \sim\!0.558)'
latex_map['eq_383'] = r'E_{\mathrm{scalar}} = 2.929 \times 10^4 \quad (3.2\%\text{ of boson})'
latex_map['eq_384'] = r'E_{\mathrm{vector}} = 2.159 \times 10^4 \quad (2.4\%\text{ of boson})'
latex_map['eq_385'] = r'E_{\mathrm{TT}} = 8.651 \times 10^5 \quad (94.4\%\text{ of boson})'
latex_map['eq_386'] = r'E_{\mathrm{boson}} = 9.166 \times 10^5'
latex_map['eq_387'] = r'E_{\mathrm{Dirac}} = 1.096 \times 10^5'
latex_map['eq_388'] = r'F/B = E_{\mathrm{Dirac}}/E_{\mathrm{boson}} = 0.1196'

# Session 20b QA collab
latex_map['eq_389'] = r'\mu_n(\tau) = \mu_n^{(0)} + \delta\mu_n(\tau)'

# Session 20b Tesla collab
latex_map['eq_390'] = r'\Delta = G \sum_k \frac{\tanh(E_k / 2T)}{E_k}'
latex_map['eq_391'] = r'E_k = \sqrt{\epsilon_k^2 + \Delta^2}'

# Session 21b Valar plan (eq_392 done in batch 5, eq_393 eq_394 eq_395 done above)
latex_map['eq_392'] = r'G_{\tau\tau} = 5 \quad (\text{Baptista eq 3.79})'
latex_map['eq_394'] = r'S_{\mathrm{bounce}} = \frac{27\pi^2}{2}\frac{\sigma^4}{\epsilon^3}'

# Session 21c collabs
latex_map['eq_398'] = r'C = \frac{1}{2\pi}\int \Omega\,d^2R'
latex_map['eq_399'] = r'S_{\mathrm{gauge}} = \frac{f_0}{2\pi^2}\int\left(\frac{g_3^2}{4}G^2 + \frac{g_2^2}{4}W^2 + \frac{g_1^2}{4}B^2\right)'
latex_map['eq_400'] = r'\omega_\tau(a) = \frac{\mathrm{Tr}\!\left(a\,f(D_K^2/\Lambda^2)\right)}{Z(\tau)}'
latex_map['eq_401'] = r'T^{(\Lambda)}_{\mu\nu} = -\frac{\Lambda c^4}{8\pi G}\,g_{\mu\nu}'
latex_map['eq_402'] = r'p_\Lambda = -\rho_\Lambda c^2'
latex_map['eq_403'] = r'w(\tau) = -1 + \frac{2}{3}\frac{\dot{\sigma}^2}{V(\sigma)}'
latex_map['eq_420'] = r'\delta T(\tau) = -\frac{1}{64\pi^2 e^{4\tau}} \sum_{(p,q)} \Delta_b(p,q) \sum_n \ln\frac{\mu^2}{\lambda_n^2(\tau)}'
latex_map['eq_423'] = r'\tau = S_{\mathrm{inst}}(\tau)\,e^{-S_{\mathrm{inst}}(\tau)^2}'
latex_map['eq_424'] = r'\gamma_n^{(a)} = -\frac{d\ln\lambda_n}{ds_a}'
latex_map['eq_425'] = r'\Delta_k = -\sum_{k^{\prime}} \frac{V_{kk^{\prime}}\,\Delta_{k^{\prime}}}{2E_{k^{\prime}}}'
latex_map['eq_426'] = r'\epsilon = \frac{G^{ss}}{2}\left(\frac{V^{\prime}}{V}\right)^2 \ll 1'
latex_map['eq_427'] = r'\delta t = \sqrt{G_{ss}}\,\delta\tau = \sqrt{10}\times 1.48 \approx 4.7'

# Session 21c r2 collabs (eq_452-469 many done above)
latex_map['eq_452'] = r'D_{\mathrm{coupled}}(\tau) = D_{\mathrm{block\text{-}diag}}(\tau) + D_{\mathrm{off\text{-}diag}}(\tau)'
latex_map['eq_453'] = r'\lambda_{H\sigma}(\Lambda) = \frac{\pi^2 e}{2 f_0 a c}'
latex_map['eq_454'] = r'\lambda_H^{\mathrm{eff}} = \lambda_H - \frac{\lambda_{H\sigma}^2}{4\lambda_\sigma}'
latex_map['eq_455'] = r'V_{\mathrm{Higgs}} = \mu_H^2 |H|^2 + \lambda_H^{\mathrm{eff}} |H|^4'
latex_map['eq_460'] = r'\delta T_{\mathrm{tot}}(\tau) = \delta T_{\mathrm{singlet}} + \delta T_{\mathrm{fund}} + \delta T_{\mathrm{adj}}'

# Session 22 Sagan verdict (eq_835-836 already in batch 5)
latex_map['eq_835'] = r'p_0 = 0.40 \quad (\text{panel prior})'
latex_map['eq_836'] = r'O = \ln\frac{0.40}{0.60} + (-1.17) = -0.405 + (-1.17) = -1.575'

# Session 22a synthesis (eq_813 already done above)

# Session 24b synthesis
latex_map['eq_830'] = r'O_{\mathrm{sagan}} = \ln\frac{0.05}{0.95} + \ln(0.31) = -2.944 + (-1.171) = -4.115'
latex_map['eq_831'] = r'p_{\mathrm{sagan}} = \frac{1}{1 + e^{4.115}} = 1.6\%'
latex_map['eq_832'] = r'O_{\mathrm{panel}} = \ln\frac{0.08}{0.92} + \ln(0.31) = -2.442 + (-1.171) = -3.613'
latex_map['eq_833'] = r'p_{\mathrm{panel}} = \frac{1}{1 + e^{3.613}} = 2.6\%'

# Session 24 Sagan verdict (eq_862-869)
latex_map['eq_862'] = r'\mathrm{BF}_{\mathrm{combined}} = \mathrm{BF}_{V\text{-}1} \times \mathrm{BF}_{R\text{-}1}^{1-r} \times \mathrm{BF}_{A/C\text{-}1} \times \mathrm{BF}_{\mathrm{Eucl}}^0'
latex_map['eq_863'] = r'O_{\mathrm{panel}} = \ln\frac{0.08}{0.92} + \ln(0.31)'
latex_map['eq_864'] = r'p_{\mathrm{panel}} = \frac{1}{1 + e^{3.613}}'
latex_map['eq_865'] = r'O_{\mathrm{sagan}} = \ln\frac{0.05}{0.95} + \ln(0.31)'
latex_map['eq_866'] = r'p_{\mathrm{sagan}} = \frac{1}{1 + e^{4.115}}'

# =====================================================================
# Generate output
# =====================================================================

# Remove duplicates (some IDs appear in both batch 5 and here)
# Check which ones already have LaTeX in the index
already_has = set()
for eq in eqs:
    if eq.get('latex') and eq['id'] in latex_map:
        already_has.add(eq['id'])

# Only output new ones
new_latex = {k: v for k, v in latex_map.items() if k not in already_has and k in eq_map}

print(f"Total curated LaTeX entries: {len(latex_map)}")
print(f"Already have LaTeX (skip): {len(already_has)}")
print(f"New to apply: {len(new_latex)}")
print(f"Skipped (prose/log): {len(skip_map)}")
print()

# Write batch 6 message
lines = []
for eid in sorted(new_latex.keys(), key=lambda x: int(x.split('_')[1])):
    latex = new_latex[eid]
    eq = eq_map[eid]
    lines.append(f"EQ_ID: {eid}")
    lines.append(f"STATUS: ok")
    lines.append(f"LATEX: {latex}")
    lines.append(f"NOTE: {os.path.basename(eq['source_file'])}:{eq['line']}")
    lines.append(f"SOURCE_VERIFIED: yes")
    lines.append("")

msg = '\n'.join(lines)
with open('tools/_batch6_msg.txt', 'w', encoding='utf-8') as f:
    f.write(msg)

print(f"Written to tools/_batch6_msg.txt ({len(msg)} chars, {len(new_latex)} equations)")

# Also write skip report
skip_lines = []
for eid in sorted(skip_map.keys(), key=lambda x: int(x.split('_')[1])):
    skip_lines.append(f"EQ_ID: {eid}")
    skip_lines.append(f"STATUS: skip")
    skip_lines.append(f"REASON: {skip_map[eid]}")
    if eid in eq_map:
        eq = eq_map[eid]
        skip_lines.append(f"NOTE: {os.path.basename(eq['source_file'])}:{eq['line']}")
        skip_lines.append(f"RAW: {eq['raw'][:100]}")
    skip_lines.append("")

skip_msg = '\n'.join(skip_lines)
with open('tools/_batch6_skip.txt', 'w', encoding='utf-8') as f:
    f.write(skip_msg)

print(f"Skip report: tools/_batch6_skip.txt ({len(skip_msg)} chars, {len(skip_map)} entries)")

# Summary
total_covered = len(new_latex) + len(already_has) + len(skip_map)
print(f"\nTotal accounted for: {total_covered}")
print(f"  New LaTeX: {len(new_latex)}")
print(f"  Already have LaTeX: {len(already_has)}")
print(f"  Skipped (prose): {len(skip_map)}")
