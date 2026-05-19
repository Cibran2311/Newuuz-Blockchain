# Assignment 3 — Multi-chain Contract Chain

## Overview

This assignment is the central multi-chain assignment of the course. Students repeat comparable actions across Ethereum, Polkadot, and TON, then compare how each ecosystem handles wallets, transactions, assets, contracts, fees, and execution.

The assignment should not be treated as three unrelated tasks. It is a single chain of evidence across three blockchain ecosystems.

## Main idea

A student completes a contract or transaction chain in three networks:

```text
Ethereum Sepolia → Polkadot Westend / AssetHub → TON Testnet
```

Each step produces public evidence. The final submission explains how the same general action differs across networks.

## Learning outcomes

Students should be able to:

- interact with Ethereum contracts;
- send or verify Polkadot extrinsics;
- work with TON wallet/message flows;
- compare EVM, Substrate, and TON execution models;
- understand why blockchain architecture affects application design;
- collect cross-chain evidence in one structured submission.

## Student tasks

### Part 1 — Ethereum step

The student must complete one Ethereum Sepolia contract interaction.

Possible instructor-provided options:

- call a trigger contract;
- activate a contract that emits an event;
- send ERC20 tokens through a contract;
- interact with a contract that unlocks the next step.

Required evidence:

- Ethereum wallet address;
- contract address;
- transaction hash;
- emitted event or state change.

### Part 2 — Polkadot step

The student must complete one Polkadot-related action on Westend or AssetHub.

Possible options:

- send a testnet transaction;
- create or transfer an AssetHub asset;
- execute an XCM-related action;
- interact with an EVM-compatible contract if the course environment supports it.

Required evidence:

- Polkadot address;
- extrinsic hash;
- network name;
- explorer link;
- short description of what changed on-chain.

### Part 3 — TON step

The student must complete one TON Testnet action.

Possible options:

- send TON on testnet;
- send Jettons;
- interact with a TON contract;
- complete a STON.fi testnet swap;
- complete a HackTON-style beginner challenge.

Required evidence:

- TON address;
- transaction hash or tonviewer link;
- contract or Jetton address if applicable;
- short explanation of the message flow.

### Part 4 — comparison report

The student must compare the three ecosystems using the following table:

| Metric | Ethereum | Polkadot | TON |
|---|---|---|---|
| Wallet/account model |  |  |  |
| Transaction structure |  |  |  |
| Contract model |  |  |  |
| Fee model |  |  |  |
| Explorer/debugging UX |  |  |  |
| Speed/finality observation |  |  |  |
| Main difficulty |  |  |  |

## Required `submission.json` fields

```json
{
  "assignment_id": "assignment3_multichain_contract_chain",
  "student": {
    "full_name": "Ivan Ivanov",
    "student_id": "123456"
  },
  "ethereum": {
    "network": "sepolia",
    "wallet": "0x...",
    "contract": "0x...",
    "tx": "0x...",
    "event": "StepCompleted"
  },
  "polkadot": {
    "network": "westend_or_assethub",
    "wallet": "5...",
    "extrinsic_hash": "0x...",
    "explorer_url": "https://..."
  },
  "ton": {
    "network": "testnet",
    "wallet": "kQ...",
    "tx_url": "https://testnet.tonviewer.com/...",
    "contract_or_jetton": "kQ..."
  },
  "comparison": {
    "ethereum_notes": "...",
    "polkadot_notes": "...",
    "ton_notes": "..."
  }
}
```

## Automatic validation plan

| Network | Validation approach |
|---|---|
| Ethereum | RPC log query, event detection, contract call evidence |
| Polkadot | RPC/Subscan query for extrinsic signed by student address |
| TON | TON Center or Tonviewer API query for transaction from student wallet |

## Grading rubric

| Criterion | Weight |
|---|---:|
| Ethereum step completed | 25% |
| Polkadot step completed | 25% |
| TON step completed | 25% |
| Architecture comparison | 15% |
| Correct `submission.json` and evidence | 10% |

## Instructor notes

This assignment is the best place to show the main philosophy of the course: the same high-level task looks different depending on blockchain architecture.
