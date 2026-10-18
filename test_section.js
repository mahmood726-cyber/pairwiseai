'use strict';

// The historical incomplete snippet is retained in docs/legacy/test_section.js.txt.
// Check the actual standalone runtimes without executing browser-only code.
const { spawnSync } = require('node:child_process');
const path = require('node:path');

for (const file of ['app.js', 'app.min.js']) {
  const result = spawnSync(process.execPath, ['--check', path.join(__dirname, file)], {
    encoding: 'utf8',
    timeout: 10000,
    windowsHide: true
  });
  if (result.error || result.status !== 0) {
    console.error(`Syntax check failed: ${file}`);
    console.error(result.error ? result.error.message : result.stderr);
    process.exitCode = 1;
  } else {
    console.log(`Syntax OK: ${file}`);
  }
}
