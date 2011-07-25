import os,sys
import numpy as N

# *********************
# FUNCTIONS
# *********************

def readSummaryIDSRow(imageIDs):
  ids = []
  idsFile = open(imageIDs)
  for line in idsFile.readlines():
    parts = line.replace("\x00","").split(" ")
    parts = [p for p in parts if p != ""]
    ids = map(float, parts)
    ids = map(int, ids)
  return ids

def readSummaryIDSCol(imageIDS):
  ids = []
  idsFile = open(imageIDs)
  for line in idsFile.readlines():
    line = line.replace("\n","")
    ids.append( int(float(line)) )
  return ids

def getRandomIds(num,lim):
  import random as R
  x = set()
  while len(x) < num:
    x.add( R.randint(1,lim) )
  return list(x)

# *********************
# MAIN PROGRAM
# *********************

if len(sys.argv) < 4:
  print "Use: klDivergence.py inputMatrix imageIDs (rows|cols|rand)"
  sys.exit()
matrixPath = sys.argv[1]
imageIDs = sys.argv[2]

# READ MATRIX
matrix = []
matrixFile = open(matrixPath)
for line in matrixFile.readlines():
  parts = line.replace("\n","").split(" ")
  v = map(float, parts)
  s = sum(v)
  matrix.append( [w/s for w in v] )

matrix = N.asmatrix(matrix)

# READ SUMMARY IMAGES
if sys.argv[3] == "rows":
  ids = readSummaryIDSRow(imageIDs)
elif sys.argv[3] == "cols":
  ids = readSummaryIDSCol(imageIDs)
else:
  ids = getRandomIds(int(imageIDs), int(sys.argv[3]))

# EVALUATE KL-DIV
h1 = matrix.sum(0)
h2 = N.zeros(h1.shape)
summary = []
for k in ids:
  h2 = h2 + matrix[k-1,:]
  summary.append( matrix[k-1,:] )

h1 = (h1 - h2)/(matrix.shape[0] - len(ids))
h2 = h2/len(ids)

kldiv = N.sum( N.multiply( h1, N.log((h1+1e-15)/(h2+1e-15)) ) )
inter = sum( map( min, zip(h1.A1.tolist(), h2.A1.tolist()) ) )
#print kldiv
#'''
# EVALUATE DISTANCES
distances = 0

for i in range(0,matrix.shape[0]):
  min,d = 999,0
  for j in range(0,len(summary)):
    diff = matrix[i,:] - summary[j]
    d = N.sqrt( N.dot(diff,diff.T) )
    if d[0,0] < min:
      min = d[0,0]
  distances += min

distances = distances/matrix.shape[0]

print kldiv,distances,inter
#'''
