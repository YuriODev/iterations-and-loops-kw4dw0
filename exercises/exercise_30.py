# Your solution to Exercise 30
hours = int(input())
cells = 1
for i in range(hours):
  if i % 3 == 0:
    cells *= 2

print(cells)
