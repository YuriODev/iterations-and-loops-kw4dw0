# Your solution to Exercise 5
verif = False
while not verif:
  num = int(input("Enter a positive number\n"))
  if num > 0:
    verif = True

#sum = int((num/2)*(2 + (num-1)))
sum = 0
for i in range(1, num + 1):
  sum += i

print(sum)
