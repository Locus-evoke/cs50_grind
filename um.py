import re
import sys


def main():
    print(count(input("Text: ")))


def count(string):
    pattern = r"(?<!\w)(um)(?:,|.| )"
    matches = re.findall(pattern, string, re.IGNORECASE)
    if not matches:
        return 0
    return len(matches)    

    ...


...


if __name__ == "__main__":
    main()