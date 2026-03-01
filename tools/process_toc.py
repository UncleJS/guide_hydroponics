#!/usr/bin/env python3
"""
Add Table of Contents and 'Back to TOC' links to all guide files.

For files 01-09: insert a TOC block after the subtitle line and add goto links before each ## section heading.
For files 10-13: TOC already exists; only add goto links before each ## section heading (skip the TOC heading itself).

Usage:
    # Process a specific guide set (relative to this script's parent directory)
    python tools/process_toc.py guide/nft
    python tools/process_toc.py guide/ebb-and-flow

    # Process ALL known guide sets (default when no argument given)
    python tools/process_toc.py
"""

import re
import os
import sys

# Resolve the repo root as the directory containing this script's parent.
# i.e. if the script is at  <repo>/tools/process_toc.py  then repo root = <repo>
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)

# Guide sets to process when no argument is supplied
DEFAULT_GUIDE_DIRS = [
    os.path.join(REPO_ROOT, "guide", "nft"),
    os.path.join(REPO_ROOT, "guide", "ebb-and-flow"),
]

BACK_LINK = "\n[↑ Back to TOC](#table-of-contents)\n"

# Files that already have a TOC (only need goto links)
HAS_TOC = {
    "10-climate-management.md",
    "11-build-guide.md",
    "12-budget-and-sourcing.md",
    "13-automation.md",
}


def heading_to_anchor(heading_text):
    """Convert a heading string to a GitHub-style anchor."""
    anchor = heading_text.lower()
    anchor = re.sub(r"[^\w\s-]", "", anchor)
    anchor = re.sub(r"\s+", "-", anchor.strip())
    anchor = re.sub(r"-+", "-", anchor)
    return anchor


def build_toc(headings):
    """Build a TOC block from a list of (level, text) tuples, skipping the subtitle."""
    lines = ["## Table of Contents", ""]
    for level, text in headings:
        anchor = heading_to_anchor(text)
        indent = "  " * (level - 2)  # ## = 0 indent, ### = 2 spaces
        lines.append(f"{indent}- [{text}](#{anchor})")
    lines.append("")
    return "\n".join(lines)


def process_file(filepath, needs_toc):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split("\n")

    # ----------------------------------------------------------------
    # Collect all ## headings (and deeper) for TOC — but skip:
    #   - line 1 (# title)
    #   - line 2 (## subtitle)
    #   - any existing "## Table of Contents" section
    # ----------------------------------------------------------------
    toc_headings = []
    in_toc_section = False
    for i, line in enumerate(lines):
        if i == 0:
            continue  # # Title
        if i == 1:
            continue  # ## Subtitle
        m = re.match(r"^(#{2,})\s+(.+)$", line)
        if m:
            level = len(m.group(1))
            text = m.group(2).strip()
            if text == "Table of Contents":
                in_toc_section = True
                continue
            if in_toc_section:
                in_toc_section = False
            toc_headings.append((level, text))

    # ----------------------------------------------------------------
    # Rebuild the file line-by-line
    # ----------------------------------------------------------------
    toc_inserted = not needs_toc
    first_hr_seen = False

    # ---- Pass 1: insert TOC ----
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        result.append(line)

        if needs_toc and not toc_inserted:
            if line.strip() == "---" and not first_hr_seen:
                first_hr_seen = True
                toc_block = build_toc(toc_headings)
                result.append("")
                result.append(toc_block)
                result.append("")
                result.append("---")
                result.pop()  # remove the extra ---
                result.pop()  # remove the extra blank
                toc_inserted = True
        i += 1

    lines = result

    # ---- Pass 2: insert back links before eligible ## headings ----
    result2 = []
    subtitle_done = False

    for i, line in enumerate(lines):
        m = re.match(r"^(##)\s+(.+)$", line)
        if m:
            text = m.group(2).strip()
            if not subtitle_done:
                subtitle_done = True
                result2.append(line)
                continue
            if text == "Table of Contents":
                result2.append(line)
                continue
            if result2 and result2[-1].strip() != "":
                result2.append("")
            result2.append("[↑ Back to TOC](#table-of-contents)")
            result2.append("")
            result2.append(line)
            continue
        result2.append(line)

    final_content = "\n".join(result2)

    # Insert back link before the final *Next: navigation line
    final_content = re.sub(
        r"\n(\*Next:)",
        r"\n\n[↑ Back to TOC](#table-of-contents)\n\n\1",
        final_content,
    )

    # Clean up any triple+ blank lines
    final_content = re.sub(r"\n{4,}", "\n\n\n", final_content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(final_content)

    print(f"  ✓ {os.path.basename(filepath)}")


def process_dir(guide_dir):
    if not os.path.isdir(guide_dir):
        print(f"  ERROR: directory not found: {guide_dir}", file=sys.stderr)
        return
    files = sorted(os.listdir(guide_dir))
    for fname in files:
        if not fname.endswith(".md"):
            continue
        fpath = os.path.join(guide_dir, fname)
        needs_toc = fname not in HAS_TOC
        action = "TOC + goto links" if needs_toc else "goto links only"
        print(f"Processing {fname} ({action})...")
        process_file(fpath, needs_toc)


def main():
    if len(sys.argv) > 1:
        # Argument may be relative (to cwd) or absolute
        arg = sys.argv[1]
        guide_dir = arg if os.path.isabs(arg) else os.path.join(os.getcwd(), arg)
        print(f"\n=== {guide_dir} ===")
        process_dir(guide_dir)
    else:
        for guide_dir in DEFAULT_GUIDE_DIRS:
            print(f"\n=== {guide_dir} ===")
            process_dir(guide_dir)

    print("\nDone!")


if __name__ == "__main__":
    main()
