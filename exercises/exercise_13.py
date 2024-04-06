# Your solution to Exercise 13
password = int(input("Set your password: "))

verif = False
while not verif:
  attempt = int(input("Enter the password: "))
  if password != attempt:
    print("Error")
  else:
    verif = True
    print("Done")
