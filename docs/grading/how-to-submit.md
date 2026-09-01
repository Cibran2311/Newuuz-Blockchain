# How to Submit

The course uses two records with different purposes:

- Google Sheets stores your identity, repository, and public testnet wallets;
- `submission.json` in your GitHub repository stores reports for all 12 labs and all 4 assignments.

Do not copy wallet addresses or personal data into every report. The checker joins the two records by `student_id`.

## Before the first submission

Fill your assigned row in `COURSE_STUDENTS` during the registration window:

- name and stable student ID;
- GitHub **repository** URL, not only a profile URL;
- Sepolia, Polkadot, and TON Testnet public addresses used in the course;
- group, when the instructor has assigned one.

The instructor protects the registry after registration. Ask the instructor to change a wallet or repository; do not add an unregistered address only to the JSON report.

## Prepare the repository once

1. Copy `submission.example.json` from the course repository to the root of your repository.
2. Rename the copy to `submission.json`.
3. Replace `TEST-001` with the exact `ID` from your Sheet row.
4. Keep all sections from `lab1` through `lab12` and `assignment1` through `assignment4`.
5. Commit and push the file.

From a local clone of the course repository, you can validate the file before pushing:

```bash
python scripts/check_submission_json.py /path/to/student-repo/submission.json
```

## Submit one work

1. Complete the work on the required testnet.
2. Push code, notebooks, screenshots, and longer reports to the registered repository.
3. Fill only that work's `evidence`, `links`, `answers`, and `notes` in `submission.json`.
4. Change its `status` from `draft` to `submitted`.
5. Commit and push the final version before the deadline.

The instructor's GitHub Action pins the exact commit it reads, validates the JSON, matches the registered wallets, checks available blockchain evidence, and updates the result workbook.

## If the result needs review

The instructor checks `Manual review` and `Errors`. Common reasons are an invalid JSON file, a draft section, a wallet mismatch, the wrong testnet, an unavailable RPC/explorer, or evidence that requires human assessment.

!!! danger
    Never commit or submit a seed phrase, private key, wallet password, service-account key, or API key. Only public addresses, transaction hashes, contract addresses, and public links belong in the registry or report.
