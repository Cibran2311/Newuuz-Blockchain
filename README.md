# CS422/CS423 Blockchain Technologies

Markdown/MkDocs version of the Blockchain Technologies course.

## Local preview

```bash
pip install mkdocs-material pymdown-extensions
mkdocs serve
```

Open `http://127.0.0.1:8000`.

## GitHub Pages deployment

1. Push this repository to GitHub.
2. Go to **Settings → Pages**.
3. Choose **Deploy from a branch**.
4. Select branch **gh-pages**, folder **/**.
5. The included GitHub Actions workflow will build and publish the site after every push to `main`.

Before publishing, edit `mkdocs.yml` and replace `repo_url` with your actual repository URL.


## Assignment reporting

Student repositories should include `submission.json` in the root. See `docs/templates/json-submission-format.md` and `submission.example.json`.
