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

# 아래 주석을 해제 하면, E coli 유전체를 통해 실습한 결과를 볼 수 있습니다.
# f = open("./dataset/E_coli.txt", "r")
# text = f.readline()[:-1]
# print(findClumps(text, 9, 500, 3))