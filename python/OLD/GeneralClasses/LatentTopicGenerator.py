from extractMatlabMatrix import MatlabExtract
from os import mkdir
from os.path import join
import subprocess
import shlex

class LatentTopic:
    def __init__(self,ids,name,belongingVector,imgDictionary):
        self.id = ids
        self.name = name
        self.belongingVector = belongingVector
        self.imgDictionary = imgDictionary
        self.cardinality = sum(belongingVector)
    def getBelongingDegree(self,imgId):
        return str(round(self.belongingVector[self.imgDictionary[str(imgId)]],6))

class LatentTopicGenerator:
    def __init__(self,path):
    #Path is the path of the matlab files
        self.path = path
        self.MLExtract = MatlabExtract(path)
        self.Tt = self.MLExtract.getTtMatrix()

    def getLatentTopics(self, numberOfTermsByLT = 20):
        H = self.MLExtract.getHMatrix()
        LT = []
        imgD = self.MLExtract.getImgDictionary()
        for i in range(len(self.Tt[0])):
            LTName = self.getLTName(i,numberOfTermsByLT)
            LT.append(LatentTopic(i,LTName,H[i],imgD))
        return LT
    def getLatentTopicsTFIDF(self, numberOfTermsByLT = 5):
        H = self.MLExtract.getHMatrix()
        LT = []
        imgD = self.MLExtract.getImgDictionary()
        for i in range(len(self.Tt[0])):
            LTName = self.getLTName(i,numberOfTermsByLT)
            LT.append(LatentTopic(i,LTName,H[i],imgD))
        return LT

    def getLTName(self,LTID,numberOfTermsByLT= 20):
        LTName = ""
        for j in range(numberOfTermsByLT):
                LTName += str(self.Tt[j][LTID][0]) + "_"
        return LTName
    #Do not use, deprecated, useless:
    def getLTOldName(self,LTID,numberOfTermsByLT = 5):
        LTName = ""
        for j in range(numberOfTermsByLT):
                LTName += str(self.Tt[LTID][j][0]) + "_"
        return LTName
    #End of useless

    def getLTNameCardinality(self,LTID,cardinality):
    #Gets the most significant terms that sum to cardinality when 
        FT = self.MLExtract.getFTSortedMatrix()
        numberOfTermsByLT = 0
        while(cardinality>0):
            cardinality = cardinality - FT[numberOfTermsByLT][LTID]
            numberOfTermsByLT = numberOfTermsByLT + 1
        numberOfTermsByLT = numberOfTermsByLT - 1
        LTName = ""
        for j in range(numberOfTermsByLT):
                LTName += str(self.Tt[j][LTID][0]) + "_"
        return LTName
    def changeLTNames(LTID, newName):
        return newName
    def generateLTDocs(self):
        LTs = self.getLatentTopics()
        LTDocsDirectory = "LatentTopicsDocuments"
        try:
            mkdir(join(self.path,LTDocsDirectory))
        except OSError:
            print "[NOTICE] " + LTDocsDirectory + " directory already exists"
        for LT in LTs:
            f = open(join(self.path,LTDocsDirectory,'LT'+str(LT.id)+'.txt'), 'w')
            #print LT.name
            f.write(LT.name.replace('_',' '))
            #f = open(join(self.path,LTDocsDirectory,'LT'+str(LT.id)+'.txt'), 'r')
            #print f.read()
            f.close()    
    def tfidfLTDocs(self, TagsofNewName):
        args = "C:/Python26/python.exe "+self.path+"/processTextsTFIDF.py "+join(self.path,"\\LatentTopicsDocuments") + " 2 100"
        args = shlex.split(args)
        print args        
        hijo = subprocess.Popen(args)
        LTs = self.getLatentTopics()
        LTDocsDirectory = "LatentTopicsDocuments"       
        HashTableTags = {}
        for line in open('tokens.txt', 'r'):
            wordsline = line.split()
            HashTableTags[wordsline[0]]= int(float(wordsline[2]))
        print HashTableTags
        for LT in LTs:
            NewName = []
            f = open(join(self.path,LTDocsDirectory,'LT'+str(LT.id)+'.txt'), 'r')
            NewName = shlex.split(f.read())
            print NewName, "\n"
            f = open(join(self.path,LTDocsDirectory,'LT'+str(LT.id)+'.txt'), 'w')
            f.write(LT.name.replace('_',' '))
            
x=LatentTopicGenerator("C:/Users/informed/Dropbox2/Dropbox/zentity/scripts/python/GeneralClasses")
x.generateLTDocs()
x.tfidfLTDocs(5)        
