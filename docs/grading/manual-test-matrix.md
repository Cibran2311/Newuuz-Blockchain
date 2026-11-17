# Manual Test Matrix

Run this matrix with controlled test wallets before using the checker on real student data. The goal is to catch false PASS results, hide no technical errors, and confirm that manual evidence stays separate from objective grading.

## Acceptance Criteria

- A missing objective requirement never becomes PASS because of a screenshot, repository, or written explanation.
- RPC, explorer, spreadsheet, or indexing failures become ERROR, not student FAIL.
- Duplicate blockchain events do not increase a student's score.
- The final result is reproducible from the registered wallet and the protected course configuration.
- The site route from course page to submission instructions works on desktop and mobile widths.

## Assignment 1 — Token, Swap and NFT

| ID | Scenario | Expected result |
|---|---|---|
| A1-01 | Registered wallet has the required token activity, approved swap activity, and NFT mint | Assignment 1 = PASS |
| A1-02 | Token activity exists, but swap activity is missing | Assignment 1 is not PASS |
| A1-03 | Token and swap activity exist, but NFT mint is missing | Assignment 1 is not PASS |
| A1-04 | NFT was minted to a different wallet | Assignment 1 is not PASS |
| A1-05 | A transaction is outside the configured scan range or on the wrong network | It is ignored; no false PASS |
| A1-06 | RPC or Etherscan is unavailable during the check | Student result = ERROR |
| A1-07 | Professor NFT flow is present without one required core check | It remains Manual review and cannot create PASS |

## Assignment 2 — Ethernaut

| ID | Scenario | Expected result |
|---|---|---|
| A2-01 | Unique completed levels total exactly 10 configured complexity points | Assignment 2 = PASS |
| A2-02 | Unique completed levels total 9 points | Assignment 2 is not PASS |
| A2-03 | The same level is completed or reported more than once | It counts once |
| A2-04 | Completion events belong to an unregistered wallet | They are not counted |
| A2-05 | On-chain completion exists but level mapping or the protected sheet is unavailable | REVIEW or ERROR; never an unjustified PASS |

## Site and submission smoke tests

| ID | Check | Expected result |
|---|---|---|
| SITE-01 | Open the course on a narrow viewport and expand the left navigation | Navigation remains usable; no right sidebar appears |
| SITE-02 | Open a lab, an assignment, and the grading instructions | Links and validation mode are clear |
| SITE-03 | Follow the submission instructions | The student is sent to Google Classroom and the assigned GitHub repository; no student JSON is requested |

## Record for each run

Record the date, checker mode, scope, test wallet aliases, expected result, actual result, and any transaction or run identifiers. Do not place private keys, seed phrases, API keys, or student JSON files in the evidence.
