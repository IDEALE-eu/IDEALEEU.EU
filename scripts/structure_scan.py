"""
Structure scan: list
1) Open points = directories that lack a README and any packaging marker.
2) End path points = leaf files printed as full path + name + extension.

Outputs:
  structure-scan-report/open_points.txt
  structure-scan-report/end_points.txt
Optional:
  --json structure-scan-report/report.json

Usage example:
  python3 scripts/structure_scan.py \
    --repo-root . \
    --markers pyproject.toml setup.py requirements.txt package.json CMakeLists.txt Makefile .gitmodules \
    --readme-names README.md README.rst README.txt
"""

from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
from typing import Iterable, Set, List


DEFAULT_SKIP_DIRS = {
    ".git", ".github", ".venv", "venv", "__pycache__", "node_modules",
    "dist", "build", ".mypy_cache", ".pytest_cache", ".ruff_cache",
    ".tox", ".idea", ".vscode", ".DS_Store"
}

DEFAULT_READMES = ["README.md", "README.rst", "README.txt"]
DEFAULT_MARKERS = ["pyproject.toml", "setup.py", "requirements.txt",
                   "package.json", "CMakeLists.txt", "Makefile", ".gitmodules"]


def normalize(p: Path) -> str:
    return p.as_posix()


def is_hidden_anywhere(p: Path) -> bool:
    # True if any segment starts with '.' except repo root segments '.' or '..'
    return any(part.startswith('.') and part not in ('.', '..') for part in p.parts)


def load_ignore_globs(ignore_file: Path) -> List[str]:
    if not ignore_file.exists():
        return []
    globs: List[str] = []
    for line in ignore_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        globs.append(line)
    return globs


def matches_any_glob(rel_path: str, patterns: Iterable[str]) -> bool:
    # Use pathlib.match on POSIX style path
    rp = Path(rel_path)
    for pat in patterns:
        if rp.match(pat):
            return True
    return False


def scan(
    root: Path,
    readme_names: Set[str],
    markers: Set[str],
    skip_dirs: Set[str],
    include_hidden: bool,
    extra_ignores: List[str],
) -> tuple[List[str], List[str]]:
    open_points: List[str] = []
    end_points: List[str] = []

    for dirpath, dirnames, filenames in os.walk(root):
        here = Path(dirpath)
        rel_dir = here.relative_to(root)
        rel_dir_posix = normalize(rel_dir) if str(rel_dir) != "." else ""

        # prune directories
        pruned: List[str] = []
        for d in list(dirnames):
            if d in skip_dirs:
                continue
            if not include_hidden and d.startswith("."):
                # keep .github so we can evaluate markers there if wanted, but skip by default
                if d != ".github":
                    continue
            pruned.append(d)
        dirnames[:] = pruned  # mutate for os.walk

        # skip this directory entirely by glob rules
        if rel_dir_posix and matches_any_glob(rel_dir_posix, extra_ignores):
            # prevent descending
            dirnames[:] = []
            continue

        files_set = set(filenames)

        # End points: file paths with extension, respect ignore and hidden flags
        for f in filenames:
            p = here / f
            relp = p.relative_to(root)
            relp_posix = normalize(relp)
            if not include_hidden and is_hidden_anywhere(relp):
                continue
            if matches_any_glob(relp_posix, extra_ignores):
                continue
            if p.is_file() and p.suffix:
                end_points.append(relp_posix)

        # Open points: non-empty dirs without README and without any marker
        nontrivial = bool(files_set or dirnames)
        has_readme = any(name in files_set for name in readme_names)
        has_marker = any(m in files_set for m in markers)

        # compute open if nontrivial and not hidden and not ignored
        if nontrivial and not has_readme and not has_marker:
            # exclude .github from "open" by default as it often lacks README
            if rel_dir_posix in ("", ".github"):
                pass
            else:
                if include_hidden or not is_hidden_anywhere(rel_dir):
                    open_points.append(rel_dir_posix)

    # dedupe and sort
    open_points = sorted({p for p in open_points if p})
    end_points = sorted(set(end_points))
    return open_points, end_points


def main() -> int:
    ap = argparse.ArgumentParser(description="Scan repository structure.")
    ap.add_argument("--repo-root", default=".", help="Path to repo root.")
    ap.add_argument("--markers", nargs="*", default=DEFAULT_MARKERS,
                    help="Filenames that count as packaging/structure markers.")
    ap.add_argument("--readme-names", nargs="*", default=DEFAULT_READMES,
                    help="README filenames to check for presence.")
    ap.add_argument("--skip-dirs", nargs="*", default=sorted(DEFAULT_SKIP_DIRS),
                    help="Directory names to skip entirely.")
    ap.add_argument("--include-hidden", action="store_true",
                    help="Include hidden files and folders in evaluation.")
    ap.add_argument("--ignore-glob", nargs="*", default=[],
                    help="Glob patterns to ignore, e.g. docs/_build/** third_party/**")
    ap.add_argument("--ignore-file", default="structure-scan.ignore",
                    help="Optional file with newline-separated glob patterns.")
    ap.add_argument("--json", default="", help="Optional JSON report output path.")
    args = ap.parse_args()

    root = Path(args.repo_root).resolve()
    if not root.exists():
        print(f"Repo root not found: {root}")
        return 2

    readme_names = set(args.readme_names)
    markers = set(args.markers)
    skip_dirs = set(args.skip_dirs)

    extra_ignores = list(args.ignore_glob)
    ignore_file = Path(args.ignore_file)
    extra_ignores.extend(load_ignore_globs(ignore_file))

    open_points, end_points = scan(
        root=root,
        readme_names=readme_names,
        markers=markers,
        skip_dirs=skip_dirs,
        include_hidden=bool(args.include_hidden),
        extra_ignores=extra_ignores,
    )

    out_dir = root / "structure-scan-report"
    out_dir.mkdir(exist_ok=True)

    (out_dir / "open_points.txt").write_text(
        "\n".join(open_points) + ("\n" if open_points else ""),
        encoding="utf-8"
    )
    (out_dir / "end_points.txt").write_text(
        "\n".join(end_points) + ("\n" if end_points else ""),
        encoding="utf-8"
    )

    if args.json:
        payload = {
            "repo_root": normalize(root),
            "counts": {"open_points": len(open_points), "end_points": len(end_points)},
            "open_points": open_points,
            "end_points": end_points,
            "readme_names": sorted(readme_names),
            "markers": sorted(markers),
            "ignored_globs": extra_ignores,
            "skip_dirs": sorted(skip_dirs),
            "include_hidden": bool(args.include_hidden),
        }
        Path(args.json).parent.mkdir(parents=True, exist_ok=True)
        Path(args.json).write_text(json.dumps(payload, indent=2), encoding="utf-8")

    print(f"Wrote {len(open_points)} open points and {len(end_points)} end points to {normalize(out_dir)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
