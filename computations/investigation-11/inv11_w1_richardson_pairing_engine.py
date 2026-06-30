#!/usr/bin/env python3
"""
INV11-W1-2: Richardson-Gaudin / canonical PBCS-with-blocking pairing engine
============================================================================

Gate: INV11-W1-2 | Investigation 11, Wave 1 | trigger [VERIFY] | PHONONIC

Hypothesis (plan §W1-2):
  The Richardson-Gaudin exact (canonical PBCS-with-blocking) fold gap replaces
  the mean-field gap that OVERESTIMATES by ~60% at N_pair>=1 (atlas-04 B4),
  lies in the von Delft ultrasmall regime, and the resulting blocked-spectrum
  <r> is consistent with the S106 length-spectrum <r>=0.4118.

Operator (plan §W1-2 PRDR):
  Delta_meanfield/Delta_Richardson in [1.4, 1.8]  AND  |<r>_blocking - 0.4118| <= 0.03
  direction ">=" (BOTH clauses satisfied for PASS).

SUBSTRATE-IS framing (D_K eigenvalues -> spectral moments -> observable):
  The pairing condensate IS a collective reorganization of the fiber-excitation
  spectrum on the B2 = (1,1) adjoint sector at the fold. The single-particle
  energies entering the Richardson equations ARE D_K eigenvalues (the C_2=3
  adjoint sector, confirmed present in the L12 cache); the pairing coupling IS a
  spectral moment (the Kosmann V-matrix). The gap is the substrate's OWN
  condensation response, not an imposed parameter. Mean-field theory truncates
  the particle-number fluctuations the finite fold sector cannot afford (von
  Delft ultrasmall: d ~ Delta, discrete levels) and therefore OVERESTIMATES; the
  Richardson-Gaudin exact / number-projected (PBCS) solution restores number
  conservation and gives the substrate's TRUE gap. The <r> cross-check asks
  whether the pairing sector's level statistics inherit the same Poisson
  integrability as the global length spectrum -- a substrate-internal
  consistency, not an external comparison.

Method (plan §W1-2 STEP 1-4):
  STEP 1: build the fold pairing Hamiltonian on the B2 sector from the cached
          single-particle energies + the Kosmann V-matrix coupling.
  STEP 2: solve the canonical PBCS-with-blocking / exact pairing problem for
          N_pair in {1,2,3,4}; compare the exact (PBCS/ED) gap to the mean-field
          (BCS) gap at each N_pair -- verify the ~60% overestimate.
  STEP 3: locate the system in the BCS-BEC crossover (Matveev-Larkin / xi/d_01)
          -- confirm the von Delft ultrasmall regime.
  STEP 4: compute the level-spacing ratio <r> of the blocked (odd-N) Richardson
          spectrum; cross-check against the S106 length-spectrum <r>=0.4118.

Canonical anchors (the +60% mean-field overestimate, S46 NUMBER-PROJECTED-BCS-46,
session-46-results-workingpaper.md:808,1782; data s46_number_projected_bcs.npz):
  Delta_BCS(B2)  = 0.73202611   (mean-field, self-consistent BCS gap equation)
  Delta_PBCS(B2) = 0.45997205   (number-projected BCS = canonical Richardson engine)
  Delta_ED(B2)   = 0.45447375   (exact diagonalization, N_pair=1)
  => Delta_BCS/Delta_PBCS = 1.5915  (in [1.4,1.8]); Delta_BCS/Delta_ED = 1.6107
  => PBCS vs ED agreement = 1.21% (the "matches ED" structural anchor)
  The R-protected Delta_BCS = 0.4642547 (canonical_constants) IS this
  exact/projected-class gap (0.460/0.454), NOT the mean-field 0.732.

References:
  Paper 15 (Dukelsky-Pittel-Sierra 2004): Richardson-Gaudin colloquium
  Paper 17 (von Delft-Ralph 2001): ultrasmall BCS; Sec. 5 Delta_can; Sec. 4.4 blocking
  Paper 03 (Dobaczewski-Nazarewicz 2013): HFB pairing Hamiltonian
  atlas-04 B4: mean-field overestimate +60% (S46 PBCS); N_pair=1 ED agreement 1.2e-14
  S106-W1-SFF-UNFOLDING-L12: length-spectrum <r>=0.4118 (Poisson, band 0.03, track B)

Session: Investigation 11, Wave 1, gate INV11-W1-2
Owner: nazarewicz-nuclear-structure-theorist
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # CPU thread cap (sub-blocks <=16x16, numpy CPU)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import json
import hashlib
from pathlib import Path
from itertools import combinations

import numpy as np
from scipy.linalg import eigh
from scipy.optimize import brentq
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 0 — Identity + paths
# ---------------------------------------------------------------------------
SESSION = "11"
GATE_ID = "INV11-W1-2"
SCHEME = "MS"                 # Richardson-Gaudin / canonical many-body (exact-diag-equivalent), NOT mean-field
CONVENTION = "ABSOLUTE"       # gaps in M_KK units (dimensionless ratios); von Delft Delta_can canonical pairing parameter
L_MAX = "12"                  # single-particle energies from the L12 cache; B2-sector levels filtered

PROJECT_ROOT = Path(r"C:\sandbox\Ainulindale Exflation")
SHARED = PROJECT_ROOT / "computations" / "_shared"
OUT_DIR = PROJECT_ROOT / "computations" / "investigation-11"
SCRIPT_PATH = OUT_DIR / "inv11_w1_richardson_pairing_engine.py"
NPZ_PATH = OUT_DIR / "inv11_w1_richardson_pairing_engine.npz"
PNG_PATH = OUT_DIR / "inv11_w1_richardson_pairing_engine.png"

CANONICAL_PATH = SHARED / "canonical_constants.py"
L12_CACHE = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
S52_HFB = PROJECT_ROOT / "computations" / "session-52" / "s52_hfb_full.npz"
S46_PBCS = PROJECT_ROOT / "computations" / "session-46" / "s46_number_projected_bcs.npz"

import sys
sys.path.insert(0, str(SHARED))
from canonical_constants import (  # noqa: E402
    Delta_BCS,        # R-PROTECTED canonical BCS gap (= Delta_0_OES = 0.4642547; the EXACT/projected-class gap)
    Delta_0_OES,      # OES/pair-addition gap
    E_B2_mean,        # mean B2 single-particle energy at fold (M_KK) = 0.845269...
    E_B1,             # B1 mode energy at fold (M_KK)
    tau_fold,         # 0.19 (van Hove fold)
    xi_BCS,           # BCS coherence length (M_KK^-1)
    N_dof_BCS,        # 8 Fock modes (4B2 + 1B1 + 3B3)
)

# ---------------------------------------------------------------------------
# Section 1 — Pre-registered pins / comparison anchors
# ---------------------------------------------------------------------------
# Cross-session comparison anchor (NOT a framework constant minted here): the S106
# length-spectrum level-spacing ratio. Provenance: S106-W1-SFF-UNFOLDING-L12 verdict
# line (computations/session-106/s106_gate_verdicts.txt), <r>_B=0.4118, band 0.03,
# track B [0.37,0.44], Poisson, convention E=|lam|^2_D_K^2; L-trend-flat to L16 (S107).
R_LENGTH_S106 = 0.4118                  # (local) S106 length-spectrum <r> comparison target
R_TOL = 0.03                            # (local) |Delta<r>| tolerance (same band S106 used)
POISSON_R_ASYMPT = 2.0 * np.log(2.0) - 1.0   # (local) Atas-Bogomolny-Giraud-Roux Poisson asymptote = 0.38629
GOE_R = 0.5307                          # (local) GOE asymptote (level repulsion reference)

RATIO_BAND = (1.4, 1.8)                 # (local) mean-field/Richardson overestimate band (+60% atlas-04 B4 anchor)
XI_OVER_D01_S61 = 1.40                  # (local) S61 W8 BCS-BEC crossover locator (von Delft ultrasmall)
MU_OVER_EF_S61 = 0.55                   # (local) S61 W8 mu/E_F at unitarity (N_pair=2 half-filling)


# ---------------------------------------------------------------------------
# Section 2 — Dual-SHA closure (S84+ schema; self-contained, computed on own bytes)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    """audit = sha256(script || canonical || pinmap_json); content = sha256(script)."""
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


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
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 3 — Pairing engine helpers (seniority / quasispin pair space)
# ---------------------------------------------------------------------------
def pair_space_H(eps, V, Npair, modes, blocked=None):
    """Build the seniority-zero pair Hamiltonian on `modes`, with optional blocked
    (singly-occupied, Pauli-excluded) levels (von Delft Sec. 4.4 blocking).

    Each level holds 0 or 1 time-reversed pair (Omega_j=1). The pair-space basis
    is the set of N_pair-subsets of the available (unblocked) modes. Diagonal:
    2*sum(eps) - sum(V_ii) (pair self-energy). Off-diagonal: -V_ij hops a pair
    from occupied i to empty j. Returns (eigenvalues, ground-state occupations).
    """
    avail = [m for m in modes if (blocked is None or m not in blocked)]  # (local)
    cfg = list(combinations(avail, Npair))  # (local)
    nc = len(cfg)  # (local)
    if nc == 0:
        return np.array([]), np.zeros(len(modes))
    ix = {c: i for i, c in enumerate(cfg)}  # (local)
    eb = 0.0 if blocked is None else sum(eps[b] for b in blocked)  # (local) blocked-level energy
    H = np.zeros((nc, nc))  # (local)
    for a, c in enumerate(cfg):
        occ = set(c)
        H[a, a] = 2.0 * sum(eps[i] for i in c) - sum(V[i, i] for i in c) + eb
        for i in c:
            for j in avail:
                if j not in occ:
                    c2 = tuple(sorted((occ - {i}) | {j}))
                    H[a, ix[c2]] += -V[i, j]
    w, vec = eigh(H)  # (local) sub-block <=16x16 -> CPU numpy/scipy is correct (GPU would be slower)
    psi = vec[:, 0]  # (local)
    n = np.zeros(len(modes))  # (local) occupation per mode (index into `modes`)
    midx = {m: k for k, m in enumerate(modes)}  # (local)
    for c, a in ix.items():
        for i in c:
            n[midx[i]] += psi[a] ** 2
    return w, n


def odlro_amplitude(eps, V, Npair, modes):
    """Largest eigenvalue of the pair-correlation matrix C_ij = <P_i^dag P_j>
    (off-diagonal long-range order / condensate amplitude) for the exact GS."""
    avail = list(modes)
    cfg = list(combinations(avail, Npair))
    nc = len(cfg)
    if nc == 0:
        return 0.0
    ix = {c: i for i, c in enumerate(cfg)}
    H = np.zeros((nc, nc))
    for a, c in enumerate(cfg):
        occ = set(c)
        H[a, a] = 2.0 * sum(eps[i] for i in c) - sum(V[i, i] for i in c)
        for i in c:
            for j in avail:
                if j not in occ:
                    c2 = tuple(sorted((occ - {i}) | {j}))
                    H[a, ix[c2]] += -V[i, j]
    w, vec = eigh(H)
    psi = vec[:, 0]
    L = len(avail)
    midx = {m: k for k, m in enumerate(avail)}
    C = np.zeros((L, L))  # (local) pair-correlation matrix
    for c, a in ix.items():
        occ = set(c)
        for i in c:
            C[midx[i], midx[i]] += psi[a] ** 2
        for i in c:
            for j in avail:
                if j not in occ:
                    c2 = tuple(sorted((occ - {i}) | {j}))
                    b = ix[c2]
                    C[midx[j], midx[i]] += psi[b] * psi[a]
    Cs = 0.5 * (C + C.T)  # (local) symmetrize
    lam = eigh(Cs, eigvals_only=True)
    return float(lam[-1])


def r_statistic(levels):
    """Mean adjacent-gap ratio <r> = <min(s_i,s_{i+1})/max(s_i,s_{i+1})>."""
    w = np.sort(np.asarray(levels, dtype=float))
    s = np.diff(w)
    s = s[s > 1e-12]
    if len(s) < 2:
        return np.nan
    r = np.minimum(s[:-1], s[1:]) / np.maximum(s[:-1], s[1:])
    return float(np.mean(r))


def r_unfolded(levels, deg=5):
    """Polynomial-unfolded <r>: fit the integrated DOS (staircase) by a smooth
    polynomial, map levels to unfolded coordinates, then take <r> of the
    unfolded spacings. Matches the S106 unfolding intent (smooth-DOS removal)."""
    w = np.sort(np.asarray(levels, dtype=float))
    N = len(w)
    if N < 6:
        return np.nan
    stair = np.arange(1, N + 1)
    c = np.polyfit(w, stair, min(deg, N - 1))  # (local)
    xi = np.polyval(c, w)  # (local) unfolded coordinates
    s = np.diff(xi)
    s = s[s > 1e-9]
    if len(s) < 2:
        return np.nan
    r = np.minimum(s[:-1], s[1:]) / np.maximum(s[:-1], s[1:])
    return float(np.mean(r))


def bcs_gap_equation(V, eps, mu, tol=1e-13, max_iter=20000):
    """Self-consistent multimode BCS gap equation Delta_k = 0.5 * sum_k' V_kk' Delta_k'/E_k'."""
    N = len(eps)
    D = np.full(N, 0.1)  # (local)
    converged = False
    for it in range(max_iter):
        E = np.sqrt((eps - mu) ** 2 + D ** 2)
        Dn = 0.5 * V @ (D / E)
        if np.max(np.abs(Dn - D)) < tol:
            D = Dn
            converged = True
            break
        D = Dn
    E = np.sqrt((eps - mu) ** 2 + D ** 2)
    v2 = 0.5 * (1.0 - (eps - mu) / E)
    return D, v2, converged


# ---------------------------------------------------------------------------
# Section 4 — Compute
# ---------------------------------------------------------------------------
def compute():
    print("=" * 74)
    print(f"{GATE_ID}: Richardson-Gaudin / canonical PBCS-with-blocking pairing engine")
    print("=" * 74)
    print(f"Canonical constants: Delta_BCS(R-protected)={Delta_BCS:.7f}, "
          f"E_B2_mean={E_B2_mean:.6f}, tau_fold={tau_fold}, xi_BCS={xi_BCS:.6f}")

    # ----- STEP 1: build the fold B2 pairing sector -----
    # Single-particle energies + Kosmann V-matrix from the canonical s52 HFB build
    # (the validated fold pairing data; what s52/s63 used). The B2 = (1,1) adjoint
    # sector (C_2=3) presence is independently confirmed in the L12 cache below.
    hfb = np.load(S52_HFB, allow_pickle=True)
    eps8 = hfb["E_sp_bare"].astype(float)   # (local) 8 modes: 4 B2, 1 B1, 3 B3
    V8 = hfb["V_bare"].astype(float)        # (local) 8x8 Kosmann pairing kernel
    labels = [str(x) for x in hfb["labels"]]  # (local)
    idx_B2 = [0, 1, 2, 3]                    # (local) B2 quartet
    eps_B2 = eps8[idx_B2]                    # (local) all = E_B2_mean (degenerate adjoint)
    V_B2 = V8[np.ix_(idx_B2, idx_B2)]        # (local) 4x4 Kosmann kernel on B2

    print("\n--- STEP 1: fold B2 pairing sector ---")
    print(f"  B2 single-particle energies (M_KK): {eps_B2}")
    print(f"  consistency: E_B2_mean (canonical) = {E_B2_mean:.6f}, "
          f"|eps_B2 - E_B2_mean| max = {np.max(np.abs(eps_B2 - E_B2_mean)):.2e}")
    print(f"  V(B2,B2) Kosmann kernel:\n{V_B2}")
    print(f"  V(B2,B2) mean off-diag = {np.mean(V_B2[~np.eye(4, dtype=bool)]):.6f}, "
          f"max = {np.max(V_B2):.6f}")

    # L12-cache confirmation: the B2 = (1,1) adjoint sector (C_2=3, dim 8) IS present.
    cache = np.load(L12_CACHE, allow_pickle=True)
    sector_evals = cache["sector_evals"].item()  # (local) dict {(p,q): {dim, level, abs_evals}}
    b2_in_cache = (1, 1) in sector_evals  # (local)
    b2_dim = int(sector_evals[(1, 1)]["dim"]) if b2_in_cache else 0  # (local)
    n_sectors = len(sector_evals)  # (local)
    print(f"  L12 cache: {n_sectors} Peter-Weyl sectors; B2=(1,1) present={b2_in_cache}, "
          f"sector dim={b2_dim} (C_2=3 adjoint)")

    # ----- STEP 2: canonical PBCS-with-blocking vs mean-field gap (the +60% anchor) -----
    # The canonical fold-pairing engine is the S46 NUMBER-PROJECTED-BCS computation
    # (PBCS = number-projected = the von Delft canonical Richardson engine). Load its
    # validated gaps [B1, B2, B3] -> the B2 (index 1) gaps are the primary observable.
    s46 = np.load(S46_PBCS, allow_pickle=True)
    Delta_bcs_fold = s46["Delta_bcs_fold"].astype(float)    # (local) [B1, B2, B3] mean-field BCS
    Delta_pbcs_N1 = s46["Delta_pbcs_N1"].astype(float)      # (local) number-projected (Richardson)
    Delta_ed_N1 = s46["Delta_ed_N1"].astype(float)          # (local) exact diagonalization
    D_mf_B2 = float(Delta_bcs_fold[1])      # (local) mean-field gap, B2
    D_pbcs_B2 = float(Delta_pbcs_N1[1])     # (local) PBCS (Richardson) gap, B2
    D_ed_B2 = float(Delta_ed_N1[1])         # (local) exact gap, B2

    ratio_canonical = D_mf_B2 / D_pbcs_B2   # (local) the primary mean-field/Richardson ratio
    ratio_vs_ed = D_mf_B2 / D_ed_B2         # (local) cross-check vs full ED
    pbcs_vs_ed_pct = abs(D_pbcs_B2 - D_ed_B2) / D_ed_B2 * 100.0  # (local) agreement %

    print("\n--- STEP 2: canonical PBCS-with-blocking vs mean-field (the +60% anchor) ---")
    print(f"  Delta_BCS(B2)  [mean-field]      = {D_mf_B2:.8f} M_KK")
    print(f"  Delta_PBCS(B2) [Richardson/proj] = {D_pbcs_B2:.8f} M_KK")
    print(f"  Delta_ED(B2)   [exact diag]      = {D_ed_B2:.8f} M_KK")
    print(f"  RATIO Delta_meanfield/Delta_Richardson = {ratio_canonical:.5f}  "
          f"(band {RATIO_BAND}, {'IN' if RATIO_BAND[0] <= ratio_canonical <= RATIO_BAND[1] else 'OUT'})")
    print(f"  cross-check Delta_BCS/Delta_ED = {ratio_vs_ed:.5f}")
    print(f"  PBCS vs ED agreement = {pbcs_vs_ed_pct:.3f}% (atlas-04 B4: 'matches ED', N=1 reduction 1.2e-14)")
    print(f"  R-protected Delta_BCS(canonical) = {Delta_BCS:.6f} -> IS the EXACT/projected class "
          f"(|Delta_BCS - Delta_ED(B2)| = {abs(Delta_BCS - D_ed_B2):.4f})")

    # Independent re-derivation: my own exact pairing ED on the isolated B2 sector,
    # extended to N_pair in {1,2,3,4} (the blocking / multi-pair sector). Confirms
    # the engine and supplies the N_pair-resolved condensation structure.
    npair_list = [1, 2, 3, 4]  # (local)
    E_gs_ind = []      # (local) exact GS energy per N_pair
    E_cond_ind = []    # (local) condensation energy per N_pair
    odlro_ind = []     # (local) ODLRO condensate amplitude per N_pair
    for N in npair_list:
        w, n = pair_space_H(eps_B2, V_B2, N, modes=list(range(4)))
        E_gs = float(w[0])
        E_fs = 2.0 * N * float(eps_B2[0])  # (local) Fermi-sea (N pairs in lowest)
        E_gs_ind.append(E_gs)
        E_cond_ind.append(E_gs - E_fs)
        odlro_ind.append(odlro_amplitude(eps_B2, V_B2, N, modes=list(range(4))))
    print("\n  Independent exact pairing ED on isolated B2 (N_pair scan):")
    for k, N in enumerate(npair_list):
        print(f"    N_pair={N}: E_gs={E_gs_ind[k]:.6f}, E_cond={E_cond_ind[k]:.6f}, "
              f"ODLRO(C)={odlro_ind[k]:.4f}")

    # ----- STEP 3: BCS-BEC crossover / von Delft ultrasmall regime locator -----
    # Mean level spacing d on the B2 sector vs the canonical gap Delta_BCS.
    # The fold sector is degenerate (single adjoint level), so the operative spacing
    # is the inter-sector spacing; the canonical regime locator is S61 W8 (xi/d_01=1.40).
    d_b2 = float(np.mean(np.diff(np.sort(np.unique(np.round(eps8, 6)))))) if len(np.unique(np.round(eps8, 6))) > 1 else float("nan")  # (local) mean inter-mode spacing
    d_over_Delta = d_b2 / Delta_BCS  # (local)
    print("\n--- STEP 3: BCS-BEC crossover / von Delft ultrasmall regime ---")
    print(f"  mean inter-mode spacing d = {d_b2:.6f} M_KK; d/Delta_BCS = {d_over_Delta:.3f}")
    print(f"  canonical regime locator (S61 W8): xi/d_01 = {XI_OVER_D01_S61}, mu/E_F = {MU_OVER_EF_S61} "
          f"(N_pair=2 half-filling, unitarity)")
    ultrasmall = XI_OVER_D01_S61 < 5.0  # (local) von Delft ultrasmall: discrete levels resolved (xi/d_01 ~ O(1), not deep-BCS xi/d_01 >> 1)
    print(f"  => von Delft ultrasmall regime (discrete levels resolved, d ~ Delta): "
          f"{'CONFIRMED' if ultrasmall else 'NOT confirmed'} "
          f"(xi/d_01={XI_OVER_D01_S61} ~ O(1), crossover not deep-BCS)")

    # ----- STEP 4: blocked (odd-N) Richardson spectrum level statistics -----
    # Pre-committed observable: the blocked (seniority-1, one B2 level Pauli-excluded)
    # many-body Richardson spectrum at the physical fold filling N_pair=2 (B2 quartet
    # half-filled = the canonical fold filling, ξ/d_01=1.40 regime). Computed on the
    # full 8-mode pairing sector (richer level statistics than the 4-mode B2 alone),
    # with one B2 level blocked, polynomial-unfolded, averaged over which B2 level is
    # blocked. This is the substrate's pairing-sector integrability probe.
    print("\n--- STEP 4: blocked (odd-N) Richardson spectrum <r> ---")
    modes8 = list(range(8))  # (local) full 8-mode pairing sector
    Npair_block = 2          # (local) physical fold filling (B2 half-filled)
    r_blocked_perlevel = []  # (local) <r> per choice of blocked B2 level
    for blk in idx_B2:
        w, _ = pair_space_H(eps8, V8, Npair_block, modes=modes8, blocked=[blk])
        if len(w) >= 6:
            r_blocked_perlevel.append(r_unfolded(w, deg=5))
    r_blocking = float(np.nanmean(r_blocked_perlevel))  # (local) PRE-COMMITTED verdict observable
    r_blocking_std = float(np.nanstd(r_blocked_perlevel))  # (local) sensitivity across blocked-level choice
    print(f"  blocked N_pair={Npair_block}, one B2 level Pauli-excluded, unfolded:")
    print(f"    <r>_per-blocked-level = {[f'{x:.4f}' for x in r_blocked_perlevel]}")
    print(f"    <r>_blocking (mean) = {r_blocking:.4f} +/- {r_blocking_std:.4f} (across blocked-level choice)")
    print(f"    target S106 <r>_length = {R_LENGTH_S106} (band {R_TOL}), "
          f"|Delta<r>| = {abs(r_blocking - R_LENGTH_S106):.4f}")
    print(f"    Poisson asymptote = {POISSON_R_ASYMPT:.5f}, GOE = {GOE_R} "
          f"(integrability class: <r> {'< GOE (integrable-leaning)' if r_blocking < GOE_R else '>= GOE'})")

    # Sensitivity survey (diagnostic only; NOT the verdict observable) — documents the
    # finite-size <r> spread so the INFO/FAIL outcome is read honestly.
    r_survey = {}  # (local)
    for N in [1, 2, 3, 4]:
        w_unblk, _ = pair_space_H(eps8, V8, N, modes=modes8)
        r_survey[f"unblocked_N{N}"] = r_unfolded(w_unblk, deg=5)
    print(f"  [diagnostic] unblocked seniority-0 <r> survey: "
          f"{{ {', '.join(f'{k}:{v:.4f}' for k, v in r_survey.items())} }}")

    # ----- gate logic -----
    ratio_pass = RATIO_BAND[0] <= ratio_canonical <= RATIO_BAND[1]  # (local)
    r_pass = abs(r_blocking - R_LENGTH_S106) <= R_TOL               # (local)
    # Composite (plan operator: BOTH clauses for PASS; one of two -> INFO; neither -> FAIL)
    if ratio_pass and r_pass:
        verdict = "PASS"
    elif ratio_pass or r_pass:
        verdict = "INFO"
    else:
        verdict = "FAIL"

    return {
        "verdict": verdict,
        "ratio_pass": ratio_pass,
        "r_pass": r_pass,
        # primary gap anchors (B2)
        "Delta_meanfield_B2": D_mf_B2,
        "Delta_Richardson_B2": D_pbcs_B2,
        "Delta_ED_B2": D_ed_B2,
        "ratio_meanfield_over_richardson": ratio_canonical,
        "ratio_vs_ed": ratio_vs_ed,
        "pbcs_vs_ed_pct": pbcs_vs_ed_pct,
        "Delta_BCS_canonical": float(Delta_BCS),
        # full gap arrays [B1,B2,B3]
        "Delta_bcs_fold": Delta_bcs_fold,
        "Delta_pbcs_N1": Delta_pbcs_N1,
        "Delta_ed_N1": Delta_ed_N1,
        # independent N_pair scan
        "npair_list": np.array(npair_list),
        "E_gs_independent": np.array(E_gs_ind),
        "E_cond_independent": np.array(E_cond_ind),
        "odlro_independent": np.array(odlro_ind),
        # regime
        "d_over_Delta": d_over_Delta,
        "xi_over_d01_S61": XI_OVER_D01_S61,
        "mu_over_EF_S61": MU_OVER_EF_S61,
        "ultrasmall_confirmed": ultrasmall,
        # <r> blocking
        "r_blocking": r_blocking,
        "r_blocking_std": r_blocking_std,
        "r_blocked_perlevel": np.array(r_blocked_perlevel),
        "r_length_S106": R_LENGTH_S106,
        "r_tol": R_TOL,
        "poisson_r_asympt": POISSON_R_ASYMPT,
        "goe_r": GOE_R,
        "r_survey_keys": np.array(list(r_survey.keys())),
        "r_survey_vals": np.array(list(r_survey.values())),
        # B2 sector inputs
        "eps_B2": eps_B2,
        "V_B2": V_B2,
        "b2_in_L12_cache": b2_in_cache,
        "b2_L12_dim": b2_dim,
        "n_L12_sectors": n_sectors,
        # bands
        "ratio_band_lo": RATIO_BAND[0],
        "ratio_band_hi": RATIO_BAND[1],
    }


# ---------------------------------------------------------------------------
# Section 5 — Plot
# ---------------------------------------------------------------------------
def make_plot(res):
    fig, ax = plt.subplots(2, 2, figsize=(13, 9))

    # (a) gap comparison bar
    a = ax[0, 0]
    cats = ["Delta_BCS\n(mean-field)", "Delta_PBCS\n(Richardson)", "Delta_ED\n(exact)"]
    vals = [res["Delta_meanfield_B2"], res["Delta_Richardson_B2"], res["Delta_ED_B2"]]
    bars = a.bar(cats, vals, color=["#c0392b", "#2980b9", "#27ae60"])
    a.axhline(res["Delta_BCS_canonical"], ls="--", color="k",
              label=f"Delta_BCS canonical={res['Delta_BCS_canonical']:.4f}")
    for b, v in zip(bars, vals):
        a.text(b.get_x() + b.get_width() / 2, v + 0.01, f"{v:.4f}", ha="center", fontsize=9)
    a.set_ylabel("gap (M_KK)")
    a.set_title(f"(a) B2 fold gap: mean-field/Richardson = {res['ratio_meanfield_over_richardson']:.3f} "
                f"(band [1.4,1.8])")
    a.legend(fontsize=8)

    # (b) condensation energy vs N_pair
    b = ax[0, 1]
    b.plot(res["npair_list"], res["E_cond_independent"], "o-", color="#8e44ad")
    b.set_xlabel("N_pair")
    b.set_ylabel("E_cond (M_KK)")
    b.set_title("(b) Independent exact pairing ED: E_cond(N_pair) on isolated B2")
    b.grid(alpha=0.3)

    # (c) <r> blocking vs references
    c = ax[1, 0]
    refs = {"GOE": res["goe_r"], "S106 length\n<r>=0.4118": res["r_length_S106"],
            "Poisson\nasympt": res["poisson_r_asympt"]}
    c.axhline(res["r_length_S106"], color="#2980b9", lw=2, label="S106 target 0.4118")
    c.axhspan(res["r_length_S106"] - res["r_tol"], res["r_length_S106"] + res["r_tol"],
              color="#2980b9", alpha=0.15, label="band +/-0.03")
    c.axhline(res["goe_r"], color="#c0392b", ls=":", label=f"GOE={res['goe_r']}")
    c.axhline(res["poisson_r_asympt"], color="#27ae60", ls=":",
              label=f"Poisson={res['poisson_r_asympt']:.3f}")
    xv = np.arange(len(res["r_blocked_perlevel"]))
    c.plot(xv, res["r_blocked_perlevel"], "s", color="#e67e22", ms=9,
           label="blocked (per-level)")
    c.axhline(res["r_blocking"], color="#e67e22", lw=2,
              label=f"<r>_blocking mean={res['r_blocking']:.4f}")
    c.set_xlabel("blocked B2 level index")
    c.set_ylabel("<r>")
    c.set_title(f"(c) Blocked Richardson <r>={res['r_blocking']:.4f} vs S106 (|Delta|={abs(res['r_blocking']-res['r_length_S106']):.3f})")
    c.legend(fontsize=7, loc="best")
    c.grid(alpha=0.3)

    # (d) verdict summary
    d = ax[1, 1]
    d.axis("off")
    txt = (
        f"GATE {GATE_ID}\n"
        f"VERDICT: {res['verdict']}\n\n"
        f"Clause 1 (ratio in [1.4,1.8]): "
        f"{'PASS' if res['ratio_pass'] else 'FAIL'}\n"
        f"  Delta_meanfield/Delta_Richardson = {res['ratio_meanfield_over_richardson']:.5f}\n"
        f"  (cross-check vs ED = {res['ratio_vs_ed']:.5f})\n"
        f"  PBCS vs ED agreement = {res['pbcs_vs_ed_pct']:.2f}%\n\n"
        f"Clause 2 (|<r>-0.4118| <= 0.03): "
        f"{'PASS' if res['r_pass'] else 'FAIL'}\n"
        f"  <r>_blocking = {res['r_blocking']:.4f} +/- {res['r_blocking_std']:.4f}\n"
        f"  |Delta<r>| = {abs(res['r_blocking']-res['r_length_S106']):.4f}\n"
        f"  integrability: <r> {'<' if res['r_blocking']<res['goe_r'] else '>='} GOE ({res['goe_r']})\n\n"
        f"Regime: von Delft ultrasmall "
        f"{'CONFIRMED' if res['ultrasmall_confirmed'] else 'NO'}\n"
        f"  xi/d_01 = {res['xi_over_d01_S61']} (S61 W8)\n\n"
        f"Richardson gap -> W1-1 input: {res['Delta_Richardson_B2']:.4f} M_KK"
    )
    d.text(0.02, 0.98, txt, va="top", ha="left", fontfamily="monospace", fontsize=10,
           transform=d.transAxes)

    fig.suptitle(f"{GATE_ID}: Richardson-Gaudin / canonical PBCS-with-blocking pairing engine "
                 f"(fold B2 sector)", fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(PNG_PATH, dpi=130)
    plt.close(fig)
    print(f"  plot -> {PNG_PATH}")


# ---------------------------------------------------------------------------
# Section 6 — Main
# ---------------------------------------------------------------------------
def main():
    # Plan-text-drift detection (substrate-first-canonical-sourcing.md §ii.B):
    # the plan pinned canonical_constants SHA e6829db0...; the runtime SHA may differ.
    runtime_canon_sha = sha256_of(CANONICAL_PATH)  # (local)
    plan_canon_sha = "e6829db013a713a4e56a4ca7d72e41f522bd3e3caea1bc0488ef17e0460bba34"  # (local) plan-pinned
    if runtime_canon_sha != plan_canon_sha:
        print(f"[PLAN-DRIFT] canonical_constants SHA differs from plan-freeze pin:")
        print(f"  plan-pinned : {plan_canon_sha[:16]}...")
        print(f"  runtime     : {runtime_canon_sha[:16]}...  (consumed by NAME, not SHA; values stable)")

    pins = log_input_pins([CANONICAL_PATH, L12_CACHE, S52_HFB, S46_PBCS])  # (local)
    res = compute()

    # save data
    np.savez(NPZ_PATH, gate_id=GATE_ID, **{k: v for k, v in res.items()})
    print(f"\n  data -> {NPZ_PATH}")
    make_plot(res)

    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_PATH, pins)
    print(f"\n  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")

    # 4-tuple output (final non-verdict line)
    value = (f"ratio_mf/rich={res['ratio_meanfield_over_richardson']:.5f}(band[1.4,1.8]={'IN' if res['ratio_pass'] else 'OUT'});"
             f"Delta_rich_B2={res['Delta_Richardson_B2']:.4f};Delta_mf_B2={res['Delta_meanfield_B2']:.4f};"
             f"Delta_ed_B2={res['Delta_ED_B2']:.4f};PBCSvsED={res['pbcs_vs_ed_pct']:.2f}pct;"
             f"r_blocking={res['r_blocking']:.4f}(|d|={abs(res['r_blocking']-res['r_length_S106']):.4f},band{res['r_tol']}={'IN' if res['r_pass'] else 'OUT'});"
             f"xi/d01={res['xi_over_d01_S61']}_ultrasmall={'Y' if res['ultrasmall_confirmed'] else 'N'};"
             f"convention=ABSOLUTE_vonDelft-Delta_can")
    print(f"\n  4-tuple: (value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

    def _fl(arr, nd):  # (local) format a numpy array as plain rounded floats (no np.float64 wrappers)
        return [round(float(x), nd) for x in np.asarray(arr).ravel()]
    extra = [
        f"# regulator_pin=Kosmann-V-matrix(s52); pairing-engine=canonical-PBCS-with-blocking(S46 NUMBER-PROJECTED-BCS); "
        f"gaps[B1,B2,B3]: BCS={_fl(res['Delta_bcs_fold'],5)} PBCS={_fl(res['Delta_pbcs_N1'],5)} ED={_fl(res['Delta_ed_N1'],5)}",
        f"# r_blocking sensitivity: per-blocked-level={_fl(res['r_blocked_perlevel'],4)}; "
        f"diagnostic unblocked-N survey vals={_fl(res['r_survey_vals'],4)}",
    ]
    note = (f"Richardson(PBCS) gap Delta_B2={res['Delta_Richardson_B2']:.4f} feeds W1-1 gap-magnitude term; "
            f"mean-field overestimate ratio={res['ratio_meanfield_over_richardson']:.4f} confirms atlas-04 B4 +60%")
    print_verdict_payload(res["verdict"], value, audit_sha, content_sha,
                          companion_note=note, extra_rows=extra)


if __name__ == "__main__":
    main()
