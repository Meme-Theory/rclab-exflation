#!/usr/bin/env python3
"""
Curate equation names in the knowledge index.

Scans all 12,247 equations in tools/knowledge-index.json and assigns human-readable
names to recognizable physics equations based on pattern matching on the raw, latex,
context, type, and source_file fields.

Strategy:
- structural/display/inline equations: match on raw + latex + context
- comment equations: match on raw + context (but require physics content in raw)
- code equations: match ONLY on raw (context describes surrounding code, not the eq)
  and only for equations whose raw contains a recognizable physics formula
"""

import json
import re
from pathlib import Path


def load_index(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_index(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved to {path}")


def _is_physics_code(raw):
    """Check if a code-type equation's raw text contains a recognizable physics formula."""
    patterns = [
        r'Tr\s*\(?\s*f\s*\(?\s*D',
        r'Delta_L',
        r'Pf\s*\(',
        r'sin\^?2?\s*\(?\s*\\?theta_W',
        r'phi_paasch\s*=\s*[\d.]',
        r'phi\s*=\s*1\.53158',
        r'F/B\s*=\s*0\.55',
        r'a_0\s*=\s*2\^',
        r'BCS.*gap',
        r'Delta_k\s*=.*sum.*V.*Delta',
        r'Gross.?Pitaevskii',
        r'V_CW\s*[=(]',
        r'F_fermion.*=.*ln\s*\(|F_boson.*=.*ln\s*\(',
        r'A_F\s*=\s*C\s*\+\s*H\s*\+\s*M_3',
        r'Christoffel',
        r'Gauss.?Bonnet',
        r'spectral.*triple',
        r'Bekenstein|S_BH\s*=',
        r'BdG.*=|Bogoliubov',
        r'CHSH|Bell.*inequal',
        r'Koide',
        r'PMNS',
        r'Pomeranchuk',
        r'D_K\s*\\?psi\s*=\s*\\?lambda',
        r'D\^2\s*=\s*nabla\*\s*nabla',
        r'R\^f\{?\}?\s*_?\{?abc',
        r'R_\{?abcd\}?\s*=\s*-',
        r'g_\{?\\?mu\\?nu\}?.*T_\{?\\?mu\\?nu\}?',
        r'H\^2\s*=.*8.*pi.*G',
        r'Friedmann',
        r'geodesic\s*equation',
        r'S\s*=\s*Tr\s*\(?\s*f\s*\(?\s*D',
        r'spectral_action\s*=',
        r'seeley_dewitt',
        r'heat_kernel',
        r'berry_curvature',
        r'casimir_energy',
        r'instanton_action',
        r'coleman_weinberg',
        # Physics definitions (comment-style in code)
        r'Compute structure constants',
        r'Clifford algebra',
        r'Riemann tensor',
        r'Ricci tensor',
        r'Lichnerowicz',
        r'Euler characteristic',
        r'chi\s*\(\s*SU\(3\)\s*\)',
        r'Pfaffian.*CLEARED|Pfaffian.*PASS|Pfaffian.*FAIL',
        r'Pf\s*\(\s*Omega\s*\)',
        r'f_ON_\{?abc\}?',
        r'structure constants',
        r'Jensen.*metric|jensen_metric',
        r'Peter.?Weyl',
        r'volume.*preserv|det\(g\).*det\(g_0\)',
        r'Connection.*coefficient|Gamma_\{?cab\}?',
        r'Killing.*mode|Killing.*vector',
        r'Born rule',
        r'spectral\s*dimension',
        r'mean.?field.*exact|d_int.*>.*d_uc',
        r'Weyl.*law',
        r'asymptotic.*counting',
        r'partition\s*function',
        r'Coleman.?Weinberg',
        r'sign\^?2?\s*\(?\s*theta_W\s*\)?\s*=',
        r'cos\^?2?\s*\(?\s*theta_W\s*\)',
        r'alpha_em.*cos\^?2',
        r'spectral.*gap',
        r'BCS.*critical',
        r'Gauss.?Bonnet.*invariant',
        r'E_4\s*=.*epsilon.*epsilon.*R',
        r'chirality.*grading',
    ]
    for pat in patterns:
        if re.search(pat, raw, re.IGNORECASE):
            return True
    return False


def classify_equation(eq):
    """
    Return a name string for the equation, or None if it should not be named.
    """
    raw = (eq.get('raw') or '').strip()
    latex = (eq.get('latex') or '').strip()
    context = (eq.get('context') or '').strip()
    eq_type = (eq.get('type') or '').strip()
    tag = (eq.get('tag') or '').strip()
    source = (eq.get('source_file') or '').strip()

    raw_lower = raw.lower()
    ctx_lower = context.lower()

    # For code-type equations:
    #   1. Only proceed if raw contains a recognizable physics formula
    #   2. Match on raw only (not context, which describes surrounding code)
    if eq_type == 'code':
        if not _is_physics_code(raw):
            return None
        combined = raw_lower  # Only match on raw for code
    elif eq_type == 'comment':
        # Comments are often physics descriptions; use raw + context
        combined = f"{raw} {context}".lower()
    else:
        # structural, display, inline: use everything
        combined = f"{raw} {latex} {context}".lower()

    # =========================================================================
    # TIER 1: Exact named equations (highest confidence)
    # =========================================================================

    # --- Spectral Action ---
    if re.search(r'Tr\s*\(?\s*f\s*\(?\s*D\s*/\s*\\?Lambda', raw) or \
       re.search(r'Tr\s*\(?\s*f\s*\(?\s*D\^?2?\s*/\s*\\?Lambda', raw) or \
       re.search(r'S\s*=\s*Tr\s*\(?\s*f\s*\(?\s*D', raw) or \
       re.search(r'S\[D\]\s*=\s*Tr', raw):
        if 'bosonic' in combined or 'boson' in raw_lower:
            return "Bosonic Spectral Action"
        if 'fermionic' in combined or 'fermion' in raw_lower:
            return "Fermionic Spectral Action"
        return "Spectral Action"
    if 'spectral action' in combined and eq_type in ('structural', 'display', 'inline'):
        if re.search(r'=|sum|integral|Tr', raw):
            if 'finite.*temp' in combined:
                return "Spectral Action (Finite Temperature)"
            return "Spectral Action"

    # --- Gross-Pitaevskii Equation ---
    if 'gross-pitaevskii' in combined or 'gross pitaevskii' in combined:
        return "Gross-Pitaevskii Equation"

    # --- Einstein Field Equations ---
    if re.search(r'G_\{?\\?mu\\?nu\}?\s*[\+\=]', raw) and 'T_' in raw:
        return "Einstein Field Equations"
    if re.search(r'G_\\mu\\nu', latex) and 'T_' in latex:
        return "Einstein Field Equations"

    # --- Friedmann Equation ---
    if re.search(r'H\^2\s*=\s*.*8\\?pi\s*G', raw) or \
       re.search(r'H\^2\s*=\s*\\frac\{8\\pi\s*G\}', latex):
        return "Friedmann Equation"
    if re.search(r'friedmann', combined) and eq_type in ('structural', 'display', 'inline'):
        return "Friedmann Equation"

    # --- Dirac Eigenvalue Equation ---
    if re.search(r'D_K\s*\\?psi\s*=\s*\\?lambda\s*\\?psi', raw) or \
       re.search(r'D\s*\\?psi\s*=\s*\\?lambda\s*\\?psi', raw):
        return "Dirac Eigenvalue Equation"

    # --- Lichnerowicz-Schroedinger Formula ---
    if re.search(r'D\^2\s*=\s*\\?nabla\*?\s*\\?nabla\s*\+\s*R', raw):
        return "Lichnerowicz-Schroedinger Formula"

    # --- Coleman-Weinberg Potential ---
    if re.search(r'V_\{?\\?mathrm\{CW\}\}?', raw) or re.search(r'V_CW\b', raw) or \
       re.search(r'V_1loop', raw):
        return "Coleman-Weinberg Potential"
    if re.search(r'coleman.?weinberg', combined):
        return "Coleman-Weinberg Potential"
    if re.search(r'1/(64\s*\\?pi\^2)\s*sum.*lambda.*\^4.*ln', combined):
        return "Coleman-Weinberg Potential"
    if re.search(r'\\frac\{3\}\{64\\pi\^2\}\s*\\sum.*m.*\^4.*\\log', latex):
        return "Coleman-Weinberg Potential"

    # --- Effective Potential ---
    if re.search(r'V_\{?\\?mathrm\{eff\}\}?\s*\(', raw) or \
       re.search(r'V_\{\\text\{eff\}\}\s*\(', latex):
        if 'full' in raw_lower:
            return "Full Effective Potential"
        return "Effective Potential"

    # --- Seeley-DeWitt Coefficients / Heat Kernel ---
    if re.search(r'seeley', combined) or re.search(r'dewitt', combined):
        if re.search(r'a_[024]', raw):
            return "Seeley-DeWitt Coefficients"
        return "Seeley-DeWitt Expansion"
    if re.search(r'heat\s*kernel', combined):
        if re.search(r'K\(.*\)\s*=\s*Tr\s*\(\s*exp', raw) or \
           re.search(r'exp\s*\(\s*-.*D.*\^2', raw):
            return "Heat Kernel Trace"
        if re.search(r'a_[024]', raw):
            return "Heat Kernel Coefficients"
        if eq_type in ('structural', 'display', 'inline', 'comment'):
            return "Heat Kernel Expansion"
    if re.search(r'K_L\(t\)\s*=\s*Sum.*e\^\{?-lambda', raw):
        return "Heat Kernel Expansion"

    # --- Spectral Zeta Function ---
    if re.search(r'\\?zeta.*\(z\)\s*=\s*.*sum.*\\?lambda.*\^?\{?-z', combined):
        return "Spectral Zeta Function"

    # --- Lichnerowicz Operator ---
    if re.search(r'\\?Delta_L\s*h', raw) or \
       (re.search(r'lichnerowicz', combined) and eq_type != 'code'):
        if re.search(r'=\s*.*\\?nabla\^?2.*h.*R.*h', raw) or \
           re.search(r'=\s*\\?Delta\s*h.*R.*h', raw) or \
           re.search(r'=\s*-\\nabla\^2\s*h.*R.*h', latex):
            return "Lichnerowicz Operator"
        if 'eigenvalue' in combined or 'eigenval' in combined or 'spectrum' in combined:
            return "Lichnerowicz Eigenvalue Problem"
        if eq_type in ('structural', 'display', 'inline', 'comment'):
            return "Lichnerowicz Operator"
    if eq_type == 'code' and re.search(r'Lichnerowicz', raw):
        if re.search(r'Delta_L|lichnerowicz.*operator|rough_lap.*R_endo', raw, re.IGNORECASE):
            return "Lichnerowicz Operator"

    # --- Riemann Curvature Tensor ---
    if re.search(r"R\^?\{?f\}?\s*_?\{?abc\}?\s*=", raw) and ('Gamma' in raw or 'f_' in raw):
        return "Riemann Curvature Tensor"
    if re.search(r'R_\{?abcd\}?\s*=\s*-\s*(1/4|\\frac\{1\}\{4\}).*f_', raw):
        return "Riemann Tensor (Bi-Invariant Metric)"
    if re.search(r'riemann\s*tensor', combined) and eq_type in ('structural', 'display', 'inline', 'comment'):
        return "Riemann Curvature Tensor"

    # --- Ricci Tensor ---
    if re.search(r'\\?mathrm\{Ric\}.*=.*frac.*lambda', raw) or \
       re.search(r'Ric\(g\^s\)\s*=', raw):
        return "Ricci Tensor (Jensen Metric)"
    if re.search(r'Ric_?\{?bc\}?\s*=\s*.*sum.*R\^?a', raw) or \
       re.search(r'\\mathrm\{Ric\}_\{bc\}\s*=\s*\\sum_a\s*R\^a', latex):
        return "Ricci Tensor Contraction"

    # --- Casimir Energy ---
    if 'casimir' in combined and eq_type in ('structural', 'display', 'inline'):
        if re.search(r'E_\{?\\?text\{Casimir\}', raw) or \
           re.search(r'casimir.*energy', combined) or re.search(r'integral.*omega', raw):
            return "Casimir Energy"
        if 'sign change' in combined:
            return "Casimir Sign Change"
        return "Casimir Energy"

    # --- BCS Gap Equation ---
    if re.search(r'Delta_k\s*=.*sum.*V.*Delta.*E', raw) or \
       re.search(r'\\Delta_k\s*=.*\\sum.*V.*\\Delta.*E', latex):
        return "BCS Gap Equation"
    if re.search(r'bcs.*gap', combined) and eq_type in ('structural', 'display', 'inline', 'comment'):
        return "BCS Gap Equation"
    if 'bcs' in combined and eq_type in ('structural', 'display', 'inline'):
        if 'condensat' in combined:
            return "BCS Condensate"
        if 'critical' in combined or 'threshold' in combined:
            return "BCS Critical Condition"
        return "BCS Gap Equation"

    # --- Bogoliubov / BdG ---
    if re.search(r'gamma_k\s*=\s*u_k.*a_k.*v_k.*a', raw):
        return "Bogoliubov Transformation"
    if re.search(r'M_\{?BdG\}?', raw) or re.search(r'M_BdG', raw):
        return "BdG Matrix Element"
    if re.search(r'bogoliubov', combined) and eq_type in ('structural', 'display', 'inline'):
        if 'quasiparticle' in combined:
            return "Bogoliubov Quasiparticle Energy"
        return "BdG Formalism"

    # --- Pfaffian ---
    if re.search(r'Pf\s*\(', raw) or re.search(r'\\operatorname\{Pf\}', raw):
        if 'sign' in combined or 'sgn' in raw or 'operatorname{sgn}' in raw:
            return "Pfaffian Invariant"
        return "Pfaffian"
    if re.search(r'pfaffian', raw_lower) and eq_type in ('structural', 'display', 'inline', 'comment'):
        return "Pfaffian"
    if re.search(r'\\mathrm\{Pf\}', raw):
        return "Pfaffian Invariant"

    # --- Berry Phase / Curvature ---
    if re.search(r'berry', combined) and eq_type in ('structural', 'display', 'inline'):
        if 'curvature' in combined or re.search(r'\\Omega', raw):
            return "Berry Curvature"
        if 'phase' in combined:
            return "Berry Phase"
        if 'connection' in combined:
            return "Berry Connection"
        if 'monopole' in combined:
            return "Berry Curvature Monopole"

    # --- Chern Number ---
    if re.search(r'chern', combined):
        if eq_type == 'code' and re.search(r'E_4\s*=.*epsilon.*epsilon.*R', raw):
            return "Chern Number (Euler Integrand)"
        if eq_type in ('structural', 'display', 'inline', 'comment'):
            if re.search(r'C_n\s*=.*integral', raw) or re.search(r'chern.*number', combined):
                return "Chern Number"
            if re.search(r'chern.*simons', combined):
                return "Chern-Simons Form"
            return "Chern Number"

    # --- Gauss-Bonnet ---
    if re.search(r'gauss.?bonnet', combined):
        if eq_type in ('structural', 'display', 'inline', 'comment'):
            return "Gauss-Bonnet Invariant"
        if eq_type == 'code' and re.search(r'gauss.?bonnet', raw, re.IGNORECASE):
            return "Gauss-Bonnet Invariant"

    # --- Euler Characteristic ---
    if re.search(r'euler.*characteristic', raw_lower) and eq_type in ('structural', 'display', 'inline', 'comment'):
        return "Euler Characteristic"
    if re.search(r'chi\s*\(\s*SU\(3\)\s*\)', raw):
        return "Euler Characteristic"

    # --- Weyl's Law ---
    if re.search(r"weyl", combined):
        if re.search(r'law', combined) or re.search(r'asymptoti', combined) or \
           re.search(r'counting', combined):
            if eq_type in ('structural', 'display', 'inline', 'comment'):
                return "Weyl's Law"

    # --- Partition Function ---
    if re.search(r'Z\s*\(.*\)\s*=\s*.*sum.*exp', raw) and 'partition' in combined:
        return "Partition Function"
    if re.search(r'partition\s*function', combined) and eq_type in ('structural', 'display', 'inline'):
        return "Partition Function"

    # --- Free Energy ---
    if re.search(r'free\s*energy', combined) and eq_type in ('structural', 'display', 'inline'):
        if 'landau' in combined:
            return "Landau Free Energy"
        if re.search(r'F\s*=.*sum.*f\(omega', raw):
            return "Spectral Free Energy"
        return "Free Energy"

    # --- Fermi-Dirac / Bose-Einstein ---
    if re.search(r'fermi.?dirac', combined) and eq_type in ('structural', 'display', 'inline'):
        return "Fermi-Dirac Distribution"
    if re.search(r'bose.?einstein', combined) and eq_type in ('structural', 'display', 'inline'):
        return "Bose-Einstein Distribution"

    # --- KK Mass Formula ---
    if re.search(r'\(Mass.*h_n\)\^2\s*=\s*mu_n', raw) or \
       re.search(r'\\mathrm\{Mass\}.*h_n.*=.*\\mu_n', latex):
        return "Kaluza-Klein Mass Formula"
    if re.search(r'm_n\^2\s*=\s*\\?mu_n\s*-', raw):
        return "KK Mode Mass"

    # --- Instanton Action ---
    if re.search(r'S_\{?\\?text\{inst\}\}?', raw) or re.search(r'S_inst\b', raw):
        if re.search(r'=.*8\\?pi\^2', raw) or re.search(r'=.*Vol', raw):
            return "Instanton Action"
    if re.search(r'instanton', combined) and eq_type in ('structural', 'display', 'inline'):
        if 'action' in combined:
            return "Instanton Action"
        return "Instanton"

    # --- Spectral Triple ---
    if re.search(r'spectral\s*triple', combined) and eq_type in ('structural', 'display', 'inline'):
        return "Spectral Triple"

    # --- KO-Dimension ---
    if re.search(r'KO.?dim', combined) and eq_type in ('structural', 'display', 'inline', 'comment'):
        return "KO-Dimension"
    if re.search(r'J\^2\s*=\s*\+?1.*JD\s*=.*DJ.*J\\?gamma\s*=', raw):
        return "KO-Dimension Signs (J, D, gamma)"

    # --- CPT Commutator ---
    if re.search(r'\[J,\s*D', raw) and ('= 0' in raw or 'CPT' in combined):
        return "CPT Commutator"
    if re.search(r'CPT', raw) and eq_type in ('structural', 'display', 'inline'):
        if 'hardwired' in combined or 'exact' in combined:
            return "CPT Invariance"

    # --- Gauge Coupling Ratio ---
    if re.search(r'g_?1\s*/\s*g_?2\s*=.*e\^\{?-2', raw):
        return "Gauge Coupling Ratio Identity"
    if re.search(r'g_1/g_2\s*=\s*\\tan\\theta_W', latex) or \
       re.search(r'g1/g2\s*=\s*\\?tan.*theta_W', raw):
        return "Gauge Coupling Ratio Identity"

    # --- Weinberg Angle ---
    if re.search(r'sin\^?2?\s*\(?\s*\\?theta_W\s*\)?\s*=', raw):
        return "Weinberg Angle"
    if re.search(r'\\sin\^2.*\\theta_W\s*=', latex):
        return "Weinberg Angle"
    if eq_type == 'comment' and re.search(r'(sin|cos)\^?2?\s*\(?\s*theta_W', raw):
        return "Weinberg Angle"

    # --- Clock Constraint ---
    if re.search(r'd\\?alpha.*=.*tau_dot', raw) or \
       re.search(r'\\frac\{d\\alpha', latex) or \
       re.search(r'dalpha.*alpha.*=.*-3\.08', combined):
        return "Clock Constraint"
    if re.search(r'clock\s*constraint', combined) and eq_type in ('structural', 'display', 'inline'):
        return "Clock Constraint"

    # --- Paasch Phi Ratio ---
    if re.search(r'phi_paasch\s*=\s*1\.53158', raw) or \
       re.search(r'm_?\{?\(3,0\)\}?\s*/\s*m_?\{?\(0,0\)\}?\s*=\s*1\.53', raw):
        return "Paasch Phi Ratio"
    if re.search(r'1\.53158', raw) and eq_type in ('structural', 'display', 'inline'):
        return "Paasch Phi Ratio"
    if re.search(r'phi_paasch', raw) and eq_type in ('structural', 'display', 'inline', 'comment'):
        if re.search(r'=|ratio|mass', combined):
            return "Paasch Phi Ratio"

    # --- Constant-Ratio Trap ---
    if re.search(r'F/B\s*=\s*0\.55', raw):
        return "Constant-Ratio Trap (F/B)"
    if re.search(r'constant.?ratio\s*trap', combined) and eq_type in ('structural', 'display', 'inline'):
        return "Constant-Ratio Trap (F/B)"

    # --- Jensen Deformation Metric ---
    if re.search(r'jensen.*deform', combined) and eq_type in ('structural', 'display', 'inline'):
        return "Jensen Deformation Metric"
    if re.search(r'g\^s\s*=.*diag', raw) and ('jensen' in combined or 'lambda' in raw):
        if eq_type in ('structural', 'display', 'inline'):
            return "Jensen Deformation Metric"
    if re.search(r'jensen.*metric', combined) and eq_type in ('structural', 'display', 'inline', 'comment'):
        return "Jensen Deformation Metric"
    if eq_type == 'code' and re.search(r'jensen_metric', raw, re.IGNORECASE):
        return "Jensen Deformation Metric"

    # --- Jensen Deformation Parameters ---
    if re.search(r'lambda_[123]\s*=\s*.*e\^\{?[+-]?[0-9]*\s*\\?tau', raw) and \
       eq_type in ('structural', 'display', 'inline'):
        return "Jensen Deformation Parameters"

    # --- Peter-Weyl Decomposition ---
    if re.search(r'peter.?weyl', combined):
        if eq_type in ('structural', 'display', 'inline', 'comment'):
            if re.search(r'L\^2.*=.*bigoplus', raw) or re.search(r'decompos', combined) or \
               re.search(r'D_\{?\(p,q\)\}?', raw):
                return "Peter-Weyl Decomposition"
            return "Peter-Weyl Decomposition"

    # --- Scalar Laplacian on Irreps ---
    if re.search(r'Delta_0\^?\{?\(p,q\)\}?\s*=', raw):
        return "Scalar Laplacian on Irrep"
    if re.search(r'scalar\s*laplacian', combined) and eq_type in ('structural', 'display', 'inline'):
        return "Scalar Laplacian on Irrep"

    # --- Yukawa Coupling ---
    if re.search(r'yukawa', combined) and eq_type in ('structural', 'display', 'inline'):
        if 'matrix' in combined or 'Y' in raw:
            return "Yukawa Coupling Matrix"
        return "Yukawa Coupling"

    # --- Neutrino Mass ---
    if re.search(r'neutrino', combined) and eq_type in ('structural', 'display', 'inline'):
        if re.search(r'm_\\?nu', raw) or 'mass' in combined:
            return "Neutrino Mass"

    # --- PMNS Matrix ---
    if re.search(r'PMNS', raw) and eq_type in ('structural', 'display', 'inline'):
        return "PMNS Mixing Matrix"

    # --- Koide Formula ---
    if re.search(r'koide', combined) and eq_type in ('structural', 'display', 'inline'):
        return "Koide Formula"

    # --- Hawking Temperature ---
    if re.search(r'hawking', combined) and ('temperature' in combined or 'radiation' in combined):
        if eq_type in ('structural', 'display', 'inline'):
            return "Hawking Temperature"
    if re.search(r'T_\{?\\?text\{GH\}\}?\s*=', raw):
        return "Gibbons-Hawking Temperature"

    # --- Bekenstein-Hawking Entropy ---
    if re.search(r'bekenstein', combined) and eq_type in ('structural', 'display', 'inline'):
        return "Bekenstein-Hawking Entropy"
    if re.search(r'S_BH\s*=', raw):
        return "Bekenstein-Hawking Entropy"
    if re.search(r'S_\{?\\?text\{dS\}\}?\s*=', raw) and re.search(r'\\?Lambda', raw):
        return "de Sitter Entropy"

    # --- Generalized Second Law ---
    if re.search(r'delta\s*S_gen.*>=\s*0', raw):
        return "Generalized Second Law"
    if re.search(r'S_gen\s*=\s*.*A.*4.*G', raw):
        return "Generalized Entropy"

    # --- Cosmological Constant ---
    if re.search(r'cosmological\s*constant', combined) and eq_type in ('structural', 'display', 'inline'):
        return "Cosmological Constant"
    if re.search(r'rho_\\?Lambda\s*=\s*.*sum.*omega', raw):
        return "Vacuum Energy (Zero-Point Sum)"

    # --- Hubble Parameter ---
    if re.search(r'hubble', combined) and eq_type in ('structural', 'display', 'inline'):
        return "Hubble Parameter"

    # --- Slow-Roll ---
    if re.search(r'slow.?roll', combined) and eq_type in ('structural', 'display', 'inline'):
        if re.search(r'\\?epsilon\s*=|\\?eta\s*=', raw):
            return "Slow-Roll Parameters"
        return "Slow-Roll Condition"

    # --- Quintessence / Equation of State ---
    if re.search(r'w_\\?tau\s*=', raw) and eq_type in ('structural', 'display', 'inline'):
        return "Equation of State (Quintessence)"
    if re.search(r'w_0.*w_a', raw) and ('dark energy' in combined or 'DESI' in combined):
        return "Dark Energy Equation of State (CPL)"

    # --- Loop Quantum Cosmology ---
    if re.search(r'1\s*-\s*\\?rho/\\?rho_c', raw) and re.search(r'H\^2', raw):
        return "Modified Friedmann Equation (LQC)"
    if re.search(r'loop\s*quantum', combined) and eq_type in ('structural', 'display', 'inline'):
        return "Modified Friedmann Equation (LQC)"

    # --- Spectral Dimension ---
    if re.search(r'd_s\s*\(.*\)\s*=\s*-2.*d\s*ln\s*P', raw):
        return "Spectral Dimension"
    if re.search(r'spectral.*dimension', combined) and eq_type in ('structural', 'display', 'inline', 'comment'):
        return "Spectral Dimension"

    # --- Acoustic Impedance ---
    if re.search(r'Z_\{?\\?text\{total\}\}?.*=.*Z_\{?\\?text\{scalar\}', raw):
        return "Total Acoustic Impedance"

    # --- Dispersion Relation ---
    if re.search(r'omega\^2\s*\(\s*p\s*,\s*q\s*\)\s*=\s*C_2', raw):
        return "Dispersion Relation"
    if re.search(r'dispersion.*relation', combined) and eq_type in ('structural', 'display', 'inline'):
        return "Dispersion Relation"

    # --- Killing Vector ---
    if re.search(r'closing', combined) and eq_type in ('structural', 'display', 'inline'):
        if 'zero mode' in combined or re.search(r'm\^2.*=\s*0', raw):
            return "Killing Mode (Zero Mass)"
        return "Killing Vector Field"

    # --- Modular Flow / Thermal Time ---
    if re.search(r'sigma.*=\s*e\^\{?iHt', raw) or re.search(r'\\sigma_t', raw):
        if eq_type in ('structural', 'display', 'inline'):
            return "Modular Flow (KMS State)"
    if re.search(r't_\{?\\?text\{modular\}\}?\s*=', raw):
        return "Modular Time Relation"
    if re.search(r'modular.*flow', combined) and eq_type in ('structural', 'display', 'inline'):
        return "Modular Flow"

    # --- Sigma Field / Modulus ---
    if re.search(r'm_\\?sigma\^2\s*=', raw) and eq_type in ('structural', 'display', 'inline'):
        return "Sigma Field Mass"
    if re.search(r'm_\{?\\?sigma\}?\s*>', raw) and eq_type in ('structural', 'display', 'inline'):
        return "Sigma Mass Bound"
    if re.search(r'\\ddot.*\\delta\\tau.*3H.*\\dot.*\\delta\\tau.*m_\\sigma', latex):
        return "Modulus Oscillation Equation"

    # --- Proper Time ---
    if re.search(r'd\\?tau_\{?\\?text\{proper\}\}?\^2\s*=\s*-g', raw):
        return "Proper Time (GR)"

    # --- Relaxation Timescale ---
    if re.search(r't_\{?\\?text\{relax\}\}?\s*=', raw):
        return "Relaxation Timescale"

    # --- Pomeranchuk Instability ---
    if re.search(r'pomeranchuk', combined) and eq_type in ('structural', 'display', 'inline'):
        if re.search(r'f\s*\(0,0\)', raw) or re.search(r'instab', combined):
            return "Pomeranchuk Instability"
        return "Pomeranchuk Criterion"

    # --- Landau Parameter ---
    if re.search(r'landau.*parameter', combined) and eq_type in ('structural', 'display', 'inline'):
        return "Landau Parameter"

    # --- Ginzburg-Landau ---
    if re.search(r'ginzburg.?landau', combined) and eq_type in ('structural', 'display', 'inline'):
        if 'free energy' in combined:
            return "Ginzburg-Landau Free Energy"
        return "Ginzburg-Landau Theory"

    # --- Order Parameter ---
    if re.search(r'order\s*parameter', combined) and eq_type in ('structural', 'display', 'inline'):
        return "Order Parameter"

    # --- DNP Instability ---
    if re.search(r'lambda_L/m\^2', raw) and re.search(r'<\s*3', raw):
        return "DNP Instability"

    # --- TT Tensor ---
    if re.search(r'TT.*tensor', combined) and eq_type in ('structural', 'display', 'inline'):
        if 'mass' in combined:
            return "TT Tensor KK Mode Mass"
        if '741' in raw:
            return "TT Tensor DOF Count"
        return "TT Tensor Decomposition"

    # --- Symmetric Tensor Decomposition ---
    if re.search(r'Sym\^2', raw) and eq_type in ('structural', 'display', 'inline', 'comment'):
        return "Symmetric Tensor Decomposition"

    # --- Altland-Zirnbauer / Symmetry Class ---
    if re.search(r'AZ\s*class', combined) and eq_type in ('structural', 'display', 'inline'):
        return "Altland-Zirnbauer Classification"
    if re.search(r'BDI', raw) and re.search(r'T\^2\s*=\s*\+1', raw):
        return "Symmetry Class BDI"

    # --- Level Statistics ---
    if re.search(r'P_\{?Poisson\}?\s*\(s\)', raw):
        return "Poisson Level Statistics"
    if re.search(r'GOE|GUE|GSE', raw) and ('level' in combined or 'wigner' in combined):
        return "Wigner-Dyson Level Statistics"

    # --- Spectral Gap ---
    if re.search(r'spectral\s*gap', combined) and eq_type in ('structural', 'display', 'inline'):
        return "Spectral Gap"

    # --- Winding Number ---
    if re.search(r'nu\s*=.*integral.*det', raw):
        return "Winding Number"

    # --- Topological Invariant ---
    if re.search(r'Z_2\s*invariant', combined) and eq_type in ('structural', 'display', 'inline'):
        return "Topological Invariant"

    # --- Homotopy Group ---
    if re.search(r'pi_3\s*\(\s*SU\(3\)\s*\)\s*=\s*Z', raw):
        return "Homotopy Group pi_3(SU(3))"

    # --- Structure Constants ---
    if re.search(r'structure\s*constants?\s*c\^k_\{?ij\}?', raw, re.IGNORECASE):
        return "Structure Constants"
    if re.search(r'f_\{?abc\}?', raw) and 'structure constant' in combined:
        return "Structure Constants"
    if re.search(r'f_ON_\{?abc\}?', raw) or \
       re.search(r'ON\s*structure\s*constants', raw, re.IGNORECASE):
        return "Structure Constants (ON Basis)"

    # --- Christoffel / Connection ---
    if re.search(r'christoffel', combined) and eq_type in ('structural', 'display', 'inline', 'comment'):
        return "Christoffel Symbols"
    if re.search(r'\\?nabla_\{?X_a\}?\s*X_b\s*=', raw) and eq_type in ('structural', 'display', 'inline'):
        return "Connection Coefficients"
    if re.search(r'Gamma_\{?cab\}?\s*=\s*\(1/2\)\s*f', raw):
        return "Connection Coefficients (Bi-Invariant)"
    if re.search(r'connection.*coefficient', combined) and eq_type in ('structural', 'display', 'inline', 'comment'):
        return "Connection Coefficients"

    # --- Kosmann Lie Derivative ---
    if re.search(r'kosmann', combined):
        if eq_type in ('structural', 'display', 'inline', 'comment'):
            if re.search(r'L_X\s*\\?psi', raw) or re.search(r'lie.*deriv', combined):
                return "Kosmann Lie Derivative"
            if 'norm' in combined or 'K_a' in raw:
                return "Kosmann Coupling Norm"
            return "Kosmann Lie Derivative"

    # --- Volume Preservation ---
    if re.search(r'vol_\{?g\^s\}?\s*=\s*vol_\{?g\^0', raw):
        return "Volume Preservation"
    if re.search(r'volume.*preserv', combined) and eq_type in ('structural', 'display', 'inline', 'comment'):
        if re.search(r'det|vol|ratio.*=.*1', raw):
            return "Volume Preservation"

    # --- Bianchi Identity ---
    if re.search(r'bianchi\s*identity', combined) and eq_type in ('structural', 'display', 'inline'):
        return "Bianchi Identity"

    # --- Energy-Momentum Conservation ---
    if re.search(r'nabla_a\s*T\^\{?a.*mu\}?', raw):
        return "Energy-Momentum Conservation"

    # --- Flux ---
    if re.search(r'F_\{?4\}?\s*=\s*c.*epsilon', raw):
        return "4-Form Flux Ansatz"

    # --- Branching Rule ---
    if re.search(r'\\mathbf\{8\}\s*\\to\s*\\mathbf\{3\}', latex):
        return "SU(3) to SU(2)xU(1) Branching Rule"

    # --- b1/b2 Ratio ---
    if re.search(r'b_?1\s*/\s*b_?2\s*=\s*4/9', raw) or \
       re.search(r'S_\{?b_?1\}?\s*/\s*S_\{?b_?2\}?\s*=\s*4/9', raw):
        return "Gauge Threshold Ratio (b1/b2 = 4/9)"

    # --- Block Diagonality ---
    if re.search(r'block.?diagonal', raw_lower) and eq_type in ('structural', 'display', 'inline'):
        if 'D_K' in raw or 'dirac' in raw_lower:
            return "D_K Block-Diagonality Theorem"
        if 'B_' in raw or '= 0' in raw:
            return "Block-Diagonality"

    # --- Second-Order Perturbation Theory ---
    if re.search(r'\\lambda_n.*=.*\\lambda_n.*\\sum.*V_\{nm\}', latex):
        return "Second-Order Perturbation Theory"
    if re.search(r'lambda_n.*=.*lambda_n.*sum.*V.*/(.*lambda_n.*-.*lambda_m)', raw):
        return "Second-Order Perturbation Theory"
    if re.search(r'\\sum.*\\frac\{.*V_\{nm\}.*\^2\}\{\\lambda_n\s*-\s*\\lambda_m\}', latex) or \
       re.search(r'sum.*V_\{nm\}.*\^2.*lambda_n.*-.*lambda_m', raw):
        return "Second-Order Perturbation Theory"
    if re.search(r'delta.*delta_T.*coupled.*sum.*frac', raw_lower) or \
       re.search(r'\\delta.*delta.*coupled.*\\sum.*\\frac', latex):
        return "Coupling Correction (Perturbative)"

    # --- Trap 3 ---
    if re.search(r'e/\(a\*c\)\s*=\s*1/16', raw):
        return "Tensor Product Trap (e/(ac) = 1/16)"

    # --- Einstein-Hilbert Action ---
    if re.search(r'einstein.?hilbert', combined) and eq_type in ('structural', 'display', 'inline'):
        if 'second variation' in combined or 'I_h' in raw:
            return "Einstein-Hilbert Action (Second Variation)"
        return "Einstein-Hilbert Action"

    # --- Action (generic) ---
    if re.search(r'S\s*=\s*\\?int.*d\^?\d?\s*x', raw) and eq_type in ('structural', 'display', 'inline'):
        return "Action Integral"

    # --- Geometric Spectral Action ---
    if re.search(r'S_geo\s*=\s*sum.*gamma.*f\(lambda', raw):
        return "Geometric Spectral Action (Berry Phase)"

    # --- Finite Algebra (NCG) ---
    if re.search(r'A_F\s*=\s*C\s*\+\s*H\s*\+\s*M_3\s*\(\s*C\s*\)', raw):
        return "Finite Algebra (NCG Standard Model)"

    # --- Spinor Space ---
    if re.search(r'Psi_\+?\s*=\s*C\^?\{?16\}?', raw):
        return "Spinor Space (C^16)"

    # --- Chirality Grading ---
    if re.search(r'chirality.*grading', combined):
        if eq_type in ('structural', 'display', 'inline', 'comment'):
            return "Chirality Grading"

    # --- V_spec / Spectral Potential ---
    if re.search(r'V_spec', raw) or re.search(r'V_\{\\text\{spec\}\}', latex):
        if eq_type in ('structural', 'display', 'inline'):
            if 'monoton' in combined:
                return "Spectral Potential V_spec (Monotonicity)"
            return "Spectral Potential V_spec"

    # --- Inter-sector Level Repulsion ---
    if re.search(r'R_\{?\\?mathrm\{reg\}\}?', raw) and 'sector' in combined:
        return "Inter-Sector Level Repulsion"

    # --- Connes 8-cutoff ---
    if re.search(r'connes.*8.*cutoff', combined) or re.search(r'8.*cutoff.*connes', combined):
        if eq_type in ('structural', 'display', 'inline'):
            return "Connes 8-Cutoff Test"

    # --- AM-GM ---
    if re.search(r'AM.?GM', combined) and eq_type in ('structural', 'display', 'inline'):
        return "AM-GM Inequality"

    # --- Seeley-DeWitt a_0 ---
    if re.search(r'a_0\s*=\s*.*4pi.*Vol', raw) or \
       re.search(r'a_0\s*=\s*2\^\{?\[?d/2\]?\}?', raw):
        return "Seeley-DeWitt a_0 Coefficient"

    # --- Penrose ---
    if re.search(r'penrose', combined) and eq_type in ('structural', 'display', 'inline'):
        if 'diagram' in combined:
            return "Penrose Diagram"
        if 'conformal' in combined and 'cyclic' in combined:
            return "Conformal Cyclic Cosmology (CCC)"

    # --- Kaluza-Klein ---
    if re.search(r'kaluza.?klein', combined) and eq_type in ('structural', 'display', 'inline'):
        if 'ansatz' in combined or 'metric' in combined:
            return "Kaluza-Klein Metric Ansatz"
        return "Kaluza-Klein Theory"

    # --- Generalized Entropy ---
    if re.search(r'generalized.*entropy', combined) and eq_type in ('structural', 'display', 'inline'):
        return "Generalized Entropy"

    # --- Internal/External Temperature ---
    if re.search(r'T_\{?internal\}?\s*=', raw) and ('planck' in combined or 'T_Pl' in raw):
        return "Internal Temperature (Planck Scale)"
    if re.search(r'T_\{?external\}?\s*=', raw) and 'H/' in raw:
        return "External Temperature (Hubble)"

    # --- Spinodal ---
    if re.search(r'spinodal', raw_lower) and eq_type in ('structural', 'display', 'inline'):
        return "No-Spinodal Condition"
    if re.search(r"V''.*>\s*0", raw) and 'everywhere' in combined:
        return "No-Spinodal Condition"

    # --- Impedance Mismatch ---
    if re.search(r'impedance.*mismatch', combined) and eq_type in ('structural', 'display', 'inline'):
        return "Impedance Mismatch"

    # --- Mode Coincidence ---
    if re.search(r'coincidence.*condition', combined) and re.search(r'lambda.*=.*lambda', raw):
        return "Mode Coincidence Condition"

    # --- Biharmonic ---
    if re.search(r'nabla\^4.*=.*lambda', raw):
        return "Biharmonic Eigenvalue Equation"

    # --- Second Variation ---
    if re.search(r'second.*variation', combined) and eq_type in ('structural', 'display', 'inline'):
        if 'einstein' in combined or 'I_h' in raw:
            return "Second Variation (Einstein-Hilbert)"
        return "Second Variation"

    # --- Gap-Edge Separation ---
    if re.search(r'gap.*edge', combined) and re.search(r'4/9|5/6', raw):
        if eq_type in ('structural', 'display', 'inline'):
            return "Gap-Edge Separation (Algebraic)"

    # --- V_IR ---
    if re.search(r'V_\{?IR\}?', raw) and eq_type in ('structural', 'display', 'inline'):
        return "IR Potential V_IR"

    # --- T''(0) gate ---
    if re.search(r"T''.*\(0\)", raw) and eq_type in ('structural', 'display', 'inline'):
        return "T''(0) Gate Condition"

    # --- Signed spectral sums ---
    if re.search(r'S_signed', raw) and eq_type in ('structural', 'display', 'inline'):
        return "Signed Spectral Sum"

    # --- Fiber dimension ---
    if re.search(r'fiber.*dimension', combined) and re.search(r'44|16|27', raw):
        if eq_type in ('structural', 'display', 'inline'):
            return "Fiber Dimension Count"

    # --- Convergence rate ---
    if re.search(r"T'\s*\(\s*tau_0\s*\)", raw) and 'convergence' in combined:
        return "Convergence Rate at Fixed Point"

    # =========================================================================
    # TIER 3: Source-file heuristics
    # =========================================================================

    # Baptista equation numbers
    if 'baptista' in source.lower() and eq_type in ('structural', 'display', 'inline', 'comment'):
        if re.search(r'eq\s*\(?3\.14\)?', combined):
            return "Baptista Eq 3.14 (TT Second Variation)"
        if re.search(r'eq\s*\(?3\.16\)?', combined):
            return "Baptista Eq 3.16 (TT Mode Decomposition)"
        if re.search(r'eq\s*\(?3\.17\)?', combined):
            return "Baptista Eq 3.17 (KK Mass Formula)"
        if re.search(r'eq\s*\(?3\.66\)?', combined):
            return "Baptista Eq 3.66 (Ricci on Jensen SU(3))"
        if re.search(r'eq\s*\(?3\.68\)?', combined):
            return "Baptista Eq 3.68 (Jensen Metric)"
        if re.search(r'eq\s*\(?3\.70\)?', combined):
            return "Baptista Eq 3.70 (Scalar Curvature)"
        if re.search(r'eq\s*\(?3\.80\)?', combined):
            return "Baptista Eq 3.80 (Two-Field Potential)"
        if re.search(r'eq\s*\(?3\.87\)?', combined):
            return "Baptista Eq 3.87 (Effective Potential)"

    # Connes papers
    if 'connes' in source.lower() and eq_type in ('structural', 'display', 'inline'):
        if re.search(r'spectral\s*action', combined):
            return "Spectral Action (Connes)"
        if re.search(r'noncommutative', combined):
            return "NCG Framework (Connes)"

    # --- Volovik ---
    if 'volovik' in combined and eq_type in ('structural', 'display', 'inline'):
        return "Volovik Vacuum Energy"

    # --- CDT ---
    if re.search(r'CDT', raw) and eq_type in ('structural', 'display', 'inline'):
        return "CDT Spectral Dimension"

    # --- Boson-Fermion cancellation ---
    if re.search(r'sum.*boson.*sum.*fermion', raw) and re.search(r'=\s*0', raw):
        return "Boson-Fermion Cancellation"

    # --- Clifford algebra ---
    if re.search(r'clifford', combined) and eq_type in ('structural', 'display', 'inline', 'comment'):
        if 'algebra' in combined or 'relation' in combined:
            return "Clifford Algebra"

    # --- Specific tagged equations ---
    if tag:
        if tag == 'E-3':
            return "Clock Constraint (E-3)"
        if tag == 'A2.1':
            return "Sigma Mass Definition (A2.1)"
        if tag == 'A2.2':
            return "Modulus Oscillation Equation (A2.2)"
        if tag == 'A2.3':
            return "Clock Violation Bound (A2.3)"
        if tag == 'A2.4':
            return "Sigma Mass Lower Bound (A2.4)"
        if tag == 'A2.5':
            return "BBN Mass Bound (A2.5)"
        if tag == 'A2.6':
            return "Thermal Clock Bound (A2.6)"
        if tag == '06.B':
            return "Proper Time (GR)"
        if tag == 'A3.1':
            return "Modular Flow (KMS State)"
        if tag == 'A3.2':
            return "Modular-Proper Time Relation"
        if re.search(r'A\.46', tag):
            return "KO-Dimension Signs"
        if re.search(r'^A\.3$', tag):
            return "KMS State"
        # Connes modular flow appendix tags
        if tag == 'A.1':
            return "KMS Condition"
        if tag == 'A.4':
            return "Density Matrix (Spectral)"
        if tag == 'A.5':
            return "Modular Operator"
        if tag == 'A.10':
            return "Modular Tick Definition"
        if tag == 'A.11':
            return "Self-Consistency Map"
        if tag == 'A.13':
            return "Self-Consistency Map (Gradient)"
        if tag == 'A.16':
            return "Tick Equation (Seeley-DeWitt)"
        if tag == 'A.18':
            return "Convergence Rate at Fixed Point"
        if tag == 'A.20':
            return "Effective Inverse Temperature"
        if tag == 'A.22':
            return "Cayley-Dickson Construction"
        if tag == 'A.23':
            return "Cayley-Dickson Multiplication"
        if tag == 'A.24':
            return "Tomita-Takesaki Doubling"
        if tag == 'A.27':
            return "Modular Tick Equation"
        if tag == 'A.28':
            return "Density Matrix (Spectral)"
        if tag == 'A.29':
            return "Partition Function (Spectral)"
        if tag == 'A.30':
            return "Cutoff Scaling"
        if tag == 'A.31':
            return "Step Size Scaling"
        if tag == 'A.32':
            return "Fixed Point Condition"
        if tag == 'A.36':
            return "Modular Tick Period"
        if tag == 'A.37':
            return "Modular Tick Period (Planck Units)"
        if tag == 'A.38':
            return "Convergence Rate at Fixed Point"
        if tag == 'A.40':
            return "Relaxation Time (Modular Ticks)"
        if tag == 'A.41':
            return "Convergence Rate (Mass Form)"
        if tag == 'A.44':
            return "Spectral Entropy"
        if tag == 'A.48':
            return "Modular Tick Equation (Simplest Form)"
        if tag == '*' and re.search(r'tau_\{n\+1\}', raw):
            return "Fixed Point Iteration"

    # --- KMS Condition ---
    if re.search(r'KMS', combined) and eq_type in ('structural', 'display', 'inline'):
        if 'condition' in combined or 'state' in combined:
            return "KMS Condition"

    # --- Cayley-Dickson ---
    if re.search(r'cayley.?dickson', combined) and eq_type in ('structural', 'display', 'inline'):
        return "Cayley-Dickson Construction"

    # --- Tomita-Takesaki ---
    if re.search(r'tomita.?takesaki', combined) and eq_type in ('structural', 'display', 'inline'):
        return "Tomita-Takesaki Modular Theory"

    # --- Algebra Expansion (Cayley-Dickson tower) ---
    if re.search(r'\\mathcal\{A\}_\d\s*=\s*\\mathbb', raw) and 'tick' in combined:
        return "Algebra Expansion (Cayley-Dickson Tower)"

    # --- Modulus Energy Density Fraction ---
    if re.search(r'\\Omega_\\tau', raw) or re.search(r'Omega_tau', raw):
        if re.search(r'rho.*H\^2', raw) or 'energy density' in combined:
            return "Modulus Energy Density Fraction"

    # --- Bott Periodicity ---
    if re.search(r'bott\s*periodicity', combined) and eq_type in ('structural', 'display', 'inline'):
        return "Bott Periodicity"

    # --- Exceptional Jordan Algebra ---
    if re.search(r'J_3\(.*O\)', raw) or re.search(r'jordan\s*algebra', combined):
        if eq_type in ('structural', 'display', 'inline'):
            return "Exceptional Jordan Algebra"

    # --- G_2 Automorphism ---
    if re.search(r'Aut\(.*O\).*G_2', raw) or re.search(r'G_2.*exceptional', combined):
        if eq_type in ('structural', 'display', 'inline'):
            return "G_2 Automorphism of Octonions"

    # --- Internal Dirac Operator ---
    if re.search(r'D_K\s*=\s*.*sum.*e_a.*nabla', raw) or \
       re.search(r'D_K\s*=\s*\\sum.*e_a.*\\nabla', latex):
        return "Internal Dirac Operator"
    if re.search(r'D_\{?\(p,q\)\}?\s*=\s*sum.*E', raw) or \
       re.search(r'D_K\s*=\s*bigoplus', raw):
        return "Internal Dirac Operator (Peter-Weyl)"

    # --- One-Loop Effective Action ---
    if re.search(r'Gamma_\{?1loop\}?\s*=', raw) or \
       re.search(r'one.?loop.*effective\s*action', combined):
        return "One-Loop Effective Action"

    # --- Spectral Entropy ---
    if re.search(r'S_spectral|spectral.*entropy', combined) and eq_type in ('structural', 'display', 'inline'):
        return "Spectral Entropy"

    # --- 4D Lagrangian ---
    if re.search(r'L_\{?4D\}?\s*=', raw) and eq_type in ('structural', 'display', 'inline'):
        return "4D KK Lagrangian"

    # --- Scalar Curvature Formula ---
    if re.search(r'R\(s\)\s*=\s*.*e\^\{?-4s', raw) or \
       re.search(r'R\(s\)\s*=\s*-\(1/4\)e\^\{-4s\}', raw):
        return "Scalar Curvature R(s)"

    # --- Volume Metric ---
    if re.search(r'G_\{?tau.*tau\}?\s*=\s*5', raw) or \
       re.search(r'G_\{\\tau\\tau\}\s*=\s*5', latex):
        return "Modulus Kinetic Metric"

    # --- Modulus Rolling Equation ---
    if re.search(r'\\ddot\{\\tau\}.*3H.*\\dot\{\\tau\}.*V\'', latex) or \
       re.search(r'ddot.*tau.*3H.*dot.*tau.*V\'', raw):
        return "Modulus Rolling Equation"
    if re.search(r'\\ddot\{\\tau\}.*3H\\dot\{\\tau\}.*V\'\(\\tau\)', latex):
        return "Modulus Rolling Equation"

    # --- Friedmann with Modulus ---
    if re.search(r'H\^2\s*=.*M_\{?\\?rm\s*Pl\}?.*G_\{?\\?tau', raw) or \
       re.search(r'H\^2\s*=\s*\\frac\{1\}\{3M', latex):
        return "Friedmann Equation (with Modulus)"

    # --- Fine Structure Constant ---
    if re.search(r'alpha_\{?\\?rm\s*FS\}?', raw) or \
       re.search(r'\\alpha_\{\\rm FS\}', latex):
        if 'variation' in combined or 'dot' in combined or 'rolling' in combined:
            return "Fine Structure Constant Variation"
        if eq_type in ('structural', 'display', 'inline'):
            return "Fine Structure Constant"

    # --- Gauge Coupling Tau-Dependence ---
    if re.search(r'\\partial.*ln\s*g_[12].*\\partial.*\\tau', latex):
        return "Gauge Coupling Tau-Dependence"

    # --- Bayesian Update ---
    if re.search(r'p_\{?\\?rm\s*final\}?\s*=\s*\\?sigma', raw) or \
       re.search(r'BF_i|bayes.*factor', combined):
        if eq_type in ('structural', 'display', 'inline'):
            return "Bayesian Update Formula"

    # --- Density of States ---
    if re.search(r'density\s*of\s*states', combined) and eq_type in ('structural', 'display', 'inline'):
        if re.search(r'N\(E\)', raw) or re.search(r'DOS', raw):
            return "Density of States"

    # --- Opposite Algebra ---
    if re.search(r'pi\^o\(a\)\s*=\s*J\s*pi\(a\*\)\s*J', raw):
        return "Opposite Algebra (Real Structure)"

    # --- Total Dirac Operator (Product) ---
    if re.search(r'D_P\(', raw) and ('tensor' in raw or 'gamma_5' in raw):
        return "Total Dirac Operator (Product Geometry)"

    # --- Mass Matrix ---
    if re.search(r'M_\{?alpha.*beta\}?\s*=.*D_K', raw) or \
       re.search(r'mass\s*matrix', combined):
        if eq_type in ('structural', 'display', 'inline'):
            return "Mass Matrix (KK)"

    # --- Z3 Triality ---
    if re.search(r'Z_?3', raw) and ('triality' in combined or 'generation' in combined):
        if eq_type in ('structural', 'display', 'inline'):
            return "Z_3 Triality"
    if re.search(r'rho_\{?\(p,q\)\}?\(zeta\)\s*=\s*omega', raw):
        return "Z_3 Action on Irrep"

    # --- Spin Connection ---
    if re.search(r'S_a\s*=.*sum.*f_\{?abc\}?.*gamma', raw) or \
       re.search(r'spin\s*connection', combined):
        if eq_type in ('structural', 'display', 'inline'):
            return "Spin Connection Generators"

    # --- Spectral Action Expansion (general) ---
    if re.search(r'S\(.*\)\s*=\s*.*sum.*f_\d.*a_\d', raw) or \
       re.search(r'spectral\s*action.*expansion', combined):
        if eq_type in ('structural', 'display', 'inline'):
            return "Spectral Action Asymptotic Expansion"

    # --- C^2 Boson Mass ---
    if re.search(r'm_C2\^2', raw) or re.search(r'C\^2.*boson.*mass', combined):
        if eq_type in ('structural', 'display', 'inline'):
            return "C^2 Boson Mass"

    # --- Tree-Level Potential ---
    if re.search(r'V_tree', raw) and re.search(r'=.*baptista|=.*R_bracket|=.*C_tree', raw):
        if eq_type in ('structural', 'display', 'inline'):
            return "Tree-Level Potential"

    # --- SU(2) Casimir ---
    if re.search(r'C2_SU2', raw) or re.search(r'C_2.*SU\(2\)', raw):
        if eq_type in ('structural', 'display', 'inline'):
            return "SU(2) Casimir Operator"

    # --- Hypercharge ---
    if re.search(r'Y_total\s*=', raw) and ('hypercharge' in combined or 'Y_rep' in raw):
        if eq_type in ('structural', 'display', 'inline'):
            return "Total Hypercharge Operator"

    # --- KO-Dimension Signs for Display ---
    if re.search(r'J\^2\s*=\s*\+\\mathbb\{I\}', raw) and re.search(r'J.*D_K.*=.*D_K.*J', raw):
        return "KO-Dimension Signs (J, D, gamma)"
    if re.search(r'J\^2\s*=\s*\+1.*JD\s*=\s*DJ', raw):
        return "KO-Dimension Signs (J, D, gamma)"

    # --- R(s)/R(0) formula ---
    if re.search(r'R\(s\)/R\(0\)\s*=|\\frac\{R\(s\)\}\{R\(0\)\}', raw):
        return "Normalized Scalar Curvature"

    # --- Mean-field exactness ---
    if re.search(r'd_int.*>.*d_uc', raw) and eq_type in ('structural', 'display', 'inline', 'comment'):
        return "Upper Critical Dimension (Mean-Field Exact)"

    # --- Scalar curvature at s=0 ---
    if re.search(r'R\s*\(\s*tau\s*\)\s*=\s*9\.92', raw):
        return "Scalar Curvature at tau=0"

    # --- R''(0) = 0 ---
    if re.search(r"R''\(0\)\s*=\s*0", raw):
        return "Curvature Second Derivative at Round Point"

    # --- Phonon ---
    if re.search(r'phonon', combined) and eq_type in ('structural', 'display', 'inline'):
        return "Phonon Mode"

    # --- Born Rule ---
    if re.search(r'born\s*rule', combined) and eq_type in ('structural', 'display', 'inline'):
        return "Born Rule"

    # Nothing matched
    return None


def main():
    index_path = Path("tools/knowledge-index.json")
    print(f"Loading {index_path}...")
    data = load_index(index_path)

    equations = data.get('equations', [])
    print(f"Total equations: {len(equations)}")

    named_count = 0
    name_counts = {}
    type_name_counts = {}

    for eq in equations:
        name = classify_equation(eq)
        if name:
            eq['name'] = name
            named_count += 1
            name_counts[name] = name_counts.get(name, 0) + 1
            t = eq.get('type', 'unknown')
            type_name_counts[t] = type_name_counts.get(t, 0) + 1
        else:
            eq['name'] = None

    print(f"\nNamed: {named_count} / {len(equations)} ({100*named_count/len(equations):.1f}%)")
    print(f"Distinct names: {len(name_counts)}")

    print(f"\nBy equation type:")
    for t, c in sorted(type_name_counts.items(), key=lambda x: -x[1]):
        total = sum(1 for eq in equations if eq.get('type') == t)
        print(f"  {t}: {c}/{total} named ({100*c/total:.1f}%)")

    # Print name distribution
    print(f"\n{'Name':<55s} {'Count':>5s}")
    print("-" * 62)
    for name, count in sorted(name_counts.items(), key=lambda x: -x[1]):
        print(f"  {name:<53s} {count:>5d}")

    # Save
    print(f"\nSaving to {index_path}...")
    save_index(data, index_path)
    print("Done.")


if __name__ == '__main__':
    main()
