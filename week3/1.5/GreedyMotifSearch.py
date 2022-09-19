from lib.HammingDistance import hammingDistance
from ProfileMostProbableKMer import profileMostProbableKMer

def greedyMotifSearch(Dnas, k, t):
  bestMotifs = initMotifs(Dnas, k)
  for i in range(len(Dnas[0]) - k + 1):
    motifs = [ Dnas[0][i:i+k] ]
    for j in range(1, t):
      profile = makeProfiles(motifs, k)
      motif = profileMostProbableKMer(Dnas[j], k, profile)
      motifs.append(motif)
      # print(motifs, Dnas[j], profile)
    if score(motifs) < score(bestMotifs):
      bestMotifs = motifs
  
  return bestMotifs
    

def score(motifs):
  k = len(motifs[0])
  profile = makeProfiles(motifs, k)
  pattern = patternFromProfile(profile, k)
  
  sum = 0
  for motif in motifs:
    sum += hammingDistance(motif, pattern)
  return sum

def patternFromProfile(profile, k):
  pattern = ""
  for i in range(k):
    p = 0
    c = ""
    for key in profile.keys():
      cp = profile[key][i]
      if cp > p:
        p = cp
        c = key
    pattern += c
  
  return pattern

def initMotifs(Dnas, k):
  motifs = []
  for Dna in Dnas:
    motifs.append(Dna[:k])
  
  return motifs

def makeProfiles(motifs, k):
  profile = {'A': [0] * k, 'C': [0] * k, 'G': [0] * k, 'T': [0] * k}
  num = len(motifs)
  for motif in motifs:
    for i in range(len(motif)):
      c = motif[i]
      profile[c][i] += 1

  def dv(n):
    return n / num

  for key in profile.keys():
    arr = profile[key]
    profile[key] = list(map(dv, arr))
  
  return profile
  
f = open('./data/dataset_159_5.txt', 'r')
k, t = map(int, f.readline()[:-1].split(' '))
Dnas = list(f.readline()[:-1].split(' '))
print(*greedyMotifSearch(Dnas, k, t))