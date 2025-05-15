
import math

def hyp_lenghth():
    ab = float(input("enter length of AB: "))
    ac = float(input("enter length of AB: "))
    bc : float = ab ** 2 + ac ** 2
    hypotenuse = math.sqrt(bc)
    print(f"L of AB is ({ab}), L of AC is ({ac}) then length of hypotenuse is {hypotenuse:.2f}")


if __name__ == '__main__':
    hyp_lenghth()    