def guessnum(num:int) -> str:
    i = 0
    guess = 0
    while guess != num:
        guess = int(input('Guess a Number!'))
        i += 1
        if guess > num:
            print('Too High')
        elif guess < num:
            print('Too Low')
    return "Correct! It took " + str(i) + " guesses"
                      
