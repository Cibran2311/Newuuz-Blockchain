# GitHub Classroom Integration

Students submit assignments through GitHub Classroom repositories.

## Repository Structure

```text
student-repo/
├── submission.json
├── reports/
├── notebooks/
└── scripts/
```

## GitHub Actions

The checker automatically validates:

- JSON structure;
- blockchain transactions;
- assignment completion;
- deadlines.

## Suggested workflow

- `push`: practice check;
- `workflow_dispatch`: instructor final check;
- `schedule`: automatic deadline-based check.
