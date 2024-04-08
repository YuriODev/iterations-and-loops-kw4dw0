# Your solution to Exercise 18
days = int(input("Enter the number of days: "))
total = 0
for i in range(days):
  errors = int(input("How many errors were caught?\n"))
  total += errors
print(total)
