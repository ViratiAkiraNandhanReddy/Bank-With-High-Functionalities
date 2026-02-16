#!/usr/bin/env node

/*
 * CONTRIBUTORS LINTER
 *
 * This script validates the CONTRIBUTORS.md file to ensure all contributor entries follow the standard:
 * - Each <a> tag points to a valid GitHub profile URL with correct tooltip
 * - Each <img> tag points to the correct GitHub avatar with width=96px and alt matching username
 * - No duplicate contributor entries exist
 *
 * Exit codes:
 * 0 - Lint passed
 * 1 - Lint failed
 */

const fs = require('fs');
const path = require('path');

const CONTRIBUTORS_FILE = path.resolve(process.cwd(), 'CONTRIBUTORS.md');

// ---
// READ CONTRIBUTORS
// ---

let content;
try {
  content = fs.readFileSync(CONTRIBUTORS_FILE, 'utf8');
} catch (err) {
  console.error(`[ERROR]: Unable to read CONTRIBUTORS.md at ${CONTRIBUTORS_FILE}`);
  console.error(err.message);
  process.exit(1);
}

// ---
// ARRAYS TO COLLECT ERRORS
// ---

const errors = [];
const seenUsers = new Set();

// ---
// REGEX PATTERNS
// ---

const aTagRegex = /<a\s+href="https:\/\/github\.com\/([^"]+)"\s+target="_blank"\s+title="(@[^"]+)">/g;
const imgTagRegex = /<img\s+src="https:\/\/github\.com\/([^"]+)\.png"\s+width="96px"\s+alt="(@[^"]+)"\/>/g;

// ---
// VALIDATE <a> TAGS
// ---

let match;
while ((match = aTagRegex.exec(content)) !== null) {
  const hrefUser = match[1].toLowerCase();
  const titleUser = match[2].replace('@', '').toLowerCase();

  // CHECK HREF/TITLE CONSISTENCY
  if (hrefUser !== titleUser) {
    errors.push(`[LINK ERROR]: Mismatch between href and title: href="${hrefUser}", title="${titleUser}"`);
  }

  // CHECK DUPLICATES
  if (seenUsers.has(hrefUser)) {
    errors.push(`[DUPLICATE ERROR]: Duplicate contributor detected: ${hrefUser}`);
  } else {
    seenUsers.add(hrefUser);
  }
}

// ---
// VALIDATE <img> TAGS
// ---

while ((match = imgTagRegex.exec(content)) !== null) {
  const srcUser = match[1].toLowerCase();
  const altUser = match[2].replace('@', '').toLowerCase();

  if (srcUser !== altUser) {
    errors.push(`[IMAGE ERROR]: Mismatch between img src and alt: src="${srcUser}", alt="${altUser}"`);
  }
}

// ---
// UNIFIED REPORTING
// ---

if (errors.length > 0) {
  console.error('\nContributors lint failed with the following issues:\n');
  errors.forEach(err => console.error(`- ${err}`));
  console.error('\nResolve the errors above.\n');
  process.exit(1);
} else {
  console.log('Contributors lint passed. No errors detected.');
  process.exit(0);
}
