from lib.Neighbors import neighbors
from lib.ReverseComplementary import reverseComplementary


def maxMap(map):
  maxValue = 0
  for value in map.values() :
    if maxValue < value:
      maxValue = value
  return maxValue

def frequentWordsWithMismatchesAndReversed(text, k, d):
  patterns = []
  freqMap = {}
  n = len(text)
  for i in range(n-k+1):
    pattern = text[i:i+k]
    neighborhood = neighbors(pattern, d)
    for neighbor in neighborhood:
      if not freqMap.get(neighbor):
        freqMap[neighbor] = 1
      else:
        freqMap[neighbor] += 1
    
    neighborhood = neighbors(reverseComplementary(pattern), d)
    for neighbor in neighborhood:
      if not freqMap.get(neighbor):
        freqMap[neighbor] = 1
      else:
        freqMap[neighbor] += 1
  
  m = maxMap(freqMap)
  for key, value in freqMap.items():
    if value == m:
      patterns.append(key)
  
  return patterns

f = open("./data/dataset_9_10.txt", "r")
text = f.readline()[:-1]
k, d = map(int, f.readline()[:-1].split(' '))

print(*frequentWordsWithMismatchesAndReversed(text, k, d))