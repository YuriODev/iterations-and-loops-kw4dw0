# Your solution to Exercise 6
verif = False
while not verif:
  num = int(input("Enter a positive number\n"))
  if num > 0:
    verif = True

for i in range(1, num + 1):
  print("*"*i)
