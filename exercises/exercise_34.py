# Your solution to Exercise 34
n = int(input())

arr = []

for i in range(1, n+1):
  arr.append(i)
  for j in arr:
    print(j, end = "") if j != arr[-1] else print(j, end = "\n")
