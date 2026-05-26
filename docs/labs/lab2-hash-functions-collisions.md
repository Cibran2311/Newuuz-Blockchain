# Lab 2 — Hash Functions and Collision Analysis

## Goal

Implement a simplified hash function and find a collision.

## What You Will Learn

After completing this lab you will be able to:

- interact with blockchain infrastructure;
- use required tools and explorers;
- save transaction or computation evidence;
- fill `submission.json` correctly.

## Required Materials

Open these materials before starting:

- Google Colab: https://colab.research.google.com/
- Python hashlib: https://docs.python.org/3/library/hashlib.html

## Step-by-Step Instructions

### Step 1 — Open Python environment

Use Google Colab, Jupyter, or local Python.
### Step 2 — Implement simplified hash

Write a function with a small output range.
### Step 3 — Find collision

Find two different inputs with the same output.
### Step 4 — Compare with SHA-256

Use `hashlib.sha256()` and explain why collisions are hard for SHA-256.

## Submission

Add the result to `submission.json`.

```json
{
  "labs": {"lab2": {"input_1": "123", "input_2": "321", "hash_1": "42", "hash_2": "42"}}
}
```

## Automatic Validation

The checker verifies:

- submitted evidence exists;
- network is correct;
- wallet belongs to the student;
- transaction or computation result is valid.

## Common Mistakes

- using the wrong network;
- submitting another wallet's transaction;
- breaking JSON syntax;
- forgetting explorer links;
- submitting private keys or seed phrases.
