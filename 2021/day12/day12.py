# filename = "input.txt"
from collections import defaultdict
filename = "inputactual.txt"

dic = {}

f = open(filename, "r")
for x in f:
  x = x.rstrip()
  frm, to = x.split("-")
  if frm in dic:
    dic[frm].append(to)
  else:
    dic[frm] = [to]
  
  if to in dic:
    dic[to].append(frm)
  else:
    dic[to] = [frm]

print(dic)

def dfs(loc, visited):
  if loc in visited:
    return 0

  if loc == 'end':
    return 1

  if loc.islower():
    visited.add(loc)

  total = 0

  for eachloc in dic[loc]:
    total += dfs(eachloc, visited)
  
  visited.discard(loc)
  return total


def part1():
  print(dfs('start', set()))

# part1()

def dfs2(loc, visited, twiced):
  if loc == 'end':
    return 1

  if visited[loc] > 0 and twiced:
    return 0


  if loc.islower():
    visited[loc] += 1
    twiced |= visited[loc] == 2

  total = 0

  for eachloc in dic[loc]:
    if eachloc != 'start':
      total += dfs2(eachloc, visited, twiced)
  
  visited[loc] -= 1
  return total


def part2():
  print(dfs2('start', defaultdict(int), False))

part2()