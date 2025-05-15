
def get_last_element(list):
        
    print(f"the last element of list is {list[-1]}.")
  # print(lst[len(lst) - 1])
     
def get_last_item():
    list = [1,2,3,4,5,6,7]
    if list:
        return list

def main():
    my_list = get_last_item()
    # print(my_list)
    get_last_element(my_list)


if __name__ == '__main__':
    main()