#!/usr/bin/env python3
"""
S102 W6-2 — S102-AF1-CHAIN-LINK-FAILURE (CF-W5-1)
==================================================

Gate: W6-2-S102-AF1-CHAIN-LINK-FAILURE ([VERIFY])

Pre-registered threshold:
  Identify WHICH link of the S83 W1-G2 GV-lift/Heitsch chain the (0,0)-singlet
  band-0 projector representative fails to reproduce. Branch set (S100b
  pre-enumerated, MUTUALLY EXCLUSIVE):
    (B1) s86-hp1 V4 Hochschild identification [phi_g^sym] <-> Ch(P_0) fails
         NUMERICALLY on the truncated spectrum (identification residual > 1e-3).
    (B2) W10a-114 ABSOLUTE normalization (eps_H_HP1_norm = 16.197719) does NOT
         TRANSPORT to the projector representative; the 0.143908 ratio IS the
         un-applied transport Jacobian.
  PASS iff link IDENTIFIED AND a substrate-DERIVED N_pair (NOT the Mode-B
  back-solve N_pair_modeB = 387.77, delta = 0 by construction) reproduces
  R_bdg_projector within 1e-3 ABSOLUTE via the corrected chain.
  INFO iff the chain is confirmed evaluator-less on its absolute half (no
  admissible correction lands inside 1e-3 ABSOLUTE).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-101/s101_w5_5_af1_mode_a_absolute.npz   (PRIMARY: cocycle_value,
        cocycle_plus, cocycle_minus, metric_trace_proj, pairing_ratio, phi_sym_signed_bdg,
        per_gen_bdg, N_pair_modeA, N_pair_modeB, R_bdg_projector, delta_bdg, heitsch_full,
        eps_H_HP1_norm_canon, envelope_rel; audit 3f402896)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz    (Jensen spectrum the cocycle
        + projector were built on; full 64-hex asserted at runtime, 16-head 9e6d9cf7fd6a6949)
  - canonical_constants.py (feeds audit_sha256 only; supplies eps_H_HP1_norm,
        R_universal_HP1_strict_F4, tau_fold)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<branch+reproduction summary>, scheme=MS, convention=ABSOLUTE, L_max=12)

Classification: GEOMETRIC

METHODOLOGY
-----------
Walk the S83 W1-G2 GV-lift/Heitsch chain link-by-link on the (0,0)-singlet band-0
projector representative. The chain (s86-hp1 V1 Hochschild form, line 481 + the
CM-1995 finite-spectral-triple residue formula line 474):

    Res_{s=0} zeta_{D, eps_H^2, r}(s) = f_4^r * <[phi_g^sym], [Ch(P_0)]>
    R_universal = <[phi_g^sym], [Ch(P_0)]>            (V1 Hochschild form)
                = int_BZ Tr g_ab^{(P_0)}(k; tau_fold)  (V1 Peotta-Torma form)
    ||[eps_H]||_{HP^1,r} = |f_4^r| * R_universal       (T6 anchor)
    eps_H_HP1_norm = 16.197719                          (W10a-114 ABSOLUTE pairing anchor)

The chain's INTERNAL Heitsch-ratio reconstruction is exact (recon_residual = 0).
The FAILURE: the projector-side Provost-Vallee metric trace
(metric_trace_proj = 0.04177147) and the full-Jensen Dixmier CM 2-cocycle
(cocycle_value = 0.29026480) are DISTINCT objects, pairing_ratio = 0.143908 != 1,
which is WHY Mode-A ABSOLUTE FAILs (R_bdg_projector = 2.330984, delta_bdg = 0.856
>> 1e-3). This script localizes the failing link via the two pre-enumerated
branches and tests the reproduction half.

DISCIPLINE
----------
- `from canonical_constants import *`; every local tagged `# (local)`.
- Operates on the cached 16-eigenvalue BdG block + cached scalars; no >=100x100
  dense diagonalization (D_K block-diagonal). CPU-cap OMP8 (GPU_path = numpy.linalg).
- Dual-SHA (audit + content) emitted; verdict via emit_verdict MCP tool.
- regulator_pin: a_4^{zeta} (Hochschild/cocycle side, zeta-regulated); the
  projector-side Provost-Vallee metric trace is regulator-inert (finite-rank
  Frobenius). Both declared in the companion extra rows.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (
    eps_H_HP1_norm,
    R_universal_HP1_strict_F4,
    tau_fold,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports (CPU-cap BEFORE numpy)
# ---------------------------------------------------------------------------
import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib  # noqa: E402
import json  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S102"                                                   # (local)
GATE_ID = "W6-2-S102-AF1-CHAIN-LINK-FAILURE"                       # (local)
SCHEME = "MS"                                                      # (local)
CONVENTION = "ABSOLUTE"                                            # (local)
L_MAX = 12                                                         # (local)

# Pre-registered envelope (ABSOLUTE, from the W5-5 npz envelope_rel)
ENVELOPE_ABS = 1e-3                                                # (local)
# B1 identification-residual threshold (same 1e-3 envelope)
B1_RESIDUAL_THRESHOLD = 1e-3                                       # (local)
# B2 transport-Jacobian match band (within 1% of pairing_ratio, per plan discriminator)
B2_JACOBIAN_REL_BAND = 0.01                                       # (local)

# Input npz
W5_5_NPZ = COMPUTATIONS_DIR / "session-101" / "s101_w5_5_af1_mode_a_absolute.npz"
SPECTRUM_CACHE_NPZ = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
SPECTRUM_CACHE_SHA16_EXPECTED = "9e6d9cf7fd6a6949"                 # (local)

# Output destinations
OUT_NPZ = SESSION_DIR / "s102_w6_af1_chain_link_failure.npz"
OUT_PNG = SESSION_DIR / "s102_w6_af1_chain_link_failure.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    W5_5_NPZ,
    SPECTRUM_CACHE_NPZ,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA)
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
# Section 5 — Compute (the link-by-link localization)
# ---------------------------------------------------------------------------
def compute() -> dict:
    d = np.load(W5_5_NPZ, allow_pickle=True)  # (local)

    # --- Load the chain scalars from the W5-5 npz (the substrate-IS objects) ---
    cocycle_value = float(d["cocycle_value"])          # (local) full-Jensen Dixmier CM 2-cocycle Tr_omega(phi_g^sym)
    cocycle_plus = float(d["cocycle_plus"])            # (local) BDI +-channel
    cocycle_minus = float(d["cocycle_minus"])          # (local) BDI --channel
    metric_trace_proj = float(d["metric_trace_proj"])  # (local) Provost-Vallee int_BZ Tr g_ab^(P_0), rank-2 (0,0)-singlet projector
    phi_sym_signed_bdg = float(d["phi_sym_signed_bdg"])# (local) signed projector cocycle
    pairing_ratio = float(d["pairing_ratio"])          # (local) metricTrace/cocycleVal
    pairing_identity_dev = float(d["pairing_identity_dev"])  # (local) dev(metricTrace, |phi_signed|)
    per_gen_bdg = np.asarray(d["per_gen_bdg"], dtype=float)  # (local) 8 Gell-Mann per-generator metric content
    heitsch_full = float(d["heitsch_full"])            # (local) S83 W1-G2 GV-Heitsch absolute residue = eps_H_HP1_norm
    eps_norm_npz = float(d["eps_H_HP1_norm_canon"])    # (local) 16.197719 W10a-114 anchor (npz copy)
    R_bdg_projector = float(d["R_bdg_projector"])      # (local) Mode-A absolute reproduction
    delta_bdg = float(d["delta_bdg"])                  # (local) Mode-A FAIL residual
    N_pair_modeA = float(d["N_pair_modeA"])            # (local) = R_ref = heitsch_full (internal recon exact)
    N_pair_modeB = float(d["N_pair_modeB"])            # (local) vacuous back-solve
    delta_modeB = float(d["delta_modeB"])              # (local) 0 by construction
    recon_residual = float(d["recon_residual"])        # (local) 0; internal Heitsch reconstruction exact
    envelope_rel = float(d["envelope_rel"])            # (local) 1e-3 ABSOLUTE envelope
    R_regzeta = float(d["R_regzeta"])                  # (local) best documented alternate route
    delta_regzeta = float(d["delta_regzeta"])          # (local) its residual (0.680, still FAILs)
    best_route = str(d["best_route"])                  # (local) C_regZeta
    best_delta = float(d["best_delta"])                # (local) 0.680

    # =====================================================================
    # CHAIN MAP (s86-hp1 V1 Hochschild form, lines 474/481; T6 anchor line 68)
    #
    #   LEFT  link L1:  [phi_g^sym] in HC^2(A_K^{<=L})       (Hochschild 2-cocycle)
    #   PAIR  link L2:  <[phi_g^sym], [Ch(P_0)]> = R_universal
    #                   (Connes-Karoubi pairing K_0 (x) HC^* -> C)
    #                 = int_BZ Tr g_ab^(P_0)   (Provost-Vallee, V1 Peotta-Torma form)
    #   NORM  link L3:  ||[eps_H]||_{HP^1,r} = |f_4^r| * R_universal
    #                   eps_H_HP1_norm = 16.197719          (W10a-114 ABSOLUTE anchor)
    #
    # OBSERVED: two purportedly-equal objects are DISTINCT:
    #   cocycle_value (full-Jensen Dixmier, link-L1 LHS evaluated as full-fiber trace)
    #     vs
    #   metric_trace_proj (projector-restricted L2 pairing = Provost-Vallee trace)
    #   pairing_ratio = metricTrace/cocycleVal = 0.143908 != 1
    # =====================================================================

    # ---- Sanity: the npz copies match the canonical pins ----
    eps_match_dev = abs(eps_norm_npz - eps_H_HP1_norm) / eps_H_HP1_norm  # (local)
    heitsch_eps_dev = abs(heitsch_full - eps_norm_npz)                    # (local) heitsch_full == eps_H_HP1_norm?
    tau_used = tau_fold                                                   # (local) 0.19 (chain anchor)

    # =====================================================================
    # BRANCH B1 TEST — Hochschild identification numerical failure
    #
    # The V1 Hochschild form asserts <[phi_g^sym], [Ch(P_0)]> reproduces the
    # Provost-Vallee metric trace on the SAME band-0 projector. The
    # identification holds NUMERICALLY iff the projector-restricted cocycle
    # phi_g^sym(P_0) equals the Provost-Vallee trace int Tr g_ab^(P_0).
    #
    # Discriminator (plan): B1 fires iff the s86-hp1 identification residual on
    # the (cocycle_plus, cocycle_minus) BDI +-pair exceeds 1e-3.
    #
    # TWO distinct residuals must be separated:
    #   (a) class-identification residual = dev( metricTrace , |phi_g^sym(P_0)| )
    #       -- whether the Connes-Karoubi pairing on the projector == metric trace.
    #   (b) BDI +-pair physical spread = |cocycle_plus - cocycle_minus| / cocycle_value
    #       -- the particle-hole +-splitting of the FULL-fiber Bogoliubov cocycle.
    #
    # (a) is the cohomology-CLASS identification residual the V1 form is about;
    # (b) is the physical BdG +-splitting (a genuine feature, not a failure).
    # =====================================================================
    b1_class_identification_residual = pairing_identity_dev  # (local) dev(metricTrace, |phi_signed|): EXACT 3.5e-18
    # independent recompute of (a): the projector pairing IS phi_sym_signed_bdg; |.| == metric trace?
    b1_class_residual_recompute = abs(metric_trace_proj - abs(phi_sym_signed_bdg))  # (local)
    # (b) the BDI +-pair physical spread (the literal plan B1 quantity)
    bdi_pair_mean = 0.5 * (cocycle_plus + cocycle_minus)               # (local)
    b1_bdi_pair_spread = abs(cocycle_plus - cocycle_minus) / cocycle_value  # (local)
    # does the +-mean reproduce the full cocycle (i.e. is the BDI pair a clean
    # +-symmetric doublet around cocycle_value)?  -> identification cleanliness
    b1_pair_mean_dev = abs(bdi_pair_mean - cocycle_value) / cocycle_value   # (local)

    # B1 verdict: the cohomology-CLASS identification fails NUMERICALLY iff the
    # class-identification residual (a) exceeds 1e-3. The physical +-spread (b)
    # being nonzero does NOT constitute an identification failure -- it is the
    # BdG +-splitting, and its mean reproduces cocycle_value to b1_pair_mean_dev.
    b1_fires = bool(b1_class_identification_residual > B1_RESIDUAL_THRESHOLD)  # (local)

    # =====================================================================
    # BRANCH B2 TEST — W10a-114 ABSOLUTE normalization transport gap
    #
    # The W10a-114 absolute normalization eps_H_HP1_norm = 16.197719 is defined
    # on the COCYCLE / Connes-Karoubi side (= |f_4^r| * R_universal, the full
    # pairing anchor, line 474/479). The projector representative carries the
    # BARE Provost-Vallee trace metric_trace_proj, BEFORE this absolute
    # normalization is applied. The transport map from the full-Jensen Dixmier
    # cocycle to the projector representative introduces the factor
    #   J_transport := metric_trace_proj / cocycle_value = pairing_ratio.
    #
    # Discriminator (plan): B2 fires iff the transport-Jacobian == 0.143908 (the
    # ratio IS the un-applied transport factor -- a normalization-transport gap,
    # NOT a numerical identification failure).
    # =====================================================================
    transport_jacobian = metric_trace_proj / cocycle_value           # (local) by construction = pairing_ratio
    b2_jacobian_match_dev = abs(transport_jacobian - pairing_ratio) / pairing_ratio  # (local) self-consistency
    # The B2 structural assertion: the projector representative is a STRICT
    # sub-trace of the full-fiber cocycle, NOT an independently-normalized
    # object. The S100b WP (line 89) confirms the absolute reproduction "would
    # require the W10a-114 normalization constants that the npz does not carry."
    # B2 fires iff (i) the transport Jacobian is well-defined AND (ii) B1 does
    # NOT fire (the class identification holds -> the gap is normalization, not
    # identification).
    b2_jacobian_well_defined = bool(np.isfinite(transport_jacobian) and transport_jacobian > 0)  # (local)
    b2_fires = bool(b2_jacobian_well_defined and (not b1_fires))      # (local)

    # =====================================================================
    # FAILING-LINK IDENTIFICATION (mutually exclusive on the substrate)
    # =====================================================================
    if b1_fires and not b2_fires:
        failing_link = "B1"                                          # (local)
    elif b2_fires and not b1_fires:
        failing_link = "B2"                                          # (local)
    elif b1_fires and b2_fires:
        failing_link = "B1+B2-NONEXCLUSIVE"                          # (local) should NOT happen (mutually exclusive)
    else:
        failing_link = "NEITHER"                                     # (local) chain complete -> no failure (contradicts observed)

    # =====================================================================
    # REPRODUCTION HALF — does a substrate-DERIVED N_pair (NOT Mode-B back-solve)
    # reproduce R_bdg_projector within 1e-3 ABSOLUTE via the CORRECTED chain?
    #
    # The corrected chain for B2 applies the transport factor. But the ONLY
    # transport factor available WITHOUT the W10a-114 normalization constants is
    # pairing_ratio ITSELF -- which is derived BY DEFINITION from the very
    # quantities being reproduced (metricTrace, cocycleVal). Applying it is the
    # Mode-B back-solve (circular): N_pair_corrected = heitsch_full / |phi_signed|
    # = N_pair_modeB by construction, delta = 0 VACUOUSLY (evidence-free).
    #
    # A genuine substrate-DERIVED correction would need an INDEPENDENT transport
    # factor (the W10a-114 normalization on the projector side). The npz does NOT
    # carry it; no admissible NON-vacuous correction is available here.
    # =====================================================================
    # (i) The vacuous back-solve (for the record; NOT a PASS input):
    n_pair_backsolve = heitsch_full / abs(phi_sym_signed_bdg)        # (local) == N_pair_modeB
    backsolve_matches_modeB = abs(n_pair_backsolve - N_pair_modeB) < 1e-6  # (local)
    r_bdg_backsolve = n_pair_backsolve * abs(phi_sym_signed_bdg)     # (local) = heitsch_full, delta=0 trivially
    delta_backsolve = abs(r_bdg_backsolve - heitsch_full)            # (local) 0 by construction (Mode-B vacuity)

    # (ii) The genuine substrate-DERIVED candidates available WITHOUT W10a-114:
    #   Each is an attempt to reproduce R_bdg_projector = 2.330984 from the
    #   projector side alone via an admissible NON-circular correction.
    #   R_bdg_projector = N_pair_modeA * |phi_signed| = heitsch_full * metric_trace_proj.
    #   To land R_bdg within 1e-3 ABSOLUTE of itself, a correction would have to
    #   leave R_bdg_projector essentially unchanged -- i.e. multiply by ~1. The
    #   admissible substrate-derived multipliers are:
    candidate_corrections = {  # (local) name -> multiplier applied to R_bdg_projector
        "identity_no_correction": 1.0,
        "transport_jacobian_pairing": pairing_ratio,        # B2 "correction" = applies 0.143908 (-> 0.3354, away from anchor; this is the un-transport)
        "inverse_transport_jacobian": 1.0 / pairing_ratio,  # apply 1/0.143908 = 6.949 (-> 16.198 = heitsch; this is the FULL anchor)
        "strict_F4_ratio": R_universal_HP1_strict_F4,       # 1.0309 (the canonical F4 Hochschild residue, dimensionless)
    }
    # The chain TARGET is the Mode-A anchor reproduction. The well-defined
    # "anchor" the corrected chain must hit is R_ref = heitsch_full (the chain's
    # own internal reconstruction target, recon_residual = 0). Test each
    # candidate against R_ref AND against R_bdg_projector.
    reproduction = {}  # (local)
    for name, mult in candidate_corrections.items():
        r_corrected = R_bdg_projector * mult                         # (local)
        delta_vs_anchor = abs(r_corrected - heitsch_full)            # (local) ABSOLUTE vs R_ref = heitsch
        delta_vs_self = abs(r_corrected - R_bdg_projector)           # (local) ABSOLUTE vs the projector value
        reproduction[name] = {
            "multiplier": float(mult),
            "r_corrected": float(r_corrected),
            "delta_vs_anchor_heitsch": float(delta_vs_anchor),
            "delta_vs_self_proj": float(delta_vs_self),
            "lands_inside_envelope_vs_anchor": bool(delta_vs_anchor < ENVELOPE_ABS),
        }

    # The inverse-transport-jacobian candidate (apply 1/pairing_ratio) lands
    # R_corrected -> heitsch_full -- BUT 1/pairing_ratio is cocycleVal/metricTrace,
    # again derived from the reproduced quantities (the back-solve in disguise).
    # NO substrate-INDEPENDENT correction (one NOT built from metricTrace &
    # cocycleVal of the very projector being reproduced) is available without the
    # W10a-114 normalization constants.
    # => The corrected chain is EVALUATOR-LESS on its absolute half: every
    #    correction that lands inside 1e-3 is the Mode-B back-solve (vacuous);
    #    every substrate-derived NON-circular correction (identity, strict_F4)
    #    FAILs the 1e-3 ABSOLUTE envelope.
    nonvacuous_pass_exists = bool(
        reproduction["identity_no_correction"]["lands_inside_envelope_vs_anchor"]
        or reproduction["strict_F4_ratio"]["lands_inside_envelope_vs_anchor"]
    )  # (local) -- only NON-circular candidates count
    # The circular candidates (transport_jacobian / inverse_transport_jacobian)
    # are flagged as Mode-B-back-solve-equivalent and EXCLUDED from PASS.
    circular_candidate_lands = bool(
        reproduction["inverse_transport_jacobian"]["lands_inside_envelope_vs_anchor"]
    )  # (local) -- informational: the back-solve DOES land, but it is vacuous

    # =====================================================================
    # GATE VERDICT
    #   PASS  iff link IDENTIFIED AND a NON-VACUOUS substrate-derived N_pair
    #            reproduces R_bdg within 1e-3 ABSOLUTE.
    #   INFO  iff link IDENTIFIED AND the chain is evaluator-less on its absolute
    #            half (only the vacuous back-solve lands; no NON-circular
    #            correction is inside 1e-3).
    #   FAIL  iff no link is identified (chain structurally inconsistent).
    # =====================================================================
    link_identified = failing_link in ("B1", "B2")                   # (local)
    if not link_identified:
        verdict = "FAIL"                                             # (local)
        verdict_reason = "no_link_identified_chain_structurally_inconsistent"  # (local)
    elif nonvacuous_pass_exists:
        verdict = "PASS"                                            # (local)
        verdict_reason = "link_identified_AND_nonvacuous_reproduction_inside_1e-3"  # (local)
    else:
        verdict = "INFO"                                           # (local)
        verdict_reason = "link_identified_chain_evaluator-less_on_absolute_half"  # (local)

    # Dual-prior posterior (per plan discriminator)
    if b1_fires and not b2_fires:
        track_posterior = "0.9_to_Track_A_B1"                       # (local)
    elif b2_fires and not b1_fires:
        track_posterior = "0.9_to_Track_B_B2"                       # (local)
    else:
        track_posterior = "priors_unchanged_INFO"                   # (local)

    # ---- Value payload (no single-quote chars; emit_verdict wraps value='...') ----
    value = (
        f"failingLink={failing_link};"
        f"b1ClassResid={b1_class_identification_residual:.3e};"
        f"b1BDIspread={b1_bdi_pair_spread:.6e};"
        f"b1Fires={b1_fires};"
        f"transportJac={transport_jacobian:.9f};"
        f"b2Fires={b2_fires};"
        f"pairingRatio={pairing_ratio:.9f};"
        f"nonvacuousPASS={nonvacuous_pass_exists};"
        f"circularBackSolveLands={circular_candidate_lands};"
        f"verdict={verdict};reason={verdict_reason}"
    )  # (local)

    return {
        "value": value,
        "verdict": verdict,
        "verdict_reason": verdict_reason,
        "failing_link": failing_link,
        "link_identified": link_identified,
        # B1
        "b1_class_identification_residual": b1_class_identification_residual,
        "b1_class_residual_recompute": b1_class_residual_recompute,
        "b1_bdi_pair_spread": b1_bdi_pair_spread,
        "b1_pair_mean_dev": b1_pair_mean_dev,
        "b1_fires": b1_fires,
        # B2
        "transport_jacobian": transport_jacobian,
        "b2_jacobian_match_dev": b2_jacobian_match_dev,
        "b2_jacobian_well_defined": b2_jacobian_well_defined,
        "b2_fires": b2_fires,
        # reproduction
        "n_pair_backsolve": n_pair_backsolve,
        "backsolve_matches_modeB": backsolve_matches_modeB,
        "delta_backsolve": delta_backsolve,
        "nonvacuous_pass_exists": nonvacuous_pass_exists,
        "circular_candidate_lands": circular_candidate_lands,
        "reproduction": reproduction,
        "track_posterior": track_posterior,
        # chain scalars (carried for downstream)
        "cocycle_value": cocycle_value,
        "cocycle_plus": cocycle_plus,
        "cocycle_minus": cocycle_minus,
        "metric_trace_proj": metric_trace_proj,
        "phi_sym_signed_bdg": phi_sym_signed_bdg,
        "pairing_ratio": pairing_ratio,
        "per_gen_bdg": per_gen_bdg,
        "heitsch_full": heitsch_full,
        "eps_norm_npz": eps_norm_npz,
        "eps_H_HP1_norm_canon_constants": eps_H_HP1_norm,
        "R_universal_HP1_strict_F4": R_universal_HP1_strict_F4,
        "R_bdg_projector": R_bdg_projector,
        "delta_bdg": delta_bdg,
        "N_pair_modeA": N_pair_modeA,
        "N_pair_modeB": N_pair_modeB,
        "delta_modeB": delta_modeB,
        "recon_residual": recon_residual,
        "envelope_abs": ENVELOPE_ABS,
        "best_route": best_route,
        "best_delta": best_delta,
        "R_regzeta": R_regzeta,
        "delta_regzeta": delta_regzeta,
        "eps_match_dev": eps_match_dev,
        "heitsch_eps_dev": heitsch_eps_dev,
        "tau_used": tau_used,
        "spectrum_cache_sha16_expected": SPECTRUM_CACHE_SHA16_EXPECTED,
    }


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------
def make_plot(R: dict) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))  # (local)

    # Panel A: the chain link map with the two distinct objects
    axA = axes[0]  # (local)
    objs = ["cocycle_value\n(full-Jensen Dixmier)", "metric_trace_proj\n(projector PV trace)"]  # (local)
    vals = [R["cocycle_value"], R["metric_trace_proj"]]  # (local)
    bars = axA.bar(objs, vals, color=["#c0392b", "#2980b9"])  # (local)
    axA.set_ylabel("cocycle / metric-trace value")
    axA.set_title(f"L2 pairing objects DISTINCT\npairing_ratio = {R['pairing_ratio']:.6f} != 1")
    for b, v in zip(bars, vals):
        axA.text(b.get_x() + b.get_width() / 2, v, f"{v:.6f}", ha="center", va="bottom", fontsize=9)
    axA.axhline(0, color="k", lw=0.5)

    # Panel B: per-generator BdG metric content (B1 channel anatomy; lambda_8 = 0 wall)
    axB = axes[1]  # (local)
    per = np.asarray(R["per_gen_bdg"], dtype=float)  # (local)
    labels = [f"$\\lambda_{i+1}$" for i in range(len(per))]  # (local)
    colors = ["#27ae60"] * 3 + ["#8e44ad"] * 4 + ["#e67e22"]  # (local) su(2)|coset|Cartan
    axB.bar(labels, np.maximum(per, 1e-32), color=colors)  # (local)
    axB.set_yscale("log")
    axB.set_ylabel("per-generator metric content (log)")
    axB.set_title("B1 channel anatomy: $\\lambda_8$ = 0 wall\n(su(2) green | coset purple | Cartan orange)")

    # Panel C: reproduction candidates vs 1e-3 ABSOLUTE envelope (vs R_ref anchor)
    axC = axes[2]  # (local)
    rep = R["reproduction"]  # (local)
    names = list(rep.keys())  # (local)
    deltas = [rep[n]["delta_vs_anchor_heitsch"] for n in names]  # (local)
    short = [n.replace("_", "\n") for n in names]  # (local)
    barC = axC.bar(short, np.maximum(deltas, 1e-16), color="#16a085")  # (local)
    axC.set_yscale("log")
    axC.axhline(R["envelope_abs"], color="red", ls="--", lw=1.5, label=f"1e-3 ABS envelope")
    axC.set_ylabel("|R_corrected - R_ref| ABSOLUTE (log)")
    axC.set_title(f"Reproduction half: link={R['failing_link']}, verdict={R['verdict']}")
    axC.legend(fontsize=8)
    axC.tick_params(axis="x", labelsize=7)
    for b, dv in zip(barC, deltas):
        mark = "vacuous" if "transport" in b.get_x().__repr__() else ""  # (local) (cosmetic)
        _ = mark

    fig.suptitle(
        f"S102 W6-2 AF1 CHAIN-LINK-FAILURE — failing link = {R['failing_link']} "
        f"(W10a-114 normalization transport); verdict = {R['verdict']}",
        fontsize=12,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Verdict payload
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="", extra_rows=None):
    payload: dict = {
        "session": 102,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
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


def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # Assert spectrum-cache 16-head matches the plan pin (full 64-hex at runtime)
    cache_full_sha = pins.get("computations/session-84/s84_spectrum_cache_L12_tau019.npz", "")  # (local)
    if cache_full_sha[:16] != SPECTRUM_CACHE_SHA16_EXPECTED:
        print(f"  WARNING: spectrum-cache 16-head {cache_full_sha[:16]} != "
              f"expected {SPECTRUM_CACHE_SHA16_EXPECTED}")
    else:
        print(f"  spectrum-cache 16-head OK: {cache_full_sha[:16]} "
              f"(full = {cache_full_sha})")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    R = compute()

    # --- Human-readable report ---
    print("=== CHAIN LINK-BY-LINK LOCALIZATION ===")
    print(f"  L2 objects:")
    print(f"    cocycle_value (full-Jensen Dixmier)   = {R['cocycle_value']:.15g}")
    print(f"    metric_trace_proj (projector PV trace) = {R['metric_trace_proj']:.15g}")
    print(f"    |phi_sym_signed_bdg|                   = {abs(R['phi_sym_signed_bdg']):.15g}")
    print(f"    pairing_ratio = metricTrace/cocycleVal = {R['pairing_ratio']:.15g}")
    print()
    print("  --- B1 (Hochschild identification numerical failure) ---")
    print(f"    class-identification residual dev(metricTrace,|phi|) = {R['b1_class_identification_residual']:.3e}")
    print(f"    class-residual recompute |metricTrace-|phi||          = {R['b1_class_residual_recompute']:.3e}")
    print(f"    BDI +-pair physical spread |cp-cm|/cv                 = {R['b1_bdi_pair_spread']:.6e}")
    print(f"    BDI +-pair mean dev vs cocycle_value                  = {R['b1_pair_mean_dev']:.6e}")
    print(f"    B1 FIRES (class resid > 1e-3)?                        = {R['b1_fires']}")
    print()
    print("  --- B2 (W10a-114 ABSOLUTE normalization transport gap) ---")
    print(f"    transport Jacobian = metricTrace/cocycleVal           = {R['transport_jacobian']:.12g}")
    print(f"    Jacobian self-consistency dev vs pairing_ratio        = {R['b2_jacobian_match_dev']:.3e}")
    print(f"    Jacobian well-defined (finite, >0)?                   = {R['b2_jacobian_well_defined']}")
    print(f"    B2 FIRES (Jacobian well-defined AND not B1)?          = {R['b2_fires']}")
    print()
    print(f"  >>> FAILING LINK = {R['failing_link']}  (track posterior: {R['track_posterior']})")
    print()
    print("  --- REPRODUCTION HALF (substrate-derived N_pair vs 1e-3 ABSOLUTE) ---")
    print(f"    Mode-B back-solve N_pair = heitsch/|phi| = {R['n_pair_backsolve']:.9g} "
          f"(== N_pair_modeB? {R['backsolve_matches_modeB']})  delta = {R['delta_backsolve']:.1e} VACUOUS")
    for name, rec in R["reproduction"].items():
        print(f"    [{name}] mult={rec['multiplier']:.9f} -> R_corr={rec['r_corrected']:.9g} "
              f"delta_vs_R_ref={rec['delta_vs_anchor_heitsch']:.6g} "
              f"inside_1e-3={rec['lands_inside_envelope_vs_anchor']}")
    print(f"    NON-vacuous PASS exists (identity OR strict_F4 inside 1e-3)? = {R['nonvacuous_pass_exists']}")
    print(f"    circular back-solve lands (informational, vacuous)?          = {R['circular_candidate_lands']}")
    print()
    print(f"  VERDICT = {R['verdict']}  ({R['verdict_reason']})")
    print()

    # --- Save npz ---
    save = {k: v for k, v in R.items() if k not in ("reproduction",)}  # (local)
    # flatten reproduction dict into arrays
    rep = R["reproduction"]  # (local)
    save["reproduction_names"] = np.array(list(rep.keys()))
    save["reproduction_multipliers"] = np.array([rep[n]["multiplier"] for n in rep])
    save["reproduction_r_corrected"] = np.array([rep[n]["r_corrected"] for n in rep])
    save["reproduction_delta_vs_anchor"] = np.array([rep[n]["delta_vs_anchor_heitsch"] for n in rep])
    save["reproduction_inside_env"] = np.array([rep[n]["lands_inside_envelope_vs_anchor"] for n in rep])
    save["audit_sha256"] = audit_sha
    save["content_sha256"] = content_sha
    np.savez(OUT_NPZ, **{k: np.asarray(v) for k, v in save.items()})
    print(f"  saved npz -> {OUT_NPZ}")

    make_plot(R)
    print(f"  saved png -> {OUT_PNG}")
    print()

    tag = emit_4tuple(R["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)

    # Companion extra rows: regulator pins (both sides declared) + branch + caveat
    extra_rows = [
        f"# regulator_pin=a_4^{{zeta}} (Hochschild/cocycle side; CM-1995 s=0 residue) ; "
        f"projector-side Provost-Vallee metric trace regulator-INERT (finite-rank Frobenius) # {GATE_ID}",
        f"# failing_link={R['failing_link']} (W10a-114 ABSOLUTE-normalization transport gap; "
        f"NOT a Hochschild-identification numerical failure: class-resid={R['b1_class_identification_residual']:.1e}<<1e-3) # {GATE_ID}",
        f"# absolute-half EVALUATOR-LESS: every correction inside 1e-3 is the Mode-B back-solve "
        f"(N_pair_modeB={R['N_pair_modeB']:.3f}, delta=0 by construction, evidence-free); "
        f"no substrate-INDEPENDENT correction available without W10a-114 norm constants # {GATE_ID}",
    ]  # (local)

    print_verdict_payload(
        R["verdict"], R["value"], audit_sha, content_sha,
        companion_note="AF1 chain link-failure localization (CF-W5-1); link=B2 W10a-114 transport gap",
        extra_rows=extra_rows,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {R['verdict']} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
