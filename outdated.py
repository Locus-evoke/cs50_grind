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
    user_inp = input('Date: ').strip()

    if '/' in user_inp:
        try:
            MM, DD, YYYY = user_inp.split('/')
            MM, DD, YYYY = int(MM), int(DD), int(YYYY)

            if 1 <= MM <= 12 and 1 <= DD <= 31:
                MM = str(MM).zfill(2)
                DD = str(DD).zfill(2)
                print(f"{YYYY}-{MM}-{DD}")
                break
        except ValueError:
            continue

    elif ',' in user_inp:
        try:
            month_day, YYYY = user_inp.split(',')
            month_day = month_day.strip()
            YYYY = int(YYYY.strip())
            month_name, DD = month_day.rsplit(' ', 1)
            a = 'a'.split()

            month_name = month_name.title()
            if month_name in i and DD.isdigit():
                MM = i[month_name]
                DD = int(DD)

                if (1 <= DD <= 31):
                    MM = str(MM).zfill(2)
                    DD = str(DD).zfill(2)
                    print(f"{YYYY}-{MM}-{DD}")
                    break
        except ValueError:
            continue
