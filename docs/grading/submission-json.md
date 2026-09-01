# `submission.json` Format

Every student repository contains one `submission.json` at its root. It is the report index for all course work, not a copy of the class registry.

## Top-level structure

```json
{
  "schema_version": 2,
  "student_id": "TEST-001",
  "labs": {
    "lab1": {}
  },
  "assignments": {
    "assignment1": {}
  }
}
```

The real file must keep all `lab1`–`lab12` and `assignment1`–`assignment4` objects. Start from `submission.example.json`; the formal rules are in `schemas/submission.schema.json`.

## Work object

Each lab or assignment uses the same envelope:

| Field | Meaning |
|---|---|
| `status` | `draft` while working; `submitted` when ready to check |
| `network` | Required testnet or environment |
| `evidence` | Task-specific transaction hashes, contracts, token IDs, or output values |
| `links` | Public repository, explorer, notebook, report, or article URLs |
| `answers` | Short required explanations or calculated values |
| `notes` | Optional context for the instructor |

The example file shows task-specific evidence keys. Do not delete unfinished sections; leave them as `draft`.

## What the checker trusts

- `student_id` must exactly match the Sheet row.
- GitHub supplies the pinned commit and report contents.
- Google Sheets supplies registered public wallets and the exact repository.
- Blockchains and explorer/RPC APIs supply transaction truth.
- JSON declares what should be checked and links the evidence; it cannot replace on-chain evidence.

The workflow stores the pinned commit SHA in both Google Sheets and its downloadable JSON audit artifact.

## Validation

From a local clone of the course repository, install the autotest requirements and pass the student file path:

```bash
python -m pip install -r requirements-autotest.txt
python scripts/check_submission_json.py /path/to/student-repo/submission.json
```

An invalid file is reported as `INVALID REPORT`; a valid `draft` section is not treated as submitted.
