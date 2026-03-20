"""
Batch 3: Apply physicist-generated LaTeX to remaining physics equations.
Covers: Session 23 Sagan verdict, Session 22 Sagan verdict, Session 20 thesis,
        Session 19 primer, Session 21c Feynman collab, Session 18 wrapup,
        Session 19a/19b prompts.

Directly modifies knowledge-index.json (no weaver needed).
"""

import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH = ROOT / "tools" / "knowledge-index.json"

with open(INDEX_PATH, encoding="utf-8") as f:
    idx = json.load(f)
eqs = idx["equations"]
eq_by_id = {eq["id"]: eq for eq in eqs}

# Batch 3 LaTeX assignments: {eq_id: latex_string}
BATCH3 = {
    # === Session 23 Sagan Verdict (Bayesian posteriors) ===
    "eq_845": r"O_{\mathrm{panel}} = \ln\frac{0.40}{0.60} + \ln(0.10)",
    "eq_846": r"p_{\mathrm{panel}} = \frac{1}{1 + e^{2.708}}",
    "eq_847": r"O_{\mathrm{sagan}} = \ln\frac{0.27}{0.73} + \ln(0.10)",
    "eq_848": r"p_{\mathrm{sagan}} = \frac{1}{1 + e^{3.297}}",
    "eq_849": r"\mathrm{BF}_{K\text{-}1e} = 0.10",
    "eq_850": r"O = \ln\frac{0.08}{0.92} + \ln(75) = -2.442 + 4.317 = +1.875",
    "eq_851": r"p = \frac{1}{1 + e^{-1.875}} = 86.7\%",
    "eq_852": r"O = \ln\frac{0.08}{0.92} + \ln(40) = -2.442 + 3.689 = +1.247",
    "eq_853": r"p = \frac{1}{1 + e^{-1.247}} = 77.7\%",
    "eq_854": r"O = \ln\frac{0.05}{0.95} + \ln(40) = -2.944 + 3.689 = +0.745",
    "eq_855": r"p = \frac{1}{1 + e^{-0.745}} = 67.8\%",
    "eq_856": r"O = \ln\frac{0.08}{0.92} + \ln(10) = -2.442 + 2.303 = -0.139",
    "eq_857": r"p = \frac{1}{1 + e^{0.139}} = 46.5\%",
    "eq_858": r"O = \ln\frac{0.05}{0.95} + \ln(10) = -2.944 + 2.303 = -0.641",
    "eq_859": r"p = \frac{1}{1 + e^{0.641}} = 34.5\%",
    "eq_860": r"E[p]_{\mathrm{sagan}} = 0.75 \times 4\% + 0.13 \times 35\% + 0.08 \times 12\% + 0.04 \times 45\% = 10.3\%",
    "eq_861": r"E[p]_{\mathrm{panel}} = 0.75 \times 6\% + 0.13 \times 45\% + 0.08 \times 17\% + 0.04 \times 55\% = 13.9\%",

    # === Session 22 Sagan Verdict ===
    "eq_834": r"p_{\mathrm{final}} = \sigma\!\left(\ln\frac{p_0}{1-p_0} + \sum_i \ln \mathrm{BF}_i\right)",
    "eq_837": r"p = \frac{1}{1 + e^{1.575}} = \frac{1}{1 + 4.83} = 0.172",
    "eq_838": r"O_{\mathrm{sagan}} = \ln\frac{0.27}{0.73} + (-1.17) = -0.994 + (-1.17) = -2.164",
    "eq_839": r"p = \frac{1}{1 + e^{2.164}} = \frac{1}{1 + 8.71} = 0.103",
    "eq_840": r"O = \ln\frac{0.40}{0.60} + \ln(0.10) = -2.708",
    "eq_841": r"p = \frac{1}{1 + e^{2.708}} = 6.3\%",
    "eq_843": r"O = \ln\frac{0.27}{0.73} + \ln(0.10) = -3.297",
    "eq_844": r"p = \frac{1}{1 + e^{3.297}} = 3.6\%",

    # === Session 20 Thesis ===
    "eq_12177": r"(\Delta_L h)_{ab} = -\nabla^2 h_{ab} - 2 R_{acbd} h^{cd} + 2 \mathrm{Ric}_{(a}{}^c h_{b)c}",
    "eq_12178": r"\lambda_1 = e^{2\tau}, \quad \lambda_2 = e^{-2\tau}, \quad \lambda_3 = e^{\tau}",
    "eq_12179": r"\mathrm{Ric}_{ab} = -\frac{1}{2} f_{acd} f_{bcd} g^{cc'} g^{dd'}",
    "eq_12180": r"R = g^{ab} \mathrm{Ric}_{ab}",
    "eq_12181": r"\Delta_L h = -\nabla^2 h - 2 \mathring{R}(h) + 2 \mathrm{Ric} \circ h",
    "eq_12182": r"E_{\mathrm{TT}} = \frac{1}{2} \sum_n \sqrt{\lambda_n^{(\mathrm{TT})}}",
    "eq_12183": r"E_{\mathrm{scalar}} = \frac{1}{2} \sum_n \sqrt{\lambda_n^{(\mathrm{scalar})}}",
    "eq_12184": r"E_{\mathrm{Casimir}} = E_{\mathrm{TT}} + E_{\mathrm{scalar}} + E_{\mathrm{vector}}",
    "eq_12185": r"\frac{F}{B} = \frac{\sum_n d_n^{\mathrm{ferm}}}{\sum_n d_n^{\mathrm{bos}}} = \frac{16}{44} = 0.364",
    "eq_12186": r"\frac{F}{B}\bigg|_{\mathrm{Weyl}} = 0.55 \quad (\text{constant-ratio trap})",
    "eq_12187": r"V_{\mathrm{CW}}(\tau) = \frac{1}{64\pi^2} \sum_n d_n \lambda_n^4(\tau) \left[\ln\frac{\lambda_n^2(\tau)}{\mu^2} - \frac{3}{2}\right]",
    "eq_12188": r"S = \operatorname{Tr}\!\left(f\!\left(\frac{D^2}{\Lambda^2}\right)\right) \sim \sum_k f_k \Lambda^{2k} a_k",

    # === Session 19 Primer (physics equations only, skip code) ===
    "eq_177": r"\mathrm{vol}_{g_K(\tau)} = \mathrm{vol}_{g_K(0)}",
    "eq_178": r"[\mathcal{L}_{e_a}, D_K] = 0 \quad \text{(Killing fields, block-diagonal)}",
    "eq_179": r"m^2(e_a^L) = \frac{3}{2}\left[(e^{\tau} - e^{-2\tau})^2 + (1 - e^{-\tau})^2\right] / 5",
    "eq_180": r"\lambda_{\min} = 0.818 \text{ at sector } (0,0), \; s \approx 0.26",
    "eq_189": r"V_{\mathrm{eff}}(\sigma, \tau) = V(\sigma, \tau) + \frac{3\kappa}{64\pi^2} m^4(\sigma,\tau) \ln\frac{m^2}{\mu^2}",
    "eq_195": r"s_0 = 0.164 \text{ (CW minimum, 80\% converged)}",
    "eq_197": r"\mathrm{vol}_{g_K(\tau)} = \mathrm{vol}_{g_K(0)} \text{ exactly (eq 3.72)}",
    "eq_199": r"N_{\mathrm{irreps}} = 28, \quad N_{\mathrm{eigenvalues}} \approx 1400 \text{ at } p{+}q \leq 6",
    "eq_204": r"m^2(e_a^L) = \frac{3\kappa}{2(15/2)^5 P_M^{-1} V_0}",
    "eq_206": r"M_{(p_1,q_1),(p_2,q_2)}^a = 0 \text{ at } \tau = 0 \text{ (bi-invariant)}",
    "eq_207": r"H_{\mathrm{spectral}}(t) = \frac{d}{dt} \left[\text{edges in } G(t) \text{ above threshold}\right]",
    "eq_208": r"H_{\mathrm{spectral}}(t) = \frac{d}{dt} \sum_{\alpha < \beta,\; \text{sectors differ}} \Theta\!\left(|M_{\alpha\beta}^a(t)| - \epsilon\right)",
    "eq_210": r"D = D_K(\tau) \text{ on } (\mathrm{SU}(3), g_K(\tau))",
    "eq_214": r"d_s(t, \sigma) = d_s(\tau(t), \sigma)",

    # === Session 21c Feynman Collab ===
    "eq_409": r"\delta T(\tau) = T(\tau) - \tau",
    "eq_410": r"T''_{\mathrm{reg}}(0, \Lambda) = \frac{1}{64\pi^2} \sum_n \Delta_b(n) \, [\cdots] \, e^{-\lambda_n^2/\Lambda^2}",
    "eq_411": r"D_{\mathrm{div}} = d - \Delta \cdot L",
    "eq_412": r"\frac{d\alpha}{d\tau} = -3.08 \, \dot{\tau}",
    "eq_413": r"t_{\mathrm{settle}} \approx 232 \text{ Gyr} \gg t_{\mathrm{universe}}",
    "eq_414": r"w = -1 \quad \text{(frozen modulus in all scenarios)}",
    "eq_415": r"\frac{\Delta\alpha}{\alpha} < 10^{-5} \Rightarrow |\tau_{\mathrm{drift}}| < 3 \times 10^{-6}",
    "eq_416": r"V_{FR}''(\tau_0) / G_{\tau\tau} = \omega^2",
    "eq_417": r"t_{\mathrm{settle}} = \frac{1}{\omega} \sim 232 \text{ Gyr}",

    # === Session 18 Wrapup ===
    "eq_161": r"\text{SU}(3) \text{ compact with } H^1 = 0 \Rightarrow \text{gap closure forbidden}",
    "eq_164": r"\text{quantum critical point at } s_c \text{ not yet falsified}",
    "eq_165": r"\tau \text{ controls ratio of scale factors: } \mathfrak{su}(3) = \mathfrak{u}(1) \oplus \mathfrak{su}(2) \oplus \mathbb{C}^2",
    "eq_166": r"\frac{dV_{\mathrm{CW}}}{d\tau} < 0 \quad \forall \tau \in [0, 2.5]",
    "eq_167": r"V_{\mathrm{CW}}(\tau) \text{ monotonically decreasing (CLOSED)}",
    "eq_168": r"\frac{F}{B} = 8.4:1 \text{ (constant-ratio trap, Trap 1)}",
    "eq_169": r"a_2(\tau) = \frac{1}{6} R_K(\tau) \, \mathrm{vol}(K)",
    "eq_170": r"a_4(\tau) = \text{Gilkey formula with } R_{abcd}, \mathrm{Ric}_{ab}, R",
    "eq_171": r"V_{\mathrm{eff}} = c_2 \Lambda^2 a_2 + c_4 a_4 + \cdots",
    "eq_172": r"\epsilon = \frac{M_P^2}{2}\!\left(\frac{V'}{V}\right)^{\!2}, \quad \eta = M_P^2 \frac{V''}{V}",
    "eq_173": r"\eta \gg 1 \text{ everywhere } \Rightarrow \text{slow-roll impossible (CLOSED)}",

    # === Session 19a Prompt ===
    "eq_12141": r"P_{\mathrm{Brody}}(s, q) = (q+1)\, b \, s^q \, e^{-b \, s^{q+1}}",
    "eq_12142": r"b = \left[\Gamma\!\left(\frac{q+2}{q+1}\right)\right]^{q+1}",
    "eq_12143": r"\Sigma^2(L, \tau) = \langle (n(L) - \langle n(L) \rangle)^2 \rangle",
    "eq_12144": r"\Sigma^2 / \langle n \rangle \to 1 \text{ (Poisson)}, \quad \to 0 \text{ (rigid)}",
    "eq_12145": r"\chi_2(L) = -\frac{d^2}{d\theta^2} \ln\langle e^{i\theta n(L)} \rangle \bigg|_{\theta=0}",
    "eq_12146": r"\omega_n = |\lambda_n|",
    "eq_12147": r"P(s) = \frac{\pi s}{2} e^{-\pi s^2/4} \quad \text{(Wigner surmise, GOE)}",
    "eq_12148": r"P(s) = e^{-s} \quad \text{(Poisson)}",
    "eq_12149": r"s = \frac{\Delta\lambda}{\langle\Delta\lambda\rangle}",

    # === Session 19b Prompt ===
    "eq_12159": r"\epsilon = \frac{\alpha^2}{10}, \quad \eta = \frac{\alpha^2}{5} \quad (M_P = 1)",
    "eq_12160": r"V_{\mathrm{tree}}(\sigma, \tau) = -\frac{5}{4}\kappa M_P^2 e^{-3\sigma} R_K(\tau)",
    "eq_12161": r"y = [\sigma, \dot{\sigma}, \tau, \dot{\tau}]",
    "eq_12162": r"\ddot{\sigma} + 3H\dot{\sigma} = -\frac{\partial V}{\partial \sigma}",
    "eq_12163": r"\ddot{\tau} + 3H\dot{\tau} = -\frac{1}{5}\frac{\partial V}{\partial \tau}",
    "eq_12164": r"H^2 = \frac{1}{3M_P^2}\!\left(\frac{1}{2}\dot{\sigma}^2 + \frac{5}{2}\dot{\tau}^2 + V\right)",
    "eq_12165": r"N_e = \int_{t_i}^{t_f} H \, dt",
    "eq_12166": r"w(\tau) = \frac{\frac{5}{2}\dot{\tau}^2 - V_{\mathrm{eff}}}{\frac{5}{2}\dot{\tau}^2 + V_{\mathrm{eff}}}",
    "eq_12167": r"a(t) \propto e^{\int H \, dt}",
}

# Apply batch
applied = 0
updated = 0
not_found = 0
for eq_id, latex in BATCH3.items():
    if eq_id in eq_by_id:
        eq = eq_by_id[eq_id]
        if eq.get("latex"):
            updated += 1
        else:
            applied += 1
        eq["latex"] = latex
    else:
        not_found += 1
        print(f"  WARNING: {eq_id} not found")

print(f"Batch 3: {applied} new, {updated} updated, {not_found} not found")
print(f"Total batch size: {len(BATCH3)}")

# Write
latex_count = sum(1 for eq in eqs if eq.get("latex"))
print(f"Total equations with LaTeX: {latex_count}")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    json.dump(idx, f, indent=2, ensure_ascii=False)
print("Written.")
