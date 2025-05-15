# Print even numbers

def even_number():
    count = 0
    for i in range(40):
        if i % 2 == 0:
            print("even number: ",i)
        count += 1
    print(f"there are {count} even numbers")                
if __name__ == '__main__':
    even_number()            

# def even_number():
#     for i in range(40):
#         print(f"even number: {i * 2}")
        

# if __name__ == '__main__':
#     even_number()        