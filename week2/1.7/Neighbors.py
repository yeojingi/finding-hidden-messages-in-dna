from lib.HammingDistance import hammingDistance

def suffix(pattern):
  return pattern[1:]

def firstSymbol(pattern):
  return pattern[0]

def neighbors(pattern, d):
  nucleotides = ['A', 'C', 'G', 'T']

  if d == 0:
    return pattern
  if len(pattern) == 1:
    return ['A', 'C', 'G', 'T']
  
  neighborhoods = set()
  suffixNeighbors = neighbors(suffix(pattern), d)

  for text in suffixNeighbors:
    if hammingDistance(suffix(pattern), text) < d:
      for nuc in nucleotides:
        neighborhoods.add(nuc + text)
    else:
      neighborhoods.add(firstSymbol(pattern) + text)

  return list(neighborhoods)

print(*neighbors("GCCATATG", 3))