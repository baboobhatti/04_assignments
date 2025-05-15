

def Phone_Book():

    my_phone_book = {}
    while True:
        name = input("Enter your name or press 'Enter' to stop: ")
        if name != "":
           try:
              number = (input("Enter your number: "))
              if number == "":
                 number = int(input("Please Enter your number: "))
                 number_int = int(number)
                 my_phone_book[name] = number_int               
              else:
                  number_int = int(number)           
                  my_phone_book[name] = number_int
           except ValueError as e:
               print("Invalid value: ", e)         
        else:
           print("Thanks to use")
           break
                   
    return my_phone_book  

# Phone_Book()   

def print_phone_data(phone_book_data):
    print("Phone Numbers list: ")
    for name in phone_book_data:
        print(f"name: {name} and contact: {phone_book_data[name]}")
      

def check_for_number(phone_book_data):
    name = input("Enter name: ")
    for in_contacts in phone_book_data:
        # print(in_contacts)
        if name in in_contacts:
            print(f"{in_contacts} =  {phone_book_data[in_contacts]}")
            # break      
    


def main():
    phone_num_data = Phone_Book()
    print_phone_data(phone_num_data)
    check_for_number(phone_num_data)

if __name__ == '__main__':
    main()    

