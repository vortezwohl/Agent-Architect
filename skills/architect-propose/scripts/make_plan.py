"""Create an Architect plan package directory and template files.

This script performs deterministic directory and file creation.
It does not fill template content and allocates the first non-conflicting
plan package name when the requested name is already taken.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


PLAN_NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TEMPLATE_FILES = (
    "00-overview.md",
    "01-context-and-baseline.md",
    "02-compatibility-contract.md",
    "03-architecture-decision.md",
    "04-impact-map.md",
    "05-detailed-design.md",
    "06-task-plan.md",
    "07-verification-plan.md",
    "08-implementation-log.md",
)


def validate_plan_name(plan_name: str) -> None:
    """Validate that the plan name satisfies the kebab-case constraint.

    Args:
        plan_name: User-provided plan name.

    Raises:
        ValueError: Raised when the plan name does not satisfy the constraint.
    """
    if not PLAN_NAME_PATTERN.fullmatch(plan_name):
        raise ValueError(
            "Plan name must be kebab-case and contain only lowercase "
            "letters, numbers, and hyphens."
        )


def copy_templates(templates_root: Path, package_root: Path) -> None:
    """Copy template files into the target plan package directory.

    Args:
        templates_root: Template directory.
        package_root: Target plan package directory.
    """
    for template_name in TEMPLATE_FILES:
        template_path = templates_root / template_name
        target_path = package_root / template_name
        content = template_path.read_text(encoding="utf-8")
        target_path.write_text(content, encoding="utf-8")


def allocate_plan_name(repo_root: Path, plan_name: str) -> tuple[str, Path]:
    """Allocate the first non-conflicting plan package path.

    Args:
        repo_root: Target repository root.
        plan_name: Requested plan package name.

    Returns:
        The allocated plan name and target package path.
    """
    architect_root = repo_root / ".architect"
    candidate_name = plan_name
    suffix = 2
    while True:
        candidate_root = architect_root / candidate_name
        if not candidate_root.exists():
            return candidate_name, candidate_root
        candidate_name = f"{plan_name}-{suffix}"
        suffix += 1


def create_package(repo_root: Path, plan_name: str) -> tuple[str, Path]:
    """Create the plan package directory and write template files.

    Args:
        repo_root: Target repository root.
        plan_name: Requested plan package name.

    Returns:
        The allocated plan name and created plan package directory.

    Raises:
        FileNotFoundError: Raised when the template directory or files are missing.
    """
    templates_root = Path(__file__).resolve().parent.parent / "templates"
    if not templates_root.is_dir():
        raise FileNotFoundError(f"Templates directory not found: {templates_root}")

    (repo_root / ".architect").mkdir(parents=True, exist_ok=True)
    allocated_name, package_root = allocate_plan_name(
        repo_root=repo_root,
        plan_name=plan_name,
    )
    package_root.mkdir()
    copy_templates(templates_root, package_root)
    return allocated_name, package_root


def main() -> int:
    """Parse CLI arguments and create the plan package."""
    parser = argparse.ArgumentParser(
        description="Create an Architect plan package from bundled templates.",
    )
    parser.add_argument("--repo-root", required=True, type=Path)
    parser.add_argument("--plan", required=True)
    arguments = parser.parse_args()

    repo_root = arguments.repo_root.resolve()
    validate_plan_name(arguments.plan)
    allocated_name, package_root = create_package(repo_root, arguments.plan)
    print(f"CREATED: {allocated_name} -> {package_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
