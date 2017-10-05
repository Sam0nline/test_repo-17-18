x = 99
my_str = "bottles"
new_str = my_str.replace("bottles","bottle")

for x in range(99,0,-1):
    print(f"{x} {my_str} of beer on the wall, {x} {my_str} of beer. Take one down, pass it around, {x-1} {my_str} of beer on the wall.")
    if(x == 1):
        print(f"{x} {new_str} of beer on the wall, {x} {new_str} of beer. So take it down, pass it around, {x-1} {new_str}s of beer on the wall!")
#string.replace("bottles","bottle")
#print("1 bottle of beer on the wall, 1 bottle of beer. Take one down, pass it around, 0 bottles of beer on the wall.")
