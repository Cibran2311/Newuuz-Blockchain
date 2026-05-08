# Assignment 2 — Ethernaut CTF Challenge

## Goal

Exploit real smart contract vulnerabilities on Sepolia using the Ethernaut platform.

## Platform

- https://ethernaut.openzeppelin.com/

## Requirement

Complete Ethernaut levels whose cumulative complexity score is at least **7**.

For the maximum score, cumulative complexity should reach **10**. Bonus is available for solving **15 or more levels**.

## Workflow

For each level:

1. Open the level.
2. Create a level instance on Sepolia.
3. Analyze the vulnerable contract.
4. Send the exploit/interactions needed to break the invariant.
5. Submit the instance.
6. Save Etherscan links.

## Verification logic

A level is considered passed when the following can be verified on-chain:

1. Instance creation transaction.
2. Interaction or exploit transaction.
3. Submit instance transaction.

## Deliverables

| Field | Description |
|---|---|
| Wallet address | Student Sepolia address |
| Level list | Completed Ethernaut levels |
| Complexity total | Sum of completed level complexities |
| Evidence | Etherscan links for create / interaction / submit |
| Short explanation | Vulnerability and exploit idea for each solved level |

## AI usage

Allowed: explanations of Solidity, EVM concepts, debugging exploit code.  
Not allowed: copying full solutions without understanding or attribution.

## Reporting JSON

In addition to the normal deliverables, add a `submission.json` file to the root of your GitHub repository.

Use the common format described in [JSON Submission Format](../templates/json-submission-format.md). This allows the instructor or checker script to verify wallet addresses, contract addresses, transaction hashes, links, and completion status automatically.
