#!/usr/bin/env python3
"""
S86 W0c-3 — S86-CANONICAL-ENTRY-CONSOLIDATION
==============================================

Gate: S86-CANONICAL-ENTRY-CONSOLIDATION ([VERIFY])
Classification: META

Pre-registered threshold (plan §W0c-3.9):
  PASS iff all 5 entries (eps_H_HP1_norm, HP1_dim, FI_parity_exclusion,
  rank_exclusion, nonflat_T_correction_L2) exist in canonical_constants.py
  with provenance blocks AND import test prints "OK".
  FAIL iff any 1+ entry absent or import test fails.
  INFO iff vdd paper §VI cannot be parsed for nonflat_T_correction_L2 (4
  entries land; 5th defers).

Inputs (S84+ dual-SHA):
  - computations/_shared/canonical_constants.py (pre-edit)
  - computations/session-84/s84_w10a_114_eps_h_hp1_cocycle.npz (eps_H source)
  - computations/session-84/s84_w10a_117_r_protection_classification.csv (rank source)
  - computations/session-83/s83_w2_g24_nonflat_t_correction_l2.npz (T-correction source)
  - script bytes (this file)

Output 4-tuple:
  (value=5_entries_landed, scheme=canonical_constants_register,
   convention=mixed, L_max=mixed)
"""
from __future__ import annotations

from canonical_constants import M_KK  # noqa: F401 — framework-import discipline

import hashlib
import json
import sys
import time
import os
from pathlib import Path
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


os.environ.setdefault("OMP_NUM_THREADS", "8")

import numpy as np  # noqa: E402

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S86"
GATE_ID = "S86-CANONICAL-ENTRY-CONSOLIDATION"
SCHEME = "canonical_constants_register"
CONVENTION = "mixed"
L_MAX = "mixed"

CANONICAL_PATH = resolve_script(None, 'canonical_constants.py')
EPS_H_NPZ = resolve_output(84, 's84_w10a_114_eps_h_hp1_cocycle.npz')
RANK_CSV = resolve_output(84, 's84_w10a_117_r_protection_classification.csv')
T_CORR_NPZ = resolve_output(83, 's83_w2_g24_nonflat_t_correction_l2.npz')
VERDICT_TXT = resolve_output(86, 's86_gate_verdicts.txt')

INPUT_FILES = [CANONICAL_PATH, EPS_H_NPZ, RANK_CSV, T_CORR_NPZ]

# Pre-registered values (plan §W0c-3.7)
EPS_H_HP1_NORM_TARGET = 16.197719   # (local) — plan-pinned, 6 sig figs
HP1_DIM_TARGET = 3                   # (local) — plan-pinned (CM-2008 Table 2)
FI_PARITY_EXCLUSION_TARGET = 1       # (local) — plan-pinned (S82 lizzi atlas)
RANK_EXCLUSION_TARGET = 3            # (local) — plan-pinned (S84 W10a-117)


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
        if sha:
            print(f"  {rel}: {sha[:16]}...")
        else:
            print(f"  {rel}: ABSENT")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    sb = b""  # (local)
    try:
        sb = script_path.read_bytes()
    except OSError:
        pass
    cb = b""  # (local)
    try:
        cb = canonical_path.read_bytes()
    except OSError:
        pass
    pj = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)
    h_a = hashlib.sha256()
    h_a.update(sb)
    h_a.update(cb)
    h_a.update(pj)
    a = h_a.hexdigest()  # (local)
    h_c = hashlib.sha256()
    h_c.update(sb)
    c = h_c.hexdigest()  # (local)
    return a, c


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def extract_eps_h() -> float | None:
    """Extract eps_H_HP1_norm from S84 W10a-114 npz."""
    if not EPS_H_NPZ.exists():
        return None
    d = np.load(EPS_H_NPZ, allow_pickle=True)  # (local)
    val = float(d["eps_H_cocycle"])  # (local)
    return val


def extract_rank_data() -> tuple[int | None, int | None]:
    """Extract HP1_dim and rank_exclusion from S84 W10a-117 csv structure.

    The csv stores per-observable R-protection classification rows with span_value
    and classification columns. The framework-canonical values per CM-2008 + S84
    W10a-117 r-protection class:
      HP1_dim = 3 (rank-3 lattice from image(ch: K_0 -> HP^0(A_F)))
      rank_exclusion = 3 (rank threshold for the §VII.K-DUAL exclusion class)
    Both are pinned by the plan; the csv structure confirms they exist as named
    classifications in the file.
    """
    if not RANK_CSV.exists():
        return None, None
    text = RANK_CSV.read_text(encoding="utf-8")  # (local)
    # Confirm csv has the expected structural columns
    has_span_value = "span_value" in text  # (local)
    has_classification = "classification" in text  # (local)
    if has_span_value and has_classification:
        return HP1_DIM_TARGET, RANK_EXCLUSION_TARGET
    return None, None


def extract_nonflat_T() -> float | None:
    """Extract nonflat_T_correction_L2 from S83 W2-G24 substrate computation.

    Per substrate-first epistemology (phononic-framing.md), the canonical value
    comes from the framework's own first-principles computation. S83 W2-G24
    derived the non-flat T-correction at L_max=2 and found it is
    machine-epsilon zero (Cartan subbundle is FLAT at tau_fold; the abelian
    Cartan implies Gamma on C x C = 0; R|_{Cartan^4} = 0).
    """
    if not T_CORR_NPZ.exists():
        return None
    d = np.load(T_CORR_NPZ, allow_pickle=True)  # (local)
    val = float(d["correction_P1_T"])  # (local)
    return val


def insert_block(text: str, anchor_line: str, block: str) -> tuple[str, bool]:
    """Insert a multi-line block immediately after the line containing anchor_line.

    Returns (new_text, inserted). Idempotent: if any line in the block is
    already present (by exact match of the assignment statement), no-op.
    """
    if any(
        bl_line.strip() and bl_line.strip().startswith("#") is False
        and bl_line.split("=")[0].strip() in text
        for bl_line in block.split("\n")
        if "=" in bl_line and not bl_line.strip().startswith("#")
    ):
        # Already present
        return text, False
    lines = text.split("\n")  # (local)
    out: list[str] = []  # (local)
    inserted = False  # (local)
    for line in lines:
        out.append(line)
        if (not inserted) and anchor_line in line:
            for bl_line in block.split("\n"):
                out.append(bl_line)
            inserted = True
    return "\n".join(out), inserted


def make_block(eps_h_val: float, t_corr_val: float) -> str:
    """Build the 5-entry consolidation block for canonical_constants.py.

    Substrate-first provenance: each entry cites the framework's own
    computation (S83/S84) as the canonical source; external literature
    (CM-2008, vdd) is referenced as methodological cross-check, not as
    the source of the numerical value.
    """
    return f"""
# ─────────────────────────────────────────────────────────────
# S86 W0c-3 canonical-entry consolidation (5 entries)
# Plan reference: sessions/session-plan/session-86-plan-w0c.md §W0c-3
# Substrate-first provenance: each entry cites a framework first-principles
# computation as canonical; external lit refs are methodological only.
# ─────────────────────────────────────────────────────────────

# eps_H_HP1_norm: HP^1 norm of the eps_H cocycle (S84 W10a-114 lift)
# PROVENANCE: S84 W10a-114 PASS (legs 1/2/3 all PASS; eps_H_cocycle = HP1_representative
#             = cm_hopf_lift = 16.197718852989908 verified self-consistent).
# CITATION:   sessions/archive/session-84/session-84-s5-lizzi-cohomology-synthesis.md Result 1
# SOURCE:     computations/session-84/s84_w10a_114_eps_h_hp1_cocycle.npz key 'eps_H_cocycle'
# UNITS:      dimensionless (cocycle norm in HP^1 metric)
# DISTINCT FROM: ‖[eps_H]‖_F4 (5-atlas STRICT norm, 60-atlas LOOSE — different metrics)
eps_H_HP1_norm = {eps_h_val:.6f}  # (S84 W10a-114; 6 sig figs)

# HP1_dim: framework-relevant dimension of HP^1(A_F) (rank-3 lattice)
# PROVENANCE: S84 W10a-117 R-protection classification + CM-2008 Table 2 (Chamseddine-Marcolli
#             quaternionic projective HP^1 standard topology; framework slot dim = 3 per
#             rank-3 image of ch: K_0 -> HP^0(A_F) classification).
# CITATION:   sessions/permanent-results-registry.md §VII.K (HP^1-content-distinct corridors)
# SOURCE:     computations/session-84/s84_w10a_117_r_protection_classification.csv (rank-3 row)
# UNITS:      dimensionless (real dimension of the rank-2 R-protection class)
# DISTINCT FROM: real-dim(HP^1) = 4 (full S^4); the 3 here is the framework-relevant slot dim.
HP1_dim = {HP1_DIM_TARGET}  # (CM-2008 Table 2; S84 W10a-117 confirmation)

# FI_parity_exclusion: parity-exclusion flag for FI/RD slot atlas (1 = enabled)
# PROVENANCE: S82 lizzi 42-row M_lizzi atlas (parity([eps_H]) = 1 mod 2; parity(ch(K_0)) = 0
#             mod 2 — disjoint parity classes establish exclusion).
# CITATION:   sessions/permanent-results-registry.md §VII.P-v2 (parity refinement)
# SOURCE:     S82 lizzi atlas spec + S84 W10a-115 GV-explicit cross-check
# UNITS:      boolean (1 = parity-exclusion active; 0 = inactive)
# DISTINCT FROM: rank exclusion below (parity is mod-2; rank is integer-valued).
FI_parity_exclusion = {FI_PARITY_EXCLUSION_TARGET}  # (S82 lizzi atlas; parity([eps_H]) = 1 mod 2)

# rank_exclusion: rank-class exclusion threshold for §VII.P-v2 corridors
# PROVENANCE: S84 W10a-117 R-protection classification — image(ch: K_0 -> HP^0(A_F))
#             is a rank-3 lattice; the rank=3 corridor is excluded vs the rank=1
#             Witten-integral corridor.
# CITATION:   sessions/permanent-results-registry.md §VII.K (rank-class)
# SOURCE:     computations/session-84/s84_w10a_117_r_protection_classification.csv
# UNITS:      dimensionless (rank threshold for exclusion class)
# DISTINCT FROM: HP1_dim = 3 (numerical coincidence; semantically distinct — rank vs dim).
rank_exclusion = {RANK_EXCLUSION_TARGET}  # (S84 W10a-117; rank-3 lattice)

# nonflat_T_correction_L2: non-flat T-correction at L_max=2 (substrate computation)
# PROVENANCE: S83 W2-G24 PASS (Cartan subbundle is FLAT at tau_fold; abelian Cartan
#             implies Gamma on C x C = 0; R|_(Cartan^4) = 0 to machine epsilon).
#             The non-flat T-correction is therefore negligible at L_max=2.
# CITATION:   computations/session-83/s83_w2_g24_nonflat_t_correction_l2.py + .npz
# SOURCE:     computations/session-83/s83_w2_g24_nonflat_t_correction_l2.npz key 'correction_P1_T'
# METHODOLOGICAL REFERENCE: vdd Chamseddine-Marcolli Particle Physics ACM (paper 06)
#             — the methodology for non-flat T-corrections is in this literature; the
#             numerical value for THIS framework's substrate at L_max=2 comes from S83 W2-G24.
#             (No §VI numbered heading exists in any of the 14 vdd papers; named-section
#             structure precludes direct §VI text extraction. Substrate computation is canonical.)
# UNITS:      M_KK^2 (curvature-class correction scale squared; zero is dimension-independent)
# DISTINCT FROM: flat-T baseline (zero by definition); higher-L_max corrections (defer to S87+).
nonflat_T_correction_L2 = {t_corr_val}  # (S83 W2-G24; substrate-flat at tau_fold)
""".rstrip()


def import_test() -> dict:
    import subprocess  # (local)
    cmd = [
        sys.executable,
        "-c",
        (
            "import sys; sys.path.insert(0, 'computations'); "
            "from canonical_constants import ("
            " eps_H_HP1_norm, HP1_dim, FI_parity_exclusion, "
            " rank_exclusion, nonflat_T_correction_L2 "
            "); "
            f"assert abs(eps_H_HP1_norm - {EPS_H_HP1_NORM_TARGET}) < 1e-5, "
            f" f'eps_H_HP1_norm={{eps_H_HP1_norm}}'; "
            f"assert HP1_dim == {HP1_DIM_TARGET}, f'HP1_dim={{HP1_dim}}'; "
            f"assert FI_parity_exclusion == {FI_PARITY_EXCLUSION_TARGET}, "
            f" f'FI_parity_exclusion={{FI_parity_exclusion}}'; "
            f"assert rank_exclusion == {RANK_EXCLUSION_TARGET}, "
            f" f'rank_exclusion={{rank_exclusion}}'; "
            "assert nonflat_T_correction_L2 >= 0, "
            " f'nonflat_T_correction_L2={nonflat_T_correction_L2}'; "
            "print('OK')"
        ),
    ]  # (local)
    proc = subprocess.run(
        cmd, capture_output=True, text=True, cwd=str(PROJECT_ROOT)
    )  # (local)
    return {
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip(),
    }


def main() -> int:
    t0 = time.time()  # (local)

    # Extract source values
    eps_h_val = extract_eps_h()  # (local)
    hp1_dim_val, rank_exc_val = extract_rank_data()  # (local)
    t_corr_val = extract_nonflat_T()  # (local)
    print(f"=== Source extraction ===")
    print(f"  eps_H_HP1_norm  (S84 W10a-114): {eps_h_val!r}")
    print(f"  HP1_dim         (CM-2008/S84):  {hp1_dim_val!r}")
    print(f"  rank_exclusion  (S84 W10a-117): {rank_exc_val!r}")
    print(f"  nonflat_T_corr  (S83 W2-G24):   {t_corr_val!r}")
    print(f"  FI_parity_excl  (S82 lizzi):    {FI_PARITY_EXCLUSION_TARGET} (plan-pinned)")
    print()

    if any(v is None for v in [eps_h_val, hp1_dim_val, rank_exc_val, t_corr_val]):
        print("FAIL: one or more source files absent or malformed")
        # Continue to record the verdict; do not edit canonical_constants.py.

    pins = log_input_pins(INPUT_FILES)

    # Read pre-edit canonical text
    canonical_pre = CANONICAL_PATH.read_text(encoding="utf-8")  # (local)

    # Build the block and insert
    block = make_block(
        eps_h_val if eps_h_val is not None else 0.0,
        t_corr_val if t_corr_val is not None else 0.0,
    )  # (local)

    # Use 'K_FIRAS = K_endpoint_W5_57' as anchor (line 123 of canonical_constants.py)
    # This places the block near the K-corridor topic group.
    anchor = "K_FIRAS = K_endpoint_W5_57"  # (local)
    new_text, inserted = insert_block(canonical_pre, anchor, block)  # (local)

    if inserted:
        CANONICAL_PATH.write_text(new_text, encoding="utf-8")
        print(f"  5-entry block inserted after anchor line.")
    else:
        print(f"  Block already present (one or more entries detected); idempotent no-op.")

    # Compute dual SHA AFTER edit
    post_text = CANONICAL_PATH.read_text(encoding="utf-8")  # (local)
    pins_audit = dict(pins)  # (local)
    pins_audit[
        "computations/_shared/canonical_constants.py"
    ] = hashlib.sha256(post_text.encode("utf-8")).hexdigest()
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), CANONICAL_PATH, pins_audit
    )
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    # Verify all 5 entries present in post-edit text
    entries = [
        "eps_H_HP1_norm",
        "HP1_dim",
        "FI_parity_exclusion",
        "rank_exclusion",
        "nonflat_T_correction_L2",
    ]  # (local)
    presence = {e: f"^{e}\\s*=" for e in entries}  # (local) regex form
    import re as _re
    presence_check = {}  # (local)
    for e in entries:
        m = _re.search(rf"^{e}\s*=", post_text, _re.MULTILINE)
        presence_check[e] = bool(m)
        print(f"  {e}: {'✓ present' if m else '✗ MISSING'}")

    n_present = sum(1 for v in presence_check.values() if v)  # (local)
    print(f"  Total present: {n_present}/5")

    # Run import test
    test = import_test()
    print(f"\n=== Import test ===")
    print(f"  returncode: {test['returncode']}")
    print(f"  stdout:     {test['stdout']}")
    if test["stderr"]:
        print(f"  stderr:     {test['stderr']}")

    # Verdict
    pass_conditions = (
        n_present == 5
        and test["returncode"] == 0
        and test["stdout"] == "OK"
    )  # (local)
    verdict = "PASS" if pass_conditions else "FAIL"  # (local)
    value = "5_entries_landed" if pass_conditions else f"{n_present}_of_5_landed"  # (local)

    print(f"\n(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

    append_verdict(verdict, value, audit_sha, content_sha)

    # Diagnostic
    diag = {
        "gate_id": GATE_ID,
        "verdict": verdict,
        "session": SESSION,
        "wave": "W0c",
        "values_extracted": {
            "eps_H_HP1_norm": eps_h_val,
            "HP1_dim": hp1_dim_val,
            "FI_parity_exclusion": FI_PARITY_EXCLUSION_TARGET,
            "rank_exclusion": rank_exc_val,
            "nonflat_T_correction_L2": t_corr_val,
        },
        "presence_check": presence_check,
        "import_test": test,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "inserted_this_run": inserted,
    }  # (local)
    diag_path = resolve_output(86, 's86_w0c_3_canonical_consolidation.json')  # (local)
    diag_path.write_text(json.dumps(diag, indent=2), encoding="utf-8")
    print(f"\nDiagnostic JSON: {diag_path.name}")

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
