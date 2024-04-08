# Your solution to Exercise 38
n = int(input())

str_n = str(n)
max = 0
min = 9
for num in str_n:
  if int(num) > max:
    max = int(num)
  if int(num) < min:
    min = int(num)

print((max - min) % 2 == 0)
