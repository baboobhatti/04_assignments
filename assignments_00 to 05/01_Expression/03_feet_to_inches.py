
# calculate the inches in feets

def calculate_inches():
    feet: float = float(input("Enter number of feet: "))  
    inches : float = feet * 12 #  1 foot = 12 inches
    print(f"{feet} feet are = {inches} inches")


if __name__ =='__main__':
    calculate_inches()    


