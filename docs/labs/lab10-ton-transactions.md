# Mission 10 — Enter TON

## Goal

In this lab you will create a TON testnet wallet, receive test TON, send a transaction, and inspect it in Tonviewer.

---

## Why This Lab Matters

TON differs from Ethereum. In Ethereum, users usually interact through externally owned accounts and EVM transactions. In TON, wallets are smart contracts, and execution is based on asynchronous messages.

Before working with jettons, TON NFTs, or STON.fi, you need to understand basic TON wallet and transaction flow.

---

## What You Will Learn

After completing this lab you will be able to:

- install and configure Tonkeeper;
- enable TON testnet;
- receive test TON;
- send TON transactions;
- inspect transactions in Tonviewer;
- understand basic TON address formats;
- compare TON transaction flow with Ethereum.

---

## Required Reading

| Topic | Link |
|---|---|
| TON documentation | https://docs.ton.org/ |
| Tonkeeper | https://tonkeeper.com/ |
| Tonviewer | https://tonviewer.com/ |
| Testnet Tonviewer | https://testnet.tonviewer.com/ |

---

## Required Software

| Tool | Purpose |
|---|---|
| Tonkeeper | TON wallet |
| TON testnet faucet | Receive test TON |
| Testnet Tonviewer | Inspect TON transactions |

---

## Key Terms

| Term | Meaning |
|---|---|
| `TON` | The Open Network blockchain. |
| `Wallet contract` | Smart contract representing a user wallet in TON. |
| `Message` | Main unit of communication between TON accounts/contracts. |
| `Testnet` | TON testing network. |
| `Tonviewer` | TON blockchain explorer. |
| `Bounceable address` | TON address format with bounce behavior. |
| `Non-bounceable address` | Safer format for first transfer to wallet. |

---

## Safety Notes

!!! warning "Use TON Testnet"
    Do not use mainnet TON for this lab.

!!! danger "Never share seed phrase"
    TON wallets also have recovery phrases. Do not upload them anywhere.

!!! info
    TON transactions may show several internal messages. This is normal.

---

## Step-by-Step Instructions

### Step 1 — Install Tonkeeper

Open https://tonkeeper.com/ and install Tonkeeper.

### Step 2 — Create Testnet Wallet

Create a wallet, save the recovery phrase securely, enable **Testnet** or developer mode, and switch to testnet wallet.

### Step 3 — Receive Test TON

Use the faucet or bot provided by instructor. Record your TON testnet wallet address.

### Step 4 — Send TON Transaction

Send `0.01 TON` to instructor wallet or assigned address.

### Step 5 — Open Tonviewer

Open https://testnet.tonviewer.com/ and search for your wallet or transaction. Record transaction link, sender, recipient, amount, status/time, and message trace if visible.

---

## Expected Result

At the end of this lab you should have TON testnet wallet, test TON balance, successful TON testnet transaction, and Tonviewer transaction link.

---

## Submission

In `submission.json`, fill `labs.lab10` with the TON Testnet transaction hash and explorer link, recipient, and amount. Set its status to `submitted`. The sender must match the TON address registered in Google Sheets.

---

## Automatic Validation

| Check | Requirement |
|---|---|
| Network | Transaction must be on TON testnet. |
| Transaction | Transaction link must exist. |
| Sender | Sender must match submitted wallet. |
| Amount | Amount must match required value or accepted range. |
| Status | Transaction must be successful / visible in explorer. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Using mainnet | Enable testnet mode. |
| Submitting wallet page instead of transaction | Submit transaction link if possible. |
| Not enough test TON | Use faucet or ask instructor. |
| Wrong recipient | Verify address carefully. |
| Confusing TON and Jetton transfer | This lab is native TON transfer only. |

---

## Self-Check Questions

1. How is a TON wallet different from an Ethereum EOA?
2. What is a TON message?
3. What is Tonviewer used for?
4. Why do we use TON testnet?
5. What evidence proves that your TON transaction happened?
