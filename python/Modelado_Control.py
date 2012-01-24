import numpy as np
from pylab import *
from scipy import mgrid
from Modelado_Entidad import *
import InterfazNMF_Control as IC

class ControlMatrix:

    @staticmethod
    def InstanceMatrix(path,name):
        return array(sio.loadmat(path)[name])
        
class ControlCollection:
    
    def __init__(self):
        self.__controlZentity = None
        self.__controlNMFTextual = None
        self.__controlNMFVisual = None
        self.__collection = None
    
    def beginCollection(self,colectionParameters):
        #try:
        self.__controlZentity = None
        
        #Latent Topics creation
        documentList = ControlMatrix.InstanceMatrix(colectionParameters.getDocumentListPath(), colectionParameters.getDocumentListVariableName())
        textualF = ControlMatrix.InstanceMatrix(colectionParameters.getTextualFPath(), colectionParameters.getTextualFVariableName()) 
        textualH = ControlMatrix.InstanceMatrix(colectionParameters.getTextualHPath(), colectionParameters.getTextualHVariableName())
        textualVisualF = ControlMatrix.InstanceMatrix(colectionParameters.getTextualVisualFPath(), colectionParameters.getTextualVisualFVariableName())
        self.__controlNMFTextual = ControlNMF(self,textualF,textualH, textualVisualF, documentList, 1, "Textual", "Tex")
        
            
        return True
        #except:
            #self.__controlZentity = None
            #self.__controlNMFTextual = None
            #self.__controlNMFVisual = None
            #self.__collection = None
            #print "Error-creation"
            #return False
        
    def imageInfo():
        if(self.__collection == None):
            return None
        else:
            return (self.__collection.getDocuments(),self.__collection.getDocumentsPath())
    def latentTopicsInfo():
        if(self.__collection == None or self.__controlNMFTextual == None):
            return None
        else:
            #FALTA
            return (self.__collection.getTextualFeatures(),self.__collection.getDocuments(),self.__collection.getDocumentsPath())
            
class ControlNMF:

    def __init__(self, controlCollection, f, h, mf, documents, id, name, abreviature):
        self.__controlCollection = controlCollection
        self.__controlLatentTopics = IC.ControlTypeLatentTopic(id, name, abreviature, documents, h, f, None, mf,None)
        if (self.__controlLatentTopics == None):
            raise Exception()
        
    def images(self):
        pass
    
    def names(self):
        pass
        
class ControlZentity:
    
    def __init__(self):
        pass
        
