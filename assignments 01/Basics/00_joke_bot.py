import random


sorry: str = "Sorry I only tell jokes."

def main():
    joke_list = ["Abe oo kuchaloo ke dukan", "ha to gureeb tera kya hoga", "Rafail ho gaya fail"]
    user_input = input("What do you want? ").strip().lower()
    
    if "joke" in user_input:
        joke_len = len(joke_list)
        get_joke = random.randint(1,joke_len)
        print(joke_list[get_joke]) 
        # print(joke)
    else:
        print(sorry)

if __name__ == "__main__":
    main()