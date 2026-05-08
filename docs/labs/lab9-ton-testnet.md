# Lab 9 — TON Testnet

## Goal

Set up a TON testnet wallet, send TON, transfer a Jetton, and perform a STON.fi testnet swap.

## Tasks

### Pre-stage — Wallet setup

1. Install Tonkeeper browser extension.
2. Create a wallet and write the seed phrase on paper.
3. Enable testnet mode.
4. Get test TON from `@testgiver_ton_bot`.
5. Confirm balance in Tonkeeper.

### Task 1 — TON transfer

1. Exchange testnet addresses with a partner.
2. Send `0.01 TON` with a short comment.
3. Open the transaction on `testnet.tonviewer.com`.

### Task 2 — Jetton transfer

1. Import the test Jetton using the master address provided by the instructor.
2. Transfer a small amount to your partner.
3. Locate sender and recipient Jetton Wallet contracts in Tonviewer.

### Task 3 — STON.fi swap

Write a script that performs a TON → Jetton swap on STON.fi testnet.

Required packages:

```bash
mkdir ston-swap && cd ston-swap
npm init -y
npm install @ston-fi/sdk @ton/ton @ton/crypto
```

Use testnet contracts only. Do not use the mainnet `api.ston.fi` / `StonApiClient` for this task.

## Deliverables

- TON transfer Tonviewer link.
- Jetton transfer Tonviewer link.
- Jetton master address.
- Sender Jetton Wallet address.
- Recipient Jetton Wallet address.
- Swap script as a single `.ts` or `.js` file.
- Tonviewer link to the swap transaction trace.
