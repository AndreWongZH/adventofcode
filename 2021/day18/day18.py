filename = "input.txt"
# filename = "inputactual.txt"

numbers = []

f = open(filename, "r")
for x in f:
  x = x.rstrip()
  numbers.append(x)

print(numbers)