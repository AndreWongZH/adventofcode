data1 = ''
data2 = ''

with open('input2.txt', 'r') as fileopen:
    data1 = fileopen.readline()
    data2 = fileopen.readline()

lst1 = data1.split(',')
lst2 = data2.split(',')

x = 10000
y = 10000

arr = [[0 for x in range(20000)] for y in range(20000)]

for word in lst1:
  if word[0] == 'R':
    for i in range(1, int(word[1:])+1):
      if arr[x][y + i] == '*':
        arr[x][y + i] = 'X'
      elif arr[x - i][y] == 'X':
        pass
      else:
        arr[x][y + i] = '-'
    y += int(word[1:])

  elif word[0] == 'L':
    for i in range(1, int(word[1:])+1):
      if arr[x][y - i] == '*':
        arr[x][y - i] = 'X'
      elif arr[x - i][y] == 'X':
        pass
      else:
        arr[x][y - i] = '-'
    y -= int(word[1:])

  elif word[0] == 'U':
    for i in range(1, int(word[1:])+1):
      if arr[x - i][y] == '*':
        arr[x - i][y] = 'X'
      elif arr[x - i][y] == 'X':
        pass
      else:
        arr[x - i][y] = '-'
    x -= int(word[1:])

  elif word[0] == 'D':
    for i in range(1, int(word[1:])+1):
      if arr[x + i][y] == '*':
        arr[x + i][y] = 'X'
      elif arr[x + i][y] == 'X':
        pass
      else:
        arr[x + i][y] = '-'
    x += int(word[1:])

x = 10000
y = 10000
for word in lst2:
  if word[0] == 'R':
    for i in range(1, int(word[1:])+1):
      if arr[x][y + i] == '-':
        arr[x][y + i] = 'X'
      elif arr[x - i][y] == 'X':
        pass
      else:
        arr[x][y + i] = '*'
    y += int(word[1:])

  elif word[0] == 'L':
    for i in range(1, int(word[1:])+1):
      if arr[x][y - i] == '-':
        arr[x][y - i] = 'X'
      elif arr[x - i][y] == 'X':
        pass
      else:
        arr[x][y - i] = '*'
    y -= int(word[1:])

  elif word[0] == 'U':
    for i in range(1, int(word[1:])+1):
      if arr[x - i][y] == '-':
        arr[x - i][y] = 'X'
      elif arr[x - i][y] == 'X':
        pass
      else:
        arr[x - i][y] = '*'
    x -= int(word[1:])

  elif word[0] == 'D':
    for i in range(1, int(word[1:])+1):
      if arr[x + i][y] == '-':
        arr[x + i][y] = 'X'
      elif arr[x + i][y] == 'X':
        pass
      else:
        arr[x + i][y] = '*'
    x += int(word[1:])



def findmax(x, y, lst):
  count = 0;
  intx = 10000
  inty = 10000
  done = 0


  for word in lst:
    if not done:
      if word[0] == 'R':
        for i in range(1, int(word[1:]) + 1):
          if intx == x and (inty + i) == y:
            count += 1
            done = 1
            break
          else:
            count += 1
        y += int(word[1:])
      
      elif word[0] == 'L':
        for i in range(1, int(word[1:]) + 1):
          if intx == x and (inty - i) == y:
            count += 1
            done = 1
            break
          else:
            count += 1
        y -= int(word[1:])

      elif word[0] == 'U':
        for i in range(1, int(word[1:]) + 1):
          if (intx - i) == x and (inty) == y:
            count += 1
            done = 1
            break
          else:
            count += 1
        x -= int(word[1:])
      
      elif word[0] == 'D':
        for i in range(1, int(word[1:]) + 1):
          if (intx + i) == x and (inty) == y:
            count += 1
            done = 1
            break
          else:
            count += 1
        x += int(word[1:])
    else:
      break
  
  return count;

      
mattDist = 10000000
maxstep = 10000000

for x in range(20000):
  for y in range(20000):
    if arr[x][y] == 'X':
      # val = abs(x - 10000) + abs(y - 10000)
      # if val < mattDist:
      #   mattDist = val
      val = findmax(y, x, lst1) + findmax(y, x, lst2)
      if val < maxstep:
        maxstep = val
      
print(maxstep)