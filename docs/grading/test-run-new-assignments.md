# Test Run for the New Assignments

Use this sequence before adding the real class roster. The goal is to prove that the checker detects the new tasks, not historical student activity.

## Prepare one test wallet

1. Create a temporary `COURSE_STUDENTS` worksheet with one active row.
2. Register one fresh Sepolia wallet in the `Ethereum` column.
3. Fill and protect `ASSIGNMENT1_CONFIG`.
4. Keep the old student workbook as an archive. Do not copy its result columns into the source registry.

## Assignment 1 — NFT Quest

Run **Blockchain Autotest** with `mode = preview` and `scope = assignment1` after each checkpoint.

For the first live test, compile `contracts/NewuuzAssignment1Test.sol` in Remix with Solidity `0.8.24` or newer. Deploy:

1. `NewuuzProfessorNFT` from the instructor wallet;
2. `NewuuzSpecialNFTReceiver` from the instructor wallet;
3. `NewuuzStudentNFT` from the registered test-student wallet.

Put the first contract address, the instructor wallet, and the second contract address into `ASSIGNMENT1_CONFIG`. A fresh test wallet can use `Start Block = 0`.

Then perform this exact flow:

1. from the instructor wallet, call `NewuuzProfessorNFT.mintTo(testStudent)`;
2. from the student wallet, call `NewuuzProfessorNFT.safeTransferFrom(testStudent, instructor, 1)`;
3. from the student wallet, call `NewuuzStudentNFT.mint()`;
4. from the student wallet, call `NewuuzStudentNFT.approve(specialReceiver, 1)`;
5. from the student wallet, call `NewuuzStudentNFT.safeTransferFrom(testStudent, specialReceiver, 1)`.

Do not use `NewuuzSpecialNFTReceiver.returnNFT` during the test. It is an instructor-only recovery helper for returning an NFT after validation.

| Checkpoint | Expected result |
|---|---|
| No new transactions | `FAIL` |
| Professor NFT received | `PARTIAL` |
| Same professor NFT returned | `PARTIAL` |
| Personal NFT minted | `PARTIAL` |
| Special contract approved, when required | `PARTIAL` |
| Same personal NFT transferred to the special contract | `PASS` |

Verify that the generated `Autotest details` worksheet contains the correct contract addresses, token IDs, and transaction hashes. A result based on an older token/swap transaction is a test failure.

## Assignment 2 — Ethernaut

Run `preview` with `scope = ethernaut` on the same registered wallet.

| Checkpoint | Expected result |
|---|---|
| No completed configured levels | `FAIL` |
| Real activity below complexity 10 | `TRIED` and manual review |
| Verified complexity 10 or higher | `PASS` |

Check that every counted level address exists in `ETHERNAUT_LEVELS`. If an official Sepolia level address changes, update the protected worksheet and repeat the preview.

## Enable the class roster

Only after both preview scenarios behave as expected:

1. replace the temporary test row with the current class roster;
2. protect all three source worksheets;
3. run `preview` for the whole class;
4. review `Errors` and `Manual review`;
5. run `final` only after the preview is accepted.
