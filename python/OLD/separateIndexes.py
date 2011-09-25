import os, sys
import random

if len(sys.argv) < 2:
  print "Use: separateIndexes.py givenIndexes numberOfTestDocs"
  sys.exit()
else:
  indexes = open(sys.argv[1])
  testDocs = int(sys.argv[2])

# Read given indexes
keys = set()
for line in indexes.readlines():
  keys.add(int(line))

# Generate random indexes
while len(keys) < testDocs:
  k = random.randint(1,25000)
  if k not in keys:
    keys.add(k)

list = [k for k in keys]
list.sort() 
for k in list:
  print k
