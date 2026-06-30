"""
S103-FOREIGN-STACK-B1B2
=======================

Session 103, Wave 2, item 11. Foreign-stack bit-exact Peter-Weyl block
re-implementation (monoculture-remedy reproducibility), EXTENDED from the (1,1)
block (S102, max_diff=0.0 PASS) to the bottom-of-spectrum (0,0) and (0,1) blocks.

GATE (per-block equality):
    PASS  iff  max_block | sorted(|foreign|)_block - sorted(|canonical|)_block | < 1e-12
               for BOTH block in {(0,0), (0,1)}.

The eigenvalue extraction is via H = iD eigvalsh ONLY (the W3-12 Hermiticity-
enforced methodology pin; hazard-H5). D_K is anti-self-adjoint in the framework
math convention (no explicit i), so iD is Hermitian and eigvalsh(H) returns the
real +/-|lambda| spectrum. NO general eig (non-Hermitian scatter), NO svd surrogate.

SUBSTRATE FRAMING (GEOMETRIC)
-----------------------------
Direction of explanation:
  SU(3) irreps V_{(p,q)} -> block Dirac operator D_{(p,q)} on V_{(p,q)} (x) C^16
  -> eigenvalue spectrum {+/-|lambda|} (extracted via H=iD eigvalsh)
  -> the B1/B2 bottom-of-spectrum anchors.

The (0,0) block is the trivial-rep ground multiplet: C_2(0,0)=0 EXACT (the unique
lowest SU(3) quadratic Casimir), so the substrate's lowest vibrational mode
provably sits in sector (0,0); B1 = 0.819741 at tau_fold. The (0,1) block is the
conjugate 3-bar fundamental; its bottom is B2 = 0.835894 (per s52 sector ordering;
B3 = 0.872975 is the (1,1) bottom, NOT a (0,1) eigenvalue). The monoculture remedy
guards against a shared-implementation artifact in the construction leg: an
INDEPENDENT foreign stack (NOT importing dirac_spectrum.py) must reproduce the
same vibrational-mode spectrum at the lowest two blocks.

TWO LEGS PER BLOCK
------------------
(a) CANONICAL leg : the (p,q) block from the project numpy pipeline
    (dirac_spectrum.get_irrep + dirac_operator_on_irrep). DIFF TARGET ONLY;
    cross-checked against the s84 (p,q)-sector cache.

(b) FOREIGN leg   : the same (p,q) block rebuilt from scratch in foreign_block(p,q)
    WITHOUT importing dirac_spectrum.py / branching_computation.py. The irrep is
    constructed INDEPENDENTLY: (0,0) is the 1-dim trivial rep (rho(e_a)=0);
    (0,1) is the anti-fundamental rho(e_a) = -e_a^T. The frame / connection /
    Clifford(R^8) / spinor-curvature-offset Omega legs reuse the S102 foreign
    construction verbatim (generalized over (p,q)).

GENERALIZATION NOTE vs S102
---------------------------
S102 hardcoded the (1,1) adjoint via rho[a][c,b] = f[a,b,c]. This gate generalizes
foreign_block() over (p,q): the SU(3)-algebra / frame / Clifford / Omega legs are
(p,q)-independent (built once); only the irrep rho is (p,q)-keyed. The (1,1) block
is re-run as a regression sentinel to confirm the generalized routine still
reproduces the S102 result.

Author: spectral-geometer (phonon-exflation project, Session 103)
"""

import os
import sys
import json
import hashlib

os.environ.setdefault("OMP_NUM_THREADS", "8")  # (local) CPU thread cap (tiny blocks; before import numpy)
os.environ.setdefault("MKL_NUM_THREADS", "8")  # (local)

import numpy as np  # noqa: E402

# ---------------------------------------------------------------------------
# canonical constants (MANDATORY import; never hardcode framework constants)
# ---------------------------------------------------------------------------
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "_shared")))
from canonical_constants import tau_fold  # noqa: E402

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
SHARED = os.path.abspath(os.path.join(HERE, "..", "_shared"))
CACHE_PATH = os.path.abspath(os.path.join(HERE, "..", "session-84", "s84_spectrum_cache_L12_tau019.npz"))
DIRAC_PIPELINE_PATH = os.path.join(SHARED, "dirac_spectrum.py")
CANON_CONST_PATH = os.path.join(SHARED, "canonical_constants.py")
FOREIGN_TEMPLATE_PATH = os.path.abspath(os.path.join(HERE, "..", "session-102", "s102_foreign_stack_pw_block_reimpl.py"))
OUT_NPZ = os.path.join(HERE, "s103_foreign_stack_b1b2.npz")
OUT_PNG = os.path.join(HERE, "s103_foreign_stack_b1b2.png")

# gate machinery (per plan W2-4 machinery_pin_map)
BLOCKS = [(0, 0), (0, 1)]    # (local) the two bottom-of-spectrum blocks (B1, B2 anchors)
SENTINEL_BLOCK = (1, 1)      # (local) S102 regression sentinel (max_diff=0.0 precedent)
DIM_SPIN = 16                # (local) 2^4 spinor rank for d=8
PASS_EPS = 1e-12             # (local) per-block strict PASS boundary (MATCHED to S102 tight floor for cross-block consistency)

# cache cross-anchors (substrate-first: queried from s60 Strutinsky / s52 ordering
# via knowledge MCP; the cache itself is the authoritative source, loaded at runtime)
B1_ANCHOR = 0.819741         # (local) (0,0)-block bottom |lambda| (s60 Strutinsky; s84 cache); B1
B2_ANCHOR = 0.835894         # (local) (0,1)-block bottom |lambda| (s52 ordering: tau=0.19 B2=0.835894); B2


# ===========================================================================
#  FOREIGN STACK -- independent of dirac_spectrum.py / branching_computation.py
# ===========================================================================

def gell_mann():
    """Gell-Mann matrices lambda_1..8 (0-indexed 0..7), FOREIGN re-implementation.

    Independent transcription -- this code does NOT import branching_computation.py
    or dirac_spectrum.py. Ordering matches the standard SU(3) convention (the same
    the canonical pipeline uses), required so the diff compares the SAME operator
    and not a relabelled basis.
    """
    s = np.sqrt(3.0)
    L = [None] * 8
    L[0] = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex)
    L[1] = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex)
    L[2] = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex)
    L[3] = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex)
    L[4] = np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex)
    L[5] = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    L[6] = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex)
    L[7] = np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / s
    return L


def foreign_irrep(p, q, e):
    """Construct the SU(3) irrep V_{(p,q)} INDEPENDENTLY (the foreign construction
    leg) for the bottom-of-spectrum blocks {(0,0), (0,1)} plus the (1,1) sentinel.

    Args:
        p, q : highest-weight labels
        e    : the 8 anti-Hermitian su(3) generators e_a = -i/2 lambda_a (3x3)

    Returns:
        rho : list of 8 complex matrices (dim_pq x dim_pq), the rep of e_a
    """
    dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
    if (p, q) == (0, 0):
        # Trivial rep: rho(e_a) = 0 (1x1). The Dirac block reduces to I_1 (x) Omega.
        return [np.zeros((1, 1), dtype=complex) for _ in range(8)]
    if (p, q) == (0, 1):
        # Anti-fundamental (conjugate of (1,0)): rho(e_a) = -e_a^T.
        # Independent of dirac_spectrum.py: built directly from the foreign e_a.
        return [-e[a].T for a in range(8)]
    if (p, q) == (1, 1):
        # Adjoint (S102 sentinel): rho(e_a)_{cb} = f_abc. Built from the foreign
        # structure constants (independent transcription).
        f = np.zeros((8, 8, 8), dtype=float)
        for a in range(8):
            for b in range(8):
                comm = e[a] @ e[b] - e[b] @ e[a]
                for c in range(8):
                    f[a, b, c] = (-2.0 * np.trace(comm @ e[c])).real
        rho = [np.zeros((8, 8), dtype=complex) for _ in range(8)]
        for a in range(8):
            for c in range(8):
                for b in range(8):
                    rho[a][c, b] = f[a, b, c]
        return rho
    raise NotImplementedError(f"foreign_irrep: ({p},{q}) not in the gate's block set")


def _foreign_su3_infrastructure():
    """Build the (p,q)-INDEPENDENT foreign infrastructure ONCE: generators,
    structure constants, Killing form, Jensen frame, ON-frame structure constants,
    Levi-Civita connection, Clifford(R^8), spinor-curvature offset Omega.

    All built WITHOUT importing dirac_spectrum.py (the foreign leg).

    Returns:
        e      : list of 8 anti-Hermitian su(3) generators
        Ed     : (8,) diagonal frame entries E_aa (e_a = E_aa X_a)
        gam    : list of 8 Hermitian Clifford generators (16x16)
        Omega  : (16,16) spinor curvature offset
        diag   : dict of verified intermediates
    """
    # 1. su(3) generators e_a = -i/2 lambda_a
    lam = gell_mann()
    e = [(-1j / 2.0) * lam[a] for a in range(8)]

    # 2. structure constants f_abc = -2 Tr([e_a,e_b] e_c) (real, antisymmetric)
    f = np.zeros((8, 8, 8), dtype=float)
    for a in range(8):
        for b in range(8):
            comm = e[a] @ e[b] - e[b] @ e[a]
            for c in range(8):
                f[a, b, c] = (-2.0 * np.trace(comm @ e[c])).real

    # 3. Killing form B_ab = sum_cd f_acd f_bcd (= 3*I for su(3))
    B = np.einsum("acd,bcd->ab", f, f)

    # 4. U(2)-invariant Jensen frame. g0=|B| diagonal -> g diagonal -> E diagonal.
    tau = float(tau_fold)
    L1, L2, L3 = np.exp(2.0 * tau), np.exp(-2.0 * tau), np.exp(tau)  # (local) u1, su2, C^2 scale factors
    SU2 = [0, 1, 2]   # (local)
    C2 = [3, 4, 5, 6]  # (local)
    U1 = [7]          # (local)
    g_diag = np.zeros(8)  # (local)
    g0 = np.abs(B)        # (local)
    for a in SU2:
        g_diag[a] = g0[a, a] * L2
    for a in C2:
        g_diag[a] = g0[a, a] * L3
    for a in U1:
        g_diag[a] = g0[a, a] * L1
    Ed = 1.0 / np.sqrt(g_diag)  # (local) diagonal frame entries

    # 5. ON-frame structure constants ft^c_{ab} = E_a E_b f^c_{ab} / E_c
    ft = np.zeros((8, 8, 8), dtype=float)  # (local)
    for a in range(8):
        for b in range(8):
            for c in range(8):
                ft[a, b, c] = Ed[a] * Ed[b] * f[a, b, c] / Ed[c]

    # 6. Levi-Civita connection Gamma^c_{ab} = 1/2 (ft_abc - ft_bca + ft_cab)
    Gamma = np.zeros((8, 8, 8), dtype=float)  # (local) Gamma[c,a,b]
    for c in range(8):
        for a in range(8):
            for b in range(8):
                Gamma[c, a, b] = 0.5 * (ft[a, b, c] - ft[b, c, a] + ft[c, a, b])

    # 7. Clifford(R^8): gamma_1..8, 16x16 Hermitian, via Pauli kron (independent build)
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)

    def k4(A, Bm, Cm, Dm):
        return np.kron(A, np.kron(Bm, np.kron(Cm, Dm)))

    gam = [
        k4(s1, I2, I2, I2), k4(s2, I2, I2, I2), k4(s3, s1, I2, I2), k4(s3, s2, I2, I2),
        k4(s3, s3, s1, I2), k4(s3, s3, s2, I2), k4(s3, s3, s3, s1), k4(s3, s3, s3, s2),
    ]

    # 8. spinor curvature offset Omega = 1/4 sum Gamma^b_{ac} gamma_a gamma_b gamma_c
    Omega = np.zeros((16, 16), dtype=complex)
    for a in range(8):
        for b in range(8):
            for c in range(8):
                coeff = Gamma[b, a, c]
                if abs(coeff) > 1e-15:
                    Omega += coeff * gam[a] @ gam[b] @ gam[c]
    Omega *= 0.25

    diag = {
        "killing_diag": np.diag(B).tolist(),
        "killing_offdiag_max": float(np.max(np.abs(B - np.diag(np.diag(B))))),
        "frame_diag": Ed.tolist(),
        "ft_norm": float(np.linalg.norm(ft)),
        "gamma_norm": float(np.linalg.norm(Gamma)),
        "omega_norm": float(np.linalg.norm(Omega)),
        "omega_antiherm_err": float(np.max(np.abs(Omega + Omega.conj().T))),
        "f_123": float(f[0, 1, 2]),
        "f_458": float(f[3, 4, 7]),
    }
    return e, Ed, gam, Omega, diag


def foreign_block(p, q, infra):
    """Rebuild the (p,q) Dirac block from scratch -- the FOREIGN numpy code path
    (independent of dirac_spectrum.py), generalized over (p,q).

    D_{(p,q)} = sum_a E_aa rho(e_a) (x) gamma_a + I_{dim} (x) Omega.
    Eigenvalues via the stable Hermitian route H = i*D (eigvalsh; W3-12 pin).

    Args:
        p, q  : highest-weight labels
        infra : the (p,q)-independent foreign infrastructure from
                _foreign_su3_infrastructure()

    Returns:
        absev : sorted |eigenvalue| array (dim*16 entries)
        bdiag : dict of block diagnostics
    """
    e, Ed, gam, Omega, _ = infra
    rho = foreign_irrep(p, q, e)
    dim_rho = rho[0].shape[0]
    dim_block = dim_rho * DIM_SPIN  # (local)

    # assemble block: D = sum_a E_aa rho(e_a) (x) gamma_a + I_dim (x) Omega
    D = np.zeros((dim_block, dim_block), dtype=complex)
    for a in range(8):
        D += Ed[a] * np.kron(rho[a], gam[a])
    D += np.kron(np.eye(dim_rho), Omega)

    # eigenvalues via the W3-12 Hermitian route (H = iD; H = (iD + iD^dag)/2 hazard-H5)
    iD = 1j * D
    H = (iD + iD.conj().T) / 2.0
    herm_err = float(np.max(np.abs(iD - iD.conj().T)))  # (local) Hermiticity-enforcement residual
    absev = np.sort(np.abs(np.linalg.eigvalsh(H)))

    bdiag = {
        "dim_rho": dim_rho,
        "dim_block": dim_block,
        "D_antiherm_err": float(np.max(np.abs(D + D.conj().T))),
        "iD_herm_err": herm_err,
        "lowest_abs": float(absev[0]),
        "highest_abs": float(absev[-1]),
    }
    return absev, bdiag


# ===========================================================================
#  CANONICAL LEG -- the project numpy pipeline (DIFF TARGET ONLY)
# ===========================================================================

def canonical_block(p, q):
    """The (p,q) block from the project numpy pipeline -- DIFF TARGET ONLY.

    Uses the same H = iD eigvalsh extraction as the foreign leg (the W3-12 pin).
    """
    import dirac_spectrum as ds  # CANONICAL leg ONLY
    tau = float(tau_fold)
    gens = ds.su3_generators()
    f = ds.compute_structure_constants(gens)
    B = ds.compute_killing_form(f)
    g = ds.jensen_metric(B, tau)
    E = ds.orthonormal_frame(g)
    ft = ds.frame_structure_constants(f, E)
    Gamma = ds.connection_coefficients(ft)
    gammas = ds.build_cliff8()
    Omega = ds.spinor_connection_offset(Gamma, gammas)
    rho, _ = ds.get_irrep(p, q, gens, f)
    D = ds.dirac_operator_on_irrep(rho, E, gammas, Omega)
    iD = 1j * D
    H = (iD + iD.conj().T) / 2.0
    absev = np.sort(np.abs(np.linalg.eigvalsh(H)))
    return absev


def load_cache_block(p, q):
    """The pre-stored (p,q)-sector |eigenvalues| from the s84 L12 cache."""
    d = np.load(CACHE_PATH, allow_pickle=True)
    rec = d["sector_evals"].item()[(p, q)]
    return np.sort(np.asarray(rec["abs_evals"], dtype=float)), int(rec["dim"])


# ===========================================================================
#  SHA / verdict helpers
# ===========================================================================

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map):
    blob = json.dumps(pin_map, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(blob).hexdigest()


def print_verdict_payload(gate_id, verdict, value, scheme, convention, l_max,
                          audit_sha256, content_sha256, schema_version="S84+"):
    """Print the EMIT_VERDICT payload block to stdout (the script never writes the
    verdict file directly -- the agent calls the race-safe emit_verdict MCP tool)."""
    payload = {
        "session": 103,
        "gate_id": gate_id,
        "verdict": verdict,
        "value": value,
        "scheme": scheme,
        "convention": convention,
        "l_max": l_max,
        "audit_sha256": audit_sha256,
        "content_sha256": content_sha256,
        "schema_version": schema_version,
    }
    print("<<<EMIT_VERDICT_PAYLOAD>>>" + json.dumps(payload) + "<<<END_EMIT_VERDICT_PAYLOAD>>>")


def main():
    # ---- input SHA pins (logged in first lines of stdout per gate-verdicts.md) ----
    canon_sha = sha256_file(CANON_CONST_PATH)
    cache_sha = sha256_file(CACHE_PATH)
    dirac_sha = sha256_file(DIRAC_PIPELINE_PATH)
    template_sha = sha256_file(FOREIGN_TEMPLATE_PATH)
    print(f"[input-sha] canonical_constants.py = {canon_sha}")
    print(f"[input-sha] s84_spectrum_cache_L12_tau019.npz = {cache_sha}")
    print(f"[input-sha] dirac_spectrum.py (CANONICAL leg only) = {dirac_sha}")
    print(f"[input-sha] s102_foreign_stack_pw_block_reimpl.py (foreign template) = {template_sha}")
    print(f"[pin] tau_fold = {float(tau_fold)} ; blocks = {BLOCKS} + sentinel {SENTINEL_BLOCK} ; pass_eps = {PASS_EPS:.0e}")
    print(f"[pin] H = iD eigvalsh (W3-12 Hermiticity-enforced extraction; NO general eig, NO svd)")

    # ---- foreign infrastructure built ONCE (p,q-independent) ----
    infra = _foreign_su3_infrastructure()
    fdiag = infra[4]
    print(f"[foreign-infra] Killing diag = {np.round(fdiag['killing_diag'],6)} offdiag_max={fdiag['killing_offdiag_max']:.2e}")
    print(f"[foreign-infra] f_123={fdiag['f_123']:.6f} f_458={fdiag['f_458']:.6f} (sqrt3/2={np.sqrt(3)/2:.6f})")
    print(f"[foreign-infra] ft_norm={fdiag['ft_norm']:.4f} gamma_norm={fdiag['gamma_norm']:.4f} omega_norm={fdiag['omega_norm']:.4f}")
    print(f"[foreign-infra] omega_antiherm_err={fdiag['omega_antiherm_err']:.2e}")

    # ---- per-block comparison (gate) + (1,1) sentinel regression ----
    results = {}  # (local) per-block diagnostics
    all_blocks = BLOCKS + [SENTINEL_BLOCK]  # (local) gate blocks + sentinel
    block_max_diffs = {}  # (local) per-block max|foreign - canonical|
    for (p, q) in all_blocks:
        foreign, bdiag = foreign_block(p, q, infra)
        canonical = canonical_block(p, q)
        cache, cache_dim = load_cache_block(p, q)
        assert foreign.shape == canonical.shape, f"({p},{q}) block dim mismatch: foreign {foreign.shape} vs canonical {canonical.shape}"

        max_diff = float(np.max(np.abs(foreign - canonical)))  # (local)
        # cache cross-check: canonical-vs-cache (confirms cache snapshot faithfulness)
        cache_diff = float(np.max(np.abs(canonical - cache))) if cache.shape == canonical.shape else float("nan")  # (local)
        block_max_diffs[(p, q)] = max_diff
        results[(p, q)] = {
            "dim_rho": bdiag["dim_rho"],
            "dim_block": bdiag["dim_block"],
            "n_evals": int(foreign.shape[0]),
            "foreign_lowest": float(foreign[0]),
            "canonical_lowest": float(canonical[0]),
            "cache_lowest": float(cache[0]),
            "foreign_highest": float(foreign[-1]),
            "max_diff": max_diff,
            "cache_diff": cache_diff,
            "D_antiherm_err": bdiag["D_antiherm_err"],
            "iD_herm_err": bdiag["iD_herm_err"],
        }
        tag = "GATE" if (p, q) in BLOCKS else "SENTINEL"
        print(f"[{tag} ({p},{q})] dim_block={bdiag['dim_block']} n={foreign.shape[0]} "
              f"foreign_lo={foreign[0]:.12f} canon_lo={canonical[0]:.12f} cache_lo={cache[0]:.12f}")
        print(f"[{tag} ({p},{q})] max|foreign - canonical| = {max_diff:.3e}  "
              f"max|canonical - cache| = {cache_diff:.3e}  (PASS boundary < {PASS_EPS:.0e})")

    # ---- cross-anchor cross-check: foreign (0,0) lowest = B1, (0,1) lowest = B2 ----
    foreign00_lo = results[(0, 0)]["foreign_lowest"]  # (local)
    foreign01_lo = results[(0, 1)]["foreign_lowest"]  # (local)
    b1_err = abs(foreign00_lo - B1_ANCHOR)  # (local)
    b2_err = abs(foreign01_lo - B2_ANCHOR)  # (local)
    print(f"[anchor] foreign (0,0) lowest = {foreign00_lo:.6f}  |.-B1={B1_ANCHOR}| = {b1_err:.2e}")
    print(f"[anchor] foreign (0,1) lowest = {foreign01_lo:.6f}  |.-B2={B2_ANCHOR}| = {b2_err:.2e}")

    # ---- the GATE: max over the two bottom-of-spectrum blocks {(0,0),(0,1)} ----
    gate_max_diff = max(block_max_diffs[(0, 0)], block_max_diffs[(0, 1)])  # (local)
    sentinel_diff = block_max_diffs[SENTINEL_BLOCK]  # (local) (1,1) regression
    print(f"[GATE] max over {{(0,0),(0,1)}} of max|foreign - canonical| = {gate_max_diff:.3e}  (< {PASS_EPS:.0e})")
    print(f"[SENTINEL] (1,1) max|foreign - canonical| = {sentinel_diff:.3e}  (S102 precedent max_diff=0.0)")

    # ---- verdict (per-block equality, both blocks must pass) ----
    pass_00 = block_max_diffs[(0, 0)] < PASS_EPS  # (local)
    pass_01 = block_max_diffs[(0, 1)] < PASS_EPS  # (local)
    if pass_00 and pass_01:
        verdict = "PASS"
    else:
        verdict = "FAIL"
    floor_note = "machine-eps_bit-exact" if gate_max_diff < 1e-14 else (  # (local)
        "sub-1e-12_round-off" if gate_max_diff < PASS_EPS else "block_spectrum_mismatch")
    value = (f"gate_max_diff={gate_max_diff:.3e}_blocks_(0,0)+(0,1)_tau_fold"
             f"_d00={block_max_diffs[(0,0)]:.2e}_d01={block_max_diffs[(0,1)]:.2e}"
             f"_floor={floor_note}_sentinel(1,1)={sentinel_diff:.2e}"
             f"_B1anchor_err={b1_err:.2e}_B2anchor_err={b2_err:.2e}")

    # ---- save data ----
    save_kwargs = {
        "blocks": np.array(BLOCKS),
        "sentinel_block": np.array(SENTINEL_BLOCK),
        "gate_max_diff": gate_max_diff,
        "max_diff_00": block_max_diffs[(0, 0)],
        "max_diff_01": block_max_diffs[(0, 1)],
        "max_diff_11_sentinel": sentinel_diff,
        "B1_anchor": B1_ANCHOR,
        "B2_anchor": B2_ANCHOR,
        "b1_err": b1_err,
        "b2_err": b2_err,
        "tau_fold": float(tau_fold),
        "pass_eps": PASS_EPS,
        "verdict": verdict,
        "results_json": json.dumps({f"{p}_{q}": v for (p, q), v in results.items()}),
        "infra_diag": json.dumps(fdiag),
    }
    # full eigenvalue vectors per block for the audit trail
    for (p, q) in all_blocks:
        f_ev, _ = foreign_block(p, q, infra)
        c_ev = canonical_block(p, q)
        save_kwargs[f"foreign_{p}{q}"] = f_ev
        save_kwargs[f"canonical_{p}{q}"] = c_ev
    np.savez(OUT_NPZ, **save_kwargs)
    print(f"[data] wrote {OUT_NPZ}")

    # ---- plot ----
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, axes = plt.subplots(2, 3, figsize=(15, 8))
        for col, (p, q) in enumerate(all_blocks):
            f_ev, _ = foreign_block(p, q, infra)
            c_ev = canonical_block(p, q)
            diffv = np.maximum(np.abs(f_ev - c_ev), 1e-18)  # (local)
            k = np.arange(len(f_ev))  # (local)
            ax_top = axes[0, col]
            ax_bot = axes[1, col]
            ax_top.plot(k, c_ev, "o", ms=3, label="canonical", color="C0")
            ax_top.plot(k, f_ev, "x", ms=4, label="foreign", color="C3")
            ax_top.set_xlabel("eigenvalue index (sorted)")
            ax_top.set_ylabel(r"$|\lambda|$")
            tag = "GATE" if (p, q) in BLOCKS else "SENTINEL"
            ax_top.set_title(f"({p},{q}) block [{tag}]  dim {len(f_ev)//16}x16")
            ax_top.legend(fontsize=8)
            ax_top.grid(alpha=0.3)
            ax_bot.semilogy(k, diffv, ".", ms=4, color="C2")
            ax_bot.axhline(PASS_EPS, ls="--", color="k", label=f"PASS {PASS_EPS:.0e}")
            ax_bot.set_xlabel("eigenvalue index (sorted)")
            ax_bot.set_ylabel(r"$|\,$foreign $-$ canonical$\,|$")
            ax_bot.set_title(f"cross-stack diff (max={block_max_diffs[(p,q)]:.1e})")
            ax_bot.legend(fontsize=8)
            ax_bot.grid(alpha=0.3)
        fig.suptitle("S103-FOREIGN-STACK-B1B2 — monoculture remedy at bottom-of-spectrum (0,0),(0,1) + (1,1) sentinel", fontsize=12)
        fig.tight_layout()
        fig.savefig(OUT_PNG, dpi=130)
        print(f"[plot] wrote {OUT_PNG}")
    except Exception as exc:  # pragma: no cover
        print(f"[plot] skipped: {exc}")

    # ---- dual SHA + verdict payload ----
    pin_map = {
        "gate_id": "S103-FOREIGN-STACK-B1B2",
        "blocks": [list(b) for b in BLOCKS],
        "sentinel_block": list(SENTINEL_BLOCK),
        "tau_fold": float(tau_fold),
        "canonical_constants_sha256": canon_sha,
        "spectrum_cache_sha256": cache_sha,
        "dirac_spectrum_sha256": dirac_sha,
        "foreign_template_sha256": template_sha,
        "scheme": "foreign-stack-independent-reimplementation-monoculture-remedy",
        "convention": "ABSOLUTE-eigenvalue-magnitude-bit-exact",
        "extraction": "H=iD-eigvalsh-W3-12-pin",
        "pass_eps": PASS_EPS,
        "gate_max_diff": gate_max_diff,
    }
    audit_sha = closure_hash(pin_map)
    content_sha = sha256_file(os.path.abspath(__file__))
    print_verdict_payload(
        gate_id="S103-FOREIGN-STACK-B1B2",
        verdict=verdict,
        value=value,
        scheme="foreign-stack-independent-reimplementation-monoculture-remedy",
        convention="ABSOLUTE-eigenvalue-magnitude-bit-exact",
        l_max="N/A",
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
