# Your solution to Exercise 41
n = int(input())
u0 = 0
u1 = 1
u2 = u1
for _ in range(n-1):
  u2 = u1 + u0
  u0 = u1
  u1 = u2

print(u2)
