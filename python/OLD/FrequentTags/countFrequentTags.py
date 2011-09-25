from operator import itemgetter
num_tags = 235
tags = []
frec_tags = [[],[]]

#Append the tags in  index file
for line in open('index.txt', 'r'):
    wordsline = line.split()
    # The tag k asociated with the image j is stored
    # in the second column of the index file
    tags.append(int(wordsline[1]))
tags.sort()
print tags
#Counting the number of ocurrences of the i tag in the array of tags
for i in range(num_tags):
    duple = tags.count(i), i
    frec_tags.append(duple)  
print frec_tags
frec_tags.sort(reverse=True)
print frec_tags

print "The most frecuent tags are:"
for i in range(1,7): #If only want the most 20 repeated tags
    print frec_tags[i]
