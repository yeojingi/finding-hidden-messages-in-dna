from PatternCount import patternCount

def frequentWords(text, k):
  freqMap = {}
  frequentPatterns = []

  freqMap = frequencyTable(text, k)
  maxValue = maxMap(freqMap)
  
  for key, value in freqMap.items():
    if value == maxValue:
      frequentPatterns.append(key)
  
  return frequentPatterns

def frequencyTable(text, k):
  freqMap = {}
  for i in range(len(text) - k + 1):
    pattern = text[i:i+k]
    if not freqMap.get(pattern):
      freqMap[pattern] = 1
    else:
      freqMap[pattern] += 1
  
  return freqMap

def maxMap(freqMap):
  maxValue = 0
  for key, value in freqMap.items():
    maxValue = max(value, maxValue)

  return maxValue

# f = open("./dataset/dataset_2_13.txt", "r")
# print(*frequentWords(f.readline()[:-1], int(f.readline()[:-1])), sep="\n")