# How to Submit

Most course work is submitted through GitHub Classroom.

## Repository structure

A typical student repository should look like:

```text
student-repo/
├── submission.json
├── notebooks/
├── reports/
├── scripts/
└── README.md
```

## Submission workflow

1. Accept GitHub Classroom assignment.
2. Clone or open the repository.
3. Complete the lab or assignment.
4. Save transaction hashes and explorer links.
5. Update `submission.json`.
6. Commit and push.
7. Open GitHub Actions.
8. Check whether the checker passed.

## Basic Git commands

```bash
git status
git add submission.json
git commit -m "submit lab evidence"
git push
```

## If GitHub Actions fails

Read the error message. Common causes:

- invalid JSON;
- missing field;
- wrong transaction hash;
- wrong network;
- transaction not found yet;
- wallet mismatch.
