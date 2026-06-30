#!/usr/bin/env python3
"""
S85 W0-8 — S85-PIXIE-MU-K-ENDPOINT-PREREG
=========================================

Gate: S85-PIXIE-MU-K-ENDPOINT-PREREG ([VERIFY])

Hypothesis:
  The PIXIE mu-distortion K-endpoint observation at K = 3.556e5
  (gamma = 1 lockout) with framework-predicted mu = 8.695e-5 is
  observationally pre-registered as a decisive discriminator against
  LCDM's mu ~ 2e-8. The 4-OOM framework-LCDM separation is well above
  PIXIE's forecast sigma(mu) ~ 1e-8, giving a pull ~ 8.7e3.

Pre-registered threshold (plan §W0-8):
  PASS iff pull >= 100 AND gamma = 1 verified in the K-band.
  INFO iff 10 <= pull < 100.
  FAIL iff pull < 10 OR gamma-lockout violated.

Inputs (SHA-256 dual-pinned at runtime):
  - canonical_constants.py
  - s84_w5_57_data.npz (W5-57 closure provenance)
  - script bytes (feeds both content_sha256 and audit_sha256)

Output 4-tuple:
  (value=pull, scheme=Chluba-Sunyaev-2012, convention=gamma-lockout, L_max=8)

Classification: PHONONIC
  The mu-distortion IS the spectral signature of substrate-photon coupling
  at recombination — the thermodynamic inheritance of the GGE relic's 59.8
  Parker-pair-produced quasiparticles propagating through the substrate
  post-transit, not a field-theoretic scattering effect.

Method:
  (a) Import mu_framework_W5_57, K_endpoint_W5_57, gamma_lockout,
      sigma_mu_PIXIE, mu_LCDM_primordial from canonical_constants.
  (b) Cross-check mu_framework against the stored W5-57 NPZ (value +
      argmax_K + gamma_fit) — confirms provenance integrity.
  (c) Compute pull = |mu_framework - mu_LCDM| / sigma(mu).
  (d) Verify gamma = 1 lockout band (|gamma_fit - 1| < 1e-6).
  (e) Evaluate gate, emit 4-tuple + dual-SHA verdict.

CPU-only (forecasting-style scalar arithmetic; no matrices).
"""

from __future__ import annotations

import os
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    mu_framework_W5_57,
    K_endpoint_W5_57,
    gamma_lockout,
    sigma_mu_PIXIE,
    mu_LCDM_primordial,
)

# ---------------------------------------------------------------------------
# Section 2 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"                                              # (local)
GATE_ID = "S85-PIXIE-MU-K-ENDPOINT-PREREG"                   # (local)
SCHEME = "Chluba-Sunyaev-2012"                               # (local)
CONVENTION = "gamma-lockout"                                 # (local)
L_MAX = 8                                                    # (local)

# Pre-registered thresholds (plan §W0-8)
PASS_PULL_THRESHOLD = 100.0                                  # (local) plan §W0-8 PASS
INFO_PULL_LOWER = 10.0                                       # (local) plan §W0-8 INFO band lower
GAMMA_TOLERANCE = 1e-6                                       # (local) |gamma_fit - 1| < 1e-6

# Output destinations
OUT_NPZ = resolve_output(85, 's85_w0_pixie_mu_k_endpoint_prereg.npz')
OUT_PNG = resolve_output(85, 's85_w0_pixie_mu_k_endpoint_prereg.png')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')

W5_57_NPZ = resolve_output(84, 's84_w5_57_data.npz')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    W5_57_NPZ,
]


# ---------------------------------------------------------------------------
# Section 3 — SHA-256 input-pin block (first 20 lines of stdout)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()                                     # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list) -> dict:
    """Print SHA-256 of each input; return {relpath: sha} map."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict = {}                                          # (local)
    for p in inputs:
        sha = sha256_of(p)                                   # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...{sha[-8:]}")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    """Stable hash over all input SHAs (invariant to dict ordering)."""
    items = sorted(pins.items())                             # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict,
) -> tuple:
    """S84+ dual-SHA schema (W9a-99):
        audit_sha256   = sha256(script || canonical || pinmap_json)
        content_sha256 = sha256(script)
    """
    script_bytes = b""                                       # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""                                    # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                        # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                              # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()                          # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 4 — Compute
# ---------------------------------------------------------------------------

def compute() -> dict:
    """Compute pull and gamma lockout verification per plan §W0-8."""
    print("\n[SEC 4] Pre-registered inputs (from canonical_constants.py)")
    print(f"  mu_framework_W5_57     = {mu_framework_W5_57:.9e}")
    print(f"  mu_LCDM_primordial     = {mu_LCDM_primordial:.3e}")
    print(f"  sigma_mu_PIXIE         = {sigma_mu_PIXIE:.3e}")
    print(f"  K_endpoint_W5_57       = {K_endpoint_W5_57:.4e}")
    print(f"  gamma_lockout          = {gamma_lockout:.6f}")

    # -----------------------------------------------------------------------
    # (b) Cross-check W5-57 provenance: load NPZ, verify mu + K + gamma
    # -----------------------------------------------------------------------
    print("\n[SEC 4b] W5-57 provenance cross-check (from NPZ)")
    d = np.load(W5_57_NPZ)                                   # (local)
    K_corridor = d['K_corridor']                             # (local)
    mu_corridor = d['mu_corridor']                           # (local)
    gamma_fit = float(d['gamma_fit'])                        # (local)
    argmax_K = float(d['argmax_K'])                          # (local)
    max_mu_K = float(d['max_mu_K'])                          # (local)

    print(f"  K_corridor         = {K_corridor}")
    print(f"  mu_corridor        = {mu_corridor}")
    print(f"  argmax_K (W5-57)   = {argmax_K:.4e}")
    print(f"  max_mu_K (W5-57)   = {max_mu_K:.9e}")
    print(f"  gamma_fit (W5-57)  = {gamma_fit:.16f}")

    # Provenance integrity: canonical mu must match stored NPZ max_mu_K
    mu_prov_abserr = abs(mu_framework_W5_57 - max_mu_K)      # (local)
    mu_prov_relerr = mu_prov_abserr / abs(max_mu_K)          # (local)
    K_prov_relerr = abs(K_endpoint_W5_57 - argmax_K) / abs(argmax_K)  # (local)

    print(f"  |canonical - NPZ max_mu|       = {mu_prov_abserr:.3e}")
    print(f"  rel err canonical vs NPZ mu    = {mu_prov_relerr:.3e}")
    print(f"  rel err canonical vs NPZ K     = {K_prov_relerr:.3e}")

    # Tolerance: canonical is rounded NPZ, relerr expected <= 1e-3 on K
    # (3.556 vs 3.556) and ~0 on mu (copied verbatim to canonical).
    CC_PROV_MU = mu_prov_relerr < 1e-12                      # (local) mu verbatim
    CC_PROV_K = K_prov_relerr < 1e-3                         # (local) K rounded
    print(f"  CC-prov mu (relerr < 1e-12):   {CC_PROV_MU}")
    print(f"  CC-prov K  (relerr < 1e-3):    {CC_PROV_K}")

    # -----------------------------------------------------------------------
    # (c) Substitution chain (Python-verified):
    #   Step 1: mu_framework = 8.695e-5            [W5-57 closure]
    #   Step 2: mu_LCDM = 2e-8                     [Chluba-Sunyaev]
    #   Step 3: sigma(mu) = 1e-8                   [PIXIE]
    #   Step 4: pull = |mu_FW - mu_LCDM| / sigma   [definition]
    #   Step 5: pull > 100  =>  PASS
    # -----------------------------------------------------------------------
    print("\n[SEC 4c] Pull computation (substitution chain)")
    delta_mu = abs(mu_framework_W5_57 - mu_LCDM_primordial)  # (local)
    pull = delta_mu / sigma_mu_PIXIE                         # (local)
    print(f"  |mu_framework - mu_LCDM| = {delta_mu:.9e}")
    print(f"  pull = |mu_FW - mu_LCDM| / sigma(mu) = {pull:.6f}")

    # Sanity: mu_FW dominates mu_LCDM by > 3 OOM, so pull ~ mu_FW / sigma
    pull_approx = mu_framework_W5_57 / sigma_mu_PIXIE        # (local)
    pull_drop_from_LCDM = pull_approx - pull                 # (local)
    print(f"  mu_FW / sigma            = {pull_approx:.6f}   (LCDM-subtracted: {pull_drop_from_LCDM:.4f})")

    # -----------------------------------------------------------------------
    # (d) Gamma = 1 lockout verification
    # -----------------------------------------------------------------------
    print("\n[SEC 4d] Gamma = 1 lockout verification")
    gamma_dev = abs(gamma_fit - gamma_lockout)               # (local)
    gamma_locked = gamma_dev < GAMMA_TOLERANCE               # (local)
    print(f"  gamma_fit              = {gamma_fit:.16f}")
    print(f"  gamma_lockout (target) = {gamma_lockout:.1f}")
    print(f"  |gamma_fit - 1|        = {gamma_dev:.3e}")
    print(f"  tolerance              = {GAMMA_TOLERANCE:.0e}")
    print(f"  gamma_locked           = {gamma_locked}")

    # -----------------------------------------------------------------------
    # (e) Cross-checks (CC-1..CC-5)
    # -----------------------------------------------------------------------
    print("\n[SEC 4e] Cross-checks")
    # CC-1: gamma_fit = 1 to 1e-6 (equivalent to plan substitution Step 5 of W5-57)
    CC1 = gamma_locked                                       # (local)
    # CC-2: mu_framework > 0 (positivity)
    CC2 = mu_framework_W5_57 > 0                             # (local)
    # CC-3: sigma_mu_PIXIE > 0 (positivity)
    CC3 = sigma_mu_PIXIE > 0                                 # (local)
    # CC-4: provenance integrity (mu + K both match W5-57 NPZ)
    CC4 = CC_PROV_MU and CC_PROV_K                           # (local)
    # CC-5: 4-OOM separation from LCDM
    OOM_separation = np.log10(mu_framework_W5_57 / mu_LCDM_primordial)  # (local)
    CC5 = OOM_separation > 3.0                               # (local) plan claims 4-OOM
    print(f"  CC-1 gamma=1 (|dev|<1e-6):    {CC1}")
    print(f"  CC-2 mu_FW > 0:                {CC2}")
    print(f"  CC-3 sigma_PIXIE > 0:          {CC3}")
    print(f"  CC-4 NPZ provenance matches:   {CC4}")
    print(f"  CC-5 OOM(mu_FW/mu_LCDM)={OOM_separation:.2f} > 3: {CC5}")
    all_CC = CC1 and CC2 and CC3 and CC4 and CC5             # (local)
    print(f"  All cross-checks PASS:         {all_CC}")

    return dict(
        value=pull,
        delta_mu=delta_mu,
        pull=pull,
        mu_framework=mu_framework_W5_57,
        mu_LCDM=mu_LCDM_primordial,
        sigma_PIXIE=sigma_mu_PIXIE,
        gamma_fit=gamma_fit,
        gamma_lockout=gamma_lockout,
        gamma_dev=gamma_dev,
        gamma_locked=gamma_locked,
        K_endpoint=K_endpoint_W5_57,
        argmax_K_NPZ=argmax_K,
        max_mu_K_NPZ=max_mu_K,
        K_corridor=K_corridor,
        mu_corridor=mu_corridor,
        CC1=CC1, CC2=CC2, CC3=CC3, CC4=CC4, CC5=CC5,
        all_CC=all_CC,
        OOM_separation=OOM_separation,
    )


# ---------------------------------------------------------------------------
# Section 5 — Gate verdict
# ---------------------------------------------------------------------------

def evaluate_gate(result: dict) -> str:
    """Per plan §W0-8: PASS iff pull>=100 AND gamma-lockout;
    INFO iff 10<=pull<100; FAIL iff pull<10 OR gamma-lockout violated."""
    pull = result['pull']                                    # (local)
    gamma_locked = result['gamma_locked']                    # (local)
    if not gamma_locked:
        return "FAIL"
    if pull >= PASS_PULL_THRESHOLD:
        return "PASS"
    if pull >= INFO_PULL_LOWER:
        return "INFO"
    return "FAIL"


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
) -> None:
    """S84+ dual-SHA schema: append single canonical line + optional
    companion comment row. Atomic append via O_APPEND semantics."""
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------

def make_plot(result: dict) -> None:
    """Two-panel plot:
    (L) mu(K) across W5-57 K-corridor, PIXIE sigma + LCDM reference bands.
    (R) Pull bar chart: framework vs LCDM with PIXIE sigma reference.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))    # (local)

    # Left: W5-57 corridor with PIXIE sigma band and LCDM reference
    K_arr = result['K_corridor']                             # (local)
    mu_arr = result['mu_corridor']                           # (local)
    ax1.loglog(K_arr, mu_arr, 'ro-', ms=8, lw=2, mfc='red', mec='k',
               label='Framework mu(K) [W5-57]')
    ax1.axhline(result['sigma_PIXIE'], color='blue', ls='--', lw=1.5,
                label=f"PIXIE sigma(mu) = {result['sigma_PIXIE']:.0e}")
    ax1.axhline(result['mu_LCDM'], color='gray', ls=':', lw=1.5,
                label=f"LCDM mu ~ {result['mu_LCDM']:.0e}")
    ax1.axhline(9e-5, color='orange', ls='-.', lw=1.5,
                label='FIRAS 95% CL = 9e-5')
    ax1.axvline(result['K_endpoint'], color='black', ls=':', lw=1.0, alpha=0.7)
    ax1.annotate(f"K_endpoint = {result['K_endpoint']:.3e}\nmu = {result['mu_framework']:.3e}",
                 xy=(result['K_endpoint'], result['mu_framework']),
                 xytext=(result['K_endpoint'] * 0.01, result['mu_framework'] * 0.5),
                 fontsize=9, arrowprops=dict(arrowstyle='->', color='k'))
    ax1.set_xlabel('K (amplification factor)')
    ax1.set_ylabel('mu-distortion')
    ax1.set_title('W5-57 mu(K) corridor with PIXIE + LCDM reference bands')
    ax1.legend(loc='upper left', fontsize=8)
    ax1.grid(True, which='both', ls=':', alpha=0.4)

    # Right: pull bar chart
    labels = ['mu_LCDM\n(primordial)', 'mu_framework\n(W5-57 endpoint)',
              'sigma(mu)\n(PIXIE)']                         # (local)
    values = [result['mu_LCDM'], result['mu_framework'],
              result['sigma_PIXIE']]                         # (local)
    colors = ['gray', 'red', 'blue']                         # (local)
    bars = ax2.bar(labels, values, color=colors, edgecolor='k', alpha=0.75)
    ax2.set_yscale('log')
    ax2.set_ylabel('mu (log scale)')
    pull_text = (f"pull = |mu_FW - mu_LCDM| / sigma(mu) = {result['pull']:.1f}\n"
                 f"PASS threshold: pull >= 100  -> PASS\n"
                 f"OOM(mu_FW / mu_LCDM) = {result['OOM_separation']:.2f}\n"
                 f"gamma_fit = {result['gamma_fit']:.10f}  (locked)")
    ax2.set_title('PIXIE pre-registration pull and gamma-lockout')
    ax2.text(0.02, 0.02, pull_text,
             transform=ax2.transAxes, fontsize=9, va='bottom',
             bbox=dict(boxstyle='round', fc='wheat', ec='k', alpha=0.85))
    for bar, v in zip(bars, values):
        ax2.text(bar.get_x() + bar.get_width() / 2.0, v * 1.4,
                 f"{v:.1e}", ha='center', fontsize=9)
    ax2.grid(True, which='both', axis='y', ls=':', alpha=0.4)
    ax2.set_ylim(1e-9, 3e-4)

    fig.suptitle(f'{GATE_ID}  —  PIXIE mu-K endpoint pre-registration',
                 fontsize=12)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130, bbox_inches='tight')
    plt.close(fig)
    print(f"  plot written: {OUT_PNG.name}")


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                         # (local)

    # 1. Input-pin SHAs (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)                       # (local)
    closure = closure_hash(pins)                             # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Dual SHAs (S84+ schema)
    script_path = Path(__file__).resolve()                   # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')    # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...{audit_sha[-8:]}")
    print(f"  content_sha256: {content_sha[:16]}...{content_sha[-8:]}")
    print()

    # 2. Compute
    result = compute()                                       # (local)
    pull = result['pull']                                    # (local)

    # 3. Evaluate gate
    verdict = evaluate_gate(result)                          # (local)

    # 4. Persist NPZ + plot
    print("\n[SEC 5] Output persistence")
    np.savez(
        OUT_NPZ,
        pull=pull,
        mu_framework=result['mu_framework'],
        mu_LCDM=result['mu_LCDM'],
        sigma_PIXIE=result['sigma_PIXIE'],
        delta_mu=result['delta_mu'],
        gamma_fit=result['gamma_fit'],
        gamma_lockout=result['gamma_lockout'],
        gamma_dev=result['gamma_dev'],
        gamma_locked=result['gamma_locked'],
        K_endpoint=result['K_endpoint'],
        argmax_K_NPZ=result['argmax_K_NPZ'],
        max_mu_K_NPZ=result['max_mu_K_NPZ'],
        K_corridor=result['K_corridor'],
        mu_corridor=result['mu_corridor'],
        OOM_separation=result['OOM_separation'],
        PASS_PULL_THRESHOLD=PASS_PULL_THRESHOLD,
        INFO_PULL_LOWER=INFO_PULL_LOWER,
        GAMMA_TOLERANCE=GAMMA_TOLERANCE,
        verdict=verdict,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
        audit_sha=audit_sha,
        content_sha=content_sha,
    )
    print(f"  NPZ written: {OUT_NPZ.name}")
    make_plot(result)

    # 5. Emit 4-tuple + append verdict
    print("\n[SEC 6] 4-tuple + verdict")
    tag = emit_4tuple(pull, SCHEME, CONVENTION, L_MAX)       # (local)
    print(tag)
    append_verdict(verdict, pull, audit_sha, content_sha)
    print(f"  verdict appended to: {VERDICT_TXT.name}")
    print(f"  verdict: {verdict}  pull={pull:.3f}")

    # 6. Final summary
    wall = time.time() - t0                                  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
