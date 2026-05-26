# Lab 6 — NFTs and Smart Contract Interaction

## Goal

Mint and transfer NFTs and interact with a special smart contract.

## What You Will Learn

After completing this lab you will be able to:

- interact with blockchain infrastructure;
- use required tools and explorers;
- save transaction or computation evidence;
- fill `submission.json` correctly.

## Required Materials

Open these materials before starting:

- ERC721: https://eips.ethereum.org/EIPS/eip-721
- OpenZeppelin Wizard: https://wizard.openzeppelin.com/
- Remix: https://remix.ethereum.org/

## Step-by-Step Instructions

### Step 1 — Get professor NFT

Receive or buy professor NFT.
### Step 2 — Return NFT

Transfer or sell it back if required.
### Step 3 — Mint personal NFT

Deploy ERC721 or use class NFT minter.
### Step 4 — Approve contract

Approve special contract if required.
### Step 5 — Transfer NFT

Send personal NFT to special contract.

## Submission

Add the result to `submission.json`.

```json
{
  "labs": {"lab6": {"personal_nft_contract": "0x...", "personal_token_id": "1", "special_contract": "0x...", "tx_hashes": ["0x..."]}}
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
