arr = []

f = open("input.txt", "r")
for x in f:
  arr.append(x)

def part1():
  row = len(arr)
  col = len(arr[0]) - 1

  count = [0] * col

  for i in range(row):
    for j in range(col):
      if arr[i][j] == "1":
        count[j] += 1
      else:
        count[j] -= 1
  
  gamma = ""
  epsilon = ""
  for val in count:
    if val > 0:
      gamma += "1"
      epsilon += "0"
    else:
      gamma += "0"
      epsilon += "1"

  gamma = int(gamma, 2)
  print(gamma)
  print(bin(gamma))
  epsilon = int(epsilon, 2)
  print(bin(epsilon))
  print(epsilon)
  print(gamma * epsilon)


# part1()

def part2():
  row = len(arr)
  col = len(arr[0]) - 1

  k = 0
  cnt = 0
  v = ""
  total = [i for i in range(row)]
  while len(total) > 1:
    # find the max common value
    for idx in total:
      if arr[idx][k] == "1":
        cnt += 1
      else:
        cnt -= 1
    if cnt >= 0:
      v = "1"
    else:
      v = "0"

    # start deleting
    toDelete = []
    for idx in total:
      # print(arr[idx], arr[idx][i] != v)
      if arr[idx][k] != v:
        toDelete.append(idx)
    for idx in toDelete:
      total.remove(idx)

    k += 1
    cnt = 0

  oxygenRating = arr[total[0]]
  print(int(oxygenRating,2))

  k = 0
  cnt = 0
  v = ""
  total = [i for i in range(row)]
  while len(total) > 1:
    # find the max common value
    for idx in total:
      if arr[idx][k] == "1":
        cnt += 1
      else:
        cnt -= 1
    if cnt >= 0:
      v = "0"
    else:
      v = "1"

    # start deleting
    toDelete = []
    for idx in total:
      # print(arr[idx], arr[idx][i] != v)
      if arr[idx][k] != v:
        toDelete.append(idx)
    for idx in toDelete:
      total.remove(idx)
    k += 1
    cnt = 0

  carbonRating = arr[total[0]]
  print(int(carbonRating, 2))
  print(int(oxygenRating, 2) * int(carbonRating, 2))

part2()
