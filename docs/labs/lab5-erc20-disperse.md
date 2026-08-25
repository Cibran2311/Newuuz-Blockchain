# Mission 5 — Launch Your Token

## Goal

In this lab you will work with ERC20 tokens on Ethereum Sepolia. You will either deploy or use a class ERC20 token, perform token transfers, inspect transfer events, and use Disperse for batch token distribution.

---

## Why This Lab Matters

ERC20 is the most common token standard in Ethereum-compatible ecosystems. Batch transfers are often used to distribute tokens to many users, contributors, or students.

---

## What You Will Learn

After completing this lab you will be able to:

- explain ERC20 token standard
- read ERC20 metadata
- perform ERC20 transfers
- understand Transfer events
- use Disperse for batch transfers
- find token activity in Etherscan

---

## Required Reading

| Topic | Link |
|---|---|
| ERC20 standard | https://eips.ethereum.org/EIPS/eip-20 |
| OpenZeppelin Contracts | https://docs.openzeppelin.com/contracts/ |
| OpenZeppelin Wizard | https://wizard.openzeppelin.com/ |
| Remix IDE | https://remix.ethereum.org/ |
| Disperse | https://disperse.app/ |

---

## Required Software

| Tool | Purpose |
|---|---|
| MetaMask | Sign transactions |
| Remix IDE | Optional deployment |
| OpenZeppelin Wizard | Generate ERC20 contract |
| Sepolia Etherscan | Inspect events |
| Disperse | Batch transfer |

---

## Key Terms

| Term | Meaning |
|---|---|
| `ERC20` | Standard interface for fungible tokens. |
| `Fungible token` | Each unit is equal to another unit. |
| `balanceOf` | Returns token balance. |
| `transfer` | Sends tokens. |
| `approve` | Allows spending. |
| `allowance` | Approved amount. |
| `Transfer event` | Event emitted when tokens move. |

---

## Safety Notes

!!! danger "Never share your seed phrase"
    Do not send it to anyone. Do not upload it to GitHub.

!!! warning "Use Sepolia only"
    Do not use Ethereum Mainnet for this lab.

---

## Step-by-Step Instructions

### Step 1 — Choose token
Use class ERC20 token or deploy your own with OpenZeppelin Wizard and Remix.
### Step 2 — Record metadata
Record contract address, name, symbol, decimals, and totalSupply.
### Step 3 — Transfer tokens
Send tokens to at least three addresses.
### Step 4 — Inspect events
Open transactions in Etherscan and find Transfer events.
### Step 5 — Use Disperse
Open Disperse, connect MetaMask on Sepolia, paste recipients and amounts, confirm transaction.
### Step 6 — Save evidence
Record token contract, transfer txs, and Disperse tx.

---

## Expected Result

At the end of the lab you should have an ERC20 token contract, at least three token transfer transactions, one Disperse transaction, and visible Transfer events.

---

## Submission

Submit the GitHub repository and Sepolia Etherscan token-contract link in Google Classroom. Include the Disperse transaction link and the three transfer transaction links. Use the Ethereum address registered in the protected course registry.

---

## Automatic Validation

The checker will verify:

| Check | Requirement |
|---|---|
| Token contract | Contract exists on Sepolia. |
| ERC20 compatibility | Basic ERC20 methods exist. |
| Transfer events | Transactions contain ERC20 Transfer events. |
| Sender | Student wallet participated. |
| Disperse | Batch transaction exists. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Sending ETH instead of token | Use token contract transfer. |
| Wrong network | Switch to Sepolia. |
| No Transfer event | Check that tx is token transfer, not approval only. |
| Disperse fails | Check token balance and allowance. |

---

## Self-Check Questions

1. What is the difference between ETH and ERC20?
2. What does Transfer event prove?
3. Why are batch transfers useful?
4. How can the checker verify transfers?
