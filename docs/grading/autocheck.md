# Auto-check System

The instructor starts the checker with one button in GitHub Actions. Students do not run grading scripts.

## Data flow

1. Google Classroom collects repository, notebook, report, and article links.
2. The protected `COURSE_STUDENTS` worksheet stores student identity and registered public addresses.
3. GitHub Actions runs `scripts/course_autotest.py` in `preview` or `final` mode.
4. The script reads the registry and queries GitHub, Sepolia RPC, and explorer APIs.
5. The script creates a new Google Spreadsheet; the source registry stays unchanged.

## Current deterministic checks

The first production version verifies:

- Assignment 1 professor NFT receive and return flow;
- Assignment 1 personal NFT mint;
- Assignment 1 approval and transfer to the configured special contract;
- GitHub repository availability as supporting metadata;
- Ethernaut on-chain completions and instructor-defined complexity.

Assignment 1 is `PASS` only when the complete current NFT Quest flow is present. Course addresses and the block range are read from the protected `ASSIGNMENT1_CONFIG` worksheet. Ethernaut is `PASS` at verified complexity 10 or higher.

## Result worksheets

Every run creates `PREVIEW_AUTOTEST_<timestamp>` or `FINAL_AUTOTEST_<timestamp>` with:

| Worksheet | Contents |
|---|---|
| `Closed list` | One-row summary per active student |
| `Autotest details` | Transaction hashes, contracts, counts, and diagnostic notes |
| `Manual review` | Ambiguous, incomplete, or failed results requiring attention |
| `Errors` | RPC, API, spreadsheet, and per-student technical failures |

## Manual checks

Written explanations, article quality, diagrams, team contribution, and tasks not yet implemented in the checker remain instructor-reviewed. Google Classroom grades are not changed automatically in this version.
