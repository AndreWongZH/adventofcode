inputs = open("file.txt")

# part 1

# head = [0,0] 
# tail = [0,0]

# tailset = set()

# def movetail():
#   xd = abs(head[0] - tail[0])
#   yd = abs(head[1] - tail[1])
#   if (yd == 0 and xd == 1) or (yd == 1 and xd == 0) or (xd == 1 and yd == 1):
#     pass
#   else:
#     if head[1] - tail[1] == 0:
#       pass
#     elif head[1] - tail[1] > 0:
#       tail[1] += 1
#     else:
#       tail[1] -= 1
    
#     if head[0] - tail[0] == 0:
#       pass
#     elif head[0] - tail[0] > 0:
#       tail[0] += 1
#     else:
#       tail[0] -= 1
#   tailset.add(tuple(tail))

# for line in inputs:
#   move = line.strip().split(" ")
#   if move[0] == "U":
#     for i in range(int(move[1])):
#       head[0] += 1
#       movetail()
#   elif move[0] == "D":
#     for i in range(int(move[1])):
#       head[0] -= 1
#       movetail()
#   elif move[0] == "L":
#     for i in range(int(move[1])):
#       head[1] -= 1
#       movetail()
#   elif move[0] == "R":
#     for i in range(int(move[1])):
#       head[1] += 1
#       movetail()
  
# print(len(tailset))

# part 2

snake = {
  0: [0,0],
  1: [0,0],
  2: [0,0],
  3: [0,0],
  4: [0,0],
  5: [0,0],
  6: [0,0],
  7: [0,0],
  8: [0,0],
  9: [0,0],
}

tailset = set()

def movetail(sec):
  xd = abs(snake[sec-1][0] - snake[sec][0])
  yd = abs(snake[sec-1][1] - snake[sec][1])
  if (yd == 0 and xd == 1) or (yd == 1 and xd == 0) or (xd == 1 and yd == 1):
    pass
  else:
    if snake[sec-1][1] - snake[sec][1] == 0:
      pass
    elif snake[sec-1][1] - snake[sec][1] > 0:
      snake[sec][1] += 1
    else:
      snake[sec][1] -= 1
    
    if snake[sec-1][0] - snake[sec][0] == 0:
      pass
    elif snake[sec-1][0] - snake[sec][0] > 0:
      snake[sec][0] += 1
    else:
      snake[sec][0] -= 1

  if sec == 9:
    tailset.add(tuple(snake[9]))

for line in inputs:
  move = line.strip().split(" ")
  if move[0] == "U":
    for i in range(int(move[1])):
      snake[0][0] += 1
      for sec in range(1, 10):
        movetail(sec)
  elif move[0] == "D":
    for i in range(int(move[1])):
      snake[0][0] -= 1
      for sec in range(1, 10):
        movetail(sec)
  elif move[0] == "L":
    for i in range(int(move[1])):
      snake[0][1] -= 1
      for sec in range(1, 10):
        movetail(sec)
  elif move[0] == "R":
    for i in range(int(move[1])):
      snake[0][1] += 1
      for sec in range(1, 10):
        movetail(sec)
  
print(len(tailset))