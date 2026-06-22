# Mission 12 — Trade or Break on TON

!!! note "Compact Course Status"
    This lab is optional in the compact course. Use it only for advanced TON work.

## Difficulty Mode

| Mode | Recommendation |
|---|---|
| Course track | Advanced |

This is a bonus lab. Use it for stronger students or as a replacement for another advanced task.

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
    Do not complete both tracks unless instructor allows bonus work.

---

## Track A — TON DeFi Swap

### Step 1 — Prepare Wallet

Make sure your testnet wallet has test TON and required jettons if needed.

### Step 2 — Open STON.fi or SDK

Use instructor-provided interface or SDK instructions.

If using SDK, prepare Node.js project:

```bash
npm init -y
npm install @ston-fi/sdk
```

Exact package may depend on current STON.fi SDK version.

### Step 3 — Prepare Swap

Record input token, output token, amount, expected output, and pool/router if visible.

### Step 4 — Execute Swap

Submit swap transaction and confirm in wallet.

### Step 5 — Inspect Trace

Open transaction in testnet Tonviewer and inspect wallet, router, pool, and token wallet messages.

---

## Track B — TON Security Challenge

### Step 1 — Open Challenge

Open HackTON or instructor-provided challenge.

### Step 2 — Read Task

Identify goal, vulnerable contract, required exploit, and proof condition.

### Step 3 — Execute Solution

Interact with contract according to challenge requirements.

### Step 4 — Save Proof

Save proof transaction, challenge level, explanation, and wallet address.

---

## Expected Result

At the end of this lab you should have either a TON DeFi swap trace or HackTON/security challenge proof.

---

## Submission

For STON.fi swap:

```json
{
  "labs": {
    "lab12": {
      "mode": "stonfi_swap",
      "network": "ton_testnet",
      "ton_wallet": "kQYourWallet",
      "input_token": "TON",
      "output_token": "JETTON",
      "tx_link": "https://testnet.tonviewer.com/...",
      "script_file": "scripts/swap.ts"
    }
  }
}
```

For HackTON:

```json
{
  "labs": {
    "lab12": {
      "mode": "hackton",
      "network": "ton_testnet",
      "ton_wallet": "kQYourWallet",
      "level": "introduction",
      "proof_tx": "https://testnet.tonviewer.com/...",
      "explanation": "..."
    }
  }
}
```

---

## Automatic Validation

| Check | Requirement |
|---|---|
| Mode | `stonfi_swap` or `hackton`. |
| Network | Evidence is on TON testnet. |
| Wallet | Submitted wallet is involved. |
| Swap/proof | Transaction or proof exists. |
| Script | Script file exists if SDK mode is used. |
| Explanation | Explanation is present for HackTON mode. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Using mainnet | Use testnet. |
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