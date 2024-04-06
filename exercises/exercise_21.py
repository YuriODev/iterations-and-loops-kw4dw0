# Your solution to Exercise 21
num = int(input("Enter a number: "))
sum = 0

for i in range(num, 0, -1):
  factorial = 1
  for j in range(i, 0, -1):
    factorial *= j
  sum += factorial

print(sum)
