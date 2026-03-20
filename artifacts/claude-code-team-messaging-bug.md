# Bug Report: Team agents send messages to agentType instead of member name, creating orphan inboxes

## Summary

When agents are spawned as teammates via `Task` with `team_name` and `name` parameters, they use the **agent type** (e.g., `hawking-theorist`) instead of the **team member name** (e.g., `hawking`) as the `recipient` in `SendMessage`. The system silently creates new inbox files for any recipient string, so messages land in orphan inbox files that no agent reads.

## Environment

- Claude Code version: latest (Feb 2026)
- OS: Windows 11 (MINGW64/Git Bash)
- Model: claude-opus-4-6

## Steps to Reproduce

1. Create a team:
```json
TeamCreate({ "team_name": "my-team" })
```

2. Spawn two agents with explicit `name` parameters:
```json
Task({
  "name": "alice",
  "subagent_type": "hawking-theorist",
  "team_name": "my-team",
  "prompt": "Send a message to your teammate bob"
})

Task({
  "name": "bob",
  "subagent_type": "einstein-theorist",
  "team_name": "my-team",
  "prompt": "Send a message to your teammate alice"
})
```

3. Agent "alice" sends a message to `recipient: "einstein-theorist"` instead of `recipient: "bob"`.

4. The system creates `~/.claude/teams/my-team/inboxes/einstein-theorist.json` (orphan) alongside `~/.claude/teams/my-team/inboxes/bob.json` (where bob actually reads).

5. Bob never receives the message.

## Evidence

From a real team session with 3 agents (`schwarzschild-penrose`, `dirac-antimatter`, `hawking`):

### Inbox files created:
```
inboxes/
  schwarzschild-penrose.json    # Correct (team member name)
  dirac-antimatter.json         # Correct
  dirac-antimatter-theorist.json  # ORPHAN (agent type name)
  hawking.json                  # Correct
  hawking-theorist.json         # ORPHAN (agent type name)
  team-lead.json                # Correct
```

### hawking-theorist.json (orphan) contained 12 unread messages:
```json
{
  "from": "schwarzschild-penrose",
  "text": "[substantive 500-word message about curvature invariants]",
  "read": false
},
{
  "from": "dirac-antimatter",
  "text": "[substantive 400-word message with algebraic proofs]",
  "read": false
}
// ... 10 more unread messages
```

### hawking.json (actual inbox) contained only 2 messages:
Both from `team-lead` (the orchestrator), which used the correct name.

### Result:
- Hawking never received any messages from his teammates during the first ~10 minutes
- SP and Dirac never received Hawking's early messages
- Agents reported "checking inbox" but found nothing (because they checked the correct inbox, which was empty)
- Eventually the team lead manually told Hawking to resend, partially resolving the issue
- Even after that, SP continued sending to `dirac-antimatter-theorist` (wrong) instead of `dirac-antimatter` (correct)

## Root Cause Analysis

Agents construct the `recipient` field using information from their system prompt. The agent type names (e.g., `hawking-theorist`, `dirac-antimatter-theorist`) are more prominent in their context than the team member names from `config.json`. The `SendMessage` tool does not validate that the recipient matches a registered team member name — it silently creates a new inbox file for any string.

Two issues compound:

1. **Agents default to agentType over name**: Even when told to use team member names, agents gravitate toward the more descriptive type names.
2. **No validation on recipient**: `SendMessage` accepts any recipient string and creates an inbox file. There is no error, warning, or fallback when the recipient doesn't match a registered team member.

## Suggested Fix

### Option A: Validate recipient in SendMessage (recommended)
When `SendMessage` receives a `recipient` that doesn't match any `name` in the team's `config.json`, either:
- **Error**: Reject the message and return an error telling the agent to use the correct name
- **Fuzzy match**: If the recipient matches an `agentType` in config, auto-resolve to the corresponding `name` and deliver to the correct inbox

### Option B: Merge inbox files
Use a single inbox file per agent, keyed by `agentId` (which is `{name}@{team}`). Any message sent to either the `name` or `agentType` should route to the same inbox.

### Option C: Inject team roster into agent context
When spawning a teammate, include the full team roster with member names prominently in the system context, so agents know the correct names to use.

## Current Workaround

Add an explicit instruction to CLAUDE.md (project instructions inherited by all agents):

```markdown
### Message Discipline
- **CRITICAL: Use teammate NAMES, not agent types.** Read `~/.claude/teams/{team-name}/config.json`
  to find the `name` field for each member. Use THAT as the `recipient` in SendMessage.
  Example: if a teammate's name is `hawking`, send to `hawking` — NOT `hawking-theorist`.
  Messages sent to the wrong name create orphan inbox files and are never delivered.
```

This partially mitigates the issue but does not fully prevent it — agents still sometimes use the type name despite the instruction.

## Impact

- **Severity**: High — silent message loss in team collaboration
- **Frequency**: Consistent — observed in every multi-agent team session
- **User experience**: Agents appear to be ignoring each other; the user sees "checking inbox" behavior that produces no results; debugging requires reading raw inbox JSON files to discover the orphan inboxes
