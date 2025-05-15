
def liftOff():
  count_spaceship = 0
  for calls in range(10 , 0, -1):
     print(calls, end=" ")
     count_spaceship += 1

  print(f"\n{count_spaceship} spaceships Liftoff!")

if __name__ == '__main__':
   liftOff()