
max_length = 4

def shorten_list(list):
    print(f"Full list: {list}")
    last_elements = 0
    removing_items = " "
    # print(list)
    # list_len = len(list)
    while len(list) > max_length:
          last_elements += 1
          last_list_item = list.pop()
          print(f"last element of list is {last_list_item} is removed")
          print(f"{last_elements} elements are removed from the last of  list ")
          print(f"Shorted_list {list}")
    print("process end")

    # print(type(to_short_list))
    



def get_full_list():
    full_list = []
    user_value = input("Enter first item in list or press the enter to stop it: ")
    while user_value != "":
        full_list.append(user_value)
        user_value = input("Enter items in list  press the enter to stop it: ")
    return full_list    


def main():
    full_list = get_full_list()
    shorten_list(full_list)


if __name__ == '__main__':
    main()    



