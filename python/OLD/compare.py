import os

f=open('textimages.txt','r')
for line in f:
   print line.split('.',1)[0]
