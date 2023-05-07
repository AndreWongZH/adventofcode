# filename = "input.txt"
filename = "inputactual.txt"
arr = []
arr = [['.'] * 3000 for i in range(3000)]
folds = []

f = open(filename, "r")
isfold = False
for x in f:
  x = x.rstrip()

  if x == "":
    isfold = True
  elif isfold:
    ls = x.split(" ")
    side, val = ls[2].split('=')
    val = int(val)
    folds.append((side, val))
  else:
    a, b = x.split(',')
    a, b = int(a), int(b)
    arr[b][a] = '#'


def part1():
  r = len(arr)
  c = len(arr[0])
  while folds:
    side, val = folds.pop(0)
    if side == 'y':
      for i in range(val + 1, r):
        for j in range(c):
          if arr[i][j] == "#" or arr[val - (i - val)][j] == "#":
            arr[val - (i - val)][j] = "#"
      r = val
    elif side == 'x':
      for i in range(r):
        for j in range(val + 1, c):
          if arr[i][j] == "#" or arr[i][val - (j - val)] == "#":
            arr[i][val - (j - val)] = "#"
      c = val
  
  count = 0
  for i in range(r):
    for j in range(c):
      if arr[i][j] == "#":
        count += 1
  print(count)
  for i in arr[:r]:
    print(i[:c])

part1()