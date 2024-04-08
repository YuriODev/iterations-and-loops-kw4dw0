# Your solution to Exercise 11
verif = False
while not verif:
  upperlim = int(input("Enter the upper limit: "))
  if upperlim > 0:
    verif = True

sum = 0
for i in range(1, upperlim + 1):
  sum += (i / (i+1))

print(round(sum, 2))
