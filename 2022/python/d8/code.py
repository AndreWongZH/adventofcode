inputs = open("file.txt")

# part 1

# grid = []
# visible = 0

# for line in inputs:
#   linels = list(line.strip())
#   grid.append(linels)

# r,c = len(grid), len(grid[0])

# print(r, c)

# for i in range(r):
#   for j in range(c):
#     grid[i][j] = int(grid[i][j])

# for i in range(r):
#   for j in range(c):
#     curr = grid[i][j]
#     if i == 0 or i == r-1 or j == 0 or j == c-1:
#       visible += 1
#     else:
#       isVisiblel = True
#       isVisibler = True
#       isVisiblet = True
#       isVisibleb = True
#       for k in range(0, i):
#         if grid[k][j] >= curr:
#           isVisiblet = False
#       for k in range(i+1, r):
#         if grid[k][j] >= curr:
#           isVisibleb = False
#       for k in range(0, j):
#         if grid[i][k] >= curr:
#           isVisiblel = False
#       for k in range(j+1, c):
#         if grid[i][k] >= curr:
#           isVisibler = False
#       if isVisiblel or isVisibler or isVisiblet or isVisibleb:
#         visible += 1

# print(visible)

# part 2

grid = []
visible = 0

for line in inputs:
  linels = list(line.strip())
  grid.append(linels)

r,c = len(grid), len(grid[0])

print(r, c)

for i in range(r):
  for j in range(c):
    grid[i][j] = int(grid[i][j])

bestscore = 0

for i in range(r):
  for j in range(c):
    curr = grid[i][j]
    if i == 0 or i == r-1 or j == 0 or j == c-1:
      pass
    else:
      left = 0
      right = 0
      top = 0
      btm = 0
      for k in range(i-1, -1, -1):
        top += 1
        if grid[k][j] >= curr:
          break
          
      for k in range(i+1, r):
        btm += 1
        if grid[k][j] >= curr:
          break

      for k in range(j-1, -1, -1):
        left += 1
        if grid[i][k] >= curr:
          break

      for k in range(j+1, c):
        right += 1
        if grid[i][k] >= curr:
          break

      scenicscore = left * right * top * btm
      bestscore = max(bestscore, scenicscore)

print(bestscore)