---
name: sage-compute
description: Quick symbolic/exact computation via the Sage MCP — factor, simplify, symbolic eigenvalues, exact integrals. Use when float answers aren't good enough
argument-hint: <expression> | --code "<multiline sage>" | --eig "<matrix>" | --latex "<expr>" | --factor "<integer>"
---

# /sage-compute — Exact Symbolic Computation via Sage

Front-end to the `sage` MCP server. Routes common patterns to the right tool with the right pre-amble so you don't need to remember Sage syntax for one-off queries.

## When to use this skill vs. raw Python

Use `/sage-compute` when the answer **must be exact or symbolic**:

- Factor a large integer into primes
- Eigenvalues of a small rational/integer matrix, returned as algebraic roots (not floats)
- Closed-form integral or sum
- Simplify a trigonometric/algebraic expression
- Render a symbolic expression to LaTeX

Use plain Python (numpy/torch) when a numerical answer is fine. Sage is slower and the round-trip to SageCell adds latency.

## Usage

```
/sage-compute factor(2^64 - 1)
/sage-compute --factor 18446744073709551615
/sage-compute --eig "[[1,2,3],[4,5,6],[7,8,0]]"
/sage-compute --latex "integrate(sin(x)^2, x)"
/sage-compute --code "
    R.<x> = QQ[]
    p = x^4 - 10*x^2 + 1
    print(p.factor())
    print(p.roots(AA))
"
```

The first form (bare expression) is treated as a Sage expression and evaluated with `print(...)` wrapper.

## Execution steps

1. **Parse `$ARGUMENTS`**. Branch on flags:
   - `--factor N` → `sage_eval(code="print(factor({N}))")`
   - `--eig "<matrix>"` → `sage_symbolic_eig(matrix="<matrix>")`
   - `--latex "<expr>"` → `sage_latex(expr="<expr>")`
   - `--simplify "<expr>"` → `sage_simplify(expr="<expr>")`
   - `--code "<block>"` → `sage_eval(code="<block>", timeout=60)`
   - No flag (bare expression) → `sage_eval(code="print(<expression>)")`

2. **Call the right MCP tool**. All tools are on the `sage` server:
   | Skill route | MCP tool |
   |:------------|:---------|
   | `--factor`, bare expr | `mcp__sage__sage_eval` |
   | `--eig` | `mcp__sage__sage_symbolic_eig` |
   | `--latex` | `mcp__sage__sage_latex` |
   | `--simplify` | `mcp__sage__sage_simplify` |
   | `--code` | `mcp__sage__sage_eval` |

3. **Relay the result**. The MCP tool already formats `backend / success / stdout / stderr`. Pass through unchanged. If `success=false`, surface the stderr prominently; do not silently hide errors.

4. **Verify the result** if the caller will act on it. Substitution-chain discipline applies: a Sage output is **an oracle**, not a proof. Before citing a Sage answer in a working paper, you (the orchestrator) should run a cross-check in Python with `sympy` or `torch` on a small instance to confirm.

## Backend transparency

The Sage MCP auto-selects a backend:

- **Local Sage** — if `SAGE_BIN` env var is set AND points to a working `sage` executable; or if `sage` is on `PATH`. Fastest, no network, persistent across calls within the subprocess.
- **SageCell (remote)** — default fallback. Uses SageCell's Jupyter kernel over WebSocket. Session-isolated: no state between calls. ~2-5s round-trip per call.

Check which is live with:
```
mcp__sage__sage_backend_info
```

## Examples with expected shape

**Factor a 64-bit number**:
```
/sage-compute --factor 18446744073709551615
```
Expected stdout: `3 * 5 * 17 * 257 * 641 * 65537 * 6700417`

**Exact eigenvalues of 3×3 rational matrix**:
```
/sage-compute --eig "[[0,1,0],[0,0,1],[6,-11,6]]"
```
Expected: characteristic polynomial `(x-1)(x-2)(x-3)` with integer roots 1, 2, 3.

**Symbolic integral to LaTeX**:
```
/sage-compute --latex "integrate(sin(x)^2, x)"
```
Expected: `\frac{1}{2} \, x - \frac{1}{4} \, \sin\left(2 \, x\right)`

## Guard rails

- **Timeout cap**: Sage calls are capped at 60s default, 120s absolute. If you need longer, chunk the computation.
- **No persistent state in SageCell mode**: each call starts a fresh kernel. If you need state (e.g., define a ring, then manipulate polynomials in it), put everything in ONE `--code` block.
- **Don't use Sage for floating-point work**. `numpy.linalg` / `torch.linalg` are faster and more appropriate — Sage's value is symbolic correctness, not numerical throughput.
- **Bare expressions are wrapped in `print(...)`**. If your expression prints already, use `--code` instead to avoid double-printing.
