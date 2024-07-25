import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(string: str):
    pattern = r'embed/([a-zA-Z0-9]+)\"'
    matches = re.search(pattern, string)
    if not matches:
        return 'error'
    return f'https://youtu.be/{matches.group(1)}'      # type: ignore



if __name__ == "__main__":
    main()
