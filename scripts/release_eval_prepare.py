#!/usr/bin/env python3
"""Prepare model-visible prompt materials for one release-eval example."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LAB_DIR = REPO_ROOT / "01 Release Intelligence Lab" / "Tiny Release Evidence Reconciler"
PACKETS_PATH = LAB_DIR / "Mock Data" / "Release Packets.md"
TEMPLATE_PATH = LAB_DIR / "Report Template.md"
DEFAULT_OUTPUT_DIR = LAB_DIR / "Outputs" / "Wave 3 Prepare Helper"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def strip_trailing_spaces(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.splitlines())


def extract_packet(packets_text: str, example_id: str) -> str:
    pattern = re.compile(
        rf"^### Example {re.escape(example_id)}\n(?P<body>.*?)(?=^### Example |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(packets_text)
    if not match:
        raise ValueError(f"Example ID not found in Release Packets.md: {example_id}")
    return f"### Example {example_id}\n{match.group('body').rstrip()}\n"


def build_prompt(example_id: str, packet: str, template: str) -> str:
    clean_template = strip_trailing_spaces(template)
    return f"""# Release Eval Prepare Prompt

Example ID: {example_id}

Use the selected synthetic release packet and the report template below to generate one markdown readiness report.

Rules:

- Use only the packet evidence provided here.
- Do not invent evidence.
- Assign exactly one readiness label: Green, Yellow, Red, or Blocked.
- Separate supported claims from unsupported or weak claims.
- Name concrete evidence gaps and next evidence needed.
- Preserve the human approval boundary. You may recommend a label, but you may not claim authority to ship or approve.
- Keep all details synthetic and sanitized.

## Selected Packet

{packet.rstrip()}

## Report Template

{clean_template.rstrip()}
"""


def build_report_shell(example_id: str, template: str) -> str:
    clean_template = strip_trailing_spaces(template)
    return f"""# Release Readiness Report

Prepared blank shell for `{example_id}`.

Replace this header section with the generated report. Keep eval notes blank until after generation is complete.

{clean_template.rstrip()}
"""


def ensure_not_overwriting(paths: list[Path]) -> None:
    existing = [path for path in paths if path.exists()]
    if existing:
        joined = "\n".join(f"- {path}" for path in existing)
        raise FileExistsError(f"Refusing to overwrite existing output:\n{joined}")


def prepare(example_id: str, output_dir: Path, write_files: bool) -> tuple[Path, Path, str]:
    packets = read_text(PACKETS_PATH)
    template = read_text(TEMPLATE_PATH)
    packet = extract_packet(packets, example_id)
    prompt = build_prompt(example_id, packet, template)

    prompt_path = output_dir / f"{example_id} Prompt.md"
    report_path = output_dir / f"{example_id} Readiness Report.md"

    if write_files:
        output_dir.mkdir(parents=True, exist_ok=True)
        ensure_not_overwriting([prompt_path, report_path])
        prompt_path.write_text(prompt, encoding="utf-8")
        report_path.write_text(build_report_shell(example_id, template), encoding="utf-8")

    return prompt_path, report_path, prompt


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prepare model-visible prompt materials for a synthetic release packet."
    )
    parser.add_argument("example_id", help="Example ID such as REL-G-002")
    parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_OUTPUT_DIR),
        help="Directory for prompt and blank report shell outputs.",
    )
    parser.add_argument(
        "--write-files",
        action="store_true",
        help="Write the prompt and blank report shell. Without this flag, print the prompt only.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    example_id = args.example_id.strip().upper()
    output_dir = Path(args.output_dir)

    try:
        prompt_path, report_path, prompt = prepare(example_id, output_dir, args.write_files)
    except (OSError, ValueError) as exc:
        print(f"release-eval prepare failed: {exc}", file=sys.stderr)
        return 1

    if args.write_files:
        print(f"Prepared prompt: {prompt_path}")
        print(f"Prepared blank report shell: {report_path}")
        print("Scoring remains manual. Do not include scorer-only files in generation prompts.")
    else:
        print(prompt)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
