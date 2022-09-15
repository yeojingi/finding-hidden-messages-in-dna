def patternMatching (pattern, text):
  indecies = []

  patternLength = len(pattern)
  for i in range(len(text) - patternLength +1):
    if pattern == text[i:i+patternLength]:
      indecies.append(i)

  return indecies


# 아래 주석을 해제 하면, Vibrio cholerae 유전체를 통해 실습한 결과를 볼 수 있습니다.
# f = open("./dataset/Vibrio_cholerae.txt", "r")
# param1 = f.readline()[:-1]
# print(*patternMatching("CTTGATCAT", param1), sep=" ")