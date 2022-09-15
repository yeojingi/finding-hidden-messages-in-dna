from lib.FrequentWords import frequencyTable


def findClumps(text, k, L, t):
  patterns = set([])
  n = len(text)
  for i in range(n - L + 1):
    window = text[i:i+L]
    freqMap = frequencyTable(window, k)
    for key, value in freqMap.items():
      if value >= t:
        patterns.add(key)
  
  return list(patterns)

# f = open("./dataset/E_coli.txt", "r")
# text = f.readline()[:-1]
# print(findClumps(text, 9, 500, 3))