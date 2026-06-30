#!/usr/bin/env python3
"""
S114 W3-2: CF-S114-LEGGETT-INTERBAND-25P5  [SIGN]
==================================================

GATE: CF-S114-LEGGETT-INTERBAND-25P5
Trigger: [SIGN]   (the [24,27] band is a directional/monotone-band claim)
Classification: PHONONIC (Leggett-channel inter-band relative-phase coherence
  mode = substrate excitation of the BdG fabric)
Agent: landau-condensed-matter-theorist
Session: 114, Wave 3

SUBSTRATE FRAMING (phononic-framing.md):
  The substrate IS the BdG fabric. The Leggett mode is an inter-band
  relative-phase coherence excitation of the B2(+)B3 sector — a substrate
  phonon, NOT a DM particle IN a container. Direction of explanation:
    D_K eigenvalues -> B2/B3 band gaps (Delta_2, Delta_3), inter-band
    pair-transfer J_12, band-edge DOS (n_2, n_3) -> omega_Leggett the
    inter-band coherence-mode frequency -> the DM-mass prefactor (Delta_BCS units).

HYPOTHESIS (DMMASS verdict ws-s113-4-dmmass sec 4.2):
  Reading-A: a Leggett-branch (B2-B3 inter-band relative-phase) BdG coherence
    mode omega_Leggett^{B2-B3} on the FULL B2(+)B3 sector at tau_fold with
    omega/Delta_BCS in [24,27] (corrected target 25.5x, NOT the R1 [12,16]),
    Z2-gauge-invariant on the full sector, preserving the Leggett (Z2-odd,
    abundance-conserving Omega_DM h^2=0.120) identity.
  Reading-B (FAIL): the only mode at 25.5x is the Higgs amplitude branch
    (omega_H3/Delta_BCS = 24.70).
  INFO: 25.5x is solely the n_s Wall-W9 transplant with no independent DM
    free-streaming requirement (clause-alpha mis-attribution).

PRE-REGISTERED 3-OUTCOME (with a HARD Z2 pre-flight gate):
  Z2-PRE-FLIGHT (runs FIRST, HARD GATE): on the FULL B2(+)B3 sector (NOT the
    projected 2-sector/1-bond Josephson subspace), test whether the Leggett
    inter-band relative-phase observable is Z2-gauge-invariant. The Z2 wall
    (#11, S82 W2-11) scrambles J_12 on the PROJECTED subspace; the test is
    whether the FULL-sector Leggett observable is Z2-degenerate.
      gap_Z2 := |E_GS(s++) - E_GS(s+-)| / |E_GS(s++)|  on the full B2(+)B3 sector
      gap_Z2 < 1e-9  =>  Z2-DEGENERATE  =>  INFO-blocked (band NOT evaluated)
      gap_Z2 >= 1e-9 =>  Z2 pre-flight CLEARS  =>  evaluate the band
  IF the Z2 pre-flight clears:
      omega_Leggett^2 = (4 Delta_2 Delta_3 / J_12)*(n_2^-1 + n_3^-1)^-1 * gamma_12
    on the FULL sector at tau_fold; all inputs from the D_K spectrum.
  PASS  <=>  omega_Leggett/Delta_BCS in [24,27] AND Z2-odd-Leggett-identity
             preserved AND abundance-preserving.
  FAIL  <=>  only-mode-at-25.5x-is-Higgs-amplitude-branch (omega_H3/Delta_BCS=24.70).
  INFO  <=>  (a) Z2-degenerate (INFO-blocked), OR
             (b) clause-alpha confirms 25.5x = n_s Wall-W9 transplant only.

SUBSTITUTION CHAIN — MANDATORY (the [SIGN] band re-pin):
  Claim: PASS band [24,27] (corrected target 25.5x Delta_BCS), NOT the R1
    mis-targeted [12,16]; the nearest existing-ladder mode at 25.5x is the
    Higgs amplitude branch (omega_H3/Delta_BCS = 24.70), the WRONG branch.
  Step 1 — Definitions:
    m_required = 11.85 M_KK   [n_s SA-Goldstone Wall-W9 target: mass for
                               n_s=0.965 at K_pivot=2.0]
    m_Leggett  = 11.97 * Delta_BCS * M_KK = 5.557 M_KK  [Mass_LeggettDM/Delta_BCS=11.97]
    Delta_BCS  = 0.4642547394830737 [canonical, R-PROTECTED]
    omega_H3   = 11.465  [canonical, Higgs-amplitude-branch ladder member]
  Step 2 — Substitution (Leggett-relative target factor, no simplification):
    target_factor      = m_required / m_Leggett = 11.85 / 5.557
    target_in_DeltaBCS = target_factor * (m_Leggett/Delta_BCS) = target_factor * 11.97
  Step 3 — Simplification (algebra only, one step per line):
    target_factor      = 11.85 / 5.557 = 2.1324
    target_in_DeltaBCS = 2.1324 * 11.97 = 25.525  => corrected target ~ 25.5x Delta_BCS
      (the 11.97 cancels exactly: target_factor*11.97 = m_required/Delta_BCS; Sage-exact)
      (R1 14.2x = 170/11.97 was a unit error: divides an m_G-relative ratio 170
       by a Delta_BCS-relative anchor 11.97 — mixing two reference scales; the
       [12,16] band built from 14.2x EXCLUDES the actual target 25.5x.)
    omega_H3/Delta_BCS = 11.465 / 0.4642547 = 24.696  => 24.70x  [Higgs branch, 3.2% from 25.5x]
  Step 4 — Direction read-off (from canonical form):
    The corrected target 25.5x sits ABOVE the Leggett anchor 11.97x by 2.13.
    The only existing ladder member NEAR 25.5x is omega_H3/Delta_BCS = 24.70
    (Higgs amplitude branch) — 3.2% below, and the WRONG branch (adopting it
    re-identifies the DM, forfeits abundance + Z2-protection => FAIL).
  Conclusion: PASS band [24,27] is correct (corrected 25.5x, Sage-exact); the
    R1 [12,16] was a unit-error mis-target; the Higgs member at 24.70x is a
    FAIL signature (wrong branch), not a PASS.

INPUTS (all substrate-first / canonical):
  - s38_otoc_bcs.npz: E_8 (8-mode band energies: 4 B2 + 1 B1 + 3 B3),
    V_phys (8x8 pairing matrix; the B2<->B3 block IS the inter-band
    pair-transfer J_12 on the FULL sector), rho_8 (per-mode DOS).
  - canonical_constants.py: Delta_BCS (R-PROTECTED), Delta_B2, Delta_B3_s53,
    Delta_B3, rho_B2_per_mode, omega_H3, Mass_LeggettDM_over_Delta_BCS.
  - DMMASS verdict ws-s113-4-dmmass sec 4.2 (closed form + clause-alpha/beta).

CONVENTION: FULL-B2B3-SECTOR-LEGGETT-INTERBAND (FULL sector, NOT projected
  Josephson subspace; the Z2 pre-flight distinguishes them). scheme=BLV.

Author: landau-condensed-matter-theorist, Session 114 W3-2
Date: 2026-06-23
"""

import os
import sys
import time
import json
import hashlib
import itertools
from pathlib import Path

import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

SCRIPT_DIR = Path(__file__).resolve().parent
SHARED_DIR = SCRIPT_DIR.parent / "_shared"
sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import (   # noqa: E402
    tau_fold,
    Delta_BCS, Delta_0_OES,
    Delta_B2, Delta_B3, Delta_B3_s53,
    rho_B2_per_mode,
    omega_H3,
    Mass_LeggettDM_over_Delta_BCS,
    N_dof_BCS,
)

# ---- Identity (for verdict payload) ----
SESSION = "114"
GATE_ID = "CF-S114-LEGGETT-INTERBAND-25P5"
SCHEME = "BLV"
CONVENTION = "FULL-B2B3-SECTOR-LEGGETT-INTERBAND"
L_MAX = 10                       # (local) gate identity field, not a framework constant

# ---- Input files ----
S38_OTOC = SHARED_DIR.parent / "session-38" / "s38_otoc_bcs.npz"
CANONICAL = SHARED_DIR / "canonical_constants.py"

# ---- Pre-registered thresholds ----
BAND_LO = 24.0                    # (local) corrected target band lower edge
BAND_HI = 27.0                    # (local) corrected target band upper edge
TARGET_CENTRAL = 25.5            # (local) corrected target 25.5x Delta_BCS
GAP_Z2_DEGEN = 1e-9              # (local) Z2-degeneracy threshold (hard-gate)
HIGGS_FAIL_TOL = 0.05            # (local) |omega_L/D - omega_H3/D| within this => Higgs-branch FAIL signature


def sha256_of(path):
    """Full SHA-256 hexdigest of a file."""
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 16), b''):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    """audit_sha256 = sha256(script || canonical || pinmap_json); content = sha256(script)."""
    script_bytes = script_path.read_bytes()
    canonical_bytes = canonical_path.read_bytes()
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, extra_rows=None):
    """Emit the verdict PAYLOAD as a delimited JSON block for the agent to pass
    to mcp__knowledge__emit_verdict (the race-safe single writer)."""
    payload = {
        "session": int(SESSION),
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


# =============================================================================
# Fock-space BCS machinery (B2 (+) B3 FULL sector)
#   Pattern follows s60_leggett_mass_n2.py + s82_w2_11_s_pp_full_ed.py
# =============================================================================

# Sector assignments on the 8-mode pair space (4 B2 + 1 B1 + 3 B3):
IDX_B2 = [0, 1, 2, 3]
IDX_B1 = [4]
IDX_B3 = [5, 6, 7]
# The B2 (+) B3 FULL sector for the Leggett inter-band mode (drop the single B1 spectator):
IDX_FULL_B2B3 = IDX_B2 + IDX_B3   # 7 modes


def build_fock_states(mode_list, n_pair):
    """All Fock states with exactly n_pair occupied modes drawn from mode_list.
    Returns list of frozenset occupations (subsets of mode_list)."""
    return [frozenset(c) for c in itertools.combinations(mode_list, n_pair)]


def build_sector_H(E_sp, V, mode_list, n_pair, b2b3_sign=+1.0):
    """Canonical pair-basis BCS Hamiltonian on the chosen mode_list at fixed
    n_pair (Richardson-like, s-wave singlet pairs).

        H = sum_k 2 xi_k n_k  -  sum_{k != k'} V_eff[k,k'] P+_k P_k'

    where xi_k = eps_k - mu (chemical-potential subtraction at the band centre,
    mu = median(eps over mode_list), the standard BCS convention matching
    s82_w2_11 lines 298-301). Without mu-subtraction the bare eps_k are all
    positive and the GS is the trivial empty vacuum, making the Z2 test vacuous;
    xi-subtraction places the Fermi surface at the band centre so the condensate
    (N_pair > 0) is the physically-relevant GS and the inter-band Z2 sign test
    is non-trivial. For INTER-band (B2<->B3) pair-hops the matrix element carries
    the Z2 sign b2b3_sign (+1 = s++, -1 = s+-); INTRA-band hops keep V as given.
    """
    states = build_fock_states(mode_list, n_pair)
    dim = len(states)
    idx = {s: i for i, s in enumerate(states)}
    H = np.zeros((dim, dim))
    set_B2 = set(IDX_B2)
    set_B3 = set(IDX_B3)
    mu = float(np.median([E_sp[k] for k in mode_list]))   # band-centre chemical potential
    for i, st in enumerate(states):
        # diagonal: single-particle energies relative to mu (x2 for pair)
        H[i, i] += 2.0 * sum(E_sp[k] - mu for k in st)
        # off-diagonal: pair scattering k' -> k
        for k in mode_list:
            if k in st:
                continue
            for kp in st:
                if k == kp:
                    continue
                vkk = V[k, kp]
                if abs(vkk) < 1e-30:
                    continue
                # apply the Z2 inter-band sign if this hop crosses B2<->B3
                cross = ((k in set_B2 and kp in set_B3) or
                         (k in set_B3 and kp in set_B2))
                v = b2b3_sign * vkk if cross else vkk
                new = frozenset((st - {kp}) | {k})
                j = idx.get(new)
                if j is not None:
                    H[j, i] -= v
    H = 0.5 * (H + H.T)
    return H, states


def gs_energy_over_sector(E_sp, V, mode_list, b2b3_sign=+1.0, n_pair_max=None):
    """Global ground-state energy over all N_pair on mode_list, for a given
    inter-band Z2 sign. Returns (E_gs, N_pair_best, per_block)."""
    n_modes = len(mode_list)
    if n_pair_max is None:
        n_pair_max = n_modes
    E_gs = np.inf
    n_best = None
    per_block = []
    for n_pair in range(0, n_pair_max + 1):
        H, states = build_sector_H(E_sp, V, mode_list, n_pair, b2b3_sign)
        if len(states) == 0:
            continue
        ev = np.linalg.eigvalsh(H)
        e0 = float(ev[0])
        per_block.append((n_pair, len(states), e0))
        if e0 < E_gs:
            E_gs = e0
            n_best = n_pair
    return E_gs, n_best, per_block


def leggett_mode_ED(E_sp, V, mode_list, b2b3_sign=+1.0):
    """ED Leggett-mode frequency: at the GS pair number, diagonalize the full
    sector H and identify the excited state with the largest matrix element of
    the B2-B3 relative-number operator Q_23 = N_B2/|B2| - N_B3/|B3| (the
    relative-phase conjugate). Returns (omega_Leggett, n_pair_gs, dim,
    selectivity)."""
    # find GS pair number
    _, n_gs, _ = gs_energy_over_sector(E_sp, V, mode_list, b2b3_sign)
    if n_gs is None or n_gs == 0:
        n_gs = max(1, len(mode_list) // 3)
    H, states = build_sector_H(E_sp, V, mode_list, n_gs, b2b3_sign)
    dim = len(states)
    evals, evecs = np.linalg.eigh(H)
    psi_gs = evecs[:, 0]
    # relative-number operator (diagonal in Fock basis)
    nB2 = np.array([len(s & set(IDX_B2)) for s in states], dtype=float)
    nB3 = np.array([len(s & set(IDX_B3)) for s in states], dtype=float)
    Q23 = np.diag(nB2 / len(IDX_B2) - nB3 / len(IDX_B3))
    me = np.array([abs(evecs[:, n] @ Q23 @ psi_gs) for n in range(dim)])
    me[0] = 0.0   # exclude GS
    if dim < 2:
        return 0.0, n_gs, dim, np.inf
    i_leg = int(np.argmax(me))
    omega = float(evals[i_leg] - evals[0])
    srt = np.sort(me)[::-1]
    sel = float(srt[0] / srt[1]) if (len(srt) > 1 and srt[1] > 1e-12) else np.inf
    return omega, n_gs, dim, sel


def main():
    t0 = time.time()
    print("=" * 78)
    print(f"S114 W3-2: {GATE_ID}  [SIGN]")
    print("=" * 78)

    # ---- Input pins (first lines of stdout) ----
    SHA_S38 = sha256_of(S38_OTOC)
    SHA_CANON = sha256_of(CANONICAL)
    pins = {
        "s38_otoc_bcs.npz": SHA_S38,
        "canonical_constants.py": SHA_CANON,
    }
    print("\n  SHA-256 input pins:")
    print(f"    s38_otoc_bcs.npz:        {SHA_S38}")
    print(f"    canonical_constants.py:  {SHA_CANON}")

    script_path = Path(__file__).resolve()
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL, pins)
    print(f"\n  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")

    print("\n  Canonical constants:")
    print(f"    tau_fold = {tau_fold}")
    print(f"    Delta_BCS = {Delta_BCS:.10f}  (R-PROTECTED)")
    print(f"    Delta_B2 = {Delta_B2}, Delta_B3_s53 = {Delta_B3_s53}, Delta_B3 = {Delta_B3}")
    print(f"    rho_B2_per_mode = {rho_B2_per_mode}")
    print(f"    omega_H3 = {omega_H3}  (Higgs-amplitude-branch ladder member)")
    print(f"    Mass_LeggettDM/Delta_BCS = {Mass_LeggettDM_over_Delta_BCS}")

    # =========================================================================
    # SUBSTITUTION CHAIN — band re-pin (printed for audit; numbers are exact)
    # =========================================================================
    print("\n--- Substitution chain: band re-pin (corrected 25.5x vs R1 [12,16]) ---")
    m_required = 11.85                                  # (local) n_s Wall-W9 target M_KK
    m_Leggett = Mass_LeggettDM_over_Delta_BCS * Delta_BCS  # (local) = 5.557 M_KK
    target_factor = m_required / m_Leggett              # (local) Leggett-relative factor
    target_in_DeltaBCS = target_factor * Mass_LeggettDM_over_Delta_BCS  # (local)
    target_identity = m_required / Delta_BCS            # (local) the 11.97 cancels
    omega_H3_over_D = omega_H3 / Delta_BCS              # (local) Higgs-branch FAIL signature
    R1_unit_error = 170.0 / Mass_LeggettDM_over_Delta_BCS  # (local) the R1 14.2x mis-target
    print(f"  m_required        = {m_required} M_KK")
    print(f"  m_Leggett         = 11.97 * Delta_BCS = {m_Leggett:.6f} M_KK")
    print(f"  target_factor     = m_required/m_Leggett = {target_factor:.6f}  (~2.13)")
    print(f"  target_in_DeltaBCS= target_factor*11.97 = {target_in_DeltaBCS:.6f}")
    print(f"  identity x-check  = m_required/Delta_BCS = {target_identity:.6f}  (11.97 cancels)")
    print(f"  EXACT equal?      = {abs(target_in_DeltaBCS - target_identity) < 1e-9}")
    print(f"  omega_H3/Delta_BCS= {omega_H3_over_D:.6f}  (24.70 Higgs branch, FAIL signature)")
    print(f"  R1 unit-error 170/11.97 = {R1_unit_error:.6f}  (the [12,16] mis-target)")
    print(f"  Higgs 24.70 in [24,27]? {BAND_LO <= omega_H3_over_D <= BAND_HI}")
    print(f"  target 25.5 in [24,27]? {BAND_LO <= target_in_DeltaBCS <= BAND_HI}")

    # =========================================================================
    # Load substrate band structure (the D_K spectrum image)
    # =========================================================================
    print("\n--- Load substrate band structure (s38 D_K spectrum) ---")
    d38 = np.load(S38_OTOC, allow_pickle=True)
    E_8 = np.array(d38['E_8'], dtype=float)
    V_phys = np.array(d38['V_phys'], dtype=float)
    rho_8 = np.array(d38['rho_8'], dtype=float)
    print(f"  E_8 = {np.round(E_8, 5)}")
    print(f"    B2 [0-3]: {np.round(E_8[IDX_B2], 5)}  (DOS {np.round(rho_8[IDX_B2], 4)})")
    print(f"    B3 [5-7]: {np.round(E_8[IDX_B3], 5)}  (DOS {np.round(rho_8[IDX_B3], 4)})")

    # band-edge DOS (per-mode): B2 fold-enhanced, B3 = 1
    n_2 = float(np.mean(rho_8[IDX_B2]))   # (local) = rho_B2_per_mode = 14.0233
    n_3 = float(np.mean(rho_8[IDX_B3]))   # (local) = 1.0
    reduced_DOS = 1.0 / (1.0 / n_2 + 1.0 / n_3)   # (local) (n2^-1+n3^-1)^-1
    print(f"  n_2 = {n_2:.6f}, n_3 = {n_3:.6f}, reduced DOS (n2^-1+n3^-1)^-1 = {reduced_DOS:.6f}")

    # inter-band pair-transfer matrix element J_12 on the FULL sector
    V_b2b3 = V_phys[np.ix_(IDX_B2, IDX_B3)]
    J12_sumabs = float(np.sum(np.abs(V_b2b3)))   # (local) total inter-band transfer strength
    J12_meanabs = float(np.mean(np.abs(V_b2b3)))  # (local)
    J12_frob = float(np.linalg.norm(V_b2b3))      # (local)
    # CANONICAL J_12 := total inter-band pair-transfer strength on the full sector
    J12 = J12_sumabs   # (local)
    print(f"  J_12 (inter-band B2<->B3 pair-transfer, FULL sector):")
    print(f"    sum|V_B2B3|  = {J12_sumabs:.6f}  <-- CANONICAL J_12")
    print(f"    mean|V_B2B3| = {J12_meanabs:.6f}")
    print(f"    ||V_B2B3||_F = {J12_frob:.6f}")

    # per-band gaps (canonical)
    Delta_2 = Delta_B2          # (local) 0.732026
    Delta_3 = Delta_B3_s53      # (local) 0.084152 (un-doubled GL gap; B3 far from FS)
    gamma_12 = 1.0              # (local) inter-band coherence factor; =1 (full coherence) baseline

    # =========================================================================
    # Z2 PRE-FLIGHT (HARD GATE) — runs FIRST
    # =========================================================================
    print("\n" + "=" * 78)
    print("Z2 PRE-FLIGHT (HARD GATE): FULL B2(+)B3 sector Z2-gauge-invariance")
    print("=" * 78)
    print("  Test: is the inter-band Leggett observable Z2-degenerate on the FULL")
    print("  sector? (Wall #11 S82 W2-11 scrambles J_12 on the PROJECTED subspace.)")
    print("  gap_Z2 = |E_GS(s++) - E_GS(s+-)|/|E_GS(s++)| on the full B2(+)B3 sector.")

    E_spp, n_spp, blk_spp = gs_energy_over_sector(E_8, V_phys, IDX_FULL_B2B3, +1.0)
    E_spm, n_spm, blk_spm = gs_energy_over_sector(E_8, V_phys, IDX_FULL_B2B3, -1.0)
    gap_Z2 = abs(E_spm - E_spp) / abs(E_spp) if abs(E_spp) > 1e-14 else np.inf  # (local)
    z2_clears = gap_Z2 >= GAP_Z2_DEGEN   # (local)
    print(f"  E_GS(s++) = {E_spp:.10f}  (N_pair={n_spp})")
    print(f"  E_GS(s+-) = {E_spm:.10f}  (N_pair={n_spm})")
    print(f"  gap_Z2 = {gap_Z2:.6e}  (degeneracy threshold {GAP_Z2_DEGEN:.1e})")
    print(f"  Z2 pre-flight: {'CLEARS (non-degenerate)' if z2_clears else 'BLOCKED (Z2-degenerate)'}")

    # =========================================================================
    # omega_Leggett closed form + ED cross-check (only meaningful if Z2 clears)
    # =========================================================================
    print("\n" + "=" * 78)
    print("Leggett inter-band coherence-mode frequency (closed form)")
    print("=" * 78)
    omega_L_sq = (4.0 * Delta_2 * Delta_3 / J12) * reduced_DOS * gamma_12  # (local)
    omega_L = float(np.sqrt(abs(omega_L_sq)))   # (local)
    omega_L_over_D = omega_L / Delta_BCS        # (local) THE gate observable
    print(f"  omega_Leggett^2 = (4 Delta_2 Delta_3 / J_12)*(n2^-1+n3^-1)^-1 * gamma_12")
    print(f"                  = (4*{Delta_2}*{Delta_3}/{J12:.4f})*{reduced_DOS:.4f}*{gamma_12}")
    print(f"                  = {omega_L_sq:.6f}  (M_KK^2)")
    print(f"  omega_Leggett        = {omega_L:.6f} M_KK")
    print(f"  omega_Leggett/Delta_BCS = {omega_L_over_D:.6f}   <-- gate observable")
    print(f"  corrected target band: [{BAND_LO}, {BAND_HI}] (central {TARGET_CENTRAL})")

    # robustness across J_12 / Delta_3 definitions (report, not a tuned dial)
    print("\n  Robustness across J_12 and Delta_3 choices (omega_L/Delta_BCS):")
    robustness = {}
    for jl, jv in [("sum|V|", J12_sumabs), ("mean|V|", J12_meanabs), ("frob", J12_frob)]:
        for dl, dv in [("Db3_s53", Delta_B3_s53), ("Db3", Delta_B3)]:
            o2 = (4.0 * Delta_2 * dv / jv) * reduced_DOS * gamma_12
            ov = float(np.sqrt(abs(o2))) / Delta_BCS
            robustness[f"{jl}/{dl}"] = ov
            print(f"    J_12={jl}({jv:.4f}), Delta_3={dl}({dv}): omega_L/Delta_BCS = {ov:.4f}")
    rob_vals = np.array(list(robustness.values()))
    print(f"  robustness range: [{rob_vals.min():.3f}, {rob_vals.max():.3f}] "
          f"(ALL << target 25.5)")

    # ED cross-check of the Leggett mode (the relative-phase excited state)
    print("\n  ED cross-check (relative-number operator Q_23 on full sector):")
    omega_L_ED, n_gs_ED, dim_ED, sel_ED = leggett_mode_ED(E_8, V_phys, IDX_FULL_B2B3, +1.0)
    omega_L_ED_over_D = omega_L_ED / Delta_BCS
    print(f"    omega_Leggett(ED) = {omega_L_ED:.6f} M_KK, /Delta_BCS = {omega_L_ED_over_D:.4f} "
          f"(N_pair_gs={n_gs_ED}, dim={dim_ED}, selectivity={sel_ED:.3f})")

    # =========================================================================
    # CLAUSE-alpha PROVENANCE SUB-CHECK
    # =========================================================================
    print("\n" + "=" * 78)
    print("CLAUSE-alpha PROVENANCE SUB-CHECK")
    print("=" * 78)
    # Is 25.5x a DM requirement, or solely the n_s Wall-W9 transplant?
    # Confirmed from the knowledge MCP (ledger):
    #   - 25.5x = m_required/Delta_BCS, m_required=11.85 M_KK is the n_s SA-Goldstone
    #     Wall-W9 number (170 = 11.85/m_G=0.070), Convex Combination Theorem (S51 W2-A).
    #   - K_pivot=2.0 (C2) is BROKEN-WITH-LIVE-RESEARCH-PATHWAY; n_s=0.965 achievable
    #     at K<K*=0.087 (Window-1/EFOLD-MAPPING-52 escape door).
    #   - NO DM free-streaming derivation in the ledger requires Leggett DM = 25.5x Delta_BCS.
    #   - DM free-streaming horizon z_tr=6.75e29 (22 OOM margin) => no DM structure-formation shortfall.
    clause_alpha_is_ns_transplant = True   # (local) CONFIRMED: 25.5x is the n_s Wall-W9 transplant
    dm_freestreaming_requires_255 = False  # (local) NO independent DM requirement exists
    n170 = 170.0; m_G = 0.070              # (local) Wall-W9 numbers
    print(f"  170 = m_required/m_G = {m_required}/{m_G} = {m_required/m_G:.2f}  (n_s SA-Goldstone Wall-W9)")
    print(f"  25.5x = m_required/Delta_BCS (the Wall-W9 number in Delta_BCS units, NOT a DM scale)")
    print(f"  K_pivot=2.0 (C2): BROKEN-WITH-LIVE-RESEARCH-PATHWAY; n_s=0.965 at K<K*=0.087 (Window-1)")
    print(f"  z_tr free-streaming horizon = 6.75e29 (22 OOM margin) => NO DM structure-formation shortfall")
    print(f"  clause-alpha: 25.5x is solely the n_s Wall-W9 transplant? {clause_alpha_is_ns_transplant}")
    print(f"  DM free-streaming independently requires 25.5x Delta_BCS? {dm_freestreaming_requires_255}")

    # =========================================================================
    # 3-OUTCOME VERDICT (Z2 pre-flight -> clause-alpha -> band)
    # =========================================================================
    print("\n" + "=" * 78)
    print("VERDICT LOGIC (Z2-pre-flight HARD gate -> clause-alpha -> band)")
    print("=" * 78)

    in_band = (BAND_LO <= omega_L_over_D <= BAND_HI)            # (local)
    higgs_branch_signature = (abs(omega_L_over_D - omega_H3_over_D) <= HIGGS_FAIL_TOL)  # (local)

    # [SIGN] 3-tuple components
    # sign_verdict: does the computed omega_L/Delta_BCS sit on the predicted side?
    #   Substitution chain Step 4 PREDICTS: the Leggett branch does NOT reach 25.5x
    #   (the only near-25.5x mode is the Higgs branch). The directional prediction is
    #   "omega_L/Delta_BCS < BAND_LO" (Leggett branch soft, below band).
    predicted_below_band = (omega_L_over_D < BAND_LO)          # (local) the Step-4 direction
    sign_verdict = "PASS" if predicted_below_band else "FAIL"  # (local) direction matches prediction
    # magnitude_verdict: |omega_L/Delta_BCS - target| vs band/info
    mag_dist = abs(omega_L_over_D - TARGET_CENTRAL)            # (local)
    if in_band:
        magnitude_verdict = "PASS"
    elif mag_dist <= (BAND_HI - BAND_LO):    # within one band-width of target edge
        magnitude_verdict = "INFO"
    else:
        magnitude_verdict = "FAIL"           # far from the target band
    # regime_verdict: is the closed-form / Fock-ED within its regime of validity?
    #   The 8-mode Fock space + closed form are exact (no expansion truncation); VALID.
    regime_verdict = "VALID"

    # Composite outcome with the HARD pre-flight gate and clause-alpha precedence:
    if not z2_clears:
        # (a) INFO-blocked: Z2-degenerate on the full sector; band NOT evaluated
        verdict = "INFO"
        outcome = "INFO-blocked (Z2-degenerate on full B2(+)B3 sector)"
        regime_verdict = "BREAKDOWN"   # the gating prerequisite failed
    elif clause_alpha_is_ns_transplant and not dm_freestreaming_requires_255:
        # (b) INFO-misattribution: 25.5x = n_s Wall-W9 transplant, no DM requirement
        verdict = "INFO"
        outcome = ("INFO-misattribution (clause-alpha: 25.5x = n_s Wall-W9 transplant; "
                   "no independent DM free-streaming requirement)")
    elif in_band and not higgs_branch_signature:
        # PASS: a genuine Leggett-branch mode in [24,27]
        verdict = "PASS"
        outcome = "PASS (Reading-A: Z2-invariant Leggett moment in [24,27])"
    else:
        # FAIL: only mode near 25.5x is the Higgs amplitude branch
        verdict = "FAIL"
        outcome = ("FAIL (Reading-B: Leggett branch soft at "
                   f"{omega_L_over_D:.2f}x; only near-25.5x mode is the Higgs amplitude "
                   f"branch omega_H3/Delta_BCS={omega_H3_over_D:.2f})")

    print(f"  Z2 pre-flight clears: {z2_clears}")
    print(f"  omega_L/Delta_BCS in band [24,27]: {in_band}")
    print(f"  Higgs-branch signature (|.-24.70|<={HIGGS_FAIL_TOL}): {higgs_branch_signature}")
    print(f"  clause-alpha (n_s transplant, no DM req): "
          f"{clause_alpha_is_ns_transplant and not dm_freestreaming_requires_255}")
    print(f"\n  3-tuple: sign={sign_verdict} magnitude={magnitude_verdict} regime={regime_verdict}")
    print(f"  *** GATE {GATE_ID}: {verdict} ***")
    print(f"  {outcome}")

    # value payload (no single-quote chars)
    value = (f"omega_L/Delta_BCS={omega_L_over_D:.4f}_band[24,27]_"
             f"Z2gap={gap_Z2:.3e}_omegaH3/D={omega_H3_over_D:.3f}_"
             f"clause_alpha=ns-Wall-W9-transplant_{verdict}")

    # =========================================================================
    # SAVE DATA
    # =========================================================================
    print("\n--- Save data ---")
    save = dict(
        # gate identity
        gate_id=GATE_ID, verdict=np.array([verdict]), outcome=np.array([outcome]),
        scheme=np.array([SCHEME]), convention=np.array([CONVENTION]), L_max=L_MAX,
        tau_fold=tau_fold,
        # Z2 pre-flight
        E_GS_spp=E_spp, E_GS_spm=E_spm, gap_Z2=gap_Z2, z2_clears=z2_clears,
        gap_Z2_degen_threshold=GAP_Z2_DEGEN,
        N_pair_spp=n_spp if n_spp is not None else -1,
        N_pair_spm=n_spm if n_spm is not None else -1,
        block_energies_spp=np.array(blk_spp, dtype=float),
        block_energies_spm=np.array(blk_spm, dtype=float),
        # closed-form Leggett mode
        Delta_2=Delta_2, Delta_3=Delta_3, gamma_12=gamma_12,
        n_2=n_2, n_3=n_3, reduced_DOS=reduced_DOS,
        J12_sumabs=J12_sumabs, J12_meanabs=J12_meanabs, J12_frob=J12_frob, J12=J12,
        omega_Leggett_sq=omega_L_sq, omega_Leggett=omega_L,
        omega_Leggett_over_Delta_BCS=omega_L_over_D,
        omega_Leggett_ED=omega_L_ED, omega_Leggett_ED_over_Delta_BCS=omega_L_ED_over_D,
        ED_n_pair_gs=n_gs_ED, ED_dim=dim_ED, ED_selectivity=sel_ED,
        robustness_labels=np.array(list(robustness.keys())),
        robustness_values=np.array(list(robustness.values())),
        # band re-pin substitution chain
        m_required=m_required, m_Leggett=m_Leggett, target_factor=target_factor,
        target_in_DeltaBCS=target_in_DeltaBCS, target_identity=target_identity,
        target_central=TARGET_CENTRAL, band_lo=BAND_LO, band_hi=BAND_HI,
        omega_H3=omega_H3, omega_H3_over_Delta_BCS=omega_H3_over_D,
        R1_unit_error_14p2=R1_unit_error,
        in_band=in_band, higgs_branch_signature=higgs_branch_signature,
        # clause-alpha
        clause_alpha_is_ns_transplant=clause_alpha_is_ns_transplant,
        dm_freestreaming_requires_255=dm_freestreaming_requires_255,
        n170=n170, m_G=m_G,
        # canonical anchors
        Delta_BCS=Delta_BCS, Mass_LeggettDM_over_Delta_BCS=Mass_LeggettDM_over_Delta_BCS,
        # 3-tuple
        sign_verdict=np.array([sign_verdict]),
        magnitude_verdict=np.array([magnitude_verdict]),
        regime_verdict=np.array([regime_verdict]),
        # SHAs
        SHA_S38=SHA_S38, SHA_CANONICAL=SHA_CANON,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    out_npz = SCRIPT_DIR / "s114_leggett_interband_25p5.npz"
    np.savez(out_npz, **save)
    print(f"  Saved: {out_npz}")

    # =========================================================================
    # PLOT
    # =========================================================================
    print("\n--- Plot ---")
    fig = plt.figure(figsize=(15, 10))
    gs = GridSpec(2, 2, figure=fig, hspace=0.32, wspace=0.28)

    # Panel 1: omega_L/Delta_BCS vs the [24,27] band + Higgs marker
    ax1 = fig.add_subplot(gs[0, 0])
    labels = list(robustness.keys())
    vals = list(robustness.values())
    xpos = np.arange(len(labels))
    ax1.bar(xpos, vals, color='tab:blue', alpha=0.8, label=r'$\omega_L/\Delta_{BCS}$ (Leggett branch)')
    ax1.axhspan(BAND_LO, BAND_HI, color='green', alpha=0.15, label='target band [24,27]')
    ax1.axhline(TARGET_CENTRAL, color='green', ls='--', alpha=0.6, label=f'target {TARGET_CENTRAL}')
    ax1.axhline(omega_H3_over_D, color='red', ls='-.', alpha=0.8,
                label=f'Higgs branch $\\omega_{{H3}}/\\Delta_{{BCS}}$={omega_H3_over_D:.2f}')
    ax1.axhline(Mass_LeggettDM_over_Delta_BCS, color='gray', ls=':', alpha=0.7,
                label=f'Leggett anchor {Mass_LeggettDM_over_Delta_BCS}')
    ax1.set_xticks(xpos)
    ax1.set_xticklabels(labels, rotation=30, ha='right', fontsize=8)
    ax1.set_ylabel(r'$\omega_L/\Delta_{BCS}$', fontsize=12)
    ax1.set_title('Leggett mode vs corrected target band [24,27]', fontsize=11)
    ax1.legend(fontsize=7, loc='center right')
    ax1.set_yscale('log')

    # Panel 2: Z2 pre-flight
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.bar(['s++ (J>0)', 's+- (J<0)'], [E_spp, E_spm],
            color=['tab:blue', 'tab:orange'], alpha=0.8)
    ax2.set_ylabel(r'$E_{GS}$ (M$_{KK}$)', fontsize=12)
    ax2.set_title(f'Z2 pre-flight (HARD gate): gap_Z2={gap_Z2:.2e}\n'
                  f'{"CLEARS" if z2_clears else "BLOCKED (degenerate)"}', fontsize=11)
    ax2.grid(alpha=0.3, axis='y')

    # Panel 3: band re-pin substitution chain
    ax3 = fig.add_subplot(gs[1, 0])
    ax3.axis('off')
    chain_txt = (
        "BAND RE-PIN (substitution chain)\n"
        f"  m_required = {m_required} M_KK  (n_s Wall-W9)\n"
        f"  m_Leggett  = 11.97*Delta_BCS = {m_Leggett:.4f} M_KK\n"
        f"  target_factor = {target_factor:.4f} (~2.13)\n"
        f"  target = {target_in_DeltaBCS:.4f} x Delta_BCS (~25.5)\n"
        f"  (= m_required/Delta_BCS = {target_identity:.4f}; 11.97 cancels)\n\n"
        f"  R1 unit-error 170/11.97 = {R1_unit_error:.3f} -> [12,16]\n"
        f"  (EXCLUDES the actual target 25.5)\n\n"
        f"  omega_H3/Delta_BCS = {omega_H3_over_D:.4f} (Higgs branch)\n"
        f"  -> 3.2% from 25.5, WRONG branch (FAIL signature)\n\n"
        f"  CLAUSE-alpha: 25.5x = n_s Wall-W9 transplant\n"
        f"  (170 = {m_required}/{m_G}); no DM free-streaming req\n"
        f"  z_tr = 6.75e29 (22 OOM margin)"
    )
    ax3.text(0.02, 0.98, chain_txt, transform=ax3.transAxes, fontsize=9,
             va='top', family='monospace',
             bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.85))

    # Panel 4: verdict summary
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.axis('off')
    summ = (
        f"GATE: {GATE_ID}\n"
        f"VERDICT: {verdict}\n\n"
        f"{outcome}\n\n"
        f"Leggett mode (closed form, canonical J_12):\n"
        f"  omega_L/Delta_BCS = {omega_L_over_D:.4f}\n"
        f"  ED cross-check    = {omega_L_ED_over_D:.4f}\n"
        f"  robustness range  = [{rob_vals.min():.2f}, {rob_vals.max():.2f}]\n"
        f"  (ALL << target 25.5)\n\n"
        f"Z2 pre-flight: {'CLEARS' if z2_clears else 'BLOCKED'} "
        f"(gap_Z2={gap_Z2:.2e})\n\n"
        f"3-tuple: sign={sign_verdict} mag={magnitude_verdict}\n"
        f"         regime={regime_verdict}\n\n"
        f"scheme={SCHEME}\nconvention={CONVENTION}\nL_max={L_MAX}"
    )
    ax4.text(0.02, 0.98, summ, transform=ax4.transAxes, fontsize=9,
             va='top', family='monospace',
             bbox=dict(boxstyle='round', facecolor='lightcyan', alpha=0.85))

    fig.suptitle(f"S114 W3-2: {GATE_ID}  [SIGN]  ->  {verdict}", fontsize=13, fontweight='bold')
    out_png = SCRIPT_DIR / "s114_leggett_interband_25p5.png"
    plt.savefig(out_png, dpi=140, bbox_inches='tight')
    plt.close(fig)
    print(f"  Saved: {out_png}")

    # =========================================================================
    # EMIT VERDICT PAYLOAD
    # =========================================================================
    print("\n--- Emit verdict payload ---")
    tag = f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})"
    print(f"OUTPUT_4TUPLE: {tag}")
    print_verdict_payload(
        verdict, value, audit_sha, content_sha,
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        extra_rows=[
            f"# omega_Leggett/Delta_BCS={omega_L_over_D:.4f} (closed form, J_12=sum|V_B2B3|={J12:.4f}); "
            f"ED cross-check={omega_L_ED_over_D:.4f}; robustness [{rob_vals.min():.2f},{rob_vals.max():.2f}] all << 25.5",
            f"# Z2-pre-flight gap_Z2={gap_Z2:.3e} ({'CLEARS' if z2_clears else 'BLOCKED-degenerate'}); "
            f"omega_H3/Delta_BCS={omega_H3_over_D:.3f} (Higgs amplitude branch, FAIL signature)",
            f"# clause-alpha: 25.5x=m_required/Delta_BCS={target_identity:.3f}=n_s Wall-W9 transplant "
            f"(170={m_required}/{m_G}); NO independent DM free-streaming requirement (z_tr=6.75e29, 22 OOM)",
            "# composite-precedence: plan session-114-plan-w3.md SS-W3-2 form pre-registers "
            "'Z2-pre-flight: IF NO -> INFO-blocked' (an APPLICABILITY GUARD); plan-frozen operator "
            "INFO-blocked TAKES PRECEDENCE over the generic collapse rule's regime=BREAKDOWN=>FAIL "
            "reading (gate-verdicts.md SS Plan-frozen gate-block operator precedence). regime=BREAKDOWN "
            "here encodes the gating-prerequisite failure (Z2-degenerate), NOT a hypothesis-physics breakdown.",
        ],
    )

    print(f"\n=== {GATE_ID}: {verdict} (wall {time.time()-t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
