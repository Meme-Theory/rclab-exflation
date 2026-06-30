#!/usr/bin/env python
"""
CF-S117-BRANCH-IV-L16 — branch-(iv) w_0 DR3-class L_max diagnostic ONE TRUNCATION DEEPER (p+q=16).

Gate: CF-S117-BRANCH-IV-L16  ([SIGN] — directional sub-claim: the per-shell decrement DECELERATES
      |d(15->16)| < |d(14->15)|=0.018456 AND the sliding-window spread NARROWS
      spread_CAC{14,15,16} < spread_CAC{13,14,15}=0.0392902; the COMPOSITE is INFO-BY-CONSTRUCTION
      per the W-5 R3-FINAL closure — the branch-iv corridor is CLOSED-WITH-RESULT and is NOT
      reopenable by an L_max diagnostic, see the `# composite-precedence:` companion row).
Classification: GEOMETRIC (a spectral-functional property of the D_K spectrum at the fixed
                tau_fold=0.190 slice; Level-1 single-tau-slice substrate-IS; NOT a phononic excitation).
Owner: baptista-spacetime-analyst.

WHAT THIS GATE DOES (and how it DIFFERS from the investigation-track INV13-W1-3)
--------------------------------------------------------------------------------
The branch-(iv) w_0_FW DR3-class L_max-stability lineage (S102 -> S103 -> S104 PRE-REG-INC ->
S105 INFO -> S116-W9 INFO at p+q=15) is extended ONE truncation deeper to p+q=16. The S106 cache
(s106_w1_highl_cache_l1416.npz) holds the COMPLETE p+q<=15 triangle (sector_evals_L16, 136 sectors)
but the 17 level-16 sectors are ABSENT — they are FB-bounded placeholders only (fb_bounded_sectors:
lambda_lower_bound = eta_FB_lower*sqrt(C_2+1), the S106 two-tier Friedrich-Bar fallback "bound on
time" for the level-16 mixed construction). The investigation-track INV13-W1-3-BRANCH-IV-W0-L1516-DR3
SET rho_B(16) == rho_B(15) EXACTLY (rho16_eq_15=0.0) by the bottom-K Friedrich-Bar saturation
argument — VALID for the bottom-K observable (the p+q=16 |lambda|_min ~ 4.5 is far above the
bottom-20 ceiling 0.845) but STRUCTURALLY WRONG for the branch-(iv) Zubarev moment, which is
LAMBDA_MAX-DRIVEN:
    rho_B(L) = mean_Z(L)/lambda_max(L) - 1.
The p+q=16 shell RAISES lambda_max (the denominator) even though its Zubarev-suppressed modes
(w_Z=exp(-|lambda|^2), |lambda|>=4.5 -> w_Z<=2e-9) barely touch mean_Z. So rho_B(16) != rho_B(15):
this is exactly the S116-W9 stated orthogonality ("bottom-K Friedrich-Bar-saturated ... ORTHOGONAL
to lambda_max-driven w0 moment shift"). THIS GATE BUILDS THE SHELL to get the genuine rho_B(16).

  (A) BUILD the p+q=16 FB-bounded shell (17 sectors), exploiting conjugate-|lambda| symmetry
      (CPT: |lambda(p,q)| == |lambda(q,p)| EXACT; S106 conj_pair_max=1.26e-13). Only the 9
      upper-triangle (p>=q) sectors are constructed; the 8 lower-triangle conjugates inherit the
      spectrum (a LIVE conjugate sentinel re-builds (0,16) and checks it matches the mirror of
      (16,0) to < 1e-10). This halves the S106 full-triangle cost.
        - GT-pure (16,0)/(0,16): irrep_symmetric_power_gt (bosonic-ladder, NEVER forms 3^16),
          dim_sym=(16+1)(16+2)/2=153, D=2448. These carry the SHELL lambda_max (largest C_2=304/3).
        - 7 mixed pairs (15,1)..(9,7) + the self-conjugate (8,8): get_irrep Casimir-projection with
          the GT builder monkeypatched for the Sym^p parents (the s105/s116-W9 validated route).
          Largest block (8,8): dim=729, D=11664, dense complex128=2.18 GB << 17.1 GB VRAM.
        - GATING sentinel: GT-pure (16,0)/(0,16) vs the cheap analytic conjugate-symmetry; the
          rho_B(13,14,15) re-derivation reproduces the S116-W9 lineage bit-exact.

  (B) rho_B(16) = mean_Z(16)/lambda_max(16) - 1 (S85 W0-7 Zubarev evaluator, imported VERBATIM from
      s105_branch_iv_direct_l1314.py), on the COMPLETE (4,4)-filled lineage merged with the new
      level-16 shell. CAC-anchored: w0^CAC(L) = rho_B(L) + offset_B, offset_B := w0_FW - rho_B(10)
      [DERIVED at runtime; CAC MANDATORY per regulator-convention-lockdown.md; the offset cancels
      EXACTLY in any spread; w0^CAC(10)=w0_FW by construction].

  (C) DIAGNOSTICS (the [SIGN] directional sub-claims, INFO-by-construction composite):
        - decrement-deceleration: |d(15->16)| < |d(14->15)|=0.018456 (the 1/lambda_max^2 law:
          |d| = mu*b/lambda_max^2, mu=mean_Z frozen ~1.9879, b=d lambda_max/dL ~0.3747).
        - sliding-window spread narrowing: spread_CAC{14,15,16} < spread_CAC{13,14,15}=0.0392902.
      VALUE-NEUTRAL (the spread is offset-INVARIANT: spread_CAC = rho_a - rho_b, bit-identical for
      any offset target), so it certifies ONLY that rho_B -> -1 smoothly (the bare-moment limit);
      it is NOT support for -0.918 (which lives entirely in the CAC offset / the q-field partition's
      effacement). The corridor disposition (CLOSED-WITH-RESULT, W-5) is UNCHANGED.

Verdict (composite forced INFO by the `# composite-precedence:` row; corridor CLOSED-WITH-RESULT):
  INFO  = the value-neutral L_max diagnostic delivered (rho_B(16), spread_CAC{14,15,16}, decrement
          sign). The [SIGN] 3-tuple carries the decrement-deceleration + spread-narrowing direction.
  FAIL  = SCRIPT BREAKAGE ONLY (shell build does not converge / Casimir-projection fails / GT
          sentinel fails / cache integrity fails) -> honest mechanical closure PRE-REG-INC.
  PASS  = N/A — this gate CANNOT PASS-reopen the corridor (CLOSED-WITH-RESULT per W-5).

Output 4-tuple:
  (value=<computed>, scheme=zeta, convention=CAC-branch-iv-anchored-L10-DERIVED-OFFSET, L_max=16)

regulator_pin: a_2^{Mellin}  (branch-(iv) w_0 channel = substrate-distance Mellin-zeta moment; zeta
  scheme; poleconv-A-double (pole_in_s=3, curvature_grade_n=2) per regulator-pin-discipline.md
  §"Mellin Pole-Set Labeling"). cutoff_axis=spectral (Zubarev kernel Lambda_Z on the D_K spectrum).

Substrate-first arrow (GEOMETRIC, Level-1 single-tau-slice substrate-IS at tau_fold): D_K eigenvalues
at tau_fold (the NEW p+q=16 shell) -> branch-(iv) Zubarev Mellin-zeta spectral moment rho_B(16) ->
CAC-anchored late-time w_0 -> DESI DR3 w0-wa measurement. lambda_max(L) is the RUNNING truncation
EDGE (sup-norm of the retained spectrum), a non-substrate quantity with no continuum limit; the
moment's smooth convergence to -1 is the substrate telling us w_0 does NOT live in the eigenvalue
spread (the W-5 categorical wall (ii)). This gate does NOT search for a hidden spectral derivation of
-0.918 — it certifies the moment converges smoothly to its OWN limit (-1), a value-neutral
presentation-hygiene fact. GR's dark energy is the consequence, not the premise.
"""
from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 1 — Identity + paths
# ---------------------------------------------------------------------------
SESSION = "S117"
GATE_ID = "CF-S117-BRANCH-IV-L16"
SCHEME = "zeta"
CONVENTION = "CAC-branch-iv-anchored-L10-DERIVED-OFFSET"
L_MAX = "16"

THIS_FILE = Path(__file__).resolve()
PROJECT_ROOT = THIS_FILE.parents[2]                  # .../computations/session-117/<this> -> root
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
SESSION_DIR = PROJECT_ROOT / "computations" / "session-117"
S105_DIR = PROJECT_ROOT / "computations" / "session-105"
S106_DIR = PROJECT_ROOT / "computations" / "session-106"
S116_DIR = PROJECT_ROOT / "computations" / "session-116"

sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(S105_DIR))

from canonical_constants import (  # noqa: E402
    w0_FW,
    Gamma_effacement,
    N_cells,
    tau_fold,
)

# VERBATIM reuse of the S105 GT bosonic-ladder builder + S85 W0-7 Zubarev evaluator + pipeline.
# (NOT re-derived; the same validated constructions that landed S105 INFO and S116-W9 INFO.)
from s105_branch_iv_direct_l1314 import (  # noqa: E402
    irrep_symmetric_power_gt,
    rho_zubarev_from_sectors,
    build_dirac_pipeline,
)

# ---------------------------------------------------------------------------
# Section 2 — Pre-registered constants (plan §W7-3 machinery_pin_map; PRDR dry-run)
# ---------------------------------------------------------------------------
LAMBDA_Z = 1.0                           # (local) Zubarev kernel width (S85 W0-7 PRDR pin), M_KK units; UNCHANGED
L_ANCHOR = 10                            # (local) CAC offset anchor truncation (rho_B(L=10) -> w0_FW)
L_SHELL = 16                             # (local) the new shell level
L_SCAN_primary = (14, 15, 16)            # (local) sliding-window VERDICT object (spread + decrement)
SPREAD_PASS_BAND = 0.025                 # (local) W9 PASS band (trajectory CONTEXT only; NOT a corridor gate here)
SPREAD_INFO_BAND = 0.050                 # (local) W9 INFO band (context only)
SENTINEL_TOL = 1e-10                     # (local) GT-pure (16,0)/(0,16) conjugate-symmetry sentinel floor
REPRO_TOL = 1e-12                        # (local) rho_B(13/14/15) W9-lineage reproduction floor

# S116-W9-GTBUILDER-L15 trajectory anchors (the {13,14,15} baseline this gate extends; plan §W7-3):
RHO_B_13_W9 = -0.656884151842210         # (local) W9 lineage rho_B(13) (SE16, complete (4,4)-filled)
RHO_B_14_W9 = -0.677718044737923         # (local) W9 lineage rho_B(14)
RHO_B_15_W9 = -0.696174388058208         # (local) W9 lineage rho_B(15)
RHO_B_10_W9 = -0.575206615134972         # (local) W9 lineage rho_B(10) (the CAC anchor)
LAM_MAX_15_W9 = 6.542827                 # (local) W9 lambda_max(15) from (0,15)/(15,0)
D_13_14_W9 = -0.020833892895713          # (local) W9 d(13->14) = rho_B(14)-rho_B(13)
D_14_15_W9 = -0.018456343220285          # (local) W9 d(14->15) = rho_B(15)-rho_B(14) (the decel sentinel)
SPREAD_CAC_W9_131415 = 0.039290236215998 # (local) W9 spread_CAC{13,14,15} = rho_B(13)-rho_B(15)
OFFSET_B_W9 = -0.342793384865028         # (local) W9 offset_B = w0_FW - rho_B(10)

# S106 cache npz-internal audit_sha256 field (runtime integrity check pin; plan §W7-3 input ledger):
CACHE_INTERNAL_AUDIT_SHA256 = "5af2b7cd09d863491cd30872384f9bc9adc7b0a580c2b7089f28ce9bfda3fcbb"

# Runtime canonical-value assertions (PLAN-TEXT-DRIFT note; substrate-first-canonical-sourcing.md §(ii.B)):
W0_FW_EXPECT = -0.918                     # (local) canonical w0_FW (S58 Volovik partition+effacement)
TAU_FOLD_EXPECT = 0.190                   # (local) canonical tau_fold (S12/S42)

# Hermiticity floor (boson (p,0) i*D is EXACTLY Hermitian; dimension-scaled guard for the mixed blocks):
ID_HERM_ERR_TOL_IDEAL = 1.0e-15          # (local)
EPS_F64 = float(np.finfo(np.float64).eps)  # (local) ~2.22e-16

# Investigation-track contrast anchor (INV13 SET rho_B(16)==rho_B(15) by bottom-K FB saturation;
# WRONG for the lambda_max-driven branch-iv moment — this gate computes the GENUINE shift):
INV13_RHO_B_16 = -0.696174388058208      # (local) INV13 rho_B(16) == rho_B(15) (bottom-K-saturation artifact)

JENSEN_S = float(tau_fold)               # (local) Jensen deformation s = tau_fold = 0.190 (cache is tau019)

# Upper-triangle p+q=16 sectors to BUILD (p>=q); conjugates (q,p) inherit |lambda| by CPT symmetry:
UPPER_TRIANGLE_16 = [(16, 0), (15, 1), (14, 2), (13, 3), (12, 4), (11, 5), (10, 6), (9, 7), (8, 8)]  # (local)

# ---------------------------------------------------------------------------
# Section 3 — Input files (resolved on disk; plan §W7-3 input-SHA ledger)
# ---------------------------------------------------------------------------
P_CANONICAL = SHARED_DIR / "canonical_constants.py"
P_CACHE_S106 = S106_DIR / "s106_w1_highl_cache_l1416.npz"
P_S105_PY = S105_DIR / "s105_branch_iv_direct_l1314.py"
P_S84 = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
P_DIRAC = SHARED_DIR / "dirac_spectrum.py"

INPUT_FILES = [P_CANONICAL, P_CACHE_S106, P_S105_PY, P_S84, P_DIRAC]

P_RESUME = SESSION_DIR / "s117_branch_iv_l16_shell_resume.npz"   # deterministic shell-spectra resume cache

# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                   # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}                              # (local)
    for p in inputs:
        sha = sha256_of(p)                                 # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p).replace("\\", "/")                # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())                           # (local)
    h = hashlib.sha256()                                   # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict[str, str]) -> tuple[str, str]:
    try:
        script_bytes = script_path.read_bytes()            # (local)
    except OSError:
        script_bytes = b""                                 # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()      # (local)
    except OSError:
        canonical_bytes = b""                              # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")                                      # (local)
    h_audit = hashlib.sha256()                             # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()                           # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — print_verdict_payload (agent calls emit_verdict with this)
# ---------------------------------------------------------------------------

def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_v="", magnitude_v="", regime_v="", extra_rows=None):
    payload = {
        "session": 117,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": L_MAX,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if sign_v:
        payload["sign_verdict"] = sign_v
        payload["magnitude_verdict"] = magnitude_v
        payload["regime_verdict"] = regime_v
    if extra_rows:
        payload["extra_rows"] = extra_rows
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")


# ---------------------------------------------------------------------------
# Section 6 — p+q=16 shell builder (upper triangle; conjugates inherit |lambda| by CPT)
# ---------------------------------------------------------------------------

def build_shell_16(gens, conj_gens, f_abc, dirac_abs_and_herr):
    """Build the 9 upper-triangle (p>=q) p+q=16 sectors; mirror the 8 conjugates by CPT |lambda|
    symmetry. GT-pure (16,0)/(0,16) via the bosonic-ladder builder; mixed via get_irrep
    Casimir-projection (GT builder monkeypatched into the Sym^p parents). Returns
    (shell_dict {(p,q):{dim,level,abs_evals}} for ALL 17 sectors, conj_sentinel_max, herr_max,
     build_times, lvl16_lam_max, lvl16_lam_max_sector)."""
    from dirac_spectrum import get_irrep, _irrep_cache

    shell = {}                                             # (local)
    build_times = {}                                       # (local)
    herr_max = 0.0                                         # (local)

    # --- GT-pure (16,0) AND (0,16): both cheap; (0,16) is the LIVE conjugate-symmetry sentinel ---
    t0 = time.time()                                       # (local)
    rho_160 = irrep_symmetric_power_gt(gens, 16)
    ab_160, herr_160 = dirac_abs_and_herr(rho_160)
    build_times["16,0"] = time.time() - t0
    herr_max = max(herr_max, herr_160)
    t0 = time.time()                                       # (local)
    rho_016 = irrep_symmetric_power_gt(conj_gens, 16)
    ab_016, herr_016 = dirac_abs_and_herr(rho_016)
    build_times["0,16"] = time.time() - t0
    herr_max = max(herr_max, herr_016)
    dim_gt = (16 + 1) * (16 + 2) // 2                      # (local) = 153
    conj_sentinel_max = float(np.max(np.abs(np.sort(ab_160) - np.sort(ab_016))))  # (local)
    shell[(16, 0)] = {"dim": dim_gt, "level": 16, "abs_evals": ab_160}
    shell[(0, 16)] = {"dim": dim_gt, "level": 16, "abs_evals": ab_016}
    print(f"    (16,0)/(0,16) GT-pure: dim={dim_gt} D={ab_160.size} "
          f"|lam|=[{ab_160.min():.6f},{ab_160.max():.6f}] herr=[{herr_160:.1e},{herr_016:.1e}] "
          f"conj_sentinel={conj_sentinel_max:.2e} ({build_times['16,0']:.1f}+{build_times['0,16']:.1f}s)")

    # --- 7 mixed pairs (15,1)..(9,7) + self-conjugate (8,8) via Casimir-projection ---
    for (p, q) in UPPER_TRIANGLE_16:
        if (p, q) == (16, 0):
            continue                                       # GT-pure already built above
        _irrep_cache.clear()                               # bound memory + avoid cross-sector contamination
        dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2      # (local)
        t0 = time.time()                                   # (local)
        rho, dim_check = get_irrep(p, q, gens, f_abc)
        assert dim_check == dim_pq, f"({p},{q}) dim {dim_check} != {dim_pq}"
        ab, herr = dirac_abs_and_herr(rho)
        dt = time.time() - t0                              # (local)
        build_times[f"{p},{q}"] = dt
        herr_max = max(herr_max, herr)
        shell[(p, q)] = {"dim": dim_pq, "level": 16, "abs_evals": ab}
        if p != q:
            # conjugate (q,p) inherits the |lambda| spectrum by CPT (|lambda(p,q)| == |lambda(q,p)|)
            shell[(q, p)] = {"dim": dim_pq, "level": 16, "abs_evals": ab.copy()}
        print(f"    ({p},{q})"
              f"{'' if p == q else f'+conj({q},{p})'}: dim={dim_pq} D={ab.size} "
              f"|lam|=[{ab.min():.6f},{ab.max():.6f}] herr={herr:.1e} ({dt:.1f}s)")

    lvl16_max = -1.0                                       # (local)
    lvl16_max_sector = None                                # (local)
    for k, d in shell.items():
        m = float(np.max(d["abs_evals"]))                  # (local)
        if m > lvl16_max:
            lvl16_max = m
            lvl16_max_sector = k
    return shell, conj_sentinel_max, herr_max, build_times, lvl16_max, lvl16_max_sector


# ---------------------------------------------------------------------------
# Section 7 — main
# ---------------------------------------------------------------------------

def main():
    print(f"=== {GATE_ID} :: branch-(iv) w_0 DR3 L_max diagnostic one truncation deeper (p+q=16) ===")
    print(f"[const] w0_FW={w0_FW}  tau_fold={tau_fold}  Lambda_Z={LAMBDA_Z}  "
          f"Gamma_effacement={Gamma_effacement}  N_cells={N_cells}")

    # --- runtime canonical-value verification (PLAN-TEXT-DRIFT; substrate-first §(ii.B)) ---
    assert abs(float(w0_FW) - W0_FW_EXPECT) < 1e-12, f"w0_FW drift: {w0_FW} != {W0_FW_EXPECT}"
    assert abs(float(tau_fold) - TAU_FOLD_EXPECT) < 1e-12, f"tau_fold drift: {tau_fold} != {TAU_FOLD_EXPECT}"
    print(f"[canon] runtime-verified: w0_FW={w0_FW} (==-0.918), tau_fold={tau_fold} (==0.190)")

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    audit_sha, content_sha = compute_dual_sha(THIS_FILE, P_CANONICAL, pins)
    canonical_sha_live = pins.get("computations/_shared/canonical_constants.py", "")  # (local)
    print(f"  closure_hash:   {closure[:16]}...")
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    # --- Load the S106 cache + RUNTIME INTEGRITY CHECK (npz-internal audit_sha256) ---
    z = np.load(P_CACHE_S106, allow_pickle=True)
    cache_internal_sha = str(np.asarray(z["audit_sha256"]).item())  # (local)
    cache_integrity_ok = (cache_internal_sha == CACHE_INTERNAL_AUDIT_SHA256)  # (local)
    print(f"[cache] npz-internal audit_sha256={cache_internal_sha[:16]}...  "
          f"integrity_ok(== 5af2b7cd...)={cache_integrity_ok}")
    if not cache_integrity_ok:
        z.close()
        value = (f"PRE-REG-INC_cache_integrity_FAIL_got_{cache_internal_sha[:16]}_"
                 f"expect_5af2b7cd; S106_cache_audit_sha256_mismatch")
        np.savez_compressed(
            SESSION_DIR / "s117_branch_iv_l16.npz",
            verdict="PRE-REG-INC", phase="CACHE_INTEGRITY_FAIL",
            cache_internal_sha=cache_internal_sha, cache_integrity_ok=cache_integrity_ok,
            audit_sha256=audit_sha, content_sha256=content_sha, closure_hash=closure,
        )
        print_verdict_payload("PRE-REG-INC", value, audit_sha, content_sha)
        return

    SE16 = z["sector_evals_L16"].item()    # (local) COMPLETE p+q<=15 triangle (136 sectors)
    cache_herm_err_max = float(z["herm_err_max"])  # (local) 1.13e-15 (S106 stored)
    z.close()
    print(f"[cache] sector_evals_L16: {len(SE16)} sectors (complete p+q<=15)  "
          f"cache_herm_err_max={cache_herm_err_max:.2e}")

    # --- W9-lineage reproduction guard: rho_B(13,14,15) on SE16 must match the W9 anchors ---
    rho_B = {}                                             # (local)
    rho_meta = {}                                          # (local)
    for L in (10, 12, 13, 14, 15):
        rr = rho_zubarev_from_sectors(SE16, L, LAMBDA_Z)
        rho_B[L] = rr["rho"]
        rho_meta[L] = rr
    w9_repro = {13: abs(rho_B[13] - RHO_B_13_W9), 14: abs(rho_B[14] - RHO_B_14_W9),
                15: abs(rho_B[15] - RHO_B_15_W9), 10: abs(rho_B[10] - RHO_B_10_W9)}  # (local)
    w9_repro_max = max(w9_repro.values())                  # (local)
    w9_lineage_ok = w9_repro_max <= REPRO_TOL              # (local)
    print(f"[w9-lineage] rho_B(10/13/14/15)={rho_B[10]:.12f}/{rho_B[13]:.12f}/"
          f"{rho_B[14]:.12f}/{rho_B[15]:.12f}")
    print(f"[w9-lineage] reproduction max_diff={w9_repro_max:.2e} ok(<= {REPRO_TOL:.0e})={w9_lineage_ok}")

    # =====================================================================
    # BUILD the p+q=16 shell (or load resume cache)
    # =====================================================================
    shell = {}                                             # (local)
    resume_loaded = False                                  # (local)
    if P_RESUME.exists():
        try:
            zr = np.load(P_RESUME, allow_pickle=True)
            shell = zr["shell"].item()
            conj_sentinel_max = float(zr["conj_sentinel_max"])
            shell_herr_max = float(zr["herr_max"])
            build_times = json.loads(str(zr["build_times_json"].item()))
            lvl16_lam_max = float(zr["lvl16_lam_max"])
            lvl16_lam_max_sector = tuple(int(x) for x in zr["lvl16_lam_max_sector"])
            zr.close()
            have_all = all((p, 16 - p) in shell for p in range(0, 17))  # (local) all 17 level-16 sectors
            resume_loaded = bool(have_all and len(shell) == 17)
            print(f"[resume] loaded shell from {P_RESUME.name}: {len(shell)}/17 sectors "
                  f"complete={resume_loaded} conj_sentinel={conj_sentinel_max:.2e} "
                  f"herr={shell_herr_max:.2e} lam_max={lvl16_lam_max:.6f}@{lvl16_lam_max_sector}")
        except Exception as e:
            print(f"[resume] failed to load {P_RESUME.name}: {e}; rebuilding")
            resume_loaded = False

    if not resume_loaded:
        print("  --- BUILD p+q=16 shell: 9 upper-triangle sectors (conjugates by CPT) ---")
        gens, f_abc, gammas, E, Omega, device, dirac_abs_and_herr = build_dirac_pipeline()
        conj_gens = [-g.T for g in gens]                   # (local) (0,p) = conjugate of (p,0)
        print(f"[pipeline] device={device}  GT builder substituted for dense symmetric-power")
        t_build = time.time()                              # (local)
        shell, conj_sentinel_max, shell_herr_max, build_times, lvl16_lam_max, lvl16_lam_max_sector = \
            build_shell_16(gens, conj_gens, f_abc, dirac_abs_and_herr)
        print(f"[build] p+q=16 shell complete: {len(shell)}/17 sectors "
              f"({time.time()-t_build:.1f}s total)  lam_max={lvl16_lam_max:.6f}@{lvl16_lam_max_sector}")
        np.savez_compressed(
            P_RESUME, shell=np.array(shell, dtype=object),
            conj_sentinel_max=conj_sentinel_max, herr_max=shell_herr_max,
            build_times_json=json.dumps(build_times),
            lvl16_lam_max=lvl16_lam_max,
            lvl16_lam_max_sector=np.array(lvl16_lam_max_sector, dtype=np.int64),
        )
        print(f"[resume] saved shell to {P_RESUME.name}")

    # --- shell completeness + Hermiticity guards ---
    lvl16 = sorted([k for k in shell if (k[0] + k[1]) == 16])  # (local)
    complete_16 = (len(lvl16) == 17) and all(shell[k]["level"] == 16 for k in lvl16)  # (local)
    dmax_block = max(d["dim"] * 16 for d in shell.values())  # (local)
    ID_HERM_ERR_TOL = max(ID_HERM_ERR_TOL_IDEAL, np.sqrt(dmax_block) * EPS_F64)  # (local)
    shell_herm_ok = shell_herr_max <= ID_HERM_ERR_TOL      # (local)
    conj_sentinel_ok = conj_sentinel_max <= SENTINEL_TOL   # (local)
    # lambda_max(16) MUST come from the GT-pure (16,0)/(0,16) by Casimir-ordering (C_2=304/3 highest)
    lam_max_from_gt = lvl16_lam_max_sector in [(16, 0), (0, 16)]  # (local)
    print(f"[shell] complete_16={complete_16} ({len(lvl16)}/17)  herr_max={shell_herr_max:.2e}"
          f"(floor {ID_HERM_ERR_TOL:.2e}, ok={shell_herm_ok})  conj_sentinel={conj_sentinel_max:.2e}"
          f"(ok={conj_sentinel_ok})  lam_max@{lvl16_lam_max_sector}(GT-pure={lam_max_from_gt})")

    # =====================================================================
    # rho_B(16) on the merged (complete p+q<=15 lineage U new level-16 shell)
    # =====================================================================
    merged = dict(SE16)                                    # (local) complete p+q<=15
    merged.update(shell)                                   # 17 new level-16 sectors
    merged_max_level = max(d["level"] for d in merged.values())  # (local)
    print(f"[merge] merged: {len(merged)} sectors, max_level={merged_max_level}")

    for L in (14, 15, 16):
        rr = rho_zubarev_from_sectors(merged, L, LAMBDA_Z)
        rho_B[L] = rr["rho"]
        rho_meta[L] = rr
        print(f"  rho_B({L:2d}) [merged] = {rr['rho']:.15f}  (lam_max={rr['lam_max']:.6f}, "
              f"mean_Z={rr['mean_Z']:.6f}, n_modes={rr['n_modes']})")

    # --- rho_B(14),rho_B(15) on merged must equal the SE16 values (level-16 cut does NOT enter) ---
    rho15_merged_consistency = abs(rho_B[15] - RHO_B_15_W9)  # (local) MUST be ~0 (level-16 absent at L<=15)
    rho14_merged_consistency = abs(rho_B[14] - RHO_B_14_W9)  # (local)
    print(f"[xcheck] rho_B(15) merged-vs-W9 = {rho15_merged_consistency:.2e}; "
          f"rho_B(14) merged-vs-W9 = {rho14_merged_consistency:.2e} (<= {REPRO_TOL:.0e})")

    # --- lambda_max + mean_Z drivers (the substitution-chain core) ---
    lam_max_15 = rho_meta[15]["lam_max"]                   # (local)
    lam_max_16 = rho_meta[16]["lam_max"]                   # (local)
    mean_Z_15 = rho_meta[15]["mean_Z"]                     # (local)
    mean_Z_16 = rho_meta[16]["mean_Z"]                     # (local)
    lam_max_raises = lam_max_16 > lam_max_15               # (local) the p+q=16 shell RAISES lambda_max
    mean_Z_frozen = abs(mean_Z_16 - mean_Z_15)            # (local) Zubarev-suppressed shift (~1e-6)
    b_slope = lam_max_16 - lam_max_15                      # (local) d lambda_max / dL ~ 0.3747
    print(f"[driver] lambda_max(15)={lam_max_15:.6f} -> lambda_max(16)={lam_max_16:.6f} "
          f"(raises={lam_max_raises}, b={b_slope:.6f})")
    print(f"[driver] mean_Z(15)={mean_Z_15:.6f} -> mean_Z(16)={mean_Z_16:.6f} "
          f"(frozen shift={mean_Z_frozen:.2e})")

    # --- CAC offset (DERIVED at runtime; cancels in span) ---
    offset_B = float(w0_FW) - rho_B[L_ANCHOR]              # (local) = w0_FW - rho_B(L=10), CAC
    w0_cac = {L: rho_B[L] + offset_B for L in (10, 13, 14, 15, 16)}  # (local)
    cac_anchor_resid = abs(w0_cac[10] - float(w0_FW))      # (local) demarcation theorem residual
    print(f"[cac] offset_B = {offset_B:.12f}  [w0_FW={w0_FW} - rho_B(10)={rho_B[L_ANCHOR]:.12f}]")
    print(f"[cac] w0^CAC(10) = {w0_cac[10]:.15f}  (== w0_FW? resid={cac_anchor_resid:.2e})")
    for L in (14, 15, 16):
        print(f"  w0^CAC({L}) = {w0_cac[L]:.15f}")

    # --- spread_CAC{14,15,16} (sliding window, VERDICT object) + offset-cancellation cross-check ---
    w0_vals = np.array([w0_cac[L] for L in L_SCAN_primary])   # (local)
    rho_vals = np.array([rho_B[L] for L in L_SCAN_primary])   # (local)
    spread_CAC = float(w0_vals.max() - w0_vals.min())        # (local)
    spread_rho = float(rho_vals.max() - rho_vals.min())      # (local) offset-free (value-neutral)
    offset_cancellation_residual = abs(spread_CAC - spread_rho)  # (local) must be ~0
    spread_narrows = spread_CAC < SPREAD_CAC_W9_131415       # (local) vs spread_CAC{13,14,15}=0.0392902
    print(f"[span] spread_CAC{{14,15,16}} = {spread_CAC:.12f}  (offset-free = {spread_rho:.12f}; "
          f"resid={offset_cancellation_residual:.2e})")
    print(f"[span] vs W9 spread_CAC{{13,14,15}}={SPREAD_CAC_W9_131415:.7f}: narrows={spread_narrows}")

    # --- decrement-deceleration (the PRIMARY [SIGN] sub-claim) ---
    d_14_15 = rho_B[15] - rho_B[14]                        # (local) reproduces W9 -0.018456
    d_15_16 = rho_B[16] - rho_B[15]                        # (local) the NEW decrement
    decrement_sign_negative = d_15_16 < 0                  # (local) monotone-decreasing rho_B
    decelerating = abs(d_15_16) < abs(d_14_15)             # (local) PRIMARY [SIGN] sub-claim
    decel_margin = abs(d_14_15) - abs(d_15_16)             # (local) > 0 if decelerating
    print(f"[decr] d(14->15)={d_14_15:+.8f}  d(15->16)={d_15_16:+.8f}  "
          f"sign_neg={decrement_sign_negative}  decelerating={decelerating}  "
          f"|d(14->15)|-|d(15->16)|={decel_margin:+.8f}")

    # --- 1/lambda_max^2 deceleration law cross-check (substitution chain Step 3-5) ---
    # |d(L->L+1)| = mean_Z*(1/lambda_max(L+1) - 1/lambda_max(L)) (mean_Z frozen)
    d_15_16_analytic = mean_Z_16 * (1.0 / lam_max_16 - 1.0 / lam_max_15)  # (local) analytic finite-diff
    law_residual = abs(d_15_16 - d_15_16_analytic)        # (local) empirical-vs-analytic decrement
    print(f"[law] d(15->16) empirical={d_15_16:+.8f}  analytic(mean_Z*Delta(1/lam_max))="
          f"{d_15_16_analytic:+.8f}  residual={law_residual:.2e}")

    # --- INV13 contrast: INV13 SET rho_B(16)==rho_B(15) by bottom-K FB saturation (WRONG here) ---
    inv13_shift = abs(rho_B[16] - INV13_RHO_B_16)         # (local) the genuine lambda_max-driven shift INV13 missed
    print(f"[inv13-contrast] this rho_B(16)={rho_B[16]:.6f} vs INV13 rho_B(16)={INV13_RHO_B_16:.6f} "
          f"(bottom-K FB-saturation artifact); genuine lambda_max-driven shift={inv13_shift:.6f}")

    # =====================================================================
    # VERDICT — INFO-BY-CONSTRUCTION (composite-precedence; corridor CLOSED-WITH-RESULT per W-5)
    # =====================================================================
    # Guards: cache integrity, W9 lineage reproduction, shell completeness/Hermiticity, GT-pure
    # conjugate sentinel, lambda_max from GT-pure, level-16 absent at L<=15, offset cancellation.
    guard_ok = (cache_integrity_ok and w9_lineage_ok and complete_16 and shell_herm_ok
                and conj_sentinel_ok and lam_max_from_gt and lam_max_raises
                and (rho15_merged_consistency <= REPRO_TOL)
                and (rho14_merged_consistency <= REPRO_TOL)
                and (offset_cancellation_residual < 1e-9)
                and (cac_anchor_resid < 1e-9))             # (local)

    # [SIGN] 3-tuple:
    #   sign     = the decrement-deceleration + monotone + offset-cancellation directional claim
    #   magnitude= the sliding-window spread NARROWING (diagnostic; not a corridor band gate)
    #   regime   = guards hold
    sign_v = ("PASS" if (decelerating and decrement_sign_negative
                         and offset_cancellation_residual < 1e-9) else "FAIL")  # (local)
    magnitude_v = "PASS" if spread_narrows else "INFO"     # (local) narrowing continues (diagnostic)
    regime_v = "VALID" if guard_ok else "MARGINAL"         # (local)

    # COMPOSITE forced INFO by the `# composite-precedence:` row (corridor CLOSED-WITH-RESULT, W-5).
    # A FAIL is reserved for SCRIPT BREAKAGE only (guards catch build failure). The directional
    # 3-tuple is reported; the composite never PASS-reopens nor FAIL-closes the corridor.
    if not (cache_integrity_ok and complete_16 and conj_sentinel_ok and w9_lineage_ok):
        # script-breakage class -> honest mechanical closure (build/sentinel/lineage failed)
        verdict = "FAIL"
    else:
        verdict = "INFO"
    print(f"[VERDICT] INFO-by-construction (corridor CLOSED-WITH-RESULT per W-5)  "
          f"rho_B(16)={rho_B[16]:.6f}  spread_CAC{{14,15,16}}={spread_CAC:.6g}  "
          f"d(15->16)={d_15_16:+.6f}  decelerating={decelerating}  spread_narrows={spread_narrows}  "
          f"guard_ok={guard_ok}  => {verdict}")

    # --- persist npz ---
    shell_keys = np.array([list(k) for k in sorted(shell)], dtype=np.int64)  # (local)
    np.savez_compressed(
        SESSION_DIR / "s117_branch_iv_l16.npz",
        verdict=verdict, phase="L16_COMPLETE",
        L_SCAN_primary=np.array(L_SCAN_primary, dtype=np.int64), L_anchor=L_ANCHOR, L_shell=L_SHELL,
        # rho_B trajectory:
        rho_B_10=rho_B[10], rho_B_13=rho_B[13], rho_B_14=rho_B[14],
        rho_B_15=rho_B[15], rho_B_16=rho_B[16],
        rho_B_window=np.array([rho_B[L] for L in L_SCAN_primary]),
        lam_max_15=lam_max_15, lam_max_16=lam_max_16, b_slope=b_slope,
        mean_Z_15=mean_Z_15, mean_Z_16=mean_Z_16, mean_Z_frozen_shift=mean_Z_frozen,
        n_modes_16=rho_meta[16]["n_modes"], n_modes_15=rho_meta[15]["n_modes"],
        lam_max_raises=lam_max_raises, lam_max_from_gt=lam_max_from_gt,
        lvl16_lam_max=lvl16_lam_max,
        lvl16_lam_max_sector=np.array(lvl16_lam_max_sector, dtype=np.int64),
        # CAC:
        w0_FW=float(w0_FW), offset_B=offset_B, offset_B_W9=OFFSET_B_W9,
        w0_cac=np.array([w0_cac[L] for L in (14, 15, 16)]), w0_cac_10=w0_cac[10],
        cac_anchor_resid=cac_anchor_resid,
        # spread + decrement (VERDICT objects):
        spread_CAC=spread_CAC, spread_rho=spread_rho,
        offset_cancellation_residual=offset_cancellation_residual,
        spread_CAC_W9_131415=SPREAD_CAC_W9_131415, spread_narrows=spread_narrows,
        d_14_15=d_14_15, d_15_16=d_15_16, D_14_15_W9=D_14_15_W9, D_13_14_W9=D_13_14_W9,
        decrement_sign_negative=decrement_sign_negative, decelerating=decelerating,
        decel_margin=decel_margin,
        d_15_16_analytic=d_15_16_analytic, law_residual=law_residual,
        # INV13 contrast:
        INV13_RHO_B_16=INV13_RHO_B_16, inv13_shift=inv13_shift,
        # shell build provenance:
        conj_sentinel_max=conj_sentinel_max, conj_sentinel_ok=conj_sentinel_ok,
        shell_herr_max=shell_herr_max, ID_HERM_ERR_TOL=ID_HERM_ERR_TOL, shell_herm_ok=shell_herm_ok,
        complete_16=complete_16, n_lvl16=len(lvl16), shell_keys=shell_keys,
        build_times_json=json.dumps(build_times),
        # lineage / integrity guards:
        w9_repro_max=w9_repro_max, w9_lineage_ok=w9_lineage_ok,
        rho15_merged_consistency=rho15_merged_consistency,
        rho14_merged_consistency=rho14_merged_consistency,
        cache_integrity_ok=cache_integrity_ok, cache_internal_sha=cache_internal_sha,
        cache_herm_err_max=cache_herm_err_max,
        guard_ok=guard_ok,
        # verdict 3-tuple:
        sign_verdict=sign_v, magnitude_verdict=magnitude_v, regime_verdict=regime_v,
        # provenance:
        Lambda_Z=LAMBDA_Z, jensen_s=JENSEN_S, Gamma_effacement=float(Gamma_effacement),
        N_cells=int(N_cells), canonical_sha_live=canonical_sha_live,
        n_sectors_merged=len(merged), n_sectors_SE16=len(SE16),
        audit_sha256=audit_sha, content_sha256=content_sha, closure_hash=closure,
    )

    _make_plot(rho_B, w0_cac, spread_CAC, verdict, lam_max_15, lam_max_16,
               d_14_15, d_15_16, decel_margin, spread_narrows)

    # --- value payload (6 sig figs; Class-8.3 publication precision; DESI DR3 w0 consumer) ---
    value = (f"rho_B(16)={rho_B[16]:.6f} spread_CAC{{14,15,16}}={spread_CAC:.6g} "
             f"d(15->16)={d_15_16:.6f}<d(14->15)={d_14_15:.6f}_DECEL "
             f"lam_max(15)={lam_max_15:.6f}->lam_max(16)={lam_max_16:.6f}@{lvl16_lam_max_sector} "
             f"mean_Z_frozen_shift={mean_Z_frozen:.2e} w0CAC(16)={w0_cac[16]:.6f} "
             f"offset_B={offset_B:.6f} spread_narrows={spread_narrows} "
             f"conj_sentinel={conj_sentinel_max:.1e} INV13_contrast_shift={inv13_shift:.6f} "
             f"INFO-by-construction_corridor-CLOSED-WITH-RESULT")
    extra_rows = [
        ("# composite-precedence: session-117-plan-w7.md §W7-3 + workshops/s116-w0-spectral-derivability.md "
         "(W-5 R3-FINAL closure). Generic 3-tuple collapse would read PASS "
         "(sign=PASS decel + magnitude=PASS narrows + regime=VALID); OVERRIDDEN to composite INFO "
         "because the branch-iv corridor is CLOSED-WITH-RESULT and is NOT reopenable by a "
         "value-neutral L_max diagnostic (the spread is offset-invariant -> certifies rho_B->-1 "
         "smoothly, NOT support for -0.918)."),
        (f"# regulator_pin=a_2^{{Mellin}} poleconv-A-double (pole_in_s=3, curvature_grade_n=2); "
         f"cutoff_axis=spectral (Zubarev Lambda_Z={LAMBDA_Z} on D_K spectrum); "
         f"GT(p,0)-bosonic-ladder + Casimir-projection mixed; conj-CPT-symmetry halved-build "
         f"(9 upper-triangle sectors, conj_sentinel={conj_sentinel_max:.1e}); cache_integrity=5af2b7cd"),
        (f"# lambda_max-DRIVEN: lambda_max(15)={lam_max_15:.6f}->lambda_max(16)={lam_max_16:.6f} "
         f"(GT-pure {lvl16_lam_max_sector}, C2=304/3 highest) RAISES denominator; mean_Z frozen "
         f"{mean_Z_15:.6f}->{mean_Z_16:.6f}(shift {mean_Z_frozen:.1e}); rho_B(16)={rho_B[16]:.6f} "
         f"!= INV13 rho_B(16)={INV13_RHO_B_16:.6f} (bottom-K FB-saturation artifact, ORTHOGONAL "
         f"to lambda_max-driven moment); 1/lam_max^2 law residual={law_residual:.1e}"),
    ]
    print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_v=sign_v, magnitude_v=magnitude_v, regime_v=regime_v,
                          extra_rows=extra_rows)


def _make_plot(rho_B, w0_cac, spread_CAC, verdict, lam_max_15, lam_max_16,
               d_14_15, d_15_16, decel_margin, spread_narrows):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 5))

    # Panel 1: rho_B(L) trajectory with the new L=16 point highlighted
    Ls = [13, 14, 15, 16]
    ax1.plot(Ls, [rho_B[L] for L in Ls], "o-", color="C0", label=r"$\rho_B(L)$ (complete lineage)")
    ax1.plot([16], [rho_B[16]], "D", color="C3", ms=11, label=r"$\rho_B(16)$ NEW (shell built)")
    ax1.axhline(rho_B[15], color="C7", ls=":", lw=0.8,
                label=fr"INV13 $\rho_B(16){{=}}\rho_B(15){{=}}{rho_B[15]:.4f}$ (FB-bottom-K artifact)")
    ax1.plot([14, 15, 16], [rho_B[L] for L in (14, 15, 16)], "o", color="C1", ms=11,
             mfc="none", mew=2, label=r"verdict window $\{14,15,16\}$")
    ax1.set_xlabel("truncation L (p+q)")
    ax1.set_ylabel(r"$\rho_B(L)$  (Zubarev branch-IV moment)")
    ax1.set_title(r"$\rho_B(L)$: $\lambda_{\max}$-driven $\to -1$"
                  "\n(L=16 shell BUILT, not FB-saturated)")
    ax1.set_xticks(Ls)
    ax1.grid(alpha=0.3)
    ax1.legend(fontsize=7)

    # Panel 2: w0^CAC(L) vs w0_FW; sliding-window spread
    L2 = [13, 14, 15, 16]
    ax2.plot(L2, [w0_cac[L] for L in L2], "s-", color="C2",
             label=r"$w_0^{\rm CAC}(L)=\rho_B(L)+{\rm offset}_B$")
    ax2.axhline(float(w0_FW), color="k", ls=":", lw=1, label=fr"$w_0^{{FW}}={w0_FW}$")
    ax2.set_xlabel("truncation L (p+q)")
    ax2.set_ylabel(r"$w_0^{\rm CAC}(L)$")
    ax2.set_title(fr"$w_0^{{\rm CAC}}$: spread$\{{14,15,16\}}={spread_CAC:.5f}$"
                  fr"$\Rightarrow$ {verdict}"
                  "\n(value-neutral; corridor CLOSED-WITH-RESULT)")
    ax2.set_xticks(L2)
    ax2.grid(alpha=0.3)
    ax2.legend(fontsize=8)

    # Panel 3: decrement-deceleration |d(L->L+1)| vs 1/lambda_max^2 law
    decs = [13, 14, 15]
    dvals = [abs(rho_B[14] - rho_B[13]), abs(d_14_15), abs(d_15_16)]   # (local) |d(13->14)|,|d(14->15)|,|d(15->16)|
    ax3.plot(decs, dvals, "o-", color="C3", label=r"$|d(L\to L{+}1)|$ (empirical)")
    ax3.set_xlabel("decrement step $L\\to L{+}1$")
    ax3.set_ylabel(r"$|d(L\to L{+}1)| = |\rho_B(L{+}1)-\rho_B(L)|$")
    ax3.set_title(fr"decrement decelerates ($|d|\sim 1/\lambda_{{\max}}^2$)"
                  f"\nmargin $|d(14{{\\to}}15)|-|d(15{{\\to}}16)|={decel_margin:+.5f}$")
    ax3.set_xticks(decs)
    ax3.set_xticklabels([r"$13\to14$", r"$14\to15$", r"$15\to16$"])
    ax3.grid(alpha=0.3)
    ax3.legend(fontsize=8)

    fig.suptitle(f"{GATE_ID} — branch-IV $w_0$ L_max diagnostic at p+q=16 "
                 f"($\\lambda_{{\\max}}$-driven shift, shell BUILT; INFO-by-construction)", fontsize=12)
    fig.tight_layout()
    fig.savefig(SESSION_DIR / "s117_branch_iv_l16.png", dpi=120)
    plt.close(fig)


if __name__ == "__main__":
    main()
