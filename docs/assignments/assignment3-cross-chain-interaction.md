# Assignment 3 — Cross-chain Smart Contract Interaction

## Goal

Perform related blockchain actions across Ethereum, Polkadot, and TON and compare architectures.

## Learning Objectives

After completing this assignment students will be able to:

- interact with smart contracts;
- analyze blockchain events;
- collect evidence from explorers;
- submit machine-readable results.

## Tasks

1. Start on Ethereum Sepolia
2. Continue in Polkadot / AssetHub
3. Complete in TON
4. Compare fees, speed, tooling, and execution model

## Deliverables

Students must submit all evidence in `submission.json` and include required reports, links, or scripts in the repository.

## submission.json Example

```json
{
  "assignments": {"assignment3": {"ethereum": {"wallet": "0x...", "tx_hash": "0x..."}, "polkadot": {"wallet": "5...", "extrinsic_hash": "..."}, "ton": {"wallet": "kQ...", "tx_link": "..."}, "comparison_notes": "..."}}
}
```

## Automatic Validation

The checker verifies submitted blockchain evidence, correct network, wallet ownership, and assignment-specific conditions.
