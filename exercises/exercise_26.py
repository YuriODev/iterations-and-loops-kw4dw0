# Your solution to Exercise 26
n = int(input())
count = 0
for i in range(100, 1000):
  first, second, third = int(str(i)[0]), int(str(i)[1]), int(str(i)[2]),
  if first + second + third == n:
    count += 1

print(count)
