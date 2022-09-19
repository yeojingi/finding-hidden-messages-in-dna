from HammingDistance import hammingDistance

def approximatePatternMatching(pattern, text, d):
  patternLength = len(pattern)
  indecies = []
  for i in range(len(text) - patternLength + 1):
    if hammingDistance(text[i:i+patternLength], pattern) <= d:
      indecies.append(i)
  return indecies

# f = open("./data/dataset_9_4.txt", "r")
# pattern = f.readline()[:-1]
# text = f.readline()[:-1]
# d = int(f.readline()[:-1])
# print(*approximatePatternMatching(pattern, text, d))