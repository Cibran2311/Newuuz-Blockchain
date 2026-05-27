# Mission 9 — Send a Cross-chain Message

## Goal

Explore AssetHub and XCM in the Polkadot ecosystem.

---

## Why This Lab Matters

Polkadot uses multiple specialized chains. XCM is the messaging format that lets them communicate.

---

## What You Will Learn

After completing this lab you will be able to:

- explain Relay Chain
- explain parachains
- understand AssetHub
- describe XCM
- inspect cross-chain extrinsic

---

## Required Reading

| Topic | Link |
|---|---|
| Polkadot docs | https://docs.polkadot.com/ |
| Polkadot.js Apps | https://polkadot.js.org/apps/ |
| Subscan | https://subscan.io/ |

---

## Required Software

| Tool | Purpose |
|---|---|
| Polkadot.js Extension | Wallet |
| Polkadot.js Apps | Interface |
| Subscan | Explorer |

---

## Key Terms

| Term | Meaning |
|---|---|
| `Relay Chain` | Shared security chain. |
| `Parachain` | Specialized connected chain. |
| `AssetHub` | Asset management chain. |
| `XCM` | Cross-consensus messaging. |

---

## Safety Notes

!!! warning "Use course test environments"
    Do not use real funds or mainnet assets. Save transaction hashes immediately.

---

## Step-by-Step Instructions

### Step 1 — Connect wallet

Open Polkadot.js Apps.

### Step 2 — Select chains

Use Westend/AssetHub as instructed.

### Step 3 — Perform action

Execute asset or XCM-related action.

### Step 4 — Find extrinsic

Open in Subscan.

### Step 5 — Explain route

Describe source, destination, action.

### Step 6 — Submit JSON

Add hash and explanation.

---

## Expected Result

AssetHub/XCM-related extrinsic and explanation.

---

## Submission

Add this fragment to `submission.json`:

```json
{"labs":{"lab9":{"source_chain":"Westend","destination_chain":"AssetHub","extrinsic_hash":"...","explorer_url":"...","explanation":"..."}}}
```

---

## Automatic Validation

| Check | Requirement |
|---|---|
| Extrinsic | Exists. |
| Action | Related to XCM/AssetHub. |
| Signer | Student signed. |
| Explanation | Present. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Normal transfer only | Use assigned XCM action. |
| Wrong chain | Check selected network. |
| No explanation | Describe message route. |

---

## Self-Check Questions

1. What is XCM?
2. What is AssetHub?
3. How is XCM different from bridge?
