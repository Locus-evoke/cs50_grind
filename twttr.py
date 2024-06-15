user_inp = input("Input: ")
vowels =  ['a','e','i','o','u',  'A','E','I','O','U']
vowels_removed = []

for i in user_inp:
    if i not in vowels:
        vowels_removed.append(i)
        new_string = ''.join(vowels_removed)

print(new_string)