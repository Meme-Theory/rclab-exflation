"""
ONE-SHOT atomic application of all audit corrections to knowledge-index.json.
Loads once, applies everything, writes once.

Steps:
1. Mark 40 equations as error (49 wrong-LaTeX minus 9 tesla-restore)
2. Mark 6 equations as typo (from audit file)
3. Bulk mark remaining as ok
4. Restore LaTeX from raw for display/inline equations where raw IS LaTeX
5. Apply batch 1 physicist-generated LaTeX (50 equations)
6. Apply batch 2 physicist-generated LaTeX (51 equations)
"""
import json
import os
from collections import Counter
from datetime import datetime

ROOT = "C:/sandbox/Ainulindale Exflation"

# ---- LOAD ----
with open(os.path.join(ROOT, "tools/knowledge-index.json"), "r", encoding="utf-8") as f:
    idx = json.load(f)

eq_map = {eq["id"]: i for i, eq in enumerate(idx["equations"])}
print(f"Loaded: {len(idx['equations'])} equations")

# ============================================================
# STEP 1: Mark error equations
# ============================================================
# 49 original wrong-LaTeX IDs, minus 9 tesla equations whose raw IS LaTeX
all_49_error_ids = [
    "eq_596", "eq_666", "eq_667", "eq_668", "eq_669", "eq_670",
    "eq_672", "eq_673", "eq_681", "eq_682", "eq_683", "eq_684",
    "eq_698", "eq_699", "eq_700", "eq_701", "eq_702", "eq_703",
    "eq_704", "eq_705", "eq_789", "eq_792", "eq_794", "eq_798",
    "eq_836", "eq_842", "eq_896", "eq_990", "eq_1149", "eq_1150",
    "eq_1161", "eq_3789", "eq_5998", "eq_5999", "eq_6000",
    "eq_6047", "eq_6048", "eq_6049", "eq_6052", "eq_10891",
    "eq_12057", "eq_12067", "eq_12068", "eq_12073", "eq_12074",
    "eq_12075", "eq_12080", "eq_12081", "eq_12083"
]

tesla_restore_ids = {
    "eq_701", "eq_702", "eq_703", "eq_704", "eq_705",
    "eq_789", "eq_792", "eq_794", "eq_798"
}

error_count = 0
for eid in all_49_error_ids:
    if eid in tesla_restore_ids:
        continue
    if eid in eq_map:
        i = eq_map[eid]
        idx["equations"][i]["audit_status"] = "error"
        idx["equations"][i]["latex"] = None
        error_count += 1

print(f"Step 1: {error_count} set to error")

# ============================================================
# STEP 2: Mark typo equations
# ============================================================
typo_ids = ["eq_192", "eq_39", "eq_21", "eq_22", "eq_4", "eq_12"]
typo_count = 0
for eid in typo_ids:
    if eid in eq_map:
        i = eq_map[eid]
        idx["equations"][i]["audit_status"] = "typo"
        typo_count += 1

print(f"Step 2: {typo_count} set to typo")

# ============================================================
# STEP 3: Bulk mark remaining as ok
# ============================================================
bulk_ok = 0
for eq in idx["equations"]:
    if eq.get("audit_status") is None:
        eq["audit_status"] = "ok"
        bulk_ok += 1

print(f"Step 3: {bulk_ok} bulk-marked ok")

# ============================================================
# STEP 4: Restore LaTeX from raw where raw IS LaTeX
# ============================================================
latex_cmds = [
    "\\frac", "\\operatorname", "\\left", "\\right", "\\text{",
    "\\quad", "\\mathcal", "\\mathbb", "\\sqrt", "\\sum",
    "\\int", "\\prod", "\\partial", "\\nabla", "\\infty",
    "\\alpha", "\\beta", "\\gamma", "\\delta", "\\lambda",
    "\\sigma", "\\omega", "\\tau", "\\mu", "\\rho", "\\phi",
    "\\tag{", "\\begin{", "\\end{"
]

raw_restored = 0
for eq in idx["equations"]:
    if eq.get("latex") is None and eq.get("raw"):
        raw = eq["raw"]
        if eq.get("type") in ("display", "inline") and any(cmd in raw for cmd in latex_cmds):
            eq["latex"] = raw
            if eq["id"] in tesla_restore_ids:
                eq["audit_status"] = "ok"
            raw_restored += 1

# Structural LaTeX from tesla-framework aligned block
for eid in ["eq_795", "eq_796", "eq_797", "eq_798", "eq_799"]:
    if eid in eq_map:
        i = eq_map[eid]
        eq = idx["equations"][i]
        if eq.get("raw") and any(cmd in eq["raw"] for cmd in latex_cmds):
            if eq.get("latex") is None:
                eq["latex"] = eq["raw"]
                if eid in tesla_restore_ids:
                    eq["audit_status"] = "ok"
                raw_restored += 1

print(f"Step 4: {raw_restored} LaTeX restored from raw")

# ============================================================
# STEP 5: Batch 1 (50 equations from this session's physicist)
# ============================================================
batch1 = {
    "eq_124": r"\Delta_0^{(p,q)} = -\sum_{a,b} g^{ab}(s) \, \rho_{(p,q)}(e_a) \, \rho_{(p,q)}(e_b)",
    "eq_125": r"\Delta_1 = \nabla^* \nabla + \mathrm{Ric}",
    "eq_128": r"\mathrm{Pf}(A) \text{ defined for } 2n \times 2n \text{ antisymmetric matrix } A",
    "eq_130": r"N(j) = \left(\frac{m_j}{m_e}\right)^{2/3}, \quad m_j = m_e \, N(j)^{3/2}",
    "eq_132": r"N_{\mathrm{trials}} = N_{\mathrm{particle\;pairs}} \times N_{\mathrm{alt\;maps}} \times N_{s\;\mathrm{values}} \times N_{\mathrm{ratio\;targets}}",
    "eq_133": r"V_{\mathrm{CW}}(s) = \frac{1}{64\pi^2} \sum_n d_n \, \lambda_n^4(s) \left[ \ln\!\left(\frac{\lambda_n^2(s)}{\mu^2}\right) - \frac{3}{2} \right]",
    "eq_134": r"R(s) = -\frac{1}{4} e^{-4s} + 2 e^{-s} - \frac{1}{4} + \frac{1}{2} e^{2s}",
    "eq_135": r"R(0) = 2",
    "eq_157": r"\sin^2\theta_W = \frac{e^{-4s}}{1 + e^{-4s}}",
    "eq_158": r"m^2(C^2) = \frac{3}{2} \left(\frac{2}{15}\right)^5 e^{\sigma} \left[ (e^s - e^{-2s})^2 + (1 - e^{-s})^2 \right]",
    "eq_196": r"\Sigma(t) = \left( g_K(t),\; \{n_\alpha(t)\},\; \{c_{\alpha,\beta}(t)\} \right)",
    "eq_198": r"\alpha = \left( (p,q),\; j,\; \sigma \right)",
    "eq_200": r"\Sigma(t) = \left( \tau(t),\; \{n_\alpha(t)\} \right)",
    "eq_209": r"S[D] = \operatorname{Tr}\!\left( f\!\left(\frac{D^2}{\Lambda^2}\right) \right)",
    "eq_211": r"S(t) = \operatorname{Tr}\!\left( f\!\left(\frac{D_K(\tau(t))^2}{\Lambda^2}\right) \right) = \sum_n \mathrm{mult}_n \, f\!\left(\frac{\lambda_n(\tau(t))^2}{\Lambda^2}\right)",
    "eq_212": r"d_s(\tau, \sigma) = -2 \frac{d \ln K}{d \ln \sigma}",
    "eq_213": r"K(\tau, \sigma) = \sum_n \mathrm{mult}_n \, e^{-\sigma \lambda_n(\tau)^2}",
    "eq_215": r"d_s(t, \sigma) = d_s(\tau(t), \sigma)",
    "eq_285": r"D^2 = \nabla^2 + \frac{R_K}{4}",
    "eq_291": r"\mathrm{Sym}^2(\mathbf{8}) = \mathbf{1} \oplus \mathbf{8}_s \oplus \mathbf{27}",
    "eq_293": r"E_{\mathrm{Casimir}}^{\mathrm{TT}} = +\frac{1}{2} \sum_n \mathrm{mult}_n \sqrt{\lambda_n}",
    "eq_309": r"\mathrm{DOF}(\mathrm{TT}) = 27 \times \sum_{p+q \leq 6} \dim(p,q)^2",
    "eq_321": r"F(\tau) = F_{\mathrm{tree}}(\tau) + F_{\mathrm{CW}}(\tau) + F_{\mathrm{Casimir}}(\tau)",
    "eq_323": r"F_{\mathrm{Casimir}}(\tau) = F_{\mathrm{Casimir}}^{\mathrm{boson}}(\tau) - F_{\mathrm{Casimir}}^{\mathrm{fermion}}(\tau)",
    "eq_616": r"V_{\mathrm{CW}}'''(0) = 1.1134 \times 10^{9}",
    "eq_627": r"V_{\mathrm{CW}} = 3.1549 \times 10^{7}",
    "eq_628": r"V_{\mathrm{CW}}'' = 4.6294 \times 10^{8}",
    "eq_629": r"E_{\mathrm{Cas}} = 4.2699 \times 10^{5}",
    "eq_630": r"E_{\mathrm{Cas}}'' = 5.6128 \times 10^{5}",
    "eq_631": r"\xi_0(\mathrm{Casimir}) = 0.8722",
    "eq_632": r"G_{\tau\tau} = 5.0",
    "eq_634": r"d_{\mathrm{int}} = 8 > d_{\mathrm{uc}} = 4",
    "eq_643": r"F = a \eta^2 + c \eta^3 + b \eta^4, \quad a = \frac{V''}{2},\; c = \frac{V'''}{6},\; b = \frac{V''''}{24}",
    "eq_644": r"\Delta F = 1.8711 \times 10^{5}",
    "eq_645": r"\delta T''(0) = 0.0000",
    "eq_646": r"T'(0) = 1 + \delta T'(0) = -60.4350",
    "eq_649": r"R^2 = 0.996605",
    "eq_657": r"G_i(\mathrm{CW}) = 2.8543 \times 10^{-3}",
    "eq_658": r"G_i(\mathrm{Casimir}) = 5.3593 \times 10^{-3}",
    "eq_669": r"T''(0) = 0 \leq 0 \quad (\text{CLOSED})",
    "eq_670": r"\lambda_{\min} = 0.822148, \quad \text{gap-controlling sector} = (0,0)",
    "eq_671": r"N(0)_{\mathrm{singlet}} = 2",
    "eq_672": r"N(0)_{\mathrm{total}} = 22 \quad (\text{within } 5\% \text{ of gap})",
    "eq_675": r"g^* N(0)_{\mathrm{sing}} = 3.24, \quad g^* N(0)_{\mathrm{tot}} = 35.64",
    "eq_680": r"F_{\mathrm{true}}(\eta) = \min\!\left\{ F_{\mathrm{pert}}(\eta),\; F_{\mathrm{cond}}(\eta) \right\}",
    "eq_682": r"f(0,0) = -4.687 \quad \text{at } \tau = 0.30, \quad \text{threshold} = -3",
    "eq_683": r"f = -4.687 < -3 \quad \text{at } \tau = 0.30 \quad (\text{Pomeranchuk instability})",
    "eq_684": r"F_{\mathrm{cond}}(\Delta) = F_{\mathrm{normal}} - N(0) \frac{\Delta^2}{2g} + \cdots",
    "eq_698": r"M_{\max} = 0.077\text{--}0.155 \ll 1.0",
    "eq_699": r"\Delta_{\mathrm{gap,gap}} = 0 \quad (\text{structural selection rule})",
}

b1_applied = 0
for eid, latex in batch1.items():
    if eid in eq_map:
        i = eq_map[eid]
        idx["equations"][i]["latex"] = latex
        idx["equations"][i]["audit_status"] = "ok"
        b1_applied += 1

print(f"Step 5: Batch 1 — {b1_applied} applied")

# ============================================================
# STEP 6: Batch 2 (51 equations from this session's physicist)
# ============================================================
batch2 = {
    "eq_12172": r"h_{ab} = h^{\mathrm{TT}}_{ab} + \nabla_{(a} V_{b)} + \frac{1}{8} g_{ab} h",
    "eq_12173": r"h = g^{ab} h_{ab}",
    "eq_12175": r"\mathrm{Sym}^2(\mathbf{8}) = \mathbf{1} \oplus \mathbf{8} \oplus \mathbf{27}",
    "eq_12176": r"\dim(2,2) = \frac{(2+1)(2+1)(2+2+2)}{2} = 27",
    "eq_12153": r"V_{\mathrm{tree}}(\sigma, \tau) = -\frac{5}{4} \kappa M_P^2 \, e^{-3\sigma} \, R_K(\tau)",
    "eq_12154": r"\rho_\tau = \frac{5}{2} \dot{\tau}^2 + V_{\mathrm{eff}}(\tau)",
    "eq_12155": r"p_\tau = \frac{5}{2} \dot{\tau}^2 - V_{\mathrm{eff}}(\tau)",
    "eq_12156": r"w_\tau = \frac{p_\tau}{\rho_\tau}",
    "eq_12157": r"\epsilon = \frac{M_P^2}{2} \left(\frac{V'}{V}\right)^2 = \frac{M_P^2 \alpha^2}{10}",
    "eq_12158": r"\eta = M_P^2 \frac{V''}{V} = \frac{M_P^2 \alpha^2}{5}",
    "eq_138": r"m_{\min}(0,0) = 0.8221 \quad (\text{lightest})",
    "eq_139": r"m_{\min}(0,1) = 0.8340 \quad (1.014 \times m_{\min}(0,0))",
    "eq_140": r"m_{\min}(1,0) = 0.8340 \quad (1.014 \times m_{\min}(0,0))",
    "eq_141": r"m_{\min}(1,1) = 0.8710 \quad (1.059 \times m_{\min}(0,0))",
    "eq_142": r"m_{\min}(0,2) = 0.9760 \quad (1.187 \times m_{\min}(0,0))",
    "eq_143": r"m_{\min}(2,0) = 0.9760 \quad (1.187 \times m_{\min}(0,0))",
    "eq_144": r"m_{\min}(2,1) = 1.1285 \quad (1.373 \times m_{\min}(0,0))",
    "eq_145": r"m_{\min}(1,2) = 1.1285 \quad (1.373 \times m_{\min}(0,0))",
    "eq_602": r"I_E(\tau) = -\frac{R(\tau) \, \mathrm{Vol}(K)}{16\pi G}",
    "eq_606": r"S_{\mathrm{spin}}(\tau) = \frac{1}{4g^2} \int K(\tau) \, \mathrm{dvol}",
    "eq_585": r"\sin^2\theta_W = \frac{c_{u(1)}^2}{c_{u(1)}^2 + c_{su(2)}^2}",
    "eq_689": r"V(1,1) = 0 \quad (\text{gap-edge to gap-edge})",
    "eq_693": r"\text{BdG gap table: } M_{\max}(\mu=0) \text{ at each } \tau",
    "eq_636": r"d = 3, \quad n = 18 \quad (3 \times 3 \text{ complex matrix order parameter})",
    "eq_637": r"d_{\mathrm{eff}} = 1 \quad (\text{real scalar modulus})",
    "eq_638": r"V_{\mathrm{CW}}(0) = 2.031013 \times 10^{7}",
    "eq_639": r"V'(0) = -1.120008 \times 10^{6}",
    "eq_640": r"V''(0) = 1.638909 \times 10^{8}",
    "eq_641": r"V'''(0) = 1.113403 \times 10^{9}",
    "eq_642": r"V''''(0) = 6.994706 \times 10^{9}",
    "eq_650": r"V_{\mathrm{IR}}''(0.30) = -8.2422 < 0 \quad (N = 10, \; \text{IR SPINODAL})",
    "eq_652": r"V_{\mathrm{IR}}''(0.30) = -10.1310 < 0 \quad (N = 20, \; \text{IR SPINODAL})",
    "eq_654": r"V_{\mathrm{IR}}''(0.30) = -1.4429 < 0 \quad (N = 100, \; \text{IR SPINODAL})",
    "eq_659": r"V'''(0) = 1.1134 \times 10^{9} \neq 0",
    "eq_679": r"w = -1 \quad (\text{exactly, in BEC regime})",
    "eq_685": r"w = -1 \quad (\text{unless dynamically disrupted})",
    "eq_404": r"\Gamma_{\mathrm{eff}} = -i \int \frac{ds}{s} \, e^{-is m^2} \, \operatorname{Tr} e^{is D^2}",
    "eq_405": r"T(\tau) = \tau + \frac{1}{64\pi^2} \sum_n \Delta_b(n) \ln(\lambda_n^2(\tau)) \, R(\tau)",
    "eq_407": r"\delta T(\tau) = -\frac{\sum_n \Delta_b(n) \ln(\lambda_n^2(\tau))}{64\pi^2 \, e^{4\tau}}",
    "eq_408": r"T(\tau) = \tau + \delta T(\tau)",
    "eq_476": r"d\mu(\tau) = J(\tau) \, e^{-S[\tau]} \, d\tau",
    "eq_477": r"\Delta = \Delta_+ + \Delta_-",
    "eq_495": r"\Gamma^{(1)}[A] = i\hbar \int \frac{ds}{s} \, e^{-is m^2} \, \operatorname{Tr} e^{is \slashed{D}^2}",
    "eq_496": r"F_{\mathrm{cond}} = F_{\mathrm{pert}} - N(0) \frac{\Delta^2}{2g} + \mathcal{O}(\Delta^4)",
    "eq_497": r"\delta F = -N(0) \frac{\Delta^2}{2g} \approx -\frac{2 \times 0.36}{7.9} \approx -0.091",
    "eq_498": r"Z = \int \mathcal{D}[\Delta] \, e^{i \Gamma[\Delta]/\hbar}",
    "eq_499": r"S_{\mathrm{rad}} = \min_I \operatorname{ext}_{\partial I} \left[ \frac{A(\partial I)}{4G} + S_{\mathrm{bulk}}(I \cup R) \right]",
    "eq_503": r"F_{\min}(\tau) = F_{\mathrm{pert}}(\tau) - \frac{1}{2} N(0) \Delta_0^2",
    "eq_505": r"r(\tau_0) = \frac{\sqrt{\lambda_{(3,0)}^2 + \Delta_{(3,0)}^2}}{\sqrt{\lambda_{(0,0)}^2 + \Delta_{(0,0)}^2}}",
    "eq_506": r"\Delta = g \int \frac{\Delta}{\sqrt{\xi^2 + \Delta^2}} \, d\xi",
    "eq_508": r"\omega^2 = \frac{V_{FR}''(\tau_0)}{G_{\tau\tau}}",
}

b2_applied = 0
for eid, latex in batch2.items():
    if eid in eq_map:
        i = eq_map[eid]
        idx["equations"][i]["latex"] = latex
        idx["equations"][i]["audit_status"] = "ok"
        b2_applied += 1

print(f"Step 6: Batch 2 — {b2_applied} applied")

# ============================================================
# WRITE + SUMMARY
# ============================================================
with open(os.path.join(ROOT, "tools/knowledge-index.json"), "w", encoding="utf-8") as f:
    json.dump(idx, f, indent=2, ensure_ascii=False)

status_counts = Counter(str(eq.get("audit_status", "none")) for eq in idx["equations"])
with_latex = sum(1 for eq in idx["equations"] if eq.get("latex"))

print()
print("=" * 50)
print("FINAL STATE")
print("=" * 50)
for s, c in status_counts.most_common():
    print(f"  {s}: {c}")
print(f"  Total: {len(idx['equations'])}")
print(f"  With LaTeX: {with_latex}")
print()
print("Index written successfully.")
