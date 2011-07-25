import nltk, sys
import numpy as N
from nltk.corpus import PlaintextCorpusReader
from scipy import sparse

def to_unicode_or_bust(obj, encoding='utf-8'):
     if isinstance(obj, basestring):
         if not isinstance(obj, unicode):
             obj = unicode(obj, encoding)
     return obj

if len(sys.argv) < 4:
  print 'Use: processText.py corpusRoot minDocFreq(=2) maxDocFreq'
  sys.exit()

# Processing: To lower, symbols removal, stopwords removal, stemming
corpus_root = sys.argv[1]
minDocFreq = float(sys.argv[2]) - 1.0
maxDocFreq = float(sys.argv[3]) + 1.0
if minDocFreq < 0:
  print 'minDocFreq: minimum number of documents in which a term must appear to be consider in the vector space model (at least 1)'
  sys.exit()
docCollection = PlaintextCorpusReader(corpus_root, '.*')
stopwordList = nltk.corpus.stopwords.words('english')
porter = nltk.PorterStemmer()

# Build the vector space 
actualWords = set(w.lower() for w in docCollection.words() )#if w.isalpha())
print len(actualWords),'different words in the corpus'
textVocab = set(w for w in actualWords if w not in stopwordList)
print len(textVocab),'after stopwords removal'
#normWords = list(set(porter.stem(t) for t in textVocab))
normWords = list(textVocab)
print len(normWords),'after stemming'
normWords.sort()
vectorSpace = dict()
for dim in range(0,len(normWords)):
    vectorSpace[normWords[dim]] = dim
docs = len(docCollection.fileids())
terms = len(vectorSpace)
print 'Vector Space Model: done',terms,'dimensions'

# Process each document in the corpus
docTermMatrix = sparse.lil_matrix((docs,terms))
documents = []
docId = 0
for docName in docCollection.fileids():
  words  = docCollection.words(docName)
  actual = [ w.lower() for w in words ] #if w.isalpha() ]
  dTerms = [ w for w in actual if w not in stopwordList ]
  #normTs = [ porter.stem(t) for t in dTerms ]
  normTs = dTerms
  for term in normTs:
    docTermMatrix[docId,vectorSpace[term]] += 1
  documents.append(docName)
  docId += 1
print 'All documents processed'

# Calculate Term Freq - Inverse Document Freq
A = sparse.coo_matrix(docTermMatrix)
docFreq = N.zeros(len(vectorSpace))
for i,j,v in zip(A.row, A.col, A.data):
  docFreq[j] += 1

upperBound = maxDocFreq
lowerBound = minDocFreq
index = dict()
dim = 0
for k in range(0,len(docFreq)):
  if docFreq[k] >= lowerBound and docFreq[k] <= upperBound:
    index[k] = dim
    dim += 1
  else:
    index[k] = -1

terms = dim
print 'Document Frequency done.',dim,' final dimensions'
docTermMatrix = sparse.lil_matrix((docs,terms))
termFreq = N.zeros(docs)
for i,j,v in zip(A.row, A.col, A.data):
  if index[j] >= 0:
    termFreq[i] += v
    docTermMatrix[i,index[j]] = 1#v*invDocFreq[j]
print 'TF-IDF computed'

# Save computed values
A = sparse.coo_matrix(docTermMatrix)
output = open('index.txt','w')
for i,j,v in zip(A.row, A.col, A.data):
  x = v
  output.write('%d %d %f\n' % (i+1, j+1, x))
output.close()

tokenList = open('tokens.txt','w')
for w in normWords:
  if index[vectorSpace[w]] >= 0:
    tokenList.write('%s %f\n' % (w,docFreq[vectorSpace[w]]))
tokenList.close()

documentList = open('documents.txt','w')
for docName in documents:
  documentList.write('%s\n' % docName)
documentList.close()
print 'All files saved'
