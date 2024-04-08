# Your solution to Exercise 39
n = int(input())

if n < 0:
  n *= -1

str_n = str(n)
sum = 0

for num in str_n:
  sum += int(num)

print(sum)
