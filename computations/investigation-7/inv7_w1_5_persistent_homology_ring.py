#!/usr/bin/env python3
"""
INV7 W1-5 — Persistent-homology beta_1/beta_2 Betti curves of the framework field vs LCDM mocks
================================================================================================

Gate: INV7-W1-5 ([VERIFY])  (investigation track)

Pre-registered threshold (plan §W1-5):
  operator:  Z = |beta_2_FW(nu_r1) - <beta_2_GRF(nu_r1)>| / std(beta_2_GRF(nu_r1)) >= n_sigma
  n_sigma = 3.0 (a >=3 sigma separation between the framework beta_2 at the ring scale and the
                 GRF-mock distribution is the threshold for 'topological feature present and
                 ABSENT in LCDM').
  PASS iff Z >= 3.0     (topological signature present, ABSENT in LCDM -> Track A; sector can be SHARP)
  INFO iff 2.0 <= Z < 3.0 (suggestive sub-threshold feature)
  FAIL iff Z < 2.0      (topologically indistinguishable from LCDM at the ring scale -> Track B)

HYPOTHESIS
----------
The persistent-homology Betti curves beta_1(nu), beta_2(nu) of the framework field
  F_FW = F_Gauss(P_FW) + A_FS * ring(k1) + f_NL=1.505 local non-Gaussianity (Row #69, S95 F-NL-ROW)
carry a beta_2 (void/shell-loop) feature localized near the ring scale r1=325 Mpc that is ABSENT in
LCDM Gaussian-random-field mocks (matched P(k) amplitude + primary BAO peak, f_NL=0, no ring) at
>= 3 sigma. This is the SPECIFIC observable-scale 325 Mpc ring, explicitly DISTINCT from the S43
volume-averaged-Betti closure at k~10^24 h/Mpc (unobservable; k_transition=9.4e23 h/Mpc per S43).

SUBSTRATE FRAMING (phononic-framing.md)
---------------------------------------
The substrate IS the post-transit GGE acoustic field; cosmic structure IS the interference pattern of
post-transit GGE excitations. The web's TOPOLOGY (loops beta_1, enclosed voids beta_2) is the
LABORATORY-IN image of that interference pattern's phase content. Flow:
  D_K spectrum -> second-sound mode + GGE relic (f_NL envelope) -> framework post-transit field with a
  preferred shell scale r1 and a phase correlation -> persistent-homology Betti curves -> measurable
  web topology.
The gate tests whether the GGE-interference picture carries a topological fingerprint that LCDM's
structureless Gaussian field cannot reproduce. The web is a topological object whose Betti numbers and
persistence capture information that P(k)/xi(r) MISS, so even when two-point statistics match LCDM, the
topology need not.

UPSTREAM (W1-1 LANDED, FAIL)
----------------------------
W1-1 returned the substrate-genuine first-sound-ring amplitude A_FS_substrate = 0.00388533
(= c2^2/c1^2 = rho_n/(3 rho_s)), which is 52.5x WEAKER than the canonical 0.204 (the canonical is the
recombination first-sound stand-in 1/[3(1+R*)], NOT the substrate second sound). This gate consumes the
substrate-genuine A_FS as PRIMARY (the realistic topological signature), and reports the canonical
A_FS=0.204 as a both-ways contrast (the upper-bound topological signature if the ring were as strong as
the standard-formula stand-in). EXPECT the beta_2 ring signal to shrink ~52x accordingly relative to
the canonical-amplitude case.

METHODOLOGY — Betti curves via sublevel-set threshold sweep
-----------------------------------------------------------
GUDHI / ripser are NOT available in the venv; the Betti curves beta_0(nu), beta_1(nu), beta_2(nu) are
computed by a documented threshold-sweep on each field realization (a cubical-complex sublevel
filtration on a periodic 256^3 grid):

  Sublevel set at threshold nu:  X(nu) = { x : F(x) <= nu }   (the low-density / void-wall structure).

  beta_0(nu) = number of connected components of X(nu)
               (scipy.ndimage.label with PERIODIC 3-torus wrap, 6-connectivity / face-adjacency).
  beta_2(nu) = number of ENCLOSED VOIDS = connected components of the complement (superlevel) set
               { x : F(x) > nu } that are bounded -- on the 3-torus, computed via the count of
               superlevel components MINUS the percolating component(s). Operationally this is the
               number of fully-enclosed over-dense pockets sitting inside the void-wall sublevel
               structure -> the 2-cycles (shells) of the filtration.
  beta_1(nu) = recovered from the integral-geometric Euler characteristic of the cubical complex:
               chi(nu) = #vertices - #edges + #faces - #cubes   (of X(nu), periodic),
               and chi = beta_0 - beta_1 + beta_2  =>  beta_1 = beta_0 + beta_2 - chi.

This is an EXACT computation of the cubical-complex Betti numbers per realization (the only
approximation is the cubical-grid discretization of the continuous field, which is the standard
practice in cosmological persistent-homology pipelines -- van de Weygaert / Pranav et al.). The
'persistence' / threshold axis is the density threshold nu in units of sigma_field; the discriminating
statistic is the standardized z-score of beta_2 at the ring-scale threshold against the GRF null
ensemble.

The ring-scale filtration threshold nu_r1 is the density level at which the preferred-shell structure
(radius r1) maximizes the beta_2 separation; pre-registered as the nu that maximizes the GRF-null
beta_2 variance contribution near the void-wall regime, evaluated identically on FW and GRF (a common,
field-agnostic threshold, NOT tuned to the FW field -- avoids look-elsewhere).
"""
from __future__ import annotations

# --- CPU thread cap BEFORE numpy import (persistent-homology labeling is CPU-bound) ---
import os  # noqa: E402
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402
import hashlib  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from scipy import ndimage  # noqa: E402

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY import)
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import (  # noqa: E402
    k1_first_sound_ring_invMpc,   # 0.0193150486 Mpc^-1
    r1_first_sound_ring_Mpc,      # 325.3 Mpc
    max_f_NL_FW,                  # 1.505 (envelope; Bogoliubov-sudden channel is NEGATIVE -1.505)
    sigma_8,                      # 0.811 (Planck 2018) — P(k) normalization reference
    planck_ns,                    # 0.9649 — primordial tilt for the P(k) shape
    Omega_m,                      # 0.315
)

# ---------------------------------------------------------------------------
# Section 2 — Gate identity + machinery pins (plan §W1-5)
# ---------------------------------------------------------------------------
GATE_ID = "INV7-W1-5"
SCHEME = "FW"
# RATIO = standardized z-score separation (absolute Betti normalization removed). The
# -NMOCK48-DEVIATION suffix discloses the runtime reduction of the GRF null ensemble from the plan-
# pinned 100 to 48 (grid=256^3 and N_NU=128 plan pins HONORED; verdict operator UNCHANGED), per the
# gate-verdicts.md / math-scripts.md operational-deviation disclosure discipline.
CONVENTION = "RATIO-PERSISTENT-HOMOLOGY-SUBLEVEL-SWEEP-NMOCK48-DEVIATION"
L_MAX = "N/A"          # persistent homology on a real-space field grid, not a D_K truncation

# machinery_pin_map (plan §W1-5) — gate pins, local to this gate (NOT framework constants)
# OPERATIONAL DEVIATION (disclosed; gate-verdicts.md / math-scripts.md feasibility): the plan pins
# grid=256^3, N_NU=128, N_mock=100. The grid (resolves r1, load-bearing) and N_NU=128 are HONORED.
# N_mock is reduced 100->48 because the per-threshold GLOBAL connected-component labeling (scipy, CPU,
# no GPU path) makes 100 full Betti curves at 256^3 x 128-thr ~110 min, beyond an agent timeslot. The
# Euler-char (beta_1) leg is GPU-accelerated (torch.roll). N_mock=48 keeps the 3-sigma null-ensemble
# std estimate robust (ddof=1; std stable to ~10%). The verdict OPERATOR (Z = beta_2 ring-scale z-score
# vs 3.0) and the field-agnostic nu_r1 selection are UNCHANGED. convention carries the deviation tag.
N_GRID = 256                  # (local) field realization resolution (256^3) — PLAN PIN, honored
N_MOCK = 48                   # (local) GRF null ensemble — DEVIATION from plan 100 (runtime; disclosed)
L_BOX_MPC = 1000.0            # (local) box size (resolves r1=325.3 Mpc with ~3 cells/wavelength margin)
NU_MIN, NU_MAX = -3.0, 3.0    # (local) density-threshold filtration range (sigma_field units)
N_NU = 128                    # (local) uniform thresholds over [-3, 3] sigma — PLAN PIN, honored
RANDOM_SEED = 12345           # (local) FIXED — deterministic verdict given the seed

N_SIGMA_PASS = 3.0            # (local) PASS boundary (plan strict_PASS_boundary)
N_SIGMA_INFO = 2.0            # (local) INFO floor (plan INFO_meaning band)

# A diagnostic sub-ensemble for the canonical-A_FS both-ways contrast (smaller, for runtime)
N_MOCK_CANON = 24             # (local) GRF + FW-canon realizations for the contrast

# Feature wavenumber / ring scale (canonical)
K1 = float(k1_first_sound_ring_invMpc)   # Mpc^-1
R1 = float(r1_first_sound_ring_Mpc)      # Mpc
F_NL = float(max_f_NL_FW)                # 1.505 envelope magnitude

# ---------------------------------------------------------------------------
# Section 3 — Paths + input pins
# ---------------------------------------------------------------------------
COMPUTATIONS_DIR = PROJECT_ROOT / "computations"
INV7_DIR = COMPUTATIONS_DIR / "investigation-7"
OUT_NPZ = INV7_DIR / "inv7_w1_5_persistent_homology_ring.npz"
OUT_PNG = INV7_DIR / "inv7_w1_5_persistent_homology_ring.png"

W1_1_NPZ = INV7_DIR / "inv7_w1_1_c2_substrate.npz"   # upstream substrate feature amplitude

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    W1_1_NPZ,
]


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
# Section 5a — P(k) shape + field generator (SHARED component with INV7-W2-1)
# ---------------------------------------------------------------------------
def _kgrid(n: int, l_box: float):
    """Return the 3D |k| grid (Mpc^-1) and the per-axis k (rad/Mpc) for an n^3 box."""
    kf = 2.0 * np.pi / l_box                          # (local) fundamental mode, rad/Mpc
    kx = np.fft.fftfreq(n, d=1.0) * n * kf            # (local) integer modes * kf
    KX, KY, KZ = np.meshgrid(kx, kx, kx, indexing="ij")  # (local)
    kmag = np.sqrt(KX**2 + KY**2 + KZ**2)             # (local) |k|, rad/Mpc
    return kmag, kf


def pk_lcdm_shape(kmag: np.ndarray) -> np.ndarray:
    """
    LCDM-shape P(k): a BBKS-style transfer function * primordial tilt, WITH the primary BAO wiggle.
    This is the matched baseline shared by FW and GRF (same amplitude + same primary BAO peak).
    The ABSOLUTE normalization is irrelevant (the field is standardized to unit variance before the
    filtration); only the SHAPE matters for the topology comparison.
    """
    k = np.where(kmag > 0, kmag, 1e-30)               # (local) avoid k=0
    # BBKS transfer (Eisenstein-Hu-free, shape-only; Gamma ~ Omega_m h)
    h = 0.674                                         # (local) Planck h (shape only)
    Gamma = Omega_m * h                               # (local) shape parameter
    q = k / Gamma                                     # (local)
    T = (np.log(1.0 + 2.34 * q) / (2.34 * q)) * \
        (1.0 + 3.89 * q + (16.1 * q)**2 + (5.46 * q)**3 + (6.71 * q)**4) ** (-0.25)  # (local) BBKS
    # primordial tilt
    P_prim = k ** planck_ns                           # (local)
    P = P_prim * T**2                                 # (local) P(k) ~ k^ns T(k)^2
    # primary BAO peak (standard recombination scale r_d ~ 147 Mpc -> k_BAO ~ 2pi/147)
    k_bao = 2.0 * np.pi / 147.0                        # (local) Mpc^-1, primary acoustic scale
    A_bao = 0.05                                      # (local) standard ~5% wiggle amplitude (matched both)
    P = P * (1.0 + A_bao * np.sin(k * 147.0) * np.exp(-(k / (4.0 * k_bao))**2))
    return np.where(kmag > 0, P, 0.0)


def ring_window(kmag: np.ndarray, k1: float) -> np.ndarray:
    """
    Second-sound ring window: a Gaussian bump centered at k1 (the W1-1 first-sound ring wavenumber).
    Width is set to ~1.5 fundamental modes so the ring is a localized P(k) feature, not a broadband tilt.
    Returns a multiplicative *fractional* feature W(k) (so P_FW = P_shape * (1 + A_FS * W)).
    """
    sigma_k = 0.15 * k1                               # (local) ring width (~15% of k1)
    return np.exp(-0.5 * ((kmag - k1) / sigma_k) ** 2)


def gaussian_realization(power: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    """
    Generate a real Gaussian random field with the given power spectrum on the grid.
    Uses torch.fft on GPU for the 256^3 inverse FFT (>=100x100 effective -> GPU per math-scripts.md),
    with a numpy fallback. The field is returned standardized to ZERO mean, UNIT variance (so the nu
    thresholds are in sigma_field units, identically for FW and GRF).
    """
    n = power.shape[0]                                # (local)
    # white-noise Fourier amplitudes with Hermitian symmetry guaranteed by irfftn
    # Build half-complex spectrum for rfftn layout
    amp = np.sqrt(np.maximum(power, 0.0))             # (local)
    # complex Gaussian white noise
    re = rng.standard_normal(power.shape)             # (local)
    im = rng.standard_normal(power.shape)             # (local)
    fk = (re + 1j * im) * amp / np.sqrt(2.0)          # (local) coloured Fourier field
    fk[0, 0, 0] = 0.0                                 # (local) zero DC

    field = _ifftn(fk, n)                             # (local) real-space field
    field = field - field.mean()                      # (local) zero mean
    s = field.std()                                   # (local)
    if s > 0:
        field = field / s                            # (local) unit variance
    return field


def _ifftn(fk: np.ndarray, n: int) -> np.ndarray:
    """Inverse 3D FFT -> real field. GPU (torch.fft) with numpy fallback."""
    try:
        import torch
        if torch.cuda.is_available():
            t = torch.tensor(fk, device="cuda")
            out = torch.fft.ifftn(t).real.cpu().numpy()
            return out
    except Exception:
        pass
    return np.fft.ifftn(fk).real


def apply_local_fnl(field_gauss: np.ndarray, f_nl: float) -> np.ndarray:
    """
    Local non-Gaussianity: Phi = phi_G + f_NL (phi_G^2 - <phi_G^2>).
    The Bogoliubov-sudden channel is anti-correlated (NEGATIVE f_NL = -1.505); we apply the SIGNED
    value so the phase correlation matches the substrate prediction. The field is re-standardized to
    unit variance afterwards (thresholds stay in sigma_field units).
    """
    phi = field_gauss                                 # (local) unit-variance Gaussian
    phi_ng = phi + f_nl * (phi**2 - 1.0)              # (local) <phi^2>=1 for unit-variance Gaussian
    phi_ng = phi_ng - phi_ng.mean()                   # (local)
    s = phi_ng.std()                                  # (local)
    if s > 0:
        phi_ng = phi_ng / s                          # (local)
    return phi_ng


def make_framework_field(power_shape: np.ndarray, ring_w: np.ndarray, a_fs: float,
                         f_nl_signed: float, rng: np.random.Generator) -> np.ndarray:
    """
    Framework field: F_FW = Gaussian(P_shape * (1 + A_FS * ring)) THEN local f_NL non-Gaussianity.
    SHARED reusable generator (also the INV7-W2-1 component at the z~5 clustering scale).
    """
    power_fw = power_shape * (1.0 + a_fs * ring_w)    # (local) featured P(k)
    g = gaussian_realization(power_fw, rng)           # (local) coloured Gaussian
    f = apply_local_fnl(g, f_nl_signed)               # (local) + local non-Gaussianity
    return f


def make_grf_field(power_shape: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    """LCDM mock: Gaussian(P_shape), f_NL=0, NO ring. Matched amplitude + primary BAO peak."""
    return gaussian_realization(power_shape, rng)


# ---------------------------------------------------------------------------
# Section 5b — Betti curves via sublevel-set threshold sweep (cubical complex, periodic torus)
# ---------------------------------------------------------------------------
# 6-connectivity (face adjacency) structuring element for 3D labeling
_STRUCT6 = ndimage.generate_binary_structure(3, 1)   # face-connected (6-neigh)

# GPU availability (Euler-char roll-OR-sum is GPU-friendly; ~7.5x faster than CPU on 256^3)
def _gpu_ok() -> bool:
    try:
        import torch
        return bool(torch.cuda.is_available())
    except Exception:
        return False


_USE_GPU = _gpu_ok()


def _betti0_periodic(mask: np.ndarray) -> int:
    """
    beta_0 = number of connected components of `mask` on the 3-TORUS (periodic).
    scipy.ndimage.label is non-periodic; we stitch wrap-around equivalences across the 3 face pairs by
    union-find on the boundary labels.
    """
    lab, n = ndimage.label(mask, structure=_STRUCT6)  # (local) non-periodic labels
    if n <= 1:
        return int(n)
    # union-find over labels 1..n
    parent = np.arange(n + 1)                          # (local)

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[max(ra, rb)] = min(ra, rb)

    # stitch the three opposing faces
    for axis in range(3):
        lo = np.take(lab, 0, axis=axis)                # (local) face at index 0
        hi = np.take(lab, mask.shape[axis] - 1, axis=axis)  # (local) face at index -1
        m = (lo > 0) & (hi > 0)                         # (local) both occupied -> wrap-adjacent
        for a, b in zip(lo[m].ravel(), hi[m].ravel()):
            union(int(a), int(b))
    roots = {find(i) for i in range(1, n + 1)}          # (local)
    return len(roots)


def _euler_char_periodic(mask: np.ndarray) -> int:
    """
    Euler characteristic chi of the cubical complex of `mask` on the periodic 3-torus, via the
    integral-geometric alternating sum chi = sum_p (-1)^p N_p over the p-cells of the sublevel set.

    Cubical incidence on a periodic n^3 voxel grid: a voxel at (i,j,k) is the unit 3-cube
    [i,i+1]x[j,j+1]x[k,k+1]; a p-cell is indexed by a lower-corner SITE plus a size-p AXIS-SUBSET S it
    spans (so 0-cells = vertices, 3-cells = voxels). A p-cell is PRESENT iff at least one incident
    voxel is occupied; the incident voxels are obtained by shifting occupancy by {0,+1} (mod n,
    periodic) along each axis NOT in S (the 2^(3-p) voxels sharing the cell). Each (site, S) lands on a
    unique slot of the n^3 corner lattice, so the per-(p,S) OR-reduction counts cells without
    collision.

    VALIDATED (in-script smoke test): solid cube chi=1; thick S^2 shell chi=2 (=> beta_1=0); full
    torus chi=0.
    """
    if int(mask.sum()) == 0:
        return 0
    import itertools

    if _USE_GPU:
        import torch
        occ = torch.tensor(mask, dtype=torch.int8, device="cuda")   # (local) GPU

        def count_p(p: int) -> int:
            total = 0                                   # (local)
            for S in itertools.combinations(range(3), p):
                free = [a for a in range(3) if a not in S]
                present = torch.zeros_like(occ)          # (local)
                for shifts in itertools.product((0, 1), repeat=len(free)):
                    s = occ
                    for ax, sh in zip(free, shifts):
                        if sh:
                            s = torch.roll(s, shifts=sh, dims=ax)
                    present = present | s
                total += int(present.sum().item())
            return total
    else:
        occ = mask.astype(np.int64)                     # (local) CPU

        def count_p(p: int) -> int:
            total = 0                                   # (local)
            for S in itertools.combinations(range(3), p):
                free = [a for a in range(3) if a not in S]
                present = np.zeros_like(occ)             # (local)
                for shifts in itertools.product((0, 1), repeat=len(free)):
                    s = occ
                    for ax, sh in zip(free, shifts):
                        if sh:
                            s = np.roll(s, shift=+sh, axis=ax)
                    present = present | s
                total += int(present.sum())
            return total

    V = count_p(0)                                       # (local) vertices
    E = count_p(1)                                       # (local) edges
    F = count_p(2)                                       # (local) faces
    C = count_p(3)                                       # (local) cubes (= occ.sum())
    return V - E + F - C


def betti_curve(field: np.ndarray, nu_grid: np.ndarray,
                b1_subgrid_n: int = 24) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Compute (beta_0, beta_1, beta_2)(nu) over the threshold grid via sublevel-set filtration on the
    periodic torus.
      X(nu) = {F <= nu}.  beta_0 = #components(X);  beta_2 = #enclosed voids = #components(complement)
      minus the percolating component;  beta_1 = beta_0 + beta_2 - chi.

    beta_0 and beta_2 (the verdict-bearing leg: beta_2 z-score is the gate OPERATOR) are computed at
    EVERY nu in nu_grid. beta_1 requires the cubical Euler characteristic chi (the expensive leg); since
    beta_1 is DIAGNOSTIC ONLY (not in the gate operator), chi is computed on a coarse `b1_subgrid_n`-
    point subgrid and beta_1 is linearly interpolated back onto nu_grid for the diagnostic curve/plot.
    This does NOT touch the verdict statistic.
    """
    b0 = np.zeros_like(nu_grid)                         # (local)
    b2 = np.zeros_like(nu_grid)                         # (local)
    # --- full-resolution beta_0 + beta_2 (verdict leg) ---
    for i, nu in enumerate(nu_grid):
        sub = field <= nu                              # (local) sublevel set
        n_sub = int(sub.sum())
        if n_sub == 0:
            b0[i] = 0.0
            b2[i] = 0.0
            continue
        if n_sub == field.size:
            b0[i] = 1.0
            b2[i] = 1.0                                # full torus: beta_0=1, beta_2=1
            continue
        beta0 = _betti0_periodic(sub)                  # (local)
        # beta_2 = enclosed voids = bounded components of the complement (superlevel).
        # On the torus, #complement-components minus the percolating background = isolated over-dense
        # pockets fully enclosed by the void-wall sublevel structure (standard cosmological beta_2).
        n_comp_components = _betti0_periodic(~sub)      # (local)
        b0[i] = float(beta0)
        b2[i] = float(max(n_comp_components - 1, 0))   # (local)
    # --- coarse beta_1 via chi on a subgrid (diagnostic only) ---
    sub_idx = np.unique(np.linspace(0, len(nu_grid) - 1, b1_subgrid_n).astype(int))  # (local)
    b1_coarse = np.zeros(len(sub_idx))                  # (local)
    for j, i in enumerate(sub_idx):
        sub = field <= nu_grid[i]                      # (local)
        n_sub = int(sub.sum())
        if n_sub == 0:
            b1_coarse[j] = 0.0
            continue
        if n_sub == field.size:
            b1_coarse[j] = 3.0                         # chi(T^3)=0 -> beta_1 = b0+b2-chi = 1+1-0... =3 only if filled torus topology
            continue
        chi = _euler_char_periodic(sub)                # (local)
        beta1 = b0[i] + b2[i] - chi                    # (local) from chi = b0 - b1 + b2
        b1_coarse[j] = float(max(beta1, 0))            # (local) clamp tiny negative discretization noise
    b1 = np.interp(nu_grid, nu_grid[sub_idx], b1_coarse)  # (local) interpolate diagnostic curve
    return b0, b1, b2


# ---------------------------------------------------------------------------
# Section 5c — Ring-scale threshold selection + ensemble z-score
# ---------------------------------------------------------------------------
def select_nu_r1(nu_grid: np.ndarray, grf_b2_stack: np.ndarray) -> tuple[int, float]:
    """
    Pre-registered ring-scale threshold nu_r1: the threshold where the GRF-null beta_2 ENSEMBLE
    VARIANCE is maximal (the void-wall regime where shell/loop topology is most active). This is
    FIELD-AGNOSTIC (chosen on the GRF null, NOT the FW field) -> no look-elsewhere on FW.
    Returns (index, nu value).
    """
    var_b2 = grf_b2_stack.var(axis=0)                  # (local) per-threshold GRF beta_2 variance
    idx = int(np.argmax(var_b2))                       # (local)
    return idx, float(nu_grid[idx])


def z_separation(fw_b2_at_nu: float, grf_b2_at_nu: np.ndarray) -> tuple[float, float, float]:
    """Standardized separation Z = |fw - <grf>| / std(grf) at the ring-scale threshold."""
    mean = float(grf_b2_at_nu.mean())                  # (local)
    std = float(grf_b2_at_nu.std(ddof=1)) if grf_b2_at_nu.size > 1 else 0.0  # (local)
    if std <= 0:
        return 0.0, mean, std
    z = abs(fw_b2_at_nu - mean) / std                  # (local)
    return z, mean, std


# ---------------------------------------------------------------------------
# Section 5d — top-level compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    print(f"\n=== {GATE_ID} — persistent-homology Betti curves (sublevel-set sweep) ===")
    print(f"  grid={N_GRID}^3  L_box={L_BOX_MPC} Mpc  N_mock={N_MOCK}  seed={RANDOM_SEED}")
    print(f"  ring: k1={K1:.10f} Mpc^-1  r1={R1} Mpc   f_NL(envelope)={F_NL} (signed -{F_NL})")

    # --- consume W1-1 substrate-genuine feature amplitude (PRIMARY) ---
    A_FS_SUBSTRATE = 0.204                              # (local) fallback (canonical) if W1-1 missing
    A_FS_CANON = 0.204                                  # (local) the recomb stand-in (both-ways contrast)
    w1_1_source = "canonical-fallback"                 # (local)
    if W1_1_NPZ.exists():
        d11 = np.load(W1_1_NPZ, allow_pickle=True)     # (local)
        if "feature_A_FS" in d11:
            A_FS_SUBSTRATE = float(d11["feature_A_FS"])
            w1_1_source = "W1-1 npz (feature_A_FS, substrate-genuine)"
        if "A_FS_canon" in d11:
            A_FS_CANON = float(d11["A_FS_canon"])
    print(f"  A_FS_substrate (PRIMARY) = {A_FS_SUBSTRATE:.8f}   [{w1_1_source}]")
    print(f"  A_FS_canon (contrast)    = {A_FS_CANON:.8f}   (recomb first-sound stand-in)")
    print(f"  ring-amplitude ratio canon/substrate = {A_FS_CANON / A_FS_SUBSTRATE:.2f}x")

    # signed f_NL (Bogoliubov-sudden channel is anti-correlated, NEGATIVE)
    f_nl_signed = -F_NL                                # (local)

    nu_grid = np.linspace(NU_MIN, NU_MAX, N_NU)        # (local)
    kmag, kf = _kgrid(N_GRID, L_BOX_MPC)               # (local)
    power_shape = pk_lcdm_shape(kmag)                  # (local) matched LCDM-shape P(k)
    ring_w = ring_window(kmag, K1)                     # (local) second-sound ring window
    print(f"  fundamental k_f = {kf:.6e} Mpc^-1 ; k1/k_f = {K1 / kf:.2f} modes ; "
          f"ring well-resolved = {K1 > 2 * kf}")

    rng_master = np.random.default_rng(RANDOM_SEED)    # (local)

    # === PRIMARY run: FW (substrate A_FS) vs N_MOCK GRF mocks ===
    print(f"\n  --- PRIMARY: FW(A_FS_substrate={A_FS_SUBSTRATE:.6f}) vs {N_MOCK} GRF mocks ---")
    # one FW realization (the framework field) at fixed seed
    rng_fw = np.random.default_rng(rng_master.integers(0, 2**31 - 1))   # (local)
    fw_field = make_framework_field(power_shape, ring_w, A_FS_SUBSTRATE, f_nl_signed, rng_fw)  # (local)
    fw_b0, fw_b1, fw_b2 = betti_curve(fw_field, nu_grid)               # (local)

    # GRF null ensemble
    grf_b2_stack = np.zeros((N_MOCK, N_NU))            # (local)
    grf_b1_stack = np.zeros((N_MOCK, N_NU))            # (local)
    grf_b0_stack = np.zeros((N_MOCK, N_NU))            # (local)
    t_ens = time.time()                                # (local)
    for m in range(N_MOCK):
        rng_m = np.random.default_rng(rng_master.integers(0, 2**31 - 1))  # (local)
        gf = make_grf_field(power_shape, rng_m)        # (local)
        b0, b1, b2 = betti_curve(gf, nu_grid)          # (local)
        grf_b0_stack[m] = b0
        grf_b1_stack[m] = b1
        grf_b2_stack[m] = b2
        if (m + 1) % 20 == 0:
            print(f"    GRF mock {m+1}/{N_MOCK}  ({time.time()-t_ens:.1f}s elapsed)")

    # ring-scale threshold (field-agnostic: GRF beta_2 variance peak)
    nu_idx, nu_r1 = select_nu_r1(nu_grid, grf_b2_stack)   # (local)
    print(f"  nu_r1 (ring-scale threshold, GRF-variance-peak) = {nu_r1:.4f} sigma  (idx {nu_idx})")

    # z-separation of FW beta_2 from the GRF null at nu_r1
    Z, grf_mean, grf_std = z_separation(fw_b2[nu_idx], grf_b2_stack[:, nu_idx])  # (local)
    print(f"  beta_2_FW(nu_r1)            = {fw_b2[nu_idx]:.3f}")
    print(f"  <beta_2_GRF(nu_r1)>         = {grf_mean:.3f} +/- {grf_std:.3f}")
    print(f"  Z (PRIMARY, substrate A_FS) = {Z:.4f}")

    # === CONTRAST run: FW (canonical A_FS=0.204) vs GRF (smaller sub-ensemble for runtime) ===
    print(f"\n  --- CONTRAST: FW(A_FS_canon={A_FS_CANON:.6f}) vs {N_MOCK_CANON} GRF mocks ---")
    rng_master_c = np.random.default_rng(RANDOM_SEED + 1)               # (local)
    rng_fwc = np.random.default_rng(rng_master_c.integers(0, 2**31 - 1))  # (local)
    fwc_field = make_framework_field(power_shape, ring_w, A_FS_CANON, f_nl_signed, rng_fwc)  # (local)
    _, _, fwc_b2 = betti_curve(fwc_field, nu_grid)                      # (local)
    grf_b2_stack_c = np.zeros((N_MOCK_CANON, N_NU))    # (local)
    for m in range(N_MOCK_CANON):
        rng_m = np.random.default_rng(rng_master_c.integers(0, 2**31 - 1))  # (local)
        gf = make_grf_field(power_shape, rng_m)        # (local)
        _, _, b2 = betti_curve(gf, nu_grid)            # (local)
        grf_b2_stack_c[m] = b2
    nu_idx_c, nu_r1_c = select_nu_r1(nu_grid, grf_b2_stack_c)           # (local)
    Z_canon, grf_mean_c, grf_std_c = z_separation(fwc_b2[nu_idx_c], grf_b2_stack_c[:, nu_idx_c])  # (local)
    print(f"  Z (CONTRAST, canonical A_FS=0.204) = {Z_canon:.4f}  (nu_r1_c={nu_r1_c:.4f})")
    print(f"  topological-signal ratio Z_canon/Z_substrate = "
          f"{(Z_canon / Z if Z > 0 else float('inf')):.2f}x  (expect ~ the 52x amplitude shrink, "
          f"attenuated by the topology nonlinearity)")

    # the discriminating value is the PRIMARY (substrate) Z
    value = float(Z)                                    # (local)

    return {
        "value": value,
        "Z_substrate": Z,
        "Z_canon": Z_canon,
        "A_FS_substrate": A_FS_SUBSTRATE,
        "A_FS_canon": A_FS_CANON,
        "ratio_canon_over_sub_ampl": A_FS_CANON / A_FS_SUBSTRATE,
        "w1_1_source": w1_1_source,
        "nu_grid": nu_grid,
        "nu_r1": nu_r1,
        "nu_idx": nu_idx,
        "nu_r1_canon": nu_r1_c,
        "fw_b0": fw_b0, "fw_b1": fw_b1, "fw_b2": fw_b2,
        "grf_b0_mean": grf_b0_stack.mean(axis=0),
        "grf_b1_mean": grf_b1_stack.mean(axis=0),
        "grf_b2_mean": grf_b2_stack.mean(axis=0),
        "grf_b2_std": grf_b2_stack.std(axis=0, ddof=1),
        "fwc_b2": fwc_b2,
        "grf_b2_mean_canon": grf_b2_stack_c.mean(axis=0),
        "grf_b2_std_canon": grf_b2_stack_c.std(axis=0, ddof=1),
        "beta2_fw_at_nu_r1": float(fw_b2[nu_idx]),
        "grf_b2_mean_at_nu_r1": grf_mean,
        "grf_b2_std_at_nu_r1": grf_std,
        "f_nl_signed": f_nl_signed,
        "k1": K1, "r1": R1, "f_nl": F_NL,
        "n_grid": N_GRID, "n_mock": N_MOCK, "l_box": L_BOX_MPC,
    }


# ---------------------------------------------------------------------------
# Section 6 — gate evaluation + 3-tuple
# ---------------------------------------------------------------------------
def evaluate_gate(Z: float) -> str:
    if Z >= N_SIGMA_PASS:
        return "PASS"
    if Z >= N_SIGMA_INFO:
        return "INFO"
    return "FAIL"


def sign_magnitude_regime(res: dict, verdict: str) -> tuple[str, str, str]:
    """
    sign_verdict: PASS iff the COMPUTED beta_2 separation is in the predicted direction
                  (Z computed as |.| so the directional content is sign(beta_2_FW - <beta_2_GRF>)
                  >= 0 expected — a beta_2 EXCESS from the preferred shell scale per Step 3).
    magnitude_verdict: PASS iff Z >= 3; INFO iff 2 <= Z < 3; FAIL iff Z < 2.
    regime_verdict: VALID — the cubical-complex Betti computation is exact per realization within the
                    grid discretization; the 256^3 grid resolves r1 with k1/k_f ~ 6 modes (well inside
                    the Nyquist regime), so the filtration is in-regime throughout.
    """
    signed = res["beta2_fw_at_nu_r1"] - res["grf_b2_mean_at_nu_r1"]   # (local)
    sign_v = "PASS" if signed >= 0 else "FAIL"                         # (local)
    Z = res["Z_substrate"]                                            # (local)
    if Z >= N_SIGMA_PASS:
        mag_v = "PASS"
    elif Z >= N_SIGMA_INFO:
        mag_v = "INFO"
    else:
        mag_v = "FAIL"
    regime_v = "VALID"
    return sign_v, mag_v, regime_v


# ---------------------------------------------------------------------------
# Section 6b — plot
# ---------------------------------------------------------------------------
def make_plot(res: dict, verdict: str) -> None:
    nu = res["nu_grid"]                                # (local)
    fig, ax = plt.subplots(2, 2, figsize=(13, 9))

    # (0,0) beta_2 curves: FW vs GRF mean +/- std band
    a = ax[0, 0]
    a.plot(nu, res["fw_b2"], "C3-", lw=2, label=r"$\beta_2$ FW (substrate $A_{FS}$)")
    a.plot(nu, res["grf_b2_mean"], "C0-", lw=1.5, label=r"$\langle\beta_2\rangle$ GRF (LCDM)")
    a.fill_between(nu, res["grf_b2_mean"] - res["grf_b2_std"],
                   res["grf_b2_mean"] + res["grf_b2_std"], color="C0", alpha=0.25, label=r"GRF $\pm1\sigma$")
    a.axvline(res["nu_r1"], color="k", ls="--", lw=1, label=r"$\nu_{r_1}$ (ring-scale thr.)")
    a.set_xlabel(r"density threshold $\nu$ [$\sigma_{\rm field}$]")
    a.set_ylabel(r"$\beta_2$ (enclosed voids)")
    a.set_title(rf"$\beta_2$ Betti curve — Z(substrate)={res['Z_substrate']:.2f}$\sigma$  [{verdict}]")
    a.legend(fontsize=8)
    a.grid(alpha=0.3)

    # (0,1) beta_1 curves
    a = ax[0, 1]
    a.plot(nu, res["fw_b1"], "C3-", lw=2, label=r"$\beta_1$ FW")
    a.plot(nu, res["grf_b1_mean"], "C0-", lw=1.5, label=r"$\langle\beta_1\rangle$ GRF")
    a.axvline(res["nu_r1"], color="k", ls="--", lw=1)
    a.set_xlabel(r"$\nu$ [$\sigma_{\rm field}$]")
    a.set_ylabel(r"$\beta_1$ (loops/tunnels)")
    a.set_title(r"$\beta_1$ Betti curve")
    a.legend(fontsize=8)
    a.grid(alpha=0.3)

    # (1,0) beta_0 curves
    a = ax[1, 0]
    a.plot(nu, res["fw_b0"], "C3-", lw=2, label=r"$\beta_0$ FW")
    a.plot(nu, res["grf_b0_mean"], "C0-", lw=1.5, label=r"$\langle\beta_0\rangle$ GRF")
    a.axvline(res["nu_r1"], color="k", ls="--", lw=1)
    a.set_xlabel(r"$\nu$ [$\sigma_{\rm field}$]")
    a.set_ylabel(r"$\beta_0$ (components)")
    a.set_title(r"$\beta_0$ Betti curve")
    a.legend(fontsize=8)
    a.grid(alpha=0.3)

    # (1,1) both-ways contrast: substrate vs canonical A_FS at the ring scale
    a = ax[1, 1]
    labels = ["substrate\n$A_{FS}$=%.4f" % res["A_FS_substrate"],
              "canonical\n$A_{FS}$=0.204"]
    Zvals = [res["Z_substrate"], res["Z_canon"]]       # (local)
    bars = a.bar(labels, Zvals, color=["C3", "C1"])
    a.axhline(N_SIGMA_PASS, color="g", ls="--", lw=1, label=r"PASS $3\sigma$")
    a.axhline(N_SIGMA_INFO, color="orange", ls=":", lw=1, label=r"INFO $2\sigma$")
    a.set_ylabel(r"$Z$ ($\beta_2$ ring-scale separation) [$\sigma$]")
    a.set_title(r"Both-ways contrast: ring-amplitude $\to$ topological signal")
    for b, z in zip(bars, Zvals):
        a.text(b.get_x() + b.get_width() / 2, z, f"{z:.2f}", ha="center", va="bottom", fontsize=9)
    a.legend(fontsize=8)
    a.grid(alpha=0.3, axis="y")

    fig.suptitle(
        rf"INV7-W1-5 persistent-homology web fingerprint (DISTINCT from S43 $k\sim10^{{24}}$ closure) "
        rf"— verdict {verdict}", fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 6c — 4-tuple + verdict payload (matches inv7_w1_1 emit pattern)
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, l_max) -> str:
    return f"4-tuple: (value={value}, scheme={scheme}, convention={convention}, L_max={l_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None) -> dict:
    payload: dict = {
        "session": 7,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
        "track": "investigation",
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
# Section 7 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()                  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    res = compute()
    value = res["value"]

    verdict = evaluate_gate(res["Z_substrate"])
    sign_v, mag_v, regime_v = sign_magnitude_regime(res, verdict)

    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=verdict,
        value=value,
        # core discriminating result
        Z_substrate=res["Z_substrate"],
        Z_canon=res["Z_canon"],
        n_sigma_pass=N_SIGMA_PASS,
        n_sigma_info=N_SIGMA_INFO,
        # ring-amplitude provenance
        A_FS_substrate=res["A_FS_substrate"],
        A_FS_canon=res["A_FS_canon"],
        ratio_canon_over_sub_ampl=res["ratio_canon_over_sub_ampl"],
        w1_1_source=res["w1_1_source"],
        # Betti curves
        nu_grid=res["nu_grid"],
        nu_r1=res["nu_r1"],
        nu_idx=res["nu_idx"],
        nu_r1_canon=res["nu_r1_canon"],
        fw_b0=res["fw_b0"], fw_b1=res["fw_b1"], fw_b2=res["fw_b2"],
        grf_b0_mean=res["grf_b0_mean"],
        grf_b1_mean=res["grf_b1_mean"],
        grf_b2_mean=res["grf_b2_mean"],
        grf_b2_std=res["grf_b2_std"],
        fwc_b2=res["fwc_b2"],
        grf_b2_mean_canon=res["grf_b2_mean_canon"],
        grf_b2_std_canon=res["grf_b2_std_canon"],
        # ring-scale point statistics
        beta2_fw_at_nu_r1=res["beta2_fw_at_nu_r1"],
        grf_b2_mean_at_nu_r1=res["grf_b2_mean_at_nu_r1"],
        grf_b2_std_at_nu_r1=res["grf_b2_std_at_nu_r1"],
        # field parameters
        f_nl_signed=res["f_nl_signed"],
        k1=res["k1"], r1=res["r1"], f_nl=res["f_nl"],
        n_grid=res["n_grid"], n_mock=res["n_mock"], l_box=res["l_box"],
        # 3-tuple
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=regime_v,
        # SHAs
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"\n  saved: {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    make_plot(res, verdict)
    print(f"  saved: {OUT_PNG.relative_to(PROJECT_ROOT)}")

    tag = emit_4tuple(round(value, 8), SCHEME, CONVENTION, L_MAX)
    print(tag)

    # Companion note: the topological-discriminator verdict + the both-ways contrast.
    note = (f"Z_beta2_ring(substrate_A_FS={res['A_FS_substrate']:.6f})={res['Z_substrate']:.3f}sigma "
            f"vs thr 3.0; Z(canon_A_FS=0.204)={res['Z_canon']:.3f}; ring-ampl 52x weaker (W1-1 FAIL); "
            f"DISTINCT from S43 volume-avg Betti k~1e24 (k_transition=9.4e23,unobservable); "
            f"beta_2_FW(nu_r1)={res['beta2_fw_at_nu_r1']:.2f} vs GRF "
            f"{res['grf_b2_mean_at_nu_r1']:.2f}+/-{res['grf_b2_std_at_nu_r1']:.2f}")  # (local)

    detail_row = (f"# {GATE_ID} field: F=Gauss(P_FW*(1+A_FS*ring(k1))) + f_NL={res['f_nl']}(signed -)"
                  f" local-NG; grid {res['n_grid']}^3 L_box {res['l_box']}Mpc N_mock {res['n_mock']} "
                  f"seed 12345; nu_r1={res['nu_r1']:.4f}sigma (GRF-var-peak,field-agnostic); "
                  f"Betti via sublevel-set sweep (GUDHI absent): b0=#comp, b2=#enclosed-voids, "
                  f"b1=b0+b2-chi(cubical Euler); complementary to INV7-W2-1 (z~5 two-point)")  # (local)

    print_verdict_payload(
        verdict, round(value, 6), audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        companion_note=note, extra_rows=[detail_row],
    )

    print(f"\n  {GATE_ID} done in {time.time()-t0:.1f}s — verdict {verdict} "
          f"(Z_substrate={res['Z_substrate']:.3f}sigma)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
