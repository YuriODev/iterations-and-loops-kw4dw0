# Your solution to Exercise 47
verif = False
while not verif:
  n = int(input())
  if (1 <= n <= 100000):
    verif = True

for num in range(1, n+1):
  num = str(num)
  if num == num[::-1]:
    print(num, end = " ")
