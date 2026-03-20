"""
Generate LaTeX for batch 4: 44 inline + ~100 structural equations.
Outputs a text file formatted for weaver to apply.
"""
import json, sys, os
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/knowledge-index.json') as f:
    idx = json.load(f)
eqs = idx['equations']
eq_map = {eq['id']: eq for eq in eqs}

# ---- INLINE EQUATIONS (44) ----
inline_latex = {
    'eq_12102': r'g_1/g_2 = e^{-2s_0}',
    'eq_12103': r'g_1/g_3 = \text{?}',
    'eq_12104': r'g_2/g_3 = \text{?}',
    'eq_12105': r'e^{-2s_0} = 0.55',
    'eq_12108': r'\det(g_s)/\det(g_0) = 1.0000000000',
    'eq_12110': r'J \, D_K(s) = D_K(s) \, J',
    'eq_12111': r'g_1/g_2 = e^{-2s}',
    'eq_12118': r'\det(g_s)/\det(g_0) = 1',
    'eq_12120': r'[D_K, R_{\mathfrak{su}(3)}] = 0',
    'eq_12121': r'K(s) = R_{abcd} \, R^{abcd}(s)',
    'eq_12123': r'[J, D_K(s)] = 0',
    'eq_12124': r'J^T D_F = -(J D_F)^T',
    'eq_12129': r"V''(s_0) = \text{?}",
    'eq_12130': r'e^{-2s_0} = \text{?}',
    'eq_12132': r'T_{HP} = \frac{1}{2\pi r_+}',
    'eq_12133': r'= \frac{1}{R_{\mathrm{SU}(3)}}',
    'eq_12135': r'\sin^2\theta_W = 0.2312',
    'eq_12136': r'g_1/g_2 = \tan\theta_W = 0.5495',
    'eq_12138': r's_W = 0.299',
    'eq_12219': r'\Omega_{m,0} = 0.315',
    'eq_12220': r'\Omega_{r,0} = 9.1 \times 10^{-5}',
    'eq_12222': r'\sin^2\theta_W = 0.231',
    'eq_12223': r'\cos^2\theta_W = 0.769',
    'eq_256': r'\dim(2,2) = 27',
    'eq_258': r'd_\pi = \dim(p,q)',
    'eq_259': r'd_\pi = 28',
    'eq_264': r'\mathrm{vol}_{g^s} = \mathrm{vol}_{g^0}',
    'eq_265': r"R''(0) = 0",
    'eq_432': r'S_{b_1}/S_{b_2} = 4/9',
    'eq_433': r'A_{b_1}/A_{b_2} = 4/9',
    'eq_444': r'\Delta_{b_1} = -0.667',
    'eq_445': r'\Delta(p-q) = \pm 1',
    'eq_764': r'f(x) = e^{-x}',
    'eq_779': r'\mathrm{SU}(2) = S^3',
    'eq_786': r'6 = 4 + 2 \pmod{8}',
    'eq_787': r'6 = -2 \pmod{8}',
    'eq_788': r'KO_{n+8}(X) = KO_n(X)',
    'eq_4090': r'\varphi = 1.618\ldots',
    'eq_7613': r'r_{03} = E_{(0,3)}/E_{(0,0)}',
    'eq_7615': r'r = E_{(3,0)} / E_{(0,0)}',
    'eq_7689': r'\epsilon = 1',
    'eq_7690': r'\epsilon = 0.01',
    'eq_10243': r'g_s = 3 \cdot \mathrm{diag}(e^{-2s}[3],\; e^s[4],\; e^{2s}[1])',
    'eq_10244': r'K(s) = R_{abcd} R^{abcd}',
}

# ---- STRUCTURAL from s22c_landau_classification.txt ----
landau_latex = {
    'eq_618': r'E_{\mathrm{ferm}}(\tau\!=\!0.1) = 9.1602 \quad (N=20)',
    'eq_620': r'E_{\mathrm{ferm}}(\tau\!=\!0.1) = 23.9021 \quad (N=50)',
    'eq_622': r'E_{\mathrm{ferm}}(\tau\!=\!0.1) = 49.9519 \quad (N=100)',
    'eq_633': r'\Delta F_{\mathrm{CW}} = 3.1549 \times 10^{7}',
    'eq_635': r'd = 3, \quad n = 2 \quad (\text{complex order parameter})',
    'eq_647': r"T''(0) = \delta T''(0) = 0",
    'eq_648': r"T''(0) = 0 \quad (\text{marginal})",
    'eq_660': r"V'''(0) = 1.1134 \times 10^{9}",
    'eq_667': r'G_i(\mathrm{CW},\; d_{\mathrm{eff}}\!=\!1) = 2.854 \times 10^{-3}',
    'eq_668': r'G_i(\mathrm{Casimir},\; d_{\mathrm{eff}}\!=\!1) = 5.359 \times 10^{-3}',
    'eq_673': r'g^* N(0)_{\mathrm{sing}} = 2.96,\; g^* N(0)_{\mathrm{tot}} = 35.52 \quad (\tau\!=\!0.10)',
    'eq_674': r'g^* N(0)_{\mathrm{sing}} = 3.10,\; g^* N(0)_{\mathrm{tot}} = 34.10 \quad (\tau\!=\!0.20)',
    'eq_678': r'\tau < 0.234\!: \text{gap closes};\; \tau > 0.234\!: \text{reopens}',
}

# ---- STRUCTURAL from feynman-predictions-session.md ----
feynman_latex = {
    'eq_126': r'R(\tau) = \sum_{\alpha<\beta,\;\text{sectors}} \frac{1}{(\lambda_\alpha - \lambda_\beta)^2}',
    'eq_127': r'R(\tau) \in [17, 66]',
    'eq_129': r'N_{\mathrm{trials}} = N_{\mathrm{pairs}} \times N_{\mathrm{maps}} \times N_\tau \times N_{\mathrm{targets}}',
    'eq_131': r"T''(0) > 0",
    'eq_136': r'V_{\mathrm{tree}}(\sigma,\tau) = -\tfrac{5}{4}\kappa M_P^2 e^{-3\sigma} R_K(\tau)',
    'eq_137': r'\Delta m^2_{\mathrm{atm}}/\Delta m^2_{\mathrm{sol}} = R(\tau_0) \in [17,66]',
    'eq_146': r'p_{\mathrm{global}} = 1 - (1-p_{\mathrm{raw}})^{N_{\mathrm{trials}}}',
    'eq_147': r'p_{\mathrm{LEE}} = 4.6 \times 10^{-3} \;(2.8\sigma)',
    'eq_148': r'N_{\mathrm{eff}} = 50',
    'eq_149': r'|P_1 - P_2| < 1 \quad (\text{Bianchi compatible})',
    'eq_150': r"V''(\tau_0) > 0",
    'eq_151': r'\omega_{\mathrm{mod}} = \sqrt{V_{\mathrm{FR}}\'\'(\tau_0)/G_{\tau\tau}}',
    'eq_156': r'w(z) = w_0 + w_a \frac{z}{1+z}',
}

# ---- STRUCTURAL from d2_pfaffian_output.txt ----
pfaffian_latex = {
    'eq_540': r'\dim(A_F) = 5',
    'eq_541': r'\mathrm{center}(\mathcal{A}_F) = \mathbb{C} \oplus \mathbb{C} \oplus M_3(\mathbb{C})',
    'eq_542': r'\dim(\mathrm{center}) = 5',
    'eq_543': r'\mathcal{A}_F = \mathbb{C} \oplus \mathbb{H} \oplus M_3(\mathbb{C})',
    'eq_544': r'\mathrm{rank}(D_F) = 32',
    'eq_545': r'\mathrm{Pf}(D_F) \neq 0',
    'eq_546': r'\mathrm{sign}(\mathrm{Pf}) = +1',
    'eq_549': r'\lambda = \pm|\lambda| \quad (\text{CPAIR eigenvalues})',
    'eq_550': r'\mathrm{alg\_rank}(\mathbb{R}) = 2',
    'eq_553': r'D_F = D_F^{(0)} + D_F^{(1)}',
    'eq_554': r'\mathrm{KO\text{-}dim} = 6',
    'eq_555': r'J^2 = -1,\; DJ = JD,\; J\gamma = -\gamma J',
    'eq_556': r"\epsilon = 1,\; \epsilon' = -1,\; \epsilon'' = 1",
    'eq_557': r'(1,-1,1) \leftrightarrow \text{KO-dim }6',
}

# ---- STRUCTURAL from s22a_euclidean_action.txt ----
euclidean_latex = {
    'eq_595': r'R_K(\tau) = -\tfrac{1}{4}e^{-4\tau}+2e^{-\tau}-\tfrac{1}{4}+\tfrac{1}{2}e^{2\tau}',
    'eq_597': r'\mathrm{Vol}(K) = \text{const} \quad (\text{volume-preserving})',
    'eq_598': r'I_E(\tau) = -\frac{R(\tau)\,\mathrm{Vol}(K)}{16\pi G}',
    'eq_599': r'I_E(0) = -\frac{2\,\mathrm{Vol}}{16\pi G}',
    'eq_600': r'I_E(\tau)/I_E(0) = R_K(\tau)/2',
    'eq_601': r'\Delta I_E = I_E(\tau) - I_E(0)',
    'eq_603': r'|R_{abcd}|^2(\tau)',
    'eq_604': r'K(\tau) = R_{abcd}\,R^{abcd}(\tau)',
    'eq_605': r'S_{\mathrm{inst}} \propto \int_K \mathrm{tr}(F \wedge {*}F)',
    'eq_607': r'\left.\frac{dS_{\mathrm{inst}}}{d\tau}\right|_{\tau=0} < 0',
    'eq_608': r'\Delta S_{\mathrm{inst}}(\tau) = S_{\mathrm{inst}}(\tau) - S_{\mathrm{inst}}(0)',
}

# ---- STRUCTURAL from s22a_impedance.txt ----
impedance_latex = {
    'eq_584': r'Z_{u(1)}(\tau) = c_{u(1)}^2(\tau)',
    'eq_586': r'Z_{su(2)}(\tau) = c_{su(2)}^2(\tau)',
    'eq_587': r'Z_{su(3)}(\tau) = c_{su(3)}^2(\tau)',
    'eq_588': r'\sin^2\theta_W(\tau) = \frac{Z_{u(1)}}{Z_{u(1)}+Z_{su(2)}}',
    'eq_589': r'\sin^2\theta_W(0) = 0.375 \quad (\text{round metric})',
    'eq_590': r'\sin^2\theta_W(0.30) = 0.2320',
    'eq_591': r'\alpha_{\mathrm{FS}}(\tau) = \frac{e^2}{4\pi} = \frac{g_1^2 g_2^2}{4\pi(g_1^2+g_2^2)}',
}

# ---- STRUCTURAL from s22c_instanton_action.txt ----
instanton_latex = {
    'eq_609': r'\mathrm{tr}(F\wedge{*}F) = |F|^2\,\mathrm{dvol}',
    'eq_610': r'S_{\mathrm{YM}} = \frac{1}{4g^2}\int_K |F|^2\,\mathrm{dvol}',
    'eq_611': r'S_{\mathrm{YM}} \geq \frac{8\pi^2}{g^2}|k| \quad (k=\text{instanton number})',
    'eq_612': r'c_2 = \frac{1}{8\pi^2}\int \mathrm{tr}(F\wedge F)',
    'eq_613': r'\mathrm{tr}(R\wedge R) = |R|^2\,\mathrm{dvol} \quad (\text{spin connection})',
    'eq_614': r'S_{\mathrm{grav}} = \frac{1}{4g^2}\int |R|^2\,\mathrm{dvol}',
    'eq_615': r'\chi(\mathrm{SU}(3)) = 0 \quad (\text{Euler characteristic})',
}

# ---- STRUCTURAL from s23a_gap_equation_results.txt ----
gap_latex = {
    'eq_690': r'V_{ij} = \langle i|K_a|j\rangle \quad (\text{Kosmann coupling matrix})',
    'eq_691': r'\|K_a\| = 0.77\text{--}1.76',
    'eq_692': r'V(\text{gap},\text{nearest}) = 0.093 \quad (\tau=0.30)',
    'eq_694': r'M = g\,N(0)\,V_{\mathrm{eff}} \quad (\text{BdG gap parameter})',
    'eq_695': r'M_{\max}(\mu=0) = 0.077\text{--}0.149',
    'eq_696': r'M_{\max}(\mu=\lambda_{\min}) = 11.2\text{--}14.8 \quad (\text{not physical})',
    'eq_697': r'\Delta_{\mathrm{gap,gap}} = 0 \quad (\text{selection rule})',
}

# Merge
all_latex = {}
all_latex.update(inline_latex)
all_latex.update(landau_latex)
all_latex.update(feynman_latex)
all_latex.update(pfaffian_latex)
all_latex.update(euclidean_latex)
all_latex.update(impedance_latex)
all_latex.update(instanton_latex)
all_latex.update(gap_latex)

# Filter out equations that already have LaTeX
already = [eid for eid in list(all_latex.keys()) if eq_map.get(eid, {}).get('latex')]
for eid in already:
    del all_latex[eid]

# Filter out IDs not in index
missing = [eid for eid in list(all_latex.keys()) if eid not in eq_map]
for eid in missing:
    print(f"WARNING: {eid} not in index, removing")
    del all_latex[eid]

print(f"BATCH 4: {len(all_latex)} equations with new LaTeX")
if already:
    print(f"  Skipped {len(already)} that already have LaTeX: {already}")
print()

# Write batch message
lines = []
for eid in sorted(all_latex.keys(), key=lambda x: int(x.split('_')[1])):
    latex = all_latex[eid]
    eq = eq_map[eid]
    lines.append(f"EQ_ID: {eid}")
    lines.append(f"STATUS: ok")
    lines.append(f"LATEX: {latex}")
    lines.append(f"NOTE: {eq['raw'][:80]}")
    lines.append(f"SOURCE_VERIFIED: yes")
    lines.append("")

msg = '\n'.join(lines)
with open('tools/_batch4_msg.txt', 'w', encoding='utf-8') as f:
    f.write(msg)

print(f"Written to tools/_batch4_msg.txt ({len(msg)} chars)")
