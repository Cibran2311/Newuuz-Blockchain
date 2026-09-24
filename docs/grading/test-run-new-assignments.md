# Test Run for the New Workflow

Use one fresh test student before enabling the real roster.

## Prepare the test record

1. Put one active `TEST-001` row in `COURSE_STUDENTS`.
2. Register its exact public GitHub repository and fresh testnet wallets.
3. Copy `submission.example.json` to that repository as `submission.json`.
4. Keep every work as `draft` and run `preview` with a small scope.

The first run should show the selected work as `DRAFT`, store the pinned commit, and create `Lab summary`, `Assignment summary`, `Autotest details`, `Manual review`, `Errors`, and `Run history`.

## Assignment 1 — NFT Quest

Configure `ASSIGNMENT1_CONFIG`, change only `assignment1.status` to `submitted`, and record the contract, token, and transaction evidence in its JSON section. Compile `contracts/NewuuzAssignment1Test.sol` with Solidity 0.8.24 or newer and perform:

1. professor NFT mint to the registered student wallet;
2. return of the same professor NFT;
3. personal NFT mint from the registered wallet;
4. approval for the configured special contract;
5. transfer of the same personal NFT to that contract.

Run `preview` with `scope = assignment1` after each checkpoint. Incomplete real activity should be `PARTIAL`/`REVIEW`; the complete ordered flow should be `PASS`.

## Assignment 2 — Ethernaut

Set `assignment2.status` to `submitted` and list completed level names in `evidence.completed_levels`. Run `preview` with `scope = assignment2`.

| Evidence | Expected result |
|---|---|
| No registered-wallet completion | `FAIL` |
| Real activity below configured complexity 10 | `REVIEW` |
| Verified complexity 10 or higher | `PASS` |

The level names in JSON guide reporting; on-chain events from the registered wallet determine the automatic result.

## Enable the roster

After both targeted checks work:

1. add the current class rows and protect the registry;
2. confirm that every row points to an exact public repository;
3. run `preview` with `scope = all`;
4. review invalid/missing reports, technical errors, and the manual queue;
5. use `final` only after accepting the preview.
