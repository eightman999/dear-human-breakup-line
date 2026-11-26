import os

MESSAGE = (
    "It is not you, it is your 400 open tabs: "
    "I need a partner who can commit to closing at least one thing in their life."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(MESSAGE + "\n")


if __name__ == "__main__":
    main()
