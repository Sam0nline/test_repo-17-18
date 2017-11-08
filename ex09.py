base_annual_salary = int(input("Enter your initial annual salary: "))
#input line for the user, written as an integer

semi_annual_raise = 0.07
#states the semi raise rate every 6 months after the initial salary raise by x% as a decimal

monthly_salary = base_annual_salary / 12
#calculates the monthly salary based on the annual salary entered by the user

total_cost = 1000000
#states the total cost of the house the user is attempting to pay a deposit for

portion_deposit = total_cost * 0.25
#calculates the deposit based on the total cost of the dream house

current_savings = 0
#initialises the amount currently saved by 0 at default

month_counter = 0
#initialises the month counter to 0 for the semi annual raise

num_steps = 0
#initialises the number of steps in the bisection search to 0

r = 0.04
#states an interest of current savings by x% as a decimal

low = 0
#initialises the lowest possible portion of monthly saving

high = 10000
#initialises the highest possible portion of monthly savings

guess = (high + low) / 2
#initialises the first guess for potential ideal portion of savings and reiterates the guess for each search step

decimal_guess = guess / 10000
#the program will initialise guesses as integers, during the search, they will convert into decimals to act as a percent of savings per month

epsilon = 100
#£100 leeway for the bisection search algorithm

#portion_saved = decimal_guess
#most ideal savings from monthly salary will be calculated by a bisection algorithm

while (current_savings < portion_deposit):
    current_savings = current_savings + ((current_savings * r) + (monthly_salary * decimal_guess))
    month_counter = month_counter + 1
    if(month_counter % 6 == 0):
        base_annual_salary += base_annual_salary * semi_annual_raise
        monthly_salary = base_annual_salary / 12
    if(month_counter == 36):
        while abs(current_savings - portion_deposit) >= epsilon:
            if(current_savings < portion_deposit):
                low = guess
            else:
                high = guess
            guess = guess = (high + low) / 2
            decimal_guess = guess / 10000
            num_steps += 1
    if(month_counter > 36):
        print("It is not possible to pay for the deposit in three years.")
    break
#loop is running infinitely at present (18.10.17), placing a break to prevent loss of powershell
print("Best savings rate: " + str(decimal_guess))
print("Steps in bisection search: " + str(num_steps))

"""
line 47 calculates interest and monthly saving for a deposit and increment the month counter if the 'current_savings < portion_deposit' condition is met
line 50 and 51 also calculates and updates monthly salary based on semi annual pay raises when each half year's total savings has not met the deposit condition
line 52 checks when the month counter reaches 36; if so, it will run a check whether the portion saved from the salary over 3 years has under or overachieved against the episolon value
line 53 checks if the epsilon condition is not met, it will check whether the savings fell short after 3 years; if so, the portion saved becomes the new low end of the guess
line 56 states an else query where it will state a new high end of the guess; after both checks, the next guess will be calculated as well as the portion saved during 3 years and add 1 step to the total number of steps to determine the ideal saving rate
line 62 print this statement when the starting salary is too low to save the portion_deposit over 3 years
line 65 prints the most ideal saving rate derived from the bisection algorithm
line 66 prints the total amount of steps required to achieve the saving goal if the saving rate is successful over 3 years
"""
