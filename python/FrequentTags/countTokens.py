num_tags = 235
tokens = []

#Append the tags in  index file
for line in open('tokens.txt', 'r'):
    wordsline = line.split()
    # The tag k is stored in the k tokens.txt row in the first column
    # in the second column is the inverseDocFreq and the 3rd column
    # is the docFrec,  wish is the one to be sorted
    duple = int(float(wordsline[2])) , wordsline[0]
    tokens.append(duple)
tokens.sort(reverse=True)
print tokens
print "The most frecuent tags are:"
for i in range(1,10): #If only want the most 10 repeated Tokens
    print tokens[i]
