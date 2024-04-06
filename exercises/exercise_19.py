# Your solution to Exercise 19
num = int(input("Enter a number: "))
string = ""
for n in range(10, 100):
  first = int(str(n)[0])
  second = int(str(n)[1])
  if (first**2 + second**2) % num == 0:
    string += f"{n}, "

print(string[:-2])
