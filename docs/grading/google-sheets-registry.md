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

The checker reads this spreadsheet and creates a separate result spreadsheet. It never writes into the source registry.
