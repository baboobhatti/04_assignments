


def double_number():
   print("Enter a number and get double of each number in a loop")
   target_value = 100 # double number should be equal or greater to break the loop 
   base_value = input('Enter the number: ')

   if base_value == "":
        print("Enter coreect value")
        base_value = input("Enter a correct numeric value: ")     
   try:
      base_value = int(base_value)
      while base_value < target_value:
            
            base_value = base_value * 2
            print(base_value)
   except ValueError as e:
       if e == TypeError:
            print("Check data")
       else:  
           print("Enter valid value")  

   print("Start again")


if __name__ == '__main__':
    double_number()