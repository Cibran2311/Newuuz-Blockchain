# Lab 3 — Merkle Trees and Block Mining

## Goal

Construct a Merkle tree and simulate Proof-of-Work mining.

## What You Will Learn

After completing this lab you will be able to:

- interact with blockchain infrastructure;
- use required tools and explorers;
- save transaction or computation evidence;
- fill `submission.json` correctly.

## Required Materials

Open these materials before starting:

- Merkle tree: https://en.wikipedia.org/wiki/Merkle_tree
- Bitcoin block chain guide: https://developer.bitcoin.org/devguide/block_chain.html

## Step-by-Step Instructions

### Step 1 — Prepare transactions

Use a small transaction list.
### Step 2 — Hash transactions

Hash every transaction.
### Step 3 — Build Merkle tree

Pair hashes until one root remains.
### Step 4 — Mine block

Change nonce until hash satisfies difficulty.

## Submission

Add the result to `submission.json`.

```json
{
  "labs": {"lab3": {"transactions": [165,124,549], "merkle_root": "...", "nonce": 12345, "block_hash": "..."}}
}
```

## Automatic Validation

The checker verifies:

- submitted evidence exists;
- network is correct;
- wallet belongs to the student;
- transaction or computation result is valid.

## Common Mistakes

- using the wrong network;
- submitting another wallet's transaction;
- breaking JSON syntax;
- forgetting explorer links;
- submitting private keys or seed phrases.
