# Mission 1 — Enter the Blockchain

## Goal

In this lab you will create your first blockchain wallet, connect it to Ethereum Sepolia, receive test ETH, send your first transaction, and inspect it using Etherscan.

---

## Why This Lab Matters

Almost every future task in the course requires a wallet address, a transaction hash, and the ability to prove that an action happened on-chain.

---

## What You Will Learn

After completing this lab you will be able to:

- install and configure MetaMask
- create a blockchain wallet
- explain address, private key, and seed phrase
- connect to Ethereum Sepolia
- receive test ETH from a faucet
- send a blockchain transaction
- find transaction evidence in Etherscan

---

## Required Reading

| Topic | Link |
|---|---|
| Ethereum accounts | https://ethereum.org/en/developers/docs/accounts/ |
| Ethereum transactions | https://ethereum.org/en/developers/docs/transactions/ |
| MetaMask support | https://support.metamask.io/ |
| Sepolia Etherscan | https://sepolia.etherscan.io/ |

---

## Required Software

| Tool | Purpose |
|---|---|
| Google Chrome / Firefox | Browser for MetaMask |
| MetaMask | Ethereum wallet |
| Sepolia faucet | Test ETH |
| Sepolia Etherscan | Transaction explorer |

---

## Key Terms

| Term | Meaning |
|---|---|
| `Wallet` | Application used to manage accounts and sign transactions. |
| `Address` | Public account identifier starting with 0x. |
| `Private key` | Secret value controlling the wallet. |
| `Seed phrase` | Recovery phrase for the wallet. |
| `Sepolia` | Ethereum test network. |
| `Faucet` | Service that gives testnet ETH. |
| `Transaction hash` | Unique transaction identifier. |

---

## Safety Notes

!!! danger "Never share your seed phrase"
    Do not send it to anyone. Do not upload it to GitHub.

!!! warning "Use Sepolia only"
    Do not use Ethereum Mainnet for this lab.

---

## Step-by-Step Instructions

### Step 1 — Install MetaMask
Open https://metamask.io/, install the extension, and pin it in your browser toolbar.
### Step 2 — Create a wallet
Open MetaMask, choose **Create a new wallet**, create a password, and safely store the Secret Recovery Phrase offline.
### Step 3 — Enable Sepolia
Open network selector. If Sepolia is hidden, enable **Settings → Advanced → Show test networks**, then select **Sepolia**.
### Step 4 — Receive test ETH
Copy your wallet address and request Sepolia ETH from a faucet.
### Step 5 — Send transaction
Send `0.0001 ETH` to the instructor wallet or assigned address.
### Step 6 — Open Etherscan
Open the transaction in https://sepolia.etherscan.io/ and record hash, sender, receiver, status, value, gas used, and fee.

---

## Expected Result

At the end of the lab you should have a MetaMask wallet, Sepolia ETH, one successful Sepolia transaction, a transaction hash, and an Etherscan link.

---

## Submission

In `submission.json`, fill `labs.lab1` with the Sepolia transaction hash, explorer link, recipient, and amount. Set its status to `submitted`. The sender must be an Ethereum address registered in Google Sheets.

---

## Automatic Validation

The checker will verify:

| Check | Requirement |
|---|---|
| Registry match | Sender must match the registered Ethereum address. |
| Network | Transaction must be on Sepolia. |
| Status | Transaction must be successful. |
| Sender | Transaction sender must match submitted wallet. |
| Amount | Transaction value must be correct or within accepted range. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Transaction sent on Mainnet | Switch to Sepolia and repeat. |
| Faucet does not send ETH | Try another faucet or wait. |
| Wrong recipient | Verify first and last characters. |
| Wallet not matched | Ask the instructor to confirm the registered address. |

---

## Self-Check Questions

1. What is the difference between wallet address and private key?
2. Why do we use Sepolia?
3. What is a transaction hash?
4. Why does a transaction require gas?
