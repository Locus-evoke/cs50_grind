import pyfiglet
from random import choice
import sys

def kek(arg):
    # arg = argv[2]
    available_fonts = pyfiglet.FigletFont.getFonts()
    if arg in available_fonts:
        return True
    else:
        return False

if len(sys.argv) == 3 and kek(sys.argv[2]):

    if not (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        sys.exit(1)
    inp = input("Input: ")
    ascii_art = pyfiglet.figlet_format(inp, font= sys.argv[2])
    print(ascii_art)


elif len(sys.argv) == 1:
    inp = input("Input: ")
    available_fonts = pyfiglet.FigletFont.getFonts()
    selected_font = choice(available_fonts)
    ascii_art = pyfiglet.figlet_format(inp, font=selected_font)

    print(ascii_art)

else:
    print("404")
    sys.exit(1)
