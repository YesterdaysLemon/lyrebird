# Lyrebird deployment

Public URL: https://lyrebird.alirezaafshan.com/

The existing Deploy Manager releases validated `main` commits to the personal
VPS. The repository workflow runs the site checks and a Docker build, signs the
request, verifies its accepted SHA, and waits for a successful terminal receipt.

- App ID and image: `lyrebird`; owner of checkout: `deploy-manager`.
- Checkout: `/opt/lyrebird/app`.
- Production/candidate loopback ports: `3240` / `3241`; container: `8080`.
- Readiness: `/healthz`; public build identity: `/version.json`.
- Application runtime secrets: none. The deployment control plane has its own
  per-app webhook secret, delivered through protected stdin and environment.
- Caddy owns the public route; Cloudflare owns its proxied A record.

## First verified release

September 22, 2026: commit `bb75e0cc2fd01d7559fcd954c44902b9d5cf88e1`,
[workflow 35707442922](https://github.com/YesterdaysLemon/lyrebird/actions/runs/35707442922),
Deploy Manager job `0f1b9123-9fef-4d63-adac-11f43b7e7f9c`, status `succeeded`.
The public version endpoint matched the commit. Real Edge checks passed for
all six papers at 1440px and 360px, including filters, citation clipboard,
PDF delivery, images, overflow, errors, and 404 behavior.

Registration was additive and reviewed at plan digest
`8a00e38eed2668ab67825da205c337765061e1d4225d63f701b41f0f383bae5f`.
It added the allowlist entry, one app env file, and one topology entry. Existing
routes/plots were preserved. Caddy was backed up and its complete proposed
configuration validated before reload. The manager was restarted only after
confirming an idle release lane. Rollback uses the prior known-good SHA-tagged
image through Deploy Manager's existing release mechanism.

This is a historical first-release receipt, not a promise that a later checkout
matches production. Always query the current version and terminal receipt.
