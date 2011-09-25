import os,sys

if len(sys.argv) < 4:
  print "Use: createQRelsFile.py groundTruthMatrix documentsList testNames"
  sys.exit()

# Load data
matrixFile = open(sys.argv[1])
matrix = []
for line in matrixFile.readlines():
  binaryLabels = map(int, line.split())
  clases = [n for n in range(0,len(binaryLabels)) if binaryLabels[n] != 0]
  matrix.append(set(clases))

docsFile = open(sys.argv[2])
docs = {}
invD = []
c = 0
for line in docsFile.readlines():
  docName = int(line.replace(".txt\n",""))
  docs[ docName  ] = c
  invD.append(docName)
  c += 1

testFile = open(sys.argv[3])
test = []
for line in testFile.readlines():
  test.append(int(line.replace("\n","")))

# Generate labels
for query in test:
  queryLabels = matrix[ docs[query] ]
  for d in range(0,len(matrix)):
    if len( matrix[d].intersection(queryLabels) ) > 1:
      print query,'0',invD[d],'2'

