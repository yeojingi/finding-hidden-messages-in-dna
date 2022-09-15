def patternMatching (pattern, text):
  indecies = []

  patternLength = len(pattern)
  for i in range(len(text) - patternLength +1):
    if pattern == text[i:i+patternLength]:
      indecies.append(i)

  return indecies


# f = open("./dataset/Vibrio_cholerae.txt", "r")
# param1 = f.readline()[:-1]
# # param2 = f.readline()[:-1]
# print(*patternMatching("CTTGATCAT", param1), sep=" ")