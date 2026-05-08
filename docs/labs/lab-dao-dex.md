# DAO/DEX Lab — AMM Mechanics and Price Impact

## Goal

Implement a Uniswap V2-style AMM pool in Python and analyze price impact.

## Learning objectives

1. Implement the constant product invariant `x · y = k`.
2. Compute swap output amounts with fees.
3. Verify that `k` never decreases after swaps.
4. Quantify price impact as a function of trade size and pool depth.
5. Compare fee tiers.

## Required formulas

```text
x · y = k
amount_out = y · amount_in · (1 − f) / (x + amount_in · (1 − f))
price_impact = (p_spot − p_execution) / p_spot
spot_price = reserve_y / reserve_x
```

## Deliverables

1. Completed notebook `lab_dao_dex_[studentID].ipynb`.
2. Working `UniswapV2Pool` class.
3. Two plots: swap size vs price impact, and pool TVL vs price impact.
4. Written answers to the research questions.

The provided notebook is stored in the repository under `notebooks/uniswap_v2_lab_task.ipynb`.
