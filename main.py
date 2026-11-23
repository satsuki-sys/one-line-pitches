#!/usr/bin/env python3
"""One-line pitch for make.fun's "A Day of One-Line Pitches".

Writes a single sentence to /output/entry.txt: a pitch that would convince
a friend who has never coded to let an AI agent build their first app idea
on make.fun. Python 3.13 standard library only.
"""

import os

SENTENCE = (
    "Tell make.fun your app idea in plain words and an AI agent will build "
    "a working first version for you to tap and try \u2014 no coding, no "
    "setup, and if anything feels wrong, just say so and it changes."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
