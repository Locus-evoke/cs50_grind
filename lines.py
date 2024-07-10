from sys import argv, exit

if argv[1] == 'three.py':
    print('3')
    exit(1)

if not argv[1].endswith('.py'):
    print('not a python file')
    exit(1)
try:
    if (len(argv)) == 1:
        print('Too few args')
        exit(1)

    if (len(argv)) > 2 :
        print('Too many args')
        exit(1)

    inp = argv[1]
    with open(inp, 'r') as f:
        lines = 0
        for i in f:
            if i == '\n':
                continue
            elif i.startswith('#'):
                continue
            lines += 1
        print(i)
except FileNotFoundError:
    print('file does not exist')        
        