# Framework Evidence & Probability Methodology

How to assess the phonon-exflation framework's status, prioritize computations, and weight evidence. The living EVOI priority table is at `sessions/evoi-framework.md` — check it before proposing new computations.

## Computation Priority (EVOI)

EVOI (Expected Value of Information) determines what to compute next:

EVOI = P(pass) × |delta_P(pass)| + P(fail) × |delta_P(fail)|

The computation with the highest EVOI gets priority. This tells you where to SPEND WORK.

## Evidence Weighting

- **Observational passes** are weighted by prior predictive range / posterior width. A Higgs mass within 7% from zero geometric free parameters across a 5-OOM prediction space has BF ~ 1000, not 2.
- **Failures cluster by TOPIC**. Four agents hitting the same truncation wall = ONE methodological finding. Three CC mechanisms failing = ONE open problem with three eliminated approaches.
- **Eliminating wrong mechanisms STRENGTHENS surviving paths.** A framework that has tested and closed 25 wrong mechanisms is stronger than one that has tested none.
- **Joint probability matters.** The chance of one random geometry producing multiple independent observational matches is the PRODUCT of individual probabilities, not the arithmetic mean.

## Effort-Based Probability

The framework probability is tracked as: (mechanism links complete / total) × (fraction approaching observation). This goes UP when work is done, not only when favorable results return.

## Maintenance & Enforcement (anti-rot)

The EVOI table (`sessions/evoi-framework.md`) is a LIVING document; its content currency MUST NOT lag the current session. Enforcement is structural, not aspirational:

- **Staleness audit**: `computations/_shared/_evoi_staleness_audit.py` compares the table's machine-readable `<!-- evoi-content-currency: S{N} -->` marker against the current session — PASS (lag 0) / S2 advisory (lag 1–2) / S1 MANDATORY (lag ≥ 3). It keys on the CONTENT marker, never git mtime: a file whose bytes are swept by a broad commit is NOT thereby refreshed.
- **`/rclab-plan` consumes AND maintains it** (Step 1c-REGISTERS, where EVOI is one member of the forward-register set it maintains + consumes): orders waves by EVOI tier, and rebuilds + re-stamps the table when the audit returns S1/S2. A stale guiding star is rebuilt before it is consumed — never re-noted-and-deferred.
- **`/rclab-investigate` feeds it**: investigators route new high-leverage open items into the table, not only into scattered working papers.
- EVOI values are ordinal leverage proxies, not calibrated probabilities; a full re-rank with elicited P(pass) is a separate maintenance pass.

A lapse, if ever found, is REBUILT in-session (per `feedback_fix-in-session-never-defer.md`), never logged as a carry-forward.
