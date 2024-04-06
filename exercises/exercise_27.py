# Your solution to Exercise 27
n = int(input())
Pi = 0
count = 1

for i in range(0, 2*n, 2):
  x = count * (i + 1)
  Pi += 4/x
  count *= -1

print(Pi)
