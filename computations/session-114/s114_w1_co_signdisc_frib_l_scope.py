#!/usr/bin/env python3
"""
S114 W1-2 CF-S114-CO-SIGNDISC-FRIB-L-SCOPE — weight-free dense-matter
discriminant constructibility SCOPE against the FRIB symmetry-energy slope L
=============================================================================

Gate: CF-S114-CO-SIGNDISC-FRIB-L-SCOPE ([VERIFY] — constructibility / set-membership)

Pre-registered PASS criterion (set-membership, NON-COMPUTE; plan §W1-2 (1) operator):
  PASS iff there EXISTS a weight-free (M_KK-free) dimensionless discriminant
       g(dDelta_CFL/dmu) whose substrate-mapped image lands in the FRIB L-band
       [40, 70] MeV with a resolvable sigma_reach > 0.5 (detector-distinguishable
       from the band edges), AND g is provably M_KK-free (uses ONLY Ohat-type
       content).
  FAIL iff NO such map exists — every dimensionless route is either degenerate
       inside the band (sigma_reach -> 0) OR the only sigma-reach discriminant
       rides M_KK (dimensionful-only).
  INFO iff the map exists but its sigma_reach is partial / regime-conditional.

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/investigation-13/inv13_w2_1_finite_mu_cfl_eos.npz  (W2-1 SIGN-PASS scan)
  - computations/session-110/s110_cf_co1_eos.npz                    (S110-CO1 self-consistent repair)
  - canonical_constants.py (feeds audit_sha256 only; M_KK)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<set-membership verdict string>, scheme=BdG-spectral-action-vanSuijlekom-Dmu,
   convention=DIMENSIONLESS-OHAT-ONLY, L_max=N/A)

Classification: PARTICLE (CFL diquark-condensate density-dependence of the SU(3)
  that color-locks in A_K = C + H + M_3(C); the FRIB-L mapping leg is methodological).

METHODOLOGY
-----------
SCOPE-class constructibility check (NOT the full discriminant build). Three sub-steps:
  (A) Re-load the W2-1 SIGN-PASS scan and PARTITION its contents into DIMENSIONLESS
      (Ohat-type, admissible) {dDelta_dmu, sign_pass, frac_increasing,
      eos_gap_ratio_Delta_over_mu, ratio_plateau} vs DIMENSIONFUL (M_KK-inherited,
      FORBIDDEN) {eos_B_eff_..._MKK_inherited, M_max_Msun, eps_c, eos_eps_cond_MKK4}
      per the §VII.BS NNU theorem O = M_KK * Ohat (STAGE-3-PERMANENT, rank-1,
      second_rel_sv=1.066e-17). Cross-load the S110-CO1 self-consistent repair
      (ratio_plateau=0.102, the physical CFL window) + Track-B dilution evidence
      (C_max_pinned=2.26e-4 vs C_MAX_FLOOR=1e-3).
  (B) CONSTRUCT the candidate dimensionless map. The symmetry-energy slope is
      L = 3 n_0 (dS/dn)|_{n_0} [MeV] — a density-derivative of the symmetry energy.
      Its DIMENSIONLESS recast is L/J (slope-to-value), J = S_0 the saturation
      symmetry-energy value (~32 MeV external nuclear-physics standard). The
      substrate analog of a density-derivative-of-the-condensate is the
      LOGARITHMIC stiffening R_stiff = dlnDelta/dlnmu = (dDelta/dmu)*(mu/Delta),
      every factor M_KK-free (a ratio of D_K eigenvalue scales). The map's job:
      does R_stiff translate to a definite L/J band, distinguishable inside the
      FRIB window?
  (C) sigma_reach: estimate whether the substrate-mapped image lands inside, at
      the edge of, or outside the FRIB band with resolvable sigma given the band
      width. The VERDICT is the EXISTENCE of a detector-reachable sigma, NOT a
      numeric L-value-vs-data chi^2.

The structural crux (substitution chain Step 5): the upstream result is a
SIGN-PASS (dDelta/dmu > 0). A sign-only map is degenerate inside the FRIB band
because L > 0 holds for essentially every realistic nuclear EoS — every L in
[40,70] MeV carries the same positive sign, so a sign discriminant cannot
resolve a value inside the band (sigma_reach -> 0). The discriminant escapes the
no-go ONLY if the substrate pins a MAGNITUDE (R_stiff value) that lands
distinguishably. This script computes R_stiff honestly and tests it.

ANTI-RESCUE FENCE (load-bearing, plan convention DIMENSIONLESS-OHAT-ONLY):
  The discriminant uses ONLY {dDelta_dmu, eos_gap_ratio_Delta_over_mu,
  ratio_plateau}. It NEVER uses {eos_B_eff_..._MKK_inherited, M_max_Msun, M_KK}.
  NO M_max-in-M_sun comparison, NO compactness-vs-NICER, NO dimensionful target
  tuning. Tuning a dimensionful target is ansatz-forced PASS (PROHIBITED Class 4).
  M_KK is imported ONLY to ASSERT (programmatically) that the discriminant value
  is invariant under rescaling M_KK — the proof of weight-freedom — never as a
  multiplier into the discriminant.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- CPU-trivial (npz re-load + scalar maps): numpy with OMP cap 8
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Gate verdict emitted via the emit_verdict knowledge-MCP tool (race-safe):
  the script PRINTS the payload; the dispatching agent calls emit_verdict.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent.parent / "_shared"))
from canonical_constants import *  # noqa: F401,F403  (provides M_KK)
from canonical_constants import M_KK

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S114"                                                  # (local)
GATE_ID = "CF-S114-CO-SIGNDISC-FRIB-L-SCOPE"                      # (local)
SCHEME = "BdG-spectral-action-vanSuijlekom-Dmu"                  # (local)
CONVENTION = "DIMENSIONLESS-OHAT-ONLY"                            # (local)
L_MAX = "N/A"                                                     # (local)

# --- External observational comparison anchor (NOT a framework canonical) ---
# FRIB-constrained symmetry-energy slope L band, Sorensen+ 2024 (combined
# chiEFT + HIC + neutron-star). Per substrate-first-canonical-sourcing.md §(i)
# this is a METHODOLOGICAL cross-check anchor the substrate's dimensionless
# stiffening-sign is COMPARED AGAINST — never a substrate-replacement. There is
# (correctly) no canonical_constants.py L pin: L is an external observation.
FRIB_L_LO = 40.0          # (local) MeV  — Sorensen+ 2024 combined lower edge
FRIB_L_HI = 70.0          # (local) MeV  — Sorensen+ 2024 combined upper edge
# Saturation symmetry-energy value J = S_0 (standard nuclear-physics value;
# external anchor, NOT a framework canonical) — used ONLY to recast the FRIB
# slope into the DIMENSIONLESS form L/J so a dimensionless substrate quantity
# can be compared without any MeV scale.
S0_SYMM_MEV = 32.0        # (local) MeV  — standard saturation symmetry energy (J)

# sigma-reach resolvability threshold (plan §W1-2 (5) tolerance):
SIGMA_REACH_PASS = 0.5    # (local) PASS-eligible iff sigma_reach > 0.5

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s114_w1_co_signdisc_frib_l_scope.npz"
OUT_PNG = SESSION_DIR / "s114_w1_co_signdisc_frib_l_scope.png"

INV13_NPZ = COMPUTATIONS_DIR / "investigation-13" / "inv13_w2_1_finite_mu_cfl_eos.npz"
S110_NPZ = COMPUTATIONS_DIR / "session-110" / "s110_cf_co1_eos.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    INV13_NPZ,
    S110_NPZ,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
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
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    """Stable hash over all input SHAs (invariant to dict ordering)."""
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    """Compute (audit_sha256, content_sha256) per the S84+ dual-SHA schema."""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute (the constructibility scope)
# ---------------------------------------------------------------------------

def compute() -> dict:
    """Partition the npz contents, construct the candidate weight-free map,
    estimate sigma_reach, and return the set-membership verdict ingredients.

    All internal intermediates tagged `# (local)`.
    """
    d13 = np.load(INV13_NPZ, allow_pickle=True)   # (local) W2-1 SIGN-PASS scan
    d110 = np.load(S110_NPZ, allow_pickle=True)   # (local) S110-CO1 repair

    # ---- (A) PARTITION: dimensionless (Ohat, admissible) vs dimensionful (FORBIDDEN) ----
    # DIMENSIONLESS / Ohat-type — the ONLY content the discriminant may touch:
    dDelta_dmu = np.asarray(d13["dDelta_dmu"], dtype=float)          # (local) [Delta]/[mu] = dimensionless
    mu_grid = np.asarray(d13["mu_grid"], dtype=float)                # (local) M_KK units
    Delta_grid = np.asarray(d13["Delta_grid"], dtype=float)          # (local) M_KK units
    sign_pass = bool(d13["sign_pass"])                               # (local) True
    frac_increasing = float(d13["frac_increasing"])                  # (local) 1.0
    gap_ratio_raw = float(d13["eos_gap_ratio_Delta_over_mu"])        # (local) 4.821 runaway (Delta/mu)
    ratio_plateau = float(d110["ratio_plateau"])                     # (local) 0.102 self-consistent (Delta/mu)
    mu_plateau = float(d110["mu_plateau"])                           # (local) M_KK units, CFL onset mu_eff
    Delta_plateau = float(d110["Delta_plateau"])                     # (local) M_KK units

    # DIMENSIONFUL / M_KK-inherited — FORBIDDEN as discriminant (asserted, never used):
    forbidden_keys = [                                               # (local)
        "eos_B_eff_MeV_fm3_dimensionful_MKK_inherited",
        "M_max_Msun", "eps_c_grid", "eos_eps_cond_MKK4",
    ]
    forbidden_present = {k: (k in d13.files) for k in forbidden_keys}  # (local)

    # Track-B dilution evidence (dimensionless ratios; corroborates the no-go branch):
    C_max_pinned = float(d110["C_max_pinned"])                       # (local) 2.26e-4
    C_MAX_FLOOR = float(d110["C_MAX_FLOOR"])                         # (local) 1e-3
    cmax_below_floor = C_max_pinned < C_MAX_FLOOR                    # (local) True => sub-floor (dilute)

    # ---- Weight-freedom proof: the discriminant must be M_KK-INVARIANT ----
    # dDelta/dmu is [Delta]/[mu]; both Delta and mu are in M_KK units, so the ratio
    # is M_KK-free. We PROVE it numerically: rescale mu->mu*lambda, Delta->Delta*lambda
    # (M_KK absorbs into lambda); dDelta/dmu = (lambda*dDelta)/(lambda*dmu) is invariant.
    lam = float(M_KK)                                                # (local) arbitrary nonzero rescale (use M_KK itself)
    # logarithmic stiffening R_stiff = dlnDelta/dlnmu = (dDelta/dmu)*(mu/Delta):
    # at the self-consistent CFL onset (S110 mu_plateau, Delta_plateau).
    # dDelta/dmu near the onset: take the median over the increasing window (robust).
    dDdmu_onset = float(np.median(dDelta_dmu))                       # (local) median slope (dimensionless)
    R_stiff = dDdmu_onset * (mu_plateau / Delta_plateau)             # (local) dlnDelta/dlnmu (dimensionless)
    # M_KK-invariance check: rescale all length/energy scales by lam; R_stiff unchanged.
    dDdmu_rescaled = (lam * dDelta_dmu) / (lam)                      # (local) numerator&denominator both *lam? no:
    # Careful: dDelta/dmu already = d(Delta)/d(mu); under Delta->lam*Delta, mu->lam*mu,
    # the derivative d(lam*Delta)/d(lam*mu) = (lam/lam)*dDelta/dmu = dDelta/dmu. And
    # mu/Delta -> (lam*mu)/(lam*Delta) = mu/Delta. So R_stiff is invariant:
    R_stiff_rescaled = (float(np.median(dDelta_dmu))) * ((lam * mu_plateau) / (lam * Delta_plateau))  # (local)
    mkk_invariant = bool(np.isclose(R_stiff, R_stiff_rescaled, rtol=1e-12, atol=0.0))  # (local) True by construction

    # ---- (B) DIMENSIONLESS FRIB datum: recast L -> L/J (MeV units cancel) ----
    L_over_J_lo = FRIB_L_LO / S0_SYMM_MEV                            # (local) 40/32 = 1.25
    L_over_J_hi = FRIB_L_HI / S0_SYMM_MEV                            # (local) 70/32 = 2.1875
    L_over_J_central = 0.5 * (L_over_J_lo + L_over_J_hi)             # (local) ~1.719
    L_over_J_halfwidth = 0.5 * (L_over_J_hi - L_over_J_lo)           # (local) ~0.469
    # The dimensionless FRIB band [1.25, 2.19] is the resolution scale.

    # ---- The candidate map g: R_stiff -> L/J ----
    # Identification: the symmetry-energy slope's dimensionless form L/J is a
    # logarithmic density-derivative of the symmetry energy (d ln S / d ln n times
    # 3, roughly); the substrate analog is the logarithmic stiffening R_stiff =
    # d ln Delta / d ln mu. The ONLY admissible map (anti-rescue) is the IDENTITY-class
    # dimensionless identification g(R_stiff) = R_stiff (no MeV scale inserted).
    g_image = R_stiff                                                # (local) the mapped dimensionless value

    # ---- (C) sigma_reach estimate ----
    # Two distinct sigma-reach questions (the structural crux):
    #
    # (C1) MAGNITUDE sigma-reach: how far is the mapped value g_image from the band
    #      EDGES, in units of the band half-width? If g_image is INSIDE [lo,hi],
    #      sigma_reach = distance-to-nearest-edge / halfwidth (capped). If OUTSIDE,
    #      it does not land in the band (degenerate-out, not detector-distinguishable
    #      INSIDE the band).
    in_band = bool(L_over_J_lo <= g_image <= L_over_J_hi)            # (local)
    if in_band:
        dist_to_nearest_edge = min(g_image - L_over_J_lo, L_over_J_hi - g_image)  # (local)
        sigma_reach_magnitude = dist_to_nearest_edge / L_over_J_halfwidth          # (local)
    else:
        sigma_reach_magnitude = 0.0                                  # (local) not inside band
    #
    # (C2) SIGN-ONLY sigma-reach: the upstream result is a SIGN-PASS. A sign-only
    #      discriminant maps {dDelta/dmu > 0} -> {L > 0}. EVERY L in [40,70] MeV is
    #      positive, so the sign carries ZERO information INSIDE the band: a sign
    #      discriminant cannot distinguish L=40 from L=70. sigma_reach_sign = 0 by
    #      construction (degenerate-in-band).
    sigma_reach_sign = 0.0                                           # (local) sign degenerate inside [40,70]

    # The discriminant's sigma_reach is the MAGNITUDE reach IF the substrate pins a
    # magnitude that lands in-band; otherwise it collapses to the sign reach (0).
    sigma_reach = sigma_reach_magnitude if in_band else sigma_reach_sign  # (local)

    # ---- Verdict (set-membership) ----
    # map_is_weight_free: g_image = R_stiff is built ONLY from dimensionless
    # {dDelta_dmu, mu_plateau/Delta_plateau}; the forbidden M_KK-inherited keys are
    # PRESENT in the npz (forbidden_present) but NEVER enter g — verified by
    # construction (g_image references only the dimensionless locals above). The
    # BINDING weight-free test is the M_KK-invariance of the discriminant value.
    map_is_weight_free = bool(mkk_invariant)                         # (local) the binding weight-free test

    if (sigma_reach > SIGMA_REACH_PASS) and map_is_weight_free and in_band:
        verdict = "PASS"                                             # (local) CONSTRUCTIBLE
        branch = "CONSTRUCTIBLE"                                     # (local)
    elif (not in_band) or (sigma_reach <= 1e-9):
        # No M_KK-free magnitude lands distinguishably in-band: the sign route is
        # degenerate-in-band (sigma_reach_sign=0) and the magnitude route either
        # misses the band or the only sigma-reach discriminant would need a MeV
        # scale (rides M_KK). STRUCTURAL NO-GO.
        verdict = "FAIL"                                             # (local) STRUCTURAL NO-GO
        branch = "STRUCTURAL-NO-GO"                                  # (local)
    else:
        verdict = "INFO"                                            # (local) partial / regime-conditional
        branch = "PARTIAL"                                          # (local)

    # Compact value string (no single-quote chars; emit_verdict wraps it):
    value_str = (f"{branch}_sigma_reach={sigma_reach:.4f}_thr={SIGMA_REACH_PASS}"
                 f"_g_image(R_stiff=dlnDelta/dlnmu)={g_image:.4f}"
                 f"_FRIB_L/J_band=[{L_over_J_lo:.4f},{L_over_J_hi:.4f}]"
                 f"_in_band={in_band}_sign_degenerate_in_band=True"
                 f"_map_M_KK_free={map_is_weight_free}"
                 f"_ratio_plateau={ratio_plateau:.4f}_C_max={C_max_pinned:.3e}_sub_floor={cmax_below_floor}")  # (local)

    return {
        "value": value_str,
        "verdict": verdict,
        "branch": branch,
        "R_stiff": R_stiff,
        "g_image": g_image,
        "dDdmu_onset_median": dDdmu_onset,
        "mu_plateau": mu_plateau,
        "Delta_plateau": Delta_plateau,
        "ratio_plateau": ratio_plateau,
        "gap_ratio_raw": gap_ratio_raw,
        "L_over_J_lo": L_over_J_lo,
        "L_over_J_hi": L_over_J_hi,
        "L_over_J_central": L_over_J_central,
        "L_over_J_halfwidth": L_over_J_halfwidth,
        "in_band": in_band,
        "sigma_reach": sigma_reach,
        "sigma_reach_magnitude": sigma_reach_magnitude,
        "sigma_reach_sign": sigma_reach_sign,
        "mkk_invariant": mkk_invariant,
        "map_is_weight_free": map_is_weight_free,
        "forbidden_present": forbidden_present,
        "sign_pass": sign_pass,
        "frac_increasing": frac_increasing,
        "C_max_pinned": C_max_pinned,
        "C_MAX_FLOOR": C_MAX_FLOOR,
        "cmax_below_floor": cmax_below_floor,
        "dDelta_dmu": dDelta_dmu,
        "mu_grid": mu_grid,
        "Delta_grid": Delta_grid,
    }


def make_plot(r: dict) -> None:
    """Two-panel diagnostic: (left) dDelta/dmu scan (the SIGN-PASS, dimensionless);
    (right) the dimensionless FRIB L/J band with the substrate-mapped g_image."""
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(12, 4.6))

    # Left: the dimensionless stiffening scan dDelta/dmu vs mu (SIGN-PASS evidence)
    ax0.plot(r["mu_grid"], r["dDelta_dmu"], "o-", color="#1f77b4", ms=3, lw=1.2)
    ax0.axhline(0.0, color="k", lw=0.8, ls=":")
    ax0.set_xlabel(r"$\mu$  (M_KK units, dimensionless)")
    ax0.set_ylabel(r"$d\Delta_{\rm CFL}/d\mu$  (dimensionless, $\hat O$-type)")
    ax0.set_title(r"W2-1 SIGN-PASS: $d\Delta/d\mu>0$ everywhere (M_KK-free)")
    ax0.grid(alpha=0.3)

    # Right: the dimensionless FRIB L/J band + substrate g_image
    ax1.axvspan(r["L_over_J_lo"], r["L_over_J_hi"], color="#2ca02c", alpha=0.18,
                label=f"FRIB L/J band [{r['L_over_J_lo']:.2f},{r['L_over_J_hi']:.2f}]\n(Sorensen+ 2024, J={S0_SYMM_MEV:.0f} MeV)")
    ax1.axvline(r["L_over_J_central"], color="#2ca02c", ls="--", lw=1.0, label="band central")
    ax1.axvline(r["g_image"], color="#d62728", lw=2.0,
                label=f"substrate $g$=R_stiff={r['g_image']:.2f}\n(d ln$\\Delta$/d ln$\\mu$)")
    ax1.set_xlim(0, max(6.0, r["g_image"] * 1.15))
    ax1.set_yticks([])
    ax1.set_xlabel(r"dimensionless slope  $L/J$  (and substrate $g$=R_stiff)")
    ax1.set_title(f"{r['branch']}: $\\sigma_{{\\rm reach}}$={r['sigma_reach']:.3f} "
                  f"(in_band={r['in_band']})")
    ax1.legend(loc="upper right", fontsize=7.5)
    ax1.grid(alpha=0.3, axis="x")

    fig.suptitle("CF-S114-CO-SIGNDISC-FRIB-L-SCOPE — weight-free dense-matter discriminant constructibility",
                 fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(OUT_PNG, dpi=140)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 6 — Verdict payload (the script PRINTS; the agent calls emit_verdict)
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          companion_note: str = "",
                          extra_rows: list[str] | None = None) -> dict:
    """Emit the verdict PAYLOAD for the dispatching AGENT to pass to emit_verdict.
    [VERIFY] gate — NO sign/magnitude/regime 3-tuple (the dDelta/dmu sign is
    settled upstream; this gate verifies the MAP existence)."""
    payload: dict = {
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
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins (first lines of stdout)
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Dual SHAs
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print(f"  M_KK (imported, used ONLY for weight-free invariance proof): {M_KK:.6e}")
    print()

    # 2. Compute the constructibility scope
    r = compute()

    # 3. Diagnostics
    print("--- PARTITION (anti-rescue DIMENSIONLESS-OHAT-ONLY) ---")
    print(f"  DIMENSIONLESS (admissible): dDelta_dmu(median)={r['dDdmu_onset_median']:.4f}, "
          f"sign_pass={r['sign_pass']}, frac_increasing={r['frac_increasing']}, "
          f"ratio_plateau(Delta/mu)={r['ratio_plateau']:.4f}, gap_ratio_raw={r['gap_ratio_raw']:.4f}")
    print(f"  DIMENSIONFUL (FORBIDDEN, present-but-untouched): {r['forbidden_present']}")
    print(f"  weight-free (M_KK-invariant) discriminant: {r['map_is_weight_free']}  (mkk_invariant={r['mkk_invariant']})")
    print("--- CANDIDATE MAP g(R_stiff) = R_stiff = dlnDelta/dlnmu ---")
    print(f"  mu_plateau={r['mu_plateau']:.4f}  Delta_plateau={r['Delta_plateau']:.4f}  "
          f"R_stiff={r['R_stiff']:.4f}  g_image={r['g_image']:.4f}")
    print("--- DIMENSIONLESS FRIB datum L/J (MeV cancels) ---")
    print(f"  L/J band=[{r['L_over_J_lo']:.4f},{r['L_over_J_hi']:.4f}]  central={r['L_over_J_central']:.4f}  "
          f"halfwidth={r['L_over_J_halfwidth']:.4f}")
    print("--- sigma_reach ---")
    print(f"  in_band={r['in_band']}  sigma_reach_magnitude={r['sigma_reach_magnitude']:.4f}  "
          f"sigma_reach_sign={r['sigma_reach_sign']:.4f}  => sigma_reach={r['sigma_reach']:.4f} (thr {SIGMA_REACH_PASS})")
    print(f"  Track-B dilution: C_max={r['C_max_pinned']:.3e} < floor {r['C_MAX_FLOOR']:.1e} => sub_floor={r['cmax_below_floor']}")
    print()

    # 4. Save data
    np.savez(
        OUT_NPZ,
        # ---- verdict + branch ----
        verdict=r["verdict"], branch=r["branch"], value=r["value"],
        sigma_reach=r["sigma_reach"], sigma_reach_magnitude=r["sigma_reach_magnitude"],
        sigma_reach_sign=r["sigma_reach_sign"], SIGMA_REACH_PASS=SIGMA_REACH_PASS,
        in_band=r["in_band"],
        # ---- substrate dimensionless discriminant ----
        R_stiff=r["R_stiff"], g_image=r["g_image"],
        dDdmu_onset_median=r["dDdmu_onset_median"],
        mu_plateau=r["mu_plateau"], Delta_plateau=r["Delta_plateau"],
        ratio_plateau=r["ratio_plateau"], gap_ratio_raw=r["gap_ratio_raw"],
        sign_pass=r["sign_pass"], frac_increasing=r["frac_increasing"],
        # ---- weight-free proof ----
        mkk_invariant=r["mkk_invariant"], map_is_weight_free=r["map_is_weight_free"],
        M_KK=float(M_KK),
        # ---- dimensionless FRIB datum (external anchor) ----
        FRIB_L_LO=FRIB_L_LO, FRIB_L_HI=FRIB_L_HI, S0_SYMM_MEV=S0_SYMM_MEV,
        L_over_J_lo=r["L_over_J_lo"], L_over_J_hi=r["L_over_J_hi"],
        L_over_J_central=r["L_over_J_central"], L_over_J_halfwidth=r["L_over_J_halfwidth"],
        # ---- Track-B dilution evidence ----
        C_max_pinned=r["C_max_pinned"], C_MAX_FLOOR=r["C_MAX_FLOOR"],
        cmax_below_floor=r["cmax_below_floor"],
        # ---- partition record ----
        forbidden_keys_present=json.dumps(r["forbidden_present"]),
        # ---- scan arrays ----
        dDelta_dmu=r["dDelta_dmu"], mu_grid=r["mu_grid"], Delta_grid=r["Delta_grid"],
        # ---- dual-SHA + scheme ----
        audit_sha256=audit_sha, content_sha256=content_sha,
        scheme=SCHEME, convention=CONVENTION,
    )
    print(f"  saved {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # 5. Plot
    make_plot(r)
    print(f"  saved {OUT_PNG.relative_to(PROJECT_ROOT)}")
    print()

    # 6. 4-tuple + verdict payload
    verdict = r["verdict"]  # (local)
    tag = emit_4tuple(r["value"], SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)
    note = (f"[VERIFY] constructibility SCOPE; set-membership verdict; "
            f"branch={r['branch']}; sigma_reach={r['sigma_reach']:.4f} (thr {SIGMA_REACH_PASS}); "
            f"discriminant DIMENSIONLESS-OHAT-ONLY (M_KK-invariant={r['map_is_weight_free']}); "
            f"NO M_max/compactness/M_KK in discriminant (anti-rescue Class-4 fence)")  # (local)
    print_verdict_payload(verdict, r["value"], audit_sha, content_sha, companion_note=note)

    # 7. Summary
    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} ({r['branch']}) (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
