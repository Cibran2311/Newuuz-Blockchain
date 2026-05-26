# Lab 11 — Jettons and TON NFTs

## Goal

Work with TON token architecture and understand how jettons differ from ERC20 tokens.

## What You Will Learn

After completing this lab you will be able to:

- interact with blockchain infrastructure;
- use required tools and explorers;
- save transaction or computation evidence;
- fill `submission.json` correctly.

## Required Materials

Open these materials before starting:

- TON docs: https://docs.ton.org/
- TON token contracts: https://github.com/ton-blockchain/token-contract
- Testnet Tonviewer: https://testnet.tonviewer.com/

## Step-by-Step Instructions

### Step 1 — Import jetton

Import or receive class test jetton.
### Step 2 — Send jetton

Transfer small amount to partner or instructor.
### Step 3 — Open trace

Open transaction in Tonviewer and inspect message chain.
### Step 4 — Find contracts

Locate Jetton Master, sender Jetton Wallet, recipient Jetton Wallet.
### Step 5 — Explain architecture

Explain per-holder jetton wallets.

## Submission

Add the result to `submission.json`.

```json
{
  "labs": {"lab11": {"jetton_master": "kQ...", "sender_jetton_wallet": "kQ...", "recipient_jetton_wallet": "kQ...", "tx_link": "https://testnet.tonviewer.com/..."}}
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
