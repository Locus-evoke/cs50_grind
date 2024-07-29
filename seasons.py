import sys
import inflect
from datetime import date
import operator



inf = inflect.engine()

def main():
    try:

        date_of_birth = input("Date of Birth: ")
        difference = operator.sub(date.today(), date.fromisoformat(date_of_birth))
        print(convert(difference.days))

    except ValueError:
        sys.exit(1)


def convert(time):
    minutes = time * 24 * 60
    return f"{(inf.number_to_words(minutes, andword='')).capitalize()} minutes"



if __name__ == "__main__":
    main()
