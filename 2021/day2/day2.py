arr = {
  "horizontal": 0,
  "vertical": 0,
  "aim": 0
}

f = open("input.txt", "r")
for x in f:
  direction, val = x.split(" ")
  val = int(val)
  if direction == "forward":
    arr["horizontal"] += val
    arr["vertical"] += (arr["aim"] * val)
  if direction == "down":
    arr["aim"] += val
  if direction == "up":
    arr["aim"] -= val

total = arr["horizontal"] * arr["vertical"]
print(total)