import random
# Number gessing game

def guess_number():

    unknown_number:int = random.randint(1, 99)
    print("Guess the number between (1-99)")

    while True:
    
         gueess_number = input("Enter your guess number or press enter to exit: ")
         if gueess_number != "":
            try:   
               number:int = int(gueess_number)
               if number == unknown_number:
                  print(f"Great Guessing! Number {number}  is matched")
                  print("Thanks t use my game")
                  break
               elif number > unknown_number:
                   print(f"Your Guess is too high try again")
                
               else:
                   print(f"Your Guess is too low try again")
                
            except ValueError as e:
              print("value error", e)               
         else:
           print("Good By!")
           break
         
if __name__ == '__main__':
    guess_number()



