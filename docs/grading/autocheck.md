# Auto-check System

The instructor starts the checker from GitHub Actions. Students prepare the registry row and the report; they do not edit the grading workbook.

## Data flow

1. The protected `COURSE_STUDENTS` sheet supplies identity, exact repository, group, and registered public wallets.
2. The checker pins the latest commit in that repository and validates its root `submission.json`.
3. A `submitted` work section tells the checker which evidence and links belong to the work.
4. Implemented validators query GitHub, Sepolia, and explorer/RPC data against registered wallets.
5. The permanent instructor-owned workbook is updated; the source registry is never changed.
6. GitHub Actions stores `input_snapshot.json` and `results.json` as a 90-day audit artifact.

## Scopes

The workflow can run `all`, `labs`, `assignments`, one of `lab1`–`lab12`, or one of `assignment1`–`assignment4`. Running one scope preserves existing detail rows for the other works.

## Current deterministic checks

The current production validators verify:

- Assignment 1 professor NFT receive/return and personal NFT mint/approve/transfer flow;
- Assignment 2 Ethernaut registered-wallet completions and configured complexity;
- report schema, exact student ID, pinned GitHub commit, and evidence-link extraction for all 16 works.

The other labs and assignments are retained in the main course and report schema. Until a dedicated deterministic validator is added, a valid submitted report is sent to `Manual review`; it is never automatically marked `PASS` merely because JSON claims success.

## Result worksheets

| Worksheet | Contents |
|---|---|
| `Lab summary` | One row per active student with Lab 1–12 statuses and totals |
| `Assignment summary` | One row per active student with Assignment 1–4 statuses and totals |
| `Autotest details` | One row per student/work with report, evidence, pinned commit, and diagnostics |
| `Manual review` | Review queue with persistent instructor decision, score, and comment columns |
| `Errors` | Technical RPC, API, spreadsheet, and per-student failures |
| `Run history` | Append-only counts for preview and final runs |

`preview` and `final` execute the same checks. The mode labels the snapshot; the instructor controls when a result becomes the grading snapshot.
