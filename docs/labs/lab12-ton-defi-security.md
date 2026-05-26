# Lab 12 — TON DeFi and Smart Contract Security

## Goal

Perform TON DEX interaction or solve a TON smart contract security challenge.

## What You Will Learn

After completing this lab you will be able to:

- interact with blockchain infrastructure;
- use required tools and explorers;
- save transaction or computation evidence;
- fill `submission.json` correctly.

## Required Materials

Open these materials before starting:

- STON.fi docs: https://docs.ston.fi/
- TON docs: https://docs.ton.org/
- HackTON: https://www.hacktheton.com/en/level/introduction

## Step-by-Step Instructions

### Step 1 — Choose mode

Instructor assigns STON.fi swap or HackTON challenge.
### Step 2 — Prepare environment

Install Node.js and packages for SDK tasks or open HackTON.
### Step 3 — Complete action

Perform swap or solve challenge.
### Step 4 — Inspect trace

Open transaction in Tonviewer.
### Step 5 — Save evidence

Record trace link, script path, or proof.

## Submission

Add the result to `submission.json`.

```json
{
  "labs": {"lab12": {"mode": "stonfi_swap", "tx_link": "https://testnet.tonviewer.com/...", "script_file": "scripts/swap.ts"}}
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
