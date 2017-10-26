import random
from random import randint

guess_count = 1
#initialises the guess count to 1 and increment for every wrong input attempt

my_random = random.randint(1,5)
#a random int is selected between 1 and 5, inclusive

random_guess = int(input("Guess my random number: "))
#a variable to require an input for each guess until the user is correct

while(random_guess != my_random):
    if(random_guess > my_random):
        print("Your guess was higher than my number. Try again.")
    else:
        print("Your guess was lower than my number. Try again.")
    guess_count += 1
    break
#while the input is not the correct number, it will check whether the guess was higher or lower and return a response

if(random_guess == my_random):
    print("Correct!")
    print("Your guess count was: " + str(guess_count))
#informs when the user is correct and displays the total amount of guesses

#    if(guess_count == 5):
#        print("Your guess count was: " + str(guess_count))
##intial loop breaker for v1


#random guess checker
#yay
