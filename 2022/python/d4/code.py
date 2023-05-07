inputs = open("file.txt")

# part 1
# count = 0
# for line in inputs:
#   p1, p2 = line.strip().split(",")
#   p1s, p1e = p1.split("-")
#   p1s = int(p1s)
#   p1e = int(p1e)
#   p2s, p2e = p2.split("-")
#   p2s = int(p2s)
#   p2e = int(p2e)
#   if p1s <= p2s and p1e >= p2e:
#     count += 1
#   elif p2s <= p1s and p2e >= p1e:
#     count += 1
  
# print(count)


# part 2

count = 0
for line in inputs:
  p1, p2 = line.strip().split(",")
  p1s, p1e = p1.split("-")
  p1s = int(p1s)
  p1e = int(p1e)
  p2s, p2e = p2.split("-")
  p2s = int(p2s)
  p2e = int(p2e)

  if p1s <= p2s and p1e >= p2e:
    count += 1
  elif p2s <= p1s and p2e >= p1e:
    count += 1
  elif p1s <= p2s and p1e >= p2s:
    count += 1
  elif p2s <= p1s and p2e >= p1s:
    count += 1
  
print(count)