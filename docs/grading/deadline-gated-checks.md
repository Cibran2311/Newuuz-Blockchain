# Preview and Final Checks

The GitHub Actions workflow has two instructor-selected modes.

| Mode | Use |
|---|---|
| `preview` | Diagnose missing data, API failures, and incomplete evidence without treating the output as a final snapshot |
| `final` | Update the result spreadsheet used for grading review |

Both modes run the same evidence checks. The `Run mode` column and `Run history` worksheet keep preview and final runs distinguishable.

The workflow does not contain a hard-coded course deadline. Google Classroom remains the source for due dates, late status, and whether a student turned in the assignment. The instructor starts the final check after the deadline and reviews exceptions before publishing grades.
