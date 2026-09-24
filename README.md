# CS422/CS423 Blockchain Technologies

Student-ready MkDocs Material course site for the Blockchain Technologies course.

## Required Course Path

```text
Lab 1, Lab 2, Lab 3,
Lab 4, Lab 5, Lab 6,
Lab 7, Lab 8, Lab 9,
Lab 10, Lab 11, Lab 12,
Assignment 1, Assignment 2,
Assignment 3, Assignment 4
```

## Additional Challenges

No existing lab or assignment is classified as an additional challenge yet. Difficulty and bonus placement will be decided after the complete path is reviewed.

## Expected Workload

| Level | Approximate Workload |
|---|---:|
| Current complete path | 55–75 hours |
| After difficulty redistribution | To be confirmed |

## Submission and Auto-check Flow

1. The instructor creates the protected Google Sheets registry.
2. Students register their exact public GitHub repository and public testnet wallets.
3. Each repository contains one `submission.json` covering all 12 labs and 4 assignments.
4. GitHub Actions pins the report commit, validates the JSON, and checks available GitHub/blockchain evidence against registered wallets.
5. The permanent result workbook receives lab and assignment summaries, detailed evidence, manual-review rows, errors, and run history.

Start from `submission.example.json`. The schema is `schemas/submission.schema.json`, and local validation is available through `scripts/check_submission_json.py`.

## Local Preview

```bash
python -m pip install -r requirements.txt
mkdocs serve
```

Open:

```text
http://127.0.0.1:8000
```

## Build

```bash
mkdocs build --strict
```

## GitHub Pages

1. Push the repository to GitHub.
2. Open **Settings → Pages**.
3. Select **Source → GitHub Actions**.
4. Run **Actions → Deploy MkDocs**.
