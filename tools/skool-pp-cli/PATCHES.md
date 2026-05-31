# skool-pp-cli Local Patch Notes

Installed binary source:

- Repository: `https://github.com/twflipper/skool-pp-cli.git`
- Base commit: `54803f0a012a743ef072c14140e1bad4845608f1`

## full-cookie-web-session

The AI-OS binary was rebuilt with a local patch that lets Skool web-route
scraping use a full browser Cookie header from `SKOOL_COOKIE`,
`SKOOL_CURL_FILE`, or config headers.

Why: Skool accepted `auth_token` alone on `api2.skool.com/health`, but
token-only requests to `www.skool.com` redirected to `/login`. The copied
browser cURL includes additional WAF/session cookies that are required for
Next.js page and data routes.

Touched upstream files in the build clone:

- `internal/cli/skoolweb_helpers.go`
- `internal/cli/kb.go`
- `internal/skoolweb/client.go`
- `.printing-press-patches.json`

Validation:

- `go test ./...` passed.
- `SKOOL_CURL_FILE=/Users/annabelfilippini/Documents/skool/skool-curl.txt tools/skool-pp-cli/bin/skool-pp-cli communities list --agent` returned 21 communities.
- Bounded first sync completed with 21 communities synced and 0 failed.
