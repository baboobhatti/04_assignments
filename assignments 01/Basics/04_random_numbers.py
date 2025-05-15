# import random

# def main():
#     count = 1
#     while count <= 10:
#         random_num = random.randint(1, 100)
#         print(f"{count}: {random_num}", end=" ")
#         count += 1

# if __name__ == '__main__':
#     main()

import random

def main():
    numbers = [random.randint(1, 100) for _ in range(10)]
    for index, num in enumerate(numbers, start=1):
        print(f"{index}: {num}", end=" ")

if __name__ == '__main__':
    main()
