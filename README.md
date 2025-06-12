# hardfoc.github.io

This repository hosts the documentation site for the hardfoc project. It uses
[MkDocs](https://www.mkdocs.org/) to build the static site and GitHub Pages to
publish it.

## Folder structure

```
.
├── docs/                 # Markdown sources
│   ├── getting-started/
│   ├── api/
│   ├── porting/
│   ├── hardware/
│   └── index.md          # Home page
├── mkdocs.yml            # MkDocs configuration
└── .github/workflows/    # CI workflow
```

Pushes to `main` trigger the workflow in `.github/workflows/build-and-deploy.yml`
which builds the site and updates the `gh-pages` branch.
