import emoji

def main():
    inp = input('Input: ')
    emojized_inp = emoji.emojize(inp, language='alias')
    print(emojized_inp)

if __name__ == "__main__":
    main()