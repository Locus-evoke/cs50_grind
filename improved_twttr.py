def main():
    user_inp = input("Input: ")
    print(shorten(user_inp))

def shorten(string):
    vowels =  ['a','e','i','o','u',  'A','E','I','O','U']
    vowels_removed = list(string)
    new_string = vowels_removed
    
    for letter in string:
        if letter in vowels:
            vowels_removed.remove(letter)
    return ''.join(new_string)
    

if __name__ == '__main__':
    main()