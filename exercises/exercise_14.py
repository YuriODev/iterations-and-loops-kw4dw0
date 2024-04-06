# Your solution to Exercise 14
entries = int(input("How many numbers do you want to imput?\n"))
zeroes = 0
for _ in range(entries):
  num = int(input("Enter a number: "))
  if num == 0:
    zeroes += 1

print(zeroes)
