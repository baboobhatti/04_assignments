

def get_list():
    get_list_item =  []

    user_value = input("Enter first value in a list: ")
    while user_value:
        get_list_item.append(user_value)
        user_value = input("Enter your next value in a list: ")

    print(f"Great here is your list: {get_list_item}")

if __name__ == '__main__':
    get_list()        


