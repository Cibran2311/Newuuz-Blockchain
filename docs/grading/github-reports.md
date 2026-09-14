# GitHub Reports

GitHub stores each student's code, supporting files, and structured course report.

## Recommended repository

```text
student-repo/
├── submission.json
├── notebooks/
├── reports/
├── scripts/
└── README.md
```

The exact public repository URL is registered once in Google Sheets. The checker reads the root `submission.json` from a pinned commit, so a later push cannot silently change the evidence attached to an earlier run.

One JSON file covers all 12 labs and all 4 assignments. Longer reports remain normal Markdown, notebook, code, or article files and are linked from the corresponding JSON section.

## Instructor workflow

1. Close or protect the registry after the allowed wallet/repository update period.
2. Run a targeted `preview` while students are working.
3. Run `final` after the deadline.
4. Review `Manual review` and `Errors`.
5. Record a decision, score, and comment in the persistent instructor columns.
6. Keep or download the workflow artifact when an immutable machine-readable audit copy is required.
