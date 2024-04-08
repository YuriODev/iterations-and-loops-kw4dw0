# Your solution to Exercise 3
verif = False
while not verif:
  num = int(input("Enter a number greater than or equal to 20\n"))
  if num >= 20:
    verif = True


for i in range(20, num + 1):
  print(i, end = " ")
