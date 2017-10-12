x = 99
#initialises x as a starting variable for the loop/song
my_str = "bottles"
new_str = my_str.replace("bottles","bottle")
#converts my_str to new_str when there is only 1 bottle remaining as the bottle noun becomes singular therefore should correct it grammatically

for x in range(99,0,-1):
    print(f"{x} {my_str} of beer on the wall, {x} {my_str} of beer. Take one down, pass it around, {x-1} {my_str} of beer on the wall.")
    if(x == 1):
        print(f"{x} {new_str} of beer on the wall, {x} {new_str} of beer. So take it down, pass it around, {x-1} {my_str} of beer on the wall!")
#iterates through the song, reducing the bottle count by 1 each time until there are none left
