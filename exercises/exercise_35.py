# Your solution to Exercise 35
n = int(input())

num = 1
while len(str(num)) != n:
  num *= 10

for i in range(num*10 - 1, num - 1, -1):
  if i % 2 != 0:
    print(i, end = " ")
