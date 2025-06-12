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
│   ├── index.md          # Home page
│   └── about.md          # About page
├── mkdocs.yml            # MkDocs configuration
└── .github/workflows/    # CI workflow
```

Pushes to `main` trigger the workflow in `.github/workflows/build-and-deploy.yml`
which builds the site and updates the `gh-pages` branch.

### How the workflow works

1. **Checkout** – pulls the repo so the runner has the docs and config.
2. **Setup Python** – installs a recent Python release for MkDocs.
3. **Install MkDocs** – installs `mkdocs-material` to render the pages.
4. **Build** – `mkdocs build --strict` generates the static site in `./site`.
5. **Publish** – `peaceiris/actions-gh-pages` pushes that folder to the
   `gh-pages` branch and writes the `CNAME` file so GitHub Pages serves
   `https://docs.hardfoc.dev`.
