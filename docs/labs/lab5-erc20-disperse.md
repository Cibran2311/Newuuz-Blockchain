# Mission 5 — Launch Your Token

## Goal

In this lab you will work with ERC20 tokens on Ethereum Sepolia. You will either deploy or use a class ERC20 token, perform token transfers, inspect transfer events, and use Disperse for batch token distribution.

## Why This Lab Matters

ERC20 is the most common token standard in Ethereum-compatible ecosystems.

Real projects use ERC20 tokens for:

- governance tokens;
- stablecoins;
- in-game currencies;
- reward systems;
- DeFi protocols;
- DAO voting.

Batch transfers are common when a project needs to distribute tokens to many users, contributors, or students.

## What You Will Learn

After completing this lab you will be able to:

- explain the ERC20 token standard;
- read ERC20 metadata;
- perform ERC20 transfers;
- understand `Transfer` events;
- use Disperse for batch token transfer;
- find token activity in Etherscan;
- prepare ERC20 evidence for automatic checking.

## Required Reading

| Topic | Link |
|---|---|
| ERC20 standard | https://eips.ethereum.org/EIPS/eip-20 |
| OpenZeppelin Contracts | https://docs.openzeppelin.com/contracts/ |
| OpenZeppelin Wizard | https://wizard.openzeppelin.com/ |
| Remix IDE | https://remix.ethereum.org/ |
| Disperse | https://disperse.app/ |

## Required Software

| Tool | Purpose |
|---|---|
| MetaMask | Sign transactions |
| Remix IDE | Optional contract deployment |
| OpenZeppelin Wizard | Generate ERC20 contract |
| Sepolia Etherscan | Inspect transactions and events |
| Disperse | Batch token transfer |

## Key Terms

| Term | Meaning |
|---|---|
| ERC20 | Standard interface for fungible tokens on Ethereum. |
| Fungible token | Token where each unit is equal to another unit. |
| `balanceOf` | Function that returns token balance of an address. |
| `transfer` | Function used to send tokens. |
| `approve` | Function that allows another address/contract to spend tokens. |
| `allowance` | Amount approved for spending. |
| `Transfer` event | Event emitted when tokens move between addresses. |
| Disperse | Tool for sending tokens to many addresses in one operation. |

## Safety Notes

!!! warning
    Use Sepolia only. Do not deploy or transfer on Ethereum Mainnet.

!!! danger
    Do not upload private keys or seed phrases.

## Step-by-Step Instructions

### Step 1 — Choose Token Approach

The instructor may provide a class ERC20 token contract. If a class token is provided, use it.

If you need to deploy your own token:

1. Open OpenZeppelin Wizard: https://wizard.openzeppelin.com/
2. Select **ERC20**.
3. Set token name and symbol.
4. Enable minting if required.
5. Copy contract code.
6. Open Remix: https://remix.ethereum.org/
7. Compile and deploy to Sepolia using MetaMask.

### Step 2 — Record Token Metadata

Open the token contract in Etherscan or Remix and record:

- token contract address;
- token name;
- symbol;
- decimals;
- total supply.

### Step 3 — Perform ERC20 Transfers

Send tokens to at least three addresses.

For each transfer, record the transaction hash.

### Step 4 — Inspect Transfer Events

Open each transaction in Sepolia Etherscan.

Find the event log:

```text
Transfer(address indexed from, address indexed to, uint256 value)
```

Record:

- sender;
- recipient;
- value;
- token contract address.

### Step 5 — Use Disperse

1. Open https://disperse.app/
2. Connect MetaMask.
3. Make sure network is Sepolia.
4. Select token transfer mode.
5. Paste recipient addresses and token amounts.
6. Confirm transaction.
7. Save transaction hash.

## Expected Result

At the end of the lab you should have:

- ERC20 token contract address;
- at least three token transfer transactions;
- one Disperse transaction;
- visible `Transfer` events in Etherscan.

## Submission

Add this fragment to `submission.json`:

```json
{
  "labs": {
    "lab5": {
      "network": "sepolia",
      "wallet": "0xYourWalletAddress",
      "token_contract": "0xTokenContract",
      "token_name": "Student Token",
      "token_symbol": "STUD",
      "transfer_txs": [
        "0xTransferTx1",
        "0xTransferTx2",
        "0xTransferTx3"
      ],
      "disperse_tx": "0xDisperseTx"
    }
  }
}
```

## Automatic Validation

| Check | Requirement |
|---|---|
| Token contract | Contract exists on Sepolia. |
| ERC20 compatibility | Token exposes basic ERC20 methods. |
| Transfer events | Submitted transactions contain ERC20 `Transfer` events. |
| Sender | Student wallet participated in transfers. |
| Disperse | Disperse transaction exists and includes batch transfers. |

## Common Mistakes

| Mistake | Fix |
|---|---|
| Sending ETH instead of ERC20 token | Use token contract `transfer`, not native ETH send. |
| Wrong network | Switch to Sepolia. |
| Contract not deployed | Wait for deployment confirmation and copy correct address. |
| No Transfer event | Check that transaction was token transfer, not approval only. |
| Disperse fails | Check token balance and allowance. |
| Invalid JSON array | Make sure `transfer_txs` is a JSON array. |

## Self-Check Questions

1. What is the difference between ETH and ERC20 tokens?
2. What does the `Transfer` event prove?
3. Why do batch transfers help?
4. What is the difference between `transfer` and `approve`?
5. How can the checker verify your transfer automatically?
