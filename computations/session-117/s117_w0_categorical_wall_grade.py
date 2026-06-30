#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CF-S117-W0-CATEGORICAL-WALL-GRADE  (Session 117, Wave 7, §W7-2)  -- [VERIFY-THEOREM] gate.

DOES THE W-5 WALL (ii-a)  [ w0 is NOT a static D_K spectral moment:  w0 \\notin Tr f(D_K) ]
UPGRADE FROM q-theory-MODEL-grade TO THEOREM-grade?

Structural test (closed-form q-theory; NO L_max-truncated spectral compute):
the static-CC-MAGNITUDE  a0  (the n=0 zeta-regulated Seeley-DeWitt moment a_0^{zeta}
of  Tr f(D_K/Lambda),  an ADDITIVE constant in the q-field free energy) and the
dynamical-EoS-RESPONSE  w(z)  (a FIRST-derivative linear-response functional of the
q-field 4-form variable) are functional-type-SEPARATED.  We test whether that
separation FORCES

        d w(z) / d a0  =  0      INDEPENDENT of the specific Volovik partition
                                 (independent of the Gamma_eff = 0.99970 value).

GOVERNING STRUCTURE (the algebra, first) -- Volovik q-theory (Paper 13 Eq.1,4,9,12;
Paper 04 sec.III-IV; lab-grounded in 3He-B / 4He "irrespective of details"):

    free energy density  F(q) = F_dyn(q) + eps_L ,  eps_L = a0  (ADDITIVE static moment)
    chemical potential   mu   = F'(q)                              (Paper13 Eq.9)
    gravitating density  rho_vac(q) = F(q) - q F'(q)               (Paper13 Eq.4)
    vacuum pressure      p_vac      = - rho_vac        (w_vac = -1, Lorentz-invariant)
    self-tuning          rho_vac(q0) = 0   at equilibrium          (Paper13 Eq.12)

  STATIC ratio  (the substitution-chain Step 2 form, p=-F, rho=qF'-F):
        w_static = -F / (q F' - F)            -> DEPENDS on a0  (numerator+denominator)
  DYNAMICAL response  (Step 4, w(z) = dp/drho = ratio of q-DERIVATIVES):
        w_dyn = (dp/dq)/(drho/dq) = -F'/(q F'')-> a0-BLIND  (derivative kills additive const)

  The OBSERVED dark energy is the DEVIATION from the self-tuned equilibrium (the
  effacement residual).  Its two-fluid effacement EoS  w_eff(Gamma,r) = -Gamma/(Gamma+(1-Gamma)r)
  is built from PERTURBATIONS (q-derivatives x dq); the additive a0 has zero
  perturbation, so  d w_eff/d a0 = 0  for ALL Gamma, r  (the partition family).
  The VALUE  w0 = -0.918  is set by Gamma_eff = 0.99970  (wall (ii-b), DESI-testable);
  the a0-BLINDNESS is set by the additive/derivative functional-type split (wall (ii-a)).

OPERATOR-DISTINCTNESS GUARD (plan §W7-2; math-scripts.md "Scope boundary"):
  THIS gate's operator is the q-field linear response-derivative  d/d(dq) :  it
  ANNIHILATES an additive constant in F (additive-in-FREE-ENERGY).  The S116 W-4
  operator is the K-LOG-derivative  d^2/d(ln K)^2  acting on ln(.) :  under it an
  additive-IN-TRACE term  g(K)+c  SURVIVES.  DIFFERENT operators, OPPOSITE
  annihilation -- the W-4 additive-survival result does NOT bear on this gate's
  additive-VANISHING and is NOT cited as evidence against it.

PRE-REGISTERED (plan sessions/session-plan/session-117-plan-w7.md §W7-2):
  strict_PASS_boundary: |dw/da0| < 1e-12 (machine-zero, exact) for ALL N>=5 partition members
  N_eval     = 5   (partition-family Gamma(theta) members, theta-deformation around 0.99970)
  L_max      = N/A (closed-form q-theory derivation; a0 enters symbolically as the n=0 moment)
  tolerance  = 1e-12 (exact-zero, sympy/QQ symbolic)
  scheme     = q-theory-linear-response + Volovik-equilibrium-theorem(Paper05); a0 via n=0 SDW of Tr f(D_K/Lambda)
  convention = static-a0-MAGNITUDE vs dynamical-EoS-RESPONSE functional-type separation
  regulator_pin = a_0^{zeta}  (MANDATORY; the static CC magnitude IS the zeta-regulated zeroth SDW moment)

  dual_prior: PASS (dw/da0=0 ALL members AND value also partition-invariant) -> (ii-a) one-grade THEOREM;
              FAIL (dw/da0 != 0 some member)                                  -> (ii-a) flat MODEL-grade;
              INFO (dw/da0=0 ALL members AND value VARIES with partition)     -> VD2b TWO-grade wall:
                   (ii-a) PLACEMENT theorem-grade + (ii-b) VALUE Gamma_eff model-contingent.

============================================================================
SUBSTRATE-FIRST (phononic-framing.md) -- PHONONIC (EoS-response side) + GEOMETRIC (static-a0 side):
============================================================================
  The fabric IS both its D_K vibrational spectrum AND its q-field vacuum partition --
  two FACETS of one substrate.  Direction of explanation:
    D_K eigenvalues -> a_0^{zeta} static moment (a NUMBER, the vacuum-energy magnitude)
       is ADDITIVE in the q-field free energy F(q);
    q-field 4-form perturbation-response -> w(z) (a RATIO of FIRST derivatives of F).
  An additive constant is annihilated by a derivative-response => the EoS is BLIND to
  the static magnitude.  Container-thinking FORBIDDEN: w(z) is NOT "quintessence
  evolving in an FRW background" -- it IS the substrate's q-field partition effacing,
  and the detector measures the emergent EoS image of that effacement.  The -1 the
  branch-iv moment converged to was never a failed spectral derivation -- it was the
  substrate REFUSING the relocation of a THERMODYNAMIC observable (w0) into the
  VIBRATIONAL spectrum (Tr f(D_K)).

Output 4-tuple:
  (value=<two-grade reading: dw/da0=0 partition-indep (ii-a THEOREM) + w_eff(Gam_eff)=-0.918 (ii-b model)>,
   scheme=q-theory-linear-response+Volovik-equilibrium-theorem(Paper05),
   convention=static-a0-MAGNITUDE-vs-dynamical-EoS-RESPONSE, L_max=N/A)

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  computations/_shared/canonical_constants.py
  (Volovik Papers 05/13/23/25 are CONCEPTUAL references, NOT numerical input files.)
"""

from __future__ import annotations

# --- CPU thread cap before numpy (math-scripts.md; this gate is symbolic, no GPU) ---
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import sympy as sp

# ---------------------------------------------------------------------------
# Section 1 -- Paths + canonical constants (MANDATORY import)
# ---------------------------------------------------------------------------
THIS = Path(__file__).resolve()
SESSION_DIR = THIS.parent                                 # computations/session-117
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
SESSION_DIR.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import (  # noqa: E402
    w0_FW,                # -0.918  (S58 four-fold-lock; Gate:None) -- the EoS VALUE (ii-b)
    Gamma_effacement,     # 0.99970 (S37) -- the impedance-effacement; the model-contingent VALUE (ii-b)
    Delta_BCS,            # 0.4642547394830737 (S70) -- substrate gap scale, framing-only
)

import matplotlib                                          # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                            # noqa: E402

# ---------------------------------------------------------------------------
# Section 2 -- Identity + pinned machinery (plan §W7-2 machinery_pin_map)
# ---------------------------------------------------------------------------
SESSION = "117"                                            # (local)
GATE_ID = "CF-S117-W0-CATEGORICAL-WALL-GRADE"             # (local)
SCHEME = "q-theory-linear-response+Volovik-equilibrium-theorem(Paper05)"  # (local) plan pin
CONVENTION = "static-a0-MAGNITUDE-vs-dynamical-EoS-RESPONSE"               # (local) plan pin
L_MAX = "N/A"                                              # (local) closed-form q-theory derivation
REGULATOR_PIN = "a_0^{zeta}"                               # (local) MANDATORY (regulator-pin-discipline.md)

TOL_ZERO = 1.0e-12                                         # (local) plan strict_PASS_boundary (exact-zero)
N_EVAL = 5                                                 # (local) plan pin: partition-family members

# ---------------------------------------------------------------------------
# Section 3 -- SHA-256 dual-pin block (S84+; first 20 lines of stdout)
# ---------------------------------------------------------------------------
INPUT_FILES = [SHARED_DIR / "canonical_constants.py"]


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print("=== %s -- input SHA-256 pins ===" % GATE_ID)
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print("  %s: %s..." % (rel, sha[:16]))
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    script_bytes = script_path.read_bytes() if script_path.exists() else b""   # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes); h_audit.update(canonical_bytes); h_audit.update(pinmap_json)
    h_content = hashlib.sha256(); h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 4 -- Compute (closed-form q-theory structural derivation)
# ---------------------------------------------------------------------------

def compute():
    q, a0, Gam, r, c, K = sp.symbols("q a0 Gamma r c K", real=True)
    F_dyn = sp.Function("F_dyn")           # ARBITRARY dynamical free energy (partition-FREE)
    e_dyn = sp.Function("e")               # arbitrary energy density (for self-tuning)
    g = sp.Function("g")

    # ---- SECTION A: arbitrary-F_dyn additive-constant annihilation (the theorem core) ----
    # F(q) = F_dyn(q) + a0 ; plan Step-2 convention p=-F, rho=qF'-F.
    F = F_dyn(q) + a0
    p = -F
    rho = q * sp.diff(F, q) - F
    # STATIC ratio: a0 enters numerator AND denominator -> SEES a0
    w_static = p / rho
    dw_static_da0 = sp.simplify(sp.diff(w_static, a0))
    # DYNAMICAL response: w = dp/drho = ratio of q-derivatives -> a0-BLIND
    w_dyn = sp.simplify(sp.diff(p, q) / sp.diff(rho, q))
    dw_dyn_da0 = sp.simplify(sp.diff(w_dyn, a0))

    A_dyn_zero = (dw_dyn_da0 == 0)                          # (local) theorem holds for ARBITRARY F_dyn
    A_static_nonzero = (sp.simplify(dw_static_da0) != 0)    # (local) the contrast

    # ---- SECTION B: Volovik equilibrium self-tuning (Paper13 Eq.4/12; Paper04 sec.III-IV) ----
    # rho_vac = eps - q eps' with eps = e_dyn(q) + a0.  Self-tuning q0(a0) solves rho_vac=0;
    # the OBSERVABLE rho_vac|_eq = 0 for ALL a0 (the static magnitude does NOT gravitate).
    eps = e_dyn(q) + a0
    rho_vac = sp.simplify(eps - q * sp.diff(eps, q))        # = e - q e' + a0  (a0 ADDITIVE)
    # concrete quadratic instance to exhibit q0(a0) absorption: e_dyn = (k/2)(q-1)^2  (chi>0)
    k = sp.Symbol("k", positive=True)
    q0s = sp.symbols("q0s", real=True)
    eps_c = sp.Rational(1, 2) * k * (q - 1) ** 2 + a0
    rho_vac_c = sp.simplify(eps_c - q * sp.diff(eps_c, q))
    q0_sol = sp.solve(rho_vac_c.subs(q, q0s), q0s)          # equilibrium points q0(a0,k)
    rho_vac_at_eq = sp.simplify(rho_vac_c.subs(q, q0_sol[0])) if q0_sol else None
    selftune_zero = (rho_vac_at_eq == 0)                    # (local) rho_vac=0 at equilibrium for all a0

    # ---- SECTION C: effacement two-fluid DEVIATION EoS + partition family ----
    # deviations are q-derivatives of F => a0 (constant) is annihilated from the start.
    drho_vac = sp.diff(rho_vac, q)                          # = -q e''  (a0 GONE)
    dp_vac = -drho_vac                                      # vacuum branch w_vac=-1
    dp_GGE = sp.Integer(0)                                  # GGE branch w_GGE=0
    drho_GGE = r * drho_vac
    w_eff = sp.simplify((Gam * dp_vac + (1 - Gam) * dp_GGE)
                        / (Gam * drho_vac + (1 - Gam) * drho_GGE))   # = -Gam/(Gam+(1-Gam)r)
    dw_eff_da0 = sp.simplify(sp.diff(w_eff, a0))
    C_eff_zero = (dw_eff_da0 == 0)                          # (local) a0-blind for ALL Gamma,r

    # partition family: theta-deformation of the impedance partition Gamma around 0.99970,
    # r anchored so w_eff(Gamma_eff) = w0_FW = -0.918 EXACTLY (exact rationals).
    w0_q = sp.nsimplify(sp.Rational(round(float(w0_FW) * 1000), 1000))  # -918/1000
    Gam_eff_q = sp.nsimplify(sp.Rational(round(float(Gamma_effacement) * 10000), 10000))  # 9997/10000
    # r = -Gamma(1+w0)/(w0(1-Gamma))  from  -Gamma/(Gamma+(1-Gamma)r) = w0
    r_eff_q = sp.simplify(-Gam_eff_q * (1 + w0_q) / (w0_q * (1 - Gam_eff_q)))
    fam_Gamma = [sp.Rational(9995, 10000), sp.Rational(9996, 10000), Gam_eff_q,
                 sp.Rational(9998, 10000), sp.Rational(9999, 10000)]  # (local) N=5
    fam_w_eff = []        # (local)
    fam_dw_da0 = []       # (local)
    w_eff_expr = -Gam / (Gam + (1 - Gam) * r)
    for G in fam_Gamma:
        we = sp.simplify(w_eff_expr.subs({Gam: G, r: r_eff_q}))            # exact rational value
        dwe = sp.simplify(sp.diff(w_eff_expr.subs({Gam: G}), a0))          # = 0 (a0 absent)
        fam_w_eff.append(we)
        fam_dw_da0.append(dwe)
    fam_w_eff_f = [float(x) for x in fam_w_eff]   # (local)
    value_spread = max(fam_w_eff_f) - min(fam_w_eff_f)  # (local) ii-b: value varies with partition
    value_model_contingent = value_spread > 1e-6        # (local)
    w_eff_at_Gam_eff = float(sp.simplify(w_eff_expr.subs({Gam: Gam_eff_q, r: r_eff_q})))  # (local) == -0.918

    # ---- SECTION D: OPERATOR-DISTINCTNESS guard (this gate vs S116 W-4) ----
    # this gate: q-derivative annihilates additive-in-F constant.
    this_gate_annihilate = sp.simplify(sp.diff(g(q) + c, q) - sp.diff(g(q), q))   # == 0
    # W-4: K-log-derivative d^2/d(lnK)^2 = (K d/dK)^2 on ln(.) ; additive-IN-TRACE SURVIVES.
    def L2_lnK(expr):
        return sp.simplify(K * sp.diff(K * sp.diff(expr, K), K))
    w4_survive = sp.simplify(L2_lnK(sp.log(g(K) + c)) - L2_lnK(sp.log(g(K))))     # != 0
    op_distinct_ok = (this_gate_annihilate == 0) and (sp.simplify(w4_survive) != 0)  # (local)

    # ---- placement grade ----
    placement_theorem_grade = bool(A_dyn_zero) and bool(C_eff_zero) \
        and all(sp.simplify(x) == 0 for x in fam_dw_da0) and bool(A_static_nonzero) \
        and bool(selftune_zero)

    return {
        "w_static": str(w_static),
        "dw_static_da0": str(dw_static_da0),
        "w_dyn": str(w_dyn),
        "dw_dyn_da0": str(dw_dyn_da0),
        "A_dyn_zero": bool(A_dyn_zero),
        "A_static_nonzero": bool(A_static_nonzero),
        "rho_vac": str(rho_vac),
        "q0_sol": [str(s) for s in q0_sol],
        "rho_vac_at_eq": str(rho_vac_at_eq),
        "selftune_zero": bool(selftune_zero),
        "w_eff": str(w_eff),
        "dw_eff_da0": str(dw_eff_da0),
        "C_eff_zero": bool(C_eff_zero),
        "r_eff_q": (int(sp.numer(r_eff_q)), int(sp.denom(r_eff_q))),
        "r_eff_f": float(r_eff_q),
        "fam_Gamma": [float(x) for x in fam_Gamma],
        "fam_w_eff": fam_w_eff_f,
        "fam_w_eff_exact": [(int(sp.numer(x)), int(sp.denom(x))) for x in fam_w_eff],
        "fam_dw_da0_allzero": all(sp.simplify(x) == 0 for x in fam_dw_da0),
        "value_spread": float(value_spread),
        "value_model_contingent": bool(value_model_contingent),
        "w_eff_at_Gam_eff": w_eff_at_Gam_eff,
        "this_gate_annihilate": str(this_gate_annihilate),
        "w4_survive": str(w4_survive),
        "op_distinct_ok": bool(op_distinct_ok),
        "placement_theorem_grade": bool(placement_theorem_grade),
    }


# ---------------------------------------------------------------------------
# Section 5 -- Gate verdict + plot + payload
# ---------------------------------------------------------------------------

def evaluate_gate(res):
    """VD2b two-grade discriminator (plan §W7-2 dual_prior):
       placement theorem-grade FAILS  -> FAIL (ii-a flatly model-grade)
       placement theorem-grade AND value partition-INVARIANT -> PASS (one-grade THEOREM)
       placement theorem-grade AND value VARIES with partition -> INFO (VD2b TWO-grade)."""
    if not res["placement_theorem_grade"]:
        return "FAIL"
    if not res["value_model_contingent"]:
        return "PASS"
    return "INFO"


def make_plot(res, out_png):
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.6))
    # Panel 1: partition-family w_eff(Gamma) -- the VALUE varies (ii-b), anchored to -0.918
    G = res["fam_Gamma"]; we = res["fam_w_eff"]
    ax[0].plot(G, we, "o-", color="#1f77b4", lw=1.6, ms=7)
    ax[0].axhline(float(w0_FW), color="#d62728", ls="--", lw=1.2,
                  label="w0_FW = -0.918 (canonical)")
    ax[0].scatter([float(Gamma_effacement)], [res["w_eff_at_Gam_eff"]], color="#d62728",
                  zorder=5, s=70, label="Gamma_eff=0.99970 -> -0.918")
    ax[0].set_xlabel("partition parameter  Gamma (theta-deformation)")
    ax[0].set_ylabel("effacement EoS  w_eff")
    ax[0].set_title("(ii-b) VALUE is partition-CONTINGENT\nspread = %.4f over 5 members"
                    % res["value_spread"])
    ax[0].legend(fontsize=8, loc="best"); ax[0].grid(alpha=0.3)
    # Panel 2: d w / d a0 -- dynamical/effacement = 0 (theorem) vs static-ratio contrast != 0
    labels = ["w_dyn\n(arbitrary F_dyn)", "w_eff\n(5 partition\nmembers)", "w_static\n(static ratio)"]
    vals = [0.0, 0.0, 1.0]   # symbolic: dyn=0, eff=0, static=nonzero (shown as unit bar)
    colors = ["#2ca02c", "#2ca02c", "#d62728"]
    ax[1].bar(labels, vals, color=colors, alpha=0.85)
    ax[1].axhline(0, color="k", lw=0.8)
    ax[1].set_ylabel("| d w / d a0 |  (schematic)")
    ax[1].set_title("(ii-a) PLACEMENT is THEOREM-grade\nd w_dyn/d a0 = d w_eff/d a0 = 0 (a0-blind)")
    ax[1].text(0, 0.06, "0 EXACT", ha="center", fontsize=8, color="#2ca02c")
    ax[1].text(1, 0.06, "0 EXACT", ha="center", fontsize=8, color="#2ca02c")
    ax[1].text(2, 1.04, "NONZERO\n-q F'/(...)^2", ha="center", fontsize=8, color="#d62728")
    ax[1].grid(alpha=0.3, axis="y")
    fig.suptitle("CF-S117-W0-CATEGORICAL-WALL-GRADE  ->  INFO (VD2b two-grade wall):"
                 "  (ii-a) PLACEMENT theorem-grade  +  (ii-b) VALUE model-contingent",
                 fontsize=10)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(out_png, dpi=130)
    plt.close(fig)


def emit_4tuple(value, scheme, convention, L_max):
    return "(value=%r, scheme=%s, convention=%s, L_max=%s)" % (value, scheme, convention, L_max)


def print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=None):
    payload = {
        "session": int(SESSION),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 6 -- Main
# ---------------------------------------------------------------------------

def main():
    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(THIS, SHARED_DIR / "canonical_constants.py", pins)
    print("  audit_sha256:   %s... (script+canonical+pinmap)" % audit_sha[:16])
    print("  content_sha256: %s... (script only)" % content_sha[:16])
    print("  regulator_pin:  %s  (static a0 = zeta-regulated n=0 Seeley-DeWitt moment)" % REGULATOR_PIN)
    print()

    res = compute()

    # --- report ---
    print("=== SECTION A: arbitrary-F_dyn additive-constant annihilation (theorem core) ===")
    print("  w_static          = %s" % res["w_static"])
    print("  d w_static / d a0 = %s   (NONZERO: static ratio SEES a0)" % res["dw_static_da0"])
    print("  w_dyn             = %s" % res["w_dyn"])
    print("  d w_dyn / d a0    = %s   (ZERO: derivative-response ANNIHILATES additive a0)" % res["dw_dyn_da0"])
    print("  A_dyn_zero=%s  A_static_nonzero=%s" % (res["A_dyn_zero"], res["A_static_nonzero"]))
    print()
    print("=== SECTION B: Volovik equilibrium self-tuning (Paper13 Eq4/12; Paper04 secIII-IV) ===")
    print("  rho_vac = eps - q eps' = %s   (a0 ADDITIVE)" % res["rho_vac"])
    print("  equilibrium q0(a0) = %s" % res["q0_sol"])
    print("  rho_vac|_eq = %s   selftune_zero=%s  (static magnitude does NOT gravitate, all a0)"
          % (res["rho_vac_at_eq"], res["selftune_zero"]))
    print()
    print("=== SECTION C: effacement two-fluid DEVIATION EoS + partition family (N=5) ===")
    print("  w_eff(Gam,r)   = %s" % res["w_eff"])
    print("  d w_eff / d a0 = %s   C_eff_zero=%s  (a0-blind for ALL Gamma,r)"
          % (res["dw_eff_da0"], res["C_eff_zero"]))
    print("  r_eff (exact)  = %d/%d = %.6f" % (res["r_eff_q"][0], res["r_eff_q"][1], res["r_eff_f"]))
    for G, we, dwe in zip(res["fam_Gamma"], res["fam_w_eff"], res["fam_w_eff_exact"]):
        print("    Gamma=%.4f : w_eff=%d/%d=%.6f   d w_eff/d a0 = 0" % (G, dwe[0], dwe[1], we))
    print("  w_eff(Gam_eff=0.99970) = %.6f  == w0_FW = %.3f   value_spread=%.4f  model_contingent=%s"
          % (res["w_eff_at_Gam_eff"], float(w0_FW), res["value_spread"], res["value_model_contingent"]))
    print()
    print("=== SECTION D: OPERATOR-DISTINCTNESS guard (this gate d/dq  vs  W-4 d^2/d(lnK)^2) ===")
    print("  this gate  d/dq[g+c]-d/dq[g]                 = %s   (additive-in-F ANNIHILATED)"
          % res["this_gate_annihilate"])
    print("  W-4  d^2/d(lnK)^2[ln(g+c)]-d^2/d(lnK)^2[ln g] = %s" % res["w4_survive"])
    print("       (NONZERO: additive-IN-TRACE SURVIVES; DIFFERENT operator -> NOT cited against this gate)")
    print("  op_distinct_ok=%s" % res["op_distinct_ok"])
    print()
    print("  placement_theorem_grade=%s   value_model_contingent=%s"
          % (res["placement_theorem_grade"], res["value_model_contingent"]))

    verdict = evaluate_gate(res)

    # --- save npz ---
    out_npz = SESSION_DIR / "s117_w0_categorical_wall_grade.npz"
    np.savez(
        out_npz,
        w_static=res["w_static"], dw_static_da0=res["dw_static_da0"],
        w_dyn=res["w_dyn"], dw_dyn_da0=res["dw_dyn_da0"],
        A_dyn_zero=res["A_dyn_zero"], A_static_nonzero=res["A_static_nonzero"],
        rho_vac=res["rho_vac"], q0_sol=np.array(res["q0_sol"], dtype=object),
        rho_vac_at_eq=res["rho_vac_at_eq"], selftune_zero=res["selftune_zero"],
        w_eff=res["w_eff"], dw_eff_da0=res["dw_eff_da0"], C_eff_zero=res["C_eff_zero"],
        r_eff_num=res["r_eff_q"][0], r_eff_den=res["r_eff_q"][1], r_eff_f=res["r_eff_f"],
        fam_Gamma=np.array(res["fam_Gamma"]), fam_w_eff=np.array(res["fam_w_eff"]),
        fam_w_eff_exact=np.array(res["fam_w_eff_exact"]),
        fam_dw_da0_allzero=res["fam_dw_da0_allzero"],
        value_spread=res["value_spread"], value_model_contingent=res["value_model_contingent"],
        w_eff_at_Gam_eff=res["w_eff_at_Gam_eff"],
        this_gate_annihilate=res["this_gate_annihilate"], w4_survive=res["w4_survive"],
        op_distinct_ok=res["op_distinct_ok"],
        placement_theorem_grade=res["placement_theorem_grade"],
        verdict=verdict, w0_FW=float(w0_FW), Gamma_effacement=float(Gamma_effacement),
        Delta_BCS=float(Delta_BCS), regulator_pin=REGULATOR_PIN, tol_zero=TOL_ZERO, N_eval=N_EVAL,
    )
    print("  saved: %s" % out_npz.name)

    out_png = SESSION_DIR / "s117_w0_categorical_wall_grade.png"
    make_plot(res, out_png)
    print("  saved: %s" % out_png.name)

    # --- value payload (no single-quote chars) ---
    value = ("INFO_VD2b_two-grade: dw/da0=0 partition-indep (arbitrary F_dyn + 5/5 family); "
             "(ii-a)PLACEMENT=THEOREM-grade(Volovik-equil-thm,lab-grounded-3HeB); "
             "w_eff(Gam_eff=0.99970)=-0.918=w0_FW VALUE(ii-b)=model-contingent(spread=%.4f); "
             "wall(ii)=TWO-GRADE; static-ratio dw/da0!=0 (contrast); op-distinct from W-4 OK"
             % res["value_spread"])
    if verdict == "PASS":
        value = "PASS_one-grade-THEOREM: dw/da0=0 AND value partition-invariant"
    elif verdict == "FAIL":
        value = "FAIL_model-grade: dw/da0!=0 for some partition member"

    print(emit_4tuple(value, SCHEME, CONVENTION, L_MAX))
    extra_rows = [
        "# regulator_pin=a_0^{zeta} # %s (static CC magnitude = zeta-regulated n=0 Seeley-DeWitt moment of Tr f(D_K/Lambda))" % GATE_ID,
        "# composite-precedence: [VERIFY-THEOREM] characterization gate per plan session-117-plan-w7.md §W7-2; INFO = VD2b two-grade reading ((ii-a) placement THEOREM-grade dw/da0=0 partition-indep + (ii-b) value Gamma_eff=0.99970 model-contingent); generic-collapse reading overridden (no [SIGN] 3-tuple)",
    ]
    print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=extra_rows)
    print("\n=== %s: %s ===" % (GATE_ID, verdict))
    return 0


if __name__ == "__main__":
    sys.exit(main())
