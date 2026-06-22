from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]


def project_slug(name: str) -> str:
    slug = name.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "_", slug)
    slug = slug.strip("_")
    return slug or "python_project"


def next_number() -> int:
    numbers = []
    for path in ROOT.iterdir():
        if path.is_dir():
            match = re.match(r"^(\d{2})_", path.name)
            if match:
                numbers.append(int(match.group(1)))
    return max(numbers, default=0) + 1


def main() -> int:
    if len(sys.argv) < 2:
        print("Please provide a project name.")
        print("Example: python scripts/new_project.py guess_number")
        return 1

    name = " ".join(sys.argv[1:])
    folder_name = f"{next_number():02d}_{project_slug(name)}"
    project_dir = ROOT / folder_name

    if project_dir.exists():
        print(f"Project already exists: {project_dir}")
        return 1

    project_dir.mkdir()
    (project_dir / "main.py").write_text(
        'print("Hello from this Python project!")\n',
        encoding="utf-8",
    )
    (project_dir / "README.md").write_text(
        f"# {folder_name}\n\n"
        "这是我的 Python 练习项目。\n\n"
        "## 运行方法\n\n"
        "```bash\n"
        "python main.py\n"
        "```\n",
        encoding="utf-8",
    )

    print(f"Created: {project_dir}")
    print(f"Open {folder_name}/main.py and start coding.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
