# Mission 6 — Create and Move NFTs

## Goal

In this lab you will work with ERC721 NFTs on Ethereum Sepolia. You will receive or buy a professor NFT, return or sell it back, mint your own NFT, approve a special contract, and transfer your NFT to that contract.

This lab prepares you for **Assignment 1 — NFT Quest**.

---

## Why This Lab Matters

NFTs are used for:

- digital collectibles;
- game assets;
- membership passes;
- certificates;
- event tickets;
- access control;
- on-chain credentials.

Unlike ERC20 tokens, NFTs are unique. Each NFT is identified by:

```text
contract address + tokenId
```

If you know only the contract address, you do not know which NFT is being discussed. If you know only the token ID, you still need the contract address.

---

## What You Will Learn

After completing this lab you will be able to:

- explain what ERC721 means;
- find the owner of an NFT;
- mint an NFT;
- understand `tokenId`;
- use `approve`;
- use `transferFrom` or `safeTransferFrom`;
- inspect ERC721 `Transfer` and `Approval` events;
- prove NFT ownership changes using Etherscan.

---

## Required Reading

| Topic | Link |
|---|---|
| ERC721 standard | https://eips.ethereum.org/EIPS/eip-721 |
| OpenZeppelin ERC721 | https://docs.openzeppelin.com/contracts/ |
| OpenZeppelin Wizard | https://wizard.openzeppelin.com/ |
| Remix IDE | https://remix.ethereum.org/ |
| Sepolia Etherscan | https://sepolia.etherscan.io/ |

---

## Required Software

| Tool | Purpose |
|---|---|
| MetaMask | Sign Sepolia transactions |
| Remix IDE | Deploy or interact with NFT contracts |
| OpenZeppelin Wizard | Generate ERC721 contract if needed |
| Sepolia Etherscan | Inspect NFT events |
| Class NFT contract | Professor NFT / course NFT interaction |
| Special contract | Contract that receives student NFTs |

---

## Key Terms

| Term | Meaning |
|---|---|
| `ERC721` | Ethereum NFT standard. |
| `NFT` | Non-fungible token; each token is unique. |
| `tokenId` | Unique identifier of NFT inside one contract. |
| `ownerOf(tokenId)` | Function that returns current NFT owner. |
| `approve(address, tokenId)` | Allows another address/contract to transfer one NFT. |
| `transferFrom(from, to, tokenId)` | Transfers NFT from one owner to another. |
| `safeTransferFrom` | Safer NFT transfer that checks if recipient contract can receive NFTs. |
| `Transfer` event | Event emitted when NFT ownership changes. |
| `Approval` event | Event emitted when NFT transfer approval is granted. |

---

## Safety Notes

!!! warning "Use Sepolia only"
    Do not use Mainnet NFTs or real assets.

!!! danger "Never share wallet secrets"
    Do not submit seed phrases, private keys, or MetaMask passwords.

!!! info "NFT identity"
    Always save both `nft_contract` and `token_id`.

---

## Step-by-Step Instructions

### Step 1 — Prepare Your Wallet

1. Open MetaMask.
2. Select **Sepolia**.
3. Make sure you have Sepolia ETH for gas.
4. Copy your wallet address.

Expected result:

```text
0xYourWalletAddress
```

---

### Step 2 — Receive or Buy the Professor NFT

The instructor will provide one of the following:

- NFT contract address;
- marketplace/interface link;
- direct transfer flow;
- mint/buy function.

Do the required interaction and save:

- professor NFT contract address;
- professor NFT token ID;
- transaction hash;
- Etherscan link.

Open the transaction in Etherscan and find the ERC721 `Transfer` event.

A typical ERC721 transfer event looks like:

```text
Transfer(from, to, tokenId)
```

Check that:

```text
to = your wallet
```

---

### Step 3 — Return or Sell the Professor NFT

Follow the instructor’s instruction:

- transfer it back;
- sell it back;
- send it to an assigned address;
- interact with a class contract.

Save the transaction hash.

Check in Etherscan that ownership changed away from your wallet.

---

### Step 4 — Mint Your Personal NFT

You may use a class NFT minter or deploy your own contract.

If deploying your own:

1. Open OpenZeppelin Wizard:

```text
https://wizard.openzeppelin.com/
```

2. Select **ERC721**.
3. Set name and symbol.
4. Enable minting if required.
5. Copy contract code.
6. Open Remix.
7. Compile contract.
8. Deploy to **Sepolia**.
9. Mint one NFT to your wallet.

Save:

- personal NFT contract address;
- personal token ID;
- mint transaction hash.

---

### Step 5 — Check NFT Owner

Use one of these methods:

- Etherscan read contract tab;
- Remix;
- custom script.

Call:

```solidity
ownerOf(tokenId)
```

Expected result:

```text
ownerOf(personal_token_id) = your wallet
```

---

### Step 6 — Approve the Special Contract

The instructor will provide a special contract address.

Call:

```solidity
approve(special_contract, personal_token_id)
```

Save the approval transaction hash.

In Etherscan, look for `Approval` event.

---

### Step 7 — Transfer NFT to the Special Contract

Transfer your NFT to the special contract using the method required by the instructor.

Common options:

```solidity
transferFrom(your_wallet, special_contract, tokenId)
```

or

```solidity
safeTransferFrom(your_wallet, special_contract, tokenId)
```

Save the transfer transaction hash.

Check that `ownerOf(tokenId)` is now the special contract address.

---

## Expected Result

At the end of the lab you should have:

- professor NFT interaction evidence;
- personal NFT contract address;
- personal token ID;
- approval transaction;
- transfer transaction to special contract;
- Etherscan links;
- updated `submission.json`.

---

## Submission

Add this fragment to `submission.json`:

```json
{
  "labs": {
    "lab6": {
      "network": "sepolia",
      "wallet": "0xYourWalletAddress",
      "professor_nft_contract": "0xProfessorNftContract",
      "professor_token_id": "1",
      "professor_nft_receive_tx": "0x...",
      "professor_nft_return_tx": "0x...",
      "personal_nft_contract": "0xPersonalNftContract",
      "personal_token_id": "1",
      "mint_tx": "0x...",
      "special_contract": "0xSpecialContract",
      "approval_tx": "0x...",
      "transfer_to_special_contract_tx": "0x..."
    }
  }
}
```

---

## Automatic Validation

The checker will verify:

| Check | Requirement |
|---|---|
| Network | All transactions are on Sepolia. |
| Professor NFT received | ERC721 `Transfer` event shows NFT moved to student wallet. |
| Professor NFT returned/sold | NFT moved away from student wallet. |
| Personal NFT minted | Mint `Transfer` event exists for personal NFT. |
| Token ID | Submitted `tokenId` exists in submitted NFT contract. |
| Approval | `Approval` event exists if approval is required. |
| Special contract transfer | Personal NFT owner becomes special contract. |
| Wallet ownership | Student wallet is involved in required transactions. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Submitting only NFT contract address | Submit contract address and token ID. |
| Wrong token ID | Check `Transfer` event logs. |
| Approval missing | Call `approve` before contract transfer. |
| Using ERC20 transfer logic | ERC721 uses `tokenId`, not amount. |
| NFT not owned by student before transfer | Check `ownerOf(tokenId)` before transfer. |
| Wrong network | Use Sepolia only. |
| Submitting marketplace page instead of tx hash | Submit transaction hash and Etherscan link. |

---

## Self-Check Questions

1. Why is `contract address + tokenId` required to identify an NFT?
2. What does `ownerOf(tokenId)` return?
3. Why might `approve` be required before transferring an NFT?
4. What is the difference between ERC20 and ERC721?
5. How can Etherscan prove that NFT ownership changed?
