# Lyrebird

Alireza Afshan's independent research library. Static, accessible paper pages,
PDFs, evidence links, citation downloads, local search, RSS and publication standards.

## Work locally

Requires Node 22 or newer. `npm ci`, `npm run check`, then `npm start`.
Open http://localhost:8080. `PORT` changes the local port.

Content lives in `content/papers.json` and one Markdown file per paper.
PDFs and figures live under `public/papers/<slug>/`. Preserve source provenance
and state evidence boundaries. Update versions when findings change.

Deployment uses the existing personal VPS and Deploy Manager, triggered by
the validated main-branch GitHub workflow. `/healthz` checks readiness and
`/version.json` identifies the deployed commit. No analytics or client secrets.

Run `npm run check` before release and verify desktop/mobile layouts, filtering,
citations, paper/PDF links, the terminal deployment receipt, and public SHA.
