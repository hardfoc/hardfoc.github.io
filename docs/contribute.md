# Contribute

How to report a problem, propose a change and report a vulnerability, for every HardFOC repository.

## Report a problem or ask a question

Open an issue in the repository closest to the problem: the driver for a chip, the HAL for a board, the product
for the application. If you cannot tell, open it in the product and say what you saw.

## Propose a change

| Step | Where |
| --- | --- |
| Read the rules for branches, commits, pull requests and the CI gate | [CONTRIBUTING.md](https://github.com/hardfoc/.github/blob/main/CONTRIBUTING.md) |
| Follow the code of conduct | [CODE_OF_CONDUCT.md](https://github.com/hardfoc/.github/blob/main/CODE_OF_CONDUCT.md) |
| Write documentation to the shared standard | [Documentation style guide](https://hardfoc.github.io/hf-general-ci-tools/latest/DOCS-STYLE-GUIDE/) |
| Add CI to a repository | [CI quickstart](https://hardfoc.github.io/hf-general-ci-tools/latest/quickstart/) |

A repository with its own `CONTRIBUTING.md` follows that file instead.

## Report a vulnerability

!!! danger "Never in public"
    Do not open a public issue, pull request or discussion for a suspected vulnerability.

Report it privately with a GitHub security advisory: in the affected repository, **Security** > **Advisories** >
**Report a vulnerability**. The [security policy](https://github.com/hardfoc/.github/blob/main/SECURITY.md) says
what to include and what is in scope.

## This site

The portal is [`hardfoc/hardfoc.github.io`](https://github.com/hardfoc/hardfoc.github.io). The repository list is
built from the GitHub API and the organisation's repository record each time the site is published; to change a
description or topics, change
[`org/org-metadata.json`](https://github.com/hardfoc/.github/blob/main/org/org-metadata.json) in `hardfoc/.github`.
