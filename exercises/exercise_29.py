# Your solution to Exercise 29
sum = 0
sum_sq = 0
verif = False
while not verif:
  num = int(input("Enter a number: "))
  sum += num
  sum_sq += num**2
  if sum == 0:
    verif = True

print(sum_sq)
