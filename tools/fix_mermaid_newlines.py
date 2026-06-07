#!/usr/bin/env python3
"""
Fix \n inside Mermaid diagram node labels.
Replaces literal backslash-n with <br/> only within ```mermaid ... ``` blocks.
Leaves all other content untouched.
"""

import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)

GUIDE_DIRS = [
    os.path.join(REPO_ROOT, "guide", "nft"),
    os.path.join(REPO_ROOT, "guide", "ebb-and-flow"),
]

def fix_mermaid_newlines(content):
    """Replace \\n with <br/> only inside ```mermaid blocks."""
    result = []
    in_mermaid = False

    for line in content.split("\n"):
        if line.strip() == "```mermaid":
            in_mermaid = True
            result.append(line)
        elif in_mermaid and line.strip() == "```":
            in_mermaid = False
            result.append(line)
        elif in_mermaid:
            # Replace \n (literal backslash-n) with <br/> inside node label strings
            # Only replace inside quoted strings ["..."] or ['...'] or unquoted node text
            fixed = line.replace("\\n", "<br/>")
            result.append(fixed)
        else:
            result.append(line)

    return "\n".join(result)


def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        original = f.read()

    fixed = fix_mermaid_newlines(original)

    if fixed != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(fixed)
        # Count replacements
        count = original.count("\\n") - fixed.count("\\n")
        print(f"  ✓ {os.path.basename(filepath)} ({count} replacements)")
        return count
    else:
        print(f"  — {os.path.basename(filepath)} (no changes)")
        return 0


def main():
    total = 0
    for guide_dir in GUIDE_DIRS:
        print(f"\n{guide_dir}/")
        for fname in sorted(os.listdir(guide_dir)):
            if fname.endswith(".md"):
                total += process_file(os.path.join(guide_dir, fname))
    print(f"\nTotal replacements: {total}")


if __name__ == "__main__":
    main()
