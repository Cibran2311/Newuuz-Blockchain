# Mission 12 — Trade or Break on TON

## Goal

Interact with TON DeFi through STON.fi or solve a TON smart contract security challenge.

---

## Why This Lab Matters

This final lab connects TON architecture to practical DeFi and security tasks.

---

## What You Will Learn

After completing this lab you will be able to:

- interact with TON DeFi
- inspect message traces
- understand async execution
- analyze TON security challenge

---

## Required Reading

| Topic | Link |
|---|---|
| TON docs | https://docs.ton.org/ |
| STON.fi docs | https://docs.ston.fi/ |
| STON.fi SDK | https://docs.ston.fi/developer-section/dex/sdk |
| HackTON | https://www.hacktheton.com/en/level/introduction |

---

## Required Software

| Tool | Purpose |
|---|---|
| Tonkeeper | Wallet |
| Node.js | Optional SDK |
| STON.fi SDK | Swap script |
| Tonviewer | Trace |
| HackTON | Challenge |

---

## Key Terms

| Term | Meaning |
|---|---|
| `Swap` | Exchange tokens. |
| `Trace` | Message sequence. |
| `SDK` | Developer toolkit. |
| `HackTON` | TON security platform. |
| `Async` | Execution through messages over time. |

---

## Safety Notes

!!! warning "Use course test environments"
    Do not use real funds or mainnet assets. Save transaction hashes immediately.

---

## Step-by-Step Instructions

### Step 1 — Choose mode

STON.fi swap or HackTON challenge as assigned.

### Step 2 — Prepare tools

Install Node.js/dependencies or open HackTON.

### Step 3 — Complete action

Perform swap or solve challenge.

### Step 4 — Inspect trace

Open Tonviewer.

### Step 5 — Save proof

Commit script or proof.

### Step 6 — Submit JSON

Add mode and evidence.

---

## Expected Result

Either TON DeFi swap trace or HackTON proof.

---

## Submission

Add this fragment to `submission.json`:

```json
{"labs":{"lab12":{"mode":"stonfi_swap","network":"ton_testnet","tx_link":"https://testnet.tonviewer.com/...","script_file":"scripts/swap.ts"}}}
```

---

## Automatic Validation

| Check | Requirement |
|---|---|
| Mode | Valid. |
| Evidence | Tx/proof exists. |
| Wallet | Student involved. |
| Network | TON testnet. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Wrong mode | Use assigned one. |
| Missing script | Commit script. |
| Mainnet | Use testnet. |
| Incomplete trace | Submit trace link. |

---

## Self-Check Questions

1. What is TON async execution?
2. What is trace?
3. How does TON DeFi differ from Ethereum?
