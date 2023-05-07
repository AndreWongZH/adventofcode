# filename = "input.txt"
filename = "inputactual.txt"
debogarr = []
finalarr = []

f = open(filename, "r")
for x in f:
  x = x.rstrip()
  debog, final = x.split(" | ")
  debogarr.append(debog.split(" "))
  finalarr.append(final.split(" "))


def part1():
  count = 0
  for code in finalarr:
    # print(code)
    n = len(code)
    if n == 2 or n == 4 or n ==3 or n == 7:
      count += 1
  # print(count)

part1()

def part2():
  count = 0
  for i in range(len(finalarr)):
    analysis = debogarr[i]
    dic = {}
    while analysis:
      word = analysis.pop(0)
      n = len(word)

      if n == 2:
        dic[1] = list(word)

      if n == 4:
        if 1 in dic:
          dic[4] = list(word)
          for char in dic[1]:
            dic[4].remove(char)
          continue
        else:
          analysis.append(word)

      if n == 3:
        if 1 in dic:
          dic[7] = list(word)
          for char in dic[1]:
            dic[7].remove(char)
          continue
        else:
          analysis.append(word)

      if n == 7:
        if 1 in dic and 7 in dic and 4 in dic:
          dic[8] = list(word)
          for char in dic[1]:
            dic[8].remove(char)
          for char in dic[7]:
            dic[8].remove(char)
          for char in dic[4]:
            dic[8].remove(char)
          continue
        else:
          analysis.append(word)

      if n == 6:
        if 1 in dic and 4 in dic and 7 in dic and 8 in dic:
          wordsplited = list(word)
          for char in dic[4]:
            if char not in wordsplited:
                dic[0] = wordsplited
                continue
          for char in dic[8]:
            if char not in wordsplited:
                dic[9] = wordsplited
                continue
          for char in dic[1]:
            if char not in wordsplited:
                dic[6] = wordsplited
                continue
        else:
          analysis.append(word)

      if n == 5:
        if 1 in dic and 4 in dic and 7 in dic and 8 in dic:
          wordsplited = list(word)
          
          for char in dic[4]:
            if char not in wordsplited:
              for char2 in dic[1]:
                if char2 not in wordsplited:
                  dic[2] = wordsplited
          
          for char in dic[4]:
            if char not in wordsplited:
              for char2 in dic[8]:
                if char2 not in wordsplited:
                  dic[3] = wordsplited

          
          for char in dic[1]:
            if char not in wordsplited:
              for char2 in dic[8]:
                if char2 not in wordsplited:
                  dic[5] = wordsplited
        else:
          analysis.append(word)
          continue
    for k, v in dic.items():
      dic[k] = "".join(v)
    # print(dic)

    ans = 0
    finalval = finalarr[i]
    for idx, code in enumerate(finalval):
      n = len(code)
      if n == 2:
        ans += (1 * 10**(3-idx))
      elif n == 4:
        ans += (4 * 10**(3-idx))
      elif n == 7:
        ans += (8 * 10**(3-idx))
      elif n == 3:
        ans += (7 * 10**(3-idx))
      else:
        for j, v in dic.items():
          if "".join(sorted(list(code))) == "".join(sorted(list(v))):
            ans += (j * 10**(3-idx))
    print(ans)
    count += ans
  print(count)


part2()