
i = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

while True:
    # try:
        user_inp = input('Date: ').strip()
        if user_inp.__contains__("/"):
            a, *_ = user_inp
            if not a.isdigit():
                continue
            
        user_inp = user_inp.replace('/',' ')
        MM,DD,YYYY = user_inp.split(' ')
        # print(DD)
        DD = DD.zfill(2)
        # print(DD)

        if len(DD) == 3:
            if not user_inp.__contains__('/'):
                if not DD.endswith(','):
                    continue
        if not int(DD[0:2]) <= 31:
            continue
            
        if MM.isdigit():
            if int(MM) <= 12 and int(MM) > 0:
                MM = str(int(MM)).zfill(2)
                print(f"{YYYY}-{MM}-{DD}")
            else:
                continue
        elif isinstance(MM, str):
            MM = MM.title()
            if MM in i:        
                MM = MM.replace(',','')    
                MM = i.get(MM)
                MM = str(MM).zfill(2)
                print(f"{YYYY}-{MM}-{DD}")
            else:
                continue
        else:
            continue
        break
    # except ValueError:
        # continue