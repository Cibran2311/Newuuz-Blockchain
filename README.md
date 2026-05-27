# CS422/CS423 Blockchain Technologies

Final MkDocs Material course site for the Blockchain Technologies course.

## Structure

```text
docs/
├── course/
├── sections/
├── labs/
├── assignments/
├── grading/
├── references/
└── resources/
```

## Local preview

```bash
python -m pip install -r requirements.txt
mkdocs serve
```

Open:

```text
http://127.0.0.1:8000
```

## Build

```bash
mkdocs build --strict
```

## GitHub Pages

1. Push the repository to GitHub.
2. Open **Settings → Pages**.
3. Select **Source → GitHub Actions**.
4. Run **Actions → Deploy MkDocs**.

## Notes

- Labs are organized by technical sections.
- Assignments are separated into their own top-level section.
- Students submit evidence through `submission.json`.
- Testnets only.
