from ChargeXML import chargeXML
from os.path import join
from Modelado_Exceptions import *

class TitleExtractor:
    def __init__(self,path):
        self.path = path
    
    def extract(self,idm):
        try:
            tree = chargeXML(join(self.path,str(idm)+'.txt'))
            for f in tree.findall("field"):
                if (f.get("name")=="nombre"):
                    return f.text.split('.')[0]
        except:
            raise(ErrorModelado("[ERROR] Extraction of " + str(idm) + " title failed."))
        return "No title"

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
            raise(ErrorModelado("[ERROR] Error extracting " + str(idm) + " description"))
        return "No description"

class MainCategoryExtractor:
    def __init__(self,controlNMF,LTNameSize,textualClustering):
        self.LTNameSize = LTNameSize
        self.controlNMF = controlNMF
        self.textualClustering = textualClustering
        
    def extract(self,idm):
        return "_".join(self.controlNMF.names(self.controlNMF.mostImportantLatentTopic(idm),self.LTNameSize,self.textualClustering))
        
        
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
        


