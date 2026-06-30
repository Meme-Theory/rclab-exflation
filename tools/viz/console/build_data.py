#!/usr/bin/env python3
"""
Ainulindale Console — live data.js generator.

Reads:
  - tools/knowledge.db      (FTS5 + typed-entity SQLite, rebuilt via /weave --db-sync)
  - computations/_shared/canonical_constants.py   (imported via sys.path)
  - tools/viz/console/data.seed.js             (visualization helpers: EQUATIONS, PAASCH, buildSpectrum, mulberry32)

Writes:
  - tools/viz/console/data.js

Design:
  - CONSTANTS / THEOREMS / GATES / SESSIONS / EDGES / TRAJECTORY / RESEARCHERS come from the DB.
  - EQUATIONS / PAASCH / buildSpectrum / mulberry32 are lifted verbatim from data.seed.js — they
    are visualization storytelling, not a database enumeration. Swapping data.js for data.seed.js
    restores the original hand-curated slice.

Run:
    "phonon-exflation-sim/.venv312/Scripts/python.exe" tools/viz/console/build_data.py
"""

from __future__ import annotations

import json
import os
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent           # tools/viz/console
ROOT = HERE.parent.parent.parent                   # project root
DB_PATH = ROOT / "tools" / "knowledge.db"
CC_PATH = ROOT / "computations/_shared" / "canonical_constants.py"
SEED_PATH = HERE / "data.seed.js"
OUT_PATH = HERE / "data.js"

MAX_CONSTANTS = 250           # (local) pull ~all 194 canonical + seed
MAX_THEOREMS = 400            # (local) pull all filtered real theorems
MAX_GATES = 600               # (local) balanced pre-S81 + S81+
MAX_SESSIONS = 100            # (local) all sessions
MAX_TRAJECTORY = 150          # (local) full trajectory
MAX_RESEARCHERS = 39          # (local) all researchers in DB
MAX_EQUATIONS_LIB = 1500      # (local) all display equations from DB
MAX_CLOSED = 350              # (local)
MAX_OPEN = 350                # (local)


# ============================================================================
# Canonical constants — whitelist driven + PROVENANCE augmentation
# ============================================================================

# Curated whitelist. Order roughly follows the seed's narrative sections.
CONSTANT_WHITELIST = [
    # core moduli + fold
    ("tau_fold",        "τ_fold",             "moduli",       "Jensen deformation where B2 group velocity vanishes"),
    ("alpha_disp",      "α (curvature)",      "dispersion",   "Dispersion curvature at the fold"),
    ("Delta_BCS",       "Δ_BCS",              "BCS",          "BCS gap energy"),
    ("E_cond",          "E_cond",             "BCS",          "B2 Cooper-pair condensation energy"),
    ("E_cond_ED_8mode", "E_cond (8-mode ED)", "BCS",          "Exact diagonalization 8-mode condensation"),
    ("E_cond_ED_5mode", "E_cond (5-mode ED)", "BCS",          "Exact diagonalization 5-mode condensation"),
    ("Delta_B3",        "Δ_B3",               "BCS",          "B3 band gap"),
    ("Delta_0_GL",      "Δ_0 (GL)",           "BCS",          "Ginzburg-Landau gap"),
    ("Delta_0_OES",     "Δ_0 (OES)",          "BCS",          "Odd-Even Staggering gap"),
    ("omega_L1",        "ω_L1",               "resonance",    "Leggett mode frequency"),
    ("omega_J",         "ω_J",                "resonance",    "Josephson frequency"),
    # spectral action
    ("S_fold",          "S_fold",             "spectral",     "Spectral action at the fold"),
    ("dS_fold",         "dS/dτ at fold",      "spectral",     "Jensen derivative — monotone up"),
    ("d2S_fold",        "d²S/dτ²",            "spectral",     "Curvature along Jensen"),
    ("S_inst",          "S_inst",             "spectral",     "Instanton action"),
    ("a2_SD",           "a₂",                 "spectral",     "Seeley-DeWitt a₂ (Einstein-Hilbert coupling)"),
    # volumes + geometry
    ("Vol_SU3_Haar",    "Vol(SU(3)) Haar",    "geometry",     "8·√3·π⁴"),
    ("Vol_SU3",         "Vol(SU(3))",         "geometry",     "Volume of internal space"),
    ("J_C2",            "J·C₂",               "geometry",     "J / Casimir-2 product"),
    # mass scales
    ("M_KK",            "M_KK",               "mass scale",   "Kaluza-Klein scale"),
    ("M_KK_gravity",    "M_KK (gravity)",     "mass scale",   "Gravity-channel KK scale"),
    ("M_Pl_reduced",    "M_Pl (reduced)",     "mass scale",   "Reduced Planck mass"),
    ("M_Pl_unreduced",  "M_Pl (unreduced)",   "mass scale",   "Unreduced Planck mass"),
    ("M_Z",             "M_Z",                "PDG",          "Z boson mass (PDG)"),
    ("M_W",             "M_W",                "PDG",          "W boson mass (PDG)"),
    ("m_H_obs",         "m_H (obs)",          "PDG",          "Higgs mass, observed"),
    ("m_t_pole",        "m_t pole",           "PDG",          "Top quark pole mass"),
    ("v_ew",            "v_EW",               "PDG",          "Electroweak VEV"),
    # gauge
    ("alpha_em_MZ_inv", "1/α_EM(M_Z)",        "gauge",        "PDG fine structure at M_Z"),
    ("alpha_s_MZ_obs",  "α_s(M_Z)",           "gauge",        "Strong coupling at M_Z"),
    ("sin2_thetaW_MSbar","sin²θ_W (MSbar)",   "gauge",        "Weinberg angle, PDG"),
    ("alpha_QM",        "α_QM",               "dispersion",   "Quantum mechanical dispersion α"),
    # acoustic + transit
    ("T_acoustic",      "T_acoustic",         "temperature",  "Acoustic Hawking temperature"),
    ("c_Gold",          "c_Gold",             "acoustic",     "Goldstone sound speed"),
    ("c_fabric",        "c_fabric",           "acoustic",     "Fabric sound speed"),
    ("dt_transit",      "Δt_transit",         "transit",      "Transit duration"),
    ("rho_s",           "ρ_s",                "acoustic",     "Superfluid density"),
    # cosmology
    ("T_CMB",           "T_CMB",              "cosmological", "CMB temperature"),
    ("H_0_km_s_Mpc",    "H₀",                 "cosmological", "Hubble today (Planck 2018)"),
    ("Omega_m",         "Ω_m",                "cosmological", "Matter density"),
    ("Omega_Lambda",    "Ω_Λ",                "cosmological", "Dark energy density"),
    ("Omega_DM",        "Ω_DM",               "cosmological", "Dark matter density"),
    ("A_s_CMB",         "A_s (CMB)",          "cosmological", "Scalar amplitude (Planck)"),
    ("planck_ns",       "n_s (Planck)",       "cosmological", "Scalar tilt (Planck 2018)"),
    ("sigma_8",         "σ_8",                "cosmological", "Matter fluctuation amplitude"),
    ("rho_Lambda_obs",  "ρ_Λ (obs)",          "cosmological", "Observed cosmological constant"),
    # CC / Jensen
    ("CC_ratio",        "CC ratio",           "CC",           "Cosmological-constant ratio (spectral/obs)"),
    ("Lambda_obs_MP4",  "Λ/M_Pl⁴",            "CC",           "Dimensionless CC"),
    # Paasch + mass quantization
    ("phi_Paasch",      "φ (Paasch)",         "mass",         "Paasch golden base; x = e^(−x²)"),
    # Volumes of reality
    ("t_universe_s",    "t_universe",         "cosmological", "Age of universe (s)"),
    ("z_BBN",           "z_BBN",              "cosmological", "BBN redshift"),
    ("eta_BBN_obs",     "η_BBN",              "cosmological", "Baryon-to-photon ratio"),
    # bands
    ("E_B1",            "E_B1",               "bands",        "B1 band edge"),
    ("E_B2_mean",       "E_B2 mean",          "bands",        "B2 band mean energy"),
]


def fmt_constant_value(name: str, val) -> str:
    """Format a numeric constant for UI display — short, readable, no Python repr."""
    import math
    if val is None:
        return "—"
    if isinstance(val, bool):
        return str(val)
    try:
        f = float(val)
    except (TypeError, ValueError):
        return str(val)
    if not math.isfinite(f):
        return str(val)
    a = abs(f)
    if a == 0:
        return "0"
    if a >= 1e5 or a < 1e-3:
        # Use scientific with 3 significant figures
        return f"{f:.3e}".replace("e+0", "e+").replace("e-0", "e-")
    if a >= 1:
        # reasonable decimal form
        return f"{f:.4g}"
    return f"{f:.4g}"


def infer_tag_from_name(name: str) -> str:
    """Heuristic tagging when no whitelist entry exists."""
    n = name.lower()
    if any(k in n for k in ["m_kk", "m_pl", "m_z", "m_w", "m_h", "m_t", "v_ew"]):
        return "mass scale"
    if any(k in n for k in ["delta", "e_cond", "bcs", "leggett", "e_b1", "e_b2", "e_b3"]):
        return "BCS"
    if any(k in n for k in ["tau", "jensen", "fold"]):
        return "moduli"
    if any(k in n for k in ["omega", "resonance"]):
        return "resonance"
    if any(k in n for k in ["vol_", "haar", "j_c2", "gell"]):
        return "geometry"
    if any(k in n for k in ["alpha_", "g_", "sin2", "thetaw", "coupling"]):
        return "gauge"
    if any(k in n for k in ["t_cmb", "h_0", "omega_m", "omega_l", "omega_dm", "a_s_cmb", "sigma_8",
                             "rho_lambda", "planck", "desi", "bbn", "eta_bbn", "z_bbn", "recomb"]):
        return "cosmological"
    if any(k in n for k in ["c_light", "hbar", "k_b", "ev_", "l_planck", "t_planck", "a_bohr", "arcsec"]):
        return "PDG"
    if any(k in n for k in ["s_fold", "s_inst", "a2_", "a_4", "seeley", "spectral"]):
        return "spectral"
    if any(k in n for k in ["t_ac", "c_gold", "c_fabric", "dt_transit", "rho_s"]):
        return "acoustic"
    if any(k in n for k in ["phi_paasch", "paasch", "golden"]):
        return "mass"
    if any(k in n for k in ["cc_", "lambda_", "lambda/"]):
        return "CC"
    if any(k in n for k in ["audit", "floor"]):
        return "audit"
    return "misc"


def load_canonical_constants():
    """Pull every numeric constant from canonical_constants.py.

    Each is tagged via whitelist → PROVENANCE → heuristic so the UI can
    group/filter them sensibly. Non-numeric entries (dicts, functions) are
    skipped; arrays/tuples are flattened only if scalar-valued.
    """
    sys.path.insert(0, str(ROOT / "computations" / "_shared"))
    import canonical_constants as CC  # noqa
    provenance = getattr(CC, "PROVENANCE", {}) or {}
    whitelist_info = {w[0]: w[1:] for w in CONSTANT_WHITELIST}

    collected = {}
    for name in dir(CC):
        if name.startswith("_"):
            continue
        if name in ("np", "sys", "warnings", "PI", "PROVENANCE", "warn_stale"):
            continue
        val = getattr(CC, name)
        # Skip functions / modules / dicts
        if callable(val) or isinstance(val, (dict, type(CC))):
            continue
        # Only scalar numeric and frozenset/list of numerics
        if not isinstance(val, (int, float, bool)):
            try:
                import numpy as _np
                if isinstance(val, (_np.floating, _np.integer)):
                    val = float(val)
                else:
                    continue
            except Exception:
                continue

        prov = provenance.get(name, {})
        wl = whitelist_info.get(name)

        display = wl[0] if wl else name
        tag = wl[1] if wl else infer_tag_from_name(name)
        note = wl[2] if wl else (prov.get("source", "") or "")

        src_parts = []
        if prov.get("session"):
            src_parts.append(f"Session {prov['session']}")
        if prov.get("source") and (not wl or prov["source"] not in note):
            src_parts.append(prov["source"])
        if prov.get("gate"):
            src_parts.append(f"Gate {prov['gate']}")
        src = " · ".join(src_parts) if src_parts else "canonical_constants.py"

        collected[name] = {
            "id": name,
            "name": display,
            "value": fmt_constant_value(name, val),
            "tag": tag,
            "note": note,
            "src": src,
        }
        if len(collected) >= MAX_CONSTANTS:
            break

    return list(collected.values())


# ============================================================================
# DB extraction
# ============================================================================

def row_dict(cur: sqlite3.Cursor, row) -> dict:
    return {cur.description[i][0]: row[i] for i in range(len(row))}


def get_theorems(con: sqlite3.Connection) -> list[dict]:
    """Top theorems filtered for quality.

    Real theorems have:
      - A `sessions` field populated like 'Session 11', '22b', or a plain integer
      - A concise statement (50-250 chars)
      - No session-wrap prose markers ('Answer**:', 'Changed**:', etc.)
    """
    cur = con.cursor()
    rows = cur.execute(
        """
        SELECT id, name, status, sessions, precision, statement
        FROM theorems
        WHERE sessions IS NOT NULL AND sessions != ''
          AND statement IS NOT NULL AND length(statement) BETWEEN 20 AND 260
        """
    ).fetchall()

    ALPHA = re.compile(r"[A-Za-z]")
    GARBAGE_NAME = re.compile(r"^[\sx\-+=.·×*\d,eE/]+$")
    WRAP_PROSE = re.compile(
        r"(Answer\*\*:|Changed\*\*:|What it is\*\*:|Key insight|Strategy\*\*:)",
        re.I,
    )
    SESS_RE = re.compile(r"^(Session\s+\d+[a-z]?|\d+[a-z]?)(\s*\|\s*.*)?$", re.I)

    out = []
    for r in rows:
        tid, name, status, sessions, precision, statement = r
        nm = (name or "").strip()
        st = (statement or "").strip()
        sess_str = (sessions or "").strip()
        if sess_str.startswith("["):
            try:
                sess_list = json.loads(sess_str)
                sess_str = ", ".join(str(x) for x in sess_list)
            except Exception:
                pass
        # Session reference must look like a real session identifier.
        if not SESS_RE.match(sess_str):
            continue
        if not ALPHA.search(nm) or GARBAGE_NAME.match(nm):
            continue
        if not ALPHA.search(st) or WRAP_PROSE.search(st):
            continue
        area = infer_theorem_area(nm, st)
        out.append({
            "id": tid,
            "name": nm[:120],
            "status": (status or "PROVEN").strip(),
            "session": sess_str or "—",
            "area": area,
            "statement": st,
            "precision": (precision or "").strip(),
        })

    # Rank: prefer shorter IDs (lower proven_N indices are the curated theorems),
    # then by whether precision is populated.
    def sort_key(t):
        m = re.match(r"proven_(\d+)", t["id"])
        idx = int(m.group(1)) if m else 9999
        return (idx, -len(t["precision"]))

    out.sort(key=sort_key)
    return out[:MAX_THEOREMS]


AREA_KEYWORDS = [
    ("spectral", ["spectral", "seeley", "dewitt", "a_2", "a_4", "heat kernel", "dirac"]),
    ("BCS",      ["bcs", "gap", "pairing", "cooper", "condensate", "leggett", "richardson", "gaudin"]),
    ("NCG",      ["ncg", "noncommut", "spectral triple", "barrett", "ko-dim", "finite spectral", "commutant"]),
    ("symmetry", ["cpt", "cp", "charge conjug", "parity", "u(1)", "weyl group", "chirality"]),
    ("transit",  ["transit", "parker", "kibble", "zurek", "instanton", "bogoliubov", "quench"]),
    ("stability",["hessian", "stabil", "monoton", "bound", "saturat", "positive definite"]),
    ("acoustic", ["acoustic", "sound", "goldstone", "phonon", "impedance", "hawking"]),
    ("CC",       ["cosmolog", "constant", "vacuum", "lambda", "cc gap", "λ"]),
    ("cosmo",    ["cmb", "desi", "planck", "hubble", "redshift", "recomb", "bbn", "firas"]),
    ("gauge",    ["gauge", "weinberg", "sin", "coupling", "standard model"]),
    ("simulation", ["gpe", "simulation", "numerical", "ed", "exact diag", "lattice"]),
    ("geometry", ["jensen", "metric", "curvature", "kk", "kaluza", "fiber", "su(3)", "volume"]),
]


def infer_theorem_area(name: str, statement: str) -> str:
    text = f"{name} {statement}".lower()
    for area, kws in AREA_KEYWORDS:
        if any(k in text for k in kws):
            return area
    return "general"


def _summarise_gate_result(result: str) -> str:
    """Collapse the canonical-form result line to value + scheme only."""
    if not result:
        return ""
    text = re.sub(r"\s+", " ", result).strip()
    # Canonical-form: value=X | scheme=Y | convention=Z | L_max=... | sha256=...
    m_val = re.search(r"value=([^|]+?)(?:\s*\||$)", text)
    m_sch = re.search(r"scheme=([^|]+?)(?:\s*\||$)", text)
    parts = []
    if m_val:
        v = m_val.group(1).strip()
        if len(v) > 26:
            v = v[:24] + "…"
        parts.append(f"value={v}")
    if m_sch:
        parts.append(f"scheme={m_sch.group(1).strip()[:32]}")
    if parts:
        return " · ".join(parts)
    # Non-canonical result: just truncate
    return text[:140]


def get_gates(con: sqlite3.Connection) -> list[dict]:
    """Pull gates with canonical verdicts. Prefer gates with a populated
    `condition` field (those are the richer pre-registered gate cards);
    fall back to canonical-form result lines with value/scheme parsed out."""
    cur = con.cursor()
    CLEAN_VERDICTS = (
        "PASS", "FAIL", "INFO", "OPEN", "DIAGNOSTIC", "CLOSED", "HYPOTHESIS", "Diagnostic"
    )
    placeholders = ",".join("?" for _ in CLEAN_VERDICTS)

    # Gate IDs must look like real identifiers: contain a hyphen, no whitespace,
    # at least one uppercase letter, and don't start with a verdict word.
    # Real IDs span short (V-1, K-1e, L-1) to long (CUTOFF-SA-37, QTHEORY-NPAIR-66).
    ID_SHAPE = (
        "id GLOB '*-*' AND length(id) >= 3 AND id NOT GLOB '* *' "
        "AND id GLOB '*[A-Z]*' "
        "AND id NOT LIKE 'PASS%' AND id NOT LIKE 'FAIL%' AND id NOT LIKE 'INFO%'"
    )

    half = MAX_GATES // 2

    # Balance the UI between pre-S81 narrative gates and the S81+ Level-3
    # reproduction gates — otherwise the list is dominated by T3-* reruns.

    # Pass A: pre-S81 (session-narrative gates — condition OR result populated).
    pre81 = cur.execute(
        f"""
        SELECT id, name, session, condition, result, verdict
        FROM gates
        WHERE verdict IN ({placeholders})
          AND {ID_SHAPE}
          AND CAST(session AS INTEGER) < 81
          AND ((condition IS NOT NULL AND length(condition) > 5 AND condition NOT LIKE '%MIGRATED%')
               OR (result IS NOT NULL AND length(result) > 5 AND result NOT LIKE '%MIGRATED%'))
        ORDER BY CASE WHEN session GLOB '[0-9]*' THEN CAST(session AS INTEGER) ELSE 0 END DESC
        LIMIT ?
        """,
        (*CLEAN_VERDICTS, half * 2),
    ).fetchall()

    # Pass B: S81+ Level-3 reruns with canonical-form result lines.
    s81 = cur.execute(
        f"""
        SELECT id, name, session, condition, result, verdict
        FROM gates
        WHERE verdict IN ({placeholders})
          AND {ID_SHAPE}
          AND CAST(session AS INTEGER) >= 81
          AND result IS NOT NULL AND length(result) > 10
          AND result NOT LIKE '%MIGRATED%'
          AND result NOT LIKE '%RUNNABLE%'
        ORDER BY CAST(session AS INTEGER) DESC
        LIMIT ?
        """,
        (*CLEAN_VERDICTS, half * 2),
    ).fetchall()

    # Interleave for narrative diversity in the UI list.
    rich = []
    for a, b in zip(pre81, s81):
        rich.extend([a, b])
    # Append leftovers.
    if len(pre81) > len(s81):
        rich.extend(pre81[len(s81):])
    elif len(s81) > len(pre81):
        rich.extend(s81[len(pre81):])
    fallback = []  # no separate fallback needed now

    seen = set()
    out = []
    for r in [*rich, *fallback]:
        gid, gname, session, cond, result, verdict = r
        if gid in seen:
            continue
        seen.add(gid)
        # Prefer the condition for claim text (real pre-reg content).
        claim_src = (cond or result or gname or "").strip()
        # If it's a canonical-form result line, summarise it.
        if claim_src.startswith("value=") or "| scheme=" in claim_src:
            claim_src = _summarise_gate_result(claim_src)
        claim_text = re.sub(r"\s+", " ", claim_src)[:180]
        verdict_norm = (verdict or "").upper()
        out.append({
            "id": gid,
            "verdict": verdict_norm,
            "session": session or "—",
            "claim": claim_text or gid,
        })
        if len(out) >= MAX_GATES:
            break
    return out


def get_sessions(con: sqlite3.Connection) -> tuple[list[dict], dict]:
    """Fetch sessions. Returns (session_list, id_map where plain '42' → 'S42')."""
    cur = con.cursor()
    rows = cur.execute(
        "SELECT id, date, type, posterior, verdict FROM sessions"
    ).fetchall()

    def numeric_key(rec):
        m = re.match(r"(\d+)", rec[0] or "")
        return int(m.group(1)) if m else 0

    rows.sort(key=numeric_key)
    rows = rows[-MAX_SESSIONS:]

    out = []
    id_map = {}
    for rid, date, stype, posterior, verdict in rows:
        sid = f"S{rid}"
        id_map[rid] = sid
        area = infer_session_area(stype, verdict)
        label = (verdict or stype or f"Session {rid}").strip()
        label = re.sub(r"\s+", " ", label)[:80]
        p = estimate_session_prob(rid)
        out.append({
            "id": sid,
            "label": label or f"Session {rid}",
            "area": area,
            "p": round(p, 3),
            "date": date or "",
        })
    return out, id_map


def infer_session_area(stype, verdict):
    text = f"{stype or ''} {verdict or ''}".lower()
    for area, kws in AREA_KEYWORDS:
        if any(k in text for k in kws):
            return area
    return "general"


def estimate_session_prob(rid: str) -> float:
    """Rough probability trajectory inferred from session number. Matches the
    seed's narrative curve (prior 0.05 → now ~0.40). This is a visual-only
    estimate; the DB probability_trajectory table has the true per-session
    values but is populated sparsely and non-monotonically."""
    m = re.match(r"(\d+)", rid or "")
    n = int(m.group(1)) if m else 0
    if n <= 0:
        return 0.05
    # Logistic curve centred on session 40
    import math
    return 0.05 + 0.35 / (1 + math.exp(-(n - 40) / 10.0))


def get_trajectory(con: sqlite3.Connection, sessions: list[dict]) -> list[dict]:
    """Return one point per session using estimated probability; overlay
    DB probability_trajectory values when they parse cleanly."""
    cur = con.cursor()
    rows = cur.execute(
        "SELECT session, panel, key_event FROM probability_trajectory"
    ).fetchall()

    # Build session → probability from DB where possible
    db_p = {}
    for sess, panel, key_event in rows:
        if not sess or not sess.strip():
            continue
        m = re.match(r"(\d+)", sess.strip())
        if not m:
            continue
        n = int(m.group(1))
        p = parse_panel_prob(panel)
        if p is None:
            continue
        # Keep latest panel per integer session
        db_p[n] = p

    out = []
    for s in sessions:
        m = re.match(r"S(\d+)", s["id"])
        if not m:
            continue
        n = int(m.group(1))
        p = db_p.get(n, s["p"])
        out.append({"t": len(out), "label": s["id"], "p": round(p, 3)})
    return out[-MAX_TRAJECTORY:]


def parse_panel_prob(panel: str):
    """Parse a panel string like '25-35', '43', '0.40' → a 0..1 float or None."""
    if not panel:
        return None
    s = panel.strip().replace("%", "")
    if not s or s.lower() in ("panel", "prior"):
        return None
    # range like "25-35"
    m = re.match(r"^\s*(\d+(?:\.\d+)?)\s*[-–]\s*(\d+(?:\.\d+)?)\s*$", s)
    if m:
        a, b = float(m.group(1)), float(m.group(2))
        return ((a + b) / 2) / 100.0 if a > 1.0 or b > 1.0 else (a + b) / 2
    # single number
    m = re.match(r"^\s*(\d+(?:\.\d+)?)\s*$", s)
    if m:
        v = float(m.group(1))
        return v / 100.0 if v > 1.0 else v
    return None


def get_researchers(con: sqlite3.Connection) -> list[dict]:
    cur = con.cursor()
    rows = cur.execute(
        """
        SELECT domain, paper_count, citation_count, description
        FROM researchers
        WHERE citation_count IS NOT NULL
        ORDER BY citation_count DESC NULLS LAST
        LIMIT ?
        """,
        (MAX_RESEARCHERS,),
    ).fetchall()
    out = []
    for domain, paper_count, cites, desc in rows:
        # Deterministic hue via domain hash
        hue = sum(ord(c) * 7 for c in (domain or "")) % 360
        # Take the first comma-separated concept from the description as the tagline.
        first_kw = (desc or "").split(",", 1)[0].strip()
        if len(first_kw) > 44:
            first_kw = first_kw[:42] + "…"
        label = f"{domain} — {first_kw}" if first_kw else (domain or "unknown")
        out.append({
            "id": (domain or "unknown").lower().replace(" ", "-"),
            "label": label,
            "hue": hue,
            "papers": paper_count or 0,
            "cites": cites or 0,
        })
    return out


def get_derived_edges(sessions: list[dict]) -> list[dict]:
    """Derive a chain-of-thought graph for the Session Ring: consecutive
    sessions in the same area link 'continues', cross-area transitions
    link 'bridges'. The DB's typed edges all target constants/gates, not
    sessions, so we synthesize a visual scaffold here."""
    out = []
    for a, b in zip(sessions, sessions[1:]):
        rel = "continues" if a["area"] == b["area"] else "bridges"
        out.append({"from": b["id"], "to": a["id"], "rel": rel})
    return out


def get_real_edges(con: sqlite3.Connection) -> list[dict]:
    """Extract the real 63 typed edges from the DB for Drill-to-Bedrock display."""
    cur = con.cursor()
    rows = cur.execute(
        "SELECT type, source_type, source_id, target_type, target_id, comment FROM edges"
    ).fetchall()
    return [
        {
            "type": t, "srcType": st, "src": si,
            "tgtType": tt, "tgt": ti, "comment": (c or "")[:140],
        }
        for (t, st, si, tt, ti, c) in rows
    ]


def get_classes(con: sqlite3.Connection) -> list[dict]:
    """Extract canonical classes from knowledge.db::classes (S86+).

    Each class is a named grouping of constants (CC, KK, alpha_s, fold,
    Higgs, ...). Defensive against pre-S86 DBs that lack the table —
    returns [] silently. Includes a `members_count` field computed from
    class_edges so the UI can rank classes by size without a separate
    query.
    """
    cur = con.cursor()
    try:
        rows = cur.execute(
            "SELECT id, name, tier, parent_id, description, seed_session "
            "FROM classes ORDER BY tier, id"
        ).fetchall()
    except sqlite3.OperationalError:
        # Table doesn't exist — pre-S86 DB; emit empty list.
        return []

    # Member counts (for UI ranking and tooltip display)
    try:
        count_rows = cur.execute(
            "SELECT src, COUNT(*) FROM class_edges "
            "WHERE type='contains' AND tgt_type='constants' "
            "GROUP BY src"
        ).fetchall()
        member_counts = {src: n for (src, n) in count_rows}
    except sqlite3.OperationalError:
        member_counts = {}

    out = []
    for (cid, name, tier, parent_id, desc, seed) in rows:
        desc_str = (desc or "").strip()
        out.append({
            "id": cid,
            "name": (name or "").strip(),
            "tier": int(tier or 0),
            "parent_id": parent_id,           # may be None for root classes
            "description": desc_str[:200],     # short for tooltips
            "description_full": desc_str,      # full text for detail views
            "seed_session": (seed or "").strip(),
            "members_count": member_counts.get(cid, 0),
        })
    return out


def get_class_edges(con: sqlite3.Connection) -> list[dict]:
    """Extract class_edges (S86+) — the 'contains' / 'parent_of' relationships
    between classes and constants/classes.

    Shape mirrors REAL_EDGES (srcType/src/tgtType/tgt) so the renderer can
    consume both streams with one helper. Distinct from REAL_EDGES because
    the user wanted these stored as a separate collection — same format,
    different semantics (curated grouping registry vs tagged-link harvest).
    """
    cur = con.cursor()
    try:
        rows = cur.execute(
            "SELECT type, src_type, src, tgt_type, tgt, role, comment "
            "FROM class_edges"
        ).fetchall()
    except sqlite3.OperationalError:
        return []

    return [
        {
            "type": t,
            "srcType": st,
            "src": si,
            "tgtType": tt,
            "tgt": ti,
            "role": role,           # PRIMARY / DERIVED / RELATED, or None for parent_of
            "comment": (c or "")[:140],
        }
        for (t, st, si, tt, ti, role, c) in rows
    ]


# ============================================================================
# Closed mechanisms / open channels / display equations
# ============================================================================

WRAP_PROSE_RE = re.compile(
    r"^(Question\*\*|Previous condition\*\*|Answer\*\*|Changed\*\*|What it is\*\*|Key insight|Strategy\*\*|"
    r"Before\*\*|After\*\*|Why\*\*|How\*\*|Goal\*\*|Status\*\*)",
    re.I,
)


def get_closed_mechanisms(con: sqlite3.Connection) -> list[dict]:
    cur = con.cursor()
    rows = cur.execute(
        """
        SELECT id, name, closed_by, session, gate_id
        FROM closed_mechanisms
        WHERE name IS NOT NULL AND length(name) > 6
        """
    ).fetchall()
    out = []
    for r in rows:
        mid, name, closed_by, session, gate_id = r
        nm = (name or "").strip()
        if WRAP_PROSE_RE.match(nm):
            continue
        out.append({
            "id": mid,
            "name": nm[:140],
            "closed_by": (closed_by or "").strip()[:200],
            "session": (session or "—").strip()[:40],
            "gate": (gate_id or "").strip(),
        })
        if len(out) >= MAX_CLOSED:
            break
    return out


def get_open_channels(con: sqlite3.Connection) -> list[dict]:
    cur = con.cursor()
    rows = cur.execute(
        """
        SELECT rowid, name, detail_1, detail_2, session
        FROM open_channels
        WHERE name IS NOT NULL AND length(name) > 3
        """
    ).fetchall()
    out = []
    seen = set()
    for r in rows:
        rid, name, d1, d2, session = r
        nm = (name or "").strip()
        if WRAP_PROSE_RE.match(nm):
            continue
        key = nm.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append({
            "id": f"open_{rid}",
            "name": nm[:120],
            "detail": re.sub(r"\s+", " ", (d1 or ""))[:180],
            "status": re.sub(r"\s+", " ", (d2 or ""))[:180],
            "session": (session or "—").strip()[:40],
        })
        if len(out) >= MAX_OPEN:
            break
    return out


def get_display_equations(con: sqlite3.Connection) -> list[dict]:
    """Pull ALL display-type equations from the DB. These form the equation
    library — a browsable/searchable grid rendered by the Library view."""
    cur = con.cursor()
    rows = cur.execute(
        """
        SELECT id, raw, file, line, context
        FROM equations
        WHERE type = 'display'
          AND raw IS NOT NULL AND length(raw) > 5
        ORDER BY CAST(substr(id, 4) AS INTEGER) ASC
        LIMIT ?
        """,
        (MAX_EQUATIONS_LIB,),
    ).fetchall()
    out = []
    for r in rows:
        eid, raw, file_, line, ctx = r
        # Trim context to one sentence
        ctx_trim = (ctx or "").strip()
        ctx_trim = re.sub(r"\s+", " ", ctx_trim)[:180]
        out.append({
            "id": eid,
            "tex": (raw or "").strip(),
            "file": (file_ or "").strip(),
            "line": int(line) if line else 0,
            "context": ctx_trim,
        })
    return out


# ============================================================================
# Template assembly
# ============================================================================

def extract_seed_block(block_name: str, seed_text: str) -> str:
    """Return the *source text* of the `const BLOCK = [...]` or function definition
    from the seed file so it can be embedded verbatim."""
    # Block name can be a const array ("const NAME = [...")
    # or a function definition ("function name(...)").
    if block_name == "EQUATIONS":
        pattern = r"(const EQUATIONS = \[[\s\S]*?\];\n)"
    elif block_name == "PAASCH":
        pattern = r"(const PAASCH = \(\(\) => \{[\s\S]*?\}\)\(\);\n)"
    elif block_name == "buildSpectrum":
        pattern = r"(function buildSpectrum\(tau\)\{[\s\S]*?\n  \}\n)"
    elif block_name == "mulberry32":
        pattern = r"(function mulberry32\(seed\)\{[\s\S]*?\n  \}\n)"
    else:
        raise ValueError(block_name)
    m = re.search(pattern, seed_text)
    if not m:
        raise RuntimeError(f"Could not find block {block_name} in seed")
    return m.group(1)


def js_array(items: list[dict], indent: int = 4) -> str:
    """Pretty-print a list of dicts as JS object literals (JSON is JS-safe here)."""
    pad = " " * indent
    lines = []
    for it in items:
        lines.append(pad + json.dumps(it, ensure_ascii=False))
    return "[\n" + ",\n".join(lines) + "\n" + " " * (indent - 2) + "]"


def extract_seed_array(name: str, seed_text: str):
    """Parse a seed `const NAME = [ ...object literals... ];` block.

    Uses explicit bracket counting (aware of string literals) rather than a
    regex, because some theorem statements contain `];` inside single-quoted
    strings (e.g., `S[D];`) which would terminate a non-greedy regex early.
    """
    # Find the opening `const NAME = [`.
    m = re.search(rf"const {re.escape(name)} = \[", seed_text)
    if not m:
        return []
    start = m.end()
    depth = 1          # we've already entered one `[`
    in_str = False
    i = start
    n = len(seed_text)
    while i < n and depth > 0:
        ch = seed_text[i]
        if in_str:
            if ch == "\\":
                i += 2
                continue
            if ch == "'":
                in_str = False
        else:
            if ch == "'":
                in_str = True
            elif ch == "[":
                depth += 1
            elif ch == "]":
                depth -= 1
                if depth == 0:
                    break
        i += 1
    body = seed_text[start:i]
    # The seed uses object literals with single-quoted values and unquoted keys.
    # Convert to JSON: quote keys, switch quotes, preserve escape sequences.
    # Easier path: parse each `{ ... }` with a permissive tokenizer via eval on a
    # sandboxed dict. We use `ast.literal_eval` after substituting JS syntax for
    # Python syntax carefully.
    # Since we only need id/name/value/etc as strings, a focused per-item regex is
    # robust enough for the six arrays we care about.
    items = []
    # Split top-level { ... } blocks that are direct list children.
    depth = 0
    start = None
    for i, ch in enumerate(body):
        if ch == "{":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0 and start is not None:
                items.append(body[start:i + 1])
                start = None
    parsed = []
    for it in items:
        obj = {}
        for km in re.finditer(
            r"(?P<k>[A-Za-z_][A-Za-z_0-9]*)\s*:\s*'(?P<v>(?:[^'\\]|\\.)*)'",
            it,
        ):
            # Collapse only the JS escape sequences we care about (\', \\, \n).
            # Do NOT go through `unicode_escape`, which corrupts valid multi-byte
            # UTF-8 codepoints like τ (U+03C4) and ³² (superscripts).
            v = km.group("v")
            v = v.replace(r"\'", "'").replace(r"\\", "\\").replace(r"\n", "\n")
            obj[km.group("k")] = v
        if obj:
            parsed.append(obj)
    return parsed


def build_data_js(seed_text: str) -> str:
    con = sqlite3.connect(str(DB_PATH))
    try:
        constants = load_canonical_constants()
        theorems = get_theorems(con)
        gates = get_gates(con)
        sessions, _ = get_sessions(con)
        trajectory = get_trajectory(con, sessions)
        researchers = get_researchers(con)
        derived_edges = get_derived_edges(sessions)
        real_edges = get_real_edges(con)
        closed_mechanisms = get_closed_mechanisms(con)
        open_channels = get_open_channels(con)
        equation_lib = get_display_equations(con)
        classes = get_classes(con)              # S86+ (empty if pre-S86 DB)
        class_edges = get_class_edges(con)      # S86+ (empty if pre-S86 DB)
    finally:
        con.close()

    # Merge seed entries so the hand-curated Equation Atlas chips can still
    # resolve to theorems/gates/constants by their original seed IDs.
    seed_constants = extract_seed_array("CONSTANTS", seed_text)
    seed_theorems = extract_seed_array("THEOREMS", seed_text)
    seed_gates = extract_seed_array("GATES", seed_text)

    live_ids = {c["id"] for c in constants}
    for sc in seed_constants:
        if sc.get("id") and sc["id"] not in live_ids:
            sc["src"] = f"{sc.get('src','seed')} (seed)"
            constants.append(sc)
            live_ids.add(sc["id"])

    live_thm = {t["id"] for t in theorems}
    for st in seed_theorems:
        if st.get("id") and st["id"] not in live_thm:
            theorems.append(st)
            live_thm.add(st["id"])

    live_gate = {g["id"] for g in gates}
    for sg in seed_gates:
        if sg.get("id") and sg["id"] not in live_gate:
            gates.append(sg)
            live_gate.add(sg["id"])

    # Preserved blocks from seed
    equations_block = extract_seed_block("EQUATIONS", seed_text)
    paasch_block = extract_seed_block("PAASCH", seed_text)
    spectrum_fn = extract_seed_block("buildSpectrum", seed_text)
    mul_fn = extract_seed_block("mulberry32", seed_text)

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    header = f"""// Ainulindalë Exflation — LIVE data slice (generated).
// Generated: {now}
// Source:    tools/knowledge.db + computations/_shared/canonical_constants.py
// Generator: tools/viz/console/build_data.py
//
// The hand-curated fallback lives at data.seed.js; swap <script src="data.js">
// for <script src="data.seed.js"> in index.html to revert.

"""

    body = (
        "window.AE_DATA = (() => {\n"
        "  // --------------------------------------------------------------\n"
        f"  //  CONSTANTS  ({len(constants)} from canonical_constants.py)\n"
        "  // --------------------------------------------------------------\n"
        f"  const CONSTANTS = {js_array(constants, 4)};\n\n"
        "  // --------------------------------------------------------------\n"
        f"  //  THEOREMS   ({len(theorems)} from knowledge.db::theorems)\n"
        "  // --------------------------------------------------------------\n"
        f"  const THEOREMS = {js_array(theorems, 4)};\n\n"
        "  // --------------------------------------------------------------\n"
        f"  //  GATES      ({len(gates)} from knowledge.db::gates, whitelist verdicts)\n"
        "  // --------------------------------------------------------------\n"
        f"  const GATES = {js_array(gates, 4)};\n\n"
        "  // --------------------------------------------------------------\n"
        f"  //  CLOSED_MECHANISMS ({len(closed_mechanisms)} from knowledge.db::closed_mechanisms)\n"
        "  // --------------------------------------------------------------\n"
        f"  const CLOSED_MECHANISMS = {js_array(closed_mechanisms, 4)};\n\n"
        "  // --------------------------------------------------------------\n"
        f"  //  OPEN_CHANNELS ({len(open_channels)} from knowledge.db::open_channels)\n"
        "  // --------------------------------------------------------------\n"
        f"  const OPEN_CHANNELS = {js_array(open_channels, 4)};\n\n"
        "  // --------------------------------------------------------------\n"
        f"  //  CLASSES    ({len(classes)} from knowledge.db::classes — canonical_classes.py groupings)\n"
        "  // --------------------------------------------------------------\n"
        f"  const CLASSES = {js_array(classes, 4)};\n\n"
        "  // --------------------------------------------------------------\n"
        f"  //  CLASS_EDGES ({len(class_edges)} from knowledge.db::class_edges — class membership / parent_of)\n"
        "  //  Same shape as REAL_EDGES; separate collection by design (curated grouping, not link harvest).\n"
        "  // --------------------------------------------------------------\n"
        f"  const CLASS_EDGES = {js_array(class_edges, 4)};\n\n"
        "  // --------------------------------------------------------------\n"
        "  //  EQUATIONS  (hand-curated atlas — preserved from data.seed.js)\n"
        "  // --------------------------------------------------------------\n"
        f"  {equations_block}\n"
        "  // --------------------------------------------------------------\n"
        f"  //  EQUATION_LIB ({len(equation_lib)} display-type LaTeX equations from knowledge.db::equations)\n"
        "  // --------------------------------------------------------------\n"
        f"  const EQUATION_LIB = {js_array(equation_lib, 4)};\n\n"
        "  // --------------------------------------------------------------\n"
        f"  //  SESSIONS   ({len(sessions)} from knowledge.db::sessions, last {MAX_SESSIONS})\n"
        "  // --------------------------------------------------------------\n"
        f"  const SESSIONS = {js_array(sessions, 4)};\n\n"
        "  // --------------------------------------------------------------\n"
        f"  //  EDGES      (session-ring continuity, derived from session order)\n"
        "  // --------------------------------------------------------------\n"
        f"  const EDGES = {js_array(derived_edges, 4)};\n\n"
        "  // --------------------------------------------------------------\n"
        f"  //  REAL_EDGES ({len(real_edges)} from knowledge.db::edges — typed reproduces/depends_on links)\n"
        "  // --------------------------------------------------------------\n"
        f"  const REAL_EDGES = {js_array(real_edges, 4)};\n\n"
        "  // --------------------------------------------------------------\n"
        "  //  SPECTRUM BUILDER (from data.seed.js)\n"
        "  // --------------------------------------------------------------\n"
        f"  {spectrum_fn}\n"
        f"  {mul_fn}\n"
        "  // --------------------------------------------------------------\n"
        f"  //  PAASCH SEQUENCES (from data.seed.js)\n"
        "  // --------------------------------------------------------------\n"
        f"  {paasch_block}\n"
        "  // --------------------------------------------------------------\n"
        "  //  TRAJECTORY\n"
        "  // --------------------------------------------------------------\n"
        f"  const TRAJECTORY = {js_array(trajectory, 4)};\n\n"
        "  // --------------------------------------------------------------\n"
        f"  //  RESEARCHERS ({len(researchers)} from knowledge.db::researchers)\n"
        "  // --------------------------------------------------------------\n"
        f"  const RESEARCHERS = {js_array(researchers, 4)};\n\n"
        "  return {\n"
        "    CONSTANTS, THEOREMS, GATES, EQUATIONS, EQUATION_LIB,\n"
        "    CLOSED_MECHANISMS, OPEN_CHANNELS,\n"
        "    CLASSES, CLASS_EDGES,\n"
        "    SESSIONS, EDGES, REAL_EDGES, TRAJECTORY, RESEARCHERS, PAASCH,\n"
        "    buildSpectrum,\n"
        "  };\n"
        "})();\n"
    )
    return header + body


def main():
    if not DB_PATH.exists():
        print(f"[build_data] ERROR: {DB_PATH} missing. Run `/weave --db-sync` first.", file=sys.stderr)
        sys.exit(1)
    if not SEED_PATH.exists():
        print(f"[build_data] ERROR: {SEED_PATH} missing. data.seed.js is required as a source of the visualization blocks.", file=sys.stderr)
        sys.exit(1)
    seed_text = SEED_PATH.read_text(encoding="utf-8")
    out_text = build_data_js(seed_text)
    OUT_PATH.write_text(out_text, encoding="utf-8")
    print(f"[build_data] wrote {OUT_PATH} ({len(out_text):,} bytes)")


if __name__ == "__main__":
    main()
