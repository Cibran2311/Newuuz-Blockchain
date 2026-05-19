# Assignment 1 — NFT Trading, ERC20 and Disperse

## Overview

This assignment introduces students to Ethereum-style token workflows. Students work with ERC20 tokens, NFTs, Disperse-style multi-send transactions, and a special smart contract that receives student NFTs.

The task is intentionally practical: students must prove their work using Sepolia transaction hashes, contract addresses, and emitted events.

## Learning outcomes

By the end of this assignment, students should be able to:

- deploy or interact with an ERC20 token;
- understand ERC20 `Transfer` events;
- use a Disperse-style multi-send workflow;
- interact with ERC721 NFTs;
- understand `approve`, `transferFrom`, and ownership changes;
- read transaction evidence in Etherscan;
- prepare machine-readable submission data.

## Student tasks

### Part 1 — ERC20 token interaction

The student must complete the following:

1. Deploy an ERC20 token on Ethereum Sepolia **or** interact with the course ERC20 token if the instructor provides one.
2. Perform at least three ERC20 transfers.
3. Record the token contract address.
4. Record transaction hashes for all transfers.
5. Confirm that `Transfer` events are visible on Sepolia Etherscan.

### Part 2 — Disperse transaction

The student must complete one multi-send operation:

1. Use a Disperse-style contract or instructor-provided disperse interface.
2. Send ERC20 tokens to at least two recipient addresses.
3. Record the Disperse transaction hash.
4. Confirm that multiple `Transfer` events were emitted from one transaction.

### Part 3 — Professor NFT trading

The instructor deploys or provides an NFT collection. The student must:

1. Buy, receive, or claim the professor NFT.
2. Prove ownership through an explorer or contract call.
3. Transfer or sell the NFT back according to instructor instructions.
4. Record both transaction hashes.

### Part 4 — Personal NFT and special contract

The student must:

1. Mint a personal ERC721 NFT.
2. Record the NFT contract address and token ID.
3. Send the NFT to a special instructor-provided contract.
4. Confirm the final owner is the special contract.

The special contract may be one of the following:

- NFT vault;
- NFT staking contract;
- NFT burn/trap contract;
- hidden challenge contract.

## Required `submission.json` fields

```json
{
  "assignment_id": "assignment1_nft_erc20_disperse",
  "network": "sepolia",
  "wallet": "0x...",
  "erc20": {
    "token_contract": "0x...",
    "transfer_txs": ["0x...", "0x...", "0x..."],
    "disperse_tx": "0x..."
  },
  "professor_nft": {
    "collection": "0x...",
    "token_id": "1",
    "buy_or_receive_tx": "0x...",
    "sell_or_return_tx": "0x..."
  },
  "personal_nft": {
    "contract": "0x...",
    "token_id": "1",
    "mint_tx": "0x...",
    "sent_to_special_contract_tx": "0x...",
    "special_contract": "0x..."
  }
}
```

## Automatic validation plan

The checker should verify:

| Check | Evidence |
|---|---|
| ERC20 transfers exist | `Transfer(address,address,uint256)` events |
| Disperse transaction exists | one transaction emits multiple ERC20 transfers |
| Professor NFT was received | ERC721 `Transfer` to student wallet |
| Professor NFT was returned/sold | ERC721 `Transfer` from student wallet |
| Personal NFT was minted | ERC721 `Transfer` from zero address |
| Personal NFT was sent to special contract | ERC721 `Transfer` to special contract |

## Grading rubric

| Criterion | Weight |
|---|---:|
| ERC20 deployment or valid interaction | 20% |
| ERC20 transfers and Disperse transaction | 25% |
| Professor NFT buy/receive and sell/return flow | 25% |
| Personal NFT mint and special contract transfer | 20% |
| Correct `submission.json` and evidence quality | 10% |

## Notes

Students must not submit private keys, seed phrases, or screenshots containing sensitive wallet data.
