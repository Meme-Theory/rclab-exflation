#!/usr/bin/env python3
"""
S85 W1a-2: ALPHA-S-REGISTRY-UPGRADE
===================================

Gate: S85-W1a-ALPHA-S-REGISTRY-UPGRADE
Trigger: [AUDIT]
Classification: META (permanent-results-registry audit under partition-invariance criterion)
Agent: mack-cosmic-bridge

Hypothesis: The S50 identity "alpha_s = n_s^2 - 1" is promotable to
PARTITION-INVARIANT status in the permanent-results-registry iff it
holds across two independent partition schemes with residual <= 1%
of alpha_s_obs(M_Z) AND both schemes reproduce PDG alpha_s(M_Z) = 0.1180
within +/-0.0010.

Scheme A (topological): alpha_s^(A) := n_s_framework^2 - 1
Scheme B (spectral second moment):
  alpha_s^(B) := <D_K^2>/<D_K^0> - <D_K>^2 / <D_K^0>^2
             = weighted-mean(lambda^2) - weighted-mean(lambda)^2
             = Var(lambda) on SU(3) Casimir spectrum at L_max=10.

SU(3) Casimir spectrum analytic construction:
  irreps labeled by Dynkin (p,q), p,q >= 0, truncated at p+q <= L_max=10.
  Weyl dimension: dim(p,q) = (p+1)(q+1)(p+q+2)/2.
  Quadratic Casimir (Dynkin normalization):
     C_2(p,q) = p^2 + p*q + q^2 + 3*(p+q).
  Dirac eigenvalue squared: |D|^2(p,q) = C_2(p,q) (up to convention).
  Multiplicity in L^2(SU(3)) under left+right action: dim^2 (Peter-Weyl).

Substitution chain (Python-verified at top of compute() below):
  Step 1: ns_framework = 0.9595 (S65 BCS+one-loop, canonical).
  Step 2: alpha_s^(A) = 0.9595^2 - 1 = -0.07936 (pure algebra).
  Step 3: SU(3) Casimir moments on L_max=10 truncation:
          <D_K^0> = sum dim^2(p,q)                     = 611,610
          <D_K>   = sum dim^2(p,q) * sqrt(C_2(p,q))     = 5,901,xxx
          <D_K^2> = sum dim^2(p,q) * C_2(p,q)           = 57,701,xxx
          mean_lambda  = <D_K>/<D_K^0>   = 9.6467 (dimensionless Casimir units)
          mean_lambda2 = <D_K^2>/<D_K^0> = 94.3223
          Var = mean_lambda2 - mean_lambda^2 = 1.2639 (plan formula raw)
          Also report CV^2 = Var/mean^2 = 0.01358 (dimensionless)
  Step 4: residual := |alpha_s^(A) - alpha_s^(B)| / alpha_s_obs_PDG
          where alpha_s^(B) is reported in TWO variants: raw Var (dimensional)
          and CV^2 (dimensionless).
          Primary variant for gate decision: CV^2 (dimensional coherence with
          alpha_s_obs requires a dimensionless spectral second-moment estimator).
  Step 5: With alpha_s^(A) = -0.07936, alpha_s^(B)_CV2 = 0.01358:
          residual = |-0.07936 - 0.01358| / 0.1180 = 0.788
  Step 6: PDG agreement check:
          PDG alpha_s(M_Z) = 0.1180 +/- 0.0010 (canonical alpha_s_MZ_obs).
          |alpha_s^(A) - PDG| / sigma_PDG = |(-0.0794) - 0.1180| / 0.0010 = 197 sigma.
          |alpha_s^(B)_CV2 - PDG| / sigma_PDG = |0.0136 - 0.1180| / 0.0010 = 104 sigma.
          Both schemes are > 2 sigma from PDG.
  Direction: residual = 0.788 > 0.05 (FAIL threshold); additionally both
             schemes > 2 sigma from PDG ==> FAIL by plan §W1a-2 rule.
             The S50 identity is SCHEME-SPECIFIC (topological only);
             spectral-second-moment route gives a different answer.
             Registry row stays single-scheme; partition-invariance claim
             is RETRACTED from S84.

Cross-check 1: both schemes must reproduce observed alpha_s(M_Z) = 0.1179
  +/- 0.0010 (PDG 2024). Computed deviations: A=197sigma, B=104sigma
  from PDG. Neither passes.

Cross-check 2: the analytic SU(3) Casimir moment construction is compared
  against the symbol-weighted mean formula: <D_K^k>/<D_K^0> = mean(lambda^k)
  weighted by Peter-Weyl multiplicity dim^2(p,q). Plan's literal formula
  <D_K^2>/<D_K^0> - <D_K>^2/<D_K^0>^2 = Var(lambda) is an identity (by
  definition of sample variance with weights); cross-check 2 verifies
  numerical coherence between the literal formula and Var() implementation
  to within machine epsilon.

Inputs (SHA-256 dual-pinned at runtime):
  - computations/_shared/canonical_constants.py
  - summary/atlas-04-permanent-results-registry.md
  - script bytes

Output 4-tuple:
  (value=<residual_primary>, scheme=AB-cross, convention=PARTITION-INV, L_max=10)

Thresholds (pre-registered, plan §W1a-2):
  - PASS iff residual <= 0.01 AND both schemes within +/-0.0010 of PDG.
  - FAIL iff residual > 0.05 OR either scheme > 2 sigma from PDG.
  - INFO iff 0.01 < residual <= 0.05 AND neither scheme > 2 sigma from PDG.

Output files:
  - computations/session-85/s85_w1a_alpha_s_registry_upgrade.py
  - computations/session-85/s85_w1a_alpha_s_registry_upgrade.npz
  - computations/session-85/s85_w1a_alpha_s_registry_upgrade.md (registry patch)
  - verdict appended to computations/session-85/s85_gate_verdicts.txt
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import alpha_s_MZ_obs, ns_framework  # noqa: E402

import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402

PROJECT_ROOT = SCRIPT_DIR.parent
SCRIPT_DIR = SCRIPT_DIR

SESSION = "S85"                                                     # (local)
GATE_ID = "S85-W1a-ALPHA-S-REGISTRY-UPGRADE"                        # (local)
SCHEME = "AB-cross"                                                 # (local)
CONVENTION = "PARTITION-INV"                                        # (local)
L_MAX = 10                                                          # (local)

# Pre-registered thresholds (plan §W1a-2)
PASS_RESIDUAL = 0.01                                                # (local)
FAIL_RESIDUAL = 0.05                                                # (local)
SIGMA_PDG = 0.0010                                                  # (local) PDG 1-sigma on alpha_s(M_Z)
SIGMA_THRESHOLD = 2.0                                               # (local) 2-sigma PASS window vs PDG

OUT_NPZ = SCRIPT_DIR / "s85_w1a_alpha_s_registry_upgrade.npz"
OUT_MD = SCRIPT_DIR / "s85_w1a_alpha_s_registry_upgrade.md"
VERDICT_TXT = SCRIPT_DIR / "s85_gate_verdicts.txt"
CANON_PY = SCRIPT_DIR / "canonical_constants.py"
REGISTRY_MD = PROJECT_ROOT / "summary" / "atlas-04-permanent-results-registry.md"

INPUT_FILES = [CANON_PY, REGISTRY_MD]


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                            # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict[str, str] = {}                                       # (local)
    for p in inputs:
        sha = sha256_of(p)                                          # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = p.name                                            # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())                                    # (local)
    h = hashlib.sha256()                                            # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = b""                                              # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        pass
    canonical_bytes = b""                                           # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        pass
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")

    h_audit = hashlib.sha256()                                      # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                     # (local)

    h_content = hashlib.sha256()                                    # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                                 # (local)

    return audit, content


def su3_casimir_spectrum(L_max: int) -> tuple[np.ndarray, np.ndarray]:
    """Build the SU(3) Casimir spectrum truncated at p+q <= L_max.

    Returns (eigval_squared, multiplicity) arrays. Excludes the trivial
    rep (0,0) which has Casimir = 0 (zero mode).

    Formulas:
      dim(p,q) = (p+1)(q+1)(p+q+2)/2
      C_2(p,q) = p^2 + p*q + q^2 + 3*(p+q)
      Peter-Weyl multiplicity in L^2(SU(3)): dim^2
    """
    evsq = []                                                       # (local)
    mults = []                                                      # (local)
    for p in range(L_max + 1):
        for q in range(L_max + 1):
            if p + q > L_max:
                continue
            if p == 0 and q == 0:
                continue  # trivial rep zero-mode excluded
            dim = (p + 1) * (q + 1) * (p + q + 2) // 2              # (local)
            C2 = p * p + p * q + q * q + 3 * (p + q)                # (local)
            evsq.append(C2)
            mults.append(dim * dim)                                 # Peter-Weyl
    return (np.array(evsq, dtype=np.float64),
            np.array(mults, dtype=np.float64))


def compute() -> dict:
    """Compute both partition schemes and the cross-residual.

    Step 1: alpha_s^(A) = n_s^2 - 1
    Step 2: Build SU(3) Casimir spectrum at L_max=10.
    Step 3: <D_K^k>/<D_K^0> = weighted mean(lambda^k) under mult=dim^2.
    Step 4: alpha_s^(B)_raw = Var(lambda) = <lambda^2> - <lambda>^2 (dimensional)
            alpha_s^(B)_CV2 = Var(lambda) / mean(lambda)^2           (dimensionless)
    Step 5: residual_raw = |A - B_raw| / alpha_s_obs
            residual_cv2 = |A - B_cv2| / alpha_s_obs (primary gate decision)
    """
    # Scheme A
    alpha_A = float(ns_framework ** 2 - 1.0)                        # (local) -0.07936

    # Scheme B
    evsq, mults = su3_casimir_spectrum(L_MAX)
    evs = np.sqrt(evsq)                                             # (local)
    N = float(mults.sum())                                          # (local) <D_K^0>
    mean_lambda = float((mults * evs).sum() / N)                    # (local) <D_K>/<D_K^0>
    mean_lambda2 = float((mults * evsq).sum() / N)                  # (local) <D_K^2>/<D_K^0>
    Var_raw = mean_lambda2 - mean_lambda ** 2                       # (local) plan literal formula
    CV2 = Var_raw / mean_lambda ** 2                                # (local) dimensionless normalized

    # Cross-check 2: sample variance identity
    # weighted Var(lambda) = sum_i mult_i * (lambda_i - mean)^2 / N
    Var_identity = float((mults * (evs - mean_lambda) ** 2).sum() / N)  # (local)
    assert abs(Var_raw - Var_identity) < 1e-9, \
        f"plan-formula vs identity disagree: {Var_raw} vs {Var_identity}"

    # Residuals (primary = CV2 variant)
    alpha_B_raw = Var_raw                                           # (local)
    alpha_B_cv2 = CV2                                               # (local)
    residual_raw = abs(alpha_A - alpha_B_raw) / alpha_s_MZ_obs      # (local)
    residual_cv2 = abs(alpha_A - alpha_B_cv2) / alpha_s_MZ_obs      # (local)

    # PDG 2-sigma checks
    pull_A = abs(alpha_A - alpha_s_MZ_obs) / SIGMA_PDG              # (local)
    pull_B_raw = abs(alpha_B_raw - alpha_s_MZ_obs) / SIGMA_PDG      # (local)
    pull_B_cv2 = abs(alpha_B_cv2 - alpha_s_MZ_obs) / SIGMA_PDG      # (local)

    return {
        "alpha_A": alpha_A,
        "alpha_B_raw": alpha_B_raw,
        "alpha_B_cv2": alpha_B_cv2,
        "mean_lambda": mean_lambda,
        "mean_lambda2": mean_lambda2,
        "Var_raw": Var_raw,
        "CV2": CV2,
        "N_spectrum": N,
        "n_irreps": int(len(evsq)),
        "residual_raw": residual_raw,
        "residual_cv2": residual_cv2,
        "value": residual_cv2,  # primary gate value
        "pull_A": pull_A,
        "pull_B_raw": pull_B_raw,
        "pull_B_cv2": pull_B_cv2,
        "alpha_s_obs_PDG": alpha_s_MZ_obs,
        "ns_framework": ns_framework,
    }


def evaluate_gate(res: dict) -> str:
    """Plan §W1a-2 pre-registered thresholds.

    PASS iff residual_cv2 <= 0.01 AND max(pull_A, pull_B_cv2) <= 1 (within PDG 1-sigma).
    FAIL iff residual_cv2 > 0.05 OR max(pull_A, pull_B_cv2) > 2 (> 2 sigma from PDG).
    INFO iff 0.01 < residual_cv2 <= 0.05 AND max(pull) <= 2.
    """
    resid = res["residual_cv2"]                                     # (local)
    max_pull = max(res["pull_A"], res["pull_B_cv2"])                # (local)
    if resid <= PASS_RESIDUAL and max_pull <= 1.0:
        return "PASS"
    if resid > FAIL_RESIDUAL or max_pull > SIGMA_THRESHOLD:
        return "FAIL"
    return "INFO"


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def write_registry_patch_md(res: dict, verdict: str, audit_sha: str,
                            content_sha: str, out_path: Path) -> None:
    """Write the registry-row upgrade patch (FAIL path keeps row single-scheme).
    """
    patch = f"""# Registry patch -- S85 W1a-2 alpha_s partition-invariance audit

**Gate**: {GATE_ID}
**Verdict**: {verdict}
**Target row** (pre-gate): `alpha_s` identity (S50-51 atlas) "alpha_s = n_s^2 - 1".

## Audit result

Scheme A (topological): alpha_s^(A) = n_s_framework^2 - 1 = {res['alpha_A']:+.6f}
Scheme B (spectral, CV^2 norm): alpha_s^(B) = {res['alpha_B_cv2']:+.6f}
Scheme B (raw Var, dimensional): alpha_s^(B) = {res['alpha_B_raw']:+.6f}

Cross-scheme residual (CV^2 variant): |A - B| / alpha_s_obs = {res['residual_cv2']:.4f}
Cross-scheme residual (raw variant):  |A - B| / alpha_s_obs = {res['residual_raw']:.4f}

PDG agreement pulls (alpha_s(M_Z) = {res['alpha_s_obs_PDG']:.4f} +/- {SIGMA_PDG:.4f}):
- pull_A        = {res['pull_A']:.1f} sigma
- pull_B_CV^2   = {res['pull_B_cv2']:.1f} sigma
- pull_B_raw    = {res['pull_B_raw']:.1f} sigma

## Registry action

{'**PASS** - promote row to partition-invariant; add provenance stamp S85-W1a-2.' if verdict == 'PASS' else '**' + verdict + '** - registry row STAYS single-scheme; partition-invariance claim RETRACTED from S84 permanent-results row for alpha_s.'}

## Provenance

- audit_sha256:   {audit_sha}
- content_sha256: {content_sha}
- schema_version: S84+
- L_max truncation for SU(3) Casimir spectrum: {L_MAX}
- Peter-Weyl multiplicity convention: dim^2
- N_irreps (L_max={L_MAX}, p+q <= L_max, excluding trivial): {res['n_irreps']}
- <D_K^0> (total weighted count): {res['N_spectrum']:.0f}
"""
    out_path.write_text(patch, encoding="utf-8")
    print(f"  MD written: {out_path.name}")


def main() -> int:
    t0 = time.time()                                                # (local)

    pins = log_input_pins(INPUT_FILES)
    print(f"  closure: {closure_hash(pins)[:16]}... (legacy)")

    script_path = Path(__file__).resolve()                          # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANON_PY, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    res = compute()
    verdict = evaluate_gate(res)

    print("=== Substitution chain (Python-verified) ===")
    print(f"  Step 1: Scheme A: alpha_s^(A) = n_s^2 - 1 = "
          f"{res['ns_framework']:.4f}^2 - 1 = {res['alpha_A']:+.6f}")
    print(f"  Step 2: SU(3) Casimir spectrum (L_max={L_MAX}, p+q<=L_max, Peter-Weyl mult=dim^2):")
    print(f"          N_irreps = {res['n_irreps']}, total weighted count = {res['N_spectrum']:.0f}")
    print(f"          <D_K>/<D_K^0>   = {res['mean_lambda']:.4f}")
    print(f"          <D_K^2>/<D_K^0> = {res['mean_lambda2']:.4f}")
    print(f"  Step 3: Scheme B raw:  Var = <D_K^2>/<D_K^0> - <D_K>^2/<D_K^0>^2 = {res['alpha_B_raw']:+.6f}")
    print(f"          Scheme B CV^2: Var / <D_K>^2 = {res['alpha_B_cv2']:+.6f}")
    print(f"  Step 4: residual_CV2 = |A - B_CV2| / alpha_s_obs = "
          f"|{res['alpha_A']:+.4f} - {res['alpha_B_cv2']:+.4f}| / {res['alpha_s_obs_PDG']} "
          f"= {res['residual_cv2']:.4f}")
    print(f"          residual_raw = {res['residual_raw']:.4f}")
    print(f"  Step 5: PDG pulls: A={res['pull_A']:.1f}s, B_CV2={res['pull_B_cv2']:.1f}s, "
          f"B_raw={res['pull_B_raw']:.1f}s")
    print(f"  Step 6: Thresholds: PASS<={PASS_RESIDUAL}+PDG1s, FAIL>{FAIL_RESIDUAL} OR pull>2s")
    print(f"          value={res['residual_cv2']:.4f}, max_pull={max(res['pull_A'], res['pull_B_cv2']):.1f}s "
          f"==> {verdict}")
    print()

    np.savez(
        OUT_NPZ,
        alpha_A=np.float64(res["alpha_A"]),
        alpha_B_raw=np.float64(res["alpha_B_raw"]),
        alpha_B_cv2=np.float64(res["alpha_B_cv2"]),
        mean_lambda=np.float64(res["mean_lambda"]),
        mean_lambda2=np.float64(res["mean_lambda2"]),
        Var_raw=np.float64(res["Var_raw"]),
        CV2=np.float64(res["CV2"]),
        residual_raw=np.float64(res["residual_raw"]),
        residual_cv2=np.float64(res["residual_cv2"]),
        pull_A=np.float64(res["pull_A"]),
        pull_B_raw=np.float64(res["pull_B_raw"]),
        pull_B_cv2=np.float64(res["pull_B_cv2"]),
        N_spectrum=np.float64(res["N_spectrum"]),
        n_irreps=np.int64(res["n_irreps"]),
        alpha_s_obs_PDG=np.float64(res["alpha_s_obs_PDG"]),
        ns_framework=np.float64(res["ns_framework"]),
        L_max=np.int64(L_MAX),
        audit_sha256=np.array(audit_sha),
        content_sha256=np.array(content_sha),
    )
    print(f"  NPZ written: {OUT_NPZ.name}")

    write_registry_patch_md(res, verdict, audit_sha, content_sha, OUT_MD)

    tag = emit_4tuple(res["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, res["value"], audit_sha, content_sha)

    wall = time.time() - t0                                         # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    # Exit 0 on any clean run (PASS/INFO/FAIL are all physics verdicts, not errors).
    # Reserve non-zero exit for genuine script errors (unhandled exceptions).
    return 0


if __name__ == "__main__":
    sys.exit(main())
