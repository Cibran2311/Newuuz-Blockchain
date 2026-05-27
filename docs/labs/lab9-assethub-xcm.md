# Mission 9 — Send a Cross-chain Message

## Goal

In this lab you will explore AssetHub and XCM in the Polkadot ecosystem. You will perform or analyze a cross-chain-related action and explain how it differs from a normal transfer.

---

## Why This Lab Matters

Polkadot is built around multiple specialized chains. XCM is a key part of Polkadot architecture because it allows chains to communicate.

---

## What You Will Learn

After completing this lab you will be able to:

- explain Relay Chain and parachains;
- explain AssetHub;
- explain XCM;
- identify source and destination chains;
- inspect cross-chain extrinsics;
- compare XCM with traditional bridges.

---

## Required Reading

| Topic | Link |
|---|---|
| Polkadot documentation | https://docs.polkadot.com/ |
| Polkadot.js Apps | https://polkadot.js.org/apps/ |
| Subscan | https://subscan.io/ |

---

## Required Software

| Tool | Purpose |
|---|---|
| Polkadot.js Extension | Sign extrinsics |
| Polkadot.js Apps | Perform XCM/AssetHub action |
| Westend / AssetHub | Test environment |
| Subscan | Explorer |

---

## Key Terms

| Term | Meaning |
|---|---|
| `Relay Chain` | Central Polkadot chain providing shared security. |
| `Parachain` | Specialized blockchain connected to Relay Chain. |
| `AssetHub` | System parachain for asset operations. |
| `XCM` | Cross-Consensus Messaging format. |
| `Reserve transfer` | Transfer model where assets are reserved on one chain and represented on another. |

---

## Safety Notes

!!! warning "Follow instructor network"
    XCM interfaces and networks may change. Use the chain and action specified in class.

!!! info
    XCM is not the same as a simple account-to-account transfer.

---

## Step-by-Step Instructions

### Step 1 — Open Polkadot.js Apps

Open https://polkadot.js.org/apps/ and connect your Polkadot.js extension.

### Step 2 — Select Required Chain

The instructor will specify which chains to use, for example `Westend → AssetHub`.

Record source chain, destination chain, and wallet address.

### Step 3 — Prepare Balance

Make sure your wallet has enough test tokens for fees.

### Step 4 — Perform AssetHub / XCM Action

Depending on class setup, perform reserve transfer, asset transfer, XCM action, or assigned extrinsic.

### Step 5 — Inspect Extrinsic

Open Subscan and find extrinsic hash, signer, pallet/method, success/failure, events, and source/destination data.

### Step 6 — Explain Message Flow

Write a short explanation:

```text
The action started on ...
The destination chain was ...
The asset/message moved by ...
This differs from a normal transfer because ...
```

---

## Expected Result

At the end of this lab you should have an AssetHub/XCM-related extrinsic hash, source and destination chain, Subscan link, and short explanation.

---

## Submission

```json
{
  "labs": {
    "lab9": {
      "source_chain": "Westend",
      "destination_chain": "AssetHub",
      "polkadot_wallet": "5YourAddress",
      "extrinsic_hash": "0xExtrinsicHash",
      "explorer_url": "https://...",
      "explanation": "The message starts on ... and is executed on ..."
    }
  }
}
```

---

## Automatic Validation

| Check | Requirement |
|---|---|
| Extrinsic | Submitted extrinsic exists. |
| Network | Extrinsic is on required network. |
| Signer | Student wallet signed the extrinsic. |
| Action | Extrinsic is related to AssetHub/XCM if detectable. |
| Explanation | Source/destination explanation is present. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Submitting normal transfer only | Use assigned XCM/AssetHub action. |
| Wrong source chain | Check network selector before submitting. |
| Wrong destination chain | Record destination carefully. |
| Failed extrinsic | Check status and repeat if needed. |
| Empty explanation | Explain route in your own words. |

---

## Self-Check Questions

1. What is AssetHub?
2. What is XCM?
3. How is XCM different from a simple transfer?
4. Why does Polkadot use parachains?
5. What evidence proves that your XCM-related action happened?
