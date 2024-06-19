def main():
    plate = input("Plate: ")

    if is_valid(plate) and check_num(plate) and check_special_characters(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(the_string: str):
    if len(the_string) >= 2 and len(the_string) <= 6:
        if the_string[0].isalpha() and the_string[1].isalpha():
                return True
        else:
            return False
    else:
        return False

def check_num(the_string: str):
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
def check_special_characters(the_string):
    for i in the_string:
        if i in ['.',':',',','_',';']:
            return False
        
    return True


main()
