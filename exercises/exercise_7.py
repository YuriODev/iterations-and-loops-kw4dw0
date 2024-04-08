# Your solution to Exercise 7
verif = False
while not verif:
  num = int(input("Enter a positive number\n"))
  if num > 0:
    verif = True

for i in range(num):
  print("#"+" "*i + "#")
