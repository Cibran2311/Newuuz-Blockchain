# Mission 8 — Enter Polkadot

## Goal

Create a Polkadot account, receive Westend tokens, send an extrinsic, and inspect it in Subscan.

---

## Why This Lab Matters

Polkadot is architecturally different from Ethereum. It uses accounts, extrinsics, runtime logic, and parachains.

---

## What You Will Learn

After completing this lab you will be able to:

- install Polkadot.js extension
- create SS58 account
- send Westend extrinsic
- use Subscan
- compare with Ethereum transaction

---

## Required Reading

| Topic | Link |
|---|---|
| Polkadot docs | https://docs.polkadot.com/ |
| Polkadot.js Extension | https://polkadot.js.org/extension/ |
| Polkadot.js Apps | https://polkadot.js.org/apps/ |
| Westend Subscan | https://westend.subscan.io/ |

---

## Required Software

| Tool | Purpose |
|---|---|
| Polkadot.js Extension | Wallet |
| Polkadot.js Apps | Send extrinsic |
| Westend faucet | Test tokens |
| Subscan | Explorer |

---

## Key Terms

| Term | Meaning |
|---|---|
| `SS58` | Polkadot address format. |
| `Extrinsic` | Action submitted to chain. |
| `Runtime` | Chain logic. |
| `Westend` | Test network. |
| `Subscan` | Explorer. |

---

## Safety Notes

!!! warning "Use course test environments"
    Do not use real funds or mainnet assets. Save transaction hashes immediately.

---

## Step-by-Step Instructions

### Step 1 — Install extension

Install Polkadot.js and create account.

### Step 2 — Get tokens

Use faucet/instructor.

### Step 3 — Open Apps

Connect to Westend.

### Step 4 — Send transfer

Send small amount to assigned account.

### Step 5 — Open Subscan

Find extrinsic.

### Step 6 — Submit evidence

Record address, hash, link.

---

## Expected Result

Successful Westend extrinsic and Subscan link.

---

## Submission

Add this fragment to `submission.json`:

```json
{"labs":{"lab8":{"network":"westend","polkadot_wallet":"5...","extrinsic_hash":"...","explorer_url":"https://westend.subscan.io/extrinsic/..."}}}
```

---

## Automatic Validation

| Check | Requirement |
|---|---|
| Extrinsic | Exists. |
| Signer | Matches wallet. |
| Network | Westend. |
| Status | Success. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Ethereum address | Use SS58. |
| Wrong network | Use Westend. |
| Block hash | Submit extrinsic hash. |

---

## Self-Check Questions

1. What is extrinsic?
2. What is SS58?
3. What is Westend?
