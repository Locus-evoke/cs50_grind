from random import randint

while True:
    try:
        level = input('Level: ')
        
        if int(level) < 0:
            continue
        
        level = int(level)
        target = randint(1, level)

        while True:
            guess = input('Guess: ')
            guess = int(guess)
        
            if guess < target:
                print("Too small!")
                continue
            elif guess > target:
                print("Too large!")
                continue
            elif guess == target:
                print("Just right!")
                quit()
            else:
                print('something unexpected happened')

    except ValueError:
        continue