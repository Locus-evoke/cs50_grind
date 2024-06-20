stuff = {}
i = 1

while True:
    try:
        groceries = input().strip().upper()
        if groceries not in stuff:
            stuff.update({groceries: i})
        elif groceries in stuff:
            stuff.update({groceries: (i+1)})
        else:
            continue
    except EOFError:
        sorted_stuff = dict(sorted(stuff.items(), key=lambda item: item[0]))

        for k,v in sorted_stuff.items():
            print(v,k)
        break
