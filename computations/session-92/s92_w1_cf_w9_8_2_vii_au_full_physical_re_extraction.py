"""
s92_w1_cf_w9_8_2_vii_au_full_physical_re_extraction.py
========================================================

S92-W1-CF-W9-8-2-VII-AU-FULL-PHYSICAL-RE-EXTRACTION

Re-extract the §VII.AU.OP-PROJ canonical Level-3 anchor at FULL-physical
CC1996 §2.2-2.3 Pauli-Villars regulator class on L_max ∈ {12, 14} at
substrate-distance-1 pole s=3; Friedrich-Bär saturation analog at the
FULL-CC class.

Pre-registered PASS:
    rel_drift = |rho_FULL(s=3, L=14) - rho_FULL(s=3, L=12)| / |rho_FULL(s=3, L=12)|
             < 1e-3                            (Friedrich-Bär saturation)
INFO band:     1e-3 <= rel_drift < 1e-2
FAIL band:     rel_drift >= 1e-2

On PASS the saturated value rho_FULL_CC_VII_AU_SAT(s=3) is promoted to
canonical_constants.py via update_constant() (canonical-write-order Step 2
of `math-scripts.md §"Canonical Write-Order for New Framework Predictions"`).

Option A supersedes-tag protocol: the corrective verdict line carries
    supersedes=0da19aba653fa19ddf7bf2178581ec5c767c115e4508dd6e92906e68e6875e1f
(full 64-char audit_sha256 of S91-W1-14-COMPOSITE-BRIDGE-MAP-RDX line 221
in s91_gate_verdicts.txt) per `v3-closure-recovery.md` sig_5 remediation +
`gate-verdicts.md §"Option A — sig_5 remediation pathway"`.

Convention discipline:
    scheme     = full-cc1996-2-2-2-3-pauli-villars-physical-multipliers-friedrich-baer-saturation-Lmax-12-14
    convention = VII-AU-OP-PROJ-FULL-CC-MULTIPLIERS-PHYSICAL-substrate-distance-1-pole-s3-Lmax-12-14-friedrich-baer-saturation
    NO `-SCHEMATIC` suffix (CLASS=FULL via `_pauli_villars_subtraction.py`
    PRIMARY helper; substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY
    level-pin discipline; companion row carries LEVEL_CLASS_PIN=FULL +
    MACHINERY_SCOPE_PIN=CACHE-PROJECTION + BINDING_AXIS_PIN=substrate-natural-binding).

Substrate framing: the substrate IS the spectral triple (A_K, H_K, D_K) at
tau_fold = 0.19; the §VII.AU.OP-PROJ Level-3 anchor IS the substrate's
intrinsic Hochschild-pairing image at substrate-distance-1 pole s=3 evaluated
at finite L_max truncation of (A_K, H_K, D_K). The L_max=12 and L_max=14
FULL-CC evaluations are TWO methodology-floor F-images of the SAME substrate-IS
canonical at the SAME pole on the SAME spectral triple.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Path discipline (project root contains space — use absolute paths)
# -----------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
ROOT_COMPUTATIONS = PROJECT_ROOT / "computations"

sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(ROOT_COMPUTATIONS))

# -----------------------------------------------------------------------------
# Canonical constants (MANDATORY: never hardcode framework constants)
# -----------------------------------------------------------------------------
from canonical_constants import (  # noqa: E402
    tau_fold,
    alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC,
    alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22,
)

# -----------------------------------------------------------------------------
# FULL-CC Pauli-Villars helper (PRIMARY; CC1996 §2.2-2.3 2-point multiplier)
# -----------------------------------------------------------------------------
import _pauli_villars_subtraction  # noqa: E402
from _pauli_villars_subtraction import (  # noqa: E402
    PV_PRIMARY_C,
    PV_PRIMARY_M_DIMLESS,
    pv_multiplier_primary,
    pv_mellin_moment_primary,
    bare_mellin_moment,
    _verify_pv_identities,
)

# -----------------------------------------------------------------------------
# Gate identity + machinery pins (per plan §W1-2 R3 YAML, lines 339-670)
# -----------------------------------------------------------------------------
GATE_ID = "S92-W1-CF-W9-8-2-VII-AU-FULL-PHYSICAL-RE-EXTRACTION"
SCHEME = (
    "full-cc1996-2-2-2-3-pauli-villars-physical-multipliers-"
    "friedrich-baer-saturation-Lmax-12-14"
)
CONVENTION = (
    "VII-AU-OP-PROJ-FULL-CC-MULTIPLIERS-PHYSICAL-"
    "substrate-distance-1-pole-s3-Lmax-12-14-friedrich-baer-saturation"
)
L_MAX_PAIR = (12, 14)
S_POLE = 3  # (local) substrate-distance-1 pole; gate-block PIN per plan §W1-2

# Option A supersedes-tag (full 64-char audit_sha256 from S91-W1-14)
SUPERSEDES_TARGET = "0da19aba653fa19ddf7bf2178581ec5c767c115e4508dd6e92906e68e6875e1f"

# Pre-registered PASS/INFO/FAIL bands (gate-block PIN MAP per plan §W1-2)
PASS_THRESHOLD = 1e-3   # (local) rel_drift < 1e-3 → PASS (Friedrich-Bär saturation)
INFO_TOL_UPPER = 1e-2   # (local) 1e-3 ≤ rel_drift < 1e-2 → INFO (marginal)
# rel_drift ≥ 1e-2 → FAIL (saturation does NOT extend to FULL-CC)

# -----------------------------------------------------------------------------
# Verdict file path (created on first append per `append_verdict`)
# -----------------------------------------------------------------------------
VERDICT_TXT = PROJECT_ROOT / "computations" / "session-92" / "s92_gate_verdicts.txt"

# -----------------------------------------------------------------------------
# Input files (sha256 computed at runtime per gate-block input_files)
# -----------------------------------------------------------------------------
SCRIPT_PATH = Path(__file__).resolve()
CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
CACHE_L12 = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CACHE_L14 = PROJECT_ROOT / "computations" / "session-87" / "s87_spectrum_cache_L14_tau019.npz"
PV_HELPER_PATH = PROJECT_ROOT / "computations" / "_pauli_villars_subtraction.py"
S91_VERDICTS_PATH = PROJECT_ROOT / "computations" / "session-91" / "s91_gate_verdicts.txt"
PERMANENT_REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
SUBSTRATE_FIRST_RULE_PATH = PROJECT_ROOT / ".claude" / "rules" / "substrate-first-canonical-sourcing.md"
MATH_SCRIPTS_RULE_PATH = PROJECT_ROOT / ".claude" / "rules" / "math-scripts.md"

OUT_NPZ = PROJECT_ROOT / "computations" / "session-92" / "s92_w1_cf_w9_8_2_vii_au_full_physical_re_extraction.npz"
OUT_PNG = PROJECT_ROOT / "computations" / "session-92" / "s92_w1_cf_w9_8_2_vii_au_full_physical_re_extraction.png"


# -----------------------------------------------------------------------------
# SHA helpers (per `_script_template.py` `closure_hash` / `compute_dual_sha`)
# -----------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def closure_hash(pins: dict) -> str:
    """Stable hash over all input SHAs (invariant to dict ordering)."""
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                    pins: dict) -> tuple[str, str]:
    """Compute (audit_sha256, content_sha256) per S84+ dual-SHA schema.

    audit_sha256 = sha256(script || canonical_constants || pinmap_json)
    content_sha256 = sha256(script)
    """
    script_bytes = b""
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
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


# -----------------------------------------------------------------------------
# Verdict-line emitter (atomic append; createsf file on first write)
# -----------------------------------------------------------------------------
def append_verdict(verdict: str, value: str,
                   audit_sha: str, content_sha: str) -> None:
    """Append a single-line verdict to s92_gate_verdicts.txt.

    Schema S87+: canonical line + supersedes= tag (Option A) + dual-SHA
    companion comment row + LEVEL_CLASS / MACHINERY_SCOPE / BINDING_AXIS
    pin rows.
    """
    # Make sure the file's parent dir exists (already does, but be safe)
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)

    # Canonical line: value carries supersedes= tag per Option A
    value_with_supersedes = f"{value}_supersedes={SUPERSEDES_TARGET}"
    line = (
        f"{GATE_ID}: {verdict} -- value='{value_with_supersedes}' "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max=12_14 "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )

    # Dual-SHA companion comment row (W9a-99 split: short heads)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"supersedes={SUPERSEDES_TARGET}\n"
    )

    # Level-pin / machinery-scope / binding-axis discipline rows
    level_pin = (
        f"# LEVEL_CLASS_PIN=FULL "
        f"# {GATE_ID} substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY "
        f"level-pin compliance (consumes _pauli_villars_subtraction.py PRIMARY "
        f"helper; FULL physical CC1996 §2.2-2.3 2-point PV multipliers; "
        f"NO -SCHEMATIC suffix)\n"
    )
    machinery_scope_pin = (
        f"# MACHINERY_SCOPE_PIN=CACHE-PROJECTION "
        f"# {GATE_ID} regulator-pin-discipline.md MACHINERY-SCOPE axis "
        f"(cache-projection-truncated observable on L_max=12 + L_max=14 master caches; "
        f"NOT full-leaf-foliation)\n"
    )
    binding_axis_pin = (
        f"# BINDING_AXIS_PIN=substrate-natural-binding "
        f"# {GATE_ID} regulator-pin-discipline.md Binding-axis "
        f"(substrate's own Hochschild-pairing image at §VII.AU.OP-PROJ slot; "
        f"NOT canonical-import binding)\n"
    )

    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
        fp.write(level_pin)
        fp.write(machinery_scope_pin)
        fp.write(binding_axis_pin)


# -----------------------------------------------------------------------------
# Spectrum cache loader
# -----------------------------------------------------------------------------
def load_spectrum_flat(cache_path: Path) -> tuple[np.ndarray, np.ndarray, int, int]:
    """Load Peter-Weyl sectored cache, flatten to (lambdas, mults) per S90 CF-61 pattern.

    Each (p,q) sector contributes dim(p,q) copies of each eigenvalue (Peter-Weyl
    multiplicity weighting baked in). For sector_evals[(p,q)] = {'dim': D, 'level': l,
    'abs_evals': [|λ_1|, ..., |λ_{16*D}|]}, each |λ_k| in the abs_evals array carries
    multiplicity D (the irrep dimension) in the Mellin moment sum
        M(s) = Σ_k m_k · |λ_k|^{-2s}
    where m_k = dim(p,q) for k in sector (p,q).
    """
    cache = np.load(cache_path, allow_pickle=True)
    sector_evals = cache["sector_evals"].item()
    lambdas_list = []  # (local)
    mults_list = []  # (local)
    n_sectors = 0  # (local)
    max_level = 0  # (local)
    for (p, q), info in sector_evals.items():
        n_sectors += 1
        dim = int(info["dim"])  # (local)
        level = int(info["level"])  # (local)
        if level > max_level:
            max_level = level
        evals_arr = np.asarray(info["abs_evals"], dtype=np.float64)
        for v in evals_arr:
            lambdas_list.append(float(v))
            mults_list.append(float(dim))
    lambdas = np.array(lambdas_list, dtype=np.float64)
    mults = np.array(mults_list, dtype=np.float64)
    return lambdas, mults, n_sectors, max_level


# -----------------------------------------------------------------------------
# tau-field consistency check (cache must be at tau_fold = 0.19)
# -----------------------------------------------------------------------------
def verify_tau_field(cache_path: Path) -> bool:
    """Cache filename embeds tau019 → corresponds to tau_fold = 0.19 by S84 convention.

    The cache npz format used here (sector_evals only) does NOT carry a 'tau' field
    explicitly; the canonical pin is in the filename. We sanity-check via the
    canonical_constants.py tau_fold value and the filename convention.
    """
    return "tau019" in cache_path.name and abs(tau_fold - 0.19) < 1e-6


# -----------------------------------------------------------------------------
# Mellin moment evaluation at substrate-distance-1 pole s=3 (FULL-CC PV)
# -----------------------------------------------------------------------------
def evaluate_rho_FULL(s_pole: float, lambdas: np.ndarray,
                      mults: np.ndarray) -> tuple[float, float, float, dict]:
    """Compute M_FULL(s=s_pole, L_max), M_BARE(s=s_pole, L_max), and ρ_FULL = M_FULL / M_BARE.

    Definitions (per plan substitution chain Step 1-5):
        M_FULL(s=3) = Σ_k m_k · w_PV(λ_k²; s=3) · λ_k^{-6}   (s=3, λ^{-2s} = λ^{-6})
        M_BARE(s=3) = Σ_k m_k · λ_k^{-6}
        w_PV(λ²; s) = 1 - Σ_{r=1..2} c_r · (m_r²/(λ²+m_r²))^s,   {c_r, m_r} per CC1996 §2.2-2.3
        ρ_FULL(s=3) = M_FULL(s=3) / M_BARE(s=3)

    Diagnostics returned:
        - w_PV statistics across the spectrum (min/mean/max)
        - PV identity cross-checks (Σ c_r = 1, Σ c_r·m_r² = 0)
    """
    M_FULL = pv_mellin_moment_primary(s_pole, lambdas, mults,
                                       c_arr=PV_PRIMARY_C,
                                       m_arr=PV_PRIMARY_M_DIMLESS)  # (local)
    M_BARE = bare_mellin_moment(s_pole, lambdas, mults)  # (local)

    rho_FULL = M_FULL / M_BARE  # (local)

    lam2 = lambdas * lambdas  # (local)
    w_PV = pv_multiplier_primary(lam2, s_pole,
                                  c_arr=PV_PRIMARY_C,
                                  m_arr=PV_PRIMARY_M_DIMLESS)  # (local)

    diagnostics = {
        "M_FULL_s3": M_FULL,
        "M_BARE_s3": M_BARE,
        "w_PV_min": float(np.min(w_PV)),
        "w_PV_max": float(np.max(w_PV)),
        "w_PV_mean": float(np.mean(w_PV)),
        "w_PV_std": float(np.std(w_PV)),
        "lambda_min": float(np.min(lambdas)),
        "lambda_max": float(np.max(lambdas)),
        "N_eigenvalues_raw": int(len(lambdas)),
        "N_weighted": float(np.sum(mults)),
    }

    return rho_FULL, M_FULL, M_BARE, diagnostics


# -----------------------------------------------------------------------------
# Friedrich-Bär NEW-sector intrusion margin diagnostic (W11-3 precedent)
# -----------------------------------------------------------------------------
def friedrich_baer_intrusion_diagnostic(cache12_path: Path,
                                         cache14_path: Path,
                                         s_pole: float) -> dict:
    """Per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection
    Feasibility Pre-Check"` Friedrich-Bär saturation theorem.

    For each Peter-Weyl sector (p,q) at L_max ∈ {13, 14} (NEW sectors not in
    L_max=12 cache), the per-sector Mellin contribution at pole s=3 is
        m_(p,q) · λ^{-6}
    where m_(p,q) = irrep dim and λ_min ≥ η_FB · √(C_2(p,q)+1) per W11-3.

    Diagnostic: report the (p+q ∈ {13, 14}) sector contributions and verify
    they constitute < 1e-3 of the s=3 Mellin total. This justifies Friedrich-Bär
    saturation analytically for the FULL-CC class at substrate-distance-1 pole.
    """
    cache12 = np.load(cache12_path, allow_pickle=True)
    sd12 = cache12["sector_evals"].item()
    cache14 = np.load(cache14_path, allow_pickle=True)
    sd14 = cache14["sector_evals"].item()

    # Sectors in L_max=14 not in L_max=12 (i.e., p+q ∈ {13, 14})
    new_sectors = {k: v for k, v in sd14.items() if k not in sd12}

    # Compute M_BARE_full_L14 (total at L_max=14)
    lambdas14, mults14, n_sec_14, max_lev_14 = load_spectrum_flat(cache14_path)
    M_BARE_L14 = bare_mellin_moment(s_pole, lambdas14, mults14)  # (local)

    # Compute contribution from NEW sectors (p+q ∈ {13, 14})
    new_lambdas = []  # (local)
    new_mults = []  # (local)
    new_levels = []  # (local)
    for (p, q), info in new_sectors.items():
        dim = int(info["dim"])  # (local)
        level = int(info["level"])  # (local)
        new_levels.append(level)
        evals_arr = np.asarray(info["abs_evals"], dtype=np.float64)
        for v in evals_arr:
            new_lambdas.append(float(v))
            new_mults.append(float(dim))
    new_lambdas = np.array(new_lambdas, dtype=np.float64)  # noqa: PLW2901
    new_mults = np.array(new_mults, dtype=np.float64)  # noqa: PLW2901

    if len(new_lambdas) > 0:
        M_BARE_new = bare_mellin_moment(s_pole, new_lambdas, new_mults)  # (local)
        intrusion_ratio = float(M_BARE_new) / float(M_BARE_L14)  # (local)
        # Levels present in NEW sectors
        unique_new_levels = sorted(set(new_levels))  # (local)
    else:
        M_BARE_new = 0.0  # (local) sentinel: no NEW sectors at L_max=14 vs L_max=12
        intrusion_ratio = 0.0  # (local) sentinel; no NEW-sector intrusion to evaluate
        unique_new_levels = []

    # Estimate η_FB_lower (Friedrich-Bär ratio lower bound) on the empirical cache
    eta_FB_per_sector = {}  # (local)
    for (p, q), info in sd12.items():
        evals_arr = np.asarray(info["abs_evals"], dtype=np.float64)
        if len(evals_arr) == 0:
            continue
        lambda_min_pq = float(np.min(evals_arr))  # (local)
        # SU(3) Casimir C_2(p,q) = (1/3) * (p² + q² + p*q + 3*p + 3*q)
        C2 = (1.0 / 3.0) * (p * p + q * q + p * q + 3.0 * p + 3.0 * q)  # (local)
        eta_FB_per_sector[(p, q)] = lambda_min_pq / np.sqrt(C2 + 1.0)
    eta_FB_lower_emp = float(np.min(list(eta_FB_per_sector.values())))  # (local)

    return {
        "M_BARE_L14_full": float(M_BARE_L14),
        "M_BARE_new_sectors_L13_L14": float(M_BARE_new),
        "new_sector_intrusion_ratio": intrusion_ratio,
        "intrusion_ratio_below_1e-3": bool(intrusion_ratio < 1e-3),
        "n_new_sectors": int(len(new_sectors)),
        "unique_new_levels": list(unique_new_levels),
        "eta_FB_lower_empirical_L12": eta_FB_lower_emp,
    }


# -----------------------------------------------------------------------------
# Verdict evaluation (PRE-REGISTERED bands)
# -----------------------------------------------------------------------------
def evaluate_gate(rel_drift: float) -> tuple[str, str, str, str]:
    """Pre-registered 3-band rubric.

    PASS  : rel_drift < 1e-3                  → Friedrich-Bär saturated
    INFO  : 1e-3 ≤ rel_drift < 1e-2           → marginal; PINNABLE-with-caveat
    FAIL  : rel_drift ≥ 1e-2                  → saturation does NOT extend
    """
    abs_drift = abs(rel_drift)  # (local)
    if abs_drift < PASS_THRESHOLD:
        return "PASS", "PASS", "PASS", "VALID"
    elif abs_drift < INFO_TOL_UPPER:
        return "INFO", "PASS", "INFO", "MARGINAL"
    else:
        return "FAIL", "FAIL", "FAIL", "VALID"


# -----------------------------------------------------------------------------
# Diagnostic plot
# -----------------------------------------------------------------------------
def make_plot(rho_FULL_L12: float, rho_FULL_L14: float, rel_drift: float,
              M_FULL_L12: float, M_BARE_L12: float,
              M_FULL_L14: float, M_BARE_L14: float,
              w_PV_stats_L12: dict, w_PV_stats_L14: dict,
              intrusion_diag: dict) -> None:
    """Three-panel diagnostic plot:
        (1) ρ_FULL(s=3) at L_max=12 vs L_max=14 + saturation thresholds
        (2) M_FULL and M_BARE at both L_max (log scale)
        (3) PV multiplier statistics (w_PV_mean) and NEW-sector intrusion
    """
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    # Panel 1: rho_FULL at L=12 vs L=14
    ax1 = axes[0]
    Ls = [12, 14]
    rhos = [rho_FULL_L12, rho_FULL_L14]
    ax1.plot(Ls, rhos, marker="o", linewidth=2.5, markersize=10,
             color="darkorange", label=r"$\rho_{FULL}(s=3, L_{max})$")
    ax1.set_xlabel(r"$L_{max}$ truncation", fontsize=11)
    ax1.set_ylabel(r"$\rho_{FULL}(s=3) = M_{FULL}/M_{BARE}$", fontsize=11)
    ax1.set_title(
        f"§VII.AU.OP-PROJ FULL-CC PV at s={S_POLE}\n"
        f"L_max=12: {rho_FULL_L12:.10f}\n"
        f"L_max=14: {rho_FULL_L14:.10f}\n"
        f"rel_drift = {rel_drift:.4e}    "
        f"(PASS<{PASS_THRESHOLD:.0e}, INFO<{INFO_TOL_UPPER:.0e})",
        fontsize=10,
    )
    ax1.set_xticks(Ls)
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=10)

    # Panel 2: M_FULL and M_BARE at both L_max (log scale)
    ax2 = axes[1]
    x = np.arange(2)  # (local)
    width = 0.35  # (local)
    ax2.bar(x - width / 2, [M_BARE_L12, M_BARE_L14], width=width,
            label=r"$M_{BARE}(s=3)$", color="steelblue", edgecolor="black")
    ax2.bar(x + width / 2, [M_FULL_L12, M_FULL_L14], width=width,
            label=r"$M_{FULL}(s=3)$", color="darkorange", edgecolor="black")
    ax2.set_xticks(x)
    ax2.set_xticklabels(["L_max=12", "L_max=14"])
    ax2.set_yscale("log")
    ax2.set_ylabel(r"Mellin moment at $s=3$ (log scale)", fontsize=11)
    ax2.set_title(
        f"Mellin moments BARE vs FULL CC (substrate-distance-1, s=3)\n"
        f"L_max=12: N_eig={w_PV_stats_L12['N_eigenvalues_raw']}\n"
        f"L_max=14: N_eig={w_PV_stats_L14['N_eigenvalues_raw']}",
        fontsize=10,
    )
    ax2.legend(fontsize=10)
    ax2.grid(True, axis="y", alpha=0.3)

    # Panel 3: PV multiplier statistics + intrusion diagnostic
    ax3 = axes[2]
    cats = ["w_PV_mean\n(L=12)", "w_PV_mean\n(L=14)", "intrusion\nratio (L=14 NEW)"]
    vals = [w_PV_stats_L12["w_PV_mean"], w_PV_stats_L14["w_PV_mean"],
            intrusion_diag["new_sector_intrusion_ratio"]]
    colors = ["steelblue", "darkorange", "purple"]
    ax3.bar(cats, vals, color=colors, edgecolor="black")
    ax3.axhline(PASS_THRESHOLD, color="green", linestyle="--", linewidth=1.5,
                label=f"PASS threshold ({PASS_THRESHOLD:.0e})")
    ax3.set_ylabel("value (linear scale)", fontsize=11)
    ax3.set_title(
        f"PV multiplier statistics + Friedrich-Bär NEW-sector intrusion\n"
        f"NEW sectors (p+q ∈ {{13, 14}}): {intrusion_diag['n_new_sectors']}\n"
        f"η_FB_emp ≥ {intrusion_diag['eta_FB_lower_empirical_L12']:.4f} (W11-3 lower bound)",
        fontsize=10,
    )
    ax3.legend(fontsize=9)
    ax3.grid(True, axis="y", alpha=0.3)

    plt.suptitle(
        f"{GATE_ID}\n"
        f"Friedrich-Bär saturation at FULL-CC PV class on §VII.AU.OP-PROJ "
        f"at substrate-distance-1 pole s={S_POLE}",
        fontsize=12, y=1.02,
    )
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=120, bbox_inches="tight")
    plt.close()


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main() -> int:
    print(f"=== {GATE_ID} ===")
    print(f"Pole s = {S_POLE} (substrate-distance-1)")
    print(f"L_max pair = {L_MAX_PAIR}")
    print(f"PASS threshold (rel_drift < ) = {PASS_THRESHOLD}")
    print(f"INFO band upper bound = {INFO_TOL_UPPER}")

    # 1) Input pins (sha256_of for each input file)
    pins = {
        "computations/_shared/canonical_constants.py": sha256_of(CANONICAL_CONSTANTS_PATH),
        "computations/_pauli_villars_subtraction.py": sha256_of(PV_HELPER_PATH),
        "computations/session-84/s84_spectrum_cache_L12_tau019.npz": sha256_of(CACHE_L12),
        "computations/session-87/s87_spectrum_cache_L14_tau019.npz": sha256_of(CACHE_L14),
        "computations/session-91/s91_gate_verdicts.txt": sha256_of(S91_VERDICTS_PATH),
        "sessions/permanent-results-registry.md": sha256_of(PERMANENT_REGISTRY_PATH),
        ".claude/rules/substrate-first-canonical-sourcing.md": sha256_of(SUBSTRATE_FIRST_RULE_PATH),
        ".claude/rules/math-scripts.md": sha256_of(MATH_SCRIPTS_RULE_PATH),
    }
    print("\n=== Input pins (SHA-256 heads) ===")
    for k, v in sorted(pins.items()):
        print(f"  {k}: {v[:16]}")

    # 2) tau-field cache consistency check
    if not verify_tau_field(CACHE_L12):
        print("ABORT: L_max=12 cache tau field mismatch against tau_fold = 0.19")
        return 1
    if not verify_tau_field(CACHE_L14):
        print("ABORT: L_max=14 cache tau field mismatch against tau_fold = 0.19")
        return 1
    print(f"\ntau_fold = {tau_fold} (cache files tau019)")

    # 3) PV identity cross-checks (Σ c_r = 1, Σ c_r·m_r² = 0)
    sc, scm2 = _verify_pv_identities()
    print("\n=== PV identity cross-checks ===")
    print(f"  Σ c_r        = {sc:.16e}  (target 1; |err|<1e-12 required)")
    print(f"  Σ c_r · m_r² = {scm2:.16e}  (target 0; |err|<1e-12 required)")
    pv_identities_pass = (abs(sc - 1.0) < 1e-12) and (abs(scm2) < 1e-12)
    if not pv_identities_pass:
        print("ABORT: PV identities failed")
        return 1
    print("  PV identities PASS")

    # 4) Load spectra at L_max=12 and L_max=14
    print("\n=== Loading L_max=12 cache ===")
    lambdas12, mults12, n_sec12, max_lev12 = load_spectrum_flat(CACHE_L12)
    print(f"  n_sectors = {n_sec12}, max_level = {max_lev12}")
    print(f"  N_eigenvalues = {len(lambdas12)}, "
          f"lambda range [{np.min(lambdas12):.6f}, {np.max(lambdas12):.6f}]")
    print(f"  total weighted multiplicity = {np.sum(mults12):.0f}")

    print("\n=== Loading L_max=14 cache ===")
    lambdas14, mults14, n_sec14, max_lev14 = load_spectrum_flat(CACHE_L14)
    print(f"  n_sectors = {n_sec14}, max_level = {max_lev14}")
    print(f"  N_eigenvalues = {len(lambdas14)}, "
          f"lambda range [{np.min(lambdas14):.6f}, {np.max(lambdas14):.6f}]")
    print(f"  total weighted multiplicity = {np.sum(mults14):.0f}")

    # 5) Evaluate rho_FULL at L_max=12 and L_max=14 (substrate-distance-1 pole s=3)
    print(f"\n=== Evaluating rho_FULL at pole s={S_POLE} on L_max=12 ===")
    rho_L12, M_FULL_L12, M_BARE_L12, diag12 = evaluate_rho_FULL(
        S_POLE, lambdas12, mults12)
    print(f"  M_BARE(s={S_POLE}, L=12) = {M_BARE_L12:.10e}")
    print(f"  M_FULL(s={S_POLE}, L=12) = {M_FULL_L12:.10e}")
    print(f"  ρ_FULL(s={S_POLE}, L=12) = {rho_L12:.10f}")
    print(f"  w_PV stats: min={diag12['w_PV_min']:.6f}, "
          f"mean={diag12['w_PV_mean']:.6f}, max={diag12['w_PV_max']:.6f}")

    print(f"\n=== Evaluating rho_FULL at pole s={S_POLE} on L_max=14 ===")
    rho_L14, M_FULL_L14, M_BARE_L14, diag14 = evaluate_rho_FULL(
        S_POLE, lambdas14, mults14)
    print(f"  M_BARE(s={S_POLE}, L=14) = {M_BARE_L14:.10e}")
    print(f"  M_FULL(s={S_POLE}, L=14) = {M_FULL_L14:.10e}")
    print(f"  ρ_FULL(s={S_POLE}, L=14) = {rho_L14:.10f}")
    print(f"  w_PV stats: min={diag14['w_PV_min']:.6f}, "
          f"mean={diag14['w_PV_mean']:.6f}, max={diag14['w_PV_max']:.6f}")

    # 6) Compute rel_drift (Friedrich-Bär saturation analog)
    rel_drift = abs(rho_L14 - rho_L12) / abs(rho_L12)
    print(f"\n=== Friedrich-Bär saturation rel_drift ===")
    print(f"  rel_drift = |ρ(L=14) - ρ(L=12)| / |ρ(L=12)| = {rel_drift:.10e}")
    print(f"  PASS threshold: rel_drift < {PASS_THRESHOLD}")
    print(f"  INFO  upper:    rel_drift < {INFO_TOL_UPPER}")

    # 7) Friedrich-Bär NEW-sector intrusion margin diagnostic
    print(f"\n=== Friedrich-Bär NEW-sector intrusion diagnostic (W11-3 precedent) ===")
    intrusion = friedrich_baer_intrusion_diagnostic(CACHE_L12, CACHE_L14, S_POLE)
    print(f"  M_BARE(s=3, L=14, full)                  = {intrusion['M_BARE_L14_full']:.10e}")
    print(f"  M_BARE(s=3, L=14, NEW sectors p+q∈13,14) = {intrusion['M_BARE_new_sectors_L13_L14']:.10e}")
    print(f"  intrusion_ratio                          = {intrusion['new_sector_intrusion_ratio']:.10e}")
    print(f"  n_new_sectors                            = {intrusion['n_new_sectors']}")
    print(f"  unique NEW levels p+q                    = {intrusion['unique_new_levels']}")
    print(f"  η_FB lower (empirical, L_max=12)         = {intrusion['eta_FB_lower_empirical_L12']:.4f}")

    # 8) Pre-registered verdict evaluation
    composite, sign_v, mag_v, reg_v = evaluate_gate(rel_drift)
    print(f"\n=== Verdict ===")
    print(f"  composite          = {composite}")
    print(f"  sign_verdict       = {sign_v}")
    print(f"  magnitude_verdict  = {mag_v}")
    print(f"  regime_verdict     = {reg_v}")

    # 9) Compute dual-SHA (audit + content) — audit from input_pin_map (sig_5 safe)
    audit_sha, content_sha = compute_dual_sha(
        SCRIPT_PATH, CANONICAL_CONSTANTS_PATH, pins)
    print(f"\n=== Dual-SHA ===")
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")
    print(f"  closure_hash(pins) [cross-check]: {closure_hash(pins)}")

    # 10) Save .npz data file
    np.savez_compressed(
        OUT_NPZ,
        # Substrate-IS observables
        rho_FULL_L12=rho_L12,
        rho_FULL_L14=rho_L14,
        rel_drift=rel_drift,
        # Component moments
        M_FULL_L12=M_FULL_L12,
        M_BARE_L12=M_BARE_L12,
        M_FULL_L14=M_FULL_L14,
        M_BARE_L14=M_BARE_L14,
        # Verdict
        verdict_composite=composite,
        verdict_sign=sign_v,
        verdict_magnitude=mag_v,
        verdict_regime=reg_v,
        # Pre-registered thresholds
        PASS_threshold=PASS_THRESHOLD,
        INFO_threshold_upper=INFO_TOL_UPPER,
        # Cache diagnostics
        n_sectors_L12=n_sec12,
        n_sectors_L14=n_sec14,
        max_level_L12=max_lev12,
        max_level_L14=max_lev14,
        N_eigenvalues_L12=len(lambdas12),
        N_eigenvalues_L14=len(lambdas14),
        # PV identities
        pv_sum_c=sc,
        pv_sum_c_m2=scm2,
        PV_PRIMARY_C=PV_PRIMARY_C,
        PV_PRIMARY_M_DIMLESS=PV_PRIMARY_M_DIMLESS,
        # w_PV statistics at each L_max
        w_PV_min_L12=diag12["w_PV_min"],
        w_PV_max_L12=diag12["w_PV_max"],
        w_PV_mean_L12=diag12["w_PV_mean"],
        w_PV_std_L12=diag12["w_PV_std"],
        w_PV_min_L14=diag14["w_PV_min"],
        w_PV_max_L14=diag14["w_PV_max"],
        w_PV_mean_L14=diag14["w_PV_mean"],
        w_PV_std_L14=diag14["w_PV_std"],
        # Friedrich-Bär intrusion diagnostic
        intrusion_M_BARE_L14_full=intrusion["M_BARE_L14_full"],
        intrusion_M_BARE_new=intrusion["M_BARE_new_sectors_L13_L14"],
        intrusion_ratio=intrusion["new_sector_intrusion_ratio"],
        intrusion_ratio_below_1e_3=intrusion["intrusion_ratio_below_1e-3"],
        n_new_sectors=intrusion["n_new_sectors"],
        unique_new_levels=np.array(intrusion["unique_new_levels"], dtype=int),
        eta_FB_lower_empirical_L12=intrusion["eta_FB_lower_empirical_L12"],
        # Constants
        tau_fold=tau_fold,
        S_POLE=S_POLE,
        L_MAX_PAIR=np.array(L_MAX_PAIR),
        # Canonical pin cross-references (Level-1 + Level-3 from canonical_constants)
        alpha_canonical_VII_AU_ASYMPTOTIC=alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC,
        alpha_sample_VII_AU_PATHWAY_B_L15_22=alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22,
        # SHAs
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        # Supersedes-target (Option A protocol)
        supersedes_target=SUPERSEDES_TARGET,
    )
    print(f"\nSaved .npz data file: {OUT_NPZ}")

    # 11) Diagnostic plot
    make_plot(rho_L12, rho_L14, rel_drift,
              M_FULL_L12, M_BARE_L12, M_FULL_L14, M_BARE_L14,
              diag12, diag14, intrusion)
    print(f"Saved plot: {OUT_PNG}")

    # 12) Verdict line (canonical-form value string + supersedes tag)
    value_str = (
        f"rel_drift={rel_drift:.10e}_"
        f"rho_FULL_L12={rho_L12:.10f}_"
        f"rho_FULL_L14={rho_L14:.10f}_"
        f"M_BARE_L12={M_BARE_L12:.6e}_M_FULL_L12={M_FULL_L12:.6e}_"
        f"M_BARE_L14={M_BARE_L14:.6e}_M_FULL_L14={M_FULL_L14:.6e}_"
        f"intrusion_ratio={intrusion['new_sector_intrusion_ratio']:.6e}_"
        f"eta_FB_emp={intrusion['eta_FB_lower_empirical_L12']:.4f}_"
        f"PV_identity_dc={sc:.2e}_PV_identity_dcm2={scm2:.2e}"
    )
    append_verdict(composite, value_str, audit_sha, content_sha)
    print(f"\nAppended canonical verdict line + dual-SHA companion + "
          f"LEVEL/MACHINERY/BINDING pin rows to:")
    print(f"  {VERDICT_TXT}")

    # 13) On PASS: canonical-write-order Step 2 promotion
    if composite == "PASS":
        # Promote rho_FULL_CC_VII_AU_SAT(s=3) to canonical_constants.py
        # via direct append. Use the L_max=14 value as the saturated reference.
        rho_saturated = rho_L14  # (local; PASS means L=12 and L=14 agree within 0.1%)
        canonical_block = f'''

# --- S92 W1-CF-W9-8-2 §VII.AU.OP-PROJ FULL-CC saturated canonical -----------
#
# Friedrich-Bär saturation at the FULL-CC regulator class on §VII.AU.OP-PROJ
# at substrate-distance-1 pole s=3 (gate {GATE_ID}, PASS verdict; rel_drift
# = {rel_drift:.4e} < {PASS_THRESHOLD:.0e}). The saturated value below pins
# the substrate-IS canonical at CLASS=FULL replacing the SCHEMATIC STRICT_F4
# anchor (per S91 W9-4 surfaced level-class mismatch).
#
# Provenance:
#   - This gate's audit_sha256: {audit_sha}
#   - Supersedes-target (Option A protocol):
#     {SUPERSEDES_TARGET}
#     (S91-W1-14-COMPOSITE-BRIDGE-MAP-RDX FAIL line, s91_gate_verdicts.txt:221)
#   - Verdict file: computations/session-92/s92_gate_verdicts.txt
#   - L_max=12 measurement: ρ_FULL(s=3, L=12) = {rho_L12:.10f}
#   - L_max=14 measurement: ρ_FULL(s=3, L=14) = {rho_L14:.10f}
#   - Friedrich-Bär NEW-sector intrusion ratio: {intrusion['new_sector_intrusion_ratio']:.4e}
#     (analytic certification per `math-scripts.md §"D_K Block-Diagonality +
#     Recursive-Casimir-Projection Feasibility Pre-Check"` W11-3 precedent)
#
# Level-pin discipline (substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY):
#   CLASS=FULL (consumes _pauli_villars_subtraction.py PRIMARY helper;
#               FULL physical CC1996 §2.2-2.3 multipliers (M_KK, +2, √2·M_KK, -1);
#               NO -SCHEMATIC suffix)
#
# MACHINERY-SCOPE axis (regulator-pin-discipline.md): CACHE-PROJECTION
#   (cache-projection-truncated observable on L_max=12 + L_max=14 master caches)
#
# BINDING axis (regulator-pin-discipline.md): substrate-natural-binding
#   (substrate's own Hochschild-pairing image at §VII.AU.OP-PROJ slot)
#
# This pin closes the S91 W9-8 α_composite = -1.518765 anti-convergence
# pattern as a level-class mismatch artifact (composite MS ∘ HKR consumer was
# FULL-CC while §VII.AU pin was SCHEMATIC); the SCHEMATIC pins
# (alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC = -3,
#  alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22 = 2.6926...) remain
# canonical at CLASS=SCHEMATIC per K=4 MANDATORY level-pin discipline.
#
rho_FULL_CC_VII_AU_SAT_s3 = {rho_saturated!r}  # FULL-CC saturated canonical at §VII.AU.OP-PROJ substrate-distance-1 pole s=3 (S92 W1-CF-W9-8-2 PASS; Friedrich-Bär saturated L_max∈{{12,14}}; rel_drift={rel_drift:.4e}<{PASS_THRESHOLD:.0e}; supersedes 0da19aba…) (S92)
'''
        # Append the canonical-write-order Step 2 block
        with CANONICAL_CONSTANTS_PATH.open("a", encoding="utf-8") as fp:
            fp.write(canonical_block)
        print(f"\n=== Canonical-write-order Step 2 PROMOTION ===")
        print(f"  Appended rho_FULL_CC_VII_AU_SAT_s3 = {rho_saturated!r} "
              f"to canonical_constants.py")
        print(f"  Provenance block cites this gate's audit_sha256 AND supersedes-target.")
    elif composite == "INFO":
        print(f"\n=== Canonical-write-order Step 2: INFO (marginal saturation) ===")
        print(f"  rel_drift = {rel_drift:.4e} in [{PASS_THRESHOLD:.0e}, {INFO_TOL_UPPER:.0e})")
        print(f"  Pin recordable with Level-2 envelope marginal-saturation caveat;")
        print(f"  registry-landing decision deferred to W2 mack-cosmic-bridge per plan.")
    else:  # FAIL
        print(f"\n=== Canonical-write-order Step 2: FAIL (saturation does NOT extend) ===")
        print(f"  rel_drift = {rel_drift:.4e} ≥ {INFO_TOL_UPPER:.0e}")
        print(f"  REGISTRY-INCOMPLETE-PENDING-FRIEDRICH-BAR-SATURATION-CERTIFICATION;")
        print(f"  no canonical-constants pin promoted; carry-forward to S93+ L_max≥16.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
