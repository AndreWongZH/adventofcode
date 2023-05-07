# filename = "input.txt"
filename = "inputactual.txt"
arr = []
input = ""
f = open(filename, "r")
for x in f:
  input = x
  arr = x.split(",")
for i, x in enumerate(arr):
  arr[i] = int(x)

def part1():
  for i in range(80):
    newfishes = 0
    for idx, day in enumerate(arr):
      if day == 0:
        arr[idx] = 6
        newfishes += 1
      else:
        arr[idx] -= 1
    for i in range(newfishes):
      arr.append(8)
  print(len(arr))


# def getTotalFish(newfish):
#   for i in newfish:

lookuptable = {}
maxday = 200

def calculateNewFishes(day, timer):
  # print(day, timer)
  newfish = []
  if day != 0 and day in lookuptable:
    return lookuptable[(day, timer)]
  
  for i in range(day, maxday + 1):
    if timer == 0:
      if i + 1 <= maxday:
        newfish.append(i + 1)
      timer = 6
    else:
      timer -= 1

  recur = []
  for i in newfish:
    x = calculateNewFishes(i, 8)
    recur += x

  lookuptable[(day, timer)] = recur + newfish
  return recur + newfish

def part2():
  count = 0
  for idx, timer in enumerate(arr):
    # print(idx, timer)
    count += 1
    x = calculateNewFishes(0, timer)
    count += len(x)
  print(count)
      
  
# part1()
# part2()


def part3():
  from collections import Counter

  from itertools import count

  def build_counter_from_day0(day0): 
      return Counter(map(int,day0.split(',')))

  def run_counter(day0, mx): 
      current_state = build_counter_from_day0(day0) 
      for day in range(mx): 
          current_state[day + 7] += current_state[day]
          current_state[day + 9] += current_state[day] 
          current_state[day] = 0 
      return current_state

  print(sum(run_counter(input, 256).values()))

part3()