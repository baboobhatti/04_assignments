# High And Low Game
import random

def low_high_game():
  print(f"🕹️ Wellcome to High and Low game 🕹️")
  print("You have only 10 rounds to score maximum")
  scorePoint = 0
  count_round = 1
  while count_round <= 5:

        print(f"\n📍Round-: {count_round} and remaining rounds: {10-count_round}")
        computer_number: int = random.randint(1, 100)
        user_number: int = random.randint(1, 100)
        print("Your number is", user_number)

        user_choice: str = input("Guess your number is higher or lower than the computer number?: ").strip().lower()
        if user_choice == "higher" and user_number > computer_number:
           print("Ooo! you are right! the computer's number is", computer_number, "less")
           scorePoint += 5
        elif user_choice == "lower" and user_number < computer_number:
            print("Ooo! you are right! the computer's number is", computer_number, "greater")
            scorePoint += 5
        elif (user_choice == "higher" or user_choice == "lower") and user_number == computer_number:
            print("You umber and opposite numver are equal")
        else:
          print("Enter a valid data")
        print(f"Your Score is {scorePoint}")
        count_round = count_round + 1
  print(f"\nYou are score {scorePoint} in {count_round-1} rounds")

if __name__ == '__main__':
   low_high_game()
