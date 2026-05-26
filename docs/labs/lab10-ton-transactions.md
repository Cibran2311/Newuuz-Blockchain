# Lab 10 — TON Wallets and Transactions

## Goal

Create a TON testnet wallet, receive test TON, send a transaction, and inspect it in Tonviewer.

## What You Will Learn

After completing this lab you will be able to:

- interact with blockchain infrastructure;
- use required tools and explorers;
- save transaction or computation evidence;
- fill `submission.json` correctly.

## Required Materials

Open these materials before starting:

- Tonkeeper: https://tonkeeper.com/
- TON docs: https://docs.ton.org/
- Testnet Tonviewer: https://testnet.tonviewer.com/

## Step-by-Step Instructions

### Step 1 — Install wallet

Install Tonkeeper or supported TON wallet.
### Step 2 — Enable testnet

Enable testnet mode in wallet settings.
### Step 3 — Get test TON

Use faucet or bot specified by instructor.
### Step 4 — Send transaction

Send small amount to instructor or partner.
### Step 5 — Open Tonviewer

Find transaction in testnet Tonviewer.

## Submission

Add the result to `submission.json`.

```json
{
  "labs": {"lab10": {"ton_wallet": "kQ...", "tx_link": "https://testnet.tonviewer.com/...", "amount_ton": "0.01"}}
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
