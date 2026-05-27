# Mission 11 — Dissect a Jetton Transfer

## Goal

In this lab you will work with TON jettons and understand why TON token architecture differs from ERC20.

---

## Why This Lab Matters

In Ethereum ERC20, balances are usually stored inside one token contract.

In TON, jettons use a different architecture:

```text
Jetton Master
    ↓
Jetton Wallet for holder A
Jetton Wallet for holder B
Jetton Wallet for holder C
```

This design fits TON’s asynchronous and sharded architecture.

---

## What You Will Learn

After completing this lab you will be able to:

- explain what a jetton is;
- distinguish Jetton Master and Jetton Wallet;
- send jettons;
- inspect TON message traces;
- compare ERC20 and jettons;
- identify sender and recipient Jetton Wallet contracts.

---

## Required Reading

| Topic | Link |
|---|---|
| TON documentation | https://docs.ton.org/ |
| TON token contracts | https://github.com/ton-blockchain/token-contract |
| Testnet Tonviewer | https://testnet.tonviewer.com/ |
| Tonkeeper | https://tonkeeper.com/ |

---

## Required Software

| Tool | Purpose |
|---|---|
| Tonkeeper | TON wallet |
| Test jetton | Token used in lab |
| Testnet Tonviewer | Inspect jetton transfer |
| Instructor faucet/minter | Receive class jettons |

---

## Key Terms

| Term | Meaning |
|---|---|
| `Jetton` | TON fungible token standard. |
| `Jetton Master` | Contract storing token metadata and wallet code. |
| `Jetton Wallet` | Per-holder contract storing jetton balance. |
| `Internal message` | Contract-to-contract message in TON. |
| `Trace` | Sequence of messages shown by explorer. |
| `Mint` | Create new jetton tokens. |

---

## Safety Notes

!!! warning "Use testnet jettons only"
    Do not use real TON assets.

!!! info
    Your TON wallet and your Jetton Wallet are not the same address.

---

## Step-by-Step Instructions

### Step 1 — Prepare TON Testnet Wallet

Use the wallet from Lab 10. Make sure testnet mode is enabled and wallet has test TON for fees.

### Step 2 — Receive Test Jettons

The instructor will provide Jetton Master address, minter link, transfer from faucet, or class distribution.

### Step 3 — Open Jetton in Wallet

Check that the jetton appears. Record Jetton name, Jetton Master address, and your wallet address.

### Step 4 — Send Jettons

Send a small jetton amount to instructor, another student, or assigned recipient. Save transaction link.

### Step 5 — Inspect Trace in Tonviewer

Open transaction in testnet Tonviewer. Look for sender wallet, recipient wallet, Jetton Master, sender Jetton Wallet, recipient Jetton Wallet, and internal messages.

### Step 6 — Explain the Architecture

Write a short explanation:

```text
In TON, each holder has a separate Jetton Wallet contract.
The Jetton Master stores metadata and wallet code.
A jetton transfer creates messages between wallet contracts.
```

---

## Expected Result

At the end of this lab you should have Jetton Master address, sender Jetton Wallet address, recipient Jetton Wallet address, jetton transfer transaction link, and short architecture explanation.

---

## Submission

```json
{
  "labs": {
    "lab11": {
      "network": "ton_testnet",
      "ton_wallet": "kQYourWallet",
      "jetton_master": "kQJettonMaster",
      "sender_jetton_wallet": "kQSenderJettonWallet",
      "recipient_jetton_wallet": "kQRecipientJettonWallet",
      "tx_link": "https://testnet.tonviewer.com/...",
      "explanation": "Jetton Master stores metadata, Jetton Wallet stores holder balance."
    }
  }
}
```

---

## Automatic Validation

| Check | Requirement |
|---|---|
| Network | Evidence is from TON testnet. |
| Jetton transfer | Transfer exists. |
| Sender | Sender wallet matches submitted wallet. |
| Jetton Master | Address is present. |
| Jetton Wallets | Sender and recipient wallet addresses are present. |
| Explanation | Architecture explanation is present. |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Confusing TON wallet and Jetton Wallet | Record both addresses separately. |
| Submitting native TON transfer | Submit jetton transfer. |
| Wrong network | Use testnet. |
| No trace | Open transaction in Tonviewer and inspect messages. |
| Missing Jetton Master | Find token root/master contract. |

---

## Self-Check Questions

1. How is a jetton different from ERC20?
2. What does Jetton Master store?
3. Why does each holder have a Jetton Wallet?
4. What is an internal message?
5. How does Tonviewer show a jetton transfer?
