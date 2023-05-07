arr = []

filename = 'inputactual.txt'
# filename = 'input.txt'
gridsize = 999

f = open(filename, "r")
for x in f:
  x.rstrip()
  arrstr = x.split(" -> ")
  x1, y1 = arrstr[0].split(",")
  x2, y2 = arrstr[1].split(",")
  
  arr.append([(int(x1), int(y1)), (int(x2), int(y2))])


def part1():
  count = 0
  grid = [[0] * gridsize for j in range(gridsize)]
  for pairs in arr:
    x1, y1 = pairs[0]
    x2, y2 = pairs[1]
    if x1 == x2:
      # vertical difference
      if y1 < y2:
        for k in range(y1, y2 + 1):
          grid[k][x1] += 1
      else:
        for k in range(y2, y1 + 1):
          grid[k][x1] += 1
    elif y1 == y2:
      # horizontal
      if x1 < x2:
        for k in range(x1, x2 + 1):
          grid[y1][k] += 1
      else:
        for k in range(x2, x1 + 1):
          grid[y1][k] += 1
    else:
      if x1 < x2 and y1 < y2:
        while x1 != x2+1 and y1 != y2+1:
        # for p in range(y1, y2 + 1):
        # for k in range(x1, x2 + 1):
          grid[y1][x1] += 1
          x1 += 1
          y1 += 1
      elif x1 > x2 and y1 > y2:
        while x1 != x2-1 and y1 != y2-1:
        # for p in range(y2, y1 + 1):
        #   for k in range(x2, x1 + 1):
          grid[y1][x1] += 1
          x1 -= 1
          y1 -= 1
      elif x1 < x2 and y1 > y2:
        while x1 != x2 + 1 and y1 != y2 - 1:
        # for p in range(y1, y2 - 1, -1):
        #   for k in range(x1, x2 + 1):
          grid[y1][x1] += 1
          x1 += 1
          y1 -= 1
      elif x1 > x2 and y1 < y2:
        while x1 != x2 - 1 and y1 != y2 + 1:
        # for p in range(y1, y2 + 1):
        #   for k in range(x1, x2 - 1, -1):
          grid[y1][x1] += 1
          x1 -= 1
          y1 += 1
  
  for i in range(gridsize):
    for j in range(gridsize):
      if grid[i][j] >= 2:
        count += 1
  # for i in grid:
  #   print(i)
  print(count)

part1()