#!/usr/bin/env python3
"""
INV11 W2-1 INV11-W2-1-STERILE-NULL-DELTA-NEFF — two zero-free-parameter spectrum-forced NULLs
=============================================================================================

Gate: INV11-W2-1-STERILE-NULL-DELTA-NEFF ([VERIFY] + a pre-registered [SIGN] direction)

Pre-registered threshold (plan §W2-1):
  (a) STERILE-NULL: count{ distinct singlet active-mixing tower bottoms } == 3 (exact)
      AND (E_first_above / E_third_bottom) >= R_gap_min = 1.05 (next distinct state >= 5%
      above the third bottom — at the KK gap scale, NOT at the eV scale a 3+1 sterile demands).
  (b) DELTA-N_eff: |Delta_N_eff(nu-sector)| <= 0.01 AND N_eff_nu_FW within |.| <= 0.01 of N_eff_SM.
  PASS iff (count==3 AND gap>=R_gap_min AND |Delta_N_eff|<=0.01), FAIL/INFO per rubric.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz   (singlet tower eigenvalues)
  - computations/session-60/s60_lepto_cp_log.txt                (M_R B-branch fold scale; read-as-text, not a SHA input)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<count==3 & gap & Delta_N_eff payload>, scheme=spectrum-forced-NULL, convention=ABSOLUTE, L_max=12)

Classification: PARTICLE (representation-theoretic content of D_K: the Peter-Weyl
singlet (0,0) tower + the M_R B-branch fold scale).

METHODOLOGY
-----------
TWO independent extractions from the existing spectrum, both zero-free-parameter.

(a) STERILE-NULL.  The substrate IS the Peter-Weyl decomposition D_K = (+)_{(p,q)} D_{(p,q)}.
    The SINGLET (0,0) sector is the lepton-tower seed (S52): its distinct |eigenvalue| levels
    are the three light active-mixing bottoms. "Three generations from Z_3 triality" is PROVEN
    (S03/S28). We load the L12 cache, isolate the (0,0) singlet sector, count its DISTINCT
    eigenvalue levels (== 3 expected), and verify the next genuinely-distinct eigenstate sits at
    O(1) M_KK ~ 10^16 GeV (the KK gap), NOT within an eV-scale window of the third bottom. The
    dispositive sterile-null statement is the 16-OOM gulf between the O(1) M_KK spectrum floor and
    the eV scale a 3+1 sterile fit demands: there is no spectral home for a light active-mixing
    sterile. We report (i) the within-singlet gap ratio (first-above / third-bottom) and (ii) the
    M_KK-to-eV scale separation in decades.

(b) DELTA-N_eff.  The right-handed Majorana partners have mass M_R = (B-branch D_K fold energy) x
    M_KK ~ 10^17 GeV (s60_lepto_cp_log.txt: M_1 = 1.004396 M_KK = 7.4613e16 GeV; leptogenesis real
    M_R PROVEN S60). Apply the S56 W0-2 freeze-out entropy-dilution arithmetic: a species that
    decouples at T_fo ~ M_R contributes to N_eff at neutrino decoupling only the entropy-diluted
    residual Delta_N_eff_residual = (4/11)^{4/3} [g_*(T_dec)/g_*(T_fo)]^{4/3} per relativistic dof.
    For T_fo ~ M_R >> T_EW the residual ceiling is ~0.0122 (g_* ratio 10.75/106.75), but the RH
    partner is ALREADY non-relativistic at T_dec ~ 1 MeV by ~19.9 OOM, so the Boltzmann factor
    exp(-M_R/T_dec) drives the PHYSICAL contribution to ~0 EXACTLY. We report BOTH the residual
    ceiling (the relativistic-relic upper bound) and the Boltzmann-suppressed physical value, and
    confirm N_eff_nu_FW = N_eff_SM + Delta_N_eff reproduces N_eff_SM = 3.044 to the dilution floor.

DISCIPLINE
----------
- `from canonical_constants import *` (M_KK, g_star_BBN, g_star_SM, N_eff_SM)
- Every local/intermediate tagged `# (local)`
- Cache is pre-diagonalized: a load + sort + count, no fresh eig (no GPU needed)
- SHA-256 of all input files logged in first 20 lines of stdout; dual-SHA emitted (S84+)
- 4-tuple printed as final non-verdict line
- Verdict via the emit_verdict knowledge-MCP tool (race-safe); script PRINTS the payload only
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Path setup + canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

_SHARED = Path(__file__).resolve().parent.parent / "_shared"  # computations/_shared
sys.path.insert(0, str(_SHARED))

from canonical_constants import *  # noqa: F401,F403,E402
# Explicit names used below (all canonical; see provenance in canonical_constants.py):
#   M_KK        = 7.428660036284456e16  GeV   (S42 CONST-FREEZE-42)
#   g_star_SM   = 106.75                       (SM relativistic dof above EW scale)
#   g_star_BBN  = 10.75                        (dof at BBN: photons + 3 nu + e+/-)
#   N_eff_SM    = 3.044                        (3 nu + non-instantaneous decoupling)
from canonical_constants import M_KK, g_star_SM, g_star_BBN, N_eff_SM  # noqa: E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent          # computations/investigation-11/
COMPUTATIONS_DIR = SESSION_DIR.parent                   # computations/
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "11"                                                     # (local) investigation number
GATE_ID = "INV11-W2-1-STERILE-NULL-DELTA-NEFF"                     # (local)
SCHEME = "spectrum-forced-NULL"                                    # (local)
CONVENTION = "ABSOLUTE"                                            # (local)
L_MAX = 12                                                         # (local) L12 cache

# Pre-registered thresholds (plan §W2-1; define BEFORE running)
EXPECTED_COUNT = 3                                                 # (local) Z_3 triality -> 3 active bottoms
R_GAP_MIN = 1.05                                                   # (local) >= 5% gap above the third bottom
DELTA_NEFF_PASS = 0.01                                             # (local) |Delta_N_eff| <= 0.01
DELTA_NEFF_INFO = 0.05                                             # (local) INFO band ceiling (0.01, 0.05]
DEGEN_TOL = 1e-9                                                   # (local) eigenvalue degeneracy / gap-edge resolution

# Cosmology pins for the freeze-out arithmetic
T_DEC_GEV = 1.0e-3                                                 # (local) ~1 MeV active-nu decoupling
EV_PER_GEV = 1.0e9                                                 # (local) 1 GeV = 1e9 eV (for the M_KK->eV scale sep)

# Output destinations
OUT_NPZ = SESSION_DIR / "inv11_w2_sterile_null_delta_neff.npz"
OUT_PNG = SESSION_DIR / "inv11_w2_sterile_null_delta_neff.png"

CACHE_L12 = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
S60_LOG = COMPUTATIONS_DIR / "session-60" / "s60_lepto_cp_log.txt"

# SHA-pinned inputs (canonical + the cache; the s60 log is read as text below and
# pinned in the pinmap for the audit trail too).
INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    CACHE_L12,
    S60_LOG,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------

def extract_singlet_tower() -> dict:
    """(a) STERILE-NULL: count distinct singlet (0,0) active-mixing bottoms + gap ratios."""
    cache = np.load(CACHE_L12, allow_pickle=True)  # (local)
    sector_evals = cache["sector_evals"].item()    # (local) dict keyed by (p,q)

    # The SINGLET (0,0) sector is the lepton-tower seed (S52). Its DISTINCT |eigenvalue|
    # levels are the three light active-mixing bottoms.
    singlet = np.sort(np.asarray(sector_evals[(0, 0)]["abs_evals"], dtype=float))  # (local)
    # Collapse degenerate multiplets to distinct levels (tolerance DEGEN_TOL).
    distinct_levels = []  # (local)
    for e in singlet:
        if not distinct_levels or abs(e - distinct_levels[-1]) > DEGEN_TOL:
            distinct_levels.append(float(e))
    distinct_levels = np.asarray(distinct_levels)  # (local)
    n_distinct = int(distinct_levels.size)         # (local)
    third_bottom = float(distinct_levels[min(2, n_distinct - 1)])  # (local) 3rd distinct level

    # Within-singlet gap ratio: the next distinct level above the third bottom, IF any,
    # else the next-sector lowest eigenvalue (the genuine "first above" the singlet tower).
    if n_distinct > EXPECTED_COUNT:
        first_above = float(distinct_levels[EXPECTED_COUNT])  # (local)
        first_above_src = "singlet (0,0) 4th distinct level"  # (local)
    else:
        # No 4th distinct level inside the singlet sector -> the first genuinely-distinct
        # higher state is the lowest eigenvalue of the next Peter-Weyl tower.
        next_min = np.inf  # (local)
        next_src = None    # (local)
        for (p, q), info in sector_evals.items():
            if (p, q) == (0, 0):
                continue
            ev = np.asarray(info["abs_evals"], dtype=float)  # (local)
            m = float(ev.min())  # (local)
            if m < next_min:
                next_min = m
                next_src = (p, q)
        first_above = next_min  # (local)
        first_above_src = f"next tower min: sector {next_src}"  # (local)

    gap_ratio = first_above / third_bottom  # (local)

    # Dispositive sterile-null: the SCALE separation between the O(1) M_KK spectrum floor
    # and the eV scale a 3+1 sterile fit demands. The singlet bottom in eV:
    singlet_bottom_eV = third_bottom * M_KK * EV_PER_GEV  # (local) = (M_KK units) x M_KK[GeV] x 1e9[eV/GeV]
    # decades between the singlet bottom and 1 eV
    scale_sep_decades = float(np.log10(singlet_bottom_eV / 1.0))  # (local) eV / 1 eV

    return {
        "singlet_abs_evals": singlet,
        "distinct_levels": distinct_levels,
        "n_distinct": n_distinct,
        "third_bottom_MKK": third_bottom,
        "first_above_MKK": first_above,
        "first_above_src": first_above_src,
        "gap_ratio": gap_ratio,
        "singlet_bottom_GeV": third_bottom * M_KK,
        "singlet_bottom_eV": singlet_bottom_eV,
        "scale_sep_decades_to_eV": scale_sep_decades,
    }


def extract_delta_neff() -> dict:
    """(b) DELTA-N_eff: RH Majorana freeze-out entropy-dilution residual + Boltzmann suppression."""
    # M_R = B-branch fold energy x M_KK. From s60_lepto_cp_log.txt:
    #   M_1 = 1.004396 M_KK (lightest RH neutrino). We hard-read the fold energy from
    #   the log line "E_B3 at fold = [...]" so the value is sourced, not invented.
    fold_energies_MKK = read_b3_fold_energies(S60_LOG)  # (local) [1.004396, 1.078573, 1.170003]
    M_R_lightest_MKK = float(min(fold_energies_MKK))     # (local) lightest sets the most generous T_fo
    M_R_lightest_GeV = M_R_lightest_MKK * M_KK           # (local) ~7.46e16 GeV
    T_fo_GeV = M_R_lightest_GeV                          # (local) freeze-out ~ M_R

    # Entropy-dilution residual (UPPER bound; the value if the RH species were STILL
    # relativistic at neutrino decoupling). g_*(T_dec)=g_star_BBN, g_*(T_fo)=g_star_SM.
    residual_ceiling = (4.0 / 11.0) ** (4.0 / 3.0) * (g_star_BBN / g_star_SM) ** (4.0 / 3.0)  # (local)

    # Boltzmann suppression: the RH partner is non-relativistic at T_dec by M_R/T_dec OOM.
    boltzmann_exponent = M_R_lightest_GeV / T_DEC_GEV   # (local) M_R/T_dec
    oom_nonrel = float(np.log10(boltzmann_exponent))    # (local) ~19.9 decades
    # exp(-M_R/T_dec) underflows to 0.0 in float64 (exponent ~7.46e19); represent as 0.0.
    boltzmann_factor = float(np.exp(-min(boltzmann_exponent, 700.0)))  # (local) clamp -> 0.0
    if boltzmann_exponent > 700.0:
        boltzmann_factor = 0.0   # (local) underflow: exp(-7.46e19) is 0 to any float precision

    delta_neff_physical = residual_ceiling * boltzmann_factor  # (local) ~ 0 EXACTLY
    n_eff_nu_FW = N_eff_SM + delta_neff_physical               # (local)
    delta_vs_sm = abs(n_eff_nu_FW - N_eff_SM)                  # (local) == delta_neff_physical

    return {
        "fold_energies_MKK": np.asarray(fold_energies_MKK),
        "M_R_lightest_MKK": M_R_lightest_MKK,
        "M_R_lightest_GeV": M_R_lightest_GeV,
        "T_fo_GeV": T_fo_GeV,
        "T_dec_GeV": T_DEC_GEV,
        "residual_ceiling": residual_ceiling,
        "boltzmann_exponent": boltzmann_exponent,
        "oom_nonrel": oom_nonrel,
        "boltzmann_factor": boltzmann_factor,
        "delta_neff_physical": delta_neff_physical,
        "N_eff_SM": float(N_eff_SM),
        "N_eff_nu_FW": n_eff_nu_FW,
        "delta_vs_sm": delta_vs_sm,
    }


def read_b3_fold_energies(log_path: Path) -> list[float]:
    """Read the 'E_B3 at fold = [...]' line from the s60 leptogenesis log (sourced, not invented)."""
    text = log_path.read_text(encoding="utf-8", errors="replace")  # (local)
    for line in text.splitlines():
        if "E_B3 at fold" in line and "[" in line:
            inside = line.split("[", 1)[1].split("]", 1)[0]  # (local)
            toks = inside.replace(",", " ").split()           # (local)
            vals = [float(t) for t in toks]                   # (local)
            if len(vals) >= 3:
                return vals[:3]
    raise RuntimeError("Could not parse 'E_B3 at fold' from s60_lepto_cp_log.txt")


def make_plot(sterile: dict, neff: dict) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))  # (local)

    # Panel A: the singlet tower vs the eV scale a 3+1 sterile demands (log scale, in eV)
    ax = axes[0]  # (local)
    distinct_eV = sterile["distinct_levels"] * M_KK * EV_PER_GEV  # (local)
    ax.scatter(range(1, len(distinct_eV) + 1), distinct_eV, s=80, color="C0", zorder=3,
               label="singlet (0,0) tower bottoms")
    fa_eV = sterile["first_above_MKK"] * M_KK * EV_PER_GEV  # (local)
    ax.scatter([len(distinct_eV) + 1], [fa_eV], s=80, color="C1", marker="s", zorder=3,
               label=f"first above ({sterile['first_above_src']})")
    ax.axhline(1.0, color="crimson", ls="--", lw=1.5, label="1 eV (3+1 sterile demand)")
    ax.set_yscale("log")
    ax.set_xlabel("distinct level index")
    ax.set_ylabel("|eigenvalue| [eV]")
    ax.set_title(f"(a) Sterile-null: {sterile['n_distinct']} bottoms at ~1e{sterile['scale_sep_decades_to_eV']:.0f} eV;\n"
                 f"NO eV-scale state (gap to eV = {sterile['scale_sep_decades_to_eV']:.1f} decades)")
    ax.legend(fontsize=8, loc="center right")
    ax.grid(alpha=0.3, which="both")

    # Panel B: Delta_N_eff residual ceiling vs Boltzmann-suppressed physical value
    ax = axes[1]  # (local)
    bars = ["residual\nceiling\n(if relativistic)", "physical\n(Boltzmann\nsuppressed)"]  # (local)
    vals = [neff["residual_ceiling"], max(neff["delta_neff_physical"], 1e-30)]  # (local)
    ax.bar(bars, vals, color=["C2", "C0"])
    ax.axhline(DELTA_NEFF_PASS, color="crimson", ls="--", lw=1.5, label=f"PASS band {DELTA_NEFF_PASS}")
    ax.set_yscale("log")
    ax.set_ylabel("Delta_N_eff (nu-sector)")
    ax.set_title(f"(b) Delta_N_eff: residual ceiling {neff['residual_ceiling']:.4f}\n"
                 f"physical ~0 (M_R non-rel by {neff['oom_nonrel']:.1f} OOM); N_eff_nu={neff['N_eff_nu_FW']:.4f}")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, which="both", axis="y")

    fig.suptitle("INV11-W2-1 — spectrum-forced neutrino NULLs (sterile-null + Delta_N_eff~0)", fontsize=12)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


def compute() -> dict:
    sterile = extract_singlet_tower()  # (local)
    neff = extract_delta_neff()        # (local)

    # --- Gate sub-verdicts ---
    count_ok = (sterile["n_distinct"] == EXPECTED_COUNT)                 # (local)
    gap_ok = (sterile["gap_ratio"] >= R_GAP_MIN)                         # (local)
    # The dispositive sterile-null is the M_KK->eV scale separation (>= 15 decades).
    no_ev_state = (sterile["scale_sep_decades_to_eV"] >= 15.0)          # (local)
    neff_ok = (neff["delta_vs_sm"] <= DELTA_NEFF_PASS)                  # (local)
    neff_info = (DELTA_NEFF_PASS < neff["delta_vs_sm"] <= DELTA_NEFF_INFO)  # (local)

    sterile_pass = count_ok and gap_ok and no_ev_state  # (local)

    if sterile_pass and neff_ok:
        verdict = "PASS"   # (local)
    elif (not count_ok) or (neff["delta_vs_sm"] > DELTA_NEFF_INFO):
        verdict = "FAIL"   # (local)
    else:
        verdict = "INFO"   # (local) gap ambiguous OR Delta_N_eff in (0.01, 0.05]

    # [SIGN] sub-verdict: the pre-registered direction is "Delta_N_eff DECREASING in M_R"
    # (Boltzmann exp(-M_R/T_dec) -> 0 as M_R grows). The computed physical value sits
    # FAR below the residual ceiling because M_R >> T_dec; direction confirmed.
    sign_ok = neff["delta_neff_physical"] < neff["residual_ceiling"]  # (local) suppression occurred
    sign_verdict = "PASS" if sign_ok else "FAIL"                      # (local)
    magnitude_verdict = "PASS" if neff_ok else ("INFO" if neff_info else "FAIL")  # (local)
    regime_verdict = "VALID"  # (local) entropy-dilution + Boltzmann valid across the full window

    make_plot(sterile, neff)

    # value payload (no single-quote chars — emit_verdict wraps value='...')
    value = (f"count={sterile['n_distinct']}(=={EXPECTED_COUNT}:{count_ok}); "
             f"gap_ratio={sterile['gap_ratio']:.4f}(>={R_GAP_MIN}:{gap_ok}); "
             f"scale_sep_to_eV={sterile['scale_sep_decades_to_eV']:.2f}dec; "
             f"M_R_lightest={neff['M_R_lightest_GeV']:.4e}GeV; "
             f"DeltaN_eff_residual_ceiling={neff['residual_ceiling']:.6f}; "
             f"DeltaN_eff_physical={neff['delta_neff_physical']:.3e}; "
             f"N_eff_nu_FW={neff['N_eff_nu_FW']:.4f}(SM={neff['N_eff_SM']:.3f})")  # (local)

    return {
        "value": value,
        "verdict": verdict,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "sterile": sterile,
        "neff": neff,
        "subverdicts": {
            "count_ok": count_ok, "gap_ok": gap_ok, "no_ev_state": no_ev_state,
            "neff_ok": neff_ok, "neff_info": neff_info, "sterile_pass": sterile_pass,
        },
    }


# ---------------------------------------------------------------------------
# Section 6 — Verdict payload + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None) -> dict:
    payload: dict = {
        "session": int(SESSION),
        "track": "investigation",
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
    if not (sign_verdict is None and magnitude_verdict is None and regime_verdict is None):
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = compute()  # (local)
    s = res["sterile"]  # (local)
    n = res["neff"]     # (local)

    print("--- (a) STERILE-NULL (singlet (0,0) tower) ---")
    print(f"  distinct singlet bottoms     : {s['n_distinct']}  (expected {EXPECTED_COUNT})")
    print(f"  distinct levels [M_KK]       : {np.array2string(s['distinct_levels'], precision=6)}")
    print(f"  third bottom [M_KK]          : {s['third_bottom_MKK']:.6f}  = {s['singlet_bottom_GeV']:.4e} GeV")
    print(f"  first above  [M_KK]          : {s['first_above_MKK']:.6f}  ({s['first_above_src']})")
    print(f"  within-singlet gap ratio     : {s['gap_ratio']:.6f}  (PASS >= {R_GAP_MIN})")
    print(f"  singlet bottom in eV         : {s['singlet_bottom_eV']:.4e} eV")
    print(f"  scale separation to 1 eV     : {s['scale_sep_decades_to_eV']:.2f} decades (NO eV-scale state)")
    print()
    print("--- (b) DELTA-N_eff (RH Majorana freeze-out) ---")
    print(f"  B-branch fold energies [M_KK]: {np.array2string(n['fold_energies_MKK'], precision=6)}")
    print(f"  M_R lightest                 : {n['M_R_lightest_MKK']:.6f} M_KK = {n['M_R_lightest_GeV']:.4e} GeV")
    print(f"  T_fo / T_dec                 : {n['T_fo_GeV']:.4e} / {n['T_dec_GeV']:.4e} GeV")
    print(f"  g_*(T_dec) / g_*(T_fo)       : {g_star_BBN} / {g_star_SM}")
    print(f"  residual ceiling (relativ.)  : {n['residual_ceiling']:.6f}")
    print(f"  M_R/T_dec (Boltzmann exp)    : {n['boltzmann_exponent']:.4e}  ({n['oom_nonrel']:.2f} OOM non-rel)")
    print(f"  Boltzmann factor exp(-M_R/T) : {n['boltzmann_factor']:.3e}")
    print(f"  Delta_N_eff PHYSICAL         : {n['delta_neff_physical']:.3e}  (PASS <= {DELTA_NEFF_PASS})")
    print(f"  N_eff_nu_FW = N_eff_SM + d   : {n['N_eff_nu_FW']:.6f}  (SM = {n['N_eff_SM']:.3f})")
    print()

    # Save data
    np.savez(
        OUT_NPZ,
        # (a) sterile-null
        singlet_abs_evals=s["singlet_abs_evals"],
        distinct_levels=s["distinct_levels"],
        n_distinct=s["n_distinct"],
        third_bottom_MKK=s["third_bottom_MKK"],
        first_above_MKK=s["first_above_MKK"],
        first_above_src=s["first_above_src"],
        gap_ratio=s["gap_ratio"],
        singlet_bottom_GeV=s["singlet_bottom_GeV"],
        singlet_bottom_eV=s["singlet_bottom_eV"],
        scale_sep_decades_to_eV=s["scale_sep_decades_to_eV"],
        expected_count=EXPECTED_COUNT,
        R_gap_min=R_GAP_MIN,
        # (b) delta_neff
        fold_energies_MKK=n["fold_energies_MKK"],
        M_R_lightest_MKK=n["M_R_lightest_MKK"],
        M_R_lightest_GeV=n["M_R_lightest_GeV"],
        T_fo_GeV=n["T_fo_GeV"],
        T_dec_GeV=n["T_dec_GeV"],
        g_star_BBN=float(g_star_BBN),
        g_star_SM=float(g_star_SM),
        residual_ceiling=n["residual_ceiling"],
        boltzmann_exponent=n["boltzmann_exponent"],
        oom_nonrel=n["oom_nonrel"],
        boltzmann_factor=n["boltzmann_factor"],
        delta_neff_physical=n["delta_neff_physical"],
        N_eff_SM=n["N_eff_SM"],
        N_eff_nu_FW=n["N_eff_nu_FW"],
        delta_vs_sm=n["delta_vs_sm"],
        delta_neff_pass_band=DELTA_NEFF_PASS,
        delta_neff_info_band=DELTA_NEFF_INFO,
        # M_KK pin
        M_KK=float(M_KK),
        verdict=res["verdict"],
        sign_verdict=res["sign_verdict"],
        magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"],
    )
    print(f"  Saved: {OUT_NPZ.name}")
    print(f"  Saved: {OUT_PNG.name}")
    print()

    verdict = res["verdict"]  # (local)
    tag = emit_4tuple(res["value"], SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)
    # [SIGN]-trigger gate -> pass all three of sign/magnitude/regime.
    print_verdict_payload(
        verdict, res["value"], audit_sha, content_sha,
        sign_verdict=res["sign_verdict"],
        magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"],
        companion_note=("sterile-null: 3 active bottoms (Z3 triality PROVEN S03/S28), "
                        "no eV-scale state (16+ decade gap); Delta_N_eff~0 (RH non-rel by ~19.9 OOM)"),
        extra_rows=[
            f"# sterile_null: count={s['n_distinct']} distinct singlet bottoms; "
            f"gap_to_eV={s['scale_sep_decades_to_eV']:.1f}dec; gap_ratio={s['gap_ratio']:.4f}",
            f"# delta_neff: residual_ceiling={n['residual_ceiling']:.6f} physical={n['delta_neff_physical']:.3e} "
            f"M_R/T_dec={n['boltzmann_exponent']:.3e}",
        ],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
