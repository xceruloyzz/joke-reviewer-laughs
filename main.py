"""Write one one-line joke about working beside AI coding agents.

Deterministic, stdlib only, no network. Writes the entry to /output/entry.txt.
"""

JOKE = (
    "My agent fixed the bug, wrote the test, and approved its own PR \u2014 "
    "I just read the diff now, like a rubber duck with merge rights."
)


def main() -> None:
    import os

    # The gate requires 1-280 Unicode code points, one line, not blank.
    assert 1 <= len(JOKE) <= 280, f"joke is {len(JOKE)} chars"
    assert "\n" not in JOKE and JOKE.strip(), "joke must be one non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
