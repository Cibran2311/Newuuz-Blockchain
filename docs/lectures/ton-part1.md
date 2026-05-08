# TON Part 1 — Architecture and Mental Model

## Key differences from Ethereum

1. TON is asynchronous, not synchronous.
2. TON is natively sharded.
3. Everything is a contract, including wallets.

## Hierarchy

- Masterchain: validator set, workchain configs, shard roots.
- Workchains: independent execution environments.
- Shardchains: parallel execution shards that split and merge under load.

## Cells

A TON cell contains:

- up to 1023 bits;
- up to 4 references to other cells.

Contract code, contract state, messages, and block data are serialized as cells / Bag of Cells.

## Actor model

A TON contract has state, balance, mailbox, and handlers. Contracts communicate only by messages. One user action can trigger a cascade of internal messages.

## Wallets

A TON wallet is itself a smart contract. The wallet verifies signatures, checks seqno, and emits internal messages.

## Jettons

Jettons are TON's fungible token standard. A Jetton Master stores metadata and wallet code; each holder has an individual Jetton Wallet contract.
