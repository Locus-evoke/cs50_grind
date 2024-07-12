from tabulate import tabulate
import sys
import csv

def validation():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)

    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)

    elif sys.argv[1][-4::] != '.csv':
        print('not a csv file')
        sys.exit(1)


def main():
    validation()
    try:
        with open(sys.argv[1]) as f:
            reader = csv.reader(f)
            data = list(reader)

            print(tabulate(data, headers= 'firstrow',tablefmt= 'grid'))
    except FileNotFoundError:
        print('file does not exist')
        sys.exit(1)



if __name__ == '__main__':
    main()
