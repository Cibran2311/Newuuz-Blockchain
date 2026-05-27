# Assignment 3 — Cross-chain Journey: Ethereum, Polkadot, TON

## Goal

Perform connected blockchain actions across Ethereum, Polkadot, and TON and compare architectures.

---

## Scenario

You are acting as a cross-chain operator. Your task is to repeat similar ideas in three different blockchain architectures and document differences.

---

## Learning Objectives

After completing this assignment students will be able to:

- compare ecosystems
- collect evidence from explorers
- understand transaction models
- describe fees/finality/tooling

---

## Requirements

1. Complete Ethereum step.
2. Complete Polkadot / AssetHub step.
3. Complete TON step.
4. Record evidence.
5. Write comparison notes.

---

## Deliverables

- Ethereum tx hash
- Polkadot extrinsic hash
- TON tx link
- comparison notes
- submission.json

---

## Submission Format

Add this section to `submission.json`:

```json
{"assignments":{"assignment3":{"ethereum":{"wallet":"0x...","tx_hash":"0x...","contract":"0x..."},"polkadot":{"wallet":"5...","extrinsic_hash":"..."},"ton":{"wallet":"kQ...","tx_link":"..."},"comparison_notes":"..."}}}
```

---

## Automatic / Semi-Automatic Validation

| Check | Requirement |
|---|---|
| Ethereum | Transaction exists. |
| Polkadot | Extrinsic exists. |
| TON | Transaction exists. |
| Identity | Actions belong to submitted wallets. |
| Comparison | Notes are present. |

---

## Grading Rubric

| Criterion | Weight | What is evaluated |
|---|---:|---|
| Ethereum evidence | 25% | Correct EVM action. |
| Polkadot evidence | 25% | Correct extrinsic/action. |
| TON evidence | 25% | Correct transaction/message. |
| Analysis | 25% | Architecture comparison. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Only one chain | Complete all three. |
| No notes | Write comparison. |
| Wrong explorer | Use correct explorer. |

---

## Final Checklist

- [ ] All required actions are completed.
- [ ] All transaction hashes are saved.
- [ ] `submission.json` is valid.
- [ ] Evidence uses testnet networks.
- [ ] Repository is pushed before deadline.
