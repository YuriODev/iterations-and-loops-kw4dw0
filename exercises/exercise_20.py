# Your solution to Exercise 20
num = int(input("Enter a number: "))

for i in range(1, num + 1):
  print( f"{i}" * (i%2 != 0), end = " ")
