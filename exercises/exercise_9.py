# Your solution to Exercise 9
low_lim = int(input("Enter a lower limit\n"))
upp_lim = int(input("Enter an upper limit\n"))
mult = int(input("Enter the multiplying value\n"))

for num in range(low_lim, upp_lim+1):
  if num % mult == 0:
    print(num, end = " ")
