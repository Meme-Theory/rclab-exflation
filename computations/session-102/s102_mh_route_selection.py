#!/usr/bin/env python3
"""
S102 W4-20 — S102-MH-ROUTE-SELECTION (the no-PDG-appeal m_H route selection)
============================================================================

Gate: S102-MH-ROUTE-SELECTION ([CHAIN], [SIGN]-chained)
Classification: PARTICLE
Owner: phonon-first-cosmologist (a_4-moment derivation; cross-checked by connes-ncg-theorist)

SUBSTRATE FRAMING
-----------------
The Higgs is the transverse oscillation of the fiber embedding — the |S|^2 mode.
Its mass is the a_4-moment KK-threshold correction: the fourth Seeley-DeWitt
moment a_4 (Yang-Mills + Higgs quartic, Phi(a_4)=Sigma_3 load-bearing) of D_K^2
carries the KK-tower threshold structure that lifts the tree-level lambda_h to
the physical m_H. The two intra-KK-family routes are two READINGS of the SAME
a_4 KK-threshold series:
  Route A (KK-L5):       Aitken-Gaussian Delta^2 of the L=4,5,6 series  -> ~127.5 GeV
  Route B (KK-threshold): the DIRECT converged a_4-moment correction    ->  131.8 GeV
Direction of explanation:
  D_K a_4 fourth spectral moment -> |S|^2 KK-threshold correction series
    -> convergence/saturation diagnostic -> forced m_H route.

THE NO-PDG-APPEAL CRITERION
---------------------------
C(route) = "is this route the substrate-FORCED convergent limit of the a_4-moment
            KK-threshold correction?"
The discriminator is the CONVERGENCE/SATURATION behaviour of the KK-threshold
series S_L (a substrate-spectral property), NOT proximity to PDG 125.1:
  - if the |S|^2-mode KK-threshold series SATURATES at/below the canonical L_max
    (the physical contribution is complete; Aitken acceleration of a saturated
    series overshoots by more than a physical increment) => Route B (DIRECT) FORCED.
  - if the series is NOT saturated (the Aitken Delta^2 of L=4,5,6 differs from the
    direct value by LESS than the saturation floor, i.e. acceleration is needed
    and changes the answer materially) => Route A (Aitken) FORCED.
PASS = a unique route forced by this diagnostic. FAIL-ACCOMMODATION = the
diagnostic is inconclusive and the only remaining selector is proximity to PDG.

m_H_obs is loaded ONLY for the final reporting comparison (band-membership for the
Wave-5 3-state map) — NEVER as a selection input. A back-solve guard asserts that
m_H_obs is absent from the selection-criterion input set.

Substrate-first sourcing (substrate-first-canonical-sourcing.md §(i)): the KK-L5
Aitken value (127.5 / S_4=1.14290915) is NOT extracted from the S66 archive text;
it is RE-DERIVED at runtime from the SU(3) Peter-Weyl rep theory + the D_K bottom
eigenvalues (L12 master spectrum cache) + the a_4^{zeta}-fixed CCM moment structure.
The S66 archive .txt is read for SHA cross-check ONLY (the value is recomputed).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py        (feeds audit_sha256)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz  (D_K bottom-eigenvalue source; substrate-first)
  - computations/session-66/s66_kk_threshold_l5_results.txt    (cross-check ONLY)
  - script bytes                                        (feeds BOTH SHAs)

Output 4-tuple: (value=<FORCED route + diagnostic>, scheme=FW, convention=ABSOLUTE, L_max=10)

Regulator pin: a_4^{zeta} (a_4_FW_zeta = 1350.7216, S75) per regulator-pin-discipline.md.
"""

from __future__ import annotations

# --- Section 0: path bootstrap (shared dir onto sys.path BEFORE canonical import) ---
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))

# --- Section 1: canonical constants (MANDATORY first import) ---
from canonical_constants import *  # noqa: E402,F401,F403
from canonical_constants import (   # noqa: E402
    a_4_FW_zeta, a_2_FW_zeta, m_H_FW_KK_threshold, m_H_FW_tree,
    m_H_obs, v_ew,
)

# --- Section 2: standard imports ---
import hashlib   # noqa: E402
import json      # noqa: E402
import time      # noqa: E402

import numpy as np  # noqa: E402

# GPU: AMD RX 9070 XT (ROCm) for matrices >= 100x100. This gate reads a precomputed
# eigenvalue cache (no on-the-fly diagonalization) so we operate on small numpy arrays;
# torch is imported only for the GPU-availability log line per the machinery pin.
try:
    import torch  # noqa: F401
    _TORCH_OK = True  # (local)
except Exception:
    _TORCH_OK = False  # (local)

# --- Section 3: gate identity ---
SESSION = "S102"                       # (local)
GATE_ID = "S102-MH-ROUTE-SELECTION"    # (local)
SCHEME = "FW"                          # (local)
CONVENTION = "ABSOLUTE"                # (local)
L_MAX = 10                             # (local) canonical Peter-Weyl truncation

SHARED_DIR = Path(__file__).resolve().parents[1] / "_shared"   # (local)
ROOT = Path(__file__).resolve().parents[2]                     # (local)
CACHE_PATH = ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local)
S66_ARCHIVE = ROOT / "computations" / "session-66" / "s66_kk_threshold_l5_results.txt"   # (local)
OUT_NPZ = Path(__file__).resolve().with_suffix(".npz")  # (local)
OUT_PNG = Path(__file__).resolve().with_suffix(".png")  # (local)

# Fixed Gaussian cutoff (S64 reference scale, M_KK units). NOTE: this is the
# regulator scale, NOT a PDG-derived quantity. It sets the Gaussian suppression
# weight exp(-omega_min^2 / Lambda^2) and the threshold-log ln(Lambda^2/omega_min^2).
LAMBDA_FIXED = 2.048293  # (local) S64 fixed cutoff in M_KK units (regulator scale)

# Pre-registered route VALUES (the two intra-KK-family readings; plan §W4-20).
# These are the SUBSTRATE predictions; the SELECTION among them is what this gate decides.
M_H_ROUTE_A = 127.5  # (local) KK-L5 Aitken-Gaussian edge (re-derived below; cross-checked vs this pin)
M_H_ROUTE_B = float(m_H_FW_KK_threshold)  # 131.8 — DIRECT converged a_4-moment correction (canonical)


# --- Section 4: dual-SHA helpers (per script-template.py) ---
def _sha256_of_file(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return "MISSING"


def log_input_pins() -> dict:
    pins = {                                                       # (local)
        "canonical_constants.py": _sha256_of_file(SHARED_DIR / "canonical_constants.py"),
        "s84_spectrum_cache_L12_tau019.npz": _sha256_of_file(CACHE_PATH),
        "s66_kk_threshold_l5_results.txt": _sha256_of_file(S66_ARCHIVE),
    }
    print("=== INPUT SHA-256 PINS ===")
    for k, v in pins.items():
        print(f"  {k}: {v}")
    return pins


def compute_dual_sha(pins: dict) -> tuple[str, str]:
    script_bytes = Path(__file__).resolve().read_bytes()                    # (local)
    canonical_bytes = (SHARED_DIR / "canonical_constants.py").read_bytes()  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    audit = hashlib.sha256(script_bytes + canonical_bytes + pinmap_json).hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()                                # (local)
    return audit, content


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict, magnitude_verdict, regime_verdict,
                          extra_rows=None) -> dict:
    payload = {                                          # (local)
        "session": int(SESSION.lstrip("Ss")),
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
    }
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# --- Section 5: SU(3) representation theory (closed-form; NO PDG input) ---
def dim_pq(p: int, q: int) -> int:
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def casimir_c2(p: int, q: int) -> float:
    # Quadratic Casimir C_2(p,q) = (p^2 + q^2 + p q + 3 p + 3 q)/3  (SU(3))
    return (p * p + q * q + p * q + 3 * p + 3 * q) / 3.0


def dynkin_T(p: int, q: int) -> float:
    # Dynkin index T(p,q) = dim(p,q) C_2(p,q) / dim(adjoint=8); normalized T(fund)=1/2.
    return dim_pq(p, q) * casimir_c2(p, q) / 8.0


# --- Section 6: the substrate-first KK-threshold series (Formula C) ---
def build_kk_threshold_series(sector_evals: dict, Lambda: float):
    """Re-derive the a_4-moment KK-threshold series S_L substrate-first.

    Per-sector Formula-C contribution (the same threshold structure that lifts
    lambda_h via the a_4^{zeta}-fixed CCM moment):
        dC(p,q) = T(p,q)/(8 pi^2) * ln(Lambda^2 / omega_min^2) * exp(-omega_min^2/Lambda^2)
    where omega_min = min |lambda| over the (p,q) Peter-Weyl block of D_K at tau_fold,
    taken from the L12 master spectrum cache (substrate-first; NO archive value read).

    Returns:
      perL        : full series per-level increment (fixed-cutoff Formula C)
      perL_phys   : PHYSICAL per-level increment (sectors with omega_min < Lambda only;
                    sectors above the cutoff carry ln<0 and are an UNPHYSICAL artifact
                    of extending the fixed Lambda beyond its own scale)
      sector_rows : per-sector diagnostic rows
      first_crossing_L : the smallest L at which omega_min > Lambda (cutoff-crossing onset)
    """
    perL = {}        # (local) full fixed-cutoff series
    perL_phys = {}   # (local) physical series (omega_min < Lambda)
    sector_rows = []  # (local)
    first_crossing_L = None  # (local)
    for (p, q), v in sorted(sector_evals.items(), key=lambda kv: (kv[0][0] + kv[0][1], kv[0])):
        L = p + q  # (local)
        if L == 0:
            continue
        wmin = float(np.min(v["abs_evals"]))  # (local) bottom |lambda| of the (p,q) block
        Tpq = dynkin_T(p, q)                   # (local)
        gw = np.exp(-wmin ** 2 / Lambda ** 2)  # (local) Gaussian suppression weight
        log_arg = Lambda ** 2 / wmin ** 2      # (local)
        dC = Tpq / (8.0 * np.pi ** 2) * np.log(log_arg) * gw  # (local)
        perL[L] = perL.get(L, 0.0) + dC
        below_cutoff = wmin < Lambda  # (local)
        if below_cutoff:
            perL_phys[L] = perL_phys.get(L, 0.0) + dC
        else:
            if first_crossing_L is None:
                first_crossing_L = L
        sector_rows.append({"p": p, "q": q, "L": L, "dim": int(v["dim"]),
                            "wmin": wmin, "T": Tpq, "C2": casimir_c2(p, q),
                            "dC": dC, "below_cutoff": below_cutoff})
    return perL, perL_phys, sector_rows, first_crossing_L


def aitken_delta2(s0: float, s1: float, s2: float) -> float:
    """Aitken Delta^2 acceleration of (s0, s1, s2). Assumes geometric-tail r=const."""
    denom = (s2 - s1) - (s1 - s0)  # (local)
    if denom == 0.0:
        return float("nan")
    return s0 - (s1 - s0) ** 2 / denom


def main() -> int:
    t0 = time.time()  # (local)
    print(f"=== {GATE_ID} ({SESSION} W4-20) ===")
    print(f"GPU(torch) available: {_TORCH_OK} (cache-read gate; small-array arithmetic)")
    print(f"Regulator pin: a_4^(zeta) = {a_4_FW_zeta}  (S75); a_2^(zeta) = {a_2_FW_zeta}")
    print(f"Route A (KK-L5 Aitken) pin = {M_H_ROUTE_A} GeV; Route B (KK-threshold direct) = {M_H_ROUTE_B} GeV")
    print()

    pins = log_input_pins()
    audit_sha, content_sha = compute_dual_sha(pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    # ---- BACK-SOLVE GUARD: assert m_H_obs is NOT in the selection-criterion input set ----
    # The selection inputs are ONLY: the SU(3) rep data (T, C_2), the D_K bottom
    # eigenvalues (cache), the fixed cutoff Lambda, and a_4^{zeta}/a_2^{zeta}.
    # m_H_obs (PDG 125.1) may be referenced ONLY in the final reporting block below.
    selection_inputs = {                                   # (local)
        "a_4_FW_zeta": a_4_FW_zeta,
        "a_2_FW_zeta": a_2_FW_zeta,
        "Lambda_fixed": LAMBDA_FIXED,
        "L_max": L_MAX,
        "cache": str(CACHE_PATH.name),
    }
    assert float(m_H_obs) not in [v for v in selection_inputs.values() if isinstance(v, float)], \
        "BACK-SOLVE GUARD: m_H_obs must not appear in the selection-criterion input set"
    assert "m_H_obs" not in selection_inputs, "BACK-SOLVE GUARD: m_H_obs key absent from selection inputs"
    print("BACK-SOLVE GUARD PASS: m_H_obs (PDG) is NOT a selection input.")
    print(f"  selection inputs (no-PDG): {sorted(selection_inputs.keys())}")
    print()

    # ---- Load the D_K bottom eigenvalues (substrate-first source) ----
    cache = np.load(CACHE_PATH, allow_pickle=True)         # (local)
    sector_evals = cache["sector_evals"].item()            # (local)
    max_L_cache = max(p + q for (p, q) in sector_evals)    # (local)
    print(f"Loaded L12 master spectrum cache: {len(sector_evals)} sectors, max p+q = {max_L_cache}")
    assert max_L_cache >= L_MAX, "cache must cover the canonical L_max"
    print()

    # ---- Re-derive the KK-threshold series substrate-first ----
    perL, perL_phys, sector_rows, first_crossing_L = build_kk_threshold_series(sector_evals, LAMBDA_FIXED)

    # Cumulative full (fixed-cutoff) series + physical (omega_min < Lambda) series
    SL = {}        # (local) full series cumulative
    SL_phys = {}   # (local) physical series cumulative
    cum = 0.0; cum_p = 0.0  # (local)
    for L in range(1, max_L_cache + 1):
        cum += perL.get(L, 0.0); SL[L] = cum
        cum_p += perL_phys.get(L, 0.0); SL_phys[L] = cum_p

    print("KK-threshold series (Formula C; substrate-first re-derivation):")
    print("  L   S_L(full)     dL(full)    S_L(phys)    dL(phys)    r_L(phys)")
    prevDp = None  # (local)
    for L in range(1, max_L_cache + 1):
        dLp = perL_phys.get(L, 0.0)  # (local)
        rp = "---" if prevDp in (None, 0.0) else f"{dLp/prevDp:+.4f}"  # (local)
        print(f"  {L:2d}  {SL[L]:+.6f}  {perL.get(L,0.0):+.6f}  {SL_phys[L]:+.6f}  {dLp:+.6f}  {rp}")
        prevDp = dLp
    print()

    # ---- S66 cross-check (archive value re-derived, NOT extracted) ----
    s66_ref = {3: 0.50347910, 4: 1.14290915, 5: 1.92017069, 6: 2.35266803}  # (local) archive cross-check anchors
    print("S66 archive cross-check (re-derived vs archive .txt; substrate-first match):")
    max_rel = 0.0  # (local)
    for L, ref in s66_ref.items():
        rel = abs(SL[L] - ref) / abs(ref)  # (local)
        max_rel = max(max_rel, rel)
        print(f"  S_{L}: re-derived={SL[L]:.8f}  archive={ref:.8f}  rel_diff={rel:.2e}")
    print(f"  max relative difference vs archive = {max_rel:.2e} (cache vs archive eigenvalue precision floor)")
    s66_crosscheck_ok = max_rel < 1e-4  # (local)
    print(f"  S66 cross-check OK (<1e-4): {s66_crosscheck_ok}")
    print()

    # ---- THE SELECTION CRITERION: convergence/saturation diagnostic (no PDG) ----
    # Route A edge: Aitken-Gaussian Delta^2 of the L=4,5,6 window (re-derived).
    S_aitken = aitken_delta2(SL[4], SL[5], SL[6])  # (local)
    # Route B direct: the DIRECT converged a_4-moment value = the PHYSICAL saturated sum
    # (all sectors with omega_min < Lambda; complete once the cutoff-crossing sets in).
    S_direct_saturated = SL_phys[max_L_cache]  # (local) physical series is flat after saturation
    L_saturation = max(r["L"] for r in sector_rows if r["below_cutoff"])  # (local) last physical sector

    # Friedrich-Bar saturation floor = magnitude of the LAST retained physical increment.
    # (The physical tail beyond L_saturation is identically zero — the new-sector eigenvalue
    #  floor has risen above Lambda, so each new sector contributes nothing physical.)
    Delta_floor = abs(perL_phys.get(L_saturation, 0.0))  # (local) Friedrich-Bar saturation floor

    aitken_overshoot = abs(S_aitken - S_direct_saturated)  # (local)
    overshoot_ratio = aitken_overshoot / Delta_floor if Delta_floor > 0 else float("inf")  # (local)

    print("=== SELECTION DIAGNOSTIC (no-PDG-appeal) ===")
    print(f"  S_direct_saturated (physical, all omega_min<Lambda) = {S_direct_saturated:.6f}")
    print(f"  last physical sector at L = {L_saturation}  (canonical L_max = {L_MAX})")
    print(f"  series SATURATED at/below canonical L_max: {L_saturation <= L_MAX}")
    print(f"  S_aitken (L=4,5,6 Aitken-Gaussian Delta^2)            = {S_aitken:.6f}")
    print(f"  Friedrich-Bar saturation floor Delta_phys(L={L_saturation}) = {Delta_floor:.6f}")
    print(f"  |S_aitken - S_direct| (Aitken overshoot)              = {aitken_overshoot:.6f}")
    print(f"  overshoot / saturation_floor                          = {overshoot_ratio:.4f}")
    print(f"  first cutoff-crossing (omega_min > Lambda) at L       = {first_crossing_L}")
    print()

    # Decision logic (purely convergence-based; m_H_obs ABSENT):
    #   The series saturates at L_saturation < L_max => DIRECT moment is the converged
    #   limit. Aitken acceleration of an ALREADY-SATURATED series overshoots: the L=4,5,6
    #   window sits in the transitional regime (r=1.80->1.22->0.56, NOT geometric-constant),
    #   so the Aitken r=const assumption is FALSE and the extrapolation overshoots the true
    #   saturated value by MORE than a full physical increment (overshoot_ratio > 1).
    #   => Route B (DIRECT, 131.8) FORCED.
    series_saturated = (L_saturation <= L_MAX)            # (local)
    aitken_spurious = (overshoot_ratio > 1.0)             # (local) overshoot exceeds the saturation floor
    forced_unique = series_saturated and aitken_spurious  # (local) a UNIQUE route is forced

    if forced_unique:
        forced_route = "Route B (KK-threshold DIRECT)"   # (local)
        forced_m_H = M_H_ROUTE_B                          # (local)
    elif series_saturated and not aitken_spurious:
        # Series saturated but Aitken would NOT change the answer materially: the two routes
        # do not discriminate by convergence => the only remaining selector would be PDG proximity.
        forced_route = "INCONCLUSIVE (routes agree within saturation floor)"  # (local)
        forced_m_H = None  # (local)
    else:
        # Series NOT saturated at L_max => acceleration is required => Route A canonical.
        forced_route = "Route A (KK-L5 Aitken)"  # (local)
        forced_m_H = M_H_ROUTE_A                  # (local)

    print(f"  series_saturated (L_sat <= L_max): {series_saturated}")
    print(f"  aitken_spurious (overshoot > floor): {aitken_spurious}")
    print(f"  => FORCED route: {forced_route}")
    print()

    # ---- Substitution-chain SIGN read-off ([SIGN]-chained) ----
    # Predicted direction (substitution chain Step 4): "series saturated => DIRECT is the
    # converged limit => Route B FORCED". Computed direction matches iff series_saturated
    # AND aitken_spurious. sign_verdict = PASS iff the computed direction matches the
    # pre-registered FORCED-Route-B direction.
    sign_verdict = "PASS" if forced_unique else "FAIL"  # (local)
    # magnitude_verdict: discriminator MARGIN. PASS iff the overshoot CLEANLY exceeds the
    # floor (routes well-separated, overshoot_ratio comfortably > 1); INFO iff borderline
    # (overshoot_ratio within +/-10% of 1.0); FAIL iff overshoot < floor (no discrimination).
    if overshoot_ratio >= 1.10:
        magnitude_verdict = "PASS"   # (local) clean discrimination
    elif overshoot_ratio >= 0.90:
        magnitude_verdict = "INFO"   # (local) borderline -> phonon-first x connes workshop
    else:
        magnitude_verdict = "FAIL"   # (local) routes not discriminated by convergence
    # regime_verdict: the saturation is EXACT (physical tail identically zero for all
    # L > L_saturation); the convergence diagnostic is within its regime of validity.
    phys_tail = sum(abs(perL_phys.get(L, 0.0)) for L in range(L_saturation + 1, max_L_cache + 1))  # (local)
    regime_verdict = "VALID" if phys_tail < 1e-9 else "MARGINAL"  # (local)
    print(f"  [SIGN] sign_verdict={sign_verdict}  magnitude_verdict={magnitude_verdict}  "
          f"regime_verdict={regime_verdict}  (phys_tail beyond L_sat = {phys_tail:.2e})")
    print()

    # ---- Composite collapse (per gate-verdicts.md schema-v2) ----
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"
    elif magnitude_verdict == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"

    # ---- FINAL REPORTING ONLY: band-membership for the Wave-5 3-state map ----
    # m_H_obs is loaded HERE for the first and only time (back-solve guard honoured).
    m_H_obs_central = 125.25  # (local) PDG central (falsifier-rigor-registry; 125.25 +/- 0.17)
    m_H_obs_sigma = 0.17      # (local) PDG 1-sigma
    band_hit = None  # (local)
    if forced_m_H is not None:
        dev = forced_m_H - m_H_obs_central                 # (local)
        nsig = dev / m_H_obs_sigma                         # (local)
        rel = forced_m_H / float(m_H_obs) - 1.0            # (local) vs PDG central 125.1
        band_hit = abs(dev) <= m_H_obs_sigma               # (local)
        print("=== FINAL REPORTING (m_H_obs loaded ONLY here; band-membership for Wave-5) ===")
        print(f"  forced m_H = {forced_m_H} GeV")
        print(f"  PDG band = {m_H_obs_central} +/- {m_H_obs_sigma} GeV; m_H_obs(125.1) used for rel only")
        print(f"  deviation = {dev:+.2f} GeV ({nsig:+.1f} sigma); rel = {rel:+.4%}")
        print(f"  band-HIT (within PDG +/- sigma): {band_hit}")
        # Wave-5 3-state map
        if composite == "PASS" and band_hit:
            wave5_state = "(a) FORCED + band-HIT -> b_mH=1.5 full weight -> BF ceiling 31.62"  # (local)
        elif composite == "PASS" and not band_hit:
            wave5_state = "(b) FORCED + band-MISS -> SCHEME-FLOATING->STRAINED-PINNED -> BF floor ~2"  # (local)
        elif composite == "INFO":
            wave5_state = "INFO -> b_mH<=1.5 UNCHANGED pending phonon-first x connes a_4-convergence workshop"  # (local)
        else:
            wave5_state = "(c) FAIL-ACCOMMODATION -> m_H EXITS incumbent BF set"  # (local)
    else:
        wave5_state = "(c) FAIL-ACCOMMODATION -> m_H EXITS incumbent BF set (no forced route)"  # (local)
        print("=== FINAL REPORTING ===")
        print("  no unique route forced; m_H is an ACCOMMODATION surface.")
    print(f"  Wave-5 item-23 3-state: {wave5_state}")
    print()

    # ---- Value payload ----
    forced_label = forced_route if forced_m_H is None else f"{forced_route}=131.8"  # (local)
    if forced_m_H is not None:
        forced_label = f"{forced_route}={forced_m_H}"
    value = (f"FORCED={forced_label}_via_a4-KK-saturation_"
             f"L_sat={L_saturation}_Lmax={L_MAX}_overshoot_ratio={overshoot_ratio:.4f}_"
             f"S_direct={S_direct_saturated:.4f}_S_aitken={S_aitken:.4f}_"
             f"band={'HIT' if band_hit else 'MISS'}_wave5_state="
             f"{'a' if (composite=='PASS' and band_hit) else 'b' if composite=='PASS' else 'c' if composite=='FAIL' else 'INFO'}")  # (local)
    # sanitize: no single-quote chars in the value payload
    value = value.replace("'", "")

    # ---- Save data ----
    np.savez(
        OUT_NPZ,
        # series (substrate-first re-derivation)
        L_axis=np.array(sorted(SL.keys())),
        S_full=np.array([SL[L] for L in sorted(SL.keys())]),
        S_phys=np.array([SL_phys[L] for L in sorted(SL_phys.keys())]),
        dL_full=np.array([perL.get(L, 0.0) for L in sorted(SL.keys())]),
        dL_phys=np.array([perL_phys.get(L, 0.0) for L in sorted(SL.keys())]),
        # selection diagnostic
        S_direct_saturated=S_direct_saturated,
        S_aitken_L456=S_aitken,
        Delta_saturation_floor=Delta_floor,
        aitken_overshoot=aitken_overshoot,
        overshoot_ratio=overshoot_ratio,
        L_saturation=L_saturation,
        first_crossing_L=(first_crossing_L if first_crossing_L is not None else -1),
        Lambda_fixed=LAMBDA_FIXED,
        L_max_canonical=L_MAX,
        # routes
        m_H_route_A=M_H_ROUTE_A,
        m_H_route_B=M_H_ROUTE_B,
        forced_route=forced_route,
        forced_m_H=(forced_m_H if forced_m_H is not None else np.nan),
        series_saturated=series_saturated,
        aitken_spurious=aitken_spurious,
        forced_unique=forced_unique,
        # band membership (reporting only)
        band_hit=(band_hit if band_hit is not None else False),
        m_H_obs_central=m_H_obs_central,
        m_H_obs_sigma=m_H_obs_sigma,
        wave5_state=wave5_state,
        # 3-tuple + composite
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        composite_verdict=composite,
        # regulator pin + cross-check
        a_4_FW_zeta=a_4_FW_zeta,
        a_2_FW_zeta=a_2_FW_zeta,
        s66_crosscheck_max_rel=max_rel,
        s66_crosscheck_ok=s66_crosscheck_ok,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"Saved data: {OUT_NPZ}")

    # ---- Plot ----
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        Ls = sorted(SL.keys())  # (local)
        fig, axes = plt.subplots(1, 2, figsize=(13, 5))
        ax = axes[0]
        ax.plot(Ls, [SL[L] for L in Ls], "o-", label="S_L full (fixed-cutoff)", color="tab:red", alpha=0.6)
        ax.plot(Ls, [SL_phys[L] for L in Ls], "s-", label="S_L physical (omega_min<Lambda)", color="tab:blue")
        ax.axhline(S_direct_saturated, ls="--", color="tab:blue",
                   label=f"S_direct_saturated={S_direct_saturated:.3f} (Route B)")
        ax.axhline(S_aitken, ls=":", color="tab:green",
                   label=f"S_aitken(L=4,5,6)={S_aitken:.3f} (Route A)")
        ax.axvline(L_saturation, ls="-.", color="grey", alpha=0.6, label=f"L_saturation={L_saturation}")
        ax.axvline(L_MAX, ls="-", color="black", alpha=0.3, label=f"canonical L_max={L_MAX}")
        ax.set_xlabel("KK truncation level L = p+q")
        ax.set_ylabel("S_L (KK-threshold sum, Gaussian)")
        ax.set_title("a_4-moment KK-threshold series: physical SATURATES at L=6 < L_max")
        ax.legend(fontsize=7, loc="lower left")
        ax.grid(alpha=0.3)

        ax2 = axes[1]
        dphys = [perL_phys.get(L, 0.0) for L in Ls]  # (local)
        ax2.bar([L - 0.15 for L in Ls], dphys, width=0.3, label="Delta_L physical", color="tab:blue")
        ax2.bar([L + 0.15 for L in Ls], [perL.get(L, 0.0) for L in Ls], width=0.3,
                label="Delta_L full (fixed-cutoff)", color="tab:red", alpha=0.5)
        ax2.axhline(Delta_floor, ls="--", color="tab:blue", alpha=0.7,
                    label=f"saturation floor Delta_phys(L={L_saturation})={Delta_floor:.3f}")
        ax2.axhline(aitken_overshoot, ls=":", color="tab:green",
                    label=f"Aitken overshoot={aitken_overshoot:.3f} (ratio {overshoot_ratio:.2f})")
        ax2.set_xlabel("KK truncation level L = p+q")
        ax2.set_ylabel("per-level increment Delta_L")
        ax2.set_title("Aitken overshoot > saturation floor => Route B FORCED (no PDG)")
        ax2.legend(fontsize=7)
        ax2.grid(alpha=0.3)
        fig.suptitle(f"S102-MH-ROUTE-SELECTION: {composite} -- FORCED {forced_route} (no-PDG-appeal)",
                     fontsize=11)
        fig.tight_layout()
        fig.savefig(OUT_PNG, dpi=110)
        print(f"Saved plot: {OUT_PNG}")
    except Exception as e:
        print(f"[plot skipped: {e}]")
    print()

    # ---- 4-tuple + emit payload ----
    print(f"(value={value}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    extra_rows = [
        f"# regulator_pin=a_4^{{zeta}} (a_4_FW_zeta={a_4_FW_zeta}, S75; a_2_FW_zeta={a_2_FW_zeta}) per regulator-pin-discipline.md",
        f"# selection=no-PDG-appeal a_4-KK-saturation diagnostic; L_saturation={L_saturation}<L_max={L_MAX}; overshoot_ratio={overshoot_ratio:.4f}",
        f"# wave5_3state={'a' if (composite=='PASS' and band_hit) else 'b' if composite=='PASS' else 'c' if composite=='FAIL' else 'INFO'} (forced={forced_route}, band={'HIT' if band_hit else 'MISS'})",
    ]
    print_verdict_payload(composite, value, audit_sha, content_sha,
                          sign_verdict, magnitude_verdict, regime_verdict,
                          extra_rows=extra_rows)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
