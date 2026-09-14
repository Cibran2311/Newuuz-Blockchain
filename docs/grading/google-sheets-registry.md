# Protected Google Sheets Registry

The course uses one instructor-owned Google Spreadsheet as the source of truth. Students do not edit it.

## Student worksheet

The protected worksheet must be named `COURSE_STUDENTS` and use these columns:

| Column | Purpose |
|---|---|
| `Name` | Student name |
| `ID` | Stable student identifier |
| `Email` | Google Classroom email |
| `GitHub` | GitHub profile or repository URL |
| `Ethereum` | Registered Sepolia address or addresses |
| `Polkadot` | Registered testnet address |
| `TON` | Registered TON Testnet address |
| `Group` | Assignment group |
| `Active` | Whether the row should be checked |

Use one header row. The checker ignores empty rows and rows where `Active` is `false`, `no`, `inactive`, `нет`, `0`, or `-`.

## Ethernaut worksheet

The protected worksheet `ETHERNAUT_LEVELS` defines the grading rule without a repository configuration file:

| Column | Purpose |
|---|---|
| `Level` | Ethernaut level name |
| `Address` | Sepolia level contract address |
| `Complexity` | Instructor-defined score |

Ethernaut is an automatic `PASS` only when verified complexity is at least 10. A student with real activity below the threshold is marked `TRIED` and sent to manual review.

## Permissions

- Give edit access only to instructors.
- Give the GitHub Actions service account viewer access to the source spreadsheet.
- Protect both worksheets and all identity/address columns.
- Give students view access only if they need to confirm their registered data.
- Never store private keys, seed phrases, passwords, or API tokens in the spreadsheet.

The checker reads this spreadsheet and updates a separate instructor-owned result spreadsheet. It never writes into the source registry. The current result tabs are refreshed on every run, and `Run history` keeps a compact audit trail.

## Assignment 1 configuration worksheet

The protected worksheet `ASSIGNMENT1_CONFIG` contains exactly one data row. It makes the checker follow the current NFT Quest instead of historical ERC20/swap tasks.

| Column | Purpose |
|---|---|
| `Professor NFT Contract` | ERC721 contract used for the professor NFT flow |
| `Professor Return Address` | Wallet or contract that must receive the professor NFT back |
| `Special Contract` | Contract that must receive the student's personal NFT |
| `Start Block` | First Sepolia block included in this course run |
| `End Block` | Last block, or `99999999` while the assignment is open |
| `Require Approval` | `TRUE` when a matching `Approval` or `ApprovalForAll` event is mandatory |

All three addresses are required and must use the `0x...` format. Protect this worksheet and give the GitHub Actions service account viewer access.

Assignment 1 becomes `PASS` only when the registered wallet has on-chain evidence for the same ordered flow:

1. receive the professor NFT and return the same token to `Professor Return Address`;
2. mint a personal NFT;
3. approve `Special Contract` when approval is required;
4. transfer the same personal token to `Special Contract`.

## Safe first run

Do not run the new checker against the historical class list first. Create a temporary `COURSE_STUDENTS` worksheet with one test wallet, run the workflow in `preview` mode, complete each new task, and run `preview` again. Copy the real class roster into the protected registry only after the test wallet changes from `FAIL` or `PARTIAL` to `PASS`.
