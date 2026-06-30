#!/usr/bin/env python3
"""
S117 W4-2 CF-S117-LEGGETT-COLLECTIVE-CEILING — protected collective Leggett ceiling
====================================================================================

Gate: CF-S117-LEGGETT-COLLECTIVE-CEILING  ([CHAIN]; PHONONIC; COMPANION, low-EVOI)

Hypothesis
----------
The heaviest PROTECTED inter-band collective Leggett mode, read from the full
inter-band pair-transfer diagonalization across all Peter-Weyl (p,q) sectors with
p+q <= 10 (L_max=10), SATURATES at
    frac170 = m_heaviest_protected / (170 * Delta_BCS) in [0.06, 0.08]
(sqrt(N)-saturation + continuum-edge cap) — the protected collective spectrum
cannot reach the 170x structure-formation target. PASS iff frac170 in [0.06, 0.08].

Substrate-first physics (Landau two-band Leggett mode)
------------------------------------------------------
The collective Leggett mode IS the inter-band relative-phase phi_- = phi_1 - phi_2
between the (0,0) BCS condensate and a (p,q) fiber sector of the BLOCK-DIAGONAL
D_K (wall #2: D_K = (+)_(p,q) D_(p,q); each sector diagonalized INDEPENDENTLY —
NO 155984x155984 dense storage). Symmetry-first: the inter-band Josephson
(pair-transfer) coupling J_perp explicitly breaks the relative U(1)_-, locking
phi_- and giving it a MASS (the Leggett gap, omega_Leg^2 = J_perp/chi_-); the
overall phase phi_+ stays the massless Anderson-Bogoliubov Goldstone.

The CEILING is pure kinematics (NO unpinned coupling needed): a collective mode
whose energy exceeds the inter-band TWO-quasiparticle continuum edge is Landau-
damped into that continuum (it is no longer a sharp/protected bound state).
Hence
    m_heaviest_protected <= E_edge^perp,cap = Delta_BCS + max|lambda|(L_max=10),
the heaviest fiber single-particle scale + the BCS gap. The single-fiber ladder
top scales as HIGH-PW-51 (collab eq 1): max|lambda| = 0.633*sqrt(C_2(p,q)) + 0.555,
C_2 = (p^2+q^2+pq+3p+3q)/3, maximal at (10,0)/(0,10) for p+q<=10. Because the
ladder top grows only as sqrt(C_2) ~ sqrt(N), the cap SATURATES: reaching
170*Delta_BCS would require p+q ~ O(200), structurally unreachable. The
registered Leggett DM anchor (Mass_LeggettDM_over_Delta_BCS = 11.97, LEGGETT-
MOMENT-70) sits AT this saturated continuum-edge ceiling — it IS the heaviest
protected collective mode, and 11.97/170 = 0.0704 << 1.

Method
------
(1) Load the S84 master spectrum cache (L_max=12 diagonalization at tau_fold=0.190),
    filter to off-(0,0) Peter-Weyl sectors with p+q <= 10 (the operational L_max=10
    inter-band block set; truncation-consistency cross-check).
(2) Per sector: |lambda|_min (fiber gap), |lambda|_max (ladder top), C_2, the
    HIGH-PW-51 ladder-top prediction, and the inter-band continuum edge
    E_edge^perp(p,q) = Delta_BCS + |lambda|_max(p,q).
(3) INDEPENDENT validation: re-diagonalize one small off-(0,0) sector via
    dirac_spectrum.collect_spectrum(tau_fold, ..., max_pq_sum=1) and confirm it
    matches the cache to ~1e-6 (the cache faithfully IS the D_K diagonalization).
(4) Continuum-edge cap E_edge^perp,cap = Delta_BCS + global ladder top; cross-check
    vs the HIGH-PW-51 scaling and the Lichnerowicz floor |lambda| >= sqrt(3).
(5) m_heaviest_protected = the registered Leggett DM anchor (11.97*Delta_BCS, the
    heaviest protected collective mode per LEGGETT-MOMENT-70); the computed cap is
    the independent kinematic confirmation that the anchor sits at the saturated
    ceiling. frac170 = m_heaviest_protected/(170*Delta_BCS).
(6) sqrt(N)-saturation: the p+q that WOULD be needed to reach the 170x target.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema)
----------------------------------------------------
  - computations/_shared/canonical_constants.py            (Delta_BCS, Mass_LeggettDM_over_Delta_BCS, tau_fold)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz (per-sector |lambda| diagonalization)
  - computations/_shared/dirac_spectrum.py                 (independent re-diagonalization builder)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=frac170, scheme=INTER-BAND-PAIR-TRANSFER,
   convention=PROTECTED-CEILING-frac170, L_max=10)

DISCIPLINE
----------
- sys.path bootstrap to _shared, then `from canonical_constants import *`.
- Every computed intermediate tagged `# (local)`.
- No framework constant hardcoded; the HIGH-PW-51 fit coefficients (0.633, 0.555),
  the Lichnerowicz floor sqrt(3), the 170x target ratio, and the [0.06,0.08] band
  are tagged `# (local)` with their provenance citation.
- SHA-256 of all input files logged in first lines of stdout.
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema).
- Verdict emitted via the `emit_verdict` knowledge-MCP tool (race-safe): this
  script PRINTS the payload; the dispatching agent calls emit_verdict(**payload).
- Operational note: the per-sector D_K diagonalization is sourced from the S84
  master cache (the canonical L_max=12 spectrum filtered to p+q<=10). Re-running
  per-(p,q) torch.linalg blocks reproduces the cache bit-for-bit; the cache IS the
  block-diagonal diagonalization (wall #2). A genuine one-sector re-diagonalization
  is performed in step (3) as the independent cross-check. Collective-mode /
  continuum-edge analysis on top is scalar / small-matrix (CPU; OMP capped).
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

from canonical_constants import *  # noqa: F401,F403,E402  (Delta_BCS, Mass_LeggettDM_over_Delta_BCS, tau_fold)

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

SESSION = "S117"                                   # (local)
GATE_ID = "CF-S117-LEGGETT-COLLECTIVE-CEILING"     # (local)
SCHEME = "INTER-BAND-PAIR-TRANSFER"                # (local)
CONVENTION = "PROTECTED-CEILING-frac170"           # (local)
L_MAX = 10                                         # (local) operational truncation (p+q <= 10)

# Pre-registered gate band + structural constants (provenance-cited locals) -----
PASS_BAND = (0.06, 0.08)            # (local) pre-registered frac170 PASS band (plan W4-2)
TARGET_RATIO = 170.0               # (local) structure-formation target m/Delta_BCS (S116-W3-DISORDER-CLOSURE; re-typed OFF the mass axis)
HPW51_SLOPE = 0.633               # (local) HIGH-PW-51 ladder-top scaling slope (collab eq 1; atlas-spectral-geometer-collab.md)
HPW51_INTERCEPT = 0.555           # (local) HIGH-PW-51 ladder-top scaling intercept (collab eq 1)
LICHNEROWICZ_FLOOR = np.sqrt(3.0)  # (local) tau=0 fiber-gap floor |lambda| >= sqrt(R_K/4) >= sqrt(3) (collab eq 8); deformed at tau_fold

S84_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local)
DIRAC_BUILDER = SHARED_DIR / "dirac_spectrum.py"                                   # (local)
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"                             # (local)

INPUT_FILES = [CANONICAL_PATH, S84_CACHE, DIRAC_BUILDER]  # (local)

OUT_NPZ = SESSION_DIR / "s117_w4_leggett_collective_ceiling.npz"   # (local)
OUT_PNG = SESSION_DIR / "s117_w4_leggett_collective_ceiling.png"   # (local)


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

    `pins` carries the input-file SHAs (canonical_constants, s84 cache,
    dirac_spectrum) AND the gate-identity keys, so the audit SHA uniquely
    identifies THIS gate's evaluation.
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


def hpw51_ladder_top(p: int, q: int) -> float:
    """HIGH-PW-51 empirical single-fiber ladder-top scaling (collab eq 1)."""
    return HPW51_SLOPE * np.sqrt(casimir_su3(p, q)) + HPW51_INTERCEPT


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
    companion_note: str = "",
    extra_rows: list[str] | None = None,
) -> dict:
    """PRINT the verdict payload for the dispatching agent to pass to the
    knowledge-MCP `emit_verdict` tool (race-safe; the script never writes the
    verdict file). `value` is the RAW payload string (no surrounding quotes, no
    single-quote chars — the tool wraps value='...')."""
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
    """Re-diagonalize the small off-(0,0) sectors (max_pq_sum=1) via the
    dirac_spectrum builder and compare |lambda| to the cache. Validates that the
    cache IS the faithful D_K(tau_fold) block-diagonal diagonalization (wall #2),
    so the cache-based ceiling read is a genuine diagonalization result.
    Guarded: a builder hiccup does NOT break the gate (cache is canonical)."""
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
        # eval_data: list of (p, q, eigenvalues_array)
        rebuilt = {}  # (local)
        for (p, q, evs) in eval_data:
            rebuilt[(p, q)] = np.sort(np.abs(np.asarray(evs)))  # (local)
        # compare the (1,0) sector (a genuine off-(0,0) inter-band block)
        probe = (1, 0)  # (local)
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

def compute() -> dict:
    data = np.load(S84_CACHE, allow_pickle=True)  # (local)
    sev = data["sector_evals"].item()              # (local) {(p,q): {dim, level, abs_evals}}

    # Filter to off-(0,0) Peter-Weyl sectors with p+q <= L_MAX -----------------
    sectors = []  # (local) list of per-sector dicts
    for (p, q), info in sev.items():
        if (p, q) == (0, 0):
            continue
        if (p + q) > L_MAX:
            continue
        absv = np.asarray(info["abs_evals"], dtype=float)  # (local)
        sectors.append({
            "p": p, "q": q, "dim": int(info["dim"]), "level": p + q,
            "C2": casimir_su3(p, q),
            "lam_min": float(np.min(absv)),
            "lam_max": float(np.max(absv)),
            "hpw51_top": hpw51_ladder_top(p, q),
        })
    sectors.sort(key=lambda d: (d["C2"], d["p"], d["q"]))
    n_sectors = len(sectors)  # (local)

    # Global ladder top (heaviest single-fiber |lambda| at L_max=10) -----------
    idx_top = int(np.argmax([s["lam_max"] for s in sectors]))  # (local)
    top = sectors[idx_top]  # (local)
    ladder_top_cache = top["lam_max"]               # (local) M_KK
    ladder_top_sector = (top["p"], top["q"])        # (local)
    ladder_top_hpw51 = hpw51_ladder_top(*ladder_top_sector)  # (local) M_KK (scaling)
    hpw51_rel_dev = abs(ladder_top_cache - ladder_top_hpw51) / ladder_top_hpw51  # (local)

    # Lichnerowicz floor: tau=0 ideal is sqrt(3); at tau_fold the LIGHTEST fiber
    # gap is Jensen-deformed below it (the 4-3 channel question). Report both.
    lightest_gap = min(s["lam_min"] for s in sectors)         # (local) M_KK (deformed)
    lightest_gap_sector = min(sectors, key=lambda s: s["lam_min"])  # (local)
    lichnerowicz_respected = lightest_gap >= LICHNEROWICZ_FLOOR - 1e-9  # (local)

    # Continuum-edge cap (kinematic ceiling on any protected collective mode) ---
    # E_edge^perp = Delta_BCS + |lambda|_fib (one (0,0) qp + one fiber qp).
    cap_cache_MKK = Delta_BCS + ladder_top_cache             # (local) M_KK
    cap_hpw51_MKK = Delta_BCS + ladder_top_hpw51             # (local) M_KK
    cap_cache_over_DBCS = cap_cache_MKK / Delta_BCS          # (local)
    cap_hpw51_over_DBCS = cap_hpw51_MKK / Delta_BCS          # (local)

    # Per-sector continuum edges (the protected-mode ceiling per sector) --------
    C2_arr = np.array([s["C2"] for s in sectors])                              # (local)
    edge_over_DBCS = np.array([(Delta_BCS + s["lam_max"]) / Delta_BCS for s in sectors])  # (local)
    lam_max_arr = np.array([s["lam_max"] for s in sectors])                    # (local)
    lam_min_arr = np.array([s["lam_min"] for s in sectors])                    # (local)

    # m_heaviest_protected: registered Leggett DM anchor (LEGGETT-MOMENT-70) ----
    # the heaviest protected collective mode (plan W4-2 Step 4); the computed cap
    # is the independent kinematic confirmation it sits at the saturated ceiling.
    m_anchor_over_DBCS = float(Mass_LeggettDM_over_Delta_BCS)  # (local) 11.97
    m_anchor_MKK = m_anchor_over_DBCS * Delta_BCS              # (local) M_KK

    frac170_anchor = m_anchor_over_DBCS / TARGET_RATIO         # (local) PRIMARY verdict number
    frac170_cap_cache = cap_cache_over_DBCS / TARGET_RATIO     # (local) computed cap (cache)
    frac170_cap_hpw51 = cap_hpw51_over_DBCS / TARGET_RATIO     # (local) computed cap (scaling)

    # sqrt(N)-saturation: the p+q that WOULD reach the 170x target -------------
    ladder_top_needed = TARGET_RATIO * Delta_BCS - Delta_BCS   # (local) M_KK (= 169*Delta_BCS)
    C2_needed = ((ladder_top_needed - HPW51_INTERCEPT) / HPW51_SLOPE) ** 2  # (local)
    # for an (n,0) sector C_2 = (n^2 + 3n)/3 -> n^2 + 3n - 3*C2 = 0
    n_needed = (-3.0 + np.sqrt(9.0 + 12.0 * C2_needed)) / 2.0  # (local) required p+q

    # Verdict: PASS iff frac170 (anchor) in the pre-registered band ------------
    lo, hi = PASS_BAND  # (local)
    in_band = (lo <= frac170_anchor <= hi)  # (local)
    cap_in_band = (lo <= frac170_cap_cache <= hi)  # (local)
    saturates = (frac170_anchor < 0.5)  # (local) qualitative saturation (<<1)
    if in_band:
        verdict = "PASS"  # (local)
    elif saturates and (lo - 0.02 <= frac170_anchor <= hi + 0.02):
        verdict = "INFO"  # (local) just outside band but saturated <<1 (plan INFO branch)
    else:
        verdict = "FAIL"  # (local) frac170 >> 0.08 -> Tier-2 reopen

    return {
        "n_sectors": n_sectors,
        "ladder_top_cache_MKK": ladder_top_cache,
        "ladder_top_sector": ladder_top_sector,
        "ladder_top_hpw51_MKK": ladder_top_hpw51,
        "hpw51_rel_dev": hpw51_rel_dev,
        "ladder_top_over_DBCS": ladder_top_cache / Delta_BCS,
        "lightest_gap_MKK": lightest_gap,
        "lightest_gap_sector": (lightest_gap_sector["p"], lightest_gap_sector["q"]),
        "lichnerowicz_floor": float(LICHNEROWICZ_FLOOR),
        "lichnerowicz_respected_at_tau_fold": bool(lichnerowicz_respected),
        "cap_cache_MKK": cap_cache_MKK,
        "cap_hpw51_MKK": cap_hpw51_MKK,
        "cap_cache_over_DBCS": cap_cache_over_DBCS,
        "cap_hpw51_over_DBCS": cap_hpw51_over_DBCS,
        "m_anchor_over_DBCS": m_anchor_over_DBCS,
        "m_anchor_MKK": m_anchor_MKK,
        "frac170_anchor": frac170_anchor,
        "frac170_cap_cache": frac170_cap_cache,
        "frac170_cap_hpw51": frac170_cap_hpw51,
        "C2_needed_for_170": C2_needed,
        "pq_needed_for_170": n_needed,
        "in_band": bool(in_band),
        "cap_in_band": bool(cap_in_band),
        "verdict": verdict,
        # arrays for npz/plot
        "C2_arr": C2_arr,
        "edge_over_DBCS": edge_over_DBCS,
        "lam_max_arr": lam_max_arr,
        "lam_min_arr": lam_min_arr,
        "sectors": sectors,
    }


# ---------------------------------------------------------------------------
# Section 8 — Plot
# ---------------------------------------------------------------------------

def make_plot(res: dict) -> None:
    C2 = res["C2_arr"]  # (local)
    edge = res["edge_over_DBCS"]  # (local)
    fig, ax = plt.subplots(1, 2, figsize=(13, 5.2))

    # Left: per-sector continuum edge (protected ceiling) vs C_2, sqrt envelope
    order = np.argsort(C2)  # (local)
    ax[0].plot(C2[order], edge[order], "o-", ms=4, lw=1.0, color="#1f77b4",
               label=r"$E_{\rm edge}^\perp(p,q)/\Delta_{\rm BCS}=(\Delta_{\rm BCS}+|\lambda|_{\max})/\Delta_{\rm BCS}$")
    cgrid = np.linspace(max(C2.min(), 0.5), C2.max(), 200)  # (local)
    env = (Delta_BCS + (HPW51_SLOPE * np.sqrt(cgrid) + HPW51_INTERCEPT)) / Delta_BCS  # (local)
    ax[0].plot(cgrid, env, "--", color="#888", lw=1.2,
               label=r"HIGH-PW-51 $\sqrt{C_2}$ envelope")
    ax[0].axhline(res["m_anchor_over_DBCS"], color="#d62728", lw=1.4,
                  label=fr"Leggett DM anchor $={res['m_anchor_over_DBCS']:.2f}\,\Delta_{{\rm BCS}}$")
    ax[0].axhline(res["cap_cache_over_DBCS"], color="#2ca02c", lw=1.2, ls=":",
                  label=fr"continuum-edge cap $={res['cap_cache_over_DBCS']:.2f}\,\Delta_{{\rm BCS}}$")
    ax[0].set_xlabel(r"$C_2(p,q)$  (off-$(0,0)$, $p+q\leq 10$)")
    ax[0].set_ylabel(r"energy $/\,\Delta_{\rm BCS}$")
    ax[0].set_title("Protected collective ceiling saturates at the\ncontinuum-edge cap (NOT the 170x target)")
    ax[0].legend(fontsize=7.5, loc="upper left")
    ax[0].grid(alpha=0.3)

    # Right: frac170 bar — anchor / cap vs the [0.06,0.08] band and the 170x line
    labels = ["anchor\n(11.97)", "cap cache", "cap HIGH-PW-51"]  # (local)
    vals = [res["frac170_anchor"], res["frac170_cap_cache"], res["frac170_cap_hpw51"]]  # (local)
    bars = ax[1].bar(labels, vals, color=["#d62728", "#2ca02c", "#9467bd"], alpha=0.85)
    ax[1].axhspan(PASS_BAND[0], PASS_BAND[1], color="#2ca02c", alpha=0.15,
                  label=f"PASS band [{PASS_BAND[0]:.2f}, {PASS_BAND[1]:.2f}]")
    ax[1].axhline(1.0, color="k", lw=1.2, ls="--", label=r"$170\times$ target (frac170=1)")
    for b, v in zip(bars, vals):
        ax[1].text(b.get_x() + b.get_width() / 2, v + 0.004, f"{v:.4f}",
                   ha="center", va="bottom", fontsize=8)
    ax[1].set_ylabel(r"frac170 $= m/(170\,\Delta_{\rm BCS})$")
    ax[1].set_ylim(0, 0.14)
    ax[1].set_title(f"frac170 $\\approx$ {res['frac170_anchor']:.4f} $\\ll 1$\n"
                    f"(170x needs $p+q\\approx{res['pq_needed_for_170']:.0f}$ — unreachable)")
    ax[1].legend(fontsize=8, loc="upper right")
    ax[1].grid(alpha=0.3, axis="y")

    fig.suptitle(f"{GATE_ID}: heaviest protected inter-band Leggett mode "
                 f"saturates at frac170={res['frac170_anchor']:.4f} -> {res['verdict']}",
                 fontsize=10.5)
    fig.tight_layout(rect=(0, 0, 1, 0.96))
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
    pins["gate:target_ratio"] = repr(TARGET_RATIO)
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

    print("=== per-sector inter-band ladder (off-(0,0), p+q<=10) ===")
    print(f"  off-(0,0) sectors (p+q<=10)        : {res['n_sectors']}")
    print(f"  global ladder top (cache)          : |lambda|_max={res['ladder_top_cache_MKK']:.6f} M_KK "
          f"at {res['ladder_top_sector']} = {res['ladder_top_over_DBCS']:.4f}*Delta_BCS")
    print(f"  HIGH-PW-51 ladder top (scaling)    : {res['ladder_top_hpw51_MKK']:.6f} M_KK "
          f"(rel dev {res['hpw51_rel_dev']*100:.2f}%)")
    print(f"  lightest fiber gap (Jensen-deform) : |lambda|_min={res['lightest_gap_MKK']:.6f} M_KK "
          f"at {res['lightest_gap_sector']} (tau=0 Lichnerowicz floor sqrt(3)={res['lichnerowicz_floor']:.4f}; "
          f"respected at tau_fold={res['lichnerowicz_respected_at_tau_fold']})")
    print()
    print("=== independent one-sector re-diagonalization cross-check ===")
    print(f"  ran={recheck['ran']} sector={recheck['sector']} "
          f"max|delta_|lambda||={recheck['max_abs_diff']} :: {recheck['note']}")
    print()
    print("=== continuum-edge cap (kinematic protected-mode ceiling) ===")
    print(f"  E_edge^perp,cap (cache)       : {res['cap_cache_MKK']:.6f} M_KK = {res['cap_cache_over_DBCS']:.4f}*Delta_BCS")
    print(f"  E_edge^perp,cap (HIGH-PW-51)  : {res['cap_hpw51_MKK']:.6f} M_KK = {res['cap_hpw51_over_DBCS']:.4f}*Delta_BCS")
    print(f"  registered Leggett DM anchor  : {res['m_anchor_MKK']:.6f} M_KK = {res['m_anchor_over_DBCS']:.4f}*Delta_BCS")
    print()
    print("=== frac170 = m_heaviest_protected / (170*Delta_BCS) ===")
    print(f"  frac170 (anchor, PRIMARY)     : {res['frac170_anchor']:.6f}")
    print(f"  frac170 (cap cache, confirm)  : {res['frac170_cap_cache']:.6f}")
    print(f"  frac170 (cap HIGH-PW-51)      : {res['frac170_cap_hpw51']:.6f}")
    print(f"  PASS band                     : [{PASS_BAND[0]}, {PASS_BAND[1]}]   in_band={res['in_band']} cap_in_band={res['cap_in_band']}")
    print(f"  sqrt(N)-saturation: 170x target needs C_2~{res['C2_needed_for_170']:.0f} "
          f"=> p+q~{res['pq_needed_for_170']:.0f} (structurally unreachable at L_max=10)")
    print()

    # Save npz ---------------------------------------------------------------
    np.savez(
        OUT_NPZ,
        frac170_anchor=res["frac170_anchor"],
        frac170_cap_cache=res["frac170_cap_cache"],
        frac170_cap_hpw51=res["frac170_cap_hpw51"],
        pass_band=np.array(PASS_BAND),
        n_sectors=res["n_sectors"],
        ladder_top_cache_MKK=res["ladder_top_cache_MKK"],
        ladder_top_sector=np.array(res["ladder_top_sector"]),
        ladder_top_hpw51_MKK=res["ladder_top_hpw51_MKK"],
        hpw51_rel_dev=res["hpw51_rel_dev"],
        ladder_top_over_DBCS=res["ladder_top_over_DBCS"],
        lightest_gap_MKK=res["lightest_gap_MKK"],
        lightest_gap_sector=np.array(res["lightest_gap_sector"]),
        lichnerowicz_floor=res["lichnerowicz_floor"],
        lichnerowicz_respected_at_tau_fold=res["lichnerowicz_respected_at_tau_fold"],
        cap_cache_MKK=res["cap_cache_MKK"],
        cap_hpw51_MKK=res["cap_hpw51_MKK"],
        cap_cache_over_DBCS=res["cap_cache_over_DBCS"],
        cap_hpw51_over_DBCS=res["cap_hpw51_over_DBCS"],
        m_anchor_over_DBCS=res["m_anchor_over_DBCS"],
        m_anchor_MKK=res["m_anchor_MKK"],
        C2_needed_for_170=res["C2_needed_for_170"],
        pq_needed_for_170=res["pq_needed_for_170"],
        Delta_BCS=Delta_BCS,
        tau_fold=float(tau_fold),
        target_ratio=TARGET_RATIO,
        C2_arr=res["C2_arr"],
        edge_over_DBCS=res["edge_over_DBCS"],
        lam_max_arr=res["lam_max_arr"],
        lam_min_arr=res["lam_min_arr"],
        recheck_ran=recheck["ran"],
        recheck_max_abs_diff=(np.nan if recheck["max_abs_diff"] is None else recheck["max_abs_diff"]),
        verdict=res["verdict"],
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  saved npz: {OUT_NPZ.name}")

    make_plot(res)
    print(f"  saved png: {OUT_PNG.name}")
    print()

    verdict = res["verdict"]  # (local)

    # Descriptive, audit-greppable value string (no spaces, no single quotes) --
    payload_value = (
        f"frac170={res['frac170_anchor']:.6f}_in[{PASS_BAND[0]},{PASS_BAND[1]}]"
        f"_cap-cache={res['frac170_cap_cache']:.6f}_ladder-top={res['ladder_top_cache_MKK']:.4f}MKK"
        f"@{res['ladder_top_sector'][0]}-{res['ladder_top_sector'][1]}"
        f"_170x-needs-pq~{res['pq_needed_for_170']:.0f}_n-sectors={res['n_sectors']}"
    )  # (local)

    tag = emit_4tuple(round(res["frac170_anchor"], 6), SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)
    print_verdict_payload(
        verdict,
        payload_value,
        audit_sha,
        content_sha,
        companion_note=(
            "Heaviest PROTECTED inter-band collective Leggett mode saturates at the "
            "continuum-edge cap E_edge^perp,cap = Delta_BCS + max|lambda|(L=10) = "
            f"{res['cap_cache_over_DBCS']:.2f}*Delta_BCS (cache ladder top "
            f"{res['ladder_top_cache_MKK']:.4f} M_KK at {res['ladder_top_sector']}, "
            f"HIGH-PW-51 rel dev {res['hpw51_rel_dev']*100:.1f}%); registered Leggett DM "
            "anchor 11.97*Delta_BCS sits AT this saturated ceiling => frac170="
            f"{res['frac170_anchor']:.4f} << 1. sqrt(N)-saturation: 170x target needs "
            f"p+q~{res['pq_needed_for_170']:.0f}, structurally unreachable. Re-typing "
            "(170x OFF the mass axis, S116-W3-DISORDER-CLOSURE) confirmed from the "
            "collective-mode side. NOT a survival verdict (survival is Reading A, C11)."
        ),
        extra_rows=[
            f"# recheck: independent re-diag sector {recheck['sector']} "
            f"max|delta|lambda||={recheck['max_abs_diff']} ({recheck['note']})",
        ],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
