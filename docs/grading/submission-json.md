# submission.json

Every student repository must contain a file named:

```text
submission.json
```

This file is the main source of evidence for automatic grading.

## Why We Use JSON

Blockchain assignments produce many pieces of evidence:

- wallet addresses;
- transaction hashes;
- contract addresses;
- token IDs;
- explorer links;
- article URLs;
- notebook paths.

A single machine-readable JSON file allows GitHub Actions and grading scripts to check submissions automatically.

## Basic Structure

```json
{
  "student": {
    "full_name": "Student Name",
    "student_id": "123456",
    "github_username": "student-github"
  },
  "wallets": {
    "ethereum_sepolia": "0x0000000000000000000000000000000000000000",
    "polkadot_westend": "5...",
    "ton_testnet": "kQ..."
  },
  "labs": {},
  "assignments": {}
}
```

## Example with Labs

```json
{
  "student": {
    "full_name": "Ivan Ivanov",
    "student_id": "220000",
    "github_username": "ivan-blockchain"
  },
  "wallets": {
    "ethereum_sepolia": "0x1111111111111111111111111111111111111111",
    "polkadot_westend": "5ExampleAddress",
    "ton_testnet": "kQExampleAddress"
  },
  "labs": {
    "lab1": {
      "network": "sepolia",
      "wallet": "0x1111111111111111111111111111111111111111",
      "recipient": "0x2222222222222222222222222222222222222222",
      "amount_eth": "0.0001",
      "tx_hash": "0xabc...",
      "explorer_url": "https://sepolia.etherscan.io/tx/0xabc..."
    },
    "lab5": {
      "network": "sepolia",
      "wallet": "0x1111111111111111111111111111111111111111",
      "token_contract": "0x3333333333333333333333333333333333333333",
      "transfer_txs": [
        "0xtransfer1...",
        "0xtransfer2...",
        "0xtransfer3..."
      ],
      "disperse_tx": "0xdisperse..."
    }
  },
  "assignments": {
    "assignment2": {
      "network": "sepolia",
      "ethernaut_wallet": "0x1111111111111111111111111111111111111111",
      "target_complexity": 10,
      "claimed_levels": [
        "Fallback",
        "Fallout",
        "Coin Flip"
      ]
    }
  }
}
```

## Validation Rules

| Rule | Description |
|---|---|
| Valid JSON | File must parse correctly. |
| Required fields | Student and wallet fields must exist. |
| Address format | Ethereum addresses must look like `0x...`. |
| Transaction existence | Submitted tx hashes must exist on correct network. |
| Wallet ownership | Transaction sender must match submitted wallet. |
| Event evidence | Token/NFT/Ethernaut events must exist. |
| Deadline | Transaction time must be before deadline if enabled. |

## How to Check JSON Locally

You can check JSON syntax with Python:

```bash
python -m json.tool submission.json
```

## Common JSON Mistakes

| Mistake | Wrong | Correct |
|---|---|---|
| Missing comma | `"a": 1 "b": 2` | `"a": 1, "b": 2` |
| Comments in JSON | `// comment` | Remove comments |
| Single quotes | `'wallet': '0x...'` | `"wallet": "0x..."` |
| Trailing comma | `"a": 1, }` | `"a": 1 }` |
| Array written as string | `"txs": "0x1,0x2"` | `"txs": ["0x1", "0x2"]` |

## Security Rules

!!! danger
    Never put private keys or seed phrases in `submission.json`.

!!! warning
    Do not submit mainnet transactions unless the instructor explicitly asks for them.

!!! info
    Use testnets: Sepolia, Westend / AssetHub test environments, and TON Testnet.
