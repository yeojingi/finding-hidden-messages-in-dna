from lib.FrequentWords import frequencyTable


def findClumps(text, k, L, t):
  patterns = set([])
  n = len(text)
  freqMap = frequencyTable(text[:L], k)
  for key, value in freqMap.items():
    if value >= t:
      patterns.add(key)

  for i in range(1, n - L + 1):
    freqMap[text[i-1:i+k-1]] -= 1
    newText = text[i+L-k:i+L]
    if not freqMap.get(newText):
      freqMap[newText] = 1
    else:
      freqMap[newText] += 1
    if freqMap[newText] >= t:
      patterns.add(newText)
  
  return len(patterns)

f = open("./dataset/E_coli.txt", "r")
text = f.readline()[:-1]
# params = list(map(int, f.readline()[:-1].split(' ')))
print(findClumps(text, 9, 500, 3))