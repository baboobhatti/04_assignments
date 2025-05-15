# method: 01

def liftOff():
    count_spaceship = 0
    number = 10
    while number > 0:
        print(number, end=" ")
        count_spaceship += 1
        number -= 1

    print(f"\n{count_spaceship} spaceships Liftoff!")

if __name__ == '__main__':
    liftOff()


# def countdown(n):
#     if n == 0:
#         return 0
#     print(n, end=" ")
#     return 1 + countdown(n - 1)

# def liftOff():
#     count_spaceship = countdown(10)
#     print(f"\n{count_spaceship} spaceships Liftoff!")

# if __name__ == '__main__':
#     liftOff()
