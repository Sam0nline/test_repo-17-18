import random
from random import randint

guess_count = 0
#initialises the guess count to 0 and increment for every wrong input attempt

random_guess = int
#states the guess input as type int, overriding any type

my_random = random.randint(1,100)
#a random int is selected between 1 and 5, inclusive

print("I have picked a random number from 1 to 100. Take a guess. \nI'll let you know if you are right and I'll guide you if you aren't.")

while(random_guess != my_random):
    random_guess = int(input("Guess my random number: "))
    guess_count += 1
    if(random_guess > my_random):
        print("Your guess was higher than my number. Try again.")
    elif(random_guess < my_random):
        print("Your guess was lower than my number. Try again.")
    else:
        break
#through line 13 to line 18, while the input is not the correct number, it will check whether the guess was higher or lower and return a response
#if the number guessed was correct, break out of the loop and conclude with a true if-true statement

if(random_guess == my_random):
    print("Correct!")
    print("Your guess count was: " + str(guess_count))
#informs when the user is correct and displays the total amount of guesses in that session
