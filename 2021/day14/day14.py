# filename = "input.txt"
from collections import Counter, defaultdict
filename = "inputactual.txt"

chain = ""
dic = {}

f = open(filename, "r")

ischain = True
for x in f:
  x = x.rstrip()
  if ischain:
    chain = x
    ischain = False
  else:
    if x != "":
      pair, produce = x.split(" -> ")
      pairlst = list(pair)
      pairlst.sort()
      "".join(pairlst)
      dic[pair] = produce


print(dic)
print(chain)

def part1():
  global chain
  for i in range(10):
    pairs = []
    finalstr = ""
    for i in range(len(chain) - 1):
      pairs.append(chain[i:i+2])
    for idx, i in enumerate(pairs):
      if i in dic:
        middle = dic[i]
        if idx == 0:
          finalstr += i[0] + middle + i[1]
        else:
          finalstr += middle + i[1]
      else:
        if idx == 0:
          finalstr += i
        else:
          finalstr += i[1]
    chain = finalstr

  wordcount = Counter(chain)
  count = wordcount.values()
  count = list(count)
  count.sort()
  print(count)
  print(count[-1] - count[0])
  
# part1()

def part2():
  count = defaultdict(int)
  for i in range(len(chain) - 1):
    pair = chain[i: i+2]
    count[pair] += 1

  def replace(freq: dict):
    updated_freq = freq.copy()
    for pair in freq:
      for start, end in dic.items():
        if pair == start:
          occur = freq[pair]
          updated_freq[pair] -= occur
          updated_freq[pair[0] + end] += occur
          updated_freq[end + pair[1]] += occur
          break
    return updated_freq

  for i in range(40):
    count = replace(count)
  print(count)

  finalcount = defaultdict(int)
  for pair, val in count.items():
    finalcount[pair[0]] += val
    finalcount[pair[1]] += val

  finalcount[chain[0]] += 1
  finalcount[chain[-1]] += 1
  
  finalval = finalcount.values()
  finalval = list(finalval)
  finalval.sort()
  print(finalval)
  print((finalval[-1] - finalval[0]) // 2)

# part1()
part2()