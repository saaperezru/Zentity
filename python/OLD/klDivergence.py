import os,sys
import numpy as N
import random as R

if len(sys.argv) < 3:
  print "Use: klDivergence.py inputMatrix imageIDs"
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
ids = []
idsFile = open(imageIDs)
for line in idsFile.readlines():
  line = line.replace("\n","")
  ids.append( int(float(line)) )

# COMPUTE HISTOGRAMS
summary = []
h1 = matrix.sum(0)
h2 = N.zeros(h1.shape)
for k in ids:
  h2 = h2 + matrix[k-1,:]
  summary.append( matrix[k-1,:] )

for i in range(0,matrix.shape[0]):
  for j in range(0,len(summary)):
    diff = matrix[i,:] - summary[j]
    print diff.shape
    #d = diff*diff.T

h1 = (h1 - h2)/(matrix.shape[0] - len(ids))
h2 = h2/len(ids)

# EVALUATE KL-DIV
result = N.sum( N.multiply( h1, N.log((h1+1e-15)/(h2+1e-15)) ) )
print "Result:",result
