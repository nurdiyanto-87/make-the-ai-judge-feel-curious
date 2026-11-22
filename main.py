"""Write one short text to /output/entry.txt to make the AI judge curious.

Final choice (revised from candidate 3): a rusted tin box under the third
stone from the gate — a photograph of a house the reader has never seen,
and on the back, in pencil, the reader's own name. Concrete, quiet, and
the question it leaves behind keeps working after the last line.
"""

import os

TEXT = (
    "Under the third stone from the gate, at the bottom of the garden, "
    "there is a rusted tin box. Inside it, a photograph of a house you "
    "have never seen. On the back, in pencil, your own name."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
