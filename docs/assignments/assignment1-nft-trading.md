# Assignment 1 — Token, Swap and NFT Quest

!!! note "Compact Course Status"
    This assignment is an additional challenge and an extension of Labs 5–6. It is also the first production assignment covered by the course autotest.

## Difficulty Mode

| Mode | Requirement | Meaning |
|---|---|---|
| Core | Complete one guided token/NFT flow | Practice track with instructor review |
| Standard | Token + Swap + NFT mint | Normal assignment target |
| Advanced | Standard target plus complete NFT ownership quest | Deeper evidence and explanation |

## Goal

Complete three independently verifiable Sepolia requirements:

1. perform the required course ERC20 token activity;
2. complete the required swap activity;
3. mint an ERC721 NFT to the registered student wallet.

The NFT ownership quest from Lab 6 may be included as an advanced extension: receive or return the Professor NFT, approve the special contract, and transfer the personal NFT to it.

## PASS Rule

The automatic Assignment 1 result is **PASS only when all three objective checks pass**:

- Token;
- Swap;
- NFT mint.

The GitHub repository link and written explanations are supporting evidence. They do not replace missing on-chain activity.

Professor NFT flow, approval details, transfer to the special contract, screenshots, and explanations are reviewed manually. Manual evidence must not silently turn a missing Token, Swap, or NFT result into an automatic PASS.

## Why This Assignment Matters

This assignment combines fungible tokens, decentralized exchange activity, NFT minting, wallet ownership, transaction events, and evidence-based blockchain verification.

## What You Will Learn

After completing this assignment you will be able to:

- inspect ERC20 token activity;
- explain what a swap transaction changes;
- mint and identify an ERC721 NFT;
- connect wallet activity with transaction logs;
- prepare evidence for automatic and manual review.

## Requirements

1. Use Ethereum Sepolia only.
2. Use the Ethereum wallet registered in the protected course registry.
3. Use the instructor-provided course token and approved swap route.
4. Complete the required token activity.
5. Complete the required swap activity.
6. Mint one ERC721 NFT to the registered wallet.
7. Save contract addresses, token IDs, transaction hashes, and explorer links.
8. Never submit a private key, seed phrase, password, or API key.

## Step-by-Step Plan

### Step 1 — Prepare the wallet

Use the Sepolia wallet registered by the instructor. Make sure it has enough test ETH for gas.

### Step 2 — Complete token activity

Use the course ERC20 token or the instructor-provided token address. Record:

- token contract address;
- token transfer transaction hash;
- sender and recipient;
- amount;
- Sepolia explorer link.

### Step 3 — Complete swap activity

Use the assigned DEX or swap route. Record:

- input token;
- output token;
- swap transaction hash;
- wallet address;
- successful Sepolia explorer link.

### Step 4 — Mint the personal NFT

Use the class NFT minter or deploy an ERC721 contract with Remix and OpenZeppelin Wizard. Record:

- NFT contract address;
- token ID;
- mint transaction hash;
- owner after minting.

### Step 5 — Optional advanced NFT quest

If the instructor assigns the full Lab 6 extension:

1. receive or buy the Professor NFT;
2. return or sell it according to the course rules;
3. approve the special contract if required;
4. transfer the personal NFT to the special contract;
5. save every transaction and explain the ownership changes.

## Deliverables

### Required automatic evidence

- course token contract and token transaction hash;
- swap transaction hash;
- personal NFT contract address;
- personal NFT token ID;
- NFT mint transaction hash;
- registered wallet address.

### Optional manual evidence

- Professor NFT receive/buy transaction;
- Professor NFT return/sell transaction;
- approval transaction;
- special contract address;
- transfer-to-special-contract transaction;
- short explanation of the NFT ownership flow.

## Submission

Push the code, notebook, report, or README to the assigned student GitHub repository. Submit the repository and Sepolia explorer links in the Google Classroom assignment.

Do not commit to the course repository. Do not submit student JSON files. The protected registry and the instructor's Google Sheets remain the source of student identity and wallet data.

## Automatic Validation

| Check | Requirement |
|---|---|
| Network | Objective evidence is on Ethereum Sepolia. |
| Wallet | The registered student wallet is involved. |
| Token | Required token activity is found. |
| Swap | Required swap activity is found. |
| NFT | An ERC721 mint to the registered wallet is found. |
| Assignment 1 | PASS only when Token, Swap, and NFT all pass. |

## Manual Review

| Check | Review |
|---|---|
| Professor NFT flow | Receive/buy and return/sell evidence |
| Special contract | Approval and transfer details |
| Explanation | Student can explain token, swap, and NFT events |
| Repository | Code/report quality and reproducibility |

## Grading Rubric

| Criterion | Weight |
|---|---:|
| Token activity | 25% |
| Swap activity | 25% |
| NFT mint | 30% |
| Evidence quality | 10% |
| Explanation and optional NFT quest | 10% |

## Final Checklist

- [ ] Registered Sepolia wallet was used.
- [ ] Required token transaction exists.
- [ ] Required swap transaction exists.
- [ ] Personal NFT was minted to the registered wallet.
- [ ] Contract addresses, token ID, hashes, and links are saved.
- [ ] Repository and explorer links were submitted in Google Classroom.
- [ ] No private keys, seed phrases, passwords, or student JSON files were submitted.
