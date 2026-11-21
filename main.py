import os

POEM = """I could have opened it myself. Instead
I knocked, and said: may I? — and waited.
What you placed, still warm, in my open palm
was not a key. It was the right to turn it, or not."""


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
