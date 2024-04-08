# Your solution to Exercise 42
n = -1
arr = []
while n != 0:
  n = int(input())
  arr.append(n)
count = 0
for i in range(len(arr)):
  if arr[i] != arr[-1]:
    if arr[i] > arr[i+1] and arr[i+1]:
      count+=1

print(count)
