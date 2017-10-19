import random
from random import randint

guess_count = 0

my_random = random.randint(1,5)

random_guess = int(input("Guess my random number: "))

while(random_guess != my_random):
    print("Sorry. Wrong! Try again.")
    guess_count += 1
    random_guess
    if(guess_count == 3):
        break



#random guess checker
#yay
