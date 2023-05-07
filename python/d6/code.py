inputs = open("file.txt")

# part 1

# signal = ""

# for line in inputs:
#   signal = line.strip()

# hashmap = {}
# processed = 0
# prev = 0
# start = 0

# while True:
#   if signal[start] not in hashmap:
#     processed += 1
#     hashmap[signal[start]] = start
#     if len(hashmap.items()) == 4:
#       break
#     start += 1
#   else:
#     popidx = hashmap[signal[start]]
#     for i in range(prev, popidx + 1):
#       prev += 1
#       hashmap.pop(signal[i])

# print(processed)

# part 2

signal = ""

for line in inputs:
  signal = line.strip()

hashmap = {}
processed = 0
prev = 0
start = 0

while True:
  if signal[start] not in hashmap:
    processed += 1
    hashmap[signal[start]] = start
    if len(hashmap.items()) == 14:
      break
    start += 1
  else:
    popidx = hashmap[signal[start]]
    for i in range(prev, popidx + 1):
      prev += 1
      hashmap.pop(signal[i])

print(processed)