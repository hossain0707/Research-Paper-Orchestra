"""Offline validation for the ChatGPT plugin source package."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.validate_plugin import inspect_repository, REQUIRED_ROLES  # noqa: E402


class RepositoryStructureTests(unittest.TestCase):
    def test_plugin_structure(self):
        self.assertEqual([], inspect_repository(ROOT))

    def test_all_five_agent_guides_are_present(self):
        guides = ROOT / "skills/research-paper-orchestra/references"
        self.assertEqual(5, len(REQUIRED_ROLES))
        for filename in REQUIRED_ROLES:
            with self.subTest(role=filename):
                self.assertGreater((guides / filename).stat().st_size, 100)

    def test_manifest_is_valid_json(self):
        data = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual("research-paper-orchestra", data["name"])
        self.assertEqual("1.0.0", data["version"])

    def test_readme_states_implementation_limits(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
        self.assertIn("not", readme)
        self.assertIn("google", readme)
        self.assertIn("chatgpt", readme)

    def test_no_automated_actions_in_repo(self):
        self.assertFalse((ROOT / ".github/workflows").exists())


if __name__ == "__main__":
    unittest.main()
