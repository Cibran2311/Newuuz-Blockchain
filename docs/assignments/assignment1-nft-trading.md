# Assignment 1 — NFT Quest: Trading and Special Contract Interaction

## Goal

Complete a full NFT ownership flow: interact with professor NFT, mint your own NFT, and send it to a special smart contract.

---

## Scenario

You are acting as an NFT engineer. Your task is to prove that you can work with NFT ownership, approvals, and contract-based NFT interactions.

---

## Learning Objectives

After completing this assignment students will be able to:

- work with ERC721 ownership
- use approve and transferFrom
- read NFT Transfer events
- prove NFT movement on-chain

---

## Requirements

1. Receive or buy professor NFT.
2. Transfer or sell professor NFT back.
3. Mint your own ERC721 NFT.
4. Approve the special contract if required.
5. Transfer your NFT to the special contract.
6. Record all hashes and token IDs.

---

## Deliverables

- submission.json with NFT contract addresses and token IDs
- transaction hashes
- explorer links
- short notes if required

---

## Submission Format

Add this section to `submission.json`:

```json
{"assignments":{"assignment1":{"network":"sepolia","wallet":"0x...","professor_nft_contract":"0x...","professor_token_id":"1","personal_nft_contract":"0x...","personal_token_id":"1","special_contract":"0x...","tx_hashes":["0x..."]}}}
```

---

## Automatic / Semi-Automatic Validation

| Check | Requirement |
|---|---|
| Professor NFT | Ownership flow exists. |
| Personal NFT | Token was minted. |
| Special contract | NFT reached correct contract. |
| Events | ERC721 events exist. |

---

## Grading Rubric

| Criterion | Weight | What is evaluated |
|---|---:|---|
| Professor NFT flow | 25% | Correctly interacts with professor NFT. |
| Personal NFT | 25% | Mints and identifies personal NFT. |
| Special contract | 30% | NFT transferred to correct contract. |
| Evidence | 20% | JSON and hashes are correct. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Wrong token ID | Check event logs. |
| Approval missing | Call approve. |
| Wrong contract | Use official class addresses. |

---

## Final Checklist

- [ ] All required actions are completed.
- [ ] All transaction hashes are saved.
- [ ] `submission.json` is valid.
- [ ] Evidence uses testnet networks.
- [ ] Repository is pushed before deadline.
