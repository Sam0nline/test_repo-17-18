base_annual_salary = int(input("Enter your initial annual salary: "))
#input line for the user, written as an integer

semi_annual_raise = 0.07
#states the semi raise rate every 6 months after the initial salary raise by x% as a decimal

monthly_salary = base_annual_salary / 12
#calculates the monthly salary based on the annual salary entered by the user

total_cost = 1000000
#input line 4 for the user, written as an integer

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
#the program will convert guesses as integers during the search then convert back into decimals

epsilon = undefined #£100 leeway for the bisection search algorithm

portion_saved = guess #most ideal savings from monthly salary will be calculated by a bisection algorithm

while (current_savings < portion_deposit):
    current_savings = current_savings + ((current_savings * r) + (monthly_salary * decimal_guess))
    month_counter = month_counter + 1
    if(month_counter % 6 == 0):
        base_annual_salary += base_annual_salary * semi_annual_raise
        monthly_salary = base_annual_salary / 12
#calculates interest and monthly saving for a deposit and increment the month counter if the 'current_savings < portion_deposit' condition is met
#also calculates and updates monthly salary based on semi annual pay raises when each half year's total savings has not met the deposit condition

#[DO NOT DELETE THIS FUNCTION] print("Best savings rate: " + str(ideal_saving_rate))
#[DO NOT DELETE THIS FUNCTION] print("Steps in bisection search: " + str(num_steps))

#prints the most ideal saving rate derived from the bisection algorithm
#prints the total amount of steps required to achieve the saving goal if the saving rate is successful over 3 years

#[DO NOT DELETE THIS FUNCTION] else: print("It is not possible to pay for the deposit in three years"))
