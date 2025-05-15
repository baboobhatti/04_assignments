import random

def main():
    guessing_number = random.randint(1, 99)
    print("Guess a number between 1 to 99.")
    guess = int(input("Enter a guess number: "))

    while guess != guessing_number:
        if guess < guessing_number:  
            print("Your guess is too low")
        else:
            print("Your guess is too high")
            
        print() 
        guess = int(input("Try to guess again: "))
        
    print(f"Congrats! The number has: {guessing_number} matched")


if __name__ == '__main__':
   main() 