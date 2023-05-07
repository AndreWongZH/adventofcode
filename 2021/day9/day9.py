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

# print(arr)



def part1():
  total = 0
  row = len(arr)
  col = len(arr[0])

  def check(val, r, c):
    if r < 0 or r >= row or c < 0 or c >= col:
      return True
    if val < arr[r][c]:
      return True
    else:
      return False

  for i in range(row):
    for j in range(col):
      if check(arr[i][j], i, j+1) and check(arr[i][j], i, j-1) and check(arr[i][j], i+1, j) and check(arr[i][j], i-1, j):
        total += arr[i][j] + 1
  print(total)



def part2():
  basin = []
  row = len(arr)
  col = len(arr[0])

  visited = set()

  def check(val, r, c):
    if r < 0 or r >= row or c < 0 or c >= col:
      return True
    if val < arr[r][c]:
      return True
    else:
      return False

  def dfs(r, c):
    if r < 0 or r >= row or c < 0 or c >= col:
      return 0
    if arr[r][c] == 9:
      return 0
    if (r,c) in visited:
      return 0
    visited.add((r,c))
    return 1 + dfs(r+1, c) + dfs(r -1, c) + dfs(r, c+1) + dfs(r, c-1)

  for i in range(row):
    for j in range(col):
      if check(arr[i][j], i, j+1) and check(arr[i][j], i, j-1) and check(arr[i][j], i+1, j) and check(arr[i][j], i-1, j):
        val = dfs(i, j)
        basin.append(val)
  basin.sort(reverse=True)
  print(basin[0] * basin[1] * basin[2])
  # print(total)

part1()
part2()
