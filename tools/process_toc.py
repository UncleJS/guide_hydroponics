#!/usr/bin/env python3
"""
Add (or refresh) Table of Contents and 'Back to TOC' links in all guide files.

This script is fully IDEMPOTENT — safe to run multiple times.  On each run it:
  1. Strips any existing TOC block(s) and any existing back-link lines.
  2. Rebuilds a single, correct TOC and places one back-link before each section.

For all files except those in HAS_TOC: inserts auto-generated TOC after the
first '---' divider, then inserts back-links before every ## section heading
and before the final navigation line (*Next: or > **Next:**).

For files in HAS_TOC (compare/ guides only): TOC is hand-written; only
back-links are inserted/refreshed.

Files in SKIP are left completely untouched.

Usage:
    # Process a specific guide set (relative to cwd, or absolute)
    python tools/process_toc.py guide/nft
    python tools/process_toc.py guide/ebb-and-flow
    python tools/process_toc.py guide/compare

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
    os.path.join(REPO_ROOT, "guide", "compare"),
]

BACK_LINK_LINE = "[↑ Back to TOC](#table-of-contents)"

# Files to skip entirely — already fully formatted; do not touch
SKIP = {
    "00-system-overview.md",
}

# Files that already have a hand-written TOC (only insert back-links).
# Includes all compare/ guide files (01–04) which have rich hand-written TOCs.
# NOTE: files 10–13 were previously listed here but they do NOT have hand-written
# TOCs — they need auto-generated ones, so they are NOT in this set.
HAS_TOC = {
    # compare/ files — all have hand-written TOCs
    "01-nutrients.md",
    "02-crops.md",
    "03-automation.md",
    "04-cost.md",
}


def heading_to_anchor(heading_text):
    """Convert a heading string to a GitHub-style anchor."""
    anchor = heading_text.lower()
    anchor = re.sub(r"[^\w\s-]", "", anchor)
    anchor = re.sub(r"\s+", "-", anchor.strip())
    anchor = re.sub(r"-+", "-", anchor)
    return anchor


def build_toc(headings):
    """Build a TOC block from a list of (level, text) tuples."""
    lines = ["## Table of Contents", ""]
    for level, text in headings:
        anchor = heading_to_anchor(text)
        indent = "  " * (level - 2)  # ## = 0 indent, ### = 2 spaces
        lines.append(f"{indent}- [{text}](#{anchor})")
    lines.append("")
    return "\n".join(lines)


def strip_back_links_only(content):
    """
    Remove only auto-inserted back-link lines, leaving any hand-written TOC
    block intact.  Used for HAS_TOC files where we only manage back-links.
    """
    content = re.sub(
        r"\n[ \t]*\[↑ Back to TOC\]\(#table-of-contents\)[ \t]*(?=\n)",
        "",
        content,
    )
    content = re.sub(r"\n{4,}", "\n\n\n", content)
    return content


def strip_existing(content):
    """
    Remove all previously-inserted TOC blocks and back-link lines so the
    script can rebuild them cleanly.  Operates on the raw string.

    A TOC block looks like:
        ## Table of Contents
        <lines that are NOT a blank line followed by ##>
        <blank line>

    We also strip every line that is exactly the back-link pattern.
    """
    # --- Strip all back-link lines (with surrounding blank lines) ---
    # We want to remove the pattern:  \n[↑ Back to TOC…]\n  (with optional blanks)
    content = re.sub(
        r"\n[ \t]*\[↑ Back to TOC\]\(#table-of-contents\)[ \t]*(?=\n)",
        "",
        content,
    )

    # --- Strip all '## Table of Contents' blocks ---
    # Match from '## Table of Contents' up to (but not including) the next '##' heading
    # or end of string.
    content = re.sub(
        r"## Table of Contents\n.*?(?=\n## |\Z)",
        "",
        content,
        flags=re.DOTALL,
    )

    # Clean up any triple+ blank lines that stripping may have created
    content = re.sub(r"\n{4,}", "\n\n\n", content)

    return content


def process_file(filepath, needs_toc):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # ----------------------------------------------------------------
    # Step 0: Strip existing content — strategy differs by file type.
    #   needs_toc=True  → full strip (removes generated TOC + back-links)
    #   needs_toc=False → back-links only (preserves hand-written TOC)
    # ----------------------------------------------------------------
    if needs_toc:
        content = strip_existing(content)
    else:
        content = strip_back_links_only(content)
    lines = content.split("\n")

    # ----------------------------------------------------------------
    # Step 1: Collect section headings for the TOC
    #   Skip:  line 0 (# Title), line 1 (## Subtitle)
    # ----------------------------------------------------------------
    toc_headings = []
    for i, line in enumerate(lines):
        if i <= 1:
            continue
        m = re.match(r"^(#{2,})\s+(.+)$", line)
        if m:
            level = len(m.group(1))
            text = m.group(2).strip()
            toc_headings.append((level, text))

    # ----------------------------------------------------------------
    # Step 2: Insert TOC (for files that need it)
    # ----------------------------------------------------------------
    if needs_toc:
        result = []
        first_hr_seen = False
        toc_inserted = False
        for line in lines:
            result.append(line)
            if not toc_inserted and not first_hr_seen and line.strip() == "---":
                first_hr_seen = True
                toc_block = build_toc(toc_headings)
                result.append("")
                result.append(toc_block)
                result.append("")
                result.append("---")
                # The '---' we just added is the separator AFTER the TOC;
                # remove the blank we added after the TOC block.
                result.pop()   # remove the extra ---
                result.pop()   # remove the extra blank
                toc_inserted = True
        lines = result

    # ----------------------------------------------------------------
    # Step 3: Insert one back-link before each eligible ## heading.
    #
    # Some files have a ## Subtitle immediately after the # Title (line 2).
    # Others (files 10–13) have no subtitle — prose follows the # Title.
    # We detect the subtitle by checking whether a ## heading appears as
    # the second non-empty line of the file (right after the # Title).
    # ----------------------------------------------------------------

    # Identify subtitle text (if present) so we can skip it below.
    subtitle_text = None
    non_empty_count = 0
    for line in lines:
        if line.strip():
            non_empty_count += 1
            if non_empty_count == 2:
                m2 = re.match(r"^##\s+(.+)$", line)
                if m2:
                    subtitle_text = m2.group(1).strip()
                break

    result2 = []
    for line in lines:
        m = re.match(r"^(##)\s+(.+)$", line)
        if m:
            text = m.group(2).strip()
            # Never add a back-link before the ## Subtitle or the ## TOC heading
            if text == subtitle_text or text == "Table of Contents":
                result2.append(line)
                continue
            # Ensure there's a blank line above the back-link
            if result2 and result2[-1].strip() != "":
                result2.append("")
            result2.append(BACK_LINK_LINE)
            result2.append("")
            result2.append(line)
            continue
        result2.append(line)

    final_content = "\n".join(result2)

    # Step 4: Insert back-link before the final navigation line.
    # Handles both formats:
    #   *Next: ...          (ebb-and-flow style)
    #   > **Next:** ...     (nft style blockquote)
    final_content = re.sub(
        r"\n(\*Next:|> \*\*Next:\*\*)",
        r"\n\n" + BACK_LINK_LINE + r"\n\n\1",
        final_content,
    )

    # Step 5: Normalise — collapse triple+ blank lines
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
        if fname in SKIP:
            print(f"  — skipping {fname} (already fully formatted)")
            continue
        fpath = os.path.join(guide_dir, fname)
        needs_toc = fname not in HAS_TOC
        action = "TOC + back-links" if needs_toc else "back-links only (hand-written TOC)"
        print(f"  Processing {fname} ({action})...")
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
