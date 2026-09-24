# Assignment 2 — Security Arena: Ethernaut

!!! note "Current Course Status"
    Assignment 2 is currently part of the main block. Its later difficulty or bonus classification has not been decided.

## Difficulty Mode

| Mode | Recommendation |
|---|---|
| Course track | To be classified |

The current automatic pass threshold is a total official JSON difficulty score of 10. The checker sums the JSON difficulty values of unique completed levels; duplicate completions do not add points.

| JSON difficulty | Course guidance |
|---:|---|
| 0 | Tutorial |
| 1–2 | Basic |
| 3–4 | Intermediate |
| 5–6 | Advanced |
| 7–8 | Expert |

The numeric values come from the official Ethernaut JSON. The guidance labels are only a convenient way to choose levels.

---

## Goal

In this assignment you will solve Ethernaut smart contract security challenges on Ethereum Sepolia.

You must reach a total official JSON difficulty score of at least:

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
| Ethernaut level data JSON | https://github.com/OpenZeppelin/ethernaut/blob/master/client/src/gamedata/gamedata.json |
| Sepolia deployment JSON | https://github.com/OpenZeppelin/ethernaut/blob/master/client/src/gamedata/deploy.sepolia.json |
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
| `JSON difficulty` | Numeric score assigned to a level in the official Ethernaut JSON. |
| `Total score` | Sum of JSON difficulty values for unique completed levels. |

---

???+ note "Official Ethernaut level grading"
    The table below is based on the official `gamedata.json`. The numeric value is authoritative; the labels are course guidance only.

    | ID | Level | JSON difficulty | Guidance |
    |---:|---|---:|---|
    | 0 | Hello Ethernaut | 0 | Tutorial |
    | 1 | Fallback | 1 | Basic |
    | 2 | Fallout | 2 | Basic |
    | 3 | Coin Flip | 3 | Intermediate |
    | 4 | Telephone | 1 | Basic |
    | 5 | Token | 3 | Intermediate |
    | 6 | Delegation | 4 | Intermediate |
    | 7 | Force | 5 | Advanced |
    | 8 | Vault | 3 | Intermediate |
    | 9 | King | 6 | Advanced |
    | 10 | Re-entrancy | 6 | Advanced |
    | 11 | Elevator | 4 | Intermediate |
    | 12 | Privacy | 6 | Advanced |
    | 13 | Gatekeeper One | 8 | Expert |
    | 14 | Gatekeeper Two | 6 | Advanced |
    | 15 | Naught Coin | 5 | Advanced |
    | 16 | Preservation | 8 | Expert |
    | 17 | Recovery | 6 | Advanced |
    | 18 | MagicNumber | 6 | Advanced |
    | 19 | Alien Codex | 7 | Expert |
    | 20 | Denial | 5 | Advanced |
    | 21 | Shop | 4 | Intermediate |
    | 22 | Dex | 3 | Intermediate |
    | 23 | Dex Two | 4 | Intermediate |
    | 24 | Puzzle Wallet | 7 | Expert |
    | 25 | Motorbike | 6 | Advanced |
    | 26 | DoubleEntryPoint | 4 | Intermediate |
    | 27 | Good Samaritan | 5 | Advanced |
    | 28 | Gatekeeper Three | 6 | Advanced |
    | 29 | Switch | 8 | Expert |
    | 30 | HigherOrder | 8 | Expert |
    | 31 | Stake | 6 | Advanced |
    | 32 | Impersonator | 8 | Expert |
    | 33 | Magic Animal Carousel | 6 | Advanced |
    | 34 | Bet House | 4 | Intermediate |
    | 35 | Elliptic Token | 8 | Expert |
    | 36 | Cashback | 8 | Expert |
    | 37 | Impersonator Two | 8 | Expert |
    | 38 | UniqueNFT | 5 | Advanced |
    | 39 | Forger | 5 | Advanced |
    | 40 | NotOptimisticPortal | 8 | Expert |

## Step-by-Step Instructions

### Step 1 — Open Ethernaut

Open https://ethernaut.openzeppelin.com/ and connect MetaMask on Sepolia.

### Step 2 — Select a Level

Start with beginner-friendly levels such as Hello Ethernaut (0), Fallback (1), Fallout (2), Telephone (1), Coin Flip (3), Token (3), or Vault (3). Add more levels until the total official JSON difficulty score reaches 10.

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

At the end of the assignment you should have several completed Ethernaut levels, total official JSON difficulty score >= 10, completion evidence on Sepolia, and wallet address used for all levels.

---

## Submission

Push a short write-up for each solved level to the registered repository. In `submission.json`, fill `assignments.assignment2` with completed level names, instance addresses, submit transactions, and write-up links; then set its status to `submitted`. Complete all levels from an Ethereum address registered in Google Sheets. The checker reads on-chain completion events; an automatic pass requires a verified official JSON difficulty score of at least 10.

---

## Automatic Validation

| Check | Requirement |
|---|---|
| Wallet | Submitted wallet is valid Ethereum address. |
| Network | Completion events are on Sepolia. |
| Level completion | Ethernaut `LevelCompletedLog` events exist. |
| Unique levels | Duplicate completions do not increase score twice. |
| Complexity | Sum of official JSON difficulty values for unique completed levels is at least 10. |
| Evidence | Found levels match submitted wallet. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Using wrong wallet | Complete levels with the wallet registered in the course registry. |
| Creating instance but not submitting | Always click `Submit instance` after solving. |
| Solving on wrong network | Use Sepolia. |
| Claiming level without completion event | Verify event in Etherscan. |
| Counting duplicate level twice | Only unique completed levels count. |
| JSON score below 10 | Solve additional levels or choose higher-difficulty levels. |
