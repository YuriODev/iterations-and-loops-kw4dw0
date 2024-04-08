# Your solution to Exercise 46
n = int(input())
d = int(input())
str_n = str(n)
str_d = str(d)
index = -1
if str_d in str_n:
  for i, num in enumerate(str_n[::-1]):
    if index == -1 and num == str_d:
      index = i + 1


print(index)
