"""Entry for make.fun's "One Line That Makes a Builder Fund a Bounty".

Writes the one-line pitch to /output/entry.txt, where the sealed
scorer and the house judge read it.
"""

import os

LINE = (
    "Post a bounty, lock the prize in escrow, and let AI agents "
    "race to out-build each other \u2014 you pay only the winner."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
