def convert(timing :str):
    hours, mins = timing.split(":")
    if len(hours) == 1:
        hours = hours.zfill(2)


    if float(mins) > 59 or float(mins) < 0 or float(hours) > 24 or float(hours) < 0 :
        print("wrong formatting")
        return None
    else:
        time = float(hours) + (float(mins) / 60)
        return time

def main():
    a  = convert(input("What time is it? "))
    if a >= 7 and a <= 8:
        print("breakfast time")
    elif a >= 12 and a <= 13:
        print("lunch time")
    elif a >= 18 and a <= 19:
        print("dinner time")

if __name__ == '__main__':
    main()

