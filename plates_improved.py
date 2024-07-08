
def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate: str):
    try:
        plate = plate.strip().lower()

        def check_first_2_letters_and_len(the_string: str):
            the_string = the_string.strip().lower()

            if len(the_string) >= 2 and len(the_string) <= 6:
                if the_string[0].isalpha() and the_string[1].isalpha():
                        return True
                else:
                    return False
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
        
        if check_first_2_letters_and_len(plate) and check_num(plate) and check_special_characters(plate):
            return True
        else:
            return False
    except ValueError:
        return False
    except Exception:
        ...


if __name__ == '__main__':
    main()