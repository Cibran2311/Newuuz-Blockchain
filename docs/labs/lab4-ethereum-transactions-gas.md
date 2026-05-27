# Mission 4 — Read the Chain

## Goal

Analyze an Ethereum transaction and understand gas, nonce, status, and fees.

---

## Why This Lab Matters

Developers debug smart contracts by reading transaction details. This lab makes explorers useful instead of mysterious.

---

## What You Will Learn

After completing this lab you will be able to:

- read Etherscan fields
- explain gas limit vs gas used
- find transaction fee
- record transaction evidence

---

## Required Reading

| Topic | Link |
|---|---|
| Ethereum gas | https://ethereum.org/en/developers/docs/gas/ |
| Ethereum transactions | https://ethereum.org/en/developers/docs/transactions/ |
| Sepolia Etherscan | https://sepolia.etherscan.io/ |

---

## Required Software

| Tool | Purpose |
|---|---|
| MetaMask | Transaction source |
| Etherscan | Explorer |

---

## Key Terms

| Term | Meaning |
|---|---|
| `Gas limit` | Maximum gas allowed. |
| `Gas used` | Actual gas consumed. |
| `Nonce` | Transaction counter. |
| `Status` | Success/failure. |
| `Fee` | Cost of transaction. |

---

## Safety Notes

!!! danger "Never share secrets"
    Never submit private keys, seed phrases, recovery phrases, or passwords.

!!! warning "Use testnets only"
    Use Sepolia for Ethereum labs unless the instructor explicitly says otherwise.

---

## Step-by-Step Instructions

### Step 1 — Choose tx

Use Lab 1 tx or send a new Sepolia tx.

### Step 2 — Open Etherscan

Search by transaction hash.

### Step 3 — Record fields

From, To, Nonce, Gas Limit, Gas Used, Fee, Status.

### Step 4 — Explain gas

Write a short explanation.

### Step 5 — Update JSON

Add tx and gas fields.

---

## Expected Result

A transaction analysis with correct gas fields and explanation.

---

## Submission

Add this fragment to `submission.json`:

```json
{"labs":{"lab4":{"tx_hash":"0x...","gas_limit":21000,"gas_used":21000,"status":"success","explanation":"Gas limit is ..."}}}
```

---

## Automatic Validation

| Check | Requirement |
|---|---|
| Transaction | Hash exists. |
| Gas fields | Values match explorer. |
| Explanation | Non-empty. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Gas price vs gas used | Use correct field. |
| Mainnet tx | Use Sepolia. |
| Empty explanation | Add 3–5 sentences. |

---

## Self-Check Questions

1. What is gas?
2. What is nonce?
3. What is failed transaction?
