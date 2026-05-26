# Lab 5 — ERC20 Tokens and Batch Transfers

## Goal

Work with ERC20 tokens and perform batch transfers using Disperse.

## What You Will Learn

After completing this lab you will be able to:

- interact with blockchain infrastructure;
- use required tools and explorers;
- save transaction or computation evidence;
- fill `submission.json` correctly.

## Required Materials

Open these materials before starting:

- OpenZeppelin Wizard: https://wizard.openzeppelin.com/
- Remix: https://remix.ethereum.org/
- ERC20: https://eips.ethereum.org/EIPS/eip-20
- Disperse: https://disperse.app/

## Step-by-Step Instructions

### Step 1 — Open token contract

Use class ERC20 token or deploy your own.
### Step 2 — Check metadata

Read name, symbol, decimals, totalSupply.
### Step 3 — Transfer tokens

Send tokens to at least three addresses.
### Step 4 — Use Disperse

Connect MetaMask on Sepolia and send batch transfer.

## Submission

Add the result to `submission.json`.

```json
{
  "labs": {"lab5": {"token_contract": "0x...", "transfer_txs": ["0x..."], "disperse_tx": "0x..."}}
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
