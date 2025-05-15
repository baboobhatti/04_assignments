

def main():
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }

    total_cost = 0.0
    total_items = 0
    Counte = 0
    buying_items = {}
    for fruit_name, price in fruits.items():

        Counte += 1
        print(f"{Counte}. one {fruit_name} price is {price}$.")
        while True:
            try:
                itemS_quantity = int(input(f"How many ({fruit_name}) do you want?: "))
                if itemS_quantity < 0:
                    print("Please enter a non-negative number.")
                    continue
                buying_items[fruit_name] = itemS_quantity
                total_items += itemS_quantity
                total_cost += price * itemS_quantity
                break
            except ValueError:
                print("Invalid input. Please enter a whole number.")

    print(f"\nYour total is ${total_cost:.2f} for {total_items} items")
    print(f"Your fruits: {', '.join([f'{key} = {value}' for key, value in buying_items.items()])}")
    print("Thanks for shoping")

# Required to call main function
if __name__ == '__main__':
    main()