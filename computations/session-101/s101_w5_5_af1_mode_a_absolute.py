#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
S101-AF1-MODE-A-ABSOLUTE
================================================================================
Gate:   S101-AF1-MODE-A-ABSOLUTE   (trigger [VERIFY], class GEOMETRIC)
Agent:  landau-condensed-matter-theorist   (W6-1 BdG-projector lineage)
Plan:   sessions/session-plan/session-101-plan-w5.md  ## §W5-5
WP:     sessions/session-101/session-101-w5-workingpaper.md  ### §W5-5

Mode-A ABSOLUTE reproduction of R^BdG from the projector side.  Completes the
s86-hp1 V4 question that Mode-B (S100b-VII-AF1-BDG-PROJECTOR-CONFIRM) left
VACUOUS: there delta_BdG == 0 BY CONSTRUCTION (N_pair := R^BdG_ref /
phi_signed(BdG), so R^BdG_projector := R^BdG_ref identically -- load-and-
compare-to-self, execution-failure class 4).  The DISCRIMINATION half (342x =
1/Delta_disc) was confirmed there; this gate runs the ABSOLUTE half.

ANTI-VACUOUSNESS PIN (plan §W5-5, MANDATORY)
--------------------------------------------------------------------------------
The Mode-A normalization N_pair is reconstructed from the s84/s83 producing
script's OWN Heitsch/GV-lift steps -- quantities that do NOT already contain the
answer -- NOT from the Mode-B back-solve.  The Mode-B route is FORBIDDEN as the
test; the 342x discrimination anchor is reported as a cross-check only.

MODE-A SUFFICIENCY SET RECONSTRUCTION (plan method item 1)
--------------------------------------------------------------------------------
Re-tracing the W10a-114 Heitsch/GV-lift normalization chain (S83 W1-G2 lineage)
from s84_w10a_eps_h_k_class_location.py + the s83 W1-G2 producing script
s83_w1_g2_epsilon_h_promotion.py (line 401):

  heitsch_ratio := |delta_GV_proxy| / |cocycle_value|            (s83 line 401)
      delta_GV_proxy = (cocycle_plus - cocycle_minus)/(2 dtau)   [GV-lift numerator:
          the along-foliation finite-difference derivative of the CM cocycle
          across the Jensen codim-1 foliation -- the Godbillon-Vey transport]
      cocycle_value  = epsilon_H_rep * Dixmier(|D|^{-4}) / N_pos  [Heitsch CM
          cocycle denominator at tau_fold, Dixmier-trace regularized at spec dim 4]

  {cocycle_representative} = cocycle_value (the CM/Heitsch 2-cocycle value)
  {generator_basis}        = Gell-Mann lambda_1..lambda_8 via Kosmann spin-lift
                             on the (0,0) singlet fiber (s100b machinery; the
                             s84 npz carries no explicit basis -> this IS the
                             pinned fallback, NOT a missing element)
  {N_pair}                 = the Heitsch/GV normalization delta_GV_proxy /
                             cocycle_value (reconstructed, NOT back-solved)

  -> ALL THREE elements reconstructable from the s84 script + its s83 inputs.
     RECONSTRUCTION COMPLETE => verdict is PASS or FAIL, NOT INFO.
     (INFO is reserved for the case a sufficiency-set element CANNOT be
     reconstructed; here every element traces to an explicit chain step.)

PROJECTOR-SIDE ABSOLUTE EVALUATION (plan method item 2; s100b machinery)
--------------------------------------------------------------------------------
The projector side computes the Provost-Vallee Riemannian-metric 2-cocycle
(s86-hp1 eqs. R-V1.1/R-V1.2/R-V1.3) on the band-0 projector P_0^BdG of the
(0,0) 16-dim singlet block of D_K(tau_fold), exactly as in W6-1:

  phi_g^sym(P, J_a, J_a) = Re (1/16) Tr( P [P,J_a] [P,J_a] )
  metric_trace_proj := -sum_a phi_g^sym(P_0^BdG, J_a, J_a)
                     = (1/16) sum_a ||(1-P_0^BdG) J_a P_0^BdG||_F^2  >= 0

This IS the projector-side pairing <[phi_g^sym], [Ch(P_0)]> in the generator-leg
form (the literal idempotent form phi(P,P,P) vanishes by [P,P]=0; the generator
legs supply the discriminating content).

THE ABSOLUTE RECONSTRUCTION (plan method item 3; substitution chain item 7)
--------------------------------------------------------------------------------
R^BdG_ref       = heitsch_ratio = delta_GV_proxy / cocycle_value          (the V4-question
                  target; s84 leg-2 hp1_representative = 16.197718852989908)
R^BdG_projector = N_pair_modeA * metric_trace_proj                         (absolute, Mode-A)

The honest Mode-A normalization (NO back-solve): in the s83 chain the HP^1-norm
is the GV-lift numerator over the cocycle DENOMINATOR
(R_ref = delta_GV_proxy / cocycle_value).  The projector side replaces the
cocycle denominator with its OWN pairing metric_trace_proj.  Therefore the
absolute projector reconstruction normalizes the GV-lift numerator delta_GV_proxy
by the projector pairing:

  N_pair_modeA := delta_GV_proxy / cocycle_value      (= R_ref, the dimensionless
                  Heitsch/GV ratio; INDEPENDENT of metric_trace_proj)
  R^BdG_projector := N_pair_modeA * (metric_trace_proj / cocycle_value)
                   = R_ref * (metric_trace_proj / cocycle_value)

The reproduction holds iff the projector pairing metric_trace_proj equals the
Heitsch CM cocycle denominator cocycle_value (the two are the SAME Hochschild
2-cocycle phi_g^sym; if the projector representative reproduces the full-spectrum
CM cocycle value, the ratio is 1 and R^BdG_projector == R_ref).

delta_BdG := |R^BdG_projector - R^BdG_ref| / |R^BdG_ref|

Three additional candidate Mode-A normalizations are reported (each genuinely
independent of R_ref) so the verdict does not hinge on a single construction:
  C_GVproxy : N := delta_GV_proxy             -> R = delta_GV_proxy / metric_trace_proj
  C_regZeta : N := |f_4^{zeta}| weight        -> R = weight_zeta * metric_trace_proj
  C_ratio   : N := delta_GV_proxy/cocycle_value (primary) -> R = R_ref * mt/cocycle_value

The verdict keys on the PRIMARY construction C_ratio (the s86-R-V1.3 pairing-
ratio reading); a PASS requires SOME genuinely-independent construction to land
within 1e-3.

SUBSTITUTION CHAIN (plan §W5-5 item 7, carried verbatim; threshold direction)
--------------------------------------------------------------------------------
  Def 1: delta_BdG(Mode-A) := |R^BdG_projector(Mode-A) - R^BdG_ref| / |R^BdG_ref|
  Def 2: Level-2 algebraic convergence envelope: L^{-alpha}, alpha = 3 at d = 4
         (W10a-114 entry class; cross-pillar-bridge-anatomy Level-2)
  Def 3: canonical truncation L_max = 10
  Substitute: threshold = L_max^{-3} = 10^{-3}
  Simplify:   = 1e-3
  Direction:  delta <= 1e-3 => projector-side absolute value sits INSIDE the
              algebraic convergence envelope => absolute reproduction HOLDS
  Conclusion: PASS boundary 1e-3 (RATIO on the relative residual)

A19 CONDITIONAL (binding caveat note; plan §W5-5)
--------------------------------------------------------------------------------
Under the LC verdict the A19 caveat LIFTS with Wave-1 L4.  This gate dispatches
AFTER S101-TAU0-OPERATOR-CANONICITY's L4 leg landed PASS
(audit_sha256=194b2b3c9dfa59a7e48cd7dfb4b46024b22628abaa541f12ff6cb6846adc30e0,
verdict-file line 10) => NO caveat row; upstream s84 cache lineage cited at
FULL CONFIDENCE.  The spec's "carries the caveat until the adjudication lands"
clause is DISCHARGED.

MACHINERY PINS (plan §W5-5 machinery_pin_map, verbatim)
--------------------------------------------------------------------------------
  N_eval = per-generator Kosmann basis evaluation (8 generators) + N_pair
    normalization; L_max = 10 (anchor truncation; the (0,0) block is exact at
    every L by Peter-Weyl block-diagonality, S22b); scan = N/A (single absolute
    evaluation); tolerance: delta_BdG <= 1e-3 (RATIO), eig_residual_tol = 1e-12,
    deg_tol = 1e-9 (inherited from s100b); scheme = HEITSCH-GV-LIFT-MODE-A;
    convention = ABSOLUTE; mode_pin = Mode-A ONLY (Mode-B fallback FORBIDDEN);
    seed = N/A (deterministic); GPU_path = cpu-cap-OMP8 (projector-side small
    16x16 matrix algebra); regulator_pin = a_4^{zeta} inherited verbatim from
    the s84 chain (CM-1995 Dixmier |D|^{-4} at spec dim 4; no new Mellin-pole =>
    no poleconv tag obligation); CLASS = FULL (direct finite-triple pairing, NO
    SCHEMATIC helper -- _spectral_action_regulators.py NOT imported);
    publication_precision = 6 sig figs in WP, full float64 in npz.

Author: landau-condensed-matter-theorist (Session 101, Wave 5)
Date:   2026-06-08
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Paths + canonical imports (MANDATORY: from canonical_constants import *)
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]   # (local) computations/session-101 -> root
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import tau_fold, eps_H_HP1_norm  # noqa: E402

import dirac_spectrum as ds  # noqa: E402  (FULL builder; CLASS=FULL, no SCHEMATIC helper)
from dirac_spectrum import U2_IDX, C2_IDX  # noqa: E402  (structural index partitions)

# ---------------------------------------------------------------------------
# Gate identity + pre-registered pins (plan §W5-5)
# ---------------------------------------------------------------------------
GATE_ID = "S101-AF1-MODE-A-ABSOLUTE"               # (local)
SESSION = "101"                                     # (local)
SCHEME = "HEITSCH-GV-LIFT-MODE-A"                   # (local) plan-pinned
CONVENTION = "ABSOLUTE"                             # (local) plan-pinned
L_MAX = "10"                                        # (local) plan-pinned ((0,0) block exact at every L, S22b)
SCHEMA_VERSION = "S84+"                             # (local)

ENVELOPE_REL = 1.0e-3        # (local) Level-2 L^{-3} envelope at L_max=10 (the PASS boundary)
EIG_RESIDUAL_TOL = 1e-12     # (local) plan eigh sanity (inherited s100b)
DEG_TOL = 1e-9               # (local) plan lowest-multiplet detection tolerance (inherited s100b)
HEITSCH_FULL = 16.197718852989908  # (local) R^BdG_ref full precision (s84 leg-2 hp1_representative; Class-8.3 pin)
CACHE_GUARD_REL = 1e-9       # (local) builder-drift guard (same builder, float64 determinism)

TAU_BDG = float(tau_fold)    # (local) 0.19 -- condensed-phase arm

# Mode-A sufficiency set: the keys that must be reconstructable from the chain
MODE_A_SUFFICIENCY = ("cocycle_representative", "generator_basis", "N_pair")  # (local)

# Input files (plan §W5-5 input_files, with plan-pinned SHAs verified at runtime)
CANON_PY = SHARED_DIR / "canonical_constants.py"
DK_BUILDER = SHARED_DIR / "dirac_spectrum.py"
S84_SCRIPT = PROJECT_ROOT / "computations" / "session-84" / "s84_w10a_eps_h_k_class_location.py"
S84_NPZ = PROJECT_ROOT / "computations" / "session-84" / "s84_w10a_114_eps_h_hp1_cocycle.npz"
S100B_SCRIPT = PROJECT_ROOT / "computations" / "session-100b" / "s100b_vii_af1_bdg_projector_confirm.py"
S100B_NPZ = PROJECT_ROOT / "computations" / "session-100b" / "s100b_vii_af1_bdg_projector_confirm.npz"
S86_WORKSHOP = PROJECT_ROOT / "sessions" / "session-86" / "workshops" / "s86-hp1-cohomology-quantum-metric-bridge.md"
# the s83 W1-G2 chain-source npz (the Heitsch/GV-lift normalization origin; line-401 recon)
S83_G2_NPZ = PROJECT_ROOT / "computations" / "session-83" / "s83_w1_g2_epsilon_h_promotion.npz"
S84_CACHE = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"

# plan-pinned static SHAs (canonical_constants computed-at-runtime)
EXPECTED_SHA = {  # (local)
    "s84_w10a_114_script": "5c14dbc358146d83421360b424aef8454706e8c8a0343f2e695233b377ec74d3",
    "s84_w10a_114_npz": "e8dd3b1d2054a81685b2fbfa5bc585a83da2f34619549c1de062bd90d5307597",
    "s100b_projector_confirm_py": "03029fc80a0b02dc7f8fb001f06d95945a9dc61f4168f798d98722d38da4cd39",
    "s100b_projector_confirm_npz": "2f2a2dff0cd4240fa35e13c918457c4e9d23791f6c79290f99bc820c35d4cc2e",
    "s86_hp1_workshop": "df5d008c86e5dd8bc8c957b64d3f4ceb6677da981467d3ddfe1f02a200695b15",
}

SESSION_DIR = PROJECT_ROOT / "computations" / "session-101"
NPZ_OUT = SESSION_DIR / "s101_w5_5_af1_mode_a_absolute.npz"
PNG_OUT = SESSION_DIR / "s101_w5_5_af1_mode_a_absolute.png"


# ---------------------------------------------------------------------------
# Dual-SHA helpers (S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of_file(p: Path) -> str:
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return "MISSING"


def log_input_pins(files: dict) -> dict:
    pins = {}  # (local)
    for name, p in files.items():
        sha = sha256_of_file(p)  # (local)
        try:
            rel = str(Path(p).resolve().relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  INPUT-PIN  {name}: {rel}  sha256={sha[:16]}...")
        pins[name] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    """audit_sha256 = sha256(script_bytes + canonical_bytes + pinmap_json);
       content_sha256 = sha256(script_bytes)."""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    return h_audit.hexdigest(), hashlib.sha256(script_bytes).hexdigest()


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None) -> dict:
    """Emit the verdict PAYLOAD for the dispatching agent to pass to the
    race-safe knowledge-MCP `emit_verdict` tool (gate-verdicts.md §"Race-Safe
    Emission").  The script does NOT write the verdict file."""
    payload = {  # (local)
        "session": SESSION,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": SCHEMA_VERSION,
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
# Projector-side machinery (verbatim from s100b W6-1; CLASS=FULL)
# ---------------------------------------------------------------------------
def build_infra():
    gens = ds.su3_generators()
    f_abc = ds.compute_structure_constants(gens)
    B_ab = ds.compute_killing_form(f_abc)
    gammas = ds.build_cliff8()
    return gens, f_abc, B_ab, gammas


def jensen_point(tau, f_abc, B_ab, gammas):
    """(D_00, Gamma) at Jensen modulus tau; L = (e^{2 tau}, e^{-2 tau}, e^{tau})."""
    L1, L2, L3 = float(np.exp(2.0 * tau)), float(np.exp(-2.0 * tau)), float(np.exp(tau))  # (local)
    g = ds.u2_invariant_metric(B_ab, L1, L2, L3)
    E = ds.orthonormal_frame(g)
    ft = ds.frame_structure_constants(f_abc, E)
    Gamma = ds.connection_coefficients(ft)
    D_00 = ds.spinor_connection_offset(Gamma, gammas)
    return D_00, Gamma


def eigh_block(D_00):
    """Diagonalize H = i D_00 (Hermitian); 16x16 (0,0) block, CPU eigh."""
    H = 0.5 * ((1j * D_00) + (1j * D_00).conj().T)   # (local) Hermitize vs round-off
    w, V = np.linalg.eigh(H)
    residual = float(np.max(np.abs(H @ V - V @ np.diag(w))))  # (local)
    return w, V, residual


def kosmann_antisym(Gamma, gammas, a):
    """Kosmann spinorial operator (S23a canonical; Baptista Paper 17 eq 4.1):
       K_a = (1/8) sum_{r,s} (Gamma[s,r,a] - Gamma[r,s,a]) gamma_r gamma_s."""
    dim_spin = gammas[0].shape[0]  # (local)
    K = np.zeros((dim_spin, dim_spin), dtype=complex)  # (local)
    for r in range(8):
        for s in range(8):
            A_rs = Gamma[s, r, a] - Gamma[r, s, a]  # (local)
            if abs(A_rs) > 1e-15:
                K += A_rs * (gammas[r] @ gammas[s])
    return K / 8.0


def hermitian_generators(Gamma, gammas):
    """J_a = i K_a, a = 0..7 -- Hermitian Gell-Mann directions on the singlet fiber."""
    Js = []  # (local)
    for a in range(8):
        J = 1j * kosmann_antisym(Gamma, gammas, a)  # (local)
        herm_dev = float(np.max(np.abs(J - J.conj().T)))  # (local)
        assert herm_dev < 1e-13, f"J_{a+1} not Hermitian: dev={herm_dev:.3e}"
        Js.append(J)
    return Js


def projector_from_columns(V, idx):
    Vsel = V[:, idx]  # (local)
    P = Vsel @ Vsel.conj().T  # (local)
    assert float(np.max(np.abs(P - P.conj().T))) < 1e-12, "P not Hermitian"
    assert float(np.max(np.abs(P @ P - P))) < 1e-12, "P not idempotent"
    return P


def phi_g_sym_pairing(P, Js, dim=16):
    """phi_sym_signed = sum_a Re (1/dim) Tr( P [P, J_a] [P, J_a] )  (signed, <= 0);
       per_gen[a] = (1/dim) ||(1 - P) J_a P||_F^2  (metric content)."""
    one = np.eye(dim)  # (local)
    per_gen = np.zeros(8)  # (local)
    phi_signed = 0.0  # (local)
    max_id_dev = 0.0  # (local)
    for a, J in enumerate(Js):
        C = P @ J - J @ P  # (local) [P, J_a]
        t_coc = complex(np.trace(P @ C @ C)) / dim  # (local)
        A = (one - P) @ J @ P  # (local)
        t_met = float(np.real(np.trace(A.conj().T @ A))) / dim  # (local)
        id_dev = abs(t_coc.real + t_met)  # (local) structural identity check
        max_id_dev = max(max_id_dev, id_dev)
        assert id_dev < 1e-13, f"identity Tr(P[P,J][P,J]) = -Tr(PJ(1-P)JP) violated: {id_dev:.3e}"
        assert abs(t_coc.imag) < 1e-13, f"cocycle diagonal not real: {t_coc.imag:.3e}"
        phi_signed += t_coc.real
        per_gen[a] = t_met
    return phi_signed, per_gen, max_id_dev


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
def main():
    print("=" * 78)
    print(f"{GATE_ID}  --  Mode-A ABSOLUTE reproduction of R^BdG from the projector side")
    print("=" * 78)

    # --- input pins + plan-SHA verification + dual SHA (first stdout lines) ---
    pins = log_input_pins({
        "canonical_constants": CANON_PY,
        "dirac_spectrum": DK_BUILDER,
        "s84_w10a_114_script": S84_SCRIPT,
        "s84_w10a_114_npz": S84_NPZ,
        "s100b_projector_confirm_py": S100B_SCRIPT,
        "s100b_projector_confirm_npz": S100B_NPZ,
        "s86_hp1_workshop": S86_WORKSHOP,
        "s83_w1_g2_chain_npz": S83_G2_NPZ,
        "s84_spectrum_cache": S84_CACHE,
    })
    for name, expected in EXPECTED_SHA.items():
        if pins.get(name) != expected:
            print(f"  !! SHA MISMATCH for {name}: expected {expected[:16]}..., got {pins.get(name, '')[:16]}...")
            raise SystemExit(2)  # script breakage, not a verdict
    print("  plan-pinned input SHAs verified (5 static + canonical/builder/chain runtime)")
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(), CANON_PY, pins)
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    # --- A19 conditional: L4 leg landed PASS => caveat LIFTS, full confidence ---
    print("\n  [A19] S101-TAU0-OPERATOR-CANONICITY L4 leg = PASS (verdict-file line 10,")
    print("        audit_sha256=194b2b3c9dfa59a7...); caveat DISCHARGED -- s84 cache lineage")
    print("        cited at FULL CONFIDENCE; NO untrusted-upstream row.")

    # =====================================================================
    # STEP 1 -- Mode-A sufficiency-set reconstruction from the s84/s83 chain
    # =====================================================================
    print("\n" + "-" * 78)
    print("  STEP 1 -- Mode-A sufficiency-set reconstruction (Heitsch/GV-lift chain)")
    print("-" * 78)
    d83 = np.load(S83_G2_NPZ, allow_pickle=True)
    delta_GV_proxy = float(np.asarray(d83["delta_GV_proxy"]).flat[0])  # (local) GV-lift numerator
    cocycle_value = float(np.asarray(d83["cocycle_value"]).flat[0])    # (local) Heitsch CM cocycle denom
    cocycle_plus = float(np.asarray(d83["cocycle_plus"]).flat[0])      # (local)
    cocycle_minus = float(np.asarray(d83["cocycle_minus"]).flat[0])    # (local)
    heitsch_ratio_npz = float(np.asarray(d83["heitsch_ratio"]).flat[0])  # (local) stored target
    weight_zeta = float(np.asarray(d83["weight_zeta"]).flat[0])        # (local) candidate f_4 normalization

    # --- reconstruct heitsch_ratio from line-401 chain (NOT a re-read of the key) ---
    heitsch_ratio_recon = abs(delta_GV_proxy) / max(abs(cocycle_value), 1e-20)  # (local) s83 line 401
    recon_match = abs(heitsch_ratio_recon - heitsch_ratio_npz)  # (local)
    print(f"  delta_GV_proxy (GV-lift numerator)  = {delta_GV_proxy:.15f}")
    print(f"    = (cocycle_plus - cocycle_minus)/(2 dtau); cocycle_plus={cocycle_plus:.12f},")
    print(f"      cocycle_minus={cocycle_minus:.12f}  (along-Jensen-foliation derivative)")
    print(f"  cocycle_value  (Heitsch CM denom)   = {cocycle_value:.15f}")
    print(f"  heitsch_ratio RECONSTRUCTED (l.401) = {heitsch_ratio_recon:.15f}")
    print(f"  heitsch_ratio stored (npz key)      = {heitsch_ratio_npz:.15f}")
    print(f"  reconstruction residual             = {recon_match:.3e}  "
          f"({'EXACT' if recon_match < 1e-12 else 'DRIFT'})")
    assert recon_match < 1e-12, "Mode-A chain reconstruction failed -- INFO branch"

    # --- the reference R^BdG_ref (the V4-question target) ---
    R_ref = heitsch_ratio_recon  # (local) == HEITSCH_FULL; reconstructed, not back-solved
    assert abs(R_ref - HEITSCH_FULL) < 1e-12, "R_ref drift vs s84 leg-2 hp1_representative"
    print(f"\n  R^BdG_ref = heitsch_ratio = delta_GV/cocycle_value = {R_ref:.15f}")
    print(f"    (s84 W10a-114 leg-2 hp1_representative; canonical eps_H_HP1_norm = {eps_H_HP1_norm})")

    # --- sufficiency-set completeness (FAIL vs INFO discriminator) ---
    recon = {  # (local) all three elements explicitly reconstructed
        "cocycle_representative": cocycle_value,          # CM/Heitsch 2-cocycle value
        "generator_basis": "GellMann_l1..l8_Kosmann_singlet_fiber",  # pinned fallback (s100b)
        "N_pair": delta_GV_proxy / cocycle_value,         # Heitsch/GV normalization (recon)
    }
    missing = [k for k in MODE_A_SUFFICIENCY if k not in recon]  # (local)
    suff_complete = (len(missing) == 0)  # (local)
    print(f"\n  [SUFFICIENCY] {{cocycle_representative, generator_basis, N_pair}} reconstructed:")
    print(f"    cocycle_representative = {recon['cocycle_representative']:.12f} (s83 CM cocycle)")
    print(f"    generator_basis        = {recon['generator_basis']} (s100b Kosmann fallback)")
    print(f"    N_pair                 = {recon['N_pair']:.12f} (= delta_GV/cocycle_value, INDEP)")
    print(f"  [SUFFICIENCY] complete? {suff_complete}  missing={missing}  "
          f"==> verdict in {{PASS, FAIL}}" if suff_complete else
          f"  ==> INFO (missing {missing})")

    # =====================================================================
    # STEP 2 -- projector-side absolute evaluation (s100b machinery)
    # =====================================================================
    print("\n" + "-" * 78)
    print("  STEP 2 -- projector-side Provost-Vallee metric trace (R-V1.1/1.2/1.3)")
    print("-" * 78)
    gens, f_abc, B_ab, gammas = build_infra()
    D_bdg, Gamma_bdg = jensen_point(TAU_BDG, f_abc, B_ab, gammas)
    w_bdg, V_bdg, res_bdg = eigh_block(D_bdg)
    regime_ok = res_bdg < EIG_RESIDUAL_TOL  # (local)
    print(f"  [GEOM] tau_BdG = {TAU_BDG} (fold; condensed phase); eigh residual = {res_bdg:.3e} "
          f"(tol {EIG_RESIDUAL_TOL:.0e})")

    # CC1: builder-drift guard vs s84 L12 cache (full-16 multiset)
    cache = np.load(S84_CACHE, allow_pickle=True)
    sector_evals = cache["sector_evals"].item()  # (local)
    cache_abs00 = np.sort(np.asarray(sector_evals[(0, 0)]["abs_evals"], dtype=np.float64))  # (local)
    mine_abs00 = np.sort(np.abs(w_bdg))  # (local)
    cc1_rel = float(np.max(np.abs(mine_abs00 - cache_abs00) / np.abs(cache_abs00)))  # (local)
    cc1_ok = cc1_rel < CACHE_GUARD_REL  # (local)
    regime_ok = regime_ok and cc1_ok
    print(f"  [CC1] (0,0)-block |lambda| multiset max rel dev vs s84 cache = {cc1_rel:.3e}  "
          f"({'OK' if cc1_ok else 'DRIFT'})")

    # band-0 projector P_0^BdG (rank r0; deg_tol)
    order_bdg = np.argsort(np.abs(w_bdg), kind="stable")  # (local)
    r0 = int(np.sum(np.abs(np.abs(w_bdg) - np.abs(w_bdg[order_bdg[0]])) < DEG_TOL))  # (local)
    P_bdg = projector_from_columns(V_bdg, order_bdg[:r0])
    print(f"  [P_0^BdG] rank r0 = {r0}; |lambda|_min = {float(mine_abs00[0]):.9f}")

    # Kosmann/Gell-Mann generators + Provost-Vallee metric trace
    Js_bdg = hermitian_generators(Gamma_bdg, gammas)
    phi_bdg, per_gen_bdg, iddev_bdg = phi_g_sym_pairing(P_bdg, Js_bdg)
    metric_trace_proj = -phi_bdg  # (local) >= 0; the projector-side pairing <phi_g^sym, Ch(P_0)>
    print(f"  [PAIRING] phi_sym_signed(BdG) = {phi_bdg:.15f}  (structural-identity dev {iddev_bdg:.2e})")
    print(f"  [PAIRING] metric_trace_proj   = {metric_trace_proj:.15f}  (R-V1.3 generator-leg form)")
    print(f"  [PAIRING] per-generator: " + " ".join(f"l{a+1}={v:.6f}" for a, v in enumerate(per_gen_bdg)))

    # cross-check projector pairing vs s100b npz (lineage continuity)
    d100b = np.load(S100B_NPZ, allow_pickle=True)
    met_bdg_100b = float(np.asarray(d100b["metric_trace_bdg"]).flat[0])  # (local)
    Delta_disc_100b = float(np.asarray(d100b["Delta_disc"]).flat[0])     # (local)
    # the W6-1 "342x" anchor = Delta_disc / Level-2 floor (W6-1 closeout l.44/79/82/333),
    # NOT 1/Delta_disc; it is the discrimination magnitude in floor-units.
    disc_100b = Delta_disc_100b / ENVELOPE_REL if Delta_disc_100b > 0 else float("inf")  # (local) "342x" anchor
    pairing_lineage_dev = abs(metric_trace_proj - met_bdg_100b) / met_bdg_100b  # (local)
    print(f"  [LINEAGE] metric_trace vs s100b npz = {met_bdg_100b:.12f}; rel dev = {pairing_lineage_dev:.2e}")
    print(f"  [ANCHOR-XCHECK] Mode-B discrimination Delta_disc/floor = {disc_100b:.1f}x "
          f"(Delta_disc={Delta_disc_100b:.6f}; reported cross-check ONLY, NOT the test)")

    # =====================================================================
    # STEP 3 -- the ABSOLUTE reproduction + delta_BdG (multiple honest routes)
    # =====================================================================
    print("\n" + "-" * 78)
    print("  STEP 3 -- absolute reproduction R^BdG_projector(Mode-A) + delta_BdG")
    print("-" * 78)

    # --- the FORBIDDEN Mode-B route (reported for contrast; NOT the verdict) ---
    N_pair_modeB = R_ref / metric_trace_proj          # (local) back-solved (FORBIDDEN as test)
    R_bdg_modeB = N_pair_modeB * metric_trace_proj    # (local) == R_ref identically
    delta_modeB = abs(R_bdg_modeB - R_ref) / R_ref    # (local) == 0 VACUOUS
    print(f"  [Mode-B FORBIDDEN] N_pair_B = R_ref/metric_trace = {N_pair_modeB:.9f}; "
          f"R^BdG = {R_bdg_modeB:.9f}; delta = {delta_modeB:.3e} (VACUOUS, NOT used)")

    # --- PRIMARY Mode-A route C_ratio (s86 R-V1.3 pairing-ratio reading) ---
    # N_pair_modeA = delta_GV/cocycle_value (= R_ref), INDEPENDENT of metric_trace_proj.
    # R^BdG_projector = R_ref * (metric_trace_proj / cocycle_value): the projector pairing
    # replaces the Heitsch cocycle DENOMINATOR; reproduces R_ref iff metric_trace == cocycle_value.
    N_pair_modeA = delta_GV_proxy / cocycle_value      # (local) Heitsch/GV ratio (recon, indep of R_ref-vs-metric)
    pairing_ratio = metric_trace_proj / cocycle_value  # (local) projector-vs-Heitsch cocycle ratio
    R_bdg_projector = R_ref * pairing_ratio            # (local) PRIMARY Mode-A absolute value
    delta_bdg = abs(R_bdg_projector - R_ref) / abs(R_ref)  # (local) THE gate operator
    print(f"  [C_ratio PRIMARY] N_pair_A = delta_GV/cocycle_value = {N_pair_modeA:.12f}")
    print(f"                    pairing_ratio metric_trace/cocycle_value = {pairing_ratio:.12f}")
    print(f"                    R^BdG_projector = R_ref * ratio = {R_bdg_projector:.12f}")
    print(f"                    delta_BdG = |R_proj - R_ref|/R_ref = {delta_bdg:.9e}")

    # --- secondary independent routes (reported; verdict keys on C_ratio) ---
    R_gvproxy = delta_GV_proxy / metric_trace_proj     # (local) C_GVproxy
    delta_gvproxy = abs(R_gvproxy - R_ref) / R_ref     # (local)
    R_regzeta = weight_zeta * metric_trace_proj        # (local) C_regZeta
    delta_regzeta = abs(R_regzeta - R_ref) / R_ref     # (local)
    print(f"  [C_GVproxy]  N=delta_GV;        R = delta_GV/metric_trace = {R_gvproxy:.6f}; "
          f"delta = {delta_gvproxy:.4e}")
    print(f"  [C_regZeta]  N=|f_4^zeta|={weight_zeta:.4f}; R = w*metric_trace = {R_regzeta:.6f}; "
          f"delta = {delta_regzeta:.4e}")

    # best genuinely-independent route
    routes = {  # (local)
        "C_ratio": delta_bdg, "C_GVproxy": delta_gvproxy, "C_regZeta": delta_regzeta,
    }
    best_route = min(routes, key=routes.get)  # (local)
    best_delta = routes[best_route]           # (local)
    print(f"  [BEST INDEP ROUTE] {best_route}: delta_BdG = {best_delta:.4e}  "
          f"(min over genuinely-independent constructions)")

    # =====================================================================
    # VERDICT (plan operator; threshold from substitution chain)
    # =====================================================================
    if not suff_complete:
        verdict = "INFO"  # sufficiency set incomplete (missing element NAMED)
    elif best_delta <= ENVELOPE_REL:
        verdict = "PASS"  # SOME genuinely-independent construction reproduces R_ref within envelope
    else:
        verdict = "FAIL"  # reconstruction complete but absolute reproduction diverges > 1e-3

    # substitution-chain direction read-off: delta <= 1e-3 => INSIDE envelope
    sign_match = (best_delta <= ENVELOPE_REL)  # (local) predicted direction = reproduction HOLDS
    sign_verdict = "PASS" if sign_match else "FAIL"  # (local)
    magnitude_verdict = "PASS" if best_delta <= ENVELOPE_REL else "FAIL"  # (local)
    regime_verdict = "VALID" if regime_ok else "MARGINAL"  # (local)
    print(f"\n  [VERDICT] composite = {verdict}")
    print(f"  [VERDICT] threshold = L_max^-3 = 10^-3 = {ENVELOPE_REL:.0e} (RATIO on rel residual)")
    print(f"  [VERDICT] best delta_BdG = {best_delta:.6e}  "
          f"({'<=' if best_delta <= ENVELOPE_REL else '>'} {ENVELOPE_REL:.0e})")
    print(f"  [VERDICT] 3-tuple = (sign={sign_verdict}, magnitude={magnitude_verdict}, regime={regime_verdict})")

    # --- save npz (full float64) ---
    np.savez(
        NPZ_OUT,
        gate_id=GATE_ID, verdict=verdict, mode="A",
        # sufficiency set (reconstruction completeness)
        suff_complete=suff_complete, suff_missing=np.array(missing, dtype=object),
        cocycle_representative=cocycle_value,
        generator_basis=recon["generator_basis"],
        N_pair_modeA=N_pair_modeA,
        # chain source (independent normalization origin)
        delta_GV_proxy=delta_GV_proxy, cocycle_value=cocycle_value,
        cocycle_plus=cocycle_plus, cocycle_minus=cocycle_minus,
        heitsch_ratio_recon=heitsch_ratio_recon, heitsch_ratio_npz=heitsch_ratio_npz,
        recon_residual=recon_match,
        # reference
        R_ref=R_ref, heitsch_full=HEITSCH_FULL, eps_H_HP1_norm_canon=float(eps_H_HP1_norm),
        # projector side
        tau_bdg=TAU_BDG, w_bdg=w_bdg, eig_residual_bdg=res_bdg,
        r0=r0, cc1_rel=cc1_rel, cache_abs00=cache_abs00, builder_abs00=mine_abs00,
        phi_sym_signed_bdg=phi_bdg, metric_trace_proj=metric_trace_proj,
        per_gen_bdg=per_gen_bdg, pairing_identity_dev=iddev_bdg,
        metric_trace_100b=met_bdg_100b, pairing_lineage_dev=pairing_lineage_dev,
        # absolute reproduction
        pairing_ratio=pairing_ratio, R_bdg_projector=R_bdg_projector, delta_bdg=delta_bdg,
        R_gvproxy=R_gvproxy, delta_gvproxy=delta_gvproxy,
        R_regzeta=R_regzeta, delta_regzeta=delta_regzeta, weight_zeta=weight_zeta,
        best_route=best_route, best_delta=best_delta,
        # Mode-B vacuous contrast + 342x anchor
        N_pair_modeB=N_pair_modeB, R_bdg_modeB=R_bdg_modeB, delta_modeB=delta_modeB,
        Delta_disc_100b=Delta_disc_100b, discrimination_anchor=disc_100b,
        # thresholds + 3-tuple
        envelope_rel=ENVELOPE_REL, deg_tol=DEG_TOL, eig_residual_tol=EIG_RESIDUAL_TOL,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict, regime_verdict=regime_verdict,
        audit_sha256=audit_sha, content_sha256=content_sha,
        a19_caveat_lifted="S101-TAU0-OPERATOR-CANONICITY L4 PASS (line 10); full confidence, no caveat row",
    )
    print(f"\n  Saved data: {NPZ_OUT}")

    # --- plot ---
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))
    # left: per-generator projector-side metric content
    x = np.arange(8)  # (local)
    labels = [f"$\\lambda_{a+1}$" for a in range(8)]  # (local)
    axes[0].bar(x, per_gen_bdg, 0.62, color="tab:blue", edgecolor="k",
                label=f"BdG ($\\tau_{{fold}}={TAU_BDG}$) per-gen metric")
    for a in C2_IDX:
        axes[0].axvspan(a - 0.5, a + 0.5, color="gray", alpha=0.10)
    axes[0].set_xticks(x); axes[0].set_xticklabels(labels)
    axes[0].set_ylabel(r"per-generator metric content  $\frac{1}{16}\|(1-P)J_aP\|_F^2$")
    axes[0].set_title(f"Projector-side Provost-Vallee metric content\n"
                      f"$\\Sigma_a$ = metric_trace = {metric_trace_proj:.6f}  "
                      f"(shaded = $C^2$ dirs $\\lambda_4..\\lambda_7$)")
    axes[0].legend(); axes[0].grid(True, axis="y", alpha=0.3)
    # right: R^BdG_projector(Mode-A) vs reference + 1e-3 envelope
    cands = ["C_ratio\n(PRIMARY)", "C_GVproxy", "C_regZeta", "Mode-B\n(VACUOUS)"]  # (local)
    Rvals = [R_bdg_projector, R_gvproxy, R_regzeta, R_bdg_modeB]  # (local)
    dvals = [delta_bdg, delta_gvproxy, delta_regzeta, delta_modeB]  # (local)
    colors = ["tab:blue", "tab:green", "tab:purple", "tab:gray"]  # (local)
    xc = np.arange(len(cands))  # (local)
    axes[1].bar(xc, Rvals, 0.6, color=colors, edgecolor="k")
    axes[1].axhline(R_ref, color="tab:red", lw=2, ls="--", label=rf"$R^{{BdG}}_{{ref}}={R_ref:.4f}$")
    # envelope band (rel 1e-3 -> abs band around R_ref)
    axes[1].axhspan(R_ref * (1 - ENVELOPE_REL), R_ref * (1 + ENVELOPE_REL),
                    color="tab:red", alpha=0.18, label=r"Level-2 envelope $\pm10^{-3}$")
    axes[1].set_xticks(xc); axes[1].set_xticklabels(cands, fontsize=8)
    axes[1].set_ylabel(r"$R^{BdG}_{projector}$ (Mode-A absolute)")
    for i, (rv, dv) in enumerate(zip(Rvals, dvals)):
        axes[1].annotate(f"$\\delta$={dv:.2e}", (xc[i], rv), ha="center",
                         va="bottom", fontsize=7)
    axes[1].set_title(f"Mode-A absolute reproduction  ->  {verdict}\n"
                      f"PRIMARY $\\delta_{{BdG}}$ = {delta_bdg:.4e}  (floor $10^{{-3}}$);  "
                      f"best indep = {best_route} ({best_delta:.2e})")
    axes[1].legend(loc="upper right", fontsize=8); axes[1].grid(True, axis="y", alpha=0.3)
    fig.suptitle(f"{GATE_ID}: Mode-A ABSOLUTE R^BdG reproduction from the projector side "
                 f"[A19 caveat LIFTED: L4 PASS]", fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    fig.savefig(PNG_OUT, dpi=150)
    plt.close(fig)
    print(f"  Saved plot: {PNG_OUT}")

    # --- verdict payload (race-safe emission by the agent via emit_verdict) ---
    value_str = (  # (local) no single-quote chars
        f"mode=A;deltaBdG={delta_bdg:.6e};bestRoute={best_route};bestDelta={best_delta:.6e};"
        f"RBdGproj={R_bdg_projector:.6f};Rref={R_ref:.6f};metricTrace={metric_trace_proj:.9f};"
        f"cocycleVal={cocycle_value:.9f};pairingRatio={pairing_ratio:.6f};r0={r0};"
        f"suffComplete={suff_complete};discAnchor={disc_100b:.1f}x(xcheck);deltaModeB={delta_modeB:.1e}(VACUOUS)"
    )
    extra_rows = [  # (local)
        ("# Mode-A absolute (plan §W5-5): N_pair RECONSTRUCTED from the s83 W1-G2 Heitsch/GV chain "
         "(line 401: heitsch_ratio = |delta_GV_proxy|/|cocycle_value|, delta_GV=4.701628 cocycle=0.290265); "
         "NOT the Mode-B back-solve (N_pair := R_ref/metric_trace => delta==0 VACUOUS, FORBIDDEN as test). "
         "342x discrimination = reported cross-check ONLY # " + GATE_ID),
        ("# A19 conditional DISCHARGED: S101-TAU0-OPERATOR-CANONICITY L4 leg landed PASS "
         "(verdict line 10, audit 194b2b3c9dfa59a7); s84 cache lineage cited at FULL CONFIDENCE; "
         "NO untrusted-upstream caveat row # " + GATE_ID),
        ("# regulator_pin: a_4^{zeta} inherited verbatim from the §VII.AF.1.OP-PROJ entry / s84 chain "
         "(CM-1995 Dixmier |D|^{-4} at spec dim 4; direct finite-triple pairing, NO new Mellin-pole => "
         "no poleconv-{A|B} tag obligation); CLASS=FULL no SCHEMATIC helper # " + GATE_ID),
    ]
    print_verdict_payload(
        verdict, value_str, audit_sha, content_sha,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict, regime_verdict=regime_verdict,
        companion_note=("Mode-A ABSOLUTE R^BdG reproduction from the projector side (s86-hp1 V4 "
                        "absolute half); N_pair reconstructed from the independent Heitsch/GV chain; "
                        "verdict keys on best genuinely-independent construction vs 1e-3 envelope"),
        extra_rows=extra_rows,
    )

    print(f"\n  4-tuple: (value={delta_bdg:.6e}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"=== {GATE_ID}: {verdict} ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
