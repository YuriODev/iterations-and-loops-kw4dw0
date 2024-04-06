# Your solution to Exercise 10
verif = False
while not verif:
  pounds = int(input("Enter the mass in pounds: "))
  if pounds > 0:
    verif = True

for mass in range(1, pounds + 1):
  print(mass, round(mass*0.453, 2))
