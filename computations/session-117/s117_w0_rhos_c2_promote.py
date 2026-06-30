#!/usr/bin/env python3
"""
S117 W0-1 CF-S117-HK-RHOS-C2-PROMOTE — promote rho_s_C2 = 7.962 to canonical
=============================================================================

Gate: CF-S117-HK-RHOS-C2-PROMOTE ([AUDIT])

Pre-registered threshold (artifact-existence value-landing; NOT a numerical
comparison against a substrate-physics threshold):
  PASS iff ALL of:
    (a) sha256(s48_goldstone_mass.npz) == cf4b77f0...e5f4a          (STATIC source pin)
    (b) float.hex(float(npz['rho_s_C2'])) == float.hex(7.962)        (bit-exact precondition)
    (c) `from canonical_constants import rho_s_C2` resolves          (importability re-verify)
    (d) float.hex(rho_s_C2_imported) == float.hex(float(npz value))  (round-trip bit-exact)
    (e) PROVENANCE['rho_s_C2'] present with session == 'S48'         (provenance entry)
    (f) canonical_constants.py source carries `rho_s_C2` AND `7.962`  (text witness)
  FAIL iff any of (a)-(f) is false.
  INFO reserved for an unforeseen same-name collision (a single update_constant
  with no derivation ambiguity ⇒ FIX-IN-SESSION expected; INFO not anticipated).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py   (MUTATE TARGET; post-landing state)
  - computations/session-48/s48_goldstone_mass.npz (STATIC value source, cf4b77f0...)
  - landing-identity pinmap {name, value, session, source}  (this specific landing)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=7.962..., scheme=CANONICAL-CONSTANTS-PROMOTION,
   convention=S48-MASS-48-PROVENANCE-BACKFILL, L_max=N/A)

Classification: PHONONIC.
  rho_s_C2 = 7.962 IS the Goldstone-sector superfluid stiffness rho_s at the C^2
  coset normalization — a spectral moment of D_K on the Jensen-deformed SU(3)
  fiber, NOT a fitted Lagrangian parameter. It governs how the phononic Goldstone
  mode stiffens the fabric, entering the substrate vacuum-energy functional
  rho_vac(tau, m) = E_spectral(tau) + E_cond(tau) + (1/2) rho_s m^2 phi_rms^2
  (S48 W11 Trace theorem). Direction: D_K eigenvalues (S48 16-mode joint spectrum
  at tau_fold = 0.190) -> rho_s spectral stiffness -> Goldstone-mass / vacuum-energy
  functional. This gate is provenance hygiene: the substrate-IS stiffness already
  computed at S48 becomes script-importable, closing the import-window PRU for the
  S116-W3-GOLDSTONE-M2 [SIGN] consumer and any future Goldstone-sector gate.

METHODOLOGY
-----------
Definitional-datum landing of a prior S48 result verbatim (math-scripts.md
§"When the chain is NOT required" — "Citing prior results ... verbatim, no new
derivation"). The value is read directly from s48_goldstone_mass.npz and landed
unchanged via the knowledge-MCP update_constant tool (Canonical Write-Order
Step 2). This script is the AFTER-pattern verifier (registry-landing.md): the
landing happens first (agent-side update_constant), then this script RE-READS the
post-landing state ONCE and emits a single verdict line. No corrective rewrite.

DISCIPLINE
----------
- sys.path bootstrap to _shared, then `from canonical_constants import *`.
- Every local/intermediate tagged `# (local)`.
- No framework constant hardcoded; PASS_VALUE = 7.962 is the pre-registered
  landing target read bit-exactly from the npz (tagged # (local)).
- SHA-256 of all input files logged in first lines of stdout.
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema).
- 4-tuple printed as the final non-verdict line.
- Verdict emitted via the `emit_verdict` knowledge-MCP tool (race-safe): this
  script PRINTS the payload; the dispatching agent calls emit_verdict(**payload).
  The script does NOT write s117_gate_verdicts.txt directly.
"""

from __future__ import annotations

import hashlib
import importlib
import json
import sys
import time
from pathlib import Path

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402  (provides PROVENANCE; rho_s_C2 after landing)

import numpy as np  # noqa: E402

SESSION = "S117"                                  # (local)
GATE_ID = "CF-S117-HK-RHOS-C2-PROMOTE"            # (local)
SCHEME = "CANONICAL-CONSTANTS-PROMOTION"          # (local)
CONVENTION = "S48-MASS-48-PROVENANCE-BACKFILL"    # (local)
L_MAX = "N/A"                                     # (local) provenance backfill; no spectral truncation

CONST_NAME = "rho_s_C2"                           # (local) constant being promoted
PASS_VALUE = 7.962                                # (local) pre-registered bit-exact landing target (== float64(npz))
EXPECTED_SESSION = "S48"                          # (local) provenance session
EXPECTED_SOURCE = "S48-MASS-48"                   # (local) provenance source tag

S48_NPZ = COMPUTATIONS_DIR / "session-48" / "s48_goldstone_mass.npz"  # (local) STATIC value source
S48_NPZ_EXPECTED_SHA = (
    "cf4b77f0c63bafb32a18e764202be942634ab5cd75963f9486f80c396a1e5f4a"  # (local) plan-pinned (freeze state)
)
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"  # (local) MUTATE TARGET (post-landing state)

INPUT_FILES = [CANONICAL_PATH, S48_NPZ]           # (local)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for the closure hash."""
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


def closure_hash(pins: dict[str, str]) -> str:
    """Stable hash over all input SHAs (order-invariant); legacy informational."""
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    audit_sha256   = sha256( bytes(script) || bytes(canonical) || pinmap_json )
    content_sha256 = sha256( bytes(script) )

    `pins` carries the npz SHA (STATIC source) AND the landing-identity keys
    {landing:name, landing:value, landing:session, landing:source}, so the audit
    SHA uniquely identifies THIS rho_s_C2 landing. bytes(canonical) pins the
    POST-landing canonical_constants.py state (the mutate target).
    """
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

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
# Section 5 — Landing verification (the "compute")
# ---------------------------------------------------------------------------

def compute() -> dict:
    """Re-read the post-landing state ONCE and check the 6 PASS conjuncts."""
    # (a) STATIC source SHA pin -------------------------------------------------
    npz_sha = sha256_of(S48_NPZ)                                   # (local)
    sha_ok = (npz_sha == S48_NPZ_EXPECTED_SHA)                     # (local)

    # (b) npz value bit-exact == 7.962 (PRECONDITION) --------------------------
    data = np.load(S48_NPZ)                                        # (local)
    npz_val = float(data[CONST_NAME])                             # (local)
    bitexact_npz = (float.hex(npz_val) == float.hex(PASS_VALUE))  # (local)

    # (c)+(d) importability re-verify + bit-exact round-trip -------------------
    import canonical_constants as _cc                              # (local) fresh module handle
    importlib.reload(_cc)                                          # (local) ensure POST-landing state
    import_ok = False                                             # (local)
    import_val = None                                            # (local)
    try:
        from canonical_constants import rho_s_C2 as _imported     # noqa: F401 (importability probe)
        import_val = float(_imported)                            # (local)
        import_ok = True                                         # (local)
    except Exception:                                            # noqa: BLE001 (probe: any failure ⇒ not importable)
        import_ok = False                                        # (local)
    import_matches = bool(
        import_ok and (float.hex(import_val) == float.hex(npz_val))
    )                                                            # (local)

    # (e) PROVENANCE entry present (session == 'S48') ---------------------------
    prov = getattr(_cc, "PROVENANCE", {})                         # (local)
    prov_entry = prov.get(CONST_NAME) if isinstance(prov, dict) else None  # (local)
    prov_ok = bool(
        isinstance(prov_entry, dict)
        and prov_entry.get("session") == EXPECTED_SESSION
    )                                                            # (local)
    prov_source = prov_entry.get("source") if isinstance(prov_entry, dict) else None  # (local)

    # (f) text witness in canonical_constants.py source ------------------------
    canon_text = CANONICAL_PATH.read_text(encoding="utf-8")       # (local)
    assign_present = (f"{CONST_NAME} =" in canon_text) or (f"{CONST_NAME}=" in canon_text)  # (local)
    literal_present = ("7.962" in canon_text)                     # (local)
    text_ok = bool(assign_present and literal_present)            # (local)

    verdict = (
        "PASS"
        if (sha_ok and bitexact_npz and import_matches and prov_ok and text_ok)
        else "FAIL"
    )  # (local)

    return {
        "value": npz_val,
        "npz_sha": npz_sha,
        "sha_ok": sha_ok,
        "bitexact_npz": bitexact_npz,
        "import_ok": import_ok,
        "import_val": import_val,
        "import_matches": import_matches,
        "prov_ok": prov_ok,
        "prov_source": prov_source,
        "text_ok": text_ok,
        "verdict": verdict,
    }


# ---------------------------------------------------------------------------
# Section 6 — Verdict payload + 4-tuple
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
    companion_note: str = "",
    extra_rows: list[str] | None = None,
) -> dict:
    """PRINT the verdict payload for the dispatching agent to pass to the
    knowledge-MCP `emit_verdict` tool (race-safe; the script never writes the
    verdict file). `value` is the RAW payload string (no surrounding quotes, no
    single-quote chars — the tool wraps value='...')."""
    payload: dict = {  # (local)
        "session": SESSION.lstrip("Ss"),
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
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins, then augment with the landing-identity keys.
    pins = log_input_pins(INPUT_FILES)  # (local)
    pins["landing:name"] = CONST_NAME
    pins["landing:value"] = repr(PASS_VALUE)
    pins["landing:session"] = EXPECTED_SESSION
    pins["landing:source"] = EXPECTED_SOURCE
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. S84+ dual SHAs (audit pins POST-landing canonical_constants.py state).
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Landing verification.
    result = compute()  # (local)
    print("=== landing-verification conjuncts ===")
    print(f"  (a) npz SHA == plan pin          : {result['sha_ok']}  ({result['npz_sha'][:16]}...)")
    print(f"  (b) npz value bit-exact == 7.962 : {result['bitexact_npz']}  (npz={result['value']!r})")
    print(f"  (c) import resolves              : {result['import_ok']}  (import_val={result['import_val']!r})")
    print(f"  (d) import bit-exact round-trip  : {result['import_matches']}")
    print(f"  (e) PROVENANCE[rho_s_C2] S48     : {result['prov_ok']}  (source={result['prov_source']!r})")
    print(f"  (f) source text witness          : {result['text_ok']}")
    print()

    verdict = result["verdict"]  # (local)
    value = result["value"]      # (local)

    # 3. 4-tuple + verdict payload. Descriptive, audit-greppable value string
    #    (no spaces, no single-quote chars).
    payload_value = (
        f"{value!r}_landed-importable-provenance-{EXPECTED_SOURCE}"
        if verdict == "PASS"
        else f"{value!r}_LANDING-INCOMPLETE_sha={result['sha_ok']}_bitexact={result['bitexact_npz']}"
             f"_import={result['import_matches']}_prov={result['prov_ok']}_text={result['text_ok']}"
    )  # (local)

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)
    print_verdict_payload(
        verdict,
        payload_value,
        audit_sha,
        content_sha,
        companion_note=(
            "rho_s_C2 Goldstone-sector C^2 superfluid stiffness; S48 W11 Trace "
            "theorem (GOLDSTONE-MASS-48/MASS-48); definitional-datum landing, no "
            "substitution chain; import-window PRU CLOSED for S116-W3-GOLDSTONE-M2."
        ),
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    # Exit 0 on a valid verdict (PASS or FAIL are both valid results); nonzero
    # is reserved for script breakage. compute() never raises on a clean read.
    return 0


if __name__ == "__main__":
    sys.exit(main())
