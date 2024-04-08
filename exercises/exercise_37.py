# Your solution to Exercise 37
verif = False
while not verif:
  a = int(input())
  b = int(input())
  if a > b:
    verif = True

integer = 0
remainder = 0

while a > b:
  a -= b
  integer += 1

if a != 0:
  remainder = a

print(integer, remainder)
