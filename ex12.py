night_cost = 70
New_York = 2000
Auckland = 790
Venice = 154
Glasgow = 65
economy = 1.0
premium_economy = 1.3
business = 1.6
first = 1.9
car_cost_daily = 30
breakout = 0

nights = 0
citytarget = None
flyingclass = 0
daysused = 0

#def hotel_cost(nights):
#    nights = int(input("How many nights are you staying for?"))
#    total_night_cost = nights * night_cost
#    return hotel_cost(nights)

"""
Error begins on line 19: entering an int repeats the input query until the input response fails
If input is not an int, it will print out "Value Error: invalid literal for int() with base 10: '' "
"""

#def plane_ticket_cost(citytarget,flyingclass):
#    while(citytarget != New_York or Glasgow or Auckland or Venice):
#        citytarget = input("Which city are you flying to? ")
#        if(citytarget == New_York or Glasgow or Auckland or Venice):
#            break
#        else:
#            print("Please enter a valid city.")
#            breakout += 1
#            if(breakout == 1):
#                break
#    while(flyingclass != economy or premium_economy or business or first):
#        flyingclass = float(input("Which city are you flying to? "))
#        if(flyingclass == economy or premium_economy or business or first):
#            break
#        else:
#            print("Please enter a valid city.")
#            breakout += 1
#            if(breakout == 1):
#                break
#    total_plane_cost = (citytarget * flyingclass)
#    return plane_ticket_cost(citytarget,flyingclass)

"""
Error begins on line 30: entering any str causes 1 more input query then the input response registers as a fail
It then prints out "ValueError: could not convert string to float: 'Venice' "
I can make the same assumption that this will repeat on the class input at line 39 exactly the same way
"""

#def rental_car_cost(daysused):
#    daysused = int(input("How many days will you rent a car for?"))
#    total_car_cost = daysused * car_cost_daily
#    if(daysused < 4):
#        total_car_cost = total_car_cost
#    elif(daysused > 7):
#        total_car_cost = total_car_cost - 50
#    else:
#        total_car_cost = total_car_cost - 30
#    return rental_car_cost(daysused)

"""
Error begins on line 57: entering an int repeats the input query until the input response fails
If input is not an int, it will print out "Value Error: invalid literal for int() with base 10: '' "
"""

#print("Total cost for your selected holiday: £" )

"""
Errors only begin when the print function on line 72 calls function returns
"""

#+ hotel_cost(nights) [do not delete]
#+ plane_ticket_cost(citytarget,flyingclass) [do not delete]
#+ rental_car_cost(daysused) [do not delete]

"""
Lines 78 to 80 are components of line 72 print function, they have been sliced out to test validity of each function above
"""
