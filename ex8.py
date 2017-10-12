base_annual_salary = int(input("Enter your initial annual salary: "))
#input line 1 for the user, written as an integer

semi_annual_raise = float(input("Enter the percent of your semi annual raise, as a decimal: "))

salary_increase = base_annual_salary * semi_annual_raise
salary_raised = base_annual_salary + salary_increase

monthly_salary = salary_raised / 12
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
    if(month_counter % 6 == 0):
        salary_raised = salary_raised + salary_increase
        print("Salary increased as follows: " + str(salary_raised))
        print("Monthly salary print test after raises: " + str(monthly_salary))
#calculates interest and monthly saving for a deposit and increment the month counter if the 'current_savings < portion_deposit' condition is met

print("Number of months: " + str(month_counter))
#prints the total amount of months required to save, using the inputted variables

#template values: base salary = 80k, salary raise = 5%, monthly save = 10%, dream home = 800k
