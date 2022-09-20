from copy import deepcopy
import random
from lib.MakeLaplaceProfile import makeLaplaceProfile
from lib.DiceProfileMostProbableKMer import diceProfileMostProbableKMer
from lib.HammingDistance import hammingDistance

# TTGCGTTCAAGTTGC GTTAAATCAAGTAGG GTCTACTCAAGTAGG GTTCTCTCAAAGCGG GTTCTCTCATCGAGG GCAATCTCAAGTAGG GTTCTCTCAAGTCTT GTTCTCATGAGTAGG GTTCTTGTAAGTAGG GTTCTCTACTGTAGG GTTCTGAGAAGTAGG GTTCTCTCGTATAGG TTTCTCTCAAGTACC GTTCTCTCAAGCGCG GTTCATACAAGTAGG AGTCTCTCAAGTAGT GTTGATTCAAGTAGG GTTCTCCTTAGTAGG TCGCTCTCAAGTAGG GTTCATGCAAGTAGG
# TTC ATC TTC ATC TTC

def gibbsSampler(Dnas, k, t, N):
  bestMotifs = randomPickedMotifs(Dnas, k, t)
  scores = []
  for _ in range(N):
    i = random.randint(0, t-1)
    bestMotifsWithoutIth = bestMotifs[:i] + bestMotifs[i+1:]
    profile = makeLaplaceProfile(bestMotifsWithoutIth, k)
    motif = diceProfileMostProbableKMer(Dnas[i], k, profile)
    motifs = deepcopy(bestMotifs)
    motifs[i] = motif
    scores.append(score(motifs))
    if score(motifs) < score(bestMotifs):
      bestMotifs = motifs
      print(*enumerate(bestMotifs), sep="\n")
      print(score(bestMotifs), len(bestMotifsWithoutIth), len(bestMotifs), i)
      print()
  # print(*scores)
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
k, t, N = map(int, f.readline()[:-1].split(' '))
Dnas = list(f.readline()[:-1].split(' '))

bestMotifs = gibbsSampler(Dnas, k, t, N)
# for _ in range(20):
#   motifs = gibbsSampler(Dnas, k, t, N)
#   if score(motifs) < score(bestMotifs):
#     bestMotifs = motifs
#   print(_, score(motifs))

print(*bestMotifs)