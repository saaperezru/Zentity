#http://docs.python.org/library/xml.etree.elementtree.html#id5
#http://effbot.org/zone/element.htm
#http://wiki.python.org/moin/PythonXml
import xml.etree.ElementTree as ET # Python 2.6
import nltk, sys
import numpy as N
from nltk.corpus import PlaintextCorpusReader


corpus_root = sys.argv[1]
docCollection = PlaintextCorpusReader(corpus_root, '.*')
print docCollection
tree = ET.parse("/home/juanffx/workspace/Flickr/fruits/xml/2504309.xml")

# the tree root is the toplevel html element
print tree.find("photo")
#print tree
# if you need the root element, use getroot
root = tree.getroot()

# ...manipulate tree...

tree.write("output.xml")
