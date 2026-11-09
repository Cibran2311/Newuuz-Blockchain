# Auto-check System

The instructor starts the checker with one button in GitHub Actions. Students do not run grading scripts and do not submit student JSON files.

## Canonical Data Flow

1. Google Classroom collects repository, notebook, report, and article links.
2. The protected COURSE_STUDENTS worksheet stores student identity and registered public addresses.
3. GitHub Actions runs scripts/course_autotest.py in preview or final mode.
4. The script reads the registry and queries GitHub, Sepolia RPC, and explorer APIs.
5. The script creates a new Google Spreadsheet; the source registry stays unchanged.
6. The instructor reviews Manual review and Errors before using a final result.

## Current Production Scope

The current workflow is intentionally limited to objective checks that are implemented and tested.

| Component | Current check | Automatic result |
|---|---|---|
| Assignment 1 | Token + Swap + NFT mint | PASS only when all three pass |
| Assignment 2 / Ethernaut | On-chain completion plus configured complexity | PASS when complexity is at least 10 |
| Labs 1–12 | Evidence contract exists in each lab page, but the production workflow does not run these lab checks yet | Manual review |
| Group work and articles | Links, reports, explanations, and contribution quality | Manual review |

The validation tables on lab pages describe the checks that should be reproducible. They do not mean that every check is already executed by the current workflow.

## Assignment 1 Rule

Assignment 1 is PASS only when all three objective checks pass:

- Token;
- Swap;
- NFT mint.

A repository link, screenshot, written explanation, or optional Professor NFT flow cannot replace a missing on-chain requirement. Qualitative evidence is sent to Manual review.

## Assignment 2 Rule

Assignment 2 uses the protected ETHERNAUT_LEVELS worksheet as the grading source of truth. Its configured complexity values are based on the official Ethernaut level data, but the checker does not depend on a student-maintained JSON file.

Ethernaut is an automatic PASS only when the verified unique completed levels have total configured complexity of at least 10. Lower or incomplete activity becomes TRIED or Manual review, not PASS.

## Result Worksheets

Every run creates PREVIEW_AUTOTEST_<timestamp> or FINAL_AUTOTEST_<timestamp> with:

| Worksheet | Contents |
|---|---|
| Closed list | One-row summary per active student |
| Autotest details | Transaction hashes, contracts, counts, and diagnostic notes |
| Manual review | Ambiguous, incomplete, or qualitative results requiring attention |
| Errors | RPC, API, spreadsheet, and per-student technical failures |

## Status Semantics

- PASS means all selected objective checks passed.
- REVIEW means evidence exists but an instructor must decide.
- ERROR means a technical problem prevented a reliable check.
- FAIL means the required objective evidence was not found.
- Manual review never silently becomes PASS.
- An API or RPC failure must be visible as ERROR, not treated as student failure.

## Preview and Final

- preview is for diagnostics and incomplete evidence;
- final creates the result spreadsheet used for grading review;
- the instructor starts final only after checking technical errors and manual-review rows;
- Google Classroom remains the source for due dates and Turn in status.

## Future Expansion

When additional labs are automated, add them to this table and to the workflow scope only after:

1. the evidence format is documented;
2. positive and negative tests exist;
3. network/API failures are separated from student failures;
4. a manual-review fallback is defined.
