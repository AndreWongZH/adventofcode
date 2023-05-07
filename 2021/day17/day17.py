filename = "input.txt"
filename = "inputactual.txt"

area = [["."] * 165 for j in range(150)]

f = open(filename, "r")
for x in f:
  x = x.rstrip()
  _, _, x, y = x.split(" ")
  x_min, x_max = x[2:].split("..")
  y_min, y_max = y[2:].split("..")
  for i in range(int(x_min), int(x_max[:-1]) + 1):
    for j in range(-1 * int(y_max), -1 * int(y_min) + 1):
      area[j][i] = 'T'


def part1(x, y):
  highestY = 0
  positionX = 0
  positionY = 0
  hit = False
  for z in range(1000):
    positionX += x
    positionY += y
    # print(positionX, positionY)
    highestY = max(highestY, positionY)
    if positionX < 165 and positionY < 0 and positionY > -150:
      if area[-1 * positionY][positionX] == "T":
        hit = True
      area[-1 * positionY][positionX] = "#"
    if x > 0:
      x -= 1
    y -= 1
  return hit, highestY

# part1
# xpos = 0
# adder = 1
# while xpos < int(x_min):
#   xpos += adder
#   adder += 1
# adder -= 1

# for b in range(5000, -1, -1):
#   hit, maxy = part1(adder, b)
#   if hit:
#     print(maxy, b)
#     break

# def part2():


def part2(x, y):
  positionX = 0
  positionY = 0
  hit = False
  for z in range(5000):
    positionX += x
    positionY += y
    # print(positionX, positionY)
    if positionX < 165 and positionY < 0 and positionY > -150:
      if area[-1 * positionY][positionX] == "T":
        return True
      area[-1 * positionY][positionX] = "#"
    elif positionY < -160:
      # return False, highestY
      break
    if x > 0:
      x -= 1
    y -= 1
  return hit

# possibleXpos = []
# xpos = 0
# adder = 1
# while xpos < int(x_max[:-1]):
#   xpos += adder
#   if xpos > int(x_min):
#     possibleXpos.append(adder)
#   adder += 1
# for i in range(int(x_min), int(x_max[:-1]) + 1):
#   possibleXpos.append(i)
# print(possibleXpos)

count = 0
for val in range(1 , int(x_max[:-1]) + 1):
  mini = 0
  for b in range(400, -200, -1):
    hit = part2(val, b)
    if hit:
      # print(val, b)
      mini += 1
      count += 1
  # print(mini)

print(count)

a = part2(10, -2)
print(a)