# Mission 2 — Hash Detective

## Goal

Explore SHA-256 interactively, implement a deliberately weak hash, find a collision, and explain why cryptographic hashes are designed differently from ordinary hash-table functions.

---

## Why This Lab Matters

Hashes connect transaction IDs, block headers, Merkle trees, signatures, and Proof of Work. This lab is the bridge between the basic hashing ideas from Mission 1 and the Merkle tree and mining work in Mission 3.

A hash used to choose a position in a hash table is not automatically a cryptographic hash. The output of a weak or non-cryptographic hash can be useful for a small programming exercise, but it must not protect blockchain data.

---

## What You Will Learn

After completing this lab you will be able to:

- explain what a hash function is;
- distinguish an ordinary or weak hash from a cryptographic hash;
- observe the avalanche effect in SHA-256;
- implement a deterministic weak hash and find a collision;
- reproduce SHA-256 in Python;
- explain why collision resistance matters in a blockchain.

---

## Required Reading

| Topic | Link |
|---|---|
| Hash functions, modulo hashing, collisions, and hash properties | [GeeksforGeeks — Hash Functions](https://www.geeksforgeeks.org/dsa/hash-functions-and-list-types-of-hash-functions/) |
| Interactive SHA-256 demonstration | [Anders Brownworth — Hash](https://andersbrownworth.com/blockchain/hash) |
| Python hashlib | [Python documentation](https://docs.python.org/3/library/hashlib.html) |
| SHA-256 overview | [Wikipedia — SHA-2](https://en.wikipedia.org/wiki/SHA-2) |
| Google Colab | [colab.research.google.com](https://colab.research.google.com/) |

For the GeeksforGeeks article, focus on the definition of a hash function, the modulo example, collisions, and the listed properties. The other hash-table methods are optional background.

---

## Required Software

| Tool | Purpose |
|---|---|
| Python / Colab | Run the experiment |
| Jupyter Notebook | Optional local notebook |
| GitHub repository | Store the script or notebook and evidence |

---

## Key Terms

| Term | Meaning |
|---|---|
| Hash function | Function that maps input data to an output value. |
| Hash table | Data structure that uses a hash to locate a value efficiently. |
| Cryptographic hash | Hash designed to provide properties such as pre-image and collision resistance. |
| Collision | Two different inputs with the same hash output. |
| SHA-256 | Cryptographic hash function that produces a 256-bit output. |
| Avalanche effect | A small input change causes a large-looking output change. |
| Collision resistance | Practical difficulty of finding two different inputs with the same hash. |

---

## Safety Notes

!!! info
    This lab uses a deliberately weak hash function for learning. It is not suitable for passwords, signatures, wallets, transaction integrity, or real blockchain systems.

!!! warning
    Do not confuse hashing with encryption. Hashing is designed as a one-way operation; encryption is reversible with a key.

---

## Step-by-Step Instructions

### Step 1 — Open a Python environment

Use Google Colab, Jupyter, or local Python. Create a notebook or script that can be committed to the course repository.

### Step 2 — Observe SHA-256 interactively

Open the [interactive SHA-256 demonstration](https://andersbrownworth.com/blockchain/hash).

1. Enter `Alice pays Bob 1`.
2. Record the displayed hash.
3. Change only the final character so the input becomes `Alice pays Bob 2`.
4. Record the new hash.
5. Describe how many hexadecimal characters appear to change. The exact count is not the important result; the important observation is that a one-character change affects the whole digest.

Repeat the same experiment in Python in Step 6. The interactive page is for intuition and must not be the only evidence.

### Step 3 — Read the hash-function distinction

From the required reading, write a short note that distinguishes:

- a small, fast hash used for a programming data structure;
- a cryptographic hash such as SHA-256.

Your note must mention output size, collisions, and why a predictable collision is dangerous when a hash protects blockchain data.

### Step 4 — Implement the canonical weak hash

Use this deterministic weak hash for the required collision evidence:

~~~python
def weak_hash(value: str) -> int:
    return sum(value.encode("utf-8")) % 100
~~~

It deliberately has only 100 possible outputs, so collisions are easy to find. Do not use Python's built-in hash() for the required result: its value can vary between runs and it is not SHA-256.

### Step 5 — Find a collision

Search different inputs until two of them have the same weak-hash result:

~~~python
seen = {}

for i in range(1000):
    value = f"student-input-{i}"
    result = weak_hash(value)

    if result in seen and seen[result] != value:
        print("input_1:", seen[result])
        print("input_2:", value)
        print("hash:", result)
        break

    seen[result] = value
~~~

Check that the two inputs are different and that recomputing weak_hash() gives the same value for both.

### Step 6 — Compare the same inputs with SHA-256

Use hashlib and compare the two inputs from Step 5:

~~~python
import hashlib

def sha256_hex(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()

print(sha256_hex("Alice pays Bob 1"))
print(sha256_hex("Alice pays Bob 2"))
~~~

Record the two full SHA-256 digests and explain why a collision in the deliberately weak hash does not demonstrate a SHA-256 collision. In this course, describe SHA-256 collisions as computationally infeasible to find, not as mathematically impossible.

### Step 7 — Save the evidence

Save a .py script or .ipynb notebook containing:

- the weak-hash function;
- the two different colliding inputs;
- the equal weak-hash result;
- the two SHA-256 avalanche-test inputs and full digests;
- a short explanation of the difference between the two hash types.

---

## Expected Result

At the end of the lab you should have:

1. two different inputs with the same result under weak_hash;
2. two SHA-256 digests for inputs that differ by one character;
3. a short explanation of collision resistance and the avalanche effect;
4. a committed script or notebook that reproduces the result.

---

## Submission

Commit the script or notebook to the course GitHub repository and put the evidence in the same file or in its README:

- file path of the script or notebook;
- input_1, input_2, hash_1, and hash_2 for the weak collision;
- the two SHA-256 digests from the one-character change;
- a short explanation of why the weak collision is easy to reproduce and why a SHA-256 collision is computationally infeasible.

Use the repository's current submission/checker process. Do not submit private keys, seed phrases, API keys, or real credentials.

---

## Automatic Validation

The checker will verify:

| Check | Requirement |
|---|---|
| Different inputs | input_1 and input_2 are not equal. |
| Weak collision | Recomputing weak_hash gives the same result for both inputs. |
| SHA-256 evidence | The submitted digests recompute from the stated strings. |
| Explanation | The student distinguishes weak hashing from cryptographic hashing and mentions collision resistance. |
| Reproducible code | The submitted notebook or script runs and contains the required functions. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Using identical inputs | Use two different strings. |
| Using Python's built-in hash() | Use the canonical sum of UTF-8 bytes modulo 100 function. |
| Calling the weak hash a SHA-256 collision | Label the algorithms separately. |
| Recording only a SHA-256 prefix | Record the full hexadecimal digest. |
| Claiming SHA-256 collisions are impossible | Say that finding one is computationally infeasible in practice. |
| Submitting only a screenshot | Submit runnable code and reproducible evidence. |

---

## Self-Check Questions

1. What is a hash collision?
2. Why is sum of UTF-8 bytes modulo 100 easy to collide?
3. Why is Python's built-in hash() unsuitable as the required evidence here?
4. What does the avalanche effect show?
5. Why are weak hash functions unsafe for blockchain integrity?
6. How will Mission 3 reuse SHA-256 without reusing the weak hash?
