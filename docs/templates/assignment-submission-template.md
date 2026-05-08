# Assignment Submission Template

## Student information

| Field | Value |
|---|---|
| Full name |  |
| Student ID |  |
| GitHub repository |  |
| Wallet address |  |

## Assignment

| Field | Value |
|---|---|
| Assignment number |  |
| Topic |  |
| Submission date |  |

## Deliverables

| Required item | Link / file / value |
|---|---|
| 1 |  |
| 2 |  |
| 3 |  |

## Short explanation

Write a short explanation of your work and how it can be verified.


## Required JSON file

Create `submission.json` in the root of your repository.

Minimum example:

```json
{
  "student": {
    "full_name": "",
    "student_id": "",
    "github_username": ""
  },
  "course": {
    "code": "CS423",
    "semester": "Spring 2026"
  },
  "wallets": {
    "ethereum_sepolia": "",
    "polkadot_westend": "",
    "ton_testnet": ""
  },
  "assignments": {}
}
```

Validate before submitting:

```bash
python -m json.tool submission.json
```
