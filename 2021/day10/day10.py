# filename = "input.txt"
filename = "inputactual.txt"
arr = []

f = open(filename, "r")
for x in f:
  x = x.rstrip()
  arr.append(x)

scorelist = {
  ")": 3,
  "]": 57,
  "}": 1197,
  ">": 25137
}

scorelist2 = {
  ")": 1,
  "]": 2,
  "}": 3,
  ">": 4
}

def part1():
  score = 0
  for eachrow in arr:
    stack = []
    for i in range(len(eachrow)):
      if eachrow[i] == "(" or eachrow[i] == "{" or eachrow[i] == "[" or eachrow[i] == "<":
        stack.append(eachrow[i])
      elif eachrow[i] == ")":
        opening = stack.pop()
        if opening != "(":
          score += scorelist[eachrow[i]]
          break
      elif eachrow[i] == "}":
        opening = stack.pop()
        if opening != "{":
          score += scorelist[eachrow[i]]
          break
      elif eachrow[i] == "]":
        opening = stack.pop()
        if opening != "[":
          score += scorelist[eachrow[i]]
          break
      elif eachrow[i] == ">":
        opening = stack.pop()
        if opening != "<":
          score += scorelist[eachrow[i]]
          break
  print(score)
          
def part2():
  score = []
  for idx, eachrow in enumerate(arr):
    stack = []
    isInvalid = False
    for i in range(len(eachrow)):
      if eachrow[i] == "(" or eachrow[i] == "{" or eachrow[i] == "[" or eachrow[i] == "<":
        stack.append(eachrow[i])
      elif eachrow[i] == ")":
        opening = stack.pop()
        if opening != "(":
          isInvalid = True
          break
      elif eachrow[i] == "}":
        opening = stack.pop()
        if opening != "{":
          isInvalid = True
          break
      elif eachrow[i] == "]":
        opening = stack.pop()
        if opening != "[":
          isInvalid = True
          break
      elif eachrow[i] == ">":
        opening = stack.pop()
        if opening != "<":
          isInvalid = True
          break
    if not isInvalid:
      multiply = 0
      miniscore = 0
      while stack:
        opening = stack.pop()
        if opening == "(":
          multiply = scorelist2[")"]
        elif opening == "[":
          multiply = scorelist2["]"]
        elif opening == "<":
          multiply = scorelist2[">"]
        elif opening == "{":
          multiply = scorelist2["}"]
        miniscore = (miniscore * 5) + multiply
      score.append(miniscore)
  score.sort()
  mid = len(score) // 2
  print(score[mid])


part1()
part2()