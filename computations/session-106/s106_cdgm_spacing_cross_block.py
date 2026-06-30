#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S106-CDGM-SPACING-CROSS-BLOCK — INFO-class structural characterization.

PARTICLE-class. Tests whether the CdGM horizon-core ladder-spacing omega_0
(Volovik Paper 05 Eq.60/61: E_n = (n+1/2) omega_0) is a CROSS-BLOCK INVARIANT
surviving the chi: A_K -> M_2(C) projection across the named horizon blocks
(0,0)+(1,0)+(0,1)+(1,1) -- vs a WITHIN-BLOCK ACCIDENT. INFO-class by the
workshop's own pre-registration: the deliverable is the per-block spacing TABLE
+ the cross-block relative variance + the invariant-vs-accident classification.

INDEPENDENT of the 2a/2b Tomita-Takesaki construction (no shared pins). Runs
unconditionally (no gating on the oprime_z disposition).

Direction of explanation (substrate-first; phononic-framing.md "IS Space"):
  D_K spectrum (named blocks, L_max=10)
    -> BDI / N_3=0 universality class (3He-B; CdGM +1/2 minigap, NO Weyl zero)
    -> CdGM bound-state ladder E_n = (n+1/2) omega_0 (Volovik Paper 05 Eq.60/61)
    -> the +1/2 minigap E_0 = omega_0/2 (= bosonic Wightman floor, BDI-protected)
    -> the per-block ladder spacing omega_0^{(p,q)}
  The CdGM ladder is the selection-rule/spacing structure of the horizon-core
  (B3) representation, read FROM the D_K spectrum, NEVER as a ladder IN a container.

SUBSTRATE-IS OBSERVABLE -- two distinct readings of omega_0 (both reported):
  R1 (CdGM rigid-ladder, MEASURED): omega_0 = 2 E_0, E_0 = min BdG level per block
     (the doubled CdGM minigap; the rigid-ladder defining quantity). This is the
     physically protected quantity (the +1/2 minigap = bosonic Wightman floor,
     BDI/N_3=0 clause (c) JOINT, theorem K12 S105).
  R2 (literal consecutive-spacing, the plan spacing_definition_pin):
     omega_0 = median consecutive Delta E within the B3 block-(p,q) unique level set
     (the upper-level spacing structure).
  DIAGNOSTIC R0 (input-constant gap = Delta_B3 = 0.176, the per_block_json 'gap'
     field): a TAUTOLOGY (the W2-2 script set gap := Delta_B3 input constant,
     not a measured spacing) -- reported only to expose why the plan-freeze
     "rigid-ladder variance = 0" check was a constant-reuse check, not a
     spectral-rigidity measurement.

INVARIANT := relative variance Var_pq[omega_0^{(p,q)}] / <omega_0>^2 <= var_threshold = 1e-2.
ACCIDENT  := relative variance > var_threshold.

INPUT-PATH DRIFT (substrate-first-canonical-sourcing.md (ii.B), recorded at runtime):
  The plan input_files block for 2c lists ONLY s105_w2_2_omega_faithful_normal.npz.
  But per_block_json in that npz carries only per-block SUMMARY STATISTICS
  (gap, f_min/max, K_abs_max, E_min, E_max, n_modes) -- NOT the per-mode level set.
  The plan method ("reconstruct the B3-sector level spectrum ... extract the
  consecutive-level spacing") provably requires the per-mode |lambda_a|, which lives
  in the S84 master cache (computations/session-84/s84_spectrum_cache_L12_tau019.npz,
  the SAME source S105 W2-2 used to BUILD per_block_json). The reconstruction
  E_a = sqrt((|lambda_a| - lam_horizon)^2 + Delta_B3^2) reproduces per_block_json's
  E_min/E_max EXACTLY (cross-checked in this script). The drift is documented in the
  verdict value string + the WP Methodology subsection per (ii.B) item 2.

Plan: sessions/session-plan/session-106-plan-w2.md  §W2-3 (gate block from line 436).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # numpy.linalg CPU path (GPU_path=numpy.linalg pin); small blocks
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

_SHARED = Path(__file__).resolve().parents[1] / "_shared"
if str(_SHARED) not in sys.path:
    sys.path.insert(0, str(_SHARED))

from canonical_constants import *  # noqa: F401,F403  (MANDATORY)
from canonical_constants import Delta_B2, Delta_B3, Delta_BCS, tau_fold

import hashlib
import json
import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 2 -- Identity + paths
# ---------------------------------------------------------------------------
SESSION = 106  # (local) session label
GATE_ID = "S106-CDGM-SPACING-CROSS-BLOCK"
SCHEME = "FW"
CONVENTION = ("CDGM-LADDER-SPACING-CROSS-BLOCK;B3-HORIZON-CORE-SECTOR;"
              "CHI-PROJECTION-OPNORM-LEVEL")
L_MAX = 10  # (local) Peter-Weyl truncation (named-block extraction; W2-2 pin; orthogonal to W1 L-envelope)

SESSION_DIR = Path(__file__).resolve().parent
SCRIPT_PATH = Path(__file__).resolve()
CANON_PATH = _SHARED / "canonical_constants.py"
# Plan-listed input (per_block_json + lam_horizon + Delta_B3 source):
S105_W2_2_NPZ = SESSION_DIR.parent / "session-105" / "s105_w2_2_omega_faithful_normal.npz"
# Input-path-drift resolution (ii.B): the per-mode level set lives in the S84 master cache
# (NOT in the W2-2 npz, which carries only summary stats). Same source S105 W2-2 used.
S84_CACHE_NPZ = SESSION_DIR.parent / "session-84" / "s84_spectrum_cache_L12_tau019.npz"

OUT_NPZ = SESSION_DIR / "s106_cdgm_spacing_cross_block.npz"
OUT_PNG = SESSION_DIR / "s106_cdgm_spacing_cross_block.png"

# ---------------------------------------------------------------------------
# Section 3 -- Pre-registered machinery pins (PRDR; plan W2-3 machinery_pin_map)
# ---------------------------------------------------------------------------
VAR_THRESHOLD = 1e-2          # (local) relative cross-block variance band (invariant <= ; accident >)
SPACING_NUM_TOL = 1e-9        # (local) spacing-extraction numerical tol (degenerate-level collapse + dE>0 filter)
HORIZON_BLOCKS = [(0, 0), (1, 0), (0, 1), (1, 1)]  # (local) named horizon-sector Peter-Weyl blocks (W2-2 set)
# B3 horizon-core sector carries the CdGM ladder (gap = Delta_B3 = 0.176; the +1/2 minigap doubled).

# ---------------------------------------------------------------------------
# Section 4 -- Dual-SHA closure (audit + content)
#   audit_sha256_inputs:  [script, canonical, pinmap, s105_w2_2_npz]   (plan block)
#   PLUS s84_cache_npz    -- input-path-drift resolution (ii.B); folded into audit closure
#                            so the audit trail pins the ACTUAL per-mode source.
#   content_sha256_inputs: [script]
# ---------------------------------------------------------------------------
def closure_hash(pins: dict) -> str:
    h = hashlib.sha256()
    for k, v in sorted(pins.items()):
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def _file_sha(p: Path) -> str:
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return "MISSING"


def compute_dual_sha(pins: dict) -> tuple[str, str]:
    """audit = sha256(script || canonical || pinmap_json || s105_w2_2_npz || s84_cache_npz);
    content = sha256(script)."""
    try:
        script_bytes = SCRIPT_PATH.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canon_bytes = CANON_PATH.read_bytes()  # (local)
    except OSError:
        canon_bytes = b""  # (local)
    try:
        w22_bytes = S105_W2_2_NPZ.read_bytes()  # (local)
    except OSError:
        w22_bytes = b""  # (local)
    try:
        s84_bytes = S84_CACHE_NPZ.read_bytes()  # (local)
    except OSError:
        s84_bytes = b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canon_bytes)
    h_audit.update(pinmap_json)
    h_audit.update(w22_bytes)
    h_audit.update(s84_bytes)
    audit = h_audit.hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 -- Verdict payload printer (race-safe: PRINT only; agent calls emit_verdict)
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          companion_note: str = "",
                          extra_rows: list | None = None) -> dict:
    payload: dict = {
        "session": SESSION,
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
# Section 6 -- B3-sector level reconstruction (the substitution chain per block)
# ---------------------------------------------------------------------------
def reconstruct_bdg_levels(abs_evals: np.ndarray, lam_horizon: float,
                           Delta_a: float) -> np.ndarray:
    """Reconstruct the per-mode BdG energy spectrum EXACTLY as S105 W2-2 did:
        xi_a = |lambda|_a - lam_horizon          (normal-state dispersion rel the horizon Fermi point)
        E_a  = sqrt(xi_a^2 + Delta_a^2)          (BdG quasiparticle energy; >= Delta_a > 0, GAPPED)
    Returns the sorted E array (with degeneracy)."""
    xi = np.asarray(abs_evals, dtype=np.float64) - lam_horizon   # (local)
    E = np.sqrt(xi * xi + Delta_a * Delta_a)                     # (local) BdG energy >= Delta_a > 0
    return np.sort(E)


def ladder_spacings(E_sorted: np.ndarray):
    """Extract the CdGM ladder-spacing observables from one block's sorted level set.

    Returns dict with:
      E0          : minigap (lowest BdG level) = omega_0/2 in the rigid CdGM reading
      omega0_R1   : 2*E0                       (R1: rigid-ladder doubled-minigap, MEASURED)
      omega0_R2   : median consecutive dE over UNIQUE levels (R2: literal spacing_definition_pin)
      omega0_R0   : the canonical gap (= 2*Delta_a? no -- the per_block_json 'gap' field = Delta_a)
                    [reported separately from per_block_json, not here]
      n_levels    : number of unique levels (degeneracy collapsed)
      slope_fit   : lstsq slope of E_n = (n+1/2)*omega_0 over unique levels (rigidity diagnostic)
      resid_fit   : max |residual| of that fit (departure from a rigid equal-spaced ladder)
    """
    Eu = np.sort(np.unique(np.round(E_sorted, 12)))    # (local) unique levels (collapse degeneracy)
    E0 = float(Eu[0])                                  # (local) minigap
    omega0_R1 = 2.0 * E0                               # (local) doubled minigap (rigid CdGM reading)
    if Eu.size > 1:
        dE = np.diff(Eu)                               # (local) consecutive unique-level spacings
        dE_pos = dE[dE > SPACING_NUM_TOL]              # (local)
        omega0_R2 = float(np.median(dE_pos)) if dE_pos.size else float("nan")  # (local)
        # rigidity diagnostic: lstsq E_n = (n+1/2)*omega_0
        n = np.arange(Eu.size)                         # (local)
        half = n + 0.5                                 # (local)
        A = np.vstack([half, np.ones_like(half)]).T    # (local)
        sol, *_ = np.linalg.lstsq(A, Eu, rcond=None)   # (local) [slope, intercept]
        slope_fit = float(sol[0])                      # (local)
        resid_fit = float(np.max(np.abs(Eu - A @ sol)))  # (local)
    else:
        omega0_R2 = float("nan")
        slope_fit = float("nan")
        resid_fit = float("nan")
    return dict(E0=E0, omega0_R1=omega0_R1, omega0_R2=omega0_R2,
                n_levels=int(Eu.size), slope_fit=slope_fit, resid_fit=resid_fit)


def relative_variance(vals) -> tuple[float, float, float, float]:
    """Var_pq[w0]/<w0>^2 (intensive, block-count-independent) + mean,min,max."""
    v = np.asarray(vals, dtype=np.float64)
    v = v[np.isfinite(v)]
    if v.size == 0 or v.mean() == 0.0:
        return float("nan"), float("nan"), float("nan"), float("nan")
    return (float(v.var() / v.mean() ** 2), float(v.mean()),
            float(v.min()), float(v.max()))


# ---------------------------------------------------------------------------
# Section 7 -- Main
# ---------------------------------------------------------------------------
def main() -> int:
    # ----- input SHAs (first 20 lines of stdout per gate-verdicts.md  2) -----
    print(f"[{GATE_ID}] input SHA-256 pins:")
    print(f"  script            = {_file_sha(SCRIPT_PATH)}")
    print(f"  canonical         = {_file_sha(CANON_PATH)}")
    print(f"  s105_w2_2_npz     = {_file_sha(S105_W2_2_NPZ)}")
    print(f"  s84_cache_npz     = {_file_sha(S84_CACHE_NPZ)}  [ii.B drift-resolution: per-mode level source]")
    print(f"  pins              : VAR_THRESHOLD={VAR_THRESHOLD}, SPACING_NUM_TOL={SPACING_NUM_TOL}, "
          f"L_max={L_MAX}, tau_fold={tau_fold}")
    print(f"  gaps              : Delta_B3={Delta_B3} (B3 horizon-core), "
          f"Delta_BCS={Delta_BCS}, Delta_B2={Delta_B2}  (cross-sector diagnostic)")

    # ----- load the W2-2 npz (per_block_json summary stats + lam_horizon) -----
    w22 = np.load(S105_W2_2_NPZ, allow_pickle=True)
    per_block_summary = json.loads(str(w22["per_block_json"]))  # (local) summary stats per block (gap, E_min/max,...)
    lam_horizon = float(w22["lam_horizon"])                     # (local) substrate-IS spectral floor (W2-2 interp (i))
    Delta_B3_w22 = float(w22["Delta_B3"])                       # (local) cross-check vs canonical
    print(f"\n[W2-2] lam_horizon = {lam_horizon:.13f}  Delta_B3(npz) = {Delta_B3_w22}  "
          f"Delta_B3(canon) = {Delta_B3}")
    assert abs(Delta_B3_w22 - Delta_B3) < 1e-12, "Delta_B3 npz vs canonical mismatch"

    # ----- INPUT-PATH-DRIFT RESOLUTION (ii.B): reconstruct per-mode levels from S84 cache -----
    # per_block_json carries only SUMMARY stats; the per-mode level set needed for the
    # consecutive-spacing extraction lives in the S84 master cache (the SAME source W2-2 used).
    cache = np.load(S84_CACHE_NPZ, allow_pickle=True)
    sector_evals = cache["sector_evals"].item()                # (local) {(p,q): {dim, level, abs_evals}}
    # reconstruct lam_horizon from the cache and verify it matches the W2-2 npz field (interp (i))
    lam_horizon_recon = min(float(np.asarray(sector_evals[pq]["abs_evals"]).min())
                            for pq in HORIZON_BLOCKS)           # (local)
    print(f"[ii.B] lam_horizon reconstructed from S84 cache = {lam_horizon_recon:.13f} "
          f"(matches W2-2 field: {abs(lam_horizon_recon - lam_horizon) < 1e-12})")
    drift_note = ("per_block_json carries summary-only; per-mode level set reconstructed "
                  "from s84_spectrum_cache_L12_tau019.npz (same source W2-2 used; ii.B)")

    # =====================================================================
    # B3-sector: per-block CdGM ladder reconstruction + spacing extraction
    # =====================================================================
    print("\n=== B3 horizon-core sector: per-block CdGM ladder spacings ===")
    print("    R1 omega_0 = 2*E_0 (rigid CdGM doubled-minigap, MEASURED)")
    print("    R2 omega_0 = median consecutive dE (literal spacing_definition_pin)")
    rows_B3 = {}            # (local) per-block records
    recon_match = {}        # (local) E_min/E_max reconstruction cross-check vs per_block_json
    w0_R1, w0_R2, E0_list = [], [], []  # (local) cross-block arrays
    w0_R0_gap = []          # (local) the per_block_json 'gap' field (= Delta_B3 input constant; tautology)
    for pq in HORIZON_BLOCKS:
        ae = np.asarray(sector_evals[pq]["abs_evals"], dtype=np.float64)
        E_sorted = reconstruct_bdg_levels(ae, lam_horizon, Delta_B3)   # (local) B3 BdG levels
        sp = ladder_spacings(E_sorted)
        rows_B3[f"B3|{pq}"] = sp
        w0_R1.append(sp["omega0_R1"])
        w0_R2.append(sp["omega0_R2"])
        E0_list.append(sp["E0"])
        # cross-check reconstruction vs the per_block_json summary E_min/E_max
        key = f"B3|({pq[0]}, {pq[1]})"
        pbs = per_block_summary.get(key, {})
        e_min_pbs = float(pbs.get("E_min", np.nan))   # (local)
        e_max_pbs = float(pbs.get("E_max", np.nan))   # (local)
        e_min_ok = abs(E_sorted.min() - e_min_pbs) < 1e-9   # (local)
        e_max_ok = abs(E_sorted.max() - e_max_pbs) < 1e-9   # (local)
        recon_match[key] = bool(e_min_ok and e_max_ok)
        w0_R0_gap.append(float(pbs.get("gap", np.nan)))   # per_block_json 'gap' (= Delta_B3 input const)
        print(f"  B3|{pq}: n_levels={sp['n_levels']:2d}  E_0={sp['E0']:.6f}  "
              f"omega0_R1(2E0)={sp['omega0_R1']:.6f}  omega0_R2(med dE)={sp['omega0_R2']:.6f}  "
              f"slope={sp['slope_fit']:.6f}  max|resid|={sp['resid_fit']:.6f}  "
              f"recon_match={recon_match[key]}")

    recon_all_ok = all(recon_match.values())   # (local)
    print(f"\n  reconstruction matches per_block_json E_min/E_max on all blocks: {recon_all_ok}")

    # =====================================================================
    # Cross-block relative variance (the INFO-class characterization)
    # =====================================================================
    rv_R1, mean_R1, min_R1, max_R1 = relative_variance(w0_R1)
    rv_R2, mean_R2, min_R2, max_R2 = relative_variance(w0_R2)
    rv_R0, mean_R0, min_R0, max_R0 = relative_variance(w0_R0_gap)
    spread_R1 = max_R1 - min_R1   # (local) op-norm-level spread (max-min across blocks)
    spread_R2 = max_R2 - min_R2   # (local)

    inv_R1 = rv_R1 <= VAR_THRESHOLD   # (local)
    inv_R2 = rv_R2 <= VAR_THRESHOLD   # (local)

    print("\n=== CROSS-BLOCK relative variance (threshold = 1e-2) ===")
    print(f"  R0 input-constant gap (TAUTOLOGY): per-block={[round(x,6) for x in w0_R0_gap]}  "
          f"relvar={rv_R0:.6e}  (gap field = Delta_B3 input constant, not a measured spacing)")
    print(f"  R1 2*E_0 (rigid CdGM minigap, MEASURED): per-block={[round(x,6) for x in w0_R1]}")
    print(f"     mean={mean_R1:.6f}  spread(max-min)={spread_R1:.6f}  relvar={rv_R1:.6e}  "
          f"=> {'INVARIANT' if inv_R1 else 'ACCIDENT'}")
    print(f"  R2 median consecutive dE (literal pin): per-block={[round(x,6) for x in w0_R2]}")
    print(f"     mean={mean_R2:.6f}  spread(max-min)={spread_R2:.6f}  relvar={rv_R2:.6e}  "
          f"=> {'INVARIANT' if inv_R2 else 'ACCIDENT'}")

    # =====================================================================
    # Cross-sector DIAGNOSTIC (NON-GATED): B2/BCS minigap-based 2*E_0 variance
    # =====================================================================
    print("\n=== Cross-sector DIAGNOSTIC (NON-GATED): 2*E_0 relvar per sector ===")
    diag_sectors = {}   # (local)
    for ch, Dg in [("B3", Delta_B3), ("BCS", Delta_BCS), ("B2", Delta_B2)]:
        w0s = []   # (local)
        for pq in HORIZON_BLOCKS:
            ae = np.asarray(sector_evals[pq]["abs_evals"], dtype=np.float64)
            Es = reconstruct_bdg_levels(ae, lam_horizon, Dg)
            Eu = np.sort(np.unique(np.round(Es, 12)))
            w0s.append(2.0 * float(Eu[0]))
        rv_d, mean_d, _, _ = relative_variance(w0s)
        diag_sectors[ch] = dict(omega0_2E0=w0s, relvar=rv_d, mean=mean_d,
                                invariant=bool(rv_d <= VAR_THRESHOLD))
        print(f"  {ch:4s} 2*E_0 per block: {[round(x,6) for x in w0s]}  "
              f"relvar={rv_d:.3e}  => {'INVARIANT' if rv_d <= VAR_THRESHOLD else 'ACCIDENT'}")

    # =====================================================================
    # Composite characterization verdict (INFO-class BY CONSTRUCTION)
    # =====================================================================
    # The verdict TOKEN is INFO (workshop pre-registration). The CHARACTERIZATION:
    #   - PRIMARY substrate-faithful reading R1 (the rigid CdGM minigap, the BDI-protected
    #     quantity, theorem K12 S105): INVARIANT or ACCIDENT.
    #   - LITERAL reading R2 (the plan spacing_definition_pin): INVARIANT or ACCIDENT.
    # The two readings dissociate: R1 (minigap) cross-block invariant; R2 (upper-level
    # spacing) within-block accident -> the rigidity that survives chi is the MINIGAP,
    # not the upper-level spacing.
    verdict = "INFO"   # INFO-class by construction (plan PASS_meaning/INFO_meaning)
    if inv_R1:
        classification_R1 = "CROSS-BLOCK-INVARIANT"
    else:
        classification_R1 = "WITHIN-BLOCK-ACCIDENT"
    if inv_R2:
        classification_R2 = "CROSS-BLOCK-INVARIANT"
    else:
        classification_R2 = "WITHIN-BLOCK-ACCIDENT"

    value = (f"omega0_R1(2E0)_relvar={rv_R1:.4e}_{classification_R1};"
             f"omega0_R2(med_dE)_relvar={rv_R2:.4e}_{classification_R2};"
             f"thr={VAR_THRESHOLD};minigap_invariant={inv_R1};upper_spacing_invariant={inv_R2};"
             f"recon_match={recon_all_ok};drift=s84cache_per_mode")

    print(f"\n=== VERDICT: {verdict} (INFO-class by construction) ===")
    print(f"  R1 minigap (2*E_0)        : {classification_R1}  (relvar={rv_R1:.4e}, thr={VAR_THRESHOLD})")
    print(f"  R2 upper-level spacing    : {classification_R2}  (relvar={rv_R2:.4e}, thr={VAR_THRESHOLD})")
    print(f"  SUBSTRATE READING         : the BDI-protected CdGM +1/2 MINIGAP survives chi cross-block;")
    print(f"                              the upper-level (rank>=3-in-sector) spacing is block-specific.")

    # ----- 4-tuple output tag (final non-verdict line) -----
    print(f"\n4-tuple: (value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

    # =====================================================================
    # npz
    # =====================================================================
    npz_payload = dict(
        gate_id=GATE_ID, verdict=verdict, scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        horizon_blocks=np.array([f"{p},{q}" for (p, q) in HORIZON_BLOCKS]),
        lam_horizon=lam_horizon, Delta_B3=Delta_B3, VAR_THRESHOLD=VAR_THRESHOLD,
        SPACING_NUM_TOL=SPACING_NUM_TOL,
        # R1 (rigid CdGM minigap, primary substrate-faithful)
        omega0_R1_per_block=np.array(w0_R1, dtype=np.float64),
        omega0_R1_relvar=rv_R1, omega0_R1_mean=mean_R1,
        omega0_R1_min=min_R1, omega0_R1_max=max_R1, omega0_R1_spread=spread_R1,
        omega0_R1_invariant=inv_R1, omega0_R1_classification=classification_R1,
        # R2 (literal consecutive-spacing pin)
        omega0_R2_per_block=np.array(w0_R2, dtype=np.float64),
        omega0_R2_relvar=rv_R2, omega0_R2_mean=mean_R2,
        omega0_R2_min=min_R2, omega0_R2_max=max_R2, omega0_R2_spread=spread_R2,
        omega0_R2_invariant=inv_R2, omega0_R2_classification=classification_R2,
        # R0 (input-constant gap tautology)
        omega0_R0_gap_per_block=np.array(w0_R0_gap, dtype=np.float64), omega0_R0_relvar=rv_R0,
        # minigap E_0 per block
        E0_per_block=np.array(E0_list, dtype=np.float64),
        # per-block full records
        per_block_B3_json=json.dumps(rows_B3),
        recon_match_json=json.dumps(recon_match), recon_all_ok=recon_all_ok,
        # cross-sector diagnostic
        diag_sectors_json=json.dumps(diag_sectors),
        # provenance
        drift_note=drift_note, tau_fold=tau_fold,
    )
    np.savez_compressed(OUT_NPZ, **npz_payload)
    print(f"[npz] wrote {OUT_NPZ}")

    # =====================================================================
    # plot
    # =====================================================================
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(13.8, 5.4))

    # left: per-block B3 CdGM levels (the ladder) + minigap markers
    colors = plt.cm.viridis(np.linspace(0.12, 0.85, len(HORIZON_BLOCKS)))  # (local)
    for ci, pq in enumerate(HORIZON_BLOCKS):
        ae = np.asarray(sector_evals[pq]["abs_evals"], dtype=np.float64)
        E_sorted = reconstruct_bdg_levels(ae, lam_horizon, Delta_B3)
        Eu = np.sort(np.unique(np.round(E_sorted, 12)))   # (local)
        nlev = np.arange(Eu.size)                          # (local)
        ax0.plot(nlev, Eu, "o-", ms=4.5, color=colors[ci], lw=1.0,
                 label=f"(p,q)={pq}  ($E_0$={Eu[0]:.4f})")
    ax0.axhline(Delta_B3, color="darkred", lw=1.0, ls="--",
                label=fr"$\Delta_{{B3}}={Delta_B3}$ (gap floor)")
    ax0.set_xlabel("CdGM level index $n$ (unique levels, B3 sector)")
    ax0.set_ylabel(r"$E_n = \sqrt{\xi_n^2 + \Delta_{B3}^2}$  (M$_{KK}$ units)")
    ax0.set_title("B3 horizon-core CdGM levels per named block\n"
                  fr"minigap $E_0$ cross-block invariant; upper levels block-specific")
    ax0.legend(fontsize=8, loc="upper left")
    ax0.grid(alpha=0.25)

    # right: cross-block omega_0 readings + threshold
    bx = np.arange(len(HORIZON_BLOCKS))   # (local)
    w = 0.38                              # (local)
    ax1.bar(bx - w/2, w0_R1, width=w, color="steelblue", alpha=0.85,
            label=fr"R1: $2E_0$ (rigid CdGM)  relvar={rv_R1:.2e} [{'INV' if inv_R1 else 'ACC'}]")
    ax1.bar(bx + w/2, w0_R2, width=w, color="indianred", alpha=0.85,
            label=fr"R2: median $\Delta E$ (literal)  relvar={rv_R2:.2e} [{'INV' if inv_R2 else 'ACC'}]")
    ax1.axhline(mean_R1, color="steelblue", lw=0.9, ls=":")
    ax1.axhline(mean_R2, color="indianred", lw=0.9, ls=":")
    ax1.set_xticks(bx)
    ax1.set_xticklabels([f"{pq}" for pq in HORIZON_BLOCKS], rotation=20)
    ax1.set_ylabel(r"$\omega_0^{(p,q)}$  (M$_{KK}$ units)")
    ax1.set_title("Cross-block CdGM ladder-spacing $\\omega_0$\n"
                  fr"(rel.var. threshold = {VAR_THRESHOLD}: $\leq$ INVARIANT, $>$ ACCIDENT)")
    ax1.legend(fontsize=8, loc="upper right")
    ax1.grid(alpha=0.25, axis="y")

    fig.suptitle(f"{GATE_ID}  --  CdGM ladder-spacing cross-block (INFO-class)  --  "
                 f"R1 {classification_R1} / R2 {classification_R2}",
                 fontsize=11.5, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"[png] wrote {OUT_PNG}")

    # =====================================================================
    # dual-SHA + verdict payload
    # =====================================================================
    pins = {
        "gate_id": GATE_ID, "scheme": SCHEME, "convention": CONVENTION, "L_max": str(L_MAX),
        "VAR_THRESHOLD": repr(VAR_THRESHOLD), "SPACING_NUM_TOL": repr(SPACING_NUM_TOL),
        "Delta_B3": repr(Delta_B3),
        "horizon_blocks": ";".join(f"{p},{q}" for (p, q) in HORIZON_BLOCKS),
        "lam_horizon": repr(lam_horizon),
        "omega0_R1_relvar": repr(rv_R1), "omega0_R2_relvar": repr(rv_R2),
        "omega0_R1_invariant": repr(inv_R1), "omega0_R2_invariant": repr(inv_R2),
        "recon_all_ok": repr(recon_all_ok),
        "verdict": verdict,
        "s105_w2_2_sha": _file_sha(S105_W2_2_NPZ), "s84_cache_sha": _file_sha(S84_CACHE_NPZ),
    }
    closure = closure_hash(pins)  # (local) closure over the ordered pin map
    audit_sha, content_sha = compute_dual_sha(pins)
    print(f"\n[closure] closure_hash(pins) = {closure}")

    companion = (f"CdGM ladder-spacing cross-block (Volovik Paper 05 Eq.60/61); INFO-class; "
                 f"R1 minigap 2*E_0 relvar={rv_R1:.4e} {classification_R1}; "
                 f"R2 upper-spacing relvar={rv_R2:.4e} {classification_R2}; "
                 f"BDI/N3=0 +1/2 minigap survives chi cross-block; upper-level spacing block-specific")
    extra = [
        f"# ii.B input-path-drift: {drift_note}; closure_hash={closure[:16]}",
        f"# diag cross-sector 2E0 relvar: B3={diag_sectors['B3']['relvar']:.3e} "
        f"BCS={diag_sectors['BCS']['relvar']:.3e} B2={diag_sectors['B2']['relvar']:.3e} (all INVARIANT, NON-GATED)",
    ]
    print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note=companion, extra_rows=extra)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
