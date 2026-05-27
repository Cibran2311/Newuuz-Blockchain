# Mission 5 — Launch Your Token

## Goal

Work with ERC20 tokens, perform transfers, inspect Transfer events, and use Disperse for batch distribution.

---

## Why This Lab Matters

ERC20 powers stablecoins, governance tokens, rewards, and DeFi. Batch transfer is a real operational task.

---

## What You Will Learn

After completing this lab you will be able to:

- explain ERC20
- read metadata
- send token transfers
- inspect Transfer events
- use Disperse

---

## Required Reading

| Topic | Link |
|---|---|
| ERC20 standard | https://eips.ethereum.org/EIPS/eip-20 |
| OpenZeppelin | https://docs.openzeppelin.com/contracts/ |
| OpenZeppelin Wizard | https://wizard.openzeppelin.com/ |
| Remix | https://remix.ethereum.org/ |
| Disperse | https://disperse.app/ |

---

## Required Software

| Tool | Purpose |
|---|---|
| MetaMask | Sign txs |
| Remix | Optional deploy |
| Etherscan | Events |
| Disperse | Batch transfer |

---

## Key Terms

| Term | Meaning |
|---|---|
| `ERC20` | Fungible token standard. |
| `balanceOf` | Reads balance. |
| `transfer` | Sends tokens. |
| `approve` | Allows spending. |
| `Transfer event` | Proves token movement. |

---

## Safety Notes

!!! danger "Never share secrets"
    Never submit private keys, seed phrases, recovery phrases, or passwords.

!!! warning "Use testnets only"
    Use Sepolia for Ethereum labs unless the instructor explicitly says otherwise.

---

## Step-by-Step Instructions

### Step 1 — Choose token

Use class token or deploy with OpenZeppelin Wizard and Remix.

### Step 2 — Record metadata

Contract address, name, symbol, decimals, totalSupply.

### Step 3 — Send transfers

Send tokens to at least three addresses.

### Step 4 — Inspect events

Open tx logs and find Transfer events.

### Step 5 — Use Disperse

Connect on Sepolia, paste recipients/amounts, submit batch tx.

### Step 6 — Save evidence

Record token contract, transfer txs, Disperse tx.

---

## Expected Result

ERC20 contract, three transfers, one Disperse transaction, and visible Transfer events.

---

## Submission

Add this fragment to `submission.json`:

```json
{"labs":{"lab5":{"network":"sepolia","wallet":"0x...","token_contract":"0x...","token_name":"Student Token","token_symbol":"STUD","transfer_txs":["0x...","0x...","0x..."],"disperse_tx":"0x..."}}}
```

---

## Automatic Validation

| Check | Requirement |
|---|---|
| Contract | Exists on Sepolia. |
| Transfers | Contain ERC20 Transfer events. |
| Sender | Student wallet participates. |
| Disperse | Batch tx exists. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| ETH instead of token | Use token transfer. |
| No Transfer event | Check tx type. |
| Disperse fails | Check balance and allowance. |

---

## Self-Check Questions

1. What is ERC20?
2. What does Transfer event prove?
3. Why use Disperse?
