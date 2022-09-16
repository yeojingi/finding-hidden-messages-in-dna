from HammingDistance import hammingDistance

def approximatePatternCount(text1, pattern, d):
  patternLength = len(pattern)
  count = 0

  for i in range(len(text1) - patternLength + 1):
    if hammingDistance(pattern, text1[i:i+patternLength]) <= d:
      count += 1

  return count


f = open("./data/dataset_9_6.txt", "r")
pattern = f.readline()[:-1]
text = f.readline()[:-1]
d = int(f.readline()[:-1])
print(approximatePatternCount(text, pattern, 2))