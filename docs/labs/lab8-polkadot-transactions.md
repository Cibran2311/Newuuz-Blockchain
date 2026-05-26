# Lab 8 — Polkadot Transactions and Extrinsics

## Goal

Create a Polkadot wallet, obtain Westend tokens, send an extrinsic, and inspect it in Subscan.

## What You Will Learn

After completing this lab you will be able to:

- interact with blockchain infrastructure;
- use required tools and explorers;
- save transaction or computation evidence;
- fill `submission.json` correctly.

## Required Materials

Open these materials before starting:

- Polkadot.js Extension: https://polkadot.js.org/extension/
- Polkadot.js Apps: https://polkadot.js.org/apps/
- Westend Subscan: https://westend.subscan.io/

## Step-by-Step Instructions

### Step 1 — Install extension

Install Polkadot.js extension and create account.
### Step 2 — Get Westend tokens

Use faucet specified by instructor.
### Step 3 — Open Polkadot.js Apps

Connect account and select Westend.
### Step 4 — Send transaction

Transfer small amount to instructor or assigned account.
### Step 5 — Open Subscan

Find extrinsic by hash.

## Submission

Add the result to `submission.json`.

```json
{
  "labs": {"lab8": {"polkadot_wallet": "5...", "extrinsic_hash": "...", "explorer_url": "https://westend.subscan.io/extrinsic/..."}}
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
