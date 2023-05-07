inputs = open("file.txt")

# part1
# pri = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# priority = {}
# for i, c in enumerate(pri):
#   priority[c] = i+1

# score = 0

# for line in inputs:
#   arr1 = []
#   arr2 = []
#   line = line.strip()
#   s = 0
#   e = len(line) - 1
#   while s < e:
#     if line[s] in arr2:
#       score += priority[line[s]]
#       break
#     else:  
#       arr1.append(line[s])
    
#     if line[e] in arr1:
#       score += priority[line[e]]
#       break
#     else:
#       arr2.append(line[e])
#     s += 1
#     e -= 1
    

# print(score)

# part 2
from collections import Counter

pri = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priority = {}
for i, c in enumerate(pri):
  priority[c] = i+1

score = 0
arr = []
for line in inputs:
  line = line.strip()
  arr.append(line)

for i in range(0, len(arr), 3):
  c1 = Counter(arr[i])
  c2 = Counter(arr[i+1])
  c3 = Counter(arr[i+2])

  for key in c1.keys():
    if key in c2 and key in c3:
      score += priority[key]
      break

print(score)