#!/usr/bin/env python3
"""
S87 W11-1 — S87-MONODROMY-V_4-EXPLICIT
========================================

Gate: S87-MONODROMY-V_4-EXPLICIT  (trigger: VERIFY)

Pre-registered threshold (per session-87-plan-w11.md §W11-1.5):
  PASS iff per-moment relative deviation
    |A_n^(g_0) - A_n^(g_1) - A_n^(g_2) + A_n^(g_3)| / max_g |A_n^(g)| <= 1e-12
  for ALL n in {0, 2, 4}.
  FAIL iff relative deviation > 1e-9 for ANY n in {0, 2, 4}.
  INFO if 1e-12 < dev <= 1e-9 (precision-limited band).

This gate SUPERSEDES the pre-registered S87-MONODROMY-Z4-LANDING per
S86 W-12 RULE-W12-1 PRU Class 8.2 calibration. The "Z_4 or similar"
literal pre-reg admitted Klein-four V_4 via cardinality match (both
order 4) DESPITE structural distinction via element orders
(V_4 = [1,2,2,2] vs Z_4 = [1,2,4,4]).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py     (tau_fold=0.19, M_KK, Vol_SU3_Haar)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz  (substrate-IS D_K eigenvalues)
  - computations/_shared/_spectral_action_regulators.py     (TIER-2 SCHEMATIC Casimir helper)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=max_n |V_4 parallelogram dev|/|max-A_n^(g)|,
   scheme=Mellin-cone-substrate-distance-{3,1,0}-SCHEMATIC,
   convention=V_4-coset-W12-E1-R3-(p,q)-Cartan-Z2xZ2,
   L_max=10)

Classification: GEOMETRIC

METHODOLOGY
-----------
The V_4 = (Z_2)^2 group acts on the regulator weight via two independent
pointwise sign-flip involutions sigma_M, sigma_C : modes -> {-1, +1}.
The four cosets are e, a, b, ab with characters:

    chi_e(p,q)  = +1
    chi_a(p,q)  = sigma_M(p,q)              (Mellin-cone-residue Z_2 axis)
    chi_b(p,q)  = sigma_C(p,q)              (W6-3 conformal-end Z_2 axis)
    chi_ab(p,q) = sigma_M(p,q) * sigma_C(p,q)

The V_4 PARALLELOGRAM IDENTITY (per S86 W-12 Volovik R3 DISSENT line 834,
S86 bimodality workshop file lines 798-840 — the additive cocycle
correction to V3's mistakenly multiplicative form):

    A_n^(e) - A_n^(a) - A_n^(b) + A_n^(ab) = 0    [for each n in {0, 2, 4}]

Per linearity:
    Delta_n := Sum_{(p,q)} [1 - chi_a][1 - chi_b] * d(p,q) * w(p,q,n)
            = 4 * Sum_{(p,q): chi_a=chi_b=-1} d(p,q) * w(p,q,n)

where w(p,q,n) = 1/C_2(p,q)^n is the Mellin-cone Casimir weight at moment n
(n=0 -> identity weight -> bare degeneracy sum). This identity holds
EXACTLY iff the (chi_a=-1, chi_b=-1) eigenspace is empty on the substrate's
mode content (the "disjoint-support" condition of W-12 EMERGENCE E-2
line 1643).

Substrate-physical hypothesis: the most natural V_4 acting on SU(3)
Peter-Weyl (p,q) lattice is
    sigma_M(p,q) = (-1)^p,  sigma_C(p,q) = (-1)^q
yielding the Cartan-toral Z_2 x Z_2 partition modulo 2.

Two evaluation pathways (both reported; primary verdict from Pathway-1):
  Pathway-1 (SCHEMATIC Casimir / Mellin-cone analog):
    Use the canonical Mellin/zeta a_n evaluator on
    the SU(3) Casimir spectrum at L_max=10 with V_4 character twist.
    Convention=V_4-coset-W12-E1-R3-(p,q)-Cartan-Z2xZ2-SCHEMATIC.
  Pathway-2 (substrate-IS cached D_K spectrum at tau_fold=0.19):
    Reduce s84_spectrum_cache_L12_tau019.npz to L_max=10 and
    evaluate the same V_4 twist on actual D_K eigenvalues.
    Convention=V_4-coset-W12-E1-R3-(p,q)-Cartan-Z2xZ2-SUBSTRATE.

Both pathways FAIL the 1e-12 threshold in general (the (1,1)-mod-2
Cartan sector is non-empty at L_max=10 -- e.g., (1,1), (1,3), (3,1),
(3,3), (1,5), ..., contributing 4 * Sum_{p odd, q odd} d/C^n which is
of the same order as the full sum). This FAIL is the substrate-physical
finding: under the natural Cartan V_4, the substrate does NOT respect
the disjoint-support condition at the mode level.

DISCIPLINE
----------
- `from canonical_constants import *` (imports tau_fold, M_KK, Vol_SU3_Haar, PI)
- All locals tagged `# (local)`
- TIER-2 SCHEMATIC convention pin per substrate-first-canonical-sourcing.md
  §(iv): the regulator module is documented as schematic (line 23-30 of
  _spectral_action_regulators.py). Convention suffix `-SCHEMATIC` is
  REQUIRED to be honest about the TIER pin.
- Dual-SHA verdict line per S84+ schema; supersession-event citation in
  value field per HIGH-DENSITY WORKSHOP TEMPLATE T2-5.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Local TIER-2 SCHEMATIC regulator module (positive-Casimir helper)
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _spectral_action_regulators import (  # noqa: E402
    weyl_dim_su3,
    casimir_su3,
    _enumerate_sectors,
    zeta_a_n,
    mellin_a_n,
)

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S87"                                                               # (local)
GATE_ID = "S87-MONODROMY-V_4-EXPLICIT"                                        # (local)
SCHEME = "Mellin-cone-substrate-distance-{3,1,0}-SCHEMATIC"                   # (local)
CONVENTION = "V_4-coset-W12-E1-R3-(p,q)-Cartan-Z2xZ2-SCHEMATIC"               # (local)
L_MAX = 10                                                                    # (local)

# Pre-registered pass/fail thresholds (per plan §5)
PASS_THRESHOLD = 1e-12                                                        # (local) PASS band ceiling
INFO_THRESHOLD = 1e-9                                                         # (local) INFO band ceiling
N_MOMENTS = (0, 2, 4)                                                         # (local) Seeley-DeWitt moment indices
COSET_LABELS = ("e", "a", "b", "ab")                                          # (local) V_4 coset labels (g_0..g_3)

# Output destinations
OUT_NPZ = resolve_output(87, 's87_w11_v4_monodromy_explicit.npz')
OUT_PNG = resolve_output(87, 's87_w11_v4_monodromy_explicit.png')
VERDICT_TXT = resolve_output(87, 's87_gate_verdicts.txt')

# Script + spectrum-cache + canonical_constants are pinned for SHA closure
SPECTRUM_CACHE = resolve_output(84, 's84_spectrum_cache_L12_tau019.npz')
REGULATOR_MOD = resolve_script(None, '_spectral_action_regulators.py')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    SPECTRUM_CACHE,
    REGULATOR_MOD,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                                      # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}                                                                 # (local)
    for p in inputs:
        sha = sha256_of(p)                                                    # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")             # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())                                              # (local)
    h = hashlib.sha256()                                                      # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins):
    script_bytes = script_path.read_bytes()                                   # (local)
    canonical_bytes = canonical_path.read_bytes()                             # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")                                                         # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                               # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()                                           # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — V_4 character + spectral-moment evaluators
# ---------------------------------------------------------------------------
def chi_V4(coset, p, q):
    """V_4 = (Z_2)^2 character on SU(3) sector (p,q).

    sigma_M(p,q) = (-1)^p   (Mellin-cone-residue Z_2 axis: parity of p)
    sigma_C(p,q) = (-1)^q   (W6-3 conformal-end Z_2 axis: parity of q)
    """
    sm = (-1) ** p                                                            # (local) sigma_M
    sc = (-1) ** q                                                            # (local) sigma_C
    if coset == "e":
        return 1
    if coset == "a":
        return sm
    if coset == "b":
        return sc
    if coset == "ab":
        return sm * sc
    raise ValueError(f"Unknown V_4 coset: {coset}")


def A_n_twisted_schematic(n, coset, L_max):
    """SCHEMATIC V_4-twisted spectral-action moment A_n^(g) on SU(3) Casimir
    spectrum.

    A_n^(g) = (1/Vol_SU3_Haar) * Sum_{(p,q): p+q<=L_max, (p,q)!=(0,0)}
              chi_g(p,q) * d(p,q) * 1/C_2(p,q)^n             (n > 0)
    A_0^(g) = (1/Vol_SU3_Haar) * Sum chi_g(p,q) * d(p,q)     (n = 0; identity weight)
    """
    sectors = _enumerate_sectors(L_max)                                       # (local)
    if n == 0:
        s = sum(chi_V4(coset, p, q) * d for p, q, d, c in sectors)            # (local)
        return s / Vol_SU3_Haar
    acc = 0.0                                                                 # (local)
    for p, q, d, c in sectors:
        acc += chi_V4(coset, p, q) * d / (c ** n)
    return acc / Vol_SU3_Haar


def A_n_twisted_substrate(n, coset, sector_evals, L_max):
    """SUBSTRATE V_4-twisted spectral-action moment using cached D_K eigenvalues.

    A_n^(g) = (1/Vol_SU3_Haar) * Sum_{(p,q): p+q<=L_max} chi_g(p,q)
              * Sum_{i in sector(p,q)} |lambda_i|^(-2n)        (n > 0)
    A_0^(g) = (1/Vol_SU3_Haar) * Sum chi_g(p,q) * #{eigvals in sector}

    Note: substrate eigenvalues at tau_fold=0.19 are dimensionless (already
    in M_KK units per S84 cache convention). Smallest |lambda| at
    tau_fold approaches ~0.05; we filter |lambda| > 1e-12 to avoid zero-mode
    division blow-up.
    """
    if n == 0:
        s = 0.0                                                               # (local)
        for (p, q), entry in sector_evals.items():
            if p + q > L_max or (p == 0 and q == 0):
                continue
            n_eigs = len(entry["abs_evals"])                                  # (local)
            s += chi_V4(coset, p, q) * n_eigs
        return s / Vol_SU3_Haar
    acc = 0.0                                                                 # (local)
    for (p, q), entry in sector_evals.items():
        if p + q > L_max or (p == 0 and q == 0):
            continue
        evals = np.asarray(entry["abs_evals"])                                # (local)
        evals = evals[evals > 1e-12]                                          # (local) zero-mode guard
        if evals.size == 0:
            continue
        acc += chi_V4(coset, p, q) * np.sum(evals ** (-2 * n))
    return acc / Vol_SU3_Haar


# ---------------------------------------------------------------------------
# Section 6 — Compute
# ---------------------------------------------------------------------------
def compute():
    # Load substrate spectrum cache
    print(f"\n=== Loading substrate spectrum cache: {SPECTRUM_CACHE.name} ===")
    cache = np.load(SPECTRUM_CACHE, allow_pickle=True)                        # (local)
    sector_evals = cache["sector_evals"].item()                               # (local) dict {(p,q): {dim, level, abs_evals}}
    print(f"  Loaded {len(sector_evals)} sectors at L_max=12; restricting to L_max={L_MAX}")
    n_used = sum(
        len(v["abs_evals"]) for k, v in sector_evals.items()
        if k[0] + k[1] <= L_MAX and k != (0, 0)
    )                                                                         # (local)
    print(f"  L_max={L_MAX} effective eigenvalue count: {n_used}")

    # Pathway 1: SCHEMATIC Casimir / Mellin-cone analog (positive-Casimir
    # spectrum, regulator module canonical zeta_a_n with V_4 twist applied
    # at the character level)
    print(f"\n=== Pathway 1 (SCHEMATIC) — Casimir / zeta-Mellin V_4 twist ===")
    A_schematic = {}                                                          # (local) A_schematic[n][g] = float
    for n in N_MOMENTS:
        A_schematic[n] = {}
        for g in COSET_LABELS:
            A_schematic[n][g] = A_n_twisted_schematic(n, g, L_MAX)
        # cross-check: untwisted (g=e) matches stock zeta_a_n
        if n == 0:
            stock = zeta_a_n(0, L_MAX, Vol_SU3_Haar)                          # (local)
        else:
            stock = zeta_a_n(n, L_MAX, Vol_SU3_Haar)                          # (local)
        delta_stock = abs(A_schematic[n]["e"] - stock)                        # (local)
        print(f"  n={n}: A^e (twisted, g=e) = {A_schematic[n]['e']:.6e}; "
              f"stock zeta_a_n = {stock:.6e}; cross-check |delta| = {delta_stock:.2e}")
        for g in COSET_LABELS:
            print(f"    A_{n}^({g}) = {A_schematic[n][g]:+.6e}")

    # Pathway 2: SUBSTRATE V_4 twist on cached D_K(tau_fold) spectrum
    print(f"\n=== Pathway 2 (SUBSTRATE) — D_K(tau_fold={tau_fold}) V_4 twist ===")
    A_substrate = {}                                                          # (local)
    for n in N_MOMENTS:
        A_substrate[n] = {}
        for g in COSET_LABELS:
            A_substrate[n][g] = A_n_twisted_substrate(n, g, sector_evals, L_MAX)
        for g in COSET_LABELS:
            print(f"    A_{n}^({g}) = {A_substrate[n][g]:+.6e}")

    # V_4 PARALLELOGRAM IDENTITY: A^e - A^a - A^b + A^ab
    print(f"\n=== V_4 PARALLELOGRAM IDENTITY: A^e - A^a - A^b + A^ab ===")
    print(f"    PASS threshold (relative deviation): {PASS_THRESHOLD:.0e}")
    print(f"    INFO threshold (relative deviation): {INFO_THRESHOLD:.0e}")

    # Pathway-1 (SCHEMATIC) is the PRIMARY verdict-emitting pathway
    parallelogram_dev_per_n = []                                              # (local) list of (n, abs_dev, max, rel_dev)
    parallelogram_dev_substrate_per_n = []                                    # (local) Pathway-2 record
    for n in N_MOMENTS:
        # Pathway 1 (SCHEMATIC) -- primary verdict
        A = A_schematic[n]                                                    # (local)
        delta = A["e"] - A["a"] - A["b"] + A["ab"]                            # (local)
        max_abs = max(abs(A[g]) for g in COSET_LABELS)                        # (local)
        rel = abs(delta) / max_abs if max_abs > 0 else float("inf")           # (local)
        parallelogram_dev_per_n.append((n, abs(delta), max_abs, rel))
        print(f"  [SCHEMATIC] n={n}: delta = {delta:+.6e}, "
              f"max|A_n^(g)| = {max_abs:.6e}, rel_dev = {rel:.6e}")

        # Pathway 2 (SUBSTRATE) -- diagnostic record
        Asub = A_substrate[n]                                                 # (local)
        delta_sub = Asub["e"] - Asub["a"] - Asub["b"] + Asub["ab"]            # (local)
        max_abs_sub = max(abs(Asub[g]) for g in COSET_LABELS)                 # (local)
        rel_sub = abs(delta_sub) / max_abs_sub if max_abs_sub > 0 else float("inf")  # (local)
        parallelogram_dev_substrate_per_n.append((n, abs(delta_sub), max_abs_sub, rel_sub))
        print(f"  [SUBSTRATE] n={n}: delta = {delta_sub:+.6e}, "
              f"max|A_n^(g)| = {max_abs_sub:.6e}, rel_dev = {rel_sub:.6e}")

    max_rel_dev = max(rel for _, _, _, rel in parallelogram_dev_per_n)        # (local) primary
    max_rel_dev_substrate = max(
        rel for _, _, _, rel in parallelogram_dev_substrate_per_n
    )                                                                         # (local) substrate

    print(f"\n  PRIMARY (SCHEMATIC): max relative deviation across n in {N_MOMENTS}: "
          f"{max_rel_dev:.6e}")
    print(f"  DIAGNOSTIC (SUBSTRATE): max rel deviation: {max_rel_dev_substrate:.6e}")

    # Cross-check 1: V_4 vs Z_4 element-order discrimination (structural, not numerical)
    # V_4 element orders: e=1, a=2, b=2, ab=2  -> [1, 2, 2, 2]
    # Z_4 element orders: e=1, g=4, g^2=2, g^3=4 -> [1, 4, 2, 4]
    v4_orders = [1, 2, 2, 2]                                                  # (local) Klein-four
    z4_orders = [1, 4, 2, 4]                                                  # (local) cyclic-four
    cc2_distinct = (v4_orders != z4_orders)                                   # (local) True (structurally distinct)
    print(f"\n  CC2 V_4 vs Z_4 element-order signature: V_4={v4_orders}, Z_4={z4_orders}, "
          f"distinct={cc2_distinct}")

    return {
        "value": max_rel_dev,
        "max_rel_dev_schematic": max_rel_dev,
        "max_rel_dev_substrate": max_rel_dev_substrate,
        "A_schematic": A_schematic,
        "A_substrate": A_substrate,
        "parallelogram_dev_schematic": parallelogram_dev_per_n,
        "parallelogram_dev_substrate": parallelogram_dev_substrate_per_n,
        "v4_element_orders": v4_orders,
        "z4_element_orders": z4_orders,
        "v4_vs_z4_structurally_distinct": cc2_distinct,
        "n_eigvals_used_substrate": n_used,
    }


# ---------------------------------------------------------------------------
# Section 7 — Plot (4-panel: A_n^(g) bar charts + parallelogram-balance viz)
# ---------------------------------------------------------------------------
def make_plot(result):
    fig, axes = plt.subplots(2, 2, figsize=(13, 9))                           # (local)
    cosets = COSET_LABELS                                                     # (local)
    sign_color = {"e": "#1f77b4", "a": "#d62728", "b": "#d62728", "ab": "#1f77b4"}  # (local)
    sign_label = {"e": "+ (g_0)", "a": "- (g_1)", "b": "- (g_2)", "ab": "+ (g_3)"}  # (local)

    for ax, n in zip(axes.flat[:3], N_MOMENTS):
        A = result["A_schematic"][n]                                          # (local)
        # Per-coset bar with signed contribution (e and ab are positive in
        # the parallelogram identity; a and b are negative).
        sign = {"e": +1, "a": -1, "b": -1, "ab": +1}                          # (local)
        signed = [sign[g] * A[g] for g in cosets]                             # (local)
        bars = ax.bar(cosets, signed, color=[sign_color[g] for g in cosets])
        # Net parallelogram value annotation
        delta = A["e"] - A["a"] - A["b"] + A["ab"]                            # (local)
        max_abs = max(abs(A[g]) for g in cosets)                              # (local)
        rel = abs(delta) / max_abs if max_abs > 0 else 0.0                    # (local)
        ax.axhline(0, color="black", linewidth=0.7)
        ax.axhline(delta, color="red", linewidth=1.4, linestyle="--",
                   label=f"net = {delta:+.3e} (rel_dev={rel:.2e})")
        ax.set_title(f"$A_{n}^{{(g)}}$ (SCHEMATIC, signed by V_4 parallelogram)")
        ax.set_ylabel(f"sign(g) * $A_{n}^{{(g)}}$")
        ax.legend(loc="best", fontsize=8)
        ax.grid(True, alpha=0.3)
        for bar, g in zip(bars, cosets):
            h = bar.get_height()                                              # (local)
            ax.annotate(sign_label[g], xy=(bar.get_x() + bar.get_width() / 2, h),
                        ha="center", va="bottom" if h >= 0 else "top", fontsize=8)

    # Panel 4: parallelogram-balance summary (bar of |Delta_n| / max|A^(g)| per n)
    ax = axes.flat[3]
    n_axis = list(N_MOMENTS)                                                  # (local)
    rel_schematic = [r[3] for r in result["parallelogram_dev_schematic"]]     # (local)
    rel_substrate = [r[3] for r in result["parallelogram_dev_substrate"]]     # (local)
    x = np.arange(len(n_axis))                                                # (local)
    w = 0.35                                                                  # (local) bar width
    ax.bar(x - w / 2, rel_schematic, w, color="#1f77b4", label="SCHEMATIC (Pathway 1, primary)")
    ax.bar(x + w / 2, rel_substrate, w, color="#2ca02c", label="SUBSTRATE (Pathway 2, diagnostic)")
    ax.axhline(PASS_THRESHOLD, color="green", linestyle=":", label=f"PASS <= {PASS_THRESHOLD:.0e}")
    ax.axhline(INFO_THRESHOLD, color="orange", linestyle=":", label=f"INFO ceiling {INFO_THRESHOLD:.0e}")
    ax.set_yscale("log")
    ax.set_xticks(x)
    ax.set_xticklabels([f"n={n}" for n in n_axis])
    ax.set_ylabel("relative deviation (log scale)")
    ax.set_title(r"V_4 parallelogram identity: $|\Delta_n|/\max_g|A_n^{(g)}|$")
    ax.legend(loc="best", fontsize=8)
    ax.grid(True, alpha=0.3, which="both")

    fig.suptitle(
        f"S87-MONODROMY-V_4-EXPLICIT — V_4 = (Z_2)^2 parallelogram identity\n"
        r"$A_n^{(e)} - A_n^{(a)} - A_n^{(b)} + A_n^{(ab)} = 0$  ?"
        f"  at  $\\tau_{{\\rm fold}}={tau_fold}$,  L_max={L_MAX}\n"
        f"V_4 char: $\\sigma_M=(-1)^p$, $\\sigma_C=(-1)^q$  "
        f"(supersedes Z_4 pre-reg per PRU Class 8.2)",
        fontsize=11,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.94])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"  Plot saved: {OUT_PNG.name}")


# ---------------------------------------------------------------------------
# Section 8 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max):
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def evaluate_gate(value):
    """Apply pre-registered threshold per plan §5.

    PASS iff value (max relative deviation across n in {0,2,4}) <= PASS_THRESHOLD
    INFO iff PASS_THRESHOLD < value <= INFO_THRESHOLD
    FAIL iff value > INFO_THRESHOLD
    """
    if value <= PASS_THRESHOLD:
        return "PASS"
    if value <= INFO_THRESHOLD:
        return "INFO"
    return "FAIL"


def append_verdict(verdict, value, audit_sha, content_sha):
    """Append canonical S84+ verdict line + dual-SHA companion row."""
    # Encode supersession-event in the value field per HIGH-DENSITY WORKSHOP
    # TEMPLATE T2-5 (orchestrator override directive).
    sup_value = (
        f"max_dev={value:.6e},"
        f"supersedes=S87-MONODROMY-Z4-LANDING_per_PRU_Class_8_2"
    )                                                                         # (local)
    line = (
        f"{GATE_ID}: {verdict} -- value='{sup_value}' scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )                                                                         # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )                                                                         # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Section 9 — Main
# ---------------------------------------------------------------------------
def main():
    t0 = time.time()                                                          # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)                                        # (local)
    closure = closure_hash(pins)                                              # (local)
    print(f"  closure: {closure[:16]}... (legacy informational)")

    # 1b. Compute dual SHA per S84+ schema
    script_path = Path(__file__).resolve()                                    # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')                     # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")

    # 2. Compute
    result = compute()
    value = result["value"]                                                   # (local)

    # 3. Evaluate gate
    verdict = evaluate_gate(value)                                            # (local)

    # 4. Save data + plot
    np.savez(
        OUT_NPZ,
        A_0_per_coset=np.array([result["A_schematic"][0][g] for g in COSET_LABELS]),
        A_2_per_coset=np.array([result["A_schematic"][2][g] for g in COSET_LABELS]),
        A_4_per_coset=np.array([result["A_schematic"][4][g] for g in COSET_LABELS]),
        A_0_per_coset_substrate=np.array([result["A_substrate"][0][g] for g in COSET_LABELS]),
        A_2_per_coset_substrate=np.array([result["A_substrate"][2][g] for g in COSET_LABELS]),
        A_4_per_coset_substrate=np.array([result["A_substrate"][4][g] for g in COSET_LABELS]),
        parallelogram_dev_per_n=np.array(
            [r[3] for r in result["parallelogram_dev_schematic"]]
        ),
        parallelogram_dev_per_n_substrate=np.array(
            [r[3] for r in result["parallelogram_dev_substrate"]]
        ),
        max_dev=value,
        max_dev_substrate=result["max_rel_dev_substrate"],
        coset_enumeration_label=np.array(COSET_LABELS),
        moment_indices=np.array(N_MOMENTS),
        v4_element_orders=np.array(result["v4_element_orders"]),
        z4_element_orders=np.array(result["z4_element_orders"]),
        v4_vs_z4_structurally_distinct=np.array(result["v4_vs_z4_structurally_distinct"]),
        n_eigvals_used_substrate=np.array(result["n_eigvals_used_substrate"]),
        tau_fold=np.array(tau_fold),
        L_max=np.array(L_MAX),
    )
    print(f"  Data saved: {OUT_NPZ.name}")
    make_plot(result)

    # 5. Emit 4-tuple + append verdict
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)                       # (local)
    print(tag)
    append_verdict(verdict, value, audit_sha, content_sha)

    # 6. Final summary
    wall = time.time() - t0                                                   # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s, max_dev={value:.6e}) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
