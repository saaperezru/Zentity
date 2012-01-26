from Modelado_Exceptions import *

class TitleExtractor:
    def __init__(self,path):
        self.path = path
    
    def extract(self,idm):
        return "No title"

class DescriptionExtractor:
    def __init__(self,path):
        self.path = path
    def extract(self,idm):
        return "No description"

class MainCategoryExtractor:
    def __init__(self,controlNMF,LTNameSize):
        self.LTNameSize = LTNameSize
        self.controlNMF = controlNMF
        
    def extract(self,idm):
        return "_".join(self.controlNMF.names(self.controlNMF.mostImportantLatentTopic(idm),self.LTNameSize))
        
        
class LatentTopicExtractor:
    def __init__(self,controlLatentTopic):
        self.LT = controlLatentTopic

    def extract(self,idm):
        return str(self.LT.getBelongingDegree(idm))


class TagExtractor:
    def __init__(self,tagValue,controlCollection):
        self.tagValue = tagValue
        self.Control = controlCollection
        
    def extract(self,idm):
        if self.tagValue in self.Control.getDocument(idm).getTags():
            return "True"
        return "False"
        
        
class ImageIdExtractor:
    def extract(self,idm):
        return idm
        


