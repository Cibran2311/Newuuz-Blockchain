# Lab 7 — Automated Market Makers and DEX Arbitrage

## Goal

Compare two AMM pools and use price differences for arbitrage.

## What You Will Learn

After completing this lab you will be able to:

- interact with blockchain infrastructure;
- use required tools and explorers;
- save transaction or computation evidence;
- fill `submission.json` correctly.

## Required Materials

Open these materials before starting:

- Uniswap developers: https://developers.uniswap.org/
- Uniswap V2: https://docs.uniswap.org/contracts/v2/concepts/protocol-overview/how-uniswap-works

## Step-by-Step Instructions

### Step 1 — Receive test tokens

Receive TEST and USDC from class faucet.
### Step 2 — Inspect DEX Alpha

Read reserves and calculate price.
### Step 3 — Inspect DEX Beta

Read reserves and calculate price.
### Step 4 — Choose strategy

Buy on cheaper pool and sell on expensive pool.
### Step 5 — Execute swaps

Submit swaps and save hashes.
### Step 6 — Calculate final value

Convert final balances to USDC equivalent.

## Submission

Add the result to `submission.json`.

```json
{
  "labs": {"lab7": {"dex_alpha": "0x...", "dex_beta": "0x...", "swap_txs": ["0x..."], "final_usdc_value": "0"}}
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
