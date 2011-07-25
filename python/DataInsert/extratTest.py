from os.path import join
from os import listdir
import sys
from ScalarProperty import ScalarProperty

def buildImageTree(idm,path,properties):
    root=Element("Image")
    for sp in properties:
        e = Element(sp.name)
        e.text = sp.extractData(idm,path)
        root.append(e)
    return root


def buildImageSTree(idArray,path,properties):
    root = Element("Images")
    for i in idArray:
        root.append(buildImageTree(i,path,properties))
    return root
    

def extractInfo(path,properties,imagesPerFile = 100):
    files = listdir(join(path,'xml'))
    idsArray = []
    for f in files:
        idsArray.append(f.split('.')[0])
    for i in range(0,len(ArrayList)/imagesPerFile)
        ElementTree(buildImageSTree(idsArray[i*imagesPerFile:((i+1)*imagesPerFile)],path,properties)).write(join(path,'ZXML','imageLot'+str(i)+'.xml'))
    ElementTree(ElementTree(buildImageSTree(((i+1)*imagesPerFile):],path,properties)).write(join(path,'ZXML','imageLot'+str(i+1)+'.xml')))

if __name__=="__main__":
    properties = []
    properties.append(ScalarProperty("Id","blabla",extractId))
    properties.append(ScalarProperty("Title","blabla",extractTitle))
    properties.append(ScalarProperty("Description","blabla",extractDescription))
    properties.append(ScalarProperty("Date_Added","blabla",extractDateAdded))
    properties.append(ScalarProperty("Date_Modified","blabla",extractDateModified))
    properties.append(ScalarProperty("Uri","blabla",extractPhotoPage))
    properties.append(ScalarProperty("Region","blabla",extractRegion))
    properties.append(ScalarProperty("City","blabla",extractCity))
    array = ["4931082597","2967202373","5536447393","5668645431"]
    ElementTree(buildImageSTree(array,"D:\Users\informed\workspace\Flickr\colombia",properties)).write(sys.argv[1])
