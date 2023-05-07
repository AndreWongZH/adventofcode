arr = []
numarr = []

f = open("input.txt", "r")
first = True

singleboard = []
row = 0
for x in f:
  x = x.rstrip()
  if first:
    numarr = x.split(",")
    for i, v in enumerate(numarr[:-1]):
      numarr[i] = int(v)
    first = False
  else:
    if x != "":
      rowarr = x.split(" ")

      def checkBlank(val):
        if val == "":
          return False
        return True

      rowarrfiltered = filter(checkBlank, rowarr)
      rowarrfiltered = list(rowarrfiltered)

      for i, v in enumerate(rowarrfiltered):
        rowarrfiltered[i] = int(v)
      singleboard.append(rowarrfiltered)
      row += 1
    else:
      arr.append(singleboard)
      singleboard = []
      row = 0
arr.append(singleboard)
arr.pop(0)

def part1():
  # print(numarr)
  # print(arr)
  # m is the number of boards
  m = len(arr)
  checkingArr = []

  # generate counting arrays
  for i in range(m):
    singleCheck = []
    singleCheck.append([0] * 5)
    singleCheck.append([0] * 5)
    checkingArr.append(singleCheck)
  
  visitedNum = []
  # loop numarr
  for num in numarr:
    visitedNum.append(num)
    # loop through each board
    for m, board in enumerate(arr):
      for i in range(5):
        for j in range(5):
          if board[i][j] == num:
            # increment checkingArr at row[i] and col[j] by 1 for board m
            checkingArr[m][0][i] += 1
            checkingArr[m][1][j] += 1
            
            # if we win
            if checkingArr[m][0][i] == 5 or checkingArr[m][1][j] == 5:
              total = 0
              # we have hit a winner
              for r in range(5):
                for c in range(5):
                  if board[r][c] not in visitedNum:
                    total += board[r][c]
              print(total * visitedNum[-1])
              return



def part2():
  # m is the number of boards
  m = len(arr)
  checkingArr = []

  # generate counting arrays
  for i in range(m):
    singleCheck = []
    singleCheck.append([0] * 5)
    singleCheck.append([0] * 5)
    singleCheck.append(False)
    checkingArr.append(singleCheck)

  def checkIfLastBoard():
    for i in checkingArr:
      if not i[2]:
        return False
    return True

  
  visitedNum = []
  # loop numarr
  for num in numarr:
    visitedNum.append(num)
    # loop through each board
    for m, board in enumerate(arr):
      for i in range(5):
        for j in range(5):
          if board[i][j] == num:
            # increment checkingArr at row[i] and col[j] by 1 for board m
            checkingArr[m][0][i] += 1
            checkingArr[m][1][j] += 1
            
            # if we win
            if checkingArr[m][0][i] == 5 or checkingArr[m][1][j] == 5:
              checkingArr[m][2] = True
              if checkIfLastBoard():
                total = 0
                for r in range(5):
                  for c in range(5):
                    if board[r][c] not in visitedNum:
                      total += board[r][c]
                # print(total)
                # print(visitedNum[-1])
                print(total * visitedNum[-1])
                return


part1()
part2()
