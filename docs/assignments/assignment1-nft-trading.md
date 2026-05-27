# Assignment 1 — NFT Quest: Trading and Special Contract Interaction

## Goal

Complete a full NFT ownership flow:

1. interact with the professor NFT;
2. return or sell it back;
3. mint your own NFT;
4. approve a special contract;
5. transfer your NFT to the special contract.

This assignment checks whether you can work with NFT ownership, approvals, events, and smart contract interaction.

---

## Scenario

You are an NFT engineer working with a course NFT system.

The professor NFT represents a controlled asset.  
Your personal NFT represents your own on-chain artifact.  
The special contract represents an external system that must receive or lock your NFT.

Your task is to prove the complete ownership flow using on-chain evidence.

---

## Learning Objectives

After completing this assignment you will be able to:

- work with ERC721 NFTs;
- track NFT ownership history;
- use `approve`, `transferFrom`, and `safeTransferFrom`;
- inspect ERC721 events in Etherscan;
- understand how contracts can receive NFTs;
- prepare NFT evidence for automatic grading.

---

## Requirements

1. Use Ethereum Sepolia.
2. Use the same wallet submitted in `submission.json`.
3. Receive or buy the professor NFT.
4. Return or sell the professor NFT back according to instructor rules.
5. Mint your own ERC721 NFT.
6. Approve the special contract if approval is required.
7. Transfer your personal NFT to the special contract.
8. Save all transaction hashes.
9. Submit NFT contract addresses and token IDs.

---

## Step-by-Step Plan

### Step 1 — Prepare Wallet

Use the same Sepolia wallet from previous labs.

Make sure you have Sepolia ETH for gas.

---

### Step 2 — Interact with Professor NFT

The instructor will provide:

- professor NFT contract;
- token ID or mint/buy flow;
- return/sell instructions.

Complete the professor NFT flow and save evidence.

---

### Step 3 — Mint Personal NFT

Use either:

- class NFT minter;
- Remix + OpenZeppelin Wizard;
- instructor-provided contract.

Save:

- contract address;
- token ID;
- mint transaction hash.

---

### Step 4 — Verify Ownership

Call:

```solidity
ownerOf(tokenId)
```

Expected result:

```text
your wallet
```

---

### Step 5 — Approve Special Contract

Call:

```solidity
approve(special_contract, tokenId)
```

Save approval transaction.

---

### Step 6 — Transfer NFT to Special Contract

Transfer NFT to special contract using the required function or UI.

Check that:

```solidity
ownerOf(tokenId) == special_contract
```

---

## Deliverables

Submit:

- professor NFT contract address;
- professor token ID;
- receive/buy transaction hash;
- return/sell transaction hash;
- personal NFT contract address;
- personal token ID;
- mint transaction hash;
- special contract address;
- approval transaction hash;
- transfer-to-special-contract transaction hash.

---

## Submission Format

```json
{
  "assignments": {
    "assignment1": {
      "network": "sepolia",
      "wallet": "0xYourWallet",
      "professor_nft_contract": "0xProfessorNft",
      "professor_token_id": "1",
      "professor_receive_tx": "0x...",
      "professor_return_tx": "0x...",
      "personal_nft_contract": "0xPersonalNft",
      "personal_token_id": "1",
      "personal_mint_tx": "0x...",
      "special_contract": "0xSpecialContract",
      "approval_tx": "0x...",
      "transfer_to_special_contract_tx": "0x..."
    }
  }
}
```

---

## Automatic Validation

| Check | Requirement |
|---|---|
| Network | All evidence is on Sepolia. |
| Professor NFT received | Transfer event shows NFT moved to student. |
| Professor NFT returned | Transfer event shows NFT moved away from student. |
| Personal NFT minted | Mint event exists. |
| Ownership | `ownerOf(personal_token_id)` existed for student before transfer. |
| Approval | Approval event exists if required. |
| Special contract | Personal NFT was transferred to special contract. |
| Wallet | Student wallet participated in required transactions. |

---

## Grading Rubric

| Criterion | Weight | Description |
|---|---:|---|
| Professor NFT flow | 25% | Correct receive/buy and return/sell evidence. |
| Personal NFT mint | 20% | Correct NFT contract and token ID. |
| Special contract interaction | 30% | Approval and transfer to correct contract. |
| Evidence quality | 15% | JSON, hashes, and explorer links are correct. |
| Explanation | 10% | Student can explain ownership flow. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Submitting only contract address | Submit contract address and token ID. |
| Wrong token ID | Check event logs. |
| Approval missing | Call approve before transfer if needed. |
| NFT sent to wrong address | Use official special contract address. |
| Using mainnet | Use Sepolia only. |
| Not checking ownerOf | Verify owner before and after transfer. |

---

## Final Checklist

- [ ] Professor NFT was received/bought.
- [ ] Professor NFT was returned/sold back.
- [ ] Personal NFT was minted.
- [ ] Personal token ID is known.
- [ ] Special contract address is correct.
- [ ] NFT was approved if required.
- [ ] NFT was transferred to special contract.
- [ ] `submission.json` is valid.
