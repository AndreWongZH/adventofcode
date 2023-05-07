inputs = open("file.txt")

# part 1

# usermap = {
#   "X": 1,
#   "Y": 2,
#   "Z": 3
# }

# oppmap = {
#   "A": 1,
#   "B": 2,
#   "C": 3
# }

# score = 0
# for line in inputs:
#   opp, usr = line.strip().split(" ")
#   score += usermap[usr]
#   if oppmap[opp] == usermap[usr]:
#     score += 3
#   else:
#     if usr == "X" and opp == "C":
#       score += 6
#     elif usr == "Y" and opp == "A":
#       score += 6
#     elif usr == "Z" and opp == "B":
#       score += 6

# print(score)


# part 2

usermap = {
  "X": 0,
  "Y": 3,
  "Z": 6,
}

oppmap = {
  "A": 1,
  "B": 2,
  "C": 3
}

userplaymap = {
  "X": 0,
  "Y": 1,
  "Z": 2,
}

#    L  D  W
# R  3  1  2
# P  1  2  3
# S  2  3  1

mtx = [
  [3,1,2],
  [1,2,3],
  [2,3,1]
]

score = 0
for line in inputs:
  opp, usr = line.strip().split(" ")
  score += usermap[usr]
  score += mtx[oppmap[opp] - 1][userplaymap[usr]]

  # if oppmap[opp] == usermap[usr]:
  #   score += 3
  # else:
  #   if usr == "X" and opp == "C":
  #     score += 6
  #   elif usr == "Y" and opp == "A":
  #     score += 6
  #   elif usr == "Z" and opp == "B":
  #     score += 6

print(score)