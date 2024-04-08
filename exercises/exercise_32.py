# Your solution to Exercise 32
verif = False
maxspeed = None
minspeed = None
over_30 = 0

while not verif:
  cars = int(input())
  if (1 <= cars <= 30):
    verif = True
    for i in range(cars):
      secondverif = False
      while not secondverif:
        speed = int(input())
        if (1 <= speed <= 300):
          secondverif = True
      if maxspeed == None or speed > maxspeed:
        maxspeed = speed
      if minspeed == None or speed < minspeed:
        minspeed = speed
      if speed <= 30:
        over_30 += 1


print(maxspeed - minspeed)
print(over_30)
