inputs = open("file.txt")

grid = []

for line in inputs:
  grid.append(list(line.strip()))

row, col = len(grid), len(grid[0])
print(row, col)

start = []
end = []

for i in range(row):
  for j in range(col):
    if grid[i][j] == "S":
      start = [i, j]
      grid[i][j] = "a"
    if grid[i][j] == "E":
      end = [i, j]

print(start, end)


visited = set()
def dfs(x, y):
  if x < 0 or x >= row or y < 0 or y >= col or (x,y) in visited:
    return 0

  if grid[x][y] == "z":
    return 1

  curr = grid[x][y]
  print(curr)
  visited.add((x, y))
  t, b, l, r = 0, 0, 0, 0

  if (x+1 < row) and (grid[x+1][y] == curr or grid[x+1][y] == chr(ord(curr) + 1)):
    t = dfs(x+1, y)
  if (x-1 >= 0) and (grid[x-1][y] == curr or grid[x-1][y] == chr(ord(curr) + 1)):
    b = dfs(x-1, y)
  if (y+1 < col) and (grid[x][y+1] == curr or grid[x][y+1] == chr(ord(curr) + 1)):
    r = dfs(x, y+1)
  if (y-1 >= 0) and (grid[x][y-1] == curr or grid[x][y-1] == chr(ord(curr) + 1)):
    l = dfs(x, y-1)

  if t == 0 and b == 0 and r == 0 and l == 0:
    return 0
  return 1 + max(t, b, r, l)
  return t + b + r + l + 1

print(dfs(start[0], start[1]))