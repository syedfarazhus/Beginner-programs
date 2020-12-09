from random import randint

def rollsum(x:int):
    i = 0
    summa = 0
    while summa != x:
        summa += randint(1,6)
        i += 1
    return "it took " + str(i) + " rolls"
