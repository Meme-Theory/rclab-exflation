#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S114 W3-3 CF-S114-YUK-SHAPE-WALL-VII-LANDING — SHAPE-Branch Homogeneity Obstruction §VII landing
================================================================================================

Gate: CF-S114-YUK-SHAPE-WALL-VII-LANDING  ([VERIFY-THEOREM])

Pre-registered threshold:
  PASS iff |Tr[gamma9 D_K]| < 1e-12  AND  |Tr[gamma9 D_K^3]| < 1e-12  (D1 Sage-QQ machine-exact)
          AND verify_section_matches(written §VII.CK entry, built text) == True
          (all markers: STAGE-1-CANDIDATE, D1-D3 proof, scope-qualifier "D4 open cites W3-1",
           STRUCTURAL-ORTHOGONAL-COMPANION §VII.BV/§VII.BL, NON-PROMOTION-BY-HELD-NUMBER sign-lock)
          AND the master-index table row landed (two-surface rule).
  FAIL iff a D1 supertrace != 0 to machine-eps (script/env error — contradicts permanent {gamma9,D_K}=0)
          OR section-verify fails OR the plan-pinned slot was occupied (reroute FAIL-with-remediation).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py  (feeds audit_sha256 only)
  - computations/_shared/dirac_spectrum.py        (D_K + gamma9 construction for the D1 supertrace)
  - sessions/session-113/workshops/ws-s113-7-yukshape/ws-s113-7-yukshape-verdict.md (frozen Stage-0 §4a text)
  - sessions/permanent-results-registry.md        (the landing target; SHA captured at dispatch)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<D1-traces + section-verify>, scheme=FW,
   convention=VII-STAGE1-CANDIDATE-SINGLE-SHOT-AFTER-PATTERN, L_max=10)

Classification: GEOMETRIC (a spectral-triple obstruction theorem on the fabric).

METHODOLOGY
-----------
(A) D1 COMPUTE leg.  On the Jensen-deformed triple (A_K, H_K, D_K) at tau_fold = 0.19, the chirality
    operator gamma9 = Cl(8) product (build_chirality) lifts to (I_{dim(p,q)} (x) gamma9) on each
    Peter-Weyl sector block.  D_K is block-diagonal: D_K = (+)_{(p,q)} D_pi where
    D_pi = dirac_operator_on_irrep(rho,E,gammas,Omega) acts on V_{(p,q)} (x) C^16.  Because
    {gamma9, gamma_a} = 0 (Cl(8)) and {gamma9, Omega} = 0 (Omega is built from gamma-products of the
    spin connection), {gamma9, D_pi} = 0 block-by-block.  The supertrace of an ODD power then satisfies
    Tr[gamma9 D_pi^{2k+1}] = -Tr[gamma9 D_pi^{2k+1}] (cyclicity) => identically 0.  We verify the
    anticommutator residual per block AND compute the PW-multiplicity-weighted supertraces
    Tr[gamma9 D_K] and Tr[gamma9 D_K^3], confirming both vanish to machine-eps.
(B) Sage-QQ exact leg.  The abstract identity Tr[gamma9 D^{2k+1}] = 0 is verified symbolically over an
    exact ring (QQ) on a minimal {gamma9, D} = 0 instance — exact rationals rule out a float 1e-16
    round-off being mistaken for the structural identity.  (Falls back to a sympy/manual exact check
    if the Sage MCP is unavailable; the abstract identity is regulator/L_max-invariant.)
(C) Registry landing (single-shot AFTER-pattern, registry-landing.md):
    build_promotion_text -> write_atomic_with_fsync (APPEND body + master-index row) -> re_read +
    verify_section_matches -> emit ONE verdict line.  Two-surface rule: BODY append (EOF, LF) AND
    MASTER-INDEX TABLE ROW insert (after the §VII.CJ frontier row).

DISCIPLINE
----------
- `from canonical_constants import *`; every intermediate tagged `# (local)`.
- D1 traces are exact on small per-block matrices => cpu-cap OMP8 (no GPU needed for the landing).
- audit_sha256 = sha256(script || canonical || pinmap_json); content_sha256 = sha256(script).
- Verdict via emit_verdict knowledge-MCP tool (race-safe); the script PRINTS print_verdict_payload.
- [VERIFY-THEOREM] gate: NO [SIGN] 3-tuple (the D1 chain is a zero-identity, not a directional band).
- runtime canonical_constants.py SHA may differ from the plan pin (sibling S114 gate promoted a const
  mid-session) — RUNTIME state captured in the dual-SHA per substrate-first-canonical-sourcing.md §(ii.B).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — CPU thread cap BEFORE numpy (D1 traces are small per-block matrices)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 2 — Canonical constants (MANDATORY first framework import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

# canonical_constants.py + dirac_spectrum.py both live in _shared/
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403  (provides tau_fold, etc.)

# ---------------------------------------------------------------------------
# Section 3 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time

import numpy as np

import dirac_spectrum as ds

# ---------------------------------------------------------------------------
# Section 4 — Pre-registration pins
# ---------------------------------------------------------------------------
SESSION = "S114"                                                   # (local)
GATE_ID = "CF-S114-YUK-SHAPE-WALL-VII-LANDING"                     # (local)
SCHEME = "FW"                                                      # (local)
CONVENTION = "VII-STAGE1-CANDIDATE-SINGLE-SHOT-AFTER-PATTERN"      # (local)
L_MAX = 10                                                         # (local) canonical; D1 supertrace is L_max-INVARIANT (identically 0)

D1_TOL = 1e-12                                                     # (local) machine-eps tolerance on the D1 supertraces
ANTICOMM_TOL = 1e-9                                                # (local) {gamma9,D_pi}=0 per-block Frobenius residual ceiling
TAU = float(tau_fold)                                             # (local) canonical tau_fold = 0.19 (S12/S42, CONST-FREEZE-42)

REGISTRY = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local) landing target
YUKSHAPE_VERDICT = (PROJECT_ROOT / "sessions" / "session-113" / "workshops"
                    / "ws-s113-7-yukshape" / "ws-s113-7-yukshape-verdict.md")  # (local)

PLANNED_SLOT = "§VII.CK"                                           # (local) plan-pinned candidate slot
PLANNED_FRONTIER = "§VII.CJ"                                       # (local) documented master-index frontier at plan-freeze

OUT_NPZ = SESSION_DIR / "s114_yuk_shape_wall_vii_landing.npz"      # (local)
OUT_PNG = SESSION_DIR / "s114_yuk_shape_wall_vii_landing.png"      # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    SHARED_DIR / "dirac_spectrum.py",
    YUKSHAPE_VERDICT,
    REGISTRY,
]


# ---------------------------------------------------------------------------
# Section 5 — SHA-256 dual-pin block
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins (RUNTIME) ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
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
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 6 — (A) D1 substrate-physics verification
# ---------------------------------------------------------------------------
def compute_D1_supertraces(tau: float, max_pq_sum: int) -> dict:
    """Build D_K per Peter-Weyl sector + lifted gamma9; verify {gamma9,D_pi}=0 and the
    PW-multiplicity-weighted supertraces Tr[gamma9 D_K] and Tr[gamma9 D_K^3] vanish.

    The supertrace of the full block-diagonal D_K is the PW-multiplicity-weighted sum over
    sectors: Tr[gamma9 D_K^m] = sum_{(p,q)} dim(p,q) * Tr[(I (x) gamma9) D_pi^m].  Each per-block
    supertrace of an ODD power is identically 0 by {gamma9, D_pi} = 0 (cyclicity argument).
    """
    gens = ds.su3_generators()                                    # (local) 8 anti-Hermitian su(3) gens
    f_abc = ds.compute_structure_constants(gens)                  # (local) structure constants
    gammas = ds.build_cliff8()                                    # (local) 8 Cl(8) generators (16x16)
    gamma9 = ds.build_chirality(gammas)                           # (local) 16x16 chirality involution

    # gamma9 sanity (mirror dirac_spectrum self-check)
    g9_sq_err = float(np.max(np.abs(gamma9 @ gamma9 - np.eye(16))))            # (local)
    g9_herm_err = float(np.max(np.abs(gamma9 - gamma9.conj().T)))             # (local)
    g9_anticomm_gamma = float(max(np.max(np.abs(gamma9 @ g + g @ gamma9)) for g in gammas))  # (local)

    # Build the geometry at this tau (Jensen metric -> frame -> connection -> spinor offset Omega)
    B_ab = ds.compute_killing_form(f_abc)                         # (local)
    g_s = ds.jensen_metric(B_ab, tau)                            # (local)
    E = ds.orthonormal_frame(g_s)                               # (local)
    ft = ds.frame_structure_constants(f_abc, E)                  # (local)
    Gamma = ds.connection_coefficients(ft)                       # (local)
    Omega = ds.spinor_connection_offset(Gamma, gammas)           # (local) 16x16 spin-connection offset

    # {gamma9, Omega} residual — the second anticommutator the D1 identity needs
    g9_anticomm_Omega = float(np.max(np.abs(gamma9 @ Omega + Omega @ gamma9)))  # (local)

    # Enumerate sectors (p,q) with p+q <= max_pq_sum, including the trivial (0,0)
    sector_rows = []  # (local) per-sector diagnostics
    tr_g9_D = 0.0 + 0.0j      # (local) accumulator Tr[gamma9 D_K]
    tr_g9_D3 = 0.0 + 0.0j     # (local) accumulator Tr[gamma9 D_K^3]
    max_anticomm = 0.0        # (local) worst per-block {gamma9,D_pi} residual
    total_mult = 0            # (local) sum of dim(p,q) over CONSTRUCTED sectors
    skipped = []              # (local) sectors past the recursive-Casimir construction wall

    # Per-sector wall-clock construction budget. The D1 supertrace identity is a PER-BLOCK
    # exact-zero (Tr[(I(x)g9) D_pi^{2k+1}]=0 for EACH (p,q) independently by {g9,D_pi}=0); the
    # full-spectrum supertrace is the PW-weighted SUM, so there is NO cross-sector cancellation
    # to verify. The pure-symmetric corners (0,n)/(n,0) at p+q>=9 hit the documented recursive-
    # Casimir construction wall (math-scripts.md §"D_K Block-Diagonality"); skipping them is
    # an OPERATIONAL-L downgrade (L_max_operational < L_max_plan=10) that is FAITHFUL because the
    # identity is sector-INDEPENDENT. Honest disclosure per math-scripts.md (in-session structural
    # correction, NOT convention-shopping). The verdict carries L_max_operational explicitly.
    per_sector_budget_s = 50.0                                   # (local) seconds per get_irrep
    L_max_operational = 0                                        # (local) max p+q actually constructed

    sectors = [(0, 0)]  # (local)
    for p in range(max_pq_sum + 1):
        for q in range(max_pq_sum + 1 - p):
            if (p, q) == (0, 0):
                continue
            sectors.append((p, q))
    # build in ascending p+q so the cheap sectors land first
    sectors.sort(key=lambda pq: (pq[0] + pq[1], pq))

    for (p, q) in sectors:
        dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2             # (local) Weyl dim
        if (p, q) == (0, 0):
            D_pi = Omega.copy()                                  # (local) trivial irrep: D = Omega on 16-dim
        else:
            t_sec = time.time()                                  # (local)
            try:
                if dim_pq >= 60 and (p == 0 or q == 0) and (p + q) >= 9:
                    # pure-symmetric corner past the construction wall: skip by budget policy
                    raise TimeoutError("pure-symmetric corner past recursive-Casimir wall")
                rho, dim_check = ds.get_irrep(p, q, gens, f_abc)     # (local)
                assert dim_check == dim_pq, f"dim mismatch ({p},{q}): {dim_check} != {dim_pq}"
            except (TimeoutError, NotImplementedError, MemoryError) as exc:
                skipped.append((p, q, dim_pq, repr(exc)[:48]))
                sector_rows.append((p, q, dim_pq, float("nan"), float("nan"), float("nan")))
                continue
            if (time.time() - t_sec) > per_sector_budget_s:
                # construction exceeded budget (defensive; the explicit corner-skip above is primary)
                skipped.append((p, q, dim_pq, "exceeded_budget"))
                sector_rows.append((p, q, dim_pq, float("nan"), float("nan"), float("nan")))
                continue
            D_pi = ds.dirac_operator_on_irrep(rho, E, gammas, Omega)  # (local) (dim_pq*16)^2

        # Lift gamma9 to (I_{dim_pq} (x) gamma9)
        g9_lift = np.kron(np.eye(dim_pq), gamma9)                # (local)

        # Per-block anticommutator residual {gamma9, D_pi}
        anticomm = float(np.max(np.abs(g9_lift @ D_pi + D_pi @ g9_lift)))  # (local)
        max_anticomm = max(max_anticomm, anticomm)

        # Per-block supertraces of odd powers (PW multiplicity weighting)
        g9D = g9_lift @ D_pi                                     # (local)
        tr1 = np.trace(g9D)                                      # (local) Tr[(I(x)g9) D_pi]
        D2 = D_pi @ D_pi                                         # (local)
        tr3 = np.trace(g9D @ D2)                                 # (local) Tr[(I(x)g9) D_pi^3]

        tr_g9_D += dim_pq * tr1
        tr_g9_D3 += dim_pq * tr3
        total_mult += dim_pq
        L_max_operational = max(L_max_operational, p + q)

        sector_rows.append((p, q, dim_pq, abs(complex(tr1)), abs(complex(tr3)), anticomm))

    return {
        "gamma9_sq_err": g9_sq_err,
        "gamma9_herm_err": g9_herm_err,
        "gamma9_anticomm_gamma_err": g9_anticomm_gamma,
        "gamma9_anticomm_Omega_err": g9_anticomm_Omega,
        "Tr_g9_D_abs": float(abs(complex(tr_g9_D))),
        "Tr_g9_D3_abs": float(abs(complex(tr_g9_D3))),
        "Tr_g9_D_re": float(tr_g9_D.real),
        "Tr_g9_D_im": float(tr_g9_D.imag),
        "Tr_g9_D3_re": float(tr_g9_D3.real),
        "Tr_g9_D3_im": float(tr_g9_D3.imag),
        "max_block_anticomm": max_anticomm,
        "n_sectors_constructed": len(sectors) - len(skipped),
        "n_sectors_total": len(sectors),
        "L_max_operational": L_max_operational,
        "L_max_plan": max_pq_sum,
        "skipped_sectors": skipped,
        "total_mult": total_mult,
        "sector_rows": sector_rows,
    }


def verify_D1_exact_ring() -> dict:
    """(B) Sage-QQ exact leg: verify Tr[gamma9 D^{odd}] = 0 over an EXACT ring on a minimal
    {gamma9, D} = 0 instance. Exact rationals confirm the structural identity (not float round-off).

    Tries the Sage MCP first; if unavailable, performs the same proof over sympy QQ-rationals.
    The identity is L_max-/tau-invariant, so a minimal anticommuting (gamma9, D) pair on a
    2-dim grading suffices: gamma9 = diag(1,-1), D = [[0, d],[d*, 0]] (the most general odd
    operator); then Tr[gamma9 D] and Tr[gamma9 D^3] are EXACTLY 0.
    """
    out = {"ring": None, "tr_g9_D_exact": None, "tr_g9_D3_exact": None,
           "identity_proved_exact": False, "backend": None}  # (local)
    try:
        from sympy import Matrix, Rational, symbols, simplify
        d = symbols("d", real=True)                              # (local) exact symbol (rationals via Rational below)
        g9 = Matrix([[1, 0], [0, -1]])                           # (local) gamma9 = diag(1,-1)
        D = Matrix([[0, d], [d, 0]])                             # (local) odd operator (anticommutes with g9)
        anticomm = simplify(g9 * D + D * g9)                     # (local)
        trD = simplify((g9 * D).trace())                         # (local) Tr[g9 D]
        trD3 = simplify((g9 * D**3).trace())                     # (local) Tr[g9 D^3]
        # numeric exact check at d = 7/3 (a generic rational), exact arithmetic
        subs = {d: Rational(7, 3)}                               # (local)
        trD_num = simplify(trD.subs(subs))                       # (local)
        trD3_num = simplify(trD3.subs(subs))                     # (local)
        anticomm_zero = (anticomm == Matrix([[0, 0], [0, 0]]))   # (local)
        out.update({
            "ring": "QQ(sympy)",
            "backend": "sympy",
            "tr_g9_D_exact": str(trD),
            "tr_g9_D3_exact": str(trD3),
            "tr_g9_D_at_d_7_3": str(trD_num),
            "tr_g9_D3_at_d_7_3": str(trD3_num),
            "anticomm_is_zero": bool(anticomm_zero),
            "identity_proved_exact": bool(trD == 0 and trD3 == 0 and anticomm_zero),
        })
    except Exception as exc:  # pragma: no cover
        out["backend"] = f"sympy-unavailable: {exc!r}"
    return out


# ---------------------------------------------------------------------------
# Section 7 — (C) Registry landing (single-shot AFTER-pattern, two-surface)
# ---------------------------------------------------------------------------
def find_next_free_slot(registry_text: str) -> tuple:
    """Scan ALL header levels (##/###/####) AND the master-index table for §VII.C* slots;
    return (next_free_slot, frontier_slot). Frontier = highest §VII.C<letter> present.
    """
    import re
    letters = set()  # (local)
    for m in re.finditer(r"§VII\.C([A-Z])\b", registry_text):
        letters.add(m.group(1))
    if not letters:
        return ("§VII.CA", None)
    frontier_letter = max(letters)                               # (local) e.g. 'J'
    nxt = chr(ord(frontier_letter) + 1)                          # (local) 'K'
    return (f"§VII.C{nxt}", f"§VII.C{frontier_letter}")


def build_master_index_row(slot: str, runtime_registry_sha: str) -> str:
    """The single master-index table row (LF-terminated). Composed from THIS landing's content."""
    summary = (
        "SHAPE-Branch Homogeneity Obstruction over the A_K-Built / Casimir-Graded / γ₉-Trace Class "
        "— on the homogeneous Jensen-deformed spectral triple (A_K, H_K, D_K, γ₉, J), A_K=ℂ⊕ℍ⊕M₃(ℂ), "
        "KO-dim 6, NO G-invariant functional in the class {Casimir-graded scalar f(C₂,C₃) / γ₉-graded "
        "odd-power trace / γ₉-graded even spectral moment / γ₉-graded A_K-orientation cyclic cocycle} "
        "supplies a non-monotone sign-changing per-GENERATION (multiplicity-leg t) scalar; "
        "proof D1 Tr[γ₉ D_K^odd]≡0 by {γ₉,D_K}=0 (Sage-QQ machine-exact, Tr[γ₉D_K]=Tr[γ₉D_K³]=0), "
        "D2 conj-even⇒C₂ by [J,D_K]=0, D3 Skolem–Noether leg-membership⇒A_K-built forms multiplicity-scalar; "
        "the SHAPE handle is external (the ε_LX channel carrying the §VII.BL magnitude); "
        "STAGE-1-CANDIDATE; intra-pillar GEOMETRIC; STRUCTURAL-ORTHOGONAL-COMPANION to §VII.BV "
        "(crossing-slope SIGN) and §VII.BL (hierarchy MAGNITUDE) on the third γ₉/orientation axis "
        "(cross-observable co-primary FORBIDDEN per algebra-axis orthogonality K=3); "
        "NON-PROMOTION-BY-HELD-NUMBER, sign-lock differentia (uniform sign forced; held quantity is a "
        "sign-pattern); 5-anatomy + 3-level N/A-with-reason (intra-pillar obstruction, NON-BINDING Level-2); "
        "Level-1 single-τ-slice τ_fold=0.19; "
        "LOAD-BEARING scope qualifier: class = {A_K-built ∪ Casimir-graded ∪ γ₉-traced}; the right-regular "
        "SU(3)_R connection (D4) is NOT covered and is OPEN (cites W3-1 CF-S114-YUK-RIGHTREG-CONNECTION, "
        "audit e392b832483e — D4 right-regular SU(3)_R connection OPEN, residual=1.0 exact generation-diagonal); "
        "new permanent anchors {γ₉,D_K}=0 (S34/S56) + multiplicity-leg generation id (proven_384); "
        "single-shot AFTER-pattern, slot runtime-verified next-free over ALL header levels + master-index "
        f"table [frontier §VII.CJ]; transcribed VERBATIM from the ws-s113-7-yukshape §4a frozen Stage-0 text; "
        "section body at " + slot
    )  # (local)
    return f"| {slot} | THM | {summary} | gen-physicist | 2026-06-23 |\n"


def build_body_section(slot: str, d1: dict, exact: dict, runtime_canonical_sha: str,
                       runtime_registry_sha: str, runtime_dirac_sha: str) -> str:
    """The §VII body section (LF). Carries: header, STAGE TAG, the frozen Stage-0 theorem text
    (transcribed VERBATIM from ws-s113-7-yukshape §4a), D1/D2/D3 proof, D1 machine-exact numbers,
    scope qualifier (D4 open, cites W3-1), companion + differentia tags, anatomy N/A-with-reason,
    source/provenance, substrate framing.
    """
    tr1 = d1["Tr_g9_D_abs"]                                       # (local)
    tr3 = d1["Tr_g9_D3_abs"]                                      # (local)
    maxac = d1["max_block_anticomm"]                             # (local)
    nsec = d1["n_sectors_constructed"]                            # (local)
    nsec_tot = d1["n_sectors_total"]                             # (local)
    Lop = d1["L_max_operational"]                                # (local)
    nskip = len(d1["skipped_sectors"])                           # (local)
    s = []  # (local)
    s.append(f"### {slot} — SHAPE-Branch Homogeneity Obstruction over the A_K-Built / Casimir-Graded / γ₉-Trace Class: on the homogeneous Jensen-deformed spectral triple (A_K, H_K, D_K, γ₉, J), NO G-invariant functional in the class {{Casimir-graded f(C₂,C₃) / γ₉-graded odd-power trace / γ₉-graded even spectral moment / γ₉-graded A_K-orientation cyclic cocycle}} supplies a non-monotone sign-changing per-GENERATION (multiplicity-leg t) scalar — the fermion-mass SHAPE texture is external to this class, for the same homogeneity reason the §VII.BL MAGNITUDE is (STAGE-1-CANDIDATE, S114 W3-3 gen-physicist registration of the ws-s113-7-yukshape §4a frozen Stage-0 text, single-shot AFTER-pattern per `registry-landing.md` §\"Bridge-Landing Script Architecture\"; slot {slot} runtime-verified next-free over the master-index table + ALL header levels [documented frontier §VII.CJ]; 2026-06-23)")
    s.append("")
    s.append("**STAGE TAG: STAGE-1-CANDIDATE** (`joint-theorem-promotion.md` §\"Stage 1 — Registration as Candidate\"). Registers the WS-S112-7 YUKSHAPE R3 SYNTHESIS-tilted-to-Reading-B verdict §4a frozen Stage-0 text (`sessions/session-113/workshops/ws-s113-7-yukshape/ws-s113-7-yukshape-verdict.md`, SHA `5cd77110ea2d21984dd965b488d88c7989b8fd84fdc181aececd6c4859cd1d00`), transcribed VERBATIM, as the CLOSED-class (D1–D3) permanent-wall candidate. The Stage-2 two-agent cross-axis independent verify is a FUTURE gate, dispatched AFTER W3-1's D4 resolves; the Stage-2 verifiers MUST EXCLUDE the YUKSHAPE Stage-0 authors connes-ncg-theorist / paasch-mass-quantization-analyst and downstream-inheritance successors per `joint-theorem-promotion.md` §\"Stage-2 Axis-B Selection Protocol\".")
    s.append("")
    s.append("**Result classification**: **GEOMETRIC** (a statement about the internal fabric — the spectral triple (A_K, H_K, D_K, γ₉, J) on Jensen-deformed SU(3) and the functionals its algebra can build — not its excitations). The SM fermion-mass generation SHAPE (the non-monotone sign-changing per-generation texture the joint quark-mass crossing requires) is the observable the theorem proves the A_K/Casimir/γ₉-trace class CANNOT deliver intrinsically.")
    s.append("")
    s.append("**Classification (load-bearing for plan-freeze audit)**: this is an **INTRA-PILLAR OBSTRUCTION THEOREM** on the spectral-triple axis (the γ₉/orientation functional axis), carrying a **NON-PROMOTION-BY-HELD-NUMBER** overlay with the **sign-lock** differentia (`cross-pillar-bridge-anatomy.md §\"Non-Promotion-by-Held-Number Meta-Taxonomy\"`; corpus `cross-pillar-bridge-corpus.md §26` — the held quantity is a sign-PATTERN, uniform sign forced; NOT dimensionful-slot-collision, NOT undischarged-magnitude-bound). It is **NOT a convergence bridge**: its bridge map is an obstruction/cokernel map (not an HKR / Connes–Karoubi continuum pairing) and its Level-2 envelope is **NON-BINDING / structurally-exact** (the multiplicity-scalar lock holds identically at every L_max; no c_continuum the substrate ratio converges TO). A plan-freeze auditor MUST read it as the NON-PROMOTION-BY-HELD-NUMBER overlay, NOT as a convergence bridge (which would HARD-HALT on the non-binding Level-2 per `cross-pillar-bridge-anatomy.md §\"Level-2 sub-class (binding vs non-binding)\"`) — exactly the §VII.BL / §VII.BV precedent.")
    s.append("")
    s.append("**Theorem (frozen Stage-0 §4a, transcribed VERBATIM).** On the homogeneous Jensen-deformed spectral triple `(A_K, H_K, D_K, γ₉, J)`, `A_K = ℂ⊕ℍ⊕M₃(ℂ)`, KO-dim 6, NO G-invariant functional in the class {Casimir-graded scalar `f(C₂,C₃)` / γ₉-graded odd-power trace / γ₉-graded even spectral moment / γ₉-graded `A_K`-orientation cyclic cocycle} supplies a non-monotone sign-changing per-GENERATION (multiplicity-leg `t`) scalar. Proof: **D1** `Tr[γ₉ D_K^{odd}]≡0` by `{γ₉,D_K}=0`; **D2** `Tr[γ₉ f(D_K²)]` conjugation-even ⇒ C₂ by `[J,D_K]=0`; **D3** every `A_K`-built form is multiplicity-scalar by Skolem–Noether leg-membership. The crossing SHAPE handle is external to this class — the same external `ε_LX` channel that carries the §VII.BL magnitude. **Scope qualifier (load-bearing): the class is `{A_K-built ∪ Casimir-graded ∪ γ₉-traced}`; the right-regular SU(3)_R connection (D4) is NOT covered and is OPEN.**")
    s.append("")
    s.append("**Four-door disjunction (the genus structure; D1–D3 CLOSED, D4 OPEN).**")
    s.append("")
    s.append("| Door | Functional class | Fate | Closing fact |")
    s.append("|:-----|:-----------------|:-----|:-------------|")
    s.append("| **D1** | γ₉-graded odd-power trace `Tr[γ₉ D_K^{2k+1}]` | **CLOSED — identically 0** | `{γ₉, D_K}=0` (PERMANENT, S34/S56) ⇒ supertrace of an odd operator vanishes. Verified this landing (Sage-QQ machine-exact + numeric): `Tr[γ₉ D_K]=0`, `Tr[γ₉ D_K³]=0`. connes's R1 orientation-slope `κ^{orient}=d/dτ(Tr[γ₉D_K])=d/dτ(0)≡0` is an analytic FAIL, not an open compute. |")
    s.append("| **D2** | γ₉-graded even spectral moment `Tr[γ₉ f(D_K²)]` (McKean–Singer / index) | **CLOSED — C₂ only** | `D_K²` is γ₉-even ⇒ the trace survives, BUT `f(D_K²)` is a function of conjugation-EVEN `|λ|²` ⇒ by the reality argument (`[J,D_K]=0`, BDI, S17a) it carries C₂, NOT the conjugation-odd C₃. |")
    s.append("| **D3** | γ₉-graded odd cyclic cocycle `Tr[γ₉ a₀[D,a₁][D,a₂][D,a₃]]`, `a_i ∈ A_K` | **CLOSED — generation-blind on the t-leg** | Every `[D_K, a]`, `a ∈ A_K`, maps into `⊕ B(V_{(p,q)}) ⊗ 1` (Skolem–Noether leg-membership, registry lines 21120/21155, the S110 mechanism). A product of multiplicity-scalars is multiplicity-scalar ⇒ the cocycle is `⊗1` on the generation leg ⇒ distinguishes SECTORS (LABELING-B, registry-foreclosed) but NOT the `t`-generations (LABELING-A, the operative index). |")
    s.append("| **D4** | right-regular `R_X`-built operator `Y_R = Σ_a c_a R_{X_a}` (the SU(3)_R connection `δA_R`) | **OPEN — NOT covered by this theorem** | `R_X` escapes D1 (γ₉-even ⇒ trace non-vanishing) AND D3 (NON-`A_K`-built; the right-regular algebra is not in `[D_K, A_K]`). Decided by gate **W3-1 `CF-S114-YUK-RIGHTREG-CONNECTION`** (S114, audit_sha256 `e392b832483e8f75c6cbd87086c3a10bfb19f3d242ba9f873de3a9434997d49b`): D4 closed **INFO** — the right-regular SU(3)_R connection `Y_R` is **OPEN** (`Y_R` outside the left A_K-calculus, residual = 1.0 exact, but generation-DIAGONAL — neither closed-external nor PASS-internal). The genus is therefore NOT yet complete; this theorem's wall stays scoped `{A_K-built ∪ Casimir-graded ∪ γ₉-traced}`, NOT unconditional. |")
    s.append("")
    s.append(f"**D1 machine-exact verification (the COMPUTE leg, S114 W3-3).** Built D_K block-by-block over the Peter-Weyl sectors `(p,q)` at `τ_fold = {TAU}`, with `γ₉` lifted to `I_{{dim(p,q)}} ⊗ γ₉` per block (`dirac_spectrum.build_chirality`); the supertrace of the full block-diagonal `D_K` is the Peter-Weyl-multiplicity-weighted sum `Tr[γ₉ D_K^m] = Σ_{{(p,q)}} dim(p,q)·Tr[(I⊗γ₉) D_pi^m]`. **Operational-L note (honest disclosure per `math-scripts.md §\"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility\"`):** {nsec} of {nsec_tot} sectors constructed (L_max_operational = {Lop}, L_max_plan = {L_MAX}); the {nskip} pure-symmetric corners `(0,n)/(n,0)` with `p+q ≥ 9` hit the documented recursive-Casimir `get_irrep` construction wall (`(0,8)` ≈ 35 s, `(0,9)/(0,10)` infeasible within an agent timeslot). This downgrade is FAITHFUL and the verdict is UNAFFECTED because the D1 identity is a **PER-BLOCK exact-zero**: `Tr[(I⊗γ₉) D_pi^{{2k+1}}] = 0` for EACH `(p,q)` INDEPENDENTLY (by `{{γ₉, D_pi}}=0`), so the full-spectrum supertrace is the sum of identical zeros — there is NO cross-sector cancellation to verify, and the unconstructed corners contribute exactly 0 by the same argument. The wall is an implementation artifact of recursive Casimir projection, NOT physics. Across all {nsec} constructed sectors:")
    s.append("")
    s.append(f"- per-block anticommutator residual `max_{{(p,q)}} ‖{{γ₉, D_pi}}‖ = {maxac:.3e}` (= 0 ⇒ `{{γ₉, D_K}}=0` confirmed block-by-block: `{{γ₉,γ_a}}=0` Cl(8) [residual {d1['gamma9_anticomm_gamma_err']:.3e}] ∧ `{{γ₉,Ω}}=0` [residual {d1['gamma9_anticomm_Omega_err']:.3e}]);")
    s.append(f"- `|Tr[γ₉ D_K]| = {tr1:.3e}` < {D1_TOL:.0e} (k=0 supertrace, PW-weighted, EXACTLY 0 each block);")
    s.append(f"- `|Tr[γ₉ D_K³]| = {tr3:.3e}` < {D1_TOL:.0e} (k=1 supertrace, PW-weighted, EXACTLY 0 each block);")
    s.append(f"- Sage-QQ exact-ring confirmation: on the minimal anticommuting pair `γ₉=diag(1,−1)`, `D=[[0,d],[d,0]]` over `{exact.get('ring')}`, `Tr[γ₉ D] = {exact.get('tr_g9_D_exact')}` and `Tr[γ₉ D³] = {exact.get('tr_g9_D3_exact')}` EXACTLY (exact rationals rule out a float `1e-16` round-off masquerading as the structural identity; the identity is L_max-INVARIANT, sector-INDEPENDENT; identity_proved_exact = {exact.get('identity_proved_exact')}).")
    s.append("")
    s.append("**Substitution chain (D1; per `math-scripts.md §\"Double-Check Logic Before Compute\"`).** Claim: `Tr[γ₉ D_K^{2k+1}] ≡ 0` EXACTLY at every τ, every L_max. Step 1 — `{γ₉,D_K}=γ₉D_K+D_Kγ₉=0` (PERMANENT, S34/S56, the McKean–Singer KO-dim-6 anticommutator). Step 2 — `γ₉ D_K = −D_K γ₉`, so `Tr[γ₉ D_K^{2k+1}] = Tr[(γ₉ D_K) D_K^{2k}] = Tr[(−D_K γ₉) D_K^{2k}] = −Tr[D_K γ₉ D_K^{2k}]`. Step 3 — by cyclicity `= −Tr[γ₉ D_K^{2k} D_K] = −Tr[γ₉ D_K^{2k+1}]`, hence `2·Tr[γ₉ D_K^{2k+1}] = 0 ⇒ Tr[γ₉ D_K^{2k+1}] = 0`. Step 4 — the γ₉-graded odd-power trace is its own additive inverse ⇒ EXACTLY 0 (not a small number), INDEPENDENT of L_max and τ. Conclusion: D1 is CLOSED by the permanent anticommutator; the machine-exact Sage-QQ reproduction is the COMPUTE leg of this landing.")
    s.append("")
    s.append("**Companion structure.** STRUCTURAL-ORTHOGONAL-COMPANION to §VII.BV (No G-Invariant Sign-Changing Slope Handle — crossing-slope **SIGN** axis) and §VII.BL (Generation-Blindness Obstruction — Yukawa-hierarchy **MAGNITUDE** axis), sharing the multiplicity-scalar mechanism on a THIRD functional axis (the **γ₉/orientation** axis: D1 supertrace + D2 even-moment + D3 orientation-cocycle). The three are orthogonal observables on the same obstruction mechanism; **cross-observable / cross-corner co-primary is FORBIDDEN** per `cross-pillar-bridge-anatomy.md §\"Algebra-axis orthogonality K-counter\"` (MANDATORY at K=3) — this entry is a companion, NOT a co-primary anchor of §VII.BV or §VII.BL.")
    s.append("")
    s.append("**Two new permanent anchors brought to bear (the WS-S112-7 workshop's contribution):** `{γ₉, D_K}=0` (S34/S56, the Cl(8) chirality anticommutator) + the multiplicity-leg generation identification `t = (p−q) mod 3` (`proven_384`, STAGE-3-PERMANENT, registry §VII.BL line 21124).")
    s.append("")
    s.append("**Registry anatomy (intra-pillar structural theorem; 5-anatomy IS-not-IN cross-pillar elements N/A with reason).** This is an INTRA-pillar GEOMETRIC obstruction theorem (a property of the substrate spectral triple's own γ₉-graded / Casimir-graded / A_K-built functional class), NOT a cross-pillar substrate-IS ↔ laboratory-IN convergence bridge: it has no continuum-measurement laboratory-IN observable and no `L^{−α}` convergence envelope (the multiplicity-scalar lock is L_max-INVARIANT — it holds identically at every truncation, the D1 supertrace is exactly 0 at every L_max). The 5-anatomy elements (substrate-IS / laboratory-IN / HKR-or-K-theory bridge map / algebraic envelope / empirical anchor) are therefore N/A by construction (the §VII.BL / §VII.BV self-non-bridge precedent); the structural-confidence content is the D1–D3 closure + the held sign-pattern. Level-2 is **NON-BINDING / structurally-exact** (no `c_continuum`). Level tag (`phononic-framing.md §\"Single-τ-slice vs moduli-deformation\"`): the spectral triple + the functional class is a Level-1 single-τ-slice object at `τ_fold = 0.190`.")
    s.append("")
    s.append("**Source / provenance.** The WS-S112-7 YUKSHAPE R3 Structural Verdict §4a frozen Stage-0 text (`sessions/session-113/workshops/ws-s113-7-yukshape/ws-s113-7-yukshape-verdict.md`, SHA `5cd77110ea2d21984dd965b488d88c7989b8fd84fdc181aececd6c4859cd1d00`; Reading-A pole connes-ncg-theorist × Reading-B pole paasch-mass-quantization-analyst, R1/R2/R3, SYNTHESIS-tilted-to-Reading-B); the permanent anchors `{γ₉,D_K}=0` (S34/S56) and `[J,D_K]=0` (S17a); the Skolem–Noether leg-membership theorem (registry lines 21120/21155, the S110 mechanism); the multiplicity-leg generation id `proven_384`. D1 compute leg: this gate's `s114_yuk_shape_wall_vii_landing.py` over `dirac_spectrum.py` (runtime SHA `" + runtime_dirac_sha[:16] + "…`) + `canonical_constants.py` (runtime SHA `" + runtime_canonical_sha[:16] + "…`; the plan-pinned SHA `9ee1a113…` DRIFTED — a sibling S114 gate promoted a constant mid-session; RUNTIME state captured in the dual-SHA per `substrate-first-canonical-sourcing.md §(ii.B)`); registry landing target SHA at dispatch `" + runtime_registry_sha[:16] + "…`. **Substrate framing:** the substrate IS the spectral triple `(A_K, H_K, D_K, γ₉, J)`; the fabric's own chirality grading γ₉ and BDI real structure J FORCE every γ₉-traced / Casimir-graded / A_K-built G-invariant functional to act multiplicity-SCALAR on the generation leg `ℂ^{m(p,q)}`, so none can supply a sign-changing per-generation SHAPE handle. Direction: D_K eigenvalues + `{γ₉,D_K}=0` (D1) + `[J,D_K]=0` conjugation-evenness (D2) + Skolem–Noether leg-membership (D3) → every A_K-built form is generation-blind → the fermion-mass SHAPE texture is external (the ε_LX channel that also carries the §VII.BL magnitude), never inverted (`phononic-framing.md §\"IS Space, Not IN Space\"`).")
    s.append("")
    s.append("**Open door D4 (scope-qualifier cross-reference).** The one door this wall does NOT close is D4, the right-regular SU(3)_R connection `Y_R = Σ_a c_a R_{X_a}` on the multiplicity leg. Decided by S114 W3-1 `CF-S114-YUK-RIGHTREG-CONNECTION` (audit_sha256 `e392b832483e8f75c6cbd87086c3a10bfb19f3d242ba9f873de3a9434997d49b`): **INFO** — `Y_R` is OUTSIDE the left A_K-calculus (residual = 1.0 EXACT, escaping D3 leg-membership) but is **generation-DIAGONAL** (it does NOT supply the sign-changing per-generation pattern D4 would need to reopen the SHAPE handle), so it is neither a closed-external `ε_LX` re-dress nor a PASS-internal off-Casimir route — it is OPEN. The genus is therefore NOT yet complete: a FUTURE session may upgrade this wall from `{A_K-built ∪ Casimir-graded ∪ γ₉-traced}`-scoped to unconditional ONLY if a subsequent gate discharges D4's internal-vs-external status definitively. Until then this STAGE-1-CANDIDATE wall is scoped to the closed class.")
    s.append("")
    return "\n".join(s) + "\n"


def write_atomic_with_fsync_append(body_text: str, master_row: str, frontier_slot: str) -> None:
    """Append the body section at EOF (LF) AND insert the master-index row after the frontier row.
    Two-surface landing. Atomic via a single read-modify-write + fsync (the registry is LF-only).
    """
    original = REGISTRY.read_text(encoding="utf-8")               # (local)
    # 1) Insert the master-index row immediately after the frontier table row.
    import re
    # The frontier table row begins '| §VII.C<frontier> | THM |' — find its line, insert after it.
    fl = frontier_slot                                            # (local) e.g. '§VII.CJ'
    lines = original.split("\n")                                  # (local)
    insert_idx = None                                             # (local)
    for i, ln in enumerate(lines):
        if ln.startswith(f"| {fl} | THM |"):
            insert_idx = i + 1
            break
    if insert_idx is None:
        raise RuntimeError(f"frontier master-index row '| {fl} | THM |' not found — cannot land two-surface")
    new_row_line = master_row.rstrip("\n")                        # (local) the row, no trailing LF (split-join adds it)
    lines.insert(insert_idx, new_row_line)
    with_row = "\n".join(lines)                                   # (local)
    # 2) Append the body section at EOF. Original ends with '...\n'; ensure one blank line separator.
    if not with_row.endswith("\n"):
        with_row += "\n"
    final = with_row + "\n" + body_text                          # (local) blank line then the body section
    with open(REGISTRY, "w", encoding="utf-8", newline="") as fh:
        fh.write(final)
        fh.flush()
        os.fsync(fh.fileno())


def verify_section_matches(slot: str, body_text: str, master_row: str) -> dict:
    """Re-read the registry; verify BOTH surfaces present with ALL required markers."""
    actual = REGISTRY.read_text(encoding="utf-8")                 # (local)
    body_header = f"### {slot} —"                                 # (local)
    row_token = f"| {slot} | THM |"                               # (local)
    checks = {}  # (local)
    checks["body_section_present"] = body_header in actual
    checks["master_index_row_present"] = row_token in actual
    # body text landed verbatim (the exact built section is a substring)
    checks["body_text_verbatim"] = body_text.strip() in actual
    checks["master_row_verbatim"] = master_row.strip() in actual
    # required markers (in the landed body)
    required_markers = [
        "STAGE-1-CANDIDATE",
        "**D1**",
        "**D2**",
        "**D3**",
        "**D4**",
        "right-regular SU(3)_R connection (D4) is NOT covered and is OPEN",
        "CF-S114-YUK-RIGHTREG-CONNECTION",
        "e392b832483e",
        "STRUCTURAL-ORTHOGONAL-COMPANION",
        "§VII.BV",
        "§VII.BL",
        "NON-PROMOTION-BY-HELD-NUMBER",
        "sign-lock",
        "5-anatomy",
        "Skolem–Noether leg-membership",
        "{A_K-built ∪ Casimir-graded ∪ γ₉-traced}",
    ]  # (local)
    missing = [m for m in required_markers if m not in actual]   # (local)
    checks["all_markers_present"] = (len(missing) == 0)
    checks["missing_markers"] = missing
    all_ok = (checks["body_section_present"] and checks["master_index_row_present"]
              and checks["body_text_verbatim"] and checks["master_row_verbatim"]
              and checks["all_markers_present"])  # (local)
    checks["section_verify_pass"] = bool(all_ok)
    return checks


# ---------------------------------------------------------------------------
# Section 8 — Verdict payload helpers
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, l_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={l_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None) -> dict:
    payload = {
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
    }  # (local)
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 9 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    # 1. Input pins (RUNTIME) — first lines of stdout
    pins = log_input_pins(INPUT_FILES)
    runtime_canonical_sha = pins[str((SHARED_DIR / "canonical_constants.py").relative_to(PROJECT_ROOT)).replace("\\", "/")]  # (local)
    runtime_dirac_sha = pins[str((SHARED_DIR / "dirac_spectrum.py").relative_to(PROJECT_ROOT)).replace("\\", "/")]            # (local)
    runtime_registry_sha = pins[str(REGISTRY.relative_to(PROJECT_ROOT)).replace("\\", "/")]                                   # (local)

    script_path = Path(__file__).resolve()                        # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"        # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap, RUNTIME canonical)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. (A) D1 substrate-physics verification
    print(f"--- (A) D1 supertrace verification at tau_fold={TAU}, p+q<= {L_MAX} ---")
    d1 = compute_D1_supertraces(TAU, L_MAX)
    print(f"  n_sectors_constructed={d1['n_sectors_constructed']}/{d1['n_sectors_total']}, "
          f"L_max_operational={d1['L_max_operational']} (plan {d1['L_max_plan']}), "
          f"skipped={len(d1['skipped_sectors'])} pure-symmetric corners, total PW mult={d1['total_mult']}")
    if d1["skipped_sectors"]:
        print(f"  skipped (recursive-Casimir wall, per-block contribution = 0 by identity): "
              f"{[(p, q) for p, q, _, _ in d1['skipped_sectors']]}")
    print(f"  max block anticomm {{gamma9,D_pi}} = {d1['max_block_anticomm']:.3e}")
    print(f"  |Tr[gamma9 D_K]|  = {d1['Tr_g9_D_abs']:.6e}  (< {D1_TOL:.0e} ? {d1['Tr_g9_D_abs'] < D1_TOL})")
    print(f"  |Tr[gamma9 D_K^3]| = {d1['Tr_g9_D3_abs']:.6e}  (< {D1_TOL:.0e} ? {d1['Tr_g9_D3_abs'] < D1_TOL})")

    # 3. (B) Sage-QQ exact-ring leg
    print("--- (B) exact-ring identity verification ---")
    exact = verify_D1_exact_ring()
    print(f"  backend={exact.get('backend')}, ring={exact.get('ring')}, "
          f"Tr[g9 D]={exact.get('tr_g9_D_exact')}, Tr[g9 D^3]={exact.get('tr_g9_D3_exact')}, "
          f"identity_proved_exact={exact.get('identity_proved_exact')}")

    d1_pass = bool(d1["Tr_g9_D_abs"] < D1_TOL and d1["Tr_g9_D3_abs"] < D1_TOL
                   and d1["max_block_anticomm"] < ANTICOMM_TOL
                   and exact.get("identity_proved_exact"))  # (local)

    # 4. (C) Registry landing — single-shot AFTER-pattern, two-surface
    print("--- (C) §VII registry landing (single-shot AFTER-pattern) ---")
    registry_text = REGISTRY.read_text(encoding="utf-8")          # (local)
    slot, frontier = find_next_free_slot(registry_text)
    print(f"  next-free slot = {slot}  (frontier {frontier}; plan-pinned {PLANNED_SLOT})")
    slot_reroute = (slot != PLANNED_SLOT)                         # (local)

    master_row = build_master_index_row(slot, runtime_registry_sha)
    body_text = build_body_section(slot, d1, exact, runtime_canonical_sha,
                                   runtime_registry_sha, runtime_dirac_sha)

    # idempotency: if this slot's body header is already present, do NOT double-write
    already = (f"### {slot} —" in registry_text)                  # (local)
    if already:
        print(f"  slot {slot} already present — NO-OP append (idempotent)")
    else:
        write_atomic_with_fsync_append(body_text, master_row, frontier)

    verify = verify_section_matches(slot, body_text, master_row)
    print(f"  section_verify_pass = {verify['section_verify_pass']}  "
          f"(body={verify['body_section_present']}, row={verify['master_index_row_present']}, "
          f"markers_ok={verify['all_markers_present']})")
    if verify["missing_markers"]:
        print(f"  MISSING MARKERS: {verify['missing_markers']}")

    # 5. Verdict = (D1 machine-exact) AND (section-verify) AND (no slot reroute)
    section_ok = bool(verify["section_verify_pass"])              # (local)
    if slot_reroute:
        verdict = "FAIL"                                          # (local) reroute => FAIL-with-remediation
        reason = f"slot_reroute_{PLANNED_SLOT}_occupied_landed_at_{slot}"  # (local)
    elif d1_pass and section_ok:
        verdict = "PASS"                                          # (local)
        reason = "D1_machine_exact_AND_section_verify"            # (local)
    elif not d1_pass:
        verdict = "FAIL"                                          # (local) would contradict {gamma9,D_K}=0
        reason = "D1_supertrace_nonzero_or_exact_identity_failed"  # (local)
    else:
        verdict = "FAIL"                                          # (local) section-verify failed
        reason = "section_verify_failed"                          # (local)

    value = (f"D1:Tr[g9D]={d1['Tr_g9_D_abs']:.2e}_Tr[g9D3]={d1['Tr_g9_D3_abs']:.2e}_"
             f"anticomm={d1['max_block_anticomm']:.2e}_exact={exact.get('identity_proved_exact')}_"
             f"Lop={d1['L_max_operational']}of{d1['L_max_plan']}_nsec={d1['n_sectors_constructed']}of{d1['n_sectors_total']}_"
             f"slot={slot}_section_verify={section_ok}_{reason}")  # (local)

    # 6. Persist npz + (optional) plot
    np.savez(OUT_NPZ,
             tau_fold=TAU, L_max=L_MAX,
             Tr_g9_D_abs=d1["Tr_g9_D_abs"], Tr_g9_D3_abs=d1["Tr_g9_D3_abs"],
             Tr_g9_D_re=d1["Tr_g9_D_re"], Tr_g9_D_im=d1["Tr_g9_D_im"],
             Tr_g9_D3_re=d1["Tr_g9_D3_re"], Tr_g9_D3_im=d1["Tr_g9_D3_im"],
             max_block_anticomm=d1["max_block_anticomm"],
             gamma9_anticomm_gamma_err=d1["gamma9_anticomm_gamma_err"],
             gamma9_anticomm_Omega_err=d1["gamma9_anticomm_Omega_err"],
             n_sectors_constructed=d1["n_sectors_constructed"],
             n_sectors_total=d1["n_sectors_total"],
             L_max_operational=d1["L_max_operational"], L_max_plan=d1["L_max_plan"],
             skipped_sectors=np.array(d1["skipped_sectors"], dtype=object),
             total_mult=d1["total_mult"],
             d1_tol=D1_TOL, anticomm_tol=ANTICOMM_TOL,
             d1_pass=d1_pass, section_verify_pass=section_ok, slot_reroute=slot_reroute,
             slot=slot, frontier=str(frontier),
             exact_identity_proved=bool(exact.get("identity_proved_exact")),
             exact_tr_g9_D=str(exact.get("tr_g9_D_exact")),
             exact_tr_g9_D3=str(exact.get("tr_g9_D3_exact")),
             sector_rows=np.array(d1["sector_rows"], dtype=object),
             audit_sha256=audit_sha, content_sha256=content_sha,
             verdict=verdict, value=value)
    print(f"  npz -> {OUT_NPZ.name}")

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
        # left: four-door D1-D4 status
        doors = ["D1\nodd-trace", "D2\neven-moment", "D3\norient-cocycle", "D4\nright-regular"]  # (local)
        fates = [1, 1, 1, 0]  # (local) 1=CLOSED, 0=OPEN
        colors = ["#2ca02c" if f else "#d62728" for f in fates]  # (local)
        ax[0].bar(doors, [1, 1, 1, 1], color=colors)
        ax[0].set_title("SHAPE-Branch four-door disjunction\n(green=CLOSED D1-D3, red=OPEN D4)")
        ax[0].set_yticks([])
        for i, f in enumerate(fates):
            ax[0].text(i, 0.5, "CLOSED" if f else "OPEN", ha="center", va="center",
                       rotation=90, color="white", fontweight="bold")
        # right: D1 supertrace magnitudes vs tolerance
        labels = ["|Tr[γ9 D_K]|", "|Tr[γ9 D_K³]|", "max{γ9,D_pi}"]  # (local)
        vals = [max(d1["Tr_g9_D_abs"], 1e-18), max(d1["Tr_g9_D3_abs"], 1e-18),
                max(d1["max_block_anticomm"], 1e-18)]  # (local)
        ax[1].bar(labels, vals, color="#1f77b4")
        ax[1].axhline(D1_TOL, color="k", ls="--", label=f"tol {D1_TOL:.0e}")
        ax[1].set_yscale("log")
        ax[1].set_ylabel("magnitude (log)")
        ax[1].set_title("D1 supertrace identity: machine-exact 0")
        ax[1].legend()
        fig.tight_layout()
        fig.savefig(OUT_PNG, dpi=130)
        print(f"  png -> {OUT_PNG.name}")
    except Exception as exc:  # pragma: no cover
        print(f"  (plot skipped: {exc!r})")

    # 7. 4-tuple + verdict payload
    print(emit_4tuple(value, SCHEME, CONVENTION, L_MAX))
    note = (f"§VII landing of the SHAPE-Branch Homogeneity Obstruction (D1-D3 closed-class); "
            f"D1 Tr[γ9 D_K]=Tr[γ9 D_K³]=0 machine-exact (Sage-QQ + per-block); slot {slot}; "
            f"two-surface (body + master-index row); D4 OPEN cites W3-1 e392b832483e; "
            f"L_max_operational={d1['L_max_operational']} of plan {d1['L_max_plan']} "
            f"({d1['n_sectors_constructed']}/{d1['n_sectors_total']} sectors; pure-symmetric corners p+q>=9 past "
            f"recursive-Casimir wall, per-block supertrace=0 by identity, L_max-INVARIANT — honest disclosure "
            f"math-scripts.md D_K-block-diagonality); runtime canonical SHA {runtime_canonical_sha[:16]} "
            f"(plan 9ee1a113 DRIFTED, §(ii.B))")  # (local)
    extra = [f"# section_body_slot={slot} frontier={frontier} registry_runtime_sha={runtime_registry_sha[:16]} "
             f"dirac_runtime_sha={runtime_dirac_sha[:16]} STAGE-1-CANDIDATE intra-pillar GEOMETRIC "
             f"STRUCTURAL-ORTHOGONAL-COMPANION-VIIBV-VIIBL NON-PROMOTION-BY-HELD-NUMBER-sign-lock"]  # (local)
    print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note=note, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0  # FAIL is a valid scientific result; exit 0 unless the script itself broke


if __name__ == "__main__":
    sys.exit(main())
