

Peturksbouipo = 16
Stanlau = 25
Mayengua = 48

def caste_vote(age):
  if age >= Peturksbouipo:
     print(f"you can caste your vote in Peturksbouipo.")
  elif age >= Stanlau:
    print(f"you can caste your vote in Stanlau.")
  elif age >= Mayengua:
    print(f"you can caste your vote in Mayengua.")
  else:
    print("You are mot eligible to cast vote in any country")


if __name__ == '__main__':
  age = int(input("Enter your age: "))
  caste_vote(age)