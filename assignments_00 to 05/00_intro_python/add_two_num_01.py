# Write a Python program that takes two integer inputs from the user and calculates their sum.
# The program should perform the following tasks:

# 1. Prompt the user to enter the first number.
# 2. Read the input and convert it to an integer.
# 3. Prompt the user to enter the second number.
# 4. Read the input and convert it to an integer.
# 5. Calculate the sum of the two numbers.
# 6. Print the total sum with an appropriate message.

def add_number(num1 , num2):
    sum = f"{num1} + {num2} is equal to = {num1+num2}"
    return sum    

user_1 = int(input("Enter first number: "))
user_2 = int(input("Enter second number: "))
print(type(user_1))
sum = add_number(user_1, user_2)
print(sum)

# def add_numbers():
#     print("program adds two numbers.")
#     num1 = int(input("Enter your first number: "))
#     num2 = int(input("Enter your second number: "))
#     total = num1 + num2
#     print(type(total))
#     print("The total is " + str(total) + ".")

# if __name__ == '__main__':
#     add_numbers()