#!/usr/bin/env python3
"""
S86 W12-5: S86-CMB-HD-ALPHA-S-FORECAST-PIN (C36)
=================================================

Gate: S86-CMB-HD-ALPHA-S-FORECAST-PIN
Trigger: [AUDIT] (event-driven; quarterly poll cadence)
Classification: META (forecast-monitoring discipline; not substrate physics)
Agent: mack-cosmic-bridge
Plan: sessions/session-plan/session-86-plan-w12.md §W12-5

Hypothesis: Quarterly polling of 3 source streams (Abazajian-companion arXiv,
CMB-HD SciBook code release, CMB-S4/CMB-HD joint forecast literature) detects
publication of an explicit CMB-HD sigma(alpha_s) forecast. On detection,
the forecast PDF is SHA-pinned (per C32 protocol) and the S85 W1b-6
verdict is re-fired against the new sigma.

S86-Q2 finding: Three streams polled at 2026-04-26 via paper-search MCP
(arxiv + Google Scholar) and WebSearch. NO publication of an explicit
numeric sigma(alpha_s) for the CMB-HD detector specification was detected.

Stream 1 (arXiv astro-ph CMB-HD-tagged): closest hits are
  - 2203.05728 Snowmass2021 CMB-HD White Paper (Aiola+ 2022) -- alpha_s
    NOT in headline forecast list (S85 W1b-6 PRE-REG-INCOMPLETE was
    based on this).
  - 2309.03021 MacInnis, Sehgal, Rothermel 2023/2024 -- forecasts
    sigma(n_s)=0.0013, sigma(N_eff)=0.014 for LCDM+N_eff+sum(m_nu);
    alpha_s NOT a marginalized parameter.
  - 2405.12220 MacInnis, Sehgal 2024 -- DM/lensing focus, no alpha_s.

Stream 2 (CMB-HD code-release tracker https://cmb-hd.org/, hdPk + hdlike
GitHub repos): no explicit sigma(alpha_s) Fisher artifact at 2026-Q2.

Stream 3 (CMB-S4/CMB-HD joint forecast literature, Google Scholar +
arXiv 2025-2026): no joint forecast paper publishing an explicit
CMB-HD sigma(alpha_s) detected.

Verdict: INFO (poll completed, no publication available).

This is NOT a FAIL. Per plan section 9, INFO records correct
discipline-execution at the expected outcome at S86-Q2 (and likely
through several subsequent quarters until publication occurs). FAIL is
reserved for cadence violation (>3 months between polls).

Substrate-framing reminder (plan section 13): CMB-HD sigma(alpha_s) is
a Fisher-forecast observability bound -- detector specification, NOT
substrate physics. The framework's alpha_s prediction (S85 W1b-6 =
+0.0023, derived from the S50-51 identity alpha_s = n_s^2 - 1 with
planck_ns = 0.9649) is the substrate-side quantity being monitored.

Inputs (SHA-256 dual-pinned at runtime):
  - canonical_constants.py
  - sessions/framework/registry/cmb-hd-alpha-s-poll-log.md (poll-log file with
    2026-Q2 entry already appended manually before this script run;
    script reads it for SHA-pin)

Output 4-tuple:
  (value=NO-PUBLICATION-YET, scheme=quarterly-cmb-hd-alpha-s-poll,
   convention=3-stream-detection, L_max=NA)

Output file inventory:
  - computations/session-86/s86_w12_cmb_hd_alpha_s_poll.npz   (poll metadata)
  - computations/session-86/s86_w12_cmb_hd_alpha_s_poll.png   (status plot)
  - computations/session-86/s86_gate_verdicts.txt              (verdict line +
                                                          companion row)

No GPU; CPU-only; OMP capped at 4.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "4")

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import *  # noqa: E402, F401, F403
from canonical_constants import (
    planck_ns,
    planck_alpha_s,
    planck_alpha_s_err,
    alpha_s_inflation_framework,
    alpha_s_framework_central,
)

import hashlib  # noqa: E402
import json     # noqa: E402
import time    # noqa: E402

import numpy as np  # noqa: E402

PROJECT_ROOT = SCRIPT_DIR.parent
SCRIPT_DIR = SCRIPT_DIR
FRAMEWORK_DIR = PROJECT_ROOT / "sessions" / "framework"

GATE_ID = "S86-CMB-HD-ALPHA-S-FORECAST-PIN"                        # (local)
SCHEME = "quarterly-cmb-hd-alpha-s-poll"                           # (local)
CONVENTION = "3-stream-detection"                                   # (local)
L_MAX_LABEL = "NA"                                                  # (local)
SCHEMA_VERSION = "S86+"                                             # (local)
POLL_DATE = "2026-04-26"                                            # (local) S86-Q2 poll execution date
POLL_QUARTER = "2026-Q2"                                            # (local)

# ------------------------------------------------------------------ poll inputs

# Stream 1 hits: arXiv CMB-HD-tagged papers (paper-search MCP returns)
STREAM1_HITS = [                                                    # (local)
    {"id": "2203.05728", "title": "Snowmass2021 CMB-HD White Paper",
     "authors": "Aiola et al. (CMB-HD Collab) 2022",
     "publishes_sigma_alpha_s": False,
     "note": "alpha_s NOT in headline forecast list; S85 W1b-6 PRE-REG-INCOMPLETE source"},
    {"id": "2309.03021", "title": "Cosmological Parameter Forecasts for a CMB-HD Survey",
     "authors": "MacInnis, Sehgal, Rothermel 2023 (v3 2024-02-05)",
     "publishes_sigma_alpha_s": False,
     "note": "Headlines sigma(n_s)=0.0013 sigma(N_eff)=0.014; alpha_s NOT marginalized"},
    {"id": "2405.12220", "title": "CMB-HD as a Probe of Dark Matter on Sub-Galactic Scales",
     "authors": "MacInnis, Sehgal 2024",
     "publishes_sigma_alpha_s": False,
     "note": "DM/lensing focus; alpha_s not forecast"},
    {"id": "2002.12714", "title": "CMB-HD: Astro2020 RFI Response",
     "authors": "Sehgal et al. 2020",
     "publishes_sigma_alpha_s": False,
     "note": "Predates Snowmass2021 White Paper; no alpha_s"},
    {"id": "2112.02109", "title": "Mitigating Foreground Bias for a CMB-HD Survey",
     "authors": "Han, Sehgal 2021",
     "publishes_sigma_alpha_s": False,
     "note": "Foreground systematics paper, not parameter forecast"},
]

# Stream 2 hits: CMB-HD SciBook / code release tracker (WebSearch returns)
STREAM2_HITS = [                                                    # (local)
    {"id": "https://cmb-hd.org/", "title": "CMB-HD project landing page",
     "publishes_sigma_alpha_s": False,
     "note": "No SciBook PDF release with explicit alpha_s table at 2026-Q2"},
    {"id": "https://github.com/CMB-HD/hdPk", "title": "CMB-HD Matter Power Spectrum & Non-CDM Forecast Code",
     "publishes_sigma_alpha_s": False,
     "note": "Reproduces MacInnis & Sehgal (2024) DM forecasts; alpha_s NOT a tracked Fisher parameter"},
    {"id": "https://github.com/CMB-HD/hdlike", "title": "CMB-HD Likelihood (Cobaya-integrated)",
     "publishes_sigma_alpha_s": False,
     "note": "Likelihood module; no explicit sigma(alpha_s) Fisher number in repo docs"},
]

# Stream 3 hits: CMB-S4 / CMB-HD joint forecast literature
STREAM3_HITS = [                                                    # (local)
    {"id": "2511.01612", "title": "Is LCDM on the run? Reconciling CMB with Lyman-alpha Forest",
     "authors": "Fairbairn, Heurtier, Olea-Romacho 2025",
     "publishes_sigma_alpha_s": False,
     "note": "Planck+ACT DR6+SPT-3G+eBOSS Lyalpha alpha_s constraint; NOT a CMB-HD Fisher forecast"},
    {"id": "2507.09552", "title": "Probing scalar-induced GWs with FAST and SKA",
     "authors": "Li, Guo, Zu 2025",
     "publishes_sigma_alpha_s": False,
     "note": "SKA forecast, not CMB-HD; alpha_s sensitivity discussed for SKA only"},
]

ALL_STREAMS = {                                                     # (local)
    "stream_1_arxiv_companion": STREAM1_HITS,
    "stream_2_scibook_code_release": STREAM2_HITS,
    "stream_3_cmb_s4_cmb_hd_joint": STREAM3_HITS,
}

# ------------------------------------------------------------------ paths

OUT_NPZ = SCRIPT_DIR / "s86_w12_cmb_hd_alpha_s_poll.npz"
OUT_PNG = SCRIPT_DIR / "s86_w12_cmb_hd_alpha_s_poll.png"
VERDICT_TXT = SCRIPT_DIR / "s86_gate_verdicts.txt"
CANON_PY = SCRIPT_DIR / "canonical_constants.py"
POLL_LOG_MD = FRAMEWORK_DIR / "cmb-hd-alpha-s-poll-log.md"

INPUT_FILES = [CANON_PY]
if POLL_LOG_MD.exists():
    INPUT_FILES.append(POLL_LOG_MD)


# ------------------------------------------------------------------ helpers

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


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    """audit = SHA(script || canonical || pin-map JSON);
       content = SHA(script). Per W9a-99 dual-SHA split."""
    script_bytes = script_path.read_bytes() if script_path.exists() else b""
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()                                      # (local)
    h_audit.update(script_bytes); h_audit.update(canonical_bytes); h_audit.update(pinmap_json)
    h_content = hashlib.sha256()                                    # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def append_verdict(verdict: str, value: str, audit_sha: str,
                   content_sha: str, n_streams_polled: int, n_hits: int) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value} scheme={SCHEME} "
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
        f"n_hits_publishing_sigma_alpha_s=0; "
        f"action=NO-FISHER-PDF-REGISTRY-APPEND; NO-CANON-CONST-ADD; NO-W1b-6-RE-EMISSION; "
        f"next_poll_target=2026-07-26 (S87-Q3); upstream=S85-W1b-CMB-HD-ALPHA-S-MACINNIS-EXPLICIT\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ------------------------------------------------------------------ classification

def classify_streams() -> tuple[str, str, int, int]:
    """Returns (verdict, value, n_streams_polled, n_hits_total).

    PASS if any hit publishes_sigma_alpha_s == True.
    INFO if all hits publishes_sigma_alpha_s == False (poll completed,
    no publication available).
    FAIL if cadence missed (would be detected by absence of this script
    run in the prior quarter; here, S86 first poll runs as scheduled).
    """
    n_streams = len(ALL_STREAMS)                                    # (local)
    n_hits = sum(len(v) for v in ALL_STREAMS.values())              # (local)
    n_publishing = sum(                                             # (local)
        1 for v in ALL_STREAMS.values()
        for h in v if h.get("publishes_sigma_alpha_s")
    )
    if n_publishing > 0:
        return "PASS", "PUBLISHED-PINNED", n_streams, n_hits
    return "INFO", "NO-PUBLICATION-YET", n_streams, n_hits


# ------------------------------------------------------------------ main

def main() -> int:
    t0 = time.time()                                                # (local)

    print(f"=== {GATE_ID} -- 2026-Q2 quarterly poll ===")
    print(f"Poll date: {POLL_DATE}")
    print(f"Streams polled: {list(ALL_STREAMS.keys())}")
    print()

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                          # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANON_PY, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    # Classify each stream
    print("=== Per-stream classification ===")
    for stream_name, hits in ALL_STREAMS.items():
        n_pub = sum(1 for h in hits if h.get("publishes_sigma_alpha_s"))  # (local)
        print(f"  {stream_name}: {len(hits)} hits, {n_pub} publishing sigma(alpha_s)")
        for h in hits:
            flag = "YES" if h.get("publishes_sigma_alpha_s") else "NO "  # (local)
            print(f"    [{flag}] {h.get('id', '?')} -- {h.get('title', '?')}")
    print()

    verdict, value, n_streams, n_hits = classify_streams()
    print(f"=== Aggregate verdict: {verdict} (value={value}) ===")
    print(f"  n_streams_polled       = {n_streams}")
    print(f"  n_hits_total           = {n_hits}")
    print(f"  n_hits_publishing_sigma= 0")
    print()

    # Substrate-framing reminder
    print("=== Substrate-framing (plan section 13) ===")
    print(f"  Framework alpha_s prediction (substrate-side, S50-51 identity):")
    print(f"    alpha_s_framework_central = n_s_canon^2 - 1")
    print(f"                               = {planck_ns}^2 - 1")
    print(f"                               = {alpha_s_framework_central:.6e}")
    print(f"  Planck 2018 alpha_s observation (canonical, NOT-CMB-HD):")
    print(f"    planck_alpha_s     = {planck_alpha_s}")
    print(f"    planck_alpha_s_err = {planck_alpha_s_err}")
    print(f"  CMB-HD sigma(alpha_s) detector-spec forecast:")
    print(f"    NOT YET PUBLISHED (poll continues at S87-Q3)")
    print()

    # Save NPZ snapshot of poll metadata
    stream_keys = list(ALL_STREAMS.keys())
    n_per_stream = np.array([len(ALL_STREAMS[k]) for k in stream_keys], dtype=np.int32)
    n_pub_per_stream = np.array(
        [sum(1 for h in ALL_STREAMS[k] if h.get("publishes_sigma_alpha_s")) for k in stream_keys],
        dtype=np.int32,
    )
    flat_hits_json = json.dumps(ALL_STREAMS, sort_keys=True)        # (local)
    np.savez(
        OUT_NPZ,
        gate_id=np.array(GATE_ID),
        poll_date=np.array(POLL_DATE),
        poll_quarter=np.array(POLL_QUARTER),
        verdict=np.array(verdict),
        value=np.array(value),
        n_streams_polled=np.int32(n_streams),
        n_hits_total=np.int32(n_hits),
        stream_keys=np.array(stream_keys),
        n_per_stream=n_per_stream,
        n_publishing_per_stream=n_pub_per_stream,
        framework_alpha_s_central=np.float64(alpha_s_framework_central),
        planck_alpha_s=np.float64(planck_alpha_s),
        planck_alpha_s_err=np.float64(planck_alpha_s_err),
        flat_hits_json=np.array(flat_hits_json),
        audit_sha256=np.array(audit_sha),
        content_sha256=np.array(content_sha),
    )
    print(f"  NPZ written: {OUT_NPZ.name}")

    # Status PNG
    import matplotlib                                                # (local)
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt                                  # (local)
    fig, ax = plt.subplots(figsize=(9, 5))                           # (local)
    ax.axis("off")
    ax.text(0.5, 0.86, f"{verdict}", ha="center", fontsize=28,
            color="#2a6f97", weight="bold")
    ax.text(0.5, 0.74, f"value = {value}",
            ha="center", fontsize=13)
    ax.text(0.5, 0.62, f"Poll {POLL_QUARTER} ({POLL_DATE})",
            ha="center", fontsize=12, color="#444444")
    ax.text(0.5, 0.50,
            f"3 streams polled, {n_hits} total hits, 0 publish explicit sigma(alpha_s)",
            ha="center", fontsize=11)
    ax.text(0.5, 0.38,
            "Closest current sigma(alpha_s)_CMB-HD anchor: agent-projected 1.5e-3",
            ha="center", fontsize=10, color="#555555")
    ax.text(0.5, 0.30,
            "(W1a-9/W1b-2 sensitivity-scaling estimate, NOT a published CMB-HD forecast)",
            ha="center", fontsize=9, color="#666666")
    ax.text(0.5, 0.18,
            f"Framework substrate alpha_s = {alpha_s_framework_central:+.4e} (S50-51 identity)",
            ha="center", fontsize=10)
    ax.text(0.5, 0.08, f"Next poll target: 2026-07-26 (S87-Q3)",
            ha="center", fontsize=9, color="#888888")
    ax.set_title(f"{GATE_ID}")
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=150)
    plt.close(fig)
    print(f"  PNG written: {OUT_PNG.name}")

    tag = (f"(value={value}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX_LABEL})")
    print(tag)
    append_verdict(verdict, value, audit_sha, content_sha, n_streams, n_hits)
    print(f"  Verdict line + companion row appended to {VERDICT_TXT.name}")

    wall = time.time() - t0                                         # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
