def reverseComplementary(text):
  comp = {"A": "T", "T": "A", "C": "G", "G":"C"}
  newStrand = ""

  for i in range(len(text)):
    newStrand += comp[text[-i-1]]
  
  return newStrand