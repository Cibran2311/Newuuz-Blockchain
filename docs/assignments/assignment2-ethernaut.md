# Assignment 2 — Security Arena: Ethernaut

!!! note "Compact Course Status"
    This assignment is optional in the compact course. It can be used as the security bonus track.

## Difficulty Mode

| Mode | Recommendation |
|---|---|
| Course track | Standard / Advanced |

Core: optional or 3–5 beginner levels. Standard: complexity score >= 6. Advanced: complexity score >= 10 or >= 15.

---

## Goal

In this assignment you will solve Ethernaut smart contract security challenges on Ethereum Sepolia.

You must reach a total complexity score of at least:

```text
10
```

---

## Why This Assignment Matters

Smart contracts often control real assets. A small mistake in Solidity code can lead to lost funds, broken access control, or permanent contract failure.

Ethernaut teaches common Ethereum smart contract vulnerabilities through practical CTF-style levels.

---

## What You Will Learn

After completing this assignment you will be able to:

- use Ethernaut on Sepolia;
- create level instances;
- interact with vulnerable smart contracts;
- submit solved instances;
- identify common Solidity vulnerabilities;
- use Etherscan to verify evidence;
- understand how automatic grading checks completion.

---

## Required Reading

| Topic | Link |
|---|---|
| Ethernaut | https://ethernaut.openzeppelin.com/ |
| Solidity documentation | https://docs.soliditylang.org/ |
| Solidity security considerations | https://docs.soliditylang.org/en/latest/security-considerations.html |
| OpenZeppelin Ethernaut GitHub | https://github.com/OpenZeppelin/ethernaut |
| Sepolia Etherscan | https://sepolia.etherscan.io/ |

---

## Key Terms

| Term | Meaning |
|---|---|
| `Ethernaut` | Smart contract security challenge platform by OpenZeppelin. |
| `Level` | Individual vulnerable smart contract challenge. |
| `Instance` | Personal deployed contract copy for a level. |
| `Submit instance` | Final transaction that checks whether the level is solved. |
| `LevelCompletedLog` | Event emitted when a level is successfully completed. |
| `Complexity score` | Difficulty score assigned to completed levels. |

---

## Step-by-Step Instructions

### Step 1 — Open Ethernaut

Open https://ethernaut.openzeppelin.com/ and connect MetaMask on Sepolia.

### Step 2 — Select a Level

Start with easier levels such as Hello Ethernaut, Fallback, Fallout, Coin Flip, Telephone, Token, Delegation, Force, or Vault.

### Step 3 — Create Level Instance

Click **Get new instance** and confirm the transaction in MetaMask.

### Step 4 — Analyze the Contract

Read the level description and contract source code. Look for missing access control, unsafe assumptions, bad randomness, delegatecall risks, forced ETH, reentrancy, and other vulnerabilities.

### Step 5 — Exploit the Level

Interact with the level contract using Ethernaut UI, browser console, Remix, Etherscan write contract tab, or a custom script.

### Step 6 — Submit Level Instance

After solving the level, click **Submit instance** and confirm the transaction.

### Step 7 — Check Completion

Open Sepolia Etherscan and inspect the submit transaction. The checker will look for completed levels using Ethernaut completion events.

---

## Expected Result

At the end of the assignment you should have several completed Ethernaut levels, total complexity score >= 10, completion evidence on Sepolia, and wallet address used for all levels.

---

## Submission

```json
{
  "assignments": {
    "assignment2": {
      "network": "sepolia",
      "ethernaut_wallet": "0xYourWalletAddress",
      "target_complexity": 10,
      "claimed_levels": [
        "Fallback",
        "Fallout",
        "Coin Flip"
      ],
      "notes": "Short explanation of solved levels"
    }
  }
}
```

---

## Automatic Validation

| Check | Requirement |
|---|---|
| Wallet | Submitted wallet is valid Ethereum address. |
| Network | Completion events are on Sepolia. |
| Level completion | Ethernaut `LevelCompletedLog` events exist. |
| Unique levels | Duplicate completions do not increase score twice. |
| Complexity | Total complexity score is at least 10. |
| Evidence | Found levels match submitted wallet. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Using wrong wallet | Complete levels with the same wallet submitted in JSON. |
| Creating instance but not submitting | Always click `Submit instance` after solving. |
| Solving on wrong network | Use Sepolia. |
| Claiming level without completion event | Verify event in Etherscan. |
| Counting duplicate level twice | Only unique completed levels count. |
| Complexity below 10 | Solve additional levels. |