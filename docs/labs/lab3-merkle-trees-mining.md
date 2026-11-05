# Mission 3 — Mine Your First Block

## Goal

Build a deterministic Merkle tree from transactions and simulate Proof of Work by finding a nonce that satisfies a block-hash target.

---

## Why This Lab Matters

A blockchain combines several ideas rather than using a hash in isolation:

1. transactions are hashed;
2. transaction hashes are compressed into a Merkle root;
3. the root is placed in a block header;
4. a nonce is searched until the header hash satisfies a difficulty rule.

This lab turns the collision and SHA-256 observations from Mission 2 into a reproducible block-building experiment.

---

## What You Will Learn

After completing this lab you will be able to:

- hash transaction strings with a fixed encoding;
- build a Merkle root from left to right;
- handle an odd number of tree nodes deterministically;
- construct a canonical simplified block header;
- find a nonce for a fixed Proof-of-Work target;
- show that changing one transaction changes the Merkle root and block hash.

---

## Required Reading

| Topic | Link |
|---|---|
| Merkle tree | [Wikipedia — Merkle tree](https://en.wikipedia.org/wiki/Merkle_tree) |
| Bitcoin block chain | [Bitcoin Developer Guide](https://developer.bitcoin.org/devguide/block_chain.html) |
| Proof of Work | [Wikipedia — Proof of work](https://en.wikipedia.org/wiki/Proof_of_work) |

---

## Required Software

| Tool | Purpose |
|---|---|
| Python / Colab | Run the Merkle-tree and mining simulation |
| Notebook or script | Submit reproducible code and results |
| GitHub repository | Store the code and evidence |

---

## Key Terms

| Term | Meaning |
|---|---|
| Leaf hash | Hash of one transaction before it enters the tree. |
| Merkle root | One hash representing all transactions in a Merkle tree. |
| Block header | Data that is hashed to identify a block candidate. |
| Nonce | Number changed repeatedly during mining. |
| Difficulty | Condition that a block hash must satisfy. |
| Proof of Work | Demonstration that computational work was performed to find a valid nonce. |

---

## Safety Notes

!!! info
    This is a local mining simulation. It does not mine real cryptocurrency and does not connect to a blockchain network.

!!! warning
    Do not use real wallets, private keys, seed phrases, API keys, or real credentials in the notebook.

---

## Canonical Rules for This Lab

Use these rules exactly so that another person or the checker can reproduce your result:

- Encode every transaction as UTF-8.
- A leaf is SHA256(transaction_bytes).
- Pair nodes from left to right.
- A parent is SHA256(left_bytes + right_bytes).
- If a level has an odd number of nodes, duplicate the final node before pairing.
- Keep the transaction order unchanged.
- Keep hashes as raw bytes during tree construction. Convert to hexadecimal only for display and submission.
- Use the exact header format below, including the pipe separators.
- Use difficulty 3, meaning the displayed block hash must start with three hexadecimal zeroes.

Do not hash the textual hexadecimal representation of a child hash. That changes the algorithm.

---

## Step-by-Step Instructions

### Step 1 — Prepare transactions

Start with a small ordered list. For example:

~~~python
transactions = [
    "Alice pays Bob 1",
    "Bob pays Carol 2",
    "Carol pays Dave 3",
    "Dave pays Eve 4",
]
~~~

You may use your own transaction strings, but keep the exact submitted list and order.

### Step 2 — Build the Merkle root

Implement the canonical tree:

~~~python
import hashlib

def hash_leaf(transaction: str) -> bytes:
    return hashlib.sha256(transaction.encode("utf-8")).digest()

def merkle_root(transactions: list[str]) -> str:
    if not transactions:
        raise ValueError("transactions must not be empty")

    level = [hash_leaf(transaction) for transaction in transactions]

    while len(level) > 1:
        if len(level) % 2 == 1:
            level.append(level[-1])

        level = [
            hashlib.sha256(level[index] + level[index + 1]).digest()
            for index in range(0, len(level), 2)
        ]

    return level[0].hex()
~~~

Record the root for the original transaction list.

### Step 3 — Demonstrate the one-transaction change

Change only one transaction, for example from Alice pays Bob 1 to Alice pays Bob 9, and calculate a second root.

Record both roots and explain that a small input change produces a different Merkle root. This is the blockchain-level consequence of the hash behavior observed in Mission 2.

### Step 4 — Create a deterministic block header

Use a fixed previous hash and an explicit timestamp string:

~~~python
previous_hash = "0" * 64
timestamp = "2026-01-01T00:00:00Z"
student_id = "replace-with-your-id"
difficulty = 3
~~~

Keep timestamp and student_id in the submitted evidence. The student_id is only a label for this local exercise; do not put personal credentials in the header.

Build the header with this exact function:

~~~python
def block_hash(
    previous_hash: str,
    root: str,
    timestamp: str,
    student_id: str,
    nonce: int,
) -> str:
    header = f"{previous_hash}|{root}|{timestamp}|{student_id}|{nonce}"
    return hashlib.sha256(header.encode("utf-8")).hexdigest()
~~~

### Step 5 — Mine the block

Search nonces from zero:

~~~python
nonce = 0

while True:
    digest = block_hash(
        previous_hash,
        merkle_root_value,
        timestamp,
        student_id,
        nonce,
    )

    if digest.startswith("0" * difficulty):
        break

    nonce += 1

print("nonce:", nonce)
print("block_hash:", digest)
~~~

A difficulty of three hexadecimal zeroes is intentionally small so that the lab finishes quickly on an ordinary computer. It is a teaching target, not a real network difficulty.

### Step 6 — Save the result

Save the following values in the notebook or README:

- ordered transactions;
- original Merkle root;
- modified transaction and modified Merkle root;
- previous_hash;
- timestamp;
- student_id label;
- difficulty;
- discovered nonce;
- final block hash.

---

## Expected Result

At the end of the lab you should have:

1. a Merkle root that can be recalculated from the submitted transactions;
2. a different root after changing one transaction;
3. a nonce found by searching from zero;
4. a block hash that starts with 000;
5. code that reproduces the complete result using the canonical rules.

---

## Submission

Commit the notebook or script to the course GitHub repository and include the reproducible evidence in the same file or its README.

The submission must contain:

- the exact ordered transaction list;
- both Merkle roots;
- the exact header fields;
- the difficulty;
- the discovered nonce;
- the resulting block hash;
- a short explanation of why changing one transaction changes the root.

Use the repository's current submission/checker process. Do not submit private keys, seed phrases, API keys, or real credentials.

---

## Automatic Validation

The checker will verify:

| Check | Requirement |
|---|---|
| Merkle root | The original root recalculates with the canonical byte-level algorithm. |
| Mutation evidence | Changing the stated transaction produces the submitted second root. |
| Header | The submitted fields use the exact pipe-separated UTF-8 header format. |
| Nonce | The nonce reproduces the submitted block hash. |
| Difficulty | The block hash starts with three hexadecimal zeroes. |
| Reproducible code | The notebook or script contains the required functions and runs successfully. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Hashing hexadecimal text instead of bytes | Keep child hashes as bytes until the final hex conversion. |
| Sorting transactions | Keep the submitted order. |
| Forgetting odd-node duplication | Duplicate the last node at every odd level. |
| Using the weak hash from Mission 2 | Use SHA-256 for every leaf, parent, and block header. |
| Changing the header delimiter | Use the exact pipe-separated format. |
| Omitting timestamp or student_id | Save every header field with the result. |
| Searching from a random nonce | Start at zero so the result is reproducible. |
| Using a real mining difficulty | Keep difficulty at three leading hexadecimal zeroes. |

---

## Self-Check Questions

1. What does the Merkle root commit to?
2. Why does changing one transaction change the root?
3. Why must the transaction order be fixed?
4. Why does this lab keep child hashes as bytes instead of hashing their hexadecimal text?
5. What is a nonce?
6. What does the difficulty condition hash.startswith("000") mean?
