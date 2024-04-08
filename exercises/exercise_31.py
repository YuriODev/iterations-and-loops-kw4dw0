# Your solution to Exercise 31
days = int(input())
lowest = None
under_neg_15 = False


for i in range(days):
  temp = int(input())
  if lowest == None or temp < lowest:
    lowest = temp
  if temp <= -15:
    under_neg_15 = 0

print(lowest)
print("Yes"*(under_neg_15) + "No"*(not under_neg_15))
