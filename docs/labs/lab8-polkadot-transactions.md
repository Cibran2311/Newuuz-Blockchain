# Mission 8 — Enter Polkadot

## Goal

In this lab you will create a Polkadot account, connect to Westend, receive test tokens, send an extrinsic, and inspect it using Subscan.

---

## Why This Lab Matters

Polkadot is not an Ethereum clone. It uses different account formats, different transaction terminology, and a runtime-based architecture.

In Ethereum you usually submit a transaction. In Polkadot you submit an **extrinsic**.

---

## What You Will Learn

After completing this lab you will be able to:

- install Polkadot.js extension;
- create a Polkadot account;
- understand SS58 addresses;
- connect to Westend;
- submit a transfer extrinsic;
- find extrinsic evidence in Subscan;
- compare Ethereum transactions and Polkadot extrinsics.

---

## Required Reading

| Topic | Link |
|---|---|
| Polkadot documentation | https://docs.polkadot.com/ |
| Polkadot.js extension | https://polkadot.js.org/extension/ |
| Polkadot.js Apps | https://polkadot.js.org/apps/ |
| Westend Subscan | https://westend.subscan.io/ |

---

## Required Software

| Tool | Purpose |
|---|---|
| Polkadot.js Extension | Polkadot wallet |
| Polkadot.js Apps | Web interface for accounts/extrinsics |
| Westend faucet | Get test tokens |
| Westend Subscan | Explorer |

---

## Key Terms

| Term | Meaning |
|---|---|
| `SS58 address` | Polkadot-style account address. |
| `Extrinsic` | External action submitted to the chain. Similar to transaction, but broader. |
| `Westend` | Polkadot test network. |
| `Runtime` | Blockchain logic executed by the chain. |
| `Subscan` | Explorer for Substrate-based chains. |
| `Signer` | Account that signs an extrinsic. |

---

## Safety Notes

!!! warning "Use Westend"
    Do not use Polkadot mainnet DOT.

!!! danger "Never share seed phrase"
    Polkadot accounts also have recovery phrases. Do not upload them to GitHub.

---

## Step-by-Step Instructions

### Step 1 — Install Polkadot.js Extension

Open https://polkadot.js.org/extension/ and install the extension for your browser.

### Step 2 — Create Account

Open extension, click **Create new account**, save the recovery phrase securely, set account name and password, and copy your address.

Expected address format:

```text
5...
```

### Step 3 — Open Polkadot.js Apps

Open https://polkadot.js.org/apps/ and connect the extension.

### Step 4 — Select Westend

In the network selector choose **Westend**.

### Step 5 — Get Westend Tokens

Use the faucet provided by instructor or official faucet if available. Record wallet address and balance.

### Step 6 — Send Transfer

In Polkadot.js Apps, open **Accounts**, find your account, click transfer/send, enter recipient address and amount, then sign and submit.

### Step 7 — Find Extrinsic in Subscan

Open https://westend.subscan.io/ and search by extrinsic hash or account address. Record extrinsic hash, signer, destination, amount, and status.

---

## Expected Result

At the end of this lab you should have a Polkadot.js account, Westend test balance, successful transfer extrinsic, and Subscan link.

---

## Submission

Submit the Westend Subscan extrinsic link in Google Classroom and state the recipient and amount. The signer must match the Polkadot address registered in the protected course registry.

---

## Automatic Validation

| Check | Requirement |
|---|---|
| Network | Extrinsic must be on Westend. |
| Extrinsic | Extrinsic hash exists. |
| Signer | Signer matches submitted wallet. |
| Status | Extrinsic was successful. |
| Transfer | Extrinsic contains expected transfer action. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Using Ethereum address | Use Polkadot SS58 address. |
| Wrong network | Select Westend. |
| Submitting block hash | Submit extrinsic hash. |
| Faucet tokens missing | Wait or use another faucet method. |
| Extension not connected | Allow Polkadot.js Apps access to extension. |

---

## Self-Check Questions

1. What is an extrinsic?
2. How is a Polkadot address different from an Ethereum address?
3. What is Westend?
4. What does Subscan show?
5. Why does Polkadot use runtime logic?
