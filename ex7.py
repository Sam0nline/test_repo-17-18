#Hi this is ex7.py

annual_salary = int(input("Enter your annual salary: "))
#input line 1 for the user, written as an integer

monthly_salary = annual_salary / 12
#calculates the monthly salary based on the annual salary entered by the user

portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ")) #decimal form i.e. 10% = 0.1
#input line 2 for the user, asking them how much of their monthly salary to put forward towards saving up to pay the deposit

total_cost = int(input("Enter the cost of your dream home: "))
#input line 3 for the user, written as an integer

portion_deposit = total_cost * 0.2
#calculates the deposit based on the total cost of the dream house

current_savings = 0
#initialises the amount currently saved by 0 at default

month_counter = 0
#initialises the month counter

r = 0.04
#states an interest of current savings by x% as a decimal

while (current_savings < portion_deposit):
    current_savings = current_savings + ((current_savings * r) + (monthly_salary * portion_saved))
    month_counter = month_counter + 1
#calculates interest and monthly saving for a deposit and increment the month counter if the 'current_savings < portion_deposit' condition is met

print("Number of months: " + str(month_counter))
#prints the total amount of months required to save, using the inputted variables
