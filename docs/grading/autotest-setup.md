# Instructor Auto-check Setup

This GitHub, MkDocs, and Google Sheets setup is completed once by the course owner.

## 1. Prepare Google Cloud access

1. Create or select a Google Cloud project.
2. Enable the Google Sheets API.
3. Create a service account and download its JSON credential file.
4. Share the protected source spreadsheet with the service account as **Viewer**.
5. Create an empty spreadsheet named `NewUUZ Autotest Results` and share it with the service account as **Editor**.

Keep the downloaded credential private. The service account updates an instructor-owned file because consumer service accounts cannot own new Drive files.

## 2. Prepare the source spreadsheet

Create:

- `COURSE_STUDENTS`: `Name`, `ID`, `Email`, `GitHub`, `Ethereum`, `Polkadot`, `TON`, `Group`, `Active`;
- `ASSIGNMENT1_CONFIG`: `Professor NFT Contract`, `Professor Return Address`, `Special Contract`, `Start Block`, `End Block`, `Require Approval`;
- `ETHERNAUT_LEVELS`: `Level`, `Address`, `Complexity`.

Give students a controlled registration period to fill only their own identity, repository, and public wallet fields. Then protect the source sheet. The service account needs viewer access only.

## 3. Configure GitHub Actions

Under **Settings → Secrets and variables → Actions**, add:

| Type | Name | Value |
|---|---|---|
| Secret | `GOOGLE_SERVICE_ACCOUNT_JSON` | Entire service-account credential JSON |
| Secret | `COURSE_STUDENTS_SPREADSHEET_ID` | Source spreadsheet ID from its URL |
| Secret | `GOOGLE_RESULTS_SPREADSHEET_ID` | Result spreadsheet ID from its URL |
| Secret | `SEPOLIA_RPC_URL` | Reliable Sepolia RPC endpoint |
| Secret | `ETHERSCAN_API_KEY` | Etherscan API key for indexed fallback checks |
| Variable | `ETHERNAUT_START_BLOCK` | Optional first Sepolia block to scan |

Student repositories must be public in this version. The course workflow token can read public repositories but does not grant access to arbitrary private student repositories.

## 4. Prepare student repositories

Each registered repository must contain `submission.json` at its root. Students start from `submission.example.json`, use the exact Sheet `ID`, retain all 16 work sections, and change a work to `submitted` only when its report is ready.

## 5. Run the check

1. Open **Actions → Blockchain Autotest → Run workflow**.
2. Choose `preview` or `final`.
3. Choose the whole course, labs, assignments, or one work.
4. Open the result workbook from the workflow summary.
5. Download the audit artifact when a machine-readable snapshot must be archived separately.

Every run refreshes the current summaries and details, preserves instructor review columns, and appends one row to `Run history`.
