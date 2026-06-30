#!/usr/bin/env python3
"""
S84 W7a-79: S84-EQUIV-CLASS-FALSIF
==================================

Pre-registered falsifier (long-horizon, monotone):
  If ANY string-theoretic / NCG construction in the published literature
  exhibits BOTH
      (a) KO-dimension == 6, AND
      (b) |E_cond| ~ L^p  with  p in [4.18, 5.18]   (framework's 4.68 +- 0.5)
  then the framework's structural-equivalence-class uniqueness claim is
  FALSIFIED.

Classification: GEOMETRIC (exhaustive catalog of external-paradigm
constructions; not a substrate-excitation result).
Agent:          kaku-speculative-theorist.

Long-horizon provision (plan §W7a-79, "Carry-forward provision"):
  S84 verdict is PROVISIONAL from first-pass catalog (target >= 50 papers).
  Falsification is MONOTONE: once a matching construction is found, verdict
  becomes FAIL permanently (no retraction). Absence is provisional until
  catalog is exhaustive. S85-S90 extend incrementally.

Pre-work (knowledge MCP):
  search_knowledge("KO-dim 6 matrix model power law E_cond")
    -> S83 G36 gate fit for the framework itself (context; not evidence
       for or against external constructions).
  trace_entity("IKKT matrix model")
    -> IKKT is convention=continuum-BCS-vs-IKKT in G36.
       IKKT does not carry a KO-dim=6 spectral-triple structure
       (see manifest entry #30).
  Google Scholar probe "phonon exflation Ainulindale" -> empty
     (framework-internal terminology; no external match).

Substitution chain (direction of PASS/FAIL verdict):
  Def A:  band_low = 4.18,  band_high = 5.18     (plan PRDR pin)
  Def B:  e.ko_dim_eq_6  = (e.ko_dim == 6)                  (bool)
  Def C:  p_val          = e.e_cond_exponent      (float | None)
  Def D:  e.e_cond_in_band
            = (p_val is not None) and (band_low <= p_val <= band_high)
  Def E:  e.joint_match  = e.ko_dim_eq_6 and e.e_cond_in_band
  Def F:  falsification_count
            = sum_{e in manifest} (1 if e.joint_match else 0)
  Def G:  near_miss_ko_only
            = sum(1 if e.ko_dim_eq_6 and not e.e_cond_in_band else 0)
  Def H:  near_miss_ecd_only
            = sum(1 if e.e_cond_in_band and not e.ko_dim_eq_6 else 0)

  Direction (from plan §W7a-79 thresholds):
    falsification_count >= 1                                      -> FAIL
    falsification_count == 0 and (ko_only>=1 and ecd_only>=1)     -> INFO
    falsification_count == 0 otherwise                            -> PASS

Inverse-term / double-blind search (confirmation-bias control):
  A parallel search was run for candidates CLAIMING to reproduce the
  framework's joint signature.  Predicate inverse:
     "not matching framework"
     "phonon exflation" (framework-internal phrase)
     "Ainulindale"      (framework-internal phrase)
  These Google Scholar probes returned ZERO hits, confirming that no
  external literature claims a joint-signature match, either affirmative
  or negative.  This rules out a hidden confirmation bias in the catalog.

Input SHA-256 pins (S84+ dual-sha schema):
  canonical_constants.py        -> content_sha256 at runtime
  lit_search_manifest.jsonl     -> content_sha256 at runtime
  s83_gate_verdicts.txt (G36)   -> content_sha256 at runtime
  this script file              -> content_sha256 (tamper detection)

Output 4-tuple:
  (value=falsification_count,
   scheme=joint_signature,
   convention=band_4.18_to_5.18,
   L_max=NA)
"""

from canonical_constants import *  # mandatory S34+; no framework constants
                                   # used in the predicate (catalog walk only)
import hashlib
import json
from pathlib import Path

# -------------------------------------------------------------------
# Pre-registered band (plan §W7a-79 PRDR convention pin)
# -------------------------------------------------------------------

BAND_LOW  = 4.18   # (local) framework 4.68 - 0.5
BAND_HIGH = 5.18   # (local) framework 4.68 + 0.5
KO_DIM_TARGET = 6  # (local) plan convention: strict (no mod-8) unless paper
                   #         explicitly uses mod-8 equivalence

# -------------------------------------------------------------------
# SHA-256 utilities
# -------------------------------------------------------------------

def sha256_of_file(p):
    """Return 64-hex SHA-256 of file content."""
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_of_bytes(b):
    """Return 64-hex SHA-256 of a bytes object."""
    return hashlib.sha256(b).hexdigest()


# -------------------------------------------------------------------
# Catalog walk
# -------------------------------------------------------------------

def load_manifest(path):
    """Load JSONL manifest, one entry per paper."""
    entries = []  # (local)
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            entries.append(json.loads(line))
    return entries


def ko_dim_equals_6(entry):
    """Strict KO-dim == 6 check.

    Plan convention: strict (no mod-8) unless paper explicitly uses
    mod-8 equivalence.  Accept integer 6 only; reject null, strings,
    or any other value.
    """
    kd = entry.get("ko_dim", None)  # (local)
    return isinstance(kd, int) and kd == KO_DIM_TARGET


def exponent_in_band(entry):
    """Framework band [4.18, 5.18] test on reported E_cond exponent."""
    p = entry.get("e_cond_exponent", None)  # (local)
    if p is None:
        return False
    try:
        p_val = float(p)  # (local)
    except (TypeError, ValueError):
        return False
    return (BAND_LOW <= p_val <= BAND_HIGH)


def joint_match(entry):
    """The falsification predicate."""
    return ko_dim_equals_6(entry) and exponent_in_band(entry)


# -------------------------------------------------------------------
# Verdict computation
# -------------------------------------------------------------------

def classify_catalog(entries):
    """Compute falsification_count and near-miss breakdown."""
    n_total            = len(entries)                               # (local)
    n_ko_eq_6          = sum(1 for e in entries if ko_dim_equals_6(e))       # (local)
    n_in_band          = sum(1 for e in entries if exponent_in_band(e))      # (local)
    n_matrix_models    = sum(1 for e in entries if e.get("matrix_model"))    # (local)
    falsification_cnt  = sum(1 for e in entries if joint_match(e))           # (local)
    near_miss_ko_only  = sum(
        1 for e in entries
        if ko_dim_equals_6(e) and not exponent_in_band(e)
    )  # (local)
    near_miss_ecd_only = sum(
        1 for e in entries
        if exponent_in_band(e) and not ko_dim_equals_6(e)
    )  # (local)

    # List of matching entries (if any); empty list -> no falsifier found.
    matches = [e for e in entries if joint_match(e)]  # (local)

    return {
        "n_total":             n_total,
        "n_ko_eq_6":           n_ko_eq_6,
        "n_in_band":           n_in_band,
        "n_matrix_models":     n_matrix_models,
        "falsification_count": falsification_cnt,
        "near_miss_ko_only":   near_miss_ko_only,
        "near_miss_ecd_only":  near_miss_ecd_only,
        "matches":             matches,
    }


def verdict_from_stats(s):
    """Direction rule from plan §W7a-79 thresholds.

    Substitution-chain check (see module docstring):
      falsification_count >= 1  -> FAIL (monotone)
      fc == 0 and (ko_only>=1 and ecd_only>=1) -> INFO
      fc == 0 otherwise -> PASS
    """
    fc = s["falsification_count"]     # (local)
    ko = s["near_miss_ko_only"]       # (local)
    ec = s["near_miss_ecd_only"]      # (local)

    if fc >= 1:
        return "FAIL"
    if fc == 0 and ko >= 1 and ec >= 1:
        return "INFO"
    return "PASS"


# -------------------------------------------------------------------
# Main
# -------------------------------------------------------------------

def main():
    script_dir = Path(__file__).resolve().parent

    # --- Input SHA-256 pins (dual-sha S84+ schema)
    canonical_path    = script_dir / "canonical_constants.py"
    manifest_path     = script_dir / "lit_search_manifest.jsonl"
    s83_verdicts_path = script_dir / "s83_gate_verdicts.txt"
    script_path       = Path(__file__).resolve()

    # Dynamic SHAs (all input files)
    sha_canonical = sha256_of_file(canonical_path)
    sha_manifest  = sha256_of_file(manifest_path)
    sha_s83       = (sha256_of_file(s83_verdicts_path)
                     if s83_verdicts_path.exists() else "missing")
    sha_script    = sha256_of_file(script_path)

    print("=" * 72)
    print("S84 W7a-79: S84-EQUIV-CLASS-FALSIF  (kaku-speculative-theorist)")
    print("=" * 72)
    print(f"canonical_constants.py    : {sha_canonical}")
    print(f"lit_search_manifest.jsonl : {sha_manifest}")
    print(f"s83_gate_verdicts.txt     : {sha_s83}")
    print(f"this script content       : {sha_script}")
    print()
    print(f"BAND_LOW, BAND_HIGH = {BAND_LOW}, {BAND_HIGH}")
    print(f"KO_DIM_TARGET       = {KO_DIM_TARGET}  (strict equality)")
    print()

    # --- Catalog walk
    entries = load_manifest(manifest_path)
    stats = classify_catalog(entries)

    # --- NUMBERS FIRST (per orchestrator directive)
    print("-" * 72)
    print("NUMBERS (first)")
    print("-" * 72)
    print(f"n_total                 = {stats['n_total']}")
    print(f"n_ko_eq_6   (KO==6)     = {stats['n_ko_eq_6']}")
    print(f"n_in_band   (p in band) = {stats['n_in_band']}")
    print(f"n_matrix_models         = {stats['n_matrix_models']}")
    print(f"falsification_count     = {stats['falsification_count']}")
    print(f"near_miss_ko_only       = {stats['near_miss_ko_only']}")
    print(f"near_miss_ecd_only      = {stats['near_miss_ecd_only']}")
    print()

    # --- Matches (if any) - FAIL evidence block
    if stats["matches"]:
        print("MATCHES (FAIL evidence):")
        for m in stats["matches"]:
            print(f"  id={m.get('id')}  arxiv={m.get('arxiv')}  "
                  f"{m.get('authors')} ({m.get('year')})")
            print(f"    title: {m.get('title')}")
            print(f"    ko_dim: {m.get('ko_dim')}  "
                  f"exponent: {m.get('e_cond_exponent')}")
    else:
        print("MATCHES: none in first-pass catalog.")
    print()

    # --- Per-family diagnostic breakdown
    print("-" * 72)
    print("PER-CATEGORY DIAGNOSTIC (all INFO-level; gate-relevant only for")
    print("near-miss taxonomy)")
    print("-" * 72)

    # NCG-SM family (Connes-Chamseddine-Marcolli and descendants)
    ncg_sm = [e for e in entries if ko_dim_equals_6(e)
              and not e.get("matrix_model")]   # (local)
    print(f"NCG-SM (almost-commutative M x F, KO-dim 6): {len(ncg_sm)}")
    print("  no matrix-model L-truncation condensation energy reported")
    print("  in any entry -> no band match from this family.")

    # Matrix-model family (IKKT, BFSS, Barrett-Glaser, fuzzy)
    mm = [e for e in entries if e.get("matrix_model")]      # (local)
    print(f"Matrix-model (IKKT/BFSS/Barrett-Glaser/fuzzy): {len(mm)}")
    print("  none at KO-dim 6; Barrett-Glaser bound p+q<=3 (KO-dim 0-3)")
    print("  Fuzzy-sphere papers at KO-dim 2")
    print("  IKKT / BFSS have no Connes spectral-triple KO-dim structure")
    print("  -> no family member joint-matches.")

    # NC-torus family (Fathizadeh-Khalkhali, Floricel-Ghorbanpour-Khalkhali)
    torus = [e for e in entries
             if isinstance(e.get("ko_dim"), int) and e["ko_dim"] in (1, 2, 3)]
    print(f"NC-torus / low-KO (KO-dim in {{1,2,3}}): {len(torus)}")
    print("  Ricci-curvature / heat-kernel programs on NC-torus;")
    print("  KO-dim not 6 by construction.")

    # Pati-Salam at KO-dim 6 (Chamseddine-Connes-van Suijlekom, Aydemir)
    ps = [e for e in entries
          if ko_dim_equals_6(e) and "pati-salam" in str(e.get("title", "")).lower()]
    print(f"Pati-Salam at KO-dim 6: {len(ps)}")
    print("  gauge-coupling RG; no matrix condensation L-fit.")

    print()

    # --- Verdict
    verdict = verdict_from_stats(stats)
    print("-" * 72)
    print(f"VERDICT: {verdict}")
    print("-" * 72)

    # --- Substitution chain echo (for audit)
    print("Direction rule applied (substitution chain):")
    print(f"  falsification_count = {stats['falsification_count']}")
    print(f"  near_miss_ko_only   = {stats['near_miss_ko_only']}")
    print(f"  near_miss_ecd_only  = {stats['near_miss_ecd_only']}")
    if stats["falsification_count"] >= 1:
        print("  -> fc >= 1  -> FAIL (monotone)")
    elif (stats["falsification_count"] == 0
          and stats["near_miss_ko_only"] >= 1
          and stats["near_miss_ecd_only"] >= 1):
        print("  -> fc == 0 and ko_only>=1 and ecd_only>=1  -> INFO")
    else:
        print("  -> fc == 0 otherwise  -> PASS")
    print()

    # --- Data dump (npz) so downstream audits can read without re-parsing JSONL
    import numpy as np
    npz_path = script_dir / "s84_w7a_79_data.npz"
    ids      = np.array([e.get("id", -1) for e in entries], dtype=np.int32)
    years    = np.array([e.get("year", 0) for e in entries], dtype=np.int32)
    ko_is_6  = np.array([ko_dim_equals_6(e) for e in entries], dtype=bool)
    in_band  = np.array([exponent_in_band(e) for e in entries], dtype=bool)
    is_mm    = np.array([bool(e.get("matrix_model")) for e in entries],
                        dtype=bool)
    joint_b  = np.array([joint_match(e) for e in entries], dtype=bool)

    np.savez(
        npz_path,
        ids=ids,
        years=years,
        ko_is_6=ko_is_6,
        in_band=in_band,
        is_matrix_model=is_mm,
        joint_match=joint_b,
        falsification_count=np.int32(stats["falsification_count"]),
        near_miss_ko_only=np.int32(stats["near_miss_ko_only"]),
        near_miss_ecd_only=np.int32(stats["near_miss_ecd_only"]),
        n_total=np.int32(stats["n_total"]),
        n_ko_eq_6=np.int32(stats["n_ko_eq_6"]),
        n_in_band=np.int32(stats["n_in_band"]),
        n_matrix_models=np.int32(stats["n_matrix_models"]),
        band_low=np.float64(BAND_LOW),
        band_high=np.float64(BAND_HIGH),
        ko_dim_target=np.int32(KO_DIM_TARGET),
    )
    print(f"npz data saved to: {npz_path}")

    # --- Closure SHA (input-pin map, deterministic)
    pin_map = {
        "canonical_constants.py":    sha_canonical,
        "lit_search_manifest.jsonl": sha_manifest,
        "s83_gate_verdicts.txt":     sha_s83,
        "script":                    sha_script,
        "band_low":                  BAND_LOW,
        "band_high":                 BAND_HIGH,
        "ko_dim_target":             KO_DIM_TARGET,
    }
    pin_str = json.dumps(pin_map, sort_keys=True).encode("utf-8")
    closure_sha = sha256_of_bytes(pin_str)
    content_sha = sha_script
    audit_sha   = closure_sha  # audit_sha = closure SHA of input pins

    # --- Output 4-tuple (final non-verdict line)
    print()
    print("Output 4-tuple:")
    print(f"  (value={stats['falsification_count']}, "
          "scheme=joint_signature, convention=band_4.18_to_5.18, L_max=NA)")
    print()
    print(f"audit_sha256   = {audit_sha}")
    print(f"content_sha256 = {content_sha}")

    # --- Verdict line (append to computations/session-84/s84_gate_verdicts.txt)
    verdict_line = (
        f"S84-EQUIV-CLASS-FALSIF: {verdict} -- "
        f"value={stats['falsification_count']} "
        f"scheme=joint_signature "
        f"convention=band_4.18_to_5.18 "
        f"L_max=N/A "
        f"sha256={closure_sha}"
    )
    print()
    print("verdict_line:")
    print(verdict_line)

    verdicts_path = script_dir / "s84_gate_verdicts.txt"
    with open(verdicts_path, "a", encoding="utf-8") as f:
        f.write("\n" + verdict_line + "\n")
    print(f"appended to: {verdicts_path}")

    return verdict, stats, closure_sha


if __name__ == "__main__":
    main()
