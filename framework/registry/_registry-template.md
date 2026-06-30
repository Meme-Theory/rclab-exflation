---
type: registry-template
ingested-by: /weave --update
---

# &lt;Registry Name&gt;

> **This is a template.** Copy to `sessions/framework/<slug>.md`, replace every `<...>` placeholder, delete this blockquote. `/weave --update` will ingest the resulting file into `tools/knowledge.db`.

**Registry ID**: `<slug>`
**Owner agent(s)**: `<agent-or-list>`
**Last updated**: `<YYYY-MM-DD, S<NN>-W<N>-<ITEM>>`
**Ingestion**: `/weave --update` picks up this file; `knowledge.db` stores one row per entry in the appropriate entity table (`closed | open | gates | theorems | researchers`).

---

## Scope

One paragraph describing:
- What this registry contains (the authoritative data)
- Which gates / waves / sessions cite it
- Why it is project-level rather than agent-private (cite the AMRI test it would fail if misfiled in agent memory)

---

## Summary table

| ID | Entry | Pin / Value | Source (session / paper) | SHA | Status |
|:---|:------|:------------|:-------------------------|:----|:-------|
| `<slug-1>` | <short name> | <value ± sigma or tag> | <S<NN>-W<N> or researchers/...> | `<16-hex>` | PINNED / WARRANT-DEFERRED / DEPRECATED |

---

## Entry detail

Repeat one block per entry:

### `<slug-1>` — <short name>

- **Description**: one-line purpose
- **Pinned value**: <exact value or tag>
- **Uncertainty**: <σ, band, or NA>
- **Source**: <session or paper citation>
- **SHA**: `<64-hex>` (full) or `<16-hex>` (head)
- **Consumer gates**: `<gate-ID-1, gate-ID-2, ...>` — gates elsewhere in the project that pin this entry as an Input-SHA
- **Falsifier / wall statement**: one sentence on what null result would falsify this entry, or what wall this entry establishes

---

## Consumer gates

Forward-reference for future auditors: gates (past and upcoming) that read this registry as Input-SHA. Update when a new consumer gate lands.

| Gate ID | Session | Role | Notes |
|:--------|:--------|:-----|:------|
| `<GATE-ID>` | S<NN> | INPUT-PIN \| OUTPUT-WRITER | <one-line> |

---

## Change log

| Date | Session | Change | Author |
|:-----|:--------|:-------|:-------|
| <YYYY-MM-DD> | S<NN>-W<N> | <create / add-entry / update / deprecate-entry> | <agent> |

---

## Migration notes

If this registry was promoted from an agent's memory via AMRI migration (see `.claude/rules/agent-standards.md` § AMRI), record here:
- Pre-migration memory file path(s): `<.claude/agent-memory/<agent>/<file>.md>`
- Migration session / gate: `S<NN>-W<N>-<ITEM>`
- Pointer installed in memory: `<line of text now residing where the content used to be>`
