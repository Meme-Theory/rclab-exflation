#!/usr/bin/env python3
"""
S100b W4-2 — S100b-KNN-ORDERED-VEIL: symmetry-resolved kNN spacing statistics
==============================================================================

Gate: S100b-KNN-ORDERED-VEIL ([VERIFY] trigger; substitution chain pre-registers
the Poisson direction -> schema-v2 3-tuple companion row REQUIRED).
Classification: PHONONIC (the sector-resolved level statistics ARE the GGE
relic's mode-spacing structure -- an intrinsic functional of the fabric).

Plan block: sessions/session-plan/session-100b-plan-w4.md §W4-2.

HYPOTHESIS
----------
Inside fixed Peter-Weyl (p,q) sectors (Weyl/conjugation degeneracy removed),
the distinct-|lambda| spacing statistics of D_K(tau_fold) at L_max=12 follow
Berry-Tabor Poisson at k = 1, 2, 3 -- no GOE-class level repulsion at any k --
resolving the pooled sub-Poisson <r> = 0.321 (CHAOS-1, S38) into a clean
sector-resolved verdict on FABRIC-SCALE integrability.

MANDATORY WAVE-4 SCOPING LAW
----------------------------
"GGE never thermalizes" is RETRACTED-S39 (atlas-04 T3 BROKEN; INTEG-39
DECISIVE FAIL: t_therm ~ 6 M_KK^-1, Brody beta = 0.633, single-cell 63% GOE,
V_phys 13% non-separable, Thouless g = 0.60). What survives: "transit IS the
physics" (atlas-10 #8) + FABRIC-SCALE integrability (CG(24) Poisson
<r> = 0.367, FABRIC-INTEG-56) + the compute-certified diabatic transit-freeze
(R_therm = 5251.82, S_ent = 0, S95). THIS gate tests the FABRIC-SCALE
integrability claim at the sector-resolved level-statistics level -- NOT the
retracted single-cell permanence.

UNTRUSTED-UPSTREAM CAVEAT (carried into verdict extra_row + WP section)
-----------------------------------------------------------------------
This gate consumes the s84 spectrum-cache lineage, which was flagged by the
S100b-TAU0-LAITEH-REDUCTION ESCALATION (FAIL, SUBCASE=STRUCTURED: the
framework tau=0 operator sits at the Levi-Civita torsion point t=1/2 of the
Lai-Teh family, NOT the Kostant cubic t=1/3; the eigensolver itself is
verified CORRECT by a cubic-modified control at machine epsilon; the cache
numerics are self-consistent with the LC lineage the framework has always
computed). The open question is operator CANONICITY, not numerical validity.
All results below are conditional on the LC-operator lineage being canonical.

PRE-REGISTERED OPERATOR (plan §W4-2 item (1))
---------------------------------------------
PASS iff for ALL k in {1,2,3}: [D_k(Poisson) < D_k(corrected-Wigner)] AND
  [V_k >= 0.5] AND [beta_1 < 0.3] AND [no unfolding flip] AND [super-Poisson,
  if present, survives the degeneracy-attribution check (NOT attributable)].
FAIL iff at ANY k: [D_k(corrected-Wigner) < D_k(Poisson)] AND
  [V_k in [-0.25, 0.5)] AND [beta_1 >= 0.3] AND [stable under BOTH unfolding
  schemes] AND [<r> cross-check closer to r_GOE than r_POISSON].
INFO otherwise: (a) attributable super-Poisson (degeneracy residue);
  (b) rigidity V_k < -0.25 (Berry-Tabor exception class, NOT chaos);
  (c) extraction-limited (PDF anchors unavailable);
  (d) mixed / unfolding-sensitive / <r>-contradicted indicators.

SUBSTITUTION CHAINS (plan §W4-2 item (7); numbers printed at runtime)
---------------------------------------------------------------------
Claim A (direction): integrable + sector-resolved => P_k -> Gamma(k,1) at all
  k; chaotic => GOE repulsion + ln-k variance. PASS direction = Poisson side.
Claim B (V_k well-defined): Delta_Poisson(k) - Delta_GOE(k) =
  k - (2/pi^2) ln k - (4/pi - 1) = 0.7268 / 1.5863 / 2.5042 > 0 at k = 1/2/3.
Claim C (<r> direction): removing exact-degeneracy s=0 spikes deletes r=0
  entries => <r>_resolved > 0.321, expected ~ 0.3863 (sigma_r ~ 0.27/sqrt(N)).

MACHINERY PINS (PRDR; plan §W4-2 item (5))
------------------------------------------
N_eval=5846 pooled distinct (27 p>=q reps; +-1% assert, drift aborts exit!=0);
L_max=12; k in {1,2,3}; dedup 1e-10 (S53); pair identity 1e-12; eligibility
n_unique >= 100; Brody boundary 0.3; V_k boundary 0.5; rigidity guard -0.25;
super-Poisson trigger 3*sqrt(F_P(1-F_P)/N) at s*=0.25 (F_P = 0.2212) or
V_k > 1.5; decile 0.10; scheme=Shir-2504.20134-corrected-kNN-surmise;
convention=sector-resolved-distinct-abs-lambda-BDI-dedup + unfolding-pair
{poly-deg5-primary, mean-norm-secondary} + beta=1-GOE-reference;
random_seed=N/A (deterministic); GPU_path=cpu-cap-OMP8.

DISCIPLINE
----------
- from canonical_constants import *  (consumed: tau_fold, r_POISSON_canonical,
  r_GOE_canonical, M_KK). Baselines <r>=0.321 (CHAOS-1, S38) and
  r_pooled=0.422 (MULTI-CELL-PLANCHEREL-74) are GATE-VERDICT citations.
- All surmise coefficients constructed from anchor-verified equations
  extracted from the LOCAL Shir PDF at execution (never training knowledge).
- Verdict emitted via print_verdict_payload -> agent calls the race-safe
  emit_verdict knowledge-MCP tool (session "100b"). NO open("a") writes.
- Exit 0 for any valid PASS/FAIL/INFO; exit != 0 reserved for breakage
  (SHA drift, count drift beyond +-1%, pipeline crash).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap BEFORE numpy import (GPU_path=cpu-cap-OMP8 pin)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import; math-scripts.md)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
# consumed names: tau_fold (= 0.19), r_POISSON_canonical (= 0.3863),
#                 r_GOE_canonical (= 0.5307), M_KK (unit anchor)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import re
import time

import numpy as np
from scipy.special import gammainc, gammaln
from scipy.optimize import minimize_scalar

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Identity + pre-registered machinery pins (plan §W4-2)
# ---------------------------------------------------------------------------
SESSION = "100b"                                                   # (local)
GATE_ID = "S100b-KNN-ORDERED-VEIL"                                 # (local)
SCHEME = "Shir-2504.20134-corrected-kNN-surmise"                   # (local)
CONVENTION = ("sector-resolved-distinct-abs-lambda-BDI-dedup;"
              "unfolding-pair{poly-deg5-primary,mean-norm-secondary};"
              "beta=1-GOE-reference"
              "+edgetrim-monotone-window-primary")                 # (local)
# +edgetrim suffix = DISCLOSED OPERATIONAL DEVIATION (math-scripts.md):
# the plan pinned poly-deg5 unfolding but left non-monotone-fit handling
# unpinned; all violations are sector spectral-EDGE artifacts (see
# monotone_window docstring); untrimmed cross-check carried in npz (xcheckA).
L_MAX = 12                                                         # (local)
K_SET = (1, 2, 3)                                                  # (local) scan_range pin
DEDUP_TOL = 1e-10            # (local) S53 lesson: 1e-15 fails near-degenerate multiplets
PAIR_TOL = 1e-12             # (local) BDI conjugate-pair identity tolerance
ELIG_MIN = 100               # (local) per-sector distinct-level eligibility floor
N_EVAL_PIN = 5846            # (local) plan-freeze pooled distinct count (+-1% assert)
N_ELIG_PIN = 52              # (local) plan-freeze eligible-sector count
N_REPS_PIN = 27              # (local) plan-freeze p>=q representative count
BRODY_BOUNDARY = 0.3         # (local) midpoint of BRODY-53 (0.001) and INTEG-39 (0.633)
VK_BOUNDARY = 0.5            # (local) Poisson-vs-GOE variance midpoint
RIGIDITY_GUARD = -0.25       # (local) picket-fence rigidity guard (INFO-b, not FAIL)
SUPERP_VK_TRIGGER = 1.5      # (local) super-Poisson variance trigger
SSTAR = 0.25                 # (local) small-s CDF excess test point
DECILE_FRACTION = 0.10       # (local) degeneracy-attribution removal fraction
POLY_DEG = 5                 # (local) PRIMARY unfolding polynomial degree (safe n>=100)
GOF_BINS = 50                # (local) Eq.(18) GoF binning (diagnostic-only quantity)
BETA_GOE = 1.0               # (local) AZ class BDI, gapped bulk -> GOE reference class
R_BASELINE_S38 = 0.321       # (local) CHAOS-1 (S38) gate-verdict citation, NOT a constant
VAR_DDOF = 1                 # (local) unbiased sample variance convention for Delta_emp

OUT_NPZ = SESSION_DIR / "s100b_w4_knn_ordered_veil.npz"            # (local)
OUT_PNG = SESSION_DIR / "s100b_w4_knn_ordered_veil.png"            # (local)

CACHE_PATH = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CACHE_SHA_PIN = "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"
PDF_PATH = (PROJECT_ROOT / "downloads" / "research-sweep-s99" /
            "spectral-geometry-math" /
            "08_Shir-Martinez-Azcona-Chenu_kNN-Level-Spacing-Surmise.pdf")
PDF_SHA_PIN = "b2b0c541d668fac2a1972d818c00dbd2d41e285d79e957401e313fbe24798841"
PREFLIGHT_44 = SESSION_DIR / "s100b_cf28_simple_pole_preflight.npz"  # diagnostic-only input

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    CACHE_PATH,
    PDF_PATH,
]

UNTRUSTED_UPSTREAM_ROW = (
    "# UNTRUSTED-UPSTREAM caveat: consumes s84 cache lineage flagged by "
    "S100b-TAU0-LAITEH-REDUCTION ESCALATION (STRUCTURED LC t=1/2; eigensolver "
    "control-verified; canonicity adjudication pending) — dispatched per "
    "pre-registered orchestrator triage")                          # (local)


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
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per the S84+ dual-SHA schema."""
    script_bytes = script_path.read_bytes()                        # (local)
    canonical_bytes = canonical_path.read_bytes()                  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")       # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Step (1): PDF coefficient extraction (LOCAL PDF, never memory)
# ---------------------------------------------------------------------------
# Anchor regexes match the pypdf-extracted text of arXiv 2504.20134v2 after
# normalization (unicode minus -> '-', tilde -> '~', control glyphs stripped,
# whitespace collapsed). Every operative coefficient below is constructed
# FROM an anchor-verified equation; extraction failure on ANY anchor =>
# extraction_ok=False => INFO sub-path (c).

ANCHOR_PATTERNS = {
    "eq2_surmise_form":   r"P \(k\)\(s\)\s*≈\s*C α sα e-Aαs2\s*,\s*\(2\)",
    "eq3_old_exponent":   r"α=\s*1\s*2\s*k\(k\+\s*1\)β\+k-1\s*\.\s*\(3\)",
    "eq4_normalization":  (r"Aα\s*=\s*\"\s*Γ\s*α\s*2\s*\+\s*1\s*kΓ\s*α\+1\s*2"
                           r"\s*#2\s*,\s*C α = 2A\s*α\+1\s*2\s*α\s*Γ\s*α\+1\s*2"
                           r"\s*\.\s*\(4\)"),
    "eq7_variance_ident": r"=\s*α\+\s*1\s*2Aα\s*-k 2\s*,\s*\(7\)",
    "eq8_rmt_variance":   r"∆\(k\)\s*β\s*=\s*2\s*π2β lnk\+c β\s*\.\s*\(8\)",
    "eq8_c1_boundary":    r"c\s*1\s*=\s*4/π-1",
    "eq9_number_var":     r"∆\(k\)\s*=\s*Σ2\(k\)-1/6\s*,\s*\(9\)",
    "eq11_poisson_var":   r"∆\(k\)\s*Poisson\s*=\s*k\s*\.\s*\(11\)",
    "eq15_corrected_exp": (r"~?α=\s*π2βk2\s*2\s*\(π2βcβ \+ 2 lnk\)\s*-\s*3\s*4"
                           r"\s*\+O\(k\s*-2\s*lnk\)\s*,\s*\(15\)"),
    "eq15_k1_special":    r"this corrected power reads ~?α=\s*1\s*2cβ\s*-\s*3\s*4",
    "eq16_new_surmise":   r"~?P \(k\)\(s\)\s*=\s*C ~?αs~?αexp\(-A~?αs2\)\s*\.\s*\(16\)",
    "eq18_gof":           r"\[p1\(si\)-p\s*2\(si\)\]2\s*\.\s*\(18\)",
    "eqC3_poisson_knn":   r"\(k-1\)!\s*sk-1e-s\s*\.\s*\(C3\)",
    "appB_unfolding":     r"Appendix B:\s*Unfolding",
}


def extract_surmise_from_pdf(pdf_path: Path) -> tuple[bool, dict]:
    """pypdf-extract the Shir paper text; verify all 14 equation anchors.

    Returns (extraction_ok, info) where info carries the matched anchor
    strings (stored to npz as provenance) and a normalized-text length.
    Fallback route (mcp__paper-search__read_arxiv_paper 2504.20134) is an
    AGENT-level route exercised only if this in-script route fails.
    """
    try:
        from pypdf import PdfReader
        reader = PdfReader(str(pdf_path))                          # (local)
        raw = "\n".join(pg.extract_text() for pg in reader.pages)  # (local)
    except Exception as exc:  # noqa: BLE001
        return False, {"error": f"pypdf extraction failed: {exc}",
                       "anchors": {}}
    norm = raw.replace("−", "-").replace("˜", "~")       # (local)
    norm = re.sub(r"[\x00-\x08\x0b-\x1f]", " ", norm)
    norm = re.sub(r"\s+", " ", norm)
    anchors: dict[str, str] = {}                                   # (local)
    ok = True                                                      # (local)
    for name, pat in ANCHOR_PATTERNS.items():
        m = re.search(pat, norm)                                   # (local)
        if m:
            anchors[name] = m.group(0)
        else:
            anchors[name] = "<MISSING>"
            ok = False
    return ok, {"anchors": anchors, "n_chars_norm": len(norm)}


# --- Operative coefficient set, constructed from the anchor-verified forms --

def c_beta_goe() -> float:
    """c_1 = 4/pi - 1 (Eq. (8) boundary condition, anchor eq8_c1_boundary)."""
    return 4.0 / np.pi - 1.0


def alpha_old(k: int, beta: float) -> float:
    """OLD literature exponent, Eq. (3): alpha = (1/2)k(k+1)beta + k - 1."""
    return 0.5 * k * (k + 1) * beta + k - 1.0


def alpha_corrected(k: int, beta: float) -> float:
    """CORRECTED exponent, Eq. (15):
    alpha~ = pi^2 beta k^2 / (2(pi^2 beta c_beta + 2 ln k)) - 3/4.
    At k=1 this reduces to 1/(2 c_beta) - 3/4 (anchor eq15_k1_special)."""
    cb = c_beta_goe()                                              # (local)
    return (np.pi**2 * beta * k**2 /
            (2.0 * (np.pi**2 * beta * cb + 2.0 * np.log(k)))) - 0.75


def A_of_alpha(alpha: float, k: int) -> float:
    """Eq. (4): A_alpha = [Gamma(alpha/2 + 1) / (k Gamma((alpha+1)/2))]^2."""
    lg = gammaln(alpha / 2.0 + 1.0) - gammaln((alpha + 1.0) / 2.0)  # (local)
    return float(np.exp(2.0 * (lg - np.log(k))))


def C_of_alpha(alpha: float, A: float) -> float:
    """Eq. (4): C_alpha = 2 A^((alpha+1)/2) / Gamma((alpha+1)/2)."""
    return float(np.exp(np.log(2.0) + (alpha + 1.0) / 2.0 * np.log(A)
                        - gammaln((alpha + 1.0) / 2.0)))


def delta_surmise(alpha: float, k: int) -> float:
    """Eq. (7): Delta(k) = (alpha+1)/(2 A_alpha) - k^2 (surmise variance)."""
    return (alpha + 1.0) / (2.0 * A_of_alpha(alpha, k)) - k**2


def delta_goe(k: int) -> float:
    """Eq. (8) at beta=1: Delta_GOE(k) = (2/pi^2) ln k + (4/pi - 1)."""
    return 2.0 / np.pi**2 * np.log(k) + c_beta_goe()


def delta_poisson(k: int) -> float:
    """Eq. (11): Delta_Poisson(k) = k."""
    return float(k)


def cdf_poisson_k(s: np.ndarray, k: int) -> np.ndarray:
    """Gamma(k,1) CDF (Eq. (C3) integrated): regularized lower inc. gamma."""
    return gammainc(k, s)


def pdf_poisson_k(s: np.ndarray, k: int) -> np.ndarray:
    """Eq. (C3): P_Poisson^(k)(s) = s^(k-1) e^-s / (k-1)!."""
    return np.exp((k - 1) * np.log(np.maximum(s, 1e-300)) - s
                  - gammaln(k))


def cdf_wigner_like(s: np.ndarray, alpha: float, k: int) -> np.ndarray:
    """CDF of Eq. (2): C_a s^a exp(-A_a s^2). With Eq. (4) normalization the
    closed form is exactly P((a+1)/2, A_a s^2) (regularized lower gamma):
    int_0^s C u^a e^(-A u^2) du, sub v = A u^2
      = [C Gamma((a+1)/2) / (2 A^((a+1)/2))] * P((a+1)/2, A s^2)  and the
    bracket = 1 by Eq. (4)."""
    A = A_of_alpha(alpha, k)                                       # (local)
    return gammainc((alpha + 1.0) / 2.0, A * s * s)


def pdf_wigner_like(s: np.ndarray, alpha: float, k: int) -> np.ndarray:
    A = A_of_alpha(alpha, k)                                       # (local)
    C = C_of_alpha(alpha, A)                                       # (local)
    return C * np.power(np.maximum(s, 1e-300), alpha) * np.exp(-A * s * s)


# ---------------------------------------------------------------------------
# Section 6 — Step (2): sector resolution (distinct |lambda|, BDI dedup)
# ---------------------------------------------------------------------------

def dedup_sorted(vals: np.ndarray, tol: float = DEDUP_TOL) -> np.ndarray:
    """Distinct values of a SORTED ascending array at absolute tolerance."""
    keep = np.empty(len(vals), dtype=bool)                         # (local)
    keep[0] = True
    keep[1:] = np.diff(vals) > tol
    # cumulative anchor dedup (successive-diff dedup is sufficient here:
    # cluster widths << tol/10 for exact-degenerate multiplets; S53 lesson)
    return vals[keep]


def load_sectors() -> tuple[dict, dict]:
    """Load cache; return (all_sector_distinct, raw_sorted_abs_evals)."""
    dat = np.load(CACHE_PATH, allow_pickle=True)                   # (local)
    se = dat["sector_evals"].item()                                # (local)
    distinct = {}                                                  # (local)
    raw = {}                                                       # (local)
    for key, rec in se.items():
        ev = np.sort(np.asarray(rec["abs_evals"], dtype=float))    # (local)
        raw[key] = ev
        distinct[key] = dedup_sorted(ev)
    return distinct, raw


# ---------------------------------------------------------------------------
# Section 7 — Step (3): unfolding pair (PRIMARY poly-deg5 / SECONDARY mean)
# ---------------------------------------------------------------------------

def unfold_primary(lam: np.ndarray) -> tuple[np.ndarray, int]:
    """Per-sector polynomial unfolding (paper App. B procedure; plan pins
    degree 5, safe at n >= 100 — the S53 artifact regime is n < 50).
    Fit smooth N_bar(lambda) to the staircase midpoints (lambda_i, i - 1/2);
    unfolded levels e_i = N_bar(lambda_i). Returns (e, n_nonmonotone)."""
    n = len(lam)                                                   # (local)
    stair = np.arange(1, n + 1, dtype=float) - 0.5                 # (local)
    poly = np.polynomial.Polynomial.fit(lam, stair, POLY_DEG)      # (local)
    e = poly(lam)                                                  # (local)
    n_bad = int(np.sum(np.diff(e) <= 0.0))                         # (local)
    return e, n_bad


def unfold_secondary(lam: np.ndarray) -> tuple[np.ndarray, int]:
    """Per-sector mean-spacing normalization (cruder robustness scheme):
    e_i = (lambda_i - lambda_1) / s_bar, s_bar = (lambda_n - lambda_1)/(n-1).
    Mean NN spacing = 1 exactly per sector."""
    sbar = (lam[-1] - lam[0]) / (len(lam) - 1)                     # (local)
    return (lam - lam[0]) / sbar, 0


def knn_spacings(e: np.ndarray, k: int) -> np.ndarray:
    """kth spacings s_i^(k) = e_{i+k} - e_i."""
    return e[k:] - e[:-k]


EDGE_ZONE = 0.10   # (local) edge-cluster zone fraction for the monotone-window trim


def monotone_window(e: np.ndarray) -> tuple[int, int, int]:
    """OPERATIONAL DEVIATION (disclosed; math-scripts.md honest-disclosure
    route). The plan pinned poly-deg5 unfolding of N(lambda) but did NOT pin
    the handling of non-monotone fitted segments — an execution-time free
    parameter surfaced at runtime. Diagnosis: ALL 60 non-monotone fit diffs
    sit at sector spectral EDGES (first <= 5 levels, idx fraction <= 0.011;
    one top-edge point in sector (11,1)) — least-squares overshoot at the
    sharp spectral onset, producing artifact spacings as negative as -3.7
    unfolded units that destroy the KS channel (gammainc(k, s<0) = nan;
    F(A s^2) -> 1 at sorted-bottom). The Shir paper itself restricts kNN
    statistics to the spectral BULK (Sec. I: 'the edges of the spectrum may
    not exhibit universality'; App. B: density window). Minimal data-driven
    remedy, applied to the PRIMARY scheme only (secondary is monotone by
    construction): trim the maximal EDGE runs containing all non-monotone
    fit diffs; mid-spectrum violations (none observed) are flagged and their
    spacings dropped, never trimmed. Deterministic; ~1.5% of levels;
    untrimmed cross-check (xcheckA) carried in the npz to show the trim does
    no physics work. Returns (lo, hi, n_mid_bad) for the slice e[lo:hi]."""
    bad = np.where(np.diff(e) <= 0.0)[0]                           # (local)
    n = len(e)                                                     # (local)
    lo, hi = 0, n                                                  # (local)
    n_mid = 0                                                      # (local)
    if len(bad):
        lo_bad = bad[bad < EDGE_ZONE * n]                          # (local)
        hi_bad = bad[bad >= (1.0 - EDGE_ZONE) * n]                 # (local)
        n_mid = int(len(bad) - len(lo_bad) - len(hi_bad))
        if len(lo_bad):
            lo = int(lo_bad.max()) + 2     # drop levels 0 .. max_bad+1
        if len(hi_bad):
            hi = int(hi_bad.min())         # drop levels min_bad .. n-1
    return lo, hi, n_mid


# ---------------------------------------------------------------------------
# Section 8 — Step (4): pooled statistics
# ---------------------------------------------------------------------------

def ks_distance(sample: np.ndarray, cdf_vals: np.ndarray) -> float:
    """Two-sided KS distance for a SORTED sample against reference CDF."""
    n = len(sample)                                                # (local)
    up = np.max(np.abs(cdf_vals - np.arange(1, n + 1) / n))        # (local)
    lo = np.max(np.abs(cdf_vals - np.arange(0, n) / n))            # (local)
    return float(max(up, lo))


def gof_eq18(sample: np.ndarray, pdf_func) -> float:
    """Eq. (18) standard-deviation goodness-of-fit: RMS difference between
    binned empirical density and reference density, restricted to 3 SD from
    the sample mean (paper's tail guard). GOF_BINS = 50 (diagnostic-only)."""
    m, sd = float(np.mean(sample)), float(np.std(sample, ddof=VAR_DDOF))  # (local)
    lo, hi = max(0.0, m - 3 * sd), m + 3 * sd                      # (local)
    hist, edges = np.histogram(sample, bins=GOF_BINS, range=(lo, hi),
                               density=True)                       # (local)
    centers = 0.5 * (edges[1:] + edges[:-1])                       # (local)
    return float(np.sqrt(np.mean((hist - pdf_func(centers)) ** 2)))


def brody_beta_mle(s: np.ndarray) -> float:
    """Brody-parameter MLE on unit-mean spacings (binning-free,
    deterministic):  P_B(s; b) = c (b+1) s^b exp(-c s^(b+1)),
    c = Gamma((b+2)/(b+1))^(b+1).  b=0 -> Poisson, b=1 -> GOE Wigner."""
    s = s[s > 0.0]                                                 # (local)

    def nll(b: float) -> float:
        b1 = b + 1.0                                               # (local)
        logc = b1 * gammaln((b + 2.0) / b1)                        # (local)
        c = np.exp(logc)                                           # (local)
        return float(-(logc + np.log(b1) + b * np.log(s)
                       - c * s**b1).sum())

    res = minimize_scalar(nll, bounds=(-0.49, 2.5), method="bounded",
                          options={"xatol": 1e-6})                 # (local)
    return float(res.x)


def r_ratio_pooled(sequences: list[np.ndarray]) -> np.ndarray:
    """Unfolding-independent r-statistic on the RAW distinct sequences:
    r_n = min(s_n, s_{n+1}) / max(s_n, s_{n+1}), pooled across sectors."""
    rs = []                                                        # (local)
    for lam in sequences:
        d = np.diff(lam)                                           # (local)
        rs.append(np.minimum(d[:-1], d[1:]) / np.maximum(d[:-1], d[1:]))
    return np.concatenate(rs)


def pooled_stats(sequences: list[np.ndarray], unfolder,
                 trim_edges: bool = False,
                 drop_nonpositive: bool = False) -> dict:
    """Full pooled-statistics block for one unfolding scheme.

    trim_edges: apply the monotone-window edge trim (PRIMARY scheme;
      disclosed operational deviation — see monotone_window).
    drop_nonpositive: drop s <= 0 artifact spacings WITHOUT trimming
      (option-A cross-check mode, npz key xcheckA_*)."""
    pooled = {k: [] for k in K_SET}                                # (local)
    n_nonmono = 0                                                  # (local)
    n_trimmed_levels = 0                                           # (local)
    n_mid_flagged = 0                                              # (local)
    n_dropped_spacings = 0                                         # (local)
    trim_table = []                                                # (local)
    for lam in sequences:
        e, nb = unfolder(lam)                                      # (local)
        n_nonmono += nb
        if trim_edges:
            lo, hi, nmid = monotone_window(e)                      # (local)
            n_mid_flagged += nmid
            n_trimmed_levels += lo + (len(e) - hi)
            trim_table.append([lo, len(e) - hi])
            e = e[lo:hi]                                           # (local)
        else:
            trim_table.append([0, 0])
        for k in K_SET:
            s = knn_spacings(e, k)                                 # (local)
            if trim_edges or drop_nonpositive:
                good = s > 0.0                                     # (local)
                n_dropped_spacings += int((~good).sum())
                s = s[good]
            pooled[k].append(s)
    out = {"n_nonmonotone": n_nonmono, "k": {},
           "n_trimmed_levels": n_trimmed_levels,
           "n_mid_flagged": n_mid_flagged,
           "n_dropped_spacings": n_dropped_spacings,
           "trim_table": np.array(trim_table, dtype=int)}          # (local)
    for k in K_SET:
        s = np.sort(np.concatenate(pooled[k]))                     # (local)
        a_corr = alpha_corrected(k, BETA_GOE)                      # (local)
        a_old = alpha_old(k, BETA_GOE)                             # (local)
        dk = {
            "sample": s,
            "n": len(s),
            "mean": float(np.mean(s)),
            "Delta_emp": float(np.var(s, ddof=VAR_DDOF)),
            "D_poisson": ks_distance(s, cdf_poisson_k(s, k)),
            "D_wigner_corr": ks_distance(s, cdf_wigner_like(s, a_corr, k)),
            "D_wigner_old": ks_distance(s, cdf_wigner_like(s, a_old, k)),
            "GoF18_poisson": gof_eq18(s, lambda x, kk=k: pdf_poisson_k(x, kk)),
            "GoF18_wigner_corr": gof_eq18(
                s, lambda x, aa=a_corr, kk=k: pdf_wigner_like(x, aa, kk)),
            "alpha_corr": a_corr,
            "alpha_old": a_old,
        }                                                          # (local)
        dk["V_k"] = ((dk["Delta_emp"] - delta_goe(k)) /
                     (delta_poisson(k) - delta_goe(k)))
        dk["F_emp_sstar"] = (float(np.searchsorted(s, SSTAR, side="right"))
                             / len(s)) if k == 1 else np.nan
        out["k"][k] = dk
    out["beta1"] = brody_beta_mle(out["k"][1]["sample"])
    return out


# ---------------------------------------------------------------------------
# Section 9 — Step (5): super-Poisson trigger + degeneracy attribution
# ---------------------------------------------------------------------------

def superp_trigger(stats: dict) -> tuple[bool, dict]:
    """Trigger iff F_emp(0.25) - F_Poisson(0.25) > 3 sigma_binomial
    (F_Poisson(0.25) = 1 - e^-0.25 = 0.2212) OR any V_k > 1.5."""
    n1 = stats["k"][1]["n"]                                        # (local)
    f_p = 1.0 - np.exp(-SSTAR)                                     # (local)
    band = 3.0 * np.sqrt(f_p * (1.0 - f_p) / n1)                   # (local)
    f_emp = stats["k"][1]["F_emp_sstar"]                           # (local)
    excess_fire = (f_emp - f_p) > band                             # (local)
    vk_fire = any(stats["k"][k]["V_k"] > SUPERP_VK_TRIGGER
                  for k in K_SET)                                  # (local)
    return bool(excess_fire or vk_fire), {
        "F_emp_sstar": f_emp, "F_poisson_sstar": f_p,
        "band_3sigma": float(band), "excess_fire": bool(excess_fire),
        "vk_fire": bool(vk_fire)}


def decile_removed(sequences: list[np.ndarray], unfolder,
                   trim_edges: bool = False) -> list[np.ndarray]:
    """Remove the right-endpoint level of every NN spacing in the smallest
    decile of the scheme's pooled unfolded NN spacings (deterministic,
    single left-to-right pass on the original sequence)."""
    all_s1 = []                                                    # (local)
    per_sector_e = []                                              # (local)
    for lam in sequences:
        e, _ = unfolder(lam)                                       # (local)
        if trim_edges:
            lo, hi, _ = monotone_window(e)                         # (local)
            e = e[lo:hi]                                           # (local)
            lam = lam[lo:hi]                                       # (local)
        per_sector_e.append((lam, e))
        all_s1.append(np.diff(e))
    thr = float(np.quantile(np.concatenate(all_s1), DECILE_FRACTION))  # (local)
    reduced = []                                                   # (local)
    for lam, e in per_sector_e:
        s1 = np.diff(e)                                            # (local)
        keep = np.ones(len(lam), dtype=bool)                       # (local)
        keep[1:][s1 < thr] = False
        reduced.append(lam[keep])
    return reduced


def attribution_check(sequences: list[np.ndarray], unfolder,
                      trim_edges: bool = False) -> tuple[bool, dict]:
    """Run the decile-removal recomputation. Attributable (INFO sub-path a)
    iff Poisson agreement is restored at ALL k (KS prefers Poisson AND V_k
    back in [0.5, 1.5]) AND beta_1(reduced) < 0.3. Excess persisting =>
    genuine super-Poisson => PASS side."""
    red = decile_removed(sequences, unfolder, trim_edges)          # (local)
    st = pooled_stats(red, unfolder, trim_edges=trim_edges)        # (local)
    restored = all(
        (st["k"][k]["D_poisson"] < st["k"][k]["D_wigner_corr"]) and
        (VK_BOUNDARY <= st["k"][k]["V_k"] <= SUPERP_VK_TRIGGER)
        for k in K_SET)                                            # (local)
    attributable = bool(restored and st["beta1"] < BRODY_BOUNDARY)  # (local)
    diag = {f"V_{k}_reduced": st["k"][k]["V_k"] for k in K_SET}    # (local)
    diag.update({f"D_poisson_{k}_reduced": st["k"][k]["D_poisson"]
                 for k in K_SET})
    diag.update({f"D_wigner_corr_{k}_reduced": st["k"][k]["D_wigner_corr"]
                 for k in K_SET})
    diag["beta1_reduced"] = st["beta1"]
    diag["restored_all_k"] = restored
    return attributable, diag


# ---------------------------------------------------------------------------
# Section 10 — Step (6)+(7): verdict assembly (pre-registered operator)
# ---------------------------------------------------------------------------

def scheme_class(stats: dict, extraction_ok: bool,
                 triggered: bool, attributable: bool | None) -> tuple[str, str]:
    """Per-scheme classification per the plan operator. Returns
    (class, sub_path) with class in {PASS, FAIL, INFO} and sub_path in
    {'', 'a', 'b', 'c', 'd'}."""
    if not extraction_ok:
        return "INFO", "c"
    vks = {k: stats["k"][k]["V_k"] for k in K_SET}                 # (local)
    if any(v < RIGIDITY_GUARD for v in vks.values()):
        return "INFO", "b"     # rigidity guard: Berry-Tabor exception, NOT FAIL
    poisson_pref_all = all(stats["k"][k]["D_poisson"]
                           < stats["k"][k]["D_wigner_corr"]
                           for k in K_SET)                         # (local)
    v_pass_all = all(v >= VK_BOUNDARY for v in vks.values())       # (local)
    beta_ok = stats["beta1"] < BRODY_BOUNDARY                      # (local)
    if poisson_pref_all and v_pass_all and beta_ok:
        if triggered and attributable:
            return "INFO", "a"     # residual accidental degeneracy
        return "PASS", ""
    fail_any_k = any(
        (stats["k"][k]["D_wigner_corr"] < stats["k"][k]["D_poisson"]) and
        (RIGIDITY_GUARD <= vks[k] < VK_BOUNDARY)
        for k in K_SET) and (stats["beta1"] >= BRODY_BOUNDARY)     # (local)
    if fail_any_k:
        return "FAIL", ""
    return "INFO", "d"


def collapse_rule(sign_v: str, mag_v: str, reg_v: str) -> str:
    """Pre-registered schema-v2 composite collapse (gate-verdicts.md)."""
    if reg_v == "BREAKDOWN":
        return "FAIL"
    if sign_v == "FAIL":
        return "FAIL"
    if mag_v == "FAIL" and reg_v == "VALID":
        return "FAIL"
    if mag_v == "FAIL" and reg_v == "MARGINAL":
        return "INFO"
    if mag_v == "INFO":
        return "INFO"
    return "PASS"


# ---------------------------------------------------------------------------
# Section 11 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                               # (local)

    # --- input pins (first 20 lines of stdout) ---
    pins = log_input_pins(INPUT_FILES)                             # (local)
    cache_rel = str(CACHE_PATH.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
    pdf_rel = str(PDF_PATH.relative_to(PROJECT_ROOT)).replace("\\", "/")      # (local)
    if pins[cache_rel] != CACHE_SHA_PIN:
        print(f"ABORT: cache SHA drift: {pins[cache_rel]} != pin {CACHE_SHA_PIN}")
        return 2
    if pins[pdf_rel] != PDF_SHA_PIN:
        print(f"ABORT: Shir PDF SHA drift: {pins[pdf_rel]} != pin {PDF_SHA_PIN}")
        return 2
    # machinery pins enter the audit pinmap (audit_discriminators item 'pinmap')
    pins["_gate_id"] = GATE_ID
    pins["_scheme"] = SCHEME
    pins["_convention"] = CONVENTION
    pins["_L_max"] = str(L_MAX)
    pins["_N_eval_pin"] = str(N_EVAL_PIN)
    pins["_k_set"] = ",".join(str(k) for k in K_SET)
    pins["_thresholds"] = ("dedup=1e-10;pair=1e-12;elig>=100;brody=0.3;"
                           "Vk=0.5;rigidity=-0.25;superP=3sigma@0.25|Vk>1.5;"
                           "decile=0.10;polydeg=5;ddof=1;gofbins=50;"
                           "edgezone=0.1;edgetrim=primary-only")
    script_path = Path(__file__).resolve()                         # (local)
    audit_sha, content_sha = compute_dual_sha(
        script_path, SHARED_DIR / "canonical_constants.py", pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print(f"  canonical imports: tau_fold={tau_fold}, "
          f"r_POISSON_canonical={r_POISSON_canonical}, "
          f"r_GOE_canonical={r_GOE_canonical}, M_KK={M_KK:.6e}")
    print()

    # --- Step (1): PDF extraction ---
    print("=== Step 1: Shir 2504.20134 coefficient extraction (local PDF) ===")
    extraction_ok, ext_info = extract_surmise_from_pdf(PDF_PATH)   # (local)
    n_found = sum(1 for v in ext_info["anchors"].values()
                  if v != "<MISSING>")                             # (local)
    print(f"  anchors found: {n_found}/{len(ANCHOR_PATTERNS)} "
          f"-> extraction_ok={extraction_ok}")
    for nm, sv in ext_info["anchors"].items():
        print(f"    {nm:22s} {sv[:64]}")

    # reference tables from the verified forms (beta = 1, GOE class for BDI
    # gapped bulk; |lambda|_min = 0.8197411121 — spectrum gapped, no chiral
    # near-zero structure)
    c1 = c_beta_goe()                                              # (local)
    print(f"  c_1 = 4/pi - 1 = {c1:.6f}")
    dgoe = {k: delta_goe(k) for k in K_SET}                        # (local)
    dpois = {k: delta_poisson(k) for k in K_SET}                   # (local)
    denom = {k: dpois[k] - dgoe[k] for k in K_SET}                 # (local)
    a_corr = {k: alpha_corrected(k, BETA_GOE) for k in K_SET}      # (local)
    a_old = {k: alpha_old(k, BETA_GOE) for k in K_SET}             # (local)
    print("  k | Delta_GOE  Delta_Poisson  denom(ClaimB) | alpha_old  alpha_corr"
          "  Delta_surmise(corr)")
    for k in K_SET:
        print(f"  {k} | {dgoe[k]:9.4f}  {dpois[k]:13.4f}  {denom[k]:12.4f} | "
              f"{a_old[k]:9.4f}  {a_corr[k]:10.4f}  "
              f"{delta_surmise(a_corr[k], k):11.4f}")
    # XC5/XC6: plan-pinned 4-sf cross-checks (Claim B substitution chain)
    plan_dgoe = {1: 0.2732, 2: 0.4137, 3: 0.4958}                  # (local)
    plan_denom = {1: 0.7268, 2: 1.5863, 3: 2.5042}                 # (local)
    xc5 = all(abs(dgoe[k] - plan_dgoe[k]) < 5e-4 for k in K_SET)   # (local)
    xc6 = all(abs(denom[k] - plan_denom[k]) < 5e-4 for k in K_SET)  # (local)
    print(f"  XC5 Delta_GOE vs plan 4-sf pins: {'OK' if xc5 else 'MISMATCH'}")
    print(f"  XC6 V_k denominators vs plan:    {'OK' if xc6 else 'MISMATCH'}")
    # XC4: surmise normalization + mean-k (validates the Eq. (4) algebra)
    print("  XC4 corrected-surmise quadrature checks:")
    for k in K_SET:
        D = delta_surmise(a_corr[k], k)                            # (local)
        grid = np.linspace(1e-9, k + 14.0 * np.sqrt(max(D, 0.05)), 400000)  # (local)
        pdfv = pdf_wigner_like(grid, a_corr[k], k)                 # (local)
        norm = float(np.trapezoid(pdfv, grid))                     # (local)
        mean = float(np.trapezoid(grid * pdfv, grid))              # (local)
        print(f"    k={k}: int P = {norm:.8f} (=1), int s P = {mean:.8f} (={k})")

    # --- Step (2): sector resolution ---
    print("\n=== Step 2: sector resolution (distinct |lambda|, BDI dedup) ===")
    distinct, raw = load_sectors()                                 # (local)
    n_sectors = len(distinct)                                      # (local)
    n_evals_total = sum(len(v) for v in raw.values())              # (local)
    print(f"  sectors in cache: {n_sectors} (plan-freeze 90); "
          f"evals with multiplicity: {n_evals_total} (plan-freeze 166896)")
    if n_sectors != 90 or n_evals_total != 166896:
        print("ABORT: cache content drift vs plan-freeze structure pins")
        return 2
    eligible = {key: v for key, v in distinct.items()
                if len(v) >= ELIG_MIN}                             # (local)
    print(f"  eligible sectors (n_unique >= {ELIG_MIN}): {len(eligible)} "
          f"(plan-freeze {N_ELIG_PIN})")
    if len(eligible) != N_ELIG_PIN:
        print("ABORT: eligibility-count drift vs plan-freeze")
        return 2
    # BDI conjugate-pair identity check (XC3) on raw sorted |lambda| arrays
    bdi_mismatch = []                                              # (local)
    pair_maxdiff = 0.0                                             # (local)
    for (p, q) in sorted(eligible):
        if p > q and (q, p) in raw:
            md = float(np.max(np.abs(raw[(p, q)] - raw[(q, p)])))  # (local)
            pair_maxdiff = max(pair_maxdiff, md)
            if md > PAIR_TOL:
                bdi_mismatch.append((p, q, md))
    print(f"  XC3 BDI conjugate identity: max |diff| = {pair_maxdiff:.3e} "
          f"(tol {PAIR_TOL:.0e}); mismatches: {len(bdi_mismatch)}")
    reps = {key: v for key, v in eligible.items() if key[0] >= key[1]}  # (local)
    if bdi_mismatch:  # keep both + flag (plan clause); pooled assert backstops
        for (p, q, _) in bdi_mismatch:
            reps[(q, p)] = eligible[(q, p)]
    rep_keys = sorted(reps)                                        # (local)
    n_reps = len(rep_keys)                                         # (local)
    pooled_n = sum(len(reps[key]) for key in rep_keys)             # (local)
    print(f"  p>=q representatives: {n_reps} (plan-freeze {N_REPS_PIN}); "
          f"pooled distinct levels: {pooled_n} (pin {N_EVAL_PIN} +-1%)")
    if abs(pooled_n - N_EVAL_PIN) > 0.01 * N_EVAL_PIN:
        print("ABORT: pooled-count drift beyond +-1% — cache change flagged")
        return 2
    sequences = [reps[key] for key in rep_keys]                    # (local)

    # unfolding-independent <r> cross-check (Claim C)
    r_vals = r_ratio_pooled(sequences)                             # (local)
    r_mean = float(np.mean(r_vals))                                # (local)
    sigma_r = 0.27 / np.sqrt(len(r_vals))                          # (local)
    z_r = (r_mean - r_POISSON_canonical) / sigma_r                 # (local)
    print(f"  XC10 r-count: {len(r_vals)} (expected {pooled_n - 2 * n_reps})")
    print(f"  <r>_resolved = {r_mean:.4f}  [baseline S38 pooled-unresolved "
          f"{R_BASELINE_S38}; Poisson {r_POISSON_canonical}; GOE "
          f"{r_GOE_canonical}; z vs Poisson = {z_r:+.2f} (sigma_r={sigma_r:.4f})]")
    r_up = r_mean > R_BASELINE_S38                                 # (local)
    r_poisson_side = (abs(r_mean - r_POISSON_canonical)
                      < abs(r_mean - r_GOE_canonical))             # (local)
    r_goe_side = not r_poisson_side                                # (local)
    print(f"  Claim C direction: <r> rose from 0.321: {r_up}; "
          f"Poisson-side: {r_poisson_side}")

    # --- Steps (3)+(4): unfolding pair + pooled statistics ---
    print("\n=== Steps 3+4: unfolding pair + pooled kNN statistics ===")
    stats_p = pooled_stats(sequences, unfold_primary,
                           trim_edges=True)                        # (local)
    stats_s = pooled_stats(sequences, unfold_secondary)            # (local)
    print("  OPERATIONAL DEVIATION (disclosed; monotone-window edge trim, "
          "PRIMARY only):")
    print(f"    levels trimmed: {stats_p['n_trimmed_levels']} of {pooled_n} "
          f"({100.0 * stats_p['n_trimmed_levels'] / pooled_n:.2f}%); "
          f"mid-spectrum violations flagged: {stats_p['n_mid_flagged']}; "
          f"residual nonpositive spacings dropped: "
          f"{stats_p['n_dropped_spacings']}")
    for label, st in (("PRIMARY poly-deg5+edgetrim", stats_p),
                      ("SECONDARY mean-norm", stats_s)):
        print(f"  -- {label} (nonmonotone unfold points: "
              f"{st['n_nonmonotone']}) --")
        print("  k |    n    mean(=k)  Delta_emp     V_k  | D_Poisson "
              "D_WigCorr D_WigOld | GoF18_P GoF18_W")
        for k in K_SET:
            d = st["k"][k]                                         # (local)
            print(f"  {k} | {d['n']:5d}  {d['mean']:8.4f}  "
                  f"{d['Delta_emp']:9.4f}  {d['V_k']:6.3f} | "
                  f"{d['D_poisson']:9.4f} {d['D_wigner_corr']:9.4f} "
                  f"{d['D_wigner_old']:8.4f} | {d['GoF18_poisson']:7.4f} "
                  f"{d['GoF18_wigner_corr']:7.4f}")
        print(f"  Brody beta_1 (MLE, k=1 pooled) = {st['beta1']:.4f} "
              f"(boundary {BRODY_BOUNDARY})")

    # --- Step (5): super-Poisson trigger + attribution (per scheme) ---
    print("\n=== Step 5: super-Poisson trigger + degeneracy attribution ===")
    trig_p, trig_p_diag = superp_trigger(stats_p)                  # (local)
    trig_s, trig_s_diag = superp_trigger(stats_s)                  # (local)
    attr_p = attr_s = None                                         # (local)
    attr_p_diag, attr_s_diag = {}, {}                              # (local)
    for label, trig, diag in (("PRIMARY", trig_p, trig_p_diag),
                              ("SECONDARY", trig_s, trig_s_diag)):
        print(f"  {label}: F_emp({SSTAR})={diag['F_emp_sstar']:.4f} vs "
              f"F_P={diag['F_poisson_sstar']:.4f} (3sigma band "
              f"{diag['band_3sigma']:.4f}); excess_fire={diag['excess_fire']}; "
              f"vk_fire={diag['vk_fire']} -> TRIGGERED={trig}")
    if trig_p:
        attr_p, attr_p_diag = attribution_check(sequences, unfold_primary,
                                                trim_edges=True)
        print(f"  PRIMARY attribution: attributable={attr_p}  {attr_p_diag}")
    if trig_s:
        attr_s, attr_s_diag = attribution_check(sequences, unfold_secondary)
        print(f"  SECONDARY attribution: attributable={attr_s}  {attr_s_diag}")

    # option-A cross-check: UNTRIMMED primary, artifact spacings (s <= 0)
    # dropped only — demonstrates the edge trim does no physics work
    stats_xa = pooled_stats(sequences, unfold_primary,
                            drop_nonpositive=True)                 # (local)
    print("\n  xcheckA (untrimmed primary, nonpositive-spacing drop only):")
    print(f"    V_k = {[round(stats_xa['k'][k]['V_k'], 3) for k in K_SET]}, "
          f"beta1 = {stats_xa['beta1']:.4f}, "
          f"D_P = {[round(stats_xa['k'][k]['D_poisson'], 4) for k in K_SET]}, "
          f"D_W = {[round(stats_xa['k'][k]['D_wigner_corr'], 4) for k in K_SET]}")

    # --- Step (6): per-scheme classes + composite (pre-registered operator) ---
    print("\n=== Step 6: verdict assembly ===")
    cls_p, sub_p = scheme_class(stats_p, extraction_ok, trig_p, attr_p)  # (local)
    cls_s, sub_s = scheme_class(stats_s, extraction_ok, trig_s, attr_s)  # (local)
    print(f"  scheme classes: PRIMARY={cls_p}{('-' + sub_p) if sub_p else ''}, "
          f"SECONDARY={cls_s}{('-' + sub_s) if sub_s else ''}")
    sub_path = ""                                                  # (local)
    if cls_p == cls_s:
        if cls_p == "PASS":
            if r_up and r_poisson_side:
                composite = "PASS"                                 # (local)
            else:
                composite, sub_path = "INFO", "d"  # Claim C <r> contradiction
        elif cls_p == "FAIL":
            if r_goe_side:
                composite = "FAIL"
            else:
                composite, sub_path = "INFO", "d"  # FAIL conj needs <r> GOE-side
        else:
            composite, sub_path = "INFO", (sub_p or sub_s or "d")
    else:
        composite, sub_path = "INFO", "d"          # unfolding-pair flip
    print(f"  composite (operator-authoritative): {composite}"
          f"{('-' + sub_path) if sub_path else ''}")

    # schema-v2 3-tuple (plan-pinned semantics)
    poisson_pref_all_p = all(stats_p["k"][k]["D_poisson"]
                             < stats_p["k"][k]["D_wigner_corr"]
                             for k in K_SET)                       # (local)
    sign_v = ("PASS" if (poisson_pref_all_p and r_up and r_poisson_side)
              else "FAIL")                                         # (local)
    vks_p = {k: stats_p["k"][k]["V_k"] for k in K_SET}             # (local)
    if any(v < RIGIDITY_GUARD for v in vks_p.values()):
        mag_v = "INFO"                                             # (local)
    elif trig_p and (attr_p is True):
        mag_v = "INFO"
    elif all(v >= VK_BOUNDARY for v in vks_p.values()):
        mag_v = "PASS"
    elif any(RIGIDITY_GUARD <= v < VK_BOUNDARY for v in vks_p.values()):
        mag_v = "FAIL"
    else:
        mag_v = "INFO"
    if cls_p == cls_s:
        reg_v = "VALID"                                            # (local)
    elif {cls_p, cls_s} == {"PASS", "FAIL"}:
        reg_v = "BREAKDOWN"
    else:
        reg_v = "MARGINAL"
    coll = collapse_rule(sign_v, mag_v, reg_v)                     # (local)
    xc9 = (coll == composite)                                      # (local)
    print(f"  3-tuple: sign={sign_v} magnitude={mag_v} regime={reg_v} "
          f"-> collapse={coll}; XC9 collapse==operator: "
          f"{'OK' if xc9 else 'DIVERGENT (operator authoritative)'}")

    # --- Step (7): per-sector diagnostic table (DIAGNOSTIC ONLY, S74 lesson) ---
    sector_table = []                                              # (local)
    for key in rep_keys:
        lam = reps[key]                                            # (local)
        d1 = np.diff(lam)                                          # (local)
        rr = np.minimum(d1[:-1], d1[1:]) / np.maximum(d1[:-1], d1[1:])  # (local)
        e_p, _ = unfold_primary(lam)                               # (local)
        s1p = np.diff(e_p)                                         # (local)
        sector_table.append([key[0], key[1], len(raw[key]), len(lam),
                             float(np.mean(rr)),
                             float(np.var(s1p, ddof=VAR_DDOF))])
    sector_table = np.array(sector_table, dtype=float)             # (local)

    # --- repaired-(4,4) robustness row (DIAGNOSTIC ONLY; no verdict weight) ---
    # The s84 cache lacks sector (4,4); W3-1 repaired it in-run (eigenvalues
    # in s100b_cf28_simple_pole_preflight.npz key evals_44_reconstructed).
    # The verdict machinery is the plan-frozen 27-rep / 5846-level pin (made
    # against the actual cache); this row tests stability to the known repair.
    diag44 = {}                                                    # (local)
    try:
        pf = np.load(PREFLIGHT_44, allow_pickle=True)              # (local)
        ev44 = np.sort(np.abs(np.asarray(
            pf["evals_44_reconstructed"], dtype=float)))           # (local)
        d44 = dedup_sorted(ev44)                                   # (local)
        if len(d44) >= ELIG_MIN:
            seq44 = sequences + [d44]                              # (local)
            st44 = pooled_stats(seq44, unfold_primary,
                                trim_edges=True)                   # (local)
            r44 = float(np.mean(r_ratio_pooled(seq44)))            # (local)
            diag44 = {
                "n_unique_44": len(d44),
                "pooled_n_with44": int(pooled_n + len(d44)),
                "r_mean_with44": r44,
                "beta1_with44": st44["beta1"],
                "V_k_with44": [st44["k"][k]["V_k"] for k in K_SET],
                "D_poisson_with44": [st44["k"][k]["D_poisson"] for k in K_SET],
                "D_wigner_corr_with44": [st44["k"][k]["D_wigner_corr"]
                                         for k in K_SET],
            }
            print(f"\n  DIAGNOSTIC repaired-(4,4) row (n_unique={len(d44)}): "
                  f"<r>={r44:.4f}, beta1={st44['beta1']:.4f}, "
                  f"V_k={[round(v, 3) for v in diag44['V_k_with44']]}")
        else:
            diag44 = {"n_unique_44": len(d44), "note": "below eligibility"}
    except Exception as exc:  # noqa: BLE001
        diag44 = {"error": str(exc)}
        print(f"  DIAGNOSTIC (4,4) row unavailable: {exc}")

    # --- npz ---
    np.savez(
        OUT_NPZ,
        # identity + pins
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION,
        L_max=L_MAX, k_set=np.array(K_SET),
        pinmap_json=json.dumps(dict(sorted(pins.items())), sort_keys=True),
        audit_sha256=audit_sha, content_sha256=content_sha,
        untrusted_upstream_caveat=UNTRUSTED_UPSTREAM_ROW,
        # extraction provenance (Eq. 15 form + constants as strings)
        extraction_ok=extraction_ok,
        extracted_anchors_json=json.dumps(ext_info.get("anchors", {})),
        c1_value=c1,
        alpha_corrected_eq15=np.array([a_corr[k] for k in K_SET]),
        alpha_old_eq3=np.array([a_old[k] for k in K_SET]),
        delta_goe_eq8=np.array([dgoe[k] for k in K_SET]),
        delta_poisson_eq11=np.array([dpois[k] for k in K_SET]),
        delta_surmise_eq7=np.array([delta_surmise(a_corr[k], k)
                                    for k in K_SET]),
        vk_denominators=np.array([denom[k] for k in K_SET]),
        # sector resolution
        rep_keys=np.array(rep_keys), n_reps=n_reps,
        pooled_n_distinct=pooled_n,
        n_eligible=len(eligible), n_sectors_cache=n_sectors,
        bdi_pair_maxdiff=pair_maxdiff,
        bdi_mismatch_pairs=np.array(bdi_mismatch, dtype=float)
        if bdi_mismatch else np.zeros((0, 3)),
        sector_sequences=np.array(sequences, dtype=object),
        per_sector_table=sector_table,
        per_sector_table_cols="p,q,n_raw,n_unique,r_mean_sector,var_s1_primary",
        # pooled spacings per k per scheme
        s_k1_primary=stats_p["k"][1]["sample"],
        s_k2_primary=stats_p["k"][2]["sample"],
        s_k3_primary=stats_p["k"][3]["sample"],
        s_k1_secondary=stats_s["k"][1]["sample"],
        s_k2_secondary=stats_s["k"][2]["sample"],
        s_k3_secondary=stats_s["k"][3]["sample"],
        # headline statistics (primary, secondary)
        D_k_poisson_primary=np.array([stats_p["k"][k]["D_poisson"]
                                      for k in K_SET]),
        D_k_wigner_corrected_primary=np.array(
            [stats_p["k"][k]["D_wigner_corr"] for k in K_SET]),
        D_k_wigner_old_primary=np.array([stats_p["k"][k]["D_wigner_old"]
                                         for k in K_SET]),
        D_k_poisson_secondary=np.array([stats_s["k"][k]["D_poisson"]
                                        for k in K_SET]),
        D_k_wigner_corrected_secondary=np.array(
            [stats_s["k"][k]["D_wigner_corr"] for k in K_SET]),
        GoF_Eq18_poisson_primary=np.array([stats_p["k"][k]["GoF18_poisson"]
                                           for k in K_SET]),
        GoF_Eq18_wigner_corrected_primary=np.array(
            [stats_p["k"][k]["GoF18_wigner_corr"] for k in K_SET]),
        Delta_emp_primary=np.array([stats_p["k"][k]["Delta_emp"]
                                    for k in K_SET]),
        Delta_emp_secondary=np.array([stats_s["k"][k]["Delta_emp"]
                                      for k in K_SET]),
        V_k_primary=np.array([stats_p["k"][k]["V_k"] for k in K_SET]),
        V_k_secondary=np.array([stats_s["k"][k]["V_k"] for k in K_SET]),
        mean_sk_primary=np.array([stats_p["k"][k]["mean"] for k in K_SET]),
        mean_sk_secondary=np.array([stats_s["k"][k]["mean"] for k in K_SET]),
        beta1_primary=stats_p["beta1"], beta1_secondary=stats_s["beta1"],
        n_nonmonotone_primary=stats_p["n_nonmonotone"],
        # OPERATIONAL DEVIATION disclosure block (monotone-window edge trim)
        edge_zone=EDGE_ZONE,
        n_trimmed_levels_primary=stats_p["n_trimmed_levels"],
        n_mid_flagged_primary=stats_p["n_mid_flagged"],
        n_dropped_spacings_primary=stats_p["n_dropped_spacings"],
        trim_table_primary=stats_p["trim_table"],
        pooled_n_primary_trimmed=int(pooled_n - stats_p["n_trimmed_levels"]),
        # option-A cross-check (untrimmed primary, nonpositive drop only)
        xcheckA_V_k=np.array([stats_xa["k"][k]["V_k"] for k in K_SET]),
        xcheckA_beta1=stats_xa["beta1"],
        xcheckA_D_poisson=np.array([stats_xa["k"][k]["D_poisson"]
                                    for k in K_SET]),
        xcheckA_D_wigner_corrected=np.array(
            [stats_xa["k"][k]["D_wigner_corr"] for k in K_SET]),
        xcheckA_Delta_emp=np.array([stats_xa["k"][k]["Delta_emp"]
                                    for k in K_SET]),
        # r cross-check
        r_values=r_vals, r_mean_resolved=r_mean, r_sigma=sigma_r,
        r_z_vs_poisson=z_r, r_baseline_S38=R_BASELINE_S38,
        # super-Poisson trigger + attribution arrays
        superp_trigger_primary=trig_p,
        superp_trigger_secondary=trig_s,
        superp_diag_primary_json=json.dumps(trig_p_diag),
        superp_diag_secondary_json=json.dumps(trig_s_diag),
        attribution_primary_json=json.dumps(
            {"attributable": attr_p, **attr_p_diag}, default=float),
        attribution_secondary_json=json.dumps(
            {"attributable": attr_s, **attr_s_diag}, default=float),
        # diagnostic-only repaired-(4,4) robustness row
        diag44_json=json.dumps(diag44, default=float),
        # verdict block
        scheme_class_primary=cls_p, scheme_class_secondary=cls_s,
        sub_path_primary=sub_p, sub_path_secondary=sub_s,
        composite_verdict=composite, info_sub_path=sub_path,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=reg_v,
        collapse_rule_composite=coll, xc9_collapse_matches_operator=xc9,
    )
    print(f"\n  npz written: {OUT_NPZ.name}")

    # --- plot ---
    fig = plt.figure(figsize=(16.5, 9.5))                          # (local)
    gs = fig.add_gridspec(2, 3, hspace=0.32, wspace=0.27)          # (local)
    for j, k in enumerate(K_SET):
        ax = fig.add_subplot(gs[0, j])                             # (local)
        s = stats_p["k"][k]["sample"]                              # (local)
        ax.hist(s, bins=60, density=True, alpha=0.45, color="#4878CF",
                label=f"pooled $s^{{({k})}}$ (n={len(s)})")
        D = delta_surmise(a_corr[k], k)                            # (local)
        xg = np.linspace(1e-6, k + 4.5 * np.sqrt(max(D, 0.3)), 800)  # (local)
        ax.plot(xg, pdf_poisson_k(xg, k), "k-", lw=2.2,
                label=r"Poisson $\Gamma(k,1)$ [Eq. C3]")
        ax.plot(xg, pdf_wigner_like(xg, a_corr[k], k), "r--", lw=2.0,
                label=r"corr. Wigner-kNN [Eq. 2+4+15], $\beta$=1")
        ax.plot(xg, pdf_wigner_like(xg, a_old[k], k), color="orange",
                ls=":", lw=1.6, label="old surmise [Eq. 3] (diag.)")
        ax.set_title(
            f"k={k}: $D_P$={stats_p['k'][k]['D_poisson']:.4f}, "
            f"$D_W$={stats_p['k'][k]['D_wigner_corr']:.4f}, "
            f"$V_{k}$={stats_p['k'][k]['V_k']:.3f}", fontsize=10.5)
        ax.set_xlabel("s"); ax.set_ylabel(f"$P_{k}(s)$")
        ax.legend(fontsize=7.5)
    ax = fig.add_subplot(gs[1, 0])                                 # (local)
    kk = np.array(K_SET, dtype=float)                              # (local)
    ax.plot(kk, [dpois[k] for k in K_SET], "k-o", lw=2,
            label=r"$\Delta_{Poisson}=k$ [Eq. 11]")
    ax.plot(kk, [dgoe[k] for k in K_SET], "g-s", lw=2,
            label=r"$\Delta_{GOE}=\frac{2}{\pi^2}\ln k+\frac{4}{\pi}-1$ [Eq. 8]")
    ax.plot(kk, [stats_p["k"][k]["Delta_emp"] for k in K_SET], "r-D",
            lw=2, ms=9, label=r"$\Delta_{emp}$ primary")
    ax.plot(kk, [stats_s["k"][k]["Delta_emp"] for k in K_SET], "b--^",
            lw=1.5, label=r"$\Delta_{emp}$ secondary")
    ax.set_xlabel("k"); ax.set_ylabel(r"$\Delta(k)$"); ax.set_xticks(kk)
    ax.set_title("variance vs references"); ax.legend(fontsize=8)
    ax = fig.add_subplot(gs[1, 1])                                 # (local)
    ax.hist(r_vals, bins=50, density=True, alpha=0.5, color="#4878CF")
    ax.axvline(r_mean, color="r", lw=2.4, label=f"<r>={r_mean:.4f}")
    ax.axvline(r_POISSON_canonical, color="k", ls="--", lw=1.8,
               label=f"Poisson {r_POISSON_canonical}")
    ax.axvline(r_GOE_canonical, color="g", ls=":", lw=1.8,
               label=f"GOE {r_GOE_canonical}")
    ax.axvline(R_BASELINE_S38, color="gray", ls="-.", lw=1.6,
               label=f"S38 unresolved {R_BASELINE_S38}")
    ax.set_xlabel("r"); ax.set_ylabel("P(r)")
    ax.set_title("unfolding-independent r-ratio (pooled, resolved)")
    ax.legend(fontsize=8)
    ax = fig.add_subplot(gs[1, 2])                                 # (local)
    xpos = np.arange(len(K_SET))                                   # (local)
    ax.bar(xpos - 0.18, [stats_p["k"][k]["V_k"] for k in K_SET], 0.36,
           color="#CF4878", label="primary")
    ax.bar(xpos + 0.18, [stats_s["k"][k]["V_k"] for k in K_SET], 0.36,
           color="#78CF48", label="secondary")
    ax.axhline(1.0, color="k", lw=1.4, label="Poisson (V=1)")
    ax.axhline(VK_BOUNDARY, color="orange", ls="--", lw=1.6,
               label=f"boundary {VK_BOUNDARY}")
    ax.axhline(0.0, color="g", ls=":", lw=1.4, label="GOE (V=0)")
    ax.axhline(RIGIDITY_GUARD, color="purple", ls="-.", lw=1.2,
               label=f"rigidity {RIGIDITY_GUARD}")
    ax.set_xticks(xpos); ax.set_xticklabels([f"k={k}" for k in K_SET])
    ax.set_ylabel(r"$V_k$"); ax.set_title("variance discriminator")
    ax.legend(fontsize=7.5, loc="center right")
    fig.suptitle(
        f"{GATE_ID}: sector-resolved kNN statistics, D_K(tau_fold={tau_fold}) "
        f"L_max={L_MAX} — {n_reps} reps, {pooled_n} distinct levels — "
        f"VERDICT {composite}{('-' + sub_path) if sub_path else ''} "
        f"[UNTRUSTED-UPSTREAM: LC-lineage canonicity pending]",
        fontsize=11.5)
    fig.savefig(OUT_PNG, dpi=130, bbox_inches="tight")
    plt.close(fig)
    print(f"  plot written: {OUT_PNG.name}")

    # --- verdict payload ---
    vstr = (f"r_mean={r_mean:.4f}|V_k={vks_p[1]:.3f},{vks_p[2]:.3f},"
            f"{vks_p[3]:.3f}|beta1={stats_p['beta1']:.3f}|"
            f"KS_P={stats_p['k'][1]['D_poisson']:.3f},"
            f"{stats_p['k'][2]['D_poisson']:.3f},"
            f"{stats_p['k'][3]['D_poisson']:.3f}|"
            f"KS_W={stats_p['k'][1]['D_wigner_corr']:.3f},"
            f"{stats_p['k'][2]['D_wigner_corr']:.3f},"
            f"{stats_p['k'][3]['D_wigner_corr']:.3f}|"
            f"N={pooled_n}|reps={n_reps}|"
            f"subpath={sub_path if sub_path else 'none'}")         # (local)
    print(f"\n(value={vstr!r}, scheme={SCHEME}, convention={CONVENTION}, "
          f"L_max={L_MAX})")
    payload = {
        "session": SESSION,
        "gate_id": GATE_ID,
        "verdict": composite,
        "value": vstr,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": reg_v,
        "companion_note": (f"sector-resolved kNN; secondary-scheme V_k="
                           f"{stats_s['k'][1]['V_k']:.3f},"
                           f"{stats_s['k'][2]['V_k']:.3f},"
                           f"{stats_s['k'][3]['V_k']:.3f}; beta1_sec="
                           f"{stats_s['beta1']:.3f}; r_z_vs_Poisson="
                           f"{z_r:+.2f}"),
        "extra_rows": [
            UNTRUSTED_UPSTREAM_ROW,
            (f"# diagnostic: repaired-(4,4) robustness row (no verdict "
             f"weight): {json.dumps(diag44, default=float)[:200]}"),
        ],
    }                                                              # (local)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")

    wall = time.time() - t0                                        # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.1f}s) ===")
    return 0   # valid scientific verdict => exit 0 (math-scripts.md)


if __name__ == "__main__":
    sys.exit(main())
