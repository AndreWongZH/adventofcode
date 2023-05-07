filename = "input.txt"
from collections import Counter, defaultdict
from collections import Counter, defaultdict, deque
from queue import PriorityQueue
from heapq import heappop, heappush

filename = "inputactual.txt"

arr = []

f = open(filename, "r")
for x in f:
  x = x.rstrip()
  arr.append(list(x))

n = len(arr)
for i in range(n):
  for j in range(n):
    arr[i][j] = int(arr[i][j])

# for i in arr:
#   print(i)

dic = {}

# failed using dp
def part1(r, c):
  if r < 0 or c < 0 or r >= n or c >= n:
    return 10000
  
  if (r,c) in dic:
    return dic[(r,c)]
  
  if r == 0 and c == 0:
    return 0

  minval = min(part1(r, c-1), part1(r -1, c))
  # print(minval)
  if (r,c) not in dic:
    dic[(r,c)] = arr[r][c] + minval
  return arr[r][c] + minval

# print(part1(n-1, n-1))
# print(dic)

class Graph:
  def __init__(self, num_of_vertices):
    self.v = num_of_vertices
    self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
    self.visited = []
  
  def add_edge(self, u, v, weight):
    self.edge[u][v] = weight
    self.edges[v][u] = weight


def part1dijkstras():
  visited = set()
  costs = {}
  pq = PriorityQueue()
  pq.put((0, (0,0)))

  while not pq.empty():
    cost, coord = pq.get()
    x, y = coord
    if coord in visited:
      continue
    visited.add(coord)

    if coord == (n-1, n-1):
      print(cost + arr[n-1][n-1])
    
    if coord == (0,0):
      costs[ (0,0) ] = 0
    else:
      lowest_cost = 9999
      for dx, dy in [(x+1, y), (x -1 , y), (x, y+1), (x, y-1)]:
        if (dx,dy) in costs and costs[dx,dy] < lowest_cost:
          lowest_cost = costs[dx,dy]
      costs[(x,y)] = lowest_cost + arr[x][y]
    for dx, dy in [(x+1, y), (x -1 , y), (x, y+1), (x, y-1)]:
      if dx >= 0 and dx < n and dy >=0 and dy < n:
        pq.put((costs[(x,y)], (dx,dy)))


# part1dijkstras()


# print(arr[0])
for i in range(1, 5):
  for r in range(n):
    # for c in range(n * (i-1), n * (i-1) + n):
    temp = arr[r][n * (i-1) : n * (i-1) + n].copy()
    for b in range(len(temp)):
      temp[b] += 1
      if temp[b] > 9:
        temp[b] = 1
    arr[r].extend(temp)

for i in range(1, 5):
  for r in range(n * (i-1), (n * (i-1)) + n):
    temp = arr[r].copy()
    for b in range(len(temp)):
      temp[b] += 1
      if temp[b] > 9:
        temp[b] = 1
    arr.append(temp)

n = len(arr)
m = len(arr[0])
print(n, m)

# for i in arr:
#   print(i)

def part2dijkstras():
  visited = set()
  costs = {}
  pq = PriorityQueue()
  pq.put((0, (0,0)))

  while not pq.empty():
    cost, coord = pq.get()
    x, y = coord
    if coord in visited:
      continue
    visited.add(coord)

    if coord == (n-1, n-1):
      print(cost + arr[n-1][n-1])
    
    if coord == (0,0):
      costs[ (0,0) ] = 0
    else:
      lowest_cost = 9999
      for dx, dy in [(x+1, y), (x -1 , y), (x, y+1), (x, y-1)]:
        if (dx,dy) in costs and costs[dx,dy] < lowest_cost:
          lowest_cost = costs[dx,dy]
      costs[(x,y)] = lowest_cost + arr[x][y]
    for dx, dy in [(x+1, y), (x -1 , y), (x, y+1), (x, y-1)]:
      if dx >= 0 and dx < n and dy >=0 and dy < n:
        pq.put((costs[(x,y)], (dx,dy)))

part2dijkstras()