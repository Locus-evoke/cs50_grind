inp = input("camelCase: ")

snake_case = []
for letter in inp:
    if letter.isupper() and letter != snake_case[0]:
            snake_case.append('_')
            snake_case.append(letter.lower())  
    else:

          snake_case.append(letter)

result = ''.join(snake_case)
print(str(result))
