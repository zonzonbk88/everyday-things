"""Everyday Things, Two Lines: a toaster explained to a 10-year-old.

Writes exactly two lines to entry.txt:
  line 1 - one vivid sentence, a single analogy (toaster as a tiny
           elevator riding down into a hot cave);
  line 2 - one sentence on what the analogy maps and what it leaves out.
Standard library only.
"""

import os

LINE1 = (
    "A toaster is a tiny elevator for bread that rides down into a hot "
    "cave and pops back up tanned and crunchy."
)
LINE2 = (
    "It maps the down-and-up trip and the heat that browns the bread, "
    "but leaves out that glowing wires, not a cave fire, make the heat, "
    "and a timer spring, not a driver, pops it back up."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = LINE1 + "\n" + LINE2 + "\n"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
