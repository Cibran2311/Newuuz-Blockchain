# Mission 3 — Mine Your First Block

## Goal

Build a Merkle tree and simulate Proof-of-Work by finding a nonce.

---

## Why This Lab Matters

Merkle trees summarize transactions, and Proof-of-Work shows why changing a block is expensive.

---

## What You Will Learn

After completing this lab you will be able to:

- construct Merkle root
- build simplified block header
- find nonce
- explain difficulty

---

## Required Reading

| Topic | Link |
|---|---|
| Merkle tree | https://en.wikipedia.org/wiki/Merkle_tree |
| Bitcoin developer guide | https://developer.bitcoin.org/devguide/block_chain.html |
| Proof of Work | https://en.wikipedia.org/wiki/Proof_of_work |

---

## Required Software

| Tool | Purpose |
|---|---|
| Python / Colab | Simulation |
| Notebook | Submit results |

---

## Key Terms

| Term | Meaning |
|---|---|
| `Merkle root` | Single hash summarizing transactions. |
| `Nonce` | Value changed during mining. |
| `Difficulty` | Rule the hash must satisfy. |
| `Block header` | Data hashed to identify block. |

---

## Safety Notes

!!! info
    This is a simplified mining simulation, not real cryptocurrency mining.

---

## Step-by-Step Instructions

### Step 1 — Prepare transactions

Create a list of transaction strings or numbers.

### Step 2 — Hash transactions

Hash every transaction.

### Step 3 — Build tree

Pair hashes until one root remains.

### Step 4 — Create header

Combine previous hash, Merkle root, and nonce.

### Step 5 — Mine

Change nonce until hash matches difficulty.

### Step 6 — Record

Save root, nonce, hash, and difficulty.

---

## Expected Result

A valid Merkle root and nonce producing a block hash matching difficulty.

---

## Submission

Add this fragment to `submission.json`:

```json
{"labs":{"lab3":{"transactions":["tx1","tx2","tx3"],"merkle_root":"...","nonce":12345,"block_hash":"...","difficulty":"000"}}}
```

---

## Automatic Validation

| Check | Requirement |
|---|---|
| Merkle root | Recalculates correctly. |
| Nonce | Produces submitted block hash. |
| Difficulty | Hash satisfies target. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Changed order | Keep order fixed. |
| Hash mismatch | Use consistent encoding. |
| Difficulty not met | Continue mining. |

---

## Self-Check Questions

1. What is Merkle root?
2. Why does one changed tx change the root?
3. What is nonce?
