#!/usr/bin/env python3
"""Simple style filter for reducing AI-sounding wording.

This tool does not bypass detection systems. It helps improve writing clarity
by flagging overused terms and optionally applying straightforward replacements.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Rule:
    pattern: re.Pattern[str]
    replacement: str
    label: str


PROFILE_CHOICES = ["general", "academic", "scientific", "resume-ats"]


def _base_pairs() -> list[tuple[str, str, str]]:
    return [
        (r"\bcomprehensive\b", "thorough", "overused adjective"),
        (r"\brobust\b", "reliable", "overused adjective"),
        (r"\bseamless\b", "smooth", "overused adjective"),
        (r"\bleverage\b", "use", "business jargon"),
        (r"\butilize\b", "use", "business jargon"),
        (r"\bfurthermore\b", "also", "stiff transition"),
        (r"\bmoreover\b", "also", "stiff transition"),
        (r"\badditionally\b", "also", "stiff transition"),
        (r"\bit's worth noting that\b", "", "filler phrase"),
        (r"\bit is important to note that\b", "", "filler phrase"),
        (r"\bin conclusion\b", "", "generic closer"),
        (r"\bto sum up\b", "", "generic closer"),
        (r"\bpotentially\b", "", "hedging"),
        (r"\bpossibly\b", "", "hedging"),
        (r"\bperhaps\b", "", "hedging"),
    ]


def _academic_pairs() -> list[tuple[str, str, str]]:
    return [
        (r"\bvery\b", "", "intensity filler"),
        (r"\ba lot of\b", "many", "informal wording"),
        (r"\bkind of\b", "", "informal wording"),
        (r"\bsort of\b", "", "informal wording"),
        (r"\bthings\b", "factors", "vague noun"),
        (r"\bstuff\b", "materials", "vague noun"),
    ]


def _scientific_pairs() -> list[tuple[str, str, str]]:
    return [
        (r"\bprove\b", "support", "overclaim"),
        (r"\bproved\b", "supported", "overclaim"),
        (r"\bhuge\b", "substantial", "informal wording"),
        (r"\bgreat\b", "strong", "informal wording"),
        (r"\bvery important\b", "critical", "wordy phrase"),
        (r"\bshows that\b", "indicates that", "precision"),
    ]


def _resume_ats_pairs() -> list[tuple[str, str, str]]:
    return [
        (r"\bresponsible for\b", "led", "weak bullet phrasing"),
        (r"\bhelped with\b", "supported", "weak bullet phrasing"),
        (r"\bworked on\b", "delivered", "weak bullet phrasing"),
        (r"\bteam player\b", "collaborated cross-functionally", "cliche"),
        (r"\bhardworking\b", "", "cliche"),
        (r"\bdetail-oriented\b", "", "cliche"),
        (r"\bresults-driven\b", "", "cliche"),
        (r"\bsynergy\b", "coordination", "jargon"),
    ]


def _compile_rules(profile: str) -> list[Rule]:
    pairs = _base_pairs()
    if profile == "academic":
        pairs.extend(_academic_pairs())
    elif profile == "scientific":
        pairs.extend(_scientific_pairs())
    elif profile == "resume-ats":
        pairs.extend(_resume_ats_pairs())
    return [
        Rule(re.compile(pattern, re.IGNORECASE), replacement, label)
        for pattern, replacement, label in pairs
    ]


def _normalize_spacing(text: str) -> str:
    text = re.sub(r"[ \t]{2,}", " ", text)
    text = re.sub(r"\s+([,.;:!?])", r"\1", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def analyze(text: str, rules: list[Rule]) -> list[tuple[str, str, int]]:
    findings: list[tuple[str, str, int]] = []
    for rule in rules:
        count = len(rule.pattern.findall(text))
        if count:
            findings.append((rule.pattern.pattern, rule.label, count))
    return findings


def rewrite(text: str, rules: list[Rule]) -> str:
    output = text
    for rule in rules:
        output = rule.pattern.sub(rule.replacement, output)
    return _normalize_spacing(output)


def _resume_ats_checks(text: str) -> list[str]:
    checks: list[str] = []
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    bullet_lines = [
        line for line in lines if line.startswith("- ") or line.startswith("* ")
    ]

    if not bullet_lines:
        checks.append("No bullet points found. ATS resumes perform better with concise bullets.")
    else:
        starts_with_verb = 0
        has_metrics = 0
        for line in bullet_lines:
            content = line[2:].strip()
            if re.match(r"^[A-Z][a-z]+ed\b|^[A-Z][a-z]+ing\b|^[A-Z][a-z]+s\b", content):
                starts_with_verb += 1
            if re.search(r"\b\d+(?:\.\d+)?%?\b", content):
                has_metrics += 1

        checks.append(
            f"Action-verb bullets: {starts_with_verb}/{len(bullet_lines)} (higher is better)."
        )
        checks.append(
            f"Bullets with metrics: {has_metrics}/{len(bullet_lines)} (aim for at least 50%)."
        )

    section_hits = 0
    for name in ["experience", "skills", "education", "projects", "summary"]:
        if re.search(rf"\b{name}\b", text, flags=re.IGNORECASE):
            section_hits += 1
    checks.append(f"Standard resume sections detected: {section_hits}/5.")

    return checks


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Flag and reduce common AI-sounding wording in text."
    )
    parser.add_argument("input", type=Path, help="Path to input text/markdown file")
    parser.add_argument(
        "--profile",
        choices=PROFILE_CHOICES,
        default="general",
        help="Style profile: general, academic, scientific, or resume-ats",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Overwrite file with suggested replacements",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Write rewritten output to a different file",
    )
    args = parser.parse_args()

    if not args.input.exists():
        raise SystemExit(f"Input file not found: {args.input}")

    text = args.input.read_text(encoding="utf-8")
    rules = _compile_rules(args.profile)
    findings = analyze(text, rules)

    print(f"Profile: {args.profile}")

    if findings:
        print("Potential AI-sounding patterns found:")
        for pattern, label, count in sorted(findings, key=lambda x: x[2], reverse=True):
            print(f"- {count:>3}x {label}: /{pattern}/")
    else:
        print("No configured patterns found.")

    if args.profile == "resume-ats":
        print("\nResume ATS checks:")
        for check in _resume_ats_checks(text):
            print(f"- {check}")

    rewritten = rewrite(text, rules)
    if args.write:
        args.input.write_text(rewritten, encoding="utf-8")
        print(f"Rewritten content saved to: {args.input}")
    elif args.output is not None:
        args.output.write_text(rewritten, encoding="utf-8")
        print(f"Rewritten content saved to: {args.output}")


if __name__ == "__main__":
    main()
