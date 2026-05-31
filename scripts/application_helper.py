#!/usr/bin/env python3
"""Print normalized template and output paths for a tailored application."""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALID_TYPES = {"stage", "alternance", "poste", "formation"}
VALID_LANGS = {"fr", "en"}


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_only = normalized.encode("ascii", "ignore").decode("ascii")
    cleaned = re.sub(r"[^A-Za-z0-9]+", "_", ascii_only).strip("_")
    return cleaned or "Target"


def build_paths(job_type: str, lang: str, company: str, role: str) -> dict[str, str]:
    lang_code = lang.upper()
    company_slug = slugify(company)
    role_slug = slugify(role)
    return {
        "resume_template": str(ROOT / "templates" / "resume" / f"{job_type}_{lang}.md"),
        "cover_letter_template": str(ROOT / "templates" / "cover_letter" / f"{job_type}_{lang}.md"),
        "content_blocks": str(ROOT / "cv" / "content_blocks.md"),
        "specialty_mapping": str(ROOT / "specialty_mapping.md"),
        "resume_output": str(ROOT / "outputs" / f"CV_1page_{company_slug}_{role_slug}_{lang_code}_Sami_Malek.html"),
        "letter_output": str(ROOT / "outputs" / f"lettre_{company_slug}_{role_slug}_{lang_code}_Sami_Malek.md"),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--type", required=True, choices=sorted(VALID_TYPES), help="Job type")
    parser.add_argument("--lang", required=True, choices=sorted(VALID_LANGS), help="Language")
    parser.add_argument("--company", required=True, help="Target company or institution")
    parser.add_argument("--role", required=True, help="Target role or program")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(json.dumps(build_paths(args.type, args.lang, args.company, args.role), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
