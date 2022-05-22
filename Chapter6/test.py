
import random

lotto = []


def getRandomNumber():
    i = 0
    while i < 6:
        
        number = random.randint(1,45)
        if( number not in lotto):
            lotto.append(number)
            i += 1
        
    return number


getRandomNumber()
lotto.sort
print(lotto)