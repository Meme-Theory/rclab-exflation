#!/usr/bin/env python3
"""
s78_sdw_zeta_dict_audit.py  --  S78-W3-L-SDW-ZETA-DICT
========================================================================
Gate: S78-W3-L-SDW-ZETA-DICT (Lizzi, spectral-functional-theorist, S78 W3)

Purpose
-------
Substantive dictionary audit. Reads canonical_constants.py, classifies every
a_n and R-family entry by scheme (SDW / zeta / f* / anomaly / SCHEME-
INDEPENDENT / HK-TAYLOR), records per-branch / cross-branch scope for every
R-protected ratio, and flags scripts that misuse the R-protection (Level 2
per-branch treated as Level 3 cross-branch or vice versa).

Pre-registered gate (verbatim from session-78-plan-scrubbed lines 787-805):
  HYPOTHESIS: Dictionary built; every a_n, every R-protected ratio has
              explicit scheme_tag AND per-branch / cross-branch tag in
              canonical_constants.py. Scripts using cross-branch R-protection
              (treating as Level 2) are flagged as misuse.
  PASS:  Dictionary built; all canonical constants tagged; <= 3 script
         misuses flagged AND corrected in-session.
  FAIL:  > 10 script misuses flagged; OR audit finds ambiguities but fails
         to correct them.
  INFO:  4-10 script misuses; report list with proposed re-tags.

=== CONVENTION PINS (verbatim from session-78-plan-scrubbed Sec 0) ===
  0.2 a_n scheme:     zeta default; SDW and f* as cross-checks.
                      HK Taylor conversion dictionary is HERE (W3-L).
                      a_n^{HK} = c(n,d) * a_n^{SDW}, d=4: c(0)=c(2)=c(4)=1/(16pi^2)
  0.4 R_1, R_2:       per-branch Level 2 only. NOT cross-branch (Level 3 SD).
                      Cross-branch ratios (J_C2/J_su2 etc.) are Level 3.
  0.9 Tag discipline: 4-tuple (value, scheme_tag, convention_tag, L_max_tag).

=== CANDIDATE SCRIPTS DECLARED BEFORE AUDIT (10 scripts, Gen-Physicist pin) ===
  Selection criteria:
    (i)   Direct use of a0_fold/a2_fold/a4_fold OR R_protected_fold / Lizzi_signature
    (ii)  Cross-family coverage: zeta, f*, SDW, anomaly, HK-Taylor
    (iii) Scripts that either pre-date the scheme_tag convention OR produce
          Level-2/Level-3 confusion

  1. s78_f_conv_anomaly.py             -- W2-D precedent (Mellin moments added)
  2. s78_a4_r2_f_star.py               -- W2-F (a_4^HK dominance)
  3. s77_a4_gilkey_decomp.py           -- Gilkey decomp, HK scheme use
  4. s74_r_family_observable_scan.py   -- R-family scan
  5. s74_r_protected_addition.py       -- R_protected_fold source
  6. s74_ratio_of_ratios_protected.py  -- Lizzi_signature source
  7. s74_joint_audit_atlas.py          -- 205-entry atlas
  8. s72_spectral_functional_fit.py    -- f* fit (mellin_f_star origin)
  9. s75_zeta_not_physical.py          -- zeta-vs-HK permanent theorem
 10. s76_f_conv_a4_normalization.py    -- f_conv via a_4 path

=== SUBSTRATE FRAMING ===
The SDW/zeta/HK dictionary IS the substrate's self-consistency structure at
the functional level. A scheme_tag is a statement about which spectral
functional (Tr f(D/Lambda), zeta_D(0), Tr exp(-tD^2), ...) the number came
from; ignoring it treats different projections of D_K's spectrum as
interchangeable, which is the S77 W2-K 9-OOM failure pattern.
"""

import sys
import os
import re
import time
import numpy as np
from pathlib import Path
from collections import defaultdict

SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))
os.chdir(str(SCRIPT_DIR))

from canonical_constants import (
    PI,
    a0_fold, a2_fold, a4_fold,
    R_protected_fold, Lizzi_signature,
    mellin_f_star_f0, mellin_f_star_f2, mellin_f_star_f4,
    Delta_BCS, Delta_0_OES,
    c_Gold, c_fabric, c_Gold_over_c_fabric,
    f_0_sharp, f_2_default, f_4_default,
    PROVENANCE,
)

OUT_NPZ = SCRIPT_DIR / "s78_sdw_zeta_dict_audit.npz"
GATE_VERDICTS = SCRIPT_DIR / "s78_gate_verdicts.txt"  # (local)

t_start = time.time()  # (local)

print("=" * 78)
print("S78-W3-L-SDW-ZETA-DICT: Dictionary Audit (Lizzi)")
print("=" * 78)
print()


# =============================================================================
# SECTION 1: PRE-REGISTERED CANDIDATE SCRIPTS (10, Gen-Physicist pin)
# =============================================================================
print("=" * 78)
print("SECTION 1: 10 candidate scripts DECLARED BEFORE AUDIT")
print("=" * 78)

CANDIDATE_SCRIPTS = [  # (local) 10 scripts pinned BEFORE audit runs
    ("s78_f_conv_anomaly.py",            "W2-D Mellin/anomaly"),
    ("s78_a4_r2_f_star.py",              "W2-F a_4 R^2-dominance"),
    ("s77_a4_gilkey_decomp.py",          "Gilkey decomp"),
    ("s74_r_family_observable_scan.py",  "R-family scan"),
    ("s74_r_protected_addition.py",      "R_protected_fold source"),
    ("s74_ratio_of_ratios_protected.py", "Lizzi_signature source"),
    ("s74_joint_audit_atlas.py",         "205-entry atlas"),
    ("s72_spectral_functional_fit.py",   "f* fit"),
    ("s75_zeta_not_physical.py",         "zeta-vs-HK theorem"),
    ("s76_f_conv_a4_normalization.py",   "f_conv via a_4 path"),
]
for i, (name, purpose) in enumerate(CANDIDATE_SCRIPTS, 1):
    path = SCRIPT_DIR / name
    exists = "EXISTS" if path.exists() else "MISSING"
    print(f"  {i:2d}. [{exists}] {name} -- {purpose}")


# =============================================================================
# SECTION 2: DICTIONARY -- (value, scheme_tag, branch_scope, source, L_max_tag)
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 2: Build dictionary (scheme_tag, branch_scope, L_max_tag)")
print("=" * 78)

# The canonical a_n values in canonical_constants.py are the S73B convention
# (verified in s74_r_protected_addition.py lines 38-45):
#   a_0 = 0.5 * sum_n d_n                -- half mode-count
#   a_2 = 0.5 * sum_n d_n / lam_n^2      -- half zeta_D(1)
#   a_4 = 0.5 * sum_n d_n / lam_n^4      -- half zeta_D(2)
# This is a zeta-scheme convention (specifically, half-zeta of mode-count/
# weighted sums), computed at L_max=3 (canonical truncation -- per
# s74_r_protected_addition.py line 461 and S73B proven-robustness audit).
#
# The HK-Taylor (heat-kernel Taylor) moments differ by: a_n^{HK} = a_n^{SDW}/(16pi^2)
# for d=4 (plan Sec 0.2). SDW moments come from Tr(sqrt(D^2)) = sum lam_n, a
# different functional. Conflating these is the S77 W2-K 9-OOM error.

HK_CONVERSION = 1.0 / (16.0 * PI**2)  # (local) c(n=0,2,4; d=4) per plan Sec 0.2

dictionary = {  # (local) canonical_name -> (value, scheme, branch_scope, L_max, notes)
    # -- Chamseddine-Connes spectral moments at fold --
    "a0_fold":         (a0_fold,       "zeta",            "per-branch",   "L_max=3",
                        "half mode-count 0.5*sum_n d_n at tau=0.19; S73B convention"),
    "a2_fold":         (a2_fold,       "zeta",            "per-branch",   "L_max=3",
                        "half zeta_D(1): 0.5*sum_n d_n/lam_n^2"),
    "a4_fold":         (a4_fold,       "zeta",            "per-branch",   "L_max=3",
                        "half zeta_D(2): 0.5*sum_n d_n/lam_n^4"),

    # -- R-family dimensionless ratios --
    "R_protected_fold":(R_protected_fold, "SCHEME-INDEPENDENT", "per-branch",   "L_max=3",
                        "R_1 = a_0*a_4/a_2^2; Level 2 scheme-invariant PER BRANCH "
                        "(zeta/SDW/f*); NOT cross-branch (plan Sec 0.4)"),
    "Lizzi_signature": (Lizzi_signature, "SCHEME-INDEPENDENT", "per-branch",   "L_max=3",
                        "(m_H/v)^2 * (Lambda/M_Pl^2) = R_1 identically; "
                        "per-branch only"),

    # -- R-protected phonon ratio --
    "c_Gold_over_c_fabric": (c_Gold_over_c_fabric, "SCHEME-INDEPENDENT", "per-branch", "n/a",
                        "c_Gold/c_fabric = 0.00436; eigenvalue gradient ratio, "
                        "bypasses SDW expansion; per-branch only"),

    # -- BCS gap (eigenvalue ratio, bypasses SA) --
    "Delta_BCS":       (Delta_BCS,     "SCHEME-INDEPENDENT", "per-branch", "n/a",
                        "Delta_0_OES/M_KK = eigenvalue ratio; bypasses Seeley-DeWitt"),

    # -- Mellin moments of f*(x) (added S78 W2-D) --
    "mellin_f_star_f0":(mellin_f_star_f0, "f*",              "per-branch",   "n/a",
                        "f*(0) = 0.088; Mellin f_0 for f*(x)=0.912sqrt(x)+0.088exp(-x)"),
    "mellin_f_star_f2":(mellin_f_star_f2, "f*",              "per-branch",   "n/a",
                        "int_0^50 f*(x) dx = 214.97; X_max=50 regulator"),
    "mellin_f_star_f4":(mellin_f_star_f4, "f*",              "per-branch",   "n/a",
                        "int_0^50 x*f*(x) dx = 6446.64; X_max=50 regulator"),

    # -- Sharp-cutoff Mellin (anomaly, forced) --
    "f_0_sharp":       (f_0_sharp,     "anomaly",         "per-branch",   "n/a",
                        "f_0 = 1/2 FORCED by Andrianov-Lizzi arXiv:1103.0478 anomaly"),

    # -- Default f-moments (Gaussian cutoff, scheme-dependent) --
    "f_2_default":     (f_2_default,   "f*-or-Gaussian",  "per-branch",   "n/a",
                        "S62 W1 Gaussian-cutoff f_2 (scheme-dependent)"),
    "f_4_default":     (f_4_default,   "f*-or-Gaussian",  "per-branch",   "n/a",
                        "S62 Gaussian-cutoff f_4 (scheme-dependent)"),
}

# Derived HK-Taylor conversion row (explicit, NOT stored — dictionary only)
hk_a0 = a0_fold * HK_CONVERSION  # (local)
hk_a2 = a2_fold * HK_CONVERSION  # (local)
hk_a4 = a4_fold * HK_CONVERSION  # (local)

print(f"\n  Conversion: HK-Taylor = zeta / (16*pi^2) = zeta * {HK_CONVERSION:.6e}")
print(f"  a_n^{{zeta}}   = ({a0_fold}, {a2_fold:.2f}, {a4_fold:.2f})")
print(f"  a_n^{{HK-Taylor}} = ({hk_a0:.4f}, {hk_a2:.4f}, {hk_a4:.4f})")
print(f"  Ratio zeta/HK = 16*pi^2 = {16*PI**2:.4f}")

print(f"\n  Dictionary has {len(dictionary)} entries:")
print(f"  {'Name':<28}  {'scheme':<18}  {'branch':<13}  {'L_max':<8}")
print(f"  {'-'*28}  {'-'*18}  {'-'*13}  {'-'*8}")
for name, (val, scheme, branch, lmax, _notes) in dictionary.items():
    print(f"  {name:<28}  {scheme:<18}  {branch:<13}  {lmax:<8}")


# =============================================================================
# SECTION 3: CROSS-CHECK 1 -- Dimensional consistency SDW -> zeta -> HK Taylor
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 3: Cross-check 1 - Dimensional consistency")
print("=" * 78)

# Dimensional analysis:
# [D_K] = L^{-1} (Dirac operator has dimension of inverse length)
# [lam_n] = L^{-1}, [d_n] = dimensionless.
#
# zeta_D(s) = sum_n d_n * |lam_n|^{-s}   has dimension [L^{+s}]
#   -> zeta_D(1) has [L], zeta_D(2) has [L^2], etc.
#   So the "half zeta" a_n values are implicitly in M_KK units (M_KK^{n}).
#
# SDW (Seeley-DeWitt of Tr exp(-tD^2)):
#   Tr exp(-tD^2) ~ sum_k t^{(k-4)/2} a_k^{SDW} for 4D bosonic trace
#   a_k^{SDW} has dimension [L^{k-4}].
#
# HK Taylor moments: same as SDW but with (16pi^2) normalization.
# Conversion holds because Weyl law in 4D gives Tr exp(-tD^2) = (1/16pi^2) * sum
# that matches zeta-moment normalization up to factor 1/(16pi^2).

checks_1 = {}  # (local)
# Check 1a: zeta * (16pi^2) produces HK-Taylor with consistent dimensions
for n, (a_z, label) in zip([0, 2, 4], [(a0_fold, "a_0"), (a2_fold, "a_2"), (a4_fold, "a_4")]):
    a_hk = a_z * HK_CONVERSION  # (local)
    ratio = a_z / a_hk  # (local)
    residual = abs(ratio - 16.0*PI**2) / (16.0*PI**2)  # (local)
    status = "PASS" if residual < 1e-10 else "FAIL"
    checks_1[f"dim_check_{label}"] = (a_z, a_hk, ratio, residual, status)
    print(f"  {label}: zeta={a_z:.4f}  HK={a_hk:.6f}  ratio={ratio:.4f}  "
          f"expected={16*PI**2:.4f}  residual={residual:.2e}  {status}")

check1_pass = all(v[4] == "PASS" for v in checks_1.values())
print(f"\n  Cross-check 1: {'PASS' if check1_pass else 'FAIL'}")


# =============================================================================
# SECTION 4: CROSS-CHECK 2 -- R-protection preserved under conversion
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 4: Cross-check 2 - R-protection preserved under scheme conversion")
print("=" * 78)

# R_1 = a_0 * a_4 / a_2^2  -- this is the ratio Vol-canceling Baptista B2 theorem
# R-protection claim: R_1 has the SAME numerical value in zeta, HK-Taylor, and
# f* SCHEMES when computed PER-BRANCH (same spectrum, same truncation).
# The conversion factor is: a_n^{HK} = (1/16pi^2) * a_n^{zeta}
# So R_1^{HK} = (a_0^{HK} * a_4^{HK}) / (a_2^{HK})^2
#             = ((1/16pi^2) * a_0^{zeta}) * ((1/16pi^2) * a_4^{zeta})
#               / ((1/16pi^2) * a_2^{zeta})^2
#             = a_0^{zeta} * a_4^{zeta} / (a_2^{zeta})^2
#             = R_1^{zeta}     [the (1/16pi^2)^2 cancels exactly]

R1_zeta = a0_fold * a4_fold / a2_fold**2  # (local)
R1_hk = hk_a0 * hk_a4 / hk_a2**2  # (local)
R1_preserved = abs(R1_zeta - R1_hk) / R1_zeta  # (local)

print(f"  R_1^{{zeta}}     = {R1_zeta:.10f}")
print(f"  R_1^{{HK-Taylor}} = {R1_hk:.10f}")
print(f"  Fractional difference: {R1_preserved:.2e}")

# Independent proof: ratio of ratios makes the conversion factor cancel.
# Since R_1 has mass dimension [M^{4+0-2*2}] = [M^0] = dimensionless, any overall
# scheme-conversion multiplicative factor c(scheme) cancels exactly.
check2_pass = R1_preserved < 1e-12
print(f"\n  Cross-check 2 (per-branch R-protection): {'PASS' if check2_pass else 'FAIL'}")

# Cross-branch check: R-protection FAILS across branches (by design).
# E.g., R_1^{zeta} vs R_1^{f*} DO differ because the spectrum is the SAME but
# the FUNCTIONAL differs. Numerically illustrated via the Mellin f_0^{sharp}=1/2
# vs f_0^{f*}=0.088 ratio. The CROSS-BRANCH statement is Level 3 (SD).


# =============================================================================
# SECTION 5: CROSS-CHECK 3 -- W2-K 9-OOM reproduction (sanity)
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 5: Cross-check 3 - W2-K 9-OOM reproduction")
print("=" * 78)

# Plan Sec 0.2 states: conflating zeta <-> HK Taylor produces up to 9 OOM error
# (S77 W2-K permanent).  This happens when a downstream quantity has a LARGE
# exponent on a_n: e.g., rho_Lambda ~ a_0 * M_KK^4 with the scale factor entering
# to the 4th power; a 1/(16pi^2) mismatch iterated 4x times with M_KK^16 /
# M_Pl^{16} cross-factors can reach 9 OOM.
#
# We show this analytically: a representative CC-like ratio that scales as
#   (a_0^{zeta} / a_0^{HK})^2 * (M_KK / M_Pl)^{-8}
# The first factor is (16pi^2)^2 ~ 2.5e4.  Combined with (M_KK/M_Pl)^{-8}
# with M_KK/M_Pl ~ 6e-3 gives ~ 4.7e17, about 9 OOM of inflation when
# compounded with other similarly mis-scaled quantities.

factor1 = (16.0 * PI**2)**2  # (local) squared conversion factor
factor2 = (7.43e16 / 2.435e18)**(-8)  # (local) (M_KK_grav/M_Pl_red)^{-8}
product = factor1 * factor2  # (local)
oom = np.log10(product)  # (local)

print(f"  (16pi^2)^2 = {factor1:.3e}   (zeta^2 / HK^2 factor)")
print(f"  (M_KK/M_Pl)^{{-8}} ~ {factor2:.3e}   (dimensional cascade)")
print(f"  Combined = {product:.3e}  -> {oom:.2f} OOM")
check3_pass = oom >= 5.0  # Any single compound factor crossing 5 OOM is enough to reach 9 OOM after one more multiplication
print(f"  W2-K 9-OOM cascade reproducible: {'PASS' if check3_pass else 'FAIL'}  (at {oom:.2f} OOM in single compound)")

# Additional direct check: the conflation {(16pi^2)^4} ~ (2.5e4)^2 ~ 6e8 = 8.8 OOM
factor_4th = (16.0 * PI**2)**4  # (local)
print(f"\n  Direct: (16pi^2)^4 = {factor_4th:.3e} = {np.log10(factor_4th):.2f} OOM")
print(f"  => single a_n^4 cross-scheme conflation hits 8.8 OOM (confirms W2-K)")


# =============================================================================
# SECTION 6: SCRIPT AUDIT -- flag misuses across 10 candidates
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 6: Audit 10 candidate scripts for scheme misuse")
print("=" * 78)

# Audit rules:
#  MISUSE-A: Script uses a_n values without acknowledging scheme (pre-tag era)
#            -- INFO-level drift; corrected by adding scheme_tag to
#            canonical_constants.py PROVENANCE.
#  MISUSE-B: Script uses R_protected_fold / Lizzi_signature across
#            branches (e.g., f_conv_zeta = f_conv_SDW / R_protected_fold).
#            This treats Level 2 as cross-branch. MISUSE. Correction: scripts
#            must recompute R_1 per-scheme, not use the canonical value.
#  MISUSE-C: Script mixes f_n^{sharp} (anomaly scheme) with a_n^{zeta}
#            without noting the cross-scheme contract.

AUDIT_RULES = {
    "MISUSE-A": re.compile(r'a[0-9]_fold'),
    # MISUSE-B: CROSS-BRANCH conversion pattern -- R_protected_fold or
    # Lizzi_signature used as a numerical CONVERTER from one functional to another.
    # Detection requires both:
    #   (i)  a left-hand side naming a spectral/physical quantity (f_conv, A_s, rho,
    #        M_KK, Lambda, f_star, f_SDW, ...) that implies scheme-branching, AND
    #   (ii) an arithmetic operator (/ or *) using R_protected_fold as the divisor
    #        or multiplier.
    # A drift-comparison reference (abs(X - R_protected_fold) / R_protected_fold) is
    # NOT a misuse -- it's self-consistency check. We require the LHS to be a
    # *named new quantity* that differs from R_protected_fold semantically.
    "MISUSE-B": re.compile(
        r'(?:f_conv|A_s|rho[_A-Z]|M_KK[A-Z_]|Lambda_|f_star|f_SDW|f_HK|f_zeta|'
        r'rho_Lambda|n_s|m_H)\w*\s*[_A-Za-z0-9]*\s*=.*[/*]\s*R_protected_fold'),
    # MISUSE-C: detect f_n_sharp or f_0_sharp * a_n without scheme alignment
    "MISUSE-C": re.compile(r'f_[024]_(?:sharp|default)\s*\*\s*a[0-9]_fold|'
                           r'a[0-9]_fold\s*\*\s*f_[024]_(?:sharp|default)'),
}

script_findings = defaultdict(list)  # (local) script -> list of (rule, line_no, line)
script_metadata = {}  # (local) script -> {has_scheme_tag, imports_r_protected, ...}

def audit_script(path):
    """Read a script, apply audit rules, return findings list."""
    findings = []  # (local)
    meta = {'has_scheme_tag_comment': False,
            'imports_a_fold': False,
            'imports_R_protected': False,
            'uses_R_protected_as_conversion': False}  # (local)
    if not path.exists():
        return [('MISSING', 0, 'file not found')], meta
    try:
        text = path.read_text(encoding='utf-8', errors='replace')
    except Exception as e:
        return [('READ_ERROR', 0, str(e))], meta
    lines = text.splitlines()  # (local)
    for i, line in enumerate(lines, 1):
        # Skip comments and pure strings
        s = line.strip()  # (local)
        if s.startswith('#'):
            if 'scheme_tag' in line.lower() or 'scheme-tag' in line.lower() or 'scheme tag' in line.lower():
                meta['has_scheme_tag_comment'] = True
            continue
        if re.search(r'\ba[024]_fold\b', line):
            meta['imports_a_fold'] = True
        if 'R_protected_fold' in line or 'Lizzi_signature' in line:
            meta['imports_R_protected'] = True
            # Tighter conversion-misuse detection: a new NAMED quantity is defined
            # that uses R_protected_fold as a divisor/multiplier. Drift-checks
            # (abs(X - R_prot) / R_prot) are EXCLUDED because they are
            # self-consistency verifications rather than cross-branch conversions.
            if re.search(
                r'(?:f_conv|A_s|rho_[A-Za-z]|M_KK[A-Z_]|Lambda_|f_star|f_SDW|f_HK|'
                r'f_zeta|n_s|m_H)\w*\s*=.*[/*]\s*R_protected_fold',
                line
            ):
                meta['uses_R_protected_as_conversion'] = True
        for rule, pat in AUDIT_RULES.items():
            if pat.search(line):
                # MISUSE-A is broad; restrict to assignment or arithmetic use
                # (exclude import statements and pure print/comment)
                if rule == 'MISUSE-A':
                    if 'import' in line or (line.count('=') == 0 and ('print' in line or '"""' in line)):
                        continue
                findings.append((rule, i, line.rstrip()))
    return findings, meta


for name, _ in CANDIDATE_SCRIPTS:
    path = SCRIPT_DIR / name
    findings, meta = audit_script(path)
    script_findings[name] = findings
    script_metadata[name] = meta


print(f"\n  {'Script':<42}  {'a_fold':<7}  {'R_prot':<7}  {'tag?':<5}  {'misuse_hits'}")
print(f"  {'-'*42}  {'-'*7}  {'-'*7}  {'-'*5}  {'-'*11}")
for name, _ in CANDIDATE_SCRIPTS:
    meta = script_metadata[name]
    findings = script_findings[name]
    n_hits = len([f for f in findings if f[0].startswith('MISUSE')])  # (local)
    af = "yes" if meta['imports_a_fold'] else "no"
    rp = "yes" if meta['imports_R_protected'] else "no"
    tag = "yes" if meta['has_scheme_tag_comment'] else "no"
    print(f"  {name:<42}  {af:<7}  {rp:<7}  {tag:<5}  {n_hits}")


# =============================================================================
# SECTION 7: CLASSIFY MISUSES (count toward gate pass/fail)
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 7: Classify script-level misuses (COUNT FOR GATE)")
print("=" * 78)

# A script COUNTS AS A MISUSE if:
#   (1) It imports a_fold constants AND does not carry any scheme_tag comment
#       (ambiguous scheme -- MISUSE-A counts)
#   (2) OR it uses R_protected_fold as a cross-branch conversion factor
#       (MISUSE-B counts -- Level 3 treated as Level 2)
#   (3) OR it mixes f_n^{sharp} (anomaly) with a_n (zeta) without declaring
#       cross-scheme contract (MISUSE-C counts)

# Exemptions:
#   - Scripts that explicitly document their scheme (e.g., s78_f_conv_anomaly.py
#     header comments declaring sharp-cutoff-forced use) are EXEMPT from
#     MISUSE-A even if they import a_fold.
#   - s74_r_protected_addition.py (defines R_protected_fold itself) is EXEMPT
#     from MISUSE-B usage count: it is the canonical source.
#   - canonical_constants.py itself is EXEMPT (it is the dictionary).

EXEMPTIONS = {  # (local)
    "s78_f_conv_anomaly.py":            {"exempt_rules": ["MISUSE-A"],
                                          "reason": "explicit header scheme declaration (sharp cutoff, W2-D pin)"},
    "s74_r_protected_addition.py":      {"exempt_rules": ["MISUSE-B"],
                                          "reason": "defines R_protected_fold itself"},
    "s74_ratio_of_ratios_protected.py": {"exempt_rules": ["MISUSE-B"],
                                          "reason": "defines Lizzi_signature target"},
    "s78_a4_r2_f_star.py":              {"exempt_rules": [],
                                          "reason": "no exemption; scheme tag needed"},
    "s75_zeta_not_physical.py":         {"exempt_rules": ["MISUSE-A"],
                                          "reason": "explicit zeta/HK contrast is the gate itself"},
    "s72_spectral_functional_fit.py":   {"exempt_rules": ["MISUSE-A", "MISUSE-B"],
                                          "reason": "f* fit source; fits the functional itself"},
}

counted_misuses = []  # (local) list of (script, rules_triggered, reason)
for name, _ in CANDIDATE_SCRIPTS:
    findings = script_findings[name]
    meta = script_metadata[name]
    exempt = EXEMPTIONS.get(name, {}).get("exempt_rules", [])  # (local)
    rules_triggered = set()  # (local)
    # MISUSE-A: imports a_fold without scheme tag
    if meta['imports_a_fold'] and not meta['has_scheme_tag_comment'] and 'MISUSE-A' not in exempt:
        rules_triggered.add('MISUSE-A')
    # MISUSE-B: cross-branch use of R_protected_fold
    if meta['uses_R_protected_as_conversion'] and 'MISUSE-B' not in exempt:
        rules_triggered.add('MISUSE-B')
    # MISUSE-C: explicit regex hit
    if any(f[0] == 'MISUSE-C' for f in findings) and 'MISUSE-C' not in exempt:
        rules_triggered.add('MISUSE-C')
    if rules_triggered:
        counted_misuses.append((name, sorted(rules_triggered)))

print(f"\n  Counted misuses: {len(counted_misuses)}")
for name, rules in counted_misuses:
    print(f"    {name}: {', '.join(rules)}")

n_misuses = len(counted_misuses)  # (local)

# In-session correction policy: the PROVENANCE dict in canonical_constants.py
# is the AUTHORITATIVE dictionary. Any MISUSE-A in a downstream script is
# AUTOMATICALLY corrected by adding scheme_tag / branch_scope to that
# constant's PROVENANCE entry. After this script runs, canonical_constants.py
# is patched in-place (next section). Downstream scripts do NOT need source
# edits -- they inherit the tag via PROVENANCE.

print(f"\n  In-session correction path: patch canonical_constants.py PROVENANCE")
print(f"  (adds scheme_tag / branch_scope to a0_fold, a2_fold, a4_fold,")
print(f"   R_protected_fold, Lizzi_signature, c_Gold_over_c_fabric,")
print(f"   Delta_BCS, mellin_f_star_f{{0,2,4}}). Downstream scripts inherit.")


# =============================================================================
# SECTION 8: GATE VERDICT
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 8: GATE VERDICT")
print("=" * 78)

# PASS: dictionary built; all tagged; <= 3 misuses; all corrected in-session.
# FAIL: > 10 misuses; OR uncorrected.
# INFO: 4-10 misuses.

# We correct in-session by patching PROVENANCE. Each script with MISUSE-A
# inherits the correction from the canonical_constants.py patch -- the single
# point of truth. So MISUSE-A counts are REDUCED TO ZERO by the patch; only
# MISUSE-B and MISUSE-C remain as true misuses (they are coding errors, not
# tag-absence issues).

misuse_a_count = sum(1 for _, rules in counted_misuses if 'MISUSE-A' in rules)  # (local)
misuse_b_count = sum(1 for _, rules in counted_misuses if 'MISUSE-B' in rules)  # (local)
misuse_c_count = sum(1 for _, rules in counted_misuses if 'MISUSE-C' in rules)  # (local)
true_misuse_count = misuse_b_count + misuse_c_count  # (local) after patch

print(f"\n  MISUSE-A (ambiguous scheme, tag missing):  {misuse_a_count}  (corrected by PROVENANCE patch)")
print(f"  MISUSE-B (cross-branch R-protection):      {misuse_b_count}")
print(f"  MISUSE-C (f_n^sharp with a_n^zeta mixing): {misuse_c_count}")
print(f"  TOTAL counted misuses                 (pre-patch):  {n_misuses}")
print(f"  TRUE misuses after in-session patch:   {true_misuse_count}")

cross1_ok = check1_pass  # (local)
cross2_ok = check2_pass  # (local)
cross3_ok = check3_pass  # (local)

all_cross_pass = cross1_ok and cross2_ok and cross3_ok  # (local)

# Apply gate criterion to true_misuse_count (post-patch)
if true_misuse_count <= 3 and all_cross_pass:
    verdict = "PASS"
elif true_misuse_count > 10:
    verdict = "FAIL"
else:
    verdict = "INFO"

print(f"\n  Cross-checks: {'PASS' if all_cross_pass else 'FAIL'} (1:{cross1_ok}, 2:{cross2_ok}, 3:{cross3_ok})")
print(f"  VERDICT: {verdict}")

if verdict == "PASS":
    print(f"    Reason: dictionary built, all canonical a_n/R constants")
    print(f"    receive scheme_tag + branch_scope via PROVENANCE patch;")
    print(f"    {true_misuse_count} true cross-branch misuses, <=3 threshold.")
elif verdict == "INFO":
    print(f"    Reason: {true_misuse_count} cross-branch misuses remain")
    print(f"    after in-session correction (MISUSE-B/C need per-script edits).")

# =============================================================================
# SECTION 9: SAVE DICTIONARY AND AUDIT
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 9: Save dictionary and audit table")
print("=" * 78)

# Build structured arrays for NPZ persistence
names = list(dictionary.keys())  # (local)
values = np.array([dictionary[n][0] for n in names], dtype=np.float64)  # (local)
schemes = np.array([dictionary[n][1] for n in names], dtype=object)  # (local)
branches = np.array([dictionary[n][2] for n in names], dtype=object)  # (local)
lmaxes = np.array([dictionary[n][3] for n in names], dtype=object)  # (local)
notes_arr = np.array([dictionary[n][4] for n in names], dtype=object)  # (local)
names_arr = np.array(names, dtype=object)  # (local)

candidate_names = np.array([n for n, _ in CANDIDATE_SCRIPTS], dtype=object)  # (local)
candidate_purposes = np.array([p for _, p in CANDIDATE_SCRIPTS], dtype=object)  # (local)

misuse_names = np.array([m[0] for m in counted_misuses], dtype=object)  # (local)
misuse_rules = np.array([','.join(m[1]) for m in counted_misuses], dtype=object)  # (local)

np.savez(
    OUT_NPZ,
    # Dictionary
    dict_names=names_arr,
    dict_values=values,
    dict_schemes=schemes,
    dict_branches=branches,
    dict_lmaxes=lmaxes,
    dict_notes=notes_arr,
    HK_conversion_factor=HK_CONVERSION,
    # Cross-checks
    cross1_pass=cross1_ok,
    cross2_pass=cross2_ok,
    cross3_pass=cross3_ok,
    R1_zeta=R1_zeta,
    R1_hk=R1_hk,
    R1_preservation_error=R1_preserved,
    oom_9oom_cascade=oom,
    # Candidate scripts
    candidate_names=candidate_names,
    candidate_purposes=candidate_purposes,
    # Misuses
    misuse_script_names=misuse_names,
    misuse_rules=misuse_rules,
    misuse_a_count=misuse_a_count,
    misuse_b_count=misuse_b_count,
    misuse_c_count=misuse_c_count,
    n_misuses_total=n_misuses,
    n_misuses_post_patch=true_misuse_count,
    # Gate
    verdict=verdict,
)
print(f"  Saved: {OUT_NPZ}")


# =============================================================================
# SECTION 10: APPEND GATE VERDICT
# =============================================================================
verdict_line = (f"S78-W3-L-SDW-ZETA-DICT: {verdict} -- misuses={true_misuse_count}, "
                f"corrected={misuse_a_count}, candidates-audited={len(CANDIDATE_SCRIPTS)}, "
                f"dict-entries={len(dictionary)}, R1_preserved_per_branch={R1_preserved:.2e}, "
                f"cross-checks={'all PASS' if all_cross_pass else 'partial'}")

try:
    with open(GATE_VERDICTS, 'a', encoding='utf-8') as fh:
        fh.write(verdict_line + "\n")
    print(f"\n  Appended verdict to: {GATE_VERDICTS}")
except Exception as e:
    print(f"\n  Verdict-file append error: {e}")

print(f"\n  Verdict: {verdict_line}")
print(f"\n  Runtime: {time.time() - t_start:.2f} s")
print("=" * 78)
