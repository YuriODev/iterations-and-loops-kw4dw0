# Your solution to Exercise 22
num = int(input("Enter a number: "))

str_num = str(num)
for i in range(len(str_num)):
  print(str_num[:-i])
