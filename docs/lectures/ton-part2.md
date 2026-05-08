# TON Part 2 — Contracts and Interaction

## Learning goals

By the end of this lecture students should be able to:

1. Trace the message cascade for a standard Jetton transfer.
2. Explain wallet v4 checks: deadline, seqno, signature.
3. Recognize deterministic address authentication for Jetton Wallets.
4. Read Jetton Wallet state.
5. Sketch off-chain TypeScript read/write code.

## Wallet v4 behavior

When a signed external message arrives:

1. Check deadline.
2. Check seqno.
3. Verify signature.
4. Call `accept_message`.
5. Fan out internal messages.
6. Increment seqno.

## Jetton transfer cascade

A Jetton transfer usually involves:

1. User wallet receives signed external message.
2. User wallet sends `op::transfer` to sender Jetton Wallet.
3. Sender Jetton Wallet sends `op::internal_transfer` to recipient Jetton Wallet.
4. Recipient Jetton Wallet credits the balance and may notify the owner wallet.
5. Excess TON may be refunded.

## Safety pattern

The recipient Jetton Wallet does not trust arbitrary messages. It recomputes the canonical sender Jetton Wallet address from the owner address, Jetton Master, and wallet code, then checks that the actual sender matches.

## Bounces

If an internal transfer fails after the sender Jetton Wallet has debited balance, the bounce handler restores the balance. This is explicit compensation, not automatic rollback.
