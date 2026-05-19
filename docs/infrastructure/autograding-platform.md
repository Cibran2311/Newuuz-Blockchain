# Auto-Grading and Portfolio Platform

## Overview

The course can be extended with a verifiable grading platform. The platform uses the same technologies students learn in the course: wallet authentication, RPC queries, smart contract events, and append-only evidence logs.

## Core idea

Instead of relying only on a public editable spreadsheet, students authenticate with their wallet and see a private dashboard with their own assignments, submissions, and grading history.

## Proposed components

| Component | Purpose |
|---|---|
| SIWE login | Authenticate students with Ethereum wallets |
| Submission API | Store submitted JSON payloads |
| Deterministic graders | Check on-chain evidence |
| Append-only grader runs | Preserve audit history |
| Portfolio page | Show verified public achievements |
| Optional SBT/attestation | Anchor completed work on-chain |

## Database model

Recommended tables:

- `students`
- `assignments`
- `submissions`
- `grader_runs`
- `auth_nonces`
- `sessions`

The most important design rule is that `grader_runs` should be append-only. Regrading should create a new row instead of overwriting the old result.

## Assignment grader mapping

| Item | Grading approach |
|---|---|
| Testnet transaction | query transaction from student wallet |
| Hash/collision lab | verify submitted inputs server-side |
| Block mining | verify nonce satisfies difficulty |
| ERC20/NFT assignment | verify contract addresses and events |
| Ethernaut | query completed level events |
| Polkadot lab | verify extrinsic signed by student address |
| XCM lab | verify XCM-related extrinsic or event |
| TON lab | query TON transaction evidence |
| Technical article | verify URL, length, references, and topic |

## GitHub Classroom mode

A simpler version can work directly through GitHub Classroom:

1. Each student repository contains `submission.json`.
2. GitHub Actions validates JSON format.
3. A Python checker reads public blockchain evidence.
4. Students receive feedback in the Actions log.
5. Final grading can run manually or after the deadline.

## Recommended GitHub Actions triggers

```yaml
on:
  push:
  workflow_dispatch:
  schedule:
    - cron: "0 19 25 3 *"
```

Recommended logic:

- run basic validation on every push;
- run final grading manually or after deadline;
- show students what is missing before the deadline;
- preserve final results after deadline.
