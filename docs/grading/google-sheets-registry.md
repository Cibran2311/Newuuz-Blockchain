# Protected Google Sheets Registry

The instructor creates one source spreadsheet. Students fill only their assigned registration row; the spreadsheet is not a laboratory report.

## `COURSE_STUDENTS`

| Column | Filled by | Purpose |
|---|---|---|
| `Name` | Student | Name used in the course list |
| `ID` | Instructor or student | Stable identifier; must match `submission.json` |
| `Email` | Student | Course contact email |
| `GitHub` | Student | Exact public repository URL containing `submission.json` |
| `Ethereum` | Student | Sepolia address or comma-separated addresses |
| `Polkadot` | Student | Registered Polkadot testnet address |
| `TON` | Student | Registered TON Testnet address |
| `Group` | Instructor | Assignment group |
| `Active` | Instructor | Whether the row is checked |

The checker ignores empty rows and rows where `Active` is `false`, `no`, `inactive`, `нет`, `0`, or `-`.

## Registration and protection

1. The instructor creates the table and assigns one row per student.
2. Students fill identity, repository, and public wallet fields during the registration window.
3. The instructor checks duplicates and then protects the sheet or individual rows.
4. Later changes are requested from the instructor, so an address cannot be silently replaced after completing a task.

Share the source spreadsheet with the GitHub Actions service account as **Viewer**. Share the separate result spreadsheet with it as **Editor**. Never give the service account ownership of either file.

## Instructor configuration sheets

`ASSIGNMENT1_CONFIG` contains one row:

| Column | Purpose |
|---|---|
| `Professor NFT Contract` | ERC721 contract used for the professor NFT flow |
| `Professor Return Address` | Address that must receive that NFT back |
| `Special Contract` | Contract that receives the student's NFT |
| `Start Block` | First Sepolia block included in the check |
| `End Block` | Last included block |
| `Require Approval` | Whether matching approval evidence is mandatory |

`ETHERNAUT_LEVELS` contains `Level`, `Address`, and `Complexity`. Assignment 2 automatically passes only when registered-wallet evidence reaches the configured complexity threshold.

The checker never edits the source registry. It updates only the permanent instructor-owned result workbook.
