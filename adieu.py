import inflect 
p = inflect.engine()
try:
    names = []
    while True:
        inp = input('Name: ')
        names.append(inp)         # Adieu, adieu, to p.join(words1, final_sep='')
except EOFError:
    adieu = '\nAdieu, adieu, to '
    final = adieu + p.join(names, final_sep= ',')
    print(final)
