# Assignment 2 — Security Arena: Ethernaut

## Goal

In this assignment you will solve Ethernaut smart contract security challenges on Ethereum Sepolia.

You must reach a total complexity score of at least:

```text
10
```

## Why This Assignment Matters

Smart contracts often control real assets. A small mistake in Solidity code can lead to lost funds, broken access control, or permanent contract failure.

Ethernaut teaches common Ethereum smart contract vulnerabilities through practical CTF-style levels.

You will learn to think like a security researcher:

- read vulnerable contracts;
- identify weak assumptions;
- interact with contracts manually;
- inspect transaction traces;
- verify completion on-chain.

## What You Will Learn

After completing this assignment you will be able to:

- use Ethernaut on Sepolia;
- create level instances;
- interact with vulnerable smart contracts;
- submit solved instances;
- identify common Solidity vulnerabilities;
- use Etherscan to verify evidence;
- understand how automatic grading checks completion.

## Required Reading

| Topic | Link |
|---|---|
| Ethernaut | https://ethernaut.openzeppelin.com/ |
| Solidity documentation | https://docs.soliditylang.org/ |
| Solidity security considerations | https://docs.soliditylang.org/en/latest/security-considerations.html |
| OpenZeppelin Ethernaut GitHub | https://github.com/OpenZeppelin/ethernaut |
| Sepolia Etherscan | https://sepolia.etherscan.io/ |

## Required Software

| Tool | Purpose |
|---|---|
| MetaMask | Sign Ethernaut transactions |
| Sepolia ETH | Pay gas fees |
| Browser DevTools | Optional debugging |
| Etherscan | Inspect transactions |
| Remix / Console | Optional interaction with contracts |

## Key Terms

| Term | Meaning |
|---|---|
| Ethernaut | Smart contract security challenge platform by OpenZeppelin. |
| Level | Individual vulnerable smart contract challenge. |
| Instance | Personal deployed contract copy for a level. |
| Submit instance | Final transaction that checks whether the level is solved. |
| Vulnerability | Mistake in contract logic or implementation. |
| Complexity score | Difficulty score assigned to completed levels. |
| `LevelCompletedLog` | Event emitted when a level is successfully completed. |

## Step-by-Step Instructions

### Step 1 — Open Ethernaut

Open:

```text
https://ethernaut.openzeppelin.com/
```

Connect MetaMask.

Make sure MetaMask uses:

```text
Sepolia
```

### Step 2 — Select a Level

Start with easier levels.

Recommended early levels:

- Hello Ethernaut;
- Fallback;
- Fallout;
- Coin Flip;
- Telephone;
- Token;
- Delegation;
- Force;
- Vault.

The instructor may provide an official score table.

### Step 3 — Create Level Instance

Each level has a button similar to:

```text
Get new instance
```

Click it and confirm the transaction in MetaMask.

This deploys or assigns your personal vulnerable contract instance.

### Step 4 — Analyze the Contract

Read the level description and contract source code.

Look for:

- missing access control;
- unsafe assumptions;
- wrong use of `tx.origin`;
- storage visibility issues;
- bad randomness;
- delegatecall risks;
- integer arithmetic issues;
- forced ETH transfers;
- reentrancy.

### Step 5 — Exploit the Level

Interact with the level contract using:

- Ethernaut UI;
- browser console;
- Remix;
- Etherscan write contract tab;
- custom script.

### Step 6 — Submit Level Instance

After solving the level, click:

```text
Submit instance
```

Confirm the transaction in MetaMask.

If successful, Ethernaut emits a completion event.

### Step 7 — Check Completion

Open Sepolia Etherscan and inspect your submit transaction.

The checker will look for completed levels using Ethernaut completion events.

## Expected Result

At the end of the assignment you should have:

- several completed Ethernaut levels;
- total complexity score >= 10;
- completion evidence on Sepolia;
- wallet address used for all levels.

## Submission

Add this fragment to `submission.json`:

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

## Automatic Validation

| Check | Requirement |
|---|---|
| Wallet | Submitted wallet is valid Ethereum address. |
| Network | Completion events are on Sepolia. |
| Level completion | Ethernaut `LevelCompletedLog` events exist. |
| Unique levels | Duplicate completions do not increase score twice. |
| Complexity | Total complexity score is at least 10. |
| Evidence | Found levels match submitted wallet. |

## Common Mistakes

| Mistake | Fix |
|---|---|
| Using wrong wallet | Complete levels with the same wallet submitted in JSON. |
| Creating instance but not submitting | Always click `Submit instance` after solving. |
| Solving on wrong network | Use Sepolia. |
| Claiming level without completion event | Verify event in Etherscan. |
| Counting duplicate level twice | Only unique completed levels count. |
| Complexity below 10 | Solve additional levels. |

## Self-Check Questions

1. What is the difference between creating an instance and submitting an instance?
2. Why does the checker look for `LevelCompletedLog`?
3. Why do duplicate completed levels not count twice?
4. Which vulnerability was the most surprising?
5. How can you prove that you completed a level without screenshots?
