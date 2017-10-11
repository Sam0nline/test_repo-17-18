your_name = input("What's your name? ")
print("Nice to meet you " + your_name + "!")
#requires user input via the prompt in quote marks and returns a response to that input

your_age = int(input("How old are you? "))
if(your_age < 21):
    print(str(your_age) + "? You are younger than me." )
elif(your_age > 21):
    print(str(your_age) + "? You are older than me.")
else:
    print(str(your_age) + "? Same age as me!")
#checks the user input against a condition that verifies if the value is less/greater than or equal to 21 and present a unique response to each.

your_height = int(input("How tall are you in centimetres? ")) #cm
if(your_height >= 200):
    print(str(your_height) + " cm is rather tall.")
elif(your_height <= 140):
    print(str(your_height) + " cm seems quite short.")
else:
    print(str(your_height) + " cm is about average.")
#similarly uses a triple condition verification however it allows for certain values to be included in the lesser/greater than thresholds.

your_weight = int(input("How much do you weigh in kilos? ")) #kg
if(your_weight / ((your_height / 100)*(your_height / 100)) > 25):
    print("You're " + str(your_weight) + " kilos? You are rather overweight for your size.")
elif(your_weight / ((your_height / 100)*(your_height / 100)) < 18.5):
    print("You're " + str(your_weight) + " kilos? You are quite underweight for your size.")
else:
    print("You're " + str(your_weight) + " kilos? That's a healthy weight for your size.")
#another triple condition check but this time it will calculate BMI as opposed to user's inputted weight and return with responses when calculated.

your_eyes = input("What colour are your eyes? ")
print(your_eyes + " is a nice colour!")
#a repeat of the your_name function, modified for eye colour

your_hair = input("What's the colour of your hair? ")
print(your_hair + " is a nice shade of colour.")
#a repeat of the your_hair function, modified for hair colour

print("")
print("Thank you for your time!")
print("")
#a brief message of gratitude to the user for completing the inputs successfully with deliberate line breaks
