import math


def minimumSkew(text):
  minValue = math.inf
  indecies = []
  gcs = 0
  for i in range(len(text)):
    c = text[i]
    if c == 'G':
      gcs += 1
    elif c == 'C':
      gcs -= 1

    if minValue > gcs:
      minValue = gcs
      indecies = [i+1]
    elif minValue == gcs:
      indecies.append(i+1)

  return indecies

# f = open("./data/E_coli.txt", "r")
# print(*minimumSkew(f.readline()[:-1]))

s = input()
print(*minimumSkew(s))