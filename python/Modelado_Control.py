import numpy as np
from pylab import *
from scipy import mgrid
from Modelo_Entidad import *
import InterfazNMF
import InterfazNMF_Control

class ControlMatrix

    @staticmethod
    def InstanceMatrix(self, path,name):
        return array(sio.loadmat(path)[name])
        
class ControlCollection:
    
    def __init__(self):
        self.__controlZentity = None
        self.__controlNMFTextual = None
        self.__controlNMFVisual = None
        self.__collection = None
    
    def __init__(self,colectionParameters):
        self.__controlZentity = None
        #Latent Topics creation
        documentList = ControlMatrix.InstanceMatrix(colectionParameters.getDocumentListPath(), colectionParameters.getDocumentListVariableName())
        #FALTA CREAR LAS MATRICES
        
        self.__controlNMFTextual = ControlNMF(self,textualF,textualH, textualVisualF, documents, 1, "Textual", "Tex")
        self.__controlNMFVisual = ControlNMF(self,VisualF,VisualH, VisualtextualF, documents, 2, "Visual", "Vis")
        
        #Collection creation
        textualFeatures = ControlMatrix.InstanceMatrix(colectionParameters.getTextualFeaturesPath(), colectionParameters.getTextualFeaturesVariableName())
        termDocumentMatrix = ControlMatrix.InstanceMatrix(colectionParameters.geTtermDocumentMatrixPath(), colectionParameters.getTermDocumentMatrixVariableName())
        documents = []
        for i in xrange(0, documentList.shape[0]):
            tags = []
            for j in xrange(0, textualFeatures.shape[0]):
                if(termDocumentMatrix[j,i]==1):
                    tags.add(textualFeatures[j])
            d = Document(documentList[i],tags,True)
            documents.append(d)
        
        self.__collection = Collection(documents, range(0,textualF.shape[1]), range(0,visualF.shape[1]), textualFeatures, None, colectionParameters.getDocumentsPath())

class ControlNMF:

    def __init__(self, controlCollection, f, h, mf, documents, id, name, abreviature):
        self.__controlCollection = controlCollection
        self.__controlLatentTopics = crateTypeLatentTopic(id, name, abreviature, documents, h, f, None, mf,None)
        
    def images(self)
        #FALTA
        return 0
    
    def names(self)
        #FALTA
        return 0
        
class ControlZentity:
    
    def __init__(self):
        pass
        
