# Mission 2 — Hash Detective

## Goal

Implement a weak hash function, find a collision, and compare it with SHA-256.

---

## Why This Lab Matters

Blockchains depend on hashes for transaction IDs, Merkle trees, block headers, and mining. Weak hashes show why cryptographic hashes are necessary.

---

## What You Will Learn

After completing this lab you will be able to:

- explain hash functions
- find a collision in a weak hash
- compare weak hash with SHA-256
- explain collision resistance

---

## Required Reading

| Topic | Link |
|---|---|
| Python hashlib | https://docs.python.org/3/library/hashlib.html |
| Google Colab | https://colab.research.google.com/ |
| SHA-2 | https://en.wikipedia.org/wiki/SHA-2 |

---

## Required Software

| Tool | Purpose |
|---|---|
| Python / Colab | Run code |
| Notebook | Submit work |

---

## Key Terms

| Term | Meaning |
|---|---|
| `Hash` | Fixed-size output from input data. |
| `Collision` | Two different inputs with the same hash. |
| `SHA-256` | Cryptographic hash function. |
| `Avalanche effect` | Small input change causes large output change. |

---

## Safety Notes

!!! info
    The lab uses a deliberately weak hash function. This is for learning only.

---

## Step-by-Step Instructions

### Step 1 — Open Python

Use Colab, Jupyter, or local Python.

### Step 2 — Write weak hash

Create a function with a small output range, for example modulo 100.

### Step 3 — Search collision

Loop over many inputs and store seen outputs.

### Step 4 — Compare SHA-256

Use hashlib.sha256 and explain why collision search is infeasible.

### Step 5 — Save notebook

Commit `.ipynb` or `.py` file.

---

## Expected Result

Two different inputs with the same weak hash and explanation of why SHA-256 is different.

---

## Submission

Add this fragment to `submission.json`:

```json
{"labs":{"lab2":{"input_1":"123","input_2":"321","hash_1":"42","hash_2":"42","notebook_path":"notebooks/lab2.ipynb"}}}
```

---

## Automatic Validation

| Check | Requirement |
|---|---|
| Inputs | input_1 != input_2. |
| Collision | hash_1 == hash_2. |
| File | Notebook/script exists. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Same inputs | Use two different inputs. |
| No file | Commit notebook. |
| Claiming SHA-256 collision | Do not claim real SHA-256 collision. |

---

## Self-Check Questions

1. What is a collision?
2. Why is collision resistance important?
3. Where are hashes used in blockchain?
