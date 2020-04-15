def lookAndSay(number, r):
  result = []
  chars = (number + " ").split(" ")
  count = 0
  prevItem = chars[0]

  for i in range(len(chars)):
    nextItem = chars[i]
    if (nextItem == prevItem):
      count += 1
    else:
      result.append(str(count))
      result.append(prevItem)
      prevItem = nextItem
      count = 1
  return " ".join(result)

def lineSeq(sequenceNumber, line):
  result = sequenceNumber
  allLines = []
  for i in range(0, line):
    allLines.append(result)
    result = lookAndSay(result,sequenceNumber)
  return allLines

