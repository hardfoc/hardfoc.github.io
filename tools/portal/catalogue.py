#!/usr/bin/env python3
"""Write the repository catalogue of the portal from the GitHub API, at build time.

    python3 tools/portal/catalogue.py [--out build/portal/catalogue.md] [--metadata FILE]

Sources, in this order of authority:

* ``org/org-metadata.json`` in ``hardfoc/.github``: the organisation's own record of each repository's description
  and topics (fetched from the API, or ``--metadata`` for a local copy);
* the GitHub API: which repositories are public, whether they publish GitHub Pages, their latest release, and the
  description and topics of a public repository the metadata does not list yet.

Only public repositories are listed. The output is Markdown with HTML cards, included by ``docs/repositories.md``
(``--8<-- "build/portal/catalogue.md"``); it is a build product and is not committed. ``GH_TOKEN`` (or
``GITHUB_TOKEN``) raises the API rate limit; ru-mkdocs-publish sets it for its check commands.
"""

from __future__ import annotations

import argparse
import base64
import html
import json
import os
import pathlib
import sys
import urllib.error
import urllib.request

ORG = "hardfoc"
API = "https://api.github.com"
ROOT = pathlib.Path(__file__).resolve().parents[2]

# Groups in reading order: (title, one-line purpose, role topic). A repository goes to the group of the first topic
# of ORDER it carries ("legacy" wins over everything), or to the last group.
GROUPS = [
    ("Products", "Application firmware, one repository per board.", "firmware"),
    ("Core libraries", "The shared platform every board builds on.", "library"),
    ("Board HALs", "One object per board, one manager per board function.", "hal"),
    ("Chip drivers", "Hardware-agnostic C++ drivers: no platform code, a small bus adapter per MCU.", "driver"),
    ("CI and tools", "Reusable workflows, project tooling and the documentation platform.", "ci-tools"),
    ("Documentation and organisation", "The portal, the handbook, diagrams and the organisation profile.", None),
    ("Legacy", "Superseded repositories, kept for history.", "legacy"),
]
ORDER = ["legacy", "firmware", "library", "hal", "driver", "ci-tools"]
HIDDEN_TOPICS = {"hardfoc"}  # on every repository


def api(path: str):
    req = urllib.request.Request(API + path, headers={"Accept": "application/vnd.github+json",
                                                      "X-GitHub-Api-Version": "2022-11-28",
                                                      "User-Agent": "hardfoc-portal"})
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise SystemExit(f"catalogue: GET {path}: HTTP {e.code} {e.reason}") from e


def metadata(path: str | None) -> dict[str, dict]:
    if path:
        doc = json.loads(pathlib.Path(path).read_text())
    else:
        blob = api(f"/repos/{ORG}/.github/contents/org/org-metadata.json")
        if not blob:
            raise SystemExit("catalogue: org/org-metadata.json not found in hardfoc/.github")
        doc = json.loads(base64.b64decode(blob["content"]))
    return {r["repo"]: r for r in doc["repos"]}


def public_repos() -> list[dict]:
    out, page = [], 1
    while True:
        batch = api(f"/orgs/{ORG}/repos?type=public&per_page=100&page={page}") or []
        out += batch
        if len(batch) < 100:
            return out
        page += 1


def group_of(topics: list[str]) -> str:
    for role in ORDER:
        if role in topics:
            return role
    return "other"


def card(r: dict) -> str:
    name = r["name"]
    topics = [t for t in r["topics"] if t not in HIDDEN_TOPICS]
    search = " ".join([name, r["description"], *topics]).lower()
    links = [f'<a href="{r["html_url"]}">Repository</a>']
    if r["docs"]:
        links.append(f'<a href="{r["docs"]}">Documentation</a>')
    if r["release"]:
        tag, url = r["release"]
        links.append(f'<a href="{url}">Release {html.escape(tag)}</a>')
    chips = "".join(f'<button type="button" class="hf-chipbtn" data-topic="{html.escape(t)}">{html.escape(t)}</button>'
                    for t in topics)
    return (
        f'<div class="card hf-repo" data-search="{html.escape(search, quote=True)}" '
        f'data-topics="{html.escape(" ".join(topics), quote=True)}">\n'
        f'<h3 id="repo-{name.lower().replace(".", "-")}"><a href="{r["html_url"]}">{html.escape(name)}</a></h3>\n'
        f'<p>{html.escape(r["description"])}</p>\n'
        f'<p class="hf-repo__topics">{chips}</p>\n'
        f'<p class="hf-repo__links">{" · ".join(links)}</p>\n'
        "</div>"
    )


def render(repos: list[dict]) -> str:
    by_group: dict[str, list[dict]] = {}
    for r in repos:
        by_group.setdefault(group_of(r["topics"]), []).append(r)
    out = [f'<p class="hf-catalogue__count" data-total="{len(repos)}">{len(repos)} public repositories.</p>', ""]
    for title, purpose, role in GROUPS:
        items = sorted(by_group.get(role or "other", []), key=lambda r: r["name"].lower())
        if not items:
            continue
        out += [f'<section class="hf-catalogue__group" markdown="1">', "", f"## {title}", "", purpose, "",
                '<div class="grid hf-catalogue__grid">']
        out += [card(r) for r in items]
        out += ["</div>", "", "</section>", ""]
    return "\n".join(out)


def collect(meta: dict[str, dict]) -> list[dict]:
    repos = []
    for gh in public_repos():
        if gh.get("archived") and "legacy" not in gh.get("topics", []):
            continue
        name = gh["name"]
        m = meta.get(name, {})
        rel = api(f"/repos/{ORG}/{name}/releases/latest")
        repos.append({
            "name": name,
            "html_url": gh["html_url"],
            "description": (m.get("description") or gh.get("description") or "").strip(),
            "topics": m.get("topics") or gh.get("topics") or [],
            "docs": f"https://{ORG}.github.io/{'' if name == f'{ORG}.github.io' else name + '/'}" if gh.get("has_pages") else "",
            "release": (rel["tag_name"], rel["html_url"]) if rel else None,
        })
    return repos


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=pathlib.Path, default=ROOT / "build/portal/catalogue.md")
    ap.add_argument("--metadata", help="a local org-metadata.json instead of the one in hardfoc/.github")
    args = ap.parse_args(argv)
    repos = collect(metadata(args.metadata))
    if not repos:
        raise SystemExit("catalogue: the API returned no public repositories")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(render(repos) + "\n")
    print(f"catalogue: {len(repos)} repositories -> {args.out.relative_to(ROOT) if args.out.is_relative_to(ROOT) else args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
