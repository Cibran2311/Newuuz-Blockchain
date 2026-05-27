# Mission 6 — Create and Move NFTs

## Goal

Work with ERC721 NFTs, approvals, ownership, and a special smart contract.

---

## Why This Lab Matters

NFTs represent ownership of unique assets. Understanding approvals and ownership is required for marketplaces, games, passes, and certificates.

---

## What You Will Learn

After completing this lab you will be able to:

- explain ERC721 ownership
- mint/receive NFT
- use approve
- use transferFrom
- inspect NFT events

---

## Required Reading

| Topic | Link |
|---|---|
| ERC721 standard | https://eips.ethereum.org/EIPS/eip-721 |
| OpenZeppelin ERC721 | https://docs.openzeppelin.com/contracts/ |
| OpenZeppelin Wizard | https://wizard.openzeppelin.com/ |
| Remix | https://remix.ethereum.org/ |

---

## Required Software

| Tool | Purpose |
|---|---|
| MetaMask | Sign txs |
| Remix/class contract | NFT interactions |
| Etherscan | Events |

---

## Key Terms

| Term | Meaning |
|---|---|
| `ERC721` | NFT standard. |
| `Token ID` | Unique NFT identifier. |
| `ownerOf` | Current owner. |
| `approve` | Allows transfer by another address. |
| `Transfer event` | Ownership change. |

---

## Safety Notes

!!! danger "Never share secrets"
    Never submit private keys, seed phrases, recovery phrases, or passwords.

!!! warning "Use testnets only"
    Use Sepolia for Ethereum labs unless the instructor explicitly says otherwise.

---

## Step-by-Step Instructions

### Step 1 — Get professor NFT

Receive/buy professor NFT as instructed.

### Step 2 — Return NFT

Transfer/sell it back if required.

### Step 3 — Mint personal NFT

Deploy/use NFT minter.

### Step 4 — Approve contract

Approve special contract for token ID if required.

### Step 5 — Transfer NFT

Send your NFT to special contract.

### Step 6 — Save evidence

Record contract, token ID, and txs.

---

## Expected Result

Evidence that professor NFT flow was completed and personal NFT reached special contract.

---

## Submission

Add this fragment to `submission.json`:

```json
{"labs":{"lab6":{"network":"sepolia","wallet":"0x...","professor_nft_contract":"0x...","professor_token_id":"1","personal_nft_contract":"0x...","personal_token_id":"1","special_contract":"0x...","tx_hashes":["0x..."]}}}
```

---

## Automatic Validation

| Check | Requirement |
|---|---|
| Events | ERC721 Transfer events exist. |
| Ownership | Owner changed as required. |
| Special contract | NFT reached correct contract. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Wrong token ID | Check logs. |
| No approval | Call approve. |
| Wrong contract | Use official address. |

---

## Self-Check Questions

1. What identifies an NFT?
2. Why approve?
3. Can a contract own NFT?
