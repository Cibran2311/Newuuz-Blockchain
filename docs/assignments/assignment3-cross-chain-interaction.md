# Assignment 3 — Chain of Contracts

## Goal

Build and verify a chain of smart contracts on Ethereum and Polkadot, then compare this synchronous contract-call model with TON asynchronous message architecture.

The main idea is to implement a linked execution flow:

```text
User
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

Each contract in the chain must call or trigger the next contract. The final contract must store or emit the final result.

---

## Scenario

You are building a modular blockchain workflow where one contract does not perform the whole operation alone.

Instead, the logic is split into several contracts:

- `ChainEntry` starts the workflow;
- `ChainLink` contracts process intermediate steps;
- `ChainTerminal` receives the final result;
- events prove that every step was executed in the correct order.

This architecture helps students understand:

- contract-to-contract calls;
- event-based verification;
- execution flow;
- gas/weight limitations;
- differences between Ethereum, Polkadot, and TON.

---

## Learning Objectives

After completing this assignment you will be able to:

- design a multi-contract workflow;
- deploy several connected smart contracts;
- execute a chain of contract calls;
- emit and inspect events;
- verify execution order;
- compare Solidity and ink! contract models;
- explain why TON requires a different asynchronous approach.

---

## Required Chain

The minimum required chain is:

```text
User → ChainEntry → ChainLink(1) → ChainLink(2) → ChainLink(3) → ChainTerminal
```

Minimum contracts:

| Contract | Purpose |
|---|---|
| `ChainEntry` | Starts the chain and validates the caller. |
| `ChainLink(1)` | Receives data from entry and forwards it. |
| `ChainLink(2)` | Receives data from link 1 and forwards it. |
| `ChainLink(3)` | Receives data from link 2 and forwards it. |
| `ChainTerminal` | Receives final data and stores/emits final result. |

---

## Required Events

The Ethereum implementation should emit events similar to:

```solidity
event ChainStarted(address indexed user, bytes32 data);
event EntryExecuted(address indexed entry, address indexed next);
event LinkExecuted(uint256 indexed index, address indexed current, address indexed next);
event FinalReceived(address indexed terminal, bytes32 finalData);
event ChainCompleted(address indexed user, bytes32 finalData);
```

The exact event names may differ, but the execution must be verifiable.

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

---

## Part A — Ethereum Implementation

### Requirements

1. Use Ethereum Sepolia or local Hardhat network if Sepolia deployment is not required by the instructor.
2. Implement or reuse the contract chain structure.
3. Deploy:
   - `ChainEntry`;
   - at least three `ChainLink` contracts;
   - `ChainTerminal`.
4. Configure contracts so that each contract knows the next contract address.
5. Call the entry function, for example:

```solidity
startChain(bytes32 data)
```

6. Verify that the full chain was executed.
7. Save:
   - contract addresses;
   - deployment transaction hashes;
   - start transaction hash;
   - emitted events;
   - final stored result.

---

## Part B — Polkadot / ink! Implementation

### Requirements

1. Implement or run a similar chain using ink! contracts.
2. Use local test environment, Westend-compatible environment, or instructor-provided setup.
3. Implement equivalent roles:
   - entry contract;
   - link contracts;
   - terminal contract.
4. Execute the chain.
5. Save:
   - contract addresses or local deployment output;
   - execution proof;
   - events if available;
   - final stored result.

If public deployment is not available, submit local test output and repository path.

---

## Part C — TON Architecture Comparison

TON implementation is not required by default.

Instead, write a technical comparison explaining how this chain would work differently in TON.

Your comparison must answer:

1. How would TON represent this workflow using asynchronous messages?
2. Why is direct synchronous contract-to-contract execution not the same in TON?
3. How would failure propagation differ?
4. How would gas/fees differ?
5. How would you trace the execution in Tonviewer?
6. What would be harder or easier compared to Ethereum and Polkadot?

Bonus: implement a small TON prototype if the instructor allows it.

---

## Deliverables

Submit:

- Ethereum contract addresses;
- Ethereum start transaction hash;
- emitted event evidence;
- final stored result;
- Polkadot / ink! contract addresses or local test output;
- Polkadot execution proof;
- TON comparison report;
- updated `submission.json`.

---

## Submission Format

Add this section to `submission.json`:

```json
{
  "assignments": {
    "assignment3": {
      "title": "Chain of Contracts",
      "ethereum": {
        "network": "sepolia",
        "wallet": "0xYourWallet",
        "chain_entry": "0xChainEntry",
        "chain_links": [
          "0xChainLink1",
          "0xChainLink2",
          "0xChainLink3"
        ],
        "chain_terminal": "0xChainTerminal",
        "deployment_txs": [
          "0xDeployEntry",
          "0xDeployLink1",
          "0xDeployLink2",
          "0xDeployLink3",
          "0xDeployTerminal"
        ],
        "start_chain_tx": "0xStartChainTx",
        "expected_events": [
          "ChainStarted",
          "EntryExecuted",
          "LinkExecuted",
          "LinkExecuted",
          "LinkExecuted",
          "FinalReceived",
          "ChainCompleted"
        ],
        "final_result": "0xFinalData",
        "explorer_url": "https://sepolia.etherscan.io/tx/0xStartChainTx"
      },
      "polkadot": {
        "network": "local_or_westend",
        "account": "5YourPolkadotAddress",
        "chain_entry": "contract-address-or-local-id",
        "chain_links": [
          "contract-address-or-local-id-1",
          "contract-address-or-local-id-2",
          "contract-address-or-local-id-3"
        ],
        "chain_terminal": "contract-address-or-local-id",
        "execution_proof": "extrinsic hash / local test output / report path",
        "final_result": "final stored value"
      },
      "ton_comparison": {
        "report_path": "reports/ton-chain-comparison.md",
        "summary": "TON would use asynchronous messages instead of direct synchronous contract calls."
      }
    }
  }
}
```

---

## Automatic / Semi-Automatic Validation

| Check | Requirement |
|---|---|
| Ethereum contracts | Required contracts are submitted. |
| Ethereum execution | `start_chain_tx` exists and is successful. |
| Event order | Expected events are emitted in correct logical order. |
| Final result | Terminal contract stores or emits final data. |
| Student wallet | Student wallet started or deployed the chain. |
| Polkadot implementation | ink! implementation or local test proof is submitted. |
| TON comparison | Report exists and answers required architecture questions. |
| JSON validity | `submission.json` is valid JSON. |

---

## Grading Rubric

| Criterion | Weight | Description |
|---|---:|---|
| Ethereum chain implementation | 30% | Contracts are deployed and connected correctly. |
| Ethereum execution evidence | 20% | Events and final result prove full chain execution. |
| Polkadot / ink! implementation | 25% | Equivalent chain or local proof is provided. |
| TON architecture comparison | 15% | Comparison explains async messages and architectural differences. |
| Submission quality | 10% | JSON, addresses, hashes, and report paths are correct. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Contracts are deployed but not connected | Set the next contract address for every chain element. |
| Only one contract is used | The assignment requires a chain of at least five contracts. |
| No event evidence | Emit events at every step. |
| Final contract does not store result | Add a readable final state variable or event. |
| Polkadot part missing | Submit ink! implementation or local test output. |
| TON part treated as normal EVM call | Explain TON asynchronous messages instead. |
| JSON contains comments | JSON does not support comments. |

---

## Final Checklist

- [ ] Ethereum `ChainEntry` is deployed.
- [ ] At least three Ethereum `ChainLink` contracts are deployed.
- [ ] Ethereum `ChainTerminal` is deployed.
- [ ] Contracts are connected in correct order.
- [ ] `startChain(...)` or equivalent function was called.
- [ ] Events prove full chain execution.
- [ ] Final result is stored or emitted.
- [ ] Polkadot / ink! implementation or local proof is submitted.
- [ ] TON comparison report is written.
- [ ] `submission.json` is valid.
