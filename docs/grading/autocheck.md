# Auto-check System

The instructor starts the checker from GitHub Actions. Students prepare the registry row and the report; they do not edit the grading workbook.

## Data flow

1. The protected Google workbook supplies identity, exact repository, registered public wallets, and instructor-controlled lab requirements.
2. The checker pins the latest commit in that repository and validates its root `submission.json`.
3. A `submitted` work section tells the checker which evidence and links belong to the work.
4. Implemented validators query GitHub, Sepolia, Subscan, and TON Center against registered wallets.
5. The permanent instructor-owned workbook is updated; the source registry is never changed.
6. GitHub Actions stores `input_snapshot.json` and `results.json` as a 90-day audit artifact.

## Scopes

The workflow can run `all`, `labs`, `assignments`, one of `lab1`–`lab12`, or one of `assignment1`–`assignment4`. Running one scope preserves existing detail rows for the other works.

## Current deterministic checks

The current production validators verify:

- Lab 1 exact `0.0001 ETH` Sepolia transfer from a registered wallet to the configured recipient;
- Lab 4 transaction status, sender, gas limit, gas used, fee, and explanation;
- Lab 5 deployed ERC20 metadata methods, three student transfers, `Transfer` events, and a batch Disperse transaction;
- Lab 6 professor NFT receive/return and personal NFT mint/approve/transfer flow;
- Lab 7 successful swaps through the instructor-configured pair of class DEX contracts; the declared final portfolio calculation remains instructor-reviewed;
- Lab 8 successful Westend transfer, signer, recipient, and amount through Subscan;
- Lab 9 successful registered-wallet XCM extrinsic on the configured Westend/Asset Hub route;
- Lab 10 submitted `0.01 TON` testnet transfer from the registered wallet, accepting `0.0099`–`0.01 TON` at the recipient after forwarding fees;
- Lab 11 outgoing class-Jetton transfer, configured master contract, owner wallet, sender Jetton Wallet, and recipient-wallet trace;
- Lab 12 instructor-assigned mode: successful approved-router STON.fi swap plus a JavaScript/TypeScript script at the pinned commit, or a safe HackTON precheck;
- Assignment 1 professor NFT receive/return and personal NFT mint/approve/transfer flow;
- Assignment 2 Ethernaut registered-wallet completions and configured complexity;
- report schema, exact student ID, pinned GitHub commit, and evidence-link extraction for all 16 works.

Lab 2 and Lab 3 have safe prechecks for required values, code artifacts, collision/difficulty conditions, and explanations. They remain `REVIEW` because the course currently permits different implementation algorithms and the checker never executes untrusted student code. Lab 7 also remains `REVIEW` after its on-chain checks because the course has not fixed one deterministic portfolio-valuation formula. The HackTON path in Lab 12 remains `REVIEW`; its challenge proof requires instructor confirmation. The STON.fi path can receive an automatic `PASS`.

Assignment 3–4 are retained in the main course and report schema. Until their dedicated deterministic validators are added, a valid submitted report is sent to `Manual review`; it is never automatically marked `PASS` merely because JSON claims success.

Subscan checks use the network-specific Westend and Asset Hub endpoints and require `SUBSCAN_API_KEY`. TON checks use TON Center testnet indexing and normalize equivalent hex/Base64 transaction hashes. A provider outage, rate limit, missing receipt for a known transaction, or malformed API response produces `ERROR`, not a student `FAIL`.

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
