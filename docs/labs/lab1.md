# Lab 1 — Creating a Wallet and Sending Your First Transaction

## Goal

In this lab you will create your first blockchain wallet, connect it to the Ethereum Sepolia testnet, receive test ETH, send your first transaction, and inspect it in a blockchain explorer.

This lab is the entry point for the rest of the course. Most future labs will require the same wallet address and the same ability to find transaction evidence in an explorer.

## What You Will Learn

After completing this lab you will be able to:

- install and configure MetaMask;
- create a blockchain wallet;
- explain the difference between a wallet address, private key, and seed phrase;
- connect to Ethereum Sepolia testnet;
- receive test ETH from a faucet;
- send a blockchain transaction;
- find and analyze your transaction in Sepolia Etherscan;
- prepare evidence for automatic grading.

## Key Terms

| Term | Meaning |
|---|---|
| Wallet | Application used to manage blockchain accounts and sign transactions. |
| Address | Public identifier of your account. It starts with `0x` in Ethereum. |
| Private key | Secret value that controls the wallet. Never share it. |
| Seed phrase | Backup phrase used to recover the wallet. Never share it. |
| Testnet | Blockchain network for testing. Testnet tokens have no real monetary value. |
| Sepolia | Ethereum testnet used in this course. |
| Faucet | Website that gives free testnet ETH. |
| Transaction hash | Unique transaction identifier. It is used to find the transaction in an explorer. |
| Etherscan | Blockchain explorer for Ethereum networks. |

## Required Software

Before starting the lab, install:

### Google Chrome or Firefox

Recommended browser:

```text
https://www.google.com/chrome/
```

### MetaMask Extension

Official website:

```text
https://metamask.io/
```

Install only from the official website or browser extension store.

!!! warning
    Never install wallet extensions from random links, Telegram messages, or unofficial websites.

## Required Links

Use these links during the lab:

| Resource | Link |
|---|---|
| MetaMask | https://metamask.io/ |
| Sepolia Etherscan | https://sepolia.etherscan.io/ |
| Google Cloud Sepolia Faucet | https://cloud.google.com/application/web3/faucet/ethereum/sepolia |
| Alchemy Sepolia Faucet | https://www.alchemy.com/faucets/ethereum-sepolia |
| QuickNode Sepolia Faucet | https://faucet.quicknode.com/ethereum/sepolia |
| Ethereum Accounts Documentation | https://ethereum.org/en/developers/docs/accounts/ |
| Ethereum Transactions Documentation | https://ethereum.org/en/developers/docs/transactions/ |

## Safety Rules

Before creating the wallet, remember:

!!! danger
    Never publish your seed phrase, private key, or MetaMask password.

!!! danger
    Do not upload screenshots containing your seed phrase.

!!! info
    In this course you should use testnets only. Do not use real ETH or mainnet transactions unless explicitly instructed.

## Task 1 — Install MetaMask

1. Open the official MetaMask website:

```text
https://metamask.io/
```

2. Click **Download**.
3. Select your browser.
4. Install the browser extension.
5. After installation, pin MetaMask in the browser toolbar if possible.

### Expected Result

You should see the MetaMask fox icon in your browser toolbar.

## Task 2 — Create a New Wallet

1. Open MetaMask.
2. Click **Get Started**.
3. Select **Create a new wallet**.
4. Create a local password.
5. MetaMask will show your **Secret Recovery Phrase**.
6. Write the phrase down on paper or store it securely offline.
7. Confirm the recovery phrase in MetaMask.

!!! warning
    Your password only unlocks MetaMask on this browser. The seed phrase controls the wallet itself. If you lose the seed phrase, you may lose access to the wallet.

### Expected Result

MetaMask should show an account similar to:

```text
Account 1
0x1234...abcd
```

Copy this address. You will use it in `submission.json`.

## Task 3 — Enable Sepolia Test Network

By default, MetaMask may hide test networks.

1. Open MetaMask.
2. Click the network selector at the top.
3. If you do not see **Sepolia**, open:

```text
Settings → Advanced → Show test networks
```

4. Turn **Show test networks** on.
5. Return to the network selector.
6. Choose **Sepolia**.

### Expected Result

MetaMask should display **Sepolia** as the active network.

!!! warning
    Check the network carefully. Do not send transactions on Ethereum Mainnet.

## Task 4 — Receive Sepolia ETH from a Faucet

You need test ETH to pay gas fees.

1. Copy your wallet address from MetaMask.
2. Open one of the faucets:

```text
https://cloud.google.com/application/web3/faucet/ethereum/sepolia
```

or

```text
https://www.alchemy.com/faucets/ethereum-sepolia
```

or

```text
https://faucet.quicknode.com/ethereum/sepolia
```

3. Paste your wallet address.
4. Request Sepolia ETH.
5. Wait until the balance appears in MetaMask.

### Expected Result

Your MetaMask balance on Sepolia should be greater than zero.

Example:

```text
0.05 SepoliaETH
```

## Task 5 — Send Your First Transaction

Send a small amount of Sepolia ETH to the instructor wallet or to the address specified by the instructor.

If no instructor address is provided during class, use your second test wallet or wait for the official address.

### Transaction Parameters

| Field | Value |
|---|---|
| Network | Sepolia |
| Amount | `0.0001 ETH` |
| Recipient | instructor wallet / assigned address |

### Steps

1. Open MetaMask.
2. Make sure the selected network is **Sepolia**.
3. Click **Send**.
4. Paste the recipient address.
5. Enter:

```text
0.0001 ETH
```

6. Click **Next**.
7. Review the transaction.
8. Click **Confirm**.
9. Wait until the transaction is confirmed.

### Expected Result

MetaMask should show the transaction as completed or confirmed.

## Task 6 — Find the Transaction in Etherscan

1. Open MetaMask activity history.
2. Click your transaction.
3. Click **View on block explorer**.

Alternatively, open:

```text
https://sepolia.etherscan.io/
```

and paste your transaction hash into the search bar.

### Find and Record

On the transaction page find:

- transaction hash;
- status;
- block number;
- sender address (`From`);
- receiver address (`To`);
- value;
- gas limit;
- gas used;
- transaction fee.

### Expected Result

The transaction status should be:

```text
Success
```

## Task 7 — Fill `submission.json`

Create or update the file `submission.json` in your GitHub Classroom repository.

Use this structure:

```json
{
  "student": {
    "full_name": "Your Name",
    "student_id": "000000",
    "github_username": "your-github-username"
  },
  "wallets": {
    "ethereum_sepolia": "0xYourWalletAddress"
  },
  "labs": {
    "lab1": {
      "network": "sepolia",
      "wallet": "0xYourWalletAddress",
      "recipient": "0xRecipientAddress",
      "amount_eth": "0.0001",
      "tx_hash": "0xTransactionHash",
      "explorer_url": "https://sepolia.etherscan.io/tx/0xTransactionHash"
    }
  }
}
```

!!! warning
    Make sure the JSON is valid. Missing commas, extra comments, or broken quotes will cause automatic validation to fail.

## Deliverables

Submit through GitHub Classroom:

- updated `submission.json`;
- transaction hash;
- Sepolia Etherscan link.

No screenshots are required unless the instructor asks for them.

## Automatic Validation

The checker will verify:

| Check | Requirement |
|---|---|
| JSON validity | `submission.json` must be valid JSON. |
| Network | Transaction must be on Sepolia. |
| Transaction existence | `tx_hash` must exist in Sepolia RPC / Etherscan. |
| Status | Transaction must be successful. |
| Sender | Transaction sender must match submitted wallet. |
| Amount | Transaction value must match the required amount or be within accepted range. |
| Deadline | Transaction must be submitted before the deadline if deadline checking is enabled. |

## Common Mistakes

| Mistake | How to Fix |
|---|---|
| Sent transaction on Ethereum Mainnet | Use Sepolia only. Check network before sending. |
| Faucet does not send ETH | Try another faucet or wait for rate limit reset. |
| Transaction is pending for too long | Wait or check Sepolia network status. |
| Wrong recipient address | Copy address carefully and verify first/last characters. |
| Lost seed phrase | Create a new wallet for the course and store the phrase safely. |
| Submitted private key or seed phrase | Remove it immediately and create a new wallet. |
| Invalid JSON | Validate the file using an online JSON validator or IDE. |

## Questions for Self-Check

Answer these questions after completing the lab:

1. What is the difference between a wallet address and a private key?
2. Why do we use Sepolia instead of Ethereum Mainnet?
3. What is a transaction hash?
4. What does transaction status `Success` mean?
5. What is gas used for?

## Additional Reading

- Ethereum Accounts: https://ethereum.org/en/developers/docs/accounts/
- Ethereum Transactions: https://ethereum.org/en/developers/docs/transactions/
- MetaMask Support: https://support.metamask.io/
- Sepolia Etherscan: https://sepolia.etherscan.io/
