

def affirmation():
    my_affirmation = "'I believe in my self that I will be the AI develoer.'"
    print("Please type the following affirmation", end="\n" + my_affirmation)
    user_affirmation = input()
    while user_affirmation != my_affirmation:
      print("That is not correct affirmation")

      print("Please type again the following affirmation", end="\n" + my_affirmation)
      user_affirmation = input()

    print("That's done in a right way")



if __name__ == '__main__':
    affirmation()
