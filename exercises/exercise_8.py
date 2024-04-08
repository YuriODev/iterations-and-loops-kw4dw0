# Your solution to Exercise 8
verif = False
while not verif:
  num = int(input("Enter a positive number\n"))
  if num > 0:
    verif = True

for i in range(1, num+1):
  if i % 2 == 0:
    print(i, end = " ")
