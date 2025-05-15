
# Leap year
while True:
     year = (input("Enter a year: "))
     if year != "":
        year = int(year)
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
           print("This is a leap year")
        else:
            print("Not a leap year")
     else:
         inpu_value = "end"
         print(inpu_value)
         print("Thnks")
         break       