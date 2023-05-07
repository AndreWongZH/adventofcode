# filename = "input.txt"
filename = "inputactual.txt"
arr = []

f = open(filename, "r")
for x in f:
  x = x.rstrip()
  arr.append(list(x))

for i in range(len(arr)):
  for j in range(len(arr[0])):
    arr[i][j] = int(arr[i][j])

# for i in arr:
#   print(i)
# print("end")

def part1():
  # print(arr)
  row = len(arr)
  col = len(arr[0])
  count = {
    "val": 0
  }
  visited = set()

  def dfs(r, c):
    # print(r, c)
    if r < 0 or r >= row or c < 0 or c >= col:
      return

    if (r,c) in visited or (r,c) in flashed:
      return

    arr[r][c] += 1
    
    if arr[r][c] > 9:
      visited.add((r,c))
      flashed.add((r,c))
      count["val"] += 1
      arr[r][c] = 0
      dfs(r+1, c)
      dfs(r-1, c)
      dfs(r, c+1)
      dfs(r, c-1)
      dfs(r+1, c+1)
      dfs(r-1, c+1)
      dfs(r+1, c-1)
      dfs(r-1, c-1)

  for b in range(100):
    flashed = set()
    allFlashed = True
    for i in range(row):
      for j in range(col):
        arr[i][j] += 1

    for i in range(row):
      for j in range(col):
        if arr[i][j] > 9:
          dfs(i,j)
          visited = set()

  print(count)

# part1()

def part2():
  # print(arr)
  row = len(arr)
  col = len(arr[0])
  count = {
    "val": 0
  }
  visited = set()

  def dfs(r, c):
    # print(r, c)
    if r < 0 or r >= row or c < 0 or c >= col:
      return

    if (r,c) in visited or (r,c) in flashed:
      return

    arr[r][c] += 1
    
    if arr[r][c] > 9:
      visited.add((r,c))
      flashed.add((r,c))
      count["val"] += 1
      arr[r][c] = 0
      dfs(r+1, c)
      dfs(r-1, c)
      dfs(r, c+1)
      dfs(r, c-1)
      dfs(r+1, c+1)
      dfs(r-1, c+1)
      dfs(r+1, c-1)
      dfs(r-1, c-1)

  for b in range(1000):
    flashed = set()
    allFlashed = True
    for i in range(row):
      for j in range(col):
        arr[i][j] += 1

    for i in range(row):
      for j in range(col):
        if arr[i][j] > 9:
          dfs(i,j)
          visited = set()
    
    for i in range(row):
      for j in range(col):
        if arr[i][j] != 0:
          allFlashed = False
    if allFlashed:
      for i in arr:
        print(i)
      print("end")
      print(b+1)
      break

  print(count)

part2()