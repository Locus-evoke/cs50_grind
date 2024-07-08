
def main():
    plate = input("Plate: ")

    if check_len(plate) and check_first_2_letters(plate) and check_num(plate) and check_special_characters(plate):
        print("Valid")
    else:
        print("Invalid")


def check_len(the_string: str):
    the_string = the_string.strip().lower()

    if len(the_string) >= 2 and len(the_string) <= 6:
        return True
    else:
        return False

def check_first_2_letters(the_string: str):
    the_string = the_string.strip().lower()
    if the_string[0].isalpha() and the_string[1].isalpha():
            return True
    else:
        return False


def check_num(the_string: str):
    the_string = the_string.strip().lower()

    for i,character in enumerate(the_string):
        if character.isdigit():
            if character != '0':
                slice = the_string[i:]
                for j in slice:
                    if j.isalpha():
                        return False
                else:
                    return True
            else:
                return False
    else:
        return True

def check_special_characters(the_string: str):
    the_string = the_string.strip().lower()
    if not the_string.isalnum():
        return False

    return True




if __name__ == '__main__':
    main()