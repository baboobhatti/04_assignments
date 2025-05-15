

def data_copies(my_list, data):
    for i in range(5):
        my_list.append(data)

def copies():
    message = input("Enter a data to copy: ")
    copy_lsit = []
    print("List before:", copy_lsit)
    data_copies(copy_lsit, message)
    print("List after:", copy_lsit)
    copy = len(copy_lsit)
    print(f"{copy} copies of the data in a list")

if __name__ == "__main__":
    copies()