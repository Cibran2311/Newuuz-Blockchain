# Lab 4 — Ethereum Transactions and Gas

## Goal

Analyze Ethereum transaction structure and gas usage in Etherscan.

## What You Will Learn

After completing this lab you will be able to:

- interact with blockchain infrastructure;
- use required tools and explorers;
- save transaction or computation evidence;
- fill `submission.json` correctly.

## Required Materials

Open these materials before starting:

- Ethereum gas docs: https://ethereum.org/en/developers/docs/gas/
- Sepolia Etherscan: https://sepolia.etherscan.io/

## Step-by-Step Instructions

### Step 1 — Choose transaction

Use your Lab 1 transaction or send a new one.
### Step 2 — Open Etherscan

Find the transaction by hash.
### Step 3 — Record fields

Record From, To, Value, Nonce, Gas Limit, Gas Used, Fee, Status.
### Step 4 — Explain gas

Explain gas limit vs gas used.

## Submission

Add the result to `submission.json`.

```json
{
  "labs": {"lab4": {"tx_hash": "0x...", "gas_limit": 21000, "gas_used": 21000, "status": "success"}}
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
