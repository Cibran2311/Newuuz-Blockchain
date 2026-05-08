# JSON Submission Format

Each assignment repository should contain a machine-readable file named `submission.json` in the repository root.

This file is used for automatic or semi-automatic checking. Students still submit notebooks, reports, links, or code when required, but the key verification data must also be duplicated in `submission.json`.

## Why JSON is required

JSON makes grading easier because the checker can read one predictable file and extract:

- student identity;
- wallet addresses;
- transaction hashes;
- contract addresses;
- Ethernaut levels;
- links to notebooks, articles, or explorers.

## Required file name

```text
submission.json
```

## General structure

```json
{
  "student": {
    "full_name": "Ivan Ivanov",
    "student_id": "123456",
    "github_username": "ivan-blockchain"
  },
  "course": {
    "code": "CS423",
    "semester": "Spring 2026"
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

## Assignment 1 — ERC20 + NFT + Uniswap

```json
{
  "assignments": {
    "assignment1": {
      "erc20": {
        "contract_address": "0x...",
        "deployment_tx": "0x...",
        "mint_tx": "0x..."
      },
      "nft": {
        "standard": "ERC721 or ERC1155",
        "contract_address": "0x...",
        "deployment_tx": "0x...",
        "mint_tx": "0x...",
        "token_id": "1"
      },
      "uniswap": {
        "network": "sepolia",
        "swap_tx": "0x...",
        "pool_or_position_tx": "0x..."
      },
      "notes": "Short explanation of what was deployed and how to verify it."
    }
  }
}
```

## Assignment 2 — Ethernaut

```json
{
  "assignments": {
    "assignment2": {
      "wallet_address": "0x...",
      "complexity_total": 10,
      "levels_solved_count": 5,
      "levels": [
        {
          "level_number": 0,
          "level_name": "Hello Ethernaut",
          "complexity": 1,
          "instance_address": "0x...",
          "create_instance_tx": "0x...",
          "interaction_txs": ["0x..."],
          "submit_instance_tx": "0x...",
          "status": "passed",
          "short_explanation": "What vulnerability or mechanism was used."
        }
      ]
    }
  }
}
```

Accepted `status` values:

```text
passed | tried | not_found
```

## Assignment 3 — Liquidity Provision

```json
{
  "assignments": {
    "assignment3": {
      "notebook_file": "assignment3_liquidity_123456.ipynb",
      "repository_url": "https://github.com/...",
      "tasks_completed": {
        "3.1": true,
        "3.2": true,
        "3.3": true,
        "3.4": true,
        "3.5_bonus": false
      },
      "fresh_kernel_runs": true,
      "plots": ["fee_income_vs_volume.png"],
      "short_report_location": "Last markdown cell in notebook"
    }
  }
}
```

## Assignment 4 — Technical Article

```json
{
  "assignments": {
    "assignment4": {
      "article_url": "https://...",
      "platform": "Medium",
      "topic": "AMM Mathematics",
      "reading_time_minutes": 7,
      "word_count_estimate": 1600,
      "has_formal_section": true,
      "has_original_diagram": true,
      "sources_count": 5,
      "moderated_platform_bonus_claimed": false
    }
  }
}
```

## Validation rule for students

Before submitting, students should check that the JSON is valid:

```bash
python -m json.tool submission.json
```

If this command fails, the submission file is malformed and may not be accepted by the checker.
