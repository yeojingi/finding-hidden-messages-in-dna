def patternCount(text, pattern):
  count = 0
  patternLength = len(pattern)
  for i in range(len(text) - patternLength+1):
    if text[i:i+patternLength] == pattern:
      count+=1
  return count

# f = open("./dataset/dataset_2_6.txt", "r")
# print(patternCount(f.readline()[:-1], f.readline()[:-1]))