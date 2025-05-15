
# Write a function that takes a list of numbers and returns the sum of those numbers.

def add_many_num(numbers):
    total_num = 0
    # print(type(numbers)) #list
    for numb in numbers:
        # print(type(numb)) # int
        total_num += numb
        # return total_num
    return total_num

if __name__ == '__main__':
    numbers = [2, 3, 6, 7, 8, 4, 10, 12]
    total = (add_many_num(numbers))
    print(f"sum of total numbers is {total}.")