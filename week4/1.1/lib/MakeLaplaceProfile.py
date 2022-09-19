def makeLaplaceProfile(motifs, k):
  profile = {'A': [1] * k, 'C': [1] * k, 'G': [1] * k, 'T': [1] * k}
  num = len(motifs) * 2
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