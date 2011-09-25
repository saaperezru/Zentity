import os, sys
import random

if len(sys.argv) < 3:
  print "Use: separateIndexes.py inputIndex numberOfDocs"
  sys.exit()
else:
  index = open(sys.argv[1])
  docs = int(sys.argv[2])

# Read given indexes
input = []
for line in index.readlines():
  input.append(int(line))

# Generate random indexes
keys = set()
while len(keys) < docs:
  k = random.randint(0,len(input))
  if input[k] not in keys:
    keys.add(input[k])

list = [k for k in keys]
list.sort()
for k in list:
  print k
