import math
from lib.HammingDistance import hammingDistance


def distanceBetweenPatternAndStrings(pattern, Dnas):
  k = len(pattern)
  dist = 0
  for Dna in Dnas:
    min_h_dist = math.inf
    for i in range(len(Dna) - k + 1):
      pattern_Dna = Dna[i:i+k]
      h_dist = hammingDistance(pattern, pattern_Dna)
      if min_h_dist > h_dist:
        min_h_dist = h_dist
    dist += min_h_dist
  return dist

f = open("./data/dataset_5164_1.txt", "r")
pattern = f.readline()[:-1]
Dnas = f.readline()[:-1]
Dnas = list(Dnas.split(' '))
print(len(Dnas))
print(distanceBetweenPatternAndStrings(pattern, Dnas))
