def main():
    s = input("Fraction: ")
    a = convert(s)
    print(gauge(a))


def convert(fraction: str):
    print('returned output:'+fraction)
    try:
        x,y = fraction.split('/')
        x = int(x)
        y = int(y)
        if x <= y and y != 0: 
            frac = int(x) / int(y)
            frac = frac * 100
            frac = round(frac)
            frac = int(frac)
            return frac
        elif x > y and y != 0:
            raise ValueError
        else:
            raise ZeroDivisionError
    except ValueError:
        raise ValueError
        
    except ZeroDivisionError:
        raise ZeroDivisionError
        

def gauge(percentage):
    # print('what is this' , percentage)
    try:
        if percentage >= 99: 
            return "F"

        elif percentage <= 1:
            return 'E'

        else:
            return (str(percentage) +'%')
    except TypeError:
        return TypeError

if __name__ == "__main__":
    main()