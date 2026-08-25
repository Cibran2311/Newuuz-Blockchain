# How to Submit

All work is submitted through the assignment created in Google Classroom. There is no student submission JSON file.

## Before the first submission

Confirm with the instructor that the protected course registry contains your current:

- student ID and Classroom email;
- GitHub profile or repository;
- Sepolia wallet;
- Polkadot and TON testnet wallets when a task uses them.

Only activity from registered addresses can be matched automatically.

## Submission workflow

1. Open the assignment in Google Classroom.
2. Complete the lab in the required testnet.
3. Push code, notebooks, and reports to the assigned GitHub repository.
4. Attach or paste the repository, notebook, explorer, or article link requested by the task.
5. Add a short note if the transaction used a newly registered wallet.
6. Click **Turn in**.

The instructor runs the course checker from GitHub Actions. It reads the protected registry, verifies available GitHub and on-chain evidence, and creates a new result spreadsheet.

## If the result needs review

The instructor checks the `Manual review` and `Errors` worksheets. Common reasons are:

- the wallet or GitHub repository is not registered;
- the wrong testnet was used;
- an explorer or RPC service was temporarily unavailable;
- the evidence is qualitative and cannot be graded safely by a script;
- the transaction has not been indexed yet.

!!! danger
    Never submit a seed phrase, private key, wallet password, or API key through Classroom, GitHub, or Google Sheets.
