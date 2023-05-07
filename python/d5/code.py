inputs = open("file.txt")

# part 1

# stacknum = "123456789"
# stackdict = {}
# instr = []
# instr_now = False
# for i in stacknum:
#   stackdict[int(i)] = []

# for line in inputs:
#   if line.strip() == "":
#     instr_now = True
  
#   if not instr_now:
#     if line[1] != " ":
#       stackdict[1].append(line[1])
#     if line[5] != " ":
#       stackdict[2].append(line[5])
#     if line[9] != " ":
#       stackdict[3].append(line[9])
#     if line[13] != " ":
#       stackdict[4].append(line[13])
#     if line[17] != " ":
#       stackdict[5].append(line[17])
#     if line[21] != " ":
#       stackdict[6].append(line[21])
#     if line[25] != " ":
#       stackdict[7].append(line[25])
#     if line[29] != " ":
#       stackdict[8].append(line[29])
#     if line[33] != " ":
#       stackdict[9].append(line[33])
#   else:
#     if line.strip() != "":
#       vals = line.strip().split(" ")
#       instr.append((int(vals[1]), int(vals[3]), int(vals[5])))


# for i, val in stackdict.items():
#   val.pop()

# # print(stackdict)
# # print(instr)

# for val in instr:
#   for i in range(val[0]):
#     popped = stackdict[val[1]].pop(0)
#     stackdict[val[2]].insert(0, popped)

# res = ""
# for x in stackdict.values():
#   res += x[0]

# print(res)

# part 2

stacknum = "123456789"
stackdict = {}
instr = []
instr_now = False
for i in stacknum:
  stackdict[int(i)] = []

for line in inputs:
  if line.strip() == "":
    instr_now = True
  
  if not instr_now:
    if line[1] != " ":
      stackdict[1].append(line[1])
    if line[5] != " ":
      stackdict[2].append(line[5])
    if line[9] != " ":
      stackdict[3].append(line[9])
    if line[13] != " ":
      stackdict[4].append(line[13])
    if line[17] != " ":
      stackdict[5].append(line[17])
    if line[21] != " ":
      stackdict[6].append(line[21])
    if line[25] != " ":
      stackdict[7].append(line[25])
    if line[29] != " ":
      stackdict[8].append(line[29])
    if line[33] != " ":
      stackdict[9].append(line[33])
  else:
    if line.strip() != "":
      vals = line.strip().split(" ")
      instr.append((int(vals[1]), int(vals[3]), int(vals[5])))


for i, val in stackdict.items():
  val.pop()

# print(stackdict)
# print(instr)

for val in instr:
  lst = []
  for i in range(val[0]):
    lst.append(stackdict[val[1]].pop(0))
  stackdict[val[2]] = lst + stackdict[val[2]]

res = ""
for x in stackdict.values():
  res += x[0]

print(stackdict)
print(res)