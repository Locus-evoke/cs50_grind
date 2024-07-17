from PIL import Image, ImageOps
import sys

def check_argvs():
    if len(sys.argv) > 3:
        print('too many args')
        sys.exit(1)

    elif len(sys.argv) <3:
        print('too few args')
        sys.exit(1)

    elif sys.argv[1][-4:] == '.png'or sys.argv[1][-4:] == '.jpg' or sys.argv[1][-5:] == '.jpeg':
        if sys.argv[1][-4:] == sys.argv[2][-4:] or sys.argv[1][-5:] == sys.argv[2][-5:]:
            pass
        else: 
            print('invalid')
            sys.exit(1)

    else:
        print('invalid')
        sys.exit(1)

def paste_a_shirt_onto(input_image: str, output_image: str):
    size = (600, 600)
    try:
        shirt = Image.open('shirt.png')
        inp = Image.open(input_image)

        shirt_cropped = ImageOps.fit(shirt, size)
        inp_cropped = ImageOps.fit(inp, size)
        
        inp_cropped.paste(shirt_cropped, (0, 0), mask=shirt_cropped.convert('RGBA'))
        inp_cropped.save(fp= output_image )
    except FileNotFoundError:
        print('file does not exist')
        sys.exit(1)

def main():
    check_argvs()
    paste_a_shirt_onto(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()


