# Mission 3 — Mine Your First Block

## Goal

In this lab you will build a Merkle tree from transactions and simulate Proof-of-Work mining by finding a valid nonce.

---

## Why This Lab Matters

Merkle trees allow blockchains to summarize many transactions with one root hash. Mining demonstrates how Proof-of-Work links computation to block creation.

---

## What You Will Learn

After completing this lab you will be able to:

- hash transactions
- build a Merkle root
- construct a simplified block header
- find a nonce for a target difficulty
- explain why changing one transaction changes the block hash

---

## Required Reading

| Topic | Link |
|---|---|
| Merkle tree | https://en.wikipedia.org/wiki/Merkle_tree |
| Bitcoin block chain guide | https://developer.bitcoin.org/devguide/block_chain.html |
| Proof of Work | https://en.wikipedia.org/wiki/Proof_of_work |

---

## Required Software

| Tool | Purpose |
|---|---|
| Python / Colab | Run mining simulation |
| Notebook or script | Submit code |
| GitHub repository | Store results |

---

## Key Terms

| Term | Meaning |
|---|---|
| `Merkle root` | Single hash representing all transactions in a Merkle tree. |
| `Nonce` | Number changed repeatedly during mining. |
| `Difficulty` | Condition that a block hash must satisfy. |
| `Block header` | Data used to calculate block hash. |

---

## Safety Notes

!!! info
    This is a simplified mining simulation. You are not mining real cryptocurrency.

---

## Step-by-Step Instructions

### Step 1 — Prepare transactions
Create a small list of transaction strings or numbers.
### Step 2 — Hash transactions
Hash each transaction using SHA-256 or the lab hash function.
### Step 3 — Build Merkle tree
Pair hashes and hash pairs until one root remains.
### Step 4 — Create block header
Combine previous hash, Merkle root, timestamp/student ID, and nonce.
### Step 5 — Mine block
Change nonce until the block hash matches the difficulty rule.
### Step 6 — Save result
Record transactions, Merkle root, nonce, difficulty, and block hash.

---

## Expected Result

At the end of the lab you should have a valid Merkle root and a nonce that produces a block hash satisfying the selected difficulty.

---

## Submission

Add this fragment to `submission.json`:

```json
{
  "labs": {
    "lab3": {
      "transactions": ["tx1", "tx2", "tx3"],
      "merkle_root": "...",
      "nonce": 12345,
      "block_hash": "...",
      "difficulty": "000"
    }
  }
}
```

---

## Automatic Validation

The checker will verify:

| Check | Requirement |
|---|---|
| Merkle root | Root recalculates from submitted transactions. |
| Nonce | Nonce produces submitted block hash. |
| Difficulty | Block hash satisfies difficulty. |
| Code | Notebook or script exists. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Changing transaction order | Keep order fixed. |
| Using inconsistent encoding | Encode strings consistently. |
| Hash does not satisfy difficulty | Continue mining. |
| Forgetting nonce | Record final nonce. |

---

## Self-Check Questions

1. What is a Merkle root?
2. Why does changing one transaction change the root?
3. What is nonce?
4. What does difficulty mean?
