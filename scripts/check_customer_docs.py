#!/usr/bin/env python3
"""Enforce the public documentation's customer/developer audience boundary."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Finding:
    path: Path
    line: int
    message: str


MARKDOWN_LINK = re.compile(r"(?<!!)\[[^]]*]\(([^)]+)\)")
MARKDOWN_IMAGE = re.compile(r"!\[([^]]*)]\(([^)]+)\)")
HTML_LINK = re.compile(r"<a\b[^>]*\bhref=[\"']([^\"']+)[\"'][^>]*>", re.I)
HTML_IMAGE = re.compile(r"<img\b[^>]*\bsrc=[\"']([^\"']+)[\"'][^>]*>", re.I)
HTML_ALT = re.compile(r"\balt=[\"']([^\"']*)[\"']", re.I)


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:", "tel:", "#"))


def local_target(source: Path, target: str) -> Path:
    clean = target.split("#", 1)[0].split("?", 1)[0]
    return (source.parent / clean).resolve()


def image_target(root: Path, source: Path, target: str, policy: dict) -> Path | None:
    prefix = policy["repository_raw_image_prefix"]
    if target.startswith(prefix):
        return (root / target.removeprefix(prefix).split("?", 1)[0]).resolve()
    if is_external(target):
        return None
    return local_target(source, target)


def forbidden_image_message(root: Path, resolved: Path | None, policy: dict) -> str | None:
    if resolved is None:
        return None
    try:
        relative = resolved.relative_to(root.resolve()).as_posix()
    except ValueError:
        return None
    if relative in set(policy.get("forbidden_image_targets", [])):
        return f"rejected documentation screenshot: {relative}"
    return None


def scan_customer_doc(root: Path, path: Path, policy: dict) -> list[Finding]:
    text = path.read_text(encoding="utf-8")
    findings: list[Finding] = []

    for rule in policy["forbidden_patterns"]:
        for match in re.finditer(rule["pattern"], text):
            findings.append(
                Finding(path, line_number(text, match.start()), f"{rule['name']}: {rule['help']}")
            )

    if len(re.findall(r"<details(?:\s[^>]*)?>", text, re.I)) != len(re.findall(r"</details>", text, re.I)):
        findings.append(Finding(path, 1, "unbalanced <details> block"))
    if len(re.findall(r"<summary(?:\s[^>]*)?>", text, re.I)) != len(re.findall(r"</summary>", text, re.I)):
        findings.append(Finding(path, 1, "unbalanced <summary> block"))

    for match in MARKDOWN_LINK.finditer(text):
        target = match.group(1).strip().split(" ", 1)[0]
        if target and not is_external(target) and not local_target(path, target).exists():
            findings.append(
                Finding(path, line_number(text, match.start()), f"broken local link: {target}")
            )

    for match in HTML_LINK.finditer(text):
        target = match.group(1).strip()
        if target and not is_external(target) and not local_target(path, target).exists():
            findings.append(
                Finding(path, line_number(text, match.start()), f"broken local HTML link: {target}")
            )

    for match in MARKDOWN_IMAGE.finditer(text):
        alt, target = match.groups()
        if not alt.strip():
            findings.append(Finding(path, line_number(text, match.start()), "image is missing alt text"))
        resolved = image_target(root, path, target, policy)
        rejected = forbidden_image_message(root, resolved, policy)
        if rejected:
            findings.append(Finding(path, line_number(text, match.start()), rejected))
        if resolved is not None and not resolved.exists():
            findings.append(
                Finding(path, line_number(text, match.start()), f"missing local image: {target}")
            )

    for match in HTML_IMAGE.finditer(text):
        tag, target = match.group(0), match.group(1)
        alt = HTML_ALT.search(tag)
        if alt is None or not alt.group(1).strip():
            findings.append(Finding(path, line_number(text, match.start()), "HTML image is missing alt text"))
        resolved = image_target(root, path, target, policy)
        rejected = forbidden_image_message(root, resolved, policy)
        if rejected:
            findings.append(Finding(path, line_number(text, match.start()), rejected))
        if resolved is not None and not resolved.exists():
            findings.append(
                Finding(path, line_number(text, match.start()), f"missing local image: {target}")
            )

    return findings


def check_pos_preservation(root: Path, policy: dict) -> list[Finding]:
    path = root / "docs_source_en/pos.md"
    text = path.read_text(encoding="utf-8")
    config = policy["pos_preservation"]
    findings: list[Finding] = []

    image_count = len(MARKDOWN_IMAGE.findall(text)) + len(HTML_IMAGE.findall(text))
    minimum = config["minimum_image_references"]
    if image_count < minimum:
        findings.append(Finding(path, 1, f"POS screenshot regression: {image_count} references, need at least {minimum}"))

    for required in config["required_text"]:
        if required not in text:
            findings.append(Finding(path, 1, f"POS customer setup regression: missing {required!r}"))
    for required in config["required_images"]:
        if required not in text:
            findings.append(Finding(path, 1, f"POS responsive evidence regression: missing {required}"))
    return findings


def public_docs(root: Path) -> list[Path]:
    return [
        root / "README.md",
        *sorted((root / "docs_source_en").glob("*.md")),
        *sorted((root / "docs/i18n").glob("README_*.md")),
    ]


def run(root: Path) -> list[Finding]:
    policy_path = root / "scripts/customer-docs-policy.json"
    policy = json.loads(policy_path.read_text(encoding="utf-8"))
    developer_docs = {root / item for item in policy["developer_docs"]}
    findings: list[Finding] = []

    missing_exceptions = sorted(path for path in developer_docs if not path.exists())
    for path in missing_exceptions:
        findings.append(Finding(path, 1, "classified developer page does not exist"))

    for path in public_docs(root):
        if path not in developer_docs:
            findings.extend(scan_customer_doc(root, path, policy))
    findings.extend(check_pos_preservation(root, policy))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    findings = run(root)
    if findings:
        for finding in findings:
            try:
                shown = finding.path.relative_to(root)
            except ValueError:
                shown = finding.path
            print(f"{shown}:{finding.line}: {finding.message}")
        print(f"customer docs gate: FAILED ({len(findings)} finding(s))")
        return 1
    policy = json.loads((root / "scripts/customer-docs-policy.json").read_text(encoding="utf-8"))
    developer_count = len(policy["developer_docs"])
    customer_count = len(public_docs(root)) - developer_count
    print(
        f"customer docs gate: clean ({customer_count} customer pages checked; "
        f"{developer_count} developer pages exempted)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
