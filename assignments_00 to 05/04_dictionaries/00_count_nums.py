


def get_values():

   number_list = []
   while True:
      user_number = input("Enter a number: ")

      if user_number != "":
         list_num = int(user_number)
         number_list.append(list_num)
      else:
          break
   return number_list


def number_collection(number_list):
   
   num_dict = {}
   for num in number_list:
      if num not in num_dict:
         num_dict[num] = 1
      else:
         num_dict[num] += 1 
   return num_dict      
             

def number_count(num_dict):
   for num in num_dict:
      print(f"{num} => apeared: {num_dict[num]} times.", end=" " )


def initializ_programe():
   data = get_values()
   data_1 = number_collection(data)
   number_count(data_1)


if __name__ == '__main__':
   initializ_programe()
