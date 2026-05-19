# Assignment 4 — Technical Article Publication

## Overview

Students publish a technical article based on their course experience. The article should not be a generic blockchain overview. It must be connected to practical work, architecture comparison, security analysis, DeFi, NFTs, TON, Polkadot, or Ethereum.

## Learning outcomes

Students should be able to:

- explain blockchain concepts clearly;
- connect theory with practical experiments;
- cite credible sources;
- present transaction evidence or technical diagrams;
- communicate technical results publicly.

## Suggested topics

Students may choose one of the following:

- how ERC20, Jettons, and Polkadot assets differ;
- Ethereum vs TON transaction model;
- Ethernaut vulnerability analysis;
- constant product AMM and DEX arbitrage;
- NFT ownership and smart contract traps;
- XCM and cross-chain communication;
- why TON uses asynchronous message cascades;
- how blockchain assignments can be automatically graded;
- building a verifiable on-chain portfolio for students.

## Article requirements

Minimum requirements:

- published on Medium, dev.to, Hashnode, Habr, HackerNoon, or a comparable technical platform;
- at least 1,500 words or approximately 6 minutes reading time;
- at least 3 credible references;
- at least one technical diagram, formula, code snippet, or transaction trace;
- clear conclusion with student observations.

## Required structure

Recommended article structure:

1. **Introduction** — what problem or concept is being explained.
2. **Background** — relevant blockchain concepts.
3. **Practical experiment** — what the student did.
4. **Evidence** — transaction hashes, contract addresses, screenshots, or diagrams.
5. **Analysis** — what the evidence shows.
6. **Comparison or lessons learned** — why it matters.
7. **Conclusion** — final technical takeaway.

## Required `submission.json` fields

```json
{
  "assignment_id": "assignment4_technical_article",
  "student": {
    "full_name": "Ivan Ivanov",
    "student_id": "123456"
  },
  "article": {
    "title": "Ethereum vs TON: Transaction Models Compared",
    "url": "https://...",
    "platform": "Medium",
    "estimated_reading_time_minutes": 6,
    "topic": "architecture_comparison"
  },
  "evidence": {
    "referenced_transactions": ["0x..."],
    "referenced_contracts": ["0x..."]
  }
}
```

## Validation plan

The checker may verify:

- URL is reachable;
- platform is recognized;
- article length is sufficient;
- references are present;
- blockchain evidence is included.

Technical quality may require instructor or LLM-assisted review.

## Grading rubric

| Criterion | Weight |
|---|---:|
| Technical accuracy | 30% |
| Structure and readability | 25% |
| Practical evidence and examples | 20% |
| References and diagrams/formulas/code | 15% |
| Publication quality | 10% |
