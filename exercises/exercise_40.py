# Your solution to Exercise 40
n = int(input())
u0 = 0
u1 = 1
u2 = u1
while u2 < n:
  print(u2, end = " ")
  u2 = u1 + u0
  u0 = u1
  u1 = u2
