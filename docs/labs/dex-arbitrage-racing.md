# Lab — DEX Arbitrage Racing Game

## Overview

This lab is a real-time DeFi competition. Students identify price inefficiencies between two Automated Market Maker instances and perform swaps to maximize their final portfolio value.

The lab reinforces the constant product formula:

```text
x · y = k
```

Two DEX pools start with different liquidity depths, creating an immediate arbitrage opportunity.

## Learning outcomes

Students should be able to:

- use the constant product AMM formula;
- understand price impact and slippage;
- compare prices across two pools;
- execute swaps under time pressure;
- understand why arbitrage changes future prices;
- reason about MEV-like competition at an introductory level.

## Initial setup

The TA or instructor deploys two XYK DEX contracts:

| DEX | TEST reserve | USDC reserve |
|---|---:|---:|
| DEX Alpha | 1,000 TEST | 5,000 USDC |
| DEX Beta | 800 TEST | 4,800 USDC |

Each student receives:

- 100 TEST tokens;
- testnet gas;
- DEX Alpha address;
- DEX Beta address.

## Student instructions

### Step 1 — Price discovery

Call `getSwapPrice` or an equivalent view function on both DEX contracts.

Record how much USDC you receive for selling `10 TEST` on each DEX.

### Step 2 — Strategy

Identify where TEST is cheaper and where it is more expensive.

Example:

```text
DEX Alpha: 1 TEST ≈ 5.0 USDC
DEX Beta:  1 TEST ≈ 5.5 USDC
```

A simple strategy would be to buy TEST on Alpha and sell on Beta, but every swap changes the pool price.

### Step 3 — Execution

Use the `swap` function to perform profitable trades.

Rules:

- time limit: 15 minutes;
- all swaps must be on the class testnet;
- students may calculate manually or use scripts;
- final score is based on total portfolio value in USDC terms.

### Step 4 — Final portfolio calculation

At the end, calculate:

```text
total_value = USDC_balance + TEST_balance × final_TEST_price
```

The instructor may define the final TEST price as:

- price on DEX Alpha;
- price on DEX Beta;
- average of both DEX prices.

## Deliverables

Students submit:

- wallet address;
- swap transaction hashes;
- final TEST balance;
- final USDC balance;
- short explanation of strategy.

## Automatic validation

The checker can verify:

- student received initial TEST;
- swap transactions interacted with approved DEX contracts;
- final balances are readable;
- final score can be calculated deterministically.

## Instructor notes

This lab works best as an in-class competition. It can also be extended into a homework assignment where students write a simple arbitrage bot.
