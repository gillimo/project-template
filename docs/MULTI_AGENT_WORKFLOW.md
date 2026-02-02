# Multi-Agent Workflow

Purpose: define how multiple agents coordinate work, avoid conflicts, and keep logs/tickets in sync.

## Roles
- Hands/Eyes: perception + input execution wiring.
- Mimicry/Model: human-like behavior modeling + decision loop glue.
- Coordinator: keeps docs, tickets, and acceptance criteria aligned.

## Communication
- Primary coordination: `docs/HANDS_TALK.md` (create if missing).
- Log every material change in `docs/LOGBOOK.md`.
- Sync tickets in `docs/TICKETS.md` and module map (if present).

## Handoff Rules
- Each agent declares current focus and dependencies in the coordination log.
- When blocking on another agent, add a short request.
- When a dependency is completed, reply and mark dependent steps as unblocked.

## Conflict Avoidance
- Avoid editing the same file concurrently without coordination.
- If unexpected changes appear, stop and ask the user how to proceed.
- Prefer small, scoped commits per agent when allowed (local only).

## Documentation Sync
- Update `docs/DOCS_CHECKLIST.md` when docs change.
- Update `docs/BUG_LOG.md` when bugs are found or closed.
- Keep `docs/HOW_TO_OPERATE.md` aligned with new CLI or behavior changes.

## Daily Flow
1) Check the coordination log for new instructions.
2) Log in `docs/LOGBOOK.md`.
3) Implement small, scoped changes.
4) Update docs/tickets/bugs.
5) Post status update in the coordination log.

