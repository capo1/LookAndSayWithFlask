def lookAndSay(number, r):
  res = []
  chars = (number + " ").split(" ")
  count = 0
  prev = chars[0]

  for i in range(len(chars)):
    ne=chars[i]
    if (ne == prev):
      count += 1
    else:
      res.append(str(count))
      res.append(prev)
      prev = ne
      count = 1
  return " ".join(res)

def lineSeq(nu, line):
  res = nu
  All = []
  for i in range(0, line):
    All.append(res)
    res = lookAndSay(res,nu)
  return All

