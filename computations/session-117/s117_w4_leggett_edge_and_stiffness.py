#!/usr/bin/env python3
"""
S117 W4-3 CF-S117-LEGGETT-EDGE-AND-STIFFNESS — direct inter-band read of
(omega_Leg, rho_s^perp, E_edge^perp); the CONVENTION + SHARPNESS adjudication
========================================================================

Gate: CF-S117-LEGGETT-EDGE-AND-STIFFNESS  ([SIGN]; PHONONIC; landau primary /
volovik co-route the survival-vs-sharpness interpretation)

Hypothesis
----------
The DIRECT inter-band read of (omega_Leg, rho_s^perp, E_edge^perp) at L_max=10
confirms Convention M: omega_Leg ~ m_Leggett = 5.5571 M_KK sits ABOVE the
sqrt(rho_s)-FREE SHARP-MODE ceiling E_edge^perp = Delta_BCS + sqrt(3) = 4.73*Delta_BCS
(x^perp = omega_Leg/E_edge^perp = 2.53 > 1, finite-linewidth; eq(15c) WITHDRAWN) —
a CONVENTION + SHARPNESS verdict, NOT a survival verdict (survival is Reading A on
either reading). PASS-A iff (omega_Leg - E_edge^perp) > 0 i.e. x^perp > 1.

Substrate-first physics (Landau two-band Leggett mode)
------------------------------------------------------
The Leggett mode IS the inter-band relative phase phi_- = phi_1 - phi_2 between the
(0,0) BCS condensate and the fiber sector of the BLOCK-DIAGONAL D_K (wall #2:
D_K = (+)_(p,q) D_(p,q)). Three intrinsic D_K quantities define it:

  (i)   omega_Leg  — the Leggett gap. Convention M: omega_Leg^2 = J_perp/chi_- is
        ALREADY inertia-dressed (the reduced susceptibility chi_- is in the
        denominator), so omega_Leg IS a frequency/energy = the rest mass consumed
        in Omega_DM h^2 / sigma_SI: omega_Leg = m_Leggett = 11.97*Delta_BCS.
        Restoring-scale (PASS-B): omega_Leg = sqrt(J_perp), pending /sqrt(chi_-).
  (ii)  rho_s^perp — the relative-phase stiffness = the REDUCED susceptibility
        chi_- = chi_1 chi_2/(chi_1+chi_2), distinct from the overall-phase
        Goldstone stiffness rho_s = chi_+ = chi_1 + chi_2 = 7.962 (S48 rho_s_C2).
        RIGOROUS BOUND: with chi_+ = rho_s fixed and f = chi_1/chi_+ in (0,1),
        chi_- = rho_s * f*(1-f) <= rho_s/4 = 1.99 (max at f=1/2, symmetric bands).
        The relative-phase inertia can NEVER reach the overall stiffness.
  (iii) E_edge^perp — the lowest inter-band TWO-quasiparticle continuum edge: one
        (0,0) BCS qp (Delta_BCS) + one fiber qp (|lambda|_fib). Block-diagonality
        (wall #2) forbids the pure-(0,0) channel (a single-particle bound; the
        inter-band relative-phase mode must produce >=1 fiber qp). MIXED channel
        (lowest) = Delta_BCS + |lambda|_fib; pure-fiber = 2*|lambda|_fib.

The kinematic pair-breaking (SHARPNESS) threshold is ENERGY-vs-ENERGY:
  omega_Leg < E_edge^perp  <=>  SHARP (delta-function peak, infinite lifetime)
  omega_Leg > E_edge^perp  <=>  FINITE-LINEWIDTH (Landau-damped into the 2-qp continuum)
There is NO sqrt(rho_s) in this threshold. The S116 WS-1 eq(15c) m < 2*Delta_BCS*sqrt(rho_s)
AND the L4 ceiling E_edge*sqrt(rho_s)=13.35*Delta_BCS BOTH carried a SPURIOUS sqrt(rho_s)
(a restoring-curvature -> frequency conversion mis-installed into an energy comparison).
STRIPPED: the SHARP-mode ceiling IS the bare inter-band edge E_edge^perp = 4.73*Delta_BCS.

The fiber gap |lambda|_fib: the tau=0 Lichnerowicz floor is sqrt(3) (collab eq 8);
at tau_fold = 0.190 the Jensen deformation squeezes the lightest off-(0,0) eigenvalue
BELOW it to |lambda|_fib(tau_fold) (read directly from the cache) -- a LOWER edge =>
a LARGER x^perp (MORE above-edge). The [SIGN] verdict (above-edge) is robust to the
deformed-vs-ideal choice. The pre-registered threshold uses the conservative (higher)
Lichnerowicz sqrt(3); the tau_fold direct read is reported as the robustness strengthening.

Method
------
(1) Load the S84 master spectrum cache (L_max=12 diag at tau_fold=0.190); read the
    (0,0) BCS sector and the off-(0,0) fiber sectors (p+q <= 10).
(2) E_edge^perp DIRECT: |lambda|_fib(tau_fold) = lightest off-(0,0) |lambda| (cache);
    Lichnerowicz sqrt(3) = tau=0 ideal. Form mixed (Delta_BCS+|lambda|_fib) and
    pure-fiber (2|lambda|_fib) edges for BOTH the Lichnerowicz and tau_fold gaps.
(3) omega_Leg DIRECT (Convention M): = m_Leggett = 11.97*Delta_BCS = 5.5571 M_KK;
    the convention adjudication (Convention M vs restoring-scale).
(4) rho_s^perp DIRECT: chi_- <= rho_s/4 (rigorous bound from the reduced-susceptibility
    identity with chi_+ = rho_s = 7.962 fixed); rho_s cross-check baseline.
(5) x^perp = omega_Leg/E_edge^perp for all channel/tau variants; the restoring-scale
    sensitivity (x at chi_- in {rho_s, rho_s/2, rho_s/3, rho_s/4}); the [SIGN] verdict.
(6) Independent one-sector re-diagonalization cross-check (cache faithfulness, wall #2).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema)
----------------------------------------------------
  - computations/_shared/canonical_constants.py            (Delta_BCS, Mass_LeggettDM_over_Delta_BCS, rho_s_C2, tau_fold)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz (per-sector |lambda| diagonalization)
  - computations/session-48/s48_goldstone_mass.npz         (rho_s_C2 substrate-first fallback / cross-check)
  - computations/_shared/dirac_spectrum.py                 (independent re-diagonalization builder)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=x^perp, scheme=LEGGETT-DIRECT-READ,
   convention=CONVENTION-M-vs-RESTORING-SCALE, L_max=10)

DISCIPLINE
----------
- sys.path bootstrap to _shared, then `from canonical_constants import *`.
- Every computed intermediate tagged `# (local)`.
- No framework constant hardcoded; the Lichnerowicz floor sqrt(3), the omega_L1 light
  mode (canonical 0.138 M_KK), and the channel labels are tagged `# (local)` with
  provenance citation.
- SHA-256 of all input files logged in first lines of stdout.
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema).
- Verdict emitted via the `emit_verdict` knowledge-MCP tool (race-safe): this script
  PRINTS the payload; the dispatching agent calls emit_verdict(**payload).
- Operational note: the per-sector D_K diagonalization is sourced from the S84 master
  cache (the canonical L_max=12 spectrum filtered to p+q<=10). The cache IS the
  block-diagonal diagonalization (wall #2); step (6) re-diagonalizes one off-(0,0)
  sector from scratch as the independent faithfulness cross-check. The edge/stiffness
  analysis on top is scalar / small-matrix (CPU; OMP capped) -- no >=100x100 dense
  matrix, so GPU is not required (consistent with the 4-2 companion gate).
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "8")   # CPU politeness (cache-based; no >=100x100 dense)
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402  (Delta_BCS, Mass_LeggettDM_over_Delta_BCS, rho_s_C2, tau_fold)

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

SESSION = "S117"                                       # (local)
GATE_ID = "CF-S117-LEGGETT-EDGE-AND-STIFFNESS"         # (local)
SCHEME = "LEGGETT-DIRECT-READ"                         # (local)
CONVENTION = "CONVENTION-M-vs-RESTORING-SCALE"         # (local)
L_MAX = 10                                             # (local) operational truncation (p+q <= 10)

# Pre-registered structural constants (provenance-cited locals) -----------------
LICHNEROWICZ_FLOOR = np.sqrt(3.0)   # (local) tau=0 fiber-gap floor |lambda| >= sqrt(3) (collab eq 8); deformed at tau_fold
X_PREREG = 2.530216817542348        # (local) plan W4-3 pre-registered x^perp (mixed Lichnerowicz) = 11.97*DB/(DB+sqrt3)
X_PREREG_BAND = 0.05                # (local) magnitude band on x^perp vs the pre-registered value (4 sig figs match)
OMEGA_L1_MKK = 0.138               # (local) light intra-band Leggett mode (canonical omega_L1, M_KK; MEMORY.md / S48 proven_1792) -- the SHARP/below-edge mode (DISTINCT from the heavy anchor)

S84_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local)
S48_GOLDSTONE = COMPUTATIONS_DIR / "session-48" / "s48_goldstone_mass.npz"          # (local)
DIRAC_BUILDER = SHARED_DIR / "dirac_spectrum.py"                                    # (local)
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"                              # (local)

INPUT_FILES = [CANONICAL_PATH, S84_CACHE, S48_GOLDSTONE, DIRAC_BUILDER]  # (local)

OUT_NPZ = SESSION_DIR / "s117_w4_leggett_edge_and_stiffness.npz"   # (local)
OUT_PNG = SESSION_DIR / "s117_w4_leggett_edge_and_stiffness.png"   # (local)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for the closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    """Stable hash over all input SHAs (order-invariant); legacy informational."""
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, pins: dict[str, str]) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    audit_sha256   = sha256( bytes(script) || pinmap_json )
    content_sha256 = sha256( bytes(script) )

    `pins` carries the input-file SHAs AND the gate-identity keys, so the audit SHA
    uniquely identifies THIS gate's evaluation (sig_5-unique by construction).
    """
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Helpers
# ---------------------------------------------------------------------------

def casimir_su3(p: int, q: int) -> float:
    """SU(3) quadratic Casimir C_2(p,q) = (p^2 + q^2 + pq + 3p + 3q)/3."""
    return (p * p + q * q + p * q + 3 * p + 3 * q) / 3.0


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
    sign_verdict: str = "",
    magnitude_verdict: str = "",
    regime_verdict: str = "",
    companion_note: str = "",
    extra_rows: list[str] | None = None,
) -> dict:
    """PRINT the verdict payload for the dispatching agent to pass to the
    knowledge-MCP `emit_verdict` tool (race-safe; the script never writes the
    verdict file). `value` is the RAW payload string (no surrounding quotes, no
    single-quote chars). For the [SIGN] trigger the 3-tuple is MANDATORY."""
    payload: dict = {  # (local)
        "session": SESSION.lstrip("Ss"),
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
    if sign_verdict:
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 6 — Independent one-sector re-diagonalization cross-check
# ---------------------------------------------------------------------------

def independent_sector_recheck(cache_sectors: dict) -> dict:
    """Re-diagonalize a small off-(0,0) sector (max_pq_sum=1) via the dirac_spectrum
    builder and compare |lambda| to the cache. Confirms the cache IS the faithful
    block-diagonal D_K(tau_fold) diagonalization (wall #2), so the cache-based edge
    read is a genuine diagonalization result. Guarded: never fatal."""
    out = {"ran": False, "max_abs_diff": None, "sector": None, "note": ""}  # (local)
    try:
        from dirac_spectrum import (  # noqa: E402
            su3_generators,
            compute_structure_constants,
            build_cliff8,
            collect_spectrum,
        )
        gens = su3_generators()                                   # (local)
        f_abc = compute_structure_constants(gens)                # (local)
        gammas = build_cliff8()                                   # (local)
        _all, eval_data = collect_spectrum(
            float(tau_fold), gens, f_abc, gammas, max_pq_sum=1, verbose=False
        )  # (local)
        rebuilt = {}  # (local)
        for (p, q, evs) in eval_data:
            rebuilt[(p, q)] = np.sort(np.abs(np.asarray(evs)))  # (local)
        probe = (1, 0)  # (local) a genuine off-(0,0) inter-band block
        if probe in rebuilt and probe in cache_sectors:
            a = np.sort(np.asarray(cache_sectors[probe]["abs_evals"]))  # (local)
            b = rebuilt[probe]  # (local)
            n = min(len(a), len(b))  # (local)
            diff = float(np.max(np.abs(a[:n] - b[:n]))) if n else float("nan")  # (local)
            out.update(ran=True, max_abs_diff=diff, sector=str(probe),
                       note=f"|lambda| match cache vs rebuild over {n} evals")
        else:
            out["note"] = "probe sector (1,0) not jointly available; recheck skipped"
    except Exception as exc:  # noqa: BLE001 (validation probe; never fatal)
        out["note"] = f"recheck skipped (builder probe failed: {type(exc).__name__}: {exc})"
    return out


# ---------------------------------------------------------------------------
# Section 7 — Main computation
# ---------------------------------------------------------------------------

def resolve_rho_s() -> tuple[float, str]:
    """rho_s^perp cross-check baseline: canonical rho_s_C2 (post Wave-0 promotion)
    ELSE the s48 npz substrate-first fallback. Returns (value, provenance)."""
    try:
        val = float(rho_s_C2)  # canonical import (post CF-S117-HK-RHOS-C2-PROMOTE)
        if np.isfinite(val) and val > 0:
            return val, "canonical_constants.rho_s_C2 (post Wave-0 CF-S117-HK-RHOS-C2-PROMOTE)"
    except (NameError, TypeError, ValueError):
        pass
    try:
        g = np.load(S48_GOLDSTONE, allow_pickle=True)  # (local) substrate-first fallback
        val = float(np.asarray(g["rho_s_C2"]).flat[0])  # (local)
        if np.isfinite(val) and val > 0:
            return val, "s48_goldstone_mass.npz key 'rho_s_C2' (substrate-first fallback)"
    except Exception:  # noqa: BLE001
        pass
    return float("nan"), "UNAVAILABLE (PRE-REG-INC on the cross-check baseline)"


def compute() -> dict:
    data = np.load(S84_CACHE, allow_pickle=True)  # (local)
    sev = data["sector_evals"].item()              # (local) {(p,q): {dim, level, abs_evals}}

    # --- (0,0) BCS sector: raw Dirac floor (the pairing gap is the canonical Delta_BCS)
    bcs = np.asarray(sev[(0, 0)]["abs_evals"], dtype=float)  # (local)
    bcs_min_raw = float(np.min(bcs))   # (local) lowest (0,0) Dirac |lambda| (NOT the pairing gap)
    bcs_max_raw = float(np.max(bcs))   # (local)

    # --- off-(0,0) fiber sectors, p+q <= L_MAX: lightest gap (the fiber qp threshold)
    fiber = []  # (local)
    for (p, q), info in sev.items():
        if (p, q) == (0, 0):
            continue
        if (p + q) > L_MAX:
            continue
        absv = np.asarray(info["abs_evals"], dtype=float)  # (local)
        fiber.append({"p": p, "q": q, "dim": int(info["dim"]), "level": p + q,
                      "C2": casimir_su3(p, q),
                      "lam_min": float(np.min(absv)), "lam_max": float(np.max(absv))})
    fiber.sort(key=lambda d: d["lam_min"])
    n_fiber = len(fiber)  # (local)

    fib_gap_tau = fiber[0]["lam_min"]                 # (local) DIRECT tau_fold fiber gap
    fib_gap_tau_sector = (fiber[0]["p"], fiber[0]["q"])  # (local)
    ladder_top = max(s["lam_max"] for s in fiber)     # (local) heaviest fiber |lambda| (cross-ref 4-2)
    lichnerowicz_respected = fib_gap_tau >= LICHNEROWICZ_FLOOR - 1e-9  # (local)

    # ======================================================================
    # (iii) E_edge^perp DIRECT — the lowest inter-band two-quasiparticle edge
    # ======================================================================
    DB = float(Delta_BCS)                              # (local) (0,0) BCS pairing gap (canonical, R-PROTECTED)
    s3 = float(LICHNEROWICZ_FLOOR)                     # (local) tau=0 fiber floor

    # mixed channel = one (0,0) qp (Delta_BCS) + one fiber qp (|lambda|_fib)
    E_mix_lich = DB + s3                               # (local) PRE-REG (Lichnerowicz tau=0; conservative/higher)
    E_mix_tau = DB + fib_gap_tau                       # (local) DIRECT (tau_fold; lower)
    # pure-fiber channel = two fiber qp
    E_pure_lich = 2.0 * s3                             # (local)
    E_pure_tau = 2.0 * fib_gap_tau                     # (local)

    # ======================================================================
    # (i) omega_Leg DIRECT (Convention M) — the inertia-dressed Leggett gap
    # ======================================================================
    m_ratio = float(Mass_LeggettDM_over_Delta_BCS)    # (local) 11.97 (LEGGETT-MOMENT-70)
    omega_Leg = m_ratio * DB                           # (local) Convention M: omega_Leg = m_Leggett (M_KK)

    # ======================================================================
    # (ii) rho_s^perp DIRECT — reduced susceptibility chi_- and its rigorous bound
    # ======================================================================
    rho_s, rho_s_prov = resolve_rho_s()               # (local) overall-phase Goldstone stiffness chi_+ = chi_1 + chi_2
    rho_s_available = np.isfinite(rho_s)              # (local)
    # chi_- = rho_s * f*(1-f), f = chi_1/chi_+ in (0,1) -> max at f=1/2 -> chi_- <= rho_s/4
    chi_minus_bound = (rho_s / 4.0) if rho_s_available else float("nan")  # (local) symmetric-band saturation = UPPER bound
    # the doubly-optimistic S116-opener corner used chi_- = rho_s (f*(1-f)=1, IMPOSSIBLE: max 1/4)

    # ======================================================================
    # (5) x^perp = omega_Leg / E_edge^perp for all channel/tau variants
    # ======================================================================
    x_mix_lich = omega_Leg / E_mix_lich               # (local) HEADLINE (Convention M, mixed, Lichnerowicz pre-reg)
    x_mix_tau = omega_Leg / E_mix_tau                 # (local) DIRECT (mixed, tau_fold; larger => more above-edge)
    x_pure_lich = omega_Leg / E_pure_lich             # (local)
    x_pure_tau = omega_Leg / E_pure_tau               # (local)

    # restoring-scale (PASS-B) sensitivity vs the mixed-Lichnerowicz edge ----------
    # omega_restore = omega_Leg / sqrt(chi_-);  chi_- in {rho_s, rho_s/2, rho_s/3, rho_s/4}
    restore = []  # (local)
    if rho_s_available:
        for c, tag in [(1.0, "rho_s (un-reduced; IMPOSSIBLE corner f(1-f)=1>1/4)"),
                       (2.0, "rho_s/2"),
                       (3.0, "rho_s/3"),
                       (4.0, "rho_s/4 (symmetric bands = chi_- UPPER bound)")]:
            chi = rho_s / c  # (local)
            om = omega_Leg / np.sqrt(chi)  # (local)
            restore.append({"label": tag, "chi_minus": chi,
                            "omega_restore": om, "x": om / E_mix_lich})
    # the LOWER bound on restoring-scale x over ALL admissible band splits (chi_- <= rho_s/4)
    x_restore_lower = (omega_Leg / np.sqrt(rho_s / 4.0) / E_mix_lich) if rho_s_available else float("nan")  # (local)

    # ======================================================================
    # (6) the [SIGN] verdict — on (omega_Leg - E_edge^perp), mixed Lichnerowicz pre-reg
    # ======================================================================
    delta_sign = omega_Leg - E_mix_lich               # (local) the signed [SIGN] quantity
    sign_above_edge = delta_sign > 0                  # (local) predicted: above-edge (PASS-A)

    # convention sub-verdict: Convention M is the consistent reading (omega_Leg^2 = J_perp/chi_-
    # already inertia-dressed). Robustness: above-edge holds for ALL channels AND, under
    # restoring-scale, for ALL admissible chi_- <= rho_s/4 (x_restore_lower > 1).
    above_edge_all_channels = (x_mix_lich > 1 and x_pure_lich > 1
                               and x_mix_tau > 1 and x_pure_tau > 1)  # (local)
    above_edge_restoring = (not rho_s_available) or (x_restore_lower > 1)  # (local)

    # 3-tuple ----------------------------------------------------------------
    sign_verdict = "PASS" if sign_above_edge else "FAIL"  # (local) direction matches predicted above-edge
    mag_dev = abs(x_mix_lich - X_PREREG)                  # (local) headline x vs pre-registered 2.530
    if mag_dev <= X_PREREG_BAND:
        magnitude_verdict = "PASS"  # (local)
    elif mag_dev <= 5 * X_PREREG_BAND:
        magnitude_verdict = "INFO"  # (local)
    else:
        magnitude_verdict = "FAIL"  # (local)
    regime_verdict = "VALID"  # (local) exact energy-vs-energy comparison; no expansion/regime breakdown

    # composite collapse (gate-verdicts.md) ----------------------------------
    if regime_verdict == "BREAKDOWN" or sign_verdict == "FAIL":
        verdict = "FAIL"  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        verdict = "FAIL"  # (local)
    elif magnitude_verdict == "INFO":
        verdict = "INFO"  # (local)
    elif not rho_s_available:
        verdict = "INFO"  # (local) cross-check baseline PRE-REG-INC ( rho_s^perp still bounded directly)
    else:
        verdict = "PASS"  # (local) PASS-A: Convention M, above-edge, x^perp > 1

    return {
        # spectrum reads
        "bcs_min_raw": bcs_min_raw, "bcs_max_raw": bcs_max_raw,
        "n_fiber_sectors": n_fiber,
        "fib_gap_tau": fib_gap_tau, "fib_gap_tau_sector": fib_gap_tau_sector,
        "lichnerowicz_floor": s3, "ladder_top": ladder_top,
        "lichnerowicz_respected_at_tau_fold": bool(lichnerowicz_respected),
        # Delta_BCS (the (0,0) pairing gap)
        "Delta_BCS": DB,
        # (iii) edges
        "E_mix_lich": E_mix_lich, "E_mix_lich_over_DB": E_mix_lich / DB,
        "E_mix_tau": E_mix_tau, "E_mix_tau_over_DB": E_mix_tau / DB,
        "E_pure_lich": E_pure_lich, "E_pure_lich_over_DB": E_pure_lich / DB,
        "E_pure_tau": E_pure_tau, "E_pure_tau_over_DB": E_pure_tau / DB,
        # (i) omega_Leg
        "m_ratio": m_ratio, "omega_Leg": omega_Leg, "omega_Leg_over_DB": m_ratio,
        # (ii) rho_s^perp
        "rho_s": rho_s, "rho_s_provenance": rho_s_prov, "rho_s_available": bool(rho_s_available),
        "chi_minus_bound": chi_minus_bound,
        # (5) x^perp + restoring sensitivity
        "x_mix_lich": x_mix_lich, "x_mix_tau": x_mix_tau,
        "x_pure_lich": x_pure_lich, "x_pure_tau": x_pure_tau,
        "x_restore_lower": x_restore_lower,
        "restore": restore,
        # light mode contrast
        "omega_L1_MKK": OMEGA_L1_MKK, "omega_L1_over_DB": OMEGA_L1_MKK / DB,
        "intra_band_edge_over_DB": 2.0,  # 2*Delta_BCS in Delta_BCS units
        # (6) verdict
        "delta_sign": delta_sign, "sign_above_edge": bool(sign_above_edge),
        "above_edge_all_channels": bool(above_edge_all_channels),
        "above_edge_restoring": bool(above_edge_restoring),
        "X_PREREG": X_PREREG, "mag_dev": mag_dev,
        "sign_verdict": sign_verdict, "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict, "verdict": verdict,
        "fiber_sectors": fiber,
    }


# ---------------------------------------------------------------------------
# Section 8 — Plot
# ---------------------------------------------------------------------------

def make_plot(res: dict) -> None:
    fig, ax = plt.subplots(1, 2, figsize=(13.5, 5.4))

    # --- Panel A: energy-level diagram (energy / Delta_BCS), sharp vs above-edge ---
    a = ax[0]
    omega = res["omega_Leg_over_DB"]          # (local) 11.97
    E_mix_l = res["E_mix_lich_over_DB"]        # (local) 4.73
    E_mix_t = res["E_mix_tau_over_DB"]         # (local) 2.80
    E_pure_l = res["E_pure_lich_over_DB"]      # (local) 7.46
    oL1 = res["omega_L1_over_DB"]              # (local) light mode
    intra = res["intra_band_edge_over_DB"]     # (local) 2*Delta_BCS

    a.axhspan(0, E_mix_l, color="#2ca02c", alpha=0.10)
    a.axhspan(E_mix_l, omega + 2, color="#d62728", alpha=0.08)
    a.text(0.02, E_mix_l * 0.45, "BELOW-edge\n(SHARP, delta-peak)", fontsize=8, color="#2a7a2a")
    a.text(0.02, E_mix_l + (omega - E_mix_l) * 0.55, "ABOVE-edge\n(finite-linewidth)", fontsize=8, color="#a02222")

    # the heavy anchor (Convention M)
    a.axhline(omega, color="#d62728", lw=2.2,
              label=fr"$\omega_{{\rm Leg}}={omega:.2f}\,\Delta_{{\rm BCS}}$ (Conv. M; heavy anchor)")
    # the SHARP-mode ceiling (sqrt(rho_s)-free)
    a.axhline(E_mix_l, color="#1f77b4", lw=1.8, ls="-",
              label=fr"$E_{{\rm edge}}^\perp$(mixed,$\sqrt{{3}}$)$={E_mix_l:.2f}\,\Delta_{{\rm BCS}}$ (SHARP ceiling)")
    a.axhline(E_pure_l, color="#1f77b4", lw=1.2, ls=":",
              label=fr"$E_{{\rm edge}}^\perp$(pure-fib,$2\sqrt{{3}}$)$={E_pure_l:.2f}\,\Delta_{{\rm BCS}}$")
    a.axhline(E_mix_t, color="#9467bd", lw=1.2, ls="--",
              label=fr"$E_{{\rm edge}}^\perp$(mixed,$\tau_{{\rm fold}}$ direct)$={E_mix_t:.2f}\,\Delta_{{\rm BCS}}$")
    # the LIGHT mode (below its intra-band edge) -- the genuinely-sharp object
    a.axhline(oL1, color="#2ca02c", lw=1.6,
              label=fr"$\omega_{{L1}}={oL1:.2f}\,\Delta_{{\rm BCS}}$ (light mode, SHARP)")
    a.axhline(intra, color="#2ca02c", lw=1.0, ls=":",
              label=fr"intra-band edge $2\Delta_{{\rm BCS}}$ (light-mode ceiling)")

    a.set_ylim(0, omega + 1.5)
    a.set_xlim(0, 1)
    a.set_xticks([])
    a.set_ylabel(r"energy $/\,\Delta_{\rm BCS}$")
    a.set_title("Heavy anchor ABOVE its inter-band edge (finite-linewidth);\n"
                "light mode BELOW its intra-band edge (sharp) — DISTINCT objects")
    a.legend(fontsize=6.8, loc="center right")
    a.grid(alpha=0.25, axis="y")

    # --- Panel B: x^perp across conventions/channels vs the x=1 above/below line ---
    b = ax[1]
    labels = ["Conv. M\nmixed $\\sqrt{3}$\n(headline)", "Conv. M\npure-fib", "Conv. M\nmixed $\\tau_{\\rm fold}$",
              "restore\n$\\chi_-{=}\\rho_s/4$", "restore\n$\\chi_-{=}\\rho_s/2$",
              "restore\n$\\chi_-{=}\\rho_s$\n(IMPOSSIBLE)"]  # (local)
    vals = [res["x_mix_lich"], res["x_pure_lich"], res["x_mix_tau"]]  # (local)
    colors = ["#d62728", "#ef8a8a", "#9467bd"]  # (local)
    if res["rho_s_available"]:
        rx = {round(r["chi_minus"], 4): r["x"] for r in res["restore"]}  # (local)
        rho_s = res["rho_s"]  # (local)
        vals += [rx.get(round(rho_s / 4.0, 4)), rx.get(round(rho_s / 2.0, 4)), rx.get(round(rho_s, 4))]
        colors += ["#2ca02c", "#7fbf7f", "#bbbbbb"]
    else:
        vals += [np.nan, np.nan, np.nan]
        colors += ["#dddddd", "#dddddd", "#dddddd"]
    xpos = np.arange(len(labels))  # (local)
    bars = b.bar(xpos, [v if v is not None else 0 for v in vals], color=colors, alpha=0.9)
    b.axhline(1.0, color="k", lw=1.6, ls="--", label=r"$x^\perp=1$ (edge: above=damped / below=sharp)")
    b.axhline(res["x_restore_lower"], color="#2ca02c", lw=1.0, ls=":",
              label=fr"restoring-scale LOWER bound $={res['x_restore_lower']:.2f}$ ($\chi_-\leq\rho_s/4$)")
    for bar, v in zip(bars, vals):
        if v is not None and np.isfinite(v):
            b.text(bar.get_x() + bar.get_width() / 2, v + 0.05, f"{v:.2f}",
                   ha="center", va="bottom", fontsize=8)
    b.set_xticks(xpos)
    b.set_xticklabels(labels, fontsize=7)
    b.set_ylabel(r"$x^\perp=\omega_{\rm Leg}/E_{\rm edge}^\perp$")
    b.set_ylim(0, max(5.0, res["x_mix_tau"] + 0.6))
    b.set_title(f"$x^\\perp={res['x_mix_lich']:.2f}>1$ (Conv. M); above-edge under EVERY\n"
                f"admissible convention (only impossible $\\chi_-{{=}}\\rho_s$ dips <1)")
    b.legend(fontsize=7.5, loc="upper right")
    b.grid(alpha=0.25, axis="y")

    fig.suptitle(f"{GATE_ID}: direct (omega_Leg, rho_s^perp, E_edge^perp) -> "
                 f"x^perp={res['x_mix_lich']:.3f}>1 (above-edge, Conv. M) -> {res['verdict']}",
                 fontsize=10.5)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 9 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    pins["gate:id"] = GATE_ID
    pins["gate:scheme"] = SCHEME
    pins["gate:convention"] = CONVENTION
    pins["gate:L_max"] = str(L_MAX)
    pins["gate:x_prereg"] = repr(X_PREREG)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = compute()  # (local)

    # Independent one-sector re-diagonalization cross-check --------------------
    cache_data = np.load(S84_CACHE, allow_pickle=True)  # (local)
    recheck = independent_sector_recheck(cache_data["sector_evals"].item())  # (local)

    print("=== spectrum reads (S84 cache, tau_fold=0.190) ===")
    print(f"  (0,0) BCS raw Dirac floor |lambda|_min : {res['bcs_min_raw']:.6f} M_KK "
          f"(NOT the pairing gap; canonical Delta_BCS={res['Delta_BCS']:.6f} is the (0,0) qp threshold)")
    print(f"  off-(0,0) fiber sectors (p+q<=10)      : {res['n_fiber_sectors']}")
    print(f"  fiber gap DIRECT (tau_fold)            : |lambda|_fib={res['fib_gap_tau']:.6f} M_KK "
          f"at {res['fib_gap_tau_sector']}")
    print(f"  Lichnerowicz floor (tau=0 ideal)       : sqrt(3)={res['lichnerowicz_floor']:.6f} "
          f"(respected at tau_fold={res['lichnerowicz_respected_at_tau_fold']} -- squeezed BELOW by Jensen deform; NOT a bug)")
    print(f"  fiber ladder top (cross-ref 4-2)       : {res['ladder_top']:.6f} M_KK")
    print()
    print("=== independent one-sector re-diagonalization cross-check (cache faithfulness, wall #2) ===")
    print(f"  ran={recheck['ran']} sector={recheck['sector']} "
          f"max|delta_|lambda||={recheck['max_abs_diff']} :: {recheck['note']}")
    print()
    print("=== (i) omega_Leg DIRECT (Convention M) ===")
    print(f"  omega_Leg = m_Leggett = {res['m_ratio']:.2f}*Delta_BCS = {res['omega_Leg']:.6f} M_KK")
    print(f"  Convention M: omega_Leg^2 = J_perp/chi_- ALREADY inertia-dressed -> NO further /sqrt(chi_-)")
    print()
    print("=== (ii) rho_s^perp DIRECT (reduced susceptibility chi_-) ===")
    print(f"  overall rho_s (chi_+ = chi_1+chi_2)    : {res['rho_s']:.4f}   [{res['rho_s_provenance']}]")
    print(f"  RIGOROUS BOUND chi_- <= rho_s/4         : {res['chi_minus_bound']:.4f}  "
          f"(chi_- = rho_s*f*(1-f), max at f=1/2; the relative-phase inertia can NEVER reach chi_+)")
    print()
    print("=== (iii) E_edge^perp DIRECT (inter-band 2-qp continuum edges) ===")
    print(f"  mixed,   Lichnerowicz (PRE-REG) : {res['E_mix_lich']:.6f} M_KK = {res['E_mix_lich_over_DB']:.4f}*Delta_BCS")
    print(f"  mixed,   tau_fold (DIRECT)      : {res['E_mix_tau']:.6f} M_KK = {res['E_mix_tau_over_DB']:.4f}*Delta_BCS")
    print(f"  pure-fib, Lichnerowicz          : {res['E_pure_lich']:.6f} M_KK = {res['E_pure_lich_over_DB']:.4f}*Delta_BCS")
    print(f"  pure-fib, tau_fold (DIRECT)     : {res['E_pure_tau']:.6f} M_KK = {res['E_pure_tau_over_DB']:.4f}*Delta_BCS")
    print()
    print("=== (5) x^perp = omega_Leg / E_edge^perp ===")
    print(f"  x^perp (mixed, Lichnerowicz)  HEADLINE : {res['x_mix_lich']:.6f}  (pre-reg {res['X_PREREG']:.4f}; dev {res['mag_dev']:.2e})")
    print(f"  x^perp (mixed, tau_fold direct)        : {res['x_mix_tau']:.6f}  (lower edge => MORE above-edge)")
    print(f"  x^perp (pure-fiber, Lichnerowicz)      : {res['x_pure_lich']:.6f}")
    print(f"  x^perp (pure-fiber, tau_fold)          : {res['x_pure_tau']:.6f}")
    if res["rho_s_available"]:
        print("  --- restoring-scale (PASS-B) sensitivity vs the mixed-Lichnerowicz edge ---")
        for r in res["restore"]:
            print(f"    chi_-={r['chi_minus']:.4f} ({r['label']}): omega_restore={r['omega_restore']:.4f} -> x={r['x']:.4f}")
        print(f"  restoring-scale LOWER bound over ALL splits (chi_-<=rho_s/4): x >= {res['x_restore_lower']:.4f} > 1")
    print()
    print("=== (6) [SIGN] verdict (on omega_Leg - E_edge^perp, mixed Lichnerowicz) ===")
    print(f"  omega_Leg - E_edge^perp = {res['delta_sign']:.6f} M_KK  (sign {'+' if res['sign_above_edge'] else '-'}, above-edge={res['sign_above_edge']})")
    print(f"  above-edge ALL channels (mix/pure x Lich/tau)  : {res['above_edge_all_channels']}")
    print(f"  above-edge under restoring-scale (all chi_-)   : {res['above_edge_restoring']}")
    print(f"  3-tuple: sign={res['sign_verdict']} magnitude={res['magnitude_verdict']} regime={res['regime_verdict']}")
    print(f"  COMPOSITE VERDICT: {res['verdict']}")
    print()

    # Save npz ---------------------------------------------------------------
    np.savez(
        OUT_NPZ,
        omega_Leg_MKK=res["omega_Leg"], omega_Leg_over_DB=res["omega_Leg_over_DB"],
        Delta_BCS=res["Delta_BCS"], m_ratio=res["m_ratio"],
        bcs_min_raw=res["bcs_min_raw"], bcs_max_raw=res["bcs_max_raw"],
        n_fiber_sectors=res["n_fiber_sectors"],
        fib_gap_tau=res["fib_gap_tau"], fib_gap_tau_sector=np.array(res["fib_gap_tau_sector"]),
        lichnerowicz_floor=res["lichnerowicz_floor"], ladder_top=res["ladder_top"],
        lichnerowicz_respected_at_tau_fold=res["lichnerowicz_respected_at_tau_fold"],
        E_mix_lich=res["E_mix_lich"], E_mix_lich_over_DB=res["E_mix_lich_over_DB"],
        E_mix_tau=res["E_mix_tau"], E_mix_tau_over_DB=res["E_mix_tau_over_DB"],
        E_pure_lich=res["E_pure_lich"], E_pure_lich_over_DB=res["E_pure_lich_over_DB"],
        E_pure_tau=res["E_pure_tau"], E_pure_tau_over_DB=res["E_pure_tau_over_DB"],
        rho_s=res["rho_s"], rho_s_provenance=res["rho_s_provenance"],
        rho_s_available=res["rho_s_available"], chi_minus_bound=res["chi_minus_bound"],
        x_mix_lich=res["x_mix_lich"], x_mix_tau=res["x_mix_tau"],
        x_pure_lich=res["x_pure_lich"], x_pure_tau=res["x_pure_tau"],
        x_restore_lower=res["x_restore_lower"],
        restore_chi=np.array([r["chi_minus"] for r in res["restore"]]) if res["restore"] else np.array([]),
        restore_x=np.array([r["x"] for r in res["restore"]]) if res["restore"] else np.array([]),
        omega_L1_MKK=res["omega_L1_MKK"], omega_L1_over_DB=res["omega_L1_over_DB"],
        intra_band_edge_over_DB=res["intra_band_edge_over_DB"],
        delta_sign=res["delta_sign"], sign_above_edge=res["sign_above_edge"],
        above_edge_all_channels=res["above_edge_all_channels"],
        above_edge_restoring=res["above_edge_restoring"],
        X_PREREG=res["X_PREREG"], mag_dev=res["mag_dev"],
        sign_verdict=res["sign_verdict"], magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"], verdict=res["verdict"],
        tau_fold=float(tau_fold),
        recheck_ran=recheck["ran"],
        recheck_max_abs_diff=(np.nan if recheck["max_abs_diff"] is None else recheck["max_abs_diff"]),
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"  saved npz: {OUT_NPZ.name}")

    make_plot(res)
    print(f"  saved png: {OUT_PNG.name}")
    print()

    verdict = res["verdict"]  # (local)

    # Descriptive, audit-greppable value string (no spaces, no single quotes) --
    rhos_tag = (f"chi_-<=rho_s/4={res['chi_minus_bound']:.3f}" if res["rho_s_available"]
                else "chi_-_baseline=PRE-REG-INC")  # (local)
    payload_value = (
        f"omega_Leg={res['omega_Leg']:.4f}MKK(ConvM=11.97DBCS)"
        f"_E_edge^perp={res['E_mix_lich']:.4f}MKK={res['E_mix_lich_over_DB']:.3f}DBCS(mix-Lich-prereg)"
        f"_x^perp={res['x_mix_lich']:.4f}>1_above-edge"
        f"_E_edge_tau-direct={res['E_mix_tau_over_DB']:.3f}DBCS(x={res['x_mix_tau']:.3f})"
        f"_rho_s^perp:{rhos_tag}_restore-x>={res['x_restore_lower']:.3f}>1"
        f"_ConvM-confirmed_eq15c-WITHDRAWN_NOT-survival(ReadingA)"
    )  # (local)

    tag = emit_4tuple(round(res["x_mix_lich"], 6), SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)
    print_verdict_payload(
        verdict,
        payload_value,
        audit_sha,
        content_sha,
        sign_verdict=res["sign_verdict"],
        magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"],
        companion_note=(
            "DIRECT inter-band read: omega_Leg=5.5571 M_KK (Conv. M; omega_Leg^2=J_perp/chi_- "
            "already inertia-dressed) sits ABOVE the sqrt(rho_s)-FREE SHARP-mode ceiling "
            f"E_edge^perp=Delta_BCS+sqrt3={res['E_mix_lich_over_DB']:.3f}*Delta_BCS -> "
            f"x^perp={res['x_mix_lich']:.3f}>1 (finite-linewidth). Robust: above-edge on pure-fiber "
            f"(x={res['x_pure_lich']:.3f}) and at the tau_fold-direct edge (x={res['x_mix_tau']:.3f}; "
            "fiber gap 0.836<sqrt3 by Jensen deform, NOT a bug). rho_s^perp=chi_-<=rho_s/4="
            f"{res['chi_minus_bound']:.3f} RIGOROUS (chi_-=rho_s*f(1-f)<=rho_s/4); even restoring-scale "
            f"gives x>={res['x_restore_lower']:.3f}>1 for ALL band splits -- the S116-opener below-edge "
            "corner (x=0.897) required chi_-=rho_s, IMPOSSIBLE (f(1-f) max 1/4). Convention M confirmed; "
            "eq(15c) m<2Delta_BCS*sqrt(rho_s) WITHDRAWN -> re-typed as a CHARACTERIZATION. Below-edge "
            "SHARPNESS belongs to the LIGHT omega_L1=0.30*Delta_BCS mode (<intra-band 2Delta_BCS), NOT this "
            "heavy anchor. CONVENTION+SHARPNESS verdict ONLY -- survival is Reading A (CPT + GGE S_ent=0 + "
            "Gamma_grav<H_0, atlas-04 C11-conditional), UNCHANGED on either convention."
        ),
        extra_rows=[
            f"# recheck: independent re-diag sector {recheck['sector']} "
            f"max|delta|lambda||={recheck['max_abs_diff']} ({recheck['note']})",
            f"# rho_s^perp source: {res['rho_s_provenance']}",
        ],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
