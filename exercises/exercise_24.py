# Your solution to Exercise 24
num = -1
count = 0

while num != 0:
  num = int(input("Enter a number: "))
  if num != 0 and num % 2 == 0:
    count += 1

print(count)
