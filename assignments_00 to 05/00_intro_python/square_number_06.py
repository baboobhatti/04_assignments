# Ask the user for a number and print its square (the product of the number times itself).
def square():
   try:  
      print("Get a square of your number")
      user_num = int(input("Enter your number here: "))
      square_number = user_num ** 2 
      print(f"Square of number {user_num} is {square_number}.")
   except ValueError:
      print("please enter valid number")

if __name__ == '__main__':
    # user_num = int(input("Enter your number here: "))
    square()
