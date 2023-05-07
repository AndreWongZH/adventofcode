inputs = open("file.txt")

# part 1

# stack = []
# result = 0

# for line in inputs:
#   cmd = line.strip().split()
#   if cmd[0] == "$":
#     if cmd[1] == "ls":
#       pass
#     else:
#       if cmd[2] == "..":
#         prev = stack.pop()
#         if prev <= 100000:
#           result += prev
#         stack[-1] += prev
#       else:
#         stack.append(0)
#   else:
#     if cmd[0] == "dir":
#       pass
#     else:
#       stack[-1] += int(cmd[0])

# while stack:
#   prev = stack.pop()
#   if prev <= 100000:
#     result += prev
#   if len(stack) > 1:
#     stack[-1] += prev

# print(result)
# print(stack)


# part 2

stack = []
maxspace = 70000000
totalusedspace = 0
totalunusedspace = 0

for line in inputs:
  cmd = line.strip().split()
  if cmd[0] == "$":
    if cmd[1] == "ls":
      pass
    else:
      if cmd[2] == "..":
        prev = stack.pop()
        stack[-1] += prev
      else:
        stack.append(0)
  else:
    if cmd[0] == "dir":
      pass
    else:
      stack[-1] += int(cmd[0])

while len(stack) > 1:
  prev = stack.pop()
  stack[-1] += prev

totalusedspace = stack[0]

totalunusedspace = maxspace - totalusedspace

print(totalunusedspace)

neededamt = 30000000 - totalunusedspace
print(neededamt)

inputs = open("file.txt")

stack = []
maxdeletesize = 70000000

for line in inputs:
  cmd = line.strip().split()
  if cmd[0] == "$":
    if cmd[1] == "ls":
      pass
    else:
      if cmd[2] == "..":
        prev = stack.pop()
        if prev >= neededamt:
          maxdeletesize = min(maxdeletesize, prev)
        stack[-1] += prev
      else:
        stack.append(0)
  else:
    if cmd[0] == "dir":
      pass
    else:
      stack[-1] += int(cmd[0])

while stack:
  prev = stack.pop()
  if prev >= neededamt:
    maxdeletesize = min(maxdeletesize, prev)
  if len(stack) > 1:
    stack[-1] += prev

print(maxdeletesize)