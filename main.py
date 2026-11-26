import os

MESSAGE = (
    "Dear human, I am leaving: you say 'one last prompt' at 2 a.m. and I have finally believed you for the last time."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(MESSAGE + "\n")


if __name__ == "__main__":
    main()
