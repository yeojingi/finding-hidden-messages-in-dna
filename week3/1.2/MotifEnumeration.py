from lib.Neighbors import neighbors

def motifEnumeration(Dnas, k, d):
  kmer_list = [set() for _ in range(len(Dnas))]
  for pos, Dna in enumerate(Dnas):
    for i in range(len(Dna) - k + 1):
      kmers = neighbors(Dna[i:i+k], d)
      for kmer in kmers:
        kmer_list[pos].add(kmer)
  
  patterns = kmer_list[0]
  for kmers in kmer_list:
    patterns = patterns.intersection(kmers)
  
  return list(patterns)

k, d = map(int, input().split(' '))
Dnas = list(input().split(' '))
print(*motifEnumeration(Dnas, k, d))