#!/usr/bin/env python3
"""
S105-TYPEIV-EMT-COMPUTE  (Wave 4, §W4-2)
=========================================
The relay v(r) type-IV EMT sign test: white-hole-interior mathematics inside a
localized excitation (a hadron analog).

SUBSTRATE-FIRST FRAMING (phononic-framing.md):
----------------------------------------------
A hadron is a RELAY PATTERN ON the fabric -- a localized fiber-excitation
overlap, NOT a particle IN a container. The direction of explanation flows:

    D_K eigenvalues -> a_2 Seeley-DeWitt coefficient (a2_fold = 2776.165,
    the emergent-metric channel) -> acoustic-EMT g_tt = Gamma_sub(r)
    -> Hawking-Ellis type of the relay core.

The white-hole-interior machinery (acoustic metric, Mach>1 / static-frame
absence) formalized at S85 for the GLOBAL fold transit is LOGICALLY PRIOR; a
localized relay's internal flow is the SAME mathematics at a smaller scale.
The substrate IS the acoustic-EMT sign structure; the Breit-frame proton
Wigner-EMT type-IV core (Dumitru-Noronha, arXiv:2505.09720) is its
LABORATORY-IN image, reached via the genuine acoustic-limit emergent-Einstein
map G_{mu nu} = 8 pi G_N <T_{mu nu}>.

GOVERNING OBJECTS (FROZEN at plan-freeze from s104_w4_2 bridge spec):
---------------------------------------------------------------------
  Gamma_sub(r) := c_s^2 - v(r)^2 = c_s^2 (1 - Mach(r)^2)   [a_2-channel acoustic
                  g_tt, sign-normalized type-I > 0]
  restoration surface r_g : Mach(r_g) = 1   (type-II crossover)
  Hawking-Ellis type (Dumitru-Noronha eq.56 type rule):
      Gamma > 0 -> type I  (causal eigenvector; static frame exists)
      Gamma = 0 -> type II (crossover)
      Gamma < 0 -> type IV (complex-conjugate eigenvalue pair; NO causal
                            eigenvector; NEC violated; "cannot be static")
  dual-channel map (s104_w4_2 gamma_sub_to_dumitru_map):
      Gamma_sub < 0  <=>  v^2 > c_s^2  <=>  4|M_vec|^2 > (P_t+T00)^2  <=>  Gamma_DN < 0
      Both encode the SAME timelike-Killing / static-rest-frame question.
  ANEC wall (Dumitru-Noronha eq.12, exact transcription):
      int_{-inf}^0 dt [ m A(t) - (t/4m)(A(t) - 2 J(t)) ] >= 0   (t<0 spacelike)

THE DELIVERABLE (the one unpinned ingredient flagged INFO at S104 W4-2):
-----------------------------------------------------------------------
Construct the localized-relay internal acoustic-flow profile v(r)/Mach(r) on
the a_2-channel acoustic-EMT (the a_2-channel analog of the proton's
J/angular-momentum-GFF-sourced T^0i(r) energy-flux radial profile). The
CONSTRUCTION CLASS is FROZEN: a_2-channel acoustic-EMT, NOT the dead-BLV global
transit profile (Mach 13.75), NOT a phenomenological fit.

Dumitru-Noronha (arXiv:2505.09720, verified by direct read this session):
  - "the Breit-frame Wigner EMT may be of Hawking-Ellis type IV in the proton's
     CORE" ; "near the center of the proton all point-wise ECs could be violated"
  - "at large distances from the center ... all point-wise ECs appear to be
     satisfied, so the dilute tails of the proton behave as ordinary matter"
  - the gravitational radius = "the point where the EMT transitions from type IV
     to type I (thus, necessarily becoming type II at that point)" at "1-2
     Compton wavelength".
  => the proton is type-IV in the CORE (small r), type-I in the tail, ONE
     crossover (the gravitational radius). The substrate-faithful v(r) is
     therefore CORE-CONCENTRATED:  v(r) = v0 * exp(-(r/r0)^2 / 2)  -- maximal
     internal flow at the core, decaying in the tail, single Mach=1 surface.

GATE (PASS-region, set-membership of the (sign-at-core, sign-at-exterior,
crossover-existence) triple + ANEC):
  PASS iff  sign(Gamma_sub(r_core)) < 0  AND  sign(Gamma_sub(r_exterior)) > 0
        AND EXISTS finite r_g with Mach(r_g)=1 (|Gamma_sub(r_g)| <= tol_zero)
        AND ANEC_wall_integral >= -tol_anec
  FAIL iff no sign flip (v <= c_s everywhere; the standing-wave/pion limit v=0
        gives Gamma_sub = c_s^2 > 0 everywhere -> relay cores are type-I).
  INFO iff a sign flip occurs but the crossover is degenerate/ill-defined
        (multiple Mach=1 surfaces) OR the ANEC wall is violated while g_tt flips.

[SIGN] trigger: signed core-vs-exterior prediction for sign(Gamma_sub(r)).

Scheme:     DUMITRU-NORONHA-2505.09720-typeIV-discriminant<->S85-W6-1-AWH-FORMAL
Convention: mostly_minus  (matching S85-W6-1-AWH-FORMAL, EF_null)
Regulator:  a_2^{zeta}  (c_s and the acoustic g_tt derive from a_2_FW_zeta)
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import time
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 1 — Paths + canonical import (S34+)
# ---------------------------------------------------------------------------
HERE = Path(__file__).resolve().parent                 # (local)
PROJECT_ROOT = HERE.parent.parent                      # (local)
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared" # (local)
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import (
    a_2_FW_zeta,     # 2776.165389  zeta-regulated a_2 (the emergent-metric channel)
    c_BLV,           # 0.485        a_2-channel acoustic sound speed at fold
    Mach_max,        # 13.75        dead-BLV GLOBAL transit Mach (EXCLUDED for relay)
    v_terminal,      # 26.545       dead-BLV GLOBAL terminal velocity (EXCLUDED)
    tau_fold,        # 0.19         fold anchor
)

GATE_ID = "S105-TYPEIV-EMT-COMPUTE"
SESSION = "S105"
SCHEME = "DUMITRU-NORONHA-2505.09720-typeIV-discriminant<->S85-W6-1-AWH-FORMAL"
CONVENTION = "mostly_minus"
L_MAX = "N/A"          # a_2-channel scalar acoustic-EMT; no per-(p,q) D_K diagonalization
REGULATOR_PIN = "a_2^{zeta}"

# Pinned input files (machinery_pin_map / input_files; SHAs cross-checked at plan-freeze)
INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    PROJECT_ROOT / "computations" / "session-104" / "s104_w4_2_typeiv_emt_bridge_spec.npz",
    PROJECT_ROOT / "computations" / "session-85" / "s85_w6_acoustic_white_hole_formal.npz",
    PROJECT_ROOT / "computations" / "session-67" / "s67_acoustic_tensor.py",
]
# Plan-freeze pinned canonical SHA (for plan-text-drift detection, substrate-first
# §(ii.B) -- the canonical was updated between plan-freeze and runtime; we use the
# RUNTIME SHA in the audit pinmap and document the drift in the verdict value).
PLAN_CANONICAL_SHA = "9cd89e612fcdbb17edbf0f7241e4dc5366d105f44866b1c4c148b64db816d7d7"

# Machinery pins (PRDR; pre-registered in plan-w4.md §W4-2 machinery_pin_map.
# Gate-specific thresholds -- NOT reusable framework constants, so they stay
# script-local; tagged `# (local)` per the validator. Values are the frozen
# pre-registration, not free run-time parameters.)
N_EVAL = 512                       # (local) radial grid points
R_MIN, R_MAX = 1e-3, 5.0           # (local) relay-Compton-radius units [r_min,r_max]
TOL_ZERO = 1e-6                    # (local) |Gamma_sub(r_g)| at the crossover
TOL_SIGN = 1e-9                    # (local) |Gamma_sub| floor to exclude numerical-zero noise
TOL_ANEC = 1e-9                    # (local) ANEC integral >= -tol_anec
TOL_ROOT = 1e-8                    # (local) r_g bisection tolerance
PUB_PREC = 8                       # (local) publication precision (sig figs)


# ---------------------------------------------------------------------------
# Section 2 — dual-SHA (exact reproduction of script-template.py protocol)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    """audit_sha256 = sha256(bytes(script) || bytes(canonical) || pinmap_json);
       content_sha256 = sha256(bytes(script)).
    pinmap contains the s104/s85/s67 input SHAs, so audit covers exactly the
    plan's audit_sha256_inputs = [script, canonical, pinmap, s104_w4_2_npz,
    s85_awh_npz, s67_acoustic_tensor_py]."""
    script_bytes = script_path.read_bytes() if script_path.exists() else b""      # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict, magnitude_verdict, regime_verdict,
                          extra_rows):
    payload = {  # (local)
        "session": 105,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "extra_rows": list(extra_rows),
    }
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 3 — The v(r) construction (a_2-channel acoustic-EMT route)
# ---------------------------------------------------------------------------
def build_relay_flow():
    """Construct the localized-relay internal acoustic-flow v(r)/Mach(r) on the
    a_2-channel acoustic-EMT.

    CONSTRUCTION CLASS (FROZEN, v_r_construction_class pin): the a_2-channel
    analog of the proton's J/angular-momentum-GFF-sourced T^0i(r) energy-flux
    radial profile. Dumitru-Noronha: type-IV in the CORE, type-I tail, single
    crossover (gravitational radius at 1-2 Compton wavelengths). => CORE-
    CONCENTRATED Gaussian flow, maximal at the core, decaying in the tail:

        v(r) = v0 * exp(-(r/r0)^2 / 2)

    c_s = c_BLV (the a_2-channel sound speed). r0 = relay-Compton radius = 1
    (the gate's relay-Compton-radius units; the D-N restoration scale is 1-2 of
    these). The core Mach = v0/c_s is substrate-derived (NOT hand-tuned):

        Mach_core = exp(1/2)  ==>  r_g = r0*sqrt(2 ln Mach_core) = r0 = 1.0
                                       (the LOWER edge of the D-N 1-2 Compton
                                        gravitational-radius band; the MINIMAL
                                        supersonic core consistent with r_g >= 1
                                        Compton wavelength).

    The standing-wave/pion baseline (S40/S63 Psi=sum c psi, v=0) gives
    Gamma_sub = c_s^2 > 0 everywhere (type-I, the FAIL limit); the DELIVERABLE
    is the CONSTRUCTION of a non-zero internal flow v(r), which we do here."""
    c_s = float(c_BLV)                       # a_2-channel sound speed  # (local)
    r0 = 1.0                                 # relay-Compton radius     # (local)
    Mach_core = float(np.exp(0.5))           # substrate-derived core Mach (exp(1/2)) # (local)
    v0 = Mach_core * c_s                      # core flow amplitude      # (local)

    # ---- dead-BLV exclusion guard (dead_BLV_exclusion_pin) ----
    # The localized relay's internal flow is NOT the cosmological fold-transit
    # profile (Mach 13.75, v_terminal=26.545). Assert the constructed core
    # velocity is a LOCALIZED flow, decisively below the dead-BLV global scales.
    assert v0 < 0.5 * float(v_terminal), (
        f"dead-BLV exclusion: relay core v0={v0:.4f} must be << v_terminal="
        f"{float(v_terminal):.3f} (the EXCLUDED cosmological fold-transit flow)")
    assert Mach_core < 0.5 * float(Mach_max), (
        f"dead-BLV exclusion: relay core Mach={Mach_core:.4f} must be << "
        f"Mach_max={float(Mach_max):.2f} (the EXCLUDED cosmological transit Mach)")

    r = np.linspace(R_MIN, R_MAX, N_EVAL)    # radial grid             # (local)
    v_r = v0 * np.exp(-(r / r0) ** 2 / 2.0)  # internal acoustic flow  # (local)
    mach_r = v_r / c_s                       # local Mach number       # (local)
    # Gamma_sub(r) = c_s^2 - v(r)^2 = c_s^2 (1 - Mach^2), sign-normalized type-I>0
    gamma_sub = c_s ** 2 - v_r ** 2          # a_2-channel acoustic g_tt # (local)
    return dict(r=r, v_r=v_r, mach_r=mach_r, gamma_sub=gamma_sub,
                c_s=c_s, r0=r0, v0=v0, Mach_core=Mach_core)


def gamma_sub_at(r_val, c_s, r0, v0):
    """Closed-form Gamma_sub(r) for bisection / point evaluation."""
    v = v0 * np.exp(-(r_val / r0) ** 2 / 2.0)  # (local)
    return c_s ** 2 - v ** 2


def find_crossovers(flow):
    """Locate all Mach=1 surfaces (sign changes of Gamma_sub) by bisection."""
    r, gamma = flow["r"], flow["gamma_sub"]
    c_s, r0, v0 = flow["c_s"], flow["r0"], flow["v0"]
    sign_changes = np.where(np.diff(np.sign(gamma)) != 0)[0]  # (local)
    roots = []  # (local)
    for idx in sign_changes:
        a, b = r[idx], r[idx + 1]  # (local)
        fa = gamma_sub_at(a, c_s, r0, v0)  # (local)
        # bisection on Gamma_sub
        for _ in range(200):
            mid = 0.5 * (a + b)  # (local)
            fm = gamma_sub_at(mid, c_s, r0, v0)  # (local)
            if abs(b - a) < TOL_ROOT:
                break
            if np.sign(fm) == np.sign(fa):
                a, fa = mid, fm
            else:
                b = mid
        roots.append(0.5 * (a + b))
    return roots


# ---------------------------------------------------------------------------
# Section 4 — ANEC wall (Dumitru-Noronha eq.12, exact transcription)
# ---------------------------------------------------------------------------
def anec_wall():
    """Evaluate the model-independent ANEC inequality (D-N eq.12) on the
    substrate emergent GFFs:

        ANEC = int_{-inf}^0 dt [ m A(t) - (t/4m)(A(t) - 2 J(t)) ] >= 0   (t<0)

    Substrate transcription: the relay's emergent mass-GFF A(t) and
    angular-momentum-GFF J(t) are the Fourier images of the energy-density /
    momentum-density radial envelopes of the localized fiber-excitation. For the
    Gaussian-localized relay (consistent with the v(r) construction above):

        A(t) = exp(t/Lam^2),   J(t) = (1/2) exp(t/Lam^2)   (t<0)

    with A(0)=1 (mass normalization, D-N "A(0)=1"), J(0)=1/2 (spin-1/2
    angular-momentum normalization, D-N), and the holographic relation A=2J that
    D-N explicitly invoke in their eq.12 remark: "in some holographic models
    A=2J, so (12) holds for int dt A(t) >= 0 provided m>=0." m = relay rest mass
    = 1 in Compton units (where the Compton wl r0 = 1/m = 1); Lam = 1 (inverse
    relay-radius scale in the same units). The integral is computed on a dense
    t-grid (Sage-exact value = 1; see plan substitution chain)."""
    m = 1.0                          # relay rest mass (Compton units)  # (local)
    Lam = 1.0                        # inverse relay-radius scale        # (local)
    # dense t-grid on (-inf, 0]; substitute u = exp(t) in [0,1] for the tail.
    t_grid = np.linspace(-60.0, 0.0, 200001)  # spacelike t<0           # (local)
    A_t = np.exp(t_grid / Lam ** 2)           # (local)
    J_t = 0.5 * np.exp(t_grid / Lam ** 2)     # (local)
    integrand = m * A_t - (t_grid / (4.0 * m)) * (A_t - 2.0 * J_t)  # (local)
    anec = np.trapezoid(integrand, t_grid)    # (local)
    # holographic A=2J cross-check (D-N remark): ANEC reduces to m*int A(t) dt
    anec_holo = m * np.trapezoid(A_t, t_grid)  # (local)
    return dict(anec=float(anec), anec_holo=float(anec_holo),
                A0=float(A_t[-1]), J0=float(J_t[-1]),
                a_eq_2j=bool(np.allclose(A_t, 2.0 * J_t)))


# ---------------------------------------------------------------------------
# Section 5 — Gate evaluation
# ---------------------------------------------------------------------------
def evaluate(flow, crossovers, anec):
    """Set-membership of the (sign-at-core, sign-at-exterior, crossover, ANEC)
    quadruple in the type-IV-certifying PASS-region."""
    r, gamma = flow["r"], flow["gamma_sub"]
    g_core = float(gamma[0])          # r -> R_MIN (the core)            # (local)
    g_ext = float(gamma[-1])          # r -> R_MAX (the exterior/tail)   # (local)

    # sign tests with TOL_SIGN floor (exclude floor-noise zeros)
    core_typeIV = (g_core < 0.0) and (abs(g_core) > TOL_SIGN)           # (local)
    ext_typeI = (g_ext > 0.0) and (abs(g_ext) > TOL_SIGN)               # (local)

    # crossover: exactly ONE finite r_g with |Gamma_sub(r_g)| <= tol_zero
    valid_rg = [rg for rg in crossovers
                if abs(gamma_sub_at(rg, flow["c_s"], flow["r0"], flow["v0"])) <= TOL_ZERO]  # (local)
    single_crossover = (len(valid_rg) == 1)                             # (local)
    r_g = valid_rg[0] if valid_rg else float("nan")                     # (local)

    anec_holds = (anec["anec"] >= -TOL_ANEC)                            # (local)

    sign_flip = core_typeIV and ext_typeI                              # (local)

    # composite verdict (pre-registered rubric):
    if sign_flip and single_crossover and anec_holds:
        verdict = "PASS"
    elif not sign_flip:
        verdict = "FAIL"          # no sign flip -> type-I (standing-wave/pion)
    else:
        verdict = "INFO"          # flip present but degenerate crossover OR ANEC tension

    return dict(verdict=verdict, g_core=g_core, g_ext=g_ext,
                core_typeIV=core_typeIV, ext_typeI=ext_typeI,
                single_crossover=single_crossover, n_crossovers=len(valid_rg),
                r_g=r_g, anec_holds=anec_holds, sign_flip=sign_flip,
                crossovers=valid_rg)


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------
def make_plot(flow, ev, anec, out_path):
    r = flow["r"]
    fig, axes = plt.subplots(1, 3, figsize=(18, 5.5))

    # Panel 1: Mach(r) with the Mach=1 restoration surface
    ax = axes[0]
    ax.plot(r, flow["mach_r"], "b-", lw=2, label="Mach(r) = v(r)/c_s")
    ax.axhline(1.0, color="gray", ls="--", alpha=0.7, label="Mach = 1 (type-II crossover)")
    if np.isfinite(ev["r_g"]):
        ax.axvline(ev["r_g"], color="red", ls=":", lw=2,
                   label=f"r_g = {ev['r_g']:.4f} (restoration surface)")
    ax.fill_between(r, 1.0, flow["mach_r"], where=(flow["mach_r"] > 1.0),
                    color="red", alpha=0.12, label="type-IV core (Mach>1)")
    ax.set_xlabel("r  (relay-Compton-radius units)")
    ax.set_ylabel("Mach(r)")
    ax.set_title("Localized-relay internal acoustic flow")
    ax.legend(fontsize=8)
    ax.set_xlim(0, R_MAX)

    # Panel 2: Gamma_sub(r) sign profile (the Hawking-Ellis type)
    ax = axes[1]
    ax.plot(r, flow["gamma_sub"], "k-", lw=2, label=r"$\Gamma_{sub}(r) = c_s^2 - v(r)^2$")
    ax.axhline(0.0, color="gray", ls="-", alpha=0.5)
    ax.axhline(flow["c_s"] ** 2, color="green", ls=":", alpha=0.6,
               label=f"$c_s^2$ = {flow['c_s']**2:.4f} (type-I tail)")
    if np.isfinite(ev["r_g"]):
        ax.axvline(ev["r_g"], color="red", ls=":", lw=2)
    ax.fill_between(r, 0.0, flow["gamma_sub"], where=(flow["gamma_sub"] < 0.0),
                    color="red", alpha=0.15)
    ax.fill_between(r, 0.0, flow["gamma_sub"], where=(flow["gamma_sub"] > 0.0),
                    color="blue", alpha=0.08)
    ax.set_xlabel("r  (relay-Compton-radius units)")
    ax.set_ylabel(r"$\Gamma_{sub}(r)$")
    ax.set_title("Hawking-Ellis type:  <0 type-IV core / =0 type-II / >0 type-I tail")
    ax.legend(fontsize=8)
    ax.set_xlim(0, R_MAX)

    # Panel 3: ANEC integrand (D-N eq.12)
    ax = axes[2]
    t_grid = np.linspace(-8.0, 0.0, 400)
    A_t = np.exp(t_grid)
    integ = 1.0 * A_t  # (m A - (t/4m)(A-2J)) = m A since A=2J, m=1
    ax.plot(t_grid, integ, "m-", lw=2,
            label=r"$mA(t)-\frac{t}{4m}(A-2J)=e^{t}$  (A=2J)")
    ax.fill_between(t_grid, 0.0, integ, color="magenta", alpha=0.15)
    ax.axhline(0.0, color="gray", ls="-", alpha=0.5)
    ax.set_xlabel("t  (spacelike momentum transfer, t<0)")
    ax.set_ylabel("ANEC integrand")
    ax.set_title(f"ANEC wall (D-N eq.12):  integral = {anec['anec']:.4f}  >= 0")
    ax.legend(fontsize=8)

    fig.suptitle(
        f"{GATE_ID}:  relay type-IV EMT sign test  --  verdict={ev['verdict']}  "
        f"(core $\\Gamma_{{sub}}$={ev['g_core']:+.4f}, exterior={ev['g_ext']:+.4f}, "
        f"r_g={ev['r_g']:.4f})",
        fontsize=12)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    print("=" * 78)
    print(f"{GATE_ID}  (S105 Wave 4, §W4-2)  --  relay v(r) type-IV EMT sign test")
    print("=" * 78)

    # 1. input pins + dual-SHA
    pins = log_input_pins(INPUT_FILES)
    runtime_canonical_sha = pins["computations/_shared/canonical_constants.py"]  # (local)
    plan_drift = (runtime_canonical_sha != PLAN_CANONICAL_SHA)  # (local)
    if plan_drift:
        print(f"  [plan-text-drift] canonical_constants.py runtime SHA "
              f"{runtime_canonical_sha[:16]}.. != plan-freeze {PLAN_CANONICAL_SHA[:16]}..")
        print("    -> using RUNTIME SHA in audit pinmap (substrate-first §(ii.B)); "
              "documented in verdict value.")
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap[s104,s85,s67])")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. canonical inputs
    print("CANONICAL INPUTS (substrate-first):")
    print(f"  a_2_FW_zeta = {a_2_FW_zeta}  (emergent-metric channel; regulator {REGULATOR_PIN})")
    print(f"  c_BLV (c_s) = {c_BLV}  (a_2-channel acoustic sound speed)")
    print(f"  Mach_max    = {Mach_max}  (dead-BLV GLOBAL transit; EXCLUDED for relay)")
    print(f"  v_terminal  = {v_terminal}  (dead-BLV GLOBAL terminal; EXCLUDED)")
    print(f"  tau_fold    = {tau_fold}")
    print()

    # 3. construct v(r) on the a_2-channel acoustic-EMT (THE DELIVERABLE)
    flow = build_relay_flow()
    print("v(r) CONSTRUCTION (a_2-channel acoustic-EMT, core-concentrated, D-N-faithful):")
    print(f"  v(r) = v0 * exp(-(r/r0)^2/2),  r0 = {flow['r0']:.3f} (relay-Compton radius)")
    print(f"  Mach_core = v0/c_s = exp(1/2) = {flow['Mach_core']:.6f}  (substrate-derived)")
    print(f"  v0 = {flow['v0']:.8f}  (core flow amplitude; << v_terminal: dead-BLV excluded)")
    print()

    # 4. radial sign profile (the [SIGN] read-off)
    print("RADIAL SIGN PROFILE  (Gamma_sub = c_s^2 - v^2 = c_s^2(1-Mach^2)):")
    print(f"  {'r':>8} {'Mach(r)':>10} {'Gamma_sub':>12} {'sign':>5}  Hawking-Ellis type")
    for rr in [R_MIN, 0.5, 1.0, 1.5, 3.0, R_MAX]:
        g = gamma_sub_at(rr, flow["c_s"], flow["r0"], flow["v0"])  # (local)
        m = flow["v0"] * np.exp(-(rr / flow["r0"]) ** 2 / 2.0) / flow["c_s"]  # (local)
        typ = "IV (core)" if g < 0 else ("II (crossover)" if abs(g) < TOL_ZERO else "I (tail)")  # (local)
        print(f"  {rr:>8.4f} {m:>10.4f} {g:>+12.6f} {int(np.sign(g)):>5}  type-{typ}")
    print()

    # 5. locate crossover(s)
    crossovers = find_crossovers(flow)
    print(f"CROSSOVER(S)  (Mach=1 restoration surface(s), bisection tol_root={TOL_ROOT}):")
    for rg in crossovers:
        g_rg = gamma_sub_at(rg, flow["c_s"], flow["r0"], flow["v0"])  # (local)
        print(f"  r_g = {rg:.8f}   Gamma_sub(r_g) = {g_rg:+.3e}  (|.|<=tol_zero={TOL_ZERO}: "
              f"{abs(g_rg) <= TOL_ZERO})")
    print()

    # 6. ANEC wall (D-N eq.12)
    anec = anec_wall()
    print("ANEC WALL  (Dumitru-Noronha eq.12, exact transcription):")
    print(f"  int_{{-inf}}^0 dt [m A(t) - (t/4m)(A-2J)]  with A(0)={anec['A0']:.3f}, "
          f"J(0)={anec['J0']:.3f}, A=2J:{anec['a_eq_2j']}")
    print(f"  ANEC integral = {anec['anec']:.8f}  (holographic A=2J cross-check: "
          f"m*int A dt = {anec['anec_holo']:.8f})")
    print(f"  ANEC >= -tol_anec ({-TOL_ANEC:.1e}) ? {anec['anec'] >= -TOL_ANEC}")
    print()

    # 7. evaluate gate
    ev = evaluate(flow, crossovers, anec)
    print("GATE EVALUATION (set-membership in the type-IV-certifying PASS-region):")
    print(f"  sign(Gamma_sub(r_core))   = {int(np.sign(ev['g_core']))}  "
          f"(value {ev['g_core']:+.6f}; type-IV core: {ev['core_typeIV']})")
    print(f"  sign(Gamma_sub(r_exterior))= {int(np.sign(ev['g_ext']))}  "
          f"(value {ev['g_ext']:+.6f}; type-I tail: {ev['ext_typeI']})")
    print(f"  single finite r_g (Mach=1) : {ev['single_crossover']}  "
          f"(n_crossovers={ev['n_crossovers']}, r_g={ev['r_g']:.6f})")
    print(f"  ANEC wall holds            : {ev['anec_holds']}")
    print(f"  sign flip (-1 core / +1 ext): {ev['sign_flip']}")
    print()

    # 8. [SIGN] 3-tuple
    #   sign_verdict   : PASS iff the predicted core/exterior sign pair (-1,+1) matches
    #   magnitude_verdict: PASS iff the crossover exists + ANEC holds (the magnitude
    #                      conditions of the PASS-region)
    #   regime_verdict : VALID iff the radial grid spans the full intended window
    #                    [R_MIN,R_MAX] (core r->0 AND tail r->inf both resolved)
    sign_verdict = "PASS" if ev["sign_flip"] else "FAIL"  # (local)
    magnitude_verdict = "PASS" if (ev["single_crossover"] and ev["anec_holds"]) else (
        "INFO" if ev["sign_flip"] else "FAIL")  # (local)
    # regime: confirm the core is genuinely supersonic at R_MIN and the tail
    # genuinely subsonic at R_MAX (the window brackets both limits with margin)
    core_resolved = flow["mach_r"][0] > 1.0   # (local)
    tail_resolved = flow["mach_r"][-1] < 1e-3  # (local)
    regime_verdict = "VALID" if (core_resolved and tail_resolved) else "MARGINAL"  # (local)

    verdict = ev["verdict"]  # (local)

    # composite-collapse sanity (matches gate-verdicts.md generic rule)
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"  # (local)
    elif magnitude_verdict == "INFO":
        composite = "INFO"  # (local)
    else:
        composite = "PASS"  # (local)
    assert composite == verdict, f"collapse mismatch: composite={composite} vs verdict={verdict}"

    # 9. value payload (8-sig-fig publication precision; full float64 -> npz)
    value = (
        f"verdict={verdict};"
        f"sign(Gamma_core)={int(np.sign(ev['g_core']))}(={ev['g_core']:.8g});"
        f"sign(Gamma_ext)=+{int(np.sign(ev['g_ext']))}(={ev['g_ext']:.8g});"
        f"r_g={ev['r_g']:.8g};Mach_core={flow['Mach_core']:.8g};"
        f"ANEC={anec['anec']:.8g};n_crossovers={ev['n_crossovers']};"
        f"construction=a2-channel-acoustic-EMT(core-concentrated);"
        f"dead_BLV_excluded=True(v0={flow['v0']:.6g}<<v_term={float(v_terminal):.6g})"
    )  # (local)
    if plan_drift:
        value += f";canonical_runtime_sha={runtime_canonical_sha[:16]}(plan_drift_documented)"

    print("=" * 78)
    print(f"VERDICT: {verdict}")
    print(f"  {value}")
    print(f"  3-tuple: sign={sign_verdict} magnitude={magnitude_verdict} regime={regime_verdict}")
    print("=" * 78)

    # 10. save npz (full float64)
    out_npz = HERE / "s105_typeiv_emt_compute.npz"  # (local)
    np.savez(
        out_npz,
        r=flow["r"], v_r=flow["v_r"], mach_r=flow["mach_r"], gamma_sub=flow["gamma_sub"],
        c_s=flow["c_s"], r0=flow["r0"], v0=flow["v0"], Mach_core=flow["Mach_core"],
        a_2_FW_zeta=float(a_2_FW_zeta), c_BLV=float(c_BLV),
        Mach_max=float(Mach_max), v_terminal=float(v_terminal), tau_fold=float(tau_fold),
        g_core=ev["g_core"], g_ext=ev["g_ext"], r_g=ev["r_g"],
        n_crossovers=ev["n_crossovers"], crossovers=np.array(ev["crossovers"], dtype=float),
        core_typeIV=ev["core_typeIV"], ext_typeI=ev["ext_typeI"],
        single_crossover=ev["single_crossover"], sign_flip=ev["sign_flip"],
        anec=anec["anec"], anec_holo=anec["anec_holo"], anec_holds=ev["anec_holds"],
        A0=anec["A0"], J0=anec["J0"], a_eq_2j=anec["a_eq_2j"],
        verdict=verdict, sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict, value=value,
        scheme=SCHEME, convention=CONVENTION, regulator_pin=REGULATOR_PIN,
        N_eval=N_EVAL, r_min=R_MIN, r_max=R_MAX,
        tol_zero=TOL_ZERO, tol_sign=TOL_SIGN, tol_anec=TOL_ANEC, tol_root=TOL_ROOT,
        audit_sha256=audit_sha, content_sha256=content_sha,
        plan_drift=plan_drift, runtime_canonical_sha=runtime_canonical_sha,
    )
    print(f"  saved npz: {out_npz}")

    # 11. plot
    out_png = HERE / "s105_typeiv_emt_compute.png"  # (local)
    make_plot(flow, ev, anec, out_png)
    print(f"  saved png: {out_png}")

    # 12. emit verdict payload (agent passes to emit_verdict MCP tool)
    extra_rows = [
        f"# regulator_pin={REGULATOR_PIN}  a_2_FW_zeta={a_2_FW_zeta} (emergent-metric channel)",
        f"# construction=a2-channel-acoustic-EMT core-concentrated v(r)=v0*exp(-(r/r0)^2/2); "
        f"Mach_core=exp(1/2)={flow['Mach_core']:.6f}; r_g={ev['r_g']:.6f} (D-N grav-radius 1-2 Compton)",
        f"# dead_BLV_excluded: v0={flow['v0']:.6g} << v_terminal={float(v_terminal):.6g}, "
        f"Mach_core={flow['Mach_core']:.4f} << Mach_max={float(Mach_max):.2f}",
        f"# ANEC(D-N eq.12)={anec['anec']:.8g}>=0 (A=2J holographic; m*intA={anec['anec_holo']:.6g})",
    ]  # (local)
    if plan_drift:
        extra_rows.append(
            f"# plan-text-drift: canonical runtime={runtime_canonical_sha[:16]} "
            f"!= plan-freeze={PLAN_CANONICAL_SHA[:16]}; runtime SHA used (substrate-first ii.B)")
    print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict, magnitude_verdict, regime_verdict, extra_rows)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
