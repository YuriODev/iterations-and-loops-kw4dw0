# Your solution to Exercise 49
a = int(input())
b = int(input())
count = 0
for num in range(a, b+1):
  num = str(num)
  if num == num[::-1]:
    print(num, end = " ")
