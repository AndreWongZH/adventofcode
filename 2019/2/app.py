def findans(x,y):
  data = ''

  with open('input.txt', 'r') as fileopen:
      data = fileopen.readline()

  lst = []

  lst = data.split(',')

  for i in range(len(lst)):
    lst[i] = int(lst[i])

  lst[1] = x
  lst[2] = y

  count = 0;
  val = 0;

  while count < len(lst):
    if lst[count] == 99:
      break

    elif lst[count] == 1:
      val = lst[lst[count + 1]] + lst[lst[count + 2]]
      lst[lst[count + 3]] = val
      count += 4

    elif lst[count] == 2:
      val = lst[lst[count + 1]] * lst[lst[count + 2]]
      lst[lst[count + 3]] = val
      count += 4

    else:
      count += 1

  return lst[0]

for i in range(100):
  for j in range(100):
    if findans(i, j) == 19690720:
      print(i, j)
      print(100 * i + j)

