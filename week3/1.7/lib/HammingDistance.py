def hammingDistance(text1, text2):
  point = 0
  for i in range(len(text1)):
    if text1[i] != text2[i]:
      point += 1
  return point

# f = open("./data/dataset_9_3.txt", "r")
# print(hammingDistance(f.readline()[:-1], f.readline()[:-1]))
