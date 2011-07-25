import os,sys

if len(sys.argv) < 2:
  print "Use: makeMatrix.py source"
  sys.exit()

f = open(sys.argv[1])
output = open(sys.argv[1]+".matrix","w")
for line in f.readlines():
  parts = line.split(" ")
  reg = line.replace(parts[0]+" "+parts[1]+" ","")
  output.write(reg)
