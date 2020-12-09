from random import randint

def diceroll():
    i = 0
    roll = 0
    while roll != 6:
        roll = randint(1,6)
        i += 1
        print(roll)
    return "It took " + str(i) + " rolls"
