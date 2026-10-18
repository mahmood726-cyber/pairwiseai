
## Installation
Run `node test_section.js` for syntax checks of app.js and app.min.js. The check
works from any working directory and fails for missing or invalid runtime files.
The old incomplete JavaScript snippet is preserved as non-executable reference
text in docs/legacy/test_section.js.txt. Neither the old snippet nor the Node
checker is loaded by the application. Browser behavior and statistical accuracy
require their own validation; this command checks syntax only.

Use the dependency files in this directory (for example `requirements.txt`, `environment.yml`, `DESCRIPTION`, or equivalent project-specific files) to create a clean local environment before running analyses.
Document any package-version mismatch encountered during first run.

TruthCert Africa Packs v1 (schema-first)

- 13 countries x 7 disease groups.
- Pairwise-only.
- Local currency (LCU) output always.

Start here:
- index.yaml
- countries/<ISO3>.yaml
- diseases/<GROUP>.yaml
- country_disease/<ISO3>__<GROUP>.yaml
