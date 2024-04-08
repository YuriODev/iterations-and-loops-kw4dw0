# Your solution to Exercise 36
a = int(input())
b = int(input())
addition = -1

while addition != 0:
  integer = a//b
  remainder = a%b
  addition = a - (integer * b)
  a = b
  if addition != 0:
    b = addition

print(b)
