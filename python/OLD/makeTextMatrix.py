import os,sys

if len(sys.argv) < 3:
  print "Use: makeTextMatrix.py documentList matrixFile"
  sys.exit()

docs = []
docFile = open(sys.argv[1])
for line in docFile.readlines():
  docs.append( line.replace("\n","") )

docFile.close

output = open("textMatrix.txt","w")
input = open(sys.argv[2])
c = 0
for line in input.readlines():
  output.write(docs[c] + " tfidf " + line)
  c += 1

input.close()
output.close()
