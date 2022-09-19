from math import log


Motifs = [
"TCGGGGGTTTTT",
"CCGGTGACTTAC",
"ACGGGGATTTTC",
"TTGGGGACTTTT",
"AAGGGGACTTCC",
"TTGGGGACTTCC",
"TCGGGGATTCAT",
"TCGGGGATTCCT",
"TAGGGGAACTAC",
"TCGGGTATAACC"
]

N = len(Motifs)
L = len(Motifs[0])
res = 0
Map = {"A": 0, "C": 0, "G": 0, "T": 0}

for i in range(L):
  for motif in Motifs:
    Map[motif[i]] += 1
  
  for key, value in Map.items():
    res += - value / N * (log(value/N) / log(2) if value >0 else 0)

    Map[key] = 0

print(res)