# Mission 4 — Read the Chain

## Goal

In this lab you will analyze an Ethereum Sepolia transaction and understand gas, nonce, status, and transaction fee.

---

## Why This Lab Matters

Blockchain developers constantly inspect transactions to debug failed calls, estimate costs, and verify user actions.

---

## What You Will Learn

After completing this lab you will be able to:

- read Etherscan transaction pages
- explain gas limit and gas used
- find transaction status
- understand transaction fee
- record evidence for grading

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
| MetaMask | Send transaction |
| Sepolia Etherscan | Analyze transaction |
| submission.json | Submit fields |

---

## Key Terms

| Term | Meaning |
|---|---|
| `Gas limit` | Maximum gas allowed for transaction. |
| `Gas used` | Actual gas consumed. |
| `Nonce` | Transaction counter for account. |
| `Status` | Success or failure of transaction. |
| `Transaction fee` | Cost paid for execution. |

---

## Safety Notes

!!! warning
    Analyze a Sepolia transaction, not a Mainnet transaction.

---

## Step-by-Step Instructions

### Step 1 — Choose transaction
Use your Lab 1 transaction or send a new Sepolia transaction.
### Step 2 — Open Etherscan
Search by transaction hash.
### Step 3 — Record fields
Find From, To, Nonce, Status, Gas Limit, Gas Used, and Transaction Fee.
### Step 4 — Explain gas
Write a short explanation of gas limit vs gas used.
### Step 5 — Update JSON
Add transaction and gas data to submission.json.

---

## Expected Result

At the end of the lab you should understand the main fields of an Ethereum transaction and have them recorded in JSON.

---

## Submission

Add this fragment to `submission.json`:

```json
{
  "labs": {
    "lab4": {
      "tx_hash": "0x...",
      "gas_limit": 21000,
      "gas_used": 21000,
      "status": "success",
      "explanation": "Gas limit is ..."
    }
  }
}
```

---

## Automatic Validation

The checker will verify:

| Check | Requirement |
|---|---|
| Transaction | Submitted hash exists. |
| Status | Transaction is successful or failure is explained. |
| Gas fields | Values match RPC/explorer. |
| Explanation | Gas explanation is present. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Copying gas price instead of gas used | Use the correct Etherscan field. |
| Using Lab 1 URL instead of hash | Submit tx hash. |
| Wrong network | Use Sepolia. |
| Empty explanation | Add 3–5 sentences. |

---

## Self-Check Questions

1. What is gas used for?
2. What is the difference between gas limit and gas used?
3. What is nonce?
4. What does failed transaction mean?
