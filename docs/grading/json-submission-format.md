# JSON Submission Format

Each assignment repository should contain `submission.json` in the repository root.

## General structure

```json
{
  "student": {
    "full_name": "Ivan Ivanov",
    "student_id": "123456",
    "github_username": "ivan-blockchain"
  },
  "wallets": {
    "ethereum_sepolia": "0x0000000000000000000000000000000000000000",
    "polkadot_westend": "",
    "ton_testnet": ""
  },
  "assignments": {
    "assignment1": {},
    "assignment2": {},
    "assignment3": {},
    "assignment4": {}
  }
}
```

Do not submit private keys or seed phrases.
