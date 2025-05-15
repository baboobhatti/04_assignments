
def double_number():
   double_number_list = []
   try:
      user_value = int(input("Enter a number less than 100: "))
      while user_value < 100:
           user_value = user_value * 2
           double_number_list.append(user_value)
           print(user_value, end=" ")
      print("Thanks")
      return double_number_list
   except ValueError as e :
      print("Invalid Data" , e)

if __name__ == '__main__':
  number_list = double_number()
  print(number_list)
