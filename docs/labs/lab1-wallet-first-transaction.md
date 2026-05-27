# Mission 1 — Enter the Blockchain

## Goal

Create your first blockchain wallet, connect it to Ethereum Sepolia, receive test ETH, send your first transaction, and inspect it in Etherscan.

---

## Why This Lab Matters

Every future blockchain task needs the same basic skill: wallet → transaction → explorer evidence. Without this, students cannot prove on-chain work.

---

## What You Will Learn

After completing this lab you will be able to:

- install and configure MetaMask
- create a wallet safely
- connect to Sepolia
- receive test ETH
- send a transaction
- read Etherscan evidence

---

## Required Reading

| Topic | Link |
|---|---|
| Ethereum accounts | https://ethereum.org/en/developers/docs/accounts/ |
| Ethereum transactions | https://ethereum.org/en/developers/docs/transactions/ |
| MetaMask | https://support.metamask.io/ |
| Sepolia Etherscan | https://sepolia.etherscan.io/ |

---

## Required Software

| Tool | Purpose |
|---|---|
| MetaMask | Ethereum wallet |
| Sepolia faucet | Test ETH |
| Etherscan | Transaction explorer |

---

## Key Terms

| Term | Meaning |
|---|---|
| `Wallet` | Application for managing accounts and signing transactions. |
| `Address` | Public identifier starting with 0x. |
| `Seed phrase` | Recovery phrase; never share it. |
| `Transaction hash` | Unique transaction identifier. |
| `Faucet` | Service that gives testnet tokens. |

---

## Safety Notes

!!! danger "Never share secrets"
    Never submit private keys, seed phrases, recovery phrases, or passwords.

!!! warning "Use testnets only"
    Use Sepolia for Ethereum labs unless the instructor explicitly says otherwise.

---

## Step-by-Step Instructions

### Step 1 — Install MetaMask

Install the extension from https://metamask.io/ and pin it in the browser.

### Step 2 — Create a wallet

Choose **Create a new wallet**, create a password, and save the Secret Recovery Phrase offline.

### Step 3 — Enable Sepolia

Open MetaMask network selector. If hidden, use **Settings → Advanced → Show test networks**, then select **Sepolia**.

### Step 4 — Get test ETH

Copy your wallet address and request ETH from a Sepolia faucet.

### Step 5 — Send transaction

Send `0.0001 ETH` to the instructor or assigned address.

### Step 6 — Open Etherscan

Open the tx in Sepolia Etherscan and record sender, receiver, value, status, gas used, and tx fee.

---

## Expected Result

A MetaMask wallet, Sepolia ETH, one successful transaction, tx hash, and Etherscan link.

---

## Submission

Add this fragment to `submission.json`:

```json
{"labs":{"lab1":{"network":"sepolia","wallet":"0x...","recipient":"0x...","amount_eth":"0.0001","tx_hash":"0x...","explorer_url":"https://sepolia.etherscan.io/tx/0x..."}}}
```

---

## Automatic Validation

| Check | Requirement |
|---|---|
| JSON | submission.json is valid. |
| Network | Transaction is on Sepolia. |
| Status | Transaction is successful. |
| Sender | Sender matches submitted wallet. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Used Mainnet | Switch to Sepolia. |
| Wrong tx hash | Copy from Etherscan transaction page. |
| Invalid JSON | Run python -m json.tool submission.json. |

---

## Self-Check Questions

1. What is a wallet address?
2. Why use Sepolia?
3. What proves the transaction happened?
