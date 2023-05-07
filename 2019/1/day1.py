import math

counter = 0

with open('input.txt', 'r') as fileopen:
  for line in fileopen.readlines():
    val = int(line)
    while val > 0:
      val = math.floor(val / 3) - 2
      if val > 0:
        counter = counter + val

print(counter)