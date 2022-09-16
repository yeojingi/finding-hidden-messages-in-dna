def immediateNeighbors(pattern):
  Neighbors = set([pattern])
  nucleotides = ['A', 'C', 'G', 'T']
  for i in range(len(pattern)):
    symbol = pattern[i]
    for nucleotide in nucleotides:
      if symbol == nucleotide:
        continue
      neighbor = pattern[:i] + nucleotide + pattern[i+1:]
      Neighbors.add(neighbor)
  
  return Neighbors

print(immediateNeighbors("ACCC"))