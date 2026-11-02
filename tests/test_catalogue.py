"""The catalogue's grouping and cards, without the network."""

from __future__ import annotations

import importlib.util
import pathlib
import unittest

spec = importlib.util.spec_from_file_location(
    "catalogue", pathlib.Path(__file__).resolve().parents[1] / "tools/portal/catalogue.py")
catalogue = importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalogue)


def repo(name, topics, docs="", release=None, description="A repository."):
    return {"name": name, "html_url": f"https://github.com/hardfoc/{name}", "description": description,
            "topics": ["hardfoc", *topics], "docs": docs, "release": release}


class CatalogueTest(unittest.TestCase):
    def test_groups(self):
        self.assertEqual(catalogue.group_of(["hardfoc", "library", "driver"]), "library")
        self.assertEqual(catalogue.group_of(["legacy", "driver"]), "legacy")
        self.assertEqual(catalogue.group_of(["hardfoc", "community-health"]), "other")

    def test_render(self):
        out = catalogue.render([
            repo("hf-x-driver", ["driver", "spi"], docs="https://hardfoc.github.io/hf-x-driver/",
                 release=("v1.0.0", "https://github.com/hardfoc/hf-x-driver/releases/tag/v1.0.0")),
            repo("hf-old", ["legacy"], description='Old <"quoted">'),
            repo("hardfoc-vortex-v1", ["firmware"]),
        ])
        self.assertLess(out.index("## Products"), out.index("## Chip drivers"))
        self.assertLess(out.index("## Chip drivers"), out.index("## Legacy"))
        self.assertNotIn("## Board HALs", out)  # empty groups are left out
        self.assertIn('data-topic="spi"', out)
        self.assertNotIn('data-topic="hardfoc"', out)  # on every repository, so not a filter
        self.assertIn(">Release v1.0.0</a>", out)
        self.assertIn("Old &lt;&quot;quoted&quot;&gt;", out)
        self.assertIn('data-total="3"', out)


if __name__ == "__main__":
    unittest.main()
