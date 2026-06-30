#!/usr/bin/env python3
"""
S93 W8-1 — NARROW-PATH-EIGENVALUE-INVENTORY (LQG cluster, Wave 8)
================================================================

Gate: S93-W8-1-NARROW-PATH-EIGENVALUE-INVENTORY ([VERIFY])
Classification: GEOMETRIC

Pre-registered threshold (plan §W8-1):
  PASS iff
    (1) per-sector spinor-bookkeeping identity holds:
        len(abs_evals) == 16*dim(p,q) for ALL populated (p,q)  [mismatch count == 0]
    AND
    (2) total Sigma_sector len(abs_evals) reproduces EXACTLY on re-load  [diff == 0]
    AND
    (3) per-sector min|lambda| is tabulated at rel_tol 1e-9 against the cache's
        stored abs_evals.min().
  FAIL iff the bookkeeping identity fails on any sector OR re-load is non-reproducible.
  INFO iff the identity holds but a sector's stored 'level'/'dim' annotation disagrees
       with p+q / the Weyl dimension formula (usable-with-caveat).

LOAD-BEARING count-convention finding (plan §"Wave 8 Decision Point Prerequisites"):
  The LQG-spec phrase "all 155,984 D_K eigenvalues" cites the s75 f_conv "a_0 = 155,984"
  historical figure (baseline-findings-s66; N_DK_eigenvalues). The CURRENT S84 cache
  restricted to p+q<=10 yields Sigma len(abs_evals) = 78,080 (the s86 N_unique figure),
  NOT 155,984. The two are DISTINCT enumeration conventions; 156,160 = 78,080*2 != 155,984
  (diff 176), so it is not a clean 2x either. This gate therefore PRE-REGISTERS its PASS
  criterion as the cache's OWN internal-integrity cross-check (items 1-3 above), with
  "155,984" recorded as a documented cross-convention ANNOTATION (NOT a gate). A literal
  Sigma == 155984 equality would be a degenerate/false-FAIL count-convention mismatch
  (Class-8.3 publication-precision boundary), NOT a substrate-physics test.

Substrate framing (phononic-framing.md §"IS Space, Not IN Space"):
  The substrate IS the finite spectral triple (A_K, H_K, D_K(tau_fold=0.19)). The D_K
  sqrt(C_2(p,q)) spectrum is PRIMARY (intrinsic to Jensen-deformed SU(3)); the candidate
  LQG sqrt(j(j+1)) SU(2) area-spectrum eigenvalue is the EMERGENT shadow (built DOWNSTREAM
  via W8-2/W8-3). Each PW (p,q) sector is a family of internal-geometry modes weighted by
  the Weyl dimension dim(p,q); per-sector min|lambda| is that sector's lowest-energy mode
  (the substrate's "area-gap" candidate at the (p,q) level). GEOMETRIC: this gate tabulates
  the fabric's spectral content, not its excitations.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz (sector_evals dict)
  - computations/_shared/spectral_action.py (dim_su3_irrep / peter_weyl_degeneracy)
  - computations/_shared/canonical_constants.py (feeds audit_sha256; tau_fold label)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<mismatch_count|PASS-string>,
   scheme=narrow-path-eigenvalue-inventory-PW-sector-tabulation,
   convention=NARROW-PATH-eigenvalue-inventory-spinor-bookkeeping-16xdim-pq-L10-and-L12-dual-scope-155984-cross-convention-ANNOTATED-NOT-GATED,
   L_max=12)

NAME-RESOLUTION NOTE: the plan prose references spectral_action.weyl_dim_su3(p,q); the
  CANONICAL function in spectral_action.py is dim_su3_irrep(p,q) (= peter_weyl_degeneracy).
  Per gate-verdicts.md (plan-text naming a non-existent entity => documentation bug), this
  script uses the canonical dim_su3_irrep; the Weyl dim formula (p+1)(q+1)(p+q+2)/2 is the
  same object the plan's substitution chain Step 1 cites (spectral_action.py:96).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 2 — Standard imports (path setup precedes canonical import)
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths (must precede canonical_constants import)
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

# _shared holds canonical_constants.py AND spectral_action.py; put it on the
# path BEFORE importing either (matches S93 W7-3 precedent lines 66-74).
sys.path.insert(0, str(SHARED_DIR))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import tau_fold  # noqa: E402  explicit tau-slice label
from spectral_action import dim_su3_irrep, peter_weyl_degeneracy  # noqa: E402

SESSION = "S93"                                                       # (local)
GATE_ID = "S93-W8-1-NARROW-PATH-EIGENVALUE-INVENTORY"                 # (local)
SCHEME = "narrow-path-eigenvalue-inventory-PW-sector-tabulation"     # (local)
CONVENTION = (
    "NARROW-PATH-eigenvalue-inventory-spinor-bookkeeping-16xdim-pq-"
    "L10-and-L12-dual-scope-155984-cross-convention-ANNOTATED-NOT-GATED"
)                                                                     # (local)
L_MAX = 12                                                            # (local) cache native ceiling
L_MAX_HISTORICAL = 10                                                 # (local) narrow-path comparison scope

# NCG-fixed internal spinor algebra dimension (16 = N_chiral_components,
# fixed by NCG; s88-w4-w1b1-composite-reading.md). The cache stores the |lambda|
# of V_(p,q) (x) S per sector, dim = dim(p,q)*16.
N_SPINOR = 16                                                         # (local) NCG-fixed

# Pre-registered tolerances / thresholds (plan §W8-1 strict_PASS_boundary)
MISMATCH_PASS = 0                                                     # (local) exact integer
MINLAMBDA_RELTOL = 1e-9                                               # (local)

# Documented cross-convention figures (ANNOTATIONS, NOT gates)
A0_S75_HISTORICAL = 155984                                           # (local) s75 f_conv a_0; baseline-findings-s66
N_UNIQUE_S86 = 78080                                                # (local) s86 N_unique (L_max=10 len-total)

# Output destinations (per-session, canonical path)
OUT_NPZ = SESSION_DIR / "s93_w8_1_narrow_path_eigenvalue_inventory.npz"
OUT_PNG = SESSION_DIR / "s93_w8_1_narrow_path_eigenvalue_inventory.png"
VERDICT_TXT = SESSION_DIR / "s93_gate_verdicts.txt"

CACHE_PATH = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    CACHE_PATH,
    SHARED_DIR / "spectral_action.py",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema; W9a-99)
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


def compute_dual_sha(
    script_path: Path, canonical_path: Path, pins: dict[str, str]
) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per S84+ dual-SHA schema."""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)

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

def load_sector_evals(path: Path) -> dict:
    """Load the sector_evals dict from the npz cache (object-array scalar)."""
    c = np.load(path, allow_pickle=True)  # (local)
    return c["sector_evals"].item()


def build_inventory(se: dict) -> dict:
    """Tabulate per-sector inventory + run the three PASS checks.

    Returns a dict with the full inventory arrays and the gate-relevant scalars.
    """
    sectors = sorted(se.keys(), key=lambda pq: (pq[0] + pq[1], pq[0]))  # (local)

    p_arr, q_arr, level_arr, dim_arr = [], [], [], []  # (local)
    mult_arr, minlam_arr = [], []  # (local)
    bookkeep_ok_arr = []  # (local)
    level_mismatch = 0  # (local) INFO trigger
    dim_mismatch = 0    # (local) INFO trigger
    mismatch_count = 0  # (local) PASS gate (item 1)

    for (p, q) in sectors:
        rec = se[(p, q)]  # (local)
        dim_stored = int(rec["dim"])          # (local)
        level_stored = int(rec["level"])      # (local)
        abs_evals = np.asarray(rec["abs_evals"], dtype=np.float64)  # (local)
        n_ev = int(len(abs_evals))            # (local)
        dim_formula = int(dim_su3_irrep(p, q))  # (local) canonical Weyl dim
        # peter_weyl_degeneracy(p,q) == dim_su3_irrep(p,q) — sanity self-check
        assert int(peter_weyl_degeneracy(p, q)) == dim_formula

        ok = (n_ev == N_SPINOR * dim_formula)  # (local) spinor-bookkeeping identity
        if not ok:
            mismatch_count += 1
        if dim_stored != dim_formula:
            dim_mismatch += 1
        if level_stored != (p + q):
            level_mismatch += 1

        p_arr.append(p)
        q_arr.append(q)
        level_arr.append(level_stored)
        dim_arr.append(dim_formula)
        mult_arr.append(n_ev)
        minlam_arr.append(float(abs_evals.min()))
        bookkeep_ok_arr.append(bool(ok))

    p_arr = np.array(p_arr, dtype=np.int64)            # (local)
    q_arr = np.array(q_arr, dtype=np.int64)            # (local)
    level_arr = np.array(level_arr, dtype=np.int64)    # (local)
    dim_arr = np.array(dim_arr, dtype=np.int64)        # (local)
    mult_arr = np.array(mult_arr, dtype=np.int64)      # (local)
    minlam_arr = np.array(minlam_arr, dtype=np.float64)  # (local)
    bookkeep_ok_arr = np.array(bookkeep_ok_arr, dtype=bool)  # (local)

    mask_L10 = level_arr <= L_MAX_HISTORICAL  # (local)

    # Totals — dim^1 convention (cache len(abs_evals) sum = N_unique)
    total_len_L12 = int(mult_arr.sum())                    # (local)
    total_len_L10 = int(mult_arr[mask_L10].sum())          # (local)
    n_sec_L12 = int(len(sectors))                          # (local)
    n_sec_L10 = int(mask_L10.sum())                        # (local)
    # excluding (0,0)
    mult_00 = int(mult_arr[(p_arr == 0) & (q_arr == 0)][0])  # (local)
    total_len_L10_no00 = total_len_L10 - mult_00            # (local)
    total_len_L12_no00 = total_len_L12 - mult_00            # (local)

    # dim^2 convention (s75-style a_0 = 16 * sum dim^2) — recorded for annotation
    a0_dim2_L10 = int(N_SPINOR * int((dim_arr[mask_L10] ** 2).sum()))  # (local)
    a0_dim2_L12 = int(N_SPINOR * int((dim_arr ** 2).sum()))            # (local)

    return {
        "sectors": sectors,
        "p_arr": p_arr,
        "q_arr": q_arr,
        "level_arr": level_arr,
        "dim_arr": dim_arr,
        "mult_arr": mult_arr,
        "minlam_arr": minlam_arr,
        "bookkeep_ok_arr": bookkeep_ok_arr,
        "mask_L10": mask_L10,
        "mismatch_count": mismatch_count,
        "dim_mismatch": dim_mismatch,
        "level_mismatch": level_mismatch,
        "total_len_L12": total_len_L12,
        "total_len_L10": total_len_L10,
        "total_len_L10_no00": total_len_L10_no00,
        "total_len_L12_no00": total_len_L12_no00,
        "n_sec_L12": n_sec_L12,
        "n_sec_L10": n_sec_L10,
        "a0_dim2_L10": a0_dim2_L10,
        "a0_dim2_L12": a0_dim2_L12,
    }


def compute() -> dict:
    # First-pass load + inventory
    se1 = load_sector_evals(CACHE_PATH)  # (local)
    inv = build_inventory(se1)           # (local)

    # Item-2: re-load reproduction (independent second load, bit-for-bit total)
    se2 = load_sector_evals(CACHE_PATH)  # (local)
    total_reloaded = int(
        sum(len(np.asarray(se2[k]["abs_evals"])) for k in se2)
    )  # (local)
    reload_diff = abs(total_reloaded - inv["total_len_L12"])  # (local)
    reload_exact = (reload_diff == 0)  # (local)

    # Item-3: per-sector min|lambda| reproduction at rel_tol (re-min from se2)
    minlam_reload = np.array(
        [float(np.asarray(se2[(int(p), int(q))]["abs_evals"]).min())
         for p, q in zip(inv["p_arr"], inv["q_arr"])],
        dtype=np.float64,
    )  # (local)
    rel_err = np.abs(minlam_reload - inv["minlam_arr"]) / np.maximum(
        np.abs(inv["minlam_arr"]), 1e-300
    )  # (local)
    max_minlam_relerr = float(rel_err.max())  # (local)
    minlam_reproduced = bool(max_minlam_relerr <= MINLAMBDA_RELTOL)  # (local)

    inv["total_reloaded"] = total_reloaded
    inv["reload_diff"] = reload_diff
    inv["reload_exact"] = reload_exact
    inv["max_minlam_relerr"] = max_minlam_relerr
    inv["minlam_reproduced"] = minlam_reproduced

    # The reported "value" is the spinor-bookkeeping mismatch count (PASS at 0).
    inv["value"] = inv["mismatch_count"]
    return inv


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple
# ---------------------------------------------------------------------------

def evaluate_gate(inv: dict) -> str:
    """PASS iff (mismatch==0) AND (reload exact) AND (min|lambda| reproduced).
    INFO iff bookkeeping holds + reload exact + min reproduced BUT a stored
    level/dim annotation disagrees. FAIL otherwise.
    """
    core_pass = (
        inv["mismatch_count"] == MISMATCH_PASS
        and inv["reload_exact"]
        and inv["minlam_reproduced"]
    )  # (local)
    if not core_pass:
        return "FAIL"
    if inv["dim_mismatch"] > 0 or inv["level_mismatch"] > 0:
        return "INFO"
    return "PASS"


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    """Atomic append: canonical line + dual-SHA companion comment row (W9a-99).
    [VERIFY] trigger => NO schema-v2 3-tuple row (plan: schema_v2_3tuple_required false).
    """
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------

def make_plot(inv: dict) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.2))  # (local)

    # Panel A: per-sector multiplicity len(abs_evals) vs 16*dim(p,q) (identity line)
    ax = axes[0]  # (local)
    pred = N_SPINOR * inv["dim_arr"]  # (local)
    ax.scatter(pred, inv["mult_arr"], s=18, c=inv["level_arr"], cmap="viridis",
               zorder=3, label="sectors (color = level p+q)")
    lim = [0, float(pred.max()) * 1.05]  # (local)
    ax.plot(lim, lim, "r--", lw=1.0, zorder=2,
            label="identity: len = 16·dim(p,q)")
    ax.set_xlabel("16 · dim(p,q)  [predicted block size]")
    ax.set_ylabel("len(abs_evals)  [cache multiplicity]")
    ax.set_title(f"W8-1 spinor-bookkeeping identity\n"
                 f"mismatch count = {inv['mismatch_count']} (PASS at 0); "
                 f"{inv['n_sec_L12']} sectors L≤12")
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(alpha=0.3)

    # Panel B: per-sector min|lambda| vs level (the substrate area-gap candidate)
    ax = axes[1]  # (local)
    mask10 = inv["mask_L10"]  # (local)
    ax.scatter(inv["level_arr"][mask10], inv["minlam_arr"][mask10], s=22,
               c="C0", zorder=3, label=f"L≤10 ({inv['n_sec_L10']} sectors)")
    ax.scatter(inv["level_arr"][~mask10], inv["minlam_arr"][~mask10], s=22,
               c="C3", marker="^", zorder=3,
               label=f"11≤L≤12 ({inv['n_sec_L12']-inv['n_sec_L10']} sectors)")
    ax.set_xlabel("level  p+q")
    ax.set_ylabel("per-sector min |λ|  [M_KK units]")
    ax.set_title("W8-1 per-sector lowest mode (area-gap candidate)\n"
                 "substrate IS primary; LQG √(j(j+1)) is emergent shadow")
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(alpha=0.3)

    fig.suptitle(
        f"S93-W8-1 NARROW-PATH eigenvalue inventory (τ_fold={tau_fold}) | "
        f"Σlen(L≤10)={inv['total_len_L10']:,} (=s86 N_unique 78,080); "
        f"a₀(s75)=155,984 cross-convention ANNOTATED, NOT gated",
        fontsize=10,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    inv = compute()  # (local)
    verdict = evaluate_gate(inv)  # (local)

    # --- Report (NUMBERS first) ---
    print("=== W8-1 inventory (PASS checks) ===")
    print(f"  spinor-bookkeeping mismatch count : {inv['mismatch_count']} "
          f"(PASS at {MISMATCH_PASS})")
    print(f"  dim-annotation mismatch count     : {inv['dim_mismatch']}")
    print(f"  level-annotation mismatch count   : {inv['level_mismatch']}")
    print(f"  re-load total (pass1/pass2)       : {inv['total_len_L12']} / "
          f"{inv['total_reloaded']} | diff={inv['reload_diff']} | "
          f"exact={inv['reload_exact']}")
    print(f"  max per-sector min|λ| rel-err     : {inv['max_minlam_relerr']:.2e} "
          f"(reltol {MINLAMBDA_RELTOL:.0e}; reproduced={inv['minlam_reproduced']})")
    print()
    print("=== dim^1 convention (cache len(abs_evals) = N_unique) ===")
    print(f"  L_max=12: Σ len = {inv['total_len_L12']:,}  | {inv['n_sec_L12']} sectors "
          f"| excl(0,0) = {inv['total_len_L12_no00']:,}")
    print(f"  L_max=10: Σ len = {inv['total_len_L10']:,}  | {inv['n_sec_L10']} sectors "
          f"| excl(0,0) = {inv['total_len_L10_no00']:,}")
    print(f"  L_max=10 total vs s86 N_unique 78,080 : "
          f"match={inv['total_len_L10'] == N_UNIQUE_S86}")
    print()
    print("=== cross-convention annotation (NOT gated) ===")
    print(f"  s75 f_conv a_0 (baseline-findings-s66) = {A0_S75_HISTORICAL:,}")
    print(f"  16·Σdim²(L≤10) [dim^2 convention]      = {inv['a0_dim2_L10']:,}")
    print(f"  16·Σdim²(L≤12) [dim^2 convention]      = {inv['a0_dim2_L12']:,}")
    print(f"  155,984 == Σlen(L10)=78,080 ?          {A0_S75_HISTORICAL == inv['total_len_L10']}")
    print(f"  155,984 == 2·78,080=156,160 ?          "
          f"{A0_S75_HISTORICAL == 2 * inv['total_len_L10']} "
          f"(diff {2 * inv['total_len_L10'] - A0_S75_HISTORICAL})")
    print(f"  155,984 == 16·Σdim²(L10) ?             {A0_S75_HISTORICAL == inv['a0_dim2_L10']}")
    print("  => 155,984 is a DISTINCT historical enumeration convention; ANNOTATED, NOT gated.")
    print()

    # --- Persist npz ---
    np.savez(
        OUT_NPZ,
        p=inv["p_arr"],
        q=inv["q_arr"],
        level=inv["level_arr"],
        dim_pq=inv["dim_arr"],
        multiplicity=inv["mult_arr"],
        min_abs_lambda=inv["minlam_arr"],
        bookkeep_ok=inv["bookkeep_ok_arr"],
        mask_L10=inv["mask_L10"],
        mismatch_count=np.int64(inv["mismatch_count"]),
        dim_mismatch=np.int64(inv["dim_mismatch"]),
        level_mismatch=np.int64(inv["level_mismatch"]),
        total_len_L12=np.int64(inv["total_len_L12"]),
        total_len_L10=np.int64(inv["total_len_L10"]),
        total_len_L10_no00=np.int64(inv["total_len_L10_no00"]),
        total_len_L12_no00=np.int64(inv["total_len_L12_no00"]),
        total_reloaded=np.int64(inv["total_reloaded"]),
        reload_diff=np.int64(inv["reload_diff"]),
        reload_exact=np.bool_(inv["reload_exact"]),
        max_minlam_relerr=np.float64(inv["max_minlam_relerr"]),
        minlam_reproduced=np.bool_(inv["minlam_reproduced"]),
        n_sec_L12=np.int64(inv["n_sec_L12"]),
        n_sec_L10=np.int64(inv["n_sec_L10"]),
        a0_dim2_L10=np.int64(inv["a0_dim2_L10"]),
        a0_dim2_L12=np.int64(inv["a0_dim2_L12"]),
        N_SPINOR=np.int64(N_SPINOR),
        a0_s75_historical=np.int64(A0_S75_HISTORICAL),
        n_unique_s86=np.int64(N_UNIQUE_S86),
        tau_fold=np.float64(tau_fold),
        verdict=np.str_(verdict),
    )
    make_plot(inv)

    tag = emit_4tuple(inv["value"], SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)
    append_verdict(verdict, inv["value"], audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    # Verdict is DATA, not exit code (math-scripts.md §Exit Codes): exit 0 on a
    # valid scientific verdict regardless of PASS/FAIL/INFO.
    return 0


if __name__ == "__main__":
    sys.exit(main())
