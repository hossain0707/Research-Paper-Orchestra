#!/usr/bin/env python3
"""Zero-dependency validation of the ChatGPT research workflow package."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = Path("skills/research-paper-orchestra")
REQUIRED_ROLES = (
    "outline-agent.md",
    "plotting-agent.md",
    "literature-agent.md",
    "writing-agent.md",
    "reviewer-agent.md",
)
REQUIRED_SUPPORT = (
    "intake.md",
    "evidence-and-ethics.md",
    "deliverables-and-gates.md",
)


def inspect_repository(root: Path = ROOT) -> list[str]:
    """Return actionable integrity errors without contacting external services."""
    errors: list[str] = []
    manifest_path = root / "plugin.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return [f"plugin.json is missing or invalid: {exc}"]

    if manifest.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        errors.append("Incorrect or missing Agent Plugins schema")
    if manifest.get("name") != "research-paper-orchestra":
        errors.append("Plugin name must be research-paper-orchestra")
    if not re.fullmatch(r"\d+\.\d+\.\d+", str(manifest.get("version", ""))):
        errors.append("Plugin version must be strict MAJOR.MINOR.PATCH")

    ui = manifest.get("extensions", {}).get("com.openai", {}).get("interface", {})
    if ui.get("displayName") != "Research Paper Orchestra":
        errors.append("Missing Research Paper Orchestra displayName")
    short = ui.get("shortDescription", "")
    if not isinstance(short, str) or not 1 <= len(short) <= 30:
        errors.append("shortDescription must contain 1–30 characters")
    if not isinstance(ui.get("defaultPrompt"), (str, list)):
        errors.append("Missing defaultPrompt")
    for key in ("logo", "composerIcon"):
        value = ui.get(key)
        if value and (not isinstance(value, str) or not (root / value).is_file()):
            errors.append(f"Referenced {key} not found: {value}")

    skill_file = root / SKILL_ROOT / "SKILL.md"
    try:
        skill = skill_file.read_text(encoding="utf-8")
    except OSError:
        return errors + ["Missing primary skill SKILL.md"]
    if not skill.startswith("---\n") or "name: research-paper-orchestra" not in skill.split("---", 2)[1]:
        errors.append("Primary skill has invalid or missing YAML frontmatter")
    for term in ("Outline Agent", "Plotting Agent", "Literature Review Agent", "Section Writing Agent", "Reviewer Agent"):
        if term not in skill:
            errors.append(f"Missing role instructions: {term}")

    for ref in (*REQUIRED_ROLES, *REQUIRED_SUPPORT):
        if not (root / SKILL_ROOT / "references" / ref).is_file():
            errors.append(f"Missing reference guide: {ref}")
    if not (root / SKILL_ROOT / "agents" / "openai.yaml").is_file():
        errors.append("Missing agents/openai.yaml")
    if not (root / "LICENSE").is_file():
        errors.append("Missing LICENSE")
    if not (root / "AGENTS.md").is_file():
        errors.append("Missing AGENTS.md")
    return errors


def main() -> int:
    errors = inspect_repository()
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print("PASS: ChatGPT plugin package, five roles, references and metadata")
    print("NOTE: This does not test model quality, citation accuracy or a deployed backend.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
