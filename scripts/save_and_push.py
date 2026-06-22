from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def run(command: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    print("$ " + " ".join(command))
    result = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if result.stdout:
        print(result.stdout, end="")
    if check and result.returncode != 0:
        raise SystemExit(result.returncode)
    return result


def main() -> int:
    message = " ".join(sys.argv[1:]).strip() or "Update Python projects"

    status = run(["git", "status", "--short"], check=True)
    if not status.stdout.strip():
        print("Nothing changed. No commit needed.")
        return 0

    run(["git", "add", "."])
    commit = run(["git", "commit", "-m", message], check=False)
    if commit.returncode != 0:
        print("Commit failed. Please check the message above.")
        return commit.returncode

    run(["git", "push"])
    print("Saved and pushed to GitHub.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
