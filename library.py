#test
import emoji

lol = input('Input: ')
print(list(lol))
if len(list(lol)) > 1:
    a,b = lol.split(' ', maxsplit=1)
    print(a,b)
    m = emoji.get_emoji_by_name(f'{b}', 'en')
    print(a,m)
else:
    m = emoji.get_emoji_by_name(f'{lol}', 'en')
    print(m)
