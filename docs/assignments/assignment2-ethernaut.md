# Assignment 2 — Security Arena: Ethernaut

!!! note "Compact Course Status"
    This assignment is an additional challenge. It can be used as the security additional challenge track.

## Difficulty Mode

| Mode | Requirement | Meaning |
|---|---|---|
| Core | Optional 3–5 beginner levels | Practice track; no automatic pass threshold |
| Standard | Total JSON difficulty score ≥ 6 | Regular challenge completion |
| Advanced | Total JSON difficulty score ≥ 10 | Automatic pass threshold |
| Bonus | Total JSON difficulty score ≥ 15 | Extended challenge result |

The checker uses the official Ethernaut JSON difficulty values. It sums the values for unique completed levels; duplicate completions do not add points.

## JSON Difficulty Scale

The numeric value is taken directly from the official Ethernaut `gamedata.json`. The labels below are course guidance only.

| JSON difficulty | Course guidance |
|---:|---|
| 0 | Tutorial |
| 1–2 | Basic |
| 3–4 | Intermediate |
| 5–6 | Advanced |
| 7–8 | Expert |

## Official Ethernaut Level Grading

The complete table is shown here so that the grading is visible without opening an additional block. The IDs, names, and difficulty values follow the official Ethernaut JSON.

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

### Official sources

- [Ethernaut level data (`gamedata.json`)](https://github.com/OpenZeppelin/ethernaut/blob/master/client/src/gamedata/gamedata.json)
- [Sepolia deployment data (`deploy.sepolia.json`)](https://github.com/OpenZeppelin/ethernaut/blob/master/client/src/gamedata/deploy.sepolia.json)

---

## Goal

In this assignment you will solve Ethernaut smart contract security challenges on Ethereum Sepolia.

You must reach a total official JSON difficulty score of at least:

```text
10
```

## Why This Assignment Matters

Smart contracts often control real assets. A small mistake in Solidity code can lead to lost funds, broken access control, or permanent contract failure.

Ethernaut teaches common Ethereum smart contract vulnerabilities through practical CTF-style levels.

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
| Ethernaut level data JSON | https://github.com/OpenZeppelin/ethernaut/blob/master/client/src/gamedata/gamedata.json |
| Sepolia deployment JSON | https://github.com/OpenZeppelin/ethernaut/blob/master/client/src/gamedata/deploy.sepolia.json |
| Sepolia Etherscan | https://sepolia.etherscan.io/ |

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

## Step-by-Step Instructions

### Step 1 — Open Ethernaut

Open https://ethernaut.openzeppelin.com/ and connect MetaMask on Sepolia.

### Step 2 — Select a Level

Start with beginner-friendly levels such as Hello Ethernaut (0), Fallback (1), Fallout (2), Telephone (1), Coin Flip (3), Token (3), or Vault (3). Add more levels until the total of official JSON difficulty score reaches 10.

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

## Expected Result

At the end of the assignment you should have several completed Ethernaut levels, total official JSON difficulty score ≥ 10, completion evidence on Sepolia, and the wallet address used for all levels.

## Submission

Push a short write-up for each solved level to the registered GitHub repository and submit that repository link in Google Classroom. Complete and submit all levels from the Ethereum address stored in the protected course registry. The checker reads on-chain completion events; an automatic pass requires a verified official JSON difficulty score of at least 10.

## Automatic Validation

| Check | Requirement |
|---|---|
| Wallet | Submitted wallet is a valid Ethereum address. |
| Network | Completion events are on Sepolia. |
| Level completion | Ethernaut `LevelCompletedLog` events exist. |
| Unique levels | Duplicate completions do not increase the score twice. |
| JSON difficulty score | Sum of official JSON difficulty values for unique completed levels is at least 10. |
| Evidence | Found levels match the submitted wallet. |

## Common Mistakes

| Mistake | Fix |
|---|---|
| Using the wrong wallet | Complete levels with the wallet registered in the course registry. |
| Creating an instance but not submitting | Always click **Submit instance** after solving. |
| Solving on the wrong network | Use Sepolia. |
| Claiming a level without a completion event | Verify the event in Etherscan. |
| Counting a duplicate level twice | Only unique completed levels count. |
| JSON score below 10 | Solve additional levels or choose higher-difficulty levels. |
