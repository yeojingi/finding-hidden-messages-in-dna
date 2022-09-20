import random

def diceProfileMostProbableKMer(text, k, profile):
  pattern = ""
  sumProb = 0

  probabilitiesAndSeqs = []

  for i in range(len(text) - k + 1):
    window = text[i:i+k]
    prob = patternProbability(window, profile)
    sumProb += prob
    if len(probabilitiesAndSeqs) == 0:
      probabilitiesAndSeqs.append([prob, window])
    else:
      lastProbabilites = probabilitiesAndSeqs[-1][0]
      probabilitiesAndSeqs.append([lastProbabilites + prob, window])
  
  dice = random.random()

  for element in probabilitiesAndSeqs:
    if element[0]/sumProb > dice:
      pattern = element[1]
      break

  return pattern
    

def patternProbability(pattern, profile):
  prob = 1
  for i in range(len(pattern)):
    c = pattern[i]
    prob *= profile[c][i]
  return prob
