<!-- al-stack:project:start -->
## Al-stack project

Project: lyrebird. Profile: web. Status: active.

An independent research library for Alireza Afshan, with readable papers, reproducible evidence, and explicit publication status.

`al-stack.toml` records this project's setup and dependencies. Work from the checkout selected for the task; other branches/worktrees are optional history. Use `al-stack register .` once when starting work here. Local registration does not change the project's lifecycle.

Project commands:
- build: `npm run build`
- check: `npm run check`
- start: `npm start`

Project skills (load when relevant):
- `frontend-quality`: `.agents/skills/frontend-quality/SKILL.md`. Claude's copy is mirrored in `.claude/skills`.
- `vps-operations`: `.agents/skills/vps-operations/SKILL.md`. Claude's copy is mirrored in `.claude/skills`.

Edit project guidance outside this managed section. Use `al-stack configure` for its fields and `al-stack check .` for setup checks. Run the actual project checks for behavioral validation.
<!-- al-stack:project:end -->

## Working agreement

- Use `frontend-quality` for UI and `vps-operations` for deployment. The existing VPS and Deploy Manager own production.
- Build: `npm ci` then `npm run build`. Required checks: `npm run check`; browser verification at desktop and 360px for changed flows. Start: `npm start` (port 8080).
- Content is scholarly work, not marketing. Preserve manuscript scope, dates, provenance, null outcomes, and explicit review status. Never invent acceptance, independent review, citations, or a DOI.
- Acceptance: all paper/figure/PDF/citation links resolve; search and filtering are keyboard usable; no overflow at mobile width; deployed SHA matches the terminal release receipt.
- New content belongs in `content/papers.json` and `content/<slug>.md`, with PDFs in `public/papers/<slug>/`. Relative evidence links resolve to pinned source commits.
- No analytics, accounts, live model APIs, or runtime secrets in the application. Public metadata and library search work without a backend database.
