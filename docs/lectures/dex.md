# DEX — How Decentralized Exchanges Work

## Core question

If there is no order book and no seller waiting on the other side, how is the price determined?

## Centralized exchange vs DEX

| CEX | DEX |
|---|---|
| Exchange holds funds | User keeps keys |
| Order book | Liquidity pool |
| Matching engine | Formula-based pricing |
| Centralized infrastructure | Smart contract execution |

## Liquidity pools

A liquidity pool is a smart contract holding two or more tokens. Traders swap against the pool, and liquidity providers deposit assets to earn fees.

## Constant product AMM

```text
x · y = k
```

The pool price is determined by the reserve ratio:

```text
spot_price = y / x
```

Large trades move the reserves and cause price impact.

## Other AMM designs

| Pool type | Use case | Tradeoff |
|---|---|---|
| Constant Product | volatile pairs | simple, general-purpose |
| StableSwap | stable or correlated assets | low slippage near peg |
| Weighted Pools | custom ratios / index-like pools | lower IL for asymmetric exposure |
| Concentrated Liquidity | active LP management | high capital efficiency, higher complexity |
