# Mission 11 — Dissect a Jetton Transfer

## Goal

Work with TON jettons and compare them with ERC20 tokens.

---

## Why This Lab Matters

TON jettons use Jetton Master and per-holder Jetton Wallet contracts. This shows how TON architecture differs from Ethereum.

---

## What You Will Learn

After completing this lab you will be able to:

- explain Jetton Master
- identify Jetton Wallets
- send jetton
- inspect trace
- compare with ERC20

---

## Required Reading

| Topic | Link |
|---|---|
| TON docs | https://docs.ton.org/ |
| TON token contracts | https://github.com/ton-blockchain/token-contract |
| Testnet Tonviewer | https://testnet.tonviewer.com/ |

---

## Required Software

| Tool | Purpose |
|---|---|
| Tonkeeper | Wallet |
| Test jetton | Token |
| Tonviewer | Explorer |

---

## Key Terms

| Term | Meaning |
|---|---|
| `Jetton` | TON fungible token standard. |
| `Jetton Master` | Metadata/code contract. |
| `Jetton Wallet` | Per-holder balance contract. |
| `Internal message` | Contract-to-contract message. |

---

## Safety Notes

!!! warning "Use course test environments"
    Do not use real funds or mainnet assets. Save transaction hashes immediately.

---

## Step-by-Step Instructions

### Step 1 — Receive jetton

Import/receive class jetton.

### Step 2 — Send jetton

Transfer to partner/instructor.

### Step 3 — Open trace

Inspect messages in Tonviewer.

### Step 4 — Find contracts

Record Master and Jetton Wallets.

### Step 5 — Explain architecture

Write short comparison with ERC20.

### Step 6 — Submit evidence

Add addresses and link.

---

## Expected Result

Jetton transfer trace and Jetton Master/Wallet addresses.

---

## Submission

Add this fragment to `submission.json`:

```json
{"labs":{"lab11":{"network":"ton_testnet","jetton_master":"kQ...","sender_jetton_wallet":"kQ...","recipient_jetton_wallet":"kQ...","tx_link":"https://testnet.tonviewer.com/..."}}}
```

---

## Automatic Validation

| Check | Requirement |
|---|---|
| Transfer | Jetton transfer exists. |
| Wallets | Jetton Wallet addresses present. |
| Network | Testnet. |
| Explanation | Present. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Wallet vs Jetton Wallet | Record both. |
| TON transfer instead of jetton | Submit token transfer. |
| No trace | Use Tonviewer trace. |

---

## Self-Check Questions

1. Why per-holder Jetton Wallet?
2. How different from ERC20?
3. What is Jetton Master?
