import math
import pygal


def findDnaA(text):
  minValue = math.inf
  indecies = []
  gcs = 0
  gcsArr = [0]

  for i in range(len(text)):
    c = text[i]
    if c == 'G':
      gcs += 1
    elif c == 'C':
      gcs -= 1

    gcsArr.append(gcs)
    if minValue > gcs:
      minValue = gcs
      indecies = [i+1]
    elif minValue == gcs:
      indecies.append(i+1)
  
  
  print("line drawing..")
  line_chart = pygal.Line()
  line_chart.title = 'the number of the value of \'G-C\' in the DNA'
  line_chart.y_title = 'G-C value'
  line_chart.x_title = 'positions'
  line_chart.x_labels = map(str, range(0, len(gcsArr), 2000))
  print("x axis is added ..")
  line_chart.add('Salmonella Enterica', gcsArr[::2000])
  print("y axis is added..")
  line_chart.render_to_file('bar_chart.svg')
  print("rendered..")

  return indecies

f = open("./data/SalmonellaEnterica.txt", "r")
f.readline()
text = ""
while True:
  t = f.readline()[:-1]
  if not t:
    break
  text += t

print(findDnaA(text))