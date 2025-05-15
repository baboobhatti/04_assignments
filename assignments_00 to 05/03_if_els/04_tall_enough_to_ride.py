
def main():
    required_height = 50  # Setting the minimum height requirement

    while True:
        height_input = input("What is your height? (Press Enter to exit): ")

        if height_input == "":
            print("Thank you for use!")
            break

        try:
            height = float(height_input)
            if height >= required_height:
                print("You are allowed to ride!")
            else:
                print("Sorry! You're not allowed to ride, try next year!")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == '__main__':
    main()
