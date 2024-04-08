# Your solution to Exercise 45
n = -1
arr = []
while n != 0:
  n = int(input())
  arr.append(n)
changes = 0
for i in range(len(arr)):
  if arr[i] != arr[-1]:
    if (arr[i] > 0 and arr[i+1] < 0) or (arr[i] < 0 and arr[i+1] > 0):
      changes += 1

print(changes)
