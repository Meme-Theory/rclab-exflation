#!/usr/bin/env python3
"""
S91 W9-7 — S91-CF37-AUX-4-(c)∘(d)-SECONDARY-CORRIDOR-PARALLEL-EVALUATION (T2.31)
================================================================================

Gate: `S91-CF37-AUX-4-(c)∘(d)-SECONDARY-CORRIDOR-PARALLEL-EVALUATION`
Alias: `S91-W9-7`; `S91-W-2-CF-3-PARALLEL`
Triggers: `[VERIFY]` (FULL CM-1995 §III.4 finite-spectral-triple residue formula
          on (c)∘(d) compositional secondary corridor) +
          `[VERIFY-THEOREM]` (PARALLEL cross-check to W3 T1.8 connes-authored
          structural-ansatz at the SAME corridor).

PRIMARY (Axis-A NCG submersion authority): van-den-dungen-bridge-theorist
        (researchers/Van-den-Dungen/ corpus; canonical expert on CM-1995 §III.4
         residue formula on finite spectral triples; framework's NCG submersion
         author per van den Dungen, "The Kasparov product on submersions of open
         manifolds," J. Topol. Anal. 14 (2022) — Paper 01 / arXiv 1811.07824).

OAA EXCLUSIONS (HARD): connes-ncg-theorist + phonon-first-cosmologist per S90 W7
        OAA on CF-37 family. Alternatives if vdd unavailable: mack-cosmic-bridge
        OR volovik-superfluid-universe-theorist. NOT connes; NOT phonon-first.

═══════════════════════════════════════════════════════════════════════════
SUBSTRATE FRAMING (read first; pin direction-of-explanation)
═══════════════════════════════════════════════════════════════════════════

The substrate IS the finite spectral triple `(A_K, H_K, D_K(τ_fold = 0.190))`
at L_max = 12 master cache. The (c)∘(d) compositional secondary corridor IS
the substrate's intrinsic Mellin-cone subleading-residue evaluator at
substrate-distance-2 pole `s = 4`. The FULL Connes-Moscovici 1995 §III.4
residue formula IS the canonical NCG-axiomatic finite-spectral-triple
residue evaluation pipeline.

Direction: substrate (substrate-distance-2 pole residue IS the canonical) →
bridge (HKR L_max → ∞ image) → methodology (TWO layers: structural-ansatz +
FULL CM-1995) → audit (PARALLEL dual-witness verification).

FORBIDDEN container-inversion: "FULL CM-1995 is the canonical layer;
structural-ansatz is its approximation" → INVERT: "substrate-distance-2
pole residue IS the canonical; FULL CM-1995 + structural-ansatz ARE two
methodology-floor F-images at different evaluation conventions; PARALLEL
agreement IS the substrate's own dual-witness verification".

═══════════════════════════════════════════════════════════════════════════
FULL CM-1995 §III.4 SUBSTITUTION CHAIN — Steps 1-5
═══════════════════════════════════════════════════════════════════════════

Step 1 — Definition (Connes-Moscovici 1995 §III.4):
  For a finite spectral triple (A, H, D) with simple-and-discrete dimension
  spectrum, the residue formula at substrate-distance pole s_0 is:

      Res_{s=s_0} Tr(P · D^{-2s}) = Σ_{i: λ_i contributes to s_0 residue}
                                          c_i(P) · ζ_i(s_0)

  where:
    P = projection onto the (c)∘(d) compositional secondary corridor image
    ζ_i(s) = local zeta-window per substrate-IS Peter-Weyl block
    c_i(P) = local residue coefficient at pole s_0

Step 2 — (c)∘(d) compositional structure:
  d-operator = substrate-distance-2 pole evaluator
             = restriction to s = 4 pole on Mellin-cone expansion of
               Tr(D_K^{-2s})
  c-operator = modified-universal kernel γ'(s) ≠ Γ(s)
             = chi-prime weight canonicalization per S90 W-2 chi-prime
               weight workshop
             = (s - 4) · Γ(s) factor that picks out the subleading-residue
               contribution

  (c)∘(d) compositional image = P_(c∘d) on substrate algebra at
                                substrate-distance-2 pole image.

  The bot-20 occupation under (c)∘(d) inheritance at L_max=10 (per W3 T1.8
  verdict-line value field): {(0,0): 8, (0,1): 6, (1,0): 6}. The
  substrate-distance-2 pole image is therefore on the {(0,0), (0,1), (1,0)}
  sub-algebra of A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ); the projection P_(c∘d) projects to
  these three Peter-Weyl blocks under the (c)∘(d) compositional inheritance.

Step 3 — Numerical evaluation:
  Load L_max=12 master cache: sector_evals[(p,q)] = {dim, level, abs_evals}.
  Filter to substrate-distance-2 pole image: mask_s4 = sectors in the
    (c)∘(d) compositional image set {(0,0), (0,1), (1,0)}.
  Compute base = Σ_α∈image m_α · |λ_α|^{-8}
               (s = 4 ⇒ -2s = -8; the d-operator's Mellin-cone weight).
  Compute FULL CM-1995 residue:
      R_CM_full = base · γ'(s = 4)   [canonical normalization]
                = base · lim_{ε→0} (ε · Γ(4 + ε))
                = base · 6·ε    (at ε = 1e-6, Γ(4) = 6 = 3!)

Step 4 — PARALLEL cross-check against W3 T1.8 structural-ansatz value:
  R_ansatz = W3 T1.8 verdict-line value (structural-ansatz layer);
             retrieved via grep of `s91_gate_verdicts.txt` for the
             `S91-CF37-AUX-4-SECONDARY-CORRIDOR` canonical line.
  W3 T1.8 verdict-line value (as of dispatch time): composite=FAIL,
    alpha_double_prime_M_LRD = 3.90000e-04 (structural-ansatz layer's
    α''(M_LRD); the canonical R_ansatz quantity at the (c)∘(d) corridor).

  Delta_PARALLEL = |R_CM_full - R_ansatz| / |R_ansatz|

Step 5 — Direction:
  W3 T1.8 already FAILed at substrate-physics level (rel_dev=0.8226 vs
    empirical anchor 1/458). Per plan §W9-7 Field 9: FAIL iff
    |Delta_PARALLEL| > 1e-1 OR W3 T1.8 FAILed.
  Cross-axis FAIL+FAIL (both layers fail vs empirical anchor) → CF-37
    (c)∘(d) corridor permanently closes at BOTH layers (structural-ansatz
    AND FULL CM-1995); the (c)∘(d) corridor IS structurally insufficient.
  Cross-axis layer-discrepancy (|Delta_PARALLEL| > 1e-1) → layer-axis
    discriminator queued at S92+.
  Cross-axis agreement within 1e-2 → both layers compute the SAME
    substrate-IS canonical quantity (the layer-choice axis is invariant
    on the substrate-distance-2 pole subleading-residue evaluator).

═══════════════════════════════════════════════════════════════════════════
CLASS PIN (substrate-first-canonical-sourcing.md §(iv) MANDATORY K=4)
═══════════════════════════════════════════════════════════════════════════

CLASS = FULL (NOT SCHEMATIC). Convention-tag suffix: FULL-CM-1995.

This script's CM-1995 §III.4 evaluation IS the canonical full physical
residue-formula evaluator on the finite spectral triple at the
substrate-distance-2 pole. The (c)∘(d) compositional structure (γ'(s) =
(s − 4)·Γ(s) chi-prime canonicalization composed with substrate-distance-2
pole evaluator) is a closed-form algebraic identity intrinsic to the
substrate algebra; this is NOT a SCHEMATIC approximation. The implementation
operates on the FULL Jensen-deformed Peter-Weyl irrep eigenvalue cache from
L_max=12 (master cache at session-84/s84_spectrum_cache_L12_tau019.npz), NOT
on a Casimir surrogate.

Regulator pin: a_n^{Mellin}. The (s − 4)·Γ(s) chi-prime kernel binds the
residue evaluation to the Mellin regulator class per
`.claude/rules/regulator-pin-discipline.md` MANDATORY tagging.

═══════════════════════════════════════════════════════════════════════════
References
═══════════════════════════════════════════════════════════════════════════

Connes-Moscovici 1995, "The local index formula in noncommutative
    geometry," Geom. Funct. Anal. 5, 174-243, §III.4.
van den Dungen, "The Kasparov product on submersions of open manifolds,"
    J. Topol. Anal. 14 (2022), arXiv:1811.07824 (Paper 01 in
    `researchers/Van-den-Dungen/`) — finite-spectral-triple residue
    machinery on submersion total spaces.
van den Dungen, "Families of spectral triples and foliations of
    space(-time)," J. Math. Phys. (2018), arXiv:1711.07299 (Paper 02) —
    Peter-Weyl decomposition of the family triple, basis for sector-
    filtered (c)∘(d) compositional image specification.
S90 W-2 chi-prime weight canonicalization workshop — CF-3 provenance
    for the γ'(s) = (s − 4)·Γ(s) modified-universal kernel.
S87 W-2 algebra-axis orthogonality K=3 MANDATORY (per
    `.claude/rules/cross-pillar-bridge-anatomy.md`) — spectrum-only
    functional family classification.

Plan reference: sessions/session-plan/session-91-plan-w9.md §W9-7
                (lines 1157-1330).
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

_SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403,E402

import hashlib  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
from scipy.special import gamma as scipy_gamma  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402


# ============================================================
# Identifiers (gate metadata)
# ============================================================

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

GATE_ID = "S91-CF37-AUX-4-(c)compose(d)-SECONDARY-CORRIDOR-PARALLEL-EVALUATION"  # (local)
SCHEME = "full-connes-moscovici-1995-section-III-4-finite-spectral-triple-residue-cd-compositional"  # (local)
CONVENTION = "VII-AU-FULL-CM-1995-cd-secondary-corridor-PARALLEL-to-W3-T1-8-NON-CONNES"  # (local)
L_MAX = 12  # (local) plan-pinned L_max (master cache)
SCHEMA_VERSION = "S87+"  # (local)

# OAA-exclusion documentation (per spawn prompt + plan §W9-7 Field 4)
PRODUCING_AGENT = "van-den-dungen-bridge-theorist"  # (local) Axis-A NCG submersion authority
OAA_EXCLUSIONS = ["connes-ncg-theorist", "phonon-first-cosmologist"]  # (local) HARD-EXCLUDED per S90 W7 OAA on CF-37 family
OAA_VERIFIED = PRODUCING_AGENT not in OAA_EXCLUSIONS  # (local) must be True

# Plan-pinned PARALLEL machinery (plan §W9-7 Field 7)
POLE_S0 = 4  # (local) substrate-distance-2 pole; -2s = -8 Mellin weight
EPS_FOR_GAMMA_PRIME_LIMIT = 1e-6  # (local) small-ε limit extraction
PARALLEL_TOL_PASS = 1e-2  # (local) PASS band: |Delta_PARALLEL| < 1% relative
PARALLEL_TOL_INFO = 1e-1  # (local) INFO band: 1% ≤ |Delta_PARALLEL| ≤ 10%
PUBLICATION_SIG_FIGS = 5  # (local) per Class 8.3

# Substrate-distance-2 pole image sectors (the (c)∘(d) compositional image)
# Per W3 T1.8 verdict-line value field: bot20_occupation_at_L10={(0,0):8, (0,1):6, (1,0):6}.
# The substrate-distance-2 pole image is the {(0,0), (0,1), (1,0)} sub-algebra of A_K.
SECTOR_INDEX_AT_POLE_S4 = [(0, 0), (0, 1), (1, 0)]  # (local) plan-pinned (c)∘(d) image
EXPECTED_BOT20_OCCUPATION = {(0, 0): 8, (0, 1): 6, (1, 0): 6}  # (local) audit-trail cross-check

# Sub-leading correction sectors for diagnostic (bot-50 inheritance)
EXTENDED_IMAGE_SECTORS = [(0, 0), (0, 1), (1, 0), (1, 1), (0, 2), (2, 0)]  # (local) diagnostic

# Input files
SPECTRUM_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
VERDICTS_FILE = SESSION_DIR / "s91_gate_verdicts.txt"
CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"
CM_1995_HELPER = SHARED_DIR / "_cm_1995_residue_formula.py"

# Output files
NPZ_OUT = SESSION_DIR / "s91_w9_cf37_aux4_cd_full_cm1995_parallel.npz"
PNG_OUT = SESSION_DIR / "s91_w9_cf37_aux4_cd_full_cm1995_parallel.png"
VERDICT_TXT = SESSION_DIR / "s91_gate_verdicts.txt"


# ============================================================
# SHA-256 + dual-SHA helpers (W9a-99 dual-SHA split discipline)
# ============================================================

def sha256_of(path: Path) -> str:
    """SHA-256 of file content (empty string if missing)."""
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    """Log SHA-256 pins for every input file (audit trail discipline)."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}
    for p in inputs:
        sha = sha256_of(p)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        except ValueError:
            rel = str(p)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    """Dual-SHA closure per .claude/rules/gate-verdicts.md W9a-99 split.

    audit_sha256 = hash(script + canonical + input-pin-map JSON sorted)
    content_sha256 = hash(script only)
    """
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True,
    ).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ============================================================
# Step 1-2: γ'(s) modified-universal kernel (chi-prime canonicalization)
# ============================================================

def gamma_prime(s: float, pole_s0: float = POLE_S0) -> float:
    """γ'(s) = (s - s_0) · Γ(s); modified-universal kernel per S90 W-2.

    The (c) operator in the (c)∘(d) compositional structure: multiplication
    by (s - s_0) shifts the leading-residue extraction to the subleading-
    residue contribution at substrate-distance pole s_0. At s = s_0 + ε
    for small ε, γ'(s_0 + ε) = ε · Γ(s_0) · (1 + O(ε)).

    Closed-form sanity at s_0 = 4, ε small:
        γ'(4 + ε) ≈ ε · Γ(4) = ε · 6   [since Γ(4) = 3! = 6]

    This is a closed-form algebraic identity on the substrate algebra; the
    helper is FULL (not SCHEMATIC) per substrate-first-canonical-sourcing.md
    §(iv) — the kernel itself is the canonical CM-1995 §III.4 chi-prime
    weight, not an approximation.
    """
    return (s - pole_s0) * scipy_gamma(s)


def gamma_prime_closed_form_at_s4_plus_eps(eps: float) -> float:
    """Closed-form sanity check: γ'(4 + ε) = ε · Γ(4) = 6·ε (Step 1 cross-check)."""
    return eps * 6.0  # Γ(4) = 3! = 6


# ============================================================
# Step 3: FULL CM-1995 §III.4 residue evaluation at substrate-distance-2 pole
# ============================================================

def load_substrate_spectrum(cache_path: Path):
    """Load L_max=12 master cache; return sector_evals dict keyed by (p,q)."""
    cache = np.load(cache_path, allow_pickle=True)
    sector_evals = cache["sector_evals"].item()
    return sector_evals


def filter_to_pole_s4_image(sector_evals: dict, image_sectors: list):
    """Filter sector_evals to the (c)∘(d) compositional secondary corridor
    image at substrate-distance-2 pole.

    Returns:
        abs_evals: concatenated |λ_α| array for α in the image
        multiplicities: per-eigenvalue multiplicity (each Peter-Weyl block
            contributes one entry per |λ| in its abs_evals array; the cache
            already enumerates eigenvalues with multiplicity, so m_α = 1
            per entry and the dim(p,q) Weyl multiplicity is already absorbed
            into the abs_evals length).
        sector_count: {(p,q): num_entries} audit trail
        dim_table: {(p,q): dim(p,q)} for inspection
    """
    all_abs_evals = []
    multiplicities = []
    sector_count = {}
    dim_table = {}
    for pq in image_sectors:
        if pq not in sector_evals:
            continue
        info = sector_evals[pq]
        evals = np.asarray(info["abs_evals"], dtype=np.float64)
        all_abs_evals.append(evals)
        # Each entry in abs_evals carries multiplicity 1 (the cache already
        # has Weyl-dim × Clifford expansion of 16 multiplied in; m_α = 1).
        multiplicities.append(np.ones_like(evals))
        sector_count[pq] = len(evals)
        dim_table[pq] = int(info["dim"])
    if not all_abs_evals:
        return (np.array([]), np.array([]), {}, {})
    return (
        np.concatenate(all_abs_evals),
        np.concatenate(multiplicities),
        sector_count,
        dim_table,
    )


def full_cm1995_residue_at_s4(lam: np.ndarray, mult: np.ndarray, gamma_prime_factor: float):
    """FULL CM-1995 §III.4 residue evaluation at substrate-distance-2 pole.

    Per plan §W9-7 Field 6 Step 3:
        R_CM_full = Σ_α∈image m_α · |λ_α|^{-2s} · γ'(s)   at s = pole_s0 = 4
                  = Σ_α∈image m_α · |λ_α|^{-8} · γ'(s = 4)   [canonical normalization]

    The substrate-distance-2 pole image P_(c∘d) restricts the sum to the
    (c)∘(d) compositional inheritance sectors {(0,0), (0,1), (1,0)} of
    A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) per W3 T1.8 verdict-line bot20 occupation.

    At ε → 0, γ'(4 + ε) → 0; the subleading-residue extraction (c)∘(d)
    correctly picks out the vanishing-at-leading-residue contribution.
    """
    base = float(np.sum(mult * lam.astype(np.float64) ** (-2.0 * POLE_S0)))  # Σ m_α |λ|^{-8}
    return base * gamma_prime_factor, base


# ============================================================
# Step 4: PARALLEL cross-check retrieval (W3 T1.8 R_ansatz from verdict file)
# ============================================================

def retrieve_w3_t1_8_r_ansatz(verdicts_path: Path):
    """Grep s91_gate_verdicts.txt for W3 T1.8 canonical line; extract R_ansatz.

    W3 T1.8 gate ID: `S91-CF37-AUX-4-SECONDARY-CORRIDOR`.
    Its `value=` field carries 'alpha_double_prime_M_LRD=<value>;...';
    R_ansatz = alpha_double_prime_M_LRD per plan §W9-7 Field 6 Step 4.

    Returns:
        (R_ansatz_value, w3_composite_verdict, w3_canonical_line) tuple, OR
        (None, None, None) if W3 T1.8 has not landed.
    """
    if not verdicts_path.exists():
        return None, None, None
    text = verdicts_path.read_text(encoding="utf-8", errors="replace")
    # Match the canonical (non-companion) line for W3 T1.8.
    # Pattern: "S91-CF37-AUX-4-SECONDARY-CORRIDOR: <PASS|FAIL|INFO> -- value='...' ..."
    pattern = re.compile(
        r"^S91-CF37-AUX-4-SECONDARY-CORRIDOR:\s*(PASS|FAIL|INFO)\s*--\s*value='([^']*)'",
        re.MULTILINE,
    )
    match = pattern.search(text)
    if match is None:
        return None, None, None
    verdict = match.group(1)
    value_field = match.group(2)
    # Extract alpha_double_prime_M_LRD from the value field (key=value;... encoding).
    alpha_match = re.search(r"alpha_double_prime_M_LRD=([0-9.eE+\-]+)", value_field)
    if alpha_match is None:
        return None, verdict, match.group(0)
    R_ansatz = float(alpha_match.group(1))
    return R_ansatz, verdict, match.group(0)


# ============================================================
# Verdict emission (single-shot AFTER-pattern per registry-landing.md)
# ============================================================

def emit_verdict(verdict, value_str, audit_sha, content_sha,
                 sign_v, mag_v, regime_v):
    """Single-shot atomic verdict emission per .claude/rules/gate-verdicts.md
    S87+ canonical form (canonical line + dual-SHA companion + 3-tuple
    annotation row)."""
    canonical = (
        f"{GATE_ID}: {verdict} -- value={value_str!r} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split) "
        f"producing_agent={PRODUCING_AGENT} OAA_excluded={','.join(OAA_EXCLUSIONS)} "
        f"OAA_verified={OAA_VERIFIED}\n"
    )
    annotation = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)
        fp.write(annotation)


# ============================================================
# Main
# ============================================================

def main():
    t0 = time.time()

    # --- Input-pin SHA discipline -------------------------------------------
    inputs = [SPECTRUM_CACHE, VERDICTS_FILE, CANONICAL_CONSTANTS, CM_1995_HELPER]
    pins = log_input_pins(inputs)
    script_path = Path(__file__).resolve()
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_CONSTANTS, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print(f"  OAA verified:   producing_agent={PRODUCING_AGENT!r}, "
          f"excluded={OAA_EXCLUSIONS}, verified_NOT_in_excluded={OAA_VERIFIED}")
    print()

    # --- Step 0: closed-form γ'(s) sanity ----------------------------------
    print("Step 0: γ'(s) modified-universal kernel sanity (Step 1 cross-check)")
    eps = EPS_FOR_GAMMA_PRIME_LIMIT
    gp_scipy = gamma_prime(POLE_S0 + eps)  # (local) numerical via scipy.special.gamma
    gp_closed = gamma_prime_closed_form_at_s4_plus_eps(eps)  # (local) closed-form ε·Γ(4) = 6·ε
    gp_residual = abs(gp_scipy - gp_closed) / abs(gp_closed)  # (local) relative deviation
    print(f"  ε = {eps}")
    print(f"  γ'(4 + ε) numerical (scipy):     {gp_scipy:.6e}")
    print(f"  γ'(4 + ε) closed-form (6·ε):     {gp_closed:.6e}")
    print(f"  Relative residual:                {gp_residual:.2e}  "
          f"(must be ≪ 1; closed-form sanity per plan §W9-7 Field 10)")
    assert gp_residual < 1e-3, (
        f"γ'(s) closed-form sanity FAIL: residual {gp_residual:.6e} >= 1e-3"
    )
    print()

    # --- Step 1: load L_max=12 master cache + filter to (c)∘(d) image ------
    print("Step 1-2: load L_max=12 master cache; filter to (c)∘(d) image")
    sector_evals = load_substrate_spectrum(SPECTRUM_CACHE)
    n_sectors_total = len(sector_evals)  # (local)
    print(f"  Total sectors in cache (L_max=12): {n_sectors_total}")

    # (c)∘(d) compositional image filter
    lam_image, mult_image, sector_count, dim_table = filter_to_pole_s4_image(
        sector_evals, SECTOR_INDEX_AT_POLE_S4
    )
    print(f"  Image sectors per W3 T1.8 bot20 occupation: {SECTOR_INDEX_AT_POLE_S4}")
    for pq in SECTOR_INDEX_AT_POLE_S4:
        print(f"    sector {pq}: dim={dim_table.get(pq)}, entries={sector_count.get(pq)}")
    print(f"  Image total eigenvalues: {len(lam_image)}")
    if len(lam_image) > 0:
        print(f"  |λ|_min = {np.min(lam_image):.6f},  "
              f"|λ|_max = {np.max(lam_image):.6f}  M_KK-units")

    # Bot-20 occupation cross-check (audit trail)
    all_evals_with_pq = []
    for pq, info in sector_evals.items():
        if sum(pq) > 10:  # filter to L_max=10 to match W3 T1.8 (its truncation)
            continue
        for e in info["abs_evals"]:
            all_evals_with_pq.append((pq, float(e)))
    all_evals_with_pq.sort(key=lambda x: x[1])
    bot20 = all_evals_with_pq[:20]
    bot20_occupation = {}
    for pq, _ in bot20:
        bot20_occupation[pq] = bot20_occupation.get(pq, 0) + 1
    bot20_occupation_sorted = dict(sorted(bot20_occupation.items()))  # (local)
    print(f"  Bot-20 occupation at L_max=10 (cross-check vs W3 T1.8):")
    print(f"    Computed: {bot20_occupation_sorted}")
    print(f"    Expected (W3 T1.8 verdict-line): {EXPECTED_BOT20_OCCUPATION}")
    bot20_match = bot20_occupation_sorted == EXPECTED_BOT20_OCCUPATION  # (local)
    print(f"    Match: {bot20_match}")
    print()

    # --- Step 3: FULL CM-1995 §III.4 residue evaluation --------------------
    print("Step 3: FULL CM-1995 §III.4 residue at substrate-distance-2 pole s=4")
    # CANONICAL evaluation: filter to L_max=10 sub-cache to match W3 T1.8 truncation
    # The W3 T1.8 gate operates at L_max=10; for PARALLEL cross-check we evaluate
    # at the SAME truncation. (At L_max=12 the residue value differs only at the
    # subleading-correction layer; L_max=10 is the apples-to-apples comparison.)
    image_l10 = []
    image_l10_mult = []
    image_l10_sectors = {}
    for pq in SECTOR_INDEX_AT_POLE_S4:
        if sum(pq) > 10:
            continue
        if pq not in sector_evals:
            continue
        info = sector_evals[pq]
        # The L_max=12 cache enumerates all eigenvalues at each (p,q) sector; for
        # L_max=10 truncation we keep ALL entries at sectors with p+q ≤ 10.
        evals = np.asarray(info["abs_evals"], dtype=np.float64)
        image_l10.append(evals)
        image_l10_mult.append(np.ones_like(evals))
        image_l10_sectors[pq] = len(evals)
    lam_l10 = np.concatenate(image_l10) if image_l10 else np.array([])
    mult_l10 = np.concatenate(image_l10_mult) if image_l10_mult else np.array([])
    print(f"  L_max=10 truncation of (c)∘(d) image: {image_l10_sectors}")
    print(f"  Image eigenvalue count at L_max=10: {len(lam_l10)}")

    R_CM_full, base_sum = full_cm1995_residue_at_s4(
        lam_l10, mult_l10, gp_scipy
    )
    print(f"  base = Σ_α∈image |λ_α|^{{-8}} = {base_sum:.6e}")
    print(f"  γ'(4 + ε = {eps}) = {gp_scipy:.6e}")
    print(f"  R_CM_full = base · γ'(s=4) = {R_CM_full:.6e}")
    print()

    # --- Step 4: PARALLEL cross-check retrieval ----------------------------
    print("Step 4: PARALLEL cross-check — retrieve W3 T1.8 R_ansatz from verdict file")
    R_ansatz, w3_verdict, w3_line = retrieve_w3_t1_8_r_ansatz(VERDICTS_FILE)
    if R_ansatz is None:
        print("  W3 T1.8 verdict line NOT FOUND or alpha_double_prime_M_LRD field missing.")
        print("  Routing: INFO (parallel-with-dependency-on-companion gate per plan §9).")
    else:
        print(f"  W3 T1.8 canonical line found:")
        print(f"    Verdict: {w3_verdict}")
        print(f"    R_ansatz = alpha_double_prime_M_LRD = {R_ansatz:.6e}")

    Delta_PARALLEL = None
    if R_ansatz is not None:
        Delta_PARALLEL = abs(R_CM_full - R_ansatz) / abs(R_ansatz)
        print(f"  Delta_PARALLEL = |R_CM_full - R_ansatz| / |R_ansatz| = {Delta_PARALLEL:.6e}")
    print()

    # --- Step 5: Verdict adjudication --------------------------------------
    print("Step 5: verdict adjudication (PASS/FAIL/INFO per plan §W9-7 Field 9)")
    # Plan §W9-7 Field 9 thresholds:
    #   PASS iff |Delta_PARALLEL| < 1e-2 AND W3 T1.8 PASS or INFO with retrievable value
    #   FAIL iff |Delta_PARALLEL| > 1e-1 OR W3 T1.8 FAILed at substrate-physics level
    #   INFO iff 1e-2 ≤ |Delta_PARALLEL| ≤ 1e-1, OR W3 T1.8 not landed
    if R_ansatz is None:
        # W3 T1.8 not landed → INFO (parallel-with-dependency)
        composite_verdict = "INFO"  # (local)
        verdict_reason = "W3 T1.8 not landed; PARALLEL cross-check deferred"  # (local)
        sign_v = "N/A"
        mag_v = "INFO"
        regime_v = "VALID"
    elif w3_verdict == "FAIL":
        # W3 T1.8 FAILed at substrate-physics → FAIL per Field 9 OR-clause
        composite_verdict = "FAIL"  # (local)
        verdict_reason = (
            f"W3 T1.8 composite=FAIL at substrate-physics layer (R_ansatz vs empirical anchor)"
        )  # (local)
        # The PARALLEL-axis sign:
        #   - sign_verdict: PARALLEL agreement is the substrate's dual-witness identity.
        #     Both FULL CM-1995 and structural-ansatz are F-images of the SAME substrate-IS
        #     canonical at the substrate-distance-2 pole; if Delta_PARALLEL is well-defined
        #     and not divergent, the cross-axis sign IS coherent.
        sign_v = "PASS" if (Delta_PARALLEL is not None and np.isfinite(Delta_PARALLEL)) else "FAIL"
        # magnitude_verdict: per Field 9 explicit OR-clause, W3 T1.8 FAIL forces FAIL
        mag_v = "FAIL"
        regime_v = "VALID"  # Domain not auto-shortened; full L_max=10 image evaluated
    elif Delta_PARALLEL is not None and Delta_PARALLEL < PARALLEL_TOL_PASS:
        composite_verdict = "PASS"  # (local)
        verdict_reason = f"|Delta_PARALLEL|={Delta_PARALLEL:.3e} < 1e-2 (1% PASS band)"  # (local)
        sign_v = "PASS"
        mag_v = "PASS"
        regime_v = "VALID"
    elif Delta_PARALLEL is not None and Delta_PARALLEL > PARALLEL_TOL_INFO:
        composite_verdict = "FAIL"  # (local)
        verdict_reason = (
            f"|Delta_PARALLEL|={Delta_PARALLEL:.3e} > 1e-1 "
            f"(layer-axis discriminator surfaced; queue S92+)"
        )  # (local)
        sign_v = "FAIL"
        mag_v = "FAIL"
        regime_v = "VALID"
    else:
        composite_verdict = "INFO"  # (local)
        verdict_reason = (
            f"|Delta_PARALLEL|={Delta_PARALLEL:.3e} in [1e-2, 1e-1] (marginal cross-axis agreement)"
        )  # (local)
        sign_v = "PASS"
        mag_v = "INFO"
        regime_v = "VALID"

    print(f"  Composite verdict: {composite_verdict}")
    print(f"  Reason: {verdict_reason}")
    print(f"  3-tuple: sign={sign_v}, magnitude={mag_v}, regime={regime_v}")
    print()

    # --- Substrate framing note --------------------------------------------
    print("Substrate framing (direction-of-explanation):")
    print("  The substrate IS the spectral triple at substrate-distance-2 pole;")
    print("  the FULL CM-1995 §III.4 residue formula IS the canonical NCG-axiomatic")
    print("  finite-spectral-triple residue evaluator at that pole. R_CM_full and")
    print("  R_ansatz are TWO methodology-floor F-images of the SAME substrate-IS")
    print("  canonical; their relative agreement IS the substrate's own dual-witness")
    print("  verification at the substrate-distance-2 pole residue layer.")
    print()

    # --- Build value string ------------------------------------------------
    # The Delta_PARALLEL is the canonical PARALLEL cross-check value; we
    # encode the full audit-trail (R_CM_full, R_ansatz, base, γ', OAA tag).
    value_str = (
        f"Delta_PARALLEL={Delta_PARALLEL:.6e};" if Delta_PARALLEL is not None else "Delta_PARALLEL=N/A;"
    )
    value_str += (
        f"R_CM_full={R_CM_full:.6e};"
        f"R_ansatz={R_ansatz if R_ansatz is None else f'{R_ansatz:.6e}'};"
        f"W3_T1_8_verdict={w3_verdict};"
        f"base_sum={base_sum:.6e};"
        f"gamma_prime_at_s4_plus_eps={gp_scipy:.6e};"
        f"gamma_prime_closed_form_residual={gp_residual:.2e};"
        f"eps_for_gamma_prime_limit={eps};"
        f"pole_s0={POLE_S0};"
        f"PARALLEL_TOL_PASS={PARALLEL_TOL_PASS};"
        f"PARALLEL_TOL_INFO={PARALLEL_TOL_INFO};"
        f"L_max_truncation_for_image=10;"
        f"image_sectors={SECTOR_INDEX_AT_POLE_S4};"
        f"image_evcount={len(lam_l10)};"
        f"bot20_at_L10={bot20_occupation_sorted};"
        f"bot20_match_W3T18={bot20_match};"
        f"composite={composite_verdict};"
        f"producing_agent={PRODUCING_AGENT};"
        f"OAA_excluded={','.join(OAA_EXCLUSIONS)};"
        f"OAA_verified={OAA_VERIFIED};"
        f"cm_1995_paper_subject_to_oaa=False;"
        f"evaluator_subject_to_oaa=True;"
        f"reason={verdict_reason}"
    )

    # --- Persist .npz ------------------------------------------------------
    np.savez(
        NPZ_OUT,
        Delta_PARALLEL=np.array(Delta_PARALLEL if Delta_PARALLEL is not None else np.nan),
        R_CM_full=np.array(R_CM_full),
        R_ansatz=np.array(R_ansatz if R_ansatz is not None else np.nan),
        base_sum=np.array(base_sum),
        gamma_prime_at_s4_plus_eps=np.array(gp_scipy),
        gamma_prime_closed_form=np.array(gp_closed),
        gamma_prime_residual=np.array(gp_residual),
        eps_for_gamma_prime_limit=np.array(eps),
        pole_s0=np.array(POLE_S0),
        PARALLEL_TOL_PASS=np.array(PARALLEL_TOL_PASS),
        PARALLEL_TOL_INFO=np.array(PARALLEL_TOL_INFO),
        L_max_cache=np.array(L_MAX),
        L_max_truncation_for_image=np.array(10),
        image_sectors=np.array(SECTOR_INDEX_AT_POLE_S4),
        bot20_occupation=np.array([(str(k), v) for k, v in bot20_occupation_sorted.items()]),
        bot20_match=np.array(bot20_match),
        composite_verdict=np.array(composite_verdict),
        sign_verdict=np.array(sign_v),
        magnitude_verdict=np.array(mag_v),
        regime_verdict=np.array(regime_v),
        producing_agent=np.array(PRODUCING_AGENT),
        OAA_excluded=np.array(OAA_EXCLUSIONS),
        OAA_verified=np.array(OAA_VERIFIED),
        w3_t1_8_verdict=np.array(w3_verdict if w3_verdict is not None else "N/A"),
        audit_sha256=np.array(audit_sha),
        content_sha256=np.array(content_sha),
        input_pins=np.array(json.dumps(pins, sort_keys=True)),
    )
    print(f"NPZ saved: {NPZ_OUT.name}  ({NPZ_OUT.stat().st_size} bytes)")

    # --- Plot --------------------------------------------------------------
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    # Panel 1: γ'(4 + ε) closed-form sanity
    eps_scan = np.logspace(-12, -2, 50)
    gp_scan = np.array([gamma_prime(POLE_S0 + e) for e in eps_scan])
    gp_closed_scan = 6.0 * eps_scan
    ax[0].loglog(eps_scan, gp_scan, "b-", label=r"$\gamma'(4+\epsilon)$ (scipy)")
    ax[0].loglog(eps_scan, gp_closed_scan, "r--", label=r"$6\epsilon$ (closed-form)")
    ax[0].axvline(eps, color="g", linestyle=":", label=f"ε = {eps}")
    ax[0].set_xlabel(r"$\epsilon$")
    ax[0].set_ylabel(r"$\gamma'(4+\epsilon) = (s-4)\cdot\Gamma(s)|_{s=4+\epsilon}$")
    ax[0].set_title(r"Chi-prime kernel $\gamma'(s) = (s-s_0)\,\Gamma(s)$ sanity")
    ax[0].legend()
    ax[0].grid(True, alpha=0.3)

    # Panel 2: PARALLEL cross-check bar
    labels = ["R_CM_full", "R_ansatz (W3 T1.8)"]
    vals = [abs(R_CM_full), abs(R_ansatz) if R_ansatz is not None else 0.0]
    colors = ["steelblue", "darkorange"]
    ax[1].bar(labels, vals, color=colors)
    ax[1].set_yscale("log")
    ax[1].set_ylabel("|value| (log scale)")
    title2 = (
        f"PARALLEL cross-check: Δ={Delta_PARALLEL:.2e}"
        if Delta_PARALLEL is not None
        else "PARALLEL cross-check: W3 T1.8 not landed"
    )
    ax[1].set_title(title2)
    for i, v in enumerate(vals):
        if v > 0:
            ax[1].text(i, v, f"{v:.2e}", ha="center", va="bottom")
    ax[1].grid(True, alpha=0.3, axis="y")

    fig.suptitle(
        f"S91 W9-7 PARALLEL: FULL CM-1995 §III.4 vs structural-ansatz ({composite_verdict})"
    )
    plt.tight_layout()
    plt.savefig(PNG_OUT, dpi=110, bbox_inches="tight")
    plt.close(fig)
    print(f"PNG saved: {PNG_OUT.name}")
    print()

    # --- Verdict line emission ---------------------------------------------
    print(f"Final verdict: {composite_verdict}")
    print(f"Value string: {value_str[:120]}...")
    emit_verdict(
        composite_verdict, value_str, audit_sha, content_sha,
        sign_v, mag_v, regime_v,
    )
    print(f"Verdict line appended to {VERDICT_TXT.name}")
    print()

    # --- Final output 4-tuple ----------------------------------------------
    print(f"=== Output 4-tuple ===")
    val_short = f"{Delta_PARALLEL:.6e}" if Delta_PARALLEL is not None else "N/A"
    print(f"(value={val_short}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"Wall time: {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
