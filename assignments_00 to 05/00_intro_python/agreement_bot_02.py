# Write a program which asks the user what their favorite animal is,
# and then always responds with "My favorite animal is also ___!"

def main():
    print("To Knoww the favourite animal")
    user_fav:str = input("What's your favorite animal? ")
    my_fave = f"My favorite animal is also {user_fav}!"
    print(my_fave)  

if __name__ == '__main__':
    main()