
# max_fibon_number = 20
def fibonaci_sequence(max_value):
    list_series = [0,1]
    while True:
       fibno_next_value = list_series[-1] + list_series[-2]
       if fibno_next_value <= max_value:
          list_series.append(fibno_next_value)
       else:
           break

    return list_series

try:
    max_value = input("Enter number to get fibno series: ")
    if __name__ == '__main__':
        max_user_value = int(max_value)
        sequence_series = fibonaci_sequence(max_user_value)
        for num in sequence_series:
          print(num)
except ValueError as e :
    print("Please Enter valid Data", e)
