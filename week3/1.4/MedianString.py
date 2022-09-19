import math
from lib.Neighbors import neighbors
from lib.HammingDistance import hammingDistance


def medianString(Dnas, k):
  patterns = neighbors("A" * k, k)
  median = ""
  dist = math.inf

  for pattern in patterns:
    d = 0
    for Dna in Dnas:
      d += distance(Dna, pattern)
    
    if dist > d:
      dist = d
      median = pattern

  return median

def distance(Dna, pattern):
  k = len(pattern)
  minD = math.inf 

  for i in range(len(Dna) - k + 1):
    text = Dna[i:i+k]
    d = hammingDistance(text, pattern)
    if minD > d:
      minD = d
  
  return minD

f = open("./data/quiz.txt", "r")
k = int(f.readline()[:-1])
Dnas = list(f.readline()[:-1].split(' '))
print(medianString(Dnas, k))

# print(hammingDistance("GAC", "GAC"))
# print(distance("AAATTGACGCAT", "GAC"))