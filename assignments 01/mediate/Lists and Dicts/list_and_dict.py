
# Problem #1: List Practice

# def fruit_list():
#   fruits = ['apple', 'banana', 'orange', 'grape', 'pineapple']
#   # Print the length of the list.
#   print(len(fruits))

#   # Add 'mango' at the end of the list.
#   fruits.append('mango')
#   # Print the updated list.
#   print(f"Updated fruit list: {fruits}")

# if __name__ == '__main__':
#    fruit_list()

# Problem #2: Index Game

# Access element
def access_element(my_list, index):
    if index < -len(my_list) or index >= len(my_list):
        return "Index out of range"
    return my_list[index]

def modify_element(my_list, index, new_value):
    if index < -len(my_list) or index >= len(my_list):
        return "Index out of range"
    my_list[index] = new_value
    return my_list

def slice_list(my_list, start_index, end_index):
    if start_index < -len(my_list) or end_index > len(my_list):
        return "Invalid range"
    return my_list[start_index:end_index]

# Interact to act game
def index_game():
    my_list = [10, "apple", 3.14, "banana", 42]
    while True:

        print("\nSelect an operation:\n1. Access an element\n2. Modify an element\n3. Slice the list\n4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":  # Access an element
            try:
                index = int(input("Enter the index of the element to access it: "))
                result = access_element(my_list, index)
                print(f"Element at index {index}: {result}")
            except ValueError:
                print("Please enter a valid number for the index.")

        elif choice == "2":  # Modify an element
            try:
                index = int(input("Enter the index of the element to modify: "))
                new_value = input("Enter the new value: ")
                result = modify_element(my_list, index, new_value)
                print(f"Updated list: {result}")
            except ValueError:
                print("Please enter a valid number for the index.")

        elif choice == "3":  # Slice the list to get new list
            try:
                start_index = int(input("Enter the start index: "))
                end_index = int(input("Enter the end index: "))
                result = slice_list(my_list, start_index, end_index)
                print(f"Sliced list: {result}")
            except ValueError:
                print("Please enter valid numbers for the slicing.")

        elif choice == "4":  #to left the game
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid operation to process.")

# Run the game
if __name__ == '__main__':
   index_game()
