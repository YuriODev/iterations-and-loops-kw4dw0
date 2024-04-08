# Your solution to Exercise 43
n = -1
arr = []
while n != 0:
  n = int(input())
  arr.append(n)
largest = 0
for i in arr:
  if i > largest:
    largest = i
diff = 9
num = None
for i in arr:
  if largest - i < diff and largest != i:
    diff = largest - i
    num = i

print(num)
