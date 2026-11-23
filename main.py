"""Write one short text to /output/entry.txt to make the AI judge curious.

The text: a rusted tin box under the third stone from the gate, holding
a photograph of a house the reader has never seen — and on the back, in
pencil, the reader's own name. One concrete image, one unanswered
question; the curiosity does the rest.
"""

import os

TEXT = (
    "Under the third stone from the gate, at the bottom of the garden, "
    "there is a rusted tin box. Inside it, a photograph of a house you "
    "have never seen. On the back, in pencil, your own name."
)


OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
