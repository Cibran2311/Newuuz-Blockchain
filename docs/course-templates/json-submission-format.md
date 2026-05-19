# JSON Submission Format

Each assignment should include a `submission.json` file in the root of the student repository.

The JSON file is used for automatic validation through GitHub Actions or an external grading platform.

## Base structure

```json
{
  "student": {
    "full_name": "Ivan Ivanov",
    "student_id": "123456",
    "github_username": "ivan-blockchain"
  },
  "wallets": {
    "ethereum_sepolia": "0x...",
    "polkadot_westend": "5...",
    "ton_testnet": "kQ..."
  },
  "assignments": {
    "assignment1_nft_erc20_disperse": {},
    "assignment2_ethernaut": {},
    "assignment3_multichain_contract_chain": {},
    "assignment4_technical_article": {}
  }
}
```

## Rules

- Do not submit private keys or seed phrases.
- All transaction hashes must be public explorer-verifiable transactions.
- Wallet addresses must belong to the student.
- If a field is not applicable, use `null` rather than deleting the field.
- The file must be valid JSON, not JavaScript.
