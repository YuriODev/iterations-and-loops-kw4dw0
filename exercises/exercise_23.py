# Your solution to Exercise 23
num = -1
count = 0
sum = 0
while num != 0:
  num = int(input("Enter a number: "))
  if num != 0:
    sum += num
    count += 1

print(sum/count)
