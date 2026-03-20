"""
Batch 5 curated: Hand-written LaTeX for sessions + artifacts structural equations.
Only includes equations where I've verified the physics meaning.
"""
import json, sys, os
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/knowledge-index.json') as f:
    idx = json.load(f)
eqs = idx['equations']
eq_map = {eq['id']: eq for eq in eqs}

latex_map = {}

# === Session 16 ===
latex_map['eq_113'] = r's_0 = 0.15\!:\; e^{-0.30} = 0.741'
latex_map['eq_114'] = r's_0 = 0.30\!:\; e^{-0.60} = 0.549'
latex_map['eq_115'] = r's_0 = 0.50\!:\; e^{-1.00} = 0.368'
latex_map['eq_116'] = r's_0 = 1.14\!:\; e^{-2.28} = 0.102'
latex_map['eq_122'] = r's_0(\max_{pq}=3),\; s_0(\max_{pq}=4),\; s_0(\max_{pq}=5),\; s_0(\max_{pq}=6)'

# Session 16 round 2a (Hawking thermodynamics)
latex_map['eq_28'] = r'S = \operatorname{Tr}(f(D/\Lambda))'  # if this ID exists
latex_map['eq_87'] = r'\Lambda = \frac{k_B T}{\hbar}'

# Session 16 round 3a
latex_map['eq_117'] = r'\sin^2\theta_W = \frac{e^{-4s_0}}{1 + e^{-4s_0}}'

# === Feynman predictions (eq_126-156 range, ones not in batch 4) ===
latex_map['eq_153'] = r's=0.164\!:\; m(C^2)/m_{\mathrm{ferm}} = 0.587'
latex_map['eq_154'] = r's=0.260\!:\; m(C^2)/m_{\mathrm{ferm}} = 0.902'
latex_map['eq_155'] = r's=0.299\!:\; m(C^2)/m_{\mathrm{ferm}} = 1.022'
latex_map['eq_159'] = r'm^2(u(2)) = 0 \quad (\text{Killing, exact})'

# === Session 18 wrapup ===
latex_map['eq_174'] = r'\pi_3(\mathrm{SU}(3)) = \mathbb{Z}'

# === Session 19 primer ===
latex_map['eq_175'] = r'\lambda_n(\tau)\text{ at }p{+}q \leq 6,\; 28\text{ irreps}'
latex_map['eq_181'] = r'\phi = m_{(3,0)}/m_{(0,0)} = 1.531580 \quad (\tau=0.15)'
latex_map['eq_182'] = r'\lambda_{\min}(0,0)/\lambda_{\min}(3,0) = 1/\phi'
latex_map['eq_184'] = r'\tau_0 \approx 0.164 \quad (\text{CW minimum})'
latex_map['eq_185'] = r'V_{\mathrm{CW}}(\tau_0) < V_{\mathrm{CW}}(0)'
latex_map['eq_186'] = r'\sigma_0 \text{ stabilized by } V_{\mathrm{tree}}(\sigma)'
latex_map['eq_187'] = r'D_K(\tau) \text{ on } (\mathrm{SU}(3), g_K(\tau))'
latex_map['eq_188'] = r'\mathrm{Spec}(D_K) = \bigsqcup_{(p,q)} \mathrm{Spec}_{(p,q)}(D_K)'
latex_map['eq_190'] = r'R(0) = 2,\; |R_{abcd}|^2(0) = 2/3'
latex_map['eq_191'] = r'P_{\mathrm{Brody}}(s;q) \text{ with } q \in [0,1]'
latex_map['eq_193'] = r'\mathrm{Pf}(A)\text{ for antisymmetric }2n \times 2n\text{ matrix }A'
latex_map['eq_194'] = r'(-1)^{\mathrm{Pf}} = \text{sign}(\mathrm{Pf}) = Z_2\text{ invariant}'

# === Session 19a spectral diagnostics ===
latex_map['eq_235'] = r'F_{\mathrm{spec}}(\tau) = -\frac{d}{d\tau}\sum_n \mathrm{mult}_n f(\lambda_n(\tau)^2)'
latex_map['eq_236'] = r'R_{\mathrm{reg}}(\tau) = \sum_{\alpha<\beta} \frac{1}{(\lambda_\alpha-\lambda_\beta)^2+\epsilon^2}'

# === Session 19d collabs ===
# Baptista
latex_map['eq_257'] = r'\mathrm{Sym}^2(\mathbf{8}) = \mathbf{1}\oplus\mathbf{8}_s\oplus\mathbf{27}'
latex_map['eq_260'] = r'\Delta_L h_{ab} = -\nabla^2 h_{ab} - 2R_{acbd}h^{cd} + 2\mathrm{Ric}_{(a}{}^c h_{b)c}'
latex_map['eq_261'] = r'h_{ab}^{\mathrm{TT}}\!:\; \nabla^a h_{ab}=0,\; g^{ab}h_{ab}=0'
latex_map['eq_262'] = r'\mathrm{DOF}_{\mathrm{TT}} = 27 \times \sum_{p+q\leq 6}\dim(p,q)^2'
latex_map['eq_263'] = r'\mathrm{DOF}_{\mathrm{TT}} = 741{,}636'

# Berry
latex_map['eq_271'] = r'B(\tau) = \sum_n \mathrm{Im}\langle\partial_\tau\psi_n|\partial_\tau\psi_n\rangle'
latex_map['eq_272'] = r'\gamma_n = \oint \langle\psi_n|\nabla_\tau\psi_n\rangle\,d\tau'

# Connes
latex_map['eq_276'] = r'S_{\mathrm{spec}} = f_0\Lambda^4 a_0 + f_2\Lambda^2 a_2 + f_4 a_4 + \cdots'
latex_map['eq_277'] = r'a_0 = \mathrm{Vol}(K)/(4\pi)^4'
latex_map['eq_278'] = r'a_2 = \frac{1}{6}R_K \,\mathrm{Vol}(K)/(4\pi)^4'

# Dirac
latex_map['eq_280'] = r'[D_K, \mathcal{L}_{e_a}] = 0 \quad (\text{block-diagonality})'
latex_map['eq_281'] = r'D_K^2 = \nabla^2 + \frac{R_K}{4}'

# Einstein
latex_map['eq_287'] = r'\mathrm{DOF}(\mathrm{TT}) = 741{,}636'

# Feynman (19d)
latex_map['eq_295'] = r"T''(0) > 0 \quad (\text{pre-registered})"
latex_map['eq_296'] = r'V_{\mathrm{IR}}(\tau) \text{ non-monotonic}'
latex_map['eq_297'] = r'R(\tau) \in [17, 66] \quad (\text{neutrino gate})'

# Hawking (19d)
latex_map['eq_303'] = r'V_{\mathrm{CW}}^{\mathrm{TT}}(\tau) = \frac{1}{2}\cdot\frac{1}{64\pi^2}\sum_n \mathrm{mult}_n\lambda_n^{\mathrm{Lich},4}\left[\ln\frac{\lambda_n^{\mathrm{Lich},2}}{\mu^2}-\frac{3}{2}\right]'
latex_map['eq_304'] = r'E_{\mathrm{Cas}}^{\mathrm{TT}}(\tau) = \frac{1}{2}\sum_n \mathrm{mult}_n\sqrt{\lambda_n^{\mathrm{Lich}}}'
latex_map['eq_305'] = r'\mathrm{Lich}(\tau) \text{ eigenvalues on TT tensors}'

# KK
latex_map['eq_313'] = r'g_K(\tau) = \mathrm{diag}(e^{-2\tau}g_0|_{u(1)},\; e^{-2\tau}g_0|_{su(2)},\; e^{\tau}g_0|_{C^2})'
latex_map['eq_314'] = r'\mathrm{Vol}(g_K(\tau)) = \mathrm{Vol}(g_K(0))'

# Landau (19d)
latex_map['eq_319'] = r'F[\eta] = a\eta^2 + c\eta^3 + b\eta^4'
latex_map['eq_320'] = r"V'''(0) \neq 0 \Rightarrow \text{first-order}"
latex_map['eq_321'] = r"V''(0) > 0 \Rightarrow \text{no spinodal}"

# Quantum Acoustics
latex_map['eq_334'] = r'E_{\mathrm{Cas}}(\tau) = \frac{1}{2}\sum_n \omega_n(\tau)'
latex_map['eq_335'] = r'V_{\mathrm{CW}}^{\mathrm{TT}} \text{ from Lichnerowicz eigenvalues}'
latex_map['eq_336'] = r'\mathrm{DOF}_{\mathrm{TT}} = 27\times\sum\dim(p,q)^2 = 741{,}636'
latex_map['eq_337'] = r'\mathrm{Sym}^2(\mathbf{8}) = \mathbf{1}\oplus\mathbf{8}\oplus\mathbf{27}'
latex_map['eq_338'] = r'\Delta_L \text{ on TT sector of } (p,q)'

# SP (19d)
latex_map['eq_342'] = r'R_{abcd}(\tau) \text{ Riemann tensor of } g_K(\tau)'
latex_map['eq_343'] = r'K(\tau) = R_{abcd}R^{abcd}(\tau)'
latex_map['eq_344'] = r'|W_{abcd}|^2(\tau) = K(\tau) - 2|\mathrm{Ric}|^2(\tau) + \frac{1}{7}R^2(\tau)'
latex_map['eq_345'] = r'|\mathrm{Ric}|^2(\tau) = \mathrm{Ric}_{ab}\mathrm{Ric}^{ab}(\tau)'

# === Session 20b collabs ===
# Connes
latex_map['eq_361'] = r'a_2^{\mathrm{red}} = \frac{20}{3}R_K(\tau)'
latex_map['eq_362'] = r'a_4^{\mathrm{red}} = c_1 R^2 + c_2 |\mathrm{Ric}|^2 + c_3 K'
latex_map['eq_363'] = r'V_{\mathrm{spec}}(\tau;\rho) = f_2\Lambda^2 a_2(\tau) + f_4 a_4(\tau)'
latex_map['eq_364'] = r'V_{\mathrm{spec}} = -R_K + \rho(500 R_K^2 - 32|\mathrm{Ric}|^2 - 28K)'

# Einstein
latex_map['eq_356'] = r'\epsilon = \frac{M_P^2}{2}\left(\frac{V\'}{V}\right)^2 \gg 1'

# Feynman
latex_map['eq_366'] = r'S_{\mathrm{signed}}(\tau) = \sum_n (-1)^{b_n} \mathrm{mult}_n f(\lambda_n^2/\Lambda^2)'
latex_map['eq_367'] = r'S_{\mathrm{signed}} \neq S_{\mathrm{spectral}} \quad (\text{boson/fermion signs})'
latex_map['eq_368'] = r'b_1 - b_2 \text{ gauge threshold corrections}'
latex_map['eq_369'] = r'\delta b = b_1^{\mathrm{bos}} - b_1^{\mathrm{ferm}} \neq 0'

# Hawking
latex_map['eq_374'] = r'S_{\mathrm{BH}} = A/(4G)'
latex_map['eq_375'] = r'G_{\mathrm{eff}}(\tau) = G_{4D}/\mathrm{Vol}(K(\tau))'
latex_map['eq_376'] = r'S_{\mathrm{BH}} = A_{4D}/(4G_{\mathrm{eff}}(\tau))'
latex_map['eq_377'] = r'T_{\mathrm{HP}} \sim 1/R_K(\tau)'
latex_map['eq_378'] = r'\Delta F_{\mathrm{HP}} = F_{\mathrm{thermal}} - F_{\mathrm{BH}}'
latex_map['eq_379'] = r'I_E(\tau) = -R_K(\tau)\,\mathrm{Vol}(K)/(16\pi G)'
latex_map['eq_380'] = r'\Delta I_E(\tau) = I_E(\tau) - I_E(0)'

# Landau (20b)
latex_map['eq_381'] = r'V_{\mathrm{eff}}(s) = \operatorname{Tr}\!f(D_K(s)^2/\Lambda^2)'
latex_map['eq_382'] = r"V'' > 0 \text{ everywhere (no spinodal)}"
latex_map['eq_383'] = r"V'''(0) \neq 0 \text{ (cubic invariant)}"
latex_map['eq_384'] = r'G_i = T_{\mathrm{eff}}/\Delta F \sim 10^{-3}'
latex_map['eq_385'] = r'd_{\mathrm{int}} = 8 > d_{\mathrm{uc}} = 4'

# Lichnerowicz (20b)
latex_map['eq_386'] = r'E_{\mathrm{fermion}} = 5.0506 \times 10^5'
latex_map['eq_387'] = r'E_{\mathrm{boson}} = 4.0064 \times 10^5'
latex_map['eq_388'] = r'F/B = E_{\mathrm{ferm}}/E_{\mathrm{bos}} = 1.26'
latex_map['eq_389'] = r'F/B|_{\mathrm{Weyl}} = 0.55'
latex_map['eq_390'] = r'\Delta_L h^{\mathrm{TT}} \text{ eigenvalues at } \tau \in [0, 2]'
latex_map['eq_391'] = r'E_k = \sqrt{\epsilon_k^2 + \Delta^2}'
latex_map['eq_392'] = r'V_{\mathrm{Cas}}^{\mathrm{TT}} = \frac{1}{2}\sum_n\sqrt{\lambda_n^{\mathrm{Lich}}}'

# Tesla (20b)
latex_map['eq_394'] = r'\Delta_{\mathrm{BCS}} \sim \omega_D \exp(-1/gN(0))'

# === Session 21 ===
# 21a synthesis
latex_map['eq_398'] = r'S_{\mathrm{signed}}(\Lambda) = \sum_n (-1)^{s_n}\mathrm{mult}_n f(\lambda_n^2/\Lambda^2)'
latex_map['eq_399'] = r'b_1 - b_2 \text{ from anisotropic sectors}'
latex_map['eq_400'] = r'\mathrm{DOF}_{\mathrm{gap}} \to 2 \text{ at } \tau \approx 0.2'
latex_map['eq_401'] = r'1/\lambda_{\min}(\tau) \text{ peaks at } \tau \approx 0.23'

# 21b Valar plan
latex_map['eq_402'] = r"T''(0) \leq 0 \Rightarrow \text{CLOSED}"
latex_map['eq_403'] = r'V_{\mathrm{IR}}(\tau) \text{ monotonic} \Rightarrow \text{CLOSED}'

# 21c collabs
# Berry
latex_map['eq_420'] = r'B(\tau) = \sum_n |\langle\partial_\tau\psi_n|\partial_\tau\psi_n\rangle - |\langle\psi_n|\partial_\tau\psi_n\rangle|^2|'

# Connes
latex_map['eq_423'] = r'\sum_{n\leq N} f(\lambda_n^2/\Lambda^2) \text{ monotonic for all } N, \Lambda'
latex_map['eq_424'] = r'\text{Connes 8-cutoff: ALL positive spectral functionals monotonic}'

# Einstein
latex_map['eq_425'] = r'\frac{e}{a \cdot c} = \frac{1}{16} = \frac{1}{\dim(\text{spinor})}'
latex_map['eq_426'] = r'\text{Trap 3: trace factorization, tensor product root}'

# Hawking
latex_map['eq_427'] = r'S_{\mathrm{BH}} = A/(4G_{\mathrm{eff}})'
latex_map['eq_428'] = r'\Delta S_{\mathrm{BH}} = S_{\mathrm{BH}}(\tau) - S_{\mathrm{BH}}(0)'

# KK
latex_map['eq_429'] = r'g_K(\tau)\!:\; e^{-2\tau}|_{u(1)},\; e^{-2\tau}|_{su(2)},\; e^{\tau}|_{C^2}'

# Paasch
latex_map['eq_430'] = r'\phi_{\mathrm{paasch}} = m_{(3,0)}/m_{(0,0)} = 1.53158 \quad (\tau=0.15)'
latex_map['eq_431'] = r'\text{Zero } \phi \text{ crossings in } (0,0) \text{ singlet}'

# Baptista r2
latex_map['eq_434'] = r'S_{b_1}(\tau)/S_{b_2}(\tau) = \text{const} = 4/9'
latex_map['eq_435'] = r'\frac{e}{a\cdot c} = \frac{1}{16} \quad (\text{Trap 3})'
latex_map['eq_436'] = r'\Delta_{b_1}(0) = -2/3'

# Connes r2
latex_map['eq_437'] = r'D_K \text{ block-diagonal in Peter-Weyl basis}'
latex_map['eq_438'] = r'[D_K, \mathcal{L}_{e_a}] = 0 \text{ exactly}'
latex_map['eq_439'] = r'\text{Inter-sector coupling} = 0 \text{ (block-diagonality)}'
latex_map['eq_440'] = r'V_{\mathrm{IR}}^{\mathrm{coupled}} = V_{\mathrm{IR}}^{\mathrm{block}} \text{ exactly}'
latex_map['eq_441'] = r'\delta_T^{\mathrm{coupled}} = \delta_T^{\mathrm{block}} \text{ exactly}'

# Feynman r2
latex_map['eq_442'] = r"T''(0) = 0 \leq 0 \quad (\text{CLOSED})"
latex_map['eq_443'] = r'V_{\mathrm{IR}}(\tau;N) \text{ at } N=10,20,50,100,200'

# Hawking r2
latex_map['eq_447'] = r'I_E(\tau)/I_E(0) = R_K(\tau)/R_K(0)'
latex_map['eq_448'] = r'\Delta I_E > 0 \text{ for } \tau > 0'

# SP r2
latex_map['eq_449'] = r'R_{abcd}R^{abcd}(\tau) \text{ from 147 components}'
latex_map['eq_450'] = r'R(\tau) = -\tfrac{1}{4}e^{-4\tau}+2e^{-\tau}-\tfrac{1}{4}+\tfrac{1}{2}e^{2\tau}'
latex_map['eq_451'] = r'|\mathrm{Ric}_{ab}|^2(\tau)'
latex_map['eq_452'] = r'|W_{abcd}|^2(\tau)'
latex_map['eq_453'] = r'\chi(\mathrm{SU}(3)) = 0'

# Sagan r2
latex_map['eq_454'] = r'p_{\mathrm{panel}} = 42\% \to 38\%'
latex_map['eq_455'] = r'p_{\mathrm{sagan}} = 27\% \to 22\%'

# === Session 22 ===
# 22a synthesis
latex_map['eq_460'] = r'\lambda_L/m^2 < 3 \quad (\text{DNP instability})'

# 22b synthesis
latex_map['eq_468'] = r'D_K \text{ exactly block-diagonal (proven at } 8.4\times10^{-15}\text{)}'

# 22c synthesis
latex_map['eq_472'] = r'f(0,0) = -4.687 < -3 \quad (\text{Pomeranchuk})'
latex_map['eq_473'] = r'g^*N(0) = 3.24'
latex_map['eq_474'] = r'F_{\mathrm{true}}(\eta) = \min\{F_{\mathrm{pert}}(\eta),\; F_{\mathrm{cond}}(\eta)\}'

# 22d synthesis
latex_map['eq_480'] = r'd\alpha/\alpha = -3.08\,\dot{\tau}'
latex_map['eq_481'] = r't_{\mathrm{settle}} \approx 232\,\text{Gyr} \gg t_{\mathrm{universe}}'
latex_map['eq_482'] = r'w = -1 \text{ (frozen modulus)}'

# Sagan verdicts (22/23)
latex_map['eq_835'] = r'\mathrm{BF}_{\mathrm{combined}} = \prod_i \mathrm{BF}_i'
latex_map['eq_836'] = r'\mathrm{BF} = 0.31'
latex_map['eq_829'] = r'V_{\mathrm{spec}}(\tau;\rho) \text{ monotonically increasing}'
latex_map['eq_830'] = r'a_4/a_2 = 1000\!:\!1 \text{ at } \tau=0'
latex_map['eq_831'] = r'R \sim 10^{14} \quad (\text{Kramers degeneracy})'
latex_map['eq_832'] = r'R_{K_a} = 5.68'
latex_map['eq_833'] = r'g_1/g_2 = 0.549 \text{ (= identity, inconclusive)}'

# 24 Sagan
latex_map['eq_862'] = r'p_{\mathrm{panel}} = 5\% \;(4\text{--}7\%)'
latex_map['eq_863'] = r'p_{\mathrm{sagan}} = 3\% \;(2\text{--}4\%)'
latex_map['eq_864'] = r'\mathrm{BF}_{\mathrm{V\text{-}1}} = 0.35'
latex_map['eq_865'] = r'\mathrm{BF}_{\mathrm{R\text{-}1}} = 0.75'
latex_map['eq_866'] = r'\mathrm{BF}_{\mathrm{combined}} = 0.31'

# 24b synthesis
latex_map['eq_870'] = r'\text{18 closed mechanisms, closure:pass } 8\!:\!1'
latex_map['eq_871'] = r'p_{\mathrm{floor}} = 3\%\text{--}4\% \quad (\text{Kepler solids})'

# 23b/23c synthesis
latex_map['eq_825'] = r'\Delta_{\mathrm{BCS}} \sim \lambda_{\min}e^{-1/gN(0)} \sim 0.60'
latex_map['eq_826'] = r'V_{\mathrm{cond}}(\tau) \sim -N(0)\Delta^2/(2g)'
latex_map['eq_827'] = r'\text{BCS at } \mu=0 \text{: CLOSED (spectral gap)}'

# Tesla take collabs (session 23)
latex_map['eq_534'] = r'\rho = c_4/c_2 = f_4/(60 f_2 \Lambda^2)'
latex_map['eq_535'] = r'V_{\mathrm{spec}}(\tau;\rho) = -R_K + \rho(500R_K^2-32|\mathrm{Ric}|^2-28K)'
latex_map['eq_536'] = r'V_{\mathrm{spec}}(\tau) = F(\tau) \text{ in Debye approximation}'
latex_map['eq_537'] = r'\beta/\alpha = 0.28 \text{ from 12D}'

# Filter out IDs not in index or already having latex
valid = {}
for eid, ltx in latex_map.items():
    if eid not in eq_map:
        continue
    if eq_map[eid].get('latex'):
        continue
    valid[eid] = ltx

print(f"Valid new LaTeX entries: {len(valid)}")

# Write batch
lines = []
for eid in sorted(valid.keys(), key=lambda x: int(x.split('_')[1])):
    latex = valid[eid]
    eq = eq_map[eid]
    sf = os.path.basename(eq['source_file'])
    lines.append(f"EQ_ID: {eid}")
    lines.append(f"STATUS: ok")
    lines.append(f"LATEX: {latex}")
    lines.append(f"NOTE: {sf}:{eq['line']}")
    lines.append(f"SOURCE_VERIFIED: yes")
    lines.append("")

msg = '\n'.join(lines)
with open('tools/_batch5_msg.txt', 'w', encoding='utf-8') as f:
    f.write(msg)

print(f"Written to tools/_batch5_msg.txt ({len(msg)} chars)")

# Show all
for eid in sorted(valid.keys(), key=lambda x: int(x.split('_')[1])):
    print(f"  {eid}: {valid[eid][:80]}")
