your_name = input("What's your name? ")
print("Nice to meet you " + your_name + "!")

your_age = int(input("How old are you? "))
if(your_age < 21):
    print(str(your_age) + "? You are younger than me." )
elif(your_age > 21):
    print(str(your_age) + "? You are older than me.")
else:
    print(str(your_age) + "? Same age as me!")

your_height = int(input("How tall are you in centimetres? ")) #cm
if(your_height >= 190):
    print(str(your_height) + " cm is rather tall.")
elif(your_height <= 130):
    print(str(your_height) + " cm seems quite short.")
else:
    print(str(your_height) + " cm is about average.")
your_weight = int(input("How much do you weigh in kilos? ")) #kg
if(your_weight / ((your_height / 100)*(your_height / 100)) > 25):
    print("You're " + str(your_weight) + " kilos? You are rather overweight for your size.")
elif(your_weight / ((your_height / 100)*(your_height / 100)) < 18.5):
    print("You're " + str(your_weight) + " kilos? You are quite underweight for your size.")
else:
    print("You're " + str(your_weight) + " kilos? That's a healthy weight for your size.")
your_eyes = input("What colour are your eyes? ")
print(your_eyes + " is a nice colour!")
your_hair = input("What's the colour of your hair? ")
print(your_hair + " is a nice shade of colour.")
print("")
print("Thank you for your time!")
print("")

#endl
