

def double_list_num(num_list):
    
    for index in range(len(num_list)): 
        # print(index)
        number = num_list[index]
        print(number)
        double_num = number * 2
        num_list[index] = double_num
    print(num_list)    

if __name__ == '__main__':
    double_list_num([1, 2, 3, 4, 5, 6, 7, 8, 9])

# def main():
# #     numbers: list[int] = [1, 2, 3, 4]  # Creates a list of numbers
# #     for i in range(len(numbers)):  # Loop through the indices of the list
# #         elem_at_index = numbers[i]  # Get the element at index i in the numbers list
# #         numbers[i] = elem_at_index * 2  # Set the element at index i to be equal to the previous element times 2
# #     print(numbers)  

# # if __name__ == '__main__':
# #     main()