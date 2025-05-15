
def get_first_element(ist_element):
    first_item = ist_element[0]
    print(f"first element of list {first_item}")
    
def get_first():

    first_item = []
    first_element = input("Enter your first element in a lsit: ")
    while first_element != "":
        first_item.append(first_element)
        break
    return first_item

def main():
    ist_item = get_first()
    get_first_element(ist_item)

if __name__ == '__main__':
    main()    
