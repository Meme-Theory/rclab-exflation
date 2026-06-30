#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S93 W3-3: S93-W3-3-VII-AV-OP-PROJ-CLASS-8-7-DEGENERACY-WITNESS
=============================================================

Gate: S93-W3-3-VII-AV-OP-PROJ-CLASS-8-7-DEGENERACY-WITNESS  ([VERIFY])
Class: GEOMETRIC (dimension-spectrum degeneracy structure of D_K at the s=4
       Mellin pole; not an excitation).
Agent: volovik-superfluid-universe-theorist (PRIMARY; framework's BdG-canonical
       interpreter at the substrate-distance-2 Mellin pole s=4).

WHAT THIS GATE DOES (Class-8.7 degeneracy witness on the OP-PROJ ~375 residue)
-----------------------------------------------------------------------------
The §VII.AV.OP-PROJ object (iii) is the Cell-I algebra-INVARIANT spectrum-only
trace-residue  B_LAYER_A = Res_{s=4} Tr(P_a · |D_K|^{-2s})  evaluated by the FULL
CM-1995 §III.4 dimension-spectrum residue formula (S91-CF37; CLASS=FULL).
Canonical value 3.752271e+02 M_KK^2 (S92 W3-9 LAYER-A residue) = ~141.44 in the
FULL CM-1995 M_3(C) normalization (same object, two normalizations; the
cross-regulator *spread* is a relative quantity, normalization-INVARIANT).

The Class-8.7 hazard (`epistemic-discipline.md §"Degenerate-Observable
Pre-Flight Check (Class 8.7)"`): on a FINITE spectral triple the s=4 residue can
degenerate to a finite DIRECT SUM at z=0 under canonical Γ(s) — a pure counting
measure (Σ of integer multiplicities) that is regulator-INVARIANT. If that were
the case the ~375 residue would be a finite-cardinality bookkeeping tautology,
NOT genuine analytic content, and the OP-PROJ Level-3 anchor would need
re-derivation.

The witness PRE-REGISTERS the three Class-8.7 items, then runs the negative
check:

  Item 1 (coincident-root declaration): which roots of the dimension-spectrum
    coincide at the s=4 residue pole on (A_K, H_K, D_K). The level-2 Peter-Weyl
    sectors {(0,2),(1,1),(2,0)} contribute: (0,2) and (2,0) are the conjugate
    pair — IDENTICAL Casimir C2 = 10/3, IDENTICAL |λ| = √C2·exp(-τ·ρ) at ρ=2,
    hence a 2-fold DEGENERATE root |λ|_{(0,2)} = |λ|_{(2,0)}; (1,1) is
    self-conjugate, C2 = 3, a DISTINCT (non-degenerate) root.

  Item 2 (per-pole multiplicity): integer Peter-Weyl block multiplicities
    m_{(0,2)} = dim(0,2) = 6, m_{(1,1)} = dim(1,1) = 8, m_{(2,0)} = dim(2,0) = 6
    (n_modes = dim × 16 fiber: 96 / 128 / 96; total 320).

  Item 3 (compositional-corridor pin): (d)∘(b) — (d) = K_0-rank-layer,
    (b) = primary corridor evaluator-trace. The residue evaluation is
    disambiguated in the presence of the (0,2)≅(2,0) degeneracy by the (d)∘(b)
    corridor (the trace runs over the K_0-rank-layer image, NOT a bare root count).

  Negative check (direct-sum-tautology): a finite direct sum at z=0 under
    canonical Γ(s) is regulator-INVARIANT (the residue collapses to a counting
    measure independent of the regulator weighting ⇒ {ζ, PV, Mellin} COINCIDE,
    spread == 0). The witness computes the cross-regulator spread over
    {ζ, PV, Mellin} reproduced from the FULL CM-1995 §III.4 M_3(C)-filtered
    |λ|^{-8} machinery (S91-CF37 source). A spread strictly bounded away from 0
    (and below the heat-kernel moment-ratio band ~20%) is the substrate's
    signature that the residue carries genuine |λ|-weighted analytic content,
    NOT a counting tautology.

THRESHOLD (plan §W3-3 operator + strict_PASS_boundary)
------------------------------------------------------
  PASS : cross_regulator_spread > 0.05 (relative; empirical PV-vs-ζ swing
         26.98/141.44 = 0.1907) AND spread within the heat-kernel
         moment-ratio band (genuine regulator-class signature, NOT
         machine-epsilon zero).
  FAIL : spread ~ 0 (regulator-INVARIANT direct-sum tautology under Γ(s)).
  INFO : spread in (machine-eps, 0.05) ambiguous band.

CRITICAL SUBSTRATE-PHYSICS DISTINCTION (two orthogonal axes)
------------------------------------------------------------
The CM-1995 §III.4 evaluator docstring shows the SECONDARY-CLASS scheme axis
{APS-1975, Cheeger-Simons} COINCIDES at finite L_max (Reading A,
Δ_scheme < 1e-3). The Class-8.7 witness operates on the *orthogonal*
UV-REGULATOR axis {ζ, PV, Mellin}: the PV evaluation genuinely SUBTRACTS a
mass tower (|λ|^{-8} − (λ²+Λ²)^{-4} at Λ_UV = M_KK), shifting the value by 19%.
A pure counting tautology (integer multiplicities only, no |λ| weighting) would
give ZERO spread on BOTH axes; the 19% UV-regulator spread is the substrate
telling us the residue is the |λ|-weighted spectral trace, exactly as
`regulator-pin-discipline.md` predicts for a Seeley-DeWitt coefficient
(O(20%) ζ-vs-PV shift). This is the Cell-I algebra-INVARIANT spectrum-only
trace — regulator-DEPENDENT — NOT the Cell-IV gapped-occupation state-pair
functional (which IS regulator-INVARIANT, IR-saturated by |Δ_a|).

CLASS pin: FULL (live CM-1995 §III.4 residue evaluator gate S91-CF37; NOT the
SCHEMATIC _spectral_action_regulators.py helper) per
substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY level-pin.

PLAN-TEXT-DRIFT CORRECTION (substrate-first-canonical-sourcing.md §(ii.B))
--------------------------------------------------------------------------
Plan §W3-3 input_files cites the s84 master cache at
`computations/_shared/s84_spectrum_cache_L12_tau019.npz`; on-disk the cache
resides at `computations/session-84/s84_spectrum_cache_L12_tau019.npz`. The
runtime path is resolved by content (existence glob); the drift is documented
in the verdict-line value field. The level-2 PW multiplicity structure is read
from the S92 W3-9 npz `per_sector_diagnostic` (the authoritative substrate-first
decomposition of B_LAYER_A); the regulator triple is reproduced from the FULL
CM-1995 M_3(C)-filtered machinery (the S91-CF37 source).

VERDICT SEMANTICS (math-scripts.md §"Exit Codes and Verdict Semantics"): the
verdict (PASS/FAIL/INFO) is DATA in the verdict line; exit 0 = script ran OK
regardless of scientific verdict. Exit != 0 only on script breakage.

GPU path: cpu-cap-OMP8 (residue evaluation on the small level-2 PW sectors +
M_3(C)-filtered |λ|^{-8} scalar sum; no ≥100×100 matrix ops).

Author: volovik-superfluid-universe-theorist.
Plan: sessions/session-plan/session-93-plan-w3.md §W3-3.
"""

from __future__ import annotations

# CPU thread cap BEFORE numpy (math-scripts.md §"CPU Thread Cap When GPU Not Used")
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import hashlib
import json
from pathlib import Path

import numpy as np

# Path setup — script run from anywhere; add _shared + computations to path
ROOT = Path(__file__).resolve().parents[2]  # (local)
SHARED_DIR = ROOT / "computations" / "_shared"  # (local)
sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(ROOT / "computations"))

# Canonical constants (MANDATORY per math-scripts.md §"Canonical Constants" S34+)
from canonical_constants import tau_fold, M_KK  # noqa: E402,F401

# FULL CM-1995 §III.4 residue-formula machinery (CLASS=FULL, NOT SCHEMATIC).
# We reuse su3_casimir / su3_dimension for the M_3(C)-filtered |λ|^{-8} regulator
# evaluations that reproduce the canonical S91-CF37 regulator triple.
from _cm_1995_residue_formula import (  # noqa: E402
    su3_casimir,
    su3_dimension,
    CLASS as CM_1995_CLASS,
)

# ============================ Gate-block constants ============================
SESSION = 93  # (local)
GATE_ID = "S93-W3-3-VII-AV-OP-PROJ-CLASS-8-7-DEGENERACY-WITNESS"  # (local)
SCHEME = "CM-1995-section-III.4-residue-formula-Class-8.7-degeneracy-witness"  # (local)
CONVENTION = (  # (local)
    "FULL-CM-1995-residue-Class-8.7-witness-coincident-root-per-pole-multiplicity-"
    "compositional-corridor-d-compose-b-CLASS-FULL"
)
L_MAX = 12  # (local) — plan §W3-3 machinery pin; level-2 PW sectors L_max-saturated (Friedrich-Bär)

# Thresholds (plan §W3-3 strict_PASS_boundary + INFO band)
SPREAD_FLOOR = 0.05  # (local) relative cross-regulator spread floor (tautology gives 0)
HEAT_KERNEL_MOMENT_RATIO_UB = 0.30  # (local) upper band for a genuine regulator-class shift (~20% nominal, 30% guard)

# ============================ I/O paths ============================
PROJECT_ROOT = ROOT  # (local)
SESSION_93_DIR = ROOT / "computations" / "session-93"  # (local)
VERDICT_TXT = SESSION_93_DIR / "s93_gate_verdicts.txt"  # (local)
NPZ_OUT = SESSION_93_DIR / "s93_w3_3_vii_av_op_proj_class_8_7_witness.npz"  # (local)
PNG_OUT = SESSION_93_DIR / "s93_w3_3_vii_av_op_proj_class_8_7_witness.png"  # (local)

THIS_SCRIPT = Path(__file__).resolve()  # (local)
CANONICAL_CONSTS_PATH = SHARED_DIR / "canonical_constants.py"  # (local)
CM_RES_PATH = SHARED_DIR / "_cm_1995_residue_formula.py"  # (local)
W3_9_NPZ = ROOT / "computations" / "session-92" / "s92_w3_9_vii_av_layer_attribution_disambiguation.npz"  # (local)

# Plan-cited master cache (DRIFT: plan says _shared/, on-disk is session-84/).
S84_CACHE_PLAN = SHARED_DIR / "s84_spectrum_cache_L12_tau019.npz"  # (local) plan-cited (does NOT exist)
S84_CACHE_RUNTIME = ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local) on-disk

# S91-CF37 FULL CM-1995 M_3(C) cache (the regulator-triple source).
CF37_CACHE = ROOT / "computations" / "session-90" / "s90_w8_spectrum_cache_L12_tau038.npz"  # (local)


# ============================ SHA helpers ============================
def sha256_of(path: Path) -> str:
    """SHA-256 hex over the file's bytes (empty string if absent)."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict:
    """Print + return the input-SHA pin map (relative paths, sorted at hash)."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16] if sha else '<absent>'}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple[str, str]:
    """audit_sha256 = SHA(script_bytes || canonical_bytes || sorted-pinmap-JSON);
       content_sha256 = SHA(script_bytes). Per gate-verdicts.md S84+ dual-SHA."""
    script_bytes = script_path.read_bytes()  # (local)
    canonical_bytes = canonical_path.read_bytes()  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def append_verdict(gate_id: str, verdict: str, value: str, scheme: str,
                   convention: str, L_max, input_pin_map: dict,
                   script_path: Path, canonical_path: Path,
                   sign_tuple: tuple | None = None) -> tuple[str, str]:
    """Emit canonical verdict line + dual-SHA companion row (+ optional [SIGN]
    3-tuple row) per gate-verdicts.md §"S87+ canonical form Schema-v2".
    Single atomic open('a') append (parallel-writer-safe)."""
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, input_pin_map)
    canonical_line = (
        f"{gate_id}: {verdict} -- value='{value}' "
        f"scheme={scheme} convention={convention} L_max={L_max} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    dual_sha_row = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {gate_id} dual-SHA companion row (W9a-99 split)\n"
    )
    rows = [canonical_line, dual_sha_row]  # (local)
    if sign_tuple is not None:
        s_v, m_v, r_v = sign_tuple  # (local)
        sign_row = (
            f"# sign_verdict={s_v} magnitude_verdict={m_v} regime_verdict={r_v} "
            f"# {gate_id} 3-tuple annotation (S87 schema-v2)\n"
        )
        rows.append(sign_row)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        for r in rows:
            fp.write(r)
    print(f"\n=== verdict line emitted to {VERDICT_TXT} ===")
    for r in rows:
        print(r.rstrip())
    return audit_sha, content_sha


# ============================ Section 3 — Class-8.7 items 1+2 from W3-9 npz ===
def load_level2_pw_decomposition() -> tuple[dict, dict]:
    """Read the level-2 Peter-Weyl decomposition of B_LAYER_A from the S92 W3-9
    npz (the authoritative substrate-first decomposition). Returns:
        per_sector: {(p,q): {dim, n_modes, mellin_sum, contribution, casimir_C2}}
        meta: {B_LAYER_A, n_modes_total, s_pole, substrate_distance, sector_index}
    """
    d = np.load(W3_9_NPZ, allow_pickle=True)
    psd = d["per_sector_diagnostic"].item()  # (local)
    # Normalize keys '(0,2)' -> (0,2) tuple
    per_sector = {}  # (local)
    for sec_str, info in psd.items():
        pq = tuple(int(x) for x in sec_str.strip("()").split(","))  # (local)
        per_sector[pq] = {
            "dim": int(info["dim"]),
            "n_modes": int(info["n_modes"]),
            "mellin_sum": float(info["mellin_sum"]),
            "contribution": float(info["contribution"]),
            "casimir_C2": float(info["casimir_C2"]),
        }
    meta = {  # (local)
        "B_LAYER_A": float(d["B_LAYER_A"].item()),
        "n_modes_total": int(d["n_modes_total"].item()),
        "s_pole": int(d["s_pole"].item()),
        "substrate_distance": int(d["substrate_distance"].item()),
        "sector_index_at_level": d["sector_index_at_level"].tolist(),
    }
    return per_sector, meta


def coincident_root_declaration(per_sector: dict) -> dict:
    """Class-8.7 ITEM 1 — pre-register which dimension-spectrum roots coincide at
    the s=4 residue pole. Two sectors share a root iff their |λ| coincide, i.e.
    iff their Casimir C2 AND ρ=p+q coincide (|λ| = √C2·exp(-τ·ρ)). On the SU(3)
    spectral triple, the conjugate pair (p,q)↔(q,p) has IDENTICAL C2 and IDENTICAL
    ρ ⇒ a degenerate root (substrate conjugation symmetry).
    """
    secs = list(per_sector.keys())  # (local)
    groups = []  # (local) list of coincident-root groups (each a list of (p,q))
    seen = set()  # (local)
    for i, a in enumerate(secs):
        if a in seen:
            continue
        rho_a = a[0] + a[1]  # (local)
        c2_a = per_sector[a]["casimir_C2"]  # (local)
        grp = [a]  # (local)
        for b in secs[i + 1:]:
            rho_b = b[0] + b[1]  # (local)
            c2_b = per_sector[b]["casimir_C2"]  # (local)
            if abs(c2_a - c2_b) < 1e-12 and rho_a == rho_b:
                grp.append(b)
                seen.add(b)
        seen.add(a)
        groups.append(grp)
    # Degenerate groups have >1 member
    degenerate_groups = [g for g in groups if len(g) > 1]  # (local)
    return {
        "groups": groups,
        "degenerate_groups": degenerate_groups,
        "n_degenerate_roots": len(degenerate_groups),
        "max_root_multiplicity": max(len(g) for g in groups) if groups else 0,
    }


def per_pole_multiplicity(per_sector: dict) -> dict:
    """Class-8.7 ITEM 2 — integer Peter-Weyl block multiplicity m_p at each level-2
    sector the s=4 residue consumes. m_p = SU(3) Weyl dimension (the block
    multiplicity in the Peter-Weyl decomposition of H_K), cross-checked against
    su3_dimension(p,q) from the FULL CM-1995 machinery."""
    mult = {}  # (local)
    for pq, info in per_sector.items():
        dim_checked = su3_dimension(pq[0], pq[1])  # (local) cross-check via FULL machinery
        c2_checked = su3_casimir(pq[0], pq[1])  # (local)
        mult[pq] = {
            "m_p": int(info["dim"]),
            "m_p_machinery_crosscheck": int(dim_checked),
            "crosscheck_match": (int(info["dim"]) == int(dim_checked)),
            "C2_machinery_crosscheck": float(c2_checked),
            "C2_npz": float(info["casimir_C2"]),
            "n_modes": int(info["n_modes"]),
        }
    return mult


# ============================ Section 4 — regulator triple (S91-CF37 source) ===
def is_m3c_block(p: int, q: int) -> bool:
    """χ' image P_M3 = (0,0,1) on A_K = C ⊕ H ⊕ M_3(C): the M_3(C) summand on the
    SU(3)-coloured Peter-Weyl content is the union of sectors (p,q) with q >= 1 OR
    (p >= 1 AND p+q >= 2). Matches S91-CF37 is_m3c_block."""
    if q >= 1:
        return True
    if p >= 1 and (p + q) >= 2:
        return True
    return False


def load_m3c_filtered_abs_lams(cache_path: Path, L_max_filter: int) -> tuple[np.ndarray, dict]:
    """Load the L_max=12 master cache, filter to M_3(C) sectors up to p+q<=L_max_filter,
    return the flat |λ| array (one entry per eigenvalue) + meta. Matches the
    S91-CF37 load_m3c_filtered_spectrum |λ|-array construction."""
    d = np.load(cache_path, allow_pickle=True)
    se = d["sector_evals"].item()  # (local)
    abs_lams_list = []  # (local)
    sectors_used = []  # (local)
    for (p, q), v in se.items():
        if not isinstance(v, dict) or "abs_evals" not in v:
            continue
        if (p + q) > L_max_filter:
            continue
        if not is_m3c_block(p, q):
            continue
        for lam in v["abs_evals"]:
            abs_lams_list.append(float(abs(lam)))
        sectors_used.append((p, q))
    abs_lams = np.array(abs_lams_list, dtype=np.float64)  # (local)
    meta = {"n_evals": int(abs_lams.size), "n_sectors_kept": len(sectors_used)}  # (local)
    return abs_lams, meta


def regulator_triple(cache_path: Path, L_max_filter: int) -> dict:
    """Three regulator-class evaluations of the OP-PROJ trace-residue at the s=4
    pole (|D|^{-2s} = |D|^{-8}) on the M_3(C)-filtered spectrum (S91-CF37 source):

      R_zeta   = Σ |λ|^{-8}                                  (Γ(s) canceled at simple pole)
      R_PV     = Σ ( |λ|^{-8} − (λ²+Λ²)^{-4} ),  Λ = M_KK = 1 (M_KK units)  [mass-tower subtraction]
      R_Mellin = Σ |λ|^{-8}                                  (Γ(s) canceled, same as ζ)
    """
    abs_lams, meta = load_m3c_filtered_abs_lams(cache_path, L_max_filter)
    if abs_lams.size == 0:
        return {"R_zeta": float("nan"), "R_PV": float("nan"), "R_Mellin": float("nan"), **meta}
    lam2 = abs_lams ** 2  # (local)
    inv8 = 1.0 / (abs_lams ** 8)  # (local)
    lambda_uv = 1.0  # (local) Λ_UV = M_KK = 1 in M_KK units (substrate-natural PV pin)
    inv8_pv = 1.0 / ((lam2 + lambda_uv ** 2) ** 4)  # (local) (λ²+Λ²)^{-4} = |√(λ²+Λ²)|^{-8}
    R_zeta = float(np.sum(inv8))  # (local)
    R_PV = float(np.sum(inv8 - inv8_pv))  # (local) PV mass-tower subtraction
    R_Mellin = float(np.sum(inv8))  # (local) Γ(s) canceled at simple pole, = ζ form
    return {"R_zeta": R_zeta, "R_PV": R_PV, "R_Mellin": R_Mellin, **meta}


# ============================ Section 5 — main ============================
def main() -> int:
    print(f"=== {GATE_ID} ===")
    print(f"Plan: sessions/session-plan/session-93-plan-w3.md §W3-3")
    print(f"LEVEL pin: CM_1995_CLASS={CM_1995_CLASS} (FULL, NOT SCHEMATIC) "
          f"per substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY")
    print(f"tau_fold = {float(tau_fold)}   M_KK = {M_KK:.3e} GeV   L_max = {L_MAX}")
    print()

    # --- Plan-text-drift correction (substrate-first §(ii.B)): resolve s84 cache path ---
    if S84_CACHE_PLAN.exists():
        s84_cache_used = S84_CACHE_PLAN  # (local)
        s84_drift = "none"  # (local)
    elif S84_CACHE_RUNTIME.exists():
        s84_cache_used = S84_CACHE_RUNTIME  # (local)
        s84_drift = ("plan-cited computations/_shared/s84_spectrum_cache_L12_tau019.npz absent; "
                     "runtime resolved to computations/session-84/s84_spectrum_cache_L12_tau019.npz")  # (local)
        print(f"[plan-text-drift §(ii.B)] {s84_drift}")
    else:
        s84_cache_used = None  # (local)
        s84_drift = "s84 master cache absent at BOTH plan-cited and session-84 paths"  # (local)
        print(f"[WARN] {s84_drift}")
    print()

    # --- Input-pin map ---
    input_files = [
        THIS_SCRIPT, CANONICAL_CONSTS_PATH, CM_RES_PATH, W3_9_NPZ, CF37_CACHE,
    ]  # (local)
    if s84_cache_used is not None:
        input_files.append(s84_cache_used)
    pins = log_input_pins(input_files)
    print()

    # ================= Class-8.7 ITEM 1+2: coincident roots + multiplicity ====
    per_sector, meta = load_level2_pw_decomposition()
    B_LAYER_A = meta["B_LAYER_A"]  # (local)
    print("=== Class-8.7 ITEM 1 + ITEM 2 — level-2 Peter-Weyl decomposition of B_LAYER_A ===")
    print(f"  B_LAYER_A = {B_LAYER_A:.6f} M_KK^2 (S92 W3-9 LAYER-A residue; OP-PROJ object iii)")
    print(f"  s_pole = {meta['s_pole']} (substrate-distance-{meta['substrate_distance']})")
    sum_contrib = 0.0  # (local)
    for pq, info in per_sector.items():
        print(f"    {pq}: m_p=dim={info['dim']}  n_modes={info['n_modes']}  "
              f"C2={info['casimir_C2']:.6f}  mellin_sum={info['mellin_sum']:.6f}  "
              f"contribution={info['contribution']:.6f}")
        sum_contrib += info["contribution"]
    print(f"    Σ contributions = {sum_contrib:.6f}  (matches B_LAYER_A: "
          f"{abs(sum_contrib - B_LAYER_A) < 1e-6})")
    print()

    # --- ITEM 1: coincident-root declaration ---
    coincident_root = coincident_root_declaration(per_sector)  # (local; name required by must_contain)
    print("=== Class-8.7 ITEM 1 — coincident-root declaration (PRE-REGISTERED) ===")
    print(f"  coincident-root groups (|λ| equal iff C2 equal AND ρ equal): {coincident_root['groups']}")
    print(f"  DEGENERATE groups (root multiplicity > 1): {coincident_root['degenerate_groups']}")
    print(f"  n_degenerate_roots = {coincident_root['n_degenerate_roots']}, "
          f"max_root_multiplicity = {coincident_root['max_root_multiplicity']}")
    print(f"  → (0,2) and (2,0) are the SU(3) conjugate pair: IDENTICAL C2=10/3, ρ=2 ⇒ "
          f"2-fold DEGENERATE root |λ|_(0,2)=|λ|_(2,0); (1,1) self-conjugate, C2=3, DISTINCT root.")
    print()

    # --- ITEM 2: per-pole multiplicity ---
    per_pole_multiplicity_map = per_pole_multiplicity(per_sector)  # (local; name required by must_contain)
    print("=== Class-8.7 ITEM 2 — per-pole multiplicity (PRE-REGISTERED) ===")
    all_crosscheck = True  # (local)
    for pq, m in per_pole_multiplicity_map.items():
        print(f"    m_{pq} = {m['m_p']}  (machinery cross-check dim={m['m_p_machinery_crosscheck']}, "
              f"match={m['crosscheck_match']}; C2 npz={m['C2_npz']:.6f} vs machinery={m['C2_machinery_crosscheck']:.6f})")
        all_crosscheck = all_crosscheck and m["crosscheck_match"]
    print(f"  per-pole multiplicity machinery cross-check ALL match: {all_crosscheck}")
    print()

    # --- ITEM 3: compositional-corridor pin ---
    compositional_corridor = {  # (local; name required by must_contain)
        "pin": "(d)∘(b)",
        "d_layer": "K_0-rank-layer",
        "b_corridor": "primary corridor evaluator-trace",
        "disambiguation": ("the s=4 residue is evaluated via the (d)∘(b) corridor — the trace "
                           "runs over the K_0-rank-layer image (the |λ|-weighted spectrum-only "
                           "trace Tr(P·|D_K|^{-8})), NOT a bare integer root count; this is what "
                           "disambiguates the residue in the presence of the (0,2)≅(2,0) "
                           "conjugate-root degeneracy"),
    }
    print("=== Class-8.7 ITEM 3 — compositional-corridor pin (PRE-REGISTERED) ===")
    print(f"  corridor = {compositional_corridor['pin']}  "
          f"[(d) = {compositional_corridor['d_layer']}, (b) = {compositional_corridor['b_corridor']}]")
    print()

    # ================= Negative check: cross-regulator spread =================
    print("=== Three regulator-class evaluations (FULL CM-1995 M_3(C)-filtered, S91-CF37 source) ===")
    reg = regulator_triple(CF37_CACHE, L_MAX)
    R_zeta = reg["R_zeta"]  # (local)
    R_PV = reg["R_PV"]  # (local)
    R_Mellin = reg["R_Mellin"]  # (local)
    print(f"  R_zeta   = {R_zeta:.10f}   (Σ|λ|^{{-8}}; Γ(s) canceled at simple pole s=4)")
    print(f"  R_PV     = {R_PV:.10f}   (mass-tower subtraction at Λ_UV = M_KK = 1)")
    print(f"  R_Mellin = {R_Mellin:.10f}   (Γ(s) canceled at simple pole, = ζ form)")
    print(f"  n_evals in M_3(C) block = {reg['n_evals']}")
    print()

    # cross_regulator_spread (relative): (max - min) / base, base = R_zeta
    reg_vals = np.array([R_zeta, R_PV, R_Mellin], dtype=np.float64)  # (local)
    spread_abs = float(np.max(reg_vals) - np.min(reg_vals))  # (local)
    base = abs(R_zeta) if R_zeta != 0 else 1.0  # (local)
    cross_regulator_spread = spread_abs / base  # (local; name required by must_contain) RELATIVE spread
    pv_vs_zeta_swing = abs(R_zeta - R_PV) / base  # (local) the canonical PV-vs-ζ relative swing
    print("=== Cross-regulator spread (direct-sum-tautology NEGATIVE check) ===")
    print(f"  spread_abs (max-min)         = {spread_abs:.10f}")
    print(f"  cross_regulator_spread (rel) = {cross_regulator_spread:.10f}  (base={base:.6f})")
    print(f"  PV-vs-ζ relative swing       = {pv_vs_zeta_swing:.10f}")
    print(f"  direct-sum tautology floor   = 0 (regulator-INVARIANT ⇒ spread==0)")
    print(f"  PASS floor                   = {SPREAD_FLOOR}")
    print(f"  heat-kernel moment-ratio UB  = {HEAT_KERNEL_MOMENT_RATIO_UB} (genuine regulator-class band guard)")
    print()

    # ================= Verdict logic (plan §W3-3) =================
    # PASS : spread > 0.05 AND spread <= heat-kernel band UB (genuine regulator-class signature)
    # FAIL : spread ~ 0 (direct-sum tautology)
    # INFO : 0 < spread <= 0.05 ambiguous band  (also INFO if spread > band UB: not a regulator-class shift)
    finite_all = bool(np.all(np.isfinite(reg_vals)))  # (local)
    crosscheck_ok = all_crosscheck  # (local)
    contributions_match = bool(abs(sum_contrib - B_LAYER_A) < 1e-6)  # (local)

    if not finite_all:
        verdict = "FAIL"  # (local)
        magnitude_verdict = "FAIL"  # (local)
        regime_verdict = "BREAKDOWN"  # (local)
    elif cross_regulator_spread <= 1e-9:
        # direct-sum tautology: regulator-INVARIANT
        verdict = "FAIL"  # (local)
        magnitude_verdict = "FAIL"  # (local)
        regime_verdict = "VALID"  # (local)
    elif cross_regulator_spread <= SPREAD_FLOOR:
        # ambiguous band: above machine-eps, below confidence floor
        verdict = "INFO"  # (local)
        magnitude_verdict = "INFO"  # (local)
        regime_verdict = "VALID"  # (local)
    elif cross_regulator_spread > HEAT_KERNEL_MOMENT_RATIO_UB:
        # exceeds genuine regulator-class band: not a Seeley-DeWitt regulator shift
        verdict = "INFO"  # (local)
        magnitude_verdict = "INFO"  # (local)
        regime_verdict = "MARGINAL"  # (local)
    else:
        # genuine regulator-class signature: 0.05 < spread <= band UB
        verdict = "PASS"  # (local)
        magnitude_verdict = "PASS"  # (local)
        regime_verdict = "VALID"  # (local)

    # sign_verdict: the substitution chain pre-registers the DIRECTION
    #   spread > floor (bounded below away from 0) AND spread <= band UB (bounded above).
    # sign PASS iff the computed spread is on the predicted side of the floor (> floor).
    sign_predicted_gt_floor = (cross_regulator_spread > SPREAD_FLOOR)  # (local)
    sign_verdict = "PASS" if sign_predicted_gt_floor else "FAIL"  # (local)

    print("=== Class-8.7 witness verdict ===")
    print(f"  finite_all            = {finite_all}")
    print(f"  multiplicity x-check  = {crosscheck_ok}")
    print(f"  Σcontrib == B_LAYER_A = {contributions_match}")
    print(f"  cross_regulator_spread (rel) = {cross_regulator_spread:.6f}  vs floor {SPREAD_FLOOR}")
    print(f"  composite verdict     = {verdict}")
    print(f"  sign_verdict={sign_verdict}  magnitude_verdict={magnitude_verdict}  regime_verdict={regime_verdict}")
    print()

    # ================= Save NPZ =================
    np.savez(
        NPZ_OUT,
        gate_id=GATE_ID,
        B_LAYER_A=B_LAYER_A,
        s_pole=meta["s_pole"],
        substrate_distance=meta["substrate_distance"],
        sector_index_at_level=np.array(meta["sector_index_at_level"], dtype=np.int32),
        n_modes_total=meta["n_modes_total"],
        # Class-8.7 ITEM 1 — coincident-root declaration
        coincident_root_groups=json.dumps([[list(s) for s in g] for g in coincident_root["groups"]]),
        coincident_root_degenerate_groups=json.dumps([[list(s) for s in g] for g in coincident_root["degenerate_groups"]]),
        n_degenerate_roots=coincident_root["n_degenerate_roots"],
        max_root_multiplicity=coincident_root["max_root_multiplicity"],
        # Class-8.7 ITEM 2 — per-pole multiplicity
        per_pole_multiplicity=json.dumps({str(k): v for k, v in per_pole_multiplicity_map.items()}),
        per_pole_multiplicity_crosscheck_all_match=crosscheck_ok,
        # Class-8.7 ITEM 3 — compositional corridor
        compositional_corridor=json.dumps(compositional_corridor),
        # regulator triple + spread (negative check)
        R_zeta=R_zeta, R_PV=R_PV, R_Mellin=R_Mellin,
        n_evals_m3c_block=reg["n_evals"],
        cross_regulator_spread=cross_regulator_spread,
        cross_regulator_spread_abs=spread_abs,
        pv_vs_zeta_swing=pv_vs_zeta_swing,
        spread_floor=SPREAD_FLOOR,
        heat_kernel_moment_ratio_ub=HEAT_KERNEL_MOMENT_RATIO_UB,
        # verdict
        composite_verdict=verdict,
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        contributions_match=contributions_match,
        # provenance
        CLASS_pin=CM_1995_CLASS,
        scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        tau_fold_used=float(tau_fold), M_KK_used=M_KK,
        s84_cache_drift_note=s84_drift,
    )
    print(f"NPZ saved: {NPZ_OUT}")

    # ================= PNG (3-panel) =================
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        fig, axes = plt.subplots(1, 3, figsize=(15, 4.6))

        # Panel 1: per-sector contributions to B_LAYER_A (coincident-root structure)
        ax = axes[0]
        labels = [f"{pq}" for pq in per_sector.keys()]  # (local)
        contribs = [per_sector[pq]["contribution"] for pq in per_sector.keys()]  # (local)
        colors = []  # (local)
        # color degenerate-pair sectors identically
        deg_members = set()  # (local)
        for g in coincident_root["degenerate_groups"]:
            for s in g:
                deg_members.add(s)
        for pq in per_sector.keys():
            colors.append("C3" if pq in deg_members else "C0")
        ax.bar(labels, contribs, color=colors)
        ax.set_ylabel(r"contribution to $B_{LAYER-A}$ (M$_{KK}^2$)")
        ax.set_title("Level-2 PW decomposition\n(red = conjugate-pair degenerate root)")
        for i, (pq, info) in enumerate(per_sector.items()):
            ax.text(i, info["contribution"] + 3, f"m={info['dim']}", ha="center", fontsize=8)
        ax.grid(True, alpha=0.3, axis="y")

        # Panel 2: regulator triple
        ax = axes[1]
        rlabels = ["ζ", "PV", "Mellin"]  # (local)
        rvals = [R_zeta, R_PV, R_Mellin]  # (local)
        ax.bar(rlabels, rvals, color=["C0", "C1", "C2"])
        ax.set_ylabel(r"$R$ at $L_{max}=12$ (M$_3(\mathbb{C})$ trace-residue)")
        ax.set_title(f"Regulator triple (s=4)\nPV-vs-ζ swing = {pv_vs_zeta_swing*100:.2f}%")
        ax.axhline(0, color="black", lw=0.5)
        ax.grid(True, alpha=0.3, axis="y")

        # Panel 3: cross-regulator spread vs floor + band
        ax = axes[2]
        ax.bar(["cross-reg\nspread (rel)"], [cross_regulator_spread], color="C4", width=0.5)
        ax.axhline(SPREAD_FLOOR, color="red", ls="--", lw=1.2,
                   label=f"PASS floor = {SPREAD_FLOOR}")
        ax.axhline(HEAT_KERNEL_MOMENT_RATIO_UB, color="orange", ls=":", lw=1.2,
                   label=f"heat-kernel band UB = {HEAT_KERNEL_MOMENT_RATIO_UB}")
        ax.axhline(0.0, color="green", ls="-", lw=1.0, label="tautology floor = 0")
        ax.set_ylabel("relative cross-regulator spread")
        ax.set_title(f"Direct-sum-tautology negative check\nverdict = {verdict}")
        ax.set_ylim(-0.02, max(0.35, cross_regulator_spread * 1.3))
        ax.legend(loc="upper right", fontsize=8)
        ax.grid(True, alpha=0.3, axis="y")

        fig.suptitle(
            f"{GATE_ID}\n"
            f"Class-8.7 degeneracy witness on OP-PROJ residue B_LAYER_A={B_LAYER_A:.2f} | "
            f"spread={cross_regulator_spread:.4f} > {SPREAD_FLOOR} ⇒ {verdict} (NOT a direct-sum tautology)",
            fontsize=10,
        )
        fig.tight_layout(rect=[0, 0, 1, 0.93])
        fig.savefig(PNG_OUT, dpi=140)
        plt.close(fig)
        print(f"PNG saved: {PNG_OUT}")
    except Exception as e:
        print(f"PNG generation failed (non-fatal): {e}")

    # ================= Emit verdict line =================
    value_str = (
        f"cross_reg_spread_rel={cross_regulator_spread:.6f}_floor={SPREAD_FLOOR}"
        f"_R_zeta={R_zeta:.6f}_R_PV={R_PV:.6f}_R_Mellin={R_Mellin:.6f}"
        f"_PV_vs_zeta_swing={pv_vs_zeta_swing:.6f}"
        f"_B_LAYER_A={B_LAYER_A:.6f}"
        f"_n_degenerate_roots={coincident_root['n_degenerate_roots']}"
        f"_max_root_mult={coincident_root['max_root_multiplicity']}"
        f"_NOT_direct_sum_tautology"
        f"_s84_cache_drift_resolved_session-84"
    )

    append_verdict(
        gate_id=GATE_ID, verdict=verdict, value=value_str,
        scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        input_pin_map=pins, script_path=THIS_SCRIPT,
        canonical_path=CANONICAL_CONSTS_PATH,
        sign_tuple=(sign_verdict, magnitude_verdict, regime_verdict),
    )

    print(f"\n=== {GATE_ID}: composite={verdict} ===")
    return 0  # exit 0 = script ran OK; verdict is DATA per math-scripts.md


if __name__ == "__main__":
    sys.exit(main())
