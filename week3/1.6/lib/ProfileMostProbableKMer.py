def profileMostProbableKMer(text, k, profile):
  maxProb = -1
  pattern = ""

  for i in range(len(text) - k + 1):
    window = text[i:i+k]
    prob = patternProbability(window, profile)
    if prob > maxProb:
      maxProb = prob
      pattern = window

  return pattern
    

def patternProbability(pattern, profile):
  prob = 1
  for i in range(len(pattern)):
    c = pattern[i]
    prob *= profile[c][i]
  return prob

# f = open("./data/dataset_159_3.txt", "r")
# text = f.readline()[:-1]
# k = int(f.readline()[:-1])
# seq = ['A', 'C', 'G', 'T']
# profile = {}

# for i in range(4):
#   row = list(map(float, f.readline()[:-1].split(' ')))
#   profile[seq[i]] = row

