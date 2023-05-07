# filename = "input.txt"
filename = "inputactual.txt"
arr = []

f = open(filename, "r")
for x in f:
  input = x
  arr = x.split(",")
for i, x in enumerate(arr):
  arr[i] = int(x)

def part1():
  # print(arr)
  maxval = max(arr)
  maxposition = -1
  maxpositionFuel = 99999999
  for position in range(maxval):
    fuel = 0
    for crab in arr:
      fuel += abs(position - crab)
    if fuel < maxpositionFuel:
      maxposition = position
      maxpositionFuel = fuel
  print(maxposition)
  print(maxpositionFuel)

def part2():
  dic = {}
  maxval = max(arr)
  maxposition = -1
  maxpositionFuel = 999999999999
  for position in range(maxval):
    fuel = 0
    for crab in arr:
      steps = abs(position - crab)
      if steps in dic:
        fuel += dic[steps]
      else:
        minifuel = 0
        for i in range(steps + 1):
          minifuel += i
        fuel += minifuel
        dic[steps] = minifuel

    if fuel < maxpositionFuel:
      maxposition = position
      maxpositionFuel = fuel
  print(maxposition)
  print(maxpositionFuel)



part1()
part2()