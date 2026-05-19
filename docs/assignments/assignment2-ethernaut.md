# Assignment 2 — Ethernaut Security Challenges

## Overview

This assignment focuses on Solidity security and EVM behavior through the Ethernaut CTF platform. Students solve vulnerable smart contract levels on Ethereum Sepolia and submit evidence through wallet-based transaction history.

## Goal

Solve Ethernaut levels until the total complexity score is **at least 10**.

## Learning outcomes

Students should be able to:

- inspect vulnerable Solidity contracts;
- identify common smart contract vulnerabilities;
- interact with deployed challenge instances;
- use Remix, Etherscan, and MetaMask for exploit execution;
- understand why a contract is vulnerable;
- submit verifiable blockchain evidence.

## Student tasks

1. Open the Ethernaut platform.
2. Connect MetaMask to Sepolia.
3. Create level instances.
4. Solve selected levels.
5. Submit completed level instances.
6. Reach total complexity score `>= 10`.
7. Record the completed levels and transaction evidence in `submission.json`.

## Complexity requirement

| Total complexity | Result |
|---:|---|
| `< 7` | insufficient |
| `7–9` | partial completion |
| `>= 10` | full completion |
| `15+ unique levels` | bonus candidate |

The exact level-to-complexity map should be configured by the instructor and stored in the checker configuration rather than hardcoded in student instructions.

## Required `submission.json` fields

```json
{
  "assignment_id": "assignment2_ethernaut",
  "network": "sepolia",
  "wallet": "0x...",
  "levels": [
    {
      "level_name": "Fallback",
      "level_address": "0x...",
      "instance_address": "0x...",
      "create_instance_tx": "0x...",
      "interaction_txs": ["0x..."],
      "submit_tx": "0x...",
      "complexity": 1
    }
  ],
  "claimed_total_complexity": 10
}
```

## Automatic validation plan

The checker should:

1. Load the official Ethernaut deployment/proxy address for Sepolia.
2. Query `LevelCompletedLog` events for the student wallet.
3. Deduplicate completed levels.
4. Map completed level addresses to instructor-defined complexity scores.
5. Sum the complexity.
6. Apply the threshold rules.
7. Store evidence in an append-only grading log.

## Grading rubric

| Criterion | Weight |
|---|---:|
| Valid Ethernaut wallet evidence | 20% |
| Completed levels detected on-chain | 40% |
| Complexity score `>= 10` | 25% |
| Clear submission data | 15% |

## Academic integrity

Students may use documentation and AI tools to understand concepts, but they must be able to explain every completed level and exploit path verbally.
