# computations/

The active computation tree.

## Layout

- `_shared/` — shared computation infrastructure (canonical_constants.py, helper modules consumed by ~140 scripts: dirac_spectrum.py, spectral_action.py, r20a_riemann_tensor.py, l20_lichnerowicz.py, branching_computation.py, plus audit scripts and migration utilities).
- `session-N/` — per-session subfolders containing the gate-producing scripts, .npz/.png outputs, and `s{N}_gate_verdicts.txt` for each session.

## Path resolution

Scripts use `tools/computation_root.py` (`resolve_script`, `resolve_output`, `resolve_glob`) for portable path handling. The active root is pinned by `computations/_shared/computation_root.json` (relocated S96 W2 from `tools/`, which was hygiene-swept); if that config is absent the resolver defaults to the nested `computations` live tree.

## Audit

Every gate-producing script appends a verdict line to `computations/session-N/s{N}_gate_verdicts.txt` per `.claude/rules/gate-verdicts.md`. Validation runs via the `python-validate.{sh,py}` PostToolUse hook in `.claude/hooks/`.
