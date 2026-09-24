# Mission 2 — Hash Detective

## Goal

In this lab you will implement a simplified hash function, test it on multiple inputs, and find a collision.

---

## Why This Lab Matters

Hash functions are used in transaction IDs, block headers, Merkle trees, signatures, and proof-of-work. Understanding weak hashes helps explain why blockchains need cryptographic hash functions.

---

## What You Will Learn

After completing this lab you will be able to:

- explain what a hash function is
- find collisions in a weak hash function
- compare weak hashes with SHA-256
- understand why collision resistance matters

---

## Required Reading

| Topic | Link |
|---|---|
| Python hashlib | https://docs.python.org/3/library/hashlib.html |
| SHA-256 overview | https://en.wikipedia.org/wiki/SHA-2 |
| Google Colab | https://colab.research.google.com/ |

---

## Required Software

| Tool | Purpose |
|---|---|
| Python / Colab | Run code |
| Jupyter Notebook | Optional local notebook |
| GitHub repository | Submit notebook or script |

---

## Key Terms

| Term | Meaning |
|---|---|
| `Hash function` | Function that maps input data to fixed-size output. |
| `Collision` | Two different inputs with the same hash output. |
| `SHA-256` | Cryptographic hash function used in many blockchain systems. |
| `Avalanche effect` | Small input change causes large output change. |

---

## Safety Notes

!!! info
    This lab uses a deliberately weak hash function for learning.

!!! warning
    Do not confuse hashing with encryption. Hashing is one-way, encryption is reversible with a key.

---

## Step-by-Step Instructions

### Step 1 — Open Python environment
Use Google Colab, Jupyter, or local Python.
### Step 2 — Implement weak hash
Create a simple function with a small output range, for example modulo 100 or modulo 256.
### Step 3 — Find collision
Run a loop over many inputs and find two different inputs with the same hash.
### Step 4 — Compare with SHA-256
Use `hashlib.sha256()` and explain why real SHA-256 collisions are infeasible.
### Step 5 — Save notebook
Save `.ipynb` or `.py` file in the repository.

---

## Expected Result

At the end of the lab you should have two different inputs that produce the same weak hash and a short explanation of collision resistance.

---

## Submission

In `submission.json`, fill `labs.lab2` with both different inputs, their equal weak-hash results, the notebook or script link, and your SHA-256 collision explanation. Set its status to `submitted`.

---

## Automatic Validation

The checker will verify:

| Check | Requirement |
|---|---|
| Different inputs | input_1 and input_2 must not be equal. |
| Collision | hash_1 and hash_2 must be equal. |
| Notebook | Submitted notebook or script must exist. |
| Explanation | Student explains why weak hash is unsafe. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Using identical inputs | Use two different inputs. |
| No collision found | Increase search range or reduce hash output size. |
| Notebook missing | Commit notebook to repository. |

---

## Self-Check Questions

1. What is a hash collision?
2. Why are weak hash functions unsafe?
3. Why is SHA-256 difficult to break?
4. Where are hashes used in blockchain?
