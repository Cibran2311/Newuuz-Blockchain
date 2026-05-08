# Assignment 3 — Liquidity Provision in an AMM

## Goal

Extend the in-class Uniswap V2 AMM notebook with liquidity provider mechanics.

## Topic

Uniswap V2 — LP shares, fee accrual, and impermanent loss.

## Tasks

### 3.1 Adding liquidity

Implement `add_liquidity` with:

```text
shares₀ = √(x · y)
Δ_shares = (Δx / x) · S_total
```

Explain how wrong-ratio deposits should be handled.

### 3.2 Removing liquidity

Implement proportional withdrawal:

```text
withdraw_x = (shares / S_total) · reserve_x
withdraw_y = (shares / S_total) · reserve_y
```

### 3.3 Fee accrual

Track fee earnings using growth in `k`:

```text
growth = √(k_current / k_entry)
fee_x = current_x − current_x / growth
```

### 3.4 Fee income vs volume

Simulate three fee tiers: 5, 30, and 100 bps. Plot cumulative fee income in USD.

### 3.5 Bonus

Design one additional experiment, for example impermanent loss, multi-hop routing, or fee-tier crossover.

## Deliverables

1. Completed notebook `assignment3_liquidity_[studentID].ipynb`.
2. All code cells must run from a fresh kernel.
3. Markdown answers to all research questions.
4. One short report at the end of the notebook.

## Evaluation

| Criterion | Weight |
|---|---:|
| LP share minting and ratio constraint | 20% |
| Withdrawal correctness | 15% |
| Fee accrual via k-growth | 20% |
| Fee-tier simulation and plot | 25% |
| Written analysis quality | 20% |
| Bonus experiment | +15% |

## Reporting JSON

In addition to the normal deliverables, add a `submission.json` file to the root of your GitHub repository.

Use the common format described in [JSON Submission Format](../templates/json-submission-format.md). This allows the instructor or checker script to verify wallet addresses, contract addresses, transaction hashes, links, and completion status automatically.
