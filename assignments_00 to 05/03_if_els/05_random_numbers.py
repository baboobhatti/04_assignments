import random
# Print 10 random numbers in the range 1 to 100.

def main():
  count = 0
  for i in range(10):
       random_num = random.randint(1, 100)
       count += 1
       print(f"{(count)}: {random_num}", end=" ")

if __name__ == '__main__':
    main()