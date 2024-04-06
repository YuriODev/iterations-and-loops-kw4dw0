# Your solution to Exercise 25
d = int(input(""))
t = int(input(""))
days = 1
while d < t:
  d += d/10
  days += 1

print(f"{round(d, 2)} km, {days} days")
