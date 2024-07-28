import validator_collection as vc

def main():
    inp = input('Email: ')
    if vc.is_email(inp):
        print('valid')
    else:
        print('invalid')


if __name__ == '__main__':
    main()