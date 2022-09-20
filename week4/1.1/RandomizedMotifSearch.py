import random
from lib.MakeLaplaceProfile import makeLaplaceProfile
from lib.ProfileMostProbableKMer import profileMostProbableKMer
from lib.HammingDistance import hammingDistance

def randomizedMotifSearch(Dnas, k, t):
  bestMotifs = randomPickedMotifs(Dnas, k, t)
  while True:
    profile = makeLaplaceProfile(bestMotifs, k)
    motifs = []
    for Dna in Dnas:
      motifs.append(profileMostProbableKMer(Dna, k, profile))
    if score(motifs) < score(bestMotifs):
      bestMotifs = motifs
    else:
      return bestMotifs
    
def score(motifs):
  k = len(motifs[0])
  profile = makeLaplaceProfile(motifs, k)
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

def randomPickedMotifs(Dnas, k, t):
  motifs = []

  for Dna in Dnas:
    r = random.randint(0, len(Dnas[0]) - k)
    motifs.append(Dna[r:r+k])

  return motifs

filename = input()
f = open(f"./data/{filename}", "r")
k, t = map(int, f.readline()[:-1].split(' '))
Dnas = list(f.readline()[:-1].split(' '))

bestMotifs = randomizedMotifSearch(Dnas, k, t)
for _ in range(1000):
  print(_)
  motifs = randomizedMotifSearch(Dnas, k, t)
  if score(motifs) < score(bestMotifs):
    bestMotifs = motifs

print(*bestMotifs)