inputs = open("file.txt")

# part 1

# def monkey0():
#   item = monkeys[0].pop(0)
#   item = item * 17
#   item = int(item / 3)
#   if item % 3 == 0:
#     monkeys[3].append(item)
#   else:
#     monkeys[6].append(item)

# def monkey1():
#   item = monkeys[1].pop(0)
#   item = item + 2
#   item = int(item / 3)
#   if item % 13 == 0:
#     monkeys[3].append(item)
#   else:
#     monkeys[0].append(item)

# def monkey2():
#   item = monkeys[2].pop(0)
#   item = item + 1
#   item = int(item / 3)
#   if item % 2 == 0:
#     monkeys[0].append(item)
#   else:
#     monkeys[1].append(item)

# def monkey3():
#   item = monkeys[3].pop(0)
#   item = item + 7
#   item = int(item / 3)
#   if item % 11 == 0:
#     monkeys[6].append(item)
#   else:
#     monkeys[7].append(item)

# def monkey4():
#   item = monkeys[4].pop(0)
#   item = item * item
#   item = int(item / 3)
#   if item % 19 == 0:
#     monkeys[2].append(item)
#   else:
#     monkeys[5].append(item)

# def monkey5():
#   item = monkeys[5].pop(0)
#   item = item + 8
#   item = int(item / 3)
#   if item % 17 == 0:
#     monkeys[2].append(item)
#   else:
#     monkeys[1].append(item)

# def monkey6():
#   item = monkeys[6].pop(0)
#   item = item * 2
#   item = int(item / 3)
#   if item % 5 == 0:
#     monkeys[4].append(item)
#   else:
#     monkeys[7].append(item)

# def monkey7():
#   item = monkeys[7].pop(0)
#   item = item + 6
#   item = int(item / 3)
#   if item % 7 == 0:
#     monkeys[4].append(item)
#   else:
#     monkeys[5].append(item)

# monkeys = {
#   0: [59, 65, 86, 56, 74, 57,56],
#   1: [63, 83, 50, 63, 56],
#   2: [93, 79, 74, 55],
#   3: [86, 61, 67, 88, 94, 69, 56, 91],
#   4: [76, 50, 51],
#   5: [77, 76],
#   6: [74],
#   7: [86, 65, 52, 86, 91, 95],
# }

# mcount = [0] * 8

# for _ in range(20):
#   for i in range(8):
#     while monkeys[i]:
#       mcount[i] += 1
#       if i == 0:
#         monkey0()
#       elif i == 1:
#         monkey1()
#       elif i == 2:
#         monkey2()
#       elif i == 3:
#         monkey3()
#       elif i == 4:
#         monkey4()
#       elif i == 5:
#         monkey5()
#       elif i == 6:
#         monkey6()
#       elif i == 7:
#         monkey7()

# print(mcount)
    

# print(241 * 242)


# part 2

def monkey0():
  item = monkeys[0].pop(0)
  item = item * 17
  item = item % 9699690
  if item % 3 == 0:
    monkeys[3].append(item)
  else:
    monkeys[6].append(item)

def monkey1():
  item = monkeys[1].pop(0)
  item = item + 2
  item = item % 9699690
  if item % 13 == 0:
    monkeys[3].append(item)
  else:
    monkeys[0].append(item)

def monkey2():
  item = monkeys[2].pop(0)
  item = item + 1
  item = item % 9699690
  if item % 2 == 0:
    monkeys[0].append(item)
  else:
    monkeys[1].append(item)

def monkey3():
  item = monkeys[3].pop(0)
  item = item + 7
  item = item % 9699690
  if item % 11 == 0:
    monkeys[6].append(item)
  else:
    monkeys[7].append(item)

def monkey4():
  item = monkeys[4].pop(0)
  item = item * item
  item = item % 9699690
  if item % 19 == 0:
    monkeys[2].append(item)
  else:
    monkeys[5].append(item)

def monkey5():
  item = monkeys[5].pop(0)
  item = item + 8
  item = item % 9699690
  if item % 17 == 0:
    monkeys[2].append(item)
  else:
    monkeys[1].append(item)

def monkey6():
  item = monkeys[6].pop(0)
  item = item * 2
  item = item % 9699690
  if item % 5 == 0:
    monkeys[4].append(item)
  else:
    monkeys[7].append(item)

def monkey7():
  item = monkeys[7].pop(0)
  item = item + 6
  item = item % 9699690
  if item % 7 == 0:
    monkeys[4].append(item)
  else:
    monkeys[5].append(item)

monkeys = {
  0: [59, 65, 86, 56, 74, 57,56],
  1: [63, 83, 50, 63, 56],
  2: [93, 79, 74, 55],
  3: [86, 61, 67, 88, 94, 69, 56, 91],
  4: [76, 50, 51],
  5: [77, 76],
  6: [74],
  7: [86, 65, 52, 86, 91, 95],
}

mcount = [0] * 8

for _ in range(10000):
  for i in range(8):
    while monkeys[i]:
      mcount[i] += 1
      if i == 0:
        monkey0()
      elif i == 1:
        monkey1()
      elif i == 2:
        monkey2()
      elif i == 3:
        monkey3()
      elif i == 4:
        monkey4()
      elif i == 5:
        monkey5()
      elif i == 6:
        monkey6()
      elif i == 7:
        monkey7()

print(mcount)
    

print(121048 * 115140)