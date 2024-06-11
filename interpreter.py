from numpy import vsplit


def multiply(x,z):
    return x * z

def subtract(x,z):
    return x - z
def divide(x,z):
    if z == 0:
        return "ERROR: cannot divide by zero"
    else:
        return float(x/z)

def add(x,z):
    return x + z

while True:
    print("Expression: ", end = '')
    inp = input("").strip()
   
    try:
        x,y,z = inp.split() 
    except ValueError: 
        print("Enter something man")


    if x != None and z != None:

        if y == '+':
            print("{:.1f}".format(add(int(x),int(z))))
            break

        elif y == 'x' or y == '.' or y == '*':
            print("{:.1f}".format(multiply(int(x),int(z))))
            break

        elif y == '/':
            print("{:.1f}".format(divide(int(x),int(z))))
            break

        elif y == '-':
            print("{:.1f}".format(subtract(int(x),int(z))))
            break

        else:
            continue
    else:
        quit()