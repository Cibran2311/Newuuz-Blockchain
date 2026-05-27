# Assignment 3 — Cross-chain Journey: Ethereum, Polkadot, TON

## Goal

Perform related blockchain actions across Ethereum, Polkadot, and TON, then compare the differences between the ecosystems.

This assignment is the main expression of the course methodology:

> Do similar blockchain actions in different networks and compare architecture, tooling, fees, and execution models.

---

## Scenario

You are a cross-chain operator.

Your task is to complete a three-part workflow:

```text
Ethereum Sepolia → Polkadot / AssetHub → TON Testnet
```

Each step must produce verifiable blockchain evidence.

The exact contract/action may be assigned by the instructor, but the final submission must prove that you can work across all three ecosystems.

---

## Learning Objectives

After completing this assignment you will be able to:

- compare Ethereum, Polkadot, and TON;
- work with several wallet types;
- collect evidence from different explorers;
- understand EVM transactions, Polkadot extrinsics, and TON messages;
- explain differences in fees, execution, account model, and developer tooling.

---

## Requirements

1. Complete the Ethereum step on Sepolia.
2. Complete the Polkadot step on Westend / AssetHub.
3. Complete the TON step on TON Testnet.
4. Use wallets that belong to you.
5. Save transaction/extrinsic/message evidence.
6. Write comparison notes.
7. Submit everything in `submission.json`.

---

## Suggested Workflow

### Step 1 — Ethereum Step

Perform the assigned Ethereum action.

Examples:

- call a smart contract;
- transfer ERC20;
- send NFT;
- trigger event;
- interact with class contract.

Save:

- Ethereum wallet;
- contract address;
- transaction hash;
- event name if applicable;
- Etherscan link.

---

### Step 2 — Polkadot Step

Perform the assigned Polkadot / AssetHub action.

Examples:

- send Westend transfer;
- perform AssetHub action;
- submit XCM-related extrinsic;
- interact with assigned pallet/action.

Save:

- Polkadot wallet;
- extrinsic hash;
- source/destination chain if relevant;
- Subscan link.

---

### Step 3 — TON Step

Perform the assigned TON action.

Examples:

- send TON testnet transaction;
- transfer jetton;
- execute STON.fi swap;
- complete TON challenge.

Save:

- TON wallet;
- transaction link;
- message trace if relevant;
- Tonviewer link.

---

### Step 4 — Compare Architectures

Write a short comparison.

Use this table as a guide:

| Metric | Ethereum | Polkadot | TON |
|---|---|---|---|
| Account model |  |  |  |
| Transaction model |  |  |  |
| Fees |  |  |  |
| Explorer |  |  |  |
| Smart contract model |  |  |  |
| Developer experience |  |  |  |
| Finality / speed |  |  |  |

---

## Deliverables

Submit:

- Ethereum transaction hash;
- Ethereum contract address if used;
- Polkadot extrinsic hash;
- TON transaction link;
- comparison notes;
- all relevant wallet addresses.

---

## Submission Format

```json
{
  "assignments": {
    "assignment3": {
      "ethereum": {
        "network": "sepolia",
        "wallet": "0xYourEthereumWallet",
        "contract": "0xContractIfUsed",
        "tx_hash": "0xEthereumTx",
        "explorer_url": "https://sepolia.etherscan.io/tx/0xEthereumTx"
      },
      "polkadot": {
        "network": "westend_or_assethub",
        "wallet": "5YourPolkadotWallet",
        "extrinsic_hash": "0xExtrinsicHash",
        "explorer_url": "https://..."
      },
      "ton": {
        "network": "ton_testnet",
        "wallet": "kQYourTonWallet",
        "tx_link": "https://testnet.tonviewer.com/..."
      },
      "comparison": {
        "account_model": "...",
        "transaction_model": "...",
        "fees": "...",
        "developer_experience": "...",
        "finality_or_speed": "..."
      }
    }
  }
}
```

---

## Automatic / Semi-Automatic Validation

| Check | Requirement |
|---|---|
| Ethereum evidence | Transaction exists on Sepolia. |
| Polkadot evidence | Extrinsic exists on expected network. |
| TON evidence | Transaction exists on TON Testnet. |
| Wallet ownership | Submitted wallets are involved in actions. |
| Comparison | Required comparison fields are present. |
| Networks | Mainnet evidence is not accepted unless explicitly allowed. |

---

## Grading Rubric

| Criterion | Weight | Description |
|---|---:|---|
| Ethereum step | 25% | Correct Ethereum action and evidence. |
| Polkadot step | 25% | Correct Polkadot/AssetHub action and evidence. |
| TON step | 25% | Correct TON action and evidence. |
| Comparison quality | 20% | Meaningful architecture comparison. |
| Submission quality | 5% | JSON is valid and complete. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Completing only one chain | Complete all three ecosystems. |
| No comparison notes | Fill comparison fields. |
| Wrong explorer link | Use Etherscan, Subscan, Tonviewer correctly. |
| Wrong network | Use Sepolia, Westend/AssetHub testnet, TON Testnet. |
| Wallet mismatch | Use your own wallets and submit matching addresses. |

---

## Final Checklist

- [ ] Ethereum transaction is complete.
- [ ] Polkadot extrinsic is complete.
- [ ] TON transaction is complete.
- [ ] All explorer links work.
- [ ] Comparison notes are written.
- [ ] `submission.json` is valid.
