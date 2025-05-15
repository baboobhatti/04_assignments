# remainder and division

def remainder_division():
    firts_num = int(input("Enter number that divide: "))
    second_num = int(input("Enter number for diviser: "))
    quotient = firts_num // second_num
    remainder = firts_num % second_num
    print(f"The result of division is {quotient} and its remainder is {remainder}")
    

if __name__ == '__main__':
    remainder_division()    