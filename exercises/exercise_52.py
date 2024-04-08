# Your solution to Exercise 52
verif = False
while not verif:
  a = int(input())
  b = int(input())
  verif = (a >= b)

for i in range(a, b - 1, -1):
  print(f"{i}"* (i % 2 != 0), end = " "*(i % 2 != 0))
