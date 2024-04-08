# Your solution to Exercise 44
n = -1
arr = []
while n != 0:
  n = int(input())
  arr.append(n)
largest = 0
for i in arr:
  if i > largest:
    largest = i

print(arr.index(largest))
