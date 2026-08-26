# Instructor Auto-check Setup

This setup is completed once by the course owner. After that, the instructor runs the checker from the GitHub Actions interface without installing Python.

## 1. Prepare Google Cloud access

1. Create or select a Google Cloud project.
2. Enable the Google Sheets API and Google Drive API.
3. Create a service account and download its credential file.
4. Share the protected source spreadsheet with the service-account email as **Viewer**.
5. Create a Drive folder for generated results and share it with the same service account as **Editor**.

The credential file is used only as an encrypted GitHub secret. Students do not create or submit JSON files.

## 2. Prepare the protected spreadsheet

Create these worksheets:

- `COURSE_STUDENTS` with `Name`, `ID`, `Email`, `GitHub`, `Ethereum`, `Polkadot`, `TON`, `Group`, and `Active`;
- `ASSIGNMENT1_CONFIG` with `Professor NFT Contract`, `Professor Return Address`, `Special Contract`, `Start Block`, `End Block`, and `Require Approval`;
- `ETHERNAUT_LEVELS` with `Level`, `Address`, and `Complexity`.

For the first run, keep only one fresh test wallet in `COURSE_STUDENTS`. Do not copy the historical result rows into the new source registry until the staged preview test passes.

In Google Sheets, open **Data → Protect sheets and ranges** and restrict editing to instructors. The service account only needs viewer access to this source file. It needs editor access only to the separate results folder.

## 3. Configure the GitHub repository

Open **Settings → Secrets and variables → Actions** and add:

| Type | Name | Value |
|---|---|---|
| Secret | `GOOGLE_SERVICE_ACCOUNT_JSON` | Full contents of the downloaded service-account credential file |
| Secret | `COURSE_STUDENTS_SPREADSHEET_ID` | ID between `/d/` and `/edit` in the source spreadsheet URL |
| Secret | `GOOGLE_RESULTS_FOLDER_ID` | ID of the Drive results folder |
| Secret | `GOOGLE_RESULTS_SHARE_EMAIL` | Instructor email that should receive edit access to results |
| Secret | `SEPOLIA_RPC_URL` | Reliable Sepolia RPC endpoint |
| Secret | `ETHERSCAN_API_KEY` | Etherscan API key for indexed transaction checks |
| Variable | `ETHERNAUT_START_BLOCK` | Optional first Sepolia block to scan; omit to scan from block 0 |

Never commit these values to the repository.

## 4. Run the check

1. Open **Actions** in GitHub.
2. Select **Blockchain Autotest**.
3. Click **Run workflow**.
4. Select `preview` or `final`.
5. Select `all`, `assignment1`, or `ethernaut`.
6. Start the workflow and open its log when complete.
7. Follow the printed result URL or open the configured Drive folder.

The source spreadsheet is read-only from the script's point of view. Every run creates a new spreadsheet and never overwrites earlier results.

Before the first class-wide run, follow [Test Run for the New Assignments](test-run-new-assignments.md).
