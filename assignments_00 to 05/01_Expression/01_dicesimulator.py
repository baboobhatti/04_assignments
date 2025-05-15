import random

def diece_rolling(num_sides):
    
    dice_1: int = random.randint(0, num_sides)
    dice_2: int = random.randint(0, num_sides)
    print(f"simulation of two dice ({dice_1} + {dice_2}) from diece_rolling() is : {dice_1 + dice_2}")

def main():
    number_main = int(input("Enter number: "))
    print("die1 in main() starts as: " + str(number_main))
    diece_rolling(number_main)
    diece_rolling(number_main)
    diece_rolling(number_main)
    print("die1 in main() is: " + str(number_main))

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()