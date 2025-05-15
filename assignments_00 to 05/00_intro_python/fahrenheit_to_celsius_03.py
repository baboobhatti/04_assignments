# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!)
# and outputs the temperature converted to Celsius.

def main():
    tem_fahr = int(input("Enter temperature in Fahrenheit: "))
    degrees_celsius = (tem_fahr - 32) * 5.0/9.0
    print(f"Temperature: {tem_fahr} = {degrees_celsius}")


if __name__ == '__main__':
    main()