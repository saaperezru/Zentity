from os.path import join
from os import listdir
import sys
from ScalarProperty import ScalarProperty
from xml.etree.ElementTree import Element, ElementTree

def buildImageTree(idm,path,properties,xmlChildName):
    root=Element(xmlChildName)
    for sp in properties:
        e = Element(sp.name)
        e.text = sp.extractData(idm,path)
        root.append(e)
    return root


def buildImageSTree(idArray,path,properties,xmlParentName,xmlChildName):
    root = Element(xmlParentName)
    for i in idArray:
        root.append(buildImageTree(i,path,properties,xmlChildName))
    return root
    

def extractInfo(path,resourceType,xmlParentName,xmlChildName,imagesPerFile = 100):
    files = listdir(join(path,'xml'))
    idsArray = []
    for f in files:
        idsArray.append(f.split('.')[0])
    for i in range(0,len(idsArray)/imagesPerFile):
        print "[DEBUG] Generating ZXML file #" + str(i)
        ElementTree(buildImageSTree(idsArray[i*imagesPerFile:((i+1)*imagesPerFile)],path,resourceType.scalarProperties,xmlParentName,xmlChildName)).write(join(path,'ZXML',resourceType.ZXMLPrefix+str(i)+'.xml'))
    print "[DEBUG] Generating ZXML file #" + str(i)
    ElementTree(ElementTree(buildImageSTree(idsArray[((i+1)*imagesPerFile):],path,resourceType.scalarProperties,xmlParentName,xmlChildName)).write(join(path,'ZXML',resourceType.ZXMLPrefix+str(i+1)+'.xml')))

