# Assignment 2 — Security Arena: Ethernaut

## Goal

Solve Ethernaut smart contract security challenges and reach total complexity score of at least 10.

---

## Scenario

You are acting as a smart contract security analyst. Your goal is to exploit vulnerable contracts and prove completion through on-chain events.

---

## Learning Objectives

After completing this assignment students will be able to:

- analyze Solidity vulnerabilities
- create and submit instances
- use Etherscan as evidence
- understand exploit classes

---

## Requirements

1. Open Ethernaut and connect Sepolia wallet.
2. Create level instances.
3. Solve levels.
4. Submit instances.
5. Reach complexity score >= 10.
6. Submit claimed levels in JSON.

---

## Deliverables

- submission.json with wallet and claimed levels
- optional notes about solved levels
- same wallet used for all levels

---

## Submission Format

Add this section to `submission.json`:

```json
{"assignments":{"assignment2":{"network":"sepolia","ethernaut_wallet":"0x...","target_complexity":10,"claimed_levels":["Fallback","Fallout","Coin Flip"],"notes":"Short explanation"}}}
```

---

## Automatic / Semi-Automatic Validation

| Check | Requirement |
|---|---|
| Wallet | Valid Ethereum address. |
| Completion | LevelCompletedLog events exist. |
| Unique levels | Duplicates do not count twice. |
| Score | Complexity score >= 10. |

---

## Grading Rubric

| Criterion | Weight | What is evaluated |
|---|---:|---|
| Completed levels | 50% | Correct levels completed on-chain. |
| Complexity | 25% | Total score reaches requirement. |
| Evidence | 15% | Wallet and data match. |
| Understanding | 10% | Student can explain vulnerabilities. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Created but not submitted | Always submit instance. |
| Wrong wallet | Use same wallet. |
| Score below 10 | Solve more levels. |

---

## Final Checklist

- [ ] All required actions are completed.
- [ ] All transaction hashes are saved.
- [ ] `submission.json` is valid.
- [ ] Evidence uses testnet networks.
- [ ] Repository is pushed before deadline.
