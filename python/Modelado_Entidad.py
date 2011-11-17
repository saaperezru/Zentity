import scipy.io as sio
from numpy import *
from os.path import join
from os.path import join
from ChargeXML import chargeXML


class Matriz:
    def __init__(self,identifiacodresFilas,identificadoresColumnas,cuerpo):
        self.filas = {}
        for i in range (len(identifiacodresFilas)):
            self.filas[str(identifiacodresFilas[i])]=i
        self.columnas = {}
        for i in range (len(identificadoresColumnas)):
            self.columnas[str(identificadoresColumnas[i])]=i
        self.cuerpo=cuerpo
    def getFC(self,fila,columna):
        return self.cuerpo[self.filas[fila],self.columnas[columna]]
    def getCF(self,columna,fila):
        return self.cuerpo[self.filas[fila],self.columnas[columna]]


class DescriptionExtractor:
    def __init__(self,path):
        self.path = path
    def extract(self,idm):
        try:
            tree = chargeXML(join(self.path,'xml',str(idm)+'.txt'))
            for f in tree.findall("field"):
                if (f.get("name")=="comentario"):
                    return f.text
        except:
            print "[ERROR] Error extracting " + str(idm) + " description"
        return "No description"

class ImageIdExtractor:
    def extract(self,idm):
        return idm
class LatentTopicExtractor:
    def __init__(self,LatentTopic):
        self.LT = LatentTopic

    def extract(self,idm):
        return self.LT.getBelongingDegree(idm)

class MostImportantLatentTopicExtractor:
    def __init__(self,TypeLatentTopic):
        self.TLT = TypeLatentTopic
        
    def extract(self,idm):
        return  self.TLT.getMostImportantLatentTopic(idm).name.replace("/","___").replace("-","__")

class TagExtractor:
    def __init__(self,tagValue,Xt):
        self.tagValue = tagValue
        self.Xt=Xt
    def extract(self,idm):
        if self.Xt.getFC(idm,self.tagValue):
            return "True"
        return "False"

class TitleExtractor:
    def __init__(self,path):
        self.path = path
    
    def extract(self,idm):
        try:
            tree = chargeXML(join(self.path,'xml',str(idm)+'.txt'))
            for f in tree.findall("field"):
                if (f.get("name")=="nombre"):
                    return f.text.split('.')[0]
        except:
            print "[ERROR] Extraction of " + str(idm) + " title failed."
        return "No title"


class MatlabExtract:
    def __init__(self,path):
        self.path = path
    def getFTMatrix(self,filename = 'Ft.mat'):
        return array(sio.loadmat(join(self.path,filename))['Ft'])
    def getWTMatrix(self,filename = 'Wt.mat'):
        return array(sio.loadmat(join(self.path,filename))['Wt'])
    def getHMatrix(self,filename = 'H.mat'):
        return array(sio.loadmat(join(self.path,filename))['H_norm'])
    def getFVMatrix(self,filename = 'Fv.mat'):
        return array(sio.loadmat(join(self.path,filename))['Fv'])
    def getWVMatrix(self,filename = 'Wv.mat'):
        return array(sio.loadmat(join(self.path,filename))['Wv'])
    def getBsMatrix(self, filename = 'Bs.mat'):
        return array(sio.loadmat(join(self.path,filename))['Bs'])        

    #Array wherrre the id of images are sorted as in Xv and Xt
    def getTtMatrix(self,filename = 'Tt.mat'):
        return array(sio.loadmat(join(self.path,filename))['Tt'])
    def getSortedLTMatrix(self,filename = 'SortedLT.mat'):
        return array(sio.loadmat(join(self.path,filename))['indexSortedLT'])
    def getImgIds(self,filename = 'imgIds.mat'):
        return array(sio.loadmat(join(self.path,filename))['imgIdsTraining'])
    def getImgList(self,filename = 'imgIds.mat'):
        imgIndex = self.getImgIds(filename)
        imgList = []
        for i in range (len(imgIndex)):
            imgList.append(str(imgIndex[i][0][0].split(".")[0]))
        return imgList
    def getImgDictionary(self,filename = 'imgIds.mat'):
        imgIndex = self.getImgIds(filename)
        imgDictionary = {}
        for i in range (len(imgIndex)):
            imgDictionary[str(imgIndex[i][0][0].split(".")[0])]=i
        return imgDictionary
    