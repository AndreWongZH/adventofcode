inputs = open("file.txt")

# part 1

# maxcalories = -10
# currcalories = 0

# for cal in inputs:
#   if cal.strip().isnumeric():
#     currcalories += int(cal)
#   else:
#     maxcalories = max(maxcalories, currcalories)
#     currcalories = 0

# print(maxcalories)

# part 2

import heapq

hq = []
currcalories = 0

for cal in inputs:
  if cal.strip().isnumeric():
    currcalories += int(cal)
  else:
    heapq.heappush(hq, (-1 * currcalories))
    currcalories = 0

total = 0

for _ in range(3):
  total += (-1 * heapq.heappop(hq))

print(total)