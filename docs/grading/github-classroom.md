# Google Classroom and GitHub

Google Classroom is the student-facing submission channel. GitHub stores code and runs the instructor's checker.

## Student repository

A typical repository can use this structure:

```text
student-repo/
├── notebooks/
├── reports/
├── scripts/
└── README.md
```

The exact repository or profile URL is recorded once in the protected Google Sheets registry. Students submit the relevant link in the Classroom assignment and push their final changes before clicking **Turn in**.

## Instructor workflow

1. Review late or unsubmitted work in Google Classroom.
2. Open the course repository on GitHub.
3. Select **Actions → Blockchain Autotest → Run workflow**.
4. Choose `preview` for a diagnostic run or `final` for the grading snapshot.
5. Choose all checks or one assignment.
6. Open the newly created Google result spreadsheet.
7. Review the `Manual review` and `Errors` worksheets before entering grades in Classroom.

The workflow is manual by design: the instructor controls when a snapshot becomes final.
