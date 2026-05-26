# Lab 1 — Creating a Wallet and Sending Your First Transaction

## Goal

Install MetaMask, create a wallet, connect to Ethereum Sepolia, receive test ETH, send your first transaction, and inspect it in Etherscan.

## What You Will Learn

After completing this lab you will be able to:

- interact with blockchain infrastructure;
- use required tools and explorers;
- save transaction or computation evidence;
- fill `submission.json` correctly.

## Required Materials

Open these materials before starting:

- MetaMask: https://metamask.io/
- Sepolia Etherscan: https://sepolia.etherscan.io/
- Google Cloud Sepolia Faucet: https://cloud.google.com/application/web3/faucet/ethereum/sepolia
- Ethereum accounts: https://ethereum.org/en/developers/docs/accounts/

## Step-by-Step Instructions

### Step 1 — Install MetaMask

Open the official MetaMask website, install the browser extension, and pin it in the toolbar.
### Step 2 — Create wallet

Choose **Create a new wallet**, create a password, and save the Secret Recovery Phrase offline. Never upload it.
### Step 3 — Enable Sepolia

Open network selector. If Sepolia is hidden, use **Settings → Advanced → Show test networks** and select Sepolia.
### Step 4 — Receive test ETH

Copy your address and request Sepolia ETH from a faucet.
### Step 5 — Send transaction

Send `0.0001 ETH` to the instructor or assigned address.
### Step 6 — Analyze in Etherscan

Open Sepolia Etherscan, search transaction hash, and record status, From, To, gas used, and fee.

## Submission

Add the result to `submission.json`.

```json
{
  "labs": {"lab1": {"network": "sepolia", "wallet": "0x...", "tx_hash": "0x...", "explorer_url": "https://sepolia.etherscan.io/tx/0x..."}}
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
