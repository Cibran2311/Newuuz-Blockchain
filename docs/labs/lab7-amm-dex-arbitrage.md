# Mission 7 — Trade Like a DeFi Bot

## Goal

Compare two AMM pools and try to profit from price differences.

---

## Why This Lab Matters

DeFi bots compare pools, calculate slippage, and execute arbitrage. This lab connects AMM math to real transactions.

---

## What You Will Learn

After completing this lab you will be able to:

- explain x*y=k
- read reserves
- calculate price
- understand slippage
- execute swaps
- calculate PnL

---

## Required Reading

| Topic | Link |
|---|---|
| Uniswap docs | https://developers.uniswap.org/ |
| Uniswap V2 | https://docs.uniswap.org/contracts/v2/concepts/protocol-overview/how-uniswap-works |
| AMM | https://en.wikipedia.org/wiki/Automated_market_maker |

---

## Required Software

| Tool | Purpose |
|---|---|
| MetaMask | Sign swaps |
| Class DEX contracts | Alpha/Beta |
| Etherscan | Inspect swaps |

---

## Key Terms

| Term | Meaning |
|---|---|
| `AMM` | Automated market maker. |
| `Pool` | Reserves for swaps. |
| `Slippage` | Price movement from trade. |
| `Arbitrage` | Profit from price difference. |
| `Reserve` | Token amount in pool. |

---

## Safety Notes

!!! warning "Use course test environments"
    Do not use real funds or mainnet assets. Save transaction hashes immediately.

---

## Step-by-Step Instructions

### Step 1 — Receive test tokens

Get TEST/USDC from TA faucet.

### Step 2 — Inspect Alpha

Read reserves and price.

### Step 3 — Inspect Beta

Read reserves and price.

### Step 4 — Choose strategy

Buy cheap, sell expensive.

### Step 5 — Execute swaps

Submit txs and record hashes.

### Step 6 — Calculate value

Convert final balances to USDC-equivalent.

---

## Expected Result

Swap txs, final value, and arbitrage explanation.

---

## Submission

Add this fragment to `submission.json`:

```json
{"labs":{"lab7":{"wallet":"0x...","dex_alpha":"0x...","dex_beta":"0x...","swap_txs":["0x..."],"final_usdc_value":"0","strategy":"Buy on Alpha, sell on Beta"}}}
```

---

## Automatic Validation

| Check | Requirement |
|---|---|
| Swaps | Interact with correct DEX contracts. |
| Wallet | Student wallet participated. |
| Final value | Calculation present. |
| Strategy | Explanation present. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Ignoring slippage | Check expected output. |
| Wrong direction | Buy cheap sell expensive. |
| No calculation | Compute final value. |

---

## Self-Check Questions

1. What is x*y=k?
2. Why does swap change price?
3. When is arbitrage profitable?
