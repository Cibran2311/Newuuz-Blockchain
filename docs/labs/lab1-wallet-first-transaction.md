# Mission 1 — Enter the Blockchain

## Goal

In this lab you will create your first blockchain wallet, connect it to the Ethereum Sepolia testnet, receive test ETH, send your first transaction, and inspect it using Etherscan.

This lab is the entry point for the entire course. Almost every future task will require a wallet address, a transaction hash, and the ability to prove that an action happened on-chain.

## Why This Lab Matters

Blockchain applications do not use traditional username/password accounts. Users control accounts with cryptographic keys and sign transactions using wallets.

Real blockchain developers use these skills when they:

- test smart contracts;
- debug failed transactions;
- inspect gas usage;
- prove that a transaction happened;
- verify token and NFT transfers.

## What You Will Learn

After completing this lab you will be able to:

- install and configure MetaMask;
- create a blockchain wallet;
- explain the difference between an address, private key, and seed phrase;
- connect to Ethereum Sepolia;
- receive Sepolia ETH from a faucet;
- send a blockchain transaction;
- find transaction evidence in Sepolia Etherscan;
- prepare data for automatic grading.

## Required Reading

| Topic | Link |
|---|---|
| Ethereum accounts | https://ethereum.org/en/developers/docs/accounts/ |
| Ethereum transactions | https://ethereum.org/en/developers/docs/transactions/ |
| MetaMask support | https://support.metamask.io/ |
| Sepolia Etherscan | https://sepolia.etherscan.io/ |

## Required Software

| Tool | Purpose | Link |
|---|---|---|
| Google Chrome / Firefox | Browser for MetaMask | https://www.google.com/chrome/ |
| MetaMask | Ethereum wallet | https://metamask.io/ |
| Sepolia Etherscan | Blockchain explorer | https://sepolia.etherscan.io/ |

## Key Terms

| Term | Meaning |
|---|---|
| Wallet | Application used to manage blockchain accounts and sign transactions. |
| Address | Public identifier of your blockchain account. Ethereum addresses start with `0x`. |
| Private key | Secret value that controls the wallet. Never share it. |
| Seed phrase | Recovery phrase used to restore a wallet. Never submit it anywhere. |
| Testnet | Blockchain network for testing. Testnet tokens have no real monetary value. |
| Sepolia | Ethereum testnet used in this course. |
| Faucet | Website or service that gives free testnet tokens. |
| Transaction hash | Unique identifier of a blockchain transaction. |
| Etherscan | Blockchain explorer for Ethereum networks. |

## Safety Notes

!!! danger "Never share your seed phrase"
    Your seed phrase gives full control over your wallet. Do not send it to the instructor. Do not upload it to GitHub.

!!! warning "Use Sepolia only"
    This lab must be completed on Ethereum Sepolia. Do not use Ethereum Mainnet.

## Step-by-Step Instructions

### Step 1 — Install MetaMask

1. Open the official MetaMask website: https://metamask.io/
2. Click **Download**.
3. Select your browser.
4. Install the browser extension.
5. Pin MetaMask in the browser toolbar.

Expected result: you should see the MetaMask fox icon in your browser.

### Step 2 — Create a New Wallet

1. Open MetaMask.
2. Click **Get Started**.
3. Select **Create a new wallet**.
4. Create a local password.
5. MetaMask will show your **Secret Recovery Phrase**.
6. Write the recovery phrase down and store it safely.
7. Confirm the phrase in MetaMask.

Expected result:

```text
Account 1
0x1234...abcd
```

Copy your wallet address. You will need it for `submission.json`.

### Step 3 — Enable Sepolia Test Network

1. Open MetaMask.
2. Click the network selector at the top.
3. If Sepolia is not visible, open:

```text
Settings → Advanced → Show test networks
```

4. Enable **Show test networks**.
5. Return to the network selector.
6. Select **Sepolia**.

Expected result: the active network in MetaMask should be `Sepolia`.

### Step 4 — Get Sepolia ETH

1. Copy your wallet address from MetaMask.
2. Open one faucet:

```text
https://cloud.google.com/application/web3/faucet/ethereum/sepolia
https://www.alchemy.com/faucets/ethereum-sepolia
https://faucet.quicknode.com/ethereum/sepolia
```

3. Paste your wallet address.
4. Request Sepolia ETH.
5. Wait until your balance appears in MetaMask.

Expected result: your balance should be greater than zero.

### Step 5 — Send Your First Transaction

Use the instructor wallet or the address assigned during class.

| Field | Value |
|---|---|
| Network | Sepolia |
| Amount | `0.0001 ETH` |
| Recipient | instructor wallet / assigned address |

Steps:

1. Open MetaMask.
2. Check that the selected network is **Sepolia**.
3. Click **Send**.
4. Paste the recipient address.
5. Enter `0.0001 ETH`.
6. Click **Next**.
7. Review the transaction.
8. Click **Confirm**.
9. Wait until the transaction is confirmed.

### Step 6 — Open the Transaction in Etherscan

1. Open MetaMask activity history.
2. Click your transaction.
3. Click **View on block explorer**.

Or open Sepolia Etherscan manually: https://sepolia.etherscan.io/

Find and record:

- transaction hash;
- status;
- block number;
- sender address;
- receiver address;
- value;
- gas used;
- transaction fee.

Expected status:

```text
Success
```

## Expected Result

At the end of this lab you should have:

- a MetaMask wallet;
- Sepolia test ETH;
- one successful Sepolia transaction;
- transaction hash;
- Sepolia Etherscan link.

## Submission

Add this fragment to `submission.json`:

```json
{
  "labs": {
    "lab1": {
      "network": "sepolia",
      "wallet": "0xYourWalletAddress",
      "recipient": "0xRecipientAddress",
      "amount_eth": "0.0001",
      "tx_hash": "0xTransactionHash",
      "explorer_url": "https://sepolia.etherscan.io/tx/0xTransactionHash"
    }
  }
}
```

## Automatic Validation

| Check | Requirement |
|---|---|
| JSON validity | `submission.json` must be valid JSON. |
| Network | Transaction must be on Sepolia. |
| Transaction existence | `tx_hash` must exist. |
| Status | Transaction must be successful. |
| Sender | Transaction sender must match submitted wallet. |
| Amount | Transaction value must match the required amount or accepted range. |

## Common Mistakes

| Mistake | Fix |
|---|---|
| Transaction sent on Ethereum Mainnet | Switch to Sepolia and repeat the transaction. |
| Faucet does not send ETH | Try another faucet or wait for rate limit reset. |
| Wrong recipient address | Copy the address again and verify first/last characters. |
| Submitted transaction from another wallet | Use your own wallet only. |
| Invalid JSON | Validate the file before pushing. |

## Self-Check Questions

1. What is the difference between a wallet address and a private key?
2. Why do we use Sepolia instead of Ethereum Mainnet?
3. What is a transaction hash?
4. What does transaction status `Success` mean?
5. Why does a transaction require gas?
