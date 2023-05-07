import math


def countGrp(x):
  count = 1
  while int(x) > 0:
    if int(x % 10) == int((x / 10) % 10):
        count += 1
    else:
      break
    x /= 10
    x = int(x)
  return count

def isValid(x):
  hasDouble = 0
  isIncreasing = 1
  oddGroup = False
  
  val = x
  while int(val) > 0:
    grp = countGrp(val)
    if int(val % 10) < int((val / pow(10, grp)) % 10):
      isIncreasing = 0
      break
    if grp % 2 == 0:
      hasDouble = 1
    if grp > 1 and grp % 2 == 1:
      oddGroup = True
    val /= pow(10, grp)
    val = int(val)

  if hasDouble and isIncreasing and not oddGroup:
    return 1
  else:
    return 0

count = 0

for i in range(359282, 820402):
  if isValid(i):
    count += 1

print(count)

#261 too low
#265 too low


import re
lower = 359282
upper = 820401

def check_same_increase(number):
    num = str(number)
    for i in range(5):
        if int(num[i+1]) < int(num[i]):
            return False
    return True

def check_doubles(number):
    num = str(number)
    matches = re.findall('00+|22+|33+|44+|55+|66+|77+|88+|99+', num)
    if matches and min([len(match) for match in matches])==2:
        return True
    else:
        return False

check_increasing_list = [num for num in range(lower, upper+1) if check_same_increase(num)]
double_check_list = [num for num in check_increasing_list if check_doubles(num)]

print(len(double_check_list))