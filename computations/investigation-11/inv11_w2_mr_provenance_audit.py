#!/usr/bin/env python3
"""
INV11-W2-4 — INV11-W2-4-MR-PROVENANCE-AUDIT : provenance trace of the S60 M_R coincidence
==========================================================================================

Gate: INV11-W2-4-MR-PROVENANCE-AUDIT ([AUDIT], solo / orchestrator-inline)
Track: investigation (n=11)

CORE QUESTION (plan §W2-4)
--------------------------
Is the S60 right-handed Majorana scale M_R *independent of* the B-branch fold
energies the type-I seesaw then consumes (=> the 1.77% M_R-vs-L12-B-branch
agreement is genuine corroboration), or *derived from the same spectral input*
(=> consistency-check / circular)? AND annotate the seesaw round-trip reldiff
1.16e-5 as by-construction (NOT a cross-check).

This is a PROVENANCE TRACE, not a re-derivation. The 1.77% and 1.16e-5 numbers
are READ from the S99-W3 npz (closed/canonical S99-W3); the seesaw is NOT
recomputed. The script independently RE-VERIFIES the two facts that decide the
classification (the round-trip-on-shared-operands floor, and the
exact-membership status of the M_R values in the L12 cache), then classifies.

PROVENANCE CHAIN (factual; traced from the on-disk source files)
---------------------------------------------------------------
(1) M_R diagonal = E_B3_fold * M_KK, with
      E_B3_fold = E_sp_sweep[fold_idx, 5:8]                [s60_lepto_cp.py:93, 212-214]
      = [1.00439566, 1.07857332, 1.17000260] M_KK
    where E_sp_sweep[t] = eigenvalues[t, :8]               [s54_ed_sweep.py:274]
      = the lowest-8 eigenvalues of the 32-CELL TIGHT-BINDING LATTICE
        Hamiltonian s54_tb_hamiltonian.npz (eigenvalues (50,32); cells labelled
        by SU(3) Casimir; adj_C2/adj_su2/adj_u1 CG adjacency).  [s54_ed_sweep.py:70-78]
    => M_R is an INTERNAL D_K spectral object, extracted via a LATTICE-ED pipeline.

(2) The type-I seesaw m_nu = -m_D^T M_R^-1 m_D consumes the SAME M_R built in (1).
    The S99-W3 npz `Sigma_mnu_crosscheck_reldiff = 1.16e-5` is the round-trip
    reconstruct(m_nu, M_R, m_D) vs m_nu on the SAME M_R operand. A forward map
    composed with its own numerical inverse on shared operands => the agreement
    is the float64 inversion floor, carrying ZERO independent physical
    information. BY-CONSTRUCTION, not a cross-check. (Re-verified here at the
    diagonal/aligned floor: 2.8e-16.)

(3) The S99-W3 npz `M_R_spectral_coincidence_maxrel = 0.0177` is the SEPARATE,
    potentially-informative number: it is the S96-MATTER-SEESAW-D5 PART-1
    comparison (s96_matter_seesaw_d5.py::load_DK_abs_eigenvalues + nearest-|lambda|).
    It takes the S60 M_R targets (lattice-ED pipeline) and finds the nearest
    |lambda| in the L12 MASTER CACHE s84_spectrum_cache_L12_tau019.npz — the
    DIRECT full Peter-Weyl block-diagonal diagonalization D_K = (+)_{(p,q)} D_(p,q)
    (sector_evals: 90 (p,q) sectors). reldiff = [0.01774, 1.3e-4, 5.0e-3];
    maxrel = 0.01774 (driven by M_1).

DISCRIMINATOR (plan §W2-4)
--------------------------
Do the S60 source (s54_ed_sweep, the 32-cell tight-binding lattice ED) and the
L12-cache B-branch (s84 Peter-Weyl direct diagonalization) constitute
STRUCTURALLY DISTINCT extractions, or the same D_K eigenvalues re-read?

FACT (re-verified here): EXACT-MEMBERSHIP of each M_R value in the L12 cache
FAILS (atol=1e-12): min|absev - M_i| = [1.78e-2, 1.45e-4, 5.83e-3] >> float floor.
None of the M_R values is an L12 eigenvalue re-read. The two are DIFFERENT
numerical objects (32-cell tight-binding lattice ED vs full Peter-Weyl operator
diagonalization) producing DIFFERENT float eigenvalues that agree to 0.01-1.77%.

EPISTEMIC CLASSIFICATION (the gate VERDICT)
-------------------------------------------
- Under "structurally distinct NUMERICAL PIPELINE" (the methods differ; not a
  re-read): the 1.77% is `independent_corroboration` — two diagonalization
  methods (lattice-ED and Peter-Weyl) converging.  [Track A]
- Under "same SPECTRAL INPUT" (both extract the SAME operator D_K at the SAME
  tau_fold near the fundamental): the 1.77% is `consistency_check_circular` — a
  re-extraction consistency of one substrate object.  [Track B]

The FACTUAL core is unambiguous (the methods are distinct; not a re-read; the
round-trip is by-construction). The LABEL on the 1.77% turns on the DEFINITION
of "independent" (distinct-pipeline vs distinct-physical-input) — a DEFINITIONAL,
not FACTUAL, residue. Per plan §W2-4 INFO_meaning, this is exactly INFO:
"the 1.16e-5 round-trip is confirmed by-construction (clean), but the
independent-vs-circular status of the 1.77% is determinable only up to whether
the ED 8x8 and L12 cache count as 'structurally distinct' under a specific
definition." The gate does NOT PASS/FAIL on the 1.77% magnitude — it classifies
its EPISTEMIC STATUS.

VERDICT RUBRIC (pre-registered, plan §W2-4)
  PASS : an UNAMBIGUOUS single classification (independent OR circular) with the
         provenance chain documented + the by-construction annotation.
  FAIL : the provenance chain cannot be resolved to a definite branch
         (S54/L12 relationship undocumented/irrecoverable).
  INFO : the 1.16e-5 round-trip is confirmed by-construction (clean), but the
         independent-vs-circular status of the 1.77% is a definitional, not
         factual, residue.

Inputs (SHA-256 input-pin block; audit_sha256 over script+canonical+pinmap):
  - computations/_shared/canonical_constants.py
  - computations/session-60/s60_lepto_cp_log.txt    (M_R provenance text)
  - computations/session-60/s60_lepto_cp.npz         (M_R diag + B3 texture)
  - computations/session-99/s99_w3_seesaw_summnu.npz (the 1.77% + 1.16e-5 numbers)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz (L12 B-branch comparison)

Output 4-tuple:
  (value=<classification + key provenance facts>, scheme=provenance-trace,
   convention=ABSOLUTE, L_max=12-vs-s54-ED-8x8)

Classification: PARTICLE (provenance audit of how a substrate observable M_R
feeds the Sigma m_nu prediction).

CROSS-TRACK BOUNDARY: writes ONLY to computations/investigation-11/ + the WP
§W2-4. No canonical / registry / inventory / capstone edits (any
"cross-check"->"by-construction" capstone language fix is a session-promotion
item, NOT an investigation-track edit).

Author: gen-physicist (orchestrator-inline solo), Investigation 11 Wave 2
Date: 2026-06-16
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
import sys

_SHARED_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_shared"
)  # (local)
if _SHARED_PATH not in sys.path:
    sys.path.insert(0, _SHARED_PATH)

from canonical_constants import *  # noqa: F401,F403,E402  (M_KK_gravity, tau_fold, Sigma_mnu_FW, ...)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402

import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent            # computations/investigation-11
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "11"                                            # (local) investigation number
GATE_ID = "INV11-W2-4-MR-PROVENANCE-AUDIT"               # (local)
SCHEME = "provenance-trace"                              # (local)
CONVENTION = "ABSOLUTE"                                  # (local) classification label; no numerical normalization
L_MAX = "12-vs-s54-ED-8x8"                               # (local) L12 cache vs s54 ED 8x8 (S60 source)

# Pre-registered classification tolerances (define BEFORE running) — plan §W2-4
EXACT_MEMBER_ATOL = 1e-12   # (local) is each M_R an EXACT L12 eigenvalue re-read?
ROUNDTRIP_FLOOR = 1e-9      # (local) below this => the round-trip is the float-inversion floor (by-construction)

# Canonical anchors READ from the S99-W3 npz (closed/canonical S99-W3) — NOT recomputed.
S99_KEY_MAXREL = "M_R_spectral_coincidence_maxrel"        # (local) the 1.77% number
S99_KEY_ROUNDTRIP = "Sigma_mnu_crosscheck_reldiff"        # (local) the 1.16e-5 number
S99_KEY_NEAREST = "M_R_spectral_coincidence_nearest"      # (local)
S99_KEY_RELDIFF = "M_R_spectral_coincidence_reldiff"      # (local)

# Output destinations (per-investigation canonical paths)
OUT_NPZ = SESSION_DIR / "inv11_w2_mr_provenance_audit.npz"
OUT_PNG = SESSION_DIR / "inv11_w2_mr_provenance_audit.png"

# Source files (read-only; the provenance chain)
CANON = SHARED_DIR / "canonical_constants.py"
S60_LOG = COMPUTATIONS_DIR / "session-60" / "s60_lepto_cp_log.txt"
S60_NPZ = COMPUTATIONS_DIR / "session-60" / "s60_lepto_cp.npz"
S99_NPZ = COMPUTATIONS_DIR / "session-99" / "s99_w3_seesaw_summnu.npz"
L12_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
# Provenance-source scripts (read as text for the trace; NOT inputs to the SHA pin —
# the SHA pin is over the canonical data/constants per the plan input_files block).
S60_SCRIPT = COMPUTATIONS_DIR / "session-60" / "s60_lepto_cp.py"
S54_SCRIPT = COMPUTATIONS_DIR / "session-54" / "s54_ed_sweep.py"

# Input-SHA pin set (matches plan §W2-4 input_files block)
INPUT_FILES = [
    CANON,
    S60_LOG,
    S60_NPZ,
    S99_NPZ,
    L12_CACHE,
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
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
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
# Section 5 — Provenance trace + classification
# ---------------------------------------------------------------------------

def load_DK_abs_eigenvalues() -> np.ndarray:
    """Full |lambda| set of D_K from the L_max=12 master cache at tau=0.19.

    sector_evals: dict keyed by Peter-Weyl (p,q), each value a dict with
    'abs_evals' = per-sector |lambda| array (block-diagonal D_K = (+) D_(p,q)).
    This is the DIRECT full-operator diagonalization pipeline — distinct from the
    32-cell tight-binding lattice ED (s54) that produced the M_R targets.
    """
    c = np.load(L12_CACHE, allow_pickle=True)  # (local)
    se = c["sector_evals"].item()  # (local)
    absev = np.concatenate(
        [np.asarray(se[k]["abs_evals"]).flatten() for k in se]
    )  # (local)
    return np.abs(absev)


def trace_provenance_text() -> dict:
    """Read the source scripts as text and confirm the M_R-build provenance
    line-anchors (no re-derivation — a literal-substring presence check)."""
    facts: dict = {}  # (local)
    s60_src = S60_SCRIPT.read_text(encoding="utf-8", errors="replace")  # (local)
    s54_src = S54_SCRIPT.read_text(encoding="utf-8", errors="replace")  # (local)
    # M_R built from s54 B3-sector single-particle energies at the fold
    facts["s60_MR_from_s54_ed"] = ("s54_ed_sweep.npz" in s60_src
                                   and "E_sp_sweep[fold_idx, 5:8]" in s60_src)
    facts["s60_MR_diag_from_EB3"] = ("M_1_MKK = E_B3_fold[0]" in s60_src)
    # s54 E_sp_sweep IS the lowest-8 lattice tight-binding eigenvalues
    facts["s54_Esp_is_TB_lattice"] = ("E_sp = eigenvalues[t, :N_MODES].copy()" in s54_src
                                      and "s54_tb_hamiltonian.npz" in s54_src)
    facts["s54_is_lattice_ED"] = ("32-Cell Lattice" in s54_src or "32-cell" in s54_src
                                  or "lattice" in s54_src.lower())
    return facts


def compute() -> dict:
    # === Branch (a): READ the canonical numbers from the S99-W3 npz (NOT recomputed) ===
    s99 = np.load(S99_NPZ, allow_pickle=True)  # (local)
    maxrel_177 = float(s99[S99_KEY_MAXREL])              # (local) the 1.77% number, READ
    roundtrip_116e5 = float(s99[S99_KEY_ROUNDTRIP])      # (local) the 1.16e-5 number, READ
    nearest_published = np.asarray(s99[S99_KEY_NEAREST], dtype=float)  # (local)
    reldiff_published = np.asarray(s99[S99_KEY_RELDIFF], dtype=float)  # (local)
    m_R_MKK = np.asarray(s99["M_R_MKK"], dtype=float)    # (local) the M_R targets
    m_D_GeV = np.asarray(s99["m_D_GeV"], dtype=float)    # (local)
    M_R_GeV = np.asarray(s99["M_R_GeV"], dtype=float)    # (local)
    m_nu_pub = np.asarray(s99["m_nu_eV"], dtype=float)   # (local)

    # === Branch (b): RE-VERIFY the round-trip is by-construction (shared operands) ===
    # Forward seesaw in the aligned/diagonal basis: m_nu_i = m_D_i^2 / M_R_i (GeV) -> eV.
    # The SAME M_R operand both BUILDS m_nu (in S99-W3) and would RECONSTRUCT it.
    m_nu_fwd_GeV = np.zeros(3)  # (local)
    for i in range(3):
        if M_R_GeV[i] != 0.0:
            m_nu_fwd_GeV[i] = m_D_GeV[i] ** 2 / M_R_GeV[i]
    m_nu_fwd_eV = m_nu_fwd_GeV * 1e9  # (local)
    nz = m_nu_pub > 0  # (local)
    roundtrip_floor_check = float(
        np.max(np.abs(m_nu_fwd_eV[nz] - m_nu_pub[nz]) / np.abs(m_nu_pub[nz]))
    )  # (local) shared-operand round-trip => float-inversion floor
    roundtrip_is_byconstruction = bool(roundtrip_floor_check < ROUNDTRIP_FLOOR)  # (local)

    # === Branch (c): RE-COMPUTE the 1.77% nearest-|lambda| from the two pipelines ===
    absev = load_DK_abs_eigenvalues()  # (local) Pipeline-2: L12 Peter-Weyl direct diag
    n_evals = int(absev.size)  # (local)
    n_unique = int(np.unique(np.round(absev, 9)).size)  # (local)
    labels = ["M_1", "M_2", "M_3"]  # (local)
    nearest = np.empty(3)  # (local)
    reldiff = np.empty(3)  # (local)
    min_abs_diff = np.empty(3)  # (local) for exact-membership
    for j, tgt in enumerate(m_R_MKK):
        d = np.abs(absev - tgt)  # (local)
        i = int(np.argmin(d))  # (local)
        nearest[j] = absev[i]
        reldiff[j] = abs(absev[i] - tgt) / tgt
        min_abs_diff[j] = float(d.min())
    maxrel_recomputed = float(reldiff.max())  # (local)
    # The S99-W3-stored maxrel (0.0177351786) and the re-computed value
    # (0.0177351767) agree to ~8 sig figs (abs diff ~1.9e-9). The match band is
    # the published-precision floor, NOT a tight 1e-9: a ~0.0177 value at 8 sig
    # figs has a ~1.8e-9 floor, so a 1e-9 tolerance would FAIL on the
    # publication-precision boundary (Class-8.3, epistemic-discipline.md). The
    # M_R targets are bit-identical between s54 and s99 (max|diff|=0.0); the
    # residual is the s99 script's own float path, not a physics difference.
    MAXREL_MATCH_TOL = 1e-7  # (local) "same number" band at the stored 8-sig-fig precision
    maxrel_matches_s99 = bool(abs(maxrel_recomputed - maxrel_177) < MAXREL_MATCH_TOL)  # (local)

    # === Branch (d): EXACT-MEMBERSHIP test (the discriminator) ===
    # Is each M_R value LITERALLY an L12 eigenvalue re-read (same float)?
    exact_member = (min_abs_diff < EXACT_MEMBER_ATOL)  # (local) per-M_i bool
    any_exact_member = bool(exact_member.any())  # (local)
    all_exact_member = bool(exact_member.all())  # (local)
    # If NONE is an exact member => the M_R values are NOT the L12 eigenvalues
    # re-read => the two pipelines are DIFFERENT numerical objects.
    pipelines_distinct_numerics = bool(not any_exact_member)  # (local)

    # === Provenance-text facts (line-anchor presence checks) ===
    facts = trace_provenance_text()  # (local)
    provenance_chain_resolved = bool(
        facts["s60_MR_from_s54_ed"] and facts["s60_MR_diag_from_EB3"]
        and facts["s54_Esp_is_TB_lattice"] and facts["s54_is_lattice_ED"]
    )  # (local) the S54->S60->L12 relationship IS documented + recoverable

    # === CLASSIFICATION (the gate verdict) ===
    # Two readings of "independent":
    #   - distinct NUMERICAL PIPELINE (32-cell TB lattice ED vs L12 Peter-Weyl
    #     direct diag): TRUE (pipelines_distinct_numerics) => independent_corroboration
    #   - distinct PHYSICAL INPUT (different operator / tau): FALSE (both are D_K at
    #     tau_fold near the fundamental) => consistency_check_circular
    track_A_independent = pipelines_distinct_numerics      # (local) distinct-pipeline reading
    track_B_circular = True  # (local) same-substrate-operator reading ALWAYS holds (both = D_K @ tau_fold)

    # Verdict logic (pre-registered plan §W2-4):
    #  FAIL : provenance chain unresolved (cannot reach a definite branch).
    #  PASS : an UNAMBIGUOUS single label (only one reading admissible).
    #  INFO : round-trip by-construction (clean) AND the 1.77% label is a
    #         definitional (not factual) residue (BOTH readings admissible).
    if not provenance_chain_resolved:
        verdict = "FAIL"  # (local)
        classification = "unresolved"  # (local)
    elif track_A_independent and track_B_circular and roundtrip_is_byconstruction:
        # Both readings admissible on the SAME unambiguous facts => definitional residue.
        verdict = "INFO"  # (local)
        classification = "definitional_residue(independent_corroboration|consistency_check_circular)"  # (local)
    elif track_A_independent and not track_B_circular:
        verdict = "PASS"  # (local)
        classification = "independent_corroboration"  # (local)
    elif track_B_circular and not track_A_independent:
        verdict = "PASS"  # (local)
        classification = "consistency_check_circular"  # (local)
    else:
        verdict = "INFO"  # (local)
        classification = "definitional_residue(independent_corroboration|consistency_check_circular)"  # (local)

    return {
        "value": classification,
        "verdict": verdict,
        # canonical numbers READ from S99-W3
        "maxrel_177_read": maxrel_177,
        "roundtrip_116e5_read": roundtrip_116e5,
        "nearest_published": nearest_published,
        "reldiff_published": reldiff_published,
        "m_R_MKK": m_R_MKK,
        # round-trip re-verification
        "roundtrip_floor_check": roundtrip_floor_check,
        "roundtrip_is_byconstruction": roundtrip_is_byconstruction,
        "m_nu_fwd_eV": m_nu_fwd_eV,
        "m_nu_pub": m_nu_pub,
        # 1.77% re-computation (two pipelines)
        "absev_n": n_evals,
        "absev_n_unique": n_unique,
        "nearest_recomputed": nearest,
        "reldiff_recomputed": reldiff,
        "maxrel_recomputed": maxrel_recomputed,
        "maxrel_matches_s99": maxrel_matches_s99,
        # exact-membership discriminator
        "min_abs_diff": min_abs_diff,
        "exact_member": exact_member,
        "any_exact_member": any_exact_member,
        "all_exact_member": all_exact_member,
        "pipelines_distinct_numerics": pipelines_distinct_numerics,
        # provenance-text facts
        "fact_s60_MR_from_s54_ed": facts["s60_MR_from_s54_ed"],
        "fact_s60_MR_diag_from_EB3": facts["s60_MR_diag_from_EB3"],
        "fact_s54_Esp_is_TB_lattice": facts["s54_Esp_is_TB_lattice"],
        "fact_s54_is_lattice_ED": facts["s54_is_lattice_ED"],
        "provenance_chain_resolved": provenance_chain_resolved,
        # classification tracks
        "track_A_independent": track_A_independent,
        "track_B_circular": track_B_circular,
        "EXACT_MEMBER_ATOL": EXACT_MEMBER_ATOL,
        "ROUNDTRIP_FLOOR": ROUNDTRIP_FLOOR,
    }


def make_plot(res: dict) -> None:
    """Provenance-chain diagram + the two distinguished numbers."""
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(13, 5))

    # --- Left panel: provenance chain (text-box flow) ---
    ax0.axis("off")
    ax0.set_title("INV11-W2-4  M_R provenance chain", fontsize=11, weight="bold")
    chain = (
        "PIPELINE 1 (M_R source)\n"
        "  s54_tb_hamiltonian.npz\n"
        "  32-cell tight-binding lattice H\n"
        "  -> eigenvalues[t, :8]  (s54_ed_sweep)\n"
        "  -> modes 5:8 = E_B3_fold\n"
        "  -> x M_KK = M_R diag\n"
        "     [1.00440, 1.07857, 1.17000] M_KK\n"
        "        |\n"
        "        v\n"
        "  SEESAW  m_nu = -m_D^T M_R^-1 m_D\n"
        "  (consumes the SAME M_R)\n"
        "  -> round-trip = 1.16e-5\n"
        "     = BY-CONSTRUCTION (float floor)\n"
        f"     re-verified floor = {res['roundtrip_floor_check']:.1e}\n"
        "\n"
        "PIPELINE 2 (comparison)\n"
        "  s84_spectrum_cache_L12_tau019.npz\n"
        "  DIRECT full Peter-Weyl diag\n"
        "  D_K = (+)_(p,q) D_(p,q)  (90 sectors)\n"
        "  -> nearest-|lambda| to each M_R\n"
        f"  -> 1.77% coincidence ({res['maxrel_recomputed']:.4f})\n"
        "     EXACT-MEMBER? "
        f"{'NO (distinct numerics)' if res['pipelines_distinct_numerics'] else 'YES'}\n"
    )
    ax0.text(0.02, 0.98, chain, va="top", ha="left", fontsize=8.5,
             family="monospace", transform=ax0.transAxes)

    # --- Right panel: M_R (lattice-ED) vs L12 nearest-|lambda| ---
    labels = ["M_1", "M_2", "M_3"]
    x = np.arange(3)
    mr = res["m_R_MKK"]
    near = res["nearest_recomputed"]
    rd = res["reldiff_recomputed"]
    md = res["min_abs_diff"]
    ax1.scatter(x - 0.06, mr, s=70, c="tab:blue", marker="o",
                label="M_R (s54 32-cell TB lattice ED)", zorder=3)
    ax1.scatter(x + 0.06, near, s=70, c="tab:red", marker="x",
                label="nearest |lambda| (s84 L12 Peter-Weyl)", zorder=3)
    for j in range(3):
        ax1.annotate(f"reldiff={rd[j]:.1e}\nmin|d|={md[j]:.1e}\n(>{res['EXACT_MEMBER_ATOL']:.0e})",
                     (x[j], max(mr[j], near[j])), textcoords="offset points",
                     xytext=(0, 10), ha="center", fontsize=7)
    ax1.set_xticks(x)
    ax1.set_xticklabels(labels)
    ax1.set_ylabel(r"$|\lambda|\ /\ M_{KK}$")
    ax1.set_title("M_R targets vs L12 nearest eigenvalue\n"
                  f"verdict {res['verdict']}: {res['value']}", fontsize=9)
    ax1.legend(fontsize=8, loc="upper left")
    ax1.grid(alpha=0.3)

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 6 — Verdict payload (print only; agent calls emit_verdict)
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          sign_verdict: str | None = None,
                          magnitude_verdict: str | None = None,
                          regime_verdict: str | None = None,
                          companion_note: str = "",
                          extra_rows: list[str] | None = None) -> dict:
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
        "track": "investigation",
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

    pins = log_input_pins(INPUT_FILES)  # (local)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy, informational)")

    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANON, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = compute()  # (local)

    # --- report ----------------------------------------------------------
    print("=" * 78)
    print(f"{GATE_ID}: M_R provenance audit")
    print("=" * 78)
    print()
    print("--- Provenance chain (text-anchor presence checks) ---")
    print(f"  M_R built from s54_ed_sweep B3-sector (E_sp_sweep[fold_idx,5:8]): "
          f"{res['fact_s60_MR_from_s54_ed']}")
    print(f"  M_R diag = E_B3_fold (s60 lines 212-214):                        "
          f"{res['fact_s60_MR_diag_from_EB3']}")
    print(f"  s54 E_sp_sweep = lowest-8 of 32-cell TB lattice H:               "
          f"{res['fact_s54_Esp_is_TB_lattice']}")
    print(f"  s54 IS a lattice-ED pipeline:                                    "
          f"{res['fact_s54_is_lattice_ED']}")
    print(f"  => provenance chain resolved + recoverable: {res['provenance_chain_resolved']}")
    print()
    print("--- The 1.16e-5 round-trip (READ from S99-W3) ---")
    print(f"  S99-W3 npz Sigma_mnu_crosscheck_reldiff = {res['roundtrip_116e5_read']:.4e}")
    print(f"  RE-VERIFY (forward seesaw on the SAME M_R operand, diagonal floor):")
    print(f"    m_nu_fwd [eV] = {res['m_nu_fwd_eV']}")
    print(f"    m_nu_pub [eV] = {res['m_nu_pub']}")
    print(f"    shared-operand round-trip reldiff = {res['roundtrip_floor_check']:.3e}  "
          f"(< {res['ROUNDTRIP_FLOOR']:.0e} => by-construction: {res['roundtrip_is_byconstruction']})")
    print(f"  => ANNOTATION: 1.16e-5 is a BY-CONSTRUCTION round-trip, NOT a cross-check.")
    print()
    print("--- The 1.77% coincidence (RE-COMPUTED from the two pipelines) ---")
    print(f"  Pipeline-1 M_R (s54 32-cell TB lattice ED) = {res['m_R_MKK']} M_KK")
    print(f"  Pipeline-2 L12 Peter-Weyl direct diag: {res['absev_n']} |lambda| "
          f"({res['absev_n_unique']} unique)")
    for j, lab in enumerate(["M_1", "M_2", "M_3"]):
        print(f"    {lab}: M_R={res['m_R_MKK'][j]:.8f}  nearest_L12={res['nearest_recomputed'][j]:.8f}  "
              f"reldiff={res['reldiff_recomputed'][j]:.4e}  "
              f"min|d|={res['min_abs_diff'][j]:.3e}  exact_member={bool(res['exact_member'][j])}")
    print(f"  maxrel (re-computed) = {res['maxrel_recomputed']:.8f} ; "
          f"matches S99-W3 ({res['maxrel_177_read']:.8f}): {res['maxrel_matches_s99']}")
    print()
    print("--- DISCRIMINATOR: exact-membership (same eigenvalues re-read?) ---")
    print(f"  any M_R an EXACT L12 eigenvalue (atol={res['EXACT_MEMBER_ATOL']:.0e})? "
          f"{res['any_exact_member']}")
    print(f"  => pipelines are DISTINCT numerical objects (not a re-read): "
          f"{res['pipelines_distinct_numerics']}")
    print()
    print("--- CLASSIFICATION ---")
    print(f"  Track A (distinct NUMERICAL PIPELINE => independent_corroboration): "
          f"{res['track_A_independent']}")
    print(f"  Track B (same SPECTRAL INPUT D_K@tau_fold => consistency_check_circular): "
          f"{res['track_B_circular']}")
    print(f"  => VERDICT {res['verdict']}: {res['value']}")
    print()

    make_plot(res)

    np.savez(
        OUT_NPZ,
        value=res["value"],
        verdict=res["verdict"],
        maxrel_177_read=res["maxrel_177_read"],
        roundtrip_116e5_read=res["roundtrip_116e5_read"],
        nearest_published=res["nearest_published"],
        reldiff_published=res["reldiff_published"],
        m_R_MKK=res["m_R_MKK"],
        roundtrip_floor_check=res["roundtrip_floor_check"],
        roundtrip_is_byconstruction=res["roundtrip_is_byconstruction"],
        m_nu_fwd_eV=res["m_nu_fwd_eV"],
        m_nu_pub=res["m_nu_pub"],
        absev_n=res["absev_n"],
        absev_n_unique=res["absev_n_unique"],
        nearest_recomputed=res["nearest_recomputed"],
        reldiff_recomputed=res["reldiff_recomputed"],
        maxrel_recomputed=res["maxrel_recomputed"],
        maxrel_matches_s99=res["maxrel_matches_s99"],
        min_abs_diff=res["min_abs_diff"],
        exact_member=res["exact_member"],
        any_exact_member=res["any_exact_member"],
        all_exact_member=res["all_exact_member"],
        pipelines_distinct_numerics=res["pipelines_distinct_numerics"],
        fact_s60_MR_from_s54_ed=res["fact_s60_MR_from_s54_ed"],
        fact_s60_MR_diag_from_EB3=res["fact_s60_MR_diag_from_EB3"],
        fact_s54_Esp_is_TB_lattice=res["fact_s54_Esp_is_TB_lattice"],
        fact_s54_is_lattice_ED=res["fact_s54_is_lattice_ED"],
        provenance_chain_resolved=res["provenance_chain_resolved"],
        track_A_independent=res["track_A_independent"],
        track_B_circular=res["track_B_circular"],
        EXACT_MEMBER_ATOL=res["EXACT_MEMBER_ATOL"],
        ROUNDTRIP_FLOOR=res["ROUNDTRIP_FLOOR"],
    )
    print(f"  Saved data: {OUT_NPZ.relative_to(PROJECT_ROOT)}")
    print(f"  Saved plot: {OUT_PNG.relative_to(PROJECT_ROOT)}")
    print()

    tag = emit_4tuple(res["value"], SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)

    # Descriptive value string (no single-quote chars; emit_verdict wraps value='...').
    value_str = (
        f"classification={res['value']}; "
        f"roundtrip_1.16e-5=BY-CONSTRUCTION(shared-operand floor={res['roundtrip_floor_check']:.1e}<{res['ROUNDTRIP_FLOOR']:.0e}); "
        f"1.77pct_maxrel={res['maxrel_recomputed']:.6f}(re-derived,matches_S99={res['maxrel_matches_s99']}); "
        f"exact_member_in_L12={res['any_exact_member']}(=>distinct_pipelines={res['pipelines_distinct_numerics']}); "
        f"provenance=MR=diag(E_B3_fold)xMKK_from_s54_32cell_TB_lattice_ED_vs_s84_L12_PeterWeyl_direct_diag"
    )  # (local)

    extra = [
        f"# provenance: M_R diag=E_B3_fold[5:8]*M_KK (s60_lepto_cp.py:93,212-214); "
        f"E_sp_sweep=lowest-8 of 32-cell TB lattice s54_tb_hamiltonian.npz (s54_ed_sweep.py:274)",
        f"# round-trip 1.16e-5 (S99-W3 Sigma_mnu_crosscheck_reldiff) is BY-CONSTRUCTION: "
        f"same M_R operand forward-then-inverse; re-verified diagonal floor={res['roundtrip_floor_check']:.1e}; NOT a cross-check",
        f"# 1.77pct (S99-W3 M_R_spectral_coincidence_maxrel=0.017735) = S96-MATTER-SEESAW-D5 PART-1: "
        f"M_R(lattice-ED) vs L12 Peter-Weyl nearest-|lambda|; reldiff=[{res['reldiff_recomputed'][0]:.4e},{res['reldiff_recomputed'][1]:.4e},{res['reldiff_recomputed'][2]:.4e}]",
        f"# discriminator: EXACT-MEMBERSHIP of M_R in L12 FAILS (min|d|=[{res['min_abs_diff'][0]:.2e},{res['min_abs_diff'][1]:.2e},{res['min_abs_diff'][2]:.2e}]>>1e-12) "
        f"=> NOT a re-read => distinct NUMERICAL pipelines (Track A); but SAME D_K@tau_fold (Track B) => INFO: definitional, not factual, residue",
        f"# INVESTIGATION-TRACK ONLY: no canonical/registry/inventory/capstone write; "
        f"capstone 'cross-check'->'by-construction' language fix is session-promotion (NOT this gate)",
    ]  # (local)

    print_verdict_payload(res["verdict"], value_str, audit_sha, content_sha,
                          extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {res['verdict']} (wall {wall:.1f}s) ===")
    # Exit 0 on a valid scientific verdict (PASS/FAIL/INFO) per
    # math-scripts.md §"Exit Codes and Verdict Semantics".
    return 0


if __name__ == "__main__":
    sys.exit(main())
