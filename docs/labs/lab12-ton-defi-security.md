# Mission 12 — Trade or Break on TON

!!! note "Current Course Status"
    Lab 12 is currently part of the main block. Its later difficulty or bonus classification has not been decided.

## Difficulty Mode

| Mode | Recommendation |
|---|---|
| Course track | To be classified |

Complete the track assigned by the instructor. Difficulty variants may be redesigned later.

---

## Goal

In this lab you will complete one of two TON advanced tracks:

- **Track A:** perform a TON DeFi swap using STON.fi or SDK;
- **Track B:** solve a TON smart contract security challenge.

The instructor will specify which track is required.

---

## Why This Lab Matters

TON is not only a transfer network. It has fungible tokens, NFT standards, DEX protocols, asynchronous smart contracts, and security challenges.

This lab connects TON architecture with real applications.

---

## What You Will Learn

After completing this lab you will be able to:

- interact with TON DeFi;
- inspect TON transaction traces;
- understand asynchronous message chains;
- use STON.fi or its SDK;
- analyze TON security challenge evidence;
- submit advanced TON evidence for checking.

---

## Required Reading

| Topic | Link |
|---|---|
| TON documentation | https://docs.ton.org/ |
| STON.fi docs | https://docs.ston.fi/ |
| STON.fi SDK | https://docs.ston.fi/developer-section/dex/sdk |
| Official testnet swap example | https://docs.ston.fi/developer-section/dex/sdk/v2/swap#testnet-swaps-manual-setup |
| HackTON | https://www.hacktheton.com/en/level/introduction |
| Testnet Tonviewer | https://testnet.tonviewer.com/ |

---

## Required Software

| Tool | Purpose |
|---|---|
| Tonkeeper | Sign TON transactions |
| TON testnet wallet | Lab account |
| STON.fi / SDK | DeFi interaction |
| Node.js | Required if using SDK |
| Tonviewer | Trace inspection |
| HackTON | Security challenge platform |

---

## Key Terms

| Term | Meaning |
|---|---|
| `Swap` | Exchange one token for another. |
| `Router` | Contract that routes swaps through pools. |
| `Pool` | Liquidity contract for token pair. |
| `Trace` | Message chain caused by a transaction. |
| `SDK` | Software development kit for programmatic interaction. |
| `HackTON` | TON security challenge platform. |
| `Async execution` | Execution model based on messages over time. |

---

## Safety Notes

!!! warning "Use testnet"
    Do not use real TON or real jettons.

!!! info "Choose assigned track"
    Complete only the track assigned by the instructor unless both tracks are explicitly requested.

---

## Step-by-Step Instructions

### Track A — TON DeFi Swap

#### Step 1 — Prepare Wallet

Make sure your testnet wallet has test TON and required jettons if needed.

#### Step 2 — Configure the Testnet SDK

The public STON.fi REST API discovers mainnet routes. Do not use its returned routers for this laboratory. Testnet swaps use explicitly configured testnet contracts.

Prepare the Node.js project:

```bash
npm init -y
npm install @ston-fi/sdk @ton/ton
```

Use the current instructor-provided contracts. Until they are replaced, the official STON.fi v2.1 testnet example provides:

| Contract | Testnet address |
|---|---|
| CPI Router v2.1 | `kQALh-JBBIKK7gr0o4AVf9JZnEsFndqO0qTCyT-D-yBsWk0v` |
| pTON v2.1 | `kQACS30DNoUQ7NfApPvzh7eBmSZ9L4ygJ-lkNWtba8TQT-Px` |
| TesREED test jetton | `kQDLvsZol3juZyOAVG8tWsJntOxeEZWEaWCbbSjYakQpuYN5` |

Testnet liquidity can be limited. If the official pool is unavailable, the instructor must provide a funded class pool rather than asking students to use mainnet.

#### Step 3 — Prepare Swap

Record input token, output token, amount, expected output, and the router address.

#### Step 4 — Execute Swap

Submit swap transaction and confirm in wallet.

#### Step 5 — Inspect Trace

Open transaction in testnet Tonviewer and inspect wallet, router, pool, and token wallet messages.

---

### Track B — TON Security Challenge

#### Step 1 — Open Challenge

Open HackTON or instructor-provided challenge.

#### Step 2 — Read Task

Identify goal, vulnerable contract, required exploit, and proof condition.

#### Step 3 — Execute Solution

Interact with contract according to challenge requirements.

#### Step 4 — Save Proof

Save proof transaction, challenge level, explanation, and wallet address.

---

## Expected Result

At the end of this lab you should have either a TON DeFi swap trace or HackTON/security challenge proof.

---

## Submission

Fill `labs.lab12` in `submission.json`, set its status to `submitted`, and provide one evidence set:

- **STON.fi mode:** GitHub script link, registered TON wallet, input/output assets, router address, and TON Testnet swap link.
- **HackTON mode:** completed level, proof link or screenshot requested by the instructor, and a short explanation of the vulnerability.

---

## Automatic Validation

| Check | Requirement |
|---|---|
| Mode | `stonfi_swap` or `hackton`. |
| Network | Evidence is on TON testnet. |
| Wallet | Submitted wallet is involved. |
| Swap/proof | Transaction or proof exists. |
| Router | STON.fi mode uses the current instructor-approved testnet router. |
| Script | A JavaScript/TypeScript SDK script exists at the pinned GitHub commit. |
| Explanation | Explanation is present for HackTON mode. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Using mainnet | Use testnet. |
| Using a router returned by `api.ston.fi` | Use the explicitly configured testnet router. |
| Testnet pool has no liquidity | Ask the instructor for the funded class pool. |
| Missing script file | Commit script if SDK was used. |
| Submitting wallet page only | Submit transaction/proof link. |
| Confusing external and internal messages | Inspect trace carefully. |
| Wrong mode value | Use `stonfi_swap` or `hackton`. |

---

## Self-Check Questions

1. What is asynchronous execution?
2. What is a TON transaction trace?
3. What is the difference between swap transaction and token transfer?
4. Why is TON DeFi harder to inspect than simple transfers?
5. What proves that a HackTON challenge was completed?
