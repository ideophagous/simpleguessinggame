"""
A simple number guessing game
"""

from random import randint

DICE_MIN = 1
DICE_MAX = 100

def get_random():
    """
    Returns a random integer n where DICE_MIN <= n <= DICE_MAX
    """
    return randint(DICE_MIN,DICE_MAX)


def input_check(n,r):
    """
    Prints indications to the user
    Returns a number code indicating whether the guess
    is bigger, smaller, close or exactly identical to
    the correct answer
    """
    if n>r+5:
        print("Too big!")
        return 1
    elif n<r-5:
        print("Too small!")
        return 2
    elif n!=r:
        print("Close!")
        return 3
    else:
        print("Bingo!")
        return 4



if __name__ == "__main__":
    r = get_random()
    print("Random number chosen between 1 and 100")
    while True:
        n = int(input("Make a guess! "))
        x = input_check(n,r)
        if x==4:
            break
