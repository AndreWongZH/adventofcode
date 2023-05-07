inputs = open("file.txt")

# part 1

# signal = 1
# cycle = 0
# q = []
# res = 0

# for line in inputs:
#   cmd = line.strip().split(" ")
#   if len(cmd) == 2:
#     q.append( [int(cmd[1]), 2] )
#   else:
#     q.append( [0, 1] )

# while q:
#   cycle += 1
#   q[0][1] -= 1

#   if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
#     # print(cycle, signal)
#     # print(cycle * signal)
#     res += (cycle * signal)

#   if q[0][1] == 0:
#     signal += q.pop(0)[0]
  
# print(res)

# part 2

signal = 1
cycle = 0
q = []

grid = ["."] * 240

for line in inputs:
  cmd = line.strip().split(" ")
  if len(cmd) == 2:
    q.append( [int(cmd[1]), 2] )
  else:
    q.append( [0, 1] )

while q:
  cycle += 1
  q[0][1] -= 1



  if q[0][1] == 0:
    signal += q.pop(0)[0]

  if signal - 1 <= (cycle % 40) <= signal + 1:
    grid[cycle] = "#"
  
for i in range(0, 240, 40):
  print("".join(grid[i : i+40]))