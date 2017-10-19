my_name = 'Sam O'
my_age = 21
my_height = 185 #cm
my_weight = 100 #kg
my_eyes = 'Grayish Blue'
my_hair = 'Hazel'
is_heavy = my_weight > 500
my_weight_imperial = my_weight * 2.2
my_height_imperial = my_height / 2.54

print(f"Let's talk about {my_name}.")
print(f"He is {my_height_imperial} inches tall.")
print(f"He's {my_weight_imperial} pounds heavy.")
print(f"It is {is_heavy} that he is overweight.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")

total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height} and {my_weight}, I get {total}.")
