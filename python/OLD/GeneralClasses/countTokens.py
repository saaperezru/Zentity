num_tags = 235
tokens = []
def countTokens(tokensFile):	
	#Append the tags in  index file
	for line in open(tokensFile, 'r'):
		wordsline = line.split()
		# The tag k is stored in the k tokens.txt row in the first column
		# in the second column is the inverseDocFreq and the 3rd column
		# is the docFrec,  wish is the one to be sorted
		duple = int(float(wordsline[2])) , wordsline[0]
		tokens.append(duple)
	tokens.sort(reverse=True)
	# print tokens
	# print "The most frecuent tags are:"
	frequentTags = []
	for i in range(20): #If only want the most 10 repeated Tokens
		frequentTags.append(tokens[i])
	return frequentTags
