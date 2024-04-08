# Your solution to Exercise 33
n = int(input())

for i in range(n):
  print("-1"*i, "0", "1 "*(n-(i+1)))
