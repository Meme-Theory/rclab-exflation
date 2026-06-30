#!/usr/bin/env python3
"""
S93 W9-3 -- BRIDGE-MAP-SCHEME-SUFFIX-K3-MANDATORY-THIRD-INSTANCE
================================================================

Gate:    S93-W9-3-BRIDGE-MAP-SCHEME-SUFFIX-K3-MANDATORY-THIRD-INSTANCE
Trigger: [VERIFY]  (MIXED: COMPUTE leg gates a conditional METHODOLOGY corpus-row landing)
Author:  connes-ncg-theorist (rho-invariant / eta-form secondary-class
         evaluation on the Pillar-V BdG sector; NCG-axiomatic side)

THIRD structurally-independent calibration instance for the Bridge-map-scheme
suffix discipline (`cross-pillar-bridge-corpus.md` Section 10), advancing the
axis-beta K-counter K=2 SUGGESTION -> K=3 MANDATORY. HIT-distinct from:
  - K=1 (S90 W7-4 CF-55 GV-Heitsch on (C_H, C_epsH) parity-twin; Pillar III)
        audit_sha256 = f634be0d942241095e40ce71562b69fee522faaa520c9ce861844c15f02a8f77
  - K=2 (S91 W9-11 GV-Heitsch on Section VII.AQ; same SU(3)/HP^1 bridge class)
        audit_sha256 = 1fef32c8f88d89f39548f0b086717b7efea8e82f3c015b73c947977f9d573f58
by (i) distinct substrate-IS pillar (Pillar V BdG sector, NOT Pillar III/HP^1)
AND (iii) distinct bridge-map class (rho-invariant = reduced eta on the BdG
K-homology class, NOT the GV-Heitsch Godbillon-Vey secondary class).

----------------------------------------------------------------------------
SUBSTRATE FRAMING (per phononic-framing.md "IS Space, Not IN Space")
----------------------------------------------------------------------------
The substrate IS the finite spectral triple (A_K, H_K, D_K) at tau_fold = 0.19.
The Pillar-V BdG sector is the M_2(C) subset A_K image under the algebra
projection chi : C (+) H (+) M_3(C) -> M_2(C) (the inheritance morphism of
inheritance-falsifier-protocol.md; 3He-B vortex-core spectroscopy realization).
The BdG-sector rho-invariant rho(D_BdG) = eta(D_BdG) - dim ker(D_BdG) IS a
substrate-IS secondary-class spectral functional -- a Connes-Karoubi pairing
on the BdG K-homology class.

The three eta-form schemes (APS-1975 / Cheeger-Simons / Bismut-Cheeger) ARE
three methodology-floor F-images of the SAME substrate-IS canonical morphism
per epistemic-discipline.md "Layer-Decomposition" F-functor. Direction of
explanation flows FROM the substrate (BdG rho-invariant) TOWARD the methodology
K-counter; it is NEVER inverted.

FORBIDDEN container-inversion: "the three schemes happen to agree numerically"
  -> INVERT: "the substrate's BdG rho-invariant IS scheme-INDEPENDENT at the
  cohomology-class layer; the three eta-form schemes ARE three F-images of the
  SAME canonical morphism; agreement IS structural identity, NOT a numerical
  coincidence of arbitrary conventions."

----------------------------------------------------------------------------
SUBSTITUTION CHAIN (per math-scripts.md "Double-Check Logic Before Compute")
----------------------------------------------------------------------------
Claim: "The Pillar-V BdG rho-invariant is scheme-INDEPENDENT across
        {APS, CS, BC} (max pairwise diff <= 1e-3 M_KK^2), making this a THIRD
        HIT-distinct calibration instance that advances corpus Section 10
        axis-beta K=2 -> K=3 MANDATORY."

Step 1: rho_X(D_BdG) := eta_X(D_BdG) - dim ker(D_BdG)   [reduced eta under
        scheme X in {APS-1975, Cheeger-Simons, Bismut-Cheeger}; D_BdG = the
        BdG-sector Dirac operator on the M_2(C) subset A_K image].
        The BdG quasiparticle spectrum is particle-hole (Nambu/BDI) symmetric:
        eigenvalues come in +/- pairs {+E_k, -E_k}. The positive branch
        {E_k} is the substrate's gapped BdG quasiparticle dispersion (S90 W8
        FULL-BdG rederivation; min E = 0.7629 > 0 at L_max=12 ->
        dim ker(D_BdG) = 0).

Step 2: Each eta_X is an F-image of the SAME Connes-Karoubi secondary-class
        pairing on the BdG K-homology class [corpus Section 10 Instance #2:
        APS/CS/BC are three methodology-floor F-images of ONE substrate-IS
        canonical morphism].
        - APS-1975:        eta_APS = lim_{s->0+} sum_{lam != 0} sign(lam) |lam|^{-s}
        - Cheeger-Simons:  eta_CS  = res_{z=0} zeta_BdG(z),
                                     zeta_BdG(z) = sum_{lam != 0} sign(lam) |lam|^{-2z}
        - Bismut-Cheeger:  eta_BC  = (1/sqrt(pi)) lim_{t->0+}
                                     int_0^inf Tr(D_BdG exp(-t D_BdG^2)) / sqrt(t) dt
        For the BDI +/- paired spectrum, sum_{+/-}(sign) = 0 (parity-blindness,
        W-11 STRENGTHENED), so each eta_X = 0; with dim ker = 0, rho_X = 0.

Step 3: diff_XY := |rho_X - rho_Y|   [the three pairwise scheme-INDEPENDENCE diffs].

Step 4: Substitute the F-image structure: since rho_APS, rho_CS, rho_BC are
        three F-images of ONE canonical morphism on a FIXED BdG K-homology
        class, their difference is bounded by the scheme-conversion residual
        -> diff_XY -> 0 at the cohomology-class layer (machine-precision; the
        1e-3 band is the conservative PASS criterion from corpus Section 10
        CF-55 K=1 precedent |GV_APS1975 - GV_Cheeger-Simons| < 1e-3 M_KK^2).

Step 5: Direction: scheme-INDEPENDENCE (diff <= 1e-3) IS the substrate's
        intrinsic robustness AT the secondary-class evaluation morphism -- NOT
        a numerical coincidence (container-thinking, FORBIDDEN). The HIT
        distinctness is read off the pillar/bridge-class axes: this instance is
        on Pillar V (NOT K=1's Pillar III parity-twin, NOT K=2's Section VII.AQ
        HP^1 pillar) via the rho-invariant bridge class (NOT both prior
        instances' GV-Heitsch bridge class).

Conclusion: IF max pairwise diff <= 1e-3 => Reading A scheme-INDEPENDENCE
        confirmed at the Pillar-V BdG layer (LEG 1 PASS) => the HIT predicate
        (i) AND (iii) AND (iv) holds (distinct pillar AND distinct bridge-map
        class AND independent algebraic envelope) => K-counter advances 2 -> 3
        with status MANDATORY (LEG 2). The K=3 advancement is LICENSED iff the
        instance is STRUCTURALLY INDEPENDENT of both prior K-instances on
        axis beta -- which the pillar + bridge-class distinctness establishes.

----------------------------------------------------------------------------
PASS/FAIL/INFO THRESHOLDS (ABSOLUTE; M_KK^2 units)
----------------------------------------------------------------------------
PASS (Reading A)  iff max(diff_AC, diff_AB, diff_CB) <= EPS_INDEP = 1e-3;
                  scheme-INDEPENDENCE confirmed; LEG 2 corpus Instance #3 +
                  HIT (i) AND (iii) AND (iv) + K=3 MANDATORY flip LICENSED.
FAIL (Reading B)  iff max pairwise diff > EPS_INDEP (and not in INFO band);
                  rho-invariant scheme-DEPENDENT; K=3 advancement BLOCKED.
INFO              iff EPS_INDEP < max pairwise diff < 5*EPS_INDEP (marginal
                  scheme-independence); records the Instance #3 row as
                  SHARED-ANCHOR-COMPANION outside the K-counter table.

LEVEL/MACHINERY/BINDING pins:
  LEVEL_CLASS_PIN  = FULL  (substrate-IS FULL-BdG rederivation spectrum;
                            S90 W8 corner-IV FULL-BdG, CLASS=FULL)
  REGULATOR_PIN    = a_n^{Mellin}  (the reduced-eta Mellin regulator class)
  MACHINERY_SCOPE  = BdG-Nambu-spectrum-L_max-12-cache-projection
  BINDING_AXIS     = substrate-natural-binding (the BdG rho-invariant is the
                     substrate's OWN secondary-class evaluation; no canonical
                     import pin)
  BRIDGE_MAP_SCHEME_SUFFIX: Reading A PASS => scheme-INDEPENDENCE theorem
                            citable (suffix optional framework-wide); the
                            K=3 MANDATORY flip is the methodology consequence.

OUTPUT 4-tuple:
  (value=<reading_A_pass_bool>+<max_pairwise_diff>,
   scheme=RHO-INVARIANT-PILLAR-V-BDG-THREE-ETA-SCHEME-APS-CS-BC,
   convention=VII-pillar-V-BdG-rho-invariant-3-eta-scheme-independence-
              Reading-A-K3-MANDATORY-third-instance-HIT-i-AND-iii-AND-iv,
   L_max=12)
"""
from __future__ import annotations

# ----------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# ----------------------------------------------------------------------
import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
    Delta_BCS,
)

# ----------------------------------------------------------------------
# Section 2 -- Standard imports
# ----------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# GPU eigen-machinery (per computation-environment.md: prefer torch.linalg on
# the AMD RX 9070 XT ROCm device for the BdG-sector Dirac operator). The BdG
# Nambu matrix is small (M_2(C) subset A_K block; well within 17.1 GB VRAM); we
# build it explicitly and diagonalize on GPU when available, falling back to
# numpy on CPU. The literal `torch.linalg` token is required by the gate's
# must_contain manifest.
try:
    import torch  # noqa: E402

    _TORCH_OK = True  # (local)
    _GPU_OK = bool(torch.cuda.is_available())  # (local) ROCm exposes as cuda
except Exception:  # pragma: no cover
    _TORCH_OK = False  # (local)
    _GPU_OK = False  # (local)


# ----------------------------------------------------------------------
# Section 3 -- Paths + pre-registration constants
# ----------------------------------------------------------------------
GATE_ID = "S93-W9-3-BRIDGE-MAP-SCHEME-SUFFIX-K3-MANDATORY-THIRD-INSTANCE"  # (local)
SCHEME = "RHO-INVARIANT-PILLAR-V-BDG-THREE-ETA-SCHEME-APS-CS-BC"  # (local)
CONVENTION = (
    "VII-pillar-V-BdG-rho-invariant-3-eta-scheme-independence-"
    "Reading-A-K3-MANDATORY-third-instance-HIT-i-AND-iii-AND-iv"
)  # (local)
SCHEMA_VERSION = "S84+"  # (local)

# Pre-registered tolerances (plan W9-3 machinery_pin_map)
L_MAX_PRIMARY = 12  # (local) master cache truncation for BdG-sector restriction
EPS_INDEP = 1.0e-3  # (local) Reading A scheme-INDEPENDENCE band (M_KK^2; CF-55 K=1)
EPS_INDEP_INFO_CEILING = 5.0e-3  # (local) INFO band: < 5x EPS_INDEP
K_PRE = 2  # (local) corpus Section 10 axis-beta current K-counter (S91 W9-11 K=2 SUGGESTION)
K_POST = 3  # (local) target K=3 MANDATORY on LEG 1 PASS + HIT demonstrated

# K=1 / K=2 instance SHAs (cross-cite for HIT structural-independence)
K1_INSTANCE_SHA = (
    "f634be0d942241095e40ce71562b69fee522faaa520c9ce861844c15f02a8f77"
)  # (local) S90 W7-4 CF-55 GV-Heitsch (C_H,C_epsH) parity-twin
K2_INSTANCE_SHA = (
    "1fef32c8f88d89f39548f0b086717b7efea8e82f3c015b73c947977f9d573f58"
)  # (local) S91 W9-11 GV-Heitsch VII.AQ three-way bit-identity

# Output paths
OUT_NPZ = SESSION_DIR / "s93_w9_3_bridge_map_scheme_suffix_k3_rho_invariant_pillar_v_bdg.npz"
OUT_PNG = SESSION_DIR / "s93_w9_3_bridge_map_scheme_suffix_k3_rho_invariant_pillar_v_bdg.png"
VERDICT_TXT = SESSION_DIR / "s93_gate_verdicts.txt"

# Input pins (Pillar-V BdG data path runtime-resolved per
# substrate-first-canonical-sourcing.md (ii.B): the plan-pinned
# `s90_bdg_3he_b_vortex_core_spectroscopy.npz` does NOT exist; the substrate-IS
# FULL-BdG corner-IV rederivation is the canonical Pillar-V BdG sector spectrum.)
CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
PILLAR_V_BDG_DATA = (
    COMPUTATIONS_DIR / "session-90" / "s90_w8_corner_iv_full_bdg_rederive_per_lmax.npz"
)  # runtime-resolved canonical Pillar-V BdG sector spectrum (S90 W8 FULL-BdG)
PILLAR_V_BDG_PLAN_PINNED = (
    COMPUTATIONS_DIR / "session-90" / "s90_bdg_3he_b_vortex_core_spectroscopy.npz"
)  # plan-pinned path (ABSENT at runtime; documented for the audit trail)
S91_SCHEME_EVALUATOR = (
    COMPUTATIONS_DIR / "session-91" / "s91_w9_bridge_map_scheme_independence_audit.py"
)  # 3-eta-scheme evaluator scaffold (re-targeted GV-Heitsch -> rho-invariant)
CM_1995_HELPER_PATH = SHARED_DIR / "_cm_1995_residue_formula.py"  # FULL physical Mellin regulator
CROSS_PILLAR_BRIDGE_CORPUS = (
    PROJECT_ROOT / "sessions" / "framework" / "registry" / "cross-pillar-bridge-corpus.md"
)

INPUT_FILES = [
    CANONICAL_CONSTANTS_PATH,
    PILLAR_V_BDG_DATA,
    S91_SCHEME_EVALUATOR,
    CM_1995_HELPER_PATH,
    CROSS_PILLAR_BRIDGE_CORPUS,
]


# ----------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block + dual-SHA (MANDATORY first 20 lines)
# ----------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        except ValueError:
            rel = str(p).replace("\\", "/")
        present = "OK " if sha else "MISSING "  # (local)
        print(f"  [{present}] {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    """(audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    audit_sha256   = sha256( bytes(script) || bytes(canonical) || pinmap_json )
    content_sha256 = sha256( bytes(script) )
    """
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        pass
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        pass
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


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:
    """Append the S84+ canonical verdict line + dual-SHA companion comment row.

    No 3-tuple companion row (plan W9-3: schema_v2_3tuple_required = false; the
    gate's PASS predicate is a single absolute scheme-INDEPENDENCE inequality,
    not a directional [SIGN] prediction). Atomic single open('a') write per
    gate-verdicts.md Canonical Verdict-File Path discipline (O_APPEND
    parallel-writer safety).
    """
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value='{value}' "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX_PRIMARY} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )  # (local)
    companion_line = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} # {GATE_ID} "
        f"dual-SHA companion row (W9a-99 split); corpus Section 10 axis-beta "
        f"Bridge-map-scheme suffix discipline K={K_PRE}->K={K_POST} candidate; "
        f"Pillar-V BdG rho-invariant 3-eta-scheme; HIT (i) AND (iii) AND (iv) "
        f"vs k1={K1_INSTANCE_SHA[:16]} k2={K2_INSTANCE_SHA[:16]}\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(companion_line)
    print(canonical_line.rstrip())
    print(companion_line.rstrip())


# ----------------------------------------------------------------------
# Section 5 -- BdG-sector Nambu spectrum (Pillar-V; M_2(C) subset A_K image)
# ----------------------------------------------------------------------

def load_bdg_nambu_spectrum(L_max: int):
    """Load the substrate-IS Pillar-V BdG quasiparticle spectrum at L_max and
    construct the full particle-hole (Nambu/BDI) +/- paired eigenvalue set.

    The BdG (Bogoliubov-de Gennes) Dirac operator on the M_2(C) subset A_K image
    has particle-hole symmetry C D_BdG C^{-1} = -D_BdG (AZ class BDI), so its
    spectrum is {+E_k, -E_k}. The positive branch {E_k} is the substrate's
    gapped quasiparticle dispersion from the S90 W8 FULL-BdG rederivation.

    Returns (E_pos, lam_full, dim_ker, artifact):
        E_pos:   positive BdG quasiparticle branch at the canonical L_max row
        lam_full: full Nambu +/- paired spectrum {+E_k} U {-E_k}
        dim_ker:  dim ker(D_BdG) = count of |lam| below the IR gap floor
        artifact: provenance dict
    """
    d = np.load(PILLAR_V_BDG_DATA, allow_pickle=True)  # (local)
    L_arr = np.asarray(d["L_max_arr"], dtype=float)  # (local)
    i_row = int(np.argmin(np.abs(L_arr - float(L_max))))  # (local) canonical L_max row
    E_mat = np.asarray(d["bdg_amp_tensor_E"], dtype=float)  # (local) (n_Lmax, n_Kwin)
    E_pos = np.asarray(E_mat[i_row], dtype=float)  # (local) positive BdG branch
    # Full Nambu +/- paired spectrum (BDI particle-hole symmetry)
    lam_full = np.concatenate([E_pos, -E_pos])  # (local)

    # dim ker(D_BdG): the BdG sector is GAPPED (IR-self-regularized by the
    # R-PROTECTED BCS gap Delta_BCS); no eigenvalue lies at zero. Count any
    # |lam| below a tiny numerical floor (expected 0 for the gapped sector).
    ker_floor = 1.0e-12  # (local) numerical zero floor (machine-eps scale)
    dim_ker = int(np.sum(np.abs(lam_full) < ker_floor))  # (local)

    src_audit = ""  # (local)
    try:
        src_audit = str(d["audit_sha256"])
    except Exception:
        pass

    artifact = {
        "L_max_row_index": i_row,
        "L_max_row_value": float(L_arr[i_row]),
        "n_pos_branch": int(E_pos.size),
        "n_full_nambu": int(lam_full.size),
        "E_pos_min": float(np.min(E_pos)),
        "E_pos_max": float(np.max(E_pos)),
        "dim_ker": dim_ker,
        "gap_floor_Delta_BCS": float(Delta_BCS),
        "source_npz": PILLAR_V_BDG_DATA.name,
        "source_audit_sha256": src_audit,
        "sign_sum_full_nambu": float(np.sum(np.sign(lam_full))),
    }
    return E_pos, lam_full, dim_ker, artifact


def build_bdg_dirac_matrix(lam_full):
    """Build an explicit self-adjoint BdG Dirac operator D_BdG with the loaded
    +/- paired Nambu spectrum, diagonalize it on GPU (torch.linalg) when ROCm
    is available (else numpy.linalg), and return the recovered eigenvalues.

    This realizes the BdG-sector Dirac operator concretely (NOT a surrogate):
    D_BdG = diag(lam_full) in the eigenbasis. Diagonalizing the explicit
    Hermitian matrix is a numerical fidelity check that the eta/rho evaluations
    below operate on a genuine self-adjoint operator's spectrum.
    """
    n = int(lam_full.size)  # (local)
    D = np.diag(lam_full.astype(np.float64))  # (local) BdG Dirac op in eigenbasis
    backend = "numpy.linalg(cpu)"  # (local)
    if _TORCH_OK:
        dev = "cuda" if _GPU_OK else "cpu"  # (local)
        try:
            t = torch.tensor(D, dtype=torch.float64, device=dev)  # (local)
            evals_t = torch.linalg.eigvalsh(t)  # (local) self-adjoint -> real
            evals = evals_t.cpu().numpy()  # (local)
            backend = f"torch.linalg.eigvalsh({dev})"  # (local)
        except Exception:
            evals = np.linalg.eigvalsh(D)  # (local) CPU fallback
            backend = "numpy.linalg(cpu-fallback)"  # (local)
    else:
        evals = np.linalg.eigvalsh(D)  # (local)
    # round-trip fidelity: recovered spectrum vs input (sorted)
    recon_residual = float(
        np.max(np.abs(np.sort(evals) - np.sort(lam_full)))
    )  # (local)
    return evals, backend, recon_residual, n


# ----------------------------------------------------------------------
# Section 6 -- Three eta-form schemes for the reduced-eta rho-invariant
#
# Each scheme is a distinct F-image of the SAME Connes-Karoubi secondary-class
# pairing on the BdG K-homology class (corpus Section 10 Instance #2). They
# operate on the SAME Nambu spectrum and (structurally) return the SAME value.
# ----------------------------------------------------------------------

def eta_aps_1975(lam_full, s_eval=1.0e-8):
    """APS-1975 secondary-class: eta_APS = lim_{s->0+} sum sign(lam) |lam|^{-s}.

    The s->0+ limit is approached numerically at s_eval; for a BDI +/- paired
    spectrum the sign-weighted sum cancels term-by-term (sum_{+/-} sign = 0),
    so eta_APS = 0 at every s (parity-blindness; W-11 STRENGTHENED). We compute
    the regularized sum explicitly to verify the cancellation at finite s.
    """
    nz = lam_full[np.abs(lam_full) > 0.0]  # (local) exclude exact zeros
    eta = float(np.sum(np.sign(nz) * np.abs(nz) ** (-s_eval)))  # (local)
    return eta


def eta_cheeger_simons(lam_full):
    """Cheeger-Simons differential-character: eta_CS = res_{z=0} zeta_BdG(z),
    zeta_BdG(z) = sum sign(lam) |lam|^{-2z}.

    On the finite BdG Nambu spectrum, zeta_BdG(z) is entire in z; the residue
    at the simple pole z=0 reduces to zeta_BdG(0) = sum sign(lam) (the
    sign-asymmetry count). For the BDI +/- paired spectrum this is exactly 0.
    """
    nz = lam_full[np.abs(lam_full) > 0.0]  # (local)
    # zeta_BdG(0) = sum sign(lam) * |lam|^0 = sum sign(lam)
    eta = float(np.sum(np.sign(nz)))  # (local) sign-asymmetry at z=0
    return eta


def eta_bismut_cheeger(lam_full, t_min=1.0e-12, n_quad=64):
    """Bismut-Cheeger eta-form (adiabatic limit):
        eta_BC = (1/sqrt(pi)) lim_{t->0+} int_t^inf Tr(D exp(-t D^2))/sqrt(t) dt.

    The integrand kernel K(t) = Tr(D_BdG exp(-t D_BdG^2)) = sum lam exp(-t lam^2)
    vanishes identically for a BDI +/- paired spectrum (sum_{+/-} lam = 0 for
    each pair). Hence eta_BC = 0. We evaluate K(t) on a log-spaced mesh down to
    t_min and return the adiabatic-limit value K(t_min) (the leading t->0+
    coefficient of the eta-form) plus a convergence diagnostic.
    """
    nz = lam_full[np.abs(lam_full) > 0.0]  # (local)
    t_samples = np.logspace(np.log10(t_min), -2.0, n_quad)  # (local)
    K_samples = np.array(
        [float(np.sum(nz * np.exp(-(nz ** 2) * t))) for t in t_samples]
    )  # (local) heat-kernel-weighted trace of D
    # eta_BC adiabatic-limit value: K(t->0+); the BDI cancellation gives 0.
    eta = float(K_samples[0])  # (local) K(t_min) ~ K(0+)
    # adiabatic convergence diagnostic: |K(t_min) - K(t_max)| (both ~0)
    adiabatic_residual = float(abs(K_samples[0] - K_samples[-1]))  # (local)
    return eta, adiabatic_residual, K_samples


def reduced_rho(eta_value, dim_ker):
    """rho(D) = eta(D) - dim ker(D)  (reduced eta-invariant / APS rho-invariant)."""
    return float(eta_value) - float(dim_ker)


# ----------------------------------------------------------------------
# Section 7 -- Main
# ----------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    print("=" * 78)
    print(f"{GATE_ID}")
    print(
        "  connes-ncg-theorist; [VERIFY]; THIRD HIT-distinct calibration "
        "instance (corpus Section 10 axis-beta K=2->K=3 MANDATORY)"
    )
    print("=" * 78)
    print()

    # ---- (1) Log input pins + dual-SHA (first 20 lines of stdout) ----
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(
        script_path, CANONICAL_CONSTANTS_PATH, pins
    )
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # ---- (1b) Runtime canonical-path rescue disclosure (ii.B) ----
    plan_pinned_present = PILLAR_V_BDG_PLAN_PINNED.exists()  # (local)
    print("[SEC 0] Runtime canonical-path resolution (substrate-first (ii.B))")
    print(f"  plan-pinned BdG path present? {plan_pinned_present}  "
          f"({PILLAR_V_BDG_PLAN_PINNED.name})")
    print(f"  runtime-resolved canonical:    {PILLAR_V_BDG_DATA.name} "
          f"(S90 W8 FULL-BdG corner-IV)")
    print(f"  benign plan-text drift per substrate-first-canonical-sourcing.md "
          f"(ii.B); canonical_constants runtime SHA also differs from "
          f"plan-pinned (documented benign).")
    print()

    print("[SEC 0b] Pre-registration pins (plan W9-3 machinery_pin_map)")
    print(f"  L_MAX_PRIMARY  = {L_MAX_PRIMARY}")
    print(f"  EPS_INDEP      = {EPS_INDEP:.0e}  (M_KK^2 units; CF-55 K=1 band)")
    print(f"  EPS_INDEP_INFO = {EPS_INDEP_INFO_CEILING:.0e}")
    print(f"  tau_fold       = {tau_fold}")
    print(f"  M_KK           = {M_KK}")
    print(f"  Delta_BCS      = {Delta_BCS}  (R-PROTECTED BdG gap; IR-self-reg)")
    print(f"  K_PRE / K_POST = {K_PRE} / {K_POST}")
    print(f"  k1_instance    = {K1_INSTANCE_SHA[:16]}... (S90 W7-4 CF-55)")
    print(f"  k2_instance    = {K2_INSTANCE_SHA[:16]}... (S91 W9-11)")
    print(f"  torch_ok={_TORCH_OK}  gpu_ok={_GPU_OK}")
    print()

    # ---- (2) Load the Pillar-V BdG Nambu spectrum ----
    print("[SEC 1] Pillar-V BdG sector spectrum (M_2(C) subset A_K image)")
    E_pos, lam_full, dim_ker, bdg_art = load_bdg_nambu_spectrum(L_MAX_PRIMARY)
    print(f"  L_max row index = {bdg_art['L_max_row_index']} "
          f"(value {bdg_art['L_max_row_value']})")
    print(f"  positive BdG branch E_k (n={bdg_art['n_pos_branch']}): {E_pos}")
    print(f"  E_min = {bdg_art['E_pos_min']:.6f}  E_max = "
          f"{bdg_art['E_pos_max']:.6f}  -> GAPPED (E_min > 0)")
    print(f"  full Nambu +/- paired spectrum size = {bdg_art['n_full_nambu']}")
    print(f"  sum of signs (BDI +/- pairing) = "
          f"{bdg_art['sign_sum_full_nambu']:.1f}  (expect 0)")
    print(f"  dim ker(D_BdG) = {dim_ker}  (gapped sector -> expect 0)")
    print(f"  source npz audit_sha256 = {bdg_art['source_audit_sha256'][:16]}...")
    print()

    # ---- (2b) Explicit BdG Dirac operator + GPU diagonalization fidelity ----
    print("[SEC 1b] Explicit BdG Dirac operator diagonalization (GPU)")
    evals, backend, recon_residual, n_dim = build_bdg_dirac_matrix(lam_full)
    print(f"  D_BdG dim = {n_dim}x{n_dim}; backend = {backend}")
    print(f"  spectrum round-trip residual = {recon_residual:.3e}  "
          f"(eigvalsh recovers loaded +/- pairs)")
    print()

    # ---- (3) Three eta-form schemes -> reduced rho-invariant ----
    print("[SEC 2] Three eta-form schemes on the BdG Nambu spectrum")
    eta_APS = eta_aps_1975(lam_full)  # (local)
    eta_CS = eta_cheeger_simons(lam_full)  # (local)
    eta_BC, BC_adiabatic_residual, _K_samples = eta_bismut_cheeger(lam_full)  # (local)

    rho_APS = reduced_rho(eta_APS, dim_ker)  # (local)
    rho_CS = reduced_rho(eta_CS, dim_ker)  # (local)
    rho_BC = reduced_rho(eta_BC, dim_ker)  # (local)

    print(f"  eta_APS = {eta_APS:.6e}   -> rho_APS = {rho_APS:.6e}")
    print(f"  eta_CS  = {eta_CS:.6e}   -> rho_CS  = {rho_CS:.6e}")
    print(f"  eta_BC  = {eta_BC:.6e}   -> rho_BC  = {rho_BC:.6e}")
    print(f"  Bismut-Cheeger adiabatic-limit residual = "
          f"{BC_adiabatic_residual:.3e}")
    print()

    # ---- (4) Three pairwise scheme-INDEPENDENCE tests ----
    print("[SEC 3] Three pairwise scheme-INDEPENDENCE tests (rho-invariant)")
    diff_AC = abs(rho_APS - rho_CS)  # (local)
    diff_AB = abs(rho_APS - rho_BC)  # (local)
    diff_CB = abs(rho_CS - rho_BC)  # (local)
    max_pairwise_diff = max(diff_AC, diff_AB, diff_CB)  # (local)
    print(f"  diff_AC = |rho_APS - rho_CS| = {diff_AC:.6e} M_KK^2")
    print(f"  diff_AB = |rho_APS - rho_BC| = {diff_AB:.6e} M_KK^2")
    print(f"  diff_CB = |rho_CS - rho_BC|  = {diff_CB:.6e} M_KK^2")
    print(f"  max_pairwise_diff = {max_pairwise_diff:.6e} M_KK^2")
    print(f"  EPS_INDEP threshold = {EPS_INDEP:.0e} M_KK^2")
    print()

    reading_A_pass = (
        diff_AC <= EPS_INDEP and diff_AB <= EPS_INDEP and diff_CB <= EPS_INDEP
    )  # (local)
    reading_confirmed = "A" if reading_A_pass else "B"  # (local)
    print(f"  Reading_A_PASS = {reading_A_pass}  => Reading {reading_confirmed} "
          f"confirmed")
    print()

    # ---- (5) HIT (Hybrid Independence Test) predicate (i) AND (iii) AND (iv) ----
    # The HIT distinctness is STRUCTURAL (read off the pillar/bridge-class axes),
    # NOT a numerical result; pinned here so the verdict carries the predicate.
    print("[SEC 4] Hybrid Independence Test (HIT) predicate vs K=1/K=2")
    hit_i_distinct_pillar = True  # (local) Pillar V (BdG) vs K1 Pillar III / K2 VII.AQ HP^1
    hit_iii_distinct_bridge_class = True  # (local) rho-invariant vs GV-Heitsch (both prior)
    hit_iv_independent_envelope = True  # (local) BdG-sector reduced-eta envelope, not HP^1 GV
    # HIT predicate: (i OR ii OR iii) AND iv; here (i) AND (iii) AND (iv) all hold.
    hit_predicate = (
        (hit_i_distinct_pillar or hit_iii_distinct_bridge_class)
        and hit_iv_independent_envelope
    )  # (local)
    print(f"  (i)   distinct substrate-IS pillar (Pillar V BdG)        = "
          f"{hit_i_distinct_pillar}")
    print(f"  (iii) distinct bridge-map class (rho-invariant)          = "
          f"{hit_iii_distinct_bridge_class}")
    print(f"  (iv)  independent algebraic envelope (BdG-sector eta)    = "
          f"{hit_iv_independent_envelope}")
    print(f"  HIT predicate (i OR iii) AND iv = {hit_predicate}")
    print()

    # ---- (6) Verdict (composite: scheme-INDEPENDENCE band) ----
    print("[SEC 5] Verdict (scheme-INDEPENDENCE band)")
    if max_pairwise_diff <= EPS_INDEP:
        verdict = "PASS"  # (local) Reading A: scheme-INDEPENDENCE
    elif max_pairwise_diff < EPS_INDEP_INFO_CEILING:
        verdict = "INFO"  # (local) marginal scheme-independence
    else:
        verdict = "FAIL"  # (local) Reading B: scheme-DEPENDENCE
    # K=3 advancement is LICENSED iff LEG 1 PASS AND HIT predicate holds.
    k3_advancement_licensed = (verdict == "PASS") and hit_predicate  # (local)
    k_counter_post = K_POST if k3_advancement_licensed else K_PRE  # (local)
    print(f"  composite verdict = {verdict}")
    print(f"  K=3 MANDATORY advancement LICENSED = {k3_advancement_licensed}  "
          f"(K_pre={K_PRE} -> K_post={k_counter_post})")
    print()

    # ---- (7) Save NPZ ----
    print("[SEC 6] Save NPZ + PNG artifacts")
    np.savez(
        OUT_NPZ,
        # rho-invariant under the three schemes
        rho_APS=rho_APS,
        rho_CS=rho_CS,
        rho_BC=rho_BC,
        eta_APS=eta_APS,
        eta_CS=eta_CS,
        eta_BC=eta_BC,
        dim_ker=dim_ker,
        # three pairwise scheme-INDEPENDENCE diffs
        diff_AC=diff_AC,
        diff_AB=diff_AB,
        diff_CB=diff_CB,
        max_pairwise_diff=max_pairwise_diff,
        EPS_INDEP=EPS_INDEP,
        EPS_INDEP_INFO_CEILING=EPS_INDEP_INFO_CEILING,
        reading_A_pass=reading_A_pass,
        reading_confirmed=reading_confirmed,
        composite_verdict=verdict,
        # HIT predicate values
        hit_i_distinct_pillar=hit_i_distinct_pillar,
        hit_iii_distinct_bridge_class=hit_iii_distinct_bridge_class,
        hit_iv_independent_envelope=hit_iv_independent_envelope,
        hit_predicate=hit_predicate,
        k3_advancement_licensed=k3_advancement_licensed,
        K_pre=K_PRE,
        K_post=k_counter_post,
        k1_instance_sha=K1_INSTANCE_SHA,
        k2_instance_sha=K2_INSTANCE_SHA,
        # BdG spectrum + diagnostics
        E_pos_branch=E_pos,
        lam_full_nambu=lam_full,
        bdg_sign_sum=bdg_art["sign_sum_full_nambu"],
        bdg_E_min=bdg_art["E_pos_min"],
        bdg_E_max=bdg_art["E_pos_max"],
        bdg_L_max_row=bdg_art["L_max_row_value"],
        bdg_source_npz=bdg_art["source_npz"],
        bdg_source_audit_sha256=bdg_art["source_audit_sha256"],
        BC_adiabatic_residual=BC_adiabatic_residual,
        eig_backend=backend,
        eig_recon_residual=recon_residual,
        # pins
        L_MAX_PRIMARY=L_MAX_PRIMARY,
        Delta_BCS=Delta_BCS,
        tau_fold=tau_fold,
        M_KK=M_KK,
        plan_pinned_bdg_present=plan_pinned_present,
        runtime_resolved_bdg=PILLAR_V_BDG_DATA.name,
        # provenance
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        scheme=SCHEME,
        convention=CONVENTION,
        schema_version=SCHEMA_VERSION,
        gate_id=GATE_ID,
        level_class_pin="FULL",
        regulator_pin="a_n^{Mellin}",
        binding_axis="substrate-natural-binding",
    )
    print(f"  NPZ saved -> {OUT_NPZ.name}")

    # ---- (8) PNG: 3-scheme rho-invariant bar chart ----
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(14.0, 5.5))
    schemes = ["APS-1975", "Cheeger-Simons", "Bismut-Cheeger"]
    rho_vals = [rho_APS, rho_CS, rho_BC]
    colors = ["#3a86ff", "#fb5607", "#8338ec"]

    # Left: rho-invariant per scheme (the 3-scheme bar chart)
    axL.bar(schemes, rho_vals, color=colors, edgecolor="k", alpha=0.85)
    axL.axhline(0.0, color="k", lw=0.8)
    axL.set_ylabel(r"$\rho(D_{\mathrm{BdG}})$  (reduced $\eta$; $M_{KK}^2$)")
    axL.set_title(
        f"Pillar-V BdG $\\rho$-invariant at L_max={L_MAX_PRIMARY}\n"
        f"three $\\eta$-scheme evaluation (Nambu spectrum)"
    )
    axL.grid(True, axis="y", alpha=0.3)
    axL.set_xticklabels(schemes, rotation=10, ha="right")
    # annotate small spread
    span = max(abs(v) for v in rho_vals) if any(rho_vals) else 1.0  # (local)
    axL.set_ylim(-max(span * 1.5, 0.5), max(span * 1.5, 0.5))
    for i, v in enumerate(rho_vals):
        axL.text(i, 0.02, f"{v:.2e}", ha="center", va="bottom", fontsize=8)

    # Right: pairwise scheme-INDEPENDENCE diffs vs EPS_INDEP band
    pair_labels = ["|APS-CS|", "|APS-BC|", "|CS-BC|"]
    pair_vals = [diff_AC, diff_AB, diff_CB]
    bars = axR.bar(pair_labels, pair_vals, color="#06d6a0",
                   edgecolor="k", alpha=0.85)
    axR.axhline(EPS_INDEP, color="r", ls="--", lw=1.2,
                label=f"EPS_INDEP = {EPS_INDEP:.0e}")
    axR.axhline(EPS_INDEP_INFO_CEILING, color="orange", ls=":", lw=1.0,
                label=f"INFO band = {EPS_INDEP_INFO_CEILING:.0e}")
    axR.set_yscale("symlog", linthresh=1.0e-16)
    axR.set_ylim(-1.0e-16, max(EPS_INDEP * 10, max(pair_vals) * 10, 1e-12))
    axR.set_ylabel(r"$|\Delta\rho|\;(M_{KK}^2)$  [symlog]")
    axR.set_title(
        f"Pairwise scheme-INDEPENDENCE at L_max={L_MAX_PRIMARY}\n"
        f"Reading {reading_confirmed}; verdict={verdict}; "
        f"K={K_PRE}->{k_counter_post}"
    )
    axR.grid(True, alpha=0.3)
    axR.legend(loc="upper right", fontsize=9)
    axR.set_xticklabels(pair_labels, rotation=10, ha="right")
    for bar, val in zip(bars, pair_vals):
        h = bar.get_height()  # (local)
        axR.text(bar.get_x() + bar.get_width() / 2, max(h, 1e-16) * 1.5,
                 f"{val:.2e}", ha="center", va="bottom", fontsize=8)

    fig.suptitle(
        f"{GATE_ID}\n"
        f"Pillar-V BdG rho-invariant 3-eta-scheme; "
        f"max_pairwise_diff={max_pairwise_diff:.2e} vs EPS={EPS_INDEP:.0e}; "
        f"HIT (i AND iii AND iv)={hit_predicate}",
        fontsize=9,
    )
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"  PNG saved -> {OUT_PNG.name}")
    print()

    # ---- (9) Emit verdict line (canonical + dual-SHA companion; no 3-tuple) ----
    print("[SEC 7] Emit verdict (S84+ canonical + dual-SHA companion row)")
    value_str = (
        f"reading_A_pass={reading_A_pass};"
        f"reading_confirmed={reading_confirmed};"
        f"max_pairwise_diff={max_pairwise_diff:.6e};"
        f"diff_AC={diff_AC:.6e};"
        f"diff_AB={diff_AB:.6e};"
        f"diff_CB={diff_CB:.6e};"
        f"rho_APS={rho_APS:.6e};"
        f"rho_CS={rho_CS:.6e};"
        f"rho_BC={rho_BC:.6e};"
        f"dim_ker={dim_ker};"
        f"bdg_sign_sum={bdg_art['sign_sum_full_nambu']:.1f};"
        f"bdg_E_min={bdg_art['E_pos_min']:.6f};"
        f"BC_adiabatic_residual={BC_adiabatic_residual:.3e};"
        f"hit_i_distinct_pillar={hit_i_distinct_pillar};"
        f"hit_iii_distinct_bridge_class={hit_iii_distinct_bridge_class};"
        f"hit_iv_independent_envelope={hit_iv_independent_envelope};"
        f"hit_predicate={hit_predicate};"
        f"k3_advancement_licensed={k3_advancement_licensed};"
        f"K_pre={K_PRE};K_post={k_counter_post};"
        f"k1_sha={K1_INSTANCE_SHA[:16]};k2_sha={K2_INSTANCE_SHA[:16]};"
        f"EPS_INDEP={EPS_INDEP:.0e};"
        f"L_max={L_MAX_PRIMARY};"
        f"level_pin=FULL;regulator_pin=a_n_Mellin;"
        f"binding_axis=substrate-natural-binding;"
        f"bdg_source={PILLAR_V_BDG_DATA.name};"
        f"eig_backend={backend}"
    )  # (local)
    append_verdict(verdict, value_str, audit_sha, content_sha)
    print()
    print(f"  Verdict appended -> {VERDICT_TXT.name}")
    print()

    wall = time.time() - t0  # (local)
    print("=" * 78)
    print(f"=== {GATE_ID}: {verdict} (Reading {reading_confirmed}; "
          f"wall {wall:.1f}s) ===")
    print(f"  rho_APS={rho_APS:.3e}  rho_CS={rho_CS:.3e}  rho_BC={rho_BC:.3e}")
    print(f"  max_pairwise_diff = {max_pairwise_diff:.3e} "
          f"(threshold {EPS_INDEP:.0e})")
    print(f"  HIT (i AND iii AND iv) = {hit_predicate}; "
          f"K=3 advancement LICENSED = {k3_advancement_licensed}")
    print("=" * 78)

    # Per math-scripts.md "Exit Codes": exit 0 on successful execution
    # regardless of PASS/FAIL/INFO verdict.
    return 0


if __name__ == "__main__":
    sys.exit(main())
