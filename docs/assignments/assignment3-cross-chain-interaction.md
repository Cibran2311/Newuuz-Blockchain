# Assignment 3 — Group Chain of Contracts

## Goal

Build a group-owned chain of smart contracts on **Ethereum Sepolia**.

Students work in groups and connect their contracts into one execution chain. The result must be verifiable through Sepolia transactions, contract addresses, and emitted events.

The main flow is:

```text
Student Wallet
  ↓
ChainEntry
  ↓
ChainLink 1
  ↓
ChainLink 2
  ↓
ChainLink 3
  ↓
ChainTerminal
```

Each group member should be responsible for at least one part of the chain.

---

## Why This Assignment Exists

In real blockchain systems, contracts rarely work alone. They interact with other contracts, forward data, emit events, and depend on correct configuration.

This assignment helps you practice:

- contract-to-contract calls;
- group coordination;
- deployment order;
- address configuration;
- event-based verification;
- transaction analysis through Etherscan;
- evidence-based blockchain reporting.

---

## Network

Use only:

```text
Ethereum Sepolia Testnet
```

Do not use Ethereum mainnet.

Recommended tools:

- MetaMask;
- Remix IDE or Hardhat;
- Sepolia faucet;
- Sepolia Etherscan;
- GitHub repository for code and reports.

---

## Group Size

Recommended group size:

```text
3–5 students
```

Minimum group size:

```text
3 students
```

If a group has only 3 students, one student may own more than one contract.

---

## Required Chain

Minimum chain:

```text
User → ChainEntry → ChainLink(1) → ChainLink(2) → ChainLink(3) → ChainTerminal
```

Required contracts:

| Contract | Minimum Quantity | Purpose |
|---|---:|---|
| `ChainEntry` | 1 | Starts the workflow. |
| `ChainLink` | 3 | Receives data and forwards it to the next contract. |
| `ChainTerminal` | 1 | Receives the final data and stores the result. |

---

## Recommended Group Roles

| Role | Responsibility |
|---|---|
| Coordinator | Organizes addresses, order, and final submission. |
| Entry Owner | Deploys or configures `ChainEntry`. |
| Link Owner | Deploys one `ChainLink`. |
| Terminal Owner | Deploys or configures `ChainTerminal`. |
| Reporter | Prepares the shared report and verifies all evidence links. |

A student may have more than one role, but every student must have a visible personal contribution.

---

## Contract Logic

### ChainEntry

`ChainEntry` starts the chain.

It should:

1. accept input data;
2. emit a start event;
3. call the first `ChainLink`;
4. emit a completion event after the chain finishes, if your design supports it.

Example function name:

```solidity
startChain(bytes32 data)
```

### ChainLink

Each `ChainLink` receives data and forwards it to the next contract.

It should:

1. receive input data;
2. optionally transform the data;
3. emit an event;
4. call the next contract.

Example function name:

```solidity
execute(bytes32 data)
```

### ChainTerminal

`ChainTerminal` receives the final result.

It should:

1. receive final data;
2. store the final result in a public variable;
3. emit a final event.

Example variable:

```solidity
bytes32 public lastResult;
```

---

## Required Events

Your implementation must emit events that make the execution order visible.

Recommended event structure:

```solidity
event ChainStarted(address indexed user, bytes32 data);
event EntryExecuted(address indexed entry, address indexed next);
event LinkExecuted(uint256 indexed index, address indexed current, address indexed next, bytes32 data);
event FinalReceived(address indexed terminal, bytes32 finalData);
event ChainCompleted(address indexed user, bytes32 finalData);
```

Exact names may differ, but the meaning must be clear.

Expected logical order:

```text
ChainStarted
EntryExecuted
LinkExecuted
LinkExecuted
LinkExecuted
FinalReceived
ChainCompleted
```

If your implementation cannot emit `ChainCompleted` after the terminal step, explain why in the report.

---

## Step-by-Step Instructions

### Step 1 — Form a Group

Create a group of 3–5 students.

Choose:

- group ID;
- group coordinator;
- contract owners;
- final chain order.

Example:

```text
Group ID: G1

Student A → ChainEntry
Student B → ChainLink 1
Student C → ChainLink 2
Student D → ChainLink 3
Student E → ChainTerminal
```

### Step 2 — Prepare Sepolia Wallets

Each student must prepare a wallet on Sepolia.

Each student should submit:

- wallet address;
- role in the group;
- owned contract address;
- deployment transaction hash.

### Step 3 — Deploy Contracts

Deploy all required contracts on Sepolia.

Recommended deployment order:

1. `ChainTerminal`;
2. `ChainLink 3`;
3. `ChainLink 2`;
4. `ChainLink 1`;
5. `ChainEntry`.

This reverse deployment order is usually easier because each contract needs to know the next contract address.

Alternative: deploy first, then call setter functions such as:

```solidity
setNext(address nextContract)
```

### Step 4 — Connect the Chain

The final chain must be connected like this:

```text
ChainEntry → ChainLink 1 → ChainLink 2 → ChainLink 3 → ChainTerminal
```

Save evidence for each connection:

- setter transaction hashes; or
- constructor arguments; or
- verified source code / deployment script.

### Step 5 — Execute the Chain

Call the entry contract:

```solidity
startChain(bytes32 data)
```

Use a unique input value.

Example:

```text
keccak256("G1-chain-test-001")
```

Save:

- start transaction hash;
- Etherscan link;
- emitted events;
- final stored result.

### Step 6 — Verify Final Result

The terminal contract must expose the final result.

Examples:

```solidity
lastResult()
lastSender()
executionCount()
```

Your report must show that the terminal contract received the data.

---

## Required Evidence

Each group must provide:

| Evidence | Required |
|---|---|
| Group ID | Yes |
| Student wallets | Yes |
| Contract owners | Yes |
| Contract addresses | Yes |
| Deployment transaction hashes | Yes |
| Chain connection evidence | Yes |
| Start transaction hash | Yes |
| Event order | Yes |
| Final result from terminal contract | Yes |
| Etherscan links | Yes |

---

## Group Submission

One coordinator submits the shared GitHub repository and group report in the Assignment 3 Google Classroom task. The Classroom comment must contain the group ID, member names, registered wallets, roles, contract addresses, deployment and connection transactions, start transaction, and final result.

---

## Individual Submission

Each student opens the same Classroom assignment and submits a short individual contribution note: group ID, role, owned contract, deployment transaction, and what they personally implemented or tested.

---

## Report Requirements

The group report must contain:

1. Group members and roles.
2. Chain diagram.
3. Contract addresses.
4. Deployment transaction hashes.
5. Connection transaction hashes.
6. Start transaction hash.
7. Event order screenshot or decoded event list.
8. Final result from `ChainTerminal`.
9. Short explanation of problems and fixes.
10. Individual contribution table.

Example contribution table:

| Student | Wallet | Role | Contribution |
|---|---|---|---|
| Student A | `0x...` | ChainEntry | Deployed entry and started chain. |
| Student B | `0x...` | ChainLink1 | Deployed first link. |
| Student C | `0x...` | ChainLink2 | Deployed second link. |
| Student D | `0x...` | ChainLink3 | Deployed third link. |
| Student E | `0x...` | ChainTerminal | Deployed terminal and verified result. |

---

## Automatic / Semi-Automatic Validation

The checker can verify:

| Check | Requirement |
|---|---|
| Network | Must be Sepolia. |
| Group size | 3–5 students recommended. |
| Contracts exist | Entry, at least 3 links, terminal. |
| Deployment txs | Each submitted deployment tx exists. |
| Start tx | `start_chain_tx` exists and succeeded. |
| Event order | Events match expected chain logic. |
| Final result | Terminal contract exposes or emits result. |
| Individual contribution | Each student has wallet, role, owned contract, and tx. |
| Evidence access | Repository, report, contracts, and transactions are accessible. |

---

## Grading Rubric

| Criterion | Weight | Description |
|---|---:|---|
| Group chain works end-to-end | 35% | Full chain executes from entry to terminal. |
| Correct event evidence | 20% | Events prove correct execution order. |
| Individual contribution | 20% | Each student owns or clearly contributes to one part. |
| Deployment and configuration quality | 10% | Contracts are connected cleanly and reproducibly. |
| Report quality | 10% | Report explains addresses, txs, screenshots, and problems. |
| Evidence quality | 5% | Classroom submission and report links are complete. |

---

## Penalties

| Problem | Possible Penalty |
|---|---:|
| Missing individual contribution | Up to -20% for that student |
| No successful start transaction | Up to -35% |
| No event evidence | Up to -20% |
| Contracts not connected | Up to -30% |
| Missing or inaccessible evidence | Up to -10% |
| Mainnet transaction used | Assignment may be rejected |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Deploying contracts but not linking them | Use constructor arguments or `setNext(...)`. |
| Starting the chain from the wrong contract | The workflow must start from `ChainEntry`. |
| No final state in terminal | Store final data in a public variable. |
| No events | Emit events at every step. |
| One student does everything | Every student needs a visible contribution. |
| Using different networks | Everyone must use Sepolia. |
| Submitting screenshots only | Always submit transaction hashes and addresses. |

---

## Final Checklist

- [ ] Group has 3–5 students.
- [ ] Every student has a Sepolia wallet.
- [ ] `ChainEntry` is deployed.
- [ ] At least three `ChainLink` contracts are deployed.
- [ ] `ChainTerminal` is deployed.
- [ ] Contracts are connected in the correct order.
- [ ] The chain was started from `ChainEntry`.
- [ ] Start transaction succeeded on Sepolia.
- [ ] Events prove the execution order.
- [ ] Terminal contract stores or emits final result.
- [ ] Group report is ready.
- [ ] Shared repository and report were submitted in Google Classroom.
- [ ] Every student submitted an individual contribution note.
