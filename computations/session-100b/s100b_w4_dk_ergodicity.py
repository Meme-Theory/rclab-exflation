#!/usr/bin/env python3
"""
S100b W4-1 S100b-DK-ERGODICITY -- Hekkelman-McDonald vacuum-uniqueness /
quantum-ergodicity criterion on the truncated spectral triple
(A_K, H_K^(12), D_K(tau_fold))
=============================================================================

Gate: S100b-DK-ERGODICITY ([SIGN] trigger -- schema-v2 3-tuple companion row)
Classification: GEOMETRIC (vacuum-state structure of the C*-dynamical system
  built on the fabric's spectral triple -- the fabric itself, not excitations)

Pre-registered operator (plan sessions/session-plan/session-100b-plan-w4.md
SS W4-1, frozen 2026-06-06):
  PASS iff [ QE_defect(P_S, 1/4) > 0.01 ] AND [ n_vacuum >= 2 ] AND
           [ dim_fix >= 2 ] AND [ Weyl-applicability: |d_fit - 8| <= 1.5 AND
           R^2 >= 0.98 on the pinned window, for BOTH global and local fits ].
  FAIL iff [ QE_defect <= 0.01 AND n_vacuum = 1 AND dim_fix = 1 ] with
           Weyl-applicability holding.
  INFO iff Weyl-applicability fails (criterion inapplicable on the finite
           truncation) OR extraction-limited OR mixed indicators.
           Sub-paths: (a) global-Weyl fit fails; (b) local-Weyl fit for P_S
           fails while global holds; (c) extraction-limited; (d) mixed.

WAVE-4 SCOPING LAW (MANDATORY): "GGE never thermalizes" is RETRACTED-S39
(atlas-04 T3 BROKEN; INTEG-39 DECISIVE FAIL: t_therm ~ 6 M_KK^-1, Brody
beta = 0.633 single-cell). What survives: "transit IS the physics" +
FABRIC-SCALE integrability (CG(24) Poisson <r> = 0.367, FABRIC-INTEG-56) +
diabatic transit-freeze (R_therm = 5251.82, S_ent = 0, S95). THIS gate tests
the FABRIC-SCALE integrability claim at the spectral-triple level -- NOT the
retracted single-cell permanence. R_therm consumed as VALUE only (its legacy
canonical_constants comment narration predates the S100b housekeeping SS A
reconcile).

UNTRUSTED-UPSTREAM CAVEAT (orchestrator-mandated): this gate consumes the s84
spectrum-cache lineage flagged by the S100b-TAU0-LAITEH-REDUCTION ESCALATION
(FAIL, SUBCASE=STRUCTURED: the framework tau=0 operator sits at the
Levi-Civita torsion point t=1/2 of the Lai-Teh family, NOT the Kostant cubic
t=1/3; the eigensolver itself is verified CORRECT by a cubic-modified control
at machine epsilon; lambda^2 = n/36 PROVEN record remains VALID; cache
numerics are self-consistent with the LC lineage the framework has always
computed). Open question is operator CANONICITY, not numerical validity.
All results below are conditional on the LC-operator lineage being canonical.

METHODOLOGY (plan SS W4-1 method block, executed exactly):
  (1) PDF-extract the operative criterion statements from the LOCAL HM paper
      (arXiv 2412.00628) via pypdf: Definition 2.3 (Weyl law / local Weyl
      law), Theorem 2.7 (NC integral = (omega.M)-log-averaged
      spectral-truncation limit), Theorem 3.2 (Szego limit theorem),
      Definition 6.10 (classical ergodicity = G_t-fixed points in L2(S*A)
      are scalars only), Theorem 6.11 (QE diagonal convergence on a
      density-one subset) + the unique-vacuum-state remark (Zel96 reading:
      classical ergodicity <=> rank of the projection onto G_t-invariant
      vectors in L2(S*A) is 1 = "uniqueness of the vacuum state").
      NEVER filled from training knowledge (feedback_research-corpus).
  (2) Weyl-applicability (Def 2.3 operationalized): log-log fit of
      Tr(e^{-t D_K^2}) over the pinned bulk window
      t in [4/lambda_max^2, 1/(4 lambda_min^2)], 40 log-spaced points,
      endpoints computed from the cache at runtime (deterministic).
      Applicability iff |d_fit - 8| <= 1.5 AND R^2 >= 0.98 for BOTH the
      global trace and the local trace Tr(P_S e^{-t D_K^2}).
  (3) QE-defect: balanced sector-union projector P_S (greedy accumulation of
      (p,q) sectors by descending eigenvalue count, lexicographic tie-break,
      until spectral fraction c_S in [0.4, 0.6]). Sector purity (PROVEN
      Peter-Weyl block-diagonality, off-diag < 8.4e-15) => diagonal elements
      <e_k, P_S e_k> in {0,1} from cache sector membership alone.
      QE_defect := fraction of k with |<e_k,P_S e_k> - c_S| >= 1/4, with
      c_S = the Thm-2.7 truncated NC integral (logarithmic mean
      M: x -> (1/log(n+2)) sum_k x_k/(k+1), paper Section 2); both the plain
      and the (omega.M)-log-averaged c_S reported, defect computed under both.
  (4) Fixed-point space (Def 6.10 on the pinned observable family): dim_fix =
      dim span of alpha_t-invariant elements among the 90 sector projectors
      {P_(p,q)} (each commutes with D_K exactly -- PROVEN block-diagonality;
      mutually orthogonal non-zero projectors => linearly independent).
  (5) Vacuum-state count (extracted Zel96 convention): n_vacuum = number of
      extremal alpha_t-invariant states on the ground (bottom-|lambda|)
      multiplet = its multiplicity m_min at degeneracy_tol = 1e-10
      (floor witness robust under every candidate convention: the bottom
      multiplet at |lambda|_min = 0.8197411121, sector (0,0), m_min = 2).
      Companion: n_vacuum_GNS_family = number of extremal invariant states
      on the abelian C*-algebra generated by the pinned family (= 90).
  (6) Szego convergence DIAGNOSTIC (Thm 3.2 / Thm 2.7): truncation sequence
      f_n = Tr(P_{lambda_n} P_S P_{lambda_n})/Tr(P_{lambda_n}) vs n, with
      logarithmic mean M; tail convergence-rate fit DIAGNOSTIC ONLY
      (Level-2 envelope channel; NO verdict weight).
  (7) Time averaging EXACT (infinite-T Cesaro projection identity
      lim_{T->inf}(1/T) int_0^T e^{i(l_i-l_j)t} dt = delta_{l_i,l_j});
      no finite-T mesh exists, hence no T pin.
  (+) (4,4)-repair sensitivity DIAGNOSTIC (orchestrator override): sector
      (4,4) is absent from the pinned 90-sector cache (plan feasibility pins
      were made against the actual cache contents); the W3-1-repaired (4,4)
      eigenvalues (2000 = 125 x 16) from s100b_cf28_simple_pole_preflight.npz
      are unioned in and the headline quantities recomputed. Diagnostic only;
      the verdict object is the plan-pinned 90-sector cache.

3-tuple ([SIGN], plan output_artifacts pin):
  sign_verdict      = n_vacuum > 1 direction (PASS iff n_vacuum >= 2)
  magnitude_verdict = QE_defect vs 0.01 floor (PASS iff QE_defect > 0.01,
                      conservatively under BOTH c_S readings)
  regime_verdict    = Weyl-applicability: VALID (both fits in-band),
                      MARGINAL (exactly one in-band), BREAKDOWN (neither).
  COMPOSITE-PRECEDENCE NOTE (pre-declared BEFORE evaluation): the gate-block
  operator (plan SS W4-1, frozen 2026-06-06) pre-registers INFO on
  Weyl-applicability failure ("applicability is a guard, not the
  hypothesis"); the generic gate-verdicts.md 3-tuple collapse rule would map
  (PASS, PASS, MARGINAL) -> PASS. The PLAN-SPECIFIC operator governs the
  composite (most-specific pre-registration; emitting PASS would certify the
  HM criterion as applicable when its Def-2.3 hypothesis is uncertified --
  a false corroboration). The 3-tuple row is descriptive per the plan's own
  axis mapping.

DISCIPLINE
----------
- from canonical_constants import * (tau_fold, M_KK, R_therm consumed)
- Every local/intermediate tagged # (local)
- cpu-cap-OMP8 (plan GPU_path pin): spectrum-cache statistics only, no dense
  linear algebra >= 100x100 is ever formed (1-D eigenvalue arrays); GPU rule
  N/A; OMP_NUM_THREADS=8 set BEFORE importing numpy.
- SHA-256 of all input files logged in the first stdout lines; cache + HM PDF
  verified against the plan Input-SHA Ledger pins (abort exit!=0 on drift).
- audit_sha256 = sha256(script || canonical_constants || pinmap_json);
  content_sha256 = sha256(script). S84+ dual-SHA schema.
- Verdict emitted via print_verdict_payload -> agent calls the race-safe
  emit_verdict knowledge-MCP tool (session "100b"). NO open("a") append.
- Exit 0 for any valid PASS/FAIL/INFO; exit != 0 reserved for breakage.

Output 4-tuple:
  (value=<summary>, scheme=HM-2412.00628-vacuum-uniqueness,
   convention=spectral-Cesaro-exact-cache-only-HM-Def6.10-Thm6.11-Zel96-rank1-vacuum,
   L_max=12)
"""

from __future__ import annotations

# --------------------------------------------------------------------------
# Section 0 -- CPU thread cap BEFORE numpy import (plan pin: cpu-cap-OMP8)
# --------------------------------------------------------------------------
import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

# Make console safe for extracted unicode (PDF text) on Windows cp1252.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
if str(SHARED_DIR) not in sys.path:
    sys.path.insert(0, str(SHARED_DIR))

# --------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first project import)
# --------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403,E402  (tau_fold, M_KK, R_therm)

# --------------------------------------------------------------------------
# Section 2 -- Standard imports
# --------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# --------------------------------------------------------------------------
# Section 3 -- Identity + pre-registered machinery pins (plan SS W4-1)
# --------------------------------------------------------------------------
SESSION = "100b"                                                   # (local)
GATE_ID = "S100b-DK-ERGODICITY"                                    # (local)
SCHEME = "HM-2412.00628-vacuum-uniqueness"                         # (local)
# Base convention per plan; extracted vacuum-convention suffix appended at
# emission per the plan's machinery_pin_map convention note.
CONVENTION_BASE = "spectral-Cesaro-exact-cache-only"               # (local)
VACUUM_SUFFIX = "-HM-Def6.10-Thm6.11-Zel96-rank1-vacuum"           # (local)
CONVENTION = CONVENTION_BASE + VACUUM_SUFFIX                       # (local)
L_MAX = 12                                                         # (local)

# Pre-registered thresholds / pins (define BEFORE running; plan SS W4-1)
QE_FLOOR = 0.01            # QE_defect exceptional-fraction floor   # (local)
QE_DELTA = 0.25            # deviation threshold delta = 1/4        # (local)
WEYL_D_REF = 8.0           # SU(3) fiber Weyl dimension (S52)       # (local)
WEYL_D_BAND = 1.5          # |d_fit - 8| <= 1.5                     # (local)
R2_MIN = 0.98              # fit quality floor                      # (local)
CS_LO, CS_HI = 0.40, 0.60  # balanced-union target band             # (local)
DEGEN_TOL = 1e-10          # S53 lesson (1e-15 fails near-multiplets) # (local)
N_EVAL_PIN = 166896        # plan N_eval pin (90-sector cache)      # (local)
N_SECTORS_PIN = 90         # plan sector-count pin                  # (local)
N_T_POINTS = 40            # heat-trace fit grid                    # (local)
NVAC_FLOOR = 2             # integer floor n_vacuum >= 2            # (local)
DIMFIX_FLOOR = 2           # integer floor dim_fix >= 2             # (local)

# Plan Input-SHA Ledger pins (static files; abort on drift)
CACHE_SHA_PIN = "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"  # (local)
HM_PDF_SHA_PIN = "9572107a7e8cc966f2f48a536766e0406a82affcf3ecdc6b9b3dfd2175813151"  # (local)

CACHE_PATH = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local)
HM_PDF_PATH = (PROJECT_ROOT / "downloads" / "research-sweep-s99" /
               "ncg-spectral-action" /
               "04_Hekkelman-McDonald_NC-Integral-Truncated-Triples-Quantum-Ergodicity.pdf")  # (local)
CF28_PATH = SESSION_DIR / "s100b_cf28_simple_pole_preflight.npz"   # (local)
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"             # (local)

OUT_NPZ = SESSION_DIR / "s100b_w4_dk_ergodicity.npz"               # (local)
OUT_PNG = SESSION_DIR / "s100b_w4_dk_ergodicity.png"               # (local)

INPUT_FILES = [CANONICAL_PATH, CACHE_PATH, HM_PDF_PATH, CF28_PATH]  # (local)


# --------------------------------------------------------------------------
# Section 4 -- SHA-256 dual-pin block (S84+ schema; template-conformant)
# --------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list) -> dict:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    script_bytes = script_path.read_bytes()                         # (local)
    canonical_bytes = canonical_path.read_bytes()                   # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="",
                          extra_rows=None) -> dict:
    """Print the emit_verdict payload (race-safe MCP emission by the agent).

    Letter-suffixed sub-session => session passed as STRING "100b".
    """
    payload = {
        "session": SESSION,  # letter-suffixed sub-session => string, not int
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }  # (local)
    if companion_note:
        payload["companion_note"] = companion_note
    if not (sign_verdict is None and magnitude_verdict is None
            and regime_verdict is None):
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# --------------------------------------------------------------------------
# Section 5 -- Step (1): criterion extraction from the LOCAL HM PDF (pypdf)
# --------------------------------------------------------------------------
# Anchored on statement-initial substrings (NOT bare citations): e.g.
# "Theorem 2.7. Let A" (statement) vs "..., Theorem 2.7)" (citation).
EXTRACTION_ANCHORS = [
    ("Remark 2.2 (Tauberian)", r"Remark 2\.2\.", 320),
    ("Definition 2.3 (Weyl law / local Weyl law)", r"Definition 2\.3\.\s*We say", 420),
    ("logarithmic mean M", r"logarithmic mean M", 260),
    ("Theorem 2.7 (NC integral = (omega.M) spectral-truncation limit)", r"Theorem 2\.7\.\s*Let A", 460),
    ("Theorem 3.2 (Szego limit theorem)", r"Theorem 3\.2\.\s*Let D", 430),
    ("Definition 6.10 (classical ergodicity)", r"Definition 6\.10\.\s*We say", 260),
    ("Theorem 6.11 (quantum ergodicity)", r"Theorem 6\.11\.\s*Let", 470),
    ("unique-vacuum remark (Zel96, proof of Thm 6.11)", r"Proof\.\s*Classical ergodicity of", 430),
    ("Example 6.12.2 (almost-commutative NOT classically ergodic)",
     r"Any nontrivial almost commutative manifold", 300),
]  # (local)

MANDATORY_ANCHOR_IDX = [1, 3, 4, 5, 6, 7]  # Def2.3, Thm2.7, Thm3.2, Def6.10, Thm6.11, vacuum remark  # (local)


def extract_criterion(pdf_path: Path):
    """pypdf extraction of the operative criterion statements (LOCAL paper).

    Returns (anchors_list_of_strings, extraction_ok, n_pages).
    extraction_ok requires ALL mandatory anchors found. The fallback route
    (mcp paper-search) is an AGENT action outside this script; if this
    primary route fails the gate closes INFO sub-path (c) extraction-limited.
    """
    try:
        from pypdf import PdfReader  # (local import; venv-verified)
        reader = PdfReader(str(pdf_path))  # (local)
        text = "\n".join((pg.extract_text() or "") for pg in reader.pages)  # (local)
        n_pages = len(reader.pages)  # (local)
    except Exception as exc:  # pragma: no cover
        return [f"EXTRACTION-FAILED: {exc!r}"], False, 0
    flat = re.sub(r"\s+", " ", text)  # (local)
    out = []  # (local)
    found = []  # (local)
    for name, pat, span in EXTRACTION_ANCHORS:
        m = re.search(pat, flat)  # (local)
        if m:
            seg = flat[m.start(): m.start() + span].strip()  # (local)
            out.append(f"[{name}] {seg}")
            found.append(True)
        else:
            out.append(f"[{name}] NOT-FOUND")
            found.append(False)
    ok = all(found[i] for i in MANDATORY_ANCHOR_IDX)  # (local)
    return out, ok, n_pages


# --------------------------------------------------------------------------
# Section 6 -- Cache load + spectral assembly
# --------------------------------------------------------------------------
def load_sectors(path: Path):
    d = np.load(str(path), allow_pickle=True)  # (local)
    se = d["sector_evals"].item()  # (local)
    sectors = {}  # (local)
    for k, v in se.items():
        sectors[(int(k[0]), int(k[1]))] = np.sort(np.asarray(v["abs_evals"], dtype=np.float64))
    return sectors


def heat_trace_fit(evals: np.ndarray, ts: np.ndarray):
    """Log-log linear fit of Tr(e^{-t D^2}) on the pinned window.

    Returns (d_fit, R2, HT). Def 2.3 form: Tr ~ C t^{-d/2}
      => log Tr = log C - (d/2) log t => d_fit = -2 * slope.
    """
    HT = np.array([np.sum(np.exp(-t * evals ** 2)) for t in ts])  # (local)
    A = np.vstack([np.log(ts), np.ones_like(ts)]).T  # (local)
    coef, *_ = np.linalg.lstsq(A, np.log(HT), rcond=None)  # (local)
    pred = A @ coef  # (local)
    ss_res = float(np.sum((np.log(HT) - pred) ** 2))  # (local)
    ss_tot = float(np.sum((np.log(HT) - np.log(HT).mean()) ** 2))  # (local)
    R2 = 1.0 - ss_res / ss_tot  # (local)
    d_fit = -2.0 * float(coef[0])  # (local)
    return d_fit, R2, HT


def greedy_balanced_union(sectors: dict):
    """Greedy accumulation by descending eigenvalue count (lex tie-break)
    until the spectral fraction first enters [CS_LO, CS_HI]. Deterministic."""
    counts = {k: sectors[k].size for k in sectors}  # (local)
    N = sum(counts.values())  # (local)
    order = sorted(sectors.keys(), key=lambda k: (-counts[k], k))  # (local)
    S = []  # (local)
    acc = 0  # (local)
    for k in order:
        S.append(k)
        acc += counts[k]
        if CS_LO <= acc / N <= CS_HI:
            break
    return S, acc / N, N, counts


def membership_sequence(sectors: dict, S: list):
    """Diagonal elements x_k = <e_k, P_S e_k> in {0,1} in the canonical
    Peter-Weyl-adapted eigenbasis, sorted by (|lambda|, p, q) (deterministic
    tie-break). Sector purity per PROVEN block-diagonality."""
    Sset = set(S)  # (local)
    rows = []  # (local)
    for k in sorted(sectors.keys()):
        ev = sectors[k]  # (local)
        mem = 1.0 if k in Sset else 0.0  # (local)
        rows.append(np.column_stack([
            ev, np.full(ev.size, mem),
            np.full(ev.size, k[0], dtype=np.float64),
            np.full(ev.size, k[1], dtype=np.float64)]))
    R = np.vstack(rows)  # (local)
    idx = np.lexsort((R[:, 3], R[:, 2], R[:, 0]))  # (local)
    return R[idx, 0], R[idx, 1]  # sorted |lambda|, membership x_k


def log_mean_endpoint(x: np.ndarray) -> float:
    """Logarithmic mean M (paper Section 2): M(x)_n = (1/log(n+2))
    * sum_{k=0}^{n} x_k/(k+1), evaluated at the full cache depth n = N-1
    (the finite-truncation stand-in for the extended limit omega o M)."""
    N = x.size  # (local)
    ks = np.arange(N, dtype=np.float64)  # (local)
    return float(np.sum(x / (ks + 1.0)) / np.log(N + 1.0))


def szego_diagnostic(x: np.ndarray):
    """Thm 2.7 / Thm 3.2 truncation sequence f_n = Tr(P_n P_S P_n)/Tr(P_n)
    (= running mean of x in the canonical |lambda| order) + its logarithmic
    mean M(f)_n + a tail convergence-rate fit. DIAGNOSTIC ONLY."""
    N = x.size  # (local)
    ks = np.arange(N, dtype=np.float64)  # (local)
    f = np.cumsum(x) / (ks + 1.0)  # (local)
    Mf = np.cumsum(f / (ks + 1.0)) / np.log(ks + 2.0)  # (local)
    f_end = float(f[-1])  # (local)
    # tail rate fit |f_n - f_N| ~ n^{-gamma} over n in [N/4, 3N/4]   # (local)
    lo, hi = N // 4, (3 * N) // 4  # (local)
    g = np.abs(f[lo:hi] - f_end)  # (local)
    n_ax = ks[lo:hi] + 1.0  # (local)
    mask = g > 0  # (local)
    gamma, gamma_R2 = float("nan"), float("nan")  # (local)
    if mask.sum() > 10:
        A = np.vstack([np.log(n_ax[mask]), np.ones(int(mask.sum()))]).T  # (local)
        coef, *_ = np.linalg.lstsq(A, np.log(g[mask]), rcond=None)  # (local)
        pred = A @ coef  # (local)
        ss_res = float(np.sum((np.log(g[mask]) - pred) ** 2))  # (local)
        ss_tot = float(np.sum((np.log(g[mask]) - np.log(g[mask]).mean()) ** 2))  # (local)
        gamma = -float(coef[0])
        gamma_R2 = 1.0 - ss_res / ss_tot
    return f, Mf, f_end, gamma, gamma_R2, (lo, hi)


def counting_exponent(allv_sorted: np.ndarray, lam_a: float, lam_b: float):
    """Tauberian cross-check (paper Remark 2.2): Weyl law <=> lambda_k ~ k^{1/d}
    <=> d_count = d ln k / d ln lambda_k over the window [lam_a, lam_b]."""
    k_ax = np.arange(1, allv_sorted.size + 1, dtype=np.float64)  # (local)
    m = (allv_sorted >= lam_a) & (allv_sorted <= lam_b)  # (local)
    if m.sum() < 10:
        return float("nan"), float("nan")
    A = np.vstack([np.log(allv_sorted[m]), np.ones(int(m.sum()))]).T  # (local)
    coef, *_ = np.linalg.lstsq(A, np.log(k_ax[m]), rcond=None)  # (local)
    pred = A @ coef  # (local)
    ss_res = float(np.sum((np.log(k_ax[m]) - pred) ** 2))  # (local)
    ss_tot = float(np.sum((np.log(k_ax[m]) - np.log(k_ax[m]).mean()) ** 2))  # (local)
    return float(coef[0]), 1.0 - ss_res / ss_tot


# --------------------------------------------------------------------------
# Section 7 -- Main
# --------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    # 1. Input pins (first stdout lines) + plan-pin verification
    pins = log_input_pins(INPUT_FILES)
    cache_rel = str(CACHE_PATH.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
    pdf_rel = str(HM_PDF_PATH.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
    if pins[cache_rel] != CACHE_SHA_PIN:
        print(f"FATAL: cache SHA drift vs plan pin ({pins[cache_rel][:16]}... != {CACHE_SHA_PIN[:16]}...)")
        return 2
    if pins[pdf_rel] != HM_PDF_SHA_PIN:
        print(f"FATAL: HM PDF SHA drift vs plan pin ({pins[pdf_rel][:16]}... != {HM_PDF_SHA_PIN[:16]}...)")
        return 2
    print("  cache + HM PDF SHA == plan Input-SHA Ledger pins: VERIFIED")

    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print(f"  canonical consumed: tau_fold={tau_fold}, M_KK={M_KK:.15e} GeV (unit anchor),")
    print(f"                      R_therm={R_therm} (VALUE only; scoping-law citation)")
    print()

    # 2. Step (1): criterion extraction (LOCAL PDF, pypdf primary route)
    anchors, extraction_ok, n_pages = extract_criterion(HM_PDF_PATH)
    print(f"--- criterion extraction: {n_pages} pages, "
          f"{sum(1 for a in anchors if 'NOT-FOUND' not in a)}/{len(anchors)} anchors, "
          f"mandatory-complete={extraction_ok} ---")
    for a in anchors:
        print("  " + a[:150] + ("..." if len(a) > 150 else ""))
    print()

    # 3. Cache load + plan-pin asserts
    sectors = load_sectors(CACHE_PATH)
    n_sectors = len(sectors)  # (local)
    allv = np.sort(np.concatenate([sectors[k] for k in sorted(sectors)]))  # (local)
    N = allv.size  # (local)
    if N != N_EVAL_PIN or n_sectors != N_SECTORS_PIN:
        print(f"FATAL: cache content drift (N={N} vs pin {N_EVAL_PIN}; "
              f"sectors={n_sectors} vs pin {N_SECTORS_PIN})")
        return 2
    lam_min = float(allv[0])  # (local)
    lam_max = float(allv[-1])  # (local)
    print(f"cache: {n_sectors} sectors, N={N} (pins OK); "
          f"lambda_min={lam_min:.10f}, lambda_max={lam_max:.10f}")

    # bottom multiplet (degeneracy_tol; S53 lesson)
    m_min = int(np.sum(np.abs(allv - lam_min) < DEGEN_TOL))  # (local)
    bottom_intra_gap = float(allv[m_min - 1] - allv[0]) if m_min >= 2 else 0.0  # (local)
    bottom_next_gap = float(allv[m_min] - allv[0])  # (local)
    ev00 = sectors[(0, 0)]  # (local)
    m_min_00 = int(np.sum(np.abs(ev00 - lam_min) < DEGEN_TOL))  # (local)
    n_vacuum = m_min  # extracted Zel96 convention, ground-multiplet floor   # (local)
    n_vacuum_gns_family = n_sectors  # extremal invariant states on abelian C^90  # (local)
    print(f"bottom multiplet: |lambda|_min={lam_min:.10f}, m_min={m_min} "
          f"(sector (0,0) carries {m_min_00}), intra-multiplet spread={bottom_intra_gap:.3e}, "
          f"gap to next={bottom_next_gap:.6f}")
    print(f"n_vacuum = {n_vacuum} (ground-multiplet extremal floor; "
          f"companion n_vacuum_GNS_family = {n_vacuum_gns_family})")

    # dim_fix: pinned 90-projector family; all alpha_t-invariant by PROVEN
    # block-diagonality (off-diag < 8.4e-15) + PROVEN [iK_7, D_K] = 0;
    # mutually orthogonal non-zero projectors => linearly independent.
    nonzero_sectors = sum(1 for k in sectors if sectors[k].size > 0)  # (local)
    dim_fix = nonzero_sectors  # (local)
    print(f"dim_fix = {dim_fix} (span of the pinned sector-projector family; "
          f"Def 6.10 ergodicity demands 1)")
    print()

    # 4. Step (2): Weyl-applicability on the pinned window
    t_lo = 4.0 / lam_max ** 2  # (local)
    t_hi = 1.0 / (4.0 * lam_min ** 2)  # (local)
    if not (t_lo < t_hi):
        print("FATAL: degenerate window (t_lo >= t_hi)")
        return 2
    ts = np.logspace(np.log10(t_lo), np.log10(t_hi), N_T_POINTS)  # (local)
    d_fit_g, R2_g, HT_g = heat_trace_fit(allv, ts)
    weyl_ok_g = (abs(d_fit_g - WEYL_D_REF) <= WEYL_D_BAND) and (R2_g >= R2_MIN)  # (local)
    print(f"pinned window: t in [{t_lo:.6f}, {t_hi:.6f}] "
          f"({np.log10(t_hi / t_lo):.3f} decades, {N_T_POINTS} log-spaced points)")
    print(f"GLOBAL Weyl fit:  d_fit = {d_fit_g:.4f}  R2 = {R2_g:.6f}  "
          f"band |d-8|<={WEYL_D_BAND}, R2>={R2_MIN}  -> in-band = {weyl_ok_g}")

    # 5. Step (3): balanced sector-union projector + QE defect
    S, cS_plain, _, counts = greedy_balanced_union(sectors)
    Sv = np.concatenate([sectors[k] for k in S])  # (local)
    lam_min_S = float(Sv.min())  # (local)
    conj_closed = all(((q, p) in S) for (p, q) in S)  # (local)
    d_fit_l, R2_l, HT_l = heat_trace_fit(Sv, ts)
    weyl_ok_l = (abs(d_fit_l - WEYL_D_REF) <= WEYL_D_BAND) and (R2_l >= R2_MIN)  # (local)
    applicability = weyl_ok_g and weyl_ok_l  # (local)
    print(f"LOCAL  Weyl fit:  d_fit = {d_fit_l:.4f}  R2 = {R2_l:.6f}  -> in-band = {weyl_ok_l}")
    print(f"P_S: {len(S)} sectors (greedy by count desc, lex tie-break), "
          f"c_S_plain = {cS_plain:.6f}, conjugate-closed = {conj_closed}, "
          f"lambda_min(S) = {lam_min_S:.6f}")
    print(f"Weyl-applicability (BOTH fits in-band): {applicability}")

    lam_sorted, x = membership_sequence(sectors, S)
    cS_logavg = log_mean_endpoint(x)
    # mixed-membership tie diagnostic (accidental cross-sector degeneracy)
    d_l = np.diff(lam_sorted)  # (local)
    tie_edges = d_l < DEGEN_TOL  # (local)
    mixed_ties = int(np.sum(tie_edges & (np.diff(x) != 0)))  # (local)
    QE_defect_plain = float(np.mean(np.abs(x - cS_plain) >= QE_DELTA))  # (local)
    QE_defect_logavg = float(np.mean(np.abs(x - cS_logavg) >= QE_DELTA))  # (local)
    QE_defect = QE_defect_logavg  # headline: Thm-2.7 (omega.M) NC integral  # (local)
    qe_above_floor = (QE_defect_plain > QE_FLOOR) and (QE_defect_logavg > QE_FLOOR)  # (local)
    print(f"c_S: plain = {cS_plain:.6f}; (omega.M)-log-averaged = {cS_logavg:.6f}")
    print(f"QE_defect: vs c_S_plain = {QE_defect_plain:.6f}; "
          f"vs c_S_logavg (HEADLINE) = {QE_defect_logavg:.6f}; floor = {QE_FLOOR}")
    print(f"mixed-membership degenerate ties (tol {DEGEN_TOL:g}): {mixed_ties} "
          f"of {N - 1} adjacent pairs (within-tie order lex-pinned)")
    print()

    # 6. Step (6): Szego truncation-sequence diagnostic (NO verdict weight)
    f_seq, Mf_seq, f_end, gamma, gamma_R2, (fit_lo, fit_hi) = szego_diagnostic(x)
    print(f"Szego diagnostic: f_N = {f_end:.6f} (= c_S_plain); "
          f"M(f)_N = {float(Mf_seq[-1]):.6f}; tail rate |f_n - f_N| ~ n^-gamma: "
          f"gamma = {gamma:.4f} (R2 = {gamma_R2:.4f}; window [{fit_lo}, {fit_hi}])")

    # Tauberian cross-check (Remark 2.2): counting exponent on the window
    d_count, d_count_R2 = counting_exponent(allv, 1.0 / np.sqrt(t_hi), 1.0 / np.sqrt(t_lo))
    print(f"Tauberian cross-check (Remark 2.2): d_count = {d_count:.4f} "
          f"(R2 = {d_count_R2:.6f}) on lambda in [{1.0 / np.sqrt(t_hi):.3f}, {1.0 / np.sqrt(t_lo):.3f}]")
    print()

    # 7. (4,4)-repair sensitivity DIAGNOSTIC (orchestrator override input)
    sens = {}  # (local)
    if CF28_PATH.exists():
        ev44 = np.asarray(np.load(str(CF28_PATH), allow_pickle=True)["evals_44_reconstructed"],
                          dtype=np.float64)  # (local)
        sectors44 = dict(sectors)  # (local)
        sectors44[(4, 4)] = np.sort(ev44)
        allv44 = np.sort(np.concatenate([sectors44[k] for k in sorted(sectors44)]))  # (local)
        lam_min44, lam_max44 = float(allv44[0]), float(allv44[-1])  # (local)
        # window endpoints recomputed from the unioned spectrum (same formula)
        ts44 = np.logspace(np.log10(4.0 / lam_max44 ** 2),
                           np.log10(1.0 / (4.0 * lam_min44 ** 2)), N_T_POINTS)  # (local)
        d_fit_g44, R2_g44, _ = heat_trace_fit(allv44, ts44)
        S44, cS44, N44, _ = greedy_balanced_union(sectors44)
        lam44_srt, x44 = membership_sequence(sectors44, S44)
        cS44_log = log_mean_endpoint(x44)
        m_min44 = int(np.sum(np.abs(allv44 - lam_min44) < DEGEN_TOL))  # (local)
        sens = {
            "N_44": int(N44), "n_sectors_44": len(sectors44),
            "lambda_min_44": lam_min44, "lambda_max_44": lam_max44,
            "d_fit_global_44": float(d_fit_g44), "R2_global_44": float(R2_g44),
            "n_S_sectors_44": len(S44), "c_S_plain_44": float(cS44),
            "c_S_logavg_44": float(cS44_log),
            "QE_defect_plain_44": float(np.mean(np.abs(x44 - cS44) >= QE_DELTA)),
            "QE_defect_logavg_44": float(np.mean(np.abs(x44 - cS44_log) >= QE_DELTA)),
            "m_min_44": m_min44, "dim_fix_44": len(sectors44),
            "ev44_min": float(ev44.min()), "ev44_max": float(ev44.max()),
        }
        print("(4,4)-repair sensitivity (DIAGNOSTIC ONLY; verdict object is the "
              "plan-pinned 90-sector cache):")
        print(f"  N = {sens['N_44']}, sectors = {sens['n_sectors_44']}, "
              f"(4,4) evals in [{sens['ev44_min']:.4f}, {sens['ev44_max']:.4f}]")
        print(f"  d_fit_global = {sens['d_fit_global_44']:.4f} "
              f"(90-sector: {d_fit_g:.4f}; delta = {sens['d_fit_global_44'] - d_fit_g:+.4f})")
        print(f"  c_S_plain = {sens['c_S_plain_44']:.6f} ({len(S44)} sectors), "
              f"QE_defect_logavg = {sens['QE_defect_logavg_44']:.6f}, "
              f"m_min = {sens['m_min_44']}, dim_fix = {sens['dim_fix_44']}")
    else:
        print("(4,4)-repair sensitivity SKIPPED: cf28 npz not found (diagnostic only)")
    print()

    # 8. Verdict per the pre-registered plan operator (frozen 2026-06-06)
    structural_pass = qe_above_floor and (n_vacuum >= NVAC_FLOOR) and (dim_fix >= DIMFIX_FLOOR)  # (local)
    structural_fail = ((QE_defect_plain <= QE_FLOOR) and (QE_defect_logavg <= QE_FLOOR)
                       and (n_vacuum == 1) and (dim_fix == 1))  # (local)
    info_subpath = ""  # (local)
    if not extraction_ok:
        verdict = "INFO"  # (local)
        info_subpath = "c-extraction-limited"
    elif not applicability:
        verdict = "INFO"
        info_subpath = "a-global-Weyl-fit-fails" if not weyl_ok_g else "b-local-Weyl-fit-fails"
    elif structural_pass:
        verdict = "PASS"
    elif structural_fail:
        verdict = "FAIL"
        print("ESCALATION (plan FAIL_meaning): FAIL contradicts PROVEN "
              "block-diagonality -- cache SHA verified above; route to S101 "
              "priority adjudication (Q1 workshop class).")
    else:
        verdict = "INFO"
        info_subpath = "d-mixed-indicators"

    # 3-tuple ([SIGN]; mapping pre-declared in the docstring BEFORE evaluation)
    sign_v = "PASS" if n_vacuum >= NVAC_FLOOR else "FAIL"  # (local)
    mag_v = "PASS" if qe_above_floor else "FAIL"  # (local)
    if weyl_ok_g and weyl_ok_l:
        regime_v = "VALID"  # (local)
    elif weyl_ok_g or weyl_ok_l:
        regime_v = "MARGINAL"  # (local)
    else:
        regime_v = "BREAKDOWN"  # (local)

    # dual-prior discriminator (plan): in-band(both) -> 0.9 Track A; else 0.9 Track B
    track = "A" if applicability else "B"  # (local)

    print(f"=== verdict logic: applicability={applicability} (global={weyl_ok_g}, "
          f"local={weyl_ok_l}); structural_pass={structural_pass}; "
          f"extraction_ok={extraction_ok} ===")
    print(f"=== composite (plan operator) = {verdict}"
          + (f" [INFO sub-path {info_subpath}]" if info_subpath else "")
          + f"; 3-tuple = (sign={sign_v}, magnitude={mag_v}, regime={regime_v}); "
          f"dual-prior: 0.9 mass to Track {track} ===")

    # 9. Persist npz (full float64; Class 8.3 round-trip discipline)
    sector_keys = sorted(sectors.keys())  # (local)
    Sset = set(S)  # (local)
    sector_fraction_table = np.array(
        [[k[0], k[1], counts[k], counts[k] / N, 1.0 if k in Sset else 0.0]
         for k in sector_keys], dtype=np.float64)  # (local)
    np.savez_compressed(
        str(OUT_NPZ),
        # plan-required keys
        QE_defect=np.float64(QE_defect),
        n_vacuum=np.int64(n_vacuum),
        dim_fix=np.int64(dim_fix),
        c_S_plain=np.float64(cS_plain),
        c_S_logavg=np.float64(cS_logavg),
        d_fit_global=np.float64(d_fit_g),
        R2_global=np.float64(R2_g),
        d_fit_local=np.float64(d_fit_l),
        R2_local=np.float64(R2_l),
        t_window=ts,
        heat_trace_curve=np.vstack([HT_g, HT_l]),  # row0 global, row1 local(P_S)
        szego_sequence=f_seq.astype(np.float32),
        sector_fraction_table=sector_fraction_table,
        extracted_criterion_anchors=np.array(anchors, dtype=object),
        # companions + diagnostics
        QE_defect_plain=np.float64(QE_defect_plain),
        QE_defect_logavg=np.float64(QE_defect_logavg),
        n_vacuum_GNS_family=np.int64(n_vacuum_gns_family),
        szego_logmean_sequence=Mf_seq.astype(np.float32),
        szego_rate_gamma=np.float64(gamma),
        szego_rate_R2=np.float64(gamma_R2),
        szego_rate_fit_window=np.array([fit_lo, fit_hi], dtype=np.int64),
        tauberian_d_count=np.float64(d_count),
        tauberian_d_count_R2=np.float64(d_count_R2),
        lambda_min=np.float64(lam_min),
        lambda_max=np.float64(lam_max),
        m_min=np.int64(m_min),
        m_min_sector00=np.int64(m_min_00),
        bottom_intra_gap=np.float64(bottom_intra_gap),
        bottom_next_gap=np.float64(bottom_next_gap),
        lambda_min_S=np.float64(lam_min_S),
        S_sector_list=np.array([[k[0], k[1]] for k in S], dtype=np.int64),
        S_conjugate_closed=np.bool_(conj_closed),
        mixed_membership_ties=np.int64(mixed_ties),
        N_eval=np.int64(N),
        n_sectors=np.int64(n_sectors),
        weyl_ok_global=np.bool_(weyl_ok_g),
        weyl_ok_local=np.bool_(weyl_ok_l),
        applicability=np.bool_(applicability),
        extraction_ok=np.bool_(extraction_ok),
        verdict=np.str_(verdict),
        info_subpath=np.str_(info_subpath),
        sign_verdict=np.str_(sign_v),
        magnitude_verdict=np.str_(mag_v),
        regime_verdict=np.str_(regime_v),
        dual_prior_track=np.str_(track),
        sensitivity_44_json=np.str_(json.dumps(sens, sort_keys=True)),
        pins_json=np.str_(json.dumps(pins, sort_keys=True)),
        thresholds_json=np.str_(json.dumps({
            "QE_FLOOR": QE_FLOOR, "QE_DELTA": QE_DELTA,
            "WEYL_D_REF": WEYL_D_REF, "WEYL_D_BAND": WEYL_D_BAND,
            "R2_MIN": R2_MIN, "CS_BAND": [CS_LO, CS_HI],
            "DEGEN_TOL": DEGEN_TOL, "N_EVAL_PIN": N_EVAL_PIN,
            "N_T_POINTS": N_T_POINTS, "NVAC_FLOOR": NVAC_FLOOR,
            "DIMFIX_FLOOR": DIMFIX_FLOOR, "tau_fold": tau_fold,
        }, sort_keys=True)),
        scheme=np.str_(SCHEME),
        convention=np.str_(CONVENTION),
        L_max=np.int64(L_MAX),
        audit_sha256=np.str_(audit_sha),
        content_sha256=np.str_(content_sha),
    )
    print(f"npz written: {OUT_NPZ.name}")

    # 10. Plot (3 panels per plan output_artifacts)
    fig, axes = plt.subplots(1, 3, figsize=(17.5, 5.2))  # (local)
    ax = axes[0]  # (local)
    ax.loglog(ts, HT_g, "o", ms=3.5, color="#1f77b4", label=f"global Tr(e^-tD^2): d_fit={d_fit_g:.3g}, R2={R2_g:.4f}")
    Ag = np.exp(np.polyval(np.polyfit(np.log(ts), np.log(HT_g), 1), np.log(ts)))  # (local)
    ax.loglog(ts, Ag, "-", color="#1f77b4", lw=1)
    ax.loglog(ts, HT_l, "s", ms=3.5, color="#ff7f0e", label=f"local Tr(P_S e^-tD^2): d_fit={d_fit_l:.3g}, R2={R2_l:.4f}")
    Al = np.exp(np.polyval(np.polyfit(np.log(ts), np.log(HT_l), 1), np.log(ts)))  # (local)
    ax.loglog(ts, Al, "-", color="#ff7f0e", lw=1)
    mid = N_T_POINTS // 2  # (local)
    ref = HT_g[mid] * (ts / ts[mid]) ** (-WEYL_D_REF / 2.0)  # (local)
    ax.loglog(ts, ref, "--", color="gray", lw=1.2, label="HM Def 2.3 reference t^-4 (d=8)")
    ax.axvspan(t_lo, t_hi, color="green", alpha=0.06)
    ax.set_xlabel("t  [M_KK^-2]")
    ax.set_ylabel("heat trace")
    ax.set_title(f"Weyl-applicability on pinned window\n[4/lam_max^2, 1/(4 lam_min^2)] = [{t_lo:.4f}, {t_hi:.4f}]")
    ax.legend(fontsize=7.5, loc="lower left")

    ax = axes[1]
    n0 = int(np.sum(x < 0.5))  # (local)
    n1 = int(N - n0)  # (local)
    ax.bar([0.0, 1.0], [n0 / N, n1 / N], width=0.08, color=["#888", "#d62728"])
    ax.axvline(cS_plain, color="red", lw=1.5, label=f"c_S plain = {cS_plain:.4f}")
    ax.axvline(cS_logavg, color="purple", lw=1.5, label=f"c_S (omega.M) = {cS_logavg:.4f}")
    ax.axvspan(cS_plain - QE_DELTA, cS_plain + QE_DELTA, color="red", alpha=0.07)
    ax.axvspan(cS_logavg - QE_DELTA, cS_logavg + QE_DELTA, color="purple", alpha=0.07)
    ax.set_xlabel("<e_k, P_S e_k>  (sector purity => {0,1})")
    ax.set_ylabel("fraction of modes")
    ax.set_title(f"QE diagonal elements vs NC integral\nQE_defect = {QE_defect_logavg:.4f} (headline) / {QE_defect_plain:.4f} (plain); floor {QE_FLOOR}")
    ax.legend(fontsize=8)

    ax = axes[2]
    sub = np.unique(np.geomspace(1, N, 4000).astype(int)) - 1  # (local)
    ax.semilogx(sub + 1, f_seq[sub], color="#2ca02c", lw=1.2, label="f_n = Tr(P_n P_S P_n)/Tr(P_n)")
    ax.semilogx(sub + 1, Mf_seq[sub], color="#9467bd", lw=1.2, label="M(f)_n (logarithmic mean)")
    ax.axhline(cS_plain, color="red", ls="--", lw=1, label=f"f_N = {f_end:.4f}")
    ax.set_xlabel("n (modes, |lambda|-ordered)")
    ax.set_ylabel("truncated NC integral of P_S")
    ax.set_title(f"Szego/Thm-2.7 truncation sequence (DIAGNOSTIC)\ntail rate gamma = {gamma:.3f} (R2 = {gamma_R2:.3f}); M(f)_N = {float(Mf_seq[-1]):.4f}")
    ax.legend(fontsize=8, loc="center left")

    fig.suptitle(f"{GATE_ID}: {verdict}"
                 + (f" [sub-path {info_subpath}]" if info_subpath else "")
                 + f"  |  n_vacuum={n_vacuum}, dim_fix={dim_fix}, QE_defect={QE_defect_logavg:.4f}  |  "
                 f"3-tuple (sign={sign_v}, mag={mag_v}, regime={regime_v})  |  L_max=12, tau_fold={tau_fold}",
                 fontsize=10)
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    fig.savefig(str(OUT_PNG), dpi=140)
    plt.close(fig)
    print(f"png written: {OUT_PNG.name}")
    print()

    # 11. 4-tuple + verdict payload (agent calls emit_verdict; session "100b")
    value = (f"INFO-subpath-{info_subpath};" if info_subpath else "") + (
        f"QE_defect={QE_defect_logavg:.4f};QE_defect_plain={QE_defect_plain:.4f};"
        f"n_vacuum={n_vacuum};dim_fix={dim_fix};"
        f"c_S_plain={cS_plain:.4f};c_S_logavg={cS_logavg:.4f};"
        f"d_fit_global={d_fit_g:.3g};R2_global={R2_g:.4f};"
        f"d_fit_local={d_fit_l:.3g};R2_local={R2_l:.4f};"
        f"weyl_applicability={'PASS' if applicability else 'FAIL'};"
        f"track={track}-0.9;N={N};sectors={n_sectors}")  # (local)
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)
    extra_rows = [
        ("# UNTRUSTED-UPSTREAM caveat: consumes s84 cache lineage flagged by "
         "S100b-TAU0-LAITEH-REDUCTION ESCALATION (STRUCTURED LC t=1/2; eigensolver "
         "control-verified; canonicity adjudication pending) — dispatched per "
         "pre-registered orchestrator triage"),
        ("# composite-precedence: plan SS W4-1 gate-block operator pre-registers INFO on "
         "Weyl-applicability failure (guard, not hypothesis); generic gate-verdicts.md "
         "collapse of (PASS,PASS,MARGINAL) would read PASS; the plan-specific operator "
         "governs the composite. Dual-prior discriminator: 0.9 mass to Track "
         + track + "."),
        ("# extracted HM Example 6.12.2: almost-commutative manifolds are NOT classically "
         "ergodic (paper-native structural corroboration of the n_vacuum>1 direction; "
         "no verdict weight -- the composite keys on the applicability guard)"),
        ("# regulator_pin: N/A -- no Seeley-DeWitt a_n citation, no Mellin-residue "
         "evaluation (Dixmier-trace functional via HM Thm 2.7 truncation formula); "
         "(4,4)-repair sensitivity input runtime-pinned in pinmap (diagnostic only)"),
    ]  # (local)
    print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=sign_v, magnitude_verdict=mag_v,
                          regime_verdict=regime_v,
                          companion_note=f"L_max=12 90-sector cache; INFO sub-path {info_subpath or 'n/a'}",
                          extra_rows=extra_rows)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0  # valid verdict regardless of PASS/FAIL/INFO


if __name__ == "__main__":
    sys.exit(main())
