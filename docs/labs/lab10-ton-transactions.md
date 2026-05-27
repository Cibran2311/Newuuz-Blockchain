# Mission 10 — Enter TON

## Goal

Create a TON testnet wallet, receive test TON, send a transaction, and inspect it in Tonviewer.

---

## Why This Lab Matters

TON uses wallet contracts and asynchronous messages, so its transaction model differs from Ethereum and Polkadot.

---

## What You Will Learn

After completing this lab you will be able to:

- create TON testnet wallet
- send TON transaction
- use Tonviewer
- understand TON address formats
- compare TON and Ethereum

---

## Required Reading

| Topic | Link |
|---|---|
| TON docs | https://docs.ton.org/ |
| Tonkeeper | https://tonkeeper.com/ |
| Testnet Tonviewer | https://testnet.tonviewer.com/ |

---

## Required Software

| Tool | Purpose |
|---|---|
| Tonkeeper | Wallet |
| Testnet faucet | Test TON |
| Tonviewer | Explorer |

---

## Key Terms

| Term | Meaning |
|---|---|
| `TON wallet` | Wallet contract controlled by user. |
| `Message` | TON communication unit. |
| `Trace` | Message chain in explorer. |
| `Testnet` | Testing network. |

---

## Safety Notes

!!! warning "Use course test environments"
    Do not use real funds or mainnet assets. Save transaction hashes immediately.

---

## Step-by-Step Instructions

### Step 1 — Install wallet

Install Tonkeeper or compatible wallet.

### Step 2 — Enable testnet

Turn on testnet in settings.

### Step 3 — Get test TON

Use faucet/instructor.

### Step 4 — Send transaction

Send small amount to assigned wallet.

### Step 5 — Open Tonviewer

Find transaction on testnet.

### Step 6 — Submit link

Record wallet and tx link.

---

## Expected Result

TON testnet wallet and one Tonviewer transaction link.

---

## Submission

Add this fragment to `submission.json`:

```json
{"labs":{"lab10":{"network":"ton_testnet","ton_wallet":"kQ...","tx_link":"https://testnet.tonviewer.com/...","amount_ton":"0.01"}}}
```

---

## Automatic Validation

| Check | Requirement |
|---|---|
| Transaction | Exists. |
| Network | Testnet. |
| Wallet | Sender matches. |
| Amount | Valid. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Mainnet | Enable testnet. |
| Wallet page link | Submit tx link. |
| Wrong address | Copy carefully. |

---

## Self-Check Questions

1. What is TON wallet contract?
2. What is message?
3. How prove TON tx?
