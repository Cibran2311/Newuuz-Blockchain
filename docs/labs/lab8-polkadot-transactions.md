# Mission 8 — Enter Polkadot

## Goal

In this lab you will create a Polkadot account, connect to Westend, receive test tokens, send an extrinsic, and inspect it using Subscan.

---

## Why This Lab Matters

Polkadot is not an Ethereum clone. It uses different account formats, different transaction terminology, and a runtime-based architecture.

In Ethereum you usually submit a transaction.  
In Polkadot you submit an **extrinsic**.

This lab introduces the practical user flow for Polkadot.

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

Open:

```text
https://polkadot.js.org/extension/
```

Install the extension for your browser.

---

### Step 2 — Create Account

1. Open the extension.
2. Click **Create new account**.
3. Save the recovery phrase securely.
4. Set account name.
5. Set password.
6. Copy your account address.

Expected address format:

```text
5...
```

---

### Step 3 — Open Polkadot.js Apps

Open:

```text
https://polkadot.js.org/apps/
```

Connect the extension.

---

### Step 4 — Select Westend

In the network selector choose:

```text
Westend
```

If the interface asks for permission, allow your account to connect.

---

### Step 5 — Get Westend Tokens

Use the faucet provided by instructor or official faucet if available.

Record:

- wallet address;
- faucet transaction/extrinsic if visible;
- current balance.

---

### Step 6 — Send Transfer

In Polkadot.js Apps:

1. Open **Accounts**.
2. Find your account.
3. Click **Send** or transfer button.
4. Enter recipient address.
5. Enter small amount.
6. Sign and submit.

---

### Step 7 — Find Extrinsic in Subscan

Open:

```text
https://westend.subscan.io/
```

Search by extrinsic hash or account address.

Record:

- extrinsic hash;
- signer;
- destination;
- amount;
- status.

---

## Expected Result

At the end of this lab you should have:

- Polkadot.js account;
- Westend test balance;
- successful transfer extrinsic;
- Subscan link;
- updated `submission.json`.

---

## Submission

Add this fragment to `submission.json`:

```json
{
  "labs": {
    "lab8": {
      "network": "westend",
      "polkadot_wallet": "5YourAddress",
      "recipient": "5RecipientAddress",
      "extrinsic_hash": "0xExtrinsicHash",
      "explorer_url": "https://westend.subscan.io/extrinsic/0xExtrinsicHash"
    }
  }
}
```

---

## Automatic Validation

The checker will verify:

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
