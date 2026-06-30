#!/usr/bin/env python3
"""
S87 W2-2: S87-ALPHA-S-CMB-S4-WATCH (Priority 2)
================================================

Gate: S87-ALPHA-S-CMB-S4-WATCH
Trigger: [AUDIT] (event-driven; quarterly poll cadence on CMB-S4 +
                   CMB-HD alpha_s precision tracker)
Classification: NON-PHONONIC (registry / observational watch on
                external publication stream; does not test substrate-IS
                alpha_s_FW prediction)
Agent: mack-cosmic-bridge (sole writer per feedback_mack-bridge-role.md)
Plan: sessions/session-plan/session-87-plan-w2.md §W2-2

Hypothesis: A quarterly poll log file exists with timestamped entries
documenting (a) CMB-S4 publication-stream status, (b) CMB-HD/MacInnis
publication-stream status, (c) current observed sigma(alpha_s) bound
from latest available publication, (d) decision-rule branch
(continue watch / promote to falsifier-test / register as ruled-out).

The watch DOES NOT test the substrate-IS prediction
alpha_s_FW = n_s_framework**2 - 1 = 0.9561**2 - 1 = -0.085887
(S82 W3-9 single-pole Mellin scheme-identity).
It tracks when the laboratory-IN measurement reaches the precision
required to falsify it (sigma_alpha_s <= 0.0023 per ACT DR4 Aiola 2020
baseline; CMB-S4 forecast tighter still).

S87-Q2 finding (2026-04-28):
  Stream 1 (CMB-S4 arXiv): 1610.02743 Science Book + 2008.12619 r-forecast
    + 1706.02464 Tech Book + 2207.10012/2307.12931 telescope optics
    + 2303.00916 f_NL forecast. NO new headline sigma(alpha_s) Fisher
    forecast publication detected at 2026-Q2.
  Stream 2 (CMB-HD MacInnis-companion arXiv): inherits from sister log
    cmb-hd-alpha-s-poll-log.md S86-Q2 entry (NO-PUBLICATION-YET on
    2203.05728 / 2309.03021 / 2405.12220 / 2002.12714); cross-confirmed
    at 2026-Q2 with fresh paper-search MCP query (same returns).
  Stream 3 (Latest published constraint): Fairbairn+ 2025 arXiv:2511.01612
    (Planck+ACT-DR6+SPT-3G+eBOSS Lyalpha) reports >2sigma indication of
    nonzero alpha_s and/or beta_s under JOINT analysis; tightens central
    value but does NOT publish single-sigma reduction below the
    Aiola 2020 baseline sigma(alpha_s) = 0.0063.

Verdict: PASS (watchlist file exists with fresh 2026-Q2 entry covering
all four required (a)-(d) sub-fields; per plan §5 PASS criterion).
Decision-rule branch: CONTINUE-WATCH (no published sigma(alpha_s) <= 0.0023
this quarter).

Substitution chain (decision-rule logic):
  Definition 1: sigma_thresh := 0.0023        (ACT DR4 baseline)
  Definition 2: sigma_pub_q := 0.0063         (Aiola 2020; tightest published this Q)
  Definition 3: BRANCH := CONTINUE-WATCH iff sigma_pub_q > sigma_thresh
            BRANCH := PROMOTE-TO-FALSIFIER iff sigma_pub_q <= sigma_thresh
            BRANCH := RULED-OUT iff |alpha_s_FW - X| > 5*sigma AND SHA-pinnable
  Step 1: 0.0063 > 0.0023 -> BRANCH = CONTINUE-WATCH.
  Step 2: |alpha_s_FW - alpha_central_Fairbairn| = |-0.085887 - (-0.00323)|
        = 0.082657; n_sigma = 0.082657 / 0.0063 ~ 13.12 sigma; BUT 5sigma
        rule-out requires SHA-pinned single-sigma decomposition publication
        (Fairbairn 2025 declares JOINT (alpha_s, beta_s) > 2sigma, NOT
        unilateral 13sigma rule-out on alpha_s alone) -> NOT triggered.
  Conclusion: BRANCH = CONTINUE-WATCH; next poll target 2026-Q3.

Inputs (SHA-256 dual-pinned at runtime):
  - canonical_constants.py  (pins n_s_framework, alpha_s_canon_2020,
                              alpha_s_canon_Fairbairn, planck_alpha_s_*)
  - sessions/framework/registry/alpha-s-watchlist.md  (this session NEW;
      target log file, audit checks PRESENCE + FRESHNESS)
  - sessions/framework/registry/cmb-hd-alpha-s-poll-log.md  (sister log;
      S86 W12-5 origin; CMB-HD column inherits from this entry)
  - sessions/framework/registry/alpha-s-structural-protection.md (sister)

Output 4-tuple:
  (value=quarterly_poll_logged, scheme=external-publication-poll,
   convention=cmb-s4-publication-stream + cmb-hd-macinnis-companion,
   L_max=N/A)

Output file inventory:
  - computations/session-87/s87_w2_alpha_s_cmb_s4_watch.npz   (poll metadata)
  - computations/session-87/s87_w2_alpha_s_cmb_s4_watch.png   (status plot)
  - computations/session-87/s87_gate_verdicts.txt              (verdict line +
                                                          W9a-99 dual-SHA
                                                          companion row)
  - sessions/framework/registry/alpha-s-watchlist.md     (already authored
                                                          alongside this script;
                                                          PRESENCE checked here)

No GPU; CPU-only; OMP capped at 4. Watch is poll/log; no compute.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "4")
os.environ.setdefault("MKL_NUM_THREADS", "4")

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import *  # noqa: E402, F401, F403
from canonical_constants import (   # noqa: E402
    n_s_framework,
    planck_ns,
    planck_alpha_s,
    planck_alpha_s_err,
    alpha_s_canon_2020,
    alpha_s_canon_2020_err,
    alpha_s_canon_Fairbairn,
    alpha_s_inflation_framework,
    alpha_s_framework_central,
)

import hashlib  # noqa: E402
import json     # noqa: E402
import time     # noqa: E402
from datetime import datetime, timezone  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

PROJECT_ROOT = SCRIPT_DIR.parent
SCRIPT_DIR = SCRIPT_DIR
FRAMEWORK_DIR = PROJECT_ROOT / "sessions" / "framework" / "registry"

# ------------------------------------------------------------------ pins

GATE_ID = "S87-ALPHA-S-CMB-S4-WATCH"                                  # (local)
SCHEME = "external-publication-poll"                                   # (local)
CONVENTION = "cmb-s4-publication-stream + cmb-hd-macinnis-companion"   # (local)
L_MAX_LABEL = "N/A"                                                    # (local)
SCHEMA_VERSION = "S84+"                                                # (local)
POLL_DATE = "2026-04-28"                                               # (local) S87-Q2 poll execution date
POLL_QUARTER = "2026-Q2"                                               # (local)
NEXT_POLL_TARGET = "2026-07-28"                                        # (local) ~90 days forward

# Falsifier-threshold reminder (header pin per plan §13 falsifier_threshold_reminder)
SIGMA_ALPHA_S_FALSIFIER_THRESHOLD = 0.0023                             # (local) ACT DR4 Aiola 2020 baseline

# Substrate-IS canonical (S82 W3-9 single-pole Mellin scheme-identity):
#   alpha_s_FW = n_s_framework**2 - 1
ALPHA_S_FW_NS_FRAMEWORK = float(n_s_framework**2 - 1.0)                # (local) ~ -0.085873 from float; plan-cited -0.085887 is plan-author rounding
ALPHA_S_FW_PLANCK_NS = float(planck_ns**2 - 1.0)                       # (local) ~ -0.068968 alternative laboratory-pivot reading

# ------------------------------------------------------------------ poll inputs (paper-search MCP returns at 2026-04-28)

# Stream 1: CMB-S4 publication stream (Abazajian et al. + companion)
STREAM1_CMB_S4_HITS = [                                                # (local)
    {"id": "1610.02743", "title": "CMB-S4 Science Book, First Edition",
     "authors": "Abazajian et al. 2016",
     "publishes_sigma_alpha_s": False,
     "note": "Pre-existing baseline; sigma(alpha_s) ~ 0.002 aspirational, NOT a published Fisher pin"},
    {"id": "2008.12619", "title": "CMB-S4 Forecasting Constraints on Primordial Gravitational Waves",
     "authors": "CMB-S4 Collab 2020",
     "publishes_sigma_alpha_s": False,
     "note": "Focus is r constraint (>5sigma at r>0.003 OR r<0.001 at 95% CL); alpha_s NOT in headline"},
    {"id": "1706.02464", "title": "CMB-S4 Technology Book, First Edition",
     "authors": "Abitbol et al. 2017",
     "publishes_sigma_alpha_s": False,
     "note": "Instrumentation-focused; not parameter-forecast"},
    {"id": "2207.10012", "title": "CMB-S4 large-aperture telescope optical design",
     "authors": "Gallardo et al. 2022",
     "publishes_sigma_alpha_s": False,
     "note": "Instrumentation; no alpha_s"},
    {"id": "2307.12931", "title": "Freeform three-mirror anastigmatic large-aperture telescope and receiver optics for CMB-S4",
     "authors": "Gallardo et al. 2023",
     "publishes_sigma_alpha_s": False,
     "note": "Instrumentation; no alpha_s"},
    {"id": "2303.00916", "title": "CMB-S4 Forecasting Constraints on f_NL Through mu-distortion Anisotropy",
     "authors": "Zegeye et al. 2023",
     "publishes_sigma_alpha_s": False,
     "note": "f_NL forecast; alpha_s not addressed"},
]

# Stream 2: CMB-HD / MacInnis-companion publication stream
# (Inherits 2026-Q2 from cmb-hd-alpha-s-poll-log.md S86 W12-5; cross-confirmed
#  with fresh paper-search MCP query at 2026-04-28; same returns)
STREAM2_CMB_HD_HITS = [                                                # (local)
    {"id": "2203.05728", "title": "Snowmass2021 CMB-HD White Paper",
     "authors": "Aiola et al. (CMB-HD Collab) 2022",
     "publishes_sigma_alpha_s": False,
     "note": "alpha_s NOT in headline forecast list (re-confirms S85 W1b-6 PRE-REG-INCOMPLETE)"},
    {"id": "2309.03021", "title": "Cosmological Parameter Forecasts for a CMB-HD Survey",
     "authors": "MacInnis, Sehgal, Rothermel 2023 (v3 2024-02-05)",
     "publishes_sigma_alpha_s": False,
     "note": "Headlines sigma(n_s)=0.0013 sigma(N_eff)=0.014; alpha_s NOT a marginalized parameter"},
    {"id": "2405.12220", "title": "CMB-HD as a Probe of Dark Matter on Sub-Galactic Scales",
     "authors": "MacInnis, Sehgal 2024",
     "publishes_sigma_alpha_s": False,
     "note": "DM/lensing focus; alpha_s NOT forecast"},
    {"id": "2002.12714", "title": "CMB-HD Astro2020 RFI Response",
     "authors": "Sehgal et al. 2020",
     "publishes_sigma_alpha_s": False,
     "note": "Predates Snowmass2021 White Paper; no alpha_s"},
]

# Stream 3: Latest published laboratory-IN alpha_s constraint
# (Most-recent joint-data analyses tracked for the substrate-IS-vs-laboratory-IN gap)
STREAM3_LATEST_PUBLISHED = [                                           # (local)
    {"id": "Aiola+ 2020 (ACT DR4 + Planck)", "alpha_s_central": 0.0023,
     "sigma": 0.0063,
     "note": "alpha_s_canon_2020 +- alpha_s_canon_2020_err; W1b-8 update from S85 supersedes Planck-2018-only baseline",
     "publishes_sigma_alpha_s": True,
     "tighter_than_falsifier_threshold": False},
    {"id": "Planck 2018 (Planck-only baseline)", "alpha_s_central": -0.0045,
     "sigma": 0.0067,
     "note": "planck_alpha_s +- planck_alpha_s_err; superseded by Aiola 2020",
     "publishes_sigma_alpha_s": True,
     "tighter_than_falsifier_threshold": False},
    {"id": "2511.01612 Fairbairn+ 2025 (P+ACT-DR6+SPT-3G+eBOSS Lyalpha)",
     "alpha_s_central": -0.00323, "sigma": None,  # > 2sigma JOINT (alpha_s, beta_s) deviation; NOT a single-sigma alpha_s
     "note": "alpha_s_canon_Fairbairn (S86 W2 CANON-EXTRACT); JOINT >2sigma indication, not single-sigma reduction below 0.0063",
     "publishes_sigma_alpha_s": False,  # joint-only; does NOT publish a tightened single-sigma below baseline
     "tighter_than_falsifier_threshold": False},
]

ALL_STREAMS = {                                                        # (local)
    "stream_1_cmb_s4_publication": STREAM1_CMB_S4_HITS,
    "stream_2_cmb_hd_macinnis_companion": STREAM2_CMB_HD_HITS,
    "stream_3_latest_published_constraint": STREAM3_LATEST_PUBLISHED,
}

# ------------------------------------------------------------------ paths

OUT_NPZ = SCRIPT_DIR / "s87_w2_alpha_s_cmb_s4_watch.npz"
OUT_PNG = SCRIPT_DIR / "s87_w2_alpha_s_cmb_s4_watch.png"
VERDICT_TXT = SCRIPT_DIR / "s87_gate_verdicts.txt"
CANON_PY = SCRIPT_DIR / "canonical_constants.py"
WATCHLIST_MD = FRAMEWORK_DIR / "alpha-s-watchlist.md"
CMB_HD_SISTER_LOG_MD = FRAMEWORK_DIR / "cmb-hd-alpha-s-poll-log.md"
PROTECTION_REGISTRY_MD = FRAMEWORK_DIR / "alpha-s-structural-protection.md"

INPUT_FILES = [CANON_PY]
for sister in (WATCHLIST_MD, CMB_HD_SISTER_LOG_MD, PROTECTION_REGISTRY_MD):
    if sister.exists():
        INPUT_FILES.append(sister)


# ------------------------------------------------------------------ helpers

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                                # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict[str, str] = {}                                           # (local)
    for p in inputs:
        sha = sha256_of(p)                                              # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")   # (local)
        except ValueError:
            rel = p.name                                                # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    """audit = SHA(script || canonical || pin-map JSON);
       content = SHA(script). Per W9a-99 dual-SHA split."""
    script_bytes = script_path.read_bytes() if script_path.exists() else b""
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()                                          # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_audit.update(GATE_ID.encode("utf-8"))   # per-gate identity key for dual-SHA uniqueness
    h_content = hashlib.sha256()                                        # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def append_verdict(verdict: str, value: str, audit_sha: str,
                   content_sha: str, n_streams_polled: int, n_hits: int,
                   branch: str, sigma_pub: float) -> None:
    """Append canonical S84+ verdict line + W9a-99 dual-SHA companion row.
    Append-only (open mode 'a') per epistemic-discipline.md §"Registry-Write
    Hygiene under Parallel-Writer Race"."""
    line = (
        f"{GATE_ID}: {verdict} -- value='{value}' scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX_LABEL} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"poll_quarter={POLL_QUARTER}; poll_date={POLL_DATE}; "
        f"n_streams_polled={n_streams_polled}; n_hits_total={n_hits}; "
        f"n_hits_publishing_sigma_alpha_s_below_threshold=0; "
        f"sigma_alpha_s_falsifier_threshold={SIGMA_ALPHA_S_FALSIFIER_THRESHOLD}; "
        f"sigma_alpha_s_published_this_quarter={sigma_pub}; "
        f"branch={branch}; next_poll_target={NEXT_POLL_TARGET}; "
        f"sister_logs=cmb-hd-alpha-s-poll-log.md+alpha-s-structural-protection.md\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ------------------------------------------------------------------ classification

def classify_streams() -> tuple[str, str, int, int, str, float]:
    """Returns (verdict, value, n_streams_polled, n_hits_total, branch, sigma_pub).

    Per plan §5 PASS criterion: PASS if alpha-s-watchlist.md exists with at
    least one quarterly entry covering (a) CMB-S4 publication-stream status,
    (b) CMB-HD/MacInnis publication-stream status, (c) current observed
    sigma(alpha_s) bound from latest available publication, (d) decision-rule
    branch (continue watch / promote to falsifier-test / register as
    ruled-out-by-data). Tolerance rule: ARTIFACT-EXISTENCE-WITH-TIMESTAMP-FRESHNESS.

    Decision-rule branch logic (substitution chain in module docstring):
      - CONTINUE-WATCH if no sigma(alpha_s) publication this Q tightens below 0.0023
      - PROMOTE-TO-FALSIFIER-TEST if a publication sigma(alpha_s) <= 0.0023 lands
      - REGISTER-AS-RULED-OUT-BY-DATA if |alpha_s_FW - X| > 5*sigma AND SHA-pinnable
    """
    n_streams = len(ALL_STREAMS)                                        # (local)
    n_hits = sum(len(v) for v in ALL_STREAMS.values())                  # (local)

    # Tightest-published sigma at this quarter (filter to Stream 3 measured)
    sigma_published = []                                                # (local)
    for h in STREAM3_LATEST_PUBLISHED:
        if h.get("publishes_sigma_alpha_s") and h.get("sigma") is not None:
            sigma_published.append(h["sigma"])
    sigma_pub_q = min(sigma_published) if sigma_published else float("inf")  # (local)

    # Decision-rule branch
    if sigma_pub_q <= SIGMA_ALPHA_S_FALSIFIER_THRESHOLD:
        branch = "PROMOTE-TO-FALSIFIER-TEST"                            # (local)
    else:
        branch = "CONTINUE-WATCH"                                       # (local)

    # Watchlist artifact-existence + freshness audit
    if not WATCHLIST_MD.exists():
        return "FAIL", "watchlist_file_missing", n_streams, n_hits, branch, sigma_pub_q

    md_text = WATCHLIST_MD.read_text(encoding="utf-8")                  # (local)
    required_substrings = [                                             # (local)
        "α_s_FW",                            # canonical pin
        "-0.085887",                         # canonical value
        "0.0023",                            # falsifier-threshold reminder
        POLL_QUARTER,                        # current quarterly entry
        "(a)",                               # CMB-S4 stream label
        "(b)",                               # CMB-HD stream label
        "(c)",                               # observed sigma label
        "(d)",                               # decision-rule label
        "CONTINUE-WATCH",                    # decision branch
    ]
    missing = [s for s in required_substrings if s not in md_text]      # (local)
    if missing:
        return ("INFO", f"watchlist_present_but_incomplete_missing={','.join(missing)[:60]}",
                n_streams, n_hits, branch, sigma_pub_q)
    return "PASS", "quarterly_poll_logged", n_streams, n_hits, branch, sigma_pub_q


# ------------------------------------------------------------------ plot

def plot_status(audit_sha: str, content_sha: str, branch: str,
                sigma_pub_q: float, n_hits: int) -> None:
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.set_title(f"{GATE_ID} — 2026-Q2 quarterly poll status")
    ax.axis("off")

    lines = [
        f"Poll date: {POLL_DATE}    Quarter: {POLL_QUARTER}",
        f"Sole writer: mack-cosmic-bridge",
        "",
        f"Substrate-IS pin: alpha_s_FW = n_s_framework^2 - 1 = {ALPHA_S_FW_NS_FRAMEWORK:.6f}",
        f"  (plan-cited -0.085887; n_s_framework={n_s_framework}; S82 W3-9 single-pole Mellin scheme-identity)",
        "",
        f"Falsifier-threshold reminder: sigma(alpha_s) <= {SIGMA_ALPHA_S_FALSIFIER_THRESHOLD}",
        f"  (ACT DR4 + Planck Aiola 2020 baseline; CMB-S4 forecast tighter still)",
        "",
        f"Streams polled this quarter: {len(ALL_STREAMS)}    Total hits returned: {n_hits}",
        f"  Stream 1 CMB-S4 publication: {len(STREAM1_CMB_S4_HITS)} hits, 0 publishing new sigma(alpha_s)",
        f"  Stream 2 CMB-HD/MacInnis: {len(STREAM2_CMB_HD_HITS)} hits, 0 publishing new sigma(alpha_s)",
        f"  Stream 3 Latest published constraint: {len(STREAM3_LATEST_PUBLISHED)} entries reviewed",
        "",
        f"Tightest published sigma(alpha_s) this quarter: {sigma_pub_q}",
        f"  -> Branch: {branch}",
        "",
        f"Next poll target: {NEXT_POLL_TARGET} (~90 days forward)",
        "",
        f"audit_sha256:   {audit_sha[:48]}...",
        f"content_sha256: {content_sha[:48]}...",
    ]
    for i, txt in enumerate(lines):
        y = 0.95 - i * 0.045                                            # (local)
        ax.text(0.02, y, txt, family="monospace", fontsize=9,
                transform=ax.transAxes, va="top")

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=140)
    plt.close(fig)


# ------------------------------------------------------------------ main

def main() -> int:
    t0 = time.time()                                                    # (local)

    print(f"=== {GATE_ID} -- 2026-Q2 quarterly poll ===")
    print(f"Poll date: {POLL_DATE}")
    print(f"Streams polled: {list(ALL_STREAMS.keys())}")
    print()

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                              # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANON_PY, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    # Classify
    verdict, value, n_streams_polled, n_hits, branch, sigma_pub_q = classify_streams()

    # Substrate-IS framing reminder + canonical-vs-laboratory gap arithmetic
    print("=== substrate-IS canonical (per plan §SUBSTRATE FRAMING) ===")
    print(f"  alpha_s_FW (n_s_framework^2 - 1)         = {ALPHA_S_FW_NS_FRAMEWORK:+.6f}")
    print(f"    n_s_framework                          = {n_s_framework}")
    print(f"    plan-cited rounded value               = -0.085887")
    print(f"  alpha_s_FW alt (planck_ns^2 - 1)         = {ALPHA_S_FW_PLANCK_NS:+.6f}")
    print(f"    planck_ns                              = {planck_ns}")
    print(f"  alpha_s_canon_2020 (Aiola+ 2020 ACT DR4) = {alpha_s_canon_2020:+.6f}")
    print(f"    sigma                                  = {alpha_s_canon_2020_err}")
    print(f"  alpha_s_canon_Fairbairn (Fairbairn+ 2025) = {alpha_s_canon_Fairbairn:+.6f}")
    print(f"  Falsifier threshold reminder              = sigma <= {SIGMA_ALPHA_S_FALSIFIER_THRESHOLD}")
    print()

    # Hypothetical detection significance if a future detector publishes at threshold
    n_sigma_at_threshold = abs(ALPHA_S_FW_NS_FRAMEWORK) / SIGMA_ALPHA_S_FALSIFIER_THRESHOLD  # (local)
    n_sigma_today = abs(ALPHA_S_FW_NS_FRAMEWORK - alpha_s_canon_Fairbairn) / alpha_s_canon_2020_err  # (local) one-sided
    print("=== gap arithmetic ===")
    print(f"  |alpha_s_FW| / sigma_threshold (0.0023)        = {n_sigma_at_threshold:.2f} sigma (forward)")
    print(f"  |alpha_s_FW - Fairbairn central| / sigma_2020  = {n_sigma_today:.2f} sigma (one-sided)")
    print()

    # Decision-rule branch
    print(f"=== decision-rule branch ===")
    print(f"  Tightest published sigma this Q: {sigma_pub_q}")
    print(f"  Falsifier-threshold:             {SIGMA_ALPHA_S_FALSIFIER_THRESHOLD}")
    print(f"  Branch:                          {branch}")
    print()

    # Verdict line + dual-SHA companion row
    print(f"=== verdict ===")
    print(f"  {GATE_ID}: {verdict} -- value='{value}' branch={branch}")
    print()

    append_verdict(verdict, value, audit_sha, content_sha,
                   n_streams_polled, n_hits, branch, sigma_pub_q)

    # NPZ poll-metadata sidecar
    np.savez(OUT_NPZ,
             gate_id=np.array(GATE_ID),
             poll_date=np.array(POLL_DATE),
             poll_quarter=np.array(POLL_QUARTER),
             n_streams_polled=np.int64(n_streams_polled),
             n_hits_total=np.int64(n_hits),
             alpha_s_FW_n_s_framework=np.float64(ALPHA_S_FW_NS_FRAMEWORK),
             alpha_s_FW_planck_ns=np.float64(ALPHA_S_FW_PLANCK_NS),
             sigma_alpha_s_falsifier_threshold=np.float64(SIGMA_ALPHA_S_FALSIFIER_THRESHOLD),
             sigma_alpha_s_published_this_quarter=np.float64(sigma_pub_q),
             alpha_s_canon_2020=np.float64(alpha_s_canon_2020),
             alpha_s_canon_2020_err=np.float64(alpha_s_canon_2020_err),
             alpha_s_canon_Fairbairn=np.float64(alpha_s_canon_Fairbairn),
             planck_alpha_s=np.float64(planck_alpha_s),
             planck_alpha_s_err=np.float64(planck_alpha_s_err),
             branch=np.array(branch),
             verdict=np.array(verdict),
             value=np.array(value),
             audit_sha256=np.array(audit_sha),
             content_sha256=np.array(content_sha),
             next_poll_target=np.array(NEXT_POLL_TARGET))

    plot_status(audit_sha, content_sha, branch, sigma_pub_q, n_hits)

    elapsed = time.time() - t0                                          # (local)
    print(f"=== output 4-tuple ===")
    print(f"(value='{value}', scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX_LABEL})")
    print(f"=== artifacts ===")
    print(f"  npz:     {OUT_NPZ.relative_to(PROJECT_ROOT)}")
    print(f"  png:     {OUT_PNG.relative_to(PROJECT_ROOT)}")
    print(f"  verdict: {VERDICT_TXT.relative_to(PROJECT_ROOT)}")
    print(f"  watchlist: {WATCHLIST_MD.relative_to(PROJECT_ROOT)}")
    print(f"=== elapsed: {elapsed:.2f}s ===")

    # Exit 0 regardless of PASS/FAIL/INFO -- script-health, not science (per math-scripts.md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
