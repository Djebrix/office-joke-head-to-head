"""Write one funny office joke line to $ENTRY_OUTPUT_DIR/entry.txt.

Stdlib only, no network, fully deterministic.
"""

import os

JOKE = "The lift's been broken for six months, so HR rebranded the stairwell as a wellness programme."


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
