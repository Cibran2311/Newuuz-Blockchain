# Mission 7 — Trade Like a DeFi Bot

## Goal

In this lab you will analyze two automated market maker pools, compare token prices, execute swaps, and calculate whether your arbitrage strategy made profit or loss.

---

## Why This Lab Matters

Decentralized exchanges do not use traditional order books. Many DEXs use liquidity pools and mathematical formulas to determine prices.

Arbitrage bots constantly monitor DeFi markets and exploit temporary price differences. This lab gives you a simplified version of that workflow.

---

## What You Will Learn

After completing this lab you will be able to:

- explain the constant product formula;
- read liquidity pool reserves;
- calculate approximate pool price;
- understand slippage;
- identify arbitrage direction;
- execute swap transactions;
- calculate profit or loss;
- understand why speed matters in DeFi.

---

## Required Reading

| Topic | Link |
|---|---|
| Uniswap V2 overview | https://docs.uniswap.org/contracts/v2/concepts/protocol-overview/how-uniswap-works |
| Uniswap developers | https://developers.uniswap.org/ |
| Automated market maker | https://en.wikipedia.org/wiki/Automated_market_maker |
| Constant product market maker | https://en.wikipedia.org/wiki/Constant_function_market_maker |

---

## Required Software

| Tool | Purpose |
|---|---|
| MetaMask | Sign swap transactions |
| Class DEX interface / Remix | Interact with DEX Alpha and DEX Beta |
| Sepolia Etherscan / private explorer | Inspect swaps |
| Calculator / Python | Calculate price and profit |
| TEST / USDC test tokens | Tokens for trading |

---

## Key Terms

| Term | Meaning |
|---|---|
| `AMM` | Automated market maker. |
| `DEX` | Decentralized exchange. |
| `Liquidity pool` | Contract containing reserves of two tokens. |
| `Reserve` | Amount of token stored in the pool. |
| `x * y = k` | Constant product formula used by many AMMs. |
| `Slippage` | Price change caused by trade size. |
| `Arbitrage` | Buying in one market and selling in another for profit. |
| `Swap` | Exchange one token for another. |

---

## Theoretical Background

In a constant product AMM:

```text
x * y = k
```

Where:

- `x` = reserve of token X;
- `y` = reserve of token Y;
- `k` = constant.

Approximate price can be estimated as:

```text
price(TEST in USDC) = USDC reserve / TEST reserve
```

Example:

| Pool | TEST Reserve | USDC Reserve | Approx. Price |
|---|---:|---:|---:|
| DEX Alpha | 1000 TEST | 5000 USDC | 5 USDC / TEST |
| DEX Beta | 800 TEST | 4800 USDC | 6 USDC / TEST |

In this example:

- TEST is cheaper on Alpha;
- TEST is more expensive on Beta;
- strategy: buy TEST on Alpha, sell TEST on Beta.

---

## Safety Notes

!!! warning "Testnet only"
    This is a testnet or private testnet lab. Do not use real funds.

!!! info "Every trade changes price"
    Your swap changes pool reserves. The next student may see a different price.

---

## Step-by-Step Instructions

### Step 1 — Receive Test Tokens

The instructor or TA will provide:

- TEST token;
- USDC token;
- DEX Alpha contract/interface;
- DEX Beta contract/interface.

Make sure your wallet has:

```text
TEST
USDC
Sepolia ETH / test gas token
```

---

### Step 2 — Read Pool Reserves

For each DEX, read reserves.

You may use:

- DEX web interface;
- Remix;
- contract read functions;
- script.

Record:

```text
DEX Alpha:
TEST reserve = ...
USDC reserve = ...

DEX Beta:
TEST reserve = ...
USDC reserve = ...
```

---

### Step 3 — Calculate Prices

Use:

```text
price(TEST) = USDC reserve / TEST reserve
```

Example:

```text
Alpha = 5000 / 1000 = 5 USDC per TEST
Beta = 4800 / 800 = 6 USDC per TEST
```

Decision:

```text
Buy TEST where price is lower.
Sell TEST where price is higher.
```

---

### Step 4 — Estimate Swap Output

Before trading, call the DEX price function if available.

Examples of possible function names:

```solidity
getSwapPrice(...)
getAmountOut(...)
quote(...)
```

Record expected output.

---

### Step 5 — Execute First Swap

Execute the first swap on the cheaper DEX.

Example:

```text
Swap USDC → TEST on DEX Alpha
```

Save transaction hash.

---

### Step 6 — Execute Second Swap

Execute the second swap on the more expensive DEX.

Example:

```text
Swap TEST → USDC on DEX Beta
```

Save transaction hash.

---

### Step 7 — Calculate Final Value

Calculate your final value in USDC.

Example:

```text
final_value = USDC balance + TEST balance * final_TEST_price
```

Write whether you made profit or loss.

---

## Expected Result

At the end of this lab you should have:

- reserve data for DEX Alpha and DEX Beta;
- price calculation;
- at least one swap transaction;
- final USDC-equivalent value;
- explanation of your arbitrage strategy.

---

## Submission

Add this fragment to `submission.json`:

```json
{
  "labs": {
    "lab7": {
      "network": "sepolia_or_private_testnet",
      "wallet": "0xYourWalletAddress",
      "dex_alpha": "0xDexAlpha",
      "dex_beta": "0xDexBeta",
      "alpha_reserves": {
        "test": "1000",
        "usdc": "5000"
      },
      "beta_reserves": {
        "test": "800",
        "usdc": "4800"
      },
      "strategy": "Buy TEST on Alpha, sell TEST on Beta",
      "swap_txs": [
        "0xSwapTx1",
        "0xSwapTx2"
      ],
      "final_usdc_value": "123.45"
    }
  }
}
```

---

## Automatic Validation

The checker will verify:

| Check | Requirement |
|---|---|
| DEX contracts | Submitted DEX addresses match class contracts. |
| Swap transactions | Swap txs exist and are successful. |
| Wallet | Student wallet participated in swaps. |
| Events | Swap or token transfer events exist. |
| Final value | Final value can be recalculated from balances/reserves. |
| Strategy | Strategy explanation is present. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Buying on expensive DEX | Compare prices before swapping. |
| Ignoring slippage | Check expected output before swap. |
| Failed swap | Check token approval and balance. |
| No final calculation | Calculate final value in USDC. |
| Submitting only one DEX address | Submit both Alpha and Beta. |
| Wrong token direction | Write token input/output clearly. |

---

## Self-Check Questions

1. What does `x * y = k` mean?
2. Why does a swap change the price?
3. What is slippage?
4. When is arbitrage profitable?
5. Why do fast bots dominate real DeFi arbitrage?
