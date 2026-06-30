"""
S100b-X-C10-BBN-CONSTRAINT-RECONCILE  --  Wave 1 (einstein-theorist)  [VERIFY]

BBN-constraint adjudication (C10 dark-energy observational arm): exactly one of
the two canonical BBN constraints on the Volovik tracking vacuum
rho_vac = alpha_V * M_Pl^2 * H^{n_eff} is the operative falsifier --
  ROUTE B (S66): the G_eff-renormalization bound alpha(T_BBN) < 0.02
      (session-66-mack-transit-workshop.md L875-883: n_eff=2.3 -> alpha~0.01 PASS;
       n_eff<=2 EXCLUDED; relief from ABOVE),
  ROUTE A (S98/S99): the additive Delta_N_eff lever
      (rho_vac/rho_rad)_BBN = frac_base * exp((n_eff-2)*X), X = ln(H_BBN/H_0)
      (relief from BELOW; n_eff=2.3 excluded by ~6 OOM)
-- and the apparent opposite-direction conflict is resolved by recovering each
route's NORMALIZATION ANCHOR (pre-registered discriminator axis:
S66 = fold/transit-anchored alpha_V decay vs S98/S99 = z=0-anchored DILUTION-CC
transport), classifying the pair as one-operative-one-rescoped,
distinct-observables, or genuine canonical contradiction.

SUBSTRATE FRAMING (phononic-framing.md -- IS not IN):
  The a_0 Seeley-DeWitt zeroth spectral moment of D_K (a_0^{zeta} = 6440.0,
  zeta-regulated -- a DIFFERENT moment than gravity's a_2) IS the early vacuum;
  the Volovik tracking response rho_vac = alpha_V M_Pl^2 H^{n_eff} is its
  H-response. Flow: D_K eigenvalues -> a_0 zeroth moment -> tracking exponent
  n_eff -> modified-Friedmann image -> BBN observables. The G_eff(BBN) 2% bound
  and the Delta_N_eff lever are TWO laboratory-IN shadows of that ONE
  substrate-IS object. This gate adjudicates which shadow's falsifier binds the
  substrate's tracking response, and at which normalization anchor (fold vs z=0
  -- which end of the substrate's own history pins alpha_V). Neither S66 nor
  S98/S99 is treated as authority over the other: the unified exact chain is.

UNIFIED CONVENTION (single, declared once; every number below lives in it):
  (i)   tracking law: rho_vac(H) = alpha_V * M_Pl_red^2 * H^{n_eff},
        M_Pl_red = reduced Planck mass; rho_crit(H) = 3 M_Pl_red^2 H^2.
  (ii)  f := (rho_vac/rho_rad)_BBN  (the BBN vacuum-to-radiation fraction);
        alpha := rho_vac/rho_total = f/(1+f)  (vacuum fraction of TOTAL).
  (iii) Delta_N_eff = f / [(7/8)(4/11)^(4/3)]   (canonical S66 formula,
        session-66-mack-qa-workshop.md L767; bound factor computed exactly
        IN-SCRIPT at 50 dps -- never hardcoded).
  (iv)  n_eff sign convention: exponent on H (larger n_eff = faster dilution
        forward in time, since H decreases).
  (v)   normalization-anchor axis (THE pre-registered discriminator):
        z0-anchored  : alpha_V fixed by rho_vac(H_0) = rho_vac_over_rho_obs *
                       rho_obs (DILUTION-CC-66), transported UP to BBN;
        fold-anchored: alpha_V fixed upstream (transit side), decaying DOWN
                       to BBN as (H_BBN/H_anchor)^{n_eff-2}.

GATE: adjudication (4-class set outcome) + chain-residual inequality: every
  numerical step of the unified chain satisfies |computed-canonical|/|canonical|
  <= 1e-12 (50-dps exact arithmetic; float64 image only at publication).
  PASS/FAIL/INFO are all valid results; exit 0 regardless. Verdict is DATA.
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")   # cpu-cap-OMP8 pin (scalar algebra; no linear algebra)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib  # noqa: E402
import json     # noqa: E402
import sys      # noqa: E402
import time     # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np      # noqa: E402
import mpmath as mp     # noqa: E402

import matplotlib       # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# -----------------------------------------------------------------------------
# Section 1 -- Paths + canonical-constants import (MANDATORY)
# -----------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent                 # computations/session-100b
SHARED_DIR = SESSION_DIR.parent / "_shared"                   # computations/_shared
PROJECT_ROOT = SESSION_DIR.parent.parent                      # repo root
SESSION_DIR.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import (  # noqa: E402
    M_Pl_reduced,            # 2.435e18 GeV (reduced)
    T_BBN_GeV,               # 1e-3 GeV
    g_star_BBN,              # 10.75
    rho_vac_over_rho_obs,    # 1.032  (DILUTION-CC-66 z=0 normalization -- THE z0 anchor)
    rho_crit_GeV4,           # 4.08e-47 GeV^4
    H_0_GeV,                 # 1.438e-42 GeV
    z_BBN,                   # 4e8
    a_0_FW_zeta,             # 6440.0 (regulator pin a_0^{zeta})
    N_eff_SM,                # 3.044
)

GATE_ID = "S100b-X-C10-BBN-CONSTRAINT-RECONCILE"
SESSION = "100b"
SCHEME = "FW"
CONVENTION = "ABSOLUTE"
L_MAX = "N/A"          # no D_K truncation enters (lever + G_eff algebra on pinned spectral-moment outputs)
SCHEMA_VERSION = "S84+"

NPZ_OUT = SESSION_DIR / "s100b_x_c10_bbn_constraint_reconcile.npz"
PNG_OUT = SESSION_DIR / "s100b_x_c10_bbn_constraint_reconcile.png"

mp.mp.dps = 50  # 50-digit working precision ("Sage-exact" engine; Sage-MCP cross-checked agent-side)

# -----------------------------------------------------------------------------
# Section 2 -- Pre-registered machinery pins (plan SW1-1 machinery_pin_map)
# -----------------------------------------------------------------------------
CHAIN_RTOL = 1e-12                       # (local) pre-registered chain-residual tolerance (plan pin)
N_EFF_REFS = (1.978111, 2.0, 2.3)        # reference n_eff set (plan)
BUDGET_DNEFF_CANONICAL = 1.0             # (local) pre-registered canonical budget Delta_N_eff <= 1 (plan pin)
BUDGET_DNEFF_GH2026 = 0.107              # (local) EXTERNAL NON-CANONICAL plan pin (Goldstein-Hill 2026, arXiv
#                                          2603.13226, N_eff = 2.990 +/- 0.070 combined BBN+CMB+BAO, 95% CL;
#                                          promoted to canonical_constants via Step-2 update_constant AFTER
#                                          the verdict per math-scripts.md canonical write-order)
GEFF_ALPHA_BOUND = 0.02                  # (local) S66 pre-registered gate alpha(T_BBN) < 0.02 (G_eff within 2%)
ANCHOR_AXIS = ("fold-anchored", "z0-anchored")  # pre-registered discriminator axis
SCAN_LO, SCAN_HI = 1.85, 2.40            # diagnostic n_eff scan range (plan)
SCAN_STEP = 0.001                        # (local) plot resolution, not verdict-relevant
PUBLICATION_DP = 6                       # (local) 6-decimal publication images on crossing exponents
# S66 published table (recovered VERBATIM, session-66-mack-transit-workshop.md L877-879):
S66_TABLE = {
    "n_lt_2": {"n_eff": 1.78, "alpha_pub": ">0.67", "verdict": "EXCLUDED"},   # Mack Re:T3-Q3 estimate
    "n_eq_2": {"n_eff": 2.0, "alpha_pub": 0.67, "Geff_pub": 3.0, "verdict": "EXCLUDED"},
    "n_2p3": {"n_eff": 2.3, "alpha_pub": 0.01, "Geff_pub": 1.03, "verdict": "PASS"},
}

# -----------------------------------------------------------------------------
# Section 3 -- Input files (plan SW1-1 input_files; static SHAs verified)
# -----------------------------------------------------------------------------
PINNED = {
    "computations/session-98/s98_mk3_2_bbn_vacuum_fraction.npz":
        "c153d8d6f859a36d11a7bce0fd9e46e152c9989f7b12e0efc82b98f73d3bf8f7",
    "computations/session-98/s98_mk3_1_c10_subleading_sign.npz":
        "cb7462c8f3aef9e3a5dad9d3ed8e91dc2f2e09a9931166aa0258613b47be8255",
    "sessions/archive/session-66/session-66-mack-transit-workshop.md":
        "9c381b0a04ff7a1210f168a500bf4714f633ed103e351128d27b1dfc70926a34",
    "sessions/archive/session-66/session-66-mack-qa-workshop.md":
        "abdc6c601143435c51948293a17f52d3564db1572c630b69a189fea69f0c1f1d",
    "downloads/research-sweep-s99/dark-energy-observational/"
    "09_Allali-Notari-Rompineve_Dark-Radiation-DESI-Neff.pdf":
        "e76fe504fe6a453239dc0189efc0bc262a97749ef2d0ef472433360445c81747",
    "downloads/research-sweep-s99/dark-energy-observational/"
    "11_Goldstein-Hill_2pct-Neff-Determination.pdf":
        "13055d9f51bf2205ac72ced2d5d358a54f4e9e21b02e925dddaf57b8abe17618",
}
RUNTIME_INPUTS = [
    "computations/_shared/canonical_constants.py",
    "computations/session-99/s99_gate_verdicts.txt",   # read-only anchor recovery (S99-W2-BBN-RELIEF)
]


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    h.update(path.read_bytes())
    return h.hexdigest()


def build_pinmap() -> dict[str, str]:
    pins: dict[str, str] = {}  # (local)
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    for rel, expected in PINNED.items():
        sha = sha256_of(PROJECT_ROOT / rel)  # (local)
        status = "OK" if sha == expected else "MISMATCH"  # (local)
        print(f"  [{status}] {rel}: {sha[:16]}...")
        if sha != expected:
            raise RuntimeError(f"input SHA drift on {rel}: {sha} != plan pin {expected}")
        pins[rel] = sha
    for rel in RUNTIME_INPUTS:
        sha = sha256_of(PROJECT_ROOT / rel)  # (local)
        print(f"  [runtime] {rel}: {sha[:16]}...")
        pins[rel] = sha
    # gate-identity + pre-registered reference/budget/axis declarations enter the audit closure:
    pins["_gate_id"] = GATE_ID
    pins["_scheme"] = SCHEME
    pins["_convention"] = CONVENTION
    pins["_n_eff_refs"] = repr(list(N_EFF_REFS))
    pins["_budget_set"] = repr([BUDGET_DNEFF_CANONICAL, BUDGET_DNEFF_GH2026, GEFF_ALPHA_BOUND])
    pins["_anchor_axis"] = repr(list(ANCHOR_AXIS))
    return pins


def compute_dual_sha(pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = Path(__file__).resolve().read_bytes()                      # (local)
    canonical_bytes = (SHARED_DIR / "canonical_constants.py").read_bytes()    # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode()  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# -----------------------------------------------------------------------------
# Section 4 -- print_verdict_payload (race-safe emission: agent calls emit_verdict)
# -----------------------------------------------------------------------------
def print_verdict_payload(verdict: str, value: str, audit_sha: str, content_sha: str,
                          companion_note: str = "", extra_rows: list[str] | None = None) -> None:
    """Print the delimited JSON payload for the dispatching AGENT to pass to the
    knowledge-MCP `emit_verdict` tool (single, lock-serialized writer per
    gate-verdicts.md 'Race-Safe Emission'). This script does NOT write the
    verdict file. [VERIFY] trigger, schema_v2_3tuple_required: false (plan) --
    no sign/magnitude/regime 3-tuple."""
    payload = {  # (local)
        "session": SESSION,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": SCHEMA_VERSION,
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = extra_rows
    print("<<<EMIT_VERDICT_PAYLOAD>>>" + json.dumps(payload) + "<<<END_EMIT_VERDICT_PAYLOAD>>>")


# -----------------------------------------------------------------------------
# Section 5 -- helpers
# -----------------------------------------------------------------------------
def rel_resid(x_mp, x_ref: float) -> float:
    """Relative residual |x_mp - x_ref| / |x_ref| as float (x_mp at 50 dps)."""
    return float(abs(x_mp - mp.mpf(float(x_ref))) / abs(mp.mpf(float(x_ref))))  # (local)


def pub_ok(x: float, pin: float, tol: float) -> bool:
    """Publication-image reproduction at the pin's own precision (Class-8.3)."""
    return abs(x - pin) <= tol  # (local)


# -----------------------------------------------------------------------------
# Section 6 -- Main computation
# -----------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    pins = build_pinmap()  # (local)
    audit_sha, content_sha = compute_dual_sha(pins)  # (local)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    # --- load full-float64 lever inputs from the S98 npz (NEVER report-rounded) ---
    d2 = np.load(PROJECT_ROOT / "computations/session-98/s98_mk3_2_bbn_vacuum_fraction.npz",
                 allow_pickle=True)  # (local)
    d1 = np.load(PROJECT_ROOT / "computations/session-98/s98_mk3_1_c10_subleading_sign.npz",
                 allow_pickle=True)  # (local)
    npz = {k: float(d2[k]) for k in
           ["frac_base", "frac_below", "X", "log10_X", "n_eff", "exp_below", "relief_factor",
            "bound", "dNeff_below", "dNeff_base", "H_ratio", "H_BBN", "H0", "rho_vac_0",
            "rho_obs", "rho_rad_BBN", "g_star_BBN", "T_BBN", "M_Pl"]}  # (local)
    n_eff_mk31 = float(d1["n_eff_T61"])  # (local) cross-npz consistency
    a3_q0 = float(d1["cubic_coeff_q0_analytic"]) if "cubic_coeff_q0_analytic" in d1.files else float("nan")  # (local)
    assert npz["n_eff"] == n_eff_mk31, "n_eff mismatch between mk3_1 and mk3_2 npz"
    print("=== full-float64 lever inputs (s98_mk3_2 npz; display roundings are images only) ===")
    print(f"  n_eff      = {npz['n_eff']!r}   (mk3_1 n_eff_T61 identical; divergence_type="
          f"{str(d1['divergence_type'])}, well_conditioned={bool(d1['C_meas_well_conditioned'])}, "
          f"a3_q0_analytic={a3_q0:.4f})")
    print(f"  frac_base  = {npz['frac_base']!r}    (display 1.144730)")
    print(f"  X          = {npz['X']!r}    (display 40.2756)")
    print(f"  frac_below = {npz['frac_below']!r}   (display 0.474049)")
    print()

    # =========================================================================
    # PART A -- z0-anchored lever route (S98/S99), 50-dps recomputation from the
    #          canonical primitive pins; residual vs npz at EVERY step
    # =========================================================================
    residual_names: list[str] = []   # (local)
    residual_vals: list[float] = []  # (local)

    def step(name: str, x_mp, ref: float):
        r = rel_resid(x_mp, ref)  # (local)
        residual_names.append(name)
        residual_vals.append(r)
        print(f"  step {name:<14s}: mp50={mp.nstr(x_mp, 12):>18s}  npz={ref!r:>24s}  resid={r:.3e}")
        return r

    print("=== PART A: unified chain, 50-dps recompute vs npz (tolerance 1e-12 per step) ===")
    # Definition chain (canonical primitive pins -> lever):
    bound_mp = (mp.mpf(7) / 8) * (mp.mpf(4) / 11) ** (mp.mpf(4) / 3)          # (local) exact bound factor
    rho_vac_0_mp = mp.mpf(rho_vac_over_rho_obs) * mp.mpf(rho_crit_GeV4)       # (local) z0 ANCHOR (DILUTION-CC)
    rho_rad_mp = mp.pi ** 2 / 30 * mp.mpf(g_star_BBN) * mp.mpf(T_BBN_GeV) ** 4  # (local)
    H_BBN_mp = mp.sqrt(rho_rad_mp / (3 * mp.mpf(M_Pl_reduced) ** 2))          # (local) rad-dom Friedmann
    Hr_mp = H_BBN_mp / mp.mpf(H_0_GeV)                                        # (local)
    X_mp = mp.log(Hr_mp)                                                      # (local) epoch lever
    n_eff_mp = mp.mpf(npz["n_eff"])                                           # (local) substrate pin (HARD from-below)
    relief_mp = Hr_mp ** (n_eff_mp - 2)                                       # (local)
    relief_exp_form = mp.exp((n_eff_mp - 2) * X_mp)                           # (local) equivalence form
    frac_base_mp = rho_vac_0_mp * Hr_mp ** 2 / rho_rad_mp                     # (local)
    frac_base_identity = rho_vac_0_mp / (3 * mp.mpf(M_Pl_reduced) ** 2 * mp.mpf(H_0_GeV) ** 2)  # (local)
    frac_below_mp = frac_base_mp * relief_mp                                  # (local)
    dNeff_mp = frac_below_mp / bound_mp                                       # (local)
    dNeff_base_mp = frac_base_mp / bound_mp                                   # (local)

    step("bound", bound_mp, npz["bound"])
    step("rho_vac_0", rho_vac_0_mp, npz["rho_vac_0"])
    step("rho_rad_BBN", rho_rad_mp, npz["rho_rad_BBN"])
    step("H_BBN", H_BBN_mp, npz["H_BBN"])
    step("H_ratio", Hr_mp, npz["H_ratio"])
    step("X", X_mp, npz["X"])
    step("relief_factor", relief_mp, npz["relief_factor"])
    step("frac_base", frac_base_mp, npz["frac_base"])
    step("frac_below", frac_below_mp, npz["frac_below"])
    step("dNeff_below", dNeff_mp, npz["dNeff_below"])
    step("dNeff_base", dNeff_base_mp, npz["dNeff_base"])
    # internal exactness checks (form equivalences; residual vs own mp twin):
    r_eq1 = float(abs(relief_mp - relief_exp_form) / relief_mp)               # (local) pow vs exp form
    r_eq2 = float(abs(frac_base_mp - frac_base_identity) / frac_base_mp)      # (local) z0-anchor identity
    residual_names += ["relief_pow_vs_exp", "frac_base_z0_identity"]
    residual_vals += [r_eq1, r_eq2]
    print(f"  identity relief: pow vs exp form          resid={r_eq1:.3e}")
    print(f"  identity frac_base == rho_vac_0/rho_crit(H_0,M_Pl) [z0 anchor manifest] resid={r_eq2:.3e}")
    max_resid = max(residual_vals)  # (local)
    chain_ok = bool(max_resid <= CHAIN_RTOL)  # (local)
    print(f"  MAX chain residual = {max_resid:.3e}  (tolerance {CHAIN_RTOL:.0e})  -> "
          f"{'OK' if chain_ok else 'VIOLATION'}")
    print()

    # --- publication-image reproductions (Class-8.3 precision images) ---
    print("=== publication-image reproductions (each at its pin's own precision) ===")
    f_bound = float(bound_mp)        # (local)
    f_below = float(frac_below_mp)   # (local)
    f_base = float(frac_base_mp)     # (local)
    f_relief = float(relief_mp)      # (local)
    f_dNeff = float(dNeff_mp)        # (local)
    f_X = float(X_mp)                # (local)
    repro = {  # (local)
        "frac_below_0.474049": (f_below, 0.474049, 1e-6),
        "dNeff_2.0873": (f_dNeff, 2.0873, 1e-4),
        "relief_0.414115": (f_relief, 0.414115, 1e-6),
        "bound_0.227107": (f_bound, 0.227107, 1e-6),
        "X_40.2756": (f_X, 40.2756, 1e-4),
        "frac_base_1.144730": (f_base, 1.144730, 1e-6),
    }
    repro_flags = {}  # (local)
    for name, (x, pin, tol) in repro.items():
        ok = pub_ok(x, pin, tol)  # (local)
        repro_flags[name] = ok
        print(f"  [{'OK' if ok else 'X'}] {name:<24s} computed={x:.8f}  pin={pin}  tol={tol:.0e}")
    # the two prior roundings of the SAME exact bound (plan footnote):
    bound_img_verdict = round(f_bound, 6)                       # (local) 0.227107 (S99 verdict-line image)
    bound_img_provenance = round(0.474049 / 2.0873, 6)          # (local) 0.227113 (provenance back-derivation image)
    print(f"  bound images: exact(50dps)={mp.nstr(bound_mp, 10)} -> verdict-line image {bound_img_verdict}; "
          f"provenance image 0.474049/2.0873 = {bound_img_provenance} (both Class-8.3 images, neither hardcoded)")
    # einstein-R3 rounded-input relief image:
    relief_rounded_inputs = float(mp.exp(mp.mpf("-0.021889") * mp.mpf("40.2756")))  # (local)
    print(f"  relief images: full-float64 -> {f_relief:.6f} (S98/S99 image 0.414115); "
          f"rounded-input exp(-0.021889*40.2756) = {relief_rounded_inputs:.6f} (einstein-R3 image 0.414123)")
    # a-exponent baseline (radiation era H ~ a^-2): fraction ~ a^{2(2-n_eff)}
    a_exponent = float(2 * (2 - n_eff_mp))  # (local)
    print(f"  a-exponent baseline: fraction ~ a^(2(2-n_eff)) = a^(+{a_exponent:.6f}) (plan +0.043778)")
    print()

    # --- crossing solves (publication 6-decimal images; downstream rel_tol >= 1e-6) ---
    print("=== crossing solves (z0-anchored lever; 50 dps; 6-decimal publication) ===")
    n1_mp = 2 + mp.log(bound_mp / frac_base_mp) / X_mp                                    # (local) dNeff = 1
    n2_mp = 2 + mp.log(mp.mpf("0.107") * bound_mp / frac_base_mp) / X_mp                  # (local) dNeff = 0.107
    f_2pct_mp = mp.mpf(GEFF_ALPHA_BOUND) / (1 - mp.mpf(GEFF_ALPHA_BOUND))                 # (local) alpha=0.02 -> f
    n3_mp = 2 + mp.log(f_2pct_mp / frac_base_mp) / X_mp                                   # (local) G_eff 2%
    dNeff_2pct = float(f_2pct_mp / bound_mp)                                              # (local)
    n1, n2, n3 = float(n1_mp), float(n2_mp), float(n3_mp)  # (local)
    print(f"  n_eff(dNeff=1)      = {n1:.6f}   [plan-chain image 1.959838; S99 verdict image 1.959839]")
    print(f"  n_eff(dNeff=0.107)  = {n2:.6f}   [plan-chain image 1.904349]")
    print(f"  n_eff(Geff 2%)      = {n3:.6f}   [alpha<0.02 <=> f<{float(f_2pct_mp):.6f} <=> "
          f"dNeff<{dNeff_2pct:.6f}]")
    cross_ok = (pub_ok(n1, 1.959838, 2e-6) or pub_ok(n1, 1.959839, 2e-6)) and \
               (pub_ok(n2, 1.904349, 2e-6) or pub_ok(n2, 1.904348, 2e-6))  # (local)
    print(f"  crossing reproduction within rel_tol 1e-6 of prior images: {cross_ok}")
    print()

    # --- lever evaluations at the reference set ---
    print("=== lever route at reference n_eff set (z0-anchored) ===")
    lever_refs = {}  # (local)
    for n_ref in N_EFF_REFS:
        f_n = float(frac_base_mp * mp.exp((mp.mpf(n_ref) - 2) * X_mp))   # (local)
        dN_n = f_n / f_bound                                              # (local)
        oom = float(mp.log10(mp.mpf(f_n) / bound_mp)) if f_n > f_bound else float("nan")  # (local)
        lever_refs[n_ref] = (f_n, dN_n, oom)
        print(f"  n_eff={n_ref:<9}: f={f_n:.6e}  dNeff={dN_n:.6e}  "
          f"{'EXCEEDS bound by ' + format(oom, '.2f') + ' OOM' if f_n > f_bound else 'within bound'}")
    frac23_lever = lever_refs[2.3][0]   # (local)
    dNeff23_lever = lever_refs[2.3][1]  # (local)
    oom23_lever = lever_refs[2.3][2]    # (local)
    print()

    # =========================================================================
    # PART B -- G_eff route (S66) under the unified convention
    # =========================================================================
    print("=== PART B: G_eff route -- same-observable identity + anchor recovery ===")
    # (B.1) EXACT identity: G_eff/G = 1/(1-alpha) == 1+f  (alpha = f/(1+f))
    #   Substitution chain: alpha := rho_vac/rho_total = f/(1+f)
    #     => 1 - alpha = 1 - f/(1+f) = 1/(1+f)  =>  1/(1-alpha) = 1+f.   QED (exact)
    id_dev = 0.0  # (local)
    for f_test in [1e-4, 0.02, 0.0204, 0.227, 0.474, 0.67, 2.0, 2.03e5]:
        fm = mp.mpf(f_test)  # (local)
        lhs = 1 / (1 - fm / (1 + fm))  # (local)
        rhs = 1 + fm                   # (local)
        id_dev = max(id_dev, float(abs(lhs - rhs) / rhs))
    same_observable_exact = bool(id_dev <= CHAIN_RTOL)  # (local)
    print(f"  identity 1/(1-alpha) == 1+f : max dev = {id_dev:.3e} over 8 samples -> "
          f"SAME observable (BBN expansion-rate shift H^2/H_std^2): {same_observable_exact}")
    print("  => the 'G-renormalization vs additive-N_eff' distinction is a VARIABLE CHANGE,")
    print("     not a different observable; Delta_N_eff is the conventional unit of the SAME H^2 shift.")
    print()

    # (B.2) direction under each anchor (the pre-registered discriminator):
    #   unified law: f(BBN) = f_anchor * (H_BBN/H_anchor)^(n_eff-2)
    #   d ln f / d n_eff = ln(H_BBN/H_anchor)
    #     z0 anchor      (H_anchor = H_0  << H_BBN): slope = +X = +40.2756 > 0 -> relief from BELOW
    #     upstream anchor (H_anchor >> H_BBN):        slope < 0               -> relief from ABOVE
    slope_z0 = f_X  # (local)
    print(f"  direction(z0 anchor):       d ln f/d n_eff = +X = +{slope_z0:.4f} > 0  -> SMALLER n_eff relieves")
    print(f"  direction(upstream anchor): d ln f/d n_eff = ln(H_BBN/H_anchor) < 0    -> LARGER n_eff relieves")
    print("  S66 published table direction (n=2.3 relieves; n<2 worsens) REQUIRES an upstream anchor;")
    print("  S66 published BASELINE 0.67 is z0-derived (qa L817: PRESENT-DAY seesaw extrapolated).")
    print("  => the S66 three-row table MIXES anchors across rows (n=2 row is anchor-degenerate).")
    print()

    # (B.3) reproduce the S66 published rows under the unified convention:
    print("=== S66 table reproduction under unified convention ===")
    # n=2 row: anchor-degenerate (f ~ H^0). Published alpha(BBN)=0.67 with 'G_eff = 3G':
    G_f_reading = 1 + 0.67            # (local) f-reading (f = rho_vac/rho_rad = 0.67, the W1-A definition)
    G_alpha_reading = 1 / (1 - 0.67)  # (local) alpha-reading (alpha = rho_vac/rho_total = 0.67)
    print(f"  n=2 row: f-reading G_eff/G = 1+0.67 = {G_f_reading:.4f}; "
          f"alpha-reading G_eff/G = 1/(1-0.67) = {G_alpha_reading:.4f} (published '3G' -> alpha-reading)")
    print("    => S66 plugged the f-valued 0.67 (W1-A: rho_vac/rho_rad) into the alpha-slot of T.4;")
    print("       under the unified convention f=0.67 gives 1.67G. BOTH readings >> 1.02 => row verdict")
    print("       EXCLUDED is convention-ROBUST (the slip moves no verdict).")
    dNeff_067 = 0.67 / f_bound  # (local)
    print(f"    qa-conversion images of the same row: exact 0.67/bound = {dNeff_067:.4f} "
          f"(qa L769 '2.95' REPRODUCED); qa L869 '1.34' = 2*0.67 (early-turn slip, superseded in-session);")
    inv_bound = float(1 / bound_mp)  # (local)
    print(f"    qa L31 '(8/7)(11/4)^(4/3) ~ 5.68' -> exact value = {inv_bound:.4f} = 1/bound "
          f"(formula correct, '5.68' an arithmetic slip; canonical L767 uses /0.227 correctly).")
    # canonical-normalization update of the same row (W1-A seesaw 0.67 -> DILUTION-CC 1.1447):
    print(f"    canonical z0 normalization updates the n=2 row magnitude: f = {f_base:.6f} "
          f"(dNeff = {float(dNeff_base_mp):.4f}); W1-A-era 0.67 (dNeff 2.95) is the older seesaw image."
          f" Factor {f_base/0.67:.4f}; EXCLUDED either way.")
    print()
    # n=2.3 row: published alpha ~ 0.01 PASS. Under z0 anchor the lever gives frac23_lever.
    disc23 = frac23_lever / S66_TABLE["n_2p3"]["alpha_pub"]  # (local) route discrepancy at 2.3
    print(f"  n=2.3 row: published '~0.01 PASS' vs z0-anchored lever f = {frac23_lever:.4e}")
    print(f"    implied-fraction DISCREPANCY between routes at n_eff=2.3: {disc23:.4e}x  (plan '~2e7x')")
    # implied anchor of the published 2.3 row (solve 0.67*(H_BBN/H_a)^0.3 = 0.01):
    lnHa = float(mp.log(mp.mpf("0.67") / mp.mpf("0.01")) / mp.mpf("0.3"))  # (local) ln(H_a/H_BBN)
    oom_Ha = lnHa / float(mp.log(10))  # (local)
    print(f"    implied anchor: ln(H_a/H_BBN) = ln(67)/0.3 = {lnHa:.4f} -> {oom_Ha:.3f} OOM above H_BBN")
    print(f"    (T ~ {10**(oom_Ha/2)*1e-3:.1f} GeV epoch -- NOT the fold, which sits tens of OOM above;")
    print("     the published '~0.01' is an OOM-rough estimate; a TRUE fold transport gives far smaller f")
    print("     and a correspondingly LARGER CC miss -- the conclusion below is monotone in anchor height.)")
    # (B.4) the CC cost of the S66 escape: continue the SAME law to z=0.
    #   f(BBN) scales linearly in alpha_V at fixed n_eff => alpha_V^{S66}/alpha_V^{z0} = f_S66/f_lever
    #   => rho_vac(z=0)|S66 = rho_vac_over_rho_obs * rho_obs * (f_S66/f_lever)
    cc_ratio = rho_vac_over_rho_obs * (S66_TABLE["n_2p3"]["alpha_pub"] / frac23_lever)  # (local)
    cc_miss_oom = float(-mp.log10(mp.mpf(cc_ratio)))  # (local)
    print(f"  CC boundary condition at z=0 under the S66 n=2.3 escape:")
    print(f"    rho_vac(z=0)/rho_obs = 1.032 * (0.01/{frac23_lever:.4e}) = {cc_ratio:.4e}")
    print(f"    => the escape UNDERSHOOTS the observed CC by {cc_miss_oom:.2f} OOM")
    # exact linearity identity: disc23 * cc_ratio == rho_vac_over_rho_obs
    id2_dev = abs(disc23 * cc_ratio - rho_vac_over_rho_obs) / rho_vac_over_rho_obs  # (local)
    residual_names.append("disc_x_ccratio_identity")
    residual_vals.append(float(id2_dev))
    max_resid = max(residual_vals)  # (local)
    chain_ok = bool(max_resid <= CHAIN_RTOL)  # (local)
    print(f"    linearity identity disc * cc_ratio == rho_vac_over_rho_obs: dev = {id2_dev:.3e}")
    print("    (anchor transport commutes with the power law: the inter-route BBN discrepancy IS the")
    print("     z=0 CC-miss factor -- one number measured at two ends.)")
    # n<2 row under the implied upstream anchor (direction reproduction):
    f_lt2_implied = 0.67 * float(mp.exp(-(mp.mpf("1.78") - 2) * mp.mpf(lnHa)))  # (local)
    f_pin_implied = 0.67 * float(mp.exp(-(n_eff_mp - 2) * mp.mpf(lnHa)))        # (local)
    print(f"  n<2 row: upstream-anchored f(1.78) = {f_lt2_implied:.4f} > 0.67 "
          f"(reproduces '>0.67 EXCLUDED'); f({npz['n_eff']:.6f}) = {f_pin_implied:.4f} > 0.67")
    print()

    # =========================================================================
    # ADJUDICATION (pre-registered 4-class rubric)
    # =========================================================================
    print("=== ADJUDICATION ===")
    # (1) distinct observables?  NO -- exact identity (B.1).
    distinct_observables = not same_observable_exact  # (local)
    # (2) genuine contradiction? Same observable + same convention + opposite directions?
    #     Under ONE anchor both forms give the SAME direction (they are the same observable);
    #     the published opposite directions live at OPPOSITE anchors. Resolvable => NO.
    genuine_contradiction = False if same_observable_exact else True  # (local)
    # (3) which anchor is substrate-justified for the DILUTION-CC tracking vacuum?
    #     z=0: (i) DILUTION-CC-66 fixes alpha_V by rho_vac(H_0)/rho_obs = 1.032 -- the mechanism's
    #          defining empirical content (sole surviving CC route);
    #     (ii) the tracking law is an ATTRACTOR (Volovik Gibbs-Duhem response; beta-relaxation
    #          Gamma_fabric/H ~ 1e43, S66 qa L40-42): alpha_V is the equilibrium-response
    #          coefficient, NOT an initial condition propagated from the fold -- fold-anchoring
    #          contradicts the attractor character that justifies the law in the first place;
    #     (iii) quantitatively, the fold-anchored escape (n=2.3 PASS row) costs >= cc_miss_oom OOM
    #          of present-day CC -- it solves BBN by un-solving the CC (re-opening the 114-OOM gap).
    #     => OPERATIVE = z0-anchored lever; S66 route RESCOPED:
    #        (a) its G_eff FORM is retained as the exact unit-conversion of the same observable
    #            (and its 2% bound maps to the TIGHTEST budget, dNeff <= dNeff_2pct);
    #        (b) its three-row n_eff TABLE is rescoped as a fold-anchored boundary-value question
    #            (anchor-mixed as published; not an escape available to the DILUTION-CC mechanism).
    outcome = ("OPERATIVE-LEVER+G_EFF-RESCOPED" if (chain_ok and same_observable_exact
               and not genuine_contradiction) else
               ("GENUINE-CONTRADICTION" if genuine_contradiction else "DISTINCT-OBSERVABLES-BOTH-OPERATIVE"))  # (local)
    repro_all = all(repro_flags.values()) and cross_ok  # (local)
    verdict = "PASS" if (outcome == "OPERATIVE-LEVER+G_EFF-RESCOPED" and chain_ok and repro_all) else \
              ("FAIL" if outcome == "GENUINE-CONTRADICTION" else "INFO")  # (local)
    print(f"  distinct_observables       = {distinct_observables}")
    print(f"  genuine_contradiction      = {genuine_contradiction}")
    print(f"  chain_ok (<=1e-12)         = {chain_ok}  (max resid {max_resid:.3e})")
    print(f"  reproductions_ok           = {repro_all}")
    print(f"  OUTCOME = {outcome}")
    print(f"  VERDICT = {verdict}")
    print()
    print("  CONSTRAINT-SCOPE STATEMENT (cited by W1-2):")
    print(f"    Operative falsifier: z0-anchored lever f = frac_base*exp((n_eff-2)*X) with the")
    print(f"    canonical conversion dNeff = f/bound; budgets dNeff <= {{1 (canonical),")
    print(f"    0.107 (GH-2026 EXTERNAL), {dNeff_2pct:.4f} (Cyburt-2016 G_eff-2% EXTERNAL)}} <=>")
    print(f"    n_eff <= {{{n1:.6f}, {n2:.6f}, {n3:.6f}}}. Substrate pin n_eff = {npz['n_eff']:.6f}")
    print(f"    (HARD from-below) exceeds ALL three crossings => the standing S98/S99 FAILs are")
    print(f"    confirmed at their proper scope (dNeff = {f_dNeff:.4f}, {f_dNeff/1.0:.4f}x canonical,")
    print(f"    {f_dNeff/0.107:.2f}x external). Relief inside the tracking family requires n_eff below")
    print(f"    the crossings; the remaining relief route is a NON-TRACKING epoch profile (W1-2).")
    print(f"    The S66 G_eff route is RESCOPED, not retired: form = exact unit-conversion (tightest")
    print(f"    budget); table = fold-anchored boundary-value question costing >= {cc_miss_oom:.2f} OOM")
    print(f"    of present-day CC at n_eff = 2.3.")
    print()

    # =========================================================================
    # Diagnostic curves + plot (n_eff in [1.85, 2.40], step 0.001)
    # =========================================================================
    n_grid = np.arange(SCAN_LO, SCAN_HI + SCAN_STEP / 2, SCAN_STEP)  # (local)
    f_lever_grid = f_base * np.exp((n_grid - 2.0) * f_X)             # (local) z0-anchored
    dNeff_lever_grid = f_lever_grid / f_bound                        # (local)
    alpha_lever_grid = f_lever_grid / (1.0 + f_lever_grid)           # (local) same-observable alpha image
    f_s66_grid = 0.67 * np.exp(-(n_grid - 2.0) * lnHa)               # (local) implied upstream-anchored

    fig, ax = plt.subplots(figsize=(11.5, 7.0))
    ax.semilogy(n_grid, f_lever_grid, "-", color="C0", lw=2.2,
                label=r"ROUTE A (operative): z0-anchored lever  $f=f_{base}e^{(n-2)X}$, $X=+40.2756$")
    ax.semilogy(n_grid, f_s66_grid, "--", color="C1", lw=2.0,
                label=r"ROUTE B (rescoped): S66-implied upstream anchor  $0.67\,e^{-(n-2)\cdot 14.016}$")
    ax.axhline(f_bound, color="C3", ls="-", lw=1.4,
               label=rf"canonical bound $f=0.227107$ ($\Delta N_{{eff}}=1$)")
    ax.axhline(0.107 * f_bound, color="C4", ls="-.", lw=1.2,
               label=rf"external GH-2026 $f={0.107*f_bound:.6f}$ ($\Delta N_{{eff}}=0.107$)")
    ax.axhline(float(f_2pct_mp), color="C5", ls=":", lw=1.4,
               label=rf"S66 $G_{{eff}}$-2% gate $f={float(f_2pct_mp):.6f}$ ($\Delta N_{{eff}}={dNeff_2pct:.4f}$)")
    for nc, lab, col in [(n1, f"n={n1:.6f}", "C3"), (n2, f"n={n2:.6f}", "C4"), (n3, f"n={n3:.6f}", "C5")]:
        ax.axvline(nc, color=col, ls="--", lw=0.9, alpha=0.6)
        ax.text(nc, 2e-7, lab, rotation=90, fontsize=7.5, ha="right", va="bottom", color=col)
    # reference points
    ax.plot([npz["n_eff"]], [f_below], "o", color="C0", ms=11, zorder=5,
            label=rf"substrate pin $n_{{eff}}=1.978111$: $f=0.474049$ ($\Delta N_{{eff}}=2.0873$) FAIL")
    ax.plot([2.0], [f_base], "s", color="C0", ms=9, zorder=5,
            label=rf"$n=2$ (z0): $f={f_base:.4f}$;  S66 W1-A image $0.67$")
    ax.plot([2.0], [0.67], "s", color="C1", ms=9, zorder=5)
    ax.plot([2.3], [frac23_lever], "^", color="C0", ms=10, zorder=5,
            label=rf"$n=2.3$ lever: $f={frac23_lever:.3e}$ ({oom23_lever:.2f} OOM over bound)")
    ax.plot([2.3], [0.01], "v", color="C1", ms=10, zorder=5,
            label=rf"$n=2.3$ S66 row: $f\sim 0.01$ 'PASS'  $\Rightarrow$ routes differ {disc23:.2e}x")
    ax.annotate("", xy=(2.3, frac23_lever), xytext=(2.3, 0.01),
                arrowprops=dict(arrowstyle="<->", color="0.3", lw=1.3))
    ax.text(2.307, 35.0, f"{disc23:.2e}x\n= CC-miss factor\n({cc_miss_oom:.2f} OOM at z=0)",
            fontsize=8.5, color="0.25")
    ax.set_xlabel(r"tracking exponent $n_{eff}$  ($\rho_{vac}=\alpha_V M_{Pl}^2 H^{n_{eff}}$)")
    ax.set_ylabel(r"$f=(\rho_{vac}/\rho_{rad})_{BBN}$")
    ax.set_xlim(SCAN_LO, SCAN_HI)
    ax.set_ylim(1e-7, 1e7)
    ax.grid(True, which="both", alpha=0.22)
    ax.set_title(f"{GATE_ID}\n"
                 f"both routes on ONE axis: identical observable (1+f == 1/(1-alpha) exact), "
                 f"OPPOSITE anchors (z0 vs upstream)\n"
                 f"outcome = {outcome}  |  chain resid max = {max_resid:.2e}  |  verdict = {verdict}",
                 fontsize=10)
    ax.legend(fontsize=7.6, loc="upper left", framealpha=0.95)
    fig.tight_layout()
    fig.savefig(PNG_OUT, dpi=140)
    plt.close(fig)
    print(f"  plot -> {PNG_OUT.relative_to(PROJECT_ROOT)}")

    # =========================================================================
    # npz output
    # =========================================================================
    np.savez(
        NPZ_OUT,
        gate_id=GATE_ID, verdict=verdict, outcome=outcome,
        # unified-convention chain (full float64 images of the 50-dps chain):
        bound=f_bound, frac_base=f_base, frac_below=f_below, relief_factor=f_relief,
        dNeff_below=f_dNeff, dNeff_base=float(dNeff_base_mp), X=f_X,
        H_BBN=float(H_BBN_mp), H_ratio=float(Hr_mp), rho_vac_0=float(rho_vac_0_mp),
        rho_rad_BBN=float(rho_rad_mp), n_eff=npz["n_eff"], a_exponent_baseline=a_exponent,
        # 50-dps decimal strings (audit):
        bound_dps50=mp.nstr(bound_mp, 50), frac_base_dps50=mp.nstr(frac_base_mp, 50),
        frac_below_dps50=mp.nstr(frac_below_mp, 50), X_dps50=mp.nstr(X_mp, 50),
        n1_dps50=mp.nstr(n1_mp, 50), n2_dps50=mp.nstr(n2_mp, 50), n3_dps50=mp.nstr(n3_mp, 50),
        # chain residuals:
        residual_names=np.array(residual_names), residual_values=np.array(residual_vals),
        max_chain_residual=max_resid, chain_rtol=CHAIN_RTOL, chain_ok=chain_ok,
        # crossings + budgets:
        n_cross_dNeff1=n1, n_cross_GH0107=n2, n_cross_Geff2pct=n3,
        budget_dNeff_canonical=BUDGET_DNEFF_CANONICAL, budget_dNeff_GH2026=BUDGET_DNEFF_GH2026,
        geff_alpha_bound=GEFF_ALPHA_BOUND, f_2pct=float(f_2pct_mp), dNeff_2pct=dNeff_2pct,
        # route comparison at the reference set:
        n_eff_refs=np.array(N_EFF_REFS),
        lever_f_refs=np.array([lever_refs[n][0] for n in N_EFF_REFS]),
        lever_dNeff_refs=np.array([lever_refs[n][1] for n in N_EFF_REFS]),
        frac23_lever=frac23_lever, dNeff23_lever=dNeff23_lever, oom23_lever=oom23_lever,
        s66_alpha_2p3=S66_TABLE["n_2p3"]["alpha_pub"], disc23=disc23,
        cc_ratio_s66_2p3=cc_ratio, cc_miss_oom=cc_miss_oom, lnHa_implied=lnHa, oom_Ha_implied=oom_Ha,
        f_lt2_implied=f_lt2_implied, f_pin_implied=f_pin_implied,
        # S66 row reproductions (unified convention):
        G_f_reading_n2=G_f_reading, G_alpha_reading_n2=G_alpha_reading, dNeff_067=dNeff_067,
        inv_bound=inv_bound, frac_base_over_067=f_base / 0.67,
        # identity checks:
        identity_dev_geff_additive=id_dev, same_observable_exact=same_observable_exact,
        identity_dev_disc_ccratio=float(id2_dev),
        # adjudication booleans:
        distinct_observables=distinct_observables, genuine_contradiction=genuine_contradiction,
        slope_z0=slope_z0, repro_all=repro_all,
        # diagnostic curves (both routes vs n_eff):
        n_grid=n_grid, f_lever_grid=f_lever_grid, dNeff_lever_grid=dNeff_lever_grid,
        alpha_lever_grid=alpha_lever_grid, f_s66_implied_grid=f_s66_grid,
        # rounding-image documentation:
        bound_img_verdict=bound_img_verdict, bound_img_provenance=bound_img_provenance,
        relief_rounded_inputs=relief_rounded_inputs,
        # provenance:
        audit_sha256=audit_sha, content_sha256=content_sha,
        a_0_FW_zeta=a_0_FW_zeta, N_eff_SM=N_eff_SM, z_BBN=float(z_BBN),
        rho_vac_over_rho_obs=rho_vac_over_rho_obs,
    )
    print(f"  npz  -> {NPZ_OUT.relative_to(PROJECT_ROOT)}")
    print()

    # =========================================================================
    # Verdict payload (agent calls emit_verdict; script never writes the file)
    # =========================================================================
    value_str = (  # (local)
        f"outcome={outcome};same_observable=EXACT(1+f==1/(1-alpha),dev={id_dev:.1e});"
        f"dir_conflict=anchor-axis(z0_slope=+{slope_z0:.4f}_vs_upstream_slope<0);"
        f"operative=z0_lever(DILUTION-CC_rho_vac/rho_obs=1.032);"
        f"rescoped=S66_table(fold-BVP;anchor-mixed;CC_miss={cc_miss_oom:.2f}OOM_at_n2.3);"
        f"Geff_form_retained=tightest_budget(dNeff<={dNeff_2pct:.4f});"
        f"n_cross_dNeff1={n1:.6f};n_cross_GH0.107={n2:.6f};n_cross_Geff2pct={n3:.6f};"
        f"lever_2.3=f{frac23_lever:.3e}(dNeff{dNeff23_lever:.2e};{oom23_lever:.2f}OOM);"
        f"disc_2.3={disc23:.2e}x;n_eff_pin={npz['n_eff']:.6f};dNeff_canonical={f_dNeff:.4f}_stands;"
        f"chain_resid_max={max_resid:.2e}"
    )
    companion_note = (  # (local)
        "[VERIFY] BBN two-route adjudication: G_eff(2%) and Delta_N_eff lever are the SAME "
        "observable (exact identity); opposite published n_eff directions = opposite normalization "
        "anchors (S66 fold-side BVP vs S98/S99 z0 DILUTION-CC); operative falsifier = z0 lever"
    )
    extra_rows = [  # (local)
        (f"# regulator_pin=a_0^{{zeta}} CLASS=N/A_no_SCHEMATIC_helper # {GATE_ID} rho_vac is the "
         f"a_0-channel tracking vacuum (a_0_FW_zeta={a_0_FW_zeta}, zeta-regulated zeroth "
         f"Seeley-DeWitt moment); CC=a_0 is a DIFFERENT moment than gravity a_2; "
         f"regulator-pin-discipline.md"),
        (f"# constraint_scope(W1-2): operative falsifier = z0-anchored lever "
         f"f=frac_base*exp((n_eff-2)X), dNeff=f/0.22710732(exact); budgets dNeff<="
         f"{{1(canonical), 0.107(GH-2026 arXiv2603.13226 EXTERNAL), {dNeff_2pct:.4f}"
         f"(Cyburt-2016 Geff-2pct EXTERNAL)}} <=> n_eff<={{{n1:.6f},{n2:.6f},{n3:.6f}}}; "
         f"substrate pin n_eff=1.978111 (HARD from-below) exceeds ALL => standing S98/S99 FAILs "
         f"confirmed at proper scope; remaining relief route = NON-TRACKING epoch profile (W1-2)"),
        (f"# anchor_evidence: S66 qa L817 0.67-baseline is z0-derived (PRESENT-DAY seesaw "
         f"extrapolated w=1/3) while E4 L723 escape row transports upstream (dilutes FASTER); "
         f"table rows mix anchors; n=2.3 escape implies rho_vac(z=0)/rho_obs={cc_ratio:.2e} "
         f"({cc_miss_oom:.2f} OOM CC undershoot) -- solves BBN by un-solving the CC; "
         f"identity disc*cc_ratio==1.032 verified {float(id2_dev):.1e}"),
    ]
    print_verdict_payload(verdict, value_str, audit_sha, content_sha,
                          companion_note=companion_note, extra_rows=extra_rows)

    print()
    print(f"OUTPUT_4TUPLE: (value={outcome}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"VERDICT: {GATE_ID}: {verdict}")
    print(f"  elapsed {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
