#!/usr/bin/env python3
"""
S102 W4-15 — CF-S102-QUARK-PERGEN-KERNEL  ([SIGN])
==================================================

Gate: CF-S102-QUARK-PERGEN-KERNEL  ([SIGN])

HYPOTHESIS (plan §W4-15):
  A generation-DEPENDENT slope structure (per-generation kappa_g, or a
  non-monotone omega_g in C2) DERIVED from the substrate dressed-block structure
  reproduces the gen-1 up/down inversion (m_u/m_d < 1) AND the gen-3 upright
  ordering (m_t/m_b > 1) SIMULTANEOUSLY -- which W2-4 (S101) proved impossible
  for ANY single uniform (kappa_up, kappa_down) pair on a C2-monotone omega-ladder
  -- with per-component CKM framed as the misalignment of two rank-one dressings,
  the [SIGN] anchor preserved, and the W3-9 walls + [J,D_K]=0 intact.

PRE-REGISTERED THRESHOLD (set-membership + RATIO):
  PASS = (m_u/m_d)_pred < 1 (DERIVED)  AND  (m_t/m_b)_pred > 1 (DERIVED)
         AND PDG held-out anchors (m_u/m_d=0.4596, m_t/m_b=41.28) reproduced to
         RATIO tol <= 30% (DERIVED-not-fitted band)
         AND triality-CG-admissibility(every nonzero inter-sector element)=True
         AND sign(SIGN-anchor) preserved.
  [SIGN] 3-tuple:
    sign_verdict  = PASS iff the substrate-DERIVED per-gen slope asymmetry
                    (kappa_g^up - kappa_g^down) CHANGES SIGN between g=1 and g=3
                    (the substitution-chain Step 5 crossing condition). FAIL iff
                    no sign change (the predicted direction is not realized).
    magnitude_verdict = PASS iff |r_g - PDG_g|/PDG_g <= 0.30 at gen1 AND gen3;
                    INFO iff <= info-band (0.60); FAIL otherwise.
    regime_verdict = VALID iff triality pre-flight holds AND Omega^D/Omega^c=2
                    (1e-12) AND [J,D_K]=0 / W3-9 sign-direction intact;
                    MARGINAL iff Omega cross-check deviates <= 1e-6;
                    BREAKDOWN iff triality pre-flight fails OR Omega!=2 beyond 1e-6.
  Composite via the CANONICAL gate-verdicts.md collapse rule, unmodified.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-101/s101_w3_quark_component_orientation.npz  (the W3
    dressed-block ladders: comp_trace_mean_lam2_D/_c (diagonals d_g^S), env_up_mg
    / env_down_mg (off-diagonal greybody dressings w_g^S), omega_g, Omega^D/Omega^c=2)
  - canonical_constants.py  (PDG SECTION E quark anchors m_u/m_d/m_t/m_b + tau_fold)
  - script bytes

Output 4-tuple:
  (value=<crossing scalars + slope-asym signs>, scheme=FW,
   convention=RATIO, L_max=10)

Classification: PARTICLE.

METHODOLOGY
-----------
The quark masses are eigenvalues of the dressed 2x2 Peter-Weyl blocks of D_K at
the Jensen-deformed fiber:
    B_g^S = [[ d_g^S , w_g^S ], [ conj(w_g^S) , d_g^S ]],  m_{g,pm}^S = d_g^S +/- |w_g^S|.
The diagonal d_g^S is the bare ladder RMS (substrate-derived: sqrt of the
multiplicity-normalized trace-mean <lam^2>_g^{(comp)} = Omega^{comp}*mean(|lambda|^2),
from S101 W3). The off-diagonal w_g^S is the substrate dressing: the
greybody-transmitted envelope env_*_mg = sqrt(Omega^S)*exp(-2*pi*C2(g)*tau_fold/kappa^S)
(also from S101 W3). The physical mass is the HEAVIER eigenvalue m_g^S = d_g^S + |w_g^S|.

The per-generation RATIO observable is r_g = m_g^{up} / m_g^{down}. W2-4 proved
that a uniform (kappa_up, kappa_down) pair on a C2-monotone ladder CANNOT realize
the joint crossing (r_1 < 1 AND r_3 > 1). The DERIVED resolution test:

  ROUTE (a) -- per-generation slope kappa_g^S := |w_g^S| / d_g^S read DIRECTLY off
             the dressed-block off-diagonal/diagonal asymmetry (substrate, NO PDG).
             The crossing is REACHABLE (substitution chain Step 4-5) iff the slope
             asymmetry (kappa_g^up - kappa_g^down) CHANGES SIGN between g=1 and g=3.

  ROUTE (b) -- a non-monotone omega_g(C2) admitted by the sector geometry. Tested
             for a substrate seed (any non-monotone substrate quantity across the
             3 generations: C2, triality, irrep dim).

CKM (the payoff, S99 structure): V_CKM = U_up^dagger U_down where U_sector is the
eigenbasis of the frozen block [[d,w],[w*,d]]^sector. The selection-rule pre-flight
(triality CG-admissibility) is applied to EVERY claimed nonzero inter-sector
element: t(p,q)=(p-q) mod 3; admissibility t(a)==t(b)+t(O) mod 3.

Direction of explanation: D_K dressed-block eigenvalue ratios -> per-generation
slope asymmetry -> observed quark mass ordering + CKM texture.

DISCIPLINE
----------
- `from canonical_constants import *` (first import).
- intermediates tagged `# (local)`.
- 2x2 frozen-block eigendecompositions: tiny, CPU (numpy.linalg per plan GPU_path).
- SHA-256 of all input files logged in first 20 lines of stdout.
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema).
- 4-tuple printed as the final non-verdict line.
- Gate verdict via emit_verdict MCP tool (race-safe): this script PRINTS the
  payload (print_verdict_payload); the AGENT calls mcp__knowledge__emit_verdict.
- No Seeley-DeWitt a_n cited => no regulator_pin. No SCHEMATIC helper => no CLASS pin.
"""

from __future__ import annotations

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

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # explicit for linters / provenance
    tau_fold,
    M_KK_gravity,
    m_u_msbar_2GeV,
    m_d_msbar_2GeV,
    m_s_msbar_2GeV,
    m_c_msbar_mc,
    m_b_msbar_mb,
    m_t_pole,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration pins
# ---------------------------------------------------------------------------
SESSION = "S102"  # (local)
GATE_ID = "CF-S102-QUARK-PERGEN-KERNEL"  # (local)
SCHEME = "FW"  # (local)
CONVENTION = "RATIO"  # (local)
L_MAX = 10  # (local)

W3_NPZ = COMPUTATIONS_DIR / "session-101" / "s101_w3_quark_component_orientation.npz"  # (local)
CANON = SHARED_DIR / "canonical_constants.py"  # (local)

OUT_NPZ = SESSION_DIR / "s102_quark_pergen_kernel.npz"  # (local)
OUT_PNG = SESSION_DIR / "s102_quark_pergen_kernel.png"  # (local)

INPUT_FILES = [CANON, W3_NPZ]  # (local)

# Pre-registered thresholds.
PASS_RATIO_TOL = 0.30  # (local)  DERIVED-not-fitted band on held-out PDG ratios
INFO_RATIO_TOL = 0.60  # (local)  info-band ceiling for magnitude_verdict
OMEGA_RATIO_TARGET = 2.0  # (local)  Omega^D/Omega^c EXACT
OMEGA_TOL_VALID = 1e-12  # (local)
OMEGA_TOL_MARGINAL = 1e-6  # (local)

# The generation tower (Peter-Weyl sectors) — C2-ASCENDING; mass map C2-DESCENDING.
#   gen3 (heaviest) <-> (1,0) [lowest C2];  gen1 (lightest) <-> (3,0) [highest C2].
TOWER = [(1, 0), (1, 1), (3, 0)]  # (local)  C2-ascending
GEN_OF_SECTOR = {(1, 0): 3, (1, 1): 2, (3, 0): 1}  # (local)


def C2(p: int, q: int) -> float:
    """SU(3) quadratic Casimir, C2(p,q) = (p^2+q^2+pq)/3 + p + q."""
    return (p * p + q * q + p * q) / 3.0 + p + q


def triality(p: int, q: int) -> int:
    """SU(3) center character (triality) t(p,q) = (p - q) mod 3."""
    return (p - q) % 3


def irrep_dim(p: int, q: int) -> int:
    """SU(3) irrep dimension (p+1)(q+1)(p+q+2)/2."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (dual-SHA, S84+)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
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
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
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


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------
def selection_rule_preflight() -> dict:
    """Triality CG-admissibility on (i) intra-sector dressing (mass op, t(O)=0),
    (ii) inter-generation CKM channels (W/mass mixing, t(O)=0).
    Returns admissibility map; intra-sector is ALWAYS admissible (t(a)==t(a)+0);
    inter-generation channels admissible iff t(sector_i)==t(sector_j) mod 3."""
    out = {}  # (local)
    # (i) intra-sector dressing
    intra = {}  # (local)
    for (p, q) in TOWER:
        ta = triality(p, q)  # (local)
        intra[(p, q)] = (ta == (ta + 0) % 3)  # mass operator t(O)=0 -> always True
    out["intra_sector"] = intra
    # (ii) inter-generation CKM channels (the claimed nonzero misalignment channels)
    inter = {}  # (local)
    for i in range(len(TOWER)):
        for j in range(i + 1, len(TOWER)):
            si, sj = TOWER[i], TOWER[j]  # (local)
            ti, tj = triality(*si), triality(*sj)  # (local)
            adm = (ti == (tj + 0) % 3)  # (local)  W/mass op t(O)=0
            gi, gj = GEN_OF_SECTOR[si], GEN_OF_SECTOR[sj]  # (local)
            inter[f"gen{gi}<->gen{gj}"] = {
                "t_i": ti, "t_j": tj, "admissible": bool(adm)
            }
    out["inter_generation"] = inter
    return out


def ckm_misalignment(d_up, w_up, d_dn, w_dn) -> dict:
    """V_CKM = U_up^dagger U_down, U_sector = eigenbasis of [[d,w],[w*,d]]^sector,
    per generation block (S99 structure). The 2x2 within-sector block mixes the
    two chirality faces; the inter-GENERATION mixing is the misalignment of the
    up-sector and down-sector eigenvectors. arg(w) lives entirely in the
    diagonalizing unitary (connes' eigenvector result) — here w is real (the
    greybody magnitude), so each 2x2 U is the symmetric-block rotation by pi/4;
    the GENERATION-space misalignment is governed by the per-gen (d,w) ratios.

    We build a 3x3 generation-space mixing proxy from the per-generation
    eigenvector overlaps and apply the triality MASK (forbidden channels -> 0)."""
    n = len(TOWER)  # (local)
    # per-generation 2x2 eigenvectors (symmetric block -> [1,1]/sqrt2, [1,-1]/sqrt2)
    # The heavier eigenvector for sector S at gen g: v = [1, sign(w)] / sqrt2.
    # Generation-space proxy: M[i,j] = (heavier-eigvec overlap weighted by the
    # off/diag ratio) -> a Cabibbo-like texture seed. Apply triality mask.
    M = np.zeros((n, n))  # (local)
    tris = [triality(*s) for s in TOWER]  # (local)
    # off/diag slope per gen per sector
    ku = [w_up[i] / d_up[i] for i in range(n)]  # (local)
    kd = [w_dn[i] / d_dn[i] for i in range(n)]  # (local)
    for i in range(n):
        for j in range(n):
            if i == j:
                M[i, j] = 1.0
            else:
                # misalignment magnitude proxy ~ |slope_up_i - slope_dn_j| normalized;
                # triality-forbidden channels (t_i != t_j) are EXACTLY zero.
                if tris[i] != tris[j]:
                    M[i, j] = 0.0  # triality-FORBIDDEN -> exact zero
                else:
                    M[i, j] = abs(ku[i] - kd[j]) / (1.0 + abs(ku[i]) + abs(kd[j]))
    return {"mixing_proxy": M, "trialities": tris}


def compute() -> dict:
    print(f"\n=== {GATE_ID} — PART 2 compute (dressed-block per-gen kernel) ===")
    data = np.load(W3_NPZ, allow_pickle=True)  # (local)

    # --- load S101 W3 dressed-block ingredients (gen3, gen2, gen1 ordering) ---
    # diagonal d_g^S = sqrt(<lam^2>_g^{(comp)})  (RMS mass scale of the bare ladder)
    cD = np.asarray(data["comp_trace_mean_lam2_D"], dtype=np.float64)  # (local) down <lam^2>
    cc = np.asarray(data["comp_trace_mean_lam2_c"], dtype=np.float64)  # (local) up   <lam^2>
    d_dn = np.sqrt(cD)  # (local)  diagonal down
    d_up = np.sqrt(cc)  # (local)  diagonal up
    # off-diagonal dressings w_g^S = greybody-transmitted envelope (substrate)
    w_up = np.asarray(data["env_up_mg"], dtype=np.float64)  # (local)  up dressing
    w_dn = np.asarray(data["env_down_mg"], dtype=np.float64)  # (local)  down dressing
    omega_D = float(data["omega_D"])  # (local)  8/3
    omega_c = float(data["omega_c"])  # (local)  4/3
    npz_ud_ratio = np.asarray(data["ud_ratio"], dtype=np.float64)  # (local) env-only ratio
    gen_of = list(np.asarray(data["gen_of_sector"]))  # (local) [3,2,1]

    print("  loaded S101 W3 dressed-block ingredients (gen3, gen2, gen1):")
    for i in range(3):
        print(
            f"    gen{gen_of[i]}: d_up={d_up[i]:.5f} d_dn={d_dn[i]:.5f}  "
            f"w_up={w_up[i]:.6f} w_dn={w_dn[i]:.6f}"
        )

    # --- diagonal-only ratio (the floor): r = d_up/d_dn = sqrt(Omega^c/Omega^D) ---
    diag_ratio = d_up / d_dn  # (local)
    sqrt_omega_ratio = np.sqrt(omega_c / omega_D)  # (local) = sqrt(1/2)=0.7071
    print(
        f"\n  diagonal-only ratio d_up/d_dn = {diag_ratio[0]:.5f} (all gens; "
        f"= sqrt(Omega^c/Omega^D) = {sqrt_omega_ratio:.5f})  -> up always lighter on diagonal."
    )

    # --- physical mass = HEAVIER eigenvalue m_g^S = d_g^S + |w_g^S| ---
    m_up = d_up + np.abs(w_up)  # (local)
    m_dn = d_dn + np.abs(w_dn)  # (local)
    r_g = m_up / m_dn  # (local)  per-generation up/down ratio (DERIVED)
    # index: 0=gen3, 1=gen2, 2=gen1
    r_gen3 = float(r_g[0])  # (local)
    r_gen2 = float(r_g[1])  # (local)
    r_gen1 = float(r_g[2])  # (local)

    print("\n  DERIVED per-gen ratio r_g = (d+|w|)_up / (d+|w|)_dn  (heavier eigenvalue):")
    print(f"    gen3 r={r_gen3:.5f}   gen2 r={r_gen2:.5f}   gen1 r={r_gen1:.5f}")

    # --- crossing test ---
    cross_gen1 = r_gen1 < 1.0  # (local)  inversion (up lighter)
    cross_gen3 = r_gen3 > 1.0  # (local)  upright (up heavier)
    crossing_realized = bool(cross_gen1 and cross_gen3)  # (local)
    print(
        f"\n  crossing: gen1 r<1 (inversion): {cross_gen1}  "
        f"gen3 r>1 (upright): {cross_gen3}  => realized: {crossing_realized}"
    )

    # --- DERIVED per-gen slope kappa_g^S = |w_g^S|/d_g^S, and the sign-asymmetry ---
    kappa_up = np.abs(w_up) / d_up  # (local)
    kappa_dn = np.abs(w_dn) / d_dn  # (local)
    slope_asym = kappa_up - kappa_dn  # (local)  (kappa_g^up - kappa_g^down) per gen
    print("\n  DERIVED per-gen slope asymmetry (kappa_g^up - kappa_g^down):")
    for i in range(3):
        print(
            f"    gen{gen_of[i]}: kappa_up={kappa_up[i]:.5f} kappa_dn={kappa_dn[i]:.5f}  "
            f"asym={slope_asym[i]:+.5f}"
        )
    # substitution-chain Step 5: crossing reachable IFF sign(asym) flips g3<->g1
    asym_gen3 = float(slope_asym[0])  # (local)
    asym_gen1 = float(slope_asym[2])  # (local)
    sign_flip = bool(asym_gen3 * asym_gen1 < 0.0)  # (local)  TRUE iff opposite signs
    print(
        f"\n  slope-asym sign: gen3={'+' if asym_gen3 > 0 else '-'}  "
        f"gen1={'+' if asym_gen1 > 0 else '-'}  => SIGN FLIP (Step 5): {sign_flip}"
    )

    # --- binding analytic crossing constraints (substitution chain Step 4) ---
    gap_gen3 = float(d_dn[0] - d_up[0])  # (local) gen3: need (w_up-w_dn) > this
    gap_gen1 = float(d_dn[2] - d_up[2])  # (local) gen1: need (w_up-w_dn) < this
    wdiff_gen3 = float(w_up[0] - w_dn[0])  # (local)
    wdiff_gen1 = float(w_up[2] - w_dn[2])  # (local)
    gen3_constraint_met = wdiff_gen3 > gap_gen3  # (local)
    gen1_constraint_met = wdiff_gen1 < gap_gen1  # (local)
    print("\n  BINDING crossing constraints (analytic, Step 4):")
    print(
        f"    gen3 upright needs (w_up-w_dn)={wdiff_gen3:.5f} > {gap_gen3:.5f}: "
        f"{gen3_constraint_met}"
    )
    print(
        f"    gen1 inversion needs (w_up-w_dn)={wdiff_gen1:.5f} < {gap_gen1:.5f}: "
        f"{gen1_constraint_met}"
    )

    # --- ROUTE (b) non-monotone omega_g seed test (across the 3 generations) ---
    c2_seq = [C2(*s) for s in TOWER]  # (local) [1.333, 3.0, 6.0]
    tri_seq = [triality(*s) for s in TOWER]  # (local) [1, 0, 0]
    dim_seq = [irrep_dim(*s) for s in TOWER]  # (local) [3, 8, 10]

    def is_monotone(seq):
        asc = all(seq[i] < seq[i + 1] for i in range(len(seq) - 1))  # (local)
        desc = all(seq[i] > seq[i + 1] for i in range(len(seq) - 1))  # (local)
        return asc or desc

    c2_mono = is_monotone(c2_seq)  # (local)
    dim_mono = is_monotone(dim_seq)  # (local)
    # triality is a step [1,0,0]: monotone non-increasing (1>=0>=0) but not STRICT;
    # a non-monotone omega needs a strict dip/peak in the MIDDLE generation (gen2).
    tri_mid_dip = (tri_seq[1] < tri_seq[0] and tri_seq[1] < tri_seq[2])  # (local) gen2 dip
    tri_mid_peak = (tri_seq[1] > tri_seq[0] and tri_seq[1] > tri_seq[2])  # (local) gen2 peak
    routeb_seed = bool(tri_mid_dip or tri_mid_peak)  # (local) any non-monotone seed
    print("\n  ROUTE (b) substrate non-monotone seed test (gen3, gen2, gen1):")
    print(f"    C2 = {c2_seq}  monotone: {c2_mono}")
    print(f"    triality = {tri_seq}  gen2 dip: {tri_mid_dip}  gen2 peak: {tri_mid_peak}")
    print(f"    irrep dim = {dim_seq}  monotone: {dim_mono}")
    print(f"    => route(b) non-monotone omega_g seed available: {routeb_seed}")

    # --- PDG held-out reference ratios (NOT fitted) ---
    pdg_mu_md = m_u_msbar_2GeV / m_d_msbar_2GeV  # (local) gen1 = 0.4596
    pdg_mt_mb = m_t_pole / m_b_msbar_mb  # (local) gen3 = 41.28
    pdg_mc_ms = m_c_msbar_mc / m_s_msbar_2GeV  # (local) gen2
    # relative deviation of DERIVED ratios vs held-out PDG
    rel_gen1 = abs(r_gen1 - pdg_mu_md) / pdg_mu_md  # (local)
    rel_gen3 = abs(r_gen3 - pdg_mt_mb) / pdg_mt_mb  # (local)
    print("\n  PDG held-out (NOT fitted):")
    print(f"    gen1 m_u/m_d = {pdg_mu_md:.4f}  DERIVED r_gen1={r_gen1:.4f}  rel={rel_gen1*100:.1f}%")
    print(f"    gen3 m_t/m_b = {pdg_mt_mb:.4f}  DERIVED r_gen3={r_gen3:.4f}  rel={rel_gen3*100:.1f}%")
    print(f"    gen2 m_c/m_s = {pdg_mc_ms:.4f}  (reference)")

    # --- selection-rule pre-flight (triality CG-admissibility) ---
    selrule = selection_rule_preflight()  # (local)
    print("\n  selection-rule pre-flight (triality CG-admissibility):")
    print("    intra-sector dressing (mass op, t(O)=0):")
    for (p, q), adm in selrule["intra_sector"].items():
        print(f"      ({p},{q}) gen{GEN_OF_SECTOR[(p,q)]}: t={triality(p,q)} admissible={adm}")
    print("    inter-generation CKM channels (W/mass mixing, t(O)=0):")
    for ch, info in selrule["inter_generation"].items():
        print(f"      {ch}: t_i={info['t_i']} t_j={info['t_j']} admissible={info['admissible']}")
    intra_all_ok = all(selrule["intra_sector"].values())  # (local)
    # Cabibbo channel (gen2<->gen1, t=0<->t=0) MUST be admissible; gen3 channels triality-suppressed.
    # (channel keys are built in TOWER order i<j: gen3 first -> "gen2<->gen1" is the 1-2 channel.)
    cabibbo_adm = selrule["inter_generation"]["gen2<->gen1"]["admissible"]  # (local)
    gen3_channels_suppressed = (
        not selrule["inter_generation"]["gen3<->gen2"]["admissible"]
        and not selrule["inter_generation"]["gen3<->gen1"]["admissible"]
    )  # (local)
    print(
        f"    => intra all admissible: {intra_all_ok}; Cabibbo (1<->2) admissible: "
        f"{cabibbo_adm}; gen3 channels triality-suppressed: {gen3_channels_suppressed}"
    )

    # --- CKM misalignment proxy (S99 structure) with triality mask ---
    ckm = ckm_misalignment(d_up, w_up, d_dn, w_dn)  # (local)
    M = ckm["mixing_proxy"]  # (local)
    print("\n  CKM misalignment proxy (generation-space, triality-masked):")
    print("    rows/cols = [gen3, gen2, gen1]")
    for i in range(3):
        print("    " + "  ".join(f"{M[i,j]:.4f}" for j in range(3)))
    cabibbo_dominant = bool(
        M[1, 2] > M[0, 1] and M[1, 2] > M[0, 2]
    )  # (local) gen1<->gen2 (Cabibbo) is the largest off-diagonal
    print(f"    Cabibbo-dominant texture (1<->2 largest off-diagonal): {cabibbo_dominant}")

    # --- Omega^D/Omega^c machinery cross-check (regime tag) ---
    omega_ratio = omega_D / omega_c  # (local)
    omega_dev = abs(omega_ratio - OMEGA_RATIO_TARGET)  # (local)
    print(f"\n  Omega^D/Omega^c = {omega_ratio:.15f} (target 2; dev={omega_dev:.3e})")

    # --- W3-9 sign-direction + [J,D_K]=0 intactness (structural, non-recomputed) ---
    # The diagonal d_g is C2-DESCENDING in mass (heavier <-> lower C2): the W3-9
    # freeze-in sign-direction. Verify the diagonal mass map is C2-descending:
    w39_sign_intact = bool(d_up[0] < d_up[2] and d_dn[0] < d_dn[2])  # (local)
    # (sqrt<lam^2> ASCENDS with C2 => mass DESCENDS with C2 == gen3 heaviest. The
    #  diagonal d ascends gen3->gen1, consistent with the W3-9 ascent of <lam^2>.)
    print(f"  W3-9 sign-direction (diagonal <lam^2> ascends with C2): {w39_sign_intact}")

    # =====================================================================
    # VERDICT ASSEMBLY (pre-registered)
    # =====================================================================
    # sign_verdict: Step-5 crossing condition = slope-asym sign flip g3<->g1.
    sign_verdict = "PASS" if sign_flip else "FAIL"  # (local)

    # magnitude_verdict: held-out PDG ratio agreement at gen1 AND gen3.
    rel_max = max(rel_gen1, rel_gen3)  # (local)
    if rel_max <= PASS_RATIO_TOL:
        magnitude_verdict = "PASS"  # (local)
    elif rel_max <= INFO_RATIO_TOL:
        magnitude_verdict = "INFO"  # (local)
    else:
        magnitude_verdict = "FAIL"  # (local)

    # regime_verdict: triality pre-flight + Omega cross-check + W3-9 / [J,D_K]=0.
    triality_ok = bool(intra_all_ok and cabibbo_adm)  # (local)
    if (not triality_ok) or (not w39_sign_intact):
        regime_verdict = "BREAKDOWN"  # (local)
    elif omega_dev <= OMEGA_TOL_VALID:
        regime_verdict = "VALID"  # (local)
    elif omega_dev <= OMEGA_TOL_MARGINAL:
        regime_verdict = "MARGINAL"  # (local)
    else:
        regime_verdict = "BREAKDOWN"  # (local)

    # composite collapse (CANONICAL gate-verdicts.md rule, unmodified)
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"  # (local)
    elif magnitude_verdict == "INFO":
        composite = "INFO"  # (local)
    else:
        composite = "PASS"  # (local)

    return {
        "d_up": d_up, "d_dn": d_dn, "w_up": w_up, "w_dn": w_dn,
        "diag_ratio": diag_ratio, "sqrt_omega_ratio": float(sqrt_omega_ratio),
        "m_up": m_up, "m_dn": m_dn, "r_g": r_g,
        "r_gen1": r_gen1, "r_gen2": r_gen2, "r_gen3": r_gen3,
        "cross_gen1": cross_gen1, "cross_gen3": cross_gen3,
        "crossing_realized": crossing_realized,
        "kappa_up": kappa_up, "kappa_dn": kappa_dn, "slope_asym": slope_asym,
        "asym_gen3": asym_gen3, "asym_gen1": asym_gen1, "sign_flip": sign_flip,
        "gap_gen3": gap_gen3, "gap_gen1": gap_gen1,
        "wdiff_gen3": wdiff_gen3, "wdiff_gen1": wdiff_gen1,
        "gen3_constraint_met": bool(gen3_constraint_met),
        "gen1_constraint_met": bool(gen1_constraint_met),
        "c2_seq": c2_seq, "tri_seq": tri_seq, "dim_seq": dim_seq,
        "routeb_seed": routeb_seed,
        "pdg_mu_md": pdg_mu_md, "pdg_mt_mb": pdg_mt_mb, "pdg_mc_ms": pdg_mc_ms,
        "rel_gen1": rel_gen1, "rel_gen3": rel_gen3, "rel_max": rel_max,
        "selrule_intra_ok": intra_all_ok, "cabibbo_adm": cabibbo_adm,
        "gen3_channels_suppressed": gen3_channels_suppressed,
        "ckm_proxy": M, "cabibbo_dominant": cabibbo_dominant,
        "omega_ratio": omega_ratio, "omega_dev": omega_dev,
        "w39_sign_intact": w39_sign_intact,
        "npz_ud_ratio": npz_ud_ratio,
        "sign_verdict": sign_verdict, "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict, "composite": composite,
    }


# ---------------------------------------------------------------------------
# Section 6 — 4-tuple + verdict payload
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(
    verdict, value, audit_sha, content_sha,
    sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
    extra_rows=None,
):
    payload = {
        "session": "102",
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if sign_verdict is not None:
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = extra_rows
    print("\n=== VERDICT PAYLOAD (JSON for emit_verdict) ===")
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------
def make_plot(R: dict) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(17, 5))  # (local)
    g_axis = [3, 2, 1]  # (local)  npz ordering idx0=gen3
    x = [0, 1, 2]  # (local)
    xt = ["gen3\n(1,0)", "gen2\n(1,1)", "gen1\n(3,0)"]  # (local)

    # Panel 1: DERIVED per-gen slope asymmetry (kappa_up - kappa_dn) — the [SIGN] axis
    ax = axes[0]
    ax.plot(x, R["slope_asym"], "o-", color="C3", lw=2, ms=9,
            label=r"$\kappa_g^{up}-\kappa_g^{down}$ (DERIVED)")
    ax.axhline(0.0, color="k", ls=":", lw=1, label="sign-flip line")
    ax.set_xticks(x)
    ax.set_xticklabels(xt)
    ax.set_ylabel(r"slope asymmetry $\kappa_g^{up}-\kappa_g^{down}$")
    ax.set_title(
        "[SIGN] axis: per-gen slope asymmetry\n"
        f"sign-flip g3<->g1: {R['sign_flip']}  (PASS needs flip)"
    )
    for xi, s in zip(x, R["slope_asym"]):
        ax.annotate(f"{s:+.4f}", (xi, s), textcoords="offset points", xytext=(4, 6), fontsize=8)
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel 2: DERIVED per-gen ratio r_g = (d+|w|)_up/(d+|w|)_dn vs PDG + crossing line
    ax = axes[1]
    ax.semilogy(x, R["r_g"], "D-", color="C2", lw=2, ms=9, label=r"DERIVED $r_g=m_{up}/m_{down}$")
    ax.axhline(1.0, color="k", ls=":", lw=1, label="crossing line (=1)")
    ax.axhline(R["sqrt_omega_ratio"], color="C0", ls="--", lw=1,
               label=r"diag floor $\sqrt{\Omega^c/\Omega^D}$=0.707")
    pdg = [R["pdg_mt_mb"], R["pdg_mc_ms"], R["pdg_mu_md"]]  # (local) gen3,gen2,gen1
    ax.semilogy(x, pdg, "*", color="C1", ms=14, label="PDG held-out (t/b, c/s, u/d)")
    ax.set_xticks(x)
    ax.set_xticklabels(xt)
    ax.set_ylabel(r"$m_{up}/m_{down}$")
    ax.set_title(
        "crossing test (DERIVED)\n"
        f"gen1<1: {R['cross_gen1']}  gen3>1: {R['cross_gen3']}  realized: {R['crossing_realized']}"
    )
    ax.legend(fontsize=7)
    ax.grid(alpha=0.3, which="both")

    # Panel 3: CKM misalignment proxy (triality-masked) heatmap
    ax = axes[2]
    M = R["ckm_proxy"]  # (local)
    im = ax.imshow(M, cmap="viridis", aspect="auto")
    ax.set_xticks([0, 1, 2]); ax.set_yticks([0, 1, 2])
    ax.set_xticklabels(["gen3", "gen2", "gen1"])
    ax.set_yticklabels(["gen3", "gen2", "gen1"])
    for i in range(3):
        for j in range(3):
            ax.text(j, i, f"{M[i,j]:.3f}", ha="center", va="center",
                    color="w" if M[i, j] < 0.5 else "k", fontsize=9)
    ax.set_title(
        "CKM misalignment proxy (triality-masked)\n"
        f"Cabibbo (1<->2) dominant: {R['cabibbo_dominant']}; gen3 channels suppressed: {R['gen3_channels_suppressed']}"
    )
    fig.colorbar(im, ax=ax, fraction=0.046)

    fig.suptitle(
        f"{GATE_ID}  [SIGN]  composite={R['composite']}  "
        f"(sign={R['sign_verdict']} mag={R['magnitude_verdict']} regime={R['regime_verdict']})",
        fontsize=11,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.94])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"\n  plot -> {OUT_PNG.relative_to(PROJECT_ROOT)}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)  # (local)
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(), CANON, pins)  # (local)
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    R = compute()  # (local)

    # --- value payload (single-quote-free per emit_verdict grammar) ---
    value = (
        f"r_g1={R['r_gen1']:.4f};r_g3={R['r_gen3']:.4f};"
        f"cross_g1<1={R['cross_gen1']};cross_g3>1={R['cross_gen3']};crossing={R['crossing_realized']};"
        f"slope_asym_g3={R['asym_gen3']:+.5f};slope_asym_g1={R['asym_gen1']:+.5f};signflip={R['sign_flip']};"
        f"PDG_u/d={R['pdg_mu_md']:.4f}(rel{R['rel_gen1']*100:.0f}pct);"
        f"PDG_t/b={R['pdg_mt_mb']:.4f}(rel{R['rel_gen3']*100:.0f}pct);"
        f"triality_intra_ok={R['selrule_intra_ok']};cabibbo_adm={R['cabibbo_adm']};"
        f"gen3_chan_suppressed={R['gen3_channels_suppressed']};cabibbo_dom={R['cabibbo_dominant']};"
        f"routeb_seed={R['routeb_seed']};OmegaD/Omegac={R['omega_ratio']:.6f};JDK0_W39={R['w39_sign_intact']}"
    )  # (local)

    print("\n" + emit_4tuple(value, SCHEME, CONVENTION, L_MAX))

    # --- save npz (full float64) ---
    np.savez(
        OUT_NPZ,
        tower=np.array(TOWER),
        gen_of_sector=np.array([GEN_OF_SECTOR[s] for s in TOWER]),
        C2_tower=np.array(R["c2_seq"]),
        triality_tower=np.array(R["tri_seq"]),
        dim_tower=np.array(R["dim_seq"]),
        d_up=R["d_up"], d_dn=R["d_dn"], w_up=R["w_up"], w_dn=R["w_dn"],
        diag_ratio=R["diag_ratio"], sqrt_omega_ratio=R["sqrt_omega_ratio"],
        m_up=R["m_up"], m_dn=R["m_dn"], r_g=R["r_g"],
        r_gen1=R["r_gen1"], r_gen2=R["r_gen2"], r_gen3=R["r_gen3"],
        cross_gen1=R["cross_gen1"], cross_gen3=R["cross_gen3"],
        crossing_realized=R["crossing_realized"],
        kappa_up=R["kappa_up"], kappa_dn=R["kappa_dn"], slope_asym=R["slope_asym"],
        asym_gen3=R["asym_gen3"], asym_gen1=R["asym_gen1"], sign_flip=R["sign_flip"],
        gap_gen3=R["gap_gen3"], gap_gen1=R["gap_gen1"],
        wdiff_gen3=R["wdiff_gen3"], wdiff_gen1=R["wdiff_gen1"],
        gen3_constraint_met=R["gen3_constraint_met"],
        gen1_constraint_met=R["gen1_constraint_met"],
        routeb_seed=R["routeb_seed"],
        pdg_mu_md=R["pdg_mu_md"], pdg_mt_mb=R["pdg_mt_mb"], pdg_mc_ms=R["pdg_mc_ms"],
        rel_gen1=R["rel_gen1"], rel_gen3=R["rel_gen3"], rel_max=R["rel_max"],
        selrule_intra_ok=R["selrule_intra_ok"], cabibbo_adm=R["cabibbo_adm"],
        gen3_channels_suppressed=R["gen3_channels_suppressed"],
        ckm_proxy=R["ckm_proxy"], cabibbo_dominant=R["cabibbo_dominant"],
        omega_ratio=R["omega_ratio"], omega_dev=R["omega_dev"],
        w39_sign_intact=R["w39_sign_intact"],
        npz_ud_ratio=R["npz_ud_ratio"],
        tau_fold=tau_fold, M_KK_gravity=M_KK_gravity,
        pass_ratio_tol=PASS_RATIO_TOL, info_ratio_tol=INFO_RATIO_TOL,
        sign_verdict=R["sign_verdict"], magnitude_verdict=R["magnitude_verdict"],
        regime_verdict=R["regime_verdict"], composite=R["composite"],
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"  data -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    make_plot(R)

    # --- extra companion rows ---
    extra_rows = [
        (
            f"# slope_asym_g3={R['asym_gen3']:+.5f} slope_asym_g1={R['asym_gen1']:+.5f} "
            f"signflip={R['sign_flip']} crossing={R['crossing_realized']} "
            f"# {GATE_ID} per-gen slope-asymmetry (Step-5 sign-flip = crossing condition)"
        ),
        (
            f"# triality_intra_ok={R['selrule_intra_ok']} cabibbo_adm={R['cabibbo_adm']} "
            f"gen3_chan_suppressed={R['gen3_channels_suppressed']} cabibbo_dom={R['cabibbo_dominant']} "
            f"OmegaD/Omegac={R['omega_ratio']:.6f}(target2) JDK0_W39={R['w39_sign_intact']} "
            f"# {GATE_ID} selection-rule pre-flight + CKM texture + machinery cross-check"
        ),
    ]  # (local)

    payload = print_verdict_payload(
        R["composite"], value, audit_sha, content_sha,
        sign_verdict=R["sign_verdict"],
        magnitude_verdict=R["magnitude_verdict"],
        regime_verdict=R["regime_verdict"],
        extra_rows=extra_rows,
    )

    print(f"\n=== {GATE_ID}: {R['composite']} "
          f"(sign={R['sign_verdict']} mag={R['magnitude_verdict']} regime={R['regime_verdict']}) "
          f"wall {time.time()-t0:.1f}s ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
