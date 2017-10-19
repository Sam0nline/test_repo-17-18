low_value = int(input("Enter your lowest value, between 1 and 100: "))
#user input for the lowest value within specified range
high_value = int(input("Enter your highest value, between 1 and 100: "))
#user input for the highest value within specified range

def is_fizzbuzz():
    for i in range(low_value, high_value):
        if(i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif(i % 3 == 0):
            print("Fizz")
        elif(i % 5 == 0):
            print("Buzz")
        else:
            print(i)
is_fizzbuzz()
#line 7 determines the input range from the user
#line 8 checks whether i is classified as Fizz and Buzz
#line 10 checks whether i is classified as Fizz
#line 12 checks whether i is classified as Buzz
#line 14 will just return i as an int is it doesn't satisfy any of the Fizz/Buzz conditions
