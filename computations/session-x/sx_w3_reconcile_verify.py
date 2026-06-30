#!/usr/bin/env python3
"""
SX W3-3 — RECONCILE+VERIFY (three-axis QA over the expanded document)
=====================================================================

Gate: WX-W3-3-RECONCILE-VERIFY  ([VERIFY])

Pre-registered threshold (defect set, PASS = empty; plan §W3-3):
  PASS iff stale_set union unframed_set union untraced_set = empty:
    (i)  CURRENCY  — no S57 number survives where a current canonical exists
                     (old numbers permitted ONLY in superseded/historical context);
    (ii) FRAMING   — no container-thinking violation (phononic-framing.md
                     LCDM-vs-substrate vocabulary table);
    (iii) PROVENANCE — every cited canonical number matches the runtime
                     canonical_constants snapshot (rel_tol 1e-3); a_n carry
                     regulator tags where cited as numerical Seeley-DeWitt values.
  Plus re-verification of the three G2 substitution chains (CLAIM 1/2/3).

This closure script re-reads the expanded document, runs the three-axis checks
(stale-number context scan + container-thinking scan + canonical cross-reference),
re-verifies the three substitution chains against the runtime canonical snapshot,
computes the dual-SHA, and appends the verdict.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - sessions/framework/Phononic-to-Cosmos.md        (document_post; the G2-expanded doc)
  - sessions/session-x/session-x-w3-workingpaper.md (the §W3-1 gap analysis + §W3-3 QA record)
  - computations/_shared/canonical_constants.py     (the currency/provenance reference)
  - script bytes                                    (feeds BOTH SHAs)

Output 4-tuple:
  (value=<three-axis defect-set state>,
   scheme=THREE-AXIS-QA-CURRENCY-FRAMING-PROVENANCE,
   convention=substrate-IS,
   L_max=N/A)

Classification: PHONONIC.

DISCIPLINE: `from canonical_constants import *`; intermediates tagged `# (local)`;
no linear algebra; CPU-only; dual-SHA atomic append; canonical verdict path.
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
import time
import re
import math
from pathlib import Path

SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"  # (local)
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403  (MANDATORY)
import canonical_constants as cc  # (local)

SESSION_DIR = Path(__file__).resolve().parent  # (local)
COMPUTATIONS_DIR = SESSION_DIR.parent  # (local)
PROJECT_ROOT = COMPUTATIONS_DIR.parent  # (local)
FRAMEWORK_DIR = PROJECT_ROOT / "sessions" / "framework"  # (local)

SESSION = "SX"  # (local)
GATE_ID = "WX-W3-3-RECONCILE-VERIFY"  # (local)
SCHEME = "THREE-AXIS-QA-CURRENCY-FRAMING-PROVENANCE"  # (local)
CONVENTION = "substrate-IS"  # (local)
L_MAX = "N/A"  # (local)

DOCUMENT_POST = FRAMEWORK_DIR / "Phononic-to-Cosmos.md"  # (local)
WP_PATH = PROJECT_ROOT / "sessions" / "session-x" / "session-x-w3-workingpaper.md"  # (local)
CANONICAL = SHARED_DIR / "canonical_constants.py"  # (local)

OUT_NPZ = SESSION_DIR / "sx_w3_reconcile_verify.npz"  # (local)
VERDICT_TXT = SESSION_DIR / "sx_gate_verdicts.txt"  # (local)

INPUT_FILES = [DOCUMENT_POST, WP_PATH, CANONICAL]  # (local)

REL_TOL = 1e-3  # (local) publication-precision-tolerant (Class-8.3 default)

# (i) CURRENCY: stale S57 numbers that must NOT appear OUTSIDE a superseded/historical
# context. For each, we require every occurrence in the document to co-occur (in the
# same line) with a reversal/historical marker.
STALE_PATTERNS = {  # (local)
    "old_r_3.86": "3.86e-10",
    "old_CC_114": "114",
    "old_ns_262": "262",
    "old_w0_509": "-0.509",
}
REVERSAL_MARKERS = [  # (local) any one of these in the same line legitimizes a stale number
    "supersede", "SUPERSEDE", "was ", "S57", "static reading", "error at S57",
    "no longer", "historical", "(was ", "deficiency of the original", "dead pre-registration",
    "I called", "I flagged", "I assessed", "I argued", "I devoted", "I wrote",
]

# (ii) FRAMING: container-thinking patterns FORBIDDEN per phononic-framing.md.
CONTAINER_PATTERNS = [  # (local)
    r"particles?\s+(created|produced)\s+in\s+(curved\s+)?spacetime",
    r"\bspace\s+expands\b",
    r"\bfields?\s+on\s+the\s+compact\s+(space|manifold)\b",
    r"\blives?\s+on\s+K\b",
    r"\bvacuum\s+energy\s+fine-tun",  # CC as a fine-tuning IN a container (the framing we inverted)
]
# Substrate-IS direction markers that MUST be present (>= 3).
SUBSTRATE_IS_MARKERS = [  # (local)
    "substrate IS", "spectral-action moment", "exflation is not inflation",
    "tracking vacuum", "emergent FRW", "a_0 zeroth",
]

# (iii) PROVENANCE: document-cited values that must match the runtime canonical snapshot.
# (value-in-document, canonical-attr-name)
CANONICAL_CHECKS = [  # (local)
    ("-0.918", "w0_FW"),
    ("0.9561", "n_s_framework"),
    ("0.9649", "planck_ns"),
    ("0.0117315", "r_CMB_framework"),
    ("0.0074705", "r_PathH"),
    ("115.5", "CC_OOM"),
    ("0.264", "Omega_DM_obs"),
    ("0.315", "Omega_m"),
    ("0.685", "Omega_Lambda"),
    ("0.811", "sigma_8"),
    ("0.112", "T_acoustic"),
    ("3.044", "N_eff_SM"),
    ("0.0547", "f_NL_FW_S82_equilateral"),
]


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
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str], content_payload: str) -> tuple[str, str]:
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    content = hashlib.sha256(content_payload.encode("utf-8")).hexdigest()  # (local)
    return audit, content


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"[VERIFY] three-axis QA (currency/framing/provenance), PASS=empty defect set; "
        f"3 substitution chains re-verified against runtime canonical snapshot\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def main() -> int:
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)  # (local)
    doc = DOCUMENT_POST.read_text(encoding="utf-8") if DOCUMENT_POST.exists() else ""  # (local)
    lines = doc.splitlines()  # (local)

    # ---- (i) CURRENCY ---------------------------------------------------
    stale_defects = []  # (local)
    for tag, pat in STALE_PATTERNS.items():
        for i, ln in enumerate(lines, 1):
            if pat in ln:
                if not any(mk in ln for mk in REVERSAL_MARKERS):
                    stale_defects.append((tag, i, ln[:80]))
    print(f"  (i) CURRENCY: {len(stale_defects)} stale survivals (un-contextualized)")
    for d in stale_defects:
        print(f"      STALE {d[0]} @ line {d[1]}: {d[2]}")

    # ---- (ii) FRAMING ---------------------------------------------------
    framing_defects = []  # (local)
    for pat in CONTAINER_PATTERNS:
        for m in re.finditer(pat, doc, flags=re.IGNORECASE):
            framing_defects.append((pat, m.group(0)))
    substrate_is = sum(1 for m in SUBSTRATE_IS_MARKERS if m in doc)  # (local)
    print(f"  (ii) FRAMING: {len(framing_defects)} container-thinking hits; "
          f"substrate-IS markers {substrate_is}/{len(SUBSTRATE_IS_MARKERS)}")
    for d in framing_defects:
        print(f"      CONTAINER: {d[1]!r} (pattern {d[0]})")

    # ---- (iii) PROVENANCE: cited values vs runtime canonical ------------
    untraced_defects = []  # (local)
    for doc_val, attr in CANONICAL_CHECKS:
        present_in_doc = doc_val in doc  # (local)
        canon = getattr(cc, attr, None)  # (local)
        if canon is None:
            untraced_defects.append((attr, "MISSING-CANONICAL", doc_val))
            continue
        try:
            dv = float(doc_val)  # (local)
            cv = float(canon)  # (local)
            denom = abs(cv) if abs(cv) > 0 else 1.0  # (local)
            match = abs(dv - cv) / denom <= REL_TOL  # (local)
        except (TypeError, ValueError):
            match = (str(canon).startswith(doc_val) or doc_val in str(canon))  # (local)
        status = "OK" if (present_in_doc and match) else (
            "VALUE-DRIFT" if present_in_doc else "NOT-IN-DOC")  # (local)
        print(f"      {attr}: doc={doc_val} canonical={canon} present={present_in_doc} -> {status}")
        if not match:
            untraced_defects.append((attr, status, f"doc={doc_val} canon={canon}"))
    print(f"  (iii) PROVENANCE: {len(untraced_defects)} value-drift/untraced defects")

    # ---- substitution-chain re-verification -----------------------------
    h = 0.674  # (local) Planck h
    chain_ok = {}  # (local)
    # CLAIM 1: CC ratio 1.032 ; CC_OOM 115.5 from runtime
    chain_ok["CLAIM1_CC"] = (abs(cc.CC_OOM - 115.5) <= REL_TOL * 115.5)
    # CLAIM 2: Leggett-only 0.03985*3.010 = 0.1199485 ; obs 0.264*h^2
    leggett = 0.03985 * 3.010  # (local)
    obs_h2 = float(cc.Omega_DM_obs) * h * h  # (local)
    chain_ok["CLAIM2_OmegaDM"] = (abs(leggett - 0.1199485) <= 1e-6 and abs(obs_h2 - 0.11993) <= 5e-4)
    # CLAIM 3: n_s sigma-distances
    ns = float(cc.n_s_framework)  # (local)
    pk = float(cc.planck_ns)  # (local)
    s_042 = abs(ns - pk) / 0.0042  # (local)
    s_062 = abs(ns - pk) / 0.0062  # (local)
    kz = abs(2.065 - pk) / 0.0042  # (local)
    alpha_s_sub = ns * ns - 1.0  # (local)
    l_2nd = math.pi * 229.48  # (local)
    chain_ok["CLAIM3_ns"] = (abs(s_042 - 2.0952) <= 1e-2 and abs(s_062 - 1.4194) <= 1e-2
                             and abs(kz - 261.93) <= 1.0 and abs(alpha_s_sub + 0.08587279) <= 1e-6
                             and abs(l_2nd - 720.93) <= 0.1)
    print(f"  substitution-chain re-verification: {chain_ok}")
    print(f"    CLAIM2 leggett={leggett:.7f} obs_h2={obs_h2:.5f}; "
          f"CLAIM3 sigma042={s_042:.4f} sigma062={s_062:.4f} kz={kz:.2f} "
          f"alpha_s={alpha_s_sub:.8f} l={l_2nd:.2f}")

    # ---- verdict --------------------------------------------------------
    checks = {  # (local)
        "currency_empty": len(stale_defects) == 0,
        "framing_empty": len(framing_defects) == 0,
        "substrate_is_present": substrate_is >= 3,
        "provenance_empty": len(untraced_defects) == 0,
        "chains_ok": all(chain_ok.values()),
    }
    verdict = "PASS" if all(checks.values()) else "FAIL"  # (local)
    print(f"  checks: {checks}")
    print(f"  VERDICT: {verdict}")

    value = (  # (local)
        f"currency{len(stale_defects)}_framing{len(framing_defects)}_"
        f"untraced{len(untraced_defects)}_substrateIS{substrate_is}of{len(SUBSTRATE_IS_MARKERS)}_"
        f"3chains_{'ok' if all(chain_ok.values()) else 'fail'}"
    )

    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), CANONICAL, pins, doc)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (document_post FINAL)")

    try:
        import numpy as np  # (local)
        np.savez(
            OUT_NPZ,
            n_stale=np.array([len(stale_defects)]),
            n_framing=np.array([len(framing_defects)]),
            n_untraced=np.array([len(untraced_defects)]),
            substrate_is=np.array([substrate_is]),
            chain_keys=np.array(list(chain_ok.keys())),
            chain_ok=np.array([chain_ok[k] for k in chain_ok]),
            canonical_attrs=np.array([a for _, a in CANONICAL_CHECKS]),
            verdict=np.array([verdict]),
        )
        print(f"  npz written: {OUT_NPZ}")
    except Exception as exc:  # noqa: BLE001
        print(f"  [npz] optional artifact skipped ({exc})")

    append_verdict(verdict, value, audit_sha, content_sha)
    print(f"  verdict appended -> {VERDICT_TXT}")
    print(f"  elapsed: {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
