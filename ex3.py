cars = 100 #The variable for total cars in existence.
space_in_a_car = 4 #The variable for amount of people-space per car.
drivers = 30 #The amount of total drivers assigned to a car.
passengers = 90 #The amount of total passengers available to occupy car space.
cars_not_driven = cars - drivers #The remainder of cars remaining unoccupied by a driver.
cars_driven = drivers #The amount of currently occupied cars.
carpool_capacity = cars_driven * space_in_a_car #The amount of total space for all driven cars.
average_passengers_per_car = passengers / cars_driven #The average amount of passengers per driven car.

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
