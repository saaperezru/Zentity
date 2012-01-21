class Documents:
     
    def __init__(self, id, tags, selected):
        self.__id = id
        self.__tags = tags
        self.__selected = selected   
    
    #Getters for each attributes
    def getId(self):
        """ Returns the LatentTopic Id.
        """
        return self.__id
    def getTags(self):
        """ Returns the Tags of the document.
        """
        return self.__tags
    def getSelected(self):
        """ Returns True if the document is selected, False otherwise.
        """
        return self.__selected
    
   
    #set method for the only attribute that can change.
    def setSelected(self, selected):
        """ Save selected variable.
        """
        self.__selected = selected
   


class Collection:
     
    def __init__(self, documents, selectedTextualLatentTopics, selectedVisualLatentTopics, textualFeatures,modelName, documentsPath):
        self.__documents = documents
        self.__selectedTextualLatentTopics = selectedTextualLatentTopics
        self.__selectedVisualLatentTopics = selectedVisualLatentTopics
        self.__textualFeatures = textualFeatures 
        self.__modelName = modelName
        self.__documentsPath = documentsPath   
    
    #Getters for each attributes
    def getDocuments(self):
        """ Returns the complete array of documents.
        """
        return self.__documents
    def getSelectedTextualLatentTopics(self):
        """ Returns the selected latent topics.
        """
        return self.__selectedTextualLatentTopics
    def getSelectedVisualLatentTopics(self):
        """ Returns the selected latent topics.
        """
        return self.__selectedVisualLatentTopics
    def getTextualFeatures(self):
        """ Returns the textual words used.
        """
        return self.__textualFeatures
    def getModelName(self):
        """ Returns the model name.
        """
        return self.__modelName
    def getDocumentsPath(self):
        """ Returns the images path in string format.
        """
        return self.__documentsPath
    
   
    #set method for the only attribute that can change.
    def setModelName(self, modelName):
        """ Save modelName variable.
        """
        self.__modelName = modelName
    def setSelectedTextualLatentTopics(self, selectedTextualLatentTopics):
        """ Save selectedTextualLatentTopics variable.
        """
        self.__selectedTextualLatentTopics = selectedTextualLatentTopics
    def setSelectedVisualLatentTopics(self, selectedVisualLatentTopics):
        """ Save selectedVisualLatentTopics variable.
        """
        self.__selectedVisualLatentTopics = selectedVisualLatentTopics

class CollectionParameters:
     
    def __init__(self):
        self.__documentListPath = None
        self.__documentListVariableName = None
        self.__textualFeaturesPath = None
        self.__textualFeaturesVariableName = None
        self.__termDocumentMatrixPath = None
        self.__termDocumentMatrixVariableName = None
        self.__documentsPath = None
        self.__textualFPath = None
        self.__textualFVariableName = None
        self.__textualHPath = None
        self.__textualHVariableName = None
        self.__textualVisualFPath = None
        self.__textualVisualFVariableName = None
        self.__visualFPath = None
        self.__visualFVariableName = None
        self.__visualHPath = None
        self.__visualHVariableName = None
        self.__visualTextualFPath = None
        self.__visualTextualFVariableName = None
        
        
    #Getters for each attributes
    def getDocumentListPath(self):
        """ Returns the path of the document list.
        """
        return self.__documentListPath
    def getDocumentListVariableName(self):
        """ Returns the name of the document list variable.
        """
        return self.__documentListVariableName
    def getTextualFeaturesPath(self):
        """ Returns the path of the textual words.
        """
        return self.__textualFeaturesPath
    def getTextualFeaturesVariableName(self):
        """ Returns the variable name of the textualFeatures matrix.
        """
        return self.__textualFeaturesVariableName
    def getTermDocumentMatrixPath(self):
        """ Returns the path of the term vs Document Matrix.
        """
        return self.__termDocumentMatrixPath
    def getTermDocumentMatrixVariableName(self):
        """ Returns the variable name of the term vs Document matrix.
        """
        return self.__termDocumentMatrixVariableName
    def getDocumentsPath(self):
        """ Returns the path of the documents folder.
        """
        return self.__documentsPath
    def getTextualFPath(self):
        """ Returns the path of the textual F matrix.
        """
        return self.__textualFPath
    def getTextualFVariableName(self):
        """ Returns the variable name of the textual F matrix.
        """
        return self.__textualFVariableName
    def getTextualHPath(self):
        """ Returns the path of the textual H matrix.
        """
        return self.__textualHPath
    def getTextualHVariableName(self):
        """ Returns the variable name of the textual H matrix.
        """
        return self.__textualHVariableName
    def getTextualVisualFPath(self):
        """ Returns the path of the visual matrix F in the asymmetric NMF.
        """
        return self.__textualVisualFPath
    def getTextualVisualFVariableName(self):
        """ Returns the variable name of the visual matrix F in the asymmetric NMF.
        """
        return self.__textualVisualFVariableName
    def getVisualFPath(self):
        """ Returns the path of the visual F matrix.
        """
        return self.__visualFPath
    def getVisualFVariableName(self):
        """ Returns the variable name of the visual F matrix.
        """
        return self.__visualFVariableName
    def getVisualHPath(self):
        """ Returns the path of the visual H matrix.
        """
        return self.__visualHPath
    def getVisualHVariableName(self):
        """ Returns the variable name of the visual H matrix.
        """
        return self.__visualHVariableName
    def getVisualTextualFPath(self):
        """ Returns the path of the textual matrix F in the asymmetric NMF.
        """
        return self.__visualTextualFPath
    def getVisualTextualFVariableName(self):
        """ Returns the variable name of the textual matrix F in the asymmetric NMF.
        """
        return self.__visualTextualFVariableName
    
   
    #set method for the only attribute that can change.
    def setDocumentListPath(self, documentListPath):
        """ Save documentListPath variable.
        """
        self.__documentListPath = documentListPath
    def setDocumentListVariableName(self, documentListVariableName):
        """ Save documentListVariableName variable.
        """
        self.__documentListVariableName = documentListVariableName
    def setTextualFeaturesPath(self, textualFeaturesPath):
        """ Save textualFeaturesPath variable.
        """
        self.__textualFeaturesPath = textualFeaturesPath
    def setTextualFeaturesVariableName(self, textualFeaturesVariableName):
        """ Save textualFeaturesVariableName variable.
        """
        self.__textualFeaturesVariableName = textualFeaturesVariableName
    def setTermDocumentMatrixPath(self, termDocumentMatrixPath):
        """ Save termDocumentMatrixPath variable.
        """
        self.__termDocumentMatrixPath = termDocumentMatrixPath
    def setTermDocumentMatrixVariableName(self, termDocumentMatrixVariableName):
        """ Save termDocumentMatrixVariableName variable.
        """
        self.__termDocumentMatrixVariableName = termDocumentMatrixVariableName
    def setDocumentsPath(self, documentsPath):
        """ Save termDocumentMatrixPath variable.
        """
        self.__documentsPath = documentsPath
    def setTextualFPath(self, textualFPath):
        """ Save textualFPathvariable variable.
        """
        self.__textualFPath = textualFPath
    def setTextualFVariableName(self, textualFVariableName):
        """ Save textualFVariableName variable.
        """
        self.__textualFVariableName = textualFVariableName
    def setTextualHPath(self, textualHPath):
        """ Save textualHPathvariable variable.
        """
        self.__textualHPath = textualHPath
    def setTextualHVariableName(self, textualHVariableName):
        """ Save textualFVariableName variable.
        """
        self.__textualHVariableName = textualHVariableName
    def setTextualVisualFPath(self, textualVisualFPath):
        """ Save textualVisualFPath variable.
        """
        self.__textualVisualFPath = textualVisualFPath
    def setTextualVisualFVariableName(self, textualVisualFVariableName):
        """ Save textualVisualFVariableName variable.
        """
        self.__textualVisualFVariableName = textualVisualFVariableName
    def setVisualFPath(self, visualFPath):
        """ Save visualFPathvariable variable.
        """
        self.__visualFPath = visualFPath
    def setVisualFVariableName(self, visualFVariableName):
        """ Save visualFVariableName variable.
        """
        self.__visualFVariableName = visualFVariableName
    def setVisualHPath(self, visualHPath):
        """ Save visualHPathvariable variable.
        """
        self.__visualHPath = visualHPath
    def setVisualHVariableName(self, visualHVariableName):
        """ Save visualFVariableName variable.
        """
        self.__visualHVariableName = visualHVariableName
    def setVisualTextualFPath(self, visualTextualFPath):
        """ Save visualtextualFPath variable.
        """
        self.__visualTextualFPath = visualTextualFPath
    def setVisualTextualFVariableName(self, visualTextualFVariableName):
        """ Save textualVisualFVariableName variable.
        """
        self.__visualTextualFVariableName = visualTextualFVariableName



#old version

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
    