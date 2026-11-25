"""Write one out-of-office auto-reply line to /output/entry.txt."""

import os

LINE = (
    "I'm away until Monday -- for urgent help, my desk plant is now "
    "acting manager and already ignoring everyone equally."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
