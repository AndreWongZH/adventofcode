filename = "input.txt"
# filename = "inputactual.txt"

code = ""

f = open(filename, "r")
for x in f:
  x = x.rstrip()
  code = x

print(code)
newcode = format(int(code, 16), "0b")
print(newcode)

versiontotal = 0

def readliteralvalue(code):
  # print(code)
  go = True
  val = ""
  i = 0
  while go and i < len(code):
    if code[i] == "1":
      go = True
    else:
      go = False
    # print(code[i+1: i+5])
    val += code[i+1: i+5]
    i += 5
  # print(val)
  # print(int(val,2))
  return i, int(val,2)


def readnewVal(code):
  global versiontotal
  print(code)
  version = code[:3]
  versionInt = int(version, 2)
  versiontotal += versionInt
  print(versionInt)
  packetID = code[3:6]
  packetIDInt = int(packetID, 2)
  print(packetIDInt)

  if packetIDInt == 4:
    bitsUsed, val = readliteralvalue(code[6:])
    # print(bitsUsed, val)
    return bitsUsed + 6
  else:
    lengthTypeID = code[6:7]
    if lengthTypeID == '0':
      # print(code[7:23])
      noOfBits = int(code[7:20] ,2)
      noOfBits2 = noOfBits
      bitsUsed = 0
      while noOfBits2 > 0:
        # print(noOfBits2)
        bitsUsed = readnewVal(code[20 + bitsUsed:])
        print("bitused: " + str(bitsUsed))
        noOfBits2 -= bitsUsed
      print("no of bits: " + str(noOfBits))
      return noOfBits + 7 + 15
    else:
      noOfPackets = int(code[7:18], 2)
      noOfBits = 0
      print("packets: " + str(noOfPackets))
      while noOfPackets > 0:
        bitsUsed = readnewVal(code[18 + noOfBits:])
        print("bitused: " + str(bitsUsed))
        noOfBits += bitsUsed
        noOfPackets -= 1
      print(noOfBits)
      return noOfBits + 7 + 11
      
print(readnewVal(newcode))
print(versiontotal)