arr = []

f = open("input.txt", "r")
for x in f:
  arr.append(int(x))

# print(arr)
# arr = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
count = 0
start = 0
end = 2
for i in range(len(arr) - 3):
  if arr[start] < arr[end + 1]:
      count += 1
  start += 1
  end += 1

print(count)