import os, sys

if len(sys.argv) < 2:
  print "Use: splitFeaturesFile.py featuresFile testIndices docsNames"
  sys.exit()

indices = open(sys.argv[2])
idx = []
for line in indices.readlines():
  idx.append( int(line.replace("\n","")) )

docNames = open(sys.argv[3])
docs = {}
c = 1
for line in docNames.readlines():
  docs[ line.replace("\n","") ] = c
  c += 1

file = open(sys.argv[1])
training = open("database.txt", "w")
test = open("queries.txt","w")
for line in file.readlines():
  imageName = line.split(" ")[0]
  if docs[imageName] not in idx:
    training.write(line)
  else:
    test.write(line)

training.close()
test.close()
file.close()
